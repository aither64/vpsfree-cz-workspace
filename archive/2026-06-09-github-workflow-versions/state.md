---
lifecycle: abandoned
---
# 2026-06-09-github-workflow-versions

## Repositories

- Workspace root:
  - Path: `/home/aither/workspace/ai/vpsfree.cz`
  - File changed: `AGENTS.md`
- `confctl`
  - Branch: `2026-06-09-github-workflow-versions`
  - Worktree: `worktrees/2026-06-09-github-workflow-versions/confctl`
  - Base: `origin/master` at `617b222`
- `haveapi`
  - Branch: `2026-06-09-github-workflow-versions`
  - Worktree: `worktrees/2026-06-09-github-workflow-versions/haveapi`
  - Base: `origin/master` at `ac8e6ff`
- `terraform-provider-vpsadmin`
  - Branch: `2026-06-09-github-workflow-versions`
  - Worktree: `worktrees/2026-06-09-github-workflow-versions/terraform-provider-vpsadmin`
  - Base: `origin/master` at `b9b0acb`
- `vpsadmin`
  - Branch: `2026-06-09-github-workflow-versions`
  - Worktree: `worktrees/2026-06-09-github-workflow-versions/vpsadmin`
  - Base: `origin/master` at `c8fbfe38f`
- `vpsadminos-org-configuration`
  - Branch: `2026-06-09-github-workflow-versions`
  - Worktree: `worktrees/2026-06-09-github-workflow-versions/vpsadminos-org-configuration`
  - Base: `origin/master` at `158fb1b`
- `vpsfree-cz-configuration`
  - Branch: `2026-06-09-github-workflow-versions`
  - Worktree: `worktrees/2026-06-09-github-workflow-versions/vpsfree-cz-configuration`
  - Base: `origin/master` at `64ec3436`

Skipped by user request:

- `zfs`
- `linux`

## Status

- Workflow action version updates were committed, fast-forward merged to default
  branches, and pushed.
- The top-level `AGENTS.md` version-check rule was committed and pushed to the
  workspace repository.
- Feature and merge worktrees were removed after merge. Feature branches were
  kept locally.

## Commands run

- `bin/dev-session current`
  - Active initiative: `2026-06-09-github-workflow-versions`.
- `git fetch --prune origin` in every canonical bare repository under `repos/`.
- Scanned default-branch workflows for
  `uses: actions/...@...` across all project repositories.
- Verified latest official action tags with `git ls-remote --tags --refs` and
  GitHub tag pages for:
  - `actions/checkout`
  - `actions/setup-go`
  - `actions/setup-node`
  - `actions/cache`
  - `actions/upload-artifact`
  - `actions/download-artifact`
- Created worktrees from current upstream default branches for the six changed
  repositories.
- Read repository-local `AGENTS.md` in changed worktrees where present.
- Post-edit scan of all non-`zfs/linux` workflows using edited worktrees where
  present.
- `nix shell nixpkgs#actionlint -c actionlint` across changed repositories.
- Scoped lint of changed workflow files with ShellCheck disabled:
  `nix shell nixpkgs#actionlint -c actionlint -shellcheck= ...`
- `git diff --check` in every changed repository worktree.
- `git diff --check -- AGENTS.md work/2026-06-09-github-workflow-versions/plan.md work/2026-06-09-github-workflow-versions/state.md`
- Hook setup/checks before commit:
  - `nix develop -c bundle exec overcommit --install` in `haveapi`
  - `nix develop -c bundle exec overcommit --run PreCommit` in `confctl`,
    `haveapi`, `vpsadmin`, `vpsadminos-org-configuration`, and
    `vpsfree-cz-configuration`
- Committed with `git commit -F <tmpfile>` in every changed repository.
- Fast-forward merged from temporary detached worktrees and pushed default
  branches.
- Removed generated local hook caches (`.gems`, `.bundle`, `.bin`) and removed
  all feature/merge worktrees for this initiative.
- Checked GitHub Actions runs for pushed commits with `gh run list`,
  `gh run view`, and `gh run watch --compact`.
- Downloaded `confctl` failed run artifact
  `confctl-test-logs-27232111479` for inspection.

## Results

- Updated `confctl`:
  - `.github/workflows/rspec.yml`: `actions/checkout@v4` to `@v6`
  - `.github/workflows/rubocop.yml`: `actions/checkout@v4` to `@v6`
  - `.github/workflows/tests.yml`: `actions/checkout@v4` to `@v6`
- Updated `haveapi`:
  - `.github/workflows/_ruby-rspec.yml`: `actions/checkout@v4` to `@v6`
  - `.github/workflows/_ruby-rspec.yml`: `actions/setup-go@v5` to `@v6`
  - `.github/workflows/clients-js-tests.yml`: `actions/checkout@v4` to `@v6`
  - `.github/workflows/clients-js-tests.yml`: `actions/setup-node@v4` to `@v6`
  - `.github/workflows/clients-php-phpunit.yml`: `actions/checkout@v4` to
    `@v6`
  - `.github/workflows/rubocop.yml`: `actions/checkout@v4` to `@v6`
- Updated `terraform-provider-vpsadmin`:
  - `.github/workflows/go-tests.yml`: pinned `actions/setup-go` v5.1.0 SHA to
    `actions/setup-go@v6`
  - `.github/workflows/release.yml`: pinned `actions/setup-go` v5.1.0 SHA to
    `actions/setup-go@v6`
- Updated `vpsadmin`:
  - `.github/workflows/api-specs.yml`: `actions/upload-artifact@v4` to `@v7`
  - `.github/workflows/api-specs.yml`: `actions/download-artifact@v4` to `@v8`
- Updated `vpsadminos-org-configuration`:
  - `.github/workflows/daily-update.yml`: `actions/checkout@v4` to `@v6`
  - `.github/workflows/daily-update.yml`: `actions/cache/restore@v4` to `@v5`
  - `.github/workflows/daily-update.yml`: `actions/cache/save@v4` to `@v5`
- Updated `vpsfree-cz-configuration`:
  - `.github/workflows/daily-update.yml`: `actions/checkout@v4` to `@v6`
  - `.github/workflows/daily-update.yml`: `actions/cache/restore@v4` to `@v5`
  - `.github/workflows/daily-update.yml`: `actions/cache/save@v4` to `@v5`
- Commits pushed:
  - `confctl` `master`: `3ed71bc` `workflows: update GitHub actions`
  - `haveapi` `master`: `239a34b` `workflows: update GitHub actions`
  - `terraform-provider-vpsadmin` `master`: `21ae92e`
    `workflows: update GitHub actions`
  - `vpsadmin` `master`: `2b505e06a`
    `workflows: update GitHub actions`
  - `vpsadminos-org-configuration` `master`: `dbb88d2`
    `workflows: update GitHub actions`
  - `vpsfree-cz-configuration` `master`: `47b9b177`
    `workflows: update GitHub actions`
  - workspace `master`: `cdbb710`
    `docs: require current workflow action versions`
- No stale non-`zfs/linux` `actions/*` refs remain in the post-edit scan.
- `git diff --check` passed for all changed repository diffs and workspace
  tracking/doc edits.
- Scoped `actionlint -shellcheck=` passed for all changed workflow files.
- Full `actionlint` found pre-existing ShellCheck findings unrelated to this
  version bump:
  - `vpsadmin/.github/workflows/libnodectld-specs.yml`: SC2016 on a run block.
  - `vpsadminos-org-configuration/.github/workflows/daily-update.yml`: SC2086
    for unquoted `$USER` in existing shell commands.
- GitHub Actions after push:
  - `confctl`:
    - `RSpec` run `27232111941`: success.
    - `RuboCop` run `27232111807`: success.
    - `Tests` run `27232111479`: failure. Checkout with
      `actions/checkout@v6` succeeded. Five integration tests then failed:
      `deploy/flakes`, `deploy/swpins`, `auto_rollback`, `carrier/deploy`,
      and `carrier/netboot`.
    - Current failure evidence: downloaded artifact
      `confctl-test-logs-27232111479`; logs show Nix evaluation failures such
      as `The option virtualisation.fileSystems does not exist` and carrier
      profile deployment errors. This is not caused by the checkout action
      update.
    - Previous `Tests` run `27225005692` on base commit `617b222` also failed
      before this change because `actions/checkout@v4` tried to start the
      runner's Node 20 binary, which was missing. The `@v6` update fixed that
      checkout/runtime failure and exposed the existing integration failures.
  - `haveapi`:
    - `clients/php PHPUnit` run `27232136521`: success.
    - `clients/js tests` run `27232136751`: success.
  - `terraform-provider-vpsadmin`:
    - `Go Tests` run `27232148237`: success.
  - `vpsadmin`:
    - `API Specs (topic parallel)` run `27232173448`: success.
  - `vpsadminos-org-configuration` and `vpsfree-cz-configuration`:
    - No push-triggered runs for the changed daily-update workflows.

## Open questions

- None.

## Cleanup

- Worktrees were removed after merge/push.
- Local feature branches remain in the bare repositories, per workspace policy.

## Archival request, 2026-10-06

The workspace operator requested archival of sessions dated August 2026 or
older, retaining recorded work and branches. This checkpoint commits the
existing plan and active state before the ordinary archive transition.
