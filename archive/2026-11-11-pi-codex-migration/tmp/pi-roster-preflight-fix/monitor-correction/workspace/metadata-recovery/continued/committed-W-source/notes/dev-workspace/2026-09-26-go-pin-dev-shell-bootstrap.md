# Updating codex-web when the generic dev shell builds the package

In `2026-09-26-codex-queue-ledger-capacity`, changing generic
`dev-workspace/flake.nix` to a new `codex-web` revision and then running
`nix develop .. --command go get ...` failed before Go ran. The dev shell
builds the workspace package, whose `postPatch` requires `portal/go.mod` to
pin the same revision as the Nix input. Updating `portal/go.mod` first avoids
that mismatch, but the old vendor hash can still prevent shell startup.

For a new pinned revision, update the Go requirement and Nix input together,
generate `go.sum` using a standalone Go tool from the selected Nixpkgs
(`nix shell nixpkgs#go_1_25 -c go mod download ...` worked here), then refresh
`vendorHash` by the procedure in
`notes/dev-workspace/2026-09-18-vendor-hash-refresh.md`. Nixpkgs in this
environment did not expose `go_1_24`; Go 1.25 accepted the module's `go 1.24`
directive. The later generic flake evaluation passed with the exact pins.
