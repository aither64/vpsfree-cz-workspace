# Development and regeneration

`src/lib.rs`, package files, examples and tests are handwritten.
`src/generated/**` is owned by the HaveAPI Rust generator, including the runtime
copied from `clients/rust/runtime/src/runtime/**`. Fix maintained HaveAPI source
and regenerate when generated behavior needs a change. A runtime fix in HaveAPI
reaches crate consumers only after regeneration and a new client release.

## Tools

Enter the committed Nix environment with `nix develop`. The client retains its
own pinned nixpkgs revision:
`fe13242281a67641c0102cdb1087f0ebe586c7df`. Generation requires the exact formatter
output `rustfmt 1.9.0` recorded in `generator.toml`, using edition 2024.
The pinned compiler is newer than the separate Rust 1.95 minimum.

The crate depends on reqwest, Serde, serde_json and url. The optional `blocking`
feature enables reqwest's blocking transport. Tokio is a development/example
dependency. Keep `Cargo.lock` local and ignored for this library; applications
that use the crate keep their own locks. In a fresh checkout, run
`cargo generate-lockfile` once in the pinned shell, then use `--locked` for
verification. Retain that lock with the verification evidence. CI resolves
dependencies once per run and passes the same lock to every compiler, package
and publishing job, using its artifact ID and SHA-256. Keep `flake.lock` tracked.
Cargo may include a resolved lock in the `.crate` archive.

## Saved schema

`schema/api-7.0.json` is a canonical sanitized snapshot of an unauthenticated
OPTIONS request to the explicit production API 7.0 endpoint. It retains paths,
wire names, validators, namespaces, nullability and authentication discovery.
The sanitizer removes prose, examples, validator messages and protected defaults.
The canonical digest covers sorted JSON object keys, two-space indentation,
LF newlines and a terminal newline. Arrays keep their order.

`schema/provenance.json` records the capture profile, acquisition time,
canonical digest, sanitizer diagnostics, generator revision, runtime digest and
toolchain. `schema/inventory.json` describes the captured resources, actions and
parameters. Plugin completeness is unknown. These files describe one public
surface; they do not combine metadata from different credentials or replace it
with an administrator's local description.

Refreshing the capture is an explicit maintenance action. Use the generator's
`fetch` command with API version `7.0` and profile `public-live-api-7.0`, review
the sanitized result and its inventory, then update provenance and regenerate.
Keep raw HTTP captures outside the repository. Never save authentication
headers, cookies, credentials, login responses or transient tokens.

## Offline generation

Obtain the exact HaveAPI 0.30.1 source revision recorded in provenance:
`1c3c98f0d77e0b23c8da1a8937f25c5799864a3b`. Use a clean, separate checkout.
HaveAPI does not track the generator's Ruby lock in Git. Restore the original
release input from the official manifest before installing dependencies.
`tools/prepare-generator-lock` accepts a local manifest and verifies its recorded
SHA-256, source, version and Ruby lock digest. It writes only the ignored
`clients/rust/Gemfile.lock`, accepts identical existing bytes and rejects a
conflict or symlink. It does not fetch or resolve dependencies.

The generator and Ruby dependencies are development tools, not crate runtime
dependencies. The generator uses Fiddle for atomic directory exchange. The Nix
shell supplies libffi to build its native extension. From this repository,
enter `nix develop` and prepare a separate Ruby 3.3 bundle frozen to that lock:

```sh
export HAVEAPI_SOURCE=/path/to/recorded/haveapi
mkdir -p target
curl --fail --location --proto '=https' --tlsv1.2 \
  https://github.com/vpsfreecz/haveapi/releases/download/v0.30.1/release-manifest.json \
  --output "$PWD/target/haveapi-release-manifest.json"
tools/prepare-generator-lock "$PWD/target/haveapi-release-manifest.json"
export GEM_HOME="$PWD/target/generator-gems"
export GEM_PATH="$GEM_HOME:$(ruby -e 'puts Gem.default_dir')"
export PATH="$GEM_HOME/bin:$PATH"
export BUNDLE_GEMFILE="$HAVEAPI_SOURCE/clients/rust/Gemfile"
export BUNDLE_PATH="$PWD/target/generator-bundle"
export BUNDLE_USER_HOME="$PWD/target/bundler-user"
export BUNDLE_APP_CONFIG="$PWD/target/bundler-config"
export BUNDLE_FROZEN=true
gem install --no-document bundler --version 4.0.23
bundle install
bundle check
tools/regenerate
tools/regenerate --check
```

Keep the recorded HaveAPI checkout and its lockfile unchanged. Do not reuse its
Ruby 3.4 native gems or write Bundler configuration into that checkout. Generation
uses this crate's exact `rustfmt 1.9.0`; the HaveAPI development formatter may be
newer and must not replace it.

Generation reads the saved snapshot without contacting the API. `--check` is
read-only and reports drift. Regeneration replaces only `src/generated`; it
preserves handwritten package files. Review manifest requirements when the
generator changes. Commit generated refreshes separately from handwritten
changes. Compare source/runtime digests and update provenance for each refresh.

## Verification

Known quick checks are `cargo fmt --all -- --check`, `bash -n tools/regenerate`,
`tools/check-provenance`, and deterministic `tools/regenerate --check` once the
generator is available. The provenance check compares snapshot, inventory and
generated digests with the retained record. Run the offline helper integrity
cases with `python3 -B tools/test-prepare-generator-lock.py`.

Compilation and acceptance commands are:

```sh
cargo test --locked --all-targets
cargo test --locked --all-targets --features blocking
cargo doc --locked --all-features --no-deps
cargo package --locked
```

Also verify the minimum supported compiler with Rust 1.95 and the same local
lockfile. CI runs offline-schema generation and the default/blocking matrices;
ordinary checks need no live API.

The real vpsAdmin acceptance test is ignored by default because it changes
disposable server state. Start HaveAPI's
`clients/rust/spec/integration/support/vpsadmin_server.rb` with an explicit
vpsAdmin fixture-source checkout, following that harness's instructions. It
owns its ephemeral listener and private database. Pass its readiness URL as
`VPSADMIN_TEST_BASE_URL` and its `VPSADMIN_FIXTURE_READY` JSON object as
`VPSADMIN_FIXTURE_JSON`. Set `VPSADMIN_REAL_INTEGRATION=1` to opt in, then run:

```sh
cargo test --locked --all-features --test real_vpsadmin -- --ignored --test-threads=1
```

The test accepts loopback HTTP URLs only, uses the fixture's local Basic
credentials, and exercises async/blocking VPS show and info update, pagination,
nullable DNS TTL, Custom JSON and token actions. Do not point it at production.
Stop the fixture through its owning harness when verification ends.

## Compatibility and release checks

API version 7.0 selects the generated contract. Crate SemVer versions the Rust
interface, including copied common types. A compatible server may add fields;
older clients tolerate unknown output fields. Removed actions, changed public
types, newly required inputs or a different API target need a breaking crate
version. During 0.x this means a new minor version. Document MSRV changes.

Before an authorized release, review the schema/provenance, regenerate, run the
verification matrix and package check, and update `CHANGELOG.md`. Inspect
`cargo package --list --locked` so the package contains the generated runtime
and has no HaveAPI path or Git dependency. Publishing to crates.io is a separate
explicit action through the manual workflow described below.

No server deployment, database migration or coordinated node update is needed.
Old and new client versions can coexist while the server offers their API
versions. Consumers can recover by pinning an older crate and lockfile. Rolling
back a client cannot undo server actions it already submitted.

## Publishing from GitHub Actions

Run `release.yml` manually against a tag matching
`v<Cargo.toml package.version>`. The workflow publishes `vpsadmin-client` from
this repository after the normal CI matrix passes for that commit. It checks
that the tag still points to the verified commit before publishing. Publication
runs execute one at a time; branch pushes and pull requests do not publish.
The reusable verification workflow exposes the lock artifact ID and SHA-256.
The publishing job restores and verifies that lock before using it. Ordinary CI
retains a package artifact before protected-environment approval. After approval,
the publishing job uses `tools/publish-crate candidate` to run native
`cargo publish --dry-run --locked` without registry credentials. The helper
retains the exact native archive, input lock and source/tool identity. It uses
explicit build and target directories and accepts only the recorded Cargo
1.98.0 revision, whose publish archive remains in
`build-dir/package/tmp-crate`. This is a guarded Cargo implementation detail;
standalone `cargo package` uses a different output location.

The existing protected publish step supplies credentials only to
`tools/publish-crate publish`, which runs native `cargo publish --locked`.
Both modes capture the native archive synchronously before validating it. The
candidate is preserved separately, and the actual publish archive must match
its hash. A failed command retains its original bytes or an absence report and
native exit status; it does not establish that an upload occurred. The workflow
uploads reports even when a started helper fails. Hard runner loss can prevent
capture or artifact upload. Neither mode repacks an archive or substitutes the
ordinary CI package for the native publish archive.

Both `release.yml` and `ci.yml` must exist on the default branch and at the
tagged revision. GitHub cannot dispatch a workflow that exists only on a feature
branch. A repository administrator must create the `release` environment,
require reviewers and restrict deployments to the intended version tags.
Configure these protections and registry credentials before running a release.

### First publication

[crates.io trusted publishing](https://crates.io/docs/trusted-publishing)
requires an existing crate. For its first version, create a short-expiry API
token with the minimum available publish scope for `vpsadmin-client`. Store it
as the `release` environment secret `CARGO_PUBLISH_BOOTSTRAP_TOKEN`. No local
Cargo login is needed.

After reviewing and pushing the version tag, select bootstrap mode. Replace
`v0.1.0` with the tag matching the manifest:

```sh
gh workflow run release.yml --repo vpsfreecz/vpsadmin-rust-client \
  --ref v0.1.0 -f authentication=bootstrap
```

Bootstrap requires a missing crate (registry HTTP 404) and a configured token.
An existing crate, missing secret or failed registry lookup stops publication.
The token is supplied only to `cargo publish --locked` after verification.

### Subsequent publications

After the first upload, a crate owner must register a trusted publisher in
crates.io Settings → Trusted Publishing with owner `vpsfreecz`, repository
`vpsadmin-rust-client`, workflow `release.yml` and environment `release`.
Revoke the bootstrap token and delete its environment secret. Dispatch later
version tags using the default OIDC mode:

```sh
gh workflow run release.yml --repo vpsfreecz/vpsadmin-rust-client \
  --ref v0.1.1 -f authentication=oidc
```

The workflow obtains OIDC credentials after verification and toolchain setup,
then passes them only to the publish step. OIDC failure never falls back to an API token.
Package checks and dry runs do not prove that registry authentication or upload
works; those require the owner prerequisites and an authorized publication.

After upload, independently compare the exact registry version and original
archive checksum with the retained actual publish archive. Observe docs.rs
indexing separately. If an upload fails or the archives differ, preserve the
original artifacts and inspect registry state before retrying: a version may
have been accepted even if the workflow failed. Never move a release tag or
overwrite a published version. To stop future publication, disable the workflow
or remove its trusted publisher binding.
