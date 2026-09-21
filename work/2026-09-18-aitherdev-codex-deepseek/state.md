---
lifecycle: complete
---

# 2026-09-18-aitherdev-codex-deepseek

## Status

The native DeepSeek Codex configuration is deployed to aitherdev, verified
against DeepSeek, and merged into `vpsfree-cz-configuration` `master`.

## Next actions

- No further action. The user requested integration and owned-worktree cleanup.

## Documentation

- Portal: `https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-09-18-aitherdev-codex-deepseek/`
- Planned project operations page:
  `docs/operations/codex-deepseek-aitherdev.md`

## Repositories

- `vpsfree-cz-configuration`
  - branch: `2026-09-18-aitherdev-codex-deepseek`
  - worktree: `worktrees/2026-09-18-aitherdev-codex-deepseek/vpsfree-cz-configuration`
  - base: `dea3e00462e39c0141481a714b5dbabf6562b353`
  - head: `3e51235d`
  - integrated remote default head: `3e51235d`

## Commands run

- `dev-session start 2026-09-18-aitherdev-codex-deepseek --as-is --no-attach --no-codex --json`
- `dev-session worktree add ... vpsfree-cz-configuration --as-is --branch 2026-09-18-aitherdev-codex-deepseek --base origin/master --no-fetch`
- `nix develop --command nixfmt --check cluster/cz.vpsfree/machines/aitherdev/config.nix`
- `jq empty packages/codex-deepseek-models/models.json`
- `nix develop --command bundle exec overcommit --run pre_commit`
- `nix develop --command git rebase origin/master`
- `nix develop --command confctl build -y cz.vpsfree/machines/aitherdev`
- `nix develop --command confctl deploy -y cz.vpsfree/machines/aitherdev dry-activate`
- `nix develop --command confctl deploy -y cz.vpsfree/machines/aitherdev switch`
- `codex-ds exec --ephemeral --skip-git-repo-check --sandbox read-only ...`
- `git merge --ff-only 3e51235d...` in a fresh worktree at `origin/master`
- `git push origin HEAD:master`

## Results

- Session and project worktree created.
- Commit `3e51235d` replaces the localhost proxy with the native DeepSeek
  Responses API profile, vends DeepSeek's model catalog, removes the proxy
  service/package, and adds the aitherdev operations page.
- Local formatting, JSON, and installed pre-commit hooks passed. The commit was
  rebased onto `origin/master` at `dea3e004`.
- The user-directed general review (`gpt-5.6-terra`, high effort) returned no
  findings. Other review lanes were explicitly skipped.
- Build passed in about six minutes; dry activation passed in about 111 seconds;
  switch deployment passed in about 104 seconds with two health checks passing.
  No local kernel build occurred.
- The deployed profile parses, the wrapper is available from the aither user
  profile, and the legacy proxy service, listener, and state directory are
  absent. The first Codex invocation cleared a conflicting inherited ChatGPT
  login. After the user rotated the key, a native request to `deepseek-v4-pro`
  returned exactly `OK` using the `ds` profile.
- A fresh detached worktree fast-forwarded `origin/master` from `dea3e004` to
  `3e51235d`. Hooks, model-catalog JSON validation, and diff checks passed;
  the update was pushed to `git@github.com:vpsfreecz/vpsfree-cz-configuration.git`.
- Git confirms `3e51235d` is an ancestor of current `origin/master`. The
  temporary merge worktree and initiative configuration worktree were removed.
  The feature branch was retained.

## Open questions

- None.

## Cleanup

- The temporary merge worktree and the initiative configuration worktree were
  removed. The feature branch remains retained after integration. The completed
  session record remains in `work/` because archival was not explicitly
  requested.
