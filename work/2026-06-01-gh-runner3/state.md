---
lifecycle: active
---
# gh-runner3 state

## Branches and worktrees

- `vpsadminos-org-configuration`
  - Branch: `2026-06-01-gh-runner3`
  - Worktree: `worktrees/2026-06-01-gh-runner3/vpsadminos-org-configuration`
  - Base: `origin/master` at `ae8f85b`
- `vpsfree-cz-configuration`
  - Branch: `2026-06-01-gh-runner3`
  - Worktree: `worktrees/2026-06-01-gh-runner3/vpsfree-cz-configuration`
  - Base: `origin/master` at `a38c85e`

## Progress

- Created initiative directories.
- Fetched both upstream repositories.
- Created feature worktrees for both repositories.
- Read `vpsfree-cz-configuration/AGENTS.md`.
- `vpsadminos-org-configuration` has no repository-local `AGENTS.md`; follow
  existing repository structure and files.
- Added `org.vpsadminos/int.gh-runner3` to `vpsadminos-org-configuration`.
- Added `gh-runner3` to the vpsadminos.org internal DNS zone in
  `vpsfree-cz-configuration`.
- Committed the user-provided vpsAdmin container data refresh in
  `vpsfree-cz-configuration`.
- Installed Overcommit hooks in both worktrees.
- Signed the `vpsadminos-org-configuration` Overcommit `pre-commit` hook after
  it blocked the first commit attempt.
- Removed transient `.bundle`/`.bin` files created by the dev shells/hooks.
- Merged both feature branches into `master` using fresh detached worktrees
  based on `origin/master` and fast-forward-only merges.
- Pushed both updated default branches to GitHub.
- Fetched the pushed default branches back into the bare clones and updated the
  local `master` refs to match `origin/master`.
- Removed the `2026-06-01-gh-runner3` feature and merge worktrees. Local
  feature branches were preserved.

## Commits

- `vpsadminos-org-configuration`: `3e5c24f cluster: add gh-runner3`
- `vpsfree-cz-configuration`: `f89bb099 internal-dns: add gh-runner3.int.vpsadminos.org`
- `vpsfree-cz-configuration`: `88e9f518 data: update vpsadmin/containers`

## Merge and push

- `vpsadminos-org-configuration`
  - `master` and `origin/master`: `3e5c24f`
  - Pushed `ae8f85b..3e5c24f` to `origin/master`.
- `vpsfree-cz-configuration`
  - `master` and `origin/master`: `88e9f518`
  - Pushed `a38c85ec..88e9f518` to `origin/master`.

## Commands run

- `git --git-dir=repos/vpsadminos-org-configuration.git fetch origin`
- `git --git-dir=repos/vpsfree-cz-configuration.git fetch origin`
- `git --git-dir=repos/vpsadminos-org-configuration.git update-ref refs/heads/master refs/remotes/origin/master`
- `git --git-dir=repos/vpsadminos-org-configuration.git symbolic-ref HEAD refs/heads/master`
- `git --git-dir=repos/vpsadminos-org-configuration.git worktree add -b 2026-06-01-gh-runner3 worktrees/2026-06-01-gh-runner3/vpsadminos-org-configuration origin/master`
- `git --git-dir=repos/vpsfree-cz-configuration.git worktree add -b 2026-06-01-gh-runner3 worktrees/2026-06-01-gh-runner3/vpsfree-cz-configuration origin/master`
- `nix develop -c nixfmt cluster/cluster.nix cluster/org.vpsadminos/int.gh-runner3/config.nix cluster/org.vpsadminos/int.gh-runner3/module.nix cluster/org.vpsadminos/proxy/config.nix`
- `named-checkzone vpsadminos.org configs/internal-dns/zone.vpsadminos.org.`
- `nix develop -c confctl ls`
- `nix develop -c confctl build -y org.vpsadminos/int.gh-runner3`
- `nix develop -c confctl build -y org.vpsadminos/proxy`
- `nix develop -c confctl build -y -t internal-dns`
- `nix develop -c overcommit --install`
- `nix develop -c overcommit --sign pre-commit`
- `nix develop -c git commit -F /tmp/2026-06-01-gh-runner3-vpsadminos-org.msg`
- `nix develop -c git commit -F /tmp/2026-06-01-gh-runner3-vpsfree-cz.msg`
- `nix develop -c confctl build -y -t alerter`
  - Interrupted after the user requested to skip the build.
- `nix develop -c git commit -F /tmp/2026-06-01-gh-runner3-vpsadmin-data.msg`
- `git --git-dir=repos/vpsadminos-org-configuration.git fetch origin`
- `git --git-dir=repos/vpsfree-cz-configuration.git fetch origin`
- `git --git-dir=repos/vpsadminos-org-configuration.git worktree add --detach worktrees/2026-06-01-gh-runner3/merge/vpsadminos-org-configuration origin/master`
- `git --git-dir=repos/vpsfree-cz-configuration.git worktree add --detach worktrees/2026-06-01-gh-runner3/merge/vpsfree-cz-configuration origin/master`
- `git merge --ff-only 2026-06-01-gh-runner3`
- `nix develop -c confctl ls`
- `named-checkzone vpsadminos.org configs/internal-dns/zone.vpsadminos.org.`
- `nix develop -c git push origin HEAD:master`
- `git --git-dir=repos/vpsadminos-org-configuration.git fetch origin master`
- `git --git-dir=repos/vpsfree-cz-configuration.git fetch origin master`
- `git --git-dir=repos/vpsadminos-org-configuration.git update-ref refs/heads/master refs/remotes/origin/master`
- `git --git-dir=repos/vpsfree-cz-configuration.git update-ref refs/heads/master refs/remotes/origin/master`
- `git --git-dir=repos/vpsadminos-org-configuration.git worktree remove worktrees/2026-06-01-gh-runner3/merge/vpsadminos-org-configuration`
- `git --git-dir=repos/vpsadminos-org-configuration.git worktree remove worktrees/2026-06-01-gh-runner3/vpsadminos-org-configuration`
- `git --git-dir=repos/vpsfree-cz-configuration.git worktree remove worktrees/2026-06-01-gh-runner3/merge/vpsfree-cz-configuration`
- `git --git-dir=repos/vpsfree-cz-configuration.git worktree remove worktrees/2026-06-01-gh-runner3/vpsfree-cz-configuration`
- `gh run list --repo vpsfreecz/vpsadminos-org-configuration --commit 3e5c24f3038ba66df2be15940ab2541335236242 --limit 10`
- `gh run list --repo vpsfreecz/vpsfree-cz-configuration --commit 88e9f518e27cbea3bc288e4ec5e50f3c5b6d41fe --limit 10`
- `git --git-dir=repos/vpsadminos-org-configuration.git ls-tree -r --name-only origin/master .github/workflows`
- `git --git-dir=repos/vpsfree-cz-configuration.git ls-tree -r --name-only origin/master .github/workflows`

## Validation

- `nix develop -c nixfmt ...` succeeded in
  `vpsadminos-org-configuration`.
- `named-checkzone vpsadminos.org configs/internal-dns/zone.vpsadminos.org.`
  loaded serial `2026060101` and returned `OK`; it warned about the expected
  repository placeholder `@fqdn@`.
- `nix develop -c confctl ls` listed
  `org.vpsadminos/int.gh-runner3`.
- `nix develop -c confctl build -y org.vpsadminos/int.gh-runner3` built
  generation `2026-06-01--15-39-32`.
- `nix develop -c confctl build -y org.vpsadminos/proxy` built generation
  `2026-06-01--15-41-55`.
- `nix develop -c confctl build -y -t internal-dns` built
  `cz.vpsfree/containers/brq/int.ns1` and
  `cz.vpsfree/containers/prg/int.ns1` as generation
  `2026-06-01--15-41-11`.
- Overcommit hooks passed for both commits.
- Overcommit hooks passed for the later
  `data: update vpsadmin/containers` commit.
- The alerter build was started for the vpsAdmin data refresh, but the user
  requested to skip it. The build was interrupted before completion.
- After fast-forward merge, `nix develop -c confctl ls` in
  `vpsadminos-org-configuration` listed `org.vpsadminos/int.gh-runner3`.
- After fast-forward merge, `named-checkzone vpsadminos.org
  configs/internal-dns/zone.vpsadminos.org.` in `vpsfree-cz-configuration`
  loaded serial `2026060101` and returned `OK`; it warned about the expected
  repository placeholder `@fqdn@`.
- Initial pushes outside the Nix dev shells were blocked by Overcommit
  pre-push hook gem loading. Retrying the same pushes via `nix develop -c git
  push origin HEAD:master` succeeded.
- No GitHub Actions runs were found for the pushed commits. Both repositories
  currently have only `.github/workflows/daily-update.yml` on `origin/master`,
  and the recent visible runs are scheduled daily update runs rather than push
  runs.

## Open questions

- None currently.

## Cleanup

- Feature worktrees removed.
- Merge worktrees removed.
- Feature branches remain active.
- Local `master` refs in both bare clones match `origin/master`.

## Archival request, 2026-10-06

The workspace operator requested archival of sessions dated August 2026 or
older, retaining recorded work and branches. This checkpoint commits the
existing plan and active state before the ordinary archive transition.
