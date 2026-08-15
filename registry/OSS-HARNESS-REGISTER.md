# OSS-HARNESS-REGISTER

**Purpose:** running register of open-source agent harnesses, runtimes, and connector fabrics we track as potential lock-in exits, evaluated against [doctrine/05 — No Vendor Lock-In](https://github.com/EVEglyphDesign/eve-glyph-methodology/blob/main/doctrine/05-no-vendor-lock-in.md) preference order.
**Concept anchor:** [Plugin Harness Swappability](https://github.com/EVEglyphDesign/eve-glyph-methodology/blob/main/notes/2026-08-15-plugin-harness-swappability.md).
**Companion file:** [EVAL-DEEPSEEK-HARNESS.md](./EVAL-DEEPSEEK-HARNESS.md).
**Baseline date:** 2026-08-15. Star counts and licenses verified via `gh api` on that date. Refresh on reconsider trigger only — chasing star deltas is rung-6 spend without a purpose.

---

## Doctrine/05 preference reminder

1. Open-source, self-hostable — preferred.
2. Open standard, multiple vendors — acceptable.
3. Proprietary, with documented export — acceptable with waiver.
4. Proprietary, no export — not approved.

Class 1 covers MIT and Apache-2.0 both. The register uses whichever the project actually ships; we do not treat Apache-2.0 as inferior.

---

## Harnesses — verified against GitHub, 2026-08-15

| Project | License | Stars | Owner | Notes |
|---|---|---|---|---|
| [`sst/opencode`](https://github.com/sst/opencode) | MIT | 197,630 | sst | Terminal-first coding agent. Highest star count in the class. |
| [`All-Hands-AI/OpenHands`](https://github.com/All-Hands-AI/OpenHands) | MIT | 84,087 | All Hands AI | Autonomous coding-agent platform. Self-hosted on Kubernetes inside a VPC. Model-agnostic. |
| [`cline/cline`](https://github.com/cline/cline) | Apache-2.0 | 66,214 | Cline | Plan-then-act loop with per-step human approval and cost transparency. VS Code extension shell + CLI. |
| [`crewAIInc/crewAI`](https://github.com/crewAIInc/crewAI) | MIT | 57,090 | CrewAI Inc | Role-based multi-agent collaboration. Independent of LangChain. |
| [`block/goose`](https://github.com/block/goose) | Apache-2.0 | 52,827 | Block | Local-first agent from Block (Jack Dorsey's fintech). Bring-your-own key, model-agnostic. |
| [`langchain-ai/langgraph`](https://github.com/langchain-ai/langgraph) | MIT | 39,709 | LangChain | Graph-based state machines for agent workflows. |
| [`deepseek-ai/deepseek-harness`](https://github.com/deepseek-ai/deepseek-harness) | MIT | 105,290 | DeepSeek | Plugin harness — see [EVAL-DEEPSEEK-HARNESS.md](./EVAL-DEEPSEEK-HARNESS.md). Not adopted for client-facing work: brand risk. |
| [`VoltAgent/voltagent`](https://github.com/VoltAgent/voltagent) | MIT | 10,362 | VoltAgent | TypeScript agent-engineering framework. Any provider. Smaller but honest. |

**Deliberately excluded from this register:**

- "OpenClaw / Hermes Agent / ZeroClaw" — repeated across several affiliate-style posts in the survey with inconsistent star counts, licensing claims, and repo URLs. When multiple secondary sources disagree on primary facts, doctrine/05 audit fails at requirement 4 (how long migration takes) because we cannot verify what we would be migrating from. Reopen if a stable primary repository appears.

## Connector fabrics — the layer hosted vendors actually charge for

Under a plugin harness, the connectors (Gmail, Slack, Notion, calendar, GitHub, drives) are tool plugins. The Model Context Protocol is the closest thing to a real open standard for this layer.

| Project | License | Stars | Notes |
|---|---|---|---|
| [`modelcontextprotocol/servers`](https://github.com/modelcontextprotocol/servers) | NOASSERTION (Apache-2.0 new / MIT existing) | 89,574 | Reference MCP server implementations: filesystem, git, memory, GitHub, Google Drive, Postgres, Slack, and others. Community-built servers are separately linked from this repo. |
| [`modelcontextprotocol/python-sdk`](https://github.com/modelcontextprotocol/python-sdk) | MIT | 24,009 | Official Python SDK for building MCP servers and clients. |
| [`modelcontextprotocol/registry`](https://github.com/modelcontextprotocol/registry) | NOASSERTION | 7,150 | Community-driven registry service for MCP servers. |
| [`perplexityai/modelcontextprotocol`](https://github.com/perplexityai/modelcontextprotocol) | MIT | — | Official Perplexity MCP server. Relevant because it means Perplexity search is reachable from any MCP-capable harness — not just from Perplexity Computer. |
| [`activepieces/activepieces`](https://github.com/activepieces/activepieces) | NOASSERTION | 23,798 | Self-hosted Zapier alternative. AI agents + MCP + workflow, one Docker container. Fair-code, not strict MIT. |
| [`n8n-io/n8n`](https://github.com/n8n-io/n8n) | NOASSERTION | 200,681 | Fair-code workflow automation, native AI. Self-hostable. |

---

## What this list means operationally

**For the harness / IDE layer.** The exit strategy that scores highest against doctrine/05 today is: use `sst/opencode`, `All-Hands-AI/OpenHands`, `cline/cline`, or `block/goose` for coding-agent work depending on whether you want terminal, autonomous, VS Code, or local respectively. All four are model-agnostic and BYOK. All four have healthy activity within the last 24 hours as of the baseline date. Any of them can be swapped for any other with minimal loss because the model provider and the connector fabric are the parts that carry your work, not the harness.

**For the connector layer.** MCP is the only spec at this stage that treats connectors as portable across harnesses. Adopting an MCP-native harness is a doctrine/05 win because tools written once run across every MCP client. This is the same "capability seams" pattern doctrine/05 wants — expressed at the protocol level rather than the code level.

**For your own harness work.** [[projects/glass-sovereign-agent]] and [[projects/agent-governance-ledger]] should conform to MCP at their tool boundary. That single decision keeps every one of the above harnesses on the table as substrate later.

---

## Refresh policy

- Refresh this table only when a reconsider trigger fires — a client asks about a specific tool, one of the above archives, a new candidate becomes primary reference for a client engagement, or one of our own projects picks one for a build.
- Do not refresh star counts as a routine — that is rung-6 spend for no decision.
- On refresh, verify license and archived status via `gh api repos/<owner>/<repo>` and record the new baseline date at the top.

---

© 2026 EVEglyphDesign. Controlled copy.
*Pour le bien-être du peuple.*
