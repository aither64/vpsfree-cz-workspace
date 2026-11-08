# Codex version update

## Goal and scope

Update to the latest stable Codex on aitherdev and in dev-workspace/codex-web,
using vpsfree-cz-configuration for the host. Architect freezes an exact stable
release and llm-agents revision before implementation.

Affected repositories: codex-web, dev-workspace, vpsfree-cz-configuration and
this workspace's runtime composition. Preserve the vpsFree extension pin.

## Approach and decisions

Use the repository-owned update skill chain. Architect owns design.md;
implementers own complete repository packages and follow-up fixes. Update
providers before consumer pins; publish feature branches over SSH. Complete
intended commits and quick checks before independent final review, followed by
required longer native/package checks and exact-output builds.

The user authorized aitherdev deployment. Integration into default branches is
not authorized. Keep feature branches and session active pending that approval.
No session archival, deletion, stopping or background cleanup is authorized.

## Compatibility and deployment

Assess App Server protocol, model catalogs, native invocation, persisted session
state, old/new package contracts and forward recovery. Preserve conversations,
retained roots/generations and operation journals. Build/copy before machine
ownership where supported; activate system before dependent user profile. Never
interrupt other sessions or bypass idle/transition refusal. Verify native/system/
profile versions, service health, naming and saved-thread continuity. Keep the
machine reserved until verified deployment and approved integrated lineage.

## Documentation and checks

Use dev-session-documentation and dev-session-handoff skills. Maintain durable
contracts in owning repos; exact versions, check evidence and individual rollout
results stay here. Architect supplies bounded quick/long checks and recovery
brief. Final reviewer receives complete base/head series, diffs, consolidated
pin streams and explicit migration provenance.
