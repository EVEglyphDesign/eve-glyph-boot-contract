# EVAL-ELEVENLABS-HOSTED-MCP

**Subject:** ElevenLabs hosted MCP server — [`https://api.elevenlabs.io/v1/mcp`](https://elevenlabs.io/docs/eleven-agents/operate/hosted-mcp)
**Date:** 2026-09-30
**Reviewer:** operating agent, on behalf of Dany Theriault
**Precedent:** [EVAL-DEEPSEEK-HARNESS](EVAL-DEEPSEEK-HARNESS.md) (shape) · session 2026-09-30 "Is this something we can add to our harness" (direction: optional, governed voice-agent capability)
**Status:** evaluated · conditionally compatible · pilot proposed, not adopted

---

## What it is

A remote MCP server, hosted by ElevenLabs, that lets an assistant manage the ElevenAgents (voice and chat agents) in one ElevenLabs workspace. It replaces the local open-source server, which was deprecated and archived on 2026-08-22 ([ElevenLabs changelog](https://elevenlabs.io/docs/changelog/2026/8/22); [elevenlabs-mcp repository](https://github.com/elevenlabs/elevenlabs-mcp)).

| Field | Value | Source |
|---|---|---|
| Endpoint (global) | `https://api.elevenlabs.io/v1/mcp` — advertises canonical resource `https://api.us.elevenlabs.io/v1/mcp` | live probe, 2026-09-30 17:14 UTC |
| Residency endpoints | EU `api.eu.residency…`, India `api.in.residency…`, Singapore `api.sg.residency…` — separate accounts, separate OAuth issuers | [Hosted MCP docs](https://elevenlabs.io/docs/eleven-agents/operate/hosted-mcp); live probe |
| Transport | Streamable HTTP, POST only (`GET` returns `405 allow: POST`); no SSE stream | live probe |
| Authentication | OAuth 2.1 bearer only. API keys rejected (`xi-api-key` → `401 OAuth bearer token required`) | live probe |
| Supported clients (vendor) | Claude, Claude Code, Cursor, ChatGPT, GrokBot, Hermes | [ElevenLabs MCP page](https://elevenlabs.io/mcp) |
| Local server | Deprecated, archived, no updates | [changelog](https://elevenlabs.io/docs/changelog/2026/8/22) |

---

## 1. Server specification — verified live

Probed unauthenticated from the sandbox. Nothing below is inferred from marketing copy.

1. **Discovery is standards-conformant (MCP 2025-06-18 authorization).** An unauthenticated `initialize` returns `401` with `WWW-Authenticate: Bearer resource_metadata="https://api.us.elevenlabs.io/.well-known/oauth-protected-resource"`. Protected-resource metadata (RFC 9728) names the authorization server `https://api.us.elevenlabs.io`, `bearer_methods_supported: ["header"]`.
2. **Authorization-server metadata (RFC 8414)** at `/.well-known/oauth-authorization-server`:

   | Field | Value |
   |---|---|
   | `authorization_endpoint` | `https://elevenlabs.io/app/oauth/authorize` |
   | `token_endpoint` | `https://api.us.elevenlabs.io/v1/oauth/token` |
   | `revocation_endpoint` | `https://api.us.elevenlabs.io/v1/oauth/revoke` |
   | `grant_types_supported` | `authorization_code`, `refresh_token` |
   | `code_challenge_methods_supported` | `S256` (PKCE mandatory) |
   | `token_endpoint_auth_methods_supported` | `none`, `client_secret_post`, `private_key_jwt` (RS256) |
   | `client_id_metadata_document_supported` | `true` (CIMD) |
   | `authorization_response_iss_parameter_supported` | `true` (RFC 9207) |
   | `registration_endpoint` | **absent** — `POST /v1/oauth/register` returns `404` |
   | OpenID configuration | none (`404`) — OAuth only, no ID token |

3. **Scopes advertised:** `convai_read`, `convai_write`, `text_to_speech`, `speech_history_read`, `flows`, `image_video_generation`, `voice_generation`. The docs describe the grant as "ElevenAgents read and write operations and Text to Speech"; the live metadata is broader (creative flows, image/video, voice generation, speech history). Scopes are workspace-wide — there is no per-agent scope.

**Consequence.** A client connects in one of two ways only: it publishes a Client ID Metadata Document (an HTTPS URL used as `client_id`), or it is a client ElevenLabs has pre-registered. There is no dynamic client registration and no self-service OAuth app registration was found in the public docs.

---

## 2. OAuth flow — step by step

1. Client `POST /v1/mcp` → `401` + `resource_metadata` pointer.
2. Client reads protected-resource metadata → authorization server `api.us.elevenlabs.io`.
3. Client reads authorization-server metadata → endpoints, PKCE S256, CIMD.
4. Client redirects the operator to `elevenlabs.io/app/oauth/authorize` with `client_id` = its CIMD URL, `code_challenge` (S256), requested scopes, `resource` = the canonical US resource URI. Operator signs in, **chooses the workspace**, reviews scopes, selects **Authorize** ([Hosted MCP docs](https://elevenlabs.io/docs/eleven-agents/operate/hosted-mcp)).
5. Redirect back with `code` and `iss`; client verifies `iss`, exchanges code + verifier at the token endpoint; receives access and refresh tokens.
6. Revocation: from the MCP client, from ElevenLabs account settings, or `POST /v1/oauth/revoke`.

**Residency trap.** For EU, India or Singapore workspaces the global connector is wrong: add a custom connector at the regional URL and sign in with the regional account, not the elevenlabs.io account.

---

## 3. Exposed agent-management tools — classified in three

Authoritative capability list ([Hosted MCP docs](https://elevenlabs.io/docs/eleven-agents/operate/hosted-mcp)): create agents; update any setting (prompt, voice, language, first message); list, inspect, compare; read recent conversations and full transcripts; explore conversation topics; duplicate and delete; estimate LLM usage and cost; retrieve widget configuration and share link; check knowledge-base size; generate speech as a short-lived link.

A third-party listing enumerates **106 tools** ([Gumloop ElevenLabs MCP page](https://www.gumloop.com/mcp/elevenlabs)) — 79 agent tools, 26 creative tools, plus `Get More Tools`. **Unverified:** the definitive set requires an authenticated `tools/list`, which this audit could not run without an OAuth grant. The Docker image listing 27 tools is the deprecated local server and is out of scope.

| Class | Tools (from the 106-tool listing) | Harness treatment |
|---|---|---|
| **Read** | agents list/get/summaries/widget/link/knowledge size/calculate LLM usage; conversations list/get/search messages; topics; branches/versions get; KB list/get/search/RAG query/dependents; tools list/get/executions; MCP servers list/get/tools; tests list/get/runs; phone numbers list/get; triage tickets list/get | Auto-approve. Transcripts carry caller PII — read access is still a data-exposure decision |
| **Write, reversible** | agents create/update/duplicate/create draft/create branch/update branch; procedures create/draft/compile; KB create text/url/folder, update; tools create/update; tests create/run; triage create/update/comment; creative generation (spends credits) | Require approval per call. Land the resulting agent config in the repo |
| **Destructive or externally consequential** | agents delete; delete draft/procedure; KB delete and bulk delete/bulk move; tool delete; MCP server create/update/delete; phone number update/delete; create deployment; merge branch; triage delete | Disabled by default at admin level. Enabled only by named operator override, labelled **irreversible** where no inverse exists |

Two tools deserve naming: **create/update MCP server** lets the harness wire an external MCP server into a live agent (the reverse direction below), and **create deployment / merge branch** pushes changes to callers immediately — the vendor markets this as "push it live in the same turn" ([ElevenLabs MCP page](https://elevenlabs.io/mcp)).

---

## Compatibility with the assistant harness

| Harness surface | Result | Reason |
|---|---|---|
| **Claude / Claude Code** | **Compatible now** | Listed in the Claude directory; Claude uses Anthropic's hosted client metadata (CIMD); admin can disable tools org-wide and users cannot re-enable them ([Hosted MCP docs](https://elevenlabs.io/docs/eleven-agents/operate/hosted-mcp)) |
| **Perplexity Computer (custom remote connector)** | **Unverified — likely blocked** | Perplexity OAuth connectors need dynamic registration or a pasted Client ID/Secret ([Perplexity Help Center](https://www.perplexity.ai/help-center/en/articles/13915507-adding-custom-remote-connectors)); ElevenLabs offers neither publicly, and Perplexity does not document CIMD. One connect attempt settles it. No native ElevenLabs connector exists in this workspace |
| **Perplexity Computer via REST/CLI** | **Compatible, different path** | The same operations exist in the REST API and the ElevenLabs CLI ("manage agents as code with version control"), authenticated with a scoped API key — not the hosted MCP |

Cross-harness rule holds: whichever surface writes, the agent configuration and action receipt land in the repository so the other harness reads rather than cold-starts ([`ACTIVE.md`](ACTIVE.md)).

### Reverse direction — ElevenLabs agent calling a harness MCP server

- Transports: SSE and Streamable HTTP. Auth to our server: a static **secret token** (Authorization header) or custom headers — no OAuth ([ElevenLabs MCP integration](https://elevenlabs.io/docs/eleven-agents/customization/tools/mcp)).
- Approval modes: **Always Ask** (recommended), **Fine-Grained Tool Approval** (auto-approved / requires approval / disabled per tool), **No Approval**.
- **Governance gap:** MCP is off by default, but *any* member or API key with `convai_write` can enable it workspace-wide by accepting the MCP terms — not restricted to admins.
- **Exclusion:** unavailable on Zero Retention Mode or HIPAA workspaces.
- Conversation data, including caller input, is sent to our server; ElevenLabs publishes static egress IPs for allowlisting ([MCP integration security](https://elevenlabs.io/docs/eleven-agents/customization/tools/mcp/security)).

---

## Conformance against the canon

| Canon rule | Fit | Gap and control |
|---|---|---|
| EgD-BOOT-008 Reader / Writer / Linker | Partial | Reader = grant `convai_read` only. Writer cannot be narrowed to one agent by scope — enforce in client tool settings and by one named agent per task |
| EgD-BOOT-004 / 005 repository record, versioned and reversible | Partial | Hosted MCP changes live state with no commit. Export agent config to the repo (CLI) before and after every write; the diff is the inverse. Deletes and deployments are irreversible rows |
| EgD-BOOT-002 spend | Partial | `calculate LLM usage` gives a pre-change cost estimate; creative tools spend ElevenLabs credits outside the Burn Ledger |

---

## Decision — three options

1. **Pilot read-only on Claude now.** Grant `convai_read` only; admin-disable every write and destructive tool; use for transcript review, topic analysis and cost estimates. Lowest risk, usable today.
2. **Operate through REST/CLI from the Perplexity harness.** Scoped API key held as a credential, agent configs as code in a repository, every change a commit with an inverse. Full control, more setup, no hosted MCP.
3. **Hold until a Perplexity connect test.** One connect attempt at the hosted URL; adopt option 1 on Perplexity if CIMD works, otherwise stay on option 2.

**Recommendation:** option 1 for the pilot, with option 2 as the write path once a named agent is in scope. The reverse direction stays read-only (search and retrieve tools only, Always Ask for anything else) per the 2026-09-30 direction.

---

© 2026 EVEglyphDesign. All rights reserved. Controlled copy.
*Pour le bien-être du peuple.*
