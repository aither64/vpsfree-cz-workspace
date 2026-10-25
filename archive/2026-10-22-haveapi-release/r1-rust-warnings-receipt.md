# R1 Rust generator warning follow-up

Owner: implementer3. Lead granted R1 under architect's frozen
[follow-up brief](release-followups-design.md). Verified exact session/environment
`2026-10-22-haveapi-release`, workspace `/home/aither/workspace/ai/vpsfree.cz`,
roster workspace-write access, new worktree `haveapi-followups`, branch
`2026-10-22-haveapi-release-followups`, clean starting head
`b64fb25bea8d8222fb3263b99956c0b61438a859`. Released 0.30.0/source/artifacts remain
untouched. Implementer0 owns all Git/index/hooks and shared flake changes.

## Source and dependency decision

Generator loading unconditionally requires `fiddle/import`; atomic replacement
uses Fiddle to call `renameat2`. Declare a runtime dependency rather than relying
on Ruby's default-gem packaging. Official RubyGems metadata on 2026-10-22 reports
latest stable `fiddle` **1.1.8**, released 2025-04-25, Ruby requirement >=2.5.0,
platform ruby, no runtime dependencies, upstream https://github.com/ruby/fiddle.
The declared generator Ruby >=3.2 support remains unchanged.

Selected gem requirement `~> 1.1`, `>= 1.1.8`; component lock resolves 1.1.8 with
official SHA-256
`7fa8ee3627271497f3add5503acdbc3f40b32f610fc1cf49634f083ef3f32eee`.
[Retained official metadata](r1-fiddle-upstream.json) binds the exact endpoint.
Bundler 4.0.23 generated the lock; it was not hand edited. Final diff has exactly
three additive lines (gemspec requirement, resolved version, checksum) without
unrelated version/platform/checksum changes.

- Original lock SHA-256:
  `aed5ca5faa7faa3439069bda4982663108083131bcd996b4c160f2641416e23a`.
- Final lock SHA-256:
  `7f51e5ea00157f4d215355acec5d95c2a8bcbb7d4600c5b34f5e1a338acbc1e4`.
- Final gemspec SHA-256:
  `1cadfc6842688c09181dc15cca798bbe42aece741473713396881364f9d9ee09`.

Two ERB templates add `#[allow(non_snake_case)]` only to generated resource
module declarations and client accessor methods whose existing public identifier
contains `__`. Comments explain the component-boundary naming contract. Names,
routes, IR allocation, generated field/action behavior, runtime source, Cargo
dependencies and atomic exchange remain unchanged. Unit fixtures distinguish
`widget__task` from `widget_task` and include `authentication__token__token`.

Added focused integration mode `HAVEAPI_RUST_NAME_LINT=1` compiles the generated
fixture library with all transport features and `-D non_snake_case` under both
development Rust and explicit 1.95. Ordinary integration execution remains the
default. Pure specs mock Cargo and assert exact lint/toolchain/failure behavior.
Actual compiler execution waits for committed-deliverable final review.

## Setup incident and native prerequisite

Owner attempted metadata-only lock refresh by evaluating `nix print-dev-env`.
Its generated environment unexpectedly invoked the component shell hook,
installing Bundler and dependencies in this new worktree's own
`clients/rust/.gems`. Handle 71892/owned process group 723009 exited 7 before a
TERM attempt; authoritative process inspection found no remaining group. It
failed building Fiddle 1.1.8: pkg-config could not find libffi and neither
`ffi.h` nor `ffi/ffi.h` existed in the declared environment. See
[native failure](r1-fiddle-setup-failure.log) and [mkmf](r1-fiddle-mkmf.log).
No old/shared gem home, published source or release artifact was changed.
Partial own installed gems are preserved. No retry was made from that operation.

Lead approved the concrete minimal prerequisite. Implementer0 added `libffi`
only to the default release and client-rust shell package lists; both already
provided pkg-config. No Nix input/flake.lock or runtime change. Architect was
notified through the lead and a subsequently delivered direct peer message.

The initial lock remained byte-identical after that failed install. Running the
declared exact Ruby interpreter and new own Bundler executable directly avoided
shell evaluation. `bundle lock --update fiddle --conservative --add-checksums`
refused because the newly declared gem was not previously locked. Ordinary
`bundle lock --conservative --add-checksums` then completed metadata-only and
produced the verified three-line delta above. Current isolated `bundle check`
reports **only fiddle 1.1.8 missing**. No setup process is running.

Prepared [frozen setup script](r1-setup.sh), syntax checked, intentionally uses
the normal declared component hook install with `BUNDLE_FROZEN=true`. It guards
the lock/gemspec hashes before and after, uses only this component gem home and
ignored Bundler user cache under `.gems`, then verifies the activated Fiddle is
1.1.8 and not a default gem. Parent reserved the single global utility slot for
this operation after J1. At that preparation checkpoint no ambient install,
eval workaround, install retry or compiler campaign was launched.

## Completed setup and quick checks

Lead granted the fresh setup operation after J1 yielded the global utility slot.
Utility `/root/r1_frozen_setup`, fresh context, pinned `gpt-6-luna`/`low`, native
identity `dw_b9dd4137280d3e047a81fbdfe0ea73c900c9fd89f8861d12`, catalog digest
`840de47527dea8325fcac0c2eb7ca5ae9728b31523ec368bcce595c6f15983fa`, ran under
`danger-full-access`/`never`. The installed utility TOML and current package
full-access policy were read before launch. It ran exactly the approved script
once, at head `b64fb25`, and exited **0 in 21.80 seconds**. Pre/post lock/gemspec
hashes match the frozen values above. `bundle check` passed; nondefault
`fiddle-1.1.8` activated successfully. No process remains. Global utility slot
explicitly yielded to lead. Evidence: [full log](r1-setup.log),
[status](r1-setup.exit), [identity/timing/hash result](r1-setup-result.json).
No source/lock was changed by the utility and no old/shared gem home was used.

Full `make test-rust-unit`: **79 examples, 0 failures**, 2.84 seconds. This covers
the newly declared installed Fiddle dependency, deterministic regeneration/check
and exact nested/flat resource names/routes, plus mocked compiler/lint command
contracts. First run had one fixture assertion expecting a one-line method
signature that rustfmt rendered across lines; corrected the assertion's
whitespace handling while retaining exact method/type/argument checks. No
generator behavior changed in response.

Final no-autocorrect RuboCop: **five owned Ruby files, no offenses**.
`git diff --check` for all Rust paths passed. Ruby syntax checks passed for
all new/changed spec/runner files. Final frozen metadata hashes remain unchanged.
Known quick commands entered only declared environments; no Cargo acceptance,
installed-artifact smoke or full release build was executed. All commands exited.

One initial tools-only style invocation excluded Ruby defaults from GEM_PATH and
therefore failed materializing default `rexml`/`racc`. Repeating it read-only with
`GEM_PATH=<own-root-.gems>:$(ruby -e 'puts Gem.default_dir')` restored the declared
root defaults; no dependency/source mutation or install occurred for that repair.

Final application inventory (nine R1-owned paths):

- `clients/rust/haveapi-rust-client.gemspec`
- `clients/rust/Gemfile.lock`
- `clients/rust/template/resources.rs.erb`
- `clients/rust/template/resource.rs.erb`
- `clients/rust/spec/unit/generator_spec.rb`
- `clients/rust/spec/unit/dependency_spec.rb`
- `clients/rust/spec/unit/name_lint_spec.rb`
- `clients/rust/spec/integration/run.rb`
- `clients/rust/docs/releasing.md`

Shared `flake.nix` prerequisite remains implementer0-owned; shared retained-gem
inspection/smoke remains implementer2-owned. No Git operation by implementer3.
The untracked `clients/rust/.bundle-user` directory is only this package's earlier
metadata cache, preserved and excluded from the path inventory; do not stage it.
New setup uses the already ignored `.gems/bundler-user` directory.

## Shared acceptance and remaining work

Implementer2 owns granted retained-artifact inspection/smoke changes: verify the
retained gem's exact runtime Fiddle requirement, activate it before loading the
generator, and reject default-gem or version mismatch. No overlap edits by R1.
Root setup is separate and completed under implementer0 ownership.

Lead confirmed the completed prose pass on `clients/rust/docs/releasing.md`.
Final approved document SHA-256:
`2d7168f0a0803515925e8d7b9f1ccfa9edb49adbbcb8be6b35dd917380798c60`.
All nine owned paths are yielded to implementer0 for a normal hooked commit;
the shared `flake.nix` libffi prerequisite has the same R1 logical purpose and
remains implementer0-owned. Source validation baseline/head remains `b64fb25`.

### Two logical commit boundaries

Lead requested this split before central commit. The complete final owned file
hash inventory is [r1-final-owned-sha256.txt](r1-final-owned-sha256.txt), rechecked
at unchanged head `b64fb25` after all quick checks and approved prose.

1. **Explicit Fiddle runtime dependency**: gemspec, component Gemfile.lock,
   `spec/unit/dependency_spec.rb`, and only the five-line Fiddle paragraph added
   after the packaged-runtime check in `docs/releasing.md` (final lines 30–34).
   Include implementer0's two shared `flake.nix` libffi additions with this
   logical purpose. Implementer2's corresponding retained-package dependency
   inspection/activation tests can follow or accompany it under their owner.
2. **Preserved generated resource naming**: both ERB templates,
   `spec/unit/generator_spec.rb`, `spec/unit/name_lint_spec.rb`, the integration
   runner's focused lint mode, and only the generated naming/lint paragraphs and
   command block in `docs/releasing.md` (final lines 62–84). This stream has no
   runtime/gemspec/lock change and does not rename any generated API identifier.

The single final documentation file contains both approved sections; stage its
two independent hunks in the corresponding central Git turns. No source or
index edits by implementer3 are needed for the split. Suggested subjects:
`clients/rust: declare the Fiddle runtime dependency` and
`clients/rust: scope lint allowances to generated resource names`.

Remaining: central hooked commit, final independent review, and post-review
generated-name/MSRV plus packaged-gem checks. No database,
protocol, source-interface, deployment or migration change. No integration or
publication permission supplied. Keep this session open.
