# Codex submission-ledger capacity and team-send retention

## Goal and ownership

Restore reliable `dev-session team assign` for long-lived teams without deleting
or truncating the active submission ledger. `codex-web` owns the ledger format and
retry primitives; generic `dev-workspace` owns team assignments and member
lifecycle. The vpsFree extension and this workspace select the exact package
revisions for the aitherdev user-profile portal.

The live ledger was 1,048,127 bytes at investigation time, 449 bytes below its
1 MiB cap. A private aggregate check counted 1,193 accepted team sends, no
pending sends, queue attempts, deletions, or retirement markers. No message
content or identity was printed. Stored turn options account for about 680 KiB.

## Implementation

1. Base new initiative worktrees on `codex-web` master and the deployed,
   unmerged Team-settings heads: generic `9e97536`, extension `1a022c2`, and
   workspace `ff0cc0a`. Preserve those existing branches and worktrees.
2. Raise the schema-3 ledger read and write ceiling to 16 MiB using one shared
   bound. Add an explicit generic compaction operation for accepted sends under
   an application-owned context prefix. It removes only stored original turn
   options, retaining the options digest, message digest, context, accepted
   turn, and steering flag. Prepared/submitting and other-context attempts are
   untouched. Maintain lock, atomic write, fsync, and mode-0600 behavior.
3. Have team assignment compact accepted `team:` sends before reserving its
   next attempt. Team assignments supply their exact options on retries and do
   not use browser original-options recovery. Keep accepted receipt identity
   until retirement; do not acknowledge-and-delete active team sends.
4. Add per-thread cleanup without deleting the root directory retirement
   marker. Call it only after exact member-thread retirement is proved, in
   removal and archival paths; order cleanup before terminal roster state so
   interrupted operations retry. Do not clear active members.
5. Pin the exact new `codex-web` commit in generic Go and Nix inputs, refresh
   the Go vendor hash, then pin generic in the extension and extension in the
   workspace. Update owner documentation and a rollout record.

## Compatibility and deployment

The ledger schema and App Server protocol remain unchanged. Existing clients
can read compacted accepted entries only while the file stays at or below
their 1 MiB limit; they cannot read a larger ledger. Workspace package
switches are forward-only. Quiesce old writers through the normal package
transition; after deploying, use the fixed or a newer package for recovery,
never truncate/delete the active ledger. No database, generated NixOS, API,
Terraform, or daemon protocol transition is involved.

Build and deploy the workspace application from this initiative's user-profile
workspace worktree, not from system configuration pins. Deployment does not
authorize any default-branch integration. Both initiatives remain active until
the user explicitly approves each repository/target merge.

## Verification

- Test read/write above 1 MiB, at and above 16 MiB; unchanged bytes on refusal;
  permissions, atomic replacement, and interprocess retry identity.
- Test selective accepted-team compaction, including same-ID receipt recovery,
  changed-text/options rejection, and preservation of unresolved/browser sends.
- Test removal/archive cleanup, preserved root operation marker, and restart
  after cleanup or roster-update failure.
- Run focused checks, commit all changes, perform the mandatory full-change
  review, then long Nix package checks and exact-head CI. Delegate long
  monitoring to fresh Luna/low utility watchers.
- Deploy the user-profile workspace package and send one benign uniquely
  identified assignment to `2026-09-23-storage-redesign`; verify one receipt
  and delivered conversation entry, checking ledger size but not contents.

The readers are future codex-web maintainers, dev-workspace lifecycle owners,
and aitherdev operators. Lasting retry/compaction semantics belong in
`codex-web` documentation; lifecycle behavior belongs in generic dev-workspace
documentation; this session owns exact rollout revisions and results.
