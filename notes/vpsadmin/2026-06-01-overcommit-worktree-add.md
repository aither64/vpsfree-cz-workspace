# vpsadmin Overcommit during worktree add

Related initiative:
`work/2026-06-01-vpsfree-irc-bot-integration-tests`

Command/workflow:

- `git worktree add --detach .../vpsadmin origin/master` from
  `repos/vpsadmin.git`

Symptom:

- The worktree was checked out, but the command exited with status 1.
- Output included:
  `Signature of configuration file has changed! Run overcommit --sign`.

Cause:

- vpsAdmin uses Overcommit hooks. The checkout hook can reject the worktree
  operation when the Overcommit configuration is not signed for that checkout.

Workaround:

- If the worktree will be used for commits or hook-managed checks, enter the
  repository's development environment and run `overcommit --sign` or the
  repository-documented hook setup before committing.
- For read-only reference inspection, the worktree exists and can be used after
  confirming it is clean.

Verification:

- `git status --short --branch` in the reference worktree reported detached
  `HEAD` with no file changes.
