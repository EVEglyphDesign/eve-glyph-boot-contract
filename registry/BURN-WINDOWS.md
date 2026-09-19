# Burn Windows — rebillability register

**Document ID** `EgD-BOOT-001/BURN` · **Key ID** `EgD-KEY-2026-07` · Companion to
[`README.md`](../README.md) §2b and the burn switch `EgD-BOOT-007`.

ECONOMY is the standing lane and is never logged — it is simply the default. This register
records only the windows in which the operator deliberately bought top-tier speed, so that
spend can be attributed rather than absorbed.

The operator opens a window with `EgD-BURN ON`, optionally naming a ceiling and a duration.
It closes on `EgD-BURN OFF`, or at 23:59 America/Bahia_Banderas the same day when no
duration was named. The agent appends the row in the same session the window closes.

**Rebillability is the point.** An unattributed window becomes overhead by default. A window
with a named client and artifact is an invoice line.

---

| Opened (UTC) | Closed (UTC) | Trigger (verbatim) | Reason | Ceiling (USD) | Models used | Artifacts produced | Rebillable | Client |
|---|---|---|---|---|---|---|---|---|
| — | — | — | register opened, no windows yet | — | — | — | — | — |

---

## How to read this against the Burn Ledger

The [Burn Ledger dashboard](https://eveglyphdesign.github.io/eve-glyph-boot-contract/dashboard/)
reports what was spent by day. This register reports *why* the heaviest days were heavy. A
day above the 5,000-credit ($50) control with no row here is unattributed overhead, and that
gap — not the total — is the number to manage.

---

© 2026 EVEglyphDesign. All rights reserved. Controlled copy.
*Pour le bien-être du peuple.*
