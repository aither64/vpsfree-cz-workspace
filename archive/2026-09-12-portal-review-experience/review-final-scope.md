# Scope and proportionality review

Review result: **0 Blocking, 1 Important, 1 Advisory.**

Reviewed the final committed ranges through `codex-web` `bdd79be2`, `dev-workspace` `8760619`, `vpsfree-dev-workspace` `db25c77`, and `workspace` `584ea0f`. I ran no tests or mutating commands.

## Findings

### Important — A nonterminal creation receipt survives destination deletion and can recreate the deleted session

Commit `106c4003` leaves `failed` and `paused` receipts outside completed-deletion cleanup. [`retireAbsentCreation()`](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/dev-workspace/portal/internal/web/creation_store.go:167) only retires `ready` or `conflict` receipts. When no destination remains, [`currentCreation()`](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/dev-workspace/portal/internal/web/creation.go:203) cannot prove completion or find a canonical conflict, so it keeps the nonterminal receipt and [`creationPage()`](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/dev-workspace/portal/internal/web/creation.go:238) continues to hide the absent destination behind retry UI.

This interacts incorrectly with the supported deletion lifecycle:

1. The CLI completes a destination but interruption before receipt evidence leaves the portal receipt failed or paused—the exact recovery boundary repaired in this pass.
2. `dev-session delete` archives the Codex thread and removes the destination. [`preserve_removed_state!()`](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/dev-workspace/libexec/dev-session:4661) moves the strict destination creation journal and tracking into deletion recovery, but does not retire the portal receipt or its binding.
3. A different request for the now-deleted slug is rejected by [`acceptCreation()`](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/dev-workspace/portal/internal/web/creation.go:101), while retrying the old receipt launches initialization again.
4. For `new`, Ruby now sees neither live destination state nor a destination journal and creates a fresh journal at [`dev-session:2553`](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/dev-workspace/libexec/dev-session:2553), recreating the explicitly deleted session. Plan/fork retries do likewise when their source remains available; otherwise the stale receipt continues reserving the slug.

This violates completed deletion/name-reuse behavior and lets stale additive portal state undo an explicit destructive lifecycle outcome. Record completed deletion as terminal for any matching portal receipt—retiring or moving its receipt/binding with the deletion recovery state—while preserving genuinely incomplete attempts where no deletion occurred. Add focused destination evidence-gap → delete → restart/retry tests for new, plan, and fork.

### Advisory — The archive-specific receipt notice becomes permanently false after revival

[`canonicalCreationConflict()`](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/dev-workspace/portal/internal/web/creation.go:165) persists “This session is archived” as a terminal `conflict`. Conflicts are returned without re-evaluating canonical state at [`creation.go:210`](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/dev-workspace/portal/internal/web/creation.go:210), and [`sessionPage()`](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/dev-workspace/portal/internal/web/server.go:820) displays the stored phase. After the supported `dev-session revive` flow restores the session to active use, the page therefore continues saying it is archived.

This does not block the revived session, but the notice should either describe the historical conflict without asserting current lifecycle state or be recalculated after revival.

## Retention decision

The durable-timing decision is proportionate and remains an **Advisory operational limitation**, not an Important lifecycle defect.

The code supports the stated contract:

- Deletion archives rather than purges the Codex thread at [`workspacecodex/client.go:289`](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/dev-workspace/portal/internal/workspacecodex/client.go:289), while tracking and creation state are retained in private recovery.
- Recorder paths are keyed from the original thread identity, not the portal slug, at [`activity_store.go:89`](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/codex-web/codex/activity_store.go:89).
- Browser reads select the current manifest’s thread ID at [`server.go:2310`](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/dev-workspace/portal/internal/web/server.go:2310), so slug reuse cannot select an old thread’s timing.
- Persistent turn records contain identities, bounds, and totals—not prompts, commands, or answers—at [`activity.go:41`](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/codex-web/codex/activity.go:41).

Each finalized turn still creates one retained file and there is no aggregate quota. That is real disk/inode growth, but adding expiry now would create an unsupported purge/recovery contract and could discard requested archived totals. Coordinated conversation-and-timing retention should remain a later explicit feature.

## Proportionality assessment

The other final mechanisms are appropriately narrow:

- History ownership uses one existing map mutex, per-thread gates, and an eight-entry partial-backfill list; it directly addresses active-reader replacement and cancelled-backfill progress without creating a general cache framework.
- The scheduler is a single four-slot channel shared by worker and browser reads. RPC deadlines begin after acquisition, while subscriptions and notifications remain independent.
- Noninteractive polling stops with one browser condition while failed initial reads remain retryable.
- Strict fork-journal parsing was removed from Go. The portal supplies frozen validated arguments, while Ruby’s existing locked journal loaders remain the sole exact schema/recovery authority.
- Provider, runtime, organization, and workspace pins select the same final dependency chain; no additional dependency or Codex-version compatibility surface was introduced.

Remaining planned gates are the packaged VM, live creation/browser flow, profile switch, and rollback tests. The new destination-deletion regression above should be resolved before those long checks.