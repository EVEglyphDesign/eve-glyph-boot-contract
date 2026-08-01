# Ledger migrated to SF-SN-Registry (star schema)

This registry's SIN entries (`SIN-DEFECTS.md`) have been migrated into the
`FACT_SIN` star-schema fact table in the private
[`EVEglyphDesign/SF-SN-Registry`](https://github.com/EVEglyphDesign/SF-SN-Registry)
repository, at:

- [`schema/fact_sin.csv`](https://github.com/EVEglyphDesign/SF-SN-Registry/blob/main/schema/fact_sin.csv) — 43 boot-contract rows migrated
- [`scripts/build_star.py`](https://github.com/EVEglyphDesign/SF-SN-Registry/blob/main/scripts/build_star.py) — migration/build script (idempotent, no network)
- [`canon/MIGRATION-THREE-LEDGERS.md`](https://github.com/EVEglyphDesign/SF-SN-Registry/blob/main/canon/MIGRATION-THREE-LEDGERS.md) — full mapping rule, worked example, and judgement calls for this ledger
- [`canon/STAR-SCHEMA.md`](https://github.com/EVEglyphDesign/SF-SN-Registry/blob/main/canon/STAR-SCHEMA.md) — the target Kimball star schema

**Migration commit:** [`4ae6ae6`](https://github.com/EVEglyphDesign/SF-SN-Registry/commit/4ae6ae6d1383ffcac2fdbfbdcbfcee807c5f1963)
on `EVEglyphDesign/SF-SN-Registry`, main branch.

This is a **read-only forwarding pointer**. `SIN-DEFECTS.md` and every
other file in this repository remain completely untouched — nothing here
was deleted, rewritten, or renumbered. Every migrated row's `legacy_id`
column in `fact_sin.csv` points back to this ledger's own original SIN ID,
so the two records can always be cross-checked.

*pour le bien-être du peuple*
