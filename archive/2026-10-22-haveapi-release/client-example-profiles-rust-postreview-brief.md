# Rust profile simplification: post-review execution brief

Preparation only. No application check, generation, formatter/compiler/tool
identity execution, dependency setup, network operation or Git command ran while
preparing this package. No utility was launched. Final review has not started;
this file does not authorize execution. Implementer3 owns these Rust technical
facts; implementer1 owns the overall long-plan and utility/setup coordination.

## Frozen source and later gate

Use only the registered `haveapi-client-example-profiles` worktree and branch
`2026-10-24-haveapi-client-example-profiles`, from immutable base
`4dc0f7e11c494d1a0dc852dabcc312411699fcab`. The final committed/reviewed candidate
head is intentionally unset. Owner0 supplies it after all intended packages are
committed and independent final review passes. Owner0 remains sole Git owner.

All ten Rust paths still match the yielded
[final inventory](client-example-profiles-rust-final-inventory.json), file SHA-256
`8dc9cd174c94d9fff4648966a1df13c070edc2bd7dcc1e990fed00378055a800`,
files-map SHA-256
`d2f5edfda004895df815693224e1ae965fa3d52713ce38e444933e04fa5d50cd`.
The [readiness record](client-example-profiles-rust-postreview-readiness.json)
adds 24 source/input file hashes, actual file-presence/cache observations,
retained binary identities and exact graph-output bindings. Hash inspection is
source evidence, not execution of those tools or checks.

Before later execution, bind the exact reviewed head/tree and unchanged input
inventory through owner0/lead's overall packet, recheck tools and frozen Ruby
locks, and verify a fresh watcher's actual resolved policy/readiness. Use one
fresh Luna/low watcher for the authorized batch under the monitoring skill.
No retry, source repair or source/input relaxation belongs to that utility.

## Existing tools and graph evidence

| Selection | Exact executable | Retained identity |
| --- | --- | --- |
| Development Cargo | `/nix/store/1jwkiz96iwqdhm4bh2hvgd86ysb0b67q-cargo-1.99.0/bin/cargo` | Cargo 1.99.0 |
| Development rustc | `/nix/store/6l9kbzxwq9ij2lcmwl2qb1jdpqisjr8l-rustc-wrapper-1.99.0/bin/rustc` | rustc 1.99.0 |
| Generation formatter | `/nix/store/zfrqd9ahnccql0zgzgc5swwi4zmm14zl-rustfmt-1.99.0/bin/rustfmt` | rustfmt 1.10.0 |
| Independent MSRV Cargo | `/nix/store/rai05nypxnmj22l65nwsk5xjsaq8s4vc-cargo-1.95.0/bin/cargo` | Cargo 1.95.0 |
| Independent MSRV rustc | `/nix/store/m4hrdkg9ypcw8y1banfc26q3f27kfqvb-rustc-wrapper-1.95.0/bin/rustc` | rustc 1.95.0 |

All five executables and selected derivation files are present. File hashes
equal the accepted setup's retained facts; no new `--version` command ran.
The actual version string of the formatter is 1.10.0, although its package path
contains 1.99.0. Do not use downstream's different formatter or compiler.

The retained complete graphs are beneath
`followups-verification-final-phases-090a188c-20261023T165049Z/`:

- `root-shell-derivation-input-graph.json`: 2,067 derivations, SHA-256
  `7d394152391db092c3059053548a0a3d30dec997c658bd9c3e71cb1137f9d0bb`.
- `msrv-tool-derivation-input-graph.json`: 1,377 derivations, SHA-256
  `73c7ec394365b777c149977899237a47d4e999e4424f6d85c4c6fc34cd294c01`.

The readiness JSON binds each tool to its exact `out` value in those graphs.
Their JSON uses store basenames for derivation keys and output paths; normalize
that representation before comparison. Do not use the local store's recorded
producer as the authoritative derivation. The old root shell derivation is
`/nix/store/ms7sialdgqsap5c6fbrm4hnlmgdf1dg9-haveapi.drv`; it is historical
evidence, not a new evaluation of the uncommitted candidate. Owner1's later
preflight must bind the selected outputs to the accepted current locked inputs
without pretending these old graph files are a new evaluation. MSRV is the
explicit independent pair; its historical nixpkgs revision is unknown.

## Ruby parent and child server environment

Use the existing own Rust profile through
`client-example-profiles-setup-preparation/in_bundle.py --cwd clients/rust rust`.
It clears inherited Ruby/Gem/Bundler variables and loads the accepted own
environment. Ruby is 3.4.11, Bundler is 4.0.23, and nondefault Fiddle is 1.1.8.
No bundle install, Nix shell hook, native gem copying or old writable gem home is
needed. The component `Gemfile.lock` SHA-256 is
`7f51e5ea00157f4d215355acec5d95c2a8bcbb7d4600c5b34f5e1a338acbc1e4`.

Both Rust runners use the component bundle. The rendered runner loads
`spec/integration/run.rb`, whose `with_server` invokes
`bundle exec RbConfig.ruby .../support/haveapi_server.rb --mount MOUNT` inside
`Bundler.with_unbundled_env`, explicitly setting:

- `BUNDLE_GEMFILE=<worktree>/servers/ruby/Gemfile`;
- `GEM_HOME=<worktree>/.gems`, with `GEM_PATH` unset;
- the same Ruby interpreter as the parent.

Thus the child requires the already prepared own server bundle in the worktree
root `.gems`; the Rust component `.gems` alone is insufficient. Both own homes
contain Bundler 4.0.23. The ignored server lock SHA-256 is
`cec5e86c703239afa8c5914111ec3773ac7b8b485fc8e33cba80872cc51959b5`.
Use the Rust wrapper profile for the parent, not the server wrapper profile.
The accepted server readiness and generated docs prerequisite are already
recorded by owners1/0; do not rerun setup or `make doc` merely for this packet.

The fixture listens only on `127.0.0.1`, kernel-selected port zero, and the
runner waits for its explicit readiness line. Its existing 30-second startup
gate and owned teardown are runner behavior, not a new generic build timeout.
The later grant must authorize these local listeners/HTTP fixture calls.
There is no real API or external SDK acquisition.

## Fresh evidence, cache and commands

[Structured commands](client-example-profiles-rust-postreview-commands.json)
provide exact argv, environment, input-clearing requirements and proposed log
paths. Replace only the future `.../client-example-profiles-rust-postreview-run-UNSET`
root with a new nonexistent absolute session directory after the execution
grant. Do not reuse prior release, downstream or other Rust caches. At this
inspection, worktree-root and `clients/rust` `.cargo` and `target` directories
are absent; inherited `CARGO_HOME` and `CARGO_TARGET_DIR` are unset. Ambient
`~/.cargo` was neither inspected nor qualified for reuse.

The later driver creates the new run root, `cargo-home`, `cargo-target` and
`tmp`, then exports `CARGO_HOME`, `CARGO_TARGET_DIR` and `TMPDIR` there. Both
runners retain their normal temporary-tree handling; evidence and Cargo target
data remain outside those temporary trees. Keep `model-equivalence` nonexistent
because its runner creates it atomically; the rendered runner creates its own
fresh `rendered/root` and `rendered/mounted-api` evidence subdirectories.

The structured environment carries the already declared native compiler and
linker settings. It selects exact rustfmt through `RUSTFMT`; the wrapper PATH
also selects that same rustfmt, which the rendered runner probes by name.
Clear inherited compiler wrappers, Rust flags, target/linker and registry
overrides as listed in the structured commands. The rendered runner itself
refuses nonempty `RUSTC`, `RUSTC_WRAPPER` or `RUSTC_WORKSPACE_WRAPPER`; it sets
`RUSTC` to the explicit 1.95 binary only inside its MSRV subprocesses.

From the worktree root, with that future common environment established:

```sh
HAVEAPI_RUST_MODEL_EQUIVALENCE=1 \
HAVEAPI_RUST_MODEL_EVIDENCE="$RUST_POSTREVIEW_ROOT/model-equivalence" \
python3 -B /home/aither/workspace/ai/vpsfree.cz/work/2026-10-22-haveapi-release/client-example-profiles-setup-preparation/in_bundle.py \
  --cwd clients/rust rust -- bundle _4.0.23_ exec ruby spec/documentation/model_equivalence.rb

HAVEAPI_RUST_DOCUMENTATION=1 \
HAVEAPI_RUST_DOCUMENTATION_EVIDENCE="$RUST_POSTREVIEW_ROOT/rendered" \
HAVEAPI_RUST_MSRV_CARGO=/nix/store/rai05nypxnmj22l65nwsk5xjsaq8s4vc-cargo-1.95.0/bin/cargo \
HAVEAPI_RUST_MSRV_RUSTC=/nix/store/m4hrdkg9ypcw8y1banfc26q3f27kfqvb-rustc-wrapper-1.95.0/bin/rustc \
python3 -B /home/aither/workspace/ai/vpsfree.cz/work/2026-10-22-haveapi-release/client-example-profiles-setup-preparation/in_bundle.py \
  --cwd clients/rust rust -- bundle _4.0.23_ exec ruby spec/documentation/run.rb
```

First command: read immutable 4dc0 objects with the runner's read-only
`git archive`, generate the same saved snapshot/config through baseline,
candidate and repeat with the same formatter, and retain all sources/outputs.
All owned bytes must match except ownership manifest `generator_source_sha256`;
all other manifest fields match, and candidate/repeat manifests match fully.
No Cargo, HTTP, install or compiler is involved in this phase.

Second command: capture the real disposable server description separately at
`/` and `/mounted/api/`, generate matching fixture SDKs, and extract actual
renderer output. It creates one Cargo.lock per mount, then performs
`cargo check --locked --all-features --examples` and each
`cargo run --locked --quiet --all-features --example NAME` under development and
independent 1.95. There are 34 programs per mount (17 async and 17 blocking),
four locked checks and 136 locked runs overall. The automatic unversioned
profile exercises the request cases; additional init programs cover legacy,
saved unversioned, Git and versioned Git forms. Auth programs use real fixture
flows; payload/null/omission/list/nested/state/error assertions remain in the
existing cases. Blocking programs keep their lifecycle outside an async runtime.

## Later download/native-build scope

No own Cargo cache is prepared. Permit the unchanged rendered runner's two
`cargo generate-lockfile --manifest-path ...` operations in temporary fixtures,
ordinary default Cargo registry index reads, and checksum-verified crate
downloads for their locks into the new Cargo home. Subsequent checks/runs use
`--locked`. Do not set offline mode without a separately proven complete cache.
Do not copy a prior Cargo.lock into the fixture or alter generator inputs.

The exact direct requirements are unchanged: serde `1` with `derive`,
serde_json `1`, url `2.5`, reqwest `0.13.5` with default features disabled and
`json,rustls`, plus dev Tokio `1` with `macros,rt-multi-thread`; the blocking
feature enables `reqwest/blocking`. The two future fixture locks do not exist
yet, so their exact resolved transitive versions/download list cannot honestly
be supplied before the authorized resolution. Retain both actual locks and
their hashes with the downloaded-source/checksum inventory after execution.
These manifest strings retain normal Cargo requirement semantics; they are
not assertions of the versions the future resolver will select.

The unchanged private runtime lock has 159 records (158 registry records),
SHA-256 `48e682446003c37e3ec111308a35a49fb895affe8b0ea3f7ae109b6655f00746`.
The readiness JSON retains its complete name/version/checksum/edge list as a
reference only. It is not the generated documentation fixture's graph.

Native compilation may build TLS dependencies such as aws-lc-sys/ring. The
declared PATH already contains GCC/C++ wrapper 16.2.0, binutils wrapper 2.46,
GNU make 4.4.1 and pkg-config wrapper 0.29.2, with existing OpenSSL/libffi
development inputs. Exact resolved executable paths/hashes and declared native
exports are in the JSON. No new Nix package/build or native Ruby install is
proposed. External `cmake` is absent from that PATH; the reference lock's Rust
`cmake` crate does not establish that this supported Linux build path needs the
external tool. If an actual native prerequisite fails, stop and report it;
do not add tools or change flags speculatively. Unexpected kernel builds stop.

## Evidence and limits

Capture each command's full output, exact exit and timing; stop on the first
failure. Retain tool identity probes, final source/input hashes, graph/output
bindings, the model-equivalence sources/inputs/manifests, both rendered mount
snapshots/configs/Cargo manifests/locks/generated source and emitted examples.
The existing rendered evidence helper retains those files even when a command
fails. Keep fresh Cargo home/target outputs and failures; no cleanup is granted.

These checks validate generated fixture SDKs and actual emitted Rust. Git
installation comments are inspected while compiling against the local fixture;
they never fetch a Git SDK. Passing does not establish installed/published
vpsAdmin SDK compatibility or authorize publication, deployment, release,
integration, version changes or a live API refresh. Release0.30.1 remains held.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-haveapi-release/
