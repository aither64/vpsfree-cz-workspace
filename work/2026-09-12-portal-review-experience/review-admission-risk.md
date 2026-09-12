Review result: **0 Blocking, 1 Important, 0 Advisory.**

## Findings

### Important — A backward wall-clock adjustment can let a stale creation recreate a deleted session

Commit `2d589990` introduces completed-deletion ordering based solely on timestamps from two independent wall-clock reads:

- Creation acceptance records `time.Now()` in [creation.go:131](</home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/dev-workspace/portal/internal/web/creation.go:131>).
- Deletion completion records Ruby `Time.now` in [dev-session:4828](</home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/dev-workspace/libexec/dev-session:4828>).
- Portal retirement accepts the tombstone only when `removed_at >= startedAt` in [removal.go:162](</home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/dev-workspace/portal/internal/session/removal.go:162>) and [creation_store.go:202](</home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/dev-workspace/portal/internal/web/creation_store.go:202>).
- The CLI repeats the same comparison in [dev-session:2875](</home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/dev-workspace/libexec/dev-session:2875>) and [dev-session:2905](</home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/dev-workspace/libexec/dev-session:2905>).

If the host clock moves backward after a request is accepted but before a causally later deletion completes, the deletion receives an earlier timestamp. Portal consequently preserves the stale receipt, and the CLI does not reject it. A queued worker can then reach the now-empty destination and recreate the session, undoing the explicit deletion. Running receipts are deliberately excluded from portal retirement at [creation_store.go:170](</home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/dev-workspace/portal/internal/web/creation_store.go:170>), so the exact-ID files copied during terminal receipt retirement do not protect that path.

The inverse also occurs: a future-skewed deletion timestamp followed by clock correction can reject genuinely fresh requests until wall time catches up, contradicting the documented name-reuse behavior.

This does not require a hostile local operator; ordinary RTC/NTP correction, reboot-time adjustment, or VM snapshot restoration is sufficient. Existing tests cover equality and a one-nanosecond increase at [dev_session_test.rb:3190](</home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/dev-workspace/test/dev_session_test.rb:3190>), but not clock regression.

Use a persisted causal token tied to the slug incarnation or deletion operation as the authority, with wall-clock timestamps retained only for presentation. Exercise backward and forward clock corrections, queued workers, fresh reuse, and mixed package generations.

## Reviewed scope

I inspected the complete committed ranges recorded in the packet:

- `codex-web`: `bdd79be2..83770217`
- `dev-workspace`: `87606197..c3502742`
- `vpsfree-dev-workspace`: `db25c77e..a0d7fdca`
- `workspace`: `584ea0f6..ef75f045`

Apart from the finding above, the admission implementation is coherent: observer-only RPC admission is generation-bound, disconnect and close cancel queued work, stale workers cannot publish into later generations, and portal per-thread serialization precedes the global four-slot gate. Interactive clients remain outside the observer admission path.

The deletion path otherwise checks the destination, runtime authority and journals under the appropriate locks; fork repeats the deletion check after reacquiring its destination lock; partial receipt retirement remains retryable; recovery additions are private and additive; and all three consumer pin layers select the reviewed provider/runtime revisions.

## Residual validation gaps

No tests were run, as requested. The packet’s longer package, VM, live-browser, live-creation, profile-upgrade, and rollback exercises remain pending. The Important finding should be fixed or explicitly accepted before integration testing proceeds.