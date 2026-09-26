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

- **Current surface:** [sapfans.io](https://sapfans.io/) and [silvatrading.com](https://silvatrading.com/) — language toggle EN · FR · ES · DE (English default) and one-line language statement
- **Current repo:** [`EVEglyphDesign/sapfans-io`](https://github.com/EVEglyphDesign/sapfans-io), [`EVEglyphDesign/silvatrading-com`](https://github.com/EVEglyphDesign/silvatrading-com) (serving), mirrored to [`EVEglyphDesign/eve-external-surfaces`](https://github.com/EVEglyphDesign/eve-external-surfaces)
- **Last-touched files:**
  [`sapfans-io/docs/i18n.js`](https://github.com/EVEglyphDesign/sapfans-io/blob/main/docs/i18n.js), `docs/style.css`, `docs/{index,sovereign-start,tutorial,standards,repos,heritage,index-v2}.html`,
  [`sapfans-io/registry/VERSIONS.md`](https://github.com/EVEglyphDesign/sapfans-io/blob/main/registry/VERSIONS.md) v2.3 (tag `v2.3-i18n-toggle`);
  [`silvatrading-com/assets/i18n.js`](https://github.com/EVEglyphDesign/silvatrading-com/blob/main/assets/i18n.js), `index.html`,
  [`silvatrading-com/registry/VERSIONS.md`](https://github.com/EVEglyphDesign/silvatrading-com/blob/main/registry/VERSIONS.md) v1.1 (tag `v1.1-i18n-toggle`);
  `eve-external-surfaces/surfaces/silvatrading.com/{index.html,assets/i18n.js}`
- **Open:** PMI section in eve-external-surfaces (`8d42b1f`) still not deployed to the serving repo — awaiting operator. 4 broken links on sapfans.io still awaiting a decision.

**Updated:** 2026-09-26T13:30-06:00 (America/Bahia_Banderas) · **By:** Perplexity Computer session

---

© 2026 EVEglyphDesign. All rights reserved. Controlled copy.
*Pour le bien-être du peuple.*
