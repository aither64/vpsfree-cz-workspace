# 2026-05-28 aitherdev gh and llm-agents

## Goal

Update `vpsfree-cz-configuration` so user `aither` has the `gh` command
available on the `aitherdev` machine, and update the `llm-agents` flake input.

## Affected repositories

- `vpsfree-cz-configuration`

## Branches and worktrees

- Branch: `2026-05-28-aitherdev-gh-llm-agents`
- Worktree: `worktrees/2026-05-28-aitherdev-gh-llm-agents/vpsfree-cz-configuration`

## Approach

- Find the `aitherdev` host configuration and user `aither` environment
  definition.
- Add the GitHub CLI package using the existing local Nix style.
- Update `llm-agents` with `confctl inputs channel update --commit
  llm-agents --no-changelog`.
- Keep the package change and generated flake input bump in separate commits if
  the input command creates its own commit.
- Verify by evaluating the affected host or the closest available build target.
- Rebase or fast-forward merge into current `master`, then push `master`.

## Compatibility and deployment

Adding `gh` to a user environment is backward compatible. Existing user state is
not migrated and no database, API, protocol, on-disk, or generated client
contract changes are expected. The package becomes available after the
`aitherdev` configuration is deployed and the user environment is rebuilt.

Updating `llm-agents` may affect automation or agent tooling that consumes that
flake input. It should not require coordinated host updates unless the new input
revision changes module options consumed by this configuration. Verification
must include evaluation of the relevant host configuration to catch option or
package incompatibilities before merge.
