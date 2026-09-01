# 2026-08-31-vps-migrate-debug

## Repositories

- `vpsadmin`
  - branch: `2026-08-31-vps-migrate-debug`
  - worktree: removed after merge
  - base: `origin/master`
    `3ded1bb20e9eceab2e47152cc438aaebda98f767`
- `vpsfree-cz-configuration`
  - branch: `2026-08-31-vps-migrate-debug`
  - worktree: removed after merge
  - base: `origin/master`
    `6dbee52ed2173bda482796db5b33f70a5dcd035d`
- Top-level workspace: this plan and state only; unrelated shared changes are
  being left untouched.

## Status

The diagnostic logging commit identified a corrupt shared daily-backup
group-snapshot action as the migration failure. The code fix and generic data
repair are committed and pushed in vpsAdmin as `a597a93ff` and `dffd204ab`.
The user deployed that revision and successfully ran migration
`20260831220000`; the post-migration read-only SQL audits passed. The logging
follow-up is pushed as `7b455cad1`, and configuration commit `64cacb34` pins
that exact revision. It logs unexpected non-Show `RecordNotFound` exceptions
outside the test environment while suppressing expected Show misses and RSpec
noise. Mandatory review found no issue, and all workflows for the final
vpsAdmin feature head succeeded. Both feature heads were then fast-forwarded
into their remote `master` branches, with vpsAdmin at `7b455cad1` and
configuration at `64cacb34`. Master API Specs and the other short workflows
succeeded; at the user's direction, the repeated full aggregate CI run was
left running without waiting for it. All initiative worktrees and generated
hook caches were removed, while both local and remote feature branches were
preserved. No direct production database access was used by this development
session.

## Commands run

- Verified the active initiative with `bin/dev-session current` and the
  matching `VPSFREE_DEV_SESSION_SLUG`.
- Inspected shared workspace status and repository-local `AGENTS.md`.
- Fetched `origin` in `repos/vpsadmin.git` over its SSH remote.
- Searched central logs read-only over SSH at
  `log.int.prg.vpsfree.cz`, including WebUI, API, database, and node logs.
- Inspected the migration WebUI handler, API action exception mapping,
  transaction-chain construction, mount migration, and mount transaction
  parameter generation from `vpsadmin` `origin/master`.
- Tried unauthenticated `vpsfreectl` object access; API metadata was reachable,
  but VPS/node records correctly returned HTTP 401. No credentials were sought
  or changed.
- Fetched `origin` for both affected repositories over SSH.
- Created both initiative branches and worktrees from their current
  `origin/master` revisions.
- The configuration worktree checkout hook reported unavailable Bundler gems
  in the ambient shell after creating the worktree. The worktree and clean
  branch were verified. This known behavior is documented in
  `notes/vpsfree-cz-configuration/2026-06-10-worktree-overcommit-gems.md`; hook
  installation and Git operations will run inside `nix develop`.
- Installed and ran Overcommit from each repository's Nix development shell.
- Added class/message and full-backtrace stderr logging directly to the existing
  `ActiveRecord::RecordNotFound` response handler.
- The first focused-spec and RuboCop invocation incorrectly attempted to
  `cd api` after `nix develop .#api` had already selected that component
  directory; reran the commands from the shell's selected directory.
- `ruby tests/ci-selection-test.rb`: 16 runs, 55 assertions, all passed.
- `nix develop .#api -c bundle exec rubocop lib/vpsadmin/api.rb
  spec/api/resources/vps_write_spec.rb`: two files, no offenses.
- `nix develop .#api -c bundle exec rspec
  spec/api/resources/vps_write_spec.rb:1376`: one example, no failures.
- vpsAdmin commit:
  `262fe53944bf9850357824e97eb9fd7f43d37d88` (`api: log record lookup
  failures`). Pre-commit hooks passed; the branch was pushed to `origin`.
- Ran `nix develop -c confctl inputs channel set --commit vpsadmin vpsadmin
  262fe53944bf9850357824e97eb9fd7f43d37d88` before the user's latest message.
  It created local commit `6c703e680e77abf6124443e830f723afeb3e55a4`
  and passed pre-commit hooks. At that stage it was left unpushed because the
  user planned to pin the revision themselves; that decision was later
  superseded by the request to implement the complete plan.
- Reworked backup-preserving VPS replacement to move only the replaced
  `GroupSnapshot`, reuse or create the destination pool's shared action and
  task, and remove a source action only when all of its memberships move.
- Added data migration `20260831220000` and a matching migration spec. It
  derives expected memberships from existing `daily_backup` assignments,
  repairs missing, duplicate, and pool-mismatched memberships, creates only
  required per-pool actions/tasks, and contains no deployment record IDs.
- `nix develop .#api -c bundle exec rspec
  spec/migrations/20260831220000_reconcile_daily_backup_group_snapshots_spec.rb`:
  4 examples, 0 failures.
- `nix develop .#api -c bundle exec rspec
  spec/models/transaction_chains/vps/replace/os_spec.rb`: 14 examples,
  0 failures.
- Focused RuboCop: four touched Ruby files, no offenses. `git diff --check`,
  migration-spec coverage, and `ruby tests/ci-selection-test.rb` all passed;
  CI selection reported 16 runs and 55 assertions.
- The first repair commit attempt was intentionally stopped by Overcommit
  because it was invoked outside the full Nix shell and lacked RuboCop,
  gettext, and MariaDB. Re-running through `nix develop .#vpsadmin` passed all
  pre-commit hooks. Before review, split the unmerged repair into focused
  prevention and data-reconciliation commits; both hook runs passed. The final
  initially reviewed vpsAdmin commits were
  `cca8121ea39052ffa69e7e262ca1b98793ed2e2c`
  and `fd3e40053d8d1da71bb9cde1b9201a652e4187f5`; the feature branch was
  updated with `--force-with-lease` after confirming the expected remote tip.
- Ran `confctl inputs channel set --commit vpsadmin vpsadmin fd3e40053...`.
  To avoid multiple commits updating the same input, regenerated the update
  once from `origin/master` in a temporary detached worktree and moved the
  feature branch to its exact generated commit
  `37ec8a99447d03ebb61653be0159534892abe54d`.
  The final commit directly advances `vpsadminServices` from `661896d0` to
  `fd3e4005`; its hook passed and its generated message is unchanged. The
  temporary worktree and only its transient `.bin/`/`.bundle/` files were
  removed.
- One `confctl` attempt in the disposable pin-generation worktree used a
  mistyped nonexistent full commit hash and failed with GitHub HTTP 404 before
  changing `flake.lock`. It was rerun with the verified `git rev-parse HEAD`
  value above.
- Mandatory standalone review reported no Blocking findings and three
  Important issues: plans unavailable in the destination environment could
  retain a group membership, destination action creation was not serialized,
  and memberships without an assignment were not part of migration
  reconciliation.
- Addressed all three findings. Replacement now gates membership movement on
  the plan actually moving, locks the destination pool row before action
  lookup/creation, and has cross-environment regression coverage. The
  migration removes memberships outside the exact assignment set, handles
  zero assignments, cleans orphan actions/tasks, and validates exact-set
  equality. Focused suites then passed with 15 replacement examples and 5
  migration examples; RuboCop and CI-selection remained green.
- Rewrote and pushed the final reviewed vpsAdmin commits with
  `--force-with-lease`: `a597a93fff3c81a1ff5755d101a9167dc9d2aa05`
  and `dffd204ab966ab73ebb1a11850ddd1dfb19e805d`. All Overcommit hooks passed.
- The same standalone reviewer confirmed all three Important findings were
  resolved and found no new code issue. It noted existing cross-writer debt:
  dataset-plan registration does not participate in the new replacement pool
  lock protocol.
- Regenerated the single configuration commit from `origin/master` with
  `confctl`; final commit `d0d449912d22e1cf1c9c16298248c1c4ac48ac77`
  pins `vpsadminServices` directly from `661896d0` to `dffd204a` with the exact
  generated message. Nixfmt passed. The temporary generation worktree and its
  transient `.bin/`/`.bundle/` files were removed.
- Pushed the final `vpsfree-cz-configuration` feature branch and set its
  upstream to `origin/2026-08-31-vps-migrate-debug`.
- GitHub Actions for final vpsAdmin head `dffd204ab` reported successful API
  migration specs, RuboCop, i18n health, and libnodectld specs. The aggregate
  CI and topic-parallel API specs were still running at the last check.
- The user ran post-migration production audits. They returned no missing,
  duplicate, pool-mismatched, or unassigned `daily_backup` memberships and no
  incorrectly scheduled group-action tasks. The targeted check for
  `DatasetInPool` 72943 returned preserved `GroupSnapshot` 28354 attached to
  new `DatasetAction` 31771, with both the dataset and action on pool 41.
- Confirmed that API Specs (topic parallel) run `33435343964` completed
  successfully for the previously deployed vpsAdmin head `dffd204ab`.
- Added an `exec_exception` listener using HaveAPI's existing action context.
  It logs `RecordNotFound` class, message, and backtrace for non-Show actions
  outside `RACK_ENV=test`; the response mapper continues to return the same
  404 response without logging itself.
- Added integration coverage for production logging of a Migrate failure,
  test-environment suppression of the same failure, and production suppression
  of an expected Show miss.
- Focused logging specs: 3 examples, 0 failures.
- Complete VPS read/write resource specs: 136 examples, 0 failures.
- Focused RuboCop: three touched Ruby files, no offenses.
- `ruby tests/ci-selection-test.rb`: 16 runs, 55 assertions, all passed.
- Confirmed the vpsAdmin pre-commit hook is installed and executable.
- Committed the logging refinement as
  `7b455cad1c0c4f5f953ad385ee7e6635852a30b3` (`api: filter record lookup
  diagnostics`). All pre-commit hooks passed. Commit-message hooks passed with
  warnings for two body lines over their preferred 72 columns; every line is
  within the workspace's required 80-column limit.
- Mandatory standalone review of `dffd204ab..7b455cad1` found no Blocking,
  Important, or Advisory issues. The reviewer independently reran the three
  focused examples successfully. Residual risk is limited to representative
  coverage of one standard Show and one non-Show action; inheritance makes the
  filter apply to all `HaveAPI::Actions::Default::Show` subclasses.
- Refreshed both affected SSH remotes. Their current `origin/master` revisions
  remain ancestors of the published feature histories, so no rebase or history
  rewrite is required.
- Pushed vpsAdmin head `7b455cad1` normally. New current-head workflows were
  created, and superseded in-progress aggregate CI run `33435343956` for
  `dffd204ab` was canceled.
- Ran `confctl inputs channel set --commit vpsadmin vpsadmin 7b455cad...` in
  the configuration worktree. Generated commit
  `64cacb3407bb4a106516ae0769100620c263ce67` advances only
  `vpsadminServices` from `dffd204ab` to `7b455cad1`; Nixfmt and commit hooks
  passed, and the generated message was kept unchanged.
- Pushed configuration head `64cacb34` normally. The repository's only GitHub
  workflow is scheduled or manually dispatched, so this push correctly
  created no configuration workflow run.
- Verified all workflows for exact vpsAdmin head `7b455cad1` completed
  successfully: RuboCop `33441429808`, i18n health `33441429867`, API Specs
  (topic parallel) `33441429906`, and aggregate CI `33441429747`. The full
  aggregate suite ran for 5h 2m 38s; changing `api/lib/vpsadmin/api.rb`
  intentionally selected the full `tag=ci` integration suite.
- Final branch checks show both worktrees at their upstream revisions:
  vpsAdmin `7b455cad1` and configuration `64cacb34`. The vpsAdmin worktree is
  clean; the configuration worktree retains only the previously documented
  untracked `.bin/` and `.bundle/` hook directories.
- Fetched both default branches immediately before integration and confirmed
  each `origin/master` was an ancestor of its feature head. No rebase was
  needed.
- Created fresh detached integration worktrees from each `origin/master` and
  fast-forwarded them with `git merge --ff-only`. The first attempt used paths
  relative to the bare repositories and created clean temporary worktrees
  under their bare directories; they were removed before recreating the
  worktrees with absolute initiative paths. This known path-resolution trap is
  already documented in
  `notes/cross-project/2026-05-28-bare-head-worktree.md`.
- Revalidated the exact integration trees: `git diff --check` passed in both,
  vpsAdmin's CI selector test passed with 16 runs and 55 assertions, and
  configuration flake metadata evaluated without changing the lock file.
- Pushed vpsAdmin `master` to `7b455cad1`. The first configuration push was
  blocked by its pre-push hook because the ambient shell lacked pinned gems;
  rerunning inside `nix develop` executed the hook and pushed configuration
  `master` to `64cacb34`. Remote inspection confirmed that each default and
  preserved feature branch points to the same intended head.
- Master-triggered API Migration Specs, RuboCop, i18n health, libnodectld
  Specs, and API Specs (topic parallel), including topic coverage, all passed.
  Aggregate CI run `33475835792` was still running when the user explicitly
  chose not to wait for the duplicate full-suite validation; it was not
  cancelled.
- Removed both detached integration worktrees and both initiative feature
  worktrees. The only untracked content removed was generated `.bin/` and
  `.bundle/` hook caches in the two configuration worktrees. Removed the now
  empty `worktrees/2026-08-31-vps-migrate-debug` directory. Feature branch refs
  were retained locally and remotely.

## Results

- The diagnostic deployment captured the failing migration on api1 at
  2026-08-31 20:29:46 CEST in the central collector file
  `/var/log/remote/cz.vpsfree/vpsadmin/int.api1/log`.
- The exception is `ActiveRecord::RecordNotFound: Couldn't find
  GroupSnapshot`. It originates in
  `DatasetPlans::Executor#del_group_snapshot`, called while
  `Vps::Migrate::Base#migrate_dataset_plans` unregisters source dataset plans.
  The missing row is the per-dataset-in-pool membership in the shared
  group-snapshot action for that pool and dataset plan.
- The user's consistency query found only the root dataset: dataset 31284,
  source `DatasetInPool` 72943 on pool 41, daily-backup plan assignment 29705,
  and backup action 28393. The pool-matched group action and group-snapshot
  columns were null. This rules out the hidden-child explanation.
- A null pool-matched group action can coexist with working daily snapshots if
  the root's `GroupSnapshot` still points to a shared `DatasetAction` whose
  `pool_id` was changed to a different pool. `DatasetAction#do_group_snapshots`
  executes its memberships without consulting `pool_id`, while
  `del_group_snapshot` requires action pool and dataset pool to match.
- The VPS replacement backup-preservation code introduced in commit
  `f226cec88` provides a concrete corruption path: `reassign_group_snapshots`
  edits the pool ID of the shared group-snapshot action while moving one VPS.
  That action is shared by unrelated datasets on the source pool, so moving it
  breaks the pool/action invariant for every membership left behind. It can
  also destroy a destination pool's whole shared action. The user's follow-up
  query confirmed this exact shape: `GroupSnapshot` 28354 for
  `DatasetInPool` 72943 (pool 41) points to `DatasetAction` 26983, whose
  `pool_id` is 37. A global mismatch query found 136 pool-41 memberships under
  action 26983. VPS 27892 itself was never replaced: it was created normally
  on node1.pgnd and later swapped to node23. Because the action is shared, the
  corrupting replacement could have involved any other dataset on pool 41;
  VPS 27892 and the other 135 memberships are collateral damage. Its earlier
  swap is not required to invoke the faulty replacement code.
- Node23 has hypervisor pools 37 (`tank`) and 41 (`dozer`). Action 26983 being
  labelled pool 37 while retaining 136 pool-41 members explains both the
  absent pool-41 action and why snapshots/backups can still appear to run:
  group execution follows memberships without validating their pools. The
  mismatch audit does not detect destination-pool memberships that the faulty
  replacement code may have destroyed, so all active dataset plan assignments
  need an anti-join audit for a correctly pool-matched GroupSnapshot before
  repair.
- Production inspection for this follow-up is restricted to the central log
  machine at the user's direction. No further attempts to access API, database,
  or node systems will be made.
- Three migration submissions for VPS 27892 were observed on 2026-08-31:
  target node ID 126 at 18:41:29 and 19:05:15 CEST, then target node ID 122 at
  19:05:31 CEST. The first target correlates with `node25.prg`; it has accepted
  other migrations. Trying a second target produced the same immediate result,
  making a target-specific fault unlikely.
- No matching migration transaction, ZFS send/receive, queue reservation, or
  nodectld action appeared on `node23.prg` or any destination at those times.
  The failure therefore precedes transaction commit and dispatch.
- VPS 27892 is present and running on `node23.prg`. Routine backup activity for
  its root dataset succeeded on 2026-08-31, so the VPS and its primary source
  dataset are not missing.
- The WebUI logged missing PHP array keys during each form render/submission.
  The same warnings occur on many other migration submissions, and absent
  checkboxes are converted to false, so they are incidental rather than the
  cause of `object not found`.
- API and database journals contain no backtrace at the submission times. This
  is explained by `api/lib/vpsadmin/api.rb`: the global action exception handler
  catches `ActiveRecord::RecordNotFound`, returns the localized generic
  `object not found` response, and stops normal hook/error propagation.
- The same-location migration path eliminates the normal explicit checks for
  a missing target pool, incompatible cgroups, unavailable IP addresses,
  remote mounts, and supported snapshot clones: these return descriptive
  errors, not `object not found`.
- `TransactionChains::Vps::Migrate::MountMigrator#sort_mounts` loads every
  `Mount` row for the VPS without filtering `enabled`, `master_enabled`,
  `confirmed`, or `object_state`. In contrast, the later `Vps::Mounts` chain
  filters to enabled mounts not awaiting destruction. A disabled, deleted, or
  partially destroyed row can therefore break migration while remaining
  absent from the effective mount configuration.
- Two VPS-specific lookups in that path can raise the exact unhandled exception:
  a missing mirrored `SnapshotInPool` for a subtree snapshot mount in
  `migrate/mount_migrator.rb`, or a missing live
  `SnapshotInPoolInBranch` for a backup snapshot mount in
  `transactions/utils/mounts.rb`.
- The user subsequently ran `SELECT * FROM mounts WHERE vps_id = 27892` and
  received no rows. This rules out both mount-related lookup paths for this
  incident.
- The strongest remaining VPS-specific direct lookup is in
  `TransactionChains::NetworkInterface::DelRoute`: same-location migration
  requires the VPS owner's `EnvironmentUserConfig` for the source environment
  using `find_by!`. Missing legacy/inconsistent owner-environment state would
  produce the same response before transaction dispatch. Other remaining
  direct candidates are either records already proven to exist or global
  facilities such as mail-server selection.
- On 2026-08-08 an administrator created child dataset `27892/data` beneath
  dataset ID 31284 from the VPS page. This is relevant to the dataset subtree,
  but the logs do not prove that it has or had a mount, and it must not be
  removed speculatively.
- A global mail-server fallback can also raise `RecordNotFound`, but it is much
  less likely: it is not VPS-specific and would affect other mailed actions.
  All three observed attempts had `send_mail=1`.
- A MySQL reconnect message on `node23.prg` at 18:42:03 occurred after the
  immediate 18:41 failure and is not causal.

## Decisions

- Keep the implementation in vpsAdmin and use HaveAPI's existing
  `exec_exception` hook context; no HaveAPI change or release is required.
- Log class, message, and full backtrace for unexpected non-Show
  `ActiveRecord::RecordNotFound` exceptions outside `RACK_ENV=test`.
- Treat actions derived from `HaveAPI::Actions::Default::Show` as expected
  misses and suppress their diagnostics. Suppress all such operational
  diagnostics in tests so normal negative-path specs do not pollute stderr.
- Keep the existing localized 404 response mapping unchanged and do not log
  request payloads or other sensitive request context.
- Fast-forward both reviewed heads to their default branches when requested,
  pushing vpsAdmin before configuration so the pinned revision is present on
  the vpsAdmin default branch first. Preserve the feature branch refs.
- Treat the master API Specs workflow as the final merge gate at the user's
  direction. Leave the duplicate aggregate CI run active without waiting for
  or cancelling it.

## Cleanup

- No production runtime state was changed. Central systems were accessed
  read-only; repository default branches were updated as explicitly requested.
- Cleanup is complete: all four initiative and integration worktrees and their
  generated hook caches are removed. Both local and remote feature branches
  remain available.
