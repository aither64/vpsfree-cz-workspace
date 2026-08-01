# Leave a worktree before removing it

Initiative: `work/2026-08-01-test-framework-ci`

A command removed a temporary Git worktree and then tried to delete its local
integration branch while the shell still used the removed directory as its
working directory. The branch cleanup failed with `Unable to read current
working directory`, although the worktree removal itself had succeeded.

Run `git worktree remove` and all subsequent cleanup from the coordination
workspace (or another directory that will remain present). Deleting the branch
from the workspace then completed successfully.
