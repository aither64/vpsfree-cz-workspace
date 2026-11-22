# Capture comparisons for changed branches before merging

`dev-session worktree capture-comparison` refuses an unchanged branch whose head
already equals its default branch. Automatic selection reports that the base is
no longer available; explicitly supplying the identical base/head reports
“comparison base and head are identical”. There is no change to capture in this
case. Record the unchanged SHA and let archive prove its remote ancestry.

Comparison snapshots are immutable per feature head. A second capture with a
different base fails with “a different comparison is already saved for this
head”. For workspace features, the automatically selected remote default may
precede shared local master because coordination commits have not been pushed.
That comparison validly includes those commits; record the narrower reviewed
base in state rather than rewriting the saved snapshot. Choose an explicit
known base on the first capture when a narrower comparison is needed.

Verified during `archive/2026-09-14-portal-planning-question-controls/`: generic,
organization and workspace snapshots were saved; unchanged codex-web at
6335da93acdcc82cc26200d2fbc7f479655aa7c3 has no comparison. Workspace snapshot base
8fed27b0e5210a47c66d461a8ca8d35d6b15cdf2 is the actual pre-push remote default;
its reviewed feature base is shared local master f523eddf3e1d1cdebf445992318247030e11c7f3.
