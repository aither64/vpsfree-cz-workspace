# Network availability and IPv4 counter implementation

## Goal and authorization

Implement the final plan accepted in this conversation. The user requested
implementation on 2026-10-06, selected both configuration channels, and explicitly
confirmed that Network.role is sufficient for public/private classification.
No RFC1918/CIDR classification or filtering is part of this feature.

## Affected repositories

- vpsadmin: enabled state, allocation policy, counter, legacy UI, docs and tests.
- vpsadmin-webui: state/control and address selectors, translations and docs.
- vpsfree-cz-configuration: exact reviewed source pins for vpsadmin and
  vpsadmin-webui channels, deployment/recovery preparation.
- vpsfree-kb-contracts: required external documentation impact verification;
  revise only evidence required by the actual UI impact.

## Design and ownership

Architect0 reconciles [design.md](design.md) before substantive implementation.
Implementer0 owns source/configuration edits; lead owns coordination, review,
verification and final user-facing English/Czech copy. Reviewer0 remains
independent and receives final committed deliverables after quick checks.
Existing default-true inventory remains visible. Disabled pools prohibit new
use, including explicit IDs and owned detached reuse, while preserving existing
service, trusted assigned-address continuity, release and rollback. Counter is
unowned/unassigned/unreserved rows from enabled public_access IPv4 pools only.
Do not infer pool retirement from purpose, location or maintenance flags.

## Compatibility and deployment

Additive NOT NULL/default-true migration; omitted updates preserve state.
Expose admin-only write and readable status, with optional list filtering.
All writers must enforce policy before first disable; already admitted chains
may complete. Preserve existing routes and ownership; no coordinated node
upgrade is needed. Old API rollback ignores disabled state and is unsafe while
retired pools remain disabled. No production activation, database mutation,
network retirement, default-branch integration, or lifecycle action is included.

## Configuration and verification

Use confctl within the configuration dev shell to pin final published feature
SHAs through channels vpsadmin/role vpsadmin and vpsadmin-webui/role
vpsadmin-webui. Preserve generated commits and inspect lock changes.
Run relevant quick checks and hooks, then commit all source/UI/config/docs.
Inventory full branch history, final diffs and migration deployment provenance;
final independent review precedes long integration tests and affected-host builds.
Fresh verification watchers own long/uncertain runs. Correct substantive review
findings and run focused verification under the narrow-fix policy.

## Documentation

Keep lasting enabled/admission/continuity semantics and upgrade guidance with
vpsadmin, UI design/work log with vpsadmin-webui, rollout evidence in session
records, and required KB impact evidence under the external contract workflow.
Production KB writes require approval of exact staged changes. Preserve unrelated
shared workspace work and keep the session open after handoff.
