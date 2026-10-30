# 2026-10-30-archived-worktree-cleanup

## Goal and authorization

Fix legacy archived-worktree compaction, apply it across this workspace's archived
sessions, and reclaim their saved checkout payloads while retaining committed Git
heads, branches, small recovery metadata, and session records.

User direction in this conversation on 2026-10-30: "well I want to handle all
sessions and get rid of the archived worktrees. so you can start tracking this
session. implement the fix, aitherdev can be deployed using
vpsfree-cz-configuration... than you can delete the archived worktrees and if it
works well, merge your work."

This authorizes tracking, implementation, aitherdev deployment if needed,
recovery-only cleanup of all eligible archived sessions, and subsequent
integration of this fix into affected repositories' master branches after
successful validation. It does not authorize archiving/deleting active sessions,
deleting retained Git heads, or cleaning unrelated caches, Nix roots, and live
worktrees. The 64.4 GiB of historical archive-directory copies inside active
workspace worktrees is a separate issue and is outside this cleanup.

## Affected repositories

- Workspace (`git@github.com:aither64/vpsfree-cz-workspace.git`): maintenance
  script, focused regression tests, and storage-retention documentation.
- Inspect selected `dev-workspace` runtime compatibility. Add a runtime change
  only if the existing compaction contract is insufficient.
- `vpsfree-cz-configuration` is authorized for aitherdev deployment if required;
  avoid an unrelated pin update when only the local workspace script changes.

## Approach

1. Preserve the investigation evidence and inventory all private recovery roots.
2. Correct the maintenance script's mistaken classification of completed
   `SLUG.creation.json` records as unfinished lifecycle operations. Keep genuine
   unfinished/unknown operations, active sessions, pending tracking sync,
   session locks, and package-transition exclusion authoritative.
3. Commit the bounded implementation and pass focused checks, then obtain
   independent whole-branch review before longer checks.
4. Deploy only the required component(s), preview recovery-only cleanup, and
   compact eligible archives through the existing runtime implementation.
5. Verify retained heads/metadata, payload removal, idempotence, and actual disk
   savings. Explain every remaining root rather than deleting around a refusal.
6. Integrate the reviewed successful fix under the workspace merge-claim rules.

## Compatibility and recovery

The installed runtime already advertises archiveRecoveryPolicy 3. Its compactor
verifies committed Git objects, publishes schema-3 committed recovery metadata,
then removes legacy files/index payloads. Interruption is resumable. Existing
old archive readers remain available; compacted records require policy 3 and
cannot be restored by older policy-2 executors. Compaction intentionally discards
uncommitted/ignored snapshot contents and is irreversible for those bytes.
Committed code remains recreatable; no database, network protocol, API, or
generated client changes are intended. No fleet-wide update is required.

## Documentation

Update `docs/operations/workspace-storage-retention.md` with the actual eligibility
rule and maintenance behavior. Keep inventory, review, and cleanup results in
this initiative rather than copying operational history into reusable docs.

## Verification

Focused tests cover ready creation records, incomplete/malformed metadata,
genuine lifecycle journals, pending tracking synchronization, lock exclusion,
legacy-to-committed recovery conversion, retained Git objects, payload removal,
and repeatability. Use repository Nix tooling. Run required independent review
after committed changes and quick checks; delegate longer verification using
the installed watcher policy. Live validation uses recovery-only preview and
apply with the selected runtime and workspace authority. Capture before/after
allocated bytes and filesystem availability without treating concurrent disk
activity as task-owned savings.
