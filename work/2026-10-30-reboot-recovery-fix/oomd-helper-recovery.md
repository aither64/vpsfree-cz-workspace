# OOMD recovery obstruction

The provider fix verifies the first two requested sessions, but OOMD has twelve
additional saved `exec` conversations in its exact tracking directory. They are
outside its retained eight-subject team. The existing exact-set guard therefore
correctly refuses with `unknown or changed Codex thread uses the session
directory; refusing archive`. No threads are loaded. All twelve latest turns
were positively read as completed.

Proposed recovery: archive only the following completed auxiliary Codex
conversations through the native archive API after rechecking identities,
inactivity, queues, active goals and submissions. Keep their history, the parent
session, all retained team members, worktrees and records. Do not delete files
or alter rosters. Require explicit user direction before this archival.

- 01a18e58-ddca-7c52-9fc2-abbd4739ce4f
- 01a18e5b-a74e-7fa1-b8e6-3d47f6ec0931
- 01a18e66-c068-7511-86a8-55fc82d4b8b1
- 01a18e71-8f67-75a1-baad-6f8a76639cd6
- 01a18e7d-46d6-7fb0-8f90-9d8db8c2f4d8
- 01a18e7d-9f58-7ed0-8ab0-fe8ca5d676f1
- 01a18e98-4735-7221-af18-6cf444a0e99e
- 01a18e9c-4d29-70a0-a9d6-c57a2069ba96
- 01a18e9e-816a-78e2-b626-8333aa047f24
- 01a18ea5-1e9a-7793-961e-8aa3723dae7a
- 01a18ea9-2abb-7f00-8c40-db981812e519
- 01a18ead-6767-7371-af1e-a49b35c021b5

Preflight completed with the public client against the selected socket and
its persistent SQLite submission store: all twelve identities match the exact
OOMD CWD, source exec, no project, and native notLoaded status. All are idle,
with no queue, pending request, active goal or unresolved submission. No archival
has been performed. The exact user approval question is pending.
