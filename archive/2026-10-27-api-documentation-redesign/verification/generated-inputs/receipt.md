# Generated-client verification inputs

Input preparation passed with exit 0 in about two minutes through the fresh
retained verification utility (`gpt-6-luna`, low, `dw_261a10738ad06c003118fa86a9c9a7ce71a28ba2529d3b2b`,
catalog `3ff7a2129ed39b4d6774466e53060bbff33d2cd2d893aa168c87cb3d64bd6b41`).
Actual execution used full access, danger-full-access and no approvals.
No utility or preparation process remains running.

This prepared dependencies, not application verification. `82a7f2ab` is an
assignment reference only; authorized unrelated UI edits may exist. Dependency
Gemfiles/gemspecs, Nix pins and package declarations were unchanged. Adapter and
local JavaScript reference hashes are retained separately; they also matched
before/after. No tests, generated SDK compilation, wire harness, API fixture,
benchmark, real documentation OAuth/TLS, Git action or hook ran.

## Prepared inputs

- Root/server and exact Go acceptance bundles are available using repository
  Nix Ruby 3.4.11 and Bundler 4.0.23. Go is 1.26.10. The Go acceptance Gemfile is
  `clients/go/spec/documentation.Gemfile`; retain its local lock without staging.
- Isolated Rust Ruby bundle is in `clients/rust/.gems`, with its local
  `clients/rust/Gemfile.lock`. Development cargo/rustc are 1.99.0; rustfmt is 1.10.0.
- Independent MSRV Cargo: `/home/aither/workspace/ai/vpsfree.cz/work/2026-10-27-api-documentation-redesign/verification/generated-inputs/msrv/rustup/toolchains/1.95.0-x86_64-unknown-linux-gnu/bin/cargo`.
- Independent MSRV compiler: `/home/aither/workspace/ai/vpsfree.cz/work/2026-10-27-api-documentation-redesign/verification/generated-inputs/msrv/rustup/toolchains/1.95.0-x86_64-unknown-linux-gnu/bin/rustc`.
  Both report 1.95.0. Repository-pinned Nixpkgs Rustup 1.29.2 installed official
  minimal binary components in this session's own Rustup/Cargo homes. The official
  channel manifest/SHA and selected artifact URLs/hashes are retained under `msrv/`.
- Separate published `haveapi-client@0.30.2` runtime: `/home/aither/workspace/ai/vpsfree.cz/work/2026-10-27-api-documentation-redesign/verification/generated-inputs/published-runtime/node_modules/haveapi-client/dist/haveapi-client.js`.
  SHA-256: `96450c40a55ec7b7af4fca903d045bd0fc7ba1216efe12c3fee9b3e6a09e9198`. Public type declarations are beside
  it. The existing local 0.30.0 JavaScript bundle was not overwritten.
- Node is 24.21.0 and npm 11.19.0. Earlier prepared TypeScript is 6.0.3 and Node
  type declarations are 24.19.2.

Keep the Ruby graphs distinct: server and Rust component locks select JSON
2.21.2; the declared Go acceptance bundle resolved JSON 3.1.0. Use its actual
Gemfile/lock. Frozen performance inputs remain in their separate benchmark gem
store and were not modified. The live preview bundle was not used or changed.

## Corrected loader boundary

The first operation stopped before any preparation phase. It called
`dev-session current` inside the repository gem environment: workspace Ruby
3.4.9 loaded the repository JSON extension built for Ruby 3.4.11 and produced a
GLIBC_2.44 mismatch. This is not evidence of a broken prepared repository bundle.
Owner1's successful packaging command uses root Nix Ruby 3.4.11/root gems and
checks session binding outside that shell.

The corrected operation checked binding before entering Nix, cleared inherited
Ruby/Bundler/loader variables and ran the same prescribed preparation phases.
No package rebuild, source/pin change, toolchain substitution or blind retry was
used. The component and Go Ruby dependencies installed their normal missing gems;
no generated client was compiled. Keep future workspace CLI orchestration outside
component gem environments.

Original failure evidence is `preparation.log`, `preparation.exit` and
`prepare-inputs.failed-runtime-context.sh`. Corrected evidence is
`preparation.corrected.log`, `preparation.corrected.exit`, `prepare-inputs.sh`,
`prepared-inputs.json`, `preparation-evidence.json` and the four phase logs.
Input identities include full lock hashes, dependency declarations, official
MSRV manifest/artifact hashes and installed MSRV binary hashes.

Acceptance remains pending the completed/reviewed milestone 4 and an explicit
run grant. No pass for application code or compiler/wire behavior is claimed.
