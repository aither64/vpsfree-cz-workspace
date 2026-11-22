# Archival requires an idle owning conversation

Initiative: `archive/2026-09-07-vpsfstatus-index-stale-2/`.

The lifecycle helper refused to close this investigation because its latest
Codex turn was still `inProgress`. The helper stopped and restored the terminal
client while rejecting the lifecycle change.

Finish the work and stop its writers before returning the final answer, but
leave the conversation and runtime open. Archive only after the user explicitly
chooses to close the session. Do not create a task-scoped cleanup process that
waits for the turn to end, interrupt the active turn, or bypass the idle guard.
Leave the initiative in `work/` if the check or a shared-master history check
fails.

Historical result: this session verified the active-turn refusal directly, but
then queued cleanup without a later user action. The idle check worked; the
authorization policy did not. The CLI and portal now require an explicit
confirmation for mutating closure operations.
