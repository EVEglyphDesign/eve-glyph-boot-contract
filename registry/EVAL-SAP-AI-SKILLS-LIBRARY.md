# EVAL-SAP-AI-SKILLS-LIBRARY

**Subject:** SAP AI Skills Library — [`SAP/ai-skills-library`](https://github.com/SAP/ai-skills-library) · catalogue [skills.cloud.sap](https://skills.cloud.sap)
**Date:** 2026-10-18
**Reviewer:** operating agent (Perplexity Computer), on behalf of Dany Theriault
**Precedent:** [EVAL-ELEVENLABS-HOSTED-MCP](EVAL-ELEVENLABS-HOSTED-MCP.md) (shape)
**Commit reviewed:** `3a38db7` (2026-10-05)
**Status:** evaluated · one skill adopted (`sap-fiori-guidelines`) · remainder held for operator choice

---

## What it is

SAP's official registry of agent skills in the open `SKILL.md` format (the same format as this repository's `skills/`). Install path upstream is `npx skills add SAP/ai-skills-library`. It is a bring-your-own-repo catalogue: this repository holds 6 skills; [skills.cloud.sap](https://skills.cloud.sap) lists 64, most living in other SAP team repositories.

| Field | Value |
|---|---|
| Licence | Apache-2.0 (REUSE-compliant) |
| API clause | SAP API calls in the code are **not** covered by Apache-2.0. Without an SAP licence for the product: internal, non-productive, non-commercial evaluation only (`REUSE.toml`) |
| Skills in this repo | `sap-fiori-guidelines`, `sap-fiori-ios`, plugin `aicore-skills` (4: admin-resources, lifecycle-management, genai-hub-foundation-models, genai-hub-tabular-orchestration) |
| Perplexity marketplace | Not listed (searched 2026-10-18) |

## Three groups

1. **Design reference, no credentials.** `sap-fiori-guidelines` — Fiori design system, page types, Fiori Elements, S/4HANA patterns, Joule/AI patterns. Pure Markdown. **Adopted** as personal skill `user:sap-fiori-guidelines` (skill id `c0f6f5d1-3d78-49b3-afc5-26ad3ec09e97`), unmodified, with Apache NOTICE.
2. **Needs an SAP tenant.** `aicore-*` — Python scripts against SAP AI Core / GenAI Hub; require a BTP AI Core instance and service key. `sap-fiori-ios` requires the Figma MCP. **Held** — no operator tenant on record.
3. **Elsewhere in the catalogue, relevant to live work.** CAP Add Remote Service (imports S/4 OData into a CAP app — the SAP endpoint accelerator for the Hawkins spine), BTP CLI, CF CLI, SAP Tutorials Content Access (no auth). **Held** — repos not yet reviewed.

## Boundary

Fiori guidelines are SAP's visual system. They apply to SAP-facing client screens only; EgD canon (cream/orange, Fraunces/Inter) still governs EVEglyphDesign surfaces.

## Inverse

Uninstall `user:sap-fiori-guidelines` from [Skills](https://www.perplexity.ai/computer/skills); `git revert` the commit landing this file.

---

© 2026 EVEglyphDesign. All rights reserved. Controlled copy.
*Pour le bien-être du peuple.*
