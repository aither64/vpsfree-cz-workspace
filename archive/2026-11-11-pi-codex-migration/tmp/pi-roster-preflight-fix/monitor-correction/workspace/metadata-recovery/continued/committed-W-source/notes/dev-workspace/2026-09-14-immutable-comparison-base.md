# Choose comparison bases before the first capture

Initiative: work/2026-09-14-portal-review-fixes.

`dev-session worktree capture-comparison` saves an immutable comparison for a
feature head. A later capture with a different base is refused. When the desired
local review base differs from origin/master, pass recorded --base and --head
revisions on the first capture. Do not guess historical bases.

The portal-fixes workspace comparison validly used origin/master efd65e4,
including its initial tracking commit. Recapturing that head from local master
8f31bab was refused. The original comparison was preserved; the review packet
records the narrower reviewed base.
