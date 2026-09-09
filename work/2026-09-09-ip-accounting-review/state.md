---
lifecycle: active
---

# IP accounting audit

## Repositories

- vpsfree-maintenance-tasks: branch `2026-09-09-ip-accounting-review`, worktree
  `worktrees/2026-09-09-ip-accounting-review/vpsfree-maintenance-tasks`, base
  `6eea682` (origin/master).
- vpsadmin: reference-only branch `2026-09-09-ip-accounting-review`, worktree
  `worktrees/2026-09-09-ip-accounting-review/vpsadmin`, base `19971f039`.

## Status

- Verified current session matches VPSFREE_DEV_SESSION_SLUG.
- Read project instructions and workspace review, writing, handoff skills.
- Inspected IP allocation repair tasks, UserClusterResource.used,
  User.calculate_cluster_resources_in_env, IpAddress and Network models.
- Maintenance repository and shared workspace declare no hook framework.
- Initial implementation in progress. No production access or writes.

## Commands and results

- Fetched both project repositories and added isolated worktrees via dev-session.
- vpsAdmin post-checkout Overcommit rejected the configuration signature after
  worktree creation. Worktree was present and clean; repeating dev-session add
  registered it successfully. Existing lesson:
  notes/cross-project/2026-06-07-overcommit-worktree-add.md.
- Schema amounts are decimal(40,0); package allowance sums assigned package
  items in the assignment environment. UserClusterResource.used includes only
  enabled and confirmed rows. IP ownership takes precedence over VPS ownership.

## Next steps

Implement task and tests, quick verification, committed change review, then
handoff with usage and portal link. Keep branch/worktrees for user review.

## Cleanup

No transient processes yet. Reference checkout is read-only.
