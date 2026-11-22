# Resuming a session with a completed legacy creation journal

Initiative: `work/2026-09-05-cgroup-v1-shared-device-fix`.

`dev-session start <slug> --as-is --no-attach --no-codex` rejected an old
schema-1 creation journal as invalid. It had `state: ready` and
`preserve_tracking: true`, but lacked provenance fields required by the newer
deployed helper. The existing portal was ready and revived active tracking
had already been committed.

For this explicitly user-requested resumption, inspected the deployed helper
and preserved the completed legacy journal under a dated sibling filename
while holding the per-slug lock. With the stale journal absent, the normal
start command successfully resumed the existing session and retained both
branches and the conversation. Do not apply this workaround to an incomplete
creation or another session's journal.

A shell launched outside the managed environment also needs both
`VPSFREE_DEV_SESSION_SLUG=<slug>` and
`VPSFREE_DEV_SESSION_WORKSPACE=<workspace-root>` for `dev-session current`.
Setting only the slug fails workspace identity validation.
