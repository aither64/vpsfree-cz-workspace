# em1 auto-update tag

## Goal

Add the `auto-update` tag to the `em1` machine in
`vpsfree-cz-configuration`, merge the change to `master`, push it, and clean up
temporary worktrees.

## Affected repositories

- `vpsfree-cz-configuration`

## Approach

1. Fetch `origin/master` in the canonical bare clone.
2. Create feature branch and worktree
   `2026-06-05-em1-auto-update-tag`.
3. Read repository-local instructions.
4. Add the tag to the existing `em1` machine declaration.
5. Run repository-appropriate validation and hooks.
6. Commit the functional change.
7. Rebase if needed, fast-forward `master`, push `master`.
8. Remove temporary worktrees after successful push.

## Compatibility and deployment

This is a configuration metadata change only. It does not alter persisted state,
database schemas, API contracts, generated clients, protocol formats, or NixOS
module interfaces.

The expected deployment impact is limited to whatever automation consumes the
`auto-update` machine tag. Mixed-version operation is not a concern because no
runtime component contract changes. Rollback is expected to be the inverse
configuration change, removing the tag from `em1`.

## Testing plan

- Inspect the changed Nix expression.
- Run the repository's configured pre-commit hooks before committing.
- Run a focused syntax/evaluation check if the repository documents one for
  machine/tag changes and it is practical in the available environment.
