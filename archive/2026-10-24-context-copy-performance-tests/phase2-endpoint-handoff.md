# Phase 2 endpoint fixture package

Owner: implementer0. Final package commit:
`4e05ca8dc4f6b938814b354996025b0aad91d9c7`. Git window relinquished; no source
changes are pending in the three owned paths. Final whole-branch review and
campaigns remain the lead's later gates.

Owned files in HaveAPI:

- `servers/ruby/test_support/performance_endpoint_fixture.rb`
- `servers/ruby/spec/performance/endpoint_contract_spec.rb`
- `servers/ruby/spec/performance/endpoint_scaling_spec.rb`

The source-neutral fixture requires `haveapi` through the worker-selected load
path. It exposes the agreed `cases`/`build` and reset/call/validate/counters/close
interface, using real Rack routing, Basic/token providers, authorization, typed
validation, nested paths and list serialization. The read-only `app` accessor is
the architect-approved addition for untimed CRUD/error tests; requests through it
outside an active call never advance or mutate timed counter records.

Quick inventory is the seven agreed IDs, with `api.list` dimensions `{rows:32}`.
Weekly preserves those and adds list `{rows:1024,user:member}`, list
`{rows:1024,user:admin}`, and basic GET `{user:admin}`. Default protected user is
member. Canonical identities use package C's shared `Identity.json` helper; that
helper must be included in the intended final branch before final checks/review.

Every successful timed operation has exactly zero queries, one authorization
and one execution. `api.invalid_post` has zero queries, one authorization and
zero executions, returning HTTP 200 with `status:false`. Counters are allocated
before the timed loop and every response/record is checked afterward. Reset
restores per-scenario store/counter state; no server, database, subscription or
external process is opened by the fixture.

Focused checks passed in the prepared top-level Nix shell with
`HAVEAPI_RELEASE_TOOLS_ONLY=1`:

```sh
make doc
cd servers/ruby
bundle exec rspec spec/performance/endpoint_contract_spec.rb spec/performance/endpoint_scaling_spec.rb
```

Result: 15 examples, 0 failures, seed 47118, 1.78 seconds examples. RuboCop on
all three owned files and the owned whitespace check passed. Normal commit hooks
passed without warnings after a message-only width amendment. No bypass, fetch,
push, rebase, long suite or campaign ran in this package.

The contract covers malformed JSON/shape, HTTP 401/403/404, typed error envelopes,
CRUD/reset and independent stores, alternating admin/member output, scalar and
nested values, omitted fields, changed output types, invalid/missing/overflow
operation records, weekly shapes and list sizes 1/32/128. Actual duplicate JSON
testing found that the installed JSON parser bypassed custom `object_class`
assignment checks. C repaired its helper using the parser's documented
`allow_duplicate_key:false` option; the actual parser regression now passes.

## Focused allocation evidence

[Raw measurements](phase2-endpoint-calibration.json) and
[reproduction script](phase2-endpoint-calibration.rb) retain two warmup batches,
three ten-request measurements, every-response validation and exact per-operation
counts. Allocation measurement covers the request loop only, with response slots,
reset, GC.start and validation outside it. Runtime is Ruby 3.4.11 against the
unchanged accepted-reference production source at `b85ec364`. This is focused
calibration; C owns the final isolated-worker calibration and all budget writes.

| Case/dimensions | Objects/request (minimum) |
| --- | ---: |
| public GET | 664 |
| Basic GET, member | 666 |
| token GET | 676 |
| typed POST | 677 |
| invalid POST | 705 |
| nested GET | 694.2 |
| list rows 1 / 32 / 128 | 640 / 795 / 1275 |
| list rows 1024, member | 5755 |
| list rows 1024, admin | 3705 |
| Basic GET, admin | 662 |

List body sizes for 1/32/128 rows were 185/3548/14070 bytes. Member list
allocation includes output blacklist filtering for each row; admin skips that
restriction and therefore has fewer allocations despite a larger serialized body.
The deterministic scaling spec allows the allocation increment for 96 additional
rows to be four times the increment for 31 additional rows, plus 32 fixed objects
of VM bookkeeping slack. The observed increment ratio is 480/155, about 3.10;
the bound rejects quadratic growth without requiring constant work for growing
responses. It is separate from C's allocation ceilings and has no timing gate.

No production API/state/schema or migration changed. No deployment, integration,
publication or session lifecycle action is authorized or claimed.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-context-copy-performance-tests/>.
