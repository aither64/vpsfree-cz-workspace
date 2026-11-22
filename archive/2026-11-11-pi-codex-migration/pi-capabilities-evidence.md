# Pi capability evidence: preserving the current portal

Package C, implementer1. Read-only upstream investigation on 2026-11-11;
no installation, provider login, model request, build, service or deployment.
This is source evidence and migration analysis, not a live compatibility result.

## Revision and provenance

- Public repository: [earendil-works/pi](https://github.com/earendil-works/pi), default
  branch `main`, not archived according to the GitHub repository API.
- Fixed inspected head: [`a22b888a58fe55b668cc45b80749ec88d4eb4ddc`](https://github.com/earendil-works/pi/commit/a22b888a58fe55b668cc45b80749ec88d4eb4ddc),
  committed 2026-11-11 21:44:26 UTC. All source links below bind that revision.
- Latest GitHub release observed: [`v1.5.2`](https://github.com/earendil-works/pi/releases/tag/v1.5.2),
  published 2026-11-10 12:25:43 UTC, tag commit
  `b4afdddf44e059c67ccf5097e5317d913521b470`. Inspected coding-agent, durable and
  Chord manifests say `1.5.2`; `main` also contains unreleased changes. This
  investigation does not establish that every `main` behavior ships in that tag.
- Method: unauthenticated GitHub API repository/commit/release/tree reads and
  pinned raw official README, docs and relevant implementation reads. Disposable
  source copies are under `/tmp/pi-evidence-2026-11-11-implementer1`; the durable
  evidence is this Markdown. No other session files or worktrees were read.
- Session identity was verified by `dev-session current` and matching
  `DEV_SESSION_SLUG`/`DEV_SESSION_WORKSPACE`. Same-session roster confirms
  implementer1 owns implementation-purpose work with workspace-write access.

## Decisive answer for the provider-switch motivation

Pi already supports changing provider/model within one conversation. The CLI
`/model` picker and RPC `set_model {provider,modelId}` select a model;
`AgentSession.setModel()` checks provider authentication, changes the existing
agent's model, appends a model-change entry and adjusts thinking. It does not
replace the session. Defaults change only when explicitly persisted. This is a
native alternative to a runtime that needs a provider fixed at daemon/thread
creation. It supports investigating removal of the provider-switch patch or
worker workaround while retaining the portal. It does not prove that the present
portal adapter can use Pi unchanged. [Models][models], [RPC model commands][rpcmodels],
[setModel implementation][setmodel].

Pi-ai explicitly documents cross-provider handoffs: user messages, tool results,
assistant text and tool calls remain usable; reasoning from a different model
is dropped because signatures/encrypted thinking belong to the producing model.
This is history continuity, not identical reasoning replay. Model choice and
thinking changes persist in session history. Thinking is clamped to the selected
model's supported levels; changing provider can therefore change available
settings. [Cross-provider handoffs][handoffs], [thinking implementation][thinking].

No paid call or live credential use was performed. Exact existing account/model
access, custom Responses gateway behavior, preserved history on representative
large sessions, switching during active tool work, queues, goals and retained
member identities still need acceptance tests in the proposed bridge. Pi's own
session identity is not automatically the portal's member or conversation ID.

## Capability and dependency inventory

| Area | Source-supported capability | Integration implication / boundary |
| --- | --- | --- |
| TypeScript SDK | `@earendil-works/pi-coding-agent` embeds `createAgentSession`, direct session/model/tool/resource access, events, abort/wait, persistence and runtime session replacement. Node.js/Bun. [SDK][sdk] | An internal TypeScript bridge can own Pi sessions while the portal remains the product. SDK integration executes inside that bridge's process. |
| Subprocess RPC | Long-lived `pi --mode rpc`, JSONL stdin/stdout, correlated responses, streamed session events, prompting, steering, follow-up, abort, compaction, model/thinking, fork/clone/switch and state/history reads. [RPC][rpc], [command union][rpctypes] | Language-independent bridge fits existing non-TypeScript hosts. It is a child-process protocol, not a ready HTTP/WebSocket conversation service. Host supplies process ownership, routing, authentication and reconnect. |
| Custom tools and policy | SDK `customTools`, resource-loader inline/file extensions, `registerTool`, tool overrides, input/context/system-prompt hooks, `tool_call` block/mutate and `tool_result`. Tool-call handler exceptions block calls. [SDK][sdk], [tool policy][toolpolicy], [extension errors/modes][extmodes] | Policy and reporting tools can run as trusted host code. The RPC command union has no generic register-tool or dedicated provider-login command; deploy an extension or mediate through SDK/MCP. RPC forwards supported extension dialogs. |
| RPC completion | Successful prompt response means accepted/queued/handled. `agent_end` may precede retries/compaction/queued work; `agent_settled` means no automatic continuation. [RPC][rpc] | Existing completion, reporting and idle semantics need explicit event mapping. A request `id` is correlation, not documented durable admission deduplication. |
| Resume and reconnect | CLI `--continue`, `--resume`; JSONL session tree; RPC `get_entries {since}` has a durable entry-ID cursor including abandoned branches and pre-compaction entries, plus active `leafId`. [Sessions][sessions], [entry cursor][entrycursor] | Good transcript reconstruction building block. Entry cursor is not a replay log of every streamed token or durable job notification. Arbitrary browser/CLI reconnect to one live owner still belongs to the host. |
| Steering and abort | SDK/RPC distinguish steering after current assistant/tool batch from follow-up after pending work. Busy prompts require an explicit choice. Abort waits for idle. [SDK][sdk], [RPC][rpc] | Preserve portal controls by mapping them deliberately; do not equate steering with immediate preemption of an already-running shell command. |
| Fork, clone, compaction | Branch tree, separate-session fork and active-branch clone; automatic/manual compaction preserves original session entries. Provider-backed summary requests may fail. [Sessions][sessions], [format][format] | Existing fork/history UI can be retained through an adapter. Storage, branch IDs, summaries and old Codex transcript migration are different contracts. |
| Custom endpoints | `models.json` supports compatible endpoints, base URL overrides, model entries/overrides, auth/header interpolation or commands; provider extensions support custom auth, discovery and streaming. [Models][models], [custom providers][customproviders] | Current private `/v1` Responses endpoints are plausible candidates for native `openai-responses` integration. Exact gateway IDs, request fields, model catalogs and token-file behavior remain unverified. |
| Model catalog | Bundled catalog with runtime pi.dev overlays; cached catalog works offline, OpenRouter optionally refreshes an account-filtered catalog. [Models][models], [Providers][providers], [root README][root] | Pinning source alone does not freeze model data. Preserve the portal's independent catalog and validate/map IDs; do not silently replace it with upstream's picker. |
| Permissions / isolation | No built-in filesystem/process/network/credential permission system. Default is launcher's authority. Project trust controls loading resources, not tool access. External container/VM/sandbox patterns are documented. [Security][security], [root README][root] | Reuse the portal/runtime's existing permission boundary where applicable, or implement one. A confirmation extension or codemode JS sandbox does not isolate host tools or arbitrary extensions. |
| Instructions / skills | User and ancestor context files include AGENTS/CLAUDE and same-directory AGENTS.override; SYSTEM/APPEND_SYSTEM and resource loading are configurable. Skills use SKILL.md, descriptions loaded first, explicit `/skill:name`, `.pi/skills` and `.agents/skills`. [Configuration][configuration], [Skills][skills] | Existing workspace instructions and many skills are reusable text. Discovery paths, precedence, trust and invocation must be mapped; descriptions are not enforced skill execution. |
| MCP | Built-in CLI MCP: stdio and streamable HTTP, OAuth, tools/resources, direct/deferred/codemode exposure, permission hooks. Legacy SSE and rendering MCP Apps are unsupported. SDK must explicitly load MCP/codemode/tool-search extensions. [MCP][mcp], [SDK][sdk] | Existing tool servers may be reusable, but preserve exact transport, caller identity, policy and result contracts. It is incorrect to describe current Pi as having no native MCP. |
| Runtime requirements | Coding-agent/durable/Chord manifests require Node >=22.19, MIT license. Root offers Nix source builds; packages should be consumed as a coherent version set. [root README][root], [manifest][manifest], [license][license] | Packaging and bridge dependencies change internally. No package was installed or built here. |

## Providers, accounts and quota behavior

These are upstream adapter claims, not confirmation that the user's accounts
have an entitlement or that any particular model works.

| Connection | Exact evidence at inspected head | What is still unknown |
| --- | --- | --- |
| OpenAI API and ChatGPT subscription | `openaiProvider` has API-key auth and OAuth labeled "Sign in with ChatGPT" / ChatGPT subscription. OAuth filters classifier models because that endpoint rejects those credentials. [OpenAI factory][openaifactory] | Which current account types/models are granted access; behavior/limits of this user's subscription; equivalence to existing native OpenAI account handling. |
| OpenAI Codex subscription endpoint | Separate `openai-codex` factory uses `https://chatgpt.com/backend-api`, OAuth labeled ChatGPT Plus/Pro, no API-key method in that factory. [Codex factory][codexfactory] | Exact entitled Codex model set and current provider-side policy. A catalog entry is not access proof. |
| Anthropic | Factory supports API key and subscription OAuth labeled Claude Pro/Max; provider docs also describe token/federation cases. [Anthropic factory][anthropicfactory], [Providers][providers] | Actual subscription entitlement/endpoint acceptance and account restrictions. |
| GitHub Copilot | Factory supports token environment auth and subscription OAuth, with account-derived endpoint behavior. [Copilot factory][copilotfactory] | Existing account policy, enabled models and rate limits. |
| Other hosted/local providers | Official provider list includes OpenRouter, Google, Bedrock, Azure and others; provider-specific API keys, ambient credentials, dynamic discovery or extension-defined auth differ. [Providers][providers], [AI auth][aiauth] | No blanket claim that all OAuth files, accounts or catalog models are available to this user. |
| Private load balancer and token files | Compatible endpoints and custom provider auth/discovery can be configured or implemented. `auth.json`, environment, command-resolved credentials and custom provider flows are documented. [Models][models], [custom providers][customproviders] | Current custom `/v1/models`, `/v1/usage`, token files, quota/reset previews and their authentication contracts are not established as native Pi features by the inspected sources. |

Pi records per-request/session token and cost usage and exposes provider response
header hooks, including rate-limit examples. Those are useful adapter inputs;
they are not evidence of equivalent account quota and reset operations. The
inspected RPC command union has no native subscription-quota/reset command.
Existing portal quota previews can remain host-owned and need not become prompt
admission gates. [Provider response headers][providerheaders], [RPC types][rpctypes].

Credentials are separate per provider. Model availability filters configured
auth; refreshing credentials and changing models do not establish entitlement.
OAuth flows are Node-only in pi-ai; web apps need a backend/proxy. Headless flows
can accept a pasted redirect/code where supported. Native/custom auth can be
integrated without exposing credentials to the browser. [AI auth][aiauth],
[browser usage][browser], [Providers][providers].

## Planning, subagents and durable orchestration

The coding-agent README explicitly says subagents and plan mode are omitted
from the core product; examples/packages supply them. This is compatible with
keeping the current portal's team orchestration instead of adopting another UI.
[Coding-agent README][clireadme].

The plan-mode example disables built-in `edit` and `write`, preserves other
active tools, and filters only calls named `bash` using regular expressions.
It extracts numbered `Plan:` text and `[DONE:n]` markers and persists example
state. Its execution prompt is UI-dependent (`ctx.hasUI`; RPC supports dialogs,
print/JSON do not). This is a concrete workflow implementation, not a complete
read-only enforcement boundary: preserved custom/MCP tools can have side effects,
and the regex allows arbitrary `awk` programs without interpreting their effects.
There is no all-tool authorization or shell-language safety proof. Keep any
required portal planning gate in trusted host policy, covering nested tools,
direct bash, MCP and execution transitions. [Plan implementation][plan],
[filter implementation][planfilter], [extension modes][extmodes].

The coding-agent subagent example launches separate `pi` processes, supports
single/parallel/chain dispatch and abort propagation, and uses Markdown agent
definitions. It is not the current portal's retained-role, member-identity,
durable delivery and recovery contract. [Subagent example][subagent].

Current upstream also has `@earendil-works/pi-durable`, a separate harness with
storage-before-publication, durable submissions keyed by `requestId`, owned
conversations/forks, tasks, gates and crash recovery. Its background-subagent
example supports spawn/message/steer/stop/list with restart-safe answer reporting.
Tool execution intent is committed before running: interrupted tools rerun only
when declared replay-safe; external effects still require idempotency. One
process writes each storage; SQLite uses WAL/NORMAL (process crash protection,
latest commits may be lost on power/host failure). JSONL optionally fsyncs.
Reconnecting views start from current state, not event replay. These are useful
building blocks, not proof of turnkey portal-team parity or automatic
coding-agent SDK/resource/MCP parity. [Durable README][durable]. Architect0 owns
the architectural tradeoff; preserving orchestration with a coding-agent bridge
does not require adopting this separate substrate.

### MCP caller identity is an explicit adaptation

The inspected built-in MCP bridge's `execute(_toolCallId, ...)` ignores its
tool-call ID and sends only tool arguments plus signal, timeout and progress.
`McpClient.callTool()` constructs `tools/call {name,arguments}`; request options
have no caller metadata field. Its `_meta` injection is a progress token.
No native portal session/member identity equivalent was found on this path.
Consequently report-to-lead and peer communication require trusted caller-bound
bridge identity, not a model-supplied argument. This is a source finding about
the inspected path, not an exhaustive claim that extensions cannot add metadata.
[MCP tool bridge][mcpbridge], [MCP client][mcpclient].

## Web and CLI access without a portal redesign

The ordinary `pi` CLI provides a TUI, print/JSON modes and RPC. The SDK/RPC
can back the existing portal; neither is a packaged authenticated web service.
The host must own one active runtime per conversation/member and expose the
browser and any CLI attachment to that runtime. Opening the same session file
from independent processes is not a demonstrated concurrent-access contract.
[RPC][rpc], [SDK][sdk], [Sessions][sessions].

There is a real browser app at `apps/p2`: a self-hosted Pi Durable UI with web
and TUI clients of the same server, provider API-key/OAuth UI and remote owner
access. However its README starts with an explicit warning: **experimental,
unsupported prototype, will be replaced, data formats/APIs change without
notice; do not build on it or use it for dependencies**. It is not a stable
replacement recommendation for the user's existing portal. There is no listed
legacy `packages/web-ui` package in this inspected tree. Chord has reusable web,
HTTP, worker and terminal surfaces, which are lower-level frameworks.
[p2 README][p2], [root package list][root].

## What can stay and what needs adaptation

This is a boundary assessment based on upstream source and the lead's current
portal contract, not an independent audit of the portal implementation.

| Classification | Concrete boundary |
| --- | --- |
| Stays unchanged in the intended product | Existing portal layout, navigation, conversation/member identities, roles, session lifecycle, queue/goals UI, provider picker workflow and quota preview behavior can remain host-owned. Pi does not require adopting p2, Pi's TUI or its picker. Existing instruction/skill content and MCP business tools can be reused after contract checks. |
| Internal adaptation | Replace the Codex runtime client with SDK/RPC bridge; map model/provider defaults and per-member settings; map streaming, settled/abort/steer/fork/compaction; bind custom reporting tools to authenticated caller identity; preserve durable prompt admission and queued delivery; translate/preserve histories; adapt credentials/catalog/quota endpoints; package Node/Pi coherently and preserve sandbox policy. |
| Potential visible differences to decide/test | Model-dependent thinking choices; prior-model reasoning is omitted on handoff; token/cost estimates, compaction summaries and error wording may differ; switching while busy needs defined timing. Provider account access and catalog differences can affect available choices. None requires a portal redesign. |
| Optional parity, not primary migration gate | Pi TUI custom renderers, p2 UI, experimental durable teams, new remote environments and new orchestration features. The immediate acceptance target is provider switching with the current portal experience. |

## Stability, migration and bounded gaps

Root/package license is MIT. The repository is active at the observed date,
with recent release/source activity and public docs/tests/examples. That is
maintenance evidence, not an SLA or API stability promise. Coding-agent changelog
contains recent breaking sections, removed experimental server/client/protocol
packages, and fixes involving SDK/RPC/MCP/auth shutdown. Keep the adapter behind
an explicit pinned compatibility contract. p2's warning is stronger and explicit.
[License][license], [changelog][changelog], [p2][p2].

Coding-agent sessions are versioned JSONL, current format v3; v1/v2 migrate on
load. Source rewrites the file when migrating, and the version comparison simply
skips migration for versions >= current. This does not establish that older
versions can safely load newer entries, tools or provider metadata. No downgrade
round trip was verified. Retain original transcript/state backups and test the
chosen source/target versions before any migration. Durable storage is a separate
format, not a transparent replacement for CLI sessions or Codex persistence.
[Format][format], [migration source][migration], [rewrite source][rewrite].

First-pass acceptance gaps, deliberately not expanded into implementation:

1. Run representative same-session provider switches against the exact private
   Responses gateway and chosen accounts/models, preserving text/tool history,
   identity, queues/goals and member settings; test idle and in-flight changes.
2. Specify and test durable host admission/retry/reconnect, cancellation and
   reporting identity. Do not reuse RPC correlation IDs as deduplication keys
   without a host-owned receipt contract.
3. Validate required quota/reset preview and dynamic catalog UX through existing
   host integrations or custom provider adapters, without assuming native parity.
4. Define transcript import/rollback and immutable source/catalog/version inputs;
   verify planning/sandbox coverage across all enabled tools.

Only the assigned evidence Markdown changed. No commits, branches, migrations,
application edits or external writes were made. Routine investigation/evidence
does not trigger automatic substantive-change review. Lead owns acceptance,
state/plan linking and synthesis.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-11-pi-codex-migration/>

[root]: https://github.com/earendil-works/pi/blob/a22b888a58fe55b668cc45b80749ec88d4eb4ddc/README.md
[clireadme]: https://github.com/earendil-works/pi/blob/a22b888a58fe55b668cc45b80749ec88d4eb4ddc/packages/coding-agent/README.md#L15
[manifest]: https://github.com/earendil-works/pi/blob/a22b888a58fe55b668cc45b80749ec88d4eb4ddc/packages/coding-agent/package.json
[license]: https://github.com/earendil-works/pi/blob/a22b888a58fe55b668cc45b80749ec88d4eb4ddc/LICENSE
[sdk]: https://github.com/earendil-works/pi/blob/a22b888a58fe55b668cc45b80749ec88d4eb4ddc/packages/coding-agent/docs/sdk.md
[rpc]: https://github.com/earendil-works/pi/blob/a22b888a58fe55b668cc45b80749ec88d4eb4ddc/packages/coding-agent/docs/rpc.md
[rpctypes]: https://github.com/earendil-works/pi/blob/a22b888a58fe55b668cc45b80749ec88d4eb4ddc/packages/coding-agent/src/modes/rpc/rpc-types.ts#L20
[rpcmodels]: https://github.com/earendil-works/pi/blob/a22b888a58fe55b668cc45b80749ec88d4eb4ddc/packages/coding-agent/docs/rpc-commands.md#L208
[entrycursor]: https://github.com/earendil-works/pi/blob/a22b888a58fe55b668cc45b80749ec88d4eb4ddc/packages/coding-agent/docs/rpc-commands.md#L689
[setmodel]: https://github.com/earendil-works/pi/blob/a22b888a58fe55b668cc45b80749ec88d4eb4ddc/packages/coding-agent/src/core/agent-session.ts#L2657
[thinking]: https://github.com/earendil-works/pi/blob/a22b888a58fe55b668cc45b80749ec88d4eb4ddc/packages/coding-agent/src/core/agent-session.ts#L2784
[handoffs]: https://github.com/earendil-works/pi/blob/a22b888a58fe55b668cc45b80749ec88d4eb4ddc/packages/ai/README.md#L1582
[models]: https://github.com/earendil-works/pi/blob/a22b888a58fe55b668cc45b80749ec88d4eb4ddc/packages/coding-agent/docs/models.md
[providers]: https://github.com/earendil-works/pi/blob/a22b888a58fe55b668cc45b80749ec88d4eb4ddc/packages/coding-agent/docs/providers.md
[customproviders]: https://github.com/earendil-works/pi/blob/a22b888a58fe55b668cc45b80749ec88d4eb4ddc/packages/coding-agent/docs/custom-provider.md
[openaifactory]: https://github.com/earendil-works/pi/blob/a22b888a58fe55b668cc45b80749ec88d4eb4ddc/packages/ai/src/providers/openai.ts#L9
[codexfactory]: https://github.com/earendil-works/pi/blob/a22b888a58fe55b668cc45b80749ec88d4eb4ddc/packages/ai/src/providers/openai-codex.ts#L7
[anthropicfactory]: https://github.com/earendil-works/pi/blob/a22b888a58fe55b668cc45b80749ec88d4eb4ddc/packages/ai/src/providers/anthropic.ts#L75
[copilotfactory]: https://github.com/earendil-works/pi/blob/a22b888a58fe55b668cc45b80749ec88d4eb4ddc/packages/ai/src/providers/github-copilot.ts#L24
[aiauth]: https://github.com/earendil-works/pi/blob/a22b888a58fe55b668cc45b80749ec88d4eb4ddc/packages/ai/README.md#L376
[browser]: https://github.com/earendil-works/pi/blob/a22b888a58fe55b668cc45b80749ec88d4eb4ddc/packages/ai/README.md#L1692
[providerheaders]: https://github.com/earendil-works/pi/blob/a22b888a58fe55b668cc45b80749ec88d4eb4ddc/packages/coding-agent/docs/extensions.md#L873
[sessions]: https://github.com/earendil-works/pi/blob/a22b888a58fe55b668cc45b80749ec88d4eb4ddc/packages/coding-agent/docs/sessions.md
[format]: https://github.com/earendil-works/pi/blob/a22b888a58fe55b668cc45b80749ec88d4eb4ddc/packages/coding-agent/docs/session-format.md
[migration]: https://github.com/earendil-works/pi/blob/a22b888a58fe55b668cc45b80749ec88d4eb4ddc/packages/coding-agent/src/core/session-manager.ts#L337
[rewrite]: https://github.com/earendil-works/pi/blob/a22b888a58fe55b668cc45b80749ec88d4eb4ddc/packages/coding-agent/src/core/session-manager.ts#L1093
[toolpolicy]: https://github.com/earendil-works/pi/blob/a22b888a58fe55b668cc45b80749ec88d4eb4ddc/packages/coding-agent/docs/extensions.md#L971
[extmodes]: https://github.com/earendil-works/pi/blob/a22b888a58fe55b668cc45b80749ec88d4eb4ddc/packages/coding-agent/docs/extensions.md#L3250
[security]: https://github.com/earendil-works/pi/blob/a22b888a58fe55b668cc45b80749ec88d4eb4ddc/packages/coding-agent/docs/security.md
[configuration]: https://github.com/earendil-works/pi/blob/a22b888a58fe55b668cc45b80749ec88d4eb4ddc/packages/coding-agent/docs/configuration.md
[skills]: https://github.com/earendil-works/pi/blob/a22b888a58fe55b668cc45b80749ec88d4eb4ddc/packages/coding-agent/docs/skills.md
[mcp]: https://github.com/earendil-works/pi/blob/a22b888a58fe55b668cc45b80749ec88d4eb4ddc/packages/coding-agent/docs/mcp.md
[mcpbridge]: https://github.com/earendil-works/pi/blob/a22b888a58fe55b668cc45b80749ec88d4eb4ddc/packages/coding-agent/src/extensions/mcp/tools.ts#L275
[mcpclient]: https://github.com/earendil-works/pi/blob/a22b888a58fe55b668cc45b80749ec88d4eb4ddc/packages/mcp/src/client.ts#L378
[plan]: https://github.com/earendil-works/pi/blob/a22b888a58fe55b668cc45b80749ec88d4eb4ddc/packages/coding-agent/examples/extensions/plan-mode/index.ts#L95
[planfilter]: https://github.com/earendil-works/pi/blob/a22b888a58fe55b668cc45b80749ec88d4eb4ddc/packages/coding-agent/examples/extensions/plan-mode/utils.ts#L7
[subagent]: https://github.com/earendil-works/pi/blob/a22b888a58fe55b668cc45b80749ec88d4eb4ddc/packages/coding-agent/examples/extensions/subagent/README.md
[durable]: https://github.com/earendil-works/pi/blob/a22b888a58fe55b668cc45b80749ec88d4eb4ddc/packages/durable/README.md
[p2]: https://github.com/earendil-works/pi/blob/a22b888a58fe55b668cc45b80749ec88d4eb4ddc/apps/p2/README.md#L1
[changelog]: https://github.com/earendil-works/pi/blob/a22b888a58fe55b668cc45b80749ec88d4eb4ddc/packages/coding-agent/CHANGELOG.md
