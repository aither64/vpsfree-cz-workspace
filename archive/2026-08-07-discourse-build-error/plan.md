# 2026-08-07-discourse-build-error

## Goal

Restore evaluation and builds for `cz.vpsfree/containers/discourse` after the
current nixpkgs input update made the local Discourse package override invalid.

## Affected repositories

- `vpsfree-cz-configuration`

## Approach

1. Reproduce the reported evaluation failure at the current `origin/master`.
2. Inspect the locked nixpkgs Discourse expression and the history of the local
   ICU override to identify the precise interface change.
3. Remove or adapt only the obsolete compatibility override, preserving the
   custom Discourse plugin package and service configuration.
4. Run repository hooks and a targeted `confctl` Discourse build, commit the
   fix, and obtain the mandatory standalone change review before any longer
   validation.

## Compatibility and deployment

The intended change is limited to package evaluation/build selection for the
existing Discourse service. It must not change service options, database
schemas, persistent state, network/API contracts, generated configuration, or
deployment ordering.

The fixed configuration should remain safe for a normal single-container
deployment and rollback because both old and new system closures use the same
Discourse state and service configuration. Any package-version or migration
implications discovered while evaluating the new nixpkgs package will be
recorded in `state.md` before deployment is recommended.

## Testing plan

- Reproduce the current failure with
  `nix develop -c confctl build --yes cz.vpsfree/containers/discourse`.
- Evaluate the locked nixpkgs Discourse package inputs and confirm its ICU
  dependency directly from the pinned source.
- Run `nix develop -c overcommit --run`.
- Re-run the targeted `confctl build` after the fix.
- Run the mandatory standalone change review after commit and quick local
  verification.
