#!/usr/bin/env python3
"""Burn Ledger — EgD-BOOT-002. EVEglyphDesign canon PDF, provenance-bearing."""
import hashlib, datetime, json
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
                                Spacer, Table, TableStyle, PageBreak, Flowable)
from reportlab.pdfgen.canvas import Canvas
from pypdf import PdfReader

W, H = LETTER
CREAM  = HexColor("#fdfaf4"); CREAM2 = HexColor("#f7f2e7")
INK    = HexColor("#1a1a1a"); LINE   = HexColor("#e7e1d3")
ORNG   = HexColor("#e87722"); MUTE   = HexColor("#6b665c")
GREY   = HexColor("#c9c2b0")

F = "/home/user/workspace/fonts"
pdfmetrics.registerFont(TTFont("Fraunces", f"{F}/Fraunces-400.ttf"))
pdfmetrics.registerFont(TTFont("Fraunces-Bold", f"{F}/Fraunces-700.ttf"))
pdfmetrics.registerFont(TTFont("Inter", f"{F}/Inter-400.ttf"))
pdfmetrics.registerFont(TTFont("Inter-SB", f"{F}/Inter-600.ttf"))
pdfmetrics.registerFont(TTFont("Inter-Bold", f"{F}/Inter-700.ttf"))

OUT  = "/home/user/workspace/EVEglyphDesign_Burn_Ledger.pdf"
DATA = "/home/user/workspace/boot/docs/dashboard/data.json"
TS   = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
CEILING = 5000
PAGES = 3
D = json.load(open(DATA))

def usd(c, prec=0):
    v = c / 100.0
    if 0 < v < 10 and prec == 0:
        return f"${v:,.2f}"
    return f"${v:,.{prec}f}"
def num(n): return f"{int(round(n)):,}"

def S(name, **kw):
    base = dict(name=name, fontName="Inter", fontSize=9.5, leading=14.5,
                textColor=INK, alignment=TA_LEFT, spaceAfter=0)
    base.update(kw); return ParagraphStyle(**base)

st_kicker = S("k", fontName="Inter-SB", fontSize=7.4, leading=10, textColor=ORNG)
st_h1     = S("h1", fontName="Fraunces-Bold", fontSize=31, leading=34)
st_sub    = S("sub", fontName="Fraunces", fontSize=13.5, leading=18, textColor=MUTE)
st_h2     = S("h2", fontName="Fraunces-Bold", fontSize=13.5, leading=17)
st_body   = S("b", spaceAfter=7)
st_lead   = S("l", fontSize=10.5, leading=16.5, spaceAfter=7)
st_cell   = S("c", fontSize=8.3, leading=12)
st_cellb  = S("cb", fontName="Inter-SB", fontSize=8.3, leading=12)
st_head   = S("th", fontName="Inter-SB", fontSize=7, leading=9.5, textColor=MUTE)
st_quote  = S("q", fontName="Fraunces", fontSize=10.5, leading=16, textColor=INK)
st_cap    = S("cap", fontSize=7.6, leading=11.5, textColor=MUTE)
st_mono   = S("m", fontName="Courier", fontSize=7.6, leading=11)

MARGIN_L, MARGIN_R = 22*mm, 22*mm
TOP, BOT = 24*mm, 26*mm
FW = W - MARGIN_L - MARGIN_R
HASHES = {}

def rule(c, y, x0, x1, col=LINE, w=0.7):
    c.setStrokeColor(col); c.setLineWidth(w); c.line(x0, y, x1, y)

def paint(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(CREAM); canvas.rect(0, 0, W, H, stroke=0, fill=1)
    canvas.saveState()
    canvas.translate(W/2, H/2); canvas.rotate(38)
    canvas.setFont("Fraunces-Bold", 62); canvas.setFillColor(HexColor("#f5f0e6"))
    canvas.drawCentredString(0, -20, "EVEglyphDesign")
    canvas.setFont("Inter", 13)
    canvas.drawCentredString(0, -46, "C A N O N   ·   C O N T R O L L E D   C O P Y")
    canvas.restoreState()
    canvas.setFont("Inter-SB", 7); canvas.setFillColor(MUTE)
    canvas.drawString(MARGIN_L, H-16*mm, "EVEglyphDesign  ·  Burn Ledger  ·  Measurement Gate")
    canvas.drawRightString(W-MARGIN_R, H-16*mm, "EgD-BOOT-002")
    rule(canvas, H-18*mm, MARGIN_L, W-MARGIN_R)
    canvas.setFillColor(ORNG); canvas.rect(MARGIN_L, H-18*mm-0.35, 26*mm, 1.6, stroke=0, fill=1)
    rule(canvas, 18*mm, MARGIN_L, W-MARGIN_R)
    canvas.setFont("Inter", 6.8); canvas.setFillColor(MUTE)
    canvas.drawString(MARGIN_L, 14.2*mm, "© 2026 EVEglyphDesign. All rights reserved. Controlled copy.")
    canvas.drawString(MARGIN_L, 11.2*mm,
        f"Issued {TS}  ·  Key ID EgD-KEY-2026-07  ·  SHA-256 {HASHES.get('sha','—')[:24]}…")
    canvas.setFont("Fraunces", 7.8); canvas.setFillColor(INK)
    canvas.drawRightString(W-MARGIN_R, 14.2*mm, "Pour le bien-être du peuple")
    canvas.setFont("Inter-SB", 6.8); canvas.setFillColor(MUTE)
    canvas.drawRightString(W-MARGIN_R, 11.2*mm, f"Page {doc.page} of {PAGES}")
    canvas.restoreState()

def tbl(rows, widths, header=True):
    t = Table(rows, colWidths=widths, repeatRows=1 if header else 0)
    style = [("VALIGN", (0,0), (-1,-1), "TOP"),
             ("TOPPADDING", (0,0), (-1,-1), 6.0),
             ("BOTTOMPADDING", (0,0), (-1,-1), 6.0),
             ("LEFTPADDING", (0,0), (0,-1), 0),
             ("RIGHTPADDING", (-1,0), (-1,-1), 0),
             ("LINEBELOW", (0,0), (-1,-2), 0.55, LINE),
             ("LINEBELOW", (0,-1), (-1,-1), 0.7, LINE)]
    if header:
        style += [("LINEABOVE", (0,0), (-1,0), 0.7, LINE),
                  ("LINEBELOW", (0,0), (-1,0), 0.7, LINE),
                  ("BOTTOMPADDING", (0,0), (-1,0), 5)]
    t.setStyle(TableStyle(style)); return t

def note(text):
    t = Table([[Paragraph(text, st_quote)]], colWidths=[FW])
    t.setStyle(TableStyle([("BACKGROUND", (0,0), (-1,-1), CREAM2),
        ("LINEBEFORE", (0,0), (0,-1), 2.2, ORNG), ("BOX", (0,0), (-1,-1), 0.6, LINE),
        ("LEFTPADDING", (0,0), (-1,-1), 11), ("RIGHTPADDING", (0,0), (-1,-1), 11),
        ("TOPPADDING", (0,0), (-1,-1), 9), ("BOTTOMPADDING", (0,0), (-1,-1), 9)]))
    return t

def kpirow(items):
    """items: list of (label, value, note)"""
    cells = []
    for lab, val, nt in items:
        cells.append(Paragraph(
            f"<font name='Inter-SB' size='6.6' color='#6b665c'>{lab.upper()}</font><br/>"
            f"<font name='Fraunces-Bold' size='16'>{val}</font><br/>"
            f"<font size='7.3' color='#6b665c'>{nt}</font>", S("kp", fontSize=8, leading=12.5)))
    n = len(items)
    t = Table([cells], colWidths=[FW/n]*n)
    t.setStyle(TableStyle([("VALIGN", (0,0), (-1,-1), "TOP"),
        ("BACKGROUND", (0,0), (-1,-1), CREAM2), ("BOX", (0,0), (-1,-1), 0.6, LINE),
        ("INNERGRID", (0,0), (-1,-1), 0.6, LINE),
        ("LEFTPADDING", (0,0), (-1,-1), 8), ("RIGHTPADDING", (0,0), (-1,-1), 8),
        ("TOPPADDING", (0,0), (-1,-1), 9), ("BOTTOMPADDING", (0,0), (-1,-1), 10)]))
    return t

class BurnChart(Flowable):
    """90-day daily burn: bars, 7-day mean line, declared control rule."""
    def __init__(self, daily, width=FW, height=62*mm):
        Flowable.__init__(self); self.d = daily; self.width = width; self.height = height
    def draw(self):
        c = self.canv
        vals = [x["credits"] for x in self.d]
        labs = [x["date"] for x in self.d]
        top = max(max(vals), CEILING) * 1.08
        pad_l, pad_b, pad_t = 17*mm, 8*mm, 2*mm
        pw = self.width - pad_l
        ph = self.height - pad_b - pad_t
        c.setFillColor(CREAM2); c.rect(0, 0, self.width, self.height, stroke=0, fill=1)
        c.setStrokeColor(LINE); c.setLineWidth(0.5)
        c.rect(0, 0, self.width, self.height, stroke=1, fill=0)
        # y gridlines
        c.setFont("Inter", 6)
        steps = 4
        for i in range(steps + 1):
            v = top * i / steps
            y = pad_b + ph * i / steps
            c.setStrokeColor(LINE); c.line(pad_l, y, self.width - 3*mm, y)
            c.setFillColor(MUTE); c.drawRightString(pad_l - 2*mm, y - 1.6, f"${v/100:,.0f}")
        bw = pw / len(vals)
        for i, v in enumerate(vals):
            h = ph * v / top
            c.setFillColor(ORNG if v > CEILING else GREY)
            c.rect(pad_l + i*bw + bw*0.12, pad_b, bw*0.76, max(h, 0.3), stroke=0, fill=1)
        # control rule
        yc = pad_b + ph * CEILING / top
        c.setStrokeColor(MUTE); c.setLineWidth(0.6); c.setDash(3, 3)
        c.line(pad_l, yc, self.width - 3*mm, yc); c.setDash()
        # 7-day mean
        c.setStrokeColor(INK); c.setLineWidth(1.0)
        pts = []
        for i in range(len(vals)):
            w = vals[max(0, i-6):i+1]
            m = sum(w) / len(w)
            pts.append((pad_l + i*bw + bw/2, pad_b + ph * m / top))
        p = c.beginPath(); p.moveTo(*pts[0])
        for xy in pts[1:]: p.lineTo(*xy)
        c.drawPath(p)
        # x labels
        c.setFont("Inter", 6); c.setFillColor(MUTE)
        for i in range(0, len(labs), 12):
            c.drawCentredString(pad_l + i*bw + bw/2, pad_b - 4.2*mm, labs[i][5:])
        # legend
        c.setFont("Inter-SB", 6)
        lx = pad_l
        c.setFillColor(ORNG); c.rect(lx, 1.6*mm, 6, 2.4, stroke=0, fill=1)
        c.setFillColor(MUTE); c.drawString(lx + 9, 1.5*mm, "over control")
        lx += 30*mm
        c.setFillColor(GREY); c.rect(lx, 1.6*mm, 6, 2.4, stroke=0, fill=1)
        c.setFillColor(MUTE); c.drawString(lx + 9, 1.5*mm, "within control")
        lx += 32*mm
        c.setFillColor(INK); c.rect(lx, 2.2*mm, 6, 1.1, stroke=0, fill=1)
        c.setFillColor(MUTE); c.drawString(lx + 9, 1.5*mm, "7-day average")

def build(hash_hex):
    HASHES['sha'] = hash_hex
    doc = BaseDocTemplate(OUT, pagesize=LETTER, leftMargin=MARGIN_L, rightMargin=MARGIN_R,
        topMargin=TOP, bottomMargin=BOT,
        title="Burn Ledger | EVEglyphDesign Measurement Gate",
        author="Perplexity Computer",
        subject="EgD-BOOT-002 — credit burn, concentration, and yield per artifact",
        creator="EVEglyphDesign")
    frame = Frame(MARGIN_L, BOT, FW, H-TOP-BOT, id="f",
                  leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
    doc.addPageTemplates([PageTemplate(id="p", frames=[frame], onPage=paint)])
    E = []; A = E.append
    SP = lambda n: E.append(Spacer(1, n))

    w = D["windows"]; s = D["shape"]; y = D["yield_30d"]
    breach = [x for x in D["daily"] if x["credits"] > CEILING]
    paid = next((x["credits"] for x in D["source_90d"] if x["name"] == "Paid"), 0)
    promo = next((x["credits"] for x in D["source_90d"] if x["name"] == "Promo"), 0)
    drift = w["d7_per_day"] / w["d30_per_day"] if w["d30_per_day"] else 0
    top_model = D["models_90d"][0] if D["models_90d"] else {"name": "—", "credits": 0}

    # ---------------- page 1 ----------------
    A(Paragraph("MEASUREMENT GATE  ·  COMPANION TO EgD-BOOT-001", st_kicker))
    SP(3)
    A(Paragraph("Burn Ledger", st_h1))
    A(Paragraph("What the credits cost, where they concentrate, and what they bought. "
                "Measured, not asserted.", st_sub))
    SP(9)
    A(tbl([[
        Paragraph("<font name='Inter-SB' color='#6b665c'>DOCUMENT ID</font><br/>EgD-BOOT-002", st_cell),
        Paragraph("<font name='Inter-SB' color='#6b665c'>KEY ID</font><br/>EgD-KEY-2026-07", st_cell),
        Paragraph("<font name='Inter-SB' color='#6b665c'>SOURCE</font><br/>Perplexity Computer usage analytics, org scope", st_cell),
        Paragraph("<font name='Inter-SB' color='#6b665c'>ISSUED</font><br/>" + TS, st_cell),
    ]], [FW*0.20, FW*0.21, FW*0.37, FW*0.22], header=False))
    SP(13)
    A(note("A contract that is not measured is a preference. This is the instrument that makes "
           "EgD-BOOT-001 enforceable."))
    SP(13)

    A(Paragraph("The bill", st_h2))
    SP(5)
    A(Paragraph("Org-scope credit consumption. One credit is one US cent, so these are real dollars, "
                "not abstract units.", st_body))
    SP(3)
    A(kpirow([
        ("Last 90 days", usd(w["d90"]), f"{num(w['d90'])} credits"),
        ("Last 30 days", usd(w["d30"]), f"{num(w['d30'])} credits"),
        ("Last 7 days", usd(w["d7"]), f"{num(w['d7'])} credits"),
    ]))
    SP(6)
    A(kpirow([
        ("Burn rate now", usd(w["d7_per_day"]) + "/day",
         f"{'up' if drift>=1 else 'down'} {abs(drift-1)*100:.0f}% against the 30-day average of {usd(w['d30_per_day'])}/day"),
        ("Paid share", f"{paid/(paid+promo)*100:.0f}% paid" if paid+promo else "—",
         f"{usd(paid)} paid · {usd(promo)} promotional, 90 days"),
    ]))
    SP(14)

    A(Paragraph("Daily burn against the declared control", st_h2))
    SP(5)
    A(Paragraph(f"The control is <b>{num(CEILING)} credits ({usd(CEILING)}) per day</b>. It is not a hard "
                f"stop; it is the line that makes a breach visible instead of invisible. "
                f"<b>{len(breach)} of {len(D['daily'])} days</b> in the window ran above it.", st_body))
    SP(4)
    A(BurnChart(D["daily"]))
    SP(4)
    A(Paragraph("Bars are single days. The solid line is the seven-day moving average. "
                "The dashed rule is the declared control.", st_cap))

    A(PageBreak())

    # ---------------- page 2 ----------------
    A(Paragraph("Concentration — the drift signal", st_h2))
    SP(5)
    A(Paragraph("Waste does not arrive evenly. It arrives in flow states, when the operator is "
                "producing and nobody is reading the meter. These ratios are the fingerprint of "
                "spend that tracked attention rather than need.", st_body))
    SP(3)
    A(kpirow([
        ("Top ten days", f"{s['top10_share']}%", "of the 90-day spend, in ten days"),
        ("Heaviest day", usd(s["peak_credits"]), f"{s['peak_day']} — {s['peak_vs_median']}× the median active day"),
        ("Median active day", usd(s["median_active_day"]), f"{s['active_days']} of 90 days had any activity"),
        ("Days over control", str(len(breach)), f"control {usd(CEILING)}/day"),
    ]))
    SP(14)

    A(Paragraph("Where the credits go", st_h2))
    SP(5)
    A(Paragraph("Model choice is the single largest lever on the bill. A heavyweight model left "
                "running on lookup work is the most common form of silent burn — which is precisely "
                "what rung one of the contract exists to prevent.", st_body))
    SP(4)
    rows = [[Paragraph("MODEL", st_head), Paragraph("90 DAYS", st_head),
             Paragraph("SHARE", st_head), Paragraph("30 DAYS", st_head)]]
    m30 = {m["name"]: m["credits"] for m in D["models_30d"]}
    for m in [x for x in D["models_90d"] if x["credits"] > 0][:9]:
        share = m["credits"] / w["d90"] * 100 if w["d90"] else 0
        rows.append([Paragraph(m["name"], st_cellb),
                     Paragraph(usd(m["credits"]), st_cell),
                     Paragraph(f"{share:.1f}%", st_cell),
                     Paragraph(usd(m30.get(m["name"], 0)) if m30.get(m["name"]) else "—", st_cell)])
    A(tbl(rows, [FW*0.40, FW*0.20, FW*0.18, FW*0.22]))
    SP(14)

    A(Paragraph("What it bought", st_h2))
    SP(5)
    A(Paragraph("Spend is only half a ledger. Yield is the other half, and spend without yield is "
                "the only definition of waste that survives an argument.", st_body))
    SP(3)
    A(kpirow([
        ("Cost per artifact", usd(y["credits_per_artifact"]) if y["credits_per_artifact"] else "—",
         f"{num(y['artifacts'])} artifacts for {usd(y['credits'])}, 30 days"),
        ("Canon format compliance", f"{y['pdf_share']}%" if y["pdf_share"] is not None else "—",
         f"{y['pdf']} PDF against {y['markdown']} markdown; canon default is PDF"),
    ]))

    A(PageBreak())

    # ---------------- page 3 ----------------
    A(Paragraph("Findings", st_h2))
    SP(6)
    findings = [
        ("Concentration is the finding, not the total.",
         f"{s['top10_share']}% of ninety days of spend landed in ten days, and the heaviest single day "
         f"ran {s['peak_vs_median']}× the median active day at {usd(s['peak_credits'])}. A steady operator "
         f"working at a steady rate does not produce that curve. It is the signature of processing that "
         f"expanded to fill available attention."),
        ("Cost per artifact is the number to drive down.",
         f"{usd(y['credits'])} over thirty days produced {num(y['artifacts'])} recorded artifacts, "
         f"or {usd(y['credits_per_artifact']) if y['credits_per_artifact'] else '—'} each. Whatever else that "
         f"bought — reasoning, retrieval, iteration — it can only fall if the cheap rungs are exhausted first."),
        ("Format drift and spend drift are the same failure.",
         f"{y['pdf']} of {num(y['artifacts'])} artifacts were PDFs against {y['markdown']} markdown files, "
         f"where the canon default is PDF. Both failures come from the same place: an agent operating on "
         f"its own defaults rather than the operator's canon."),
        ("Heavyweight models carry the bill.",
         f"{top_model['name']} alone accounts for {usd(top_model['credits'])} of the ninety-day total. "
         f"Correct for hard reasoning, wasteful for lookups. The ladder exists so that lookups never "
         f"reach that far."),
    ]
    for head, txt in findings:
        A(Paragraph(f"<font color='#e87722'><b>{head}</b></font> {txt}", st_body))
        SP(4)
    SP(8)

    A(Paragraph("Duty of the agent", st_h2))
    SP(5)
    A(Paragraph("Before any rung-six action — broad search, subagents, batch browsing, generation — "
                "state the current burn rate and whether the day is already over control. That one line "
                "is the whole gate. It costs nothing, it is a rung-two fact, and it converts an invisible "
                "charge into a decision the operator is able to make.", st_lead))
    SP(6)
    A(note("Free and cheap actions are never to be confirmed. Expensive actions are always to be "
           "confirmed. That asymmetry is the entire design."))
    SP(11)

    A(Paragraph("Provenance", st_h2))
    SP(5)
    prov = [
        ("Document", "EgD-BOOT-002 — Burn Ledger, companion to EgD-BOOT-001"),
        ("Live surface", "eveglyphdesign.github.io/eve-glyph-boot-contract/dashboard/"),
        ("Data and generator", "docs/dashboard/data.json · scripts/refresh_ledger.py"),
        ("Data source", "pplx analytics computer usage / leaderboard, org scope. 1 credit = 1 US cent"),
        ("Analytics updated", D.get("last_updated", "—") + "  ·  data generated " + D.get("generated", "—")),
        ("Content SHA-256", hash_hex),
        ("Key ID", "EgD-KEY-2026-07"),
    ]
    A(tbl([[Paragraph("FIELD", st_head), Paragraph("VALUE", st_head)]] +
          [[Paragraph(k, st_cellb), Paragraph(v, st_mono if len(v) > 48 else st_cell)]
           for k, v in prov], [FW*0.30, FW*0.70]))

    doc.build(E)

src = open(DATA, "rb").read() + open("/home/user/workspace/boot/README.md", "rb").read()
h = hashlib.sha256(src).hexdigest()
build(h)
n = len(PdfReader(OUT).pages)
if n != PAGES:
    PAGES = n
    build(h)
print("pages", len(PdfReader(OUT).pages), "sha", h)
