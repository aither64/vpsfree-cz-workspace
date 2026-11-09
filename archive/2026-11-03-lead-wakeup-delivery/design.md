# Lead wake-up delivery implementation brief

Status: implementation authorized by the user's subsequent “implement it”,
relayed by the lead on 2026-11-03. Architect: architect0. The lead releases the
bounded packages below. Integration, deployment and session lifecycle actions
remain unauthorized. Native end-to-end acceptance is pending.

## Recommendation and established defect

Add a small runtime-owned monitoring operation with a fresh utility thread,
separate from the retained team. Persist its outcome and submit one identified
event to the owning lead through the existing durable start/steer transport.
The runtime, rather than an idle model or native collaboration message, owns
delivery. Keep the current member-only `report_to_lead` guard intact.

The application currently has no durable bridge from temporary watcher completion
to lead input. The monitor skill promises automatic continuation without stating
the active-parent limitation. A utility is intentionally outside the roster, so
its team-report rejection is expected. This explains the missing supported handoff;
it does not independently prove every native scheduling detail in the incident.

Until the new path passes acceptance, keep the parent turn active and use native
interruptible waits. Qualify the monitor skill and consuming instructions
accordingly. Ending a turn while promising later continuation requires a durable
operation-start acknowledgement from the new runtime path.

## Evidence and limits

The exact user seed and acceptance are in [plan.md](plan.md). The four independent
diagnoses are the authoritative detailed evidence:

| Report | Established evidence | Limit |
| --- | --- | --- |
| [Runtime reporting](diagnostic-runtime-reporting.md) | Exact native caller/roster guard, session/team locks, durable start/steer; five runtime and three client fixture tests passed | No utility-to-idle-lead native test |
| [Native utility](diagnostic-native-utility.md) | No runtime child-completion handler; activity events are display/invalidation; exact native schema exposes potential parent provenance | Schema extraction is not live spawn/completion proof |
| [Prompt delivery](diagnostic-prompt-delivery.md) | Existing notification fixture and eight client tests passed; restart, uncertainty and queue constraints; reusable readiness pattern | Controlled RPC fixtures, not stock native utility execution |
| [Monitor contract](diagnostic-monitor-contract.md) | Installed skill/source and catalog provenance match; policy lacks callback registration | No wake-up experiment |

Relevant inspected revisions: dev-workspace
`c2182254d29c4175c3e9fe4267e5a92dd1da6b79`, codex-web
`d3a29bee90ef00a08816920408c596152339a637`, vpsFree extension
`e4e7e95ed39bf514b33f8f8ae61ba9868de060ae`. The installed generic source was
independently bound to this revision by NAR hash and relevant file equality.
The selected application is
`/nix/store/0q7rc75dh4mjrxpb37m1hchfwcbmpa7a-dev-workspace-0.2.0`;
the schema probe used packaged Codex 0.165.0. Exact source/input/native hashes
are retained in the reports; they do not prove the running daemon's identity.

The supplied incident remains seed evidence. Real reports within this session
received active-turn steering receipts. Neither those receipts nor the native
reporting fixture's fabricated `fixture-lead-turn` establishes an idle wake-up.
The proposed implementation has not run any acceptance test below.

## Smallest supported launch and delivery choices

Use a runtime-owned standalone utility thread, created through existing
`CreateProject` / `StartThreadWithSettings` APIs. Reuse the exact-project creation
and unknown-start reconciliation approach already present in
`portal/internal/teamruntime/runtime.go:1281–1471`, without creating a roster
member or copying member lifecycle wholesale. Persist launch intent before native
creation; reconcile the original project/thread after a lost reply. Do not create
a second watcher merely because the first launch acknowledgement was lost.

For each new operation, resolve the currently selected installed catalog's
`utilities.verification_watcher` model, effort, instructions and operation
lifetime, plus effective execution policy. Retain that exact operation snapshot
for retries/recovery. Preserve the current Luna/low and full-access/never
policy and `max_concurrent = 1`. Use a fresh minimal brief, not a conversation
fork. The existing watcher still runs or observes only its assigned verification.
This proposal adds neither command scheduling nor automatic command retries.

A fresh managed native-only fallback watcher likewise selects the currently
installed validated utility catalog and its matching native configuration, then
retains that launch identity. It has no durable idle-wake capability: the parent
must remain active. This does not reconfigure an existing watcher, operation or
team member. An unmanaged caller still needs an explicit applicable caller/site
lineup. If the managed policy or native capacity is unavailable, use the visible
parent-monitoring fallback; do not search store paths by digest, infer a lineup
or silently substitute a model. Explicit user directions retain precedence.

Native spawn plus operation attachment could be smaller in launch code. The
pinned schema supplies parent provenance, but no supported adoption verifier or
live retention/recovery proof exists. It would require exact native parent/source
and spawn-record matching, not an asserted child ID. Keep it as an alternative
for a separately bounded proof; it is not a prerequisite or additional task here.

For lead delivery, use the configured workspace client and its shared persistent
submission ledger: `ReconcileSendWithOptions` and `SendWithOptions`
(`codex-web/codex/client.go:5193–5432`). Reuse the readiness and immutable-delivery
pattern in `portal/internal/communication/{native.go:97–155,service.go:264–372}`.
Extract only a small common helper if useful; do not route through pair grants or
change cross-session authority.

Do not copy the coordination outbox's retry policy: it intentionally changes
message IDs after failures (`libexec/workspace-coordination.rb:961–965`) and
restores held events on revival. Do not treat a native queue row or browser
notification as activation. Cold queues stay unloaded; automatic delivery must
not call a recovery wrapper that grants execution permission to held work.

## Operation, source and outcome contract

One new `monitor_operation` MCP tool has `start`, `report`, `status`, `cancel` and `resolve`
actions. `start` accepts an authorized monitoring brief from the exact current
lead. `report` accepts a structured event from the registered utility.
`status` exposes launch, outcome and delivery separately;
`cancel` revokes pending continuation for that exact operation. `resolve` records
lead-owned evidence that external effects were reconciled, without changing the
original outcome or running a command. Initial
scope is lead-owned asynchronous monitoring; member/native-only monitoring keeps
its active-parent workflow. No caller may select a destination session or thread
in a report, substitute a roster identity, or send arbitrary team messages.

The runtime stores a versioned private operation record, under its existing
state root, with atomic locked writes. Keep it separate from manifests, rosters,
cross-session grants and the submission database schema.

| Identity or field | Contract |
| --- | --- |
| `operation_id` / start request ID | Stable opaque UUID, allocated or admitted before launch; same start ID plus changed brief refuses; retries recover the same operation |
| Owner | Canonical workspace, session slug, retained session incarnation, exact lead thread and originating lead turn; slug/cwd alone are insufficient |
| Execution binding | Native socket path and verified socket epoch, runtime authority/package contract, selected provider, utility project/thread and launch submission/turn receipt |
| Utility policy | New operation snapshots selected package/catalog/model/effort/instructions/effective execution policy; retries retain it, never copy it into lead settings |
| Source/run | For local work: exact argv/cwd, declared nonsecret input/environment references, tested revision/input identity, and a runtime invocation UUID; for CI: canonical repository/provider, workflow/run ID, run attempt and tested commit |
| Attempt | Exact command invocation or CI attempt, distinct from notification delivery attempts; reruns are new operations and never silently replace this field |
| Event | Stable ID and slot (`escalation` or `terminal`), operation/source/run/attempt binding, outcome, timestamp, elapsed time, exit status/CI conclusion, bounded evidence references and any still-running command |
| Delivery | Immutable rendered envelope, context `monitor:<operation>:<event>`, stable native message ID, original turn options, state and native receipt; these survive retries unchanged |

Persist the operation/outcome before acknowledging the corresponding call.
`monitor.report` derives native caller thread from trusted MCP metadata and
resolves exactly one registered utility; tool arguments cannot grant ownership.
The new tool may share the daemon-start MCP transport, but not `ResolveReporter`.
The start tool similarly derives and revalidates the exact live lead. This also
works for Solo without manufacturing a team. Revalidate under existing session
admission and the operation lock immediately before mutation.

An event may report `passed`, `failed`, or `incomplete`. A terminal pass/failure
requires the exact run's authoritative exit status/conclusion. An escalation
reports `incomplete` plus its reason and still-running ownership; it does not
mean the command finished. Allow at most one escalation and one terminal event
per operation. Duplicate same-slot identical reports return the original event;
conflicting reports refuse. Further information is read through status/evidence,
not automatic repeated wake-ups. A CI rerun or a new command needs a fresh operation.

Managed monitoring is one-way: there is no lead-to-utility reply/reassignment
action. After escalation, retain ownership of the exact run and continue only
the originally authorized observation and cancellation conditions until
authoritative terminal evidence. Do not wait for later guidance or infer new
command, retry or cancellation authority from the escalation. If the original
scope cannot continue, record terminal incomplete with exact still-running or
unknown effects; do not leave the operation silently unaccounted for. Native-only
fallback may still use its ordinary active-parent communication channel.

Observe the registered utility's exact native turn for failure/termination. If it
ends without a durable report, record one incomplete terminal event, never infer
test success from a completed model turn. A disconnected/unknown utility remains
unknown until authoritative reconciliation; elapsed silence alone is not failure.
Late reports cannot overwrite a terminal incomplete result. They remain evidence
for lead reconciliation. Any still-running or uncertain external command remains
explicitly owned and must not be killed, repeated or declared finished by this
notification mechanism.

## Delivery and recovery invariants

Operation state and delivery state are separate. A finished check can have a held
notification. Delivery states are `pending`, `held`, `submitting`, `accepted`, and
`canceled`; a persisted native queue receipt remains pending activation evidence,
not an assertion that the lead started. Status records the actual turn ID and
whether a start or steer was observed when available.

1. Save the exact event/envelope, one native ID and first-send options before
   submission. Reconcile an existing submission before any send. A transport
   retry does not allocate a new event, native ID, utility or command attempt.
2. Before new dispatch, hold ordinary session admission and check current
   incarnation/root, lifecycle exclusion, ready runtime authority/socket epoch,
   provider admission and execution permission. Use the current lead settings
   for first preparation, then retain those exact options for recovery. Busy
   steering preserves the active turn and uses `expectedTurnId`.
3. An eligible idle lead gets a real `turn/start`; a busy lead gets `turn/steer`.
   Pending user input/approval, provider pause, uncertain activity or execution
   hold delays delivery. A stopped session is held until ordinary explicit resume;
   idle is not stopped. The worker never grants execution permission itself.
4. Portal-only restart on the same socket epoch may continue eligible deliveries.
   Native daemon restart/lost execution authority holds them. Reconcile exact
   utility/run state; never respawn, restart the utility turn or rerun commands
   automatically. A persisted outcome may deliver after ordinary user-authorized
   lead activation in the new epoch; prepare unsent events only then. Unknown old
   submissions reconcile their original identity. A utility lacking an outcome
   needs explicit evidence recovery, not inferred completion. Preserve origin
   epoch and record delivery's admitted epoch separately.
5. Cancel/revoke or archive/delete/owner replacement cancels unsent continuation
   permanently for that operation. Revival, forks and reused slugs do not revive
   it. Operation cancellation is not permission to kill an external command;
   command interruption requires the original brief's exact cancellation scope.
6. For a possibly submitted event, reconcile the original receipt even after
   cancellation or ownership loss, without sending again. An already accepted
   steer/turn cannot be recalled. Unknown outcome stays visible and unresolved;
   missing history is not proof of non-delivery. Definitely-unsent transport
   failures may retry the same request under valid admission.
7. Run a bounded background reconciliation worker with interruptible waits and
   no browser dependency. Retry observation/transport, not completed events or
   commands. Delivery failure becomes status attention, never another wake event
   about the failed wake event. An exact preparation positively proved unsent
   after a typed refusal may be retired under current admission so a later scan
   recomputes start/steer for the same immutable message, as specified below.
   Submitting, accepted, queued or uncertain attempts remain reconcile-only.

The submission ledger suppresses duplicate managed input, not arbitrary external
effects or all native writers. Native `turn/start` lacks atomic compare-and-start;
an unmanaged concurrent writer can change scheduling. Preserve this existing
limit rather than claiming global exactly-once execution.

## Implementation packages and file boundaries

The lead assigns the following retained members and serializes shared entry-point
edits/Git operations. Contract changes return through architect and lead before
dependent work proceeds. A owns shared Go type/store definitions; other owners
must not change their shape unilaterally. D's native-only wording correction is
independent and has already been released by the lead.

| Package | Files and boundary | Dependencies / acceptance |
| --- | --- | --- |
| A / implementer0: authority and launch | `portal/internal/monitoroperation/{types,store,service,authority,launch}.go` and tests; new `agentteams/utility.go` and tests | Stable types/store, one utility launch/recovery, correct policy, same-epoch permission, run/event immutability and persistence; no roster writes |
| B / implementer2: delivery | `monitoroperation/{delivery,native}.go` and tests; `portal/internal/web/{monitor.go,monitor_test.go}`; coordinated worker-start hook in `server.go` | Depends on A types/store; owns DeliveryService, NativeDelivery, missing-report observation and worker. Same-ID start/steer, holds/cancel/unknown and restart; no communication/coordinator edits |
| C / implementer1: entry points and compatibility | New `cmd/workspace-portal/{monitor.go,monitor_mcp.go}` and tests; narrow wiring in main/team_mcp/codex_provider, libexec dev-session/workspace-host, agentteams registration, runtime-contract, teamruntime observation/lifecycle; `monitoroperation/lifecycle.go` as needed | Depends on A API/inventory; native caller, selected-profile dispatch, complete lifecycle/provider/package inventory including Solo; preserve startup 1/2 and add policy 3 |
| D / implementer3: acceptance and guidance | New `cmd/workspace-portal/monitor_native_integration_test.go`; generic monitor skill, session guide and portal contract; consuming verification instructions in workspace feature checkout | Independent limitation wording released. Runtime docs/native test depend on A–C; reuse synthetic Responses/native fixtures with real dispatcher/receipts |

Keep new behavior primarily in generic dev-workspace. No demonstrated codex-web
API/schema change or vpsFree extension source change is necessary. Workspace
instruction alignment is a separate repository change. Concrete wiring follows;
this brief does not authorize broad lifecycle refactoring. Runtime-owned
utility threads must enter ordinary ownership inventories so they cannot bypass
existing quiescence checks. Completion retains records/history; it does not
archive, delete, stop or clean the session or utility automatically.

## Stable interfaces and release order

`monitoroperation` may depend on `session`, `agentteams`, `workspacecodex` and
`codex`, but not `teamruntime`, `communication` or `web`: C must import it from
teamruntime. Supply prepared lead policy through a callback. B follows the
communication readiness contract with a small local adapter; do not extract a
generic delivery framework or introduce an import cycle.

A owns these public seams. Implementers agree representation adjustments before
dependent source begins; semantic changes return through architect/lead:

```go
NewStore(stateRoot, workspace string) (*Store, error)
(*Store).Get(ctx context.Context, operationID string) (Operation, error)
(*Store).List(ctx context.Context, slug string) ([]Operation, error)
(*Store).ResolveReporter(ctx context.Context, threadID string) (Operation, error)
(*Store).Lock(ctx context.Context, operationID string) (*Transaction, error)
// Transaction exposes Operation *Operation, Save() error, Close() error.
// Save persists immediately; closing never implicitly commits.
(*Service).Start(ctx context.Context, callerThread string, req StartRequest) (Operation, error)
(*Service).Report(ctx context.Context, callerThread string, req ReportRequest) (Operation, error)
(*Service).Status(ctx context.Context, callerThread, operationID string) (Operation, error)
(*Service).Cancel(ctx context.Context, callerThread, operationID string) (Operation, error)
(*Service).ResolveEffects(ctx context.Context, callerThread, operationID string, req ResolutionRequest) (Operation, error)
(*Store).Inventory(ctx context.Context, slug, rootThread string) (Inventory, error)
(*DeliveryService).Pending(ctx context.Context) ([]EventRef, error)
(*DeliveryService).Dispatch(ctx context.Context, operationID, eventID string) error
(*DeliveryService).Observe(ctx context.Context, operationID string) error
```

`Service` owns start/report/cancel/resolve with injected launch/authority dependencies.
B owns `DeliveryService{Store, Resolve, LockSession, Transport}`: Resolve returns
current owner, LockSession takes ordinary runtime SH, and Transport provides
`Ready(ctx, Owner) (string,error)`, `Prepare(ctx, Owner) (codex.TurnOptions,error)`,
and `Send/Reconcile` for a saved Event. B can add a narrow exact-turn observer
dependency. C constructs production dependencies at the CLI/server boundary.

`Operation` contains ID, Owner, immutable Source/Brief/UtilityPolicy, Launch,
Events, CanceledAt, optional Resolution and lifecycle disposition. Owner contains Slug, RootThreadID,
Incarnation, Socket and origin SocketEpoch; Store fixes canonical workspace.
Launch retains project/thread, creation/bootstrap attempted flags and marker,
exact brief send ID/options/receipt and state. Event contains ID, slot, outcome,
evidence and Delivery. Delivery contains Status, MessageID, Envelope, Context,
Options (*codex.TurnOptions), Receipt (*codex.SendReceipt), admitted epoch and
diagnostic detail. A reserves these for B, with one delivery record per event.
A publishes the concrete field names/types in types.go before B/C depend on them.

Use private schema-1 operation files under
`monitor-operations/<workspace-sha256>/`; UUID/32-hex IDs are not paths. Validate
owner/slug and uniqueness. A short workspace admission lock reserves per-session
maximum concurrency and stable start IDs; never hold it over RPC. Each operation
has its own interruptible transaction lock. Lock order: runtime/session SH,
optional existing team operation fence for lifecycle, operation transaction,
existing client submission/recovery locks. Never acquire runtime/team locks
inside a store transaction. Snapshot reads must be revalidated before mutation.
Malformed or ambiguous state refuses, rather than becoming an empty inventory.

StartRequest has stable ID (= operation ID), bounded exact brief, Source and
cancellation scope. Source is local exact argv/cwd, input/revision identity and
invocation ID (= operation ID), or CI repository, workflow/run ID, positive run
attempt and commit. Keep secret values out. ReportRequest has slot, outcome,
exit status/conclusion, elapsed time, bounded evidence and still-running identity.
Native caller selects the registered operation; reports cannot choose another
operation/recipient. Derive stable event/message ID from operation + slot;
identical same-slot reports return the original acknowledgement, changed content
refuses. Status/cancel selects an operation only for its current exact lead;
utility status resolves only its own operation. Cancel revokes continuation, not
command execution. Only proved native termination releases live-watcher capacity,
not receipt of a final report.

Inventory returns exact owned threads (operation/project/thread/cwd/settings,
retirement disposition), unresolved launch/receipt and activity blockers. C uses
it for ownership, not caller authorization. Terminal incomplete external work
remains visible; it does not itself prove a live native utility. Actual native
quiescence is checked separately. Unknown launch is never deleted/recycled or
replaced automatically.

The lead approved one necessary recovery action on 2026-11-03. `resolve` takes the
same operation ID, a stable resolution ID, bounded nonempty evidence references
and detail. It is current-exact-lead-only. Under ordinary admission and the
operation lock, prove native utility quiescence and known launch/submission
outcomes, then save one immutable Resolution (ID, time, lead thread, evidence,
detail). An identical retry returns it; conflicting resolution refuses. Retain
original Source, run/attempt, events and receipts unchanged. Revoke remaining
unsent continuation; never create a wake event, retry/kill a command or infer
completion from silence. This records the owner's evidence acknowledgement, not
a rewritten passing test result. It clears only the external-effects fence;
unknown launch/submission or active native execution still refuses. A owns the
type/service/transition validation; C supplies the native quiescence check and
tool/CLI adapter. Terminal-incomplete or latest still-running evidence requires
resolution before retirement. Historical escalation is superseded by an
authoritative terminal completion and must not permanently block lifecycle.
Test owner/active/unknown refusals, same-ID retry, preserved original outcome,
absence of wake/command side effects, and retirement after exact proofs.

Cancellation cannot disable recovery of original native effects. Status/resolve
may perform bounded observation and reconciliation of the original unique
project/thread, bootstrap marker and launch/delivery receipts, persisting proved
facts under the same operation lock. After cancellation this path must never
create a project/thread, bootstrap, send, resume, replace an ID or repeat a
command. A canceled same-start retry may return reconciled state only. Unproved
absence remains unknown; owner evidence cannot override unknown native effects.
Test cancellation before a lost launch/report acknowledgement and successful
later discovery of its original receipt without any second mutation.

Preflight utility/effect readiness before creating a lifecycle journal or
quiescing the root where the existing procedure permits. If an operation journal
already exists, retain a narrow exact-owner status/resolve path for metadata and
receipt reconciliation under its original session lock. It grants no native
execution or delivery; ordinary starts and sends still honor the lifecycle
fence. C must bind this recovery to the original session/root/incarnation and
journal, rather than bypass pending-lifecycle checks generically. This prevents
the refusal itself from blocking the only supported way to resolve its evidence.

### Launch policy and execution permission (A/C)

A adds `agentteams.VerificationWatcherInstructions(packageRoot, catalog)`: read
the validated generated utility TOML's JSON-string developer_instructions and
verify native identity/digest. Do not duplicate its literal policy, add a TOML
dependency or change catalog schema. New operations construct a validated
CatalogPin from the selected installed package and verify it through LoadPinned;
save exact package path, digest, model/effort/instructions and effective execution
policy in the operation and start acknowledgement. Recovery uses that frozen
operation snapshot, not a newly selected default. Direct-session rosters retain
catalog digests but no resolvable original utility package pin; do not search the
store by digest or migrate the roster. The lead accepted this clarification on
2026-11-03. The exact brief adds source/report instructions without changing
retained team settings or an existing operation's model/effort.

Create, bootstrap and send using the underlying configured `*codex.Client`
(`workspacecodex.Client.Client`), preserving its provider resolver and shared
SQLite submission ledger. Deliberately omit utility automatic-turn-retry
enrollment; do not broaden RetryPolicyResolver to utilities. Persist CreateAttempted
before thread/start; after uncertainty adopt only the unique exact project
thread. Persist BootstrapAttempted/marker before BootstrapHeadlessThread and use
VerifyHeadlessBootstrap on retry. Missing/ambiguous evidence stays unresolved.

Before its brief can run, the utility binding is durable. Under session admission,
an A-owned activation callback adds only that utility to existing
RecoveryStore.ActiveThreads, requiring the root already Active at the exact
unchanged origin socket epoch and preserving all other threads. This makes the
existing ThreadOwner/implicit-resume checks work without a new recovery format
or lead activation. Partial launch failure reconciles the same operation. A new
epoch never re-enrolls/restarts the utility automatically.

### Concrete C wiring and lifecycle policy

- Add monitor_operation to team_mcp.go tools/list/dispatch, with adapter in
  monitor_mcp.go. Derive native _meta.threadId first. Mirror communication.go and
  libexec/dev-session#communication/run_communication for stable-profile
  `monitor --request-stdin`, carrying a distinct expected native caller instead
  of member authority. Ruby verifies package/lifecycle/root under the session
  lock; Go rechecks caller. Legacy bound team helpers keep their old report path.
- agentteams/registration.go:WithWorkspaceReporting adds the tool and approval
  entry. Runtime contract adds workspaceReportingPolicy=3,
  monitorOperationStateSchema=1 and monitorOperationPolicy=1. Host
  reporting_startup_contract?/valid_reporting_registration_argv? validate exact
  policy 1/2/3 shapes (10/12/14 argv elements). A changed tool set takes ordinary
  idle daemon cutover; an old running helper is not a monitor capability.
- workspace-host#require_compatible_session_recovery! checks monitor capability
  whenever operation state exists, including malformed state.
  require_compatible_session_communication! accepts reporting 2 or 3 with
  communication policy 1. Preserve forward-only recovery and exact old startup
  proof; a changed number alone cannot bless an unknown invocation.
- dev-session#quiesce_and_require_idle! checks monitor inventory for ordinary stop
  and package require-execution-idle; ensure_archive_conversations_ready! includes
  it for automatic/merged archive. Do not skip Solo when sync_team_lifecycle!
  has no roster. Active or uncertain utility execution refuses before successful
  quiescence is claimed.
- Explicit archive/delete retains its existing journal owner. Revoke unsent
  events and retain uncertain receipts before destructive effects. Require exact
  utility native quiescence, known launch/submission outcomes and resolved
  external effects before archiving its proved thread; persist archiving/archived
  disposition for retries. CancellationScope prose never grants interruption
  authority, even through QuiesceExplicitArchive. Wire quiesce_explicit_archive!,
  archive-retained completion and delete prepare-delete/retire. Refuse unresolved
  work with the supported resolve path above. Revival never restarts these
  utilities/events. Ordinary stop holds pending notifications; package transitions
  retain them under the existing admission contract. Only archive/delete and
  explicit cancel/resolve revoke unsent continuation. No broad forced cleanup.
- codex_provider.go:providerThreads includes proven utility project/thread and
  retained settings before native loaded-thread comparison; active/uncertain
  utilities block provider transitions. teamruntime retained observation and
  RequireExactActiveConversations expected sets include the same owned inventory
  with honest utility subjects. Inventory stays separate from roster membership.

B adds Server.startMonitorOperations beside startCommunication, using
operationContext/operationWG, current-generation admission, bounded batches and
interruptible timeouts. No new service, browser poller or scheduler. Lead Prepare
options come from C/server construction using current settings and retained lead
instructions. Utility observation uses cold metadata/turn reads and never loads
a missing utility. A receipt with only QueuedSubmissionID is not an activated
lead: retain pending activation evidence. A known-unsent prepared start/steer
mismatch uses the bounded admission repair below, retaining its original
ID/options/body/context. Unknown submissions never enter that repair.

Release order: after lead acceptance, A may implement types/store/launch and C
may independently implement startup policy/registration/compatibility checks.
A publishes types.go before B dependent source or C lifecycle/MCP code begins.
D's wording correction is independent; its native fixture follows a compiling
MCP/CLI construction. No placeholder authority/lifecycle checks to make incomplete
work appear ready. Quick fixtures develop with each package; long native tests
remain after committed quick checks and mandatory final independent review.

### Monitor-only repair of a known-unsent routing choice

The lead accepted this correction to the earlier held-race assumption. A lead
can finish between selection of `turn/steer` and native admission. A definitive
no-active-turn refusal restores the SDK attempt to `prepared` with its original
`Steered=true`; a later idle send then refuses that routing mismatch indefinitely.
This loses outcome liveness within the supported wake-up goal. Repair only the
positively proved unsent preparation, never the operation or message identity.

Existing codex-web `d3a29bee90ef00a08816920408c596152339a637` APIs suffice:

- `ReconcileSendWithOptions(ctx, thread, text, id, action, options)` returns an
  accepted receipt, reconciles a submitting attempt, or returns unknown when
  submitting history is absent. Prepared and absent return no receipt. That
  last result alone cannot authorize discarding anything.
- `IsPreparedSendWithOptions(thread, text, id, action, options) (bool, error)`
  proves the exact digest/context/options match, `prepared` state and no queue
  attempt. Absence is false; mismatch is an error (`codex/client.go:5469–5496`).
- `DiscardPreparedSendWithOptions` has the same arguments/result and rechecks
  exact identity/state under its own thread lock and durable transaction. It
  refuses submitting, accepted or queued attempts. It also returns true for
  absence, so that return is never sufficient proof by itself
  (`codex/client.go:5146–5179`).

B owns generic `portal/internal/monitoroperation/native.go`, `delivery.go` and
their focused tests. Extend only `DeliveryClient` with these two option-aware
proof/discard methods; the configured `workspacecodex.Client` already promotes
them and `web.monitorDeliveryClient` retains them through its embedded interface.
`DeliveryTransport`, operation schema, worker scheduling and public MCP/CLI stay
unchanged. No codex-web change, new generic retry API or dependency update is
needed. Do not bypass configured send/admission with the raw native client.

`NativeDelivery.Send`, called by ordinary `Dispatch` under existing session and
operation locks, performs this finite sequence:

1. Run the normal configured `SendWithOptions` with the saved owner/root and
   exact event message ID, envelope, context and options. Success/receipt or
   `UnknownSendOutcomeError` cannot enter repair. Unknown takes precedence even
   if an error chain also contains `MessageNotSentError`.
2. Only a typed `MessageNotSentError` permits asking for the exact prepared proof.
   No error-string matching, history-absence inference or `Retryable`-flag
   substitution is an authority. The public proof exposes no saved steer bit;
   the supported policy is repair of a proved unsent monitor input, not a
   fragile match for one native refusal string. A false proof grants no discard.
3. With positive proof, recheck `Ready` for that exact owner/socket epoch while
   the current uncanceled/nonrevoked operation and owner remain protected by
   existing session/operation admission. A changed epoch, provider/user wait,
   stopped runtime or unavailable readiness leaves the preparation untouched.
   This check grants no execution permission or settings change.
4. Call exact option-aware discard once. Its transactional recheck must win over
   the earlier observation: false or error cannot become a successful repair.
   Proof errors and ambiguous discard/storage failures remain unconfirmed for
   reconciliation. `Dispatch` must prioritize Unknown over NotSent so wrapping
   an original unsent error cannot downgrade new uncertainty to a held retry.
5. After successful retirement, return the original unsent outcome and persist
   held status. Do not prepare or send again inline. A later existing bounded
   scan repeats current owner/revocation/readiness admission and the normal
   configured send, which reserves the same immutable tuple with current
   start/steer routing. It may hold again if saved policy is no longer admitted.

Cancellation/retirement and normal sends share the existing operation fence;
read-only status/resolve reconciliation never invokes this repair. A cancellation
after repair prevents the next scan from sending. An accepted/uncertain native
attempt is still reconciled after revocation and never discarded. The two SDK
calls use separate transactions; discard rechecks an intervening writer's state.
Cooperating monitor senders are serialized by the operation lock. This adds no
guarantee against an unmanaged writer reusing the same message ID.

Crash boundaries retain the existing schema and recovery contract. Before
discard, the original prepared attempt survives and can be proved again. After
committed discard but before the held-status save, the operation can still say
`submitting`, with its complete original envelope/options and an absent SDK row;
no replacement native call has occurred. On recovery, ordinary SDK reconciliation
and fresh admission may submit that saved event: this is the existing
ledger-before-network path, not an absence-based permission to discard or reset
an unknown attempt. After new preparation, its exact tuple survives. After its
submission claim, missing history stays unknown; after acceptance, the same
receipt wins. A failed/ambiguous durable write is never treated as successful
retirement. Existing held events become eligible for this bounded repair without
migration; existing queued/submitting/accepted evidence keeps its interpretation.
Older code can still load the unchanged records, although it retains the liveness
defect. Existing package-transition and forward-recovery restrictions still apply.

Fast acceptance uses the real SDK/configured adapter and disposable ledger/RPC
fixtures: make a selected active turn end before steering, return the definitive
native-shaped refusal, prove the exact prepared entry, repair once, then on a
later Dispatch accept idle `turn/start` with the same ID/body/context/options.
Assert one accepted input, no inline second send, preserved managed snapshot and
deduplication after restart. Include crash after discard before held save; current
Ready hold/cancel/revoke between scans; absent proof, tuple mismatch, proof/storage
errors, queued input, changed-to-submitting/accepted at discard, and unknown with
absent history. Negative controls must show no discard/replay and preserve the
original accepted receipt or unresolved status. Test Unknown precedence for
wrapped/joined errors. These fixtures do not count as actual native race evidence.

D owns the separate tagged native regression in
`portal/cmd/workspace-portal/monitor_native_integration_test.go` and the smallest
needed addition beside the existing `turn_retry_native_proxy_test.go` forwarding
helper. A one-shot transparent barrier can intercept only the exact monitor
event/root `turn/steer`, release the already-held real lead backend, and observe
that exact expected turn completed plus native thread status idle through a
separate passive client to the private native socket. This pre-forward barrier
reads only native identity/turn/status; it must not invoke the full idle proof
or wait for submission-ledger settlement, because the original steer is
deliberately still pending. Then forward the unchanged original frame and
preserve the actual native refusal. A later ordinary worker pass must yield
a real same-ID idle start receipt and exactly one history input. Do not fabricate
a refusal/receipt, hide history, reuse the receipt-rewriting behavior for this
case, or block a delivery-observer callback. Require final full native/ledger
idle proof after the request and continuation settle. Failure to obtain the
real refusal fails the fixture. Keep the existing item/case deadlines and owned teardown;
add no timeout extension or test framework. Preserve the initial idle barrier,
source/run/outcome identity, R1–R4 closures and trusted code-cell contract.

Release is through lead acceptance of this saved brief. B's production/unit
package precedes D's dependent native regression, with shared test edits and Git
serialized by the lead/A. Long checks remain stopped until intended changes are
committed, quick checks pass, and the affected final independent review accepts
the production repair and revised test assumptions. This brief authorizes no
native execution, build, push, CI, deployment, integration or lifecycle action.

## Compatibility, deployment and recovery implications

Existing roster, session manifest, lifecycle journal, cross-session grants and
submission-store formats stay unchanged. Add one versioned operation-state
contract and its package capability; absence means the current native-wait
fallback. Old native-only watchers are not adopted retrospectively. An updated
skill cannot wake a lead that already ended its turn.

The candidate must preserve existing operation/outcome/receipt records across
compatible portal restarts and forward package selection. Unsupported readers
must refuse before admitting new operations or consuming new records. If a
package lacks the new contract, it cannot silently replace a capable runtime
with outstanding operation/uncertain-delivery obligations. Add the minimum
capability/preflight fence needed in existing package transition machinery.
Do not call additive JSON fields alone rollback compatibility.

The selected runtime's package recovery is forward-only; ordinary rollback to
an older package already refuses. Recover by selecting the same or a newer
compatible package and reconciling exact receipts. Preserve older lifecycle
journals and recovery commands. A future downgrade would need a separately
designed drain/export contract; it is not part of this fix.

MCP startup policy changes may require an idle native-daemon cutover even if the
native binary stays unchanged. Decide this from the final complete invocation,
not from package version. Build, quick-check, independently review and run native
acceptance before selecting a package. The deployment authorization recorded in
the rollout brief below now applies, with ordinary machine coordination and
exact source/input/profile receipts. This design records no live activation.
The application change requires no infrastructure node/schema/API/client/Terraform
coordination; rollout also includes the matching aitherdev host-input pin below.

## Verification brief and completion gate

Quick deterministic checks use repository Nix environments, existing fixtures,
disposable state and sockets. Extend tests to cover A–C contracts: exact caller
and owner rejection, changed run/attempt/payload refusal, one launch after lost
ack, success/failure/incomplete outcomes, identical duplicate events, real client
RPC start/steer shape, current settings preservation, persistence, unknown-send
reconciliation, cancellation races, provider/user waits, stopped/runtime-held
sessions, new epochs and lifecycle exclusion. Retain ordinary member-report and
session-communication regressions. Syntax/format/document-link checks apply to
guidance. Never point fixtures at this or a peer's registered runtime.

After intended implementation commits, passing quick checks and mandatory final
independent review, a fresh Luna/low utility runs the longer packaged/native
batch against isolated runtime state with the exact candidate native binary.
Use a deterministic synthetic model backend where needed, while retaining the
real App Server and runtime path. Do not use a fake lead dispatcher or receipt.

Required end-to-end cases:

- Launch through the proposed runtime path, prove the lead turn ended and is
  idle, then complete each of success, failure and escalation. Observe an actual
  lead `turn/started` (or authoritative history after reconnect), exact event
  input and matching durable native receipt, without browser/user prompting.
- While the lead is busy, prove the exact active turn is steered and its saved
  model/effort/mode/instructions remain intact. Re-report/restart and prove no
  second input for the same event; escalation followed by terminal is two
  intentionally distinct events.
- Exercise report accepted before lost acknowledgement, delivery accepted before
  lost reply, portal restart, socket disconnection and native restart. Prove
  reconciliation, explicit activation holds, and no second watcher/command launch.
- Exercise cancel before send, cancel during uncertain send, stopped session,
  user/approval wait, provider pause, archived/revoked/replaced owner and wrong
  utility/session/run attempt. Prove no unauthorized activation or revival replay.
- Include cancellation after thread creation but before bootstrap. Native fresh
  metadata may omit projectId: require the original durable project/thread binding
  plus the existing exact fresh-thread proof, not generic id/cwd adoption.
  Retirement uses ArchiveThread and exact archived proof only. If the pinned
  native runtime cannot archive that unmaterialized thread, preserve refused or
  archiving recovery and report the limitation; do not delete/recycle/recreate it.
  Do not claim all fresh-cancellation retirement is supported without this proof.
- Prove existing retained-member reports still work and no roster/settings change
  occurs. Verify a utility ending without reporting wakes the eligible lead once
  with incomplete status and preserves any still-running/unknown external work.

Keep batches bounded to these risks; inspect failures before adding work. A test
log, native message, stored event, queued input or fabricated receipt alone is
insufficient. Native-live idle activation is the remaining acceptance gate, not
an established result of this diagnosis. Implementation is now assigned through
the lead; this evidence boundary remains until native acceptance passes.

### Pinned native fixture adapter (2026-11-04)

The E1a probe established a fixture protocol mismatch: the root gpt5.5 request
advertised 13 top-level tools, while gpt-6-luna omitted that field. It did not
establish utility command execution, report delivery or wake-up acceptance.
The pinned official Codex 0.165.0 source is commit
`360319d8dee62d87e2d59fc0c21805d79519cfed`. Its ordinary Luna policy uses
Responses Lite and CodeModeOnly. Lite places the tools in developer
`input` items of type `additional_tools`; CodeModeOnly exposes the executor and
hides its nested functions from the direct tool list. The naming-only derived
direct/non-Lite catalog is not this runtime policy and must not be substituted.
See [request construction](https://github.com/openai/codex/blob/360319d8dee62d87e2d59fc0c21805d79519cfed/codex-rs/core/src/client.rs#L1016),
[Lite namespaces](https://github.com/openai/codex/blob/360319d8dee62d87e2d59fc0c21805d79519cfed/codex-rs/tools/src/tool_spec.rs#L95)
and [tool visibility](https://github.com/openai/codex/blob/360319d8dee62d87e2d59fc0c21805d79519cfed/codex-rs/core/src/tools/spec_plan.rs#L853).

D owns the bounded correction in generic
`portal/cmd/workspace-portal/monitor_native_integration_test.go`, including its
small pure helper tests. Minimal test-guidance rationale may accompany it if
useful. No production, codex-web dependency, model, catalog, settings or package
changes are part of this correction. Preserve the existing ten case scenarios;
do not add a general protocol framework or scheduler. The adapter contract is:

- For initial advertisement, read the actual top-level `tools` array and developer `additional_tools`
  input items, traversing their declared namespaces. Validate direct function
  schemas and the advertised outer custom executor's pinned grammar shape;
  reject malformed, conflicting, ambiguous or missing required capabilities.
  Do not infer available tools from model names, shell metadata or arbitrary
  description text. Retain bounded schema diagnostics without raw prompt data.
- For the observed Lite shape, select advertised namespace `functions`, custom
  tool `exec`, grammar/lark, and emit `custom_tool_call` with exact `call_id`,
  `name`, advertised `namespace` and raw JavaScript `input`. Do not put the code
  in function-call JSON arguments. Follow the pinned upstream
  [custom-call SSE helper](https://github.com/openai/codex/blob/360319d8dee62d87e2d59fc0c21805d79519cfed/codex-rs/core/tests/common/responses.rs#L1029)
  and [executor specification](https://github.com/openai/codex/blob/360319d8dee62d87e2d59fc0c21805d79519cfed/codex-rs/core/src/tools/code_mode/execute_spec.rs#L5).
  Keep the existing direct-function route only when its actual advertisement
  validates; do not inject a direct MCP call into a CodeModeOnly utility turn.
- Nested calls use the pinned API: `tools.exec_command({cmd, workdir})` for the
  existing short recorder/observation command, and
  `tools.mcp__team_reporting__monitor_operation(args)` for the unchanged candidate
  MCP request. Shell registration uses `exec_command` even when model metadata
  says `shell_command`; see [registration](https://github.com/openai/codex/blob/360319d8dee62d87e2d59fc0c21805d79519cfed/codex-rs/core/src/tools/spec_plan.rs#L1242),
  [shell schema](https://github.com/openai/codex/blob/360319d8dee62d87e2d59fc0c21805d79519cfed/codex-rs/core/src/tools/handlers/shell_spec.rs#L19)
  and [nested name mapping](https://github.com/openai/codex/blob/360319d8dee62d87e2d59fc0c21805d79519cfed/codex-rs/tools/src/code_mode.rs#L265).
  Each cell first requires the exact nested identity in actual `ALL_TOOLS` and
  a callable matching `tools` property, then awaits the real call and emits its
  returned value or a compact validated projection through `text`. For MCP,
  require a successful actual CallToolResult, parse its Operation text, verify
  the exact operation ID/schema, and copy only the needed launch/report identity
  fields into a marked acknowledgement. Do not print the full retained utility
  instructions or synthesize receipt fields; durable/native receipt assertions
  remain authoritative. Shell projections retain actual exit/session/output
  fields and terminal validation. Parse the marker only in the exact correlated
  native output, without treating it alone as success evidence.
  Serialize fixture arguments as JSON data; never
  interpolate command or report content into executable JavaScript text.
- Strict validation has two distinct authorities. The fixture validates raw
  direct/outer advertisements and its finite pinned argument shapes. The native
  registry validates the real nested invocation. CodeModeOnly renders nested
  declarations into descriptions/metadata and clears raw nested schemas; the
  wire does not offer an independent JSON-schema proof for them. Do not invent
  that proof, parse arbitrary TypeScript or create synthetic tool definitions.
  [Definition preparation](https://github.com/openai/codex/blob/360319d8dee62d87e2d59fc0c21805d79519cfed/codex-rs/core/src/tools/code_mode/tool_definitions.rs#L24)
  and [native nested dispatch](https://github.com/openai/codex/blob/360319d8dee62d87e2d59fc0c21805d79519cfed/codex-rs/core/src/tools/code_mode/mod.rs#L393)
  retain the real session/turn tool path, including native MCP caller identity.
- Correlate the exact expected call ID and output type:
  `function_call_output` for direct calls, `custom_tool_call_output` for exec.
  Accept the pinned string/content-array output shapes with existing bounds.
  A completed script is not a successful shell command or MCP report: require
  its actual nested result, authoritative exit evidence and durable operation
  receipt. Reject script errors, termination, running-cell output, missing or
  still-running shell results, MCP errors and mismatched/stale output IDs.
  Preserve intentional failed-command exit status 7 as test evidence.
- Every code cell awaits one bounded call to completion. No unawaited promises,
  background/yielded cells, `yield_control`, wait-cell recovery or detached
  commands. A finite executor pragma may keep the call within the remaining
  existing 90-second case budget; it cannot extend that budget. The escalation
  process remains the exact fixture-owned process, with short native observation
  calls and the original run/PID/exit checks. Unexpected ongoing effects fail
  the case visibly and remain owned by the existing disposable-run teardown;
  neither an idle turn nor a successful assertion authorizes leaving them alive.

The root-only deferred-discovery refinement is authorized by the lead after the
later probe found no monitor definition in the root's 13 advertised tools, only
native client `tool_search`. Preserve the immediate direct path when the actual
candidate monitor definition/schema is already available. Otherwise, for the
initial root monitor start only:

1. Require one actual `type: tool_search` advertisement with `execution: client`
   and the pinned object parameters: required `query: string`, optional numeric
   `limit`, no unsupported required fields. Emit exactly one native
   `tool_search_call` with a separate stable `call_id`, `execution: client` and
   object `arguments: {"query":"monitor_operation"}`. Do not use a function call,
   encode arguments as a string, vary the query or retry discovery.
2. Await the real native input item `tool_search_output` for that exact call ID;
   require `status: completed`, `execution: client` and a bounded `tools` array
   of actual `LoadableToolSpec` function/namespace definitions. The pinned
   [constructor](https://github.com/openai/codex/blob/360319d8dee62d87e2d59fc0c21805d79519cfed/codex-rs/core/src/tools/context.rs#L284)
   and [protocol type](https://github.com/openai/codex/blob/360319d8dee62d87e2d59fc0c21805d79519cfed/codex-rs/protocol/src/models.rs#L872)
   both include `execution`; direct GitHub contents API verification identified
   blobs `c80a89ddd1fe2adb5a36b36016cdd5f4a3198b43` and
   `351f45c03c943fac9bc9d2f195a5b927fa844ba2`, respectively. Do not accept a guessed
   missing-field variant. The emitted call shape is defined by
   [ToolSearchCall](https://github.com/openai/codex/blob/360319d8dee62d87e2d59fc0c21805d79519cfed/codex-rs/protocol/src/models.rs#L1150);
   [search parameters](https://github.com/openai/codex/blob/360319d8dee62d87e2d59fc0c21805d79519cfed/codex-rs/core/src/tools/handlers/tool_search_spec.rs#L88)
   and [loadable definitions](https://github.com/openai/codex/blob/360319d8dee62d87e2d59fc0c21805d79519cfed/codex-rs/tools/src/responses_api.rs#L44)
   establish the remaining wire contract.
3. Select the exact candidate monitor namespace/name and validated schema from
   that real result, then emit the original unchanged start request. Reject
   absent, empty, ambiguous, malformed, conflicting or wrong-ID results without
   fabricating a definition, interpreting an alias or searching again. Keep
   discovery state separate from the pending MCP call: search output is not an
   operation-start acknowledgement and must not advance utility/report phases.

This adds one finite fixture stage, not a new production protocol or state.
The utility retains its source-supported `ALL_TOOLS`/callability guard; deferred
native tools are available in code mode, so no utility search stage is inferred.
Preserve initial-origin identity, the same 90-second case budget, completed/idle
barrier, command/source/run/report/receipt checks and failure ownership. D owns
the same one-file helpers and focused checks: immediate-direct versus one-search
flow, exact output correlation/schema, rejection paths, no repeated query and
no discovery-as-start acknowledgement. After D freezes passing quick checks,
the lead inspects and A handles Git. The committed dispatch change goes to the
same reviewer for affected general/architecture/scope/risk assessment before
native acceptance; reuse unchanged-path review and R1–R4 closures. This release
does not authorize native execution, builds, pushes, CI or lifecycle actions.

Reuse the bounded request projection/output handling style in codex-web's
`codex/ephemeral_integration_test.go` (`integrationToolDiagnostic`, around
2247–2346), plus the upstream custom-call SSE shape. Those diagnostic/rejection
helpers are not prior successful CodeModeOnly dispatch evidence;
`integrationToolNames` deliberately rejects AdditionalTools for a different
contract and must not become this adapter's acceptance policy.

Quick acceptance covers direct versus Lite projection, namespace/custom grammar
validation, missing/conflicting definitions, exact call/output correlation,
safe argument serialization and rejection of nonterminal/error outputs. Compile
the tagged fixture without executing native cases. D freezes the focused diff
and quick-check evidence; the lead commits and assigns the affected-lane
independent review before another native probe. That review must include the
boundary below. Native acceptance still requires the original completed **and**
idle lead barrier before releasing the utility, exact command/source/run/attempt,
real candidate MCP/CLI/worker delivery, actual new-turn or steering receipt,
duplicate/restart/cancel assertions and final scoped idle evidence. No fake
receipt or nested result may replace any of these assertions.

**Supported-boundary assessment for review.** Pinned
[execute_handler.rs](https://github.com/openai/codex/blob/360319d8dee62d87e2d59fc0c21805d79519cfed/codex-rs/core/src/tools/code_mode/execute_handler.rs#L141)
retains yielded cells beyond their initial response; the naming exclusion in
`docs/codex-package.md:162–164` records that cells can survive completed turns
without supported scoped stop/join. This is not a monitor guard. C confirmed at
generic `e1a2796ee30552a00c026013ecb318d77bd2d1ce` / codex-web
`d3a29bee90ef00a08816920408c596152339a637`: monitor
`lifecycle.go:66–178` delegates to `workspacecodex/archive_proof.go:217–250` and
`codex/client.go:4290–4343`, proving identity, thread/turn, prompts, queues and
submissions, not code-cell termination. `monitoroperation/service.go:245–258`
separately fences reported external effects; missing/incomplete or nonempty
`stillRunning` refuses, but a valid passed/failed terminal with empty
`stillRunning`, or an exact lead resolution, clears that fence. Observation in
`native.go:121–140` also proves only the original turn's termination. Therefore
an unreported surviving cell is not independently excluded by current retirement
preflight. Archive still requires its own actual native archive proof; its
behavior with such a cell has not been exercised here. This is a source-backed
conditional gap in the managed quiescence proof, not proof of live orphaned
effects. The non-yielding fixture establishes only its scoped calls. The committed
adapter review must assess the smallest necessary correction or a precise
residual supported boundary before long acceptance; it must not silently weaken
native-uncertainty fences or infer a new cell supervisor, catalog substitution
or unconditional permanent lifecycle refusal. No production correction is
authorized by this verification appendix.

## Aitherdev rollout and compatible source refresh

The user's new direction, “aitherdev can be deployed using
vpsfree-cz-configuration”, authorizes preparing and deploying this feature to
aitherdev through that repository. It does not authorize default-branch
integration, session lifecycle changes or forced interruption of conversations.
The selected installed coordination guide is the complete snapshot
`/tmp/lead-wakeup-deployment-guide-totmxyml.txt`, from package
`/nix/store/myjy32qh6bd4avgym1awx180y29nvwz9-dev-workspace-0.2.0`.
Its machine-retention and forward-recovery rules govern this rollout.

### Proven baseline and preservation requirement

A's public derivation/source inventory proves selected profile generation 223
uses runtime `3bb08df22aa4a36b7ff23ef62aaad586f4c59bb7` (source NAR
`sha256-pDaBIdK6uFgVq0Gw7arQLjvIjKsGrKg33IFmwmxnOoo=`) and extension
`f8da821e3c76e26e73aa9d89a712eab0e0faa319` (NAR
`sha256-U5y/TEny6nsyXWNlCMktmxTZhpVO0QY4kOo/qgwsapM=`). The installed native
executable remains the tested Codex 0.165.0 at `/nix/store/2rqwqchjlv6l2nw5l491pkhvrsijn50c-codex-package-0.165.0/libexec/codex/bin/codex`,
SHA256 `647b0157e6472a793e0a0bd45bc44ef8ade673b6d8f3db4118260acda4976652`;
codex-web remains `d3a29bee90ef00a08816920408c596152339a637` and the installed
catalog remains `495ef6620926420612ee4988e69d03a4e975e41734a1a5e3208db65fcd731db7`.
No Codex, provider, model, catalog or saved-team change is needed.

The previously verified `925a76e7974784204be15edcf3f3305cbe362e4a` candidate
cannot be selected directly. It lacks installed `turnRetryManagedTurnProof=1`,
`sessionServicesStateSchema=1`, `sessionServicesLifecyclePolicy=1`, typed machine
claims and the exact profile machine identity policy. Retired/terminal records
can retain those obligations; do not inspect or remove peer records to justify
a downgrade. Build a reviewed successor **R** preserving the complete public
3bb baseline and adding the owned monitor implementation, including reporting
policy 3 and monitor state/policy 1. Keep original 925/a595 reviews, source refs,
NARs, candidate roots, native eleven-case, runtime 28-check, composed six-check
and CI receipts intact and attributed to their exact old inputs.

### Stable packages and dependencies

| Owner | Source/files and result | Dependency and acceptance |
| --- | --- | --- |
| A | Refresh the generic feature onto proved public runtime 3bb, preserving old 925 evidence/ref. Reapply only the owned baseline fix and monitor change where still necessary; reconcile overlaps in the existing files. Publish exact reviewed successor R. | Independent of config gem setup. Preserve selected retry, registered-service lifecycle, typed-claim and identity capabilities plus the monitor contract. Conflicts with changed semantics return to architect/lead before expanding scope. No generic framework/API/schema change is authorized by this refresh. |
| D | Refresh the owned workspace feature onto public workspace `12a3df65467c7c460cae5e0a3cd8dca60138288e`; preserve current extension f8, machineIdentityConfig, site/team/coordination/integration composition and sibling/follows wiring. Retain only the owned monitor guidance correction in `docs/agent-instructions/verification.md`; pin R through `flake.nix` and generated `flake.lock`, producing W. | Baseline/guidance reconciliation can follow lead release independently; the pin waits for published R. Preserve newer public guidance. Do not copy the old a595 flake wholesale, introduce a top-level runtime input or edit the extension lock. |
| C | Own configuration worktree/branch at `worktrees/2026-11-03-lead-wakeup-delivery/vpsfree-cz-configuration`, initial public base `2fe2a83d74d6ca1aa35909d9115ad3cd2a6d49fe`. Prepare pinned repository tools/hooks, then generate the channel pin, expected `flake.lock` only, producing C. | Pin waits for published R. Channel `dev-workspace`, role `devWorkspace`, root input `devWorkspace`; preserve all unrelated inputs and host settings. Tool-environment preparation does not block A's independent refresh. |
| Lead | Accept source/composition, coordinate independent review and exact artifacts, launch the authorized mutation driver, verify effects and own the machine claim. | No activation before committed quick checks, applicable review and exact builds. A/C/D retain their source boundaries and serialized Git ownership; no default mutation is included. |

C's worktree and ordinary registration already exist and are clean. Its
post-checkout hook failed because pinned local gems were absent; ordinary
repository `nix develop` tools setup repairs that prerequisite without bypassing
hooks or replaying worktree creation. The coordination operations document C
initially read came from bare local HEAD 86e19685, not its fresh 2fe checkout;
do not add that stale document or its release policy to this pin package.

After R is published, C uses
`confctl inputs channel set --commit dev-workspace devWorkspace R`, retaining
generated history/changelog and hooks. D sets the existing direct nested
`inputs.vpsfree-dev-workspace.inputs.dev-workspace.url` to
`github:aither64/dev-workspace/R`, then runs
`nix flake update vpsfree-dev-workspace/dev-workspace` in its own feature worktree.
Inspect the semantic lock diff: exact R in both paths, unchanged f8 revision/NAR,
root nixpkgs follows, sibling inputs and native/catalog identities. Run
`bin/check-dev-workspace-deployment --workspace-root ABS_W --configuration-root ABS_C`
against the final locks; it also verifies hostname, alias and wildcard identity.
Do not hand-edit the config lock or bypass its channel. Existing host modules
need no functional edits merely to ship the application.

The historical 64-commit workspace-prefix caveat remains part of the old review
record. Fresh public master has advanced to 12a; that is public baseline evidence,
not retroactive review of those commits by this feature. Inventory the refreshed
owned range and its guidance conflict/equivalence explicitly. Do not read,
classify, transplant or remove peer tracking contents. New source review must
bind old/new ranges, migration conclusions, overlap resolutions and complete
deployed input lineage; no unsupported whole-branch equivalence claim.

### Compatibility, ordering and recovery

The system consumes R's host module through the existing confctl channel.
The application remains W's composed **user-profile package**, never a system
package or a generic default package substituted for site composition. Preserve
the exact profile target `github.com/vpsfreecz/vpsfree-cz-configuration` /
`cz.vpsfree/machines/aitherdev`, adapter `confctl`, and legacy bridge
`machine:vpsfree:aitherdev`. One physical-machine claim covers system and profile.

Deploy the host configuration first and prove its effects before selecting the
user package. The old profile must remain compatible with the new host substrate
during this interval. Same native bytes do not prove a live profile switch:
reporting policy 2 to 3 changes the MCP invocation and requires the ordinary idle
daemon cutover. Prepare/copy while work continues, arrange natural completion of
owned turns, and let the selected host command's normal global execution and
pending-operation checks decide admission. The lead's mutation driver must be
owned independently of an active Codex turn that would itself block that check;
use supported external/registered execution, not private stop/finalize helpers.
Do not force-interrupt peer conversations, stop this session or clear their
state. Busy or uncertain admission pauses the profile stage until normal work
finishes; recheck the same prepared source and original effects before retry.

After selection, recover forward with the same R/W preparation or a separately
reviewed newer compatible package. Do not switch back to 925 or an old profile,
discard state or call `--from-candidate` as an ordinary path. A preselection
refusal leaves the old profile selected and uses ordinary restoration. A partial
selection keeps its target/journal and machine ownership until the original
recovery completes. Confctl's system auto-rollback remains enabled; a restored
system link alone does not prove its remote activation or rollback worker ended.
After a system fallback, reconcile effects and restore a host compatible with
the selected forward profile. No reboot is required or authorized by this brief.
The separately proposed recovery below is limited to the source-proved
predecessor communication-admission refusal; it requires main's explicit adoption.

### Checks, artifacts and activation

R first receives committed component quick checks and independent review, then
publication so downstream pins can resolve that exact revision. W/C final
composition review follows their committed pins and quick checks; this sequence
does not waive either review or release long builds early.

Quick checks precede final review: inspect refresh/range diffs and retained
contracts, run focused monitor plus overlapping retry/service/lifecycle/claim
regressions, verify hooks and generated locks, and run the final deployment
checker. Give the reviewer R/W/C exact ranges, migration/rollback conclusions,
new composition and startup cutover; preserve R1–R4 closures and the trusted
code-cell limitation. Reuse earlier review only for demonstrably unchanged
content under the review skill. After committed quick checks and review, build
the final composed W package and exact aitherdev configuration, and verify the
app/native/startup/claim contracts of the built outputs. Changed composition
does not inherit old 925/a595 success. Bind the new declared runtime/composed
check inventory and rerun affected checks; reuse a positive only when its exact
derivation/input/NAR evidence still matches. Run the eleven native cases against
the final composed candidate and exact retained native binary. Long/uncertain
checks use the installed fresh Luna/low monitor workflow; new temporary test
services use the current registered-service procedure, preserving owned teardown.

C's pinned confctl `7bee58a52372b95c2198ce3f2a719807a3c2c66b` supports:

1. `confctl build cz.vpsfree/machines/aitherdev`; retain the actual named GEN and
   its generation metadata, toplevel, autoRollback, machine mapping and input graph.
2. `confctl deploy --generation GEN --copy-only cz.vpsfree/machines/aitherdev`
   before the claim where supported. Build/root W with its exact clean committed
   source, e.g. `nix build --out-link ABS_OWNED_ROLLOUT_ROOT/composed-package --print-out-paths ABS_W`.
   Use a dedicated session-owned output link created atomically by this build,
   retained through verification, activation and handoff. A previous GC failure
   proves that an unrooted `--no-link` output is insufficient. Retain its target,
   derivation, NAR, source/input graph and predecessor profile token; preserve
   existing candidate roots and do not replace a link owned by another run.
3. Only near activation acquire a schema-2 claim for repository
   `vpsfree-cz-configuration`, selector `cz.vpsfree/machines/aitherdev`, adapter
   `confctl`, with no repository merge claim. Verify authoritative held status
   and run `verify-machine` for this exact committed deployment batch. Recheck
   selected package/source, prepared artifacts and current system/profile
   baselines; a newly changed selected generation invalidates the old comparison.
4. Under that ownership, run named-generation `dry-activate`, then named-generation
   `switch` through ordinary confctl. Preserve health checks and auto-rollback;
   do not rebuild implicitly, disable guards or reboot. Verify both
   `/run/current-system` and `/nix/var/nix/profiles/system` plus actual command and
   health outcomes. A proved identical system output may be recorded as a no-op.
5. Invoke the **selected** `workspace-host switch --source ABS_W` with exact
   `DEV_SESSION_SLUG`, `DEV_SESSION_WORKSPACE` and `DEV_WORKSPACE_CLAIM_ID`.
   Its normal compatibility, transition, registration and idle checks remain
   authoritative. No forced daemon cleanup or direct profile-link edits.

The lead launches the mutation driver; a watcher may only observe its bounded
status/logs. A claim or dry activation is not success. Preserve source/system/app
store paths, named generation and final runtime graph in existing rollout/review
receipts outside configuration Git. If using a retained adapter operation,
its exact attempt/request/observed `adapter-result.json` and original recovery
remain required; live links cannot replace that receipt. Do not create a legacy
job or new scheduler to bypass ordinary claims.

The supported policy-2-to-3 handoff is an external operator shell after managed
work naturally becomes idle. The lead prepares the exact reviewed source,
rooted output, claim ownership and command/result handoff, then ends its turn;
the external invoker runs the ordinary selected command under the retained
ownership:

```sh
DEV_SESSION_SLUG=2026-11-03-lead-wakeup-delivery \
DEV_SESSION_WORKSPACE=/home/aither/workspace/ai/vpsfree.cz \
DEV_WORKSPACE_CLAIM_ID=EXACT_HELD_CLAIM \
  workspace-host switch --source ABS_W
```

On 2026-11-05 the user confirmed the external-invoker role in direct reply to
the separate-aitherdev-shell handoff: “I can run the commands you'll give me”.
The user will run the prepared ordinary application switch after the lead's
turn ends, with the exact held claim and session environment, and return logs
and status here. A owns the finite fresh source/artifact/selected/system-profile
baseline; C owns the bounded command/handoff source proof. The lead owns host
copy, schema-2 claim and named-generation dry activation/system switch before
handing the ordinary profile command to the user. This records the invoker
decision only; it releases no activation or repeated source/build/review work.

The named invoker is confirmed. Before claim or driver release, the lead still
establishes the exact retained command/status/log handoff and ordinary preflight
guards. A continuously active lead
cannot synchronously drive its own restart admission. Selected 3bb's
`docs/workspace-portal.md:1088–1095` documents the external-shell idle path;
`libexec/workspace-host:722–725,2420–2427` and
`libexec/dev-session:9333–9344,9450–9460` retain the ordinary execution-idle
refusal/restoration. Do not infer global idle from completion of our own turn;
the command performs that check without inspecting peer conversation contents.

An already-idle external invoker may use ordinary `dev-session service run`
with a fresh explicit resource ID as the independent process container. It
persists intent and starts immediately in its own `app.slice` unit with
`Type=exec`, `Restart=no` and `RemainAfterExit=yes`
(`libexec/workspace-session-services.rb:419–449`). Its source placement survives
portal/Codex unit restart, not reboot or user-manager loss; this survival has
not been exercised here. Pass exact ownership environment through explicit
absolute `env` argv; the service CLI has no environment flag. Same-ID launch
recovery only observes the original unit and does not retry the switch.
Service state alone is not an activation receipt.

No supported automatic active-lead-to-idle dispatch primitive was established.
Starting this service from the active lead would race the same idle refusal;
it is not a timing solution. Do not add a delay, polling scheduler, private
lifecycle helper or forced stop. A busy/unknown result retains the original
claim, pending target and ordinary forward-recovery rules. The external owner
reconciles that exact attempt and returns its real command, selected-profile
and health results to the lead; neither automatic retry nor automatic wakeup
is promised by this handoff.

Default integration and session lifecycle remain unapproved. Keep the exact
machine held until deployment/effects and complete approved integrated lineage
satisfy the release requirements below.

Live acceptance verifies the selected W/R and system generations, portal/router
health, naming and this session's conversation continuity, retained settings and
ordinary member reporting, and actual monitor capability after policy-3 startup.
Use one bounded owned monitor check to prove a persisted exact outcome starts
the idle lead through the selected runtime, with real launch/event/turn receipts;
the already packaged matrix covers failure/escalation and recovery. Do not treat
stored events, a browser indicator or the prior disposable suite as that live
proof. Preserve other sessions and all unresolved work. Failure or ambiguity
keeps the exact claim and original recovery; do not declare the runtime usable.

Promptly release the physical machine only after verified deployment/effects,
no unfinished command effects, and fresh remote proof that its complete deployed
feature lineage (R, W, C and dependencies) is integrated into approved defaults.
Integration needs separate explicit repository/target approval; until then a
successfully deployed machine remains held. For equivalent rewritten history,
retain independently reviewed old/new mapping rather than claiming a nonancestor
commit merged; substantive successors require a new verified deployment. Check
the exact owned claim before release and its terminal state afterward. Release
does not stop, archive, delete or clean this session. This appendix is a design
release candidate for the lead; it performs no pins, builds, claims or activation.

## Archive-hydration failure: bounded diagnostic package

Main accepted evidence-only instrumentation after exact R
`58e87f9d3ccc1aac262b29f587a1d0553257a554` FULL29 exited naturally with failure.
C traced the terminal browser timeout to the initial operation-GET hydration
wait, before the archive opener or POST, in the disposable archive-lifecycle
guest. The current diagnostic epoch precedes context/page creation and omits
the waiter-arm time; elapsed/navigation/GET observations cannot establish the
exact spent waiter budget or a backend, load or monitor cause. No production
fix, stage-budget change or deadline increase is justified. Keep the original
failure and effects records, and earlier positive artifacts in their exact scope.

**Boundary and ownership.** A creates and supplies an owned AUX ref/worktree
from exact R58; primary R/W/C remain clean and frozen. After that worktree is
ready, C owns only `test/archive_lifecycle_browser.cjs` and its quick checks.
A alone owns AUX Git/commit operations. No immediate publication, downstream
pins, production changes, Nix fixture edits or additional documentation package.
Source diagnosis remains C-owned; architect synthesizes the next evidence.

**Instrumentation contract.** Keep the existing `performance.now()` epoch and
`elapsedMs` calculation. Add scalar milestones immediately before hydration
waiter arming and `goto`, at navigation/hydration settlement, and on entry to
the outer catch before diagnostic work. Add one wall-clock anchor beside that
epoch for correlation with existing guest logs; do not treat browser timestamps
as proof of server dispatch. Record only bounded document/module and exact
operation-GET metadata: relevant pathname, event stage, timestamps, status or
failure, and existing Playwright request timing fields. Use a finite selection
of the document/modules relevant to this hydration path and the existing
bounded diagnostic structure. Preserve output bounds; add no payload, query,
header, environment, credential or instruction values.

Keep the 30-second default wait, `Promise.all` ordering, all predicates and
assertions, and the existing 1500-ms diagnostic cap exactly unchanged. Add no
await, network request, retry, delay, production logging, framework or changed
VM resources. Passive event/milestone recording must preserve resolution and
rejection behavior. Existing diagnostic bodies need no expansion. Failure must
still exit as failure; instrumentation is not a remedy or acceptance result.

**Checks and release.** C runs repository-environment `node --check` and scoped
diff/whitespace checks, then freezes the one-file delta. Main inspects that
delta; A commits the AUX change. The affected independent review must verify
the diagnostics-only boundary, unchanged ordering/budgets/assertions and bounded
metadata at that exact committed head. Only main may subsequently release ONE
natural run of the failed VM after review disposition and reconciliation of
prior check effects. This brief releases no VM, full-matrix rerun, W6, copy,
claim or activation. A successful diagnostic run belongs to its exact revision
and input graph; it cannot retroactively make R58 FULL29 pass. Any verification
reuse needs the actual derivation/input evidence. Retain old roots and failure
logs; no migration, rollback or general code-cell conclusion follows. A later
runtime or stage-budget correction requires a separate source-backed decision.

### Accepted final verification disposition

Main explicitly adopted this disposition: retain the already reviewed passive
helper as final test observability. Its bounded
milestones fill a demonstrated gap in diagnosing the existing hydration check
without changing request flow, deadlines or assertions. This remains within the
feature's verification work and needs no further instrumentation. The successful
AUX run completed all eleven existing archive-lifecycle subtests, including the
original scenario, but emitted no failure timing dump. The original pre-POST
timing cause remains an explicitly accepted residual uncertainty; neither the
helper nor that success establishes a fix.

The intended final runtime is exact reviewed head
`f161ede8a6ea4cf540edcb7ece81ebb76f064a05`, tree
`861e89b9f1d5a412ed3f9f290356dddfcffe3e83`: the existing baseline fix, monitor
capability and passive diagnostic in three coherent commits. Preserve R58's
failure, source/artifact roots and the separate AUX successful graph. No
production, runtime state, schema, native, catalog or settings change is added
by the diagnostic commit. Main reports all four component review lanes already
accepted exact f161; those conclusions apply unchanged to that code. Its new
final-consumer purpose and downstream composition still need review.

Main released A for primary-source/ref reconciliation and publication of exact
f161. D/C's matching generated workspace/configuration pin packages are
conditional on A's verified publication. Consolidate each owned runtime-pin stream to its final
pin, retain the independent guidance commit and original receipts, and give
main/reviewer the exact final ranges, complete graph and no-migration conclusion.
Committed quick checks and final composition review precede acceptance execution.
Acceptance execution remains unreleased until final committed pin quick checks
and affected consumer/composition review. The exact-f161 code review is reused;
the new consumer purpose and graphs remain in that later review's scope.

Canonical final runtime 29 and composed W6 checks must all pass. A's completed
read-only comparison establishes five unchanged reusable checks with exact
derivation/output/current-NAR proof: `codex-package`, `host-auth-benchmark`,
`host-module`, `host-module-idempotency` and `ruby-source-filter`. The actual
passed AUX archive check is the sixth positive for final f161. The other 23
current bindings remain unproved, including all fourteen Ruby shards and their
aggregate, and the creation/recovery VMs. Twenty-four bindings changed from
R58, including twenty-one formerly positive checks; those old successes cannot
substitute for the changed bindings.

A's finite mapping is retained at
`/tmp/lead-wakeup-archive-hydration-f161ede8-bcawgpsx/receipts/reuse-assessment.json`,
SHA256 `f0b72d032768add3281ab39f017713111d1155cfd8ccd63c2f9aa82e3aee900d`.
It also records changed generic-package and Go-module derivations; the unchanged
fixed vendor hash establishes no binary or composition equivalence. W6 still
requires its final composed graph. These artifacts support only their actual
provenance and do not relabel R58 FULL29 as successful. Earlier application,
host, native and CI results retain
their exact scope. Main releases only the remaining necessary verification after
the final source/composition gates; no repeated positive check is justified by
this disposition alone. A recurrence returns to the recorded evidence and
failed-check procedure, with no timeout increase or blind retry.

Retaining R58 without the helper was considered and not selected. It would
still require complete final 29/W6 success and would not explain the earlier
failure. Retaining the small reviewed helper is preferable because
future failures of this existing check otherwise retain the same known evidence
gap. External-invoker, machine ownership, forward recovery and activation gates
remain unchanged. This decision makes no deployment-readiness claim.

### Selected zmy package: verification and rollout disposition

A's public inventory establishes that selected
`/nix/store/zmyllqw6x1cxk8vhwliy7r11ykd19cz9-dev-workspace-0.2.0` still uses
exact runtime 3bb, extension f8, SDK d3 and the same native executable. Its
35 runtime-contract fields equal myjy; f161 preserves them with only the planned
reporting-3/monitor-1 additions. Claim, machine identity, coordination and
integration contracts are byte-identical. No generic runtime or configuration
pin refresh is justified by this selection change.

The changed catalog is
`a3f49bd3c1429d2d570cde01d509ae2d65a84c03b896c4265d9b9ccb0e317958`.
Nineteen default role-instruction slots (six unique variants) changed; models,
efforts, access, purposes, utility behavior and capacity did not. Generated
names changed, including the verification utility's native name. Current xff/W64
still produces catalog 495 and would replace the newer instruction defaults.
That does not satisfy the rollout's preservation requirement, even though the
runtime/state contracts match. Retained member settings must remain untouched.

Evidence is A's `selected-zmy-public-inventory.json` under
`/tmp/lead-wakeup-candidate-f161-W64-jtvylqbn/receipts/`. The selected immutable
workspace snapshot is `/nix/store/sj9h2xl6qvs5a198fz2gn61jp52a5j54-source`, NAR
`sha256-f8x3gvG1D5KH5IxnbK6YF+pvMG3kREJOSAoPp5vBwo0=`; its Git revision is
unknown. Do not infer ancestry, copy the whole snapshot or investigate peer
state. The installed coordination guide body is unchanged; current package and
catalog headers differ.

**Accepted separate gates.** Main accepted this split and released A's isolated
fixed-f161 runtime-29 verification under the current installed utility policy.
Selected-package metadata adds no new
runtime incompatibility, and these checks do not select a live package. Fresh
verification watchers must resolve and freeze the current installed a3f49 utility
policy and actual available definition, including its generated name, with the
unchanged Luna/low behavior and execution policy. Do not substitute old aliases
or modify retained team settings. Keep the candidate's own policy and source
identity inside disposable fixtures; the orchestrating watcher's policy is a
separate identity. Existing review, isolation and exact-artifact reuse gates
still apply. A owns the active heavy-resource batch until its natural terminal
result and explicit resource return; no W build overlaps that ownership.

For the shortest final delivery path, defer W-specific native acceptance and W6
until the composition preserves current instruction defaults. D's completed
read-only inventory establishes the one-file package below. Require the resulting
catalog's 19 slots and all unchanged policy fields to match the selected catalog;
preserve f161/f8/SDK/native, existing follows, site/claim configuration and saved
settings. No whole-source rebase or automatic refresh.
Rf161 and Ce3 need no change on current evidence. Then perform the affected
instruction/composition quick checks and committed review, the final W/C
matching check, and build/root the final W package before its native/W6 checks.
Reuse previous artifacts only with exact derivation/input/output/NAR proof.

Retain xff, GEN and all successful receipts with their original scope. Live
rollout remains held on preservation of the newer defaults, ordinary startup
and compatibility admission, fresh selected/system/profile baselines, the named
external invoker and exact machine ownership. Unknown future changes remain
unassessed. Apart from main's separately recorded A verification release, this
disposition grants no source, Git, pin, test, build, copy, claim or activation
release and does not change the accepted original timing residual.

### Settled W-only instruction-preservation package

**Owner and source.** Main accepted this brief and released D's complete
source/quick/focused-commit package, plus C's conditional single final checker.
D owns one file in its existing workspace feature: `config/agent-teams.nix`.
Apply exactly the five replacement
blocks from selected immutable
`/nix/store/sj9h2xl6qvs5a198fz2gn61jp52a5j54-source/config/agent-teams.nix`.
The W64 input SHA256 is
`7ac7140f0b1d55d6df4288898732a5db47f779b7c24cd5d693734e8ae648c188`;
the resulting file must equal selected SHA256
`8541976c7050d182163449296be36320d3039a12acc3f2fa23297f6dd80d5986`.
D's exact five-block diff SHA256 is
`9b8b9ea8e2e0814f465bb1c3ae21759d1f407cfd2b601a2e7b28d4b8dce12ed6`.
This preserves public selected bytes; no new wording or source-check edits.

The blocks change common lead requirements, add shared delegated requirements,
replace Full-team/Lead-designed lead prefixes and replace designer/implementer
defaults. They produce the established 19 instruction slots/six variants.
Preserve all other prefixes, reviewer/observer instructions, models, efforts,
access, purposes, lifetimes, routing, utility/work policy and capacity. Keep
W64's `flake.nix`, `flake.lock`, monitor guidance and all composition files
unchanged: the selected snapshot's flake selects older 3bb and must not be copied.
Rf161/Ce3 need no edit or new pin. No retained settings are read or changed.

**Quick acceptance.** In the existing repository environment, parse the Nix file,
run `test/agent_instructions_test.rb`, and check the scoped diff/whitespace and
exact file hash. Evaluate raw `teamConfig` and its generator-equivalent digest:

```sh
nix-instantiate --parse config/agent-teams.nix
nix develop --command ruby test/agent_instructions_test.rb
nix eval --impure --json --file config/agent-teams.nix
nix eval --impure --raw --expr 'builtins.hashString "sha256" (builtins.toJSON (import ./config/agent-teams.nix))'
```

Require exact digest `a3f49bd3c1429d2d570cde01d509ae2d65a84c03b896c4265d9b9ccb0e317958`,
all 19 instruction values equal the selected catalog, and equality of remaining
raw policy after removing only the generator-defined generated fields. D proved
the 3bb/f161 generator byte-identical; do not invent broader normalization.
Require unchanged flake/lock/guidance/composition blobs. Generated team/behavior
digests and native names are expected to follow the new catalog; utility
behavior stays `20212a3e814132d953ca91029e022451e03acc83fc52872ca238f8c76f4dfbb5`.

**History, review and later checks.** D retains W64's ref/evidence and creates
one focused preservation commit after the existing guidance and final runtime
pin. No new pin stream, history reset or whole-source rebase. Freeze the clean
head, one-file diff, exact hashes, quick results and no-migration conclusion for
main. C owns ONE final W/C checker after that commit. Affected instruction and
composition independent review follows the committed quick/checker evidence
before any rooted W build, native or W6 acceptance. The existing app-dependent
`checks.x86_64-linux.agent-team-policy` belongs to that longer post-review phase,
where the actual generated catalog/native TOML must match the selected policy;
it is not a quick static check. Main releases later work only after A's active
R29 batch naturally terminates and returns its heavy-resource ownership.
No extra docs, framework, runtime change or additional execution release is
added here. No further design work is needed absent a material contradiction.

### Settled W-only refresh onto public 2b

D's read-only inventory proves public
`2b5944e8df2ba06fb3193264c231adafa8329b5c` descends from old base 12a by nine
commits. Its `config/agent-teams.nix` equals selected source and owned 6b1 at
SHA256 `8541976c7050d182163449296be36320d3039a12acc3f2fa23297f6dd80d5986`.
The upstream and owned scoped preservation diffs are byte-identical, SHA256
`e1e30a7146f4f5476a80b0549448e64350031c36b2b9e04b57d30c75560a5337`, with
stable patch ID `7a3d2aea7e3c8e189ba2f0c8d314980dd6ce3774`. The preservation
content is patch-integrated upstream; commit 6b1 itself is not an ancestor of
2b and must not be described as literally merged. Selected immutable workspace
Git provenance remains unknown.

**Complete package, awaiting main release.** D owns the mechanical refresh of
only the existing monitor guidance e19 and final f161 pin 64eb onto exact 2b in
the owned workspace feature. Retain old head
`6b1ff5c2a63e616a4628af90dcc30b4d98922f9e`, W64 refs, review 444620, earlier
reviews, graphs, roots and receipts. Omit the now-redundant preservation commit
using the exact upstream-content proof. Expected final owned history is two
coherent commits and three changed paths: `docs/agent-instructions/verification.md`,
`flake.nix` and `flake.lock`. No new pin stream, wording or source behavior.

Preserve the newer public sessions/verification/team-workflow documentation.
The owned guidance hunks and public verification hunk are textually disjoint;
clean replay is an expectation until D performs and verifies it. Preserve exact
config854/catalog a3 and the owned f161/L9 pin: public 2b still pins 3bb.
Extension f8, SDK/native, site/machine identity, coordination/integration and
all other graph/follows bindings remain unchanged. Use ordinary owned-worktree
Git operations and hooks; no whole-tree copy/reset or peer tracking contents.
Any nonmechanical conflict returns to main before changing semantics.

**Acceptance evidence.** D supplies exact old/new base/head ranges, ordered
guidance/pin patch equivalence and range-diff, the dropped-commit/upstream config
proof, expected three-path/two-commit inventory, and an explicit no-migration
conclusion. Run scoped diff/whitespace, Nix parsing, the existing instruction
and deployment-contract quick checks, and raw catalog-a3/policy/graph preservation
checks. C owns ONE final W/C checker against the committed refreshed W and
unchanged Ce3. No check/build loop or repeated unchanged R check is included.

Retain prior reviews for demonstrably unchanged owned content; give the same
reviewer the complete committed quick/checker packet for affected consumer and
history disposition, including the newer public guidance baseline. Patch/config
equality is evidence, not an automatic whole-branch review exemption. Preserve
the historical 64-prefix caveat without retrospectively reviewing or classifying
peer records. A later artifact reuse claim separately needs exact derivation,
input, output and NAR proof; matching patches or policy alone are insufficient.

Rf161, Ce3, GEN and A's active R29 remain fixed. New W build waits for R29's
natural pass/effect reconciliation and resource return, plus final committed
quick/checker, affected review and verified publication. This brief releases no
source, Git, push, build or activation by itself. Deployment direction grants
no default-branch integration; external-invoker and machine gates are unchanged.

### Accepted recovery for the predecessor communication guard

The user's ordinary profile switch on 2026-11-05, 09:16:46–09:16:54 UTC,
exited 1 with the communication-preservation refusal. Preserve its original
`profile-switch-refusal.json` and log/status files in
`/tmp/lead-wakeup-aitherdev-rollout-c2n4xj47`. Main separately verified unchanged
selected zmy/profile token and the existing held claim; the verified host TOPpyw
remains deployed.

C's source proof establishes an admission gap in the predecessor, rather than
a missing candidate reader. Selected zmy's 3bb guard requires communication
policy 1 and reporting policy 2 when communication-state filenames exist.
Reviewed Prbx/Rf161 truthfully declares communication 1/reporting 3 and accepts
reporting 2 or 3; communication implementation/dependency paths are unchanged.
Selected preparation refuses before candidate native probes, transition lock,
activation, pending-update write, selection or daemon restart. Earlier source
realization/local diagnostics and conditional cluster `transition-adopt` may
precede that guard: do not describe the entire command as side-effect-free.
No private communication or peer-state inventory is needed or authorized.

**Accepted by main on 2026-11-05.** This actual preselection admission gap
qualifies for the existing public, source-bound `--from-candidate` recovery
entry. Use the reviewed candidate's real compatibility reader and gates; keep
its truthful descriptors and all state. A reporting-2 bridge would be larger
and is not required by the established source contract. No source/history,
descriptor, schema or test-framework correction is proposed.

The bounded command interface, to be wrapped in C's existing foreground
log/status handoff after main accepts the disposition, is:

```sh
DEV_SESSION_SLUG=2026-11-03-lead-wakeup-delivery \
DEV_SESSION_WORKSPACE=/home/aither/workspace/ai/vpsfree.cz \
DEV_WORKSPACE_CLAIM_ID=5ed5527b-c5b0-42fe-8d2d-53aacf27fd81 \
  /nix/store/rbxh3i5sqqc8j6ms0qhkggfd9m68wnp7-dev-workspace-0.2.0/bin/workspace-host \
  switch --source /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-03-lead-wakeup-delivery/workspace \
  --from-candidate
```

The source remains exact clean W1b219 with Rf161/Ce3; Prbx and its root/artifact
receipts remain unchanged. Fresh handoff files are
`/tmp/lead-wakeup-aitherdev-rollout-c2n4xj47/profile-candidate-recovery-1.log`,
`.exit`, `.start` and `.end` (all four suffixes on that same basename, observed
absent when this brief was saved). Preserve original refusal files, prevent
overwrite and return the actual command exit and complete log here. No new
background runner or retry loop is introduced.

The user invokes this from the separate aitherdev shell after the lead ends
and native work is idle. Main/C bind fresh unchanged predecessor/profile-token,
source/artifact and exact held-claim evidence before handoff. The public entry
requires an installed profile and an unselected executor identical to the output
built from `--source`; candidate-generation/transition locks, source/registry,
typed machine ownership and all compatibility checks still apply. The selected
predecessor still owns preselection quiescence and native-idle proof. This
entry point grants no forced interruption, state removal or private-helper use.

Source anchors are Rf161 `docs/workspace-portal.md:1124–1139`, public
switch/prepare/activate and candidate-generation locking. Existing tests cover
source binding and predecessor quiescence; final native11/runtime29/W6 successes
do not establish this live communication transition. No unchanged-source test
or build loop is needed to decide the recovery entry. Main must still verify
actual selection, startup, health and owned monitor usability afterward.
On failure or uncertain effects, retain this attempt's logs, state and claim;
do not blindly rerun. If selection occurred, continue the selected forward
package's ordinary recovery rather than reuse an unselected-candidate entry.
Reconcile any earlier outstanding effects through their existing owner.

Main inspected and adopts this operational recovery on 2026-11-05. The user may
run the filled foreground handoff once from the separate idle shell after the lead
turn ends. This is the documented recovery exception for the demonstrated refusal,
not an ordinary-update shortcut. Main owns the handoff; architect performs no switch.
Default integration and lifecycle remain unapproved. The held machine remains
subject to verified effects and complete approved integrated-lineage release.

### Recovery-2: natural-idle admission disposition

The user's recovery-2 invocation on 2026-11-05, 09:59:52–10:01:36 UTC,
exited 1. Preserve
`/tmp/lead-wakeup-aitherdev-rollout-c2n4xj47/profile-candidate-recovery-2.log`:
selected-predecessor `require-execution-idle` reported an unsupported native
execution-status shape. Main confirmed selection remains zmy; the pending Prbx
target, held claim and verified host TOPpyw keep their original ownership.
This refusal is distinct from the preceding communication-policy refusal.

C's completed source/protocol diagnosis establishes that the exact packaged
native schema declares `active` with required `activeFlags`. An authorized
status-only observation of C's own member returned `active`, empty flags and
two keys, reproducing the shared cardinality guard's misleading rejection.
Empty active flags do not establish idle. The original other-thread response
was not retained and remains unknown; do not classify it from this reproduction.
Both selected and candidate helpers have the same guard. Correcting its label
would still refuse active work and would not unblock deployment.

The remaining cold admission path checks the latest terminal turn, queue and
retry/submission storage. C found matching pinned request/response schemas and
no second decoder incompatibility. That is source/protocol evidence, not proof
that every managed conversation currently meets those conditions. The normal
team proof stops at its first blocker.

**Settled operational boundary.** No inspected public aggregate all-blockers,
count-only readiness, wait-idle or maintenance-window interface exists.
Preparation checks compatibility/probes rather than global idle; activity is
only an update timestamp. Suspend mutates services/coordination and itself
quiesces or refuses busy work, so it is not a solution. A bridge, busy-label
fix, helper, poller or new service is not justified for this admission problem.

A feasible cutover requires an operator-coordinated natural-idle/no-new-input
window across managed native work, including roots, members and this lead/team.
Original owners let work finish and resolve their own outstanding interactions;
no forced idle, stop, queue removal or peer-state editing is authorized. Only
after that window and the existing fresh source/profile/token/claim/effects
preflight may main prepare one justified external user handoff through the
already adopted public candidate entry. Its transition locks, drain and selected
predecessor quiescence remain authoritative; no status snapshot substitutes for
action-time checks. Earlier handoff releases do not authorize blind retries
after these refusals. No next command is released by this disposition.

The user has now explicitly answered “yes” to main’s bounded metadata-only
execution-status/queue-count inventory request. Main released one read-only
census to C under that scope. Conversation/project-file reads, stopping work,
queue changes and cross-session messaging remain unauthorized. Native `thread/read` also returns preview content and queue
listing returns inputs, so any separately approved inventory must extract only
the approved metadata without outputting or retaining those payload values.
Do not treat these endpoints as count-only or expand into a general audit.

Synthesis is complete. The remaining prerequisite is the coordinated idle
window and, if approved separately, its bounded metadata evidence. No further
source investigation, correction or verification loop is proposed. Preserve
all refusal/artifact receipts, forward recovery, held-machine release conditions
and the absence of integration/lifecycle approval.

### Automated maintenance: user requirement and existing-source reuse

The user subsequently rejected a manual idle window as the delivered solution:
“well thats not acceptable. this process has to be automated -- active turns
are paused and resumed after activation. didnt we recently work on this in
another session?” They then authorized missing implementation: “well if that
feature doesnt already exist, design it and implement it”. This supersedes the
preceding manual-window recommendation as the product outcome, while retaining
its refusal evidence. It does not authorize unannounced live interruptions,
queue removal, default integration or session lifecycle actions.

C located existing cooperative maintenance in retained committed generic source
`fc7c6a05be304dccc86dd976a5d573e6ba72368c`, principally
`c8ee5ca7337ffbce2034aac40637457f7a2d66a5`. It diverges from both frozen Rf161
and observed default `240a53dafabf24b6718195b88bee012a4ead8698`; its named remote
feature ref was not advertised. Existing review/publication is unproved.
Reuse this implementation rather than create a second coordinator. Compose it
with current monitor/reporting3, service, typed-claim, recovery, native and
selected policy obligations; never select the older feature wholesale.

Design is assessing the supported initial bootstrap as well as later updates.
The retained implementation uses cooperative safe-boundary acknowledgement,
exact finished-turn proof and durable continuation, not a transparent suspension
of arbitrary tools/processes. Its documented first tool installation requires a
native restart and cannot add an MCP tool to an already running daemon. A
settled implementation brief must automate coordination/recovery for that first
transition without representing uncovered active turns as checkpointed. Source
release belongs to main after that contract is sufficient; no live operation is
released here. Original Prbx/refusal receipts, host TOPpyw and held claim remain
their exact provenance.

#### Settled reuse and initial-install boundary (2026-11-05)

The user simplified bootstrap: “Im ok with pausing all threads at the first
migration manually... if future activations will be automated.” They further
authorized main: “actually, you can send a pause/resume command to the active
sessions yourself”, limited by “..during the first switch”. Main coordinates
that first window only after reviewed source and verified artifacts are ready.
This is not permission to delete queues, interrupt unknown external effects,
archive sessions or integrate defaults. No pause or switch is released by this
design. Future activation remains an automated product requirement.

**Decision: no reporting2 bridge.** Compose the existing maintenance feature
with the current final monitor runtime, retaining the current native/catalog
and public compatibility obligations. Within the authorized first pause window,
use the reviewed final package's public source-bound `--from-candidate` entry
without `--enable-maintenance`. It installs final reporting3 reader/control
through ordinary predecessor quiescence. Then use the selected public
`workspace-host switch --source <same-final-source> --enable-maintenance` to add
the MCP startup contract. This is an ordinary startup-only maintenance operation,
even when the package/profile path stays unchanged. Hold the initial window
through both stages, fresh startup/continuity proof and restoration; main resumes
only the work it actually paused. Do not hand off literal commands before the
new exact artifacts and current predecessor/claim/operation preflight are known.

Source basis at fc7: `libexec/workspace-host:624–645,651–720` requires both reader
packages only when the requested maintenance target is enabled;
`libexec/workspace-maintenance.rb:166–225` declines maintenance dispatch for a
nonreader predecessor and otherwise creates the existing owned worker;
`workspace-host:773–781` and the startup grant methods stage even a same-package
startup change. Thus the first stage uses the guarded ordinary path and the
second uses the existing `idle-bootstrap` mode. The source-bound candidate entry
does not add tools to the old native process or waive quiescence. The ordinary
switch may supersede a valid preselection pending Prbx target through its existing
writer; selecting Prbx first is not required. Never edit that record directly.
Preserve both earlier failed attempts and all old receipts. The distinct-target
fixture below verifies this supported path before the new live handoff.

#### Runtime contract to retain

Reuse `docs/workspace-updates.md` and `docs/maintenance-mcp.md` at fc7 as the
feature contract, adapted to actual native0.165 and current monitor integration.
The worker, journal, status/cancel/recover commands, private retained observer,
MCP acknowledgement and startup grants already exist; do not introduce a second
scheduler, daemon, checkpoint format or pause protocol.

- Pause means cooperative safe-boundary completion. An exact active retained
  root/member receives a conditional steer only after uninterrupted observation
  of that turn's start. It reconciles tools, child work and effects, saves needed
  context and directly calls `maintenance_ready(operation_id, nonce, ack_id)`.
  Native caller metadata, retained incarnation/root/member, source turn, pending
  tool item, socket epoch and current owner must agree. A receipt alone is not
  readiness. Preserve the existing 30-second lease, 90-second call and 120-second
  tool budget; expiry loses readiness, never forces interruption.
- The worker holds new application admissions while existing work reaches its
  boundary. Preserve already accepted input, native queues/goals, submission
  identities and saved settings. A held new request must remain visibly held or
  refused before acceptance; never report delivery or silently drop it. Existing
  source tool/report completion and maintenance acknowledgement must not deadlock
  behind a lock held by the waiter. No runtime/generation lock spans agent waits.
- Retain the same observer while joining application writers. Recheck readiness
  before the existing exact-process SIGHUP drain; no SIGSTOP/SIGCONT, repeated
  force signal, turn interrupt or forced deadline. Native0.165's admission drain
  rejects new turn admission and waits running turns/admitted requests; it is not
  a process/cell checkpoint. Keep its source-exit and destination proof gates.
- Resume only a participant whose exact maintenance finish and terminal turn
  are proved. Existing queues/goals use the existing activation-only path;
  otherwise send the existing single stable continuation with retained settings.
  Unknown delivery retains its original identity and blocks completion. Stop
  before admission suppresses continuation; later Stop governs admitted work.
  Cold/inactive histories and uncovered turns receive no invented resume turn.
- Uncovered turns or unsupported effect/tool modes remain visible waiting
  conditions with pre-cutover cancellation. New observer installation cannot
  reconstruct earlier coverage. First bootstrap uses the agreed pause window;
  later normal covered turns are coordinated automatically. This is not a promise
  to suspend arbitrary OS processes, yielded code cells or every unobserved turn.
  Existing cell uncertainty is not solved by a terminal turn or by this feature.
- Preserve cancellation/restoration before cutover and exact-operation forward
  recovery afterward. Startup grants remain bound to unit/process/invocation,
  source/target/profile token and startup digest; uncertain startup is reconciled,
  never replaced blindly. Restore owned portals/terminal shells and delivery
  admission before declaring the operation terminal. Sessions remain open.

Native source corroboration: pinned
[shutdown state](https://github.com/openai/codex/blob/360319d8dee62d87e2d59fc0c21805d79519cfed/codex-rs/app-server/src/lib.rs#L214-L298)
and [turn admission](https://github.com/openai/codex/blob/360319d8dee62d87e2d59fc0c21805d79519cfed/codex-rs/app-server/src/turn_admission.rs)
support graceful drain, not transparent execution checkpointing. Keep the
already established distinction between thread resume and interrupted-task
continuation. Do not change native/model/catalog policy to make a fixture pass.

#### Implementation packages and dependencies

These are sufficient source boundaries for main's release; this document itself
does not assign or release implementation. Owners retain complete package
responsibility, including focused tests, documentation and review fixes.

**A — SDK prerequisites (implementer0), independently ready.** Compose the three
existing commits `c91d89e` (conditional steer), `786a391` (structured RPC error)
and `b193883` (ordered observer/write freeze) onto current SDK d3a29bee. Their
branch diverges at f6f4a187; selecting b193 wholesale would discard current work.
Own `codex/{client.go,conditional_steer.go,observer_events.go}` and their focused
tests plus owning SDK docs/protocol assertions. Preserve the existing APIs:
`ConditionalSteer(ctx, thread, cwd, expectedTurn, text, id, action)`,
`DiscardPreparedConditionalSteer` with the same tuple,
`RPCErrorData(error)`, `ObserverGeneration()` and
`FreezeObserverWrites(ctx, expectedGeneration)`, with ordered detached
`ObserverEvent` delivery. Conditional steer never starts/resumes/queues or changes
settings; uncertain sends reconcile exactly. Freeze joins writes, retains the
same read connection and never creates coverage. Preserve d3 submission/retry
behavior and all current-native changes. Quick tests cover exact-turn refusal,
lost receipt/unknown replay, observer loss/order/freeze and unchanged monitor
send/reconcile behavior. Main owns the reviewed dependency publication/pin gate.

**B — runtime controller and application composition (implementer2), depends on
A's exported API, otherwise reuses fc7.** Own `portal/internal/maintenance/**`,
`portal/cmd/workspace-portal/maintenance_*.go` except D's tagged native fixture,
`portal/internal/web/{activity*,maintenance*,server.go}` except D's browser test,
and the maintenance admission changes in `workspacecodex/{client,recovery,turn_retry}.go`.
B owns `cmd/workspace-portal/main.go` wiring in one announced shared-file window;
consume C's registration/helper interfaces without concurrent edits. Preserve
current managed-turn retry proof, service/claim capabilities, monitor delivery
progress budgets and known-unsent repair. Port actual0.165 request/item shapes;
never treat an unknown effect as inert to recover old0.164 assumptions.

The necessary monitor seam is bounded: enumerate exact owned utility threads
through existing `monitoroperation.Store.Inventory` and use its lifecycle/effects
proofs. They stay non-roster and are not cooperative acknowledgement participants
or recipients of synthetic continuation. Running/uncertain utility effects block
cutover until resolved by their existing owner contract. Permit durable utility
report recording and original receipt reconciliation while holding new utility
launches and lead delivery. Readiness/dispatch must recheck maintenance admission;
do not cancel monitor operations merely for an update, rerun commands, enroll
utilities as members or clear their effects evidence. If this requires changing
the existing monitor contract rather than composing it, return that concrete
deviation to main before editing it.

**C — host/startup/package composition (implementer1), depends on A/B contracts.**
Own reused `libexec/{workspace-maintenance.rb,workspace-switch-diagnostics.rb}`,
host/dev-session/coordination-host seams, `agentteams/maintenance_registration*`,
runtime descriptor and Nix packaging/unit wiring. Retain current reporting3,
communication1, typed claims, services, managed retry and native/catalog identity;
add truthful maintenance1 contracts. Preserve strict legacy startup shapes and
the separate opt-in MCP startup path. First final-package install omits that opt-in;
second same-source operation enables it. No reporting2 artifact or source stream.
Focused tests must exercise the real predecessor contract, reporting2-to3 public
candidate route, same-package startup-only operation, stale token/refused claim,
cancel/failed-stage restoration and exact forward recovery. No idle-shape guard
weakening: valid active status is a busy condition, not permission to switch.

**D — acceptance and owning documentation (implementer3).** Reuse fc7's existing
tagged maintenance-native test, `nix/tests/workspace-maintenance.nix`, browser
test and owning maintenance/update docs; adapt their synthetic backend to the
actual pinned advertised tools as already required for monitor fixtures. No new
test framework. Unit tests stay with A–C; D integrates actual SDK/native/host
paths once interfaces compile. Cover the two-stage initial install and a later
automated update with active retained root/member, exact command completed once,
saved checkpoint, verified activation and one continuation. Add accepted queue/
goal preservation, cold-thread no-wake, Stop suppression, uncovered/unsafe-effect
hold, disconnect/lost acknowledgement and failed-stage same-operation recovery.
Use real native receipts/history and real disposable service/activation effects;
no fabricated completion or receipt. Keep direct maintenance-call proof distinct
from CodeMode and monitor utility reporting.

#### Evidence, history and rollout gates

Existing fc7 source is a reuse candidate, not a passed review or an installed
feature. Preserve its exact base/head/commit lineage and current Rf161/W1b/Ce3
refs, reviews, roots and failures. Reconcile reused source into coherent feature
history; do not claim that either divergent branch is literally merged. Preserve
schema1 reader/recovery obligations; absent historical state-consumption evidence
does not authorize deleting or rewriting a supported format. Main/A serialize
Git and overlapping files. No unrelated public-default refresh or Codex upgrade.

Commit completed source and pass focused quick checks before independent affected
review. The review covers full composed history, native/effect trust boundary,
admission/continuation races, first-install public path and recovery, not only
the reused patch. Long disposable native/activation tests follow review through
fresh policy watchers. Final runtime/workspace/config pins, rooted artifacts and
composition checks must bind the new exact graph; old R29/W6/native11 successes
remain evidence only for their old graph. Existing test results may be reused
only with their required actual input/derivation/output proof.

Live first-window pause/resume belongs to main after those gates and fresh exact
machine/claim/source/profile/pending-operation checks. Test both ordinary stages
before giving the user one justified handoff. No live pause, retry, switch,
claim change, integration or session lifecycle action is authorized by this brief.

#### Historical predecessor fixture boundary

The reused fc7 VM starts with maintenance-reader support, so it cannot prove the
first reporting2/nonreader transition. For that case C adds one explicit
**test-only flake input**, `maintenance-predecessor`, pinned to
`github:aither64/dev-workspace/3bb08df22aa4a36b7ff23ef62aaad586f4c59bb7` with
source NAR `sha256-pDaBIdK6uFgVq0Gw7arQLjvIjKsGrKg33IFmwmxnOoo=`.
Retain that flake's own locked inputs: no follows/override to the candidate SDK,
native or nixpkgs. Generate the lock normally and compare the predecessor's
reachable locked identities/follows semantics with its original lock; node names
and deduplication are not dependency identity. Preserve all unrelated production
input paths. This is a declared fixture dependency, not a production runtime pin
or another deployable bridge.

C owns `flake.nix`/generated lock wiring and passes `predecessorMkPackage` into
D's `nix/tests/workspace-maintenance.nix`. Construct that factory from the pinned
input's actual `lib.mkPackage`, using its own pinned nixpkgs for the VM system;
the historical factory closes over its original SDK and native inputs. D may
supply the same ordinary fixture site/team/router parameters used by the test,
but must not override source, SDK, runtime descriptor or registration behavior.
Do not substitute a current-source package with fields removed, an impure local
store path or a moving historical getter. There is no existing historical-source
getter in the inspected flake that needs reuse.

Quick evidence: Nix syntax and semantic lock-graph checks, exact predecessor
revision/NAR and original SDK d3 binding, and the new check's argument wiring.
The app-dependent build remains a post-review long check. D's real VM records
the actual predecessor package/native/startup/contract identities, executes the
public final candidate entry from that nonreader, then enables maintenance using
the same final source and verifies both stages. Fixture parameters mean this is
an actual historical-runtime package, not a claim of byte identity with installed
zmy. A's candidate SDK successor must never enter the predecessor package. The
existing C/D package and main's Git/review/execution ownership remain unchanged.

#### First migration with an earlier pending target

Main accepts C's source-only pending-target finding. The historical selected3bb,
Rf161 and current pending writer/reconciliation method bodies are unchanged.
Current `workspace-host:623–744` binds the new source/package/token, compatibility,
registry/plans and claim; `:757–777` writes the new pending target on quiescence
refusal or before successful selection. `write_pending_codex_update:3511–3535`
validates the new tuple and safe owned file, then replaces it atomically without
requiring equality with the earlier target. Later reconciliation's selected-target
check does not require selecting that earlier target first. Completion at
`:809–821` must still match selection/token and its pending snapshot; it cannot
clear a newer interleaved target. This establishes eligibility, not current live
readiness or a claim that failed preparation had no effects.

D adds one case to the existing historical-predecessor VM fixture: start with
the actual reporting2/nonreader predecessor; invoke distinct fixture candidate
A's own `bin/workspace-host switch --source <source-A> --from-candidate`, without
enabling maintenance, while controlled native work is active. Do not invoke the
historical selected helper for this attempt: its reporting1/2 parser rejects A's
reporting3 registration during preparation, before quiescence or a pending write
(C's exact3bb `libexec/workspace-host:1780–1845` source finding). A's public
candidate entry validates its exact source and delegates ordinary quiescence to
the predecessor. Assert the failure reached that busy/quiescence boundary,
left the predecessor selected and wrote real pendingA; a nonzero exit alone is
insufficient. Retain that attempt's exit/log evidence. Let the owned fixture
work finish normally, then invoke final candidate B's public `--from-candidate`
entry without enabling maintenance. Verify the existing guarded writer replaces
pendingA with B and clears B only after verified target startup/completion. Do
not select A, fabricate receipts, seed private state or bypass quiescence. Then
exercise the already planned same-B `--enable-maintenance` stage. Preserve the
existing interleaved-target guard tests; no new target-replacement mechanism.

Main conditionally released D's fixture source/static work once this brief was
saved. D owns this addition and its bounded static checks; main owns runtime Git.
C's host helpers and completed independent checks remain unchanged unless D
identifies a concrete uncovered contract. No duplicate Ruby batch is required.
Native/VM execution remains behind final committed quick checks and affected
review. Return any actual API/design conflict to main before expanding scope;
no live probe, pause or switch is released here.

#### One disposable reader-error capture (9cf1 / c3c2)

**Decision: temporary diagnostic instrumentation, no permanent SDK API or pin.**
The original diagnostic at
`/tmp/lead-wakeup-runtime-first-sdk-reason-9cf1c769/diagnostic-result.json`
(SHA256 `b2059aad82813375c63fe7df0126100c695f541e9b81722be636bcecad740134`)
records generation1/sequence30 `invalid` with SDK `read-error`, followed by a
lost snapshot. Successful native exit does not identify a typed close or EOF.
Use B's accepted source diagnosis
`/tmp/lead-wakeup-9cf1-read-error-B-eorxkgbl/diagnosis-result.json`
(SHA256 `75be55041de953d098bd4418b7a653d6299b178f5fb6ea9d40107d00e837ea63`);
do not repeat its producer audit. It establishes the original `Read`-error seam
before disconnect, the absence of another accessible error hook, and the limits
of errors already replaced by coder/websocket1.8.14.

A permanent additive ObserverEvent value could carry the same facts, but its
only established consumer is this one investigation. Publishing that API and
refreshing production pins adds no diagnostic evidence. An exact-source SDK copy
and ordinary Go overlay/modfile reach the same code and existing first-origin
record without that commitment. The fixture's MCP helper executes the same
compiled Go test binary; there is no separately built portal to miss the overlay.
This is an instrumented diagnostic graph, never canonical acceptance evidence.

**Owner/files.** B owns the complete finite source-and-quick-check package after
main's release. Seed an owned disposable SDK copy from verified published
`c3c2adb705f5ff6bb42c98bd44be3649fd93bedb` (module
`v0.0.0-20261105132033-c3c2adb705f5`), such as its immutable source
`/nix/store/rv7i2mkzrq8qwkkpmn22nlw8x0a653fg-source`. Do not edit the store,
module cache, SDK worktree or canonical runtime. In that copy, change only
`codex/{client.go,observer_events.go}` and the existing owning focused test file.
For exact runtime `9cf1c7694b3918fcef1b088669ee6241605f071f`, tree
`2c71c9b4c15da00f0353c1d31d3b2b8f70ad23b9`, use ordinary Go `-overlay` mappings
for temporary copies of `portal/internal/maintenance/observation.go` and
`portal/internal/web/activity_maintenance.go` plus their existing owning tests.
The native fixture file, production module files and Nix pins remain unchanged.

**Data and control contract.** Add one detached fixed value to the existing
ObserverEvent, populated only from the actual error returned by the original
Read call, before `markDisconnected`. Include availability; integer
`websocket.CloseStatus` (including -1); independent `errors.Is` flags for EOF,
UnexpectedEOF, net.ErrClosed, context cancellation and deadline; net.Error
presence plus Timeout; syscall.Errno presence plus its numeric value. Preserve
independent facts for wrapped/joined errors. False fields without availability
are unknown, not negative proof. No error interface/pointer, type/error/close
reason text, payload, path, frame or new clock/buffer/callback is retained.

Pass this value in the existing callback to the existing Apply call, and copy
it into the same first-origin value under its existing mutex and generation/
sequence. Never backfill an earlier poison with a later reader error. Preserve
first-cause lifetime, reset/bounds and detached access. Keep the exact Reason
mapping, event dispatch order, disconnect/close paths and all classification,
Covered/WaitReady, lease, drain, cleanup and continuation decisions unchanged.
No observation, native request, reconnect, pending RPC or authority is added.
The existing fixture serializer prints the extended origin automatically.
Origin and Snapshot remain separate non-atomic observations; their output after
Wait does not timestamp the original error. Missing/opaque/library-replaced
cause remains honestly unavailable and does not authorize another capture.

**Binding and focused checks.** Copy the runtime's unchanged go.mod/go.sum to
external diagnostic `.mod`/`.sum` files and add only an explicit codex-web replace
to the disposable SDK root. Use absolute `-modfile`/`-overlay` paths,
`-mod=readonly` and `GOWORK=off` in the repository Nix environment. Record original
commits/trees, source hashes, complete overlay map, replacement source/diff hashes,
modfile/sum hashes, effective module graph, toolchain, exact commands and compiled
test binary identity. Prove all other resolved dependencies unchanged and check
canonical files/index/pins stayed unchanged. No ambient replacement or fresh
dependency selection is allowed; reuse existing evidence output conventions.

Run focused non-native checks of typed1000/1001/1005/custom close status;
wrapped/joined EOF/network/context/errno facts; absent metadata; actual event to
first-origin copying, earlier-cause preservation, reset and detached reads.
Compare the existing classification/readiness results and event sequence with
the uninstrumented expectations. Compile the tagged fixture with no native case
selected. Freeze the complete disposable diff and evidence for main inspection;
no new framework, source publication or canonical pin stream.

**Inspection and one capture.** Under the installed mandatory-change-review
skill's routine-investigation boundary, this disposable, nonshipping evidence
instrumentation does not automatically become a final product deliverable or
require an independent final-review cycle. Main inspects its full diff, binding,
control-flow preservation and quick results before separately releasing A's ONE
native diagnostic capture. A uses the existing fresh utility/ownership procedure,
exact pinned native, original code_mode/strict=absent case, 90-second budget,
modes/seed/order/assertions and original cleanup/effect accounting. No model,
close policy or fixture control change. Either outcome stops for interpretation;
do not launch remaining modes, full suites, publication or live actions.

This classification is not a waiver for a later functional fix. If evidence
supports one, implement only that correction on canonical sources, without the
diagnostic replacement/overlay. Retain original and instrumented receipts under
their exact graphs. Any production SDK change follows normal reviewed publication
and explicit pinning; runtime changes follow normal committed quick checks and
affected independent review. Verify the resulting canonical graph has no local
replace/overlay and run its required native acceptance there. A diagnostic pass
cannot certify the production close contract. This brief authorizes no source
execution or native run by itself; main retains release.

#### Canonical EOF compatibility: completed source witness

**Status: shelved.** The later maintenance scope-reduction decision below
supersedes this proposal for the current release. No EOF consumer implementation,
SDK reason change or pin update is released. The evidence remains historical.

**Evidence and decision.** The one frozen overlay capture
`/tmp/lead-wakeup-runtime-returned-error-9cf1c769/diagnostic-result.json`
(SHA256 `31f0bc448339e77d66bd0ed0f156f2b42fe79b2fc0d9bf50829c1fd16ab9e97b`)
proved returned EOF with no typed WebSocket close; its original assertion failed.
B's accepted producer packet
`/tmp/lead-wakeup-eof-interpretation-B-i8q_2jmb/diagnosis-result.json`
(SHA256 `7f257fbb54c845765426a0b7f207bd08a67c6e8caf81a49cfe122a068b8d7b54`)
binds exact native360319d8 source and raw anchors. Its graceful-ready shutdown
cancels transports without sending a close frame. The same disconnect token
also serves abnormal paths, and library EOF can occur within a partial header.
Neither EOF nor successful native exit establishes a clean stream or checkpoint.
The capture did not preserve the terminal item map or order EOF against the
finish publication; no second diagnostic capture is needed just to reconfirm EOF.

Choose a narrow **conditional consumer correction**: distinguish EOF passively
in the canonical SDK, and admit a non-ready EOF tail only with the stronger
ordered completed-source witness below. Do not label EOF normal-close or treat
the diagnostic result as proof that this predicate will pass. Retire the
temporary diagnostic field/API, module replacement and overlay entirely from
the production graph. Native version/model/catalog remain unchanged for this
correction; main releases source work only after accepting this boundary.

**SDK contract.** Keep ObserverInvalid, generation/sequence and dispatch order.
`observerReadErrorReason` retains typed1000/1001 → `normal-close`. A returned
error with CloseStatus -1 and `errors.Is(err, io.EOF)` becomes `read-eof`, provided
it does not also match UnexpectedEOF, net.ErrClosed, context cancellation or
deadline. All other cases remain `read-error`, including typed1005/other close
codes, standalone UnexpectedEOF and cancellation. Wrapped EOF is supported;
the new string asserts only the returned error identity, not frame completeness
or shutdown cause. No raw error text, new event structure or diagnostic payload.
An old runtime treats the new reason as ordinary loss; a new runtime with the
old SDK also remains held. No mixed-version fallback guesses EOF.

**Earliest eligible EOF and missing-effects boundary.** The same existing
ordered observer must have received, in order:

1. Continuous exact source-turn coverage and the existing pre-cutover readiness/
   full effect-and-descendant cleanup proof. The original call is the sole
   foreground maintenance wait, with no earlier poison or unresolved effect.
2. Exact `item/completed` for that original maintenance call, with status completed,
   matching start/completion identity, server/tool and all three operation/nonce/
   ack arguments; no error; exactly the existing successful finish result.
   Reuse the predicate in `NativeAdapter.VerifyFinished`, retaining only a bounded
   derived witness, not the result payload. That result can be produced only
   after the original handler's durable FinishPublished and global drain gate.
3. Exact `turn/completed` for the same source, status completed, after that finish
   event. All known items are terminal. No new tool/effect/child start after the
   finish, successor turn, post-completion effect or later poison may intervene.
4. The original reader's EOF in that unchanged connection generation.

The successful source-completion event is necessary: finish alone leaves room
for later same-turn tool effects hidden by a partial-frame EOF. Existing native
global drain/new-turn admission and exact successful source exit remain required;
queue/goal metadata by itself grants no proof. Any missing event or changed
identity holds. Later FinishPublished, drain, exit, history, reconnect, restart or
new observer cannot repair an EOF that arrived before the ordered witnesses.
Do not broaden the documented unreported-cell limit to excuse missed known
native effects. No new cell inventory or global quiescence claim is introduced.

**Reducer and consumer.** Use bounded volatile state on the existing watched
turn/item for successful finish and completed-source eligibility. Reset on the
existing watch/generation/turn boundaries; invalidating effects cannot be erased
by a later repeated completion. Preserve the first diagnostic cause separately.
Ordinary source completion sets Covered false; it must not erase a valid earlier
witness merely because readiness ended normally. EOF always returns
Covered=false and WaitReady=false. Only the fully eligible exact tuple may expose
its ToolItemID with a distinct `observation-eof` reason; ineligible EOF remains
loss. The following disconnect preserves only that already-qualified EOF tail,
never creates it. Typed normal-close handling retains its existing contract.

The runtime's separate EOF-exit candidate must require current operation cutover,
all exact source HUP intents/global DrainProved, FinishPublished, retained owner/
native/socket/generation/source/item identity and the eligible snapshot. Existing
passive source history may corroborate it; positive active/failed/interrupted/
different-source or semantic proof failure rejects it. Transport unavailability
does not establish finish. Candidate status permits only waiting for the exact
successful source exit; every service's verified exit still precedes ordinary
target activation. Keep Finished and ResumeObligation false for the EOF-tail path,
including against source-loop promotion, until passive destination VerifyFinished
proves the original completed turn, exact successful call and terminal effects.
No new persisted proof/schema is needed. A retained disposition cannot replace
the live owner witness on recovery. Stop suppression, lease expiry, unknown
delivery, stable continuation IDs, queue/goal activation and two-stage first
installation remain unchanged. Missing destination proof stays recovery-required.

**Producer alternative and limit.** Pinned native can cancel before queued
terminal notifications flush; its biased DisconnectAll and sibling-task abort
do not guarantee this witness. If canonical acceptance lacks the required event,
retain the refusal and return the exact failed predicate to main; do not remove
it or automatically run another capture. The alternative is a separately scoped
native graceful-ready publication/flush barrier followed by a typed close,
leaving slow-client, forced, error and generic cancellation paths unchanged.
Simply sending Close on the shared cancellation token is unsafe. The needed
terminal-publication-before-flush ordering has not been proved or designed here.
That native/package scope is larger and is not released or presumed necessary
by this conditional correction. No guarantee of native acceptance is claimed.

**Packages and checks.** A owns canonical SDK `codex/observer_events.go`, its
focused tests and owning reference wording. Read-loop sequencing needs no change.
Test unchanged1000/1001 behavior, untyped/wrapped EOF, conflicting joined error
identities,1005,UnexpectedEOF/cancellation/network/unknown errors, and actual
ObserverInvalid followed by disconnect with unchanged generation/sequence.

B owns runtime `internal/maintenance/{observation.go,native.go}` and owning tests,
`internal/web/activity_maintenance.go` and tests, and
`cmd/workspace-portal/{maintenance_observation.go,maintenance_cutover.go}` with
their existing owning tests/docs. Extract only the exact finish predicate needed
to share history/event validation; preserve the existing canonical history check.
The current native fixture may recognize qualified EOF as a distinct closed,
non-ready result, requiring the exact nonempty tool identity for that branch.
Keep its modes,90-second budget, seeds, ordering, drain/exit and independent
destination assertions; no synthetic receipts or fixture-only policy bypass.

Meaningful quick controls cover the complete ordered positive witness and EOF
before finish/between finish and turn completion, wrong/failed/duplicate call,
cancel/retry-wait result, missing/failed/interrupted completion, new post-finish
effect or successor, prior poison/gap/generation loss, unresolved known effect,
late journal flags, wrong owner/drain/exit, negative destination proof and Stop.
Assert no EOF path creates readiness, source-only obligation or continuation.
Existing normal-close and queue/goal/uncertain-delivery checks remain relevant.

C owns one final mechanical SDK module/Nix pin update only after A's committed
quick-checked component passes affected independent review and is published.
Keep the historical predecessor's original SDK graph unchanged. B may perform
independent reducer tests against the stable Reason contract, but final compile/
acceptance must resolve the published SDK with no local replacement or overlay.
No repeated interim pin stream, DB migration or persisted observation format.
Update SDK semantics and the owning maintenance/update close explanation; keep
individual diagnostic provenance here.

Main inspects the complete composed diff, commits and quick evidence, then runs
the applicable affected independent review (protocol/authority/recovery risks,
including this ordering boundary) before canonical native acceptance. Reuse
unaffected prior reviews; do not treat the disposable diagnostic as acceptance.
Run the original relevant native cases on the exact canonical graph, with the
normal watcher/effects procedure and no deadline or assertion relaxation. Only
after required proof succeeds can main release dependent suites/publication/
rollout. This design performs no source edit, check, native run, Git or live action.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-03-lead-wakeup-delivery/).

#### Maintenance reduction: retain the transaction, remove peripheral obligations

**Decision and ownership.** Main accepted these scope reductions after the user's
changeset-size concern. This is one sufficient package for one implementer,
subject to main's source release; main owns Git. It supersedes donor requirements
for maintenance browser controls, separate switch timing and automatic terminal
reattachment, and shelves the EOF proposal above. Automatic cooperative updates,
CLI status/cancel/recover, durable ownership, admission/queue preservation,
checkpoint/effect proof, source exit, forward recovery and duplicate-safe
continuation remain required. Original monitor/wakeup is an independent delivered
feature. B's native graceful-close feasibility is independent of these deletions;
no native/SDK change or guaranteed cutover follows from this package.

**Browser boundary.** Delete `portal/internal/web/maintenance.go` in full:
`maintenanceView`, public-reason projection, `maintenanceAffects` and
`maintenanceAPI` have only the two browser routes and their tests as consumers.
Delete `static/maintenance.js` and `maintenance_browser_test.cjs`. In `server.go`
remove `/api/maintenance{,/cancel}` dispatch and the cancellation exemption from
the maintenance mutation fence. Remove only the Workspace update section and
script from `templates/operations.html`; preserve existing coordination controls.
Keep `maintenance_stop.go`, `requireMaintenanceAdmission`, prompt-response and
interrupt exceptions, `activity_maintenance.go`, and monitor delivery admission.
Keep `maintenance_test.go` helpers needed by
`TestMaintenanceAllowsExistingPromptResponse` and
`TestMaintenanceMonitorDeliveryHoldsNewEffectsAndReconcilesOriginalReceipt`;
remove its five status/projection/browser-cancellation tests, not the whole file.
The CLI/controller cancellation path remains authoritative.

**Diagnostics boundary.** Delete `libexec/workspace-switch-diagnostics.rb`, its
require/install lines in `workspace-host`/`nix/workspace-portal.nix`, and its test
file/require in `test/workspace_host{,/switch_diagnostics}_test.rb`. In
`workspace-maintenance.rb` remove `switch_diagnostics`, `switch_decision` and the
diagnostics-only `registration_storage_mismatch?`. Unwrap recorder calls in the
worker and host, preserving original call/lock/exception order; remove elapsed
lock clocks and diagnostic environment propagation. Keep the actual
`codex_restart_required?`, registration comparisons and all admission checks.
Important dependency: `switchOperationId` is functional, despite its origin in
the recorder. Generate its UUID once in `prepare_profile`, retain it in the
prepared record, and reuse it for operation/startup/recovery exactly as today.
Do not mint a replacement during worker restart. Keep existing operation-ID,
waiting, package-result and recovery-error progress output. Remove only the
diagnostic assertions from `test/workspace_host/live_switch_test.rb`; retain its
storage/restart-authority cases.

**Stopped-client recovery, without automatic presentation.** Do not delete
`restoration.go`, `TerminalIntents`, or the pre-quiesce `terminal-intent` journal.
`quiesce_native_client!` records ownership before replacing an owned Codex pane
with its shell; that uncertain-effect/recovery boundary remains necessary.
Keep `maintenance_terminal_sessions`, ordinary `restore_quiesced_sessions`/sync,
`maintenance_restore_writers`, Begin/FinishRestoration and their immutable
package/token/owned-set, cancellation, continuation and worker fences.

Remove `cmd/workspace-portal/maintenance_terminal.go`'s presentation observer,
attach eligibility, Stop-dependent attach reconciliation and per-pane receipt
writer. Replace its `terminal-sync` dispatch in the existing control file with
only an owned-sync authorization check: same worker/operation; exact owned
workspace/slug/root/incarnation; current restoration package/token and service
epoch (source for cancellation, destination otherwise). A pre-cutover retry may
preserve its recorded source terminals only under the unchanged source token/
epoch and owner. Reuse the existing terminal-restoration identity check; no new
controller, native RPC or durable terminal state. Remove `terminal-confirm`.

In `dev-session#reconcile_native_client!`, the maintenance-specific sync branch
must validate the existing managed session/pane and preserve its live shell (or
an already-present managed client) without sending a client command or loading a
thread. Unexpected/dead/replaced panes still refuse; do not kill or respawn them
to make restoration pass. Ordinary non-maintenance sync/attach stays unchanged.
Propagate the existing operation grant to maintenance-owned retry/compensation
calls of `restore_quiesced_sessions`, not only the final tail; after cutover an
unowned restoration attempt must remain refused. Remove `maintenance_finish_restoration`'s
per-pane confirmation loop. It completes only after all owned sync calls succeed
and owned portal services are positively restored. Worker loss retries these
idempotent effects; it must not repeat selection or continuation.

Remove `ReconcileTerminalResult` and its attach-specific tests, and remove the
per-pane result requirement from FinishRestoration. Keep the small existing
`TerminalResult`/optional `TerminalResults` decoding and validation for retained
records; new operations do not write them. A nonterminal old operation with
presentation receipts must refuse this reduced tail rather than silently erase
an earlier admitted attach; retain its original graph/evidence for disposition.
No migration, record cleanup or generic legacy recovery is added. Completed
records remain readable. The supported new tail relies on the existing trusted
worker's successful owned sync/start effects, as portal restoration already does.

**Checks, fixtures and order.** Implement the three reductions together, then
reconcile `docs/{workspace-updates,maintenance-mcp,workspace-portal}.md` with CLI
operation and shell preservation. Preserve startup, two-stage historical
predecessor/pending-target acceptance, native modes/deadline and continuation
assertions. In `nix/tests/workspace-maintenance.nix`, remove `decisions()` and its
two timing-record assertions while retaining actual process/profile/registration
proof. Replace presentation/reattachment receipt assertions with exact owned
shell/client survival and no new load/send assertions. Do not remove the VM or
substitute fake receipts. Keep native-effect `terminal_statusless.go`; its name
does not denote tmux presentation.

After main releases source, run repository-environment focused Ruby host
maintenance/live-switch and session tmux tests; focused Go maintenance/control
and web admission/Stop/prompt/monitor tests; Nix parse/embedded fixture syntax and
whitespace checks. Cover stable prepared UUID across recovery, CLI cancel,
wrong owner/incarnation/epoch, owned shell preservation with zero attach/load,
partial restoration/worker loss, and unchanged Stop/queue/continuation behavior.
Retain failure-before-finalize coverage; update it to the reduced tail, not
delete it. The package is complete after source/docs/quick checks and a compact
diff report. Main commits and obtains affected independent review before any
long native/VM acceptance. No source, check or execution is released by this text.

**Size and remaining architecture.** Actual named production files support an
estimated net removal of roughly 700–850 lines, including shared wrappers;
replacement checks make the final diff authoritative. This leaves roughly
7.3k of the maintenance production addition. Removing optional tests is not an
architectural reduction. Current source lengths show the dominant responsibilities:

| Existing owners/paths | Approximate current lines | Required responsibility |
| --- | ---: | --- |
| `maintenance/{observation,native,native_effects,terminal_statusless}.go` | 1,495 | Exact active-turn/tool/effect evidence; unknown work cannot become safe by assertion. |
| command `maintenance_{control,cutover}.go` plus `workspace-maintenance.rb` | 2,179 before cuts | One operation's inventory, admission, drain, activation and recovery sequencing across surviving processes. |
| store/controller/types, internal+command startup and restoration | 1,761 before cuts | Durable IDs, lost-ack recovery, startup ownership, Stop and continuation obligations. |
| owner/MCP/admitted-wait/activity integration | about 900 | Authenticated cooperative wait and preservation of the same observation owner while writers stop. |

These responsibilities are necessary under the current blocking-tool protocol;
their necessity does not prove that their implementation is minimal. The safe
consolidations established here are removal of parallel diagnostic registration
classification and replacement of the terminal eligibility/receipt state machine
with existing owned sync. No further large backend deletion is established by
this dependency inspection. Combining files would only hide the size. A material
further reduction requires revisiting the checkpoint/observation protocol itself,
not deleting recovery guards. B's separately owned graceful publication/flush/
typed-close assessment may remove the need for the shelved EOF machinery, but
cannot yet justify removing current checkpoint or effect evidence. This brief
does not claim that the peripheral cuts resolve the user's overall size concern.

#### Core protocol comparison: admission barrier versus completion evidence

**Historical comparison; superseded by the minimal core decision below.** B's
completed admission/history trace establishes the shared queue/goal gate and
passive cold startup, while identifying a narrower admission handoff defect.

**Disposition.** No materially smaller, fully supported protocol is established
by the current interfaces for the full queue/goal-preserving requirement. Reject
finish-before-drain as the general release contract. Destination-history
reconciliation is the preferable simplification to an EOF-specific witness,
but the existing `VerifyFinished` alone is insufficient; the prerequisites below
remain unresolved. Keep source frozen and the EOF proposal shelved. This is a
bounded comparison, not a new implementation or native-fork package.

B's completed pinned-native inspection establishes SIGHUP as combined RPC
admission drain plus automatic exit at observed zero running turns/admissions
(`app-server/src/lib.rs:226–305`). No public drain-without-exit control is
established. Crucially, that inspection does **not** establish an atomic fence
against core automatic queue/goal successors. Final history durability is also
not implied by exit0: shutdown/snapshot failures can be logged without failing
the process. These are proof gaps, not observed lost-work defects. Earlier
references here to global `DrainProved` must not imply stronger scheduler or
durability guarantees than the actual RPC refusal proves. This affects the
donor protocol too; keeping its observer alive does not close these gaps.

| Choice | Responsibilities removed or moved | Remaining problem |
| --- | --- | --- |
| Checkpoint, return finish, prove completed source, then HUP | Could remove the wait lease and retained observation tail if an authoritative completion/admission boundary existed. | Application writer exclusion cannot stop native queue/goal scheduling. Between completed-history sampling and HUP, a successor may start. SIGHUP before finish closes only the established RPC gate and returns to the current drain-first ordering. No supported independent freeze/read window is established. |
| Keep readiness wait until drain; use exact cold destination history for completion | Removes transport-close classification as completion authority, the proposed EOF witness, and potentially the post-release observer tail. Existing journal and send/reconcile own recovery and continuation. | Requires complete final effect/descendant proof and a genuinely held destination; success exit and stored acknowledgement identity are not those proofs. The native successor-admission gap remains. |
| Retain current observer through shutdown | Preserves current readiness evidence and can detect published later effects. | Cannot turn dropped notifications, typed close or EOF into authoritative completion. It retains substantial machinery without proving the missing scheduler barrier. No positive canonical cutover is accepted. |

**Exact races and existing reuse.** `RequireAdmission` and writer/terminal drain
fence application submissions; `maintenance_cutover.go#drain` signals the exact
process and tests `thread/queue/start` for `serverShuttingDown`. That is not proof
that internal queue/goal scheduling is fenced. `ListQueue`/`HasActiveGoal` inspect
state; they do not pause it. Repeated idle samples cannot supply the missing
atomic boundary. An unexpected successor can be detected by exact turn identity,
but rejection afterward does not itself prove preservation of consumed input.

After a successful maintenance reply, the same source turn can still start a
tool or child. The instruction to finish is cooperative, not native enforcement.
`NativeAdapter.VerifyFinished` (`native.go:393+`) proves the exact latest completed
source, successful original MCP result/arguments and terminal parent items.
It does not walk newly created descendants; a completed spawn call is not child
cleanup. The existing passive `verifyDescendants` machinery is the reuse point
for a completed-source check, without its active pending-item exception. Missing,
interrupted, changed or incomplete history remains unproved; absence of a child
from the new daemon's loaded set is not evidence that its effects ended.

For a destination-history design, ordinary target/native startup and **agent
activation** must be separate: startup would occur with application admission,
queue/goal activation, continuation and client reattachment still held. Only
passive exact history/effect checks could authorize an obligation, then the
existing stable-ID continuation or queue/goal activation. Current
`continueParticipants` already has this ordering for its deferred-history path;
it does not justify assuming every target startup consumer is held. Selecting
the target with unresolved completion would be an explicitly recoverable phase,
not a completed update or proof that unknown effects are safe. If the required
contract instead forbids even target startup before all effects are proved,
destination history cannot meet it without an independent offline/history
boundary; none is established here.

Lost acknowledgement still needs the exact successful recorded MCP result and
source completion: `FinishPublished` is an intent, not a receipt. Never recreate
a command, call or continuation to make missing evidence disappear. Before HUP,
cancellation may release the original wait and restore source writers. After
HUP, preserve the owning forward-recovery journal and exact process identities.
Worker restart cannot recreate live coverage from persisted `Observed`; early
finish would also need to distinguish agents already finished when cancellation
arrived. Destination reconciliation can reuse current identities/dispositions,
but must retain unknown-delivery and Stop suppression. These obligations survive
either design; deleting them would sacrifice user work, not simplify presentation.

**Product boundary.** Required: cooperative checkpointing, preservation of
accepted work/settings, no duplicate resume, and honest recoverable failure.
Not intrinsically required: a blocking tool after its result is released, a
particular observer surviving until process exit, or a WebSocket close category
as the completion receipt. A proven cold-history boundary could remove those
requirements. It has not yet been established for all post-finish effects and
native successors, so there is no safe one-line close-gate deletion.

The precise choice for main is between a narrower automatic contract that waits
when native queued/goal work cannot be safely fenced, and obtaining the missing
native scheduling/history guarantees for the full requirement. The narrower
contract can wait indefinitely on an active goal and must not be described as
automatic pause/resume of all accepted work. No queue/goal deletion or manual
future idle-window workaround is proposed. A native publication/flush patch is
not selected: B also found missing terminal-publication ordering, FIFO writer
fencing and graceful close/join semantics, with new packaging obligations. Moving
that work into a fork is not an established simplification. Main retains this
scope decision; no further audit, implementation or execution follows here.

#### Minimal core decision: drain, cold completion proof, then resume

**Current design709ca7a9; design only.** The user retained coupled wakeup delivery
and full automatic cooperative pause/resume, including queued and goal work.
Use the existing controller, journal, acknowledgement and stable delivery IDs.
Readiness belongs before cutover; exact passive destination history owns final
completion. Transport closure is not completion evidence. This supersedes the
donor's observer-through-exit requirement and the shelved EOF proposal1857+.
It does not release source, native packaging, tests or live operations.
Current baseline is main's accepted `86cd0f03e9fdab2e40c80912a4284508438f3afa`,
tree `8a4639809f301f9787bbde3956959215a0778605`; its19-path UI/timing deletion
has quick checks complete and affected review pending. Core/native/SDK source
is unchanged from retained9cf1/c3. No repeated Git or verification was needed here.

**Settled prerequisite and precise missing guarantee.** B's accepted final note
`/tmp/lead-wakeup-eof-interpretation-B-i8q_2jmb/diagnosis.md`
(SHA256 `572a1521ad12cf918294b66f397af399ca37711f8bc31728f6ec21abb0271292`)
binds these findings to native `360319d8dee62d87e2d59fc0c21805d79519cfed`:

- Queue and goal starts share `TurnAdmission` with HUP. Closing its mutex-protected
  gate rejects later starts; queue removal requires `Started`, and refusal leaves
  the goal intact. No second queue/goal fence or scheduler is needed.
- An already admitted start can release its permit after task registration but
  before asynchronous `TurnStarted` increments the app-server running count.
  Queue input can already have been removed. Shutdown can therefore sample both
  counters as zero. This is a source-supported interleaving, not observed loss.
  Runtime inventory/`VerifyIdle` samples do not exclude it, particularly for idle
  services and mixed actors. A counted maintenance waiter, delay or repeated
  sampling is not a general substitute.
- Ordinary `app-server --listen` has `managed_daemon=false`; it does not restore
  threads on startup. Cold read/list/loaded/turns/items calls do not resume them.
  Positive persisted completion is usable: canonical appends flush before their
  SQLite projection. Exit0 is not a durability receipt; errors/timeouts can be
  logged, and incomplete history may normalize to interrupted, never completed.
  No power-loss/fsync guarantee is added.

The minimum additional native contract is **continuous accounting from successful
admission through authoritative running ownership until task termination**.
Shutdown must never observe zero in the permit-to-running handoff, including
queue/goal starts, failure/cancellation and task removal. The concrete source
boundary is existing core `turn_input.rs` admission/start, `tasks/mod.rs` task
registration/lifetime, and the app-server `TurnAdmission`/running-count handoff;
`RegularTask`/bespoke `TurnStarted` must not be its sole delayed registration.
Transfer the existing permit/accounting ownership before releasing it, or retain
that permit through the registered task lifetime. Do not add a public pause RPC,
separate controller, queue, transport flush protocol or graceful-close machinery.
Main must separately allocate the exact native correction and its package input;
no such change is currently released. Full automation on the unchanged native
cannot yet be certified. The runtime/history simplification is separable source
work, but its automatic-cutover acceptance depends on this corrected source.

**Supported transaction.**

1. Preserve current preparation, typed claim, source/profile/startup identity,
   application admission and prompt/Stop/reporting exceptions. Retain the existing
   observer only for continuous active-turn readiness, exact pending MCP identity,
   known effect/descendant cleanup and lease renewal. Drain application writers
   and actual client processes; recheck inventory and readiness under the owning
   transition lock. No history-only reconstruction of readiness is allowed.
2. Journal cutover and exact source HUP intents. Require each live cooperative
   service's existing structured drain refusal; preserve the existing proven-idle
   source-exit branch without inventing a waiter for an empty service.
   With corrected native accounting, pre-admitted tasks
   remain owned through termination and later queue/goal starts stay unconsumed.
   Only then publish finish. The original admitted `maintenance_ready` invocation
   returns its finish result using `finishOriginalWait`; no replacement handler,
   restored lease or acknowledgement inferred from the journal is permitted.
3. After global drain and finish publication, the observer has no completion
   authority. Release/join its existing owner through `release-tail`; exact owner
   cleanup remains required, but need not wait for native exit. The same source
   turns complete cooperatively. Wait for exact native process exit and successful
   service result; do not interrupt them or extend the MCP's existing deadline.
   A missing finish/result is a recovery condition, never a guessed continuation.
4. Use ordinary activation/startup grants to select and start the exact target
   **held**. Force the existing `defer_portals` path for an unfinished maintenance
   operation, including the post-reconcile start branch. Keep actual stopped
   clients, ordinary resume/load, application sends, monitor delivery and automatic
   recovery consumers held. Native startup is the already-established non-managed
   mode, with no thread resume/watch or implicit resume. Selection/startup is an
   unfinished forward transition, not successful maintenance or permission to run
   an actor. Normal pending/startup reconciliation retains its existing ownership.
5. Before the first continuation or writer restoration, pass a passive completion
   phase for **all** captured sources, including Stop-suppressed actors. For each
   acknowledged source require the exact latest completed turn, original MCP
   item/three arguments/successful literal finish result, complete terminal parent
   effects and all descendant edges/terminal histories/cleanup. Reuse
   `verifyDescendants` in completed-source mode: no pending-source or active
   statusless-item exceptions. Cold/notLoaded alone proves no cleanup. Sources
   that naturally ended or were stopped before acknowledgement use existing
   natural-terminal cleanup, with no finish result or resume obligation invented.
   Missing rows, successor identity, incomplete/unknown effects, unresolved children
   or an unexpected loaded destination keep the entire operation held. A source
   `Finished` bit from an earlier path cannot skip this destination proof.
6. Only after that pass, retain the existing per-participant Stop linearization,
   stable explicit continuation, queue/goal activation and uncertain-delivery
   reconciliation. Queued/goal work is resumed by activation, not copied or resent.
   Inactive histories receive no synthetic turn. Resume only the recorded owned
   work; then restore actual stopped clients and writers through the existing
   restoration journal. Report complete only after these effects settle.

The all-source proof precedes the first continuation admission, not every recovery
of an already admitted delivery. Move entry to `resuming` after that proof and
write `Finished` only from the destination proof in this protocol. Reuse those
existing fields, exact destination identity and per-participant dispositions;
after an admitted/uncertain continuation, reconcile its original attempt instead
of demanding that the now-resumed thread remain cold or match its old latest turn.
No new completion table/marker is needed. Legacy phase/`Finished` values alone
cannot establish this ordering; old operations retain their old owner below.

This closes the post-finish effect gap without interpreting EOF: a tool or child
started after the finish reply must appear in the final completed parent/descendant
proof. No destination actor runs while that proof is unknown. Corrected admission
accounting prevents a pre-admitted task from disappearing into the shutdown count
gap; the closed gate prevents a successor after drain. Neither success exit nor
finish intent substitutes for persisted completion. Existing limits for genuinely
unreported external cells remain explicit; known native effects are not moved
into that exception.

**Implementation boundaries after main release.**

| Existing owner/files | Minimal change |
| --- | --- |
| `portal/cmd/workspace-portal/maintenance_cutover.go`, `maintenance_observation.go` | Keep pre-cutover proof/HUP/drain/process ownership. Remove the post-finish observation loop, `maintenanceOrderlyExitCandidate` and its transport-error classifier. Move owner release before exit waiting. Make `continueParticipants` prove all sources before its delivery pass; retain `recordDestinationFinish` identity/Stop checks. |
| `portal/internal/maintenance/native.go`, `native_effects.go` | Compose exact `VerifyFinished` with completed-source descendant cleanup, reusing existing pagination, identities and effect validators. Do not create another history service or persist transcript payloads. |
| `portal/internal/maintenance/observation.go`, `portal/internal/web/activity_maintenance.go` | Remove maintenance's special orderly-close completion branch/mapping. Preserve pre-cutover continuity, bounded item membership, poison, freeze and prompt checks. SDK c3's generic event API needs no new EOF reason or diagnostic fields. |
| `libexec/workspace-host`, `libexec/workspace-maintenance.rb`, existing startup/control helpers | Hold target portals/clients through the all-source proof; reuse startup grants, source/target selection and restoration. Do not let `_activate` or reconciliation start deferred portals early. Keep exact owner-release recovery. No replacement worker or state framework. |
| Existing native admission/task owners and native package input | Independently prove/fix the handoff above. Publish one reviewed immutable native dependency before final runtime pin/build/acceptance; bind supported cooperative source execution to that exact corrected package/registration contract. Version0.165, target capability or exit0 alone cannot assert source support. No general binary-probing facility. |

The final implementation must keep ordinary nonmaintenance switches unchanged.
These are coherent runtime changes for one owner, with native correction and
mechanical package composition separately owned; main allocates them and Git.
D's isolated Operations UI/browser cancellation and timing deletions are now
committed at86cd and under separate review by the assigned reviewer; that review
is pending, not a core review. Preserve functional `switchOperationId`. Terminal presentation
reduction stays held. Actual stopped-client recovery is retained here.

**Compatibility and recovery.** Reuse schema1 journals and current source/target,
incarnation, startup and delivery identities; no new database or transcript
format is required. Retained older operations keep their original owner/recovery
semantics, and absent historical proof remains unavailable. Do not reinterpret
old `Finished`/observer records as a cold proof or discard an uncertain send.
Cancellation before cutover restores the source; after HUP use the same operation's
existing forward/source-recovery selection. Worker restart cannot recreate live
readiness. After selection, missing history leaves a held target and recoverable
journal; it does not reopen writers or rerun the source. Unknown continuation
delivery reconciles the same ID without retrying as new work. Stop still suppresses
or interrupts at its existing admission boundary. Cooperative checkpointing is
not transparent process/cell suspension, and uncovered work still needs genuine
completion; this is not a new indefinite queue/goal-wait product reduction.

**First migration.** A fixed target cannot repair the currently selected0.165
source. Keep the user's one explicitly authorized lead-coordinated initial pause
window and the two ordinary stages: final candidate public `--from-candidate`
without enable, then same final source with `--enable-maintenance`. The window
must safely hold all required queued/goal work and new input through both stages;
do not delete, consume speculatively or infer a hold from a sent pause message.
Main proves the actual ordinary initial quiescence and resumes the work it paused.
Do not claim automated-source guarantees retroactively or build a reporting2
bridge. Later automatic operations must positively bind their **source** native
to the reviewed handoff correction using existing exact registration/package
validation. Unsupported old sources require that initial window, not a target-only
capability claim. Preserve original Prbx/refusal/pending receipts and claim ownership.

**Acceptance and proportionality.** Focused native regression stalls a successfully
admitted queue/goal start before asynchronous running-count publication, delivers
drain and proves no premature Finish; cancellation/failure release accounting,
and post-drain queue/goal records survive. Focused runtime regressions prove cold
parent plus nested-child cleanup with reads only, reject missing/wrong finish,
post-finish effects/unknown children/successor/history gaps, and prohibit first
activation when a later participant fails proof. Cover early observer loss versus
deliberate post-drain release, restart at release/startup/history/delivery boundaries,
Stop and uncertain send, and target startup without a portal/resume side effect.
Retain ordinary-switch and actual stopped-client restoration checks.

After committed quick checks and affected independent review, require an actual
disposable activation roundtrip with active acknowledged actors, accepted queue
and goal work, dropped terminal socket delivery, cold history verification,
one continuation/activation and restored clients. Include failed-stage recovery,
missing-history hold and the real historical predecessor/two-stage pendingA-to-B
fixture. No overlay/local replace, unpublished pin, native timeout or error-label
change counts as canonical success. Existing final acceptance obligations and
monitor evidence retain their original scopes. Update the owning update/MCP docs
to explain readiness, held startup, cold completion and recovery; remove obsolete
close-tail authority. This planning record itself needs no final-change review.

The simplification removes a second completion authority and its transport-specific
recovery branches, rather than merely reducing tests or moving them into a native
fork. It retains the genuinely necessary journal, readiness, effects, startup and
delivery transaction. The additional native cost is one admission-lifetime
correction plus its packaging/review, not publication/flush/typed-close repair.
No line-count saving or successful canonical cutover is claimed before implementation.

##### Legacy operation owner clarification for the released runtime package

`SourcePackage`, not `CandidatePackage`, is the existing immutable protocol owner.
`start_maintenance_switch` records the selected predecessor there, roots both
packages, then starts the stable-profile systemd worker. Before selection that
worker executes `SourcePackage`; its `package_root` remains fixed across target
selection. The same is true when an unselected candidate prepared the operation.
The stable profile only changes the executor on a later worker restart or MCP
control call. The earlier statement that old operations retain their owner
requires this routing correction; it is not already guaranteed by current code.

Route operation-scoped worker/control requests to the exact retained
`SourcePackage` binaries before interpreting phase, `Finished`, continuation or
restoration semantics. Reuse bounded strict schema1 loading solely to resolve
the operation/profile/source owner, preserving the original arguments, request,
worker flag and existing guards. Refuse an unavailable or mismatched retained
owner; never substitute the candidate or current profile. Source and candidate
roots already provide retention. Global startup/status actions without an
operation retain their existing reader and acquire no continuation authority.
New operations also belong to the selected source; target selection cannot
upgrade an in-flight protocol. This adds no completion marker or journal schema.
Cover restart after profile selection and an old `resuming`/`Finished` record in
the affected runtime tests. Main owns source release; B owns these existing
worker/control seams within the coherent runtime package.

##### Native correction boundary50648f6a: packaging settled, lifetime contract open

**Finite disposition; no native source release.** The existing permit can cover
the traced root/queue/goal start through termination, but that alone does not
establish continuous accounting for every task using the same start machinery.
The immediately required common-seam reads below expose accepted child work and
other starts with no such permit. Do not give A a partial functional patch as
whole-source support. B's runtime/history work remains independent; automatic
acceptance stays blocked on this exact native ownership contract. This narrows
the earlier assumption that one ordinary permit transfer was already sufficient.

Source is the locally retained official `360319d8` tree at
`/nix/store/j4xcz959sk3k5isb6q29gpyivjym37j9-source`, matching the pinned
`rust-v0.165.0` source NAR `sha256-b9PpwNQeZsJIN4wbGA3FLfWAKd2EDMN5E/zj/Y62/vk=`.
Only admission, task start/finish/abort and their immediate callers were inspected;
this is not a new producer-wide audit or observed lost-work finding.

| Existing path | Required ownership; present boundary |
| --- | --- |
| `core/src/session/turn_input.rs:409–445` and `:492–622` | Ordinary root starts and queue/goal/recovery starts already acquire the host permit. Move that same permit through `spawn_task`/`start_task`, without reacquiring after HUP or changing the admission decision. Early rejection/settings failure/cancel before registration releases the original guard once. |
| `core/src/state/turn.rs:75`, `core/src/tasks/mod.rs:388–438`, `:655–918`, `:957–1067` | A registered task needs ownership spanning both the spawned future and `RunningTask` cleanup. Normal `on_task_finished` takes/drops `RunningTask` before terminal persistence; abort cleanup runs outside the spawned future. Either location alone releases too early. A private shared RAII owner around the existing `Box<dyn Send>` permit, held by both lifetimes, covers the traced permit-bearing path. Use a `Send+Sync` container such as an ordinary mutex; the payload needs no inspection or new authority. Release only after both run/finalization and abort/removal ownership end. |
| `turn_input.rs:399–416`, `:492–515` | MAv1 parent-delegated explicit input deliberately bypasses admission; the one-shot review delegate can proceed after drain to finish its already-running parent. These are accepted parent work. Preserve that behavior: share/transfer a still-owned parent's admission through accepted child dispatch and task cleanup. A parent-turn ID proves lineage, not possession of a live permit. The exact existing carrier for this transfer is not established by the inspected seam. |
| `core/src/tasks/mod.rs:469–570`, `turn_input.rs:699–770`, `session/handlers.rs:80–98` | Pending mailbox work reserves a turn and calls `start_task` without a host permit. Independent root wakes must use the existing gate before reservation/input consumption and preserve pending mail on refusal. A wake that continues already accepted parent work instead needs that parent's still-live ownership. The current reservation helper establishes neither classification nor permit inheritance; treating every pending message as independent or every lineage-bearing message as inherited is unsupported. |
| `session/handlers.rs:101–135`, `:247–258` | Idle shell/compact calls use `spawn_task` directly. Their already admitted request must carry accounting into the task; a later call to the closed gate cannot replace ownership of an accepted request. The common task signature currently receives no such owner. Active-turn auxiliary shell work retains its existing owning-turn/effect contract and is not converted into a new admission here. |

**Exact unresolved prerequisite.** Establish the carrier and release boundary
from an accepted request or still-live parent through deferred child/mail/task
dispatch, registration, normal completion and abort/removal. Independently
scheduled work must pass the same existing gate; accepted descendants must remain
covered by inherited ownership until their run and cleanup end. Closing admission
must never see zero between those owners. A guard only on `start_if_idle`, an
unconditional new admission at `start_task`, or a counter based on asynchronous
`TurnStarted` cannot establish this. Rejecting accepted descendants to make the
counter simple changes the required behavior. Adding a second scheduler, global
fence, transport protocol or public pause API is outside the brief.

The bounded next native package must settle these actual callers together before
implementation allocation. If an internal owner carrier cannot be reused, main
must explicitly scope the minimum shared carrier/interface and its compatibility
cost; it is not silently authorized here. No additional autonomous investigation
follows this result. No completion marker or change to B's cold-history journal
is proposed.

**Regressions the sufficient native patch must own.** Use the existing
`core/src/session/turn_input_tests.rs`, `core/src/tasks/mod_tests.rs` and
app-server admission/shutdown tests. Deterministically hold task/event scheduling
after an accepted queue/goal/root start, close admission and prove shutdown cannot
finish while its task or cleanup remains. Cover rejection and cancelled/failed
registration before spawn, normal removal before final flush, abort with the
future ending before cleanup and cleanup ending before future destruction, and
no duplicate permit release. Accepted delegated/review work must complete across
drain without a zero-count gap; independent mailbox wakes refused after drain
must retain their input. Shell/compact must retain their original request owner.
These are the boundary tests, not an instruction to run a broad native suite now.
Cold destination history still decides actual completion; permit lifetime does
not turn exit0 or a swallowed persistence error into a durable receipt.

**Immutable package route, chosen by main.** C's accepted packaging finding is
recorded in `implementation-c.md:1095+` (receipt SHA prefix `79d0806b`). Append
one reviewed R-owned patch, e.g. `nix/patches/codex-turn-admission-lifetime.patch`,
to the existing llm91ff Codex `rustPlatform.buildRustPackage` derivation's
`patches` through `overrideAttrs`; pass that corrected output into unchanged
`mkCodexPackage`. Patch both existing native selections in `flake.nix` coherently;
the package check must bind the same corrected input. Do not patch only the
assembler. The exact llm recipe is retained at
`/nix/store/6xb99l21zqwilx52r3m1d1797vpa9xdw-source/packages/codex/package.nix`.
Keep its daemon patch, postPatch/postFixup, materialized layout/completions,
CLI/CodeMode-host outputs and license/NOTICE. No native fork/repository, release
version, SDK revision or dependency update is required by this route.

Preserve Cargo.lock (SHA256
`580ce642d0bc924e683c97f269cc2d20b0d74e9037b82cd8cde7a67def764e60`),
vendor hash and RustyV8 152.2 archive/binding inputs. Use the recipe's actual
Rust/cargo1.98.1, not a silent rustup change to upstream's requested1.99.1;
compilation of the eventual correction is untested. Required vendor/compiler/V8
outputs are not all present locally; substitutes/downloads and a full Rust build
are expected. Preserve the recipe's ThinLTO/debug reductions and eight-job cap.
Plan one heavy slot, multi-GB scratch and minutes-to-hours uncertainty with phase
reassessment, not a cache-only or cheap assembly promise. Native tests require
their explicit test invocation: the production recipe has `doCheck = false`.

The reviewed exact R feature commit contains both patch and expression. Committed
local R may be built/tested before publication under main's existing native-first
acceptance order; publish that final R commit before W/C consumer pins. There is
no separate native Git dependency to publish. Bind future cooperative **source**
support to the corrected immutable native bytes/package input and existing exact
registration checks, never version text or target capability alone. Browser,
terminal and the separately owned system-native selection must use the same
corrected output. The patched target cannot repair the current source: retain the
single authorized safe initial window/two ordinary stages, preserving held queues
and goals. All implementation/build/pin/live releases remain with main.

##### Native ownership disposition4afbef83: accepted mailbox preservation is distinct

**Superseded product requirement:** the bounded pause/interrupt design92cb873d
below replaces this section's preservation prerequisite and50648f6a's proposed
native carrier. Retain the source findings as history, not implementation scope.

**Bounded result; native source remains unreleased.** Immediate dispatch/queue
inspection resolves why a common task counter alone cannot satisfy full
preservation. The smallest task-accounting mechanism is an internal shared lease
over the existing host permit, transferred across existing submission and task
owners. But accepted native agent mail can outlive all tasks without durable
storage. A task-only patch would leave that work unproved; holding its lease
forever would turn some legitimate non-waking mail into an indefinite shutdown
wait. No preserving mailbox/replay subsystem is designed or released here. This
supersedes50648f6a's unresolved-carrier-only characterization: the carrier is
tractable, while accepted pending-mail preservation is the irreducible additional
contract for the complete workload. Main owns the explicit product disposition.

**Two different queues in exact360319d8.** Durable user queue entries handled by
`ext/queue/src/service.rs` and active goals handled by `ext/goal/src/runtime.rs`
use `start_turn_if_idle`; the shared gate rejects post-HUP starts before queue
removal and preserves the goal row. They need the admitted-task handoff fix, not
a new queue store or indefinite goal wait.

Native inter-agent mail enters through `LocalAgentControl::send_input` for MAv1
delegated input, `submit_inter_agent_communication` for messages/follow-ups, and
`notify_parent_of_terminal_turn` for child results. In particular,
`agent/control/completion.rs:112–141` sends child results with `trigger_turn=false`;
success means queued, not consumed. `agent/control.rs:278–330` accepts non-triggering
mail to an unloaded recipient into `Mailboxes`, or routes loaded recipients via
`ThreadManagerState::send_op` -> `SessionIo::submit_with_trace` -> `Submission`.
`session/handlers.rs:655–665` moves it into `PendingAgentMessage`/`InputQueue`.
`agent/types.rs:58–64` expressly permits queue-only delivery without waking an
idle actor. These are ordinary descendant/message effects in the maintained
workload, not hypothetical foreign sessions or the durable user queue API.

`agent/control/mailbox.rs` stores that unloaded mail only in a mutex-protected
map; `session/input_queue.rs:99–110,208–275` keeps loaded pending mail in memory.
`PendingAgentMessage` serializes the communication when it is eventually recorded,
but that type's serialization is not an independently durable pending-mail queue.
`MessageDelivery::consumed` tracks history consumption through its existing
extension callbacks; neither queue acceptance nor a completed send tool proves
it happened. Eviction transfers pending mail between those memory owners
(`agent/control/residency.rs:69–80`); it does not persist it across process exit.
Tree shutdown closes/discards its mailbox (`runtime.rs:297–301`). The inspected
ordinary shutdown handlers flush existing history but establish no pending-mail
park/restore receipt. No observed data loss is claimed.

**Existing ownership mechanisms and the bounded accounting correction.**

- `AgentExecutionGuard` cannot be reused as the complete drain count unchanged:
  `agent/control/execution.rs` limits/counts only V2 subagents, not roots/MAv1.
  `AgentTreeMembership` owns tree teardown/start membership; closing its tracker
  cancels the tree and closes mailboxes. It is not a cooperative admission fence.
- Retain a shared opaque lease from the existing gate on an accepted request or
  live parent, before the producer releases its own reference. Carry it through
  existing `Submission` alongside residency/delivery ownership, `SpawnInitialInput`
  and the direct delegate call, and `PendingAgentMessage` when delivery is deferred.
  This is memory-only metadata, not a serialized parent ID or a new public RPC.
  Sibling crates may need a small internal shared lease type; no SDK API changes.
- Keep the existing public-request serialization recheck in
  `message_processor.rs:1006–1054`. Requests refused there were never admitted for
  execution. Once accepted into core dispatch, idle shell/compact/review must carry
  that owner rather than reacquire after HUP. Ordinary root and queue/goal starts
  reuse their existing permit. Delegated/review work clones an actual live parent's
  lease before queuing; parent/root-turn strings remain lineage only.
- The lease spans both `task_future` and `RunningTask`/abort ownership as described
  in50648f6a. Registration failure drops its producer owner; normal removal before
  final flush leaves the future owner; cancellation/abort leaves cleanup ownership
  until it and the run end. No extra counter or asynchronous event establishes
  this transfer. Independent new wakes require the existing gate before consuming
  input; already accepted mail/descendants retain their original owner and cannot
  simply be reclassified as rejected work after drain.

That accounting crosses the concrete host dispatch, core submission, agent
delivery/spawn, pending input and task/state seams; it is not a two-file
`start_if_idle` fix. The same files already carry residency and message delivery,
so no replacement scheduler is necessary. Nonetheless, a queue-only item may
intentionally wait for a later user turn. Keeping its lease blocks exit; releasing
it without consumption or a durable parking receipt can lose it. Automatically
waking the recipient to consume it changes queue-only semantics. The existing
internal `suspend_turn_and_shutdown` is not a shortcut: `turn_suspension.rs:82–85`
explicitly clears process-local accepted input/waiters and states that persistence
or replay needs a separate protocol.

**Pre-cutover proof does not close this gap.** Current acknowledgement proof
establishes the exact live pending maintenance call and known foreground effects.
Completed descendant verification proves terminal item histories, closed lifecycle
actions and notLoaded/absent-loaded state. It does not prove receipt/consumption
of every accepted message. A completed `sendMessage`/`followupTask` or child close
does not supply that missing fact; a child result may be queued to an idle root.
`thread/queue/list` is the separate durable queue. The inspected thread status
tracks running turns and permission/user-input prompts, not a complete unloaded
mailbox inventory. Existing observer item membership and `thread/status/changed`
handling provide no exact pending-mail receipt. No authoritative scoped public
empty-mailbox refusal/observable is established. Internal mailbox watches/gauges
and delivery callbacks exist but are not an atomic controller-facing drain proof.
The runtime therefore cannot honestly wait/refuse *only* affected mailbox state
using its current public interfaces; absence of visible messages is unknown.

**Explicit product boundary for main.** Preserving automatic cutover with accepted
non-waking native mail requires native-owned durable park/restore semantics
(identity, ordering, acknowledgement and recovery), beyond the unchanged-format
small patch. Alternatively, preserve durable queue/goal automation but wait or
refuse when native mail is unresolved. That alternative needs a trustworthy scoped
native mailbox/drain observable and fencing of concurrent delivery, or a genuinely
proved no-mail workload; current runtime samples cannot implement it. It is a
narrower mailbox behavior, distinct from the rejected indefinite active-goal wait,
and must be stated to the user. Neither choice is selected by this planning note.
Do not infer successful consumption from actor acknowledgement, delete mail,
force wakeups or ship the task-only patch as full preservation.

If main selects the bounded refusal contract later, deterministic acceptance must
distinguish empty mail, loaded pending mail, unloaded queue-only mail and a late
child result; prove no false empty across transfer/eviction/consumption; retain
existing durable queue/goal behavior and the task/abort ownership regressions from
50648f6a. A preserving park/restore choice instead requires its own sufficient
state/recovery brief before source allocation; no such framework is implied here.
The settled single R-owned patch/build route remains unchanged, but the total
functional native scope is not yet a small task-counter correction. B completes
and freezes its independent runtime package; its full automatic acceptance stays
held. No new source/tests/probes/build/Git or investigation package follows this
finite result. Capacity returns to main.

##### Held activation reconciliation clarification

If `reconcile_codex_update` finds `restart_required` while maintenance completion
is held, refuse the generic restart before portal drain, `quiesce_sessions`,
native adoption or restart. Preserve the existing pending record, startup grant
and exact process evidence and direct recovery to the same owning maintenance
operation. Raise this refusal even with `defer_busy`; `_activate` must not report
completion after an unauthorized replacement was deferred. Restarting native
units alone is insufficient: a consumed grant is not replacement authorization,
and generic quiescence/rescue can reopen clients outside the owner.

The matching no-restart path may perform its existing passive registration
refresh/reconciliation while portals remain held; ordinary nonmaintenance
reconciliation is unchanged. The brief requires no new startup reauthorization
path or replacement machinery. B's focused regression should assert no drain,
quiesce, restart or client restoration, with pending/grant unchanged on the held
mismatch. Existing owning startup recovery settles the failed stage. This is a
bounded clarification of B's released runtime package, not native or live release.

##### Held-completion target admission repair

**Sufficient single-implementer package; design only.** Current runtime baseline
is `fb7820b3ddda043c4e5053201726e0fc02939d78` / tree
`bb9d1dd3843a8322b1ba5bef908b1c272639e89c`. B's accepted source-only finding and
reviewer concern establish that86cd and the new cold-completion owner advertise
the same three maintenance policy1 fields, while86cd `_activate` reopens portals.
SourcePackage routing preserves the source protocol, not target host behavior.
This repair is independent of the native accepted-mail product decision.

**Choose one additive descriptor field:** `maintenanceHeldCompletionPolicy: 1`
in `portal/internal/session/runtime-contract.json`, installed unchanged through
the existing `nix/workspace-portal.nix` descriptor copy. Value1 promises that
target activation/startup and reconciliation keep application writers and actual
stopped clients held for the owning nonterminal maintenance operation, preserve
startup-grant ownership, and leave restoration to that operation. It is not
native pause support, a completion receipt or permission to continue an actor.

Keep `maintenanceStateSchema`, `maintenancePolicy` and `maintenanceMcpPolicy`
at1. Raising maintenancePolicy to2 would also reject existing policy1 readers
and source-owned recovery through their exact equality checks, despite unchanged
journal/MCP formats. Accepting both numbers would still need a specific new
target-behavior rule. The additive field expresses that one rule without a
generic feature registry or state migration.

**Exact admission and implementation owners.**

| Existing file/seam | Required change |
| --- | --- |
| `libexec/workspace-maintenance.rb` | Add one bounded strict target-descriptor predicate requiring integer1, with missing/malformed/unknown values refused. Keep it separate from the existing retained-state reader check. Reuse the same maintenance-transition eligibility as `start_maintenance_switch`; enforce before operation creation, rooting/worker launch, notices, writer drain or HUP. No capability inferred from absent state, old policy1 fields or native version. |
| `libexec/workspace-host#prepare_profile` | Once exact candidate/startup plans establish that this switch will use maintenance, require target capability before admitting that operation. Build/source inspection may precede this, as today; refusal claims no maintenance/profile/service effects, not a wholly side-effect-free preparation. Ordinary nonmaintenance selection/startup has no new requirement. |
| `workspace-host#validate_candidate_preparation!` and maintenance worker | Re-read the capability from the exact prepared target under existing fresh source/token/registry/claim/startup checks before cutover and activation. A prepared boolean is not authority. The worker already substitutes source fields on source recovery; check that actual target. Preserve immutable package binding and all existing admission checks. |
| `portal/cmd/workspace-portal/maintenance_control.go#worker` | In the NEW cold SourcePackage owner, the `prepare` action checks exact operation/prepared candidate consistency and target capability before store creation or observer retain. At `activation-intent`, recheck the actual target after choosing `prepared.CandidatePackage` or, when `SourceRecovered`, `prepared.SourcePackage`, before writing intent. Use one small bounded descriptor predicate with exact supported integer value; no new journal field or dispatcher-wide semantic upgrade. Existing requested/prepared package/native/plans equality remains. |
| `workspace-host#activate` | For an actual nonterminal maintenance operation, verify this executing/selected target's declared capability before `install_links`, service configuration or startup effects, alongside existing owning activation/startup checks. Keep forced `defer_portals`, exclusion of post-reconcile portal start, held generic-restart refusal and delayed restoration. An incapable old target cannot perform this new self-check; the source-side gates are what prevent entering it. |

New cold owners enforce the requirement because they implement that protocol;
an absent own descriptor cannot silently downgrade them to legacy semantics.
`maintenanceProtocolOwner` must continue forwarding operation-scoped requests to
the retained SourcePackage **before** phase/activation interpretation. A new
dispatcher must not retrofit this rule onto an old owner's operation. New target
self-checks govern its own service effects only, and grant no continuation proof.
New source recovery must satisfy the capability from its own exact package; no
fallback to CandidatePackage or latest profile is allowed.

**Compatibility and migration.** There is no on-disk conversion, new marker or
journal-schema change. Legacy policy1 operations stay with their retained source
and old protocol; the additional field does not purport to repair them. A new cold
source refuses86cd or any missing/unknown-capability maintenance target before
pause/cutover. A capable target remains usable for ordinary startup and the
historical first-stage public candidate switch; startup-only records without an
operation do not become cold-completion operations. Existing first migration,
source native prerequisites and forward-only recovery remain unchanged.

One mechanical compatibility dependency must be included: archive and
failed-creation recovery compare whole runtime descriptors through
`maintenance_predecessor_contract` (`workspace-host#require_archive_recovery_contract!`
and `#require_failed_creation_recovery_contract!`). For these unrelated
lifecycle-recovery comparisons only, validate the new field as absent or exact1,
then omit it from both comparison projections. Keep current executing-target
descriptor equality and every other historical contract/identity check intact.
Do not insert a default1 into a descriptor or reuse that projection for maintenance
target admission. Malformed or unknown present values still refuse. This preserves
the existing historical recovery contract without treating a missing target
capability as support; it adds no recovery action or permission.

**Required focused regression and quick scope.**

- In `test/workspace_host/maintenance_test.rb` (and existing transition fixture
  helper only as needed), prove new-source -> legacy/missing/0/unknown/string/
  float/bool capability refusal before prepare-operation/worker/notices/drain/HUP/
  profile/service events. Preserve the original failure evidence. Prove exact1
  capable target stays held through `_activate` and reconciliation until the
  existing completion/restoration path. Ordinary nonmaintenance startup and
  startup-only bootstrap remain supported.
- In existing `portal/cmd/workspace-portal/maintenance_control_test.go`, cover
  prepare refusal before creation/observer effects, both actual activation target
  branches, changed prepared target, incapable
  source-recovery target, and old-source forwarding without reinterpretation.
  The source owner rechecks capability before intent; destination proof and Stop
  tests retain their scope. Do not duplicate the history/observer suite merely
  to test a descriptor number.
- Extend the existing archive/failed-creation descriptor comparison tests only
  for absent/exact1 compatibility and malformed/unknown rejection. Run those
  focused Ruby lanes plus maintenance/profile/held-start lanes, focused Go
  command/control/startup tests and the shared session-contract tests. Use the
  declared Nix environment; JSON/Ruby/Go formatting and diff checks are quick.
  Compile the changed activation fixture with its actual
  `live_switch_integration` tag if relevant sources/fixture bindings change;
  compile-only remains distinct from executing it.

One implementer owns descriptor, Ruby/Go admission, focused tests and the small
documentation update. Add the capability/mixed-version refusal to
`docs/workspace-updates.md`; link the target requirement from
`docs/maintenance-mcp.md` without duplicating protocol history. Mention that
policy1 reader compatibility alone does not certify held startup. Main owns
allocation, final prose and Git. After committed quick checks, the existing
affected independent review must cover this new compatibility contract and the
two descriptor-equality consumers; the deletion-only review remains valid for
its separate scope. Required final packaged/activation acceptance must include
legacy-target refusal and capable-target held success on the exact final package.
No new native run is released by this design, and the pending native-mail decision
still limits full automation acceptance. No blocker remains for implementing
this target-admission repair within that boundary.

##### R1 activation rescue boundary

The existing method-wide `activate` rescue can stop/remove an already present
autoarchive timer after the new held-capability check refuses. That is a service
effect and contradicts R1's target-side pre-effect refusal. Earlier source-side
checks do not excuse this independent activation boundary.

Use one invocation-local activation-effects flag: false at method entry, set
true immediately **before** `install_links`, the start of the existing activation
mutation block. At rescue entry, re-raise the original error unless that flag is
true; otherwise retain the existing timer cleanup and error handling unchanged.
Setting it before the call preserves cleanup if `install_links` fails partway.
Do not key cleanup on successful return, capability presence or a preexisting
timer link. This scopes timer compensation to an invocation that entered
activation effects; it is not generic rollback or a claim about all preparation
effects elsewhere.

Extend the refusal regression with an actual preexisting timer symlink and assert
that capability refusal leaves it intact and calls neither `install_links`,
service configuration, archive stop/removal nor daemon-reload. Retain/add one
failure after activation effects start proving the original cleanup still runs,
including partial `install_links` failure. B owns this narrow R1 correction and
focused Ruby checks after main's release; unrelated source stays frozen. No
native, startup-grant or journal contract changes are needed.

##### Replacement92cb873d: bounded pause, interruption, activation, resume

**Current sufficient contract; supersedes the strict maintenance protocol.**
The user's latest instruction is: “we pause active threads, wait for them to
settle... if they don't in a given timeout, we interrupt them. we activate the
new workspace, we send them command to resume.” This applies to participant
parents as well as native children. The responsible thread alone decides whether
to restart a child. No further product decision is outstanding. Baseline is
reviewed R40c342f924561d6ed3f3632bdff8463ce8bb2d3d/tree4b163546f23ade0468004c086c5a66059dfeba65;
architect0's session/environment and saved Astra/xhigh/workspace_write match.

Remove uninterrupted-turn, exact maintenance-MCP finish, complete parent/child
history, lossless transient child-mail and native admission-lifetime requirements
from release scope. This replaces2227+'s cold-completion prerequisite and the
native proposals50648f6a/4afbef83; EOF1857+ remains abandoned. Do not implement
the Rust patch, inherited lease, mailbox persistence, flush barrier or new SDK
surface. Interrupted commands can have partial effects; the resume instruction
must tell the actor to inspect its saved state and actual effects before retrying.
The controller preserves its own delivery identities, not transactional execution
of arbitrary agent commands. Durable user queue/goal rows and saved conversations
are retained; maintenance never clears them to obtain an idle result.

**One existing worker executes the following sequence.**

1. Keep ordinary prepared-candidate/profile/claim validation and the existing
   maintenance admission hold. Capture active registered roots and ready roster
   members once, with their workspace/incarnation/thread identities and current
   Stop revision. These independently registered members each receive their own
   resume command. Native descendants are owned children, not new participants.
   Ancestry may explain their loaded presence without overriding retained roster
   or monitor ownership. Unknown/ambiguous ownership is an ordinary reported
   preparation failure, not permission to interrupt unrelated work.
2. Persist one pause deadline before sending notices. Use a documented positive
   `--pause-timeout` in seconds, default90, captured in preparation; persist the
   absolute deadline so worker recovery cannot restart the grace period. Existing
   `WaitDuration=90s` is a renewable MCP wait and is removed, not reused as an
   endlessly renewed timeout. Send the pause/checkpoint request with existing
   `Client.ConditionalSteer` and the saved NoticeID to the captured active turn.
   Ask it to save useful context, settle or interrupt child work, and finish its
   current turn without starting more work. No acknowledgement/tool call is
   required. A turn that already ended needs no new pause turn. Preserve the
   existing notice receipt/unknown-outcome handling; it cannot extend the deadline.
3. Poll `ReadTurnState`/`ActiveTurnID` until the captured threads have settled or
   the deadline expires. Completed, failed or interrupted turns can settle; no
   successful-turn requirement, item census or completedAt proof is added.
   Queued input or an active goal is not a reason to wait indefinitely. At the
   deadline interrupt remaining active participant threads and identified owned
   children using existing `turn/interrupt` (Client.Interrupt, or Request with
   the just-read exact turn ID). A successor on the same captured thread remains
   within this interruption scope. Re-read a no-active-turn race; report real
   RPC failures through the existing recovery path. These maintenance interrupts
   do not invoke user Stop/suppress-resume. User Stop still does.
4. Drain application writers and quiesce actual managed clients through the
   existing host paths. Stop the captured source native units through ordinary
   systemd shutdown, then activate the prepared workspace through
   `activate_candidate`/`complete_candidate_activation`. Existing service stop
   has a150-second bound; use it rather than adding a second cleanup framework.
   Normal service termination handles remaining native work, including children;
   known background processes use existing termination/cleanup paths. A reported
   stop/cleanup failure or remaining owned process is a recovery error, not a
   successful switch. Do not require HUP, a queue-start probe, exit0, transport
   close classification or a native internal-accounting certificate. Do not
   expand service termination into a claim that remote external effects rolled
   back. Preserve ordinary pending-target/forward recovery on activation failure.
5. Only after activation and its existing socket/registration checks succeed,
   send one saved resume command to each captured participant not suppressed by
   Stop. Keep `AdmitContinuation` as the existing locked Stop/delivery boundary;
   derive eligibility from captured activity plus successful activation, not
   Finished/FinishPublished. Use `SendWithOptions` with the existing stable
   ContinuationID and `ReconcileSendWithOptions` on uncertain replies. This
   existing sender starts or steers as appropriate; queue/goal presence does not
   replace the requested resume command and is never deleted. Recheck retained
   identity; never substitute another thread. Unknown delivery remains recoverable
   under the same ID, never a fresh duplicate. Restore clients actually stopped
   and clear the existing admission hold. No child restart or pane-presentation
   completion obligation is added.

Normal activation's existing `defer_portals`/owned restoration may keep clients
held until resume admission is settled; retain that small ordering mechanism,
not passive history proof. Ordinary non-maintenance activation is unchanged.
Worker restart resumes the saved phase/deadline and stable deliveries. A failed
switch sends no resume commands. An explicitly recovered successful activation
can resume them. Pre-cutover Cancel restores the source and cancels the pause;
any necessary resume uses the same captured identities/delivery rules and honors
Stop. Do not automatically resume in a generic error handler.

**Single-implementer removal and replacement boundary.** Reuse the current Ruby
host worker and Go journal; no parallel controller or event framework.

| Existing owner | Required simplification |
| --- | --- |
| `libexec/workspace-maintenance.rb`, `libexec/workspace-host` | Replace await-ready/retained-observer/HUP/finish/cold-proof orchestration with the sequence above. Keep candidate preparation, token/claim, ordinary service and activation failure handling, pending target and stopped-client restoration. Remove maintenance-MCP launch injection and its readiness dependency; keep existing generation/startup ownership where ordinary package selection still uses it. |
| `portal/cmd/workspace-portal/maintenance_control.go`, `maintenance_cutover.go` | Keep capture/identity/status/cancel/worker ownership and stable notice/continuation delivery. Replace awaitReady/drain with bounded polling/interruption and ordinary shutdown status. Delete `adapter`, `proveDestinationSources`, `verifyColdServices`, exact completed-source checks and the `ContinuationKind=activation` queue/goal shortcut. Keep actual destination identity and successful activation checks. |
| `portal/internal/maintenance/{types,store,controller}.go` | Keep one operation journal, captured participants, deadline, Stop revisions, delivery outcomes and activation/recovery phases. Delete acknowledgement leases, renew/wait/finish publication and completion-derived continuation validation. `SuppressResume` and `AdmitContinuation` remain small transactions. |
| Strict-only maintenance files | Delete `maintenance/{admitted_wait,observation,native,native_effects,terminal_statusless,owner}.go` and command-side `maintenance_{mcp,observation,owner}.go` once their obsolete callers are removed. Delete their dedicated tests. Remove maintenance observation/freeze plumbing from `web/activity_maintenance.go` and `activity.go`; preserve normal activity monitoring and the independent wakeup/monitor deliverable. |
| `maintenance_terminal.go`, `maintenance/terminal.go`, `restoration.go`, `libexec/dev-session` | Keep ownership/restoration of clients actually stopped. Replace `terminal-intent`'s strict safe-point authorization with captured operation/identity and bounded-pause phase authorization. Remove presentation/reattachment proof as transaction completion. Keep ordinary lifecycle/archive checks unchanged. |
| Maintenance startup/registration consumers and docs | Remove direct `maintenance_ready` registration/configuration, mandatory tool availability and corresponding launch tests from new operations. Keep general team-reporting/MCP settings and ordinary registration consistency. Update `docs/workspace-updates.md` and replace the obsolete blocking-MCP contract in `docs/maintenance-mcp.md` with a link/explanation of the pause workflow; remove stale instructions to finish/join every child or await exact acknowledgements. |

Two concrete integration seams must be changed, not bypassed accidentally.
`workspacecodex/transition.go#RequireThreadExecutionIdle` refuses nonempty queues;
it must remain strict for ordinary callers. The already existing
`DEV_WORKSPACE_MAINTENANCE_OPERATION` branch in `dev-session#quiesce` can use the
bounded worker's operation authorization instead, preserving queued/goal state.
Likewise `@maintenance_drained` must mean ordinary owned shutdown succeeded in
the new worker, not a fabricated old HUP/exit-proof chain. The worker must not
fall back into an unbounded “wait for every queue to empty” branch.

**Compatibility without two implementations.** Retain SourcePackage dispatch;
old operations finish/recover under their immutable old owner, never acquire
timeout-interruption semantics from a newer profile. Removing strict journal
fields requires one version change to the existing private operation format,
not a migration framework: new operation schema2, existing request transport
unchanged. Resolve a bounded identity envelope (schema, operationId, profile,
SourcePackage) before source-owned semantic decoding; current
`maintenanceProtocolOwner` calls full `Store.Load` and therefore needs this small
adjustment. Global active/status must use the same owner routing. No rewriting
old records or mixed interpretation of Finished is allowed. Advertise the new
behavior with existing `maintenancePolicy=2`/`maintenanceStateSchema=2`, retain
held-start policy1 where used, and stop advertising required MCP policy1 for the
new launch. Keep narrow mixed-package refusals before effects; old active
operations must settle under their old owner before beginning this new flow.
No database migration, native version, SDK revision or package fork is needed.
The previously authorized initial coordinated window remains available for an
old source lacking this worker; the strict MCP/native fix's mandatory two-stage
upgrade is no longer a requirement of the new design.

For the two unrelated whole-descriptor comparisons in
`require_archive_recovery_contract!` and
`require_failed_creation_recovery_contract!`, replace defaulting strict1 fields
with a scoped validation/projection: schema/policy are both absent or the exact
integer pair(1,1) or(2,2); reject partial, mixed and unknown pairs. Optional MCP
and held-completion values must each be integer1. Omit only those maintenance
fields from these two equalities; keep the executing full descriptor equal to
RUNTIME_CONTRACT and preserve every unrelated contract check. Retain the existing
absent-contract/retained-maintenance-state refusal or its established owning
recovery gate. This projection grants no maintenance reader, target or startup
authority; actual new target admission remains schema2/policy2/held1.

Legacy admission/Stop also uses that owner boundary. `RequireAdmission`,
`SuppressActive` and web `recordMaintenanceStop` must not decode schema1 with
the new `Store.Active`. Resolve its Identity and request bounded schema1
`status` for that exact operation from its retained SourcePackage. Validate the
common operation/profile/source identity, status/phase and workspace/thread
membership only. Complete/cancelled releases the fence; other owner phases keep
the workspace held. Unavailable/malformed owners remain errors. Recheck active
identity before using a terminal response; preserve missing-pointer/nonterminal
journal refusal. Forward Stop's `suppress-resume` to that same owner before
package exclusion, without reading Finished/deadline or rewriting its record.
The same common projection must serve `Store.Create`'s occupancy check: a retained
terminal schema1 pointer cannot permanently prevent a new operation. Existing
terminal pointers need no manual clearing or conversion. Cover terminal legacy
admission/new creation, live legacy Stop forwarding, workspace isolation and
owner failure alongside unchanged schema2 behavior.

The schema2 admission hold covers the entire validated profile, including
registered native units inactive at capture. `Services` remains the captured
shutdown set, not a membership exemption in `RequireAdmission` or Ruby
`maintenance_native_admission!`. Target startup uses only existing exact owning
activation grants; retain their normal consumption/revalidation. This adds no
participants, registry snapshot or resume recipients. Keep operation-owned
control and user Stop usable, preserve schema1 owner-status workspace membership,
and do not fence unrelated profiles. Check inactive-unit source-start refusal,
exact target grant success, missing/wrong grant refusal and terminal release.

**Acceptance and cost.** One implementer owns the coherent runtime deletion,
worker replacement, necessary shared-call-site fallout, docs and focused checks;
main allocates that package. Test a cooperative participant and a noncooperative
participant interrupted at the persisted deadline, including worker restart;
an active child interrupted without automatic restart; independent roster members
resumed individually; durable queue/goal rows retained without idle waiting;
user Stop before/after resume admission; unknown resume reply reconciled without
duplicate delivery; ordinary stop/activation failure causing no resume; and
legacy source-owner routing. The native fixture must exercise this sequence with
the canonical existing native/SDK and ordinary activation, including one queued
and one goal case. Replace obsolete strict-proof assertions, not merely their
expected failures. Keep unrelated original wakeup/monitor tests and shared
package/recovery checks. Run affected Go/Ruby/registration quick checks, then
independent review of the committed functional replacement before real native/VM
acceptance under main's allocation. No new test harness, diagnostic campaign or
Rust build is needed. This removes core responsibilities as well as peripheral
lines; exact deleted size belongs to the implementation diff, not a design promise.

The obsolete strict `nix/tests/workspace-maintenance.nix`,
`test/maintenance_model.py`, `test/maintenance_transport.py` and their flake check
export may be removed with this replacement, without building a new VM harness.
Remove the native fixture's `vm-parser` subtest dependency on that Python file
and update `test/README.md`; tagged compilation alone cannot catch the runtime
file dependency. Remove dead predecessor factory bindings with the export;
main owns any now-unused historical input/lock pruning. Preserve independent
monitor acceptance and ordinary activation/recovery tests. The removed VM also
covered actual Ruby worker/systemd/profile activation: an injected local native
fixture does not replace that evidence. Main must allocate bounded real-host
activation and failure/no-resume acceptance before full automation readiness;
deletion neither waives it nor automatically expands B's package into a VM rewrite.

No demonstrated API inability blocks this conventional sequence. The known
native internal handoff/mail uncertainties do not justify reinstating the rejected
guarantees. Actual operation failures remain visible recovery failures. This is
the finite design deliverable, not source, interruption, lifecycle, build or
deployment release. Capacity returns to main.

##### Review remediation bb68de0b: bounded pause I/O and cancellation resume

**Sufficient correction to92cb873d, pending main's consolidated allocation.**
Reviewer scope is frozen R1c06628c. The ordinary replacement protocol stays;
these two defects add no native, SDK, journal format or controller requirement.
Session/environment and saved architect Astra/xhigh/workspace_write were verified.

**Bound existing synchronous calls.** In `maintenance_pause.go`, use a five-second
deadline per logical native operation, matching `maintenanceMonitorInventory`'s
existing convention. The cap covers the whole `ActiveTurnID`, `ConditionalSteer`
(including its internal reconciliation), `maintenanceChildren` enumeration,
`maintenanceInterrupt` (read/request/race recheck), or notice retirement call,
not five seconds afresh for every nested RPC. Derive deadlines from the caller
context and always cancel each derived context immediately on return. Preserve
normal client Close; the pinned SDK uses CloseNow, not a close-handshake wait.

Keep the saved absolute `PauseDeadline` unchanged. During cooperative waiting,
each operation is bounded by the earlier of that deadline, now+5s and its caller
deadline. Recompute expiry before each operation/participant and before advancing
phase; the current once-per-outer-loop `expired` value is insufficient. Once
grace expires, stop sending pause notices and use an interrupt/reconciliation
context with one shared30-second allowance for the whole remaining pass. For a
call entered before expiry, its final bound is saved PauseDeadline+30s. An explicit
recovery invoked after that deadline gets one fresh30-second recovery attempt,
immediately in interrupt mode; it never resets PauseDeadline or enters another
cooperative wait. Do not renew the allowance per thread, page, error or loop.
An exhausted allowance returns recovery-required; no automatic internal retry
loop turns it into an unlimited wait.

Check persisted `CancelRequested` before and after every bounded logical call
and between participants/services; keep the existing250ms wait interruptible by
the caller context. Thus a persisted Cancel is observed within at most the
current5-second native call plus normal local bookkeeping, rather than after an
unbounded RPC or all participants. No watcher goroutine or new scheduler is
needed. Once observed, do not start another steer/interrupt or advance to
draining-writers; return through the existing cancellation path. The final
journal update must recheck Cancel under its existing lock. Parent context
cancellation returns promptly too. Never hold the journal lock across native I/O.

Distinguish these outcomes:

- Grace expiry itself is normal: change to the bounded interruption pass. If a
  passive read/enumeration was cancelled solely by the grace boundary, discard
  the incomplete result and perform any still-needed read in that pass. It did
  not prove settled or empty. A shorter caller deadline/cancellation wins.
- A five-second RPC timeout before grace expiry, an interrupt/reconciliation
  timeout, or exhausted30-second allowance is a real operation failure. Return
  to owned recovery without paused/sources-stopped/activation/resume success.
  An interrupt timeout is not the existing natural-completion race; never turn
  its error into success using the same cancelled context.
- A timed-out/cancelled steer retains the original NoticeID, action and SDK
  ledger. Honor the SDK's known-unsent versus unknown result; never reset a
  submitting row or create a replacement ID. Persist unknown disposition and
  return recovery when it cannot be reconciled, including at grace expiry.
  If Cancel was observed, preserve that uncertainty for cancellation cleanup
  instead of reporting cancellation complete.

Use a separate bounded context (at most5s, no native calls) to save an uncertain
notice/result after the RPC context expires. Prefer the still-live caller;
only local result bookkeeping may detach from caller cancellation, and it must
remain bounded. If that save fails, return the error and leave the SDK's durable
attempt authoritative. Do not reuse an expired RPC context for the save or give
reconciliation an unbounded background context.

`maintenance_notice_cleanup.go#cancelNotices` also needs one shared30-second
attempt and capped retirement calls, so returning cancelled cannot enter a new
indefinite cleanup wait. Stop after budget exhaustion and retain
notice-cleanup-unresolved/recovery-required. The existing command boundary in
`maintenance_control.go` must preserve a concise timeout/unknown-outcome reason
in its existing error response instead of flattening this to an identity failure;
Ruby's ordinary worker rescue records recovery. Do not impose a fixed5/30-second
timeout on the whole90-second cooperative command, retrofit historical owners,
or broaden this correction into all maintenance/SDK operations.

**Serialize cancellation resume with Stop.** In
`libexec/workspace-maintenance.rb#maintenance_cancel_restore`, keep notice cleanup
and its uncertainty handling. Run the subsequent `continue` call inside existing
`with_transition_lock`, exactly as normal resume does. Inside that lock, freshly
inspect the same operation and require the exact recorded source package and
source profile token to match `File.realpath(@profile)` and `profile_link_token`,
with cancellation still owned and no cutover; refuse before continuation on
mismatch. Keep the exclusive lock through continuation admission and native
ActivateThread/SendWithOptions return. Release it before ordinary restoration's
own lock; no nested lock or new lock order. Preserve user Stop recording intent
before waiting for the shared transition lock and the existing final StopRevision
check/stable delivery. If Stop arrives after the final check, it can record intent
but cannot complete its native interrupt until this dispatch exits the exclusive
section. If it arrives earlier, continuation is suppressed. Do not place Stop
intent itself behind the lock or manufacture a new continuation ID.

**Files/checks and ownership.** B's eventual consolidated fix owns
`maintenance_pause.go`, `maintenance_notice_cleanup.go`, the narrow error/context
fallout in `maintenance_control.go`, `workspace-maintenance.rb`, their existing
Go/Ruby tests and a short timeout paragraph in `docs/workspace-updates.md`.
Use connected fixture peers which complete initialization then withhold responses
for turn reads, steer, child-list and interrupt separately. Assert bounded return,
unchanged saved deadline, no false settled/activation, and retained unknown steer
identity. Exercise normal grace expiry into interruption, a caller deadline,
persisted Cancel during an outstanding call, cancellation cleanup timeout, and
late explicit recovery without a renewed grace period. Use short test-local
durations/deadlines with a generous outer guard; no real30/90-second sleeps or
new harness. For Ruby/Stop, hold cancellation continuation after admission, record
Stop, prove its shared-lock native interruption cannot finish before the pending
dispatch returns, then verify no later resume; also test changed source package
and token refusing before continue and ordinary cancellation/restoration success.
Run only affected quick scopes after main releases source. Final affected review
and later acceptance remain main-owned; no tests, application edits, Git, native
or build execution occurred for this design package. Capacity returns to main.

**Third correction, retained-claim source recovery (d1975ab8).** The two fixes
above remain settled. In the current worker, a changed invocation after cutover
but before activation intent records `SourceRecovered`; Ruby substitutes the
saved source target and calls `validate_candidate_preparation!`. Its existing
claim predicate accepts that substitution only after activation intent, creating
an ordering cycle. Do not move activation intent ahead of validation or bypass
the retained coordination attempt with a direct claim.

In `libexec/workspace-coordination-host.rb#require_coordination_profile_claim!`,
retain ordinary candidate matching and all existing job-kind, claimed-state,
attempt, reservation-owner/state and blocked-recovery artifact/history checks.
Extend only the existing maintenance source-recovery target alternative to admit
the pre-intent validation stage under transition exclusion. Read the exact
operation through its existing owner. Require nonterminal `SourceRecovered=true`,
`CutoverIntent=true`, `ActivationIntent=false` and no conflicting activation tuple.
Bind operationId to the current maintenance operation and the saved preparation's
switchOperationId; its coordinationAttempt must equal the retained job attempt.
Bind the original candidate to both the saved preparation and job snapshot,
and sourcePackage/candidate argument to the saved sourcePackage. The operation's
profile must be this host profile; saved sourceProfileToken, preparation
profileToken and job expectedProfileToken must agree and still equal the fresh
profile token, with the selected package still the exact saved source.

Use the existing prepared-artifact identity/digest check to bind this tuple to
`job.snapshot.operation.preparedArtifact`: recorded preparation ID and original
artifact contents must agree, excluding only the already appended
coordinationAttempt when comparing/digesting the saved preparation. Do not accept
an arbitrary source path merely because sourceRecovered is true. Source native,
registration plans, registry and source-content checks remain in the existing
subsequent `validate_candidate_preparation!` and activation-intent consumers;
use the unmodified saved preparation for ownership checks, not Ruby's substituted
local target view. An already written activation intent retains its existing
exact-source activation-tuple path; do not apply the pre-intent source-token rule
to unrelated forward-target recovery.

Do not require sourcesStopped at this early validation seam: worker loss can
precede recording ordinary shutdown success. The existing source-current/stop/
process verification must still run, and activation-intent remains after
sources-stopped and full candidate validation. The correction establishes claim
ownership for validation; it neither certifies shutdown nor authorizes immediate
effects. No reservation rewrite, new state, authority or coordinator mechanism
is introduced. Retain normal mismatched-candidate refusal.

Add one composed regression using the existing Ruby maintenance worker and
coordination fixtures with the real `require_coordination_profile_claim!` and
preparation validation, no direct DEV_WORKSPACE_CLAIM_ID and no stub of that
predicate. Model worker replacement with cutover owned, source selected and no
target intent; exercise the saved-source substitution through validation, ordinary
shutdown verification and then source activation intent under the retained
attempt/reservation. Assert validation precedes activation intent and original
candidate/artifact/attempt/reservation remain unchanged. Include mismatched
source/profile token, operation/attempt/artifact and missing source-recovery
authority refusals; retain existing ordinary-candidate and blocked-recovery
owner/state negative controls. Only the claim method and directly affected
`test/workspace_coordination_test.rb`/`test/workspace_host/maintenance_test.rb`
fixtures join B's consolidated correction boundary. No broader coordination
audit or source release follows this note. All three corrections are now covered;
capacity returns to main with source1c066 and Git still frozen.

### Next acceptance9c686052: bounded native flow, packaged switch, initial rollout

**Binding and disposition.** Planning only. Current/environment match this
session; retained architect0 is Astra/xhigh/workspace_write. Main accepted
R`ea8774d6cd27761ffbb009e7da3871e18d9304fa`, tree
`6d6d4e2e1b8583a2fc392eef768b29dc161c927b`, parent38967, and closed R1/R2/R3
under review step9 against committed packet7dffeb52. Those fixes are not reopened.
No execution or application edit is authorized by this brief. W/C still select
earlier f161: neither their old packages nor old composed positives establish
acceptance of this replacement. The shortest sequence is the native fixture,
the missing packaged-switch cases in an existing fixture, final matching W/C
composition, then the already authorized initial host/profile window.

**1. Existing native acceptance, independently runnable after main allocation.**
From the exact reviewed R checkout, use the declared Nix shell and pinned module:

```sh
nix develop --command env GOWORK=off \
  LIVE_SWITCH_CODEX=/nix/store/2rqwqchjlv6l2nw5l491pkhvrsijn50c-codex-package-0.165.0/libexec/codex/bin/codex \
  go -C portal test -mod=readonly -tags=live_switch_integration \
  -run '^TestNativeWorkspaceBoundedPause$' -count=1 -failfast -timeout=10m -v \
  ./cmd/workspace-portal
```

Retained binary SHA256 is
`647b0157e6472a793e0a0bd45bc44ef8ade673b6d8f3db4118260acda4976652`, Codex0.165.0;
SDK is c3c2adb705f5ff6bb42c98bd44be3649fd93bedb/module
`v0.0.0-20261105132033-c3c2adb705f5`. Check that retained input at execution;
absence means preparation is needed, not permission to substitute another native.
Keep the existing five cases: four code-mode/strict combinations and timed
interruption. Each has90seconds and a one-second fixture grace. The fixture
uses private `/tmp/wmn-*` homes/sockets, the actual native and an embedded
synthetic Responses server; it needs no external inference or credentials.
It tests production pause, ordinary owned TERM/restart, retained queue identity
and active goal before target activation, actual resume delivery and stable
replay. It manually supplies activation/registration state: this is explicitly
not Ruby, systemd, real profile selection, Stop-race or activation-failure proof.

Budget up to7.5minutes for the cases plus shell/startup; the explicit10minute Go
cap bounds the test process. Setup/version and deferred native join do not all
share the case context, so the executor must retain exact subprocess ownership
and reconcile teardown on timeout; a killed runner is not a clean pass. Use the
normal fresh verification watcher. Stop the batch on first failure, preserve
its log and exact source/command/binary bindings, and investigate before retry.
No new diagnostics/census or production deadline changes are needed. Existing
accepted connected-silent RPC, cancellation/Stop-lock and claim regressions
remain evidence for their scopes; do not rerun them merely because of this plan.

**2. Real Ruby/systemd/profile coverage is still missing.**
`test/workspace_host/maintenance_test.rb` uses host/service doubles;
`test/workspace_coordination_systemd_test.rb` runs a real user manager but tests
coordination workers, not maintenance profile activation. The existing
`session-recovery-boot` VM exercises real native units and failure drop-ins for
provider changes, not this switch. Running any of these unchanged cannot fill
the deleted strict VM's packaged-maintenance coverage. Do not revive its
MCP/HUP/history assertions or add another VM/model framework.

The smallest sufficient separate source package is to extend
`nix/tests/session-creation.nix` with bounded package-switch subtests, reusing its
real disposable developer user/profile, systemd host module, managed roots/team
creation, `test/creation_model.py` hold/release/request log and existing portal
and native read helpers. No new model is needed. Reuse `mkPackage` for two
immutable fixture packages with the same native/SDK and a valid declared native
registration change (e.g. catalog capacity4→5), plus a store-backed fixture
source selecting the target. Include both closures/source in the guest store;
use real preparation/build and public switch, not patched registration markers
or direct maintenance journal seeding. Confirm the prepared registration really
requires restart. A no-op same-invocation switch is not this acceptance case.

Keep this extension within that existing Nix fixture and only immediately needed
assertion/RPC helpers in `test/creation_transport.py`; retain all existing cases.
Main must separately allocate, review and commit these test changes. Production
source is unchanged; bind the resulting test commit and package derivations
instead of calling the extended fixture an ea8774d6 execution. The existing
entrypoint remains:

```sh
nix build --print-build-logs --out-link OWNED_RESULT/session-creation \
  .#checks.x86_64-linux.session-creation
```

The subtests invoke the selected `workspace-host switch --source SOURCE
--enable-maintenance --pause-timeout 2`, inspect `maintenance status UUID`, and
use `maintenance recover UUID` for the same failed operation. Exercise:

- Cooperative release and deadline interruption through the actual
  `workspace-maintenance@UUID.service`, ordinary source stop, real profile
  selection, held target startup and resume of captured roots/ready members.
  Existing held model responses provide both behaviors. Check actual resume
  input and stable delivery identity; children receive no automatic restart.
- Stop one captured participant through the existing user Stop endpoint before
  continuation; its resume remains suppressed while another participant resumes.
  Retain queue/goal identities and saved conversations through the switch;
  a preserved queued item legitimately consumed later is not data loss.
- Fail target native startup using a fixture-instance-only systemd drop-in,
  following `session-recovery-boot`'s existing `ExecStart=false` pattern. Require
  a real failure/recovery status, no resume input and retained operation/profile
  ownership. Remove only that fixture fault, recover the original UUID, and
  require successful ordinary recovery before any resume, without duplication.
  Do not assert rollback when the profile has already selected the target.

Fixture clarification: use a bounded, fixture-user-only `ExecStartPost` hold on
`workspace-router.service` for the passive pre-resume observation window. This
supersedes the earlier native-unit hold suggestion: native startup grant
consumption requires that native unit's ControlPID be zero, so a native
ExecStartPost changes the admission being tested. Keep the router active when
installing its drop-in, without restarting it; activation's first `enable --now`
then leaves it running, while its subsequent synchronous `try-restart` holds
`_activate` before completion/continuation. Observe the hold's entered marker,
exact target native process/socket, active native unit and zero native ControlPID
before passive reads; Type=simple active alone does not prove grant consumption.
The socket is created after `run-codex` consumes that grant and execs native.
Use direct fixture native reads, not the held router/portal. Bound and release
the helper before normal startup timeout, with fixture-only cleanup on failure.
This is a guest activation delay, not a product mechanism. Source user Stop
still occurs in the earlier captured/pausing window before portal writer drain;
the router hold cannot reopen that window. No production or additional fixture
files are needed for this correction.

**R2 actual-client restoration correction (a21b401b).** Against committed
Rbf4de3da0ed4abcb6e66188ef146d9d34bd59918, `switch_done` currently proves service
and journal completion only. Its ordinary-client claim needs the following
observation, not another production change. Exact VM/transport source reads use
D's retained bf4 copies (VM599ea499, transportb5be983d); D's separate R1 working
edit remains untouched. Reuse the existing `checkpoint("automatic")` root for
all three maintenance cases, including startup failure/same-operation recovery.
The earlier explicit-fork subscription case does not establish this root's client.

Before each case submits its held work, run ordinary selected-profile
`dev-session sync SLUG --as-is` from the guest workspace to ensure this already
created managed session's client is running. This is source fixture setup only;
no new session, manual pane command, authority edit or private helper. Read and
retain the real source tuple via `tmux -S RUNTIME/tmux.sock display-message -p`
for the exact managed session/pane: session ID/name, managed mark, workspace/slug,
identity token, `@dev_session_codex_thread`, `@dev_session_codex_socket`,
`@dev_session_codex_pane`, pane ownership, current command and pane PID. Match
thread/slug/socket against the existing creation record. Require a live ordinary
native client, not a shell with stale tmux options. The pane PID is normally its
shell: a small read-only helper may inspect that pane's process descendants and
their `/proc` stat/exe/cmdline, requiring exactly one matching live native client
with the pinned executable and `--remote unix://SOCKET resume ROOT` arguments.
Retain its PID/start time to distinguish the old process from a replacement;
do not search unrelated guest processes or infer the client from pane text.

Bind exactly one matching `terminalIntents` entry in the public exact-UUID
maintenance status to workspace/slug/root and the captured root participant's
nonempty incarnation. Other existing session intents may remain. This is an
intent before `quiesce_native_client!` respawns the pane, so also observe that
same managed pane at the router barrier now runs the configured shell, with no
matching native client and the saved source process identity gone. In the
failure case assert this already at the original `recovery-required` boundary,
then again at the recovered router barrier under the same operation UUID. Keep
the existing no-resume-on-failure checks. No direct private-journal read/write
or Preparation access is needed.

After `switch_done`, bounded passive polling must observe an ordinary native
client again in the same retained managed session/pane/token, with a new process
identity, the exact prepared target executable supplied by R1, and the same
remote socket path/root arguments. The existing native `thread/read` must still
return the retained root and expected thread cwd. Keep the matching terminal
intent and restoration.completed checks, but neither substitutes for the live
client observation. Repeat the observation after completed-operation recovery
replay. Do not invoke sync/start/attach/resume/send-keys during these observations:
the worker's existing `restore_quiesced_sessions` → `dev-session sync` must own
restoration. The root is not the member selected for user Stop, preserving that
separate suppression case. This verifies ordinary client process/session
restoration, not screen layout, focus or a rendered-terminal guarantee.

Scope remains `nix/tests/session-creation.nix` plus only the read-only observation
and assertion helper needed in `test/creation_transport.py`. Preserve all prior
cases, finite polling budgets and the router barrier; guest teardown owns the
existing client, with no additional host/peer lifecycle cleanup. D can extend
its existing quick Python predicate control under the declared Nix shell: a
complete journal with matching intent but a shell/absent native client must
fail; a correct independent live observation passes, and a wrong-root client
fails. Exercise the actual consuming predicate with these local data, not a
stub returning “restored”. Existing Python/embedded-Nix-script syntax checks
cover the small change; only the later existing VM execution establishes real
stop/restore. No new fixture/harness or production gate is needed. Main owns
release of R2 alongside D's R1 correction, affected review and VM allocation.
This sufficient brief returns architect capacity; no application/check/Git or
lifecycle action was performed.

**Wrapper/executable comparator correction for R1/R2.** “Prepared target
executable” above distinguishes two identities; direct equality between the
prepared launcher and `/proc/PID/exe` is incorrect for the existing package.
`nix/workspace-portal.nix` links `P/libexec/codex` to the assembled Codex package,
and `nix/codex-package.nix` makes that package's `bin/codex` a wrapper executing
its `libexec/codex/bin/codex`. No build or capture is needed to establish this
declared layout. Retain both exact comparisons in the existing fixture:

- L = realpath(`P/libexec/codex/bin/codex`) must equal the public prepared
  candidateCodex; public activationNative remains equal to L. The selected
  profile must still resolve to the prepared candidate package P.
- N = realpath(`P/libexec/codex/libexec/codex/bin/codex`) is the actual runtime
  executable. Require it executable and compare `/proc/PID/exe` exactly to N
  for the target native service and restored pane client. Bind the source
  client's equivalent L/N through its prepared source package/sourceCodex.
  This same-native fixture requires both source/target launcher identities and
  their inner executable identities equal. Preserve all PID/start-time,
  invocation, socket, pane and root/remote-argument comparisons.

Use the concrete immutable package P already selected by the public preparation,
not a separately supplied native override, arbitrary wrapper parser, version-only
test or pathname-prefix match. `argv[0]` may retain the launcher spelling;
the executable comparison belongs to `/proc/PID/exe`. Keep a local predicate
control where the legitimate L≠N layout passes, and wrong public L, inner N or
package binding fails. This only corrects the two fixture comparators and their
existing helper/controls. It requires no production/package/native change or
new file, and supersedes the earlier direct prepared-path/proc-path equality.

Affected call sites are `switch_start` (validate/carry the public package and L
along with declaration-derived N), `maintenance_case` source-client setup and
target native barrier, and all `managed_client_state` calls including failed,
restored and replay observations. Source setup can derive L/N from the selected
immutable source package before preparation, retaining the current
`state/codex/current/bin/codex` equality to L; subsequent public preparation
must match that source package and sourceCodex. Pass N, not L, to the existing
client-observation executable predicate. No need to alter its process/session
rules. The R1 exact-UUID privacy correction stays accepted: do not read
Preparation. D's retained entrypoint facts bind wrapper8da58a47 and ELF647b0157
to distinct paths in the same2rq package, confirming this source-only correction.
Rerun only the directly affected local comparator/predicate and syntax controls;
unchanged declaration/graph/registration evidence needs no replay. Main owns
revised source release and amendment; this clarification grants no execution.

**Package-Go cgroup control correction (R40b41eac).** B retains the failed-check
package. Both preserved package logs return nil in the live-cgroup test; neither
records sandbox mount topology. Do not claim the failure proves a native loss or
that a particular mount was absent. The test assumes `/proc/self/cgroup` maps to
a visible populated subtree of `/sys/fs/cgroup`, which is not an established
property of the package sandbox. A skip alone would remove the sole populated
scan control. The smallest sufficient seam is an unexported
`emptyStartupCgroupTree(root string) error` in
`portal/cmd/workspace-portal/maintenance_startup.go`, containing the existing
WalkDir/read logic unchanged. `emptyStartupCgroup(group)` retains its exact
absolute/canonical/non-root validation and calls that helper only with
`filepath.Join("/sys/fs/cgroup", group)`. No injectable global, environment/config
override, new interface, or change to `proveFailedStartup` is needed.

Keep every production outcome: missing scan root alone succeeds, empty/whitespace
membership succeeds, any populated root or descendant membership refuses, and
all other walk/read errors propagate. In `maintenance_startup_test.go`, use
`t.TempDir()` trees to cover populated root, empty root with populated descendant,
empty tree, missing root, and a deterministic membership read failure. A dangling
`cgroup.procs` symlink supplies the last case without permission tests that depend
on the test UID; its read error must not be swallowed as missing scan-root success.
Retain invalid-group wrapper controls and all existing process/boot/unit/listener
controls. This tests the actual production scanner, without a test-only copy or
stub saying “empty”.

Retain the actual live-cgroup composition subtest, but run its refusal assertion
only after a valid non-root self group and its mapped readable `cgroup.procs`
positively contain this test PID. Otherwise explicitly skip just that live-view
subtest with the unavailable prerequisite; never turn a scan/assertion failure
after that positive observation into a skip. The deterministic populated controls
always run. No mount mutation or access to a real cgroup is needed for them.

After main releases this tiny production extraction, B owns gofmt and focused
`go -C portal test -mod=readonly -count=1 -run
'Test(EmptyStartupCgroup|StartupReplacementRequiresPositiveProcessUnitCgroupAndListenerAbsence)'
./cmd/workspace-portal` under the repository Nix shell (use the chosen actual new
test name). Also run B's already assigned affected deadline test for its separate
callback-cancellation correction; retain saved deadline and positive parent/child
interrupt assertions, with no blanket EOF exemption. Full package/VM rerun stays
main-owned after committed remedies; no graph/native audit or duplicate full
review is implied. Files are the existing startup Go/helper test plus B's already
owned deadline fixture. No production behavior/public contract changes are
authorized. This sufficient source-only clarification returns architect capacity;
only design.md changed, with no checks/build/evaluation/Git/lifecycle execution.

**Caller-deadline fixture clarification (B6c81e96d, reviewed Rc52480c0).**
Limit the concrete failed-test correction to
`TestMaintenanceCallerDeadlineWinsNativePauseCap`: initialize a real `m.client`
with a successful ActiveTurnID under its existing setup guard, arm the fixture's
silent-read callback, then pass the original20ms caller context through
`pauseNative` with the500ms call cap. Require that its callback sees exactly the
caller deadline, the actual read is observed, DeadlineExceeded returns and saved
phase/notice/cutover state does not advance. This isolates the intended deadline
winner without excusing handshake errors. B owns that already accepted correction.

Retain `GraceBoundaryRetriesPassiveReadInInterruptPass` and
`ExpiredRecoveryHasOneSharedAllowance` as full `m.pause` tests, with existing
20ms/40ms settings and assertions. No existing test callback can prewarm the
clients created inside `pausePass` before its grace/allowance is calculated;
callbacks run after handshake, and changing the persisted deadline there would
not replace the operation/deadline already captured by the current pass. Moving
these tests entirely to `pauseNative` would lose automatic grace-expired retry,
real parent/child interruption/no-steer, or fresh expired-recovery allowance
calculation. No supported small test-only substitution for that whole-loop
composition was established. Do not add a production clock/client seam, increase
timeouts or ignore handshake failures in anticipation of an unobserved sibling
failure. The existing worker-restart test and its saved-deadline/actual interruption
assertions also remain intact.

To assert shared-budget nonrenewal precisely, add only a small same-file
`pauseNative` callback control: pass the same fixed absolute allowance through
two successive calls, choose grace/call/caller limits strictly later, and have
both callbacks return immediately after recording their effective deadline.
Both must equal that original allowance. Use a comfortably future timestamp,
not elapsed sleeps or a silent socket; the assertion tests exact deadline identity,
not wall-clock speed. A third call with an already elapsed allowance must refuse
without entering its callback. This supplements, rather than replaces, the
existing full-loop40ms expired-recovery test. It adds no native fixture or shared
test framework. Run only the affected caller/shared-budget and retained grace/
expired/worker-restart focused names under the existing Nix Go command after
main's release. Any actual sibling failure remains a concrete failed-check result
for its owner; this note does not pre-authorize a broader redesign or VM retry.
Only maintenance_pause_test.go is affected. Main owns release; architect capacity
returns with no application edits or checks/execution performed.

Use the fixture's real claim path if its configured profile policy requires a
claim; no stubbed ownership predicate or invented live claim. Generic fixture
policy without a profile resource is not live claim coverage; the accepted
composed R3 test and actual rollout retain that separate obligation. Preserve
normal client restoration for clients the fixture actually stopped. Do not add
terminal-presentation or child-mail guarantees.

These are guest-only mutations: no registered development/peer session, actual
user profile or host service is a failure target. Use existing VM timeouts,
bounded status polls that stop on terminal failure, and the real150second native
unit stop limit; allow roughly5minutes per added switch case. Existing VM cold
build/run cost can be tens of minutes (a retained recovery run took about35),
not a quick check. Main launches the authorized mutation driver; the watcher
only observes. Reassess at30minutes without a completed phase; no automatic retry
or expanded campaign. Unexpected kernel build, escaped ownership, stale source
binding or unresolved process effects stops advancement. This test-only extension
is the concrete outstanding coverage dependency, not a new production blocker.

**3. Packaged composition and independent wakeup remain separate evidence.**
After final R publication, update W's existing nested runtime override and C's
confctl-managed `devWorkspace` input to the same exact R, preserving extension
selection/follows. Run `bin/check-dev-workspace-deployment --workspace-root W
--configuration-root C` and the final declared affected package/composed checks;
reuse prior successful checks only with matching derivation/input receipts.
Build W with an owned GC-root output link and C with its named confctl generation.
Retain exact source/input revisions, resulting package/toplevel store paths,
derivation/NAR identities and native/SDK binding in the existing rollout receipt.
No obsolete strict-maintenance flake check is expected to reappear.

The original wakeup/monitor obligation remains `TestNativeMonitorOperation`
with `LIVE_MONITOR_PACKAGE=EXACT_BUILT_MANAGED_W_PACKAGE`, the same
`LIVE_SWITCH_CODEX`, `GOWORK=off`, the same tag, exact test-name selection,
`-count=1 -failfast -timeout=20m -v`. It has eleven existing modes. Keep earlier
accepted evidence for its actual immutable inputs; the final composed candidate
needs its own applicable binding/acceptance, not an inference from bounded-pause
success. Do not change its assertions or run maintenance as a substitute.

**4. Authorized initial rollout is not an automatic-switch test.**
The recorded aitherdev deployment direction and initial manually coordinated
window remain valid; integration and session lifecycle actions remain unapproved.
Use the previously established host-first/profile-second path at design943+:
prepare/root/build/copy, then exact machine ownership and named-generation
dry-activate/switch, then the ordinary selected profile command. W/Cf161 must be
replaced by the final reviewed composition first. Fresh selected/profile-token,
system and retained recovery checks decide whether an existing operation must
be recovered; no forced idle, profile-link rewrite or replacement claim.

Configuration entrypoints remain `confctl build cz.vpsfree/machines/aitherdev`
and `confctl deploy --generation GEN --copy-only`, then the same exact GEN's
`dry-activate`/`switch`. Pass the held typed aitherdev claim and exact session
environment to `workspace-host switch --source W`. The recorded external-user
invoker handoff applies to the initial old-source window; preparing it does not
authorize this architect to interrupt or stop the development session. Once
schema2 source is selected, ordinary `--enable-maintenance` enables the new
behavior; no MCP restart stage or native upgrade is required. A successful idle
initial install does not prove active automatic pause/resume.

Verify selected app/system identities, portal health, naming, conversation
continuity and ordinary follow-up after the actual switch. Do not inject failure
into the live profile or manufacture a disruptive switch merely for a second
acceptance run. An actual stop/activation failure means retain ownership and use
the exact original recovery, with no resume claim. Machine release follows the
existing verified-effects/integrated-lineage rule; deployment grants neither
default-branch integration nor session cleanup. Main owns execution allocation,
watchers, claims, pins, final evidence and user-facing handoff. This finite brief
returns architect capacity; only design.md was changed and no checks were run.

### Creation completion lock correction after the b1f6d582 VM failure

Bounded primary diagnosis, 2026-11-06. Session/environment and retained
architect0 Astra/xhigh/workspace_write confirmed. Baseline R
`b1f6d582a32342546ae4a6bdae43f214f91242ec`, tree
`97d6fb9848012d94bb0d5b687ad42987a731caa8`. The original VM log
`/tmp/lead-wakeup-vm-b1f6d582-h5_s7zc9/vm.log` (SHA256
`a33ecc38ca091547587084a249ae96db7c4d67e25f18e079ca6db5db4930d993`)
and D's preservation.json under
`/tmp/lead-wakeup-vm-creation-failure-D-g7t9ceuy/` establish the automatic
request's terminal initialization failure at19:00:45.724Z, after the terminal
client restart message, with `another dev-session command is changing
2026-11-06-accepted-session`. Naming reported model/ok; the initial automatic
request reached the model. This does not establish client readiness. The VM
failed before maintenance cases. Model-list decode errors and tracking/retry
activity are not proven causes. No exported automatic private receipt/journal
or lock-holder capture exists; the exact competing reader/writer is unknown.

The owning Ruby source supplies a concrete avoidable interval. `start` holds
the outer creation lock, deliberately releases the slug lock for initial goal
delivery, then reacquires slug EX at libexec/dev-session1310. It reconciles the
client (restart message at9597), writes ready manifest/authority/journal, and
releases EX. It separately reacquires EX at1332 solely to write receipt evidence.
`with_slug_lock`8456 waits for a creating authority, but after ready publication
this last acquisition defaults to nonblocking. Any ordinary shared reader or
exclusive writer taking the lock in that interval can cause the observed error.
The local ready/evidence writers do not need another slug acquisition. Portal
creation.go1064 correctly refuses a failed initializer without successful exact
`proveCreation`; a ready manifest alone is not completion evidence. This is a
source-supported failure mechanism consistent with the captured run, not a claim
that the absent automatic journal or exact holder was observed. The failing
creation path belongs to an original case; no evidence attributes it to execution
of the maintenance addition, and introduction history was not audited here.

**Sufficient single-implementer boundary, subject to main allocation:** change
only `libexec/dev-session` and focused tests in
`test/dev_session/session_initialization_test.rb`; reuse existing team/progress
tests. Write receipt evidence before releasing the existing slug EX in all
three `start` completion paths: the post-send creating-to-ready block; the
ordinary no-pending-goal block after ready bookkeeping; and the exclusive
already-ready replay branch after its existing identity/client validation.
Remove the final separate evidence acquisition. In replay, normalize the existing
unmanaged/missing-session result to nil and retain the evidence writer's refusal;
do not let the early `next` bypass evidence or newly accept a missing session.
Move the existing prompt-finish emission into the post-send block immediately
before evidence so prompt/evidence progress order and one emission are preserved.
Keep the block's return value as the selected session. No new helper framework
is needed; a short comment explains why ready publication and evidence share EX.

Keep initial goal delivery outside slug EX, with the outer creation lock intact;
the initial request must remain able to invoke workspace helpers. Do not add
lock waits/retries, weaken ordinary contention refusal, change reconciliation,
alter provider/name/team selection, or infer completion from the restart log.
Evidence I/O failure still propagates and leaves the same accepted ready journal
recoverable through its original receipt without resending. Public/private
formats, settings, thread/tmux identity, removal protection and old-package
recovery stay unchanged. This adds only local evidence writing to an already
owned critical section; no native, Go, SDK, package/pin or deployment change is
part of the repair. A nearby comment suffices for the lasting rationale.

**Deterministic acceptance:** use the existing Ruby runner subclass seam and
real flock on a separate file descriptor. Immediately after the real ready slug
critical section returns, acquire and retain its lock as an ordinary competitor
(table cases SH and EX); release it in test ensure. The original code then fails
at the redundant acquisition; corrected creation must already have written exact
receipt/thread/goal evidence and return success despite the now-held lock. No
sleep, real model or production hook is needed. Cover fresh initial-send and
same-receipt ready replay, with one initial delivery and no replacement thread;
retain no-goal completion coverage where the existing start contract permits it.
Assert initial delivery still runs without slug EX, and evidence itself runs
under EX. Keep the existing evidence-write-failure retry after source archive/
deletion, wrong-goal/journal refusals, deleted-destination refusal, retained team/
provider/sensitive assertions and progress ordering. An evidence-write error must
remain a real failure, not become a successful or silently retried creation.

After release, focused quicks use the repository Nix Ruby environment: `ruby -c
libexec/dev-session`, then the session_initialization, agent_team_creation and
creation_progress test files. Run the existing dev_session suite through
`ruby test/run_ruby_suite.rb dev_session_test.rb` (or its four declared shards)
for lifecycle-access/preparation exclusion and recovery controls; retain the
existing naming-failure and collection/package-exclusion coverage under the
workspace verification procedure. Do not invent a replacement harness. D's
secondary no-maintenance-journal diagnostic fix remains separately owned and
preserves the primary failure. Main owns combined review and any later original
VM rerun with unchanged creation/readiness/follow-up assertions. This diagnosis
neither authorizes a retry nor claims VM/native acceptance. Only design.md was
edited; no application edits, checks or lifecycle actions. Capacity returned.

### ed35cf1b manual-name recovery: transcript failure and bounded diagnostic

Current76ef1ad1, 2026-11-06. Identity/environment and retained architect0
Astra/xhigh/workspace_write reconfirmed. R
`ed35cf1bccf024c2ebbf455a25f51fe9af6e13ee`, tree
`e4830f3f97783478abf0031476b0120882fcc14e`, was unchanged/clean at the natural
VM failure. Original `/tmp/lead-wakeup-vm-ed35cf1b-vonit3o6/vm.log` SHA256
`23f0ab612105b80d60b815e2d8937f0e233fdbc02f07a082b856f3e04cd227b4`,
result SHA256 `d474d84c5864aa846630a254f81d833402bca50c4e5b24d265ee62b0b461c4fd`.
D owns preservation at `/tmp/lead-wakeup-vm-browser-failure-D-n1az1jn6/`
(preservation.json `7d1766037cace3021fce6e7fe5eebba24e66f48c1b4d1dc6b8c0a4398c59d302`).
The prior automatic creation/lock case passed in131.50s. Nine logged subtests
passed; maintenance was never reached. These remain exact-source successes,
not final whole-suite acceptance.

**Exact failed boundary.** Browser `name naming-error` accepted the manual name,
observed attempt2 ready, followed the canonical page, and read its nonempty thread
ID `01a1b2ae-822e-7523-b96f-6e43bc1f89df`. Then
`test/creation_acceptance_browser.cjs:106` timed out after30000ms waiting for
`#transcript` to visibly contain `CREATION_REPLY_`; caller is the name branch200.
The follow-up was never submitted. Request
`ea7cfc5f-01dd-4501-86ea-9381c2c3fef1`, receipt
`cb95723914a3eeaf404196488c50e942551e7b4931258a3ada704ce2d45fa0e6`,
canonical slug `2026-11-06-php-upload-progress-mitigation`, ready update
21:05:52.374602615Z. The local diagnostic record merges status via Object.assign,
so old error/canSetName/phase fields can remain from the failed naming attempt;
their presence is not proof that naming or initializer failed again. No pageerror
was recorded. The body remained CONNECTING/Loading conversation, with file-status
timeout and unavailable settings. D's exact model rows29/30 prove alternate
naming/initial requests, neither overload nor retry advice; they do not prove
response delivery or persisted native history. No failed-thread native.json,
manifest or private completion receipt was exported.

The immediately owning frontend is portal static/app.js7089–7212: it starts
an independent paged snapshot read and SSE through pinned codex-web
`c3c2adb705f5ff6bb42c98bd44be3649fd93bedb` conversation/assets/sync.js.
The snapshot/request deadline is35s; uploads use10s. The30s fixture assertion
can precede the conversation timeout presentation. That fact is not grounds
to enlarge either deadline. Server resolution is server.go3875+ and the pinned
conversation handler's resolve/verify/read/Subscribe path. Existing Server-Timing
and X-Portal-Read response headers can identify its completed stages. Native
thread/read timing logs in the failed interval omit thread identity and cannot
prove this page's read. Existing fixture capture records only response events,
then truncates to30; it omits initiated/failed/still-pending requests, timings and
snapshot payload results. Thus fixture/environment versus production fault is
not established. No production correction is justified by this evidence.

**Sufficient next package is diagnostic-only, owned by D after main release.**
Files: `test/creation_acceptance_browser.cjs` and only the failure-diagnostic
branch of `nix/tests/session-creation.nix`. Keep every original assertion,
deadline, creation/receipt/private-state check, follow-up and no-resend condition.
Before navigating, use existing Playwright events to retain a small bounded
request table: method/path/resource type, start/response/finished/failed times,
status, failure text and request timing, with only Server-Timing/X-Portal-Read
headers. Keep still-pending entries separately so response truncation cannot
erase them. Retain the exact conversation thread/page, events, collaboration-modes
and upload-status requests; no cookies, authorization headers or request bodies.
For a completed thread/page response, retain only whether parsing succeeded,
thread identity, turn/entry statuses and matching initial/reply counts, without
waiting indefinitely for an unfinished response body. Capture bounded console
errors and failure-time URL/document visibility/readiness plus the existing DOM
and exception. Save this in the already exported `/tmp/creation-evidence/`
directory before browser close; retain the original exception even if diagnostic
capture fails. No injected production state, synthetic response or transport
replacement. Exact assertions still decide success.

On that same failed invocation only, the VM's existing exception branch may
take one bounded passive native snapshot and one bounded portal snapshot for the
exact thread/slug from that failure record. Reuse `creation_transport.py read`
under an external8s timeout and Unix-socket `curl --max-time 8` to
`/api/sessions/SLUG/thread/page`; record exit/status, elapsed time, timestamps and
output/errors in creation-evidence. Never list/adopt another thread, resume,
restart, reload the page, resend, or retry creation to obtain the evidence.
These snapshots occur after the browser failed and must be labelled accordingly;
they cannot retroactively certify what it rendered. Diagnostics remain best
effort and cannot mask the original failure. No changes to transport/model,
production Ruby/Go/JS, pinned SDK/native, or private format are needed.

**Shortest runtime route, separate from final acceptance.** The retained
driver derivation858w2qlv resolves to
`/nix/store/vzwlazgyg2yn8qzd1cwyf06aswvd0nkg-nixos-test-driver-dev-workspace-session-creation`;
its ordinary `bin/nixos-test-driver --interactive --output_directory OUT`
is verified in the installed driver's source. It exposes `driver.tests`,
`driver.test_symbols()` and the original Python subtests. There is no discovered
CLI case-filter option or retained running guest. After committing the diagnostic
changes, quick checks and affected review, prepare the new exact
`.#checks.x86_64-linux.session-creation.driver` output with the usual
`nix build --no-write-lock-file --out-link DRIVER ...` route, retain its source/
package/native bindings, and invoke that driver's existing interactive mode in
a fresh disposable output directory. The old path identifies the available
interface; it must not be claimed to contain the new diagnostics.

In its Python REPL, execute the exact existing setup prefix and only the exact
`failed naming stops before reservation and keeps manual recovery` subtest,
retaining the original outer exception/finally. A finite source selection is:

```python
import ast
script = ast.parse(driver.tests)
outer = script.body[-1]
assert isinstance(outer, ast.Try)
label = "failed naming stops before reservation and keeps manual recovery"
cases = [n for n in outer.body if isinstance(n, ast.With)
         and isinstance(n.items[0].context_expr, ast.Call)
         and n.items[0].context_expr.args
         and isinstance(n.items[0].context_expr.args[0], ast.Constant)
         and n.items[0].context_expr.args[0].value == label]
assert len(cases) == 1
outer.body = cases
exec(compile(script, str(driver.config.test_script), "exec"), driver.test_symbols())
```

This uses the original guest/package/provider/registration setup, then existing
browser admit(auto,alternate,attachment), failed, manual-name, readiness/follow-up
and proof commands. It adds no permanent selector or test harness. Preserve
original handlers/final copy and let the ordinary driver own guest teardown.
Expected focused runtime is minutes after the driver is prepared, not a promised
build duration; reassess after10minutes without reaching/completing this one
case. Stop at its first failure with evidence, no retry loop or additional cases.
An isolated pass only disproves a deterministic single-case failure; it does not
reproduce the accumulated sessions, clients, earlier provider faults or portal
restart from the failed full sequence. Final original whole-VM acceptance remains
required, with diagnostics retained, after any evidence-supported correction.
Do not use a full42minute replay as the first diagnostic by default.

Quick scope: Node syntax for the changed browser fixture; existing Nix embedded
Python syntax/type check when preparing its driver. Review that pending and
failed reads stay distinguishable, diagnostic failure preserves the primary
exception, and no mutation/retry or changed assertion was added. A completed
snapshot containing the exact reply while the DOM lacks it isolates rendering;
HTTP failure/pending with a later positive native snapshot narrows the transport/
portal path but does not prove the earlier history state. Absent issued reads
requires the captured boot/console/visibility evidence; an absent native reply
does not implicate the browser. The next report must state which boundary the
evidence establishes, not infer a production fix from a green isolated rerun.
Main owns allocation, review and runtime permission. Only design.md changed;
no checks, build/evaluation or guest/native/browser/lifecycle execution. Capacity
returned with the precise missing-observation prerequisite above.

### Observed grace-boundary fixture failure: scheduling correction, 4897133d

2026-11-06, baseline R4681a5c88dce3aa6e87d3b733a76e93180e2df44/tree
701af5726dc08baef2245ca4ed0bc47ee99454ee. Identity/environment and retained
architect0 Astra/xhigh/workspace_write confirmed. B owns immutable evidence at
`/tmp/lead-wakeup-grace-driver-evidence-B/`: evidence.json SHA256
`c8585ce3b2f1dc22b20b05347f92bd7c212eb820cd5a23f0aa5bdc2e36843c19`,
failed60x.log `a89dc948185efd49aa0778b4e1b5e7276b5243beebfe8fa93b00c7b771f224a6`.
The original driver-build log is
`/tmp/lead-wakeup-driver-build-4681-1794001462-2855040/driver-build.log`
(SHA256 `a20062272e554bd2b4f937fd5c9d9608ba1c139a7d326c6a3e58753e5f8d6d43`).
No guest started. The other package's Go command passed, but that log is not
proof that its entire derivation completed.

`TestMaintenanceGraceBoundaryRetriesPassiveReadInInterruptPass` failed at
maintenance_pause_test.go377 in0.13s, with DeadlineExceeded and
`pause-interrupt-timeout`, then a fake-server reader EOF. In this test,20ms grace
is persisted before `m.pause`; each `pausePass` constructs fresh clients for the
participant and service. The first real thread/turns/list response is withheld
regardless of whether the request actually arrived before grace. `pauseNative`
covers connection initialization as well as the logical call. Its80ms per-call
cap can expire during interrupt mode and produces the same reason as exhausted
shared recovery. The reported0.13s total strongly supports the80ms call cap,
not exhaustion of the300ms recovery allowance. No request trace identifies the
specific timed-out call or connection. In this fixture, post-handshake read EOF
returns nil, so the reported reader EOF came from a handshake; initialize versus
initialized, and whether this was the grace or a later connection, remain unknown.
This does not establish a production pause defect.

This supersedes design3448+'s instruction to retain the artificial20/80/300ms
values now that the concrete sensitivity has occurred. Main clarified that a
measured test scheduling correction is permitted; timeout inflation without
phase proof is not. B confirmed there is no existing sufficient prewarm seam:
its callback runs after handshake, journal changes do not replace the copied
current-pass deadline, and a separately warmed client is not the one `pausePass`
constructs. Adding production clock/client/pass injection solely to retain these
short test values is larger and less useful than correcting this test's budgets.

**Sufficient one-file implementation:** only
`portal/cmd/workspace-portal/maintenance_pause_test.go`, specifically the failed
full-loop test. Use500ms saved grace,1s per-call cap,3s shared recovery allowance,
and a5s caller guard. These are fixture values, not product defaults. They give
ordinary local setup and fresh interrupt connections room while ensuring the
first deliberately silent read is bounded by grace rather than the call cap.
Expected healthy runtime is about0.5s plus real local interrupt/cleanup work;
there is no retry loop. This is event-asserted coverage, not a claim that any
finite wall-clock budget is immune to an arbitrarily stalled test machine.

Use the existing method callback and atomic counters/timestamps: record entry
to the first actual thread/turns/list and withhold only that response; record
entry to the next such request and let all later ordinary replies proceed.
Require first entry to exist and precede the exact saved grace deadline, and
the retry entry to exist and be at/after that same deadline. Compare recorded
timestamps after the run rather than racing a mutable deadline in the server
callback. One invocation of the real `m.pause` must return paused, leave the
original saved deadline unchanged, reach draining-writers, and produce exactly
`[interrupt:thread interrupt:child]` with no steer. Preserve pending continuation
and explicit-Stop identity; maintenance interruption must not become user Stop.
If the first callback missed grace, fail explicitly instead of interpreting an
interrupt-mode timeout as successful coverage. On failure, include callback
count/entry times, saved deadline, effect log and returned reason so the next
failure identifies the intended phase. Do not accept or suppress handshake EOF.

Keep `pauseNative` classification/precedence and the entire production loop
unchanged. Retain the existing20ms caller-deadline test,40ms expired-recovery
full-loop test, exact shared-allowance/nonrenewal control, worker-restart saved
deadline and actual parent/child interruption test, silent-read/steer/list/
interrupt bounds, persisted Cancel/caller cancellation, and unknown-steer ledger
controls. They continue to test small deadline/allowance behavior independently;
the repaired test specifically proves the grace-pass-to-interrupt-pass transition
with real client RPCs. No shared fixture signature, production seam, global fake
clock, SDK/native, public or persisted format, pin, migration or deployment change.

After main release, use the existing Nix Go environment from portal/: first
`go test -mod=readonly ./cmd/workspace-portal -run
'^TestMaintenanceGraceBoundaryRetriesPassiveReadInInterruptPass$' -count=10`
as one bounded local repetition for the observed scheduling failure. Then run the
existing affected pause/deadline/cancellation controls once, and the owning Go
package's ordinary check once. Preserve exact commands/results and the unchanged
production files. A missed callback phase or another failure stops expansion;
do not automatically increase budgets or change a sibling test. Quick success
permits the normal commit and affected review; main owns rebuilding the exact
diagnostic driver and the previously planned focused browser runtime, followed
by required whole-VM acceptance. No guest rerun is part of this source fix.
Only design.md changed here; no source/check/build/evaluation/native/VM/Git/live
action. Finite brief complete, architect capacity returned.

### Finish-path verification inventory after c81, c0cfd085

2026-11-06. Current/environment and same-session roster reconfirmed; architect0
retains Astra/xhigh/workspace_write. This continuation uses reviewed R
`c81bd849807825fa3ad9caece77b6229aeb3c574`, tree
`681f812ab3c0f75687588ce10981d1984e3db80c`, review846e144c (no findings).
It changes no implementation or acceptance contract. The full session-creation
run started22:47:50UTC is main/watcher-owned; its output was not inspected here.
Its result remains pending for this brief. A failure returns only the affected
package for diagnosis, without an automatic retry or new architecture.

**Evidence boundary.** The c81 driver build at
`/tmp/lead-wakeup-driver-c81-6a1w_a0r/result.json` passed in1010.281s and built
both declared fixture packages. Driver
`/nix/store/r2a9wdhv3bf3ilywmspzssd9023xavs4-nixos-test-driver-dev-workspace-session-creation`
is preparation, not a guest result or the final configured workspace package.
The isolated manual-recovery result at
`/tmp/lead-wakeup-manual-c81-1y8ia0i6/result.json` passed in377.013s; it neither
explains the earlier full-sequence timeout nor replaces original whole-VM
acceptance. Accept the pending full run only from its exact source/driver/check
binding, natural result, original creation and maintenance case results, and
owned-effect reconciliation. Preserve queue identity/text or actual saved
delivery, goals, explicit Stop, same-operation failure recovery, and observed
managed-client restoration; restoration.completed alone is insufficient.

**Package 1 — final R verification, no source changes.** One available
implementer can reconcile the declared29 outputs with existing receipts, then
run only unresolved outputs in the established Nix environment. The manifest is:

- Four VM checks: `session-creation` (already running),
  `session-archive-lifecycle`, `host-module-idempotency`, `session-recovery-boot`.
- Ten other checks: `codex-package`, `package`, `ruby-source-filter`,
  `host-module`, `host-auth-benchmark`, `host-package-contract`,
  `extension-catalog`, `agent-team-catalog`, `user-namespace`, `generic-source`.
- Fourteen Ruby shards: `ruby-dev_session-{0,1,2,3}`,
  `ruby-workspace_coordination-{0,1}`, and `ruby-{auto_archive,workspace_host,
  coordination_claims,machine_identity,coordination_admission,coordination_gc,
  integration,integration_certification}-0`; plus `ruby-verification`.

Use the recorded canonical command shape from the R worktree:
`nix flake check --print-build-logs --no-write-lock-file --no-update-lock-file
--max-jobs 4 --cores 4` against the exact committed R flake reference. Nix may
reuse outputs; explicitly building unresolved `.#checks.x86_64-linux.NAME`
instead is sufficient with a complete29-output binding receipt. Do not rerun
the successful creation VM merely to fill that receipt. Preserve complete unique
Ruby shard coverage; the143-test driver summary and the earlier551-test ordinary
Ruby run alone do not prove all14 shards. Exact-head CI covers25 non-VM checks,
archive and creation; feature-push CI omits the two host VMs, whose local evidence
must remain explicit. Use current-head CI, not the old f161 success.

Reuse requires the final attribute's derivation/output and complete relevant
source/input graph to match successful retained evidence, with valid output/NAR
and terminal effects. A version string, unchanged filename or tree comparison
alone is insufficient. The existing f161 inventory at
`/tmp/lead-wakeup-runtime-checks-f161-gli552zj/receipts/` already supplies the
comparison layout; use its check-derivations, binding-validation, valid-output
and Ruby records without a new framework. Current driver dependencies may also
supply exact successes. Their overlap with final29 is not yet enumerated, so
there is no honest fixed count of checks still needing execution.

The five-mode `TestNativeWorkspaceBoundedPause` passed against R40b41eac in
21.866s at `/tmp/lead-wakeup-native-40b41eac-d0i4dh4c/`. Reuse only after binding
the exercised production/fixture/SDK/native inputs to final R; its five recorded
file hashes alone are not a complete equivalence proof. If that cannot be
established cheaply, run the existing fixture once against final inputs with
`nix develop --command env GOWORK=off LIVE_SWITCH_CODEX=N_FINAL go -C portal test
-mod=readonly -tags=live_switch_integration -run '^TestNativeWorkspaceBoundedPause$'
-count=1 -failfast -timeout=10m -v ./cmd/workspace-portal`. It has five90s case
bounds. This is disposable native TERM/restart acceptance, not live activation.

**Package 2 — final W/C pin preparation, two disjoint edit boundaries.** W is
recorded at1b219d61 and C at e3f942e6; both still select Rf161ede8. Their old
artifacts/checks are historical until exact final bindings prove reuse. Main
first confirms final R publication; publication is not established by this
inventory. After main allocation, W's owner changes only the existing nested
runtime URL in `workspace/flake.nix` and generates its lock using
`nix flake update vpsfree-dev-workspace/dev-workspace`. Preserve extension
f8da821e, sibling inputs and follows paths; no new top-level runtime input or
extension-lock edit. C's separate owner uses its declared channel/role:
`nix develop --command confctl inputs channel set --commit dev-workspace
devWorkspace FINAL_R`. Preserve generated history; no manual C lock edit.
These are feature-worktree operations, with their ordinary hooks, publication
and applicable affected review; no default-branch integration is implied.

The W owner completes all six declared checks: `tracking-source`,
`deployment-contract`, `storage-retention`, `agent-instructions`,
`agent-team-policy`, `cluster-provider-composition`. Use `nix flake check
--no-write-lock-file --print-build-logs` or bind the six explicit outputs.
After both locks settle, run the existing
`bin/check-dev-workspace-deployment --workspace-root W --configuration-root C`.
W/C here mean this session's existing workspace/configuration worktrees.
R's settled source review is not reopened for mechanical pin preparation;
material consumer deviations return to main before expanding the package.

**Package 3 — final composed artifacts and independent wakeup acceptance.**
Build W's actual configured default using `nix build --no-write-lock-file
--print-build-logs --out-link OWNED_CANDIDATE_ROOT .#default`, and retain its
exact package/derivation, complete semantic input graph/closure, selected catalog
and utility bindings. This must use the final W/R pair, not R's generic default
or the VM's capacity4/5 fixtures. Preserve the accepted stock0.165 native and
SDK c3c2adb705f5ff6bb42c98bd44be3649fd93bedb selection; no SDK/native work is
proposed. Bind declared launcher to its entrypoint and native identity to the
inner executable, not the Bash wrapper. `P_FINAL/libexec/codex/bin/codex` is the
native-package launcher; its declared inner executable is
`P_FINAL/libexec/codex/libexec/codex/bin/codex` (resolve/store/hash as N_FINAL).

Run the existing11-mode matrix once from final R:
`nix develop --command env GOWORK=off LIVE_MONITOR_PACKAGE=P_FINAL
LIVE_SWITCH_CODEX=N_FINAL go -C portal test -mod=readonly
-tags=live_switch_integration -run '^TestNativeMonitorOperation$' -count=1
-failfast -timeout=20m -v ./cmd/workspace-portal`. Required modes remain passed,
failed, escalation, busy, steer-race, restart, native-restart, lost-reply,
cancel-uncertain, cancel and missing-report. Require actual per-case native
receipts, same-ID refusal/accepted-start proof and terminal owned effects.
The old f161/W1b219 matrix passed75.690s but is not final package acceptance.
These fixtures use private disposable workspaces/sockets and synthetic Responses;
they do not access or restart this development session.

C's matched host artifact preparation uses its existing
`nix develop --command confctl build cz.vpsfree/machines/aitherdev`; retain the
named generation and exact toplevel/source graph. This is the existing consumer
build boundary, not a revival of the canceled separate host release/integration
detour. The earlier e3/f161 host artifact and deployed host remain recorded
separately; neither is silently relabeled final C. W provides the user-profile
application, and C does not install that application.

**Order, bounds and authority.** Now-independent work is read-only receipt
comparison and W/C pin-diff preparation; no active-run observation or conflicting
heavy command is needed. After main accepts the fullVM result, package1's missing
checks and package2's disjoint consumer preparation may progress independently.
Final W package construction feeds native11; final W/C locks feed the cross-check
and C artifact. Main confirms implementer capacity and assigns complete packages
and Git windows; roster ready alone is not capacity. No allocation is made here.
Use existing fresh Luna/low watchers for long commands and the retained heavy
resource slot. Historical scheduling evidence: R29 took55m14s, one archive run
35m31s, W build about12m43s, C build about2min, native11 about76s; these are not
guarantees. Reassess at10min without a new phase and30min without a completed
milestone. First actual failure, source/ownership mismatch or unexpected kernel
build stops the affected batch; no automatic retry or broader campaign.

Next observable results are (1) the watcher-owned fullVM disposition,
(2) exact29R/6W check coverage with reuse versus execution identified,
(3) final matching W/C pins and rooted artifacts, and (4) final native11 receipts
plus native5 reuse or execution disposition. No new product decision is needed.
Live profile upgrade has not happened; prior host activation/reservation is
unchanged. Main retains the recorded initial rollout/recovery authority and must
freshly bind exact selected/source/target/profile/claim before any live action.
This note grants no integration, claim release or session lifecycle permission.
Only design.md was edited; no checks, evaluation, Git, pin or runtime actions
were performed. Brief complete; architect capacity returned.

### c81 full-VM bootstrap failure: correct the fixture restart trigger

2026-11-07. Bound current/environment and retained architect0
Astra/xhigh/workspace_write reconfirmed. R remains the reviewed c81/tree681f
named above. The original fullVM ended naturally1 after1952.784s, before any
maintenance operation. D owns preservation at
`/tmp/lead-wakeup-fullvm-c81-preserve-D-58xjxnlk/`; preservation.json SHA256
`2a4b79f38f7ebfd5db80da91b62f0c784b80dc664540bab9d774a7552dee5150`.
Original vm.log SHA256 is
`973de09c3503f26975c17c96319a4e338b69816ea6f33a0c229979b2d7faefb6`.
All13 original subtests completed, including manual recovery and lost-reply
restart. These remain exact-c81 evidence, not final full-VM acceptance.

**Decisive cause.** Generated test773 is
`nix/tests/session-creation.nix:950`: it requires
`original_marker['launch']['required_native_child_threads'] == 4`; the actual
value is0. All three expected MCP `approval_mode="approve"` entries are already
present in the dumped argv. They are data in the failed assertion, not its
predicate. No MCP approval defect is established. The exception occurs before
`switch_start("target", "bootstrap")`, so no pause/activation/restoration result
can be inferred. D's source-mapping and observed-registration records bind this
finding to the actual driver script and package.

The owning contract is explicit in `portal/internal/agentteams/registration.go`:
direct members are independent App Server threads, and BuildRegistrationPlan
returns zero native child capacity. Catalog identity contributes to provenance
digest, not native launch capacity. `libexec/workspace-host`'s
marker_has_semantics?/registration_argv_equivalent? intentionally permits a
catalog/package-only change with equivalent reporting arguments; only the
owned reporting command path is normalized. Its codex_restart_required? and
`workspace-maintenance.rb` maintenance_switch_required? require a real change
to native identity or launch semantics. Consequently, changing the two4/5
assertions to0 alone is insufficient: catalog capacity4→5 does not start the
operation the fixture awaits. This is a fixture setup error, not evidence that
bounded pause needs a new production trigger or strict native protocol.

**Sufficient two-file correction.** D's next package may edit only
`nix/tests/session-creation.nix` and the corresponding explanation at
`test/README.md:116`. Keep the original package/team catalog (capacity4) intact.
Replace the capacity5 target with the original package's existing `.override`
seam, overriding only its `codex` dependency with
`previous.codex.overrideAttrs (old: { name = old.name + "-maintenance-fixture"; })`.
The name is fixture-local: preserve version, original assemblyScript, pinned
native input, helpers/resources and every other derivation input/attribute.
This creates a distinct immutable packaged native launcher/runtime from the
same stock0.165 payload; it changes no Rust source, SDK, global package
definition, registration contract or production configuration. Remove the now
unneeded packageFor capacity parameter rather than retain a false trigger.
Use the existing store-backed sourceFor and public prepare/switch/recover paths.

Bind each package P to its own declared launcher L and inner executable N as
already done by package_native_identity. Add a passive SHA256 of N to that
fixture record. Require source and target package/launcher/executable paths to
differ and their executable bytes to match. This supplements the unchanged
assembly/input binding; do not compare wrapper bytes, whose embedded paths
necessarily differ. A payload mismatch fails, never expands an allowed set.
Public prepared.sourceCodex/candidateCodex must still equal the corresponding
L exactly. At the barrier, activationPackage/activationNative and `/proc/PID/exe`
must equal the chosen target P/L/N exactly; source and restored pane clients
retain their respective source/target N comparisons. No basename equivalence,
wrapper parser or fallback native probing is introduced.

Replace cross-package L/N equality at switch_start and maintenance_case with
that distinct-path/equal-payload predicate. Bootstrap requires registration
capacity0 before and after, source codex_path==source L, and target codex_path==
target L after successful switch; it no longer requires those paths equal.
Keep sourcePlansDigest!=plansDigest as provenance observation, not as proof of
a restart. Actual operation creation and changed native service invocation,
process/socket identity remain the runtime proof. Rename the bootstrap/README
description to a packaged-native identity change with unchanged native code,
not a same-path capacity change. This explicitly supersedes the capacity4/5
trigger assumed by the earlier acceptance and R1/R2 fixture briefs. It does
not weaken their per-role exact identity comparisons.

Keep all original creation cases, model/provider settings, bounds, router hold,
startup failure drop-in and client helper unchanged. Preserve captured root and
ready member turns, real cooperative completion versus deadline interruption,
queued input identity/text or actual delivery, active goal, Stop suppression,
same-operation failure recovery/no early resume, stable one-time continuation
and passive stopped/restored managed-client evidence. No production or
creation_transport.py change is needed for this disposition; its existing
client helper already receives source and target identities separately.

**Local controls and review.** In the existing Nix development environment,
parse/format the changed Nix and extract/compile its generated Python using the
existing fixture quick-check approach. Exercise the changed identity predicate
with distinct P/L/N and equal SHA (pass), same source/target launcher (fail),
same executable identity (fail), unequal payload SHA (fail), and a prepared
candidate launcher inconsistent with its declared package (fail). Retain a
wrong actual executable negative for the existing service/client comparator;
do not weaken that comparator to pass a new fixture. The old bootstrap must
reject the preserved capacity0 marker; the corrected direct-thread expectation
must accept0 and reject4/5. Inspect the narrow Nix dependency diff: only target
native package name changes, not assembly/native/SDK inputs. Existing accepted
production registration/caller-deadline controls need no unrelated rerun.
After intended changes/quick controls are committed, obtain the affected
fixture/identity/activation review before build or guest execution. A changed
production dependency or unexpectedly unequal native bytes returns to main,
not an automatic implementation expansion.

**Shortest driver follow-up after release.** Build only the corrected existing
`.#checks.x86_64-linux.session-creation.driver` with no lockfile writes, binding
its final source/config/test-script/package/launcher/executable identities.
Use the already exercised interactive driver/AST selection mechanism from
`/tmp/lead-wakeup-manual-c81-1y8ia0i6/{run.py,selection.py}` in a new owned output,
runtime, tmp and IPython directory, with its attached tty. Select unchanged
top-level setup/functions and exactly five original subtests in original order:
automatic naming/sensitive retained team; corrected bootstrap; cooperative
pause; deadline/Stop; target startup failure/recovery. Retain the unchanged
except/finally. Select labels exactly once, verify selected AST bodies against
the final driver, and require both case-result success and terminal driver0.

This prerequisite selection is supported by the source: maintenance_case uses
checkpoint("automatic"), its real root/ready roster and existing model; the
automatic case independently creates and proves them from ordinary initial
setup. It does not require explicit/fork/alternate sessions or earlier transport
faults, and those proxy/hold mutations are absent in this selected run. The
bootstrap establishes the target profile for the alternating three cases.
Do not fabricate checkpoints or transplant private journals. Entry command is
the corrected `DRIVER/bin/nixos-test-driver --interactive --output_directory
OWNED_OUTPUT`; submit the bounded selection through the same working launcher,
not heredoc stdin to the REPL. No new driver or test framework is needed.
Retain five-minute maintenance waits,60s router hold/40s inspection and driver's
3600s overall bound; reassess10min without phase progress and stop on first
failure. No retry loop or timeout inflation. A selected pass permits the later
unchanged whole-VM check; it does not prove accumulated full-sequence behavior.
Main owns each runtime release and final acceptance. Only design.md changed
here; no source/check/build/evaluation/native/VM/Git/live action. Brief complete,
architect capacity returned.

### Five-case prepare prerequisite correction, 68ef4ed1

2026-11-07. Current/environment and retained architect0 Astra/xhigh/
workspace_write reconfirmed; applicable unchanged session/documentation,
verification/lifecycle guidance reused and runtime AGENTS.md reread. Baseline
R`3caeb5e64d5c7136b800faeeb9a61e4030aff209`, tree
`d5e9ab80be70a548fd8b7d6a9550ba091cffb4e9`, remains reviewed with no findings.
D's preservation is
`/tmp/lead-wakeup-native-variant-D-318negrk/five-case-preservation/`,
preservation.json SHA256
`3bb13215b5ac2d814bace1be8ad9fdd5edc0ed7fa11da41fded5198c1b0a7ef4`;
original guest.log SHA256
`258f4f5746343a0da8d6a48e32c38a585101bf6cf57104100e2369df94b21864`.

**Observed cause:** public prepare invokes the unchanged
`WorkspaceCoordinationHost#coordination_build`, which executes
`nix build --no-link --print-out-paths SOURCE`. Nix immediately refuses with
`experimental Nix feature 'nix-command' is disabled`. The guest node in
`nix/tests/session-creation.nix` does not enable these features. SOURCE is the
existing immutable directory containing flake.nix, so both `nix-command` and
`flakes` are necessary. This is an omitted VM prerequisite for the newly added
ordinary package-preparation path; no bounded-pause, native, SDK or production
launch defect is established. It fails before candidate validation and operation
creation. Setup/install73.64s and automatic sensitive-team191.60s completed:
one of five selected cases passed, bootstrap failed, three maintenance cases
were not reached. Watcher's zero count is incorrect. DriverExit0 only records
the interactive wrapper; casePassed=false/targetedPassed=false is failure.

**Sufficient one-file repair:** within the existing `nodes.machine` in
`nix/tests/session-creation.nix`, set
`nix.settings.experimental-features = [ "nix-command" "flakes" ];`, with a
short comment tying it to ordinary public flake preparation in this guest.
Use the standard NixOS setting so both the developer command and user-service
worker receive the same ordinary configuration. Do not modify production
commands, add per-invocation flags/environment overrides, fabricate preparation
or preseed maintenance state. All testScript bodies, package variants, P/L/N
and equal-payload comparisons, router/failure controls, queue/goal/Stop/client
restoration/continuation assertions and deadlines remain byte-identical.
No public/persisted format, package contract, native/SDK input or live host
configuration changes. The failed run remains the negative evidence.

After main source release, D runs the existing local Nix formatting/parsing
checks and evaluated-node configuration check: the effective guest setting must
contain both features, and the diff is only this setting/comment. Preserve the
existing testScript and input/source guards; no new permanent regression or
diagnostic framework is warranted for this declarative prerequisite. Normal
commit and affected environment/fixture review precede runtime preparation.

Cheapest valid continuation is the same corrected driver build,
`nix build --no-write-lock-file --print-build-logs --out-link OWNED_DRIVER
.#checks.x86_64-linux.session-creation.driver`, reusing exact unchanged outputs
where their derivations/inputs match. Bind the new guest/config/driver and
unchanged case bodies. Then main may run the existing five-case AST selection
once with the same setup/automatic/bootstrap/three-maintenance prerequisites,
fresh owned runtime/output/tmp/IPython directories and the existing attached-tty
launcher. The first decisive result is successful ordinary public prepare and
real operation creation; all five must then pass with terminal driver0 and
casePassed=true. Keep current bounds and first-failure stop, no retry loop.
After selected success, the whole original VM remains final sequence acceptance.
No preparation success or downstream maintenance result is presumed from this
fix. Only design.md changed here; no source/check/build/evaluation/native/guest/
Git/live action. Finite brief complete; architect capacity returned.

### Automatic transcript timeout at716a: one proxy-timing diagnostic, 069204e8

2026-11-07. Bound current/environment and retained architect0 Astra/xhigh/
workspace_write confirmed. Current state and design4150+ read; applicable full
workspace documentation/lifecycle/verification and repository guidance read or
reused unchanged in this context. Lead's terminal result supersedes state.md's
still-running wording:716a five-case wrapper failed naturally1 in345.0606s;
driverExit0 with casePassed=false is failure. Only setup70.03s passed, zero of
five selected cases passed. Automatic failed; bootstrap and all maintenance
cases were unreached. D's accepted25-file packet is
`/tmp/lead-wakeup-guest-nix-D-raf8o6zl/automatic-failure-preservation/preservation.json`,
SHA256 `35e43adf05d3bfaad95a83a9a66f81da0324f25bf7c5058d7d8d5d7876bb0a49`;
original guest.log SHA256
`20347f06bbedec8f2d9d481201f50de7fae2e43a1bdb87826975999b1d40d025`.

**Established boundary.** `creation_acceptance_browser.cjs:166`, called by
create224, timed out waiting30s for visible CREATION_REPLY_ in #transcript.
The request67a892a1-124d-44f0-9e62-53006b0df893 reached ready; canonical
slug2026-11-07-accepted-session and document thread
01a1b381-995f-7483-9471-490125ba2764 agree. Document/transcript were visible,
reply absent, pageerrors empty. At00:57:15.012Z failure, exact thread/page and
events requests begun00:56:51.011 were pending without response status.
Playwright timing startTime0/requestStart-1 alone does not establish whether
bytes reached nginx. Earlier completed entries can leave the80-entry ring.
The5console resource errors lack request identity and do not identify cause.

After browser close, native passive read00:57:20.039–28.097 timed out8s;
the following Unix portal read completed in0.379s with HTTP200, exact thread,
idle status and one initial/one reply in a completed turn. That later read
establishes saved content, not its availability or rendering at failure.
The earlier manual-recovery transcript failure shares this visible boundary,
but common cause remains unproved. The accepted diagnostic-order correction
is not implicated: no completed browser thread/page was available to snapshot.
Neither the creation-lock fix nor guest Nix feature fix is reopened.

Immediately owning app.js starts independent transcript read and SSE. The host
nginx BasicAuth/proxy path precedes the portal's existing Server-Timing interval.
Some completed HTTPS requests took about19s while their portal total was below
1ms. This establishes delay outside those measured portal handlers, not whether
it was browser scheduling, network, nginx authentication, router or guest load.
Current metadata lacks proxy ingress/upstream timing. No production correction,
lower auth cost, new timeout or retry is justified yet.

**Sufficient diagnostic-only one-file package:** only
`nix/tests/session-creation.nix`. In the guest's standard nginx configuration,
add one fixture-named `log_format ... escape=json` through commonHttpConfig and
one unbuffered access_log to `/var/log/nginx/creation-timing.jsonl` in the existing
`*.workspace.example.test` virtual host via mkAfter. Preserve inherited config,
authentication cost12, TLS/proxy settings and all services. The metadata whitelist
is completion `$msec`, `$request_method`, `$uri` (not request_uri/query), `$status`,
`$request_time`, `$server_protocol`, `$connection`, `$connection_requests`,
`$request_id`, `$upstream_status`, `$upstream_connect_time`,
`$upstream_header_time`, `$upstream_response_time`, and ONLY the two existing
upstream response headers `$upstream_http_x_portal_read` and
`$upstream_http_server_timing`. Quote/JSON-escape values, including missing `-`
or multi-upstream timing strings. No credentials, Authorization/cookies,
password/hash, full headers, bodies, full request line or native payloads.

The lead's scope reduction removes all in-fixture parsing, matching and
projection. The log_format already enforces the confidentiality whitelist;
no additional filtering is needed. Keep the live timing log outside exported
creation-evidence. ONLY on the existing outer exception path, after the failed
browser command has returned/closed and before existing best-effort passive RPC
diagnostics, export at most the last1MiB of its unchanged JSONL bytes into the
already exported creation-evidence directory. Read as the existing guest-root
machine command; do not change permissions. Record original observed byte size,
truncation, capture time and missing/read-error metadata separately. A truncated
first line may remain partial; do not parse or repair it in the fixture.
Keep the original exception unconditional; missing log, read or export errors
must not prevent the remaining evidence copies. Successful execution never
exports the timing log. No browser/production source, extra request, polling,
native probe, test body, deadline, assertion or success predicate changes.

Local checks after main release: existing Nix format/parse/evaluated-node checks
for the final log_format and exact wildcard-vhost access_log; compile the embedded
Python and use the existing local diagnostic-control style to cover exact bytes
below the cap, bounded oversized export with correct metadata, missing/read-error
handling and failed export preserving the primary exception. Confirm original
case bodies and browser/native/SDK input hashes unchanged. No new permanent
test or logging framework. Commit and affected fixture/diagnostic review before
runtime. This is observation only, not a proposed auth or readiness repair.

**One next runtime operation.** Prepare the corrected existing
`.#checks.x86_64-linux.session-creation.driver` with the ordinary no-write-lockfile
build/out-link, reusing exact unchanged derivation/input-bound successes from
716a where valid. Bind the new nginx/guest/config/script to that driver; do not
claim the old driver contains diagnostics. Using the established attached-tty
interactive launcher and fresh owned output/runtime/tmp/IPython directories,
select unchanged setup/functions plus ONLY the original automatic-naming,
sensitive-retained-team subtest, with unchanged except/finally. It creates its
own prerequisite root/roster without earlier cases. Require both casePassed=true
and driverExit0 for a pass. Keep original30s transcript and all other bounds;
stop on first failure, no repeat or full-suite fallback in this operation.

After the run, correlate read-only against the already exported browser evidence:
exact method/path/time, X-Portal-Read for completed responses, and nginx request_id
plus connection/request count to distinguish duplicates. Mark missing, partial
or ambiguous matches unavailable; absence in a truncated export proves nothing.
No permanent matching algorithm is added. Compare browser elapsed with the nginx
request interval to identify time outside nginx's measured request; nginx request
versus upstream timing identifies pre-upstream delay; upstream versus correlated portal stages narrows
router versus application/dependency time. These are measured intervals, not
automatic proof of an auth/CPU/connection cause. Completion/499 after browser
close is labelled after-failure. A completed snapshot with the reply while the
DOM lacks it instead identifies the rendering boundary. Missing/ambiguous
records or a nonreproducing pass returns that precise residual uncertainty;
do not certify a cause or automatically add logging/replay. Main then decides
the evidence-supported next action. Five-case maintenance and whole original VM
acceptance remain required later; all P/L/N, equal payload, actual activation,
queue/goal/Stop/client restoration/continuation/recovery proofs remain unchanged.
Only design.md changed here; no execution/source/Git/live action. Finite brief
complete; architect capacity returned.

### Clean flake evaluation: retain explicit package recipe/output dependencies

2026-11-07. Current/environment and retained architect0 Astra/xhigh/
workspace_write reconfirmed; current state and applicable unchanged workspace
procedures read/reused, runtime AGENTS.md reread. Current clean42669fd1 contains
the reviewed10480c81 proxy diagnostic; preserve its42 added lines exactly.
The earlier716a CI failure is reproduced by B's sole corrected Nix2.35.3
source-only fresh-store evaluation, natural1/61.715s. Authoritative packet:
`/tmp/lead-wakeup-verification-716a-B/ci-context-2353-3fwdbivw/corrected-diagnosis.json`,
SHA256 `4b246d5d26930c532de5bc09127627a0bc2de2fb2bc0c7d8349cfdf7e8943b46`.
All13 pre-failure derivation identities and the invalid nhkj53 package recipe
match original CI. The registered store still contained only source0ag, with
zero derivations/outputs. Path-flake metadata differs from CI Git metadata as
disclosed in B's packet. This does not establish GC/corruption or a Nix regression.

**Mechanism and smallest representation.** sourceFor in
`nix/tests/session-creation.nix` interpolates selected.drvPath into writeTextDir.
That derivation-path string has a derivation-deep dependency: its outputs and
entire build closure. The failure is while constructing the generated flake
derivation, before any guest/build, when the computed selected recipe is not
persisted in read-only evaluation. The fixture needs that recipe file and the
selected package output, not an eager dependency on every build-closure output.
The documented narrow conversion is unsafeDiscardOutputDependency, not
unsafeDiscardStringContext. The installed Nix2.34.9 manual explicitly defines
it as converting derivation-deep context to constant path context; it does not
erase the recipe reference. See the locally read
`/run/current-system/sw/share/doc/nix/manual/language/builtins.html` and
`language/string-context.html`. These are documentation evidence, not a claim
that a corrected2.35.3 application evaluation has already passed.

**One-file implementation:** change only the drvPath interpolation to:

```nix
drvPath = ${builtins.toJSON (builtins.unsafeDiscardOutputDependency selected.drvPath)};
```

Add a short adjacent comment: retain the recipe as a file dependency; outPath
below supplies the selected output dependency, avoiding deep-closure expansion
during read-only flake checking. Leave
`outPath = ${builtins.toJSON (toString selected)};` unchanged. The serialized
path bytes for a fixed selected argument remain the same; only dependency
representation changes. Keep the existing package variants, sourceFor outputs,
additionalPaths, public prepare and all guest logic unchanged. No source seeding,
storePath existence workaround, empty-context conversion, CI skip, fake package
or extra packaging stage. No language prototype is needed before implementation.

The dependency invariant is two explicit edges: selected.drvPath as a constant
store-file dependency, and selected's normal output dependency. At ordinary
build time the recipe is materialized through Nix's normal derivation handling;
sourceFor's generated file references the exact .drv and output. Their references
retain the recipe's source/recipe closure and selected output's runtime closure
for the VM. Unneeded outputs of every build dependency are not part of the
guest's prepared-package requirement. Do not remove either edge or all context.
The same native/SDK, exact source/target P/L/N, equal ELF bytes, source ownership,
real restart, held activation, restoration, queue/goal/Stop and continuation/
recovery proofs remain intact. No public/persisted/production contract changes.

**Finite validation after main release.** Existing Nix formatting/parsing and
small context inspections must show: transformed drv string keeps identical
bytes and nonempty `path = true` context without allOutputs; the unchanged
outPath keeps the selected normal output edge; complete generated text retains
both. A fully discarded context and loss of the output edge must fail these
controls. Use existing temporary quick-check practice, not a permanent harness.
Verify the42 diagnostic lines and all unrelated source/native/SDK inputs remain
exact. Context inspection proves representation only; it does not replace the
following clean evaluation or later closure/runtime proof.

Run ONE corrected-source `nix flake check --no-build` using B's matching2.35.3
command/method: distinct owned source-only fresh store/eval-store and cache,
complete exact final source NAR/lock, no preseeded derivations or outputs,
`--show-trace --no-update-lock-file --no-write-lock-file`, max-jobs0/builders
empty. Retain before/after store facts, exact command/version/source identity,
all declared check evaluation results and natural exit. Reuse B's already
prepared executable through its recorded environment; do not repeat716a or
silently substitute the ambient CLI. Preserve the original/parser failures.
Expected scheduling basis is the observed62s; use a fresh watcher and the
existing10min reassessment/20min cap. Any failure stops; no retry, store seeding
or wider context removal. This is the corrected clean-evaluation proof, not
check realization or runtime acceptance.

Main owns allocation/Git: make one focused corrective commit on42669fd1 after
quicks, preserving its diagnostic commit and earlier history rather than folding
this unrelated dependency fix into the42-line diagnostic. Bind any precommit
evaluation to unchanged committed source NAR/lock instead of rerunning solely
for commit metadata. Obtain the affected dependency/fixture/history review;
10480c81's unchanged diagnostic acceptance stays valid. Do not build the held
42669 driver graph. After clean evaluation and review, prepare only the corrected
ordinary session-creation.driver. Its closure receipt must include both generated
source flakes, their exact selected .drv files and package outputs. After
construction, inspect each flake's drvPath/outPath and registered references;
do not infer retention from pathname text alone. Changed-source derivations need
fresh bindings; exact unchanged outputs may be reused under existing rules.
Then continue the already settled one-automatic proxy diagnostic, later five-case
maintenance/public-prepare proof and whole-VM acceptance, with no new runtime
allocation from this note. Only design.md changed; no application evaluation,
prototype, build, source/Git/native/guest/live action. Sufficient finite brief
complete; architect capacity returned.

### CI716a prepare refusal: direct-team temporary preset namespace

**Finding and evidence limit (2026-11-07).** Verified current session/environment
and retained architect0 Astra/xhigh/workspace_write. Exact CI log
`/tmp/lead-wakeup-R-publication-716a-tkuar84c/ci-completion-20261107T013222Z/creation-job-128240299412.log`
SHA256 `a15e3be1d03520a7086d38b753c94d57a9d9daf8cc8ebd75e3a2b809223a3d94`
records the first maintenance bootstrap's public prepare refusing at15144:
`portal creation receipt has an invalid filename: .direct-team-2363313347.json`.
The completion packet SHA256 is
`8aa24a93d54496d327cd691218ca6734564b446a92169be2e8195497f66970c4`.
Thirteen subtests finished including setup; no maintenance operation/switch
acceptance follows. The missing browser diagnostic is secondary. The separate
local automatic-transcript delay remains unresolved and is not explained here.

This is a supported writer/reader namespace conflict. In
`portal/internal/web/creation.go:1044,1083`, `writeDirectTeamPreset` creates
`.direct-team-*.json` inside `creationDirectory()`, then supplies that private
file to ordinary `dev-session --team-preset`; removal is deferred until its
initialization caller returns. The ordinary consumer at
`libexec/dev-session:5316` validates the private bounded preset and its shape.
It is command input, not a durable creation receipt. Go's existing CreateTemp
implementation supplies a decimal random suffix. In contrast,
`libexec/workspace-host:2749` treats every JSON filename except completion
evidence as a receipt. Its receipt grammar requires an alphanumeric first
character, so the ordinary auxiliary file necessarily refuses. The log does
not establish this individual file's contents, owner, live writer or abandoned
lifetime; none was inspected. No corrupt durable receipt or failure of bounded
pause is demonstrated.

**Smallest implementation package: two files.** In `libexec/workspace-host`,
add one named, anchored auxiliary-name predicate alongside the existing receipt
and evidence constants: `\A\.direct-team-[0-9]+\.json\z`. In
`unfinished_portal_managed_creations`, exclude only that reserved name before
receipt parsing, with a short comment identifying `writeDirectTeamPreset` as
its owner. Do not skip all dotfiles, all invalid names, or parse failures. The
reserved leading-dot namespace cannot be a valid durable receipt identity.
No other scanner, writer, filename, directory, schema or API changes are needed.
Add focused regressions in
`test/workspace_host/agent_team_registration_test.rb`; application ownership
and its short Git window remain main-assigned. This boundary is disjoint from
B's Nix sourceFor correction and preserves the42 reviewed proxy diagnostic lines.

The scanner neither opens nor removes the auxiliary file and grants it no
lifecycle authority. Therefore a partial live write, ordinary removal, or an
abandoned preset cannot create a receipt parse/absence race in this path. Keep
the private creation-directory check and all durable receipt checks unchanged:
strict JSON/duplicate keys, bounds, schema branching, ownership/mode, exact
workspace/slug, direct-team/managed shape and cancellation-without-effects proof.
Running/paused/failed durable receipts and ordinary lifecycle journals still
block the public gate. Do not mark them ready or renew/retry initialization.
`saveCreation` remains unchanged: private `.creation-*.tmp`, sync/close, rename
to exact `slug.json`, then directory sync. All existing transition and creation
locks, preset consumer validation and ordinary recovery stay unchanged.

Compatibility requires no migration or cleanup: the corrected reader recognizes
the existing writer's temporary namespace from both retained and new packages.
The writer and durable formats remain identical. An older reader retains the
same refusal if such a file exists; this correction does not repair an already
running older binary or authorize bypassing its refusal. Supported profile
changes remain forward-only. No live upgrade or session cleanup is allocated.

**Focused controls and release sequence.** Use existing disposable Ruby fixtures:

- A numeric `.direct-team-2363313347.json` with an open, incomplete synthetic
  payload plus a valid ready receipt passes the scanner and existing lifecycle
  gate. Repeat with the auxiliary closed/retained and ordinarily removed; assert
  the scanner did not alter or delete it. No sleep, native process or real state.
- With the same auxiliary present, managed and direct running receipts still
  produce the exact blocker and make the lifecycle gate refuse. Malformed durable
  JSON still refuses. Existing schema, duplicate-key, private-file, bounds and
  cancelled-effect controls remain intact.
- Near misses `.direct-team-.json`, `.direct-team-invalid.json` and an unrelated
  hidden JSON name still raise invalid-filename errors. A nonhidden
  `direct-team-2363313347.json` is a normal receipt name and must be parsed and
  validated. The positive regression against the retained old scanner must fail
  at the original invalid-filename refusal, not a setup error.

After source release, run syntax and the aggregate loader's focused creation
controls in the repository Nix environment, for example
`nix develop --no-write-lock-file -c ruby -c libexec/workspace-host` and
`nix develop --no-write-lock-file -c ruby test/workspace_host_test.rb --name '/portal_.*creation|provider_plan_receipts|recover_archive_refuses_unfinished_or_invalid_creation/'`.
Keep new tests inside that selector; report actual counts/skips/duration and the
old-source negative control. Expect seconds once the environment is ready;
an uncertain environment build returns to main for the existing watched path.
No new Go test, harness, stress campaign or permanent diagnostic is necessary.
One focused corrective commit and affected final review follow quick success;
preserve prior sourceFor/proxy history and unchanged acceptance evidence.

Combine both necessary source corrections before the next driver build. Main
owns the matching clean Nix evaluation after review, corrected
`checks.x86_64-linux.session-creation.driver` preparation and exact source/package
closure bindings. The existing selected prerequisite/maintenance cases then
exercise public prepare and real activation/restoration with exact P/L/N and
equal payload, queue/goal/Stop/continuation/failure recovery unchanged. Their
selection does not reproduce all preceding CI creation scenarios; the final
whole original VM remains required. Keep the separately authorized one-automatic
proxy diagnostic in its existing scope and order, without treating it as this
regression's proof. Stop on a concrete new failure and retain its primary result;
no blind retry, timeout change or temp-file deletion to force acceptance.

Only this design note was changed. No application edit, check, evaluation,
build, source/Git/native/browser/guest/live or lifecycle action was performed.
Sufficient brief complete; main owns release and architect capacity is returned.

### 6a9 driver request returned the source: command-boundary correction

2026-11-07, package907a3b77. Current/environment and retained architect0
Astra/xhigh/workspace_write match. Read current plan/state and accepted sourceFor
brief; applicable unchanged guidance reused. No application change is proposed.
Combined review69c43c4f and exact6a9 clean2.35.3 evaluation688341ee remain accepted.

**Established execution, bounded classification.** In
`/tmp/lead-wakeup-verification-716a-B/driver-6a9-7dihktvj`, command.json and
launch.json agree on absolute executable
`/nix/store/kp71jf0isr8pix0nn2lx2x3hj3vasii5-nix-2.35.3/bin/nix`, build flags
and the sole `path:SOURCE#checks.x86_64-linux.session-creation.driver` argument.
SOURCE is `/nix/store/0vaxf4zm02dx544hwq8kn2zy99xifkx9-source`, also the cwd.
The retained watcher-events item11 directly executes `Popen(c['argv'], cwd=...,
env=..., start_new_session=True)` without shell argument interpretation. It
removes NIX_REMOTE/NIX_CONF_DIR/NIX_USER_CONF_FILES/NIX_CONFIG, retaining normal
host environment. Selected nonsecret variables are recorded; a complete private
environment/configuration dump is neither available nor necessary. Earlier
item7 failed its assertion before Popen and is not another build attempt.

PID1752431 ran02:16:29.429899–29.522674UTC, natural0/0.092727s. Its stdout is
the one-element JSON array containing SOURCE, stderr empty, and outlink resolves
to SOURCE. B's terminal-binding.json confirms no driver executable/test script
or driver drv/output record. Retained source path-info identifies a source NAR
with deriver null; source bytes remain unchanged. The current binary is a regular
executable, not a shell wrapper; its same-version help executes successfully.
There is no evidence of a wrong executable, truncated argv, second target or
launcher failure. These records establish failed target binding, not a successful
driver build or source/check failure.

Matching2.35.3 `nix --help` and `nix build --help` distinguish flake attributes
from store-path installables; the latter are fetched/linked. The observed result
is consistent with that store-path interpretation, but the help does not explain
why this full path-scheme/fragment argument chose it. Matching parser source is
not present in the inspected executable output and its recorded .drv is absent;
do not claim a proven parser bug or acquire source to extend this package.
Prior successfulc81 command used `.#checks.x86_64-linux.session-creation.driver`
from its non-store worktree. It proves that earlier command/output only; it does
not validate the new absolute store-source syntax. Do not guess that replacing
the argument with `.#...` inside the store will fix this failure.

**One decisive next validation, then the ordinary build.** After main release,
use the same absolute2.35.3 binary and host shared-store environment. Explicitly
select the driver through the documented `--expr` path, avoiding ambiguous
positional flake/store interpretation. Define the expression as:

```nix
(builtins.getFlake "path:/nix/store/0vaxf4zm02dx544hwq8kn2zy99xifkx9-source?narHash=sha256-CRhZpx0FZ9ZmMUzDgSfFe4ns778%2FN6ixAPRK8M1ocKI%3D").checks.x86_64-linux.session-creation.driver
```

The NAR query binds the already accepted source hash and supplies a locked path
reference; it changes no source or dependency selection. Matching `nix flake
--help` documents path URLs and narHash. No `--impure`, override-input, source
copy, new default target or application edit. Pass the expression as one literal
argv element, with no trailing positional argument.

Run once: `NIX_BIN derivation show --no-update-lock-file --no-write-lock-file
--expr DRIVER_EXPR` (NIX_BIN/DRIVER_EXPR denote the exact values above).
Matching help documents this command as evaluating the selected store derivation
and returning its JSON representation. It is recipe preparation, not a build or
guest run. Require exactly the selected driver .drv and its concrete `out` path,
distinct from SOURCE; retain the actual2.35.3 JSON schema rather than assuming an
older schema from memory. This is the missing positive selection fact. Preserve
full stdout/stderr/exit and source identity in the existing owner packet. Stop
at the first error, non-derivation/source-only result, unexpected realization,
changed source/input or missing output mapping; do not try another syntax in the
same package. A normal full evaluation previously took72s; retain main's finite
watcher/reassessment rules and bound this preparation at10min, without launching
any build from an uncertain result.

Only after that positive mapping, the shortest unambiguous build is the same
ordinary binary/flags with sole installable `EXACT_DRIVER_DRV^out`:
`NIX_BIN build --json --print-build-logs --no-update-lock-file
--no-write-lock-file --max-jobs 4 --cores 4 --out-link NEW_ROOT/driver
EXACT_DRIVER_DRV^out`. This standard output-selection syntax is documented in
the matching help. Reuse the selected recipe; no second flake evaluation or
whole clean-evaluation replay. Use a new owned evidence/output root, preserving
all failed6a9 records and the source outlink unchanged. Main owns execution
allocation; keep the existing10min phase reassessment/40min build cap and
first-failure/no-retry rule, including unexpected local kernel builds.

Success requires more than exit0: stdout's output and real outlink must equal
the selected recipe's exact out path, with ordinary executable
`bin/nixos-test-driver` and its retained test script/configuration. Preserve the
driver recipe/output/NAR and dependency bindings, including both generated
source flakes and their selected package recipe/output closure from the accepted
sourceFor brief. Name or executable presence alone is insufficient. Missing
binding stops before any guest. Reuse actual unchanged derivation/input evidence
only; no native/SDK/receipt/sourceFor remedy is reopened. This command correction
needs no application commit/review rerun. One-automatic diagnostic, selected
maintenance cases and whole-VM acceptance remain separate later allocations.

Only design.md changed. Read-only matching executable help was the only new Nix
operation; no application evaluation, instantiation, build/dry-run/substitution,
test, Git, input, native/guest/live/profile/claim/lifecycle action occurred.
Sufficient finite brief complete; architect capacity returned.

### Exact6a9 CI: independent generic-source fixture correction

2026-11-07, package4328331a/A. Current/environment and retained architect0
Astra/xhigh/workspace_write confirmed; current plan/state and unchanged applicable
guidance read/reused. Exact42327281138/attempt1 fast log SHA256
`898eeaf19cb77673861df11386d203cf915785789f8b28f6da16e286a47ec58a`, retained under
`/tmp/lead-wakeup-R-publication-6a9-7rm5kwhx/ci-disposition-20261107T022609Z`,
shows successful check evaluation followed by generic-source2h6 builder refusal
of `test/workspace_host/maintenance_test.rb`. This is distinct from creation's
missing bison source and from earlier positional driver selection.

The owning flake check intentionally rejects site-specific strings in all source
contents and filenames. The emitted file's sole match is line687:
`git@github.com:vpsfreecz/maintenance-fixture.git`. The retained-attempt recovery
test needs canonical SSH metadata, not a particular organization; it explicitly
does not contact this remote. The ordinary validator in
`libexec/workspace-coordination.rb` accepts generic canonical SSH remotes.

Sufficient independent one-file change: replace that literal with
`git@github.com:example/maintenance-fixture.git`. Preserve the actual claim
predicate, saved source/target/artifact/attempt/reservation identity, all success
and mismatch assertions, the existing local Git fixture and no-remote behavior.
Do not modify generic-source, split/encode its forbidden literal, add exclusions
or change production. No format, compatibility, deployment or recovery change.

After main release, Nix Ruby syntax and the aggregate loader selection
`ruby test/workspace_host_test.rb --name test_maintenance_source_recovery_validates_retained_attempt_before_intent`
must pass with unchanged assertions. Apply the exact existing generic-source
content/name predicates to the corrected source and verify zero matches; the
retained original file must still trigger its content predicate. Use the existing
command/check machinery, not a permanent test framework. This is a seconds-scale
fixture correction once the environment is available; any unexpected failure
stops expansion. Packaged generic-source remains an ordinary final check.

Main may release C independently while B's generated-source diagnosis continues.
This belongs to the owning maintenance test history; ordinary final consolidation
into that unmerged owning change is appropriate under main's Git sequencing,
retaining old/new source/history evidence. A focused correction can be committed
first if needed to avoid blocking the independent package; no history rewrite
is assigned by this note. Final quick/committed affected review precedes long
checks. All sourceFor/proxy/native/SDK and other test bytes remain untouched.

### Exact6a9 CI: generated-source construction stops on missing bison input

2026-11-07, package4328331a/B. The separately retained creation log SHA256
`26a62b7228d16a57f26158d5f177cf3ece289d0f0f7cc8546d604c8a7f6b2fb9`
in the same CI disposition directory shows selected package3pl completing
install/fixup, then building generated flake recipeagwnf159 at3453 and reporting
invalid9vm1 bison source at3454. There are no VM subtest markers. This is a
construction failure after successful evaluation, not a guest/native failure.
No cache/GC/network or Nix-regression cause follows from those two lines.

**Exact existing graph facts.** Read immutable local recipe
`/nix/store/agwnf159fnbslm7nfrlkn7frbjg709dx-flake.nix.drv`, identical in identity
to CI. Its output is `j7nvsbiffwv5hs4m8jrkn70xa5kggvq8-flake.nix`; it has
selected `n5kvvd7rp91az4n4szf752sy81ppc5ap-dev-workspace-0.2.0.drv` both as an
inputSrc and as an ordinary inputDrv requiring out. Generated text contains
that exact recipe and `3plw8fx8b3b7ymvh34shbhn1wqchsfky-dev-workspace-0.2.0`.
The other source recipe1xgf retains the corresponding q2j/6yms original tuple.
Thus the accepted constant-recipe and selected-output context edges really are
present; neither has silently disappeared from the construction recipe.

The specific missing file is a real transitive recipe dependency. A bounded
read of45 immutable recipes established the chain n5kv -> tmux197bmhq ->
bisonx1w0jlg -> source-fetchhcf0pv0, whose out is
`/nix/store/9vm1ihdg1ysmrjdbb80g834iizzxb4yk-bison-3.8.2.tar.gz`, fixed SHA256
`06c9e13bdf7eb24d4ceb6b59205a4f67c2c7e7213119644430fe82fbd14a0abb`.
B's retained6821-path recipe requisite list contains these recipes, not that
tarball output. It is recipe-graph evidence, not realized build-closure proof.
The current9vm1, package3pl and generated-sourcej7 paths are absent on a passive
filesystem read; no store mutation or build was used to establish this.

There is also an exact downstream `1509bap02wm13x5hvwl18047p5nshczp-closure-info.drv`
whose structured exportReferencesGraph includes both generated sources, both
packages and the guest system. CI's output does not identify the first Nix
operation that requires9vm1: generated-flake input/sandbox assembly versus
subsequent reference-graph export. The recipe graph alone cannot select between
these phases. The earlier sourceFor brief's context controls and clean evaluation
remain valid, but its proposed build/guest closure retention is still unproved.
Do not treat successful package output or a recipe requisite list as that proof.

**One missing fact and bounded validation.** No source correction is released
from this evidence. The next discriminator is construction of only the exact
generated source whose build was announced, excluding the VM closure export.
After main release, use B's same rooted2.35.3 binary/shared-store environment:

```text
NIX_BIN build --json --no-link --print-build-logs --show-trace --debug
  --max-jobs 4 --cores 4
  /nix/store/agwnf159fnbslm7nfrlkn7frbjg709dx-flake.nix.drv^out
```

This is one exact immutable recipe realization, not an application evaluation,
full driver/VM replay, sourceFor change or cache-preseeding step. Main assigns one
owner/fresh watcher and existing compact evidence root; record command, source,
natural result/full stderr and read-only before/after validity of9vm1, selected
out3pl and generated outj7. Retain the existing10min phase reassessment/40min
build cap and stop on the first actual failure or unintended build. No retry,
source fetch for investigation, deletion, forced cache miss or second target.
Normal dependencies of this single selected build remain ordinary build work.

If the same missing9vm1 refusal occurs, the trace/target isolates the defect to
generated-source construction; report its first requiring operation for a
one-file sourceFor repair brief. If it succeeds, require exact recipe/out mapping
and actual generated text plus registered references, and report whether9vm1
remained unavailable or was realized normally. A warm success or newly realized
tarball does not erase CI or establish cold-store retention; stop with that
specific residual gap rather than automatically running closure-info/fullVM.
This single boundary result is sufficient to choose the next source correction
or the precise downstream question; no broader diagnosis campaign is proposed.

Any consequent source repair belongs only to `nix/tests/session-creation.nix`
unless the discriminator demonstrates a necessary wider boundary. It must retain
ordinary public prepare and exact selected recipe/output ownership, source and
target P/L/N, equal native payload, all cases/assertions/bounds and42 proxy lines.
It must pass quick dependency controls and committed affected review, then one
matching source-only clean2.35.3 evaluation regression and actual generated-source
construction/reference proof. Do not erase context, substitute fake packages,
revert to the failed read-only deep expansion, seed a store to certify success,
disable checks or change native/SDK. C's generic fixture correction is independent.

Explicit driver selection3cg/96cv remains successful selection-only evidence;
held Stage2 never launched. Final corrected source requires new exact graph/input
bindings before driver/runtime acceptance. Earlier clean evaluation/review and
failure records remain unchanged. Only design.md was edited; no application
source/check/evaluation/build/test/network/CI/Git/live action. Capacity returned;
main owns source and execution release.

### Restore the generated-source diagnostic through ordinary instantiation

2026-11-07. Current/environment and saved architect0 Astra/xhigh/workspace_write
confirmed; applicable full workspace/repository guidance reused, agent-teams
procedure reread. B's sole diagnostic at
`/tmp/lead-wakeup-verification-716a-B/generated-source-6a9-u28f9edc` ended
natural1/0.619s before construction. Matched stderr SHA256
`d9f59abbf15bba0089e85b65498035cf610dd3769f10ff82b9b39fc8ce0f0e58` shows
the build daemon trying to obtain recipeagwn, receiving cache404s and refusing
before its builder. Physical ATerm/nonnull path-info metadata did not establish
availability to that build. The conflicting prior validity observations do not
establish GC, database damage or configuration cause. No9vm1 diagnostic result
was obtained, and the cold CI gap remains open.

**One complete conditional execution package, no source change.** Use ordinary
instantiation from immutable reviewed6a9, retaining the resulting recipe graph,
then perform the already selected single generated-source build. This avoids
inventing an exposed generated-source attribute: it is lexical fixture data,
whereas the driver's existing public flake attribute identifies its exact graph.
Instantiating that graph does not realize the driver, guest system or VM.

Use only binaries below
`/nix/store/kp71jf0isr8pix0nn2lx2x3hj3vasii5-nix-2.35.3/bin`, including its actual
`nix-instantiate` and `nix-store` entrypoints. Keep the previous ordinary host
environment with isolated-evaluation overrides removed; explicitly set
process-local `NIX_REMOTE=daemon` and `--eval-store daemon` so instantiation,
validity reads and construction address the same host store. Do not change
global configuration. DRIVER_EXPR is the exact already successful expression:

```nix
(builtins.getFlake "path:/nix/store/0vaxf4zm02dx544hwq8kn2zy99xifkx9-source?narHash=sha256-CRhZpx0FZ9ZmMUzDgSfFe4ns778%2FN6ixAPRK8M1ocKI%3D").checks.x86_64-linux.session-creation.driver
```

After main release, in a fresh owned evidence root RUN, invoke once:
`NIX_DIR/nix-instantiate --eval-store daemon --add-root RUN/driver-recipe --indirect --expr DRIVER_EXPR`.
Pass the expression as one literal argv element; no `--eval`, read-only mode,
unlocked reference, positional default, alternative source or manual ATerm
registration. Installed help distinguishes default instantiation (writes store
derivations) from `--eval` (hashes/discards them); --add-root retains its result.
This replaces the insufficient bare-path preparation, not the application.

Before any build, require natural instantiation success, the retained root
resolving to exact driver3cg2wpinxvdnqyf66ymy7179rcwkm774 and its exact out96cv
mapping, and same-daemon2.35.3 `nix-store --check-validity` success for driver3cg,
generated recipeagwnf159 and selected recipen5kvvd7. Do not use exit0 from
`--print-invalid` or nonnull cached metadata alone. Verify driver3cg's direct
input includes agwn; agwn bytes must still have SHA256
`a07ce7197838f553d8f83279bf228712f0a4fb34d851ff3aa9ce84129d58d665`, mapping
to j7nvsbiff and exact selected n5kv/3pl. These checks bind the child build to
fresh ordinary source instantiation, not merely a retained pathname. Record the
root and retain it across the build; this note allocates no cleanup action.

Only with those checks positive, run once against that same daemon:
`NIX_DIR/nix build --eval-store daemon --json --no-link --print-build-logs --show-trace --debug --max-jobs 4 --cores 4 /nix/store/agwnf159fnbslm7nfrlkn7frbjg709dx-flake.nix.drv^out`.
No whole-driver, closure-info or VM target. Record before/after store validity
for j7,3pl,9vm1 and the actual first result. Success requires exact j7 output,
generated text and registered references; report whether9vm1 remained absent
or was realized by normal dependencies. A missing9vm1 failure is now the desired
phase evidence, not permission for another retry. A warm success does not close
the cold CI gap. Preserve all original receipts/outlinks and their conclusions.

Main assigns B and the existing watcher workflow one conditional package:
10min instantiation cap, existing10min build reassessment/40min cap, first
error/mapping/validity mismatch stops before further work. No alternative syntax
or store repair on failure. Rooting source-derived recipes does not preseed
dependency outputs or certify them; normal builds/substitutions remain subject
to the previous diagnostic boundaries. Recheck source NAR and owning inputs;
current06025's URL-only change is not substituted for this exact6a9 diagnosis.
No sourceFor/native/SDK/product change or application review rerun is proposed.
The earlier source review, clean evaluation and positive expression selection
remain evidence for their original scope only.

Only design.md changed. Read-only evidence/source/help inspection only; no
instantiation, registration, copy, evaluation, build, network acquisition,
Git/profile/claim/live or lifecycle action. Sufficient brief complete; capacity
returned and main owns execution release.

### Generated-source success: engine binding and remaining CI proof

2026-11-07. Current/environment and saved architect0 Astra/xhigh/workspace_write
confirmed; unchanged applicable guidance reused. Main accepted B's exact6a9
terminal receiptc7fe2af5 at
`/tmp/lead-wakeup-verification-716a-B/retained-generated-6a9-6ha3srf4/terminal-receipt.json`.
Ordinary instantiation14.388s and sole agwn construction685.998s succeeded.
Actual j7 text and registered direct references are exactly selected recipen5
and output3pl. Its4437-path registered closure contains both and excludes9vm;
9vm was invalid/physically absent before and after. Trace contains neither9vm
nor downstream1509. This proves construction/reference retention in that run,
not downstream VM export or the original CI engine/context.

**Client and engine are different.** Receipt versions identify the2.35.3
entrypoints only. The authorized read-only query using that exact client,
`nix store info --store daemon --json`, returned
`{"trusted":true,"url":"daemon","version":"2.34.9"}`.
Read-only `systemctl show nix-daemon.service` reports MainPID1642, start/active
2026-10-30 23:06:54CET (before the build), and ExecStart
`/nix/store/z4wkkj3ncr69vgrb3020saqx1c8mfsjj-nix-2.34.9/bin/nix-daemon`.
The optional /proc1642/exe readlink was unavailable; no access override was used.
Protocol version plus unchanged service lifetime is the supported engine binding.
Earlier phrases “same2.35 daemon” mean same daemon endpoint accessed by2.35.3
clients; they must not be read as proof of a2.35.3 execution engine.

Retained CI creation log26a62b72 lines230,427,534,541–543 shows a fresh2.35.3
installer, exactkp71 package, and service links into its new default profile.
The already availablekp71 service file names its own2.35.3 nix-daemon executable.
This supports CI's installed2.35.3 daemon context; no CI runtime version handshake
was retained. Guest2.34.8 package lines are build inputs, not the CI host daemon.
The engine difference does not establish a version regression or explain CI.

**Disposition.** The successful run rules out an unconditional claim that the
two sourceFor edges were absent or that constructing j7 always needs9vm. It does
not prove construction under the CI-installed engine, nor relocate the CI error
automatically to closure-info. Keep sourceFor unchanged; no context erasure,
deep-context reversal or other source correction is justified. C's06025 URL-only
package remains independent and complete as source work; main owns review timing.
Its changed source identity does not inherit exact6a9 runtime acceptance.

**One minimal further validation, after main release.** Test only agwn's
construction using the existingkp71 Nix2.35.3 engine directly in a new owned local
chroot store RUN/store. Matching `nix help-stores` explicitly documents an absolute
root as a direct local engine, without the daemon, retaining logical `/nix/store`.
It requires Linux mount/user namespaces; setup refusal stops the package rather
than changing host services or disabling isolation. No new daemon/service,
configuration deployment, source acquisition, flake evaluation or instantiation.

Reuse accepted inputs through ordinary `nix copy --from daemon --to RUN/store`:
the exact registered agwn recipe closure and its three direct input outputs
(selected3pl, bashrzl7 and stdenvmhmv), as bound by the existing immutable recipes.
This avoids repeating package compilation/checks. Copy only those allowlisted
inputs and their ordinary references; locally built unsigned inputs may use
per-copy `--no-check-sigs` into this disposable owned store, with exact receipt
hash binding and no change to global trust. Do not copy j7,9vm,driver96cv,
closure-info1509 or a whole host store. Before the build require same-store valid
agwn/three inputs, exact agwn SHAa07ce719 and outj7 mapping, and invalid/absent
j7 and9vm. No missing output is seeded or accepted as proof.

One target command, using the absolutekp71 binary and explicit RUN/store for
both stores, is:

```text
nix build --store RUN/store --eval-store RUN/store --json --no-link
  --print-build-logs --show-trace --debug --max-jobs 1 --cores 1
  --option build-users-group '' --option builders '' --option substituters ''
  /nix/store/agwnf159fnbslm7nfrlkn7frbjg709dx-flake.nix.drv^out
```

The process-local single-user build setting belongs only to this owned local
store. Keep sandboxing; unset inherited NIX_REMOTE and previous evaluation-store
overrides. Explicit local store and empty remote builders bind execution to the
2.35.3 process, not the host2.34.9 daemon. Log actual binary/version/store URL,
input mapping and target command. Normal input copy is preparation; no target
substitution or network fetch is needed for this writeTextDir construction.

Use the existing watcher/evidence workflow, one copy/preflight/build package,
10min phase reassessment and40min total cap. The target itself should take
seconds after input copy; unexpected dependency realization, missing input,
namespace/setup refusal or first build failure stops with its exact phase.
No alternate store mode, privilege escalation, input repair or second target.
Success requires actual construction (not an existing/copied j7), exact output
NAR/text and registered n5+3pl references/closure, with9vm still unavailable.
Failure must identify the first engine operation requiring9vm or the precise
other error. Either result is engine-specific construction evidence, not a
complete controlled-version regression claim or whole cold-CI acceptance.
Stop after this result; downstream export/full driver/VM remains unallocated.

Preserve source/input/public prepare/P-L-N/equal-native/proxy/case boundaries,
original failures and retained roots. No application change/review rerun follows
from this design alone. Only design.md changed; permitted daemon info/service
metadata reads and local help were performed, with no source/Git/evaluation/
build/copy/root/service mutation or CI/network acquisition. Capacity returned;
main owns the next execution and acceptance decision.

### Exact06025 monitor dispatch failure: retain the missing phase evidence

2026-11-07, architect package7c3a847b. Current/session environment and saved
Astra/xhigh/workspace_write verified; workspace and owning repository guidance
read/reused. Exact06025 CI42334351045 attempt1 creation128287789516 failed before
VM in `TestMonitorPortalWorkerDeliversPastBlockedOperation/dispatch`,
`portal/internal/web/monitor_test.go:236`. Retained disposition51ec3ad4 and raw
loga9882375 under `/tmp/lead-wakeup-R-publication-06025-ukx8ns6u/ci-disposition-20261107T034243Z`
bind the failure. Lines3067–3073 show B's original terminal event still pending,
nil options/receipt, no admitted epoch and zero fake sends. The prior blocked
assertion passed. Package/driver dependency errors are secondary; no VM acceptance.

**Established mechanism and limit.** `web/monitor.go:131–169` dispatches saved
events before observations, with separate250ms batch contexts in this test and
50ms item contexts. Cursors advance before admission. `monitoroperation/store.go`
lists validated atomic snapshots sorted by ID, so reported A precedes reported B
in the dispatch case. `DeliveryService.Dispatch` takes generation admission,
Store.Get, fixture session admission and a second operation transaction before
Ready. A's fake Ready waits for its context, then Dispatch saves held status;
that real save performs file sync, rename and directory sync without a context
parameter. Time spent there can exhaust the remaining batch before B. B can also
fail generation/operation admission before its pending event is changed. The
fixture has no native/SDK handshake or asynchronous delivery client; its fake
session lock is a no-op and the server has no configured monitor client to start
a competing background worker. This is not evidence of native contention.

The synchronous worker returned and B's Store.Get succeeded under the2s parent.
A Ready entry is proved; B Send entry and accepted persistence did not occur.
The test discards the worker error and fails before printing the cursors. Its
0.84s includes server/start/report setup before these worker budgets, so it cannot
identify their failing interval. Batch expiry, pre-publication dispatch error and
their precise cause remain unresolved. No production starvation, filesystem
latency cause, flaky-test classification or timeout correction is established.
The accepted independent delivery/observation budgets and cursor design remain.

**One narrow next package, after main allocation.** Only
`portal/internal/web/monitor_test.go`, temporary diagnostic additions around this
test and its existing fakes. Keep2s/250ms/50ms, both subtests, real Start/Report/
Store/Dispatch, all original assertions and synchronous cancellation unchanged.
Retain the run's returned error, both cursors, elapsed time and parent ctx.Err
before any fatal assertion. Collect a small ordered in-memory trace at existing
LockSession entry/release, Resolve, Ready entry/exit, Prepare, Send and
ObserveUtility entry/exit callbacks. Record only fixture operation/owner,
relative monotonic time, context deadline/error and callback result; no envelopes,
headers or generic tracing interface. Append metadata during the pass and print
once afterward, including on assertion failure, to avoid logging I/O inside the
50ms waits. Preserve the exact blocker wait on ctx.Done and record its return.
Include A/B status/read errors after return using ordinary Store.Get; never
replace the failing B snapshot with a retry. No new goroutine, clock injection,
production hook, store implementation, error exemption or timing change.

Interpretation is source-bounded: nextEvent=1 after positive A readiness means
the delivery loop stopped before B; with its two known refs the remaining loop
gate is the delivery context. nextEvent=2 means B was selected, not that it was
admitted. B LockSession entry proves its first read completed; B Ready proves
its transaction and owner validation succeeded; Prepare/Send locate the later
boundary. A's lock release follows its held-save attempt. A saved held status
proves publication, not successful final directory sync; retain the error too.
Context/error metadata
must support any timing diagnosis; batchErr is only the last error and observation
may overwrite an earlier one. If still ambiguous, report that exact interval;
do not fabricate a root cause or expand into production instrumentation.

**Finite checks and stop.** In the declared Nix environment, from `portal/`, one
bounded diagnostic command is `go test -mod=readonly ./internal/web -run
'^TestMonitorPortalWorkerDeliversPastBlockedOperation$' -count=10 -failfast -v
-timeout=60s`. This is one small repeat batch, not a full package/VM reproduction
or a load campaign. Stop at its first failure or completion; no retry, artificial
load or second budget. Preserve the command/source delta and phase trace. A green
batch is non-reproduction only; main must resolve the remaining CI evidence gap
before accepting a repair. The blocker entry/ctx cancellation plus B's accepted
original message/exactly one send and cursor assertions remain the positive and
negative controls. For any subsequently justified final test change, focused
quicks also retain `TestMonitorPortal` siblings and the existing monitoroperation
delivery/revocation/concurrent-dispatch/observation tests; no new framework tests.

No behavior fix or history rewrite is released by this diagnosis. Keep temporary
instrumentation separate until its result supports the smallest final correction.
The owning monitor capability is58e87f9d; main owns any ordinary consolidation,
retained06025 failure reference, replay equivalence and affected review. Final
committed quick-checked source needs that review before packaged/long acceptance.
No persisted-format, API, native/SDK, compatibility, deployment or recovery change
is proposed. Existing identity, ownership, durable outcomes, uncertain-send and
cancellation controls stay intact. The separate original6a9 Nix export question
remains parked; no Nix or guest target added. Only design.md changed, no source or
execution action performed. Brief complete; capacity returned to main.

### Monitor diagnostic disposition: test the retained-cursor contract directly

2026-11-07. Current/environment and saved architect0 Astra/xhigh/workspace_write
confirmed; unchanged applicable guidance reused. Main accepted B's receipt
`/tmp/lead-wakeup-verification-716a-B/monitor-phase-06025-vikely82/terminal-receipt.json`
SHAf49c2e01. Actual patch and traces show ten successful runs of both subtests;
dispatch A reaches its deadline, publishes held, and B reaches every callback
and accepted persistence. Dispatch workers took73.7–79.1ms, including4.77–6.71ms
between A Ready exit and first session-lock release. This is non-reproduction.
The retained+78/-6 diagnostic is uncommitted, sole changed source path;06025 is
the reviewed/published baseline, not the current working-tree bytes.

**Contract decision.** The only production caller, `startMonitorOperations`,
retains both cursors outside its ticker loop, makes fresh20s batches with5s item
caps, and continues after an error. `runMonitorOperations` advances cursors before
admission and stops a pass when its batch context expires. Accepted review R1 in
review.md requires independent delivery progress and prevents A consuming every
delivery opportunity. It does not require B in the same250ms test pass when
legitimate admission/persistence exhausts that pass. Progress across bounded
passes, subject to successful admission/storage and continuing worker operation,
is the supported contract; there is no unconditional finite-pass latency SLA.
Independent delivery/observation budgets and item bounds remain essential.

The single-pass assertion is a stronger fixture scheduling assumption, not a
public guarantee. This mismatch can be corrected independently of the unproved
CI cause; CI may instead have selected B and failed before publication. Main's
current5685d9a clarification permits considering a bounded contract-aligned
test. The fixed two-pass control below replaces the provisional diagnostics-only
disposition. It neither retries a failed B nor changes the product contract.

**One sufficient source package for main allocation.** In
`portal/internal/web/monitor_test.go` only; use the existing worker parameters,
fake callbacks and real Start/Report/store. Keep the observation subtest's original
single250ms/50ms pass, positive canceled observer, accepted B, exact message/send
count and cursor proof. It retains independent delivery/observation and per-item
bound coverage. Its expected observer DeadlineExceeded is not a global nil-error
requirement. Keep the original2s parent created after setup, cancellation cleanup
and sibling ownership/receipt/settings tests.

In the dispatch subtest, run exactly two passes with the same parent and actual
retained cursors, with an immediate failure gate between them:

1. Use50ms for BOTH batch and item limits on the first pass. Pending completes
   before item creation, so A's item deadline inherits the earlier delivery
   batch deadline. Require positive A Ready entry and its actual wait returning
   DeadlineExceeded. That necessarily ends the delivery batch before B; no sleep,
   injected clock, manual parent cancellation or timing measurement is needed to
   force the yield. Require nil returned batch error, live parent, nextEvent=1,
   exactly one readiness entry (A), zero sends, A's saved held status and the
   authoritative first B read still pending with unchanged event/message/options/
   receipt. Any error, unexpected B callback or other snapshot fails immediately.
2. Only after those exact gates, run the second and final pass with the existing
   250ms batch/50ms item limits, without resetting parent allowance or cursors.
   Require B to be the FIRST readiness entry, nil returned batch error, live
   parent, exactly one send for B's original event/message, and one final ordinary
   B Store.Get proving accepted with its expected receipt. A remains configured
   to block and must never send. If A is subsequently selected, its callback must
   still wait for its item context. There is no third pass or retry after a B
   selection/error. Retain both snapshots; the second does not replace a failed
   first attempt, since pass1 positively proves B was unattempted.

Bind cursor progress to the actual callback order/count on each pass, rather
than demand traversal of unrelated items after a legitimate batch yield. The
first event cursor must be1; the second must advance once for each readiness
entry, whose order is B followed only by A if another item fits. Record observer
visits and require corresponding operation-cursor advances from its retained
value and cyclic A/B order. Do not reset either cursor or replace exact counts
with a lower bound. The original observation subtest still requires its original
two-operation/one-event result. No acceptance of B pending after selection.

The dispatch fake observer never blocks or returns an error. The worker's
batchErr is only overwritten by another non-nil error, never cleared by success;
therefore requiring nil on EACH dispatch pass rejects any generation/admission,
read, held-save or accepted-save error, even if later errors overwrite its text.
A Ready's expected deadline is translated into held state by ordinary Dispatch.
Saved held alone cannot certify directory sync; nil batchErr supplies the needed
save-success condition. This avoids relying on last-error classification to
excuse real storage failures. A failure to reach A within the short first budget
fails the positive setup gate rather than silently passing or retrying.

Reduce the temporary78-line trace to the needed per-pass callback identities,
blocker context result/deadline, worker error/cursors/parent state and snapshot
statuses. Emit only on test failure, after the pass, through the existing fake
callback seam; remove generic phase structures, constant-result text, duplicate
operation-ID lookup and unneeded wrappers. Keep enough order metadata to identify
B selected versus unselected and publication failure. No production hook, new
goroutine/framework, relaxed durable store, larger budget or blanket error rule.

**Quick/review/publication boundary.** Reuse the established declared Nix
environment and GOWORK=off; from portal run once:
`go test -mod=readonly ./internal/web ./internal/monitoroperation -run
'^TestMonitor(Portal|Delivery|Observation|Status)' -count=1 -timeout=60s`.
This keeps cancellation/settings, ownership, concurrent dispatch, uncertain
receipt and observation controls. Two small disposable controls at the existing
test seams: reset nextEvent to0 before pass2 (must fail B-first/cursor proof), and
return a sentinel B session-admission error in pass2 (must fail immediately,
remain unsent and never reach a third pass). Retain expected failures and restore
exact final bytes before the single final positive quick. No permanent mutation
framework, stress batch or another localcount10. Format and ordinary hooks
precede commit and affected review. Main owns the58e monitor owning-commit
consolidation window, retained06025 reference, unchanged replay/input proofs and
final review; this assignment performs no history action.

After review, main may publish for the ordinary packaged creation/check path;
no workflow, test selection or CI timing change is needed. A new failure must
name pass/gate and retain its actual error, both cursors, callback order and
authoritative B snapshot; any B admission/publication failure stops this package
instead of opening another pass. New-source green proves the revised invariant
under that environment, not the original CI cause. Do not require another whole
VM solely for this Go test: it runs in the package check phase of main's required
preparation/CI. Full VM/native acceptance remains separately required and
unreleased here. Main may close the test-contract blocker on final quick/control,
review and packaged evidence while explicitly retaining the old cause as unknown.

No API/schema/production/native/SDK/Nix/proxy/deployment/recovery change; ordinary
ownership/cancellation and durable outcome contracts stay intact. Original CI
failure51ec3ad4/a9882375 remains unresolved evidence, and the6a9 Nix transfer/export
question stays parked. Only this design record changed; no application edit,
test/eval/build/Git/CI/network/runtime/live action. Sufficient one-file fixture
correction brief complete; original CI cause remains open; capacity returned.

### Reviewed36dc: refresh final-source identities and construct the driver

2026-11-07. Current/environment and ready architect0 Astra/xhigh/workspace_write
confirmed; unchanged applicable guidance reused. Main accepted monitor receipt
69029056 and affected/history review9b045d17 at
`36dc76d7149f929e2591b9dcdae7b8a92d1f9f66`, tree
`f66c5c17c033f305cc04c731e2a74d6518062404`. Only monitor_test.go differs from06025;
all734 other entries, sourceFor37c79af5, proxy, native and SDK selections remain.
Original06025 CI cause is unknown. C owns publication; its active outputs were
not inspected. This is a sufficient proposed verification package, not allocation
or permission to resume old f42 Stage2, which remains HELD.

**One owner, no application changes.** After main allocation, refresh immutable
36dc source/check bindings, then prepare the current session-creation driver.
Source review is already satisfied. Local preparation uses the exact commit and
does not depend on C finishing remote publication; it must not mutate shared
refs/index or inspect C's active work. Publication remains a separate prerequisite
for later consumer pins/CI attribution. Clean evaluation succeeds before ordinary
instantiation; positive registered recipe/output mapping precedes realization.
Do not add a separate old6a9 generated-source or closure-info diagnostic target.

1. Reuse B's exact whole-archive/source-only preparation and matching2.35.3
   evaluation method from `final-eval-6a9-0v0tq6dh`, substituting only final36dc
   and fresh owned RUN paths. Verify every committed blob/mode/symlink, tree,
   source NAR and unchanged lock/eight input identities; include final monitor
   SHA99cf1871. Record the archive/path-flake metadata qualification (no Git
   self.rev/lastModified); do not claim identity with a CI Git flake by tree alone.
   No dirty worktree source, old package-output/DRV seeding or old store reuse in
   the clean evaluation. Use the existing rooted binary directory
   `/nix/store/kp71jf0isr8pix0nn2lx2x3hj3vasii5-nix-2.35.3/bin` (NIX_DIR).
   The first acceptance target is once-only `NIX_DIR/nix --store RUN/store flake
   check --eval-store RUN/store --no-build --print-build-logs --show-trace
   --no-update-lock-file --no-write-lock-file --option max-jobs 0
   --option builders '' path:SOURCE36`, using the retained isolated config/cache
   recipe and source-only before/after inventory. Preserve all29 declarations,
   including14 unique Ruby shards plus aggregate. This computes check identities;
   it executes none of them. The old72.168s result is scheduling evidence only.
2. Refresh the29-name drv/out mapping in the existing inventory format, using
   explicit locked getFlake of SOURCE36 with its actual URL-encoded NAR query.
   Mapping must evaluate `builtins.mapAttrs (_: c: { drvPath = c.drvPath;
   outputPath = c.outPath; }) F.checks.x86_64-linux`, where F is that locked flake.
   The outputPath key corrects the original outPath serialization mistake; see
   the36dc mapping disposition below. Do not use the old collapsing row shape.
   Use ordinary `nix eval --json --expr MAPPING_EXPR` with the same explicit
   evaluation store and no-update/no-write-lock flags, after the clean receipt.
   Do not confuse computed drv paths with registered recipes. For the build,
   remove isolated-evaluation overrides and explicitly use NIX_REMOTE=daemon
   with --eval-store daemon. Read the actual client version and
   `nix store info --store daemon --json`; record the daemon engine separately
   (last observed2.34.9), without changing it. Ordinary host build/substitution
   policy remains; do not copy accepted outputs into a fresh store to certify
   fresh-source behavior.
3. Define DRIVER_EXPR as `(builtins.getFlake "path:SOURCE36?narHash=ENCODED_NAR").checks.x86_64-linux.session-creation.driver`,
   with concrete captured values, supplied as one literal argv argument. Run
   `NIX_DIR/nix-instantiate --eval-store daemon --add-root RUN/driver-recipe
   --indirect --expr DRIVER_EXPR` once, without --eval. Retain that ordinary root.
   Then read its actual derivation JSON/ATerm and require one driver .drv/out
   mapping, distinct from source, matching the current expression. Check actual
   same-store validity of driver and owning child recipes with nix-store
   --check-validity; nonnull path-info or a physical ATerm alone is insufficient.
   Bind both generated-flake recipes/outputs, selected source/target package
   recipes/outputs, driver config/test-script and guest closure-info graph from
   this current recipe. The generated recipes must retain the selected recipe
   file edge and normal selected output edge. Record exact graph bindings before
   building, without requiring unbuilt outputs to be valid.
4. Only after those gates, realize ONE target in that same host store:
   `NIX_DIR/nix build --store daemon --eval-store daemon --json
   --print-build-logs --show-trace --no-update-lock-file --no-write-lock-file
   --max-jobs 4 --cores 4 --out-link RUN/driver DRIVER_DRV^out`.
   This earns current-source package/generated-source/guest-export/driver
   preparation together. It neither runs the VM nor builds all29 checks. No
   ambiguous positional path-flake target, stale bare recipe, old3cg/agwn target,
   sourceFor repair, manual registration or second target on failure.

**Actual success evidence.** Require natural success and stdout/outlink equal to
the selected driver out, its executable bin/nixos-test-driver and bound script/
configuration. Keep recipe/output/NAR and actual registered reference closure.
Read both constructed generated flakes: drvPath/outPath must equal their own
selected package pair, and registered direct refs must retain both. Require the
actual current closure-info export's store-paths/registration to include both
generated sources and their selected package recipes/outputs, linked through the
current guest/driver graph; a recipe's exportReferencesGraph text alone is not
export completion. Bind declared P/L/N for each package and passively verify
distinct launcher/executable paths with equal actual inner ELF bytes. Preserve
the script's native variant, ordinary prepare, proxy42 lines and all case bounds.
No native invocation is needed for these preparation reads. Report built,
substituted and reused dependencies separately, including package check evidence.

Reuse accepted checks only when the new29 table's exact drv/out, complete relevant
source/input graph and actual valid output/NAR match a retained successful result.
Changed source identity requires fresh mapping even where a filtered input may
remain equal. The earlier716a20-of29 tally and f161 results are not a final count.
Return the updated reuse/unresolved table; do not run unrelated unresolved checks
in this package. Existing quick/review evidence remains for its exact scope.

**Bounds and handoff.** Reuse normal owner receipts and fresh verification watcher;
no new launcher framework. Existing phase caps:20min clean evaluation,10min
instantiation/mapping,40min driver build, with10min reassessment. First error,
mapping/source/input mismatch, missing validity/export proof, unintended target
or unexpected local kernel build stops the package. No retry, store repair,
source modification, forced cache miss or timeout expansion. Preserve all prior
roots/receipts. Prior driver build1010s is a scheduling reference, not a guarantee.

Successful current driver/export preparation feeds only the already specified
setup plus one original automatic proxy diagnostic (design069204e8/d9821e94),
after main's runtime release. Require actual casePassed and driverExit, preserve
failure-only timing exports/no retry; selected maintenance cases and original
whole VM remain later acceptance. Local host-engine driver success does not prove
fresh-source transfer/cold CI under2.35.3. The accepted6a9 local2.35 construction
from copied inputs with9vm absent, and earlier2.34.9-daemon construction, remain
their exact evidence; neither is repeated or relabeled here. No bison/sourceFor
cause or repair follows automatically from this preparation.

Finish-path c0cfd085 still owns remaining R29/native11/native5/W-C composition/
VM/rollout scope and reuse rules; no new gate or delivery-plan rewrite is added.
Only design.md changed. Read-only committed source/retained recipes/records only;
no evaluation, instantiation, build, test, copy, acquisition, Git mutation, CI,
native/guest/profile/claim/live/integration/lifecycle action. Capacity returned;
main owns allocation, acceptance and the next runtime release.

### 36dc mapping representation: independent command correction

2026-11-07. Current/environment and saved architect0 Astra/xhigh/workspace_write
verified; unchanged guidance reused. Main accepted terminal receiptfceb2116 at
`/tmp/lead-wakeup-verification-716a-B/final-preparation-36dc-lv_xk4nl`.
The69.961s clean2.35.3 evaluation/all29 declarations/source-only before-after
inventory is accepted and must not replay. Mapping alone returned29 output
strings, not the requested recipe/output objects; natural0 did not satisfy that
gate. The a08625bb execution package stopped before instantiation/build.

**Mechanism settled.** Nix JSON serialization coerces an attribute set containing
outPath to that string. My original row shape therefore discarded drvPath from
the JSON representation. One explicitly authorized offline literal-only probe
with the actualkp71 Nix2.35.3 binary, no flake/import/store path input, returned
`{"corrected":{"drvPath":"dummy-recipe","outputPath":"dummy-output"},"original":"dummy-output"}`
from `{ original = { drvPath = "dummy-recipe"; outPath = "dummy-output"; };
corrected = { drvPath = "dummy-recipe"; outputPath = "dummy-output"; }; }`.
No application evaluation, store mutation or second probe occurred. Rename only
the result key to outputPath; preserve c.outPath and all string contexts.

After main allocation, reuse the exact mapping command/environment/store in
the accepted packet, with a new output receipt and this one literal expression:

```nix
let F = builtins.getFlake "path:/nix/store/dxa6l68vy91ba7wnydnr1yawv9ap9bwy-source?narHash=sha256-c%2BKvon5rr3tfF6oBf9H6UglCiw86tydsq14z8l6HxlE%3D";
in builtins.mapAttrs (_: c: { drvPath = c.drvPath; outputPath = c.outPath; }) F.checks.x86_64-linux
```

Command remains pinned `nix --store OLD_RUN/store eval --eval-store OLD_RUN/store
--json --no-update-lock-file --no-write-lock-file --expr EXPR`; OLD_RUN is the
accepted final-preparation-36dc-lv_xk4nl root, not a newly seeded store. Guard
unchanged SOURCE36 NAR/lock and retained evidence; keep isolated configuration.
Require exactly the29 accepted names, each an object with exactly drvPath and
outputPath strings: drvPath must equal that name's clean-evaluation declaration,
outputPath its actual retained mapping output string, with valid store-path
shape and recipe/output distinction. Any missing/extra/collapsed row or mismatch
stops. Preserve raw output and parse it as returned; do not synthesize a success
by joining old logs. Result is computed mapping only, not recipe validity,
realization or check reuse. One mapping invocation,10min cap (previous64.126s),
ordinary watcher; no clean evaluation replay or application/history change.
This boundary is independently sufficient; it does not release the held driver.

### 36dc repeated CI construction refusal: fresh materialization discriminator

Main accepted disposition5affbb31 and raw logc4873327 under
`/tmp/lead-wakeup-R-publication-36dc-continuation-fl4h25da/ci-disposition-20261107T045510Z`.
Exact36dc/attempt1/run42339691318 creation128304407489 failed before VM. The
announced graph includes driver
`/nix/store/z83l78i7q5pb2llsxbfbi5q9nlqhzr7c-nixos-test-driver-dev-workspace-session-creation.drv`
and checkkmpr6gp0, matching the accepted clean check declaration. It announces
generated source03gmi8m9 at3425, then
`/nix/store/bcrdchd01crnxl7kf1pn240g73py6ndl-flake.nix.drv` at3433, followed by
invalid9vm1 bison source at3434. The two generated recipes are not present in the
inspected host filesystem, and no current registered graph was reached by B.
No guest case or current-source driver success follows.

**Disposition.** This repeats the missing-source boundary on current source,
but does not identify the first requiring operation. The unchanged sourceFor
declaration still requests the selected recipe-file and output edges; old6a9
recipes/actual direct references show those edges existed. Their unconditional
absence is not established. Source-only evaluation does not materialize/transfer
that graph, and constructing a copied2.34.9-materialized recipe with2.35.3 does
not test fresh2.35.3 materialization. Neither success distinguishes CI's input
assembly from downstream export. No sourceFor/closure/configuration correction,
cache/GC/network cause or Nix regression is justified. The proposed host-daemon
full-driver continuation is now held for this disposition; do not resume
a08625bb or f42. Fresh current-source runtime evidence is indispensable because
neither a current recipe graph nor the failing Nix operation is retained.

**One proposed discriminator package, after main allocation.** Reuse accepted
36dc source/NAR/lock and corrected mapping A; do not repeat its clean evaluation.
Use the already demonstrated direct local2.35.3 store workflow in a new owned
root, starting with ONLY the immutable SOURCE36 (ordinary source-only copy/add,
references empty). No old recipe graph, generated output, selected package or
9vm output is copied/preseeded. Ordinary locked input retrieval and normal build
substitution remain allowed in the subsequently allocated operation. This is
different from the accepted6a9 copied-input experiment, which remains complete.

Use the exactkp71 Nix2.35.3 entrypoints and a fresh local root RUN/store, retaining
Linux namespace/sandbox requirements and the previous direct-engine guard method.
No new daemon/service or host configuration. Ordinary instantiation is:
`NIX_REMOTE=RUN/store NIX_DIR/nix-instantiate --eval-store RUN/store
--add-root RUN/driver-recipe --indirect --option max-jobs 0 --option builders ''
--expr DRIVER_EXPR`, where DRIVER_EXPR is the exact NAR-locked36dc expression in
the prior brief. This registers recipes from source; it must not realize outputs.
Require the retained driver root to resolve to exactz83l78 above, its ordinary
out mapping, and registered03gmi8m9/bcrdchd recipes in the same local store.
Read bcrd's selected package recipe/output tuple, both context edges and out
mapping from actual JSON/ATerm; guard those against the owning immutable source.
No assumption about JSON schema or basename paths. If graph identities differ
from current CI, stop before building and report the exact source/context delta.

Then, with inherited NIX_REMOTE unset and both stores explicitly RUN/store, run
ONE target using that direct2.35.3 process:

```text
NIX_DIR/nix build --store RUN/store --eval-store RUN/store --json --no-link
  --print-build-logs --show-trace --debug --max-jobs 4 --cores 4
  --option build-users-group '' --option builders ''
  /nix/store/bcrdchd01crnxl7kf1pn240g73py6ndl-flake.nix.drv^out
```

The empty build-users-group is process-local single-user configuration for this
owned direct store, as in the accepted local2.35 workflow. Keep normal configured
caches and sandboxing; do not force dependency misses, alter global trust or
change source inputs. Record actual executable/version/local-store identity,
fresh registered recipe source, before/after validity of target out, its selected
package and9vm, and the actual build/substitution phases. Require target out
absent before construction. This realizes only one generated source and its
ordinary dependencies, not the whole driver, closure-info, guest or VM. Any
unintended target, graph/setup/namespace mismatch or first failure stops; no
alternate store, manual registration, source change or retry.

Failure on9vm now isolates a requirement on the path to this single construction;
retain its first trace operation instead of classifying from the nearest banner.
Another failure retains its own boundary. Success requires actual construction,
exact generated text/out/NAR and registered selected-recipe plus package-output
references. State whether9vm remained absent or was realized normally; target
substitution alone is not the requested construction discriminator. This proves
fresh current-source materialization and construction within one2.35.3 store,
not CI's distinct evaluator/daemon transfer path or downstream closure export.
Those remain specifically unproved after success; do not silently relocate the
old error or launch another target. A smaller pure-source check cannot settle
which Nix operation required9vm at runtime.

Use existing receipts/watcher,10min materialization cap and10min reassessment/
40min build cap; prior generated construction685.998s is a scheduling reference.
No new harness, full-driver retry or old6a9 recertification. Main owns selection
of the next boundary from this result. Application/native/SDK/P-L-N/proxy/case
contracts and required eventual full-driver/automatic/whole-VM acceptance remain
unchanged. Only design.md changed; the sole execution in this architect package
was the authorized literal-only offline serialization probe. No application
evaluation, instantiation, build, copy, store mutation, source/Git/CI acquisition,
native/guest/live or lifecycle action. Both sufficient boundaries returned;
capacity available, no implementer allocated here.

### After fresh36dc construction: prepare the current driver in the same store

2026-11-07. Current/environment and live same-session architect0 settings
Astra/xhigh/workspace_write verified; unchanged full applicable guidance reused.
Main accepted receipt a5f733e4 at
`/tmp/lead-wakeup-verification-716a-B/fresh235-materialize36dc-mx70t1xy` (FRESH).
Source-only direct2.35.3 materialization37.333s and bcr construction700.076s
succeeded;9vm remained absent/invalid. Exact36dc/tree f66c, source dxa/NAR,
lock adda, final monitor99cf, both recipe context edges and target actual refs
are bound. fceb clean evaluation, faae corrected29 mapping and review9b045d17
remain accepted. No repeated evaluation, mapping, materialization or bcr build.

**Decision: continue required preparation, no extra discriminator.** A complete
current driver and actual guest export are still required for the automatic
proxy diagnostic. Build that target in the already populated FRESH/store with
the same direct2.35.3 engine, reusing its accepted graph/outputs. This supersedes
the earlier host-daemon driver proposal for the next allocation; oldf42/a086
stay stopped and the completed discriminator stays terminal. No sourceFor repair
or further exploratory target is justified. Current CI5aff/c487 still has an
unidentified requiring operation; preparation can proceed without relabeling
that failure or claiming its cause solved. Main must allocate this new package.

**One implementer package, no source changes.** Use a new compact evidence/output
root NEXT, the existing FRESH/store and rooted driver recipe. Recheck accepted
source/NAR/lock and recipe hashes, actual local-store version2.35.3/sandbox true,
same-store validity and exact retained root. The driver recipe is
`/nix/store/z83l78i7q5pb2llsxbfbi5q9nlqhzr7c-nixos-test-driver-dev-workspace-session-creation.drv`
(SHA768a588f), out
`/nix/store/6nnkafrh939fxn8bha694m6wdaw9ii3l-nixos-test-driver-dev-workspace-session-creation`.
Guard accepted mfd target output/NAR0TxRPYqs and its exact direct0lb recipe/wbm
output refs; record driver/original generated output availability without forcing
misses. A stale/missing registered graph stops, not re-instantiates or repairs.

With NIX_DIR the existingkp71 Nix2.35.3 bin directory, inherited NIX_REMOTE and
isolated-evaluation overrides unset, invoke once:

```text
NIX_DIR/nix build --store FRESH/store --eval-store FRESH/store --json
  --print-build-logs --show-trace --debug --max-jobs 4 --cores 4
  --option build-users-group '' --option builders '' --out-link NEXT/driver
  /nix/store/z83l78i7q5pb2llsxbfbi5q9nlqhzr7c-nixos-test-driver-dev-workspace-session-creation.drv^out
```

Retain the accepted normal cache/trust/sandbox policy and process-local direct
single-user setting. No daemon construction, forced cache miss, target substitution
ban or copied-input reseeding. Record what was built/substituted/reused. This sole
driver target normally supplies the remaining original package/generated flake,
guest system/export, script and wrapper; it does not execute the VM. Do not request
a separate03g, bcr, closure-info, fullVM or R29 target.

**Require actual artifacts, not banners.** Natural success, JSON out and ordinary
outlink/root must identify6nnkaf with correct logical-to-physical FRESH/store
mapping; resolve/read store-internal symlinks in that store, not against unrelated
host paths. Bind bin/nixos-test-driver, actual test-script8pc9119 and driver config
65dglb46 to their retained recipe declarations. Read both generated texts and
registered direct refs: original03g -> d18vzm -> selected32zshld recipe/5rmqdwij
package, targetbcr -> mfd701 -> selected0lbqwmi recipe/wbm490 package. Target
evidence may reuse a5f only after unchanged validity/NAR/ref guards. Require the
actual closure-info store-paths/registration reached from current driver config/
guest graph to include both generated sources AND selected recipe/output pairs;
exportReferencesGraph in a recipe alone is insufficient. Bind that export to the
actual guest launch/image dependency. If a driver succeeds but that export is
missing, report incomplete preparation; do not improvise another target.

Record each package's declared P/L/N separately using existing package layout:
launcher P/libexec/codex/bin/codex and native executable
P/libexec/codex/libexec/codex/bin/codex. Resolve within the local store, require
distinct original/target package/launcher/executable paths and equal actual inner
ELF hashes. Preserve existing wrapper/ELF distinction, exact package ownership,
42proxy lines, test/provider/browser/native inputs and all case assertions.
No native/browser invocation or success claim follows from these passive reads.

**Make the accepted artifact usable, without a second build.** After all local
artifact gates pass, ordinary `NIX_DIR/nix copy --from FRESH/store --to daemon
--no-check-sigs DRIVER_OUT` may copy only that verified output and its ordinary
runtime reference closure into the host store for the later existing launcher.
First require the known host daemon to report this operator trusted. The per-copy
flag admits the hash-bound locally built unsigned closure; no global
key/trust/configuration change, manual DB repair
or arbitrary source/build-closure copy. Retain the copy's real result and compare
destination driver/closure path-NAR-reference bindings to the source, including
export/generated/package artifacts. Establish a normal retained host output root
through existing owner preparation machinery; do not execute the driver. If
ordinary copy refuses or the operator is untrusted, stop at that exact refusal
rather than change configuration or rebuild. Record its actual daemon version;
the daemon is a destination store, not the2.35.3 build engine. This
post-build output copy is preparation only, not CI evaluator/daemon recipe-transfer
proof. Preserve all source roots and original failure receipts; no cleanup.

**Bounds and acceptance.** Existing watcher/receipt workflow,10min build phase
reassessment/40min hard build cap; output copy has10min reassessment/20min cap.
At cap or first source/recipe/output/export mismatch, build/copy error, unintended
target or unexpected local kernel build, stop the owned command with the existing
interruptible cancellation procedure, reconcile effects and report. No retry,
engine/store fallback, extra realization or source edit. Recheck terminal owned
processes, exact source and retained roots; return the heavy slot/capacity.
Previous700s generated and1010s driver times are scheduling evidence, not limits
to increase. Current-package dependency successes may enter the29 inventory only
through exact existing mapping/input/output evidence; no broad check-reuse audit.

Next observable result is one current driver with actual guest export, both
package/native identities and usable host closure, or its precise first failure.
Success qualifies final36dc local2.35.3 driver/export preparation, not cold CI,
the old missing9vm cause, public prepare in the guest, native11/native5 or VM
acceptance. The previously defined setup+one original automatic proxy diagnostic
is the next runtime boundary only after main acceptance/allocation; wholeVM and
remaining delivery scope stay unchanged. Only design.md changed here; no eval,
instantiate/build/copy, source/Git/CI/network or runtime action. Brief sufficient;
capacity returned, no execution or next work assigned by architect.

### Driver modules stop: classify the exact assembly recipe before continuation

2026-11-07. Current/environment and live same-session architect0
Astra/xhigh/workspace_write verified; applicable guidance reused and verification
procedure reread. Immutable recipes below are in accepted FRESH/store from the
preceding brief. B's mutable driver-local36dc output was excluded until main
released its complete terminal packet7fda3f5f. It was then read as below. No Nix
query/evaluation/build/copy or source/
Git/configuration/runtime mutation is authorized by this investigation.

**Exact finding.** Recipe
`fl8vad67ff9apa0b2nxqy9myz8gavk0d-linux-6.18.49-modules.drv`, SHA256
`7ebc60a03e660e3ab70e43921c2674a9fab553fb9de9802abad4094b791aecb0`, produces
mlx5n0... through module-tree assembly, not kernel compilation. Its only module
input is existing5x8s3i...linux-6.18.49-modules from the modules output of
y55a9ima...linux-6.18.49.drv. The build command invokes Perl builder3r3xyh20
(SHA5b6a1276), whose actual body walks chosen outputs, checks collisions and creates
directories/symlinks. Its postBuild checks for one kernel version, then conditionally
removes old generated module-index files and runs kmod depmod against the assembled
output. It does not unpack Linux, configure it or invoke make/compiler/linker.

The owning immutable nixpkgs definitions match this exactly:
`pkgs/os-specific/linux/kmod/aggregator.nix` uses buildEnv over modules plus the
observed depmod postBuild; `nixos/modules/system/boot/kernel.nix` applies
aggregateModules to system.modulesTree and names it kernel-name + "-modules".
The readable retained nixpkgs sources nqkh6j5... and glw7ngr... contain this same
mechanism. `pkgs/build-support/buildenv/default.nix:144–145` defaults
preferLocalBuild=true and allowSubstitutes=false, both explicit in fl8. Local
assembly is therefore expected; no cache/runner inquiry is needed to permit this
specific recipe. These facts do not establish whether a different input missed
its cache or whether any canceled output completed.

The actual registered dependency path is driverz83 -> driverConfigurationszvb ->
VM4h97 -> guest systemjzgp -> fl8 -> y55[modules]. The separate y55 kernel recipe
has a Linux source tarball, GCC/LD/AR build flags and bzImage/vmlinux/scripts_gdb/
modules targets. It is the compilation boundary; fl8 is an ordinary guest-system
assembly dependency. The source-backed classification does not depend on the
substring "linux" or "modules" in a filename.

**Rule and sufficient continuation disposition.** The verification procedure's
unexpected Linux-build rule is written for vpsAdminOS kernels. Main additionally
carried an unexpected-kernel stop into this NixOS driver package; retain that
instruction for actual kernel/module compilation. Correct only its application
to the exact known fl8 assembly. No waiver of real compilation, source change,
standalone cache query or extra target is necessary. The canceled invocation is
not success and must remain canceled evidence, regardless of capture natural:true.
Main has now accepted B's terminal receipt/effects; new allocation is still needed.

Released receipt
`/tmp/lead-wakeup-verification-716a-B/driver-local36dc-1hzf7m7g/terminal-receipt.json`
SHA7fda3f5f was matched on read. Actual stderr45173 is the exactfl8 banner;
112412 is `error: interrupted by the user`. The separate cancellation record
binds SIGINT05:46:55.621841UTC to PID/PGID3673041/startTicks63231786; child exit1
at05:46:56.225911 followed94.576795s. This controls the disposition over the
capture's natural:true (which counts only capture-owned signals). No natural
driver failure, kernel compilation or cache-miss cause is established. Nix/CLI
handles are terminal; driver/original output and outlink absent; mfd/wbm remain
valid. Export/P-L-N/destination/copy gates were not reached. Raw v4 derivation
JSON has top-level structuredAttrs, not an assumed env.__structuredAttrs object;
use actual returned schema without another query or inferred field values.

The separate after-NAR guard failed because it hashed the absent HOST logical
`/nix/store/dxa6l68vy91ba7wnydnr1yawv9ap9bwy-source`. Keep that failure and make
no canceled-run after-NAR claim. The owning build's actual physical source is
`/tmp/lead-wakeup-verification-716a-B/fresh235-materialize36dc-mx70t1xy/store/nix/store/dxa6l68vy91ba7wnydnr1yawv9ap9bwy-source`;
the released complete735-entry blob/mode/symlink comparison found no changes or
extras there. New pre/post guards must hash that physical directory with pinned
`nix hash path PHYSICAL_SOURCE`, compare the accepted c+Kvon5... NAR, and read
validity/NAR/references for the logical source through explicit --store FRESH/store.
Also bind actual local-store engine/DB identity and the existing archive/tree
proof. Do not restore/requery the irrelevant host source or infer GC. This is
a corrected guard for a new allocation, not a retroactive success for the old one.

After that acceptance, main may allocate one continuation of the SAME prepared
z83^out driver in the SAME retained direct2.35.3 store, under the entire preceding
driver/export/conditional-copy brief. Use a new attempt/evidence/outlink, retain
the canceled one verbatim, recheck exact source/recipe/local-store identity and
accepted a5f target guards, and let ordinary Nix reuse valid dependency outputs.
Do not repeat clean evaluation,29 mapping, graph materialization or a standalone
generated-source build. No sourceFor repair or CI missing9vm cause is established.

Give the watcher the exact fl8 path/hash and classification before launch. Its
ordinary local builder is allowed; do not stop merely for this basename. Stop
on an actual build of y55a9ima...linux-6.18.49.drv or another positively identified
kernel compilation/out-of-tree-module compilation recipe. Identify such work by
its actual registered build commands or concrete kernel compiler output, never
a linux/modules name-prefix heuristic. Uncertain evidence goes to the parent for
bounded classification; a name alone does not authorize automatic SIGINT or prove
compilation. Ordinary cache copying of kernel outputs is not local compilation.
Keep all other first-error,
unexpected-target and source/ownership gates. No new watcher parser framework.

Use the existing40min build cap/10min reassessment and ordinary interruptible
cancellation/effect reconciliation. Only actual driver6nnkaf, both generated
flake refs, guest closure-info export and P/L/N/passive equal-ELF gates permit the
conditional output-only host copy from the preceding brief (20min cap). No
driver/native/guest execution. Next result is complete current preparation or
its actual first failure, not an inferred kernel/cache defect. Oldf42/a086 stay
stopped, a5f construction remains accepted and current CI cause remains open.

Only design.md changed. Immutable source/recipes and released completed evidence
read; no Nix query/evaluation/build/copy, source/Git/index/daemon/configuration,
cache/CI/network or runtime action. Sufficient brief complete; capacity returned.

### Natural36dc downstream invalid9vm: isolate the guest export boundary

2026-11-07, package c48b9a67. Current/environment and live same-session
architect0 Astra/xhigh/workspace_write reconfirmed; settings retained. Applicable
workspace sessions/documentation/verification/lifecycle/team guidance, repository
AGENTS and documentation skill read. This is a diagnosis/verification brief only.

**Settled evidence and contract.** Accepted continued-driver receipt
`/tmp/lead-wakeup-verification-716a-B/driver-continued36dc-d2j8znsv/terminal-receipt.json`
SHA29c6ce0f records natural1/292.971s without signals. Original03g -> d18 and
targetbcr -> mfd both constructed successfully. Their actual direct references
are respectively selected32z recipe +5rm output and selected0lb recipe +wbm
output. Retain both: ordinary public prepare needs the exact selected derivation
and its package, and the guest must receive them. The missing9vm is not a missing
generated-file reference or evidence that either construction failed.

The registered closure-info718 ATerm SHA256
`f76367d7419f8c2ce8a17e4d81a8ecac5209b567dfcc2ecdf2cfa4ecd93cf25f`
requests structured `exportReferencesGraph.closure` for 5rm, wbm, d18, mfd,
playwright2xc and guest-systemqm77. Its builder reads that supplied graph from
NIX_ATTRS_JSON_FILE and emits registration/store-paths/size data; it does not name
Bison. This is the actual guest population contract, not merely a diagnostic
closure. Test-scriptxd ATerm SHA256
`8b923b8bddb206b601789d74e6bccfba404687db05b1bbff990cf5d009f63932`
is ordinary writeText/passAsFile with no exportReferencesGraph. Both input
closures include the two generated files and selected recipe/output pairs.
Trace12007/12011 excludes9vm from both (5174/4735 paths). Both reach input
realization and output locking; neither reaches a builder banner before12084.
The parallel trace cannot identify the goal or requiring API.

The recipe graph gives a concrete provenance, not a required realized edge:
32z package ->197bmhqc tmux ->x1w0jlgr Bison ->hcf0pv0q tarball-fetch recipe,
whose declared output is9vm. Those are input-derivation edges; a reachable output
name is not proof that this downstream consumer requires that output materialized.
A permitted read-only pinned2.35.3 query, with NIX_REMOTE unset, returned0 with
4703 paths and no9vm:

```sh
/nix/store/kp71jf0isr8pix0nn2lx2x3hj3vasii5-nix-2.35.3/bin/nix-store \
  --store /tmp/lead-wakeup-verification-716a-B/fresh235-materialize36dc-mx70t1xy/store \
  --query --requisites --include-outputs \
  /nix/store/d18vzm30xg2bjifq409ml6j6247ywn7c-flake.nix
```

This controls ordinary traversal of that generated closure, including available
outputs; it does not emulate builder setup or certify the complete export graph.
No exact2.35.3 implementation source was found in inspected local source/manual
locations. The installed2.34.9 advanced-attributes manual describes exporting
input reference graphs, but cannot identify the2.35.3 call that refused9vm.
Do not claim exportReferencesGraph expands every unbuilt derivation output, a
sandbox/API regression, or a missing sourceFor edge on this evidence.

**Decision: no application correction; one necessary discriminator.** Isolate
exact closure-info718, because it directly earns the required guest export and
removes the parallel test-script goal. Missing fact: can that registered export
recipe alone prepare/build with the presently valid inputs and absent9vm?
Main may allocate one complete operation to an implementer; this brief releases
no execution and no second target. Reuse accepted current36dc/tree/source NAR,
clean evaluation/mapping/materialization and both constructions. Do not redo them.

Use the SAME owned FRESH/store and direct-local kp71 Nix2.35.3 engine, with
NIX_REMOTE unset, sandbox=true, existing cache policy and no remote builders.
Before launch bind registered718 ATerm/hash -> declared snf4 output, retained
physical dxa6 source/NAR and ordinary local-store metadata. Read actual metadata
to confirm the six export roots and ordinary required inputs remain valid,
generated texts/direct refs unchanged, and snf4/9vm absent and invalid. A missing
or changed prerequisite stops this package, without restoration or realization.
Use the existing capture/watcher workflow and a new attempt directory/outlink:

```sh
"$NIX_DIR/nix" build --store "$LOCAL_STORE" --eval-store "$LOCAL_STORE" \
  --json --print-build-logs --show-trace --debug --max-jobs 1 --cores 4 \
  --option build-users-group '' --option builders '' \
  --out-link "$ATTEMPT/closure-info" \
  '/nix/store/71833aa3y7m9wmqildkal667j8lx4hnr-closure-info.drv^out'
```

NIX_DIR is the exact kp71/bin above; LOCAL_STORE is the exact FRESH/store above.
This uses an already registered immutable recipe, not a stale pathname or a new
flake evaluation. No substitutes are disabled and no dependency is preseeded.
Only718's builder is expected: every required input already reached realization.
Expected seconds, reassess at60s, hard cap120s. Stop on a new dependency build,
9vm realization attempt, changed identity/input, unexpected goal, natural error
or cap; reconcile the owned process and preserve output. No automatic retry,
second downstream goal, full driver, host copy or VM. Preserve prior roots/failures.

Require natural result plus actual snf4 output metadata and registration/store-
paths, not a banner. On success with9vm still invalid/absent, verify the export
contains d18/mfd and both selected recipe/output pairs and binds the guest graph;
this earns local export preparation and contradicts a deterministic718 refusal
under these inputs. It does not prove the parallel run's test-script caused the
failure or authorize continuing the driver. On the same pre-builder invalid9vm
failure with no other build goal, identify718 setup as sufficient to reproduce
this local boundary; do not promote that to an exact API diagnosis. A different
failure, cap or unexpected dependency is inconclusive and stops. Return the
single terminal result, raw trace and before/after metadata to main for the next
decision. No build or closure-output success is inferred in advance.

Original CI5aff/c487/b688 still has an unlocated requiring operation; this local
isolation cannot retroactively attribute it. SourceFor/proxy/native/SDK and every
case/bound/assertion remain unchanged. No source/history/compatibility/deployment
or recovery change is justified; retain selected P/L/N, equal native payload and
actual restart/restoration/queue/goal/Stop proofs. Oldf42/a086 stay stopped. Any
later repair needs its own narrow implementation, quick checks and affected
review before longer verification; none is specified without the missing result.
Only design.md was written; one read-only named-store metadata query and retained
source/recipe/log reads were performed. Capacity returned after this brief.

### Exact718 mechanism and minimal package-output fixture correction

2026-11-07, package217db81d, superseding the preceding discriminator and the
requirement to export selected recipe graphs into this guest. Current/environment
and live architect0 Astra/xhigh/workspace_write reconfirmed; unchanged guidance
reused. Only this design and owned read-only evidence were written. Main owns
source, review and execution allocation.

**Established local mechanism.** Accepted isolated receiptc97e562c binds sole718,
valid six roots/ordinary inputs, natural1/0.469190s, no signals, no builder and
only invalid9vm. Evidence/provenance is in
`/tmp/lead-wakeup-nix235-export-A-dorehjgr/evidence.json`; original run receipts
remain untouched. Official Nix2.35.3 tag objecte98b7c7 resolves to immutable
commit8624d7c74eaee2638d2aff9b1e30455a74baba8c. Downloaded official upstream source
archive SHA25616dd66483724424a206d045a39944668ef5274231656d8da0c6c59ee705287e1,
origin/tag responses and content hashes are retained. No Nix tool was installed,
built, switched or patched.

At that revision, `derivation-building-goal.cc:969` calls DesugaredEnv::create
before creating/starting the builder. Its structured branch calls
`StructuredAttrs::prepareStructuredAttrs` (`derivation-env-desugar.cc:28–31`),
which calls `Store::exportReferences` (`parsed-derivations.cc:116–119`).
`store-api.cc:830–865` first computes the ordinary closure of the export roots,
then visits **every .drv in that initial closure** and computes the closure of
**every declared output**, without an isValidPath guard. Closure traversal calls
queryPathInfo; its invalid-path exception (`store-api.cc:624/644`) has the observed
message. This happens before the closure-info shell/jq builder can run.

Generated d18/mfd retain actual selected32z/0lb recipes as intended. Their recipe
closures include Bison fetch recipes declaring9vm: the retained32z ->tmux197 ->
Bisonx1w ->fetchhcf witness is one path;004v2 is also present and is the first
sorted .drv in the export closure. Ordinary validity does not imply validity of
all these declared outputs. The CLI include-outputs control differs explicitly:
`misc.cc:57–60` only follows an output when isValidPath succeeds. It is therefore
consistent with the export failure, not a contradictory reproduction.

Correspondence exceeds a version label but is not a whole-build attestation.
Retained official-installer/signed-cache acquisition and host metadata bind kp71
NAR NBHz... to deriverlcjya and split store librarywll. Both local derivation bodies
are absent; the exact glcbc store-library derivation cache lookup returned404.
No complete source/patch-set provenance or reproducible binary equality is claimed.
Installed kp71 ELF RUNPATH names wll; its SHA256 is82770581..., and wll's is7dfc81f8...
(full hashes in binary-provenance.json). Retained wll disassembly has the structured
export call2969cb ->exportReferences2dd3d0, outputsAndOptPaths at2dd68d and the
unguarded output-closure call2dd719. Store vtable slot4fc648 resolves that call to
computeFSClosure278e70. These actual compiled operations corroborate the relevant
upstream behavior despite the broader provenance limit. No version regression,
cache/GC/corruption cause, or original CI API attribution follows. CI5aff/c487/b688
and parallel29c6 keep their previous limits; sole718 establishes the local boundary.

**Why a one-path preparation repair is wrong.** Read-only same-store queries find
5167 paths in the six-root ordinary closure,3768 .drv files and4838 distinct declared
outputs,4371 invalid including9vm. The precise old export precondition is that all
those outputs and their ordinary closures be valid. Seeding9vm or retrying718
would not satisfy it. No broad realization is proposed. As a control, removing
only the two generated-flake roots from this query leaves928 valid runtime paths,
zero .drv files and no9vm. This is a control on current artifacts, not acceptance
of a changed driver.

**One-file implementer boundary: nix/tests/session-creation.nix.** Remove sourceFor,
maintenanceSources, the Python maintenance_sources mapping and its two
virtualisation.additionalPaths entries. Keep package, maintenanceTarget and
playwright in additionalPaths, and keep both mkPackage definitions/override exactly.
Use existing `maintenance_packages[target]` as the --source argument to BOTH
ordinary public prepare and ordinary public switch. Add a brief comment explaining
that this selects an already built immutable package through the public API and
avoids exporting its entire build-recipe graph. Do not add a wrapper flake, alias
package, custom import/export, private hook or alternate runtime.

This is supported by the existing consumer: workspace-host:650–716 accepts an
existing canonical PATH, fingerprints it, calls coordination_build and requires
one executable candidate package; it does not require flake.nix.
workspace-coordination-host.rb:11–39 fingerprints a non-Git directory and invokes
`nix build --no-link --print-out-paths PATH`. Nix's ordinary store-path installable
form selects that immutable output (upstream installables.cc:493–509/build.md and
installed2.34.8 manual). All compatibility, native, plan/profile, source-stability
and maintenance checks still execute. Current5rm/wbm each have115 regular files
and22 symlinks, below the source fingerprint's20,000-file limit. Prepared `source`
will now be the requested candidate artifact; `sourcePackage` remains the actual
currently active package. Do not conflate the two.

Retain existing exact candidatePackage/sourcePackage assertions. Add
`prepared["source"] == maintenance_packages[target]`, and bind the operation's
`preparation.source` and `preparation.sourceIdentity` to that public prepare result.
Retain distinct original/target P/L/N, equal native ELF bytes, actual service/pane
identity comparisons and restart, immutable source/output ownership, source and
candidate native checks, saved digest/token validation and all pause/cancellation,
restoration, queue, goal, Stop, continuation and recovery proofs. No case, timeout,
auth/TLS/provider setting,42proxy lines or production file changes.

**Explicit representation/coverage change.** Build receipts and current-source
mapping still bind each real selected recipe to its package output and reviewed
source. Guest export must contain both actual packages and their runtime closures;
it no longer has to contain the selected build recipes or miniature wrapper flakes.
The guest tests ordinary prepare of a prebuilt store installable and subsequent
activation/resume. It does not claim guest flake evaluation/build-dependency
acquisition coverage. Those were fixture choices, not the durable-wakeup/bounded-
maintenance product contract. Public source ownership is still fingerprinted and
revalidated; immutable artifact identity is more direct. No persistent format,
compatibility, deployment or recovery behavior changes.

**Controls and acceptance.** Implementer quick checks: existing Nix syntax and
embedded-Python syntax checks, exact diff/unchanged case-and42proxy guards, and the
existing maintenance stale-source/token/claim negative test
`test_maintenance_rejects_stale_source_token_and_claim_before_operation_effects`
in test/workspace_host/maintenance_test.rb through the repository environment.
No new permanent test/framework or mutation of a store artifact. The existing
exact candidate assertions are the wrong-artifact guard; the source-identity
assertions prove the new source representation reaches the saved operation.
Use the normal owning fixture commit/consolidation under main's Git window,
preserving old refs/evidence, then independent affected/whole-history review.

After source/review acceptance, refresh clean matching2.35.3 no-build evaluation,
29 mapping (`outputPath`, not outPath) and ordinary retained driver graph for the
new exact head/source. Do not infer new package/driver identities from36dc, or
reuse generated03g/bcr/718 as current outputs. Realize the new driver under the
existing bounded same-store/direct-engine preparation workflow; validate actual
closure-info registration/store-paths contain both mapped packages/runtime paths,
with no fixture-induced recipe expansion. Retain exact source/NAR/lock and actual
P/L/N/equal-ELF gates before conditional host output copy. Stop on any identity,
export or natural build failure; no old718/xd/full-driver diagnostic replay.
Then main may allocate the already required setup+one automatic proxy diagnostic;
maintenance and whole original VM acceptance remain required under the existing
sequence. Automatic-only success cannot accept maintenance. No runtime acceptance
or new execution is asserted by this brief. Oldf42/a086 stay stopped.

Settled: the local export mechanism and this narrower public-API fixture change.
Open: original CI attribution and all corrected-source build/runtime acceptance.
Only read-only source/provenance retrieval, installed-binary inspection and named
store metadata queries ran. Sufficient one-file brief complete; capacity returned.

### Reviewed6bc: one final-source driver preparation package

2026-11-07. Current/environment and live architect0 Astra/xhigh/workspace_write
verified; capacity available and settings retained. Unchanged applicable guidance
reused; monitoring skill reread for this release brief. Main accepts implementation
13aef8c7 and independent review8a97bc91/no findings, including all four lanes and
11-commit/single-SDK/no-migration history. The leading review packet was still
being updated when read; main's acceptance assignment controls this handoff.
Exact R is6bcbb5246531a70e5b24c6e4f7e9fd40016bbba3, tree
4cfa50f47f66e2eaa71be889862d5e850d989c0d. Read fixture SHA256
 aa24b7d20a4b13b0e52365f95e58f00349642ace687c82620660b81b0895996f matches
accepted checked/committed bytes; only +7/-28 versus36dc, all734 other entries equal.
C owns publication; this package needs no C output or Git/ref/index mutation.

**One owner, one terminal result.** After main allocation, one implementer owns
source preparation, clean evaluation, mapping, retained graph, sole driver build,
actual export/native gates and conditional host copy through completion or first
error. No command-by-command release, standalone diagnostic or new harness. Reuse
the accepted fceb clean-evaluation preparation, faae corrected mapping, a5f direct-
local materialization and later driver/copy machinery, with the amendments below.
Do not resume oldf42/a086 or reuse their targets; retain all failure stores/roots.

Use pinned NIX_DIR=
`/nix/store/kp71jf0isr8pix0nn2lx2x3hj3vasii5-nix-2.35.3/bin`.
Create one owner evidence root RUN with **separate** EVAL_STORE and BUILD_STORE.
EVAL_STORE uses the proven isolated config/cache method for clean read-only source
evaluation and mapping. BUILD_STORE is a new source-only direct-local2.35.3 store,
not a daemon build or a copy of an older recipe graph. Ordinary source-only
add/copy of the same verified new archive into each is permitted in the allocated
package; no package, output or recipe seeding. Verify initial inventories contain
only SOURCE with empty references. Normal locked-input acquisition/substitution
may follow in their owning phases. Do not impose source-only inventory after
ordinary materialization, which intentionally registers the graph.

**1. Exact archive and clean evaluation, once.** Use the existing whole-archive
method for6bc: bind all735 committed paths/bytes/modes/symlinks and no extras,
head/tree, fixtureaa24, unchanged lock and all eight locked URL/rev/NAR identities.
Record actual archive hash, logical SOURCE and its new NAR; no old dxa/source path
or NAR inference. Keep the archive/path-flake metadata qualification: absent Git
self.rev/lastModified means this is not automatically the CI Git-flake identity.
Run from the owned evidence directory or actual physical source, never an assumed
host logical source. Under the retained isolated configuration invoke once:

```text
NIX_DIR/nix --store EVAL_STORE flake check --eval-store EVAL_STORE
  --no-build --print-build-logs --show-trace --no-update-lock-file
  --no-write-lock-file --option max-jobs 0 --option builders '' path:SOURCE
```

Require natural0, all29 declarations (including14 unique Ruby shards and their
aggregate), and actual locked-input identity evidence; preserve source-only
before/after registered-store inventories as in fceb. This executes no check.
Cap20min. No parser-assumption repair by retry: inspect saved output, and stop on
an actual missing/mismatched declaration/input/source or failed invocation.

**2. Corrected mapping, once, after clean evaluation.** In the SAME EVAL_STORE/
isolated environment run `nix --store EVAL_STORE eval --eval-store EVAL_STORE
--json --no-update-lock-file --no-write-lock-file --expr MAPPING_EXPR`.
MAPPING_EXPR is the single literal argument:

```nix
let F = builtins.getFlake "path:SOURCE?narHash=URL_ENCODED_ACTUAL_NAR";
in builtins.mapAttrs (_: c: { drvPath = c.drvPath; outputPath = c.outPath; }) F.checks.x86_64-linux
```

Substitute actual captured SOURCE/NAR using structured argv, without shell
interpolation. Require exactly29 named object rows, exactly drvPath/outputPath
string fields, recipe/output path distinction and drvPath equality to each clean
declaration. `outPath` is not a permitted row key: it collapses JSON rows. Bind
outputPath to the returned current expression, not old output strings. Cap10min.
Computed paths are not proof of registration, realization or passed checks.
No old successful tally transfers. Any dependency/check reuse needs exact current
drv/output, relevant source/input graph and valid output/NAR evidence; report
unproved rows without running unrelated checks in this package.

**3. Ordinary current graph, once.** Start BUILD_STORE from the same immutable
SOURCE only. Use ordinary instantiation with NIX_REMOTE=BUILD_STORE, no isolated
evaluation overrides, and explicit --eval-store BUILD_STORE:

```text
NIX_DIR/nix-instantiate --eval-store BUILD_STORE --add-root RUN/driver-recipe
  --indirect --option max-jobs 0 --option builders '' --expr DRIVER_EXPR
```

DRIVER_EXPR is `(builtins.getFlake "path:SOURCE?narHash=URL_ENCODED_ACTUAL_NAR").checks.x86_64-linux.session-creation.driver`.
Cap10min; no --eval and no realization. Guard actual local store/DB identity,
engine2.35.3 and sandbox=true. Retain the ordinary driver-recipe root. Require one
current DRIVER_DRV/output pair from actual registered JSON/ATerm, distinct from
SOURCE. Bind selected original/candidate package recipes/outputs, script, config,
closure-info and guest launch/image graph to this expression and the reviewed
fixture. Read actual schema; require same-store recipe validity using legacy
check-validity as well as metadata. Unbuilt output absence is expected and is
recorded, not repaired. No03g/bcr/718 or other36dc identities are presumed current.

Check the actual script still passes each mapped package output to BOTH public
prepare/switch and preserves source/sourceIdentity, P/L/N, native/case/budget and
42proxy assertions. Export roots contain the two packages, playwright and the
ordinary guest-system root; the removed wrapper sources/build-recipe graph must
not reappear through fixture wiring. Do not impose the historical928 count or
ban unrelated legitimate runtime paths. Preserve exact new source -> selected
recipe -> selected output bindings outside the guest export.

All source/NAR guards use the **owned physical path**
`BUILD_STORE/nix/store/<actual-source-basename>` (and the corresponding EVAL_STORE
path), paired with logical SOURCE metadata through explicit --store. Hash the
physical tree before/after; never restore or require an absent host copy.

**4. Sole driver realization.** After prior gates, unset inherited NIX_REMOTE and
isolated-evaluation overrides and run only this target in the SAME BUILD_STORE:

```text
NIX_DIR/nix build --store BUILD_STORE --eval-store BUILD_STORE --json
  --print-build-logs --show-trace --debug --max-jobs 4 --cores 4
  --option build-users-group '' --option builders ''
  --out-link RUN/driver DRIVER_DRV^out
```

The empty build-users-group is process-local single-user configuration. Keep
normal caches/trust and sandbox=true; no daemon engine, forced miss, substitute
ban, source edit or separate package/generated/export/check target. Record actual
build/substitute/reuse outcomes. Cap40min with10min reassessment. Known module
buildEnv assembly classification from a499 may be reused only after binding the
current recipe content/inputs to that classified operation. Stop actual unexpected
kernel/out-of-tree-module compilation; no name-prefix, debug-goal or cache-copy
SIGINT. Uncertain evidence goes to the owner for bounded classification.

**5. Artifact gates and conditional copy.** Natural success, stdout and ordinary
root must identify current DRIVER_OUT, its NAR/references and executable
bin/nixos-test-driver. Bind actual script/config outputs to their recipes and the
runtime inputs. Read the REAL closure-info registration/store-paths reached from
the current guest launch/image graph and require both mapped packages' runtime
closures. Export text in a recipe or a build banner is not acceptance. Selected
build recipes and removed wrapper flakes are no longer guest-export requirements.
Missing export, source linkage or driver artifacts stop preparation without an
extra target. Resolve all store-internal links in the owning local store.

For each package P, bind launcher L=P/libexec/codex/bin/codex and inner executable
N=P/libexec/codex/libexec/codex/bin/codex through the actual package layout.
Require distinct original/candidate P/L/N and equal actual inner ELF SHA256;
retain wrapper/native distinction and declared source/native ownership. These
are passive reads, with no native/browser/guest invocation.

Only after all gates, require the known host destination daemon to report the
operator trusted and record its actual version separately from the2.35.3 local
build engine. Ordinary `NIX_DIR/nix copy --from BUILD_STORE --to daemon
--no-check-sigs DRIVER_OUT` may copy the verified output and ordinary runtime
reference closure. The per-copy unsigned-local allowance changes no global trust
or configuration. Require destination path/NAR/reference parity for driver,
script/config/export and both package closures, then establish the existing
normal owned host output root. Cap20min, reassess10min. No host build, arbitrary
build-closure copy, store repair or driver execution. A refusal stops as observed.

**Ownership, stop rule and result.** Resolve the retained pinned Luna/low utility
policy and use a fresh watcher for each long/uncertain operation; keep short
metadata guards inline. If native utility launch is unavailable, report that and
use the proven standalone CLI fallback with explicit `--sandbox danger-full-access
--ask-for-approval never` and the same pinned model/effort. If that is unavailable,
use the monitoring skill's visible bounded parent fallback; no model substitution
or indefinite wait for capacity. Watchers own only their assigned operation,
logs/status and authorized cancellation, never diagnosis/retries. Existing capture
and receipt machinery suffices.

At the first real source/input/schema/mapping/validity/build/export/copy error,
unexpected target or phase cap, stop the owned operation, reconcile exact signals,
terminal process effects and partial artifacts, and return the precise failure.
No retry, repair, extra target or store/engine switch. Keep satisfied phase results
and every previous root/failure intact. One successful owner package returns a
usable exact6bc driver/export with host parity, or its first failure; it never
runs a guest. Preserve original CI attribution and whole-binary source-provenance
limits. Main then accepts preparation and separately allocates the existing
setup+one automatic proxy diagnostic. Five maintenance cases/original wholeVM,
native11/native5, R29, W-C composition and rollout remain existing scope.

This refresh changes only design.md. No Nix command/query/evaluation/build/copy,
source acquisition, CI/C-output inspection, application/Git/index/runtime or
lifecycle action ran. Complete dispatchable brief returned; capacity available,
no execution or next package allocated by architect.

### Exact6bc bootstrap: consume command stdout at both terminal-control callers

2026-11-07. Current/environment and live same-session architect0
Astra/xhigh/workspace_write verified; capacity available, settings retained.
Repository AGENTS and workspace lifecycle/documentation/verification procedures
read; unchanged session/team/skill guidance reused. Leading records still contain
older preparation status; main's accepted8001 preparation and completed CI
assignment control this diagnosis. No application or runtime action is released.

**Demonstrated defect.** Read exact committed6bc source through `git show` and
matched working bytes: libexec/dev-session SHA256670a47910f1eb364f927be91181abb3a8dfcf2958f21dd90923c33207d5b049b;
tmux_runtime_test.rb d62cf222...; workspace-maintenance.rb5998250f.... Raw CI log
`/tmp/lead-wakeup-R-publication-6bc-vy9lmtxq/ci-disposition-20261107T081252Z/creation-job-128338991229.log`
was rehashed to ab5d6048ac5eb065de0ac65c21f654864e312e3b9150a2e33e649e808e0c17d6
(1507096 bytes). Lines6685/6689 report JSON.parse Array-to-String TypeError at
packaged31403 `.dev-session-wrapped:9544`, reached from quiesce:1801.

CommandRunner#capture (libexec/dev-session:409–429) returns
`[stdout, stderr, status]`, raising CommandError on nonzero exit unless explicitly
allowed. quiesce_native_client!:9543–9544 passes that entire Array to JSON.parse.
This is a production caller/helper mismatch, not native timing, fixture selection,
Nix packaging or a malformed portal JSON conclusion. The immediately related
restoration caller reconcile_native_client!:9577 makes the same mistake. It was
not reached by this bootstrap, but violates the identical return contract and
would block admitted/suppressed restoration. Adjacent recovery/other JSON callers
already destructure stdout; no broader caller cleanup is needed.

Why existing coverage missed it: the held-terminal restoration test at
 test/dev_session/tmux_runtime_test.rb:331 mocks capture to return a bare JSON
String (:342), matching the erroneous caller rather than production. The existing
package-transition quiesce test (:420) does not set the maintenance-operation env,
so it follows the ordinary cold-proof branch. Workspace-host maintenance unit
fixtures stub quiesce_sessions/restore_quiesced_sessions above this transport
boundary. Keep those useful orchestration tests; repair the missing boundary test.

**Smallest implementer package: two files.** In libexec/dev-session, destructure
only stdout at the two maintenance-control capture sites (`output, = ...` then
`JSON.parse(output)`, matching nearby conventions). Preserve capture's tuple,
nonzero-status enforcement, input JSON/argv, error behavior and both existing
status checks. No new transport wrapper, response protocol/schema, fallback,
rescue-and-ignore, helper-wide return change, timeout or Go/native change.
In test/dev_session/tmux_runtime_test.rb, replace the misleading held-terminal
mock and add focused quiesce/restoration regression coverage using the real
CommandRunner/Open3 transport with a tiny disposable Ruby portal responder,
following existing tests in that file. Keep shared support unchanged unless a
concrete existing helper requires a minimal adjustment; route any larger boundary
change to main. Do not invoke real native, tmux services or registered workspaces.

Tests must exercise real capture tuples, stdout JSON plus harmless stderr, and
verify the request action/operation/slug/invocation (and restoration thread),
--worker/workspace/state/profile context. Required behavior:

- Authorized terminal-intent permits the existing owned-pane respawn to shell
  exactly once; it neither kills the tmux session nor sends a resume command.
  A refused status, malformed JSON or nonzero exit (even with plausible success
  JSON on stdout) must stop before that pane effect.
- terminal-sync-suppressed retains the existing held-root test: no reconciliation,
  materialization/load or terminal send; return the same session. Exercise real
  capture, not a string-returning mock.
- terminal-sync-admitted with no held recovery proceeds through the existing
  readiness/client checks and resumes the exact retained thread in its owned
  stopped pane. Preserve current behavior for an already running client. A held
  root must still reject admitted status through the existing `!held` guard;
  refusal/nonzero/malformed responses must not start a client. Reuse local native
  version/provenance test fixtures and existing ManagedTmux effects rather than
  adding an acceptance framework or bypassing the changed transport.

Keep negative scenarios proportional (a small table/local responder is enough).
Preserve existing replacement-pane identity, already-stopped client, ordinary
quiesce/refusal restoration and explicit Stop tests; no weakening to merely
asserting absence of TypeError. The new positive cases should fail against the
old caller at JSON.parse and pass with stdout selection. One red/green focused
regression cycle is sufficient, not a repeat/stress campaign.

**Recovery and compatibility.** Go terminal-intent persists the exact terminal
identity and grants authorization only during settled draining-writers; terminal-
sync owns restoration and suppresses explicit Stop. These gates remain unchanged
(maintenance_control.go:591–642). This caller fails before its own respawn/terminal
record, but the portal was already drained and the Go terminal intent persisted;
do not describe the failed operation as effect-free. The Ruby worker catches the
exception and records recovery-required before source stop/activation. CI6743
accordingly has sourcesStopped=false/activationIntent=false and an owned terminal
intent. Existing worker ordering, durable queues/goals, bounded pause/interrupt,
activation/resume, cancellation and restoration ledger semantics stay intact.
The fix changes no on-disk format or migration and supports the same statuses.
Existing failures/journals remain evidence. Retained operations are owned by their
saved source package, so installing a corrected candidate alone does not rewrite
or repair an old operation; no live recovery or lifecycle action is proposed.

**Quicks, commit and acceptance.** Run Ruby syntax on both files. Use the repository
Nix environment and the aggregate `ruby test/dev_session_test.rb --name REGEX`
entry, as test/README.md requires; direct feature-file execution can miss helpers.
Select the new maintenance-terminal cases, existing held-terminal case,
package-transition quiesce/refusal, already-stopped and ordinary stop/restoration
controls. Also run the existing workspace-host maintenance group through
`ruby test/workspace_host_test.rb --name '/test_.*maintenance|test_restoration_failures_and_worker_loss_retry_owned_tail_before_terminal|test_source_recovered_outcome_waits_for_owned_restoration/'`
(or the equivalent exact existing selectors) to retain orchestration/recovery
controls. Keep ordinary check bounds/watchers for any uncertain-duration batch,
record case/assertion counts, and stop first real failure. No new permanent tests
outside the owning file or repeated full unrelated suite is needed for this fix.

Implementer owns ordinary focused maintenance commit/consolidation and required
hooks under main's Git window; preserve published6bc/ref/failures and full reviewed
old/new history. Independent affected review must assess both callers, real
transport regression and unchanged recovery/Stop ownership, plus whole-history/
single-SDK/no-migration disposition. Existing source review does not cover new code.
After accepted quicks/commit/review, refresh exact final-source recipe/driver/input
bindings under the existing preparation workflow and run the ordinary original
session-creation VM acceptance through bootstrap, maintenance and recovery. A
selected existing failure-focused package is main's runtime choice; it cannot
replace whole original acceptance. No old6bc driver or success tally silently
transfers to changed source. The actual6bc automatic70.11s success remains scoped
evidence; a new local automatic-only diagnostic is not needed to diagnose this
Ruby failure. Native/R29/W-C/rollout requirements remain unchanged.

Settled: two concrete tuple consumers, the masking mock and two-file correction.
Open: corrected-code quick/review/packaged runtime acceptance; no further diagnostic
or product decision is needed to release implementation. Only design.md written;
read-only committed-source/log inspection and guidance/identity checks performed.
No tests/eval/build/Nix/CI/network/source/Git mutation/native/guest/live/lifecycle
action. Sufficient package complete; capacity returned, main owns allocation.

## Exact9823 bootstrap: owning activation must not invoke generic held restart

Sufficient correction brief for c5a44df3, 2026-11-07. Current source is reviewed,
published `9823ae6e869a105b2de296d46115d37ae9f38e16`, tree
`271e29f3c37cf337978a74d3ad4fe72fa04f3449`. Session/current/environment and live
architect0 Astra/xhigh/workspace_write were reconfirmed; settings unchanged.
Read applicable workspace/session/team/lifecycle/documentation/verification and
repository guidance, current leading records and the owning update guide. This
package changes design only; main owns implementation and runtime allocation.

**Evidence and demonstrated mechanism.** Released evidence is
`/tmp/lead-wakeup-R-publication-9823-4ilji4sl/ci-disposition-20261107T091354Z/creation-job-128357141490.log`,
SHA256 `5dcdb21ea38abc06580b27e2717a6b8b3cadf647183ec49e7ea321aa7576f68e`;
disposition `754a49d7a570c353635e72dd8dc3f26d8051ce4063c00e47e791a9d74527e1e0`.
Exact run42356994910/attempt1 has14 starts/13 finishes, automatic45.83s and
bootstrap6345. Lines6708–6709 are the held generic-restart refusal and selected
candidate `_activate` failure. Snapshot6720 has sourcesStopped, activationIntent
and cutoverIntent true, sourceRecovered false, phase recovery-required. Candidate
rv66 remains selected over sourcevq2984; no completion/resume is proved. This is
an effectful forward failure, not an admission-only refusal or local-driver proof.

The current call chain establishes the composition defect:

- `workspace-maintenance.rb:261–348` claims the saved-source worker, validates
  preparation under the transition lock, drains writers/terminals, verifies
  captured source exit and records activation intent before `activate_candidate`.
- `workspace-host:750–797` stages and authorizes startup for that operation,
  selects the target and adopts candidate native when maintenance already drained.
  `activate_installed` (1259–1266) passes private-activation and owning-operation
  environment to the selected candidate. `activate` checks foreign maintenance,
  pending startup ownership/profile and held-target compatibility before effects.
- `activate` (1229–1231) enables native services with portals deferred, then calls
  `reconcile_codex_update` unconditionally. Its immediate registration snapshot
  can still need restart; lines2328–2330 then refuse *every* held operation. This
  is the exact emitted error, not evidence that the caller lost its operation ID.
  The unit is Type=simple (`nix/systemd/workspace-codex@.service:8`); enable/start
  returning does not certify the later `run_codex` registration write, one-use
  startup consumption or exec (`workspace-host:1757–1783`). CI shows native start
  before the refusal, but does not preserve the exact marker/read predicate at
  that instant. Delayed publication is a supported ordering, not a proven complete
  reconstruction of the CI marker timing.
- The owner already calls `complete_candidate_activation` (815–847): bounded
  socket wait, actual registration semantics, fresh profile/pending/claim checks,
  startup reconciliation/finish and destination process/socket proof. Only then
  does the worker continue participants and restore recorded clients/writers.
  Generic reconciliation instead owns fresh drain/quiesce/restart of both native
  and portals. It is the wrong path for an already admitted, held cutover.

**Smallest implementation boundary: three files, one owner.** Change only
`libexec/workspace-host`, `libexec/workspace-maintenance.rb` and
`test/workspace_host/maintenance_test.rb`. Keep the generic refusal in
`reconcile_codex_update` intact, including both defer_busy modes and its passive
matching-registration behavior. In `activate`, a validated held owning activation
configures services with portals deferred and returns to the existing worker
completion path without calling generic reconciliation. Do not report that branch
as reconciled/complete, clear pending recovery evidence, open portals or restore
terminals there. Non-held activation, including startup-only selection without
an active operation, retains its existing reconciliation/start behavior. Add a
short adjacent comment explaining the ownership and asynchronous-start reason.

Qualify this branch at the existing `maintenance_activation_target!` boundary,
before links/units change; pass the already determined held context (for example
an optional `held:` keyword) rather than making a new public API or Go action.
Reuse the ordinary decoded startup selection and active/inspect operation:
private activation, active operation ID and inherited maintenance ID must agree;
operation profile must be this profile; cutover/source-stop/activation intent must
be recorded and phase activating; selected package/package_root must equal its
admitted `activationPackage`; startup operation/candidate/authorizedProfileToken
must agree with that owner, selected package and current profile token. Preserve
all existing compatibility/generation/claim checks and use the admitted activation
package, not unconditionally `candidatePackage`: saved-source recovery legitimately
admits the source instead. Do not infer authority from an environment ID alone.
These are checks of existing state, with no new journal fields or grants.

Preserve the **completed-startup retry** as well as pending startup. StageStartup
is idempotent after FinishStartup for the same operation/target/source tuple
(`portal/internal/maintenance/startup.go:61–122`); the worker can retry after
startup-finish but before continuation/restoration. Its matching non-pending
selection is therefore valid, with the same owner/target/token and existing
completed startup evidence. Do not impose `pending == true` on all held
activation. Missing/foreign selection, unadmitted phase or changed target/token
still refuses before activation effects. Existing Go-owned grant consumption,
readiness and replacement-attempt checks stay authoritative and unchanged.

Do not replace this correction with a sleep, increased readiness budget, a second
restart, removal of the held guard, or unconditional success on registration
mismatch. No Go/native/Nix/SDK/input/service-policy change is needed. The product
guide already states ordinary owned activation, held portals and refusal of
generic restart; a code comment is enough for this correction, without another
document or framework.

**Regression and controls.** The old positive test
`test_maintenance_activation_keeps_portals_deferred_after_native_reconciliation`
stubs reconciliation to true and supplies no pending owning grant. The worker
fixture also stubs both activation and completion (maintenance_test.rb:516–521),
while TransitionHost replaces activate_installed (suspension_test.rb:476).
These tests could not exercise the failing composition. Replace/extend the owning
test locally; do not change shared fixture behavior for unrelated tests.

- Exercise real activate_installed environment propagation, candidate `_activate`
  and its held-target/ownership checks, with real generic reconciliation available
  and real marker mismatch. Use a small fixture-local command adapter for the
  candidate invocation plus existing temporary profile/registration/control
  fixtures; fake external systemctl/Nix transport only. The candidate invocation
  must receive the actual environment, not inherit the parent's Ruby instance
  variables. Let native start return before the candidate marker is published.
  Old code must reach the exact held-restart refusal; corrected code must leave
  portals/clients held, pending evidence retained and no generic restart/drain/
  probe effects. Also cover an already matching marker so behavior is not timing
  dependent. No live subprocess/service or sleep is needed for this ordering.
- Run the real complete_candidate_activation boundary after the fixture publishes
  the expected candidate marker/readiness. Preserve socket/marker, profile/pending,
  startup and destination checks and prove their order before continuation and
  restoration. A persistent bad marker or startup readiness refusal still fails
  completion and leaves recovery required, with no resume/restoration. Do not
  replace all these methods by success stubs; stub only the external observations
  needed by the existing unit fixtures. Existing worker failure/no-resume tests
  remain controls for error propagation.
- Table the narrow pre-effect negatives: missing/wrong inherited owner, wrong
  startup owner, changed selected target/token, and source-stop/activation intent
  not yet admitted. Assert links/services/pending/grant state unchanged on refusal.
  Exercise both a pending grant and completed same-operation startup retry, plus
  admitted sourceRecovered activation using activationPackage=source. Preserve
  source-recovery preparation/claim validation; this must not become rollback
  after candidate activation intent.
- Keep generic held reconciliation refusal tests in both defer modes, ordinary
  startup-only/nonmaintenance activation, matching passive refresh, all-inactive
  source startup, one-use launch ordering, forward pending-target recovery,
  failure-no-resume and Stop/held restoration controls. No weakening or broad
  combinatorial test scaffold is required.

**Compatibility, effects and verification.** No stored format, public CLI, API,
grant schema, migration, deadline or runtime contract changes. The owner still
chooses source versus candidate from retained preparation; target selection is
forward-only once admitted. The correction changes the candidate activation
implementation, not old immutable selected packages or saved operation journals.
Do not claim installing a new package repairs the existing failed operation or
perform recovery of it. Retain old roots/failures and current source/history.
Queues/goals/conversations, bounded pause/interruption, Stop suppression, stable
resume IDs, child ownership and exact recorded restoration sets stay unchanged.

Implementer quick package: Ruby syntax for the three affected files, one focused
old-red/new-green regression cycle, then the maintenance group through the
aggregate `ruby test/workspace_host_test.rb --name REGEX` in the repository Nix
environment. Include existing source-recovered/restoration-tail tests whose names
lack `maintenance`, and the named forward-selection/pending-evidence cases in
profile_transition_test.rb. Retain the existing run_codex one-use startup test
and relevant held/Stop terminal controls from test/dev_session_test.rb. Record
actual selectors/counts/results; one bounded batch, no stress/retry campaign.
Use the normal fresh watcher for uncertain duration, stop on a real failing
invariant and return the concrete mismatch rather than weakening a control.

One implementer owns this three-file correction and ordinary owning-maintenance
commit consolidation under main's source/index/Git window. Preserve retained9823,
first four/SDK history and independent later patches; provide actual old/new
range/diff/equivalence evidence and no-migration disposition. After quicks and
commit, independent affected review must inspect ownership qualification,
completed-startup and source-recovery compatibility, completion/error ordering
and the actual regression seam. Main then allocates exact new-source preparation
using the accepted workflow and original session-creation VM acceptance through
bootstrap and maintenance/recovery. Current9823 CI automatic success and B's
preparation remain scoped evidence; neither certifies changed-source runtime.
No automatic-only replay or revived Nix investigation is needed for this defect.
Full original VM/native/R29/W-C/rollout scope remains unchanged.

Settled: wrong reconciliation path during ordinary owned activation, masking
test seams and the narrow correction above. Unknown: the precise CI marker
snapshot and later corrected-runtime outcome; neither requires a new diagnostic
before implementation. Next observable result is deterministic old-red/new-green
owned activation plus negative authority/completion controls. No B mutable
preparation files were inspected. Only design.md edited; no application change,
test/Nix/CI/network/Git mutation/runtime/recovery/lifecycle action. Sufficient
brief complete; capacity returned. Main retains allocation and acceptance.

## Exactd56d bootstrap: retain the refused control action and fixed proof reason

Sufficient diagnostic-only brief, 2026-11-07; no product correction is established.
Current reviewed/published source is `d56d23843e7efb8d86e4be044f863387683417e3`,
tree `8efc4f459f01615c84c1c0789c7241e9d2c92ef7`. Confirmed current session and both
environment bindings, live ready architect0 gpt-6-astra/xhigh/workspace_write;
retained settings unchanged. Reused unchanged full guidance, read R AGENTS,
leading plan/state/review and accepted design6142. Only this document is edited.

**Observed and narrowed, not uniquely identified.** Independently rehashed the
released immutable raw log
`/tmp/lead-wakeup-R-publication-d56d-0ihr0lfb/ci-disposition-20261107T102301Z/creation-job-128372052517.log`:
SHA256 `d5abf161304a4c9b3a9558e9e1ff813846367fd96cf522670877ba269da3861c`.
Run42361961758/attempt1/exactd56d has14 starts/13 finishes, automatic48.61s and
bootstrap6332. At6639, the worker reports only
`maintenance control refused: identity-or-proof-refused`, then exits1. It does
not name a request action or failed proof. Snapshot6648 binds operation
`7d29c748-b901-471e-9bf4-e7c7b76f3fd7`, revision19, recovery-required,
sourcesStopped/cutoverIntent/activationIntent true, sourceRecovered false,
continuationsSettled false, no destination receipt fields and no restoration.
The source is klvafjdy and selected/admitted candidate37a1cpik. These are CI log
identities, not proof of equivalence to B's local driver or runtime.

The source-supported reachability is narrower than the generic message:

- Candidate service/timer configuration is visible immediately before the error.
  There is no selected-forward `_activate` command-failure wrapper, unlike9823.
  Together with the unchanged activate_candidate rescue, this supports successful
  return from candidate `_activate` and entry into the parent completion path.
  It is a control-flow inference, not a recorded controller action or complete
  timing trace. The accepted held-activation correction is not reopened.
- `complete_candidate_activation` (workspace-host:817+) waits for sockets and
  checks registration, then profile/pending/claim, clears pending Codex evidence,
  reads startup-status, optionally calls startup-reconcile and startup-finish,
  inspects the operation and calls destination-ready. The recorded source service
  set is nonempty. A successful destination-ready persists destination fields;
  subsequent recovery-required does not remove them. Controller.Status removes
  preparation/notice contents, not destination fields (controller.go:20–31).
  The actual projection thus
  supports failure before that receipt was retained, rather than successful
  continuation/restoration. It does not tell whether startup-finish happened or
  whether the pending Codex record was already cleared.
- The possible controller request boundaries in this completion interval are
  startup-status, startup-reconcile, startup-finish, inspect and destination-ready.
  The log cannot uniquely select one. Ordinary local socket/marker/profile errors
  have different Ruby messages. A returned startup `retry-wait` also raises the
  distinct `startup invocation readiness remains unproved`, not this refusal.
  Do not label this an ordinary startup delay or increase a timeout.

**Exact evidence loss.** `WorkspaceMaintenanceHost#maintenance_control`
(workspace-maintenance.rb:13–38) sends the action and invocation, validates helper
exit/JSON, but its refusal exception omits the action. It also intentionally
drains/discards stderr. `maintenanceControlCommand` routes the original request
to its immutable SourcePackage owner before decoding/dispatching it; at
maintenance_control.go:102–104 it converts receiver errors to a refused response.
`maintenanceControlFailureReason` (842+) preserves typed ProofError and timeout/
cancellation reasons but collapses other errors to identity-or-proof-refused.
The inspected receiver contains multiple distinct fixed errors: startup authority,
registered-unit tuple, invocation/process/cgroup, marker/listener, persisted startup
attempt/completion and destination/worker identity. No retained observation selects
one of those guards. The native model warning and nearby coordination collection
output do not establish the cause and do not justify changes to either subsystem.

Existing Ruby completion tests exercise the actual Ruby flow but substitute
controller responses (maintenance_test.rb:510–529). Go startup tests exercise
real store and passive socket handling with constructed unit/marker/process
fixtures (maintenance_startup_test.go:168+ and390+). These are useful controls;
they neither reconstruct this packaged failure nor test preservation of its
original proof reason through the Ruby/Go reporting boundary.

**Minimal owner package: four existing files.** Implementer changes only
`libexec/workspace-maintenance.rb`,
`portal/cmd/workspace-portal/maintenance_control.go`,
`test/workspace_host/maintenance_test.rb` and
`portal/cmd/workspace-portal/maintenance_control_test.go`.

1. Add the requested control action to the Ruby refusal exception; include the
   requested operation UUID when present and valid. Use only bounded action
   tokens/UUID, with a constant fallback for invalid/missing values. Preserve the
   existing reason, exit/size/JSON checks and refusal behavior. This is local
   correlation, not authority. Do not print the request, environment, preparation,
   entire response, stderr or a success trace.
2. In the existing Go failure-reason mapper, preserve distinct fixed reason tokens
   for the inspected completion guards. Use an explicit finite allowlist of the
   literal errors in startup selection/attempt/finish, reconcileStartup and its
   direct proof helpers, and destination-ready/worker ownership. Map exact known
   literals to constant tokens (space-to-hyphen spelling is sufficient); do not
   return arbitrary err.Error() or dynamically register/classify errors. Include
   the concrete authority, registered-unit, process/invocation/cgroup, marker,
   listener, stale-attempt, unconsumed/unready-grant and destination-epoch guards,
   so those different failed predicates remain distinguishable. Preserve existing
   typed ProofError, timeout and cancellation handling, and the current generic
   fallback for unknown/unlisted errors. No journal/response field or version is
   added; status remains refused and existing reason is diagnostic text. Do not
   modify the guards or successful/retry-wait results themselves.

The allowlist is confined to this observed completion path, not a project-wide
error taxonomy. A syscall/decoder error outside it may still yield the generic
fallback; the newly recorded action then gives a bounded residual question.
Retaining that limit is preferable to dumping arbitrary error strings or adding
state/protocol tracing. No fixture dump, diagnostic RPC, new framework or broad
instrumentation is needed for this package. No product documentation changes are
needed because supported behavior and recovery semantics are unchanged.

**Meaningful quick verification.** One focused old-red/new-green cycle must prove
the actual reporting gap. A Ruby transport fixture should exercise the real
maintenance_control method with a refused JSON response and assert the exact
requested action/operation correlation, reason preservation and raised error;
do not replace the method under test with the existing success stub. Keep a
success response unchanged, plus nonzero/malformed/bounds refusals. A small local
fake helper or existing Open3 test seam is enough; no native/systemd execution.
In Go, use the existing startup/worker fixtures to induce actual receiver errors
for at least changed startup authority or marker, unfinished startup grant and
wrong worker/destination identity, then apply the real failure mapper and assert
distinct safe reasons plus unchanged refused effects/store evidence. This checks
real rejection paths rather than merely mirroring a constant lookup table. An
unknown error containing a sentinel payload must retain the generic fallback
without leaking that payload; preserve typed proof/timeout/cancel controls.

Run Ruby syntax and the focused host aggregate selector, and
`go -C portal test -mod=readonly ./cmd/workspace-portal` with a focused regex for
the added diagnostic tests and existing startup/maintenance worker controls.
Retain the owning held-activation completion/refusal, completed-startup and
source-recovery cases; no repeated full stress batch. Record actual commands,
counts and results under the normal quick bounds/watchers. Stop on a real failure.
One implementer owns the narrow source/quick/commit package under main's window;
preserve d56d and reviewed history, consolidate in the owning maintenance change
with exact old/new equivalence evidence, then independent affected/history review.

**One necessary runtime observation, only after main allocation.** Read-only
inspection cannot recover the erased `(action, receiver refusal reason)` pair.
After quicks/commit/review, use one ordinary original packaged session-creation
CI attempt on the exact diagnostic successor through normal publication, preserving
the original bootstrap prerequisites/cases/bounds. This is a proposal, not a CI
query, rerun or release. Bind actual head, source owner/candidate and log to that
attempt; the new operation's saved source package itself must contain the
diagnostic mapper, since forwarding to an old owner would still erase the reason.
Preserve current B preparation separately. No unmodified d56d replay,
automatic-only case, local-driver equivalence assumption or extra diagnostic
target is proposed. Any local preparation remains the already accepted exact-source
workflow under main, not a new investigation here.

At first failure retain the correlated action/reason and existing operation
projection. A concrete fixed proof code selects the corresponding narrow guard
and its actual evidence for the next source decision. If the fallback remains,
report that exact action and unclassified receiver error as the bounded residual;
do not retry or add targets. If the original suite passes, report non-reproduction
and its actual coverage, not a product fix or proof of the original cause. The
original d56d failure remains unresolved until causally explained or explicitly
disposed by main. Do not infer acceptance from the code being diagnostic-only.

All current admission/effect ordering remains unchanged: source shutdown and
activation intent, selected forward package, original worker/claim/generation,
completed-startup/source recovery, actual registration/process/socket proofs,
held portals/clients, stable resume IDs, Stop, queues/goals/conversations and
responsible-thread children. No timeout/sleep/guard relaxation, fake completion,
strict MCP contract, format/migration or native/package/input change. Failed old
operations still route through their saved source package; a corrected candidate
alone does not instrument or recover them. No old-operation action is proposed.

Settled: the reporting boundary erases action and untyped proof identity; current
source/log cannot justify a product repair. Open: the actual failed action/predicate
and successor runtime outcome. Next observable result is tested safe failure
correlation, followed only on main allocation by the one original packaged attempt.
No B mutable stores/outputs/logs/processes or C unfinished packet inspected. No
application edit/test/Nix/query/eval/build/copy/CI/network/Git mutation/runtime/
recovery/claims/lifecycle action. Brief complete; capacity returned, session open.

## Exact3afe startup: resolve the native socket alias for listener ownership proof

Sufficient two-file correction brief for135e2cc9, 2026-11-07. Verified current
session/environment and live architect0 Astra/xhigh/workspace_write/full_access;
settings retained. R is `3afe8067c457e6c95eea34aa914ed5b3abec8761`, tree
`95f69efe4c99c43bc99bb9aaa6c99c9d0df09181`. Read current leading records, R AGENTS
and accepted6316; reuse unchanged full applicable procedures. This is design only.

**Current failure and exact guard.** Released raw log
`/tmp/lead-wakeup-R-publication-3afe-oq0ztb6r/ci-observation-continuation-20261107T112650Z/creation-job-128388178279.log`
SHA256 `d33ab4323c12863904515b11501785d3c8eb717718b9e651c80d7f7e97ddf8a1`
identifies startup-reconcile / startup-listener-identity-unavailable at6816,
operation `9d292655-b943-4654-97dc-81408233fb76`. Snapshot6831/revision19 retains
source stop, cutover and activation intent, selected candidate01mrwyfj, source6vffci2d,
sourceRecovered=false and continuationsSettled=false; recovery-required remains
an effectful failure. Fourteen cases started/thirteen finished before bootstrap.
These facts do not establish oldd56d's cause or any CI/local-driver equivalence.

`processOwnsListener` (maintenance_startup.go:348–379) returns this exact error
only after successfully reading /proc/net/unix and finding no row with eight
fields, the supplied pathname and listener flag00010000. It has not yet inspected
the consumed PID's FDs. Thus this is unavailable *lookup identity*, not a proved
foreign process owner or absence of a working socket. Its caller (211–305) has
already checked selected startup authority, registered unit/native tuple,
consumed PID/process/invocation/cgroup, new socket epoch, active unit/no job and
matching launch marker. Passive LoadedThreadIDs and the final epoch/process
recheck have not been reached for the refused grant. No timeout inference follows.

**Concrete production representation mismatch.** Earlier completed native-source
packet `/tmp/lead-wakeup-eof-interpretation-B-i8q_2jmb/diagnosis-result.json` points
to exact upstream360319d8dee62d87e2d59fc0c21805d79519cfed. Its retained
`primary-source/codex-rs/app-server-transport/src/transport/unix_socket.rs` was read
and independently hash-matched to
`a2ff08a28cb52c8a11895bb4cff41401180fb0efd0491984b77af381e7efafe3`;
primary-source.json retains origin/revision/Git blob10fc9067/bytes19732.
The old full-source store pointer is absent; no restoration/acquisition was done.
The retained source file suffices: bind_private_daemon_socket (69–145) derives a
protected physical path, binds there, then creates the requested rendezvous path
as a symlink to it. protected_socket_path (354–368) hashes the canonical advertised
parent/name into the native shared socket directory. App-server's UnixSocket
branch calls this acceptor (retained app-server/src/lib.rs:832–833).

Current flake.lock still selects llm-agents91ff550fe42d4dd51dcf8b6bad87a0134fe7f314;
its existing local recipe/hashes declare0.165.0 and source NAR
`sha256-b9PpwNQeZsJIN4wbGA3FLfWAKd2EDMN5E/zj/Y62/vk=` matching the earlier
accepted source provenance. The recipe's daemon patch changes prepare_install,
not this transport; R's assembler copies native executables unchanged and the
maintenance fixture changes only output name. This binds the supported source
contract; it is not a new binary equivalence or guest /proc capture.

Ruby run_codex advertises the registry socket path. startupTarget reconstructs
that same path and checks the original service tuple. session.SocketIdentity
(recovery.go:222+) uses unix.Stat, which follows the alias, and passive RPCs also
connect through it. Only processOwnsListener incorrectly compares the advertised
spelling with the physical bind pathname recorded in /proc/net/unix. A healthy
native listener behind the supported symlink therefore fails this proof.
TestProcessOwnsExactNativeListener and startupRegistrationTest.startTargets bind
Go listeners directly at the advertised name; their coverage misses this seam.

This is a source-supported consumer compatibility defect, not a need to alter
the fixture/native identity, relax ownership or wait longer. The exact CI symlink
target and /proc row were not exported, so a complete incident reconstruction
remains unproved; the independent representation defect and deterministic test
are sufficient for correction without another diagnostic run.

**Implementation: one owner, two existing files.** In
`portal/cmd/workspace-portal/maintenance_startup.go`, resolve the supplied socket
path with filepath.EvalSymlinks inside processOwnsListener before comparing
/proc/net/unix pathnames. Propagate resolution failure; no fallback match, basename
match, guessed native hash/directory, path rewrite or retry. Keep the exact unique
listening-row lookup, inode and `/proc/PID/fd -> socket:[inode]` ownership check.
Retain the existing caller's before/after logical-path socket epoch and process
identity comparisons around passive readiness, and selected native/marker/unit
checks. The registry, journal, grant and RPC path remain the advertised path;
the resolved path is a transient lookup value only. Direct-bound sockets continue
to work. A short nearby comment documents why alias resolution is required.

Do not change session.SocketIdentity, native startup, the systemd units, Go/Ruby
grant handling, response taxonomy, timeout or package/input pins. No extra
canonical-path trust policy is needed under the trusted-local-operator contract;
actual ownership and replacement detection remain mandatory.

**Deterministic regression and controls in maintenance_startup_test.go.**

- Bind a real Unix listener at physical pathP and symlink advertised pathA to P.
  Assert current PID owns P and, after correction, A. The old helper must fail A
  with the exact startup listener identity unavailable error; this is the focused
  old-red/new-green mechanism. Preserve the existing direct-path positive and
  wrong-path/missing-PID controls. An alias to a live socket must still fail for
  a different live PID that does not own its FD; a dangling alias and a closed
  listener with retained socket node must also refuse. No sleeps are needed.
- Exercise the real reconcileStartup/store/passive-RPC path with the existing
  startup fixture configured to bind target listeners physically and publish
  advertised aliases. Keep actual registration/grants/logical source paths and
  selected profile checks; assert consumed attempts become ready and FinishStartup
  succeeds for active-source and all-inactive coverage. Reuse the existing helper
  with a small local setup option, not a new fixture or production injection seam.
  Retain direct binding coverage as a compatibility control.
- Prove existing epoch protection still detects alias replacement: at the fixture's
  passive RPC boundary deterministically retarget A to another already-bound
  socket, then let the request return. The unchanged post-read check must refuse
  startup-changed-during-readiness-proof; the attempt stays consumed, FinishStartup
  refuses and no destination/continuation effects are certified. Use a test-local
  callback/channel in the existing handler, not polling or a production seam.
  Keep existing wrong registration/invocation/native/argv/profile, failed-startup
  replacement and completed-startup retry tests unchanged.

One focused old-red/new-green cycle, gofmt/normal quick checks, then the bounded
existing command `go -C portal test -mod=readonly ./cmd/workspace-portal -run
'^(TestProcessOwnsExactNativeListener|TestStartup.*|TestMaintenance.*)$' -count=1`
(add the exact new names if outside these prefixes) in the repository Nix
environment. No repeated stress campaign. Existing internal maintenance startup
store controls may be included once for ready/failed/finish preservation; no
unrelated full suites. Use the normal watcher if duration is uncertain and stop
on the first real mismatch. Tests require only disposable Go sockets/files and
existing systemd observations; no native/model/VM is required for the quick proof.

**Compatibility and acceptance.** No API, stored-state, source protocol, grant,
migration, native/input or budget change. The proof still requires the selected
process to own the exact listening inode, with the logical endpoint generation
stable before/after readiness. The fix supports existing direct and native-alias
representations. Forward selected activation, held portals/clients, one-use
startup/source recovery/completed retry, claims, Stop and stable resume remain.
Queues/goals/conversations and responsible-thread children are unchanged. Old
operations still execute their saved source package; installing a new candidate
does not repair old owner code or authorize recovery of old failures.

Implementer owns two-file source/quicks and ordinary owning-maintenance commit
consolidation under main's window; retain3afe/failure refs and exact full-history,
single-SDK/no-migration evidence. Independent affected review must inspect alias
resolution without ownership weakening, the actual receiver seam and replacement
control. After accepted quicks/commit/review, the next long acceptance is the
ordinary original session-creation packaged VM/CI on the exact successor through
bootstrap and existing maintenance/recovery cases, allocated by main. No extra
standalone listener diagnostic or packaging re-investigation is needed. This
design releases no source execution, publication or runtime. Preparation evidence
cannot silently transfer to a changed source; broader existing full VM/native/
R29/W-C/rollout acceptance remains unchanged.

Settled: supported native alias versus literal /proc lookup, missed direct-bind
test seam and two-file correction. Open: exact historical guest row and corrected
packaged outcome, neither blocks implementation. Next result is deterministic
alias old-red/new-green with unchanged ownership/replacement controls. Only
design.md edited; no test/Nix/query/build/eval/copy/CI/network/Git mutation/native/
guest/profile/recovery/claim/lifecycle action. A historical-source filename search
incidentally surfaced a current implementation-c status line; it was not used as
evidence and no unfinished C packet/index or B output/process/store was inspected.
Brief complete; capacity returned, session open; main owns allocation/acceptance.

## Exact7540 restoration: bind owned terminal admission to recovery permission

Sufficient correction brief for fffea413, 2026-11-07. Current/env/session match
2026-11-03-lead-wakeup-delivery; live architect0 remains Astra/xhigh/workspace_write,
full_access, settings unchanged. Read current leading plan/state/review, R AGENTS,
applicable full procedures and the preceding briefs. Exact R is
`7540c669822a6c38bc7ae634b02522852559c62e`, tree
`0c6633567e9b0ba9cceb5d672cdcbbd689d738ff`. Main owns implementation/allocation.

**Evidence and limit.** Rehashed the released creation-job-128400429855.log under
`/tmp/lead-wakeup-R-publication-7540-wuw3828x/ci-parent-fallback-20261107T121957Z`
to `7228bb796abf9486b9b7239a9758b479245fed2345bb322d2df6c0b5115f7156`.
Lines6835–6878 contain ten owned terminal restoration admission refusals;
6881 aggregates them and6893 records revision23 of
`cd89f23a-1cfb-4eca-8680-04cb07393eb3`, recovery-required, continuationsSettled=true,
participants=[], ten terminal intents, updated restoration incomplete, and different
source/destination socket epochs. Source p4xf3z and selected candidate sybfqc2 remain
literal log identities. There is no emitted terminal-sync response or RecoveryStore
record: neither the actual status/reason nor the exact refused boolean is observed.
This is later progress, not bootstrap/native acceptance or an explanation of d56d.

**Demonstrated contract defect.** workspace-maintenance.rb:445–463 checks the
saved restoration package/token under transition exclusion, then workspace-host:
3323–3346 calls that package's ordinary `dev-session sync --as-is` for the recorded
terminal set with DEV_WORKSPACE_MAINTENANCE_RESTORATION. INVOCATION_ID is retained
through codex_environment; no lost-invocation mechanism is demonstrated.
dev-session:9564–9580 reads recovery `held` before sending terminal-sync. The Go
receiver routes to the immutable SourcePackage, checks worker invocation and an
incomplete restoration, matches the terminal intent and suppresses a stopped root
participant; otherwise it returns admitted (maintenance_control.go:591–605).
It does not establish current-generation recovery permission.

recovery.go:55–73 reports held whenever Recovery.Active(root,currentEpoch) is
false; session/recovery.go:237 requires exact epoch plus root membership.
continueParticipants advances permission only for its Participants
(maintenance_cutover.go:140–160). Empty Participants therefore leave the old
terminal recovery generation unchanged, despite successful native replacement.
A supported idle-but-running terminal, recorded before quiescing, becomes held
solely because its App Server changed. Current terminal-sync can admit it while
the consumer deterministically refuses it. Fixing the producer alone still leaves
Ruby using its pre-admission boolean. This independent source defect justifies a
correction; it is not a claim that CI exported the missing response/record.

The earlier stdout fix remains correct. Its real-transport positive fixture
hardcodes held:false, and its admitted/held negative never models a legitimate
generation transfer. Go tests cover terminal incarnation and continuation stores
separately, not terminal-sync composed with real recovery state. Host worker tests
stub terminal restoration above this boundary. Keep those tests' other controls.

**One owner; four existing files.** Change
`portal/cmd/workspace-portal/maintenance_control.go` and its `_test.go`, plus
`libexec/dev-session` and `test/dev_session/tmux_runtime_test.rb`. No general
RecoveryStore policy, worker orchestration, native/SDK/Nix, fixture, timeout,
journal format or response-schema change. A short adjacent rationale is sufficient;
the existing workspace-updates/dev-sessions contract need not be rewritten.

- Make terminal-sync's admitted response mean that the exact recorded terminal
  root has current-generation recovery permission. Reuse the existing operation,
  retainedIdentity/service and RecoveryStore.Update machinery, with a small local
  helper if useful. Recheck the current worker and incomplete restoration and
  exact workspace/slug/root/incarnation before mutation; retain lifecycle refusal.
  Use the saved source service proof for pre-cutover cancellation; use the saved
  destination proof for updated **and source-recovered** outcomes (source recovery
  also has a new native generation). The selected restoration package/profile
  token checks in the enclosing Ruby tail remain mandatory. Reuse existing
  destinationServiceIdentity/sourceCurrent checks rather than inventing a proof.
- Under the existing operation/recovery serialization, retain root StopRevision
  suppression and treat an exact recovery record with Automatic=false as
  suppressed, without enabling it. Missing, mismatched or unreadable recovery
  identity refuses; do not seed records. Require the record's epoch to be the
  recorded source or the proved current service epoch, not a third generation.
  For an eligible recorded terminal, transfer only its root permission to the
  proved epoch. Clear stale-generation ActiveThreads/Continuation using the
  existing recovery convention; preserve already-current participant/member
  permissions, add the root idempotently, and preserve Automatic. Recheck the
  socket epoch at the write boundary. Do not grant all members or restart children.
- This intentionally distinguishes a generation hold from Stop: the durable
  terminal intent, written only after validating a running managed Codex pane
  and before replacing it with its shell, authorizes restoring that client even
  when it had no active turn. Ordinary held sessions without that owned intent
  gain nothing. No participant, resume message, queue row or goal is fabricated.
  Use fresh operation state for Stop ordering; Stop before admission suppresses,
  Stop after admission retains ordinary interruption/exclusion. No new stronger
  guarantee or long/native call under the admission locks is required.
- In Ruby, preserve the ordinary nonmaintenance held early return. For maintenance,
  request owned admission first, return immediately on suppressed, and accept
  admitted only after a fresh recovery-status read says not held. The initial
  nonmaintenance read may be moved into its branch; do not reuse its old boolean.
  An admitted response with permission still held must continue to fail before
  materialization/client effects. Preserve real stdout tuple parsing, nonzero/
  malformed/refused handling, root/provenance/readiness, exact tmux pane/session,
  shell/native-version checks and already-running-client idempotence.

The operation's general new-work fence remains closed through terminal and portal
restoration. Granting this recorded root permission does not complete restoration,
send another maintenance continuation, drain queues or activate a goal. Existing
normal terminal resume is the effect; no new native RPC belongs in terminal-sync.
An error after permission publication leaves an incomplete owned tail. Retry of
that same tail rechecks identity, preserves current permissions and retries the
ordinary client effect without replaying cutover/activation/continuation.

**Deterministic quick proof and controls.** One old-red/new-green cycle, no stress
or diagnostic CI loop. In the Go control test, use disposable real Unix sockets,
the existing exact process/marker/profile helpers, real maintenance and recovery
stores, a recorded terminal and zero participants. Seed ordinary running-root
permission on source epoch, replace the socket and record the proven destination,
then invoke the actual terminal-sync worker path. Assert the root is not Active at
the new epoch before admission, but is Active after admitted; old source admits
without satisfying this postcondition. Verify a repeated call adds no duplicate
permission and leaves operation completion, queues/submissions and other roots
unchanged. No native/model process is needed for this test.

Cover updated/source-recovered versus pre-cutover cancelled source identity, a
current-epoch member permission that must survive root admission, and failed-tail
retry. A compact table must keep wrong worker/operation/root/incarnation/socket/
selected package, absent/completed restoration and missing/mismatched recovery
fail-closed before permission changes. StopRevision and Automatic=false suppress
without record or client effects. Preserve existing Stop-after-admission tests;
do not invent a terminal-presentation completion requirement.

In the existing Ruby/Open3 responder, model held:true before owned admission and
held:false only after its successful response. The actual caller must consume the
post-admission status before its exact retained-root client command; old Ruby must
fail the positive case. Retain admitted-but-still-held, suppressed, refused,
malformed/nonzero, ordinary generic-held, changed-pane and already-running controls.
This complements the real Go/store test; do not replace both sides with matching
constant responses or add a cross-language fixture framework.

Use the repository Nix environment, syntax/gofmt and one focused count=1 Go batch
for new TestMaintenanceTerminalSync cases plus existing maintenance/recovery
controls in cmd/workspace-portal, internal/maintenance and internal/session;
use existing selectors to keep the batch bounded (60s test timeout, no count10).
Run tmux_runtime_test.rb and the relevant existing workspace_host maintenance
restoration/cancellation/failed-tail cases once. Retain exact commands, old failure,
new pass, test counts and source hashes. A first unexpected behavior stops the
package for main disposition; no unrelated suite or timeout inflation. Required
long/uncertain checks use the normal watcher only after separate allocation.

**Compatibility and acceptance.** Existing transport/schema, stored record formats,
immutable protocol owner, selected package/native/process/listener proofs, profile
generation/token and claims remain. Root permission is a narrow owned-restoration
effect, not a generic sync/Stop bypass. Source-recovered and cancelled outcomes
keep their distinct service identities; an unfinished tail remains recoverable.
Queues/goals/conversations, original submission IDs and responsible-thread child
ownership stay intact. Saved old SourcePackage code still owns old journals;
installing a corrected candidate cannot repair or authorize recovery of7540.

After main allocates, one implementer owns this correction, focused quicks and
ordinary owning-maintenance commit consolidation; retain7540/failure evidence.
Independent affected review must assess authority, permission/Stop ordering,
real producer/consumer composition and full-history/single-SDK/no-migration
disposition. Then the necessary long acceptance is the original packaged
session-creation successor through bootstrap and existing maintenance/recovery
cases, on main allocation. No extra local preparation cycle or standalone target
is proposed. Existing remaining native/R29/W-C/VM/rollout scope is unchanged.

Settled: missing owned-terminal generation permission plus stale consumer read,
four-file boundary and meaningful deterministic proof. Open: historical response/
recovery bytes and final packaged behavior; do not label all ten CI refusals
uniquely reconstructed. Next observable deliverable is reviewed source with the
old-red/new-green seam and retained controls, not another diagnostic run.
Only design.md edited; no application/test/Nix/CI/network/Git/runtime/recovery/
lifecycle action or mutable B/C packet inspection. Capacity returned; session
open. Stable session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-03-lead-wakeup-delivery/.

## Exacta57 fast check: test the native-call bound, not a whole-pause stopwatch

Sufficient one-file test correction brief, 2026-11-07. Verified current session,
both environment values, live architect0 design/ready/Astra/xhigh/workspace_write
and full_access; settings retained. Read leading state/plan/review and R AGENTS;
reuse unchanged full applicable workspace procedures and documentation skill.
R is clean `a57d3e6fa4768341ae1c83c5356a0ab4f06657bb`, tree
`2c5cf2ec27210900f8c823f724238419b5ef1ebb`. Main owns allocation and acceptance.

**Exact failure.** Released
`/tmp/lead-wakeup-R-publication-a57-yjap_85i/ci-parent-observation-20261107T133902Z/fast-job-128419047514.log`
rehashes to `1c56a5eceba6f8598e4cf1dacf3d178ebf531f221c6988ecf77a684dd4dd62f7`.
Lines1896–1902 identify TestMaintenancePauseSilentNativeOperationsAreBounded /
turn/steer, maintenance_pause_test.go:343, elapsed1.030685502s. The exact failed
conjunct is `time.Since(start) > time.Second`: err is nonnil, containing
notice-outcome-unknown, context DeadlineExceeded and pause-native-timeout; returned
Status is empty, not paused. The assertion's wording does not establish escaped
native cancellation. Fatal occurs before the saved operation and submission-ledger
assertions, so this failed subtest does not prove those later values. Secondary
package/builder/catalog failures are not separate product mechanisms.

The pause implementation, this test and the SDK pin are unchanged from7540.
Current test SHA256 is d512c69e07dc02d31265b0d3ad12a7ef83ca3ee7dc37e9fc4e9a092a74ab859e;
pause implementation is da380b91231270b9ddaa3938ea646a2fa00939ae040b39d2ec61b06bf1d518b3.
The prior grace-transition correction changed a different test. No connection to
the accepted terminal-permission correction or historical7540/d56d cause follows.
The released final CI view still had creation/archive active; no current creation
output or whole-run conclusion is used here.

**Source-supported mismatch and remaining uncertainty.** The silent test configures
500ms per logical call,700ms recovery, a saved grace deadline1s after setup (already
expired for interrupt), and a2s parent. Its stopwatch covers the entire `m.pause`:
state/identity reads, a fresh client and ActiveTurnID, a separate ConditionalSteer,
submission storage, result saving and Close. `pauseNative` (maintenance_pause.go:
134–172) derives the earliest call/grace/allowance/parent context for each logical
operation; the cap is not a timer on this entire sequence. `savePauseResult`
(177–185) has a separate capped local write and can preserve uncertainty after
caller cancellation. Thus valid native work up to the grace boundary can still
require result bookkeeping afterwards. The one-second total assertion is a
stronger fixture requirement than the documented native-call contract.

The pinned c3c2adb705f5 SDK was inspected read-only from the existing module cache;
conditional_steer.go/client.go/submission_database.go match the same-session exact
c3c2 committed blobs (SHA256 a98e6ef3/383ec9a5/ad843c38 respectively). ConditionalSteer
uses the supplied context for dispatch and subsequent reconciliation and does not
renew its native deadline. Client.Close uses CloseNow. Its local SQLite submission
transactions have their existing independent bounded storage contexts; they are
not a second native request budget and do not prove any actual CI contention.
The error means a potentially submitted steer was not reconciled, not that it was
definitely sent or definitely absent. It must remain unknown under the original
NoticeID, never be relabeled unsent or resent with a new identity.

No phase timestamps isolate the observed extra time among setup, scheduling,
storage, native waiting and result saving. Do not call this a proved scheduler,
cache, Nix, SDK or product defect, nor claim a complete timing reconstruction.
The independent total-versus-call test mismatch is sufficient to correct its
oracle without a production edit or another diagnostic CI. Product defaults stay
90s configurable grace,5s logical native cap and one30s recovery allowance.

**Implementation boundary: only maintenance_pause_test.go.** Keep every existing
numeric fixture budget and production file unchanged. Keep the real client,
SQLite submission ledger, persisted operation and ordinary fake native endpoint.
Do not preseed acceptance or change the shared fixture's production-facing API.

1. In the failed four-method test, replace the unsupported total1s verdict with
   positive phase and outcome checks. Use the existing method callback and local
   atomics/counters to prove the selected silent method actually arrived; record
   its first arrival for failure output. For steer, require exactly one dispatch
   observed by the endpoint. No first-method/handshake failure may count as a
   successful silent-steer test. A missing target remains an explicit failure.
2. Require a nonnil DeadlineExceeded-containing error, not-paused result and a
   still-live original2s parent. For steer require notice-outcome-unknown; for
   passive/list/interrupt cases require the existing applicable native/interrupt
   timeout classification. Grace may select the existing interrupt pass, but
   unrelated errors or caller-budget exhaustion never satisfy the test. The
   parent is an unchanged outer test guard, not a replacement production limit.
3. Always inspect the saved operation with its load error checked. Preserve the
   exact saved PauseDeadline, no draining-writers/cutover/activation, unchanged
   StopRevision and continuation identity/disposition. For steer assert unknown
   NoticeDisposition, exact original NoticeID/action/target and retained submitting
   ledger evidence. Preserve no turn/start or thread/resume and no duplicate
   steer; normal prerequisite steer in the child-list case is not a resume.
   Gather this small evidence before the combined failure report so an overrun
   does not hide the durable-state result as the present Fatal does.
4. Add a direct native-cap control beside the existing deadline controls. Call
   the actual pauseNative with its existing callback, configured500ms cap and
   grace/allowance/parent later than that cap. In the immediate callback capture
   its context and deadline. Bracket the derivation with local before-entry and
   callback-entry times and require the deadline within
   `[before + 500ms, callbackEntry + 500ms]`, strictly earlier than the other
   supplied bounds; require the callback was entered and parent is live. After
   return verify the derived context is cancelled. This tests the computed cap
   directly without sleeps, clock injection or a production seam. Existing exact
   caller-deadline, shared-allowance/nonrenewal and grace-transition controls
   continue to prove the other competing bounds.

Keep elapsed time as failure context, together with method/count/first-entry,
saved deadline, caller.Err, returned reason/error, load result and saved notice/
phase/continuation. Do not turn this into permanent generic tracing or dump
unrelated state. A test machine unable to reach the intended phase or finish
before its existing parent guard still fails; there is no skip or blind retry.

**Meaningful verification.** The preserved actual CI failure is the old-red for
the invalid total stopwatch; do not manufacture a historical reproduction with
sleeps or claim a local green identifies its timing cause. The added cap assertion
must independently reject an omitted/renewed call cap: one finite negative-control
mutation in an isolated disposable source copy may bypass that cap, run only this
control and require its specific deadline assertion to fail. Restore/preserve exact
production bytes; no mutated production is committed or packaged. This control
guards against merely deleting a useful timeout test. No stress campaign is needed.

After main allocates the one owner, run syntax/gofmt and one count=1 focused batch
in the repository Nix environment, `go test -mod=readonly ./cmd/workspace-portal`
with exact selectors for the new cap control, SilentNativeOperationsAreBounded,
CallerDeadlineWinsNativePauseCap, SharedAllowanceDoesNotRenewAcrossCalls,
ExpiredRecoveryHasOneSharedAllowance, GraceBoundaryRetriesPassiveReadInInterruptPass,
GraceExpiryRetainsUnknownSteerForRecovery, PersistedCancelAndCallerCancellationBoundOutstandingRead,
UnknownSteerIsSavedAfterCallerExpiresAndCleanupIsBounded and the existing saved-
deadline/Stop/no-duplicate-resume controls. Use count=1 and a60s batch guard; no
unbounded count loop. Preserve original elapsed evidence, exact commands/results,
target-method proof, state/ledger assertions and unchanged production/pin hashes.
An unexpected phase, deadline, parent expiry or state failure stops expansion
and returns that precise fact to main; do not increase budgets or repair siblings.
Use the normal watcher for any authorized uncertain-duration execution.

**Compatibility and acceptance.** No product code, storage/protocol/schema,
authority, grace/cancellation policy, public preparation, native/SDK/input or
deployment/recovery change. Unknown submissions, Stop, saved deadlines, bounded
native operations, queues/goals/conversations and responsible-thread children
retain their existing contracts. Ordinary owning-test/maintenance history
consolidation is appropriate under main's Git window, preserving a57/failure refs,
single SDK stream and no-migration disposition. Independent affected review must
check that exact deadline and outcome coverage replaces the invalid total bound;
it must not accept error-only success or merely a larger stopwatch threshold.

After committed quicks and accepted review, main owns publication and the original
packaged successor fast check/session-creation acceptance. No unmodified a57 rerun,
extra local preparation, native test or new diagnostic target is proposed. The
currently running a57 creation/archive and any future C output remain separately
owned. Whole-VM/native/R/W-C/rollout requirements are unchanged.

Settled: exact elapsed-only failed conjunct and source-supported fixture contract
mismatch; one-file correction with positive method, durable outcome and direct cap
proof. Open: precise CI phase timing and final packaged successor result. Next
observable deliverable is the narrow tested/reviewable fixture change. Only
design.md edited; no checks/Nix/CI/network/Git mutation/runtime or mutable C/B
inspection. Capacity returned; session remains open; main owns next allocation.

## Exacta57 creation: restore proxy-created roots before maintenance capture

Sufficient fixture-only brief for c04e83d1, 2026-11-07. Current/env match the
bound session/workspace; live architect0 remains ready/design, Astra/xhigh,
workspace_write/full_access, settings unchanged. Read leading records, exact R
AGENTS and full applicable guidance. All repository reads use committed
`a57d3e6fa4768341ae1c83c5356a0ab4f06657bb`, tree
`2c5cf2ec27210900f8c823f724238419b5ef1ebb`; B's mutable test/index/output is excluded.
Main owns allocation, source acceptance and publication.

**Evidence and uncertainty.** Released creation-job-128419047638.log under
`/tmp/lead-wakeup-R-publication-a57-yjap_85i/ci-completion-20261107T135523Z`
matches SHA256 `7b53441cb38f5a237b2f6fc407ef76bd870589865f598be5c40762f3fe630396`,
1565090 bytes/8223 lines. Original emitted refusals6904/6907 name `after` and
`before`; aggregate6955/worker6956/bootstrap6961 follow. Operation
`cc823793-6461-4a58-b90e-690805058e75` has ten terminal intents, no participants,
settled continuations and incomplete restoration. Eight other emitted client
restart messages are progress, not independent proof of complete restoration.
The actual terminal-sync response and contemporaneous recovery records are absent.
Ruby's shared error at dev-session:9579 does not distinguish non-admitted status
from admitted plus a fresh held status. Neither branch is uniquely observed.
No historical7540/d56d attribution or CI/local-driver equivalence follows.

**Independent fixture mismatch.** session-creation.nix:912–944 moves the native
advertised socket alias to `.native`, binds a distinct proxy socket at the original
path, creates precisely these two roots through it, then removes the proxy and
restores the alias. creation_transport.py uses real `websockets.unix_serve`.
The log records installation5765–5774 and completed teardown6345–6351 before
bootstrap6374. Ordinary successful creation calls `recovery_state!(..., 'running')`
(dev-session:1337); RecoveryStore.Set records SocketIdentity of the advertised
endpoint. That identity follows the alias and includes boot/device/inode/ctime
(session/recovery.go:222–267). The proxy epoch is different from the restored
native source epoch, and from the later destination epoch.

No explicit ordinary restoration follows teardown. Automatic recovery need not
repair this: web/recovery.go:180–184 returns for a still-interactive root without
rewriting its epoch. A different observed recovery path could have changed a
record, so the historical record bytes remain unknown. Nevertheless, the fixture
does not establish the source-generation permission needed by its next test.
terminalSync correctly refuses a record outside the captured source/proved
destination generations (maintenance_control.go:867–875). Existing third-generation
negative coverage deliberately enforces that rule. The accepted6633 producer and
fresh Ruby read remain correct; no production guard repair is justified.

**One implementation file: nix/tests/session-creation.nix.** After restoring the
native alias and before public maintenance bootstrap, explicitly restore only
the two retained `before`/`after` roots through ordinary public commands. This is
fixture setup after its own endpoint replacement, not a maintenance admission
exception or recovery of a saved failed operation.

1. Retain their existing checkpoint/receipt/root/team/native evidence before
   teardown. Read the existing recovery records, requiring exact workspace,
   slug, root and advertised socket, automatic=true and ordinary ready creation.
   Missing, wrong-owner or disabled records stop; do not create/patch private
   state to satisfy the fixture. Record the proxy permission epoch. Preserve
   original evidence rather than overwriting it with post-restoration proof.
2. After teardown, bind the selected profile to the original package and the
   restored source listener; record current recovery status/epoch. Do not require
   the asynchronous worker to have left a particular held value: both an old
   proxy epoch and an already restored source epoch must be reported honestly.
   An unrelated third epoch or changed root/automatic setting is an error.
3. For each exact retained slug run once, in the registered fixture workspace,
   `package/bin/dev-session start SLUG --as-is --no-attach --json`, checking exit
   and returned slug/threadId. Supply no new goal, team/model/provider settings,
   exclusive/new flags or maintenance environment. Then run one ordinary
   `package/bin/dev-session sync SLUG --as-is`. This fixed sequence is deliberate:
   start publishes root permission at its end, after its first reconcile; sync
   then ensures a client even if the earlier held reconcile left a shell. It is
   not a conditional retry-until-green. Do not call the private `running` writer.
4. Before maintenance capture, require fresh recovery status held=false, existing
   automatic=true, exact root membership and the restored source epoch. Reading
   the existing `recovery --operation status` bridge and record is sufficient;
   no duplicated epoch algorithm or new helper framework is needed. Use the
   existing managed_client_state with original package-native identity to prove
   both actual managed clients, exact root/socket/pane and native executable.
   Recheck unchanged receipt/root/incarnation, saved team/provider/model/effort,
   exactly one original initial user message and no extra native thread identity
   using the existing proof assertions. Save post-restoration evidence separately.
5. Keep both roots in bootstrap's captured terminal intents; assert their exact
   identities instead of allowing the corrected setup to silently exclude them.
   After ordinary switch_done, require restoration.completed and actual target
   managed clients for both, with the same retained roots/panes and selected
   target native. Use the helper without its participant-specific operation
   option: these idle terminals legitimately have no participant. Check the
   operation's terminal intents separately. Retain all existing bootstrap,
   queue/goal/Stop/recovery cases and original message/ownership assertions.

Use the existing command/check budgets and bounded read-only client observer.
Any command, identity, permission or client proof failure stops with its small
before/after tuple. No sleeps, increased budgets, swallowed errors, synthetic
permissions, session exclusion, Stop override or proxy retained across activation.
This explicit start is permitted setup for these unstopped fixture roots only;
it is not a general policy to reactivate stopped sessions.

**Regression and checks.** The missed seam is composition: the creation cases
prove ready/initial-send/team identities behind the proxy, whereas maintenance
tests initialize recovery at the captured source generation. Neither existing
test checks permission after this proxy teardown. Add the real public-command
and postcondition assertions above inside the existing packaged fixture. They
deterministically require source-generation permission and actual clients before
capture, then destination clients after owned restoration; success cannot be
inferred from a reduced refusal count. Preserve the actual a57 CI as old failure,
but do not claim a deterministic reproduction of its unrecorded refusal branch.
No second VM solely to manufacture old-red evidence is needed.

Retain the existing deterministic real-store/socket controls:
TestMaintenanceTerminalSyncTransfersOwnedIdleRootPermission,
PreservesCurrentMemberAndOutcomeIdentity, RefusesForeignOrUnownedRecovery and
SuppressesStoppedOrDisabledRoot, plus TestRecoverySurvivesRuntimeLossWithoutExecutionPermission
and the Ruby fresh-status/admitted-held/generic-held/failed-tail controls. These
prove third-generation refusal, source-to-destination transfer, Stop/automatic=false,
exact owner and unchanged held behavior; do not replace them with canned success.
No additional Go/Ruby test scaffold is required for an unchanged production guard.
After allocation, run the existing Nix/test-script syntax quicks and a bounded
count=1 focused terminal-sync/recovery selector (60s Go batch guard), using the
repository environment. Reuse accepted unchanged Ruby controls by source/check
binding. Stop the first unexpected failure; do not expand into a stress campaign.
After combined committed source and affected review, the necessary long result is
one original successor packaged session-creation run through these real boundary
assertions, bootstrap and existing maintenance/recovery cases. Main allocates
publication/observation; no extra local driver or standalone diagnostic is proposed.

**Ownership, compatibility and acceptance.** This file is disjoint from B's
maintenance_pause_test.go, but B's current source/index/Git window remains exclusive.
Main allocates the fixture owner/window after the sufficient brief; no work is
stacked onto B here. Consolidate under the existing owning creation/maintenance
fixture history, retain a57/failure evidence and include both necessary corrections
in final affected/full-history review before publication. No native/SDK/input,
RPC/schema, journal, public preparation or product-doc change is needed. Preserve
profile token, worker/source owner, exact service/process/listener proofs, generation
fence, unknown submissions and responsible-thread children. Old journals remain
owned by their immutable source package; candidate installation cannot recover them.
Existing whole-VM/native/R/W-C/rollout obligations remain.

Settled: a narrow fixture preparation defect and ordinary public start-then-sync
correction with real source/destination client proof; production refusal remains.
Open: actual a57 response/record and final packaged result. Next observable result
is the one-file reviewed correction plus its explicit pre-bootstrap permission/
client proof, not a diagnostic campaign. Only design.md edited; no test/source/
Nix/CI/network/Git mutation/runtime/recovery/lifecycle action. Capacity returned;
session open. https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-03-lead-wakeup-delivery/.

## Exact13fb creation: bind the standalone observer's tmux executable

Sufficient one-file brief for e4e29d2a, 2026-11-07. Current/env/session verified;
live architect0 ready/design remains Astra/xhigh/workspace_write/full_access,
settings unchanged. Read leading plan/state/review and exact R AGENTS; reuse
unchanged full applicable guidance and accepted design6946. All source inspection
uses committed `13fbf63a229b1917829944d37eb0020ee9a735b0`, tree
`3f4d564e1f26c06787ba817c0631922256b28636`. No mutable C packet is inspected.

**Observed boundary.** Independently rehashed released
`/tmp/lead-wakeup-R-publication-13fb-wmpdxuq5/ci/creation-raw.stdout`:
`e60c36c509f7e3e1a7aaddd7b87720a18ab5ab901a4c70b2d2d3f09f84e45f72`,
1410107 bytes/7774 lines. Line6092 reports Python PermissionError/Errno13 executing
bare `tmux`; repeated failures end in the existing20s observer timeout6599.
Stack6064–6092/7699–7704 identifies the first before-root managed_client_state call,
before any successful tmux observation. This is an executable-launch failure,
not a failed client, root, permission or restoration assertion. Later bootstrap
and maintenance coverage is unproved. Missing browser-failure.json is secondary.
Fast/archive success and terminal original42385029613 are accepted only for their
scope. The raw log does not identify the searched PATH candidates or denied
filesystem component; no root-profile, mode, mount or permission cause is claimed.

**Source-supported environment mismatch.** session-creation.nix:193–196 and405–412
launch absolute Python directly as developer with XDG_RUNTIME_DIR; this bypasses
the application wrappers. test/creation_transport.py:109–113 uses
`subprocess.check_output(["tmux", "-S", ...])`, with no executable binding or env
override. Its only subprocess command is tmux; process observations use pathlib.
The fixture's systemPackages157–163 contains git/curl/node/chromium/python, not
tmux; the host module adds only its reconciliation program at596. The Python
environment declares websockets/pyyaml, not an external tmux executable.

By contrast, nix/workspace-portal.nix:477–502 explicitly prefixes tmux into the
runtime PATH for dev-session/workspace-host. These wrappers' successful earlier
calls do not supply PATH to a sibling Python process. flake.nix:23–57/120–122
passes the same pkgs to mkPackage and this test, so `pkgs.tmux` is the conventional
matching executable. The original and target packages already retain it through
their wrapper dependencies and the guest's additionalPaths. This establishes a
missing observer dependency binding without reconstructing the historical EACCES
search. The correction does not require another diagnostic run to choose a path.

**Only nix/tests/session-creation.nix, at managed_client_state.** Prepend the
existing shlex.join argv with absolute env and an observer-local PATH:

```python
command = shlex.join(["${pkgs.coreutils}/bin/env", "PATH=${pkgs.tmux}/bin",
    "${python}/bin/python", "${../../test/creation_transport.py}", "managed-client",
    runtime + "/tmux.sock", record["slug"], json.dumps(expected)])
```

Keep the existing user_prefix and wait_until_succeeds unchanged. The explicit
PATH is sufficient because Python is absolute and tmux is the helper's sole
external command. This gives every managed-client call the declared tmux without
depending on inherited login/root PATH entries. Add at most a short adjacent
rationale. Do not edit the helper API, application wrapper, node systemPackages,
service environment, user/permissions, inputs or export machinery.

Adding tmux globally to systemPackages is broader and leaves observer command
selection ambient. Passing a new helper executable argument would also bind it,
but unnecessarily changes two files and an interface. Guessing a root PATH entry,
chmod, changing users, wrapping a shell to read login setup, ignoring EACCES or
increasing20s are unsupported. No replacement observer, canned tmux output or
skipped client assertion is acceptable.

**Preservation and quick checks.** Keep original17 cases plus the source-permission
preflight, all actual tmux/proc/native observations and5s/20s bounds unchanged.
Keep before/after roots, proxy/source epoch proofs, fixed public start+sync,
receipt/incarnation/team/message identity, terminal intent matching, selected
target-client proof and old-client PID/startTime exclusion. Closed
R-pane-pid-41cc50af stays closed: do not reintroduce post-maintenance pane_pid
equality or alter the separately retained preflight tuple. No production permission,
Stop/automatic, authority or admission semantics change.

After main allocates one implementer, use the existing repository-Nix syntax and
embedded Python compile quicks plus scoped diff/AST inspection. Require the only
semantic delta to be this argv environment prefix; helper bytes, all cases and
assertions/budgets remain unchanged. Retain the rendered command evidence when
the normal packaged check produces it; do not add a separate driver evaluation.
The emitted EACCES remains historical red. Compilation is only syntax evidence;
the later real observer success is the behavioral regression proof. No fake PATH
framework, manufactured VM reproduction, separate tmux server or additional
native probe is needed. Reuse accepted unchanged Go/Ruby/B checks by exact source/
input binding rather than rerunning them for a fixture command prefix.

**Acceptance and ownership.** The implementer owns this one-file correction,
quicks and existing fixture-owner consolidation only when main allocates the
source/Git window. Preserve13fb and prior evidence/refs, full-history/single-SDK/
no-migration conclusions within their actual boundaries; obtain affected review
for the new command change through the normal main-owned process. No production
docs, persisted schema, compatibility, deployment ordering or recovery change is
needed. Saved operations retain immutable source ownership and remain untouched.

Necessary long acceptance remains the original reviewed successor packaged
session-creation through both proxy roots, source-permission preflight, bootstrap
and existing maintenance/recovery cases. Main allocates publication/observation;
no unmodified rerun, local preparation/driver loop or standalone target is proposed.
The first new real failure stops for its precise disposition; there is no automatic
repair/retry. Existing whole-VM/native/R/W-C/rollout obligations remain.

Settled: standalone observer lacks an explicit tmux dependency binding; one-call
process-local PATH correction preserves real observation. Open: exact historical
denied PATH component and successor runtime result, neither needed to select this
fix. Next observable deliverable is the narrow committed/reviewable fixture delta;
the next runtime result must actually execute tmux and satisfy existing observations.
Only design.md edited, no tests/Nix/CI/network/runtime/Git mutation or peer-output
inspection. Capacity returned; main owns allocation; session remains open.

## Exact36d6 creation: read restored rosters through the selected profile

Sufficient one-line fixture correction brief, 2026-11-07. Current/env match the
bound session/workspace; live architect0 ready/design remains Astra/xhigh,
workspace_write/full_access with unchanged settings. Read leading plan/state/
review; full applicable workspace guidance and R AGENTS are unchanged from their
full reads. Reuse design6946/7088. All repository reads use committed
`36d6e06a49cff668272d8dd895b0e47bc916ba5c`; no mutable head/index/source or C packet
inspection. Main owns implementation/review/publication allocation.

**Exact boundary and cause.** Released
`/tmp/lead-wakeup-R-publication-36d6-cc390rls/ci/creation-raw.stdout` independently
matches `b9320d0414ae8d5f94a48c3773d6233d1dfacac5a74746dd736b4e188fdbd2d7`,
1740703 bytes/8615 lines. Before/after cases and source-permission preflight finish
at6066/6462/6694. The explicit-tmux target-native before-root observation finishes
at7336. The following roster command7361 still invokes original
`/nix/store/rz1dzylgpgyvpvs4h2dpas9gbp396s6n-dev-workspace-0.2.0/bin/dev-session`;
7363 refuses its superseded generation. Stack8538–8545 identifies proof():333,
called by the target-restored identity proof at1050. This is farther successful
observation, not a completed bootstrap or proof of all restored terminals/later
cases. Preserve the separate historical tmux failure and other CI limitations.

The helper's global `package` is intentionally the immutable original installable
(187); it does not change when public switch selects maintenanceTarget.
workspace-host's public dev-session dispatch passes its own real package_root as
`--expected-host-generation` and captures the selected profile token (1535–1601,
3859–3861). dev-session then acquires the shared transition lock and requires the
selected profile realpath and token to match before executing team list
(9884–9912,10034–10047). Team list's read-only classification exempts provider
admission, not generation validation. Invoking the original wrapper after selecting
the target supplies a stale expected generation. The message alone does not
identify every failed conjunct, but source and the actual stale command establish
this fixture error; no production guard defect or race need be inferred.

**Change only nix/tests/session-creation.nix:333.** Replace `package` with the
existing `profile` in proof()'s public roster command:

```python
roster = json.loads(user("cd " + root + " && " + profile + "/bin/dev-session team list " + slug + " --as-is"))
```

The profile variable is assigned before any proof() call; initial installation
selects the original package before all creation/source proofs. After the completed
bootstrap switch it selects the target. Executing the profile entrypoint binds
the ordinary public wrapper to that selected generation, and its token/transition
checks still reject a concurrent replacement. Keep every roster/native/receipt/
incarnation/message assertion and the returned identity projection unchanged.
The target-restored equality must still compare the real current roster with the
saved original identity. No fallback to a stored roster or private reader.

**Complete bounded caller check.** Earlier proof calls, including both proxy
roots and source-restored proofs, use the selected original profile. Both
target-restored roots share the corrected helper. The remaining maintenance
cases already use profile for ordinary sync and both roster reads (585/591/715),
while host(), maintenance_status(), switch_start()/switch_done() and recover
also use profile. They alternate target/original through ordinary activation;
retain those bindings. recovery_proof(), explicit source start/sync and the
original settings calls execute only before the first switch. Original package
policy/catalog/native metadata and maintenance_packages are provenance inputs,
not stale dynamic commands; leave them unchanged. No further same-dependency
correction is supported by these callers.

A new package argument/call-site matrix would duplicate the existing selected-
profile seam. Reassigning global package would erase original-versus-target
provenance. Calling the internal Ruby/Go reader or exempting read-only commands
from generation checks would bypass supported ownership. None is justified.

**Verification and acceptance.** After main allocates, use the existing repository-
Nix parse, embedded Python compile and scoped diff/AST checks. Require exactly
this command receiver change: substituting profile back to package must reconstruct
the prior AST/bytes apart from any minimal rationale comment. Statically confirm
profile assignment and original installation precede all proof calls and that
both target-restored calls reach the same corrected helper. This is the meaningful
positive command-binding and negative unchanged-scope control; do not add a test
framework or manufacture a second historical VM failure.

Keep existing generation controls intact: lifecycle_commands_test.rb:115–147
refuses even read-only current after a transition; commands_and_locks_test.rb
checks wrapper generation/token propagation. Qualified accepted Go/Ruby/B and
helper checks are reused only with unchanged source/input binding; this fixture
token substitution does not justify replaying them. The released failure is old
red; syntax/static checks do not establish packaged green. After committed quicks
and affected review, main allocates the original successor packaged creation
through both target-restored roster proofs, bootstrap and remaining maintenance/
recovery cases. No unmodified rerun or local preparation/driver/probe campaign.
Stop at the first new failure with precise evidence, without automatic repair.

Preserve all18 cases, numeric budgets, explicit observer PATH, real tmux/proc/
native checks, source/proxy permission and fixed start+sync, Stop/automatic=false,
exact session/pane/token and PID/startTime exclusion, selected native identities,
full terminal restoration and stable continuation proofs. Closed pane-PID review
and accepted prior source corrections remain intact. The package has no production
API/schema/input/native, persisted ownership, deployment or recovery change;
old journals remain owned by their immutable source package. No product docs needed.

One implementer owns this file/quicks/ordinary fixture-owner consolidation only
after main allocation; preserve36d6/failure refs and existing history. Affected
review must assess the selected-generation binding and unchanged full identity
proofs, retaining full-history/single-SDK/no-migration conclusions within verified
boundaries. C's current evidence-only package is independent; no work stacked.

Settled: the source-pinned roster invocation is wrong after activation; use the
already-established selected-profile public command in one place. Open: complete
successor bootstrap/maintenance acceptance. Next deliverable is the narrow
committed/reviewable correction, followed only by main-allocated packaged proof.
Only design.md edited; no source/test/Nix/CI/network/Git/runtime action. Capacity
returned; session remains open and existing whole-VM/native/R/W-C/rollout scope
is unchanged.

## Exactddb creation: wait only for public sync admission

Sufficient fixture-only brief, 2026-11-07. Current/env/session and live saved
architect0 ready/design/Astra/xhigh/workspace_write/full_access verified; settings
retained. Read leading plan/state/review and R AGENTS; applicable full guidance is
unchanged. Use committed `ddb2968e3ac7bf2d0541538709bebc4e367cd6ac` only. This
amends design6946's single-process sync assumption, retaining its one ordinary
start, one admitted synchronization and all positive restoration proofs. Main
owns allocation; C's mutable evidence/index package remains excluded.

**Observed result.** Released
`/tmp/lead-wakeup-R-publication-ddb-n3do3gxj/ci/creation-raw.stdout` independently
matches SHA256 `a217c2bf01764d1d341502245a113f3717681065090d3c836fb9878ea73c8743`,
1475155 bytes/7784 lines. Before/after finish6089/6481. Preflight records the old
permission epoch with automatic=true/held=true at6523. The exact retained-root
public start returns successfully6530; immediate sync fails6533 with
`error: another dev-session command is changing 2026-11-07-before`, exit1.
Stack7709–7714 identifies the fixed sync, before fresh source permission/client
proof or bootstrap. This attempt does not inherit36d6's farther coverage. Neither
the lock holder nor its mode/duration is logged; no leaked child, automatic
recovery owner, harmless flake or product failure is established.

**Admission contract.** `sync(..., as_is: true)` validates the literal slug, then
enters with_slug_lock before manifest readiness, tmux synchronization and client
reconciliation (dev-session:1780–1787,3032–3034). with_host_lock attempts exclusive
nonblocking flock, raises this SessionBusyError before yielding and explicitly
unlocks/closes on exit (8271–8310,8457–8477). For ready ordinary sessions neither
wait nor wait_for_readers is requested. CLI maps this sync refusal to exit1;
only service busy uses75 (9916–9918). Do not retry arbitrary exit1 or borrow the
resume command's75 contract.

For this exact command/error, no sync body, repository/window update or native
client dispatch has occurred. Wrapper setup, identity reads and lock-file opening
can occur; this is not a claim of zero filesystem activity anywhere. The exact
unwrapped slug-specific error distinguishes refusal at the outer sync lock from
later command/reconciliation failures, whose errors must remain fatal.

start releases its slug scope before publishing `running` recovery permission,
then leaves the creation scope and returns JSON (1299,1337–1350). It does not
reserve the next command's lock or join independent portal tasks. Locks explicitly
unlock on scope exit, so successful start is not evidence of an inherited-lock
leak. A running terminal is managed by tmux, not a child whose exit start awaits.
Go runtime shared readers and exclusive writers use the same `<slug>.lock`
(session/authority.go:45–70). Portal automatic recovery can separately launch
ordinary resume (web/recovery.go:115–143,305–333); resume takes the same slug lock
and maps contention to temporary recovery (dev-session:1384–1433). These establish
possible legitimate competition, not the historical owner. Even a passive shared
reader can refuse this exclusive attempt despite the diagnostic's wording.

Existing real-lock tests in ordinary_readiness_test.rb:208–233 preserve exact
identity and prove no native operation on contention, then successful admission
after release. The product's fail-fast behavior is supported. The fixture's
assumption that start completion guarantees immediate uncontended sync is not.
No production change, lock bypass or private lifecycle waiting mode is justified.

**One file: nix/tests/session-creation.nix.** Add one small sync-specific admission
helper and use it at the two ordinary source-setup sync sites: proxy-root
preflight1008 and maintenance_case585. The latter has the same running-portal/
public-sync admission contract; no failure there is claimed. Preserve each
caller's selected command path (`package` while the original profile is positively
anchored; `profile` in alternating maintenance cases), cwd, exact slug and --as-is.
No general command-retry API and no modification of start, resume or recovery.

- Use the existing driver command execution and fixture polling convention.
  Capture status and complete command output, including stderr, without losing
  the exit status. Only `status == 1` and the exact single diagnostic line
  `error: another dev-session command is changing <this exact slug>` permit
  another admission attempt. Allow only the ordinary final newline; no substring
  matching, warning filtering, other-slug matching or empty-output acceptance.
- One monotonic20s admission deadline covers all attempts and their command
  durations. Pass only its remaining time to each driver execution; do not reset
  the deadline. Use the existing quarter-second polling cadence only after an
  exact refusal, capped by remaining time. This is bounded admission polling,
  not an initial/post-start settling sleep. The20s ceiling follows the fixture's
  existing client-observation scale; it is not a claim that every legitimate
  holder must release within20s. Exhaustion fails with attempts/last status/output.
  All existing product, command and observer numeric limits stay unchanged.
- Return on the first completed exit0 and never invoke sync again in that helper.
  Every other status/output, execution exception, signal or timeout is terminal
  and must stop immediately. A killed/timed-out/admitted-but-failed command has
  uncertain effects and is never retried. Do not wrap an unfiltered effectful
  command in wait_until_succeeds. Each retry is a new ordinary admission request;
  no lock descriptor or private token is acquired/inherited by the fixture.
- Keep one successful public start per proxy root and check its original JSON.
  Never repeat start, create a new prompt, change Automatic, seed permission or
  treat sync exit0 as the acceptance proof. Immediately retain the existing fresh
  permission/epoch, identity/message/roster and actual client assertions, then
  full target restoration and final-client checks. Held/suppressed/wrong-root or
  changed-generation results cannot be hidden by admission waiting.

Do not replace sync with resume (which restores authority while leaving execution
held), drop sync because a client happened to survive, poll a lock file then race
a separate command, or change sync to block globally. Do not stop portal recovery,
probe processes for an assumed owner or serialize the whole fixture. These either
change the contract, introduce a check/use race or exceed the observed boundary.

**Focused verification.** Keep the historical log as red; no manufactured VM
reproduction. In the existing quick-verification approach, extract the actual
small helper for a finite control using scripted driver responses and a controlled
clock, without a persistent harness or production seam: exact busy then success
must make two calls and stop; immediate success one; busy until deadline must
fail; another slug, extra output, generic exit1, status75, signal/timeout and
post-admission failure must stop on the first terminal result. Check decreasing
remaining timeout and no reset/restart invocation. This tests the newly introduced
classification/termination, not real production concurrency. Source inspection
and retained real-lock tests establish the no-admission boundary independently.

Run existing repository-Nix syntax, embedded Python compile and scoped semantic
checks once after implementation. Require only the helper/two sync-call changes;
preserve all18 cases/assertions, observer PATH/5s+20s, source/proxy permissions,
generation guard/profile roster correction, pane identity and old-client
PID/startTime exclusion. Reuse qualified unchanged Go/Ruby/B/transport controls
by source/input binding; no broad replay or new timeout campaign. First unexpected
quick failure returns for precise disposition. After owning-fixture consolidation
and affected review, main allocates one original successor packaged creation
through real admission, source client preflight, bootstrap and maintenance/recovery.
No extra local driver/preparation or unmodified CI retry is proposed.

**Compatibility and acceptance.** No product API/schema/native/input/permission/
Stop/generation behavior changes. Lock ordering and original unknown-submission
semantics stay intact. Queues/goals/conversations and responsible-thread child
ownership remain; no saved operation is recovered. Preserve old failures/refs and
immutable journal source owners. Independent affected review must inspect exact
non-admission classification, finite deadline and fatal treatment of unknown
effects, plus normal full-history/single-SDK/no-migration conclusions. No product
docs are required for this fixture-only admission correction.

Settled: legitimate contention is possible after start; this exact sync rejection
precedes its effects, allowing bounded admission attempts until one successful
synchronization. Open: historical owner/duration and complete successor packaged
acceptance. Next deliverable is the narrow helper with meaningful control results,
not lock-owner diagnostics. Only design.md edited; no checks/Nix/CI/network/Git/
runtime action or mutable peer inspection. Capacity returned; main owns allocation;
session stays open and remaining whole-VM/native/R/W-C/rollout scope is unchanged.

## Exact7bf amendment: integer driver timeout within the admission ceiling

Sufficient one-file correction brief, 2026-11-07; amends design7303 only. Current,
environment and fresh same-session roster verified; architect0 retains
Astra/xhigh/workspace_write/full_access. Main owns implementation allocation.

**Settled contract.** Committed `7bf46df803d19870be1c22b8fcbb544c30169162`,
`nix/tests/session-creation.nix:198–228`, passes floating `remaining` to
`machine.execute`. Released `/tmp/lead-wakeup-R-publication-7bf-vzy_r2nw/ci/creation-raw.stdout`
matches SHA256 `9ccd36b3cc71c37d5f577c8fcaf8fa8a1e8a5e11da7f7f24ee411c5a62c15a09`.
Lines3437–3457 reject that argument before VM startup; no admission/restoration
coverage transfers. The actual cached `gxf3q4fva317n39j307wc4dhwg4ryqma-nixos-test-driver-1.1`
package declares `BaseMachine.execute(timeout: int | None = 900)` in
`test_driver/machine/__init__.py:583–636`. QemuMachine._execute:871–910 sends
`timeout {timeout} bash -c ...` when non-None, then reads output/status. GNU
coreutils9.11's retained timeout documentation explicitly says duration0 disables
the timer; None omits it. Neither is an exhausted-budget representation.

**Smallest implementation.** Only change sync_source in
`nix/tests/session-creation.nix`: immediately after computing remaining from the
existing absolute deadline, compute `timeout_seconds = int(remaining)`; fail
before incrementing attempts or dispatching when `timeout_seconds < 1`; pass
`timeout=timeout_seconds`. For positive remainders this rounds down. Keep the
original floating deadline, post-execution deadline check, complete exact
same-slug refusal classification and bounded quarter-second polling unchanged.
The integer is the driver argument, not a replacement/reset of the deadline.
Add a short comment explaining integer API/zero semantics, not a retry framework.

This deliberately declines a new command with less than one second left and
shortens any command allowance by less than one second. It may fail earlier;
it never grants more than the sampled remaining20s budget. Exactly1s permits
timeout1; a smaller positive remainder permits no command. No ceiling/rounding
up, max(1), default/None/zero, type cast/ignore, checker disable or driver edit.
Command durations still consume the one monotonic deadline; a late successful
return remains failure. This preserves the fixture's configured ceiling, not a
new hard-real-time guarantee over driver callbacks/transport, scheduler delays
or guest signal handling. Any execution timeout/status124/exception or other
unknown-effect outcome remains terminal, never another admission attempt.

**Necessary quick gate, before review/push.** Prior Python compilation and
scripted controls did not exercise the packaged type boundary. The inspected
cached nixpkgs `nixos/lib/testing/driver.nix:77–88` constructs testScriptWithTypes
from test-script-prepend.py, machine declarations and the script, then runs
`ty check testScriptWithTypes`. Use that checker, with the locked Python3.13
driver environment and real CI-named gxf module visible, for the focused check.
Do not build a driver/VM to obtain this result. A minimal affected file can contain
the **exact extracted sync_source**, its existing time/shlex imports and string
globals, and `from test_driver.machine import QemuMachine` with
`machine: QemuMachine`; this exercises the actual inherited execute signature.
No fake execute annotation, Any substitute, suppressed/unresolved imports or
untyped mock can stand in for the driver. Use the normal pinned Nix checker
environment when main allocates checks; the inspected ty0.0.38 derivation exists,
but its executable is not currently cached, so no local checker pass is claimed.
Run `ty check testScriptWithTypes` once for the original helper and once for the
successor in the same isolated check context: require old invalid-argument-type
at timeout/int|None and new exit0. Record tool/module paths and extraction source;
this is focused interface evidence, not full packaged-script/guest acceptance.

Adjust the existing finite extracted-helper controls, without a new persistent
harness: require every dispatched timeout to be a positive int no greater than
remaining; cover fractional>1 (e.g.1.9→1), exactly1, positive<1, zero and negative
remainders. Subsecond/exhausted cases must dispatch nothing. Retain busy→success,
elapsed command time reducing the next allowance, late success refusal and
terminal timeout/unknown effects; keep the strict status/output and caller
package/profile/cwd/slug/--as-is controls. One adjusted focused batch suffices.
Run changed-file Nix syntax/embedded Python checks once; reuse unchanged qualified
Go/Ruby/B/transport evidence. Do not repeat preparation or historical inventories.

**Release and limits.** One implementer owns this fixture and its quick controls,
then owning-history consolidation and affected independent review. No production,
API/schema/native/input/budget/recovery contract or product-doc change. Preserve
one start, one admitted sync, all18 cases and every source/proxy permission,
Stop/identity/client/roster/generation proof. No old journal recovery. Next required
long acceptance is main-allocated original reviewed successor packaged creation,
including its real static gate and preflight/bootstrap/maintenance; no diagnostic
VM or extra local preparation loop. No historical lock-owner conclusion changes.

Only design.md amended; no checks/Nix/CI/network/runtime or application mutations
performed. Brief complete, capacity returned; main owns the next allocation and
the session remains open.

## Exact7bf fast check: separate native cap from integrated submission uncertainty

Sufficient test-only amendment to design6798, 2026-11-07. Current/env and fresh
same-session roster match; architect0 retains Astra/xhigh/workspace_write and
full_access, with prior capacity returned. Applicable full guidance is unchanged.
Only committed `7bf46df803d19870be1c22b8fcbb544c30169162` and released evidence
were inspected. This package is disjoint from C's integer-timeout fixture change;
main allocates B and serializes R Git windows behind C.

**Finding and boundary.** Released fast-raw.stdout under
`/tmp/lead-wakeup-R-publication-7bf-vzy_r2nw/ci` matches SHA256
`ab6d5aec5910a540a0c491aaa06de2ff057df40604122d0d968bed7c61afd282`.
2737–2741 show selected steer0, private WebSocket handshake DeadlineExceeded,
prepared ledger/refused notice and live parent. This is known-unsent setup failure,
not lost post-submission uncertainty; historicala57 phase/host cause stay unknown.
Independent source inspection confirms pauseNative:134–172 starts its cap before
the callback, and pausePass:290–339 uses separate ActiveTurnID and ConditionalSteer
calls. Pinned c3c2 conditional_steer.go:61–95 creates a fresh private connection,
checks metadata/activity, then claims the real submission immediately before write.
The existing outer-client warmup cannot move that private setup outside its cap.
No production timing or server-serialization defect is demonstrated.

**One source file: portal/cmd/workspace-portal/maintenance_pause_test.go.** Split
the current four-method test's obligations; do not merely raise its500ms limit.
Keep production/SDK/defaults and every unrelated numeric test limit unchanged.

1. Keep TestMaintenancePauseSilentNativeOperationsAreBounded as a direct native
   cap test. For each of its four methods, create the real fixture/client and
   complete ActiveTurnID initialization with the existing3s setup guard, requiring
   the captured turn. Only then arm the selected-method silence/counters. Invoke
   actual pauseNative with that same real client's Request and ordinary valid
   method parameters. Retain500ms call cap,700ms recovery setting,1s future grace
   (past grace for interrupt) and2s caller, established after setup. Persist that
   grace once as in the current test. Pass allowance=grace+700ms for future grace;
   for expired interrupt grace use now+700ms, matching pause's existing expired-
   recovery rule, so the intended native request is admitted. The callback
   must observe the exact selected request; a missing request fails, never skips
   or retries. Check DeadlineExceeded, the applicable pause-native-timeout or
   pause-interrupt-timeout, live caller and cancelled derived context. Preserve
   saved deadline, phase/nonactivation, Stop and continuation identity checks.
   One raw steer in this test proves bounded on-wire Request only: it deliberately
   supplies no ConditionalSteer ledger claim. Other rows issue no steer; all rows
   forbid turn/start and thread/resume. Count only the armed phase, not warmup.

2. Add TestMaintenancePauseConditionalSteerAmbiguityKeepsLedger for the real
   m.pause→ConditionalSteer→submission-database→saved-operation path. Use ordinary
   product limits (no500ms override), the existing3s integration guard and the
   fixture's ordinary prepared90s grace. Persist that grace deadline once before
   dispatch and compare it afterwards; do not reset it or seed any submission.
   At the endpoint's first actual turn/steer, capture its params/count and return
   an ordinary JSON-RPC error such as code -32000 with a fixed fixture message,
   rather than a success receipt or silence. Continue serving the existing empty
   history for reconciliation. No sleep, retry-until-reached or second pause call.
   The request's arrival occurs after the SDK's genuine submitting claim. SDK
   conditional_steer.go:99–129 only restores a known-unsent claim for unwritten
   writes or -32600/-32601/-32602; this different error plus absent receipt retains
   UnknownSendOutcomeError/submitting. Absence of a receipt is not acceptance.
   Require that exact injected response was written successfully, one steer,
   no start/resume, live actual m.pause caller, non-paused result, typed unknown
   (not MessageNotSentError) and notice-outcome-unknown classification. A setup
   timeout must fail this test, not satisfy it. Export the real ledger normally.

For the second test, minimally extend the existing optional reply callback's
arguments to include its connection and decoded request; keep its true=normal
reply/false=already handled or silent convention. Existing callbacks extract the
same method and retain behavior. The new callback writes through existing
threadCommandWriteObject, retains any write error for the test goroutine, and
returns false. No new fixture framework, shared main_test.go change, SDK injection
or public API. This permits a deterministic post-dispatch failure without
cancelling the actual parent or changing the logical call's deadline midway.

**Explicit coverage allocation.** The original combined assertion is not a
supported guarantee that cold private setup reaches a selected RPC within500ms.
Its useful contracts remain as follows:

| Contract/assertion | Required proof |
| --- | --- |
| Exact method reached, bounded silent call, DeadlineExceeded, live2s caller | Initialized real connection + actual pauseNative in each four-method row |
| Actual500ms deadline and derived cancellation, earliest caller/grace/allowance | Existing NativePauseCapDerivesBoundedDeadline and caller/shared/grace controls, plus direct-call context |
| One genuine ConditionalSteer, no start/resume | New real m.pause test, exact endpoint params and counters |
| Unknown disposition/reason and genuine submitting ledger | New integrated test; original Root/NoticeID, Cwd/SourceTurn/NoticeAction context, one entry, exact text/turn/message ID on wire |
| Saved deadline, StopRevision, continuation identity/disposition, no cutover/source-stop/activation or paused result | Retain checked Load and full prior comparisons in the integrated test; direct cap rows cannot advance state either |
| Unknown after caller cancellation, grace expiry and bounded cleanup | Existing UnknownSteerIsSavedAfterCallerExpiresAndCleanupIsBounded and GraceExpiryRetainsUnknownSteerForRecovery remain unchanged |

Move the current genuine ledger/participant assertion block to the integrated
test; do not replace it with prewritten state or claim raw Request tests cover it.
The integrated error is deliberately not DeadlineExceeded: deadline cancellation
is proved separately, while its actual caller stays live and pause saves unknown.
The3s integration guard bounds setup/bookkeeping; it is not a new native-call
promise. Extreme scheduling can still fail a positive-arrival precondition.
No test-only arrangement can guarantee progress under arbitrary starvation.

**Finite checks and release.** Keep exact7bf's log as historical red; do not
manufacture its handshake timing. Run gofmt and one anchored `go test
-mod=readonly ./cmd/workspace-portal -count=1 -timeout=60s -run '^(...)$'` batch
in the repository environment. Select the two changed/new tests above plus
NativePauseCapDerivesBoundedDeadline, CallerDeadlineWinsNativePauseCap,
SharedAllowanceDoesNotRenewAcrossCalls, ExpiredRecoveryHasOneSharedAllowance,
GraceBoundaryRetriesPassiveReadInInterruptPass, GraceExpiryRetainsUnknownSteerForRecovery,
PersistedCancelAndCallerCancellationBoundOutstandingRead,
UnknownSteerIsSavedAfterCallerExpiresAndCleanupIsBounded and
CooperativePauseUsesOrdinarySteer (all with TestMaintenance prefix). Existing
cap-bypass negative evidence is reusable only with unchanged production cap and
unchanged direct deadline assertion; no new mutation/stress campaign. Preserve
qualified unchanged Stop/resume/history/SDK checks. First unexpected check failure
returns its precise phase; no cap inflation or optional sibling repair.

Next deliverable is B's one-file source/control result after main allocation,
then one combined affected review/publication with C's typed-timeout correction
and original successor packaged acceptance. Retain owning-history/single-SDK/
no-migration conclusions. No deployment, journal/recovery, API/schema, user grace,
Stop/queue/goal/conversation or responsible-thread-child contract changes; no
product documentation update is needed. No extra VM/preparation/SDK audit.
Only design.md appended; no tests/Nix/CI/runtime/application or Git mutations.
Brief complete and capacity returned; session stays open.

## Exacta654 fast check: cleanup timeout evidence instead of aggregate stopwatches

Sufficient bounded amendment, 2026-11-07; current/env/fresh roster verified,
architect0 Astra/xhigh/workspace_write/full_access retained. Full applicable
guidance unchanged; read accepted combined review and immutable a6542ced source.
Main allocates implementation; implementer2's CI observer/mutable packet is excluded.

**Exact failure and limits.** Released `/tmp/lead-wakeup-R-publication-a654-bc_q2emf/ci/fast-raw.stdout`
rehashes to `42974211fb12ec2692d8b9f350d9954ae9ad7ee3220fc2aafeb8e924d070ab56`.
1895–1896 identify maintenance_pause_test.go:658. Since printed err=nil and
Status=recovery-required satisfy the other conjuncts, the failed conjunct is
`time.Since(start) > time.Second`. The printed1.26s covers the whole subtest;
the log does not give the isolated cleanup duration or its phase timings.
The test previously observed an actual steer, explicitly cancelled its caller,
received context.Canceled, loaded unknown NoticeDisposition and completed
Controller.Cancel. Despite its name, this path exercises explicit cancellation
after dispatch, not a proved automatic expiry of the one-second parent.
Post-cleanup state assertions were not reached; do not infer their success.

**Source contract.** cancelNotices (maintenance_notice_cleanup.go:98–151) derives
one650ms shared attempt and a500ms per-participant context using this fixture's
unchanged pauseLimits. notice-cleanup-timeout means either attempt.Err before a
participant, or retireNotice returned an error with bounded.Err nonnil. The log
does not select between them, or prove the history RPC was reached. retireNotice
first saves retirement intent, exports the real ledger, then reconciles under the
bounded context. On unresolved reconciliation it saves unknown using resultCtx;
cancelNotices saves its final summary after that. These saves each use the separate
pauseCallTimeout context in savePauseResult (maintenance_pause.go:177–185), with
the original result context, not the expired native context. SDK submission
storage also has its existing independent local transaction bounds. Thus a whole
cleanup stopwatch includes setup, storage, native waiting, Close, result saving
and scheduling;1s is not its native/shared deadline contract. This explains the
unsupported oracle, not which activity consumed historical time. Product budgets
and documented bounded requests/result-saving remain supported; no production
correction or SDK/host/scheduler diagnosis follows.

The exact test differs from7bf only in callback plumbing; this stopwatch and
cleanup/pause production bytes were unchanged. The bounded sibling scan finds
one other elapsed verdict, ExpiredRecoveryHasOneSharedAllowance:679–682: complete
m.pause is required below500ms although its40ms shared recovery allowance starts
inside pause and the stopwatch includes identity/setup/Close/return scheduling.
No failure there is claimed. Other Since calls are diagnostics; existing
time.After/context gates are explicit arrival/completion guards, not this same
numeric total-versus-inner-deadline assertion. No wider audit is needed.

**One file: portal/cmd/workspace-portal/maintenance_pause_test.go.** Change only
these two tests and any small local assertion code needed within them.

- UnknownSteerIsSavedAfterCallerExpiresAndCleanupIsBounded: preserve the actual
  endpoint-arrival→cancel→done sequence and500ms/650ms limits. Check Load errors,
  retain exactly one real steer with original wire identities, no start/resume,
  typed UnknownSendOutcomeError (never MessageNotSentError) and context.Canceled.
  Export the actual submitting ledger before cleanup and again afterwards;
  require one original Root/NoticeID entry with Steered=true, exact text digest
  and `conditional-steer:v1:[Cwd,SourceTurn,NoticeAction]`. Reuse the adjacent
  integrated test's assertion shape, not preseeded rows or raw Request.
- Replace only cleanup's elapsed1s verdict with explicit nil error,
  recovery-required/notice-cleanup-timeout and a live cleanup caller. Use a fresh
 3s context for this cleanup invocation (the existing integration-guard scale),
  defer cancel and inspect Err before cancelling. This is an outer failure guard,
  not a new product limit or an enlarged native cap: inner500ms/650ms still must
  expire before the guard. Keep elapsed and observed cleanup-method count as
  diagnostics. Reconciliation need not reach a particular on-wire method to
  exhaust a complete logical cleanup budget; do not impose cold-setup progress
  or mistake that branch for an on-wire silence proof. The existing initialized
  native-cap controls retain that separate proof.
- Always gather post-cleanup evidence before reporting a combined failure:
  checked Load/export, CancelRequested=true, NoticeCleanupComplete=false,
  unknown original notice, neither retired nor cleanup-accepted, unresolved
  blocker, unchanged saved PauseDeadline, StopRevision, continuation identity/
  disposition, root/cwd/turn/action and phase/cutover/source-stop/activation.
  Retirement intent may have been saved; it does not prove acceptance. Preserve
  exact source ownership and no new sends. Do not require retirement intent when
  the shared allowance expired before the first participant was admitted.
- ExpiredRecoveryHasOneSharedAllowance: retain1s call/40ms shared allowance,
  past saved grace and existing1s caller. Replace the aggregate500ms verdict
  with nonnil pause-interrupt-timeout, live caller, non-paused result and checked
  unchanged saved deadline/prepared notice/Stop/continuation/nonactivation.
  Expiry before native admission is valid; do not require a request to beat40ms.
  SharedAllowanceDoesNotRenewAcrossCalls retains the exact equal-deadline and
  expired-before-callback oracle. Keep elapsed only as diagnostic information.

**Fastest faithful verification, before another packaged run.** After main's
allocation, gofmt and one anchored repository-environment batch from portal:
`GOWORK=off go test -mod=readonly ./cmd/workspace-portal -count=1 -timeout=60s`
with `-run '^(TestMaintenanceUnknownSteerIsSavedAfterCallerExpiresAndCleanupIsBounded|TestMaintenanceExpiredRecoveryHasOneSharedAllowance|TestMaintenanceSharedAllowanceDoesNotRenewAcrossCalls|TestMaintenanceNativePauseCapDerivesBoundedDeadline|TestMaintenancePauseConditionalSteerAmbiguityKeepsLedger|TestCancellationDoesNotErasePreparedJournalSubmittingLedgerRaceOrUnknown)$'`.
Expect low single-digit test-runtime seconds plus existing compile/startup cost;
retain a60s ceiling and first unexpected failure as the stopping boundary. No
stress repetitions or full Go/Nix/VM campaign. Historical42974211 is the old-red
for the unsupported stopwatch; do not manufacture its scheduling.

One finite negative control is necessary because the old pauseNative cap-bypass
does not exercise cancelNotices' independent contexts. In an isolated uncommitted
test copy only, make both cancelNotices native limits exceed the3s caller guard
(e.g. multiply its recovery and per-participant call timeout arguments by10;
leave production pauseLimits/savePauseResult and all other bytes intact). Run
only the changed cleanup test once/count1/60s. Require actual original steer and
cleanup entry/history observation, then failure specifically because cleanup's
caller expired, even if response still says notice-cleanup-timeout. Missing
dispatch, unrelated failures or the overall60s watchdog are not accepted red.
This proves the new semantic verdict rejects cleanup bounded only by its caller;
it is not a measurement of an exact500ms elapsed interval. No mutated source is
committed or packaged. Expected additional runtime about3s plus bookkeeping;
return any different failure without expanding diagnostics. Reuse unchanged
source-bound cap/caller/Stop/generation/typed-driver controls.

**Release/compatibility.** No production, SDK/input, persisted format, product
grace, recovery/Stop, queue/goal/conversation, ownership or deployment behavior
changes; no product docs needed. Main accepts the targeted source/control result,
then owning consolidation/affected review and original successor packaged
acceptance. Current creation/archive observation continues independently and
cannot supply a successor fast pass. No extra local driver/preparation or blind
rerun. Remaining uncertainty is historical phase timing and eventual packaged
acceptance; no missing fact prevents this narrow oracle correction. Only design.md
appended, no checks/runtime/source or Git mutations. Capacity returned; session open.

## Exacta654 creation: distinguish the completed predecessor while awaiting admission

Sufficient fixture-only brief, 2026-11-07. Current/env/fresh roster and retained
architect0 Astra/xhigh/workspace_write/full_access verified; capacity available,
settings unchanged. Read current records/R guidance; full applicable procedures
unchanged. The reviewed55db Go correction and W guidance are outside this package.

**Observed sequence.** Released `/tmp/lead-wakeup-R-publication-a654-bc_q2emf/ci/creation-raw.stdout`
matches SHA256 `d85d13118752ae7cccc9c96c8cfdfb6fa5372d7dcdfaec1336837298ca4abbf4`.
Exacta654 bootstrap finished7526 after both target client/roster proofs; this is
meaningful actual progress. Cooperative starts7527. Its switch_start reads
unqualified status7650–53, prepares original package jnd1l5…7669, and launches
one `systemd-run --user --unit=creation-maintenance-cooperative --property=Type=exec`
stable-profile workspace-host switch with pause30 at7702–08. First subsequent
unqualified status7709–12 yields operation9ba315d4-15fd-4d76-b835-82ebcad4422c,
revision23/complete. That exact UUID is already bound to bootstrap completion,
worker-exit and evidence commands7333–7368, with source jnd1l5…→candidate hgl28…,
pause2. Cooperative is the opposite package direction with pause30.

**Demonstrated mechanism.** Committed session-creation.nix:530–531 asks for a
nonempty operation with a different UUID. Since that predicate was false, the
printed operation is necessarily the captured previous UUID. maintenance_wait:
475–485 then raises solely because its phase is complete, applying a terminal
guard intended for the awaited operation to the known predecessor. The failure
occurs before new-operation provenance assertions or cooperative completion.

Ruby workspace-maintenance.rb:48–61 maps status without ID to active; Go
maintenance_control.go:368–373 returns Store.Active's record, including terminal
records. Store.Create publishes the next active pointer only after writing the
new operation (store.go:294–330). workspace-host:624–627 performs prepare_profile
again before start_maintenance_switch publishes that operation. Type=exec launch
success therefore does not mean a new operation has already been admitted.
The old completed record is valid during this interval. No product defect,
new cooperative UUID/outcome, exact delayed step or scheduling cause is proved.
The preview prepare UUID is not the later switch UUID: do not bind polling to it.

**One file: nix/tests/session-creation.nix.** Add one optional predecessor UUID
argument to maintenance_wait, default absent, and use it only from switch_start.
Before launching, switch_start captures previous and requires it to be absent or
complete, matching these sequential cases' switch_done contract. Pass only that
captured UUID. In the wait loop, a record with that exact UUID and phase complete
is pending admission: skip both success predicate and terminal guard for that
record, then use the existing quarter-second polling path. If that same UUID is
no longer complete, fail; never suppress another operation or recovery failure.
No new loop, deadline reset, arbitrary sleep or repeated prepare/switch launch.

For a new UUID preserve normal predicate/terminal behavior. At the new-admission
call, exclude cancelled/recovery-required from the success predicate so those
records reach the existing fatal guard immediately. A genuinely new complete
record may satisfy admission only after all normal source/candidate/preparation
checks; completion is still proved by switch_done, never inferred from admission.
Retain current sourceIdentity/source/sourcePackage/candidatePackage/pauseTimeout
and switchOperationId==operationId checks and the selected profile/native bindings.
Do not compare the separate preview's switchOperationId with the actual new ID.
No broad exception for arbitrary terminal records, suppressed CLI/JSON errors or
private pointer writes. Keep300s monotonic wait,0.25s cadence and10s status-command
limit. If no new record appears, fail at the existing deadline with the last
observation; launch acceptance alone never counts as successful maintenance.

Same-helper scope is finite: bootstrap and all maintenance_case switch_start
calls use the new predecessor handling. Identity-bound switch_done, public Stop,
pause-notice acceptance, expected startup failure, same-operation recovery and
target barrier keep the default handling and existing recovering=True exceptions.
Predicate-first success for an explicitly awaited complete/recovery-required
phase remains valid; no global terminal-guard reordering. Preserve every current
case, target/client/source permission proof, restoration/continuation/Stop,
queue/goal and final command/worker exit assertion.

**Focused check before publication.** Extract the actual maintenance_wait and
switch_start helpers into the existing temporary Python control approach. Script
maintenance_status/host/user/package_native_identity and a controlled monotonic
clock; never execute a VM or rewrite the helper under test. One finite batch:
old complete→old complete→new prepared must fail with originala654 and pass with
the successor, with exactly one prepare/launch and unchanged command arguments.
Also cover no predecessor→none→new, permanent predecessor→300s exhaustion,
changed predecessor phase, new cancelled/recovery-required, wrong new package/
sourceIdentity/pause/operation relation, and CLI/JSON failure. Include new complete
with valid provenance as admission only, plus named completion, unexpected named
terminal and recovering=True same-ID caller controls. No arbitrary terminal can
be accepted just because its UUID differs. These controls exercise all relevant
caller modes, not the application lifecycle itself.

Run changed-file Nix syntax, embedded Python compilation and the existing pinned
ty/actual-driver static-check method over changed helper/caller definitions;
reuse unchanged sync_source34 controls and reviewed Go results by source binding.
Expected helper runtime is subsecond, quick batch seconds with cached tools;
one60s batch ceiling, first unexpected failure stops expansion. Retain one compact
old-red/new-green result and exact source/diff, not historical artifact inventories.
No new framework, full suite, local driver/preparation or manufactured VM red.

**Release.** Main allocates one implementer, owning fixture consolidation and
affected review, combining this independent correction with accepted55db before
the next publication/original successor packaged acceptance. No production/API/
schema/input/native/budget/recovery/deployment change or product-doc update.
Exacta654 bootstrap passed; cooperative/deadline/Stop/recovery acceptance remains
due and does not transfer to the successor. Only design.md appended; no checks,
Nix/CI/network/runtime/application/Git mutation or mutable packet inspection.
Brief complete, capacity returned; main owns allocation and session stays open.

## Exact7b3b deadline setup: request observation gap, no selected cause fix

Bounded source disposition, 2026-11-07, package88b8b269. Current/env/fresh
same-session roster and retained architect0 Astra/xhigh/workspace_write/full_access
were verified; settings unchanged. Only immutable7b3b7734 source and released raw
`/tmp/lead-wakeup-R-publication-7b3b-tw8b8wow/ci/creation-raw.stdout` were used for
the failure diagnosis (SHA256
`425a3a5c94f456ac7c529a54409f212ef947509bb2bf29df4a2e362fbf6537a5`,
2579972bytes/11048lines). Current records/guidance read; peer mutable evidence,
source/index and runtime were excluded.

**Settled failure boundary.** Final trace10970–10978 binds top-level deadline-stop
to maintenance_case:645 and held_model_request:263–272 in
`nix/tests/session-creation.nix`. This is root Responses-request setup, before
the member-request assertion, queue/goal creation, switch_start or public Stop.
It is not the maintenance pause deadline. Root is
`01a1b791-687b-7971-bd85-329111615649`, slug2026-11-07-accepted-session;
marker is `CREATION_MAINTENANCE_deadline-stop_325a43bb-e788-44ec-872e-8aa46774c6e1`.
The single public root POST with client ID1176e91a-181f-423f-b981-d4fb635511bb
completed8205–08 in0.48s; assignment to reviewer0 with message ID
c54168c6-5587-4068-8ac3-e390bed43a7f completed8209–12 in0.41s. Fixture parsing
and access to receipt["turnId"] succeeded, but its value/steered flag were not
printed. The command success is not an observed fresh-turn receipt.

The900s driver wait began8213 at20:07:03.2098576. Each printed lookup found zero
rows satisfying all of: index>0, model exactlygpt-5.5, role=user,
content.type=input_text, and an entire text part equal to the marker (both
marker/text arguments are identical here). Thus a stale after-index cannot
exclude a positive request index; no observed count>1 exists. Zero does not
distinguish absence from wrong model/role/part representation or missing marker.
Finally removed hold-turn9709–12, then fatal9713 at20:22:10.6807906 reported
903.91s. No retry or later Stop/maintenance acceptance occurred.

**Production/fixture contract.** R server.go:1943–1960/2046–52 routes the legacy
message URL to the pinned c3c2 conversation handler. Its handler.go:568–632
validates the message/UUID, calls Client.Send, and returns202 plus the accepted
receipt; it does not await an external Responses request. SDK client.go:
5363–5501 resumes/observes the exact thread, chooses turn/start when idle or
turn/steer with expectedTurnId when active, and reports Steered in the receipt.
No fresh-model-request guarantee follows from an accepted steer. The fixture's
own prefix case:833–865 explicitly advances one known held response after each
accepted steer before demanding the next model request.

`test/creation_model.py`:21–28/74–77/114–116 logs the complete request before
waiting under global hold-turn; a permit releases only its known request index.
maintenance_case touches that global hold before Send and unconditionally waits
for the new marker. It does not establish an idle/fresh-turn precondition or
advance a preceding held response. The preceding cooperative case proves resume
input and retained queue/active goal plus completed recovery, not that all
continuation/queue/goal inference has finished. Therefore a valid active-turn
submission can reach a circular fixture wait: existing response held, steer
accepted, new marker not sent to the model until the held response advances.
This is a source-supported possible composition defect, NOT an established
historical receipt/blocked-request identity or sole cause of this failure.

**Evidence limit.** Neither the submission receipt, pre/post-submission root
turn state, nor relevant Responses bodies are printed. The post-failure JSON
files contain earlier creation observations; the model summary prints naming
requests only. Portal automatic-retry-unavailable messages are not correlated
send receipts and do not settle admission. Errno28 is first printed10914 at
20:25:28 during export, followed10939/10964; its stack is the model log write.
It follows timeout/hold removal and cannot establish earlier disk exhaustion or
explain the earlier zero matches. No capacity/cleanup/storage correction follows.
Exact7b3b fast/archive, bootstrap and cooperative successes remain meaningful
within their recorded scope; deadline/Stop/final recovery remain unproved.

**Next decision requires one bounded discriminator, not a production patch.**
The narrow unknown is whether the accepted marker was steered behind an already
held request, or was dispatched with a representation the selector rejects (or
failed to reach/log a request for another reason). Historical bytes cannot be
recovered from this raw log. Do not modify Send, Automatic, Stop, native/SDK/input,
model/filter identities, queue/goal state, or deadlines on this evidence.

Before another packaged run, main may allocate ONE disposable real-interface
control using the selected existing0.165 native, pinned c3c2 Client.Send and the
actual creation_model handler/held_model_request selector, with isolated state.
Reuse the existing SDK native integration harness pattern and fixture's known
per-index release protocol, without modifying the SDK or adding a framework.
Start one root turn, observe its exact request index under hold, then send the
new unique marker once through real Send. Record the same-root/turn/client-ID
receipt, native user item, request bodies and every selector conjunct. If the
receipt is steered and marker absent while that known response is held, release
that one index once and require exactly one subsequent matching request on the
same turn and exactly one marker user item. Keep the successor response held
until evidence is captured. An initial idle send is the positive selector
control; wrong model/role/text, old index and duplicate rows must still fail
the extracted actual predicate. Never repeat submission to obtain the result.

This finite control tests the demonstrated source seam, not a reenactment of
the historical scheduler/cooperative run. A mock Send or invented request body
alone cannot establish native steering behavior. One invocation,60s total
runtime ceiling, expected seconds with existing native/tools; first mismatch,
timeout, unavailable pinned input or unexpected side effect ends the package.
No build/acquisition, VM, profile switch, full suite or second control campaign.
Main separately owns allocation and any required monitor. A confirming result
would justify a narrowly designed fixture gate that admits the new marker to
the external boundary before holding it; it does not yet authorize that change
or an arbitrary release of unbound existing requests. Contrary evidence returns
the captured receipt/body/native projection, not a guessed correction.

For eventual fixture work, keep diagnostics in session-creation.nix at this
boundary: print the original receipt and exact root/turn/client-ID projection,
request-index watermark and compact model/role/type/exact-match counts while
hold remains set, before finally/teardown. Preserve parser errors and duplicates
as failures. Include the last observation in the failure, independently of the
browser-failure file and artifact export. No broad payload/host inventory is
needed. All held_model_request callers are the managed-prefix initial/advance
path and maintenance_case; preserve after-index semantics and len(matches)==1.

No source latency contract yields a correctness-valid replacement for900s.
A bounded discriminator can stop at60s as an evidence-budget decision, not a
new product SLA or accepted-case deadline. Merely shortening/increasing900s
does not fix this failure. Once a supported fixture correction is selected,
require its focused real-interface red/green result, Nix/Python syntax and the
actual packaged-driver typed gate before owning consolidation/affected review
and one original successor packaged creation acceptance. Reuse unchanged Go/
Ruby/Stop/generation/client checks by source binding. No migration, production
API, source-owned recovery or deployment contract change is selected; no product
docs needed. Preserve all cases and original/target identities, admission,
continuation counts, Stop suppression and final restoration assertions.

Bounded findings/missing-evidence decision complete; only design.md appended.
No checks or runtime/source/Git effects performed. Capacity returned; main owns
the next evidence/implementation allocation and this session remains open.

## Send-control setup: missing allowed thread source, harness-only repair

Sufficient amendment to7850, package48d17e8c, 2026-11-07. Current/env and fresh
same-session roster confirmed; architect0 remains Astra/xhigh/workspace_write,
installed full_access, capacity available and settings unchanged. Applicable
guidance hashes unchanged. Read only released terminal control source/logs under
`/tmp/send-gap-aanhnxnl`, pinned c3c2 source and immutable R7b3b guidance; no
mutable final receipt/effect inspection or execution.

**Concrete cause of the setup refusal.** Retained client.go:20 constructs
ClientOptions with ledger/database paths and PreserveThreadInstructionsOnResume,
but omits ThreadSourceKinds. c3c2 client.go:957 copies that slice without a
default; threadSource:5890–92 returns true only for a string contained in it.
With the omitted/nil list every possible source is rejected. headless.go:35–38
includes `!c.threadSource(thread.Source)` in the exact "headless Codex thread
has the wrong identity" branch. This missing client-side allowed source is
independently sufficient to cause the observed error; no timing hypothesis or
native metadata value is needed to demonstrate it.

result.json records CreateProject ID01a1b7bf-ac88-7d60-964c-38044d7ec7b0 and root
01a1b7bf-ac9c-7052-86e9-c174079ad58a followed by this Bootstrap error, before any
Send. StartThreadWithSettings:3727–35 already checked nonempty returned root ID,
exact `/tmp/send-gap-aanhnxnl/work` cwd and requested project ID. Bootstrap's
ReadThreadMetadata checks the queried root ID too. The later metadata source,
cwd/project/fork, ephemeral and historyMode values were not retained, so do not
claim every other identity conjunct passed or that the native actually printed
source=vscode. Model/effort/instructions/provider are not operands of this
particular guard; native log's bundled-bubblewrap fallback does not explain it.
Existing recovery_integration_test.go:53 and
conditional_steer_integration_test.go:58 explicitly configure
`ThreadSourceKinds: []string{"vscode"}` for the same native/headless pattern.

**Minimal revised control package, main allocated.** Repair only the disposable
client constructor with that exact single-source allowlist. Do not change the
SDK guard, accept arbitrary sources, skip Bootstrap or reuse/recover the failed
root. Keep the0.165 binary/hash, c3c2 module, isolated cwd/project, modelgpt-5.5,
effortlow, read-only/never policy, preserved instructions, ledger and actual
creation-model/selector binding. R/application/fixture files remain unchanged.
No SDK/native/config migration or production recovery implication exists.

Before allocating another native invocation, inspect the actual revised
constructor/options value against those two pinned harness call sites and
confirm its sole allowed source is vscode; ordinary readonly compilation must
pass. Preserve the old terminal control and exact revised diff. Within the
same eventual init, before unchanged Bootstrap, retain one ReadThreadMetadata
projection: requested/returned ID, cwd, project, fork source, source kind,
ephemeral, historyMode, rollout path, status and turn count, plus the configured
allowlist. Check source=vscode and the exact requested root; leave the unchanged
Bootstrap guard authoritative for cwd/origin/ephemeral/history/freshness/path
and durable marker verification. In particular, do not add a stricter nonnil
project requirement before materialization: headless.go deliberately permits
nil project metadata for a fresh rollout and requires it after materialization.
Record the projection even on refusal.
This extra read is passive and stays inside the existing operation deadline;
it prevents another opaque setup error, not a promise all runtime setup will pass.
No independent readiness run or mutation-before-admission workaround.

Only after this real init succeeds may the unchanged7850 control perform its
two unique Send calls, prove idle then same-turn steered receipts/native user
identity, release exactly one observed prior request index once, and require
one successor matching the actual selector with negative controls. Keep the
original60s total execution ceiling/55s work deadline and first behavioral
mismatch stopping rule; no retry, deadline increase, additional send or permissive
receipt. Keep existing owned-child finalization, not session lifecycle actions.
The already-terminal9.314s run establishes setup failure only and supplies no
Send/steer/selector evidence, historical7b3b cause or contrary hypothesis result.

Next deliverable is the narrowly repaired control's bound input/diff, metadata
preflight and actual protocol result, or the first precise failure. Main owns
allocation; no second native run is authorized by this document. No product
fix/check campaign/publication follows automatically. Only design.md appended;
capacity returned, session open.

## Send-control ordering: receipt before native history materialization

Sufficient bounded amendment, 2026-11-07. Current/env/fresh architect roster
confirmed; retained Astra/xhigh/workspace_write/full_access unchanged, prior
capacity returned. Guidance hashes unchanged. Read only released
`/tmp/send-gap-repaired-q5fahb_2/{result.json,client.go,control.py,model.py}`,
pinned c3c2 and relevant immutable7b3b fixture source. No final effect receipt,
new native execution, checks or application edits.

**Established interface ordering.** Init/Bootstrap passed. Initial Send returned
Steered=false for root01a1b7c8-ba2c-7061-827e-861a44e90027 and turn
01a1b7c8-bb0e-7781-aacf-909289d99038; actual model request1 and native initial
user item passed. The single marker Send returned Steered=true for that same
turn and client ID777dba71-0f08-4825-a5a8-ffe69fe92c8d. Immediately afterwards,
the page contained only the initial item; releases=[] and no subsequent model
snapshot/negative controls exist. Failure is control.py:64→49's premature
len(users)==1 verdict. This is not an eventual-loss result or historical7b3b
cause, and it does not establish absence of a later model request.

c3c2 client.go:5492–5501 validates the successful turn/steer reply's turnId and
calls finishAcceptedSend:5533–41, which saves the receipt and returns without
reading/waiting for native history. Its accepted reply path therefore promises
no immediate materialization. docs/reference.md's exact-active-turn notice
contract explicitly separates transport acceptance from model processing.
The related native conditional_steer_integration_test.go:78–125 checks receipts
while the provider is held, releases it, then checks unique notice history.
R session-creation.nix:274–281/833–865 likewise advances a known response before
prefix/history proof. The actual released0.165 observation independently shows
why acceptance and materialization must not share the pre-release verdict.

**One disposable file: control.py.** Keep the pre-release projection, but make
the marker-presence requirement phase-specific. Always retain/validate the exact
root, expected/active turn, complete single page (nextCursor=None), native item
IDs and the initial user item's unchanged client ID/text/turn. Before release,
record marker count0 or1: zero is pending observation, not failure; if present,
it must already have the exact marker client ID/text/turn and a nonempty item ID.
Marker text under another client ID is a mismatch, not count0/pending.
Duplicate matching IDs, wrong content/turn, malformed page, changed root/active
turn or RPC error still fail immediately. Do not require marker absence either.
No polling for marker history while the response remains held.

Then take the existing model snapshot and run the actual selector as already
planned. Preserve the explicit discriminator outcome: one initial request and
zero marker matches while held, otherwise stop with the contrary observation.
Touch only the observed initial request's one permit, once. Use the existing
successor-request arrival wait and unchanged remaining deadline. Require exactly
two requests, one matching successor with index>initial, global hold retained,
the initial permit consumed, and no successor permit. Only then run the strict
native proof on one fresh page: exactly one initial user and exactly one marker
user, each bound to its original client ID/text/turn; distinct nonempty item IDs,
unchanged initial item ID, same root/active turn, no incomplete pagination or
duplicate client identities. Reuse that same final page for both identities.
The marker's exact positive assertion moves; it is not removed or satisfied by
receipt/model text alone. Keep all actual model/role/type/text/index/duplicate
selector negatives and the two unique Send calls unchanged.

**Remaining sequence/limits.** Reviewed actual model.py extraction and existing
creation_model handler: logging precedes holding; the initial permit is unlinked
before its response continues. Retained initial data proves the current
thread/items/list envelope and clientId field used by this client. No SDK/client,
model wrapper, filter or input change is needed. Receipt success alone remains
insufficient both before and after release. A matching successor is the useful
processing boundary for the final check, not a general SDK guarantee that every
history reader is synchronously current. If the one final native read still
lacks the marker, stop and retain that exact post-successor gap; do not invent
loss, add a history retry loop, repeat Send or release a second response.

**Preflight and allocation.** Before main releases another invocation, compile
only changed Python syntax and exercise the phase-specific projection with the
already-released initial-only page: observational phase accepts count0; final
phase still rejects it. A finite exact-marker page passes both phases; duplicate
client ID/wrong text/turn/root remains rejected. This is a tiny pure control
check, not simulated native evidence. Reuse the unchanged compiled Go client and
bound source/binary hashes; no new Go build, SDK test, VM or preparation campaign.
The native control retains55s work/60s total, the existing arrival waits and
first substantive mismatch stopping rule, with no new retry loop or budget.
No fixture/product patch is selected. Required original packaged acceptance
remains after a justified correction, owning consolidation and affected review.
Only design.md appended; sufficient control amendment complete, capacity
returned. Main owns any allocation after B's effects/capacity return; session open.

## Maintenance marker admission: sufficient two-file fixture correction

Settled implementation brief, package0d32dc0c, 2026-11-07. Current/env/fresh
architect roster verified; Astra/xhigh/workspace_write/full_access and unchanged
guidance retained. Main's duration steering is accepted: the interface
investigation is closed. One implementer owns the following complete change,
focused batch and commit, then affected review and original packaged acceptance.
No further discriminator, historical-cause prerequisite or harness-only package.

**Established basis.** Released `/tmp/send-gap-ordering-sbj8oip6/result.json`
records pass with the unchanged0.165/c3c2/actual Handler and selector. One initial
request was held; the unique marker Send was accepted on the same root/turn,
but marker history and its model request appeared only after releasing that
known initial index. Final native page contained both exact client IDs/texts
once with stable initial/distinct marker item IDs; all six selector negatives
rejected. This proves a reachable circular wait in the current maintenance
fixture's global-hold-before-Send composition. It does not supply the historical
7b3b receipt or prove that attempt's sole cause. That qualification does not
block correcting the demonstrated fixture defect.

**Owned source: only `test/creation_model.py` and
`nix/tests/session-creation.nix`.** Add a separate fixture control file,
`/tmp/creation-model/hold-maintenance.json`, containing just two records with
`threadId` and `marker`: the selected root and its new case marker, and the
selected ready member and marker+"_member". A small model helper reads these
rules and matches the actual request's `client_metadata.thread_id` plus a complete
line equal to the marker in role=user/content.type=input_text text. No substring
match across arbitrary JSON, system/developer text or another thread. The
complete-line rule accommodates the real team envelope, whose production
runtime.go:2440–43 places the assignment message on its own line; it avoids
copying that envelope into the model. Root acceptance still separately requires
the existing exact whole text part and modelgpt-5.5.

The existing wait_for_turn_response receives the request as well as index and
waits while the original global hold applies OR this maintenance rule matches.
Keep legacy hold-turn and bound release-turn-N behavior intact. Re-evaluate the
small scoped rule while waiting so deleting it releases only its matching
requests, and a later case's different markers cannot keep an earlier request
held. Missing scoped file means no scoped hold; malformed rules are errors,
never an implicit successful release. Keep actual request logging before the
hold and all response/SSE/naming/archive behavior unchanged. This is one small
fixture predicate, not a configurable scheduling framework.

maintenance_case verifies the global hold-turn file is absent (do not remove it
to proceed), chooses/saves the root client ID and member assignment ID once,
and atomically installs the two rules before the existing single root public
Send and single public team assignment. Pre-existing/unrelated requests continue
normally because they do not match; neither a global release nor an inferred
request-index permit is used. An idle Send reaches its first matching request;
an accepted steer can finish the preceding response and reach its matching
successor. Both matching root/member responses then remain held for the same
maintenance assertions as before. A different returned member thread is an
identity mismatch, not permission to silently retarget the installed rule.

Replace only maintenance_case's touch/remove-global-hold operations with owned
scoped-rule installation/removal: cooperative pause acceptance, ordinary final
release before switch_done, and finally. Preserve existing failure restoration
and target barrier behavior. Do not touch global hold operations in managed-input
prefix, lost-reply/restart or other cases. held_model_request's exact-model,
whole-user-text, after-index and len(matches)==1 semantics remain unchanged;
advance_model_response and its known-index permits remain unchanged.

Retain root receipt's nonempty turn and exact original client ID regardless of
Steered=true/false. Bind the selected root model row to its root and receipt
turn through the observed `client_metadata.thread_id`/`turn_id` fields. For the
member, keep the original public assignment/roster and native active-turn proof;
select its unique request by exact thread and complete marker line, then bind
its request turn to that observed member turn. Reject duplicate matching rows,
wrong model at the existing root matcher, wrong thread/turn, malformed metadata,
or changed assignment identity. Do not demand immediate post-receipt native
marker materialization. Require both intended requests before queue/goal setup
and switch_start; preserve captured source turns, once-only assignments and all
subsequent pause/deadline/PublicStop, continuation, retained queue/goal, source
failure/recovery, client identity and restoration assertions/cases/budgets.

**Small useful diagnostics, before teardown.** Save the receipt, root/client ID,
member address/thread/assignment ID, installed marker rules, selected request
indices and expected/observed turn IDs. If request setup fails, print a compact
projection while the scoped file still exists: complete-row count/max index,
candidate model/thread/turn, marker exact-part/line match booleans/counts and
selection error. Retain the original failure after projection. Do not print raw
system prompts, tool catalogs or full request bodies; do not make diagnostics
depend on browser-failure.json or successful artifact export. No new native
probe is needed for these already available request/receipt facts.

**One affected check batch, not another investigation.** Reuse the accepted
a13eef94 result as the old global-hold blocked-predecessor/steer mechanism proof.
Use its retained real initial/successor request bodies with the actual changed
Handler over the existing disposable HTTP control: scoped rule for successor
must let initial complete normally, then log/select and hold the exact successor
until that scoped rule is removed. This exercises the changed implementation;
no new native run is necessary to reconfirm the already-proved Send behavior.
The same finite batch covers idle matching request, member envelope line,
unrelated thread/text passage, wrong role/type/substring not selecting, malformed
rules as errors, duplicate-selection rejection, and unchanged global hold plus
one bound-index permit used by prefix. Use real Handler/predicate/selector code,
not a rewritten implementation. Retain compact old-evidence/new-green binding;
captured prompt/catalog payloads stay disposable and out of committed evidence.

Add finite extracted-caller controls for rule installation before exactly one
Send/assignment, both idle/steered receipts, both intended request/turn bindings,
and owned rule removal on existing cooperative/success/failure-finally paths.
Run changed Python syntax, Nix syntax/embedded Python and the retained actual
packaged-driver typed gate. One60s focused control batch, expected seconds with
available tools, first different failure stops; syntax/type checks use the
already-established quick method. No stress, native exploration, local driver,
VM/preparation or full suite. Unchanged Go, Ruby, sync_source and predecessor
controls are reused by source binding. An extra native execution is not a
default prerequisite; this brief's actual changed-model HTTP test is sufficient
before final independent review.

**Release/compatibility.** Consolidate into the existing owning fixture history,
preserving the accepted preceding corrections and full branch lineage; no Git
action is allocated to architect. Affected independent review covers both model
and fixture caller, exact selection versus gating, unaffected prefix/other
callers and the complete history/no-migration conclusion. Then one original
reviewed-successor packaged creation acceptance must run all cases, especially
deadline/PublicStop and final startup/recovery. Prior7b3b fast/bootstrap/
cooperative successes retain their original scope, not successor acceptance.
No production/SDK/API/schema/input/permission or product-budget change, product
docs, host cleanup or old-operation recovery. There is no unresolved design
dependency preventing this two-file implementer allocation. Only design.md
changed; capacity returned, no execution performed, session remains open.

## Exact8105 startup setup: one same-identity reattempt after proven non-delivery

Sufficient source-only delivery decision, 2026-11-07. Current/env and fresh
architect0 Astra/xhigh/workspace_write/full_access verified, unchanged guidance
reused. Immutable8105939637 source and released creation rawf71c1c52 used; no
mutable final bookkeeping, source edits or execution. Exact8105 cooperative
and deadline/PublicStop finished; final startup/recovery operation did not start.

**Established refusal and authority.** At9705–9716 the root Send was rejected
with native-32600: expected active turn01a1b80d-dcf0-7b20-8b03-c22d70c42597,
found01a1b80d-df4a-75f2-8a79-7718c114202e. Portal logged "message was not sent"
for root01a1b7f6-8c15-7a12-b27f-c33017d19dae and client ID
6d7809a7-aa9c-465f-974b-5d6fc6940b0e; curl failed503 before assignment. Neither
marker appeared in586 diagnostic rows. This is the definite native precondition
refusal path, not a lost reply or failed maintenance operation.

c3c2 client.go:5458–60 restores explicit-32600/-32601/-32602 refusals through
send_delivery.go:17–44/62–78: restore only the owned submitting claim to prepared,
then recheck the original identity/options and queue state. Uncertain/conflicting
state returns UnknownSendOutcomeError or an already-accepted receipt, never a
false non-delivery assertion. docs/reference.md:63–76 explicitly permits retry
with the same identity/options. Next Send re-reads ActiveTurnID and generates
its expectedTurnId; the prepared record binds Steered, not the superseded active
turn UUID. A prepared steer becoming idle is refused at client.go:5425–26; it
must not be changed into a new turn or a new message ID by this fixture.

conversation/handler.go:634–651 maps MessageNotSentError to503 with
code=message_not_sent, notSent=true, retryable from its classifier. Protocol
refusal yields retryable=false; unknown delivery is409/message_delivery_unknown/
notSent=false. The HTTP JSON intentionally omits the native error detail. The
historical response body was suppressed by curl-f, so those exact body bytes
are source-derived, not observed. Browser automatic retry requires retryable=true;
do not describe this protocol refusal as browser-auto-retryable.

**Selected correction: one deliberate fixture reattempt, not a generic retry
policy.** The API permits explicit same-identity recovery of proven non-delivery;
one maintenance-only reattempt lets Send recompute its active-turn precondition.
HTTP cannot distinguish this particular native refusal from another nonretryable
message_not_sent, so do not invent such a classifier or scrape journal text.
The narrowly allowed class is the complete structured non-delivery response;
another persistent protocol refusal gets at most one further no-effect attempt
and then fails. There is no uncertainty about duplicate safety under that class,
and no guarantee the second attempt will succeed if turns continue changing.

**One owning file: nix/tests/session-creation.nix.** Add a maintenance-specific
input helper, used only at maintenance_case's root setup. Leave managed_input
for the prefix/other cases unchanged. Build the original body once from the
saved marker/client ID and original slug. Capture HTTP status and JSON body
using curl without-f, preserving nonzero transport exits as fatal. Require202
with exact client ID, nonempty turn and no queued-only receipt for success.
Only the first response with status503, code exactlymessage_not_sent,
notSent is true and retryable is false admits one second POST. Retain original
URL/root, text, client ID and options; add only the existing retry:true transport
hint. handler.go:618–28 then checks the original attempt before Send. Never
generate another UUID, change text, alter Stop/Automatic or discard a ledger.

Use at most two requests, each with curl's30s max-time (the existing handler
operation timeout), no sleep/backoff or retry-until-green. This bounds HTTP work
to60s plus existing command overhead; it is not a new product grace or a strict
whole-VM scheduling stopwatch. Keep the existing driver command bound. Timeout,
curl failure, malformed JSON, nonmatching status/flags/code, retryable=true,
409/unknown, any second failure or invalid receipt is fatal, with no third
request. Preserve both observed status/body projections in setup diagnostics
before scoped-hold teardown. A first202 never issues another POST; assignment
still occurs once only after the successful receipt, followed by all existing
request/native-turn/unique model/queue/goal/maintenance checks.

The source fixture legitimately remains busy: preceding cases restore one
continuation, retain an active goal and queue/history, and test completed recover;
they do not promise native inactivity. Fast fixture responses permit turn
changes between ActiveTurnID and turn/steer. Historical exact turn producer or
timing is unknown and unnecessary for this contract correction. Waiting once
for idle is not atomic admission; pausing/removing goals, queues or permission
to manufacture idle would weaken required acceptance. Keep the scoped model
hold and all accepted Handler/prefix/Stop/identity/restoration behavior unchanged.

**One focused batch before review/publication.** Exercise the actual extracted
maintenance HTTP helper against the pinned conversation Handler and real c3c2
Client backed by a deterministic Unix-WebSocket protocol peer, using existing
repository/SDK test patterns (web/plan_delivery_test.go and
codex/send_admission_test.go:TestExplicitProtocolRefusalLeavesSendRetryable).
The peer reports activeA, refuses first steer-32600 after changing toB, then
reportsB and accepts the second expectedTurnId=B. Assert unchanged root/client/
text, two RPC attempts but exactly one accepted mutation, prepared after refusal
and accepted after success; the actual handler emits the expected503 then202.
The old one-shot helper fails at that first503; the changed helper succeeds.
No native binary, VM, model call or exploratory harness run is needed.

Finite related controls: first202 submits once; repeated definite refusal stops
after two; unknown-after-write/lost HTTP reply, unrelated503, malformed body and
retryable=true stop after one; changed root/client/text or queued/invalid success
cannot pass. Prepared-steer→idle remains fatal without turn/start; a changed
ledger cannot be relabelled unsent. Keep these in the same small affected batch,
not a new framework. Expected seconds with available tools, one60s test/control
ceiling, first different failure stops. Python/Nix syntax and existing actual
driver type gate cover the changed helper/caller. Reuse unchanged native
a13eef94, scoped Handler, Go/sync/predecessor controls by source binding.

One implementer owns fixture change, focused controls and owning-history commit;
affected independent review follows, then one original reviewed-successor
packaged acceptance including the still-unreached final startup/recovery case.
No production/SDK/API/schema/permission/budget change or product docs. This is a
settled minimal handling decision with no missing evidence prerequisite. Only
design.md appended; capacity returned, main owns allocation, session stays open.

**Accepted verification disposition (423fd4d3 / implementer1 package8bdebe71).**
Main accepted the one-file source and definitive-unsent contract above, but
superseded its layered verification paragraph. Check only the actual changed
HTTP helper with finite response/identity/attempt-count controls, syntax and the
existing real-driver typed gate. Reuse unchanged SDK, Handler and accepted
native evidence; do not build a new SDK/WebSocket harness or retest those
delegated contracts. If a concrete upstream gap appears, use only an existing
named test. Owning commit, affected independent review and original packaged
acceptance remain required. No further investigation or execution by architect;
capacity returned, session open.

## Exact8ef7 final member admission: execution-state evidence is missing

Bounded source-only disposition, 2026-11-08. Current/environment and fresh
same-session architect0 Astra/xhigh/workspace_write/full_access verified;
settings retained, previous package has no pending effects. Documentation skill
and applicable unchanged guidance used. Only immutable
8ef7b8110c49b99f0261f4fb985e406f1bdf082c/tree8004bb64269be09be354ac5cba676f51f78bca3a
and released creation-raw.stdout under
/tmp/lead-wakeup-R-publication-8ef7-hwonsufa/ci were investigated (SHA256
dc37dc93b0de7522227d724fbbff623525c610d78ed258a8e7358c1f3376365f).
No peer mutable packet, source mutation, check or runtime action was used.

**Observed boundary.** Exact8ef7 completed 17 of 18 cases, including
deadline/PublicStop at9626. Final startup-failure setup begins9627; it never
reaches its maintenance operation. The prior complete operation
8742ccb0-4d58-4e22-9b88-f6828dc9c297/revision31 prints reviewer0
thread01a1b82f-fff8-7912-84b1-d24dfe1d11f0 with stopRevision=2 and
continuationDisposition=suppressed at9497. The final setup selects the same
ready member. Its one public assignment dd6a909d-bc62-4ec3-b4fb-2f695d71f170
succeeds at9700–9708; nearby thread/resume logging is not bound to that thread.
At10298, root input has202/steered=true and exact request534 on its receipt
turn. The member marker has no matches; its four diagnostic candidate rows
are older requests37/39/140/332. The ready=True matcher times out903.76s;
first fatal10311 and trace11490–11498 bind this wait, before final recovery.
These facts prove neither a rejected assignment nor a stalled native queue.

**Settled source contract.** nix/tests/session-creation.nix:688–739 chooses
the first roster member with state=ready, sends one assignment, verifies the
returned thread, then waits for both model requests. Roster readiness is not
execution permission. web/server.go:2467–2486 discards Service.Assign's receipt
and returns a roster on success. teamruntime/runtime.go:2344–2450 preserves
the stable message ID, retained model/effort/policy, exact member and envelope;
its marker is a complete line within the assignment text. The existing scoped
matcher accepts that envelope format and exact thread metadata. Neither its
filter nor the already-observed root request warrants a change.

workspacecodex/recovery.go:49–143 has two distinct success paths: an active
thread uses ordinary Send; a cold thread reconciles first, prepares the original
identity, queues it, calls ActivateThreadWithSettings, publishes current-epoch
permission and returns QueuedSubmissionID without TurnID. The HTTP roster
response cannot distinguish them. maintenance_cutover.go:128–147 intentionally
does not grant target activation/continuation to a stopped participant. Thus
the preceding Stop is a concrete relevant setup difference, but no actual
pre/post-assignment recovery record or queue in this log establishes which
Send branch ran or where execution stopped.

Do not equate that queued receipt contract with permission to leave assignments
unexecuted: docs/workspace-portal.md:792–800 says team assignment explicitly
activates the addressed cold thread. c3c2 codex/client.go:4599–4640 implements
activation as thread/resume; QueueWithPolicy:4797–4870 never loads a cold
thread, while already-loaded additions can execute immediately. Existing
TestColdAssignmentAndProgressReceiptsRemainKnownAfterExecutionWithoutBrowser
simulates consumption of queued work on resume. It proves receipt behavior
under that response, not the historical native member state. An unconditional
extra resume, public queue Start, different member, private permission write or
reassignment would guess at the missing state and could hide an assignment
execution defect. No such behavioral correction is selected.

**Shared setup disposition.** Keep the same member/root, installed scoped rules,
single root input with its accepted definite-unsent handling, single assignment,
both unique model requests and exact observed turns. The retained root queue
and active goal from earlier cases explain why inactivity is not a legitimate
new prerequisite; do not drain, pause or recreate them. The preceding stopped
member's suppressed continuation remains a required passing assertion. Fresh
explicit assignment is the supported next activation intent. Current member
queue, pending/native error and activation state are not observed before the
15-minute model wait. No later final-case precondition is established: its
new queue/goal, participant capture, target failure, same-operation recovery,
continuation, client and restoration verdicts all remain required and untested.

**Smallest missing discriminator; main decision required.** Obtain one bounded
passive snapshot of that exact member immediately after the successful original
assignment, while the scoped hold remains installed: (1) ordinary GET
/codex/conversations/<slug>~<address>/queue, retaining queue IDs/order and
clientUserMessageId plus exact expected envelope/marker comparisons; (2) the
existing native(memberThread) read, projecting status, turn IDs/status/error and
user-item ID/clientId/assignment-marker comparisons only; (3) the existing
read-only recovery-record pattern, projecting the exact root/socket/epoch and
whether this member is in ActiveThreads. Preserve the assignment response's
member identity and the existing model-selection projection alongside it.
No raw prompts/catalogs or full histories are needed. The same projection on
the existing failure path distinguishes immediate acceptance from later state;
diagnostic failure must retain the original failure, never grant permission.

This separates an exact still-queued assignment, materialized input with a
native failure/pending state, missing or changed identity, and absent evidence.
Queue presence alone would not justify starting foreign work or another Send;
an empty queue alone would not prove non-delivery. This log has none of these
decisive member observations. Do not infer them from a successful resume log or
zero model matches. No new native/protocol harness, historical reproduction or
automatic CI run is proposed. Main can allocate this diagnostic-only fixture
amendment if needed; it is not a selected green-producing correction.

**Smallest implementation/check boundary if allocated.** Only
nix/tests/session-creation.nix, at maintenance_case's assignment/model-wait
boundary and its existing diagnostic handler; use the current public queue and
native/recovery read interfaces, not new product APIs. One finite extracted
helper/caller batch checks exact member/assignment binding, queued versus native
item projections, malformed/unavailable observations and preservation of the
original failure. Assert no extra Send, assignment, queue Start, recovery or
permission write. Expected seconds, one60s control ceiling, first different
failure stops; reuse existing Python/Nix syntax and real-driver typed gates.
Reuse unchanged root HTTP, scoped Handler/native, Go, sync and predecessor
evidence within their original scopes; no delegated SDK retest or new framework.

No product/SDK/schema/budget/permission change, migration, deployment or recovery
action is justified. A diagnostic-only change needs owning-history consolidation
and affected independent review before use. A subsequently justified correction
still needs original reviewed-successor packaged acceptance through the final
startup-failure/recovery case; the17 completed8ef7 cases are scoped progress,
not successor or final recovery acceptance. Behavioral implementation is not
releasable from these bytes. The precise open decision is member execution state
after this accepted assignment, not another root-transport or matcher question.
Only this design amendment changed; capacity returned, session remains open.

## Exact625e native JSON read: use the driver's file-transfer interface

Bounded source disposition, 2026-11-08. Current/environment and fresh own roster
verified; architect0 retains Astra/xhigh/workspace_write/full_access. Prior
effects are terminal. Applicable guidance is unchanged; documentation workflow
used. Read immutable625e8533825ee4d4fa1f9ae3ed567a6de1856c38 and released
/tmp/lead-wakeup-R-publication-625e-l3wgqtyp/ci/creation-raw.stdout (main-verified
SHA256 ce557b319db699c1e79a09abaa8710f06d689dae6957b1a494b5ad5e68a6d20b),
plus actual cached gxf3q4fva317n39j307wc4dhwg4ryqma driver source. No mutable
peer evidence, source edits or checks were used.

**Exact boundary and limits.** Raw8180–8183 records the root read
01a1b889-4553-7ad3-a4c2-390756384ab8 returning successfully in1.46s.
Trace9458–9484 binds maintenance_case -> continuation_items -> native ->
driver-side json.loads. It is the negative continuation proof while the owned
target startup barrier is held (fixture905), before release and switch_done,
not a completed-cooperative restoration verdict. Finally releases the fixture
barrier; fatal8204 reports comma delimiter failure at character88256. The log
does not retain returned stdout, its length/hash, or JSONDecodeError.doc.
That position is not an output length or demonstrated truncation threshold.
Bootstrap finished7549; cooperative did not finish. Deadline/PublicStop and
final startup/recovery did not run. Cooperative member snapshot7649 cannot
explain the prior8ef7 stopped-member failure.

test/creation_transport.py:65–89 first parses a complete WebSocket message,
checks the RPC response, then prints json.dumps(metadata) once. Protocol parse,
RPC error or unsuccessful producer exit would fail the guest command instead.
session-creation.nix:253–255 passes the successful user()/machine.succeed
returned string into json.loads; continuation_items:535–536 filters the resulting
full history. The passive member helper has a directly equivalent read at715
with its own10s process bound; it did not change native() or the failing caller.

The actual driver machine/__init__.py:434–451 returns successful stdout without
logging it. execute/_execute:583–627/871–909 base64-encodes the guest stdout,
reads a newline-terminated shell block, decodes it, and separately reads exit
status. It declares no output-size cap;4096 is a socket receive chunk, not a
payload limit. Switching succeed to execute, double-base64 encoding, changing
JSON separators or raising a timeout has no established justification. The
released bytes cannot identify the exact corruption/truncation/interleaving
mechanism or prove a driver defect. No guessed mechanism is an acceptance claim.

**Selected smallest output-boundary correction.** One owning file:
nix/tests/session-creation.nix. Have native() obtain the unchanged single
creation_transport.py read result through the driver's existing
copy_from_machine(source, target_dir) interface (machine/__init__.py:650–668),
already used through copy_from_vm for this fixture's final exports. Redirect
that command's stdout to a uniquely named fixture-owned guest JSON file as the
same developer user; retain ordinary command failure/exit handling. Only after
successful completion, copy that exact file and strictly parse the full bytes
from machine.out_dir/target_dir/basename on the driver host. The driver itself
uses its shared directory and host filesystem copy; no payload goes through a
new shell framing/parser. Use paths from its documented interface, not a guessed
build output directory. Do not cat the file back through command stdout.

Keep a small shared local read helper so native() and the member snapshot's
equivalent read use the same file transport. Preserve native()'s existing
unqualified command bound; preserve the snapshot's explicit coreutils timeout10
and its unavailable-on-error behavior. Leave user(), native_request(), protocol
helper, model, HTTP input and unrelated callers unchanged. Unique per-read paths
prevent stale data or later diagnostics from replacing the failed snapshot;
there is no replay or read-until-valid. Keep the exact copied file on parse
failure and print only requested identity, file path, byte length/SHA256 and
parser position. Do not print raw history/prompts/catalogs. A copy, decoding or
JSON failure remains fatal for native() and unavailable for the passive snapshot.

This replaces the observed failing returned-text boundary with the owning
driver's ordinary file interface and retains the full snapshot for assessment.
It is a narrow output-path remedy, not a claim that a proven size limit caused
625e or that another run must pass. It preserves every item, turn, identity and
continuation assertion, including absence before target release and exact once
after recovery. No partial JSON, salvage, sleeps, larger bounds, ignored errors,
new schema/API, native/SDK or production change. The new file path does not
authorize private permission/state writes or session cleanup.

**One finite affected batch.** Use the existing extracted-fixture helper-control
method and local temporary files, without native/VM/protocol setup. Exercise
the actual changed helper with a full synthetic history larger than the observed
parser position, escaped text and distinct continuation/client identities;
require exact parsed equality and preservation of first/middle/last items.
The command-output double may return invalid text while the completed copied
file is valid: the old helper fails and the new helper uses the complete file.
This is a deterministic interface regression, explicitly not historical-byte
reproduction. Nonzero command, failed copy, missing/malformed file and a second
read with a different identity must not return a stale/partial success or retry.
Check the snapshot retains10s and unavailable semantics and native() keeps its
original exception behavior. Delegate unchanged driver-copy internals; no new
transport harness. Run existing Python/Nix syntax and the actual gxf-driver
typed gate. Expected seconds, one60s helper-control ceiling, first different
failure stops; no full suite or local preparation campaign.

One implementer can own this one-file change through those checks and owning
history consolidation, followed by affected independent review. Reuse unchanged
root HTTP, scoped model, member projections, Go/SDK/sync checks within their
proved scope. Main alone allocates original reviewed-successor packaged
acceptance through cooperative, deadline/PublicStop and final startup/recovery.
The member-admission cause and repeated-final-setup-ci-loop concern remain open;
no prior-Stop conclusion transfers from this failure. No migration, mixed-version
product contract, deployment or old-operation recovery changes. The output-path
package is sufficiently specified for main allocation; exact historical bad
bytes/cause remain unavailable. Only design.md changed; no execution or pending
effects, capacity returned, session stays open.

## Exactfe062 cold assignment: start its still-idle queue head explicitly

Sufficient source-only implementation brief, 2026-11-08. Current/environment,
fresh own roster and returned prior effects verified. Retain architect0
Astra/xhigh/workspace_write/full_access; unchanged full guidance/documentation
workflow reused. Source is fe06218801e11e6b2d9d574b3bc7237b5472ace5,
treeb974c338eef1578abe75f542990f2d90d9247d9e, with pinned SDKc3c2. Released
/tmp/lead-wakeup-R-publication-fe062-sfvir2da/ci/creation-raw.stdout has SHA256
dbed937fb8f7d3e803231c8f1b6eadc0eb05bdc219170e8c13d77b71c7409bae.
Only immutable source/released raw were used; no new execution or peer packet.

**The discriminator is obtained.** Raw10748 records the same reviewer0
thread01a1b8b4-a720-7eb2-aaf0-5ffcf3724ba5 after assignment and on failure:
queue head01a1b8cd-c20d-7ea0-ba0b-93094e5387c1 has original client
84915c2c-c1a5-407b-bb9a-0371f17865c1 and exact envelope/marker; native status
is idle with no assignment item, two completed turns and one interrupted turn,
no turn error; root/socket/current epoch match and Automatic/memberActive are
true. These are two sequential snapshots, not continuous or atomic state proof.
Root202/steered input and request557 are present; no member marker exists among
557 complete rows. Prior operation610c6cac-deba-4ccc-bddf-f414939c882c/rev31
binds this same member to stopRevision2/suppressed at9866. Final setup times out
before its maintenance operation. Cooperative and deadline/PublicStop finished
at8842/10027; final recovery remains untested. The native-file fix works at this
boundary. None of these identities or findings is attributed retrospectively
to8ef7.

**Owning defect.** portal/internal/workspacecodex/recovery.go:98–131 prepares
the exact send, QueueWithPolicy adds it, ActivateThreadWithSettings resumes
with retained settings, then permission is published and a queued receipt is
returned. No explicit queued start occurs. Maintenance correctly omitted this
stopped member's continuation/target activation; the next explicit assignment
crosses that cold path. Actual loaded/idle/current permission does not imply
that its durable input has started. docs/workspace-portal.md:792–800 identifies
assignment as explicit activation intent, and the caller waits for its work.
The source assumption that resume is sufficient is disproved for this setup;
the exact unprinted native internal pause flag or scheduling history is not
needed to fix this owner.

c3c2 codex/client.go:4610/4669 implements resume/settings separately from
StartQueueWithPolicy:5177–5232. The latter validates current queue head, binds
the member policy, checks exact client/text history, issues native
thread/queue/start with threadId/queuedSubmissionId, requires an inProgress
turn and reconciles uncertain replies against exact native history. Its existing
TestStartQueueRejectsANonHeadSubmission and prepared-send/queue tests describe
that interface. SDK docs/reference.md:82–96 distinguish queued acceptance from
execution and promise observational receipt recovery without another start.
The R test TestColdAssignmentAndProgressReceiptsRemainKnownAfterExecutionWithoutBrowser
currently consumes its synthetic queue on every thread/resume; that modeled
behavior hides the observed idle-but-queued state.

**Two-file implementation, no dependency update.** Change only
portal/internal/workspacecodex/recovery.go and recovery_test.go. Add a small
private completion step for a freshly enqueued cold send, after the existing
ActivateThreadWithSettings and existing checked permission publication, before
returning its receipt. Keep that publication order: accepted queue input and
explicit activation already grant addressed-thread permission in the current
contract, so an unresolved start remains accessible to ordinary queue controls.
Keep the early hot path and every earlier reconciled/unknown receipt return
unchanged. Do not make a same-ID retry activate an already-accepted old queue.

Read the current native queue using the existing SDK. Match the new entry by
queue ID, original client ID and complete text. If it remains the exact head
and ActiveTurnID is empty, invoke embedded c.Client.StartQueueWithPolicy once
for that entry with the original options.ThreadPolicy. Preserve the preceding
activation's original model/effort and common/member/MCP execution policy.
Do not issue raw turn/start, Send, enqueue, remove or reorder work. A foreign
head or an active turn leaves the accepted input queued under existing FIFO
semantics, with no explicit queue start. A changed entry identity is an error.
If activation already consumed the entry, require existing exact SDK receipt/
history reconciliation; absence alone is not evidence of execution. No start
is needed in that branch. Keep the established queued receipt shape rather than
inventing a TurnID or claiming model completion.

Retain the caller's runtime/roster/managed-retry admission through this step.
The ordinary Send and SendProgressCheck paths already pass a held retry
transaction into recovery. Calling c.StartQueueWithPolicy would reacquire that
lock and cancel the in-flight send's retry state; call the embedded SDK method
inside the existing admitted operation, as the activation path already does.
Check ordinary maintenance admission and original root/socket/current epoch
and addressed-thread permission before the added native mutation, using existing
identities; do not grant or
clear Stop/Automatic/continuation state to obtain permission. Concurrent
managed Stop retains its existing admission/interrupt ordering. Prior completed
Stop suppression stays recorded; this fresh assignment is the new explicit
intent. Keep the recovery-store identity/epoch checks and grant permission
only to the addressed thread as before; a failed start must not roll back or
fabricate that already-published state.

Delegate native head revalidation and exact post-resume/failed-reply history
reconciliation to StartQueueWithPolicy. If its initial head lookup races an
automatic consumption, a passive follow-up may accept only an absent exact
entry PLUS positive original SDK queue/history reconciliation under the held
managed admission. Never convert a remaining queued entry, missing history,
foreign head, cancellation or an unknown outcome into successful execution.
Propagate unresolved start/identity/observation errors, retain all original
prepared/queue ledger records, and issue no second start. A queue-add acceptance
must never be relabelled MessageNotSent or replaced with a new ID. After any
uncertain execution, normal same-ID reconciliation stays observational; explicit
queue controls remain the recovery route. No new durable state or retry policy.

**One focused regression batch using existing tests.** Extend the named R
cold-assignment test's existing serveUnixWebsocket peer, not a new harness.
Keep resume-consumes-queue as a control; add resume-leaves-idle-head where only
the actual SDK thread/queue/start consumes it and produces the original user
item. The old owner must fail because no start/execution occurs; the correction
must perform one enqueue and one queue/start, preserve exact client/text/options,
resolve the real ledger and leave root permission untouched. Run this for direct
assignment and SendProgressCheck. Exercise the held managed-retry context too,
so the new step cannot pass only with RetryPolicyResolver disabled or deadlock
by reacquiring its lock.

Finite sibling controls in recovery_test.go: already-consumed exact input starts
zero times; foreign head and active turn start zero times; changed identity and
unresolved start reply fail without reenqueue; a lost reply with exact materialized
history reconciles; repeated same-ID call adds/starts nothing; changed epoch or
maintenance admission refuses the added start. Keep hot accepted/unknown retry
and stopped/held receipt controls. Reuse current SDK's ordinary queue-start
implementation and tests; no new native/SDK/WebSocket framework or dependency.

Within the repository Nix environment, one anchored command from portal/ is
go test -mod=readonly ./internal/workspacecodex -run
'^(TestColdAssignment.*|TestProgressSubmissionCannotEnterOrdinaryRetry|TestProgressPreservesPendingManualObserverRetry|TestMaintenanceHoldsManagedAdmissionsButPreservesOriginalReceiptAndQueue)$'
-count=1 -timeout=60s, plus normal formatting/diff checks. Expected seconds of
test runtime with cached compilation; first different failure stops for a
bounded fix, no stress/fullsuite or native discriminator. Existing fixture
HTTP/model/snapshot/file-copy/type/sync and unrelated Go evidence is reused
unchanged. Progress's scheduler/admission remains its owner; this shared cold
execution correction does not add scheduled inference or automatic retries.

**Release and compatibility.** This is an R product correction, not a fixture
queue Start workaround. No cross-repository implementation dependency, SDK pin,
native API, schema, journal, budget, input or permission change is required.
Retained queues and original receipt IDs remain readable by older packages;
an older owner may retain the stall. A new binary does not automatically execute
historical saved assignments or recover old maintenance operations. The inline
owner comment/test explains resume versus execution; no product-doc rewrite is
needed to change the existing activation promise. One implementer owns both
files through focused checks and owning-history consolidation, followed by
affected independent review and main-allocated original successor packaged
acceptance through all cases, especially final startup/recovery. Keep the useful
fixture diagnostics and file transport unchanged. The generic missing-state
question is closed; exact native internal pause history remains unknown and is
not a prerequisite. Implementation is releasable from this brief; final recovery
and repeated-final-setup-ci-loop remain open until accepted. Only design.md
changed; no pending effects, capacity returned, session remains open.

## Exactf204 fast failure: apply cleanup limits only to cleanup

Sufficient test-only brief, 2026-11-08. Current/environment and fresh own roster
verified; retain architect0 Astra/xhigh/workspace_write/full_access. Prior effects
returned, unchanged full guidance/documentation workflow reused. Read immutable
f204d431bd19be3e0feadae1b5d57e2e0bb1d056 and released fast-raw.stdout under
/tmp/lead-wakeup-R-publication-f204-btmdu8ln/ci, SHA256
dc98dcb8cc28aae01b1d2f6e6fc272f24aa6177afd37562850b1411162761a12.
The committed maintenance_pause_test.go independently hashes to
d6dc0ff15450ee42ee9bbeac63cb491b8fc3993500d90ccdcfe503465eadd6b5.
No active CI/peer packet, source/check/runtime or lifecycle effects.

**Demonstrated mismatch.** Raw1910–1913 fails
TestMaintenanceUnknownSteerIsSavedAfterCallerExpiresAndCleanupIsBounded at652:
the pause call returns MessageNotSent during the private WebSocket handshake,
DeadlineExceeded/pause-native-timeout, before the endpoint's turn/steer event.
The test's500ms logical-call cap begins before the callback, covering connection,
initialize, metadata and active-turn lookup. Its1s parent also starts before
dispatch. Neither timer measures only the intended post-dispatch cancellation
or cleanup. No unknown-outcome/cleanup assertion was reached; host/load cause
and historical scheduling remain unknown. Production honored a bounded refusal;
this evidence does not demonstrate a product failure.

The peer listens before launching Serve and handles connections concurrently
(main_test.go:257–298). Its optional maintenance callback runs after each
connection's handshake, so it cannot prewarm that setup. c3c2
conditional_steer.go:61–95 creates a new private transport for each call and
claims the genuine submitting ledger only immediately before the steer write.
Warming m.client or waiting for the listener would not move this later private
connection outside the cap. maintenanceControl.client returns *codex.Client;
this path cannot enter workspacecodex.sendWithRecovery or f204's new cold queue
completion. No cold-assignment fix, server/helper or SDK change is selected.

**One file and one test.** Edit only
portal/cmd/workspace-portal/maintenance_pause_test.go, the failing test. Follow
the adjacent accepted TestMaintenancePauseConditionalSteerAmbiguityKeepsLedger
convention for the integrated dispatch stage: ordinary m.pause limits (defaults
5s call/30s recovery), unchanged prepared90s product grace and the existing3s
integration caller guard. Remove500ms/650ms overrides from that stage. Replace
the independent1s arrival timer with that caller's Done guard. Missing dispatch,
early pause return or caller expiry is fatal, never a skip or successful unknown.
This stops asserting arbitrary cold connection progress within a short cleanup
allowance; it does not redefine or enlarge any production deadline.

At the actual turn/steer event, require the caller still live, capture the exact
wire request, then explicitly cancel that same caller and join the pause result.
Continue withholding its reply and require typed UnknownSendOutcomeError plus
context.Canceled, never MessageNotSentError. This preserves caller termination
after real dispatch, genuine submitting ledger and savePauseResult's detached
bounded persistence; no preseed, raw-Request substitute, timer reset, sleep or
retry. A3s integration guard is still a finite setup limit, not a guarantee
against arbitrary scheduler stalls. Keep early-exit diagnostics phase-specific.

After the pause goroutine has returned, create a value copy for cleanup (e.g.
cleanup := m) and set only that copy's pauseCallTimeout=500ms and
pauseRecoveryTimeout=650ms. Call cleanup.cancelNotices with the existing fresh3s
cleanup caller. Do not mutate a controller being read by the running pause.
Both controllers retain the same store/operation and real ledger. The ordinary
Controller.Cancel, before/after exports and all cleanup assertions remain.
cancelNotices derives its own650ms shared and500ms per-call contexts on entry
(maintenance_notice_cleanup.go:107–119); it does not need those limits installed
before the original steer. No on-wire cleanup-arrival prerequisite is added.

Preserve one original Root/NoticeID/Cwd/SourceTurn/action/text digest and actual
wire parameters, Steered=true/submitting ledger before and after cleanup,
one steer/no start/no resume, saved unknown notice, recovery-required with
notice-cleanup-timeout and live cleanup caller, CancelRequested, unresolved
blocker, nonaccepted cleanup, unchanged saved deadline, StopRevision,
continuation, phase/cutover/source-stop/activation and package/profile identities.
Keep elapsed values diagnostic only. Prior design7672–7735's cleanup verdict
and acceptance stay intact; only the unrelated dispatch timer coupling changes.
Direct initialized-call and NativePauseCapDerivesBoundedDeadline tests still
prove the500ms cap independently; this integrated test must not claim that proof.

**Single quick batch.** In the repository environment from portal/, gofmt and
`GOWORK=off go test -mod=readonly ./cmd/workspace-portal -count=1 -timeout=60s`
with `-run '^(TestMaintenanceUnknownSteerIsSavedAfterCallerExpiresAndCleanupIsBounded|TestMaintenancePauseConditionalSteerAmbiguityKeepsLedger|TestMaintenancePauseSilentNativeOperationsAreBounded|TestMaintenanceNativePauseCapDerivesBoundedDeadline)$'`.
Require actual endpoint arrival, explicit cancellation and all original ledger/
state/cleanup assertions. Expect a few seconds of test runtime plus cached
compilation; first different failure stops for a bounded disposition. Historical
dc98dcb8 is the failed setup evidence; do not manufacture a timing reproduction.
Reuse the prior cleanup cap-bypass negative evidence because cancelNotices,
its500ms/650ms limits and3s live-caller oracle are unchanged. No new negative
harness, stress repetition, SDK/native test, Nix/VM campaign or unrelated checks.

The owning maintenance commit in this exact history is3c854f54; the later
ed010010 test commit touches the same file for a separate grace-transition
purpose. Fold this small correction into its actual owning test history while
preserving that later purpose and all unrelated lineage, under main's serialized
Git allocation and affected independent review. No product/SDK/API/schema,
permission, migration, deployment or recovery change; no cross-repo dependency.
One implementer package is releasable now. Main selects subsequent original
reviewed-successor packaged acceptance. The still-running original creation
observer continues unchanged; its eventual evidence is separate from this fast
failure. Final recovery and repeated-final-setup-ci-loop remain OPEN. Only this
design amendment changed; no pending effects, capacity returned, session open.

## Exactf204 cooperative assignment: retain the missing HTTP refusal

Sufficient bounded disposition, 2026-11-08. Current/environment and fresh own
roster verified; retain architect0 Astra/xhigh/workspace_write/full_access.
Prior effects returned; applicable guidance and documentation workflow read/reused.
Source is immutable f204d431bd19be3e0feadae1b5d57e2e0bb1d056, tree
78399507aabd9b5efee2ed76414c46c2d44652f7. Released creation-raw.stdout under
/tmp/lead-wakeup-R-publication-f204-btmdu8ln/ci has SHA256
464b1eb0a0380ea41d22c90671c99e73adb39c85eb7b7cacd944999a67e87569.
No mutable implementation/CI packet or current source was used.

**Decision: the discarded error body prevents selecting a product correction.**
Raw7623–7628 is one team assignment, HTTP409/exit22 with empty captured stdout;
curl -f discarded the response. Raw8834–8844 binds public_post, before the new
cooperative maintenance operation. Raw7645/7650 independently proves later exact
execution: reviewer0 thread01a1b90f-9d82-7412-afe2-ac6eaa57fc64, client/assignment
dea237d4-7975-4230-bef5-bbf400ca9671, active turn
01a1b919-3a49-7842-aefd-414cc5883565 and original user item
01a1b919-3a9f-7783-8998-4912fce87a7c with exact envelope/marker. Queue is empty;
native error is null; saved/current permission epoch matches with Automatic and
memberActive true. Model row37 matches that member/turn/marker; root row36
matches its distinct202/nonsteered receipt. These later sequential observations
do not prove API acceptance, its internal branch or the earlier observation
state. Returned roster/member and after-assignment snapshot are absent.
The released service tail contains no assignment refusal text; its model-catalog
decode message is not evidence of this409's cause. Bootstrap finished7549;
cooperative failed7663; deadline/PublicStop/final recovery are unrun.

**Exact return boundaries.** portal/internal/web/server.go:2467–2486 maps
Service.Assign errors to409 (settings errors400). Its final roster reload
failure is503, so that boundary cannot explain this409.
teamruntime/runtime.go:2344–2450 returns SendWithOptions directly after admission,
member/policy resolution and accepted-ledger compaction. Ordinary successful
assignment has no later roster write. withOperationLock:643–649 returns its
callback error; deferred unlock/close cannot replace success with409.

workspacecodex/recovery.go:81–134 can select hot Send or cold queue/activation;
the log does not identify which. In the cold path, native queue acceptance can
precede an activation error, managed retry-binding save error
(turn_retry.go:481–486/445–475), checked recovery publication error, or the new
completeColdSend read/identity/admission/reconciliation error at139–219.
Pinned c3c2 codex/client.go:QueueWithPolicy:4797–4863 validates the queue-add
reply and otherwise reconciles exact client/text; execution can coexist with an
invalid/lost reply whose immediate observation fails. StartQueueWithPolicy:
5177–5232 similarly validates turn ID/inProgress and performs bounded exact
history reconciliation before returning an error. R adds one passive absent-entry
plus exact reconciliation after a failed Start, never a second Start. Missing
history, remaining queue, identity mismatch, cancellation and read/persistence
errors remain failures. ReconcileSendWithOptions:5294–5325 returns a queued
receipt for either a queue row or a history item; receipt shape alone cannot
prove execution. Its walkThreadItems uses thread/items/list; the later fixture
native read is not evidence of that earlier page. Hot-send receipt/binding
failures also remain possible. None is selected as the historical reason.

Design8586 and review01a60438 remain context, not proof against this failure.
The existing cold test covers auto/idle/race consumption, absent history,
lost reply and cancellation with immediate controlled observations. Those
passing controls do not establish the missing real response or justify relaxing
any error. No SDK pin, product mutation, extra wait or new cold-start policy is
supported by these bytes.

**Smallest releasable amendment: one fixture helper.** Change only
nix/tests/session-creation.nix public_post:518–521. Reuse the nearby
maintenance_input response convention: one curl -sS with the original max-time20,
socket, Origin, Content-Type, URL and exact serialized body; remove -f and append
the existing newline/http_code write-out. Split the last newline once. Before
JSON decoding or returning, fail with path, exact status and raw response body
for an unsuccessful HTTP result. Preserve both existing successful callers:
teamAPI returns200; pinned conversation/handler.go:541–553 interrupt returns202.
Do not mistakenly impose200 on Public Stop. No other public_post callers exist
in this source. Keep the success JSON result and all caller identity/roster/
Stop assertions. Transport failure, missing/malformed status, malformed success
JSON and any other response remain fatal. One request only, including409;
no parsing of an error into success, reconciliation call, retry or new ID.

The error must retain the raw payload even if it is not JSON, so its original
reason cannot be replaced by a JSONDecodeError. Existing setup catch/snapshots
and driver failure output remain; no new diagnostic subsystem or service logging
is needed. Log only endpoint/status/error payload on failure, without dumping
successful roster instructions, request headers, prompts or catalogs. This
changes observability, not the assignment verdict, permission/Stop/held guards,
queue order, receipt uncertainty, submission count or any budget. It does not
authorize another request after an uncertain or failed result.

**One finite affected batch.** Use the established extracted-Python-helper
control recipe with injected user results, exercising the actual changed
public_post. Require200 team JSON and202 interrupt JSON to return unchanged;
409 with a distinctive error body and503 must fail with their exact status/body;
non-JSON error must retain its bytes; malformed success/framing and transport
exception must fail. In each case require one original request, unchanged
URL/body/IDs/max-time20 and no second call. This checks the changed HTTP-helper
behavior, not a simulated native diagnosis. Run that Python control once under
the existing60s control ceiling (expected seconds), Python/Nix syntax and the
established actual gxf-driver type gate (`ty check testScriptWithTypes` in the
locked environment), plus normal diff checks. First different failure stops.
No Go replay, native/SDK/protocol harness, timing reproduction, VM preparation or
full-suite check is required for this diagnostic change. Reuse unchanged
Handler/SDK/cold-recovery/model/native/file-copy/sync evidence within its scope.

One implementer may own this helper through focused checks and consolidation
into its fixture-owning history, preserving the separate design8732/6e37cbbf
test correction and all other purposes. Main allocates that window and affected
independent review. No schema, API, dependency, migration, deployment or recovery
behavior changes; no cross-repository dependency. Diagnostic implementation is
releasable; a cause fix is not. The smallest remaining discriminator is the
actual failed assignment's HTTP error body, captured at this same public POST
boundary. These historical discarded bytes cannot be recovered by another
snapshot. Main must explicitly decide any successor packaged acceptance;
this brief does not allocate an automatic rerun or claim the409 resolved.
Original full creation acceptance through cooperative, deadline/PublicStop and
final startup/recovery remains required. repeated-final-setup-ci-loop stays OPEN.
Only design.md changed; no executable checks, source/Git/runtime effects or
pending handles. Capacity returned; session remains open.

## Exact93fd model evidence: reduce retention, stream reads, fail on corruption

Sufficient source-only brief, 2026-11-08. Current/environment and fresh own
roster verified; retain architect0 Astra/xhigh/workspace_write/full_access.
Prior effects returned. Applicable unchanged guidance/documentation workflow
reused and exact R AGENTS read. Source is93fd14ba36bd2efaf86f1a3ace9ae8ce605e6af5,
treee9e1ca90ee5edf702d1e483320ea81183d3c50b2. Released creation-raw.stdout under
/tmp/lead-wakeup-R-publication-93fd-7kvjjx7y/ci has SHA256
57436bd2718216ef664faa8aed0da784265424832151f653e64d5d26be70861e.
No pending peer packet, new execution or mutable source was used.

**Earlier concrete failure found.** Raw10041–10046,10070–10075,10096–10101
and10129–10134 bind four OSError(ENOSPC) failures to creation_model.py:100,
the requests.jsonl log.write, at04:02:53–55UTC. These precede the first guest
JSONDecodeError10162 at04:03:20.854. The malformed complete-line parse repeats
at the same position, including diagnostic10847/10850; the wait eventually
fails904.88s/900 at10863. This is guest Python reading its local log, not JSON
returned through the NixOS driver's stdout/native() path. char5586699 is only
a position in the string passed to json.loads. No failing line bytes, physical
file offset, file size or filesystem allocation breakdown are retained here.
The exact partial-write/append sequence and which files exhausted storage are
unknown; later OOM/panic/brokenpipe do not establish their cause or explain
the earlier write failure. No capacity increase or host cleanup is selected.

Current exact93fd cooperative8661 and deadline/PublicStop9949 completed.
Final case starts9950 but never starts its new maintenance/recovery operation.
Raw10146/10831 bind the same selected/returned reviewer0
01a1b93f-fc8c-7601-af1b-55ffe2a91dc9 and assignment
e9d433d8-ecef-47b2-a50f-c7ba6bf67199 to exact native user input in active turn
01a1b952-ce91-7330-bb4d-b8aed9afbac0, empty queue and matching current-epoch
Automatic/memberActive permission. Those sequential observations prove neither
the model request nor continuous state. Request counts are unavailable, not
zero. Historical f204409 and final recovery remain unproved.

**Owning mechanism and limits.** test/creation_model.py:79–101 parses the actual
Responses request, allocates its index, then appends the entire request plus
index/provider/overload/retryAdvice. Its process-local threading.Lock spans
write and close, serializing its ThreadingHTTPServer writers. This is not an
atomic durable record transaction: an I/O failure can leave an unfinished
append, and the server can handle a later request after that handler fails.
The emitted ENOSPC is at this sink before that handler's hold/SSE response.
It does not prove interleaved successful writes or malformed incoming JSON.

All six readers are in nix/tests/session-creation.nix: held_model_request:321,
naming_proof:381, resume_requests:553, maintenance_model_requests:695,
post-restoration resume proof:957 and failure export:1414. Each retains all
decoded request bodies; the export additionally reads/splits the entire file.
Five skip non-newline fragments but are not finite snapshots. The three waits
retry every nonzero process result, conflating parse failure with absence.
No consumer needs the other top-level Responses fields, including tools and
instructions. Every original input predicate can be preserved without changing
body.input; do not narrow it to selected roles or replace text with booleans.

**One complete two-file fixture package.** Only edit test/creation_model.py and
nix/tests/session-creation.nix. At the existing append boundary persist the same
index/provider/overload/retryAdvice and a body containing model, full input and
client_metadata with their original values. Preserve missing-field semantics,
all input roles/order/content, duplicates, exact text and metadata; no truncation,
hash-only replacement, record filtering, sampling or rolling retention. Remove
only unused top-level request data from the saved evidence. The original parsed
request remains unchanged for response selection, archive repair, naming,
scoped/global holds and bound-index release. Keep one index and append per actual
request and the current writer lock; propagate write/close failures before a
successful response, never ignore/retry the append. No SDK/product input changes.

Put one small strict request-row iterator beside the existing model helpers and
reuse it through the fixture's existing runpy convention. Open the JSONL in
binary mode, capture the append-only file's size once, and read individual lines
only through that boundary. Stop at an unterminated final fragment; never resume
parsing a suffix after discarding its prefix or read new appends past the boundary.
Decode/parse every complete row strictly. Malformed complete JSON, invalid UTF-8,
I/O or required row-shape errors propagate, with line/offset context rather than
payload dumps. Do not salvage a bad row or return partial success. Close the file
on completion/error. A later ordinary observation gets a fresh prefix; no writer
lock across polling, compressed framing, per-request file store or new service.

Convert all six consumers to one-pass accumulation of their existing results:
matching indices/providers, complete count/max index, exact per-rule match
projections, existing last20 candidate projections and naming export fields.
Do not collect raw rows or repeatedly reopen the iterator per rule. Exhaust the
whole captured complete prefix even after finding a match, so later corruption
or duplicate matches cannot be hidden by any()/early return. Preserve every
model/role/text/marker/thread/turn/after-index predicate and duplicate failure.
This reduces reader memory to one row plus required compact results, not all
historical bodies. Input itself remains unbounded by a new arbitrary threshold.
The change removes unnecessary storage and aggregate memory amplification; it
cannot promise space availability under arbitrary guest work or establish the
historical byte contribution of omitted fields.

For the three polling consumers, use the already exported NixOS driver retry
callback with the same900s default/one-second interval. The cached gxf driver
machine/__init__.py:101–119 retries False and propagates exceptions; driver.py:331
exports it to test scripts. Each callback calls ordinary user()/machine.succeed
to obtain a strict parsed compact result. Return False only for a valid scan
whose required request is not yet present. Parsing/transport errors and duplicate
matches raise immediately. A valid complete match returns True and is retained
for the caller. For maintenance readiness, require exactly one match per original
rule; for the later resume proof, retain its existing predicate. Preserve all
configured deadlines; this only stops retrying a demonstrably invalid observation.
No second Send/assignment/start, fallback identity, altered holds or recovery
action belongs in this change.

**One focused affected batch, expected seconds,60s control ceiling.** Reuse the
existing extracted Python/model helper recipe, ordinary temporary files and
injected user replies; no HTTP/native/server/VM harness. Exercise the actual
projection/iterator and extracted six consumers with exact marker/envelope,
model/provider/thread/turn and duplicate/after-index controls. Compare original
and projected predicates on the same representative records, including markers
in non-user content, so pruning cannot silently alter broad existing predicates.
Large unused tools/instructions must not change stored evidence; changing any
retained field must remain observable. Preserve every record/index and naming
overload/retry-advice facts. Check complete prefix plus growing incomplete tail,
malformed complete row before/after a valid match, invalid encoding and injected
write failure; errors remain errors, not empty counts or successful responses.
Check streaming consumption without accumulating full bodies. Exercise callback
False-then-valid success and immediate parse/transport/duplicate failure using
the real exported retry function and injected replies, with one observation for
each fatal case; this is control-flow evidence, not a historical reproduction.

Run Python syntax, Nix syntax/extracted embedded Python, existing real gxf-driver
`ty check testScriptWithTypes` and normal diff checks in the repository environment.
First different failure stops; no stress, full Go replay or new framework.
Reuse unchanged root HTTP, native-file transport, scoped hold/selector mechanism,
Go/SDK/sync/identity/Stop evidence within its source scope. The shared archive
model still uses the untouched actual request for repair/SSE; its log has no
additional repository consumer. Keep that behavior in the finite model controls,
without replaying archive acceptance locally.

**Release.** One implementer may own both files through the finite batch and
owning fixture/model history consolidation, preserving accepted8732/8829 and
other purposes, then affected independent review. This is a supported fixture
evidence correction, not a product failure diagnosis or a guarantee that every
storage issue is solved. No persistent product schema, API, dependency, budget,
permission or old-operation recovery changes. JSONL stays disposable test
evidence; new readers also accept old complete records with extra fields, while
the new writer preserves fields used by old selectors. Do not rewrite old logs
or claim malformed historical bytes repaired. Source/check contracts above are
stable for allocation; original reviewed-successor packaged acceptance through
final recovery remains main-owned and required. No new run is allocated here.
repeated-final-setup-ci-loop remains OPEN. Only design.md changed; no checks,
application/Git/runtime effects or pending handles. Capacity returned; session open.

## Exact2219 queued assignment: preserve fresh acceptance across history visibility

Sufficient bounded source/design brief, 2026-11-08. Current/environment and fresh
own roster verified; retain architect0 Astra/xhigh/workspace_write/full_access.
Prior effects returned; unchanged full guidance/documentation workflow reused
and exact R AGENTS read. Source2219b520521ad068020d119ae79769e05632f79f/tree
58d039a63fe243fbf479540f1c8719336f84a7d0 uses the actual c3c2adb705f5 SDK.
Released creation-raw.stdout under /tmp/lead-wakeup-R-publication-2219-lz8qu3re/ci
has SHA25688fc532bfd130496f2fc5d26a43b3e73be75d5c70f013760953bf562a67d4b26.
No mutable packet/source or new execution was used.

**The new body selects queued reconciliation, not an HTTP transport refusal.**
Raw7739 retains409 and the exact SDK UnknownSendOutcomeError wrapper plus
"earlier queued send outcome is unknown". c3c2 codex/client.go:5323/5407 are
the only producers of that suffix, in ReconcileSendWithOptions and
SendWithOptions. Both passed exact ledger identity/options validation, found a
queue-attempt digest, then obtained successful queue/history reads with no
matching original item. A client-ID match with changed text, malformed page,
RPC error or ledger error would produce a different error. The queue-attempt
digest is recorded before queue/add: by itself it proves attempted submission,
not acceptance. The HTTP adapter preserves the error at409; it does not retry.

The fixture creates one fresh assignment UUID and makes one public POST
(raw7699–7703). For that fresh path, R recovery.go:98–134 already obtained a
successful QueueWithPolicy result, completed activation, and published checked
current-epoch permission before completeColdSend. Its first queue scan can find
the entry absent and call ReconcileSendWithOptions at166/183–184. That is the
fresh-completion route to the unjoined error. A failed StartQueue route at209–215
would retain the original Start error with errors.Join; the observed body has
no such prefix/join. A prior-attempt reconciliation or hot Send can emit the
same suffix in general; they require prior identity state and must not be
changed. No RPC transcript or original page bytes were captured, so exact page
contents, visibility delay and native scheduling cause are not established.

Later raw7720/7739 binds reviewer0 thread01a1b986-4f30-7280-a41b-49175f2896ef,
assignment73eb8b18-1b85-41a6-8c22-36a24d2ef12e and active turn
01a1b990-7fa1-7200-a851-e66158a852f2 to exact user item
01a1b990-800f-7e30-bfaa-6cbda647b357, empty queue, null native error and matching
Automatic/memberActive current epoch. Model rows36/37 bind root/member. These
later non-atomic observations do not supply the earlier missing proof. Fixture
native() uses thread/read(includeTurns=true); SDK startedByClientID uses
thread/items/list across validated descending pages. Their observations are
not interchangeable. No2219 reader-corruption fatal was reported. Bootstrap7625
finished; cooperative failed before its operation; later cases are unrun.

**Supported mismatch and owning decision.** SDK QueueWithPolicy:4797–4863
returns success only after an exact native queue acknowledgement (nonempty ID,
original client/text) or positive queue/history reconciliation. R holds that
fresh result locally. The SDK explicitly accommodates history appearing after
native acceptance: continuation_integration_test.go:78–101 documents that fact
and uses observational reconciliation for lost receipts. Its recovery tests
separately preserve unknown queued attempts and reject duplicate dispatch.
No immediate-history guarantee is supplied. R's new initial-absence check
therefore makes a fresh acknowledged queue admission depend on a second,
potentially not-yet-visible history observation. This is unnecessary for returning
the existing queued receipt. The same helper already returns queued acceptance
for a foreign queue head or active turn without claiming execution completion.

Revise design8586 only at that fresh initial-absence branch. This is a material
design correction referred to main for acceptance. No provider/SDK change or
new pin is needed: keep the provider's conservative prior-attempt contract.
Do not add a live-history fallback in R, new ledger acceptance state, wait loop
or a second SDK Send. Those expand the owner boundary without being necessary
to preserve the positive acknowledgement already obtained by this call.

**Two-file R package.** Edit only portal/internal/workspacecodex/recovery.go
and recovery_test.go. In completeColdSend, after the existing first ListQueue
and exact position validation, an absent entry means there is no matching head
left for this completion step to start. Preserve the existing ctx.Err refusal;
otherwise finish this step and return the original fresh queued receipt from
sendWithRecovery:134. Do not invoke reconciliation solely to re-prove that
already acknowledged fresh queue admission. Add a short comment distinguishing
acceptance from asynchronous history visibility. No fabricated TurnID, Steered
flag, resolved-ledger state or execution-ready result is introduced.

The authority is the successful exact QueueWithPolicy result in THIS admitted
call plus successful retained-settings activation and checked permission
publication, not empty queue alone, later samples or a saved queue-attempt bit.
Keep every earlier reconcile return, queue/add error, activation/binding/save
error, identity conflict, cancellation and ListQueue error fatal. Preserve
foreign-head/active-turn handling and the idle exact-head StartQueueWithPolicy
once path, including its admission/root/socket/epoch/member-active checks.
After a failed Start, keep existing absent-entry PLUS positive exact history
reconciliation; an unresolved start error must never use this new acceptance
branch. Preserve held runtime/team/managed-retry locks and Stop ordering.

The original queued acceptance is not proof that the item has executed or that
history/lifecycle is resolved. RequireSubmissionAttemptsKnown/Resolved and
same-ID replay still use the unchanged SDK: if neither queue nor history is
visible, they remain errors and cannot submit/activate again. The unchanged
creation fixture must still observe exact root/member model requests, native
input/turn identities and all continuation/Stop/restoration/recovery assertions
before progressing. HTTP409 is not caught or swallowed; the unnecessary fresh
re-observation is removed before it manufactures that error. Progress's
SendProgressCheck shares this cold path under its own held admission and gets
the same queued-acceptance semantics; its deferral and retry exclusions remain.

**One focused existing-peer batch.** Extend
TestColdAssignmentAndProgressReceiptsRemainKnownAfterExecutionWithoutBrowser
for direct and progress calls. Separate executed/consumed state from paginated
history visibility in the existing serveUnixWebsocket peer. The exact queue/add
acknowledges once; resume consumes it; first queue scan is empty while items
history remains hidden. Require the original queued receipt, one enqueue,
zero explicit queue/start, successful addressed activation and unchanged root
permission. Original2219 must fail this control with the exact Unknown suffix;
the correction must pass without waiting for history. While hidden, assert
resolved proof and same-ID replay remain errors with no further mutations.
Then expose the original exact item through the peer's controlled state and
require passive reconciliation/resolved proof, retaining identity/options.
No timed sleep, retry-until-visible or real-native reproduction is needed.

Keep independent negatives for invalid/lost queue acknowledgement with no
positive queue/history proof, an earlier unknown queue attempt, and cancellation
in the initial absent branch: all error, no fresh activation/start/resend. Keep
the existing failed-start/missing-history, lost-reply-positive-proof, changed
identity, foreign head, active turn, epoch/permission/maintenance and held retry
lock controls. Do not merely change the old missing-history assertion to success
without proving this fresh-acknowledgement versus prior/failed-start distinction.

One repository-environment command from portal/:
`GOWORK=off go test -mod=readonly ./internal/workspacecodex -count=1 -timeout=60s -run '^(TestColdAssignment.*|TestProgressSubmissionCannotEnterOrdinaryRetry|TestProgressPreservesPendingManualObserverRetry|TestMaintenanceHoldsManagedAdmissionsButPreservesOriginalReceiptAndQueue)$'`,
plus gofmt/diff checks and the isolated old-owner negative for the new case.
Expected seconds of test runtime with cached compilation; first different
failure stops for disposition. Reuse unchanged SDK tests and native/Handler/
fixture/model/file-copy/type/sync evidence in their exact scopes. No new native,
HTTP/protocol harness, full suite, VM preparation or timing campaign.

**Release/compatibility.** One implementer owns both files through focused
checks and consolidation into the actual maintenance owner5d1739b5, preserving
the later independent purposes and accepted8732/8829/8943 corrections. Main must
accept this revised boundary before allocating source/Git windows, affected review
and original successor packaged acceptance separately. No cross-repository
implementation, SDK/API/schema/input/permission/budget change or migration.
Original queue-attempt/prepared records stay intact for ordinary same-ID
observation and queue controls; older packages may reproduce the strict fresh
history refusal. No automatic replay or old-operation recovery is added.
Historical f204409 cause remains unknown. Exact2219 observation timing is not
needed to correct this contract mismatch and is not claimed resolved. Final
packaged recovery and repeated-final-setup-ci-loop remain OPEN. Only design.md
changed; no checks/application/Git/runtime effects or pending handles. Capacity
returned; session remains open.

## Exact1207: post-recovery blocked goal and guest evidence ENOSPC

Bounded disposition87eaa808, 2026-11-08. Current/environment and fresh own roster
match this session; architect0 retains Astra/xhigh/workspace_write/full_access.
Documentation workflow and applicable full guidance read/reused. Sole source is
1207fb734a599232374aaa5858f66acfc5a18807/tree3600ff42afcaccf640653210d049c26c7b580a70.
Released creation-raw.stdout under /tmp/lead-wakeup-R-publication-1207-4wwm3ymt/ci
has SHA256630a70b77cf38817820816c9b490dfcbb6dce415d7a08d6560f7f89bbb6ca5e2.
No source/check/runtime/CI mutation was performed.

**Settled stage and verdict.** The traceback12694–12697 maps embedded script821
to session-creation.nix:999, the post-completion retained_state call; its691
requires the exact original root/objective/goal identity to remain active.
The earlier held-state check964 passed. Final operation1492f696-1f46-4773-b103-d1ffd735ea63
did run and recover under that same UUID (public recovery10837–10842). Raw10964
passes activating/rev23 to the stopped-client proof;11207 passes complete/rev32,
outcome updated, settled accepted continuations and completed ten-terminal
restoration to the restored-client proof. Its command succeeds at11215. Execution
then passes continuation uniqueness/text, resumed-model observation and roster
equality before the final retained-state check. Native history and queue identity
checks inside that call also precede the failing goal assertion. Completed-recover
replay1000–1006 and final case evidence write were NOT reached. Cooperative and
deadline/PublicStop completed only within this exact run; the final case remains
failed/unaccepted despite this meaningful recovery progress.

The root is01a1b9b5-81d9-7fb2-adf2-4d8ce84e691a; final objective is
CREATION_MAINTENANCE_startup-failure_4981ac3e-96e0-4142-ad97-a61e4a1c60b3 goal.
Raw11362 reports blocked, no tokenBudget, tokensUsed2150/timeUsedSeconds452.
Its createdAt is06:03:46UTC, also retained in earlier case snapshots; updatedAt
is06:14:24UTC. This is a last-update timestamp, not a captured transition reason.
The first logged writer ENOSPC is11257–11262 at06:14:23.847, followed by two more
at11287/11312. Portal state writing under /home/developer fails later11364.
No goal-status event or final native turn error is printed. Temporal proximity
does not establish which failure blocked the goal.

**Owning growth/storage boundary.** creation_model.py:21–50/112–194 projects
only model/input/client_metadata, but retains the FULL input for EVERY request.
Append/close precede response holding and SSE; an ENOSPC therefore escapes without
a successful mock response. Complete malformed records still fail strictly;
an unfinished final append remains an uncommitted tail, not proof of a response.
The ordinary mock emits the same final answer and two-token usage; it never
completes or pauses a goal. maintenance_case894 activates the retained root goal,
916/976 remove scoped response holds, and no goal retirement follows the case.
The actual complete-row count grows37→599→980 at7799/8891/10187, with distinct
root turn IDs among the later candidates. Cooperative's target-held snapshot
at8739 already has456 tokens/68seconds; deadline's10034 has1114/221. These facts
support uncontrolled fixture inference/evidence growth; they are not byte counts
or proof that requests.jsonl alone filled the filesystem.

Immediate consumers remain the six strict streaming selectors/summaries in
session-creation.nix; native_json253–279 also retains each full native read in
a unique guest file and copies it through the driver. Native histories, portal
state and logs are additional source-supported consumers. The fixture164–175
declares6144MiB RAM/4096MiB disk. Its owning root nixpkgs is a5cc6f2c37bf518436dc8d1c288ccd0c43c2f4c4
(flake.lock root.nixpkgs_2, not llm-agents' f20c input). Its cached nar-hash-bound
source /nix/store/nqkh6j5xlyvlw4hlrw4ybpq1cis79szf-source, at
nixos/modules/virtualisation/qemu-vm.nix457/1495, selects an ext4 root disk;
nixos/modules/system/boot/tmp.nix51 defaults useTmpfs=false. The R host/test modules
do not override /tmp. Raw3485/4010/4044 independently shows a4GiB vda and ext4
mount. Writable Nix-store overlay defaults to separate tmpfs; additionalPaths
does not by itself prove4GiB of guest-root package copies. No retained df/statvfs,
allocated-file totals, inode exhaustion or free/reserved-block sample exists.
No artifact was retained by this failed workflow. Do not substitute current host
storage readings or historical runs for those missing guest observations.

**Decision: no cause correction is yet justified.** Neither a larger disk nor
weaker active-goal verdict follows from these bytes. Unrestricted mock progress is
a concrete risk, but blindly retaining hold-maintenance after activation can
deadlock the existing continuation proof: maintenance_cutover.go:150–156 activates
queue/goal work before SendWithOptions, and c3c2 client.go:5375–5530 may steer the
continuation into that active turn. Accepted steer does not promise immediate
history materialization; its held predecessor can need a response. Conversely,
allowing an entire restored turn would not bound repeated same-turn inference.
Do not select a new response-gating protocol or clear/reset the tested goal on
this evidence. No R product/SDK correction or9085 contract revision is selected.

**Smallest releasable boundary is failure evidence, subject to main acceptance.**
One implementer, two existing fixture files, no new diagnostic framework:

- In test/creation_model.py, retain the one serialized row already needed by
  log.write. On append/open/close ENOSPC, print one compact stderr JSON record
  before re-raising the ORIGINAL error: request index/model/thread_id/turn_id,
  serialized ASCII byte length, requests.jsonl st_size/st_blocks/st_dev, and
  parent statvfs block/free/available plus inode/free counts. Catch diagnostic
  failures separately and mark unavailable; never replace the write error,
  manufacture a row or send SSE success. No raw input, tools or prompts. Do not
  add a second full serialization, salvage, retry or storage threshold.
- In nix/tests/session-creation.nix retained_state, when the active-goal check
  fails, print the saved/current goal fields and the already-read native thread's
  latest turn id/status/error and most recent failed turn if distinct. Reuse
  local data; no additional native call or mutation. Bound diagnostic error text
  with an explicit truncation flag, while preserving the complete copied native
  file and original assertion. Before existing failure exports allocate more
  guest files, use one ordinary timeout-bounded10s machine.execute read to print
  df block/inode data for the failing paths and du allocated totals for ONLY
  /tmp/creation-model, /tmp/creation-evidence, the fixture Codex home, portal state
  and /var/log. Print command status/unavailability, use no guest output file,
  preserve the original failure, and label this later sample's timestamp. This
  distinguishes journal versus snapshots/state/log allocation without a disk
  census or cleanup. Successful-case behavior is unchanged.

The missing discriminator is thus exact failing-filesystem free blocks/inodes
and journal allocation at the write, later named-consumer allocation, and the
native failure already present in the goal assertion's thread snapshot. A null
native error or incomplete totals must remain explicitly inconclusive. This
package improves evidence; it does not claim to reproduce or repair1207.

**One focused batch; no native or VM discriminator.** Reuse the existing extracted
Python/model helper recipe with temporary files and injected failures. Exercise
the actual Handler writer with successful append, ENOSPC on write and close, and
unavailable stat diagnostics; require original error propagation, one bounded
metadata record and no successful response after failure. Exercise extracted
retained_state with exact active-goal success, blocked-goal failure, and failed
diagnostic reads; all original identity/queue/history assertions and the original
failure must remain. Verify metadata omits input/prompts. Then existing Python/Nix
syntax, extracted embedded Python and real gxf-driver ty check testScriptWithTypes
gates, in the repository environment. Expected seconds;60s finite control ceiling,
first different failure stops. No repeated Go/SDK/HTTP/native/hold/selector/archive
checks for unchanged behavior; reuse their accepted scoped evidence.

Consolidate with the existing fixture/evidence owners (maintenance96c59622 and
diagnostic803c4419/453d48cd according to the final actual diff), preserving the
eleven-purpose history and accepted9085. No product API/schema/pin/budget/permission,
state migration, rollback or old-operation recovery change. Strict records and
full identity/count/text/history proofs, one assignment, uncertainty, Stop and
same-operation recovery remain mandatory. Main must accept this evidence-only
boundary before allocation; independently reviewed committed source and original
successor packaged acceptance remain required, but this brief selects NO rerun.
Space attribution, native blocked cause, final-case replay/acceptance and
repeated-final-setup-ci-loop remain OPEN. Only design.md changed; no checks,
application/Git/runtime effects or pending handles. Capacity returned; session open.

Design9227 interface clarification: the saved thread/read(includeTurns=true)
array has no established chronological-order guarantee in this brief. c3c2
turn_state.go:55–74 obtains “latest” through a different, explicitly descending
thread/turns/list query. Project `returnedLastTurn` and `returnedLastFailedTurn`
(last failed in returned array order), deduplicating the same element, with
original zero-based indices/count and exact id/status/error; label chronology
and recency unavailable. This supersedes “latest/most recent” above. No extra RPC,
timestamp/UUID inference or changed verdict. Implementer1's actual hunk owners:
goal projection96c59622/position5; model append90d97710/position9; pre-export storage
453d48cd/position10. Preserve all11 messages/authors and affected paired deltas.

## Exact66d4: lossless request-body encoding in the fixture journal

Sufficient source/design brief, 2026-11-08. Current/environment/fresh own roster
verified; retain architect0 Astra/xhigh/workspace_write/full_access. Prior effects
returned. Unchanged full guidance/documentation workflow reused (hashes match),
current records and exact R AGENTS read. Source66d4d0ed329d952aefa0e4faaaa140bd35e08322,
tree6df65b9b5051f0b16c23a220783054d56089c167; released creation-raw.stdout under
/tmp/lead-wakeup-R-publication-66d4-52ys8_89/ci has SHA256
f69aef27ec83dfd8828775909b58514149cf1ca885253e0709c766cba8394a5c.

**The missing allocation evidence is now obtained.** Raw11133 records request1122,
modelgpt-5.5, root01a1b9fa-e3a4-7db3-90b3-47af3b1b2cb8 and turn
01a1ba0e-8123-7643-ac3c-e271112ac251. Its7056028-byte ASCII row fails append
with ENOSPC11155; the journal already occupies3829403648 allocated bytes,
with only1355776 non-root-available bytes and260100 free inodes. Later11278
shows the model directory dominates named allocated totals:3829415936 bytes,
versus7.3MB evidence/39.7MB fixture home/2.7MB portal/19.8MB logs. The later
sample is non-atomic; it does not reconstruct every preceding write. This is
block-capacity exhaustion dominated by the fixture journal, not evidence of
inode exhaustion or a need to enlarge production budgets.

Raw11264 binds the SAME failed turn to the native error “stream disconnected
before completion: error sending request”, with saved active/current blocked
goal; array order/recency limitations remain. creation_model.py:133–165 appends
before hold/response and re-raises the write error. Failed evidence recording
therefore prevents this request's normal SSE response: a supported fixture
failure mechanism consistent with the same-turn stream error. Native's precise
goal-state transition reason is not printed. Trace12626–12627 maps to fixture
1026/718, the post-completion retained-goal check; final-case replay1027+ remains
unaccepted. These facts belong to66d4 only, not1207/93fd/f204.

**Selected correction, for main's material acceptance: one file.** Edit only
R test/creation_model.py. Keep request_evidence's current lossless projection of
model/input/client_metadata and keep the original raw request for all behavior.
Encode that projected BODY with Python standard-library gzip.compress
(compresslevel=1, mtime=0) followed by base64.b64encode. Store the ASCII result
as the outer JSONL row's body, with an explicit bodyEncoding="gzip+base64-v1".
The other four fields (index/provider/overload/retryAdvice) stay literal. Retain
one independently complete JSON object/newline per request under the existing
append lock. This is a small reversible representation adapter, not a streaming
compression/framing subsystem, index, rotation or storage service.

In request_rows, after parsing a complete outer JSON line, recognize that exact
encoding marker, strictly base64-decode (validate=True), gzip-decompress and
strictly JSON-decode the body. Require a dictionary as before, remove the codec
marker from the yielded row, and expose EXACTLY the previous decoded row shape.
Unknown marker, missing/string-invalid encoded body, invalid base64/gzip/CRC,
truncated compressed data INSIDE a newline-complete row, invalid inner UTF-8/JSON
or non-JSON constants must raise with the existing physical line/offset context.
Include codec exceptions such as EOFError/zlib.error in that wrapping; never
convert them into an empty body, skipped row or nonready observation. Preserve
legacy unmarked dictionary-body rows for already retained evidence. An unmarked
string body is invalid; do not sniff/fallback after a decode failure. Missing
original input/model/metadata stays missing inside the faithfully decoded body,
not newly synthesized. A marked row cannot silently fall back to legacy parsing.

The finite physical-size snapshot, original file/index order, every complete-row
validation and unfinished outer-line semantics stay unchanged: an incomplete
last OUTER JSON line is pending; a complete but broken codec payload is fatal.
No gzip stream is left open across requests. Append/open/close failure remains
fatal before any successful response. Existing ENOSPC diagnostics still report
the actual serialized ASCII OUTER row length, now encoded; do not confuse it
with decompressed body length or add another full serialization for diagnostics.
Use ordinary small helpers only as needed for the adapter; no new repository
framework or dependency. The implementation may retain the body serialization
once for compression. The actual request must never be replaced/mutated by its
stored or decoded evidence form.

**Why preserve the full decoded body.** This explicitly revises8943's on-disk
representation while retaining ALL its information and predicates. Exact66d4
has only six repository journal consumers, all through request_rows:

| Consumer in session-creation.nix | Required decoded evidence |
| --- | --- |
| held_model_request321–339 | index>after, exact model, role=user/type=input_text, exact full text membership; duplicate count and index order |
| naming_proof390–399 | exact model/provider and marker substring in json.dumps of the ENTIRE input; attempt count/order |
| resume_requests562–569 | original user-item order/last user, resume substring in that item's JSON, marker anywhere in full input JSON, matching indices |
| maintenance_model_requests732–771 | exact thread/turn metadata/model/index, user text/full-line marker, exactParts/markerLines multiplicity, complete-row count/maxIndex and ordered candidate suffix |
| resumed-model callback1013–1024 | resume text AND marker anywhere in the SAME input JSON, full-prefix validation even after a match |
| failure naming summary1495–1503 | model and index/provider/overload/retryAdvice in original record order, strict full-prefix scan |

Thus pruning assistant/tool/history, keeping only the last user, deduplicating
parts, storing only marker flags/digests or sampling records can change existing
assertions. gzip decoding preserves strings (including Unicode/escapes), nested
values, object insertion order, array order and absent fields, so the existing
json.dumps predicates retain their meaning. No consumer edits are required.
The shared archive fixture only launches this model (session-archive-lifecycle.nix242);
it has no additional journal reader. Holds/marker matching, naming advice and
archive repair inspect the ORIGINAL request, including tools and last user;
response/SSE content and request indices must stay unchanged.

The concrete need for encoding is the observed multi-gigabyte duplication of
request histories on a finite guest disk. Per-body standard gzip avoids changing
outer JSONL commit semantics and preserves information unlike a compact custom
selector index. A single long-lived gzip journal would complicate finite-prefix
and incomplete-tail handling. Larger disk, truncation, deletion, rotation,
response gating, goal edits and product/SDK changes are not selected. This
reduces stored-evidence amplification; it does not reduce actual inference or
claim constant space for arbitrary incompressible/unbounded requests. Decoding
still processes one full body at a time. Original acceptance must establish the
remaining real workload fits; no historical compression ratio is invented.

**One finite affected check batch.** Reuse the existing direct Handler/temporary
file and extracted consumer recipes (released66d4 source receipt points to
/tmp/lead-wakeup-R-failure-evidence-ugl7qy80/model-controls.py and extract.py).
Adapt those controls in the implementer's own check directory, not the released
packet. No HTTP/native/server/VM harness. Exercise:

- Actual Handler writes and request_rows round-trip of all projected body fields,
  including nested non-user text, key order, Unicode/escapes, absent keys, repeated
  user parts, multiple users and exact metadata. Compare all six extracted
  consumers' original/plain versus encoded observations, including wrong
  model/role/thread/turn, after-index, duplicate matches, naming attempt order,
  full-input versus last-user and strict trailing-corruption cases. Keep actual
  Handler raw-request/hold/SSE and archive repair inputs unchanged in these finite
  injected controls; do not replay native/archive acceptance locally.
- One representative approximately7MB input with repeated history and varied
  exact marker/metadata fields, streamed through a small fixed set (e.g. eight)
  of actual appends. Compare actual encoded journal bytes against calculated
  unencoded row lengths; require substantial reduction (at least10x for this
  deliberately repetitive control) and exact decoded equality. No production
  size/ratio threshold. The isolated66d4 writer must fail this storage-amplification
  control; never fill host disk or manufacture ENOSPC by volume. Do not call the
  generated body the missing original request1122 bytes.
- Legacy and encoded rows together; finite-prefix growing outer tail; complete
  invalid base64/gzip/CRC/inner JSON before and after a valid match; incomplete
  compressed payload with a complete outer newline is fatal. Preserve all outer
  shape/encoding/non-JSON-constant/read errors. Reuse affected ENOSPC open/write/
  close/stat-unavailable controls with actual encoded serialized length; require
  original exception identity, no successful SSE and no payload in diagnostics.

Run once inside the existing repository environment: `timeout 60s nix develop
--offline --no-update-lock-file --no-write-lock-file --option max-jobs 0 --option
builders '' --command bash <owned-quick.sh>`, containing the adapted finite
Python controls, Python syntax and scoped diff checks. Expected roughly10–30s
with cached environment; first different failure or60s stops for disposition,
not another exploratory campaign. Nix/testScript/driver types are unchanged:
reuse the accepted66d4 syntax and corrected type-only proof, and reuse unchanged
Go/SDK/HTTP/native/sync/Stop evidence in its actual scope. If implementation
requires a consumer/Nix edit, return that material deviation before expanding.

**Release and compatibility.** Main can allocate this complete one-file package
once this explicit representation revision is accepted. Consolidate with actual
fixture owner4c4f038f (position9), preserving earlier maintenance/product9085,
diagnostics and all eleven author/message purposes. Standard-library-only;
no pin/API/permission/schema/product-state/deployment/rollback changes. New reader
accepts old plain logs; old readers cannot read new encoded logs, so writer and
reader ship atomically in this SAME fixture module. Logs are disposable evidence,
not persisted product state; do not convert old logs or claim old packages can
consume the new artifact. Preserve full native histories and all current storage/
goal diagnostics. No extra send/retry/ID, changed timeout/hold/goal, weakened
uncertainty/Stop/retained-active/recovery/replay assertion or artifact cleanup.

After focused checks and committed owning consolidation, require independent
affected review and main-selected original successor packaged acceptance through
all18 cases, including final retained ACTIVE goal and completed-recover no-duplicate
replay. This design does not authorize publication/run. Current66d4 final-case
acceptance and repeated-final-setup-ci-loop remain OPEN. No essential source
contract blocks this one-file correction; original workload acceptance is the
remaining runtime dependency. Only design.md changed; no checks/application/Git/
runtime effects or pending handles. All effects/capacity returned; session open.

## Exactdde23212 archive setup: wait on definitive worktree admission

Sufficient bounded disposition, 2026-11-08. Current/environment/fresh own roster
verified; architect0 retains Astra/xhigh/workspace_write/full_access and has no
prior pending effects. Unchanged full lifecycle/verification/documentation/team
procedures reused; current plan/state, accepted9370 and exact R AGENTS read.
Source dde232129d4b59c1431160c4cabebb2d804a08b5/tree87e093e23a981961e13fc7080c9151489bdc6824;
released archive-raw.stdout under /tmp/lead-wakeup-R-publication-dde23212-rlcwvs37/ci
has SHA256c4d6855c5c8afd16f372dac307572ed2399ab3afdf672564ec2815c172f7d0d6.
Only this terminal archive evidence was inspected; implementer2 retains ongoing
original CI observation. Fast/creation acceptance is not inferred.

**Demonstrated mismatch.** session-archive-lifecycle.nix266–287 starts the native
lead, observes idle, GETs retry-policy, then runs a separate shared flock probe
before worktree add. Raw4437/4445/4449 show those preceding commands completing;
4450–4453 shows SH acquired and RELEASED. Command4454 subsequently refuses at4457
with exactly `error: another dev-session command is changing 2026-10-25-lead-archive-repair`
and exit1. Casefatal4460 is before creating the repair blocker, browser archive
submission, lead repair or portal-restart/recovery assertions. No archive operation
for this case was admitted. Model-refresh diagnostics4358/4456 are separate.

libexec/dev-session:2804–2809 takes the slug EX lock before worktree registration,
fetch, checkout or tmux sync. with_slug_lock8457–8475 resolves session_lock_file
8315–8320 to the same runtime authority/<slug>.lock. with_host_lock8282–8304 first
tries nonblocking EX; worktree_add's wait_for_readers=true permits waiting only
if its own subsequent SH probe succeeds. A failed admission raises SessionBusyError
before yielding. CLI9916–9918 prints the exact refusal/exit1. Errors from commands
AFTER admission instead include CommandError's command/exit context (261–277);
worktree_add/sync_slug do not reacquire this slug lock inside their mutation.
The externally observed SH success is neither an EX reservation nor a promise
that a writer cannot arrive before the command's own probes. Precise holder and
continuous ownership timing are not printed and are not required to correct
that invalid readiness assumption.

The fixture comment “finish that checkpoint” is too strong. GET retry-policy
only loads the persisted policy (web/turn_retry_policy.go64–75). Background retry
bootstrap can already have observed missing policy (turn_retry.go215–219), then
wait for EX and recheck the saved policy AFTER acquiring it (policy.go121–149).
It can therefore contend after a successful GET. Other ordinary lifecycle/setup
writers share this exclusion; source possibilities do not identify this run's
holder. Runtime LockRuntimeExclusiveContext uses the same .lock (authority.go63–70).
The stopped tracking-sync timer does not stop portal background admission. Product
writer refusal is intentional, also covered by the existing named
Test-style Ruby method test_worktree_mutations_use_the_slug_lock in
 test/dev_session/tmux_runtime_test.rb:62. No product lock/admission defect is
established.

**Selected one-file fixture correction, for main acceptance.** Edit only
nix/tests/session-archive-lifecycle.nix. Replace this case's detached SH probe
and one-shot worktree add with a small local worktree-admission helper. It invokes
the SAME original command/slug/project/options and captures combined stdout/stderr
using machine.execute. Only `(exit=1, output=exact same-slug refusal with at most
its single final newline)` means definitively not admitted and may return False
from the ordinary driver retry callback. Exit0 returns True immediately, so
there is exactly one successful registration and no post-success re-entry.
Any other status/output, extra warning, wrong slug, signal, transport exception,
command timeout or malformed driver result raises immediately and is NEVER
reissued. Do not substring-match, trim arbitrary output, catch all errors or
turn an uncertain process result into contention.

Use the existing driver's retry callback and the30s allowance already assigned
to the removed flock probe; no new duration, explicit sleep or product timeout.
The callback's final `last=True` call must raise with attempts/last status/output
WITHOUT invoking worktree add again. Retain the existing per-command driver
execution timeout; this bounds repeated refused admissions, not the duration of
a successfully admitted Git command. An in-flight command is never assumed
unsent merely because the admission wait expired. Preserve/report failures with
the command and compact last observation. The retry-policy GET/idle checks may
remain as their actual observations, but cannot be described as reservations.
Use this helper only for this demonstrated native-lead setup call; do not expand
all fixture commands or other cases to retry. The existing creation fixture's
sync_source198–229 is the precedent for exact pre-admission handling, not code
to generalize into a common framework.

This is a fixture admission correction, not changed product retry semantics.
Each refused attempt entered none of the worktree mutation block. Every admitted
attempt still runs ALL lifecycle/provider/generation/identity checks under its
own lock, and every later failure stops the test. The same native root/goal and
one initial Send remain; repair model hold, one browser archive receipt/attempt,
restart, agent shutdown, committed-content restoration and all later assertions
are unchanged. No external lock is held across the CLI (which would conflict
with its independent EX lock); no lock is cleared or bypassed. Moving worktree
creation ahead of the first native start would instead require committed
tracking-only conversion/absence proof (dev-session3652–3667), an unnecessary
setup-path change. Sleeps, wider budgets, generic retry-all and holder diagnostics
are not needed for this exact refusal contract.

66d4..dde23212 changes only creation_model.py. Archive/product lock bytes are
unchanged; the codec changes journal representation before SSE and may alter
scheduling, but does not acquire this authority lock or promise its availability.
No historical holder or timing cause is attributed to it. Keep accepted9370
lossless/strict decoder and9085 fresh-acceptance/Unknown boundaries unchanged.

**One finite focused batch.** Extract the changed fixture helper with the existing
Python fixture-check recipe and actual gxf driver retry implementation. Inject
returned command outcomes, not a native/server/VM harness. Require exact busy
then success (one successful invocation, same argv each time); direct success;
wrong slug/extra output/other exit and transport/timeout exceptions (one call,
no retry); persistent exact busy through a simulated driver deadline (fatal,
no final `last=True` invocation). Use a fake clock/driver interval in controls,
not wall-clock sleeps. The original one-shot setup must fail the busy-then-success
control; the new helper must still reject every non-admission error. Run the
existing `ruby test/dev_session/tmux_runtime_test.rb -n test_worktree_mutations_use_the_slug_lock`
as the small owning-lock check; do not broaden Ruby/Go suites. Run Nix syntax,
extracted Python and real-driver `ty check testScriptWithTypes` for this changed
archive script, plus scoped diff checks. One repository-environment batch,
expected10–30s/60s control ceiling, first different failure stops. No actual
archive/lifecycle/native action is needed for the focused batch.

The archive fixture is unchanged in the current feature series (last owning
commit95a53aed); use one focused fixture-fix commit rather than fold this into
model encoding/product history or rewrite the preserved baseline purposes.
No API/pin/persisted-state/migration/permission/deployment or rollback change.
After main accepts the brief and allocates implementation, require committed
focused results and independent affected review, then separately selected
original packaged archive acceptance including this complete repair/restart
case. Current original fast/creation remain with their observer; no cancellation,
replacement or successor run is selected here. Exact holder remains unknown,
but is not a release blocker for the narrow definitive-refusal handling. Only
design.md changed; no checks/application/Git/runtime/CI effects or pending handles.
Capacity returned; session open and repeated-final-setup-ci-loop remains OPEN.


### Finish-path reconciliation at published8a810: consumer preparation is ready

2026-11-08; bounded update to design3869–4017, no new product design or gate.
Current/env/fresh own roster match; architect0 retains Astra/xhigh/workspace_write/
full_access, with no prior pending effects. Main accepted originaldde23212 fast
and creation18/18, including ACTIVE-goal preservation and completed-recover replay;
its archive failed before admission. Published successor R
`8a810ba0b977fa24de218f7621dfee61d7f8f370`, tree
`e47c2f9c17728cd3cf325e0f713bc1181aaa1dbd`, changes only the archive fixture from
that parent. Released publication.json under
`/tmp/lead-wakeup-R-publication-8a810ba0-oojvjfkb/` confirms publication and returned
Git windows. Original42464384422 remains exclusively B/watcher6747-owned; no CI
state was inspected here.

**Ready package.** W/C pin preparation may proceed during that original run:
reviewed runtime/product contracts and exact publication are settled; independent
consumer files do not affect the running immutable CI or activate a package.
This supersedes design3869's sequencing that withheld consumer preparation until
the whole VM result. Main can allocate one complete W+C composition package to
one available implementer; two owners are safe only with disjoint repositories
and one named final cross-check owner. No product/SDK/catalog work is required.

Read-only current bindings (both worktrees clean): paths share prefix
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-03-lead-wakeup-delivery/`.

| Consumer | Path and current head | Selected contract |
| --- | --- | --- |
| W | `workspace`, `66ca9c64d165e3adc02e52f49948d55edeb40e28` | `flake.nix` nested `vpsfree-dev-workspace/dev-workspace` selects Rf161ede8a6ea4cf540edcb7ece81ebb76f064a05. Preserve reviewed/published observer addition66ca and all prior guidance. |
| C | `vpsfree-cz-configuration`, `e3f942e6d2c9449ce02782a388f3ef9202fbbf05` | `flake.nix:134` channel `dev-workspace`, role/root input `devWorkspace`, locked to the same f161; aitherdev module declares that channel and config imports its host module. |

W extension remains `f8da821e3c76e26e73aa9d89a712eab0e0faa319`, NAR
`sha256-U5y/TEny6nsyXWNlCMktmxTZhpVO0QY4kOo/qgwsapM=`; root nixpkgs follows
`["vpsfree-dev-workspace", "nixpkgs"]`. Preserve extension/siblings/follows, no
new top-level runtime or extension-lock edit. Both old consumers select SDK
`d3a29bee90ef00a08816920408c596152339a637`; importing final R's lock intentionally
selects accepted `c3c2adb705f5ff6bb42c98bd44be3649fd93bedb` (NAR
`sha256-oXED0TaBUsl4cyKXgQ8JNGCVAO6Xck95MUjHI4WHUzk=`). Runtime llm-agents
`91ff550fe42d4dd51dcf8b6bad87a0134fe7f314` and nixpkgs
`a5cc6f2c37bf518436dc8d1c288ccd0c43c2f4c4` match in old W/C and final R; this
supports preserving stock0.165 selection, not claiming final binary equality.

Implementation boundary: W changes only the existing nested URL in `flake.nix`
to exact8a810, then `nix flake update vpsfree-dev-workspace/dev-workspace` generates
`flake.lock`. C runs `nix develop --command confctl inputs channel set --commit
 dev-workspace devWorkspace 8a810ba0b977fa24de218f7621dfee61d7f8f370` (one command,
without the displayed line wrap), generating its `flake.lock` and genuine history;
no manual lock edit. Inspect semantic graph changes against R's published lock,
not node labels; unrelated drift stops the package. Use existing branches and
preserve observer content, prior source refs and rollout receipts. No rebase
baseline is selected here; an upstream/conflict decision returns to main. Retain
one final logical pin update per stream under existing consolidation policy,
with generated C history preserved and affected whole-series/history review.

One focused preparation batch: Nix syntax/semantic lock checks, existing W
`deployment-contract` test and ordinary hooks, then exactly one final
`bin/check-dev-workspace-deployment --workspace-root W --configuration-root C`
after both locks settle. Preserve runtime/extension/follows and all W additions;
no schema/API/migration or new rollback policy. Commit/publish feature sources
under main's windows and obtain the existing affected composition/history review
before long artifact checks. Expected source/quick work is minutes; reassess at
10 minutes without a concrete phase result, stop at first actual failure or
binding drift. Do not replay unchanged Go/SDK/native controls as pin checks.

**Remaining acceptance, using the existing inventory rather than another campaign:**

- R29 remains the declared14 Ruby shards + aggregate + ten non-VM + four VM
  checks (`flake.nix:95+`, `nix/ruby-checks.nix:42+`). Current workflow fast covers
  the25 non-VM outputs; archive/creation are separate, host VMs are feature-push
  skipped. B's original run supplies its own results. Bind final attributes to
  retained successful DRV/input/output/NAR receipts; run only unresolved outputs.
  In particular `host-module-idempotency` and `session-recovery-boot` need that
  explicit disposition. The f161 `receipts/canonical-result.json` and binding/
  derivation/output/Ruby records under `/tmp/lead-wakeup-runtime-checks-f161-gli552zj/`
  are a comparison source, not final acceptance. No current reuse count is known;
  do not rerun successful creation merely to fill the map.
- Native5: retained40b result `/tmp/lead-wakeup-native-40b41eac-d0i4dh4c/result.json`
  proves five passes/21.866s at its exact source/native. Its five file hashes are
  not a complete final-input binding. Settle cheap equivalence of exercised inputs
  or use the existing `TestNativeWorkspaceBoundedPause` command from design3869
  once against final inputs; no new fixture or mode.
- W6 remains `tracking-source`, `deployment-contract`, `storage-retention`,
  `agent-instructions`, `agent-team-policy`, `cluster-provider-composition`
  (current W flake). Complete/bind all six on final W, avoiding repeat of a quick
  result when its exact derivation/input/output already qualifies.
- Build final W `.#default` and C's named `confctl build
  cz.vpsfree/machines/aitherdev` artifact through the existing commands in3869.
  Preserve rooted package/toplevel, exact graph/closure/NAR/derivation and native/
  catalog/launcher evidence. Final W feeds the unchanged eleven-mode
  `TestNativeMonitorOperation` acceptance from3869. Old
  `/tmp/lead-wakeup-candidate-f161-W1b219-sgtavp_i/receipts/final-verification.json`
  binds only Rf161/W1b219, its Prbx package, native11, W6 and Ce3 host generation;
  none establishes the final consumer graph. No final artifacts are claimed yet.

These unresolved bindings are acceptance work, not blockers to the pin package.
Retain serialized heavy-resource scheduling, existing watcher policy and first
failure stop; no automatic rerun or optional verification inventory. Live rollout
stays gated on accepted original successor CI, final applicable checks/artifacts/
native proof and the existing deployment preflight. Preserve host-first/profile-
second and operation-owned forward recovery; C supplies the host contract, W the
user-profile application. Current deployed profile, host generation, claim and
unfinished operation state were not queried and remain to be freshly bound by
main before activation. Old summaries cannot establish them. Existing deployment
direction is retained; no default integration, claim release, lifecycle action
or cleanup is granted. Only design.md changed; no evaluation/check/build/Git
mutation/runtime/CI effects or pending handles. Capacity returned; session open.


### Final rollout command boundary: R8a810 / Wb78ed11f / Cac90ea87

2026-11-08; existing finish path only, after design9655 and accepted review40846dec.
Identity/both env markers/fresh own roster verified; retained Astra/xhigh access,
no prior effects. Publication/artifacts belong to implementer1; recovery VM11034
and original CI6747 were not inspected. Final artifact gates and14:55UTC cutoff
remain main-owned. Reuse design943–1055,1340–1468,3530+ and terminal receipts in
`/tmp/lead-wakeup-aitherdev-rollout-c2n4xj47`; no new product or check requirement.

**Invoker decision.** The initial profile cutover still requires the recorded
external user shell and a coordinated idle window, including this active lead
and team. Main can perform the authorized host stage first, then prepare the
foreground handoff and end its turn. It cannot use the final candidate to
bootstrap automatic pause from this active session. Selected zmy's immutable
`share/workspace-portal/runtime-contract.json` has reporting2 and no maintenance
schema/policy. R8a810 `libexec/workspace-maintenance.rb:116` skips the worker for
that predecessor; `workspace-host:697–699` refuses premature
`--enable-maintenance`. Candidate activation still quiesces through selected zmy
(`workspace-host:751–772,2513–2556`). The first-upgrade paragraph in
`docs/workspace-updates.md` explicitly requires this idle transition.

The accepted reporting2-to3 admission exception remains the public
`P_FINAL/bin/workspace-host switch --source W --from-candidate` from design1340;
it is not an idle bypass. Its executing package must equal the unselected output
built from W, with unchanged profile token, transition lock, source/registry,
compatibility and held-claim checks (`workspace-host:650–747,3581–3593`;
`docs/workspace-portal.md:1078+,1131+`). No bridge, override, timer, private helper,
forced stop or active-lead background launcher is selected. After successful
selection and completion, ordinary same-source `--enable-maintenance` is supported
by the now-capable source; it may use the existing bounded worker, without a
second special MCP installation or native upgrade.

**Reconcile the original attempts before authorizing a final invocation.**
`profile-switch-refusal.json` records ordinary switch09:16:46–09:16:54Z exit1 at
the communication guard, before selection. `candidate-idle-refusal.json` records
attempt1 exit1 after drain/quiesce admission; `candidate-recovery-2-failure.json`
records attempt2 09:59:52–10:01:36Z exit1, unsupported native-status shape, again
before selection. Both had restoration activity; no blanket no-effects claim.
The latter retained schema1 `/home/aither/.local/state/dev-workspaces/codex/pending`,
SHA07dc9996cb0d669b3d7f53e03b56fa721d8d1659b0d7693a4be9820eea279f56, target
`/nix/store/rbxh3i5sqqc8j6ms0qhkggfd9m68wnp7-dev-workspace-0.2.0`, with its Codex
wrapper and registration identities. Preserve every original log/status/root;
none of these terminal failures authorizes another launch automatically.

Main's necessary fresh preflight, using public status and narrowly scoped own
recovery metadata, is: selected profile/token and active/profile Codex; exact
claim5ed5527b-c5b0-42fe-8d2d-53aacf27fd81 still held and current C machine mapping;
original command effects/host system links; any owned coordination attempt/job,
integration or lifecycle fence; exact pending target metadata and maintenance
startup/active-operation state. `workspace-host status` does NOT expose pending
or startup state (`workspace-host:1525+`). Read only metadata of the known pending
record and, if present, `maintenance/startup.json` (schema/operation/profile/
source/target/token/phase), without communication payloads or peer files. Use
public `workspace-host maintenance status [UUID]` through the capable package for
operation disposition; its controller routes by retained `SourcePackage` before
schema interpretation (`maintenance_control.go:109+`). Do not infer absence
from an unsupported old CLI command. Main already reported selectedzmy/heldclaim/
no jobs or fence; that is not the missing pending/startup inspection.

If fresh evidence confirms zmy remains selected, no startup/maintenance/legacy
operation owns recovery, and only the ordinary preselection Prbx pending record
remains, a deliberately approved final source-bound candidate switch is the
existing forward-to-newer-package path (README:91–93). It revalidates everything
and writes its own pending target through normal activation
(`workspace-host:750–805,3515+`); it is not a replay of attempt2 or a manual record
rewrite. Do not call zmy `reconcile-codex` against a different pending target:
`workspace-host:2314–2318` refuses that mismatch. If selection has advanced, use
the selected forward package's recovery, never the unselected entry. Any actual
unfinished maintenance operation keeps its original UUID, source owner, saved
phase/deadline/delivery IDs and claim via `maintenance recover UUID`; historical
schema1 is not converted to schema2. A pending startup grant also retains its
own activation/recovery; `prepare_profile` refuses a new switch. Missing owner,
changed target or uncertain effects returns to main rather than this template.

**Literal template after gates/preflight and main's release.** Fill only the
reviewed artifact values; the host commands run in C's declared Nix environment,
under the existing held typed claim, with ordinary health/auto-rollback enabled:

```sh
C='/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-03-lead-wakeup-delivery/vpsfree-cz-configuration'
W='/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-03-lead-wakeup-delivery/workspace'
P_FINAL='/nix/store/<final-reviewed-composed-package>'
GEN_FINAL='<final-Cac90ea87-named-generation>'
export DEV_SESSION_SLUG=2026-11-03-lead-wakeup-delivery
export DEV_SESSION_WORKSPACE=/home/aither/workspace/ai/vpsfree.cz
export DEV_WORKSPACE_CLAIM_ID=5ed5527b-c5b0-42fe-8d2d-53aacf27fd81
cd "$C"
nix develop --command confctl deploy --generation "$GEN_FINAL" --copy-only cz.vpsfree/machines/aitherdev
nix develop --command confctl deploy --generation "$GEN_FINAL" cz.vpsfree/machines/aitherdev dry-activate
nix develop --command confctl deploy --generation "$GEN_FINAL" cz.vpsfree/machines/aitherdev switch
# Continue only after host command/effects/health and both system links verify.
# The following initial cutover is run by the external user in the idle window:
"$P_FINAL/bin/workspace-host" switch --source "$W" --from-candidate
# Only after successful selection/completion and no unresolved operation:
workspace-host switch --source "$W" --enable-maintenance
```

These are ordered phases, not an unconditional shell script: stop at any nonzero
or uncertain result. Use the existing foreground no-clobber log/start/end/exit
capture pattern with a fresh basename; do not overwrite attempts1/2 or append a
retry loop. Initial cutover omits `--enable-maintenance`; the subsequent ordinary
command uses the stable selected launcher, same exact source and claim. Record
its operation UUID immediately if emitted. Public `maintenance status UUID` and
`maintenance recover UUID` retain that operation; never rerun switch to replace
it. Source-owned recovery applies equally if the caller disappears during the
native restart. Host deployment is a no-op only with proved identical final
system output, not the old Ce3 receipt.

Existing success/effects/usability verdict stays unchanged: actual final system
and user-profile targets, native registration/socket readiness, terminal command
and rollback effects, restored stopped clients and any complete original
operation; portal/router health, naming, conversation continuity, retained
settings/reporting, and one bounded owned live monitor outcome that wakes the
idle lead with actual receipts. No disruptive live failure injection or second
acceptance campaign. Preserve queues/goals, explicit Stop, stable resume IDs,
forward-only state and all full branches; fallback is main's separate-branch
choice under14:55UTC. Current uncertain binding is the fresh pending/startup/owner
state, not an unimplemented command interface. This note grants no activation,
integration, claim release or lifecycle permission. Only design.md changed; no
checks, probes, CI/VM observation, runtime/Git mutations or pending handles.
Capacity returned; session stays open.


### Final C artifact availability: restore the exact retained derivation once

2026-11-08; current/env/fresh own roster match, settings retained and prior effects
returned. R29/native5, final W6/configured package/native11 remain accepted. This
is artifact preparation for unchanged Cac90ea870bdbd2193241f07df970cbb143e4fffe,
not a runtime failure or fallback decision. Only terminal receipts and narrow
local source/own metadata were read; no store query, execution or remote probe.

**Observed versus explained.** Under
`/tmp/lead-wakeup-WC-final-8a810-hvx2afyo/`, C-host.json/stdout record natural0 in
113.782s,09:43:09–09:45:03UTC, and generation2026-11-08--10-43-41. C-generation.json
binds R8a810 and TOP
`/nix/store/c8lyg8zdzd0i6m80ix4mzkcw0v2bkqw2-nixos-system-aitherdev-26.05.20261026.718f670`.
C-artifact-path-info.json maps TOP to null despite command exit0; no earlier
positive TOP NAR exists. C-root-failure-reconciliation.json confirms TOP absent,
W candidate retained, rollback helper present; all commands are terminal.
C-root-toplevel.json/stderr records --realise TOP failing without a build recipe.
Neither natural0 nor generation.json establishes current artifact availability.

Pinned confctl7bee58a52372b95c2198ce3f2a719807a3c2c66b explains the missing inner
log: `lib/confctl/cli/command.rb:20–24` calls Logger.close_and_unlink after success
unless explicitly retained. C-host.stdout survives as the original outer log.
No storage fault or GC inference follows from the inner log's removal.

`NixFlake#build_attributes` calls `nix build --json --no-link` for this machine's
toplevel/autoRollback through local `SystemCommand`, then evaluates output paths
and saves the generation (`lib/confctl/{nix_flake,nix_build_flake}.rb`). This path
selects no separate --store, build host or SSH endpoint. The captured command has
no such option; later reconciliation env has NIX_REMOTE/NIX_STORE_DIR/NIX_STATE_DIR
absent. There is no evidenced remote-only output or identified remote store to
query. Nix may use configured distributed builders, but the retained outer log
does not identify one or prove historical realization location; do not guess a
host. Source/default behavior expects realization in the invoking Nix store.

`Generation::Build#save/add_gcroot` creates generation symlinks/JSON, then
`GCRoot.add` adds per-user links under `confctl-<SHA256(real C path)[0:8]>`.
Read-only inspection finds this exact chain still present:
`/nix/var/nix/gcroots/per-user/aither/confctl-0ec34411/`
`cz.vpsfree:machines:aitherdev-generation-2026-11-08--10-43-41-toplevel`
points to C's `.confctl/generations/cz.vpsfree:machines:aitherdev/`
`2026-11-08--10-43-41/toplevel`, which points to absent TOP. The same generation's
rollback/input links and own corresponding roots resolve. Thus empty query-roots
output does not prove confctl omitted its root. Source has a no-link build to
post-build-root interval, but no event here proves GC in that interval, later
root loss, corruption or another cause. Aitherdev retention guidance preserves
confctl roots and documents pressure GC; it is policy, not evidence that GC ran.
The precise disappearance cause remains unknown and does not block restoration.

**Minimal released-boundary proposal for implementer1, main to allocate.** The
exact retained derivation is a regular7585-byte file whose raw `out` mapping is
exactly TOP:
`/nix/store/n2aqnp54ml2zf5xhdkrxkd23j8h890ac-nixos-system-aitherdev-26.05.20261026.718f670.drv`.
Use the same ordinary Nix tool/configuration once, realizing the derivation and
rooting its output in that operation; preserve all original failures and metadata:

```sh
/run/current-system/sw/bin/nix-store --realise   /nix/store/n2aqnp54ml2zf5xhdkrxkd23j8h890ac-nixos-system-aitherdev-26.05.20261026.718f670.drv   --add-root /tmp/lead-wakeup-WC-final-8a810-hvx2afyo/C-host-root --indirect   --max-jobs 4 --cores 4
```

The previously failed owned root is absent in the retained receipt; recheck that
specific path before dispatch and do not overwrite a new/conflicting link.
Confirm the retained derivation/output mapping and exact source receipts, capture
natural exit/full stdout/stderr externally, and retain existing NIX_CONFIG/cache/
trust/builder settings. This may substitute or rebuild missing outputs; it does
not rerun confctl evaluation, create another generation, change pins or replay
checks. No source fix or provider upgrade is selected.

After success, require exactly TOP, positive non-null path-info with its actual
NAR/deriver, resolving owned root plus generation link, and the existing complete
host source/input/closure/rollback receipt. This becomes the first positive TOP
availability/NAR observation; do not claim equality to an unrecorded earlier NAR
or retroactively repair the old metadata failure. Preserve the named generation
and rollback root. Expected work is seconds to a few minutes given the original
114s build; fresh ordinary watcher for uncertain duration,10min reassessment,
first nonzero/output mismatch/unexpected kernel build stops. Missing derivation
or changed source/store identity returns to main; no automatic confctl rebuild,
remote search, cache/trust change or retry loop. This is the only required batch
for this artifact gap; passing R/W/native evidence remains closed. Deployment
still follows accepted gates/preflight, cutoff14:55UTC and intact full branches.
Only design.md changed; no command effects or handles remain. Capacity returned;
session open, no next task assumed.

### Full-feature startup-only repair and original a3e29943 recovery

2026-11-08; sufficient implementation brief for main's allocation/acceptance.
The user's “since we have it deployed already, fix it” supersedes fallback,
automation removal and cancellation-only proposals, including the earlier
14:55 fallback selection. Keep full R8a810ba0/Wb78ed11f/Cac90ea87 and their
original refs/worktrees intact; make the repair a forward successor. Current,
both environment markers (absent), trusted session binding and fresh own roster
match; architect settings retained. Documentation workflow applies. This brief
authorizes no live action and creates no application changes.

**Demonstrated boundary.** The final profile cutover succeeded and selected
`/nix/store/0d9006b9dqfxs70y63daq08cgc3pxjzv-dev-workspace-0.2.0` (P).
The separate enable invocation in
`/tmp/lead-wakeup-aitherdev-rollout-c2n4xj47/final-maintenance-enable.{json,stdout,stderr}`
ended1 at14:45:59UTC after24.210s. Its ordinary probes passed, timers were
disabled, and startup-reconcile refused operation
`a3e29943-46d2-447b-8a6d-6adc051252cd`. R8a810
`workspace-host:750–789` places this refusal before native adoption and private
activation; this invocation did not stop native or select another package.
Its terminal process group is absent per main's reconciliation.

The exact schema1 startup selection remains pending, enabled=false/target=true,
candidate=P, source=authorized profile token
`9a7d8e07c5f7ad5b751c000a6e405007b829b014004ead91dd677f2129a28738`.
Its sole sequence1 grant is unconsumed: workspace-codex@vpsfree-cz.service,
this workspace, native
`/nix/store/2rqwqchjlv6l2nw5l491pkhvrsijn50c-codex-package-0.165.0/bin/codex`,
digest3b9da3cc0df10c909955b84dd2f55537d8b309347095d04fb3bff38bf451c23d.
The operation directory is absent. The earlier matching schema1 codex/pending
was absent on the latest narrow read. Main reports no intervening mutation;
`pending-disappearance-boundary.json` preserves this unknown-cause change.
Absence is neither completion nor permission to reconstruct that record.

`portal/cmd/workspace-portal/maintenance_startup.go:129–159,210–227` requires
Load(operationId) in both consume and reconcile. Ordinary same-package enable
intentionally has no full operation (`workspace-maintenance.rb:116–121,215+`).
Thus the immediate refusal precedes native/environment proof. Independently,
`internal/maintenance/startup.go:94–113` requires every grant to have a ready
invocation although the accepted same-package path needs no restart.
`test/workspace_host/maintenance_test.rb:108` checks preparation only. Fixing
Load alone leaves the completion defect. This is an R ownership mismatch, not
an SDK/native fault. Public recover currently starts the full-operation worker;
new switch refuses pending startup. Neither owns this recovery today.

**One R implementation package.** Own `libexec/workspace-maintenance.rb`, the
necessary dispatch/completion seams in `libexec/workspace-host`,
`portal/cmd/workspace-portal/maintenance_{startup,control}.go`,
`portal/internal/maintenance/startup.go` and its request type in `types.go` if
needed, their existing startup/control/Ruby tests, the bounded maintenance-setup
addition in `nix/tests/session-creation.nix`, and `docs/workspace-updates.md`.
Use one cohesive follow-up commit; do not rewrite
the published full-feature series. No SDK, model, queue, monitor, pause/resume,
Stop, runtime catalog or host-module redesign. One implementer owns this seam;
W/C pin composition is a dependent mechanical package after R review/publication.

1. Resolve startup authority explicitly. An existing operation, including
   historical schema1, always keeps immutable SourcePackage routing and its
   activation/participant/source-epoch proofs. Startup-only means the exact
   operation directory is genuinely absent, not merely Load failed. Malformed,
   partial, unavailable or foreign owners refuse. For startup-only, bind the
   strict saved startup, ID, selected candidate, authorized current profile
   token, complete registered grant set and native/registration plans. Retain
   the host transition exclusion and ordinary lifecycle/coordination admission.
   Fix consume and reconcile together; actual new native launches still require
   exact systemd invocation/PID/cgroup proof and the one-use grant before exec.
   Do not fabricate an Operation to feed the full-operation branch.

2. Add a narrow internal `startup-observe-existing` action for startup-only
   no-restart activation. The host first uses existing full registration
   semantics and live-package/reporting compatibility, then supplies the exact
   grant and SHA256 of the observed launch-marker bytes. This ephemeral request
   field is not persisted in startup.json and is never sent to an old operation
   owner. The controller re-reads that same marker and validates registered
   workspace/unit/native identity; use the existing unit, process identity,
   boot, cgroup, listener ownership, socket epoch and passive LoadedThreadIDs
   readiness proof, with repeat identity/marker observations before saving.
   Preserve `marker_has_semantics?`/`registration_argv_equivalent?` compatibility:
   an unchanged running invocation may retain a supported older launch-package
   marker. Do not rewrite that marker or demand a restart solely for its path.

   Save a directly observed **ready** StartupAttempt with the actual invocation,
   PID/process identity/boot/cgroup/executable/socket epoch under the original
   grant and sequence. This is an observation of an existing process, not a
   fabricated consumed-before-exec event or a new launch. Under the store lock,
   compare the complete saved selection/grant snapshot and require an initially
   unconsumed sequence1/no-attempt grant; never overwrite consumed/failed/ready
   evidence. Replays validate the identical retained ready invocation. Real
   consumed attempts use existing reconciliation, including positive failure
   proof before replacement. Finish retains its all-grants-ready requirement.
   Startup JSON remains strict schema1 with its existing fields/dispositions;
   old readers can read the directly observed ready proof. This explicit
   semantic extension replaces the mistaken assumption that every ready
   invocation must have been newly launched by the enable command.

3. Ordinary same-package enable observes already-running matching units through
   this action, leaves genuinely inactive units to normal one-use launch, and
   completes only after all grants prove ready. Keep native restarts, actual
   operation admission, held completion and regular recovery unchanged. Add
   public `maintenance startup-status UUID` and
   `maintenance recover-startup UUID --source SOURCE [--from-candidate]`.
   The latter recovers startup-only state, never a full operation. Candidate
   entry uses the existing exact source-build/source-identity and transition
   generation checks; the executing reviewed candidate Q must equal SOURCE's
   output. Q is the repair executor, **not** a replacement for saved candidate P.
   Current-generation entry retains its normal generation check. No generic
   alternative-owner flag or arbitrary helper dispatch is introduced.

4. The public recovery supported here is the same-package pending enable:
   source token=authorized token=current token, original selected P unchanged,
   exact original ID/target/grants, no full operation directory, no conflicting
   active operation, ordinary held machine claim and verified session identity.
   Require the complete current registry/plans to equal the saved grants, native
   already running and ready without stop/adopt/restart, and codex/pending either
   exactly matching or absent. Refuse mismatches and consumed uncertain effects;
   absence never substitutes for the startup/native proof. For this rollout use
   the original claim5ed5527b-c5b0-42fe-8d2d-53aacf27fd81; do not invent a saved
   claim or coordination job that the schema1 startup never contained.

   Revalidate under transition exclusion, observe/reconcile the original ready
   grants, restore auto-archive/tracking-sync timer effects through existing
   `configure_auto_archive_services(..., package: P)`, clear only an exact
   matching pending record if present, and finish the original startup last.
   Do not call switch, resume, `_activate`, nix-env, or launch a replacement
   native as part of this recovery. Any failure keeps the original pending
   intent and already recorded evidence for the same command; idempotent
   completed replay verifies the same identity/effects without reissuing grants.
   Do not stop newly restored workers to manufacture rollback. Public status
   must distinguish startup pending/completed from “no full operation”.

**Finite acceptance package.** Extend the existing Ruby same-package test to
execute enable/completion, not just preparation, and cover exact candidate
recovery, timer restoration failure/replay, absent versus mismatching pending,
source/token/claim/registry mismatch and full-owner refusal. Reuse existing Go
startup peer/process helpers for startup-only observe, genuine consume/reconcile,
changed invocation/socket/marker, stale CAS, one-use/failed attempt and existing
schema1/2 owner routing. At least one affected test crosses actual Ruby JSON
transport to the real Go controller/store without stubbing startup success;
the old absent-operation and unlaunched-grant code must fail this regression.
Keep this in existing fixtures, not a new protocol framework. Include old-schema
readability and no operation-directory creation/no native stop/no duplicate
launch assertions. Do not test only a hand-built store success path.

Quick batch in R's declared Nix shell: Ruby syntax for changed Ruby, then
`ruby test/workspace_host_test.rb --name '/maintenance|startup/'`; from portal,
`go test -mod=readonly ./internal/maintenance ./cmd/workspace-portal -run
'Test(Startup|CompletedStartup|TerminatedStartup|MaintenanceProtocolOwner)'` plus
the explicitly named new transport regression if it is outside that selector.
Expected seconds to a few minutes; stop on first different failure and reassess
at10min, without adding retries or a wider speculative suite. Commit complete
source/docs/tests, then mandatory independent final review before long checks.
One affected packaged real-systemd/native control must exercise ordinary
same-package enable and exact pending recovery through the public command;
extend the existing session-creation maintenance setup/helpers for this seam,
preserving its current cases/verdicts. Use the original exact-successor packaged
acceptance once, not a separate native harness or exploratory run. Final normal
checks and artifacts follow changed-input scope; accepted SDK/assignment/model/
monitor evidence is retained, and unchanged derivations reuse exact receipts.
No count-by-name reuse or waiver of affected host/native startup checks.

Packaged-seam clarification to implementer0: use an initial ordinary enable with
a fixture-only timer-restoration fault, then remove that exact fault and recover
its original UUID publicly, replay completion and replay ordinary enable. Require
the expected failure after pending startup/ready proof, rather than an earlier
masking or reconcile error. Preserve the disabled predecessor, unchanged native
invocation/marker/profile and original grants; assert timer restoration and no
duplicate launch. Staging a second intent after successful enable would instead
exercise enabled-to-enabled state. The focused real-controller regression still
covers the original unconsumed-grant failure; the later timer fault does not
replace that coverage. No additional run or case-order change is selected.

**Forward delivery and live order.** After reviewed R publication, compose W
through its existing nested runtime URL/lock update, preserve W's observer
addition and extension/follows, and set C's existing devWorkspace channel to
the exact successor through confctl. Preserve original refs; no default merge
is implied. Build/check/review the affected final composition and root Q and
required host artifact. Main rebinds actual startup/profile/native/claim and
the unknown pending disappearance before dispatch. With the verified session
environment and original held claim, the new supported command is:

```sh
"$Q/bin/workspace-host" maintenance recover-startup \
  a3e29943-46d2-447b-8a6d-6adc051252cd --source "$W_REPAIR" --from-candidate
```

Q must report original startup completed/enabled, P still selected, all original
grant identities retained with actual ready proof, timers restored, and matching
pending absent. Capture terminal status/effects; stop on any uncertainty, with
no replacement UUID or automatic retry. Then main can perform the ordinary
host-first/profile-second forward deployment of the reviewed successor under
the existing rollout contract. Regular schema2 and historical1 owner recovery
remain supported throughout. Verify exact selected artifacts, restored effects,
portal/conversation/settings continuity and the already required owned monitor
wakeup/usability outcome; do not inject another live failure. No rollback to
pre-support packages, session cleanup or lifecycle action is authorized.

Settled: owning R defect, full-feature repair, schema-compatible observed-ready
representation, source-bound public recovery and dependent pin boundary.
Open before live execution: fresh original identity/effects proofs, cause of
codex/pending disappearance (not needed to infer completion), and actual repair
acceptance. Main owns release and live decisions. Only design.md changed; all
source/live/Git/check effects remain zero, no handles remain. Capacity returned;
session stays open, no next task assumed.

### W repair checkout: preserve the registered full branch, prepare separately

2026-11-08; bounded clarification after the refused second workspace registration.
Current/env/fresh roster verified; Git/session routes and selected P source read.
Original W remains branch2026-11-03-lead-wakeup-delivery at exact
b78ed11f18a5de3449cbaf81ac8f3ae3816b9bca. Main reports the refused add created
no branch/path. Preserve that branch, checkout and portal registration literally.

Selected P `.dev-session-wrapped:2804–2910` reserves project/name `workspace`
and refuses a changed branch for an existing registration. Sync at8758–8765
also refuses checkout/registered-branch mismatch; remove does not unregister.
Thus switching the existing checkout to the repair branch is not a supported
registration update. Do not rename the project, edit the manifest, or exploit
sync to register a forbidden alias. No runtime feature is needed.

The sufficient path is an ordinary isolated **unregistered** Git worktree from
exact b78, with a distinct repair branch, under this initiative. Main may release
this preparation to implementer1; this template was not executed:

```sh
ROOT=/home/aither/workspace/ai/vpsfree.cz
W_REPAIR="$ROOT/worktrees/2026-11-03-lead-wakeup-delivery/workspace-startup-repair"
REPAIR_BRANCH=2026-11-03-lead-wakeup-delivery-startup-repair
git -C "$ROOT" worktree add --no-checkout -b "$REPAIR_BRANCH" "$W_REPAIR" \
  b78ed11f18a5de3449cbaf81ac8f3ae3816b9bca
git -C "$W_REPAIR" sparse-checkout set --no-cone --stdin <<'PATTERNS'
/*
!/work/
!/archive/
PATTERNS
git -C "$W_REPAIR" read-tree -mu HEAD
```

Require both destination and new ref absent before creation; a collision or
uncertain result returns for effects reconciliation, never force/reuse/reset.
Sparse initialization follows `WorkspaceSourceCheckout.configure` on a new
empty index only, excluding tracking/archive from this additional checkout.
Shared master/index and original W index/branch remain untouched. Ordinary
workspace instructions/hooks/publication apply in the new checkout. Keep its
canonical origin and exact head/source-input/artifact bindings in current
state/review/rollout records. Normal sync may warn that this extra checkout is
not canonical; it must not acquire a portal registration. No cleanup is selected.

**Source and ownership boundary.** Selected
`workspace-coordination-host.rb:11–39` fingerprints/builds the supplied source;
ordinary `switch --source` with the held claim does not require that source to
be the registered W branch. The repair's public `recover-startup` similarly
binds its executing Q to the supplied source output and rechecks source identity.
Use this explicit W_REPAIR path for pins, composition checks, build and public
recovery/forward profile selection. Original startup P/ID/token and the held
machine claim remain unchanged. Main still verifies the exact registered C
machine mapping under the original claim; this checkout grants no deployment.
The older managed `coordination candidate-prepare/candidate-reconcile` path
at `workspace-coordination-host.rb:374–380` explicitly demands the registered W
head and is **not** available for this repair source. Do not redirect that path.

**Final-head obligation.** Registration remains evidence for original b78 only.
Record the additional exact repair branch/head and complete base-to-head review
explicitly; publish it and preserve the original branch. Existing registered W
comparison cannot be relabeled as the repair comparison. After separate explicit
workspace/master integration approval, ordinary reviewed fast-forward Git
integration from the shared master, under the registered workspace repository
claim plus tracking lock, can integrate the repair head. Preserve unrelated
shared changes; if master moved, prepare the necessary reviewed successor on
the repair branch outside ownership, leaving original b78 intact. Record both
original deployed lineage and exact repair-final remote ancestry before machine
release/session completion; passing the original registered-head check alone
is insufficient. Legacy reservation/job workflows retain their own registration
and proof limits and are not substituted for the present held-claim path.

No added checks, manifest changes, source/Git/registration mutation, build,
runtime/claim/lifecycle action or command effects. Only this design note changed.
Sufficient preparation boundary returned to main; capacity returned, session open.

### Original machine claim with the C repair registration alias

2026-11-08; sufficient existing-interface disposition, no product change.
Keep claim5ed5527b-c5b0-42fe-8d2d-53aacf27fd81 and its original registered
binding `vpsfree-cz-configuration` / `cz.vpsfree/machines/aitherdev`.
The released `repair-machine-binding-preflight.json` failed4 before resolution:
selected `workspace-coordination-claims.rb:495–503` requires the exact saved
repository name and selector. The repair alias is not that saved name.
`repair-original-machine-binding-preflight.json` passed at16:55:04UTC and binds
the same held claim/resourcecb771535 to current original Cac90. Binding equality
deliberately excludes sourceRevision; retained e3f942 is acquisition provenance,
not a deployment-version pin. No alias retry, record rewrite or new claim.

This original-name proof establishes ownership/mapping, not C304 artifact
acceptance. The independent source/artifact binding is sufficient here: exact
C304eadbc93a593807ea626bbdf47ff120418d880 differs from ac90 only in the R input
lock8a810->7196886a. Its unchanged
`cluster/cz.vpsfree/machines/aitherdev/module.nix` selects that exact machine and
host.target172.16.106.40. Canonical origin remains
git@github.com:vpsfreecz/vpsfree-cz-configuration.git; no lock-label, selector,
adapter or routing change is selected. R's host module is unchanged. Released
`/tmp/lead-wakeup-WC-repair-final-719-6he1xa27/C-artifact.json` binds clean304,
R719, generation2026-11-08--17-45-50 and TOP
`/nix/store/fnc1w243r8h2cxchfgjg318fmkfzxgix-nixos-system-aitherdev-26.05.20261026.718f670`.
Final packet acceptance remains main-owned; this is no new build/evaluation gate.

Qb83kfhq5's installed machine-identity-policy retains the identical structured
origin/name target and legacy bridge. Its claims implementation is byte-identical
to P0d9006. `profile_claim!` at468–487 selects the held logical resource, then
verifies the claim's saved original repository/selector. Therefore public Q
recovery and ordinary profile switch use the original binding automatically;
the repair source need not masquerade as that registration. The selected guide
expressly makes aliases/branches with equal canonical origin/name contend for
one target; physical routing remains the operator's artifact/configuration proof.

After existing final gates and main's fresh original-intent/effects preflight,
use the verified session environment and original DEV_WORKSPACE_CLAIM_ID:

```sh
Q=/nix/store/b83kfhq5zrz88y3isspd8vga0ga36a9m-dev-workspace-0.2.0
W_REPAIR=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-03-lead-wakeup-delivery/workspace-startup-repair
C_REPAIR=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-03-lead-wakeup-delivery/vpsfree-cz-configuration-startup-repair
export DEV_SESSION_SLUG=2026-11-03-lead-wakeup-delivery
export DEV_SESSION_WORKSPACE=/home/aither/workspace/ai/vpsfree.cz
export DEV_WORKSPACE_CLAIM_ID=5ed5527b-c5b0-42fe-8d2d-53aacf27fd81
"$Q/bin/workspace-host" maintenance recover-startup \
  a3e29943-46d2-447b-8a6d-6adc051252cd --source "$W_REPAIR" --from-candidate
# Stop and verify original completion/effects while P remains selected.
# Then, from C_REPAIR, use its existing named generation:
cd "$C_REPAIR"
nix develop --command confctl deploy --generation 2026-11-08--17-45-50 --copy-only cz.vpsfree/machines/aitherdev
nix develop --command confctl deploy --generation 2026-11-08--17-45-50 cz.vpsfree/machines/aitherdev dry-activate
nix develop --command confctl deploy --generation 2026-11-08--17-45-50 cz.vpsfree/machines/aitherdev switch
# Only after terminal host effects/health, ordinary selected profile command:
workspace-host switch --source "$W_REPAIR"
```

These remain individually released phases, not an unconditional script. Preserve
the original failed evidence and stop on uncertain effects. No switch replaces
startup recovery; successful recovery retains enabled selection for the forward
switch. No --repository alias is injected into the profile command. Record
original claim binding, C_REPAIR name/exact head, W/R input graph, system/profile
paths and routing together. Release still requires verified effects and complete
deployed/final lineage integrated under separate approval; unchanged original
registration alone cannot discharge repair-final obligations. No registrations,
branches, claims, runtime state or source changed; only this design note. Capacity
returned, session open.

### Live monitor8e92318c: unresolved configured-send failure before wake receipt

2026-11-08; bounded disposition for assignment45137efa. R7196886a, deployed
Qb83kfhq5 and pinned SDKc3c2adb7 remain the source boundary. The four inspected
R delivery/wrapper files match immutable source0ay89fmb byte-for-byte. Current
session/environment and fresh own roster match architect0/Astra/xhigh/
workspace_write/full_access. This is diagnosis, not wake acceptance or authority
to submit another input.

**Settled evidence.** Original monitor8e92318c-78d1-4802-a4a3-69531c59557e
completed its command and utility, but event99ab2be3e78ee17e088c10b665101349
has no accepted lead-turn receipt. Retained public status is
`/tmp/lead-wakeup-aitherdev-rollout-c2n4xj47/repair-usability/monitor-status-after-user.json`
(SHA256fe5dfea40486e451a3118c11c01e01eb93dc84ecdb237035ca72cca00ae91348);
request/start are beside it. Status reports held, "The original input has not
been submitted". Subsequent authorized exact-operation file reads show submitting,
the same ID/context/options/admitted epoch and no receipt. This is not continuous
state evidence and does not prove a successful send or recovery.

Read-only SQLite inspection of the configured socket database
`~/.local/state/dev-workspaces/submissions/bced879de15a05f23836072b53ea2860aa13a982415f07bf83ab93a6ee8c9ea6.sqlite`
found zero submission_records rows for exact root01a1a349-247f-7ad0-aa2f-1c9881e5f4c6
and event ID. Its own turn-retries record likewise has no matching snapshot.
The record is schema2/epoch2, pending=null, 63 snapshots, 624594 bytes, no unbound
snapshot; saved binding policy equals the event's frozen policy. These samples
do not prove a capacity failure, historical absence, native nonexecution, or
the original returned error. Do not erase or synthesize either ledger.
The exact event query against the portal journal has no correlated diagnostic;
the monitor worker logged context deadline exceeded at17:12:18 and17:50:21,
without event or phase identity. Those generic lines cannot select this event's
failed predicate. Own-root/event queries against the native unit supplied no
additional discriminator.

**Source boundary.** R `portal/internal/monitoroperation/delivery.go:175–202`
manufactures the reported held text during status reconciliation when SDK
Reconcile returns no receipt/no error. It does not preserve the initial send
failure. Dispatch at90–165 saves submitting before Send; a generic Send error
is reduced to "Delivery is unconfirmed" and the function returns tx.Save().
Consequently a successful save hides that error from the existing worker logger.
`portal/internal/web/monitor.go:28–69,102–151` composes the real workspacecodex
client, takes ordinary admission, and gives each event five seconds. Pending,
held and submitting already receive later ordinary worker passes. The observed
state is not a request for manual enablement, activation, resume or new monitor.

R `portal/internal/workspacecodex/turn_retry.go:112–129,167–294,321–380`
performs policy/scope/lock admission, exact SDK reconciliation and managed
capture before calling SDK Send. In particular, after no existing receipt it
calls SendAttemptedWithOptions even for a new ID. Actual c3c2
`codex/client.go:5608–5637,4936–4970,2436–2498` then searches descending native
items for the exact ID/text; proving absence walks the complete history, without
retained cursor progress across calls. The method takes the queue mutex with
Lock(), unlike Reconcile's LockContext. Only SDK Send installs deliveryIdentity
for the existing RPC trace, so wrapper preflight RPCs lack event correlation.
This explains a concrete possible pre-capture/deadline failure and why the
current diagnostics cannot identify it. It does NOT establish that this scan,
its lock, metadata reads, transport, policy or provenance caused the live failure.
The existing configured-monitor fixture uses short history; it does not prove
that this mature root's absence search fits the worker budget.

The history search cannot simply be deleted: SDK AcknowledgeSends can remove an
accepted ledger row after exact native proof, and R's
TestRetryRetentionManagedSteersBeyond64AndExactReplay explicitly preserves
history-only accepted replay. Ledger absence alone must not authorize a duplicate.
Pre-reserving the live event, calling bare SDK Send, increasing five seconds,
or using a new ID would choose a cause or change authority without evidence.
Prior9085 fresh queue acknowledgement is a different boundary and stays intact.

**Smallest releasable next boundary: retain this one missing failure, not a
behavioral workaround.** The missing discriminator is the configured Send's
failed phase and cause, correlated to the exact event before Dispatch discards
it. A cause correction and a manual same-event recovery command are not yet
supported. Main can allocate one R-only bounded diagnostic correction in
`portal/internal/workspacecodex/{client,turn_retry}.go` and its existing tests:
reuse the already supplied codex.ClientOptions.DeliveryObserver callback for
fixed managed phase completion events (admission, receipt reconciliation,
history-only discovery, capture, policy refresh and actual send), carrying the
original thread/message ID, elapsed time and failed flag. Give failed stages
a fixed safe cause suffix using errors.Is/As (deadline, canceled, transport,
unknown, unsent, snapshot-capacity, or other); retain recognized local refusals
as fixed codes, never arbitrary RPC text, envelopes, settings or instructions.
Preserve errors and their Unwrap/type behavior; no persistence/schema, public
tool, SDK pin, retry or admission change. Existing main.go deliveryDiagnostics
already logs failures. This is the existing trace interface, not a new journal,
status subsystem or diagnostic run. If the first classified boundary is still
insufficient, return its precise error/owner gap rather than enlarging scope.

Extend the existing managed-send fixture to observe phase/cause/ID for a
controlled history-read deadline/refusal before capture, zero native sends and
no admitted snapshot, plus accepted/history-only replay and unknown outcomes.
Reuse configured-monitor repair and status-reconcile tests to preserve one
event, original immutable options, prepared-only repair, no receipt-only wake
claim and no status-triggered send. One finite focused batch, after implementation
and only on main's allocation, from R's declared Nix environment:
`go test -mod=readonly ./internal/workspacecodex ./internal/monitoroperation -run 'TestRetryRetentionManagedSteersBeyond64AndExactReplay|TestMonitorConfiguredOutcome|TestMonitorStatusReconciliation|TestManagedSendDeliveryDiagnostic' -count=1`
from portal/. The last name is the proposed focused regression. Expected test
execution under one minute with prepared inputs; first different failure or
unexpected preparation returns to main. Independent committed-change review and
affected package validation remain required before selecting a new artifact;
this brief launches none and reopens no unrelated accepted suite.

After a reviewed forward diagnostic artifact is selected through main's normal
release, use the existing worker's ORIGINAL retained event to obtain the first
correlated failure; no new utility, synthetic failure, manual Dispatch, extra
send or retry loop. Then release the owning cause correction or a supported
ordinary hold disposition. Preserve current permission/Stop/provider/lifecycle
checks, exact owner/root/epoch, frozen text/options/context, unconfirmed receipts
and all accepted recovery contracts. Final wake acceptance still needs the
original exact event's accepted receipt and matching native lead input/turn;
command success, submitting, held or queue-only receipts do not satisfy it.

Only this design append changed. All read commands/cells are terminal; no
application/Git/check/build/network probe/native mutation or lifecycle effect.
The report transport returned unconfirmed on the same c913aaef-3b7f-4469-9db7-ee0504da3982
message; its exact text/ID was retained for retries, no replacement report or
accepted delivery assumed. Per main's clarification, further report retries
stopped and this file is the direct handoff. Capacity returned; session open.

### Original-event observation before a diagnostic deployment

2026-11-08; sufficient bounded clarification, no execution. Current/env/own
roster reverified; unchanged guidance reused, deployment/project routes and
selected Q coordination guide read. Implementer0 retains instrumentation28a13ae2;
this does not alter or duplicate that package.

**A shorter safe observation exists, with a narrower conclusion.** The public
c3c2 SDK `SendAttemptedWithOptions` is an exact history-discovery API, not a send:
client.go:5608–5637 checks its ledger, calls the same private sentByClientID /
walkThreadItems used by R's pre-capture reconciliation, and records a discovered
accepted receipt. Therefore it is NOT read-only when attached to the live ledger.
ReconcileSendWithOptions and public monitor status are not substitutes: they can
save recovered receipts, and an absent ledger entry makes Reconcile return
without doing the history search.

A dedicated bare `codex.NewWithOptions` client can safely perform that exact
lookup against live native history with ALL ledger paths confined to a fresh
private observation directory. Use ObserverOnly=true, explicit absolute
SubmissionDatabasePath=SCRATCH/observed.sqlite and
SubmissionLedgerPath=SCRATCH/import.json, LegacySubmissionLedgerPath="".
Do not leave SubmissionLedgerPath empty (it defaults beside the live socket),
copy/seed the live ledger, use the workspacecodex configured constructor, or
share this client with another operation. SDK submission initialization may
create SQLite/WAL/locks and a schema4 import fence, and a positive lookup may
write an observational receipt, but all those paths are in SCRATCH. None is
live acceptance authority. No live retry, monitor, queue, permission or ledger
record changes. No new monitor operation or input identity is allocated.

`client.go:1124–1130` enforces ObserverOnly's read-method allowlist;
`readLoop` at1410 ignores approval/user-input requests rather than answering or
rejecting them. With no Watch/ObserveEvent/ActivityRecorder/lifecycle callback,
this sequence has no subscription, resume or settings side effect. Only the
ordinary initialize/initialized handshake and thread/read + thread/items/list
reads reach native. The existing TestObserverListQueueStaysReadOnly proves the
mutation/request-answer exclusion; SendAttempted's source supplies the separate
local-write boundary. Do not call Send, Dispatch, Prepare/Discard, queue methods,
managed capture or live admission helpers in the observation.

**One finite invocation, if main allocates it.** A small one-shot caller of the
existing API is sufficient; no parser, alternate history implementation or SDK
edit. Compile against immutable R719 portal/go.mod/go.sum (c3c2adb705f5), using
the declared Go environment and -mod=readonly/GOWORK=off; do not build from A's
changing source or repin dependencies. Inputs are the exact private operation
snapshot's root01a1a349-247f-7ad0-aa2f-1c9881e5f4c6, original
event99ab2be3e78ee17e088c10b665101349, envelope/context/frozen TurnOptions and
socket, plus expected workspace/cwd and original operation8e92318c. Validate
those identities before use; retain an input digest, never print instructions
or message bodies. Confirm metadata with ReadThreadMetadata(excludeTurns=true).
Use one five-second context for the handshake/identity/lookup sequence and close
the client afterwards. Capture each phase's elapsed time and safe error class,
found boolean, and per-RPC completion timings through DeliveryObserver with the
externally known exact ID. Count completed item-page RPCs; do not record payloads
or invent row counts from RPC count. No second invocation on failure.

Important bound: the native calls honor that five-second context, but SDK local
submission transactions have independent ten-second contexts and its queue mutex
Lock is not context-aware. Fresh exclusive scratch/client avoids shared-lock
contention, but does not establish a hard five-second wall-clock guarantee for
local I/O/receipt recording. Record setup/identity time separately within the
overall budget. A deadline after only two seconds of history cannot be reported
as a five-second history traversal failure. Stop at that actual stage; do not
increase the live worker budget or silently warm/repeat the observation.

If this returns a concrete native history error, it establishes that this exact
production lookup path fails NOW for the original event. A deadline during the
lookup establishes incomplete traversal in its measured remaining budget; a
successful false result establishes completed absence only in that observation.
A positive result is history evidence for main's ordinary same-event receipt
reconciliation, not permission to copy the scratch receipt into live state.
Neither success nor failure proves the original17:12 cause or recreates portal
admission/shared-client contention. No claim that the wake is fixed follows.
If inconclusive, stop and use A's correlated production instrumentation; do not
grow a preflight framework. This is a useful earlier discriminator, not a full
replacement for the already allocated instrumentation.

Review the finite caller's method/path inventory before live use; compile it
without invoking the socket. Existing SDK observer and
TestSharedHistoryRecoveryRecordsAcceptanceAtomically contracts are the relevant
unchanged evidence. If that evidence is unavailable, one focused existing SDK
test batch suffices (those two named tests, -count=1, expected seconds); there is
no R29/native5/native11/W6/C build requirement for this read-only caller. Main
owns allocation/review and its single execution. This assignment creates no
caller, artifact, scratch ledger, test or connection.

**Minimal artifact fallback, if the observation does not settle the owner.**
A completes focused checks and independent committed-change review. For actual
instrumented worker observation, use the ordinary composed application artifact;
do not start a second portal or swap a binary into Q. Publish R, update W's
existing nested URL/lock and C's declared confctl dev-workspace/devWorkspace pin
to that same R, preserving extension/catalog/follows and all full branches.
The existing cross-repository deployment checker requires exact R identity on
both input paths even when C's generated system is unchanged. Bind affected
R/W output derivations to retained receipts and run only changed/unresolved
checks; do not identify reuse by output names. W's configured package changes
and its package checkPhase exercises Go/JS. Production delivery regressions and
same-event invariants require the new focused evidence; unchanged native/startup
contracts do not automatically require their entire matrices to be rerun.

The host application is NOT installed by C. Current C config.nix consumes R only
through nixosModules.host (line106) and lib.mkCodexPackage (lines19,82,224);
R flake.nix:150 imports host-module.nix, and codex-package.nix depends on its
unchanged assembly and selected native/package tools, not the edited Go wrapper.
Thus R-only observer instrumentation has no source-supported host behavior
change. New C pin/generation provenance remains necessary, but a new host build
or activation is required only if the resulting toplevel/derivation actually
differs or cannot be bound to the accepted rooted artifact. Main's later normal
evaluation/artifact comparison must establish that; source inspection alone
does not certify equality. If equal, retain existing deployed host evidence and
proceed with the reviewed W profile artifact under ordinary claim/compatibility
checks; no pointless host switch. If different, use the established host-first,
profile-second route and explain the actual changed dependency. Do not waive
composition or rewrite old receipts. No deployment command is released here.

Only this design addition changed; all commands terminal, no live observation,
SDK/application/Git mutation, build/check, claim or lifecycle action. Reporting
transport retries remain stopped as directed. Effects/capacity returned; main
can read this sufficient boundary directly. Original event remains unresolved.

### Mature-root send discovery: continue the proof across bounded passes

2026-11-08; sufficient cause-correction package for main's release decision.
Current/env/own roster match; retained architect settings unchanged. R719 remains
deployed through Qb83/W67d/C304. Reviewed diagnostic successor19efc6eee3ff34e2e890c07dc2a43ac93ab1063f
is an unselected preparation dependency, not evidence of a repaired wake.

**Demonstrated defect and limit.** Main's single completed observation is in
`/tmp/lead-wakeup-original-event-observation-4t1bxtnf/{main-execution,observation}.json`.
Exact snapshot6caca614690730fd454043ad5bdefa413cdd902f3d32917ce85535f85d37af59
binds monitor8e92318c-78d1-4802-a4a3-69531c59557e,
event99ab2be3e78ee17e088c10b665101349 and root01a1a349-247f-7ad0-aa2f-1c9881e5f4c6.
Handshake4.316ms and metadata8.466ms succeeded; history lookup5009.564ms ended
deadline after130 successful completed item-page RPCs. found=null means unknown,
not false. PID3424920 naturally exited1 and was joined. No observation replay.
This proves the required current lookup cannot finish in the worker budget;
it does not identify the historical17:12 failure or shared-lock timing.

R's reconcileRetrySend calls SDK SendAttemptedWithOptions before capture. At
c3c2 client.go:5608–5637,4936–4970,2436–2498 a missing ledger entry initiates a
complete descending item traversal. Every invocation starts at the head; a
deadline loses all progress. Repeating this mandatory proof under the same
five-second item budget can prevent an otherwise admissible mature root from
ever reaching capture/send. This is the correction boundary; do not enlarge
timeouts or modify admission, monitor scheduling, queue completion or goals.

**Dependency decision: a narrow SDK addition is needed.** The existing boolean
lookup exposes neither an unfinished cursor nor an accepted-receipt import.
ReadThreadPage is presentation paging, not an exact submission proof/receipt
interface; moving that proof into R would duplicate SDK identity and acceptance
logic. Ledger absence cannot establish first admission: AcknowledgeSends can
remove an accepted row after history proof, and R's retention regression requires
history-only accepted replay after restart. The live submitting monitor record
cannot retroactively prove that its first send never happened. Do not use
PrepareSend as a reservation shortcut, bypass history for monitor-prefixed IDs,
invent a first-attempt flag for this record, or change acknowledgement retention.
This explicitly adds codex-web ownership/pin work for main's allocation; it is
not an R workaround or authorization to edit that dependency now.

**SDK package, preserving the old public method.** Add one opt-in public sibling
`SendAttemptedWithOptionsResumable(ctx, thread, text, id, action, options)
(bool, error)` beside SendAttemptedWithOptions. It has the same final-result and
atomic accepted-receipt semantics, and NEVER sends/queues/resumes input. Other
SDK callers retain their existing method. Put its small private discovery state
and helper in `codex/send_discovery.go`, with construction/Close integration in
client.go, focused existing-peer tests in `codex/send_discovery_test.go`, and a
short contract in docs/submission-storage.md. No database or native protocol
schema, persisted cursor, background worker, generic index or new dependency.

The state is a disposable per-client proof continuation, keyed by exact thread,
client ID, text digest, action and normalized options digest. Preserve the
existing per-thread SDK queue serialization using LockContext(ctx) in this new
entry point. Recheck ordinary exact ledger state on every call; a prepared or
accepted record retains the old method's result, identity conflict remains an
error, and R's preceding queued/submitting reconciliation remains authoritative.
Do not reinterpret an unknown or queued result as an unsubmitted input.

Retain only completed, fully validated raw history pages' continuation and
matching/ordering proof, not message/tool bodies. Reuse the existing
sentByClientID validation/receipt construction rather than a second text parser.
Carry the current duplicate-item/cursor checks across continuation; an error or
incomplete page cannot advance the cursor. A match at a page boundary must still
obtain the adjacent older item needed for the existing Steered classification.
Only the existing atomic recordSendAttemptWithReceipt path publishes a positive
result; a failed record save remains an error. Partial progress alone writes no
live receipt, admission or retry snapshot.

Validate continuation against the existing SDK page identity machinery:
thread/cwd/path/lineage, native connection generation, same rollout file,
nontruncation and the saved prefix-tail check (thread_page.go:139–179,260–284;
page_metadata.go). Save a checkpoint only after a complete page and invalidate
it on identity/generation/reset/changed prefix or malformed pagination. Missing
source identity cannot authorize reuse; restart the proof or return an error.
Close/restart loses hints and safely rescans, without changing durable receipts.
Bound the number and idle lifetime of retained hints using the existing cursor
cache convention; eviction restarts proof, never returns absent. Preserve
strict cross-page validation without a total-history/page cutoff. The retained
validation sets replace the existing traversal's sets, not a stored transcript.

Do not miss input appended while old history is traversed. Keep the native head
anchor of the scanned prefix. Before returning a complete negative, refresh and
validate the new head through that anchor and recheck the exact ledger; if this
catch-up itself crosses the deadline, retain its progress and remain unresolved.
Retain an exact completed-negative checkpoint until the caller has crossed
admission, so a deadline in later capture does not force a second full scan;
each reuse must freshly validate identity and appended head, never treat an old
negative as current authority. Reordered/missing anchor requires invalidation.
The same native append/cursor contract already supports SDK transcript/activity
paging; no later sample or file-size comparison alone proves absence. If its
existing checks cannot support a safe raw-item continuation, stop implementation
and return that specific contract gap rather than weakening it.

Incomplete discovery returns a non-nil error, preserving context cancellation/
deadline and transport causes. It must NEVER return (false,nil) until all retained
history and head catch-up are complete under valid identity. A later ordinary
worker pass continues the same lookup; no internal sleep/resend or detached
work outlives the call. Other errors stay errors; no false receipt, partial
acceptance or error-as-absence. This changes proof progress, not execution rights
or the existing limit against unmanaged concurrent native writers.

**R consumer package, dependent on reviewed/published SDK.** Starting from19ef,
replace only reconcileRetrySend's history-discovery call with that new method;
retain its diagnostics, early reconciliation, capture, policy refresh and send
ordering. Update the one SDK stream in flake.nix/flake.lock, portal/go.mod/go.sum
and nix/workspace-portal.nix vendorHash through the existing pin workflow. No
change to monitor event format, Send/Dispatch/Ready, native.go prepared-only
repair, Stop/provider/epoch permission,9085 cold queue semantics, SDK unknown
handling or acknowledgement. Test through the real configured workspace client
and existing monitor fixture, not a fake transport that skips managed admission.

**Meaningful regression before release.** Extend the existing peer with many
descending history pages and deterministic per-call cancellation after a small
number of successful page replies. New code must finish across finite successive
bounded calls while old code repeatedly revisits the head and cannot reach
capture. Use server-observed page progress rather than a timing-sensitive sleep.
First prove absent original ID across the full history, then exactly one native
start/steer with the unchanged ID/text/action/options; every incomplete pass has
zero new capture/send. Also put an acknowledged matching ID on an old page and
prove receipt recovery without capture or send, including a match at the page
edge. Include completed-negative reuse after a canceled capture, head append
with an exact match during backfill, changed text/options, malformed/repeated
pages, source truncation/replacement, reconnect and cold client restart. Cached
partial state must never authorize a negative after any invalidation. Existing
accepted, prepared, unknown and queued cases retain their receipts/refusals and
never gain a duplicate start. Retain all monitor prepared-discard/revocation and
queue-only-not-wake assertions.

One quick SDK batch in its declared environment:
`go test ./codex -run 'TestSendDiscovery|TestOptionAwareDurableAttemptFamily|TestSharedHistoryRecoveryRecordsAcceptanceAtomically|TestSharedLedgerAdmitsOnlyOnePreparedSender|TestObserverListQueueStaysReadOnly' -count=1`.
Then R's existing focused batch with the new configured regression plus
TestRetryRetentionManagedSteersBeyond64AndExactReplay,
TestManagedSendDeliveryDiagnostic, TestMonitorConfiguredOutcome and
TestMonitorStatusReconciliation (go test -mod=readonly from portal/). Expected
seconds to about one minute per prepared batch; first different failure, lost
identity or scope expansion stops for main. Use ordinary independent committed
SDK and composed R review before long validation. SDK's declared checks.default
and generic-source, R's changed package/protocol-pin checks and W composition
must be covered; preserve unchanged successes only with actual input/output
binding, not names. The accepted native protocol version is unchanged, but the
new SDK reader/pin affects delivery: run the existing final configured native11
matrix once after review, and reconcile other required R/W outputs by their
affected dependencies. No new native harness or full blind replay is proposed.

**Shortest delivery and recovery.** SDK implementation/review/publication feeds
R pin/consumer/regression/review/publication, then the existing W nested pin and
C declared confctl channel to the exact same R. Preserve original8a/719/W/C
refs and consumers literally; use the chosen forward feature lineage. Build the
actual configured W artifact, retain SDK/R/input identity, and apply the
design10430 host-output comparison: changed Go/SDK source does not by itself
change C's host module or mkCodexPackage/native inputs. Reuse a proven identical
host artifact; otherwise resolve the actual difference through the ordinary
host-first route. Composition/claim/forward-recovery remain mandatory.
Main selects the reviewed profile and observes ORIGINAL monitor8e92318c/event99ab2be3
through its existing worker. No new monitor, manual Dispatch/send or state edit.
Acceptance needs that event's accepted receipt plus matching actual lead input/
turn and the requested idle wake; utility success or queue-only receipt remains
insufficient. The observation and diagnostic commits remain useful evidence,
not substitutes for this acceptance or claims about the historical failure.

Only this design addition changed. All commands terminal; no source/pin/Git,
build/test, network/live query or lifecycle mutation. No report transport retry.
Cross-repository dependency and sufficient execution boundary returned to main;
effects/capacity returned, session open.

### Original event after profile switch: recovery and idle activation are distinct

2026-11-08; bounded sequencing clarification, independent of SDK review674b643e
and R implementation. Current/env/fresh own roster verified; retained settings
and applicable full guidance unchanged. Read only deployed719/Q source and
existing contracts, not dd90 implementation or the active review.

**The event permits idle activation but cannot guarantee it.** Frozen delivery
options retain model/effort/policy/context, not an idle-only condition. Deployed
R monitoroperation/native.go:55–94 admits idle, working and eligible waiting
activity; only user/approval waits and ordinary execution holds defer it.
DeliveryService.Dispatch reconciles first and accepts either a start or steer
receipt with a TurnID (delivery.go:90–173). In the existing SDK SendWithOptions,
ActiveTurnID at send routing selects turn/steer for an active turn and turn/start
for idle (Q's installed share/workspace-portal/codex/client.go:5416–5528).
Thus successful recovery is not necessarily steering merely because main was
active when the portal started: discovery can finish after main ends its turn.
Conversely, remaining active through verification gives the worker a legitimate
steer target. No saved option orders it to wait for main's final response.

The worker starts its ordinary two-second scan independently of main's completion
(web/monitor.go:102–151), under the current-generation/admission locks. A profile
switch preserving validated native invocation keeps Codex running; it supplies
no separate monitor hold until post-switch verification is over
(docs/workspace-updates.md:3–8). NativeDelivery's existing prepared-only repair
can reroute a positively unsent stale steer on a later scan with the SAME ID.
It cannot undo an accepted steer or reset an unknown result. Once accepted,
Dispatch returns without another send, even after the lead later becomes idle.
The current portal guide:1627–1650 states these same contracts.

**Shortest supported main-owned sequence.** Complete the already required
artifact/review gates and preparation before switching. Run the ordinary
claim-bound corrected profile switch once, join its command, and reconcile its
required selection/native/service/effect evidence. Preserve the claim and all
uncertain effects; do not leave a deployment command unjoined to manufacture an
idle window. Then finish the current lead turn normally and leave execution
permission unchanged. Ending the turn is not Stop, lifecycle shutdown or a
user-input/approval hold. An original event still unaccepted at that point may
continue discovery and start the eligible idle lead through its ordinary worker.
Do not assume that a preceding status sample reserves the event: delivery may
race between that sample and the final response. This sequence offers an idle
opportunity; no existing public interface makes the handoff atomic or guarantees
which routing wins. No new suspension, queued hold, timer change or product
behavior is proposed.

**Next observable result and acceptance.** On the original event's delivery,
main binds monitor8e92318c-78d1-4802-a4a3-69531c59557e /
event99ab2be3e78ee17e088c10b665101349 to its public accepted receipt and exact
native root input/turn, retaining original options/context. A successful steer
into the still-active main turn proves original-event recovery and delivery
liveness, but DOES NOT prove idle wake. If native evidence shows main's previous
turn completed and this original input started a distinct lead turn without a
user/manual input causing it, both recovery and idle activation are proved.
Use actual receipt/native evidence, not the timing of a status call or a
queue-only receipt. Held/submitting/unknown keeps recovery open.

If the event is accepted by steering, retain that success honestly and mark the
separate live idle-wake proof unresolved. The same accepted event cannot provide
a second idle activation. This note authorizes no replacement monitor or new
verification operation; any remaining acceptance decision returns to main.
Neither this race nor the need to label its result blocks SDK review, publication
or the already authorized correction work.

Only this note was appended under the existing tracking lock, released
immediately. All commands terminal; no live probes, source/Git changes,
checks/builds, claim/lifecycle or delivery mutation. No report transport retry.
Effects/capacity returned; session open.


### d272 delivery selection: affected checks, exact reuse and C provenance

2026-11-08; sufficient source-only addendum to design10549. Identity/current,
both absent environment markers and fresh own roster verified; retained
Astra/xhigh/workspace_write/full_access and documentation workflow unchanged.
This does not review d272 or SDKdd90, observe active work, or allocate execution.
R below means committed d272efc3716a7a03a26b2270086c2941d27a73ee, including
reviewed diagnostics19ef; final reviewer disposition remains main-owned.

**Minimum path.** After review, publish R and use its ordinary original CI for
fast/archive/creation; do not also replay those locally. In parallel, prepare the
existing W nested pin and C declared channel to that same published R, preserving
all original branches/additions and extension/follows/native pins. Compare the
two local host-VM outputs; retain exact host-idempotency success if bound, and
run changed recovery-boot once. Build W6/configured package and ordinary C named
artifact, and run final configured native11 once. Native5's direct SDK input has
changed: one existing short batch is simpler and stronger than a new equivalence
exercise. SDK's accepted default/generic-source CI need not be repeated by R.

| Output/evidence | Actual declared dependency and minimum disposition |
| --- | --- |
| R package and package consumers | R flake.nix:26–60,95–148 and nix/workspace-portal.nix:278–325 bind self, SDK source/version/vendor inputs, protocol checks and Go suite. package, host-package-contract, extension-catalog, agent-team-catalog and user-namespace need current outputs; generic-source scans current self. The seven-path consumer diff alone omits diagnostics19ef; use the complete719..d272 inputs. |
| R Ruby14 + aggregate | nix/ruby-checks.nix:19–40 filters out portal implementation but includes ALL nix/. The SDK vendor change in nix/workspace-portal.nix therefore changes this filtered source too. Do not reuse719 shards merely because Ruby code is unchanged. Ordinary fast/package builds cover these current derivations and the aggregate's unique complete shard proof. |
| Candidate exact reuse | codex-package, host-module, host-auth-benchmark, ruby-source-filter and host-module-idempotency have no declared dependency on Go/SDK implementation (flake.nix:96–113; owning nix/tests declarations). Compare complete root derivations, recursive inputs and valid successful outputs/NARs before reuse. In particular retain m9q5…drv/apfr… output only if the exact prior4091-input host-idempotency binding still holds; unchanged names/source alone are insufficient. Fast CI still requests its declared checks. |
| R recovery/archive/creation VMs | All consume the changed devWorkspace/mkPackage. recovery-boot actually enables the application units and calls workspace-portal (nix/tests/session-recovery-boot.nix:143–188,235), so unchanged scenario text does not prove current execution. Reuse only an unexpectedly identical complete derivation/output binding; otherwise run the existing recovery-boot once locally. Ordinary feature-push check.yml always launches archive and creation; host job runs only on master/manual dispatch. Preserve these original jobs, no workflow change/skip/cancel or extra local copies. |
| W6 and configured package | W67 flake.nix:22–30,62–134,280–301: four checks consume workspaceSource (which includes changed flake files), storage also consumes R, and policy/composition consume configured package. Expect all six and default to change after pinning; map actual derivations, build current outputs once, retain earlier behavioral evidence only within its old binding. Configured native11 remains mandatory once with the final package/native paths. |
| Native5, native/service identity | maintenance_native_integration_test.go:214 directly constructs the selected SDK client; the harness's Go inputs changed even if the native executable did not. Run existing five-case test once (719 Go12.478s), no other native campaign. Prove native wrapper/inner executable, catalog and service-unit identities separately from prior Q input/output receipts; this can preserve unchanged protocol/service evidence, not replace changed SDK/package validation or main's required switch-effect reconciliation. |

**C host reuse has a concrete provenance limit.** C304 aitherdev/config.nix:19–22,
106 imports only R's mkCodexPackage and host module, not the portal. Host/native
behavior may therefore be identical. However the accepted C graph actually
contains etc-confctl-inputs-info.json.drv (3s3mhjvs…) with R719 in env.text and
etc-confctl-configuration-info.json.drv (avw9i6x6…) with C304. These files are
installed under TOP/etc/confctl, as the existing validate-C.py and C-artifact.json
prove. A new matching R/C pin changes those bytes and the enclosing TOP: old
fnc1/6rk1 is not the final configured artifact even if all service derivations
match. This refines design10430's conditional host-equality option; do not spend
a separate campaign trying to prove impossible full-TOP equality with new
revision metadata. Reuse unchanged subclosures/check evidence, perform the
ordinary named C build (prior114.149s), retain positive output/NAR/root/generation
and source bindings, and follow the existing host-first/profile-second route.
Only genuinely identical full TOP/DRV/closure plus correct final embedded source
metadata could justify whole-artifact reuse; stale719/C304 metadata cannot.

**Ordinary comparison/command boundary (main allocates; none run here).** For
immutable R and final W, use the existing map command:
`nix eval --json --no-write-lock-file --no-update-lock-file REF#checks.x86_64-linux --apply 'checks: builtins.mapAttrs (_: c: { derivation = c.drvPath; output = c.outPath; }) checks'`.
For candidates, `nix derivation show --recursive DRV...` and
`nix path-info --recursive --json OUTPUT...` bind complete definitions/input
sources/outputs and positive NAR/closure metadata against retained success.
A null/missing output is unavailable, not a pass. Compare native actual launcher,
inner executable and installed service/catalog bytes as well as their producing
DRV/input graph; a shared native version string is insufficient.

Use existing explicit `nix build --no-write-lock-file --print-build-logs
--max-jobs 4 --cores 4 --out-link OWNED_ROOT ATTR...` for unresolved local R
outputs/W6, and W .#default. C remains
`nix develop --no-write-lock-file --command confctl build --yes --max-jobs 4
--cores 4 cz.vpsfree/machines/aitherdev`; its final generation and embedded
inputs-info/configuration-info must name final R/C, with immediate positive TOP,
rollback and root proof. Run the existing composition checker once on final W/C;
W nested URL/update and `confctl inputs channel set --commit dev-workspace
devWorkspace FINAL_R` remain the existing pin interfaces.

Native commands retain the declared Nix environment: `nix develop --command env
GOWORK=off LIVE_SWITCH_CODEX=N_FINAL go -C portal test -mod=readonly
-tags=live_switch_integration -run '^TestNativeWorkspaceBoundedPause$' -count=1
-failfast -timeout=10m -v ./cmd/workspace-portal`; final native11 adds
`LIVE_MONITOR_PACKAGE=P_FINAL`, selects `^TestNativeMonitorOperation$`, and uses
its existing20m limit. Prior native11 Go73.95s/overall82.509s and recovery VM
script352.31s are duration guides, not new deadlines. Stop on first different
failure, unexpected input/pin drift or unfinished effects; return its owner,
not a replay. W/C may proceed independently while the unavoidable original CI
VMs run. Complete R29 coverage joins original CI25+archive+creation and the two
local host dispositions; no count-by-name acceptance or second whole-suite run.

**Reuse receipts and authority.** R719 local bindings are under
/tmp/lead-wakeup-R-remaining-7196886a-jebisyk2/receipts/{coverage-29,idempotency-reuse,native-result,planned-commands}.json;
its final27 CI coverage belongs to the accepted terminal receipt under
/tmp/lead-wakeup-R-startup-publication-7196886a-itjwxq4z (the earlier local map's
B-pending labels are not final CI results). W/C baseline is
/tmp/lead-wakeup-WC-repair-final-719-6he1xa27/{W-six-bindings.stdout,W-six-derivation-graph.json,Q-derivation-graph.json,Q-source-input-bindings.json,C-full-derivation-graph.json,C-artifact.json,native-harness-binding.json}.
Reuse unchanged scenarios as prior behavioral evidence, never as a pass for a
changed package/derivation. Do not repeat already accepted SDK CI or create new
protocol/catalog gates.

Preserve held claim5ed5527b-c5b0-42fe-8d2d-53aacf27fd81 and its original registered
vpsfree-cz-configuration binding/selector cz.vpsfree/machines/aitherdev. The repair
alias is not an interchangeable verify-machine name. Main freshly verifies the
original claim and maps final C canonical origin/selector/logical target/routing
to it, retaining the new source/artifact metadata separately; no rebind/new claim
or stale sourceRevision assertion. Review, source publication, comparison and
artifact owners remain main-allocated; this note adds no approval gate. Live
selection/effects and ORIGINAL monitor8e92318c/event99ab2be3 recovery/idle proof
remain main-owned under the prior sequencing note, not replaced by native tests.

Only this note was appended under the existing nonblocking tracking lock,
released immediately. All read commands/cells terminal; no application/Git,
Nix/check/build, network/CI/live/native, claim or lifecycle mutation. No report
transport retry. Effects/capacity returned; session open.


### 7b original CI: repair the cold-assignment peer's rollout identity

2026-11-08; sufficient narrow implementer0 follow-up, released to main for
allocation after its current effects return. Current/env/fresh own roster match;
retained settings/full guidance and documentation workflow unchanged. Immutable
R7b23476e775283bdd80146da617f9ab81ededa91/tree96e9072c and SDKdd90fb4 inspected;
no active review, local recovery or CI observer inspected.

**Settled failure.** The terminal receipt at
/tmp/lead-wakeup-R-publication-7b23476e-pgwjpwl5/terminal-receipt.json matches
SHAf943f747df565ec37952d02bbb0ac7a6d7db38f99e08668289ec3e6a19fa6ee8. Independently
matched all three full job raw hashes to ci/first-original-failures.json. Original
archive3018–3059, creation3081 onward and fast1931–1972 contain the same19
progress=false subcase failures, all before queue/add/start/resume (counters0):
`send discovery requires rollout source identity`. Fast1977 onward is repeated
Nix tail, not another failure mechanism. ci/coverage.json establishes zero
creation starts/finishes and no archive scenario execution; package checkPhase
failed before either VM. No current cold/recovery/Stop or whole25/29 pass follows.

**Owner is this R test peer, not a weakened SDK predicate.** R
portal/internal/workspacecodex/recovery_test.go:139 returns member/cwd/source/
provider/historyMode but NO path. Its RetryPolicyResolver enables managed
admission; turn_retry.go:408→321–331 now reaches SDK
SendAttemptedWithOptionsResumable before capture or sendWithRecovery. SDK
send_discovery.go:83–107 returns this exact error only when cwd/path is empty
(the peer's cwd is present), then requires a canonical readable regular rollout
and binds lineage/generation/file/prefix. This is a deterministic missing peer
precondition, not CI timing. progress=true directly calls sendWithRecovery
(progress.go:18–35), so it does not take that discovery path; prior-unknown is
stopped by existing durable-attempt reconciliation before new discovery. Preserve
both distinctions rather than disabling RetryPolicyResolver to make this pass.

Actual ready-member setup supports the required identity: R
teamruntime/runtime.go:1454–1490 bootstraps/verifies before ready, and2403–2425
checks materialization before2450 SendWithOptions. SDK headless.go:16–60 requires
a canonical rollout path, regular file and matching persisted identity;
74–122 injects one internal developer marker and verifies it before ready.
A cold member is unloaded, not thereby unmaterialized. The existing configured
native monitor fixture likewise materializes its lead before managed send
(monitor_native_integration_test.go:1413–1441,1522). The SDK's separate fresh
unmaterialized-thread read contract (client.go:4376–4408) requires a NONEMPTY path
and exact missing-file/native-error evidence; it does not justify inventing
history absence for this pathless peer or broadening discovery. This diagnosis
establishes the failing cold-member boundary, not every possible consumer.

**One-file implementation.** Only
portal/internal/workspacecodex/recovery_test.go, inside
TestColdAssignmentAndProgressReceiptsRemainKnownAfterExecutionWithoutBrowser:
create a private per-subcase regular rollout.jsonl under its existing t.TempDir
before starting the peer, and return its stable absolute path in thread/read.
Use the existing R test convention (turn_retry_settings_test.go:65–66,150–163,212)
with a minimal valid session_meta record binding member/cwd, not a user item or
accepted assignment. Check write errors; close before serving. No new helper,
server/harness, pre-send, bootstrap RPC or production mutation is needed. Keep
the file identity stable for the subcase; do not recreate it per read. Do not
invent a turn_context, seed a ledger/snapshot or expose hidden assignment history.
All native item pages remain controlled by the current started/historyVisible
state; this file supplies the already-materialized rollout identity only.

Preserve all40 progress×mode cases, original time budgets and verdicts unchanged:
one queue attempt, exact ID/text/policy, recipient-only permission, foreign-head/
active-turn deferral, hidden-history fresh acknowledgement versus unresolved
replay, invalid/lost/prior acknowledgements, consumed/raced/missing history,
caller cancellation, epoch/permission/maintenance refusal and zero replay adds/
starts/resumes. The persisted-hot accepted/unknown test remains unchanged.
The same full cold matrix is the regression for this correction; no redundant
new test framework is necessary. Missing source stays an SDK error, already
covered by dd90 send_discovery_test.go:402–458; do not add a production fallback,
synthetic path, relaxed identity, timer slack, extra assignment or SDK pin.

**Finite checks and history.** From R's declared Nix environment run one focused
batch (no run authorized here):
`nix develop --command go -C portal test -mod=readonly ./internal/workspacecodex -run '^(TestColdAssignmentAndProgressReceiptsRemainKnownAfterExecutionWithoutBrowser|TestColdAssignmentRetryPreservesPersistedHotSendOutcome|TestManagedSendMatureHistoryDiscovery|TestManagedSendDeliveryDiagnostic|TestRetryRetentionManagedSteersBeyond64AndExactReplay)$' -count=1 -failfast -timeout=2m -v`.
Expected test execution seconds to under one minute with prepared inputs; cold
matrix was0.80–0.84s in failed CI. First different failure stops for its exact
cause, no retry or timeout increase. Acceptance needs all40 cold cases and the
accepted/unknown/history-only replay regressions passing, no assertion removal,
and an otherwise test-only diff. Normal package checkPhase later supplies the
full Go suite; do not send another original packaged run with this focused
selector omitted. Quick checks precede independent affected review.

This hunk belongs to the newest resumable-discovery consumer commit7b, which
introduced the precondition, not the older maintenance/9085 behavior. Consolidate
with that logical change under main's Git allocation, preserving its author/
message and the other accepted15-commit series boundaries; retain the
published7b receipt/ref and reviewed old/new range/equivalence. No rewrite of
preserved full8a/719/W67/C304 lineages. Current W3691/Ca7f2 review may finish its
exact existing scope independently. Successor consumer pins can be mechanical
only after final test-only R diff, unchanged SDK/production inputs and exact
nested/channel lock deltas are proved; main owns that disposition.

**Delivery impact.** SDKdd90 and production contracts/schema/authority/recovery
stay unchanged; no SDK review/CI rerun. A changed R test still changes its
unfiltered package/check derivation, so build current package outputs and use
one newly published original R CI (fast/archive/creation), retaining this failed
attempt honestly. No local duplicate archive/creation. Prior selection10782
continues: exact reuse for unchanged host/native/service/Ruby filtered inputs
requires retained successful DRV/input/output evidence; do not infer partial
CI success by name. Main reconciles any already-launched A recovery effects;
this note neither observes nor cancels them. W/C must select final R and build
final configured artifacts; C provenance bytes change despite unchanged host
behavior. Final configured native11 once remains required. Do not repeat an
already accepted native5 solely for this unrelated test edit if its actual
production/SDK/native/harness inputs are proved unchanged. No new native/live
monitor: original8e92318c/event99ab2be3 and idle acceptance remain unresolved.

Only this design append changed under the nonblocking tracking lock, released
immediately. All read commands/cells terminal; no source/Git/pin/Nix/check,
network/CI/live/native/claim/lifecycle mutation. One report attempt only;
main may read this record directly. Effects/capacity returned; session open.


### Approved integration after the verified idle wake: order and lineage

2026-11-08; bounded disposition only. Current/env/fresh architect roster match;
settings retained. Read workspace Git/coordination/deployment/lifecycle routes and
selected Q9yib coordination guide; unchanged documentation/verification guidance
reused. No fetch or live query. The saved idle-wake-4ac77e89-accepted.json under
/tmp/lead-wakeup-aitherdev-rollout-c2n4xj47/repair-usability binds passed command,
acceptedeventa0a68ece/steered:false, old-turn completion and NEW lead turn
01a1bd12-8856-74e1-9488-d117d063fd22. Its approval names all five repositories
below/master. Thus the user's conditional merge/release direction is effective;
no new product/verification decision is needed.

**Minimal order:** SDK, R, then W/C (either consumer order), with fresh proof that
the extension dependency is already on its default. Preparation is independent
of short merge claims. Two implementer packages can proceed now: SDK+R ancestry/
hook/equivalence preparation; W+C baseline/consumer/equivalence preparation.
W/C final pins depend only on the settled R successor disposition, not on waiting
for unrelated checks. Preserve existing immutable pins if integrated lineage is
proved; do not repin solely because a remote branch name changed. If a new R
revision is selected, refresh only the existing nested W and C channel streams,
retain one final update each and the observer patch; no new registration/tooling.

| Repository/master | Local read-only facts, not fresh remote proof | Integration disposition |
| --- | --- | --- |
| aither64/codex-web | origin/master d3a29bee; final dd90fb4308ba85617ee2a4267cc835aa9a4f11ce is2 commits ahead and contains registered original c3c2 | Prepare exact fast-forward; no checks/review replay if fresh target/feature inputs remain identical. Both SDK registrations then have literal ancestry. |
| aither64/dev-workspace | final c8edcb90dfccb720f7be6d0dd0876f254cf662cc has15 reviewed commits from3bb08df2; recorded default240a53da has one separate creation-fixture commit | Cannot ff c8 onto240a. Implementer prepares an equivalent successor outside claims, preserving the default diagnostic/assertions and all reviewed feature behavior. Current default change touches test/creation_acceptance_browser.cjs (+25/-2), so this is an explicit affected fixture/input boundary, not a reason to re-audit production. |
| vpsfreecz/dev-workspace | deployed extension f8da821e3c76e26e73aa9d89a712eab0e0faa319 equals recorded origin/master; registered e4e7e95e is its ancestor | Already integrated locally recorded lineage; main needs fresh canonical remote proof only, no feature replay or new extension pin. |
| aither64/vpsfree-cz-workspace | final d1560dbdc7e5fb7cacb290eb090c0e91fd4fdec1 is3 commits above2b5944e8; shared master63f0b973 has later tracking/notes commits, plus unrelated dirty paths | Prepare W on the actual shared-master/fresh-remote baseline without touching unrelated files/index. Preserve75a guidance, the single runtime pin and observer patch (review proves66ca→67d→3691→d156 preservation). Unregistered Wrepair remains an explicit additional final-head obligation, not the registered W comparison. |
| vpsfreecz/vpsfree-cz-configuration | final44cd8cbaefdac0e4187a01c44ef8c89580eab9b5 is one generated pin on f4069909; recorded defaultf225fe5f is5 commits beyondf406 | Reconcile on fresh default outside claims; preserve mx2/DNS/foto/WebUI changes and their pins. Only our devWorkspace lock update is owned. f406 remains honest old/deployed base, never relabel it current. Do not run unrelated mx2/service suites. |

**Only changed-baseline work adds checks.** Keep accepted SDK/R29/native5/W6/
Q9yib/Ckycb/native11/deployment/idle evidence intact. Use ordinary range-diff,
ordered patch IDs and complete source/input comparisons against the accepted
ranges, plus required hooks and existing focused syntax/composition checks.
For R's changed creation fixture, inspect actual resolution, run its existing
syntax/driver checks and affected packaged creation if the resulting input is
changed; ordinary original CI may also run archive/fast by declaration, without
adding duplicate local runs. Preserve exact output/DRV proof where unchanged.
For W tracking-only baseline additions, prove filtered source effects; notes
are NOT excluded by workspaceSource, so do not assert package equality from
work/archive exclusion alone. C's default changes do not directly edit aitherdev,
but DNS/global configuration can feed it: compare the actual named aitherdev
inputs/output to deployed evidence before claiming equivalence. Changed provenance
metadata alone is not a runtime defect or automatic full-suite replay. Material
behavior/conflict resolutions need affected independent review/checks and, if
not independently equivalent to deployed behavior, a newly verified deployment
before release. Stop for that concrete boundary; no blanket rebuild/retest.

**Historical registrations are a separate completion constraint.** Current
portal.yml has11 registrations across these five canonical repositories. Local
ancestry proves original R8a810, R-archive-hydration-diag f161 and R-history1c066
are NOT ancestors of c8; original Cac90 and C-final-pin e3f942 are NOT ancestors
of44cd; registered Wb78 is NOT an ancestor ofd156. Earlier deployed719/W67/C304
and original observer66ca also remain retained nonancestors. Existing whole-series
reviews and wc-c8-review-reuse-certificate.json retain their supported behavior,
consolidated pin history and no-migration conclusions; they do not turn those
SHAs into ancestors. Retain every original/recovery ref and immutable SourcePackage
reader. Do not merge obsolete implementations/pins just to make a graph green.

For machine release, the selected guide's machine-retention rule permits an
independently proven equivalent integrated successor, with old/new base/head,
review/migration and actual deployed artifact mapping retained. For ordinary
session completion, every REGISTERED exact final head must still be integrated;
equivalence alone does not waive that separate rule. With the current frozen
nonancestor registrations, that condition is NOT yet satisfied and cannot be
claimed by merely merging c8/d156/44cd. Main must retain this explicit historical
registration/head disposition as open unless a separately supported, authorized
refresh yields integrated exact final registered heads while retaining recovery
refs. No silent manifest edit, unregistration, branch reset or new lifecycle
mechanism is proposed. This need not prevent machine release once the complete
deployed lineage/effects conditions are met; leave this session active/open.

**Main's merge/release boundary.** Fresh fetch/target and hook preparation are
later allocated operations. Capture comparisons for registered final branches;
save explicit old/new comparison for unregistered Wrepair. Then acquire ONE
canonical repository claim immediately before fresh target/feature/cleanliness
checks, ff-only merge with required hooks, normal SSH push and fresh remote
ancestry proof; release before CI/records. W integrates from shared master,
claim first then nonblocking dev-session-tracking.lock; if busy or baseline/hook
intervention is needed, reconcile effects and release before preparation. Never
hold multiple merge claims for the sequential order. No force/default rewrite.

Preserve selected /nix/store/9yibngx0gbiq17waqffcgszk067ngmhb-dev-workspace-0.2.0
and TOP/nix/store/kycb055vxzjn9jzz4yyfwbgf673z6q8s-nixos-system-aitherdev-26.05.20261026.718f670
with final source/input receipts. After all five deployed dependency lineages
have fresh integrated/default proof, main reads authoritative status for exact
held claim5ed5527b-c5b0-42fe-8d2d-53aacf27fd81, reconciles all effects, releases
through the ordinary owner command and verifies released state promptly. Keep
original C registration/selector/logical-machine mapping. No extra UI gate,
monitor, claim replacement or lifecycle action follows.

Evidence anchors: repair-usability/{idle-wake-4ac77e89-accepted,wc-c8-main-acceptance,
wc-c8-review-reuse-certificate,c8-host-accepted,c8-profile-accepted}.json;
review-cold-rollout-fixture-c8.md and review-consumer-send-discovery-3691.md;
portal.yml; local exact refs/merge-base checks above. Remote freshness and prepared
successor equivalence remain execution-owner work, not claimed here. Only this
append under tracking lock changed; lock released, all commands terminal, no
source/Git/registration/claim/build/CI/network/live mutation. Effects/capacity
returned; session open.


### R integration conflict: preserve both diagnostic intents; proportional checks

2026-11-08; clarification of design10996, implementer0 owns the isolated rebase.
Current/env/fresh roster match architect0; retained settings unchanged. Evidence:
`/tmp/lead-wakeup-SDK-R-integration-prep-A-jm8ix3x_/receipts/r-conflict-milestone.json`
binds step7/15 at896251eb, stopped HEADace0f8fd and the sole conflict in
`test/creation_acceptance_browser.cjs`. Original c8 and deployed pins remain intact.

**Resolution:** retain the entire feature `catch` and finalizer, adding only
`settingsEvidence` to its `diagnostic` object (beside `errors, consoleErrors`).
Keep `failed = true`, bounded captures, projected record/request fields,
`browser-failure.json`, console output, capture-error handling, original `throw
error`, and failure-aware browser close. Do not retain the old additional console
call/full record/unbounded body. Keep target240a's automatically merged
`settingsProjection`, `retainSettings`, all four collection sites and exact fork
submitted-settings assertion. The settings array contains fixed stage/enum
projections, not arbitrary request bodies. This is an intent-preserving union
within the approved rebase; no new production behavior, schema, timing, retry,
permission, recovery or deployment contract. It is not a byte-identical fixture.

**Exact distinction:** the conflict itself changes only failure evidence. Target
240a independently adds a success-path POST tuple assertion absent from c8:
`{stage:"submitted-post", provider:options.provider || null,
model:"gpt-5.5", reasoningEffort:"high"}` for fork. Preserve it literally; do not
claim c8 executed that checkpoint. It checks the same selected form values passed
by unchanged `static/app.js` fork submit/client serialization; c8 already checked
final thread model/effort and the packaged explicit-alternate fork. The collection
writes also remain upstream behavior; the existing driver creates
`/tmp/creation-evidence` before browser use. Review must confirm these upstream
hunks survive and the union adds no success-path control-flow/assertion changes.

**Smallest acceptance batch on the completed successor, in its Nix environment:**
`nix develop --command node --check test/creation_acceptance_browser.cjs`, then
`nix develop --command go -C portal test -mod=readonly ./internal/web -run
'^TestShippedBrowserClientMatchesSessionAPI$' -count=1` (one shell command with the
selector). The latter is the documented deterministic shipped-client/fork and
preparation contract entry, not a browser/native/VM run; it does not execute the
new Playwright checkpoint or force the failure branch. Syntax should take seconds;
focused test normally seconds with prepared environment/cache; reassess unexpected
preparation or >2min rather than broadening. Stop at the first failure.
Independent affected review inspects both parent intents, final resolved catch,
upstream assertion/data flow and complete old/new range-diff; retain the existing
whole-series/migration conclusion and separately prove production/input equality.

**Refines10996:** no additional creation VM, driver build/type campaign, native11,
R29, consumer artifact rebuild or deployment is justified by this one-hunk union
or merely changed Nix source hashes. The Python driver body/types are unchanged
by the resolution; `.#checks.x86_64-linux.session-creation.driver` preparation would
not validate the JS catch. Reuse accepted c8 passing scenarios only as behavioral
evidence for their unchanged paths, not as a new-head derivation/tuple-check pass.
The inherited stronger assertion is accounted by unchanged serializer/settings
source, the focused contract check and affected review; it alone does not require
replaying the full VM for this integration. If review finds a changed actual
success predicate/serializer/settings behavior beyond the preserved target hunk,
return that precise gap to main before choosing an existing packaged scenario.
Ordinary CI declarations/hooks remain unchanged; do not duplicate automatic runs.
No live/pin change follows from this disposition.

Only this design append changed under the nonblocking tracking lock. No source,
index/rebase, check/build/CI/network/claim/live action by architect0; read commands
terminal, lock released, effects/capacity returned. Main retains acceptance;
implementer0 may apply the simple union within its existing allocated window.

Transport completion: direct clarification9a671090 delivered to implementer0;
command39020 natural0. Lead reportec0509d5 confirmed delivered. No owned
commands/cells or uncertain sends remain; effects/capacity returned.
