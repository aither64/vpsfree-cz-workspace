# 2026-11-20-nixos-channel-fix-status

## Goal

Please check if channel nixos-26.05 already contains these fixes:

https://github.com/NixOS/nixpkgs/pull/590275
https://github.com/NixOS/nixpkgs/pull/590478

or if we have to use release-26.05

## Affected repositories

- `vpsfree-cz-configuration` only. Leave `vpsadminos-org-configuration` unchanged, as requested.

## Approach and decisions

Make a one-time `nixos-stable` pin update to a freshly resolved exact revision of upstream `release-26.05`, using the existing confctl channel mapping. Preserve the normal channel source for future updates. The purpose is to pick up the PHP fixes from #590478 before they reach the published channel. A Ruby backport is out of scope.

## Compatibility and deployment

Same NixOS release series, but the branch tip can include other backports. No intended application schema, API, or persisted-state changes. Keep the previous pin for rollback; any live rollback would require checking service-specific state compatibility. Prepare the configuration branch only; default-branch integration and deployment are separate approval boundaries.

## Documentation

Record the temporary exception, exact revisions, and check results in this session. No enduring change to the channel policy or project documentation is intended.

## Testing plan

Verify that the PHP fix is contained in the chosen upstream revision, that the generated diff updates only the mapped pin and any required lock metadata, and that normal channel source configuration is unchanged. Use bounded project-specific quick checks; independently review the complete commit and its history before any long checks.
