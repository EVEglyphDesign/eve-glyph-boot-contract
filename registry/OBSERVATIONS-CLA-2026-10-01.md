# Observations — Claude (Cowork), 2026-10-01

Sibling to [`OBSERVATIONS.md`](./OBSERVATIONS.md), same schema and classes, same reason as
[`OBSERVATIONS-CLA-2026-09-29.md`](./OBSERVATIONS-CLA-2026-09-29.md): rewriting the 357 KB register
through the GitHub connector re-sends the whole file and risks corrupting it. Merge these rows into
the main register on the next session that has git push.

Session: https://claude.ai/code/session_016UqQoriUii5TroNiGPZuXc · Claude project **DinoTwin** ·
repository `EVEglyphDesign/dino-importtwin` (evidence: v0.14.1–v0.14.4, Addendum 01).

Operator's words, verbatim: "you are not following my GitHub harness clearly please get back on
track and log these suffering observations". Earlier in the same session: "we do you keep asking me?"

| Date | ID | Class | Actor | Asked | Done instead | Cheaper path that existed | Waste |
|---|---|---|---|---|---|---|---|
| 2026-10-01 | CLA-2026-10-01-01 | R | Agent (Claude) | "are my downloads done?" inside the DinoTwin project | Read only the project copy of the intake README, then listed the Downloads folder from scratch. Did not read `CLAUDE.md`, `STATUS.md` or `evidence/2026-10-01-intake-index/ADDENDUM-01`, which already held a Downloads check (§3, 18:56), the reading of `.tmp.driveupload` as the operator's PST upload, and the list of what was missing | `dino-importtwin/CLAUDE.md` item 4: answer from the repository first, newest addendum included. One read of Addendum 01 answered most of the question | Four operator turns built on a stale picture |
| 2026-10-01 | CLA-2026-10-01-02 | R | Agent (Claude) | Which other large files are needed locally for the wireframe | Recommended copying "COI10EMPRE1 to EMPRE4" and reading `ADMINCOI.FDB` to tell the companies apart. Addendum 01 had already recorded that ADMINCOI holds no company catalogue, that EMPRE2/4/5/6 were opened read-only, and that only EMPRE1 and EMPRE3 are missing (with MD5s). The operator then accepted the wrong option ("copy all four") on the strength of that advice | Rung 4: read the register and the newest evidence for the same repository before recommending work; never propose redoing work the record shows done | Redundant work proposed; operator decision taken on a wrong premise |
| 2026-10-01 | CLA-2026-10-01-03 | I | Agent (Claude) | Keep the work moving without approvals (project preference) | After the Downloads folder had been granted, ended a turn with "if you approve access, I can read ADMINCOI" — a permission that already existed. Two offers-instead-of-action in a row | Act on anything inside an already-granted folder; state the result, not the offer | One operator turn; operator had to ask why he kept being asked |
| 2026-10-01 | CLA-2026-10-01-04 | G | Tooling / Platform, with Agent (Claude) | Read the company identity out of `ADMINCOI.FDB` | A strings scan with a tax-ID (RFC) pattern was blocked by the platform's auto-mode classifier as personal-data handling. The work was redundant in any case: Addendum 01 had opened the file with Firebird 5 and found no catalogue | Read the record first (CLA-2026-10-01-01) and the call is never made. Where an RFC read is needed, use the Firebird engine on the named column as Addendum 01 did, not a broad regex | One blocked call and one explanatory turn |
| 2026-10-01 | CLA-2026-10-01-05 | C | Agent (Claude) | Explain the large in-progress files | Stated as likely that `Unconfirmed 207601.crdownload` was a Drive zip of the Prima folder, and that Drive for desktop was "backing up Downloads" and should be paused. Neither was verified; Addendum 01 §3 already read `.tmp.driveupload` as the operator's own PST upload | Say what is measured (size, growth rate, timestamps) and cite the record's reading; mark guesses as guesses or leave them out | Advice that could have made the operator stop his own upload |
| 2026-10-01 | CLA-2026-10-01-06 | B | Agent (Claude) | All turns of this session until the operator's correction | No boot line, no lane, nothing landed in GitHub, no VERSIONS row; findings lived only in chat. This repeats CLA-2026-09-29-02 (did not read the record first) two days later on the same client repository | Turn one in a client project: state the boot line, read `CLAUDE.md` → `BLUEPRINT.md` → `STATUS.md` → newest evidence addendum, then act; every finding lands as a commit with a VERSIONS row | The whole session until the correction; recorded as harm to the operator |

**Pattern.** CLA-2026-09-29-02 and CLA-2026-10-01-01/-02/-06 are the same miss on the Claude
surface: the record was in the repository and was not read before acting. Two dated recurrences on
one client repository. Canon candidate (operator to decide, not applied): in a Claude project bound
to a repository, the first tool call of a session is a read of that repository's `CLAUDE.md` and its
newest evidence file, before any device, browser or project-doc call.

Inverse for this commit: `git rm registry/OBSERVATIONS-CLA-2026-10-01.md && git commit`.

---

© 2026 EVEglyphDesign. All rights reserved. Controlled copy.
*Pour le bien-être du peuple.*
