# API example copy regression: implementation and verification brief

Scope accepted by the user: finish the investigation, repair generated TypeScript
example copying using the supplied patch where suitable, put **all** registered
client examples into meaningful performance coverage, verify, integrate HaveAPI,
backport all new fixes into `haveapi-0.31`, and release 0.31.1. This is one HaveAPI
change; no consumer rollout or general benchmark redesign is required.

Investigated base: `4d36efcfb2a9f677b5dfe0e632d8353eefe9a79c`. Source work belongs
to implementers in this session's HaveAPI worktree. Lead owns tracking, approval
records, final review, serialized Git operations, integration and release.

## Package A — generated TypeScript fix (ready now; implementer0)

Files: `clients/typescript/lib/haveapi/typescript_client/documentation.rb`,
`clients/typescript/spec/unit/documentation_spec.rb`, optionally a focused
`documentation_performance_spec.rb` beside it, and a short invariant note in
`clients/typescript/docs/documentation.md` if useful. Start from the session's
`supplied-typescript-documentation.patch`; do not access its source session.

Use shallow normalized member lookup along the selected resource/action path,
authentication provider and metadata namespace, then recursively normalize only
the selected action/provider/value. The supplied patch follows the existing Rust
solution and is the selected implementation direction. No persistent request
cache and no shared adapter mutation. Do not normalize the complete authorized
description inside a render.

Preserve output and limitations, canonical-action precedence over aliases,
ambiguous-alias rejection, symbol values and last-insertion string/symbol key
collisions. Provider equality must still compare the complete selected provider
when explicit authentication metadata is supplied. Token headers, filtered
fields, routes and metadata contracts keep their existing validation. Frozen
inputs must remain unmodified; allowed/denied/allowed contexts through one frozen
adapter must not retain authorization decisions.

Acceptance: real successful public/protected and aliased examples; Basic/token
authentication; unavailable or stale actions/providers; collision and frozen-input
checks. A deterministic recursive-work regression must fail on the original
adapter and pass with the patch while unrelated descendants grow and the selected
action/provider/output remain fixed. Test canonical and alias action lookup and
auth separately. Selected-provider contents legitimately affect full equality;
do not prohibit required selected-subtree work. Preserve the supplied behavioral
tests, reducing duplication where appropriate.

Quick checks: focused TypeScript documentation/recursive-work specs and changed
Ruby style under the declared Nix environment; record the original red and fixed
green result. All TypeScript unit/compilation checks are the next package check;
uncertain or long checks use the monitor skill. No unrelated client runtime
compilation is needed merely to prove this source fix.

## Package B — all-client performance coverage (implementer1)

Independent files: server performance fixture/specs, benchmark coverage entry
point if needed, `utils/performance_ci.rb`, the performance workflow, relevant
Makefile targets, and performance/client-example contributor docs. Do not edit
Package A files. Go production code needs no rewrite: it copies its private model
once during setup and looks up selected live subtrees while rendering.

Use a **current-source all-client performance contract** beside the existing
historical paired timing suite. The old fixed reference predates generated
TypeScript; it cannot honestly render every current client. Do not weaken its
provenance checks, manufacture an old TypeScript implementation, skip an unknown
renderer, or change its calibrated budgets/reference to hide this constraint.
The new required contract measures deterministic work/allocation scaling and
complete HTML rendering on the candidate. It is not a historical timing pass.

Lead accepted this approach. The concrete entry point is a focused spec beneath
`servers/ruby/benchmarks/spec/`, outside ordinary server Bundler discovery, with
an explicit Makefile target executed unbundled in the existing locked benchmark
shell. That bundle already supplies Rust's optional third-party dependencies;
the ordinary server bundle does not. The required performance workflow runs this
target before the historical comparison. Do not silently change the ordinary
`test-performance` dependency context. Document both required commands and the
difference between all-client allocation/work gates and historical wall/CPU gates.

The contract must load real optional Go/Rust/TypeScript adapters with the existing
prepared Ruby dependency closure, register valid profiles, and enumerate the
complete live `HaveAPI::ClientExample.clients` registry. Account for all 15
current IDs/modes. A coverage matrix must equal the registry (not just be a
subset); new IDs or unsupported kinds without an explicit reviewed expectation
must fail. Missing dependencies/profiles must fail, never skip. Exercise init,
advertised authentication and action samples for each renderer with real code,
including Basic auth shared by all current renderers. Cover additional advertised
authentication as code or an explicit limitation according to existing support;
a limitation-only fixture must not stand in for successful action rendering.

Build a small common supported schema with scalar fields, successful and failed
samples, multiple resources, and admin/member filtering. Avoid letting Go's Custom
limitations turn all its action panels into limitations. For direct renderer
measurements keep the chosen action/sample/provider fixed and increase unrelated
description descendants; setup, ownership copying, profiling registration and
expectations stay outside measurement. Assert bounded allocation/work growth
using modest repeated batches and a stated tolerance, with unchanged output.
Demonstrate that the unfixed TypeScript path fails the contract. Existing focused
Rust traversal assertions remain in place.

Render complete HTML pages with all profiles enabled and assert every registered
init/auth/example panel, actual code and admin/member isolation. Measure page
allocation scaling across resource counts with fixed actions/samples per
resource; account for expected linear output growth. Validate that this bound
rejects whole-description-per-example copying. Do not use an uncalibrated wall
clock deadline as the regression assertion. Record counts/allocation evidence;
wall/CPU may be diagnostic only. Reject an inventory containing unmeasured modes
or missing panels even if the timing/comparison step succeeds.

Wire this contract into ordinary relevant CI and the required performance gate
before the historical comparison. Extend relevance to all client sources and
shared rendering/coverage inputs, including Go and TypeScript; cover that routing
with a small resolver test. Ensure manual/scheduled execution also runs complete
current-source coverage. Keep the existing quick/weekly historical workload and
fixed-reference budgets unchanged. Prefer a focused spec/entry point over adding
a second baseline/replay/migration framework.

Package B must report exact fixture shapes, registry matrix, demonstrated
red/green sensitivity and bounded checks to the lead. If all-profile loading
requires a dependency or runtime change beyond existing prepared dependencies,
stop that expansion and route the concrete issue through the lead/architect.

## Compatibility, recovery and delivery

No API wire/schema, database migration, persisted format, generated SDK naming,
configuration requirement or daemon protocol changes. Mixed server versions
remain compatible; the change reduces documentation rendering work. Restore
the prior HaveAPI packages to roll back; no new persisted state needs reversal.
There is no production deployment in this task. Keep generated SDK/runtime
versions distinct from the HaveAPI package patch version.

Quick package checks and hooks precede committed independent review. The review
must assess complete source/test changes and branch history, including no
migrations. Then run longer required all-client/full-suite and performance CI
checks with a fresh monitor. Reuse exact successful evidence; do not rerun broad
suites without changed inputs or a concrete unresolved risk. Review any material
design change through the lead before changing the approach.

User authorized integration and 0.31.1 publication after verification. Lead will
fresh-check remote heads, integrate master under the short repository claim,
backport all new source/test fixes to the newest `haveapi-0.31` branch using
`cherry-pick -x`, preserve unrelated maintenance commits, and verify equivalence.
Release metadata/changelog is a separate commit. Follow the repository release
procedure and protected workflow with exact final-head evidence; never move an
existing tag or rebuild an accepted partial release. The original artifacts and
receipts remain the recovery authority for partial publication. Session remains
open; integration or publication does not authorize lifecycle cleanup.

## Package C — synchronized own-version comparison (release blocker)

Lead authorized this necessary correction after read-only investigation. The
existing generic paired runner compares raw internal `haveapi-client` constraints;
`make version` changes those constraints. Both 0.30.0 master versus 0.31.1 release
and 0.31.0 versus 0.31.1 therefore fail before measurement. The special 0.30
maintenance mapping cannot help: `Release.lineage` returns nil when the fixed
reference is a literal ancestor, as it is for the 0.31 branch. The maintenance
mapping's historical ancestry proof must remain unchanged.

Owner: implementer1, after Package B's Git slot is free. Files:
`servers/ruby/benchmarks/performance_compare.rb`, `endpoints.rb`,
`utils/performance_ci.rb`, focused `servers/ruby/spec/performance/` tests and a
small `doc/performance.md` clarification. No workload, budget, fixed-reference,
sample-format migration or external dependency changes. Lead serializes commits.

Add one small shared own-source-version capture/validation helper, separate from
the existing 0.30 ancestry certificate. It may normalize **only** a source's
canonical numeric `VERSION`, the matching VERSION assignments of the three
consumed Ruby components (server, Ruby client and Rust generator), and their
exact synchronized `haveapi-client '~> <own version>'` requirements. Validate
package identities, unique declarations and equality to the source VERSION
before replacement with a fixed own-version placeholder. Missing/duplicate,
malformed or unsynchronized declarations fail. Do not strip arbitrary version
strings, relax external dependency requirements or normalize other source bytes.

Retain raw contents, raw hashes, own version and normalized hashes in an explicit
`source_versions` receipt (or equivalently named distinct key). Compose the
existing exact JSON-preparation rule; keep third-party manifest bytes, benchmark
bundle/lock, loaded dependency graph, runtime and other identities strict.
Preserve the old `release_versions` path and its 0.30 proof unchanged, and reject
simultaneous conflicting receipt types. This is input identity normalization,
not authorization for a different baseline or a new release-lineage mapping.

Three consumers must agree:

1. `Campaign.verify_dependencies`: generic preparation captures both sources
   using this helper, validates evaluated gemspec/runtime requirements as now,
   and compares the normalized complete input graph. If parsed gemspec objects
   are also compared, normalize only their already-validated own dependency
   field; do not leave a second raw own constraint that recreates the failure.
2. `Worker.inputs` and the live runner: generic workers retain the receipt and
   normalized manifests; verify loaded component VERSION constants equal the
   captured source version. The parent recomputes the receipt, binds every raw
   hash to the exact verified source tree, and compares the normalized graph.
3. Replay validation and `Release.graph`: recompute and source-bind the same
   receipt, then exclude only the raw receipt wrapper from common-graph equality.
   Normalized manifests remain in the compared graph. Preserve old sample
   acceptance with raw manifests when no new receipt is present; stripping a
   receipt must never make normalized manifests pass raw-source verification.

Keep resolver event/baseline/ancestry rules unchanged. No special branch-name
exception, synthetic baseline or new command-line bypass. The ordinary 0.31
path must not invoke `Release.capture` or `Release.html`, which intentionally
support the historical 0.30 mapping only. Cross-source response changes already
remain diagnostics; own-version footer/WebUI changes need no new HTML
normalizer. Within-source response stability and all existing output checks
continue to apply.

Quick acceptance checks: demonstrate current rejection then acceptance for
0.30.0→0.31.1 and 0.31.0→0.31.1 with otherwise identical dependency inputs;
cover preparation, live worker graph validation and replay. Reject external
dependency edits, benchmark lock/runtime changes, unsynchronized own versions
or requirements, missing/tampered receipts and raw-source hash mismatch. Retain
the existing 0.30 lineage and legacy replay tests. Synthetic fixture versions
must not depend on the checkout's current minor version. No new timing run is
required to prove this metadata rule; focused deterministic specs and Ruby
style are the quick checks, followed by the necessary exact-release performance
CI once the reviewed change is backported.

Commit this as a separate functional source-branch correction, then backport it
with `-x` before 0.31.1 release metadata. The lead reruns independent review for
affected comparison/provenance lanes with the retained reviewer. Existing source
CI for 8ea2c365 continues; new final-head checks follow the actual source change.
