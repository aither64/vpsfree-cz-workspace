---
lifecycle: abandoned
---
# 2026-05-11 ct wrapper state

## Current status

- Feature branch fetched, worktree prepared, rebased onto current `staging`,
  regenerated osctl gem package metadata committed, merged into `staging`, and
  pushed to upstream.
- Affected repository: `vpsadminos`.

## Branches and worktrees

- Bare repository: `repos/vpsadminos.git`
- Feature branch: `2026-05-11-ct-wrapper`
- Feature worktree: removed after merge
- Temporary merge worktree: removed after push
- Base branch: `staging`
- Final local `staging` and local feature HEAD:
  `9e01370d87ec59769b8fee72eff257f8b8664a5a`
- `origin/staging` after this merge:
  `9e01370d87ec59769b8fee72eff257f8b8664a5a`
- `origin/staging` later advanced to
  `cb665cd26` by `2026-05-31-vpsadminos-firewall-notrack`; this commit is a
  descendant of the pty-wrapper merge.
- `origin/2026-05-11-ct-wrapper` was left untouched at
  `76ab40c76e08f883e048e0a5c376a27abf031ae8`.

## Commands and results

- `git -C /home/aither/workspace/vpsadmin/vpsadminos status --short --branch`
  showed the older checkout on `staging...origin/staging` with many untracked
  files; it will not be used for the rebase.
- `git -C repos/vpsadminos.git remote -v` confirmed the remote is
  `git@github.com:vpsfreecz/vpsadminos.git`.
- The older checkout's local `2026-05-11-ct-wrapper` and
  `origin/2026-05-11-ct-wrapper` both point to
  `76ab40c76e08f883e048e0a5c376a27abf031ae8`.
- Fetched `staging` and `2026-05-11-ct-wrapper` from upstream into
  `repos/vpsadminos.git`.
- Fetch updated local `staging` from `8a76972f7` to `a23367b0e` and created
  local `2026-05-11-ct-wrapper` at `76ab40c7`.
- Created worktree
  `worktrees/2026-05-11-ct-wrapper/vpsadminos`.
- `git log --oneline --reverse staging..2026-05-11-ct-wrapper` before rebase
  showed the remaining feature-side commits:
  `ctptywrapper: replace go prototype with rust wrapper`,
  `osctld: use packaged container pty wrapper`, two console tests, and the
  old generated gem update
  `os: update gems to 25.11.0.build20260526151406`.
- `git log --oneline --reverse 2026-05-11-ct-wrapper..staging` showed that
  current `staging` contains
  `dfed89a5d os: update gems to 25.11.0.build20260531170948`.
- Rebased with an interactive sequence that dropped the stale feature gem
  update commit. The rebase completed without conflicts.
- Installed Overcommit hooks with
  `nix develop --command overcommit --install`; hooks are executable in
  `repos/vpsadminos.git/hooks`.
- Ran `nix develop --command make gems`. It generated build ID
  `25.11.0.build20260603142841`, published the matching gem builds to
  `https://rubygems.vpsfree.cz/`, and updated `.build_id` plus
  `os/packages/*/{Gemfile,Gemfile.lock,gemset.nix}`.
- Committed the regenerated package metadata with a temp message file and
  `git commit -F`. Overcommit pre-commit hooks passed:
  Nixfmt and RuboCop. Commit message hooks passed:
  SingleLineSubject, TrailingPeriod, and TextWidth.
- Replacement gem commit:
  `9e01370d8 os: update gems to 25.11.0.build20260603142841`.
- Ran `nix build .#ctptywrapper`; it succeeded and fetched
  `ctptywrapper-25.11` from `https://cache.vpsadminos.org`.
- `nix develop --command cargo check --manifest-path ctptywrapper/Cargo.toml`
  failed because the default dev shell does not include Cargo.
- Ran
  `nix develop .#ctptywrapper --command cargo check --manifest-path ctptywrapper/Cargo.toml`;
  it passed.
- Removed ignored generated artifacts from this worktree:
  `result` and gem `pkg/` directories created by `nix build`/`make gems`.
- Removed untracked `ctptywrapper/target/` created by `cargo check`.
- Final `git status --short --branch` in the worktree is clean.
- Final local history on top of `staging`:
  `f04300129 ctptywrapper: replace go prototype with rust wrapper`,
  `0aa4d79ba osctld: use packaged container pty wrapper`,
  `bd927dcb4 tests: cover container console reconnect`,
  `9cdd2c470 tests: cover console terminal resize`,
  `9e01370d8 os: update gems to 25.11.0.build20260603142841`.
- `git rev-list --left-right --count origin/2026-05-11-ct-wrapper...HEAD`
  reports `5 25`; the local branch is rebased and has not been pushed.
- User asked to merge into `staging`.
- Fetched `origin/staging` again before merging; it was still
  `a23367b0e92a2b9145d333f99af7109ae0eec414`.
- Created temporary merge worktree
  `worktrees/2026-05-11-ct-wrapper/vpsadminos-merge-staging` from local
  `staging`. The checkout itself succeeded, but `git worktree add` exited with
  status 1 because the shared Overcommit post-checkout hook reported that the
  configuration signature had changed. Verified `.overcommit.yml` and ran
  `nix develop --command overcommit --sign`.
- Ran `git merge --ff-only 2026-05-11-ct-wrapper` in the temporary staging
  worktree. It fast-forwarded `staging` from `a23367b0e` to `9e01370d8`.
- Re-signed Overcommit after the fast-forward because the post-merge hook
  again reported a changed configuration signature.
- Ran `nix develop --command overcommit --run` in the merged staging worktree;
  Nixfmt and RuboCop passed.
- Ran `nix build .#ctptywrapper` in the merged staging worktree; it passed.
- Ran
  `nix develop .#ctptywrapper --command cargo check --manifest-path ctptywrapper/Cargo.toml`
  in the merged staging worktree; it passed.
- Removed generated `result` and `ctptywrapper/target` artifacts.
- Fetched `origin/staging` again before push; it was still an ancestor of local
  `staging`.
- `git push origin staging` from the ambient shell failed because the
  Overcommit pre-push hook used the ambient Ruby environment and reported a
  configuration signature mismatch. Retried with
  `nix develop --command git push origin staging`; it succeeded and pushed
  `staging` from `a23367b0e` to `9e01370d8`.
- Removed both initiative worktrees:
  `worktrees/2026-05-11-ct-wrapper/vpsadminos-merge-staging` and
  `worktrees/2026-05-11-ct-wrapper/vpsadminos`.
- Final ref check in `repos/vpsadminos.git`:
  local `staging`, `origin/staging`, and local `2026-05-11-ct-wrapper` all
  point to `9e01370d8`; `origin/2026-05-11-ct-wrapper` remains at `76ab40c7`.
- `git rev-list --left-right --count origin/staging...staging` reports `0 0`.
- GitHub Actions after pushing `staging` at `9e01370d8`:
  - RuboCop run `26885780897`: success.
  - RSpec run `26885781007`: success.
  - CI run `26885780878`: failed in the full test suite after 1h0m25s.
    Build job `79297482031` passed; test job `79297832281` failed with
    6 unexpected test failures.
- Downloaded CI artifact `os-test-logs-26885780878` to
  `/tmp/vpsadminos-ci-26885780878` for inspection. The failures were all in
  AlmaLinux/Rocky 8 scripts while creating containers:
  `cgroups/mount-v2#rocky-8`, `dist-config/systemd-rundir#rocky-8`,
  `systemd/device-units#rocky-8`, `systemd/device-units#almalinux-8`,
  `cgroups/mount-v1#almalinux-8`, `cgroups/mount-v1#rocky-8`,
  `dist-config/netif-routed#almalinux-8`, `dist-config/start-stop#rocky-8`,
  and `dist-config/start-stop#almalinux-8`.
- Representative failure: `osctl ct new --distribution rocky --version 8`
  or `osctl ct new --distribution almalinux --version 8` failed during
  rootfs import with `error: internal error` after `Writing data stream`.
- Checked recent pre-merge `staging` CI failures. Run `26716929404` from
  `2026-05-31` already showed the same AlmaLinux/Rocky 8 test family failing,
  e.g. `cgroups/mount-v2#rocky-8` and
  `dist-config/netif-routed#almalinux-8`. This makes the `9e01370d8` CI
  failure very likely unrelated to the pty-wrapper merge.
- A later push advanced `origin/staging` to `cb665cd26`, which includes
  `9e01370d8`. CI run `26889296877` for that newer staging tip also failed in
  the same pre-existing AlmaLinux/Rocky 8 family. Build job `79310380990`
  passed; test job `79310568282` failed after 1h29m with:
  `docker/almalinux#8`, `cgroups/mount-v1#almalinux-8`,
  `systemd/device-units#rocky-8`, `systemd/device-units#almalinux-8`, and
  `cgroups/mount-v2#rocky-8`.
- Latest run list confirms the pushed `9e01370d8` commit has successful
  RuboCop (`26885780897`), RSpec (`26885781007`), and Dependency Graph
  (`26885781468`) workflows. The full CI failure is not isolated to this
  pty-wrapper merge and persists on the newer staging tip.

## Notes

- Added `notes/vpsadminos/2026-06-03-ctptywrapper-dev-shell.md`.
- Added `notes/vpsadminos/2026-06-03-overcommit-nix-env.md`.

## Open questions

- None.

## Cleanup

- Feature and temporary merge worktrees removed.
- Removed temporary CI log download `/tmp/vpsadminos-ci-26885780878`.
- Removed the empty worktree group directory
  `worktrees/2026-05-11-ct-wrapper` and pruned stale git worktree metadata.

## Archival request, 2026-10-06

The workspace operator requested archival of sessions dated August 2026 or
older, retaining recorded work and branches. This checkpoint commits the
existing plan and active state before the ordinary archive transition.
