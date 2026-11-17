---
lifecycle: active
---

# Stable kernel update

## Status

Design phase. Identity verified using dev-session current and both environment
markers: 2026-11-17-stable-kernel-update in /home/aither/workspace/ai/vpsfree.cz.
Existing Full-team roster retained; all assignment settings preserved.

## Phases

- [x] Session identity and required guidance
- [ ] Design and patch inventory
- [ ] Skill/process committed and usable
- [ ] 6.12.118 port, all patches and conflicts accounted for
- [ ] Quick checks and committed delivery
- [ ] Independent final review and history/migration conclusion
- [ ] Longer checks / CI
- [ ] Published branches ready for integration approval
- [ ] Integration (not authorized)
- [ ] Deployment (not requested)

## Packages and transitions

| Package / deliverable | Owner | Dependencies / acceptance | Status | Evidence / next |
| --- | --- | --- | --- | --- |
| D: bounded investigation, design.md, full patch inventory | architect0 | Existing kernel/source/patch policy; sufficient process and port briefs | Executing; assigned 2026-11-17 | Report source inventory and release boundaries |
| P: skill/process in vpsadminos | Unassigned | D; discoverable process, validated skill, checks | Blocked on brief | Must precede port execution |
| K: Linux 6.12.118 port and package registration | Unassigned | D and P; every patch mapped, conflicts resolved, source/package checks | Blocked | No silent patch drops |

## Repositories

Canonical bare repositories exist at repos/vpsadminos.git and repos/linux.git.
Feature worktrees/branches pending sufficient design. No integration or deployment
authorized. Preserve unrelated shared workspace files and index entries.

## Evidence and next action

Read workspace routing procedures, team workflow, documentation and skill-creator
skills. architect0 has a bounded design assignment and workspace-write access.
Next: commit initial tracking, prepare own worktrees, accept design boundaries.

## Risks and recovery

Principal risk is losing behavior during conflict resolution or overlooking a
patch layer. Require full inventory/correspondence and independent review.
No session lifecycle action is requested; leave the session open.
