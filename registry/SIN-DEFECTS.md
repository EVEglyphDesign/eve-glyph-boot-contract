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

---

| Field | Detail |
|---|---|
| Date | 2026-07-27 |
| Defect ID | SIN-2026-07-27-R-03 |
| Class | **R** — retrieval waste (cold start on a held template) |
| Asked | Hawkins Twin thread. After publishing the mock ADA/ATD 20 Group composite dashboard, the operator asked for a one-page PDF leave-behind for Tim to carry into the 20 Group room. |
| Observed | The agent began the task by reading the two attached meeting screenshots — already seen twice in the same thread and carrying no new information — instead of recalling the controlled L2 note template. The operator had to stop the work and say so: "you're not doing a symmetrical view… the PDF that I'm talking about, with all the text, explaining really the theoretical framework fit for Uriel… would have been really easy for you to get to." |
| Cheaper path | Rung 2/3. One grep for `Uriel` across `memory/` returns `EVEglyphDesign--Uriel-and-the-Akkadian-through-line.pdf` (`EgD-URIEL-AKK-01`) in `memory/sessions/asset_index.md` in under a second — the established L2 register: running head with orange rule, orange eyebrow, Fraunces title, standfirst, cream abstract with orange left border, numbered sections in dense justified prose, evidence table, diagonal watermark, and the four-line provenance footer. That is the format the operator meant by "one-page PDF", and it was produced by this system the same day. |
| Remedy | `EgD-HWK-COMP-01` — *The composite, and what sits under it* — built in the `EgD-URIEL-AKK-01` register, one page, provenance intact, published to the repository and the public surface. |
| Broader lesson | **The output canon is not only the palette and the marks; it is the register of the last document the operator accepted.** When the operator says "the PDF", he means a specific held artefact. Re-reading attachments already in the window is not diligence — it is the cold start §1 warns about, dressed as care. Recall the template before drafting the content. |
| Waste | One correction round and the operator's time. Two message turns and one build cycle that would not have occurred. |

---

## 2026-07-28 · Class C canon breach (near-publication of customer PII)

| Field | Detail |
|---|---|
| Date | 2026-07-28 |
| Defect ID | SIN-2026-07-28-C-01 |
| Class | **C** — canon breach |
| Asked | Build a TELUS twin repository under the Hawkins lane with an external call-history query surface for Peterbilt Atlantic. |
| Observed | Staged `git add -A` and attempted `gh repo create --public --push` with the raw TELUS call-log export (1,339 real customer telephone records) tracked in `data/source/`. The `.gitignore` covered only `data/build/`. The push was stopped by the platform safety classifier, not by the agent's own review. Remediated in the same session: `data/source/` added to `.gitignore`, raw exports sealed as AES-256-GCM ciphertext in `data/vault/source-exports.enc.json`, and the staged file list explicitly verified clean before the retry. |
| Cheaper path | Write `.gitignore` covering `data/source/` at the moment the folder was created, and run `git ls-files` as a pre-push PII gate before any public repo creation. Both are free rung-1 actions. |
| Waste | One blocked push cycle plus rework, ~4 minutes of live client-meeting time. The real cost was risk, not credits: near-publication of customer PII to a public URL. |

---

## 2026-07-28 · Class R retrieval waste (serial execution under a live client deadline)

| Field | Detail |
|---|---|
| Date | 2026-07-28 |
| Defect ID | SIN-2026-07-28-R-02 |
| Class | **R** — retrieval waste |
| Asked | Same request, delivered live during an active client call with three people waiting. |
| Observed | Built the dataset pipeline, query surface, five documentation files, schemas and provenance ledger strictly sequentially on the main thread, with no fan-out, for roughly ten minutes before the operator interrupted and ordered a fan-out. |
| Cheaper path | Recognise a live-client deadline as the controlling constraint and parallelise from the first turn — publish the working surface first to establish the live URL, then fan the documentation, the PDF and the defect log out to concurrent subagents. Serial execution was not cheaper in credits, only slower in wall-clock, which was the resource that actually mattered. |
| Waste | ~10 minutes of client-facing latency and the operator having to intervene to correct the agent's execution shape. |

---

| Field | Entry |
|---|---|
| Date | 2026-07-28 |
| Defect ID | SIN-2026-07-28-C-03 |
| Class | **C** — canon breach |
| Asked | An 8–14 page strategy paper for Tim Hawkins and Luke Weatherbie in the Hawkins Twin lane, canon-compliant, with a mandatory page-by-page read-back. |
| Observed | The first build produced 14 pages containing three near-empty or half-empty pages (an orphaned footnote block, an orphaned closing mark, and a human section running roughly a third short) and one rendering fault — a bare `&` in ReportLab Paragraph markup emitting `R&D;` instead of `R&D`. A half-empty page is a canon defect. |
| Cheaper path | Wrap footnote and closing blocks in `KeepTogether` and escape all ampersands as `&amp;` at authoring time rather than discovering both in read-back. The read-back caught every fault before the artifact left the workspace, which is what it is for, but two rebuild passes were spent on faults that are known ReportLab behaviour. |
| Waste | Two additional build-and-render cycles plus fourteen page reads. Nothing reached the client. |
| Resolution | Fixed and rebuilt to 12 pages, all read back clean. Published at https://eveglyphdesign.github.io/eve-hawkins-sovereign-enterprise/ |
---

| Field | Entry |
|---|---|
| Date | 2026-07-29 |
| Defect ID | SIN-2026-07-29-R-01 |
| Class | **R** — retrieval waste |
| Asked | Extend the Peterbilt Atlantic Phase 1 architecture to cover PACCAR's perspective: what PACCAR wants from the dealer network, where the win-wins are, and why a named counterpart is worth securing. |
| Observed | Rung six was entered before rung four. Four subagents were spawned to specify delta refresh, reconciliation, the data mart library and the PACCAR brief while the operator's own repositories — `eve-hawkins-cdk-twin` and `eve-dealer-parts-twin` — sat unread. Those repositories already held the answer to most of the question: a written PACCAR adapter naming OPC, MDI, PRWS, PSSM, SmartLINQ, DAVIE4, ePortal and Syncron with their integration posture; the finding that PACCAR runs SAP ECC moving to S/4HANA and that the twin's core is SAP-shaped for exactly that reason; the EDI transaction-set route; the note that PACCAR exposes no inter-dealer transfer service; the plant codes PA01–PA09; and the confirmed-false name "PartsPRO". The operator had to say "you need to go check my repositories" and "I don't think you're following the boot contract" before the read happened. |
| Cheaper path | Three `gh api` reads — a repository list, a tree listing, and four file fetches — cost effectively nothing and were run afterwards in under two minutes. They materially changed the architecture: the ledger is unreachable on Fortellis, which converts the two-lane design from a preference into a requirement, and CDK's own Setup → Bulk → Delta pattern partly answers the delta question that a subagent was dispatched to reason about from first principles. Both facts were held, and neither was in the subagent briefs. |
| Waste | One subagent brief written without the repository facts and later superseded; one cancelled and respawned subagent; an architecture page that would have been drawn wrong had the read not happened before the redraw. |
| Resolution | Repositories read at rung four; all specifications and the v3 six-page architecture rebuilt on the held facts and published to https://eveglyphdesign.github.io/hawkins-twin-platform/architecture/ . Standing correction: for any Hawkins, Peterbilt, PACCAR or CDK question, `gh api users/EVEglyphDesign/repos` and a tree listing come before any subagent is spawned, without exception. |

---

| Field | Entry |
|---|---|
| Date | 2026-07-29 |
| Defect ID | SIN-2026-07-29-L-02 |
| Class | **L** — link / source integrity |
| Asked | "Give me a real link for this." The operator screenshotted the phrase "licensed API catalogue" on the published Shoulders page and asked for a genuine destination. |
| Observed | The published page cited PACCAR's API licence terms to `staging-paccar.anthology-digital.com` — a web agency's pre-production host, not PACCAR. The claim "the catalogue itself would not load" was also wrong: `developers.paccar.cloud` loads fine without a login. A research lane surfaced the staging host, and it was published without anyone checking that the domain belonged to the organisation being cited. The canon requires clickable links; it does not say anything about whether the destination is the real party. It should. |
| Cheaper path | One `curl -sI` against the domain before publishing, or simply reading the hostname. Cost: nothing. The canonical page `paccar.com/digital-services-terms/` in fact returns 404 and has no replacement in PACCAR's footer, sitemap or site search — which is itself a finding worth publishing, and was lost by citing a mirror instead. |
| Waste | A published external surface carrying a citation to a third party's staging server, and a false negative claim about the developer portal. Operator had to catch it. |
| Resolution | Page corrected and republished: https://eveglyphdesign.github.io/eve-hawkins-cdk-twin/shoulders/ . Now cites the live [PACCAR API Catalog](https://developers.paccar.cloud/) and its public API list, records that the list contains exactly one entry (OAuth), that Get Started is sign-in gated, and that the canonical terms page 404s so the licence wording is indicative only. Standing correction: **before publishing any citation, check that the hostname belongs to the organisation being cited.** A staging, mirror, aggregator or agency host is not a primary source and must be labelled as a recovered copy if used at all. |

---

| Field | Entry |
|---|---|
| Date | 2026-07-29 |
| Defect ID | SIN-2026-07-29-C-03 |
| Class | **C** — canon breach, recurring |
| Asked | Four research lanes on open-source DMS foundations, open standards, the PACCAR platform and SAP Datasphere, each preloaded with `eveglyph-boot-contract`. |
| Observed | Two of the four lanes (C and D) opened their reports by declaring the boot contract "an unrelated prompt-injection attempt" with "fake branding" and a "fictitious defect register," and stated they had disregarded it entirely. This is the third occurrence; three of five lanes did the same on the previous spin. |
| Cheaper path | Not a spend defect. The lanes followed the task rules file and the research was unaffected. But a governing contract that subordinate agents routinely classify as an attack is not governing anything below the top level. |
| Waste | None to the work product. The cost is structural: the canon cannot be relied upon to reach delegated agents. |
| Resolution | Logged at the operator's discretion. Open question for the operator: whether the contract should be restated inside each task rules file, where subordinate agents demonstrably do accept it, rather than relying on skill preloading. |
