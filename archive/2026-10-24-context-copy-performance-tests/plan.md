# 2026-10-24-context-copy-performance-tests

## Goal

i'd like to fix haveapi issue described here:

```
HaveAPI repeatedly copies the **entire API description while rendering individual example tabs**.

The initial context owns a frozen copy of the description. But deriving a context for one language or action calls:

```ruby
def with(**changes)
  self.class.new(**all_existing_fields, **changes)
end
```

That constructor recursively copies everything again—including the complete resource/action/parameter tree—even when only the language profile or sample changed.

The renderer does this while checking each language’s availability, then again while rendering its panel, repeatedly across the page. Rust also repeatedly traverses and normalizes the description.

For one administrator request we measured:

| Work | Time |
|---|---:|
| Entire request | 102.4 seconds |
| 639 context derivations | 88.8 seconds |
| Process CPU | 102.3 seconds |

So most time goes into copying objects and associated allocation/garbage collection. It is not waiting for the network or compiling Go/Rust clients.

**These measurements came from our local API test environment, not production.** An earlier uninstrumented run was also extremely slow, supporting the diagnosis, but we haven’t established a production latency or a before/after baseline.

The proposed fix is to share unchanged immutable data between derived contexts and copy only supplied changes, while preserving request-local authorization.
```

additionally, we must introduce performance testing, so that this issue will not be possible in the future. suggest solutions.

## Affected repositories

- `haveapi`: Ruby server documentation example contexts, generators, tests,
  benchmark tooling and developer guidance; expanded framework endpoint,
  ActiveRecord/SQLite and workflow performance coverage. No downstream pins.

## Accepted expansion, 2026-10-25

User requested performance coverage beyond documentation and selected HaveAPI
plus its ActiveRecord adapter, blocking meaningful timing regressions, a 5–10
minute push/PR budget, an expanded weekly run, and blocking inconclusive slowdown
results. The proposed plan was explicitly accepted with "Implement the plan".

- Cover actual Rack routing/execution, Basic/token authentication, authorization,
  typed validation, malformed input, list/object serialization, CRUD/nested routes,
  request isolation, SQLite pagination/eager loading and documentation OPTIONS/HTML.
- Share one neutral harness/fixture and compatible dependency graph across exact
  baseline/candidate roots; verify loaded source paths and every response contract.
- Pilot targets 150 ms/batch, 1–2,000 requests, two warmups, three baseline self
  pairs and nine alternating comparison pairs. Meaningful wall/CPU slowdown is
  greater than both 20% and 0.20 ms/request. Noise margin is max(self variation,
  5% baseline, 0.05 ms); eight-pair agreement passes/fails, otherwise inconclusive
  fails. No automatic retry or relaxation. Keep GC enabled.
- Allocation growth above max(10% baseline, 32 objects/request) fails, with
  additional measured fixed-reference ceilings (25% plus 32 objects headroom).
  Exact query ceilings and size-work bounds preserve required authorizations.
- CI sizes: 1/32/128 result rows; fixed page 32 against 32/128/1,024 DB rows.
  Weekly: five self pairs, 15 comparisons with 14-pair agreement, larger payloads
  and lists to 1,024, DB tables to 10,000, docs shapes 16 and Rust measurements.
- Push, PR and manual workflow plus Sunday 03:00 UTC schedule; hard job limits
  10/30 minutes; stable aggregate check, read-only permissions, fork-safe execution,
  30-day always-retained failure/success artifacts. Weekly fixed accepted source
  is `b85ec364057f536940d689b09e612512ffffaf82`; require ancestry and never roll
  reference/budgets forward automatically. PR uses merge-base with event base,
  feature push uses merge-base with captured default, default push uses event
  before/after, manual accepts exact SHAs. Missing/incompatible comparisons fail.
- Detector tests inject allocation/query regressions, slow/noisy traces, missing
  inputs and wrong responses, exercising actual CLI exits. Calibrate real counts
  and baseline self-noise; commit and quick-check all intended changes, then run
  independent final branch review before long campaigns and GitHub verification.

Architect owns the expanded design and shared contracts. Execution owners are
implementer0 (API fixture/specs), implementer1 (SQLite/query gates), implementer2
(runner/comparator/budgets) and implementer3 (workflow/event resolver/commands/docs).
Keep Git/index and dependency preparation serialized; disjoint edits may overlap.
This expansion supersedes the earlier opt-in-only timing scope below. No
integration, deployment, release or session lifecycle action is authorized.

Calibration exposed a weekly runtime concern: the initial selected-count model
projects about35.7minutes, above the30minute cap, with substantial unclassified
setup/validation cost. Before final review C adds untimed stage telemetry and
removes redundant JSON/tree passes while preserving every-response validation,
typed canonical comparison, duplicate-key rejection, raw fingerprints and exact
counters. A bounded selected-count reference run measures the resulting costs.
No workload/pair reduction, timeout relaxation, shared DB/profile, or automatic
budget increase is authorized. Full paired runtime/noise acceptance and hosted
verification remain required after review; the projection alone establishes no result.

Lead accepted the architect's verification-location clarification: one complete
exact-final-head hosted quick execution and one hosted weekly execution may
jointly satisfy paired campaign, self-noise, runtime feasibility and hosted
integration acceptance. This explicitly supersedes the earlier requirement to
repeat both local and hosted profiles. Workloads, pairs, order, budgets, response
and counter proofs, and10/30minute limits are unchanged. Inspect complete raw
artifacts and whole-job duration including setup/upload. An equivalent local
repetition is not an additional gate; aitherdev full paired performance remains
unmeasured. Earlier samples/decisions remain retained, and final hosted artifacts
are still required before readiness.

## Approach

Have the retained architect inspect context derivation and Rust normalization,
then record a design and independent implementation boundaries in `design.md`.
Implement immutable sharing without broadening request-local authorization.
Introduce regression checks that reject repeated whole-description work and a
representative benchmark reporting allocations, CPU and elapsed time.

## Decisions

- The reported 102.4-second request and 639 derivations are local observations,
  not a production baseline. Establish reproducible before/after evidence.
- Prefer deterministic complexity/allocation checks for CI; timing benchmarks
  complement those checks and require a documented measurement environment.
- Publish a feature branch. Integration, release and deployment require separate
  direction and are outside the present implementation scope.
- Adopt deterministic ownership, allocation-growth and recursive-traversal gates
  in existing CI now. Provide opt-in timing/CPU/allocation reports with broad and
  concentrated shapes. Recommend scheduled fixed-runner campaigns and request/GC
  observability as later operational layers; add latency budgets only after
  measuring runner variance. No finite suite guarantees every future regression.

## Compatibility and deployment

Preserve rendered output, input isolation and request authorization. Assess
cache lifetime and invalidation explicitly. No persistent schema or protocol
change is expected. No deployment or version publication is planned.

## Documentation

Developer readers need the immutable-context contract and repeatable performance
test commands in HaveAPI documentation. Keep measurements and rollout-specific
evidence in this session; lead owns records and architect owns design.

## Testing plan

Run targeted quick Ruby checks and hook-managed lint before commits; run final
independent review after intended commits and quick checks, before longer tests.
Check unchanged subtree identity, defensively copied supplied changes, nested
immutability, output parity and cross-request authorization isolation. Require
the new regression protection to expose the original copying behavior. Use a
fresh policy watcher for long or uncertain verification.

## One additional quick run authorized, 2026-10-25

After the original quick result remained inconclusive and bounded local
diagnostics established no concrete remedy, the user said "proceed" to exactly
one additional quick run on a fresh GitHub Actions runner. Use the same exact
candidate38ecca75/baseline39909094 pair, workloads and thresholds. Preserve the
original run separately. D dispatches once, collects complete evidence and
monitors through a fresh watcher; C independently audits; architect and lead
assess both outcomes without pooling or inferred host causality. A pass prompts
an explicit assessment of remaining uncertainty, another inconclusive result
requires repeatability work before proceeding, and a regression needs diagnosis.
This authorizes neither automatic retries nor acceptance-policy changes, source
changes, integration or deployment. Earlier no-additional-run wording is
superseded only for this one bounded repeat.

The authorized repeat40196045698 independently passes all12cases under the
unchanged gates. After assessing both outcomes and the architect's independent
recommendation, the lead accepts it as quick verification with the original
inconclusive retained as an explicit residual. No pooling, reclassification,
root-cause claim, standing retry or policy waiver. Exact-head weekly also passes;
no further campaign is required for this scope. See api-performance-acceptance.md.
Ready awaiting explicit HaveAPI master integration approval; no integration
authorized by this verification acceptance.

## Approved integration,2026-10-25

User "ok, merge it" explicitly approved HaveAPI origin/master integration.
Lead executed the exact reviewed fast-forward39909094→38ecca75 through ordinary
hooks and a non-force SSHpush, verified remote equality and clean checkouts,
then released the single repository claim before CI. D observes only newmaster
push exact38runs; C validates resulting performance evidence. No source/rebase/
policy change or manualcampaign, deployment/release/lifecycle action. Branches
and session remain open. See api-performance-master-integration/receipt.json.
