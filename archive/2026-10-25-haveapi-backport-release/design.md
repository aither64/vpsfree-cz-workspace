# HaveAPI 0.30.2 backport design

Design owner: architect0. Implementation owners: implementer0 and implementer1,
assigned by the lead. The master-first amendment below is the current execution
brief and supersedes earlier release-only ordering and auto-abbreviated diff
serialization. Historical package evidence remains valid only for its exact head.

## Accepted maintenance verification against the mapped accepted reference

Lead accepted this no-code verification substitution and assigned implementer0
**one existing manual quick comparison**, with final candidate
`321ce8256ad4704efaed04f4f2aa1ea4c2a3b4b8` and baseline
`8b7abc097db49893da9cc8fa4395648901fec71d`.
No source change is recommended. The baseline is the already verified literal
maintenance ancestor corresponding to fixed reference `b85ec364`; its complete
tree difference is the accepted release metadata delta. Both the resolver and
direct runner already support this explicit ancestor pair. Do not use master
`39e9802` as a quick baseline: it is source-equivalent but not a literal ancestor
of the maintenance candidate, and no new ancestry exception is needed.

The original automatic quick run **40237146941 attempt 1 remains failed**.
Its historical 0.30.1 baseline `1c3c98f0` exceeded the 30-second request guard
during one initial full Rust-page request, after setup and before any candidate
worker. This establishes an unavailable baseline measurement, not a candidate
regression, a completed comparison or a measured speedup. The manual result must
be recorded separately; it does not clear/relabel that failed default-push gate
or demonstrate 0.30.1-to-0.30.2 timing or a speedup. Lead explicitly accepted this
named alternative and its tradeoff for release verification. Check applicable
required-check rules read-only before relying on it; no required-check bypass is
authorized.

This is sufficient bounded verification when combined with accepted master39
quick/weekly results and the reviewed exact master39-to-final source/input/
environment equivalence. The tradeoff is explicit: verify the final release
against the usable accepted reference, leaving the old 0.30.1 timing comparison
unavailable. Keep all 14 quick workloads, live correctness/auth/counter checks,
candidate **30-second** guard, unchanged batching/adequacy/budgets and 15-minute
limit. Retain the accepted 34-case master weekly evidence; no new weekly or
historical-baseline campaign. The shortest checks are existing exact-pair
selection/ancestry/input validation and that one complete manual quick run,
alongside the already-running component/build checks. A failure returns to its
concrete diagnosis; no automatic fallback, timeout increase or retry loop.

## Current override: compact useful performance evidence

User direction to simplify supersedes the per-operation artifact/replay contract
and synthetic capacity exercise below. Stop that exercise; no further resource
models, 1.75 GB replay or capacity-campaign acceptance gates. Preserve existing
original artifacts unchanged as historical evidence.

Implementer1 owns one bounded change in the existing `endpoints.rb`,
`performance_compare.rb`, affected performance specs/support and
`doc/performance.md`; adjust `utils/performance_ci.rb` only for the changed report
contract. Every live request still passes status/header/index, body/authorization
and operation-counter validation outside the measured interval. Keep existing
fixture checks and sample-local body reuse. Temporary live arrays may remain
where needed; they must not become retained per-operation output/counter arrays.

Each measured workload emits timing/allocation/operation metrics, the validated
counter summary and distinct response examples with occurrence counts. Use the
existing raw body, status/envelope, canonical identity and narrow release-version
handling for each example; identical responses need one retained copy per sample.
The existing uniform counter contract can retain one counter record and its
validated operation count. Replay checks positive integer cardinalities, sums
matching operations, expected counters, each retained response's consistency,
source/environment/input identity and paired metrics/output equality. It does
**not** reconstruct individual request order or independently reprove every live
authorization/counter check. Document that deliberate loss of per-operation
replay detail; a compact summary is not a full execution transcript.

Use the owning samples-format version bump if needed and reject unsupported
versions clearly. No automatic old-format conversion or permanent compatibility
lane is required for this benchmark tool. Old evidence stays attributable to its
recorded implementation. Emit a small report containing source/profile identity,
overall outcome and per-workload metric/correctness results; do not merge the raw
samples or response bodies into it. Keep full source/input preparation checks;
add no provenance, streaming, compression or dependency framework.

Preserve all 14/34 workloads, common baseline-selected counts and 100,000 cap,
adequacy, pairing/agreement, 20%/10% plus 50-ms policy, allocation budgets,
30-second safety and 15/45-minute job limits. No product/state/migration changes.
Focused tests must show that a bad late/repeated live response or operation still
fails, summaries preserve counts/metrics and reject inconsistent examples or
counters, repeated operations do not multiply retained output records, and the
report excludes raw samples. Retain relevant source/version/auth negatives.
Run normal quick checks/hooks, commit, obtain affected independent final review,
then actual final-head quick and one weekly CI campaign. No additional large
replay/resource gate. Integrate master first, then `-x` backport and separate
0.30.2 metadata under the existing lead-owned release procedure.

## Current acceptance: enough representative work to detect regressions

Latest user correction supersedes the coarse policy below: **remove the 10×/1s
acceptance rule before proceeding**. The aim is meaningful regressions across
request types, measured with adequate volume or realistic complexity. Master
first, then exact `-x` backports and separate .2 metadata remain mandatory.

Implementer1 owns this bounded adjustment in the existing runner/comparator and
their tests/docs. Inspection confirms the current pilot chooses only 150 ms of
work, capped at 2,000 requests, while collecting two full-count warmup batches.
Quick has twelve existing API/SQLite/documentation workloads; each process runs
them all. Increasing volume without bounding warmups/pairs would multiply runtime.

- Target **1 second of baseline request execution per workload/batch**, using
  the existing pilot. Baseline alone selects a common count for both revisions;
  preserve per-request normalization and exact per-operation validation. Raise
  the bounded count ceiling to **20,000**. Use one bounded calibration adjustment
  if the first real baseline batch is below **750 ms**; retain observed duration,
  chosen count and any cap limitation. Do not call an undersized capped batch
  adequate evidence or restart the workflow until it looks green. Keep response
  retention bounded; implementer diagnoses any concrete memory issue before
  increasing the cap further.
- Keep two warmup batches, but select warmup counts for about **100 ms each**
  rather than repeating a full one-second measurement count. Use **three self
  pairs and five baseline/candidate pairs**, alternating order, for quick checks;
  four of five consistent comparisons establish a direction. Expanded diagnostic
  runs may use seven pairs/six agreement. This gives about four minutes of request
  work for twelve quick cases (16 workers × 12 × 1.2 seconds). This initial
  estimate used a ten-minute job; measured full execution later required the
  accepted fifteen-minute quick allowance below. Retain actual elapsed
  stages; avoid runner tuning or new scheduling machinery.
- Keep a **20% relative regression budget**. Replace the old per-request
  0.20-ms floor, which can hide large relative regressions in cheap calls, with
  a **50-ms batch-level minimum detectable increase**, converted by the common
  operation count when comparing per-request values. At a one-second baseline,
  the 20% effect is 200 ms, comfortably larger than that floor. Report wall and
  CPU separately, retaining paired/self noise evidence. A consistent increase
  beyond the budget and measured self noise blocks; do not accept it merely
  because it is less than tenfold. Ordinary variation remains informational.
  Residual noisy/inconclusive timing must be labeled as such, never called a
  demonstrated performance pass; it does not trigger endless workflow retries.
  Deterministic checks stay independently authoritative.
- Exercise a complete Rust-enabled documentation page at realistic complexity
  through the existing fixture: initial **64 resources × 4 actions × 2 samples
  × 4 parameters**, admin/member variants. Include its rendering in the same
  paired measurement mechanism: an expensive request naturally selects count 1
  once it exceeds the target. Validate actual full-page output, Rust panels and
  authorization boundaries, not only one adapter snippet. Use existing fixture
  controls and counters, plus relative allocation/scaling invariants; do not
  fabricate calibrated reference allocation ceilings for a new workload. Retain
  existing calibrated budgets unchanged and keep the new workload's explicit
  deterministic/relative checks distinct. Any shape adjustment must cite actual
  output size, duration and memory rather than being selected to hide a failure.

The 30-second individual-request deadline remains supplementary runaway safety
for **all** workloads, including pilot/warmup; it is not the regression budget.
Keep the implemented worker supervision only if it preserves request timing and
allocation boundaries, reports source/workload, and terminates/reaps stuck work.
Setup has its separate operational timeout. Product runtime is unchanged.

Smallest file boundary: existing `endpoints.rb` pilot/measurement/inventory,
`performance_compare.rb` classifier, their focused specs/support fixtures and
`doc/performance.md`; change `utils/performance_ci.rb`, workflow and development
instructions only where the new report/exit/warmup contract requires it. No new
benchmark, calibration, equivalence framework or public configuration surface.
Portable full-index lineage and component-test fixes stay in the master package.

Quick acceptance must prove count selection/duration bounds, equal revision
counts, warmup exclusion and normalized counters; replay cases with consistent
**25–50%** increases must fail, including a cheap-request case formerly hidden by
the 0.20-ms floor. Add one controlled execution-level slowdown using extra work
or a test-only delay over repeated operations to prove the live batching path
detects an increase well below 10×. Do not sleep for 100 seconds. Noise-only and
insufficient-signal cases must retain honest diagnostic classification; existing
wrong-response/auth/count/allocation/source/input negatives still fail. Demonstrate
full Rust page coverage and bounded runaway supervision. After normal hooks,
committed-source review and quick checks, run one representative exact-head
hosted campaign for master and reconstructed release with real batch-duration,
sample-count and complex-page receipts. No automatic timing reruns or mandatory
weekly precision campaign; any real measured regression returns to diagnosis.

### Weekly supplement and accepted Rust environment reuse

User direction: “the weekly performance test can be even broader and stricter”.
This supplement adds explicit weekly acceptance without blocking quick-profile
implementation. Reuse the existing profile/runner/comparator structure.

| Setting | Quick | Weekly |
| --- | --- | --- |
| Baseline measured work per workload/batch | 1 second | 2 seconds |
| Minimum adequate observed batch before bounded adjustment | 750 ms | 1.5 seconds |
| Self pairs | 3 | 3 |
| Baseline/candidate pairs and required agreement | 5 / 4 | 7 / 6 |
| Relative wall/CPU regression budget | 20% | 10% |
| Aggregate minimum detectable increase | 50 ms | 50 ms |

Weekly retains all existing expanded API, authorization/member-admin, large
payload/list, SQLite row-count/include-depth, documentation shape and Rust
async/blocking action/auth cases. Add the quick full Rust-enabled HTML cases
plus an expanded page shape of **128 resources × 4 actions × 2 samples × 4
parameters**, with admin/member output checks. This doubles resource breadth
without adding a new fixture family. Long individual requests naturally use
count 1; the universal 30-second request deadline remains supplementary safety.
Retain the same bounded pilot adjustment/count/memory controls and short warmups;
do not hide insufficient work under a larger count cap or noisy green result.

The weekly 10% budget is justified by twice the per-batch request work and more
paired observations: at a two-second baseline a 10% regression is a 200-ms effect,
still four times the 50-ms aggregate floor. Keep self-noise visible and require
the agreed direction in six of seven pairs. These are practical engineering
thresholds, not a claimed statistical confidence level. Weekly uses the accepted
45-minute job limit documented below; retain elapsed stages and case inventory.
If the larger inventory exceeds that limit, diagnose actual work/preparation
cost rather than silently dropping cases, weakening thresholds or retrying.

Lead accepted a concrete dependency identity choice: the new quick full-page
Rust workload needs fiddle/racc/tomlrb, absent from the former quick calibration
environment. **Use the already recorded weekly Rust environment as the expected
runtime identity for both quick-with-Rust and weekly.** Prepare the Rust bundle
for quick as well; include Rust Gemfile/gemspec and resolved lock in input
comparison/retention. Require exact baseline/candidate/source/runtime equality
and the existing recorded Rust dependency closure. Preserve all existing
allocation ceilings and their bytes; do not rewrite historical quick calibration
as if it contained these dependencies, invent new measurements, or add another
orchestration lane/calibration framework. Reports must identify which existing
environment was selected and retain actual loaded versions/manifests/locks.
If its exact closure is unavailable or identities differ, fail the identity check
and diagnose rather than silently selecting a new environment.

Focused acceptance: profile tests prove weekly selects its broader inventory,
two-second work target, seven/six pair policy and 10% threshold; a consistent
15% injected slowdown can pass quick's 20% budget while failing weekly with
adequate signal. Both profiles must reject meaningful larger regressions and
all existing deterministic/output/auth/provenance violations. Prove quick Rust
input capture includes the required closure and rejects missing/changed Rust
dependencies. After committed-source review, execute one exact-head expanded
weekly campaign, retaining actual batch durations, full inventory, runtime and
large-page results. Weekly failures caused by real regressions or invalid inputs
block acceptance; unresolved timing noise remains explicitly inconclusive and
does not authorize endless reruns. Master-first implementation/integration then
`-x` release backport applies to this supplement too.

### Measured complex-page sizing amendment

This amendment supersedes the unmeasured repeated 64-resource quick and
128-resource weekly shapes above. Implementer1 measured the full
64 × 4 × 2 × 4 Rust-enabled page: admin **23.610839 seconds / 13,272,210 bytes**;
member **15.199303 seconds / 9,629,611 bytes**; authorization count 257,
output/security checks passing. The probe, including two warmups and one
measurement per variant, took 108 seconds with RSS 156,720 KiB. Repeating that
shape with all quick samples and full-page warmups would take roughly 31 minutes
and exceed the ten-minute job. These are legitimate baseline costs, not evidence
of a new regression. Retain the exact probe receipt and source/input identities.

Use **16 resources for repeated quick** and **32 for repeated weekly**, keeping
four actions, two samples and four parameters per resource and both admin/member
variants. This still exercises complete Rust-enabled pages with 64/128 actions
and 128/256 declared samples, respectively, rather than single snippets. Weekly
remains broader than quick. These sizes are provisional until implementer1
measures their actual request durations, output sizes, peak memory and
authorization/output contracts in the existing probe. Do not run 128 blindly or
claim linear scaling from 64. Use a fresh watcher for the bounded probe; no extra
performance framework or orchestration lane.

An expensive case whose baseline pilot already meets its profile's one/two-second
target uses **one measured request and no extra full-request warmups** per fresh
worker. Both revisions receive the same policy. This intentionally measures the
first complete request after the same fixture setup; retain the warmup count in
evidence and test that setup remains excluded. Pilot classification fixes this
policy for the pair; do not let a slower candidate select a different warmup
path. Cheap cases retain adaptive batching and two approximately 100-ms warmups.
Keep common counts, pairing/alternating order and the **20% quick / 10% weekly**
budgets, 50-ms aggregate floor and adequacy checks unchanged. One already-long
request supplies the intended timing signal; three duplicate renders do not.

Before accepting the proposed sizes, project the campaign cost from measured
16/32 admin/member durations, actual pair/worker counts and short-workload setup
cost. Require room within the current fifteen/forty-five-minute job budgets, including
preparation and evidence validation; record the arithmetic and measured runs.
If the actual shapes still do not fit or lack sufficient signal, return the
concrete measurements to the lead for the smallest justified adjustment. Do not
drop output/auth checks, widen regression budgets or retry until it passes.

The 30-second per-request watchdog is only a runaway safety cutoff. The observed
23.6-second 64-resource baseline leaves too little host-noise margin to mandate
that shape under this cutoff, which is another reason not to repeat it as a
release gate. Verify the accepted 16/32 baseline has substantial margin below
30 seconds; if it does not, report that measurement rather than treating an
expected near-limit baseline as an arbitrary regression. No mandatory extra
64-resource smoke is added. Its existing large-page evidence remains diagnostic;
any later one-shot expansion must fit a measured runtime/deadline plan and is
not a prerequisite for this release.

Acceptance additionally covers expensive-case count 1 / warmup 0 symmetry and
unchanged cheap-case batching, then one recorded 16/32 probe and the existing
postreview exact-head quick/weekly campaigns. Implementation and measurement
ownership remains with implementer1; architect performs no application edits.
Master-first integration and provenance-preserving release backport remain.

### Accepted weekly execution allowance

Lead accepted **45 minutes for the weekly workflow timeout**, with quick then
remaining at **10 minutes**, subsequently extended as recorded below. Actual
arithmetic for 34 weekly cases gives **1,766.3 seconds
of request work**, plus approximately **100 seconds of pilot/calibration** before
dependency preparation and evidence validation. The former 30-minute allowance
therefore cannot contain the intended work. This measured operational adjustment
supersedes that earlier allowance; it does not change the two-second batches,
seven pairs/six agreement, 10% regression budget, 32-resource complex page,
allocation ceilings or any deterministic check. The 30-second individual-request
runaway safeguard is a separate limit and remains unchanged.

Implementer1 amends the unmerged coherent source commit and matching project
documentation. Reviewer0 has been informed and must bind the resulting new head.
No new investigation, separate source package or approval wait is required.
Historical references to the original 10/30-minute workflow below describe the
inspected predecessor rather than the current execution allowance.

### Accepted framework footer normalization correction

Reviewer0's real 16-resource HTML response demonstrated another release identity
difference: `servers/ruby/lib/haveapi/views/main_layout.erb:83` emits the framework's
own VERSION in the footer, beyond the already recognized WebUI hrefs. Comparing
the real .0/.2 pages therefore failed response identity despite equivalent
non-version content. Lead accepted this bounded correction; no new approval wait
or broader investigation is needed.

At the existing `Release.html` comparison boundary, also normalize **only the
exact framework-emitted own-version footer in its real markup**, validated against
that source's own VERSION. Retain the complete original body, raw byte count and
raw hash; replay must recompute and validate the same narrow transformation.
All other content remains exact. No global version substitution, template or
product-runtime change, unrelated footer/text normalization, or relaxation of
authorization/output checks is permitted. Earlier href-only statements describe
the previous boundary and are superseded solely for this exact footer emission.

Implementer1 owns the focused fix and real-markup positive/negative tests in the
coherent unmerged master batching commit. Test both genuine own-version footer
differences and rejection of lookalike/incorrect versions, altered surrounding
markup or other content, plus raw/replay tampering. Reviewer0 continues the
affected compatibility/risk review against the amended head. Integrate master
first, then backport the exact finalized fix with `-x` as already required.

### Accepted calibrated JSON activation fix

Lead accepted a bounded preparation correction. Root, server and Rust locks all
resolve installed JSON **2.21.2**, but the shared gem store also contains **3.1**;
an unbundled `require` selects the higher version. A tiny Rust-page probe after
explicit 2.21.2 activation matched the recorded weekly dependency closure with
no differences and preserved the response body. The active 3.1 selection is an
environment identity mismatch, not a reason to change calibration or budgets.

Implementer1 must make the existing common helper/import boundary own exact
activation of calibrated JSON **2.21.2 before the first JSON load** in the parent,
neutral worker and direct replay entry points. Preserve the existing strict
loaded-version/environment checks. A local RUBYOPT mask alone is insufficient:
worker launch clears it, so the source-level entry paths must establish the same
identity independently. Do not install dependencies, parse lockfiles through new
machinery, add configuration or a dependency framework, or change calibration.
If the required installed identity is missing or another version is already
incompatibly activated, fail clearly rather than silently selecting a substitute.

Focused tests cover an extra higher JSON version visible in the gem store,
successful exact activation before loading, missing/incompatible identity and
consistent parent/worker/replay behavior. Implementer1 owns the minimal source
fix and checks; reviewer0 continues the affected environment/import boundary
review and binds the amended head. This is required hosted preparation within
the authorized master-first work, not a user-permission gate. Preserve exact
master integration and subsequent `-x` backport ordering.

### Accepted fresh-hosted JSON availability extension

The activation fix also needs a fresh-install prerequisite. Ignored library
lockfiles are absent on hosted checkouts; without explicit development constraints,
root/server/Rust Bundler preparation can resolve JSON 3.1 without installing
calibrated 2.21.2. Exact activation alone cannot establish availability.

Lead accepted minimal explicit JSON **2.21.2** constraints in the existing root,
`servers/ruby` and `clients/rust` development/test Gemfiles. Follow their ordinary
Gemfile conventions; do not create a shared-constant framework for one version.
Keep all published gemspec dependency requirements unchanged, library lockfiles
untracked, and existing calibration/allocation data unchanged. This supersedes
the preceding no-install restriction only to allow ordinary declared dependency
preparation to supply the constrained version on a fresh checkout; no ad hoc
installation workaround or new dependency machinery is authorized.

Implementer1 owns availability through the three Gemfiles, bundled startup and
the existing explicit parent/worker/replay activation boundary. Add focused
consistency checks against the immutable calibrated expected JSON identity and
cover fresh preparation without local locks plus bundled/unbundled selection.
Keep higher-visible/missing/incompatible-version negatives. Reviewer0 assesses
the changed dependency/preparation boundary and binds the new exact head.
No new approval wait or architect source edit; master-first integration followed
by the exact `-x` release backport remains required.

### Accepted JSON preparation-manifest compatibility delta

Lead accepted the direct compatibility consequence of the three development
Gemfile pins: their authored bytes differ from the retained `1741`, fixed
`b85ec364` and released .1 baselines even though both measured runtimes must
already use exactly JSON 2.21.2. The existing capture/input/replay normalization
may recognize **only the exact known JSON 2.21.2 constraint addition or replacement
of the known old unversioned entry**, restricted to the root, server and Rust
development Gemfiles. This is a preparation-identity delta, not permission to
change the resolved external version graph.

Retain raw Gemfile bytes and hashes, normalized hashes and explicit evidence of
the exact permitted delta. Replay must reconstruct and validate that same narrow
transformation; both actual runtime identities remain strictly JSON 2.21.2.
Reject every other requirement or content change, unexpected JSON spelling/value,
extra occurrence or path. Do not ignore Gemfiles, remove arbitrary JSON entries,
add a generic normalization registry, or broaden production dependency handling.
Published gemspec requirements, calibration and allocation budgets stay unchanged.

Implementer1 must run actual input preflight against the exact retained `1741`
baseline, original fixed `b85ec364` reference and .1 release baseline, recording
their full source identities and positive/negative evidence before a campaign.
Reviewer0 continues the affected input/provenance/replay boundary review against
the new head. No further design or approval wait; master-first integration and
exact `-x` backport remain required.

### Accepted measured quick execution allowance

Lead accepted **15 minutes for the quick workflow timeout**, with weekly unchanged
at **45 minutes**. The actual `be520` quick campaign measured **14/14 workloads
passing**, all batches adequate, **5/5 paired agreement** and the expected JSON
closure, but consumed **597 of 600 seconds**. Three seconds of operational margin
is insufficient for this valid workload. This adjustment is grounded in completed
execution cost, not a change made to convert a measured regression into a pass.

Only the workflow timeout, matching documentation limits and focused assertion
change. Workloads, operation counts, relative/absolute thresholds, environment
bytes and deterministic checks remain unchanged. Implementer1 folds the focused
change into the coherent unmerged commit with normal checks/hooks. Preserve the
`be520` refs and exact-source quick result, the ongoing weekly receipt, and proof
of implementation/input/derivation equivalence to the amended head.

Do not start a duplicate weekly campaign solely for this timeout metadata change.
Final review still covers the affected configuration/history and binds the new
head; new-head quick validation remains required. Any substantive difference
outside the declared timeout/doc/assertion change invalidates this narrow reuse
decision and returns to the ordinary affected-check/review procedure. Master-first
integration and exact `-x` backport ordering remain unchanged.

### Accepted measured validation and cheap-workload correction

Lead accepted this bounded amendment before application edits and assigned
implementer1 sole master source, index and canonical Git ownership. It addresses
the completed diagnosis of weekly run **40221259354, attempt 1**, at
`be520ed8ea8a82b4d1cb719a4066460f110bcf83` versus the unchanged fixed reference.
The run was cancelled at the 45-minute limit; its aggregate gate failed. All
23 workers completed all 34 workloads, but neither `report.json` nor runner exit
exists. Preserve the original **1,753,651,637-byte** samples and artifacts.
The [diagnosis](batching-hosted-be520ed8ea8a82b4d1cb719a4066460f110bcf83/weekly-diagnosis.json)
has SHA-256 `2ea43f8d724b265dde34eb35af472f4f97df2a8e6162dfb5291b77f1a1ba69ef`.

Measured worker process time was 2,520.6 seconds, including **714.5 seconds of
validation**, 136.4 seconds of reset/GC, 116.9 seconds of warmup requests,
45.3 seconds of fixture construction and 20.7 seconds of loading. The paired
measurement requests took 1,352.4 seconds; pilot/calibration add further request
work. Six list/OPTIONS cases account for 554.5 seconds of validation. One worker
contains 132,073 output references but only 34 distinct bodies, including 131,998
JSON references. The 2,627-second campaign leaves 106.4 seconds of parent/file/
partial-comparison work without finer attribution. Worker serialization took
only **3.50 seconds**. There is no RSS/OOM evidence and no measured remaining
comparison/report duration; neither a memory diagnosis nor a completion-margin
claim follows from artifact size.

**Implementation boundary.** Implementer1 owns one coherent correction in
`servers/ruby/benchmarks/{endpoints,performance_compare}.rb`, the existing
`test_support/performance_{endpoint,sqlite}_fixture.rb` validation boundaries,
focused `spec/performance/{runner,comparator,endpoint_contract,sqlite}_spec.rb`
and existing test support, plus `doc/performance.md`. No product runtime,
dependency, budget, reference or workflow-timeout change is proposed. Lead
serializes source/Git ownership. Implementer0 can independently retain and
measure diagnostic evidence against the supplied candidate after that handoff;
it must not edit source or duplicate the full campaign.

1. **Reuse expensive body proof only within one sample.** In the worker,
   separate body-only parsing, canonicalization and semantic output validation
   from operation-dependent checks at the existing fixture interface. Validate
   each distinct raw body completely once for that scenario, role and source.
   For every response still compute/check its raw digest and byte count, require
   exact bytes on a reuse hit (including the existing collision rejection), and
   execute status, relevant headers, called-index and per-operation counter/
   authorization checks. Reusing a valid body cannot validate an uncalled index,
   changed HTTP response or missing execution. Body-only semantic expectations
   may be reused only while the scenario/expected fixture state is unchanged.
   Reset reuse at every measurement/warmup boundary; do not key by response
   object identity or share results across scenarios, users, workers or sources.
   Keep verified body/canonical values immutable against later mutation.
2. **Apply the same boundary in replay.** In `Comparator#validate_sample`, verify
   retained raw hashes/bytes and raw-to-canonical equality once per distinct
   body, with duplicate-key rejection and exact own-version HTML normalization
   bound to the observation's source VERSION. Then validate *every* output
   reference against that proof: existence, digest syntax and equality, status,
   envelope, byte count, allowed comparison metadata/context, and every counter.
   Keep operation cardinality/order, cross-operation/revision equality and all
   source/input/lineage checks. Do not trust an asserted digest, memoize an entire
   output record, or let a later reference change normalization mode/version.
   All raw bodies and per-operation records remain in the existing sample and
   report format. No general cache or persisted validation proof is introduced.
3. **Raise the existing finite count ceiling to 100,000**, retaining baseline
   pilot selection and its one bounded adjustment, common counts for both
   revisions, and existing warmup rules. This supersedes the earlier 20,000 cap.
   The measured `rust.async_auth`/`rust.blocking_auth`
   batches took 0.50225/0.48421 seconds for 20,000 operations: approximately
   79,643/82,610 operations would target two seconds at those observed rates.
   A 100,000 ceiling accommodates those estimates with bounded headroom; it is
   not a hard-coded count for either endpoint. Worker and replay bounds must
   agree. Preserve observed wall/CPU adequacy and explicit cap diagnostics:
   an undersized batch is still inconclusive, never a measured pass. If the
   finite cap cannot provide adequate signal, report the measured limit for
   diagnosis; do not add another retry/adjustment loop or drop the workload.

The count estimates imply roughly 122,000 additional output/counter records
per measured worker for the two cases, and about **60 seconds of additional
request work across the 20 measured workers**, before calibration and validation.
These are estimates, not measured execution/memory bounds. Before a full run,
measure both cheap cases at the selected counts, record actual wall/CPU duration,
record cardinality/serialized bytes and peak process memory. Reuse must not retain
an additional body copy per operation. Establish sufficient wall/CPU signal and
a practical aggregate cost/memory bound from that receipt and the replay below;
do not silently increase the cap again if retention becomes a concrete problem.

**Focused acceptance before campaigns.** Use the prepared Nix environment and
`make test-performance`, focused normal lint/hooks, and the existing runner/
comparator specs. Add controls where a valid first occurrence is followed by a
changed body, forged digest/collision, canonical/raw disagreement, duplicate JSON
key, altered status/header/envelope/bytes, missing/reordered reference or counter,
wrong/uncalled index, or authorization/SQL/execution mismatch. Verify sample/user/
source isolation and mutation safety. Retain own-version HTML/footer lookalike,
comparison-context and source/input tampering negatives. Assert expensive parse/
canonical proof scales with distinct bodies while all operation checks still run.
Test selection and replay above 20,000, rejection above 100,000, common counts,
one adjustment only, cap-underadequacy, and the existing meaningful injected
regression controls. No threshold or correctness test is removed.

Perform bounded differential validation of retained representative samples
(including the six measured hotspots and repeated Rust auth bodies) through the
old and amended validation paths, preserving their original identities. Record
equal accepted identities/counters/classification and identical rejection of
the focused corruptions, together with elapsed validation/parse work. Derived
subsets are diagnostic evidence, not complete campaign passes. Exercise worker
validation as well as comparator replay; replay alone cannot prove worker
fixture semantics. Complete this focused subset differential, worker safety
checks, live proof for both cheap cases and quick checks, then commit with normal
hooks. Obtain an **affected independent final-review PASS before the long full
retained-sample replay**. This ordering preserves review before long integration
verification. After review, replay the preserved complete samples with the supported
`make performance-compare PERFORMANCE_ARGS='--input <original-samples> --budgets
servers/ruby/benchmarks/performance_budgets.json --output <new-directory>'` path
under a bounded watcher. Do not rewrite original evidence or its harness/source
hashes to resemble the new implementation. Retain stage elapsed times for input
parse, comparison and report writing so measured worker savings, added cheap-case
work and actual parent completion cost can support the next campaign estimate.
The full replay, including stage timing, precedes hosted quick and the one
representative weekly campaign. If full replay or retained identity validation
cannot complete, diagnose that concrete boundary before another campaign; do
not infer missing time or bypass the check.

**Report shape stays unchanged.** Compact reporting is not justified as the
primary fix by 3.50 seconds of measured worker serialization or an absent report.
Keep raw/replay recovery intact. A separately measured remaining report/IO cost
can be routed through the lead if it still prevents completion; no speculative
report/schema/storage redesign belongs in this package.

All **34 weekly workloads**, two-second target/1.5-second adequacy, seven pairs/
six agreement, 10% weekly and 20% quick budgets, 50-ms floor, allocation ceilings,
30-second batch safeguard, and **15/45-minute workflow limits** remain unchanged.
Existing expensive pages keep count 1/warmup 0. No request-count reduction,
timeout increase or reclassification of the original failed run is authorized.
The exact `40b514b92132c07f83a51752443448e42ec88a17` quick pass and other successful
checks remain historical source-bound receipts. This validation/fixture change
requires focused verification, committed-source independent review of the
affected correctness/security/history boundaries, final-head quick validation,
and **one representative final-head weekly campaign after review**, proving all
34 cases and both cheap cases adequate with a final report/exit and actual margin.
Unchanged component checks may be reused only with explicit source/input/
derivation equivalence. There are no migrations, persistent-state or product API
changes; benchmark evidence remains replayable. Master integration precedes
`-x` backport and separate .2 metadata; final release verification/publication
and the already accepted PHP mirror/recovery ordering remain lead-owned.

### Postreview retained replay and aggregate memory assessment

The accepted implementation `bdb034436e0dffbc39537a481442c3a2880cea9c` passed
affected final review and completed the supported full retained replay once.
The [assessment](retained-weekly-replay-assessment.json) preserves the original
`b85`/`be520` identities and sample hash: **31 pass, three inconclusive, zero
conclusive regressions**, with all 34 inventories and deterministic/raw/counter/
source/input/lineage checks accepted. Both old 20,000-operation authentication
cases remain inadequate. `rust.async_example` at size 16/admin is adequate at
2.128 seconds but has four pass/two regression votes, below six required.
Neither the original cancelled campaign nor this replay is a weekly pass; do not
weaken agreement or relabel these results. The new live cheap-case adequacy
receipt is separate evidence, not a replacement for these original measurements.

The unchanged-schema report is 1,753,704,743 bytes, SHA-256
`591b068d9bdf1956e9d6299a1936904637137295c552ad9a9c92e62104daaa4f`.
[Stage evidence](postreview-bdb03443-retained-replay-stages.json) records read
2.091 seconds, parse 12.419, comparison 40.693, serialization 8.390 and write
6.705; outer make/Ruby exited zero in 83.490 seconds (Nix launch 89.728).
Ruby peak RSS was **6,831,416 KiB, approximately 6.52 GiB**. This is a measured
process high-water mark on the replay host, not aggregate hosted-job memory or
an OOM diagnosis. The original samples, generated report and receipts stay intact.

Read-only inspection of `performance-replay-stages.rb` establishes that the
diagnostic observers retain scalar times, byte counts, digest/object ID and small
source metadata. They do not keep another raw input string, parsed sample graph
or serialized report alive after the observed call. The Python wrapper hashes
in blocks and writes child output to files. Instrumentation can affect allocation
or GC timing, so exact uninstrumented RSS is unmeasured, but there is no evidence
for dismissing the peak as an extra diagnostic-held full sample copy.

The normal comparison CLI briefly holds input text plus its parsed graph and
later materializes a complete report string. The normal run path accumulates
all paired worker case graphs, then serializes samples and report sequentially;
it does not read the aggregate samples file back. Report/case merges are shallow,
so their raw structures are shared in memory rather than deep copied. However,
`utils/performance_ci.rb` subsequently reads/parses the complete report after the
runner exits. That separate parent validation phase also needs to fit. Per-body
proof reuse reduces computation; it does not remove retained per-operation output
and counter objects or complete JSON serialization buffers.

Implementer0's [projection](retained-weekly-next-campaign-projection.json) uses
original hosted rates to estimate 79,643/82,610 authentication operations. These
are not actual future selections: local live proof selected 16,979/27,027.
The hosted-rate estimate adds 2,445,060 measured output/counter references and
about 1.20 GB of pretty JSON, taking samples to roughly **2.95 GB before larger
calibration records**. Both authentication bodies remain one distinct body per
sample. Scaling the old RSS by file size gives roughly 11 GiB as a sensitivity
only; graph/string lifetimes, GC and host differences prevent treating it as a
bound. The shared 100,000 ceiling is not a campaign-wide memory bound. Likewise,
the projection's time scenarios are sensitivities, not a verified 45-minute fit.

The fresh [capacity receipt](hosted-public-runner-capacity.json) confirms HaveAPI
is public (`private: false`). [GitHub's official public-runner table](https://docs.github.com/en/actions/reference/runners/github-hosted-runners#standard-github-hosted-runners-for-public-repositories)
documents standard x64 `ubuntu-24.04` as **four CPUs, 16 GB RAM and 14 GB SSD**.
This is the applicable documented capacity, not the original VM's measured
MemTotal, free memory or cgroup limit; the old receipt still contains none of
those. Do not equate documented total capacity with available process headroom.

Lead accepted **one requestless synthetic resource probe**, owned by
implementer0 through a fresh watcher, before selecting any source correction.
Use the existing reviewed implementation and preserve all original artifacts.
The finite envelope sets both `rust.async_auth` and `rust.blocking_auth` to the
**100,000-operation cap** in all 20 measured samples per case (six self and
14 baseline/candidate) and in each case's one retained calibrated pilot sample.
Relative to the original 20,000 counts, this adds **3,360,000 output/counter
record pairs** across 42 samples. The earlier 491-byte/reference estimate gives
about 1.65 GB extra, or approximately 3.40 GB total serialized samples; measure
the exact bytes rather than treating this estimate as a bound. Keep all other
32 workload counts and bodies as retained. This envelope bounds the two known
cap-related increases, not every possible new pilot selection in the other
workloads. Future count differences outside it require explicit reconciliation.

Preserve one distinct body per authentication sample and real, separate
per-operation objects as a normal JSON parse would allocate; repeated shallow
references must not artificially lower measured memory. Account for initial
one-operation pilot and pre-adjustment calibration artifacts at their actual
transient lifetimes, including worker-output/parse overlap. They are not extra
persistent comparison pairs; do not multiply all 23 full worker graphs as if
they were live simultaneously. Cover sample retention, normal complete samples/
report serialization and the outer CI report parse after the runner exits.
Record phase and peak RSS, elapsed time, actual bytes and the probe host's
available/cgroup/disk limits under bounded resources. Separate sequential peaks
from genuinely concurrent process memory.

The enlarged derivative is explicitly **synthetic resource evidence**, with
original-input/source attribution and a separate derivation receipt. Its altered
counts or measurement fields are not actual selected counts, request timings or
a performance pass. No original evidence or identity is rewritten. Hosted launch
remains on hold for lead acceptance of the resulting capacity/time/memory fit;
architect performs no duplicate parse, probe, campaign or remote observation.

No compact report, schema, runner-size, timeout, request-volume or threshold
change is selected from the current evidence. If a measured memory limit is
exceeded, route the smallest correction at the demonstrated owning boundary
through the lead, preserving complete raw evidence, replay and all output/
counter/source checks. Any substantive correction requires focused checks and
affected final review of the new committed head before long verification.
Existing master-first/backport/release recovery ordering remains unchanged.

## Superseded proposal: gross regressions across request types

This later user direction supersedes **all fine-timing pass and mandatory weekly
timing acceptance requirements below**. The user wants obvious slowdowns such as
100-second requests caught, across all request types; documentation was an
example, not the entire scope. Master-first integration and `-x` backport remain.
Implementer1 owns the bounded source/test/docs change under lead coordination.

Keep existing deterministic response/type, authorization, execution/SQL-count,
allocation/scaling, source identity and dependency checks authoritative. Keep
wall/CPU measurements as useful reports; ordinary small differences, runner noise
and an inconclusive fine comparison must not fail readiness or trigger repeated
campaigns. Do not tune GitHub hosts, recalibrate references or add provenance
machinery to make timing green. Existing correctness/proof failures still block.

Use the existing comparator and worker for a broad generous guard over **every
existing workload**, including public/Basic/token API actions, validation,
nested/list requests, SQLite pagination/includes, OPTIONS/HTML and Rust examples.
Initial concrete policy: a completed comparison blocks for timing only when the
candidate median request is both at least **10 times** baseline and at least
**1 second slower**. Independently, any single representative request exceeding
**30 seconds wall time** is a runaway failure, even without a completed pair or
when both revisions are slow. Record the exact workload/source and threshold.
These are gross-regression tolerances, not latency SLOs: versus the reported
roughly 0.1-second workload, a 1-second additive threshold and 30-second absolute
limit leave substantial host-noise headroom while rejecting the user's 100-second
failure class. Threshold changes need a concrete measured reason and lead
acceptance, not repeated-run tuning. Ordinary fine classifications may remain in
diagnostics but do not determine the process/aggregate exit.

The existing worker has no request deadline; only the workflow's 10/30-minute
job deadline is present. Bound a stuck request in the existing isolated worker
path, including pilot/warmups, preserve partial diagnostics and terminate/reap
owned work. Do not wait through all repeated samples after a runaway. Keep setup,
mount and dependency installation outside the request deadline; a separate coarse
worker/setup timeout remains an operational failure with a distinct diagnostic.
Implementer chooses the minimal reliable deadline mechanism without altering
application runtime or contaminating deterministic allocation checks.

Retain existing scale coverage as the base. Add one full HTML documentation
request with the Rust SDK profile enabled using the existing parameterized
fixture, initially **64 resources × 4 actions × 2 samples × 4 parameters**, with
admin/member output checks. Exercise actual page rendering, not only a single
adapter snippet. Apply the same 30-second request guard as all other workloads.
This bounded large-page smoke may live beside the existing deterministic request
contracts and need not enter repeated paired timing/calibration inventories.
Report actual action/example count, elapsed request duration and peak relevant
allocation evidence; do not add a fixed calibrated budget or a new benchmark
framework for it. If preparation proves this shape unsuitable, implementer
reports the concrete observation and proposes the smallest adjustment to lead.

Smallest owning files: `servers/ruby/benchmarks/{performance_compare,endpoints}.rb`,
focused comparator/runner/request-contract specs, `utils/performance_ci.rb` and
`.github/workflows/servers-ruby-performance.yml` only as needed to reflect the
new exit/report contract, plus `doc/performance.md` and directly conflicting
development instructions. Reuse the existing documentation fixture; change it
only if its parameters cannot express the full-page smoke. Preserve fixed source
reference and existing allocation budget bytes. No new framework, new general
configuration surface or expanded calibration/equivalence work.

Acceptance: tests show small/noisy/inconclusive timing passes with diagnostics,
clear gross slowdown fails, and a blocked request is terminated with its source
and workload identified. Test deadline logic with a controlled short test-only
limit or clock/process fixture, not a 100-second sleep. All existing negative
output/auth/count/allocation/provenance cases must still fail. Demonstrate the
same guard is used by API, SQLite and documentation categories, and run the
larger Rust-enabled page successfully. Normal hooks and focused quick checks,
then final committed-branch review, precede long verification under a watcher.

Run one representative postreview hosted check for the exact master feature and
the reconstructed final release head, with applicable component/release CI. Do
not require a successful 8/9 or 14/15 fine-timing agreement or mandatory weekly
precision campaign. Weekly/paired timing may remain optional diagnostic reporting;
if executed, deterministic and gross failures still block. Preserve original
failed evidence, classify ordinary timing findings informational, and rerun only
for an actual code/input fix or unresolved correctness/gross failure. Integrate
all source fixes into master first, then backport their exact commits with `-x`
and apply separate .2 metadata as specified below. No state migrations added.

## Current amendment: master fixes first, then backport

User correction: “what assumptions? the fixes should go to master first and then
be backported”. This explicitly authorizes HaveAPI master integration of the
bounded tooling/CI fixes, followed by their `-x` backport to `haveapi-0.30` and
the already authorized 0.30.2 release. No consumer pins or deployment are added.

Implementer1 owns the following package now in the lead-prepared, separately
registered same-session master feature checkout, clean at
`38ecca75edaf797d048fb36c6a50ea7e05eb50a9`. Lead serializes shared repository Git
operations. Implementer0 has relinquished application/Git handles. Preserve the
old published release candidate `5832ccc64dcf725a625c88ad440ddb631ff404b4`,
its complete eleven-commit range/diff, review and test/package/CI receipts.
It is superseded as the release candidate, not retroactively verified after fixes.

### Master implementation boundary

1. Transplant the coherent package B source change from
   `d32aa0f35e2af0ff5053de54c3e1eae2ca385a62` onto master. Retain its origin in
   evidence, consolidate the diagnosed fixes into reviewable functional source
   commit(s), and leave master VERSION/changelog at their development values.
   Do not transplant package C's 0.30.2 metadata to master.
2. Fix the confirmed Git serialization defect in the existing lineage proof.
   `git diff --binary` emitted variable-length abbreviated blob IDs: local
   auto-eight digits and hosted auto-seven digits changed the pinned digest for
   identical trees. Use explicit full object IDs (`--full-index`) and deterministic
   diff options/config isolation where required by the owning Git invocation.
   The complete two comparison deltas remain equal: canonical full-index output
   is **9,374 bytes**, SHA-256
   `0a008acbb46434a0914421064149ce154ea41a6e82a29022c53e666eb2066fd5`.
   This pin replaces the unstable 8,350-byte / `7fe745...` serialization pin;
   all four tree identities, exact mapping, ancestry, original fixed reference
   and budget bytes remain unchanged. Add a controlled short-abbreviation Git
   configuration regression; do not ignore proof differences or loosen equality.
3. Fix tests that assume the developer checkout contains full mapped history and
   a root Gemfile.lock. Server-only CI legitimately uses shallow history and a
   component bundle; it failed nine examples per Ruby. Use owned disposable Git
   fixtures and controlled input fixtures/mocks at the relevant test boundary.
   Keep actual production proof/source integration coverage in a full-history
   prepared test lane. Do not skip the gate, manufacture production history,
   require unrelated root installation for component tests, or weaken missing
   object/lock refusals. Implementer1 owns concrete diagnosis and implementation.

Source boundaries remain the existing resolver, endpoint runner/comparator,
their focused performance specs (including release_lineage_spec.rb), and owning
performance documentation. Change a workflow only if diagnosed execution needs
it; route any broader source/input change through the lead. No generalized proof
framework, new policy settings, budget relaxation, reference replacement or
product runtime redesign. Preserve narrow own-version dependency/HTML validation
and raw/replay evidence, with existing master/default/PR behavior.

### Acceptance and ordering

Quick checks on the complete master feature: normal hooks, syntax/RuboCop,
focused resolver/lineage/worker/replay specs, canonical full-index positive and
tamper-negative proof, controlled Git abbreviation settings, and server tests
with shallow/component-only assumptions represented accurately. Record actual
checks and exact inputs. Once intended source commits and quick checks pass,
obtain independent final whole-master-branch review before longer checks.

Postreview verification must resolve the original failures, not merely rerun:
Performance `40210112771`, server RSpec `40210112783`, and build-only release
`40210113193`. Preserve original logs/artifacts and diagnosis. Run required
master feature CI and applicable master quick/weekly comparison with unchanged
reference/budgets; use fresh verification watchers for long/uncertain work.
Require final exact-head results and full-history production proof as well as
portable component specs. A release build-only check retains master's current
development version and does not publish.

After review/checks and final remote refresh, lead integrates the master feature
fast-forward with the already authorized short repository claim, push and remote
proof; release before records or CI waits. Then reconstruct the release series
from retained package A head `b9b971b929edc75ef2f11fb6e541c1e0b52c99e1`, preserving
all nine exact A backports and mapped ancestor
`8b7abc097db49893da9cc8fa4395648901fec71d`. Cherry-pick the final integrated master
fix commit(s) with `-x`. Do not carry old B as a second redundant adaptation.
Apply one separate final 0.30.2 metadata/changelog commit last. Lead owns the
registration/ref transition; retain the old published candidate ref/evidence and
never rewrite master, existing release tags or accepted package bytes.

Compare old and new release ranges, map B's coherent master successor and its
backport, record exact final heads and substantively changed versus equivalent
parts. Previous exact-C review/full-suite/build evidence is historical: follow
mandatory review's affected-lane/reuse rules and obtain the explicit final
whole-release-history/migration conclusion. Rerun changed-path quick checks and
required exact-final-head CI, quick .1-to-.2 and weekly fixed-reference-to-.2
campaigns, then final package/version/artifact checks. Reuse only independently
supported exact verification; tree similarity does not substitute for new-head
evidence. Preserve the original tagged-run-artifact PHP pre-sync publication and
partial-failure contract, now bound to the new final release source.

Compatibility remains unchanged: tooling/test portability fixes only; **no
database migrations or persisted-state changes**. No new release authorization
is required. No tagging, mirror pre-sync or registry publication until the
master-first sequence and new release gates complete.

## Scope and immutable baselines

Backport every improvement present in the fetched HaveAPI master snapshot to the
maintained `haveapi-0.30` branch, then publish all maintained packages as 0.30.2.
Only HaveAPI application source and its documented PHP publication mirror are
in scope. The current amendment adds master-first tooling integration; there are
no consumer pin changes or system deployments.

SSH fetch of `git@github.com:vpsfreecz/haveapi.git` completed on 2026-10-25.

| Role | Exact revision |
| --- | --- |
| Master source snapshot | `38ecca75edaf797d048fb36c6a50ea7e05eb50a9` |
| Maintenance baseline and peeled v0.30.1 | `1c3c98f0d77e0b23c8da1a8937f25c5799864a3b` |
| Common ancestor and peeled v0.30.0 | `b64fb25bea8d8222fb3263b99956c0b61438a859` |
| Annotated v0.30.1 tag object | `86748f77c090b2549f83df9fcdf26db7626a1539` |

`git cherry -v origin/haveapi-0.30 origin/master` establishes 13 already
patch-equivalent commits and exactly nine missing commits. Do not replay the
duplicates or merge master wholesale. Retain the maintenance branch's 0.30.1
metadata until the separate version commit.

## Package A: source backport, implementer0

Use the lead-created feature checkout
`worktrees/2026-10-25-haveapi-backport-release/haveapi`, branch
`2026-10-25-haveapi-backport-release`, starting at the exact maintenance baseline.
Apply these commits in order with `git cherry-pick -x`, preserving provenance:

| Order | Master commit | Change and owned files |
| --- | --- | --- |
| 1 | `39909094649b1d14a23f00615775ca7136acf4fd` | Flake ancestry guard: `.github/workflows/update-nixpkgs.yml`, `utils/update-nixpkgs.sh`, development instructions |
| 2 | `5003ded2a47db6b1637a3fef2fdd40474ea7de06` | Ruby documentation context ownership and its context specs |
| 3 | `82a7f8880663dfa9d8ad6cd67e981a5842dedf9c` | Rust documentation adapter selection and unit/performance specs |
| 4 | `de799b595d04e880d092b3e5ef47bce2f4587130` | Documentation context/rendering complexity specs and shared fixture |
| 5 | `b85ec364057f536940d689b09e612512ffffaf82` | Documentation benchmark, Makefile and explanatory docs |
| 6 | `610da4e3212e66fac026eb94eedb55abf6d3c66a` | SQLite performance fixture and deterministic contracts |
| 7 | `4e05ca8dc4f6b938814b354996025b0aad91d9c7` | Endpoint fixture, contract and scaling specs |
| 8 | `e98e704e926961bc6d8e4a12ee15c77c1380e7a8` | Performance CI workflow/resolver, event specs, Makefile, README and performance docs |
| 9 | `38ecca75edaf797d048fb36c6a50ea7e05eb50a9` | Paired runner, comparator, fixed budgets and runner/comparator specs |

This is one serialized Git package because source commits overlap Makefile and
documentation. Preserve each upstream functional commit and its provenance;
these are separately integrated upstream changes, not obsolete local attempts.
Report conflicts or non-equivalent adaptations to the lead. Do not version,
publish, rewrite the performance reference or change budgets in package A.

Acceptance: nine mapped backport commits; all 22 master-side changes since the
common ancestor accounted for; final functional tree matches master except
maintenance release metadata. Record full source-to-backport SHAs, especially
the backport of `b85ec364`, for package B's lineage proof. Re-run `git cherry` and
review the final master-to-feature diff after applying the complete set.

## Already covered source changes

The following master commits already have patch-equivalent 0.30 backports:

| Master | Existing maintenance commit |
| --- | --- |
| `cbf6a3f0` | `587a04d0` |
| `431d7ffe` | `40471f2e` |
| `01a30a39` | `e3648859` |
| `41251117` | `73df3866` |
| `c424c579` | `e406ae4c` |
| `090a188c` | `8270b519` |
| `4dc0f7e1` | `682a9869` |
| `6cb3c3e8` | `a252adbc` |
| `f08d3f63` | `d7bfed77` |
| `dc52a7a5` | `9c5de167` |
| `67fcd34b` | `8591394e` |
| `7ac977a2` | `2ffaa682` |
| `1103a3a1` | `17318459` |

## Interfaces, invariants and compatibility

The two runtime changes optimize documentation work. Context derivation shares
already-owned immutable snapshots while normalizing explicitly replaced values;
caller containers remain detached, unknown keywords remain errors, and subclass
construction preserves subclass initialization behavior. Rust documentation
selects the authorized action/provider subtree before recursive normalization;
it must preserve mixed String/Symbol key precedence, provider equality and
credential selection, without retaining one user's request context for another.

All other missing changes are fixtures, deterministic tests, measurement tools,
CI and documentation. Flake updates must remain forward-only with proof of input
ancestry; the backport itself does not change flake.lock. No database migration,
seed, stored-state format, network protocol or generated-client public API
change is intended. SQLite schemas are disposable test fixtures only. Existing
0.30 clients and servers can run together; there is no fleet-wide update or
deployment ordering requirement. Rolling back package selection to 0.30.1 does
not require state conversion. Published package/tag bytes remain immutable.

The supported Ruby declarations are unchanged: server and Go generator >=3.2.0,
Ruby client >=3.0, Rust generator >=3.2; repository Nix shells use Ruby 3.4.
PHP requires >=8.0, Python >=3.11, and the embedded Rust runtime declares 1.95.
The JavaScript bundle retains its existing ES5/browser and TypeScript contracts.
Minimum-version support is not inferred solely from testing in Ruby 3.4.

## Package B: performance release-lineage adaptation, implementer1

Confirmed incompatibilities of an unadapted backport:

1. Feature/release pushes use merge-base against master, which selects v0.30.0;
   that source predates libffi shell input changes already released in 0.30.1.
2. Strict dependency and raw gemspec equality reject the release's internal
   `haveapi-client` constraint changes from 0.30.0/0.30.1 to 0.30.2.
3. Weekly verification requires master reference `b85ec364` to be a literal
   ancestor, which cherry-picked maintenance history cannot establish.

The fixed reference, budget bytes, actual third-party dependencies and fail-closed
gates must remain intact. The lead accepted this bounded adaptation and the
presentation normalization below. Implementation diagnosis belongs to
implementer1; consequential scope changes return to the lead.

Owned files are `utils/performance_ci.rb`,
`servers/ruby/benchmarks/{endpoints,performance_compare}.rb`,
existing relevant specs under `servers/ruby/spec/performance/` and
`doc/performance.md`. Prefer existing resolver, input and body-comparison paths.
A small shared helper is allowed only if those existing paths need identical
validation; do not introduce a general provenance framework or new settings/API.
Do not edit fixed budget JSON, fixtures or product runtime for this adaptation.
Lead must transfer ownership after package A checks and serialize Git/index
operations. Package C owns version files and changelog afterward.

### Release lineage and event selection

Master fixed reference `b85ec364057f536940d689b09e612512ffffaf82` maps to the
literal maintenance ancestor `8b7abc097db49893da9cc8fa4395648901fec71d`.
The full package A head is `b9b971b929edc75ef2f11fb6e541c1e0b52c99e1`.
The reference-to-mapped-reference tree delta must be exactly the already released
metadata-only commit `1c3c98f0d77e0b23c8da1a8937f25c5799864a3b` relative to its
parent. Comparing those complete binary Git diffs proves the same source tree
modulo that exact published version/changelog transformation; preserve both
exact ranges, trees and comparison result. Do not accept cherry-pick trailers
alone, ignore entire version-containing files, or call the nonancestor master
reference literally merged. The equality was verified by the architect.

Retain original `REFERENCE` and budget calibration source SHA. Weekly continues
to measure the original reference bytes, not a newly calibrated replacement.
Permit its nonliteral ancestry only for this exact proven mapping when the
mapped maintenance commit is an ancestor of the actual candidate. Apply the same
check in event resolution and the direct runner; unrelated or missing history
still fails. Retain mapping evidence in the performance receipt. Future history
rewrites need a newly reviewed mapping rather than an inferred replacement.

For pushes to `haveapi-0.30`, compare event `before` and `after`, covering the
whole pushed batch. For feature pushes on this proven maintenance lineage, use
merge-base with the captured `origin/haveapi-0.30` head rather than master.
Record captured release head and selection reason alongside existing captured
default evidence. Keep master pushes, ordinary master features, PR event head/base,
schedule/manual default resolution and fail-closed malformed-event behavior.
Explicit manual quick pairs accept a real ancestor; explicit weekly pairs use
the original fixed reference plus the approved equivalent-ancestor proof.

### Dependency and presentation comparisons

Keep exact source exports, source SHAs, raw tree hashes, loaded-file proof, Nix
graph, local lock bytes and actual third-party runtime identity. Compare dependency
graphs after normalizing only the repository's own patch version and internal
`haveapi-client` constraint where it exactly matches that source's own shared
VERSION and a matching local component loaded from that verified source. Accept
only same-series 0.30 patch identities for this release adaptation. Require every
non-own dependency requirement, platform, Ruby requirement, flake input and
non-version gemspec content to remain equal. Preserve raw and normalized hashes
and the exact substituted own-version evidence; never mutate exported sources.
The candidate's prepared environment is reused for both sources, with no second
dependency resolution or relaxed environment/budget comparison.

HTML includes own-version WebUI links. Outside the timed request loop, allow only
the validated own HaveAPI version in the documented
`https://webui.haveapi.org/v<own-version>/` link target to normalize for comparison.
Read and validate each source's own VERSION. Retain complete raw body, raw hash,
raw byte count and normalized comparison digest. The comparator must be able to
revalidate the exact narrow transformation from raw evidence when replaying.
Do not globally replace version strings or alter JSON/API values, example code,
other hosts/URLs, authorization markers, missing panels or any other content.
All non-version output differences continue to fail. Ordinary master comparisons
must remain unchanged. The lead explicitly accepted this scope.

### Required bounded checks

Add meaningful tests for release push whole-batch selection, new/subsequent
release-feature pushes, captured release refs, explicit weekly fixed-reference
mapping, and existing master/PR/default behavior. Reject missing refs, wrong
mapping tree/metadata delta, nonancestor mapped reference and unrelated history.
For inputs, accept own .1/.2 version and synchronized internal constraints only;
reject third-party constraints, Ruby/flake changes, mismatched local package
identity and arbitrary changes in otherwise version-containing files. Preserve
and verify raw provenance in worker and replay paths. For HTML, accept only the
specified own-version link change and reject lookalikes, other URLs, API data,
auth/output differences and inconsistent raw/normalized hashes.

Quick checks: changed-file syntax and RuboCop, focused event/runner/comparator
specs, then existing deterministic `make test-performance` when classified quick
by observed duration; otherwise use a fresh verification watcher. Final review
includes these source changes and the exact release metadata .2, followed by
long timing acceptance through a watcher. No fixed-budget or fail classification
may change to make these pass.

Actual post-review campaign commands run in the top-level prepared Nix shell,
outside Bundler with the same GEM_PATH/environment clearing as `doc/performance.md`.
Let C be the full final committed 0.30.2 candidate SHA. Use unique new evidence
and source directories beneath this session's disposable evidence directory.
The existing supported resolver/campaign entry points are:

```sh
ruby utils/performance_ci.rb resolve \
  --event /absolute/quick-event.json --event-name workflow_dispatch \
  --event-sha C --repository "$PWD" --output /absolute/quick-selection.json
ruby utils/performance_ci.rb run --repository "$PWD" \
  --selection /absolute/quick-selection.json \
  --evidence /absolute/quick-evidence --sources /absolute/quick-sources
```

The quick event JSON has repository default_branch `master`, inputs profile
`quick`, candidate_sha C, and baseline_sha
`1c3c98f0d77e0b23c8da1a8937f25c5799864a3b`. For the corresponding weekly event,
use profile `weekly` and baseline_sha
`b85ec364057f536940d689b09e612512ffffaf82`, with distinct output paths. These are
real CLI invocations, not replacing the fixed baseline with the release mapping.
Preparation needs root/server bundles and client-rust bundle for weekly.
Capture resolver evidence and exact runtime/input graph. Require exit 0, report
status pass, matching final C, complete workloads and the unchanged fixed-budget
digest for both campaigns. Timing regression, inconclusive, dependency mismatch
or output mismatch blocks release readiness and belongs to implementer diagnosis.
Hosted feature-push Performance gate must independently pass on exact final C;
do not substitute a manual local campaign for unexplained hosted failure.

## Package C: release metadata and artifacts, implementer1

Depends on packages A and B. Prepare ignored library dependency locks in the Nix
shell; preserve their resolved third-party graphs when running
`make version VERSION=0.30.2`. Update CHANGELOG.md with the repository's dated
heading and only changed components: Ruby server documentation performance,
Rust documentation performance and development/CI safeguards. Lead owns final
user-facing wording under the writing procedure. Keep release metadata in its
own commit after source changes, with hooks enabled. No library lockfiles or
generated server documentation/build artifacts may be committed.

`make version` owns shared VERSION, Ruby version constants, internal gem
constraints, JS package/source/distribution versions, PHP metadata/version,
Python pyproject/local lock and the example dependency. Verify its exact diff
instead of editing version fields independently.

## Verification and final acceptance

Read repository development/release instructions and use the declared Nix shell.
Hooks must be installed, signed where required and passing; no bypasses. Quick
checks include syntax/RuboCop on changed Ruby, `bash -n utils/update-nixpkgs.sh`,
source/metadata consistency, relevant documentation context and Rust adapter unit
specs, and deterministic performance resolver/comparator/fixture specs. Run
`make doc` before Ruby server specs. Verify imported workflow action versions
against their official repositories when backporting/changing workflow files.

Known quick checks can run inline. Fresh policy-resolved utility watchers launch
and monitor uncertain/long checks; source diagnosis remains with implementers.
Commit all intended changes and pass quick checks before independent final
review. Give reviewer0 the complete baseline-to-final series, final diff, all
source/backport mappings, the package B adaptation proof, and an explicit
**no database migrations or persisted-state changes** conclusion.

After review, run the relevant complete checks and all-component release build:
`make release-deps`, `make release-check`, `make release-test`, `make release`,
`make test`, npm retained-tarball smoke, Rust packaged-generator smoke/verification,
and Python package smoke, with clean tracked source and an empty build destination.
Avoid redundant rebuilds when exact reviewed-head evidence already covers these
commands. Preserve local resolved locks, Nix derivation/input graph, exact source
head, manifest and checksums. Verify branch CI for the exact final feature head,
including Performance gate and release build-only checks. Package B must define
and pass exact quick and weekly release-lineage performance acceptance before
declaring the branch ready.

## Publication, integration and recovery

The lead records the user's explicit instruction as authorization to integrate
HaveAPI `haveapi-0.30` and release 0.30.2 through the existing all-component
workflow, including `haveapi-client-php/master` plus its version tag. The later
explicit user correction additionally authorizes master-first integration of the
tooling fixes described in the current amendment. Repository/target coordination
claims, selected-package instructions and final fresh remote checks remain
required for the maintenance integration; complete preparation/review outside
the claim and release ownership before CI or tracking work.

The documented release produces four gems (`haveapi`, `haveapi-client`,
`haveapi-go-client`, `haveapi-rust-client`), npm `haveapi-client`, Python wheel
and sdist on PyPI, the PHP Composer mirror, browser bundle and GitHub release
assets/manifest. Elixir is unmaintained and excluded. Push an annotated v0.30.2
tag only after source integration and release checks. Protected GitHub `release`
environment approval is an enforced publishing gate; do not bypass or weaken it.
Build-only Actions runs do not publish. No credentials belong in evidence.

For the PHP mirror's separate short repository claim, see the operational
recommendation in [architect-evidence.md](architect-evidence.md#php-mirror-publication-and-short-claims).
The supported pre-synchronized path uses the original tagged-run PHP artifact,
an exact snapshot/source-attributed mirror commit and annotated tag, then remote
proof and claim release before protected publishing approval. The unchanged
helper verifies the matching tag and skips its own mirror mutation. This is
actual PHP publication before the remaining registries; lead acceptance of that
ordering is required. It introduces no private helper call or workflow change.

After publication, verify remote maintenance head/tag, all package identities and
retained hashes, PHP mirror source attribution/tag, GitHub release assets and
Packagist indexing. Publication can be partial: retain the original tag, Actions
artifacts, manifest and draft release, diagnose failure and reconcile successful
uploads before retrying failed jobs. Do not move tags, overwrite accepted packages,
rebuild accepted artifacts or blindly reupload on stale metadata. Source fixes
after a partial published version require a new patch version. Leave this session
open; no lifecycle action is authorized by completion or handoff.
