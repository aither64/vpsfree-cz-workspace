---
lifecycle: active
---
# 2026-06-08-vpsadmin-storage-redesign

## Repositories

- `vpsadmin`
  - Worktree:
    `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-06-08-vpsadmin-storage-redesign/vpsadmin`
  - Branch: `2026-06-08-vpsadmin-storage-redesign`
  - Base fetched from `origin/master`, current checkout `b46d38616`.

## Status

- Added a read-only topology report script as the first diagnostic step before
  proposing or implementing data-model changes.
- Added a read-only DB-wide topology scan script so production does not require
  manually collecting every dataset one by one.
- Extended the report script with batch mode, so it can consume scan output and
  write one detailed JSON report per candidate dataset.
- User confirmed the first practical step should be looking at inconsistent
  production state before deciding whether data-model changes are needed.
- User constraints: do not use `zfs destroy -R`; production captures are
  point-in-time and may be stale by deployment because snapshots are created
  daily; all redesign/mutation paths must use the existing lock system; any
  updated data model must be reviewed before implementation; snapshot
  downloads are part of the concurrency/compatibility surface.

## Commands run

- `bin/dev-session current`
- `git -C repos/vpsadmin.git remote -v`
- `git -C repos/vpsadmin.git symbolic-ref refs/remotes/origin/HEAD`
- `git -C repos/vpsadmin.git fetch origin --prune`
- `git -C repos/vpsadmin.git worktree add -b 2026-06-08-vpsadmin-storage-redesign ... origin/master`
- Read repository `AGENTS.md`.
- Searched and read storage models, transaction chains, node-side ZFS
  commands, API resource definitions, web UI snapshot actions, and existing
  storage topology tests.
- `nix develop .#api -c bundle exec rspec api/spec/models/...`
  - Failed before examples because the API dev shell runs from `api/` and the
    paths were doubled as `api/api/spec/...`.
- `nix develop .#api -c bundle exec rspec spec/models/transaction_chains/dataset/rotate_spec.rb spec/models/transaction_chains/dataset/rollback_spec.rb spec/models/transaction_chains/snapshot_in_pool/destroy_spec.rb spec/api/resources/dataset_snapshot_spec.rb`
- Added `api/bin/storage-topology-report`.
- Added `api/bin/storage-topology-scan`.
- `nix develop .#api -c bundle exec rubocop bin/storage-topology-report`
- `nix develop .#api -c ruby -c bin/storage-topology-report`
- `nix develop .#api -c ruby bin/storage-topology-report --help`
- `nix develop .#api -c bundle exec ruby - <<'RUBY' ...`
  - Created committed temporary test records, invoked
    `bin/storage-topology-report` through a separate DB connection with
    `--skip-zfs`, parsed the JSON, and asserted selected dataset/DIP/snapshot
    rows plus the `snapshot_downloads` section and skipped-ZFS marker.
- `nix develop .#api -c bundle exec ruby - <<'RUBY' ...`
  - Created a parent dataset and child dataset, invoked
    `bin/storage-topology-report --scope subtree --skip-zfs`, parsed JSON, and
    asserted both datasets, both DIPs, both snapshots, `snapshot_downloads`,
    and skipped-ZFS marker were present.
- `nix develop .#api -c ruby -c bin/storage-topology-scan`
- `nix develop .#api -c ruby bin/storage-topology-scan --help`
- `nix develop .#api -c bundle exec rubocop bin/storage-topology-scan bin/storage-topology-report`
- `nix develop .#api -c bundle exec ruby - <<'RUBY' ...`
  - Created a backup DIP with an old snapshot and intentionally stale
    `reference_count`, ran `storage-topology-scan --pool-role backup`, asserted
    the dataset was ranked as a candidate with
    `reference_count_over_expected` and `old_blocked_snapshots`, then fed the
    scan JSON into `storage-topology-report --dataset-ids-file ... --output-dir
    ... --skip-zfs` and asserted the detailed report and manifest were written.

## Results

- Fetch advanced `origin/master` from `a5b59432d` to `b46d38616`.
- Worktree creation completed, but the checkout hook reported missing
  `overcommit` gem. This matters before any commit.
- Current schema stores logical snapshots globally, per-pool snapshot presence,
  backup dataset trees/branches, branch entries, and a single dependency edge
  from branch entry to parent branch entry.
- `reference_count` is maintained by snapshot clones and selected branch-entry
  rewrites. Rotation skips snapshots with `reference_count > 0`, but ZFS
  destroy safety ultimately depends on actual `origin`/`clones`.
- Existing tests already include topology fixture capture/replay and pending
  contracts for repeated rollback branching and complex rotation where DB leaf
  candidates can diverge from ZFS leaves.
- API snapshot delete still rejects any dataset with backups; web UI shows a
  delete icon for all snapshots and relies on API rejection after confirmation.
- Selected API storage snapshot specs passed: 39 examples, 0 failures,
  1 pending. The pending example is the known branched rotation case where all
  eight fixture snapshots remain because dependency metadata is incomplete.
- `api/bin/storage-topology-report` is read-only and can report by
  `--dataset-id`, `--dip-id`, or `--dataset-ids-file`, with
  `--scope dataset|subtree`.
- `api/bin/storage-topology-scan` is read-only and scans all selected
  dataset-in-pools, defaulting to candidate-only output. It can filter by
  `--node`, `--pool-role`, repeated `--pool-id`, repeated `--dataset-id`, and
  age threshold `--old-days`.
- The report includes selected `datasets`, `dataset_in_pools`, `snapshots`,
  `snapshot_in_pools`, `dataset_trees`, `branches`,
  `snapshot_in_pool_in_branches`, `snapshot_in_pool_clones`,
  `snapshot_downloads`, mounts, exports, export hosts/mounts, resource locks,
  locked transaction chains, transactions, confirmations, and live ZFS
  `origin`/`clones` metadata unless `--skip-zfs` is used.
- RuboCop passed for the two diagnostic scripts: 2 files inspected, no
  offenses.
- Syntax checks passed for both diagnostic scripts: `Syntax OK`.
- Help output lists DB connection options, selection options, `--scope`,
  `--skip-zfs`, `--include-transaction-payloads`, metadata fields, and
  `--output`.
- Local smoke tests passed against isolated temporary MariaDB test databases,
  including nested dataset `--scope subtree` selection and end-to-end
  scan-to-batch-report flow.
- The API spec run created ignored bundle artifacts in `api/.gems/` and
  `api/Gemfile.lock`.

## Open questions

- What production DB/ZFS samples are available from `backuper2.prg`, and can
  they include all backup DIPs for one dataset plus live ZFS
  `origin`/`clones`?
- Which inconsistent dataset should be captured first, and should capture be
  scoped to one dataset tree or include all backup pools and primary pools for
  that logical dataset?

## Cleanup

- Worktree should be removed after the design/implementation initiative is
  merged or abandoned.

## Archival request, 2026-10-06

The workspace operator requested archival of sessions dated August 2026 or
older, retaining recorded work and branches. This checkpoint commits the
existing plan and active state before the ordinary archive transition.
