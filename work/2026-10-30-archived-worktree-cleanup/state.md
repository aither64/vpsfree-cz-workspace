---
lifecycle: active
---

# 2026-10-30-archived-worktree-cleanup

## Current phase: setup and bounded design

- [x] Diagnose disk use and the compaction refusal without modifying archives.
- [x] Obtain explicit authorization for tracking, all-session recovery cleanup,
  necessary deployment, and integration after successful validation.
- [x] Create initiative with the installed dev-session command.
- [ ] Commit initial plan/state and register the dedicated workspace worktree.
- [ ] Implement and commit the fix; pass focused checks.
- [ ] Complete independent whole-branch review.
- [ ] Complete longer verification and any required deployment.
- [ ] Compact eligible archived sessions and verify retention and reclaimed space.
- [ ] Merge exact final feature heads and record remaining exclusions.

## Identity and ownership

Created this initiative from the previously untracked conversation with
`dev-session start archived-worktree-cleanup --no-attach --no-codex --json`.
The returned slug is `2026-10-30-archived-worktree-cleanup`; explicit matching
DEV_SESSION_SLUG/DEV_SESSION_WORKSPACE subsequently passed `dev-session current`.
No managed Codex lead or retained team exists (`team list` reports no valid lead
thread), so application work stays with this conversation's lead. Required final
review uses the installed catalog standalone fallback; verification uses its
separate utility policy. No roster or member settings were invented/changed.

## Existing evidence

The prior investigation measured 24.60 GiB under private archived-worktrees.
Archive creation switched to full local snapshots on October 12; the deployed
October 25 policy retains committed heads only for new captures, with explicit
compaction for predecessor snapshots.

The Rust-client-generator archive (2026-10-18, archived October 24) contains
9,942,306,816 allocated bytes. All tracked files in its three saved worktrees
match their retained commits; staged differences are empty and all additional
files are ignored. Most space is Rust target/build output.

The existing cleanup preview refuses this completed archive because
`bin/compact-session-storage:66` treats every SLUG.*.json file as an unfinished
journal. Its only matching file is SLUG.creation.json with state ready; tracking
sync is synced. No lifecycle journal, coordinated job, or reservation was found
for that session. No data has been deleted and no runtime metadata has changed.

## Repositories and constraints

Workspace feature branch/worktree: 2026-10-30-archived-worktree-cleanup,
worktrees/2026-10-30-archived-worktree-cleanup/workspace (creation requested).
Shared master has many unrelated modifications/untracked files; preserve all of
them and stage only this initiative's tracking paths. No workspace hook framework
or configured hooksPath was found; repository Git hooks must not be bypassed.

Selected runtime at investigation:
/nix/store/d97nazmvhm2a2m3jn8ichid4ksannliq-dev-workspace-0.2.0,
archiveRecoveryPolicy 3. Recheck selection after taking transition admission.

## Next action

Finish initial tracking commit, inspect the dedicated source worktree, implement
the smallest correction with regression coverage, and inventory all old recovery
roots. Deployment is authorized if needed; do not manufacture configuration
changes for a workspace-only maintenance-script fix.

## Links

- [Plan](plan.md)
- [Storage operation guide](../../docs/operations/workspace-storage-retention.md)
- [Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-30-archived-worktree-cleanup/)
