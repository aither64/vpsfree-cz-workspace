---
lifecycle: active
---

# 2026-10-29-workspace-resource-monitoring

## Status

- Phase: demonstration preparation and design update, authorized by user.
- Verified current identity and both environment markers match this exact slug
  and `/home/aither/workspace/ai/vpsfree.cz`.
- Inspected retained same-session roster: architect0 (Astra/xhigh) owns design;
  implementers retain Sol/xhigh workspace-write; reviewer0 retains Sol/xhigh
  read-only independent review. Assignments are recorded below.

## Phase checklist

- [x] Establish request scope, identity and design ownership.
- [x] Inspect current runtime and complete proposed design.
- [x] Identify stock exec-server route avoiding native rebuild/auth sharing.
- [ ] Update design and assign bounded demonstration packages.
- [ ] Commit demonstration and pass quick checks.
- [ ] Independent final review.
- [ ] Disposable integration demonstration and evidence reconciliation.
- [ ] Complete design and user handoff. Production deployment is not in scope.

## Next actions

- Commit initial tracking, update architect-owned brief, prepare own feature
  worktree, then assign full demo package(s). Verify container prerequisites
  without altering live services. No real credentials are needed for fixtures.

## Documentation

- [Plan](plan.md); architect-owned [proposed design](design.md).
- Stable portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-29-workspace-resource-monitoring/
- No product documentation changed: this turn produced planning/investigation
  evidence only, with behavior and operational documentation deferred to any
  requested implementation.

## Repositories

- Feature worktree and demo base/head will be recorded when created.

## Commands run

- `dev-session current`; environment identity check; same-session team list.
- Assigned `architect0` with stable message ID
  `5035b315-3a6c-464f-a9de-f85ac9600b5a`.

## Results

- Proposal only: no application tests, independent review, CI or deployment run.
- Architect's initial finding: shared workspace App Server and tmux services
  mean terminal-only cgroups cannot account for all agent commands. Exact
  session process accounting needs execution routing support; design pending.
- Disk accounting and pressure cleanup can be independent of cgroup rollout.
- Existing restart/recovery holds must remain intact; cleanup must not revive
  held/stopped sessions or implicitly resume pending work in idle sessions.
- Architect completed source-grounded proposal, accepted by lead for presentation.
  Baseline dev-workspace `52dcd471186ef874c5c93f4133744195d4815454`, pinned
  codex-web `57972192e30f`; installed-package equivalence was not established.
- Ordinary send resumes before steering/starting, so idle cleanup requires a
  verified maintenance-only admission guard; deferred if that is unavailable.
- Existing coordination outbox tolerates duplicate status sends using fresh IDs;
  cleanup must instead reconcile immutable event IDs and uncertain submissions.
- Suggested defaults: host samples 5 s, filesystem 30 s, session disk target
  30 min; pressure >90% twice, clear <85% for 5 min, eligibility >=5 GiB;
  persistent cooldown 1 h, with 6 h/24 h no-reclaim backoff.
- Proposal remains active for follow-up. No feature branch is declared ready;
  no independent final review is triggered by these planning artifacts.

## Open questions

- Stock runtime validation remains: per-thread executor selection, all managed
  execution/file paths, fork/resume/child behavior and fail-closed recovery.
- Host prerequisite: noninteractive privilege/container capability and storage
  reclaim support are not yet proven. Do not bypass host permission failures.

## Cleanup

- No cleanup, lifecycle action or cross-session messaging performed.
