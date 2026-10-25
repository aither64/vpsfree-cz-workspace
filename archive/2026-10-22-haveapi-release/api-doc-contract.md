# Approved API documentation implementation contract

User approved implementation on 2026-10-22. This contract supersedes provisional
interfaces in the examples plan. Architect owns this record; application changes
belong to the four implementers. Baseline: HaveAPI `08345b2` (FS removal may follow).

## Context and renderer ABI — implementer0

Define `HaveAPI::ClientExample::Context` in `haveapi/documentation_context.rb`.
`Context.new(version:, host:, base_url:, version_url:, description:,
resource_path: [], resource: nil, action_name: nil, action: nil, sample: nil,
profile: nil)`. Readers have those exact names. `#with(**changes)` returns a new
context. Deep-copy/freeze data containers, not global server descriptions.

- `version`, `host`, `base_url`, `version_url`: Strings. `host` preserves the old
  renderer argument. `base_url` is origin plus mounted API root with trailing
  slash; `version_url` additionally includes the selected `vVERSION/` segment.
- `description`: current user's filtered version-description Hash, retaining
  existing key conventions. `resource_path`: ordered Array<String> of canonical
  names; `resource`/`action`: authorized descriptor Hash or nil;
  `action_name`: canonical String or nil. `sample`: existing filtered structured
  example Hash or nil (no new example protocol keys).
- `profile`: selected immutable Go/Rust profile or nil. It exposes `language`
  (Symbol), `package_name`, `package_version` (Strings), `adapter` (opaque object).
  Go package_name is its import path; Rust is Cargo crate_name. Full saved schema,
  filesystem paths and generator config remain private inside profile/adapter.

Keep the existing positional renderer constructor and `init`, `auth(method,
desc)`, `example(sample)` callable unchanged. Add `#with_context(context)` returning
self and `attr_reader :context`, avoiding constructor keywords for old subclasses.
Class `.render(kind, context:, auth_method: nil, auth_description: nil)` constructs
using the old positional arguments, binds context, then invokes those methods.
Kinds are `:init`, `:auth`, `:example`. New renderers may return result hashes;
legacy String results are wrapped centrally. Legacy nil means no legacy panel.

Results are frozen plain Hashes: `{status: :code, code: String}` or
`{status: :limitation, reason: String}`. Text is unescaped source/plain prose;
templates escape HTML once. Never return HTML or silently drop unsupported data.
New renderer methods always return one of these two results.
Class `.available?(context)` returns Boolean: dynamic and legacy formats true;
Go/Rust true only for the matching configured profile. Apply before overview,
initialization, authentication and action tabs. No profile => completely hidden.
Configured unsupported sample => limitation panel. Invalid config => startup error.

## Profile configuration and adapter ABI

`api.documentation_clients(version, go: nil, rust: nil)` runs before `api.mount`.
Go exact keys: `import_path`, `module_version`, `description_path`,
`generator_version`. Rust exact keys: `snapshot_path`, `generator_config_path`,
`generator_version`. All values are nonempty Strings. Paths are trusted absolute
local files. Go description and Rust snapshot use JSON; Rust config uses existing
TOML (`Tomlrb.load_file`). Rust package fields derive from config, not duplicate
server settings. Use explicit Go import alias `client`.

Registration rejects unknown keys/languages, duplicate version/language, malformed
files/import/version values, missing adapter, mismatched installed generator
version, invalid schema/config. At mount reject unselected API versions and Rust
snapshot API-version mismatch. Go raw description's version binding is the
configuration key plus retained published SDK fixture; do not invent an embedded
version check. Freeze loaded profiles; never read files/fetch/generate on requests.
No mandatory generator dependencies in the server gem.

Generator-owned classes: `HaveAPI::GoClient::Documentation` and
`HaveAPI::RustClient::Documentation`, in each generator's `documentation.rb`.
Go `.new(description:, import_path:, module_version:)` uses pure `ApiVersion`.
Rust `.new(snapshot:, config:)` reuses Snapshot/Generator validation and IR;
never call generate. Loader checks generator_version before construction.
Both implement `#resolve(resource_path:, action_name:)` returning an opaque
resolved action handle or nil and `#render(kind:, context:, mode:,
auth_method: nil, auth_description: nil)` returning the result Hash above.
Modes: Go `:sync`; Rust `:async`/`:blocking`. Render resolves internally, checks
the authorized context against saved schema, and emits only that sample's data.
No adapter may require the server gem; context is consumed through its readers.

## Stable variants and ownership

| ID | Label | order | highlight | Owner |
| --- | --- | ---: | --- | --- |
| javascript-callback | JavaScript (callback) | 10 | javascript | implementer1 |
| javascript-async | JavaScript (async) | 11 | javascript | implementer1 |
| typescript-callback | TypeScript (callback) | 12 | typescript | implementer1 |
| typescript-async | TypeScript (async) | 13 | typescript | implementer1 |
| python-sync | Python (sync) | 14 | python | implementer1 |
| python-async | Python (async) | 15 | python | implementer1 |
| go | Go | 16 | go | implementer2 |
| rust-async | Rust (async) | 17 | rust | implementer3 |
| rust-blocking | Rust (blocking) | 18 | rust | implementer3 |

Add class `.id(value = nil)`; retained formats keep their existing IDs/anchors,
labels, relative ordering and code languages. UI IDs use variant ID, not grammar.
impl0 owns base/context/profile loader, server wiring, registry, shared templates,
overview/FS removal, UI/highlighter, manifests and shared fixtures/test runners.
impl1 owns dynamic renderer files/helpers and separate language specs, plus JS
callback helper/types/specs. Node package examples may use `node:process` env;
request Node test declarations through impl0. Preserve browser client behavior.
impl2 owns Go documentation.rb, server go_client.rb and Go-only fixtures/specs.
impl3 owns Rust documentation.rb, server rust_client.rb (both variants) and
Rust-only fixtures/specs. Shared-file edits and all Git/index/hooks go through
impl0; each owner supplies commands/dependencies rather than editing shared files.

## Fixed capability and verification rules

Callback `ClientConstructor.findAction(resource: BaseResource, name: string):
Action` uses a private null-prototype canonical map; canonical names win, aliases
resolve only unambiguously. Unknown/ambiguous lookup raises ProtocolError. Keep
direct property attachment and actions:string[] unchanged; use existing typed
findResource. No endpoint-specific inference or any/private-property escapes.
Go supports object inputs, object/list outputs and existing nullable setters.
Call `NewInput().SelectParameters()` before setters to preserve omission, likewise
metadata. General Custom and list inputs get limitations (global includes has
its existing string exception). Scalar nullable outputs cannot distinguish null
from zero; don't promise otherwise. Dynamic list-input limitations must reflect
actual client support, not fabricated calls.

Quick unit/rendering/style/syntax/typed-helper checks precede commits and mandatory
final independent review. After review run extracted rendered snippets against
installed npm/Python packages and pinned generated Go/Rust fixtures: strict TS,
Go compile/run, Rust async/blocking compile/run and full server packaging/HTML
checks through the verification watcher. Check auth, mount/version, hostile
literals/names, metadata/state, omission/null/false/zero, profile visibility,
unsupported samples and all retained formats. No DB/protocol/state migrations.
Lead owns final prose/review/verification and history consolidation; final release
commit message remains exactly `Version 0.30.0`. No publishing/default integration.
