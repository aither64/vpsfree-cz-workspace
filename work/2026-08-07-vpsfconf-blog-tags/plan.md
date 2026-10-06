# 2026-08-07-vpsfconf-blog-tags

## Goal

Change the `int.blog` machine tag from `manual-update` to `auto-update`, merge
the configuration change into `master`, and clean up temporary worktrees.

## Affected repositories

- `vpsfree-cz-configuration`

## Approach

1. Fetch the latest upstream `master` and create the initiative feature branch
   and worktree.
2. Locate the `int.blog` machine definition and replace only its update-policy
   tag.
3. Run the repository-prescribed hooks and focused configuration checks.
4. Commit the change, fast-forward it through a fresh integration worktree,
   test and push `master`, then remove both temporary worktrees.

## Compatibility and deployment

This is an operational policy metadata change. It does not alter persistent
state, schemas, APIs, protocols, generated interfaces, or NixOS module options.
Mixed-version operation is unaffected. After deployment, `int.blog` becomes
eligible for the existing automatic update workflow; rollback consists of
restoring the `manual-update` tag. No coordinated machine or node update is
required.

## Testing plan

- Run the repository's configured pre-commit hook suite for the changed file.
- Run a focused configuration evaluation/check for `int.blog` if the repository
  provides one.
- Verify the committed diff changes only the intended tag.
- Re-run the relevant quick verification from the fresh `master` integration
  worktree before pushing.

This is a mechanical tag-only update, so the mandatory standalone change review
is not required.
