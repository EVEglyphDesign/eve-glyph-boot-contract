#!/usr/bin/env python3
"""Render EgD-STR-001.md into the public /strategy/ page. Single source of truth."""
import re, hashlib

SRC = "/home/user/workspace/ebc/docs/strategy/EgD-STR-001.md"
OUT = "/home/user/workspace/ebc/docs/strategy/index.html"
RAW = open(SRC, encoding="utf-8").read()
SHA = hashlib.sha256(RAW.encode("utf-8")).hexdigest()
DECK = ("How EVEglyph Design gets read, checked and cited by people who already hold the audience we need — without buying attention and without a content programme.")


def inline(s):
    s = s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"`([^`]+?)`", r"<code>\1</code>", s)
    s = re.sub(r"\[([^\]]+?)\]\((https?://[^)]+?)\)", r'<a href="\2">\1</a>', s)
    s = re.sub(r"(?<!\*)\*([^*]+?)\*(?!\*)", r"<i>\1</i>", s)
    return s


def body(md):
    out, para, lst, i = [], [], None, 0
    lines = md.split("\n")
    seen = False

    def fp():
        nonlocal para
        if para:
            out.append("<p>" + inline(" ".join(para)) + "</p>"); para = []

    def fl():
        nonlocal lst
        if lst:
            tag = lst[0]
            out.append(f"<{tag}>" + "".join(f"<li>{x}</li>" for x in lst[1]) + f"</{tag}>")
            lst = None

    while i < len(lines):
        ln = lines[i].rstrip()
        if ln.startswith("# "):
            seen = True; i += 1; continue
        if not seen or ln.startswith("**Document ID**") or ln.startswith("©") \
           or ln.startswith("*Pour") or ln.strip() == "---":
            i += 1; continue
        if ln.startswith("> "):
            fp(); fl()
            q = [ln[2:]]
            while i + 1 < len(lines) and lines[i+1].startswith("> "):
                i += 1; q.append(lines[i][2:])
            out.append("<blockquote><p>" + inline(" ".join(q)) + "</p></blockquote>")
            i += 1; continue
        if ln.startswith("### "):
            fp(); fl(); out.append("<h3>" + inline(ln[4:]) + "</h3>"); i += 1; continue
        if ln.startswith("## "):
            fp(); fl(); out.append("<h2>" + inline(ln[3:]) + "</h2>"); i += 1; continue
        m = re.match(r"^(\d+)\. (.*)", ln)
        if ln.startswith("- ") or m:
            fp()
            tag = "ol" if m else "ul"
            txt = m.group(2) if m else ln[2:]
            while i + 1 < len(lines) and lines[i+1].startswith("  ") and lines[i+1].strip():
                i += 1; txt += " " + lines[i].strip()
            if not lst or lst[0] != tag:
                fl(); lst = (tag, [])
            lst[1].append(inline(txt))
            i += 1; continue
        if not ln.strip():
            fp(); fl(); i += 1; continue
        para.append(ln.strip()); i += 1
    fp(); fl()
    return "\n".join(out)


HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>The Review Path \u2014 EgD-STR-001 \u00b7 EVEglyphDesign</title>
<meta name="description" content="%(deck)s">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,700&family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
<style>
:root{--cream:#fdfaf4;--cream2:#f7f2e7;--ink:#1a1a1a;--line:#e7e1d3;--mute:#6b665c;--accent:#e87722}
*{box-sizing:border-box}
body{margin:0;background:var(--cream);color:var(--ink);font:400 17px/1.62 Inter,system-ui,sans-serif;-webkit-font-smoothing:antialiased}
.wrap{max-width:760px;margin:0 auto;padding:0 24px}
header.top{border-bottom:1px solid var(--line);padding:18px 0;font-size:13px;letter-spacing:.04em}
header.top a{color:var(--mute);text-decoration:none}
header.top a:hover{color:var(--accent)}
.hero{padding:64px 0 40px;border-bottom:1px solid var(--line)}
.kicker{font:600 12px/1 Inter;letter-spacing:.22em;text-transform:uppercase;color:var(--accent);margin:0 0 20px}
h1{font:700 clamp(38px,7vw,60px)/1.04 Fraunces,Georgia,serif;margin:0 0 8px;letter-spacing:-.015em}
.rule{width:120px;height:3px;background:var(--accent);margin:22px 0 26px}
.deck{font:400 21px/1.5 Fraunces,Georgia,serif;color:var(--mute);margin:0 0 28px;max-width:38em}
.meta{font-size:12.5px;color:var(--mute);line-height:1.9}
.meta b{color:var(--ink);font-weight:600}
.meta code{font-size:11.5px;word-break:break-all}
.cta{display:flex;flex-wrap:wrap;gap:12px;margin:30px 0 0}
.btn{display:inline-block;padding:13px 22px;background:var(--accent);color:#fff;text-decoration:none;font:600 14px/1 Inter;letter-spacing:.02em}
.btn:hover{background:#cf6716}
.btn.ghost{background:transparent;color:var(--ink);border:1px solid var(--line)}
.btn.ghost:hover{border-color:var(--accent);color:var(--accent)}
main{padding:14px 0 10px}
h2{font:700 25px/1.25 Fraunces,Georgia,serif;margin:52px 0 4px;padding-top:22px;border-top:2px solid var(--accent)}
h3{font:700 17.5px/1.35 Fraunces,Georgia,serif;margin:30px 0 2px}
p{margin:0 0 16px}
blockquote{margin:30px 0;padding:18px 22px;background:var(--cream2);border-left:3px solid var(--accent);font:400 19px/1.55 Fraunces,Georgia,serif}
blockquote p{margin:0}
ul,ol{margin:0 0 18px;padding-left:22px}
li{margin:0 0 10px}
a{color:var(--accent)}
code{background:var(--cream2);padding:1px 5px;font-size:.88em}
footer{margin-top:64px;border-top:1px solid var(--line);padding:26px 0 60px;font-size:12.5px;color:var(--mute)}
footer .mark{font:400 15px/1 Fraunces,Georgia,serif;color:var(--ink);margin-top:10px}
</style>
</head>
<body>
<header class="top"><div class="wrap"><a href="../">&larr; EVEglyphDesign \u00b7 Executive Boot Contract</a></div></header>
<div class="wrap">
<section class="hero">
  <p class="kicker">EVEglyph Design \u00b7 Position Paper</p>
  <h1>The Review Path</h1>
  <div class="rule"></div>
  <p class="deck">%(deck)s</p>
  <p class="meta">
    <b>Document ID</b> EgD-STR-001 &nbsp;\u00b7&nbsp; <b>Key ID</b> EgD-KEY-2026-07 &nbsp;\u00b7&nbsp; <b>Status</b> strategy note, v1.0<br>
    <b>SHA-256 of source</b> <code>%(sha)s</code>
  </p>
  <div class="cta">
    <a class="btn" href="EVEglyphDesign_Review_Path.pdf">Read the controlled PDF &rarr;</a>
    <a class="btn ghost" href="https://eveglyphdesign.github.io/paix-parish-platform/">See it running \u2014 PAIX Parish Platform</a>
  </div>
</section>
<main>
%(body)s
</main>
<footer>
  <p>\u00a9 2026 EVEglyphDesign. All rights reserved. Controlled copy. \u00b7 Key ID EgD-KEY-2026-07 \u00b7
  <a href="EVEglyphDesign_Review_Path.pdf">Controlled PDF</a> \u00b7
  <a href="https://github.com/EVEglyphDesign/eve-glyph-boot-contract">Repository</a></p>
  <p class="mark">Pour le bien-\u00eatre du peuple.</p>
</footer>
</div>
</body>
</html>
"""

if __name__ == "__main__":
    open(OUT, "w", encoding="utf-8").write(
        HEAD % {"deck": DECK, "sha": SHA, "body": body(RAW)})
    print("wrote", OUT, SHA[:16])
