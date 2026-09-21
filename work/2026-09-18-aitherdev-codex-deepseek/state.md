---
lifecycle: active
---

# 2026-09-18-aitherdev-codex-deepseek

## Status

The native DeepSeek Codex configuration was deployed to aitherdev. Build,
dry activation, switch deployment, and host health checks passed. The one
provider smoke test is blocked because the existing DeepSeek API key is
rejected upstream.

## Next actions

- Replace `/home/aither/.codex/deepseek-key` with a valid DeepSeek API key.
- Re-run one `codex-ds exec --ephemeral` smoke request after rotating the key.
- Keep the feature branch unmerged until explicit integration direction.

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
  login. A subsequent native request retried without a response; a direct,
  redacted Responses API probe returned HTTP 401 `authentication_error` for the
  installed key. No credential value was recorded.

## Open questions

- The existing `/home/aither/.codex/deepseek-key` is invalid at DeepSeek. A
  valid API key is required to complete the live request acceptance check.

## Cleanup

- Do not touch unrelated dirty coordination paths or other initiative
  worktrees.
