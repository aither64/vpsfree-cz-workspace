# Retained team blocks root retirement during archive

Incident: archive of `2026-10-03-api-specs-optimization` on 2026-10-04,
selected workspace package
`/nix/store/cfrf8mjcww7lks1ylqzgfay5920ab029-dev-workspace-0.2.0`,
Codex 0.160.0. Recovery belongs to
[session-modes-review-timing](../../work/2026-10-04-session-modes-review-timing/state.md).
The user explicitly authorized recovery and asked to preserve the reason for
failure so the archive implementation can be fixed later.

## Original failure and preserved evidence

The portal began the archive at `2026-10-04T16:25:20.244099071Z`, committed the
tracking transition in workspace commit `232471a8`, and failed at
`2026-10-04T16:25:48.708328441Z` during conversation retirement:

> multiple Codex threads use /home/aither/workspace/ai/vpsfree.cz/work/2026-10-03-api-specs-optimization; refusing ambiguous retirement

The schema-2 journal remained at `tracking_committed`, complete mode, operation
`51fdeaeea51ba72c58afe2644cb3b406aa74b89380a493a0ec3567820c149531`.
Its retained root is `01a10359-edb2-7022-bad6-0853ebcb5af5`; all three recorded
specialists still had ready threads in the same session directory. The blocked
journal subsequently prevented an unrelated workspace package deployment.

Before recovery, the exact journal and original failed portal receipt were
preserved in [incident evidence](../../work/2026-10-04-session-modes-review-timing/archive-recovery-evidence.json),
including the original hash and a private byte-for-byte journal backup.
No journal, archived tracking tree or conversation identity was changed by hand.

The executor's archive path calls `retire_portal_thread!` before
`sync_team_lifecycle!(slug, 'archive')`. `RetireThread` performs active directory
discovery even when the exact root ID is supplied, and rejects multiple
candidates. The retained team therefore prevents the lead from reaching the
later team retirement step. This ordering explains the observed failure; the
archive implementation was not changed in this initiative.

## Recovery and additional CLI failure

Under the selected generation's transition lock and normal creation/slug locks,
the selected lifecycle runner verified the committed archive tracking and exact
merged heads. The selected portal helper then ran `team require-idle`,
`team archive --retained-only`, and `team require-archived` for the recorded
root and session. All three recorded members were archived. This path verifies
materialization, project/directory identity, idle status and submission attempts;
it cannot force, replace or recreate members. The normal journal remained intact.

A piped retry of `dev-session archive` refused without an interactive terminal.
The PTY retry then failed with:

> archive proof requires a retained thread, canonical directory and Codex home

The normal host dispatch computes `DEV_WORKSPACE_CODEX_HOME` in
`dev_session_invocation` but discards the returned environment before
`exec_with_workspace`. Explicitly exporting the canonical
`DEV_WORKSPACE_CODEX_HOME=/home/aither/.codex` supplies the missing helper context.
The candidate's `workspace-host recover-archive` entry is limited to selected
Codex 0.155.0 and cannot handle this selected 0.160.0 protocol.

The final matching retry succeeded with exit 0 at `2026-10-04T17:57:42Z`
(121.436 seconds). The journal was completed by the ordinary archive executor;
archived tracking remained and the selected profile was unchanged. See the
[recovery record](../../work/2026-10-04-session-modes-review-timing/archive-recovery.md).
The archive implementation itself remains a later task.

## Follow-up implementation targets

Retire the verified retained team before root discovery, or make root retirement
explicitly roster-aware while preserving refusals for unknown directory-sharing
threads. Preserve journal identities, committed-tree/exact-head checks, idle and
submission checks, retry behavior, and concurrent package-generation guards.

Pass the computed host-selected Codex-home environment through the ordinary CLI
archive dispatch. Reconcile the recovery entry with the actually selected
protocol contract instead of relying on its fixed 0.155.0 gate.

Regression coverage should include direct-team archive from the browser and CLI,
a retry paused at `tracking_committed`, partially archived members, missing helper
context, unknown same-directory threads, and the supported Codex version. These
are follow-up proposals; no archive implementation or new archive test was added
by this session-mode policy change.
