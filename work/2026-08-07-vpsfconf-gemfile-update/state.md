# 2026-08-07-vpsfconf-gemfile-update

## Repositories

- Repository: `vpsfree-cz-configuration`
- Branch: `2026-08-07-vpsfconf-gemfile-update`
- Worktree:
  `worktrees/2026-08-07-vpsfconf-gemfile-update/vpsfree-cz-configuration`
- Base: `origin/master` at `348a4e63`
- Compatibility reference: `vpsadmin` `origin/master` at `1657a321`

## Status

- Complete: changes are committed, reviewed, tested, and integrated into
  upstream `master`.
- Mandatory standalone change review passed after its commit-split findings
  were addressed.
- The next scheduled daily run will provide the first clean GitHub-hosted
  end-to-end execution of the updated workflow.

## Commands run

- `bin/dev-session current`
- `git fetch origin --prune` in both affected/reference bare repositories
- Inspected root Gemfile history, the daily update workflow, the confctl dev
  shell implementation, vpsAdmin's Ruby declarations, and pinned vpsAdmin
  revisions.
- Audited the current root lock with RubySec advisory database commit
  `36427421334c837ac49f3fd8ed5d31046d384af7`.
- Resolved the current root lock in a disposable worktree to assess available
  compatible updates.
- `bin/dev-session worktree add 2026-08-07-vpsfconf-gemfile-update
  vpsfree-cz-configuration --as-is --branch
  2026-08-07-vpsfconf-gemfile-update --base origin/master`
- `nix develop --accept-flake-config -c bundle exec overcommit --install`
- Regenerated the root lock with Ruby 3.4.9 and Bundler 4.0.18 using the same
  update sequence added to the daily workflow.
- `nix develop --accept-flake-config -c bash -lc 'nixfmt flake.nix;
  bundle check; bundle exec rake spec; bundle exec rubocop;
  bundler-audit check --update'`
- `nix flake check --no-build --accept-flake-config`
- `nix shell nixpkgs#actionlint -c actionlint
  .github/workflows/daily-update.yml`
- Re-ran the Bundler update sequence and compared the lock checksum.
- Committed with Overcommit hooks active using temporary message files.
- Ran the mandatory standalone review using
  `skills/mandatory-change-review/SKILL.md`.
- Rewrote the unmerged series in a detached temporary worktree, verified the
  rewritten head was tree-identical to the reviewed implementation, and moved
  the feature branch with `nix develop -c git rebase --onto`.
- Refreshed the shared Overcommit signature with `overcommit --sign` and ran
  the full hook set before retrying the policy commit.
- Removed the detached rewrite worktree and three disposable planning
  worktrees after confirming they were clean.
- Pushed feature branch `2026-08-07-vpsfconf-gemfile-update` over SSH.
- Created a fresh integration worktree from current `origin/master`, merged
  with `git merge --ff-only 2026-08-07-vpsfconf-gemfile-update`, and repeated
  the full validation there.
- Installed, signed, and ran Overcommit in the integration worktree.
- Guarded `origin/master` at `348a4e63`, then pushed the tested fast-forward
  `HEAD:master` over SSH.
- Removed the feature and integration worktrees after confirming both were
  clean.

## Results

- Before this change, the root `Gemfile.lock` was last updated manually on
  2026-04-19 and was not included in the daily dependency updater.
- Before this change, the 04:30 UTC/manual daily workflow regenerated package
  locks only for geminabox, ssh-exporter, and syslog-exporter before its atomic
  push to `master`. It now updates and validates the root bundle first.
- The old root lock had ten RubySec findings: two for `json` and eight for
  `net-imap`. The committed refresh resolves all ten.
- vpsAdmin `.ruby-version` is 3.4.0, its dev shells explicitly use
  `pkgs.ruby_3_4`, and the configuration's production, staging, and services
  input revisions all declare 3.4.0.
- The configuration dev shell already happened to use Ruby 3.4.9 through the
  Nixpkgs default, but its RuboCop target and repository guidance still said
  Ruby 3.1.
- Before `csv` was declared, the existing RSpec suite failed under Ruby 3.4
  because that library is no longer a default gem.
- The refreshed lock uses Ruby 3.4.9 and Bundler 4.0.18. It updates `json` to
  2.21.2 and `net-imap` to 0.6.6, among other compatible updates.
- `bundle check` passed.
- RSpec passed: 15 examples, 0 failures.
- RuboCop passed: 30 files, 0 offenses.
- Bundler Audit passed against RubySec database commit
  `36427421334c837ac49f3fd8ed5d31046d384af7`: no vulnerabilities.
- `nix flake check --no-build` passed; the existing unknown `confctl` output
  warning remains informational.
- actionlint 1.7.12 passed.
- Dependency resolution was idempotent: `Gemfile.lock` retained SHA-256
  `b20ffff07522c6d327e5eba559ea49d18fe95b5059dbd688441e56da5f1848f8`.
- The initial mandatory review found no implementation, deployment, or
  security defect, but required the two commits to be split by independently
  reviewable purpose.
- Final commits:
  - `676a365e` `dev-shell: align Ruby with vpsAdmin`
  - `3fccdbe6` `gems: refresh root dependencies`
  - `3306ead3` `ci: enforce hooks for daily updates`
  - `f72ff5d6` `ci: update root gems daily`
- `git diff 5e65763d f72ff5d6` was empty, confirming that the history rewrite
  did not change the tested final tree.
- The same standalone reviewer confirmed both blocking findings were resolved
  and reported no remaining Blocking, Important, or Advisory findings.
- Residual review gap: the scheduled workflow has not yet run end-to-end on a
  clean GitHub-hosted runner.
- Integration-worktree validation passed with the same results: Ruby 3.4.9,
  Bundler 4.0.18, 15 RSpec examples, 30 RuboCop files, no RubySec findings,
  successful flake evaluation, and clean actionlint.
- Upstream `master` and remote feature branch both point to `f72ff5d6`.
- No push-triggered workflow exists. The latest listed Daily update remains the
  successful scheduled run from 2026-08-07 before these commits; the next
  scheduled run is the remaining end-to-end workflow check.

## Open questions

- None. The user selected the existing direct daily updater, full RSpec/lint/
  audit gating, existing Gemfile constraints, and a coordinated Ruby 3.4 pin.

## Cleanup

- Feature and integration worktrees were removed.
- Generated `.bin`, `.bundle`, and `.rubocop_cache` directories were moved to
  task-specific temporary directories; they were never committed.
- The temporary rewrite worktree and all disposable planning worktrees created
  by this initiative were removed cleanly.
- Local and remote feature branches were preserved as required. The temporary
  local integration branch was also left intact; it points to the merged head.
