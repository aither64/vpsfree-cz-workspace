# Linked worktrees need their own ignored gem directory

Related initiative: `work/2026-07-20-security-advisory-review/`

Creating a temporary linked worktree for `security-advisories` ran the shared
Overcommit post-checkout hook before that worktree had its ignored `.gems/`
directory. The worktree was created, but the command exited with missing-gem
errors from Bundler.

Run `nix develop -c bundle install` in a newly created linked worktree before
using Git operations that invoke Overcommit hooks. Run those Git operations
through `nix develop` as well, because the ambient Ruby may not match the
repository shell even after `.gems/` exists. After doing so, all three split
commits passed the repository's RuboCop pre-commit hook.
