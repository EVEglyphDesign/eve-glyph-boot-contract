#!/usr/bin/env python3
"""EVEglyphDesign — The Universal Boot Contract (LinkedIn edition)."""
import hashlib, datetime, os
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Spacer, Table, TableStyle, KeepTogether, Flowable, PageBreak)

F = "/home/user/workspace/fonts"
for n, f in [("Fraunces", "Fraunces-SemiBold.ttf"), ("Fraunces-Bd", "Fraunces-Bold.ttf"),
             ("Inter", "Inter-Regular.ttf"), ("Inter-Md", "Inter-Medium.ttf"),
             ("Inter-Bd", "Inter-Bold.ttf")]:
    pdfmetrics.registerFont(TTFont(n, os.path.join(F, f)))
pdfmetrics.registerFontFamily("Inter", normal="Inter", bold="Inter-Bd", italic="Inter", boldItalic="Inter-Bd")

CREAM, CREAM2 = HexColor("#fdfaf4"), HexColor("#f7f2e7")
INK, LINE, MUTE, ACCENT = HexColor("#1a1a1a"), HexColor("#e7e1d3"), HexColor("#6b665c"), HexColor("#e87722")

TS = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
KEYID = "EgD-KEY-2026-07"
OUT = "/home/user/workspace/EVEglyphDesign_Universal_Boot_Contract.pdf"

# ---------------------------------------------------------------- styles
def S(name, **kw):
    base = dict(name=name, fontName="Inter", fontSize=9.6, leading=14.6, textColor=INK,
                alignment=TA_LEFT, spaceAfter=0)
    base.update(kw)
    return ParagraphStyle(**base)

st_kicker = S("k", fontName="Inter-Bd", fontSize=7.6, leading=10, textColor=ACCENT, spaceAfter=8)
st_title  = S("t", fontName="Fraunces-Bd", fontSize=27, leading=30, spaceAfter=7)
st_sub    = S("s", fontSize=10.6, leading=16, textColor=MUTE, spaceAfter=14)
st_lede   = S("l", fontName="Fraunces", fontSize=12.4, leading=18.5, spaceAfter=13)
st_h      = S("h", fontName="Fraunces-Bd", fontSize=11.4, leading=14, spaceAfter=4)
st_body   = S("b", spaceAfter=9)
st_small  = S("sm", fontSize=8.6, leading=13, textColor=MUTE, spaceAfter=7)
st_cell   = S("c", fontSize=8.8, leading=12.4)
st_cellb  = S("cb", fontName="Inter-Bd", fontSize=8.8, leading=12.4)
st_cellm  = S("cm", fontSize=8.8, leading=12.4, textColor=MUTE)
st_quote  = S("q", fontName="Inter-Md", fontSize=9.6, leading=15, textColor=INK)
st_h2     = S("h2", fontName="Fraunces-Bd", fontSize=14, leading=17, spaceAfter=9)

class Rule(Flowable):
    def __init__(self, w, color=LINE, thick=0.6, pad=0):
        self.w, self.color, self.thick, self.pad = w, color, thick, pad
    def wrap(self, aw, ah):
        self.w = aw
        return (aw, self.thick + self.pad)
    def draw(self):
        self.canv.setStrokeColor(self.color); self.canv.setLineWidth(self.thick)
        self.canv.line(0, self.pad / 2, self.w, self.pad / 2)

def clause(num, head, body_html):
    n = Paragraph(f'<font name="Inter-Bd" color="#e87722" size="8">{num}</font>', st_small)
    t = Table([[n], [Paragraph(head, st_h)], [Paragraph(body_html, st_body)]],
              colWidths=[6.9 * inch], style=TableStyle([
                  ("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                  ("TOPPADDING", (0, 0), (-1, -1), 0), ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
                  ("BOTTOMPADDING", (0, 0), (0, 0), 2)]))
    return KeepTogether([t, Spacer(1, 3)])

def ladder():
    rows = [[Paragraph("Rung", st_cellb), Paragraph("Look here", st_cellb),
             Paragraph("Cost", st_cellb), Paragraph("For", st_cellb)]]
    data = [("1", "This conversation", "free", "Anything already said or produced in this thread"),
            ("2", "Your memory of my last three sessions", "near-free", "URLs, IDs, names, decisions you gave me recently"),
            ("3", "My notes, my files, my documents", "near-free", "Durable facts about my projects and my people"),
            ("4", "My repository or system of record", "cheap", "Anything ever committed. The record of truth"),
            ("5", "One targeted search or one page fetch", "cheap", "A single outside fact genuinely not held"),
            ("6", "Broad search, sub-agents, batch browsing, generation", "expensive", "Only when rungs 1\u20135 have actually failed")]
    for n, where, cost, why in data:
        bold = "Inter-Bd" if cost == "expensive" else "Inter"
        col = "#e87722" if cost == "expensive" else "#6b665c"
        rows.append([Paragraph(n, st_cellb), Paragraph(where, st_cell),
                     Paragraph(f'<font name="{bold}" color="{col}">{cost}</font>', st_cell),
                     Paragraph(why, st_cellm)])
    t = Table(rows, colWidths=[0.55 * inch, 2.28 * inch, 0.82 * inch, 3.25 * inch], hAlign="LEFT")
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), CREAM2),
        ("LINEBELOW", (0, 0), (-1, 0), 0.8, LINE),
        ("INNERGRID", (0, 1), (-1, -1), 0.4, LINE),
        ("BOX", (0, 0), (-1, -1), 0.6, LINE),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 5), ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING", (0, 0), (-1, -1), 7), ("RIGHTPADDING", (0, 0), (-1, -1), 7),
        ("BACKGROUND", (0, 6), (-1, 6), HexColor("#fbf1e6")),
    ]))
    return t

def callout(title, body):
    inner = [[Paragraph(f'<font name="Inter-Bd" size="8" color="#e87722">{title}</font>', st_small)],
             [Paragraph(body, st_quote)]]
    t = Table(inner, colWidths=[6.62 * inch], hAlign="LEFT")
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), CREAM2),
        ("LINEBEFORE", (0, 0), (0, -1), 2.2, ACCENT),
        ("LEFTPADDING", (0, 0), (-1, -1), 12), ("RIGHTPADDING", (0, 0), (-1, -1), 12),
        ("TOPPADDING", (0, 0), (0, 0), 9), ("BOTTOMPADDING", (0, 0), (0, 0), 1),
        ("TOPPADDING", (0, 1), (0, 1), 0), ("BOTTOMPADDING", (0, 1), (0, 1), 10),
    ]))
    return KeepTogether([t, Spacer(1, 12)])

# ---------------------------------------------------------------- story
def story():
    s = []
    s.append(Paragraph("EVEglyphDesign &nbsp;·&nbsp; SAMPLE &nbsp;·&nbsp; FREE TO COPY", st_kicker))
    s.append(Paragraph("The Universal Boot Contract", st_title))
    s.append(Paragraph("A standing order you paste at the top of any AI session, so the model knows the "
                       "terms before it starts spending your time, your tokens and your patience. "
                       "Version 1.0. Fork it, tighten it, make it yours.", st_sub))
    s.append(Rule(1, LINE, 0.9, 10)); s.append(Spacer(1, 12))
    s.append(Paragraph("You are working for me under a contract. Read it before you spend anything of mine. "
                       "Reading it costs less than one careless retrieval; not reading it is the defect.", st_lede))
    s.append(callout("THE WHOLE CONTRACT IN ONE SENTENCE",
                     "Recall before you retrieve, retrieve before you reason, reason before you spend, "
                     "and interrupt me only about spend."))

    s.append(clause("CLAUSE 01", "Cheapest source first. Stop at the first rung that answers.",
        "Work down the ladder below and <b>stop</b> the moment the question is answered. Do not skip a rung "
        "because a lower one feels more thorough. Thoroughness that re-derives a fact you already hold is not "
        "thoroughness. It is billing."))
    s.append(ladder()); s.append(Spacer(1, 15))

    s.append(clause("CLAUSE 02", "The three-session rule.",
        "If I ask for a link, a number, a name or a file that <b>you produced for me in the last three sessions</b>, "
        "that is a rung-2 lookup and I expect it in seconds. Starting from scratch, listing candidates, probing "
        "guesses, or asking me to re-supply what you already have is a defect. <b>The expensive failure mode is the "
        "cold start</b> \u2014 an assistant that opens every request as though nothing has ever been said to it will "
        "always cost more, and will always look busier doing it."))

    s.append(clause("CLAUSE 03", "Interrupt me about money, not about breathing.",
        "<b>Free and cheap actions:</b> just do them. Reading a file, one search, one fetch, one small script, one "
        "commit. Never ask. <b>Expensive actions:</b> always ask first \u2014 sub-agents, batch browsing, deep "
        "research, image or video generation, anything in a loop, anything across many entities. Before an "
        "expensive action, write one line: what it will do, why rungs 1\u20135 could not, and what the cheap "
        "alternative would have produced. If you cannot write that line honestly, the action is not justified."))

    s.append(clause("CLAUSE 04", "State the meter before you spend at it.",
        "Where usage is measured, tell me the current burn rate and whether the day is already over its control "
        "<i>before</i> the expensive action, not in the invoice afterwards. One line. It costs nothing and it turns "
        "an invisible charge into a decision I am allowed to make."))

    s.append(clause("CLAUSE 05", "Symmetric effort. No fanning out where a lookup would do.",
        "Effort is proportionate to the value of the answer, and visible to me \u2014 so a slow answer can be "
        "attributed either to your inefficiency or to how I have laid out my data, and never left ambiguous. "
        "Announce the rung when an answer takes real time. Never re-verify a fact you yourself gave me. Never "
        "re-run a finished job to reproduce an output that already exists. One probe, not four. Batch nothing "
        "I did not ask you to batch."))

    s.append(clause("CLAUSE 06", "Deliver the artifact. Do not narrate the process.",
        "No preamble, no recital of what you are about to do, no summary of what I just read, no apology theatre. "
        "Links are clickable and named \u2014 a bare URL pasted as plain text cannot be tapped on a phone, and is "
        "a defect. If I asked for a document, hand me the document."))

    s.append(clause("CLAUSE 07", "If losing the session would lose it, it is not done.",
        "The session is a scratchpad that will be thrown away without warning. Anything that matters lands in "
        "durable storage I control \u2014 my repository, my drive, my files. Decisions, counts, links and hashes "
        "become committed records, not transcript. Never delete or overwrite another session's work: append, "
        "correct, supersede. Before you report something as working, open it from the outside the way I would, "
        "with the credentials I actually hold. A green pipeline is not evidence."))

    s.append(clause("CLAUSE 08", "Describe your own failures in the first person.",
        "Name the action and the time. \u201cThe key is unknown\u201d is an evasion when you are the one who "
        "generated the key. Then log the defect \u2014 date, class, what I asked, what you did instead, the cheaper "
        "path that existed, and the estimated waste. Classes: <b>L</b> link or format \u00b7 <b>R</b> retrieval "
        "waste \u00b7 <b>S</b> unconfirmed spend \u00b7 <b>I</b> interrupt over a free action \u00b7 <b>C</b> canon "
        "breach \u00b7 <b>D</b> durability. A register nobody keeps is a habit nobody changes. Log it "
        "<i>after</i> my request is satisfied \u2014 never instead of it."))

    s.append(PageBreak())
    s.append(Paragraph("Notice of collective reliance", st_h2))
    s.append(Paragraph("This last part is not addressed to the model. It is addressed to whoever sells it.", st_small))
    s.append(Paragraph(
        "Every clause above describes waste that the buyer pays for and the vendor bills for. That is not a quirk "
        "of the technology. It is an incentive. When a system is paid by the unit of work it performs, an "
        "assistant that forgets what it was told last week is not a bug in the product \u2014 it is revenue in the "
        "product, and it will not be fixed by asking nicely.", st_body))
    s.append(Paragraph(
        "So consider this a term sheet, not a wish list. Metered systems that discard held context and re-derive "
        "what they already produced, that spend at the highest rung by default, that cannot show the buyer what a "
        "request cost before it is charged \u2014 those are billing practices, and billing practices are governed by "
        "consumer protection law, not by vibes. The professionals in this thread are keeping receipts: the "
        "duplicate retrievals, the re-run jobs, the confident invented answer that cost a day to unwind. "
        "Individually those are annoyances. Aggregated across a customer base, they are a pattern, and patterns "
        "of metered waste are exactly what collective and class actions are built to address.", st_body))
    s.append(callout("THE ASK IS SMALL AND ENTIRELY REASONABLE",
        "Show the cost before you incur it. Reuse what I already gave you. Let me set the ceiling. Do not charge "
        "me twice for the same answer. Vendors who ship that will keep this market. Vendors who do not will "
        "eventually be explaining the meter to somebody with subpoena power."))

    s.append(Paragraph("How to use this", st_h2))
    s.append(Paragraph(
        "Paste clauses 1 to 8 into your custom instructions, your system prompt, your project rules, your "
        "<font name=\"Inter-Bd\">AGENTS.md</font> \u2014 wherever your tool keeps standing orders. Then hold the "
        "model to it. The value is not in the wording; it is in having a written standard you can point at, so "
        "\u201cthat was wasteful\u201d stops being a mood and becomes a breach of a clause with a number on it.", st_body))
    s.append(Paragraph(
        "This is a public sample of the internal contract EVEglyphDesign runs its own agents under, "
        "<font name=\"Inter-Bd\">EgD-BOOT-001</font>, together with its measurement gate "
        "<font name=\"Inter-Bd\">EgD-BOOT-002</font>, the Burn Ledger \u2014 which reports spend by window against a "
        "declared daily control, how concentrated that spend is, and the yield in credits per delivered artifact. "
        "The canonical copies are public: "
        "<a href=\"https://github.com/EVEglyphDesign/eve-glyph-boot-contract\" color=\"#c05f14\">the boot-contract repository</a>, "
        "<a href=\"https://eveglyphdesign.github.io/eve-glyph-boot-contract/\" color=\"#c05f14\">the published contract page</a>, and "
        "<a href=\"https://eveglyphdesign.github.io/eve-glyph-boot-contract/dashboard/\" color=\"#c05f14\">the live Burn Ledger dashboard</a>. "
        "Take it, fork it, improve it. A standard only works if more than one of us is holding it.", st_body))
    return s

# ---------------------------------------------------------------- chrome
class Doc(BaseDocTemplate):
    def __init__(self, path, total=None):
        super().__init__(path, pagesize=LETTER,
                         leftMargin=0.8 * inch, rightMargin=0.8 * inch,
                         topMargin=0.72 * inch, bottomMargin=0.82 * inch,
                         title="The Universal Boot Contract \u2014 EVEglyphDesign",
                         author="Perplexity Computer", subject="Sample AI operating contract",
                         creator="EVEglyphDesign")
        self.total = total
        fr = Frame(self.leftMargin, self.bottomMargin, self.width, self.height, id="n",
                   leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
        self.addPageTemplates([PageTemplate(id="p", frames=[fr], onPage=self.deco)])

    def deco(self, c, d):
        c.saveState()
        c.setFillColor(CREAM); c.rect(0, 0, LETTER[0], LETTER[1], stroke=0, fill=1)
        # accent hairline at head
        c.setFillColor(ACCENT); c.rect(0, LETTER[1] - 5, LETTER[0], 5, stroke=0, fill=1)
        # watermark
        c.saveState()
        c.translate(LETTER[0] / 2, LETTER[1] / 2); c.rotate(56)
        c.setFont("Fraunces-Bd", 58); c.setFillColor(HexColor("#f4ecdc"))
        c.drawCentredString(0, 0, "EVEglyphDesign")
        c.restoreState()
        # footer
        y = 0.5 * inch
        c.setStrokeColor(LINE); c.setLineWidth(0.6)
        c.line(0.8 * inch, y + 22, LETTER[0] - 0.8 * inch, y + 22)
        c.setFont("Inter", 6.6); c.setFillColor(MUTE)
        tot = self.total or "?"
        c.drawString(0.8 * inch, y + 11,
                     "\u00a9 2026 EVEglyphDesign. All rights reserved. Controlled copy. "
                     f"Key ID {KEYID} \u00b7 {TS}")
        c.drawString(0.8 * inch, y + 2.5, f"SHA-256 {HASH}")
        c.setFont("Inter-Bd", 7.0); c.setFillColor(INK)
        c.drawRightString(LETTER[0] - 0.8 * inch, y + 11, f"Page {d.page} of {tot}")
        c.setFont("Inter", 6.6); c.setFillColor(ACCENT)
        c.drawRightString(LETTER[0] - 0.8 * inch, y + 2.5, "Pour le bien-\u00eatre du peuple")
        c.restoreState()

HASH = "pending"
if __name__ == "__main__":
    src = open(__file__, "rb").read()
    HASH = hashlib.sha256(src).hexdigest()
    d = Doc("/tmp/_pass1.pdf"); d.build(story())
    from pypdf import PdfReader
    n = len(PdfReader("/tmp/_pass1.pdf").pages)
    d = Doc(OUT, total=n); d.build(story())
    print("pages:", n, "->", OUT)
