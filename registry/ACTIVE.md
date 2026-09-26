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

- **Current surface:** [sapfans.io/references.html](https://sapfans.io/references.html) — filterable SAP references catalog with review queue (v2.4)
- **Current repo:** [`EVEglyphDesign/sapfans-io`](https://github.com/EVEglyphDesign/sapfans-io)
- **Last-touched files:**
  `docs/references.html`, `docs/references.json`, [`registry/PROPOSALS.md`](https://github.com/EVEglyphDesign/sapfans-io/blob/main/registry/PROPOSALS.md), `registry/proposals.json`,
  `scripts/refs.py`, `intake/INBOX.md`, `.github/workflows/references.yml`, `.github/ISSUE_TEMPLATE/reference.yml`, `docs/i18n.js`, nav on all pages, `registry/VERSIONS.md` v2.4 (tag `v2.4-references-catalog`)
- **Open:** 21 proposals awaiting operator review (9 sessions need the original LinkedIn post link; ch-geo Databricks gist is a scope question). R-021 learning.sap.com unit returned 404 on first check. Weekly ARK discovery run (model spend) proposed, not scheduled. Silva PMI section still undeployed.

**Updated:** 2026-09-26T15:40-06:00 (America/Bahia_Banderas) · **By:** Perplexity Computer session

---

© 2026 EVEglyphDesign. All rights reserved. Controlled copy.
*Pour le bien-être du peuple.*
