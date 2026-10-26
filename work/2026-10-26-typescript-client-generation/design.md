# Concrete TypeScript clients: investigation and proposal

Status: proposal, not an implementation or verified deployment. The user selected
one API version deployed with WebUI. Architect0 investigated HaveAPI JS/TS;
implementer0 supplied Go/Rust evidence and implementer1 supplied WebUI/vpsAdmin
evidence. Inspection used canonical bare repositories read-only, without fetching,
tests or live API calls. Cached refs do not establish current remote/deployed state.

## Recommendation

Support a HaveAPI TypeScript generator and a separate generated
`vpsadmin-typescript-client` package. Generate named async operations, per-action
inputs/outputs and metadata from a recorded schema for the API version used by
that WebUI release. This gives autocomplete and compile-time checks for operation
names, arguments, filters and result fields. Generate a small facade with an
injected request executor; keep HTTP, authentication and error handling in the
consumer's established runtime. For WebUI, adapt its existing `haveApiCall` and
retain its domain wrappers. An adapter for HaveAPI's `AsyncClient` can serve other
consumers later. A second standalone HTTP/authentication implementation is not
needed, and switching WebUI to the npm transport is not a prerequisite.

Keep the generic dynamic HaveAPI client for API exploration and arbitrary servers.
Declarations alone would improve autocomplete, but attaching a complete static
interface to permission-filtered dynamic properties can promise methods absent
at runtime. A generated facade offers stable names and one explicit execution
boundary. Its methods still can fail because of permissions or schema drift.

## Evidence and inspected revisions

| Repository | Explicit cached default revision |
| --- | --- |
| HaveAPI (`origin/master`) | `ec84ec874eb209ab59848873998456293ddf3c52` |
| vpsAdmin (`origin/master`) | `b82eeca50cd4dd7bd76728685c7de8aad66e7ba5` |
| vpsadmin-webui (`origin/main`) | `5a2d2bdc3ad7a827038f877d75959916528db844` |
| vpsadmin-go-client (`origin/master`) | `1d9240f3d27b5831baf3694baab5fe06294875d8` |
| vpsadmin-rust-client (`origin/main`) | `ff876abe17e3301da62c1b6afbda055ec89db9d2` |

Paths and line numbers below refer to these revisions, not bare local `HEAD`.

- **There is one JS/TS runtime.** HaveAPI `clients/js/package.json` and
  `clients/js/README.md` describe the TypeScript-authored npm package. Runtime dot
  properties already exist in `clients/js/src/haveapi/async/client.ts:101` and
  `async/resource_model.ts:253`. Generic declarations (`resource_model.ts:11`)
  cannot infer endpoint names fetched later. Callback `findResource`/`findAction`
  also safely resolve names that collide with JavaScript helpers
  (`clients/js/src/haveapi/client.ts:192`).
- **WebUI already has typed adapters and its own transport.** Its
  `tsconfig.json:3` enables strict checking; `src/lib/api/haveapi.ts:83` defines
  request options and `:405` implements `haveApiCall<T>`. `networks.ts:37` is a
  small adapter candidate; `vps.ts:194` translates UI options to wire filters,
  includes and pagination. These wrappers contain product behavior worth keeping.
- **Transport replacement would carry material migration risk.** WebUI
  `haveapi.ts:175` preserves omitted/null query semantics, `:369` selects language
  and authentication headers, and `:471` permits OAuth recovery replay only for
  GET/OPTIONS. `:270` and `haveapiEnvelope.ts:5` preserve uncertain-write receipts.
  Errors, metadata, cancellation, reconciliation and explicit write resubmission
  must survive the generated adapter unchanged.
- **Complete source-derived schema has a precedent, but export needs preparation.**
  HaveAPI `servers/ruby/lib/haveapi/documentation_clients.rb:62` builds Go/Rust
  naming adapters from the mounted DSL using a context with no user and no
  endpoint authorization; `documentation_schema.rb:5` strips structural copies.
  This private documentation machinery is not a supported export CLI.
  vpsAdmin `api/lib/vpsadmin/api.rb:325` loads configured plugins before mount;
  `cluster_resources.rb:463` reads database rows to define fields. A reproducible
  exporter must load the intended plugins and controlled schema fixture data,
  recording their provenance. Static Ruby source scraping is insufficient.
- **Permissions and response filtering remain runtime facts.** HaveAPI
  `servers/ruby/lib/haveapi/action.rb:213` filters descriptions;
  `authorization.rb:111` filters actual output. vpsAdmin
  `api/lib/vpsadmin/api/resources/network.rb:41` restricts fields/rows and
  `resources/vps.rb:117` limits member visibility. WebUI `networks.ts:72` and
  `nodes.ts:312` use OPTIONS to gate writes. A generated method's existence is
  not permission evidence.
- **Types do not validate responses.** HaveAPI `async/request.ts:103` and
  `async/resource_model.ts:224` cast payloads to caller-selected types. Server
  `parameters/typed.rb:132` can return null regardless of input nullability;
  filtered fields can be absent. Generate conservative action-specific output
  shapes, not a fully required universal resource model. WebUI's existing output
  shape checks remain necessary.
- **Borrow Rust's generation discipline.** HaveAPI
  `clients/rust/lib/haveapi/rust_client/snapshot.rb:7` records API/protocol/profile
  identity and canonical schema; `generator.rb:56` records input/output hashes
  and `:126` stages owned output with check mode. The Rust consumer retains
  `schema/provenance.json` and offline `tools/regenerate`. Go's
  `clients/go/lib/haveapi/go_client/generator.rb:37` normally describes a live
  API, while `:22` offers supplied-description generation. Prefer saved inputs;
  do not copy Go's silent unsupported-parameter omission
  (`input_output.rb:37`) or full-Show association assumptions
  (`parameters/resource.rb:24`).

## Proposed interface and initial slice

Illustrative syntax only; this package and interface do not exist yet:

```ts
import { createVpsAdminClient } from 'vpsadmin-typescript-client';

// Adapter retains haveApiCall's errors, receipts and auth/retry behavior.
const api = createVpsAdminClient({ execute: webUiHaveApiExecutor });
const result = await api.network.index({
  params: { limit: 50 },
  signal,
});
const networks = result.data; // Generated conservative NetworkIndexOutput
```

The generated package fixes API version 7.0 for this example, based on inspected
vpsAdmin `api/lib/vpsadmin/api.rb:2` and WebUI `src/app/config.ts:126`.
The executor contract carries method, version-relative path, namespaces,
parameters, metadata and cancellation, returning the existing data/meta/envelope
receipt. It must not accidentally duplicate the configured `/v7.0` prefix.
`fetchNetworks` remains a UI adapter; its operation serialization and handwritten
wire types can be replaced incrementally. No frontend language conversion or
BFF rewrite is involved.

Proposed independent implementation boundaries, for later lead assignment:

1. **Schema export and provenance:** HaveAPI exporter plus a vpsAdmin-owned
   controlled loading fixture; record API/protocol versions, source revisions,
   plugins, schema-defining data and digest. Establish completeness before claiming
   a full vpsAdmin client. This is the explicit prerequisite.
2. **Generator and executor contract:** a new HaveAPI generator directory, with
   deterministic fixtures, operation/type emission, collision diagnostics and
   owned-output check mode. Can develop against fixtures independently of export.
3. **Generated package:** proposed `vpsadmin-typescript-client` repository/package,
   consuming the accepted schema and generator; publish declarations and JS with
   provenance. Depends on the first two boundaries.
4. **WebUI pilot:** `src/lib/api` executor adapter and `networks.ts` read path,
   depending on the package contract. Retain runtime OPTIONS checks and domain
   semantics. Expand to writes and other domains only after the pilot is accepted.

## Invariants, compatibility and recovery

- Separate API version, HaveAPI protocol version, generator version and npm
  package version. Pin the generated package/schema with WebUI's release inputs.
  Do not silently select the server's default API version. One deployment pair is
  the primary target; arbitrary independently upgraded servers are out of scope.
- Generate per-action filters, required inputs and pagination from their actual
  input declarations. An output field is not automatically a list filter.
  Preserve omission versus explicit null, false, zero and empty string; distinguish
  ordinary input/output from global/object metadata.
- Use optional and, where necessary, nullable outputs; resource associations are
  partial references, not guaranteed full objects. Datetime wire values remain
  strings; unspecified Custom values remain `unknown`/JSON. Do not infer closed
  output enums, required fields or integer precision guarantees that the schema
  cannot support. JavaScript safe-integer handling needs an explicit policy before
  claiming lossless 64-bit support.
- Preserve canonical names and deterministic collision handling for helpers,
  aliases and names such as `then`. Reject unsupported schema constructs clearly
  rather than silently dropping operations or parameters.
- Runtime OPTIONS and server authorization remain authoritative. Generated full
  schema is never installed as a user's permission set. Runtime validation and
  schema drift can still reject statically valid calls. Existing HaveAPI async
  validation silently drops unknown inputs (`async/authentication.ts:25`), so any
  later adapter for that runtime must deliberately preserve or improve this
  behavior rather than assume TypeScript prevents stale inputs.
- Preserve WebUI authentication, impersonation, localization, envelope errors,
  metadata, AbortSignal, blocking-action receipts and uncertain-write handling.
  No automatic retry of writes, implicit association fetch or eager pagination.
- Prefer release-time schema drift checks and a tested API/WebUI pair. Roll out
  compatible API changes before the UI consumes them; require explicit ordering
  for incompatible changes. Browser tabs can retain an old bundle during rollout,
  so same-release deployment does not eliminate mixed-version operation.
- This proposal changes no database schema, persisted format, node protocol,
  CLI, Terraform contract or host configuration. Client rollback restores the
  previous WebUI/package pair; reverting UI code cannot undo accepted API writes.
  Schema fixture/export changes must not mutate production data. No deployment or
  publication is authorized by this investigation.

## Acceptance and verification brief

No checks were run: the deliverable is a source-backed recommendation. Future
implementation acceptance is a deterministic generated package whose network
pilot removes handwritten operation/wire typing while retaining WebUI behavior.
Autocomplete and compile-time rejection must work without `any` casts in callers;
permission failures and incomplete responses must still be handled at runtime.

Quick checks should cover deterministic regeneration, wrong operation/argument
compile failures, optional/null semantics, collisions, Custom/association shapes,
and adapter preservation of request and receipt fields. Use HaveAPI's component
Nix environment and established JS/type checks when changing its runtime; WebUI
has an existing `typecheck` script. Check schema coverage and input provenance,
not just successful compilation. Exact commands for the new generator/package
remain to be designed.

After implementation and required independent final review, longer checks should
exercise the pilot against a controlled matching API: authenticated member/admin
descriptions, denied writes, filtered fields, null clearing, cancellation, blocking
receipts and OAuth expiry without write replay. Include a bundled browser smoke
check with WebUI's TypeScript/Vite configuration and an old UI/new API rollout
case. Use the required verification watcher for long/uncertain checks. Actual
export completeness, package publication, deployed-version compatibility and
browser behavior are unverified; they are not blockers to this recommendation.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-26-typescript-client-generation/>

## Follow-up: use the HaveAPI 0.30.2 adoption as the baseline

Retain the work in `2026-10-24-vpsadmin-haveapi-upgrade`. Its recorded Package C
replaces WebUI's custom transport with npm `AsyncClient`, while retaining
`haveApiCall`, domain wrappers, BFF session policy, per-request credentials/locale,
public/authenticated isolation, error/receipt semantics and protection against
automatic write replay. Package C3 pins 0.30.2 without another adapter rewrite
([upgrade design](../2026-10-24-vpsadmin-haveapi-upgrade/design.md), lines 466–487
and 777–795). The proposed call chain becomes generated operations → WebUI
`haveApiCall` adapter → existing `haveapiRequestClient` → HaveAPI `AsyncClient`.
Do not restore a custom HTTP transport, duplicate decoding or call setup/authenticate
merely to reconstruct WebUI's existing policy on its already-versioned API base.

Our earlier WebUI evidence describes cached base `5a2d2bdc...`, not that upgrade.
Its current [state](../2026-10-24-vpsadmin-haveapi-upgrade/state.md), lines 50–66,
records WebUI candidate `f10d3d48c4f21cc39187c3667ffffd9952404c11` and vpsAdmin
candidate `70a2ed54b98d0c2f359a9cc4484452a257a9807b`. Use the upgrade's accepted
final successor as the WebUI implementation baseline once available through its
normal publication/integration process. Generator/schema work can proceed
independently; serialize subsequent WebUI adapter/package edits after adoption.
No work is transferred from that session by this assessment.

The user reports creating `vpsfreecz/vpsadmin-typescript-client`; the repository
is therefore the intended existing destination, while its contents and package
publication remain unverified. The schema-export prerequisite and generation
proposal are otherwise unchanged. This correction relies only on the explicitly
requested read of that session's plan/state/design/handoff, not its source or
worktrees. The dated handoff still describes 0.30.1 and is superseded by current
state: reviewed 0.30.2 work is not yet merged, legacy verification/cluster work
remains, and browser results retain two accepted preexisting mobile failures.
No implementation, fetch, test, deployment or integration was performed here.
