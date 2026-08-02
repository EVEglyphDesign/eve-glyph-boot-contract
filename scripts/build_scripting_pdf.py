#!/usr/bin/env python3
"""EgD-STR-001 — The Review Path. EVEglyphDesign canon PDF."""
import hashlib, datetime, math, re, sys
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Spacer, KeepTogether, Flowable, Table, TableStyle)

W, H = LETTER
CREAM = HexColor("#fdfaf4"); CREAM2 = HexColor("#f7f2e7")
INK = HexColor("#1a1a1a"); LINE = HexColor("#e7e1d3")
ORNG = HexColor("#e87722"); MUTE = HexColor("#6b665c")

F = "/home/user/workspace/fonts"
pdfmetrics.registerFont(TTFont("Fraunces", f"{F}/Fraunces-400.ttf"))
pdfmetrics.registerFont(TTFont("Fraunces-Bold", f"{F}/Fraunces-700.ttf"))
pdfmetrics.registerFont(TTFont("Inter", f"{F}/Inter-400.ttf"))
pdfmetrics.registerFont(TTFont("Inter-SB", f"{F}/Inter-600.ttf"))
pdfmetrics.registerFont(TTFont("Inter-Bold", f"{F}/Inter-700.ttf"))

SRC = "/home/user/workspace/ebc/docs/scripting/EgD-STR-002.md"
OUT = "/home/user/workspace/ebc/docs/scripting/EVEglyphDesign_Hook_Context_Rehook_Payoff.pdf"
TS = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
DOC_ID = "EgD-STR-002"; KEY_ID = "EgD-KEY-2026-07"
TITLE = "Hook, Context, Rehook, Payoff"
VERSION = "v1.2"
SUB = ("A short-form scripting method quoted from the captions and mapped clause by clause onto the EVEglyphDesign boot contract.")
RAW = open(SRC, encoding="utf-8").read()
SHA = hashlib.sha256(RAW.encode("utf-8")).hexdigest()
PAGES = int(sys.argv[1]) if len(sys.argv) > 1 else 0

MARGIN_L, MARGIN_R = 24*mm, 24*mm
TOP, BOT = 26*mm, 24*mm
FW = W - MARGIN_L - MARGIN_R


def S(name, **kw):
    b = dict(name=name, fontName="Inter", fontSize=10, leading=15.4,
             textColor=INK, alignment=TA_LEFT, spaceAfter=0)
    b.update(kw); return ParagraphStyle(**b)


st_h1 = S("h1", fontName="Fraunces-Bold", fontSize=15, leading=19, spaceAfter=3)
st_h2 = S("h2", fontName="Fraunces-Bold", fontSize=11.6, leading=15, spaceAfter=2)
st_body = S("b", spaceAfter=8)
st_bul = S("bu", spaceAfter=6, leftIndent=13, bulletIndent=2, firstLineIndent=0)
st_quote = S("q", fontName="Fraunces", fontSize=11.2, leading=17, spaceAfter=0)
st_cap = S("cap", fontSize=7.8, leading=11.6, textColor=MUTE, spaceAfter=6)



st_th = S("th", fontName="Inter-Bold", fontSize=7.6, leading=10.6)
st_td = S("td", fontSize=7.6, leading=10.6)


def mk_table(rows, esc):
    """rows: list of list[str] markdown cells; first row is the header."""
    ncol = len(rows[0])
    _w = {3: [0.26, 0.34, 0.40], 2: [0.40, 0.60]}.get(ncol, [1.0 / ncol] * ncol)
    widths = [FW * w for w in _w]
    data = [[Paragraph(esc(c), st_th if r == 0 else st_td) for c in row]
            for r, row in enumerate(rows)]
    t = Table(data, colWidths=widths, repeatRows=1, hAlign="LEFT")
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), CREAM2),
        ("LINEBELOW", (0, 0), (-1, 0), 1.0, ORNG),
        ("LINEBELOW", (0, 1), (-1, -2), 0.5, LINE),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    return t


class Rule(Flowable):
    def __init__(self, w=FW, col=LINE, th=0.7, pad=0):
        Flowable.__init__(self); self.w = w; self.col = col; self.th = th; self.pad = pad
    def wrap(self, aw, ah): return (self.w, self.th + self.pad)
    def draw(self):
        self.canv.setStrokeColor(self.col); self.canv.setLineWidth(self.th)
        self.canv.line(0, self.pad, self.w, self.pad)


class Pull(Flowable):
    """Cream-2 panel with an orange left edge."""
    def __init__(self, text, style=st_quote, pad=9):
        Flowable.__init__(self); self.p = Paragraph(text, style); self.pad = pad
    def wrap(self, aw, ah):
        w = FW - 2*self.pad - 3
        _, h = self.p.wrap(w, ah)
        self.h = h + 2*self.pad; return (FW, self.h)
    def draw(self):
        c = self.canv
        c.setFillColor(CREAM2); c.setStrokeColor(LINE); c.setLineWidth(0.7)
        c.rect(0, 0, FW, self.h, stroke=1, fill=1)
        c.setFillColor(ORNG); c.rect(0, 0, 3, self.h, stroke=0, fill=1)
        self.p.drawOn(c, self.pad + 6, self.pad)


def smart(s):
    """Typographic quotes — GLOBAL.md §1a. Rendered output never carries straight quotes."""
    s = re.sub('(^|[\\s(\\[\u2014\u2013])"', '\\1\u201c', s)
    s = s.replace('"', '\u201d')
    s = re.sub(r"(?<=[A-Za-z0-9])'(?=[A-Za-z])", '\u2019', s)   # contractions
    s = re.sub(r"(?<=[A-Za-z])'(?![A-Za-z])", '\u2019', s)       # possessive plurals
    s = re.sub(r"(^|[\s(\[])'", '\\1\u2018', s)
    return s


def esc(s):
    s = smart(s)
    s = s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    s = re.sub(r"\*\*(.+?)\*\*", r'<font name="Inter-Bold">\1</font>', s)
    s = re.sub(r"`([^`]+?)`", r'<font name="Courier" size="8.6">\1</font>', s)
    s = re.sub(r"\[([^\]]+?)\]\((https?://[^)]+?)\)",
               r'<link href="\2" color="#e87722"><u>\1</u></link>', s)
    s = re.sub(r"(?<!\*)\*([^*]+?)\*(?!\*)", r"<i>\1</i>", s)
    return s


def parse(md):
    """Markdown subset -> flowables. Skips the H1 block; it is the cover."""
    out = []
    lines = md.split("\n")
    i = 0
    seen_h1 = False
    para = []

    def flush():
        nonlocal para
        if para:
            out.append(Paragraph(esc(" ".join(para)), st_body)); para = []

    while i < len(lines):
        ln = lines[i].rstrip()
        if ln.startswith("# "):
            flush(); seen_h1 = True; i += 1; continue
        if not seen_h1:
            i += 1; continue
        if ln.startswith("> "):
            flush()
            q = [ln[2:]]
            while i + 1 < len(lines) and lines[i+1].startswith("> "):
                i += 1; q.append(lines[i][2:])
            out.append(Spacer(1, 3)); out.append(Pull(esc(" ".join(q))))
            out.append(Spacer(1, 11)); i += 1; continue
        if ln.startswith("### "):
            flush(); out.append(Spacer(1, 6))
            out.append(KeepTogether([Paragraph(esc(ln[4:]), st_h2), Spacer(1, 3)]))
            i += 1; continue
        if ln.startswith("## "):
            flush(); out.append(Spacer(1, 12))
            out.append(KeepTogether([Rule(col=ORNG, th=1.6), Spacer(1, 6),
                                     Paragraph(esc(ln[3:]), st_h1), Spacer(1, 5)]))
            i += 1; continue
        if ln.startswith("|") and i + 1 < len(lines) and re.match(r"^\|[\s:\-|]+\|$", lines[i+1].strip()):
            flush()
            def cells(x):
                return [c.strip() for c in x.strip().strip("|").split("|")]
            rows = [cells(ln)]
            i += 2
            while i < len(lines) and lines[i].strip().startswith("|"):
                rows.append(cells(lines[i])); i += 1
            out.append(Spacer(1, 4)); out.append(mk_table(rows, esc)); out.append(Spacer(1, 12))
            continue
        if ln.strip() == "---":
            flush(); i += 1; continue
        m = re.match(r"^(\d+)\. (.*)", ln)
        if ln.startswith("- ") or m:
            flush()
            txt = m.group(2) if m else ln[2:]
            mark = f"{m.group(1)}." if m else "\u2014"
            while i + 1 < len(lines) and lines[i+1].startswith("  ") and lines[i+1].strip():
                i += 1; txt += " " + lines[i].strip()
            out.append(Paragraph(esc(txt), st_bul, bulletText=mark))
            i += 1; continue
        if not ln.strip():
            flush(); i += 1; continue
        if ln.startswith("**Document ID**") or ln.startswith("©") or ln.startswith("*Pour"):
            i += 1; continue
        para.append(ln.strip()); i += 1
    flush()
    return out


def paint(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(CREAM); canvas.rect(0, 0, W, H, stroke=0, fill=1)
    canvas.saveState()
    canvas.translate(W/2, H/2); canvas.rotate(38)
    # auto-fit the mark inside the rotated page so it can never clip an edge
    _wm, _sub = "EVEglyphDesign", "C A N O N   \u00b7   C O N T R O L L E D   C O P Y"
    _avail = 0.86 * min(W / abs(math.cos(math.radians(38))),
                        H / abs(math.sin(math.radians(38))))
    _size = min(52.0, _avail / (pdfmetrics.stringWidth(_wm, "Fraunces-Bold", 1000) / 1000.0))
    canvas.setFont("Fraunces-Bold", _size); canvas.setFillColor(HexColor("#f9f6ef"))
    canvas.drawCentredString(0, -0.30 * _size, _wm)
    _s2 = min(11.0, _avail / (pdfmetrics.stringWidth(_sub, "Inter", 1000) / 1000.0))
    canvas.setFont("Inter", _s2)
    canvas.drawCentredString(0, -0.30 * _size - 1.9 * _s2, _sub)
    canvas.restoreState()
    canvas.setFont("Inter-SB", 7); canvas.setFillColor(MUTE)
    canvas.drawString(MARGIN_L, H - 15*mm,
                      "EVEglyphDesign  \u00b7  Hook, Context, Rehook, Payoff  \u00b7  " + DOC_ID)
    canvas.drawRightString(W - MARGIN_R, H - 15*mm, KEY_ID)
    canvas.setStrokeColor(LINE); canvas.setLineWidth(0.7)
    canvas.line(MARGIN_L, H - 17*mm, W - MARGIN_R, H - 17*mm)
    canvas.line(MARGIN_L, 17*mm, W - MARGIN_R, 17*mm)
    canvas.setFont("Inter", 6.6); canvas.setFillColor(MUTE)
    canvas.drawString(MARGIN_L, 13.4*mm,
                      "\u00a9 2026 EVEglyphDesign. All rights reserved. Controlled copy.  \u00b7  "
                      + TS + "  \u00b7  SHA-256 " + SHA[:20] + "\u2026")
    canvas.drawString(MARGIN_L, 10.6*mm, "Pour le bien-\u00eatre du peuple.")
    tot = f" of {PAGES}" if PAGES else ""
    canvas.setFont("Inter-SB", 7.4)
    canvas.drawRightString(W - MARGIN_R, 13.4*mm, f"Page {canvas.getPageNumber()}{tot}")
    canvas.restoreState()


def cover(canvas, doc):
    paint(canvas, doc)
    canvas.saveState()
    y = H - 72*mm
    canvas.setFillColor(ORNG); canvas.setFont("Inter-SB", 8)
    canvas.drawString(MARGIN_L, y + 34*mm, "E V E G L Y P H D E S I G N   \u00b7   S T R A T E G Y   N O T E")
    canvas.setFillColor(INK); canvas.setFont("Fraunces-Bold", 34)
    canvas.drawString(MARGIN_L, y + 20*mm, TITLE)
    canvas.setFillColor(ORNG); canvas.rect(MARGIN_L, y + 15*mm, 42*mm, 2.4, stroke=0, fill=1)
    canvas.restoreState()


def build():
    frame = Frame(MARGIN_L, BOT, FW, H - TOP - BOT, id="f",
                  leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
    frame1 = Frame(MARGIN_L, BOT, FW, H - 66*mm - BOT, id="f1",
                   leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
    doc = BaseDocTemplate(OUT, pagesize=LETTER, title=f"{TITLE} — {DOC_ID}",
                          author="EVEglyphDesign", subject=SUB,
                          leftMargin=MARGIN_L, rightMargin=MARGIN_R,
                          topMargin=TOP, bottomMargin=BOT)
    doc.addPageTemplates([
        PageTemplate(id="cover", frames=[frame1], onPage=cover),
        PageTemplate(id="body", frames=[frame], onPage=paint),
    ])
    story = [
        Rule(), Spacer(1, 9),
        Paragraph(
            f'<font name="Inter-SB">Document ID</font>  {DOC_ID}'
            f'&nbsp;&nbsp;\u00b7&nbsp;&nbsp;<font name="Inter-SB">Key ID</font>  {KEY_ID}'
            f'&nbsp;&nbsp;\u00b7&nbsp;&nbsp;<font name="Inter-SB">Status</font>  strategy note, {VERSION}'
            f'&nbsp;&nbsp;\u00b7&nbsp;&nbsp;<font name="Inter-SB">Issued</font>  {TS}',
            st_cap),
        Paragraph(f'<font name="Inter-SB">SHA-256 of source</font>  '
                  f'<font name="Courier" size="7">{SHA}</font>', st_cap),
        Spacer(1, 4),
    ] + parse(RAW) + [
        Spacer(1, 20), Rule(), Spacer(1, 9),
        Paragraph('© 2026 Dany Theriault. EVE “digital stem cell” glyph and glyph-based design principles — all rights reserved. Stewardship of rights of use and assignment for large public and institutional usage rests with the Pacific Utilities Design Council. Published as a time-stamped record of authorship and intent.',
                  S("canonfoot", fontSize=7.4, leading=10.6, textColor=MUTE)),
    ]
    # switch to the full-height body frame after the cover page
    from reportlab.platypus import NextPageTemplate, PageBreak
    story.insert(0, NextPageTemplate("body"))
    doc.build(story)
    from pypdf import PdfReader
    return len(PdfReader(OUT).pages)


if __name__ == "__main__":
    n = build()
    print("pages", n, "stamped", PAGES, "sha", SHA[:16])
