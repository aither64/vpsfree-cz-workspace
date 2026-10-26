# Expanded HaveAPI performance review packet

FINAL REVIEW REQUEST. All intended expansion changes are committed; quick
checks pass and the worktree/index are clean. Prior original review/report is
retained separately; it does not complete this expanded final gate.

## Acceptance and boundaries

User explicitly accepted implementation of HaveAPI API execution, ActiveRecord
with SQLite, documentation and GitHub performance checks. Keep the original
context/Rust fixes. Fast relevant push/PR jobs target 5–10 minutes; weekly profile
uses larger fixtures. Meaningful timing and inconclusive slowdown signals block.
No vpsAdmin, external database, production load or deployment scope is included.

Inspect real routing/auth/parser/action/serializer behavior and DB adapter paths,
every response/envelope/state contract, denied-access isolation, source selection
and dependency equivalence. Query improvements cannot skip required authorization.
Neutral harness and fixtures must run both exact implementation roots. No silent
missing scenarios, auto rebaseline, dependency fallback or retry-until-green.

Inspect timing policy: baseline pilot 150 ms and count 1–2,000, two warmups,
3 self pairs + 9 alternating comparison pairs, material threshold max(20% of
baseline, 0.20 ms/request), noise max(self variation, 5% baseline, 0.05 ms), 8/9
agreement and otherwise blocking inconclusive. Weekly uses 5+15 pairs and 14/15.
Allocation gate max(10% baseline, 32 objects/request), calibrated fixed ceilings
with 25%+32 slack, exact SQL ceilings and size-work bounds. Ensure reporter and
CLI exits cannot present harness failures or incomplete data as passing metrics.

Inspect workflow exact event baselines, fixed weekly reference, source ancestry,
fork safety/read-only permissions, no secrets, stable aggregate/change detection,
hard 10/30-minute limits, Sunday 03:00 UTC, official action pins and 30-day
always-retained diagnostic artifacts. Attempt manual rehearsal after review and
publication without changing weekly/default semantics. A new workflow may be
undispatchable until its definition reaches default; retain actual refusal,
verify the identical weekly CLI locally and disclose hosted weekly execution as
unverified. No merge is authorized to enable dispatch.

## Repository and history

Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-24-context-copy-performance-tests/haveapi`.
Feature: `2026-10-24-context-copy-performance-tests`, target `origin/master`.
Original initial base: `39909094649b1d14a23f00615775ca7136acf4fd`.
Fresh read-only `git ls-remote origin refs/heads/master` on2026-10-25 still
returns that exact base; no upstream source refresh is needed on this evidence.
Prior reviewed/published head and fixed accepted reference:
`b85ec364057f536940d689b09e612512ffffaf82`.

Exact final head: `1f8649f3aa2b3ea885e178fbed03d837b850b518`.
Exact tree: `197748d49c75d1b197d58af47fd4277ee77a12de`.
Final diff SHA256: `aed43dc1797098cc12c32b4b958ac1cbc3f32255e759b4e4dd8203cbd357772a`.
Scope31files,5798additions/26deletions. [Final diff](api-performance-final.diff),
[full inventory](api-performance-final-inventory.json),
[history](api-performance-final-history.txt), [stat](api-performance-final-stat.txt).
Exact base/head diff whitespace check passes. Original base is still local
origin/master and fresh remote master; no rebase/source refresh is necessary.

Entire series in order:

1. `5003ded2a47db6b1637a3fef2fdd40474ea7de06` — owned Context sharing and compatibility specs.
2. `82a7f8880663dfa9d8ad6cd67e981a5842dedf9c` — selected authorized Rust normalization and regressions.
3. `de799b595d04e880d092b3e5ef47bce2f4587130` — real-page deterministic work/isolation gates and shared fixture.
4. `b85ec364057f536940d689b09e612512ffffaf82` — opt-in documentation harness and ownership/benchmark docs.
5. `610da4e3212e66fac026eb94eedb55abf6d3c66a` — SQLite scenarios and query/scaling/isolation specs.
6. `4e05ca8dc4f6b938814b354996025b0aad91d9c7` — executable endpoint scenarios and contract/scaling specs.
7. `e98e704e926961bc6d8e4a12ee15c77c1380e7a8` — CI/event resolver/Make commands and performance guide.
8. `1f8649f3aa2b3ea885e178fbed03d837b850b518` — paired runner/comparator, measured budgets and detector controls.

Each unit groups behavior with its owning tests/documentation. The CI unit
consumes the final runner CLI; the final complete tree is the intended deliverable.
No obsolete expansion fixup commits remain. B removed an ineffective logger
experiment before committing a followup; no rebase/consolidation is needed.
No repeated dependency/channel/generated update streams exist. Original b85
lineage is deliberately preserved as the exact supported fixed benchmark
reference consumed by the weekly workflow; do not rewrite it away. The original
opt-in benchmark remains a supported manual diagnostic alongside the new gate.
The reviewer must independently assess these history conclusions.

No migrations: only isolated disposable fixture databases/schema are created.
No application schema, persisted format, protocol or dependency pin changed.
No migration was merged, released, deployed or externally consumed. No merge,
deployment, publication of versions or lifecycle action is authorized. Ordinary
feature branch publication is authorized after review.

## Quick evidence and documentation

- A: 15 focused examples, changed-file lint/doc generation/hooks pass;
  [handoff](phase2-endpoint-handoff.md).
- B: 17 focused examples, measured page/includes/query/allocation contracts,
  lint/hooks pass; [handoff](api-performance-sqlite-handoff.md). Rejected local
  logger experiment is absent from history/final tree; before/after proof retained
  in `api-performance-sqlite-logger-equivalence.json`. C owns runner policy checks.
- D: 22 focused resolver/workflow/subprocess examples, syntax/lint, embedded
  Bash/YAML contracts, docs links, real resolver CLI and isolated dependency
  compatibility pass; [handoff](phase2-package-d.md).
- C: clean shared-worker calibration, 12 quick and 32 weekly cases; bounded
  weekly worker ran once via fresh pinned utility, exit0/42s. Final complete
  `spec/performance` passes70 examples, zero failures, seed50550,35.35s examples;
  six C Ruby files lint clean in `phase2-c-final-quick.log`. Exact final checks
  are70 examples/zero failures,35.56s,seed54353 after the final same-SHA source
  guard; all normal commit hooks pass, `phase2-c-commit.log`. Real CLI replay/live
  faults, ordering/provenance controls, calibrated12/32 inventories and all A/B/D
  consumers are covered.

Selected-count weekly telemetry is retained in
`phase2-c-weekly-selected-stages.json` and its frozen-input/result receipts.
Architect independently accounts40.334s versus40.352s worker total, plus0.031s
serialization; outer command41.682s. Updated repeat model~27.62min before
remaining overhead supports review and a hard30min post-review attempt, while
full local/hosted feasibility remains unproven. The prior35.7min model is
superseded. No workloads, pairs, thresholds or cap were relaxed. See
[C handoff](phase2-c-handoff.md) and accepted clarification in design.md.

Calibration provenance deliberately retains the bytes originally measured.
Weekly calibration briefly included an ineffective fixture subclass-logger
assignment; B's retained before/after equivalence proves identical request
allocation/output/counter behavior after removing it. Subsequent C changes
record runtime/order/provenance/untimed stages and consolidate after-timer JSON
work. Budget counts and request timing boundaries are unchanged. Inspect this
evidence chain rather than expecting historical and final harness hashes to be
identical; arbitrary future drift is not accepted by this rationale.

`doc/performance.md` owns lasting behavior and operator command contracts, linked
from README, `doc/client-examples.md` and development command guidance. Session
calibration/raw input reports retain individual execution evidence. There are no
production migrations, protocol/schema/dependency pin changes or deployment
steps; SQLite creates disposable per-scenario schema. Existing application
runtime fixes remain in scope for complete-branch review.

## Final review policy

Retained reviewer0: independent, saved `gpt-6.1-sol`/`xhigh`, read-only.
Overall high risk due authorization isolation and CI execution of untrusted
branches. General, architecture, scope and risk lanes apply. Read the mandatory
review skill and all selected references, inspect the complete final branch and
give explicit history/repeated-stream/migration conclusions. No automatic early
review assignment; routine planning and this packet are not final deliverables.

After final review, fresh policy utility watchers execute long calibration,
campaign and exact-head workflow verification. Timing positive controls,
allocation/query regressions and detector error/inconclusive cases must prove
nonzero exits. Record observed baseline counts/noise and actual job duration;
never claim unexecuted weekly/PR/default-path verification succeeded.

Review progress at exact1f8649f3: reviewer independently reran70 examples and
reproduced two Important actual replay-CLI gaps (typed numeric raw/canonical
equality and same-SHA evidence acceptance). Both require narrow fixes before
long verification. Full report remains forthcoming; preserve this original
reviewed range/diff and attach narrow-fix successor evidence separately.

Final review report is now retained as
[api-performance-review-report.md](api-performance-review-report.md). Both
Important findings were corrected in successor
`ae60e0fdbc892d248c1cd4bff9a52ee74a0cfc43`, tree
`e83aff21574490a79282f58fc5cbe28bb2d8170b`. Lead directly inspected the
[four-path narrow diff](api-performance-review-remediation.diff) and actual CLI
controls under the review skill's narrow-fix policy; no broader design/contract
change or full-review rerun is needed. [Remediation receipt](api-performance-review-remediation.json)
binds old/new ranges and74 passing examples,seed30410,40.53s, normal hooks/lint.
The owning last commit was amended; first7 commits, exactb85 lineage, budget and
scenario bytes are unchanged. Final complete diff is
[successor diff](api-performance-successor-final.diff), SHA256
`4853f4d911ec16fc4c08205a60273ffcb3b677d298b6755a5c72af8ffcde0887`.
No obsolete/repeated/migration history was introduced. Review gate is satisfied;
long verification remains required and is not implied by this acceptance.

Hosted manual quick on ae60 exposed a separate parent assembly bug: run_samples
returned the original symbol-keyed source proof instead of its already normalized
@sources. No measurements were accepted. The minimal corrected successor is
`7f926021834a64e64d3ec65561cfe07337989d17`, tree
`b6ea955a99919a55b0c115ffe2a4a5da7760a71b`: one return-value line and a direct
run-assembly/replay regression. Lead directly inspected
[integration remediation](api-performance-composition-remediation.json) and its
two-path diff, after75 examples pass and normal lint/hooks. Existing reviewed
JSON boundary/gates/workloads/budgets/timing are unchanged; no new design or
contract requires another review lane. First7/fixedb85 preserved. Current final
diff is [api-performance-current-final.diff](api-performance-current-final.diff),
SHA256 `0b6b0be28083d983702cc593ed0349b255b800e2b0c9de9b7827ef1a15edc840`.
Old reviewed/intermediate reports and failing hosted artifacts remain evidence.
Final-head full/paired/hosted verification is required again as applicable.

Ordinary server CI at7f then exposed test-control input coupling: its component
job prepares only the server bundle, whereas production Worker.inputs requires
root and component locks. Final test-only successor
`38ecca75edaf797d048fb36c6a50ea7e05eb50a9`, tree
`c6cf3c6809ab52b3b2fba57c117139c7bcff6a37`, isolates live controls in a genuine
root-lock-free temporary harness using the actual server manifest/lock. The
production input path remains strict, with an explicit missing-root negative.
Lead inspected [two test paths](api-performance-server-input-remediation.diff)
and76 passing examples/lint/hooks. [Receipt](api-performance-server-input-remediation.json)
binds unchanged production benchmark/fixture/budget/runtime inputs, original
failure and current final diff SHA256
`4fe1fae97def3dcbb7363b4a00e4fd3bff4e30fd775af17c2792dedb1daeb08d`.
No reviewed production boundary or gate policy changes, so direct narrow-fix
inspection suffices. First7/fixedb85 unchanged; all prior evidence preserved.

## Ownership, consumers and compatibility

HaveAPI owns the neutral scenarios, worker/result/CLI contracts and budgets.
Current consumers are server RSpec, Make targets, `utils/performance_ci.rb`, the
new workflow and developer commands. No downstream runtime API/SDK/transport
contract changes. The production Context/Rust source changes in the original
four commits retain their prior compatibility assessment but remain in complete
branch scope. Mixed workers can coexist; rollback requires no data conversion.
No coordinated machine/package update, downstream pin change, release or deploy.

Read project AGENTS.md/development guidance and workspace procedures. Read the
mandatory-change-review skill and all four selected lane references. Please
verify session/current/env/roster/settings, remain read-only, and return full
findings/report through report_to_lead for lead persistence as
`api-performance-review-report.md`; do not write that file yourself. Independently
conclude on complete history, repeated streams, migrations, proportionality,
authorization coverage, detector effectiveness and CI/provenance boundaries.
No nested agents. No long suites/campaigns, dependency installs or hosted
workflow execution during review. Bounded prepared-environment checks allowed.
