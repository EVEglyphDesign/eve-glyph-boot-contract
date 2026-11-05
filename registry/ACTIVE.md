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

- **Current surface:** SCS offer structure for Jeff Eden to sell repeatedly: front end = value of a DI PMO (V16 wording verbatim); back end = EVE Sphere (enterprise data map from the perpetually refreshed lake; base = map, context, control over MCP; action-response extra), proposed as SCS delivery background technology; client data and all indexing sovereign; DI CoE gives architecture and setup; lake connectivity and wider rollout owned by SCS delivery or client, else billed at Dany's and Tobias's hourly rates.
- **Current repo:** [`EVEglyphDesign/scs-di-coe`](https://github.com/EVEglyphDesign/scs-di-coe), review branch `eve-sphere-v0.4` (tags `v0.4.1`, `v0.5.0`), **not merged**, awaiting Dany. `main` at v0.3.1.1.
- **Last-touched files:**
  `1-sell/OFFER-STRUCTURE.md`, `1-sell/briefs/offer-structure/` (PDF + `build_offer.py`), `1-sell/KIT.md`, `2-deliver/2.1-architecture/EVE-SPHERE.md`, `1-sell/briefs/jeff-eve-sphere/`, `registry/VERSIONS.md`
- **Open:** Dany's review and merge; Lilian's consent to V16 wording in an SCS offer (V16 is under review; its IP slide places DI PMO IP in the DI PMO venture); Jeff's access to private `scs-di-coe`; entry price not on the sheet (V16 assessment USD 25,000 vs OFFERING Phase 0 USD 5,000); Steel Cloud Claude account "To connect"; Q-011–Q-014.

**Updated:** 2026-11-05 · **By:** Perplexity Computer (EVE project session).
---

© 2026 EVEglyphDesign. All rights reserved. Controlled copy.
*Pour le bien-être du peuple.*
