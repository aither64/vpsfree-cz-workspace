# Implementation and verification brief

Lead-owned design from the accepted plan (no retained implementation roster).

ArchiveRecovery adds compact committed records containing path, repository,
head, branch and retained head ref, but no file/index/permissions snapshots.
Fresh operations use that format; existing inventories/journals preserve their
old restore policy. Capability gates recognize both old formats and require the
new policy for new data. Track summary filtering before sealing fresh archive
tracking; retry never re-filters an already sealed predecessor operation.

A shared small Git helper initializes only workspace-owned additional checkouts
without tracking directories, using per-worktree sparse configuration. Runtime
source and scratch creation use it; other project contents remain complete.
Workspace export-ignore excludes work/archive from package sources.

Collector default TTL is 24h; explicit expire-unused expires only unused leases
and orphan grace, never live dependency roots. Busy integration payloads remain
marked while independent completed integrations are collectible. Keep generation,
preparation, Git and process guards. Optional sizes use allocated blocks.

Maintenance preview/apply uses exact owned roots, skips unfinished lifecycle and
tracking sync, saves compact committed recovery before deleting legacy payloads,
and removes only non-summary historical tracking artifacts. Script reruns must
finish partial payload cleanup without deleting branches or active worktrees.

Acceptance scenarios and rollout gates are in plan.md. Implementation may refine
format mechanics only while preserving these user-visible and recovery contracts;
record consequential deviations here and in state before executing them.
