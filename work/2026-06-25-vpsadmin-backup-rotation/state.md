---
lifecycle: active
---
# 2026-06-25-vpsadmin-backup-rotation

## Repositories
- `vpsadmin`
  - Worktree: `worktrees/2026-06-25-vpsadmin-backup-rotation/vpsadmin`
  - Branch: `2026-06-25-vpsadmin-backup-rotation`
- `vpsfree-maintenance-tasks`
  - Worktree:
    `worktrees/2026-06-25-vpsadmin-backup-rotation/vpsfree-maintenance-tasks`
  - Branch: `2026-06-25-vpsadmin-backup-rotation`

## Status
- Reusing active dev session `2026-06-25-vpsadmin-backup-rotation`.
- Investigating production failures where `DestroySnapshot` on backup branch
  snapshots fails with `snapshot has dependent clones`.
- Root cause: backups appended after rollback to a backup head branch that is
  still a ZFS clone did not inherit that branch's
  `SnapshotInPoolInBranch` parent metadata. The new snapshots therefore did
  not increment the origin snapshot's `SnapshotInPool.reference_count`, so
  rotation later scheduled the origin snapshot for destruction even though ZFS
  still had dependent clone branches.
- Reproduced a prevention failure in an API unit spec: when backup snapshots
  are appended to a backup head branch that is itself a ZFS clone of another
  branch snapshot, the new branch entries get no parent pointer and the parent
  snapshot reference count is not incremented.
- Added a vpsAdmin fix in `TransactionChains::Dataset::Send` to inherit the
  branch clone parent for new branch entries.
- Added a vpsfree-maintenance-tasks dry-run/apply script to repair the three
  known production datasets.
- Committed both repositories and completed quick local verification.
- Revisited the diagnosis after the first production run found a maintenance
  script pool lookup bug and an independent reviewer questioned the rollback
  metadata path.

## Commands run
- `bin/dev-session current`
- `git --git-dir=repos/vpsadmin.git fetch origin --prune`
- `git --git-dir=repos/vpsadmin.git --work-tree=worktrees/2026-06-25-vpsadmin-backup-rotation/vpsadmin worktree add -b 2026-06-25-vpsadmin-backup-rotation worktrees/2026-06-25-vpsadmin-backup-rotation/vpsadmin origin/master`
- Read vpsAdmin `AGENTS.md`.
- Inspected rollback, transfer, rotate, destroy snapshot, branch create, and
  branch metadata models/specs with `rg`/`sed`.
- `nix develop .#api -c bundle exec rspec spec/models/transaction_chains/dataset/transfer_spec.rb:102`
  - Before fix: failed because `snapshot_in_pool_in_branch_id` was `NULL`.
  - After first patch: failed because legacy `append` rebinds `self` to
    `Transaction::Confirmable`; fixed by resolving the branch parent outside
    the confirmation block.
  - After fix: passed.
- `nix develop .#api -c bundle exec rspec spec/models/transaction_chains/dataset/transfer_spec.rb spec/models/transaction_chains/dataset/rollback_spec.rb spec/models/transaction_chains/dataset/rotate_spec.rb spec/models/transaction_chains/snapshot_in_pool/destroy_spec.rb`
  - Result: 26 examples, 0 failures, 1 pending.
- Re-ran the same focused suite after review-driven clarification:
  26 examples, 0 failures, 1 pending.
- `nix develop .#api -c bundle exec rubocop models/transaction_chains/dataset/send.rb spec/models/transaction_chains/dataset/transfer_spec.rb`
  - Result: no offenses.
- `nix develop .#api -c bundle exec rubocop models/transaction_chains/dataset/send.rb models/transaction_chains/dataset/rollback.rb spec/models/transaction_chains/dataset/transfer_spec.rb`
  - Result: no offenses.
- `git diff --check`
  - Result: clean.
- `nix develop -c bundle exec overcommit --install`
- `nix develop -c bundle exec overcommit --sign`
- `nix develop -c git commit -F /tmp/vpsadmin-commit-message`
  - Result: hooks passed and commit was created.
- `git --git-dir=repos/vpsfree-maintenance-tasks.git fetch origin --prune`
- `git --git-dir=repos/vpsfree-maintenance-tasks.git --work-tree=worktrees/2026-06-25-vpsadmin-backup-rotation/vpsfree-maintenance-tasks worktree add -b 2026-06-25-vpsadmin-backup-rotation worktrees/2026-06-25-vpsadmin-backup-rotation/vpsfree-maintenance-tasks origin/master`
- Read vpsfree-maintenance-tasks `AGENTS.md`.
- `./new fix-backup-branch-dependencies api`
- `ruby -c 2026-06-25-fix-backup-branch-dependencies/fix_backup_branch_dependencies.rb`
- `git add -N 2026-06-25-fix-backup-branch-dependencies/fix_backup_branch_dependencies.rb && git diff --check`
  - Result: clean.
- `git commit -F /tmp/vpsfree-maintenance-tasks-commit-message`
  - Result: commit was created; this repository declares no hook framework.

## Results
- vpsAdmin worktree was created from `origin/master` at `858d4ec49`.
- vpsAdmin commit:
  `194aecc40 api: preserve backup branch clone dependencies`.
  - Amended after independent review to clarify the rollback/send dependency
    handoff in comments and the regression spec. No behavior changed from the
    original prevention patch.
- vpsAdmin Overcommit hooks were installed/signed and run through
  `nix develop`.
- Existing pending rotate spec mentions this class of issue:
  branched rotation can strand snapshots because dependency metadata is
  incomplete.
- New reproduction spec confirms the missing metadata path for future snapshots
  on dependent backup head branches.
- vpsfree-maintenance-tasks worktree was created from `origin/master` at
  `5e4532a`.
- vpsfree-maintenance-tasks commit:
  `4f48c0e 2026-06-25-fix-backup-branch-dependencies: add repair script`.
  - Amended after production dry-run showed that `Pool.filesystem` is not
    unique. The script now selects the exact pool by filesystem and
    `pool.node.domain_name == backuper2.prg`, and fails with a list of
    matching pools when the target pool cannot be found.
- Maintenance script:
  `2026-06-25-fix-backup-branch-dependencies/fix_backup_branch_dependencies.rb`
  encodes the immediate dependency edges:
  - `29494`: `branch-2026-05-19T02:28:40.0` depends on
    `branch-2026-06-02T23:00:32.0@2026-06-02T23:00:32`.
  - `28821`: `branch-2026-06-04T23:00:21.0` depends on
    `branch-2026-06-02T23:00:21.0@2026-06-02T23:00:21`.
  - `28915`: `branch-2026-06-16T23:00:01.0` depends on
    `branch-2026-06-02T23:00:01.0@2026-06-02T23:00:01`, and
    `branch-2026-05-20T13:13:45.0` depends on
    `branch-2026-06-16T23:00:01.0@2026-06-16T23:00:01`.

## Open questions
- Production should dry-run the maintenance script first. Applying can be done
  before or after deploying the API fix, but should happen while affected
  backup dataset actions are not running; the API fix prevents recurrence for
  newly appended backup snapshots.

## Mandatory change review
- Reviewer agent: `019f0062-ff15-7b21-857c-564653885779`.
- Result: no blocking, important, or advisory findings.
- Residual risks noted by reviewer:
  - The repair script still needs production dry-run review before `--apply`.
  - Old workers or already-created old transaction chains can still append bad
    metadata until the API fix is deployed.
  - Quick tests are metadata/unit coverage, not a full ZFS integration proof;
    the broader branched-rotation pending case remains outside this fix.
- Follow-up reviewer agent: `019f04e7-4d7e-72b0-8ec5-b9c7c52b197c`.
- Result: raised one blocking concern that the prevention patch might miss a
  newly rollback-created branch with no existing parented entries, confirmed
  the repaired maintenance script selects the `backuper2.prg` pool, and
  advised verifying encoded repair edges against ZFS origins before `--apply`.
- Resolution of blocking concern: inspected rollback and nodectld branch
  creation. `BranchDataset` clones and immediately promotes the new rollback
  branch; rollback already schedules parent metadata for entries left on the
  old branch, which is the branch that later can become head while still being
  a ZFS clone. The send fix deliberately inherits from those existing parented
  entries. Added comments in rollback/send and the transfer regression spec to
  make this contract explicit.
- Need run one more fresh independent review on the amended committed state
  before force-pushing rewritten branches.
- Fresh reviewer agent: `019f04f5-64eb-7ce2-b8d8-09dae04cb2e6`.
- Result: no blocking, important, or advisory findings on amended committed
  state.
- Reviewer agreed the earlier concern is resolved by the rollback
  clone-then-promote flow: the newly created rollback branch is promoted, while
  the old branch remains the dependent clone and already has parent metadata on
  newer entries for `send.rb` to inherit.
- Reviewer residual risks before production `--apply`:
  - inspect repair-script dry-run output against live ZFS origin/clone
    evidence for all encoded edges;
  - ensure affected `DatasetInPool`s have no active/queued operations;
  - note that verification remains metadata/unit coverage, not a live ZFS
    integration proof.

## Push and CI
- Pushed `vpsfree-maintenance-tasks` branch
  `2026-06-25-vpsadmin-backup-rotation` to GitHub.
- Amended `vpsfree-maintenance-tasks` locally from `fd12771` to `4f48c0e`
  after production reported that the repair script selected the
  `storage/vpsfree.cz/backup` pool on `backuper.prg` instead of
  `backuper2.prg`.
- Initial ambient-shell push of `vpsadmin` failed because the Overcommit
  pre-push hook could not find the `overcommit` gem; retrying through
  `nix develop -c git push ...` succeeded.
- Pushed `vpsadmin` branch `2026-06-25-vpsadmin-backup-rotation` to GitHub.
- vpsAdmin GitHub Actions for head
  `c34b94612841f8195f52074e3217509c23e3973d`:
  - `28197436618` API Specs (topic parallel): success.
  - `28197436663` CI: success after 2h24m1s.
  - `28197436653` RuboCop: success.
- vpsfree-maintenance-tasks had no workflow runs for the branch at first check.
- Final branch workflow sweep confirmed all vpsAdmin runs completed
  successfully and vpsfree-maintenance-tasks still had no branch workflow runs.
- Both repository worktrees were clean after push and workflow monitoring.
- Both branches are currently rewritten locally and need force-push with lease
  after the fresh review:
  - vpsAdmin: `c34b94612` -> `194aecc40`.
  - vpsfree-maintenance-tasks: `fd12771` -> `4f48c0e`.
- Force-pushed both rewritten branches with lease:
  - vpsAdmin `c34b94612...194aecc40`.
  - vpsfree-maintenance-tasks `fd12771...4f48c0e`.
- Fresh vpsAdmin GitHub Actions for head
  `194aecc40ef5b7db33bdadf0c9c6221bf0b31f51`:
  - `28254364019` CI: success after 2h28m11s.
  - `28254364055` RuboCop: success.
  - `28254364347` API Specs (topic parallel): success.
- Old vpsAdmin runs for `c34b94612` were already completed, so no
  superseded queued/in-progress runs needed cancellation.
- vpsfree-maintenance-tasks still had no workflow runs for the branch after
  force-push.
- Final branch workflow sweep confirmed all current-head vpsAdmin runs
  completed successfully, vpsfree-maintenance-tasks still had no branch
  workflow runs, and both repository worktrees were clean.

## Default branch merge
- Fetched current `origin/master` for both code repositories before merge.
- vpsAdmin `master` had advanced from the original base by
  `1f5c2f5d6 packages: update gem dependencies`; rebased the feature commit
  onto it with hooks active through `nix develop`.
- Rebased vpsAdmin feature head:
  `f42b44d64abe4b4dfe77cf8a44eca09dc9640408`.
- Re-ran quick checks after the rebase:
  - `nix develop .#api -c bundle exec rspec
    spec/models/transaction_chains/dataset/transfer_spec.rb:102
    spec/models/transaction_chains/dataset/rollback_spec.rb:73`: passed.
  - `nix develop .#api -c bundle exec rubocop
    models/transaction_chains/dataset/send.rb
    models/transaction_chains/dataset/rollback.rb
    spec/models/transaction_chains/dataset/transfer_spec.rb`: passed.
  - `ruby -c
    2026-06-25-fix-backup-branch-dependencies/fix_backup_branch_dependencies.rb`:
    passed.
- Created fresh merge worktrees under
  `worktrees/2026-06-25-vpsadmin-backup-rotation/merge/` and fast-forwarded:
  - vpsAdmin `master`: `1f5c2f5d6` -> `f42b44d64`.
  - vpsfree-maintenance-tasks `master`: `5e4532a` -> `4f48c0e`.
- Pushed both default branches to GitHub.
- vpsAdmin `master` workflows for `f42b44d64`:
  - `28263385305` RuboCop: success.
  - `28263385320` API Specs (topic parallel): success.
  - `28263385304` CI: success after 2h39m0s.
- vpsfree-maintenance-tasks did not start any new workflow for the `master`
  push.
- Local vpsAdmin feature branch was rebased to `f42b44d64` before merging;
  the remote feature branch still points to the earlier reviewed head
  `194aecc40`. `master` contains the rebased commit and is the deployed
  history. The remote feature branch was not force-pushed again to avoid
  starting another redundant branch workflow after the default branch was
  already green.

## Configuration channel update
- Added `vpsfree-cz-configuration` worktree:
  `worktrees/2026-06-25-vpsadmin-backup-rotation/vpsfree-cz-configuration`.
- Ran `nix develop -c confctl inputs channel ls`; before update,
  `vpsadmin` channel role `vpsadmin` input `vpsadminServices` pointed to
  `b16caa7f`.
- Ran `nix develop -c confctl inputs channel update --commit vpsadmin`.
- Generated commit:
  `b9475aae inputs: update vpsadminServices to f42b44d6`.
- Verified with `confctl inputs channel ls` that `vpsadminServices` now points
  to `f42b44d6`, matching the merged vpsAdmin `master` head.
- Created fresh config merge worktree and fast-forwarded `master`:
  `8b30c516` -> `b9475aae`.
- Pushed `vpsfree-cz-configuration` `master` to GitHub.
- `vpsfree-cz-configuration` did not start a push workflow; only scheduled
  Daily update runs were listed.
- Removed local `.bin/` and `.bundle/` helper directories created by the config
  dev shell from both config worktrees.

## Cleanup
- Removed all worktrees under
  `worktrees/2026-06-25-vpsadmin-backup-rotation/` after the code and
  configuration changes were merged and pushed.
- Kept feature branch refs as required. The vpsAdmin remote feature branch was
  left at the pre-rebase reviewed SHA, as noted above, to avoid an extra
  redundant CI cycle after `master` was already green.

## Follow-up integration coverage
- User asked to return to the work branch and implement an integration test for
  the missing scenario: create snapshots, roll back a VPS dataset across backup
  branches, then verify rotation takes care of the dependent branch safely.
- Latest user instruction: do not merge to `master` without explicit approval.
  This follow-up is therefore being developed and pushed on the feature branch
  only.
- Recreated vpsAdmin worktree:
  `worktrees/2026-06-25-vpsadmin-backup-rotation/vpsadmin`.
- Recreated detached pre-fix scratch worktree:
  `worktrees/2026-06-25-vpsadmin-backup-rotation/vpsadmin-pre-fix`.
- Added dedicated test
  `tests/suite/storage/rollback-dependent-branch-rotation.nix` and registered
  it in `tests/all-tests.nix`.
- Initial attempt to extend `storage/branching-rotation` was discarded because
  the second VPS setup in the same test file reused the existing pool filesystem
  context and exposed a separate `CreateTree`/`tree.0` collision instead of the
  production rollback/rotation regression.
- Fixed-branch integration result:
  `./test-runner.sh test --fresh storage/rollback-dependent-branch-rotation`
  passed in 1093.48 seconds.
- Pre-fix reproduction result at parent commit `1f5c2f5d6` with only the new
  test applied:
  `./test-runner.sh test --fresh storage/rollback-dependent-branch-rotation`
  failed in 1076.69 seconds.
- Pre-fix failure evidence:
  - metadata assertion saw appended backup branch parents `[2, nil, nil]`
    instead of all entries depending on parent entry `2`;
  - rotation then failed with the production-shaped ZFS error
    `snapshot has dependent clones` while destroying
    `tank/backup/1/tree.0/branch-2026-06-27T10:37:56.0@2026-06-27T10:37:56`.
- Quick checks on the fixed worktree:
  - `nix-instantiate --parse tests/all-tests.nix`
  - `nix-instantiate --parse
    tests/suite/storage/rollback-dependent-branch-rotation.nix`
  - `git diff --check`
  - `ruby tests/ci-selection-test.rb`: 15 runs, 54 assertions, 0 failures.
  - `./test-runner.sh ls --filter 'tag=ci && tag=storage-rollback &&
    tag=storage-rotation'`: selected only
    `storage/rollback-dependent-branch-rotation`.
- Committed vpsAdmin follow-up:
  `c9cc15ce0 tests: cover rollback backup branch rotation`.
- Mandatory follow-up review:
  - Reviewer agent: `019f08b2-e556-7220-8b27-0653e00dad3d`.
  - Result: no blocking, important, or advisory findings.
  - Reviewer confirmed the test uses a real two-node VPS backup flow, marker
    data integrity checks, rollback through `s2`, restore of `s3` from backup,
    backup-head ZFS clone verification, parent dependency assertions, and
    rotation verification.
  - Reviewer residual risk: did not rerun the full integration test, relying on
    the fixed/pass and pre-fix/fail evidence recorded above.
- Force-pushed feature branch only, per user instruction not to merge without
  approval:
  `194aecc40...c9cc15ce0
  2026-06-25-vpsadmin-backup-rotation`.
- Current-head GitHub Actions for vpsAdmin branch at
  `c9cc15ce09a949c3b917432dc7cf839b15ec57f5` started:
  - `28287180239` RuboCop: success.
  - `28287180245` CI: success after 4h28m9s.
  - `28287180258` API Specs (topic parallel): success.
- Final branch workflow sweep confirmed all current-head vpsAdmin runs
  completed successfully. No default branch merge was performed for this
  follow-up.

## Follow-up default branch merge
- User approved merging the follow-up test commit to `master`.
- Created fresh detached merge worktree:
  `worktrees/2026-06-25-vpsadmin-backup-rotation/merge/vpsadmin`.
- Fast-forwarded from `origin/master`:
  `f42b44d64` -> `c9cc15ce0`.
- Quick checks in the merge worktree:
  - `nix-instantiate --parse tests/all-tests.nix`
  - `nix-instantiate --parse
    tests/suite/storage/rollback-dependent-branch-rotation.nix`
  - `git diff --check origin/master..HEAD`
- Pushed vpsAdmin `master`:
  `f42b44d64..c9cc15ce0`.
- Fetched after push and verified:
  `origin/master` and `origin/2026-06-25-vpsadmin-backup-rotation` both point
  to `c9cc15ce09a949c3b917432dc7cf839b15ec57f5`.
- Current-head GitHub Actions for vpsAdmin `master`:
  - `28296563755` CI: success after 6h18m10s.
- Final `master` workflow sweep confirmed the current-head vpsAdmin CI run
  completed successfully.
- Cleanup:
  - Removed
    `worktrees/2026-06-25-vpsadmin-backup-rotation/merge/vpsadmin`.
  - Removed `worktrees/2026-06-25-vpsadmin-backup-rotation/vpsadmin`.
  - Removed
    `worktrees/2026-06-25-vpsadmin-backup-rotation/vpsadmin-pre-fix`.
  - Removed the now-empty
    `worktrees/2026-06-25-vpsadmin-backup-rotation/` directory.
  - Verified no vpsAdmin worktrees remain for this initiative.
