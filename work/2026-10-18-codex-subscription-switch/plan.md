# 2026-10-18-codex-subscription-switch

## Goal

Switch the registered vpsfree-cz workspace from codex-lb to the user's retained
Codex subscription promptly, investigating the reported idle-thread wait.

## Affected repositories

Operational use of the installed dev-workspace runtime; no application changes
planned. Coordination records belong to this workspace.

## Approach

Inspect provider state, submit a fresh openai request through workspace-host,
identify exact activity or ownership blockers, and use supported recovery only.
Preserve other sessions, histories, team settings, portal and tmux.

## Decisions

The user explicitly authorized the provider switch. The previous openai request
was canceled. This external conversation has no managed session binding, so a
new threadless initiative owns the operational record.

## Compatibility and deployment

Use the installed provider schema/policy and native cold-resume transition.
Persisted histories and saved model, effort and permission settings must survive.
No package, schema, API or configuration deployment is planned. Returning to the
load balancer uses the same supported provider request; never edit native history
or force a daemon restart around an activity/ownership refusal.

## Documentation

Readers are the operator and future recovery agent. Keep operation evidence in
state.md; the existing runtime docs/codex-providers.md owns the procedure.

## Testing plan

Read-only inventory and provider status; confirm active=openai and phase=applied,
then check native and portal services and effective resume evidence. No build or
integration suite is needed for this operational switch.
