# Build HaveAPI release artifacts in the top-level Nix shell

## Symptom

`gem build clients/ruby/haveapi-client.gemspec` run with the ambient Ruby
produced a valid gem with the same version and source files as
`nix develop . --command make release`, but the two `.gem` files had different
SHA-256 hashes.

## Cause

The builds used different Ruby/RubyGems toolchains. HaveAPI's release contract
requires the coordinated top-level Nix shell, so source equality is not enough
when another repository pins the exact package hash.

## Workflow

1. Install component dependencies.
2. Run `nix develop . --command make test`.
3. Run `nix develop . --command make release`.
4. Compute downstream Nix hashes only from
   `dist/haveapi-client-<version>.gem`.
5. Publish that exact `dist/` artifact; do not rebuild it outside the release
   shell.

For 0.29.5, the ambient and release-shell artifacts differed even though two
consecutive ambient builds were byte-for-byte stable. Comparing two builds is
therefore insufficient unless they use the official release toolchain.

## Verification

The vpsAdmin packaged-client `gemset.nix` hash was recomputed from the
top-level `make release` artifact and checked with
`nix hash file --type sha256 --base32`.

Related initiative:
`work/2026-07-24-vpsfreectl-snapshot-download-fix/`.
