# Rust HaveAPI generator and vpsAdmin client: implementation design

Status: implementation authorized; P0 shared contract FROZEN revision 1,
with numbered clarifications 2 through 7 below.
Architect0 owns this design. Ruby/ERB generation, embedded runtime source,
async default and optional reqwest blocking support are accepted. Material
contract changes require a numbered clarification through the lead. Four source
owners may begin against the following contract. The rationale below explains
the same boundaries; contract revisions remain architect-owned.

The client targets an **explicit API version**. Package SemVer is independent;
no other vpsAdmin version belongs in generation inputs or the support contract.

## FROZEN revision 1: shared implementation contract

This section is the implementation boundary, effective immediately. Signatures
below specify types and visibility; omitted method bodies are implementation
work. Helpers and private storage may vary without changing this contract.

### Owners and source-copy boundary

- Implementer0 exclusively owns `clients/rust/runtime/**`, including its docs
  and private Cargo test harness.
- Implementer1 owns Ruby/ERB `clients/rust/{bin,lib,template}/**`, generator
  unit specs/fixtures and shared spec setup, gem/build files, generator docs,
  HaveAPI flake/Makefile/CI. It owns the sanitizer and snapshot format.
- Implementer2 exclusively owns `clients/rust/spec/integration/**`, including
  protocol fixture launcher and test-only server extensions. Generic HaveAPI
  fixture profile is explicit API `1.0`; vpsAdmin behavior fixtures use `7.0`.
  Extensions stay here and do not modify production schema or server behavior.
- Implementer3 exclusively owns the existing `vpsadmin-rust-client` repository,
  including its authoritative capture, saved snapshot, provenance, examples,
  package/CI files and generated tree. Lead serializes Git operations.

Maintain runtime modules under `clients/rust/runtime/src/runtime/**`. The private
harness `src/lib.rs` contains `pub mod runtime; pub use runtime::*;`. Copy that
runtime directory byte-for-byte to generated `src/generated/runtime/**`.
Generated `src/generated/mod.rs` declares `pub mod runtime;` and generated
resource/client modules. The handwritten client `src/lib.rs` contains
`mod generated; pub use generated::*;`. Runtime internal paths use
`crate::runtime`, valid in both harness and generated crate. Do not copy the
harness manifest/tests or add a published runtime dependency.

### Core types and protocol functions

All these names are exported from `runtime`; `JsonMap` means
`serde_json::Map<String, serde_json::Value>`. Ordinary generated outputs and
public error enums are non-exhaustive. Sensitive values never derive Debug.

```rust
pub type JsonMap = serde_json::Map<String, serde_json::Value>;
pub type ValidationErrors = std::collections::BTreeMap<String, Vec<String>>;
pub enum InputValue<T> { Unset, Null, Value(T) }
pub type Input<T> = InputValue<T>;
pub trait Validate { fn validate(&self) -> Result<(), Error>; }
pub enum Method { Get, Delete, Post, Put, Patch }
pub enum Layout { Object, ObjectList, Hash, HashList }
pub enum ParameterKind { String, Text, Integer, Float, Boolean, Datetime, Resource, Custom }
pub enum RequestAuth { Configured, None }
pub struct ParameterSpec {
    pub name: &'static str,
    pub kind: ParameterKind,
    pub required: bool,
    pub nullable: bool,
    pub protected: bool,
}
pub struct InputSpec {
    pub layout: Layout,
    pub namespace: Option<&'static str>,
    pub parameters: &'static [ParameterSpec],
}
pub struct OutputSpec {
    pub layout: Layout,
    pub namespace: &'static str,
    pub allow_empty_response: bool,
}
pub struct ActionSpec {
    pub name: &'static str,
    pub method: Method,
    pub path: &'static str,
    pub input: Option<InputSpec>,
    pub output: Option<OutputSpec>,
    pub meta_namespace: Option<&'static str>,
    pub global_meta: &'static [ParameterSpec],
    pub object_meta: &'static [ParameterSpec],
    pub auth: RequestAuth,
}
pub struct ApiSpec {
    pub api_version: &'static str,
    pub protocol_major: u16,
    pub schema_sha256: &'static str,
    pub basic_auth: bool,
    pub token_header: Option<&'static str>,
    pub oauth2_header: Option<&'static str>,
}
pub struct RequestParts {
    pub path_params: std::collections::BTreeMap<String, String>,
    pub input: Option<serde_json::Value>,
    pub global_meta: Option<JsonMap>,
    pub object_meta: Option<JsonMap>,
}
pub struct PreparedRequest {
    pub method: Method,
    pub url: url::Url,
    pub headers: reqwest::header::HeaderMap,
    pub body: Option<Vec<u8>>,
}
pub struct RawResponse { pub status: u16, pub body: Vec<u8> }
pub struct Response<T, M> { pub output: T, pub meta: M, pub http_status: u16 }
pub fn prepare(config: &ClientConfig, spec: &ActionSpec, parts: RequestParts)
    -> Result<PreparedRequest, Error>;
pub fn decode<T: serde::de::DeserializeOwned, M: serde::de::DeserializeOwned>(
    spec: &ActionSpec, response: RawResponse,
) -> Result<Response<T, M>, Error>;
```

`InputValue` defaults to Unset and provides `is_unset(&self) -> bool`; generated
Serde fields skip Unset, serialize Null as null, and preserve zero/false/empty.
GET encodes input/metadata in the query; DELETE/POST/PUT/PATCH encode a JSON
object body through the same preparation path (clarification 5).
`Validate` runs BEFORE serialization (especially for nonfinite floats); runtime
`prepare` enforces required/null/type rules again on serialized input/metadata.
Implement `Validate` for generated unique action input structs, `()` and
`Vec<T: Validate>`. Input absence uses `ActionSpec.input=None`, not an invented
namespace. All output fields are `Option<T>`. Generated output item structs
capture `_meta` as `Option<JsonMap>`; response metadata has an action-specific
all-optional struct plus flattened extras. Missing response metadata becomes
an empty object. Associations use a transparent JSON map wrapper named
`Association` with `as_map(&self) -> &JsonMap`; described ID/label key names
remain in schema/field documentation, without assuming a complete Show model.

Input `namespace=false` normalizes to None and is supported for object/hash.
Metadata `namespace=false` also normalizes to None. Unnamespaced list input is
rejected. Ordinary output namespace=false is a generation error: current server
wraps it under JSON key `"false"`; do not infer flattened output. True no-output
uses `output=None`, `T=()`, and requires a valid success envelope with empty
response object. Named empty schemas follow clarification 2 below.
No implicit success on empty HTTP204. Single-object metadata is response-level;
list item metadata remains on each item. Per-item input metadata is deferred.

Paths in ActionSpec are safe mount-relative templates without a leading slash,
for example `v7.0/vpses/{vps_id}` or `_auth/...`. The snapshot records the capture
mount; generator strips it once. Client base URL denotes the server mount root,
not a version root. Preserve its mount when joining paths. Placeholder values
are strings encoded as single segments; numeric conveniences use ToString.
Reject traversal, authority/absolute action URLs, escaping the mount, fragments
and credential-bearing URLs. Never infer numeric IDs from placeholder names.

### Client, execution modes and generated builders

```rust
pub trait Mode: private::Sealed {}
pub struct AsyncTransport { /* private */ }
#[cfg(feature = "blocking")]
pub struct BlockingTransport { /* private */ }
pub struct Client<C: Mode> { /* private */ }
pub struct ClientConfig { /* private; common immutable config */ }
pub struct ClientBuilder<C: Mode> { /* private */ }
impl<C: Mode> ClientBuilder<C> {
    pub fn new(base: impl AsRef<str>, api: &'static ApiSpec) -> Self;
    pub fn basic_auth(self, username: impl Into<String>, password: impl Into<String>) -> Self;
    pub fn token(self, token: impl Into<String>) -> Self;
    pub fn oauth2_token(self, token: impl Into<String>) -> Self;
    pub fn timeout(self, timeout: std::time::Duration) -> Self;
    pub fn connect_timeout(self, timeout: std::time::Duration) -> Self;
    pub fn max_response_bytes(self, bytes: usize) -> Self;
    pub fn user_agent(self, value: impl Into<String>) -> Self;
}
impl ClientBuilder<AsyncTransport> { pub fn build(self) -> Result<Client<AsyncTransport>, Error>; }
#[cfg(feature = "blocking")]
impl ClientBuilder<BlockingTransport> { pub fn build(self) -> Result<Client<BlockingTransport>, Error>; }
impl AsyncTransport {
    pub fn new(config: &ClientConfig) -> Result<Self, Error>;
    pub async fn execute(&self, request: PreparedRequest) -> Result<RawResponse, Error>;
}
#[cfg(feature = "blocking")]
impl BlockingTransport {
    pub fn new(config: &ClientConfig) -> Result<Self, Error>;
    pub fn execute(&self, request: PreparedRequest) -> Result<RawResponse, Error>;
}
pub struct Request<'a, C: Mode, I, O, M> { /* private */ }
impl<'a, C: Mode, I, O, M> Request<'a, C, I, O, M> {
    pub fn new(client: &'a Client<C>, spec: &'static ActionSpec,
        path_params: std::collections::BTreeMap<String, String>, input: I) -> Self;
    pub fn input(self, input: I) -> Self;
    pub fn global_meta(self, meta: JsonMap) -> Self;
    pub fn object_meta(self, meta: JsonMap) -> Self;
    pub(crate) fn input_mut(&mut self) -> &mut I;
}
impl<'a, I: serde::Serialize + Validate, O: serde::de::DeserializeOwned,
    M: serde::de::DeserializeOwned> Request<'a, AsyncTransport, I, O, M> {
    pub async fn send(self) -> Result<Response<O, M>, Error>;
}
#[cfg(feature = "blocking")]
impl<'a, I: serde::Serialize + Validate, O: serde::de::DeserializeOwned,
    M: serde::de::DeserializeOwned> Request<'a, BlockingTransport, I, O, M> {
    pub fn send(self) -> Result<Response<O, M>, Error>;
}
```

Mode is sealed and implemented for the two transports; no public pluggable
transport API. Both send implementations call the same validate/prepare/decode.
Runtime does not define `Client::builder`: generated code supplies it for each
concrete mode using `ClientBuilder::new(base, &API_SPEC)`. Generated root alias
is `pub type Client = runtime::Client<runtime::AsyncTransport>`; gated
`blocking::Client` aliases the blocking specialization. Generated resource
methods are inherent methods on `runtime::Client<C>` and borrow the client.
Both constructors use the same static API_SPEC. No runtime API-version setter.

Generate modules `resources::<snake_resource_path>::<snake_action>` containing
`Input`, `Output`, `Meta`, `SPEC`; nested resource paths join with double underscores,
and any name collision fails generation with both schema paths. Object/hash
Input is a unique struct even when empty; list input is `Vec<Input>`, list
output `Vec<Output>`. Each input field uses `InputValue<T>` and is public;
inputs implement Default. Generated setters are specialized inherent impls on
the corresponding `Request` instantiation, shared across C. `.hostname(value)`
sets Value; nullable fields also get `.hostname_null()`. Common `.input(...)`
supports list/replacement inputs. A resource action's path arguments appear in
template order, accept `impl ToString`, and populate the BTreeMap. Examples:
`api.vps().show(123)`, `api.vps().update(123).hostname("example")`.
Nested resource accessors take accumulated parent placeholders explicitly.

Builder validates URL/auth/header settings at build; only one auth mode may be
selected (conflicts error). Header names come exclusively from API_SPEC.
Existing tokens are sent verbatim using their described header, not an invented
Bearer prefix. Basic uses normal HTTP Basic. Unsupported/missing configured
provider errors at build. Ordinary actions use Configured even if auth is
optional; token request/challenge actions use None, renew/revoke Configured.
Defaults: request timeout 30s, connect timeout 10s, response limit 16MiB. TLS verifies
platform roots, redirects disabled, no automatic retry, including mutations.
No arbitrary HTTP client injection, extra auth headers or TLS bypass in v1.
Client/request/config Debug output must exclude credentials, inputs and bodies.

Blocking construction/use/drop must all occur outside an async runtime; async
callers use async methods or put the full blocking lifecycle in spawn_blocking.
No block_on bridge, reentrancy promise, implicit retry or cancellation rollback.

### Errors and explicit token steps

Freeze error variant names `Configuration`, `Validation`, `Encode`, `Transport`,
`Http`, `Api`, `Protocol`, `Decode`, `ResponseTooLarge`, `UnsupportedAuthStep`.
Payload structs/private constructors are runtime-owned; expose `http_status()`
returning Option<u16> and `validation_errors()` returning Option<&ValidationErrors>.
Distinguish timeout in Transport. API failure messages/details may be available
through explicit accessors but never printed by Debug/Display. Decode errors
also suppress original field values/raw bodies. Non2xx is never success; parse
valid API failure envelopes before falling back to Http. Protocol is malformed
envelope/namespace, Decode is typed-output mismatch.

```rust
pub struct SecretString { /* private; redacted Debug/Display */ }
impl SecretString { pub fn expose_secret(&self) -> &str; }
pub enum TokenStep {
    Complete { token: SecretString },
    Challenge { token: SecretString, next_action: String },
}
impl TokenStep {
    pub fn from_parts(complete: bool, token: Option<String>,
        next_action: Option<String>, known_steps: &[&str]) -> Result<Self, Error>;
}
```

Generated auth output convenience `token_step(&self) -> Result<TokenStep, Error>`
extracts described wire fields and calls from_parts with generated known steps.
complete=false requires a nonempty transient token and a known next action;
complete=true requires a final token. An unknown next action returns
UnsupportedAuthStep; missing/inconsistent fields return Protocol. Runtime
does not assume a per-provider response field layout. Callers invoke generated
token steps explicitly; transient/final tokens are never installed automatically.

### Frozen acquisition/configuration/package contract

Authoritative production snapshot is public unauthenticated OPTIONS
`https://api.vpsfree.cz/v7.0/`, profile `public-live-api-7.0`. Lead/implementer
capture reports protocol 2.0, 104 top-level/152 total resources, 519 API actions
and 5 auth actions. Inventory saved snapshot exactly; these observed counts are
not a completeness/plugin guarantee. No production auth is needed for this
profile. Controlled local metadata is only a separate behavior-test input.

Snapshot JSON envelope keys are exactly `schema_format` (1), `api_version`
(string), `protocol_version` (string), `source_url` (explicit version URL),
`profile` (string), `mount_path` (string, `/` initially), `description` (sanitized
HaveAPI response description object, after validating the successful OPTIONS
envelope). Preserve version/auth structural discovery.
The schema SHA256 hashes canonical UTF-8 snapshot JSON (sorted object keys,
two-space indent, LF and terminal newline); arrays retain order. Separate
`schema/provenance.json` records capture time, source/digest/profile, generator
revision, runtime digest, toolchain and sanitizer diagnostics. Separate
`schema/inventory.json` records resources/actions/parameters and known coverage;
unknown plugin coverage is explicit. Never save credentials/login responses.
Strip prose/descriptions/examples/validator human messages and protected default
values; retain validators, wire names, key names, auth schemas and machine paths.

CLI contract: `fetch URL --api-version VERSION --profile PROFILE --output FILE`;
`generate --schema FILE --api-version VERSION --config FILE --output DIR [--check]`.
Fetch URL is the explicit version endpoint. Generation is offline. Both require
version; unknown/absent/mismatched versions fail, never use default_version.
Config `generator.toml` has root keys `crate_name="vpsadmin-client"`,
`crate_version="0.1.0"`, `license="MIT"`, `edition="2024"`,
`rust_version="1.95"`, `rustfmt_version` (exact stdout of pinned rustfmt --version).
No application release field. Fixture configs can choose another crate name.
Generator facade is `HaveAPI::RustClient::Generator.new(schema:, config:)` with
parsed Hash values and `generate(output:, check: false)`; `Snapshot.load(path)`
returns validated envelope Hash; `Snapshot.fetch(url:, api_version:, profile:)`
returns sanitized envelope Hash, with no file writes. CLI owns serialization.
Additional diagnostics/inventory helpers belong to implementer1 without changing
these entry points. Generation replaces only its owned output tree atomically;
check never writes. Scaffolding/templates supply initial manifest requirements;
subsequent regeneration must not overwrite handwritten package files.

Initial Rust crate is `vpsadmin-client` 0.1.0 (import vpsadmin_client), MIT,
edition 2024, MSRV 1.95. Private runtime harness uses the same dependency contract:
serde 1 with derive, serde_json 1, url 2.5; reqwest 0.13.5 with default-features=false
and features `["json", "rustls"]`. Cargo feature `default=[]`,
`blocking=["reqwest/blocking"]`. Caret dependency ranges are recorded in manifest;
committed Cargo.lock freezes resolutions for CI/reproduction. Tokio 1 with macros
and rt-multi-thread is a dev/example dependency, not a second runtime adapter.
No additional production dependency is required by the contract. Rustls here
uses reqwest's platform verifier and aws-lc backend; do not promise a C-free build.

The actual client retains Nix pin fe13242281a67641c0102cdb1087f0ebe586c7df:
rustc 1.98.1, cargo 1.98.0, rustfmt 1.9.0. HaveAPI's own development pin may
advance independently; clarification 7 defines the test/reproduction boundary.
Config records the complete selected rustfmt --version stdout, not its package
version. Use edition 2024 formatting and reject formatter mismatch. MSRV 1.95
is a separate check; do not downgrade either Nix input to enforce it.

All lanes may author tests now and run only known quick checks. Generated
fixture compilation, real HaveAPI/vpsAdmin fixture execution, real generated
client builds/tests, feature/MSRV matrices and package verification are mandatory
long/uncertain gates only AFTER committed intended deliverable, passing quick
checks and independent final review, launched/monitored by a fresh watcher.
Real new-client acceptance includes async/blocking VPS show/update (disposable
server only), list pagination, nullable/Custom values and auth flows. No production
mutations, new external repository creation, publication or default-branch
integration is implied. Runtime fixes require client regeneration/release.

### Clarification 2: named empty output and ok! (2026-10-19)

Evidence: HaveAPI `c14e7d3158b91c134c2817b489cd29772fc09f82`,
`servers/ruby/lib/haveapi/action.rb` methods `output`, `safe_output`, `ok!`,
and `servers/ruby/lib/haveapi/authentication/token/provider.rb` Revoke.
`output(false)` without a block is a getter, not a no-output DSL declaration.
The server's `ok!` can produce successful `response: {}` even when description
contains a named empty output schema; Token Revoke does this. No server/DSL
change is required.

Add the `OutputSpec.allow_empty_response: bool` field shown above. Generator sets
it true ONLY for Object/Hash layouts with zero described output parameters;
otherwise false, including all list layouts. Keep the generated named Output
struct rather than changing its public type to `()`. Decoder accepts either the
normal named output object, or an exactly empty response object when this flag
is true. In the latter case deserialize an empty JSON object into Output.
Preserve response metadata normally. This is a narrow compatibility rule for
the captured schema, not a claim of complete metadata or a rule permitting
missing declared fields generally.

All envelope/status/HTTP checks still apply. Missing namespace for nonempty
schemas, nonempty response with the wrong namespace, null/scalar/list response
in place of the envelope object, and missing namespace for list schemas remain
errors. `output=None` remains the distinct explicit no-output path. Tests must
cover actual token revoke success, both named/unnamed empty-object successes,
and each negative case above. Implementer0 owns decode, implementer1 emits the
flag, implementer2 supplies protocol/revoke fixtures, implementer3 regenerates.

### Clarification 3: nested resource and auth accessor names (2026-10-19)

Clarification 4 supersedes the single-underscore spelling in examples here;
the flat accessor and placeholder-binding policy remain unchanged.

Use one flat root resource accessor per generated resource path in v1:
`api.project_task(project_id).show(task_id)`. Its name matches the flattened
resource module (`resources::project_task::show`). The resource handle binds
accumulated ancestor placeholders; each action accepts only remaining path
placeholders in template order. Values still use `impl ToString` and runtime
segment encoding. Ancestor prefix interpretation must be deterministic and
validated against each full action template; unresolved/ambiguous placeholder
ownership fails generation rather than guessing or losing arguments.

Authentication follows the same deterministic names: the described
authentication/token/token resource becomes
`api.authentication_token_token().request()` and
`resources::authentication_token_token::request`. This establishes names from
schema paths, not a claim that every server has the same auth resource path.
Do not add a second chained accessor such as `api.project().task(project_id)`
in v1. That convenience can be additive later. Async and blocking use identical
accessors. Implementer1 owns generation; implementers2/3 use these names in
fixtures/examples, with runtime interfaces unchanged.

### Clarification 4: preserve resource component boundaries (2026-10-19)

The actual production description contains both nested `dataset/plan` and
top-level `dataset_plan`. Single-underscore joining loses those distinct schema
paths and blocks the required complete snapshot generation. Normalize each
resource component to snake_case, preserving its ordinary word underscores, and
join components with `__` for both module and flat root accessor names. Thus
`dataset/plan` becomes `dataset__plan`, while `dataset_plan` remains
`dataset_plan`. Examples from clarification 3 become
`api.project__task(project_id).show(task_id)`,
`resources::project__task::show`,
`api.authentication__token__token().request()` and
`resources::authentication__token__token::request`.

This is a generic naming rule, with no site-specific snapshot edits or config
overrides. Validate the final normalized identifiers/files and still reject any
remaining collision with both original schema paths. Do not add traversal-order
suffixes. Flat accessor shape and parent/action placeholder ownership remain as
in clarification 3. Existing PascalCase type names local to each action module
do not need a new global naming scheme. Implementer1 applies this rule;
implementers2/3 use it in fixtures/examples. Runtime interfaces are unchanged.

### Clarification 5: DELETE uses JSON body input (2026-10-19)

This corrects the original GET/DELETE query rule; it does not add methods,
execution modes, server behavior or a compatibility switch. Relevant evidence
read from canonical HaveAPI Git objects at
`b80ed05b2f8ef6ec68fc182464fe4133b3663da5`:

- `servers/ruby/lib/haveapi/server.rb:721-739` classifies every method except
  GET/HEAD/OPTIONS as a body method; action input is parsed JSON body or `{}`,
  never `request.GET`, for DELETE. Nonempty bodies require JSON Content-Type
  and a top-level object. This is also present at baseline `c14e7d3`.
- `clients/go/template/action.go.erb:435-475` selects query encoding only for
  GET and `DoBodyRequest` for all other described methods, including DELETE.
- `doc/protocol.md:250-263` describes query null encoding with a GET example;
  it does not establish DELETE as a query method. The reported real-server
  fixture failure (DELETE receives `{}`, GET succeeds) matches this source.

The supported action Method enum stays Get/Delete/Post/Put/Patch. The common
method classifier, currently `Method::query`, is true only for Get. All four
other variants use the existing JSON-body preparation logic, with the actual
HTTP method preserved. JSON Content-Type is set, action/global/object metadata
retain their established namespaces, and an empty assembled body is `{}`.
Named list input stays nested in this object envelope; the existing prohibition
on unnamespaced list input remains. No HEAD/OPTIONS action support is introduced;
OPTIONS schema acquisition is separate.

For DELETE, preserve unset omission and actual JSON null/false/zero/empty string,
nested Custom values and already-supported named list input, exactly as for
other body methods. Do not duplicate input/metadata into the query or add a
query fallback/retry. The restrictions on nested Custom/list query values now
apply only to GET. URL path encoding, authentication, error/status rules,
redirect rejection, redaction and no-retry invariants are unchanged. A failed
or timed-out DELETE must never be replayed to probe encoding compatibility.

Implementation boundaries and acceptance:

1. Implementer0 changes only the shared runtime classifier, its focused tests
   and runtime documentation. Reclassify the existing nested-query rejection
   case as GET. Preparation tests cover all five methods, including DELETE
   omission/null/falsy values, metadata, Custom and named list body shapes,
   JSON Content-Type and absence of input/metadata query keys. Both transports
   must emit the same DELETE body and retain GET query behavior.
2. Implementer2 keeps real generic-server fixtures strict: generated async and
   blocking DELETE calls must deliver the exact expected input/metadata to
   action code, paired with a passing GET query control. No changing expected
   DELETE output to `{}` or patching server input parsing. Disposable fixtures
   only; its separately assigned database/EOF harness fix stays independent.
3. Implementer1 reconciles any generator-facing prose/test expectation that
   says DELETE uses query encoding; no ActionSpec/schema format/public setter
   change is needed. Implementer3 regenerates the actual client with corrected
   embedded source and runtime/provenance digest, preserving the API7.0 snapshot.
4. After intended fixes and regenerated client are committed and known quick
   checks pass, obtain affected-lane independent final review before the next
   long tests. A fresh watcher then runs the focused runtime async/blocking
   regressions and real generic-server matrix, and verifies corrected real
   client default/blocking compilation, MSRV1.95 and package/regeneration checks.
   No production mutation is part of acceptance. The unchanged public GET
   smoke need not be repeated solely for this classifier correction.

Compatibility: this repairs initial v1 wire behavior to match the current
HaveAPI server and Go client; it changes no public Rust signatures or API target.
Do not claim support for servers requiring DELETE query input. No database,
server deployment or migration is involved. Existing embedded clients need
regeneration to receive the fix; pinning an older generated revision restores
the defective DELETE encoding and is not an acceptable DELETE workaround.
If delivery must be rolled back, hold DELETE use until a corrected build is
available rather than replaying mutations. Prior checks at HaveAPI `b80ed05`
and client `e4f4638f48b99d0944ffaa2e8e6e684831bea0a8` exercised old encoding;
they remain historical evidence, not verification of the corrected runtime.

### Clarification 6: client publication through GitHub Actions (2026-10-19)

The user prefers Actions publication; local Cargo publication is on hold and
the Cargo-login request is retracted. This brief changes the client publication
path only. It authorizes no registry settings, upload, tag/branch mutation or
HaveAPI shared release. Source remains frozen until the lead's current dry-run
watcher at client `c4a0f597cd3602e28ae11846962e2d1e07a0c1ff` finishes.

Official requirements checked today:

- [crates.io trusted publishing](https://crates.io/docs/trusted-publishing)
  requires an existing crate and crate ownership. Its
  [current documentation source](https://github.com/rust-lang/crates.io/blob/6cf63268f7fac38f8d255bbb22497c8ecff35d57/svelte/src/routes/docs/trusted-publishing/+page.svelte)
  explicitly requires an API token for initial publication. That first upload
  can run in GitHub Actions; local Cargo login/publication is unnecessary.
- [RubyGems pending publishers](https://guides.rubygems.org/trusted-publishing/#pushing-a-new-gem-with-a-trusted-publisher)
  permit a new gem's first upload with OIDC. The registering account becomes
  an owner after the first push. This capability does not exist in the checked
  crates.io prerequisites. Both public package APIs returned 404 for
  `vpsadmin-client` and `haveapi-rust-client` at this checkpoint.

Implementer3 owns exactly the client `.github/workflows/release.yml`, a small
reuse change to `.github/workflows/ci.yml`, and release instructions in
`docs/development.md`. No README/generated/schema/runtime changes; the README
review and all HaveAPI release work remain separate. Implement this sequence:

1. New release workflow uses `workflow_dispatch` only, with required choice
   `authentication: oidc | bootstrap`, default `oidc`. Dispatch against a version
   tag; [gh workflow run --ref](https://cli.github.com/manual/gh_workflow_run)
   accepts a tag. A non-tag dispatch fails. Require repository
   `vpsfreecz/vpsadmin-rust-client`, package name `vpsadmin-client`, and tag
   exactly `v<Cargo.toml package.version>`. Resolve the source commit once and
   retain it through verification/publication; fail if its tag moves. Workflow
   must exist on the default branch and at the tagged revision before use.
   No automatic publication on pushes/PRs and no new release-management framework.
2. Add `workflow_call` to existing `ci.yml`; a release `verify` job calls
   `./.github/workflows/ci.yml` from the same revision after tag validation.
   Reuse its async/blocking tests, docs/package, MSRV and regeneration jobs.
   `publish` needs both validation and successful verification. Keep ordinary
   branch/PR/manual CI; limit standalone push CI to branches to avoid duplicate
   tag verification. Do not copy the test matrix into the release workflow or
   accept a green result for another commit. Pass no publishing secrets to CI.
3. Publishing job uses protected environment `release`, with required reviewers
   and permitted version tags configured by a repository administrator. Use
   `contents: read` globally; grant `id-token: write` only to this job. Check out
   the verified commit with persisted credentials disabled. Serialize client
   publication runs with `cancel-in-progress: false`. Use the committed Nix
   environment and `cargo publish --locked`; no cargo login or upload scripts.
4. `bootstrap` is an explicit first-publication choice, never an automatic
   fallback from failed OIDC. Require the crate to be absent (registry 404;
   network/auth/other failures are errors) and protected environment secret
   `CARGO_PUBLISH_BOOTSTRAP_TOKEN`. The maintainer creates a short-expiry API
   token with the minimum available crate/publish scope. Supply it only as
   `CARGO_REGISTRY_TOKEN` to the publish step. Missing token fails visibly.
5. For `oidc`, use official `rust-lang/crates-io-auth-action`, then pass its
   `token` output only to the publish step. Verified latest release is v1.0.5,
   commit `c6f97d42243bad5fab37ca0427f495c86d5b1a18`; pin that SHA. Keep token
   acquisition late, after checks/tool setup. Never print credentials. After
   the initial upload, the crate owner registers owner `vpsfreecz`, repository
   `vpsadmin-rust-client`, workflow filename `release.yml`, environment `release`
   in crates.io Settings → Trusted Publishing, then revokes/removes the bootstrap
   token/secret. Subsequent releases select `oidc`; no retained token is needed.

Acceptance: quick workflow/YAML/shell validation and review of the tag/mode/
permissions gates; negative paths for wrong repository/tag/version, unavailable
bootstrap secret and registry lookup/auth failure must stop before upload.
Commit intended workflow/docs changes and obtain independent final review before
watcher-run CI/package checks. Confirm reused CI covers the exact published
source. Only an explicitly authorized registry upload can validate end-to-end
OIDC; package/dry-run success is not evidence of that. After a failed upload,
check registry state before retrying; never move tags or overwrite a version.
Recovery can disable publication/remove its trust binding without changing the
API7.0 client contract. Existing package SemVer and source-provenance rules apply.

Generator recommendation only: HaveAPI
`9e4c29a0412a25256ce944641f60ba13e9f03c2b` already has protected
`.github/workflows/release.yml`, job-level OIDC and
`rubygems/configure-rubygems-credentials` pinned v2.1.0. Source gem
`clients/rust/haveapi-rust-client.gemspec` is `haveapi-rust-client` 0.29.0,
sharing VERSION and depending on `haveapi-client ~> 0.29.0`; `make version`
already updates both. It is NOT yet in the shared release artifact/build list.
If separately requested, extend existing `utils/release/artifacts.rb` GEMS,
version/dependency/lock checks, `utils/release/build.sh`, Makefile dependency/test
coverage and release specs/docs. The existing generic publish loop then handles
the fourth gem after `haveapi-client`; add no second gem-publishing workflow.
An intended RubyGems owner would register a pending publisher for this gem with
`vpsfreecz` / `haveapi` / `release.yml` / `release`. Existing shared-release
approval publishes the other gems, npm and PHP mirror too: the client Actions
request does not authorize that integration, configuration or publication.

### Clarification 7: formatter ownership after HaveAPI rebase (2026-10-21)

Lead accepted this bounded correction before implementation. Source stays frozen
until the lead assigns the changes. Preserve the exact production formatter
guard, the client's own toolchain, and all generated client bytes. No new pin,
formatter framework, generation mode, API behavior or publication is involved.

Evidence at HaveAPI `68cc80b012b7a6b9bcdf35c008c338cbc3f4c000` and client
`945af6a97717a7a6373507bbc9592d5cd53727c2`:

- [Final integration review](final-review-integration-rebase.md) records unchanged
  generator/runtime source and HaveAPI's new nixpkgs
  `02c087f3fe673c9e317f206a627cb6b910336dbe`; the client retains its own
  `fe13242281a67641c0102cdb1087f0ebe586c7df` pin and rustfmt 1.9.0 config.
- [Batch result](artifacts/integration-package-recheck/result.json) has nine
  passing workflows, failed HaveAPI clients/rust run 39600600027, failed local
  package reproduction, and no active operations. Exact client CI 39600821857
  passed at `945af6a` with its own toolchain.
- [Failed CI log](artifacts/integration-package-recheck/failed-39600600027.log)
  shows four generator specs stopping at `generator.rb:29` before rendering.
  `clients/rust/spec/spec_helper.rb:13` hard-codes rustfmt 1.9.0. The new
  HaveAPI shell supplies Ruby 3.4.11, rustc/Cargo 1.99.0 and rustfmt 1.10.0.
- [Packaged generation log](generator-package-integration-acceptance/generation.log)
  shows the same guard failure. The saved probe reads unchanged client
  `generator.toml`, but the operation selected HaveAPI's newer PATH formatter.
  This is an environment-selection error, not evidence of changed API7 bytes.

Recommendation and bounded file ownership:

1. Implementer1 changes `clients/rust/spec/spec_helper.rb` so temporary test
   config obtains exact version text from the SAME executable the generator
   uses: `ENV.fetch('RUSTFMT', 'rustfmt')`, passed as one executable argument
   with `--version` to Open3. Check successful status and nonempty stripped
   stdout; a missing/failing tool is a test setup failure, never a skipped spec
   or fallback to a constant. Derive once per selected fixture configuration,
   then reuse that configuration for repeated/shuffled/check-only assertions.
   This adapts ephemeral fixtures, not stored client configuration.
2. Keep `lib/haveapi/rust_client/generator.rb` unchanged: its exact comparison
   remains mandatory. In `spec/unit/generator_spec.rb`, retain deliberate
   mismatch rejection and prove it preserves an existing output tree as well
   as refusing to create a new one. Cover selected-executable override and
   failed version-probe handling in the fixture setup where useful. Keep the
   successful real-formatter determinism/ownership tests; do not mock them away.
3. Implementer1 reconciles `clients/rust/README.md` and
   `clients/rust/docs/generation.md`: current shell supplies development tools;
   an existing client uses its own recorded exact formatter, optionally selected
   by existing RUSTFMT. The example 1.9.0 value must be labelled as an example,
   not claimed to be the current HaveAPI shell version. Implementer0 owns the
   equivalent stale claim in `clients/rust/runtime/README.md`; docs-only there.
4. No integration source edit is needed for the observed failure:
   `spec/integration/run.rb:101` already derives a temporary formatter version.
   Run that fixture matrix with current HaveAPI PATH and RUSTFMT unset. If a
   later assigned check intentionally supplies RUSTFMT to this runner, its
   version probe must first be aligned with the same selected executable and
   checked status, by implementer2. Do not introduce a cross-lane helper or
   silently inherit the saved-client override into generic integration checks.

Saved API7 package verification is a separate operation, owned by the lead's
session-only harness and fresh watcher. Build/extract the gem and run its probe
under current HaveAPI Ruby 3.4, but set RUSTFMT to the absolute rustfmt executable
resolved from the actual client's locked Nix environment. Restore/root that
tool through the fresh setup utility if needed, retain it for the whole run,
and record executable/store path, complete version stdout and both source/lock
identities. Probe version must match the UNCHANGED client generator.toml before
generation. Do not hard-code a garbage-collected store path, substitute current
HaveAPI rustfmt, rewrite saved config, or enter the client's older Ruby shell
for the package probe: that would lose current-Ruby acceptance coverage.
The existing RUSTFMT override is enough; no generator production change is needed.

Acceptance after intended changes are committed and quick checks pass:

- Independent affected review covers fixture selection, mismatch tests, docs
  and any session probe-command change; no broader source review is inferred.
- Fresh watcher verifies the full HaveAPI clients/rust workflow at the final
  feature head, including previously unexecuted later runtime/lint/integration
  steps under the new shell. A passing first unit step alone is insufficient.
- The extracted-gem probe, under current Ruby plus client rustfmt 1.9.0, must
  reproduce the saved API7 generated manifest and every owned file byte, then
  pass read-only --check. It must retain the existing proof that loaded
  generator logic came from the extracted package, not the source checkout.
- Compare generator/runtime/template/lock/schema/client config inputs before
  claiming retained client evidence. `generator_digest` covers lib/template,
  not specs/docs; these bounded edits should not change generated bytes or
  require client source/config/provenance edits. Keep the recorded compatible
  HaveAPI source ref available. Any unexpected output/digest delta returns to
  diagnosis instead of updating expected files to make the check green.

Alternative rejected: adding a second fixed formatter pin to HaveAPI's shell
would couple generic generator tests to one client's formatting history and
hide rather than exercise the updated development environment. Exact formatting
belongs to each saved generation config/toolchain, not a universal generator
release pin. No cross-formatter byte equality is promised. Recovery is retaining
the client's input bundle and selecting its recorded formatter; never weakening
the mismatch guard. Nine unrelated passes remain evidence only for their exact
heads/inputs; the failed Rust/package gates still block integration until fixed
and verified. Release hold, no registry/token access and no production changes
remain in effect.

### Clarification 8: new-client merge catalog prerequisite (2026-10-21)

Status: bounded diagnosis and configuration proposal only. HaveAPI/master is
merged and its six default-branch checks passed, per the lead. Client feature
`945af6a97717a7a6373507bbc9592d5cd53727c2` is reviewed and CI-green; its `main`
target remains `b67a3ba5eef89b2bd6533050aa8769aaa0574114`. The user approved
those project merges, not workspace configuration integration or activation.
No client mutation, claim, package build, deployment or registry action was
performed for this diagnosis. Releases and token access remain on hold.

**Cause and owning configuration.** The session's `portal.yml` already registers
`vpsadmin-rust-client` with default branch `main`, and its canonical bare clone
exists. That does not register an immutable coordination resource. The installed
guide requires both session registration and catalog presence. Workspace
`config/coordination.nix` owns remote/target identities; `flake.nix:48` passes it
as `coordinationConfig` to the composed package. Generic runtime
`nix/workspace-portal.nix` writes it to `share/dev-workspace/coordination.json`.
Installed `libexec/workspace-coordination.rb`, `Catalog#initialize` and
`Catalog#repository`, read that package file and reject an absent repository.
The installed host/session command dispatchers provide no ordinary catalog-add
command. `workspace-host register` registers a workspace root, not a repository.
Neither re-registering this client worktree nor editing its portal entry fixes
the refusal recorded with
[the requested client claim](artifacts/approved-default-integration/vpsadmin-rust-client-claim.json).

The exact minimal source proposal is two additions to the workspace-owned file:

```diff
--- a/config/coordination.nix
+++ b/config/coordination.nix
@@
   targets = {
+    vpsadmin-rust-client = "main";
     vpsadminos = "staging";
@@
           "vpsadmin-go-client"
+          "vpsadmin-rust-client"
           "confctl"
```

Its evaluated entry must be exactly
`remote = "git@github.com:vpsfreecz/vpsadmin-rust-client.git"` and
`defaultTarget = "refs/heads/main"`. The existing map supplies the remote;
omitting the target override would incorrectly select `master`. No local-path
field, runtime implementation, system configuration, input update or new
registration framework is needed.

**Selected-source boundary.** Read-only inspection found that the selected
package has advanced from the lead's earlier `6bbjch8…` package to
`/nix/store/hzf9qda2ckjsv72b689bclc6p3v8ap9l-dev-workspace-0.2.0`; it still lacks
the client entry. Its catalog digest is
`sha256:7f101a6bb029df484140060a13ad73f01f78a7f6839eb9e346904c2067b554bc`.
Its extension catalog references workspace source
`/nix/store/29b3kfr8xjx4v8dm6qd74hrhcx009zik-source`. That source locks the generic
runtime to `f8f2938b4e2cfd6e5b82657d08f014357817808f`, retaining extension
`767dfd587e346168e1443e65ccdb67ce748f3fe3`. Its nine packaging inputs under
`flake.nix`, `flake.lock`, `config/` and `skills/update-codex/` match workspace
Git commit `530038a8ee2bf6772144b07ca0cb02426fc1e6d6` by direct blob comparison.
This identifies input content; it does not authorize using that branch/history.

Shared workspace HEAD `1ec83cc87b2ad4e9fa944524fe8c0c2cd6e4fbf8` instead locks
runtime `968646471b1190c16a8cf60ff50736cd0525fa3f` and has different team settings;
the selected package supports eight native child threads and additional Full
team variants. Thus building from current master would also change selected
runtime/team behavior. Do not revert that deployment, consume another session's
unmerged history, access its worktree, or characterize such a package as merely
the client catalog addition. The owning workspace source/base and deployment
scope need a separate decision before a candidate package is prepared.

**Bounded next options and authority.** The supported ordinary route is the
two-entry workspace configuration change followed by reviewed forward profile
activation. The lead must first settle the source/base with the workspace
deployment owner. An assigned implementer then works in this session's dedicated
`worktrees/2026-10-18-rust-client-generator/workspace` feature worktree, using an
explicitly agreed base. Preserve the selected runtime, extension, lock graph,
team policy and other catalog mappings; do not silently expand this patch.
Prepare the concrete reviewed candidate before seeking final user approval for
the new workspace integration/activation scope. Publication of that feature
branch follows ordinary SSH policy; workspace/master integration is a separate
explicit approval, not implied by client/main approval. No such candidate or
activation is authorized or performed by this design-only assignment.

Quick preparation checks are whitespace/Nix syntax and evaluated catalog checks:
the new entry has the exact remote/main target above, removing it reproduces
the baseline catalog, and the flake/lock/team/runtime inputs are unchanged from
the agreed baseline. Commit intended changes and pass quick checks before
independent final review of the complete branch and source-selection proof.
Only afterward may a fresh watcher build the minimal composed workspace package
and verify its installed catalog, claims contract and registration plans against
the selected package; no activation or claim is part of verification. Stop on
any unrelated runtime, Codex, team, machine or registration-plan difference.
No generic coordinator or full infrastructure test campaign is indicated.

If later authorized, the lead follows the then-selected installed guide for a
machine-only `vpsfree:aitherdev` claim and ordinary forward profile activation,
checks continuity and catalog visibility, then releases machine ownership.
Only afterward does the client use its ordinary short repository merge claim.
Prepare/build outside claims. Preserve existing claim/state mappings; recover
an interrupted selection through its supported forward recovery, never by
editing store/state files or selecting the older package as a shortcut.

Alternatively, the lead may ask the user for an explicit one-off exception to
the workspace's catalog-claim requirement for this exact already-approved
client/main merge, instead of undertaking workspace deployment in this task.
No exception is inferred or granted here. Unless and until that direction is
given, the missing catalog entry remains a hard merge blocker. Even with such
direction, retain fresh exact local/remote ref checks, required hooks, ordinary
fast-forward-only integration and non-force SSH push, remote proof, and no
release/token actions. A moved target or changed reviewed feature returns to
preparation. The architect hands off this decision; the lead owns communication,
any separately authorized setup, and the final merge operation.

## Recommendation and scope

Add a Ruby generator under `haveapi/clients/rust/` and a separate
`vpsadmin-rust-client` repository containing a self-contained generated, typed
client. Maintain common Rust protocol/transport source once in HaveAPI and copy
it into each generated crate, as the Go generator does. There is no separately
published HaveAPI runtime dependency. Retain Ruby/ERB for generation. Rust users
consume an ordinary crate with normal ecosystem dependencies such as reqwest
and Serde; they need neither Ruby nor a running API at build time.

The first implementation supports HaveAPI protocol major 2, one selected API
version per generated crate, async calls using Tokio/reqwest and sync calls
through an optional `blocking` feature, typed action builders, JSON bodies,
query parameters, response/error envelopes, metadata,
partial associations, Basic authentication, existing HaveAPI/OAuth2 tokens, and
explicit generated token request/challenge/renew/revoke actions. Start the
vpsAdmin client with API `7.0`, using the reviewed public production snapshot
from `https://api.vpsfree.cz/v7.0/`. The captured surface and digest, rather than
an assumed complete admin schema, define its generated interface.

V1 has no automatic retries, background token refresh,
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
| Embed maintained runtime source in every generated client, as Go does | Accepted: one source of truth in HaveAPI, one published client crate to consume, and no separate runtime compatibility/release boundary. Runtime fixes require regenerating and releasing each affected client. |
| Publish a shared runtime crate | A compatible dependency update can deliver runtime fixes without regeneration. It adds a public compatibility contract, package naming and publication coordination. Reconsider if many generated clients make regeneration burdensome. |
| Write the generator in Rust | Reasonable later; adds schema acquisition and tooling work without improving the generated API. Keep Ruby initially. |
| Discover the API at runtime | Loses the requested compile-time, version-specific API. Do not mix dynamic discovery into normal client calls. |
| Generate closed enums and complete associated resource structs everywhere | Metadata and permission filtering do not justify those guarantees. Use conservative representations in v1. |

## Evidence and limits of investigation

Inspected canonical bare repository HEADs with `git show`, `git ls-tree`, and
`git grep`; no other session's worktrees were used. These revisions identify
source evidence, not client/server support requirements. The lead and client
owner subsequently captured public production OPTIONS without credentials;
its inventory is recorded in the frozen contract. Architect0 ran no build,
test or deployment. HaveAPI implementation baseline is now
`c14e7d3158b91c134c2817b489cd29772fc09f82`; its AGENTS, development guidance,
Go client sources and current Nix inputs were rechecked for this handoff.

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
  establish full visibility. The accepted public capture defines the initial profile.
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
- [reqwest blocking](https://docs.rs/reqwest/latest/reqwest/blocking/index.html)
  documents its optional feature and prohibition on direct use inside an async
  runtime. [Tokio spawn_blocking](https://docs.rs/tokio/latest/tokio/task/fn.spawn_blocking.html)
  provides the supported bridge; already-started blocking work cannot be aborted.
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
  The frozen contract pins generation tools and declares dependencies; MSRV
  dependency compatibility still requires the scheduled acceptance check.

## Repository and interface boundaries

The frozen contract above owns exact names and signatures. The generator owns
acquisition/sanitization, schema validation, IR, naming, source rendering, and
generated-file ownership. The maintained runtime owns credentials, transport,
URL/query/body encoding, envelopes and common errors, without vpsAdmin-specific
resource names. Generated actions own static paths/namespaces, typed models,
validation and mode-independent setters. Runtime source is copied unchanged;
there is no independently published HaveAPI Rust runtime package.

```text
haveapi/clients/rust/
  bin/haveapi-rust-client
  Gemfile, Rakefile, haveapi-rust-client.gemspec
  lib/haveapi/rust_client/{cli,snapshot,ir,naming,generator,...}.rb
  template/
  spec/{unit,fixtures}/                 # implementer1
  spec/integration/                     # implementer2, including server harness
  runtime/                              # implementer0 exclusively
    src/lib.rs                          # private harness crate root
    src/runtime/{mod,protocol,types,error,auth,client,...}.rs
    Cargo.toml, Cargo.lock, tests/, docs/ # publish=false
  README.md, docs/{generation,releasing}.md

vpsadmin-rust-client/                    # implementer3 exclusively
  Cargo.toml, Cargo.lock, flake.nix, flake.lock
  src/lib.rs                            # handwritten facade/re-exports
  src/generated/{mod.rs,runtime/,resources/,...}
  schema/{api-7.0,provenance,inventory}.json
  generator.toml, tools/regenerate
  tests/, examples/, README.md, CHANGELOG.md
  .github/workflows/ci.yml
```

Generator gem is `haveapi-rust-client`; client crate is `vpsadmin-client` in
`git@github.com:vpsfreecz/vpsadmin-rust-client.git`. The user has already created
that repository. Registry publication and package-name availability checks are
separate from this implementation; no publication is authorized here.

The usage contract becomes a compiling example in the real client repository.
This mutation example requires a disposable fixture endpoint and fixture token:

```rust
use std::time::Duration;
use vpsadmin_client::Client;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let api = Client::builder(std::env::var("TEST_API_BASE_URL")?)
        .token(std::env::var("TEST_API_TOKEN")?)
        .timeout(Duration::from_secs(30))
        .build()?;
    let vps = api.vps().show(123).send().await?.output;
    println!("{}", vps.hostname.as_deref().unwrap_or("<not returned>"));
    api.vps().update(123).hostname("example").send().await?;
    Ok(())
}
```

With feature `blocking`, ordinary sync code uses `blocking::Client` and
`.send()?`. Models, setters, metadata, errors and API version are identical.
Root constants `API_VERSION` and `SCHEMA_SHA256` identify generated support.
Outputs own data and perform no hidden network calls; resource handles borrow
the client. Runtime version changes require regeneration, not a setter.

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

Use JSON object bodies for described DELETE/POST/PUT/PATCH actions and bracketed
query parameters for GET, matching the server and Go client (clarification 5).
Preserve input and
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
decode errors. The frozen contract explicitly supports input/metadata
namespace=false and rejects ordinary output namespace=false. Empty named output
and true no-output remain different contracts.

Datetime input accepts `YYYY-MM-DD` or
`YYYY-MM-DDTHH:MM[:SS[.fraction]](Z|±HH:MM|±HHMM)`, validating calendar,
time and offset ranges. A parser that accepts only RFC3339 is insufficient.
Strictly typed Rust setters need not expose every coercion accepted by Ruby. Non-numeric custom
resource primary keys lack enough portable metadata and remain a documented
limitation. Resource input IDs use nonnegative i64 (`0..=i64::MAX`); an optional
string helper may accept trimmed ASCII decimal digits with overflow checks.
Do not promise generic ID typing that the description cannot provide.

## Transport, authentication, and errors

Use a reusable async reqwest client by default; enable a reusable
`reqwest::blocking::Client` through the optional `blocking` feature in v1.
Use common request preparation and response decoding with JSON/Serde and
the pinned rustls feature set. V1 builder configuration provides timeouts,
user agent and response-size limit; custom roots/proxy controls are deferred.
Do not accept an opaque preconfigured HTTP client in v1 if
its redirect policy cannot be enforced. The runtime can remain concrete rather
than introducing a public pluggable transport trait initially. Both adapters
apply the same configuration/security policy and response-size limits.

Sync execution blocks the calling thread and needs no caller-owned Tokio runtime.
Do not implement it by calling `block_on` on an async client's runtime. The
blocking client's construction, use, and destruction must stay outside an async
runtime; direct use there is unsupported and can panic in reqwest. Async callers
should use the async client, or put the entire blocking-client lifecycle in
`tokio::task::spawn_blocking` with owned inputs/results. Do not move its final
drop back into async code or use `block_in_place`, which is unsuitable for a
current-thread runtime. There is no hidden reentrant sync-to-async bridge.
Started blocking work cannot be cancelled by aborting its join handle; HTTP
deadlines still apply, and a timeout does not undo a server mutation.

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

Separate acquisition from offline rendering. Frozen commands:

```text
haveapi-rust-client fetch https://api.vpsfree.cz/v7.0/ --api-version 7.0 \
  --profile public-live-api-7.0 --output schema/api-7.0.json
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
  coverage of missing resources/parameters. The initial production profile
  is the unauthenticated public capture; local profiles only support behavior
  tests. Authenticated metadata may still be partial and is not required here.

Generation provenance includes API version, protocol version, canonical schema
SHA-256, capture/profile and plugin coverage declarations where known, generator
version/revision, generator options, embedded runtime source digest, generated
dependency/feature requirements, Ruby dependency lock, and exact Rust/rustfmt
toolchain. The client lockfile records resolved ecosystem dependencies; there
is no independent HaveAPI runtime version requirement. Acquisition timestamp belongs
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
owned generated tree, including copied runtime modules; refuse symlinks/out-of-scope destinations. Remove obsolete
owned files, preserve handwritten files, and make `--check` read-only. Repeated
generation and reordered JSON-object input must produce identical files.
The scaffold declares the optional `blocking` feature and dependencies once;
regeneration checks those requirements against the maintained crate manifest
and reports needed changes without silently replacing handwritten packaging.

## Package versioning, compatibility, and release

The Ruby generator follows HaveAPI's existing shared release/version mechanism.
The generated vpsAdmin crate uses independent SemVer for its entire public Rust
interface, including exposed common types and both execution modes. Embedded
runtime source has no separate package version or public dependency boundary.
Initial package versions are chosen at implementation/release time; they do not
encode API 7.0. Record the supported API version prominently in crate docs and
constants. A change to the generated API target is an explicit compatibility
decision and, where it breaks consumers, a breaking package release.

Additive output fields and unknown validator choice values should remain usable
by older clients. Adding required inputs, removing/renaming methods or changing
public types requires a breaking package version; during 0.x that means a new
minor. New optional fields can use compatible releases with non-exhaustive
types/builders. MSRV changes are deliberate and documented, never accidental
patch updates. `rust-version="1.95"` is fixed; later CI verifies that minimum
and the pinned generation toolchain independently.

Generated crates depend only on the selected ecosystem libraries, with copied
runtime source compiled as part of the crate. Do not hand-edit generated actions
or runtime modules: fix the maintained HaveAPI source/config/snapshot, regenerate,
check and release each affected client. This is the explicit cost of embedding;
fixing HaveAPI alone does not update already published clients. Reusing a saved
API snapshot permits runtime-only regeneration without contacting the API.

The generator gem and generated vpsAdmin crate can be published when separately
authorized; no runtime publication or registry-order prerequisite exists. The
generator revision used must remain reproducible even if its gem is unpublished.
Add explicit opt-in release tasks; do not unexpectedly extend a broad existing
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

The lead owns scheduling, worktree setup, plan/state, serialized Git/index
operations and acceptance. Architect0 retains the design and shared contract.
The four source lanes below are assigned and may start after this P0 freeze.
Tests can be authored during implementation. Only measured, known quick checks
run before final review; uncertain checks count as long.

| Priority/package | Owner and file boundary | Dependencies | Acceptance and checks |
| --- | --- | --- | --- |
| P0: frozen design | Architect0: this design only | Authorized implementation | Shared signatures, source-copy convention, package/config/snapshot contract, four lanes and acceptance gates frozen; document-only consistency checks |
| P1: embedded runtime | Implementer0: `clients/rust/runtime/**`, including runtime docs/harness | P0 | Shared prepare/decode/validation and two transports; omission/null, errors, redaction, no retry/redirect; source contains no API-specific names. Author focused tests; formatter/static checks now, compilation-dependent tests after review unless already measured quick |
| P1: Ruby generator/tooling | Implementer1: `clients/rust/{bin,lib,template}/**`, unit specs/fixtures/shared spec setup, gem/build/docs; HaveAPI flake/Makefile/CI | P0; parallel with runtime | Exact offline facade/CLI/snapshot, safe public capture sanitizer, complete supported inventory, unique models/setters, runtime copy/digest, deterministic names and formatter pin; quick Ruby unit/RuboCop and read-only generation checks |
| P1/P2: behavior fixtures | Implementer2: `clients/rust/spec/integration/**` exclusively, including launcher/test-only server extensions | P0 to author; generator/runtime for execution | Explicit generic API1.0 fixture plus disposable vpsAdmin API7.0 behavior profile; auth/challenges/nullable/Custom/metadata/base paths/errors and async/blocking parity. No production schema edits. Generated compilation and server execution only after final review |
| P1/P2: actual client | Implementer3: sole `vpsadmin-rust-client/**` owner | P0 to scaffold/capture; generator/runtime for generation | Save authoritative public API7.0 snapshot/provenance/inventory via agreed sanitizer, generate real crate, author package/CI/examples/tests and offline regeneration. Real crate compilation/package/tests and behavior acceptance are mandatory after final review |
| Final gates | Lead selects independent reviewer and fresh verification watcher | Intended deliverable committed and known quick checks pass | Independent final whole-branch/history review before long tests; then watcher runs actual crate and generated fixtures, server integration, feature/MSRV/package matrix. Lead accepts exact evidence; no merge/publication implied |

Required implementation test matrix:

1. No parameters; required/optional/nullable input; default omission; empty string,
   zero and false; bad float/datetime; signed integer limits and numeric resource ID.
2. Named namespaces and supported no-namespace cases; JSON object/list layouts;
   GET query scalars/null; DELETE JSON omission/null/falsy/Custom/metadata;
   unsupported nested Custom GET query fails locally.
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
   escaping, copied runtime digest, stale-file removal confined to owned tree,
   read-only `--check`; packaged crate needs no HaveAPI path/Git dependency.
9. Async/blocking request and response parity using the same fixtures; ordinary
   sync execution without an application runtime; repeated calls and clean drop;
   complete blocking-client lifecycle inside `spawn_blocking` on current-thread
   and multi-thread Tokio runtimes. Cover deadlines and continued execution after
   aborting an already-started blocking task; do not promise nested runtime use.

Quick commands will be documented in the new `client-rust` Nix shell: generator
unit specs/RuboCop, `cargo fmt --check`, and generated tree `--check`. Runtime
unit tests and clippy require compilation: treat them as long/uncertain unless
already measured quick in the current environment.
Full generated-crate compilation, async/blocking test-server integration, MSRV
and blocking-feature matrices, and
package verification are longer/uncertain checks run through the required fresh
verification watcher only after all intended changes are committed, quick local
checks pass, and independent final review is complete. No
large vpsAdminOS cluster is necessary for the first client. A gated, read-only
live smoke test is supplemental and never the reproducibility gate.

## Acceptance dependencies and bounded follow-up

No product/default choice remains open for implementation. The frozen contract
selects API7.0 public-live metadata, crate/license/TLS/edition/MSRV/toolchain,
namespace/path/no-output handling, numeric resource IDs, datetime grammar,
descriptive-text sanitization and four owners. Contract ambiguities discovered
while implementing return through the lead as numbered amendments; they do not
authorize broadening v1 or changing another lane's files.

Evidence still needed for acceptance is implementation work: review the saved
sanitized snapshot/inventory; demonstrate offline deterministic generation;
compile/package/test the actual existing client repository in async and blocking
modes; verify dependency resolution on MSRV1.95; exercise disposable VPS
show/update, pagination, Custom/nullable and auth behavior. Long checks wait for
committed deliverable plus quick checks and independent final review. A read-only
live smoke may supplement those fixtures with approved credentials; production
mutations are excluded. No server changes or production-auth acquisition are
needed for the initial generated surface.

Initial public visibility cannot prove full permission/plugin coverage. Unknown
future parameter types, unsupported layouts, unnamespaced action output and
version mismatch fail explicitly instead of silently dropping schema. Registry
publication, OAuth browser orchestration, automatic retries/pagination/polling,
per-item input metadata and opaque resource IDs remain outside v1.

This is a design freeze, not a claim that implementation, compilation, review
or acceptance testing has passed. Recovery remains pinning the previous client
and reproducible snapshot/generator inputs; runtime fixes regenerate clients.
