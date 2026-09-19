# Model routing reference — §2b and EgD-BOOT-007

Read this when choosing a subagent model, starting a new session or scheduled task, or
opening and closing a BURN window. **1 credit = 1 US cent.** Classes below are the canon
Small / Mid / Top tiers of §2b, not prices.

---

## Subagent model ids — `run_subagent(model=...)`

| Class | id | Use for |
|---|---|---|
| Small | `gemini_3_7_flash` | high-volume or long-context parsing, extraction, is-this-alive checks |
| Small | `gpt_5_6_luna` | cheapest fast option; already carries the scheduled fleet |
| **Mid — default** | `claude_sonnet_5_0` | git operations, sweeps, repo scaffolding, drafting, most subagents |
| Top | `claude_opus_5_0` | named-reason turns only: ambiguous synthesis, client-facing writing, hard architecture |
| Top+ | `claude_fable_5` | only when the operator asks for the top tier and accepts the charge |

Pair the mid and small lanes with `reasoning_effort="low"` for mechanical work and
`"medium"` for drafting. Never omit `model` on a mechanical subagent — omission inherits the
orchestrator, which is how top-tier spend leaks into git operations.

## Session and cron model ids — `pplx session new --model`, and the operator's picker

| Intent | id |
|---|---|
| Cheapest capable | `pplx_asi_glm_5_3` |
| Economy standard — repo, script, data sessions | `pplx_asi_sonnet` |
| BURN lane, latency-optimised | `pplx_asi_opus_fast` |
| Hardest judgment | `pplx_asi_opus` · `pplx_asi_fable_5` (bills above Opus) |

Scheduled tasks are background agents: keep every cron on Small or Mid unless its output is
client-facing prose.

---

## Work classification

**Mechanical — Small or Mid, always delegated.** Git clone, pull, commit, push; conformance
sweeps; repo and file reads; JSON/CSV/XLSX parsing; VIN and warranty joins; log and diff
scanning; link checking; ledger and dashboard refreshes; PDF assembly from settled copy;
renaming and moving files.

**Judgment — Top is earned by naming the reason.** Client-facing wording; data-model and
architecture decisions; commercial boundaries and pricing; canon and defect rulings;
anything a client reads under the EVEglyph watermark.

**Never delegated to a cheap worker:** the operator's actual question, a canon ruling, or a
defect-register entry.

---

## Escalation — the quality floor outranks the cheap rung

If a cheap-lane task breaches canon, returns unusable output, or fails twice, escalate that
one task to Top, finish it, and record the escalation with the shape of work that failed so
§2b can route that shape upward by rule. Do not attempt a third cheap retry and do not hand
the operator degraded work to save credits. An escalated cheap-lane failure is not a defect;
a cheap-lane failure that shipped is class **C**.

---

## BURN window record

Append one row to `registry/BURN-WINDOWS.md` in the boot-contract repository in the same
session the window closes:

`opened_at` (ISO-8601 UTC) · `closed_at` · `trigger` (operator phrase, verbatim) ·
`reason` (client, surface, or developer session) · `declared_ceiling_usd` ·
`models_used` · `artifacts_produced` · `rebillable` (yes / no / unknown) · `client`

Rebillability is the entire point of the record. An unattributed window becomes overhead.

---

© 2026 EVEglyphDesign. All rights reserved. Controlled copy.
*Pour le bien-être du peuple.*
