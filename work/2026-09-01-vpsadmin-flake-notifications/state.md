# 2026-09-01-vpsadmin-flake-notifications

## Repositories

- `vpsfree-cz-configuration`
  - Bare clone: `repos/vpsfree-cz-configuration.git`
  - Branch: `2026-09-01-vpsadmin-flake-notifications`
  - Worktree:
    `worktrees/2026-09-01-vpsadmin-flake-notifications/vpsfree-cz-configuration`
  - Base: `origin/master` at
    `74f2c58be77f022b4e28401345896128edbe90b9`

## Status

- Complete: commit `94125328acb7a6f5b28cfe4d58e49ed4788d23a1`
  was fast-forwarded to `master` and pushed.
- Mandatory standalone change review will be skipped at the user's explicit
  request because the change only normalizes fetcher metadata for an unchanged
  public source revision.

## Commands run

- `bin/dev-session current`
- `git --git-dir=repos/vpsfree-cz-configuration.git fetch origin`
- `git log` / `git show` history inspection for `flake.nix`
- `gh repo view vpsfreecz/vpsfree-notification-templates ...`
- `bin/dev-session worktree add 2026-09-01-vpsadmin-flake-notifications
  vpsfree-cz-configuration --as-is --base origin/master`
- `nix develop -c bundle exec overcommit --run`
- `nix develop --no-write-lock-file -c confctl inputs update
  vpsfreeNotificationTemplates`
- `nix flake metadata --no-write-lock-file --json .`
- `nix develop --no-write-lock-file -c git push --set-upstream origin
  2026-09-01-vpsadmin-flake-notifications`
- `git merge --ff-only 2026-09-01-vpsadmin-flake-notifications` in a fresh
  integration worktree based on `origin/master`
- `nix develop --no-write-lock-file -c git push origin HEAD:master`
- `gh run list --repo vpsfreecz/vpsfree-cz-configuration --commit 94125328...`

## Results

- The URL originated on the long-lived `2026-06-15-vpsadmin-events` branch,
  where it selected an unmerged feature branch through SSH. The feature ref was
  removed when the input reached `master`, but the SSH transport remained.
- GitHub reports `vpsfreecz/vpsfree-notification-templates` as public, so no
  private-repository authentication requires the SSH form.
- Current lock revision and upstream `master` both resolve to
  `9e1ddbd973703cf48a43f0e5afc2bfb392a8b676`.
- Worktree creation reported the known ambient-shell Overcommit gem error after
  checkout. The branch and worktree were created successfully; the existing
  durable workaround is recorded in
  `notes/vpsfree-cz-configuration/2026-06-10-worktree-overcommit-gems.md`.
- Commit `94125328` changes `flake.nix` to
  `github:vpsfreecz/vpsfree-notification-templates` and rewrites only that
  input's lock representation from `git`/SSH to `github`.
- The first ambient-shell commit attempt was blocked by the active Nixfmt hook.
  The commit was rerun in `nix develop`; Nixfmt passed. The complete explicit
  Overcommit run also passed Nixfmt and RuboCop.
- `confctl inputs update` rewrote `flake.lock` but reported `No changes` because
  its change detector compares revisions and the revision intentionally stayed
  unchanged. The transport-only lock delta was included in the same commit.
- `git diff --check` passed.
- Lock and evaluated metadata both retain revision
  `9e1ddbd973703cf48a43f0e5afc2bfb392a8b676` and NAR hash
  `sha256-jA1cfa/mX500XdEl7fpTuicVhMntJUpO4PDD1vrhKek=`.
- Searches confirmed that neither `flake.nix` nor the input's lock entry retains
  the notification-template SSH URL.
- The feature branch and remote `master` both point to `94125328`.
- GitHub reported no Actions runs for this commit.
- No service deployment is needed: the resolved package contents are unchanged.

## Open questions

- None.

## Cleanup

- Feature and integration worktrees removed, including their transient Nix and
  Ruby cache directories.
- Feature and integration branch refs retained as required.
