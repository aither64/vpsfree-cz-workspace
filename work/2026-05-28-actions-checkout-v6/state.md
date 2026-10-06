---
lifecycle: active
---
# actions/checkout v6 state

## Goal

Update vpsfree-irc-bot GitHub workflows from actions/checkout@v4 to @v6 and
merge directly to master. Do not touch vpsfree-cz-configuration.

## Repositories

- vpsfree-irc-bot only.

## Status

- Started.

## Commands run

- Created detached worktree from `vpsfree-irc-bot` `origin/master` at
  `worktrees/2026-05-28-actions-checkout-v6/vpsfree-irc-bot`.
- Updated all three bot workflows from `actions/checkout@v4` to
  `actions/checkout@v6`:
  - `.github/workflows/rspec.yml`
  - `.github/workflows/daily-update.yml`
  - `.github/workflows/nixpkgs-update.yml`
- Ran `git diff --check`: passed.
- Ran `nix shell github:NixOS/nixpkgs/nixos-unstable#actionlint -c actionlint`:
  passed.
- Committed `6db629e` `Update GitHub checkout action to v6`.
- Verified the commit fast-forwards current `origin/master` and pushed
  `vpsfree-irc-bot` `master` to `6db629e`.
- Watched GitHub Actions RSpec run `26590838069`: passed, using
  `actions/checkout@v6`.

## Status

- Complete. `vpsfree-cz-configuration` was not touched.

## Cleanup

- Remove the temporary bot worktree.
- Removed the temporary bot worktree after merge.

## Archival request, 2026-10-06

The workspace operator requested archival of sessions dated August 2026 or
older, retaining recorded work and branches. This checkpoint commits the
existing plan and active state before the ordinary archive transition.
