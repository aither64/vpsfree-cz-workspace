# Rust HaveAPI generator and vpsAdmin client: proposed design

Status: planning complete; implementation has not started. Architect0 owns this
design. The lead accepted the bounded direction below. Material implementation
deviations return through the lead. Implementers and reviewer remain unassigned.

The client targets an **explicit API version**. Package SemVer is independent;
no other vpsAdmin version belongs in generation inputs or the support contract.

## Recommendation and scope

Add a Ruby generator under `haveapi/clients/rust/`, a shared Rust runtime crate
in that directory, and a separate `vpsadmin-rust-client` repository containing a
generated, typed client. Retain Ruby/ERB for generation, as the Go generator
already does. Rust users consume ordinary crates and need neither Ruby nor a
running API at build time.

The first implementation supports HaveAPI protocol major 2, one selected API
version per generated crate, async calls using Tokio/reqwest, typed action
builders, JSON bodies, query parameters, response/error envelopes, metadata,
partial associations, Basic authentication, existing HaveAPI/OAuth2 tokens, and
explicit generated token request/challenge/renew/revoke actions. Start the
vpsAdmin client with API `7.0`, subject to capturing and validating that exact
description before implementation acceptance.

V1 has no blocking facade, automatic retries, background token refresh,
interactive login callbacks, browser OAuth2/PKCE/WebAuthn orchestration, automatic
pagination, or automatic ActionState polling. Generated pagination parameters
and ActionState actions remain callable. A successful action submission does
not imply its asynchronous server operation has completed.

No server behavior, database, daemon protocol, configuration, existing Go client,
CLI, or Terraform provider change is required. A server-side complete-schema
export and richer parameter descriptions are possible later work, not v1
dependencies or implied assignments.

Alternatives considered:

| Alternative | Assessment |
| --- | --- |
| Embed the runtime in every generated client, as Go does | Avoids a dependency, but duplicates fixes and requires regenerating every client for transport/security changes. Prefer a shared crate. |
| Write the generator in Rust | Reasonable later; adds schema acquisition and tooling work without improving the generated API. Keep Ruby initially. |
| Discover the API at runtime | Loses the requested compile-time, version-specific API. Do not mix dynamic discovery into normal client calls. |
| Generate closed enums and complete associated resource structs everywhere | Metadata and permission filtering do not justify those guarantees. Use conservative representations in v1. |

## Evidence and limits of investigation

Inspected canonical bare repository HEADs with `git show`, `git ls-tree`, and
`git grep`; no other session's worktrees were used. These revisions identify
source evidence, not client/server support requirements. No live production
schema was fetched and no build, test, or deployment was run.

| Repository | Inspected revision | Relevant evidence |
| --- | --- | --- |
| HaveAPI | `1e475d2e39f0b33a009a5e17c9aac3439da0c546` | `doc/{protocol,create-client,typed-input-validation}.md`; `clients/go/README.md`; `clients/go/lib/haveapi/go_client/{generator,api_version,action,input_output,parameter}.rb`; `clients/go/template/{request,action,types,authentication/token,authentication/oauth2}.go.erb` |
| vpsadmin-go-client | `45a5170b7190a520c6cef3d4cd4ef86ca0fa43c1` | `README.md`, `AGENTS.md`, `go.mod`, `client/resource_vps_action_show.go`, recent history and tag inventory |
| vpsAdmin | `b4ef8535a629ee8c9cd753afecdb05e0895d0eea` | `api/lib/vpsadmin/api.rb`; `api/lib/vpsadmin/api/authentication/token_config.rb`; `api/lib/vpsadmin/api/action_state.rb`; `api/lib/vpsadmin/api/resources/{vps,dns_record,debug,dns_record_log,ip_release_campaign}.rb` |

Concrete implications:

- The Go generator uses Ruby `HaveAPI::Client::Communicator` and ERB. Its
  `--version` selects a description; omitting it selects the current default.
  Runtime code is copied into the generated output. Keep the useful model,
  without making the Rust generator depend on Go-specific IR/classes.
- The Go client README documents regeneration from the live default. No tags,
  checked-in description JSON, or GitHub workflows were found in the inspected
  canonical repository. The proposed Rust reproducibility/release process is
  new work, not an existing workflow claimed to have been verified.
- vpsAdmin declares `HaveAPI.implicit_version = '7.0'`; the Go client's VPS show
  path is `/v7.0/vpses/{vps_id}`. This supports choosing API 7.0, but does not
  establish the full schema/profile to publish.
- HaveAPI `servers/ruby/lib/haveapi/parameters/typed.rb` describes `required`
  and `nullable` from input validation; output formatting can still return null.
  `params.rb` and `action.rb` filter descriptions and actual outputs by
  authorization. A required output field is therefore not a safe Rust guarantee.
- `model_adapters/active_record.rb` returns unresolved associations as ID/label
  maps; expanded associations have additional fields. Unauthorized associations
  may contain only `_meta: { resolved: false, authorized: false }`.
- `action.rb` merges single-object metadata into response-level metadata, while
  object-list items carry their own `_meta`. `path_params` can be omitted when
  IDs are hidden. Metadata placement must follow observed wire shapes.
- `Custom` appears in real vpsAdmin inputs and outputs. The Go parameter factory
  drops unsupported parameter handlers, except its special `includes` handler.
  Rust must represent Custom explicitly and fail on unknown types, not drop them.
- `authentication/chain.rb`, `server.rb`, and token provider code describe auth
  resources separately. Globally mounted auth paths need not start with the
  chosen `/v7.0/` prefix. Validate them as described same-origin paths, rather
  than mechanically prefixing every URL.
- vpsAdmin's token configuration has TOTP and password-reset steps. Actual code
  uses `complete = false` for continuation; the protocol prose has an inverted
  sentence. Use code-backed fixtures for this flow.

Primary Rust references checked during planning:

- [reqwest Client](https://docs.rs/reqwest/latest/reqwest/struct.Client.html)
  documents reusable, cloneable pooled clients;
  [reqwest overview](https://docs.rs/reqwest/latest/reqwest/) documents Tokio
  async operation and redirect defaults. Configure redirects explicitly.
- [Serde field attributes](https://serde.rs/field-attrs.html) provide rename,
  defaults, conditional omission, custom deserialization, and flattened extra
  fields. These are mechanisms, not a substitute for protocol null semantics.
- [Cargo dependency locations](https://doc.rust-lang.org/cargo/reference/specifying-dependencies.html)
  distinguish local path/git development from published registry dependencies.
  [Cargo SemVer guidance](https://doc.rust-lang.org/cargo/reference/semver.html)
  supports non-exhaustive public types from their first release.
- [Cargo rust-version](https://doc.rust-lang.org/cargo/reference/rust-version.html)
  defines the minimum-supported compiler declaration;
  [rustfmt](https://github.com/rust-lang/rustfmt) documents formatting and checks.
  Select exact dependency/toolchain versions in P0, not from remembered versions.

## Repository and interface boundaries

Proposed layout (names are recommendations, availability is not yet checked):

```text
haveapi/clients/rust/
  bin/haveapi-rust-client
  Gemfile, Rakefile, haveapi-rust-client.gemspec
  lib/haveapi/rust_client/{cli,snapshot,ir,naming,generator,...}.rb
  template/                       # Rust sources, not copied transport code
  spec/{unit,integration}/
  spec/fixtures/                  # synthetic protocol/schema cases
  runtime/                       # crate haveapi-client
    Cargo.toml, Cargo.lock, src/, tests/
  README.md, docs/{design,generation,releasing}.md

vpsadmin-rust-client/
  Cargo.toml, Cargo.lock, flake.nix, flake.lock
  src/lib.rs                     # small handwritten facade/re-exports
  src/generated/                 # generator-owned tree
  schema/api-7.0.json             # reviewed, sanitized version description
  schema/provenance.json         # schema digest, profile, generator/toolchain
  generator.toml, tools/regenerate
  tests/, examples/, README.md, CHANGELOG.md
  .github/workflows/ci.yml
```

Generator gem name: `haveapi-rust-client`; runtime crate: `haveapi-client`;
generated crate: `vpsadmin-client`, in repository `vpsadmin-rust-client`.
Resolve name availability and license/package metadata before creating or
publishing anything. There is no repository-creation or publication action in
this planning assignment.

The generator owns schema acquisition/validation, a language-neutral-enough
internal model, names, source rendering, and generated-file ownership. The
runtime owns HTTP, credentials, URL/query construction, common wire types, and
envelope errors. The generated client owns exact paths/methods/namespaces, input
validation rules, per-action types, auth descriptions, and resource methods.
The runtime must contain no vpsAdmin resource names.

P0 freezes a small interface before runtime/generator work proceeds in parallel:

```text
ActionSpec: action name, method, path template, input/output layout and namespace,
            metadata namespace, no-output distinction
RequestParts: named path values, serialized input, global/object input metadata
Client::execute<T, M>(&self, spec, request) -> Result<Response<T, M>, Error>
Response<T, M>: typed output, typed/global metadata, HTTP status
Input<T>: Unset | Null | Value(T)       # internal/generated field representation
Association: map + described ID/label keys + optional object metadata
```

This is an interface brief, not finished Rust signatures. Generated builders
validate before execution; runtime encoding must preserve those validated states.
Expose generated input/output types through stable modules, with Serde renames
for wire names. Builders avoid exhaustive input struct literals; output structs
and error enums are non-exhaustive from the outset. Resource handles borrow the
client; output values own their data and never perform hidden network calls.

Proposed usage, to become a compiling example during implementation:

```rust
use std::time::Duration;
use vpsadmin_client::Client;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let api = Client::builder("https://api.vpsfree.cz")
        .token(std::env::var("VPSADMIN_TOKEN")?)
        .timeout(Duration::from_secs(30))
        .build()?;

    let vps = api.vps().show(123).send().await?.output;
    println!("{}", vps.hostname.as_deref().unwrap_or("<not returned>"));

    // Only hostname is sent; other update fields remain omitted.
    api.vps().update(123).hostname("example").send().await?;
    Ok(())
}
```

The generated crate exports `API_VERSION` and `SCHEMA_SHA256`; the client has no
runtime version selector. Null-capable fields also get explicit setters such as
`cpu_limit_null()`; setters such as `cpu_limit(value)` send a value.

## Types and protocol invariants

| Metadata/wire concept | V1 Rust representation/policy |
| --- | --- |
| String, Text | `String`; keep validator choices as documented strings, not closed enums |
| Integer | `i64`; report overflow rather than truncate |
| Float | `f64`; reject NaN/infinities locally before serialization |
| Boolean | `bool` |
| Datetime | String-based wire value with local input validation for the documented ISO forms; no forced public chrono/time type in v1 |
| Resource input | Validated nonnegative numeric resource ID for the documented v1 contract; no resource-specific ID newtypes inferred from names |
| Resource output | `Association` preserving the received map and described ID/label keys; optional metadata; no required Show action dependency |
| Custom | `serde_json::Value`; no invented schema for arbitrary JSON |
| Unknown type/layout | Generation failure identifying the action/parameter; never silent omission |
| Object/hash output | Per-action output struct |
| Object-list/hash-list output | `Vec` of per-action output structs, retaining item metadata where present |
| Ordinary output field | `Option<T>` even if description says required; absent and null deliberately collapse to `None` in v1 |
| New response fields | Ignore safely or retain in a flattened extra map; do not reject additive fields |

All input fields begin unset. A setter sends its value, including `false`, `0`,
and an empty string; a null setter sends JSON null and exists only where the
snapshot explicitly allows null. Required inputs are checked before dispatch.
Server defaults stay server-side: never populate an omitted field automatically.
Missing legacy nullable metadata means no explicit clearing guarantee. A direct
low-level input still receives the same validation, including Custom null.
Do not rely on nested `Option` serialization to implement three input states.

Use JSON for described POST/PUT/PATCH actions and bracketed query parameters for
GET/DELETE, matching the existing protocol/server behavior. Preserve input and
metadata namespaces separately. Query null uses the documented empty-string
encoding; omitted fields do not appear. This encoding cannot distinguish all
empty/null values on nullable parameters, so document that limitation. Scalars
are supported; arbitrary nested Custom query values and list-layout query input
must fail clearly until a tested encoding contract exists. JSON list layouts
remain supported. For includes, the observed comma-separated string is enough
for v1; do not invent arbitrary JSON-in-query conventions.

Metadata includes ordinary typed fields plus Custom JSON. Preserve global
metadata and per-item metadata, including count, resolved/authorized markers,
path parameters, and action-state IDs when present. No metadata field is
universally required. A user explicitly supplies nested resource path arguments;
do not infer missing IDs from partial associated objects. Path placeholders are
strings with ergonomic numeric conversions, encoded as individual URL segments;
their types cannot be inferred reliably from placeholder names.

Require a valid envelope status and the declared response namespace/layout on
success; optional *fields* must not make missing/corrupt envelopes look successful.
No-output actions have a distinct `()` decoding path. Type mismatches remain
decode errors. Characterize absent/false namespaces against fixtures in P0:
the current server's output wrapping has edge cases, so v1 must either support
the proven shape explicitly or reject that schema, not guess unwrapping rules.

Datetime input validation must cover date-only, timezone offsets, shortened
times, fractional seconds, and calendar validity from HaveAPI's documented
grammar. A parser that accepts only RFC3339 is insufficient. Strictly typed
Rust setters need not expose every coercion accepted by Ruby. Non-numeric custom
resource primary keys lack enough portable metadata and remain a documented
limitation; do not promise generic ID typing that the description cannot provide.

## Transport, authentication, and errors

Use a reusable reqwest client with Tokio, JSON/Serde, and a selected TLS feature
set. Builder configuration provides timeout, user agent, TLS roots, and proxy
options as needed. Do not accept an opaque preconfigured HTTP client in v1 if
its redirect policy cannot be enforced. The runtime can remain concrete rather
than introducing a general pluggable transport trait initially.

Runtime invariants:

- Every API action path is validated as a same-origin path; reject absolute
  action URLs, authority-relative URLs, credentials in URLs, and traversal.
  Combine base mount paths according to captured fixtures without double-prefixing
  server-described paths. Encode path data rather than interpolate raw strings.
- Disable automatic redirects, including for metadata acquisition. Credentials
  never follow redirects to another origin. Unsupported redirects are errors.
- No automatic retry of mutations, token requests, or challenge steps. A timeout
  may follow server execution; report uncertainty rather than replay a request.
- Set `Accept: application/json`; JSON bodies also set Content-Type. Apply
  connect/request deadlines and a documented response-size limit.
- Credential holders and protected fields have redacted Debug output. Do not
  log request/response bodies or credential headers by default. Error Display
  excludes raw bodies/URLs that may contain secrets; explicit raw diagnostic
  access, if provided, is clearly separate and must not leak through Debug.

Authentication scope:

| Method | V1 behavior |
| --- | --- |
| Basic | Explicit username/password; no MFA promise |
| Existing HaveAPI token | Send only in the metadata-declared token header |
| Existing OAuth2 token | Send using described OAuth2 header; no assumption that all HaveAPI implementations use identical headers |
| Token login | Generated typed request action; explicit required credentials/lifetime; no automatic login or invented policy defaults |
| Token continuation | Generate described actions, including vpsAdmin TOTP and reset_password; caller supplies challenge input/token and decides whether to continue |
| Token renew/revoke | Explicit actions; no background worker and no logout in Drop |
| OAuth2 acquisition/refresh/revocation helpers, browser/WebAuthn flows | Deferred; existing OAuth2 token usage is supported |
| Unknown auth provider | Clearly reported unsupported provider; other supported methods remain usable |

For token responses, provide a small checked conversion into complete versus
challenge state: complete requires a usable final token; continuation requires
its transient token and next-action name. A transient token is never installed
as general client authentication. Unknown next actions produce an actionable
unsupported-step result; never guess a URL. Explicit step calls avoid recursive
callback loops and permit arbitrary described steps without owning interaction.

Return `Result<Response<T, M>, Error>`. Distinguish local input/encoding errors,
transport/timeouts, non-JSON HTTP failures, malformed envelopes, typed decode
errors, and HaveAPI failures. Retain HTTP status, server message, and structured
parameter errors. Parse an available failure envelope even for non-2xx status;
`status:false` is an error even on HTTP 200, and non-2xx cannot become success
solely because a body claims `status:true`.

## Explicit version and reproducible generation

Separate acquisition from offline rendering. Proposed commands:

```text
haveapi-rust-client fetch URL --api-version 7.0 --output schema/api-7.0.json
haveapi-rust-client generate --schema schema/api-7.0.json --api-version 7.0 \
  --config generator.toml --output src/generated
haveapi-rust-client generate ... --check
```

Missing `--api-version` is an error, including acquisition. Fetch the explicit
version endpoint, preserve protocol version, and verify returned version help
and action paths against the requested version; global auth paths are the
documented exception. Fail on unsupported protocol major, unavailable API
version, mismatched snapshot/version, or malformed response. Do not fall back
to `default`, unversioned endpoints, or another snapshot. Allow known protocol
minor extensions only if their types/layouts remain understood.

At compile time, only actions in the snapshot exist; using an absent action is
a Rust compile error. At runtime, calls continue using that exact version's
paths; an old/unsupported server returns a structured HTTP/API error. Optional
explicit version probing may be added later, but is not implicit per-request
discovery or proof of full schema compatibility. A fixed API version can gain
actions and fields; the schema digest identifies the exact generated surface.

Snapshots must be reviewed publishable descriptions, not raw HTTP sessions:

- Preserve structural metadata, public auth discovery, header names, token
  action schemas, required/nullable flags, namespaces, paths, validators, and
  selected API version. Do not delete the entire authentication subtree.
- Never persist auth headers/cookies, request credentials, transient tokens,
  credential-bearing URLs, or actual login/action responses. Use environment/
  stdin-based acquisition credentials, not password command arguments.
- Exclude examples and arbitrary free text from the generation snapshot by
  default, or explicitly review them before inclusion. Public descriptions and
  defaults are not inherently secret-free: protected defaults must be removed
  with a recorded diagnostic; inspect remaining values before publication.
- Preserve public auth endpoints; reject credential/query-bearing endpoint
  URLs and record any deliberate sanitization in a separate deterministic
  manifest. Avoid broad deletion by words such as `token`, which are valid
  schema names. V1 need not call deferred external OAuth endpoints.
- Record a non-secret capture profile label and explicitly distinguish
  authenticated/unauthenticated acquisition. Permission-filtered descriptions
  cannot prove completeness. Do not union unrelated users' schemas or claim
  coverage of missing resources/parameters. Prefer an agreed controlled fixture
  profile; authenticated metadata may still be partial.

Generation provenance includes API version, protocol version, canonical schema
SHA-256, capture/profile and plugin coverage declarations where known, generator
version/revision, generator options, runtime compatibility requirement, Ruby
dependency lock, and exact Rust/rustfmt toolchain. Acquisition timestamp belongs
outside reproducible generated source. vpsAdmin support is defined by the API
version and described surface, not another version label.

Sort maps/names deterministically, preserve meaningful array order, normalize
newlines, and exclude timestamps/absolute local paths. Use deterministic naming
and escaping; detect reserved-word/name/file collisions before writing. Fail
with original schema paths rather than silently rename differently by traversal
order. Reject path escapes and source injection from metadata strings/comments.

Pin rustfmt and edition through the repository's Nix toolchain and explicit
configuration; regeneration must reject a mismatching formatter version rather
than accept arbitrary local output. If a rust-toolchain file is added, it must
match that pin. Generate into a temporary tree, compare, then replace only the
owned generated tree; refuse symlinks/out-of-scope destinations. Remove obsolete
owned files, preserve handwritten files, and make `--check` read-only. Repeated
generation and reordered JSON-object input must produce identical files.

## Package versioning, compatibility, and release

The Ruby generator follows HaveAPI's existing shared release/version mechanism.
The Rust runtime and vpsAdmin generated crate use independent SemVer because
their public Rust interfaces have separate compatibility boundaries. The
initial package versions are chosen at implementation/release time; they do not
encode API 7.0. Record the supported API version prominently in crate docs and
constants. A change to the generated API target is an explicit compatibility
decision and, where it breaks consumers, a breaking package release.

Additive output fields and unknown validator choice values should remain usable
by older clients. Adding required inputs, removing/renaming methods or changing
public types requires a breaking package version; during 0.x that means a new
minor. New optional fields can use compatible releases with non-exhaustive
types/builders. MSRV changes are deliberate and documented, never accidental
patch updates. P0 selects and verifies `rust-version`; CI checks that minimum
and the pinned generation toolchain.

Generated crates declare a compatible runtime version requirement and provenance
records the exact runtime tested. Local development may use an explicit path
override. Registry publication requires the runtime dependency to be available
there first. Do not publish a crate whose manifest relies solely on a local
path or unpublished Git dependency. Do not hand-edit generated Rust to repair
an API refresh; change the generator/config/snapshot and regenerate.

Publication order, when separately authorized: runtime crate, generator gem
with its compatible runtime contract, then the generated vpsAdmin crate. Add
explicit opt-in release tasks; do not unexpectedly extend a broad existing
publish command to publish new Rust packages. Keep generated refresh commits
separate from handwritten fixes and record schema/generator changes in release
notes. Do not assume or create a scheduled live-schema update process.

There is no persisted server state or schema migration, no Nix option change,
and no fleet/node coordination. Old/new clients can coexist against supported
API versions. Package consumers roll forward independently. Recovery is to pin
the prior crate version/lockfile and retained snapshot/generated revision;
this cannot undo server-side actions already executed. A bad generation is
recreated from retained inputs, not repaired by modifying generated files.

## Prioritized implementation packages

These are proposed packages for later assignment, not current delegation.
The lead owns scheduling, repository setup, plan/state, Git coordination, and
acceptance. Architect0 retains design ownership. Serialize shared-file changes
and Git/index operations inside the HaveAPI worktree.

Packages include authoring their tests and running known quick local checks.
Long or uncertain acceptance runs are deferred until the completed deliverable
is committed, quick checks pass, and independent final review is complete.
This includes generated-fixture compilation and HaveAPI test-server execution;
their placement in a package below identifies ownership, not earlier execution.

| Priority/package | Proposed execution lane and file boundary | Dependencies | Acceptance and checks |
| --- | --- | --- | --- |
| P0: contract and fixtures | Architect resolves questions with lead; future implementers agree `clients/rust/docs/design.md` contract and fixture ownership | Implementation authorization | Freeze ActionSpec/RequestParts/Response/Input/Association interfaces, initial API/profile, names, MSRV/toolchain, namespace/path edge behavior; minimal fixture captures auth/global paths, nulls, partial output and metadata |
| P1: runtime | Implementer0: `clients/rust/runtime/**`, runtime-specific docs/tests | P0 | HTTP and encoding match fixtures; omission/null/zero/false distinct; typed errors; redirects blocked; credentials redacted; no retries; focused unit/mock-server tests, fmt and clippy |
| P1: generator | Implementer1: `clients/rust/{bin,lib,template,spec}/**`, gem manifest/Gemfile/Rakefile, generation docs | P0; can proceed alongside runtime using agreed interface | Explicit-version fetch/offline generate/check; stable names/escaping and safe output ownership; all supported fields emitted; unsupported constructs diagnosed; Ruby unit specs/RuboCop and golden generated fixtures |
| P2: cross-component protocol integration | Implementer1 owns `clients/rust/spec/integration/**`; implementer0 fixes runtime only | Both P1 lanes | Author fixtures for auth challenge chain, all layouts, metadata, failure envelopes and partial associations; quick deterministic regeneration/deletion checks; generated-fixture compilation and HaveAPI test-server execution run after final review |
| P2: generated vpsAdmin crate | Implementer0: new `vpsadmin-rust-client/**` after lead authorizes setup | P1 contracts; agreed reviewed API 7.0 snapshot | Full selected snapshot generates without dropped fields; author realistic example and VPS show/update, nullable DNS TTL and Custom JSON fixtures; longer compilation/acceptance runs follow final review; ordinary CI needs no live API |
| P3: tooling/release/docs | Implementer1: HaveAPI `flake.nix`, `Makefile`, root documentation links and `.github/workflows/clients-rust-*.yml`; implementer0 owns corresponding new-client files | P2 | Pinned Rust/Ruby environment; source and generated CI; check/dry-run packaging; documented regeneration and API support; new publication remains explicit |
| Final gates | Lead selects retained reviewer only when implementation is complete | Committed final deliverable and quick checks | Independent whole-branch/history review, then watcher-run longer integration; lead accepts exact evidence; no merge/publication implied |

Required implementation test matrix:

1. No parameters; required/optional/nullable input; default omission; empty string,
   zero and false; bad float/datetime; signed integer limits and numeric resource ID.
2. Named namespaces and supported no-namespace cases; JSON object/list layouts;
   GET/DELETE query scalars/null; unsupported nested Custom query fails locally.
3. Nested resources, repeated placeholders, encoded path segments, base paths,
   metadata namespaces, global auth paths, reserved names and malicious metadata.
4. Successful and failed envelopes on both 2xx/non-2xx; empty/non-JSON/malformed
   bodies; missing namespace; missing/null fields; wrong field types; extra fields.
5. Basic, existing token/OAuth2 headers, request/TOTP/reset-password continuation,
   unknown challenge, token renew/revoke; no credential leakage on redirects/logs.
6. Partial/expanded/unauthorized associations; omitted path metadata; counts,
   includes, object-list metadata and action-state references.
7. Explicit version absent/unavailable/mismatched; protocol major rejection;
   filtered/incomplete snapshot coverage report; no silent default fallback.
8. Offline repeated generation, shuffled object keys, pinned formatter, source
   escaping, stale-file removal confined to owned tree, read-only `--check`.

Quick commands will be documented in the new `client-rust` Nix shell: generator
unit specs/RuboCop, `cargo fmt --check`, focused runtime unit tests, and generated
tree `--check`. Compilation/clippy duration must be measured, not assumed quick.
Full generated-crate compilation, test-server integration, MSRV matrix, and
package verification are longer/uncertain checks run through the required fresh
verification watcher only after all intended changes are committed, quick local
checks pass, and independent final review is complete. No
large vpsAdminOS cluster is necessary for the first client. A gated, read-only
live smoke test is supplemental and never the reproducibility gate.

## Remaining choices and acceptance of this plan

Resolve in P0 rather than expanding this investigation:

- Confirm the intended API 7.0 metadata profile and plugin coverage, and the
  controlled acquisition source. Missing permissions cannot be reconstructed.
- Confirm crate names/registry availability, license metadata, exact dependencies,
  TLS backend, minimum compiler and formatter pin.
- Characterize output namespace=false/no-output and mounted-base-path behavior;
  define explicit generation errors for unsupported shapes.
- Finalize resource-ID limits and datetime parser against canonical fixtures;
  preserve the conservative public types above.
- Decide whether public descriptive text is retained after review or excluded
  from initial snapshots; do not alter structural auth discovery to sanitize it.

The planning deliverable is complete when the lead accepts these boundaries,
the version-only contract, explicit limitations, interface split, and proposed
verification gates. This document makes no claim that code exists, that a schema
has been captured, that tests passed, or that packages are ready to use.
