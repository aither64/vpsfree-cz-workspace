# Architecture review

No Blocking findings. I found four Important findings that require remediation or an explicit recorded decision before long integration testing.

## Important: history caches are not retired after read-only activity requests

Commit `4dde3c6a` introduces a per-thread cache in `codex-web/codex/turn_history.go:35-46`. `readAllTurns` obtains that cache and may retain metadata for as many as 100,000 turns (`turn_history.go:91-126`). However, the read lifetime established by `ReadActivity` at `codex/activity.go:139-143` applies only to `ActivityRecorder`; it does not retain or release the separate `Client.turnHistory` cache.

The only production removal I found is when the last subscription is removed at `codex/client.go:963-987`. A thread that is read without being watched therefore leaves its history cache in the long-lived client indefinitely. This is a normal portal path: the monitor excludes archived sessions at `dev-workspace/portal/internal/web/activity.go:116-130`, while the conversation resolver still supplies the activity provider to every read-authorized session at `portal/internal/web/server.go:2298-2314`. Archived session pages also continue polling activity every five seconds at `portal/internal/web/static/app.js:1637-1653`. Visiting distinct archived sessions can consequently accumulate large history caches for the lifetime of the portal process, contrary to the packet and `codex-web/README.md:97-98`, which state that caches are released after the last watch or read.

There is also an overlap defect: `removeWatch` can delete the map entry while an unrelated browser `ReadActivity` still holds the cache pointer and its gate. A subsequent read creates a second cache for the same thread, bypassing the intended per-thread serialization and discarding the first read’s reusable pagination progress.

The history cache needs a unified watch/read lifetime, such as reference-counted acquisition and release that cannot remove the map entry while a reader holds it. Add coverage for repeated no-watch reads and for last-unsubscribe overlapping an active read.

## Important: the monitor replaces global serialization with unbounded authority-wide fan-out

Commit `40837d24` launches one goroutine for every eligible active session without a concurrency limit (`portal/internal/web/activity.go:87-113`). Every new worker immediately performs `VerifyThread`, `Subscribe`, and `ReadActivity`, then repeats reads on five- or thirty-second intervals (`activity.go:132-188`).

A cold `ReadActivity` can issue thousands of paginated requests before reaching the 100,000-turn limit (`codex-web/codex/turn_history.go:91-145`). On portal restart, observer reconnect, or discovery of many sessions, all workers can backfill concurrently against the same App Server authority. The four-second per-worker timeout bounds individual duration but not the number of concurrent RPCs, goroutines, caches, or writers. Each subscription also adds an entry to a client-wide subscriber map, which every broadcast scans (`codex-web/codex/client.go:928-960,1118-1129`).

The per-thread provider locks correctly remove the previous head-of-line lock, but they turn the same workload into unconstrained concurrency. With hundreds of retained active sessions, restart or reconnect can produce a large RPC and filesystem burst, cause repeated timeouts, and contend with interactive App Server work. The reported stress checks cover writer isolation and limited thread combinations; the portal activity test covers one worker rather than authority-scale restart or reconnect behavior.

Use a bounded, fair scheduler for expensive reads and initial subscription work, with coalescing or staggering so old histories cannot monopolize the available slots. Preserve independent event observation, but explicitly bound backfill concurrency and test many-session startup/reconnect alongside interactive responsiveness.

## Important: per-turn files still have no deletion or retention ownership

The replacement recorder writes one immutable file for every finalized observed turn at `codex-web/codex/activity_store.go:275-310`. Retirement at `activity_store.go:424-447` unloads memory and stops the writer, but it deliberately leaves all files. There is no provider operation to delete or compact a thread’s durable history.

The portal stores these directories below its persistent lifecycle-operation state root (`dev-workspace/portal/internal/web/activity.go:38-45` and `portal/internal/web/operation_store.go:35-65`). When a session is archived, monitoring stops but the files remain for historical display; when a session is fully deleted, monitoring likewise only cancels the worker at `activity.go:99-103`. The provider cannot distinguish those lifecycle outcomes and the application never removes the deleted thread’s directory. `codex-web/README.md:100-105` explicitly confirms that historical summaries have no authority-wide size limit.

This avoids rewriting a single ever-growing ledger, but does not establish an authority-wide retention contract. Long-lived or later-deleted sessions permanently consume one inode and filesystem allocation per turn. Exhausting the shared user-state filesystem can then affect creation receipts and lifecycle-operation persistence, not merely optional timing.

Define application-owned retention for definitively deleted threads and a bounded representation or quota strategy for retained histories. Any cleanup must respect pending lifecycle recovery and rollback, but cancellation alone is insufficient. Exercise deletion, restart, quota/inode pressure, and preservation of archived timing.

## Important: fork recovery duplicates the Ruby journal contract in the portal

Commit `1de0a78d` makes the Go portal parse and validate the Ruby CLI’s complete fork-journal schema in `portal/internal/web/creation.go:686-732`. `readCreationJSON` rejects every unknown field (`portal/internal/web/creation_store.go:221-242`). The Ruby owner independently declares the exact field set and validations at `libexec/dev-session:2947-2975`, and is already the locked recovery authority: it skips live source validation when the destination journal exists and then validates that journal during retry (`libexec/dev-session:991-1015`).

This creates two strict declarations of persistent recovery state that must evolve together. A future additive journal field, schema version, state transition, or settings representation could remain valid and recoverable to the CLI while being rejected by the portal before the CLI is invoked. That is especially relevant because interrupted journals survive package upgrades and rollback. The current Go tests construct their own journal documents; they do not make one implementation consume fixtures produced by the other.

Prefer asking the CLI for a validated recovery decision or invoking it as the sole authority with the receipt-bound arguments. If the portal must parse the journal, establish an explicitly versioned shared contract with bidirectional Go/Ruby fixtures and mixed-generation behavior.

## Cross-project assessment

The remaining ownership and pin structure is coherent:

- `codex-web` owns Codex protocol normalization, activity persistence, and the shared typed renderer.
- The browser whitelist and capability probe were removed without introducing another event registry.
- Complete Git rename detection remains bounded by the existing process deadline.
- The final Go module, Nix source, and shared browser assets select `codex-web` `4dde3c6a`.
- The pin-only heads `vpsfree-dev-workspace` `4e03a3f0` and `workspace` `ea6cc34a` select the reviewed runtime chain.

The creation receipt retirement and canonical-conflict changes otherwise preserve the CLI journal as the operational authority and address the previous lifetime-wide completed-receipt exhaustion.

## Residual verification gaps

Per instruction, I did not run tests. The packet reports focused and CI verification, while packaged VM, live App Server/browser creation, profile upgrade, and rollback tests remain pending. Those tests should not begin until the Important findings above are fixed or explicitly accepted.