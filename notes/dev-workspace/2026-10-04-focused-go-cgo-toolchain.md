# Focused Go checks need the pinned C compiler

`nix shell --inputs-from . nixpkgs#go --command go -C portal test ...`
failed with `cgo: C compiler "gcc" not found` in dev-workspace packages using
SQLite. The packaged Go build supplies the compiler through stdenv; a focused
Go-only shell does not.

Use `nix shell --inputs-from . nixpkgs#go nixpkgs#gcc --command go -C portal test ...`
for those focused checks. Core policy/runtime packages and focused web tests
passed with that environment. Keep cgo enabled to exercise the real SQLite path.

Evidence: `work/2026-10-04-session-modes-review-timing/state.md` and its focused
check artifacts.
