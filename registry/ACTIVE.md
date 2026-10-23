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

- **Current surface:** Universal DI PMO pitch for Sashi as SI, under Lilian's governance. Deck v3 remains rejected. Uploaded V12 guide and 15-slide source have been audited; no replacement deck generated.
- **Current repo:** [`EVEglyphDesign/eve-liliantwin-pmo`](https://github.com/EVEglyphDesign/eve-liliantwin-pmo) for instructions, templates and checks; private Universal DI PMO Project file repo for the case, deck and release status.
- **Last-touched files:**
  `eve-liliantwin-pmo`: `AGENTS.md`, `scripts/preflight.py`, `registry/VERSIONS.md`; Project: `di-pmo-pitch/sources/v12/`, `di-pmo-pitch/V12-COVERAGE-AUDIT.md`, `START-HERE.md`, `AGENTS.md`, `di-pmo-pitch/RELEASE-STATUS.json`; boot contract: `registry/ACTIVE.md`
- **Open:** tag `v0.1` not on the remote (the Claude Code session's git proxy refused the tag push, HTTP 403); create it on `7761009` from GitHub Releases. `Q-001` (EVE Sphere, domain gene, key-by-day, three update loops) partly answered from `dino-importtwin`, still open. `Q-002`–`Q-010` open, owners named in `scs-di-coe/registry/OPEN-QUESTIONS.md`. Prior open items (sovereign-starter i18n strings, 21 reference proposals, PR #3, Silva PMI) unchanged.

**Updated:** 2026-10-22 · **By:** Perplexity thread `9a86f655-6dd9-46db-bbb2-c4828d683d20`. The SCS open items above are preserved from the prior state, not newly verified.

---

© 2026 EVEglyphDesign. All rights reserved. Controlled copy.
*Pour le bien-être du peuple.*
