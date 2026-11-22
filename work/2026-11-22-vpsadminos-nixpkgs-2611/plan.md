# 2026-11-22-vpsadminos-nixpkgs-2611

## Goal

I'd like you to port vpsadminos to nixpkgs 26.11, which will be released soon. Use whatever branch is available for now, I suppose nixos-26.11? There should be a skill/docs in vpsadminos for this purpose.

## Affected repositories

- `vpsadminos` only; base is the current upstream `staging`. No fleet configuration, kernel source, or service rollout is in scope.

## Approach

1. Find the repository's port workflow and the newest appropriate upstream 26.11 ref. Verify the revision actually reports 26.11 and pin it so the candidate is reproducible.
2. Map the pin consumers and port the supported build, install and test entry points. Make only the compatibility changes required by the new inputs; carry forward supported downstream patches and defaults.
3. Use quick evaluation to isolate porting failures, then independently review the committed branch before integration checks. Publish only the feature branch for CI.

## Decisions

- Prefer `nixos-26.11`, then `release-26.11` if available and appropriate; otherwise select a verified 26.11 development snapshot and record its provenance and refresh conditions. Do not present a pre-release pin as released.
- The architect will record implementation boundaries and exact verification targets in `design.md`.

## Compatibility and deployment

Keep existing module interfaces, state-version defaults, persisted pool/container state, API/CLI contracts, and supported kernel/ZFS choices unless a concrete upstream change requires a documented exception. Check for boot/init, dependency, and toolchain changes. No default-branch integration or activation is approved. Preserve a previous bootable generation for a later operator rollout; do not assume on-disk features are safe to enable across rollback.

## Documentation

Use existing project developer/OS docs for durable port instructions and any operator-facing compatibility notes. Keep exact prerelease provenance, evidence, and any deployment limits in this session; do not duplicate a project workflow.

## Testing plan

Quick checks: identity and consistency of pins, format/hooks, representative Nix evaluation including system and test outputs. After independent review, exercise relevant build and VM/CI targets chosen from the actual breakage and repository guidance; record untested profiles or missing cache outputs. Stop unexpected local kernel builds and distinguish unavailable infrastructure from a port failure.
