# 2026-08-23-vpsadmin-ci-failure

## Repositories

- `vpsadmin`
  - failed revision: `b12f41859a9ae198224cd6ca63eddbcdd0371db8`
  - target branch: `master`
  - feature branch: `2026-08-23-vpsadmin-ci-failure` (not yet created)
  - worktree: `worktrees/2026-08-23-vpsadmin-ci-failure/vpsadmin` (not yet
    created)
- `vpsadminos`
  - vpsAdmin input revision: `67fcc17372d175b036706a1459a8b471bfc225e0`
  - base revision: `80a0017d7b35cdfd4d11311876f487d2d56e3e3d`
  - target branch: `staging`
  - feature branch: `2026-08-23-vpsadmin-ci-failure`
  - worktree: `worktrees/2026-08-23-vpsadmin-ci-failure/vpsadminos`
  - implementation commit: `7dc777a5ddd543e54bb61abc58f9c8b2fe293188`

## Status

Implementation in progress. The investigation found a recurrence of the known
Linux 6.18 execmem cache race during parallel module loading, not a failure of
the `vps/deploy-public-key-and-user-data` behavior or of the vpsAdmin change
under test. The selected containment is to use Linux 6.12 in generated NixOS
test VMs and remove the insufficient udev-worker serialization parameters.

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
- This matches `notes/vpsadmin/2026-08-19-linux-execmem-ci-kernel-page-fault.md`.
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

## Cleanup

- The vpsAdminOS feature worktree and branch are active and will be retained
  until both repositories are merged and verified.
- The downloaded artifact and temporary Linux repository were used only under
  `/tmp` and removed after the investigation.
