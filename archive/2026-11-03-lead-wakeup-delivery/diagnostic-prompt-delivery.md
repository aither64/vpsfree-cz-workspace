# Prompt delivery diagnosis

Owner: implementer2. The baseline diagnosis below predates implementation
authorization. See the implementation follow-up near the end for Package B.

Original scope: diagnosis and proposal only. No application edits,
Git mutations, package selection, live runtime changes, lifecycle actions or
peer-session access. Session identity verified with `dev-session current` and
both matching environment values before session access.

## Conclusion

The existing Go transport can start a lead turn while idle and steer an active
turn. The smallest candidate is a runtime-owned operation delivery record using
`codex.SendWithOptions` and `ReconcileSendWithOptions`, with the readiness and
immutable-delivery pattern already used by session communication. A temporary
watcher still needs a supported operation identity and durable completion bridge;
the transport alone does not enroll it or observe its completion.

Do not reuse the Ruby coordination outbox unchanged: it intentionally switches
native message IDs after failed sends, allowing duplicate status messages. Do
not use native queue persistence as proof of wake-up: cold queues remain unloaded
until explicit activation. Do not route utility reports through cross-session
grants or retained team identities.

## Source identity and evidence levels

Read-only checkouts:

| Repository | Examined revision |
| --- | --- |
| dev-workspace | `c2182254d29c4175c3e9fe4267e5a92dd1da6b79` |
| codex-web | `d3a29bee90ef00a08816920408c596152339a637` |

The first pins the second in its flake and Go module. References below are paths
relative to those repositories at these revisions. This report distinguishes
source contracts, disposable RPC fixture checks, and native-live behavior.
No native-live utility completion or idle-lead activation was exercised here.
The user's supplied native failure is seed evidence, not independently reproduced
by this package.

## Existing delivery boundaries

| Boundary | Source evidence | Implication |
| --- | --- | --- |
| Idle vs active dispatch | codex-web `codex/client.go:5277`, `:5381`, `:5423` | `SendWithOptions` resumes with policy, observes the active turn, calls `turn/steer` with `expectedTurnId` when active, otherwise `turn/start`. Model/effort accompany idle start only. |
| Stable native acceptance | codex-web `codex/client.go:5196`, `:5232` | Reconciliation never sends. Accepted attempts return the saved receipt; submitting attempts search history for the original client ID/text. Absence stays uncertain. |
| Durable state | codex-web `docs/submission-storage.md:3`; dev-workspace `portal/cmd/workspace-portal/main.go:55` | Managed clients share a private persistent SQLite submission database keyed by socket, with predecessor JSON fences. The record binds text, action context and turn options. Native client IDs correlate messages; they do not themselves deduplicate. |
| Queue persistence | codex-web `codex/client.go:4699`, `:5079` | `QueueWithPolicy` may execute immediately when loaded, but never loads a cold thread. `StartQueueWithPolicy` verifies the FIFO head before resume/start. Adding a queue row alone cannot establish wake-up. |
| Retained team reporting | dev-workspace `portal/internal/teamruntime/reporting.go:20`, `:55`; `runtime.go:2322`, `:2428` | A report resolves an exact ready roster thread and active root, then uses the shared send primitive with a stable message ID. The roster gate intentionally excludes a temporary utility. |

Browser attention/push notifications are a separate user-facing channel, not a
lead-turn submission mechanism. In particular, member completion alone cannot
trigger a session completion notification (`docs/browser-notifications.md:148`).
An attention event or push outbox entry cannot satisfy the wake-up acceptance.

The transport has a per-client queue mutex and durable admission claim. The
embedding application still must hold its common session/admission fence across
readiness and dispatch. Native `turn/start` has no compare-and-start field and can
join a concurrently active regular turn; `SendReceipt.Steered == false` proves
the selected client RPC, not atomic native exclusion against unmanaged writers
(codex-web `docs/reference.md:232`). Preserve that limitation rather than promise
global ordering or exactly-once external effects.

## Closest durable worker pattern

The session-communication subsystem is a useful implementation template, not
utility authority:

- `portal/internal/communication/service.go:251` lists pending, held and
  submitting records; `:264` dispatches under session locks and the private store
  lock. It re-resolves identities, saves the immutable envelope/options before
  sending, and retains the same ID through restart or unknown outcomes.
- `portal/internal/communication/native.go:28` binds the retained root plus
  observation incarnation and refuses unfinished lifecycle work. `:97` checks
  provider admission, exact ready runtime authority, root/socket, recovery socket
  epoch and active permission, native thread/cwd and known activity. User input
  and approval waits hold delivery; working, idle and automatic waits are allowed.
- `portal/internal/web/communication.go:106` runs the worker without a browser.
  Its two-second scan uses bounded batches and current-generation admission.
- `portal/internal/communication/service.go:310` reconciles a submitting message
  before checking whether its authority remains active. Revocation cancels
  unsent messages but can still resolve an already accepted send without issuing
  a replacement. Terminal delivered/canceled records do not dispatch again.
- `portal/internal/communication/service_test.go:118`, `:161`, `:199` contain
  restart/lost-ack, revoke/archive/identity-change and revoke-after-submission
  fixtures. `native_test.go:30` checks readiness holds and preserved instructions.
  These communication tests were inspected, not executed in this package.

Reuse/extract the readiness and same-ID reconciliation shape while leaving
pair grants and peer messages alone. Utility ownership needs its own exact
session/operation/generation authority, established at launch. No existing
utility-to-outbox enrollment was demonstrated by this diagnostic package.

## Unsafe reuse boundaries

The coordination path is a current example of actual start/steer dispatch:
`portal/cmd/workspace-portal/coordination.go:105` reconciles before sending with
saved options, and `coordination_test.go:17` checks the two RPC paths and duplicate
same-ID calls. Ruby owns admission and the outbox, not this private Go helper.

However, `libexec/workspace-coordination.rb:955` changes the native message ID
when `attempts > 0`. Its comment explicitly permits duplicate status messages;
`test/workspace_coordination_test.rb:1358` asserts the new-ID retry behavior.
The general retry loop at `:985` backs off up to 60 seconds but keeps retrying.
An unknown native result therefore can create another lead turn under a new ID.
That is incompatible with strict one-completion delivery and no replay loops.

The same outbox holds undelivered messages on archive/delete at `:505` but
restores held messages to pending on revival at `:666`. A utility completion
design must explicitly choose cancellation/hold behavior and must not inherit
automatic revival replay accidentally. The owner and generation checks at
`:1078` and `libexec/workspace-coordination-host.rb:618` remain useful invariants.

Direct ordinary sends are not an automatic readiness policy:
`portal/internal/workspacecodex/recovery.go:36` can queue and explicitly activate
a held conversation for an assignment. An automatic completion worker must pass
the stopped/recovery readiness checks before calling that path. Preserve the
documented policy in `docs/dev-sessions.md:613`: after App Server/runtime loss,
saved work waits for user activation; portal-only restart on the same server
preserves active work.

## Focused verification

Existing tests only, with disposable `t.TempDir` state and Unix sockets. A fresh
catalog verification watcher owns this batch, using `gpt-6-luna`/`low`, operation
lifetime, fresh context and full-access/never native configuration. Catalog
digest: `495ef6620926420612ee4988e69d03a4e975e41734a1a5e3208db65fcd731db7`.

Result: both commands passed once, exit 0. dev-workspace took 11 seconds;
codex-web took 72 seconds, including Nix setup. The named coordination test
passed for idle and active leads, asserting `turn/start`/`turn/steer` and one
native mutation for two same-ID sends. All eight selected codex-web tests passed,
including cancellation admission across JSON/SQLite and idle/active cases,
same-ID restart receipts, unknown-outcome refusal and cold queue behavior.

Complete disposable logs:
`/tmp/lead-wakeup-prompt-checks-1793741240/dev-workspace.log` and
`/tmp/lead-wakeup-prompt-checks-1793741240/codex-web.log`.
An ignored Nix SQLite evaluation-cache busy warning did not affect either check.
No kernel build, retry or still-running test process was reported. Fixture
temporary state/sockets were owned and removed by Go test cleanup; compact logs
remain as disposable supporting evidence.

Commands:

```sh
# dev-workspace checkout, exact revision above
nix develop --command env DEV_WORKSPACES_CODEX_PROVIDERS=/tmp/lead-wakeup-absent-test-providers go -C portal test -mod=readonly ./cmd/workspace-portal -run '^TestCoordinationNotificationRetainsSettingsAndDeduplicatesNativeDelivery$' -count=1 -v

# codex-web checkout, exact revision above
nix develop --command go test -mod=readonly ./codex -run '^(TestSendWithOptionsUsesStartAndSteerProtocolFields|TestOriginalSendOptionsSurviveSettingChangesAndReconnect|TestSendWithOptionsRetainsUnknownOutcome|TestCancellationDuringDurableAdmissionRemainsRetryable|TestPreparedSendSurvivesRestartAndRetainsAcceptanceReceipt|TestAcceptedSendRetryUsesDurableReceipt|TestSendRetryFailsClosedWhileRecordedAttemptIsAbsent|TestQueuePolicyPrecedesLoadedExecutionAndKeepsColdThreadsUnloaded)$' -count=1 -v
```

These prove specific client RPC behavior against controlled App Server fixtures,
not stock native execution or a running utility completing after its parent is
idle. Even a passing suite cannot close that acceptance gap.

## Minimum proposed implementation/test boundaries

1. Generic dev-workspace owns a durable operation registration and outcome
   record, separate from retained team rosters. Bind workspace incarnation,
   session/root/socket generation, opaque operation identity, exact source/run/
   attempt and allowed outcome revision at launch. Persist completion before
   notification so disconnect cannot erase the event. Enrollment/authentication
   is the other diagnostic package's boundary; this report does not prescribe
   a token format or claim a bridge exists.
2. Add one operation-delivery worker using existing persistent submission
   storage and `ReconcileSendWithOptions`/`SendWithOptions`. Store an immutable
   application envelope, one stable native message ID, action context and options
   before the first send. Do not derive a fresh native ID after uncertainty.
   Revalidate current authority before new dispatch; saved options do not grant
   continuing permission after settings or ownership changes. Retry
   definitely-unsent failures; retain unknowns for same-ID reconciliation
   and visible attention. Bound escalation so notification of a notification
   cannot create an automatic loop.
3. Reuse the communication readiness/fence pattern for provider pause, stop,
   socket epoch, restoration holds, pending lifecycle and user waits. Cancel
   unsent operation events on revoked ownership/archive; reconcile uncertain
   sends without permitting a fresh send. Revival/reused slug must not regain
   operation ownership implicitly. Do not weaken ordinary team reports.
4. Quick tests should assert native method, exact recipient thread, input and
   run/attempt/outcome identity, one same-ID acceptance, active-turn settings
   preservation, restart/lost-ack reconciliation, definitely-unsent cancellation,
   cold queue behavior, stop/recovery/provider/user-wait holds, revocation races,
   archive and identity replacement. Existing transport contracts need no
   demonstrated codex-web API change; keep its schema unchanged if practical.
5. The later native end-to-end test must launch a disposable owned watcher and
   lead, end the lead's turn, complete success/failure/escalation independently,
   and observe a new lead `turn/started` plus the exact completion in native
   history and the durable receipt. Repeat busy steering, browser absence,
   transport/portal restart, operation cancellation and stale generation. Use
   stock pinned native App Server with a synthetic model backend where needed;
   do not treat a text log or collaboration message as turn activation.

Compatibility: prefer additive private operation state and unchanged submission
ledger formats. A candidate package that can create durable operation records
must also preserve them during rollback/forward recovery and reject incompatible
readers before any replay. Older packages cannot be assumed to deliver new
records; recovery must remain visible. Existing session manifests, lifecycle
journals, roster settings and cross-session authorization formats need no
established change. Exact final storage schema, operation authority and whether
stop holds or cancels unsent operations belong to architect/lead synthesis.

## Implementation follow-up: Package B

The user subsequently authorized implementation through the lead. B follows
architect0's finalized `design.md` and A's concrete operation/transaction types.
Session identity and implementer2's retained workspace-write access were verified
again before source edits. A owns the shared Git index and commits; B made no
Git mutation, deployment, package selection or session lifecycle action.

Source files added in the generic runtime:

- `portal/internal/monitoroperation/{delivery.go,native.go}`: immutable same-ID
  delivery, native readiness, exact cold utility termination and missing-report
  fallback, plus read/reconcile-only receipt recovery for canceled status and
  resolution. Submitting receipts reconcile before current-authority checks;
  unknown and queue-only receipts never become a replacement send or an asserted
  activated turn.
- `portal/internal/web/monitor.go`: the existing portal owns a bounded background
  worker, without a browser dependency. It uses configured lead transport,
  current lead settings and retained instructions, provider readiness, ordinary
  runtime/team admission and operation transactions. Generation-lock waits and
  native reads use the interruptible operation context.
- Matching `delivery_test.go`, `native_test.go` and `web/monitor_test.go`.
  `web/server.go` has only the coordinated startup call alongside communication.

Focused checks in the repository Nix environment:

| Check | Result |
| --- | --- |
| B delivery/observation/native fixture cases | Passed; Go test time 0.544s |
| `./internal/web -run '^TestMonitorPortal' -count=1` | Passed; 0.120s |
| New read-only status reconciliation + exact native transport rerun | Passed; 0.180s |
| Owned-file formatting and whitespace checks | Passed |

The status fixture initially used a noncanonical `time.Now()` timestamp, which
failed the store's immutable timestamp comparison after a saved transaction was
round-tripped through JSON. Production paths already normalize timestamps to
UTC. The fixture was corrected to UTC, and the affected test passed. No failed
check was accepted through an unexplained rerun.

The native adapter fixture uses a real Unix WebSocket client and persistent
SQLite receipts. It checks actual `turn/start`/`turn/steer` requests, exact event
input, no active-turn settings override and one native mutation across client
restart. It still uses a controlled server, so it does not replace D's stock
native acceptance gate. Readiness tests cover stopped execution, stale/wrong
activity, provider pause, user/approval waits and a changed daemon epoch.

B source is ready for A's coordinated combined compile/quick batch. The last
worker refinement changes generation admission to use the operation cancellation
context; the combined batch will cover it. Intended changes remain uncommitted
until A's coordinated commit. Independent final review and long/native acceptance
remain pending. C owns lifecycle/MCP construction and consumes the read-only
receipt helper; D owns shared feature guidance and the native acceptance fixture.
Non-obvious B invariants are documented beside their source boundaries.

## Handoff

Lead owns shared state and synthesis. This is a findings and package-evidence
artifact, not completed initiative verification or deployment.
Session remains open:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-03-lead-wakeup-delivery/
