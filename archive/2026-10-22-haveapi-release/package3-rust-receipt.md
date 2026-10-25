# Rust documentation examples

Owner: implementer3. Session/environment identity and roster workspace-write
access verified on 2026-10-22. Baseline: HaveAPI `08345b2`.

## Source checks

- `Generator.new(schema:, config:)` validates the existing exact TOML contract,
  validates the Snapshot and builds full IR without network, subprocesses or
  generated-file writes. The documentation adapter can reuse this constructor.
- `IR` owns normalized resource modules, action methods, ancestor bindings,
  ordered placeholders and parameter fields. Keep full saved IR internal;
  authorization must intersect it with the current request's filtered help.
- `Generator#rust_type` and `#meta_parameters` supply canonical types/metadata.
- Async requests use `.send().await`; blocking requests use `.send()` and the
  `blocking` Cargo feature. Construct, use and drop a blocking client outside
  async runtime threads.
- Object inputs have generated setters and nullable `_null` setters. Lists use
  `.input(Vec<Input>)`; public fields are `InputValue::Unset`, `Null` or `Value`.
- `Response` exposes `output`, `meta` and `http_status`. Authentication uses
  builder methods `basic_auth`, `token` and `oauth2_token`. Error diagnostics
  expose `http_status()`, `server_message()` and `validation_errors()`;
  displaying raw diagnostic values needs care because they may be sensitive.
- GET list and nested Custom input remain unsupported; no capability expansion
  is part of this package. No high-level operation waiting helper exists.

## Current state

Architect's frozen [contract](api-doc-contract.md) accepted by lead. Implemented
the pure `HaveAPI::RustClient::Documentation` adapter and stable async/blocking
server renderer classes. No shared-file edits or Git/index/hooks operations.
Lead completed required prose pass over `clients/rust/docs/documentation.md`,
its README link, and user-visible adapter/renderer strings.

Owned application deliverables in the HaveAPI worktree:

- `clients/rust/lib/haveapi/rust_client/documentation.rb`
- `servers/ruby/lib/haveapi/client_examples/rust_client.rb`
- `clients/rust/spec/unit/documentation_spec.rb`
- `clients/rust/spec/unit/documentation_harness_spec.rb`
- `servers/ruby/spec/client_examples/rust_client_spec.rb`
- `clients/rust/spec/documentation/{cases,run}.rb`
- `clients/rust/docs/documentation.md` and README entry-point link.

The adapter copies saved inputs, validates through Generator/IR and freezes the
cyclic internal map. It does not cache or mutate per-request state. Rendering
checks authorized help before emitting route/input/output/authentication code.
Unsupported examples return frozen limitation hashes without schema names,
defaults, sample secrets or local profile paths. List input uses actual generated
structs; authenticated action programs select an advertised available provider.
No migrations, runtime/generator capability expansion or deployment changes.

## Quick evidence

Fresh pinned verification watcher `rust_quick_setup`, `gpt-6-luna/low`, catalog
`840de47527dea8325fcac0c2eb7ca5ae9728b31523ec368bcce595c6f15983fa`, full-access
native utility identity `dw_b9dd4137280d3e047a81fbdfe0ea73c900c9fd89f8861d12`,
ran the first uncertain Rust component setup/check operation. It exited 1 in six
seconds: 17 adapter specs, two fixture expectation failures. The alleged name
collision used distinct names; the escaping fixture used a literal backslash-n.
Corrected fixture names/string. No underlying generator deviation was needed.
Original evidence: [quick log](package3-quick.log),
[exit status](package3-quick.exit). No command remains running.

Final quick checks passed: 20 adapter examples plus five acceptance-harness
contracts (25 total, 0.13 seconds), and seven standalone server bridge examples
(0.05 seconds). Ruby style passes on all seven owned Ruby source/spec/runner
files after ordinary auto-corrections; no bypasses. Implementer0 independently
included the bridge in a 33-example passing renderer batch. Component setup and
all quick commands have exited; no command remains running.

Known quick commands (from repository root):

```sh
nix develop .#client-rust --command bash -c 'cd clients/rust && bundle exec rspec spec/unit/documentation_spec.rb spec/unit/documentation_harness_spec.rb && bundle exec rubocop lib/haveapi/rust_client/documentation.rb spec/unit/documentation_spec.rb spec/unit/documentation_harness_spec.rb spec/documentation'
HAVEAPI_RELEASE_TOOLS_ONLY=1 nix develop --command bash -c 'cd servers/ruby && bundle exec rspec spec/client_examples/rust_client_spec.rb && bundle exec rubocop lib/haveapi/client_examples/rust_client.rb spec/client_examples/rust_client_spec.rb'
```

The acceptance runner and fixture source are part of the deliverable before
review. It extracts actual registered renderer output, generates a matching SDK,
adds output assertions without rewriting requests, and composes emitted auth
builders with emitted action bodies. Both modes use 13 programs each at `/` and
`/mounted/api/` under development Rust and independent Rust 1.95. Execution is
pending final committed-deliverable review. No Cargo/server acceptance was run.

```sh
HAVEAPI_RUST_DOCUMENTATION=1 \
HAVEAPI_RUST_MSRV_CARGO=/absolute/rust-1.95/bin/cargo \
HAVEAPI_RUST_MSRV_RUSTC=/absolute/rust-1.95/bin/rustc \
nix develop .#client-rust --command ruby clients/rust/spec/documentation/run.rb
```

No new shared dependency required. Pure bridge specs use a fake adapter; real
combined adapter/renderer contracts run under the Rust bundle and load only the
server's base/context/renderers. The disposable real server retains its separate
server bundle and default Ruby gem paths. Component gem-home setup is serialized
with implementer0; initial setup is now known quick.

## Verification gates

First: pure adapter/renderer capability specs and Ruby style in declared Nix
environments, serialized with shared gem-home setup by implementer0. Next:
all deliverables committed and independent final review. Only then generate
fixture crates and compile/run actual async/blocking snippets, including MSRV,
through a fresh verification watcher. Shared runner/dependency changes and all
Git operations belong to implementer0. Lead owns final documentation prose pass.

## Bounded evidence follow-up

Main nine-path Rust package committed by implementer0 as `db412ea`. Before
final review, lead requested fixture graph retention. Changed only these three
project paths: `clients/rust/spec/documentation/run.rb`,
`clients/rust/spec/unit/documentation_harness_spec.rb`,
`clients/rust/docs/documentation.md`. Implementer0 owns the fixup/fold; no Git
mutation by implementer3.

The optional `HAVEAPI_RUST_DOCUMENTATION_EVIDENCE` retains `root` and
`mounted-api` receipts with the loaded snapshot, generator TOML, Cargo.toml and
the actual generated Cargo.lock, complete generated source/ownership manifest,
emitted examples, and selected tool paths/verbose versions. Separate temporary
crates prevent a failed second mount from inheriting the first mount's files.
Existing receipt directories are refused. An ensure block retains artifacts
available on failure. No target, build output, gem home or Cargo cache is copied.
No fixture token or HTTP auth response is retained. Compiler overrides are
refused so the development and MSRV passes preserve their selected identities.

Read architect's [MSRV readiness](api-doc-msrv-readiness.md). Development is
Rust/Cargo 1.99.0, generation formatter is `rustfmt 1.10.0`, independently
selected local MSRV Cargo/compiler are 1.95.0. That receipt holds exact store
paths, derivation roots, source/NAR hashes and complete graph digest. The private
runtime harness Cargo.lock is a different dependency graph and is not used as
evidence for a generated fixture.

Lead completed the new ENV instruction/paragraph prose pass unchanged. First
follow-up quick run passed 28 adapter/harness examples; four routine style
offenses were fixed. Final quick rerun passed 28 examples in 0.14 seconds;
five Ruby files inspected, no offenses. All commands exited; setup slot free.

Exact post-review selection, not executed:

```sh
HAVEAPI_RUST_DOCUMENTATION=1 \
HAVEAPI_RUST_MSRV_CARGO=/nix/store/rai05nypxnmj22l65nwsk5xjsaq8s4vc-cargo-1.95.0/bin/cargo \
HAVEAPI_RUST_MSRV_RUSTC=/nix/store/m4hrdkg9ypcw8y1banfc26q3f27kfqvb-rustc-wrapper-1.95.0/bin/rustc \
HAVEAPI_RUST_DOCUMENTATION_EVIDENCE=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-22-haveapi-release/rust-documentation-evidence \
nix develop .#client-rust --command ruby clients/rust/spec/documentation/run.rb
```

The evidence directory above must not already contain mount receipts. Long
acceptance still waits for final independent committed-deliverable review and a
fresh verification watcher. No installation or compiler campaign performed.

## Final-review A1 remediation

Read the completed [final review](api-doc-final-review.md), advisory A1. Lead
accepted a narrow correction after the frozen `607941c0` review concluded.
The Float capability check now requires a real, finite Ruby Numeric whose
converted `f64` is also finite. This prevents large finite Integers from emitting
invalid `Infinity_f64`, and rejects non-real Complex input before conversion.
Existing generic sample-value limitation text is unchanged; no generator/runtime
behavior, public API or documentation wording changed.

Exact two-file delta: `clients/rust/lib/haveapi/rust_client/documentation.rb`
and `clients/rust/spec/unit/documentation_spec.rb`. Sixteen new examples cover
positive/negative overflow and non-real Numeric input, plus ordinary finite
integer/float controls, across object/list input and async/blocking modes.
Focused adapter/harness checks pass: **44 examples, 0 failures** in 0.17 seconds;
both changed Ruby files pass style with no offenses. The serialized known-quick
Rust component command exited; no compiler acceptance or Git mutation performed.
Implementer0 owns the hooked fixup/fold into the Rust source commit `1f8aac4c`.
