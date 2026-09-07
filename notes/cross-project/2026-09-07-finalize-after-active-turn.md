# Finalize only after the current Codex turn becomes idle

Related initiative: `archive/2026-09-05-cgroup-v1-shared-device-fix`.

`dev-session finalize` and `dev-session stop` use the portal's
`thread require-idle` check. Calling that check from the initiative's own
active Codex turn returns `is not idle ... has status "inProgress"`, even
after all project builds and tests have finished. Waiting within the same
turn cannot satisfy this condition.

Prepare all merges, CI verification, artifact cleanup, terminal tracking, and
the archive commit text before ending the turn. An independent user service
can wait for the exact thread/cwd/socket to become idle, verify that the
prepared files have not changed, and then run the normal sequence:

1. Fetch workspace origin and preserve linear shared `master`.
2. Run `dev-session finalize <slug> --as-is` without bypassing its guards.
3. Inspect and commit only the initiative's archive move and related notes.
4. Run `dev-session stop <slug> --as-is` after the archive commit.

Keep the finishing process outside the managed tmux session and project
worktrees. Treat unexpected idle-check errors or tracking changes as failures;
do not delete session authority or weaken the idle check. Keep output in the
user service journal, outside the curated archive.

For a shared index, `git commit --only -F <message> -- work/<slug>
archive/<slug> <note>` preserves unrelated staged changes. A disposable
repository check confirmed that this handles the archive move and leaves an
unrelated staged edit out of the commit and still staged afterwards.

Verification: the direct idle check rejected the active turn as expected;
the finishing script passed syntax and read-only preflight checks. Its
independent user service also verified GitHub SSH access and the installed
session helper's stable URL without changing repositories or session state.
Finalization verification: the normal helper passed the idle check,
removed both clean worktrees, and archived this initiative.
