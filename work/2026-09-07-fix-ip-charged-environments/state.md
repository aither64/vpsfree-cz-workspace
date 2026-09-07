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
  source changes.
  - reference branch: `2026-09-07-fix-ip-charged-environments`
  - worktree:
    `worktrees/2026-09-07-fix-ip-charged-environments/vpsadmin`
  - base: `origin/master` at
    `cd3fac386ee34ba81387c379b2b48aee9170111f`

## Status

- Investigation confirmed that owned IPs with a null charged environment fail
  disowning in `TransactionChains::Ip::Update#reallocate_user`.
- Implementation plan agreed with the user.
- Implemented the interactive repair task. It discovers all affected
  VPS-purpose addresses, validates each owner/resource group, prints safe and
  blocked groups, requires an exact `yes`, and revalidates under application
  and database locks before changing any row.
- Applied the workspace user-facing writing skill to the preview, diagnostics,
  and confirmation text.
- Committed the implementation as `34d5121` on the
  `2026-09-07-fix-ip-charged-environments` branch and pushed it to the SSH
  `origin` remote.
- Mandatory change review completed with High risk classification. The General,
  Architecture, Scope, and Risk lanes all used `gpt-5.6-sol` with `xhigh`
  reasoning. All blocking and important findings were remediated and folded
  into the feature commit.
- No GitHub Actions workflows were registered for the pushed branch.

## Commands run

- `dev-session start fix-ip-charged-environments --no-attach --no-codex --json`
- `dev-session worktree add 2026-09-07-fix-ip-charged-environments vpsfree-maintenance-tasks --as-is --base origin/master`
- `dev-session worktree add 2026-09-07-fix-ip-charged-environments vpsadmin --as-is`
- Read the workspace and repository instructions, current vpsAdmin IP ownership
  and resource-accounting code, relevant migrations, resource locking, and
  earlier maintenance tasks.
- `ruby -c 2026-09-07-fix-ip-charged-environments/fix_ip_charged_environments.rb`
- Ran a disposable API-database validation through `nix develop .#api` using
  the vpsAdmin source deployed with the reported failure and its JSON 2.21.2
  dependency version.
- Ran `git diff --check` before and after review remediation.
- Fetched `origin/master`; it remains at the initiative base, so no rebase was
  needed.
- Pushed branch `2026-09-07-fix-ip-charged-environments` to GitHub and queried
  GitHub Actions for the branch.

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
- Disposable database validation covered mixed target environments for one
  user, VPS and unassigned inference, export exclusion, accounting conflicts,
  inconsistent primary mappings, a missing environment config, cancellation,
  stale-plan rollback, lock release, PaperTrail attribution, unchanged cluster
  resource uses, and an idempotent second plan.
- Expanded validation after review also covered userless assigned addresses,
  wrong-owner resource-use rows, missing environments and networks, export
  interfaces, partial application of safe groups, and full rollback after an
  injected failure on the second IP update. The final run printed
  `repair task validation passed`.
- Review found that userless VPS addresses and wrongly linked resource-use rows
  could escape the original consistency guard. The final implementation treats
  every relevant uncharged address as a group blocker, validates resource uses
  reached through either side of the association, uses canonical IP resource
  mapping, locks exact owner/resource pairs, and fails closed if an application
  lock cannot be acquired.
- The task prints every acquired `ResourceLock` ID. A hard-killed process can
  leave an ownerless lock row, so its header documents the recovery procedure:
  first verify that the task is no longer running, then inspect and remove only
  the printed IDs. This is an accepted operational residual risk rather than a
  silent cleanup heuristic.
- vpsAdmin `origin/master` advanced only in packaged gem locks relative to the
  deployed revision. Its current JSON 3.0.0 lock cannot boot ActiveSupport
  serialized attributes; validation used the deployed JSON 2.21.2 lock. No
  vpsAdmin source was changed.

## Remaining work

- Review and merge the pushed maintenance-task branch before running the script
  in production.

## Cleanup

- Both worktrees are clean. They remain active pending branch review and merge.
- Disposable validation code, the generated API Gemfile lock, and the local
  Bundler cache were removed after testing.
- No production command has been run and no production data has been changed.
