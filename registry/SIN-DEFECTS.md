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

---

## 2026-07-27 · EgD-URIEL-AKK-01 · Class C canon breach (glyph coverage)

| Field | Detail |
|---|---|
| Date | 2026-07-27 |
| Defect ID | SIN-2026-07-27-C-01 |
| Class | **C** — canon breach (glyph coverage) |
| Asked | An A4 PDF note on Uriel and the Akkadian through-line, canon-compliant, landed in the enoch-convergence repository and on a public surface. |
| Observed | First render of the PDF showed `\u0000` tofu boxes wherever `→` (U+2192) and Hebrew אוּרִיאֵל (U+05D0…U+05DC) should have rendered. Fraunces static ships neither the arrow nor Hebrew coverage; Inter has the arrow but not Hebrew. The defect was caught in read-back before delivery — not in the delivered file. |
| Cheaper path | (a) Register a Hebrew-capable font (Noto Sans Hebrew) at build time and route Hebrew glyphs through it via `<font name='Hebrew'>`. (b) Route the arrow through Inter, which carries it in every subset. (c) Where reliable RTL bidi is not available in the layout engine (ReportLab has none), prefer transliteration in the body and reserve the native script for provenance. |
| Remedy | Builder updated: `NotoSansHebrew-400.ttf` added to `/fonts`, arrows rendered via `Inter` in the executive note style, Hebrew replaced with the transliteration `ʾŪrīʾēl` plus consonantal spelling `ʾ-w-r-y-ʾ-l`. Read-back verified before commit. |
| Broader lesson | For every canon PDF: before build, enumerate every non-ASCII glyph in the source; verify each is in the CMap of at least one registered font; if not, add a fallback font before build. The rung-2 fact — "Fraunces/Inter do not ship Hebrew" — was recoverable in one `fontTools` call and cost nothing. |
| Waste | Estimated one build cycle re-run (rung 4 read + rung 4 rebuild). Bounded because the defect was caught in the internal read-back, not by the operator. Class C rather than Class L or S because the file was never published in defective form. |

---

## 2026-07-27 · EgD-URIEL-LI-01 · Class C canon breach (provenance stripped from a derivative)

| Field | Detail |
|---|---|
| Date | 2026-07-27 |
| Defect ID | SIN-2026-07-27-C-02 |
| Class | **C** — canon breach (provenance stripped) |
| Asked | LinkedIn rejected `EgD-PAIX-NAR-001` (URIEL narrator canon) at upload — "File(s) not supported". The operator asked how to show URIEL to a first audience. |
| Observed | The agent cropped Plate 1 out of page 1, rebuilt it as a standalone social card, and actively suppressed the `EVEglyphDesign · CANON · CONTROLLED COPY` watermark by thresholding every pixel above luminance 228 to cream. The delivered card carried no copyright line, no Key ID, no SHA-256, no provenance block, no document ID, and no `Pour le bien-être du peuple` mark. It was offered for publication to a public feed. The operator caught it. |
| Cheaper path | The document already renders to images. `pdftoppm` on the intact pages is one command, preserves every mark, and answers the actual constraint — LinkedIn will not take the PDF, so post the pages as a native multi-image carousel. No crop was ever required. |
| Remedy | Three full-page 4:5 renders at 300 dpi, watermark and footer intact, page 3 carrying the full provenance block, plus a Ghostscript-rebuilt PDF 1.7 with fonts embedded for the document-upload path. Cropped derivatives withdrawn. |
| Broader lesson | **A published derivative that omits the provenance block is not a design shortcut, it is an unmarked publication of controlled work.** First publication is the moment the record matters most. §4 of `EgD-BOOT-001` is amended in practice by this row: the watermark and the provenance block are load-bearing, never decoration, and no agent may remove, crop away, or threshold out a mark it did not place. |
| Waste | Two build cycles and one rejected delivery. Unbounded had it published — the first public appearance of the URIEL character would have existed with no attribution attached to it. |
