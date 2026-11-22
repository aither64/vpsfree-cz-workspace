# P5: Pi teams, reports and verification utilities

P5-D implementation brief, 2026-11-12. Architect1 owns this brief; architect0
accepts sufficiency in `design.md`; lead releases implementer3. This is a
source plan, not installed-runtime acceptance. P4-D is complete and accepted.

## Release and boundary

Release the independent typed policy, delivery, report and refusal-fixture slice
below. Actual Pi dispatch requires the named operation gates. Ordinary witnessed
idle Send is the only P3 delivery operation currently supported; busy steering
and follow-up are unavailable. Preserve the existing Codex executor and formats.
Retained roster settings, explicit reports, reviewer independence and fresh
watcher semantics remain required initial-integration scope, even where their
runtime connection is still gated. No new scheduler, registry, receipt ledger,
cross-session grant, generic agent server or H0 modification is part of P5.

Consume [main plan](implementation-plan.md), [P2 contracts](implementation-contracts.md),
[runtime M](pi-runtime-plan.md), [boundaries N](backend-evolution-boundaries.md),
[integration O](backend-integration-map.md), [P4](pi-provider-plan.md) and
[current design](design.md). One development session uses one backend and one
supervisor/cgroup/exact mount namespace. Loaded members and utilities are its
children; dormant retained histories need no process. Shared canonical auth
directory/locks stay outside private scratch; member history/settings remain
private. P5 handles references and policy, never credentials.

## Files and ownership

All application paths below are relative to D, `dev-workspace`. Names describe
new additive files, avoiding concurrent edits to existing native implementations.

| Owner | Files / deliverable |
| --- | --- |
| Implementer3, independent P5 | `portal/internal/teamruntime/pi_types.go`, `pi_policy.go`, `pi_delivery.go`, `pi_reporting.go`, corresponding `pi_*_test.go`: typed projections, policy checks, one-send adapter and explicit report handling. Existing roster remains authoritative. |
| Implementer3, independent P5 | `portal/internal/agentteams/pi_policy.go` and tests: project validated retained/catalog policy to Pi inputs without rewriting saved model/effort/access/instructions. |
| Implementer3, independent P5 | `portal/internal/monitoroperation/pi_types.go`, `pi_policy.go`, tests: utility/receipt/result projections and unavailable launch gate; `communication/pi_delivery.go` and tests: delivery-policy adapter; `progressobserver/pi_policy.go` and tests: activity eligibility/refusals. No new persistence or scheduling loop. |
| Implementer3, independent P5 | `portal/internal/pihosttools/team.go`, tests, and `pi-runtime/src/host-tools/reporting.mjs` with focused fake tests: strict tool arguments and injected callback handler. These modules are inert until registered by their owners. |
| Implementer2 / P2 integration | Existing session authority/creation writers, central `cmd/workspace-portal`/web/CLI composition and service registry, including team/monitor/communication selection. P5 supplies constructors, not edits to central routing. |
| Implementer1 / P3 integration | `portal/internal/piruntime/`, supervisor/worker entrypoint and private transport: verified caller capture, callback transport, execution adapter, member initialization evidence and distinct utility mode. No parallel P5 worker-entrypoint edits. |
| Later owner-coordinated P5 window | Existing team/monitor/communication record codecs and stores, only if needed for versioned backend variants. No Pi record writes through Codex-shaped schema 1. Exact format changes need architect0/owning-package acceptance first. |
| Existing owners | P4 validates provider/model/account/thinking; P7 packages and registers the inert modules. H0 unchanged. Technical docs go in D's existing session/report/communication guides during the implementation owner's assigned documentation window. |

Keep import direction: `teamruntime` already imports `agentteams` and
`monitoroperation`. Their additive files must not import `teamruntime` or its
Pi caller/delivery types; use lower `agentbackend`/runtime values or their own
policy/utility projections. `communication` may consume `teamruntime` as it
already does. `pihosttools` composes handlers above these packages. No new shared
registry/package is needed to solve an import cycle.

No application edits or checks are performed by P5-D. No commit, deployment,
profile activation, lifecycle operation or model call is authorized by this plan.

## Frozen independent consumer contracts

Use existing `agentbackend.SessionRef`, `ConversationRef`, `ExecutionHandle`,
`piruntime.RuntimeRef`, `EffectiveSettings`, `SubmissionRef`, `SubmissionStatus`
and `conversation/backend.SendRequest`, `SendResult`. Do not replace them with
Codex IDs/options or derive logical identity from a process/PID. Generation
fences execution; it never changes the stable receipt/idempotency namespace.

P5 owns these in-process consumer values and ports (not a new wire format):

```go
type PiCaller struct {
    Runtime piruntime.RuntimeRef
    Handle  agentbackend.ExecutionHandle
}
type PiMessage struct {
    ID, To, Text string // caller/from comes only from PiCaller
}
type PiPreparedDelivery struct {
    Target   agentbackend.ExecutionHandle
    Settings piruntime.EffectiveSettings // already applied, exact resolved revision
    Request  backend.SendRequest        // frozen envelope, ID and ActionContext
}
type PiAdmission interface {
    WithDelivery(context.Context, PiCaller, PiMessage,
        func(PiPreparedDelivery) error) error
}
type PiNative interface {
    Deliver(context.Context, agentbackend.ExecutionHandle,
        backend.SendRequest) (backend.SendResult, error)
    Lookup(context.Context, piruntime.SubmissionRef) (piruntime.SubmissionStatus, error)
}
```

`PiAdmission` is a P5 consumer port implemented by the central composition
owner, not a permission cache. Its callback runs while the existing admission
and team operation ownership is held. It verifies package/session/backend,
exact caller and target incarnations, live generation, roster membership and
retirement, execution hold, resolved P4 settings and current native availability.
It must not acquire locks in reverse order. The caller holds no team lock before
entering it. Absent/unreleased authority implementation returns unavailable and
does not invoke the callback. This permits faithful refusal fixtures now.

`PiNative.Deliver` is the small P3-owned shim over `Controller.Bind` and the
returned `Operations.Send` with P3's trusted identity projection. P5 cannot
invent a browser identity or call SDK methods. Missing Send/authority/witness
means unavailable. The adapter makes at most one Send call; P3 owns its durable
receipt. `Lookup` receives the original saved reference, never a digest guessed
from visible text. No private ledger inspection, second deduplication store,
hidden replacement IDs or implicit `Configure` calls are allowed.

Return a P5 delivery result with separate `Disposition` (`held`, `unavailable`,
`attempted`) and optional `backend.SendResult`. A policy refusal before Send has
no native receipt. Once Send is called, retain its exact outcome and error;
missing/contradictory evidence is Unknown. A host pending-record acknowledgment
must be described as stored/pending, never native Accepted.

Reports use `PiMessage{ID, To:"lead", Text}` and the same admission/delivery
path. Stable lowercase UUID/32-hex message IDs keep existing team conventions;
same ID with changed full envelope/options is a conflict. Preserve the existing
assignment envelope and report instruction. `ActionContext` uses existing
`team:<slug>:<from>:<to>` semantics; exact conversation/incarnation is additionally
bound by P3. A final assistant answer alone sends no report.

## Caller, tools and permissions

The host constructs `PiCaller` from the authenticated worker channel and its
registered RuntimeRef/ExecutionHandle. It is never decoded from tool JSON,
environment supplied by a model command, a claimed PID, native thread metadata
from another backend, or sender arguments. Revalidate immediately before an
effect, including a callback delayed across replacement or removal. The local
operator remains trusted; remote requests and model-selected tool arguments do
not become authority. Possessing a valid handle or a supported backend method
does not permit spawning/loading/sending.

Freeze `BindTeamTools(caller PiCaller, handlers TeamHandlers)` as an inert
host-side factory. `TeamHandlers.Report(ctx, caller, messageID, text)` and
`Peer(ctx, caller, PiMessage)` return the delivery result above. Worker-side
`createReportingTools(callHost)` returns definitions for `report_to_lead`
(`message_id`, `message`) and `team_message` (`message_id`, `to`, `message`).
Reject unknown identity/authority fields. The callback knows the worker; tool
arguments never contain `from`, workspace, slug, generation or native ID.

P3 must accept the concrete authenticated callback transport/registration
contract before registration. P5's fake `callHost` proves parsing and handler
binding only. P7 registers approved tools in the immutable worker package;
central Go registration remains P2-owned. Existing Codex MCP tools remain intact.

Allowed operations remain policy-specific: active retained members may explicitly
report to their own lead and use permitted same-session peer delivery; reviewer
purpose grants no roster mutation or execution-policy bypass. Cross-session
`session_communication` is lead-only and uses the existing exact-pair grant,
revocation/incarnation and recipient-hold checks. There is no new grant here and
no lookup of another session's roster/transcript. Any mixed-backend communication
requires typed endpoint support in the existing grant/message store before use;
otherwise refuse visibly, without masquerading as a Codex root.

## Initialization, queues and recovery

P2 reserves each selected address and conversation incarnation in its schema-4
creation receipt and durable binding before native creation. P5 consumes those
exact values, including the retained model/effort/instructions/access snapshot.
Validate all requested provider/model/thinking combinations through P4 first;
unsupported combinations remain unavailable, with no default model substitute.
Installed execution policy and saved role access are reported separately, as
today; instructions/read-only purpose alone do not claim a filesystem sandbox.

Initialize the lead through P2/P3 first. Root ready may coexist with selected
members `creating`/held; it does not enable member tools or automated dispatch.
Then initialize members in retained selection order using their frozen creation
IDs, configure exact private policy, and obtain native identity/history and any
required initialization-input witness. A returned ID or `Persisted:false` alone
cannot publish ready. Do not invent a bootstrap prompt or mint a new ID after
loss. Native materialization/bootstrap policy is a P3/P2 integration gate.

Architect2's proposed P2-owned port is
`PublishMemberReady(ctx, expectedRevision, handle, creationID, bootstrapOperationID)`
returning `{binding, authority, complete}, error`. It is **not yet an exported or
released API**. P2 verifies the references against authoritative P3 proof, takes
the accepted transition/runtime then team locks, CAS-publishes the same member
native ID/ready state and increments binding revision, then refreshes the live
projection without changing generation. Partial publication remains blocked;
exact retry finishes the same revision. P5 neither writes these files nor
substitutes an independent registry. Lead release/architect0 acceptance and the
P2 owner export are required before this initialization path is connected.

| Recipient/receipt state | Pi action |
| --- | --- |
| Ready, authorized, loaded, positively idle; settings applied | One ordinary Send under existing admission; Accepted only with P3's persistent native witness. |
| Busy/waiting | Do not invoke SDK enqueue/steer/follow-up. Keep an existing eligible host pending item pending; otherwise return a visible busy refusal. No new mailbox is introduced for team sends. |
| Stopped, cold or held | No automatic Ensure/Load/resume. A separate existing authorized resume may establish readiness; a tool message is not resume permission. |
| Race becomes busy inside P3 | Preserve terminal NotSubmitted receipt. Do not recycle it when idle or mint a replacement ID. An accepted future attempt contract is needed to retry execution. |
| Accepted | Lookup/reconcile original receipt; never resend, including after restart or lost acknowledgment. |
| Unknown, partial witness or effect | Hold affected operation/worker; inspect original evidence. No retry, reroute or automatic cancellation of another generation. |

Existing communication/monitor/progress pending stores keep their semantics.
Their Codex-specific prepared-attempt discard/retry paths must not run for Pi.
P5 does not treat `Retryable` as permission to violate P3's frozen negative
receipt rule. A pre-Send pending item can later be admitted only by the existing
owner scan and current policy; this introduces no background loop.

Canceling a pending message or monitor continuation does not interrupt an
accepted turn or its command. An explicitly authorized per-worker stop targets
the exact current handle through P3; SDK abort/idle is not proof every descendant
ended. Whole-session cgroup stop is separate authority and affects all members;
never use it as an individual report/utility cancellation. Generation changes
invalidate cached callers, while original durable receipts remain authoritative.

## Reviewers, observers and fresh watchers

Retained review-purpose members use their saved settings and independent history;
assignment is explicit, not automatic review on every completed turn. A fresh
reviewer outside the roster needs the same distinct utility authority proof as a
watcher; never silently add/reconfigure a member to obtain it.

The existing progressobserver scheduler/state owns interval, explicit check-now,
concerns and quiet healthy results. Pi adaptation supplies proved activity and
delivery only. Stale/unknown activity cannot wake an observer or idle lead;
observer activity does not count as development. No duplicate timer/daemon.

Fresh watchers stay owned by existing `monitoroperation` records, never retained
roster/P2 conversations. Freeze a P5 projection `PiUtilityHandle` with exact
SessionRef, monitor operation ID, utility incarnation/native ID and execution
generation; `PiUtilityLaunch` additionally references the original launch
operation/receipt, frozen policy and native creation proof. These are typed
projections, **not authorization to serialize a new format or pass the handle to
retained-member Create/Load/Bind**. P3 currently has no such utility mode.

For each new launch, resolve the installed utility policy once: package/store
identity, catalog digest, model/effort/instructions/access and concurrency limit.
Validate it through P4. A retry uses that original snapshot and launch ID, not a
fresh policy or fresh watcher. Launch inside the session boundary, with private
history/settings and shared auth. Existing operation Source freezes exact
command/cwd/input identity or CI run/attempt; no command is rerun to fix reporting.

The required supported extension must bind native creation, launch input receipt,
source execution identity and report caller to that exact operation. Store it as
a versioned Pi variant of the existing monitor operation, with old Codex records
unchanged; use P3's receipt ownership, not a second launch ledger. P3/P5/P2 owners
and architect0 must settle this small authority/codec extension before execution.
Until then `monitor_operation` start for Pi is explicitly unavailable.

The watcher reports through `monitor_operation` slots, not `report_to_lead`.
Retain existing immutable operation/slot report identities, authoritative local
exit status or CI conclusion, exact evidence and still-running/unknown effects.
Terminal success requires both source completion and positive settlement of
all operation-owned cells/tools/processes plus durable report publication.
Assistant final/idle, SDK abort or command exit alone is insufficient. A lost
report reply reconciles the existing event; a lost launch reply reconciles the
original creation/input receipt. Canceled continuation cannot clear Unknown,
kill a command or authorize a new attempt. Existing visible monitor fallback
rules remain; no fallback launches a Codex watcher inside a Pi session silently.

## Gates, compatibility and acceptance

The first package can compile/test the frozen consumer ports with strict fakes,
returning unavailable where production owners are absent. It must not advertise
installed team readiness. Remaining gates are specific:

1. P2-C/P5: member publication CAS export and persisted initialization proof;
   versioned roster/native projection without Codex placeholders.
2. P3: exact production Deliver shim/native witness; authenticated worker callback
   and immutable caller binding. P4: validated/applied role model settings.
3. Monitor owner/P3: distinct utility authority, creation/input receipt and complete
   settlement evidence; versioned existing-record codec, no retained-member bypass.
4. Central integration: backend-aware communication/monitor/observer stores and
   registrations. Unsupported variants refuse before writes or native calls.
5. Busy delivery and terminal NotSubmitted reattempt remain separately unproved;
   do not infer them from the ordinary idle Send witness.

Keep old Codex roster/message/monitor behavior and schema readers/writers intact.
No automatic rewriting of saved settings, receipt IDs or Codex records. New Pi
record versions require explicit reader/writer fencing before persistence; an
older package must refuse unsupported Pi operations, never interpret them as
empty/legacy Codex. Runtime rollback retains referenced package/policy/history
and unresolved receipts; no deletion or automatic replay. Initial source release
requires no installed runtime and changes no selected/default backend.

Focused fake acceptance covers: wrong workspace/session/member incarnation or
generation; removed/retiring caller; identity arguments rejected; reviewer/saved
policy unchanged; unavailable model/account; member creating vs root ready;
busy/held/cold zero-dispatch; idle exactly one dispatch; identical original-ID
replay vs changed-envelope conflict; Accepted/Unknown/NotSubmitted never resend;
explicit report only; caller replacement between validation and effect; grant
revocation/recipient hold; stale observer activity; utility outside roster;
policy snapshot retry; duplicate report slot; command-complete but unsettled
effects; cancel leaves command untouched. Every unavailable owner fake must show
zero native calls and zero persistent mutation.

Quick implementation checks use D's Nix environment and focused
`go test -mod=readonly` for changed `teamruntime`, `agentteams`, `monitoroperation`,
`communication`, `progressobserver`, `pihosttools` packages, plus `node --check`
and finite fake Node tests for the inert tool module. Run existing relevant
Codex report/monitor/communication regressions once after integration. A longer
cross-process disposable fixture is justified only after those gates release:
lost ACK/restart, stale caller, exact member publication, watcher launch/result/
settlement and original receipt recovery. Use a fresh authorized watcher for
long/uncertain checks; never duplicate a launched command. No checks ran in P5-D.

## Evidence and handoff

Source bounded to own D worktree and accepted records; D baseline
`6587c4c1cedabee95bcc52f4667e7d33e3a82859`, Pi pin
`a22b888a58fe55b668cc45b80749ec88d4eb4ddc`. Current P3 source is concurrent work,
not a released binary. Useful exact seams:

- D `portal/internal/teamruntime/runtime.go`: `Member`, `Client`, `Service.Assign`,
  `assignLocked`; `reporting.go`: `ResolveReporter`; `observation.go`: unknown
  activity and exact retained identity. Current native interfaces are Codex-shaped.
- D `portal/internal/monitoroperation/types.go`, `launch.go:initialLaunch`,
  `service.go:Start/Report/Cancel`, `native.go:NativeDelivery`: existing operation,
  source, policy snapshot, explicit terminal reporting and cancellation semantics.
- D `portal/internal/communication/service.go:Transport/Identity/Message`,
  `agentteams/utility.go:VerificationWatcherInstructions`,
  `progressobserver/state.go:Due`, CLI `team_mcp.go` and `monitor_mcp.go` caller gates.
- D `portal/internal/piruntime/types.go`, `pi-runtime/src/session.mjs`; C
  `conversation/backend/operations.go`: concrete current execution/outcome types.
- Owner clarification: implementer1 confirms idle-only Send, no host callback or
  utility mode; architect2/implementer2 confirm no released member-ready writer;
  architect0 accepts the independent/refusal split in principle. Implementer3
  verified proposed additive files have no ownership collision and H0 is untouched;
  its existing-import-direction constraint is recorded above.

Session identity/environment and retained architect1 Astra/xhigh/workspace_write
were reverified. Planning artifact only; source-path/link/whitespace checks are
the relevant handoff checks. No installed capability, live authorization, model
or settlement proof is claimed. Lead owns plan/state/user summary; architect0
owns synthesis and technical acceptance.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-11-pi-codex-migration/>

## TEAM-I addendum: production records and utility authority

2026-11-12 continuation after accepted P5-D. This section settles the required
next source contract; it does not extend implementer3's currently released pure
slice. Architect0 technical acceptance and lead allocation precede source edits.
The earlier list of missing codecs/utility interfaces is superseded by the
formats below; runtime evidence and installation remain separate gates.

### Scope and writer fence

Production retained reviewers and observers use the ordinary retained-member
path. The distinct utility extension is initially `verification_watcher`, using
existing monitor `Source.kind=local|ci` and report slots. Fresh-reviewer fallback
is explicitly unavailable, not a synthetic retained member or a new review
operation kind. A configuration without an eligible retained reviewer cannot
claim supported mandatory review; no self-review or waiver follows. Architect0
accepted this bounded distinction; lead chooses the supported initial release.

Every new writer must hold ordinary package-transition admission, revalidate
its exact selected package after waiting, and then acquire runtime/session and
existing domain locks in established order. Utility/domain callers do not hold
store locks while entering a P3 callback that could reenter those stores. P3
never imports `monitoroperation`; it receives a typed authority-verifier port.
No H0, schema-4 creation receipt or P2 durable-binding format changes follow.

Add the following exact capability map to D's existing runtime contract, under
P2/P7 ownership, rather than a new manifest:

```json
"piTeamRecords": {
  "policy": 1, "roster": 2, "monitorOperation": 2,
  "communication": 2, "progressObserver": 2, "utilityReceipt": 2
}
```

Missing, null, partial or unequal support refuses new writers. This advertises
codec support only; it never advertises native launch or callback readiness.
Before publishing this capability, package preflight must inspect the existing
team, monitor, communication, observer and P3 runtime stores under the selected
workspace state root, including retained records whose Pi binding is no longer
live. No inventory of another session's content is authorized to this design
agent; this is the application's existing package-transition responsibility.
Any retained schema-2 Pi obligation requires the target's complete capability
map and readers. Inconsistent/unreadable state refuses transition, not omission.
Keep the existing schema-4/Pi-binding fence too. Test old package reader/writer
refusal with frozen fixtures before enabling the new writer; source metadata
alone cannot substitute for that proof. Old executing helpers recheck selected
generation after their lock wait. No automatic downgrade or deletion of records.
In particular, an old candidate may not inventory these new domain stores at
all. Retain the already-recognized schema-4 creation journal/ordinary creation
fence for the exact session while **any** dependent Pi roster, monitor, observer,
communication endpoint/message or utility mapping/receipt remains. This extends
the accepted existing retention rule; it adds no marker or registry. Binding
retirement alone cannot remove that journal. A supported old-reader fixture must
prove rejection through this retained fence or its own exact domain scan before
the new writer enables. Unsupported Pi retirement stays refused; this addendum
does not implement retirement or invent a cleanup path to make rollback pass.

The exact [P2-TEAM-FENCE scanner contract](design.md) owns API, output, bounds and
locking. Existing `workspace-host` preflight invokes the proven **executing**
package's `workspace-portal pi-team-preflight --state-root ROOT`, repeating
`--workspace` for every registered canonical root; the target package supplies
metadata and is never selected as the scanner executable. Command composition
imports existing strict domain decoders, while P3's `retention.go` exports
`InspectRetainedUtilities(ctx, userStateRoot, workspaces)`. No session-to-domain
import, duplicate Ruby codec, registration inventory or new persisted inventory.
The child inherits the existing transition exclusion and takes no runtime/domain
mutation locks, creates no lock files and starts no native runtime. Its bounded
strict output contains only proved source/session/lead/member constraints;
Ruby crosschecks those against current binding or exact retained ready schema-4
journal/request/completion proof. No missing-binding shortcut or inferred owner.

Scan terminal/revoked records and all retained namespaces. An empty or legacy-only
schema-2 communication aggregate is still a capability obligation, but supplies
no exact Pi fence owner and the actual old reader does not scan it: refuse it as
orphan retained state. Never attach an arbitrary journal/marker or report absence.
Ordinary Codex delivery that preserves actual retained Pi arms after binding
retirement remains supported, subject to their exact retained fence constraints.

### Exact codec additions in the existing stores

All new objects use strict UTF-8 JSON, unique keys, exactly one supported schema,
bounded fields, no unknown/null identity fields and existing private atomic
write/fsync/rename rules. Ordinary message/input/operation IDs keep their exact
original lowercase UUID or 32-hex spelling; both forms are valid and distinct.
Retained roster creation receipt IDs follow the separate exact 64-lowercase-hex
P2 contract. No trim/case/hyphen normalization or cross-field ID conversion.
Incarnations/generations are 64 lowercase hex. Existing bounds remain: roster
256 KiB, monitor operation 512 KiB, communication state 16 MiB, observer 64 KiB;
admission reserves future receipt/terminal growth before an effect.

For this addendum's JSON projections, `session` is exactly
`{workspace,slug,incarnation}`; `conversation` is exactly
`{session,backend,member,incarnation,nativeId}` with backend `pi`; `utility` is
exactly `{session,operationId,incarnation,nativeId}`. A reserved utility omits
`nativeId` until native creation is positively mapped. Native IDs are opaque
bounded strings. A persisted retained-input reference is
`{conversation,operationId,action,digest}`; a utility-input reference replaces
`conversation` with `utility`. Digests are P3-produced 64-hex values, never
recomputed by P5 from presentation text. Execution generation is evidence beside
these stable references, never part of their identity/digest namespace.

| Existing file/store | New exact variant; old behavior |
| --- | --- |
| `teamruntime.Store`, existing `<slug>.json` | Schema 2 is Pi only: common `schema,workspace,slug,revision,createdAt,updatedAt,presetId,catalogDigest,teamDigest,leadModel,leadEffort,leadInstructions,members`; add required `backend:"pi",backendContract:1,sessionIncarnation,leadIncarnation`. Omit `rootThreadId` and `forkSource`. Members retain existing policy/address/index/time/state fields, replacing `threadId,projectId,createAttempted,bootstrapAttempted` with required `incarnation,creationId` and optional `initialInputId`. No native ID is duplicated: resolve it from the matching P2 binding. Pi forks/replacements need their separately accepted identity reservation; no new inheritance path here. Schema 1 remains Codex exactly. |
| `monitoroperation.Store`, existing `<operation ID>.json` | Schema 2 is Pi only; exact common keys remain `schema,id,workspace,source,brief,cancellationScope,requestDigest,createdAt,events,canceledAt,disposition,resolution` with existing optionality. Add `backend:"pi",backendContract:1`; `owner`, `utilityPolicy`, `launch` use the Pi variants below. Existing operation path, lock, admission limit, request digest algorithm, event-ID derivation and source shape are retained. Schema 1 remains Codex exactly. |
| `communication.Store`, existing `state.json` | Schema 2 retains exact top-level `schema,workspace,grants,messages`. Existing Codex grant/message entries retain their original field values and legacy endpoint shapes. A Pi endpoint is exactly `{backend:"pi",session,leadIncarnation,nativeId}`; no `thread` placeholder. Mixed/unknown endpoint shapes refuse. Pi-target delivery has `piDelivery` below and forbids legacy `options,receipt`; Codex-target delivery retains those old fields. A message may have one Pi endpoint and one Codex endpoint only under the ordinary actual pair grant. |
| `progressobserver.Store`, existing workspace directory | Schema 2 Pi state uses common `schema,paused,intervalMinutes,lastCheck,pending,concern,notice,unavailable,previousEvidence`; replace `root` with `backend:"pi",session,leadIncarnation`. Path uses the existing hash function over exact ASCII `pi:<session incarnation>:<lead incarnation>`. Pi pending uses `id,address,model,effort,message,startedAt,evidenceComplete` plus `conversation,input` (optional until reserved), `settings`, and optional `outcome`; omit Codex `thread,turn`. Concern/notice shapes stay unchanged. Schema 1 and its root-based path remain Codex exactly. |

For roster members, `creationId` is the existing owning P2 creation receipt
reference, exactly 64 lowercase hex and scoped by the reserved member incarnation;
the UUID-or32 message-ID validator must not be used for it. It is not a new
receipt. `initialInputId` is absent until the first actual assignment is
authorized, then immutable. Ready requires P2's matching ready conversation and
native proof; an optimistic roster flag is never sufficient. Retired/removed
member policy/history identities remain available as required by existing
recovery. No new Pi fork, replacement or removal semantics are inferred.

Communication upgrades schema 1 to 2 once, atomically under its current lock,
only when the first authorized Pi grant/message write requires it and the writer
fence passes. Preserve every existing grant/message ID, approval text, timestamp,
endpoint, status, options, receipt and pending obligation; do not reapprove or
redispatch legacy messages. This is a forward codec transition, not conversation
migration. New code reads/writes both variants; an old reader must refuse schema
2 without rewriting it. Same-package Codex delivery continues through the legacy
adapter. The workspace-wide file means rollback to a package lacking schema 2
is blocked even after a Pi session retires while that file is retained.

Its queued writer integration distinguishes the common package/transition/full-map
gate from actual Pi runtime admission. `UpdatePi` owns `WithPiTeamWrite` followed
by `lockedAdmitted(true)` and does not nest `Schema2Write`. Legacy writes use
`Schema2Write` before the aggregate lock, under their ordinary Codex authorization;
they need no fabricated Pi SessionRef/generation or live worker. That closure
rechecks invocation-local already-held outer transition ownership rather than
acquiring transition beneath runtime locks or mutating a shared gate. P2 owns
web's existing `withCurrentGeneration` composition and actual CLI/lifecycle
parent/child transition convention. Actual Pi effects additionally require their
exact current binding/runtime gate. This follow-up remains separately queued;
the read-only scanner release does not enable a writer or change source ownership.

`piDelivery` is exactly `{settings,input,outcome?,generation?,detail?}` once
submission is reserved; before reservation it is absent. `settings` is the
frozen P4/P3 effective settings projection, `input` the exact original retained
input reference. The domain retains its existing envelope/context. `outcome`
is `accepted|not_submitted|unknown`; no synthetic Codex receipt is added. A
pending/held message can reserve once; `submitting` with missing/uncertain P3
proof becomes held Unknown, never a fresh Send. A terminal NotSubmitted remains
held with that original receipt. Accepted may project existing `delivered`.
Grant revocation cancels only unsubmitted delivery; it cannot erase accepted or
unknown effects. Reconciliation is read-only under central read/recovery
admission, which may inspect held/busy original work. `WithDelivery` is only for
new effects and is not used to bypass or block legitimate receipt lookup.

### Pi monitor record and authority

Pi `owner` is exactly `{session,lead,originInput,generation}`. `lead` is the
retained lead conversation; `originInput` its original accepted P3 input
reference, positively active when the start request is admitted. Generation is
the launch-time execution fence. No socket/epoch/runtime-schema/Codex turn fields
are fabricated. The immutable owner is retained across restart; current runtime
admission must separately prove a permitted current generation.

Pi `utilityPolicy` is exactly
`{kind:"verification_watcher",packageRoot,catalogDigest,model,effort,instructions,
savedAccess,executionAccess,maxConcurrent,settings}`. `settings` freezes the
validated applied P4 selection, including account reference and policy revision;
no credential content. Use the currently installed utility selection only on a
new operation; retries retain the original package/policy snapshot and limit.

Pi `launch` is exactly
`{state,utility,creationId,createAttempted,messageId,envelope,settings,input?,
outcome?,generation?,terminatedAt?,termination?,detail?}`. Reserve the utility
incarnation once in the original monitor record before any creation call.
`creationId=derivedID(operationID,"utility")`; `messageId` stays the existing
`derivedID(operationID,"launch")`. `input` is the original utility-input
reference; no replica of its native witness or second receipt lives here.
`state` is `reserved|creating|initialized|submitting|running|held|terminated`.
Only proved state transitions advance it; no state retries a terminal input.
`createAttempted` is monotone and saved before the call; native ID and all
request/policy/input fields become immutable once populated.

A monitor launch's domain outcome `unknown` may reconcile to `accepted` or
`not_submitted` only when read-only Lookup of the exact original
`UtilitySubmissionRef` returns P3's authoritative terminal outcome, with its
native witness or positive refusal. Verify schema-2 utility owner/root, original
dispatch generation, and complete frozen input/settings/digest; current read
admission separately fences access and does not rewrite that original generation.
Recheck the immutable monitor tuple before publishing the domain projection.
P3 Unknown remains held; terminal Accepted/NotSubmitted is immutable. This is
recovery of a lost acknowledgment, not permission to alter a receipt/reference,
resend, mint an ID, load or resume. Reconciliation alone proves neither running
state nor source/tool settlement. A blanket freeze of every nonempty domain
outcome must not prevent this exact original-receipt reconciliation.

Events retain exact `id,createdAt,report,delivery` and the existing two slots,
`escalation` and `terminal`, with original derived IDs. Pi event delivery uses
existing `status,messageId,envelope,context,detail` and optional `piDelivery`;
omit legacy options/receipt/admittedEpoch. Resolution retains `id,at,evidence,
detail` and replaces `leadThreadId` with exact `lead` conversation. It cannot
clear a launch/input Unknown or supply missing native settlement evidence.

Add optional `settlement` to the Pi operation, exactly
`{state,sourceEvidence,toolEvidence,reportEventId,observedGeneration,observedAt}`;
state is `incomplete|settled`, evidence lists contain bounded nonsecret references
to existing authoritative source/resource/callback records, not caller claims.
Each list is at most 16 references of 1024 bytes. An incomplete projection can be
replaced by later positive evidence under the same operation lock; settled
evidence is immutable. Missing evidence is incomplete. There is no new effects
registry: this is a reference projection in the original operation.

### P3 utility API and receipt variant

P3 owns these additive types and parallel methods, composed into its existing
supervisor; they do not alter retained `Controller.Create/Load/Bind` semantics:

```go
type UtilityRef struct {
    Session agentbackend.SessionRef
    OperationID, Incarnation, NativeID string
}
type UtilityExecutionHandle struct { Utility UtilityRef; Generation string }
type UtilityCreateRequest struct {
    Utility UtilityRef // NativeID empty before first successful mapping
    CreationID string
    Settings EffectiveSettings
}
type UtilityState struct {
    Utility UtilityRef
    Generation, State string
    Persisted bool
    Settings EffectiveSettings
}
type UtilitySubmissionRef struct {
    Utility UtilityRef
    OperationID, Action, Digest string
}
CreateUtility(ctx, RuntimeRef, UtilityCreateRequest) (UtilityState, error)
LoadUtility(ctx, UtilityExecutionHandle) (UtilityState, error)
BindUtility(ctx, UtilityExecutionHandle) (backend.Operations, error)
LookupUtility(ctx, UtilitySubmissionRef) (UtilitySubmissionStatus, error)
UnloadUtility(ctx, UtilityExecutionHandle) (StopResult, error)
```

`UtilitySubmissionStatus` has the same phase/input/settings/witness/timestamp
semantics as `SubmissionStatus`, with schema 2 and its explicit utility ref.
Its exact serialized keys remain P3's current `SubmissionStatus` field names,
except `Schema:2`, added `OwnerKind:"utility"`, and `Ref` uses
`{Utility,OperationID,Action,Digest}`. `Utility` serializes
`{Session,OperationID,Incarnation,NativeID}` using the existing exported identity
field convention. No `Conversation` is allowed. Schema-1 retained receipts and
their digest bytes remain unchanged. The utility digest is P3's single
`UtilitySubmissionDigest` over the JSON struct
`{Version:2,OwnerKind:"utility",Ref:<Digest empty>,Input,Settings}` in that exact
field order, using the same `json.Marshal` and SHA256 as its existing helper.
Consumers reference its output; a cross-language fixture fixes exact bytes.

`BindUtility` uses P3's explicit `UtilityIdentity(handle)` helper, returning a
neutral `backend.Identity` whose `BackendID` is `pi`, `ConversationID` is the
exact native utility ID, `Directory` is the canonical session work directory,
and `Generation` is the handle's current generation. `ScopeKey` is exactly
`pi-utility:` plus lowercase SHA256 of Go `json.Marshal` of the ordered struct
`{Version:1,Kind:"utility",Utility:<full UtilityRef>}`. Generation is excluded
from that stable scope hash. Fix the bytes in a cross-language fixture alongside
the receipt digest. Verify/Read/Send/Interrupt compare this complete projection
and the matching utility-owned mapping before any effect. Never pass a retained
`HistoryRef`/`ConversationRef`, reuse a retained scope-key derivation, or route
solely by `ConversationID`. This domain separation applies even if opaque native
IDs happen to match; it is not a second native identity or registry.

Use the same mapping/worker/receipt engine implementation with an internal tagged
owner (`retained` or `utility`), not a second engine. Utility mapping schema 2
contains the same creation/native/history/initialized/persisted evidence as
retained schema 1, with `OwnerKind:"utility"` and UtilityRef instead of member
ConversationRef. Store beneath the existing P3 session-incarnation root at
`utilities/<monitor operation ID>/<utility incarnation>/`, with the same
`agent/`, `history/`, `conversation.json`, `submissions/<original ID>.json` layout.
This is per-operation runtime state subordinate to the original monitor record,
not a utility registry or new session authority. Session runtime/cgroup/mount
namespace and shared auth directory remain identical to the retained workers'.

Inject a P3 `UtilityAuthority` consumer port with the concrete signature:

```go
type UtilityGrant struct {
    Runtime RuntimeRef
    Utility UtilityRef
    CreationID, LaunchOperationID string
    Settings EffectiveSettings
    Input SendInput // exact frozen launch envelope/context
}
WithUtility(context.Context, RuntimeRef, UtilityRef, string,
    func(UtilityGrant) error) error
```

The string is the action enum below, not an arbitrary method. The central
monitor owner implements it using the original operation, current P2 session
authority, retained policy and lifecycle/hold checks. Supported actions are
`create|load|bind|send|unload`; callbacks execute under appropriate runtime admission,
but no short monitor file lock is held during P3 execution. Persist/freeze the
expected operation before releasing the store lock; compare it again before
publication. Lookup instead uses exact read/recovery authorization, with no
activation. A missing verifier refuses. P3 owns native proof, not the monitor
record's interpretation. No utility is put into P2 conversations or a roster.
P3 compares creation/settings/input requests to this host grant, revalidating
each effect rather than treating Bind as lasting permission. Utility Send accepts
only its original frozen launch ID/envelope/action/settings; no additional prompt
or follow-up is admitted by this extension. The shared receipt reader verifies
both owner tag and expected root: utility schema 2 in a member root, or a retained
schema-1 receipt in a utility root, is a conflict rather than a conversion.

### Initialization, callback and settlement sequence

For selected retained members, use accepted P2-C `PublishMemberReady` and P3
`CreationVerifier`, not a new writer. No public header-only persistence seam is
proved. `Create` may return initialized/mapped with no history file; nil
bootstrap proof certifies only no-file/no-dispatch, not ready. Freeze the first
real authorized assignment's original message ID as `initialInputId`, pass its
exact team envelope/action context through the initialization owner, then verify
the original native witness and host receipt before publication. Root input
alone uses `initial`; members retain `team:<slug>:<from>:<to>`. A roster reference
does not replicate text/settings already in P3's receipt. P2 owns the accepted
transition SH → runtime EX → team operation/short roster lock publication order
and projection completion. No synthetic prompt, raw JSONL or private flush API.

A fresh watcher uses its actual monitor launch brief as its first real input.
Reserve the original monitor record/policy/utility incarnation, save attempted
creation, create the exact mapping, then reserve/send its original launch input
through the utility receipt engine. `initialized` is not running; only Accepted
native+host witness permits that projection. First input NotSubmitted/Unknown
holds the original operation. A lost response never creates a replacement
utility, launch ID or input. Native history missing after uncertain dispatch
stays held; `open(missing)` is never repair. An empty undispatched mapping can
be reconstructed only with positive no-dispatch and old-worker-drain proof.

The [BRIDGE-D contract](pi-host-tools-plan.md) owns callback transport: existing
worker pipes and portal-attached duplex existing `control.sock`, not a new
listener. Its exact `CallbackSubject` utility arm contains
`Session,MonitorOperationID,Incarnation,NativeID,Generation`; the outer callback's
`InputOperationID` carries the original input ID. The supervisor captures both
from the original operation and mapping, never tool arguments. Before a
side-effecting handler, require that exact input's durable Accepted receipt and
native witness. Prepared/dispatching waits only within BRIDGE-D's bounded deadline
without witness/receipt/store locks; Unknown/NotSubmitted holds or refuses.
Native tool origin alone is not input-acceptance proof.

Immutable callback identity includes the persisted assistant anchor/toolCallID,
action and original input ID; generation fences current caller only. BRIDGE-D
owns its `linear-v1` selection token and exact LP32-UTF8-v1 utility tuple ending
in `rootEntryID`; TEAM-I's `UtilityIdentity` scope hash is a separate routing
projection, never a substitute for that callback lineage proof. Utility tools
permit only exact bound
`monitor_operation status/report`, plus the approved ordinary tool policy;
no retained report/peer/question/plan/communication identity is granted.
BRIDGE-D owns authoritative callback validation/drain counters; P5 owns domain
report validation and existing durable event receipt. Do not add a bridge ledger.

For local Source, launch/observe exactly the existing `invocationId` and bind
P3's owned resource/tool handle; CI observes exactly its provider/run/attempt.
Terminal report includes the authoritative result and existing report slot ID.
Accept durable report publication independently from declaring settlement.
Settle only when source evidence is terminal, the original launch/input outcomes
are known, all operation-owned registered resources and in-flight callbacks/tools
are proved drained (including the reporting callback), and the terminal event
is durable. The reporting callback may receive its durable event reply before
its own drain; a later owner reconciliation completes settlement. This avoids
waiting for a callback to finish while it is still publishing its reply.
Unknown/untracked descendants or incomplete native tool inventory prevent
settled status. This contract does not claim exactly-once arbitrary tool effects.

SDK idle/final/abort is insufficient. Source command exit alone is insufficient.
Lead delivery is a separate original input receipt and may remain held; do not
repeat the source command to repair that delivery. Existing monitor concurrency
capacity is freed only after positive utility exit/drain proof. Cancel revokes
continuation, not command execution; target-specific unload still needs its
own authority. Whole-cgroup stop remains a separate session operation. Restart
can read and reconcile the original records; it cannot silently bind a new
generation, reload a stopped utility or retry Accepted/Unknown/terminal negative.
Any permitted later reattachment must prove old generation drained and current
explicit resume authority, preserving original logical IDs and receipts.

### Source windows, fixtures and outstanding proof

| Owner/window | Exact dependent work |
| --- | --- |
| P5 / implementer3 after lead release | Existing `teamruntime/runtime.go`, `reporting.go` plus `pi_*` codec/adapters; `monitoroperation/{types,store,service,launch,authority,lifecycle}.go` with Pi variants; `communication/{store,service,native}.go` and `pi_delivery.go`; `progressobserver/state.go` and Pi policy. Add focused codec/fault fixtures beside each. Keep all legacy branches/fixtures. |
| P3 / implementer1 | `piruntime/{types,receipts,worker,supervisor}*.go` and own native mapping/session files as actually named in its current package; shared engine tagged-owner support, utility API/native witness/settlement. P5 does not edit worker entrypoints. No capability before the corresponding fixture passes. |
| P2 / implementer2 | Existing central registration/read-recovery/member initialization, accepted publication port, runtime contract and package preflight in `session/contract.go`, `session/runtime-contract.json`, `libexec/workspace-host` and existing backend helper. Sequence with current P2-C format work, no concurrent writer edits. |
| BRIDGE-D / architect2 and its released implementer | Exact caller transport/tool registration/drain contract; TEAM-I only supplies utility subject/domain authority. P7 packages approved capabilities/modules in its existing window. |

Focused fake fixtures must prove: old Codex bytes/values round-trip; unknown,
duplicate and mixed-owner keys refuse; schema-2 old-reader/old-writer refusal;
workspace communication upgrade preserves pending legacy delivery; target
preflight detects retained records after binding retirement; wrong current
generation cannot mutate; delayed callback cannot spoof another utility/member;
first real assignment publishes only after actual witness; nil/empty bootstrap
cannot; accepted/unknown/negative replay never sends; original UUID and 32-hex
filenames remain distinct; utility lookup cannot cross owner kind; create and
receipt crash points keep same operation; settings/policy retry frozen; duplicate
report slot returns original; durable report does not imply reporting callback
drained; known source exit plus unknown child remains incomplete; cancel leaves
commands/receipts intact; stale observer/invalid grant cannot dispatch.

Quick checks remain scoped D Nix Go/Node fixtures. Longer disposable cross-process
proof follows the released owner implementations and review: utility launch,
native first-input witness, report callback/reply drain, source/resource
settlement and restart/lost-ACK cases. Installed root launcher/tool availability
is still a separate gate; no live auth/model call is needed for these fakes.
Fresh-reviewer fallback, busy enqueue and automatic negative retry remain
explicitly unsupported rather than introduced in this extension.

Evidence: existing `monitoroperation/store.go:read/reserve/validateTransition`,
`service.go:validateOperation/Start/Report/Cancel`, `lifecycle.go:knownMonitorReceipts/ProveQuiescent`;
`teamruntime/runtime.go:Validate/load/Update`; `communication/store.go:read/locked/admit`
and `service.go:Dispatch`; `progressobserver/state.go:Load/Save`; current
`piruntime/receipts.go:SubmissionDigest/receiptEngine`. Source inspection and
owner clarifications only; no tests, application edits or runtime actions in
TEAM-I. This addendum requires architect0's exact read before source release.

## Production composition checkpoint after central schema1/2 acceptance

2026-11-12. Bounded clarification from accepted TEAM-I/P5 evidence and direct
owners2/3 facts at central `25af2aba` plus producer
`d4e15e9d6b36fb2c4f4ff93e4f68a290494e265b`. No application checks or new source
survey. The completed schema1/2 history/review checkpoint proceeds independently;
team/reviewer/observer/watcher/communication workflows remain requested scope.
Ordinary physical Pi execution needs no native-routing-3 capability.

**Conclusion: one complete production team/utility backend package is not yet
source-sufficient.** Existing adapters and authority gates supply substantial
joins, but do not supply a retained-lead monitor API, production settlement proof
or the required pre-startup same-Manager assembly point. These are explicit
remaining contracts, not permission to register incomplete tools. No source
allocation follows from this addendum.

### Actual available joins and ownership

Paths below are in D's `portal/internal/` unless qualified. This replaces stale
"API missing" descriptions above only where the named export is now implemented;
it does not promote adapter fixtures to end-to-end proof.

| Join | Existing exact surface and remaining composition |
| --- | --- |
| Single Manager | `web/pi_providers.go`: `NewPiCreationServices(Config)`, private `newPiCreationManager`/`piManagerConfiguration`; `web.Config.PiCreation *PiCreationServices`, whose `Runtime PiCreationRuntime` retains the actual Manager. Its Config currently has no utility authority/read injection. Use this same object for utility effect/read authority, Controller and host attachment; no second Manager. |
| Current domain admission | `web/pi_team_admission.go`: Server already implements `WithPiTeamWrite(ctx,SessionRef,generation,func()error)error`, `WithPiUtilityRead`, `WithUtilityRead` and communication `WithPiInputRead`. These are real package/current authority gates, not production monitor/report construction. Record-write SH does not itself grant a native effect. |
| Utility adapter | `monitoroperation/pi_runtime.go`: `PiRuntimeAdapter{Domain PiDomainAuthority,Controller piruntime.UtilityController,ReadAdmission piruntime.UtilityReadAuthority}`. Pointer implements P3 UtilityAuthority/UtilityReadAuthority. `Launch(ctx,RuntimeRef,id)error`, `ReconcileLaunch(ctx,RuntimeRef,id)error`, `Report(ctx,RuntimeRef,UtilityRef,inputID,ReportRequest,time.Time)(string,error)`, `Unload(ctx,RuntimeRef,id,time.Time)error` already exist. Configure Manager with this adapter and point adapter.Controller at that same Manager before use. |
| Utility domain | `monitoroperation/pi_service.go`: `PiDomainAuthority{Store,Admission,Verifier}` consumes `VerifyPiUtilityEffect(ctx,RuntimeRef,PiOperation,action)error`. `PiReportService{Store,Admission,ReadAdmission}` supplies original-operation status/report, `CancelPi` and `ReconcileSettlement(ctx,scope,generation,id,PiSettlementVerifier,time.Time)error`. Existing Store.ReservePi/UpdatePi and NewPiOperation own durable state. The production effect verifier and source/settlement collector are absent. |
| Authenticated utility callback | Existing P3 `HostCallbackHandler.HandleHostCall(ctx,HostCall)(HostReply,error)` follows original Accepted/native-lineage validation. `pihosttools/utility.go` supplies `BindUtilityTools(PiUtilityCaller,UtilityHandlers)`; caller must be built from HostCall.Runtime, Utility subject, Generation and InputOperationID. `MonitorDomainHandlers{Service,Runtime,Now}` connects status/read and explicit report to the adapter. Only exact utility monitor status/report are supported; `createMonitorTools` already forwards nativeToolCallID/signal. |
| Retained explicit report/peer | `teamruntime.PiDelivery{Admission,Native}` uses `PiAdmission.WithDelivery(ctx,PiCaller,PiMessage,func(PiPreparedDelivery)error)error` and real Manager `Deliver/Lookup`; `Deliver(ctx,PiCaller,PiMessage)(PiDeliveryResult,error)` sends once. `pihosttools/team.go` BindTeamTools and existing Report/Peer handlers receive only authenticated retained callers. Central production admission/handler construction remains absent. Explicit reviewer assignments use retained review-purpose settings; final answers never auto-report. |
| First real member assignment | `web/pi_member_publication.go` already exports `PublishMemberReady(ctx,expectedRevision,handle,creationID,bootstrapOperationID)`. `web.Config.PiMembers PiMemberPublicationAdapter` has no production adapter/caller. Supply its existing `LockRoster(ctx,handle)(PiMemberAdmission,release,error)` and CreationVerifier; no new P2 writer. Original first assignment/envelope/settings/input proof stays frozen. Call publication with no locks; retain team operation ownership while releasing the short roster lock before native verification/publication. |
| Existing aggregate and consumers | `web/pi_workflows.go` newPiWorkflowComposition/ensureAttachment currently exposes only publish_plan/request_user_input_async; HandleHostCall rejects utilities and composePiWorkflowPolicy rejects other factories. Extend that same aggregate and first-Create factory selection only after complete handlers are available. `web/communication.go` still selects Codex NativeClient; progressobserver.PiDue is pure and uncomposed. Existing policy/store/scheduler owners must select Pi adapters; no new loop, grant or client. |

P3's UtilityController method signatures already exist: CreateUtility, LoadUtility,
BindUtility, LookupUtility and UnloadUtility with TEAM-I's exact refs/state/result
types. This is not a missing Controller interface. Accepted adapter evidence
`0e8c0fb5` used the actual interface/digest, not a complete native Manager flow;
combined functionality still needs actual original-input/callback/settlement
proof. Nothing here permits loading a utility as recovery or substituting a
retained ConversationRef.

### Three precise blockers and the shortest next facts

1. **Startup assembly (owner2, later constructor window).** Actual constructors
   are `web.New(Config)` and `web.NewContext(ctx,Config)`, not NewServer.
   NewContext constructs or replaces services/Manager, allocates Server, immediately
   calls newPiWorkflowComposition, then loads/reconciles retained state and starts
   display/recovery/observer/communication/monitor workers before returning.
   No existing hook or PiCreationServices binder allows safe post-return assembly.
   The shortest required declaration is one internal assembly step after the
   final Server/config/services exist and before newPiWorkflowComposition and
   retained startup effects in `web/server.go`, with the matching private factory
   change in `web/pi_providers.go`. It must bind the final Manager retained in
   server.config; configurePiCreation may replace an earlier injected value.
   Owner2 must freeze that construction/lifetime signature before release; this
   addendum does not invent a closure field or authorize changing closed `25af`.
2. **Retained-lead monitor caller boundary (P5/BRIDGE design with owner2 consumer,
   lead allocation).** Owner3 confirms no accepted Pi retained-lead monitor
   start/status/cancel handler or signature exists. NewPiOperation/ReservePi,
   PiRuntimeAdapter.Launch and CancelPi are building blocks, not this authority.
   Utility-only BindUtilityTools/status/report and legacy Codex monitor Service
   cannot impersonate it. The shortest next contract must name the exact trusted
   retained lead caller/original Accepted input, frozen installed watcher policy,
   source selection and immutable StartRequest/operation identity, existing
   reservation/Launch/status/continuation-cancel methods, and matching approved
   factory projection. Cancellation must not interrupt source commands. Until
   accepted, retained monitor tool registration is unavailable, not routine wiring.
3. **Positive source/settlement proof (P3/host owning collectors plus P5 consumer,
   owner2 composition).** `PiSettlementVerifier.ObservePiSettlement(ctx,PiOperation)
   (PiSettlementObservation,error)` exists only as a consumer with fakes at the
   accepted P5 boundary. No production collector joins exact local invocation/CI
   run result, operation-owned resource identities, callback/tool inventory and
   positive utility exit/drain. The shortest next fact is each existing owning
   read/export able to prove that tuple, including reporting-callback drain; if
   any is absent, its narrow owning port must be designed/released explicitly.
   Empty pending counters, report success, command exit, SDK idle or Unload's
   verified exit alone cannot implement this collector. No generic effects
   framework, synthetic success or new ledger is an acceptable replacement.

The central PiUtilityEffectVerifier also needs its precise implementation under
current session admission: verify the original monitor operation/owner input,
frozen installed policy/settings, utility identity, allowed action and current
runtime without holding a short monitor lock. This is an existing consumer port
whose production composition must be part of the same bounded contract, not a
new authority API. Owners2/3 identify no implementation in accepted central25af.

### Invariants and eventual bounded acceptance

Preserve one real Manager and one session supervisor/cgroup/namespace. Expose
HostTools only after both callback handlers and current policy/model/account
validation exist; no native3 or default-backend switch. Retained roster access,
model/effort/instructions and independent review-purpose assignments stay exact.
Fresh-reviewer fallback remains unavailable and cannot waive required review.
Cross-session communication uses only the existing approved pair policy/stores.

Manager utility methods acquire configured per-effect authority themselves;
do not wrap them in a duplicate outer gate. Native work holds no short monitor
file lock. Callback report may arrive before Send returns: use exact original-ref
Lookup, then recheck the immutable operation tuple before report publication.
Reserve create intent/mapped utility/input digest before each first corresponding
effect. After reserved input, retry Launch is Lookup only. Accepted/Unknown/terminal
NotSubmitted never resend, mint IDs or infer current running state. Cancel revokes
continuation only; explicit Unload is separately admitted and does not settle.
Release monitor capacity only after positive complete settlement of the original
operation and reporting callback. Restart reads/reconciles; it never auto-loads,
resumes or substitutes a generation.

Use existing parsers, stores and schema1/2 full-map/old-reader guards; preserve
Codex branches and mixed communication aggregates. No new schema, registry,
scheduler, public server or harness is needed merely for composition. Once the
three contracts are sufficient and lead releases exact owner windows, the smallest
acceptance cases are: same final Manager assembled before any startup effect;
authenticated retained report/peer one-send and first-real-assignment publication;
fresh watcher reserve/create/original-input Accepted; early native monitor report
before Send reply with duplicate/lost-ACK reconciliation; utility-only caller
restrictions; current read versus original generation; known source exit with
pending callback/resource remains incomplete; later full positive drain releases
capacity; cancel leaves commands/receipts untouched; restart/Unknown/busy/held
causes zero replacement dispatch; ordinary Codex regression unchanged.

Use the existing P3 admitted Manager/worker fixture and owning P5 tests, with
physical fake providers and actual persisted receipt/callback flow. Strict fake
ports establish refusal/identity behavior only, not installed/production completion.
Quick Nix composition checks precede the single finite combined case; uncertain
or longer checks use a fresh watcher under the normal rule. No tests run here.
The full backend package remains **blocked on the three named declarations/proofs**;
owner2's capacity alone does not release it. This addendum is for architect0's
focused sufficiency/blocked-boundary acceptance and lead sequencing, without
holding the completed schema1/2 review checkpoint.

## TEAM constructor and settlement facts: bounded follow-up

2026-11-12. Architect0 accepted the preceding join/blocker assessment in canonical
P5 (lead report `1af59887-063f-4623-9afd-c1d1597c7adb`), not a complete backend
source release. Architect0 technically accepted the constructor order and exact
missing-proof assessment below in canonical design.md:2204/2241 (lead report
`e91b7a48-360d-4f13-9a84-c6343fc13139`). This settles constructor source fit,
not the complete production backend package or its source release. Architect2
separately owns the retained-lead monitor start/status/cancel and full original
caller-input question. No native3 dependency or source allocation is introduced.

### Same-final-Manager construction order

Use the existing preparation/final-construction split; do not add a public hook,
forwarding authority delegates, binder field or after-return closure. Owner2
confirmed NewContext invokes no Pi Runtime method before Server allocation.
configurePiCreation/newPiSelectionServices there only prepare frozen catalog,
account bindings, roots/providers and Selection; NewManager only validates and
constructs, without invoking its configured authority callbacks.

The smallest exact later owner2 change is confined to `web/server.go` and
`web/pi_providers.go`:

1. Keep configurePiCreation's preparation and current package/profile checks in
   their existing pre-Server position. Remove only the conditional production
   newPiCreationManager call from that location.
2. Allocate Server as today. Before newPiWorkflowComposition, loadCreations,
   retained reconciliation, routes/startup workers or any Ensure/Attach/Create,
   construct the private P5 domain/adapter using this Server's actual Store,
   admission/read gates and the separately settled effect verifier.
3. Pass that adapter's existing `piruntime.UtilityAuthority` and
   `piruntime.UtilityReadAuthority` through narrow private factory arguments into
   the ONE final Manager's Config. Use the final prepared services in
   `server.config`, not the earlier local Config/factory object. Existing fields
   already suffice; no PiCreationServices field or public Config hook is added.
4. Synchronously set the private PiRuntimeAdapter.Controller to that exact
   returned Manager, then finish/publish the same services Runtime+StartRequest
   as the current factory does. Only then invoke newPiWorkflowComposition and
   ordinary startup. No Controller/authority call, goroutine, registration or
   effect occurs during the incomplete construction, and no later rebinding or
   Manager Config mutation is allowed.

Preserve current branch semantics: with PiProviderConfig nil, retain the supplied
Config.PiCreation/Runtime exactly, without a replacement Manager or Ensure.
Standalone NewPiCreationServices retains its current construction; absent utility
authority means utility support unavailable. An injected Manager cannot gain
missing immutable authorities after construction. Optional team/utility support
for trusted injection requires that injection already provide the same completed
assembly, otherwise it stays unavailable. With PiProviderConfig supplied, keep
configurePiCreation's existing replacement behavior and bind only the resulting
final services. Preserve Pi-unavailable/Codex-retained failure behavior and
cancelOperations on fatal constructor errors; publish no partially assembled
adapters. No startup locks or goroutines are needed for this synchronous move.

This settles the source-fit order, not the absent verifier/monitor/settlement
contracts. Focused later constructor cases must prove exactly one final Manager,
no effect before Controller/authorities are bound, final-services replacement
identity, unchanged trusted-injection branch and no partially published support
on failure. The closed schema1/2 source/review checkpoint remains unchanged.

### Exact settlement consumer and missing authoritative facts

Owner3 confirms the accepted `monitoroperation/pi_service.go` contract:

```go
type PiSettlementObservation struct {
    SourceTerminal, InputKnown, ResourcesDrained, CallbacksDrained bool
    ToolsDrained, UtilityExited, CompleteInventory bool
    SourceEvidence, ToolEvidence []string
}
type PiSettlementVerifier interface {
    ObservePiSettlement(context.Context, PiOperation) (PiSettlementObservation, error)
}
```

ReconcileSettlement enters current record-write admission, captures the original
operation, calls this verifier without a short monitor-file lock, then rechecks
the entire unchanged snapshot before publication. Settled requires all seven
booleans, original launch outcome accepted, TerminatedAt/nonempty terminated
state, and the durable exact terminal event. Both evidence lists must be nonempty
for settled, at most 16 references each, each at most 1024 bytes. Settled evidence
is immutable. The report callback can return its durable event before it drains;
only a later exact observation can prove that dimension. Nil/default values are
unavailable/incomplete, never a partial-success settlement.

The current evidence identifies these owning proof requirements without freezing
new hypothetical API names:

| Dimension | Existing usable fact / exact remaining source contract |
| --- | --- |
| InputKnown | Actual P3 UtilityController.LookupUtility accepts the complete saved UtilitySubmissionRef. Validate original owner/root/input/settings/digest/generation and native witness or terminal refusal, with separate current read admission; only accepted launch can settle. No newest-input inference. |
| SourceTerminal | No accepted host source-read verifier is identified. The frozen local invocationId+argv/cwd/inputIdentity/revision or CI provider/run/attempt selects the source; watcher ReportRequest is not authoritative result proof. The host/source owner must supply an exact existing result observation or identify the minimal absent owning read port. |
| ResourcesDrained | Requires every operation-owned registered resource/descendant and its positive terminal proof, with unmatched/unknown effects held. Individual resource handles/statuses do not establish the complete operation inventory. P3 owns this evidence. |
| CallbacksDrained | Requires exact authenticated callback inventory through the reporting callback's completion, bound to the original utility input/worker generation. P3 private counters alone are not a public proof port. |
| ToolsDrained | Requires actual native ordinary/tool/nested-resource completion evidence; a tool result, idle or final response cannot stand in for unknown descendants/effects. P3 owns this evidence. |
| UtilityExited | Requires positive exit of the exact original utility worker/process identity. Unload's VerifiedExit proves only that stop result; restart/current empty worker pointer cannot prove the original process exited. |
| CompleteInventory | Requires a complete original-operation tool/callback/resource/worker inventory and zero unknown/untracked descendants; omission of a category cannot produce true. No accepted collector currently supplies this conjunction. |

The shortest next source fact is owner1's exact public runtime exports for the
last five dimensions, including retained proof after unload/restart, and the
host/source owner's exact terminal-source observation. If those exports do not
exist, name only their smallest owning observational contracts before collector
composition. Do not synthesize a new effects framework, registry, persisted
parallel ledger or universal successful verifier. P5 validates/publishes the
existing domain record; owner2 composes real proof only after its sources are
settled. Constructor readiness alone does not release full utility execution.

**Owner-confirmed runtime/source limit.** Owner1's direct reply closes the pending
export question: there is **no exported complete positive utility settlement
certificate** in current P3. Available APIs have these exact limits:

- UtilityController.LookupUtility proves original admission/witness, not execution
  completion. UtilityExecutionHandle contains UtilityRef+Generation, without an
  original PID/start/process-group/exit or source-inventory certificate.
- Controller.Resources returns cgroup/scratch accounting and exclusions, not an
  enumeration of operation-owned identities. InspectResource(ctx,ResourceHandle)
  returns one caller-known Handle/Phase/ExitCode; StopResource stops one resource.
- A live successful UnloadUtility checks receipts, callback count/unknown, native
  idle/held, worker.Wait, original process-group emptiness and unexpected session
  children before saving Loaded=false. Its transient StopResult cannot be treated
  as a retained complete certificate: the already-unloaded path can return
  VerifiedExit from bookkeeping without freshly proving the original process or
  source inventory. Neither nil worker nor Loaded=false proves that evidence.
- InspectRetainedUtilities is pure capability inventory, and ObserveWorkflow is
  retained-conversation ToolPolicy scope; neither proves utility drain. Private
  counters and H0 successor settlement cannot establish monitor source attribution.

The minimal absent P3 contract is therefore an owning observational proof bound
to the exact original UtilitySubmissionRef **and captured original utility worker
incarnation/process identity**, with positive exit and complete attributable
resource/tool/callback drain, under current read authority. It must distinguish
live evidence from retained proven evidence and refuse absent provenance after
restart. Its concrete API/retention shape is not frozen here; no existing export
can be renamed or wrapped to pretend it supplies these facts. P3 owns that narrow
missing declaration; source/domain adapters supply their own authoritative facts.

Architect2/owner2 additionally confirm no current production source-ownership
producer binds a local invocation or CI provider/run/attempt to this caller and
session. The **same** missing host/source observation contract must cover both
start-time ownership and later terminal result for the original frozen Source.
A supplied invocationId, argv/cwd, CI identifier or watcher report establishes
neither. Establish the existing runner/CI owner's authoritative identity/result
record and approved caller/session relationship before freezing that contract;
there is no second collector or parallel source ledger. Without it, both retained
monitor Start admission and SourceTerminal remain unavailable. Architect2 owns
the Start consumer and original-active-input callback contract, without duplicating
this producer. The shortest next release question is the exact owning source
identity/result producer plus P3's missing original-worker drain proof declaration;
constructor source-fit is now settled, full production composition is not.

## R4 public prompt-options observation: accepted corrected source fit

Architect0 technically accepted this correction and replaced the false canonical
interface claim (lead report `ab11fec0`). It fits the existing four-file R4 scope;
owner1 may resume dependent JS within lead's release. Actual pinned SDK proof
remains required and unrun at this checkpoint.

Owner1 corrected the source premise in canonical design.md's same-worker
instruction application clause: pinned Pi 1.5.2 ordinary ExtensionContext has
getSystemPrompt, but getSystemPromptOptions belongs only to
ExtensionCommandContext. An inert session_start event context cannot provide
the latter. The earlier ordinary-context claim is withdrawn; pure Go/Node checks
do not prove the actual SDK path. Owner1 stopped dependent execution before
effects while this source correction was resolved.

The smallest sufficient public observation is the same actual AgentSession's
public extensionRunner getter, followed by that runner's public
createCommandContext(), calling ONLY getSystemPromptOptions(). Owner1 confirms
runner.js:732–766 constructs a plain context using descriptors of createContext
and installs lazy method closures; construction invokes no command, wait, reload,
rebuild or mutation. The options accessor asserts the runner is active and calls
its bound getSystemPromptOptionsFn. AgentSession._applyExtensionBindings binds
that function to the session's actual base prompt options and getSystemPrompt to
its current systemPrompt; bindExtensions applies these bindings before awaiting
session_start. Do not read private SDK fields in the worker: these source facts
justify the public path and remain part of the pinned construction proof.

Require completed same-session bind and the actual inert session_start capture;
capture session.extensionRunner after bind and retain its identity with that
session and the accepted loader. On every existing instruction verification,
require that same active runner, create a fresh command context, call only the
read accessor and detach its returned options before comparison. Keep the event
context solely for getSystemPrompt. Recheck runner/session/loader identity and
all existing exact observations: whole loader append array, options addendum
equal to the whole array joined by two newlines, genuine customPrompt and
contextFiles from that loader, and session.systemPrompt equal to the event
context's getSystemPrompt. Preserve the closed actual builder/extension proof,
literal-byte digest and verification timing; no substring match or parallel
prompt parser/builder is added.

The runner's unbound fallback normalizes cwd-only options. It is not accepted
binding evidence and cannot satisfy the exact nonempty append/whole-options
proof. Missing/replaced/inactive runner, incomplete bind, missing event context,
fallback or mismatched options hold before effects under the existing contract.
No command is registered/dispatched, and no other command-context method is
called or exposed. This changes only the public read accessor in the existing
R4 session.mjs construction/verification closure and focused real pinned SDK
cases; it adds no SDK patch, API, protocol, stored field or source allocation.
Actual pinned SDK preflight has not run; native fix history, production capability
and downstream consumer release remain separate. Lead retains source/release
sequencing.
