# Pi extensions: bounded findings for the current backend follow-up

Architect1, 2026-11-20. Source-only investigation complete; no application edits,
checks/builds, live Pi calls, log/transcript reads, package changes or peer-session
actions. Own session and live roster verified; saved Astra/xhigh/design/workspace_write
unchanged. Previous package is terminal. This packet contains only pinned-source
facts, not user transcript/envelope content. Main owns implementation allocation;
architect0 owns the overall backend/interface brief and owner0 owns latency.

## Recommendation

Keep the current SDK custom tools and authenticated host callback path. Pi
extensions already underpin it. Moving the same tools to `pi.registerTool` or
replacing delivery with custom messages would not fix the reported portal display
and receipt gaps. The smallest useful change is to project the existing trusted
communication/team origin and original delivery receipt into the portal's common
transcript representation, retaining its exact native entry anchor. Architect0
should fit that projection to the existing shared interface; this packet does not
freeze a new field or duplicate that inventory.

For an additional approved model-callable communication operation, use one inert
SDK tool definition and the existing HostBridge/domain handler, exactly as current
reporting tools do. This is a possible later missing-tool implementation boundary,
not a recommendation to create a second transport, extension bus, scheduler or
receipt store. Do not add tools merely to repair display labels.

## Exact pinned inputs and current machinery

R is `25b679656bbd63d8e13406f0e2bcaec45bfa1d89`, immutable source
`/nix/store/wf6yazj31l9bh9lzzlzl5qxv3ms13hf0-source` (R below). The supplied selected
app is `/nix/store/gh680l33jv55f0pxnfi4sca1nmjcavl4-dev-workspace-0.2.0`.
Its existing `share/dev-workspace/pi-worker.json` identifies worker protocol2,
Node22.23.2, worker `/nix/store/19vlbpqm8bryky9bvvx38dr1gybp5and-dev-workspace-pi-worker`
and SDK `/nix/store/9hf2a7rz231w2pn50s4jlmrgs4007xc5-pi-1.5.2`.
SDK references below are relative to that package's
`lib/pi/node_modules/@earendil-works/pi-coding-agent` (P).
R `pi-runtime/upstream.json:1` pins revision
`a22b888a58fe55b668cc45b80749ec88d4eb4ddc`, manifest version1.5.2; the R guide
explicitly distinguishes this main-source revision from release-tag equivalence.
No f4/source3 updater or target upgrade inspection was used.

- R `pi-runtime/src/package.mjs:5` imports the public SDK export. `session.mjs:379-436`
  constructs `ModelRuntime.create`, `SettingsManager.create`,
  `DefaultResourceLoader` with trusted inline `extensionFactories`,
  `SessionManager.create/open`, `createAgentSession`, then `bindExtensions({})`.
  Ambient extensions, skills, templates and themes are disabled. The public runner
  command context is used only to inspect the bound system-prompt options.
- R `protocol.mjs:80-106` supplies `HostBridge.tools(names)` through SDK
  `customTools`. `host-bridge.mjs:56` exposes the admitted reporting, monitor,
  question and plan definitions; it has no session_communication definition in
  this selected source. This states only that factory's scope, not absence of
  every other communication entry point. `host-tools/reporting.mjs:23-54` passes
  native toolCallID and AbortSignal outside model arguments and returns the domain
  disposition/outcome in content plus structured tool-result details.
- R `tool-policy.mjs:40-58` already uses extension events: before_agent_start,
  tool_call, execution start/end and agent_settled. It enforces the exact retained
  tool set; `lineage.mjs:93` cancels tree/fork/switch changes. P
  `dist/core/agent-session.js:2973-3018` combines registerTool definitions and SDK
  customTools into the same registry/wrappers. A different registration spelling
  does not create better permissions, receipts or portal rendering.
- R `session.mjs:89-114` subscribes to public events and associates the exact user
  object, waiting until append before inspecting persisted history. Input uses
  literal `session.prompt(...,{expandPromptTemplates:false})` when idle and public
  `session.agent.steer/followUp(originalObject)` when active (`:233-281`). It then
  proves the native entry by public SessionManager reopen and syncs history.
  `HostBridge.call:14-38` waits for that original witness/commit before forwarding;
  `lineage.mjs:69-82` verifies the native assistant tool call after that user entry.
  Supervisor/domain authority remains essential; a tool event is not that authority.

## What the pinned extension APIs can and cannot provide

| API / source | Useful capability | Limit relevant here |
| --- | --- | --- |
| `registerTool`, SDK `customTools`; P docs/sdk.md:104-116, docs/extensions.md:1575 | Typed model tools, arguments, tool-call identity, signal, structured result details and normal lifecycle events | Already used through the same registry. Model arguments cannot supply trusted caller/from/to authority. Tool completion alone is not recipient acceptance. |
| `sendMessage` / AgentSession.sendCustomMessage; P docs/extensions.md:1627, dist/core/agent-session.js:1953-1999 | `customType`, content, display and details; steer/followUp/nextTurn; optional idle turn trigger | Extension `sendMessage` returns void; binding at :2867 catches/report errors asynchronously. Even awaiting AgentSession's method supplies no durable external operation ID/dedup/acceptance receipt. Steer is still a queue at a safe boundary. |
| Custom-message details; P dist/core/session-manager.js:960-980, messages.js:89 | Structured persisted metadata excluded from model context; content becomes a user-role model message | `custom_message` replaces the native input shape, not just its display. Current witness and callback-origin readers require type=message/role=user. Fresh custom-only history does not flush until a real user/assistant message exists (`_hasConversation`, session-manager.js:801-819). |
| `appendEntry`; P docs/extensions.md:1683, session-manager.js:922 | Custom extension state, outside model context, readable on reopen | Adds history and has the same fresh-history persistence limitation. It is not an atomic domain/native receipt transaction and cannot manufacture provenance for old inputs. No reason to add it for the reported display fixes. |
| `registerMessageRenderer` / `registerEntryRenderer`; P docs/extensions.md:1805 and types.d.ts:1292 | Pi interactive/TUI presentation of custom entries | Does not render the portal's browser transcript or decide its Messages/Sessions filter. The Go/common browser projection still needs the correct origin semantics. |
| `pi.events`; P docs/extensions.md:1965, dist/core/event-bus.js:1-25, resource-loader.js:262 | In-process extension notifications | Default loader owns a local EventEmitter; emit is void, handlers are not durably awaited and errors are logged. It is no cross-session transport, authenticated address space or recoverable receipt. Do not share it across members to bypass host authority. |
| `subscribe`, agent_start/agent_settled/tool events; P docs/sdk.md:74-96, docs/extensions.md:663-695 | Existing worker activity and invalidation | agent_end is not final idle; retries/queued work may follow. Events are observations, not a source of missing historical elapsed time or complete external effect drain. |

The selected worker already produces activity counts/timing in
R `pi-runtime/src/activity.mjs:1-83`, consumes those public events, and exposes
`activity_v1` in `protocol.mjs:116`. Therefore the all-dash report does not establish
an SDK event deficiency or a need for another extension. Coverage begins at worker
attachment and remains explicitly partial; tab changes should not be treated as
new SDK coverage. The exact portal cause belongs to architect0's trace.
P docs/sdk.md:64-69 and docs/extensions.md:1643-1646 explicitly define steering
as queued until the assistant/tool boundary. No extension change alone can promise
instant interruption. That semantic fact does not explain the user's multi-second
Sending interval; owner0 is tracing it separately.

## Smallest implementation fit and retained compatibility

R `portal/internal/piruntime/transcript_snapshot.go:12-58` already joins validated
native EntryID to original OperationID and wire Digest. Its owning producer in
`conversation.go:514-553` admits the original receipt generation and exact mapped
conversation before returning that tuple. Use this trusted correlation, joined to
the existing communication/team record by its original ref, to supply provenance
for shared display. Keep sender/recipient labels from authoritative saved domain
identities. Do not guess from text, timestamps or a model-authored customType;
missing proof remains unavailable. This is a proposed composition, not a claim
that the current snapshot already carries all from/to labels.

Display-only repair needs no native history rewrite or new tool registration.
Retain ordinary user entries, original IDs/digests, Pending/Unknown/NotSubmitted and
Accepted semantics. Reopening old history must retain its full content even when
provenance cannot be proven; it must not resend or reclassify an uncertain input
as accepted. Existing custom entries, if encountered, do not establish authority
merely by their shape.

A genuine new host tool requires the existing factory/whitelist/domain admission
plus retained RegisteredCeiling/upgrade design. Dynamic registerTool after startup
would violate the current exact tool policy (`tool-policy.mjs:29-37,70-74`), and
AttachHost reconnect cannot expand a captured tool set (R docs/pi-runtime.md:364).
Do not enable ambient extensions or use reload to bypass this boundary. Existing
workers keep their frozen app/SDK package; only the ordinary ready-session upgrade
may replace them after idle/effect drain, preserving native IDs/history/settings/
receipts (R docs/pi-runtime.md:271-329). Old extension contexts and subscriptions
must be rebound after replacement (P docs/sdk.md:56-60). The already completed
reported target upgrade is not redone or used to claim unrelated capabilities.

If custom-message input becomes a separately requested feature, it needs an owning
versioned witness/history/callback-origin and old/new-reader contract, including
first-input persistence, active steering, crash before/after commit and retained
reopen. That larger change is unnecessary for the present portal symptoms.

## Next action and finite acceptance

Architect0 can incorporate the existing-proof projection into its smallest shared
backend contract brief. Keep current tools/events for native integration; no new
extension framework is warranted. A future allocated display package should use
existing transcript/communication fixtures for exact known provenance, no-proof
legacy history, mixed backend from/to labels, unchanged original receipt after
reload/upgrade and no resend on Unknown. Any genuinely missing model tool uses
existing callback fixtures and retained-tool adoption proof, not a new harness.
No check is requested or run by this source-only packet. Broad interface cleanup,
latency diagnosis and final file ownership remain with their assigned owners.

Status: investigation complete; no source blocker for the recommendation. Capacity
available after lead acceptance; no queued implementation or session action.
