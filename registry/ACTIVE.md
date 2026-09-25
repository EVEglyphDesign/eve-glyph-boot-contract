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

- **Current surface:** [sapfans.io](https://sapfans.io/) — link and staleness check; boot contract roles clause
- **Current repo:** [`EVEglyphDesign/sapfans-io`](https://github.com/EVEglyphDesign/sapfans-io) and [`EVEglyphDesign/eve-glyph-boot-contract`](https://github.com/EVEglyphDesign/eve-glyph-boot-contract)
- **Last-touched files:**
  [`sapfans-io/scripts/check-links.py`](https://github.com/EVEglyphDesign/sapfans-io/blob/main/scripts/check-links.py),
  [`sapfans-io/registry/LINK-CHECK.md`](https://github.com/EVEglyphDesign/sapfans-io/blob/main/registry/LINK-CHECK.md),
  [`sapfans-io/registry/VERSIONS.md`](https://github.com/EVEglyphDesign/sapfans-io/blob/main/registry/VERSIONS.md) (tag `v2.1-link-check`),
  `README.md` §12, `skill/SKILL.md` §4f, `registry/VERSIONS.md` v1.8 (tag `v1.8-boot-008-roles`)
- **Open:** 4 broken links on sapfans.io awaiting an operator decision (report only, nothing repaired). SAPfans PR #3 still open behind the failed Cloudflare deploy.

**Updated:** 2026-09-24T22:30-06:00 (America/Bahia_Banderas) · **By:** Perplexity Computer session

---

© 2026 EVEglyphDesign. All rights reserved. Controlled copy.
*Pour le bien-être du peuple.*
