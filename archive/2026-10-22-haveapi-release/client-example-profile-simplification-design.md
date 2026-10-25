# Proposed simplification of generated-client documentation profiles

Design only, 2026-10-24. This responds to the user's request to remove unnecessary
server settings. No application changes, tests, builds, probes, Git operations
or release actions were performed. The current behavior remains documented in
[vpsadmin-client-examples-configuration-design.md](vpsadmin-client-examples-configuration-design.md).
This proposal changes the original [profile contract](api-doc-contract.md) for the forthcoming implementation package after lead acceptance of this brief. HaveAPI 0.30.1/default integration remain held.

## Recommendation and direct answers

- Make `generator_version` optional, defaulting to `HaveAPI::VERSION`.
  Still verify that the installed optional generator gem matches that value.
- Make `module_version` and `crate_version` optional. Omission means resolution
  by the user's package manager at installation time, never by the API server.
- Use the server's complete selected-version description by default. No JSON
  file, schema capture, network fetch or duplication is needed for an SDK that
  matches the current API.
- Replace the required Rust TOML file with inline `crate_name` and optional
  `crate_version`. Add one optional `source: {git:, rev:}` setting for
  unpublished Git-distributed crates.
- Keep the existing file-based forms as explicit overrides for an older or
  deliberately restricted SDK. They remain supported, but are not the normal
  setup. This preserves the already published API without adding a new registry
  or fallback framework.

`description_path` is the generator's machine-readable API shape, not HTML.
`snapshot_path` is the Rust version of that data, with capture/version metadata.
They were required to reconstruct the exact names/types of an independently
generated SDK. The server already owns the declarations, so requiring those
files for a matching SDK is unnecessary.

`generator_config_path` currently points to six Rust TOML fields: crate name,
crate version, license, edition, minimum compiler and formatter version.
Only the first two affect documentation imports/dependency text. Rust IR itself
does not read that config. The remaining four belong to generating/packaging
the SDK, not serving its examples.

## Proposed public interface

```ruby
# Inside vpsAdmin's existing api/config/api.rb configure block:
VpsAdmin::API.configure do |api|
  api.documentation_clients('7.0',
    go: {
      import_path: 'github.com/vpsfreecz/vpsadmin-go-client/client'
    },
    rust: {
      crate_name: 'vpsadmin-client',
      source: {
        git: 'https://github.com/vpsfreecz/vpsadmin-rust-client',
        rev: 'ff876abe17e3301da62c1b6afbda055ec89db9d2'
      }
    }
  )
end
```

This is proposed syntax, not supported at 090a/4dc0 today. No Go version must
be discovered merely to configure examples. The Rust source identifies the actual
unpublished SDK; its manifest still declares 0.1.0, but the API need not repeat
it. For a published crate, omit `source`. Normal configuration requires only
package identity, with no versions or files.

| Field | Proposed rule |
| --- | --- |
| `go.import_path` | Required; retain existing validation and explicit source alias `client`. |
| `go.module_version` | Optional; omitted means `go get IMPORT@latest`. Explicit values retain existing validation and `@VERSION` output. |
| `rust.crate_name` | Required in inline form; reuse generator package-name validation and existing import-name logic. |
| `rust.crate_version` | Optional; omitted means `cargo add CRATE` for registry source. Explicit values retain existing validation and Cargo requirement semantics. |
| `generator_version` in either profile | Optional; omitted means server `HaveAPI::VERSION`, not SDK version. Explicit value must equal the installed generator VERSION. It cannot select/download another gem or weaken schema checks. |
| `go.description_path` | Optional exact-SDK override; existing absolute local JSON contract retained. Omitted means current server description. |
| `rust.snapshot_path` | Optional exact-SDK override; existing snapshot/version validation retained. Omitted means current server description. |
| `rust.generator_config_path` | Legacy alternative to inline crate fields; mutually exclusive with them. Continue validating full existing TOML. It may accompany either schema source; no silent precedence. |
| `rust.source` | Optional exact hash `{git: HTTPS_URL, rev: FULL_40_HEX_SHA}`. Absent means registry installation. When present, Git/rev selects the source; an explicit version additionally constrains its package. No branch, tag, path, credentials, command text or custom registry support. |

Existing exact-key legacy configurations keep working. Unknown fields,
conflicting identity forms, invalid values, missing optional gems and actual
generator-version mismatches remain startup errors. A compatible explicitly
pinned older generator is a legitimate override use, especially with an exact
SDK snapshot; if it lacks the new factory interface, automatic mode must reject
it rather than falling back. No profile still hides the language everywhere.

For Git source, render git and rev, version only when supplied (or read from
legacy TOML), plus `features = ["blocking"]` for blocking. Validate an absolute HTTPS URL
without userinfo/query/fragment/control characters and escape each TOML value.
Never fetch it on the API server. This is installation metadata, independent
of the API schema. Registry/source conflicts are configuration errors, not a
reason to print a nonworking installation hint.

### Version omission and installation text

Represent an omitted version as nil, never the literal string `latest`, an empty
string, a fake 0.0.0 or a value copied from HaveAPI. Reject explicit empty/invalid
strings. Legacy TOML keeps its explicit version. Neither Go's `ApiVersion` nor
Rust's `IR` needs the package version; current requirements come from adapter/profile
validation/storage and install-text rendering. Actual generated package
manifests retain their version; only the documentation configuration changes.

For omitted registry versions, render these valid instructions:

```text
// go get github.com/vpsfreecz/vpsadmin-go-client/client@latest

// Async Rust registry example, only for an actually published crate:
// cargo add vpsadmin-client
// cargo add tokio --features macros,rt-multi-thread
// cargo add serde_json

// Blocking registry example:
// cargo add vpsadmin-client --features blocking
// cargo add serde_json
```

Cargo selects its normal latest-compatible release under its resolver, manifest
and toolchain rules; never emit `version = "latest"`. Go resolves `@latest` by
its normal rules. Existing manifests and lockfiles still apply. Explicit Go
versions select that version; explicit Cargo versions retain existing version
requirement semantics rather than silently introducing an exact `=` pin.

For the real unpublished Rust profile, use this instead of a registry command:

```toml
# Cargo.toml
vpsadmin-client = { git = "https://github.com/vpsfreecz/vpsadmin-rust-client", rev = "ff876abe17e3301da62c1b6afbda055ec89db9d2" }
# Blocking variant adds features = ["blocking"].
```

Keep separate Tokio/serde_json instructions. Git/rev pins source even when its
package version is omitted. These are user installation commands; the server
never executes them. Latest selection can change over time and is less
reproducible; explicit versions remain available where that matters.

`Profile#package_version` becomes nil-or-String, copying/freezing only present
strings. The overview prints identity and a version only when present; it must
not display `nil` or claim a resolved registry version. No additional source
reader is needed for this label. Go adapter's keyword becomes
`module_version: nil`; Rust documentation's `crate_version: nil` is independent
of the generator's still-required manifest version. The registry validates
omitted fields separately from malformed supplied fields.

## Lifecycle and canonical naming

At registration, `Server#mount` has not set its root or assembled routes.
Authentication resources also do not exist until `auth_chain.setup`.
Therefore deriving schema during `documentation_clients(...)` is too early.

Use two bounded initialization stages in the existing per-server Profiles object:

1. Registration validates identity/source/version settings and loads optional
   adapter code. Preserve early validation/loading for supplied legacy files.
   Start of mount checks selected API versions and closes registration.
2. At the end of mount, after auth setup, every version's routes and post-mount
   hooks, bind automatic profiles once to the completed server. Capture only
   versions that have an automatic profile, once per version, then construct
   and freeze the adapters. Startup completes only after this succeeds.

No process-global cache, request-time initialization, file rereads or network
acquisition is needed. Nothing is initialized when Go/Rust are unconfigured.
Rebuilding a Server instance rebuilds its models. Runtime mutation of mounted
DSL resources is not a new supported schema-refresh mechanism.

The source is the existing
`describe_version(Context.new(server, version:, user: nil, endpoint: false,
doc: true))` declaration path. In `Action.describe`, nil user/nonendpoint
skips executing authorization rules and endpoint `prepare`; it describes the
complete mounted surface. Pre-authorization hooks still run to assemble blocks,
and provider description methods run: this is declaration processing, not an
authenticated request. Do not invent an administrator user, authenticate a
request or execute actions. If an application's description hook cannot run
without a request, report the configuration failure; do not fetch its HTTP API.

Do not build models from a request's filtered `@help`. Go's
`Resource.allocate_member_names` assigns collision suffixes across siblings;
Rust IR checks naming scopes and derives parent arguments from complete parent
routes. Omitting hidden actions/resources can otherwise produce different names
or argument lists for different users.

Retain a private copied structural description for naming/types. Remove example
payloads/prose and parameter defaults from that internal copy at their known
structural positions; preserve parameter names, wire types, layouts, validators,
auth routes and associations. Do not recursively delete arbitrary same-named
keys inside Custom JSON or validator data. Neither private schema nor its
diagnostics may become visible HTML/JSON. No new authorization-bypass context
mode or public all-fields description endpoint is needed.

Keep the existing request-local context unchanged: its description, action,
sample and credentials remain the current user's authorized values. Adapters
use private IR only for resolution and compatibility checking. Hidden fields
must not appear as setters, output accesses, defaults, samples or error text.
Current auth/schema filtering must remain intact, including sequential users
and locale changes.

## Minimal generator seams

Go already accepts a pure in-memory description:
`Documentation.new(description:, import_path:, module_version:)` uses
`ApiVersion.new`. Feed it the complete copied server description; retain
its existing `resolve`/`render` interface and capability checks.

For Rust add a pure documentation factory:

```ruby
Documentation.from_description(
  description:, api_version:, protocol_version:, mount_path:,
  crate_name:, crate_version: nil, source: nil
)
```

Add `Documentation.from_snapshot(snapshot:, crate_name:, crate_version: nil,
source: nil)` for an optional exact snapshot with inline identity. The
`from_description` factory builds its internal snapshot, then delegates there.
Keep the legacy `new(snapshot:, config:)` form callable with its existing full
validation. Both factories return the same resolve/render adapter interface.

Reuse `Snapshot.from_description`, `IR` and `Naming`. The existing snapshot
validator requires a source URL although current documentation naming does not
need a hostname. The factory can use an internal
`https://haveapi.invalid<MOUNT>v<VERSION>/` structural URL and profile label
`server-documentation`, never exposed, persisted as SDK provenance, fetched or
used in emitted requests. The real mount/version come from the server;
`HaveAPI::PROTOCOL_VERSION` supplies protocol metadata. Rendered request URLs
continue to come from the actual request context.

Decouple documentation construction from `Generator.new`'s packaging config.
Factor the existing pure package-name/version validation and
`rust_type`/`meta_parameters` helpers into a generator-owned small model
module `HaveAPI::RustClient::Model` in
`clients/rust/lib/haveapi/rust_client/model.rb`, shared by Generator and
Documentation. Keep the existing helper method names; centralize package
validation there with a caller-controlled required-version check. Construct IR directly for docs;
do not fill in fake license/MSRV/formatter settings or relax actual generation
validation. The legacy `new(snapshot:, config:)` constructor still validates
its full config and delegates to the same documentation model. Add the optional
source metadata there too. No generated runtime, names, format or compiler
requirements change as a consequence. The shared validator checks a supplied
version; Generator still requires one, while Documentation permits omission.

An unsupported full model still fails initialization as it does with a saved
profile. A particular unsupported sample still returns the existing limitation
result. Do not prune failing actions to force successful IR construction or
silently omit unsupported input.

## Compatibility tradeoff

Automatic mode means **the configured SDK is expected to match the current
server's generation contract**. It does not prove that a package with the
configured name/version was generated from it. Without SDK input metadata,
the server cannot detect a missing newer action or a name changed by a new
collision in an older SDK. Do not claim otherwise or replace evidence with a
best-effort naming table.

Most unrelated additions are harmless, but names, required inputs, types and
nested binding changes need actual SDK compile/run checks. Document this
assumption beside configuration instructions. The explicit saved-description
override has a concrete use: older or subset SDKs can continue showing verified
matching actions and limitations for absent/stale ones. Retaining those existing
fields is sufficient; no hashes/version registry/auto-discovery are added.

For vpsAdmin, this removes the need to recover an old Go description merely
to try automatic examples. It does not prove that cached Go 1d9240 matches
today's API. Rust ff876abe has a known public-only snapshot; until its surface
is checked against the intended server, the already available optional snapshot
override is an honest choice. No SDK regeneration or publication is implied.

The optional generator gems remain necessary for canonical naming. This changes
HaveAPI code first; vpsAdmin's inspected 0.29 API bundle still needs an explicit
upgrade before either old or proposed profiles work. Changes to actual vpsAdmin
configuration, dependency installation, deployment, releases and current holds
are separate scope. No DB/protocol/persisted-state migration is involved.
Old profiles work on new HaveAPI; new inline profiles require new code, so
rollback also reverts that config. Mixed API workers may display different
examples, without changing wire requests or stored data.

## Implementation packages after lead acceptance

Lead has directed isolated preparation from immutable
`4dc0f7e11c494d1a0dc852dabcc312411699fcab`, worktree name
`haveapi-client-example-profiles`, branch
`2026-10-24-haveapi-client-example-profiles`. Owner0 owns Git and preparation;
application edits wait for the lead to accept this exact brief. No further user
permission loop is needed for these compatible implementation choices.

- **implementer0 — shared server and Git:** `documentation_clients.rb`,
  `server.rb`, a private structural-copy helper only if needed, profile/mount
  and authorization/HTML specs, `views/version_page.erb` for optional version
  display, `servers/ruby/doc/client-examples.md`, shared
  fixture/test wiring. No new tab/highlighter/variant work is needed.
- **implementer2 — Go:** Go documentation unit/acceptance fixtures and any narrow
  adapter changes required for the automatic description. Own Go-only specs;
  canonical naming/generation behavior remains unchanged.
- **implementer3 — Rust:** documentation factory/source rendering, shared pure
  model helper and extraction from `generator.rb`, Rust unit/acceptance specs.
  Preserve generated outputs exactly; no SDK runtime/template churn.
- **Lead:** final user explanation, scope acceptance and independent review.
  vpsAdmin configuration remains a subsequent isolated package; do not overlap
  the current dependency verification or frozen release patch.

Quick gates: omitted/default/explicit generator and SDK versions; nil internal
versions and valid latest-compatible Go/Cargo commands; Git source precedence; legacy profiles
unchanged; source/config rejection; no-profile absence/no generator load;
deferred initialization sees plugin/auth/action-state routes and final mounts;
one model per selected server version; no requests/processes/files generated;
canonical collision/ancestor results; two users with different fields/actions
and locales; no hidden samples/defaults; source-literal/HTML escaping; current
sample limitations preserved. Test failed mount remains unusable and does not
publish a partial profile set.

Pass quick checks and commit all intended source/docs before full-range final
independent review. Then run existing documentation/packaged-server gates,
Go rendered compile/run checks, Rust async/blocking rendered compile/run and
generation-determinism checks. Exercise actual mounted routes, authentication,
nested paths, payload/meta/null/omission behavior against disposable fixtures.
Prove refactoring shared Rust helpers leaves generated fixture output unchanged;
reuse prior MSRV evidence only where input equivalence warrants it, otherwise
run the affected 1.95 check. Keep real installed SDK checks distinct from freshly
generated fixture checks. Longer work uses the normal fresh watcher.

No unresolved architecture choice blocks this brief. Actual server/SDK
compatibility remains an acceptance check when a vpsAdmin patch is requested;
no Go version lookup is required by the optional-version configuration. Lead
accepts the implementation boundary and assigns the packages. The architect
does not edit application code or launch verification.

## Source evidence

Inspected source at 090a188cb4ef3477324718627f4ae3415d1c0975; relevant server/Go/Rust
library files compare unchanged at 4dc0f7e11c494d1a0dc852dabcc312411699fcab.

- [Profile keys and current loaders](https://github.com/vpsfreecz/haveapi/blob/090a188cb4ef3477324718627f4ae3415d1c0975/servers/ruby/lib/haveapi/documentation_clients.rb).
- [Mount and description lifecycle](https://github.com/vpsfreecz/haveapi/blob/090a188cb4ef3477324718627f4ae3415d1c0975/servers/ruby/lib/haveapi/server.rb):
  context254, mount442, auth setup610, version mounts618–623,
  describe_version893. [Action authorization/description](https://github.com/vpsfreecz/haveapi/blob/090a188cb4ef3477324718627f4ae3415d1c0975/servers/ruby/lib/haveapi/action.rb#L213).
- [Go canonical allocator](https://github.com/vpsfreecz/haveapi/blob/090a188cb4ef3477324718627f4ae3415d1c0975/clients/go/lib/haveapi/go_client/resource.rb),
  [Rust IR](https://github.com/vpsfreecz/haveapi/blob/090a188cb4ef3477324718627f4ae3415d1c0975/clients/rust/lib/haveapi/rust_client/ir.rb).
- [Rust config validation and pure helpers](https://github.com/vpsfreecz/haveapi/blob/090a188cb4ef3477324718627f4ae3415d1c0975/clients/rust/lib/haveapi/rust_client/generator.rb),
  [documentation dependencies](https://github.com/vpsfreecz/haveapi/blob/090a188cb4ef3477324718627f4ae3415d1c0975/clients/rust/lib/haveapi/rust_client/documentation.rb#L71),
  [snapshot construction](https://github.com/vpsfreecz/haveapi/blob/090a188cb4ef3477324718627f4ae3415d1c0975/clients/rust/lib/haveapi/rust_client/snapshot.rb#L84).
- Actual vpsAdmin/SDK revisions, TOML and source permalinks remain in the
  [current-behavior investigation](vpsadmin-client-examples-configuration-design.md).

