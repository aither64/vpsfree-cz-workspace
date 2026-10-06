# 2026-07-04-discourse-update

## Goal

Fix the Discourse container build in `vpsfree-cz-configuration`. Deployment
currently fails while building nixpkgs' `discourse-assets-2026.1.4`
derivation.

## Affected repositories

- `vpsfree-cz-configuration`

## Approach

1. Reproduce the failing build for `cz.vpsfree/containers/discourse`.
2. Inspect the full `discourse-assets` builder log, not only the trimmed Nix
   error.
3. Patch the local package overlay if the failure is in the pinned nixpkgs
   package.
4. Rebuild the Discourse target through `confctl build`.

## Compatibility and deployment

The change is a build-only package override for Discourse. It rebuilds the
Discourse Ruby environment and assets, but does not change Discourse
configuration, database schema options, service units, persistent state layout,
API contracts, host networking, or deployment ordering.

Rolling deployment and rollback implications are the same as the existing
Discourse package update. A rollback can return to the previous system closure;
no new persisted state format is introduced by the overlay itself.

## Testing plan

- `nix develop -c confctl build --yes cz.vpsfree/containers/discourse`
- Run repository hooks before committing.
- Run mandatory change review after committing and quick local verification.
