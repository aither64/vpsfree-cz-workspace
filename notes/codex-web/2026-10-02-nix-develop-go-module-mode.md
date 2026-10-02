# Focused Go checks in the package-derived Nix environment

codex-web has a default buildGoModule package and no separate dev shell.
`nix develop` derives an environment from that package and sets
`GOFLAGS=-mod=vendor -trimpath`. The source checkout has no vendor directory,
so a plain `go test` stops with an inconsistent-vendoring error before tests.

For focused checks from the source checkout, use
`nix develop -c go test -mod=readonly ./codex <test-options>`.
This uses the pinned toolchain and dependency checksums while avoiding source
dependency changes. Normal packaged checks continue to use the generated
vendor tree. Initial observation: SDK focused verification in
`work/2026-10-02-portal-creation-performance/`; the corrected result is recorded
in that initiative's state.
