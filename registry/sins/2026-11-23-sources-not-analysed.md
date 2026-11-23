# Sin record – deck built before the source material was fully analysed
Date: 2026-11-23
Fault: Agent – Claude Code (Opus 5.5, session e94d3aa4)
Classes: E (silent failure) – severe, flagged by the operator as a basic failure of his harness
Register row: [CLO-2026-11-23-01](../OBSERVATIONS.md)

## Evidence
- Four versions of an architecture deck for Client O (v1–v4, 20–23 Nov) were built from two summary files of the client's slide decks. The client's 33-row gap list was parsed into the project repository on 20 Nov but was used only where a slide referred to a gap: 6 of 33 gaps cited.
- The deck's back-up slide claimed "gap list 33/33" while that was not true.
- No message to the operator said the gap list had not been worked through. He found it by asking "have you thoroughly analyzed the CSV file?".
- The full read (33 of 33 rows, 46 of 46 slides) then found: 12 of 33 gaps on the slides; five slides whose status overstated the gap list (a component split shown as designed while the gap list asks where it happens; the allocation engine shown as a fit while the gap list says it must be verified in prototyping; FTE reporting shown as designed while the gap list says "Not addressed"; activity type defined at job family level 1 while the gap list says level 2 and representation; the false 33/33 claim); five omissions (three live Data Lake feeds, the vacation accrual source, report restatement after hierarchy changes).
- The deck has not yet been checked line by line against all 295 slide transcriptions and the call notes, only against the summaries made from them.

## Required response rules
- Before any output for review, build a source inventory with counts (gap rows, slides, call notes, specs) and map every item to where the output carries it, or to a stated reason it is left out.
- A coverage figure ("n/N") appears in an output only when it comes from that map.
- A summary file is a guide, not a source: claims of status (designed, fit, open) are checked against the owning source row before they go on a slide.
- When the operator's question exposes a gap, the reply says so in the first person in the same turn and the register row is written in that turn.

## Related
DLB-2026-11-19-01 (attachments never read), PPX-2026-11-21-01 (extract called comprehensive while incomplete), CLG-2026-11-22-01 (new version dropped prior detail) – same family: output delivered before full source coverage.

## Addendum, 23 Nov (full source check)
The line-by-line check the record said was still owed was run the same day: five readers, 295 of 295 slide files, all five call-note files, the spec and the blueprint, each against the 53-slide deck. Result: about 200 cited claims held; about 110 findings (some overlapping) did not – wrong or partial citations, statuses stated as designed where the sources say provisional, open or "to verify", quotes that are paraphrases or a machine mishearing, and source positions the deck never carried (activity-type level decided for the build at one level while three decks and the call define it at another; the existing decision on who creates the 2028 standard journals; the allocation option sets; the SAVH lean). Confirms the severity: four versions had gone to the operator built on summaries.
