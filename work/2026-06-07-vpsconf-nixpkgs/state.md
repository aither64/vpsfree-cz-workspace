---
lifecycle: active
---
# 2026-06-07-vpsconf-nixpkgs

## Repositories
- `vpsfree-cz-configuration`
  - Bare repo: `/home/aither/workspace/ai/vpsfree.cz/repos/vpsfree-cz-configuration.git`
  - Remote: `git@github.com:vpsfreecz/vpsfree-cz-configuration.git`
  - Feature branch: `2026-06-07-vpsconf-nixpkgs`
  - Commit: `c0041cef6ae270ee3f4f7863275eaf6e41c0de38`

## Status
- Investigated current `origin/master` history for nixpkgs channel inputs.
- Moved `nixpkgsProduction` and `nixpkgsStaging` to `nixos-26.05`.
- Updated `nixos-stable`, `production`, and `staging` nixpkgs channel locks to
  `9b696460ac78b5ccfc17c854d8c976f20456e943`.
- Committed and pushed to `origin/master`.
- Removed initiative worktrees after the push. Feature branch refs were kept.

## Commands run
- `bin/dev-session current`
- `git fetch --prune origin`
- `git show origin/master:AGENTS.md`
- `git show origin/master:flake.nix`
- `git show origin/master:flake.lock`
- `git log --all ... -- flake.nix flake.lock`
- `git show 0e19692b -- flake.nix flake.lock`
- `git show fe8e1e33 -- flake.nix flake.lock`
- `git show 76671f15 -- flake.nix flake.lock`
- `git show fb184af9 -- flake.lock`
- `git show 58ad6547 -- flake.lock`
- `git show origin/master:.github/workflows/daily-update.yml`
- `git worktree add -b 2026-06-07-vpsconf-nixpkgs ... origin/master`
- `nix develop -c confctl inputs channel update --no-commit --no-changelog '{nixos-stable,production,staging}' nixpkgs`
- `nix develop -c confctl inputs channel ls '{nixos-stable,production,staging}'`
- `nix develop -c bundle exec overcommit --install`
- `git add flake.nix flake.lock`
- `nix develop -c bundle exec overcommit --run PreCommit`
- `nix develop -c git commit -F <tmpfile>`
- `nix develop -c git commit --amend -F <tmpfile>`
- `git fetch --prune origin`
- `git worktree add --detach ... origin/master`
- `nix develop -c git merge --ff-only 2026-06-07-vpsconf-nixpkgs`
- `git push origin HEAD:master`
- `git branch -f master origin/master`
- `git worktree remove ...`
- `gh run list --repo vpsfreecz/vpsfree-cz-configuration --branch master --limit 5`

## Results
- Initial flake commit `0e19692b` from 2026-02-20 mapped both `staging` and
  `production` channels to `nixpkgsStable`.
- Commit `fe8e1e33` from 2026-02-28 introduced separate
  `nixpkgsProduction` and `nixpkgsStaging` flake inputs, both pointing at
  `github:NixOS/nixpkgs/nixos-25.11`, and changed channel mappings to use
  them.
- Through May 2026, automated input updates generally updated
  `nixpkgsProduction`, `nixpkgsStable`, and `nixpkgsStaging` together to the
  same revision because all three inputs pointed at `nixos-25.11`.
- Commit `76671f15` from 2026-06-04 moved only `nixpkgsStable` to
  `nixos-26.05`.
- Commit `fb184af9` from 2026-06-05 temporarily set production/staging locks to
  the same rev as stable, `6b316287`, while their original source remained
  `nixos-25.11`.
- Bot commit `58ad6547` from 2026-06-06 updated production/staging from their
  own `nixos-25.11` source to `535f3e69`, making them diverge from stable
  again.
- Commit `c0041cef` changes `nixpkgsProduction.url` and
  `nixpkgsStaging.url` to `github:NixOS/nixpkgs/nixos-26.05`.
- `flake.lock` now has `nixpkgsProduction`, `nixpkgsStable`, and
  `nixpkgsStaging` locked to `9b696460`.
- `confctl inputs channel ls '{nixos-stable,production,staging}'` confirmed
  all three nixpkgs roles at `9b696460`.
- Overcommit hooks passed:
  - `PreCommit/Nixfmt`
  - `CommitMsg/TextWidth`
  - `CommitMsg/SingleLineSubject`
  - `CommitMsg/TrailingPeriod`
- Push succeeded: `50726274..c0041cef  HEAD -> master`.
- GitHub reported existing default-branch Dependabot security alerts during
  push: 2 high, 3 moderate, 1 low. These were unrelated to this change.
- GitHub Actions check: no push-triggered run appeared for `c0041cef`; the
  latest listed `master` runs were scheduled `Daily update` runs, most recently
  successful at 2026-06-07T08:06:31Z.
- Added durable note:
  `notes/vpsfree-cz-configuration/2026-06-07-overcommit-nix-shell.md`.

## Notes
- `git worktree add` triggered an Overcommit checkout hook before repo-local
  gems were available and exited with code 78, but the worktrees were created.
  Running hook-managed commands inside `nix develop` fixed the environment.
- A first `git commit` outside `nix develop` failed because the pre-commit hook
  could not find `nixfmt`. The commit was rerun inside `nix develop`.
- The first successful commit had Overcommit warnings for the generated-style
  long subject/body lines. It was amended before push to
  `inputs: move nixpkgs channels to 26.05`, after which all commit-msg hooks
  passed cleanly.

## Open questions
- None.

## Cleanup
- Removed:
  - `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-06-07-vpsconf-nixpkgs/vpsfree-cz-configuration`
  - `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-06-07-vpsconf-nixpkgs/vpsfree-cz-configuration-master`
- Remaining worktree group directory is empty.

## Archival request, 2026-10-06

The workspace operator requested archival of sessions dated August 2026 or
older, retaining recorded work and branches. This checkpoint commits the
existing plan and active state before the ordinary archive transition.
