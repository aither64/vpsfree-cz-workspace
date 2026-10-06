# 2026-06-14-vpsfree-web-update

## Goal

Update the `vpsfreeWeb` flake input in `vpsfree-cz-configuration` so the
deployed vpsFree.cz presentation site uses the latest upstream
`vpsfreecz/web` commit.

## Affected repositories

- `vpsfree-cz-configuration`

## Approach

- Reuse the active workspace initiative and create a feature worktree from the
  current `origin/master`.
- Verify the current upstream `vpsfreecz/web` HEAD over SSH.
- Use `confctl inputs channel update --commit vpsfree-web` from the repository
  dev shell, rather than editing `flake.lock` manually.
- Keep the generated input bump isolated in its own commit.

## Compatibility and deployment

- The update changes the source tree consumed by the `services.vpsfree-web`
  module. It does not change schemas, protocols, generated clients, NixOS
  module options, or persisted state.
- Mixed-version operation is acceptable: only machines using the
  `vpsfree-web` input see the new website files after rebuild/deploy.
- Rollback is the normal configuration rollback to the previous flake lock;
  no new state should be written that would block rollback.
- The affected service is `cz.vpsfree/containers/int.web`; no coordinated
  vpsAdminOS node update is expected.

## Testing plan

- Inspect the lockfile diff to confirm only `vpsfreeWeb` changed.
- Evaluate/build `cz.vpsfree/containers/int.web` with `confctl build`.
- Ensure the repository Overcommit hooks are installed and run for the commit.
