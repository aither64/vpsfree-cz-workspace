---
lifecycle: active
---

# Limit autostart alerts to node boot

## Current status

Phase: implementation preparation. User explicitly authorized implementation.
No merge or deployment authorized. Session identity and all six retained members
verified; four implementers have ready/workspace_write access. Architect is
reconciling design/contracts before source implementation.

## Phase checklist

- [x] Investigate root cause and agree behavior and component scope.
- [x] User selects persistent genuine failures, osctld history, 5m capture retry.
- [x] Verify expanded roster and define four execution packages.
- [ ] Reconcile design and commit substantive initial tracking.
- [ ] Implement all packages and complete local quick checks.
- [ ] Commit and inventory complete branches; independent final review.
- [ ] Run long integration tests and resolve failures.
- [ ] Publish and verify final feature branches; report readiness.
- [ ] Integrate/deploy only with separate explicit approval.

## Ownership and next actions

See [plan](plan.md) backlog and [design](design.md). Lead creates initial tracking
commit, then implementers set up own same-session worktrees. implementer1 owns
shared vpsAdmin Git setup/operations until handed to implementer2. No simultaneous
index operations. implementer3 owns only integration files in that repository.

## Repositories

Pending registration: vpsadminos, vpsadmin, vpsfree-cz-configuration. Feature
branch/worktree group: 2026-10-22-limit-autostart-alerts-to-boot.

## Evidence

Source inspection confirmed VpsAutostartStatus rebuilds unsatisfied from current
API autostart_enable/current state every poll. Existing Prometheus rule suppresses
first 30m but then evaluates indefinitely. osctld started-cts.txt is pre-start
bookkeeping, not success proof. Exact analyzed hashes and investigation evidence
are in design.md; these do not claim deployed revisions.

No application code committed, tests run, review or deployment performed yet.
Shared workspace has extensive unrelated changes; preserve all and stage only
owned records. Shared master was two commits ahead of freshly fetched origin;
remote had no new commits. No declared root hook framework or hooksPath found.

## Risks / next action

Architect must save final contracts before edits. Validate actual fresh default
bases against analyzed source; report scope/dependency differences. Use repository
Nix environments and mandatory hooks. Long verification must use fresh watcher;
stop unexpected kernel builds. No claims/resources acquired.

## Handoff / lifecycle

Session remains active and open. No archive/delete/stop/release requested.
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-limit-autostart-alerts-to-boot/
