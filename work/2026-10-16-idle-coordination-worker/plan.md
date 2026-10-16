# Idle coordination workers

Implement durable background continuation for approved coordinated merges and deployments so waiting sessions can end their turns. Background runs wake the retained lead only when action or review is needed. Reservation grants and intermediate progress stay visible in Operations.

## Projects and design

- dev-workspace: background CLI, journal/schema capability, systemd dispatch, restart and generation handover, pause/intervention semantics, native notifications, status and operations documentation.
- workspace: waiting policy, matching nested runtime input, deployment verification.
- vpsfree-cz-configuration: matching dev-workspace/devWorkspace channel pin, aitherdev system build and deployment preparation.
- codex-web: reuse existing native notification transport; no planned changes.

Preserve existing synchronous and --no-wait behavior, approval scope, FIFO scheduling, machine ownership through review, exact integration proofs, and existing uncertain-effect recovery. Background preparation runs outside claims. Continue only existing certified mechanical refreshes; conflicts, stale machine artifacts, changed scope and uncertain effects require intervention.

## Compatibility and rollout

Use versioned background journals while supporting schema-1 manual journals. Unsupported package generations must refuse retained background state. Preserve schema-1 operation ledger, snapshots and worker protocols where possible. The selected compatible generation resumes the exact run; predecessor workers must stop admitting steps after a profile switch. No database migration is planned.

Build aitherdev from cz.vpsfree/machines/aitherdev in the configuration feature branch, through its existing dev-workspace channel and devWorkspace role. Match the workspace nested runtime input, check composed locks, prepare the exact final configuration commit, activate system before workspace user profile under one vpsfree:aitherdev reservation. Never infer default-branch integration approval.

## Verification

Quick Ruby, Go, Nix and JavaScript checks as applicable, then committed whole-branch independent review, then long packaged and native acceptance tests. Cover idle sessions, FIFO contention, per-run notification suppression, pause/resume, retry identity, crashes around submission/delivery/finalization, lifecycle fencing, generation changes and unsupported downgrade.

## Session setup limitation

The initial managed conversation 2026-10-16-idle-coordination was created but its initial request was refused twice with materialized Codex thread has no initial user request. Its creation journal and retained thread remain untouched. This separate tracking-only initiative enables implementation. A valid managed owner is required before live coordination/deployment; do not bypass the startup refusal.
