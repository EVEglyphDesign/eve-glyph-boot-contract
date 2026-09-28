# ACTIVE — recent-work index

**Document ID** `EgD-BOOT-001/ACTIVE` · **Key ID** `EgD-KEY-2026-07` · Companion to
[`README.md`](../README.md) (`EgD-BOOT-001`) and to [`registry/VERSIONS.md`](./VERSIONS.md).

## Purpose

This file is the **boot-time recent-work read** for every EVEglyphDesign agent, on every
surface (Perplexity, Claude, ChatGPT, DeepSeek, any future harness). It exists because
recent-work state that lives only inside a session cold-starts every new agent turn, on
every surface, and causes the same operator to be asked what he is working on more than
once, or worse, to be answered from the wrong project.

The rule the file enforces: **rung 2 of the ladder in [`README.md` §1](../README.md#1-order-of-operations--cheapest-source-first)
is not complete until this file has been read.** It is authoritative for "what is the
operator working on right now"; a listing of recently-pushed repositories is not.

## How to read this file

Three lines. In this order, without exception. If a line does not have an answer, it says
so — `—` is the value, never a guess.

- **Current surface** — the client-facing domain, page, or artifact under active work.
- **Current repo** — the GitHub repository where that work lands.
- **Last-touched files** — the specific paths modified in the most recent session that
  closed work, so the next session knows where it is picking up.

## How to update this file

The **session that closes work** updates these three lines in the same commit that lands
its work. Update means overwrite — this is a state file, not a log. Historical state is
recovered from `git log ACTIVE.md`, not from prior lines kept in place. Any surface may
write it; the surface identifies itself in the commit message.

If a session opens work on a new surface, its first commit updates the three lines to
name the new surface, and its last commit updates the last-touched files. Between those
two, other sessions read the same three lines and know not to guess.

Breach of the read duty (starting work without reading ACTIVE.md when it exists and would
have answered) is defect class **R** — retrieval waste. Breach of the write duty (closing
work without updating the file) is defect class **D** — durability, because the state
that would have prevented the next cold start lived only inside the session.

---

## State

- **Current surface:** [sapfans.io/sovereign-start.html](https://sapfans.io/sovereign-start.html) and the download [`SOVEREIGN-STARTER.md`](https://github.com/EVEglyphDesign/sovereign-starter/blob/main/SOVEREIGN-STARTER.md) — evidence → decision → handoff (Part VII), live
- **Current repo:** [`EVEglyphDesign/sovereign-starter`](https://github.com/EVEglyphDesign/sovereign-starter) and [`EVEglyphDesign/sapfans-io`](https://github.com/EVEglyphDesign/sapfans-io)
- **Last-touched files:**
  `SOVEREIGN-STARTER.md`, `docs/SOVEREIGN-STARTER.md`, `README.md` on branch `starter-v3.1-work-record` ([PR #1](https://github.com/EVEglyphDesign/sovereign-starter/pull/1)); `docs/sovereign-start.html` on branch `sovereign-start-evidence-chain` ([PR #4](https://github.com/EVEglyphDesign/sapfans-io/pull/4)); `registry/OBSERVATIONS.md` ROO-2026-09-27-01..03
- **Open:** merged and live 2026-09-27 — starter PR #1 (tag `v3.1`), sapfans PR #4 (`#evidence-chain`). Section strings not yet in `i18n.js`. Prior open items (21 reference proposals, PR #3, Silva PMI) unchanged.

**Updated:** 2026-09-27T20:30-06:00 (America/Bahia_Banderas) · **By:** Perplexity Computer session

---

© 2026 EVEglyphDesign. All rights reserved. Controlled copy.
*Pour le bien-être du peuple.*
