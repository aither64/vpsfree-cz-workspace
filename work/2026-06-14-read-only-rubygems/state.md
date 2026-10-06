---
lifecycle: active
---
# 2026-06-14-read-only-rubygems

## Repositories

- `vpsfree-cz-configuration`
  - branch: `2026-06-14-read-only-rubygems`
  - worktree:
    `worktrees/2026-06-14-read-only-rubygems/vpsfree-cz-configuration`

## Status

- Created the `vpsfree-cz-configuration` worktree from updated `origin/master`
  (`29ffeee3`).
- Updated `int.rubygems` so Geminabox sets `allow_upload = false`.
- Disabled `services.geminabox.garbage-collector` for `int.rubygems` and
  removed the now-unused host-local GC scripts.
- Pre-commit hooks are installed and pass.
- Committed the change in `vpsfree-cz-configuration` as `46a0c48f`
  (`rubygems.int: disable gem uploads`).
- Merged to `master` with a fast-forward from a temporary target worktree and
  pushed `46a0c48f` to `origin/master`.
- Removed the feature and temporary merge worktrees. Branch refs were kept.

## Commands run

- `bin/dev-session current`
- `git --git-dir=repos/vpsfree-cz-configuration.git fetch origin`
- `git --git-dir=repos/vpsfree-cz-configuration.git worktree add -b 2026-06-14-read-only-rubygems worktrees/2026-06-14-read-only-rubygems/vpsfree-cz-configuration origin/master`
- `sed -n '1,240p' AGENTS.md`
- `rg -n "geminabox|rubygems\\.int|garbage|gc|gem.*collect|rubygems"`
- `curl -fsSL https://raw.githubusercontent.com/geminabox/geminabox/v3.1.0/lib/geminabox/server.rb | sed -n '1,260p'`
- `nix develop -c nixfmt cluster/cz.vpsfree/containers/int.rubygems/config.nix`
- `nix develop -c confctl build "cz.vpsfree/containers/int.rubygems"` (failed:
  interactive confirmation prompt reached EOF)
- `nix develop -c confctl build --help`
- `nix develop -c confctl build -y "cz.vpsfree/containers/int.rubygems"`
- `nix develop -c bundle exec overcommit --version`
- `nix develop -c bundle exec overcommit --install`
- `nix develop -c bundle exec overcommit --run`
- `git diff --check`
- `nix develop -c git commit -F /tmp/vpsfree-rubygems-read-only-commit-msg`
- `git status --short --branch --untracked-files=all`
- `git --git-dir=repos/vpsfree-cz-configuration.git worktree add --detach worktrees/2026-06-14-read-only-rubygems/vpsfree-cz-configuration-merge origin/master`
- `git merge --ff-only 2026-06-14-read-only-rubygems`
- `nix develop -c confctl build -y "cz.vpsfree/containers/int.rubygems"`
- `git push origin HEAD:master`
- `gh run list --repo vpsfreecz/vpsfree-cz-configuration --commit 46a0c48fd189f0d44c431bd1b4d8fb986c818df0 --limit 10`
- `gh run list --repo vpsfreecz/vpsfree-cz-configuration --branch master --limit 10`
- `git --git-dir=repos/vpsfree-cz-configuration.git branch -f master origin/master`
- `git --git-dir=repos/vpsfree-cz-configuration.git worktree remove worktrees/2026-06-14-read-only-rubygems/vpsfree-cz-configuration-merge`
- `git --git-dir=repos/vpsfree-cz-configuration.git worktree remove worktrees/2026-06-14-read-only-rubygems/vpsfree-cz-configuration`
- `rmdir worktrees/2026-06-14-read-only-rubygems`

## Results

- The worktree checkout triggered an Overcommit/Bundler warning because the
  ambient shell lacks the locked Ruby gems. Running Overcommit through
  `nix develop` resolved this for validation and commit hooks.
- Geminabox 3.1.0 has `Geminabox.allow_upload`; its server rejects both web and
  API upload routes when this setting is false.
- `confctl build -y "cz.vpsfree/containers/int.rubygems"` succeeded and built
  generation `2026-06-14--13-36-50`.
- Overcommit pre-commit hooks passed:
  - `Nixfmt`
  - `RuboCop`
- `git diff --check` passed.
- Commit hook ran during `git commit`. The text-width check emitted warnings
  for lines longer than 72 characters, but the hook passed and the longest
  commit-message line is 79 characters, within the workspace 80-character rule.
- The fast-forward merge updated `master` from `29ffeee3` to `46a0c48f` and
  pushed successfully to GitHub.
- GitHub Actions had no runs for commit `46a0c48f`. Recent `master` runs are
  scheduled `Daily update` workflows only; the latest listed run was successful.
- The merged-tree validation build succeeded and built generation
  `2026-06-14--14-58-27`.

## Open questions

- None.

## Cleanup

- Feature and merge worktrees were removed.
- The empty `worktrees/2026-06-14-read-only-rubygems` directory was removed.
- Feature branch refs were kept locally as requested by workspace policy.

## Archival request, 2026-10-06

The workspace operator requested archival of sessions dated August 2026 or
older, retaining recorded work and branches. This checkpoint commits the
existing plan and active state before the ordinary archive transition.
