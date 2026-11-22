# Selecting a team after precommitting session tracking

In `2026-09-26-codex-queue-ledger-capacity`, `dev-session start <slug> --as-is
--team delegated` refused an exact slug that already had committed `plan.md`
and `state.md`: team selection is accepted only for a fresh session destination.
Starting the exact slug without `--team` and then running `dev-session team
preset <slug> delegated --as-is` created the intended ready roster. A
noninteractive start also requires `--goal-file`; its goal is submitted to the
new root thread and may start work immediately, so coordinate writers before
creating project worktrees. The session creation took about 90 seconds and
restarted its terminal Codex client after an App Server disconnect, then
completed successfully.

Related initiative: `work/2026-09-26-codex-queue-ledger-capacity/`.
