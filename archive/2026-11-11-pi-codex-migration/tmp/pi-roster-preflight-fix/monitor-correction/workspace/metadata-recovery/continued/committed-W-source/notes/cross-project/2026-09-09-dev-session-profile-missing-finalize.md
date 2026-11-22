# Installed `dev-session` profile can lag the workspace finalizer

## Symptom

`dev-session finalize <slug> --as-is` failed with `unknown command: finalize`.
The installed helper's usage still offered the older `archive` command, while
the workspace documentation and current `libexec/dev-session` implemented the
guarded `finalize` workflow.

## Workaround

Confirm that the workspace checkout is on the intended current branch, inspect
the version-controlled helper, and invoke it directly:

```sh
./libexec/dev-session finalize <slug> --as-is
```

Do not substitute the older `archive` command without first proving that it
has the same safety and lifecycle contract.

## Verification

The workspace helper validated the terminal lifecycle and clean attached
worktrees, removed the worktrees without force, retained their branches, and
moved tracking atomically into `archive/`.

Related initiative: `archive/2026-09-07-fix-ip-charged-environments/`.
