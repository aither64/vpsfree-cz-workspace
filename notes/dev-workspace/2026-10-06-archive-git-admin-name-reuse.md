# Git administration names can block a retained archive receipt

An ordinary retry of the September 18 portal archive refused with
"archive worktree path or registration remains after removal", although the
sealed old checkout paths and their registrations were absent. Git had reused
two removed administration directory names for new worktrees in this fix
initiative. The current inode identities differed from the sealed inventory,
and their gitdir files pointed to our new worktrees. The cleanup reader checks
administration-path absence even after Git reuses the name.

After the user authorized resuming the archive, and after builds finished,
we removed only the two clean fix-owned worktrees with ordinary non-force
`git worktree remove`. Their exact commits and published branches were retained.
The unchanged installed archive retry then completed all retained-head,
conversation and runtime proofs and cleared both receipts. Ordinary
`dev-session worktree add ... --as-is --no-fetch` restored the same fix branches
at their unchanged heads afterward.

This workaround was possible because both colliding live registrations belonged
to this fix initiative. A collision with another initiative's live worktree
requires its owner to release it. Do not remove another owner's checkout, edit
the sealed receipt, prune the repository globally or delete an administration
directory. Inspect both filesystem identity and the gitdir pointer first.

Evidence and authorization are retained in
[the session state](../../work/2026-10-06-cluster-status-metadata/state.md).
