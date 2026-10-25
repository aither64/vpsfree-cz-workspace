# Disposable collector/admission probe

Status: prepared for refreshed, clean, published B
`529e075ad07e2d967a8af4902584e37527115454`, tree
`c9c3286858934ba63ff11c9e37879e7803a8351f`, with A
`801099102ef9af4a82c1f3853c53d6b442ecd4dc`.
**Execution on this pair is pending final review and the lead's watcher release.**
The Oct 25 update is static planning, not independent review or execution.
No application files, executable prototype files, package definitions or live
runtime are changed. The user's deployment hold remains in force; C113d/7510
stay frozen, with no claim, copy, activation, merge or lifecycle authority.

The exact `37a87a8a..529e075a` delta changes 16 files: preserved upstream
message-delivery browser behavior/tests/docs, exact A dependency metadata and
the separately reviewed creation-refusal diagnostics in the VM/browser fixture.
Byte comparisons prove the probe's host/collector/preparation/switch files,
coordination fixture, portal server/creation/preparation/authority and retry-worker
files unchanged. Naming helper/launcher files also remain identical. In
particular, `libexec/workspace-host`, `workspace-coordination-host.rb`,
`workspace-coordination-execution.rb`, `test/support/coordination_fixture.rb`,
`test/workspace_coordination_test.rb`, and Go `server.go`, `creation.go`,
`preparation.go`, `preparation_test.go`, `turn_retry.go` and
`session/authority.go` have identical B37/final529 blobs. The probe uses custom
naming, nil Codex and `RecoverSessions=false`; upstream A changes do not introduce
a native call into that path. Changed browser assets are not exercised by this
HTTP-only probe, and the new refusal observer belongs only to the separate
creation VM. No probe seam change is required. All three executable prototype
hashes below still match their original saved copies.

Historical B37/A6e469 collection execution **passed in 23.396 seconds**, as
recorded in `verification-packages-37a87a8a-result.json` and its original preserved
copy under `package-b-creation-37a87a8a-original/`. The same batch's creation VM
failed; that result remains preserved and is not changed by collection success.
All earlier logs/results remain historical, not final529 evidence. The new
[verification brief](verification-preparation-529e075a.md) supplies the separate
two-engine upstream message-delivery browser recipe and its non-skip criterion.

Historical execution passed on B `e515437822e6a2ee7e61be7b613d1e058dad56d7`
in 10.481 seconds; see `verification-packages-e5154378-result.json`. That receipt
does not establish refreshed-head execution. On 2026-10-24, exact-head/clean-tree
checks before and after the syntax/compile-only command passed at `556a6e51`:
`bash -n`, `ruby -c` and `go -C portal test -mod=readonly -overlay OVERLAY -c`
all passed in a combined 19.669 seconds. The test binary was never executed;
the overlay and binary lived only in an owned temporary directory. These checks
establish syntax/type compatibility, not concurrency behavior. The first shell
recipe was rejected before execution for its cleanup syntax; the successful
recipe used an owner-scoped Python `TemporaryDirectory` context instead.
Admission failures retain up to 4 KiB of response body for diagnosis.

The historical `556a6e51..37a87a8a` diff contains only three files:
`portal/internal/workspacecodex/client.go`, `client_test.go` and
`loaded_retirement_test.go` in the same directory. The production change extracts
the loaded-retirement observation reader and joins caller cancellation with
failed list/metadata observations (`client.go:799–829`); successful observations
and mutation receipts remain unchanged. The other two files test that boundary.
No collector, host lock, portal admission/handoff, naming, fixture configuration
or prototype file changes appear in this delta. The probe still supplies nil
Codex and `RecoverSessions=false`, so it cannot enter native loaded-retirement
discovery. This supports rebinding the unchanged prototype, not execution proof.
No syntax, compilation, test, live or CI command was run for either artifact-only rebind; the
compile-only receipt above remains specific to `556a6e51`.

The component inventory in [package-b-coverage-inventory.md](package-b-coverage-inventory.md)
does not prove that a real collector and portal admission work concurrently.
The session-only artifacts `collection_probe.rb`, `collection_probe_test.go`
and `run-collection-probe.sh` compose those existing seams. Implementer1
confirmed the original source paths and fixture boundaries at B
`ae0399b31746bc14ea2fcbe3185f36d8e4b04885`. The Oct 24 inspection was coordinated
with implementer1 while its behavior files were stable, then bound to published
`556a6e51`; the three-file comparison above established the B37 rebind, followed
by the final529 comparison recorded at the top of this plan.
The actual collector, coordination-host, fixture setup,
preparation/handoff, creation command and naming helper/launcher paths remain
unchanged from the previously tested `e5154378` source. Host additions preserve
the existing switch/lock methods. The new portal retry worker is gated off by
the probe's nil Codex client and `RecoverSessions=false`
(`portal/internal/web/turn_retry.go:113–117`). New retained-session admission and
retry behavior therefore requires no probe seam change.

All three executable prototype files are unchanged, including their runtime
bounds and refusal checks. Originals of all four artifacts are preserved in
`package-b-before-forward-refresh-2026-10-24/`; byte equality was verified before
this plan-only update. Their SHA-256 values are:

- `run-collection-probe.sh`: `d7f50481fae8e6ce9e33a23dd8fef87ee097b9f481180503d850ab3e9a7bf113`
- `collection_probe.rb`: `70fe161d5ca635f87a186bf6b43152285ff7ab620dff0979178fd966c52ce28a`
- `collection_probe_test.go`: `778c94b7bef0de7da10dd1e6dc5766e431ffd1c2e3aab4453a3bb21c854d2d1a`

This static comparison and compile check supply no refreshed execution evidence.

## Exact command after review

Run once through the lead-assigned watcher, retaining stdout/stderr and exit
status as a session artifact. Do not run this during final review or silently
update the expected head. A changed source head requires confirming this
fixture still matches the reviewed source.

```sh
bash /home/aither/workspace/ai/vpsfree.cz/work/2026-10-20-workspace-session-naming/run-collection-probe.sh \
  /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-20-workspace-session-naming/dev-workspace \
  529e075ad07e2d967a8af4902584e37527115454
```

The runner requires a clean exact checkout, creates a temporary Go overlay,
enters the repository Nix development shell and selects only
`TestSessionOnlyRealCollectionAdmission`. The overlay adds a test virtually;
it writes nothing into the checkout. Ruby orchestration has a 25-second bound,
its Go subprocess context 35 seconds, and the selected Go check 60 seconds.
Nix environment realization/Go compilation occurs outside those runtime bounds;
the watcher retains its usual ownership and escalation rules. No VM, systemd
unit, Nix package build or profile switch is part of this command.

## Composition and assertions

1. Reuse `test/support/coordination_fixture.rb` to create a private temporary
   workspace, state, package/profile symlink and local Git repositories. Prepare
   and cancel one disposable merge job, making its payload eligible for real
   collection. Create a separate valid owner/feature for the preparation waiter.
   The fixture catalog keeps `profileMachine=nil` so switch cannot route to a
   real coordinated deployment. HOME, TMPDIR and global Git configuration are
   isolated; local Git pushes target only the fixture filesystem remote.
2. Invoke production `Host#run('workspace-host', ['coordination', 'gc', '--apply',
   '--json'])`. Its real shared generation lock and exclusive preparation guard
   wrap the actual `WorkspaceCoordination::Collector`. Wrap only the engine's
   `capture` immediately before its first Git `worktree remove`, as the existing
   test does; signal the exact arguments and pause. Resume by calling the
   original capture, so collection/removal itself is not stubbed.
3. Start a real `coordination_prepare` call for the separate disposable owner.
   Observe entry into its actual shared preparation guard. Its inner
   `coordination_prepare_owned` is a sentinel so no new payload is built.
   Also dispatch the ordinary `Host#run('workspace-host', ['switch', '--source',
   fixture_package])`. `prepare_profile` is an inert prepared-result stub;
   the real switch, saved profile-token check and exclusive generation guard
   remain. Both activation effect boundaries are inert sentinels.
4. After both waiters have reached their guards, assert neither preparation nor
   activation effect sentinel is entered. The package's preparation stub is
   allowed before the exclusive lock, matching production ordering. Observe
   the collector still paused before removal.
5. Construct production portal `New(Config)` against that exact workspace,
   state, profile and `state/transition.lock`. Use the production HTTP handler
   over a private `httptest` TLS listener, not a mocked response. POST `/sessions`
   with a custom name and exact origin; require HTTP 202 and persisted
   preparation state `handed_off`, exact slug and nonnil handoff while collection
   is paused. The test intentionally supplies `probe-model` with no Codex client,
   stopping subsequent initialization at model-catalog validation. The absolute
   dummy session command records and fails any unexpected invocation, which
   fails the probe. No real session helper, native model or socket is reachable.
6. Recheck both exclusion sentinels after the HTTP handoff, then release Git
   removal. Require actual collector success with at least one removed worktree;
   preparation and activation sentinels must each resume afterward. Assert the
   fixture profile symlink and generation token did not change. Emit compact
   JSON evidence for pause/removal and successful resumption. Close only this
   test's server, threads and subprocess; remove only its freshly created
   temporary directories. Any failure exits nonzero for owner diagnosis.

The lock routines are not replaced with synthetic flock assertions. Fixture
registry/package/engine selection is the same injection used by existing host
tests. No live registered workspace is passed to any runtime command, and no
private activation or lifecycle helper is invoked.

## Source anchors and evidence limits

- Real collector command and both guards:
  `libexec/workspace-coordination-host.rb:285`.
- Real preparation admission path: same file `:217`; the preparation CLI's
  retained-operation compatibility checks are outside this test's scope.
- Switch ordering and generation lock: `libexec/workspace-host:618`, `:3259`,
  `:3269`. Preparation is before exclusive admission; effect sentinels are after.
- Existing safe removal gate: `test/workspace_coordination_test.rb:62`.
- Real portal admission baseline: `portal/internal/web/creation_test.go:29`;
  production reservation/handoff: `portal/internal/web/preparation.go:598`.

Passing proves simultaneous real collector removal admission, real portal
creation acceptance/reservation/handoff, and the ordinary preparation/package
exclusion paths. It **does not** prove completed native-backed session creation
or browser usability during collection. It does not exercise real activation,
package building, machine claims, or native naming during the sweep. Those
remain separate final package/VM and deployed checks. Existing generation-change
and missing-lock component cases remain required; this probe replaces none.

If acceptance specifically requires a usable native conversation during the
same sweep, report this limit rather than treating this probe as that proof.
The smallest necessary follow-up is one scenario in the existing
`nix/tests/session-creation.nix` VM: its installed portal/native/browser request
while a disposable fixture collector is gated at Git removal. That is a test
source change for implementer1 and lead/reviewer approval, not an authorized
expansion of this artifact. If the session-only probe fails to compose on the
exact reviewed head, stop and return its logs; the watcher must not edit it or
weaken assertions to make it pass.

## Historical separate live naming smoke compatibility

Read-only inspection of `package-b-live-naming-smoke_test.go`, its overlay map,
`package-b-discover-live-naming.py` and the refreshed production source found no
required seam change. `session_name.go:83` still owns the total naming budget;
`session_namer.go:34–56` still resolves the provider and calls the same
`modelSessionNameWithRetry`/`modelSessionName` with the production client accessor.
The overlay intentionally calls those production helpers with the independently
discovered selected provider. It does not exercise portal HTTP admission or the
`normalSessionName` provider-resolution wrapper itself.

`portal/cmd/workspace-portal/naming_runtime.go:50–96` still owns the private
`naming-*/app.sock`, cwd, eager asynchronous native startup and startup catalog.
The discovery script's all-OS-thread child traversal, exact executable/profile
checks and local-only marker remain appropriate. Production launch/environment
and naming-helper files are unchanged from `e5154378`; the refreshed A dependency
preserves the same public accessor. Implementer1 owns these smoke artifacts and
reported their cheap overlay compile passed on B556; this consultation did
not modify or execute them. Final source/evidence prose remains that owner's work.

Live discovery, inference, empty-loaded-thread precondition and post-call cleanup
remain authorized post-deployment checks owned by the lead. Static compatibility
does not prove current provider availability, selected runtime health or the
absence of concurrent naming work. The disposable collection probe does not
validate retained retry-policy package capability gates because its preparation
and activation effect boundaries are intentionally inert; the packaged tests
and ordinary deployment guards retain that separate responsibility.
