#!/usr/bin/env python3
"""
EgD-BOOT-001 · Burn Ledger refresh
Pulls Perplexity Computer usage analytics and writes docs/dashboard/data.json.

Usage (inside Perplexity Computer, bash tool):
    pplx analytics computer usage get --time-range 90d --scope org \
        --datasets credit_usage > /tmp/u90.json
    pplx analytics computer usage get --time-range 30d --scope org \
        --datasets credit_usage,artifacts,skills,connectors > /tmp/u30.json
    pplx analytics computer leaderboard get > /tmp/lb.json
    python3 scripts/refresh_ledger.py /tmp/u90.json /tmp/u30.json /tmp/lb.json

1 credit = 1 US cent.
"""
import json, sys, datetime, statistics, pathlib

u90p, u30p, lbp = sys.argv[1], sys.argv[2], sys.argv[3]
OUT = pathlib.Path(__file__).resolve().parent.parent / "docs" / "dashboard" / "data.json"

u90 = json.load(open(u90p))
u30 = json.load(open(u30p))
lb  = json.load(open(lbp))

cu90 = u90["datasets"]["credit_usage"]
daily = [{"date": d["date"], "credits": d.get("count") or 0} for d in cu90["daily"]]

def cat(node, name):
    bc = (node.get("totals") or {}).get("by_categories") or {}
    return sorted(bc.get(name, []), key=lambda x: -x["count"])

def ds(src, key):
    node = src["datasets"].get(key)
    return node or {}

# --- windows -------------------------------------------------------------
def window(n):
    w = daily[-n:]
    return sum(x["credits"] for x in w), w

t90, w90 = window(90)
t30, w30 = window(30)
t7,  w7  = window(7)
t1,  _   = window(1)

active = [x["credits"] for x in daily if x["credits"] > 0]
median_active = statistics.median(active) if active else 0
peak = max(daily, key=lambda x: x["credits"]) if daily else {"date": "", "credits": 0}

# Concentration: share of the 90-day spend landing in the ten heaviest days.
top10 = sorted((x["credits"] for x in daily), reverse=True)[:10]
concentration = (sum(top10) / t90 * 100) if t90 else 0

# --- what the credits bought --------------------------------------------
arts = cat(ds(u30, "artifacts"), "Artifact Type")
art_total = sum(a["count"] for a in arts)
pdf = next((a["count"] for a in arts if a["category"] == "PDF"), 0)
md  = next((a["count"] for a in arts if a["category"] in ("Markdown/Text", "Markdown")), 0)

data = {
    "generated": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    "last_updated": u90.get("last_updated", ""),
    "document": "EgD-BOOT-001",
    "daily": daily,
    "windows": {
        "d1": t1, "d7": t7, "d30": t30, "d90": t90,
        "d7_per_day": round(t7 / 7, 1),
        "d30_per_day": round(t30 / 30, 1),
        "d90_per_day": round(t90 / 90, 1),
    },
    "shape": {
        "active_days": len(active),
        "median_active_day": median_active,
        "peak_day": peak["date"],
        "peak_credits": peak["credits"],
        "peak_vs_median": round(peak["credits"] / median_active, 1) if median_active else 0,
        "top10_share": round(concentration, 1),
    },
    "models_90d": [{"name": m["category"], "credits": m["count"]} for m in cat(cu90, "Model")],
    "models_30d": [{"name": m["category"], "credits": m["count"]}
                   for m in cat(ds(u30, "credit_usage"), "Model")],
    "source_90d": [{"name": s["category"], "credits": s["count"]} for s in cat(cu90, "Credit Source")],
    "yield_30d": {
        "credits": t30,
        "artifacts": art_total,
        "credits_per_artifact": round(t30 / art_total, 1) if art_total else None,
        "pdf": pdf, "markdown": md,
        "pdf_share": round(pdf / art_total * 100, 1) if art_total else None,
        "by_type": [{"name": a["category"], "count": a["count"]} for a in arts],
        "skills": [{"name": s["category"], "count": s["count"]}
                   for s in cat(ds(u30, "skills"), "Skill")],
        "connectors": [{"name": c["category"], "count": c["count"]}
                       for c in cat(ds(u30, "connectors"), "Connector")],
    },
    "members": [
        {"email": r.get("email", ""), "used": r.get("credits_used", 0),
         "paid": r.get("credits_paid", 0), "promo": r.get("credits_promo", 0)}
        for r in lb.get("rows", [])
    ],
    "leaderboard_range": lb.get("time_range", ""),
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(data, indent=1))
print("wrote", OUT, f"{t90} credits over 90d")
