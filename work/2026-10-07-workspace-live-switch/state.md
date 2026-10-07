---
lifecycle: active
---

# Live workspace switching

Current phase: implementation setup. Initial investigation and approved design
are recorded in [plan.md](plan.md); detailed brief is [design.md](design.md).

## Phase checklist

- [x] Investigation and scope decisions.
- [x] Dedicated threadless initiative created and ownership recorded.
- [ ] Implementation and documentation.
- [ ] Quick checks, commits, final branch inventory and independent review.
- [ ] Packaged and exact-binary integration checks; CI.
- [ ] Matching aitherdev host/application deployment and live-switch proof.
- [ ] All three approved master targets integrated at exact final heads.

## Authorization and ownership

User approved implementation, one initial idle cutover, aitherdev deployment,
and integration of dev-workspace, workspace and vpsfree-cz-configuration into
master. No archive/delete/branch deletion was requested. This initiative was
created by this conversation with no Codex thread or retained team. Existing
shared changes are unrelated and must be preserved.

## Current evidence and next action

`dev-session current` initially refused because no current session existed;
both DEV_SESSION identity environment variables were absent. Creation returned
slug 2026-10-07-workspace-live-switch and threadId null.

Next: register isolated worktrees, inspect current runtime and test support,
implement the design, and update this phase checklist with verification results.

Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-07-workspace-live-switch/
