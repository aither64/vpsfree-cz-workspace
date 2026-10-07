# Sidebar menu and one-time archival, 2026-10-06

Implement the approved plan. This is a bounded sidebar edit and a one-off
operation, not a new lifecycle subsystem. Main supplies the direct brief for
this small edit; retained implementer0 owns application edits and reviewer0
owns independent final review at their saved settings. Main owns preparation,
backups, failures, deployment and tracking.

## UI brief

Add a shared vertical-ellipsis menu at the top of the existing index/session
sidebars, beside the workspace name or home link. The only new menu item is
Automatic archival at its existing /automatic-archival URL. Remove the loose
main-page link and the index's standalone Workspace heading. Keep the real
workspace label, session title and home navigation. Use a small native popover,
keyboard access, Escape/outside-click dismissal and usable desktop/compact
placement. No new framework, API, persisted format or automatic-policy change.
Existing docs may receive a short navigation sentence; main applies the writing
skill to final user-facing prose. Retain browser/Codex contracts and cache-bust
changed static assets using the existing convention.

## Actual archival

Select active dated records through 2026-08-31 inclusive, skipping exactly
2026-06-15-vpsadmin-events and 2026-07-24-ct-start-hang. The frozen current
selection contains 141 records. A short private shell loop invokes the existing
archive command, supplying its normal confirmation through script's
PTY. Log each result, skip already archived rows on rerun, and inspect failures
on demand. Do not create installed batch machinery or change archive guards.
The CLI requires a TTY; the installed script utility's child-TTY path was checked.
After the initial sequential run, use three xargs workers to shorten the remaining
batch. Once package builds have finished, the same scheduler may use six workers
while the portal stays responsive; reduce scheduling if responsiveness suffers.
Native per-session locks and the existing shared tracking-commit lock remain in
force. No native child is interrupted when changing scheduling.

User explicitly chose Archive and retain work: completed mode where exact merge
proof succeeds; abandoned mode for empty/unfinished/unprovable sessions, retaining
branches and records. Preserve dirty files in verified private backups with
recovery notes, restore only the saved tracked paths and move only the saved
untracked paths before ordinary cleanup. No resets, cleans, stashes, forced
worktree removal, fabricated refs or default-branch integration of unfinished
work. Resume any accepted journal in its original mode. The two exceptions and
September/later records remain outside this one-time operation; holds and the
existing automatic policy are unchanged.

## Verification, compatibility and rollout

Focused template/browser checks cover the removed heading/link, menu navigation,
keyboard/dismissal behavior and desktop/compact placement. Inspect the complete
new commit series and final diff, explicitly with no migrations, then run retained
independent final review before the one required package/host build. Existing
persisted formats remain unchanged; UI rollback uses the normal package path.
Deploy the UI once from the workspace user profile with matching officially
managed configuration pins, then run archival without another package switch.
Confirm every selected row is archived, both exceptions/later records remain
active, no failed journal is left, backups are recoverable and the portal responds.
Do not wait for CI or revive the previous broad acceptance matrix.

User's latest instruction overrides previous integration approval: do not merge
these features automatically. Deploy for UI review and leave runtime, workspace
and configuration feature branches unmerged until explicit approval.

## Shared-master correction discovered during the operation

A session registered on workspace/master must retain its sealed head while master
advances through ordinary tracking commits, including its own archive commit.
The bounded fix uses monotonic ancestry only for that exact shared workspace
registration. Completed mode also proves the sealed head merged into origin
master; abandoned mode keeps its publication exemption. Other feature/auxiliary
head equality and all journal, tracking, conversation and package-generation
checks remain. No format/migration is added. The retained implementer owns source
edits; quick checks and final independent review precede use. A private one-time
entry derives the entire installed host invocation and changes only the executor
to the reviewed source, retaining the installed generation and transition guard.
This lets existing journals finish before any further package switch.
