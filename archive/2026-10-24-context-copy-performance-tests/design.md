# Context derivation and documentation performance

Design owner: architect0. Implementation brief ready, 2026-10-24.
Reviewed source baseline: HaveAPI `39909094649b1d14a23f00615775ca7136acf4fd`.
Lead accepted the bounded scope below; application changes belong to implementers.

## Scope and evidence

Fix repeated whole-description copying in `ClientExample::Context#with` and
repeated whole-description normalization in the Rust documentation adapter.
Introduce required deterministic regression specs and a repeatable timing and
allocation benchmark. Only the HaveAPI repository needs changes. Do not change
vpsAdmin, generated SDKs, configuration pins, release versions or deployed systems.

The request reports 102.4 seconds per local administrator HTML request, with
639 context derivations consuming 88.8 seconds and 102.3 seconds process CPU.
Those are supplied measurements from a local API test environment, not production
measurements. This investigation confirmed the code paths but has not independently
reproduced those numbers. No before/after timing baseline has yet been measured.

Relevant paths and behavior at the baseline:

- `servers/ruby/lib/haveapi/documentation_context.rb`: constructor copies/freezes
  Hash, Array and String values; `with` invokes the constructor with all fields.
- `servers/ruby/lib/haveapi/server.rb:254`: `documentation_context` owns one
  root snapshot in a Sinatra request instance. `documentation_clients` derives
  a context for every availability check; `documentation_panels` repeats those
  checks and derives another context for every renderer.
- `servers/ruby/lib/haveapi/views/version_page.erb`, `version_page/auth_body.erb`
  and `version_page/resource_body.erb`: initialization, authentication and
  per-sample panels all use those helpers. Action panels explicitly pass the
  resource, action and sample from request-local `@help`.
- `client_examples/go_client.rb` and `client_examples/rust_client.rb`: the
  example bridges derive again with the supplied sample.
- `clients/rust/lib/haveapi/rust_client/documentation.rb`: `authentication`,
  `authorized_action` and `action_credentials` each normalize the complete
  description. A successful authenticated action normally traverses it twice,
  for each async/blocking variant.
- `mount_version` obtains `@help` using the current authenticated user and
  request parameters. `documentation_clients.rb` separately builds frozen
  mount-time profiles from a private structural schema, without prose, defaults
  or samples. The private model resolves SDK names; it is not permission evidence.

The existing context specs establish copying and frozen state, but do not assert
identity sharing or operation/allocation growth. Existing HTML authorization and
profile-mount specs cover hidden actions, fields, defaults and samples across
users. Rust adapter specs already cover unavailable actions, stale shapes,
authentication and source output. Extend that coverage rather than replacing it.

## Context interface and invariants

Keep `Context.new` as the boundary that takes ownership of untrusted caller
containers. Keep its public signature and field readers unchanged. Centralize
field normalization if useful so initial construction and changed values cannot
drift apart.

For an instance of the exact base `Context` class, `with(**changes)` shall create
a new frozen instance, share each unchanged field by identity, and normalize/copy
only fields explicitly supplied by the caller. A shallow `dup`, validated field
assignment and final `freeze` is a suitable implementation. Do not change the
public constructor to accept a caller-controlled trusted/frozen flag.

For subclasses, preserve the current `self.class.new(**existing_fields,
**changes)` path. This deliberately leaves subclass derivations unoptimized and
preserves overridden constructors, extra keywords, extra instance variables and
constructor side effects. Do not bypass subclass initialization through allocate
or dup. A subclass that accepts additional keywords must still receive them.

Preserve these semantics:

- Version, host and URLs use `to_s`, duplicate and freeze. `action_name` keeps nil;
  otherwise it uses the same string conversion. Resource paths map elements
  through `to_s` and copy/freeze the result. Existing invalid values, such as
  nil resource paths, must not silently become valid.
- Description, resource, action and sample recursively copy Hash keys/values,
  Arrays and Strings, freezing those copies. They do not freeze caller inputs.
  Mutable nested values in a shallow-frozen supplied Hash still require copies.
- Non-Hash/Array/String leaves retain existing pass-through semantics. This is
  not a new arbitrary-object deep-immutability guarantee. Cyclic input support
  and changes to Hash defaults/subclass behavior are outside this fix.
- Profile is intentionally shared as a reference, including explicit replacement
  or nil. Actual registered Profile instances and adapters are already frozen.
  Do not start freezing arbitrary caller-supplied profiles.
- Explicitly supplied values are changes even if equal to existing values.
  Do not infer provenance from `frozen?`, equality or an identity-keyed global
  cache. Missing fields and fields explicitly set to nil are different cases.
- Unknown keywords on a base Context continue raising ArgumentError; validate
  before changing the new object. No public reader silently appears.
- `with` with no changes returns a distinct frozen Context sharing all fields.
  The parent remains unchanged. Chains and sibling derivations are independent.

This changes identity of unchanged nested values between related contexts by
design. The values and rendering output remain unchanged. Custom subclasses keep
their constructor behavior. Existing renderers must already treat context-owned
containers as frozen.

## Rust selection before normalization

Keep adapter methods, frozen profile ownership and duck-typed context interface
unchanged. Add private lookup helpers if needed, but introduce no request or
process cache and no dependency on the server Context class.

Find the selected subtree in the raw authorized description first:

1. `authorized_action`: follow only resources along `context.resource_path`,
   then the selected action. Normalize that action subtree before existing
   compatibility and supplied parameter checks. Never trust `context.action`
   or the saved model as proof that an action is authorized.
2. `authentication`: select the requested advertised provider, normalize its
   complete authorized provider description and compare it with the normalized
   supplied authentication description as today. Keep saved-provider existence
   and header compatibility checks. Checking only a header would weaken this
   equality check and is not allowed.
3. `action_credentials`: retain public-action behavior and basic/token/oauth2
   preference order. Inspect only relevant provider presence and required
   headers. It need not recursively normalize provider resource trees or
   unrelated providers. Preserve normalization of any value actually compared.

Lookup must preserve existing normalized-key semantics: symbol and string keys
are supported at every traversed level; keys normalize with `to_s`; collisions
use the last inserted entry as `normalize` currently does. Preserve absent versus
present-nil/false distinctions where the old code uses `has_key?`, `fetch` or
truthiness. A shallow scan of an ancestor map is acceptable when necessary to
preserve these semantics; do not recursively normalize its unrelated children.
Do not silently substitute string-key precedence or create symbols for arbitrary
request names merely as an optimization. Preserve existing valid-input results
and documented limitation messages. Malformed shapes must not become authorized.

Repeated renders against a mutable duck-typed context must see updated supplied
values. Reusing an adapter across contexts, users or locales must not retain any
authorized description, rendered sample or authentication decision.

## Explicit performance bounds and remaining work

With a description of size D, N derivations and changed input of size C per
derivation, the context target changes from repeated O(N*D) deep-copy work to
one O(D) ownership copy plus O(N*C) supplied-value copying and fixed-field work.
Unchanged description identity and its owned descendants must survive derivation.

Rust normalization shall scale with the selected action/sample/provider, not
the descendants of unrelated resources. Ancestor lookup can depend on sibling
map width. Saved IR `resolve` still scans actions; no constant-time bound on the
entire Rust rendering operation is claimed.

The HTML template explicitly supplies resource/action/sample for each tab.
Those supplied objects still require copying. In particular, a very broad
resource containing many actions or deeply nested resources can remain expensive.
This is a known bound, accepted by the lead, not evidence that the original
whole-description regression remains. Do not claim every page shape is linear
or every future performance regression is impossible. Benchmark both broad
resource sets and concentrated actions to make this remaining cost visible.

Do not add server-level rendered-output caching, availability caching, shared
authorized models, generic memoization or an IR-index refactor in this change.
Further optimization requires new evidence and a brief routed through the lead.

## Independent implementation packages

All paths below are relative to the HaveAPI worktree. Four implementers can edit
these exclusive file sets concurrently. Lead assigns actual owners and serializes
Git/index operations and dependency installation. Only architect0 edits this
design file. Implementers report material deviations before expanding scope.

| Package | Exclusive files | Dependencies and result |
| --- | --- | --- |
| A: context ownership | `servers/ruby/lib/haveapi/documentation_context.rb`; `servers/ruby/spec/client_examples/context_spec.rb` | Independent. Implement derivation sharing, constructor parity and subclass fallback, with behavioral regressions. |
| B: Rust normalization | `clients/rust/lib/haveapi/rust_client/documentation.rb`; `clients/rust/spec/unit/documentation_spec.rb`; new `clients/rust/spec/unit/documentation_performance_spec.rb` | Independent of A; retain duck-typed contexts. Select authorized subtrees, prove output/auth parity and bounded normalization work. |
| C: deterministic request regressions | new `servers/ruby/spec/client_examples/context_performance_spec.rb`; new `servers/ruby/spec/documentation/performance_spec.rb`; new `servers/ruby/test_support/documentation_performance_fixture.rb` | Write against A contract now; passes after A. Own reusable synthetic fixture, derivation allocation growth, real HTML request identity/isolation checks. |
| D: benchmark and contributor docs | new `servers/ruby/benchmarks/documentation.rb`; `Makefile`; `doc/client-examples.md`; `doc/agent-instructions/development.md`; `clients/rust/docs/documentation.md` | CLI/report scaffolding independent; real-page benchmark consumes C fixture. Document final behavior after A/B, calibrate and retain before/after evidence through lead. |

No workflow edit is required: server `bundle exec rspec` discovers C's specs on
Ruby 3.2/3.3/3.4; Rust CI runs every `spec/unit` spec. Both workflow path filters
cover the changed components. If a concrete coverage gap requires a workflow
change, route ownership to D through the lead and read the applicable workflow
procedure, including fresh upstream action verification, first.

### Shared fixture contract between C and D

`servers/ruby/test_support/documentation_performance_fixture.rb` must load without
RSpec and expose `HaveAPI::DocumentationPerformanceFixture.build` with keywords
`resource_count:`, `actions_per_resource:`, `samples_per_action:`, and
`parameters_per_action:` (positive small integer defaults permitted).
Return a mounted `HaveAPI::Server`; caller uses `server.app` with Rack::MockRequest.
Use API version `1`, mount `/benchmark/api/`, a stable host `example.test`, and
the HTML route `/benchmark/api/v1/`. Generated names, values and ordering are
deterministic. Build separate servers, without modifying a shared registered API.

The fixture contains valid request/response samples with nested Custom data,
zero/false/empty/null values where the action contract permits them. Provide
Basic users `admin` and `member` with password `fixture-only`; admin-only actions,
fields/defaults and sample markers allow explicit leakage assertions. These are
synthetic test credentials, never real accounts. No network server, database,
compiler or formatter is required. Preserve existing anonymous documentation
semantics; do not redefine them as part of this performance fix.

Dynamic renderers are the default. An optional keyword `rust: false` may enable
a real Rust profile with a synthetic crate name, only when its generator is
available. Optional Rust dependencies must not become required for server specs.
C and D may agree a simpler variant before implementation, but report any changed
interface through the lead; do not independently create two fixtures.

Mount/schema/profile preparation is separate from a timed HTML request. Benchmark
setup must not be mistaken for request CPU. D can require the Rust adapter and
prepare its optional measurement lane without compiling a generated SDK.

## Required acceptance and deterministic gates

### A: ownership and compatibility

Exercise every field and compare derived values with the old constructor's
equivalent values. Verify identities for unchanged owned data and profile; verify
changed nested containers/strings are detached and frozen while source inputs
remain mutable. Mutate supplied nested values after construction/derivation and
assert parent/child/siblings do not change. Include shallow-frozen containers,
string keys, resource-path conversion, action-name nil, nil-valued optional
fields, missing versus explicit replacement, no changes and unknown keywords.
Use a subclass with a constructor counter and an extra keyword to show that
derivation still invokes its constructor and returns that subclass.

### B: Rust traversal, output and authorization

Render the same selected action in async and blocking modes against descriptions
that differ only by large unrelated nested subtrees. Preserve full result equality
(source or limitation) and assert normalized-node work is independent of those
unrelated descendants. Instrument calls around public `render` in the test;
do not expose production counters. Account for recursive normalization, not only
top-level method invocation count. Include auth render and action credentials,
unknown/hidden providers, missing selected actions and changed parameter types.

Test symbol/string/mixed keys and both collision insertion orders. Keep complete
provider-description equality checking. Re-render with changed mutable supplied
descriptions/samples/headers on the same adapter to detect stale retained values.
Alternate admin-like and member-like contexts through one frozen adapter and
assert hidden saved names/defaults/values never enter restricted output.

### C: complexity and allocation growth

Use at least two substantially different description sizes (for example 8 and
128 synthetic resources) with a constant selected action/sample. Construct and
warm both parent contexts before measurement. Run a fixed number of profile-only
and constant-small-sample derivations per case. Assert each derived description
is the parent object, all unchanged fields share identity, and parents from
separate requests do not share their ownership copies.

Measure `GC.stat(:total_allocated_objects)` deltas around only the derivation
loop, outside expectations, fixture creation and JSON serialization. Use a few
warm repeated batches and minimum allocation count to reduce incidental VM
bookkeeping; no GC disable across a request and no heap-byte absolute budget.
The size-growth allowance must be a generous fixed amount per derivation, not
proportional to D. Calibrate it on supported Ruby versions and record observed
small/large values and why it rejects the original constructor path. Do not
invent final thresholds before seeing actual counts. Pair this gate with the
identity/work assertions so runtime-specific allocation slack cannot hide a
whole-description copy. New data explicitly supplied through `with(description:)`
must still be copied; the performance expectation applies to unchanged data.

Render real HTML pages from C's fixture. Capture contexts passed to public
renderers while invoking their real methods. Assert status 200, expected sample
panels and normal client variants, one shared description identity throughout
each request, and a different root snapshot on subsequent requests. Alternate
admin/member/admin requests through the same app and inspect HTML and captured
contexts for action/field/default/sample leakage and correct privileged output
restoration. Confirm the original request-help containers remain unmodified.

The request regression should fail the old copying implementation without a
wall-clock threshold. An optional instrumented copy count can supplement these
assertions, but must distinguish whole-description copies from legitimate copies
of explicitly supplied resource/action/sample fields. Avoid large fixture counts
that turn ordinary server CI into a benchmark campaign.

### D: repeatable measurement and evidence

Provide a documented command, preferably `make benchmark-documentation`, that
runs the synthetic harness in the declared environment and prints machine-readable
JSON. Include Ruby engine/version, source revision (or explicit supplied revision),
fixture dimensions, selected renderers/profile mode, warmup/trial counts, wall
time from a monotonic clock, process CPU time and allocated objects. Include
HTML byte count/digest and status so an accidental empty/failed result cannot
appear as a performance improvement.

Separate context derivation, representative full HTML request and optional Rust
adapter lanes. Report every trial plus median; avoid comparing one noisy run.
Default sizes/trials should remain practical, with explicit options for a larger
campaign. Use both many-small-resources and many-actions-in-one-resource shapes.
Keep setup, mount and dependency preparation out of request measurements and
report them separately if useful. Do not include generated client compilation.

Run the identical harness/fixture against the recorded baseline and candidate in
equivalent dependency/runtime environments, before claiming measured improvement.
Retain exact heads, lock/input identities, commands, fixture parameters, host
identity and raw result JSON under this session through the lead. Record output
parity for baseline/candidate, or explain the exact normalized volatile fields
if any; do not weaken comparisons just to make them pass. A small focused
derivation baseline can prove the old algorithm fails the deterministic gate.
Broader runs or uncertain setup must be launched by the verification watcher.

No timing limit belongs in ordinary PR CI initially. Optional benchmark output
can be archived in CI later; a controlled dedicated runner can support measured
latency budgets once variance and stable baselines are known. Scheduled scaled
page/request workloads and production observability are broader options, not
implied deployment work. These layers detect this regression class; no finite
test suite guarantees the absence of all future performance regressions.

## Checks and execution order

Read repository `AGENTS.md` and `doc/agent-instructions/development.md`, use its
Nix environments and prepared bundles, and run `make doc` before server specs.
Dependency setup can take time and must not race across members. Lead owns
preparation and watcher coordination. Known focused specs/lint run inline only
when their environment is already prepared and duration is bounded.

Quick checks by package:

- A: `bundle exec rspec spec/client_examples/context_spec.rb` from server root;
  RuboCop on its changed source/spec files.
- B: `bundle exec rspec spec/unit/documentation_spec.rb
  spec/unit/documentation_performance_spec.rb` from Rust root; changed-file
  RuboCop. No Cargo invocation is needed for this Ruby adapter change.
- C: focused new specs plus `spec/documentation/auth_filtering_spec.rb` and
  `spec/client_examples/profile_mount_spec.rb`; changed-file RuboCop.
- D: Ruby syntax/lint, benchmark CLI smoke with minimal fixture, JSON schema/data
  inspection and documentation command/link checks. A real benchmark campaign is
  longer verification and is watcher-owned.

After all intended changes are committed and quick checks pass, mandatory
independent final review covers the entire branch, ownership/security contract,
test effectiveness, complete history and absence of migrations. Long verification
then uses a fresh utility watcher: full server specs, Rust generator unit suite,
`make test-documentation` where relevant dependencies are prepared, and bounded
baseline/candidate benchmark campaigns. Existing Rust compiled-snippet acceptance
is available if output changes or unresolved type/wire concerns justify it; this
change intends byte-identical source and does not alter runtime code. Inspect CI
for the exact published candidate, including Ruby 3.2/3.3/3.4 allocation behavior.

Prove that the new regression assertions fail the original defect in an isolated
baseline run, without changing shared defaults or another session's worktree.
Lead coordinates any additional baseline checkout/copy and retains evidence.

## Documentation, compatibility, deployment and recovery

Primary readers are HaveAPI maintainers, renderer-extension authors and people
diagnosing slow HTML documentation. D updates `doc/client-examples.md` to explain
that construction owns a request-local copy and derivation shares unchanged owned
data. Explain the profile exception and subclass compatibility without claiming
arbitrary-object deep freezing. Link benchmark instructions from existing
verification sections; Rust-specific traversal rationale belongs in its adapter
guide. Baseline/candidate measurements and the original incident remain session
evidence, not unsupported production claims in permanent documentation.

No persistent format, schema, migration, seed, wire protocol, client API,
Terraform contract, Nix option or SDK generation contract changes. No migration
reset or coordinated all-node update is required. Old/new workers can serve the
same API and documentation; values, source snippets and auth boundaries must
match. Updating only the server fixes copying; updating the optional Rust generator
adds its normalization improvement. Existing generator-version matching rules
still govern installation; do not loosen them or publish versions in this task.

No deployment is authorized by this design. For a later authorized release,
deploy compatible server/generator gems by the existing process and verify
request isolation plus representative local timings. Rollback restores prior
packages, losing the optimization but needing no data conversion or recovery
migration. Do not put caches or persisted benchmark state into the request path.

Session remains open. This brief authorizes no merge, deployment, publication,
lifecycle operation, machine release or cleanup.

## Phase 2: endpoint performance and required CI — READY, 2026-10-25

The user approved implementation of the broader plan. This section governs the
expansion; the original design and completed evidence above remain historical.
Starting head and fixed accepted reference are
`b85ec364057f536940d689b09e612512ffffaf82`. Scope is HaveAPI Ruby endpoints,
real ActiveRecord SQLite, and documentation; no vpsAdmin or production changes.
The architect owns this brief; the lead owns assignments, records and Git windows.

### Exclusive implementation paths

| Owner | Exclusive paths relative to HaveAPI | Result/dependency |
| --- | --- | --- |
| implementer0 (A) | `servers/ruby/test_support/performance_endpoint_fixture.rb`; `servers/ruby/spec/performance/endpoint_contract_spec.rb`; `servers/ruby/spec/performance/endpoint_scaling_spec.rb` | Neutral API scenarios and contracts; independent of B/C/D. |
| implementer1 (B) | `servers/ruby/test_support/performance_sqlite_fixture.rb`; `servers/ruby/spec/performance/sqlite_spec.rb` | Isolated SQLite scenarios, exact query and authorization counts; same interface as A. |
| implementer2 (C) | `servers/ruby/benchmarks/endpoints.rb`; `servers/ruby/benchmarks/performance_compare.rb`; `servers/ruby/benchmarks/performance_budgets.json`; `servers/ruby/spec/performance/runner_spec.rb`; `servers/ruby/spec/performance/comparator_spec.rb`; `servers/ruby/spec/performance/support/` | Runner, small comparator, budgets and detector controls; consumes A/B and existing documentation fixture. |
| implementer3 (D) | `.github/workflows/servers-ruby-performance.yml`; `utils/performance_ci.rb`; `servers/ruby/spec/performance/event_baseline_spec.rb`; `Makefile`; `doc/performance.md`; `doc/agent-instructions/development.md`; `doc/client-examples.md`; `README.md` | Event baseline resolution, workflow, commands and links; consumes C CLI. |

No owner edits production runtime code or another owner's files. Existing
`benchmarks/documentation.rb` stays unchanged; reuse its measurement ideas and
existing documentation fixture through C's bounded adapter. No benchmark framework.
A/B send measured count contracts to C, who alone writes budgets. A/B/C/D can
code concurrently now. Suggested commit order A, B, C, D; the lead grants each
Git window, preserving unrelated staged/working files. C/D may use contract stubs
in their own tests until A/B arrive, never publish stub measurements as evidence.

### Shared scenario contract, version 1

A defines `HaveAPI::PerformanceFixtures::Endpoints`, B defines
`HaveAPI::PerformanceFixtures::SQLite`. Both expose:

```ruby
cases(profile: 'quick') # [{ id: 'api.public_get', dimensions: {} }, ...]
build(case_spec)       # new isolated scenario; no RSpec dependency
```

Each scenario implements exactly this small duck-typed interface:

```ruby
scenario.reset!(iterations: count) # seed/reset; prepare counters outside timer
response = scenario.call          # actual Rack request, returns Rack response
identity = scenario.validate!(response, index: 0) # pure, after timer; raises on error
counts = scenario.counters        # after timer; JSON-safe per-operation records
scenario.close                   # close owned subscriptions/connection, ensure path
```

Lead-approved clarification (2026-10-25): endpoint scenarios may expose an
`attr_reader :app` for untimed Rack CRUD/error contract specs. This adds no timed
operation, alternate request flag or case ID. Direct requests outside an active
`scenario.call` slot must not create, advance or mutate timed counter records.
`reset!` restores fixture state and operation records before subsequent batches.

`validate!` returns `{http_status:, envelope_status:, body_bytes:,
body_sha256:, canonical_sha256:}`; envelope_status may be nil for HTML.
Canonicalization preserves types, array order and values, and ignores only Hash
map ordering; detect duplicate normalized keys. C owns the shared identity helper
in `performance_compare.rb`; A/B may initially return their validated parsed body
as `canonical_body:` for C to hash, while retaining raw bytes/digest. No broad
volatile-field deletion. The final helper call is pure and outside timing.

`counters` returns `{operations: [{queries: 0, authorizations: 1, executions: 1},
...]}` with exactly `iterations` records. A/B preallocate records in `reset!`,
and `call` increments the current operation's record. Absence of an expected
record/count is an error, not zero. Use zero queries for in-memory scenarios.
Authentication/authorization counts are scenario-specific contracts; do not
assume every endpoint makes one permission check. Every response and counter
record is validated; checking only the last response is insufficient.

C preallocates response slots outside measurement, calls reset!, runs GC.start,
then times only the fixed request loop and records allocations/CPU/wall. All
response parsing/digests/assertions and counter inspection occur after timing.
Mount/schema/seed/token issuance/reset are excluded. GC stays enabled. Each
baseline/candidate sample uses an isolated process, never both code roots in one
Ruby VM. Fixture files use `require 'haveapi'` only after C selects the source
root. Do not directly load candidate `client_test_api.rb`: its require_relative
can load candidate runtime during a baseline run. Reuse its endpoint contracts
and provider patterns in neutral fixture definitions. Verify loaded Server,
Action, adapter and dependent Ruby client paths against selected source roots.

B uses a named abstract AR base with its own connection; never changes an
unrelated global Base connection. SQLite schema/database/subscriptions are owned
and closed by the scenario/process. Use explicit eager include paths and
query-cache policy, exclude setup/schema/transaction SQL, and preserve per-row
authorization. Fixture authorization/prepare must not perform per-row finds.
Do not change production reflection/default-includes behavior to make counts pass.

### Stable case IDs and dimensions

Quick timed cases are:

- A: `api.public_get`, `api.basic_get`, `api.token_get`, `api.typed_post`,
  `api.invalid_post`, `api.nested_get`, `api.list` (`rows: 32`).
- B: `sqlite.page` (`rows: 128, page_size: 32`), `sqlite.includes`
  (`rows: 32, include_depth: 2`).
- C documentation adapter: `docs.options`, `docs.html_resources`,
  `docs.html_actions` (`size: 8` for each).

Treat `(id, dimensions)` as the unique key; do not encode dimensions into IDs.
Weekly retains IDs and adds sizes through dimensions: list/includes to 1024,
SQLite table to 10000 with page_size32, documentation size16, member/admin
variants through `user:` dimensions. Optional weekly Rust IDs are
`rust.async_example`, `rust.async_auth`, `rust.blocking_example`,
`rust.blocking_auth`, with a separately matched Rust dependency graph.
SQLite pagination MAX_LIMIT is 1000: 1024-row output is an unpaginated
serialization/full-relation case, never an invalid limit request. All fixed
page cases remain page_size32.

Lead-approved endpoint weekly inventory clarification (2026-10-25): retain A's
seven quick cases and their already-used dimension keys unchanged. Add
`api.list` with `rows: 1024, user: 'member'`, `api.list` with
`rows: 1024, user: 'admin'`, and `api.basic_get` with `user: 'admin'`, omitting
any exact duplicate. Quick protected cases default to member. Do not add a
role Cartesian product for typed/token/nested cases: their quick workloads and
deterministic role/isolation specs supply that coverage. C consumes this inventory
through `cases(profile:)`; it must not synthesize extra combinations.

Deterministic specs cover sizes1/32/128, fixed page32 over tables32/128/1024,
malformed JSON and auth/route errors, CRUD state/reset, hidden-field isolation,
zero/false/empty/null/omitted values and changed output shapes. HaveAPI typed
validation normally returns HTTP200 with status:false; malformed JSON is400.
Do not mistake a fast failure or missing sample for success.

### CLI and JSON contract between C and D

```sh
ruby servers/ruby/benchmarks/endpoints.rb run \
  --baseline-root /absolute/baseline --baseline-sha FULL_SHA \
  --candidate-root /absolute/candidate --candidate-sha FULL_SHA \
  --profile quick --budgets servers/ruby/benchmarks/performance_budgets.json \
  --output /absolute/new-evidence-directory
ruby servers/ruby/benchmarks/endpoints.rb compare \
  --input /absolute/evidence/samples.json \
  --budgets servers/ruby/benchmarks/performance_budgets.json \
  --output /absolute/new-comparison-directory
```

Profiles are `quick` and `weekly`. C's private `worker` mode is an internal
subprocess protocol, not another D orchestration entry point. `run` produces
`samples.json`, `report.json` and per-process diagnostics; `compare` consumes
the exact same versioned samples schema and emits report.json. Exit codes:
0=pass, 1=regression, 2=inconclusive, 3=error (including contract/provenance/
missing-workload failures). All nonzero codes block. Invalid inputs fail closed.

Minimal report example:

```json
{"schema_version":1,"status":"pass","profile":"quick",
 "baseline_sha":"FULL_SHA","candidate_sha":"FULL_SHA",
 "harness_sha256":"DIGEST","fixture_sha256":{},"budget_sha256":"DIGEST",
 "environment":{},"cases":[{"id":"api.public_get","dimensions":{},
 "iterations":100,"self_pairs":[],"pairs":[],"classification":"pass"}]}
```

Each self/comparison pair retains order, both per-request wall_seconds,
cpu_seconds and allocated_objects, operation counts, output identities and
counter records. `samples.json` also binds complete case inventory, source paths,
input/lock hashes and Ruby/gem graph. C may add fields but must not rename these
keys or exit codes without notifying D and the lead. Case/report failure cannot
be converted to a missing case, success or automatic baseline update.

### Locked gate policy

Quick uses three AA self-noise pairs and nine AB pairs with alternating AB/BA
order and two warmup batches per process/case. One baseline pilot selects count
1..2000 targeting150ms; use the same count for both revisions. Record when the
cap cannot achieve target duration; do not pretend the target was reached.
Weekly uses five AA and fifteen AB pairs. No automatic retry-until-green.

For each case and EACH wall/CPU metric, per request, let
`T_i=max(0.20*B_i,0.00020)` and `E_i=C_i-B_i-T_i`. Noise is
`N=max(max(abs(AA differences)),0.05*median(B),0.00005)`. Regression requires
at least8/9 E_i>N; pass requires at least8/9 E_i< -N; otherwise inconclusive
blocks. Weekly requires14/15. This is a conservative agreement rule, not a
claimed statistical confidence interval. High noise never widens the budget.
Keep raw observations, no aggregate score masking a slow endpoint.

Allocations block above baseline median plus max(10% baseline,32 objects/request).
Fixed reference ceilings are measured accepted-reference counts with25% headroom
plus32 objects/request. Query ceilings are exact measured integers per scenario
shape, with separate required authorization counts. Scaling bounds follow actual
output work; do not require constant allocation for growing responses. Populate
counts through small focused calibration, never invent counts or silently relax
them. Uncalibrated/mismatched budgets block readiness. C owns budget writes;
A/B supply measurements and rationale; lead/reviewer accept changes.

### Workflow, baseline and compatibility policy

D supplies push, pull_request, workflow_dispatch and Sunday03:00UTC weekly
(`0 3 * * 0`) triggers. Quick job hard10min (target5–10min); weekly hard30min.
Always-created change-detection/aggregate status prevents required checks being
left pending by path filters. Relevant sources, dependencies, fixtures, budgets,
workflow and flake inputs trigger work. Use read-only permissions, ephemeral
fork-safe runners, persist-credentials:false, no secrets/release context or
pull_request_target execution. Preserve30day failure/inconclusive artifacts;
cancel only superseded runs for the same branch/PR. Verify official action refs.

Baselines are explicit immutable SHAs:

- PR candidate=head.sha; baseline=merge-base(head,event base.sha); no accidental
  synthetic merge checkout. Feature push baseline=merge-base(after,captured
  default SHA). Compare the whole feature, not only its last push.
- Default push candidate=after, baseline=before for the whole batch, never HEAD^.
- Weekly current default vs fixed accepted b85ec364 above; require reference
  ancestry and preserve that object/lineage. Do not use the pre-fix baseline.
- Manual explicit full candidate/baseline SHAs, otherwise default vs fixed
  reference. Missing/zero/unavailable/unrelated baseline blocks; no HEAD-vs-HEAD
  fallback. A new feature branch still uses its merge-base with default.

Run identical neutral fixtures/harness on both code roots with one compatible
third-party dependency graph. Keep resolved locks as artifacts, not tracked
library lockfiles. Incompatible graph, fixture interface, config or provenance
blocks; a separate reviewed environment/reference migration is required.
No automatic budget update or rebaseline. Keep exact raw/canonical outputs,
case inventory, SHA graph, source/input graphs, tool versions, orders/samples,
SQL/counter evidence and classifications. SQLite/Rack measurements make no
production DB/server or vpsAdmin latency claim.

### Acceptance, verification and release boundaries

A/B prove response contracts and scenario reset/connection isolation with focused
specs. C proves real CLI failures for allocation amplification, extra query,
slowdown, noisy inconclusive, missing results and wrong outputs: live isolated
fixture controls for work/query faults and controlled sample replay for timing
classification. The complete CLI/subprocess path and exit status must be tested,
not only comparison arithmetic. Controls live in C's test support; no production
defect flags. D tests PR/default multi-commit/feature/new-branch/missing/manual
event selection and the aggregate status behavior. Stock AA comparisons must
pass with clean deterministic controls.

Small focused calibration/quick checks may precede final review. Record actual
runtime/noise/counts and disclose gaps. Once all intended source is committed
and quick checks pass, mandatory independent whole-branch review precedes long
campaigns/workflow verification. Run those through the required utility watcher,
record exact final-head results, and satisfy both quick and weekly profile
calibration before readiness; timeout/inconclusive is a blocker to diagnose.
Retain original review/campaign evidence, including the narrowly proven resource
map-order comparison, without overwriting historical results.

No persisted application formats, API/wire contracts, production configuration
or migrations change. Fixtures use disposable owned process/database state.
The workflow can be reverted with ordinary source changes; reference receipts
remain evidence. No merge, deployment, publication, lifecycle action or cleanup
is authorized by this implementation brief.

### Accepted runtime and feasibility clarifications, 2026-10-25

The actual inventories are **12 quick cases and 32 weekly cases**. Earlier
coordination referred to 31 weekly cases; the retained worker inventory is
authoritative. Keep all cases, pairs, warmups, pilot selection, thresholds and
timeouts unchanged. No profile/model sharing across scenarios has been approved.

The worker owns runtime policy: set `RACK_ENV=test` before loading ActiveRecord,
HaveAPI and their dependencies in its fresh subprocess. Verify this through an
actual worker regression started with RACK_ENV initially absent, asserting clean
JSON output and recorded test policy. A fixture is not responsible for making an
unspecified development environment silent. ActiveRecord8 can log through the
global `ActiveRecord::Base.logger`/LogSubscriber even when a fixture subclass
sets its own logger to nil. The ineffective subclass-logger experiment was
rejected and removed from the tree. Do not replace it with a global logger
mutation or a fixture guard rejecting another test's global logger: either would
violate fixture ownership or create random-suite order dependence. Keep named
connection isolation and the existing runner pre-load policy.

The [single-operation weekly calibration](phase2-c-weekly-calibration.json) and
[execution receipt](phase2-c-weekly-result.json) record a successful 42-second
command with two warmups and one measured operation per case. That duration
includes the Nix invocation and unseparated setup, GC, validation and output
work. It is not a full weekly campaign or evidence that the 30-minute job fits.

Read-only projection using those observations and the existing pilot formula:

| Quantity | Seconds |
| --- | ---: |
| Sum of one measured operation across 32 cases | 5.230 |
| Sum after selecting counts with ceil(0.150 / wall), clamped1..2000 | 8.730 |
| Approximate two warmups plus measured request work per counted worker | 26.191 |
| Added request work versus the one-operation calibration | 10.503 |

Assuming unchanged residual overhead and comparable baseline/candidate speed,
`42 + 40 * (42 + 10.503)` projects about2142seconds, **35.7minutes** before
additional job setup/artifact overhead. The request-work-only projection is
about17.7minutes. Neither is a measured bound: warmup durations and nonrequest
stages were not separately retained, and hosted runners can differ. With a
three-minute job setup/artifact reserve, post-pilot workers would need to average
about39.45seconds, leaving about13.26seconds for their nonrequest work. Do not
attribute the unexplained residual to SQLite or promise an optimization saving.

C may add **untimed stage telemetry** for dependency loading, scenario build,
reset, GC, warmup request/validation, measured request/validation, close and
serialization/worker elapsed. Place new observations outside the measured request
loop and its allocation/CPU/wall snapshots; do not change what an operation
measures. First use a bounded, lead-authorized calibration through the required
watcher to identify material costs. No long paired campaign precedes final review.

C may consolidate redundant after-timer JSON roundtrips and repeated canonical
tree traversals. The inspected pipeline canonicalized while parsing, again while
digesting the fixture identity, roundtripped identity/body through JSON, then
canonicalized again in the worker. Removing duplicate transformations must
retain **every-response** contract validation, typed values and array ordering,
duplicate-key rejection, raw bytes/SHA and canonical identity checks, and every
operation's query/authorization/execution records. Equal digests do not permit
skipping response validation. Timing/noise policy remains identical; retain the
new harness identity and any required focused calibration evidence.

SQLite already creates and bulk-seeds its three tables once per scenario;
`reset!` resets only operation records. No repeated reseeding optimization is
available there. Keep each scenario's own database/connection. Neither a shared
DB nor shared prepared documentation/Rust profiles is approved by this note.
The weekly30minute feasibility gate remains open until measured evidence confirms
the complete accepted profile fits, or a consequential change is returned to the
lead/user. Do not reduce workloads, pairs, checks or budgets to obtain a pass.

### Accepted verification location clarification, 2026-10-25

The lead explicitly supersedes the plan's earlier requirement for both local
and hosted runtime/noise acceptance. **One complete exact-final-head hosted
execution of each quick and weekly profile may jointly satisfy paired campaign,
self-noise, runtime feasibility and hosted integration acceptance.** An equivalent
local repetition is not an additional gate. The hosted wrapper executes the
actual standalone CLI against exported baseline/candidate roots; this changes
execution location only. Full paired performance on aitherdev remains unmeasured,
and no local paired pass is claimed. Preserve earlier samples and decisions.

All workloads, pair counts, orders, warmups, pilot rules, budgets, strict output
and counter checks, blocking outcomes and deadlines remain unchanged. Acceptance
requires the following evidence for each final profile:

1. Retain run ID/attempt, event, exact final candidate SHA and workflow/harness
   identity. Require an actual relevant comparison and successful aggregate;
   no-work, skipped, cancelled or missing execution cannot satisfy this gate.
2. Retain event-selected baseline and ancestry evidence: the push merge-base and
   captured default, or the weekly fixed reference
   `b85ec364057f536940d689b09e612512ffffaf82`. Bind exported archives, trees and
   loaded source hashes to those SHAs; retain matching resolved locks,
   dependencies, Ruby ABI and runtime policies for both sources.
3. Retain complete raw samples and worker evidence for all 12 quick or 32 weekly
   cases, pilot-selected identical operation counts across sources, two warmups,
   3 AA/9 AB or 5 AA/15 AB pairs, and required alternating orders. No case or
   observation may disappear during aggregation.
4. Verify every response's typed, duplicate-key, raw and canonical identity
   checks and every operation's counters. Require exact queries/authorizations,
   allocation ceilings and scaling bounds against the unchanged calibrated
   budgets; preserve the corresponding deterministic contract evidence.
5. Require runner exit 0 and a passing report. Independently recompute report
   classifications from retained raw observations, including wall and CPU noise
   margins/agreement and allocation results. Missing, erroneous, regressed or
   inconclusive evidence remains blocking.
6. Verify the whole performance job completes within 600 seconds for quick or
   1,800 seconds for weekly, including setup, export, execution, validation and
   artifact upload. Require successful 30-day artifact retention and retained
   checksums. The separate aggregate job has its own one-minute limit; workflow
   queue time is not performance-job runtime. A short benchmark step alone does
   not establish job feasibility.

At this decision, final artifacts and acceptance remain pending; this note
declares no readiness. Existing exact-final-head ordinary tests/CI, accepted
review and narrow-fix lineage, and deterministic CLI positive controls remain
separate obligations. Earlier-head successes support diagnosis but do not replace
the final profile evidence. No additional duplicate local campaign, hosted
manual quick run or defect injection is required solely to change location.

A successful hosted run establishes observed noise and feasibility for that
runner and time, not a universal runtime guarantee. Manual weekly execution
verifies dispatch and the full weekly profile, not an actual Sunday schedule
event or fork PR; retain resolver/permission tests and disclose those live-event
limits. Synthetic Rack/SQLite results make no production, network-server or
vpsAdmin latency claim. Diagnose any timeout or inconclusive outcome without
relaxing the cap, changing policy or retrying until green.

### Proposed bounded SQLite timing diagnostic, 2026-10-25

The lead authorized diagnostic design only. C owns preparation of a session-only
probe after this brief is accepted; no probe implementation or measurements have
run under this assignment. D currently owns the utility for existing weekly CI.
Keep that operation undisturbed and obtain a separate launch authorization and
fresh watcher for any diagnostic. Do not edit application, fixture, runner,
workflow or budget files, or reinterpret the failed quick result as a pass.

The retained final quick result is genuinely inconclusive: `sqlite.includes`
with `{rows:32, include_depth:2}` has 7/9 passing wall and CPU pairs, below the
required 8/9. Its wall AA margin is 0.853391 ms/request; comparison pairs 5 and 8
remain unresolved. All allocations are 11265.0625/request and counters are
3 queries, 65 authorizations and 1 execution/request. Wall and CPU differ by
at most 4.602 microseconds/request. Those facts identify no unique cause.

Preserve the failed run directory
`api-performance-hosted/38ecca75edaf797d048fb36c6a50ea7e05eb50a9/final-ci-watch/40187916872/artifact/`
unchanged. Freeze the diagnostic script, manifest and prepared roots before a
launch. Use baseline `39909094649b1d14a23f00615775ca7136acf4fd` and candidate
`38ecca75edaf797d048fb36c6a50ea7e05eb50a9`, from the retained source archives:

| Input | SHA-256 |
| --- | --- |
| Baseline archive | `c61f0e459fc14db61194ed6134a0e3da89f5d53c3b59c0aad11a5685785107d2` |
| Candidate archive | `3a5fea45cd8bd8245a270c6d5c2720759e230cfa69aa3de7d0bda1648c549740` |
| Original runner source | `d64b722f7c361fc88f9938b7e1f54c28709c2b0701e1824cd62df8fabe7ea2fe` |
| SQLite fixture | `faa5073996e7c666604080873c303d5ee6f8bd97ceaf7e33418342ceb83b6f0a` |
| Root lock | `0a48c3e68d0b78caf945cb5a0430d13841ee140eb1bdca5734d823617a42afe6` |
| Server lock | `fdc5129f60f9ed2f6a56fbf7f9483af5d6a003fedb13a93e895e9cab87193b52` |

Bind the remaining fixture/input hashes, actual gems, Ruby executable/ABI and
test/locale/timezone/JIT policy to the retained worker evidence. Require the same
graph locally; refuse mismatches rather than install or change dependencies.
Retain the new host identity and disclose its difference from the failed hosted
VM. C records script/manifest hashes and verifies source/input hashes afterward.

Run six fresh workers, sequentially in the predeclared order
`B0, B1, B2, C0, C1, B3`: one baseline same-source control `(B0,B1)`, one
baseline-first comparison `(B2,C0)`, and one candidate-first comparison `(C1,B3)`.
Each worker builds only the exact SQLite case, runs two warmup batches and one
observed batch, each with exactly 16 operations. This is 288 diagnostic requests
in total. Reuse the original worker loading, source verification, measurement
loop and every-response/counter validation. Do not perform a new pilot, aggregate
these diagnostic pairs into a gate result, add repetitions or retry on a chosen
outcome. Isolating one scenario intentionally omits preceding quick workloads;
absence of the effect here cannot rule out process-history effects in the full
campaign.

C may prepare a narrowly instrumented session-only copy of `Worker#measure`,
guarded by the exact original source hash and exact replacement text. Preserve
the original reset, explicit `GC.start`, allocation/CPU/wall snapshots, call loop
and validation body. Preallocate telemetry records before reset/GC. Capture the
pre-batch telemetry after explicit GC and before the original snapshots; capture
post-batch telemetry after the original final snapshots and before validation.
Take GC snapshots last in the pre-hook and first in the post-hook so proc/file
inspection is not attributed to request GC work.
Collect the same fields for warmup and observed batches, with no per-operation
callbacks or polling process. Record snapshot overhead: outside-timer collection
can still perturb the heap, so these timings are diagnostic only.

- GC: counts, minor/major counts, total allocated/freed objects, heap pages and
  live/free slots; record `GC.measure_total_time` and total GC time only when
  already enabled. Do not enable profiling, disable GC or tune its parameters.
- Process: monotonic/process CPU clocks, PID/start identity, minor/major faults,
  user/system ticks and CPU placement from `/proc/self/stat`; scheduler runtime
  and runqueue wait from `/proc/self/schedstat` when available. Tick counters are
  coarse at these batch durations; retain the original high-resolution clocks.
- Environment: resolve the actual cgroup/mount from `/proc/self/cgroup` and
  mount information; record readable CPU quota/cpuset and throttling counters.
  Treat shared-cgroup counters as shared observations. Optional readable CPU
  frequency snapshots are hints, not effective-frequency proof. Record absent
  or denied fields with reasons, never fabricated zeros or privileged fallbacks.

Interpret the result against predeclared hypotheses:

| Hypothesis | Discriminating evidence and limit |
| --- | --- |
| GC work explains a slow batch | Additional collections/GC time tracking its CPU excess supports this mechanism. A slow batch with zero collections excludes a collection pause in that batch, not every heap/cache effect. Disabled GC timing leaves time attribution unknown. |
| Scheduling, throttling or faults explain a slow batch | Increased wait/throttling/fault counters and wall-minus-CPU support that mechanism; shared counters alone do not attribute it to this worker. Original wall/CPU agreement already disfavors pure waiting. |
| CPU throughput varies without more request work | Similar GC/counters/allocations with CPU and wall moving together is compatible with throughput variation. Frequency snapshots cannot establish its cause; do not label it a proven host fault. |
| Inputs or source selection differ | Provenance/runtime/counter mismatch invalidates the diagnostic and supplies a concrete setup issue to investigate; identical metadata does not prove identical machine state. |

Proposed exact launch interface, after C prepares and freezes the two named
session files and the lead authorizes execution, from the HaveAPI worktree:

```sh
timeout --signal=TERM --kill-after=5s 120s env HAVEAPI_RELEASE_TOOLS_ONLY=1 \
  nix develop --command bash -euo pipefail -c '
    env -u RUBYOPT -u RUBYLIB -u BUNDLE_BIN_PATH -u BUNDLE_GEMFILE \
      -u BUNDLE_LOCKFILE -u BUNDLE_PATH -u BUNDLE_FROZEN -u BUNDLER_SETUP \
      GEM_PATH="$PWD/.gems:$PWD/clients/rust/.gems:$(ruby -e "puts Gem.default_dir")" \
      ruby --disable-yjit /home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-context-copy-performance-tests/sqlite-timing-diagnostic.rb \
      --manifest /home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-context-copy-performance-tests/sqlite-timing-diagnostic-manifest.json \
      --output /home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-context-copy-performance-tests/sqlite-timing-diagnostic-once
  '
```

The output directory must be new. No detached children, separate process groups,
installs, network preparation or retries are permitted. The watcher retains the
exit/status, elapsed time and logs and reconciles termination of all children.
The diagnostic has a 120-second deadline plus at most five seconds for forced
termination; expected duration is tens of seconds, not yet measured. Timeout or
missing telemetry is incomplete evidence, not a performance result.

This local probe can identify a mechanism worth investigating, not retrospectively
prove the cause on the original hosted VM. It cannot replace the failed required
quick campaign or change references, budgets, pair counts, thresholds or caps.
If it establishes a concrete defect, C proposes the smallest remedy to the lead
before implementation or any new required run. If evidence remains ambiguous,
report that limit and keep the original blocking result; no optimization or
unchanged campaign rerun follows automatically.

### Approved diagnostic v2 preparation deviation, 2026-10-25

The lead approved **preparation only**, assigned to C as
`2816a43f-e8aa-4da2-9c50-09608810f558`. Preserve the original diagnostic,
zero-request preflight, manifests, launchers and results. The
[preflight graph receipt](sqlite-graph-preflight-once/graph-preflight.json), SHA-256
`c555532d5b8e958243203dd43a50b71eab8a41a0250111937a6e136be867c2f1`,
establishes one difference: `io-console` 0.9.4, platform `ruby`, was available but
absent from the activated 83-gem map; all other entries and Ruby/executable/ABI
matched the expected 84-gem map. It captured no requests or timing evidence.

For a new session-only v2, explicitly activate that exact available `io-console`
version/platform before scenario construction for both source roots. Record the
activation as altered startup history. This is the sole approved deviation from
the earlier no-preload contract. Retain the **same complete 84-gem equality**,
Ruby, source/input, original measurement-body and every-response/counter guards.
Do not omit the gem from expectations or tolerate any additional difference.

Replace the earlier Nix launcher with a direct invocation of the already-present
exact Ruby executable and frozen prepared gem paths/inputs. The offline Nix
invocation attempted unexpected derivation work and reported bootstrap errors;
the logged Linux source-tar derivation did not establish kernel compilation.
The v2 preparation must perform no Nix evaluation, realization, build, network
access or dependency installation. Bind the existing executable and inputs
statically; stop and report if that cannot be done. Do not load workers or issue
requests during preparation.

Freeze v2 files and retain their hashes for a separate lead inspection and
execution decision. The six-worker order, 16 operations, two warmups, strict
validation, outside-snapshot telemetry and 120-second deadline plus five-second
termination grace remain unchanged. Preparation approval authorizes no new
diagnostic execution, required campaign, automatic retry or policy change.
This repairs the local diagnostic setup only; it neither identifies the original
hosted timing cause nor clears the blocking quick inconclusive result. The
accepted weekly result remains unchanged.
