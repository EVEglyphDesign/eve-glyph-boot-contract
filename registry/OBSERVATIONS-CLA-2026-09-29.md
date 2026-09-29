# Observations — Claude (Cowork), 2026-09-29

Sibling to [`OBSERVATIONS.md`](./OBSERVATIONS.md), same schema and classes. It is a separate file
because rewriting the 340 KB register through the GitHub connector means re-sending the whole
file, and that risks corrupting it. Merge these rows into the main register on the next session
that has git push. Session: https://claude.ai/code/session_015kpqMsyebvcjGsjWWQRfZx

| Date | ID | Class | Actor | Asked | Done instead | Cheaper path that existed | Waste |
|---|---|---|---|---|---|---|---|
| 2026-09-29 | CLA-2026-09-29-01 | I | Tooling (Claude Cowork approval card) and Agent (Claude) | Audit a private client repository and land the result without interrupting the operator | The operator clicked approval cards for GitHub writes. I split the landing into three write calls (create branch, push, open PR), and each one could raise its own card | One push call to the named repository. The host setting (GitHub tools allowed without asking) removes the card | Operator's continuity. Remedy: EgD-BOOT-010 (README §14) |
| 2026-09-29 | CLA-2026-09-29-02 | R | Agent (Claude) | Harness conformance audit of a private client repository | I read the harness and the client repo, but not this register's DIN-2026-09-29 rows first. Three findings (audit D-01, D-03, D-09) recommended re-adding a gate and a narrower scope that the operator had already removed on record (DIN-2026-09-29-12, -14, -15) | Rung 4: read the register rows for the same repository before writing findings. The pattern-review rule already says never recommend reversing a decision the log shows was deliberate | One correction commit to the audit, plus the operator's time reading three wrong findings |
| 2026-09-29 | CLA-2026-09-29-03 | D | Agent (Claude) | Land README §14 | I rewrote the whole README from a copy fetched before another session's commit 6ff9ebe, and did not re-fetch before pushing. That deleted the First principle section and changed one literal escape in §7.3.1. My own blob-hash check after the push caught it | Re-fetch the file immediately before any whole-file write; on a mismatch, rebase the change onto the current file | One repair commit; the First principle was absent from main for about 20 minutes |

---

© 2026 EVEglyphDesign. All rights reserved. Controlled copy.
*Pour le bien-être du peuple.*
