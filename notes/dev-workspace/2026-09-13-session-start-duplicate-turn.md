# Noninteractive startup submits the goal to the managed terminal

`dev-session start <slug> --as-is --goal-file FILE --no-attach` creates the managed
conversation and submits the goal. When a coordinating agent continues in its
original external conversation, the managed terminal can begin a duplicate
implementation turn. `--no-attach` only prevents attaching the caller.

Inspect the owned tmux pane after startup. If continuing externally, interrupt
that duplicate with Escape and verify it is idle before making project edits.
Keep the terminal and session alive for follow-up. Do not interrupt another
session or adopt its identity. Here the duplicate had only read files; the
project worktrees were still clean after interruption.

Related initiative: work/2026-09-13-portal-recovery/.
