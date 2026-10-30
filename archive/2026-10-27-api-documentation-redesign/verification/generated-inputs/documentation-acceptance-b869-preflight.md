# M8 generated-documentation acceptance preflight

STATIC ONLY: `b8697c428e759f05d1d9a12f3d83692d02b330de`, tree
`5207e34f5f998fb43fd40f6cfe371d47aac7838d`. Final review is in progress;
execution requires its reconciliation, a main relay and sole utility capacity.
No compiler, version/resolution probe, test, listener, fixture, Nix, network,
Git/index/ref/hook mutation or utility ran. Source slot remains free/quiet.

documentation-acceptance-b869-static-inputs.json refreshes the existing format:
44 source contracts are bound to current SHA256/native blobs, including all17
modern-package paths, three adapters/runners, Go/TS fixtures and exact M8 Rust
run.rb→haveapi_server.rb→haveapi_fixture.rb/serve.rb chain and composition cases.
Nine previously bound contracts changed from24ec; fourteen additional owning
spec/fixture paths are bound. Old24ec/d67 plans and all results stay historical.
No new runner, projection or acceptance framework was introduced.

All12 selected lock/runtime/MSRV/manifest inputs equal the existing24ec record;
all46 published declarations and strict compiler files match. Published runtime
is0.30.2, SHA256 `96450c40a55ec7b7af4fca903d045bd0fc7ba1216efe12c3fee9b3e6a09e9198`;
TypeScript metadata is6.0.3. Local JS0.31 is a separate input, never a substitute.
Root lock isd877e062…, server6f1d83b7…, Goacceptanceb5fc2727…, Rust412c5357…;
full hashes remain in the JSON/retained input receipts. Root/server JSON2.21.2
and Goacceptance JSON3.1.0 graphs stay distinct. MSRV1.95 Cargo/rustc hashes and
official manifest still match. The final-history2148 preservation proof is reused,
not rerun: ../../history-m8-final-20261028t225625z/final-preservation.json.

Exact restored Go/Cargo/rustfmt/uv are present, as are all22 retained session
tool roots. Current static path/executable-mode reads confirm the selected
Ruby/Git/Bash/Node, Rust6l9 wrapper→1qg compiler, gcc/ld and calibratedRuby7b77.
Wrapper/stdenv/cc bytes still match runtime-and-linker-support.json. Native
integrity/trust/closure proofs and root ownership are reused from
tool-restoration-20261028t220111z/receipt.md and
php-restoration-20261028t223438z/receipt.md; no new native verification is claimed.
Support remains declared stdenvan9g93/gccwrapperr5ri78/ldfi98/pkg-configs70gz6/
OpenSSLwps4g7/libffiy8ynp6. CalibratedRuby7b77 and its separate frozen benchmark
graph/budgets/reference remain intact; these three runners do not use that graph.

## Exact later commands and environment

CWD `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-27-api-documentation-redesign/haveapi`.
Use the existing24ec command forms below, with the current M8 sources bound above.
The following is a plan, not a launched script. Clear inherited Ruby/Bundler/
loader overrides listed in documentation-acceptance-d67-preflight.md. Unset
GEM_PATH for root/Go defaults. Before Rust also clear RUSTC, RUSTC_WRAPPER,
RUSTC_WORKSPACE_WRAPPER, RUSTUP_TOOLCHAIN and CARGO_TARGET_DIR. Keep normal OS
utilities in PATH. Do not enter a broad Nix/component shell or run shell hooks.

Let `repo` be the CWD, `inputs` this generated-inputs directory, `ruby` the exact
`/nix/store/jnjll1yxfq02bdcw5pjf9gl86wh8gfhq-ruby-3.4.11/bin/ruby`.
Prepend these exact immutable bin directories, plus `$repo/.gems/bin`, to the
normal OS PATH (not alternative same-version tools):

```text
/nix/store/jnjll1yxfq02bdcw5pjf9gl86wh8gfhq-ruby-3.4.11/bin
/nix/store/xgw813vgzl2q0696sq45adpj0xd690jq-git-2.56.0/bin
/nix/store/nnm9gdr70ihc6zc9298mzz8jpcgaciql-bash-5.3p20/bin
/nix/store/fkz7zn1a0yiryf9kri2yh1s12k1sv557-go-1.26.10/bin
/nix/store/l3jrya2cdjmzxgdpnxzwvx3h416lcbr6-cargo-1.99.0/bin
/nix/store/6l9kbzxwq9ij2lcmwl2qb1jdpqisjr8l-rustc-wrapper-1.99.0/bin
/nix/store/vwgbz9vm1gyxqn6z4fg1jd6va2nzfa3m-rustfmt-1.99.0/bin
/nix/store/r5ri78axx1qggkjq3vawywlzglg70b5w-gcc-wrapper-16.2.0/bin
/nix/store/s70gz6bvz74c36xigh5m2ab2cqli08cv-pkg-config-wrapper-0.29.2/bin
/nix/store/j1j9b0w3mhpccdli73ycj5w7nf6fkzqz-nodejs-24.21.0/bin
```

Use `CC=/nix/store/r5ri78axx1qggkjq3vawywlzglg70b5w-gcc-wrapper-16.2.0/bin/cc`,
`NODE=/nix/store/j1j9b0w3mhpccdli73ycj5w7nf6fkzqz-nodejs-24.21.0/bin/node`,
and `TSC=$repo/clients/js/node_modules/typescript/bin/tsc`.
No regenerated root shell or rustup preparer is needed. MSRV executables below
are independent retained1.95 files; development rustc remains the declared1.99
wrapper. Both toolchains must run; do not select1.95 through PATH for development.

```sh
# 1. Existing Go acceptance bundle; GEM_PATH unset.
GEM_HOME="$repo/.gems" BUNDLE_FROZEN=true \
BUNDLE_GEMFILE="$repo/clients/go/spec/documentation.Gemfile" \
  "$ruby" "$repo/.gems/bin/bundle" exec "$ruby" \
  clients/go/spec/documentation_acceptance.rb

# 2. Existing root bundle, fixed published JS/declarations and strict compiler.
GEM_HOME="$repo/.gems" BUNDLE_FROZEN=true \
BUNDLE_GEMFILE="$repo/Gemfile" \
HAVEAPI_TYPESCRIPT_RUNTIME="$inputs/published-runtime/node_modules/haveapi-client/dist/haveapi-client.js" \
  "$ruby" "$repo/.gems/bin/bundle" exec "$ruby" \
  clients/typescript/spec/documentation/wire.rb

# 3. Existing isolated Rust bundle; development1.99 plus independent1.95.
GEM_HOME="$repo/clients/rust/.gems" \
GEM_PATH="$repo/clients/rust/.gems:/nix/store/jnjll1yxfq02bdcw5pjf9gl86wh8gfhq-ruby-3.4.11/lib/ruby/gems/3.4.0" \
BUNDLE_GEMFILE="$repo/clients/rust/Gemfile" BUNDLE_FROZEN=true \
CARGO_HOME=/home/aither/.cargo CARGO_NET_OFFLINE=true \
HAVEAPI_RUST_DOCUMENTATION=1 \
HAVEAPI_RUST_MSRV_CARGO="$inputs/msrv/rustup/toolchains/1.95.0-x86_64-unknown-linux-gnu/bin/cargo" \
HAVEAPI_RUST_MSRV_RUSTC="$inputs/msrv/rustup/toolchains/1.95.0-x86_64-unknown-linux-gnu/bin/rustc" \
HAVEAPI_RUST_DOCUMENTATION_EVIDENCE=/absolute/fresh/session/verification/rust \
  "$ruby" clients/rust/spec/documentation/run.rb
```

Go formats/builds/executes32 actual Simple/Thorough programs, with literal
credentials and unchanged exact headers/body/query/output/state checks; its
runner enforces GOWORK/GOPROXY/GOSUMDB off and GOTOOLCHAIN local. TS compiles28
root/mount × both-detail × seven-case programs with NodeNext/ES2022/strict/
exactOptionalPropertyTypes/noUncheckedIndexedAccess/verbatimModuleSyntax, then
runs the local wire fixture against published0.30.2. Rust uses root+/mounted/api/,
async/blocking action Simple/Thorough plus its init/auth/profile variants, both
development1.99 and independent1.95. Its opt-in documentation fixture receives
public literals through normal handlers; actual token acquisition must issue
example-token. Exact Simple fragments compose at the existing let_=&api seam.
Generated source/config/lock/tool evidence stays with the fresh run directory.

## Remaining gaps and stopping boundary

No selected required executable is currently missing. Historical missing
Go/Cargo/rustfmt records are superseded only for availability by exact restoration.
The old Nix rustup preparer and broad shell derivation remain unnecessary and
unavailable; do not rebuild/replace them. Cached158 Rust package archives/sources
were observed historically, not re-audited here. Fresh generated-crate offline
lock resolution remains UNPROVEN despite the successful narrower16-program M8
quick using the copied runtime lock. No automatic fetch on an offline miss.
Fresh npm/uv isolated-cache completeness is also unproven; these three commands
use existing compiler/runtime inputs and do not invoke installers.

After review/main relay, one fresh retained Luna/low watcher owns the serialized
batch and its logs/PIDs under the monitor skill, with current native full-access/
never proof. Expected warm Go/TS1–3min each, Rust5–20min; do not run duplicate
ordinary CI units/runtime suites or an extra strict-compile/make-doc quick.
Retain the TS60s preparation/10s snippet and Rust30s readiness/native teardown
limits. Do not invent retry loops or arbitrary replacement timeouts.
Stop the batch on its first actual compile/wire/harness failure, source/input/
toolchain drift, missing declared input or unexpected kernel build. Preserve
failed evidence, reconcile owned child effects and report; do not retry, install,
substitute, relax checks or change runtime/reference/budgets. Main grants any
bounded diagnosis beyond that stop. No pass or runtime-loaded identity is claimed
by this static preparation. Source/Git/utility remain quiet and unclaimed.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-27-api-documentation-redesign/
