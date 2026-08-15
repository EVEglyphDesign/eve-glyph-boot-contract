# EVAL-DEEPSEEK-HARNESS

**Subject:** DeepSeek Harness (`dsh`) — [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness)
**Date:** 2026-08-15
**Reviewer:** operating agent, on behalf of Dany Theriault
**Doctrine anchor:** [doctrine/05 — No Vendor Lock-In](https://github.com/EVEglyphDesign/eve-glyph-methodology/blob/main/doctrine/05-no-vendor-lock-in.md)
**Status:** evaluated · not adopted · retained for reference

---

## What it is

An open-source agent harness developed by DeepSeek AI. Runs as a local web UI or terminal, drives coding agents from the editor, ships a sandboxed shell, and exposes plugins for every capability.

| Field | Value | Source |
|---|---|---|
| License | MIT | [`LICENSE`](https://github.com/deepseek-ai/deepseek-harness/blob/master/LICENSE) |
| Version | `0.1.0-rc.5` | [`packages/llm/llm/package.json`](https://github.com/deepseek-ai/deepseek-harness/blob/master/packages/llm/llm/package.json) |
| Stars / forks | 105,290 / 10,085 | GitHub API, 2026-08-15 |
| Last push | 2026-08-13 | GitHub API, 2026-08-15 |
| Default branch | `master` | GitHub API |
| Underlying framework | Cordis (vendored) | [`vendor/`](https://github.com/deepseek-ai/deepseek-harness/tree/master/vendor) |
| Status | Developer preview — compatibility-breaking changes are policy | [`AGENTS.md`](https://github.com/deepseek-ai/deepseek-harness/blob/master/AGENTS.md) |

---

## Verdict against doctrine/05

**Adoption decision:** Do not adopt for client engagements at this time. Retain the clone and this record; re-evaluate at first tagged release (post-`rc`).

**Adoption decision if adopted later:** would be acceptable under doctrine/05 preference class 1 (open-source, self-hostable). Escape path from the harness itself is trivial — MIT, forkable, seams documented.

---

## Swappability — verified against the code

The `everything is a plugin` claim is real. Verified by reading [`docs/capability-seams.md`](https://github.com/deepseek-ai/deepseek-harness/blob/master/docs/capability-seams.md) — a graph auto-generated from the package tree by [`scripts/gen-doc-graphs.ts`](https://github.com/deepseek-ai/deepseek-harness/blob/master/scripts/gen-doc-graphs.ts), so it cannot drift from the code — and inspecting each seam's `package.json` for its declared role.

The architecture is a strict Service Definition / Service Provider / Service Consumer split. The Service Definition depends only on Cordis, never on a backend. That is the property that makes the swap real rather than cosmetic.

Seams verified in-tree:

| Seam | Service Definition | Alternate providers already shipping |
|---|---|---|
| Model | [`@deepseek-ai/dsh-llm`](https://github.com/deepseek-ai/deepseek-harness/tree/master/packages/llm/llm) — self-described as "provider-neutral LLM service interface" | `llm-deepseek`, `llm-replay`, **`llm-pi-ai`** (OpenAI, Anthropic, self-hosted OpenAI-compatible endpoints as YAML, not code) |
| Agent loop | [`@deepseek-ai/dsh-agent-loop`](https://github.com/deepseek-ai/deepseek-harness/tree/master/packages/core/agent-loop) registers as `ctx.agentLoop` | replaceable by binding a different provider to the seam |
| Sandbox | [`@deepseek-ai/dsh-sandbox`](https://github.com/deepseek-ai/deepseek-harness/tree/master/packages/sandbox/sandbox) | `sandbox-local` (bwrap / Landlock / Seatbelt / Windows ACL). Container / microVM / remote executor is a whole-capability replacement, not a plugin — the README says so plainly |
| Shell, fs, subprocess, terminal | separate seams under `packages/shell`, `packages/fs`, `packages/subprocess`, `packages/terminal` | local + sandboxed providers ship |
| Web (search + fetch) | [`@deepseek-ai/dsh-web`](https://github.com/deepseek-ai/deepseek-harness/tree/master/packages/web) | `web-search-exa`, `web-search-perplexity`, `web-search-deepseek`, `web-fetch-http` |
| Sub-agents | [`@deepseek-ai/dsh-subagent`](https://github.com/deepseek-ai/deepseek-harness/tree/master/packages/subagent) | `subagent-claude-code`, `subagent-codex`, `subagent-acp`, in-process variants — the harness already treats Claude Code and Codex as sub-agents you delegate to |
| Session persistence | seam | JSONL and SQLite providers |
| Credentials, settings, telemetry, skills, storage, workflow, LSP | all seams | at least one provider each; most have two |

The lock-in surfaces that matter are all seams, and the seams have working alternate providers already in the tree. The `dsh-plugin` GitHub topic exists for third-party plugin discovery.

---

## Why we are not adopting now

1. **Client brand risk from the DeepSeek name.** The single most important reason. Regardless of the technical merit and regardless of whether the concern is well-founded, our clients associate any product carrying a Chinese company's brand with the same threat register they attach to state-affiliated actors. That association is not something we resolve with an architecture diagram in a client meeting. Under doctrine/06 (Operator-is-Apex) the Operator's client relationships are the ground truth; a technically superior tool that damages a client relationship on introduction is not superior in the setting that matters.

2. **Pre-release policy.** [`AGENTS.md`](https://github.com/deepseek-ai/deepseek-harness/blob/master/AGENTS.md) is explicit: *"With no external consumers, prefer the correct foundation over compatibility shims: rename or repackage freely."* Compatibility-breaking changes are the current stance. Building client work on `0.1.0-rc` is disallowed by prudence, not by doctrine.

3. **Sandbox is same-world only.** True isolation requires replacing the whole shell/fs/subprocess provider group. Doable — the [`packages/e2b`](https://github.com/deepseek-ai/deepseek-harness/tree/master/packages/e2b) tree demonstrates the pattern — but it is work we would rather not carry.

4. **Connector fabric is absent.** No Gmail, Slack, Notion, calendar connectors — the layer hosted-agent vendors actually charge for. We would rebuild these as tool plugins or bridge in through `subagent-claude-code` / `subagent-codex`.

---

## Retention rationale

We keep the clone at [`/home/user/workspace/dsh`](https://github.com/deepseek-ai/deepseek-harness) (local, shallow) and this record because:

- The seam split is the exact "capability seams" pattern named in our own concept note [Plugin Harness Swappability](https://github.com/EVEglyphDesign/eve-glyph-methodology/blob/main/notes/2026-08-15-plugin-harness-swappability.md). The best public reference for that pattern is now this codebase, and we cite it.
- If a client brings their own harness requirement and DeepSeek's brand is not a factor (open-source contributor, research setting, non-enterprise), this is a defensible pick.
- At first tagged release, re-evaluate.

---

## Reconsider triggers

Reopen this evaluation when **any one** of these fires:

1. A first non-`rc` tag is cut.
2. A client explicitly asks about `dsh` or an equivalent open harness.
3. A viable fork appears under a non-DeepSeek brand (the [`dsh-plugin`](https://github.com/topics/dsh-plugin) topic is worth checking then).
4. Our own harness architecture in [[projects/glass-sovereign-agent]] hits the same "loop / sandbox / storage / tools / model as plugin" question and we want to borrow rather than invent.

---

## Downstream artifacts

- Concept note: [notes/2026-08-15-plugin-harness-swappability.md](https://github.com/EVEglyphDesign/eve-glyph-methodology/blob/main/notes/2026-08-15-plugin-harness-swappability.md)
- Local clone: `/home/user/workspace/dsh` (85 MB, `--depth 1`) — not committed; source of truth remains upstream.

---

© 2026 EVEglyphDesign. Controlled copy.
*Pour le bien-être du peuple.*
