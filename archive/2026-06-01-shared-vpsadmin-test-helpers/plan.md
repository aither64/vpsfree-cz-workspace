# shared vpsAdmin test helpers

## Goal

Share the vpsAdmin service VM test helpers used by external integration suites
instead of copying `VpsadminServicesMachine`, `vpsadminctl`, and API fixture
helpers into every project.

The initial consumers are:

- `vpsf-status`
- `terraform-provider-vpsadmin`
- `vpsfree-irc-bot` integration tests, currently WIP in another worktree

## Affected repositories

- `vpsadminos`: add generic support for loading test-runner extensions from
  explicit external paths.
- `vpsadmin`: publish the shared vpsAdmin service helper and provide a wrapped
  test-runner app/package that loads it.
- `terraform-provider-vpsadmin`: consume the shared helper and remove the local
  duplicate.
- `vpsf-status`: consume the shared helper after, or while folding, the current
  integration-test branch.
- `vpsfree-irc-bot`: consume the shared helper once the WIP integration tests
  are ready to rebase.

## Worktrees

All worktrees are under:

`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-06-01-shared-vpsadmin-test-helpers`

- `vpsadminos`: branch `2026-06-01-shared-vpsadmin-test-helpers`, based on
  `origin/staging` at `6dc4209c4`.
- `vpsadmin`: branch `2026-06-01-shared-vpsadmin-test-helpers`, based on
  `origin/master` at `21a1d0b11`.
- `terraform-provider-vpsadmin`: branch
  `2026-06-01-shared-vpsadmin-test-helpers`, based on `origin/master` at
  `6984147`.
- `vpsfree-irc-bot`: branch `2026-06-01-shared-vpsadmin-test-helpers`, based
  on `origin/master` at `6db629e`.
- `vpsf-status`: branch `2026-06-01-shared-vpsadmin-test-helpers`, based on
  `origin/master` at `c6fab24`.

## Proposed design

### 1. Make extension loading generic in vpsadminos

Extend the vpsAdminOS `test-runner` so it loads Ruby extensions from:

- the existing local `tests/runner/extensions/*.rb`; and
- an explicit external list, for example a colon-separated
  `TEST_RUNNER_EXTENSIONS` environment variable and/or a repeated
  `--extension` CLI option.

External entries should accept either a file or a directory. Directories should
load `*.rb` in sorted order. De-duplicate by absolute path so wrappers can be
composed safely.

Load external extensions before local repo extensions. That lets a project load
the shared vpsAdmin helper and then keep a small local extension that adds
project-specific machines or reopens helper classes.

This keeps vpsAdmin-specific knowledge out of vpsAdminOS. vpsAdminOS only gains
a generic test-runner feature.

### 2. Publish the vpsAdmin helper from vpsadmin

Split the current `vpsadmin/tests/runner/extensions/vpsadmin_services.rb` into:

- a shared helper file, for example
  `tests/runner/shared/vpsadmin_services.rb`; and
- the existing vpsAdmin-local extension wrapper, which loads the shared helper
  and then adds vpsAdmin-only helpers such as Mailpit, migration debug helpers,
  and broad ZFS helpers.

The shared helper should include the parts external projects need:

- `Vpsadminctl` wrapper with raw JSON parsing;
- `VpsadminServicesMachine < OsVm::NixosMachine`;
- `services.vpsadminctl`;
- `wait_for_vpsadmin_api`;
- `api_ruby` and `api_ruby_json`;
- optional plugin model loading for `api_ruby`, e.g.
  `plugins: %w[outage_reports newslog]`;
- MariaDB helpers where external suites already use them;
- transaction-chain wait helpers and transaction signing key unlock helper.

Plugin model loading should be explicit per call rather than always requiring
every plugin. That keeps fixtures clear and avoids unnecessary coupling:

```ruby
services.api_ruby_json(
  plugins: %w[outage_reports],
  code: <<~RUBY
    outage = Outage.create!(...)
    puts JSON.dump(id: outage.id)
  RUBY
)
```

Expose a wrapped test runner from `vpsadmin`, for example:

- `packages.${system}.test-runner-with-vpsadmin-helpers`
- `apps.${system}.test-runner-with-vpsadmin-helpers`

The wrapper should set `TEST_RUNNER_EXTENSIONS` to the shared helper path and
then exec `${vpsadminos.packages.${system}.test-runner}/bin/test-runner`.

### 3. Migrate consumers

For each external consumer with vpsAdmin integration tests:

- keep the `vpsadmin` input and `vpsadminos.follows = "vpsadmin/vpsadminos"`;
- set `packages.${system}.test-runner` and `apps.${system}.test-runner` to the
  vpsAdmin wrapped runner;
- remove the copied local `VpsadminServicesMachine` helper;
- keep only project-specific extensions locally.

Consumer-specific notes:

- `terraform-provider-vpsadmin`: remove
  `tests/runner/extensions/vpsadmin_services.rb`; existing workflow tests
  should continue to call `services.wait_for_vpsadmin_api`,
  `services.api_ruby_json`, and `services.vpsadminctl`.
- `vpsf-status`: the migration should be applied on top of the current
  `2026-06-01-vpsf-status-integration-tests` branch or folded into it before
  review. The standalone shared-helper worktree is based on `origin/master`
  only to avoid touching that staged WIP.
- `vpsfree-irc-bot`: once the other WIP integration branch is ready, remove
  the duplicate vpsAdmin service helper from `tests/runner/extensions/irc_bot.rb`
  and leave only IRC-specific machines/helpers there. Its news/outage fixtures
  should call `api_ruby_json(..., plugins: %w[newslog outage_reports])`.

## Deployment and compatibility

- No production runtime behavior changes.
- No persisted state, database schema, API contract, or node protocol changes.
- `vpsadminos` change is test-runner-only and backward compatible: existing
  local `tests/runner/extensions/*.rb` loading continues to work.
- `vpsadmin` change preserves its local extension path so the vpsAdmin test
  suite does not need broad edits.
- Consumer migrations only affect integration tests and CI.
- Deployment order for branches:
  1. merge vpsAdminOS test-runner external extension support to `staging`;
  2. update/pin vpsAdmin to that vpsAdminOS revision and add shared helper plus
     wrapped runner;
  3. update consumer repos to the vpsAdmin revision with the shared helper.

## Validation plan

For `vpsadminos`:

- test-runner unit/spec coverage for local extensions, external file loading,
  external directory loading, missing path errors, and duplicate suppression.
- targeted command such as `nix develop .#test-runner --command bundle exec
  rspec test-runner/spec/test_runner/cli/command_spec.rb`.

For `vpsadmin`:

- `./test-runner.sh ls services-up`
- a small representative test such as `./test-runner.sh test services-up`

For `terraform-provider-vpsadmin`:

- `./test-runner.sh ls -t ci`
- `./test-runner.sh test workflows` or `make test-integration`

For `vpsf-status`:

- after rebasing/folding current integration work,
  `./test-runner.sh test status-page`.

For `vpsfree-irc-bot`:

- after the WIP branch settles, `./test-runner.sh test vpsadmin-events`.

## Open review questions

- Should the test-runner interface be env-only, CLI-only, or both? The proposed
  answer is both: env for Nix wrappers, CLI for ad hoc local debugging.
- Should vpsAdmin expose one shared helper or split it into `core`,
  `mailpit`, `transactions`, and `zfs` helper files? The proposed first pass is
  one core shared file plus vpsAdmin-local extras to keep consumer adoption
  simple.
- Should consumer wrappers keep the app name `test-runner` while pointing to
  the vpsAdmin wrapped runner? The proposed answer is yes, so existing
  `./test-runner.sh` commands and workflows do not change.
