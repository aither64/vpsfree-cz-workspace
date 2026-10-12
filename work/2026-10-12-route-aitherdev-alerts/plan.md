# 2026-10-12-route-aitherdev-alerts

## Goal

I'd like to change monitoring in vpsfree-cz-configuration so that alerts about the aitherdev machine would go only to me (aither), and not others. Look it over and suggest a solution.

## Affected repositories

- `vpsfree-cz-configuration`: monitoring labels, Prometheus rules and Alertmanager
  routes. Investigation uses the canonical bare repository; no feature worktree
  or configuration changes are requested at this stage.

## Approach

- Trace alerts for aitherdev through exporter identity labels and alert rules.
- Inventory mail, Telegram and SMS routes, including severity, repeat frequency
  and daytime behavior.
- Suggest an exclusive route with minimal deployment scope and an offline
  receiver-selection verification plan.

## Decisions

- Current request is investigation and a proposal, without implementation,
  deployment or integration.
- Lead owns investigation and proposed design. Retained `reviewer0` is ready,
  read-only, Astra/xhigh; final review is reserved for a completed substantive
  deliverable, not routine findings.

## Compatibility and deployment

- Preserve existing alert rules, label identities, inhibition and notification
  timing unless the investigation establishes a reason to change them.
- Prefer Alertmanager-only deployment to both replicas. Check whether aitherdev
  already carries an adequate identity label before proposing new labels.
- No database, API, daemon protocol, client or persisted-state migration is
  expected. Record mixed-version delivery and rollback consequences in findings.

## Documentation

- Readers: aither and monitoring maintainers. Findings and proposal belong in
  session records. Inspect `docs/services/monitoring.md`; update project docs
  only if implementation later changes the supported monitoring behavior.

## Testing plan

- Investigation: inspect source and upstream routing semantics, without sending
  notifications.
- Implementation candidate: check exact receiver sets for aitherdev and an
  ordinary host, all severities, frequency overrides and daytime behavior;
  evaluate/build both Alertmanager machines after final independent review.
