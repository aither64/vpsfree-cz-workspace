# Plan: generated API documentation for maintained clients

**Implementation approved by the user on 2026-10-22.** The exact interface and
owner contract is [api-doc-contract.md](api-doc-contract.md); it is authoritative
over earlier provisional details. Baseline inspected:
`08345b2d5ede025972a3daec8b4a373efb51d711` in HaveAPI. Existing release verification
does not cover the new implementation. Publication and default integration remain
outside authorization. Architect updates design only; four implementers own code.

## Current coverage and intended result

The server's HTML documentation registers exactly **Ruby, JavaScript, PHP, CLI,
File system, curl, HTTP**. The JavaScript renderer uses `HaveAPI.Client` and
callbacks. Component README examples do not become server HTML examples.

| Requested variant | Current generated server examples | Planned tab |
| --- | --- | --- |
| Go | Absent | Go |
| Rust async | Absent | Rust (async) |
| Rust blocking | Absent | Rust (blocking) |
| Python synchronous | Absent | Python (sync) |
| Python asynchronous | Absent | Python (async) |
| JavaScript callbacks | Present, labeled JavaScript | JavaScript (callback) |
| JavaScript Promises | Absent | JavaScript (async) |
| TypeScript callbacks | Absent | TypeScript (callback) |
| TypeScript Promises | Absent | TypeScript (async) |

Remove the **File system** renderer/tab because that client is no longer actively
developed and the examples consume space. Preserve Ruby, PHP, CLI, curl and HTTP
examples. This removes generated documentation examples, not the separate FUSE
client/project. Remove the obsolete client-list entry along with its tab; do
not delete unrelated protocol or client functionality.

## Source facts that constrain the implementation

- `servers/ruby/lib/haveapi.rb:28` loads the renderer directory.
  `client_example.rb:15` registers classes via `label`; `:57` sorts by `order`.
  Its existing constructor receives host/base URL/API version plus resource and
  action descriptors. Preserve that constructor for existing subclasses.
- `views/version_page.erb:39`, `views/version_page/auth_body.erb:35` and
  `views/version_page/resource_body.erb:107` enumerate the same registry for
  initialization, authentication and action examples. Per-action examples appear
  only where the API supplies structured/prose samples. Do not invent executable
  calls for prose-only or incomplete samples.
- `client_examples/js_client.rb:5` labels JavaScript; `:9` initializes the
  callback client and `:68` renders callback actions. Basic/token/OAuth2 examples
  exist, but syntax checks alone do not prove imports, discovery or calls work.
- `example.rb:63` describes samples as path parameters, request/response,
  status/message/errors/HTTP status. It has **no dedicated example metadata
  field**. Preserve its wire shape and authorization filtering. Do not invent
  metadata values or expand the public example DSL as a hidden prerequisite.
- `server.rb:601` obtains help using the current user/version. The new rendering
  context must use that filtered help, not unfiltered global descriptions.
  `server.rb:242` currently returns an origin-only base URL: new examples must
  explicitly account for the server mount root and selected API version.
- `public/js/highlight.pack.js` is highlight.js **9.8.0**, bundled only with bash,
  HTTP, XML, PHP, JSON, JavaScript and Ruby. `highlighter.js` calls its old
  `highlight(language, source)` API. Go/Rust/Python/TypeScript need actual bundled
  language support and a matching worker API, not just new CSS class names.
- Current `spec/client_examples/syntax_spec.rb` parses JS/PHP/Ruby/curl and
  checks HTTP structure; it does not compile new-client snippets or execute
  their imports/requests. Existing documentation authorization/HTML escaping
  specs remain mandatory regressions.

All paths in this section are relative to `servers/ruby/lib/haveapi` unless
already prefixed. Generator/client paths below are relative to the repository.

## Concrete design recommendation

### Shared server rendering context and UI

Add a small server-owned documentation context, bound through `#with_context`
while retaining old positional constructor calls. It contains selected API
version, mount-aware origin/base, filtered description, and optional generated
client profiles. Compute shared mappings once per HTML request, not once per
example. Do not cache a privileged user's description across requests/users.

Keep the existing registry and tab mechanism; no generic plugin framework.
Use explicit language/mode labels above, stable identifiers for new tabs, logical
ordering, wrapping on narrow screens and a no-JavaScript readable fallback.
Preserve existing action/section anchors and Ruby/PHP/CLI/curl/HTTP ordering.
Render a short explanation in a requested variant's panel when that client
cannot represent a sample; do not show an empty panel or silently drop inputs.

Update the client overview to link maintained repository locations. Explain
that shared HaveAPI package versions differ from generated SDK package versions
and target API versions; the current blanket same-version advice is insufficient
for generated Go/Rust packages. Bundle a maintained, pinned highlighter build
with all retained languages plus Go/Rust/Python/TypeScript, keep its license and
reproducible build instructions, adapt the worker, and safely fall back to plain
text if a language is unavailable. No CDN or production network dependency.

### Dynamic clients: JavaScript, TypeScript and Python

All six dynamic variants are available without server operator configuration.
Share language-family formatting/helpers where behavior is actually common;
keep callback and async control flow distinct.

- JS callback: explicit `CallbackClient` export (the old `Client` alias remains
  valid), discovery/auth completion before action calls, real callback response
  and failure methods. Preserve the existing callback interface.
- JS async: `AsyncClient`, `await setup()`/authentication, explicit
  `resource(name).action(name)` access, `{value, response}` invocation result and
  rejected-error handling. Low-level `request()` results are a different shape;
  do not mix them with dynamic invocation examples.
- TS callback/async: import the **installed `haveapi-client` package**, use
  exported public types and explicit lookup. Do not write `api.someEndpoint`
  as though dynamic discovery generates static endpoint declarations. Avoid
  permissive `any`/casts to hide invalid examples. Reuse the public typed static
  `CallbackClient.findResource` and add `findAction(resource, name): Action`,
  backed by a private null-prototype canonical map. Canonical names win;
  unambiguous aliases resolve; unknown/ambiguous names raise `ProtocolError`.
  Preserve direct properties and `actions: string[]`; no new resource method
  may steal an existing endpoint name. This does not infer endpoint payload types.
- Python sync/async: `Client`/`AsyncClient` context managers, mapping lookup for
  keyword/helper collisions, `.call(params=..., path_params=..., meta=...)`,
  `.data`/`.meta` and package exceptions. Async snippets use `async with`, `await`
  and a complete asyncio wrapper; do not require a framework event loop.
- Authentication panels show only advertised providers. Existing credentials
  use documented Basic/token/OAuth2 APIs; login/continuation examples must use
  real client methods and provider input names, with placeholders/environment
  variables rather than actual credentials. OAuth acquisition is not invented
  for clients supporting existing access tokens only.

Initialization/authentication/action snippets must form a coherent runnable
program, including imports, setup and async ownership. It is acceptable to keep
sections visually separate if a tested complete composition is supplied. Do not
assume the existing callback initialization snippet is already sufficient.

### Generated Go/Rust clients: generator-owned adapters and explicit profiles

**Recommendation:** reuse each generator through a small pure-Ruby documentation
adapter; configure an optional generated-client profile per API version when
an operator wants concrete Go/Rust SDK calls. The server alone does not know a
consumer's Go import path, Rust crate name/version or captured SDK surface.
Do not hard-code `vpsadmin-client` for arbitrary HaveAPI servers.

Use `api.documentation_clients(version, go: ..., rust: ...)` with exact fields
from the frozen contract. Go config has `import_path`, `module_version`,
`description_path`, `generator_version`; use fixed import alias `client`. Rust
has `snapshot_path`, `generator_config_path`, `generator_version`; crate name and
version derive from the existing TOML generator config, parsed with Tomlrb.
Descriptions/snapshots are JSON. Profiles identify actual published SDKs; their
versions are independent of HaveAPI/API versions. All paths/names are trusted
startup configuration, never request parameters. Do not invent published SDK names.

Add adapters inside `clients/go/lib/haveapi/go_client/` and
`clients/rust/lib/haveapi/rust_client/`. They accept already loaded saved schema
and config, return resolved resource/action/input/type/auth capabilities, and
never fetch URLs, write generated source, invoke a formatter or compile code.
The application installs the matching generator gem to enable its profile; the
server keeps these dependencies optional, avoiding a new mandatory compiler or
generator dependency for every API server. Resolve optional adapter availability
at startup, not through repeated package loading in HTML requests.

Without a Go/Rust profile, omit that language's overview entry and every
initialization/authentication/action tab. There is no setup panel. A configured
profile with missing adapter, malformed config or wrong API version fails startup.
If a valid saved SDK lacks an authorized visible action/parameter or cannot
represent a particular sample, show that specific within-tab limitation. A profile is not permission:
never expose additional SDK actions, auth fields, defaults or sample data beyond
the current user's filtered server description. Do not silently build a reduced
schema and recompute names: sibling collisions can change generated names.

Generator-specific contracts:

- **Go:** use `ApiVersion`, `Resource#go_member_name`,
  `Action#go_member_names`, parameter resolved Go types and the existing
  `MemberNameAllocator`/`Utils`; ordinary capitalization is insufficient because
  reserved members, aliases and collisions allocate suffixes/hashes. `ApiVersion`
  accepts an in-memory description and is the no-network adapter construction
  seam; `Generator.new` fetches and must not be used by docs serving.
  Actual calls use `Prepare()`, `SetPathParamInt/String`, `NewInput()`/generated
  setters, then `Call()`. Use `NewInput().SelectParameters()` before setters,
  likewise metadata: a nil selection map otherwise means all fields. Preserve
  omitted versus null/zero/false values using generated nullable setters.
  Object inputs and object/list outputs are supported. General Custom fields
  are skipped (global metadata includes is a string exception); list inputs are
  unsupported. A sample requiring either gets a limitation. Nullable scalar
  outputs are values and cannot distinguish null from zero; do not promise it. Do not
  expand this docs feature into an unapproved client capability rewrite.
- **Rust:** reuse `Snapshot`, `IR`, `Naming` and generator type information.
  Resource components normalize and join with `__`; keywords get suffixes;
  remaining collisions fail. Use resolved ancestor/action path argument order,
  generated setters or `InputValue`/`Vec<Input>` for lists, preserving null/unset.
  Async ends in `.send().await?`; blocking uses the enabled `blocking` feature
  and `.send()?`, with its complete lifecycle outside async runtime threads.
  Named SDK imports and generated modules/types come from the profile/adapter.
  Existing runtime limits (such as GET nested Custom/list input and unsupported
  output namespaces) remain explicit. No server request runs `Generator#generate`.

Saved SDK profiles can legitimately lag the live server while API version stays
the same. Validate that the particular sample's route, layout, parameter types
and nullability match the profile before offering code. Do not reject an entire
profile merely because the live API gained unrelated actions. Provenance checks
tie the adapter mapping to the matching generator/schema; they do not claim a
live server version is identical to a published SDK snapshot.

### Sample fidelity and safety

Use the existing filtered sample as data, never as executable source. Escape
language literals (including URL/path/name/import values and comments) before
the existing HTML escaping. Cover quotes, backslashes, newlines, Unicode,
`</script>`, keyword/helper names, hostile identifiers and nested Custom data.
Preserve ordered path arguments, request namespaces/layouts, omitted/null/false/
zero/empty values and partial association/output semantics. Reject unsupported
values clearly; never silently turn omitted input into defaults or drop fields.

For failed samples generate the actual error/response branch, not invented
successful return values. Output examples may be abbreviated; access only fields
that exist in the sample and are supported by the client. Metadata examples use
advertised schemas and explicit documented values in dedicated fixture/guidance
sections; no new sample wire keys are needed for the first implementation.
Show available metadata/result access without inventing metadata payloads.

Long-running operation support is client-specific: JS async has
`waitForCompletion`; Python exposes `response.operation`; Go generates
`IsBlocking`/operation methods only where supported. Rust exposes metadata and
explicit action-state calls, not an invented high-level wait helper. Call out
that request success/timeout does not establish task completion or undo a server
mutation. Unsupported continuation or waiting behavior gets a clear note.

## Four-implementer execution sequence

The user approved these packages. Read the exact ABI in
[api-doc-contract.md](api-doc-contract.md) before implementation.

| Owner | Exclusive boundaries | Dependencies and acceptance |
| --- | --- | --- |
| implementer0 | Shared context/profile loader, server/base registry, shared ERB templates/overview, File system removal, UI/highlighter, dependency manifests and shared fixture/test orchestration | Publish contract-compatible skeleton first; no-profile Go/Rust absent everywhere, invalid profile startup failure, old constructor calls preserved, retained formats unchanged. Own all shared Git/index/hooks. |
| implementer1 | JS/TS/Python renderer family and private formatting helpers, separate family specs, JS callback helper/types/specs | Use shared context/results; all six variants have real package interfaces. Static typed findAction map preserves canonical names/aliases and bound args. Node package examples may use node:process env; Python uses os.environ. |
| implementer2 | clients/go/lib/haveapi/go_client/documentation.rb, server client_examples/go_client.rb, dedicated Go adapter/renderer/compile fixtures and specs | Reuse pure ApiVersion naming/types; exact profile import/module version; object input/list output, nullable/omission semantics and explicit unsupported cases. |
| implementer3 | clients/rust/lib/haveapi/rust_client/documentation.rb, server client_examples/rust_client.rb containing both variants, dedicated Rust fixtures/specs | Reuse Snapshot/config validation and IR; JSON snapshot/TOML config; async and blocking imports/types/path ordering compile against actual generated package. |

Language owners send shared registry/manifest/runner changes to implementer0.
Use distinct per-language spec files and fixture directories. Pure adapters can
proceed against the frozen interface while the foundation is implemented.
No language package depends on another; assembled tests depend on foundation.
Dynamic TS examples depend on the packaged additive callback helper. Generator
adapters ship in their normal optional gems; standalone server installation
continues without those gems. Lead owns final prose, review and verification.

## Verification and acceptance

The bounded callback/Go/profile questions are resolved in the contract. No
architecture choice remains delegated to implementers; material deviations go
through architect and lead. Tests must consume the frozen fields and verify
real generator/client interfaces, not mirror invented naming rules.

**Quick checks:** Ruby style/unit rendering and adapter tests, old-format golden
or semantic regressions, registry/HTML presence and absence, authorization and
HTML/literal escaping, native JS/Python/shell syntax checks, profile validation,
worker language support and unrecognized-language fallback. Tests must prove
Go/Rust name mapping against the generators rather than mirror copied rules.
Use known short fixtures; delegate uncertain-duration setup/checks to a watcher.

**Commit and independent review next:** all intended changes and quick checks,
whole branch/history plus no-migrations conclusion, docs and package implications.
Do not substitute this planning audit for final review.

**After review, longer checks through a fresh watcher:**

- Render HTML from a disposable real server fixture with mounted root/version,
  nested resources, keyword/collision names, no-input/single/list layouts,
  nullable/Custom values, success/failure, metadata and action-state actions.
  Extract actual rendered code, not a hand-rewritten approximation.
- Install the built npm tarball into an isolated consumer; execute JS callback
  and async snippets and compile both TS variants with `tsc --strict` against
  package exports. No checkout declaration fallback or broad `any` escapes.
- Install Python wheel/sdist into isolated environments; parse/type-check
  applicable snippets and run sync/async examples against the fixture. Verify
  lifecycle, auth and error results, not merely imports.
- Generate a Go fixture module using the same saved profile and real generator;
  `gofmt`, compile/test and execute rendered code, including mapped identifiers,
  omitted/null/zero values and supported auth/state methods.
- Generate a Rust fixture crate from the saved snapshot/config with exact
  formatter; compile/test rendered async and blocking examples, including the
  declared MSRV, package dependencies and blocking lifecycle. Keep generated
  files generator-owned. Compile checks must catch wrong crate/type/method names.
- Verify token challenge examples with a deterministic disposable provider only
  where supported; never contact production or use real credentials. Exercise
  safe rendering for unsupported sample capabilities.
- Check narrow-screen tabs, keyboard/no-JavaScript access, all syntax languages,
  packaged server docs/assets and retained Ruby/PHP/CLI/curl/HTTP behavior.

Every requested variant must have initialization, applicable authentication,
success/failure and representative request/response coverage. Each limitation
must be visible and tested. Distinguish fixture-backed execution evidence from
prose/example presence; a syntax-only pass is insufficient.

## Compatibility, release and recovery

No database, on-disk application state or wire-protocol migration is intended.
Old clients continue working. File system examples disappear by explicit user
choice; all other existing formats and public renderer extension calls remain.
Server startup/docs continue without optional Go/Rust profiles or generator gems.
No production JS execution of examples, server-side network acquisition, Cargo/
Go compiler installation or write to generated clients occurs on a docs request.

Implement on the lead-selected initiative branch under the user's approval. Reconcile reviewed release
candidate and new scope explicitly; do not silently append unreviewed changes
to a completed release. Follow source → quick checks → commits → final review →
longer verification → explicit integration/release approval. The retained release baseline is unpublished; final history consolidation must
leave the release commit message exactly `Version 0.30.0`. Never alter published
tags/artifacts; any later publication remains separately authorized.

Deployment updates the Ruby server gem and, for concrete generated-client tabs,
matching optional generator gems/profiles. Operators need no coordinated node
upgrade. Rollback restores the previous server/docs assets and profile setup;
it does not remove installed SDKs or reverse API actions users ran from examples.
