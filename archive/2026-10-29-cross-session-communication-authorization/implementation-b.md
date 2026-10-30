# Package B implementation evidence

Owner: implementer1. Current owning commit:
`b0279514b60fc1c33678bae733df5840705c2e6c`, after unchanged package A
`ed16c606b8b3a5ae1624e1f8dd5e7bcccf3cc387`. Original reviewed B commit was
`c43904a72d705562b79dcf9d59a29cf743bc9de7`; its narrow fixture repair is folded
into B, followed by the fixture corrections and final production-worker
adaptation/consolidation below. Final branch head includes C:
`4155d0099d03028b43d5f08d225a88156cb4155a`. Worktree is clean. No push, integration, deployment, live-runtime change or session lifecycle
action was performed. Authorized own unpublished autosquashes are recorded below.

Current correction: earlier fixture statements that `Set(false, true)` preserved
active execution were wrong; it clears the active set. Earlier claims that
portal auto-resume was definitely refused were also unproved because the
helper could skip successfully without the marker. See the final correction
below and the architect-owned design fixture note. The final fixture uses the
normal active setter and explicit, observed unsupported-command exit 64.
Original review reports are preserved verbatim.


Session and environment match `2026-10-29-cross-session-communication-authorization`
and `/home/aither/workspace/ai/vpsfree.cz`. Native read-only self-check bound only
to implementer1 thread `01a189c3-597f-7c70-8c0b-58afcea906f3` confirmed `codex-lb`,
`gpt-6.1-sol`, `xhigh`, CLI `0.165.0` and the session CWD in its thread row,
session_meta and latest turn_context. Saved roster access is `workspace_write`.

## Delivered

- Fresh technical lead policy and MCP tool description distinguish peer claims,
  copied context and textual IDs from runtime authority. An active verified
  exact-pair grant permits both directions without another local approval;
  legacy or ambiguous inbound context calls for `list` before refusal or
  requesting duplicate approval. Saved role instructions remain unchanged.
- Existing communication and upgrade/recovery guides cover quoted audit data,
  current state versus submission snapshots, message-only scope and exact
  saved-tuple compatibility. Lead inspected and accepted wording, including
  the user-facing-writing pass; requested formatting fixes are included.
- `TestSessionCommunicationRealCommandRoundTrip` exercises the real MCP handler,
  native caller-to-lead resolution, communication command in a subprocess,
  persisted service/store and Native dispatch, with only NativeClient RPCs
  simulated. It proves a single A approval, B reverse reply, exact registry
  snapshot, separated forged peer text, rejection of a third peer/member caller,
  and retained recipient role/settings.
- Tagged `TestNativeSessionCommunicationAuthorizationRoundTrip` is authored and
  compiled before initial review. The first post-review execution failed at
  fixture MCP startup; the narrow repair and remaining rerun are below. Its
  idle and steer subtests use fresh temporary
  Codex home/state/socket and a loopback Responses backend. Real native MCP
  caller metadata enters the production handler/command/service; Native sends
  to the pinned App Server. The backend emits B's reverse reply only when
  exact production-generated application context is present in a developer
  item separately from user peer text. It verifies the reply reaches A, one
  grant remains, saved roster is unchanged and idle/steer receipts agree.
  This proves the transport and policy inputs, not arbitrary model behavior.

The fixture's strict host-selection adapter replaces the installed Ruby
`dev-session` wrapper only. It checks fixture workspace/state/profile, exact
session CWD/environment, absent member identity and current expected root, then
calls production `communicationCommand`. It does not fake a send or receipt.
The existing Ruby CLI suite remains required evidence for that boundary and is
included by the post-review packaged check.

## Quick checks

All commands below ran from the dev-workspace worktree using its Nix shell.
No hook framework is declared and no active repository hooks are installed;
no hooks were bypassed. Formatting and `git diff --check` passed.

```sh
nix develop --command go -C portal test -mod=readonly \
  ./internal/communication ./internal/workspacecodex ./cmd/workspace-portal \
  -run 'Test.*Communication|TestLeadPolicy|TestFallbackLead|TestCoordinationPolicy|TestTeamMCP|TestWorkspaceTeamMCP|TestRetainedTeamMCP' \
  -count=1 -timeout=45s
```

Passed: communication 0.203s, workspacecodex 0.046s, command package 0.629s.
The preceding focused invocation also passed the real command round trip
(command package 0.524s).

```sh
nix develop --command env \
  DEV_WORKSPACES_CODEX_PROVIDERS=/tmp/communication-b-absent-provider-fixture.json \
  go -C portal test -mod=readonly ./internal/web \
  -run '^TestCommunication(PortalApprovalAndRevocationFromEitherSide|TranscriptProjection)$' \
  -count=1 -timeout=45s
```

Passed in 0.104s; the provider fixture path was verified absent.

```sh
nix develop --command go -C portal test -mod=readonly \
  -tags live_switch_integration ./cmd/workspace-portal -run '^$' -timeout=45s
```

Passed in 0.057s with no tests run: compilation evidence only.

An expanded whole-package attempt was deliberately capped:

```sh
nix develop --command go -C portal test -mod=readonly \
  ./internal/communication ./internal/workspacecodex -count=1 -timeout=45s
```

Communication passed in 6.036s. The 94-test workspacecodex package timed out
at 45.044s while
`TestRetryRetentionCachedProofSuppressedAndNewQueueEligible/member=true` was
about 1s into its 63-send fixture. The active stack was
`retryRetentionSend` -> `SendWithOptions` -> `claimSendSubmissionIf` ->
`writeQueueLedgerLocked` -> `os.File.Sync`. No assertion failed before the
whole-package timeout. This is NOT a passing full suite. Lead accepted the
bounded focused checks and deferred the full package to the post-review
watcher; no inline retry was made.

## Post-review native execution and remaining acceptance

Exact executable resolved from the current flake's `lib.mkCodexPackage`, using
its pinned `inputs.llm-agents.packages.x86_64-linux.codex` and nixpkgs:

`/nix/store/idil0dg5623qarasafiqsjfc3s2bm2a9-codex-package-0.165.0/bin/codex`

The path exists. Resolution expression:

```sh
nix eval --impure --raw --expr 'let f = builtins.getFlake (toString ./.); pkgs = import f.inputs.nixpkgs { system = "x86_64-linux"; }; in (f.lib.mkCodexPackage { inherit pkgs; codex = f.inputs.llm-agents.packages.x86_64-linux.codex; }).outPath'
```

After the lead's narrow-fix inspection, a fresh verification utility watcher
must rerun the following against the amended head:

```sh
nix develop --command env \
  LIVE_SWITCH_CODEX=/nix/store/idil0dg5623qarasafiqsjfc3s2bm2a9-codex-package-0.165.0/bin/codex \
  go -C portal test -mod=readonly -tags live_switch_integration \
  ./cmd/workspace-portal \
  -run '^TestNativeSessionCommunicationAuthorizationRoundTrip$' \
  -count=1 -timeout=180s -v
```

Each mode has a 75s internal context; the whole command has a 180s Go timeout.
Failure evidence reports the message ID and item roles/types for missing context,
or a bounded synthetic native log tail. Temp state belongs only to this test.

Also pending, as selected by lead:

```sh
nix build --no-link --print-build-logs .#checks.x86_64-linux.package
```

Independent review passed the original exact range; the lead accepted the
fixture-only delta under the narrow-fix rule. Passing native execution and
the full packaged result remain required before branch readiness. No integration or deployment is authorized.
No schema/migration, generated dependency stream or compatibility contract was
changed by B; no history consolidation is needed within B's one focused commit.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-29-cross-session-communication-authorization/


## Native startup diagnosis and folded repair

The original independent review remains unchanged in `review-report.md` and
covers `08f3dbb92bc8585929edee85a824d44dfb3b0846` through
`c43904a72d705562b79dcf9d59a29cf743bc9de7` (all lanes, no findings).
The fresh Luna/low watcher's original full-native attempt is preserved in
`verification/native.log` and `verification/native-result.md`: it failed in
10.1s overall, 1.581s reported test time. Both idle and steer failed on
`StartThreadWithSettings`: required team_reporting MCP handshake closed before
initialize. No inference request or authorization delivery had occurred.

Cause: the fixture-child guard and other five disposable fixture environment
variables were supplied only on the App Server process environment. Native MCP
children inherit a filtered environment and did not receive those markers.
`TestSessionCommunicationHostHelper` therefore skipped instead of serving MCP.
The direct real-command quick test supplies its own explicit environment and
could not expose this boundary. This is fixture setup, not model nondeterminism.

Repair is limited to
`portal/cmd/workspace-portal/session_communication_native_integration_test.go`:

- Explicitly populate `mcp_servers.team_reporting.env` from the existing six
  fixture marker variables, retaining all existing host adapter checks.
- Add `TestNativeSessionCommunicationMCPHandshake`, reusing the same startup
  setup with a 5s internal budget and stopping immediately after the first
  successful native thread creation. It performs no Responses turn.
- Include a bounded native log tail on thread-startup failure.

The startup-only native test reproduced the original failure before the env
fix (0.661s), then passed with the fix (0.680s):

```sh
nix develop --command env \
  LIVE_SWITCH_CODEX=/nix/store/idil0dg5623qarasafiqsjfc3s2bm2a9-codex-package-0.165.0/bin/codex \
  go -C portal test -mod=readonly -tags live_switch_integration \
  ./cmd/workspace-portal -run '^TestNativeSessionCommunicationMCPHandshake$' \
  -count=1 -timeout=15s -v
```

Known-short follow-up checks passed:

```sh
nix develop --command go -C portal test -mod=readonly \
  -tags live_switch_integration ./cmd/workspace-portal -run '^$' -timeout=45s
nix develop --command go -C portal test -mod=readonly \
  ./cmd/workspace-portal -run '^TestSessionCommunicationRealCommandRoundTrip$' \
  -count=1 -timeout=15s
```

Compilation: 0.051s, no tests. Real command round trip: 0.510s. Formatting and
`git diff --check` passed. No longer roundtrip was rerun by implementer1.

Lead directly inspected and accepted this exact +28/-2, one-test-file repair
under mandatory review's narrow-fix rule. No runtime, public API, trust boundary,
recovery semantics, schema, migration, dependency or design contract changed.
The initial review report was not modified. Full native acceptance remains
pending the fresh lead-owned watcher run against the amended commit.

History evidence after folding the unapplied fixture repair:

- Shared unchanged base: `08f3dbb92bc8585929edee85a824d44dfb3b0846`.
- Unchanged A/owning parent: `ed16c606b8b3a5ae1624e1f8dd5e7bcccf3cc387`.
- Old reviewed B/head: `c43904a72d705562b79dcf9d59a29cf743bc9de7`.
- New amended B/head: `124be7794936b84c4b26811c7deb74ff3843666b`.
- `git range-diff ed16c606..c43904a7 ed16c606..124be779` maps one B commit
  to one B commit and shows only the three fixture changes listed above.
- `git diff --stat c43904a7 124be779` is one file, 28 insertions/2 deletions;
  `git diff --check` for that delta passed. A remains the exact same parent.
- No superseded failed fixture commit is left in the final two-commit series.
  No migration or externally consumed/deployed lineage was rewritten.


## Native first-turn diagnosis and folded seed repair

The fresh watcher at intermediate B head
`124be7794936b84c4b26811c7deb74ff3843666b` passed the previous MCP boundary,
then failed both roundtrip modes while seeding their first materialization
message: `message was not sent: Codex RPC -32600: no rollout found for thread id`.
Original evidence is retained in `verification/native-fixed.log` and
`verification/native-fixed-result.md` (11s whole command, 1.383s package time).
No retry or process remained.

Cause: `StartThreadWithSettings` produces a fresh native thread without an
initial rollout. `SendWithOptions` first resumes the managed conversation,
which requires that rollout. Existing `team_reporting_native_integration_test.go`
materializes such threads by submitting their first actual `turn/start` before
managed sends. The final fixture now follows that existing native contract,
passing its retained model/effort explicitly and waiting for `RequireThreadIdle`.
All later communication sends still use the real Native/managed path.

The existing short handshake test was renamed
`TestNativeSessionCommunicationStartup` and extended through one seed and idle
check, keeping the same 5s internal budget and no communication exchange.
Before correcting the seed it reproduced the no-rollout failure in 0.691s.
An uncommitted attempt to reuse `EnsureInitialMessageWithOptions` correctly
refused the raw client's `source=vscode` as outside its managed application
freshness contract; that attempt was removed, without changing the client,
source or production refusal. The settled direct first-turn path passed the
startup+seed diagnostic in 1.036s:

```sh
nix develop --command env \
  LIVE_SWITCH_CODEX=/nix/store/idil0dg5623qarasafiqsjfc3s2bm2a9-codex-package-0.165.0/bin/codex \
  go -C portal test -mod=readonly -tags live_switch_integration \
  ./cmd/workspace-portal -run '^TestNativeSessionCommunicationStartup$' \
  -count=1 -timeout=15s -v
```

Follow-up tagged compile-only passed in 0.053s and the real command roundtrip
passed in 0.514s, using the same short commands listed in the prior repair.
Formatting and delta `git diff --check` passed. No full native roundtrip was
rerun by implementer1. The lead directly inspected and accepted the +11/-7
one-tagged-test-file delta under the narrow-fix rule; no new reviewer lane is
required. No runtime, API, design, trust, recovery or schema boundary changed;
no rollout, source identity or delivery success was fabricated.

Second folding evidence:

- Same whole-branch base: `08f3dbb92bc8585929edee85a824d44dfb3b0846`.
- Same exact A/parent: `ed16c606b8b3a5ae1624e1f8dd5e7bcccf3cc387`.
- Intermediate failed-seed B/head: `124be7794936b84c4b26811c7deb74ff3843666b`.
- New final B/head: `0bb745041fa508252e1c6d7f2bed26a31b7619fc`.
- `git range-diff ed16c606..124be779 ed16c606..0bb74504` maps one owning
  commit to one, with only the startup diagnostic/seed correction above.
- `git diff --stat 124be779 0bb74504` shows one file +11/-7. A remains the
  exact parent; the final series contains no obsolete fixture repair commit.
- The original `c43904a7` review report and both full-native failure records
  remain preserved. No migration/release/deployed lineage was rewritten.

Fresh watcher execution of the unchanged full-roundtrip command is pending
against `0bb745041fa508252e1c6d7f2bed26a31b7619fc`; startup success is not
whole-exchange acceptance. No push, rebase, integration, deployment or live
session mutation was performed.


## Active readiness diagnosis, fixture repair and remaining production boundary

The fresh watcher at `0bb745041fa508252e1c6d7f2bed26a31b7619fc` established
real idle end-to-end acceptance in 2.37s: separate application context reached
both leads, one grant remained, and the receiving lead immediately replied
through native MCP. That passed idle evidence is preserved in
`verification/native-seeded.log` and `verification/native-seeded-result.md`.
The same run's steer mode reached the 75s context limit while polling for a
reply (75.20s mode, 77.693s whole package). No idle rerun was performed during
this diagnosis.

Focused diagnosis showed a readiness hold, not a blocked native steer. The
raw native fixture client lacked an ActivityRecorder/subscription. The pinned
client deliberately reports an in-progress unobserved turn as `unclassified`;
`communication.Native.Ready` preserved its gate and returned `Recipient activity
is unavailable`. Dispatch therefore left the message `held`, Options=nil and
Receipt=nil, without attempting Native.Send. Thread/read and turns/list RPCs
completed in milliseconds. The old polling loop hid that result until expiry.

The final fixture configures the real `codex.NewActivityRecorder` in disposable
state and `client.Subscribe` for its native threads. It does not fake activity,
readiness or a send receipt. Its bounded `TestNativeSessionCommunicationStartup`
now creates/materializes both threads, opens a real held Responses turn,
asserts that actual activity events classify the exact held turn as `working`,
then requires the unchanged `Native.Ready` to admit it. It returns before
communication dispatch, so it is fixture-readiness evidence, not a passing
active message exchange.

Before recorder/subscription, the short real Ready probe failed with the
expected hold in 39.379562ms (1.890s package). After recorder/subscription it
passed in 1.908s. The settled stronger exact-active-turn/state plus Ready check
passed in 1.935s using:

```sh
nix develop --command env \
  LIVE_SWITCH_CODEX=/nix/store/idil0dg5623qarasafiqsjfc3s2bm2a9-codex-package-0.165.0/bin/codex \
  go -C portal test -mod=readonly -tags live_switch_integration \
  ./cmd/workspace-portal -run '^TestNativeSessionCommunicationStartup$' \
  -count=1 -timeout=15s -v
```

The same final tagged source also compiles as part of that executed short
check. Prior compile-only result on the repaired fixture was 0.058s; untagged
real-command regression passed in 0.509s. Formatting and delta diff checks pass.
The first actual communication dispatch is now capped at 5s and explicitly
reports a native send error, or held status/reason if Send was not reached.
The overall acceptance timeout was not raised. The fixture's original
context/source/receipt assertions remain intact.

### Diagnostic process reconciliation

Two early diagnostic outer caps (15s, then 20s) exposed a second fixture issue:
failure cleanup signaled and waited for native shutdown while its Responses
stream was still held. Both caps are failed diagnostics, not acceptance. Only
the following disposable owned groups were reconciled:

- PID/PGID `1274968`, exact native executable
  `/nix/store/idil0dg5623qarasafiqsjfc3s2bm2a9-codex-package-0.165.0/libexec/codex/bin/codex`,
  argv `app-server --listen unix:///tmp/nix-shell.Dq6tjQ/TestNativeSessionCommunicationAuthorizationRoundTripsteer1532845675/001/app.sock`.
  Verified PGID==PID, exact argv and fixture env
  `COMMUNICATION_FIXTURE_WORKSPACE` equal to that root plus
  `COMMUNICATION_FIXTURE_CHILD=1`; signaled that group with SIGTERM.
- PID/PGID `1285961`, same exact native executable and app-server argv bound to
  `/tmp/nix-shell.RO1sJ7/TestNativeSessionCommunicationAuthorizationRoundTripsteer1237856142/001/app.sock`.
  Verified the exact fixture environment, argv and PGID==PID before SIGKILL of
  that group after the graceful-stop dependency was identified.

Both exact PIDs were subsequently absent. A scoped /proc check of the exact
native executable plus `COMMUNICATION_FIXTURE_WORKSPACE` matching these
communication test names found no remaining fixture processes after the settled
short run. No incident, live workspace or session lifecycle process was touched.
Raw temporary evidence paths above are disposable, retained only as concise
recovery identity here. No real communication/session state was mutated.

Cleanup now releases the held Responses stream, cancels the owned native
context, signals its process group and waits, avoiding the previous dependency.
The settled short failure and success paths returned within their own budgets
without leaving fixture processes.

### Source composition boundary referred to the architect

Following the real recorder pattern exposed a separate production composition
question: `web/activity.go` owns a recorder on its separate activity observer,
while `web/communication.go` passes `s.config.Codex` into `Native`; the configured
normal client in `main.go`/`workspacecodex.NewWithOptions` did not appear to
receive that recorder or override `ReadActivity`. This source finding was
reported to lead, who assigned production diagnosis to the architect. B did not
change production composition or duplicate that investigation.

The manually recorded native fixture establishes that real observed active
state passes Native.Ready. It does NOT prove installed production wiring. Full
steer/native acceptance and readiness remain pending the architect's conclusion,
any required committed production fix/review, and a fresh watcher run. The old
idle pass remains valid for its exact source/state boundary.

### Third folded fixture amendment

Lead directly inspected the settled one-tagged-file +48/-7 correction and
accepted it under the narrow-fix rule; no fixture assertion or runtime contract
was weakened. History remains one A commit and one final B commit:

- Shared base `08f3dbb92bc8585929edee85a824d44dfb3b0846`.
- Exact unchanged A/parent `ed16c606b8b3a5ae1624e1f8dd5e7bcccf3cc387`.
- Prior B/head `0bb745041fa508252e1c6d7f2bed26a31b7619fc`.
- New B/head `ace1577a2d0bf50b4117d01e183d7f788267f5ec`.
- `git range-diff ed16c606..0bb74504 ed16c606..ace1577a` maps one owning
  commit to one, showing only the recorder/subscription, active readiness,
  dispatch failure diagnostics and cleanup correction.
- `git diff --stat 0bb74504 ace1577a` is one file +48/-7; delta
  `git diff --check` passes and worktree/index are clean.

Original independent review and every intermediate diagnostic head/result
remain preserved above and in their original reports. No production source,
schema, migration, dependency or deployed lineage changed in this amendment.
Git slot was released to the lead immediately after the amendment. No push,
rebase, integration, deployment or live session mutation was performed.


## Production constructor/worker acceptance authored and consolidated

Read the full accepted design addendum. C owns the small production adapter and
fresh gated activity read; B's follow-up edits only the existing tagged native
fixture. Its final implementation now uses the actual production composition:

- Bootstrap creates/materializes two real native histories with the existing
  fresh-thread first-turn contract. It has no recorder or subscription.
- Delivery uses `newCodexClientWithHistory` without an ActivityRecorder and the
  public `portalweb.NewContext` constructor with `ObserveActivity:true` and
  `RecoverSessions:true`. The actual portal activity monitor/observer establishes
  live coverage, and its actual generation-guarded communication worker delivers
  both the initial message and immediate reverse native MCP reply.
- No test-owned activity recorder/subscription, operational activity override,
  transport decorator, private worker access, production test hook, or direct
  `Service.Dispatch` remains in the tagged test.
- Before admitting the message in steer mode, a public portal activity GET
  verifies the actual monitor reports the real held native turn as working.
  The model backend checks separate developer context metadata against the
  grant recorded by A; no locally captured transport options supply authority.
- Ordinary stored message status and native receipt IDs prove both worker
  deliveries. The first stored receipt must agree with idle/start or active/
  steer mode. The backend's immediate reply remains gated on exact grant,
  endpoints, source approval, creation time, message and message-only scope in
  developer context separately from peer user text. One grant and saved roster
  settings are still required.

All constructor paths are isolated from the host. The provider catalog points
to an absent path below the disposable workspace; Codex home and workspace name
are explicit fixture values. Private state is a separate owned temporary root
outside that workspace, as required by the real upload/private-storage
contract. Host profile is an owned symlink to the fixture package directory;
no installed package/registration authorities are selected. Manifests specify
ordinary empty repository/artifact scope plus exact fixture thread/socket/client
version. Recovery records keep execution active but automatic restoration off,
so the constructor cannot attempt to restore the intentionally absent fixture
tmux runtime. Native/observer recovery gates still read the real active records.
The original strict host-selection adapter remains unchanged.

The first short construction attempt correctly rejected the old nested private
state (`upload storage must be an absolute private path outside the workspace`,
1.409s). Only fixture placement was corrected; no product contract changed.
The final `TestNativeSessionCommunicationStartup` now stops after actual native
bootstrap, production client/portal construction and public health verification.
It does not execute either worker acceptance exchange. It passed in 1.415s with
its existing 5s internal/15s command bounds, using the exact pinned native path
and command recorded above. No owned communication fixture processes remained.

Quick authoring evidence before consolidation:

```sh
nix develop --command go -C portal test -mod=readonly \
  -tags live_switch_integration ./cmd/workspace-portal -run '^$' -timeout=45s
nix develop --command env \
  LIVE_SWITCH_CODEX=/nix/store/idil0dg5623qarasafiqsjfc3s2bm2a9-codex-package-0.165.0/bin/codex \
  go -C portal test -mod=readonly -tags live_switch_integration \
  ./cmd/workspace-portal -run '^TestNativeSessionCommunicationStartup$' \
  -count=1 -timeout=15s -v
nix develop --command go -C portal test -mod=readonly ./cmd/workspace-portal \
  -run '^Test(SessionCommunicationRealCommandRoundTrip|CommunicationMCP.*)$' \
  -count=1 -timeout=15s
```

Compile-only passed 0.050s (no tests); final constructor/health passed 1.415s;
focused MCP/real command passed 0.500s. Final constructor execution also compiles
the entire tagged package after the state-placement correction. Formatting and
full branch/delta diff checks passed. C separately reported its focused service/
activity checks passed 2.133s and provider exact-reason follow-up passed 0.261s.
No long native exchange was run by B; all worker acceptance execution is pending
final affected review and a fresh verification utility watcher.

### Authorized unpublished history consolidation

After C released the Git slot, B committed only the tagged fixture follow-up as
`855eab51fcacf90f0e05c804c3e7d056d2ad7ec9`
(`fixup! communication: clarify bidirectional runtime authorization`). The
lead explicitly authorized autosquashing this own unpublished series only,
without fetching, rebasing onto upstream, changing other refs/worktrees or
rewriting any default branch. The exact operation was:

```sh
nix develop --command env GIT_SEQUENCE_EDITOR=true \
  git rebase -i --autosquash 08f3dbb92bc8585929edee85a824d44dfb3b0846
```

Pre-consolidation base/head:
`08f3dbb92bc8585929edee85a824d44dfb3b0846` /
`855eab51fcacf90f0e05c804c3e7d056d2ad7ec9`.
Its exact source tree was `7177a7a43218f4f91ad23d5be12430a1742a65d7`.
Final base/head:
`08f3dbb92bc8585929edee85a824d44dfb3b0846` /
`a6c0e10f4d0c828631a4bbf02da16fa3b6d556f5`.
The final tree is the identical `7177a7a43218f4f91ad23d5be12430a1742a65d7`;
`git diff --exit-code 855eab51 a6c0e10f` was empty/passed. Thus quick checks
retain their identical source inputs across consolidation.

Final exact series:

1. A `ed16c606b8b3a5ae1624e1f8dd5e7bcccf3cc387` — unchanged.
2. B `99da3951e621d0424f8c7ae74b30662501a1ddef` — final policy/docs and native
   production-worker fixture directly, without superseded fixture iterations.
3. C `a6c0e10f4d0c828631a4bbf02da16fa3b6d556f5` — production activity adapter,
   same patch as old C
   `2c8ec005d8717044ae79411e45a12046fd030edf`.

`git range-diff 08f3dbb9..855eab51 08f3dbb9..a6c0e10f` concluded:
A equal; B includes only the settled +112/-93 tagged fixture adaptation relative
to `ace1577a`; C equal patch; fixup absorbed. Source/index are clean. No obsolete
intermediate fixture/fixup commit remains in the final series; no migration,
state schema, dependency/pin stream or externally consumed/deployed lineage was
rewritten. Original review and every prior head/result stay preserved in their
original records and the evidence above. C is a substantive production addition
and requires the planned final affected independent review; old A/B review does
not cover it.

Git slot was released immediately after source/history verification, before
this evidence update. No fetch, push, upstream rebase, integration, deployment,
live-runtime or lifecycle action was performed.

After final affected review, a fresh watcher must run the full pinned-native
command above against final head `a6c0e10f4d0c828631a4bbf02da16fa3b6d556f5`.
Both modes now exercise the actual production worker, so the prior direct idle
pass is retained history, not acceptance of this changed composition. Packaged
verification remains separately required. No branch readiness is claimed.


## Final fixture prerequisite correction after production-native failure

Original affected review remains verbatim in `review-report-production.md` for
exact head `a6c0e10f4d0c828631a4bbf02da16fa3b6d556f5`. The fresh production-native
watcher then failed both modes: 75.20s idle and 75.21s steer, Go 150.534s/161s
command total. Original output is preserved in `verification/native-production.log`
and `verification/native-production-result.md`. No new production defect was
established by that run; its fixture prerequisites were incorrect.

Source-backed correction, accepted by architect and lead, is in
[design.md, fixture recovery note](design.md#fixture-correction-active-recovery-permission):

- `RecoveryStore.Set(..., automatic=false, activate=true)` explicitly clears
  `ActiveThreads` and `Continuation` after processing activate. The original
  fixture therefore had no active permission. Prior claims that this kept it
  active were incorrect. The final fixture uses normal `Set(..., true, true)`
  for its exact fixture root/current socket, immediately reloads automatic/root/
  socket/socket-epoch/Active identity, and fails before polling if any differ.
- The original public activity read used a display cache, including up to 30s
  cached idle state. Waiting for it to show working was an invalid admission
  oracle. C intentionally reads the actual observer freshly instead. The final
  test logs the public status/body once as diagnostic data, then relies on the
  actual worker's native accepted receipt for the exact message and held turn,
  with `Steered:true`. It adds no recorder or private dispatch call.
- Terminal `VerifyTmux` is not used by communication Native.Ready,
  monitor owns/recoveryHeld, or retained readiness. Short diagnostics proved
  the absent fixture terminal produces a passive read dependency error while
  still returning a valid idle activity body. No terminal subsystem or gate
  bypass was introduced for that unused requirement.

The first bounded prerequisite diagnostic failed in 1.669s and printed both
loaded records: automatic=false, active=false, ActiveThreads=[]; authority
loaded, terminal inspection exit1, and public activity200 with valid completed/
idle snapshots. Normal setter correction alone reloaded active exact roots and
passed the flag diagnostic in 1.663s. A subsequent short UI-working wait reached
its unchanged5s cap, exposing the display-cache proof error; that failed result
was not described as readiness. No full75s exchange was rerun during diagnosis.

### Exact first-worker green within the original short budget

Lead authorized the existing `TestNativeSessionCommunicationStartup` as the
bounded actual-worker prerequisite probe: hold a real native turn, let the real
portal worker make only the first communication delivery, require exact held
turn/message/native Steered receipt, then stop before the reverse exchange.
The internal budget remains5s; command budget remains15s. Final mode suppresses
only the synthetic backend's reverse tool call for this short probe; full idle/
steer modes retain the required immediate native MCP reply assertion.

```sh
nix develop --command env \
  LIVE_SWITCH_CODEX=/nix/store/idil0dg5623qarasafiqsjfc3s2bm2a9-codex-package-0.165.0/bin/codex \
  go -C portal test -mod=readonly -tags live_switch_integration \
  ./cmd/workspace-portal -run '^TestNativeSessionCommunicationStartup$' \
  -count=1 -timeout=15s -v
```

The final exact-turn and actual-helper-effect assertions passed in3.724s. The
actual held turn was `01a18a0e-9599-7993-9e47-0bec670037a0` for thread
`01a18a0e-929f-7021-8f70-5c50082d4c27`. The actual worker accepted message
`aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa` with that identical turn and `Steered:true`.
At the same time, public activity200 still named the old completed/idle turn
`01a18a0e-9316-7430-9bfd-f6cde0abd1a1`, demonstrating why cached display data
cannot be used as admission authority. Worker pending traffic was zero before
admission. The probe stopped before reverse exchange; it proves active readiness
and real submission, not the full context/reply exchange.

### Actual automatic helper effects and exact sidecar preservation

Correction to earlier evidence: `runDevSession` inherits the portal's parent
environment, whereas the marker had only been explicitly supplied to native/
MCP children. Without the marker, the old helper could `t.Skip` and exit0.
The earlier assertion that portal automatic resume was definitely refused was
not justified. Original reports remain intact; this paragraph supersedes that
fixture assumption.

The final existing local profile dispatcher now records argv and explicitly
rejects every unsupported command before entering the helper, with stderr
`fixture explicitly refuses unsupported host command` and exit64. It retains
the original strict communication path/environment/root checks. In the final
short run the actual trace was:

```text
communication allow session-a --as-is --request-stdin --json
resume session-b --as-is
exit=64 unsupported=resume session-b --as-is
resume session-a --as-is
exit=64 unsupported=resume session-a --as-is
communication send session-a --as-is --request-stdin --json
```

Both public recovery results were status200, state failed, with that exact
fixture-refusal error. The short test asserts the outcome when an actual resume
call is present and logs the actual trace, rather than assuming any call occurred.
The complete canonical JSON of each recovery sidecar is captured before portal
actor startup and compared exactly afterwards; both were unchanged, including
root/socket/socket epoch, automatic intent and active thread list. The failed
automatic calls changed only portal in-memory UI status. They did not clear
persisted active permission or execute any session lifecycle workflow. Exact
scoped process checks after completion found no remaining native communication
fixture process. No live or incident session was touched.

### Final source, quick checks and narrow-fix disposition

The final one-tagged-file repair is +88/-25 against the production-reviewed
head. It also caps each diagnostic/delivery polling stage at10s (never increases
the overall timeout), and prints latest registry status/detail/receipt presence,
public activity data and a bounded native/portal log tail before failure. It
avoids the former generic registry-read context error after75s. All current
runtime, policy, authority and message/context assertions are retained; no
production source or test hook changed.

Final quick checks:

- Tagged compile-only command recorded above: pass0.051s, no tests run.
- Exact-turn/sidecar/refusal startup probe: pass3.724s.
- Focused MCP/real-command command recorded above: pass0.457s.
- Formatting, full range and delta diff checks passed. Source/index are clean.

Lead directly inspected/accepted this narrow fixture correction after the
architect's source note and the actual first-worker proof. The final +5 lines
beyond its initial +83/-25 inspection assert actual unsupported-helper outcomes;
those assertions passed in the settled short probe. No further reviewer rerun
is required for this test-only correction. Both independent reports remain
verbatim. Full native exchange and packaged verification remain pending.

### Final authorized consolidation

Own fixture fixup: `8eeeb163baf71b51a811675eb719cca712358762`, after old reviewed
head `a6c0e10f4d0c828631a4bbf02da16fa3b6d556f5`. The lead authorized only the own
unpublished same-base autosquash; no upstream fetch/rebase or other refs/worktrees
were changed. Exact base remains `08f3dbb92bc8585929edee85a824d44dfb3b0846`.
Pre-consolidation head/tree:
`8eeeb163baf71b51a811675eb719cca712358762` /
`9b80c67e2f800c3354776404711c458b02c0881e`.
Post-consolidation head/tree:
`4155d0099d03028b43d5f08d225a88156cb4155a` /
`9b80c67e2f800c3354776404711c458b02c0881e`.
Tree equality and `git diff --exit-code 8eeeb163 4155d009` passed, preserving the
exact successful quick-check source inputs.

Final series:

1. A `ed16c606b8b3a5ae1624e1f8dd5e7bcccf3cc387` unchanged.
2. B `b0279514b60fc1c33678bae733df5840705c2e6c` final fixture directly.
3. C `4155d0099d03028b43d5f08d225a88156cb4155a` same production patch as
   `a6c0e10f4d0c828631a4bbf02da16fa3b6d556f5`.

`git range-diff 08f3dbb9..8eeeb163 08f3dbb9..4155d009` shows A equal, B only
the settled fixture repair, C equal patch, and the fixup absorbed. Production
comparison `git diff --quiet a6c0e10f 4155d009 -- portal/internal` passed. No
superseded fixture/fixup history, migration, schema, pin stream or deployed/
externally consumed lineage was retained or rewritten. Git slot was released
before updating these records. No production edit, push, upstream rebase,
integration, deployment, live/session lifecycle action or full exchange test
was performed by B in this continuation.

A fresh utility watcher may now run the existing full-native exchange command
against exact head `4155d0099d03028b43d5f08d225a88156cb4155a`, following the
lead's narrow-fix inspection. Whole-exchange readiness is still not claimed.

## Later lead acceptance checkpoint

Full actual portal-worker native idle/steer exchange PASSED on published final
4155d0099d03028b43d5f08d225a88156cb4155a (Go12.043s, wall17.9s). CI40975812804
completed successfully on the same head: packaged/focused, archive and creation
passed, host skipped. This closes the earlier pending native/full-suite items;
original commit/check history above remains evidence for its stated range.
See [final handoff](handoff.md), [native result](verification/native-final-result.md)
and [CI result](verification/ci-result.md). No integration/deployment performed.
