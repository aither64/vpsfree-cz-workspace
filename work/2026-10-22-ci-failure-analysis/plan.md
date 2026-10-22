# 2026-10-22-ci-failure-analysis

## Goal

# New session: CI failure root causes and test usefulness

The user explicitly requests a new workspace session with a Full team of FOUR
implementers to investigate the failures below, determine root causes and
suggest solutions. The user adds: evaluate whether these tests are useful and
explain what they are for. Use installed `delegated_4`, retaining its lead,
architect, four implementers and independent reviewer settings. This is a new
initiative, separate from 2026-10-20-kernel-check.

Verify your own new session identity/environment before writing owned records.
Read workspace procedures, repository AGENTS.md and applicable skills. Write a
substantive initial plan/state and commit under workspace rules before project
code/external mutations. The architect must write the investigation design and
assign four independent lanes through the new session's verified roster. Use
your own records/worktrees; never edit the source session's records/branches or
take over its CI watcher. Source-session artifacts listed below are explicitly
authorized READ-ONLY handoff evidence for this investigation.

Goal: give evidence-supported causes, recurrence history, test-purpose analysis
and concrete solution proposals. Do not simply label recurring failures flaky
or harmless. Distinguish a product defect, stale/wrong assertion, environmental
or predecessor-image defect, and missing evidence. Explain for each test the
user-visible behavior/invariant protected, why that matters, whether the test
actually measures it, cost/noise/coverage, and a justified keep/revise/remove
recommendation. Include smallest useful diagnostics and regression acceptance.
No implementation of fixes, workflow reruns, production operations, merges,
deployment, pin changes or session lifecycle actions are authorized by this
investigation-only request. Read-only historical GitHub metadata/log/artifact
retrieval and source inspection are authorized. Avoid blind reruns. If a longer
disposable diagnostic is necessary, propose its exact scope before execution.

Source context: vpsadminos feature 846bb469505789ba0b2a405fa5905ba6d8253006 on
base55c5046514d06fe9398a022c1622bdaae5228841, unchanged panic owner852826 then
generic sysctl service. All-four-lane final review accepted, focused VM8/8 exit0
and CI system/sysctl passed. Current CI39767770407 remains red/nonterminal and
belongs ONLY to the existing source-session watcher. The user explicitly waived
the currently observed failures as blockers to that feature's staging merge;
do not change that branch, merge it here, cancel its CI or claim CI is green.
Original lead/implementer2 owns integration and current600s observation.

Evidence root (read-only):
/home/aither/workspace/ai/vpsfree.cz/work/2026-10-20-kernel-check/

Read first:
- generic-sysctl-ci-failure.md: exact current run/jobs/errors/causal limits.
- generic-sysctl-ci-nested-podman.md: predecessor DHCP/seccomp evidence.
- design.md#separate-failure-investigation-handoff and
  #current-product-ci-causal-boundary and #amd-livepatch-hotplug-warning-boundary.
- synthesis.md; generic-sysctl-focused-vm-846bb4695-receipt.json.
- os-hardlockup-ci-failure-analysis.md and os-hardlockup-ci-new-result.json,
  os-hardlockup-ci-new-jobs.log, os-hardlockup-ci-native-logs.zip/extract:
  historical b81c43ff6865a033268072f55cd94ad763d0630b run39600028637.

Suggested four independent packages (architect may refine boundaries):
1. Five upgrade guest impermanence boot_dataset mismatches: expected retained
   tank/ct/niximpermanent.impermanence-<suffix>, got tank/ct/niximpermanent.
   Current tests from-6.12-guests, from-6.12-guests-v1,
   from-6.12-inherited-guests, from-6.18-guests, from-6.18-guests-v1.
   Containers keep init PID/running state across successful userspace switch.
   Same five signatures occur before generic service in b81c CI; actual
   pre/post run-conf bytes and mounted source were not uploaded. Prior
   occurrence does not exclude current generic contribution or prove data loss.
   Investigate runtime loader/export and test's intended retained-state contract.
2. upgrade/from-6.18-nested-podman: first error before feature activation, on
   predecessor3cb830/kernel6.18.49. dhcpcd10.1.0 ps_managersandbox seccomp
   Permission denied, ifup/networking fail, noIPv4/default route;126 failed
   readiness probes,900s timeout. Exact denied syscall/filter/introducer unknown.
   Explain workload purpose and correct networking/readiness assertions.
3. kernel/livepatch-qualification@amd-scale-aged-v6: CPU127 offline warns
   Dying CPU not properly vacated! / sched_cpu_dying core8332; dump2total names
   only migration127. nr_running!=1 OR nr_pinned invariant. Kernel6.12.95.6,
   current feature OS. Warning before incomingv7 corrected.ko insmod, not
   hardlockup/panic. Offline returns0 despite warning; later activation succeeds
   in757.998s and secondhotplug succeeds, final no-fault assertion correctly
   detects retained warning. Extra task/pinned state/callback owner unresolved.
   Generic service/stress actual sysctl values absent; don't exclude by silence.
4. Historical recurrence and independent cross-test utility review: compare
   exact signatures against prior completed runs/staging and feature heads,
   include passing/executed and unexecuted/cancelled/prebuild categories. Begin
   with10–15 relevant recent runs per lane; report sample/artifact limits, avoid
   duplicate downloads with owners. Assess useful invariant vs brittle/noisy
   setup and recommend retain/improve/remove with rationale, not greenCI gaming.

Current preserved artifacts under evidence root:
generic-sysctl-ci-39767770407-600s-failure-119793311317/artifacts/
os-test-logs-39767770407-1-native/ (product124pass6fail,130tests338scripts).
generic-sysctl-ci-39767770407-600s-failure-119793311395/artifacts/ (AMD warning).
Source feature worktree is read-only reference; create your own worktree if needed.
Canonical repos/<project>.git may be read; serialize any future authorized Git.

Deliver concise explanations understandable to a user who does not know these
tests, an exact recurrence table with run links and evidence strength, source
causal chains/remaining uncertainties, and prioritized solution suggestions.
Keep this new session open and autonomous within investigation scope.

## Affected repositories

- vpsadminos: read-only source and historical GitHub Actions evidence at exact
  feature/base/predecessor revisions. Linux scheduler source is reference only.
- Workspace: this session's coordination records and investigation findings only.
  No project branch or worktree is needed initially.

## Approach and acceptance

The retained delegated_4 architect owns the investigation design and four lane
briefs before substantive work. Four implementers independently investigate
impermanent guest upgrade state, predecessor nested Podman networking, AMD CPU
hotplug/livepatch warning, and historical recurrence with cross-test usefulness.
The lead coordinates dependencies, evidence acceptance and user explanation.

Each lane must distinguish observed first error, source-backed mechanism,
inference and unknowns; classify product/assertion/environment/predecessor
causes without forcing a conclusion. Explain the user-visible invariant, actual
coverage, cost/noise and justified keep/revise/remove recommendation. Propose
smallest discriminating diagnostics and concrete regression acceptance.

History starts with 10–15 relevant recent runs per lane and includes exact
head/attempt/job/test, executed pass/fail, unexecuted/cancelled/prebuild and
artifact limits. A workflow conclusion alone does not establish a test result.
The history owner coordinates downloads to avoid duplication. Deliver linked
lane findings, exact recurrence table and concise prioritized synthesis under
this tracking directory for maintainers and a user unfamiliar with these tests.

## Decisions and boundaries

Investigation only: source inspection and read-only GitHub metadata/log/artifact
retrieval are authorized. No fixes, reruns, production operations, merge,
deployment, pins, lifecycle actions or takeover of the source watcher. Longer
disposable diagnostics require proposing exact scope before execution.

Source-session evidence is read-only under work/2026-10-20-kernel-check. Its
feature 846bb469505789ba0b2a405fa5905ba6d8253006 and CI 39767770407 remain owned
there. The failure waiver does not establish green CI or causal exclusion.
No repository-wide cleanup, reset, stash or branch changes.

## Compatibility and deployment

No runtime or persistent state changes are planned. Proposals must discuss
retained running-container state, old/new daemon and predecessor-image behavior,
rollback, and frozen-kernel/livepatch boundaries as relevant. No coordinated
machine updates, schema migration, deployment or recovery operation is selected.

## Documentation

Session design.md, per-lane findings, recurrence evidence and synthesis are the
appropriate homes for this investigation. No product documentation change is
planned before proposals are accepted. Keep state current; leave session open.
Routine investigation/findings/evidence do not trigger automatic final review.
The retained reviewer remains available without an automatic assignment.

## Verification plan

Read required workspace procedures, exact-revision repository AGENTS.md and
relevant subsystem docs. Cross-check citations, timestamps, first-error ordering,
source chains, run coverage categories and evidence strength. No test or build
runs are selected. Any necessary longer diagnostic must first be scoped for the
user; any later authorized long verification uses the monitor skill.
