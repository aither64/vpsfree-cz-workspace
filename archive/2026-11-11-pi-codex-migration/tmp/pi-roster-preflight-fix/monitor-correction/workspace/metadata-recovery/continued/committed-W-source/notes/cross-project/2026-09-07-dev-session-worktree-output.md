# `dev-session worktree add` has no JSON output option

## Symptom

`dev-session worktree add SLUG PROJECT --as-is --json` exits with `invalid
option: --json`.

## Cause

The `worktree add` subcommand does not implement the `--json` option accepted
by `dev-session start`.

## Workaround

Run `dev-session worktree add SLUG PROJECT --as-is` and read the worktree path
from its plain-text output. Confirm the result in `work/SLUG/portal.yml`.

## Verification

The command without `--json` created and registered both worktrees for
`work/2026-09-07-fix-ip-charged-environments`.
