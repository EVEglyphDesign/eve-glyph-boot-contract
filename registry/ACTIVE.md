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

- **Current surface:** Reply to Jeff Eden positioning the EVE Sphere as the architecture component: the enterprise data map, reverse-engineered from the perpetually refreshed lake. Base model = map, context (persistent brain, memory of interactions), control (one project GitHub repo, requirement → source → component), reached by any AI surface over MCP; action-response deterministic component is an extra requirement. Supersedes Claude's rejected Curated Events margin proposal (v0.3.1) as the reply.
- **Current repo:** [`EVEglyphDesign/scs-di-coe`](https://github.com/EVEglyphDesign/scs-di-coe), review branch `eve-sphere-v0.4` (tag `v0.4.1`), **not merged**, awaiting Dany. `main` still at v0.3.1.1.
- **Last-touched files:**
  `2-deliver/2.1-architecture/EVE-SPHERE.md` (v0.4), `1-sell/KIT.md`, `1-sell/ESTIMATION.md`, `1-sell/use-cases/CURATED-EVENTS.md`, `1-sell/briefs/jeff-eve-sphere/` (PDF + `build_brief.py`), `registry/VERSIONS.md`
- **Open:** Dany's review and merge of `eve-sphere-v0.4`; reply to Jeff not sent (Dany sends on WhatsApp); Jeff's access to private `scs-di-coe` open (BLUEPRINT §9); Steel Cloud Claude account still "To connect"; Q-011–Q-014 carried.

**Updated:** 2026-11-05 · **By:** Perplexity Computer (EVE project session).
---

© 2026 EVEglyphDesign. All rights reserved. Controlled copy.
*Pour le bien-être du peuple.*
