# Git maintenance memory incident

Investigate the host memory exhaustion reported on 2026-11-10, identify the
originating processes, recover memory safely, and determine prevention and the
relationship to slow portal repository views. Affected components are the shared
Linux partial clone, installed Git, and the installed dev-workspace portal.

Evidence currently identifies 96 concurrent maintenance/repack/pack-objects trees
in the Linux object store, triggered during a Codex-launched blame in the node5
investigation worktree. No other initiative records or branches will be changed.

First preserve process identity, disable automatic maintenance for the shared
Linux repository, and terminate only the identified redundant maintenance trees.
Leave the initiating blame stopped until recurrence protection is established.
Inspect detached-maintenance locking and portal subprocess behavior. Do not run
heavy repacking, full repository validation, or restart shared services during
memory pressure. Preserve refs, existing packs, working trees and user edits.

Compatibility: repository-local maintenance settings affect all Linux worktrees
but do not alter repository formats, objects, branches, APIs or deployed software.
Manual maintenance remains possible and must be serialized and resource-bounded.
Any application implementation or deployment requires its own documented scope,
review and verification; this incident starts as diagnosis and operational repair.

Readers are the workspace operator and future responders. Keep evidence and
recovery decisions here. Verify process counts and memory after recovery, inspect
Git source for the locking mechanism, and inspect installed portal code without
launching expensive live diffs. Initial tracking has no application deliverable.
