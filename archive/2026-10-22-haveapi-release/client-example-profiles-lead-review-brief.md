# Final profile review brief at67fcd34b

Review after owner0's final committed packet is accepted; all source quick
receipts and actual hooks have passed. This brief supplies user intent and scope; owner0 supplies exact
head/tree, complete series/diff/maps and inventory. No conclusion is prescribed.

The user requested simpler configuration for SDK examples: default generator
version to the server HaveAPI version; derive current schema automatically;
remove required Rust packaging TOML; make SDK package versions optional. Go
requires only import_path; Rust requires crate_name, with optional exact Git/rev
for an unpublished SDK. Package-manager commands choose omitted versions when
the user installs the SDK; no server-side registry lookup occurs. Old saved
forms remain supported. Accepted design:
client-example-profile-simplification-design.md.

Repository HaveAPI, worktree haveapi-client-example-profiles, initial4dc0f7e.
Final head67fcd34ba506264a5c7ee2e8e18a88d221c6f469, tree
80804b1c0c3ed33fc4b086673dbc3618a789cd4f, clean tracked/index/nonignored.
Lead read-only inspection confirms exactly five commits after090a, including
4dc0,6cb3c3e8,f08d3f63,dc52a7a5 and67fcd34b, with the accepted four source
purposes and unchanged dependency boundary.
Whole final-readiness range starts at remote master090a188c and includes the
independently reviewed dependency commit4dc0 plus four intended profile commits.
Do not review only the newest server commit. Owner0 packet must identify final
SHA/tree and full diff, dependency streams, commit rationale and supported
090a/downstream provenance. No DB/state migrations. New profile work is not yet
merged, released, deployed or externally consumed. Preserve already merged and
published history; consolidate only obsolete unmerged iterations.

Risk HIGH because the complete private naming model includes unauthorized DSL
surface while rendered requests must remain authorized, plus mount lifecycle,
public configuration compatibility and mixed-worker rollback. Review all four
lanes: general, architecture/repetition, scope/proportionality, risk/compatibility.
Read mandatory-change-review SKILL.md and each lane reference in full. Retained
reviewer0 is independent, ready/read_only, gpt-6.1-sol/xhigh, thread
01a16406-faaa-7cd0-bde3-c20802c18a72, roster34. No model/effort override or nested
reviewer. Review source directly; no tests/install/builds or other utility state
inspection is assigned.

Key invariants: complete selected version schema captured only after auth,
routes and post-mount hooks; one private model per version/mount; atomic publish
and failed mount rollback; no optional gem without profile; strict legacy and
source validation; copied/frozen data without hidden prose/default/sample leaks;
per-request authorized fields/examples across users/locales; canonical names and
ancestor binding from complete declaration; no request generator/compiler/I/O.
Structural copying must preserve arbitrary Custom/validator payloads while
removing only known structural prose/default/sample positions. Version hints do
not establish actual installed SDK compatibility. Rust lightweight factory must
not relax real generator packaging requirements or change generated/runtime names.

Compatibility: old file profiles remain supported; new minimal profiles require
new server/adapter support. generator_version validates the installed generator,
not a registry selection. Omitted SDK versions remain nil, explicit Cargo
versions retain normal constraints, Git uses validated HTTPS/full40hex source.
Restoring older server code also requires restoring compatible settings. No wire
protocol/state migration or application deployment is intended.

Actual consumer inspection: vpsAdmin cached26518b still uses old HaveAPI0.29.12;
no application adoption is in scope. Go cached SDK1d9240 lacks complete retained
schema/version identity; do not claim it is proven current-compatible. Rust
ff876abe has saved7.0 input and unpublished vpsadmin-client0.1.0, generator090a;
no repin/regeneration/publication is needed or authorized for this feature.
Postreview generated fixture compile/run validates render/generator integration,
not installation of those external SDKs. Architectural provider ownership belongs
to HaveAPI server registry/schema boundary and the two optional generator gems.

Quick owner evidence: server43/0/style7/syntax7; Go62/0/style4/syntax4 and actual
mounted DSL checkerPASS0/2.127s; Rust90/0/style10/syntax10; lead prose
three docs with protected code/links/identifiers preserved. Original setup/check
failures, fixture/sentinel/style corrections and checksum repairs remain in
receipts. Owner executions are not independent reviewer tests. Require exact
final receipts rather than this draft's counts if later source changed.

Changed docs: doc/client-examples.md (authoritative profile contract),
clients/go/docs/documentation.md and clients/rust/docs/documentation.md. Session
rollout/verification details remain in session records. Lead prose receipt is
client-example-profiles-prose-receipt.json. No production KB changes.

Long gates AFTER review: packaged server/docs/HTML, actual Go rendered fixture
compile/run, Rust model generation equivalence baseline4dc0/candidate/repeat,
actual async/blocking/root/mount/development+1.95 render acceptance and final-head
CI. Allow only manifest generator_source_sha256 change in generation comparison.
No full campaign is represented as already run by pure quicks.

User explicitly authorizes subsequent master integration and0.30backport/release
preparation after gates (integration-backport-release-preparation.md). No tag,
registry/publication/PHP mirror/deployment or session lifecycle action is
included. Review does not execute any integration. Record findings and explicit
whole-history/repeated-update/migration conclusions in final review report.

Precommit acceptance integration correction: two legacy-only Go acceptance
fixtures now need actual finalization before reading published profiles. Owner2
authored exactly two finalize(nil) calls in documentation_acceptance.rb and
one actual check_environment! regression in documentation_build_check.rb.
The first preflight stopped before app load due missing selected Git tool.
After exact persistent-root recovery, actual acceptance --check-environment,
mounted DSL checker and two-file syntax/style passed; all six Go hashes matched.
No product publication shortcut is intended. Final packet includes the two
extra paths and their pure checks, making27profile-related paths total.

Additional postreview acceptance gate under design: actual Rust automatic
registration through Server.mount with the real optional Rust gem. Current
shared specs use fake optional modules; the existing Rust rendered runner uses
real factories and frozen Struct profiles. Those are distinct proofs. Accepted matrix is client-example-profiles-rust-mount-brief.md, using a
session-only qualified server/Rust combined bundle and actual Server.mount,
with no product source change. Do not claim real mounted registration has passed yet;
review its interface from source and record the pending runtime gate.

Normal precommit found one NumericPredicate style offense in the equivalence
spec. The actual root configuration requires comparison form; owner3 owns the
one-expression correction, explicit root-config style across all ten Rust paths
and two focused pure units. No commit was made on the failed attempt. Original
component-check result and hook-failure logs remain distinct; no cause for that
discrepancy is asserted without retained command/config evidence. Use the final
overlay hash fb364e7e603bb6c95c5452160a882d161e8ac9ab03e6bcaa6d303f3824a862ba
and quick receipt in owner0's committed packet. Explicit root style10/0 and
focused2/0 passed after the one-expression correction.
