# Architecture and repetition review

Review result: **0 Blocking, 1 Important, 1 Advisory finding.** The existing durable-retention decision is supported by the code; its per-turn storage growth remains an Advisory operational limitation, not an additional lifecycle defect.

Reviewed final heads:

- `codex-web` `bdd79be2`
- `dev-workspace` `87606197`
- `vpsfree-dev-workspace` `db25c77e`
- `workspace` `584ea0f6`

## Findings

### Important — The four-slot scheduler is bypassed during reconnect and can spend all slots waiting on one thread

Commit `87606197` limits portal worker and browser activity calls through four monitor-local slots at [activity.go](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/dev-workspace/portal/internal/web/activity.go:63) and [activity.go](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/dev-workspace/portal/internal/web/activity.go:177). This bounds initial verification, subscription, and history reads, but it does not bound all subscription work performed by the observer client:

- After a WebSocket connection is re-established, `Client.Ensure` calls `restoreWatched` directly at [client.go](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/codex-web/codex/client.go:554).
- `restoreWatched` starts one goroutine for every watched thread at [client.go](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/codex-web/codex/client.go:1001).
- Every goroutine sends its own `thread/resume` through `requestConnected` at [client.go](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/codex-web/codex/client.go:1019), below and therefore outside the portal scheduler.

With hundreds of observed sessions, the first bounded worker that reconnects the client consequently launches hundreds of pending resume RPCs at once. Those requests compete with the four scheduled reads and can make verification fail, after which the monitor removes subscriptions and begins subscribing again at [activity.go](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/dev-workspace/portal/internal/web/activity.go:182). This recreates the reconnect burst the authority scheduler was intended to prevent.

There is a second admission-boundary problem: the portal takes an authority slot before `codex-web` reaches its per-thread history gate at [turn_history.go](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/codex-web/codex/turn_history.go:131). Four concurrent browser reads for one old thread can therefore occupy all four authority slots while three wait behind the same per-thread reader, excluding unrelated session workers.

The current 40-worker regression uses distinct threads and covers only initial startup, cancellation, and peak `ReadActivity` concurrency at [activity_test.go](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/dev-workspace/portal/internal/web/activity_test.go:207). It does not exercise observer reconnection or duplicate same-thread admission.

Reconnect restoration should use the same bounded authority executor, or an equivalently bounded provider queue included in that authority budget. Per-thread coalescing should occur before consuming a global slot. Add a many-watch reconnect case and a duplicate-thread browser case that proves an unrelated worker can still progress.

### Advisory — A persisted archived-receipt notice becomes inaccurate after revival

When an archived canonical destination lacks exact completion evidence, `canonicalCreationConflict` returns `creationArchivedMessage` at [creation.go](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/dev-workspace/portal/internal/web/creation.go:165), and `currentCreation` persists that phase as a terminal conflict at [creation.go](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/dev-workspace/portal/internal/web/creation.go:217).

Afterward, conflicts are returned without reconciliation at [creation.go](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/dev-workspace/portal/internal/web/creation.go:209). If the user revives that archive through the supported lifecycle, the session becomes active again, but its page continues displaying “This session is archived” through [server.go](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/dev-workspace/portal/internal/web/server.go:820).

This does not hide or corrupt the revived session, but it freezes a transient canonical lifecycle fact into a longer-lived receipt state. Derive the displayed lifecycle qualifier from the current summary, or normalize the archived conflict after revival. Cover archive-without-evidence → page reconciliation → revive.

## Retention decision

The decision to retain timing summaries is consistent with the actual lifecycle and identity contracts:

- Archive and delete both retire a conversation through `retire_portal_thread!` at [dev-session](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/dev-workspace/libexec/dev-session:1421) and [dev-session](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/dev-workspace/libexec/dev-session:1565).
- Retirement calls App Server `thread/archive`, not conversation deletion, at [client.go](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/dev-workspace/portal/internal/workspacecodex/client.go:289).
- Session deletion moves tracking and its creation journal into private recovery storage at [dev-session](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/dev-workspace/libexec/dev-session:4661).
- Activity storage is keyed by authority and hashed thread identity, not by slug, at [activity.go](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/dev-workspace/portal/internal/web/activity.go:46) and [activity_store.go](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/codex-web/codex/activity_store.go:89). Conversation resolution always supplies the thread ID from the current manifest at [server.go](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/dev-workspace/portal/internal/web/server.go:2264).

A reused slug therefore selects its new manifest’s thread and cannot expose the old thread’s timing. An archived or revived session retaining the same thread correctly retains its totals. Deleting timing during the current delete operation would conflict with the retained-conversation and recovery contract; no existing component owns a permanent conversation purge.

The real residual cost is confirmed: every finalized turn creates a separate durable summary at [activity_store.go](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/codex-web/codex/activity_store.go:275), with no expiry or quota. Recording that inode/disk growth as Advisory is proportionate. A future purge or quota feature should coordinate conversation and timing retention rather than silently expiring one side.

## Other architecture assessment

The history-cache repair has coherent ownership: watches and active or queued readers share one cache object; completed unowned histories retire; only eight incomplete idle histories retain retry progress. The map mutex, per-thread gate, and release ordering address the previously identified replacement race.

The journal-authority repair also has the right boundary. The portal forwards immutable validated receipt arguments at [creation.go](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/dev-workspace/portal/internal/web/creation.go:543), while Ruby alone validates the strict fork-journal shape at [dev-session](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/dev-workspace/libexec/dev-session:2952). Portal checks for start/fork journal presence without duplicating their field schema. Fresh attempts still validate their live source, while established destination journals own exact recovery.

The dependency chain is consistent: runtime Go, Nix source, organization wrapper, and consuming workspace all select `bdd79be2`, `87606197`, and `db25c77e` as appropriate. No additional public interface, persistent schema, or consumer-side journal registry was introduced.

Per instruction, I ran no tests. Packaged VM, live App Server/browser, profile upgrade, and rollback validation remain pending.