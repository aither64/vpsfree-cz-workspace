# Workspace deploy/update investigation

## Goal and authorized scope

Suggest solutions for updating dev-workspace without requiring idle Codex threads in the common case, automating pause/switch/continue for active sessions when interruption is unavoidable, and reducing activation latency. Current authorization covers investigation and proposals, not implementation, deployment, integration, or sending live pause messages.

## Affected repositories

- dev-workspace: primary runtime, package transition, activation and conversation ownership.
- codex-web: inspect only if runtime continuity depends on its App Server integration.
- This coordination workspace: session findings and proposals only.
- vpsFree extension/host configuration: inspect contracts only if required; no pin changes.

## Approach and ownership

Architect0 owns substantive source investigation and the proposal in design.md, with bounded read-only diagnosis delegated to available implementers as useful. Lead owns scope, tracking, evidence acceptance and the user-facing recommendation. No project worktrees or branches are required for read-only bare-source inspection.

## Acceptance criteria

Explain current idle gates and actual restart boundaries with source references; identify activation hot paths and distinguish measured delays from hypotheses; recommend an incremental solution covering common noninterrupting updates, automated active-only pause/resume, failure/recovery, and latency verification. Identify concrete implementation boundaries without implementing them.

## Compatibility and recovery

Assess old/new helper and service coexistence, runtime/App Server identity, persistent state/schema and rollback guarantees. Preserve lifecycle exclusion, generation fencing, coordination ownership, and existing recovery contracts. Do not remove safety gates without a compatible replacement. Inactive sessions must not be woken by a future maintenance operation.

## Documentation and checks

Readers: the user choosing an approach and future implementers. Findings/design belong in this session until a solution is selected. Inspect source/docs and any authorized read-only runtime evidence; do not time activation by switching the live package. Record uncertainties and intended future quick/integration checks. No code tests, builds or mandatory final change review are needed for investigation/planning alone.
