# 2026-08-23-vpsadmin-ci-failure

## Repositories

- `vpsadmin`
  - failed revision: `b12f41859a9ae198224cd6ca63eddbcdd0371db8`
  - target branch: `master`
  - feature branch: `2026-08-23-vpsadmin-ci-failure`
  - worktree: `worktrees/2026-08-23-vpsadmin-ci-failure/vpsadmin`
  - base revision after rebase:
    `6610c6789c3d567ba0c67fdbf8392904b9f266ba`
  - implementation commit:
    `a7a1dfc9b06131bcacf22adfc4e361c9742ea517`
- `vpsadminos`
  - vpsAdmin input revision: `67fcc17372d175b036706a1459a8b471bfc225e0`
  - base revision: `80a0017d7b35cdfd4d11311876f487d2d56e3e3d`
  - target branch: `staging`
  - feature branch: `2026-08-23-vpsadmin-ci-failure`
  - worktree: `worktrees/2026-08-23-vpsadmin-ci-failure/vpsadminos`
  - implementation commit after rebase:
    `8e44a5124439b1f3048ffc56b1717614a5360358`

## Status

Rollout in progress. vpsAdminOS `staging` contains the Linux 6.12 containment
at `8e44a5124` and both feature and target CI are green. vpsAdmin pins that
revision on feature head `a7a1dfc9b`; local focused tests pass and feature CI
is running.

## Commands run

- Queried GitHub Actions run `32628417831` and job `97167303577` metadata with
  `gh api`.
- Read the failed job log with `gh run view --job ... --log-failed`.
- Downloaded artifact `vpsadmin-test-logs-32628417831` and inspected
  `test.log` plus the failing test's `test-result.txt`, `test-runner.log`, and
  guest console/lifecycle logs.
- Inspected workspace notes about the earlier matching kernel Oops and the
  later execmem root-cause analysis.
- Inspected vpsAdmin's `flake.lock` at the failed SHA and verified vpsAdminOS
  commit ancestry.
- Queried kernel.org release metadata and compared upstream Linux commit
  `1871d548fc4feb007644efb6d669c93a4e191254` with Linux 6.18.46 and the
  current `linux-6.18.y` source.
- Verified the active development session with `bin/dev-session current` and
  `VPSFREE_DEV_SESSION_SLUG`.
- Fetched vpsAdminOS and created the feature branch/worktree from current
  `origin/staging` at `80a0017d7`.
- Formatted `tests/configs/nixos/base.nix` with `nixfmt` in the repository's
  development shell.
- Built `.#tests.x86_64-linux."driver/nixos"` and inspected the generated
  driver JSON at
  `/nix/store/jqzkd0v82pqvam1x4khdkh0n6pbb901f-os-test-driver-nixos.json`.
  The Linux 6.12.104 kernel was fetched from `cache.nixos.org`; no kernel was
  compiled locally.
- Ran the complete Overcommit pre-commit suite with
  `nix develop --command overcommit --run`; Nixfmt and RuboCop passed.
- Committed the vpsAdminOS change as `7dc777a5d`,
  `tests: use Linux 6.12 for NixOS VMs`. The commit hook reran Nixfmt and
  passed; commit-message hooks passed with non-fatal 72-column warnings while
  every line remains within the workspace's required 80 columns.
- Ran `./test-runner.sh test -f --jobs 1 driver/nixos`; the single test passed
  in 124.54 seconds. Test-runner Ruby packages were rebuilt from the changed
  repository source, but the Linux kernel was not compiled.
- Refetched `origin/staging`; it remained at `80a0017d7`, with the feature
  branch one commit ahead and no divergence.
- Pushed vpsAdminOS branch `2026-08-23-vpsadmin-ci-failure` at exact head
  `7dc777a5ddd543e54bb61abc58f9c8b2fe293188`.
- Feature GitHub Actions CI run: `32668034165`, initially queued on the generic
  self-hosted runner with zero executed steps. The available token cannot list
  repository self-hosted runner status (`403 Resource not accessible by
  personal access token`), so the run status itself is being monitored.
- Feature GitHub Actions CI run `32668034165` completed successfully on exact
  head `7dc777a5ddd543e54bb61abc58f9c8b2fe293188`. The OS build, full 76-test CI
  selection, and AMD and Intel livepatch jobs all passed. In particular,
  `zfs/block-cloning-corruption` passed in 115.43 seconds.
- Started a second, workflow-equivalent local CI selection with
  `./test-runner.sh test --test-config tests/test-configs/ci.nix -f --jobs auto
  -t ci`. It fetched the Linux 6.12 kernel from the binary cache and did not
  compile a kernel. Resource sharing limited the run mostly to one high-memory
  VM at a time.
- The extra local run encountered one unrelated evaluation-only failure in
  `zfs/block-cloning-corruption`, before a VM was started. Its immutable source
  snapshot contains the linked worktree's `.git` file; vpsAdminOS revision
  discovery accepts a `.git` directory or `.git-revision`, so channel source
  generation tried to coerce a null revision. A normal CI checkout has a
  `.git` directory and the exact feature CI ran this test successfully. The
  reusable caveat is recorded in
  `notes/vpsadminos/2026-08-24-test-runner-linked-worktree-revision.md`.
- Fetched `origin/staging` after feature CI. It had advanced independently to
  `93014dd1f` with an automated Nixpkgs lock update, so rebased the one
  functional commit without conflict. Its new SHA is `8e44a5124`.
- On the rebased head, ran the full Overcommit suite successfully, rebuilt and
  inspected `.#tests.x86_64-linux."driver/nixos"`, and reran
  `./test-runner.sh test -f --jobs 1 driver/nixos`. The test passed in 80.32
  seconds. The generated JSON still uses cached Linux 6.12.104 and omits both
  udev parameters; no kernel was compiled.
- Force-pushed the rebased feature head with an exact `--force-with-lease`.
  The superseded run was already complete, so no queued or running workflow
  required cancellation. Exact-head CI run `32695473960` passed its OS build,
  full 76-test selection, and AMD and Intel livepatch jobs.
- Stopped the redundant local CI selection after 48 of 76 test groups had
  completed: 47 succeeded and only the documented linked-worktree evaluation
  failure was unexpected. The exact pre-rebase feature CI had already passed
  all 76 groups, and the rebased focused test passed, so continuing the
  resource-constrained duplicate would not add useful evidence.
- Fetched vpsAdmin `origin/master` and created its isolated feature branch and
  worktree at current master `66f58d761`. The vpsAdminOS input remains
  unchanged until the verified vpsAdminOS commit reaches `staging`.
- Created a fresh vpsAdminOS integration worktree at `93014dd1f`, merged the
  feature branch with `git merge --ff-only`, rebuilt the generated NixOS
  driver JSON, and verified cached Linux 6.12.104 plus the absence of both
  udev parameters. Pushed exact head `8e44a5124` to `staging`.
- vpsAdminOS target CI run `32699480491` passed the OS build, full 76-test
  selection, and AMD and Intel livepatch jobs on exact `staging` head
  `8e44a5124439b1f3048ffc56b1717614a5360358`.
- Ran `tools/update_vpsadminos_flake.sh` in `nix develop .#vpsadmin`. It
  resolved vpsAdminOS from `67fcc1737` to merged `8e44a5124` and changed only
  `flake.lock`. Its automatic commit was correctly stopped by the mandatory
  `VpsadminApiI18n` hook because the API component bundle was not installed.
- Followed `notes/vpsadmin/2026-08-22-overcommit-api-bundle.md`: prepared
  `api/.gems` with `nix develop .#api --command true`, then ran the complete
  root-shell Overcommit suite. Nixfmt, MigrationSpecs, both i18n hooks,
  PhpCsFixer, and RuboCop passed. Committed the generated update as
  `ed806873d`, `flake: vpsadminos 67fcc1737 -> 8e44a5124`; the commit hooks and
  commit-message hooks passed.
- Built vpsAdmin `.#tests.x86_64-linux."services-up"` and inspected the
  resulting JSON. Its services VM uses Linux 6.12.104, keeps `console=ttyS0`,
  and contains neither udev parameter. The resolved flake metadata names exact
  vpsAdminOS revision `8e44a5124` and expected NAR hash. No kernel was
  compiled.
- On `ed806873d`, `services-up` passed all 27 examples in 422.99 seconds and
  `vps/deploy-public-key-and-user-data` passed its end-to-end example in
  824.59 seconds.
- vpsAdmin `master` advanced independently to `6610c6789` with an automated
  packaged `curses` update, so rebased the lock commit to `a7a1dfc9b`. Rebuilt
  the services JSON; only the new dependency and affected service closures
  were rebuilt, while Linux 6.12 remained cached. The rebased JSON again uses
  Linux 6.12.104 and omits both udev parameters.
- On rebased head `a7a1dfc9b`, `services-up` passed all 27 examples in 470.93
  seconds and `vps/deploy-public-key-and-user-data` passed its end-to-end
  example in 852.68 seconds.
- Pushed vpsAdmin feature branch `2026-08-23-vpsadmin-ci-failure` at exact head
  `a7a1dfc9b06131bcacf22adfc4e361c9742ea517`. Feature workflow runs include
  CI `32704895810`, i18n health `32704895590`, WebUI PHPUnit `32704895736`,
  Client Specs `32704895803`, and libnodectld Specs `32704895708`.

## Results

- The job ran on `gh-runner3.int.vpsadminos.org` against vpsAdmin
  `b12f41859a9ae198224cd6ca63eddbcdd0371db8`. Setup, test selection, preview,
  state preparation, artifact upload, log summary, and cleanup succeeded.
- The suite completed 118 tests: 117 succeeded and only
  `vps/deploy-public-key-and-user-data` failed unexpectedly.
- That test did not reach its feature assertions. At 7.35 guest-seconds, its
  NixOS `services` VM running Linux 6.18.43 Oopsed in `(udev-worker)` with a
  supervisor write-protection page fault at `native_set_pte`.
- The decisive call trace is `native_set_pte` ->
  `__change_page_attr_set_clr` -> `set_memory_nx` ->
  `__execmem_cache_free` -> `execmem_free` -> `load_module`. The shared test
  framework detected it as `OsVm::KernelFailure` while waiting for the API and
  terminated the VMs.
- This matches
  `notes/vpsadmin/2026-08-19-linux-execmem-ci-kernel-page-fault.md`.
  Linux 6.18's execmem cache population and following allocation are not
  atomic. Another module loader can consume the newly populated area before
  the first loader retries, leaving error cleanup to restore/free executable
  memory with inconsistent permissions.
- Upstream Linux commit `1871d548fc4feb007644efb6d669c93a4e191254`,
  `mm/execmem: make the populate and alloc atomic`, fixes the matching race by
  holding the cache mutex across both operations.
- The failed vpsAdmin revision pins vpsAdminOS `67fcc1737`, which contains
  `651aa87bc tests: serialize NixOS udev workers`. The test-only
  `rd.udev.children_max=1` and `udev.children_max=1` workaround was therefore
  present. This recurrence proves that serializing udev workers is not a
  complete workaround for all module-loader concurrency.
- Linux 6.18.46 was released on 2026-08-23. Its release commit is also the
  current `linux-6.18.y` head at the time of this check, and its
  `mm/execmem.c` retains the old separate `execmem_cache_populate()` followed
  by `__execmem_cache_alloc()` flow. The upstream fix is not backported there;
  updating from 6.18.43 to 6.18.46 alone is insufficient.
- Linux 6.12.105 does not contain the execmem cache involved in this race:
  `execmem_alloc()` allocates directly and `execmem_free()` calls `vfree()`.
  Pinning generated NixOS test guests to the 6.12 package line is therefore a
  credible temporary containment. At the Nixpkgs revision used by this failed
  run, `linuxPackages_6_12.kernel.version` evaluates to 6.12.102 while the
  default evaluates to 6.18.43.
- The generated NixOS test base currently leaves `boot.kernelPackages` at the
  Nixpkgs default. Selecting `pkgs.linuxPackages_6_12` there would affect
  generated NixOS guests, not vpsAdminOS machines. The main tradeoff is losing
  integration coverage against NixOS 26.05's default 6.18 kernel until the
  upstream fix is backported. It should use the public NixOS binary cache and
  avoid the custom-kernel build required by a locally patched 6.18 kernel.
- The durable remedy remains backporting upstream commit `1871d548fc4f` into
  the NixOS test kernel and requesting its inclusion in Linux 6.18.y. Keep the
  kernel-failure detector enabled because it correctly classified this run.
- The generated `driver/nixos` machine uses
  `/nix/store/c9ahm2mgq3fwz3f3g8xk78rs8gljmbwy-linux-6.12.104/bzImage`.
  Its effective kernel arguments include `console=ttyS0` and contain neither
  `rd.udev.children_max=1` nor `udev.children_max=1`.
- The exact feature-branch CI completed green after the initial runner queue:
  <https://github.com/vpsfreecz/vpsadminos/actions/runs/32668034165>.
- The rebased exact-head feature and target CI runs are green:
  <https://github.com/vpsfreecz/vpsadminos/actions/runs/32695473960> and
  <https://github.com/vpsfreecz/vpsadminos/actions/runs/32699480491>.
- vpsAdmin now pins exact merged vpsAdminOS revision `8e44a5124`; both focused
  tests pass before and after the independent `master` dependency update.

## Decisions

- Pin generated NixOS test VMs with
  `lib.mkDefault pkgs.linuxPackages_6_12`, leaving deliberate per-test
  overrides possible.
- Remove both `rd.udev.children_max=1` and `udev.children_max=1`; their presence
  did not prevent module-loader concurrency outside udev.
- Keep `console=ttyS0` and the test runner's kernel-failure detector.
- Remove the 6.12 pin only after the upstream fix is in `linux-6.18.y`, the
  pinned Nixpkgs packages the fixed release, and parallel boot/module-load
  stress is free of both known `__execmem_cache_free` and `__text_poke`
  failures.

## Mandatory change review

- One fresh standalone reviewer inspected vpsAdminOS range
  `80a0017d7..7dc777a5d`, workspace commit `f8b7f2c`, the initiative records,
  and the quick-verification evidence before long VM testing.
- Result: `READY_WITH_NOTES`.
- Blocking findings: none. Important findings: none. Advisory findings: none.
- The reviewer confirmed that every direct-boot `spin = "nixos"` guest imports
  the changed base configuration, vpsAdminOS guests use a separate path,
  `lib.mkDefault` permits deliberate per-test overrides, and no copy of either
  udev serialization parameter remains.
- Residual validation matches the plan: run `driver/nixos`, inspect the later
  vpsAdmin services machine against the exact pin, run the two focused
  downstream tests, require green feature/target CI, and stop if a kernel
  compilation starts.

## Cleanup

- The vpsAdminOS feature worktree and branch are active and will be retained
  until both repositories are merged and verified.
- The downloaded artifact and temporary Linux repository were used only under
  `/tmp` and removed after the investigation.
