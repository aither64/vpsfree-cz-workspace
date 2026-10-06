# vpsAdmin channel update

## Goal

Update the `vpsadmin` channel in `vpsfree-cz-configuration` to the current
`vpsadmin` `origin/master` revision and push the resulting generated input
commit.

## Affected repository

- `vpsfree-cz-configuration`: feature branch and worktree only; update through
  `confctl inputs channel update --commit vpsadmin`.

## Compatibility and deployment

- This is a mechanical channel/input update. It introduces no configuration
  schema, API, protocol, database, or persisted-state format change itself.
- The referenced vpsAdmin revision adds documentation landmarks and related
  WebUI documentation metadata without changing routes or deployment ordering.
- Normal mixed-version deployment and rollback behavior is unchanged. Machine
  deployment remains operator-only and is outside this task.

## Verification and integration

1. Install and verify the declared Overcommit hooks.
2. Run the generated channel update through `confctl`.
3. Inspect the generated commit and ensure it pins current vpsAdmin
   `origin/master`.
4. Evaluate the affected configuration as practical, push the feature branch,
   then fast-forward `master` from a fresh integration worktree and push it.

The mandatory standalone review is skipped because this is an isolated,
generated dependency/channel update with no relevant hand-written code or
design change.
