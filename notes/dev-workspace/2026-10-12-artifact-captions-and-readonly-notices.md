# Artifact captions and read-only refresh notices

Session: [2026-10-12-session-archive-policies](../../work/2026-10-12-session-archive-policies/state.md).

A session portal failed with `artifact 0: unknown field "name"` after agents
prepended freehand artifact entries. The deployed parser required `label`.
The repair changed only the three caption keys, preserving unrelated edits.
Runtime now accepts `name` as a caption alias and provides validated atomic
`dev-session artifact add` registration; canonical writes use `label`.
The session guide and installed documentation skill own the supported command.
Shared Ruby/Go fixtures cover aliases, Unicode blank captions and precedence.

The archive browser check also exposed an older visibility callback bug.
Read-only pages omit pending-request and queue controls, but the refresh
library publishes notice state on visibility events even without a request.
Those renderers need the same explicit DOM-presence guard as other optional
controls. Browser exception stacks identified the two callbacks; the existing
Chromium/Firefox archive regression then passed with zero page errors.

The first real explicit archive also exposed a caller/provider context gap:
Ruby invoked `thread quiesce-explicit` without the workspace and private state
root required by Go. Go refused before worktree deletion. The Ruby fixtures
accepted unrelated commands, while provider tests constructed the correct
context directly. The correction passes selected context explicitly; regression
coverage now checks both caller arguments and the real Go CLI's private queue
capture before deletion. Use the aggregate Ruby harness for module tests; its
shared support classes are loaded by test/dev_session_test.rb.
