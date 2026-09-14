# 2026-09-14-node1-stg-livepatch-unload

## Goal
Determine why the kernel livepatch was unloaded on node1.stg, using central
logs and the vpsfree-cz-configuration / vpsAdminOS implementation.

Follow-up: identify why vpsAdmin reports the recent transition as occurring after
2026-08-22 17:33:29, and recommend a concrete fix. This phase diagnoses the API's
observation/event handling and proposes changes; it does not implement or deploy them.

The investigation and planning are complete. The user explicitly requested a new
dev-portal session for implementation. The agreed implementation scope, including
the historical repair tool and vpsadmin channel pin, is preserved in handoff.md.
This initiative is retained as a read-only reference for the new owner.

## Affected repositories
- vpsfree-cz-configuration: read-only configuration and deployment history.
- vpsadminos: read-only livepatch service and activation implementation.
- vpsadmin: read-only kernel evidence recorder, supervisor, node reporter, WebUI,
  history schema, and existing tests; diagnostic reproduction under tracking.
- Workspace: investigation tracking and concise evidence only; no feature branches.

## Approach
Find the unload timestamp, correlate service/activation/authentication events,
and trace the responsible code. Separate observed facts from hypotheses.
Trace `observed_after` from the node's previous report through event creation and
WebUI rendering. Reproduce a long unchanged state followed by removal/transition,
identify missing regression coverage, and describe migration and repair limits.

## Compatibility and deployment
Read-only investigation. No host, persisted-state, schema, API, protocol, Nix
configuration, or deployment changes are planned. No rolling-upgrade or rollback
impact. Any proposed remediation will be described for follow-up.

## Testing plan
Cross-check kernel messages against service logs and exact deployed code when
available. No builds or integration tests are needed for read-only diagnosis.
