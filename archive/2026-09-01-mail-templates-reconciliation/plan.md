# 2026-09-01-mail-templates-reconciliation

## Goal

Restore the production meaning of an omitted notification template: when the
deployment-provided template set does not contain a fallback, vpsAdmin must not
silently install and use the bundled fallback. Remove the six defaults that
were introduced by the first overlay-based reconciliation deployment through a
separate, guarded operator task.

## Affected repositories

- `vpsadmin`: add an explicit authoritative/replace reconciliation mode and
  regression coverage for omitted request templates.
- `vpsfree-cz-configuration`: pin the vpsAdmin feature revision and select
  replace mode on `int.api1`, the sole reconciliation instance.
- `vpsfree-maintenance-tasks`: add a dry-run-by-default cleanup task for the
  six accidentally created database rows.

`vpsfree-mail-templates` is intentionally unchanged. Its current 69-template
set is the desired authoritative production set.

## Approach

1. Add `vpsadmin.api.notificationTemplates.mode`, an enum with compatibility
   default `overlay` and an explicit `replace` value.
2. Preserve the existing core + plugin + configured-source composition in
   overlay mode. In replace mode, reconcile the configured source directly.
3. Prevent database auto-setup from installing bundled defaults when replace
   mode is selected, and reject an explicitly contradictory setting.
4. Document that omissions in a replace source intentionally suppress optional
   notifications.
5. Cover registration correction and approval request chains so absent generic
   fallbacks cannot result in mail, while specific admin and account-creation
   messages remain unaffected.
6. Configure only `int.api1` to use replace mode. Keep `int.api2` without a
   notification-template reconciliation unit.
7. Add a dated maintenance task targeting exactly IDs 71--76 and their known
   names/template identifiers. It will default to dry-run, require `--apply`,
   validate the complete unchanged set and exact creation audit history, reject
   any mail usage, orphan, or unexpected reference, and delete atomically. Apply
   mode additionally requires an explicit confirmation that all vpsAdmin
   database and mail writers are stopped.

## Compatibility and deployment

- `overlay` remains the module default, so existing deployments retain current
  behavior unless they opt into replace mode.
- There are no database schema, API, protocol, template-data, generated-client,
  or persistent-format changes.
- Both API instances can run mixed revisions because they read the same
  existing tables; only API1 owns reconciliation.
- Deploy replace mode before running the cleanup. Reconciliation should then
  expose exactly the configured 69-template source and must not recreate the
  six rows after cleanup.
- Run the cleanup apply phase only in a maintenance window. Stop
  `vpsadmin-api`, `vpsadmin-supervisor`, and every scheduled vpsAdmin rake task
  on all API hosts, keep them stopped while the task validates and commits,
  and pass `--apply --confirm-mail-writers-stopped`. Dry-run remains safe while
  services are running.
- Production cleanup is an explicitly approved later operator action. This
  initiative integrates the reviewed changes into the three default branches,
  but does not deploy them, run the maintenance task, or modify production
  data.
- Rolling back configuration to overlay mode can recreate the six defaults on
  the next reconciliation. Returning to replace mode and rerunning the guarded
  cleanup restores the intended state.
- No coordinated vpsAdminOS or node update is required.

## Testing plan

- Focused Nix package/module evaluation for overlay and replace composition,
  replace-mode database seeding defaults, and rejection of contradictory
  explicit seeding.
- Focused API request-chain specs for missing user-facing fallbacks.
- Maintenance-task syntax/style checks and isolated-database dry-run/apply,
  audit-history, reference, orphan-reference, confirmation, and idempotency
  scenarios.
- Repository hook suites, RuboCop/Nix formatting as declared locally, and
  `git diff --check` before commits.
- Mandatory standalone change review after all intended commits and quick
  checks, before longer configuration builds.
- Build/evaluate both `int.api1` and `int.api2`; inspect the resulting API1
  reconciliation source/unit and confirm API2 has no reconciliation unit.
- Push feature branches, fast-forward the reviewed commits into current default
  branches, and monitor current-head GitHub Actions. Cancel only superseded
  runs after any follow-up push.
