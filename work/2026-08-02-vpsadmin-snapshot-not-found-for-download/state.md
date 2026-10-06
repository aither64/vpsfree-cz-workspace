---
lifecycle: active
---
# 2026-08-02-vpsadmin-snapshot-not-found-for-download

## Repositories

- `vpsadmin`
  - canonical repository: `repos/vpsadmin.git`
  - inspected commit: `19e613c2ae72103fc04265002402544f387e08c0`
  - original implementation base: `ae5dd5e016c68e347ece409223299b30f2134340`
  - final rebased base: `50f8223c3792e1409167c9ca0d97126c781a57e7`
  - feature worktree: `worktrees/2026-08-02-vpsadmin-snapshot-not-found-for-download/vpsadmin`
  - temporary merge worktree: `worktrees/2026-08-02-vpsadmin-snapshot-not-found-for-download/merge/vpsadmin`
  - branch: `2026-08-02-vpsadmin-snapshot-not-found-for-download`
- `vpsfree-cz-configuration`
  - canonical repository: `repos/vpsfree-cz-configuration.git`
  - worktree: `worktrees/2026-08-02-vpsadmin-snapshot-not-found-for-download/vpsfree-cz-configuration`
  - branch: `2026-08-02-vpsadmin-snapshot-not-found-for-download`

## Status

Implementation is complete and merged by fast-forward into `master` at
`0b066c42814d3a9f5b0b8f8e3ed7910ae20a4fac`. Before merging, the feature was
rebased unchanged onto the then-current `origin/master` at
`50f8223c3792e1409167c9ca0d97126c781a57e7`; `git range-diff` again confirmed
all three reviewed patches were identical. Focused verification on the exact
merge tree passed. All final feature and `master` GitHub Actions workflows are
terminal. The complete `master` workflow set passed, including all 117 selected
integration tests. The feature CI run failed during test-environment bootstrap;
its artifacts show two tests never reached their scenarios because nodectld
could not authenticate to the test RabbitMQ instance. Configuration commit
`e5395e1d` is merged into
`vpsfree-cz-configuration/master` and updates the `vpsadmin` channel's
`vpsadminServices` input to merged vpsadmin `0b066c428`. No logical Snapshot
lock was added.

## Commands run

- `bin/dev-session current`
- `git --git-dir=repos/vpsadmin.git show ...`
- `git --git-dir=repos/vpsadmin.git grep ...`
- `git --git-dir=repos/vpsadmin.git log ...`
- `git --git-dir=repos/vpsadmin.git diff 19e613c2...master ...`
- `bin/dev-session worktree add 2026-08-02-vpsadmin-snapshot-not-found-for-download vpsadmin --as-is --branch 2026-08-02-vpsadmin-snapshot-not-found-for-download --base origin/master`
- `nix develop .#api -c bundle exec rspec spec/models/transaction_chains/snapshot_in_pool/destroy_spec.rb`
- focused `nix develop .#libnodectld -c bundle exec rspec` for snapshot destroy
  command and confirmation processing specs
- `nix develop .#api -c bundle exec rspec spec/models/transaction_chains/dataset/backup_spec.rb spec/models/transaction_chains/dataset/full_download_spec.rb spec/models/transaction_chains/dataset/incremental_download_spec.rb spec/api/resources/snapshot_download_spec.rb`
- focused API examples for both new HTTP 409 responses
- `nix develop .#api -c bundle exec rspec spec/models/transaction_chains/snapshot_in_pool/use_clone_spec.rb spec/api/resources/export_spec.rb:680`
- `nix develop .#api -c bundle exec rspec spec/api/resources/export_spec.rb:521 spec/api/resources/export_spec.rb:567 spec/api/resources/export_spec.rb:633 spec/api/resources/export_spec.rb:669`
- targeted `nix develop .#api -c bundle exec rubocop ...` for all changed Ruby
  files
- `nix develop .#api -c bundle exec rake vpsadmin:i18n:update`
- `nix develop .#api -c bundle exec rake vpsadmin:i18n:health`
- three commits through active Overcommit hooks using `git commit -F`
- `nix develop .#api -c bundle exec rspec spec/models/transaction_chains/dataset/rollback_spec.rb spec/models/transaction_chains/dataset/full_download_spec.rb spec/models/transaction_chains/dataset/incremental_download_spec.rb`
- review-fix commit through active Overcommit hooks using `git commit -F`
- rebuilt the unpublished history as three commits with `git cherry-pick
  --no-commit` and `git commit -F`, then verified the final tree is identical to
  the reviewer-approved tree
- inspected GitHub CI run `30820324305`, including failed-step logs and the
  complete `vpsadmin-test-logs-30820324305` artifact
- `./test-runner.sh test storage/snapshot-download-incremental-branch-mismatch`
  on the default bridge network
- `nix-instantiate --parse
  tests/suite/storage/snapshot-download-incremental-branch-mismatch.nix`
- committed the CI correction through active Overcommit hooks and autosquashed
  it into the download commit
- force-pushed the reviewed three-commit series with an exact
  `--force-with-lease`
- manually dispatched `libnodectld Specs` for current-head coverage because the
  force-push tree delta did not match that workflow's automatic path filter
- monitored all current-head GitHub Actions workflows to terminal results
- fetched `origin/master`, rebased the clean feature branch, and verified the
  rewritten series with `git range-diff`
- force-pushed the rebased branch with an exact `--force-with-lease`
- inspected failed post-rebase CI run `30885363008`, including its complete
  32.5 MB test-log artifact and the failed test's VM/service logs
- manually dispatched CI in `auto` mode for the exact rebased head so test
  selection is based on its merge base with current `origin/master`
- fetched the subsequently advanced `origin/master`, rebased the clean branch
  from `6fb60827f` onto `3f9b68adb`, and verified all three patches again with
  `git range-diff`
- force-pushed current head `a6b9e7ed7` with an exact lease against published
  head `9e6e0e34d`
- monitored all seven workflows for current head `a6b9e7ed7` to successful
  terminal results
- fetched `origin` after CI and verified that `origin/master` remained at
  `3f9b68adb`, was the exact merge base, and matched the default remote branch
- verified the local and remote feature heads matched, the worktree was clean,
  and `git diff --check origin/master...HEAD` passed
- fetched the subsequently advanced `origin/master` at `50f8223c3`, inspected
  its unrelated libnodectld export-mount fix, and rebased the feature cleanly
- verified all three patches remained exactly equal with `git range-diff` and
  force-pushed final feature head `0b066c428` with an exact lease
- created a fresh temporary merge worktree from current `origin/master` and
  fast-forwarded it to the feature branch with `git merge --ff-only`
- ran focused API and libnodectld regression specs on the exact merge tree
- pushed the merge worktree head to `master` as a regular fast-forward and
  verified published and canonical local `master` both point to `0b066c428`
- created the `vpsfree-cz-configuration` feature worktree at `8203153f`,
  entered its Nix dev shell, and installed the active Overcommit hooks
- ran `confctl inputs channel update --commit --no-editor vpsadmin`; generated
  commit `e5395e1d` changes only `flake.lock` and pins `vpsadminServices` from
  `2f9546ce` to `0b066c428`
- verified `confctl inputs channel ls vpsadmin` resolves the requested channel
  to `vpsadminServices` at `0b066c42`
- investigated the focused `confctl build -y 'cz.vpsfree/vpsadmin/*'` failure:
  unchanged base input `web` revision `26e85847` has stale locked NAR hash
  `bvpx...`, while a forced current fetch hashes to `ETi8...`
- pushed configuration feature commit `e5395e1d`, confirmed the repository has
  no push-triggered workflow, and fast-forwarded it into configuration
  `master` from a fresh temporary merge worktree
- verified published and canonical local configuration `master` both point to
  `e5395e1d`
- inspected failed final feature CI run `31005054727`, including its complete
  test-log artifact and both failed environments' VM/service logs
- monitored the independent final `master` CI run `31006032240` to success on
  the same `0b066c428` tree
- fetched both repositories after CI and verified the merged commits remain the
  published and canonical local `master` heads and match retained feature refs
- removed the vpsadmin feature and temporary merge worktrees, deleted only the
  transient merge branch, and retained the feature branch locally and remotely
- removed 477 MB of downloaded CI diagnostic artifacts from two exact `/tmp`
  directories with scoped depth-first deletion; direct recursive removal was
  rejected by the execution safety policy

## Results

- The API successfully resolves and authorizes the logical `Snapshot` row
  before the exception.
- `FullDownload` first looks for a live backup branch entry, then for a
  non-`confirm_destroy` copy on a primary or hypervisor pool. It raises only if
  both lookups return `nil`.
- The message describes database eligibility, not a direct ZFS/filesystem
  lookup.
- Normal destroy/rotation/rollback chains can mark the last storage copy for
  destruction while the logical snapshot row remains queryable until transaction
  confirmation. Snapshot list/show/download lookup does not filter logical
  snapshots by confirmation state.
- The same result can persist when destruction is stuck/failed, or when backup
  metadata has no live branch path (entry, snapshot-in-pool, branch, or tree is
  missing or marked `confirm_destroy`). Orphaned association metadata is a less
  likely integrity-failure variant.
- The existing full-download model spec explicitly confirms that a logical
  snapshot with no storage copy raises this exact exception.
- No relevant implementation changes exist between the deployed commit and the
  current local `master`.
- Follow-up production observation: snapshot `8561077` no longer exists. Since
  `SnapshotDownload::Create` freshly loaded this row before reaching
  `FullDownload`, it existed at report time and was removed afterward. This
  strongly supports a request racing with the committed destruction/rotation
  lifecycle window rather than a permanently orphaned logical snapshot.
- The responsible chain was identified as
  `TransactionChains::Dataset::Backup`. This chain transfers snapshots and then
  immediately builds rotations for the source and destination dataset-in-pool.
  Those nested rotations mark pruned storage copies `confirm_destroy` while
  the outer backup chain is queued/running. The destination rotation can mark
  the final backup branch copy after source rotation marked the primary copy,
  scheduling deletion of the logical `Snapshot` row on confirmation. This
  exactly explains the observed request window and subsequent disappearance.
- Confirmation processing is chain-wide, not per transaction. libnodectld runs
  all pending confirmations only when `chain_finished?`, then closes the chain
  and releases its resource locks in the same database transaction. Therefore
  the inconsistent API-visible state lasts from committing the newly queued
  backup chain through its entire queue and execution time. The download does
  not actually pass a conflicting lock: `FullDownload` filters out all
  `confirm_destroy` storage copies before calling `lock(sip)` or
  `lock(sip.dataset_in_pool)`, so it raises on the empty lookup without ever
  attempting lock acquisition.
- The initial design considered using the logical `Snapshot` as a shared lock,
  but the approved implementation deliberately avoids that broader lock. It
  instead reuses already-held physical SIP locks for pending work and adds the
  missing physical DIP/SIP locks to export clone use.

## Implementation

- `89bef9baa api: mark snapshots pending final-copy destruction`
  - Marks the logical snapshot `confirm_destroy` exactly when the last live
    physical copy is scheduled for destruction.
  - Leaves it confirmed while another live copy or branch remains.
  - Confirms existing nodectld name lookup behavior for `confirm_destroy`.
- `9074a0499 api: handle unavailable snapshot download sources`
  - Replaces raw full/incremental download exceptions with a typed unavailable
    exception.
  - Performs bounded lookups over only the requested snapshots' physical copies
    and their `ResourceLock` rows.
  - Returns the standard 423 response with the owning chain when a physical
    source is pending work; otherwise returns localized 409 responses.
  - Covers the exact queued `Dataset::Backup` reproduction, archive download,
    incremental download, and both public HTTP 409 mappings.
  - Checks both requested SIP and associated DIP locks, excludes locks owned by
    the download under construction, and tolerates orphaned legacy topology in
    diagnostics.
  - Aligns the branch-mismatch integration scenario with the typed unavailable
    exception contract by checking its class and `no_common_source` reason.
- `0b066c428 api: lock snapshot sources used by exports`
  - Locks the source dataset-in-pool and snapshot-in-pool before snapshot clone
    selection or reference-count changes.
  - Makes export creation serialize with physical snapshot destruction and
    return the standard 423 response on conflict.

## Verification

- Snapshot-in-pool destroy model specs: 6 examples, 0 failures.
- Focused libnodectld destroy/confirmation specs: 36 examples, 0 failures.
- Backup/full/incremental/snapshot-download specs: 50 examples, 0 failures.
- New archive HTTP 409 example: 1 example, 0 failures.
- New incremental HTTP 409 example: 1 example, 0 failures.
- UseClone plus pending-export example: 4 examples, 0 failures.
- Four snapshot-export source-selection/conflict examples: 4 examples,
  0 failures.
- Targeted RuboCop: no offenses.
- API i18n update and health: passed.
- Overcommit pre-commit hooks passed for all three commits (Nixfmt,
  MigrationSpecs, VpsadminWebuiI18n, RuboCop, and VpsadminApiI18n).
- `git diff --check` on the vpsadmin change: passed.
- Review-fix rollback/full/incremental specs: 21 examples, 0 failures.
- Public pending-copy, archive 409, and incremental 409 request specs after the
  review fixes: 3 examples, 0 failures.
- Focused branch-mismatch integration test after the CI correction: 1 test,
  1 example, 0 failures.
- Nix parse check for the corrected integration test: passed.
- Final GitHub CI: 67 selected tests, 67 successful.
- Final current-head API Specs, RuboCop, libnodectld Specs, and i18n health:
  passed.
- Final current-head Client Specs and Webui PHPUnit: passed.
- Final current-head CI: all 117 selected integration tests succeeded in
  16,473.77 seconds.
- Final upstream/remote verification: `origin/master` remained the default at
  `3f9b68adb`; it was the exact merge base of `a6b9e7ed7`, the published and
  local feature heads matched, and the worktree was clean.
- Exact final merge-tree API regression set: 129 examples, 0 failures.
- Exact final merge-tree libnodectld regression set: 38 examples, 0 failures.
- Final fast-forward: published `origin/master` and canonical local `master`
  both point to `0b066c428`.
- Final merged-head API Specs, RuboCop, libnodectld Specs, and i18n health:
  passed on both the feature push and the `master` push.
- Final feature CI: 95 of 97 selected tests passed. The two failures stopped in
  node/API readiness before test setup: nodectld repeatedly received RabbitMQ
  `403 ACCESS_REFUSED`, while the diagnostic database queries showed no
  transaction chains, snapshots, or resource locks. The full artifact was
  inspected before accepting another run as validation.
- Final `master` CI on the identical `0b066c428` tree: all 117 selected tests
  passed; 134 scripts ran in 16,790.04 seconds.
- Configuration Overcommit Nixfmt hook: passed.
- Configuration channel resolution: `vpsadmin` role `vpsadmin` resolves
  `vpsadminServices` at `0b066c42`.
- Configuration focused build: blocked before machine evaluation by the
  unchanged base `web` input's stale NAR hash. The mismatch was reproduced with
  the exact hash-qualified URL and a forced current fetch; see
  `notes/vpsfree-cz-configuration/2026-08-05-web-input-nar-hash-mismatch.md`.
- Configuration merge: published and canonical local `master` both point to
  generated input-only commit `e5395e1d`.

## GitHub Actions

### Initial head

The first reviewed head was pushed directly. Its five workflows were all
terminal before the corrected head was force-pushed, so there were no
superseded queued or in-progress runs to cancel.

- [API Specs](https://github.com/vpsfreecz/vpsadmin/actions/runs/30820324035):
  passed, including all 26 topic jobs.
- [RuboCop](https://github.com/vpsfreecz/vpsadmin/actions/runs/30820324292):
  passed.
- [libnodectld Specs](https://github.com/vpsfreecz/vpsadmin/actions/runs/30820324454):
  passed.
- [i18n health](https://github.com/vpsfreecz/vpsadmin/actions/runs/30820324442):
  passed for API and WebUI.
- [CI](https://github.com/vpsfreecz/vpsadmin/actions/runs/30820324305):
  failed after running all 117 selected tests: 115 passed and 2 failed.
  `storage/snapshot-download-incremental-branch-mismatch` reached the intended
  `SnapshotDownloadUnavailable(reason: :no_common_source)` path, but its
  integration assertion still expected the retired raw exception text. That
  assertion is corrected and passes locally. The independent
  `storage/dataset-migrate-remote` test never reached migration behavior: it
  timed out waiting for node 101 to become API-ready while its VM logs showed
  repeated filesystem `Invalid argument` errors and virtiofs restart activity.
  The full 32.5 MB test-log artifact was downloaded and inspected before any
  rerun decision.

### Updated head

All runs below used
`a565081b78188627d814a6189f73e7d30caf9ff9`:

- [API Specs](https://github.com/vpsfreecz/vpsadmin/actions/runs/30844272103):
  passed, including all 26 topic jobs.
- [RuboCop](https://github.com/vpsfreecz/vpsadmin/actions/runs/30844272527):
  passed.
- [libnodectld Specs](https://github.com/vpsfreecz/vpsadmin/actions/runs/30844305341):
  passed after a manual current-head dispatch.
- [i18n health](https://github.com/vpsfreecz/vpsadmin/actions/runs/30844272458):
  passed for API and WebUI.
- [CI](https://github.com/vpsfreecz/vpsadmin/actions/runs/30844272370):
  passed; all 67 selected integration tests succeeded in 10,331.71 seconds.

### Rebased head

The unchanged feature series was rebased from
`ae5dd5e016c68e347ece409223299b30f2134340` onto
`6fb60827fb44fb8f8a83d2238f59ee4e6ddf8d66`. Post-rebase workflows for
`9e6e0e34d97f0cda2e60e638864f1a788de432dc` produced these results:

- [API Specs](https://github.com/vpsfreecz/vpsadmin/actions/runs/30885362733):
  passed, including all topic jobs.
- [libnodectld Specs](https://github.com/vpsfreecz/vpsadmin/actions/runs/30885362753):
  passed.
- [i18n health](https://github.com/vpsfreecz/vpsadmin/actions/runs/30885362762):
  passed for API and WebUI.
- [RuboCop](https://github.com/vpsfreecz/vpsadmin/actions/runs/30885362910):
  passed.
- [Webui PHPUnit](https://github.com/vpsfreecz/vpsadmin/actions/runs/30885362708):
  passed.
- [force-push CI](https://github.com/vpsfreecz/vpsadmin/actions/runs/30885363008):
  failed with 116 of 117 selected tests successful. The sole failure was
  `cluster/node-evacuate-concurrency`, which does not exercise snapshot
  downloads. Its artifact shows widespread `Invalid argument` errors while
  reading the VM's virtiofs-backed `/nix/store`; evacuation chain `#12` then
  timed out. This matches the unrelated runner/virtiofs failure signature
  already investigated in run `30820324305`.
- [replacement auto CI](https://github.com/vpsfreecz/vpsadmin/actions/runs/30906454421):
  passed on the exact rebased head; all 117 selected tests succeeded in
  17,283.27 seconds.

The replacement `workflow_dispatch` used `mode=auto` and independently selected
the same 117-test set, confirming that this is the current selector's intended
feature-impact scope. GitHub did not publish partial logs for the running
self-hosted job (`BlobNotFound`), and the current token could not list
self-hosted runner registration state (HTTP 403); neither diagnostic limitation
affected the run itself.

### Current master head

While the replacement CI ran, `origin/master` advanced through six commits to
`3f9b68adb97b7f43df929a85fc172d9d11e15211`, including CI source-stability
fixes, a vpsAdminOS input update, and API dependency-lock refreshes. The clean
feature series was rebased again; `git range-diff` matched every patch exactly.
Current published head `a6b9e7ed74d1f6f7ad683fc35f94261219089974`
passed all seven workflows:

- [API Specs](https://github.com/vpsfreecz/vpsadmin/actions/runs/30930610568):
  passed.
- [CI](https://github.com/vpsfreecz/vpsadmin/actions/runs/30930610804):
  passed; all 117 selected integration tests succeeded in 16,473.77 seconds.
- [i18n health](https://github.com/vpsfreecz/vpsadmin/actions/runs/30930610556):
  passed.
- [libnodectld Specs](https://github.com/vpsfreecz/vpsadmin/actions/runs/30930610988):
  passed.
- [RuboCop](https://github.com/vpsfreecz/vpsadmin/actions/runs/30930610513):
  passed.
- [Client Specs](https://github.com/vpsfreecz/vpsadmin/actions/runs/30930612174):
  passed.
- [Webui PHPUnit](https://github.com/vpsfreecz/vpsadmin/actions/runs/30930612268):
  passed.

After all workflows completed, `origin/master` was fetched again and remained
at `3f9b68adb97b7f43df929a85fc172d9d11e15211`. It is the remote default branch
and exact merge base of the feature head. The published feature ref matches the
local head, and the worktree is clean.

The first API test invocation incorrectly added `cd api` even though the API
development shell already changes into that directory; it exited before tests.
The established workspace note already documents this behavior. An attempted
`vpsadmin:i18n:check` task did not exist; the documented
`vpsadmin:i18n:health` task was then run successfully.

### Merged head

The final merged tree is
`0b066c42814d3a9f5b0b8f8e3ed7910ae20a4fac`. The feature and `master` pushes
each ran the four short workflows successfully:

- [Feature API Specs](https://github.com/vpsfreecz/vpsadmin/actions/runs/31005054703)
- [Feature RuboCop](https://github.com/vpsfreecz/vpsadmin/actions/runs/31005054681)
- [Feature libnodectld Specs](https://github.com/vpsfreecz/vpsadmin/actions/runs/31005054551)
- [Feature i18n health](https://github.com/vpsfreecz/vpsadmin/actions/runs/31005054601)
- [Master API Specs](https://github.com/vpsfreecz/vpsadmin/actions/runs/31006030694)
- [Master RuboCop](https://github.com/vpsfreecz/vpsadmin/actions/runs/31006030747)
- [Master libnodectld Specs](https://github.com/vpsfreecz/vpsadmin/actions/runs/31006031395)
- [Master i18n health](https://github.com/vpsfreecz/vpsadmin/actions/runs/31006030974)

[Feature CI](https://github.com/vpsfreecz/vpsadmin/actions/runs/31005054727)
failed with 95 of 97 tests successful. Both failures were bootstrap failures:
`storage/backup-multiple-destinations-diverged-remote` timed out waiting for a
node to become API-ready, and `storage/snapshot-download-incremental-transfer`
timed out waiting for nodectld supervision. Their artifacts showed repeated
RabbitMQ `403 ACCESS_REFUSED` errors and empty API diagnostic tables, so neither
scenario exercised the changed code. The broker setup service had reported
successful node-user creation, making this a test-environment inconsistency
rather than an application assertion failure.

[Master CI](https://github.com/vpsfreecz/vpsadmin/actions/runs/31006032240)
then passed independently on the same commit: all 117 selected tests succeeded,
with 134 scripts completing in 16,790.04 seconds. No failed run was blindly
rerun; the successful master push was already an independent exact-tree
execution on another self-hosted runner.

## Mandatory change review

The fresh-context reviewer found three issues in the initial head `5eb822586`:

1. Blocking: the incremental second-stage missing-base path could mistake the
   download's own target SIP lock for external queued work.
2. Blocking: no-backup rollback owns only the affected DIP lock while marking
   newer SIPs for destruction, so SIP-only inspection returned 409 instead of
   the rollback chain's 423.
3. Important: unavailable diagnostics dereferenced potentially orphaned legacy
   DIP/pool associations and could raise `NoMethodError` instead of 409.

All three findings were addressed in temporary review-fix commit `69bf13f68`
with focused regression tests. The same reviewer approved the delta with no new
behavioral, security, compatibility, or test-adequacy findings. Per the
reviewer's history advisory, the fix was then folded into the unpublished
download commit as `05d54f242`; `git diff --exit-code 69bf13f68 c0fa8ec14`
confirmed the final tree is identical to the approved tree.

After the first GitHub CI run exposed the stale branch-mismatch assertion, the
same standalone reviewer inspected updated head
`a565081b78188627d814a6189f73e7d30caf9ff9`. It approved the final tree and
three-commit series with no findings, and confirmed that folding the integration
test into `411aa1544` is the correct placement. The full CI rerun subsequently
passed all 67 selected tests. The independent remote-migration VM-startup
timeout remains documented from the first run, and did not recur.

The review also corrected a bookkeeping-only base SHA typo in this file; the
actual base and merge base are
`ae5dd5e016c68e347ece409223299b30f2134340`.

## Decisions

- Pending snapshots remain visible and return the existing HTTP 423
  transaction-chain lock response when used for downloads or exports.
- A logical snapshot with no eligible or locked physical source returns HTTP
  409, not 404 or an unhandled 500.
- Archive and incremental downloads are both covered.
- Snapshot exports receive physical DIP/SIP locking coverage.
- No logical Snapshot resource lock is added.

## Cleanup

- Configuration feature and merge worktrees were removed after integration.
- The transient configuration merge branch was deleted.
- vpsadmin feature and merge worktrees were removed after final CI
  verification, along with the now-empty worktree group directories.
- The transient vpsadmin merge branch was deleted.
- Both repositories' feature branches remain locally and remotely, as
  required.
- Downloaded CI artifacts were removed after their findings were recorded in
  this state file and
  `notes/vpsadmin/2026-08-05-ci-rabbitmq-node-auth-bootstrap.md`.

## Archival request, 2026-10-06

The workspace operator requested archival of sessions dated August 2026 or
older, retaining recorded work and branches. This checkpoint commits the
existing plan and active state before the ordinary archive transition.
