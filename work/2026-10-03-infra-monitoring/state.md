---
lifecycle: active
---

# 2026-10-03-infra-monitoring

## Status

- Phase: investigation finished; policy proposal prepared for operator review.
- Configuration is unchanged. No feature branch/worktree, application edit,
  rule test, independent review, build, deployment, or merge was performed.
- Findings and proposed values are in [plan.md](plan.md).

## Phase checklist

- [x] Verify the bound session and read applicable workspace/project guidance.
- [x] Inspect current remote cluster inventory, Prometheus rules, and routing.
- [x] Propose VPS SMS suppression and later infra disk critical thresholds.
- [x] Propose a shared relaxed stg/pgnd CPU and load policy.
- [ ] Settle the proposed values and scope with the operator.
- [ ] If implementation is requested: establish an appropriate team, implement,
  run quick checks and independent review, then verify and deploy as authorized.

## Next actions

Discuss the recommended values. A future implementation must use this same
initiative and delegate application edits to an appropriate implementation
member after team setup. No lifecycle action is requested; leave the session open.

## Documentation

- [Evidence, policy proposal, compatibility, and verification plan](plan.md).
- No project documentation change: this is an unaccepted configuration proposal.
- Stable portal:
  https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-03-infra-monitoring/

## Repositories

- `vpsfree-cz-configuration`, inspected read-only through
  `repos/vpsfree-cz-configuration.git`, fetched origin/master at
  `2a3e6a977db4464b585e413839953f08f57521f7`.
- No feature repositories are registered in the portal and no worktrees created.

## Commands run

- `dev-session current`: matched 2026-10-03-infra-monitoring; both environment
  identity markers also matched the trusted workspace/session binding.
- Read project map, session, Git, lifecycle, documentation, verification,
  deployment, and commit procedures, the documentation/handoff skills, and
  repository AGENTS.md/README.
- `git --git-dir=repos/vpsfree-cz-configuration.git fetch origin`, followed by
  focused `git show`, `git grep`, and inventory reads against origin/master.
- Checked official Prometheus routing, alert hold-time, and rate/irate guidance.
- `dev-session url 2026-10-03-infra-monitoring --as-is` obtained the stable URL.
- Fetched coordination origin; shared master was ahead by one and not behind.
  Existing unrelated working-tree changes were preserved. No declared hook
  framework or active pre-commit hook is present in the coordination repository.

## Results

- Infra has no generated container discriminator, but container metadata is
  available to derive one without exporter or host changes.
- Filesystem critical is <= 10% free for 5m; filesystem fatal at <= 5% applies
  only to node root filesystems. Common pool critical/fatal values are 90%/95%
  used for 120m/30m. Several pool descriptions have stale percentages.
- Email precedes Telegram and SMS routes, permitting a narrow terminal route
  before SMS without losing email delivery or downgrading severity.
- Staging has longer CPU/load holds already; playground is selected by the
  strict rules. Both locations can share a relaxed policy.

## Open questions

- Suggested values are not measured workload tuning; recent live time series
  and actual deployed revisions have not been inspected.
- `/run` capacity is not covered by VPS dataset expansion. Any separate tmpfs
  escalation policy remains to be decided.
- The optional infra pool critical adjustment matters only where the pool
  capacity metrics are actually exported. No new infra filesystem fatal alert
  is proposed.

## Cleanup

- Only session-owned coordination records changed. No application worktree,
  test/build process, development cluster, or staging allocation was created.
- Session remains active and open for discussion; no cleanup or closure scheduled.
