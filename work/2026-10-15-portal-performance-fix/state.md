---
lifecycle: active
---

# Portal performance implementation

## Status

Implementation setup. No retained roster; lead owns design and code.
Created managed session 2026-10-15-portal-performance-fix in
/home/aither/workspace/ai/vpsfree.cz with lead 01a14155-d18d-7512-85a3-c3105dd6fa7d.
Bootstrap conversation explicitly waits while the initiating conversation works.
Explicit literal environment identity matches dev-session current.

- [x] Diagnosis and approved plan.
- [x] Create managed implementation initiative and technical brief.
- [ ] Implement, document and quick-check source changes.
- [ ] Publish and independently review complete committed branches.
- [ ] Longer checks and exact configuration/application builds.
- [ ] Merge all four final heads to remote master.
- [ ] Deploy system then profile and verify acceptance.
- [ ] Prove integration and release aitherdev reservation.

## Repositories and next actions

codex-web, dev-workspace, workspace and vpsfree-cz-configuration.
Feature branches/worktrees use the initiative slug; shared root stays master.
Next: commit initial tracking and create isolated worktrees.

## Authorization and documentation

plan.md records the user's explicit merge, deployment and release direction.
design.md owns implementation/verification details.
Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-15-portal-performance-fix/

## Commands, risks and cleanup

Initial start without --goal-file refused before creating a session. An explicit
waiting bootstrap goal created a valid managed lead. The prior threadless
investigation is not reused. No machine reservation or source edits yet.
Preserve unrelated shared index/files. Ownership caching must fail closed on
identity changes; history backfills must not block watches or fabricate counts.
