# Choose the comparison base before capture

`dev-session worktree capture-comparison` defaults to the merge base with
locally available `origin/<default_branch>`. In the shared workspace, local
master may include coordination commits not yet pushed, so the default capture
can include those records as well as the feature.

An attempt to replace that capture using `--base` and `--head` refused with
“a different comparison is already saved for this head”. The saved comparison
is immutable for that head; do not delete its private cache to change it.

When a narrower comparison is needed, pass the verified review/integration base
and exact feature head on the first capture. Here the existing broader capture
was retained and the feature-only base remained recorded in the review packet.
The initial captures succeeded for all three repositories.

Related initiative: `work/2026-09-15-session-documentation-review/`.
