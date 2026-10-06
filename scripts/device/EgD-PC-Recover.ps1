# EgD-PC-Recover.ps1 - EVEglyphDesign device space and memory recovery (EgD-DEV-001)
# Windows PowerShell 5.1. Three modes, one at a time:
#   -Mode Measure  (default) read only: RAM, disks, top processes, Dino/large files. Changes nothing.
#   -Mode Archive  copy the archive list to Google Drive for desktop under
#                  "My Drive\PC Archive - Oct 2026\<Lane>", MD5 every file, write manifest. Deletes nothing.
#   -Mode Remove   delete local copies ONLY for manifest rows that the agent marked verified=yes
#                  against Drive's own MD5. Asks for YES first.
# Precedent: pc-space-recovery (upload, verify, then approve removal); DIN-2026-10-02-03 (one file, one line).
# Inverse: Measure and Archive are reversible (delete the Drive copy). Remove is irreversible locally;
#          the Drive copy with matching MD5 is the restore path.
param(
  [ValidateSet('Measure','Archive','Remove')][string]$Mode = 'Measure',
  [string]$Lane = 'Dino',
  [string]$Manifest = ''
)
$ErrorActionPreference = 'Continue'
$ts   = Get-Date -Format 'yyyyMMdd-HHmmss'
$out  = Join-Path $env:USERPROFILE 'Downloads\EgD-PC-Recovery'
New-Item -ItemType Directory -Force -Path $out | Out-Null
$rep  = Join-Path $out "report-$Mode-$ts.txt"
function W($s){ $s | Tee-Object -FilePath $rep -Append }

# Locate Google Drive for desktop "My Drive"
$myDrive = $null
foreach($d in (Get-PSDrive -PSProvider FileSystem)){
  $p = Join-Path $d.Root 'My Drive'
  if(Test-Path $p){ $myDrive = $p; break }
}
$dest = if($myDrive){ Join-Path $myDrive "PC Archive - Oct 2026\$Lane" } else { $null }

# Dino archive list: patterns from dino-importtwin intake addenda 01, 02, 06
$roots = @('Downloads','Desktop','Documents') | % { Join-Path $env:USERPROFILE $_ }
$dinoPat = 'Dino|ImportTwin|Blueprint|repo-sync|DICSA|PRIMA|COI10|ADMINCOI|EMPRE|ASIGNACIONES|service-orders|drive-manifest|email-index|CFDI|pedimento|\.pst$|\.FDB$'

if($Mode -eq 'Measure'){
  W "EgD-PC-Recover Measure $ts  host=$env:COMPUTERNAME"
  $os = Get-CimInstance Win32_OperatingSystem
  W ("RAM GB total {0:N1} free {1:N1}" -f ($os.TotalVisibleMemorySize/1MB), ($os.FreePhysicalMemory/1MB))
  W ("Commit GB limit {0:N1} free {1:N1}" -f ($os.TotalVirtualMemorySize/1MB), ($os.FreeVirtualMemory/1MB))
  Get-PSDrive -PSProvider FileSystem | % { W ("Disk {0}: used {1:N1} GB free {2:N1} GB" -f $_.Name, ($_.Used/1GB), ($_.Free/1GB)) }
  W "GoogleDrive MyDrive = $myDrive"
  W "`n== Top 20 processes by memory (MB, count) =="
  Get-Process | Group-Object ProcessName | % {
    [pscustomobject]@{Name=$_.Name; Count=$_.Count; MB=[int](($_.Group | Measure-Object WorkingSet64 -Sum).Sum/1MB)}
  } | Sort-Object MB -Descending | Select-Object -First 20 | Format-Table -AutoSize | Out-String -Width 160 | % { W $_ }
  W "== Startup entries =="
  Get-CimInstance Win32_StartupCommand | Select-Object Name, Location | Format-Table -AutoSize | Out-String -Width 160 | % { W $_ }
  W "== Folder sizes (GB) =="
  $extra = @("$env:LOCALAPPDATA\Google\DriveFS", "$env:LOCALAPPDATA\Microsoft\Outlook", "$env:USERPROFILE\AppData\Local\Temp")
  foreach($f in ($roots + $extra)){
    if(Test-Path $f){ $s = (Get-ChildItem $f -Recurse -File -Force -EA SilentlyContinue | Measure-Object Length -Sum).Sum; W ("{0,8:N2}  {1}" -f ($s/1GB), $f) }
  }
  W "`n== Dino-lane candidates (path | GB | modified) =="
  $cand = foreach($r in $roots){ Get-ChildItem $r -Recurse -File -Force -EA SilentlyContinue | ? { $_.FullName -match $dinoPat -and $_.FullName -notmatch '\\\.tmp\.driveupload\\' } }
  $cand | Sort-Object Length -Descending | % { W ("{0} | {1:N3} | {2:yyyy-MM-dd HH:mm}" -f $_.FullName, ($_.Length/1GB), $_.LastWriteTime) }
  W ("Dino candidates total GB {0:N2}" -f (($cand | Measure-Object Length -Sum).Sum/1GB))
  W "`n== 40 largest files in Downloads/Desktop/Documents =="
  $(foreach($r in $roots){ Get-ChildItem $r -Recurse -File -Force -EA SilentlyContinue }) | Sort-Object Length -Descending | Select-Object -First 40 | % { W ("{0:N2} GB | {1}" -f ($_.Length/1GB), $_.FullName) }
  W "`n== Incomplete downloads (.crdownload / .partial) =="
  $(foreach($r in $roots){ Get-ChildItem $r -Recurse -File -Force -Include *.crdownload,*.partial -EA SilentlyContinue }) | % { W ("{0:N2} GB | {1}" -f ($_.Length/1GB), $_.FullName) }
  W "== Outlook data files attached =="
  try { $ol = [Runtime.InteropServices.Marshal]::GetActiveObject('Outlook.Application'); foreach($st in $ol.Session.Stores){ W $st.FilePath } } catch { W "Outlook not running (attached PSTs not listed)" }
  # list for Archive mode: Dino candidates, excluding PSTs (originals already in Drive, Correo Dino) and in-flight files
  $list = Join-Path $out "archive-list-$Lane.txt"
  $cand | ? { $_.Extension -notin '.pst','.crdownload','.partial','.tmp' } | % { $_.FullName } | Set-Content -Encoding UTF8 $list
  W "`nArchive list written: $list"
}

if($Mode -eq 'Archive'){
  if(-not $dest){ W "STOP: Google Drive for desktop 'My Drive' not mounted. Nothing copied."; exit 2 }
  $list = Join-Path $out "archive-list-$Lane.txt"
  if(-not (Test-Path $list)){ W "STOP: run -Mode Measure first."; exit 2 }
  New-Item -ItemType Directory -Force -Path $dest | Out-Null
  $man = Join-Path $out "manifest-$Lane-$ts.csv"
  $rows = foreach($src in (Get-Content $list)){
    if(-not (Test-Path $src)){ continue }
    $rel = $src.Substring($env:USERPROFILE.Length).TrimStart('\')
    $tgt = Join-Path $dest $rel
    New-Item -ItemType Directory -Force -Path (Split-Path $tgt) | Out-Null
    Copy-Item -LiteralPath $src -Destination $tgt -Force
    $m = (Get-FileHash -LiteralPath $src -Algorithm MD5).Hash.ToLower()
    [pscustomobject]@{source=$src; drive_path="PC Archive - Oct 2026/$Lane/" + ($rel -replace '\\','/'); bytes=(Get-Item -LiteralPath $src).Length; md5=$m; verified='pending'}
  }
  $rows | Export-Csv -NoTypeInformation -Encoding UTF8 $man
  Copy-Item $man (Join-Path $dest '_manifest.csv') -Force
  W "Archived $($rows.Count) files to $dest. Manifest: $man (also in Drive as _manifest.csv). Nothing deleted."
  W "Next: the agent checks each MD5 against Drive and marks verified=yes."
}

if($Mode -eq 'Remove'){
  if(-not (Test-Path $Manifest)){ W "STOP: pass -Manifest <verified manifest path>."; exit 2 }
  $ok = Import-Csv $Manifest | ? { $_.verified -eq 'yes' }
  $gb = ($ok | % { [double]$_.bytes } | Measure-Object -Sum).Sum/1GB
  $a = Read-Host ("Delete {0} local files ({1:N2} GB) whose Drive copy is MD5-verified? Type YES" -f $ok.Count, $gb)
  if($a -ne 'YES'){ W "Cancelled. Nothing deleted."; exit 0 }
  foreach($r in $ok){
    if((Get-FileHash -LiteralPath $r.source -Algorithm MD5).Hash.ToLower() -eq $r.md5){ Remove-Item -LiteralPath $r.source -Force; W "removed $($r.source)" }
    else { W "KEPT (changed since archive) $($r.source)" }
  }
}
W "Report: $rep"
if($dest){ $rd = Join-Path $dest '_reports'; New-Item -ItemType Directory -Force -Path $rd | Out-Null; Copy-Item $rep $rd -Force }
