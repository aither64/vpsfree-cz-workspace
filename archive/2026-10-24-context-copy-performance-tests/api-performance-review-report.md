FINAL INDEPENDENT WHOLE-BRANCH REVIEW — expanded API performance deliverable

Please persist this report verbatim/attributed as work/2026-10-24-context-copy-performance-tests/api-performance-review-report.md. I remained read-only and did not write that report file.

Findings, ordered by severity

1. Important — raw/canonical validation permits a numeric type contradiction and a false passing replay. General and risk lanes. servers/ruby/benchmarks/performance_compare.rb:196, introduced by 1f8649f3aa2b3ea885e178fbed03d837b850b518.

validate_sample compares the parsed raw JSON tree with the canonical tree using Ruby ==. Ruby considers Integer 0 and Float 0.0 equal, including inside Hash/Array equality. The preceding canonical digest check only authenticates the supplied canonical tree; it does not derive that digest from the raw body. Consequently a candidate raw response can change from zero:0 to zero:0.0 while its canonical representation still advertises the original integer, and comparison accepts it.

Bounded reproduction through the actual endpoints.rb compare CLI: start with PerformanceSamples.fixture, modify every comparison candidate's raw body from "zero":0 to "zero":0.0, update that body's valid SHA-256 and byte count and the corresponding output raw metadata, but retain its integer canonical_body/canonical_sha256. The command returned exit 0 and report status pass, despite the contradictory numeric types. Baseline raw bodies remained integer-valued. This is a replay/input-integrity defect, not evidence of an authorization bypass or of current live workers producing bad canonical data. It violates the explicit typed raw/canonical contract and can hide a raw type change behind retained canonical metadata.

Requested correction: compare the typed canonical digest/serialization derived from parsing the raw body against the recorded canonical identity, rather than Ruby's coercive tree equality. Keep duplicate-key rejection, all values, types and array order. Add a focused actual compare CLI regression requiring exit 3 for nested Integer/Float contradictions while map-order-only variation remains accepted. This validation is outside timing; no gate threshold or workload expansion is needed.

2. Important — replay comparison omits source-policy guards enforced by live runs. General and risk lanes. servers/ruby/benchmarks/performance_compare.rb:96-127; contrast servers/ruby/benchmarks/endpoints.rb:405-417, introduced by 1f8649f3aa2b3ea885e178fbed03d837b850b518.

Comparator.validate_header checks SHA syntax/source-field agreement but never requires baseline_sha != candidate_sha. The compare CLI bypasses run_samples, where the distinct-source and fixed-weekly-baseline guards currently live. A replay can therefore issue a successful regression report for a same-revision comparison. The weekly replay header likewise lacks the fixed-reference source check, although the run/resolver path enforces it.

Bounded actual compare CLI reproduction: take the complete controlled passing samples, change baseline_sha and its baseline source/observation SHA fields to the existing candidate SHA, leaving all other complete evidence consistent. The command returned exit 0/status pass with identical baseline and candidate SHAs. This contradicts the documented refusal of equal comparisons and means replay does not enforce the same source policy as run. The current run-path same-SHA spec does not exercise this path.

Requested correction: enforce the pure source-policy invariants in the shared comparison-header boundary as well: distinct source SHAs, and REFERENCE as baseline for a weekly report. Add actual compare CLI exit-3 cases for both invalid headers; retain valid quick ancestor-pair and fixed-reference weekly behavior. Offline replay need not acquire a new Git/environment dependency merely to enforce these available header facts.

No Blocking findings or additional Advisory findings were identified. Important findings require fixes or an explicit recorded decision before proceeding under the mandatory review workflow. I have not approved the expanded branch as ready. Both requested corrections are narrow validation fixes; focused direct remediation inspection and CLI tests can satisfy the narrow-fix policy unless their implementation changes the design or contract further.

Reviewer and exact scope

Retained reviewer0, thread 01a16fb2-e46d-7710-ab37-0ab731b8befe; model gpt-6.1-sol, reasoning effort xhigh. dev-session current and both DEV_SESSION_SLUG/DEV_SESSION_WORKSPACE matched 2026-10-24-context-copy-performance-tests and /home/aither/workspace/ai/vpsfree.cz. The live same-session roster confirmed ready, purpose review, access read_only, and the saved settings. No override, fallback, substantive authorship or nested agents. High overall risk due authorization/isolation and execution of untrusted CI branches. Read the mandatory review skill and all four selected lanes; performed general, architecture/repetition, scope/proportionality, and risk/compatibility review directly.

Repository/worktree: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-24-context-copy-performance-tests/haveapi. Target origin/master.
Reviewed complete base: 39909094649b1d14a23f00615775ca7136acf4fd.
Reviewed complete head: 1f8649f3aa2b3ea885e178fbed03d837b850b518.
Reviewed tree: 197748d49c75d1b197d58af47fd4277ee77a12de.
Final diff: 31 files, 5,798 additions/26 deletions. Packet api-performance-final.diff is byte-identical to a fresh exact-range git diff; SHA-256 aed43dc1797098cc12c32b4b958ac1cbc3f32255e759b4e4dd8203cbd357772a. Worktree/index clean at start and finish. Local origin/master and independent read-only git ls-remote origin refs/heads/master both returned exact base. Fixed b85ec364 ancestry was verified. No fetch/rebase/push/merge/deployment/workflow dispatch/install/lifecycle operation was performed.

Complete history and migration conclusions

All eight commits, messages, per-commit paths and final combined tree were assessed:

- 5003ded2a47db6b1637a3fef2fdd40474ea7de06 — Context sharing and ownership/subclass compatibility tests.
- 82a7f8880663dfa9d8ad6cd67e981a5842dedf9c — authorized Rust subtree normalization and behavior/work tests.
- de799b595d04e880d092b3e5ef47bce2f4587130 — deterministic page/allocation/isolation gates and shared fixture.
- b85ec364057f536940d689b09e612512ffffaf82 — original opt-in documentation benchmark and supporting docs.
- 610da4e3212e66fac026eb94eedb55abf6d3c66a — isolated SQLite/query/scaling/isolation scenarios and specs.
- 4e05ca8dc4f6b938814b354996025b0aad91d9c7 — executable endpoint scenarios and contract/scaling specs.
- e98e704e926961bc6d8e4a12ee15c77c1380e7a8 — CI/event resolution, Make commands and performance guide.
- 1f8649f3aa2b3ea885e178fbed03d837b850b518 — paired runner/comparator, calibrated budgets and detector tests.

No obsolete branch approach, redundant expansion fixup, unused transitional runtime path or superseded dependency update remains in this series. The original opt-in diagnostic remains supported alongside the paired gate. Preserving the original b85ec364 lineage is justified by its concrete new consumer: the exact accepted reference selected and required by weekly policy and budgets. This is a supported reference boundary, rather than publication alone being used to excuse obsolete history. The four expansion units have coherent ownership; they are integrated through the shared final runner/identity contract.

There are no repeated dependency/channel/input/generated-update streams to consolidate. No dependency pins or library locks are committed. Migration conclusion: no migrations. Fixture create_table calls operate only on each scenario's disposable in-memory database; they introduce no production schema, seed, persisted-format or supported upgrade transition. No intermediate migration was merged/released/deployed/externally consumed.

Architecture, correctness, scope and security assessment

- Production runtime changes remain exactly the original Context/Rust fixes: the expansion diff adds no servers/ruby/lib or clients/rust/lib changes. The original ownership/subclass path and current-help authorization selection remain in complete-branch scope and are compatible with the new fixtures/consumers. No cache or shared authorized response state was added.
- The neutral fixtures load HaveAPI only after source selection. The runner uses separate processes per revision/sample, checks representative Server/Action/AR adapter/Ruby client/weekly Rust source locations and all loaded runtime hashes, and verifies tracked source blobs against exact Git objects. Dependency manifests, common resolved locks, actual loaded third-party gems and Ruby ABI/executable are compared. The two findings concern replay validation; the live run also performs stronger source/ancestry checks.
- Endpoint scenarios use real Rack routing, Basic/token providers, authorization, typed parsing/validation, nested paths and serialization. Timed invalid input requires the real HTTP-200/status:false envelope with no execution. Direct app specs cover malformed JSON, missing/bad credentials, denial, missing routes, CRUD/reset, omitted/null/zero/false/empty/nested values and admin/member/admin isolation. Counter records are preallocated and direct untimed app requests do not alter them.
- SQLite scenarios own named abstract bases, in-memory pools, model/resource namespaces and SQL subscriptions; close affects only their resources. They use the real adapter with uncached queries and explicit include paths. Fixed pages remain 32 rows, including over 10,000-row tables; 1,024-row serialization is unpaginated. Required per-row authorization remains counted, including denied member associations; associated Show execution is rejected. No runtime workaround for the pre-existing default-includes reflection issue was introduced.
- The worker keeps response slots/reset/GC, fixtures, schema/seeding, response validation, canonicalization/hashing and counter inspection outside the timed request loop, retaining GC triggered by measured work. Two warmups and selected 1..2,000 counts are preserved. Runtime/locale/timezone/JIT policy is explicit before loading dependencies. Every response and per-operation counter is validated; actual query/output faults exercise worker failure.
- Timing arithmetic matches the accepted max(20%, 0.20 ms) material threshold and max(AA variation, 5% baseline, 0.05 ms) noise rule. Wall and CPU classify independently; 8/9 and 14/15 agreement and blocking inconclusive behavior are implemented. Allocation growth and calibrated ceiling formulas match policy, and required SQL/authorization/execution counts are exact. Workload inventory checks prevent silent omitted/extra cases. No automatic retry, rebaseline or budget increase exists.
- The workflow uses ordinary pull_request, exact head/event SHAs, merge-base selection for whole feature branches, before/after for default pushes, explicit manual selection and fixed weekly ancestry. It has contents:read, disabled persisted credentials, hosted ephemeral runners, no secrets/release context/comments or pull_request_target, pinned official actions, Sunday 03:00 UTC, hard 10/30-minute limits, always-attempted 30-day evidence upload and a stable aggregate that rejects failure/cancellation/skipped work/missing outcomes. No unsafe event interpolation was found. Actual fork/hosted execution remains to be observed.
- The added runner is proportionate to the user-approved paired timing/error/source requirements. Fixture/worker/comparator/CI responsibilities are separate, with a shared owning identity helper and scenario interface. Repeated explicit counter expectations serve different fixture validation and calibrated-budget boundaries; no newly duplicated authorization policy requiring another abstraction was identified. The original manual harness remains a distinct supported diagnostic, not obsolete code.
- doc/performance.md owns current behavior/commands and is linked from README, development guidance and documentation benchmark guidance. Generated server copy is correctly ignored. Permanent docs distinguish synthetic SQLite/Rack results from production latency and retain no individual rollout checklist. No production deployment, runtime API/wire contract, state-format or coordinated machine update is introduced; package rollback needs no conversion. Documentation's strict replay/source claims need the two findings reconciled.

Independent bounded checks and calibration audit

- Prepared Nix environment, with HAVEAPI_RELEASE_TOOLS_ONLY=1 suppressing dependency installation only: cd servers/ruby && bundle exec rspec spec/performance — 70 examples, 0 failures, seed 30410, 36.95 seconds examples plus 1.39 seconds load. Expected error-control JSON appeared as part of passing tests.
- git diff --check on the complete exact base/head range passed.
- Actual standalone compare CLI reproductions for both findings each returned exit 0/status pass. They used only controlled sample data in temporary test directories; no application/source/index/report-file edits were made.
- Independently recomputed the two raw calibration hashes against performance_budgets.json: quick d31d9261848936f86dae2f7aa1ec785023c8ea7006b334cc27149306c316ad82 and weekly 175b5703eb8fc536500da36ee826e715897ce093a4e552ecff547d8e35d2fb34. For every one of the 12 quick/32 weekly entries, exact case/dimension keys, measured reference allocations, recorded counters, ceil(1.25*reference)+32 ceilings and calibrated environment matched the retained raw measurement.
- Reviewed the calibration provenance explanation and logger-equivalence evidence. The temporary ineffective subclass logger assignment is absent from final source/history; paired local evidence shows identical request allocations/output/counters under the worker's pre-load test policy. Later telemetry/order/provenance/after-timer transformation changes do not change request timing boundaries. This is a bounded explanation for these recorded revisions, not blanket acceptance of future fixture drift.
- Reviewed selected-count weekly evidence: 32 cases/1,443 operations per batch, two warmups, fixed test/locale/timezone/JIT policy, worker total 40.352 s, serialization about 0.031 s. It is a calibration, not the paired profile or a hosted job result. The roughly 27.6-minute extrapolation leaves little reserve within 30 minutes and omits remaining parent/setup/artifact overhead.

Residual gates and limits

Full paired quick/weekly campaigns, real AA/noise acceptance, end-to-end hard-limit feasibility and exact published-head hosted verification remain unexecuted for this expansion. They are required after findings are resolved/decided and final quick checks are bound to the successor. Do not relax workloads, pair counts, thresholds, environment checks or timeouts to obtain a pass. Retain actual dispatcher refusal if the newly added workflow cannot dispatch before default integration; local weekly CLI success would still leave hosted weekly execution unverified. This review grants no integration approval to enable it.

The original full suites/CI/benchmarks at b85ec364 are useful retained evidence, but do not validate all expanded final-head interactions. Run appropriate post-review full server/documentation/Rust verification through the assigned policy watcher. Cross-version and final CI effects are not inferred from local Ruby 3.4.11 checks. Synthetic workloads establish no production DB/network/vpsAdmin latency result. Explicitly supplied large-resource copying and Rust ancestor/IR scans retain their documented costs.

Next action: assign the two narrow replay validations to the owning implementer; inspect focused CLI exit-3 controls and bind the final successor range/evidence. Then proceed with accepted monitored long verification after fixes or explicit recorded decisions. No automatic full-review rerun is requested for straightforward corrections to these rejected acceptance paths.

Session remains open: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-context-copy-performance-tests/
