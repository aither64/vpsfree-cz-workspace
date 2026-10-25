# Version-sensitive verification for HaveAPI 0.30.1

Accepted read-only findings, 2026-10-24. All 27 profile paths inspected matched
the retained inventory for `67fcd34ba506264a5c7ee2e8e18a88d221c6f469`, tree
`80804b1c0c3ed33fc4b086673dbc3618a789cd4f`. No profile-source correction or
routine test-fixture version rewrite was identified. Lead reports final review
of 67 passed; the required longer source checks remain separate gates.

This note plans verification; it records no application execution. Owner0 owns
Git/backports/version edits after master integration proof. Owner1 owns qualified
dependency environments and lock rebinding. Lead owns prose, review and execution
grants. No publication, tag or source change is authorized by this note.

## Minimum real 0.30.1 acceptance

Run after actual patch version preparation and committed candidate review, using
the patch worktree `worktrees/2026-10-22-haveapi-release/haveapi-0-30-1`.
Never substitute the unchanged profiles worktree or stub version constants.

**Rust:** use the existing session
`client-example-profiles-rust-mount/probe.rb` through owner1's separately bound
combined-bundle launcher, with:

```text
HAVEAPI_RUST_MOUNT_MODE=version-subset
HAVEAPI_RUST_MOUNT_EXPECTED_VERSION=0.30.1
HAVEAPI_REPO_ROOT=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-22-haveapi-release/haveapi-0-30-1
```

Also supply the retained exact inert `HAVEAPI_RUST_MOUNT_FORMATTER_VERSION`, a
fresh absolute session evidence directory in `HAVEAPI_RUST_MOUNT_EVIDENCE`, and
the newly qualified patch-bound `BUNDLE_GEMFILE`. The existing subset checks:

- Actual loaded `haveapi`, `haveapi-client`, `haveapi-rust-client` gem versions
  and paths, plus server/Rust version constants, against 0.30.1.
- No profile/no optional adapter load; minimal profiles at `/` and
  `/mounted/api/` through real registration and mount, with omitted generator
  version and nil SDK version.
- Both real Rust renderers, authorized HTML and actual base URL; valid
  versionless `cargo add` instructions; no internal origin or fabricated version.
- Explicit matching generator version and rejected mismatch.

No probe fixture change is needed solely for 0.30.1. Complete the full
[Rust mount matrix](client-example-profiles-rust-mount-brief.md) before integration
of the pre-version source; do not repeat its whole privacy/Git/legacy/failure
matrix merely for metadata.

**Go:** run `clients/go/spec/documentation_profile_check.rb` through the owning
patch-bound `clients/go/spec/documentation.Gemfile` closure. It already exercises
real mounted minimal configuration, nil SDK version/`@latest`, explicit loaded
generator version, saved-description legacy control, and authorized rendering.
Add only session-driver assertions that all three loaded specs (`haveapi`,
`haveapi-client`, `haveapi-go-client`) equal 0.30.1 and come from this patch
worktree, and that `HaveAPI::VERSION`/`HaveAPI::GoClient::VERSION` equal 0.30.1.
Require the checker, call `GoDocumentationProfileCheck.run!`, then assert that
`GoDocumentationProfileFixture.server(generator_version: '0.30.0')` raises
`HaveAPI::ClientExample::Profiles::Invalid` with a version-mismatch message.
The checker's standalone invocation is guarded by `$0 == __FILE__`.

Do not replace this with `documentation_acceptance.rb --check-environment`:
that preflight uses an explicit version and saved description. Neither minimum
version check requires generation, a compiler, a listener or network access.

## What `make version` changes

The current target changes these **18 paths**, with 0.30.1 as its input:

| Paths | Operation |
| --- | --- |
| `VERSION` | Shared version. |
| `servers/ruby/lib/haveapi/version.rb`, `clients/ruby/lib/haveapi/client/version.rb`, `clients/go/lib/haveapi/go_client/version.rb`, `clients/rust/lib/haveapi/rust_client/version.rb` | Four version constants. |
| `clients/js/package.json`, `clients/js/package-lock.json`, `clients/js/src/haveapi/client.ts`, `clients/js/dist/haveapi-client.js` | Package/root-lock versions and client version marker. |
| `clients/php/composer.json`, `clients/php/src/Client.php` | PHP package/runtime version. |
| `clients/python/pyproject.toml`, `clients/python/uv.lock` | Package version and `uv lock`. |
| `servers/ruby/haveapi.gemspec`, `clients/go/haveapi-go-client.gemspec`, `clients/rust/haveapi-rust-client.gemspec` | Local Ruby-client requirement becomes `~> 0.30.1`. |
| `examples/servers/ruby/activerecord_auth/Gemfile` | Server requirement. |
| `clients/rust/Gemfile.lock` | `bundle lock --local` through the declared Rust bundle. |

It does not update CHANGELOG/date, documentation/specs, saved API snapshots,
API/protocol versions, independent SDK versions/configuration, Rust runtime
Cargo metadata/lock, other Ruby locks, or session acceptance manifests/locks.
Lead supplies the actual preparation date in CHANGELOG separately.

Normal JS build must reproduce the target's bundle version-marker change;
preserve dependency/declaration equivalence. Rust lock changes should be limited
to local client/generator versions, their dependency constraint and corresponding
PATH/CHECKSUMS identities. `utils/release/spec/release_spec.rb:147` already tests
a disposable 999.0.0 bump against the actual baseline with unchanged external
dependencies. Investigate any non-version lock/input drift rather than accepting
it as routine versioning.

## Owner1 lock and graph rebinding

| Lock | Version-sensitive local specs |
| --- | --- |
| Root `Gemfile.lock` | None; no version-only change. |
| `servers/ruby/Gemfile.lock` | `haveapi`, `haveapi-client`. |
| `clients/ruby/Gemfile.lock` | Local `haveapi-client` when prepared; this lock was absent in the inspected profiles worktree. |
| `clients/go/Gemfile.lock` | `haveapi-go-client`, `haveapi-client`. |
| `clients/go/spec/documentation.Gemfile.lock` | `haveapi`, `haveapi-go-client`, `haveapi-client`. |
| Tracked `clients/rust/Gemfile.lock` | `haveapi-rust-client`, `haveapi-client`; updated by the target. |
| Session combined Rust lock | `haveapi`, `haveapi-rust-client`, `haveapi-client`; new patch-bound manifest/input record required. |

The component locks other than Rust's are ignored, as is the Go acceptance
lock. Rebind their PATH/spec/CHECKSUMS identity entries and requirements to the
actual patch source before frozen activation. Preserve prior locks/receipts;
do not rewrite the profile gate's historical evidence. Relative paths must still
resolve to the owning patch worktree. The current combined Gemfile has absolute
profiles-worktree paths and must not be reused unchanged.

Keep the owning external graphs fixed: combined/server `mime-types-data
3.2026.1020`; component Rust `mime-types-data 3.2026.1013`; Fiddle `1.1.8` and
Tomlrb `2.0.5` unchanged. Preserve exact Ruby/Bundler/native-input qualification.
No mixing component gem homes or pretending version-changed lock bytes are
identical. Refresh digests/local-version records and prove external graph
equality while retaining the old input evidence. Owner1 supplies actual commands
and qualified patch environments; this note performs no setup.

## Preserve the pre-version model comparison

`clients/rust/spec/documentation/model_equivalence.rb` fixes its baseline at
4dc0 and permits only `generator_source_sha256` to differ. At 0.30.1,
`generator.rb:57–65` intentionally also changes ownership-manifest
`generator_version` and `ruby_dependency_lock_sha256`: the tracked Ruby lock
contains the new local versions. The unchanged comparator would reject these
legitimate release metadata differences.

**Do not rerun that 4dc0 comparison unchanged after versioning and do not relax
its comparator.** Complete it successfully on the pre-version source, then
retain its exact source/generated/runtime/schema/config/tool proof together with
the backport tree equality and enumerated metadata-only changes. A pending
pre-version result is not applicable success. The unit comparator stays intact.
Existing successful development/1.95 compiler evidence is prior applicable
evidence, not a freshly executed 0.30.1 campaign. Relevant code/input changes or
failures reopen affected checks and review.

## Fixture and packaging limits

Shared profile/mount specs derive fake generator versions from
`HaveAPI::VERSION`; the real Go checker uses the loaded generator version.
Independent fixture SDK versions (Rust 0.1.0, Go v1.2.3/v2.3.4), deliberate fake
0.29.0 compatibility/mismatch controls and self-contained mocked 0.30.0 registry
tests remain unchanged. None requires a release-version rewrite.

`doc/client-examples.md:115/120` explicitly illustrates legacy
`generator_version: '0.30.0'`; this is an explicit old-generator selection, not a
claim that it matches an installed 0.30.1 generator. `make version` does not
update it. Any lead-selected current-version example edit is an explicit
reviewed documentation change. The old artifact names in
`servers/ruby/spec/client_examples/dynamic_acceptance.md` are illustrative;
execution uses the actual retained candidate artifact paths.

The release manifest captures nine locks: root, Ruby server, Ruby client, Go
client, Rust generator, Rust runtime Cargo, JS npm, PHP Composer and Python uv.
It excludes Go's documentation lock and the session combined lock; retain these
separately with mount evidence. Fresh packaging validates actual 0.30.1 source,
packages and locks. Rust artifact smoke derives its expected generator version
from `artifacts.version` and checks extracted code.

Keep the accepted proportional gates: fresh release-check/release-test, committed
full-range candidate review, one authoritative final-head build-only campaign,
and the real version-sensitive subset above. No duplicate full local/feature/tag
or MSRV campaign is added for identical relevant inputs. Preserve all original
artifact bytes and label old versus fresh evidence accurately.
