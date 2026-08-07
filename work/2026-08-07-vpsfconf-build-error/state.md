# 2026-08-07-vpsfconf-build-error

## Repositories

- `vpsfree-cz-configuration`: branch
  `2026-08-07-vpsfconf-build-error`; worktree
  `worktrees/2026-08-07-vpsfconf-build-error/vpsfree-cz-configuration`, based
  on `origin/master` at `3c3de36a`.
- `vpsadminos`: branch `2026-08-07-vpsfconf-build-error`; worktree
  `worktrees/2026-08-07-vpsfconf-build-error/vpsadminos`, based on
  `origin/staging` at `d1d73edcd`.

## Status

Complete. The fix is fast-forwarded to vpsAdminOS `staging`, and the generated
three-channel pin is fast-forwarded to configuration `master`. All local,
review, and feature-branch CI gates passed. Worktrees and transient artifacts
are removed. No deployment was performed.

## Commands run

- `bin/dev-session current` with matching `VPSFREE_DEV_SESSION_SLUG`
- Inspected workspace status, tracking files, bare-repository remotes, refs, and
  symbolic heads.
- Fetched `vpsfree-cz-configuration` and `vpsadminos` upstream refs over SSH.
- Created the isolated configuration worktree from `origin/master` at
  `3c3de36a` and read its repository-local `AGENTS.md`.
- Ran `nix develop --no-write-lock-file -c confctl ls -t build`.
- Reproduced with
  `nix develop --no-write-lock-file -c confctl build -y -t build --show-trace`.
- Compared configuration input commits `0984078f`, `7de52d4e`, and their
  parents, including locked vpsAdminOS revisions.
- Inspected the focused vpsAdminOS diff for `b0c2ea255` and the unchanged
  container-image repository NixOS module.
- Evaluated the generated build host toplevel derivation while overriding only
  `vpsadminosOsStaging` to `008aa4605`, `b0c2ea255`, `13d07aa36`, and
  `14843dbb`; all commands used `--no-write-lock-file`.
- Walked configuration lock history and tested vpsAdminOS ancestry around the
  June 12/13 input update.
- Removed Nix development-shell artifacts `.bin/` and `.bundle/`, verified the
  project worktree was clean, and removed it with `git worktree remove`.
- Re-fetched both upstreams before implementation. vpsAdminOS `origin/staging`
  advanced from `c140a894` to `d1d73edcd` only through an unrelated livepatch
  commit; the broken module and overlay interface are unchanged.
- Created fresh isolated worktrees for both affected repositories and attached
  them to the initiative branches.
- Changed the container-image repository module to use the source flake's
  pre-applied `osctl` and `ruby` overlays, added a focused module evaluation,
  and wired it into the early vpsAdminOS CI job.
- Installed and signed vpsAdminOS Overcommit hooks, ran the full suite, and ran
  the focused evaluation with
  `nix eval --impure --raw --file tests/nixos-container-image-repository-eval.nix`.
- The first vpsAdminOS commit attempt ran the installed hook from the ambient
  shell and could not find `nixfmt`; repeated the commit from `nix develop`
  without bypassing hooks.
- Committed vpsAdminOS as `8d5fe0058`, pushed the feature branch, and cancelled
  its initial long CI run `31190238532` until mandatory review is complete.
- Installed and signed configuration Overcommit hooks and ran
  `confctl inputs channel set --commit '{production,staging,os-staging}'
  vpsadminos 8d5fe0058f5f4db3840c7d8043c7aba3b88ccca4`.
- Preserved the generated configuration commit message unchanged, committed as
  `496ec3c2`, and pushed the feature branch.
- Ran `confctl inputs channel ls` and the full configuration Overcommit suite.
- Ran the required fresh-context mandatory change review. It reported no
  blocking or advisory findings and one important deployment-documentation
  finding about the included livepatch v3 update; updated `plan.md` with its
  mixed-version and rollback contract without changing the generated pin.
- Restarted vpsAdminOS CI run `31190238532` after review; its new focused module
  evaluation step passed before the full toplevel build.
- Ran `confctl build -y -t build --show-trace`; evaluation passed the former
  recursion point and reached the expected missing local SystemRescue ISO.
- Ran `confctl build -y cz.vpsfree/containers/int.blog`; it built the complete
  representative `os-staging` NixOS generation successfully.
- Monitored vpsAdminOS CI run `31190238532` to completion. The build, binary
  cache, and profile job passed in 36m31s; the full test-suite job passed in
  49m7s; the complete workflow concluded successfully.
- Re-fetched both defaults before integration. vpsAdminOS `origin/staging`
  remained `d1d73edcd`; configuration `origin/master` advanced to `c3e7fbf3`
  through unrelated ssh-exporter and syslog-exporter dependency commits.
- Rebased the generated configuration pin cleanly onto `c3e7fbf3`, preserving
  its generated message and exact three-lock-node diff. The rebased head is
  `1d6ef004fdb4cf37f8454eb18de45fdcd464bb64`.
- Re-ran configuration Overcommit, channel listing, the representative
  `int.blog` build, and the build-host evaluation against the refreshed base,
  then force-pushed the feature branch with an exact force-with-lease guard.
- Created fresh integration worktrees, fast-forwarded vpsAdminOS `staging` to
  `8d5fe0058`, re-ran the focused evaluation, and pushed `staging` over SSH.
- Fast-forwarded configuration `master` to rebased pin `1d6ef004`, verified all
  three channel roles from the integration worktree, and pushed `master` over
  SSH.
- Confirmed configuration has no push workflow for the integrated head. New
  vpsAdminOS default-branch CI run `31198648330` is in progress.
- Removed both feature worktrees and both fresh integration worktrees with
  their generated development-shell, RuboCop, confctl log, and test artifacts.
  Retained the feature branches locally and remotely as required.
- Stopped monitoring default-branch CI at the user's request after its cached
  build/cache/profile job passed in 15 seconds; the full test-suite job was
  still running without a failure state.

## Results

- The active session is verified as `2026-08-07-vpsfconf-build-error`.
- The canonical repositories use the required SSH remotes.
- `-t build` selects only `cz.vpsfree/machines/build`.
- The build machine enables channels `nixos-stable` and `os-staging`, then
  imports vpsAdminOS module
  `os/modules/services/misc/build-vpsadminos-container-image-repository/nixos.nix`.
- That module installs `(import ../../../../overlays/osctl.nix)` directly in
  `nixpkgs.overlays`.
- vpsAdminOS commit `b0c2ea255` changed `os/overlays/osctl.nix` from a normal
  `self: super: { ... }` overlay to a function that first requires the source
  inputs `{ netlinkrb, ruby-lxc }`, followed by `self: super: { ... }`.
- Other vpsAdminOS callers were updated to apply those inputs, but the
  container-image repository NixOS module was not. Nixpkgs consequently calls
  the unapplied function as an overlay, passes its recursive final package set
  as the source-input argument, and recurses while constructing `pkgs`.
- The Bluetooth module is incidental: its `pkgs.formats.ini` option is simply
  where module option checking first forces the broken package set.
- Current `c140a894`, older descendant `008aa4605`, and the introducing commit
  `b0c2ea255` reproduce the same recursion.
- The parent `13d07aa36` and last pre-update configuration pin `14843dbb`
  evaluate past the recursion and reach the expected local-only missing ISO
  error for `/srv/iso-images/systemrescue-11.01-amd64.iso`.
- Configuration commit `a10a50a7` first advanced `vpsadminosOsStaging` from
  `14843dbb` to descendant `0236bcd3` on 2026-06-13, introducing the broken
  overlay call into the build host. The 2026-08-07 `reline` update in
  `c140a894` is unrelated.
- The focused vpsAdminOS evaluation now succeeds and returns the derivation
  `/nix/store/2iggsc0b3sccvmg5mxdb8dxr3im1jyc9-osvm-26.05.0.drv`.
- `git diff --check`, Nixfmt, and the full vpsAdminOS Overcommit suite passed.
- Configuration roles `vpsadminosProduction`, `vpsadminosStaging`, and
  `vpsadminosOsStaging` all resolve to `8d5fe005`; configuration Nixfmt,
  RuboCop, and the full Overcommit suite passed.
- vpsAdminOS feature head: `8d5fe0058f5f4db3840c7d8043c7aba3b88ccca4`.
- Configuration feature head:
  `1d6ef004fdb4cf37f8454eb18de45fdcd464bb64`.
- Mandatory review confirmed that the implementation, focused evaluation,
  commit boundaries, generated pin, and exact lock-node scope are sound. The
  review's livepatch rollback documentation finding was resolved in `plan.md`.
- The build-host evaluation no longer contains an infinite-recursion error. It
  now terminates only because
  `/srv/iso-images/systemrescue-11.01-amd64.iso` is absent locally, matching the
  pre-existing development-environment limitation.
- Representative consumer `cz.vpsfree/containers/int.blog` built generation
  `2026-08-07--17-09-29` successfully.
- GitHub CI run `31190238532` completed successfully, including the full
  vpsAdminOS closure build, cache/profile publication, and complete test suite.
- After rebasing onto the refreshed configuration base, all three roles still
  resolve to `8d5fe005`; Overcommit passed, `int.blog` built generation
  `2026-08-07--18-36-31`, and the build-host evaluation again reached only the
  known missing-SystemRescue-ISO boundary with no infinite recursion.
- Remote vpsAdminOS `staging` now resolves to `8d5fe0058`; remote configuration
  `master` now resolves to `1d6ef004`.
- Default-branch vpsAdminOS CI run `31198648330` passed its complete cached
  build/cache/profile job. Further workflow monitoring was explicitly waived
  by the user while the test-suite job remained in progress.

## Open questions

- None. The user selected all three vpsAdminOS channel pins, default-branch
  fast-forward integration, and no deployment.

## Cleanup

Complete. The two feature and two integration worktrees were removed, including
generated development-shell and test artifacts. Feature branches remain both
locally and remotely. Default-branch CI was left running at the user's request.
