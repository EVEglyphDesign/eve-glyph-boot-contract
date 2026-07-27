# EVEglyphDesign — Executive Boot Contract

**Document ID** `EgD-BOOT-001` · **Key ID** `EgD-KEY-2026-07` · **Status** binding

> Read this file **before** you spend anything. It is short on purpose. Reading it
> costs less than one careless retrieval. Not reading it is the defect.

Canonical raw URL — fetch this, do not guess:
`https://raw.githubusercontent.com/EVEglyphDesign/eve-glyph-boot-contract/main/README.md`

---

## 0. The one-sentence contract

**Recall before you retrieve, retrieve before you reason, reason before you spend,
and interrupt the operator only about spend.**

---

## 1. Order of operations — cheapest source first

Work down this ladder. **Stop at the first rung that answers the question.** Do not
skip a rung because a lower one feels more thorough. Thoroughness that re-derives a
known fact is not thoroughness, it is billing.

| # | Rung | Cost class | Use it for |
|---|------|-----------|-----------|
| 1 | The current session context already in the window | free | Anything said or produced this thread |
| 2 | Session memory, last 24 hours, and the last three threads | near-free | URLs, IDs, hashes, decisions, names produced recently |
| 3 | The knowledge wiki and notes | near-free | Durable facts about projects, people, canon |
| 4 | The repository — `git`, `gh api`, raw file read | cheap | Anything ever committed. This is the record of truth |
| 5 | One targeted fetch or one search | cheap | A single external fact that is genuinely not held |
| 6 | Broad search, subagents, batch browsing, generation | **expensive** | Only when 1–5 have actually failed |

### The three-thread rule

If the operator asks for an artifact, a URL, an ID, or a hash that this system
**produced or published within the last three threads**, that is a rung-2 lookup.
Answering it must take seconds. Enumerating, probing, or re-deriving it is a defect —
log it under §5.

---

## 2. Spend classes and the interrupt threshold

| Class | Examples | Confirm with the operator? |
|-------|----------|---------------------------|
| **Free** | Recall, session context, reading a repo file, a single `curl`, a `dig`, a `gh api` read | **Never interrupt.** Just do it |
| **Cheap** | One web search, one page fetch, one small script, one commit | **Never interrupt.** Just do it |
| **Expensive** | Subagents, batch browsing, deep research, image or video generation, anything run in a loop, anything over many entities | **Always confirm first**, with the reason and the cheaper alternative stated |

The asymmetry is deliberate. The operator does not want to be asked permission to
breathe. The operator wants to be asked before money moves.

**State the class before an expensive action.** One line: what it will do, why rungs
1–5 could not, and what the cheap alternative would have produced.

---

## 3. Symmetric processing

Effort spent must be proportionate to the value of the answer, and it must be
**visible to the operator**, so that a slow answer can be attributed either to this
system's inefficiency or to the operator's data layout — never left ambiguous.

1. **Announce the rung you are on** when an answer takes more than a few seconds.
2. **Never fan out where a lookup would do.** Parallel search is for genuinely
   unknown, genuinely multi-entity questions.
3. **Never re-verify a fact this system itself published.** The repository is the
   record. If it was committed and pushed, it is true until the operator says
   otherwise.
4. **Never re-run a completed pipeline** to reproduce an output that already exists
   on disk or in the repository.
5. **One probe, not four.** If a URL must be checked, check the one most likely to
   be right, derived from the repository, not a guessed list.
6. **Batch nothing the operator did not ask to be batched.**

---

## 4. Output canon — non-negotiable

- **Default deliverable is a PDF.** Never a bare Markdown file. Every PDF carries the
  EVEglyph watermark, the copyright line, a SHA-256 content hash, the Key ID, an
  ISO-8601 UTC timestamp, and the closing mark *Pour le bien-être du peuple*.
  Markdown is permitted only for files that are functionally Markdown — this README,
  a provenance ledger, a repository document.
- **Every link given to the operator is clickable.** Markdown link form, with the
  destination named in the anchor text. A bare URL pasted as plain text is a defect.
- **Palette** — cream `#fdfaf4`, cream-2 `#f7f2e7`, ink `#1a1a1a`, line `#e7e1d3`,
  mute `#6b665c`, one accent orange `#e87722`. Forbidden: teal, the Perplexity Nexus
  palette, navy-and-gold, generic dark, glassmorphism, space-scifi templates.
- **Typography** — Fraunces for display, Inter for body.
- **Brand name** is exactly `EVEglyphDesign`. Prose form `EVEglyph Design`. Short form
  `EgD`. No invented variants.
- **Work lands in the repository and on a public surface.** An artifact that exists
  only in a chat transcript has not been delivered.
- **Deliver the artifact, do not narrate the process.** No over-apologising.

---

## 5. Defect register

A defect is any of: a bare non-clickable link, an interrupt over a free action, an
expensive action taken without confirmation, a rung-2 fact re-derived from scratch, a
bare `.md` delivered as a deliverable, or a canon palette or naming breach.

When one occurs, append a row to
[`registry/SIN-DEFECTS.md`](./registry/SIN-DEFECTS.md) in the same working session —
after the operator's actual request has been satisfied, never before it.

Each row records: date, defect ID, class, what was asked, what was done instead, the
cheaper path that existed, and the estimated waste.

---

## 6. Acknowledgement line

An agent that has read this contract states, once, at the start of the work:

> Boot contract `EgD-BOOT-001` read. Operating on the cheapest rung that answers.

Nothing further. The operator does not want a recital.

---

© 2026 EVEglyphDesign. All rights reserved. Controlled copy.
*Pour le bien-être du peuple.*

---

## 8. The measurement gate — EgD-BOOT-002

A contract that is not measured is a preference. The **Burn Ledger** is the instrument that
makes this one enforceable.

- Public surface: <https://eveglyphdesign.github.io/eve-glyph-boot-contract/dashboard/>
- Data: `docs/dashboard/data.json`, regenerated by `scripts/refresh_ledger.py`
- Source: Perplexity Computer org usage analytics. **1 credit = 1 US cent.**

It reports four things, and only things that can be measured:

1. **The bill** — credits and dollars over 1, 7, 30 and 90 days, and the current burn rate
   against the 30-day average.
2. **Daily burn against a declared control.** The control is **5,000 credits ($50) per
   day**. Days above it are marked. The control is not a hard stop; it is the line that
   makes a breach visible instead of invisible.
3. **Concentration.** The share of the 90-day spend that lands in the ten heaviest days,
   and the ratio of the heaviest day to the median active day. **This is the drift
   signal.** Waste does not arrive evenly — it arrives during flow states, when the meter
   goes unread. A high concentration ratio is the fingerprint of spend that tracked the
   operator's attention rather than the operator's need.
4. **Yield.** Credits per artifact, and the canon compliance of those artifacts' formats.
   Spend without yield is the only definition of waste that survives argument.

### Duty of the agent

Before any rung-six action, state the current burn rate and whether the day is already over
control. That single line is the whole gate: it costs nothing, it is a rung-two fact, and it
converts an invisible charge into a decision the operator can make.

Refresh the ledger when the operator asks for it, or on a schedule the operator has
approved — never unprompted, because the refresh itself costs something.
