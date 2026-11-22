# Archive only after the current Codex turn becomes idle

Related initiative: `archive/2026-09-05-cgroup-v1-shared-device-fix`.

`dev-session archive` uses the portal's `thread require-idle` check. Calling
that check from the initiative's own active Codex turn returns `is not idle ...
has status "inProgress"`, even after all project builds and tests have
finished. Waiting within the same turn cannot satisfy this condition.

Finish the work and leave the session open for follow-up. Run `dev-session
archive <slug> --as-is` only after the user explicitly chooses Archive and the
turn has become idle. The single command performs and commits the tracking
move, then retires the managed conversation and runtime. Do not schedule a
user service or background process to archive after the turn.

Treat unexpected idle-check errors or tracking changes as failures. Do not
delete session authority or weaken the idle check.

Historical result: the direct idle check rejected the active turn as expected.
An independent user service later closed the initiative. That automation must
not be repeated: lifecycle completion and an idle thread are safety
preconditions, not authorization to close a session.
