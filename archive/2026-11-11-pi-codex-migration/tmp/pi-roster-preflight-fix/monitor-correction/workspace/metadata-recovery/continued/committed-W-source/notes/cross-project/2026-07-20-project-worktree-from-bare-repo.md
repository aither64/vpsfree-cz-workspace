# Create project worktrees from the canonical bare repository

## Symptom

Running `git worktree add` from the coordination workspace root creates a
worktree of the top-level coordination repository, even when the intended path
is named after an independent project. Repository hooks may then run against
the wrong project.

## Cause

`git worktree` acts on the repository identified by the current working
directory. The destination path does not select the project repository.

## Safe form

Invoke the canonical bare clone explicitly:

```sh
git --git-dir=repos/PROJECT.git worktree add \\
  -b FEATURE_BRANCH worktrees/INITIATIVE/PROJECT origin/master
```

Verify the new worktree's `origin`, branch, and HEAD before changing files.
If the wrong top-level worktree was created and is still clean, remove it with
the top-level repository's `git worktree remove` and delete only its temporary
branch.

Verified while correcting downstream pins for
`work/2026-07-20-kernel-boot-evidence-history/`.
