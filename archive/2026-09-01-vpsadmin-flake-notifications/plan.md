# 2026-09-01-vpsadmin-flake-notifications

## Goal

Use the standard GitHub flake URL for the public
`vpsfree-notification-templates` input in production configuration while
preserving the exact locked source revision.

## Affected repositories

- `vpsfree-cz-configuration`

## Approach

1. Change the input URL from the inherited SSH Git transport to
   `github:vpsfreecz/vpsfree-notification-templates`.
2. Refresh only `vpsfreeNotificationTemplates` through `confctl` so
   `flake.lock` records the GitHub fetcher without changing the revision.
3. Verify the resolved revision and source hash, commit and push the feature
   branch, then fast-forward `master` from a fresh integration worktree.

## Compatibility and deployment

- This changes only how Nix fetches a public GitHub repository. It does not
  change the template revision, package contents, API contracts, persisted
  state, database schema, generated configuration, or service protocols.
- Existing and updated configurations can coexist; no deployment ordering or
  coordinated machine update is required.
- Rollback restores the SSH fetcher metadata and resolves the same source.

## Testing plan

- Run the repository Overcommit hooks for each commit.
- Run `git diff --check`.
- Inspect `nix flake metadata --no-write-lock-file --json` and confirm that the
  input remains at revision `9e1ddbd973703cf48a43f0e5afc2bfb392a8b676`
  with the same NAR hash.
- Confirm the lock entry uses the GitHub input type and contains no SSH URL.
- Skip mandatory standalone change review at the user's explicit request
  because this is a mechanical fetcher normalization with unchanged content.
