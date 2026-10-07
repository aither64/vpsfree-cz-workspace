---
lifecycle: active
---

# Archive content integrity and useful failures

Current phase: setup and recovery. The user approved implementation and aitherdev
deployment through vpsfree-cz-configuration. Master integration is not approved.

This independent initiative has no retained Codex team; the lead owns design
and edits. Mandatory review uses the installed default team's standalone
reviewer, and long verification uses the utility watcher policy.

Phase checklist:

- [x] Read-only diagnosis and approved plan.
- [x] Separate initiative created and environment identity verified.
- [ ] Existing completed archive recovered.
- [ ] Implementation, docs and quick checks complete.
- [ ] Whole-branch independent review complete.
- [ ] Package and browser verification complete.
- [ ] Matching aitherdev host and application deployed and verified.
- [ ] Feature branches ready, awaiting merge approval.

Expected branch for all affected repositories:
2026-10-07-archive-content-integrity. Worktrees will be registered beneath
worktrees/2026-10-07-archive-content-integrity/.

Diagnosis: the target archive checksum matches when only state.md is projected
as 0644 instead of its actual 0600. Contents match. The automatic worker
overwrites the actual error with a generic diagnostic. Existing native archive
journal remains at clusters_released after removal and move; it is not edited.

Next: commit initial tracking, recover the old archive, then implement from the
lead-owned design brief. Preserve unrelated shared checkout and index changes.

Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-07-archive-content-integrity/
