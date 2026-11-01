---
lifecycle: complete
---

# 2026-10-30-archived-worktree-cleanup

## Current phase: complete; fix merged and cleanup verified

- [x] Diagnose disk use and the compaction refusal without modifying archives.
- [x] Obtain explicit authorization for tracking, all-session recovery cleanup,
  necessary deployment, and integration after successful validation.
- [x] Create initiative with the installed dev-session command.
- [x] Commit initial plan/state and register the dedicated workspace worktree.
- [x] Implement the fix; pass focused checks (8 tests / 45 assertions).
- [x] Commit final implementation and tests.
- [x] Complete independent whole-branch review (no findings).
- [x] Complete Nix verification; no package deployment required.
- [x] Compact all archived recovery payloads; verify heads and reclaim 24.600 GiB.
- [x] Fast-forward and SSH-push exact feature head to remote master; release claim.

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
for that session. These were read-only investigation results; the later cleanup is recorded below.

## Repositories and constraints

Workspace feature branch/worktree: 2026-10-30-archived-worktree-cleanup,
worktrees/2026-10-30-archived-worktree-cleanup/workspace (registered and clean).
Shared master has many unrelated modifications/untracked files; preserve all of
them and stage only this initiative's tracking paths. No workspace hook framework
or configured hooksPath was found; repository Git hooks must not be bypassed.

Selected runtime at investigation:
/nix/store/d97nazmvhm2a2m3jn8ichid4ksannliq-dev-workspace-0.2.0,
archiveRecoveryPolicy 3. Recheck selection after taking transition admission.

## Implementation and verification

Initial tracking commit: eb43748ba9ecb180d7246e90fc36542dc5e18d37.
Original feature base: 4beddf77a8f9af1d926c5b48bd6ee4c84f439e85.
Final reviewed base: eb43748ba9ecb180d7246e90fc36542dc5e18d37.
Final feature head: 0548c2fbb6e7fa70bc99f0fb5511dae99f38410b.
The final patch exempts only matching ready creation records; all other journal
and tracking protections stay intact. Regression tests include actual legacy
snapshot capture and policy-3 compaction. Eight tests / 45 assertions pass using
the selected installed runtime's Nix Ruby 3.4.9. `git diff --check` passes.
The previously unexported test suite is now a Nix `storage-retention` check;
evaluation succeeds at dqxzfd9afkqm1krkf262bi5s0wi3c7cp-workspace-storage-retention-tests.drv.

Inventory found 58 sessions with recovery inventories: 57 archived and one
revived/active (`2026-10-18-archive-live-acceptance`), which was subsequently archived under the user's explicit additional approval.
Many completed archives are blocked only by their ready creation records.

No runtime package or configuration change is required: the fixed maintenance
script lives in the workspace repository and runs against the already deployed
policy-3 runtime. It is not part of the system or user-profile package. Run the
reviewed feature script before merge; an aitherdev rebuild would not install it.

## Next action

No remaining task work or blockers. Keep this completed initiative open for
follow-up; the user authorized archival only for the separately named older
session. No additional cleanup, deployment or integration is pending.


## Review and verification milestone

Independent reviewer /root/archive_cleanup_review, gpt-6.1-sol/xhigh, found no
issues across general, architecture, scope and risk lanes. The report concludes
clean whole-branch history, no repeated update streams, and no migrations.
Reviewed base/head 4beddf77..de694fb17 were rebased onto current shared master
eb43748ba as 0548c2fbb6e7fa70bc99f0fb5511dae99f38410b. Range-diff is identical;
all four changed files are byte-identical between reviewed and rebased heads.
Eight tests / 45 assertions pass again. Feature is published over SSH.

Fresh CLI watcher 01a18e9c-8b48-7961-bbcb-a1906fb93f12 used installed catalog
495ef6620926420612ee4988e69d03a4e975e41734a1a5e3208db65fcd731db7 utility
gpt-6-luna/low, explicit danger-full-access and approval never. Actual startup
settings verified. The storage-retention and tracking-source Nix checks passed
in 3.4 seconds at 0548c2fbb; result paths and exact command are in
nix-verification-result.json. No CI workflows exist in the workspace repository.
The worktree is clean; Nix emitted a dirty-tree warning from the shared repository
context, but the changed source files match the committed reviewed content.

## Cleanup authorization update

User answered the active-snapshot question: "you can archive this session and
clean it up", explicitly referring to 2026-10-18-archive-live-acceptance. The
ordinary archive command was invoked for that exact session, with its required
yes/no confirmation supplied under this approval. This does not authorize closing
the current cleanup initiative.

First archive attempt refused because the root workspace .gitignore's negations
overrode private info/exclude rules for the sensitive session. No records were
tracked/staged. Under the shared tracking lock, added exact session exclusions to
the existing ignored local work/.gitignore and archive/.gitignore, preserving
other entries. Verified both directories, records and local ignore files remain
ignored. No sensitive record contents were copied into this initiative. Ordinary
archive retry completed successfully, including checkout removal, tracking
relocation and runtime retirement. The current initiative remains open.

## Live inventory and preview

recovery-before.json records 58 directories / 59 inventories, 24.603 GiB total;
schema counts were 4 schema-1, 21 schema-2, 34 schema-3. One active/revived session
had 8,884,224 bytes and was archived under the new explicit instruction.
Initial preview admitted 266 entries. After the explicit extra archival, the
final preview admitted 267 entries with 24.6026 GiB of recovery data. Nine
nonterminal/unfinished tracking entries were skipped and have no private
recovery inventories. Apply and final verification completed successfully below.

## Links

- [Plan](plan.md)
- [Design and verification brief](design.md)
- [Independent review](review.md)
- [Verification watcher result](watcher-result.md)
- [Storage operation guide](../../docs/operations/workspace-storage-retention.md)
- [Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-30-archived-worktree-cleanup/)

## Final-range review confirmation

The same independent reviewer confirmed eb43748ba..0548c2fbb after rebase: identical
one-commit patch, four identical source files, tracking-only base advancement,
no new findings, obsolete history, repeated update streams or migrations.
See the preserved original report and final-range addendum in review.md.

## Live cleanup verification

Recovery-only apply exited 0 after 522.86 seconds. The complete private root is
now 2,813,952 bytes, down by 26,414,231,552 bytes (24.600 GiB). All 58 session
roots / 60 inventories are schema 3, with 249 committed records in 21 repositories.
All 248 baseline entries and exact heads were preserved; every retention ref and
commit validates. No snapshot payload or unexpected file remains. Final preview
matches all apply remaining-byte totals. Nine historical tracking exclusions
have no recovery directories. Fixture tests prove repeatability; no redundant
live rehash/apply was run. See [cleanup result](cleanup-result.md) and its raw
untracked evidence. No deployment was needed.

## Integration completed

On 2026-10-30, acquired workspace repository claim
b370089d-5f1e-4128-ab00-461b469cf4b6, then acquired the shared tracking lock
without waiting. Fresh target/ref checks matched preparation. The complete final
series and diff still matched the independent review: one coherent commit, no
obsolete history, repeated update streams or migrations. Shared master advanced
fast-forward from eb43748ba9ecb180d7246e90fc36542dc5e18d37 to
0548c2fbb6e7fa70bc99f0fb5511dae99f38410b. SSH push and remote proof confirmed
that exact final feature head on origin/master. The intervening preexisting local
master commits were tracking-only. No staged or unrelated working-tree changes
were included or altered. Feature branch and worktree remain retained.

The repository claim was immediately released and its released state verified.
No CI workflows exist for this repository. All registered exact final heads are
now remotely integrated and no review, checks, deployment or cleanup remains.
See merge-result.json for the compact execution evidence. Final tracking changes
remain local under the ordinary initial-commit/final-archive cadence; the current
initiative has not been archived.
