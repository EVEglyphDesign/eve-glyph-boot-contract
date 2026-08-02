#!/usr/bin/env python3
"""EgD-STR-002 public page. Renders docs/scripting/EgD-STR-002.md into the
EVEglyphDesign shell. Durable per EgD-BOOT-003 — the page is rebuilt from the
markdown, never hand-edited."""
import hashlib, re

BASE = "/home/user/workspace/ebc/docs/scripting"
SRC = f"{BASE}/EgD-STR-002.md"
HEAD = f"{BASE}/_shell.head.html"
OUT = f"{BASE}/index.html"
VERSION = "v1.2"
DECK = ("A short-form scripting method quoted from the captions and mapped "
        "clause by clause onto the EVEglyphDesign boot contract.")

RAW = open(SRC, encoding="utf-8").read()
SHA = hashlib.sha256(RAW.encode("utf-8")).hexdigest()


def smart(s):
    """Typographic quotes — GLOBAL.md §1a."""
    s = re.sub('(^|[\\s(\\[\u2014\u2013])"', '\\1\u201c', s)
    s = s.replace('"', '\u201d')
    s = re.sub(r"(?<=[A-Za-z0-9])'(?=[A-Za-z])", '\u2019', s)
    s = re.sub(r"(?<=[A-Za-z])'(?![A-Za-z])", '\u2019', s)
    s = re.sub(r"(^|[\s(\[])'", '\\1\u2018', s)
    return s


def inline(s):
    s = smart(s)
    s = s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"`([^`]+?)`", r"<code>\1</code>", s)
    s = re.sub(r"\[([^\]]+?)\]\((https?://[^)]+?)\)", r'<a href="\2">\1</a>', s)
    s = re.sub(r"(?<!\*)\*([^*]+?)\*(?!\*)", r"<i>\1</i>", s)
    return s


def render(md):
    out, lines, i = [], md.split("\n"), 0
    para, bullets, quote, seen_h1 = [], [], [], False

    def flush():
        nonlocal para, bullets, quote
        if para:
            out.append("<p>" + inline(" ".join(para)) + "</p>"); para = []
        if bullets:
            out.append("<ol>" + "".join(f"<li>{inline(b)}</li>" for b in bullets) + "</ol>")
            bullets = []
        if quote:
            out.append("<blockquote><p>" + inline(" ".join(quote)) + "</p></blockquote>")
            quote = []

    while i < len(lines):
        ln = lines[i].rstrip()
        if ln.startswith("# "):
            flush(); seen_h1 = True; i += 1; continue
        if not seen_h1:
            i += 1; continue
        if ln.startswith("**Document ID**") or ln.startswith("©") or ln.startswith("*Pour"):
            i += 1; continue
        if ln.startswith("---"):
            flush(); i += 1; continue
        if ln.startswith("## "):
            flush(); out.append("<h2>" + inline(ln[3:]) + "</h2>"); i += 1; continue
        if ln.startswith("> "):
            if para or bullets:
                flush()
            quote.append(ln[2:]); i += 1; continue
        if quote and not ln.startswith("> "):
            flush()
        if ln.startswith("|"):
            flush()
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
                cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                if not all(set(c) <= set("-: ") for c in cells):
                    rows.append(cells)
                i += 1
            head = "".join(f"<th>{inline(c)}</th>" for c in rows[0])
            body = "".join("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>"
                           for r in rows[1:])
            out.append(f"<table><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table>")
            continue
        m = re.match(r"^(\d+)\. (.*)$", ln)
        if m:
            if para:
                flush()
            txt = m.group(2)
            while i + 1 < len(lines) and lines[i + 1].startswith("   ") and lines[i + 1].strip():
                i += 1; txt += " " + lines[i].strip()
            bullets.append(txt); i += 1; continue
        if not ln.strip():
            flush(); i += 1; continue
        para.append(ln.strip()); i += 1
    flush()
    return "\n".join(out)


head = open(HEAD, encoding="utf-8").read()
canon = ('© 2026 Dany Theriault. EVE \u201cdigital stem cell\u201d glyph and glyph-based design '
         'principles — all rights reserved. Stewardship of rights of use and assignment for '
         'large public and institutional usage rests with the Pacific Utilities Design '
         'Council. Published as a time-stamped record of authorship and intent.')

html = f"""{head}
<body>
<header class="top"><div class="wrap"><a href="../">&larr; EVEglyphDesign · Executive Boot Contract</a></div></header>
<div class="wrap">
<section class="hero">
  <p class="kicker">EVEglyph Design · Strategy Note</p>
  <h1>Hook, Context, Rehook, Payoff</h1>
  <div class="rule"></div>
  <p class="deck">{DECK}</p>
  <p class="meta">
    <b>Document ID</b> EgD-STR-002 &nbsp;·&nbsp; <b>Key ID</b> EgD-KEY-2026-07 &nbsp;·&nbsp; <b>Status</b> strategy note, {VERSION}<br>
    <b>SHA-256 of source</b> <code>{SHA}</code>
  </p>
  <div class="cta">
    <a class="btn" href="EVEglyphDesign_Hook_Context_Rehook_Payoff.pdf">Read the controlled PDF &rarr;</a>
    <a class="btn ghost" href="https://github.com/EVEglyphDesign/jre-montreal-bridge/blob/main/episodes/jack-neel-052-daniel-bitton/FINDINGS.md">Full-episode findings</a>
  </div>
</section>
<main>
{render(RAW)}
</main>
<footer>
  <p class="canon">{canon}</p>
  <p>© 2026 EVEglyphDesign. All rights reserved. Controlled copy. · Key ID EgD-KEY-2026-07 ·
  <a href="EVEglyphDesign_Hook_Context_Rehook_Payoff.pdf">Controlled PDF</a> ·
  <a href="https://github.com/EVEglyphDesign/eve-glyph-boot-contract">Repository</a></p>
  <p class="mark">Pour le bien-être du peuple.</p>
</footer>
</div>
</body>
</html>
"""
open(OUT, "w", encoding="utf-8").write(html)
print("wrote", OUT, "sha", SHA[:16])
