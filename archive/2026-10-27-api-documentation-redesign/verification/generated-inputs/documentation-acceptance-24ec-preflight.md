# Exact M7 generated-documentation acceptance plan

STATIC refresh only for `24ec424c9592951da38584379b43379b0c39f115` / `288376a727deb3905d2c368150543a6d7cfc0971`.
Publication completed/released in publication-m7-20261028t213355z/receipt.md.
All4-lane final review accepted; no compiler, tool-version command, listener,
fixture, build, fetch/install/resolution or utility ran in this preparation.
The old d67 plan/inputs and actual M6 checks remain historical, not M7 passes.

## Commands after a separate execution/input-availability grant

Use the existing three runners only, under one fresh retained Luna/low watcher
per monitor policy after owner3 browser releases capacity and main grants. Verify
watcher native identity/full access outside component Ruby. Do not run duplicate
ordinary CI component/unit/runtime suites or a separate strict-compile repeat.

CWD `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-27-api-documentation-redesign/haveapi`.
Clear inherited Ruby/Bundler/LD overrides exactly as the old plan and successful
publication environment. Ruby must be the existing declared immutable
`/nix/store/jnjll1yxfq02bdcw5pjf9gl86wh8gfhq-ruby-3.4.11/bin/ruby`;
Bash/Git and root frozen bundle identity are in the publication preflight.
Unset GEM_PATH for ordinary root/Go defaults; use the explicit isolated Rust
GEM_PATH below. No broad nix develop/component shell/install hook: the earlier
full shell outputs are unavailable. Required Go/Node/Cargo/rustc/rustfmt PATH
entries must first be bound to retained declared, available inputs; do not select
other same-version outputs merely because their version text matches.

Let `repo` be the absolute CWD, `ruby` the absolute interpreter above. These are
the existing acceptance invocations, not commands run in this static package:

```sh
# Go: exact existing acceptance bundle, root gem home/default gems
GEM_HOME="$repo/.gems" BUNDLE_FROZEN=true \
BUNDLE_GEMFILE="$repo/clients/go/spec/documentation.Gemfile" \
  "$ruby" "$repo/.gems/bin/bundle" exec "$ruby" \
  clients/go/spec/documentation_acceptance.rb

# TypeScript: root frozen bundle, separately pinned published runtime/declarations
GEM_HOME="$repo/.gems" BUNDLE_FROZEN=true \
BUNDLE_GEMFILE="$repo/Gemfile" \
HAVEAPI_TYPESCRIPT_RUNTIME="/home/aither/workspace/ai/vpsfree.cz/work/2026-10-27-api-documentation-redesign/verification/generated-inputs/published-runtime/node_modules/haveapi-client/dist/haveapi-client.js" \
  "$ruby" "$repo/.gems/bin/bundle" exec "$ruby" \
  clients/typescript/spec/documentation/wire.rb

# Rust: isolated existing component bundle + distinct development/MSRV tools
# Clear RUSTC, RUSTC_WRAPPER, RUSTC_WORKSPACE_WRAPPER, RUSTUP_TOOLCHAIN,
# CARGO_TARGET_DIR first; retain the selected cached Cargo home.
GEM_HOME="$repo/clients/rust/.gems" \
GEM_PATH="$repo/clients/rust/.gems:/nix/store/jnjll1yxfq02bdcw5pjf9gl86wh8gfhq-ruby-3.4.11/lib/ruby/gems/3.4.0" \
BUNDLE_GEMFILE="$repo/clients/rust/Gemfile" BUNDLE_FROZEN=true \
CARGO_HOME=/home/aither/.cargo CARGO_NET_OFFLINE=true \
HAVEAPI_RUST_DOCUMENTATION=1 \
HAVEAPI_RUST_MSRV_CARGO="/home/aither/workspace/ai/vpsfree.cz/work/2026-10-27-api-documentation-redesign/verification/generated-inputs/msrv/rustup/toolchains/1.95.0-x86_64-unknown-linux-gnu/bin/cargo" \
HAVEAPI_RUST_MSRV_RUSTC="/home/aither/workspace/ai/vpsfree.cz/work/2026-10-27-api-documentation-redesign/verification/generated-inputs/msrv/rustup/toolchains/1.95.0-x86_64-unknown-linux-gnu/bin/rustc" \
HAVEAPI_RUST_DOCUMENTATION_EVIDENCE=/absolute/fresh/session/verification/rust \
  "$ruby" clients/rust/spec/documentation/run.rb
```

No duplicate make doc: final packaged shared-doc inputs were unchanged through
the two test-only assertions and the current extracted-gem/profile quick passed.
Recheck docs only if relevant source inputs subsequently change. Source/head and
all selected tool/graph/runtime inputs must be proved at actual execution.

Go formats/builds/executes32 actual Simple/Thorough programs using its local
WEBrick fixture; init/auth/mounted/versioned paths, output/list/error/operation
cases remain. Harness enforces GOWORK/GOPROXY/GOSUMDB off and GOTOOLCHAIN local.
Go acceptance JSON3.1.0 graph remains distinct from server/root JSON2.21.2.

TS wire compiles28 actual cases (2mounts x2details x7cases), strict6.0.3/NodeNext/
ES2022/exactOptionalPropertyTypes/noUncheckedIndexedAccess/verbatimModuleSyntax,
then executes its local Node wire fixture. Published runtime0.30.2 JS SHA256
`96450c40a55ec7b7af4fca903d045bd0fc7ba1216efe12c3fee9b3e6a09e9198`
and all adjacent declarations are separately hashed in the JSON receipt; local
JS0.31 never substitutes. Preserve60s readiness/10s per-snippet runner deadlines.

Rust runs actual async/blocking Simple/Thorough programs at / and /mounted/api/
with development1.99 AND independently prepared1.95 Cargo/rustc. It generates
one disposable lock per mount, checks/runs --locked under both toolchains,
retaining emitted source/config/locks/tool paths. The existing actual fixture
provides synthetic token acquisition; no real provider/private fixture.
Keep Cargo offline: historical158 cached packages do not prove fresh generated
lock resolution. An offline missing dependency is a stop, not permission to fetch.
Expected warm duration Go/TS1–3min each, Rust5–20min; uncertain checks require the
fresh watcher. Preserve native runner deadlines, no arbitrary new timeout/retry.

## Static identity and readiness gaps

Current locks/published runtime/MSRV binaries/manifest match old d67 static inputs
and all2148 protected hashes. Current M7 runner/fixture/adapter/contract hashes are
in documentation-acceptance-24ec-static-inputs.json. That binds source bytes; it
does not claim fresh runtime-loaded paths or tool versions. Retained metadata
versions: Ruby3.4.11/Bundler4.0.23/Go1.26.10/Node24.21.0/TS6.0.3, devRust1.99
(rustfmt1.10.0), independentMSRV1.95. No version command was run now.

Actual execution is NOT ready: recorded Go output
`/nix/store/fkz7zn1a0yiryf9kri2yh1s12k1sv557-go-1.26.10` is absent; no exact
go-1.26.10 output directory was available at the static observation. Recorded
Cargo `/nix/store/l3jrya2cdjmzxgdpnxzwvx3h416lcbr6-cargo-1.99.0` and rustfmt
`/nix/store/vwgbz9vm1gyxqn6z4fg1jd6va2nzfa3m-rustfmt-1.99.0` are absent too.
Other1.99/Node outputs exist but were not selected or treated as equivalent;
exact declared availability/input proof remains needed. The old haveapi-env
derivation itself is now absent. No restoration/realization/setup was attempted.
Lead was notified; later bounded input availability grant is required before the
generator execution batch. Frozen component/MSRV/runtime identity is preserved.

Stop on first real harness/compile/wire failure, source/runtime/input/toolchain
drift, missing declared tool or unexpected kernel build. Preserve evidence, no
automatic retry/substitution/assertion or budget/reference changes. Missing
inputs go to bounded diagnosis under lead scope, never release-deps/general
refresh. Main alone grants later execution; no CI wait/dispatch, service/preview,
provider/TLS/peer/lifecycle or source/Git work is part of this plan.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-27-api-documentation-redesign/
