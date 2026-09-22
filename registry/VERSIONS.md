# Version Arc — reversibility register

Companion to [`README.md`](../README.md) (`EgD-BOOT-005`, §10). This arc is monotonic —
rows are appended, never edited or removed. Every row states its own inverse. A row with
no inverse is not a finished row.

IDs are dotted and hierarchical, tied to a component blueprint — `L0` for the whole
repository, `L1.x` for a major component, `L2.x.y` for a sub-component change — the
operator's S/4-retrofit blueprint split, also used on his eDiscovery platform and his
truth ledger. The dots are the structure. Do not flatten them into a running number.

Irreversible changes are labelled **irreversible** in the Inverse column rather than
quietly listed among the rest, and are only made after the operator's confirmation —
recorded in the Confirmed column.

---

| Version | ID | Date (UTC) | Change | Inverse (exact command/action) | Tag | Confirmed (if irreversible) |
|---|---|---|---|---|---|---|
| v1.0 | L0 | 2026-07-30 | Added EgD-BOOT-004 (repository-only record) and EgD-BOOT-005 (versioned and reversible) to `README.md` and `skill/SKILL.md`; added defect class **V**; created this arc. | `git revert` the commit that lands this row, or `git checkout <prior-tag> -- README.md skill/SKILL.md` | `v1.0-boot-004-005` | n/a — reversible |
| v1.1 | L1.1 | 2026-07-30 | Added EgD-BOOT-006 (the rule of three) as §11 in `README.md` and §4e in `skill/SKILL.md`; added defect class **T** — drift or shape breach — to the §5 class list in both files; bumped `skill/SKILL.md` metadata version to `1.2` and updated its frontmatter description to mention EgD-BOOT-006. | `git revert` the commit that lands this row, or `git checkout <prior-tag> -- README.md skill/SKILL.md` | `v1.1-boot-006` | n/a — reversible |
| v1.2 | L1.2 | 2026-08-01 | Published position paper **EgD-POS-001 — The Additive Position** as `docs/position/EgD-POS-001.md`, the canon PDF `docs/position/EVEglyphDesign_Additive_Position.pdf` (5 pp., source SHA-256 `56b9c42c…dc9a`), and the public page `docs/position/index.html` at the `/position/` surface. Adds no clause to the boot contract; states the availability position derived from it. | `git revert` the commit that lands this row, or `git rm -r docs/position && git checkout <prior-tag> -- registry/VERSIONS.md` | `v1.2-pos-001` | n/a — reversible |
| v1.3 | L1.3 | 2026-08-01 | **EgD-POS-001 raised to v2.0.** Rewrote the paper in operating register — sentiment removed, claims bounded and testable — and added §III **Channel strategy — SAP and Salesforce**: reciprocal non-competition (no substitution, mirror rights, return rights), mirror-without-cannibalisation, and the return path into the vendor's system of record. Sections renumbered I–VII. Public page now generated from the Markdown by `md2html.py`; PDF rebuilt to 6 pp., source SHA-256 `5bc43d7a…0fd5`. | `git revert` the commit that lands this row, or `git checkout v1.2-pos-001 -- docs/position registry/VERSIONS.md` | `v1.3-pos-001-v2` | n/a — reversible |
| v1.4 | L1.4 | 2026-08-01 | Published strategy note **EgD-STR-001 — The Review Path** as `docs/strategy/EgD-STR-001.md`, the canon PDF `docs/strategy/EVEglyphDesign_Review_Path.pdf` (4 pp., source SHA-256 `3d7ae32e…e8e0`), and the public page `docs/strategy/index.html` at the `/strategy/` surface; added `/position/` and `/strategy/` links to `docs/index.html` §07. Identifies the review counterpart (Ashutosh Bansal, *The Transformation Advantage*, a LinkedIn newsletter — not a Substack) and sets the three-surface, three-piece distribution path. Adds no clause to the boot contract. | `git revert` the commit that lands this row, or `git rm -r docs/strategy && git checkout v1.3-pos-001-v2 -- docs/index.html registry/VERSIONS.md` | `v1.4-str-001` | n/a — reversible |
| v1.5 | L1.5 | 2026-09-18 | **Additive only — no existing file modified.** Added the Claude loader skill `skills/eveglyph-boot-contract/SKILL.md` (frontmatter `name` + `description`, 665 chars, 359 under the 1024 ceiling) so EgD-BOOT-001 is discoverable by Claude's `skills/<name>/SKILL.md` loader; added `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json` so the contract installs as a versioned plugin by repository URL. `skill/SKILL.md` is untouched and remains the single source of the full contract text; the loader carries no forked copy of it. No change to `README.md`, `docs/`, or any surface Perplexity or ChatGPT reads. | `git revert` the commit that lands this row, or `git rm -r .claude-plugin skills/eveglyph-boot-contract && git checkout v1.4-str-001 -- registry/VERSIONS.md` | `v1.5-claude-plugin` | n/a — reversible |
| v1.6 | L1.6 | 2026-09-21 | **Cross-harness recent-work index — ACTIVE.md.** Added `registry/ACTIVE.md`, a three-line boot-time read (current surface, current repo, last-touched files) written by the session that closes work and read by every session that opens it. Modified `README.md` §1 rung 2 to name the file as the boot-time recall read and to state that rung 2 is not complete until it has been read. Cause logged as ROO-2026-09-21-01 (Perplexity misrouted to sapfans.io on a listing sort) and ROO-2026-09-21-02 (Perplexity and Claude cold-started on the same operator on the same repository the same night). Fix is repository-side and cross-harness by design: both surfaces load this contract; both will therefore read the same file. | `git revert` the commit that lands this row, or `git rm registry/ACTIVE.md && git checkout v1.5-claude-plugin -- README.md registry/VERSIONS.md` | `v1.6-active-md` | n/a — reversible |

---

## How to walk the arc backwards

1. Read this table from the bottom up.
2. For the version you want to return to, run the Inverse of every row **above** it, in
   reverse order, or check out the annotated tag of the target version directly:
   `git checkout <tag>`.
3. Rows marked **irreversible** cannot be undone by git alone — read the row's Inverse
   column for what was actually done to compensate, if anything.
4. If the repository state does not match what this table says it should, the table is
   wrong and gets corrected in a new appended row — the row that turned out to be wrong is
   never edited in place.

---

© 2026 EVEglyphDesign. All rights reserved. Controlled copy.
*Pour le bien-être du peuple.*
