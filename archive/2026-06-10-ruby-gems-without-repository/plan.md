# 2026-06-10-ruby-gems-without-repository

## Goal

Remove the dependency on the private RubyGems repository for first-party
vpsAdminOS and vpsAdmin Ruby packages. Builds should use the source trees that
are already available through the repositories and flake inputs. Build IDs are
not needed; the git commit is the source identifier.

## Affected repositories

- `vpsadminos`: osctl/osctld and related Ruby packages, generated Bundler
  lockfiles and `gemset.nix`, native-extension gem inputs, and package helper
  code.
- `vpsadmin`: nodectl/nodectld packages, generated Bundler lockfiles and
  `gemset.nix`, integration with the `vpsadminos` flake input, and the gem
  refresh task.
- `confctl`: direct consumer of `vpsadminos.lib.testFramework` and
  `vpsadminos.packages.${system}.test-runner`.
- `terraform-provider-vpsadmin`, `vpsf-status`, `vpsfree-irc-bot`, and `web`:
  integration-test consumers that follow vpsAdmin's `vpsadminos` input through
  their `vpsadmin` flake input.
- `vpsfree-cz-configuration`: no code changes planned. The hosted gem
  repository may remain for old branches or unrelated packages.

## Chosen approach

1. Keep `bundlerEnv`/Bundix packaging, but make first-party gems source-built
   by Nix `gemConfig` overrides instead of fetched from
   `rubygems.vpsfree.cz`.
2. Remove build IDs from gem versions, lockfiles, gemsets, Make/Rake tasks,
   and update scripts. Package versions are the project versions, for example
   `26.05.0` and `4.1.0`.
3. Stop faking git repositories during source gem builds. Gemspecs now use
   deterministic `Dir[...]` file lists instead of `git ls-files`, so the helper
   only has to copy the source tree into the build directory.
4. In `vpsadminos`, add `netlinkrb` and `ruby-lxc` as non-flake inputs and use
   those inputs from `os/overlays/osctl.nix`. There is no duplicate
   `fetchFromGitHub` path for these Ruby dependencies.
5. In `vpsadmin`, build `libosctl`, `osctl`, and `osctl-exportfs` from the
   `vpsadminos` flake input, and build `libnodectld`, `nodectl`, and
   `nodectld` from the vpsAdmin checkout.
6. Regenerate package lockfiles by temporarily using path dependencies during
   `tools/update_gem.rb`, then normalize the committed metadata back to plain
   Rubygems sections with source gems represented by `source = { type = "gem"; }`.
   This keeps committed metadata compatible with `bundlerEnv` while avoiding
   path sources in deployments. The updater is Ruby so the lockfile and gemset
   normalization logic is not embedded in a shell script.
7. Replace `make gems`, `make commit-gems`, and `rake vpsadmin:gems` behavior
   with local metadata refreshes. No gem build/upload step is required.
8. Remove the unused vpsAdmin cronie package and module wiring. The scheduler
   no longer enables or overlays cron.
9. Add daily and manually runnable GitHub workflows for refreshing packaged
   Ruby gem dependency metadata. vpsAdminOS runs `make gems`; vpsAdmin runs
   the existing Bundix refresh plus `rake vpsadmin:gems`.
10. Update all default-branch users of the vpsAdminOS test framework in this
    workspace to a vpsAdminOS/vpsAdmin revision that contains the new
    source-gem packaging scheme.
11. Expose a flake-backed `lib.testFramework` object from vpsAdminOS. Consumer
    tests call `testFramework.makeTest` and `testFramework.makeTestLib`
    instead of passing raw vpsAdminOS source paths through `suiteArgs`. The
    framework object carries the vpsAdminOS source path and the flake inputs
    needed by osctl packages.
12. Keep vpsAdminOS's NixOS 26.05 direct-boot fix inside the actual test-runner
    VM graph. The shared `tests/configs/nixos/base.nix` remains importable by
    external deployment tests, while qemu-vm-only `virtualisation.*` defaults
    live in a separate module imported only after `qemu-vm.nix`.

## Compatibility and deployment

The runtime Ruby code, database schemas, APIs, daemon protocols, and persisted
state are unchanged. This is a packaging/source-selection change.

Mixed versions are safe. Existing deployed systems and older branches can keep
using `rubygems.vpsfree.cz`; new builds use local source trees and flake
inputs. Rollback to an older build returns to the older package metadata and
remote repository use.

`vpsadmin` must update its `vpsadminos` flake input to a revision containing the
vpsAdminOS side of this change before it can build independently without the
private gem repository. During development, selected vpsAdmin validations were
run with a temporary local flake-lock override and the lockfile restored after
the run.

No coordinated update of all running vpsAdminOS nodes is required.

External test-runner consumers now receive the vpsAdminOS source and osctl
dependency inputs through the flake-exported framework API. This keeps normal
consumer evaluation pure without adding repository-specific fallback fetching
or asking each suite to know about `netlinkrb` and `ruby-lxc`.

## Testing plan

- Regenerate vpsAdminOS package metadata with `make gems`.
- Regenerate vpsAdmin package metadata with `rake vpsadmin:gems` while pointing
  `VPSADMINOS_PATH` at the local vpsAdminOS worktree.
- Build all affected vpsAdminOS Ruby package derivations.
- Build vpsAdmin `libnodectld`, `nodectl`, and `nodectld` with the local
  vpsAdminOS source input.
- Smoke-test generated `osctl` and `nodectl` wrappers.
- Run a direct vpsAdminOS integration test after regeneration.
- Run a focused vpsAdmin integration scenario that exercises `nodectl` and
  `nodectld` against a real vpsAdminOS node.
- Run a focused vpsAdmin scheduler integration scenario to cover the cronie
  removal path.
- Validate workflow YAML with `ruby -e 'require "yaml"; YAML.load_file(...)'`
  and `actionlint`.
- Locally run the workflow gem update commands:
  `nix develop .#vpsadminos --command bash -lc 'make gems'` and vpsAdmin's
  `./tools/bundix_all.sh && rake vpsadmin:gems && nixfmt packages/*/gemset.nix`
  with a temporary local vpsAdminOS input override.
- For downstream test-runner consumers, evaluate the exported test metadata or
  representative check derivations from the updated flake graph without local
  overrides.
- Run cheap native checks in downstream consumers:
  - Terraform provider: Go tests in the repository Nix shell.
  - vpsf-status: Go tests and Nix package build.
  - vpsfree-irc-bot: package build and RSpec.
  - web: validator check.
  - confctl: pure check evaluation and package build.
