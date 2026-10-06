# 2026-06-11-vpsfconf-llm-agents-update

## Goal
Add a conditional `llm-agents` flake input update to
`vpsfree-cz-configuration`'s daily GitHub workflow. The input should be updated
only when upstream `numtide/llm-agents.nix` changes the Codex package version
used by `cz.vpsfree/machines/aitherdev`.

## Affected repositories
- `vpsfree-cz-configuration`

## Approach
- Modify `.github/workflows/daily-update.yml`.
- After the existing input updates, evaluate the currently pinned Codex version
  from `builtins.getFlake (toString ./.)`.
- Evaluate the upstream Codex version from
  `github:numtide/llm-agents.nix#packages.x86_64-linux.codex.version`.
- Skip the `llm-agents` update when the versions match.
- When versions differ, run
  `nix develop --accept-flake-config -c confctl inputs channel update --commit --no-changelog llm-agents`.
- Re-evaluate the pinned Codex version after the update and fail the workflow if
  it does not match the upstream version.

## Compatibility and deployment
- No machine configuration, API, database, or persisted state changes.
- The only runtime effect is that future daily workflow runs may create an
  automated `inputs: update llm-agents ...` commit when Codex changes upstream.
- The workflow keeps using `confctl inputs` for flake input changes and keeps
  changelogs disabled for `llm-agents`.

## Testing plan
- Evaluate the currently pinned Codex version from the checked-out flake.
- Evaluate the upstream Codex version from `numtide/llm-agents.nix`.
- Run the update path in a disposable checkout to confirm `confctl` accepts the
  `llm-agents` channel update and the updated Codex version matches upstream.
- Run the skip path in a disposable checkout after the update to confirm it
  exits cleanly without further changes.
