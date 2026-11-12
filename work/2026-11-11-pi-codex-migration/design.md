# Pi replacement feasibility: preserve the portal, replace the agent backend

Status: revised feasibility design, packages A/E/K, updated 2026-11-12. Owner:
architect0. No implementation package is released. Lead owns scope, plan/state,
acceptance and any later implementation assignment.

The current allocation/delivery plan is [implementation-plan.md](implementation-plan.md)
(package P). It adds only new opt-in Pi sessions alongside unchanged, fully
writable Codex, one backend per development session. Its single package table
supersedes the earlier candidate allocations. Migration, conversion, cross-backend
handover, cutover, retirement automation and default switching are future-only;
the comparisons below retain rationale, not current implementation scope.
Later conversion should prefer the full representable conversation, with a
summary alternative only if full conversion is too complicated.

## Recommendation

Pi is a credible way to remove the provider-switch limitation while keeping the
current portal. Its coding-agent supports changing provider/model on the same
conversation through a normal API. The portal does not need to become Pi's UI,
and the session, repository, cluster and team workflows do not need redesign.
Recommend **side-by-side Pi and Codex**, with a backend selected for each
development session. Existing sessions must remain fully usable through Codex:
send, tools, queues, members, follow-up, recovery and the existing terminal path,
not merely a readable transcript. New Pi sessions can use the same portal.
Removing Codex now conflicts with that requirement because no full-fidelity
execution-state migration has been established.

The requested process boundary is **one development-session cgroup and mount
namespace containing that session's lead, team workers and tool processes**.
No Pi host process is shared across development sessions. A session supervisor
owns loaded lead/member worker processes and their tools; a worker can embed
the SDK or run Pi RPC with a small first-party extension. Dormant histories do
not need permanent workers. This supersedes the earlier SDK multiplexing
preference; resource savings from shared agent processes are not the selected
design. Keep the Go portal and host coordination as the control plane, outside
the agent workload trees.

Worker separation does not require separate OpenAI logins. Start with one Pi
login for the selected account/grant and Pi's native shared, locked credential
store. A shared authentication service or personal inference gateway is an
optional control-plane component, not a reason to share agent execution.
Legacy Codex credentials and exact Daybreak access need the explicit contract
below; do not copy one rotating grant into independent stores.

Compare SDK workers with stock RPC workers behind a narrow conversation-backend
interface; SDK remains attractive for explicit tool/resource ownership. The
production substrate remains unsettled until durable submission/recovery is demonstrated through supported
APIs. SDK access alone does not solve that problem. If meeting the contract
requires a maintained Pi fork, that weakens the principal reason to migrate;
compare Pi Durable before accepting another patch dependency.

Pi Durable is a serious alternative because it supplies durable deduplicated
submissions and background task/report primitives. It is a separate,
explicitly experimental harness, not a durability option on the coding-agent
SDK. It would increase ownership of resource loading, policy and integration.
Its native team example is useful evidence, not a replacement for the portal's
retained roles, authority and lifecycle rules.

The benefit is native cross-provider conversation support and less coupling to
Codex's loaded-thread behavior. It is not a reduction to a configuration-only
integration: conversation recovery, reporting identity, packaging and history
still require real engineering. Do not reproduce the complete Codex App Server
wire protocol merely to hide the change.

## Scope and evidence

The user's latest priority is to preserve the current portal workings; the
motivation is inability to keep using unmodified Codex with provider switching.
Web is the primary client, multiple providers within a session are essential,
automated teams remain important, planning is desirable, and interchangeable
web/CLI access is optional. This assessment preserves existing workflows and
identifies parity gaps; it does not authorize removing them. Subsequent user
constraints add session-owned process isolation, mounted temporary storage and
accounting, optional questions that allow work to continue, per-member provider
overrides, and explicit provider/model fallback. These are desired capabilities,
not claims that the current portal or stock Pi already supplies every part.

Detailed inventories belong to the assigned evidence owners:

- [Current runtime evidence](current-runtime-evidence.md), implementer0: portal
  seams, provider transition, patches, durable delivery and lifecycle contracts.
- [Pi capability evidence](pi-capabilities-evidence.md), implementer1: providers,
  authentication, SDK/RPC, tools, planning, MCP and source-linked capabilities.
- [Process/isolation evidence](process-isolation-evidence.md), architect1:
  session process ownership, namespace and temporary-service boundaries.
- [Coexistence evidence](coexistence-evidence.md), architect2: writable legacy
  sessions, versioned backend authority and migration distinctions.
- [Extensions/questions evidence](extension-and-question-evidence.md),
  implementer4: trusted first-party integration and nonblocking questions.
- [Provider/fallback evidence](provider-fallback-evidence.md), implementer5:
  member provider overrides and explicit fallback semantics.
- [Authentication evidence](authentication-evidence.md), implementer5:
  native cross-process refresh locking and OpenAI login flows.
- [Authentication/gateway evidence](authentication-gateway-evidence.md),
  architect2: shared store, broker, personal gateway and legacy compatibility.

Audited snapshots are dev-workspace
[`6587c4c1cedabee95bcc52f4667e7d33e3a82859`][runtime], codex-web
[`dd90fb4308ba85617ee2a4267cc835aa9a4f11ce`][web], and Pi main
[`a22b888a58fe55b668cc45b80749ec88d4eb4ddc`][pi]. Local bare master refs and
earlier source snapshots differ; these findings use the exact default-branch
snapshots above, not a reconciled or deployed tree. Pi's latest observed release
is v1.5.2 at `b4afdddf44e059c67ccf5097e5317d913521b470`; findings from main are
not all certified to exist in that tag.

Session identity, environment and live same-session roster were verified before
work. Required procedures and the documentation skill were read. Only canonical
bare/default blobs, public upstream source and this session's assigned evidence
were inspected. No prior-session records, worktrees, transcripts, credentials or
live model calls were used. No prototype, build, test or deployment ran.

The user's provider-patch report is an accepted motivation, not disproved by the
default source. That source documents an archive/unarchive workaround for loaded
Codex threads; the separately identified Nix daemon/store packaging patch does
not implement provider switching. The exact reported patch and live executable
remain unverified and need not be reconstructed to answer what would change.

## What stays, adapts and may look different

“Stays” describes intended product behavior and ownership, not a claim that
every current source file can remain byte-for-byte unchanged.

| Area | Can stay as the user experiences it | Internal adaptation or visible difference |
| --- | --- | --- |
| Portal shell | Layout, navigation, session URLs, workspace selection, host authentication and file links | Keep existing host/Go application; replace runtime composition. No p2 adoption. |
| Repository and operations features | Compare/review, worktrees, Files, clusters, reservations and existing lifecycle controls | Reconnect agent status/notifications; preserve domain authority and recovery journals. |
| Chat | Composer, streamed transcript, uploads, history paging, stop, queue and model controls | Generalize conversation client/types and translate Pi events/history. Existing DOM/styles can remain; Codex item shapes and transport cannot. |
| Providers | Existing workspace default and session selector, model validation, progress and error handling | Native Pi model/provider change replaces native-thread closing/reopening. Auth/catalog discovery and token resolution change. A provider may offer different thinking levels or models. |
| Teams | Addresses, retained members, assignments, reviewers, separate transcripts and report-to-lead workflow | Preserve portal roster/orchestration. Replace thread creation, activity, dispatch, utility launches and native caller binding with backend equivalents. |
| Planning | Existing Plan/Default and implement-plan workflow can be retained | Custom mode/transition handling and accepted-plan identity are required. Do not mistake the upstream example for a complete enforcement boundary. |
| Existing sessions | Codex sessions remain editable, runnable and recoverable, including their members and tools | Retain the supported Codex backend and state. A Pi continuation is a new derived conversation, not a lossless conversion or retirement of the original. |
| Optional questions | Show choices/free text while the agent keeps working; accept a later answer in the correct conversation | Add durable question and answer identities with host-owned delivery; do not substitute a blocking Pi dialog. |
| Session resources | Existing portal remains the place to inspect and control a session | New session-owned cgroup/namespace, mounted temporary storage and per-session resource display; retain existing authorization and recovery. |
| Quotas/account UI | Existing private-pool usage preview can remain host-owned | Pi token/cost usage is not Codex subscription allowance/reset parity. Unsupported account operations need an honest unavailable state or a separately verified adapter. |
| Terminal | Existing Codex sessions can keep their established terminal path during coexistence | Pi's native TUI is not automatically an attach client for a portal-owned SDK session. Shared live web/CLI access is separate optional work. |

The present provider selection applies to the whole development session,
including retained members. The user now requests an additional hierarchy:
session default, explicit member override, and explicit provider/model fallback
chain. Retain the existing default behavior for members without an override.
All members still belong to the same development-session process boundary,
even when they use different providers. Backend choice (Codex or Pi) and model
provider choice are separate; switching a Pi member's provider is not a
cross-backend migration.

Model responses, compaction wording and tool presentation cannot be promised
identical. Pi retains text/tool history across providers, but drops another
model's reasoning when constructing its context. Thinking is adjusted to the
selected model's supported levels. Preserve original history for display;
distinguish it from what the next model actually receives.

## Backend choice and architectural boundary

codex-web already separates trusted application conversation IDs from native
clients through `conversation.Client` and `Target`, but method signatures use
`codex.*` types. Generalizing that narrow seam is plausible. The scope is the
operations needed by the portal, not an emulation server for arbitrary Codex
clients. Keep generic UI behavior and application authority outside the backend.

The smallest useful portal capability contract is the following. Keep its
implementation in the existing portal and a session worker adapter; do not
build a new general-purpose agent server.

| Capability | Minimum contract |
| --- | --- |
| Identity and lifecycle | Backend-tagged trusted session/member/conversation identity, incarnation and package generation; create/load/fork/interrupt/recover through existing authority. Old schema-1 authority rejects unknown fields, so version routing deliberately. |
| Conversation view | Paged history, typed text/tool/question projections, live updates and reconnect cursor; preserve raw backend evidence separately. A view projection is not an execution-state migration. |
| Admission and execution | Stable immutable input/queue IDs, acceptance receipt or honest unknown state, steering/follow-up semantics, cancellation and terminal/settled observations. |
| Settings and routing | Session defaults, member override, exact provider/model/thinking and fallback policy; capture effective settings on admission and actual provider on execution. |
| Host interaction | Caller-bound reporting, utility/peer delivery and persistent optional questions/answers; existing authorization, origin checks and held-recipient rules. |
| Ownership and accounting | Session supervisor/cgroup/namespace identity, owned tool/service handles, mounted temporary paths, resource observations and recovery holds. |

Backend, conversation and provider identities are distinct. Only trusted host
state selects paths, endpoints and member identities. Unsupported capabilities
must be explicit; never silently downgrade editable Codex sessions to viewers.

| Candidate | Evidence and benefit | Cost or decisive limit | Position |
| --- | --- | --- | --- |
| Coding-agent SDK in per-session worker processes | Direct sessions, tools, resource loaders, credentials and extension hooks; retains standard coding-agent features | Adds pinned worker packaging and a narrow host transport; durable admission is not supplied by `prompt()` | Candidate alongside RPC, subject to receipt/recovery gate |
| `pi --mode rpc` subprocess | Native JSONL commands/events; natural Go process boundary; custom tools can be loaded as extensions | Correlation IDs are not deduplication; custom tools/auth need extension or extra control path; UI supports dialogs but not arbitrary TUI widgets | Viable simpler comparator, not rejected merely for using RPC |
| Pi Durable service | Atomic admissions, `requestId` dedup, persisted tasks, child/report recovery, safe/unsafe replay declarations | Explicitly experimental; separate data format and resource/tool integration; single-writer ownership and upgrade policy required | Compare if supported SDK cannot meet recovery without a fork |
| pi-ai / agent-core directly | Provider and agent-loop components with maximum host control | We own substantially more harness, history, tool and recovery behavior | Higher-cost fallback, not the default |
| p2 / wholesale Chord application | Demonstrates browser/TUI and durable-agent integration | p2 explicitly says unsupported prototype, will disappear, do not build on it; replaces a portal the user likes | Reject for this task |

RPC is not excluded by web dialogs: `select`, `confirm`, `input` and `editor`
are supported. The SDK advantage is explicit ownership of tools, resources,
policy and callbacks, not an unsupported claim that RPC cannot host custom
tools. Runtime services should have one authoritative writer per conversation
and reconnecting clients; browsers do not spawn independent file writers.

### One session process tree, namespace and temporary storage

The intended topology is portal → session supervisor → lead/member workers →
tools and registered temporary services. The supervisor enters one owned cgroup
and mount namespace before spawning any worker. Every member/provider uses that
same session boundary. Workers may be unloaded only after queues, uncertain
submissions, active tools, utilities and terminal subscriptions permit it under
existing recovery rules; unloading is not archiving or deleting a session.

[Process/isolation evidence](process-isolation-evidence.md) establishes two
concrete integration obligations. The current session-service helper launches
sibling `app.slice` units, so its spawn path must enter the session supervisor
while preserving registration and shutdown/recovery contracts. `JoinsNamespaceOf`
shares temporary directories, not the exact mount namespace; mounts created by
`ExecStartPre` do not establish the later worker namespace. Use one owning
`ExecStart` process and inherited descendants rather than claim that sibling
units automatically provide the requested boundary.

Give each session explicit backing directories mounted at its temporary paths,
with persistent ownership metadata outside those temporary mounts: session
incarnation, supervisor generation, cgroup, namespace identity, backing paths
and live command/service leases. Keep recovery records and receipts on durable
storage, not ephemeral tmpfs. Recreating the worker must preserve temporary
paths that accepted work still depends on. Namespace exit removes its view;
it does not authorize deleting backing data. Retain the ordinary explicit
lifecycle/cleanup authorization and interrupted-operation recovery rules.
Prefer disk-backed scratch for the first comparison; stock `PrivateTmp` and
`RuntimeDirectory` stop-time cleanup must not erase retained recovery inputs.
Directory allocated-block telemetry is observed usage, not a hard allocation
budget: deleted-but-open files can be missed, and `df` on a bind mount still
reports the shared filesystem. Quotas, dedicated filesystems or bounded tmpfs
need separate capacity/permission choices; no hard storage limit is assumed.

Rootless systemd mount isolation is not yet proved with the required tool
permissions. `PrivateUsers` can change host-root/setuid/sudo behavior; a narrow
host-managed launcher that establishes mounts then runs as the original UID is
an alternative to validate, not an approved deployment. Do not grant mount
administration privileges to agents. This is a bounded host-permission decision,
not a project to defend against the already trusted local operator.

Account the session's CPU, memory/peak, process count and I/O from its cgroup,
and temporary-storage usage from its owned backing paths. Label cache versus
anonymous memory and excluded/shared services. Nix daemon builders and existing
shared tmux are not inherited worker descendants; do not charge their whole
resource use to one session or assert complete attribution. The existing shared
Codex daemon remains an explicit transitional limitation for legacy sessions.
Retroactively rehosting it is outside this package; side-by-side support does
not pretend that legacy execution already has the new Pi isolation boundary.

## Hard contracts and release gates

### Providers, credentials and model catalogs

[`AgentSession.setModel()`][setmodel] validates auth, changes the existing
agent's model, appends a model-change entry and adjusts thinking. This directly
addresses the provider-switch motivation. Custom compatible endpoints are
supported; the existing private Responses gateway still needs an exact check.
Initially perform managed changes at a settled boundary, preserving retained
member identities, queue order and instructions. Mapping interrupted switches
to the current journal/continuation semantics is part of acceptance, not a reason
to discard those guarantees.

Source exposes OpenAI API keys and ChatGPT OAuth, separate `openai-codex` OAuth,
Anthropic API/subscription auth, Copilot and other provider adapters. These are
available mechanisms, not proof of the user's account entitlements or exact
model access. Credentials remain server-side. Preserve trusted private endpoint
and token-file configuration; do not accept executable paths or secrets from
ordinary model-selection input. Unknown quota data remains unknown.

Pin a coherent Pi/Node/dependency set and explicitly control model catalog
updates: Pi can overlay pi.dev catalog data at runtime, so a source pin alone
does not freeze the model choices. Preserve portal catalog validation and
record supported provider/model/thinking combinations. Credential refresh,
custom endpoint compatibility and unsupported-model errors are release gates.

The new override/fallback policy is session default → optional member override
→ an explicit ordered provider/account/model chain. An override affects only
that member, never a global endpoint or another member's settings. Preserve
the requested and effective thinking level and the actual physical provider on
each attempt. For the user's example, “Snajpa codex-lb → subscription Daybreak”
is a requested binding/route; Daybreak's canonical model ID and subscription
availability have not been verified. Do not offer it through an API-key pool
merely because a similarly named model appears in a catalog.

Pi has a supported virtual-model `route()` hook that receives the previous
physical model, failed response and persisted branch state. This can select a
different provider on a retry. However, the coding-agent only initiates that
retry when its own error classifier and budget admit it. A custom router alone
does not make every cybersec/content error retryable. Model text refusals are
ordinary text, not a structured provider failure. The
[fallback evidence](provider-fallback-evidence.md) pins the exact routing,
retry-gate and response-normalization sources.

Implement an explicit, finite host policy for verified error categories; use
native routing where its admission semantics fit and a supported host
continuation only where separately proved. Preserve unclassified outcomes and
do not infer a security-error category from arbitrary assistant prose. Record
policy revision, chain position, original input/switch identity, observed error,
old/new provider/account/model and prepared/applied/verified/unknown status.
Keep the active provider and reason visible. Bound the combined provider
retries, agent retries and fallback hops so separate retry loops do not multiply
uncontrolled work. Never replay a tool or accepted prompt just because the
fallback provider lacks part of the preceding response.

### Authentication ownership across workers and legacy Codex

**Use native Pi shared storage first; do not build a broker solely for worker
count.** The pinned source supports independent processes sharing one canonical
writable `AuthStorage` file and provider credential key. It acquires a
cross-process lock before rereading stored JSON, rechecks expiry under that
lock, holds the lock through OAuth refresh, and writes the rotated credentials
before release. One authoritative entry/refresh coordinator can therefore serve
all workers using that account/grant. Separate session processes do not imply
interactive login per worker. This is supported source behavior, not a live concurrency
test of this deployment; [authentication evidence](authentication-evidence.md)
records the exact implementation and limits.
The lock is not an atomic transaction with OpenAI: a lost refresh response,
failed credential write or abrupt worker death after token rotation can still
require reauthentication. Do not promise automatic repair on HTTP 401; the
inspected normal refresh path is expiry-based. Custom/in-memory/read-only stores
do not inherit the canonical writable file backend's coordination behavior.

Per-session mount namespaces must expose the **same underlying credential
directory, authoritative data and lock sidecars**, with rotation/replacement
visible to every participant. Do not copy `auth.json` into session scratch or
bind only a file into separate directories whose adjacent lock files differ.
This narrow shared control-plane data is compatible with separate agent process
trees. It must survive worker restarts and session scratch cleanup.

Pi auth entries are keyed by provider ID, not member or UI account alias. Use one
account-bound credential reference for workers sharing the same grant; do not
clone it into independently refreshed aliases. Distinct accounts need explicit
store/key mapping. Pi's ordinary Codex OAuth client and its ChatGPT direct-token
flow are different client/scope/transport contracts, not interchangeable labels.

The existing native Codex backend has different storage and locking. Pi's lock
does not coordinate a native Codex writer. Preserve legacy authentication under
its existing owner; use separately supported independently issued grants, or an
explicit common refresh authority/compatible inference path. Do not import or
copy its current rotating grant into Pi and claim co-safe refresh. One initial
Pi login for its worker group is different from sharing legacy Codex's exact
grant. Verify that a separate grant's issuance and renewal leave legacy Codex
usable; this has not been tested. The side-by-side recommendation does not
silently change native auth.

| Choice | What it buys | Obligation / recommendation |
| --- | --- | --- |
| Canonical native Pi store | One login and coordinated refresh among participating Pi workers, with no new service | Simplest default for trusted same-user workers; verify shared directory/lock visibility and exact account/client access. Workers can access credentials under the existing trust model. |
| Credential broker | One refresh owner keeps the refresh token central and supplies access credentials | Workers still own provider protocol, scopes and Daybreak behavior. Adds service/lease/error handling; use only for a concrete credential-access or cross-client requirement. |
| Personal inference gateway / codex-lb | One upstream auth owner and inference route; workers need no upstream refresh token | Gateway owns model mapping, streaming/Responses/WebSocket/account/feature compatibility and availability. Potentially useful, but not automatically necessary or Daybreak-capable. |

Source evidence already identifies a packaged personal `codex-lb`, separate from
Snajpa's pool. Its nginx entry point blocks inference paths; that does not prove
local internal API access is blocked. This is pinned configuration/source
evidence, not installed-image equivalence, a ready endpoint or permission to
expose it.
Reusing it may be smaller than a new broker if it supports the exact target,
but generic OpenAI compatibility or a listed model name does not establish
Daybreak access. The gateway must preserve the required model/account mapping,
client scopes, transport and feature/access-program metadata. Details and exact
source revisions belong to [gateway evidence](authentication-gateway-evidence.md).
Pi's `openai-codex` transport extracts account identity from an upstream JWT;
changing its base URL and supplying an ordinary gateway API key is not
automatically compatible. Select and verify the gateway-facing adapter rather
than treat the proxy as a transparent subscription login replacement.

The user's hardware-key requirement is an acceptance input. Perform the chosen
OpenAI sign-in in a real browser once for the shared Pi account/grant, **if that
flow supports the account/model**; any hardware-key challenge remains a user
interaction. Device-code or browser-callback support does not bypass MFA or
prove Daybreak support. Refresh can avoid repeated worker logins while valid,
but revocation, expiration or a recurring account challenge can require another
interactive login. Neither Pi source nor a gateway promises permanent unattended
access. No login or hardware-key prompt was attempted in this investigation.

Any shared auth service/gateway sits outside session agent cgroups as control
plane. Report its resource cost separately; per-session agent counters do not
include it. The smallest future acceptance check is shared-lock/rotation across
two disposable workers and their namespace views, then the exact browser/client/
account/model flow; keep legacy Codex under its original authority. Test gateway
inference only if that option is chosen. No credentials/token contents were
read or copied, and no live auth/model call ran. This clarification does not
justify a new authentication-platform package or a precise new effort quote.

### Durable delivery, teams and utility recovery

The current guarantee is durable prompt acceptance/reconciliation with honest
unknown outcomes. It does not mean arbitrary external tool effects happen
exactly once. Keep the same distinction in the replacement.

At the inspected Pi head, [RPC prompt handling][rpcsource] uses the command ID
only in the response; it is not passed into SDK prompt input. SDK prompt options
lack a native client/request identity, and steering/follow-up constructs
in-memory user messages. [SessionManager][sessionmanager] assigns entry IDs and
appends finalized records. Therefore adding a Go outbox and retrying a lost RPC
response is not sufficient. The crash between actual acceptance and recording
the host receipt cannot be called “not sent” based on missing history.

A future prototype must prove supported durable identity/acceptance hooks or
choose the durable harness. Until then, uncertain SDK sends stay held for
reconciliation/manual recovery; automatic re-send with a new ID is invalid.
This is a production automation blocker, not a reason to implement private API
monkey patches during the assessment.

Pi Durable materially reduces this work: `submit(requestId)` deduplicates
admissions, documents/tasks commit together, and the [background-subagent
example][background] persists delivery/report phases. It does not supply our
roster, approvals, permission holds or lifecycle policy. In particular, the
example automatically forwards final answers, while current team members
explicitly call `report_to_lead`; preserve the latter contract. Default unsafe
tools interrupted by a crash report interruption instead of replaying effects.
Safe replay still needs operation-specific idempotency. Its default SQLite
WAL/NORMAL commits can lose the newest data on host/power failure, and the
library requires one writer per storage. Verify the selected durability mode
and process ownership before claiming parity with current full-sync receipts.

Retain stable message IDs and immutable payload/settings binding, per-recipient
queue order, cancellation, held/stopped recipients, and separate utility watcher
identity. Pi `agent_end` can precede retry/compaction/follow-up work;
`agent_settled` is the closer idle boundary, but neither alone proves an external
command completed or that its result was durably delivered. Utility launch and
report receipts remain host-owned evidence.

Current reporting trusts native `_meta.threadId`. The inspected Pi MCP path
does not provide that identity; it supplies tool arguments and progress metadata.
Bind host reporting tools to the worker's trusted conversation/member context
and recheck the current roster/session incarnation under the existing admission
locks. A model-provided `from`, slug or recipient is not an identity substitute.
Existing reporting and peer-message business logic can remain behind this
adapter. MCP is natively supported by Pi CLI; SDK loads the necessary MCP,
codemode and tool-search extensions explicitly.

### Optional questions, trusted extensions and planning

Optional questions are a distinct host capability, not Plan mode or blocking
approval. A first-party tool must commit a question with stable request ID,
immutable revision and session/member/conversation/incarnation binding, publish
the current choice/free-text card, and immediately return its pending ID. The
agent continues independent work. Preselection or elapsed time is not an answer
and does not authorize work dependent on that answer.

The browser authenticates a reply against that question/revision and commits
an immutable response ID plus pending delivery before acknowledging it. Retries
return the same receipt; corrections are ordered new responses, not silent
rewrites of an answer already used. Reconnect reconstructs the question from
host state even if the worker unloaded. A later answer goes to the original
logical recipient through ordinary durable dispatch: steer at a safe boundary,
follow-up, or eligible idle activation. Holds and stopped state remain in force.
Finished turns can still receive answers to open questions; a changed branch,
retired member or session incarnation needs explicit stale/rerouting handling.
Treat the answer as data, not a slash command or executable prompt template.

Pi's `ctx.ui` dialogs await in-memory Promise resolvers; official question
examples are TUI widgets. They do not provide this ask-and-continue contract.
SDK message injection and RPC steer/follow-up supply execution primitives, but
question/outbox receipts do not close the unresolved Pi admission crash window.
The same durable-delivery release gate applies. Detailed source and contract:
[extensions/questions evidence](extension-and-question-evidence.md).

Use supported SDK `customTools`/extensions or one small reviewed extension in
stock RPC workers for reporting, questions and mode controls. No external
extension is selected or needed here. Pin actual source/artifact and transitive
dependencies; inspect loaded code, install hooks, overrides and credential/
process access; verify maintenance and exact supported Pi version; package the
reviewed artifact reproducibly. Use ordinary checks/final review for updates,
not a new approval process. Managed workers should not float-install executable
extensions or silently skip required host tools; preserve intended instruction
and skill discovery. Official examples establish provenance, not portal trust
or recovery parity.

The upstream Plan example disables built-in edit/write and regex-filters bash
while retaining other active tools. That is not enforceable read-only planning:
custom/MCP/nested tools and shell programs can still mutate state.

Preserve the current Plan workflow and its promised restrictions as trusted
host state. Stronger strict read-only enforcement beyond that existing contract
is a product decision, not automatic migration scope. If required, such a
read-only planning profile must restrict
every enabled tool family and delegated task, including codemode/MCP, and avoid
arbitrary shell execution rather than try to prove shell programs safe with
regex. Bind “implement plan” to the accepted plan's immutable identity/digest
and receipt, as today. Test restart, stale plan, duplicate click and queued work.
Pi has no built-in OS permission boundary. The current installed policy grants
full execution access, but any required restricted profile must have a real
host/process enforcement design. This does not change the trusted-local-operator
model or require protecting against the host administrator.

### Persistence, coexistence and recovery

Use a backend-tagged binding for new sessions and retain original Codex session,
queue, receipt and rollout evidence. Never reinterpret a Codex thread ID as a
Pi session ID. An unresolved old operation must be reconciled by its original
supported backend; creating a Pi session cannot settle it.

For future migration/retirement decisions, the choices are materially different.
Only side-by-side new Pi sessions are in the initial implementation plan; no
continuation converter or transfer/cutover machinery is to be built now:

| Route | Existing-session usability | Cost and recommendation |
| --- | --- | --- |
| Side-by-side, new Pi sessions | Existing sessions keep full Codex execution and recovery | Recommended first step. Two pinned backend adapters/test matrices remain, with additional Pi process/storage cost during coexistence. |
| Derive a new Pi development session | Original Codex session stays fully usable; Pi receives an attributed context summary or transformed completed messages | Smallest independent continuation. New ownership/resources must be assigned explicitly; copying context does not transfer worktrees, claims or completion obligations. |
| Derive a Pi conversation within the same development session | Preserve initiative/Git/resource identity and the activatable original Codex conversation | Needs deliberate handover with one active execution authority per member, source/target mapping and effect reconciliation before switching either way. This is not lossless migration. |
| Full-fidelity session migration | Would need equivalent history, members, queues, goals, pending tools, receipts and recovery, including retained archives | Not established. Pi's JSONL import reads Pi sessions; it is not a Codex execution-state converter. No reliable effort quote without a supported fidelity contract and fixtures. |
| Remove Codex | Old sessions remain usable only if every required execution/recovery dependency has a proved replacement | Reject as the first step. A read-only history viewer, new default or successful new Pi session does not meet the requirement. |

Retirement additionally needs supported archive/restore paths that cannot
reintroduce an unsupported Codex dependency. Preserve the old executable,
protocol adapter and state readers while writable sessions or uncertain native
operations need them. No stop/removal/cleanup is authorized by this design.
The tradeoff is ongoing dual-backend maintenance in exchange for avoiding a
high-risk mandatory migration. Keep the legacy adapter stable and generalize
only the shared portal contract. Source-backed route and state details are in
[coexistence evidence](coexistence-evidence.md).

Coding-agent v3 JSONL migration and Pi Durable storage are different formats;
opening legacy files can rewrite them. Keep original data and test selected
readers/writers before touching retained history. Preserve source attribution
and explicit omissions in any derived continuation; hidden reasoning and native
execution state do not transfer merely because text/tool output can be imported.

Current workspace software recovery is **forward-only**. Do not promise that
an older package can be selected after new state is written. A corrected newer
package may disable new Pi creation while retaining readers and recovery for
both backends. Routing future sessions back to a supported Codex backend is a
product fallback, not permission to downgrade storage or overwrite receipts.
Extend the installed runtime/package capability fences so incompatible packages
refuse state they cannot preserve. Existing lifecycle journals, exact final-head
rules, resource ownership and recovery commands remain authoritative.

No application database/API/client changes to vpsAdmin, its Terraform provider,
or vpsAdminOS node protocols are proposed. Mixed-version concerns here are the
portal, runtime helpers, agent service, browser clients and persisted session
state. A later rollout must retain old browser/API recovery behavior or require
an explicit refresh without duplicating an accepted operation.

## Historical estimate and current allocation

[implementation-plan.md](implementation-plan.md) now owns the complete future
packages, file owners, dependencies, release gates and checks. The earlier
candidate table is superseded. Nothing is implemented or assigned by either
document; lead accepts sufficient package release after its relevant contracts
settle. The current plan distinguishes a usable manual pilot from the stronger
automation gate, with independent seam/UI work proceeding when safe.

Package A's narrower web/team/lifecycle parity estimate was **30–60 engineer-days,
roughly 6–12 working weeks for one experienced engineer**. The newly requested
session supervisor/namespace/tmp accounting, optional questions and per-member
fallback add real scope; that estimate is a baseline, not an all-in quote for E.
Those historical estimates are not additive. Resolve supported admission and namespace/permission mechanisms
before giving a revised total: a narrow integration differs materially from a
new privileged launcher or maintained harness fork. The first 3–5 day prototype
is a decision timebox, not a promise that every expanded acceptance case fits.
Do not presume two implementers halve elapsed time across these dependencies.

Those bands assume the existing endpoint/accounts work, a supported admission
solution exists, old sessions coexist rather than convert, and ordinary portal
workflows are preserved. Unverified authentication/entitlement and missing model
feature parity are exclusions, not zero-cost tasks; external provider refusals
may block feasibility rather than add predictable engineering days. An SDK fork,
new generalized harness, broad history conversion or reproducing unsupported
subscription reset APIs invalidates the estimate. Optional same-live-session
CLI attachment is a separate approximately 5–10 day exploration/implementation
after the owner protocol is stable; it is not on the web migration's critical
path. Historical import effort remains unestimated without a defined fidelity
contract and representative retained fixtures.

## Resource use: stored history is different from running agents

The user added a resource comparison after the capability investigation.
Implementer0 owns the bounded aggregate observations in
[resource-evidence.md](resource-evidence.md). The figures below are reconciled
with that completed package-D artifact; native process memory was sampled at
22:14:56 UTC on 2026-11-11, with other observations near 22:14–22:18 UTC.
No Pi benchmark has run, so numerical claims about Pi RAM, CPU, startup latency,
throughput or savings would be unsupported.

| Observed current population or resource | Meaning and limit |
| --- | --- |
| 83 current tracking directories + 343 archived = 426 dated sessions | Directory classification, not active-agent count. Four non-date directories are excluded. |
| Public session listing: 432 known rows, 60 with managed tmux | A broader known-slug union than the directory count. A terminal attachment/session does not establish active model work. |
| Dedicated Codex home: 4,190 stored threads, 2,213 unarchived / 1,977 archived | Of these, 3,667 match this workspace's session-cwd prefix, across 205 distinct cwds. Stored/unarchived is not loaded or active. |
| Shared native daemon: 6.50 GiB PSS; 91 reporting helpers: 0.78 GiB aggregate PSS | Process-memory observations. Helpers are separate processes, not proof of 91 active agents or retained roster members. |
| Code-mode host: 0.054 GiB PSS; portal Go: 0.108 GiB; child naming Codex: 0.218 GiB | Separate observed components; not a complete host or all-agent memory total. |
| Native cgroup: 34.20 GiB, including approximately 24.05 GiB file cache | Cgroup charge is not daemon heap or private resident memory. |
| Rollout files: approximately 17.26 GiB; native thread-history SQLite: 5.86 GiB | Persistent disk footprint, not RAM. Coexistence must retain supported original recovery/history data. |

The attributed native-service processes total approximately **7.34 GiB PSS**.
Thirteen other Codex processes are excluded because workload ownership was not
established; this is not a host-wide total. Measurements are live observations
at nearby times, not one atomic or idle-baseline snapshot. The evidence artifact
retains raw units, observed store paths and collection methods; installed source
equivalence was not proved by those executable paths alone.

Loaded conversation count, active model-call count and retained-member count
remain unknown; no peer roster/transcript contents were read. These limits
prevent a defensible per-agent memory estimate or a numeric Pi savings claim.
The practical conclusion is still strong: thousands of stored threads must not
force thousands of permanent Pi processes or loaded histories. Use loaded
lead/member workers inside each session's supervisor boundary and evaluate safe
idle unloading. The earlier shared-SDK saving hypothesis is superseded by the
chosen worker topology. More process baselines may cost memory; retained
histories, extensions, MCP helpers and isolation still need measurement.

| Population or cost | Expected architectural comparison |
| --- | --- |
| Open or archived session records | Mainly persisted history/metadata. An archived session does not require a Node process or loaded AgentSession. Open-but-idle records can also be unloaded. Counts alone do not establish RAM demand. |
| Loaded conversations and retained members | Both candidate implementations use SDK or RPC worker processes for loaded members within one session boundary. Node/package overhead can repeat; dormant retained members need no permanent worker. Do not assume SDK workers are smaller without measurement. |
| Active model/tool work | Provider latency, concurrency, tool processes and builds can dominate. Replacing the harness does not eliminate this work; multi-provider concurrency can increase total usage. |
| Long histories | Coding-agent SessionManager holds entries and indexes in memory when loaded; keeping many long histories loaded can be expensive. Pi Durable explicitly recommends SQLite over its all-history-in-memory JSONL backend for long-running agents. Measure history paging/reconstruction as well as idle process RSS. |
| Process isolation | Worker processes separate event loops and some failures; the cgroup/namespace and supervisor are shared only within the development session. A session-wide memory limit or supervisor failure can affect every member. This is ownership/accounting, not a hostile-member security guarantee. |
| Migration coexistence | Keeping Codex available for old histories plus the Pi service can initially increase baseline memory and retained disk. Retiring native history/recovery dependencies is a separate later decision, not an assumed immediate saving. |

The source basis is the [SDK session ownership contract][sdk],
[SessionManager's in-memory entry indexes][sessionmanager], and [Pi Durable's
storage documentation][durablestorage]. These establish plausible cost drivers,
not a measured ranking against Codex. Independent runtime/provider refresh
timers, catalog/auth caches and browser subscriptions may keep otherwise idle
processes alive; the prototype should count them rather than infer “idle” from
an empty composer.

A later comparison should hold provider/model, tool workload, transcript size
and active concurrency constant. Record cold service baseline, one short/long
loaded history, the representative retained team, reconnect, and idle unload;
measure aggregate PSS/RSS, CPU, startup/reconnect latency and storage growth.
Use the current aggregate session/thread counts to select a representative
population, not to launch every archived thread. Separate model/tool subprocess
cost from harness cost and avoid double-counting shared pages. This can be part
of the decision prototype; it is not permission to run one now.

## Acceptance and verification plan

No verification below ran in this investigation. First prototype acceptance is
bounded to the risky interfaces, not a complete feature demo:

1. Use the exact intended custom gateway and one other required provider/account
   to switch A → B → A in one conversation. Preserve identity, text/tool history,
   model/thinking intent and retained member behavior. Show unsupported-account
   and unsupported-model failure without losing the old usable session.
2. Kill/restart around admission, lost acknowledgement, steering/queue dispatch,
   report delivery and cancellation. Retry the same ID/payload; prove one
   accepted input or a preserved explicit unknown, never an invented “not sent”.
   Establish the supported API path and cost before choosing SDK or Durable.
3. Bind reporting and utility calls to real worker identities. Reject a forged
   sender, stale roster binding and wrong session; preserve the exact original
   receipt on retry. Demonstrate idle lead wakeup and held-recipient behavior.
4. Preserve one fully writable Codex-backed fixture beside a Pi fixture across
   restart and a forward package update: follow-up, tools, queues, members and
   recovery must still work, not only history reads. A new backend cannot
   retire old proof or resend uncertain native work.
5. Verify the supervisor, every loaded worker/tool and registered temporary
   service share the owning session's cgroup and exact mount namespace. Check
   permissions, tmp path identity across restart, outstanding leases and
   resource labels/exclusions. Keep Nix daemon accounting explicit.
6. Publish a question, continue work, reconnect and answer later. Prove correct
   member identity, held-recipient behavior, duplicate/corrected/late replies,
   restart and uncertain answer delivery without duplicate cards or prompts.
7. Exercise member-local provider overrides and a finite configured fallback
   chain using the intended accounts/models. Distinguish a supported structured
   failure, text refusal and unknown error; preserve tools/history/receipts and
   show the actual provider. Validate subscription entitlement separately.

If those pass, quick implementation checks should cover adapter types/schema,
provider and catalog validation, queue/receipt state transitions, plan policy
and browser request serialization. Use repository Nix shells and targeted
Go/TypeScript/browser tests against the actual interfaces. Keep failing cases
small before running expensive suites.

After complete commits and independent final review, longer checks should use
disposable installed environments: browser creation/follow-up, uploads,
stream/reconnect/history, multi-member assignment/reporting, utility waits,
provider changes during controlled activity, Plan implementation, and lifecycle
creation/archive/revive recovery with both backends. Add storage/process-failure
fixtures relevant to the selected durability mode and long-history paging.
Fresh verification utilities own long checks under the monitor skill. Live
credentials/deployment require their separately scoped authorization and machine
ownership; this assessment requested neither.

Deployment order, if later authorized: pin/build the coherent backend and portal
package; pass review and installed checks; prepare compatible forward recovery;
deploy the user-profile application under current coordination procedures; verify
old conversations and opt-in Pi sessions before changing the default. Preserve
host system configuration unless a concrete dependency requires it. Deployment
does not authorize repository integration or session lifecycle actions.

## Settled boundaries and remaining decisions

Settled: keep the portal and choose side-by-side backends with fully workable
legacy Codex sessions; use one Pi development-session supervisor/cgroup/mount
namespace and loaded lead/member worker processes; retain host-owned teams and
lifecycle with a narrow adapter. No shared agent host across development
sessions, p2 adoption, full Codex protocol emulation, automatic history migration
or legacy daemon rehosting. Preserve async optional questions and implement
the requested member override/explicit fallback as host policy using supported
native primitives where they fit. Existing skills/MCP functions need source,
maintenance, policy and caller-binding checks, not an extension-shopping phase.

Open production decisions: supported SDK acceptance/receipt mechanism versus
Pi Durable; namespace setup preserving required tool permissions; exact provider/
account/model/gateway/error matrix; fallback outside Pi's native retry gate;
safe switch timing with queued/in-flight work; quota/reset priorities; strict
Plan enforcement if wanted beyond current behavior; and later migration or
CLI-attachment fidelity. These block dependent production packages, not this
assessment. No implementation package has been released. Full Codex retirement
is a separate future dependency-removal decision, with no demonstrated date.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-11-pi-codex-migration/>

[runtime]: https://github.com/aither64/dev-workspace/tree/6587c4c1cedabee95bcc52f4667e7d33e3a82859
[web]: https://github.com/aither64/codex-web/tree/dd90fb4308ba85617ee2a4267cc835aa9a4f11ce
[pi]: https://github.com/earendil-works/pi/tree/a22b888a58fe55b668cc45b80749ec88d4eb4ddc
[setmodel]: https://github.com/earendil-works/pi/blob/a22b888a58fe55b668cc45b80749ec88d4eb4ddc/packages/coding-agent/src/core/agent-session.ts#L2657
[rpcsource]: https://github.com/earendil-works/pi/blob/a22b888a58fe55b668cc45b80749ec88d4eb4ddc/packages/coding-agent/src/modes/rpc/rpc-mode.ts#L409
[sessionmanager]: https://github.com/earendil-works/pi/blob/a22b888a58fe55b668cc45b80749ec88d4eb4ddc/packages/coding-agent/src/core/session-manager.ts#L1180
[background]: https://github.com/earendil-works/pi/blob/a22b888a58fe55b668cc45b80749ec88d4eb4ddc/packages/durable/test/examples/22-subagent-background.ts
[sdk]: https://github.com/earendil-works/pi/blob/a22b888a58fe55b668cc45b80749ec88d4eb4ddc/packages/coding-agent/docs/sdk.md
[durablestorage]: https://github.com/earendil-works/pi/blob/a22b888a58fe55b668cc45b80749ec88d4eb4ddc/packages/durable/README.md#storage
