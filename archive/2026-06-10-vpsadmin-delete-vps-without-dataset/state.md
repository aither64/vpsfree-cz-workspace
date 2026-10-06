---
lifecycle: abandoned
---
# 2026-06-10-vpsadmin-delete-vps-without-dataset

## Repositories

- `vpsadmin`

## Status

- Investigation complete. Recommended recovery is to recreate the missing
  `dataset_in_pools` association(s), then run the normal admin hard-delete
  path.

## Commands run

- `bin/dev-session current`
- `find work/2026-06-10-vpsadmin-delete-vps-without-dataset -maxdepth 2 -type f -print`
- `find worktrees/2026-06-10-vpsadmin-delete-vps-without-dataset -maxdepth 3 -type d -print`
- `git --git-dir=repos/vpsadmin.git worktree list`
- `git --git-dir=repos/vpsadmin.git remote -v`
- `git --git-dir=repos/vpsadmin.git rev-parse origin/master`
- `git --git-dir=repos/vpsadmin.git fetch origin`
- `git --git-dir=repos/vpsadmin.git worktree add -b 2026-06-10-vpsadmin-delete-vps-without-dataset worktrees/2026-06-10-vpsadmin-delete-vps-without-dataset/vpsadmin origin/master`
- `sed -n '1,240p' AGENTS.md`
- `rg ... api/models api/lib api/db`
- `sed -n ... api/models/vps.rb api/models/dataset*.rb api/models/transaction_chains/vps/*.rb`
- `sed -n ... api/models/transaction_chains/network_interface/*.rb api/models/transaction_chains/export/*.rb`
- `sed -n ... api/db/schema.rb api/lib/vpsadmin/api/lifetimes.rb`
- `sed -n ... api/lib/vpsadmin/api/resources/vps.rb`
- `git --git-dir=repos/vpsadmin.git worktree remove worktrees/2026-06-10-vpsadmin-delete-vps-without-dataset/vpsadmin`

## Results

- Active initiative slug is `2026-06-10-vpsadmin-delete-vps-without-dataset`.
- `repos/vpsadmin.git` exists and uses the required SSH GitHub remote.
- Created `worktrees/2026-06-10-vpsadmin-delete-vps-without-dataset/vpsadmin`
  on branch `2026-06-10-vpsadmin-delete-vps-without-dataset`.
- Worktree creation reported that Overcommit hooks are installed but the
  `overcommit` gem is missing in the ambient shell. No commits were made.
- `Vps::SoftDelete` and `Vps::Destroy` both call `lock(vps.dataset_in_pool)`.
  Missing association rows therefore break normal deletion.
- `Vps::Destroy` removes network interfaces, routes/IP assignments, export host
  permissions, mounts, cluster resource uses, statuses, OOM data, SSH host keys,
  and export mount rows through normal transaction confirmations.
- Admin API delete with `lazy=false` requests `hard_delete`.
- Preferred recovery is to recreate missing `dataset_in_pools` rows with the
  correct pool and dataset, then use normal hard-delete. Directly changing
  `vpses.object_state` would leave too much related state behind.
- Added durable note
  `notes/vpsadmin/2026-06-10-delete-vps-missing-dataset-in-pool.md`.

## Open questions

- Which exact production VPS id is affected.
- Whether the empty replacement dataset is represented in vpsAdmin's database
  or only on the node/storage side.
- Whether any `mounts.dataset_in_pool_id` rows for the VPS also point to
  missing rows.

## Cleanup

- Removed
  `worktrees/2026-06-10-vpsadmin-delete-vps-without-dataset/vpsadmin`.
- Kept local branch `2026-06-10-vpsadmin-delete-vps-without-dataset` and
  durable notes.

## Archival request, 2026-10-06

The workspace operator requested archival of sessions dated August 2026 or
older, retaining recorded work and branches. This checkpoint commits the
existing plan and active state before the ordinary archive transition.
