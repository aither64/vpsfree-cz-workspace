# Package C implementation evidence

Owner: implementer0. Brief: [design.md](design.md), production activity
composition addendum. Implementation and scoped quick checks are complete.
Affected final review, B's native constructor/observer/worker acceptance and
packaged checks remain separate lead-owned phases. No deployment or integration.

## Verified source and ownership

`dev-session current`, both environment values and the trusted thread binding
matched `2026-10-29-cross-session-communication-authorization` in
`/home/aither/workspace/ai/vpsfree.cz`. The retained member and exact native thread
row confirmed implementer0, `01a189c3-549d-7080-a702-dfcb7b53ac63`,
`codex-lb` / `gpt-6.1-sol` / `xhigh`, with saved `workspace_write` access and
full execution access. The complete design/addendum and applicable guidance were
read before implementation.

Worktree: `worktrees/2026-10-29-cross-session-communication-authorization/dev-workspace`.
Clean starting head: `ace1577a2d0bf50b4117d01e183d7f788267f5ec`.
Commit: `2c8ec005d8717044ae79411e45a12046fd030edf`,
`communication: use fresh observer activity for delivery admission`.

Exactly three paths were staged and committed:

- `portal/internal/web/activity.go`
- `portal/internal/web/communication.go`
- `portal/internal/web/communication_activity_test.go`

Diffstat: 350 additions and one deletion, including 313 focused test lines.
Production change: 37 additions and one deletion. The index and C paths were
clean after commit; B's in-progress native test remained unstaged. First Git
slot was released through `report_to_lead`. No branch, rebase or push operations.

## Behavior and documentation

A private adapter overrides only communication activity reads. When a monitor
exists, its fresh-read helper takes the existing per-thread and global gates
and reads the observer directly. It never uses display snapshots, display read
backoff or stale fallback. Stale and wrong-thread results are refused on both
observer and monitor-free direct paths. Incomplete historical timing alone adds
no new hold. Metadata, send and reconciliation remain delegated to the original
operational client. Existing provider/runtime/socket/recovery/metadata checks
and `Native.Ready` state/wait handling remain unchanged.

No exported API, registry, schema, dependency, recorder ownership, subscription
manager or operational client changes were needed. Nearby comments preserve the
cache/admission rationale. The owning feature guide already describes the same
delivery holds; no additional user-facing procedure was needed. The lead
inspected and accepted the production diff and private wording before commit.

## Failing before

With only the new test added to the clean starting source:

```sh
nix develop --command go -C portal test -mod=readonly -count=1 \
  -timeout=45s ./internal/web \
  -run '^TestCommunicationDispatchUsesFreshObserverAndOperationalDelivery$'
```

Failed in 0.099 seconds. The real `communicationService` constructed dispatch
read the deliberately rejecting recorder-free operational activity client.
Despite a fresh working observer, the queued message remained `held`, with
`Recipient status is unavailable`, instead of reaching `submitting`.

## Passing after

```sh
nix develop --command go -C portal test -mod=readonly -count=1 \
  -timeout=45s ./internal/web -run '^(TestCommunication|TestActivity)'
```

Passed in 2.133 seconds. This includes existing communication API/transcript
and activity observation/gate tests plus the new composition cases:

- Poisoned operational activity, warm idle display cache and fresh working
  observer; metadata, send and uncertain-send reconciliation use the operational
  client.
- Warm working display cache and active failure backoff cannot replace the
  fresh observer result. Working, idle, automatic wait and incomplete historical
  timing permit delivery. User-input/approval waits, unclassified activity,
  wrong thread, stale activity and read errors hold without native sends.
- Provider reservation, missing runtime authority, recovery hold, wrong socket
  and recipient metadata mismatch hold before activity is read.
- Existing per-thread/global gates cancel a queued delivery promptly, without
  observer reads or native sends. No duplicate general concurrency harness.
- Monitor-free composition retains direct reads with identity/stale guards.

The provider fixture was then strengthened to require a valid reservation and
assert its precise refusal reason. Its affected rerun passed in 0.261 seconds:

```sh
nix develop --command go -C portal test -mod=readonly -count=1 \
  -timeout=45s ./internal/web \
  -run '^TestCommunicationDispatchKeepsPreActivityHolds$'
```

Formatting and staged `git diff --cached --check` passed. The full staged diff
was inspected. The repository declares no hook framework and canonical hooks
contained no non-sample hooks. Commit used a message file in `nix develop`,
with no bypass. Nix printed a transient ignored evaluation-cache busy warning
during commit; the normal commit completed successfully without intervention.

Tests use disposable fixture workspaces and absent provider catalogs, except
the explicit disposable provider fixture. Short Unix sockets use temporary
`communication-activity-*` directories registered with test cleanup; listeners
are closed and directories removed. No live or incident session state was read.

## Remaining acceptance boundary

These quick tests exercise real service construction and dispatch with narrow
native/activity fakes. They do not establish native activity classification.
B owns the actual `NewContext(ObserveActivity: true)` constructor, recorder-free
operational client, observer and background worker proof in the tagged native
test. Run that and the required packaged checks only after affected final review,
under the lead's fresh utility watcher. No known C blockers or design deviations.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-29-cross-session-communication-authorization/)

## Later lead acceptance checkpoint

Full actual portal-worker native idle/steer exchange PASSED on published final
4155d0099d03028b43d5f08d225a88156cb4155a (Go12.043s, wall17.9s). CI40975812804
completed successfully on the same head: packaged/focused, archive and creation
passed, host skipped. This closes the earlier pending native/full-suite items;
original commit/check history above remains evidence for its stated range.
See [final handoff](handoff.md), [native result](verification/native-final-result.md)
and [CI result](verification/ci-result.md). No integration/deployment performed.
