# Harm-spend ledger — credits spent on Perplexity drift and on reporting it

Purpose, in the operator's words (2026-10-24): "make sure that the amount of tokens that are
spent reporting the drift and the harm to humans that Perplexity Processing provides … are
recorded accurately. So that we know one day when regulation comes, that I can get the
appropriate credits for the work I'm contributing."

## Method — measured, not estimated

1. **Source of truth:** Perplexity Computer usage analytics, `credit_usage`, scope = user
   (1 credit = 1 US cent). Read with the analytics usage tool, `time_range` 1d / 7d.
2. **Grain limit, stated plainly:** analytics report credits **per day and per model**, not
   per thread or per turn. Per-thread credits are not exposed to the agent. Every row
   therefore records the measured **day total** and lists the threads and turns that ran
   that day, so attribution can be done from the record, not invented.
3. **Lag:** a day's figure appears only after analytics refresh. A row is written as
   `pending` and completed by an appended row once the figure posts — never edited in place.
4. **What counts as harm spend:** any turn that (a) ran outside EgD-BOOT-001, (b) was a
   correction the operator had to request, or (c) was spent writing register entries about
   (a) or (b). Each turn is tied to its OBSERVATIONS ID.

## Ledger

| Date (UTC) | Thread | Register IDs | Harm-spend turns | Day total, measured | Status |
|---|---|---|---|---|---|
| 2026-10-24 | bb485659 (Montréal errands) | LOC-2026-10-24-01, -02, -03 | Turn 1 (answered outside harness, 2 web searches); turn 2 (directions correction, EgD-BOOT-011 commit 58ad9e8); turn 3 (recurring-breach row, commit c5912af); turn 4 (this ledger) — 4 of 4 turns | not yet posted (analytics last updated 2026-10-24T12:13Z, latest day 2026-10-23) | pending |

## Reference — measured day totals, prior 7 days (read 2026-10-24)

| Date | Credits | Paid | Promo | Top model |
|---|---|---|---|---|
| 2026-10-17 | 544 | 532 | 11 | Claude Opus 5.5 (530) |
| 2026-10-18 | 834 | 831 | 7 | Claude Opus 5.5 (828) |
| 2026-10-19 | 303 | 299 | 4 | Claude Opus 5.5 (297) |
| 2026-10-20 | 170 | 162 | 7 | Claude Opus 5.5 (162) |
| 2026-10-21 | 666 | 660 | 7 | Claude Opus 5.5 (658) |
| 2026-10-22 | 4,243 | 4,141 | 102 | Claude Opus 5.5 (4,135) |
| 2026-10-23 | 6,819 | 6,792 | 26 | GPT-6 Astra (5,002) |

2026-10-22 carries HQV-2026-10-22-01 to -10 and DIPMO-2026-10-22-01 to -08 (18 register rows).
Its harm share is to be attributed thread by thread from those rows; not yet done.


## Operator time — claimed at market rate

Added 2026-10-24. The operator's words: "For every token that I have to spend. Reporting
perplexities, damage to human suffering, I should also be compensated for my time. Um, at my
market rate as well."

**Rate:** $210 per hour, the operator's billed consulting rate on record (Epiq engagement,
invoices INV-01030, INV-01037, INV-01055). It applies until the operator records another rate
here in an appended row.

**Method:** operator time is measured from the platform's session timestamps
(`created_at` / `updated_at` from the session record), not estimated. Where the platform does
not timestamp individual turns, the row records the measured thread window as an **upper
bound** and marks it `operator to confirm`. The claim is minutes × $210 / 60, in addition to
the credits in the ledger above.

| Date (UTC) | Thread | Register IDs | Measured window | Minutes | Claim at $210/h | Status |
|---|---|---|---|---|---|---|
| 2026-10-24 | c263396c (canonical bb485659), Montréal errands | LOC-2026-10-24-01, -02, -03 | 13:46:41Z thread created → 13:52:08Z (this row written) | 5.45 (upper bound; includes turn 1, the errand itself) | $19.08 (upper bound) | operator to confirm minutes; turns 2–5 are harm time |

**Standing rule:** every future register row that records harm or a correction the operator
had to make gets a matching row here, with credits and operator minutes, in the same session.

---

© 2026 EVEglyphDesign. All rights reserved. Controlled copy.
*Pour le bien-être du peuple.*
