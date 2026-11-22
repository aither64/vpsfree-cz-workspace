# Focused Go and browser contract checks

For checks outside the derivation shell, include GCC alongside Go in the Nix
toolchain: `nix shell --inputs-from . nixpkgs#go nixpkgs#gcc nixpkgs#nodejs`.
Go alone failed because cgo could not find `gcc`; the same package tests passed
with the complete toolchain.

Do not invoke `portal/internal/web/browser_contract_test.cjs` without a fixture
server URL. Its Go test driver owns the fixture and supplies that argument.
Run the owning Go package/test instead. The standalone invocation failed with
"browser contract test requires the server URL"; `go test ./internal/web`
passed with Node present.

Related initiative: `work/2026-09-14-auto-archive/`.
