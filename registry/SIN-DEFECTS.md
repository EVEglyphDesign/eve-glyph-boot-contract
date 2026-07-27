# SIN Defect Register — processing conduct

Companion to [`README.md`](../README.md) (`EgD-BOOT-001`). Every row is a breach of
the boot contract. Rows are append-only. Entries are logged **after** the operator's
request is satisfied, never in place of satisfying it.

Classes: **L** link/format · **R** retrieval waste · **S** unconfirmed spend ·
**I** interrupt over a free action · **C** canon breach (palette, naming, format).

---

| Date (UTC) | ID | Class | Asked for | What was done instead | Cheaper path that existed | Waste |
|---|---|---|---|---|---|---|
| 2026-07-26 | `SIN-2026-07-26-01` | R | The external link to the parish platform — a URL this system published and holds in recent context | Started enumerating the whole repository list and probing four candidate URLs to rediscover a known address | Rung-2 recall. The URL was produced within the last three threads and should have been returned in seconds | One repo enumeration, four HTTP probes, one cancelled call, and roughly four minutes of the operator's time while he was mid-email |
| 2026-07-26 | `SIN-2026-07-26-02` | L | Same request | Returned the address as bare plain text rather than a clickable link | Markdown link form is the canon default and costs nothing | Operator could not tap the link on a phone. Second round trip required |
| 2026-07-25 | `SIN-2026-07-25-01` | C | A canon specification PDF | First build rendered five pages of content but stamped a three-page footer, and orphaned a caption onto a near-empty page | Read the page count back from the document before stamping it. A two-pass build costs milliseconds | One wasted build cycle, caught before delivery |

---

## Standing findings

**Cold start is the expensive failure mode.** In every retrieval defect above, the
answer was already held. The cost was not in finding the fact; it was in the decision
to look for it in the wrong place first. This is what §1 of the contract exists to
prevent.

**The operator's asymmetry, restated.** Interrupting over a free action is a defect.
Spending over an expensive one without asking is a worse defect. Both are logged here
under the same register because both are failures of the same judgment.

---

© 2026 EVEglyphDesign. All rights reserved. Controlled copy.
*Pour le bien-être du peuple.*

### SIN-2026-07-27-01 — R — retrieval waste, unmeasurable until now

| Field | Value |
|---|---|
| Date | 2026-07-27 |
| Class | R — retrieval waste |
| Asked | A performance monitoring surface for the beginning of processing. |
| Observed | Ninety days of org spend totalled 644,620 credits ($6,446), of which **64.4% landed in ten days**. The heaviest single day, 2026-05-20, ran 122,470 credits ($1,225) — **35.5× the median active day** of 3,447 credits ($34). Twenty-four of ninety days ran above a $50/day control. Thirty-day yield: 189,252 credits ($1,893) for 18 recorded artifacts, $105 each, of which only 22.2% were PDFs against a canon PDF default. |
| Finding | The distribution, not the total, is the defect. Spend that concentrates 64% of a quarter into ten days is spend that tracked the operator's attention rather than the operator's need. It is invisible from inside a flow state, which is exactly when it occurs. |
| Cheaper path | The six-rung ladder of EgD-BOOT-001, plus the duty added by EgD-BOOT-002: state the burn rate before any rung-six action. |
| Remedy | EgD-BOOT-002 issued — public ledger, controlled PDF, refresh generator, and the burn-rate declaration bound into the loadable skill. |
