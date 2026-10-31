# Archive failure repair

## Goal and authority

Diagnose the failed archive of `2026-10-30-vpsadminos-kernel-cve-check`, fix the owning component, verify it and integrate the fix. User request: “aitherdev can be deployed using vpsfree-cz-configuration. merge when fixed and verified.” This authorizes necessary runtime/configuration deployment and integration into their normal default branches once checks and independent review pass. It does not authorize archiving this repair session or changing the affected session lifecycle.

## Scope and approach

Likely owners are generic `dev-workspace` lifecycle code, this workspace's runtime selection, and `vpsfree-cz-configuration` host runtime selection. Architect must establish actual ownership from the archive failure and identify the smallest implementation package before edits. Preserve existing archive journals and recovery contracts. No unrelated session changes or metadata repair to bypass safeguards.

## Owners and milestones

- architect0: root cause, evidence and design/verification brief in design.md.
- implementer0: complete runtime execution package, regression tests, documentation, quick checks, commits and fixes once design is accepted.
- implementer1: deployment configuration/selection package only if design proves independent boundaries.
- reviewer0: independent committed-deliverable review after quick checks and full history/migration inventory.
- lead: tracking, acceptance, review assignment, deployment/merge coordination and user communication.

## Compatibility and deployment

Assess saved lifecycle journal/state formats, interrupted operation retries, old/new helper compatibility, package-switch checks and rollback. Use disposable fixtures for lifecycle tests. Keep runtime available; use the selected user profile for application deployment and matching configuration channel for aitherdev. Build and review before activation, reserve the machine separately, and retain until verified effects and integrated lineage permit release.

## Documentation

Readers are runtime maintainers and operators recovering failed archival. Lasting invariants/recovery guidance belong in the owning repository; concrete root cause, checks and rollout evidence remain here.

## Verification and completion

Reproduce the actual failure against disposable state, verify the regression and supported recovery paths with quick checks, commit deliverables, independently review full branch history and migration provenance, then run required longer checks/CI under a fresh utility watcher. Verify deployment health and read-only affected-session readiness where supported. Integrate only reviewed/verified branches with short repository claims and SSH remote proof. Leave this session open.
