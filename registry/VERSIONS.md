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
