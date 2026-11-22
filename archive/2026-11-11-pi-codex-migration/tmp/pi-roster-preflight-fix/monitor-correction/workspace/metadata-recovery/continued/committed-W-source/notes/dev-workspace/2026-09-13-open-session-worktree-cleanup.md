# Removing worktrees while keeping a session open

`dev-session worktree remove <slug> <project> --as-is` records the final head and
removes the verified worktree without deleting its branch or stopping the
conversation. Use it for registered feature worktrees; remove unregistered,
detached merge worktrees directly with non-force `git worktree remove`.

The current portal resolves unarchived repository history and status through
the attached canonical worktree, even when state.md says lifecycle: complete.
After removal, conversation and artifacts remain available but repository
browsing requires restoring that retained branch/worktree. Recorded final heads
are used for archived repository views. Cleanup does not authorize archival.

Verified in portal/internal/repository/review.go and status.go at dev-workspace
8f75ece; related initiative: work/2026-09-13-portal-recovery/.
