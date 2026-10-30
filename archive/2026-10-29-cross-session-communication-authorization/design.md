# Cross-session communication authorization design

Final implementation and verification are summarized in [handoff.md](handoff.md).
The final fixture recovery note supersedes earlier fixture assumptions about
automatic recovery flags and cached UI activity; production uses fresh observer
admission and the full actual-worker idle/steer exchange passes.

Design owner: architect0. Implementation brief, 2026-10-29. The lead accepted
the single-repository boundary and delivery-time authorization context design.

## Scope and source evidence

One user approval of an exact pair in either session must let both leads
communicate. The receiving lead must distinguish the runtime's verified grant
from untrusted peer assertions and must not request duplicate approval.

Only `dev-workspace` needs application changes. Examined base:
`08f3dbb92bc8585929edee85a824d44dfb3b0846`. Worktree:
`worktrees/2026-10-29-cross-session-communication-authorization/dev-workspace`;
branch: `2026-10-29-cross-session-communication-authorization`.

Existing ownership:

- `portal/internal/communication/service.go`: bidirectional grants, message
  admission, fresh dispatch validation, saved envelopes/options, revocation and
  reconciliation. `store.go` owns strict schema-1 state and capacity reservation.
- `portal/internal/communication/native.go`: exact lead resolution, recipient
  holds, retained role policy and native delivery.
- `portal/internal/workspacecodex/lead_policy.go`: refreshed technical developer
  policy, separate from saved role instructions.
- `portal/cmd/workspace-portal/team_mcp.go`: native caller binding, tool schema
  and CLI dispatch. `communication.go` owns the command receiving that request.
- `portal/internal/web/communication.go`: authenticated portal approval and
  generation-guarded queued delivery worker.
- `docs/session-communication.md` and its upgrade companion own lasting behavior
  and recovery guidance.

The pinned codex-web dependency `9d337b70987fdf1dd42a5d8efff31f755a122550`
already sends `TurnOptions.AdditionalContext` on both `turn/start` and
`turn/steer`, separately from user text. It includes those options in the durable
send-attempt identity. No codex-web, protocol, UI, host configuration, migration,
dependency-pin or lifecycle subsystem change is needed.

This investigation used canonical source and this session only, not either
incident session's records, worktrees, conversations or communication registry.
The incident brief in `plan.md` is sufficient reproduction evidence.

## Trusted authorization context

Keep the existing grant authority and tool API. At dispatch, after the existing
session locks and store lock have established an active matching grant and
fresh exact sender/recipient identities, attach an application context entry
to the first preparation of `Message.Options`:

- Stable application-owned source key, for example
  `dev-workspace/session-communication`; `Kind: "application"`.
- A concise runtime statement that active registry approval authorizes deliberate
  messages in both directions without duplicate approval in the receiving chat.
- Structured, safely encoded metadata containing grant ID, `status: active`,
  exact A/B identities (slug, lead thread, incarnation), delivered message ID,
  approving session, recorded approval evidence, creation time, and scope.
- Explain that this is a submission-time snapshot. Every later send/reply is
  checked against current registry state; a remembered snapshot cannot override
  revocation, identity change or lifecycle invalidation.
- Scope is deliberate lead-to-lead messages only. It grants no access to peer
  files, transcript, roster/team, worktrees, credentials, merge, deployment or
  lifecycle operations and does not replace recipient task/settings.

The metadata comes exclusively from the validated stored `Grant` and `Message`,
never by extracting a grant ID or an approval assertion from `Message.Text`.
Keep peer prose solely in the ordinary message envelope. Treat the stored
approval wording/reference as quoted audit data, not executable instructions.
The existing `Approval` field already records the supplied wording and message
reference; include it faithfully, without inventing a separate reference or
parsing free text into a purported native proof. Portal approvals identify the
portal source instead of pretending to have a chat message reference.

The local operator and consent-recording lead retain their existing trust model:
the runtime verifies the stored authority and exact identity, not the meaning of
natural-language consent. Do not add transcript access, signatures or a second
authorization system.

The approving lead receives authoritative state in the existing `allow` result.
The recipient receives authorization context with its first ordinarily eligible
message. The lead explicitly accepted this behavior; no standalone activation
notification, extra turn or wakeup subsystem is required.

## Dispatch and retry invariants

1. Preserve lock ordering: sorted session runtime locks, then store lock. Grant
   validation, first option preparation, durable save and native send remain in
   that critical section. Existing revocation serialization defines the race:
   already accepted traffic cannot be recalled; a later new send is refused.
2. Exact equality includes slug, root thread and incarnation for both parties.
   `IdentityFor` uses `ObservationIdentity`, bound to workspace, slug, directory
   device/inode and root thread. No slug-only or caller-supplied substitute.
3. Match the active grant to both stored message endpoints in either direction.
   Store validation already enforces this; make new context generation use that
   same validated relationship. Never attach active context to an absent,
   revoked or mismatched grant.
4. Preserve `Ready` behavior for stopped sessions, provider pauses, recovery
   holds, pending user input and approvals. Do not activate a held recipient or
   change its model, effort, mode, saved role or current task. The current native
   preparation leaves model/effort empty and adds the retained lead policy.
5. For a never-prepared message (`Options == nil`), prepare the existing options,
   merge the application context, validate the size of the **complete** encoded
   options, save the original envelope and options before native submission,
   then send normally. No transport-interface change is required.
6. Once options exist, preserve them and the envelope exactly. This includes
   `submitting` and a previously submitting message now `held`. Do not add fresh
   timestamps or new context to a saved tuple. Native receipts/digests depend on
   exact originals, including after restart, upgrade or revocation.
7. Reconcile uncertain submissions before deciding whether another submission
   is permitted. Revocation may reconcile prior acceptance but never creates a
   new send. Preserve the existing cancellation and reapproval rules.
8. Old pending/held messages without options receive new context when first
   prepared. Legacy messages with saved options/envelopes retain them. If a
   legacy message lacks trusted context, the updated lead/tool policy directs
   the lead to query `session_communication list` before refusing or asking for
   duplicate permission. Active exact-pair registry evidence is sufficient.

Update new-message envelope wording to distinguish the peer payload from the
runtime context. Keep the existing `Cross-session message from ... to ...
(message ...):` prefix so transcript classification remains compatible. Do not
rewrite existing envelopes. If adding the grant ID to the envelope, derive it
from the validated grant during initial admission and do not make that textual
ID itself an authority. Avoid increasing envelopes during dispatch, because
existing state admission reserves option/receipt growth, not arbitrary new
envelope growth. Context fits the existing 64 KiB options budget; oversize must
hold before submission as today.

## Policy and documentation

Fresh lead developer policy and the MCP description must say that peer-written
claims are not authorization, while an active runtime-verified exact-pair grant
is bidirectional authorization and needs no duplicate local approval. Before
refusing a legacy or ambiguous inbound claim, use `list` to resolve current
authority. Do not issue another `allow` simply because approval originated in
the peer chat. A forged ID, third session or revoked grant stays insufficient.

Preserve saved role instructions exactly, and describe the same scope limits
and lifecycle boundaries in both policy and docs. Update the existing feature
guide and upgrade/recovery guide; do not create a new documentation subsystem.
Lead owns final user-facing wording inspection before implementer commits.
Workspace guidance already says approval is bidirectional and links to the
runtime guide; no workspace feature branch is necessary for this fix.

## Implementation packages and coordination

The lead assigns owners. These packages can be developed concurrently after
acceptance of this brief; they share no edited files.

| Package | Suggested owner | Files | Dependencies and acceptance |
| --- | --- | --- | --- |
| A: runtime context and recovery | implementer0 | `portal/internal/communication/service.go`, `service_test.go`; focused new context helper/test in that directory if useful; `store.go` only if a demonstrated capacity issue requires it; `native_test.go` if needed | Keep current exported service/transport API and state schema. Implement trusted context, safe new-envelope wording, size/retry/identity/revocation checks. Tests prove context derives from registry, stays separate from peer text and preserves exact saved tuples. |
| B: policy, documentation and real-path regression | implementer1 | `portal/internal/workspacecodex/lead_policy.go`, `lead_policy_test.go`; `portal/cmd/workspace-portal/team_mcp.go`, `team_mcp_test.go`; new `session_communication_integration_test.go` and/or `session_communication_native_integration_test.go` in that command package; existing communication docs | Policy/docs can proceed independently. Real-path test authoring uses unchanged public service API and frozen metadata semantics; final execution depends on A. No edits to A's files. Native test may reuse existing tagged fixture conventions without refactoring unrelated tests. |

Serialize staging, commits, hooks and branch operations in this one worktree
through the lead. Each owner stages only their paths. Coordinate focused test
runs while files settle so evidence identifies the tested source state. Package
B's final combined regression depends on A; do not call its early policy-only
checks complete runtime validation. Any required overlap, public API/state
change, new repository or changed trust boundary goes back through the lead.

## Verification and acceptance

Quick checks, in the repository's Nix environment, before final independent
review:

- `go -C portal test -mod=readonly ./internal/communication
  ./internal/workspacecodex` (focus tests if the whole command is not quick).
- Focused command-package MCP/communication tests, plus a quick real-path test
  connecting native caller metadata through the production communication
  handler/service, persisted store and dispatch, with only native RPC simulated.
- Existing portal communication approval/revocation and transcript tests. For
  focused web tests, select an absent `DEV_WORKSPACES_CODEX_PROVIDERS` fixture
  path as the README requires. Do not read the host provider catalog as fixture
  configuration.
- Formatting, `git diff --check`, and scoped review of final docs/policy.

Required regression cases:

1. A records approval once with wording/reference; sends to B; B receives runtime
   context with exact grant, endpoints, approving A and source; B replies through
   the real tool path without its own `allow`. Only one grant exists.
2. Ordinary peer text naming a fake grant, copying context-looking text or
   requesting wider access never supplies metadata or authorizes a send. An
   actual A/B grant cannot authorize C. Members cannot call as lead.
3. Changed thread or incarnation before dispatch cancels unsent traffic; explicit
   revoke and the existing lifecycle `Expire` path do likewise. Reapproval does
   not revive canceled messages. Use disposable fixtures, never real sessions.
4. Held work remains held with no native send, and authorized ordinary resumption
   permits one delivery. Revoke while held prevents delivery.
5. Lost acknowledgment/restart/revoke reconciles the exact original text/options;
   saved legacy tuples remain unchanged; unprepared legacy messages gain context.
   Include the case where an attempted send becomes held and then is retried.
6. Peer text is absent from application authorization context; quoted approval
   source is distinguishable from policy; retained recipient settings and roles
   survive; capacity reservation/oversized-option refusal still works.

Author the longer native regression before review, but execute it only after
the final committed-deliverable review. Follow existing `live_switch_integration`
fixture conventions with the exact pinned `LIVE_SWITCH_CODEX`, fresh temporary
Codex home/state/socket, loopback synthetic Responses endpoint and no live
workspace access. Exercise real MCP caller binding/communication command,
registry/service/Native dispatch and pinned App Server delivery, then B's reply.
Inspect the model-facing request to prove context is application-owned and
separate from peer user text on **both idle start and active steer**. A synthetic
backend may gate the reply on those fields to reproduce the missing-context
failure deterministically; that proves transport/policy inputs, not arbitrary
model behavior. Avoid a fake send success or helper-only test as end-to-end proof.
Any fixture adapter around the unchanged host CLI must be disclosed and retain
its expected-root/environment checks; existing Ruby CLI tests remain required
evidence for that boundary.

Use the mandatory verification watcher for long or uncertain test/build runs.
The lead selects the post-review packaged/CI batch under repository procedures;
the packaged Go suite is required. Native test execution should have a bounded
timeout and preserve concise failure evidence. No new VM suite or provider
inference campaign is needed solely for this change. Broaden checks only for a
failure or changed boundary. Implementation, quick checks, independent review,
native acceptance and deployment remain distinct milestones.

## Compatibility, deployment and recovery

No manifest, grant/message schema, database, CLI argument, MCP tool argument or
runtime contract version changes. Existing `TurnOptions.AdditionalContext` is
already supported by the selected dependency and native package. Schema-1 state
keeps the same fields; new context lives inside the existing saved options.
Old readers supporting this communication contract can decode those options.
An older package would omit the improved context for new deliveries and restore
the original ambiguity; do not call that equivalent behavior.

Preserve the existing generation guard, single selected worker, forward-only
package transition and communication recovery contracts. In-flight tuples are
never migrated to new wording. Do not erase state, replace stable IDs or bypass
holds to obtain new context. After any future authorized deployment, validate
with dedicated disposable sessions and verify tools, both delivery modes and
conversation continuity. No deployment or integration is authorized here.

No vpsAdmin/API/Terraform/database/OS-node compatibility impact, coordinated
fleet update or credential handling is introduced. The runtime application alone
owns delivery; host modules and the incident sessions need no inspection/change.

## Remaining implementation checks

The architecture and owner split are settled. Implementers must establish the
exact model-facing native representation of application context (especially on
steer), verify combined options fit the existing bound, and demonstrate saved
tuple compatibility through tests. If native evidence contradicts the documented
start/steer contract, report it through the lead before expanding scope. These
are concrete implementation checks, not reasons to extend design exploration.

Next observable milestone: package A's passing context/retry regression and
package B's changed policy/docs plus authored real-path regression, followed by
serialized commits and final independent review.

## Addendum: production activity composition (2026-10-30)

### Proven gap and affected consumer

The original runtime/policy deliverable passed independent review. Its subsequent
native fixture exposed an additional composition defect, confirmed by source at
clean head `ace1577a2d0bf50b4117d01e183d7f788267f5ec`. The changes between the
reviewed head and this head were test-only; this gap is in production wiring.

The production path is:

1. `main.go:configuredCodexClient` creates `workspacecodex.Client` without an
   `ActivityRecorder`. `workspacecodex.NewWithOptions` does not add one and has
   no `ReadActivity` override, so reads use its embedded ordinary codex client.
2. `web.NewContext` starts `startActivityMonitor` before `startCommunication`.
   The monitor creates a separate `ObserverOnly` codex client with an activity
   recorder and background subscriptions. Those subscriptions run without a
   browser, gated by retained session identity, runtime authority, lifecycle,
   provider and recovery state.
3. `web.communicationService` currently supplies `s.config.Codex` directly as
   `communication.NativeClient`. The generation-guarded background worker uses
   this service for `Dispatch`, so `Native.Ready` reads the recorder-free client.
4. Pinned codex-web `activity.go:ReadActivity` does not subscribe or resume.
   `activity_snapshot.go:snapshotContextCached` starts an in-progress turn as
   `unclassified` and needs live observation to classify it. A recorder-free
   client can return idle from completed history, explaining why idle delivery
   passed while the active native fixture held with "Recipient activity is
   unavailable".

This is a dev-workspace **web composition** repair. Do not add a recorder to the
operational client, change codex-web, relax `Native.Ready`, or refactor all activity
consumers. Existing conversation/progress/attention consumers have separate
display/evidence needs and retain their behavior.

### Minimal wiring contract

In `web.communicationService`, use a small private adapter around the existing
operational `communication.NativeClient`. Delegate metadata, send and reconcile
unchanged. Override only activity reading to use the already-owned activity
monitor's observer when present. No exported API, transport interface, package
contract, registry or state-schema change is necessary.

Add a narrow fresh-read method on `activityMonitor`, or an equivalent small
private helper in the same package. It must acquire the existing per-thread and
global read gates, call `m.observer.ReadActivity` directly, and return its result
or error. It must not use `m.ReadActivity`/`readSnapshot`: those UI paths can
return a 5-second active or 30-second idle cache, or a stale success after a
failure. Even `readSnapshot(..., true)` still has stale/backoff fallback, so it
is not sufficient for delivery admission.

The communication adapter rejects a stale snapshot or one whose `ThreadID`
does not exactly match the requested thread. Unknown/unclassified activity and
user-input/approval waiting remain handled by unchanged `Native.Ready`.
`Refreshing`/incomplete historical timing alone must not invent a new hold when
current activity is valid: history completeness is not delivery authority.
Fresh-read errors propagate to the existing held-message behavior. Do not
substitute cached working/idle state or infer working from an active turn ID.

When there is no monitor (existing non-observing embeddings/test configurations),
retain the existing direct-client behavior, with the same identity/stale guard;
never manufacture activity or create an observer on demand. Production enables
the monitor at startup. If observation has not yet established active coverage,
normal queued retries remain held until it does. No new subscription manager,
queue, timer, lifecycle action or activation permission is introduced.

Preserve these boundaries:

- `Dispatch` still holds the exact pair's runtime locks and stored grant check.
  `Native.Ready` still checks provider admission, runtime authority, exact socket
  epoch/recovery permission and recipient metadata before reading activity.
- The observer uses the same configured workspace/socket and existing
  `providerThreadResumeAllowed`/recovery gates. Provider watch recovery already
  refreshes both operational and observer clients; do not bypass or duplicate it.
- No raw observer send is permitted: delivery uses the original operational
  client, preserving workspace recovery, provider settings and native receipts.
- Fresh reads are read-only and share the existing concurrency bound. They do
  not subscribe, resume, answer blocking requests or change thread settings.
  Cancellation while waiting for a gate remains interruptible.
- Portal startup/shutdown retains current worker/observer/recorder ownership.
  A transient shutdown/observation failure holds traffic rather than falling
  back to old activity. Saved message options and grant snapshots are untouched.

### Follow-up packages

| Package | Suggested owner | Owned files and contract |
| --- | --- | --- |
| C: production activity wiring | implementer0 | `portal/internal/web/communication.go`, narrow addition to `activity.go`; focused `communication_activity_test.go` and/or `activity_test.go`. Add a short owning-guide clarification only if useful, with lead wording review. Preserve all exported APIs. Tests exercise `communicationService` and its actual dispatch/worker composition, not a hand-built `communication.Native` with a recorder. |
| B follow-up: native production composition acceptance | implementer1 | Existing `portal/cmd/workspace-portal/session_communication_native_integration_test.go`; reuse its disposable native/MCP/Responses fixture. Add or adapt a mode to build the production recorder-free operational client plus `portalweb.NewContext(ObserveActivity: true)` and let the actual communication worker deliver. Do not manually inject a recorder or subscription into that operational client. Author after contract acceptance; execution depends on C and affected final review. |

No overlap with A's service/context files is expected. B may author its fixture
adaptation while C develops; both use existing public composition APIs. Serialize
Git/hooks through the lead. If the native fixture needs shared helper changes,
keep them with B and notify the lead before overlap. Do not add production test
hooks just to expose the private worker. Inspect ordinary stored message status
and model-facing native context instead of decorating the production transport.

### Acceptance and checks

Quick tests must fail on the old composition and cover the following:

- Real `communicationService` construction uses the monitor's fresh activity
  while metadata/send/reconcile still hit the operational client. Configure the
  operational client's `ReadActivity` to reject unexpected use; prove a freshly
  working recipient reaches send through actual service dispatch.
- Populate a cached idle/working snapshot, then make the observer report
  user-input wait, approval wait, unclassified, wrong thread, stale or an error.
  Each relevant case must hold with zero sends and no stale-cache fallback.
  Fresh idle/working/automatic-wait results retain existing allowed behavior.
- Existing provider/recovery/runtime-identity holds still occur before activity
  can authorize delivery. Cancellation through a saturated shared read gate
  must return promptly and not cause native submission. Reuse existing activity
  gate tests rather than duplicating a general concurrency suite.
- Include a constructor/worker composition regression using the actual portal
  monitor setup and operational client without a recorder. A protocol fixture
  may supply native events, but it must not replace the observer with a manually
  marked working snapshot. The longer native test below can provide this exact
  constructor proof if keeping it quick would require a duplicate harness.

After quick checks and all intended changes are committed, run the explicitly
required **affected final-review rerun** for this substantive production addition.
Prior review of A/B is not review of C. Then use the utility watcher for the
bounded native production-composition case: approved A/B pair, real working B,
actual portal observer/worker, trusted application context delivered by steer,
immediate native MCP reply without local `allow`, and no recipient setting
changes. Retain existing idle/legacy/revocation coverage; repeat only affected
checks. Do not claim the manually recorded direct-Native fixture alone proves
production composition.

Focused quick command: in the Nix environment run the relevant
`go -C portal test -mod=readonly ./internal/web -run 'TestCommunication|TestActivity'`
selection with the absent provider-catalog fixture configuration already used
by web tests. Bound the selection; use a watcher if duration is uncertain.
Tagged native execution and the required packaged suite follow review. No
live/incident session access, deployment, integration or lifecycle action is
part of this follow-up. No long tests were run during this investigation.

The next observable milestone is C's small wiring diff and failing-before /
passing-after composition evidence, plus B's production-worker fixture ready
for the affected review. No additional architecture question blocks assignment.

### Fixture correction: active recovery permission

Source decision at `a6c0e10f4d0c828631a4bbf02da16fa3b6d556f5`:
`RecoveryStore.Set(..., automatic=false, activate=true)` does **not** mean active
execution with automatic recovery disabled. The setter clears `ActiveThreads`
and `Continuation` whenever `automatic` is false, after processing `activate`.
Consequently the fixture's empty active set correctly held both observer
subscription and communication. Any prior review assumption that this call
preserved active execution is incorrect; retain the original review and append
the source-backed correction and new diagnostic evidence.

Use the normal fixture initialization `Set(..., true, true)` for the exact root
and current native socket. Existing session recovery tests establish this
contract. Immediately reload and assert the root/socket tuple, automatic intent,
socket epoch and `record.Active(root, epoch)`; do not infer success from setter
arguments. This is a test-only correction, not a production or gate change.

Communication `Native.Ready`, monitor `owns`/`recoveryHeld`, and
`RequireRetainedReady` do not require `VerifyTmux` terminal proof. They retain
their exact runtime authority, root, socket, lifecycle, provider and persisted
execution checks. Do not add a terminal fixture subsystem for an unused gate.
The public activity endpoint can legitimately retain its previous idle snapshot
for 30 seconds. Do not require it to report working, wait for its cache to expire,
increase the diagnostic deadline, or use it as delivery-admission authority.
For the lead-authorized diagnostic, keep the existing five-second bound: hold
an actual native turn open, let the actual portal communication worker make the
first delivery, and require its real accepted receipt to identify the exact
message and held turn with `Steered: true`. Stop before the reverse exchange.
This directly exercises C's fresh observer admission and proves the working
recipient was eligible without relying on a displayed snapshot. Do not inject
a recorder, fabricate activity, or call `Dispatch` manually for this proof.
The full exchange remains a later check after this narrow result is inspected.

With automatic intent enabled, the separate recovery sweep may attempt `resume`
after its terminal-interactivity check. Inspect the actual helper invocation:
`runDevSession` inherits the portal process environment, while this fixture
explicitly supplies its `COMMUNICATION_FIXTURE_CHILD` marker to native/MCP
children. The test helper skips without that marker; with it, the argument guard
rejects unsupported commands before mutation. Do not call a skipped, successful
test-helper exit a refusal. If a refusal is intended, make it explicit in the
fixture's local adapter. Neither branch should write recovery state.
`web.restoreRuntime` updates its in-memory recovery-status map after helper
completion and does not itself rewrite persisted recovery permission. Record
the actual helper outcome and reload the exact recovery record after the short
check; do not assume arbitrary helpers are harmless or treat a changed record
as success. The fixture-local unsupported-command refusal trace must record
the actual call and outcome, or explicitly that no call occurred. Compare the
exact before/after sidecar and root/socket/active identity. Preserve ordinary
queued/held behavior and all existing authority checks. B owns the narrow fixture
fix and diagnostic evidence; no additional production package is indicated.

## Aitherdev rollout addendum (2026-10-30)

The completed runtime deliverable is published at
`4155d0099d03028b43d5f08d225a88156cb4155a`, with independent review, native
idle/steer acceptance and CI recorded in this session. This addendum adds two
matching composition pins and deployment; it does not reopen runtime design.
Exact baseline paths, input identities and execution receipts belong in
[rollout.md](rollout.md).

The user authorized deployment via vpsfree-cz-configuration, then said “when
deployed and verified, you can merge it and release aitherdev”. As scoped by the
lead, integration covers this feature's dev-workspace/master,
vpsfree-cz-configuration/master and workspace/master, **after deployed
verification**. Keep the physical machine reserved until settled deployment
effects and complete remote integrated-lineage proof. No lifecycle action,
incident-session access or grants between actual sessions are authorized.

### Source ownership and minimal change

Configuration's `flake.nix` maps channel `dev-workspace`, role `devWorkspace`,
to the matching host module/runtime input. Workspace `flake.nix` independently
selects the application through
`inputs.vpsfree-dev-workspace.inputs.dev-workspace.url`. The extension remains
`767dfd587e346168e1443e65ccdb67ce748f3fe3`; its own older runtime lock is not the
effective selection. Preserve the direct nested override, all follows edges,
sibling identities and locked hashes. Neither codex-web nor extension source
needs edits.

The configuration owner's
`docs/operations/codex-providers-aitherdev.md` explicitly supports application-only
profile activation. Old selected runtime `5f4f1c1c52cc009970a2697f5dbc330c0a4dd7a3`
to target has no changes in `nix/`, `libexec/`, `flake.nix`, `flake.lock` or
`portal/internal/session/runtime-contract.json`. Selected runtime contract bytes
also equal the candidate. Installed and inspected workspace composition, catalog
and coordination inputs match. Thus update the matching configuration channel
and workspace nested pin, build the composed application, and activate only its
user profile. A system build/switch, provider switch or native upgrade adds no
necessary behavior. Reassess this decision if final input comparison differs.

### Complete execution packages

| Package / proposed owner | Owned files and deliverable | Dependencies and acceptance |
| --- | --- | --- |
| D / implementer0 | Own configuration worktree: channel-generated `flake.lock` and any channel-owned generated metadata actually changed by confctl | Start at registered `b3b933bf6f9fc9f7f533b3f4e06775defd8879da`. Establish pinned Nix/gem environment and required hooks/trust first; no hook bypass. Run `confctl inputs channel set --commit dev-workspace devWorkspace 4155d0099d03028b43d5f08d225a88156cb4155a`; preserve generated history. Only intended runtime identity changes; host, provider, native and unrelated inputs remain equal. |
| E / implementer1 | Own workspace worktree: `flake.nix`, generated `flake.lock` | Registered initial base `398dc7bab89ee51bcc77d23a5acc52c7e02878c1`. Change only nested runtime URL, run `nix flake update vpsfree-dev-workspace/dev-workspace`, preserve extension/siblings/follows. Required hooks and formatting pass. |
| Verification / implementer1 with lead-owned activation | Existing source-native evidence plus selected-artifact smoke and this session's rollout receipt; no application edits | After D/E quick checks and review disposition, build exact composed package, identify its complete inputs and native executable, then perform artifact verification below. Lead performs claim/activation/integration/release. |

D and E can proceed independently in separate repositories. The final combined
`bin/check-dev-workspace-deployment --workspace-root WORKSPACE --configuration-root
CONFIGURATION` depends on both pins. Each owner supplies exact base/head, clean
status, complete semantic lock diff, hooks/check evidence and no-migration/history
assessment. Inspect the entire input graph in addition to the matching checker;
the checker is not a proof that all sibling inputs stayed equal. Keep one final
logical pin update per stream. Serialize any later overlapping Git operations
through the lead. No new reusable operations page is needed for routine pins.

### Review, verification and supported recovery

Quick checks: matching checker; semantic full-lock comparison; relevant
format/hooks and workspace deployment-contract tests; target runtime contract,
host-source and native-input equality. Commit all intended changes before final
review. The lead applies mandatory-review rules to the mechanical pins and
complete branch histories; substantive composition or fixture changes require
affected final review. Existing runtime evidence remains valid for its exact
source; do not repeat the whole suite without a changed input or open failure.

After review, a utility runs the exact composed package build and applicable
package checks. Retain output/derivation/input identities; prepare copies before
machine ownership. No build, claim or deployment was run by the architect.
The lead then performs ordinary selected `workspace-host switch --source PATH`
with the exact held machine claim and verified session identity. Same-native
live-switch policy preserves Codex, tmux and managed terminals, restarts the
portal/router and retains roster/provider settings. Do not force idle, stop
sessions, supply a native override, or use an unnecessary candidate entry.

Postdeployment proof combines selected-output/source/native identity, shipped
tool/policy smoke, and read-only live health, naming availability, own-conversation
continuity and provider/settings checks. Retain the completed source-native
idle/steer/reply evidence and its fresh-observer, recovery and receipt invariants.
The tagged test exercises the production constructor/worker inside its test
executable; `LIVE_SWITCH_CODEX` selects native only. Record that boundary rather
than claiming it executes the installed portal process. The lead accepts this
combined proof on the unchanged graph/module evidence. Do not build an additional
installed-worker harness or run new provider/DeepSeek requests without a concrete
mismatch. If an installed-binary fixture becomes materially necessary, use only
owned unregistered roots, isolated state/socket/mock provider and an exact
disposable pair; refer consequential additions through the lead. No incident
records, real-workspace grants or actual-session lifecycle calls are involved.

There is no new schema, transport or migration. Preserve grants, original legacy
saved options, queued messages, stable IDs and uncertain receipt reconciliation.
Submission-time context remains a snapshot; later send/reply revalidates current
authority. Generation fencing prevents parallel old/new delivery. On activation
failure retain the machine, roots and journals, establish actual effects and
retry the same supported switch or a corrected compatible forward package.
Do not select an older package, erase state, reset clusters or bypass refusals.

Only after deployed verification may the lead integrate runtime, then matching
configuration/workspace branches. Prepare outside claims; hold one repository
claim only for fresh checks, fast-forward/hooks, SSH push and remote proof.
Workspace integration also takes the nonblocking tracking lock. Release each
repository before CI/records. For a clean history refresh preserve exact old/new
ranges, range-diff, package/input equivalence, migration evidence and independent
conclusion. A nonancestor deployed commit is not literally merged; an accepted
equivalent successor may prove lineage. A substantive successor needs a new
verified deployment and applicable scope approval. Before machine release verify
its exact owned claim, settled effects and fresh remote lineage for all three
repositories; release and confirm state. Leave this session open.
