# Archive failure investigation

## Goal and scope

Find the root cause of the failed workspace archive and deliver the smallest
correct fix, with regression coverage and independent review. The user permits
aitherdev deployment through vpsfree-cz-configuration when needed. Integration
into default branches and any exact session lifecycle action need separate
explicit direction; preserve the failed operation and its recovery contract.

## Affected repositories

Diagnosis will identify the owning component. Likely boundaries are the generic
dev-workspace runtime, workspace package composition, and host configuration.
Do not expand scope beyond evidence from the failed operation.

## Approach and ownership

Architect0 owns bounded diagnosis and design.md. Implementer0 will own the core
fix, regression checks, documentation and commits after brief release.
Implementer1 is available for independent host/configuration preparation if needed.
Reviewer0 independently reviews completed committed deliverables after quick
checks, before longer integration verification. Lead owns acceptance, tracking,
authority and deployment/integration drivers.

## Compatibility and deployment

Preserve persisted lifecycle journals, recovery policy, ownership fences and
conversation continuity. Reproduce against disposable state only. If deployment
is required, prepare artifacts before acquiring a machine claim, use the selected
package guides, and keep the user-profile application separate from host pins.

## Documentation and checks

Record first-failure evidence, causal source and the smallest supported recovery
path. Keep lasting behavior/recovery guidance in the owning repository. Use
focused regression/quick checks, mandatory final review, and warranted integration
checks. Never retry a real archive without explicit direction for that session.
