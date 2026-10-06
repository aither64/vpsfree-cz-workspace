# Node Evidence Compatibility Cleanup

## Goal

Remove the temporary compatibility paths retained for the completed kernel
evidence rollout: the legacy `vpsfree_cz_configuration` component alias and
runtime reconciliation of events written by old supervisors. Keep canonical
`system_configuration`, first-report reconstructed-boot reconciliation, and the
already-deployed corrective migration.

## Affected repositories

- `vpsadmin`: API payload parser, evidence recording operation, WebUI aliases,
  and focused tests.
- `vpsfree-cz-configuration`: all three vpsAdmin channel pins and the deployment
  runbook.
- `vpsadmin-kb-captures`: exact vpsAdmin source/contract pin validation; no
  visible documentation or screenshot change is expected.

All repositories use branch and worktree group
`2026-07-20-node-evidence-compat-cleanup`. Default branches remain unchanged
until explicit user review and approval.

## Implementation

- Remove legacy component normalization from the evidence payload parser.
  Canonical `system_configuration` remains optional and enum value `3` remains
  unchanged, so stored evidence requires no migration.
- Remove the WebUI component-key mapper and use canonical API component names
  directly for version tables, labels, changes and revision links.
- Remove `reconcile_existing_reported_boot!`, its same-boot lookup, and the
  now-unused confidence derivation from stored evidence.
- Preserve `delete_reconstructed_boot_duplicate!` and its boot-time tolerance
  for the supported first exact report. Adapt coverage so deleting at most one
  candidate remains tested on this path.
- Do not modify migration `20260720120000` or its specs. It is deployed,
  historical behavior and must remain reproducible for fresh databases.
- Remove obsolete compatibility tests while retaining canonical payload,
  confidence, reboot, authorization and first-report reconciliation coverage.

## Compatibility and deployment

The production premise is that all supervisors and Node reporters run the
previous compatible release and canonical reporters emit
`system_configuration`. A rolling cleanup deployment is safe because both the
current and cleanup versions accept and render canonical data. Rolling back to
the current release restores the aliases and runtime repair.

After cleanup, a missed legacy reporter is intentionally unsupported. Its
kernel evidence is stored as an invalid evidence gap and derived evidence
events are not created, while ordinary Node status ingestion continues. There
is no schema, API response, stored enum, evidence schema-version, Node reboot,
history reconstruction or migration change.

The runbook will require a pre-deployment gate: current reporters on all active
Nodes, recent successful evidence, no reported boot whose effective time or
confidence differs from immutable evidence, and no unexpected reconstructed
duplicate candidate. Stop rather than deploy if the gate is not clean.

## Verification

- Focused payload parser/supervisor, record-kernel-evidence and WebUI regression
  tests.
- Explicit source search confirming legacy runtime and WebUI identifiers are
  absent while the deployed migration remains unchanged.
- vpsAdmin hooks, relevant GitHub Actions and a fresh bridge development
  cluster.
- Configuration hooks, `nix flake check`, and channel inspection after exact
  generated pin commits.
- KB `bin/check` and `nix flake check`; no PNG or KB page changes.
- Mandatory standalone fresh-context change review before the development
  cluster integration scenario.

## Integration

Push feature branches for review. After explicit approval, fetch defaults,
refresh pins if revisions change, integrate only through fresh fast-forward
worktrees, and retain feature branches.
