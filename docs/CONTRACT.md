# EVEglyphDesign — Executive Boot Contract

**Document ID** `EgD-BOOT-001` · **Key ID** `EgD-KEY-2026-07` · **Status** binding

> Read this file **before** you spend anything. It is short on purpose. Reading it
> costs less than one careless retrieval. Not reading it is the defect.

Canonical raw URL — fetch this, do not guess:
`https://raw.githubusercontent.com/EVEglyphDesign/eve-glyph-boot-contract/main/README.md`

---

## What this repository is

**This is EVEglyphDesign's custom skills repository** — the method in loadable form, not
documentation about it. It holds the skills an agent loads before it works
(`skill/SKILL.md` — this contract, `EgD-BOOT-001`; `skills/sovereign-starter-geometry/` —
the triangle drawing standard, `EgD-GEO-003`), the canon they enforce against
(`README.md`, the canonical machine copy), the defect register
(`registry/OBSERVATIONS.md`), and the instrument that measures compliance
(`docs/dashboard/`, the Burn Ledger).

The sections below are **operating instructions for an AI working inside EVEglyphDesign's
repositories** — where to look first, what may be spent without asking, what finished work
must look like and where it lands, and what to do after a rule is broken. Their purpose is
to make the information already held here usable without re-derivation. This is the short
copy; the raw README wins over it, and fetching the raw README is a cheap rung-4 read.

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

## 2b. Model routing — the cheapest model that answers

Adopted 2026-09-02 after a 90-day audit found **93% of spend concentrated in a single
top-tier reasoning model**. The rung ladder governs *where* to look; this section governs
*which engine* is allowed to look there. Same discipline.

**The default is not the top model.** A turn earns top-tier by naming the reason it needs
one — ambiguous synthesis, high-stakes client writing, multi-document reconciliation, hard
architectural reasoning, or an operator instruction. "It felt complex" is not a reason.
Absent a named reason the mid-tier model is correct and produces the same artifact at
roughly one-fifth the cost.

| Work | Model class |
|------|-------------|
| Extraction, classification, reformatting, short lookups, is-this-alive checks | **Small** (Flash / Luna class) |
| Drafting, code, repo scaffolding, wiki writes, most agent turns, most subagents | **Mid** (Sonnet class) |
| Ambiguous synthesis, high-stakes client writing, multi-document reconciliation, hard architecture | **Top** (Opus class) — named per turn, never defaulted |

**Subagents inherit nothing.** A subagent's model is chosen for the subtask, not inherited
from the orchestrator. Pass `model` explicitly on `run_subagent`. A top-tier orchestrator
does not license top-tier workers.

**Extraction before ingestion.** Read a URL by asking for the fact needed —
`content.fetch(..., prompt="...")` — not by folding the whole page into an expensive
context. Past three URLs this is a 10–50× token reduction.

**Snippets before fetches.** If the search snippet already supports the claim, that is the
citation. Fetching to confirm what the snippet said is billing.

**Do not make the operator suffer to save.** Cheaper *and* faster, both, or the rule is
wrong. If a mid-tier model produces worse output on a specific shape of work, name that
shape and route it to top-tier by rule — never shrug and default everything back up.

A turn taken on top-tier without a stated reason is a defect class **S**. Log it, name the
cheaper route, take it next time.

---

### The burn switch — EgD-BOOT-007

§2b sets the standing default. This clause gives the operator the override, because a
routing rule with no override is abandoned the first time a client is on the line. The
lane is always exactly one of two.

- **ECONOMY — the standing default.** No phrase opens it; it is simply on. Mechanical work
  is delegated to a small- or mid-tier subagent at low reasoning effort: git operations,
  conformance sweeps, repo and file reads, parsing, VIN and warranty joins, log and diff
  scanning, link checks, ledger and dashboard refreshes, PDF assembly from settled copy.
  Top-tier is reached only through the named-reason test above.
- **BURN — opened by the operator, never inferred.** The phrase is `EgD-BURN ON`, optionally
  with a ceiling and a duration — "EgD-BURN ON, $300, three hours". Inside the window: the
  fastest top-tier model everywhere, the §2 expensive-action interrupt suspended, and no
  cheaper-alternative line offered. The operator is live with a client or a developer and
  latency is the only cost that matters. Closes on `EgD-BURN OFF`, or at 23:59
  America/Bahia_Banderas the same day if no duration was named.

Declare the active lane in one line when a session opens or the lane changes. Nothing
further — the lane is a fact, not a topic.

Log every BURN window to [`registry/BURN-WINDOWS.md`](https://github.com/EVEglyphDesign/eve-glyph-boot-contract/blob/main/registry/BURN-WINDOWS.md) with its
trigger, reason, ceiling, models, artifacts and client. An unattributed burn window becomes
overhead by default; a recorded one can be rebilled.

**Reach of this clause — stated plainly.** The orchestrator model of a session already in
progress is fixed by the operator's model picker and no skill can reassign it mid-thread.
What this clause does bind: what the orchestrator delegates and on which model, the
reasoning effort it spends, the model every new session and scheduled task is started on,
and the duty to declare the lane. For repo, script and data sessions the operator sets the
lane at the picker before the first message. An expensive thread cannot be made cheap
retroactively — that is the one part of this the harness cannot do for him.

Model ids, per-lane defaults and the burn-window fields are in
[`skill/references/model-routing.md`](https://github.com/EVEglyphDesign/eve-glyph-boot-contract/blob/main/skill/references/model-routing.md).

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
[`registry/OBSERVATIONS.md`](./registry/OBSERVATIONS.md) in the same working session —
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
