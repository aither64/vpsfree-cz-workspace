# Do not unconditionally drop after `git stash pop`

## Symptom

A history-rewrite workflow ran `git stash pop` and then an unconditional
`git stash drop stash@{0}`. When the pop applied cleanly, Git had already
dropped that entry, so the second command targeted the next, unrelated stash.

## Recovery

Git printed the dropped stash object's commit ID. Recreate the entry with
`git stash store -m '<original message>' <object-id>` and verify its message
and position with `git stash list`.

## Safer workflow

After `git stash pop`, inspect its exit status and `git stash list`. Drop an
entry manually only when the pop reports conflicts and explicitly says that
the entry was retained. Never assume `stash@{0}` still identifies the popped
entry.

This was verified while rewriting vpsAdmin history for
`work/2026-07-13-security-advisory-automation`; the unrelated stash was
restored immediately and no worktree data was lost.
