---
lifecycle: active
---

# mx2 NixOS migration preparation

## Current phase

Investigation and design. Identity verified with `dev-session current`, matching
both environment markers and thread binding. Saved team uses Full team with four
implementers; settings retained. Architect owns branch/dependency investigation.

## Phase checklist

- [x] Verify session identity and inspect same-session roster/access.
- [x] Scope request and assign architect investigation/design.
- [ ] Locate exact source branch/range and dependency graph.
- [ ] Import/register isolated worktree and rebase on fetched defaults.
- [ ] Complete quick checks and inventory final history.
- [ ] Independent final review of substantive configuration.
- [ ] Publish branch and deliver verification recommendation.
- [ ] Runtime verification, production deployment and integration: future work.

## Backlog

| Owner | Deliverable | Dependency | Acceptance/check |
| --- | --- | --- | --- |
| architect0 | Branch provenance and design/verification brief | Read-only source investigation | Exact refs/ranges, bounded execution package, realistic mail acceptance criteria |
| implementer0 (planned) | Imported, rebased configuration branch | Architect brief and initial tracking commit | Source untouched; current default ancestry; quick checks; clean published head |
| reviewer0 (planned) | Independent final branch review | Committed deliverable and quick checks | Full history/diff and migration conclusion |
| lead | Scope, records and recommendation | Member evidence | Distinguish checks performed from proposed tests |

## Repositories and evidence

Expected project: `vpsfree-cz-configuration`; source checkout above in plan.
No worktree registered yet. Architect assignment queued successfully.
Shared workspace has unrelated dirty files: preserve them and stage owned paths
only. No merge, machine reservation or deployment has been requested.

## Next action

Commit initial plan/state; receive architect brief and delegate import/rebase.
