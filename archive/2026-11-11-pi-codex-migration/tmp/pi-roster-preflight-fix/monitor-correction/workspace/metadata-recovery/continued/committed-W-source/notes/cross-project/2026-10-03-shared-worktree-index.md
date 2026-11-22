# Shared worktree index access during delegated conflict resolution

A member with source-write access can still see the shared repository's `.git`
administration directory as read-only. In this session, `git restore --source`
with `--worktree` failed before writing because Git tried to create the linked
worktree's `index.lock`. Do not chmod the administration directory, bypass the
sandbox or replace the index.

For a lead-authorized conflict resolution, the member can read the exact
upstream Git blobs, write only the assigned worktree paths, make the bounded
source edit, and compare complete bytes against the upstream baseline. Leave
unmerged entries untouched and report file hashes plus the stopped rebase's
base, replayed commit and path inventory. These files are not committable yet.

The lead owns the short Git step: verify the reported bytes and rebase identity,
stage only those assigned paths, generate any owning lock with Nix, verify its
exact leaf delta, and continue the normal rebase. This preserves application
ownership without asking the member to mutate inaccessible shared Git state.
A generated lock baseline must stay exact; never hand-splice old lock metadata.

Observed here: consumer rebase on `93389c33`, member's exact upstream lock and
one provider URL edit, parent stage/Nix generation/expected eight leaves, then
normal rebase to `6d1b9c4d`. No permission or hook bypass occurred.

[Session](../../work/2026-09-23-storage-redesign/state.md).
