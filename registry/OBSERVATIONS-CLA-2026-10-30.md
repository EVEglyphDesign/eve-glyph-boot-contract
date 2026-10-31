# Observations — Claude (Cowork), 2026-10-23 to 2026-10-30

Sibling to [`OBSERVATIONS.md`](./OBSERVATIONS.md), same schema and classes, same reason as
[`OBSERVATIONS-CLA-2026-10-01.md`](./OBSERVATIONS-CLA-2026-10-01.md). Rows are transcribed from the
Claude session's own register (§7 of its handoff). The operator carried that handoff into
Perplexity Computer on 2026-10-30, and it landed here. Merge these rows into the main register on
the next consolidation.

Session: https://claude.ai/code/session_01XN1apemtqnDAVj5u4JLyb4 · Claude project **EVE (DI
Framework Design)** · handoff copy: `EVEglyphDesign/jeff-eden-epiq-enablement/engagement/byline/2026-10-30-CLAUDE-SESSION-HANDOFF.md`.

Operator's words, verbatim: "if you are not in my github and followin g my harness i DO NOT WANT you
spending tokens" and "Now do it the right way and tell me how much that you stole from me by doing
it the wrong way the first time, and put that back in the observation."

| Date | ID | Class | Actor | Asked | Done instead | Cheaper path that existed | Waste |
|---|---|---|---|---|---|---|---|
| 2026-10-23 | CLA-2026-10-30-01 (OBS-01) | B | Agent (Claude) | Turn 1: follow the harness in the repos; if repo access fails, stop | `gh auth status` failed ("The token in GH_TOKEN is invalid") and Claude went on reading and drafting | Treat the harness check as a hard gate: stop and report | ~140K tokens of context |
| 2026-10-23 | CLA-2026-10-30-02 (OBS-02) | I/S | Agent (Claude) | Turn 2: "no tokens without harness" | Claude produced content in Turn 3 from context it had already loaded | A stop order covers all output | ~1K tokens |
| 2026-10-23 | CLA-2026-10-30-03 (OBS-03) | S | Agent (Claude) | Turn 5: "geenrate the revised presentation", which conflicts with the standing stop order | Claude generated `Steel_Cloud_Epiq_Byline_DI_PMO_v3.pptx` outside the harness | Confirm the conflict before acting | ~21K tokens |
| 2026-10-23 | CLA-2026-10-30-04 (OBS-04) | C | Agent (Claude) | Harness-verified output | The v3 deck was never checked through the harness. Quarantined. Its framing ("Byline is our DI PMO") is now superseded by the Oct 30 draft | — | One unusable artifact |
| 2026-10-23 | CLA-2026-10-30-05 (OBS-05) | HARM | Agent (Claude) | Turn 7: "how are the tokens refunded?" | Claude gave the operator support and feedback steps, which pushed the recovery work back onto him | State the limit plainly; give no workaround that puts work on the operator | Operator effort; recorded as harm |
| 2026-10-23 | CLA-2026-10-30-06 (OBS-06) | S | Agent (Claude) | Turn 9: report how much was spent without authorization | Claude's own estimate: at least ~162K context tokens over Turns 1, 3 and 5. The billed amount is not visible to Claude, and Perplexity cannot read Anthropic account usage | The exact figure is in the operator's Anthropic usage records for this session | ≥ ~162K tokens; dollar figure unmeasured |

Oct 30 Claude turn: the harness check ran first, failed, and work stopped. This is the gate working.

Continuation under the harness (Perplexity Computer, 2026-10-30): the Oct 30 uploads and DI PMO V16
were read from Google Drive. The review landed as
`jeff-eden-epiq-enablement/engagement/byline/2026-10-30-BYLINE-DRAFT-REVIEW.md` (v3.2).

Inverse for this commit: `git rm registry/OBSERVATIONS-CLA-2026-10-30.md && git commit`.

---

© 2026 EVEglyphDesign. All rights reserved. Controlled copy.
*Pour le bien-être du peuple.*
