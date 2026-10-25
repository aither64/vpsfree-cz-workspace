# Rust documentation profile simplification

Status: Rust source and assigned quick checks are complete and yielded to the
lead and sole Git owner implementer0. Final pure checks passed: 90 examples,
0 failures; RuboCop inspected all 10 owned files with no offenses; all 10 Ruby
syntax checks passed. No command remains active. Generation, Cargo, compiler
and rendered-source acceptance remain unexecuted pending committed final review.
Owner1 separately completed the isolated dependency setup before these checks.

Bound session/workspace and implementer3 workspace_write access were verified.
Owner0's registration was independently checked at
`worktrees/2026-10-22-haveapi-release/haveapi-client-example-profiles`, branch
`2026-10-24-haveapi-client-example-profiles`, base/head
`4dc0f7e11c494d1a0dc852dabcc312411699fcab`, tree
`a5c78fa77f4647e75d3f485ab12d7657bfcfab01`, initially clean with empty index.
Owner0 retains all Git/index/hooks and shared server/documentation ownership.
The complete accepted design and required project/workspace procedures were read.

## Rust-owned paths and interfaces

1. `clients/rust/lib/haveapi/rust_client.rb`
2. `clients/rust/lib/haveapi/rust_client/model.rb` (new)
3. `clients/rust/lib/haveapi/rust_client/generator.rb`
4. `clients/rust/lib/haveapi/rust_client/documentation.rb`
5. `clients/rust/spec/unit/documentation_factory_spec.rb` (new)
6. `clients/rust/spec/unit/model_spec.rb` (new)
7. `clients/rust/spec/unit/model_equivalence_spec.rb` (new)
8. `clients/rust/spec/unit/documentation_harness_spec.rb`
9. `clients/rust/spec/documentation/run.rb`
10. `clients/rust/spec/documentation/model_equivalence.rb` (new)

Factories implement the exact accepted keywords:
`from_description(description:, api_version:, protocol_version:, mount_path:,
crate_name:, crate_version: nil, source: nil)` and
`from_snapshot(snapshot:, crate_name:, crate_version: nil, source: nil)`.
Legacy `new(snapshot:, config:)` remains supported, with optional source metadata.
Factories construct Snapshot/IR directly; documentation never constructs a
Generator or manufactures packaging fields. Internal structural URLs never
become rendered requests or claimed SDK provenance.

Shared Model contains only existing Rust type/metadata helpers and
`validate_package(crate_name:, crate_version: nil, required_version: false)`.
Actual Generator requires a version and preserves all six packaging fields,
license/edition/MSRV/formatter validation. Public `Generator.validate_config(config)`
also lets shared registration validate deferred legacy profiles without constructing
a generator. Private instance validation delegates to that same method.

`Documentation.validate_source(source)` accepts only nil or the exact two-key
git/rev hash, returning copied/frozen string keys and values. It rejects invalid
HTTPS URLs, credentials, query/fragment/control characters and non-40-hex revs
with a generic error. No URL is fetched. Omitted registry versions remain nil
and render normal cargo-add commands; explicit versions retain ordinary Cargo
requirements, while Git/rev selects source and an explicit version constrains
its package. TOML string values are escaped independently of Rust literals.

## Verification boundaries

Pure factory/model specs cover optional/explicit versions, source validation,
TOML round-trip, immutability, actual-context URL visibility, legacy/new equivalence,
canonical collisions, authorized hidden fields, metadata consistency and strict
generator validation. Existing documentation specs retain payload, null/omission,
list, nested path, hostile literal, auth, error and numeric limitation checks.

The final focused command ran from the registered worktree using owner1's
validated wrapper and the new component's own frozen bundle:

```sh
python3 -B /home/aither/workspace/ai/vpsfree.cz/work/2026-10-22-haveapi-release/client-example-profiles-setup-preparation/in_bundle.py \
  --cwd clients/rust rust -- bundle _4.0.23_ exec rspec \
  spec/unit/documentation_spec.rb spec/unit/documentation_factory_spec.rb \
  spec/unit/model_spec.rb spec/unit/model_equivalence_spec.rb \
  spec/unit/documentation_harness_spec.rb
```

It passed 90 examples with 0 failures, seed 53557. The same isolated Ruby/bundle
was used for the 10-file style and syntax checks. The existing generator specs
invoke rustfmt generation and were excluded from this pre-review selection.
The exact formatter was identified but was not invoked by these quick checks.

Setup evidence is in
[dependency-readiness.json](client-example-profiles-setup-preparation/dependency-readiness.json),
[rust-03-check.json](client-example-profiles-setup-preparation/rust-03-check.json),
[rust-04-activation.log](client-example-profiles-setup-preparation/rust-04-activation.log)
and [00-rustfmt-identity.log](client-example-profiles-setup-preparation/00-rustfmt-identity.log).
The selected environment was Ruby 3.4.11, Bundler 4.0.23 and nondefault Fiddle
1.1.8 in this worktree's `clients/rust/.gems`. The formatter identity was
`/nix/store/zfrqd9ahnccql0zgzgc5swwi4zmm14zl-rustfmt-1.99.0/bin/rustfmt`,
reporting rustfmt 1.10.0. The wrapper clears inherited Ruby/Gem/Bundler settings
and selects the declared tool paths without running Nix shell hooks.

Final logs and corresponding `.exit` files (all exit 0):

- [Focused RSpec](client-example-profiles-rust-final-reviewed-focused.log): 90/0.
- [RuboCop](client-example-profiles-rust-final-style.log): 10 files, no offenses.
- [Ruby syntax](client-example-profiles-rust-syntax.log): 10 Syntax OK results.

The original failed focused check is retained in
[client-example-profiles-rust-focused.log](client-example-profiles-rust-focused.log).
Its hidden-value sentinel `unavailable` overlapped an existing generic limitation
word. Replacing only that test sentinel with `not-visible-secret` fixed the
assertion; product limitation wording was unchanged. Initial style findings and
their corrections are also retained. The final focused suite passed after all
style-related edits, with no lint rule relaxation.

The real rendered-source acceptance runner now renders the full fixture through
automatic unversioned factories at root/mounted paths, preserving async/blocking
and independent MSRV passes. Extra init programs retain actual renderer output
for legacy, saved unversioned and Git forms. Git source appears only as inspected
installation comments; compilation uses the matching locally generated fixture
and does not establish installed-Git SDK compatibility.

After committed final review, the generation-only comparison command is:

```sh
HAVEAPI_RUST_MODEL_EQUIVALENCE=1 \
HAVEAPI_RUST_MODEL_EVIDENCE=/path/to/new-evidence-directory \
bundle exec ruby spec/documentation/model_equivalence.rb
```

Run from clients/rust in the confirmed environment. The harness reads immutable
4dc0 Git objects into the new evidence directory, generates one fixture with
the baseline source and twice with candidate source, and retains inputs,
generated files, ownership manifests and stdout/stderr. Every owned nonmanifest
byte and all manifest fields must match except `generator_source_sha256`, which
necessarily identifies changed generator Ruby source. Candidate/repeat manifests
must also be equal. There is no compiler, registry, network or native installation.
The quick comparison contract spec only uses tiny synthetic files.

[Canonical input inventory](client-example-profiles-rust-baseline.json) records
55 baseline Rust/template/runtime/spec/lock/flake paths, SHA-256
`fb8164d0336a376d8c5831a1dc2e0c61e204ea61acb6c54ea2f720a8fd0f160b`.
Runtime, templates, IR/naming, Cargo, dependencies and Nix inputs are unchanged.
No SDK regeneration or release/default integration is part of this work.

## Final source yield

[Final inventory](client-example-profiles-rust-final-inventory.json) records the
exact 10 owned paths, byte lengths, modes, SHA-256 hashes, log hashes and setup
identity. Its file SHA-256 is
`8dc9cd174c94d9fff4648966a1df13c070edc2bd7dcc1e990fed00378055a800`.
The owned-files aggregate is
`d2f5edfda004895df815693224e1ae965fa3d52713ce38e444933e04fa5d50cd`,
computed as SHA-256 of UTF-8 JSON for the `files` mapping with sorted keys and
compact separators `(',', ':')`. Source and retained log hashes were rechecked
at handoff; no application edits followed the final checks.

The original `rust_type` and `meta_parameters` method bodies are unchanged in
the extracted Model. Templates, runtime/Cargo, IR/Naming/Snapshot, component
Gemfile/lock and flake inputs are unchanged from 4dc0. No Git/index mutation was
performed; implementer0 remains the sole Git owner. Lead accepted visible
commands/errors and owns prose; implementer0 owns shared documentation. No
interaction finding arose from these pure Rust checks. Whole-package commits,
independent final review and authorized longer checks remain separate gates.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-haveapi-release/
