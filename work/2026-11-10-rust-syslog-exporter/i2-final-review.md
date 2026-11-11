# I2 affected final independent review

Reviewer: reviewer0, retained gpt-6.1-sol/xhigh/read_only, thread 01a1c742-93c5-7c50-b59e-f792fafd9624.
Risk: high. Affected lanes: general, architecture/repetition, risk/compatibility. Prior scope/proportionality conclusion retained for the same bounded task.
Complete final provider range: 7c5a8e74e44a704cceb99cd05716af6800d78efd..faf06c1185ad2f6d39286d2e33896a6455b7bea6.
Affected implementation comparison: 8ef8241c60f3b99976191b92f0467c945e36b1c8..faf06c1185ad2f6d39286d2e33896a6455b7bea6.

## Findings and disposition

No Blocking, Important or Advisory findings in the affected I2 implementation, tests or documentation.

Affected final review is complete. The source change correctly implements D2's supported two-consumer admission boundary and does not block the lead's release of the prepared consumer pin/build and targeted verification work. It does not certify final-package performance or production readiness, and grants no deployment, dry-activation, integration, claim or lifecycle authority.

Preserve the original independent exporter review of 7c5..9a5, the lead's direct verification of the narrow 8ef fixes, and my C2 review of 3c088a4b71881b3649441ce3c4e92c71757708e6..75b0af0323db1412de457cb73362fd741941eef4. Those reviews remain applicable to their independently established unchanged scope; this report covers the substantive HTTP successor.

## Identity, scope and evidence

Reverified dev-session current from the assigned session directory, the exact trusted workspace/thread binding and the live roster. Both DEV_SESSION identity environment variables are absent. Roster confirms reviewer0, review purpose, ready, saved Sol/xhigh/read_only and the same native thread. Reused the applicable unchanged workspace/repository guidance, mandatory-change-review skill and required general/architecture/risk references already read in full in this context. No exporter-local AGENTS.md is present.

Read the current main/owner I2 packet, D2 brief, observed verification gap, old/new patch and range-diff, equivalence receipt, final HTTP source and all five private tests, affected docs and quick/CI evidence. Inspected the narrowly relevant configured consumer paths at C2 head75b: both int.mon1 and int.mon2 enable independent monitoring and receive the same 60-second log scrape job.

The correction addresses an actual supported consumer, not an optional expansion: 40 paired requests on the old candidate produced 7 HTTP503 responses while all160000 input records counted exactly. The isolated successful60s scrape proved only isolated scheduling. The recorded I2 milestone is approximately23:07 assignment to23:16 acceptance for review, about9 minutes by dispatch records, not an exact active-work measurement. Only3 files changed from8ef, +225/-12, predominantly private concurrency tests. The original task's scope remains unchanged, so another scope-wide review is unnecessary.

## Concurrency, cancellation and failure assessment

src/http.rs:25–38 defines one private production HttpState constructor with shared Arc semaphores: two admission permits and one encoder permit. router constructs this state once (66–71), outside per-connection cloning in serve (79–94). Admission is therefore shared across connections and requests, including HTTP/2 streams; it is not accidentally a per-connection limit.

src/http.rs:40–48 acquires admission without waiting and then asynchronously waits for the single encoder for at most1s. Excess admission receives503 immediately. Timeout or cancelled waiting futures drop their admission and acquisition future, returning capacity; there is no unbounded application waiter queue. At most one encoder and one additional admitted request are retained.

src/http.rs:49–54 moves both owned permits into the blocking closure. Dropping the HTTP future/JoinHandle cannot release either permit while that queued/running encode continues. This preserves the cap under client cancellation instead of accumulating detached blocking jobs. Normal return, encode error and closure unwind release the permits through their owned lifetimes; the existing match maps encoding/join failures to500.

The closure releases permits before the response is converted/written (56–64). A slow body consumer consequently does not reserve admission or encoder capacity. The change introduces no ingestion lock or new registry ownership and leaves response bytes detached as before. The32-connection cap,30s complete connection lifetime, compression, fallback and shutdown transport path are unchanged.

There is no new public hook, configurable scheduler, cache, worker pool, dependency or metric/transport protocol. Separate admission and encoder permits express different necessary limits. The private constructor prevents production/test limits from drifting.

## Regression quality and independent checks

The tests in src/http.rs:118–300 exercise the real metrics handler with the production state constructor and an actual registered collector whose first collect blocks. They do not merely acquire a substitute semaphore.

- two_overlaps_serialize_and_third_is_rejected forces a running encode and admitted waiter before checking the third503. Both admitted responses then contain valid200 exposition; peak concurrent collection remains1. The first response body is deliberately unread until the second response completes, checking pre-body release.
- waiting_encoder_times_out_and_recovers checks the1s timeout,503, admission recovery and a later successful request.
- cancelling_a_waiter_returns_its_admission aborts an actually admitted waiter and checks restored capacity.
- cancelling_a_running_encode_retains_both_permits aborts the HTTP future while the collector is blocked, observes admission1/encoding0, admits one waiter, rejects a third request and verifies full recovery and peak1 after release.
- dropping_the_test_gate_unblocks_failure_cleanup checks the fixture's sole-sender drop path. The same owned sender is dropped on assertion unwind, so the test fixture does not strand a blocking worker while Tokio shuts down.

Independently reran the existing compiled library binary's five http::tests in memory, serially: all5 passed in1.01s. This reused the existing binary and did not rebuild or launch a temporary service; it is not a new release-build identity proof.

Inspected the final scoped commit-hook evidence for formatting/Clippy and the complete19-test suite, and exact-head CI receipt for run42921690945, attempt1, completed success, head faf06c1. I did not independently query live GitHub run metadata. Fresh read-only SSH refs independently confirm feature faf06c1185ad2f6d39286d2e33896a6455b7bea6 and unchanged master7c5a8e74e44a704cceb99cd05716af6800d78efd. Exporter tree/index are clean and full-range git diff --check passes.

The private handler tests establish admission semantics and cancellation ownership. Actual two-consumer network scrapes, final Nix release scheduling and HTTP/2 wire traversal are not independently exercised by those in-memory tests. The unchanged transport/router structure supports the shared-state reasoning; targeted release-binary verification remains necessary.

## Complete history, migrations and verification reuse

Independently inspected the complete base-to-head log, final diff and old-to-new range-diff. The final series contains one amended functional replacement commit, faf06c1185ad2f6d39286d2e33896a6455b7bea6. It introduces the final design directly. No obsolete branch approaches, transition path, fixup chain or intermediate source-pin commits remain in the provider series.

The HTTP correction, relevant regression tests and reference/verification updates belong in the same replacement. Its amended message describes the final two-consumer behavior. Earlier9a5/8ef candidate identities remain review/measurement provenance rather than redundant commits in the final series. Published/local development use does not justify retaining obsolete pin history.

No migrations. The full provider tree has no migration inventory, no persisted application schema/cursor conversion and no intermediate state lineage requiring a transitional commit. The feature candidates are reported never deployed or integrated. No repeated dependency/channel/pin stream exists in this provider series.

Independently derived the changed-path set by comparing complete tracked trees: exactly docs/reference.md, docs/verification.md and src/http.rs. The other31 tracked paths are byte/blob-identical, including parser, input, collectors, metrics, main/config/lib, manifest/lock, profiles/toolchain, driver and existing fixtures/tests. Cargo.lock SHA256 remains031d0b542c8a95a8e0293cd7c62aa3c052b17c29342bbec4d4195feabb78ea1e.

The overall src trees differ: old1362270280553d1978986649adc54e4231c9666e, newf563642a228e19e368b7f3b7ad638ef866f0bc89. The complete artifacts are not equivalent. Preserve old/new bases/heads and the scoped equivalence evidence; do not label old8ef literally merged into this amended successor.

Prior Ruby wire/parser/collector/framing/expiry evidence can be reused only for the proven unchanged behavior and exact applicable inputs. Existing benchmark data still describes8ef's package and measured environment. It does not certify faf06c1's HTTP behavior, complete binary throughput/RSS or final Nix package. The new source must be built and the affected scrape behavior verified on that actual output. Completed unrelated checks should not be repeated solely because this bounded HTTP module changed.

## Documentation placement and preservation

docs/reference.md:71–78 is the correct authoritative home for two-request admission,1s wait,503 boundary, HTTP/2 applicability and cancellation-held permits. Its wording agrees with the implementation, including release before response writes. It preserves the distinction between normal two-consumer operation and declared excess/pathological timeout.

docs/verification.md:7–9 accurately describes the private real-collector concurrency/cancellation checks. It does not claim a production benchmark, complete wire-conformance suite or extra encoder.

The unchanged README still reaches both topic pages. These additions remain useful after this initiative, are owned by the exporter, and contain no temporary branch status or rollout receipt. Existing gzip/fallback, connection, loss, memory/cardinality, reset, single-reader and recovery limitations remain intact. No guide move, obsolete upgrade retirement or recovery instruction loss occurred; no duplicate cross-project contract or new broken link was introduced.

Conclusion: documentation placement, fidelity and preservation are sound. Site cutover/rollback operations remain in the previously reviewed consumer guide; exact old/new source and test results remain in session records.

## Consumer boundary and remaining gates

The CLI, JSON/FIFO/account/port, metric names/labels/timers, manifests/dependency graph and release profile are unchanged. The previously reviewed C2 service/package/check/operations logic remains applicable; an unrelated whole-C2 rereview is not warranted.

C2 must refresh its exact exporter revision/source hash through its owner, verify any reused vendor/build inputs against the unchanged manifests/lock and actual vendoring inputs, consolidate the unmerged source-pin stream and bind the final C2 head to this provider review. Verify that the consumer delta stays mechanical; any additional substantive consumer behavior requires its affected review. Do not treat the old75b/4gb package/host receipt as a build of the successor.

After acceptance and exact consumer preparation, build the Nix package/host as authorized, then use that exact release binary for focused paired/normal-consumer scrapes during ingestion and the relevant scrape/no-scrape performance comparison. Preserve the original collision evidence. More than two concurrent handlers or an encode exceeding the defined wait may legitimately yield503; the acceptance fixture must distinguish that explicit overload from the two normal monitors.

Previously unfulfilled transport/size/short-write/restart/backlog gates remain outstanding; do not duplicate completed unchanged-scope evidence without a changed input or unresolved concern. The existing observed-loss and no-persistence/cardinality limits remain, and no capacity or production-losslessness claim is justified by these source tests.

User authorization still stops before deployment. No dry activation, production copy/probe, default merge, machine/merge claim, review-file write, application edit, nested agent, build, long test, cleanup or lifecycle action was performed by this reviewer. Lead will persist this report and record disposition; implementer0 owns any later I2 findings.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-10-rust-syslog-exporter/
