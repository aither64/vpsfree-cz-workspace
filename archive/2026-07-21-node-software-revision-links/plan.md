# Node Software Revision Links

## Goal

Keep the built-in vpsAdminOS, vpsAdmin and nixpkgs commit links when a
deployment adds a repository link for the generic `system_configuration`
component. Production currently renders the first three exact revisions as
`unavailable` even though current Node evidence stores all revisions.

## Affected repositories

- `vpsadmin`: change the WebUI Nix module's standard link definitions from an
  option-level default to independently mergeable per-component defaults.
- `vpsfree-cz-configuration`: update the vpsAdmin service, staging and
  production pins to the reviewed vpsAdmin head. The existing
  `system_configuration` link remains unchanged.
- `vpsadmin-kb-captures`: update the exact vpsAdmin source pins and verify that
  the documentation contract and screenshot inventory do not drift.

The reviewed `2026-07-20-node-evidence-compat-cleanup` changes are replayed on
the current default branches so default-branch integration retains that
approved cleanup and this correction in one fast-forward chain. Repeated
unmerged dependency-pin updates are folded into one final update per channel.

## Implementation

- Give `softwareRevisionLinks` an empty option default.
- When the WebUI is enabled, define the standard `nixpkgs`, `vpsadmin` and
  `vpsadminos` keys individually with `lib.mkDefault`.
- Preserve deployment overrides and additions, including the production
  `system_configuration` repository link.
- Verify through Nix evaluation that extending the mapping produces all four
  keys and that generated PHP contains all four repository prefixes.

## Compatibility and deployment

This changes only generated WebUI configuration. It has no database, evidence
payload, daemon protocol, API, migration, Node closure or persisted-state
impact. Old and new WebUI instances can run concurrently. Rollback only
restores the misleading link rendering; evidence remains intact.

After integration, update and deploy the vpsAdmin WebUI/service configuration.
Nodes do not need a restart, reconstruction or backfill.

## Verification

- Nixfmt and focused Nix module evaluation with an added
  `system_configuration` mapping.
- vpsAdmin pre-commit hooks and flake evaluation/checks appropriate to the
  module change.
- vpsFree.cz configuration flake check and WebUI host evaluation after exact
  vpsAdmin pin updates.
- KB contract and flake checks with no screenshot or page-content changes.
- Mandatory standalone change review before default-branch integration.
