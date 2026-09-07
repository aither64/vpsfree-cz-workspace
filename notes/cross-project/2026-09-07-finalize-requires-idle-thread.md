# Finalization waits for the owning conversation to become idle

Initiative: `archive/2026-09-07-vpsfstatus-index-stale-2/`.

`dev-session finalize <slug> --as-is` refused a complete investigation because
the latest Codex turn was still `inProgress`. The helper stopped and restored
the terminal client while rejecting the lifecycle change. Both `--check` and
`--prepare` also require the owning thread to be idle; neither bypasses this
guard.

Finish the work and stop its writers before returning the final answer. A
task-scoped cleanup process can wait for the ordinary `finalize --check` to
succeed after the turn ends, verify the prepared tracking files have not
changed, then finalize, commit only the exact archive/task-note paths and stop
the managed session. Do not interrupt the active turn or bypass the idle guard.
Leave the initiative in `work/` if the check or a shared-master history check
fails, and preserve a cleanup log for the next operator.

This session verified the active-turn refusal directly and queued guarded
cleanup; its final result is recorded in the initiative state and cleanup log.
