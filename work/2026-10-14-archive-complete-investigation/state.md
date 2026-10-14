---
lifecycle: active
---

# 2026-10-14-archive-complete-investigation

## Status

Root cause confirmed and reproduced in the installed package. The affected
session has valid `lifecycle: complete`; explicit archive chooses `archived` but
the older conversion helper refuses every different non-active source lifecycle.

Phase checklist:

- [x] Inspect affected session state and selected runtime implementation.
- [x] Trace the error and identify the introducing change.
- [x] Reproduce through the installed pure helper with actual session content.
- [ ] Finish durable diagnosis and handoff.

No application changes, independent review, deployment or successful archival
are claimed. Investigation-only evidence does not trigger mandatory change review.

## Next actions

Record the reusable diagnosis and report the required implementation correction.
Any implementation must correct `tracking_lifecycle_content` and test explicit
archival from complete and abandoned states, preserving strict-mode policy.

## Documentation

The owning runtime's `docs/dev-sessions.md` and
`docs/session-archive-recovery.md` already specify neutral explicit archival.
The workspace lifecycle procedure agrees. The implementation contradicts them.

## Repositories

No feature branches or worktrees are registered for this investigation.
The session was created with `dev-session start
2026-10-14-archive-complete-investigation --as-is --no-codex --no-attach --json`.
It retains an ordinary threadless manifest and managed shell. Team listing
requires a lead Codex thread and therefore refuses this threadless session;
no retained members were created or assigned.

## Commands run

- Read the applicable workspace procedures and documentation/handoff skills.
- Read the affected state, runtime recovery guide, installed executor and
  matching upstream source/tests.
- Invoke installed Ruby with `DevSession::Runner.allocate` and call only
  `tracking_lifecycle_content`/`lifecycle_state`; no CLI archive was executed.
- Inspect introducing commit `f02ed71165ebc6d64e70a21248ba84bdc55366d2`.

## Results

Selected runtime:
`/nix/store/2jxac4wqrj2j7sk2czi0p0fdfznn14wj-dev-workspace-0.2.0`.
The stable command at `/home/aither/bin/dev-session` dispatches this package.

Actual input lifecycle: `complete`. Installed helper results for target
`archived`:

| Source | Result |
| --- | --- |
| active | archived |
| complete | exact reported error |
| abandoned | same refusal with abandoned in the message |
| archived | unchanged archived |

Actual affected session content reproduces the exact reported error.

`archive` at line 1855 chooses `archived` for explicit calls and its top-level
preflight at line 1891 permits every valid source lifecycle. During
`prepare_archive_journal!` (line 6860), `archived_tracking_identity` (line 6780)
calls `tracking_lifecycle_content` (line 7331). That method returns for an
already matching lifecycle, otherwise insists on `active` and raises at line
7335. Its substitution also hardcodes `lifecycle: active`, so changing only the
guard would leave a completed state's header unchanged.

The October 12 explicit-archive change `f02ed711` changed the target, entry
preflight, CLI and recovery formats but left this older helper unchanged.
Explicit archive tests exercise active fixtures; existing complete-state tests
invoke the strict internal default (`explicit: false`), which targets complete
and returns before the faulty guard.

The failure happens before the archive journal and cleanup sidecar are written
and before checkout removal or tracking move. Earlier preflight can already
quiesce owned agents and capture private worktree recovery. No archive-related
lock filenames for the affected slug were found in `worktrees/.locks/` during
inspection. All ten worktree directories remain listed; tracking remains under
`work/`. This investigation has not changed the affected session.

## Open questions

No unresolved question about the reported refusal. The next gates after a future
fix were not executed, so diagnosis does not certify full archival success.

## Cleanup

Retain this investigation's managed shell and tracking. No archive/delete/stop
was requested for the investigation, and branches in the affected initiative
remain untouched. The shared master has many unrelated working-tree changes;
stage only owned investigation records and the diagnostic note.
