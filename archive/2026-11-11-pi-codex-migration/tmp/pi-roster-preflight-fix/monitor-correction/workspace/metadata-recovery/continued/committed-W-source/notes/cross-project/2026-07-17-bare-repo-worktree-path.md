# Use absolute paths with bare-repository worktree commands

## Symptom

Running `git -C repos/project.git worktree add relative/path ...` against a
bare repository created an invalid worktree record that was immediately
reported as prunable. The relative path was resolved from the bare repository,
where Git also keeps its own `worktrees/` administration directory.

## Workaround

Pass an absolute destination path whenever `git worktree add` or
`git worktree move` is invoked through `git -C` on a bare repository. Remove
the invalid administrative record with `git worktree prune`, then add the
worktree again at the absolute path.

## Verification

The vpsAdmin rewrite worktree for
`work/2026-07-13-security-advisory-automation` was re-added at its absolute
workspace path, recognized normally by `git worktree list`, and later moved
to the initiative's canonical vpsAdmin path.
