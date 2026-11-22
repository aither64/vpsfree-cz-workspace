# Generic source check includes test fixtures

`nix flake check` in generic `dev-workspace` runs the `generic-source` check
over the entire source tree, including Go tests. A new test fixture with a
site-specific workspace path failed that check, but the CI summary showed only
the path to the offending file. Use `nix log <failed-derivation>` or the failed
CI build log to identify it. Keep reusable fixtures site-neutral, such as
`/workspace`, and run `nix build .#checks.x86_64-linux.generic-source --no-link`
after adding source files.

Found and verified during
`work/2026-09-24-session-identity-team-prompts/`; the corrected generic-source
check passed locally and in final-head CI.
