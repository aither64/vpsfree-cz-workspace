# Overcommit can report a failed worktree add after creating the worktree

`dev-session worktree add <slug> vpsadmin --as-is --base origin/master` can exit
nonzero when vpsAdmin's inherited Overcommit `post-checkout` hook rejects an
unsigned `.overcommit.yml`. The underlying Git command may already have created
the branch and worktree, and `dev-session` may already have registered it in
`portal.yml`.

Before retrying, inspect the exact session's `git worktree list --porcelain`,
branch HEAD, `portal.yml` entry, and worktree status. In the
`2026-09-30-portal-review-improvements` session these all matched the fetched
`origin/master` head `5c76e3290481b297dcd0baa76d246133f0353d8f`, and the
worktree was clean. It was used only as read-only cluster source. If a later
task needs to commit in a vpsAdmin worktree, verify `.overcommit.yml` and sign
its hook configuration through the repository's documented Overcommit tooling
before committing; do not bypass the hook.
