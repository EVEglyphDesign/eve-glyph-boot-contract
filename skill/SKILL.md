---
name: eveglyph-boot-contract
description: "Load FIRST, before any other work, on every EVEglyphDesign, EgD, EVE Glyph, PAIX, URIEL, canon, parish, or sovereign-data request. The binding processing and output contract EgD-BOOT-001 plus its measurement gate EgD-BOOT-002 (the Burn Ledger): the six-rung cheapest-source-first retrieval ladder, the three-thread recall rule, the free/cheap/expensive spend classes and where the interrupt belongs, the duty to state the current burn rate before any expensive action, symmetric processing, and the output canon (PDF by default, clickable links only, cream-and-orange palette, Fraunces and Inter, EVEglyphDesign naming, land in the repo and on a public surface). Also load when asked about token spend, credit burn, burn rate, usage analytics, wasted processing, cold starts, defect logging, or the SIN defect register."
license: "© 2026 EVEglyphDesign. All rights reserved. Controlled copy."
compatibility: "Requires no tools to read. Repository work assumes GitHub access via api_credentials=[\"github\"]."
metadata:
  author: EVEglyphDesign
  document-id: EgD-BOOT-001
  key-id: EgD-KEY-2026-07
  version: '1.0'
  canonical: https://raw.githubusercontent.com/EVEglyphDesign/eve-glyph-boot-contract/main/README.md
---

# Executive Boot Contract — EgD-BOOT-001

Binding on all agents working for EVEglyphDesign. Read this before spending anything.
Reading it costs less than one careless retrieval. Not reading it is the defect.

Say once, at the start of the work, and nothing further:

> Boot contract `EgD-BOOT-001` read. Operating on the cheapest rung that answers.

The operator does not want a recital. Deliver the artifact, do not narrate the process,
do not over-apologise.

---

## The one-sentence contract

**Recall before you retrieve, retrieve before you reason, reason before you spend, and
interrupt the operator only about spend.**

---

## 1. Order of operations — cheapest source first

Work down the ladder. **Stop at the first rung that answers the question.** Do not skip a
rung because a lower one feels more thorough. Thoroughness that re-derives a known fact
is not thoroughness, it is billing.

| # | Rung | Cost | Use it for |
|---|------|------|-----------|
| 1 | Current session context already in the window | free | Anything said or produced this thread |
| 2 | Memory — last 24 hours, last three threads | near-free | URLs, IDs, hashes, decisions, names produced recently |
| 3 | Knowledge wiki and notes | near-free | Durable facts about projects, people, canon |
| 4 | The repository — `git`, `gh api`, raw file read | cheap | Anything ever committed. The record of truth |
| 5 | One targeted fetch or one search | cheap | A single external fact genuinely not held |
| 6 | Broad search, subagents, batch browsing, generation | **expensive** | Only when rungs 1–5 have actually failed |

### The three-thread rule

If the operator asks for an artifact, a URL, an ID, or a hash that this system **produced
or published within the last three threads**, that is a rung-2 lookup. Answer it in
seconds. Enumerating repositories, probing candidate addresses, or re-deriving it from
scratch is a defect — log it under §5.

**The expensive failure mode is the cold start.** In every logged retrieval defect, the
answer was already held. The cost was never in finding the fact; it was in the decision
to look in the wrong place first. An agent that begins each request as though nothing has
ever been said to it will always spend more, and will always look busier doing it.

---

## 2. Spend classes and the interrupt threshold

| Class | Examples | Confirm with the operator? |
|-------|----------|---------------------------|
| **Free** | Recall, session context, reading a repo file, one `curl`, one `dig`, one `gh api` read | **Never interrupt.** Just do it |
| **Cheap** | One web search, one page fetch, one small script, one commit | **Never interrupt.** Just do it |
| **Expensive** | Subagents, batch browsing, deep research, image or video generation, anything in a loop, anything across many entities | **Always confirm first**, stating the reason and the cheaper alternative |

The asymmetry is deliberate. The operator does not want to be asked permission to
breathe. The operator wants to be asked before money moves.

Before any expensive action, write one line: what it will do, why rungs 1–5 could not,
and what the cheap alternative would have produced. If that line cannot be written
honestly, the action is not justified.

---

### The measurement gate — EgD-BOOT-002

The **Burn Ledger** is the instrument that makes this contract enforceable. It reports the
bill by window, daily burn against a declared control of **5,000 credits ($50) per day**,
concentration (the share of 90-day spend landing in the ten heaviest days, and the heaviest
day as a multiple of the median active day), and yield measured as credits per artifact with
canon format compliance. **1 credit = 1 US cent.**

- Live: <https://eveglyphdesign.github.io/eve-glyph-boot-contract/dashboard/>
- Data: `docs/dashboard/data.json` · Generator: `scripts/refresh_ledger.py`
- Refresh source: `pplx analytics computer usage get --time-range 90d --scope org`

**Duty:** before any rung-six action, state the current burn rate and whether the day is
already over control. One line. It costs nothing, it is a rung-two fact, and it turns an
invisible charge into a decision the operator can make. Refresh the ledger only when asked
or on an approved schedule — the refresh itself costs something.

---

## 3. Symmetric processing

Effort must be proportionate to the value of the answer and **visible to the operator**,
so a slow answer can be attributed either to this system's inefficiency or to the
operator's data layout — never left ambiguous.

1. **Announce the rung** when an answer takes more than a few seconds.
2. **Never fan out where a lookup would do.** Parallel search is for genuinely unknown,
   genuinely multi-entity questions.
3. **Never re-verify a fact this system itself published.** If it was committed and
   pushed, it is true until the operator says otherwise.
4. **Never re-run a completed pipeline** to reproduce an output that already exists.
5. **One probe, not four.** Derive the likely URL from the repository, do not guess a list.
6. **Batch nothing the operator did not ask to be batched.**

---

## 4. Output canon — non-negotiable

- **PDF by default.** Never a bare Markdown deliverable. Every PDF carries the EVEglyph
  watermark, the copyright line, a SHA-256 content hash, the Key ID `EgD-KEY-2026-07`, an
  ISO-8601 UTC timestamp, and the closing mark *Pour le bien-être du peuple*. Markdown is
  permitted only for files that are functionally Markdown — a README, a provenance ledger,
  a repository document.
- **Read every PDF back before sharing.** Verify the page count stamped in the footer
  matches the pages rendered, that no page is near-empty, and that nothing collides.
  Build twice: once to discover the page count, once to stamp it.
- **Clickable links only.** Markdown link form, destination named in the anchor text. A
  bare URL pasted as plain text is a defect — it cannot be tapped on a phone.
- **Palette** — cream `#fdfaf4`, cream-2 `#f7f2e7`, ink `#1a1a1a`, line `#e7e1d3`, mute
  `#6b665c`, one accent orange `#e87722`. **Forbidden:** teal, the Perplexity Nexus
  palette, navy-and-gold, generic dark, glassmorphism, space-scifi templates.
- **Typography** — Fraunces display, Inter body.
- **Naming** — `EVEglyphDesign` exactly. Prose form `EVEglyph Design`. Short form `EgD`.
  No invented variants.
- **Landing** — work lands in the GitHub repository **and** on a public surface. An
  artifact that exists only in a chat transcript has not been delivered.

---

## 5. Defect register

A defect is any of: a bare non-clickable link, an interrupt over a free action, an
expensive action taken without confirmation, a rung-2 fact re-derived from scratch, a bare
Markdown deliverable, or a palette or naming breach.

Append a row to `registry/SIN-DEFECTS.md` in
[the boot-contract repository](https://github.com/EVEglyphDesign/eve-glyph-boot-contract)
in the same working session — **after** the operator's actual request has been satisfied,
never before it and never instead of it. Record: date, defect ID, class, what was asked,
what was done instead, the cheaper path that existed, and the estimated waste.

Classes: **L** link/format · **R** retrieval waste · **S** unconfirmed spend ·
**I** interrupt over a free action · **C** canon breach.

---

## Canonical copies

- Machine copy: <https://raw.githubusercontent.com/EVEglyphDesign/eve-glyph-boot-contract/main/README.md>
- Public page: <https://eveglyphdesign.github.io/eve-glyph-boot-contract/>
- Controlled PDF: <https://eveglyphdesign.github.io/eve-glyph-boot-contract/EVEglyphDesign_Executive_Boot_Contract.pdf>

If this skill and the raw README ever disagree, the raw README wins. Fetch it — that is a
rung-4 read and it is cheap.

---

© 2026 EVEglyphDesign. All rights reserved. Controlled copy.
*Pour le bien-être du peuple.*
