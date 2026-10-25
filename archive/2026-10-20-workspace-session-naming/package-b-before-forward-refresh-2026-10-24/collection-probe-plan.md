# Disposable collector/admission probe

Status: prepared, **not executed**. Lead owns review clearance and assigns the
fresh verification watcher. This is verification planning, not independent
review. No application files, package definitions or live runtime are changed.
Only `bash -n run-collection-probe.sh` has passed; the Ruby/Go probe has not been
run or compiled. Passing shell syntax is not concurrency-coverage evidence.
Implementer1 statically checked all four artifacts against frozen B and found no
blocking safety or fixture issue. This consultation is not independent final
review or execution proof. Admission failures include up to 4 KiB of response
body for diagnosis.

The component inventory in [package-b-coverage-inventory.md](package-b-coverage-inventory.md)
does not prove that a real collector and portal admission work concurrently.
The session-only artifacts `collection_probe.rb`, `collection_probe_test.go`
and `run-collection-probe.sh` compose those existing seams. Implementer1
confirmed the source paths and fixture boundaries at B
`ae0399b31746bc14ea2fcbe3185f36d8e4b04885`.
The invocation is now bound to final B
`4c6b9f177d5b205b21b45880c6ac1bc3c403eef6`. Read-only comparison confirms the
collector, host guards, support fixtures and entire portal web package are
unchanged from the earlier inspected head. The five changed paths are dependency
metadata (`flake.lock`, `flake.nix`, `nix/workspace-portal.nix`, `portal/go.mod`,
`portal/go.sum`). This compatibility check supplies no execution evidence.

## Exact command after review

Run once through the lead-assigned watcher, retaining stdout/stderr and exit
status as a session artifact. Do not run this during final review or silently
update the expected head. A changed source head requires confirming this
fixture still matches the reviewed source.

```sh
bash /home/aither/workspace/ai/vpsfree.cz/work/2026-10-20-workspace-session-naming/run-collection-probe.sh \
  /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-20-workspace-session-naming/dev-workspace \
  4c6b9f177d5b205b21b45880c6ac1bc3c403eef6
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
- Switch ordering and generation lock: `libexec/workspace-host:616`, `:3086`,
  `:3096`. Preparation is before exclusive admission; effect sentinels are after.
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
