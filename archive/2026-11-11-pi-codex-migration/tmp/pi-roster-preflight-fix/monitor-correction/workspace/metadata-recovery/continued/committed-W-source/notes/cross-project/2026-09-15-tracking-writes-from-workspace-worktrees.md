# Use the shared absolute tracking path from workspace feature worktrees

A script run from `worktrees/<slug>/workspace` used a relative `work/<slug>` path.
It appended to the feature checkout's historical state.md, then failed because
that checkout did not contain the active portal.yml. The shared coordination
records were elsewhere. Only the accidental owned edit was restored, and the
script was rerun against the absolute shared workspace root.

Workspace feature worktrees can contain committed tracking records, so existence
of state.md does not prove that a relative path targets active coordination.
Pass the shared absolute tracking directory explicitly in scripts. The feature
checkout was clean again; its clean-source deployment-contract check passed and
the site package derivation was unchanged.

Related: `work/2026-09-15-portal-diff-highlighting/`.
