# 2026-09-02-vpsadminos-chattr-test

## Repositories

- `vpsadminos`
  - branch: `2026-09-02-vpsadminos-chattr-test`
  - worktree removed after integration; branch retained
  - base: fetched `origin/staging` at
    `f38b0018ee80bb2c36fb7940b4bcfd185f8e7194`
  - head: `ee6d2f99d3c2ac51d4cbea54e1922808f345299d`
- `zfs`
  - branch: `2026-09-02-vpsadminos-chattr-test`
  - worktree removed after integration; branch retained
  - base: exact ZFS revision pinned by vpsAdminOS staging,
    `6f5f54c3bfd68c1e52b0b6f454ee9679aaa9e83d`
  - head: `9f479d6551bebde664b71b6d7553e8d23c162c4c`
  - remote feature branch is pushed

## Status

- The ZFS feature branch was recreated from the current vpsAdminOS pin instead
  of a nominal default branch.
- The minimal mount-idmap-aware `FS_IOC_SETFLAGS` fix is committed and pushed.
- The vpsAdminOS pin update, two-map-mode regression test, and full-suite ext4
  harness fix are committed as separate changes and pushed.
- Two mandatory independent reviews passed with no findings on the final
  ZFS/pin/regression-test series and the follow-up test-harness fix. Focused,
  selected upstream, and aggregate local integration tests all pass.
- vpsAdminOS was fast-forwarded into `staging` and pushed at
  `ee6d2f99d3c2ac51d4cbea54e1922808f345299d`. The post-merge OS build, both
  livepatch jobs, and the changed 6.12.95 kernel build pass. Full suites and the
  unchanged 6.12.48 kernel build are waiting for runners.

## Changes

- ZFS now passes the effective mount idmap through the existing
  `FS_IOC_SETFLAGS` inode-owner check and setattr operation. No other attribute
  path is changed.
- The existing first-level user namespace capability policy remains intact.
- The active vpsAdminOS 6.12.95 kernel pins ZFS commit `9f479d655` with source
  hash `sha256-arX7aWuTpmJ74YYtRgxh2MsA4ixC656GsDLcVWHhAZE=`.
- `misc-attrs` creates explicit `native` and `zfs` Alpine containers. It checks
  `lsattr`, immutable write/append/unlink denial, append-only append success and
  truncate/unlink denial, and normal behavior after each flag is cleared.

## Commands and results

- Reproduced the original failure in a native-map container and confirmed the
  ZFS-map control works with the same capabilities.
- Inspected BusyBox 1.37.0 and e2fsprogs 1.47.4 implementations. BusyBox logs
  the failed ioctl but returns status 0; e2fsprogs propagates failure.
- Repointed the clean ZFS worktree to the exact current pin. An initial broad
  historical callback backport was rejected as unnecessary and rewritten to a
  14-line diff in `zpl_file.c` limited to `FS_IOC_SETFLAGS`.
- `scripts/spdxcheck.pl`: passed.
- `scripts/cstyle.pl -cpP` on changed C/header files: passed.
- `scripts/commitcheck.sh HEAD^..HEAD`: passed after wrapping the unpublished
  commit message to 72 columns.
- `make checkstyle`: could not run before configure because a pristine checkout
  has no generated Makefile. Equivalent source checks were run directly; see
  `notes/zfs/2026-09-02-checkstyle-pristine-checkout.md`.
- Force-pushed the rewritten, still-unmerged ZFS branch through the SSH remote
  using an explicit lease for the replaced commit.
- `nix store prefetch-file --unpack` for the pushed ZFS archive produced the
  recorded source hash.
- Installed vpsAdminOS Overcommit hooks through `nix develop`.
- Both vpsAdminOS commits ran the installed Nixfmt pre-commit hook successfully.
  The first ambient commit attempt was correctly blocked because `nixfmt` was
  absent; the commits were then made inside `nix develop` without bypassing
  hooks.
- `./test-runner.sh ls 'kernel/vpsadminos#misc-attrs'`: passed and returned the
  expected test name. No kernel build was started.
- `nix develop --command overcommit --run`: all final-tree Nixfmt and RuboCop
  checks passed.
- Repeated `./test-runner.sh ls 'kernel/vpsadminos#misc-attrs'` after rewriting
  the ZFS pin: passed. Only test-runner closures were built; no kernel build was
  started.
- ZFS current-head GitHub Actions were inspected after the force-push. The
  zloop runner compiled the changed `zpl_file.c` on Linux 6.17, then failed in
  unchanged `zfs_vnops_os.c` because that fork still accesses removed
  `struct page.index`. CodeQL compiled the changed file on Linux 6.8, then
  failed at modpost on the fork's existing GPL-only `posix_acl_clone` and
  `init_user_ns` references. The checkstyle workflow reached its generic build
  and failed on those same existing GPL-only symbols. All zfs-qemu matrix jobs
  timed out in their 20-minute `Setup QEMU` step before test preparation, then
  lacked `env.txt` for follow-up steps. The exact base commit also has all four
  workflows recorded as failed; its logs have expired. See
  `notes/zfs/2026-09-02-ci-runner-kernel-incompatibilities.md`.
- Mandatory change review by standalone agent
  `mandatory_chattr_review_20260902`: no Blocking, Important, or Advisory
  findings. It confirmed the focused ZFS scope, unchanged namespace gate,
  Linux 6.12 API choice, exact pin, commit split, and semantic test coverage.
  Residual gaps are compilation against the pinned kernel and the VM semantic
  run. Nested-userns denial is statically preserved but not directly added to
  the vpsAdminOS test.
- vpsAdminOS CI run `33641348420` failed before compilation because GitHub
  returned HTTP 429 for the unchanged pinned Linux archive `a2384967...` on all
  four Nix fetch retries. The ZFS/kernel derivations therefore never started.
  The failed attempt was inspected before requesting a rerun; see
  `notes/vpsadminos/2026-09-02-ci-linux-archive-rate-limit.md`.
- CI attempt 2 failed on the same unchanged Linux archive with four more HTTP
  429 responses, again before compilation. No further immediate rerun was
  requested. Because this initiative intentionally changes built-in ZFS and
  the responsible runner has not published the kernel closure, a local focused
  kernel/test build is justified by the workspace policy.
- `./test-runner.sh test 'kernel/vpsadminos#misc-attrs'` was attempted locally.
  It failed after 49 seconds while evaluating/building dependencies because the
  same unchanged Linux archive returned HTTP 429 on every retry. The kernel and
  changed ZFS code were not compiled, the VM did not start, and no test
  assertion ran. The runner state is in
  `/tmp/os-test-runner/os-test-kernel__vpsadminos-f1b75a4a`.
- Populated the exact fixed-output Linux source path through the equivalent
  codeload endpoint with `nix store prefetch-file`. It produced the configured
  hash `sha256-QlwV4uFeX7ZbWHMuU14rFXswmpqpb1hdVmYUAGOWRh8=` and exact expected
  store path, so no source or pin was changed.
- Re-ran `./test-runner.sh test 'kernel/vpsadminos#misc-attrs'`. The intentional
  local kernel build compiled the changed ZFS code into Linux 6.12.95, rebuilt
  the cumulative livepatch, assembled both VM images, and booted successfully.
  All four examples passed: append-only and immutable attributes under both
  `zfs` and `native` ID mapping. The focused script passed in 402.05 seconds;
  the full build-and-test command exited 0 after 5870.64 seconds.
- The first selected OpenZFS positive test attempt built its external-ZFS
  kernel, livepatch, userspace test package, and VM image successfully, but the
  harness failed before invoking `chattr_001_pos.ksh`. Its ext4 work-image
  mount returned `unknown filesystem type 'ext4'`. The kernel config has
  `CONFIG_EXT4_FS=m`, while vpsAdminOS disables module autoloading; failure
  diagnostics show the resulting denied request as
  `kernel.modprobe: action=deny -q -- fs-ext4`. The full-suite test had no
  explicit ext4 module entry at the exact staging base. Added the minimal
  test-only `boot.kernelModules = [ "ext4" ];` fix before rerunning.
- Fresh mandatory review by standalone agent
  `mandatory_ext4_review_20260902`: no Blocking or Important findings. It
  confirmed that `ee6d2f99d` is the minimal correct fix for the observed
  modular-ext4/autoload-denial failure. Its tracking-only advisory to replace a
  stale status sentence was applied.
- Re-ran the selected upstream positive case with
  `VPSADMINOS_ZFS_FULL_TEST=tests/functional/chattr/chattr_001_pos.ksh
  ./test-runner.sh test 'zfs/full-suite'`. The setup, selected test, and cleanup
  all passed; the runner completed successfully in 570.63 seconds.
- Ran the selected upstream negative case with
  `VPSADMINOS_ZFS_FULL_TEST=tests/functional/chattr/chattr_002_neg.ksh
  ./test-runner.sh test 'zfs/full-suite'`. The setup, selected test, and cleanup
  all passed; the runner completed successfully in 499.23 seconds.
- `./test-runner.sh test 'kernel/vpsadminos'` exited successfully but selected
  zero scripts. Multi-script tests require a fragment selector; see
  `notes/vpsadminos/2026-09-02-test-runner-multiscript-selector.md`.
- `./test-runner.sh ls 'kernel/vpsadminos#*'` listed all 14 kernel scripts.
  `./test-runner.sh test 'kernel/vpsadminos#*'` then ran the actual aggregate:
  all 14 scripts, including all four `misc-attrs` examples, passed in 1994.55
  seconds.
- Current-head vpsAdminOS CI run `33661523571` for `ee6d2f99d3c2` passed its
  checkout and image-reuse checks and is building the toplevel closure. It has
  not reproduced the old HTTP 429 failure.
- Fetched `origin/staging` immediately before integration. It remained at the
  feature base `f38b0018e`, with the feature branch zero commits behind and
  three ahead, so no rebase was necessary.
- Created a fresh detached integration worktree from `origin/staging` and ran
  `git merge --ff-only 2026-09-02-vpsadminos-chattr-test`. The result advanced
  cleanly to the already-tested feature head `ee6d2f99d`.
- `nix develop --command overcommit --run` in the integration worktree passed
  both Nixfmt and RuboCop.
- Re-fetched `origin/staging`, verified it was still an ancestor of the tested
  head, and pushed `HEAD:staging` without force. The server-side `staging` ref
  was verified at `ee6d2f99d3c2ac51d4cbea54e1922808f345299d`.
- The staging push queued CI run `33670276663` and `Build all kernel versions`
  run `33670276671`, both for the merged commit.
- Feature-branch CI run `33661523571` built and published the exact merged OS
  closure successfully in 1h32m55s. Its AMD livepatch job passed; its Intel
  livepatch job is running and its full suite is queued.
- Post-merge staging CI run `33670276663` reused the published closure and
  passed its OS build plus both Intel and AMD livepatch lifecycle jobs. Its full
  test suite is queued.
- Post-merge `Build all kernel versions` run `33670276671` detected both
  supported kernels and passed the changed 6.12.95 build. The unchanged
  6.12.48 build is queued.

## Commits

- ZFS `9f479d655`: `linux: honor mount idmap in FS_IOC_SETFLAGS`
- vpsAdminOS `9ee2bf18e`: `os: update ZFS for idmapped file attributes`
- vpsAdminOS `a0f9fa6ee`: `tests/kernel: cover attributes with both map modes`
- vpsAdminOS `ee6d2f99d`: `tests/zfs: load ext4 for full-suite work image`

## Compatibility

- No persisted formats or external interfaces change.
- Mixed-version nodes and rolling deployment are safe.
- Rollback restores the native-map limitation but leaves attribute state
  readable and manageable by host root.
- The existing nested-user-namespace restriction is unchanged.

## Open questions

- None.

## Cleanup

- Debug containers were deleted and debug VMs stopped normally.
- Both project feature branches are retained locally and remotely.
- The clean temporary vpsAdminOS integration worktree was removed after the
  successful push.
- The clean vpsAdminOS and ZFS feature worktrees and their empty worktree group
  directory were removed after integration. Their transient test artifacts were
  removed with the worktrees.
