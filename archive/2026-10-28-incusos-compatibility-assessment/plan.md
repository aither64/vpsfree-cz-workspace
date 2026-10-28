# 2026-10-28-incusos-compatibility-assessment

## Goal

Evaluate if we could support IncusOS inside vpsAdminOS containers / vpsAdmin VPS. We'd need to build its container image (see build scripts in vpsAdminOS), support distribution configuration (network interfaces, hostname, etc., see dist config in osctld). And finally integration into vpsAdmin, although the primary task would be supporting it in vpsAdminOS. Would it be possible or is it incompatible?

## Affected repositories

- `vpsadminos`: primary read-only assessment of image scripts, osctld distribution configuration and nested-container runtime boundaries.
- `vpsadmin`: secondary read-only assessment of distribution/image registration and node integration.
- Upstream IncusOS official documentation and source: appliance requirements and supported execution model.
- Coordination workspace: findings and session records only; no implementation or deployment requested.

## Approach

Architect0 owns upstream investigation and the compatibility design in `design.md`, with independent local evidence packages delegated to retained implementers where useful. Lead owns scope, acceptance inspection, records and the user-facing conclusion. Identify exact inspected revisions, distinguish hard architectural conflicts from configuration work, and distinguish IncusOS from Incus installed on another distribution.

Acceptance: a sourced verdict on stock IncusOS as an osctld container, concrete image/configuration/runtime implications, secondary vpsAdmin work, viable alternatives, and explicit untested boundaries. Stop after the evidence supports that verdict; no prototype or broad redesign is needed for this request.

## Decisions

- This request authorizes an assessment, not source implementation, deployment or integration.
- User clarified that Incus inside an ordinary distribution already works; focus findings and recommendations on IncusOS specifically. Do not spend further work validating or recommending that known alternative.
- Use canonical bare-repository source reads; no feature branches or worktrees are necessary unless investigation proves otherwise.

## Compatibility and deployment

Assess guest boot, host-kernel sharing, persistent storage, atomic updates and rollback, network/hostname ownership, nested Incus requirements, tenant isolation and mixed versions. No state/schema/API changes or deployments are being made. Any proposed future support must identify whether it preserves upstream IncusOS behavior or creates a maintained derivative.

## Documentation

Audience: the requester and future developers deciding whether to implement support. Keep current findings under this session, linked from state; do not publish unsupported product documentation or change KB material.

## Testing plan

Verify claims against official upstream docs/source and local code at recorded revisions. Source inspection can establish incompatibility but does not prove runtime support. Do not build, start containers, reserve machines or run integration tests for this assessment. List bounded future proof-of-concept checks only if a credible support path remains.
