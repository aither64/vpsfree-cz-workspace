# Final review: cold observers and session progress controls

Reviewed all four lanes directly, with no nested agents, source edits, long
checks, deployment or integration. Exact committed ranges:

- Runtime `9baeea528f2e270332afa13786ec85a49a68e4c3..5fea2be1cba9d1574c178951170cb68b639d58f1`: `54e968ae` cold scheduling; `5fea2be1` Settings/interval/Check now.
- Workspace `dacd3d7afb20f42c6f7bf95b767fb73fbbd61ea4..a878419176920e5521743fbbd633a8b293032c77`: `e3aff9c9d` site docs; `a87841917` runtime pin.
- Configuration `7eaaafd718809e16867c9b4614f9b2e2d54fa62a..7dd40ff46d78a475d9730888771d20122d51c919`: `7dd40ff4` generated channel pin.

## Findings

1. **Important: a refused Check now can leave progress permanently pending.**
   Commit `5fea2be1`, `portal/internal/web/progress_observer.go:385` saves a new
   pending check before `sendProgressCheck` calls the dispatch boundary at
   `:479`. If the observer is idle natively but its manually assigned task has
   a pending capacity retry, `workspacecodex.SendProgressCheck` correctly
   refuses before sending anything (`portal/internal/workspacecodex/progress.go:25`).
   The API returns 409, but the failure path retains the pending progress record.
   Reproduction: pause automatic checks, let a manual observer task enter retry
   backoff, then click Check now. Once the original three-minute deadline passes,
   settlement repeatedly reports an unknown submission outcome (`progress_observer.go:459`)
   even though this request was definitively never sent. Further Check now
   requests always refuse at `:269`; pause/resume cannot recover it. This also
   affects automatic checks deferred beyond their deadline.

   Distinguish a definite pre-dispatch refusal from an uncertain submitted
   outcome. Defer before reserving progress ownership, or clear only an exactly
   proven unsent reservation while retaining uncertain-send IDs. Preserve the
   manual retry's original identity/deadline. Add one API/scheduler regression
   for paused Check now while a manual retry owns the idle observer, then advance
   past the deadline and prove a later valid explicit check remains possible.
   The existing native-wire test protects the manual retry itself but does not
   inspect the scheduler's progress record. Lanes: general, risk/compatibility,
   architecture.

2. **Advisory: site documentation still states a fixed cadence and omits the
   explicit idle exception.** Commit `e3aff9c9d`, `docs/agent-teams.md:144` says
   the runtime checks every 15 minutes and fully idle sessions do not start
   checks, immediately after introducing configurable intervals and Check now.
   Say that automatic checks default to 15 minutes and exclude idle sessions;
   explicit Check now is the documented exception. Runtime guides already
   describe this correctly. Lane: general/documentation.

## History, ownership and compatibility

The complete new series is focused and matches the requested split. The cold
observer fix is independently reviewable from Settings/interval/manual behavior;
tests and documentation accompany their owners. Workspace prose and generated
pins are separated. **No obsolete unmerged approaches or fixup history remain.**
Each consumer has one final runtime-pin update; **no repeated update streams
require consolidation**. Earlier observer pins are merged master history and
must remain unchanged.

Independently compared parsed locks: only workspace `dev-workspace` and
configuration `devWorkspace` nodes change. Both select `5fea2be1` with identical
content hash `sha256-ubGeIOAy64reS6R/3NOSFrZ2MQjEfZlVZBWftEBa0QM=`; input
edges, extension and sibling nodes are preserved. Runtime owns state, scheduler,
API, browser and dispatch; existing consumer composition remains appropriate.
The changes add no unrelated framework, approval gate or host behavior.

**No migrations.** Optional `intervalMinutes` remains in schema-1 private state;
missing/zero state uses 15 minutes. Older schedulers ignore it and may discard it
on rewrite, restoring their prior cadence. No lifecycle, roster, native protocol,
Codex version or irreversible state transition changes. Existing generation,
provider, lifecycle and exact dispatch ownership remain applicable. Activation
must use the matched composed package; no new feature integration is authorized.

## Evidence and remaining verification

Inspected complete histories/diffs, repository guidance, appended design,
state, progress/retry/recovery dispatch boundaries, API/browser tests and updated
guides. All feature trees are clean; runtime `git diff --check` passes. Supplied
focused Go, real-wire cold receipts, Node and workspace instruction tests pass;
the consumer-pin checker passes. These are proportionate checks, but do not
cover the pending reservation left by a definitive manual-retry refusal.
After resolving/deciding the Important finding, one composed package validation
and ordinary live post-deployment acceptance remain. No extra model pilot or
unchanged host VM suite is required by this review.
