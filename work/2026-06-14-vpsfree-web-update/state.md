---
lifecycle: active
---
# 2026-06-14-vpsfree-web-update

## Repositories

- `vpsfree-cz-configuration`
  - branch: `2026-06-14-vpsfree-web-update`
  - worktree:
    `worktrees/2026-06-14-vpsfree-web-update/vpsfree-cz-configuration`

## Status

- Created feature worktree from `origin/master` at `61305ff0`.
- Current `vpsfreeWeb` lock: `b6a55b769e75d2bf73aa6ea6d7bb6bf83cfcfd75`.
- Verified latest `git@github.com:vpsfreecz/web.git` `master`/`HEAD`:
  `bae16b505ce3cdea043a9e6be9bd0ffdb7f9c3b8`.
- Updated `vpsfreeWeb` to `bae16b505ce3cdea043a9e6be9bd0ffdb7f9c3b8`.
- Commit created:
  `5ea20a9b inputs: update vpsfreeWeb to bae16b50`.
- Fast-forwarded `master` to `5ea20a9b` and pushed it to origin.

## Commands run

- `bin/dev-session current`
- `git --git-dir=repos/vpsfree-cz-configuration.git remote -v`
- `git --git-dir=repos/vpsfree-cz-configuration.git fetch origin --prune`
- `git --git-dir=repos/vpsfree-cz-configuration.git worktree add -b 2026-06-14-vpsfree-web-update worktrees/2026-06-14-vpsfree-web-update/vpsfree-cz-configuration origin/master`
- `git ls-remote git@github.com:vpsfreecz/web.git HEAD refs/heads/master refs/heads/main`
- `nix develop --accept-flake-config -c bundle exec overcommit --install`
- `nix develop --accept-flake-config -c bundle exec overcommit --sign`
- `nix develop --accept-flake-config -c confctl inputs channel update --commit vpsfree-web`
- `nix develop --accept-flake-config -c confctl build "cz.vpsfree/containers/int.web"`
- `nix develop --accept-flake-config -c confctl build -y "cz.vpsfree/containers/int.web"`
- `curl -LfsS https://vpsfree.org/registration/fyzicka-osoba/`
- `curl -LfsS https://vpsfree.org/js/form.js`
- `curl -i -sS -X POST https://vpsfree.org/prihlaska/send.php -d 'entity_type=fyzicka'`
- `curl -i -sS -X POST https://vpsfree.org/registration/send.php -d 'entity_type=fyzicka'`
- `git --git-dir=repos/vpsfree-cz-configuration.git fetch origin --prune`
- `git --git-dir=repos/vpsfree-cz-configuration.git worktree add --detach worktrees/2026-06-14-vpsfree-web-update/vpsfree-cz-configuration-master origin/master`
- `nix develop --accept-flake-config -c git merge --ff-only 2026-06-14-vpsfree-web-update`
- `nix develop --accept-flake-config -c confctl build -y "cz.vpsfree/containers/int.web"`
- `nix develop --accept-flake-config -c git push origin HEAD:master`
- `git --git-dir=repos/vpsfree-cz-configuration.git worktree remove worktrees/2026-06-14-vpsfree-web-update/vpsfree-cz-configuration-master`
- `git --git-dir=repos/vpsfree-cz-configuration.git worktree remove worktrees/2026-06-14-vpsfree-web-update/vpsfree-cz-configuration`
- `git --git-dir=repos/vpsfree-cz-configuration.git update-ref refs/heads/master refs/remotes/origin/master`

## Results

- Worktree checkout succeeded, but the checkout hook reported missing bundled
  gems in the ambient shell. Use `nix develop` for repository commands so the
  documented dev environment installs/uses the expected tooling.
- Overcommit hooks were installed and signed from the dev shell.
- `confctl inputs channel update --commit vpsfree-web` created commit
  `5ea20a9b`. Pre-commit hooks passed. Commit-msg hooks passed with a generated
  message width warning on the changelog line.
- Lockfile diff changes only `vpsfreeWeb`:
  `b6a55b769e75d2bf73aa6ea6d7bb6bf83cfcfd75` ->
  `bae16b505ce3cdea043a9e6be9bd0ffdb7f9c3b8`.
- Initial `confctl build "cz.vpsfree/containers/int.web"` did not build because
  it reached the interactive confirmation prompt and exited on EOF.
- `confctl build -y "cz.vpsfree/containers/int.web"` succeeded and built
  generation `2026-06-14--09-24-52`.
- Live `https://vpsfree.org/registration/fyzicka-osoba/` still served the old
  static form action `/prihlaska/send.php`, matching deployed
  `/etc/confctl/inputs-info.json` with `vpsfreeWeb` at `b6a55b76`.
- Live `/js/form.js` matched the old `b6a55b76` JavaScript, which rewrites the
  form action in the browser DOM to `/registration/send.php`. This explains why
  browser developer tools can show the corrected action while page source still
  shows the broken static action.
- Posting to `https://vpsfree.org/prihlaska/send.php` returned HTTP 404 with
  body `File not found.`. Posting to
  `https://vpsfree.org/registration/send.php` reached the form handler.
- Temporary detached master worktree fast-forwarded from `61305ff0` to
  `5ea20a9b`.
- Merged master validation build succeeded and built generation
  `2026-06-14--09-35-06` for `cz.vpsfree/containers/int.web`.
- Pushed `5ea20a9b` to `origin/master`.
- Local bare `master` and `origin/master` both point to `5ea20a9b`.
- Removed the feature and temporary merge worktrees. Kept local and remote
  feature branches, per workspace cleanup policy.

## Open questions

- None.

## Cleanup

- Done. Feature and temporary merge worktrees were removed. Branch refs were
  kept.

## Archival request, 2026-10-06

The workspace operator requested archival of sessions dated August 2026 or
older, retaining recorded work and branches. This checkpoint commits the
existing plan and active state before the ordinary archive transition.
