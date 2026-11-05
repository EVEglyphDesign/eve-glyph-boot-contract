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

- **Current surface:** SCS EVE kit for Jeff Eden's eight items (solution set, presentations, architecture, implementation, estimation, use case, team, support), first use case Curated Events (Dave Paulus, event margin). Review branch, not operator-approved.
- **Current repo:** [`EVEglyphDesign/scs-di-coe`](https://github.com/EVEglyphDesign/scs-di-coe), branch `eve-kit-v0.3` (v0.3.0.1). Patterns from `hawkins-twin` and `dino-importtwin`, shape only.
- **Last-touched files:**
  `1-sell/KIT.md`, `1-sell/ESTIMATION.md`, `1-sell/use-cases/CURATED-EVENTS.md`, `2-deliver/2.1-architecture/EVE-SPHERE.md`, `2-deliver/2.2-phases/BLUEPRINT-TEMPLATE.md`, `2-deliver/2.3-pmo/TEAM.md`, `3-keep/SUPPORT.md`, `registry/VERSIONS.md`, `registry/OPEN-QUESTIONS.md`; boot contract: `registry/ACTIVE.md`, `registry/OBSERVATIONS.md`
- **Open:** Dany reviews and merges `eve-kit-v0.3`; reply to Jeff (WhatsApp) not sent; Steel Cloud Claude account still "To connect" (point it at scs-di-coe, not hawkins-twin); Q-011–Q-014 in scs-di-coe. Prior open items (DI PMO v5 tag `v0.1`, Q-001–Q-010) carried, not re-verified.

**Updated:** 2026-11-05 · **By:** Claude Code (desktop, SitRep session).
---

© 2026 EVEglyphDesign. All rights reserved. Controlled copy.
*Pour le bien-être du peuple.*
