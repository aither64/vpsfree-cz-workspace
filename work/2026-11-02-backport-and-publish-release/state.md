---
lifecycle: active
---

# HaveAPI 0.32.2

## Current status

Phase: investigation/design. Session identity and retained roster verified.
Initial user request explicitly names HaveAPI `master` → `haveapi-0.32` and
publication of 0.32.2. Integration approval is scoped to `haveapi-0.32` only.

## Phase checklist

- [x] Verify session identity and team access.
- [ ] Inventory backports and release contract; architect writes design brief.
- [ ] Implement/commit backports and release metadata; pass quick checks.
- [ ] Independent final history, migration and content review.
- [ ] Required longer checks and CI.
- [ ] Integrate `haveapi-0.32`, publish 0.32.2, verify public artifacts.
- [ ] Reconcile documentation/evidence and hand off; keep session open.

## Ownership and dependencies

- `architect0` (Astra/xhigh, workspace_write): investigation/design; assigned.
- `implementer0` (Sol/xhigh, workspace_write): execution after accepted design.
- `reviewer0` (Sol/xhigh, read_only): independent final review after commits/checks.
- Lead: tracking, acceptance, release/integration coordination and user contact.
One implementer avoids overlapping repository edits/Git operations.

## Repositories and evidence

HaveAPI canonical clone: `repos/haveapi.git`. Feature branch/worktree pending
registration after the release target is confirmed. Plan: [plan.md](plan.md).
No checks, integration or publication performed yet.

## Risks and next action

Pending: exact source commit inventory, compatible patch scope, repository
publication workflow and available authorization/tooling for package registries.
Next: architect reports concrete backport list and release steps.

## Workspace safety

Shared master has extensive unrelated dirty paths; preserve them. Initial
tracking commit stages only this session's plan/state/manifest. No session
lifecycle or cleanup action is authorized.
