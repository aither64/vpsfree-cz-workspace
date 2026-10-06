---
lifecycle: abandoned
---
# 2026-06-10-ruby-gems-without-repository

## Repositories

- `vpsadminos`
  - Worktree: `worktrees/2026-06-10-ruby-gems-without-repository/vpsadminos`
  - Branch: `2026-06-10-ruby-gems-without-repository`
  - Base: `staging`
- `vpsadmin`
  - Worktree: `worktrees/2026-06-10-ruby-gems-without-repository/vpsadmin`
  - Branch: `2026-06-10-ruby-gems-without-repository`
  - Base: `master`
- `vpsfree-cz-configuration`
  - Worktree:
    `worktrees/2026-06-10-ruby-gems-without-repository/vpsfree-cz-configuration`
  - Branch: `2026-06-10-ruby-gems-without-repository`
  - Base: `master`
  - Status: unchanged
- `confctl`
  - Worktree: `worktrees/2026-06-10-ruby-gems-without-repository/confctl`
  - Branch: `2026-06-10-ruby-gems-without-repository`
  - Base: `master`
- `terraform-provider-vpsadmin`
  - Worktree:
    `worktrees/2026-06-10-ruby-gems-without-repository/terraform-provider-vpsadmin`
  - Branch: `2026-06-10-ruby-gems-without-repository`
  - Base: `master`
- `vpsf-status`
  - Worktree: `worktrees/2026-06-10-ruby-gems-without-repository/vpsf-status`
  - Branch: `2026-06-10-ruby-gems-without-repository`
  - Base: `master`
- `vpsfree-irc-bot`
  - Worktree:
    `worktrees/2026-06-10-ruby-gems-without-repository/vpsfree-irc-bot`
  - Branch: `2026-06-10-ruby-gems-without-repository`
  - Base: `master`
- `web`
  - Worktree: `worktrees/2026-06-10-ruby-gems-without-repository/web`
  - Branch: `2026-06-10-ruby-gems-without-repository`
  - Base: `master`

## Status

- Implemented in `vpsadminos` and `vpsadmin`.
- Downstream default-branch test-runner consumers have been migrated to the
  flake-backed `lib.testFramework` API and pushed.
- Replaced the disliked vpsAdminOS pure fallback commit with a public framework
  object exported by vpsAdminOS. Consumers call `testFramework.makeTest` and
  `testFramework.makeTestLib`; the object carries `sourcePath`, `netlinkrb`,
  and `ruby-lxc`.
- Changes are committed in logical steps.
- `vpsfree-cz-configuration` was not changed. The private gem repository can
  remain for old builds and unrelated packages.
- Rewritten replacement branches have been force-pushed after canceling
  superseded queued/in-progress CI runs. New CI runs are being monitored.

## Commits

- Workspace coordination repo:
  - `e3772b8` `docs: update Ruby gem packaging workflow`
- `vpsadminos`:
  - `c8fa25fee` `os-bundler-app: tolerate packages without manpages`
  - `1f157f6af` `ruby: package gems from local sources`
  - `fb2ba4d42` `os: update packaged gem dependencies`
  - `b5903ca86` `docs: describe local gem packaging`
  - `3d3142ab0` `ci: add daily gem dependency update`
  - `97daa38c7` `ci: build ruby-lxc extension for RSpec`
  - `d176829d9` `ci: allow manual CI runs`
  - `8a55d8661` `os: include Ruby source gems in installer channel`
  - `aa89665fa` `tests: expose flake-backed test framework API`
  - `8b0f7e0e0` `tests: split NixOS qemu VM defaults from base config`
- `vpsadmin`:
  - `578c63b0d` `ruby: package nodectl gems from local sources`
  - `6d12fa1bd` `packages: update nodectl gem dependencies`
  - `b901ed3e3` `docs: document nodectl gem metadata refresh`
  - `205a1d454` `ci: update nodectl gem dependencies daily`
  - `fc8a142f3` `flake: vpsadminos 715b58e95 -> c7ce73f0d`
  - `fec8b9dde` `flake: vpsadminos c7ce73f0d -> d8036a848`
  - `6ddd78c05` `flake: vpsadminos d8036a848 -> 8a55d8661`
  - `4a68957da` `tests: use vpsAdminOS test framework API`
  - `e588b2478` `flake: vpsadminos aa89665fa -> 8b0f7e0e0`
- `confctl`:
  - `4002d60` `tests: use vpsAdminOS test framework API`
  - `cc5e24a` `flake: vpsadminos aa89665fa -> 8b0f7e0e0`
- `terraform-provider-vpsadmin`:
  - `f759611` `tests: use vpsAdminOS test framework API`
  - `32e93d2` `flake: vpsadmin 4a68957da -> e588b2478`
- `vpsf-status`:
  - `dff42e5` `tests: use vpsAdminOS test framework API`
  - `dd06ceb` `flake: vpsadmin 4a68957da -> e588b2478`
- `vpsfree-irc-bot`:
  - `b4bfeed` `tests: use vpsAdminOS test framework API`
  - `7307c0d` `flake: vpsadmin 4a68957da -> e588b2478`
- `web`:
  - `990cd02` `tests: use vpsAdminOS test framework API`
  - `21598d9` `flake: vpsadmin 4a68957da -> e588b2478`

## vpsAdminOS changes

- Added non-flake inputs:
  - `netlinkrb` from `github:vpsfreecz/netlinkrb`
  - `ruby-lxc` from `github:vpsfreecz/ruby-lxc/2026-06-03-nixos-26-05-port`
- `os/overlays/osctl.nix` now source-builds:
  - vpsAdminOS Ruby gems from the local repository
  - `netlinkrb` and `ruby-lxc` from flake inputs
- `os/overlays/osctl.nix` no longer fetches `netlinkrb` or `ruby-lxc` with
  duplicate `fetchFromGitHub` calls.
- `os/default.nix` passes flake inputs to overlays, with a fallback for direct
  imports used by tests.
- `os/packages/ruby-source-gem-config.nix` builds source gems without creating
  a git repository.
- vpsAdminOS gemspecs now use deterministic `Dir[...]` file lists instead of
  `git ls-files`.
- vpsAdminOS gem versions no longer include `OS_BUILD_ID`.
- Source Gemfiles use local path dependencies for first-party gems.
- `osctld` source Gemfile uses `NETLINKRB_PATH` and `RUBY_LXC_PATH` for native
  extension dependencies from flake inputs.
- `tools/update_gem.rb` now refreshes lockfiles and gemsets locally and
  normalizes committed metadata. It does not build, upload, or use build IDs.
  The updater resolves flake inputs, rewrites temporary path dependencies, and
  formats generated Nix with `nixfmt`.
- `Makefile` gem targets now refresh/commit local metadata and no longer use
  `.build_id`.
- `os/packages/os-bundler-app/default.nix` now creates an empty `share/man`
  directory when the wrapped app has no man output. This avoids broken symlinks
  rejected by newer `buildEnv`.
- `AGENTS.md` and docs now describe local metadata refreshes instead of remote
  gem builds/uploads.
- Added `.github/workflows/daily-update.yml` to run `make gems` daily and on
  manual dispatch. The workflow pushes to the selected ref so branch dispatch
  can update a feature branch instead of `staging`.
- `lib.testFramework` now exports a flake-backed framework object with:
  - `sourcePath`
  - `sourceInputs.netlinkrb`
  - `sourceInputs.ruby-lxc`
  - `makeTest`
  - `makeTemplate`
  - `makeTestLib`
- `lib.testFramework.mkTests` and `mkTestsMeta` pass this framework object to
  consumer `tests/all-tests.nix` files. `tests/make-test.nix` consumes
  `testFramework.sourceInputs` when importing `os/`.
- The previous `os/default.nix` lockfile/fetchTree fallback and the later
  private suite-argument propagation were removed from the feature branch.
  Flake/test-framework evaluation now passes inputs explicitly through the
  framework object.
- `tests/configs/nixos/base.nix` no longer sets qemu-vm-only
  `virtualisation.*` defaults. Those defaults moved to
  `tests/configs/nixos/test-vm.nix`, which `tests/make-test.nix` imports only
  after NixOS `virtualisation/qemu-vm.nix`.

## vpsAdmin changes

- `packages/ruby-source-gem-config.nix` builds source gems without creating a
  git repository.
- `nixos/overlays/default.nix` source-builds:
  - `libnodectld`, `nodectl`, and `nodectld` from vpsAdmin source
  - `libosctl`, `osctl`, and `osctl-exportfs` from `vpsadminosPath`
- vpsAdmin modules pass `vpsadminosPath` into the overlay import.
- `flake.nix` derives the vpsAdminOS gem version from the vpsAdminOS input and
  sets default `VPSADMINOS_PATH` and `VPSADMINOS_GEM_VERSION` in dev shells.
- `tools/vpsadminos.rb` no longer exposes build IDs. It exports
  `VPSADMINOS_PATH` and `VPSADMINOS_GEM_VERSION`.
- nodectl/nodectld Gemfiles use local path dependencies for vpsAdminOS and
  vpsAdmin source gems.
- nodectl/nodectld gemspecs use deterministic file lists and plain versions.
- `tools/update_gem.rb` now refreshes lockfiles and gemsets locally and
  normalizes committed metadata.
- `rake vpsadmin:gems` now refreshes local package metadata and no longer
  builds/uploads gems.
- Removed the unused cronie package and scheduling module. The vpsAdmin API
  scheduler module no longer overlays `pkgs.cron` or enables `services.cron`.
- `AGENTS.md` now documents refreshing nodectl package metadata from local
  sources and vpsAdminOS flake inputs.
- Extended `.github/workflows/daily-update.yml` with `workflow_dispatch`, made
  the gem-dependency step run `rake vpsadmin:gems`, and changed the final push
  to the selected ref so manual dispatch can test feature branches.
- Manual vpsAdmin dispatch defaults to `scope=gems`, can run `scope=webui` or
  `scope=all`, and accepts an optional `vpsadminos_input` flake override so
  nodectl metadata can be tested against an unmerged vpsAdminOS branch.
- vpsAdmin tests now consume vpsAdminOS through the flake-exported
  `testFramework` object instead of passing `vpsadminosPath` through
  `suiteArgs`. Cluster helper imports retain a compatibility fallback for
  downstream suites that still pass `vpsadminosPath` directly.

## Commands run

- `bin/dev-session current`
  - Result: active slug is `2026-06-10-ruby-gems-without-repository`.
- `bin/dev-session worktree add ... vpsadminos ... --base staging`
  - Result: worktree checked out. Helper exited nonzero because the ambient
    shell lacked the repository hook dependencies.
- `bin/dev-session worktree add ... vpsadmin ... --base master`
  - Result: worktree checked out. Helper exited nonzero because the ambient
    shell lacked the repository hook dependencies.
- `bin/dev-session worktree add ... vpsfree-cz-configuration ... --base master`
  - Result: worktree checked out. Helper exited nonzero because the ambient
    shell lacked the repository hook dependencies.
- `nix develop .#vpsadminos --command ruby -v`
  - Result: installed the vpsAdminOS development bundle/Overcommit
    environment.
- `nix flake lock` in `vpsadminos`
  - Result: added non-flake inputs `netlinkrb` and `ruby-lxc`.
- `nix shell nixpkgs#nixfmt-rfc-style -c nixfmt ...`
  - Result: formatted changed Nix files in both repositories during early
    development. The updater and Makefile now call only `nixfmt`.
- `nix develop .#vpsadminos --command bash -lc 'make gems'`
  - Result: regenerated all vpsAdminOS package `Gemfile.lock` and `gemset.nix`
    files without the private gem repository or build IDs.
- `nix develop .#vpsadmin --command bash -lc 'VPSADMINOS_PATH=../vpsadminos VPSADMINOS_GEM_VERSION=26.05.0 BUNDLED_WITH=2.7.2 rake vpsadmin:gems'`
  - Result: regenerated vpsAdmin `libnodectld`, `nodectl`, and `nodectld`
    package metadata against the local vpsAdminOS source tree.
- `nix develop .#vpsadminos --command ruby -c tools/update_gem.rb`
  - Result: syntax OK.
- `nix develop .#vpsadmin --command ruby -c tools/update_gem.rb`
  - Result: syntax OK.
- `nix develop .#vpsadmin --command ruby -c tools/vpsadminos.rb`
  - Result: syntax OK.
- `nix develop .#vpsadmin --command ruby -c tasks/release.rb`
  - Result: syntax OK.
- `nix develop .#vpsadminos --command ruby -e ...` compiling selected
  gemspecs
  - Result: passed.
- vpsAdminOS package build for:
  - `osctl`, `osctld`, `osctl-env-exec`, `osctl-exporter`,
    `osctl-exportfs`, `osctl-image`, `osctl-oomd`, `osctl-repo`, `osup`,
    `osvm`, `svctl`, `test-runner`
  - Result: passed after the `os-bundler-app` fix.
- Direct `svctl` `buildEnv` check with `pathsToLink = [ "/bin" "/share/man" ]`
  - Result: passed.
- vpsAdmin package build with local vpsAdminOS source overlay for:
  - `libnodectld`, `nodectl`, `nodectld`
  - Result: passed.
- `osctl --version` from the built vpsAdminOS package
  - Result: `osctl version 26.05.0`.
- `nodectl --help` from the built vpsAdmin package
  - Result: exited 0 and printed command usage.
- Metadata checks:
  - vpsAdminOS package lockfiles have exactly one `GEM` section.
  - vpsAdmin node package lockfiles have exactly one `GEM` section.
  - No forbidden matches for `rubygems.vpsfree.cz`, build IDs, `OS_BUILD_ID`,
    `PATH`, `CHECKSUMS`, or `type = "path"` in the touched package metadata.
- `git diff --check && git diff --cached --check`
  - Result: passed in both `vpsadminos` and `vpsadmin` after normalizing extra
    blank lines at EOF in generated package Gemfiles.
- `nix build --no-link --impure --expr ...` in `vpsadminos` for the affected
  Ruby package set
  - Result: passed after rewriting `tools/update_gem.rb`.
- `nix build --no-link --impure --expr ...` in `vpsadmin` for `libnodectld`,
  `nodectl`, and `nodectld` against the local vpsAdminOS source input
  - Result: passed after rewriting `tools/update_gem.rb` and removing cronie.
- `git diff --check && git diff --cached --check`
  - Result: passed in `vpsadminos`, `vpsadmin`, and the workspace root after
    final validation.
- Verified workflow action refs from official upstream git tags:
  - `actions/checkout@v6`; latest published v6 tag seen was `v6.0.3`.
  - `cachix/install-nix-action@v31`; latest published v31 tag seen was
    `v31.10.6`.
  - `ruby/setup-ruby@v1`; latest published v1 tag seen was `v1.312.0`.
- `ruby -e 'require "yaml"; YAML.load_file(...)'` for the changed daily
  workflow in both repositories
  - Result: passed.
- `nix shell nixpkgs#actionlint -c actionlint .github/workflows/daily-update.yml`
  in both repositories
  - Result: passed.
- `nix develop .#vpsadminos --command bash -lc 'make gems'`
  - Result: passed while validating the new vpsAdminOS workflow command; it
    produced no package metadata diffs.
- vpsAdmin workflow command validation with a temporary local vpsAdminOS input
  override:
  `./tools/bundix_all.sh && rake vpsadmin:gems && nixfmt packages/*/gemset.nix`
  - First result: failed because stale `.gems` native extensions were linked
    against an older Ruby ABI.
  - Fix: removed the local `.gems` cache and restored validation-only package
    metadata diffs.
  - Second result: passed. Remaining validation-only package diffs were
    restored, leaving only the workflow edit.
- Pushed `vpsadminos` branch
  `2026-06-10-ruby-gems-without-repository` to origin.
- Pushed `vpsadmin` branch
  `2026-06-10-ruby-gems-without-repository` to origin.
- `gh workflow run daily-update.yml --ref 2026-06-10-ruby-gems-without-repository`
  in `vpsadminos`
  - Result: failed with HTTP 404 because the new workflow file is not present
    on the default branch yet. GitHub does not expose newly added workflows
    for manual dispatch until they exist on the default branch.
- First vpsAdmin manual dispatch:
  `gh workflow run daily-update.yml --ref 2026-06-10-ruby-gems-without-repository`
  - Result: passed at
    `https://github.com/vpsfreecz/vpsadmin/actions/runs/27357228705`.
  - The run pushed generated `packages: update gem dependencies` and
    `webui: update dependencies` commits. They were removed from the feature
    branch with `git push --force-with-lease` because the run used the old
    committed vpsAdminOS flake input and the webui update was unrelated.
- Amended the vpsAdmin workflow commit to add manual `scope` and
  `vpsadminos_input` inputs.
- Second vpsAdmin manual dispatch:
  `gh workflow run daily-update.yml --ref 2026-06-10-ruby-gems-without-repository -f scope=gems -f vpsadminos_input=github:vpsfreecz/vpsadminos/2026-06-10-ruby-gems-without-repository`
  - Result: passed at
    `https://github.com/vpsfreecz/vpsadmin/actions/runs/27357752072`.
  - The `Update webui dependencies` step was skipped as intended.
  - The run pushed an unrelated API package dependency update
    (`net-imap` and `rubocop-rspec`). It was removed from the feature branch
    with `git push --force-with-lease` to keep the branch scoped.
- Ambient `git restore --staged -- .` in `vpsadminos` and `vpsadmin`
  - Result: failed because the installed Overcommit wrapper could not find the
    `overcommit` gem outside the Nix dev shell. Git staging and commits were
    then run through each repository's `nix develop` shell so hooks remained
    active.

## Rebase and CI follow-up

- `vpsadminos` was rebased onto current `origin/staging`
  `c2f5575a0` and pushed to origin.
- `vpsadmin` was rebased onto current `origin/master` `eb9c9dd6b` and pushed
  to origin. The earlier cronie-removal commit was skipped by rebase because
  the removal was already present upstream.
- vpsAdmin `flake.lock` was updated with `tools/update_vpsadminos_flake.sh` to
  pin vpsAdminOS commit `d8036a84821bdfe9e21c4a0c5001b96f6178375f`. Running
  `rake vpsadmin:gems` after the pin produced no package metadata diffs.
- Superseded GitHub Actions runs were canceled where possible before the
  rewritten branches were pushed. Canceled runs included vpsAdminOS CI
  `27358629065` and vpsAdmin CI `27358738646`.
- The first post-push vpsAdminOS RSpec run failed because Bundler path
  dependencies do not build the `ruby-lxc` native extension. Commit
  `d8036a848` builds the extension into `.native/ruby-lxc` before running
  osctld specs.
- Local vpsAdminOS RSpec validation passed with:
  `rm -rf .native .gems && nix develop .#vpsadminos --command bash -lc 'GITHUB_WORKSPACE=$PWD bash .github/workflows/scripts/run-rspec-all.sh'`
  - Result: all suites passed, including `osctld` with `1012 examples, 0
    failures`.
- Remote vpsAdminOS RSpec run
  `https://github.com/vpsfreecz/vpsadminos/actions/runs/27359462186`
  passed on `d8036a848`.
- vpsAdminOS CI was made manually dispatchable in commit `beb729349`.
  Validation before commit:
  - `ruby -e 'require "yaml"; YAML.load_file(".github/workflows/ci.yml")'`
    passed.
  - `nix shell nixpkgs#actionlint -c actionlint .github/workflows/ci.yml`
    passed after quoting `$GITHUB_OUTPUT` and `$GITHUB_ENV`.
  - `nix develop .#vpsadminos --command overcommit --run` passed.
- Pushing `beb729349` automatically reran vpsAdminOS CI at
  `https://github.com/vpsfreecz/vpsadminos/actions/runs/27361934921`.
  As of 2026-06-11 19:35 Europe/Amsterdam:
  - Build OS and populate binary cache: passed.
  - Run test suite: still in progress in the `Run tests` step.
- Current vpsAdmin runs on `fec8b9dde`:
  - `libnodectld Specs`
    `https://github.com/vpsfreecz/vpsadmin/actions/runs/27359547971`: passed.
  - `Webui PHPUnit`
    `https://github.com/vpsfreecz/vpsadmin/actions/runs/27359548032`: passed.
  - `Client Specs`
    `https://github.com/vpsfreecz/vpsadmin/actions/runs/27359547992`: passed.
  - `CI`
    `https://github.com/vpsfreecz/vpsadmin/actions/runs/27359548024`: still
    in progress in the `Run tests` step as of 2026-06-11 19:35
    Europe/Amsterdam. GitHub does not expose logs for this job until it
    completes.

## Integration tests

- `nix run --override-input vpsadminos ../vpsadminos .#test-runner -- test --state-dir /tmp/vpsadmin-test-runner-ruby-gems-local -f admin/nodectl-refresh-and-runtime-state`
  - Result: failed because the nested test evaluation still used the locked
    old vpsAdminOS input, whose gemspecs still depended on `git`.
- Temporary vpsAdmin lock override without `--allow-dirty-locks`
  - Result: did not replace the nested locked input as intended.
- Temporary vpsAdmin lock override with
  `nix flake lock --allow-dirty-locks --override-input vpsadminos ../vpsadminos`
  and automatic lockfile restoration
  - First result: failed building vpsAdmin `packages/cronie` against the newer
    nixpkgs input because of a stricter callback prototype diagnostic.
  - Fix: removed the unused cronie package and scheduler wiring instead of
    carrying a patch for a package vpsAdmin no longer uses.
  - Second result: failed building the vpsAdminOS system path because
    `svctl/share/man` was a broken symlink.
  - Fix: patch `os/packages/os-bundler-app/default.nix`.
  - Final result:
    `./test-runner.sh test --state-dir /tmp/vpsadmin-test-runner-ruby-gems-local-lock5 -f admin/nodectl-refresh-and-runtime-state`
    passed with `1 tests successful` in 355.34 seconds.

The temporary `flake.lock` override was restored after each run.

- `./test-runner.sh test --state-dir /tmp/vpsadminos-test-runner-ruby-gems-driver-current -f driver/vpsadminos`
  - Result: passed with `1 tests successful` in 899.6 seconds after the Ruby
    updater rewrite and regenerated package metadata.
- Temporary vpsAdmin lock override with
  `nix flake lock --allow-dirty-locks --override-input vpsadminos ../vpsadminos`
  and automatic lockfile restoration
  - `./test-runner.sh test --state-dir /tmp/vpsadmin-test-runner-ruby-gems-nodectl-current -f admin/nodectl-refresh-and-runtime-state`
    passed with `1 tests successful` in 378.28 seconds.
  - `./test-runner.sh test --state-dir /tmp/vpsadmin-test-runner-ruby-gems-scheduler-current -f admin/scheduler-socket-control`
    passed with `1 tests successful` in 472.6 seconds.
  - The vpsAdmin `flake.lock` was restored cleanly after the test command.

## Downstream test-runner consumers

- Searched default upstream refs for vpsAdminOS test-runner/test-framework
  consumers.
- Direct `vpsadminos` consumer:
  - `confctl`
- Consumers through `vpsadmin` and `vpsadminos.follows = "vpsadmin/vpsadminos"`:
  - `terraform-provider-vpsadmin`
  - `vpsf-status`
  - `vpsfree-irc-bot`
  - `web`
- `vpsfree-cz-configuration`, `vpsadminos-org-configuration`, and
  `vpsfree-mail-templates` were checked earlier and do not use the test
  framework on their default branches.
- The first downstream worktree creation used stale local `master` refs.
  All five downstream feature branches were rebased onto current
  `origin/master` before editing lockfiles.
- `confctl` exposed a vpsAdminOS compatibility issue during pure check
  evaluation:
  `cannot call 'getFlake' on unlocked flake reference '/nix/store/...-source'`.
  Root cause: `os/default.nix` used `builtins.getFlake` as the fallback for
  `netlinkrb` and `ruby-lxc` when vpsAdminOS modules were imported directly
  from the flake source path. The first fix added a lockfile/fetchTree
  fallback, but it was replaced with commit `6a525f7c3`, which passes the
  source inputs through private test-framework state instead.
- vpsAdminOS `system/install` was rerun locally after the installer channel
  fix:
  `./test-runner.sh test 'system/install'`
  - Result: passed, `1 tests successful` in 2021.24 seconds.
- vpsAdminOS replacement input-propagation validation:
  - `nix eval --json .#testsMeta.x86_64-linux --no-write-lock-file`
    returned 127 tests.
  - `nix eval --json --override-input vpsadminos path:../vpsadminos
    .#checks.x86_64-linux."carrier/deploy".drvPath --no-write-lock-file`
    in `confctl` returned a derivation path.
  - `./test-runner.sh test defaults` in `vpsadminos` passed with
    `1 tests successful` in 214.88 seconds.
  - `nix develop .#vpsadminos --command overcommit --run` passed.
- Rewrote and force-pushed replacement commits after canceling superseded
  queued/in-progress CI runs:
  - `vpsadminos`: `a2e3302ce` replaced by `6a525f7c3`.
  - `vpsadmin`: `1f378a6f7` replaced by `83b004e60`.
  - `confctl`: `a671934` replaced by `8a95a93`.
  - `terraform-provider-vpsadmin`: `43d662f` replaced by `2def7ac`.
  - `vpsf-status`: `2936703` replaced by `9ea2412`.
  - `vpsfree-irc-bot`: `9c8e71f` replaced by `ecc281b`.
  - `web`: `bc75a54` replaced by `c9ccd23`.
- Superseded GitHub Actions runs canceled before force-push:
  - `vpsadminos` CI `27370597355`.
  - `vpsadmin` CI `27370773389`.
  - `confctl` Tests `27371439376`.
  - `vpsf-status` Integration Tests `27371434078`.
  - `vpsfree-irc-bot` Integration Tests `27371437875`.
- Replacement downstream validation after lock rewrites:
  - `confctl`: pure eval of
    `.#checks.x86_64-linux."carrier/deploy".drvPath` passed.
  - `terraform-provider-vpsadmin`: `./test-runner.sh ls --filter 'tag=ci'`
    listed `workflows`.
  - `vpsf-status`: `./test-runner.sh ls --filter 'tag=ci'` listed
    `status-page`.
  - `vpsfree-irc-bot`: `./test-runner.sh ls --filter 'tag=ci'` listed
    `irc-basic` and `vpsadmin-events`.
  - `web`: `./test-runner.sh ls --filter 'tag=ci'` listed `web`.
- Downstream validation after final pins:
  - `confctl`: built `.#packages.x86_64-linux.test-runner`, listed 5
    CI-tagged tests, evaluated
    `.#checks.x86_64-linux."carrier/deploy".drvPath`, built
    `.#packages.x86_64-linux.confctl`, and ran Overcommit.
  - `terraform-provider-vpsadmin`: built
    `.#packages.x86_64-linux.test-runner`, listed 1 CI-tagged test, and ran
    `make test && make test-get-token` inside `nix develop`. The ambient
    shell failed first because `gcc` was missing; the Nix-shell rerun passed.
  - `vpsf-status`: built `.#packages.x86_64-linux.test-runner`, listed 1
    CI-tagged test, ran `go test ./...` inside `nix develop`, built
    `.#packages.x86_64-linux.vpsf-status`, installed Lefthook with
    `make hooks`, and ran `lefthook run pre-commit`.
  - `vpsfree-irc-bot`: listed 2 CI-tagged tests, built
    `.#packages.x86_64-linux.vpsfree-irc-bot`, ran `bundle exec rspec`
    inside `nix develop`, and ran `bundle exec overcommit --run`.
  - `web`: built `.#packages.x86_64-linux.test-runner`, listed 1 CI-tagged
    test, and built `.#checks.x86_64-linux.validator-tests`.
- Hook notes:
  - `confctl` had a stale `.gems` cache linked against Ruby 3.4.8 while the
    dev shell used Ruby 3.4.9. Removed the transient `.gems`/`.bin` cache and
    reran `bundle install && bundle exec overcommit --run`.
  - `vpsfree-irc-bot` Overcommit is available through Bundler in the dev shell,
    so hooks were run with `bundle exec overcommit --run`.
- Pushed downstream branches:
  - `confctl`: `2026-06-10-ruby-gems-without-repository`
  - `terraform-provider-vpsadmin`: `2026-06-10-ruby-gems-without-repository`
  - `vpsf-status`: `2026-06-10-ruby-gems-without-repository`
  - `vpsfree-irc-bot`: `2026-06-10-ruby-gems-without-repository`
  - `web`: `2026-06-10-ruby-gems-without-repository`

## Final framework API update

- Replaced the private `_vpsadminosTestFramework` suite-argument design with
  a public `lib.testFramework` framework object in vpsAdminOS.
- vpsAdminOS final framework commit:
  `aa89665fae38f0f79c2691d3658773b070cd0bc9`
  `tests: expose flake-backed test framework API`.
- vpsAdminOS final test-base compatibility commit:
  `8b0f7e0e072d16be0797827d98b1acbc6b7f355e`
  `tests: split NixOS qemu VM defaults from base config`.
- vpsAdmin final consumer commit:
  `4a68957da8120014476b159d4bb6208bb4ba7879`
  `tests: use vpsAdminOS test framework API`.
- vpsAdmin final lock follow-up:
  `e588b247814013f7114857e8126f1daf297da137`
  `flake: vpsadminos aa89665fa -> 8b0f7e0e0`.
- Downstream final consumer commits:
  - `confctl`: `4002d60` `tests: use vpsAdminOS test framework API`
  - `confctl`: `cc5e24a`
    `flake: vpsadminos aa89665fa -> 8b0f7e0e0`
  - `terraform-provider-vpsadmin`: `f759611`
    `tests: use vpsAdminOS test framework API`
  - `terraform-provider-vpsadmin`: `32e93d2`
    `flake: vpsadmin 4a68957da -> e588b2478`
  - `vpsf-status`: `dff42e5`
    `tests: use vpsAdminOS test framework API`
  - `vpsf-status`: `dd06ceb`
    `flake: vpsadmin 4a68957da -> e588b2478`
  - `vpsfree-irc-bot`: `b4bfeed`
    `tests: use vpsAdminOS test framework API`
  - `vpsfree-irc-bot`: `7307c0d`
    `flake: vpsadmin 4a68957da -> e588b2478`
  - `web`: `990cd02` `tests: use vpsAdminOS test framework API`
  - `web`: `21598d9` `flake: vpsadmin 4a68957da -> e588b2478`
- Superseded vpsAdmin CI run `27373134647` on `83b004e60` was canceled before
  the final vpsAdmin force-push. No active superseded downstream runs were
  present before the final downstream force-pushes.
- Root cause of the confctl failure exposed by the final lock update:
  vpsAdminOS commit `8dfaa2698` added `virtualisation.fileSystems` to the
  shared NixOS test base for NixOS 26.05 direct-boot VM tests. Confctl imports
  that same base into normal generated NixOS deployment configurations, where
  qemu-vm-only options such as `virtualisation.fileSystems` are not declared.
  The fix keeps qemu-vm defaults in `tests/configs/nixos/test-vm.nix`, imported
  only by the vpsAdminOS test runner after `qemu-vm.nix`.
- Final local validation:
  - vpsAdminOS: `nix eval --json .#testsMeta.x86_64-linux
    --no-write-lock-file` returned 127 tests.
  - vpsAdminOS: `./test-runner.sh test defaults` passed with
    `1 tests successful` in 185.68 seconds.
  - vpsAdminOS: `./test-runner.sh test driver/nixos` passed with
    `1 tests successful` in 126.65 seconds after the NixOS base split.
  - vpsAdminOS: `nix develop .#vpsadminos --command overcommit --run` passed.
  - vpsAdmin: `nix eval --json .#testsMeta.x86_64-linux
    --no-write-lock-file` returned 117 tests.
  - vpsAdmin: `./test-runner.sh test services-up` passed with
    `1 tests successful` in 398.85 seconds.
  - `confctl`: `./test-runner.sh test deploy/flakes` passed with
    `1 tests successful` in 794.15 seconds using the local vpsAdminOS split
    before the pushed SHA was available.
  - `confctl`: pure eval of
    `.#checks.x86_64-linux."carrier/deploy".drvPath` passed.
  - `terraform-provider-vpsadmin`: real-lock `testsMeta` eval listed
    `workflows`.
  - `vpsf-status`: real-lock `testsMeta` eval listed `status-page`.
  - `vpsfree-irc-bot`: real-lock `testsMeta` eval listed `irc-basic` and
    `vpsadmin-events`.
  - `web`: real-lock `testsMeta` eval listed `web`.

## Current CI monitoring

As of 2026-06-12 01:05 Europe/Amsterdam:

- `vpsadminos`
  - CI `27380541917` on `8b0f7e0e0`: in progress.
  - Previous CI `27376937355` on `aa89665fa`: passed.
  - RSpec `27376937371` on `aa89665fa`: passed.
- `vpsadmin`
  - CI `27380608211` on `e588b2478`: in progress.
  - `libnodectld Specs` `27380608176` on `e588b2478`: passed.
  - `Client Specs` `27380608202` on `e588b2478`: passed.
  - `Webui PHPUnit` `27380608215` on `e588b2478`: passed.
  - Superseded CI `27377871235` on `4a68957da`: canceled before pushing
    `e588b2478`.
- `confctl`
  - Tests `27380904669` on `cc5e24a`: queued.
  - RSpec `27380904681` on `cc5e24a`: passed.
  - RuboCop `27380904660` on `cc5e24a`: passed.
  - Previous Tests `27377994856` on `4002d60`: failed with the
    `virtualisation.fileSystems` issue fixed by `8b0f7e0e0`.
- `terraform-provider-vpsadmin`
  - Integration Tests `27380902099` on `32e93d2`: in progress.
- `vpsf-status`
  - Integration Tests `27380902212` on `dd06ceb`: queued.
- `vpsfree-irc-bot`
  - RSpec `27380905320` on `7307c0d`: passed.
  - Integration Tests `27380905255` on `7307c0d`: passed.
- `web`
  - Integration Tests `27380902721` on `21598d9`: queued.

## Known follow-up

- No remaining design follow-up is known for the test-framework packaging
  issue. The final design exposes the needed source/input context as a
  first-class vpsAdminOS flake API and updates all default-branch consumers in
  this workspace.
- The Ruby test-runner still uses legacy `nix-instantiate`/`nix-build`
  commands internally, but normal consumers now evaluate through flake outputs
  and do not need repository-specific fallbacks. Rewriting the runner internals
  to call `nix eval`/`nix build` directly would be a separate cleanup, not a
  blocker for this initiative.
- `vpsfree-cz-configuration` can be updated later if operators decide to remove
  the hosted gem repository. It is no longer needed by the touched package
  builds, but old branches may still use it.

## Cleanup

- No cleanup done yet.
- Integration-test state directories are under:
  - `/tmp/vpsadmin-test-runner-ruby-gems-local-lock3`
  - `/tmp/vpsadmin-test-runner-ruby-gems-local-lock4`
  - `/tmp/vpsadmin-test-runner-ruby-gems-local-lock5`
  - `/tmp/vpsadminos-test-runner-ruby-gems-driver-current`
  - `/tmp/vpsadmin-test-runner-ruby-gems-nodectl-current`
  - `/tmp/vpsadmin-test-runner-ruby-gems-scheduler-current`

## 2026-06-12 worktree recreation and cleanup planning

- The feature worktrees were accidentally removed and have been recreated from
  the bare repositories:
  - `worktrees/2026-06-10-ruby-gems-without-repository/vpsadminos`
  - `worktrees/2026-06-10-ruby-gems-without-repository/vpsadmin`
  - `worktrees/2026-06-10-ruby-gems-without-repository/confctl`
  - `worktrees/2026-06-10-ruby-gems-without-repository/terraform-provider-vpsadmin`
  - `worktrees/2026-06-10-ruby-gems-without-repository/vpsf-status`
  - `worktrees/2026-06-10-ruby-gems-without-repository/vpsfree-irc-bot`
  - `worktrees/2026-06-10-ruby-gems-without-repository/web`
- All recreated repository worktrees are clean and track
  `origin/2026-06-10-ruby-gems-without-repository`.
- Upstreams were fetched. `vpsadminos` is behind current `origin/staging`
  `14843dbb9` by three commits and ahead by ten commits. The other affected
  repositories are not behind their default upstream branches.
- `vpsadminos` CI `27380541917` on old feature head `8b0f7e0e0` completed
  with failure: 71 tests passed and `incus/fedora#latest`,
  `incus/debian#latest`, and `firewall/conntrack#conntrack` failed
  unexpectedly.
- The incus failures were caused by timeouts reaching
  `images.linuxcontainers.org` from inside the test container. The conntrack
  failure occurred before the branch was rebased onto current `staging`; current
  `staging` includes `5c3876223` `firewall: check installed iptables rules` and
  CI `27386586427` on that commit passed.
- Current cleanup direction for review: rebase `vpsadminos` onto current
  `staging`, drop or absorb duplicated upstream changes, replace intermediate
  flake input bumps in consumers with one final pin per dependency, and rewrite
  the top-level workspace `AGENTS.md` commit so the generic Ruby gem packaging
  instructions are removed instead of updated.

## 2026-06-12 vpsAdmin gem update task unification

- Implemented the requested vpsAdmin gem-update cleanup:
  - added `tasks/gem_updates.rb`;
  - moved `vpsadmin:gems` out of `tasks/release.rb`;
  - exposed `rake vpsadmin:gems` for all packages and per-package tasks under
    `vpsadmin:gems:<package>`;
  - removed the old `tools/bundix_*.sh`, `tools/update_gem.rb`, and
    `tools/vpsadminos.rb` helper scripts;
  - changed `.github/workflows/daily-update.yml` to call
    `rake vpsadmin:gems`;
  - kept `VPSADMINOS_INPUT` in the workflow as the explicit local source
    override for the generated nodectl/libnodectld/nodectld metadata update;
  - updated vpsAdmin `AGENTS.md` to document `rake vpsadmin:gems` and
    `rake -T vpsadmin:gems`.
- vpsAdmin commits pushed to
  `origin/2026-06-10-ruby-gems-without-repository`:
  - `862bcdca5` `packages: unify gem metadata updates under Rake`
  - `af07c5305` `packages: update gem dependencies`
- vpsAdmin validation:
  - `ruby -c tasks/gem_updates.rb`: passed.
  - `nix develop .#vpsadmin --command bash -lc 'rake -T vpsadmin:gems'`:
    passed and listed all public package tasks.
  - `nix develop .#vpsadmin --command bash -lc 'rake vpsadmin:gems:api'`:
    passed.
  - `nix develop .#vpsadmin --command bash -lc 'rake vpsadmin:gems:nodectl'`:
    passed.
  - `nix develop .#vpsadmin --command bash -lc 'rake vpsadmin:gems'`:
    passed and was idempotent.
  - `nix develop .#vpsadmin --command overcommit --run`: passed. The PHP hook
    autoformatted unrelated web UI files; those hook-created changes were
    restored before commit and push.
  - `nix eval --json .#testsMeta.x86_64-linux --no-write-lock-file`:
    returned 117 tests.
  - `git diff --check HEAD~2..HEAD`: passed.
- The generated vpsAdmin gem metadata update bumped `json` from `2.19.8` to
  `2.19.9` in package lock/gemset files. No console-router metadata changed.
- Superseded vpsAdmin CI run `27404064124` on `86f125c02` was cancelled before
  force-pushing `af07c5305`.

## 2026-06-12 downstream repin after vpsAdmin gem task cleanup

- Updated final downstream flake lock commits to point at vpsAdmin
  `af07c53052210ff681ae422d9629b89bd6d3eeb7`:
  - `terraform-provider-vpsadmin`: `0e9e236`
    `flake: vpsadmin c8fbfe38f -> af07c5305`
  - `vpsf-status`: `569459c`
    `flake: vpsadmin c8fbfe38f -> af07c5305`
  - `vpsfree-irc-bot`: `49f6645`
    `flake: vpsadmin c8fbfe38f -> af07c5305`
  - `web`: `1e61bda`
    `flake: vpsadmin eb9c9dd6b -> af07c5305`
- Before force-pushing these rewritten lock commits, checked that there were no
  queued or running Actions runs on the downstream feature branches.
- Downstream validation after the final vpsAdmin repin:
  - `terraform-provider-vpsadmin`:
    `nix eval --json .#testsMeta.x86_64-linux --no-write-lock-file` passed and
    listed `workflows`.
  - `vpsf-status`:
    `nix eval --json .#testsMeta.x86_64-linux --no-write-lock-file` passed and
    listed `status-page`.
  - `vpsfree-irc-bot`:
    `nix eval --json .#testsMeta.x86_64-linux --no-write-lock-file` passed and
    listed `irc-basic` and `vpsadmin-events`.
  - `web`:
    `nix eval --json .#testsMeta.x86_64-linux --no-write-lock-file` passed and
    listed `web`.
- Current CI status after final pushes:
  - `vpsadminos` head `6b768aaae`: RuboCop `27403628412`, RSpec
    `27403628391`, and CI `27403628399` all passed.
  - `confctl` head `7e288c8d`: RuboCop `27404551464`, RSpec `27404551478`,
    and Tests `27404551463` all passed.
  - `vpsadmin` head `af07c5305`: RuboCop `27406865171` passed; CI
    `27406865134` and API Specs `27406865176` are still running.
  - `terraform-provider-vpsadmin` head `0e9e236`: Integration Tests
    `27407029136` are running.
  - `vpsf-status` head `569459c`: Integration Tests `27407028703` are
    running.
  - `vpsfree-irc-bot` head `49f6645`: RSpec `27407042167` is running and
    Integration Tests `27407041980` are queued.
  - `web` head `1e61bda`: Integration Tests `27407029954` are queued.

## 2026-06-12 vpsadminos.org docs host verification

- Added `vpsadminos-org-configuration` to this initiative:
  - worktree:
    `worktrees/2026-06-10-ruby-gems-without-repository/vpsadminos-org-configuration`
  - branch: `2026-06-10-ruby-gems-without-repository`
- The relevant machine is `org.vpsadminos/int.www`. It publishes:
  - `www.vpsadminos.org` from a mkdocs `docsroot`;
  - `man.vpsadminos.org` from generated md2man HTML manuals;
  - `ref.vpsadminos.org` from YARD output for Ruby osctl components.
- Initial evaluation with the new vpsAdminOS packaging showed why this
  configuration needed a change:
  - `cluster/org.vpsadminos/int.www/config.nix` imported
    `${docsOs}/os/overlays/osctl.nix` directly without passing `netlinkrb` and
    `ruby-lxc`;
  - confctl machine modules pass `inputs.vpsadminos` as a source path, not as a
    full flake object, so full flake outputs must be read from `flakeInputs`.
- Implemented and pushed a vpsAdminOS flake API for this:
  - commit `6f9b2c755` `flake: expose vpsAdminOS overlays`;
  - exposes `overlays.all`, `overlays.default`, and individual
    `overlays.osctl`, `overlays.ruby`, `overlays.minify`, and
    `overlays.packages`;
  - reuses the shared overlay list in vpsAdminOS package/dev-shell outputs.
- Updated and pushed `vpsadminos-org-configuration`:
  - commit `ac8ad6b` `www: use vpsAdminOS flake overlays for docs`;
  - `int.www` now uses `flakeInputs.vpsadminos.overlays.osctl` and
    `flakeInputs.vpsadminos.overlays.ruby`;
  - `inputs.vpsadminos` remains the source path for docs/man source files;
  - `flake.lock` pins vpsAdminOS to
    `6f9b2c755143197bd9c3452e1c0121b22e978c4d` and records the new
    transitive `netlinkrb` and `ruby-lxc` flake inputs.
- Validation:
  - vpsAdminOS: `nix eval --json .#overlays --apply builtins.attrNames`
    returned `all`, `default`, `minify`, `osctl`, `packages`, and `ruby`.
  - vpsAdminOS: `nix develop .#vpsadminos --command overcommit --run` passed.
  - vpsadminos.org config:
    `nix develop --command overcommit --run` passed.
  - Local override build:
    `nix build --override-input vpsadminos ../vpsadminos --no-write-lock-file
    --no-link --print-out-paths
    .#confctl.toplevel.m_org_vpsadminos_int_www_27f4ac6e` passed and built
    `docsroot`, `vpsadminos-webmanuals`, and `ref-gems`.
  - Committed-lock build:
    `nix build --no-write-lock-file --no-link --print-out-paths
    .#confctl.toplevel.m_org_vpsadminos_int_www_27f4ac6e` passed and returned
    `/nix/store/mfwqz481dvxh8hqyc212qdjgmbp9k7mz-nixos-system-www-26.05.20260608.bd0ff2d`.
  - Generated-output spot checks passed:
    - mkdocs root contains `index.html`, search assets, CSS/JS, and the Matomo
      script;
    - man root contains `index.html`, `style.css`, and generated HTML/Markdown
      pages such as `man8/osctl.8.html` and `man1/test-runner.1.html`;
    - YARD ref root contains `index.html` for `libosctl`, `osctl`,
      `osctl-exportfs`, `osctl-image`, `osctl-repo`, `osctld`, `converter`,
      `osup`, `svctl`, `osvm`, and `test-runner`.
- CI status after the pushes:
  - vpsAdminOS head `6f9b2c755`: RSpec `27410841241` passed.
  - vpsadminos.org configuration has no push workflow; only
    `.github/workflows/daily-update.yml` exists, scheduled for default-branch
    input updates.
  - vpsAdmin head `af07c5305`: CI `27406865134`, RuboCop `27406865171`, and
    API Specs `27406865176` passed.

## 2026-06-12 final workflow status refresh

- `vpsadmin` head `af07c5305`: CI, RuboCop, and API Specs passed.
- `vpsadminos` head `6f9b2c755`: RSpec passed. Earlier head `6b768aaae` had
  CI, RSpec, and RuboCop green before the overlay-output follow-up.
- `vpsadminos-org-configuration` head `ac8ad6b`: no push workflow exists on
  the branch; only the scheduled `daily-update.yml` workflow is present.
- `confctl` head `7e288c8d`: Tests, RSpec, and RuboCop passed.
- `terraform-provider-vpsadmin` head `0e9e236`: Integration Tests passed.
- `vpsf-status` head `569459c`: Integration Tests passed.
- `vpsfree-irc-bot` head `49f6645`: RSpec and Integration Tests passed.
- `web` head `1e61bda`: Integration Tests passed.

## 2026-06-12 default-branch merges

- Merged and pushed the feature work to default branches:
  - `vpsadminos` `staging`: `14843dbb9..6f9b2c755`
  - `vpsadmin` `master`: `03f23e44d..ce5e5432c`
  - `confctl` `master`: `3ed71bc..8ccb94d`
  - `terraform-provider-vpsadmin` `master`: `21ae92e..803e396`
  - `vpsf-status` `master`: `457b111..9b7f2ee`
  - `vpsfree-irc-bot` `master`: `65b19c9..f15e077`
  - `web` `master`: `7f686dd..5b89796`
  - `vpsadminos-org-configuration` `master`: `d211cb3..ac8ad6b`
- After merge, vpsAdmin `libnodectld Specs` failed on `ce5e5432c` because
  `libnodectld/Gemfile` and `nodectld/Gemfile` still required the removed
  `tools/vpsadminos.rb` helper.
- Fixed vpsAdmin on `master` with `bb38a42cd`
  `nodectld: use exported vpsAdminOS source path in Gemfiles`. The Gemfiles now
  use the `VPSADMINOS_PATH` exported by the Nix shells and CI workflows and
  report a clear manual-use error when it is unset.
- Validation for the vpsAdmin follow-up:
  - `nix develop .#vpsadmin --command rake vpsadmin:gems`: passed and left only
    the intended Gemfile changes.
  - `nix develop .#libnodectld --command bash -lc 'bundle exec rspec'`: got
    past Bundler and failed only because the writable `libosctl/native`
    workflow prerequisite had not been built.
  - Workflow-equivalent local run copied the vpsAdminOS flake input to a
    writable directory, built `libosctl/native`, and ran
    `bundle exec rspec`: 397 examples, 0 failures.
  - `nix develop .#nodectld --command bash -lc 'bundle exec ruby -e "require
    \"bundler/setup\"; puts :ok"'`: passed.
  - Commit hooks passed through Overcommit.
- Repinned downstream default branches from vpsAdmin `ce5e5432c` to
  `bb38a42cd`:
  - `terraform-provider-vpsadmin`: `3ec4a1c`
    `flake: vpsadmin ce5e5432c -> bb38a42cd`
  - `vpsf-status`: `036c754`
    `flake: vpsadmin ce5e5432c -> bb38a42cd`
  - `vpsfree-irc-bot`: `1deb4e9`
    `flake: vpsadmin ce5e5432c -> bb38a42cd`
  - `web`: `bae16b5`
    `flake: vpsadmin ce5e5432c -> bb38a42cd`
- Downstream validation after the follow-up repin:
  - `terraform-provider-vpsadmin`: `testsMeta` length 1.
  - `vpsf-status`: `testsMeta` length 1.
  - `vpsfree-irc-bot`: `testsMeta` length 2.
  - `web`: `testsMeta` length 1.
- Superseded feature/default branch runs were cancelled where applicable.
- Current default-branch CI status:
  - `vpsadminos` head `6f9b2c755`: RuboCop and RSpec passed; CI is running.
  - `vpsadmin` head `bb38a42cd`: `libnodectld Specs` passed; CI is running.
  - `confctl` head `8ccb94d`: RuboCop and RSpec passed; Tests is running.
  - `terraform-provider-vpsadmin` head `3ec4a1c`: Integration Tests queued.
  - `vpsf-status` head `036c754`: Integration Tests queued.
  - `vpsfree-irc-bot` head `1deb4e9`: RSpec passed; Integration Tests queued.
  - `web` head `bae16b5`: Integration Tests queued.

## 2026-06-12 vpsadminos.org ISO build fix

- Reproduced the reported failure in `vpsadminos-org-configuration` with:
  `nix build --json --no-link --no-write-lock-file --no-update-lock-file
  .#confctl.build.m_org_vpsadminos_int_iso_eda0cf4b.toplevel`.
- Root cause: `lib/images.nix` source-imported `${inputs.vpsadminos}/os/`.
  That path used `os/default.nix`'s fallback
  `builtins.getFlake (toString ../.)` to find `netlinkrb` and `ruby-lxc`.
  During pure flake evaluation the vpsAdminOS input is an unlocked store source
  path, so `builtins.getFlake` fails with `cannot call 'getFlake' on unlocked
  flake reference`.
- Fixed on `vpsadminos-org-configuration/master` with commit `49cb30d`
  `iso: build vpsAdminOS images through flake output`.
  `lib/images.nix` now uses
  `flakeInputs.vpsadminos.lib.vpsadminosSystem`, which already carries the
  vpsAdminOS flake inputs needed by the osctl overlay. The old scoped source
  import and NIX_PATH emulation were removed as legacy code.
- Validation:
  - Focused ISO build passed and returned
    `/nix/store/qg2g7qd07i9cipcxlcphzlkwnxmzmzin-nixos-system-iso-26.05.20260608.bd0ff2d`.
  - The full multi-attribute build shape from the reported failure passed,
    including cache, docker-registry, images, iso, www, proxy toplevels and
    autoRollback outputs.
  - Re-ran both validations after removing the scoped-import fallback; both
    still passed.
  - Overcommit hook passed (`Nixfmt`).

## 2026-06-12 docs and org input update

- Committed and pushed the approved vpsAdminOS osctld development docs update:
  - `vpsadminos/staging`: `0236bcd3c`
    `docs: update osctld development gem workflow`
  - The document no longer mentions pushing first-party gems to a RubyGems
    repository and now describes source-backed packaging, `make gems`,
    focused package targets, and generated gem metadata commits.
  - Overcommit hook passed (`Nixfmt`). Commit-msg checks passed with only the
    repository's advisory 72-character body warning.
- Updated only `vpsadminos-org-configuration` as requested:
  - `vpsadminos-org-configuration/master`: `d096257`
    `inputs: update vpsadminos to 0236bcd3`
  - `flake.lock` input `vpsadminos_2` moved from
    `6f9b2c755143197bd9c3452e1c0121b22e978c4d` to
    `0236bcd3c0b632642ba7e2eb217fbe88ddbf3108`.
  - Overcommit hook passed (`Nixfmt`).
- Validation after the input update:
  - `nix build --json --no-link --no-write-lock-file --no-update-lock-file
    .#confctl.build.m_org_vpsadminos_int_www_27f4ac6e.toplevel
    .#confctl.build.m_org_vpsadminos_int_iso_eda0cf4b.toplevel` passed.
  - Outputs:
    `/nix/store/r42sz6pjqks007n56rid76xqqzbx9jby-nixos-system-www-26.05.20260608.bd0ff2d`
    and
    `/nix/store/i0l12kc01srcw8i5bjjh3vz0k4clwwkq-nixos-system-iso-26.05.20260608.bd0ff2d`.
- Workflow status after the final pushes:
  - `vpsadminos/staging` remote head is `0236bcd3c`; no GitHub Actions run
    was created for that docs-only commit. The previous `6f9b2c755` RuboCop,
    RSpec, and CI runs are green.
  - `vpsadminos-org-configuration/master` remote head is `d096257`; no push
    workflow was created. The repository currently shows only scheduled daily
    update runs.
  - Earlier downstream/default-branch runs are green for `confctl`,
    `terraform-provider-vpsadmin`, `vpsf-status`, `vpsfree-irc-bot`, and
    `web`.
  - `vpsadmin/master` run `27420325967` for commit `bb38a42cd` is still
    running in the `Run selected ci-tagged tests` job. GitHub does not expose
    logs for that job until it completes. The separate `libnodectld Specs` run
    for the same commit passed.

## 2026-06-25 cleanup

- Removed all linked worktrees under
  `worktrees/2026-06-10-ruby-gems-without-repository/`, including the original
  feature worktrees and the temporary `merge/` worktrees.
- Pruned worktree metadata in the affected bare repositories:
  `confctl`, `terraform-provider-vpsadmin`, `vpsadmin`,
  `vpsadminos-org-configuration`, `vpsadminos`, `vpsf-status`,
  `vpsfree-irc-bot`, and `web`.
- Preserved local and remote branch refs, plus this plan/state record.

## Archival request, 2026-10-06

The workspace operator requested archival of sessions dated August 2026 or
older, retaining recorded work and branches. This checkpoint commits the
existing plan and active state before the ordinary archive transition.
