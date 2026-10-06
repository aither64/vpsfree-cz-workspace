---
lifecycle: active
---
# NixOS 26.05 Port State

## Status

vpsAdminOS port is buildable on `nixos-26.05` and has been fast-forward merged
into `origin/staging` at `0ac745ae3`. The feature branch had been rebased onto
`origin/staging` (`a0adfcf74`) before the merge. It targets `nixos-26.05`,
exposes 26.05 NixOS container templates, has regenerated vpsAdminOS packaged
gems with build id
`26.05.0.build20260604154538`, and has package fixes for Ruby 3.4/GCC
15/rsyslog 26.05 fallout. The CI follow-ups keep generated NixOS image builds
pinned to the tested source revision, enable explicit NFSv4 client support,
and update the Linux 6.12.91 ZFS pin to a branch commit that fixes the
fallocate/page-fault deadlock reproduced by GitHub Actions.

After review feedback, the vpsAdminOS feature branch history was rewritten to
split test changes, collapse related image-build fixes, keep generated gem
updates separate, and clarify the NFS kernel config commit. After rebasing
onto current staging, the old generated gem commit was dropped and a fresh gem
rebuild commit was created.

`vpsadmin` was added to the initiative after the initial plan because it will
be ported as part of the `vpsfree-cz-configuration` rollout. `ruby-lxc` was
also added because vpsAdminOS `osctld` needed a Ruby 3.4-compatible native gem
before vpsAdminOS packaged gems could be rebuilt on 26.05.

vpsAdmin is ported to the vpsAdminOS 26.05 input graph and pushed at
`4f413dfd0`. Its `vpsadminos` flake lock is pinned to the merged vpsAdminOS
26.05 revision `0ac745ae324072ec079620445ed4ea3531a7db96` while `flake.nix`
still points at `staging` for normal future updates. The generated
nodectl/nodectld/libnodectld package gems have been refreshed against
vpsAdminOS build id `26.05.0.build20260604154538`; the vpsAdmin package gem
build id is `4.1.0.build20260604181618`. vpsAdmin no longer packages or
enables cronie for the scheduler because the scheduler no longer relies on an
external crontab. The previous post-rebase `services-up` integration test
passed; after the latest upstream rebase, the regenerated nodectl packages
build successfully.

`vpsfree-cz-configuration` is ported to the 26.05 stable service graph and
pushed at `92982a0c`. The branch has been rebased onto current
`origin/master` (`1f1532af`), updates `nixos-stable` to `nixos-26.05`, updates
`home-manager` to `release-26.05`, pins `os-staging`/`staging` vpsAdminOS to
`0ac745ae3`, pins `vpsadminServices` to `4f413dfd0`, and pins `confctl` to
`eb26c228`. Representative vpsAdmin service and stable NixOS
container/machine builds pass. The old `nixpkgsMunin` fork input was removed
after moving the Munin graph FastCGI service into the local Munin container
configuration.

ConfCtl was added to fix flake-based health checks. Flake mode previously read
machine metadata with `nix eval`, which serialised store paths embedded in
local builder health-check commands without realising the derivations behind
those paths. The branch now exposes machine metadata as a built JSON derivation
and makes `NixFlake#list_machines` build and read it, matching the legacy
`nix-build` metadata path.

## Workspace

- Initiative: `2026-06-03-nixos-26-05-port`
- Tracking:
  - `work/2026-06-03-nixos-26-05-port/plan.md`
  - `work/2026-06-03-nixos-26-05-port/state.md`
- Worktree group:
  - `worktrees/2026-06-03-nixos-26-05-port/`

## Repositories

### vpsadminos

- Bare repo: `repos/vpsadminos.git`
- Remote: `git@github.com:vpsfreecz/vpsadminos.git`
- Default branch: `origin/staging`
- Feature branch: `2026-06-03-nixos-26-05-port`
- Worktree: `worktrees/2026-06-03-nixos-26-05-port/vpsadminos`
- Original base commit: `9e01370d8 os: update gems to 25.11.0.build20260603142841`
- Current upstream base: `a0adfcf74 os: update gems to 25.11.0.build20260603210657`
- Current head: `0ac745ae324072ec079620445ed4ea3531a7db96`
- Merge status: fast-forward merged into `origin/staging` at `0ac745ae3`
  on 2026-06-04.
- Commits:
  - `f4fc2445a os: support NixOS 26.05`
  - `772971874 os: bump version to 26.05`
  - `95bdc59f6 doc: add nixpkgs porting guide`
  - `8dfaa2698 tests: let NixOS VM initrd own root mounts`
  - `9f4db7a2f tests: load NFS modules in crashdump NFS test`
  - `4f0567a8a osctl-image: stage vpsAdminOS source for image builds`
  - `6f93d5d37 image-scripts: pin NixOS templates to tested vpsAdminOS rev`
  - `090decd7d os: enable NFSv4 client support`
  - `4a9866b73 os: update ZFS pin for fallocate fix`
  - `0ac745ae3 os: update gems to 26.05.0.build20260604154538`
- Status: clean; pushed to `origin/2026-06-03-nixos-26-05-port`

### zfs

- Bare repo: `repos/zfs.git`
- Remote: `git@github.com:vpsfreecz/zfs.git`
- Base commit: `f53469bdc dmu_recv: remove unused spill record local`
- Feature branch: `2026-06-03-nixos-26-05-port`
- Worktree: `worktrees/2026-06-03-nixos-26-05-port/zfs`
- Commits:
  - `6f5f54c3b linux: keep invalidate window over hole-punch frees`
- Status: clean

### ruby-lxc

- Bare repo: `repos/ruby-lxc.git`
- Remote: `git@github.com:vpsfreecz/ruby-lxc.git`
- Default branch used: `vpsfree`
- Feature branch: `2026-06-03-nixos-26-05-port`
- Worktree: `worktrees/2026-06-03-nixos-26-05-port/ruby-lxc`
- Base commit: `df19e1f gemspec: set license and required ruby version`
- Commits:
  - `004bf35 ext: support Ruby 3.4 rescue callbacks`
- Status: clean

### vpsfree-cz-configuration

- Bare repo: `repos/vpsfree-cz-configuration.git`
- Remote: `git@github.com:vpsfreecz/vpsfree-cz-configuration.git`
- Default branch: `origin/master`
- Feature branch: `2026-06-03-nixos-26-05-port`
- Worktree:
  `worktrees/2026-06-03-nixos-26-05-port/vpsfree-cz-configuration`
- Original base commit: `dc474a75 geminabox: update dependencies`
- Current upstream base: `1f1532af configs/internal-dns: add snajpadev.int zone`
- Current head: `92982a0c13e850698654f75a2572875e53339217`
- Commits:
  - `76671f15 inputs: update nixos-stable to 26.05`
  - `24ed62e9 inputs: update home-manager to 26.05`
  - `703c10b6 monitoring: ignore removed rspamd exporter option`
  - `a8f2d6d4 munin: run graph FastCGI service locally`
  - `b5b74e38 flake: remove unused nixpkgsMunin input`
  - `14b7094e inputs: set vpsadminosOsStaging, vpsadminosStaging to 0ac745ae`
  - `7ab3b814 inputs: set vpsadminServices to 4f413dfd`
  - `92982a0c inputs: set confctl to eb26c228`
- Status: clean; pushed to `origin/2026-06-03-nixos-26-05-port`

### vpsadmin

- Bare repo: `repos/vpsadmin.git`
- Remote: `git@github.com:vpsfreecz/vpsadmin.git`
- Default branch: `origin/master`
- Feature branch: `2026-06-03-nixos-26-05-port`
- Worktree: `worktrees/2026-06-03-nixos-26-05-port/vpsadmin`
- Original base commit: `4ffac2b0e webui: update dependencies`
- Current upstream base: `ad03f5cad tests: cover staged advisory publication time`
- Current head: `4f413dfd0e5a49aa0d1e08ec49ca24929072422d`
- Commits:
  - `5e8528463 tools: support exact vpsAdminOS flake pins`
  - `7e497223f nixos: remove cronie scheduler dependency`
  - `25283b9dc flake: vpsadminos 8f64dc771 -> 0ac745ae3`
  - `4f413dfd0 packages: update nodectl gems`
- Status: clean; pushed to `origin/2026-06-03-nixos-26-05-port`

### confctl

- Bare repo: `repos/confctl.git`
- Remote: `git@github.com:vpsfreecz/confctl.git`
- Default branch: `origin/master`
- Feature branch: `2026-06-03-nixos-26-05-port`
- Worktree: `worktrees/2026-06-03-nixos-26-05-port/confctl`
- Original base commit: `771aacd9 inputs: fail on cached GitHub metadata`
- Current upstream base: `771aacd9 inputs: fail on cached GitHub metadata`
- Current head: `eb26c2286e149c67eeea1906c49df28666d5b970`
- Commits:
  - `eb26c228 flakes: build machine metadata JSON`
- Status: clean; pushed to `origin/2026-06-03-nixos-26-05-port`

## Latest Rebase And Validation

Default branches were fetched on 2026-06-04 and feature branches were rebased
where upstream had advanced.

- `vpsadminos`
  - Rebased onto `origin/staging` at `a0adfcf74`.
  - Dropped stale generated gem commits and regenerated gems from the rebased
    tree.
  - New vpsAdminOS gem build id:
    `26.05.0.build20260604154538`.
  - Pushed rewritten branch head `0ac745ae3`.
  - Validation passed:
    `nix build .#template-stable .#template-impermanence-stable --no-link`.
- `vpsadmin`
  - Rebased onto `origin/master` at `ad03f5cad`.
  - Dropped stale generated package commit and regenerated packaged gems.
  - Pinned `vpsadminos` to `0ac745ae3`.
  - New vpsAdmin package gem build id:
    `4.1.0.build20260604181618`.
  - Pushed rewritten branch head `4f413dfd0`.
  - Validation passed for regenerated packages:
    `nix build --no-link --impure --expr 'let flake = builtins.getFlake
    "path:/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-06-03-nixos-26-05-port/vpsadmin";
    pkgs = import flake.inputs.nixpkgs { system = "x86_64-linux"; overlays =
    [ flake.overlays.default ]; }; in [ pkgs.libnodectld pkgs.nodectl
    pkgs.nodectld ]'`.
  - Previous validation passed before the latest upstream-only rebase:
    `./test-runner.sh test services-up`.
- `vpsfree-cz-configuration`
  - Rebased onto `origin/master` at `1f1532af` after upstream added the
    `snajpadev.int` internal DNS zone.
  - Dropped stale exact pins to vpsAdminOS `e9b6857c` and vpsAdmin
    `0a9ab0d3`.
  - Re-created generated `confctl` commits for vpsAdminOS `0ac745ae3`,
    vpsAdmin `4f413dfd0`, and ConfCtl `eb26c228`.
  - Pushed rewritten branch head `92982a0c`.
  - Validation passed:
    `confctl build -y "cz.vpsfree/vpsadmin/*"`.
  - Validation passed: `confctl build -y cz.vpsfree/containers/int.munin`.
  - Validation passed: `confctl build -y cz.vpsfree/containers/int.vpsfbot`.
  - Validation passed: `confctl build -y cz.vpsfree/machines/nixos-live`.
  - Validation passed: `nix build --no-link --json .#confctl.machinesJson`.
  - Validation passed: `nix develop -c confctl ls cz.vpsfree/containers/brq/ns1`.
  - Validation partially passed for the targeted DNS health check:
    `timeout 35s nix develop -c confctl health-check -y -j1
    cz.vpsfree/containers/brq/ns1`. All four local `dig` builder checks
    succeeded; the command was stopped during unrelated remote systemd checks
    that returned SSH/status `255` in this environment.
- `confctl`
  - Created feature branch from `origin/master` at `771aacd9`.
  - Validation passed: `bundle exec rspec spec/confctl/nix_flake_spec.rb`.
  - Validation passed:
    `bundle exec rubocop lib/confctl/nix_flake.rb
    spec/confctl/nix_flake_spec.rb`.
  - Validation passed: `nixfmt --check nix/flake/mk-confctl-outputs.nix`.
  - Pushed branch head `eb26c228`.
- GitHub Actions
  - vpsAdminOS current-head RuboCop and RSpec completed successfully.
  - vpsAdmin current-head API Specs and aggregate CI for `4f413dfd0` were
    queued at the latest poll.
  - vpsAdminOS current-head aggregate CI and changed-container-image workflows
    were queued at the latest poll.
  - ConfCtl current-head RSpec and RuboCop completed successfully.
  - ConfCtl current-head aggregate Tests workflow was queued at the latest
    poll.
  - `vpsfree-cz-configuration` current head had no branch workflow runs at the
    latest poll.
  - Superseded vpsAdmin aggregate CI run `26946249430` on this branch was
    cancelled after the rebase.
  - Superseded vpsAdmin aggregate CI run `26956773246` on this branch was
    cancelled after the latest rebase.
  - Superseded vpsAdmin API Specs run `26964838038` and aggregate CI run
    `26964837352` for the amended `ab097eb2c` head were cancelled.

## vpsAdminOS Staging Merge

Merged `vpsadminos` into `origin/staging` on 2026-06-04.

- Fetched `origin/staging` from `repos/vpsadminos.git`.
- Verified `origin/staging` (`a0adfcf74`) is an ancestor of the feature branch
  head `0ac745ae3`.
- Created temporary worktree:
  `worktrees/2026-06-03-nixos-26-05-port/vpsadminos-staging-merge`.
- Created temporary local branch:
  `2026-06-03-nixos-26-05-port-staging-merge`.
- Fast-forwarded the temporary branch with:
  `git merge --ff-only origin/2026-06-03-nixos-26-05-port`.
- Validation passed from the temporary staging worktree:
  `nix build .#toplevel .#template-stable .#template-impermanence-stable --no-link`.
- Pushed with:
  `nix develop --command git push origin HEAD:staging`.
- Confirmed `origin/staging` now resolves to
  `0ac745ae324072ec079620445ed4ea3531a7db96`.
- Removed the temporary worktree and temporary local branch.
- Staging push triggered vpsAdminOS workflows:
  - Build all kernel versions `26960430504`
  - CI `26960429951`
  - Build and test changed container images `26960430084`
  - RuboCop `26960430269`
  - RSpec `26960430381`

## Commands Run

- Inspected workspace directories:
  - `pwd && ls`
  - `find . -maxdepth 3 -type d ...`
  - `ps -u "$USER" ...`
- Checked remotes, existing branches, and worktrees for both repositories:
  - `git remote -v`
  - `git branch --list '2026-06-03-nixos-26-05-port'`
  - `git worktree list --porcelain`
- Fetched upstream refs:
  - `git -C repos/vpsadminos.git fetch --prune origin`
  - `git -C repos/vpsfree-cz-configuration.git fetch --prune origin`
  - `git -C repos/vpsadmin.git fetch --prune origin`
- Found default branches:
  - vpsAdminOS: `origin/staging`
  - vpsAdmin: `origin/master`
  - configuration: `origin/master`
- Created directories:
  - `work/2026-06-03-nixos-26-05-port`
  - `worktrees/2026-06-03-nixos-26-05-port`
- Created worktrees:
  - `git worktree add -b 2026-06-03-nixos-26-05-port .../vpsadminos origin/staging`
  - `git worktree add -b 2026-06-03-nixos-26-05-port .../vpsfree-cz-configuration origin/master`
  - `git worktree add -b 2026-06-03-nixos-26-05-port .../vpsadmin origin/master`
- Verified worktree status:
  - `git status --short --branch`
- Read repository instructions:
  - `vpsadminos/AGENTS.md`
  - `vpsadmin/AGENTS.md`
  - `vpsfree-cz-configuration/AGENTS.md`
- Inspected relevant Nix/channel files with `rg`, `sed`, and `find`,
  including:
  - `vpsadminos/flake.nix`
  - `vpsadminos/os/lib/nixos-container/*`
  - `vpsadminos/os/configs/image-repository.nix`
  - `vpsadminos/os/modules/nixos-modules.nix`
  - `vpsadminos/os/modules/nixos-compat.nix`
  - `vpsadminos/os/packages/linux/available-kernels.nix`
  - `vpsadmin/flake.nix`
  - `vpsadmin/tools/update_vpsadminos_flake.sh`
  - `vpsadmin/tasks/release.rb`
  - `vpsfree-cz-configuration/flake.nix`
  - `vpsfree-cz-configuration/README.md`
- Verified the NixOS 26.05 release announcement via:
  - https://nixos.org/blog/announcements/2026/nixos-2605/
  - https://nixos.org/manual/nixos/stable/release-notes
- Started `nix flake show --json --no-write-lock-file` in the vpsAdminOS
  worktree. It was taking longer than useful for planning and was killed.
  No lock file writes were allowed by the command.
- Added `ruby-lxc` to the top-level workspace project map in `AGENTS.md`.
- Cloned and prepared `ruby-lxc`:
  - `git clone --bare git@github.com:vpsfreecz/ruby-lxc.git repos/ruby-lxc.git`
  - `git -C repos/ruby-lxc.git worktree add -b 2026-06-03-nixos-26-05-port .../ruby-lxc vpsfree`
  - An initial mistaken worktree path under `repos/ruby-lxc.git/worktrees/...`
    was removed and recreated at the workspace-standard path.
- Updated vpsAdminOS `flake.nix` from `github:NixOS/nixpkgs/nixos-25.11` to
  `github:NixOS/nixpkgs/nixos-26.05`.
- Ran `nix flake lock --update-input nixpkgs`.
  - nixpkgs moved from `25f538306313eae3927264466c70d7001dcea1df`
    (`nixos-25.11`) to `b51242d7d43689db2f3be91bd05d5b24fbb469c4`
    (`nixos-26.05`).
- Ran focused vpsAdminOS evaluation probes while fixing 26.05 option fallout:
  - `nix eval --raw .#checks.x86_64-linux.os-eval.drvPath`
  - `nix eval --raw .#packages.x86_64-linux.toplevel.drvPath`
  - `nix eval --raw .#packages.x86_64-linux.template-stable.drvPath`
  - `nix eval --raw .#packages.x86_64-linux.template-impermanence-stable.drvPath`
  - `nix eval --raw .#nixosModules.container_26_05 --apply 'x: "ok"'`
- Ran `nix flake check --no-build`; this still fails on the repository's
  pre-existing `nixosConfigurations.container` output shape, where a module
  function is exposed in a position expected to be a full NixOS
  configuration. This is not currently treated as a 26.05 regression.
- Ran `make version VERSION=26.05`.
- Ran `nix build .#template-stable --no-link`; passed.
- Ran `nix build .#template-impermanence-stable --no-link`; passed.
- Ran `nix build .#toplevel --no-link --dry-run`; the dry-run evaluated and
  planned a 26.05 system build successfully.
- Ran `make gems`; the first run failed while building
  `ruby-lxc 1.2.4.vpsadminos.5` against Ruby 3.4.
  - Cause: the `rb_rescue` callback used the old no-argument callback
    signature.
- In `ruby-lxc`, changed the rescue callback signature and bumped the gem
  version to `1.2.4.vpsadminos.6`.
  - `bundle exec rake compile` passed in the vpsAdminOS dev shell.
  - `gem build ruby-lxc.gemspec` produced
    `ruby-lxc-1.2.4.vpsadminos.6.gem`.
  - Published the gem to the configured geminabox host from the vpsAdminOS
    dev shell; credentials are intentionally not recorded.
- Updated `osctld/osctld.gemspec` to require
  `ruby-lxc 1.2.4.vpsadminos.6`.
- Ran `make gems` again; passed and published vpsAdminOS gems with build id
  `20260603160117`.
- Ran `make osctl-env-exec BUILD_ID=20260603160117`; passed and brought
  `osctl-env-exec` to the same `26.05.0.build20260603160117` package set.
- Verified no remaining stale packaged-gem pins with:
  - `rg -n '25\.11\.0\.build|20260603155242|1\.2\.4\.vpsadminos\.5' os/packages osctld/osctld.gemspec .build_id`
- Ran Nix formatting with the repository's available `nixfmt` on changed Nix
  files and generated gemset files.
- Ran `nix build .#toplevel --no-link`; first full build failed on two 26.05
  package issues:
  - `irq_heatmap` failed under GCC 15 because `init_header()` was called with
    one argument.
  - `rsyslogd -N1` segfaulted during build-time config validation because
    `libfastjson.so.4` referenced the `modf` IFUNC without a direct `libm`
    dependency.
- Added vpsAdminOS package fixes:
  - Patch `irq_heatmap.c` at build time to call `init_header()` without the
    stale argument.
  - Override nixpkgs `libfastjson` so `libfastjson.la` links with `-lm`.
- Targeted rebuilds passed:
  - overlayed `pkgs.irq_heatmap`
  - overlayed `pkgs.libfastjson`
  - `readelf -d` confirmed rebuilt `libfastjson.so.4` has `NEEDED`
    `libm.so.6`.
- Re-ran `nix build .#toplevel --no-link`; passed.
- Re-ran `nix build .#template-stable .#template-impermanence-stable --no-link`;
  passed.
- Signed/installed Overcommit in the vpsAdminOS dev shell.
- Committed vpsAdminOS compatibility port:
  - `a8cbb03ff os: support NixOS 26.05`
  - Overcommit pre-commit hooks passed (`Nixfmt`, `RuboCop`).
- Committed vpsAdminOS version bump separately:
  - `ff6b14783 os: bump version to 26.05`
  - Overcommit pre-commit hooks passed (`Nixfmt`, `RuboCop`).
- Committed vpsAdminOS generated gem update:
  - `8422a4480 os: update gems to 26.05.0.build20260603160117`
  - Overcommit pre-commit and commit-message hooks passed.
- Added and committed `PORTING.md`:
  - `c64617d4c doc: add nixpkgs porting guide`
  - The document describes nixpkgs release porting, container templates,
    version bumping, gem rebuilds, validation, commit split, and
    compatibility checks.
- Committed `ruby-lxc` native fix:
  - `004bf35 ext: support Ruby 3.4 rescue callbacks`
- Pushed branches:
  - `ruby-lxc` `2026-06-03-nixos-26-05-port`
  - `vpsadminos` `2026-06-03-nixos-26-05-port`
- Rewrote the vpsAdminOS feature branch after user feedback to split the
  previous mixed `os: port to NixOS 26.05` commit into compatibility,
  version-bump, generated-gem, and documentation commits.
  - Kept a local backup branch:
    `2026-06-03-nixos-26-05-port-before-split`.
  - Verified the rewritten tree matches the previous implementation tree,
    excluding the newly added `PORTING.md`.
  - Force-pushed with lease to update the remote branch.
- Checked GitHub Actions:
  - Before the rewrite, vpsAdminOS RuboCop and RSpec passed.
  - After the rewrite, vpsAdminOS RuboCop passed.
  - After the rewrite, vpsAdminOS RSpec passed.
  - At the last poll, current-head changed-container-image tests were running
    in the `Build and test images` step.
  - At the last poll, current-head main CI had built and cached the OS
    closure, but the test-suite job was still queued.
  - Obsolete pre-rewrite CI runs remain visible for the same branch. Attempts
    to cancel them with `gh run cancel` failed with `HTTP 403: Resource not
    accessible by personal access token`, so they are being ignored rather
    than treated as signal.
  - `ruby-lxc` showed no branch runs in `gh run list` immediately after push.
- Investigated failed changed-container-image workflow
  `26897111651`.
  - Downloaded logs to
    `work/2026-06-03-nixos-26-05-port/artifacts/26897111651`.
  - The failure was not AlmaLinux 8 or Rocky Linux 8. It affected
    `nixos-25.11`, `nixos-25.11-impermanence`, `nixos-26.05`, and
    `nixos-26.05-impermanence`.
  - All four failed during the `nixos_rebuild` image test because the
    generated template flake resolved `vpsfreecz/vpsadminos` from the default
    `staging` branch and therefore did not expose `container_26_05`.
  - Local direct template generation pinned the branch head correctly, but the
    image test mounted a flake store copy of the repository without Git
    metadata, causing rebuild-time resolution to fall back to `staging`.
- Added image-test/source-revision fix:
  - Image tests mount `TEST_RUNNER_REPO_ROOT` when available, so CI passes the
    live checkout to `osctl-image`.
  - NixOS image builds record the source checkout `HEAD` in
    `.vpsadminos-git-rev` before stripping Git metadata from their temporary
    source copy.
  - The flake uses `.vpsadminos-git-rev` only when normal flake `self.rev` or
    `self.dirtyRev` are unavailable.
- Validation for image-test/source-revision fix:
  - `TEST_RUNNER_REPO_ROOT=$PWD nix-build test-runner/nix/evaluate-tests.nix --arg repoRoot ./. --argstr system x86_64-linux --argstr mode testJson --argstr testPath image-scripts/test@nixos-26.05 --out-link /tmp/vpsadminos-image-test-json`
    produced test JSON whose `sharedFileSystems.hostOs` points at the live
    checkout.
  - Simulated the image builder copy without `.git` plus
    `.vpsadminos-git-rev`; the generated template lock pinned
    `vpsfreecz/vpsadminos` to `c64617d4c3f0a9fc0455da636ef22a98e955d079`
    instead of `staging`.
  - `nix build .#template-stable .#template-impermanence-stable --no-link`
    passed.
  - `git diff --check` passed.
  - Overcommit pre-commit and commit-msg hooks passed for commit
    `7fc46e487`.
  - Initial ambient `git push` attempts failed because the ambient Overcommit
    hook saw an unsigned config. `nix develop --command overcommit --sign`
    and `nix develop --command git push` succeeded.
- Post-fix GitHub Actions:
  - New runs for `7fc46e487` were created:
    - RSpec `26901224846`, completed successfully.
    - CI `26901224705`, queued at last poll.
    - Build and test changed container images `26901224706`, queued at last
      poll.
- CI follow-up for `7fc46e487`:
  - CI `26901224705` completed with failures before the local follow-up fixes
    were pushed.
  - Build and test changed container images `26901224706` completed with
    failures before the local follow-up fixes were pushed.
  - Downloaded changed-image logs to
    `work/2026-06-03-nixos-26-05-port/artifacts/26901224706`.
  - Driver NixOS failures were caused by NixOS 26.05 systemd initrd receiving
    both the generated `root=fstab` parameter and explicit test-runner
    `root=/dev/disk/by-label/nixos rootfstype=ext4` parameters. This created
    duplicate `sysroot.mount` units and left NixOS tests in the initrd
    emergency shell.
  - `crashdump/nfs-inspect` failed after boot with `mount.nfs -o vers=4`
    reporting `Protocol not supported`; the test loaded NFS modules only in
    the initrd crashdump path.
  - NixOS image-template tests no longer failed on missing source revision.
    They failed during nested builder setup because Nix evaluated
    `path:/build/vpsadminos.<id>` as a build user and could not read the
    bind-mounted checkout.
- Added CI follow-up fixes:
  - NixOS tests now force `virtualisation.fileSystems = { }` and no longer add
    explicit root device/fstype kernel parameters, letting NixOS 26.05 provide
    its generated `root=fstab` boot parameters.
  - `crashdump/nfs-inspect` loads NFS modules after boot as well as in the
    initrd.
  - NixOS image builder setup copies `--vpsadminos-dir` to a builder-local
    `/tmp` directory, makes the copy readable by Nix build users, writes the
    revision fallback, and points the setup flake at the local copy.
  - NixOS image build copies also normalize checkout permissions before Nix
    evaluates them.
- Validation for CI follow-up fixes:
  - `./test-runner.sh test -f driver/nixos` passed locally.
  - `./test-runner.sh test -f driver/named-shells` passed locally.
  - `nix develop --command nixfmt tests/make-test.nix tests/configs/nixos/base.nix tests/suite/crashdump/nfs-inspect.nix`
    passed.
  - `bash -n image-scripts/builders/nixos/setup.sh image-scripts/include/nixos.sh`
    passed.
  - `git diff --check` passed.
  - `nix develop --command overcommit --run` passed.
  - A local `./test-runner.sh test -f image-scripts/test@nixos-26.05` attempt
    was terminated after 300 seconds because the VM stayed at firmware output
    before running the first shell command. The CI artifact had already
    isolated the image-template failure to the nested builder source path, so
    the full image-template verification is left to the fresh GitHub run.
  - Overcommit hooks passed while committing `497b5635c` and `108cf689f`.
- Pushed vpsAdminOS `108cf689f` to branch
  `2026-06-03-nixos-26-05-port`.
- Fresh GitHub Actions for `108cf689f`:
  - CI `26907158639`, in progress at first poll.
  - Build and test changed container images `26907158766`, queued at first
    poll.
- CI follow-up for `108cf689f`:
  - Build and test changed container images `26907158766` failed on all NixOS
    image-template tests with `cp: cannot access '/build/vpsadminos.../.'` in
    nested builder setup.
  - The main CI `26907158639` also completed with failures on the stale head
    and is ignored after the newer fixes.
- Added source-staging follow-up:
  - `osctl-image` now stages `--vpsadminos-dir` into a temporary local copy,
    removes `.git` and `result`, writes `.vpsadminos-git-rev` when possible,
    normalizes permissions, and mounts the staged copy into nested builders.
  - This avoids relying on direct virtiofs or Nix-store checkout readability
    inside nested unprivileged image builders.
- Validation for source-staging follow-up:
  - `nix develop --command bundle exec rubocop osctl-image/lib/osctl/image/operations/image/build.rb osctl-image/spec/osctl/image/operations/image/build_spec.rb`
    passed.
  - `nix develop --command bash -lc 'cd osctl-image && bundle install && bundle exec rspec spec/osctl/image/operations/image/build_spec.rb'`
    passed.
  - `nix develop --command make gems` rebuilt generated gems with build id
    `26.05.0.build20260603221830`.
  - Overcommit hooks passed for commits `02fb31cc5` and `b9e62d9a9`.
  - Local `./test-runner.sh test -f image-scripts/test@nixos-26.05` is running
    on the new head; it has reached `osctl-image ... test nixos-26.05` and
    passed the earlier builder setup failure point.
- Pushed vpsAdminOS `b9e62d9a9` to branch
  `2026-06-03-nixos-26-05-port`.
  - Ambient `git push` loaded Overcommit 0.69.0 and failed the pre-push
    signature check even after signing with Overcommit 0.70.0 from the Nix
    shell.
  - `nix develop --command git push origin 2026-06-03-nixos-26-05-port`
    succeeded.
- Fresh GitHub Actions for `b9e62d9a9`:
  - RuboCop `26911602075` completed successfully.
  - RSpec `26911601957` completed successfully.
  - CI `26911601390` built and cached the OS closure; its test-suite job is
    running.
  - The changed-container-image workflow did not retrigger, because the latest
    push range changed only `osctl-image` and generated gem files and
    `image-scripts.yml` has no `workflow_dispatch`.
- Local image-template follow-up for `b9e62d9a9`:
  - `./test-runner.sh test -f image-scripts/test@nixos-26.05` passed the
    builder setup and ran 13 of 14 image tests successfully.
  - The remaining `nixos_rebuild` test failed because the generated template
    lock fell back to `origin/staging` commit `a0adfcf74`, which did not
    expose `container_26_05`.
  - Cause: when the repository is mounted into the VM from a Git worktree,
    `.git` is a pointer to a host-only absolute gitdir, so Git inside the VM
    cannot resolve `HEAD` and the template omits its flake lock.
- Added explicit source-revision follow-up:
  - `test-runner.sh` exports `TEST_RUNNER_REPO_REV` from the host checkout.
  - `tests/suite/image-scripts/test.nix` passes that revision to
    `osctl-image` as `OSCTL_IMAGE_VPSADMINOS_REV`.
  - `osctl-image` and the NixOS image-builder shell scripts prefer the
    explicit revision before probing Git, and propagate it into nested
    builders.
- Validation for explicit source-revision follow-up:
  - `bash -n test-runner.sh image-scripts/include/nixos.sh image-scripts/builders/nixos/setup.sh`
    passed.
  - `nix develop --command nixfmt tests/suite/image-scripts/test.nix` passed.
  - `nix develop --command bundle exec rubocop osctl-image/lib/osctl/image/operations/image/build.rb osctl-image/spec/osctl/image/operations/image/build_spec.rb`
    passed.
  - `nix develop --command bash -lc 'cd osctl-image && bundle install && bundle exec rspec spec/osctl/image/operations/image/build_spec.rb'`
    passed.
  - Evaluated `image-scripts/test@nixos-26.05` test JSON with
    `TEST_RUNNER_REPO_REV`; the generated test command includes
    `OSCTL_IMAGE_VPSADMINOS_REV=... osctl-image`.
  - `nix develop --command make gems` rebuilt generated gems with build id
    `26.05.0.build20260603231238`.
- Pushed vpsAdminOS `9545c07e3` to branch
  `2026-06-03-nixos-26-05-port`.
- Fresh GitHub Actions for `9545c07e3`:
  - RuboCop `26913596206` completed successfully.
  - RSpec `26913596048` completed successfully.
  - CI `26913596171` built and cached the OS closure; its test-suite job is
    failed after 68 successful tests and three failures:
    `osctl/ct-local-transfer`, `crashdump/nfs-inspect`, and
    `zfs/fallocate-deadlock`.
  - Build and test changed container images `26913596957` built and cached
    the OS closure, detected changed image scripts, ran image tests, and
    completed successfully.
  - Local `./test-runner.sh test -f image-scripts/test@nixos-26.05` passed in
    2351.78 seconds.
- Investigated CI artifacts from run `26913596171`:
  - `crashdump/nfs-inspect` failed because neither the normal system nor the
    crash initrd could mount NFSv4; `mount.nfs` returned
    `Invalid argument`/`Protocol not supported`.
  - `zfs/fallocate-deadlock` reproduced a blocked-task deadlock in the
    fallocate/page-fault stress test.
  - `osctl/ct-local-transfer` failed once while restarting the source
    container after split-copy cleanup.
- Added a vpsAdminOS kernel config fix:
  - `NFS_FS = yes`
  - `NFS_V4_1 = yes`
  - `NFS_V4_2 = yes`
- Created and pushed the ZFS branch `2026-06-03-nixos-26-05-port`:
  - `git clone --bare git@github.com:vpsfreecz/zfs.git repos/zfs.git`
  - `git worktree add -b 2026-06-03-nixos-26-05-port .../zfs f53469bdc...`
  - `6f5f54c3b linux: keep invalidate window over hole-punch frees`
  - `git push origin 2026-06-03-nixos-26-05-port`
- Updated the vpsAdminOS Linux 6.12.91 ZFS pin to
  `6f5f54c3bfd68c1e52b0b6f454ee9679aaa9e83d`.
  - Prefetched archive hash:
    `sha256-4WQWL4wd3TYaTfqEqQ6ZDYLXmqnHW7XQz2DP0FpwsRQ=`.
- Local validation for the CI follow-up:
  - `./test-runner.sh test -f zfs/fallocate-deadlock` passed in
    4247.59 seconds.
  - `./test-runner.sh test -f crashdump/nfs-inspect` passed in
    1314.1 seconds.
  - `./test-runner.sh test -f osctl/ct-local-transfer` passed in
    1137.28 seconds. The CI-failing restart example passed locally in
    95.81 seconds, so no code change was made for that case.
  - `nix develop --command nixfmt os/packages/linux/common-config.nix
    os/packages/linux/available-kernels.nix` passed.
  - `git diff --check` passed in both the vpsAdminOS and ZFS worktrees.
- Committed and pushed vpsAdminOS follow-up fixes:
  - `8ddf1d2ea os: enable NFS client support`
  - `03a1637a0 os: update ZFS pin for fallocate fix`
  - Overcommit pre-commit and commit-message hooks passed for both commits.
- Fresh GitHub Actions for `03a1637a0`:
  - CI `26921583239` completed successfully.
  - `Build OS and populate binary cache` completed successfully after
    rebuilding the top-level closure with the new kernel/ZFS inputs.
  - `Run test suite` completed successfully.
- Rewrote the vpsAdminOS feature branch again after review feedback:
  - Backup ref: `2026-06-03-nixos-26-05-port-before-review-cleanup`.
  - Split generic NixOS VM initrd changes from `crashdump/nfs-inspect`
    runtime NFS module setup.
  - Collapsed the four exploratory image source/revision commits into two
    commits: one for source staging and one for tested revision pinning.
  - Collapsed the two later generated gem commits into one generated commit:
    `3f3441052 os: update gems to 26.05.0.build20260604085422`.
  - Rewrote the NFS kernel config commit message to explain that vpsAdminOS
    kernel config remains independent from nixpkgs.
- Validation after the rewrite:
  - `bash -n test-runner.sh image-scripts/include/nixos.sh
    image-scripts/builders/nixos/setup.sh` passed.
  - Initial top-level `bundle exec rspec ...build_spec.rb` failed because the
    top-level bundle does not include RSpec; reran from `osctl-image`.
  - `cd osctl-image && bundle install && bundle exec rspec
    spec/osctl/image/operations/image/build_spec.rb` passed with
    9 examples and 0 failures.
  - `nix build .#template-stable .#template-impermanence-stable --no-link`
    passed.
  - Compared rewritten tree with the old backup ref; only generated packaged
    gem build ids differ.
- Pushed rewritten vpsAdminOS branch with `git push --force-with-lease`.
  Remote moved from `03a1637a0` to `e9b6857cc`.
- GitHub Actions for rewritten head `e9b6857cc`:
  - RuboCop `26936576915`: success.
  - RSpec `26936576932`: success.
  - Build and test changed container images `26936577045`: success.
  - CI `26936576969`: success.
- Ported vpsAdmin to the vpsAdminOS 26.05 input graph:
  - Installed and signed Overcommit in the vpsAdmin dev shell.
  - Added optional exact-pin support to `tools/update_vpsadminos_flake.sh`.
    The script keeps the no-argument staging update path, supports a flake URL
    argument for lock-only exact pins, and now commits through `git commit -F`.
  - Ran
    `tools/update_vpsadminos_flake.sh github:vpsfreecz/vpsadminos/e9b6857ccb7ca75a144e71469441b8d54948b2ad`
    in the dev shell. The script committed the isolated lock update.
  - Verified `flake.lock`:
    - `vpsadminos` locked rev:
      `e9b6857ccb7ca75a144e71469441b8d54948b2ad`
    - original input remains `github:vpsfreecz/vpsadminos/staging`
    - followed `nixpkgs_2` locked rev:
      `b51242d7d43689db2f3be91bd05d5b24fbb469c4`
  - `./test-runner.sh --version` prints `test-runner version 26.05.0`.
  - `./test-runner.sh ls services-up` found the target test.
  - First `./test-runner.sh test services-up` was stopped after the build log
    showed packaged nodectl dependencies still pulling vpsAdminOS 25.11 gems.
  - `rake vpsadmin:gems` initially failed because `.gems` contained native
    `json` built against Ruby 3.4.8 while the 26.05 shell used Ruby 3.4.9.
    Removed the ignored `.gems` directory and reran successfully.
  - `rake vpsadmin:gems` published and regenerated:
    - `libnodectld-4.1.0.build20260604111221`
    - `nodectl-4.1.0.build20260604111221`
    - `nodectld-4.1.0.build20260604111221`
  - Verified the regenerated package gemsets now use vpsAdminOS gems
    `26.05.0.build20260604085422` and no longer contain old
    `25.11.0.build` pins.
  - The next `services-up` run failed during evaluation because the local
    `cronie-1.6.1` package did not build with GCC 15:
    `load_entry` used an unprototyped callback declaration incompatible with
    `log_error(const char *)`.
  - Initially committed a cronie build patch, then replaced it after review:
    `vpsadmin-scheduler` no longer relies on an external crontab, so the
    branch was rewritten to remove cronie instead of patching unused code.
  - Removed the local cronie package, the custom `services.cron` module and
    `permitAnyCrontab` option, and the scheduler module's cron overlay and
    enablement.
  - `./test-runner.sh test admin/scheduler-socket-control` passed in
    599.16 seconds with the scheduler socket update/run path verified.
  - `./test-runner.sh test services-up` passed in 432.44 seconds with all
    27 examples successful, including the scheduler service check.
  - Overcommit signing had to be done with the same environment as the hook:
    ambient Ruby for inspection and the Nix dev shell for the final commit,
    so `nixfmt` was available to the pre-commit hook.
  - Committed and force-pushed vpsAdmin branch
    `2026-06-03-nixos-26-05-port` with lease:
    `0a9ab0d38 nixos: remove cronie scheduler dependency`.
  - Attempted to cancel old queued same-branch CI run `26943515869`; GitHub
    returned `HTTP 403: Resource not accessible by personal access token`.
  - GitHub Actions for old vpsAdmin head `267a1cc01`:
    - Webui PHPUnit `26943515874`: success.
    - Client Specs `26943515915`: success.
    - libnodectld Specs `26943515906`: success.
    - API Specs (topic parallel) `26943515875`: success.
    - CI `26943515869`: still queued at the last poll; cancellation is blocked
      by token permissions.
  - GitHub Actions for new vpsAdmin head `0a9ab0d38` at the last poll:
    - API Specs (topic parallel) `26946249973`: success.
    - CI `26946249430`: in progress in `Run selected ci-tagged tests`.
      Later polls still showed the `Run tests` step in progress; GitHub does
      not expose job logs until the job completes.
  - A second attempt to cancel old same-branch CI run `26943515869` also
    failed with `HTTP 403: Resource not accessible by personal access token`.
- Ported `vpsfree-cz-configuration` to the 26.05 stable service graph:
  - Fast-forwarded the worktree branch to current `origin/master`
    `6471a92e`.
  - Installed and signed Overcommit in the configuration dev shell.
  - Updated `nixpkgsStable.url` to
    `github:NixOS/nixpkgs/nixos-26.05`.
  - Ran `confctl inputs channel update --commit --no-changelog --no-editor
    nixos-stable`; because the URL edit was already dirty, confctl updated the
    lock and the result was committed manually with hooks.
  - Updated `home-manager.url` to
    `github:nix-community/home-manager/release-26.05`.
  - Ran `confctl inputs channel update --commit --no-editor home-manager`;
    because the URL edit was already dirty, confctl updated the lock and the
    result was committed manually with hooks.
  - Ran `confctl inputs channel set --commit --no-editor
    '{staging,os-staging}' vpsadminos
    e9b6857ccb7ca75a144e71469441b8d54948b2ad`.
  - Ran `confctl inputs channel set --commit --no-editor vpsadmin vpsadmin
    0a9ab0d38902afdec3fc160c46356becc3c6a994`.
  - Left `nixpkgsStaging` and `nixpkgsProduction` on `nixos-25.11`; those are
    separate rollout channels.
  - Checked `aither64/nixpkgs` for `26.05-munin-fastcgi`; no such branch was
    present.
  - Initial `confctl build "cz.vpsfree/vpsadmin/*"` failed because NixOS
    26.05 removed `services.prometheus.exporters.rspamd`.
  - Fixed generic exporter discovery by filtering the removed `rspamd`
    exporter option.
  - `confctl build "cz.vpsfree/vpsadmin/*"` then passed for all 11 vpsAdmin
    service machines with generation `2026-06-04--13-25-20`.
  - `confctl build "org.vpsadminos/*"` matched no machines in the current
    configuration.
  - `confctl build cz.vpsfree/machines/build` failed on a local input:
    `/srv/iso-images/systemrescue-11.01-amd64.iso` is missing. The same run
    also printed warnings about `boot.zfs.forceImportRoot` and
    `vimPlugins.sensible`, but the missing ISO stopped the build before they
    could be assessed as blockers.
  - Representative stable builds passed:
    - `cz.vpsfree/machines/nixos-live`: `2026-06-04--13-37-16`
    - `cz.vpsfree/containers/brq/ns1`: `2026-06-04--13-39-19`
    - `cz.vpsfree/containers/prg/proxy`: `2026-06-04--13-40-34`
    - `cz.vpsfree/containers/int.web`: `2026-06-04--13-42-43`
    - `cz.vpsfree/containers/prg/int.mon1`: `2026-06-04--13-49-38`
    - `cz.vpsfree/containers/int.munin`: `2026-06-04--13-54-04`
    - `cz.vpsfree/containers/int.vpsfbot`: `2026-06-04--13-57-03`
  - `int.munin` initially failed while mixing vpsAdminOS 26.05 container
    modules with the 25.11 `nixpkgsMunin` fork. The fork existed only for
    Munin graph FastCGI support. The branch now defines the local
    `munin-cgi-graph` `spawn-fcgi` service, removes the machine override, and
    removes the unused `nixpkgsMunin` flake input.
  - Pushed `vpsfree-cz-configuration` branch
    `2026-06-03-nixos-26-05-port` to GitHub.
  - `gh run list --branch 2026-06-03-nixos-26-05-port` returned no runs for
    `vpsfree-cz-configuration`. The repository only has the scheduled
    `Daily update` workflow and no push/PR CI trigger.

## Observations

- vpsAdminOS currently pins `inputs.nixpkgs.url` to
  `github:NixOS/nixpkgs/nixos-26.05` in the feature worktree.
- vpsAdminOS container template outputs build stable and unstable variants:
  - `template-stable`
  - `template-unstable`
  - `template-impermanence-stable`
  - `template-impermanence-unstable`
- Stable container modules currently include versioned files through
  `vpsadminos-25.11.nix`; the feature worktree adds
  `vpsadminos-26.05.nix` and exports `nixosModules.container_26_05`.
- `os/configs/image-repository.nix` gives NixOS `25.11` and
  `25.11-impermanence` the `latest` and `stable` tags at baseline. The
  feature worktree moves those tags to `26.05` and `26.05-impermanence` while
  keeping untagged 25.11 entries.
- vpsAdminOS currently pins its own kernel/ZFS pair at Linux `6.12.91`; NixOS
  26.05's default kernel does not automatically apply to the vpsAdminOS
  runtime kernel.
- `vpsadmin` has:
  - `vpsadminos.url = "github:vpsfreecz/vpsadminos/staging"`
  - `nixpkgs.follows = "vpsadminos/nixpkgs"`
  - repository-local rule requiring `tools/update_vpsadminos_flake.sh` for
    vpsAdminOS flake input updates.
  - `rake vpsadmin:gems` for generated Nix-packaged gem rebuilds.
- `vpsfree-cz-configuration` has:
  - `nixpkgsStable.url = "github:NixOS/nixpkgs/nixos-26.05"`
  - `home-manager.url = "github:nix-community/home-manager/release-26.05"`
  - `nixpkgsStaging.url = "github:NixOS/nixpkgs/nixos-25.11"`
  - `nixpkgsProduction.url = "github:NixOS/nixpkgs/nixos-25.11"`
  - no `nixpkgsMunin` input after the Munin FastCGI service was moved local
    to `cluster/cz.vpsfree/containers/int.munin/config.nix`
  - `vpsadminosOsStaging` and `vpsadminosStaging` pinned to `0ac745ae3`
  - `vpsadminServices` pinned to `4f413dfd0`
  - `confctl` pinned to `eb26c228`
- Many configuration hosts/containers consume `nixos-stable`; the update is
  broad enough to require sampled builds before any production rollout.
- NixOS 26.05's `services.resolved.fallbackDns` surface changed for the
  stable container template; the feature worktree now sets
  `services.resolved.settings.Resolve.FallbackDNS`.
- NixOS 26.05 module evaluation required additional compatibility stubs in
  vpsAdminOS for:
  - `services.howdy.enable`
  - `services.kanidm.unix.enable`
  - `systemd.generatorEnvironment`
  - `systemd.generatorPath`
- nixpkgs 26.05 deprecates `lib.fold`; vpsAdminOS local uses were changed to
  `foldr`.

## Hook/Environment Notes

- Worktree adds checked out successfully but exited non-zero due hook
  environment/setup:
  - vpsAdminOS: Overcommit reported a changed config signature and asked for
    `overcommit --sign`.
  - vpsAdmin: Overcommit reported a changed config signature and asked for
    `overcommit --sign`.
  - configuration: Bundler could not find hook gems in the ambient shell and
    suggested `bundle install --gemfile=Gemfile`.
- Before any commit:
  - enter each repository's Nix dev shell;
  - install/sign Overcommit as required;
  - run hooks with repository-pinned tools.
- While rewriting vpsAdminOS from the 25.11 base through 26.05 commits, the
  untracked `.gems` cache contained native extensions built against the other
  Ruby patchlevel. `overcommit` then failed with incompatible `json` native
  extension errors until `.gems` was removed and rebuilt in the current dev
  shell.

## Open Work

1. Decide whether the local `/srv/iso-images/systemrescue-11.01-amd64.iso`
   input should be provided or the `cz.vpsfree/machines/build` validation
   should be deferred to an environment that has it.
2. Default-branch CI follow-up was stopped at user request after the merges.

## 2026-06-04 Deprecation Scan

- Ran `nix develop -c confctl build -y` for all machines and terminated it
  once `nix build` was confirmed running. No `warning:`, `deprecated`,
  `renamed`, `obsolete`, or similar notices were emitted before termination.
- Ran `nix develop -c confctl build -y -t build`. This selected
  `cz.vpsfree/machines/build` and emitted:
  - `boot.zfs.forceImportRoot` is using the 26.05 default value `true`, which
    is recommended to be set to `false` before the 26.11 default flip.
  - `vimPlugins.sensible` was renamed to `vimPlugins.vim-sensible`.
  - The run then failed on missing local input
    `/srv/iso-images/systemrescue-11.01-amd64.iso`.
- Ran a direct `nix build --dry-run --no-link` over generated
  `.#confctl.build.<key>.{toplevel,autoRollback}` installables. This stopped
  before build planning on the `int.kb` missing `fsType` error above.
- Retried dry-run and derivation-path evaluation while excluding
  `cz.vpsfree/containers/int.kb`; those broad evaluations were interrupted or
  timed out without emitting deprecation warnings.
- A single known-good vpsAdmin service derivation-path evaluation completed in
  about 20 seconds and emitted no warnings.
- Result: the `-t build` path has two actionable 26.05 warnings. The
  `int.kb` missing `fsType` remains a separate full-fleet blocker before an
  exhaustive dry-run scan can complete.

## 2026-06-04 Warning Fixes

- Added commits in `vpsfree-cz-configuration`:
  - `6fd81a1b cluster: fix build machine 26.05 warnings`
  - `5752a767 cluster: fix int.kb bind mount fs type`
- Pushed `origin/2026-06-03-nixos-26-05-port` to
  `5752a7673a224937cb9e6cd40bd4360706785f79`.
- Changes:
  - `environments/deploy.nix` now uses `vimPlugins.vim-sensible`.
  - `cluster/cz.vpsfree/machines/build/config.nix` sets
    `boot.zfs.forceImportRoot = false`.
  - `cluster/cz.vpsfree/containers/int.kb/config.nix` sets `fsType = "none"`
    for the Dokuwiki shared media bind mounts.
- Validation:
  - `nix develop -c nixfmt --check` passed on all three changed files.
  - `nix develop -c confctl build -y -t build` no longer emits the
    `forceImportRoot` or `vimPlugins.sensible` warnings. It still fails on the
    known missing local input `/srv/iso-images/systemrescue-11.01-amd64.iso`.
  - `nix develop -c nix eval --raw ...int_kb...toplevel.drvPath` succeeded
    and produced a `nixos-system-kb-26.05...drv` path.

## 2026-06-04 Default Branch Merges

- Fast-forwarded and pushed default branches:
  - `vpsadminos`: `staging` already contained
    `0ac745ae324072ec079620445ed4ea3531a7db96`.
  - `confctl`: `master` pushed to
    `eb26c2286e149c67eeea1906c49df28666d5b970`.
  - `vpsadmin`: `master` pushed to
    `4f413dfd0e5a49aa0d1e08ec49ca24929072422d`.
  - `vpsfree-cz-configuration`: `master` pushed to
    `5752a7673a224937cb9e6cd40bd4360706785f79`.
- Removed temporary merge worktrees after push. Feature worktrees and feature
  branches were kept.
- GitHub Actions after merge:
  - `confctl`: RSpec and RuboCop succeeded; aggregate was still queued.
  - `vpsadmin`: several workflows were still running or queued.
  - User asked to forget workflow follow-ups, so no further CI monitoring was
    done in this turn.

## 2026-06-04 Grafana Secret Key

- Added and pushed `vpsfree-cz-configuration` commit
  `63b96943 cluster: set Grafana secret key file`.
- `cluster/cz.vpsfree/containers/prg/int.grafana/config.nix` now sets
  `services.grafana.settings.security.secret_key` to
  `$__file{/private/grafana/secret_key.txt}`.
- Pushed both `origin/2026-06-03-nixos-26-05-port` and `origin/master` to
  `63b9694339949384c9d9b3dd7382ca59b162745f`.
- Validation:
  - `nix develop -c nixfmt --check
    cluster/cz.vpsfree/containers/prg/int.grafana/config.nix` passed.
  - `nix develop -c confctl build -y
    cz.vpsfree/containers/prg/int.grafana` passed and produced generation
    `2026-06-04--19-56-49`.

## 2026-06-04 ns0 BIND Config Check

- Reproduced the reported `cz.vpsfree/containers/ns0` build failure:
  `named-checkconf` rejected the runtime include
  `/var/named/vpsadmin/named.conf` while building the generated
  `named.conf` derivation.
- Kept the fix in `vpsfree-cz-configuration`, because the BIND configuration
  is in the shared production DNS fragment rather than in `vpsadmin`.
- Added and pushed `vpsfree-cz-configuration` commit
  `2d954a19 cluster: skip bind config check for DNS containers`.
- `cluster/cz.vpsfree/vpsadmin/common/dns.nix` now sets
  `services.bind.checkConfig = false` next to the BIND enablement. The runtime
  include remains intact; nodectld still writes the included configuration
  after boot.
- Pushed both `origin/2026-06-03-nixos-26-05-port` and `origin/master` to
  `2d954a1945e863808f7e795c50b3c363b6e46524`.
- Validation:
  - `nix develop -c nixfmt --check
    cluster/cz.vpsfree/vpsadmin/common/dns.nix` passed.
  - `nix develop -c confctl build -y cz.vpsfree/containers/ns0` passed and
    produced generation `2026-06-04--20-52-52`.
- Temporary merge worktree
  `worktrees/2026-06-03-nixos-26-05-port/vpsfree-cz-configuration-merge-bind-check`
  was removed after pushing `master`.

## 2026-06-04 PHP-FPM Session Cleanup

- Implemented shared PHP-FPM session cleanup for pools configured in
  `vpsfree-cz-configuration`.
- Added and pushed `vpsfree-cz-configuration` commit
  `6007b964 modules: manage php-fpm session cleanup`.
- Pushed both `origin/2026-06-03-nixos-26-05-port` and `origin/master` to
  `6007b9646a50aa6199ef272d3b9bb02636ce09c8`.
- Added a NixOS helper module
  `modules/system/phpfpm-session-cleanup.nix` with internal option
  `vpsfconf.phpfpmSessionCleanup.pools`.
- Managed pools now store sessions under
  `/var/lib/phpfpm/<pool>/sessions`, disable request-time PHP session GC, and
  rely on `systemd-tmpfiles-clean.timer` to clean files older than `1d`.
- Opted in pools:
  - `dokuwiki-kb.vpsfree.cz`
  - `dokuwiki-kb.vpsfree.org`
  - `vpsfree`
  - `blog`
  - `foto`
  - `adminer`
- Added the helper import to the nested `aitherdev` `vpsfree-web` container so
  its direct `vpsfree-web.nix` import has the new option available.
- Validation:
  - `nix develop -c nixfmt --check ...` passed for all changed Nix files.
  - Direct derivation eval passed for `cz.vpsfree/containers/int.kb`,
    `cz.vpsfree/containers/int.web`, and
    `cz.vpsfree/containers/int.utils`.
  - `nix develop -c confctl build -y cz.vpsfree/containers/int.kb` passed and
    produced generation `2026-06-04--21-59-35`.
  - `nix develop -c confctl build -y cz.vpsfree/containers/int.utils` passed
    and produced generation `2026-06-04--22-01-04`.
  - `nix develop -c confctl build -y cz.vpsfree/containers/int.web` was rerun
    serially after a parallel ConfCtl log-name collision and passed, using
    generation `2026-06-04--22-01-04`.
  - Grepped the built PHP-FPM unit PHP ini files and confirmed the managed
    `session.save_path`, `session.gc_probability = 0`, and
    `session.gc_maxlifetime = 86400` values for all six opted-in pools.
  - Grepped the built tmpfiles config and confirmed `1d` cleanup entries for
    all six session directories.
- `cz.vpsfree/machines/aitherdev` derivation eval was attempted, but it fails
  on an existing duplicate declaration of
  `home-manager.users.aither.programs.tmux.tmuxinator.projects` before reaching
  this PHP-FPM change.

## 2026-06-04 Munin FastCGI Perl Wrapper

- Reproduced `int.munin` `munin-cgi-graph.service` startup failure from the
  generated 26.05 system path. The immediate failure was Perl compilation in
  `munin-cgi-graph`, not the systemd BPF/IPAccounting warning:
  missing `Date::Parse`/`CGI::Fast`/`CGI.pm` under taint mode.
- Confirmed the old `nixpkgsMunin` fork carried both the
  `use_lib_in_fcgi_scripts.patch` package patch and the `CGI`/`CGIFast`
  wrapper path for Munin CGI scripts. Removing that fork exposed the stock
  nixpkgs Munin package issue.
- Added a local `vpsfree-cz-configuration` Munin overlay that applies the CGI
  `use lib` patch and prepends `CGI`/`CGIFast` plus propagated Perl
  dependencies to the generated CGI wrapper `PERL5LIB`.
- Added and pushed `vpsfree-cz-configuration` commit
  `0aa4fd1b munin: fix FastCGI Perl wrapper`.
- Pushed both `origin/2026-06-03-nixos-26-05-port` and `origin/master` to
  `0aa4fd1bd59e42cc6304a4593eadae14a2d35c83`.
- Left the NixOS 26.05 `DefaultIPAccounting=true` BPF warning unchanged, per
  user decision.
- Validation:
  - `nix develop -c nixfmt overlays/packages.nix` completed successfully.
  - First `confctl build -y cz.vpsfree/containers/int.munin` failed because
    the new patch file was untracked and therefore missing from the flake
    source copied to the store.
  - After staging the overlay and patch file, `nix develop -c confctl build -y
    cz.vpsfree/containers/int.munin` passed and produced generations
    `2026-06-04--22-34-00` and, after tightening the patch context,
    `2026-06-04--22-39-15`.
  - Inspected the generated `munin-cgi-graph` wrapper and confirmed `CGI`,
    `CGIFast`, and the patched `use lib` stanza are present.
  - Direct startup probe now reaches Munin runtime state and exits only with
    `[FATAL] munin_readconfig_part(datafile) - missing file`, confirming the
    Perl module startup failure is gone. The datafile condition remains a
    separate boot-order follow-up if it appears after deployment.

## 2026-06-04 Production/Staging vpsAdminOS and vpsAdmin Inputs

- Updated production vpsAdminOS using ConfCtl.
- Added local `vpsfree-cz-configuration` commit
  `5ed98885 inputs: update vpsadminosProduction to 0ac745ae`.
- Updated production and staging vpsAdmin using ConfCtl.
- Added local `vpsfree-cz-configuration` commit
  `33aee2db inputs: update vpsadminProduction, vpsadminStaging to 4f413dfd`.
- Pushed both `origin/2026-06-03-nixos-26-05-port` and `origin/master` to
  `33aee2db4623823665414b2717cbf2b16e4ce5ea`.
- Channel state after updates:
  - production `vpsadminosProduction`: `cb665cd2` -> `0ac745ae`
  - production `vpsadminProduction`: `5c2785b3` -> `4f413dfd`
  - staging `vpsadminStaging`: `5c2785b3` -> `4f413dfd`
  - staging `vpsadminosStaging` was already `0ac745ae`
  - `vpsadminServices` was already `4f413dfd` and was not changed.
- Validation:
  - `nix develop -c confctl inputs channel ls '{production,staging}'`
    confirmed production and staging channel revisions.
  - `nix develop -c confctl build 'cz.vpsfree/nodes/*/*'` was attempted
    without `-y`; ConfCtl listed the 13 target nodes and stopped at the
    confirmation prompt without building.
  - `nix develop -c confctl build -y 'cz.vpsfree/nodes/*/*'` evaluated inputs
    and attempted to build all 13 vpsAdminOS nodes, but local evaluation is
    blocked by missing operator secret
    `/secrets/nodes/initrd/ssh_host_ed25519_key`.
  - `nix develop -c confctl build -y 'cz.vpsfree/nodes/stg/*'` reached the
    same missing secret path for staging nodes, confirming the blocker comes
    from shared node netboot configuration rather than a specific production
    node.

## 2026-06-04 em1 vpsf-status Proxy Build Fix

- Fixed `cz.vpsfree/machines/em1` build after `vpsf-status` moved to its own
  flake-provided NixOS module.
- Added local `vpsfree-cz-configuration` commit
  `52697640 vpsf-status: publish service port metadata`.
- Pushed both `origin/2026-06-03-nixos-26-05-port` and `origin/master` to
  `52697640155ec5bcabc7e87b9dcc12f2f745af55`.
- Added `vpsf-status.port = 8080` to cluster service definitions.
- Published `vpsf-status` from `cz.vpsfree/machines/prg/apu` at
  `172.31.0.33`; its port comes from service definitions.
- Changed `configs/vpsf-status.nix` to configure the service from
  `confMachine.services.vpsf-status`.
- Changed `em1` nginx proxy to target the `apu` service metadata instead of
  local `config.services.vpsf-status`, which `em1` does not import.
- Validation:
  - `nix develop -c nixfmt --check ...` passed for all changed Nix files.
  - `nix develop -c confctl build -y cz.vpsfree/machines/em1` passed and
    produced generation `2026-06-04--23-09-11`.
  - Inspected the built nginx config and confirmed
    `proxy_pass http://172.31.0.33:8080;`.
  - `nix develop -c confctl build -y cz.vpsfree/machines/prg/apu` evaluated
    the machine but is blocked by unrelated missing local ISO
    `/srv/iso-images/systemrescue-11.01-amd64.iso`.

## 2026-06-05 Production/Staging nixpkgs 26.05 Inputs

- Replaced an incorrect manually created input-update commit with a ConfCtl
  generated commit.
- Rebased the generated commit on top of upstream
  `a67439e3 inputs: update vpsadminosOsStaging, vpsadminosStaging to
  62de2d8b`.
- Set production and staging nixpkgs channels to the current 26.05 revision
  using `confctl inputs channel set --commit --no-changelog --no-editor
  '{production,staging,nixos-stable}' nixpkgs
  6b316287bae2ee04c9b93c8c858d930fd07d7338`.
- Added local `vpsfree-cz-configuration` commit
  `fb184af9 inputs: set nixpkgsProduction, nixpkgsStaging to 6b316287`.
- Channel state after updates:
  - production `nixpkgsProduction`: `25f53830` -> `6b316287`
  - staging `nixpkgsStaging`: `25f53830` -> `6b316287`
  - staging `vpsadminosStaging`: `0ac745ae` -> `62de2d8b` from upstream
    `master`
  - `nixpkgsStable` in channel `nixos-stable` was checked and was already
    `6b316287`
- Validation:
  - ConfCtl-generated git commit hooks passed.
  - `git ls-remote https://github.com/NixOS/nixpkgs.git
    refs/heads/nixos-26.05` confirmed the current branch tip is
    `6b316287bae2ee04c9b93c8c858d930fd07d7338`.
  - `nix develop -c confctl inputs channel ls
    '{production,staging,nixos-stable}'` confirmed all three nixpkgs channels
    at `6b316287`.
  - `nix develop -c confctl build -y 'cz.vpsfree/nodes/*/*'` evaluated inputs
    and reached the build phase for all 13 vpsAdminOS nodes in one build group;
    the build was terminated intentionally after the build graph started.
    Repeated after rebasing; latest log:
    `.confctl/logs/2026-06-05--10-36-43-confctl-build.log`.

## 2026-06-05 llm-agents Input

- Updated channel `llm-agents` using
  `nix develop -c confctl inputs channel update --commit --no-changelog
  --no-editor llm-agents llm-agents`.
- Added local `vpsfree-cz-configuration` commit
  `ff7aac11 inputs: update llm-agents to f764eba1`.
- Channel state after update:
  - `llm-agents`: `096ee16c` -> `f764eba1`
- Validation:
  - ConfCtl-generated git commit hooks passed.
  - `nix develop -c confctl inputs channel ls
    '{production,staging,nixos-stable,llm-agents}'` confirmed the expected
    channel revisions.
- Pushed `origin/2026-06-03-nixos-26-05-port` and fast-forwarded
  `origin/master` to `ff7aac116c139505468c8c53a80943b57bb7fdf1`.

## Cleanup

- Removed all initiative worktrees under
  `worktrees/2026-06-03-nixos-26-05-port/`:
  `confctl`, `ruby-lxc`, `vpsadmin`, `vpsadminos`,
  `vpsfree-cz-configuration`, and `zfs`.
- Deleted temporary local merge branches:
  `merge-2026-06-03-nixos-26-05-port-confctl-master`,
  `merge-2026-06-03-nixos-26-05-port-vpsadmin-master`, and
  `merge-2026-06-03-nixos-26-05-port-vpsfree-cz-configuration-master`.
- Kept feature branches as requested by workspace policy:
  `2026-06-03-nixos-26-05-port` in all affected repositories.

## Archival request, 2026-10-06

The workspace operator requested archival of sessions dated August 2026 or
older, retaining recorded work and branches. This checkpoint commits the
existing plan and active state before the ordinary archive transition.
