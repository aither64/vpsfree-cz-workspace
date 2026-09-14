# 2026-09-14-node1-stg-livepatch-unload

## Goal
Determine why the kernel livepatch was unloaded on node1.stg, using central
logs and the vpsfree-cz-configuration / vpsAdminOS implementation.

## Affected repositories
- vpsfree-cz-configuration: read-only configuration and deployment history.
- vpsadminos: read-only livepatch service and activation implementation.
- Workspace: investigation tracking and concise evidence only; no feature branches.

## Approach
Find the unload timestamp, correlate service/activation/authentication events,
and trace the responsible code. Separate observed facts from hypotheses.

## Compatibility and deployment
Read-only investigation. No host, persisted-state, schema, API, protocol, Nix
configuration, or deployment changes are planned. No rolling-upgrade or rollback
impact. Any proposed remediation will be described for follow-up.

## Testing plan
Cross-check kernel messages against service logs and exact deployed code when
available. No builds or integration tests are needed for read-only diagnosis.
