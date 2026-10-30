# Exact d67 generated-documentation acceptance preflight

Planning/static identity only, after publication slot release. No gate, tool
--version, compiler, listener, fixture, dependency install or watcher was run.
Source is `d67bebcb37f2d4558a97caa208465147da19dbef` / `cd91bf06fd14d297aaa2470844f679f0998d85f9`, clean. Publication and2148-hash proof are in
publication-m6-console-20261028t192136z. Selected fresh file hashes and owning
contract hashes are in documentation-acceptance-d67-static-inputs.json.

## Proposed bounded batch after separate execution grant

Use one fresh retained Luna/low watcher, pinned3ff7 utility/policy verified
outside Nix, after owner1 installed-dynamic batch and owner3 browser release
capacity. No normal component suites or make test/test-rust broad targets.
The three existing documentation runners already compile and execute actual
rendered fragments for both levels; Rust covers both modes/development/MSRV.
Known successful pure/profile/unit checks are not repeated without new scope.

Run from `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-27-api-documentation-redesign/haveapi`. Clear ambient Ruby/Bundler/loader overrides before Nix, as in
accepted input preparation (RUBYOPT,RUBYLIB,GEM_HOME,GEM_PATH,BUNDLE_GEMFILE,
BUNDLE_BIN_PATH,BUNDLE_PATH,BUNDLE_LOCKFILE,BUNDLE_FROZEN,BUNDLER_SETUP,
BUNDLER_VERSION,RUBYGEMS_GEMDEPS,LD_LIBRARY_PATH,LD_PRELOAD).
Also clear Rust compiler/wrapper/toolchain overrides for the Rust runner.
Use HAVEAPI_RELEASE_TOOLS_ONLY=1, no-write-lock-file and frozen Ruby bundles;
do not call component shell hooks that reinstall dependencies.
Choose a fresh session verification directory when the grant arrives; compact
logs go.log,typescript.log,rust.log plus exit/elapsed/source/input receipts.
No new runner or manifest framework is required.

Go (owning clients/go/docs/documentation.md Verification):

```sh
HAVEAPI_RELEASE_TOOLS_ONLY=1 nix develop --offline --no-write-lock-file --command bash -c '
  set -e
  make doc
  export BUNDLE_GEMFILE="$PWD/clients/go/spec/documentation.Gemfile" BUNDLE_FROZEN=true
  bundle exec ruby clients/go/spec/documentation_acceptance.rb
'
```

This invokes its own environment/profile precheck, saves/generates the matching
fixture, formats/builds and executes32 simple/thorough programs using a disposable
loopback WEBrick server. GOWORK/GOPROXY/GOSUMDB off and GOTOOLCHAIN local are
already enforced by the harness. No separate duplicate build/profile/unit lane.
Go's bundle has local0.31 server/client/generator and its declared JSON3.1.0,
not the root/server JSON graph. Expected1–3min; no earlier timing pass inferred.

TypeScript (clients/typescript/docs/documentation.md Adapter and checks):

```sh
HAVEAPI_TYPESCRIPT_RUNTIME=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-27-api-documentation-redesign/verification/generated-inputs/published-runtime/node_modules/haveapi-client/dist/haveapi-client.js \
HAVEAPI_RELEASE_TOOLS_ONLY=1 nix develop --offline --no-write-lock-file --command bash -c '
  set -e
  export BUNDLE_GEMFILE="$PWD/Gemfile" BUNDLE_FROZEN=true
  bundle exec ruby clients/typescript/spec/documentation/wire.rb
'
```

It compiles28 actual simple/thorough cases at root+/mount against generated
modules, TypeScript6.0.3/NodeNext+strict flags and the separate published runtime.
Node owns the local wire fixture. Runtime0.30.2 SHA256 must remain
96450c40a55ec7b7af4fca903d045bd0fc7ba1216efe12c3fee9b3e6a09e9198.
Local JS0.31 remains a separate input and is never substituted. Expected1–3min;
existing runner has its own60s compiler-ready/10s per-snippet limits.

Rust (clients/rust/docs/documentation.md acceptance command):

```sh
HAVEAPI_RUST_DOCUMENTATION=1 \
HAVEAPI_RUST_MSRV_CARGO=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-27-api-documentation-redesign/verification/generated-inputs/msrv/rustup/toolchains/1.95.0-x86_64-unknown-linux-gnu/bin/cargo \
HAVEAPI_RUST_MSRV_RUSTC=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-27-api-documentation-redesign/verification/generated-inputs/msrv/rustup/toolchains/1.95.0-x86_64-unknown-linux-gnu/bin/rustc \
HAVEAPI_RUST_DOCUMENTATION_EVIDENCE=/absolute/fresh/session/verification/rust \
HAVEAPI_RELEASE_TOOLS_ONLY=1 nix develop --offline --no-write-lock-file --command bash -c '
  set -e
  export GEM_HOME="$PWD/clients/rust/.gems"
  export GEM_PATH="$GEM_HOME:$(ruby -e "puts Gem.default_dir")"
  export PATH="$GEM_HOME/bin:$PATH"
  export BUNDLE_GEMFILE="$PWD/clients/rust/Gemfile" BUNDLE_FROZEN=true
  ruby clients/rust/spec/documentation/run.rb
'
```

This is the exact documentation runner with the repository Makefile RUST_ENV
selection and root declared compiler packages, matching the accepted0.31 input
refresh. The literal .#client-rust shell from the guide always gem-installs/
bundle-installs in flake.nix even with tools-only; root+explicit prepared Rust
environment avoids that mutation while retaining the same pinned tools and
isolated graph. Server child already selects its own prepared root gem home,
server Gemfile/default gems. No benchmark or preview bundle substitution.

MSRV is REQUIRED by this adapter acceptance, not omitted: run.rb asserts rustc
1.95, then checks/runs every emitted async/blocking example under dev1.99 AND
independent1.95 at / and /mounted/api/. Actual rendered imports/requests are
retained; the runner obtains its synthetic existing token through its local API.
It retains per-mount generator config, manifests/lock/generated source/emitted
programs/tools under the supplied fresh evidence directory. No broader runtime,
name-lint, full generator or real-vpsAdmin fixture is needed for this adapter-only
scope. Expected5–20min warm; cold/generated dependency resolution is uncertain.

## Static inputs and stopping boundary

Root/server locks, Go acceptance lock, isolated Rust lock, local npm lock and
local built JS all match the protected inventory. Their prepared0.31 source
selection was checked in the retained input refresh; this preflight does not
claim fresh runtime loading. TypeScript6.0.3 package metadata is present.
MSRV executable hashes and official1.95 manifest match recorded preparation;
published runtime/version/hash/type declarations remain separate and intact.
All158 tracked-runtime crate versions have cached archives or extracted sources
in the selected Cargo home. The Rust runner creates a disposable generated
Cargo.lock; this static observation does not prove a completely offline/fixed
resolution for that generated crate. No dependency fetch/install/resolution was
performed. This is the remaining availability uncertainty, not a gate failure.

Stop on first actual harness assertion/compile/wire failure, source/manifest/
runtime/toolchain/hash drift or unexpected kernel build; preserve log/artifacts,
no retry loop, substitutions, altered assertions/budgets or independent source
repair. No arbitrary new cancellation timeout: use runner's existing limits and
report uncertain prolonged work. Missing generated dependencies need bounded
input diagnosis under lead scope, not release-deps/general refresh. Final source/
input evidence must bind each executed command; no output from these planned
commands is claimed now. No CI, service/bus, preview, provider/TLS/private fixture,
peer, lifecycle or Git mutation occurs in this static package.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-27-api-documentation-redesign/
