# Archive timeout recovery and deployment

## Authorization and preflight

User authorized implementing the plan, completing the exact UCEPROTECT archive
and leaving it archived, and deploying aitherdev. Do not revive or delete it.

Preflight observation: application profile 47 selects
/nix/store/ql5prmqfml0y62z2xj4yx45sdv7ijgrz-dev-workspace-0.2.0.
Codex PID 1090021, tmux PID 435397, portal PID 4033047, router PID 4033045,
all active. Recheck immediately before activation for concurrent deployments.

Source archive journal operation:
9a6219fda3a306872793abfdffc34eae4cb99815d5b32c11ba7313523d21b5ff.
Phase tracking_committed; retained thread 01a0a4da-4f2b-7ad1-ab6d-27b3262dc671.
Exact proven project head b6e650ad902482b4c4e66b5a89a4275bed92419e.
Tracking commit 50ec47f; no attached worktree remains.

## Ordered procedure

1. Complete four-lane review and packaged/isolated-browser checks; inspect CI.
2. Recheck source journal/identity. Run installed
   dev-session archive 2026-09-15-abuse-uceprotect --as-is and answer its ordinary
   confirmation yes. This resumes the exact operation with the existing manual
   deadline. Preserve branch refs/history and unrelated sessions. If it refuses,
   diagnose that refusal without modifying journal or tracking.
3. Verify journal and source authority/runtime retired and conversation archived.
   Pending journals block package changes, so this must succeed before activation.
4. Build the consuming workspace package from the final committed feature head.
   Record its store path and run workspace-host switch --source the initiative's
   workspace worktree. Application deployment uses the user profile; the existing
   host configuration requires no update.
5. Verify selected store path, served app.js checksum and session markup, health,
   portal/router activity and retained Codex/tmux PIDs. Check source session read-only
   archived state without a pending lifecycle or historical-failure banner.
6. Record exact evidence here and in state.md. Leave feature branches and worktrees
   available for follow-up; integration into master is outside this request.

## Recovery

The old and new packages share all persisted formats. Previous profile 47 remains
available to workspace-host rollback, subject to normal pending-operation guards.
Never roll back a later concurrent deployment. No shared Codex restart is planned.

## Executed recovery

On 2026-09-16 at approximately 20:47 UTC, the installed manual archive command
completed normally: thread retired, runtime retired, archived. The exact original
operation resumed from tracking_committed without another tracking commit or
journal modification. Local and remote source feature refs both remain at
b6e650ad902482b4c4e66b5a89a4275bed92419e. Source conversation remains archived;
no revival was performed.

Post-recovery verification: source journal and authority are absent; retained
thread moved to archived_sessions and is absent from sessions. Portal operation
reports complete at 2026-09-16T20:47:21.062633803Z. Its page remains read-only with
verified retained thread identity, lifecycle=complete, empty pending lifecycle
and no composer. Archive tracking commit remains 50ec47f.

## Executed deployment

Final committed source chain:
- Runtime: 0bd68efa9cadb0589148fac40de7645a06b03468.
- Organization extension: 90ce0cfe7c39c944aca0c7b27fe1e53a719075a3.
- Consuming workspace: c60bac9f4ab92eb17a5bdae1b2fa7740c19a0e01.

Built the exact consuming workspace package and deployment-contract check, then
successfully ran workspace-host switch --source the initiative workspace worktree.
Profile 48 selects /nix/store/bspd81hp98awq942lnr7p93k38i8d8di-dev-workspace-0.2.0;
profile 47 remains available for guarded rollback. Codex protocol preflight passed
and remains on version 0.154.0. No system configuration deployment or merge occurred.

Verified after activation:
- Codex PID 1090021 and tmux PID 435397 are unchanged and active.
- Portal PID 1341341 and router PID 1341339 are active; portal /healthz returns ok.
- Automatic-archive timer is active.
- Served app.js exactly matches the runtime worktree; SHA256
  07e7d16e84fe7fa8cb828407cdcb19d5e3a417bcd350ed04e39f14c60b259578.
- Installed wrapped dev-session has THREAD_RETIRE_TIMEOUT=210 and scoped use.
- Source archived page retains verified thread identity, remains read-only with
  no composer, empty pending lifecycle and a hidden last-failure banner.
- Source operation remains archive/complete with the exact original journal ID.

## Integration and cleanup, 2026-09-17

User authorized default-branch merges and cleanup. Runtime master fast-forwarded
from eb658d49 to 0bd68ef; extension from 17da396e to 90ce0cf. Workspace pin commit
rebased unchanged over shared coordination master 33f0657 to eca34d0, then merged
fast-forward from the shared checkout and pushed. No merge commits were created.
The deployed runtime, extension and site configuration are unchanged, so profile 48
was retained without another switch or service restart.

Captured repository comparisons before integration, then removed all three clean
feature worktrees with dev-session worktree remove and both clean temporary merge
worktrees with git worktree remove. Retained local/remote feature refs, final heads
in portal.yml and saved comparisons. Session remains open; no archive/delete/stop
command was run for this initiative. Post-merge evidence is in verification.md.
