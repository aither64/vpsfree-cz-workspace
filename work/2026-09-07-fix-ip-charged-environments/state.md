---
lifecycle: active
---

# 2026-09-07-fix-ip-charged-environments

## Repositories

- `vpsfree-maintenance-tasks`
  - branch: `2026-09-07-fix-ip-charged-environments`
  - worktree:
    `worktrees/2026-09-07-fix-ip-charged-environments/vpsfree-maintenance-tasks`
  - base: `origin/master` at
    `996585953bf54fe928843e7f21b7fd501a31375f`
- `vpsadmin`: inspected through the canonical bare repository; no feature
  worktree or source changes.

## Status

- Investigation confirmed that owned IPs with a null charged environment fail
  disowning in `TransactionChains::Ip::Update#reallocate_user`.
- Implementation plan agreed with the user.
- Maintenance-task worktree created; implementation not started.

## Commands run

- `dev-session start fix-ip-charged-environments --no-attach --no-codex --json`
- `dev-session worktree add 2026-09-07-fix-ip-charged-environments vpsfree-maintenance-tasks --as-is --base origin/master`
- Read the workspace and repository instructions, current vpsAdmin IP ownership
  and resource-accounting code, relevant migrations, resource locking, and
  earlier maintenance tasks.

## Results

- Environment selection policy:
  - assigned IP: environment of the current VPS node location;
  - unassigned IP: environment of the network primary location.
- Existing cluster resource use is a consistency authority. A mismatch blocks
  the affected owner/resource group instead of being recalculated.
- The task will run online with application locks, database locks, and an exact
  post-confirmation plan comparison.
- The task must clearly list VPS ID and hostname for assigned addresses and
  require an exact interactive confirmation before writing.

## Open questions

- None.

## Cleanup

- Worktree is active and must remain until review and testing are complete.
- No production command has been run and no production data has been changed.
