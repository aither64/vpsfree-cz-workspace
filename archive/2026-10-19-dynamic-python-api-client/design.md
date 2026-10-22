# Dynamic Python HaveAPI client: implementation brief

Status: accepted for implementation on 2026-10-19, as relayed by the lead.
Python 3.11+ is the accepted baseline assumption. Application implementation and
verification are assigned by the lead; this document does not claim they passed.
This brief grants no merge or release authority; later approvals and outcomes
are recorded in session state. The original investigation is retained below;
concrete contracts in the implementation section resolve its open API
details and take precedence over illustrative prose.

Implementation worktree:
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-19-dynamic-python-api-client/haveapi`,
initial HaveAPI revision `c58704a08451a231fdf6c6123437133422af46dc`.

## Dependency refresh amendment: native Ruby 3.4 shell

Status: accepted by the lead with the narrowed verification below. The approved
refresh targets certifi `2026.10.19`, Ruff
`0.17.1` and the existing nixpkgs updater. This amendment changes development
tool selection only; it grants no runtime/package deployment or release.
Implementer1 retains all application/Git ownership under claim
`342cd062-0205-45c7-b636-20d958b8fa75`; architect edits this record only.

**Verified cause and compatibility.** The updater at HaveAPI `c1823f3` changed
only `flake.lock`, from nixpkgs `fe13242281a67641c0102cdb1087f0ebe586c7df`
to `02c087f3fe673c9e317f206a627cb6b910336dbe`, then failed in `nix flake check`
before staging or committing. The selected input removes `ruby_3_3` during
Nixpkgs 26.11's support cycle (`pkgs/top-level/aliases.nix:2351`). See
[observer evidence](verification/dependency-refresh/observer-result.md) and its
linked log. This was attribute evaluation failure, not a Ruby test failure.

Implementer1's read-only evaluation of that exact input reports Ruby `3.4.11`,
uv `0.13.1` and Ruff `0.17.1`; the inspected store source also confirms the
Ruff/uv versions. HaveAPI's `.ruby-version` is `3.2.0`: server and Go-generator
gemspecs use it as a minimum; Ruby client requires `>=3.0`. No inspected Gemfile
pins Ruby 3.3. Installed Bundler 4.0.23 requires Ruby >=3.2; Overcommit 0.73.0,
RuboCop 1.85.1, Prism 1.9.0 and BigDecimal 4.1.3 metadata permit Ruby 3.4.
The existing shared RSpec workflow already includes 3.2, 3.3 and 3.4. These are
compatibility constraints, not evidence of this refreshed shell passing tests.

The unchanged vpsAdmin reference at `fb2f51222503a45f2e5a42af505f719e44279ed0`
selects `pkgs.ruby_3_4` in its API shell (`flake.nix:403,520`). Its actual API
checks against released HaveAPI 0.29.12 have passed in this session; see
[verification summary](verification-summary.md). The released HaveAPI tag also
declares Ruby >=3.2. That is useful Ruby-3.4 precedent, not proof for the newly
selected nixpkgs revision or a newly refreshed Python environment.

**Smallest change and invariants.** In `flake.nix`, replace exactly three
`ruby_3_3` selections with explicit `ruby_3_4`: the `rubyShell` default argument,
root development-shell package list, and `client-python` package list. The helper
covers server, Ruby client, Go-generator and ActiveRecord-example shells. Preserve
their names, environment contracts, dependency initialization, native Nix tools
and existing Overcommit checks/signatures. Choose explicit 3.4 rather than the
moving `pkgs.ruby` alias. No overlays, wrappers, compatibility aliases, alternate
channel pins, updater framework or workspace-runtime edits.

The already approved Python refresh owns `clients/python/pyproject.toml`'s exact
Ruff pin and `clients/python/uv.lock`'s Ruff/certifi resolution. Retain the existing
Ruff entrypoint and require native Ruff's version to equal the lock. Keep
Python >=3.11, `uv_build>=0.13.0,<0.14`, public dependency ranges, shared VERSION,
protocol/authentication behavior, wheel/sdist metadata and build-once release
policy unchanged. uv 0.13.1 remains inside the accepted backend range. certifi's
new CA bundle is the intended TLS-trust-data change; no certificate bypass is
introduced. No `.ruby-version`, gemspec, CI-matrix or action-version edit is
needed for native Nix Ruby selection. Existing non-Nix Python/JS/PHP server jobs
continue using Ruby 3.3, preserving that compatibility exercise.

**Environment and updater recovery.** The old shell used Ruby 3.3 and the shared
session checkout's `.gems` contains native extensions for that ABI. Enter the
new native shell using its ordinary declared `GEM_HOME` and let normal Bundler
installation supply/rebuild Ruby-3.4 extensions;
do not treat presence of old gems or a prior `bundle check` as successful setup.
Inspect ABI/load failures before any scoped cache repair; do not delete shared
or unrelated caches or update unrelated gems speculatively. Record unexpected
Gemfile.lock changes and resolve them with the lead before expanding scope.
The lead selected ordinary declared gem paths for setup and checks. The proposed
isolated `.gems/ruby-3.4` path override is not adopted. Diagnose specific extension
failures before targeted repair; keep hooks, checks and developer use on the same
declared environment.

The updater refuses a dirty `flake.lock`, so blind rerun is not a continuation.
Preserve the exact failed generated lock and evidence. With the three-attribute
correction accepted, the lead/owner coordinates completion of the
existing updater's remaining flake-check and scoped commit sequence, with its
required `flake: nixpkgs <oldrev11> -> <newrev11>` subject. Keep the shell source
adjustment reviewable and preserve unrelated changes. Do not modify the script,
reset the lock merely to repeat it, or bypass hooks. Commit ordering and any
required source-diff review remain with the lead and implementer1.

**Focused acceptance/check plan (not executed by architect).**

- Evaluate `nix flake check --all-systems --no-build` for both declared Linux
  architectures, then complete the updater's normal `nix flake check`. Evaluation
  is not evidence that a shell or native gem loads. Prepare the affected native
  shells through their existing entrypoints and record Ruby, uv and Ruff versions.
  Long or uncertain setup/checks use a fresh policy watcher.
- After setup, check root/server/client/Go Bundler environments and ordinary
  Overcommit loading under Ruby 3.4; verify the Python shell sees the same native
  Ruby/Ruff selection. Run `clients/python/utils/check.sh` and the existing native
  hooks. Inspect the final lock diff for the intended dependency changes.
- After quick checks, committed changes and the required affected-lane independent
  review, run `make doc` and the Ruby server/client/Go RSpec suites in their
  component environments, Python `uv run --locked pytest tests/integration`,
  `uv run --locked python utils/package_smoke.py`, and root
  `make release-check release-test`. These exercise native gems, the real Ruby
  server, Python wire behavior, standalone packaging and Ruby release helpers.
  They do not authorize publishing. Use existing harnesses; add no mirror tests
  for the three literal attribute changes.
- Verify the refreshed Python environment reports the intended certifi version
  and can load `certifi.where()` into a standard verifying SSL context. Per the
  lead's bounded no-repeat disposition, retain the completed vpsAdmin API evidence
  without rerunning that bridge: its shell, pin and authentication code are
  unchanged. Reconsider only if a concrete compatibility failure emerges. No
  vpsAdmin source/pin change, node VM or production access.
- Observe applicable exact-head CI, including its Ruby 3.3 server integration
  and existing Ruby 3.4 matrix lane. The flake-only change may not trigger every
  Ruby workflow, so local Ruby-3.4 suite evidence is still required. Any newly
  exposed removed Nix attribute, native-gem failure or formatting change is a
  diagnosed follow-up through the lead, not permission for a broad tool upgrade.

**Rollback and deployment.** There is no schema, persisted API state, node or
workspace-runtime migration. Before publication, the owner can return only the
owned dependency-refresh edits to the recorded pre-refresh state if the lead
abandons this refresh; preserve evidence and unrelated content. After integration,
use ordinary reviewed revert commits rather than rewriting master. Restore a
coherent prior nixpkgs/Ruff/lock combination: old Ruby 3.3 cannot be selected from
the new pin, and native Ruff must still match the Python lock. Native extensions
must match whichever Ruby is selected. No deployment ordering or production
rollback is introduced; build artifacts from the prior toolchain remain distinct
from newly verified artifacts. The held claim is managed by the lead, not this
design amendment.

## Implementation contracts (A/B/C/D)

These interfaces are the coordination boundary. Implementers may choose private
helpers freely; changes to names/signatures or behavior below go through the
architect and lead before a dependent package adopts them. Paths are relative to
`clients/python`. All examples describe intended interfaces, not existing code.

### Ownership and import direction

- **implementer0 / A then D** owns `src/haveapi_client/_protocol/**`,
  `exceptions.py`, `response.py`, `pagination.py`, `operations.py` and tests in
  `tests/unit/{protocol,response,pagination,operations}/`.
- **implementer1 / B then release E** owns `pyproject.toml`, `uv.lock`,
  `src/haveapi_client/__init__.py`, `py.typed`, package license, check scripts,
  Nix/Overcommit/GitHub workflow/release integration and initial shared fixture
  harness. This owner alone edits root files and sets up hooks. Git operations
  remain serialized by the lead. Package imports may initially be minimal;
  do not import unfinished modules merely to stub an export.
- **implementer2 / C** owns `client.py`, `async_client.py`, `_auth/**`,
  `_transport/**`, `_resources/**`, and `tests/unit/{client,auth,resources}/`.
- **implementer3 / bounded follow-up** can own an explicitly assigned fixture or
  example file after the interface settles. Preserve this member's retained low
  effort; do not assign the substantive D design/implementation or change settings.
  The lead assigns exact files, keeping them disjoint from the harness/docs owner.

A defines protocol models and executor Protocols, never imports HTTPX, C modules,
or D at runtime. `_protocol/execution.py` imports D's Response only under
`TYPE_CHECKING` with postponed annotations. C imports A and D; D imports A and
calls the executor/resource factory instead of importing C. Each owner controls
their subpackage `__init__.py`; only B edits the top-level export file. Tests
import owning modules while waiting for B to add public re-exports.

### A: immutable description and wire core

Use frozen dataclasses with defensive copies/read-only nested collections for
description and request state. Preserve unknown extension fields in `.raw`.
Canonical models exported from `haveapi_client._protocol`:

| Model | Required fields |
| --- | --- |
| `ParameterSpec` | `name: str`, `type: str`, `required: bool`, `nullable: bool`, `raw: Mapping[str, object]`; absence/default/validators/association metadata remain distinguishable in `raw` |
| `LayoutSpec` | `layout: str`, `namespace: str | None`, `parameters: Mapping[str, ParameterSpec]`, `raw` |
| `ActionSpec` | `name: str`, `resource_path: tuple[str, ...]`, `method: str`, `path: str`, `path_parameters: tuple[str, ...]` in template order, `aliases: tuple[str, ...]`, `input: LayoutSpec | None`, `output: LayoutSpec | None`, `meta: Mapping[str, object]`, `blocking: bool`, `auth: bool`, `raw` |
| `ResourceSpec` | `name: str`, `resource_path: tuple[str, ...]`, `resources: Mapping[str, ResourceSpec]`, `actions: Mapping[str, ActionSpec]` keyed by canonical names, `raw` |
| `Description` | `protocol_version: str`, `api_version: str | None` (None when default identifier is not reported), `resources`, `authentication: Mapping[str, Mapping[str, object]]`, `meta_namespace: str`, `raw` |
| `RequestSpec` | `method: str`, `url: str` (resolved/validated absolute URL without assembled query), `query: tuple[tuple[str, str], ...]`, `headers: Mapping[str, str]`, `content: bytes | None` |
| `WireResponse` | `status_code: int`, `headers: Mapping[str, str]`, `content: bytes` |
| `DecodedResponse` | `data: object`, `meta: Mapping[str, object]`, `envelope: Mapping[str, object]`, `status_code: int`, `headers: Mapping[str, str]`; successful envelope only |
| `CallContext` | `action: ActionSpec`, `bound_args: tuple[str | int, ...]`, `path_params: Mapping[str, str | int]`, `generation: int`; copied immutable invocation binding |
| `RequestOptions` | `timeout: float | None = None`; None inherits the client's finite timeout, positive values override it for this request |

Keep raw secrets/body values out of default dataclass repr; a read-only mapping
does not itself provide redaction. Python `bool` is not an accepted path integer.

Required shared type aliases, exported by `_protocol/__init__.py`:
`InputObject = Mapping[str, object]` and
`InputParams = InputObject | Sequence[InputObject]` (from `collections.abc`).
This 2026-10-19 clarification corrects the initial Mapping-only signatures to
honor existing `object_list`/`hash_list` **input** layouts, as requested by the
lead and A owner. It adds no dependency. `coerce_input` returns a mapping for
object/hash input and a sequence of independently validated/coerced row mappings
for object_list/hash_list. Strings/bytes and mixed/non-mapping rows are rejected.
An empty list is an explicit list input, distinct from omitted input; metadata
remains separate from rows. Custom parameter types preserve JSON-compatible
values (reject unsupported Python objects and non-finite numbers); do not apply
scalar coercion to an unknown/custom type. A false/missing namespace normalizes
to None and means no invented namespace wrapper, not absent input/output.

Required pure entry points, exported by `_protocol/__init__.py`:

```python
parse_description(
    envelope: Mapping[str, object], *, api_version: str | None = None
) -> Description
parse_resources(
    raw: Mapping[str, object], *, parent_path: tuple[str, ...] = ()
) -> Mapping[str, ResourceSpec]
lookup_resource(description: Description, path: tuple[str, ...]) -> ResourceSpec
lookup_action(
    description: Description, resource_path: tuple[str, ...], name: str
) -> ActionSpec
coerce_input(
    layout: LayoutSpec | None, params: InputParams | None
) -> InputParams
build_request(
    description: Description, context: CallContext, *, base_url: str,
    params: InputParams | None = None,
    meta: Mapping[str, object] | None = None,
) -> RequestSpec
decode_envelope(response: WireResponse) -> Mapping[str, object]
decode_response(
    description: Description, action: ActionSpec, response: WireResponse
) -> DecodedResponse
```

`parse_description` handles a single-version description envelope, as returned
by default/explicit-version discovery; it validates protocol major 2. Whole-API
`versions`/`default_version` selection belongs to C if offered, not this parser.
`parse_resources` is also used for authentication-provider resource trees.
`lookup_action` accepts exact canonical names and unambiguous aliases. Canonical
names win alias conflicts; multiple aliases with no exact name raise a clear
lookup error. Unknown metadata extensions are preserved; malformed mandatory
structures fail as ProtocolError.

`build_request` performs coercion, metadata encoding, template substitution and
same-origin URL validation. Positional bound_args fill placeholders left-to-right;
named path_params supply remaining placeholders or must equal an already-bound
value. Reject extras, missing bindings and conflicts. Percent-encode each value
once, preserving the configured API mount prefix (a leading slash in an action
path is API-relative). Reject external URLs, scheme-relative paths and traversal;
never let URL joining discard the mount prefix. Credentials are absent here and
are added by C only after destination validation. GET encodes only the representable bracket-query subset specified below;
POST/PUT/DELETE use UTF-8 JSON and Content-Type. DELETE is a body method in the
current Ruby server and released 0.29.12; legacy Ruby client query behavior is not
authoritative. Other methods must fail clearly until their encoding is deliberately
supported. Absent input rejects nonempty params; no guessed default injection.
Input nullability and scalar coercion follow the existing typed-input document.

`decode_envelope` parses JSON and checks HTTP status and boolean envelope status;
both failing HTTP and status=false are errors, preserving message/errors where
available. A valid 2xx status=false is ActionError, not success. Non-JSON or bad
envelope shapes are ProtocolError with HTTP context. `decode_response` extracts
the declared output namespace and global metadata; absent output yields None.
It validates layout/container shape but does not create bound ResourceObjects.

Central exceptions owned by A: `HaveAPIError`, `ProtocolError`, `TransportError`,
`AuthenticationError`, `ValidationError`, `ActionError`, `NotConnectedError`,
`StaleDescriptionError`, `PaginationError`, `OperationFailedError`,
`OperationTimeoutError`. Error context supports `status_code`, `message`,
`errors: Mapping[str, object]` and redacted envelope inspection. Type validation
reports field errors; HTTP 401 maps to AuthenticationError; 403/404 remain
ActionError with status. Operation failure does not masquerade as transport error.

### GET representability and DELETE correction (2026-10-20 review decision)

The initial GET/DELETE query contract copied a legacy client's behavior and was
wrong for the authoritative Ruby server. `servers/ruby/lib/haveapi/server.rb`
uses `body_method = !%i[get head options].include?(...)` and selects parsed JSON
for body methods, identically in the implementation base and tag v0.29.12.
DELETE therefore shares POST/PUT JSON construction, including input namespace and
metadata. Do not change the described method or server to work around encoding.
JSON root must be an object under that server's explicit check; reject an
unnamespaced list body locally. Namespaced list JSON remains supported.

A owns the GET representability check after coercion and before flattening;
C owns preserving ordered query pairs when passing them to HTTPX. These are
separate fixes. GET permits only structures known to round-trip through Rack:

- Described typed scalar leaves use the existing canonical coercion and nullable
  empty-value representation. No change to Integer/Boolean/etc wire conventions.
- Nonempty mappings can nest, with nonempty bracket-free string key components.
  Reject literal `[` or `]` in namespace/parameter/custom keys; percent encoding
  does not make these literal because Rack decodes before applying bracket grammar.
- Nonempty arrays of scalar strings preserve array order. Nonempty dense arrays
  of flat objects are also allowed if every row has exactly the same nonempty
  key set and no container-valued field. Emit every row in the same deterministic
  key order. For described object_list/hash_list rows, scalar types are restored
  by their ParameterSpecs. For Custom arrays of objects, leaves must be strings.
- Reject sparse/different-key rows, empty rows, nested arrays, and arrays with
  container-valued fields outside the flat dense-row whitelist. Do not insert
  null/default fields or sentinel keys to create row delimiters.
- Custom data has no declared nested coercion schema: only string leaves can be
  preserved in a GET query. Reject numeric, boolean and null leaves in nested
  Custom values instead of changing them to strings. A top-level nullable Custom
  None follows Typed.clean's documented nullable empty-value behavior; that does
  not authorize nested null conversion. No JSON-stringification fallback.
- Explicit empty Custom mappings/lists at any depth and explicit empty list input
  cannot be represented and raise ValidationError. Missing params stays omitted;
  empty structural object/meta wrappers with no supplied fields may emit no pairs.
  Empty row objects in a supplied list are not structural wrappers and reject.

The same check covers global/object metadata as action input. Report an actionable
ValidationError with the field/index path before sending any HTTP request. Keep
POST/PUT/DELETE JSON behavior unchanged for representable namespaced payloads:
empty containers, sparse rows and finite Custom booleans/numbers/nulls are retained.
The public README must explain that all layouts have JSON support while GET has
this explicit subset; users cannot choose JSON for an action declared GET.

Evidence: a known-quick read-only Ruby experiment loaded the checkout's installed
Rack 3.2.7 query_parser and URI-encoded ordered pairs. Results:
`x[][a]=1&x[][b]=2` becomes one row `{a: "1", b: "2"}`;
`x[][a]=1&x[][b]=2&x[][a]=3&x[][b]=4` preserves two dense rows;
`x[0][a]=1&x[1][b]=2` becomes a mapping with string numeric keys;
`x[]=` becomes `[""]`, not `[]`; `x[][]=a&x[][]=b` becomes two singleton
arrays, not one two-element nested array. `parameters/typed.rb:clean` returns
Custom raw values after optional top-level null handling, so no generic numeric
or boolean recovery exists. No server or client integration suite was run for
this decision, and application source remained frozen.

Required regressions: accepted dense flat rows with differing caller key order;
sparse/different-key rows and nested/empty structures rejected locally; scalar
string array order; typed nullable scalar; Custom nested numeric/bool/null and
ambiguous keys rejected; omission remains omission; exact JSON preserves these
values in POST/PUT/DELETE. Both transports must preserve the complete pair sequence
as encoded query bytes instead of regrouping repeated names through HTTPX params.
Add actual generic-server GET dense-row and DELETE input+metadata cases; run after
review under the verification gate. Rerun affected core, transport, API and docs
review lanes once final corrections are committed and quick checks pass.

### Shared executor contract: C implements, D consumes

`_protocol/execution.py` exports `SyncExecutor` and `AsyncExecutor` Protocols.
Both expose read-only `description: Description` and `generation: int` plus:

```python
resource(
    path: tuple[str, ...], *, bound_args: tuple[str | int, ...] = (),
    path_params: Mapping[str, str | int] | None = None,
) -> Any  # dynamic resource proxy; navigation only, no I/O

# SyncExecutor:
execute(
    context: CallContext, *, params: InputParams | None = None,
    meta: Mapping[str, object] | None = None,
    options: RequestOptions | None = None,
) -> Response[Any]

# AsyncExecutor: identical arguments, declared async def, awaitable Response[Any].
```

C may implement these directly on Client/AsyncClient or on a private adapter.
`execute` checks context.generation before any request, calls A to build/decode,
and D to adapt output. It is the sole action execution path, including auth
actions (whose ActionSpec can come from a separate parsed provider tree).
Transport adapters expose `send(RequestSpec, *, options) -> WireResponse` and
async equivalent. They map HTTPX failures to TransportError and never implement
HaveAPI envelope behavior. C owns connection, timeouts, authentication headers,
redirect policy and transport lifetime. Authentication bootstrap can use the
same pure request/decode functions before a public client is connected.

Generation increments when a new description/identity is installed or invalidated.
Resource and action proxies carry their original generation; stale calls fail
before network I/O rather than executing under a newly changed identity. Explicit
refresh invalidates old proxies; users obtain fresh proxies from the client.
Refresh/auth mutation and active requests must not install/send a mixture of
old description and new credentials. Concurrent ordinary calls have independent
bindings; serialize auth changes (or reject them while calls are active).

### C: public clients, discovery, authentication and facade

Public constructors:
`Client(base_url, *, version=None, auth=None, timeout=30.0, language=None,
http_client=None)` and AsyncClient with corresponding HTTPX client type. Validate
positive finite timeout. Owned clients close on context exit; injected clients
remain caller-owned. `connect() -> Self`, `refresh_description() -> Description`,
`close() -> None`; AsyncClient provides async connect/refresh and `aclose()`.
Context entry connects; construction/navigation never performs I/O.

`connect` uses OPTIONS default or selected version, obtains auth description,
then authenticates with configured BasicAuth/TokenAuth/OAuth2Auth and installs
the authorized description. Do not put username/password login in the constructor:
explicit `begin_token_login(params)` obtains/uses public provider description and
returns `Authenticated` or `AuthenticationChallenge`; async returns corresponding
AsyncAuthenticationChallenge. This resolves the earlier ambiguous connect/challenge
proposal. Successful begin/submit atomically installs final credentials and an
authorized description. Challenge fields are next_action, input ParameterSpecs
and validity; submit(params) executes only that next described action and adds
the private continuation token. Never send a continuation token as normal API
credentials. Unknown steps are supported as described actions, not auto-prompted.

`BasicAuth(username, password)`, `TokenAuth(token)` and `OAuth2Auth(access_token)`
live in `_auth` and hide secrets in repr. Basic necessarily retains credentials
for HTTP Basic requests; the earlier no-retained-password rule applies to
password-to-token login, not BasicAuth. Plugin interface: `AuthProvider.method`
and `headers(description) -> Mapping[str, str]`; adapters validate returned
header names/values and reject overrides of routing/framing headers. Token uses
the advertised validated header; OAuth2 uses Bearer authorization. `set_auth(auth)`
invalidates old state, then reconnects; `logout()` clears local auth and obtains
public discovery. `renew_token()`/`revoke_token()` are explicit remote operations;
revoke clears local auth on confirmed success. Close does not revoke anything.

Final-review refactor boundary (2026-10-20): centralize duplicated continuation
policy in existing ClientState, without a new framework or public API.
`_prepare_challenge(description, next_action) -> (fields, nonce)` resolves the
advertised token action, requires its token input, excludes that field from the
public challenge fields, then creates/installs a fresh nonce only after validation.
`_continuation_params(nonce, token, values) -> Mapping[str, object]` checks current
nonce identity, rejects caller-supplied token, and returns a fresh copy with the
private token. Both helpers perform no I/O and run inside the existing `_mutation`
reservation (the first is stateful because it installs the nonce).
Keep `_login_result` shared; sync/async wrappers retain execution/await and their
typed challenge construction. Preserve explicit failed-step retry semantics and
invalidate old challenge nonces on progress, connect/logout/identity invalidation.
Paired tests cover missing described token input, token override and stale
challenges after progress/connect/logout. Source changes still require the lead's
release of the review freeze.

Resources expose `.resources` and `.actions` exact-name maps and dot shortcuts;
`resource[id]` adds one immutable positional path binding, nested navigation
retains parent bindings. `action(**params)` calls
`action.call(params=params)`. `.call(*, params=None, meta=None, path_params=None,
options=None)` accepts InputParams, combines bindings and invokes executor.
The `action(**kwargs)` shorthand remains mapping-only; list-layout input uses
explicit `.call(params=[{...}, {...}])`. Apply the same InputParams annotation
in core, SyncExecutor, AsyncExecutor, action proxies and auth executor plumbing;
auth challenge submissions remain mappings because their described layout is
hash. Paging helpers accept mapping filters only, since their cursor/limit
strategy cannot update a row-list payload. No positional action
arguments in v1; bind IDs on resource proxies or pass named path_params. Facade
delegates paging to D's `iter_pages`/`iter_all`, with the same names on action
proxies; Async variants return async iterators without a leading await.

### D: response adaptation, paging and operations

`response.py` exports `Response[T]`, `ResourceObject` and adapter functions
`adapt_response(decoded, context, executor: SyncExecutor) -> Response[Any]` and
`adapt_async_response(decoded, context, executor: AsyncExecutor) -> Response[Any]`.
Both are synchronous **pure adaptation** functions; the latter creates async
bindings but performs no I/O. Response fields: data, meta, status_code, headers,
envelope, operation (`Operation | AsyncOperation | None`). `ResourceObject` is
a read-only field Mapping with attribute convenience, `.meta`, and `.resource`
resolved through executor.resource. Fields, metadata and the binding are kept
separate. Association `.fetch()` is explicit and has the owning executor's sync
or async semantics; unresolved identity/path means a clear local error.

Keep hash layouts ordinary data. Use per-object metadata path_params when present;
otherwise bind only identities established unambiguously by current context and
the described show path. Do not invent missing parent IDs. Response metadata and
original payload must remain inspectable even when operation tracking is present.

`pagination.py` exports `IdCursor(parameter="from_id", field="id",
direction="asc")` and `CursorStrategy` with
`next_cursor(page: Response[Any], previous: object | None) -> object | None`.
The strategy also exposes `.parameter: str`; empty page returns None to finish.
Provide `iter_pages(executor, context, *, strategy, page_size=100, params=None,
meta=None, options=None)` and `iter_all(...)`; async equivalents are named
`aiter_pages`/`aiter_all`. Every page is a Response; iter_all yields its items.
An initial cursor comes from params[strategy.parameter]. Require described
limit/cursor inputs, positive page size, explicit strategy and object-list/hash-list
output; preserve filters, detect repetition/nonprogress, never infer direction.

`operations.py` exports `Operation`/`AsyncOperation` bound to executor, generation
and action_state_id. Methods: `show() -> Response[Any]`,
`wait(*, timeout=300.0, interval=1.0) -> Response[Any]`,
`cancel() -> Response[Any]`, async equivalents awaited. Wait uses a monotonic
deadline and finite per-request timeout no greater than remaining time, returns
the terminal state response only on finished=true/status=true, raises
OperationFailedError for terminal false status and OperationTimeoutError with
operation ID when deadline expires. A simple interruptible show/sleep loop is
valid initially; poll optimization may follow using its described timeout fields.
No automatic server cancel on timeout/coroutine cancellation. Explicit cancel
checks advertised capability and current can_cancel; its returned response may
itself carry a new operation. Do not auto-wait recursively. AnyIO is a declared
runtime dependency if used for async sleep/cancellation.

Wait deadline clarification: if execute raises TransportError, re-check the
monotonic deadline. Preserve that error before expiry; after expiry raise
OperationTimeoutError with the transport error chained as its cause. In async
wait, bound each awaited execute with `anyio.fail_after(remaining)` as well as
RequestOptions. Translate only expiration of that specific cancel scope (check
its `cancelled_caught`), not a foreign TimeoutError or outer cancellation.
Neither path automatically cancels the server operation. Sync HTTPX timeouts
bound individual transport phases, not a strict end-to-end wall-clock interrupt;
the sync wait checks its budget between calls and after success/failure. Document
this limitation rather than introduce detached timeout worker threads. Test early
transport failure, late transport failure, own async deadline, foreign TimeoutError
and caller cancellation, including absence of server cancel requests.

### Start gates and public exports

A and B can start immediately. A's first checkpoint is importing stable models,
pure function signatures and execution Protocols; C can then build against them.
D can follow A using fake executors without waiting for C. Changes in stubbed
signatures must be communicated before consumer edits. Test owner-local modules
until the full package is assembled; no persistent passing placeholder tests.

B integrates top-level exports after their owning modules are available:
`Client`, `AsyncClient`, `BasicAuth`, `TokenAuth`, `OAuth2Auth`, `Authenticated`,
`AuthenticationChallenge`, `AsyncAuthenticationChallenge`, `Response`,
`ResourceObject`, `IdCursor`, `Operation`, `AsyncOperation`, `RequestOptions`,
and the central exception classes. Obtain `__version__` from installed
`importlib.metadata.version("haveapi-client")`. The import module is
`haveapi_client`; distribution metadata name remains `haveapi-client`.

Acceptance at each handoff: producer provides exact files/exports, focused tests
and known unsupported cases; consumer confirms imports and one meaningful
cross-boundary fixture. No independent reviewer assignment is implied by these
early implementation checkpoints; final review follows the existing gate.

## Recommendation and scope

Add `clients/python` to HaveAPI. Publish distribution `haveapi-client`, with
imports from `haveapi_client`, subject to registry ownership/name checks. Use
Python 3.11+, uv for environments, locking and builds, `uv_build`
as the pure-Python build backend, HTTPX for both transports, Ruff for formatting
and lint, mypy for static checking, and pytest for tests. Preserve HaveAPI's
shared version and release pipeline.

Provide `Client` and `AsyncClient` with identical discovery, resources, request
construction, responses and exceptions. Only network operations, iteration over
remote pages, waiting, and resource closing differ by `await`/`async` syntax.
The implementation must contain no vpsAdmin resource names or special cases;
vpsAdmin belongs in examples and compatibility tests.

Initial scope includes nested resources, aliases, all documented layouts,
typed inputs, metadata, associations, Basic/existing-token/token-login auth,
multi-step authentication, and blocking-operation monitoring. Accept externally
obtained OAuth2 bearer tokens and expose an authentication-provider interface.
Browser authorization, WebAuthn interaction, automatic OAuth2 refresh, generated
API-specific types, a CLI, and a persistent credential/description cache are
separate follow-ups. Thus “generic” means arbitrary supported HaveAPI descriptions,
not that the client can invent handlers for unknown authentication schemes.

## Evidence and verified protocol facts

Inspected existing canonical bare repositories, without fetching or accessing
other sessions. These are local `origin/master` snapshots, not claims about the
latest upstream or deployed production revision:

- HaveAPI: `c58704a08451a231fdf6c6123437133422af46dc`.
- vpsAdmin: `fb2f51222503a45f2e5a42af505f719e44279ed0`.

Paths below are relative to the named repository at those revisions.

| Contract | Evidence and consequence |
| --- | --- |
| Discovery and versions | HaveAPI `doc/protocol.md`, `clients/ruby/lib/haveapi/client/communicator.rb`: `OPTIONS /?describe=versions` lists API versions; `OPTIONS /?describe=default` describes the default; `OPTIONS /v<version>/` describes a selected version. Envelope `version` is the **protocol** version, distinct from API version. Ruby client declares protocol `2.0` in `clients/ruby/lib/haveapi/client/version.rb`, rejects different majors and tolerates different minors. |
| Authorized descriptions | `doc/protocol.md`: authenticated discovery includes only allowed resources/actions/parameters. A public description is insufficient for a logged-in client. vpsAdmin's `api/lib/vpsadmin/api.rb` adds action scopes; permissions remain server-authoritative. Its implicit API version is `7.0`, which is not the HaveAPI protocol version. |
| Actions and nesting | `doc/create-client.md`, `doc/protocol.md`, Ruby `action.rb`: descriptions supply resource hierarchy, aliases, methods, input/output namespaces and layouts, and path templates with placeholders. IDs must be encoded as individual path values. Object metadata can contain `path_params`, but its absence is valid. |
| Serialization | `doc/typed-input-validation.md`, Ruby `communicator.rb`: POST/PUT use namespaced JSON. The 2026-10-20 review correction establishes DELETE also uses JSON, from current and v0.29.12 server.rb; only GET uses bracket-encoded query input. Legacy Ruby client DELETE query behavior is not authoritative. Metadata is a separate described namespace, usually `_meta`. Explicit nullable null becomes JSON `null` or an empty query value; omission stays distinct. Boolean, numeric, datetime and resource coercion have strict documented rules. |
| Responses | `doc/protocol.md`, Ruby `response.rb`: envelopes contain `status`, `response`, `message`, `errors`; payload uses the action's output namespace. Layouts are `object`, `object_list`, `hash`, `hash_list`; output may be absent. Global metadata is inside `response`, separate from the namespaced data; per-object metadata also exists. Localized messages remain strings. |
| Authentication | Ruby `authentication/token.rb`, server `authentication/token/provider.rb`: described token header, request/renew/revoke actions and credentials. Completed login has `complete=true`; `complete=false` carries a temporary token and `next_action`. Continuation supplies the temporary token as described action input. **The protocol prose has an inverted sentence saying multiple steps use `complete=true`; server and client implementation establish the opposite.** |
| vpsAdmin login/session | `api/lib/vpsadmin/api/authentication/token_config.rb`: password login can continue with `totp` (`code`) and then `reset_password` (`new_password1`, `new_password2`). Completion creates a user session and final token; renewal/revocation act on that session. Lifetime and interval belong to the generic described token request; vpsAdmin additionally uses scope. Basic cannot satisfy MFA (`doc/protocol.md`). |
| Pagination | HaveAPI `servers/ruby/lib/haveapi/actions/paginable.rb`, `actions/default.rb`, `model_adapters/active_record.rb`: `from_id`/`limit`, not offset/page numbers. The adapter supports ascending `id > from_id` and descending `id < from_id`. `_meta[count]=true` requests `total_count`; it need not exist otherwise. Description alone does not prove ordering, next-cursor calculation or a stable snapshot. |
| Long operations | `doc/protocol.md`, Ruby `action.rb` and `action_state.rb`: `blocking=true` plus response metadata `action_state_id` identifies an operation. `action_state.show/poll/cancel` expose `finished`, result `status`, progress and cancellation capability. vpsAdmin `resources/vps.rb` implements blocking start/stop/restart. |
| Generic test harness | `servers/ruby/test_support/client_test_server.rb` and `client_test_api.rb` provide the actual Ruby server harness used by existing clients, with users/roles, nested objects and action-state support. Reuse it instead of testing only self-invented JSON. |

Ruby/JS are useful dynamic-interface references. Go is a **generator**, not a
generic dynamic runtime. JS `authentication/oauth2.js` already limits its OAuth2
provider to externally obtained tokens; that is a reasonable first-release boundary.

## Public interface and examples

Construction performs no I/O. `connect()` explicitly discovers the selected API;
context entry calls it. If authentication is configured, connect first obtains
the provider description, completes authentication, and reloads authorized
discovery before exposing resources. An unfinished login returns/raises a typed
challenge without pretending to be connected. `refresh_description()` explicitly
reloads discovery; login completion, identity changes and logout also refresh or
invalidate it. Never share description caches across identities or API versions.

Illustrative read-only vpsAdmin use (not yet executed):

```python
import os
from haveapi_client import Client, TokenAuth

with Client("https://api.vpsfree.cz", auth=TokenAuth(os.environ["VPSADMIN_TOKEN"])) as api:
    result = api.vps.list.call(params={"limit": 100}, meta={"count": True})
    for vps in result.data:  # this page only; iteration performs no I/O
        print(vps.id, vps.hostname)
    print(result.meta.get("total_count"))
    detail = api.vps[123].show()
    interfaces = api.network_interface.list(vps=123).data
```

```python
from haveapi_client import AsyncClient, TokenAuth

async def list_vps(url: str, token: str) -> None:
    async with AsyncClient(url, auth=TokenAuth(token)) as api:
        result = await api.vps.list.call(params={"limit": 100}, meta={"count": True})
        for vps in result.data:
            print(vps.id, vps.hostname)
        detail = await api.vps[123].show()
        interfaces = (await api.network_interface.list(vps=123)).data
```

`VPS.Index` (`list` alias), `VPS.Show` and top-level `NetworkInterface.Index`
are verified in vpsAdmin `resources/vps.rb` and `resources/network_interface.rb`.
Do not present network interfaces as a fictitious child of VPS. Generic nesting
uses `api.parent[1].child[2].show()` only when the discovered hierarchy says so.

All actions return `Response[T]` with `data`, global `meta`, HTTP status and access
to the original envelope. `object` yields `ResourceObject`; `object_list` yields
a finite sequence of them; hash layouts yield ordinary dictionaries/sequences.
`ResourceObject` exposes fields by attribute and mapping lookup, object metadata,
and a bound resource for further actions. Associations expose their available ID,
label and prefetched fields; fetching missing data is explicit, never property I/O.
Bind object actions using supplied `path_params` or only an unambiguous combination
of known parent arguments and identifiers; otherwise require explicit arguments.

Resource/index proxies are immutable. No generated executable code, `eval`, or
mutation of client methods from server names. Exact resource/action names remain
accessible through maps:

```python
api.resources["close"].actions["from"].call(
    path_params={"item_id": 123},
    params={"meta": "a real API parameter", "class": "example"},
    meta={"count": True},
)
```

Normal dynamic calls treat **all** keyword arguments as API input parameters.
Only `.call(params=..., meta=..., path_params=..., options=...)` separates request
controls; this avoids reserving parameter names. Declared class methods/attributes
win dot-name collisions, and ambiguous resource/action aliases require maps.
Returned field collisions use `obj["items"]` etc. Keep `dir()` and description
inspection useful without promising compile-time knowledge of arbitrary APIs.

`BasicAuth(user, password)` is supported where advertised and MFA is not required.
For password/token login, use `begin_token_login(params)` returning
`Authenticated` or `AuthenticationChallenge`; the latter has `next_action`,
described input fields and `submit(params)` (awaitable on AsyncClient). Keep the
temporary token private. This models TOTP and forced password changes without
hard-coding either into the core or automatically prompting on stdin. Supplying a
handler is optional convenience; unsupported challenges remain resumable outcomes.
Never retain passwords after login or silently re-login/replay failed writes.
`renew_token()` and `revoke_token()` are explicit. Closing an HTTP client releases
connections; it does not revoke an externally supplied token/server session.

Pagination remains explicit: one action call returns one page. Provide
`iter_pages()` and `iter_all()` with an explicitly selected strategy, e.g.
`IdCursor(parameter="from_id", field="id", direction="asc")`, only where the
application knows that ordering is supported. Validate advertised parameters,
positive page size, monotonic cursor progression and missing/repeated cursors.
Stop on an empty page rather than assuming a short page is final. Preserve all
filters/metadata. Support custom next-cursor strategies; do not infer a universal
HaveAPI paginator or promise snapshot consistency. Sync uses `for`, async uses
`async for`. The basic example deliberately avoids unverified ordering assumptions.

For blocking actions return immediately with `result.operation`, then use
`result.operation.wait(timeout=...)` / `await ...wait(...)`. Polling failure,
HTTP failure, unfinished state and finished-but-failed operation are distinct.
Timeout/coroutine cancellation stops local waiting, not the server operation;
server cancellation is an explicit call, subject to `can_cancel`. Preserve the
operation ID so callers can resume monitoring.

## Architecture, invariants and compatibility

- Shared pure core: immutable discovery models, version checking, input coercion,
  path/query/JSON construction, envelope decoding and auth state transitions.
  Return request specifications; transport owns HTTPX requests. Thin separate
  sync/async execution methods avoid duplicated protocol logic and avoid running
  async through `asyncio.run()` in the sync API. Use AnyIO explicitly if its
  cancellation/locks/sleep are imported for backend-neutral async orchestration.
- HTTPX connection pools, finite configurable timeouts, TLS verification, explicit
  close ownership for injected clients, and no automatic retry of mutations.
  No hidden I/O in navigation, introspection or field access. Synchronize discovery
  and auth mutation; concurrent requests must not race by mutating shared paths.
- Preserve API base-path prefixes, encode every path argument independently,
  reject unsupported methods/layouts/protocol majors clearly, and validate
  discovery-supplied endpoint origins before adding credentials. Disable automatic
  cross-origin redirects. Explicitly configured external OAuth endpoints need an
  allowlist; unknown descriptions do not authorize credential forwarding.
- Preserve omission versus explicit null; reject NaN/Infinity and accidental
  `bool`-as-`int`; use the existing typed-input rules rather than generic Pydantic
  coercion. Native dates/aware datetimes serialize to accepted ISO forms. Do not
  inject all described defaults or blindly translate server regex validators.
  Server-side business validation remains authoritative.
- Separate `TransportError`, `ProtocolError`, `AuthenticationError`,
  `ValidationError`, `ActionError` and operation failure/timeout. Preserve HTTP
  status, envelope message and per-field errors even on non-2xx; handle HTML,
  malformed JSON and success-HTTP/error-envelope independently. Redact tokens,
  passwords and protected fields in repr/logging. Pass `Accept-Language` through.
- Ship annotations and `py.typed` for stable client interfaces, discovery,
  responses, authentication outcomes and exceptions. Strictly check internals;
  dynamic dot access inevitably has `Any`/runtime limits. Do not imply mypy can
  validate resource names, arbitrary response fields or action keyword schemas.
  Exact mapping APIs and optional later generated stubs address stricter users.
- No server, database, protocol, CLI, Terraform, daemon or NixOS option change is
  needed. New client and older clients coexist. Additive description fields are
  tolerated; unsupported features fail clearly. Initial compatibility is protocol
  major 2, verified against current HaveAPI plus a selected released baseline in
  later tests; older/pre-2 compatibility is not promised without evidence.
- No deployment ordering or coordinated node update; no persisted client state
  by default. Downgrading the package does not reverse already-issued API writes
  and cannot cancel a server operation. Roll back by pinning a prior package;
  maintain monitoring/recovery instructions for operations already started.

## Packaging, standards and release

Use `clients/python/pyproject.toml`, a committed `uv.lock`,
`src/haveapi_client/`, `tests/`, `README.md`, `examples/` and a packaged license.
uv is the environment/build frontend; `uv_build` is the independent PEP 517
backend. It supports this pure-Python library. Put a **static** project version in
the component's pyproject and extend root `make version`/release preparation to
synchronize it with root `VERSION`; release checks assert equality. Wheel and
sdist must build/install without a file outside `clients/python` or a Git checkout.
Read installed version via `importlib.metadata`, not a second hand-edited constant.
Follow upstream's bounded `uv_build` requirement and re-evaluate it when building.
Implementation decision approved by lead: use `uv_build>=0.13.0,<0.14`.
The selected Nix uv is 0.13.0 and can use its bundled native backend at that
floor; requiring 0.13.2 forced an isolated PyPI backend binary that the NixOS
loader rejected. Other PEP 517 consumers can resolve maintained 0.13.2 within
this range. This changes no runtime dependency or package capability.

Runtime dependencies: HTTPX; AnyIO only if directly used. Development group:
Ruff, mypy, pytest, async test support and coverage tooling as justified. Lock
development/CI dependencies, while publishing tested compatible runtime ranges
rather than forcing consumers to use the development lock. Test Python 3.11
through current stable versions, with dependency/CI support confirmed at
implementation; 3.11+ is the accepted product baseline, not a dependency limit.

Ruff supplies both formatter and linter; start with E/F/I/UP/B and intentional
exceptions, with one pyproject configuration. Extend existing **Overcommit**
hooks (`.overcommit.yml`, `.git-hooks/pre_commit/`) to run Python format/lint checks
on relevant files and preserve existing hooks. Do not install a competing hook
manager. Full mypy/tests run through a common check command and CI. Add a Python
Nix dev shell alongside current component shells.

Add `.github/workflows/clients-python-tests.yml` for formatting, lint, typing,
unit/contract tests and wheel/sdist smoke checks, with path filters including
shared protocol/harness files. Add Python to the existing build/release checks.
Resolve current action versions from official repositories when implementing;
no guessed action version pins are proposed here.

HaveAPI `doc/agent-instructions/releases.md`, `Makefile` and
`.github/workflows/release.yml` establish shared `VERSION`, annotated `vX.Y.Z`
tags, newest supported `haveapi-X.Y` branch, protected `release` approval,
build-once artifacts and recoverable partial publication. Extend that contract
to wheel/sdist and PyPI receipts/checksums. An independent Python `0.x` version
or Python-only tag scheme would be a policy change, not the default proposal.

PyPI Trusted Publishing requires a project (or pending publisher for its first
upload), registry ownership, GitHub owner `vpsfreecz`, repository `haveapi`,
workflow filename `release.yml`, and recommended environment `release`. Only the
approved publisher job gets `id-token: write`; no stored PyPI password/token.
Use the official PyPA publisher action to upload the verified wheel/sdist built
before approval. Match the environment in PyPI exactly. TestPyPI is separately
configured. Build-only/PR runs never publish. Retain original artifacts and
verify matching hashes on recovery; do not overwrite versions or rebuild an
already-approved version. Publishing remains a later explicitly authorized action.

Upstream facts checked read-only on 2026-10-19:

- [HTTPX PyPI metadata](https://pypi.org/pypi/httpx/json): stable `0.28.1`,
  uploaded 2024-12-06; [official repository metadata](https://api.github.com/repos/encode/httpx)
  says not archived/disabled, pushed 2026-10-02. This supports current maintenance,
  not a promise about future support. [Official async docs](https://www.python-httpx.org/async/)
  confirm sync/async clients and asyncio/Trio support.
- [uv build backend source documentation](https://github.com/astral-sh/uv/blob/main/docs/concepts/build-backend.md)
  confirms pure-Python support and a bounded backend requirement; observed example
  is `uv_build>=0.13.2,<0.14`. [uv_build metadata](https://pypi.org/pypi/uv_build/json)
  reports `0.13.2` uploaded 2026-10-19; [Ruff metadata](https://pypi.org/pypi/ruff/json)
  reports `0.17.1` uploaded 2026-10-15. Their official repositories are not archived.
- Warehouse's authoritative docs for
  [adding](https://github.com/pypi/warehouse/blob/main/docs/user/trusted-publishers/adding-a-publisher.md)
  and [using](https://github.com/pypi/warehouse/blob/main/docs/user/trusted-publishers/using-a-publisher.md)
  confirm repository/workflow identity, environment, monorepo support and required
  `id-token: write`. HTML documentation access returned 403; official raw GitHub
  sources supplied the evidence instead.
- `https://pypi.org/pypi/haveapi-client/json` returned **404**. This does not prove
  the name is registrable, reserved status, or our ownership. No registry or
  GitHub environment configuration was inspected or changed. Exact supported
  Python CI matrix and all development dependency pins remain implementation checks.

## Implementation package acceptance

The lead assigns execution using the ownership above and serializes shared
root/release edits and Git operations. The original acceptance matrix below
retains the behavior/check requirements; ownership is updated for the live roster.

| Package / suggested owner | File boundary and dependency | Acceptance and checks |
| --- | --- | --- |
| A: protocol core / implementer0 | `src/haveapi_client/_protocol/`, `exceptions.py`, `tests/unit/protocol/`; begin after public/internal contracts are agreed | Arbitrary descriptions and names; exact namespaces, paths, nulls, aliases and all layouts; version/envelope failures. Pure fixtures plus typed-input corpus. |
| B: package/tooling + harness / implementer1 | `pyproject.toml`, `uv.lock`, license, `tests/fixtures/`, `tests/integration/` harness; root hooks/Nix/CI changes assigned exclusively to this owner | Reproducible locked checks; package import from wheel and rebuilt sdist outside repo; real Ruby harness boots with managed readiness/cleanup. Agree fixture boundary with A; no edits in A's source. |
| C: clients/auth/dynamic facade / implementer2 | `client.py`, `async_client.py`, `_transport/`, `_auth/`, `_resources/`, their tests; depends on A interfaces and B scaffold | Identical sync/async behavior, typed resumable challenges, authorized rediscovery, Basic and token flows, immutable concurrent requests, no property I/O or credential leakage. |
| D: responses/paging/operations / implementer0 | `response.py`, `pagination.py`, `operations.py`, their tests; depends on A and agreed execution adapter | Finite page results plus metadata; explicit safe cursor progression; associations/path binding; wait failure/timeout/cancel semantics. Paired sync/async tests. |
| E: integration/docs/release / implementer1 with architect/lead acceptance | `README.md`, `examples/`, integration cases, shared version/release helpers; after C/D, serialize root-file edits | Generic real-server suite and isolated vpsAdmin compatibility evidence; self-contained distribution; shared version and build-once trusted-publishing workflow; user-facing writing and final review before long tests. |

Quick checks (proposed commands from `clients/python`, inside the declared Nix
environment): `uv sync --locked`, `uv run ruff format --check .`,
`uv run ruff check .`, `uv run mypy src`, `uv run pytest tests/unit`.
Test protocol output independently of implementation: HTTPX MockTransport can
assert exact requests for both clients. Cover UTF-8/slashes/query metacharacters,
mounted base paths, nested IDs, colliding/keyword names, malformed descriptions,
nullable/omitted values, bool versus integer, NaN/Infinity, invalid dates,
error envelopes on both successful and failing HTTP statuses, authorization
changes, MFA chains, token renewal/revocation, timeout and concurrent isolation.

After committed implementation, quick checks and mandatory independent final
review, run the real generic HaveAPI server suite and wheel/sdist build/install
checks. A watcher owns long or uncertain-duration verification. Verify Basic,
token login including a generic custom challenge, authorized discovery refresh,
nested associations, metadata, pagination and operation monitoring against the
actual server, not just Python mocks.

Before calling it vpsAdmin-compatible, run against an owned disposable vpsAdmin
API with ordinary-user/admin fixtures: current-user/VPS/network-interface reads,
two-page traversal with verified ordering, authorization-filtered discovery,
invalid typed inputs, TOTP and forced-password-reset chains, expiry/revocation.
Add harmless write/operation tests only on seeded disposable objects; VPS
start/stop requires an owned development cluster and is a separate integration
check. Sanitized vpsAdmin fixtures aid fast CI but do not replace this run.
Production credentials/services are not required for default CI. Record exact
server/client revisions and distinguish API-only proof from node execution proof.

Remaining release/verification decisions: PyPI namespace/ownership and supported
released-server baseline. Browser OAuth stays out of initial scope. Python 3.11+
and the explicit paginator interface above are settled for implementation.
Implementation approval does not authorize merging, release publication or
session closure. The session remains open.

The concrete API-only integration plan and selected released baseline are in
[verification-plan.md](verification-plan.md). That plan selects HaveAPI 0.29.12
and removes released-baseline selection from the open decisions above.
