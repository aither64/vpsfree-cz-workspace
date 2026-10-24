# Oversized-test correction: independent final review

20 October 2026. Retained reviewer0 completed general, architecture/repetition,
scope/proportionality and risk/compatibility lanes. No Blocking, Important or
Advisory findings. This records the reviewer report returned to the lead;
reviewer remained read-only.

Identity: exact session current and trusted workspace binding verified; both
DEV_SESSION markers absent. Roster17 reviewer0 bound thread
01a14ae6-d2fe-7b31-9950-3ada7e94023b, ready review-purpose,
gpt-6.1-sol/xhigh/read_only. No overrides, fallback or nested agents.

Reviewed base0081fc01f13236a098380094ddbd00539a9c8dae through
heade32d5382910501b0c8fe80bc6b9e6044e56ead8e,
treea57b700797c2396e148da18b6729cb49b2fc0d21 in vpsadminos-admission.
Clean before/after. Full mandatory skill/references/procedures/AGENTS and
patch-series policy read. Inspected complete final series/final diff and exact
a2-to-e32 delta, current design/user decision and prior review context.

## Behavior and evidence

Executor236-256 restores baseline scheduling: first select any normally fitting
pending test; if none fits and running==0, select first pending test with generic
exhaustion warning. Scheduler mutex reserves the exact TestResources object;
other workers retain normal budget checks and release broadcasts. No request,
limit, CPU, shared-memory accounting or disk changes. Oversized RAM/shm/both/CPU
are attempted without refusal or an impossible-fit wait. User-accepted host
exhaustion/OOM is a residual, not a review finding.

Inspected condition-variable regressions: active reservation prevents fallback,
release wakes worker, oversized request stays unchanged and blocks concurrent
reservation, warning/accounting correct. Existing fitting work, budgets,
prepared-config/retry/no-Nix and cleanup tests remain. Recorded155examples0failures
in1.48s and enabled Nixfmt/RuboCop/commit hooks pass. Reviewer ran no tests/builds
or deliberate OOM; source/recorded evidence and baseline restoration proportionate.

Seven-path correction removes ResourceError/overflow helpers/refusal and claims;
runtime fallback/worker loop equal baseline, prebuild worker-join cleanup retained.
Cache, prep sizing, aggregate contexts, source/roots, canonical allocation-free
validation, exact-config retries, CI option/default, CPU/cores unchanged. Docs/man/
help match behavior. No new knob/skip/retry/sampler/framework. Provider vpsAdminOS
and representative consumer vpsAdminb4ef8535.../pin8e44a512... inspected; no export/
JSON/CLI migration or coordinated running-node update.

## Complete history and provenance

Final shipping series: unchanged5acb08db650a0c72d3b00ab66cbdd9da6b50eb46 cache;
e32d5382910501b0c8fe80bc6b9e6044e56ead8e prebuild with inseparable
resolver/root/validation/CI/docs/tests. Obsolete09fb4131d strict refusal removed,
not retained followed by revert. No obsolete approach, fixup or transitional
implementation. Historical measureda2 remains exact in datedbackup and as parent
of benchmark295b814, preserving reproducibility without shipping rejectedhistory.
No temporary benchmark files in product delta. No repeated dependency/channel/
input/generated streams. No migrations/transitional formats; merge/release/
deployment/external migration provenance empty.

Direct cmp: a2..e32 matches admission-correction-final.diff SHA256
662bea01d9e736991ab4af1013352e2f37332f87808071c9e6a7b0f506e10595;
base..e32 matches product-final-after-admission-correction.diff SHA256
e0dc3e1793f0d88dfaf2d939c1b961e200bcde10e16196644f5e96b81cca33f7.
Diff-check passes. merge-base with staging remains0081, currentstagingf4bac6b49.
Review covers recorded original-base range, not a future rebase. Refresh/checks
needed before later authorized integration. No merge/deploy approval.

Residuals: run-alone may exhaust runner/OOM as accepted.8192MiB/job and2048MiB
cache are heuristics, not totalRSS caps. Full VM/performance evidence belongs to
historicala2, cannot be relabeled fore32 or causal/statistical equivalence. No
full benchmark or deliberateOOM needed for baseline schedulerrestoration.
Reviewer performed no edits/tests/commits/push/build/deploy/lifecycle/nestedagent.
Session remains open.
