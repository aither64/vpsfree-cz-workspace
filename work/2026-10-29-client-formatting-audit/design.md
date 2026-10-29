# Client formatting implementation design

Status: accepted conversational plan, recorded for implementation on 2026-10-29.
Design owner: architect0. Application changes belong to the retained implementers.

## Scope and baseline

The user authorized implementation with “Implement the plan.” The earlier
read-only audit used HaveAPI `f6e5c3750c747b33ec869c54ca220bf6f1d9d2d0`.
Implementation starts at `ae46cf27a9afb6558d386c293cec7231dd6c423d` in
`worktrees/2026-10-29-client-formatting-audit/haveapi`.

Seven client directories are in scope: Ruby, Go, Rust, JavaScript, TypeScript,
Python and PHP. Retain all existing clients and generators. Elixir is excluded.
No ESLint, metrics tightening, broad Ruby reformatting, API renaming, new shared
formatter framework, release/version bump, downstream repository change or
deployment belongs to this work. Integration and publication remain separately
authorized actions.

The new baseline adds the example-source conventions in
`doc/client-examples.md#example-source-style` and routes renderer changes there
from AGENTS.md. Preserve those conventions, literal encoders, direct/custom
adapter behavior and formatter-free documentation rendering. This brief does
not authorize changing example renderers merely to match client formatting.

## Prettier policy and TypeScript generation

The user chose “whatever the formatter wants.” Use exactly **Prettier 3.9.10**
with its defaults: two-space indentation, double quotes, semicolons, width 80,
default trailing commas and arrow parentheses, and LF. One canonical JSON
configuration lives at
`clients/typescript/lib/haveapi/typescript_client/prettier.json`, containing
`{}` and a final newline. Authored JavaScript/TypeScript scripts explicitly use
that same file. Do not duplicate configuration or add plugins/style overrides.

Keep `Emitter.new(ir, config).files` pure and formatter-free. Add a small Ruby
formatter boundary in the TypeScript generator library. The generation pipeline
is:

1. Validate the destination and emit the existing source map.
2. Validate relative paths and UTF-8/LF source using the existing checks.
3. Format the map in a disposable temporary tree.
4. Read and validate the formatted map.
5. Hash those final bytes, construct the manifest, compare, and use the existing
   writer to install only when needed.

Select the executable with `PRETTIER` or `prettier` on PATH. The override is an
executable path, not a shell command. Require a successful `--version` response
equal to `3.9.10`. Invoke with argv through Open3, without a shell, using the
absolute packaged `--config`, `--no-editorconfig`, `--ignore-path` pointing to
Ruby's `File::NULL`, `--parser typescript`, `--write` and the literal `**/*.ts`
glob from the isolated temporary directory. Explicit ignore-path replaces
Prettier's default ignore files. These options exist in the tagged 3.9.10 CLI.
The temporary tree contains only validated emitted files; do not recursively
format a consumer directory.

Use one version probe and one formatting process per generation/check, not one
process per file. Do not add environment-isolation infrastructure or blanket
NODE_OPTIONS/NODE_PATH changes to production generation. Keep existing release
smoke environment isolation. The explicit config, ignore policy and temporary
input tree define canonical formatting.

Both `generate` and `generate --check` require the prepared formatter. Fetch,
help, library loading, pure emitter use, documentation adapters and HTML requests
do not. Never run npx, install dependencies or access the network during offline
generation. Missing executable, version mismatch, parse/format failure or invalid
formatted content must fail before touching the destination. Formatting must not
be moved into the emitter or invoked on API documentation requests.

### Ownership, provenance and existing trees

Retain ownership manifest **format 1**. Add formatter provenance with `name`,
`version` and `config_sha256`; output hashes describe formatted bytes. Include
the packaged JSON in `Generator.source_files` and its source digest. The existing
gemspec and release inspection `lib/**/*` globs already package and compare this
location; add regression coverage for it rather than another packaging mechanism.

Accept existing valid format-1 manifests lacking formatter provenance for normal
regeneration. Their `--check` result is stale, with no writes. Normal regeneration
replaces owned output and records formatter provenance. Do not require manual
manifest edits, an ownership-version bump or a migration flag. Preserve current
foreign-file and symlink refusals, stale-owned-file removal and unchanged-tree
timestamps.

Keep the current per-file atomic writer and manifest-last behavior. Formatting
failures preserve the destination; an interruption during installation retains
the existing mixed-tree recovery contract. Restore the committed generated tree
before retrying. For an interrupted first generation with no ownership manifest,
preserve the partial directory and regenerate into a fresh empty destination.
Rollback restores the matching generator revision, generated tree and manifest
together; do not claim an old generator's `--check` accepts newly formatted bytes.

## Tool preparation, source formatting and packaging

Add `prettier: "3.9.10"` to the existing JS development dependencies. Continue
using the ignored local JS package lock; do not add a second npm package/lock or
vendor node_modules into the Ruby gem. Locked nixpkgs
`3ec636362e1816bc2f0888fa0fa2c69f1bc9e504` already provides Prettier 3.9.10.
Supply it in the default and client-js shells and check parity with the exact npm
dependency and generator requirement. No flake-lock update is required.

Ruby gem consumers must prepare Node and `prettier@3.9.10` explicitly, exposing
the executable through PRETTIER or controlled PATH. RubyGems and the published
JS package's development dependencies do not install that consumer tool.
Prettier 3.9.10 declares Node >=14 and no runtime dependencies; retain the
repository's existing Node development/release toolchain.

Provide `npm run format` and `npm run format:check` for authored JS/TS sources,
tests and build scripts. Use explicit source scope, the canonical config and a
repository-owned ignore file. Exclude build/dist/node_modules and generated
`clients/js/src/haveapi/i18n_messages.js`. Do not format ERB templates directly.
Apply mechanical source formatting, then produce bundles/declarations through
the existing build commands. Generated artifacts remain build outputs under the
repository instructions.

### Version-string compatibility

Prettier changes `Client.Version` in authored source to double quotes. Update
the narrowly coupled metadata/version code:

- `Makefile` version substitutions for client.ts and the built JS bundle.
- `utils/release/artifacts.rb` JS source version matcher and browser-bundle
  version validation.
- Related fixtures/assertions in `utils/release/spec/release_spec.rb`.

Accept existing single-quoted and new double-quoted assignments while preserving
exact version equality. Source version updates emit double quotes. Test update
behavior on disposable fixtures; do not bump VERSION or run a release migration.
Preserve package-name, bundle identity and runtime version checks.

### Packaged generator and consumer verification

Record the actual Prettier version in release tool provenance; Node and the JS
dependency lock are already retained. The formatter Ruby code/config must work
from the extracted gem, with config identity included in the generator digest.
Extend package inspection tests for missing/changed config and source identity.

The extracted-gem smoke uses the prepared exact-version executable and the
EXTRACTED config, generates a fixture, runs `--check`, and compiles/exercises a
strict consumer against the existing supported published runtime 0.30.2. Do not
fall back to checkout configuration or module discovery. Prepare tools before
packaging/smoke through existing release-deps/Nix seams. Retained-artifact
verification in tools-only publication mode does not install or execute Prettier.
Keep the existing artifact restoration/publication recovery contracts.

## Other clients and common check entrypoints

PHP uses the existing pinned PHP-CS-Fixer with only `@PER-CS3x0 => true`.
Remove `@PHP82Migration`: its inherited octal_notation rule can emit PHP8.1-only
`0o` syntax when the formatter runs under PHP83. Explicit PER-CS3x0 preserves the
current pinned fixer's resolved PER policy without its moving alias. This is a
preventive compatibility adjustment, not a claim of an existing PHP8.0 failure.

Use the same config/fixer in CI and local checks. The dry-run command from root
is `php-cs-fixer fix --dry-run --diff --using-cache=no
--config=.php-cs-fixer.dist.php --path-mode=intersection clients/php`.
Explicitly exclude generated `clients/php/src/Client/I18nMessages.php` from
formatting unless generator conformance has been independently established.
No direct generated-catalog edits are allowed. Add configuration/hook/Nix trigger
coverage and a PHP8.0 syntax lane over shipped src PHP files plus bootstrap.php.
Retain PHP8.3/8.4 PHPUnit lanes: PHPUnit10 itself needs PHP >=8.1. Keep the library
requirement PHP >=8.0 and do not bypass platform requirements.

Ruby retains existing relaxed RuboCop rules. Use/document the ROOT Gemfile and
bundle consistently. Broaden workflow triggers for extensionless bin files,
Rakefiles, nested Gemfiles/component configs and the workflow itself. Existing
RuboCop covers Ruby generator source, not emitted-language formatting.

Go retains CLI `go fmt` and separate library `generate`/`go_fmt` operations.
Add narrow formatter-failure/CLI-failure and canonical generated-output coverage.
Go already writes before formatting; failure must be reported but does not gain
an atomic-output guarantee. Do not add naming changes or a linter overhaul.

Rust retains exact rustfmt version checking and existing runtime Clippy. Add
missing-executable and nonzero formatting-operation preservation tests where
absent; retain existing mismatch tests. Check actual generated fixture bytes
with rustfmt using the same edition/options, without requiring cargo compilation
for a formatting-only assertion. Preserve the copied runtime's identity.

Python retains existing exact Ruff, hook, Nix parity, typing and test setup.
It needs regression verification, not a new tool.

Add `make check-rust` for runtime `cargo fmt --all -- --check`, and
`make check-format` composing root-bundle RuboCop, npm format:check, PHP dry-run,
existing Ruff format --check and check-rust. Reuse these commands in applicable
CI/hooks and the local test-rust path. Keep Clippy, lint, compilation and tests
distinct from formatting. Add a required scoped JS format hook and retain the
existing Ruby/PHP/Python hooks. Align EditorConfig with JS/TS two spaces, Go tabs
and Rust/Python native indentation, leaving excluded-language policy alone.

## Ownership and implementation sequence

| Owner | Files and responsibility | Dependency |
| --- | --- | --- |
| implementer2 | clients/typescript formatter/config/generator/specs/docs; utils/release package/provenance/TS smoke/specs and release documentation | Publish the config/tool/manifest contract first; owns shared release-file edits |
| implementer0 | clients/js authored source/scripts/ignore/docs and JS CI; Ruby workflow/root-invocation gaps; narrow Go tests/docs | Uses implementer2's canonical config; supplies JS quote-compatibility changes to release/shared-file owners |
| implementer3 | PHP fixer config, PHP CI/floor check and PHP docs | Independent once common dry-run command and catalog exclusion are fixed |
| implementer1 | Rust tests/local parity; flake.nix, Makefile, .overcommit.yml, JS hook, EditorConfig and development instructions | Sole owner of shared root edits; incorporates component commands and version-update changes |

Lead coordinates package release, application worktree access, checks and Git
operations. Serialize overlapping files and all Git handoffs in the shared
feature worktree. Implementer2 alone changes shared release files; implementer1
alone changes shared root files, including Makefile version substitutions.
Independent PHP, Ruby/Go and Rust work can proceed from this settled brief.
Shared final checks follow availability of the JS scripts and TS config/tool.
Material deviations return through the lead to architect0. Architect0 changes
this design only; lead owns plan/state and coordination commits.

## Acceptance and verification

Quick checks precede final review:

- Native formatting checks and focused Ruby/Go/Rust/TS specs pass with prepared
  repository tools. Run appropriate quick checks per package, then the aggregate.
- Real Prettier output is canonical and its hashes match the manifest. Repeat
  generation preserves bytes/timestamps. `--check` detects drift and missing
  output without touching destination files or parents.
- An old format-1 tree regenerates without manual edits; formatter failures,
  wrong/missing tools and invalid formatted content preserve existing output.
  Ambient Prettier/EditorConfig/ignore files do not change generated bytes.
- Writer-focused tests may stub the formatter boundary; retain real complete
  generation coverage. Pure emitter/documentation tests remain formatter-free.
- Version-update/extraction regressions accept old/new quotes and still reject
  wrong versions. Config inclusion/source identity and Nix/npm/tool parity pass.
- PHP8.0 parses shipped sources; formatter excludes owned catalogs. Existing
  ownership, literal encoding, type and protocol expectations remain intact.

After all intended changes are committed and quick checks pass, lead assigns
reviewer0 under mandatory-change-review for the complete branch/diff/history,
manifest compatibility, version coupling, packaging and generated ownership.
This design record itself is planning evidence, not an automatic earlier review.

After review, run bounded integration/release batches with fresh verification
watchers where required: JS build/compatibility/async/type tests; generated TS
consumer/wire tests; affected Go/Rust integration and Rust feature/Clippy checks;
PHP PHPUnit; existing Python regression; and one clean build-only retained-gem,
npm and extracted-TS smoke batch. Use existing commands, reuse valid evidence,
and investigate failures before retrying. Update documentation assertions only
when affected; do not add broad benchmarks or unrelated renderer rewrites.

## Compatibility, delivery and recovery limits

No database schema, persisted application data, wire protocol, public API,
Terraform behavior, NixOS configuration or runtime deployment ordering changes.
Generated source/manifest bytes intentionally change. Node and exact Prettier
become generation-time requirements; consumer execution of already-generated
clients needs neither formatter nor Ruby generator. Mixed old/new generated
clients retain the same API behavior. No coordinated machine update is required.

Operator action is limited to preparing the generator tool and regenerating
owned output with the recorded schema/revision. Preserve source/input/tool
identities and the existing interrupted-install recovery path. Publication,
default-branch integration, deployment, kernel/system builds and session lifecycle
actions are outside this implementation authorization.
