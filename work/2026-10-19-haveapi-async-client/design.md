# HaveAPI JavaScript Promise support: investigation and implementation proposal

Status: execution authorized by the user's **“Implement the plan.”**, 2026-10-19.
Architect: `architect0`. The lead has released the initial implementer packages.
This brief governs application work; the architect edits design only. Revised for the user's
standalone async client object: this supersedes the Async-suffixed method proposal.
The user has also selected TypeScript authoring for **both** the existing callback
Client and new AsyncClient, superseding the earlier async-only source option.
The earlier investigation performed no implementation. Execution progress and
verification results belong in state.md and implementer reports, not historical
claims in the evidence section. Current browsers and React WebUI adoption remain
requirements. No npm publication, default-branch integration or deployment is
authorized.

## Execution addendum and interface freeze

This addendum fixes the accepted execution choices and supersedes conditional
build wording in the earlier proposal below. Current implementation bases:

- HaveAPI: `worktrees/2026-10-19-haveapi-async-client/haveapi`,
  `cb3f39f75e8a63416388d24293f936d1db97162b`.
- React pilot: `worktrees/2026-10-19-haveapi-async-client/vpsadmin-webui-async`,
  branch `dev/haveapi-async-client`, base
  `7860521f30826c3886c89c35e8ab6f4e082e0a4b`. The earlier dated-branch WebUI
  worktree is read-only and not an implementation destination.
- Baseline HaveAPI dist SHA256, captured by implementer1 before conversion:
  `3e8fcefe8edf78f6cea635c1bf4312b56c2e05355287153e142d30a9608c6436`.

**Build fixed:** keep the gulp command; run `tsc` with `target: ES5`,
`module: ESNext`, declaration emit, then Rollup named-export UMD at unchanged
`clients/js/dist/haveapi-client.js`. Preserve package main, `HaveAPI` browser
global, AMD/CommonJS shape and `Client.*` static exports; add `AsyncClient`
without a `.default` wrapper. Generated declarations go under `dist/types` with
a matching package types entry. No separate ESM runtime artifact initially;
React/Vite consumes the packed CommonJS/UMD package. No new engines restriction,
runtime polyfills or eager Promise/AbortController access during callback-only
loading, construction or requests.

AMD compatibility requires the original `define([], factory)` registration and
the factory's returned namespace object. Rollup's direct named UMD output uses
an `exports` dependency instead. Therefore generate a named-export IIFE payload
with Rollup, then compose the original UMD shell around it in the build: the
factory returns the local HaveAPI binding, CommonJS assigns `module.exports =
factory()`, and browser scripts assign `root.HaveAPI = factory()`. Final output
remains UMD; the intermediate IIFE is an intentional build detail. Do not weaken
the baseline AMD fixture or rewrite generated wrapper text with an unchecked
regex. Preserve ambient CommonJS/XHR detection if an inner export-container
parameter would shadow `exports`; keep any detection capture factory-local.

Use named-export TS modules at the existing source paths. Preserve function
constructors/prototype assignments and represent callable objects with component
interfaces plus constructable callable bridges; do not convert their behavior
to ES classes. `src/haveapi/types.ts` owns shared description, transport and
callback shapes; each component owns its public interfaces. Type-only imports
break type cycles. The export entry populates runtime `Client.*` and provider
registries in the original order after modules load.

Rollup `output.strict: false` is required for existing sloppy-mode behavior;
prevent the TS configuration from reintroducing a bundle-wide strict directive.
Preserve actual hook `.apply` receiver/argument behavior. Undeclared legacy
globals require localized, documented compatibility handling. The actual Vite
proof below supersedes bare ambient assignments for reachable global effects:
use an explicit typed host-global bridge for `Authentication`, `v1`, `v2` and
`ret`, preserving their observable values and live reads without a new
globalThis requirement. Unreachable references may use erased ambient typing.
Do not turn these into unrelated callback bug fixes. New async code is scoped
normally. Escalate broader incompatibility or disproportionate complexity.

The generated `i18n_messages.js` remains unchanged: implementer0 may provide a
typed catalog declaration and include its contents as Rollup factory-local intro,
preserving the existing catalog scope. Intermediate ES modules are build inputs,
not published runtime entries. No generator or translation changes are implied.

**Initial ownership:** implementer0 owns build/package/TS configuration, shared
types/export registration, callback client/http/hooks/authentication/exceptions/
i18n migration and generated dist. Implementer1 owns self-contained `node:test`
VM compatibility fixtures and callback action/action_state/base_resource/
resource/resource_instance/resource_instance_list/response/local_response/
parameters/validator migration, including validators. Fixture work can proceed
independently against the pinned baseline before converted modules exist. Both
read current repository guidance; only implementer0 edits build/export/shared
type files. Serialize Git operations and generated-output writes through lead.

**Shared seams:** normalize RequestSpec fields (method, API-relative path,
namespaces, params, meta, headers, signal and timeout) and snapshot per-client
request context at dispatch. The low-level transport reports HTTP status,
body and transport error without prematurely collapsing them. It must remain
usable by Client without constructing Promises; AsyncClient wraps that internal
completion boundary and applies the new rejection contract. Callback Client
keeps its existing observable outcome/timing mapping. Async RequestResult has
fixed data/meta/envelope/httpStatus fields; dynamic InvocationResult has fixed
value/response fields. Async resources invoke the normalized request seam and
return only async-owned objects. Auth state is per-client; WebUI supplies current
headers and retains its refresh/read-retry policy. No shared mutable mode flags,
credentials, prepared paths or callback-owned resource objects.

The accepted resource/core seam is `src/haveapi/async/types.ts`, owned by
implementer0. `AsyncResourceContext` supplies readonly `description`,
`metaNamespace` and `generation`, plus `request<T>(spec)`,
`validateParams(action, params?)`, `makeError(kind, message, details?)` and
`recordInvocation(value, response, action)`. Validation reuses typed coercion
and the snapshot's language context without mutating caller input; public
async methods turn its synchronous errors into Promise rejections. A resource
request checks the generation before sending; low-level client requests use
the current dispatch context. Absent/null `outputNamespace` selects the full
payload; a selected namespace must exist. RequestResult and InvocationResult
retain the fixed shapes above. Error details retain HTTP status, response,
envelope, validation errors, completion state, cause and reason when available.

Async MFA/resource snapshots use null-prototype parameter maps. The legacy
`Parameters` implementation assumes callable map-owned `hasOwnProperty`, so
implementer0 owns a narrow optional per-validation dictionary policy: async
validation supplies null-prototype allocation and safe own-key checks; the
default callback path retains plain objects and its original receiver-method
calls, including existing throws. Apply it consistently to Parameters-owned
result/error maps and ownership checks. Keep constructor arity/prototype and
legacy instance shape unchanged; no global policy, client mode flag, duplicated
validators or unrelated validator-option changes. Cover null-prototype MFA and
action input, own `hasOwnProperty`/`__proto__` parameter names, and callback
default parity. The resource-context interface is unchanged.

Implementer1 owns the resource factory and public resource type:

```ts
export function createResource(
  context: AsyncResourceContext,
  path: readonly string[],
  ids?: readonly IdArgument[]
): AsyncResource;
```

Resolve resource descriptions from the context and path. AsyncClient imports
this factory; resource modules use type-only imports for core types and invoke
the injected context, avoiding a reverse runtime dependency. Encode bound IDs
once, retain independent path/option snapshots, and associate completion data
privately with invocation wrappers. Do not eagerly allocate async-only runtime
primitives at package load.

The initial packages are released; callback parity is the gate before shared-core
extraction and async behavioral packages. The phase table below retains later
ownership. Independent final review follows committed intended changes and
quick checks, before long integration checks. This design handoff alone does not
trigger final review.

### React pilot without an npm release

Implementer1's later WebUI package adds a thin structural/injectable request-client
adapter plus one dedicated script, type consumer fixture and browser test using
existing tooling. Reuse existing auth/session/retry policy and HTTP fixtures;
do not create a parallel protocol decoder or a new harness framework. Normal
production application entry points retain their current default transport.
Do not add an unpublished npm version, absolute/local file dependency, root lock
update or Nix dependency hash. Ordinary `npm ci`, typecheck and build must still
work without the candidate HaveAPI package installed.

The HaveAPI owner builds the candidate then runs local `npm pack --ignore-scripts`
in `clients/js`, writing the tarball to an owned temporary artifact directory.
Packing does not publish and needs no version bump. The WebUI proof command is:

```sh
npm run test:haveapi-package -- --package /absolute/path/haveapi-client-0.29.0.tgz --webui-ref HEAD
```

Use the actual packed filename/version; the example does not select a release.
The dedicated script snapshots the specified committed WebUI ref into an owned
disposable directory, runs `npm ci` there, and installs the tarball there with
`npm install --ignore-scripts --no-save --package-lock=true <tarball>`. No
dependency mutation reaches the real worktree. A dedicated TS fixture imports
the package's emitted declarations and assigns AsyncClient to the adapter's
structural interface; a dedicated Vite/browser test loads its actual compiled
JS and injected adapter. Prove one read, mutation, qualifying 401 refresh/read
retry, no write replay, abort and response-first action-state receipt. Keep these
candidate-dependent fixtures outside the default application compilation/tests.

The first post-review proof demonstrated that the earlier `--package-lock=false`
command ignored the snapshot's resolver baseline and upgraded 96 installed
packages, including pinned Playwright. Its existing CLI guard correctly refused
before browsers launched. Therefore explicitly enable lockfile reading while
retaining `--no-save` and `--ignore-scripts`. Before candidate installation,
capture snapshot manifest/lock bytes and installed name/version at each existing
lock-listed package path after `npm ci`; verify those versions match the lock.
Before any candidate compilation or browser launch, require unchanged manifest
and lock bytes and unchanged presence/name/version of every baseline installed
locked package. New candidate/dependency paths are allowed; replacements are
not. Do not require platform-optional paths absent from the baseline. This is an
integrity assertion, not a dependency solver or per-tool pin workaround.

Implementer1 owns this narrow runner correction and drift/lock-change
regressions. First run the lead-authorized single fresh npm-only disposable
feasibility probe with a new watcher; no compiler/browser invocation or blind
retry of the drifted snapshot. Record the probe result before editing the runner.
The change restores isolation already required by the reviewed pilot and does
not expand its public/cross-project contract; focused inspection and quick checks
apply under review steps 9/10, with no automatic reviewer rerun. If preserving
the graph needs a new resolver or broader behavior, return to the lead. The
earlier candidate type/Vite run used drifted tools and is not final proof.

Record tarball SHA256, both source heads, Node/tool versions and results. Accept
`--haveapi-ref <full-SHA>` as pack-owner-supplied provenance, required when the
candidate package has no `gitHead`. Record whether the source reference came
from this argument or package metadata; fail clearly if both exist and disagree.
Neither source label independently proves the tarball's Git contents. The pack
owner confirms the candidate was built from the stated committed source; the
tarball hash identifies the exact artifact exercised by the proof. No adjacent
manifest or publication step is needed. Run the
long/uncertain proof via the verification watcher after committed-deliverable
review; existing quick structural/fake-client checks remain independent. This
proves real package fit, not production migration. Switching the default WebUI
transport and committing a registry dependency follows an approved published
release in a later rollout; no package publication is authorized here.

### Synthetic BFF state for the adapter fixture

The dedicated Vite fixture explicitly compiles with
`import.meta.env.VITE_RUNTIME_MODE` set to `bff`, matching the production policy
under test; verify the actual resolved fixture config rather than a copied
mock. Its four adapter scenarios start from a deliberately synthetic,
already-validated session identity, not a full application/OAuth bootstrap.
The existing window bootstrap supplies API/provider/meta configuration and a
synthetic token. The fixture uses a known 64-hex-character session key, matching
token and a fresh browser context with empty session storage.

Implementer1's fixture-only session helper calls the real
`bindBffImpersonationToSession(key, window.sessionStorage)` and then
`rememberBffSession(sameOriginSessionUrl, key, token)` on that same runtime object,
matching `src/app/runtimeBootstrap.ts:250-251`. `rememberBffSession` alone does
not establish the validated identity required by `src/app/config.ts:232-245`.
Before the first API call, assert the actual production runtime reports OAuth2
auth with the synthetic token and that both bound/remembered session identities
match the fixture key. Do not rebind during refresh or replace the runtime
object: the real refresh/session-identity checks remain under test.

No production guard, config, auth source or storage policy changes are needed.
Do not introduce a second validator/bootstrap framework or call
`loadRequiredBffRuntime` merely to run adapter tests. That would add config and
initial session HTTP requests unrelated to their contract. The fixture does not
certify config/session-response validation, OAuth login or application bootstrap;
existing production-bootstrap tests own those checks. Retain current assertions
for old/new token headers, one read refresh/retry, no write replay, changed-session
rejection, abort and response-first receipts. Commit the coherent fixture/config
and focused quick checks for direct acceptance before another browser proof.

### Real-browser UMD smoke within the packed pilot

Implementer1 owns one `scripts/haveapi-package/umd.spec.ts` in the WebUI
repository and the existing pilot's config/type/script-check updates.
Implementer0 supplies the exact minimal OPTIONS/description/action wire fixture
compatible with both clients, referencing the committed core/contract tests;
there is no additional application-source package. Replace the preliminary
Chromium-only raw-script check rather than retaining two overlapping checks.
The shared fixture is pinned to HaveAPI
`ae0fe39738c3eb10019377d0fce95dc249cdfd16`: explicit `{version: 1}` sends OPTIONS
to `/umd-api/v1/`; a `widgets.show` action at `/v1/widgets/{widget_id}` then sends
GET `/umd-api/v1/widgets/7`. Use the protocol-2.0 success envelope with description
at `response`, object payload at `response.widget` and
`response._meta.path_params: [7]`. Callback setup takes `(client, status)`;
action `onReply(client, value)` receives ResourceInstance. References are
`test/compatibility/callback.spec.cjs:64-112,128-134` and
`test/async/core.spec.cjs:27-45`, relative to `clients/js`. No authentication or
version-discovery scenario is needed for this smoke.

Run the same small scenario in named `umd-chromium`, `umd-firefox` and
`umd-webkit` projects using the WebUI's pinned Playwright 1.61.0. Keep the fuller
adapter `browser.spec.ts` on Chromium only. A fresh empty HTML page loads the
exact installed candidate `dist/haveapi-client.js` through an ordinary script
element. Serving the HTML, script bytes and synthetic API responses with
Playwright routes is sufficient; the page must not import the npm module or
pass its script through Vite transformation. Verify `window.HaveAPI.Client` and
`AsyncClient` with no default wrapper. Use real browser XHR for callback setup
and one described GET action, then async setup and the same awaited action.
Check callback arguments/undefined immediate action return, async value/meta,
request methods/paths, and absence of page errors/unexpected requests. These
are browser/transport fixture checks, not live-server certification.

The existing `npm run test:haveapi-package -- --package <absolute-tgz>
--webui-ref <committed-ref> --haveapi-ref <full-SHA>` runs the Chromium adapter
proof and all three UMD projects. Reuse its artifact/provenance record and
existing preview server; no new framework or production dependency. Apply any
Chromium executable override only to Chromium projects. Commit all fixture
code and pass quick type/config-discovery (`--list`)/runner unit checks before
final review; run browsers only afterward through the verification watcher.

Runtime availability is a separate preflight: on 2026-10-19 the default browser
cache contained Chromium/headless-shell build 1228 and ffmpeg, but no Firefox or
WebKit entries; no launch was attempted. This is cache evidence, not successful
runtime verification. Provision missing matching engines through the existing
pinned runner (`node scripts/playwright.mjs install chromium firefox webkit`)
in the documented environment before the post-review run. Record actual engine
versions/results. Missing engines or system libraries must produce an incomplete
matrix report, never an automatic skip or a three-browser success claim.

### Vite strict-context correction (awaiting lead implementation release)

The actual locked/minified proof using HaveAPI
`dc94157808966c12418b4009085fec237a869789` passed raw-script UMD in Chromium and
Firefox, but all four adapter cases failed before initialization. The emitted
`index-CrWIWntf.js:4:2456` retained `Authentication={...}` from
`src/haveapi/authentication.ts:42-44`; its ambient declaration emitted no runtime
binding. Vite had neither omitted nor mis-renamed it: a script of type module
applies strict semantics to the bundled CommonJS code despite the inner bundle
having no strict directive. Evidence is retained under
`/tmp/webui-haveapi-package-IsQ5c6/source/scripts/haveapi-package/dist/assets/`.
The later callback `v1`/`v2` and `ret` assignments have the same mechanism.

Correct the package source, not its consumer import: one small internal typed
host-global bridge explicitly reads/writes these four known properties. Preserve
the exported authentication registry object, registerProvider's live global
lookup, protocol scratch globals and defaultParams' returned/global object.
Resolve the actual host global with guarded globalThis/browser/worker/Node
fallbacks; do not require globalThis, dynamic evaluation, a new package entry or
an unminified consumer. Retain the original non-strict UMD loader shell and other
callback behavior. Do not turn the bridge into a general compatibility layer.

Implementer0 owns the package bridge and generated bundle, coordinating edits
to callback client/authentication/resource_instance files with implementer1.
Implementer1 owns any packed-consumer fixture adjustment; the named-import Vite
proof must remain minified. Quick verification includes raw UMD/AMD/CommonJS
and global-value parity, callback loading without async primitives, host fallback
without globalThis, and strict-context CommonJS-wrapped VM initialization plus
protocol/defaultParams paths. This changes the preservation mechanism assessed
by review; submit the cohesive committed fix and quick evidence for affected
general, architecture and risk/compatibility review before repeating the actual
packed browser proof. No existing green raw-script result certifies Vite fit.

## Review remediation decisions

At HaveAPI `ae0fe39738c3eb10019377d0fce95dc249cdfd16`, review found two
new-async correctness gaps during preliminary triage and a third in the final
report. The lead released bounded remediation after the complete four-lane
review: no Blocking findings; Important R1/R2/R3. Owners implement the following
seams, retain callback compatibility, and coordinate generated output/commits.

- **R1 / implementer1:** preserve AsyncResourceInstance references as leaves
  only when copying local resource attributes. Keep generic parameter/metadata
  snapshot and cycle semantics unchanged. Remove the premature `new()` and
  `submittedParams` deep copies: dynamic actions normalize Resource values
  synchronously before snapshotting the request. For a Resource-typed input,
  extract the declared `value_id` (default `id`) from an async entity or an own
  key of a plain association record; a custom key never falls back to `id`.
  Missing/invalid identifiers reject validation, not silent omission. This is
  parameter conversion, not binding inference; `path_params` remains authoritative.
  Local entity references must not survive into the dispatched scalar payload.
- **R2 / implementer0, feasibility confirmed:** keep callback coercion
  and the dictionary policy unchanged. In the async validation adapter, create
  one Parameters accumulator with empty input, coerce each own input entry in
  a separate `coerceParams` call, merge the results into its safe parameter map,
  then validate once with the complete map and accumulated type errors. Separate
  calls isolate function-scoped scratch values that legacy coercion accidentally
  reuses between fields. This reuses coercion and cross-field validators without
  duplicating their logic or introducing a compatibility mode.
  For null input descriptions and unknown schema keys, do not read ignored
  supplied values merely to create the single-entry map.
- **R3 / implementer0 receipt; implementer1 guard regressions:** construct the
  existing RequestResult diagnostic receipt immediately after top-level envelope
  validation, before metadata/payload/namespace interpretation. It retains raw
  `envelope.response` (possibly undefined), the envelope and HTTP status; `meta`
  begins empty and is populated only after validation. Attach that same receipt
  to invalid-metadata, missing-payload and missing-namespace protocol failures.
  Materialization failures already preserve it. No new public type is needed.
  An unsaved instance's existing accepted-unbound guard latches when HTTP is 2xx
  and the validated envelope says `status: true`, preventing another create on
  that instance while preserving local attributes/identity and original failure
  context. Invalid JSON/top-level envelopes have no validated success receipt;
  transport/timeout/abort, non-2xx and `status: false` remain distinct. Do not
  infer success from HTTP alone or introduce automatic retries.

Regression gates cover direct create, `new(attributes)`, set/save, loaded
association update, custom/missing/inherited identifier keys, and deferred
entity/scalar mutations after dispatch; preserve generic metadata behavior.
Exercise the actual emitted bundle, Parameters and fake XHR in addition to
resource-context unit tests. For R2 cover valid-then-invalid Integer, Float,
Boolean and Datetime fields, order/mixed/nullable cases, MFA and complete-map
cross-field validation, while callback compatibility checks retain old behavior.
For R3 use actual emitted request decoding plus save for HTTP 201 success with
missing selected namespace and missing response payload; also cover malformed
metadata. Assert retained response/envelope/status, unchanged local attributes
and binding, and exactly one POST after two save attempts. Negative controls
must not turn ambiguous transport or API failures into confirmed-create latches.

## Recommendation

Export **`HaveAPI.AsyncClient` alongside `HaveAPI.Client` from the same npm
`haveapi-client` package**. It is a standalone public client object, not a
separate npm package or a `.async` facade. Its network methods use ordinary
names and return Promises. Existing `Client` keeps its callback signatures,
return values and documented callback-free/fire-and-forget behavior.

Author both clients and their action/resource/authentication implementations in
TypeScript, compiling them to ordinary JavaScript with generated declarations.
The user's “sync client” means the existing callback-based Client: its HTTP
operations are already asynchronous. Rewriting its source language does not
convert its public API to Promises or introduce blocking network operations.

Share protocol, validation and transport machinery through composition and
small internal helpers; give the async client its own state and resource model.
Do not subclass callback resources and expose their network methods, toggle a
mutable async mode, or change existing Client instances. A separate package
would duplicate maintenance and complicate keeping protocol/security fixes
consistent. The tradeoff is maintaining two public object models in one package,
with contract tests proving their shared protocol behavior.

The separate React **vpsadmin-webui already uses its own async TypeScript/fetch
client** and has no direct or transitive npm HaveAPI dependency. This feature
does not automatically benefit that application. Making it usable there is now
an explicit design goal: add a typed low-level request API and prove a thin
WebUI adapter can replace transport/protocol duplication. Broad migration follows
that proof. Scope is HaveAPI and the **new React vpsadmin-webui only**; legacy PHP
WebUI and console integration are excluded by the user's latest direction.

## Evidence scope and exact revisions

Inspected existing canonical bare repositories using Git object reads; no other
session's checkout was used. These are cached remote-tracking heads, not claims
about the latest upstream or deployed revisions. HaveAPI local `master` differs
from the inspected remote-tracking ref.

| Repository | Inspected ref | Exact commit |
| --- | --- | --- |
| haveapi | `refs/remotes/origin/master` | `06865bb847a564fe20e59ea6d72856c2f01a82e3` |
| vpsadmin-webui | `refs/remotes/origin/main` | `7152729dcde326e00d16b5af0a46d0f60b431dbb` |

All paths and line numbers below refer to these commits. `implementer0`
independently inspected the HaveAPI callback contracts; `implementer1` traced
the WebUI dependencies. Their read-only findings inform this design.

## Proposed public contract

These methods and signatures are **proposals**, not currently available APIs:

```js
const HaveAPI = require('haveapi-client');
const api = new HaveAPI.AsyncClient('https://api.example.test');

await api.setup();
await api.authenticate('token', { token });

const { value: vps, response } = await api.vps.show(101);
console.log(vps.hostname, response.meta);

const { value: vpses } = await api.vps.list({
  params: { limit: 10 },
  meta: { count: true }
});

// The request was accepted; the server operation may still be running.
const started = await api.vps.restart(101);
const completed = await api.waitForCompletion(started, {
  timeoutMs: 120000,
  onStateChange: state => console.log(state.progress)
});
```

- `setup(): Promise<void>` validates descriptions and installs async resources.
  `authenticate(method, options): Promise<void>` supports authentication before
  setup and refreshes the authorized description before resolving. These reject
  all failures, including errors from later transport callbacks. They do not
  return the client. `availableVersions()` also returns a Promise. Constructor,
  `useDescription`, local language settings and resource selection remain
  synchronous; they perform no network I/O.
- Dynamic `api.vps.show(101, options?)` and explicit
  `api.resource('vps').action('show').invoke(101, options?)` use the same Promise
  contract. Support aliases, resource-curried IDs and an unambiguous options
  object containing `params`, `meta`, `signal` and request timeout. Resolve a
  fixed `{ value, response }` wrapper; never detect optional completion
  callbacks or introduce suffixed action aliases.
- `value` is an **async-owned** resource instance/list for object layouts, or
  plain data for other layouts. `response` is a data-only RequestResult carrying
  `data`, `meta`, `envelope` and `httpStatus`. No callback Client, provider,
  ResourceInstance, ResourceInstanceList or ActionState leaks into this API.
  Low-level `request<T>()` provides raw/unwrapped results without a second
  `directInvoke` flavor in the first release.
- AsyncResourceInstance field access and list indexing/iteration are local.
  Its bound actions return the same Promise result as root actions. `.save()`
  awaits create/update, validates the reply and updates identity, attributes and
  bound paths only after success; it returns `{ value: instance, response }`.
  A local `resource.new(attributes)` creates an unsaved async instance. Lists
  contain only async instances; any future pagination/network helper must also
  return a Promise. No automatic fetch occurs during iteration or field access.
- Server `path_params` is authoritative for returned identity; never infer a
  generic binding from `data.id`. An update may retain its existing binding when
  path metadata is omitted; explicit invalid metadata is a protocol error.
  Require new identity only where the described binding needs it, preserving
  valid singleton/idless resources. A definitely successful create missing
  required identity rejects with a protocol error retaining the successful
  response/envelope. Preserve local attributes/identity and set one small
  accepted-unbound guard so a second save cannot issue another create. Its
  message states that creation succeeded but identity is missing and the caller
  must fetch/rebind; it must not imply rollback or retry safety. Ordinary
  unbound results remain readable, while network helpers needing missing IDs
  reject until bound. This is new async behavior only, not a generalized
  recovery state machine or a callback Client change.
- Associations use explicit `await instance.loadAssociation(name, options)`
  returning `{ value, response }`; prefetched data can satisfy it without I/O.
  Here `response` is the actual load reply, or null for a prefetched cache hit;
  do not fabricate an HTTP reply for local data.
  Association property access never starts a hidden request. Failed loads reject
  without a half-resolved shell. This replaces callback `whenResolved` and avoids
  superficial wrappers around the existing save/lazy-load correctness gaps.
  Save and explicit association loading are included in first-release coverage;
  callback lazy-property semantics are not carried into AsyncClient.
- Authentication includes Basic, token and existing-token OAuth2 with independent
  async provider state. Token MFA uses an async-capable `onChallenge` function
  returning input/Promise<input>; no continuation callback is needed. Provider
  setup does not newly prove credential validity. OAuth authorization-code,
  session-refresh policy, automatic renewal and a convenience `logout()` are
  deferred; existing explicit revoke actions remain callable with Promises.
  Do not expose callback-only provider methods to fill these gaps.

### Isolation, collisions and Promise safety

AsyncClient owns credentials, language, descriptions, resource bindings and
in-flight lifecycle state. Independent async/callback clients cannot change each
other's state. Concurrent requests snapshot IDs/options/auth context at dispatch;
there is no shared mutable prepared path. Serialize setup/authentication changes
within each async instance, and publish new descriptions atomically after
validation. A late result cannot replace a newer authentication generation;
cross-generation requests retain their dispatch identity and never replay.

Lead-approved binding rule: after a successful description/authentication
generation replacement, an older bound resource/instance rejects new network
operations with a clear stale-binding error before dispatch. Already-dispatched
requests may settle using their original context but cannot republish the old
root registry. Implement this as a generation snapshot and guard; no retry
framework is needed. Low-level `request<T>()` uses current explicit dispatch
context and is not tied to a description binding. Merely changing per-request
headers/language does not replace a description generation. Callback Client
behavior is unaffected.

Fixed result wrappers retain metadata without flattening resources. Additionally
**all async-owned client/resource/list objects must be non-thenable**: reserve a
noncallable `then` on these new surfaces, and keep described `then` actions,
resources and attributes reachable through explicit `action(name)`,
`resource(name)` and `get(name)` lookup. Apply the same explicit lookup rule to
helper-name collisions and reject unsafe prototype attachments. Do not change
legacy Client's attachment rules. API-supplied properties stay nested in
response records; setup/auth resolve void. Thus neither Promise settlement nor
an accidental `await` on a local async resource can invoke a remote `then` action.

Shared internals must retain URL-origin, encoded-path, validation and language
rules. Prefer extracting pure serialization/decoding helpers and a per-instance
transport adapter; do not route AsyncClient through callback methods that lose
HTTP status/errors or throw later without a rejection channel. Preserve old
Client behavior while reusing the lower-level implementation where safe.

### Typed path-based API for the React WebUI

Add `asyncClient.request<T>(request): Promise<RequestResult<T>>` alongside the
dynamic action API in the **same package**. This is necessary because the React
WebUI already knows endpoint paths/types and should not need to download a
resource description or construct ResourceInstance objects for every adapter.
A dynamic-invocation-only wrapper would leave transport/protocol duplication or
force an unnecessarily broad application rewrite.

Proposed TypeScript-facing example:

```ts
const result = await api.request<Vps>({
  method: 'GET',
  path: '/v1/vpses/101', // Illustrative: retain the actual WebUI endpoint path.
  outputNamespace: 'vps',
  signal,
  headers: currentAuthenticationHeaders()
});
// Stable typed fields: result.data, result.meta, result.envelope, result.httpStatus.
```

`RequestSpec` explicitly carries method, API-relative path, input/output
namespace, metadata namespace, params, meta, headers and optional AbortSignal.
The client validates the URL against its configured origin, serializes query or
JSON payloads using shared HaveAPI rules, sends language/authentication headers,
parses and validates the envelope, and unwraps the selected output namespace.
The adapter supplies endpoint-specific namespace/metadata settings already
known to the WebUI; this route does not require `setup()` or an OPTIONS fetch.
Dynamic actions derive the same request information from descriptions
and share the request/decoding pipeline. Do not build a second transport.

`RequestResult<T>` has fixed own fields `data`, `meta`, `envelope` and
`httpStatus`; API-supplied properties remain nested. It exposes the raw envelope
without forcing consumers to use rich resource wrappers. The error contract
includes HTTP status independently from HaveAPI envelope status, plus structured
errors and the parsed envelope when available. Type parameters describe the
caller's expected payload; they do not replace runtime envelope validation.

Generate `.d.ts` declarations from TypeScript for **both** public surfaces,
including callback overloads, RequestSpec, RequestResult, AsyncError, dynamic
invocation results and completion options. Publish them via the package `types`
field and included package files; do not maintain duplicate handwritten full-API
declarations. Endpoint/resource schemas remain separate from declaration emit
and their generation is deferred. Check actual TypeScript/Vite consumption of the retained
UMD/CommonJS package; add an additive bundler entry only if that proof requires
it. Do not assume the existing global bundle is automatically a working Vite
dependency or introduce ESM-only packaging.

The WebUI keeps a small adapter around this API:

- Supply the current token/provider headers at each request and set the current
  language; no stale credential snapshot or persistent token storage is added.
  Document header precedence and validation. Pass the caller's AbortSignal into
  the actual transport, including already-aborted signals; remove listeners
  after completion and preserve recognizable abort errors.
- On a qualifying HTTP 401, call the existing BFF/session refresh code with its
  session-identity guard. Retry GET/OPTIONS at most once under the existing
  policy. Never automatically replay mutations. Keep refresh orchestration and
  application-specific session-expired/resubmit errors in the WebUI adapter.
- Map the library's typed error/result to the existing WebUI-facing contract
  while retaining HTTP status, errors, metadata and raw envelope. Remove old
  fetch, query/body encoding and envelope parsing for migrated calls; this
  adapter owns application policy, not another HaveAPI implementation.
- Preserve response-first mutation acceptance and action-state receipts. React
  Query and the existing UI task tracker can continue polling separately; the
  application is not required to use the library's blocking completion helper.

A bounded proof-of-fit must cover one read, one mutation, HTTP/authentication
failure with refresh, cancellation and a blocking-action receipt before broad
consumer migration. Execution is authorized within the lead's assigned packages;
the addendum fixes how to prove fit without an unpublished dependency.

### Errors and server completion

New Promise methods reject an `Error` subtype, proposed `HaveAPI.AsyncError`,
with a stable `kind` (validation, transport, protocol, authentication, API,
action-failed, timeout or aborted), `message`, and available `httpStatus`,
`response`, `envelope`, `errors`, `state` and `cause`. Unavailable fields remain absent.
Preserve the underlying response/envelope rather than throwing only a string or
boolean. Do not claim to recover server detail already lost by a boolean-only
provider callback; extend the internal completion/error channel where needed.
Do not attach credentials or authorization headers to errors.

Normalize non-success HTTP replies, HaveAPI `status: false`, invalid/missing
envelopes, invalid JSON, network errors, local validation, incompatible
descriptions and callback-time exceptions. Each operation settles exactly once.
Timeout/abort handling must use an explicit transport error path; wrapping the
current outer method in `new Promise` cannot catch a later callback's throw.
Keep legacy callback behavior and synchronous throws covered separately.

Dynamic action calls and `request()` resolve on the successful API reply, including for a
server-declared blocking action. JavaScript asynchronous I/O and a server job's
completion are separate concepts; there is no server protocol change.

`waitForCompletion(result, options)` is the separate completion API:

- Use the existing protocol condition: a blocking action description plus
  `action_state_id` metadata. For an ordinary/nonblocking reply, resolve
  `{ value, response, state: null }` immediately; otherwise use action-state
  show/poll and resolve that wrapper with a successful terminal state.
- Reject failed terminal execution even when the polling HTTP/envelope status
  succeeded. Reject polling failure, malformed/missing state and local stopping
  rather than leaving a Promise pending. Preserve the original action response
  and final/last state in completion results or errors.
- Accept a positive overall `timeoutMs` and optional abort signal; require the
  timeout in the first version so the completion wait is bounded. This differs
  from the existing per-poll server timeout. Stopping/aborting local observation
  does not cancel server execution. Remove local timers/listeners on settlement.
- Server cancellation is an explicit API call to `action_state.cancel`, only
  when supported; its response may itself describe another blocking operation.
  Expose progress/terminal states as data-only snapshots; do not return legacy
  ActionState helpers. Cancel through an async action/request and stop tracking
  through AbortSignal. Keep legacy `ActionState.stop/cancel` behavior intact.
  Do not implement
  new completion by merely wrapping the existing `onDone` callback: that callback
  does not establish terminal success and may never run after local stop.

## Implementation boundaries and phased plan

The lead has assigned the initial packages described above. Later packages use
the following independent file boundaries and are released by the lead as their
dependencies become ready.

| Phase / suggested owner | Files and responsibilities | Dependency and acceptance |
| --- | --- | --- |
| 1 / architect + lead; build owner implementer0; fixtures implementer1 | Freeze both public contracts and shared internal types; `clients/js/tsconfig*.json`, package/build scaffolding and baseline callback/consumer fixtures | Establish callback behavior and supported runtimes before source conversion; build fixtures must exercise published JS exports |
| 2A / implementer0 | Convert `src/haveapi/{client,http,hooks,authentication,exceptions,i18n}.js` and `authentication/*.js` to `.ts`; own `src/haveapi.ts` export/build integration | Preserve callback timing, provider setup/MFA/logout behavior, hook order and error delivery; own shared type definitions, serialize build/export edits |
| 2B / implementer1, parallel after type scaffold | Convert `src/haveapi/{action,action_state,base_resource,resource,resource_instance,resource_instance_list,response,local_response,parameters,validator}.js` and `validators/*.js` to `.ts`; callback overload/type fixtures | Preserve callable objects, IDs/aliases/prototypes/attributes, save/lazy behavior, validation, undefined returns and synchronous throws; no callback bug fixes mixed into conversion |
| 3 / implementer0, coordinated with implementer1 | Extract typed internal protocol/request outcome helpers from the converted modules | Only after callback parity; share validation/serialization/transport while callback facade retains its original observable mapping/timing; independent per-client state |
| 4A / implementer0 | New `src/haveapi/async/{client,request,authentication,error,completion}.ts` and core/completion tests | Use phase-3 core; Promise setup/auth/request, AbortSignal, isolated state, reply-first receipts and bounded completion wait |
| 4B / implementer1, parallel on frozen core interface | New `src/haveapi/async/{resource,resource_instance,resource_list}.ts`, unit tests, `test/helpers/adapter_async.js` and type-consumer fixtures | Async dynamic actions/save/loadAssociation; non-thenable objects and explicit collision lookup; generated declarations, no callback helper leakage |
| 5 / implementer1; serialized build owner implementer0 | README/API examples, scoped `AGENTS.md` source/build guidance; finalize package `main`/`types`/files and generated JS/declarations | Both surfaces type-check and emit; one owner regenerates bundle; verify script tags, CommonJS and TypeScript/Vite imports |
| 6 / implementer1, WebUI pilot package | Structural/injectable API adapter and focused tests; one package-proof script/type fixture/browser test and npm script entry | Use disposable packed-artifact proof; default transport/dependencies/root lock/Nix hashes unchanged; preserve local interface; no broad page rewrites |
| Release / lead + retained reviewer + watcher | Quick checks, committed-deliverable review, then shared Ruby-server contracts, browser/WebUI integration and CI; release proposal | Future workflow only; publishing requires approval; broad WebUI adoption follows successful fit evidence |

Serialize edits to shared fixtures, export/build lists and Git operations.
Keep migration, shared-core extraction and new async behavior as separate
reviewable changes. Temporary mixed JS/TS build support may bridge conversion
packages; the final authored client implementation is TypeScript. Generated
locale/catalog inputs remain generated under their own procedure, and tests or
build scripts need not be converted merely because production source is.
Keep repairs to the **old callback** save/lazy-association implementation,
a fetch rewrite, ESM-only packaging and generated endpoint schemas outside the
initial change. The new async-owned save and explicit association loader are
included and tested independently. Automatic token renewal, OAuth flow/session
management and convenience logout are explicit first-release deferrals; no
callback-only substitutes are exposed. Broad WebUI migration follows the bounded
adapter trial; WebUI usability is initial acceptance. Route material contract
changes through the lead.

## Runtime, packaging, compatibility and recovery

### Selected TypeScript authoring and migration contract

Both Client and AsyncClient, including their resource/action/authentication
implementations, are authored in TypeScript. This is the selected design scope;
execution follows the lead's assigned packages and the addendum above.

Compile `.ts` with `target: ES5`, `module: ESNext` and declaration emit, then use
Rollup named-export UMD through the retained gulp entry as fixed in the addendum.
Keep `dist/haveapi-client.js`, CommonJS/AMD/browser contracts and the Client
export; add AsyncClient alongside it. No separate ESM runtime artifact initially.
Package compiled JS and declarations together, with `main`/`types` pointing to
those artifacts. `.ts` source is never the runtime entry. Plain JS consumers
need neither a TypeScript compiler nor a source rewrite: `require('haveapi-client')`
and a browser script exposing `HaveAPI` continue to work.

TypeScript types are erased and cannot validate network data. Keep runtime
description/envelope/input validation. Source typing also cannot infer endpoint
names loaded at runtime through OPTIONS: precise resource/action typing requires
application-authored or generated schemas, or the explicitly typed `request<T>()`
surface. Both exported client APIs receive generated declarations; JavaScript
build/test artifacts do not justify a second handwritten public-API definition.

For callback conversion, preserve argument/callback shapes, return values,
synchronous local throws, hook order and fire-and-forget behavior. Never add
`async` to callback methods as a convenience: that changes throws and returns.
Keep existing exception constructors and provider failure semantics observable
through Client; new Promise error normalization belongs to AsyncClient. Known
callback save/lazy-load defects are separate fixes, not incidental conversion.

Represent callback signatures and variadic action calls with overloads and
callable interfaces in source, including optional parameters and resource-curried
IDs. Preserve function-object prototypes, exported constructor/static access,
`this` binding and attribute descriptors; a mechanical rewrite into ES classes
can change these. Keep dynamic description/payload values at explicit typed
boundaries, narrow after validation, and use localized documented casts where
the runtime callable model requires them. Do not claim that a permissive index
signature or type assertion validates arbitrary API endpoint names or data.

Generate declarations for the complete callback and async surfaces from source;
author supporting interfaces/overloads in `.ts`, not a parallel full `.d.ts` API.
Check positive and negative type-consumer fixtures for callback forms, Promise
results and unknown dynamic endpoints. Source conversion must preserve JS
runtime exports: avoid accidentally requiring `.default` after CommonJS import.

Update HaveAPI's client-specific ES5 source/build guideline deliberately to allow
TypeScript authoring and generated JS/declarations for the JavaScript client.
This scoped guideline update supersedes the earlier async-only exception; it
does not change other languages/components. Choose emitted syntax for current
supported browsers and the preserved supported Node baseline. No generated
output is edited by hand; the serialized build owner maintains compilation,
bundling and package metadata.
Verify script-tag, CommonJS and TypeScript/Vite consumers of the **published
artifacts**, not imports of uncompiled source. No build was run in this pass.

### Existing constraints and rollout

The inspected npm package is version `0.29.0`, ships only `dist`, uses a CommonJS
`main`, and produces a browser/global/AMD/CommonJS UMD bundle through gulp.
The inspected repository instructions require ES5-style source; the selected
TypeScript migration includes the scoped guideline update above. The package
declares no `engines`; CI selects `lts/*`, so there is no evidenced minimum Node version.
Keep current entry points and XHR transport for this change. Do not add ESM-only
exports, `fetch`, `Proxy` or a syntax/runtime bump as an incidental dependency.

Target current, vendor-supported browsers, as requested; do not add obsolete
browser support or Promise/AbortController polyfills. Preserve public JS entry
points while moving authoring to TypeScript and using native Promise and
AbortSignal for the new surface.
`async`/`await` syntax can appear in consuming applications and examples. Test
current supported Chromium, Firefox and WebKit-family browsers and document the
tested versions at implementation time. Preserve Node operation and CommonJS;
its exact supported minimum remains a release prerequisite rather than an
invented new requirement. Runtime modernization beyond this is separate scope.

No persisted-state, database, protocol, Ruby/PHP/Go client, CLI, Terraform,
daemon, NixOS/vpsAdminOS configuration or migration change is needed. Old/new
clients may coexist with existing servers. No coordinated node update or server
deployment ordering is required. Rollback is a dependency/bundle revert, with
the consuming application's Promise calls reverted together; no data rollback
is involved. AsyncClient's explicit resource/action/attribute lookups retain
access to names reserved by its new object model. Test these collisions without
changing legacy name attachment globally. Do not mutate a callback instance to
make it async or reuse its mutable authentication/resource state.

The existing version/release process remains authoritative; do not invent a new
release number or publish without approval. The bounded React WebUI adapter
trial depends on the new typed client, then consumer rollout may proceed
incrementally after an approved package release. The initial pilot keeps the
default transport/dependencies unchanged. For the later default switch, revert
its dependency and adapter together for rollback; no
server deployment is required. Legacy WebUI and console integration are outside
the requested scope.

## Acceptance and verification brief

The investigation established source/dependency evidence; implementation checks
below are release gates, with actual results recorded by the implementers/lead.
Use HaveAPI's declared Nix shells and repository procedures.

Quick checks after implementation:

1. Type-check both client implementations, then run configured TypeScript JS and
   declaration emit followed by bundle generation in the declared environment.
   Run this through the retained gulp entry point using the accepted Rollup build.
   Check generated output and packed files: callback and async exports must work
   through the same script-tag/CommonJS contract without `.default`, runtime TS
   loaders or missing declarations. Compare callback runtime behavior before and
   after conversion at each migration stage.
2. Run focused Mocha unit/regression files, including async error delivery with
   deferred fake XHR callbacks. Cover malformed/empty JSON, network/open/send
   failures, validation without HTTP, HTTP errors and envelope `status: false`.
3. Preserve callback argument shapes, return values, local synchronous throws,
   fire-and-forget calls, hooks, aliases, curried/nested IDs and path cleanup.
   Test Client and AsyncClient side by side without state leakage or changes to
   callback return/throw behavior. AsyncClient rejects callback invocation forms
   rather than silently exposing a mixed API.
4. Verify async-owned result/resource/list classes, metadata/count/includes,
   all output layouts and low-level results; reject during materialization.
   Concurrent calls use independent IDs/options, and setup/auth publish state
   atomically. Test described `then` resources/actions/aliases and attributes
   through explicit lookup; resolving or awaiting async-owned objects must not
   execute them. Test create/update save identity/path refresh and failure
   atomicity, omitted versus invalid update identity, singleton/idless create,
   and successful create with missing required identity (successful response
   retained, local state unchanged, second create prevented). Cover readable
   unbound results and rejected ID-dependent sends; old-generation bound sends
   reject before transport, while dispatched calls retain their snapshot.
   Test cached and uncached association loads, loading errors, and no I/O
   during property access/list iteration. No returned object exposes a
   callback-only network helper or callback-owned provider/state object.
5. Cover setup failure, unsupported provider, description refresh failure,
   Basic/token/OAuth2 setup and async MFA challenge/rejection/missing handler. Preserve
   callback-only use without introducing Promise-returning legacy methods.
6. Test reply-first blocking/nonblocking calls and completion success, failed
   terminal status, polling errors, timeout, abort/local stop and cancellation
   as a separate potentially blocking request. Check single settlement and no
   polling/listeners after settlement.
7. Compile positive/negative TypeScript consumer fixtures against generated
   declarations from the packaged artifacts for both Client and AsyncClient,
   including callback overloads, callable resources/actions and Promise results.
   Compile the actual WebUI adapter with its normal TypeScript/Vite tooling.
   Exercise path-based GET/query and mutation JSON,
   strict envelopes and missing namespaces, HTTP versus API errors, current
   token/language headers and pre-start/in-flight AbortSignal cancellation.
   Prove one 401 refresh retry for reads, no mutation replay, stable-session
   protection and response-first action-state receipt handling. Check that
   migrated calls no longer retain a second fetch/serialization/decoder path.

After committed-deliverable independent review, run the existing shared contract
suite against both CallbackAdapter and the new AsyncAdapter using the Ruby test
API, plus the full JS suite and real-browser UMD smoke coverage. Existing
`npm test` includes server-starting contract tests; it is not assumed quick.
Use a fresh verification watcher for these uncertain/long checks. Ruby test-server
dependencies require the top-level/Ruby environment in addition to the Node-only
`client-js` shell. Retain the existing path/query, OAuth2 origin and localized
typed-validation tests. This design addendum alone does not trigger review;
completed substantive implementation follows the mandatory review workflow.

## Key source references

HaveAPI, at `06865bb847a564fe20e59ea6d72856c2f01a82e3`:

- `clients/js/package.json:1-38`, `gulpfile.js:6-43`,
  `src/haveapi.js:6-38`, `.github/workflows/clients-js-tests.yml:36-51`:
  package version/entry points, UMD build, browser/Node XHR and current CI.
- `clients/js/src/haveapi/action.js:18-30,128-130,173-213,221-343`:
  callable action methods, documented callback-free operation, invocation,
  argument parsing and existing undefined returns.
- `clients/js/src/haveapi/client.js:316-335,417-468,517-570,580-715`:
  setup/authentication, error loss/callback-time exception paths, logout and
  raw/rich response mapping.
- `clients/js/src/haveapi/http.js:18-66` and
  `src/haveapi/authentication/token.js:105-145`:
  transport missing structured error delivery and MFA callback semantics.
- `clients/js/src/haveapi/client.js:77-95,476-503`,
  `src/haveapi/base_resource.js:9-13,44-64`,
  `src/haveapi/resource_instance.js:271-305`: arbitrary attached names and
  the thenable-assimilation risk.
- `clients/js/src/haveapi/resource_instance.js:28-50,103-141,173-217`:
  rich response access, save and lazy-association caveats.
- `doc/protocol.md:479-491`, `clients/js/src/haveapi/action.js:381-435`,
  `src/haveapi/action_state.js:19-28,55-90`: server blocking identification,
  polling, final-status distinction and local stop/cancel.
- `clients/js/test/helpers/adapter_callback.js:9-18,63-84,91-125` and
  `test/contract/client_contract.spec.js:25-115`: existing test-only Promise
  wrapping and shared contract coverage, not production Promise support.

React vpsadmin-webui, at `7152729dcde326e00d16b5af0a46d0f60b431dbb`:

- `AGENTS.md:3-6` identifies React/BFF ownership separately from legacy PHP.
- All four root/BFF package manifest/lock files contain no `haveapi` match;
  the inspected locks contain 483 and 90 package entries respectively. This
  supports absence of both direct and transitive npm HaveAPI dependencies.
- `src/lib/api/haveapi.ts:405-514` exports `async haveApiCall<T>` returning
  `{data,meta,envelope}`, uses native `fetch` at line 471 and throws HaveApiError.
  `src/lib/api/vps.ts:229-235,263-268` uses that local adapter.
- `src/lib/api/haveapi.ts:434-490`,
  `src/lib/auth/bffSession.ts:36-70`: language headers, AbortSignal, session-aware
  OAuth refresh, retry of reads only and deliberate non-replay of writes.
- `src/lib/api/actionStates.ts:33-56` separates polling from request completion;
  `docs/design/ARCHITECTURE.md:35-50` and `bff/README.md:13` confirm SPA direct
  HaveAPI access and an OAuth/session BFF, not a resource-client proxy.

Consequently the planned upstream-client adoption needs behavioral parity for
typed results/errors, namespaces/metadata, headers, abort, refresh/session
identity, write replay prevention and action-state tracking. The user's reuse
goal is addressed by the typed request core and bounded adapter trial above;
preserve this application-specific policy while replacing protocol duplication.

Current supported browsers are the explicit baseline; obsolete browsers are
out of scope. The exact supported Node minimum and tested browser versions must
be recorded during implementation. No other unresolved design question blocks
this proposal.
