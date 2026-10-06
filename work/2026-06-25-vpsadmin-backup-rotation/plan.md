# 2026-06-25-vpsadmin-backup-rotation

## Goal
Find and fix a vpsAdmin backup-branch metadata bug that lets rotation attempt
to destroy rollback parent snapshots on `backuper2.prg` while ZFS still has
dependent clones. Provide a production repair path for the three affected VPS
datasets.

## Affected repositories
- `vpsadmin`: rollback/backup branch metadata and tests.
- `vpsfree-maintenance-tasks`: likely operational repair script for existing
  production state if SQL/ZFS remediation is non-trivial.

## Approach
- Reproduce the failure in vpsAdmin tests from the production shape:
  rollback-created backup branch, later backup snapshots on the dependent
  branch, missing dependency metadata/reference counts, and rotation scheduling
  the parent snapshot for destruction.
- Fix the root cause so rollback and/or later backup transfer creates
  `snapshot_in_pool_in_branches.snapshot_in_pool_in_branch_id` and
  `snapshot_in_pools.reference_count` consistently with ZFS clone origins.
- Add focused specs for the reproduction and for future backup snapshots after
  rollback.
- Add an operational repair task/script if production needs more than a small
  SQL update.

## Compatibility and deployment
- Existing ZFS datasets and branch trees must remain readable; the fix should
  only add missing metadata edges that reflect already-existing ZFS clone
  dependencies.
- Mixed deployment risk is limited to vpsAdmin API scheduling new transaction
  chains and nodectld applying confirmations. New chains created before the API
  fix can still carry stale metadata and may need the repair task.
- No schema change is planned unless reproduction proves the current tables
  cannot represent the dependency.
- Rollback: reverting code stops creating the new metadata but does not need
  to undo repaired reference counts because those counts represent real ZFS
  dependencies.

## Testing plan
- Run focused API specs for dataset rollback/backup rotation.
- Run RuboCop for touched API files.
- Run maintenance task checks if a script is added.
- Run mandatory change review after commits and quick local verification, then
  decide whether a longer integration test is needed.
