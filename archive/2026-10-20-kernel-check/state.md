---
lifecycle: archived
---

# Node24 kernel hang investigation

I2 terminal ownership receipt, 2026-10-23: original CI39767770407 on exact
846bb completed with failure at01:14:16Z, captured01:14:27Z. All11 jobs are
terminal:8success/3failure (product suite, aged-v6, aged-v5). Final amd-fresh
and amd passed. Wall14h10m20s includes allocation waits. Focused VM8/8 exit0
and accepted-exception staging integration remain complete. The later v5
RCU-stall failure was separately reported, not covered by the earlier waiver.
Full metadata/logs/native artifacts and all six product names are linked in
generic-sysctl-ci-failure.md and generic-sysctl-verification.md. Watch exit1,
watcher CLI/tool exit0; generic-sysctl-ci-39767770407-no-active-observer.json
confirms no active matching observer at01:16:30Z. I2 monitoring is complete;
no further assigned operation remains. Separate investigation retains cause/
test-value work. Branches, worktrees and this session stay retained/open; no
retry, cancellation, source/Git change or lifecycle action followed.

## Preterminal status and investigation checkpoints (retained)

Current phase: vpsadminos integration COMPLETE with explicitly accepted CI
failures; root-cause/test-value investigation started in a new session.
DISTINCT later failure: current846bb run39767770407 aged-v5 job119793311416
failed Run livepatch lifecycle tests/Evaluate test results. Overall nonterminal,
twoAMD jobs unfinished. Evidence preserved by same observer under
generic-sysctl-ci-39767770407-600s-detail-failure-119793311416/artifacts/.
This is NOT within premerge accepted-failure waiver; merge already completed.
I2 is assigned bounded local first-error/result/time extraction only, with
deeper cause investigation belonging new CI-failure session. No retry/cancel/
new observer/source edits/revert selected; same600s watcher retains remainingCI.
First evidence captured20:44:01–13Z, artifactdownload0, joblogAPI1/unavailable
untiloverallterminal. First assertion20:35:17Z after16629.89s example is final
dmesg nofault pattern. Exact CORRECTED signature: test-runner.log138
14822.947301 rcu_preempt self-detected stall, line189 expedited stalls CPU114,
kernel6.12.95.5/Comm insmod. It is RCU STALL, not agedv6 sched_cpu_dying WARNING;
earlier genericWARNING label was corrected. Lead directly read saved excerpt.
No causalclassification/featurelink/repair inferred; evidence retained for
separate investigation, no claim of delivery beyond original artifact record.
User asks why currentCI duration is so long and whether a serious regression.
I2 owns fresh current scheduled-watch status/step/start/queue-vs-runtime/progress;
architect owns compact time-budget investigation brief/synthesis, with proposed
i0 historical comparable job-duration sample and i1 workflow/runner limits and
workload graph source. Read-only diagnosis only; no duplicate current observer,
new jobs/tests/retries/cancel/source edits. Separate failure-rootcause session
retains original failures, no duplicate audit. Need explain observed bottleneck
and comparison evidence, not equate totalworkflow age with active execution.
Exact current duration receipt20:32:57Z via SAME observer: run created/started
11:03:56Z, wall9h29m01s, attempt1. API overallqueued/conclusionnull despite
partialexecution; job states authoritative. Only aged-v5 job119793311416 active,
gh-runner4.int.vpsadminos.org/id11199,amd-livepatch label; jobstart15:54:58Z,
elapsed4h37m59s, teststep15:55:02Z elapsed4h37m55s. amd-fresh119793311399 and
amd119793311543 trulyQUEUED,runner_id0/no steps,created11:18:07Z→9h14m50s queue.
Their started_at equalscreated placeholder, not execution. Latest inner progress
unknown; active step alone notproofhung. Raw -duration-run.json/-jobs.json saved.
Historical interim from i0 last15 completed ci.yml: b81c39600028637 agedv6
success4h48m58/agedv5success4h44m25; earlier feature39413777406 sameAMD runner
agedv5success4h45m12/v6success4h42m14. Currentfailedv6~4h24 notnovelduration.
Cancelled rows with no runner/steps near24h excluded from runtime sample.
Final sourcebudget and comparable sample interpretation pending.
Historical duration lane COMPLETE: ci-duration-history.md and normalizedJSON,
15completedpush runs (threefocuseddispatch discovery entries excluded),72AMD
job records:20success,3runtimefail,3runtimecancel,46unassigned/no-stepcancel.
Strong comparable source-matched workload/workflow/runner (OS/pins differ):
v5successfuln2 job4:44:25–4:45:12 median4:44:48.5;v6n2 job4:42:14–4:48:58
median4:45:36. Current snapshotv5step4:37:55 belowhistorical4:44:12–4:44:59.
Historical metadata/read coverage retained, no current API by i0; three small
joblogs distinguish actual qualificationruntime from discovery/prebuild/earlyfail.
No execution-duration regression demonstrated; unfinished innerprogress unknown.
Duration source lane COMPLETE: ci-duration-source.md and source-comparisonJSON.
Five-head comparison shows128vCPU/16GiB/100000tasks and14400sminimumage unchanged;
b81c/49636 exact workflow/qualification/helper/fixture/bootbase/runner/osvm match
current, while OS/pins differ. Aging actively probes every60s+probe time,
not blind sleep. Attempts default1; no hidden whole-test retry. SixAMD/threeIntel
jobs needbuildonly,failfastfalse,no maxparallel; observed serialization does not
prove onlyoneeligibleAMDhost. Outerjob360min/teststep350min include fixture builds/
prebuild; no YAML aggregatequeuecap. Source budgets unchanged, not a new loop/
scale increase. Exact current9h29m01 accounting=55sbuildallocation+796sbuild+
16611sagedv5allocationwait+16679sactivejob. Individual command/deadline limits
are not an additive globalmaximum. Projected21:45:02Z/21:54:58Z cutoffs refer
to fixed20:32:57Z snapshot, not a later status observation. No new tests or
source changes; remaining action is existing watcher terminal follow-up.
Source/history reconciliation: currentsame-runner sequence agedv6 11:18:09–
15:42:18Z, lowmemv5 15:42:20–15:48:38Z, lowmemv6 15:48:40–15:54:57Z, then
agedv5 15:54:58Z. Agedtest deliberately includes4h aging, unchanged from b81c
and49636 workflow/qualification/runner code (OS/pins differ). Teststep350min
deadline21:45:02Z,job360min deadline21:54:58Z, no innerprogress/hang proof.
Historical b81c39600028637 overall12h41m30s, sixAMD assigned job durations sum
11h56m21s (correction to earlier interim~12h12 statement), build14m40 plus
postbuild wait30m18; sixAMD lanes serial on same runner. Allnine livepatch jobs
passed. Current~4h38 agedv5 still below prior successful same-runner durations.
Evidence supports existing4h workload+AMD runner serialization/queue bottleneck,
not demonstrated new sysctl runtime regression; currentlane remainsunfinished.
Module-autoload compatibility investigation complete, no product edit/new test
execution: design.md#module-autoload-compatibility-finding and
module-autoload-test-coverage.md. Ordinary policy is preserved: disabled/logged
activation and generated60/service replay use the same deny wrapper; disabled/
silent uses empty helper; enabled/logged uses load wrapper; enabled/silent uses
upstream plain kmod activation with no OS sysctl key. No default regression or
runtime fix found. Existing CI16/16 real-trigger autoload tests and8/8 sysctl
cases pass, but no explicit completed-service replay/restart + autoload probe,
policy-changing switch or silent-mode interaction coverage. Proposed smallest
extension is one existing dummy trigger after fresh completion/restart and a
four-mode switch/test roundtrip, with narrow override/null/precedence checks.
Activation always rewrites modprobe even if unchanged inputs skip replay;
manual-value retention for generic sysctl does not apply unconditionally here.
Explicit stronger/later-file conflicting values can override policy; null omits
replay but not activation. First-introduction replay is asynchronous. Initrd and
explicit host module loads are separate. No source/test/eval/build/host changes.
I2 confirmed ONLY originalCI39767770407 terminal accounting remains: snapshot
20:08:32Z sixpassed/twoknownfailed/threeunfinished, sole600s watcher PID3401090,
no active code/Git/merge/modprobe investigation/cleanup from that member.
Merged staging55c5046514d06fe9398a022c1622bdaae5228841→
846bb469505789ba0b2a405fa5905ba6d8253006, exact reviewed tree
df9bd828d843225df749b7a05ed9529bf17425c9. Ordinary ff-only merge/Overcommit
hooks and non-force SSH push succeeded. Independent remote proof17:19:40Z has
feature and staging both846bb. Claim8c19bca8-754b-4b6c-9400-78ab645943f0 held
17:18:38Z–17:19:57Z, released before records/CI; lead independently read logs,
refs and authoritative released claim-status. See generic-sysctl-merge-command.log,
generic-sysctl-merge-push.log and [integration receipt](generic-sysctl-integration.md).
Lead inspected the final receipt; both checkouts remain clean exact846bb.
Original39767770407 remains sole600s watcher-owned. No observer/query was added
for a possible automatic staging-push run, and no result is claimed for it.
Branches/worktrees
retained, no deploy/pin/runtime/lifecycle/cleanup. Existing600s watcher continues
run39767770407 through terminal; distinct failures still reported. Session stays
active/open while it owns this remaining CI, not archived or stopped.
User now directs: "let's not consider them blockers for merging of our changes"
and requests a new workspace session with4implementers to find root causes and
suggest solutions; additionally evaluate whether the tests are useful/what for.
This supersedes the earlier CI-success condition for the observed product six
failures and AMD-scale-aged-v6 warning only. CI remains red, not certified
harmless or unrelated. Distinct new failures remain reportable. Merge approval
covers vpsadminos→staging; no deployment/pins/configuration merge/lifecycle.
Lead inspected17:15:38Z fresh refs55c504/846bb, exact unchanged reviewed two-owner
series/final six-file +399/-1 diff and accepted-exception packet. Target checkout
clean/hooks ready, no migrations/streams. Lead final freshness gate accepted;
i2 completed the short repository-claim merge/push/proof/release above.
New session CREATED through public dev-session start with delegated_4:
2026-10-22-ci-failure-analysis, root thread01a1649d-ed97-7f91-b191-678781cacd36,
goal ci-failure-investigation-goal.md (rootcause,recurrence,testutility/proposals).
Verified installed roster: architect0 Astra/xhigh, FOUR ready implementers0–3
Sol/xhigh/workspace_write and reviewer0 Sol/xhigh/read_only. New portal:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-ci-failure-analysis/
The new goal explicitly assesses protected invariants, assertion validity,
cost/noise/coverage and keep/revise/remove recommendations for failing tests.
Original session/team/watch remain owned and open; no investigation duplication.

## Earlier CI failure analysis (accepted merge exceptions, still valid evidence)
User asks whether these failures recur and to check previous results. Architect
owns bounded historical comparison brief/synthesis; proposed independent lanes
are i0 product-suite signatures and i1 AMD hotplug signature. Compare previous
completed runs with exact test/errors, passing and unexecuted evidence, date/head
and artifact availability. Initial bound10–15 relevant recent runs per lane;
no new workflows/tests/reruns/source changes. I2 retains sole current600s watcher,
no duplicate current polling. Recurrence is distinct from harmlessness/causality;
merge remains blocked pending evidence and successful CI.
Second failed job reported by the same600s watcher at2026-10-22T16:02:21Z:
119793311395, Livepatch lifecycle (amd-scale-aged-v6), Run livepatch lifecycle
tests and Evaluate test results failed. Overall run39767770407 is nonterminal.
Separate preserved evidence:
generic-sysctl-ci-39767770407-600s-failure-119793311395/{job*,artifacts/}.
I2 is inspecting first actual local error/stage before selecting any action;
cause unknown, no new observer/query/rerun/cancel/source edit/claim/merge.
AMD first actual error is final dmesg no-fault assertion, not setup/build or
activation timeout: kernel/livepatch-qualification@amd-scale-aged-v6 reports
Dying CPU not properly vacated! then WARNING CPU127/PID789 migration/127 at
kernel/sched/core.c:8333 sched_cpu_dying.cold, kernel6.12.95.6 uptime14636.489.
CPU127 offline exercise17:24:42–51CEST and subsequent online both returned0;
activation attempts1 elapsed757.998s below1800, expected trace/callbacks.
Final assertion17:41:35CEST detects retained warning. Clarified chronology:
first hotplug warning17:24:42–51CEST precedes corrected.ko insmod17:26:09–
17:38:46; v7 then activates and second hotplug succeeds. This does not make the
warning benign. Guest boots CURRENT846bb OS36lyy... on frozen6.12.95.6 kernel,
not predecessor OS; new sysctl supervisor/logger/down are observed but actual
output/stamp/values absent. Cmdline lacks hard/soft panic arguments, no OSswitch.
Generic boot-service reachability remains; contribution not excluded. Architect
owns bounded exact-source interpretation of preexisting v6/kernel path, no broad
kernel audit or new tests/repair selected.
Subsequent same scheduled watcher table:6success,2failed,3active; AMD low-memory
v6 job119793311386 and v5 job119793311444 passed. Remaining active:amd-fresh,
amd-scale-aged-v5,amd. Overall nonterminal. Architect's exact-source reading
classifies the warning as runqueue CPU-hotplug invariant (nr_running!=1 OR
pinned), not lockup/panic; offline0 and later activation cannot prove harmless.
No root cause/fix established; only adjacent retained dump is being checked for
the failing invariant branch, then bounded diagnosis stops. Existing600s watcher
continues; no source changes/rerun/cancel/claim/merge.
AMD bounded diagnosis complete: adjacent CPU127 dump says2total, naming only
migration127/PID789. Excess task, pinning and callback owner are unknown; no
attribution to another unnamed task. Exact pinned a238 core.c:8332 WARN tests
nr_running!=1 OR nr_pinned, then continues/returns0, explaining why successful
offline is insufficient health proof. Incoming v7 execution is excluded at the
warning by timing, current846bb/generic boot-state contribution is not. Stress
also writes sysctls; actual service/stress values and excess-task/timing evidence
needed for a causal chain are absent. See design.md#amd-livepatch-hotplug-warning-boundary
and generic-sysctl-ci-failure.md. No repair, rerun, broader audit or merge
selected; original incident attribution unchanged. Existing600s watcher retains
the three remaining jobs, no duplicate observation.
At2026-10-22T14:42:27Z the existing watcher reported product job119793311317
failed after3h6m41s (Run tests and Evaluate test results). Run39767770407 is
still active:4success,1failed,6unfinished at the captured table. Available
artifacts are preserved under
generic-sysctl-ci-39767770407-600s-failure-119793311317/artifacts/;
per-job log retrieval returned1/empty, artifact download succeeded. I2 owns
bounded local first-failure diagnosis before any source edit/rerun. No cause
attributed yet; focused VM8/8 remains separate passing evidence. Native suite
reports124pass/6fail (130tests,338scripts,8782.07s), guest assertion failures,
not prebuild. Five upgrade guest variants expected an impermanence-suffixed
boot dataset but got tank/ct/niximpermanent, matching prior signature; historical
similarity alone does not establish current independence. Sixth test
upgrade/from-6.18-nested-podman timed out waiting nestedpodman online. I2 owns
current sysctl/service evidence; architect owns historical dataset provenance
and causal synthesis; i0 independently owns nested timeout logs. Local preserved
artifacts only, no new tests or source edits selected. No claim,
merge, rerun, cancellation or duplicate observer. Existing600s watcher retains
remaining CI. Implementation/review/publication and focused VM verification
are complete; successful CI is required before integration under user approval.
Bounded local diagnosis: nested-Podman timeout occurs before any feature switch
on predecessor h772xs...; dhcpcd reports ps_managersandbox seccomp Permission
denied, ifup fails, no IPv4/default route, DNS online probes fail. This first
error precedes new sysctl/panic activation; deeper DHCP cause unresolved.
The same five dataset signatures predate the generic feature in b81c CI, but
current artifacts cannot prove generic apply success/timing/live values or
mounted-dataset/runtime-YAML cause. New runsv sysctl/svlogd and down state are
present, insufficient to prove application. Current CI system/sysctl itself
passed (expected_success,15:26:05–15:27:34CEST,89.08s), separate from local8/8.
No demonstrated feature-caused first error or justified source fix; merge stays
blocked on redCI and no rerun/unrelated repair is selected. I2 consolidates
architect/i0 note and retains existing600s watcher through overall terminal.
Consolidated evidence: [current CI failure note](generic-sysctl-ci-failure.md),
[nested-Podman diagnosis](generic-sysctl-ci-nested-podman.md), and architect's
design.md#current-product-ci-causal-boundary. Architect directly compared all
five current retained-state failures and b81c history; unchanged fixture/export/
run-config/stage1/switcher plus prior occurrence are not a controlled baseline.
Distinguishing dataset mechanisms would require pre/post run-conf bytes and
mount source plus timed sysctl outcome/readbacks, absent from current artifacts.
No expanded loader audit, repair or rerun is selected. All bounded diagnosis
lanes completed without source mutation or another observer. Merge remains held.
User explicitly directed in this conversation: "keep checking it periodically,
like every 10minutes, and merge when it is done". Approval covers vpsadminos
into its registered staging target, conditional on CI success; it does not
authorize deployment, pins, configuration integration or session lifecycle.
I2 owns existing-watch cadence (~600s), persistent CI/failure follow-up and
unlocked integration preparation. Lead retains final freshness gate; only then
acquire one repository claim for checks/ff-only merge/hooks/non-force SSH push/
remote proof, release before records/CI. No claim during CI waits. Source head is
846bb469505789ba0b2a405fa5905ba6d8253006, tree
df9bd828d843225df749b7a05ed9529bf17425c9, clean. Complete history remains
base55c504 → unchanged panic852826 → generic846bb, six files +399/-1.
Literal-source tracking and the valid EINVAL probe pass quick checks/hooks.
Reviewer0 (retained Sol/xhigh/read_only) accepted all four HIGH-risk lanes,
turn01a16344-9ca0-78a2-b440-68d74c5d0482, no findings, explicit clean whole-series,
no-migrations/no-repeated-streams conclusions. Lead released normal publication
and one corrected focused run to i2. See generic-sysctl-final-review.md.
Cadence handoff confirmed: same native watcher01a1634c-0553-7530-ba30-b19cfc2307d0
owns exactly one `gh run watch39767770407 --interval600 --exit-status` with
durable generic-sysctl-ci-39767770407-600s.log/.exit/.started/.ended. Previous
local watch PID2270275 was deliberately interrupted (exit130 control-only),
old handles/CLI accounted; remote CI untouched. Terminal/material-failure
notifications route through i2 to lead, with no unchanged-update loop. Fresh
SSH refs still staging55c504/feature846bb, source clean. I2 continues unlocked
integration preparation and stops before merge until CIgreen+lead release.
Premerge preparation accepted from generic-sysctl-premerge.md: fresh SSH refs
at2026-10-22T14:00:14Z still55c504/846bb, exact reviewed two-owner range and
six-file +399/-1 final diff, no migrations/repeated streams/obsolete history.
Clean detached target vpsadminos-staging-integration is at55c504; declared Nix
environment/ordinary hooks are ready, actual postmerge hook exited0. V3 backup
and exact history/patch/ref inventory/comparison retained. No source changes,
new tests or claim. Existing600s watcher remains the only CI owner; lead final
freshness gate and short critical section remain conditional on CI success.
CI status receipt2026-10-22T13:07:42Z from the existing watcher: run39767770407
at exact846bb remains in_progress, conclusion unset. Eleven jobs:4success,
0failed,2running,5pending. OS/cache and three Intel lifecycle jobs passed;
product suite is at Run tests and AMD-scale-aged-v6 is at livepatch lifecycle
tests. Remaining five AMD variants are pending. No first failure reported.
See generic-sysctl-ci-39767770407-current.json; next action remains existing
watcher terminal/material-failure follow-up, no new observer/query/retry.
Normal declared-env SSH publication of846bb completed with exact895 lease;
remote proof confirms846bb and unchanged staging55c. Automatic exact-head
CI39767770407 was discovered queued, no workflow manually launched. Old895
CI39764186292 is completed/cancelled (generic-sysctl-v2-stale-final.json);
recovered native CLI exited0 and all started command IDs are accounted complete,
no active operations. First895 evidence is retained; no failed CI jobs existed
at stale control. One fresh retained Luna/low batch owns exact846bb
CI39767770407. Its selected focused command passed: durable exit0, native
expected_success, all8/8 examples successful. Wrapper PID2229812 ran
2026-10-22T11:08:31Z–11:14:33Z (362s); runner353.17s. Lead directly inspected
the current selected log and exit/start/end files and confirmed clean source.
See generic-sysctl-focused-vm-846bb4695.log/.exit/.started/.ended and
[the final binding receipt](generic-sysctl-focused-vm-846bb4695-receipt.json).
All six changed paths in actual frozen runner source1dvy794... match exact846bb
Git blobs and clean worktree. Native config2mv081... contains corrected bootwait,
EINVAL probe, attempts1 and cached kernel/initrd; current expected_success was
written11:14:33Z. Native logs/resolved config are copied under
generic-sysctl-focused-vm-846bb4695-artifacts; old895 failure diagnostic is
explicitly historical. Lead inspected receipt and current packet, accepted the
complete focused binding. No retry/cache gate/duplicate.
The watcher now owns only existing CI39767770407; broad completion is pending.
Fresh native watcher identity01a1634c-0553-7530-ba30-b19cfc2307d0 is verified
from actual turn context as gpt-6-luna/low, danger-full-access/never in the exact
OS worktree, retained utility digestffaf9deb97720995ad1d662badae7645eba1fede5068eef529c9024efa7e7376.
During this run, focused-log frontier reported at11:12:57Z showed examples1–3
passed at
11:12:34/50/53Z, proving this guest boot and service assertions executed.
An interim unexpected_failure/empty-shell report was from retained895 files
in the reused native temp path (old12:46CEST timestamps), not846. Terminal
authority is the current durable exit plus selected log and time-bound native
evidence; the terminal pass above supersedes that interim report.
The earlier895 focused run booted and completed natively6/8 pass,2 failure-path
fixture failures; preserved historical evidence does not certify846bb. The
current successful focused test verifies benign disposable-guest integration,
not production application, panic/crash capture or broadCI. No merge/pin/deploy
or session lifecycle action. Session remains active and unmerged.

Architect0 reproduced an actual same-path local source content edit that changes
the installed etc store file but leaves toString-based inputs/hash/triggers and
run/check unchanged. The pinned etc renderer canonicalizes literal paths through
Nix string interpolation. Lead selected that exact one-line normalization plus
a comment, with no new framework. I2 completed v3 implementation/quick checks/
commit and all-four-lane final review is accepted. The earlier895 test used
frozen store inputs; source independence allowed the bounded fix concurrently.

Pinned procps4.0.6 source confirms the failure-probe diagnosis: `--system`
sets IgnoreError and treats a missing key (ENOENT) as success. I0 replaced
the unknown-key probe with `kernel.printk_ratelimit=invalid`, which takes the
EINVAL/EXIT_FAILURE path. Nixfmt/parse/whitespace, full graph render and Ruby
syntax passed; fixture SHA256 is
974690e33b6ec9428c7a6f8c74b4006dc975bc20df37e137a75a3c6493fb1be7.
See [the source diagnosis](generic-sysctl-failure-injection.md). This changes
fixture expectations and logs only; product error handling remains unchanged.
I2 folded both corrections into generic v3; its accepted final review is linked
above. Publication and corrected focused integration verification are complete.

Recovered SAME native watcher01a16333-01c8-7451-afe4-b8c8c406a16b owned
895 CI39764186292 through the terminal accounting above, without a duplicate.
At12:47:40CEST the earlier native test ended:
examples1–6/8 passed;7–8 failed because the expected-failing custom check
returned0 under the unknown-key error injection. Boot succeeded; this is not
another boot/shell failure. All local run processes ended. Original handle58982
and outer exit are unavailable after CLI-15; native unexpected_failure is
explicit. I0's pinned-source diagnosis and valid numeric probe correction are
complete as described above; no product error parser or blind retry. Old88486
CI39759039117 is completed/cancelled; handle11206 and earlier handles are ended.
Both authorized cancellation requests targeted only that stale run. No old
active operation remains. No merge, pin update or deployment occurred.

V3 source normalization and comment are implemented. Same-path literal content
7→9 now changes canonical store source, identity/triggers and run/check; the
canonical trigger source equals actual etc renderer output. Ten ordinary
text/store graph variants retain identities/triggers/generated scripts and
service/panic settings. See generic-sysctl-literal-check.log and
generic-sysctl-v3-ordinary-inputs.log. No new VM or cache query was launched.

## Earlier checkpoint details (historical)

Guest shell readiness consumed the first service check's60s; no guest command
or actual sysctl failure was recorded. Product service/panic/docs are unchanged.
Normal declared-env SSH replacement push89587060 completed against the exact
88486 lease; SSH refproof confirms89587060 and unchanged staging55c. Automatic
exact-v2 CI39764186292 was discovered queued. Superseded88486 CI39759039117
remains with its existing owner until terminal accounting. I2 used one explicitly
authorized status/cancel control: verified exact88486/in_progress and zero
completed failed CI jobs, cancellation request exit0; no second observer loop.
First native VM failure remains copied durably. The next fresh batch waits only
for old observer/handle11206 no-active receipt, not another OS/cache build.
Architect0 owns the written service contract; implementer2 owns the module,
quick checks and serialized OS Git operations; implementer0 owns focused VM
coverage and operator documentation. Existing paired panic declarations remain
at85282623; its CI remains under the existing observer, not generic-service
verification. No merge, pin update or deployment occurred.

Current local tuple:55c5046514d06fe9398a022c1622bdaae5228841 →
895870606179f0c1170ad92a5fdc49eb2d6d1bbf, tree9d2966d6d0f66520c827b434106946c635ef991c,
clean. Delta from88486 is exactly machine.start(wait_for_boot:true) in fixture
setup plus the generic owner's v2 message/history; parent852826 is unchanged.
Normal hooks and fresh fixture checks pass. Reviewer0's retained Sol/xhigh
general/scope review accepted in turn01a16329-9d23-7272-88c3-aef7a719a25d, no findings;
prior product architecture/risk conclusions are reused with byte-identity proof.
No second VM run yet; replacement publication is reported above. Exact kernel/initrd paths match the first
native run and exist locally; full guest path equality across differing import
provenance is not claimed or needed. No additional cache probe/build selected.

Original accepted review tuple:55c5046514d06fe9398a022c1622bdaae5228841 →
88486d43f7d47917b6ab796163abf8cd1f0be94a, clean. Complete history is unchanged
panic owner8528262315b0794a8f50917cf33c53a07fd14030 followed by one generic
service owner88486d43. Six files397+1-, no migrations or repeated update streams.
See [the complete verification packet](generic-sysctl-verification.md).
Reviewer0 accepted all four lanes at retained Sol/xhigh/read_only, native
turn01a16302-7eb1-7f62-98b3-4ea30746351f, HIGH host-runtime risk, no findings.
Whole-series no-migrations/no-repeated-stream conclusions explicitly accepted.
See [the retained final review](generic-sysctl-final-review.md). Lead released
publication and the one-shot focused VM verification gate. SSH proof confirms
feature88486d43 and staging55c504 unchanged; automatic exact-head CI39759039117
started. Old852826 CI39745935323 is completed/cancelled after authorized stale
cancellation; its observer/handle99939 ended (watch exit130), no old process.
First HTTP429 cause and125 final artifacts/logs are retained. One fresh native
utility `/root/generic_sysctl_88486_watch`, retained Luna/low/fresh context and
installed full_access/danger-full-access/never, positively verified session,
clean HEAD and exact CI binding. It owns CI39759039117 plus the single focused
command after exact OS/cache job119758301061 succeeds. At startup that job was
in progress at the persistent-activation check; the VM had not started then.
The first focused result follows. No parent CI observer exists. Old final job totals are
4success/1failure/6cancelled, all11 terminal.

Focused command `./test-runner.sh test system/sysctl` ran once at88486d43 and
exited1 after187s (native runner159.54s), unexpected_failure. First error:
test-runner.log:1240 timeout running `/service/sysctl/check`. Native artifacts
are `/tmp/os-test-runner/os-test-system__sysctl-8ae7035e/`; full captured output
is generic-sysctl-focused-vm-88486d43f.log. Linux6.12.113 image was substituted
from cache.vpsadminos.org; only modules/modules-shrunk local derivations were
reported, no kernel image compile. No cache investigation/probe or blind rerun
was launched. Existing utility retains CI observer session11206.

Diagnosis: machine-shell.log contains only its header; console contains firmware
and BootingROM before harness termination. Machine#start defaults
wait_for_boot:false and Shell#execute waits for shell readiness inside the
command deadline. I0 changed only setup to machine.start(wait_for_boot: true),
using the existing900s boot budget before the60s service check. This fixes
classification/budget, not the still-unexplained lack of Linux/shell output.
Fresh Nix format/parse/whitespace, complete fixture graph and rendered Ruby
syntax passed (generic-sysctl-i0-boot-wait-quick.log). Owner amendment and affected
general/scope final review must precede the next focused run. First-failure
artifacts remain preserved; no blind retry or service-code change is selected.
Existing watcher metadata reconciles timing: OS/cache job succeeded10:07:28UTC,
focused command ran10:09:47–10:12:54UTC, so the cache gate was satisfied. The
late receipt supersedes earlier last-known cache-pending updates.

Quick evidence: ten real module variants and isolated native runsv/generated
run/check behavior passed, including success, failure after success without
retry, explicit retry, stale identity and setup/marker failure paths. The
eight-case focused fixture evaluates and its rendered Ruby parses; format,
Nix parse, whitespace, bundle and MkDocs checks passed. No host sysctls or VM
test were run. See generic-sysctl-module-check.log, generic-sysctl-isolated.log,
generic-sysctl-i0-render-final.log and generic-sysctl-i0-final-quick.log.

Prior-head CI39745935323 reported a test-preparation failure: GitHub HTTP429
while fetching Linux source, before VM assertions. See
[the bounded failure note](os-hardlockup-v3-ci-failure.md). That run and its
observer are now terminal/accounted; no rerun or generic-service inference is made.

## Phase checklist

- [x] Agree normal runit service, retained early boot apply, one attempt and
  unchanged switcher exit-status behavior; user requested implementation.
- [x] Record final architect-owned service design and implementation boundaries.
- [x] Implement service, focused test and documentation; pass quick checks.
- [x] Commit original generic owner and independently review complete history.
- [x] Amend the readiness fixture and complete affected final review.
- [x] Normalize literal-path sources and correct EINVAL probe; quick-check/commit v3.
- [x] Complete independent all-four-lane final review of v3; no findings.
- [x] Pass focused disposable VM verification under a fresh utility watcher (8/8).
- [x] Publish exact final head and reconcile evidence; leave session open.
- [ ] Existing watcher accounts exact-head broadCI39767770407; no duplicate observer.
- [x] User accepted observed CI exceptions; final freshness gate and vpsadminos/
  staging ff-only integration completed under short claim, remote proof/release.
- [x] Start separate delegated_4 failure/rootcause/test-usefulness investigation.
- [ ] Deployment/pin updates remain outside authorization; leave session open.

### Earlier phases (historical)

- [x] Remove custom activation hook/helper and add paired ordinary panic sysctls.
- [x] Quick-check enabled/disabled/overrides and absence of custom activation.
- [x] Consolidate/commit/publish v3 and obtain independent review.
- [x] Hand off declaration-only semantics and generic switch proposal; CI pending.


- [x] Confirm runtime sysctl/application gap and select targeted activation boundary.
- [x] Add same-gate sysctl, targeted activation and hard-lockup comment; quick checks pass.
- [x] Commit/consolidate, publish and independently review final history.
- [x] Report targeted live-activation path and runtime/readback/CI limits.


- [x] Design OS-owned hard-panic policy with identical crashdump gate/mechanism.
- [x] Withdraw obsolete configuration assignment and consolidate unmerged history.
- [x] Implement/check/commit/publish minimal vpsAdminOS change.
- [x] Review final cross-repository history and resolve message-only finding.
- [x] Reconcile terminal exact-head CI: 10 jobs passed, product suite failed.
- [x] Hand off completed source change, with CI explicitly pending and no deployment/pin update.


- [x] Design minimal shared-node policy and verify all-node scope.
- [x] Implement, quick-check, commit and publish configuration branch.
- [x] Independently review complete committed branch and migration inventory.
- [x] Hand off published/reviewed branch with explicit system-build limitation.
The configuration-only phase above is superseded. Its missing-secret system
build and integration tasks are no longer selected: the assignment is withdrawn
and the branch has zero changes. OS adoption/integration remains a later step
requiring separate user direction.


- [x] Inventory all-node eligible corpus and fixed July20–Oct20 window.
- [x] Complete every selected file/prefix and final directory reconciliation.
- [x] Independently validate full coverage and classify all in-window matches (zero reports).
- [x] Reconcile all-node three-month findings and limitations for user handoff.

- [x] Inventory complete retained node24 corpus and define current cutoff.
- [x] Search every retained node24 file successfully; record all detections (zero).
- [x] Independently validate full no-hit coverage; no episode to classify.
- [x] Reconcile node24-only policy evidence; no automatic setting change.

- [x] Search bounded cluster history for hard-lockup detections.
- [x] Verify recovery/same-boot evidence for found episodes (recovery unproven).
- [x] Reconcile source semantics and policy-risk evidence with user.

- [x] Verify exact bound session identity and retained team/write access.
- [x] Establish incident window, deployed kernel and old livepatch provenance.
- [x] Account for every custom Linux patch and extra packaged ZFS change.
- [x] Complete independent custom source analyses.
- [x] Complete authorized targeted upstream source analyses.
- [x] Finish reconciled synthesis and user handoff.
- [x] Validate evidence local links and whitespace (17 Markdown artifacts).

## Current conclusions

- Complete three-month search: zero hard-lockup mentions/reports in all 1,221
  selected prefixes (557.249 GB), July 20 through October 20, 23:08:52 CEST.
  Independent reconciliation passed. Thirteen active sources supplied records;
  thirteen older directories have no retention in this window. See the
  [final report](cluster-hardlockup-three-months.md).
- Node24 stopped logging Oct20 at18:58:26.658330+02:00; recovery boot logs begin
  19:12:04.761663+02:00. Other nodes continued reporting. No forwarded kernel
  panic/lockup/RCU/blocked-task/hostOOM/storage/hardware error signature found.
- Exact incident OS2abbe3cc1c102a4b39022d3f73ef4a432ad4d616 selects Linux
  1dfea587406b7dd79973831d1677fb2418e5e9aa, later6.12.113 after proactive swap
  retirement. Earlier6.12.113 pin11058eb4 is different and was distinguished.
- Initial .113 carries all60 old custom patch bodies unchanged plus NLM guard.
  Incident .113 retains52, removes6 proactive/DAMON owners, consolidates2 memcg
  lifetime fixes into identical helper source, adds defensive NLM guard and
  ordinary swap reporting. All55 incident custom commits accounted.
- Extra .113 ZFS free-account patch removes a concrete prepatch lock-order edge;
  no replacement hang/race/lifetime chain found. Patch selected in both modes
  at exact incident OS:358cd303c is its ancestor despite equal timestamps.
- Targeted upstream memory/NFS/scheduler/RCU/locking/platform/printk intersections
  yielded no supported host-wide failure chain. This is not exhaustive review
  of all7278 stable commits/5291 changed paths or all drivers.
- Definite defects kept separate: preexisting syslog allocation-cleanup NULL
  dereference; new swap reporting unsigned underflows; upstream FREE_STATEID
  allocation-error reference leak pinning a mount. No incident trigger or
  host-hang chain established. Documented old-v6 effective FREE_STATEID error
  unwind differs; exact old loaded module/controlstate remains unknown.

## Missing crash upload: evidence and configuration

User confirms normal panic should crashboot/upload, none happened, and sysctls
had no runtime changes. Exact OS/config/Nixpkgs source trace gives configured
hardlockup_panic=0, softlockup_panic=1, watchdog1/NMIenabled, threshold10,
panic timeout0 and panic_on_warn/oops/RCU/hungtask0. Compile defaults are
source-inferred through unchanged Kconfig/recipe lineage, not recovered.config.
A detected hardlockup therefore need not invoke panic/kdump. This is compatible
with no upload, not proof a hardlockup occurred or evidence of a causing patch.

Kdump:loaded is positively logged18:31:57/59,26.5min before lastlog. Source marker
checks a nonnull crash image; crashentry/transfer/capture/NFSupload remain
unobserved. Configured SPLspl_panic_halt1 calls Linuxpanic, so deliberate SPL
assertion freezing with value0 is excluded. VGA hardware cursor can blink
without scheduler progress. Missing dump/cursor alone does not locate failure.

## Owners, results and evidence

| Owner | Completed result | Acceptance evidence |
| --- | --- | --- |
| architect0 | Design, scheduler/custom intersections, final synthesis | Exact source chains/gates; bounded negative |
| implementer0 | Full custom inventory, upstream/livepatch provenance, printk7 audit |60/61/55 accounting; exact bodies/blobs; panic ordering |
| implementer1 | Central logs, hardware/crash markers, ZFS patch audit | Exact bounded excerpts; ownership/lock cycle proof |
| implementer2 | Custom and upstream memory audits | Balanced refs; complete retirement; reporting defect/source gates |
| implementer3 | Custom syslog/NFS and upstream RPC audit | Defect proof; TLS wait actor exclusion; mount leak scope |
| implementer4 | Packaging, applicability, platform and watchdog policy | Exact selectors/ancestry; repo precedence and user attestation |
| lead | Scope, assignments, acceptance, tracking and portal | All final source artifacts read and registered |

Entry point: [synthesis.md](synthesis.md). Design: [design.md](design.md).

Custom evidence: [patch-inventory.md](patch-inventory.md),
[packaging-audit.md](packaging-audit.md),
[scheduler-analysis.md](scheduler-analysis.md),
[memory-audit.md](memory-audit.md),
[syslog-nfs-audit.md](syslog-nfs-audit.md),
[zfs-patch-audit.md](zfs-patch-audit.md).

Upstream evidence: [upstream-provenance.md](upstream-provenance.md),
[upstream-memory-audit.md](upstream-memory-audit.md),
[upstream-nfs-audit.md](upstream-nfs-audit.md),
[upstream-scheduler-audit.md](upstream-scheduler-audit.md),
[upstream-platform-audit.md](upstream-platform-audit.md),
[upstream-printk-audit.md](upstream-printk-audit.md).

Logs: [log-evidence.md](log-evidence.md) and its linked exact selected excerpts.

## Verification and limits

- Canonical bare repos read; no feature branch/worktree/source edits. Old boot
  a2384967b90f24d2470c9eb15f0e66d938df7e08; stable source bases
  296aabce459470a4c1b68ffd0c0c0920e563aaad to
  7fdb7c1824a1f9979d648d7ae28ac446bcee9c6e.
- Source checks include patch/body/blob identity, lock/ref/error-path traces,
  configuration predicates/ancestry and complete owner accounting. No dynamic
  test, kernel build, reproduction, configuration mutation or deployment run.
- Source-proven defects do not justify a blind host-hang reproducer without a
  demonstrated progress chain. No automatic review for findings/evidence alone.
- Central logs read as root@log.int.prg.vpsfree.cz. Direct node SSH blocked by
  absent trusted key; no trust bypass/change. Historical runtime mounts/NFS
  transport and final binary.config not recovered.
- Partial Linux clone missing blobs materialized only by implementer0, authorized
  exact object-only fetches67+11, no refs/FETCH_HEAD refresh. Early implicit
  retrieval was disclosed/stopped. No future stable history fetched; local later
  refs limit does not prove no later upstream fix exists.
- Initial plan/state/portal commit78f1ea18. Subsequent evidence is consolidated into one end-of-work daily checkpoint
  under normal tracking cadence; unrelated shared workspace changes preserved.

## Remaining source-attribution evidence

The original source investigation is complete; no further source work planned without new
discriminating evidence. Attribution remains blocked by absent stalledCPU/task stack, NMI/IP/held-lock
trace or source-specific reproducible trigger. A future diagnostic decision can
consider hardlockup_panic1 and independent crash-progress capture; no such
configuration change or forced crash has been authorized/performed.

Stable session URL:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-20-kernel-check/
Session lifecycle stays active/open; no archive/delete/stop action authorized.

## Follow-up: detector distinction and policy history

User asked for bug details, syslog-namespace ownership, and rationale
for softlockup panic1 but hardlockup panic0. Same-session current/env/roster
verified; implementer4 owns bounded history check, no source/config changes.

- softlockup_panic1 introduced with crashdump.nix by OScommit
  5e7a0d7af5bd92fb8ac11778ed570d5cc32400ee, 2022-05-21,
  "os: kernel crashDump dmesg extraction". New enabled-crashdump module adds
  crashkernel reservation and softlockup panic together. Message has no rationale
  comparing hard/soft, no explicit attribution proving copied NixOS source.
- Incident-ancestor history in OS/config relevant paths reveals no hardpanic/NMI
  policy override or documented deliberate reason. Why hardpanic stayeddefault0
  is unknown; no invented intentional tradeoff or copied-code provenance.
- Soft detector: local hrtimer checks scheduled per-CPU watchdog work timestamp
  (current source uses stop_one_cpu_nowait/softlockup_fn), roughly
  2*watchdog_thresh=20s. Hard detector: PMU NMI checks local hrtimer heartbeat,
  roughly watchdog_thresh=10s. Independent triggers/panic policies; a hard stall
  can prevent the timer-based soft detector from executing.
- Bug explanations refer to final audits: syslog namespace setup failed
  allocations call cleanup with NULLprb; swap independently sampled counters
  wrap in reported values; FREE_STATEID calldata allocation failure leaks refs,
  pins mount, no proven hostwidewait. All remain unattributed to incident.
- Follow-up complete, no new blocker. Main recommendation can consider enabling
  hardpanic and verifying nonproduction crash capture, no change/test performed.

Follow-up evidence: [watchdog-history.md](watchdog-history.md), accepted and
registered. No additional same-day tracking commit under normal cadence.

## Follow-up: could hard-lockup detections be nonfatal?

User explicitly asks whether cluster nodes have survived hardlockups and wants
central-log evidence before enabling hardpanic1. New read-only investigation;
no policy change, crash, stress test or production mutation authorized.

| Owner | Result | Acceptance / checks | Dependencies |
| --- | --- | --- | --- |
| architect0 | Follow-up design/confidence boundaries | Differentiate detector event, continued otherCPU traffic and actual affectedCPU recovery | Source and log reports |
| implementer1 | cluster-hardlockup-history.md, bounded central search | Exact signatures/hosts/timestamps/coverage; low production IO cost | Log inventory |
| implementer4 | hardlockup-recovery-semantics.md | Exact warning/reset/panic source paths, no historical claims from source alone | Canonical Linux |
| lead | Evidence acceptance and policy explanation | No blanket rollout advice without observed risk evidence | All packages |

Start with bounded recent allnode log inventory/search; extend only rationally
within available retention/IO budget, report explicit limits. Assign independent
recovery verification once eventfiles known. No absence-of-hits=>neverhappened
claim and no otherCPUlogging=>affectedCPUrecovery claim.

### Hard-lockup follow-up milestones

- Log inventory26hostdirs3477files~1.08TiB, rotations2022-11..2026-10, all
  uncompressed, no obvious indexedremote source. i1 sole sequentialscanner.
- Current13activefiles3.822GB searched with noevents/noerrors/timeouts; cannot
  conclude wholeclusterhistory. Authorize next bounded historical tranche up to
  30GiB after metadata/datebounds, noblind1TiBscan.
- I4 source: panic0 returns afterwarning; subsequent sameCPUfailedchecks silently
  suppressed, healthyheartbeatchange clearswarned withoutrecoverymessage.
  Fresh repeated sameCPUreports can support intervening recovery only excluding
  boot/hotplug/toggle/reset ambiguity. Panic1 requestspanic onFIRSTaccepted
  detection, including transientrecoverable events; no escalationdelay.

### Hard-lockup search completed tranche

All78selectedfiles30,118,840,414bytes28.05GiB completed119s(~253MB/s),
no matchingdetections/noerrors/timeouts.65activerotationsactualOct15–19;13inactive
latest sparseolderdates2022–25. Extra3legacyfiles.861GB within30GiB authorized.
Attributionsurvivalclassification notpossiblewithout actualhit. Sourceartifact
[hardlockup-recovery-semantics.md](hardlockup-recovery-semantics.md) accepted and
registered; exact .95/.113 detectorfilesidentical, noolderlogicclaimwithoutsource.

I1 asked metadata-only calendar-stratifieddisjoint proposal<=60GiB for older
examples (~4min at measuredthroughput), notblindfull1TiB(~80min). Need representative
month/host coverage explicitly, nofrequencyfromsample nor'never'fromabsence.
Policyrecommendation conservative holdoffclusterwidehardpanic pending evidence.

### Hard-lockup follow-up final accepted evidence

- Total historical81files30,980,043,942bytes (~30.98GB/28.85GiB), plus
  separate13currentfiles3.822GB atinventory. Everysearchedfilecomplete, noerror
  ortimeout. Current/selectedrecentrotations nohardlockupdetections. Other
  ~1.08TiBretention mostlyunsearched; no frequency/never/safetystatement.
- One realhistoricalepisode stg/node1 Oct28,2022: CPU25 and33 watchdogreports
  uptime129s on5.10.147.8 livepatched, precedingpagefaultuptime108s/RCUstall.
  Nextoriginalrecordafterdiagnostics is5.10.149boot, collector~10m22slater.
  Batchedtimestamps doNOTmeasurestall duration. No samebootservicecontinuation
  or affectedCPUprogress/recovery established; resetcause/irreversibilityunknown.
- Independentclassification [hardlockup-episode-analysis.md](hardlockup-episode-analysis.md)
  accepted, noextraremotequeries. Collector
  [cluster-hardlockup-history.md](cluster-hardlockup-history.md) accepted, source
  [hardlockup-recovery-semantics.md](hardlockup-recovery-semantics.md) accepted.
- Source permits finite/recoverablestalls and firstacceptedreportpanic1 would
  requestpanicbeforeanylaterrecovery. This risk isrealpolicytradeoff, but
  noverifiednonfatalclusterexample found in boundedhistory. Holdoffblanket
  hardpanicpolicychange; no claim currentdefaultoptimal.
- No calendartranchelaunched, no scannersrunning, noconfig/test/productionchange.
  Furtherhistoricalscanning optionalfuturework, notnecessaryboundedanswer.

Final follow-up synthesis accepted in [synthesis.md](synthesis.md). All local
artifact links/whitespace checks pass; no further search or policy change planned.
Remaining uncertainty is historical recoverable-event frequency and node24 cause,
not a pending assigned action. Session stays open.

## Follow-up: complete node24 retention

User explicitly requests all node24 logs for hardlockup and survival, considering
a node24-only policy rather than clusterwide. This expands beyond previous
30GiB sample budget for node24 only. No deployment/config authorization.

| Owner | Result | Acceptance | Dependencies |
| --- | --- | --- | --- |
| architect0 | Separate design/coverage/confidence scope | Full corpus, snapshot/cutoff, no negative partial results | Collector inventory |
| implementer1 | node24-hardlockup-history.md and manifest/status/matches | Every retained node24 file searched, aliases/compression/rotation accounted | Central log read-only |
| implementer2 | Local episode classification or no-hit coverage corroboration | Distinguish hostcontinuity/CPUrecovery; no extra scanner | Collector evidence |
| lead | User report, records and acceptance | Full retained coverage; no unearned pilot safety claim | All packages |

Sole sequential low-priority scanner, interruptible per-file work, all hits kept.
Source current/old detector semantics used only at verified versions. No-hit
means no forwarded detection in retained corpus, not no stall or guaranteed
safe panic policy. No config/production/trust/ref/source changes or tests.

### Complete node24 inventory milestone

Collector snapshot1792523256 includes181regularuncompressedfiles,
89,603,613,857bytes83.45GiB:180dailyrotations+currentlog. Actualfirstcontent
2026-04-23T00:00:01.261611+02 throughcurrentcutoff
2026-10-20T21:07:36.802428+02, current359,236,720bytesdevice74/inode204420.
No legacy/compressed/nonregular entries or discoverednamed/IPaliases under
remote boundedhierarchy; maxfile2.67GB. I2 independentlychecksmanifest locally.
One sequential lowpriorityscan planned6–8min, allcandidate+bootidentitylines
samebytepass, timeout/retry and pre/post fileidentity checks. Noresultsclaimyet.

### Full node24 progress and manifest corroboration

I2 independently validates181uniquepaths/inodes,180contiguoussuffixdates
Apr24–Oct20,89,603,613,857B, alluncompressednewlinecutoffs andmetadataadjacent
timestampgap<=.654s. This verifiesretentionsequence, notcontinuousforwarding.
At31/181completed i1 nohardlockupmentions/readtimeouts/identityerrors; nofinal
resultbeforeall181complete. Report+manifest registeredportal whilepending.

At63/181collectorfiles,33,751,283,538snapshotbytes complete, zeroinclusive
hardlockupmentions, noresumes/timeouts/identityerrors. Bootlabelscollected
separatelyare notdetections. Finaldirectoryreinventory planned; latercurrent
appends outsidecutoff explicitlyreported. No completedfile rerunsrequired.

Fullnode24 at102/181collectorfiles56,232,504,710B throughAug2rotation,
zero hardlockupmentions/timeouts/retries/identityerrors. I2 independentlocal
pairedstatus/identitychecks inprogress; finalnohitacceptance stillpending.
Priorclusterwideholdoff notautomaticnode24trialrejection; fullhostnohitresult
wouldprovide noobservedhistoricalrecoverablecounterexample, notfuturezerorisk.

I2at140/18172,050,227,054B verifiesuniquestatuspairs+manifestcutoffs/dev/inode/
staticmetadata, zerohardlockupmentions/failures. Finalreceipt/postdirectory
reinventory pending, noepisodesartifact neededifnohits. Rootlink/whitespace
checks passsofar. No node24policychangeperformed or implicitlyauthorized.

### Full node24 scan and independent reconciliation complete

Rawpassfinished402seconds. Independenti2 validates181manifestentries=181unique
BEGIN=181uniqueEND,89,603,613,857snapshotbytes; rc0x5/1x176, noerrors/timeouts,
allstaticmetadata/device/inode/cutoffs agree/currentappendallowed. All19source
matchesareboot/versionlabels; inclusivehardlockupmentioncount0. Norealepisode
existsfor survivalclassification. Finalcollector directoryreinventory/append
delta pendingbeforecompletenegative acceptance. CutoffunchangedApr23→Oct20
21:07:36.802428CEST, nohistoryearlierretentioncovered.

### Full node24 final accepted result

Collectorreceipt+independentlocalcorroboration complete:181unique successful
files89,603,613,857B402s, zeroinclusivehardlockupmentions/detectionepisodes.
All19matchesboot/versionlabels,5filesrc0+176rc1. Noerrors/timeouts/retries or
identity/staticmetadataissues; postdirectorysame181paths withnonew/missing.
Currentdev74/inode204420 grew2,318,193Bafterfixed21:07:36.802428cutoff, excluded.
ManifestSHA caba1fe8496cf65f6230c07203ee1f8d146fe76b3f8c43ebcd017c993a138346
validated byi2againstreceipt/output/matches. Noepisodeanalysisartifactrequired.

[node24-hardlockup-history.md](node24-hardlockup-history.md),
[node24-hardlockup-manifest.tsv](node24-hardlockup-manifest.tsv),
[node24-hardlockup-search-output.txt](node24-hardlockup-search-output.txt),
[node24-hardlockup-coverage-receipt.json](node24-hardlockup-coverage-receipt.json)
registeredportal. Fixedscopeactual2026-04-23 00:00:01.261611CEST through
2026-10-20 21:07:36.802428CEST. No observedhistoricalnode24survivedhardlockup
because no forwardedreportfound; unknownunforwarded/preretention/futureevents.

Node24-onlytrial is reasonableoption forfuturecapture givennohistoricalrecorded
counterexample, but no guarantee ofsafeorbeneficialpanic orsuccessfuldump.
Useronlyaskedsearch/consideration; no sysctl/configdeployment orfaulttest.
Remainingdecision optionalnode24pilot, originalnode24hang remainsunattributed.
No furtherassignedcollectionorverificationneeded, sessionstaysopen.

Finalnode24collectorreport and independentsummary accepted; registeredcomplete
manifest/rawmatches/searchoutput/postinventory/JSONreceipt+history links. All
localMarkdownlink/whitespace checks pass. No scannerremainsactive, nosetting
changed. Read-only fullhistoryassignedwork done; finaldesign/synthesis refresh
reflects completed scope, no extra analysis/deployment needed.

## Follow-up: SysRq through Dell remote console

User requests explanation/instructions only for MagicSysRq via IPMI/iDRAC and
serialBREAKtiming. No liveconsoleconnection/command/crash/config/testauthorized.
I4 owns exactLinuxUART/sysrq docs timing/prerequisites; i0 primaryDellconsole
transport/generation docs; architect shortacceptance scope; lead userexplanation.
Need distinguishvirtualgraphicalkeyboard Alt+SysRq fromSerialOverLAN realBREAK,
serialmapping/build/sysctlmask and stoppedinput/interruptpathlimits. Precise
timing mustbeverified, no inventediDRACUIfeaturewithoutprimarysupport.

SysRqfollowupusersteering: wants atloginprompt duringhangtoforcecrashkernel.
Kernelinputpathneedsnologin; 'c'deliberatelypanics and attemptsloadedkdump, still
requiresinput/interruptprogress. I4sourceverifies serialoneBREAKthencommand
within5s (no2swait), secondBREAKcancels, ipmitoolEnter~B realSOLbreak. c mask
SYSRQ_ENABLE_DUMP0x8, serialmaskenforced; hhelpnotproofcpermission. I0Dell
graphicalmodifier/macrobehavior checking, noinventedprefixrelease workflow.
RepoSysRqmask/serialmapping/build prerequisites pending. No liveoperation.

SysRqsource/prerequisites accepted: ordinarynode24recipe MAGIC_SYSRQ+SERIALy,
DEFAULT_ENABLE1/no sysctlassignment inexactOS/config/Nixpkgs andusernoruntime
changes => expectedkernel.sysrq1, alloperationsincludingcpermits. Current
node24observedfullbootcmdlineNOconsole=ttyS*, serial-consoledefaultfalse/no
override; compilingserialSysRqdoesnotestablishLinuxconsoleUARTforSOLBREAK.
GraphicaliDRACAltSysRqC kernelkeyboardroute separate, worksatloginpromptifinput
processingworks. DellHTML5listsgenericSysRqmacros butmodifierlifetimeundocumented;
donotteachclickprefix/release/typec, fixedAltSysRqBrebootsnotcrashprefix.
I0primaryDellmanualURLsverified, i4Linuxdoc/source+ipmitoolEnter~B5swindowverified.
No mandatory2swait, noEnterbetweenBREAKandcommand. No BMCconnection/crash/test.

SysRqfollowup complete: accepted [sysrq-remote-console-notes.md](sysrq-remote-console-notes.md),
registeredportal. Architectconsistencyaccepted conditionalGUIchorddelivery vs
SOLUARTrouteunestablishednode24; lowercasec/noShift, deliberatepanic notgeneric
reboot. No consoleconnection/config/crash/testperformed. Optionalhhelpsafekey
routeprobe butnotcpermissionproof. No furtherassignedresearchneeded.

PrimaryDellread-onlydocs fortransport/clientcapability:
- https://www.dell.com/support/manuals/en-in/idrac9-lifecycle-controller-v3.1-series/idrac_3.15.15.15_ug/html5-based-virtual-console?guid=guid-d7844cc4-f163-49e5-93f4-1e7f9e926857&lang=en-us
- https://www.dell.com/support/manuals/en-uk/idrac8-lifecycle-controller-v2.75.75.75/idrac8_2.75.75.75_ug/using-opensource-ipmi-tool?guid=guid-248dff06-6a09-4395-8b13-eb0068e6cb3d&lang=en-us
- https://www.dell.com/support/kbdoc/en-us/000185549/idrac-virtual-console-troubleshooting

## Follow-up: GUI SysRq h consumed but no visible output

Userreportsfirsthnottyped afterAltPrintScreen, subsequenthtyped. Consumption
isconsistentwitharmedinputroutebutnotproofkernelhandlerexecuted. I4checks
exactkeyboard/help/consolelevelhandling; i1boundedlast10minnode24forwardedtail
found0sysrq/HELP/disabledmessages,21:39:42–21:49:42CEST11,224records. Actual
GUItargetunconfirmed, asyncasked; nodirectBMC/host/sysctl/crashactions. Parent
providedread-onlysysctlkernel.sysrq+dmesg-w andrepeath procedure toobserve
actualkernelHELP outputwithoutc. No additionalpolicychangeauthorized.

ActualGUItesttargetcorrectedbynode2.stg; priornode24zeroHELPquerydoesnotapply.
Useraskedactualhostcat/proc/sys/kernel/sysrq andwhetherHELPabsencecheckedhost
dmesgvsGUIonly. Sourcei4: nativekbdactiveuntilmatchingAltrelease, hdoesnotdisarm;
subsequenthtypedAFTERAltreleaseexpected, notmodifierfault. __handle_sysrq
raisesconsoleleveltemporarilyforHELP andclears suppression, so ordinarylow
consoleloglevelaloneinsufficientexplanation. I1boundedcorrectnode2queryassigned
(shortlast15min, nohistory) followingearlierfailedtransientdelivery.
No node24mask1 claimappliednode2withoutverification. No ctest/settingchanges.

Node2.stguserconfirmedactualkernel.sysrq=1 andHELPabsentbothhostdmesgandGUI.
Thisrulesoutsimplemask0/GUI-onlyvisibilityassumption; inputdelivery/state main
suspectbutnotprovenfromswallowedh. Correctnode2forwardedlast15minqueryalso0
sysrqmatches(21:37:34–21:52:33CEST2139records), no runtimeversionobtained.
ParentrequestedactualiDRACgeneration/firmware/client(eHTML5/HTML5vsJava) and
keyboardmenuentries toidentifyreliablefullchordinjection. No ctest/settings
changes/additionalremotequeryneedednow. Awaitclientdetail, kernel source facts
remainversionqualified; node24sourceinferredmasknotused.

## User-requested new Full team bug-proposal session

Created via publicdev-sessionstart with --new --no-attach --teamdelegated and
self-containedtechnicalgoal. Newslug2026-10-20-kernel-bug-fix-proposals,
thread01a15aed-15b5-7621-863c-efb515e257ad.
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-20-kernel-bug-fix-proposals/

[kernel-bug-proposal-handoff.md](kernel-bug-proposal-handoff.md) preserves scope
and exact initialgoal: threebugsolution+verificationproposals, notincidentcause,
noautomaticimplementation/build/merge/livepatch/deployment. Fullteampreset owns
its ownrecords/team; thisrootstillcurrent2026-10-20-kernel-check. Creationexit0
reportedterminalrestartafterAppServerdisconnect andreturnednewslugURLthread.
Noarchive/delete/stop/lifecyclechange tothisinvestigationsession.
Phasecreation/handoffcomplete; proposalworknextinnewsession, no blockersreported.

## New request: complete three-month all-node hard-lockup search

Userexplicitlyrequests allnodes last3months, notsampling. Windowcalendar
2026-07-20T00:00:00+02 throughcollector exactcurrentOct20snapshot. Includesall
identifiednodehierarchy/aliases/compressed/legacyeligibleactualtimestampfiles,
boundaryoverlap/currentcutoffs; inactive/noeligible sourcesreportgaps, notnegative.

| Owner | Expected result | Acceptance / checks | Dependencies |
| --- | --- | --- | --- |
| architect0 | Scope/confidence/design+synthesis | Exactwindow/fullcoverage vsretention gaps | Collectorinventory+finalreports |
| implementer1 | cluster-hardlockup-three-months.md + manifest/status/matches/receipt | Solelowpriorityserialcollector, allselectedfilescomplete, continueafterhits | Centralread-onlyaccess |
| implementer2 | Independentlocalfullcoverage andepisodeclassification | Paths/bytes/identity/cutoff/status/matches/window/dedup | Localcollectorevidence |
| lead | Userupdates/resultacceptance/records | No partialnegative, no policychange | Allreports |

Prior30GiBsamplebudget/firsthitstopdoNOTapply. Read-onlylargecorpusauthorized,
resourceuse remainslowpriority/interruptible withadaptive timeout/resume.
Preferfreshuniformprovenance vs unsupportedpriornode24 reuse. No otherremote
scanner/sourcefetch/config/SysRq/NMI/fault/test/build/merge/deployment.

### All-node three-month inventory milestone

Fixedupper2026-10-20T23:08:52+02, lower2026-07-20T00:00:00+02. Selected
1221files557,248,915,782B(~519GiB),13active sources;13inactive directories
retentionendsbeforewindow aregaps. Fullmetadata3477plainfiles26dirs,no
compressed/symlinks/unexpectedentries, allfirstlastparse/newlineprefixes.
Freshuniformscan, no priornode24reuse. Fastcaseinsensliteral'lockup'+bootlabels
thenlocalhardregex/timestampclassification, serialnice/ionice. Estimateprior
throughput37–42min, measurednewmethodmayimprove. Usernotifiedlongduration.
Artifacts use `cluster-three-month-*`; report: [three-month search](cluster-hardlockup-three-months.md).
A final result requires every selected prefix to complete and independent local
coverage reconciliation. No production configuration or policy changes.

Collection started at 23:10 CEST. At 418.6 seconds, 321/1,221 files and
96,875 MB were complete, with zero hard-lockup mentions. One 30-second timeout
on a 9.724 GB rotation completed on a 60-second retry; no unresolved errors.
Ten current-prefix tails extend fractionally beyond the exact upper bound;
local match classification must exclude records above it. Endpoint selection
does not certify timestamp ordering of every record in excluded old files.
The report is registered in the portal as in progress.

Halfway milestone: at 1,165.8 seconds, 619/1,221 prefixes and
278.400 GB were complete (about half the selected bytes). No hard-lockup
mentions were found; the single resolved timeout remains the only retry.
The final complete receipt, post-inventory and independent acceptance are pending.

### Three-month final accepted result

All 1,221 selected prefixes completed: 557,248,915,782 bytes in 2,344 seconds,
23:10:00–23:49:04 CEST. There were zero hard-lockup mentions or detections.
All 253 unique source-position matches are inside the exact inclusive window:
96 are `softlockup_panic=1` boot-command-line records and 157 are boot/version
labels. No episode exists to classify as survived or recovered.

Implementer2 independently reconciled the complete manifest, raw output,
statuses, timestamps, matches and final inventory. All 1,222 attempts are
accounted for: one 30-second timeout was followed by a successful 60-second
retry, with no partial matches to deduplicate. Stderr is empty; no unresolved
read, identity, extent or status issue remains.

Final inventory at 23:49:11–16 CEST has the same 3,477 paths: no new/missing
paths, all 3,464 fixed files unchanged, and all 13 current device/inode pairs
retained. Their 263,131,061 appended bytes are outside the original prefixes.
All classified matches satisfy the common timestamp cutoff, including checks
of current prefixes whose tail records extend fractionally above it.

Coverage is the available retained records for 13 active sources. Thirteen
other directories have retention ending before July 20 and provide no records
for this window. Endpoint-based selection does not prove timestamp ordering
of every excluded old file. Unforwarded events and undocumented aliases remain
outside the evidence; zero reports does not prove no stall or safe panic policy.

Report: [full three-month history](cluster-hardlockup-three-months.md).
Evidence: [manifest](cluster-three-month-manifest.tsv),
[coverage receipt](cluster-three-month-coverage-receipt.json),
[final metadata receipt](cluster-three-month-final-metadata-receipt.json),
[per-source coverage](cluster-three-month-host-coverage.tsv).
No further collection or source work is needed. No settings, policy, source,
ref, build, test, deployment or session lifecycle changes were performed.
The session remains active and open. Final report/design/synthesis consistency
checks passed; portal report, manifest, coverage and metadata receipts are
registered. Relative links and final newlines pass; the two trailing spaces
inside the report code block intentionally preserve exact search strings.
No additional tracking commit is required under the existing daily cadence.
Next action: user handoff; no remaining collection or investigation blocker.

## October 21: enable hard-lockup panic on all nodes

User instruction: “update vpsfree-cz-configuration to enable hardlockup_panic
on all nodes.” This supersedes prior discussion-only policy boundaries for
configuration source editing. It does not direct a merge or production rollout.

| Owner | Package | Acceptance | Dependencies |
| --- | --- | --- | --- |
| architect0 | Shared-node policy and verification brief in design.md | All compute nodes covered; compatibility/rollback/activation described | Current configuration |
| implementer0 | Isolated worktree, minimal setting, checks, commit, publish and review fixes | Hooks and quick checks pass; exact base/head/history inventory | Architect brief |
| implementer2 | Independent read-only node/import/override coverage check | No missing node or unintended non-node coverage | Brief and patch receipts |
| reviewer0 | Mandatory final review after committed deliverable/checks | General, architecture, scope and risk lanes; whole history/no migrations | Final committed head |
| lead | Acceptance, tracking, portal and user handoff | No implicit merge/deployment; retain open session | All reports |

Risk classification is high because the setting changes host/node crash policy.
A future detected finite stall can trigger a panic; capture still requires
progress through diagnostics and the crash path. Mixed policy during gradual
rollout is compatible and no persisted format/API migration is expected.

Design accepted: one ordinary integer assignment in
`cluster/cz.vpsfree/nodes/common/all.nix`, covering all 12 compute nodes plus
registered storage node backuper2 (13 node consumers; zero unrelated roots).
[Design and verification brief](design.md#all-node-hardlockup-panic-configuration).
Repo-required confctl builds follow quick checks, commit and final review,
using a fresh policy watcher; unexpected local kernel builds must stop.
No per-host changes, force overrides, input updates or induced failures.

Quick validation milestone: actual branch baseline is upstream
`d5c95e9315fb62cf38a172b303527c6553d752ba`, refreshed from the initial
`86e19685` inspection before checks. The sole source diff remains one sysctl
assignment. Format/parse/whitespace and declared bundle checks pass. The pinned
full-module evaluator reports integer 1 and exact generated sysctl text for
all 13 node consumers; aitherdev and int.log controls have no assignment.
Evidence: [effective values](hardlockup-effective.json),
[assertion output](hardlockup-effective-check.log),
[read-only evaluator accessor](hardlockup-eval.nix).
Inventory clarification: 60 cz.vpsfree roots plus 7 org.vpsadminos roots = 67
ordinary configuration roots. No change to org.vpsadminos nodes is intended.
Implementation is awaiting hook-managed commit/final reviewer packet; required
builds remain after review, production unchanged.

Committed deliverable and review packet:

- Repository/worktree: `vpsfree-cz-configuration`,
  `worktrees/2026-10-20-kernel-check/vpsfree-cz-configuration`.
- Feature: `2026-10-20-kernel-check`.
- Reviewed base: `d5c95e9315fb62cf38a172b303527c6553d752ba`.
- Intended head: `8515b68288be7f6c78ed010f93d1424c377973fd`.
- Complete series: one commit, `nodes: panic on hard lockups`; exactly one
  insertion in `cluster/cz.vpsfree/nodes/common/all.nix:63`.
- No migrations, obsolete branch approaches or repeated update streams;
  no dependency/lock/generated changes. Earlier upstream changes are baseline.
- Quick format, parse, whitespace, dependency and effective-value checks pass;
  Overcommit pre-commit/commit-message hooks pass. Clean source tree.
- Independent implementer2 coverage/receipt check passed; no findings.
- Mandatory final reviewer0 assignment submitted with all four lanes:
  general, architecture, scope and risk. Retained independent reviewer settings:
  `gpt-6.1-sol`, `xhigh`, `read_only`; high risk because host crash policy changes.
- All-node confctl builds await final review; no production activation/merge.

Evidence: [verification receipt](hardlockup-verification.json),
[hook/commit log](hardlockup-commit.log). Worktree initialization initially
failed the existing post-checkout hook due to missing gems; native registration
was retried and declared nix-develop dependencies/hooks restored, without bypass.
An initial evaluator function-application invocation failed; corrected command
passed, with failed and successful logs retained in the execution package.

Publication verified by implementer0: SSH remote feature head is exactly
`8515b68288be7f6c78ed010f93d1424c377973fd`; master remains the reviewed base.
The clean worktree comparison was captured natively; repository claim
`7705e877-96de-4d8f-a595-a8f4df22fc19` was explicitly released after Git effects
were verified. [Execution and verification summary](hardlockup-verification.md)
is registered in the portal. Implementer2's final local provenance check passes
all checksum/blob/lock/module-graph and scope comparisons. Final reviewer0 and
required builds are still pending; no runtime setting has changed.

Final review accepted with no findings: retained reviewer0, Sol/xhigh/read-only,
exact range d5c95e93→8515b682, all four lanes, sound complete one-commit history,
no obsolete approaches/repeated streams/migrations. Preserved report:
[final review](hardlockup-final-review.md). Lead accepts review; no remediation.
Required post-review checks are now running under implementer0: a fresh exact
pinned Luna/low utility first checks the build plan, then a separate fresh
utility will own the required all-node confctl build if cache/plan permits.
No build or activation success is claimed yet.

Post-review build-plan check is blocked before substitution/compilation:
missing `/secrets/nodes/initrd/ssh_host_ed25519_key` while evaluating node5
system output. Fresh watcher thread `01a15e2a-4457-7723-9026-9658eaaed74a`,
retained utility Luna/low, explicit full-access policy; dry-run exit 1.
No kernel compile or deployment started. Implementer0 owns bounded
repository-documented prerequisite diagnosis and required-build status; no
secret reads/copies/placeholders, input changes or production access requested.
Effective-option validation/review remain successful; no source edit needed.

### Final source handoff and build limitation

The repository-required command was attempted after accepted review:
`nix develop -c confctl build --yes 'cz.vpsfree/nodes/*'`.
It selected all 13 nodes / 26 outputs and exited 1 after 58.12 seconds during
node5 evaluation, at absent `/secrets/nodes/initrd/ssh_host_ed25519_key`.
`common/netboot.nix` unconditionally references the RSA and Ed25519 initrd keys;
this host lacks `/secrets/nodes`, and repository docs assume provisioned build
secrets without documenting an applicable local retrieval mechanism. No secret
contents were read, copied or fabricated; no input/config workaround was made.

A separate fresh policy watcher owned this actual required invocation:
thread `01a15e2d-2ce1-7051-9380-f57813924c1a`, pinned Luna/low with explicit
full-access execution. It reported no remaining process. No kernel compilation
or cache/substitution conclusion was reached; system build success is unverified.
Evidence: [actual build log](hardlockup-build.log),
[build exit receipt](hardlockup-build-watch-result.json),
[dry-run result](hardlockup-build-dry-run-result.json).

Final unchanged clean head is `8515b68288be7f6c78ed010f93d1424c377973fd`,
reviewed complete one-commit range over `d5c95e93`; SSH feature branch published.
Repository claim released. No remediation edit or review rerun is needed.
The source task is complete with validation limits; it is not claimed fully
built or deployed. Next operator step is to provide a properly provisioned
build environment for the remaining system check, then separately direct
master integration and any runtime rollout. No automatic lifecycle action.

## Superseding instruction: handle hard panic like soft panic in vpsAdminOS

User correction: “move the hardlockup_panic into vpsadminos as well” and
“handle it the same way as soflockup_panic.” The source owner/mechanism now
follows the existing crashdump-enabled soft-lockup boot parameter, rather than
a site-wide sysctl. Architect0 confirms soft is in crashdump.nix under
`mkIf cfg.enable`, `boot.kernelParams`. Linux's recognized hard panic boot
parameter is `nmi_watchdog=panic`, not `hardlockup_panic=1`; the panic token
changes failure policy without enabling or changing detector flags.

| Owner | Package | Acceptance/dependency |
| --- | --- | --- |
| architect0 | Minimal OS-owned brief and compatibility | Same enablement gate/mechanism, exact recognized argument |
| implementer0 | Withdraw former configuration edit | Verify unmerged/unused; clean zero-diff history and SSH branch, no delete |
| implementer2 | vpsAdminOS execution/checks/commit/publication | Written brief first; enabled/disabled real-module values and hooks |
| reviewer0 | Final committed revised-deliverable review | Whole OS series plus zero configuration diff; gates/history/compatibility |
| lead | Acceptance/tracking/handoff | No pin bump, merge, deploy or fault injection implied |

Earlier8515 effective checks/review/build failures remain historical evidence,
not certification of the new OS change. The completed source relocation will
only reach pinned consumers through a later normal OS input update and rollout.
No new downstream pin update is needed for source ownership relocation.

Bounded small-edit lead briefs unblocked the already-decided execution packages
while architect0 finished the durable brief. Written brief is now accepted at
[move policy to OS](design.md#move-panic-policy-to-vpsadminos): OS adds
`nmi_watchdog=panic` adjacent to soft under the same crashdump gate and corrects
the nearby enable-option description (panic response, not detector activation).
Quick actual-OS checks cover enabled, disabled and ordered `nopanic` override;
no VM/fault/kernel build or new evidence subsystem is needed. Configuration
withdrawal is a safe empty-range rebase/owned exact lease after verified unused
preflight; no add/revert residue or default/ref deletion. Both packages proceed.

Configuration withdrawal accepted: clean session feature and SSH remote now
have base=head `37a338b25192d9271ee211110800c2dc6a094a57`, exactly upstream master,
zero feature commits and zero diff. Obsolete8515 was verified unmerged/unused
in session/ref evidence and dropped via empty-range rebase, published with an
exact lease. No add/revert residue, default-branch rewrite or ref deletion.
[Withdrawal summary](hardlockup-configuration-withdrawal.md).
Native comparison cannot capture identical base/head and refused explicitly;
the older captured diff is historical, not current. No replacement/false base
was recorded. Previous8515 checks and review remain superseded history.

OS current committed head `f3e91f6213934bf5d1a2ca52a7fdc6e63941a647`
over staging `252b80dfdb4bced0713e8423ef7ba3d5600d05dd`: one coherent module
change adding the hard panic argument and correcting enable-option description.
[Actual-module evaluation](os-hardlockup-eval.json) confirms enabled gets
both panic arguments once, disabled retains baseline parameters, and mkAfter
nopanic appears later. No global hard panic sysctl added. Hooks/format/parse
passed per implementer2; final packet/publication confirmation pending before
independent final review of replacement (old site-only review cannot certify it).

OS publication verified by implementer2: remote feature
`f3e91f6213934bf5d1a2ca52a7fdc6e63941a647`, upstream staging remains
`252b80dfdb4bced0713e8423ef7ba3d5600d05dd`; clean source blob
`13e9b1f7371b2c98c19429e44f5173c6b1af134a`. One commit / one module,
no obsolete OS history, migrations or dependency/update streams.
[OS source/check packet](os-hardlockup-verification.md) registered in portal.
Reviewer0 retains saved independent Sol/xhigh settings and all four lanes for
new final committed review; previous8515 review does not certify replacement.
Automatic GitHub CI started for exact OS head, run39598560664; implementer2
owns a fresh policy watcher's observation and any failure diagnosis. No extra
workflow/local kernel build/deployment started by the lead.

Revised final independent review completed: same retained reviewer0 Sol/xhigh,
all four lanes, high risk. Source/semantics/configuration withdrawal accepted.
One Important finding: OS local patch-series policy requires a validation
account in the commit body, omitted from f3e91f6. Lead accepted local-policy
requirement and delegated message-only amendment to implementer2. No source
change, extra behavioral check or full review rerun is required; step9 direct
remediation will verify tree/blob/parent identity, hooks, publication and CI.
[Preserved review](os-hardlockup-final-review.md). Old exact-head CI is being
reconciled with the replacement-head observation; no deployment started.

Message-only review fix accepted by lead: new final OS head
`b81c43ff6865a033268072f55cd94ad763d0630b`, same parent252b80df,
exact reviewed tree3585d2ce/moduleblob13e9b1f737; full source diff old→new
empty, clean worktree. Body now includes required concise validation prose;
hooks pass, SSH published. All final findings resolved under step9, no full
rerun or additional source checks justified. New exact-head automatic CI
run39600028637 follows old39598560664 cancellation; implementer2 owns watcher
and diagnosis. Downstream pins/config defaults/runtime remain unchanged.

CI lifecycle update: superseded run39598560664 reached completed/cancelled,
old observer ended. Fresh retained utility follows only final-head run39600028637
at b81c43ff; no duplicate workflow or parent polling. No source change or new
local build/test was launched. Source worktrees and defaults stay unchanged.

### OS source handoff, automatic CI still owned

Source implementation is complete, published and reviewed with all findings
resolved; quick enabled/disabled/ordered-override module checks and hooks pass.
No further local check, source edit or review is selected. The automatic
pipeline is broader: run39600028637, exact b81c43ff, job119221889153 “Build OS
and populate binary cache”, followed by dependent test-suite/livepatch jobs.
At the last owner report, container-image repository module, guest/generated
flake, and squashfs flags/wiring checks passed; persistent activation and
remaining build stages were unfinished. No failed step reported. Duration is
uncertain; no ETA/deadline/cancellation inferred.

Implementer2 and its fresh retained watcher continue to own this existing run;
there is no duplicate observer/workflow. CI completion is not claimed. If a
failure occurs, implementer2 retains diagnosis/fix ownership and must notify
lead, preserving first-failure evidence before retry. This handoff does not
finalize/stop the session or any operation. No default-branch integration,
downstream pin update or runtime change occurred. Stable portal remains:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-20-kernel-check/

### Automatic CI: OS build milestone passed

Existing watcher reports final-head run39600028637 / b81c43ff,
job119221889153 “Build OS and populate binary cache” passed in 14m40s.
Preliminary compatibility, persistent activation, disk-image reuse and ZFS
parity checks, top-level closure build and cache publication all passed.
Dependent product tests/livepatch jobs remain pending; overall CI is not yet
terminal. No failure or source fix reported; implementer2 retains the existing
watcher. This is build/check evidence, not downstream adoption or deployment.

### Automatic CI: product test failure escalation

Existing watcher reports run39600028637 at exact
`b81c43ff6865a033268072f55cd94ad763d0630b`: Run test suite,
job119228578900 failed after3h36m46s. Five jobs passed, five livepatch jobs
unfinished. Failed-test/stage relevance is not established yet. Implementer2
is preserving failed attempt logs/artifacts and diagnosing against actual guest
configuration/source; no blind rerun, source edit or new test has been started.
Current exact-head run stays owned, with no duplicate workflow/status observer.
Next action is a bounded failure diagnosis and justified corrective step, then
continued CI reconciliation. Source review/quick checks remain valid evidence
but do not certify this failed automatic test stage.

### Accepted first-failure diagnosis

[Native failure analysis](os-hardlockup-ci-failure-analysis.md) reviewed and
accepted. Product runner:129 tests/337 scripts,124 tests passed and five
unexpected failures, all upgrade/from-6.12 or6.18 guest variants. Every first
failure is `assert_retained` at tests/suite/upgrade/common.nix:1534: expected
saved `tank/ct/niximpermanent.impermanence-<suffix>`, reported base
`tank/ct/niximpermanent` after successful live userspace activation. The same
old kernel, boot ID, booted-system link and container init process persist.
Thus the new kernel boot argument was never parsed in these failures; this is
execution-path exclusion, not an inference from a small diff. No policy fix
or blind rerun is justified. A secondary teardown timeout follows one assertion.

Run-state API export/load fallback explains the reported base-dataset form,
but exact runtime-loader cause and actual mounted ephemeral root are unknown:
uploaded artifact lacks relevant runtime YAML bytes/mount proof. Do not claim
baseline reproduction, data loss or harmlessness. Full failed log and950-member
native ZIP retained with matching uploader SHA256; no CI retry/source edit/new
test was performed. Lead selected no broader loader audit or diagnostic run
for this task. Current CI remains failed; remaining jobs stay under existing
watcher. Next action: retain final CI results and keep the policy branch
unchanged unless new evidence justifies a scoped correction. No merge/pin/
deployment/runtime/lifecycle action was authorized or performed.

### Terminal CI accepted, October 22

Local final metadata confirms run39600028637, head
`b81c43ff6865a033268072f55cd94ad763d0630b`, status completed / failure,
updated2026-10-22T01:11:10Z. All11jobs terminal:10success (OS/cache and all
nine livepatch lifecycle jobs),1failure Run test suite119228578900. The last
AMD-fresh job119228579002 passed in1h32m17s, completed01:11:09Z.

Product result remains124passed/5failed; the accepted native failure analysis
lists all five variants, including both v1 cases. Watcher abbreviated examples
do not replace full-job/artifact diagnosis. Same predecessor boot identity
proves the new boot argument was not parsed in those five first errors; exact
run-configuration/mount-root cause remains unknown. No policy edit or blind
rerun selected. CI must not be represented as green or full-test success.

[Final CI metadata](os-hardlockup-ci-new-result.json),
[all-job log](os-hardlockup-ci-new-jobs.log),
[accepted failure analysis](os-hardlockup-ci-failure-analysis.md).
Implementer2 reports watcher completed (CLI0 / gh-watch1); no owned running
CI/observer or verification handle remains. Monitoring ended naturally;
no session lifecycle action or current-head cancellation performed. Final
plain packet/design/synthesis have been reconciled with this terminal receipt.
Next action: hand off published source and exact CI limitation. No automatic
integration/downstream adoption/deployment or further diagnostics are selected.

Final handoff record reconciled: implementer2's completed verification packet
and architect0's design/synthesis agree with final metadata and all five native
failure cases. Relative artifact links/whitespace/final newlines checked. Final
metadata is registered in the portal. No remaining monitor, rerun or source
repair is selected. Session stays active/open; source remains published,
reviewed and unmerged, with the explicit failed-suite validation limitation.

## October 22: runtime sysctl plus hard-lockup boot-argument comment

User: the boot-only solution does not enable panic on running systems; add
sysctl parameters and a comment identifying the hard-lockup boot argument.
Same OS crashdump ownership and enable gate are intended; retain boot coverage.
Architect0 owns concise boundary/design, implementer2 owns OS source/checks/
commit/review fixes/publication, implementer0 independently traces current
sysctl service/activation lifecycle. Lead owns acceptance/records/reviewer0.
No site-config duplicate, detector change, general sysctl framework, unrelated
upgrade failure fix, runtime write or deployment is selected.

A `boot.kernel.sysctl` declaration must not be represented as proof that a
running kernel was changed. Establish actual live switch/reload behavior and
report any remaining explicit application step. High risk remains host failure
policy; all enabled/disabled/override semantics and native runtime override
must stay reviewable. Earlier CI had ten passed jobs and five product-test
assertion failures, whose execution path excluded the old new-boot argument;
that exclusion does not automatically certify a new runtime-sysctl path.

Runtime scope decision: independent source trace confirms boot-only runit
stage1 `sysctl --system`, no runit sysctl service, and no sysctl replay during
live switch/test. Declaration alone is not live-complete. Lead accepted the
smallest existing mechanism: crashdump-gated system.activationScripts for only
the final merged hardlockup value, explicit procps command, ordered after
specialfs, preserving override0/null omission and default dry-activation
exclusion. No replay of unrelated sysctls/new service/general switch refactor.
Architect/i0 finalize generator failure visibility/order contract; i2 owns
implementation and checks without writing the host kernel. Activation precedes
crashdump-service start and cannot certify an already-loaded crash image.

Runtime implementation committed: new head
`10f31e04c41c4a542c678faf3eb2038578367752` over unchanged staging
`252b80dfdb4bced0713e8423ef7ba3d5600d05dd`. Whole feature is one coherent
v2 commit, one crashdump module(+19/-1), no migrations/repeatedstreams/inputs.
Tree d402031bdc82325939f9d8003e169f1984086271 and moduleblob
80566cb122af59df22540c195ea11de203b584ee; clean worktree. Prior b81c
unmerged iteration folded into owner, exact backup/historical receipts kept.

Quick actual OS evaluation covers enabled/disabled/override0/null/false,
generated sysctl text, existing bootargs, activation ordering after specialfs,
and full dry-script exclusion. Isolated generated-wrapper mock checks exact
key/value and success/failure aggregate status, with no host sysctl write.
Format/parse/whitespace/bundle/hooks passed; normal -F commit includes required
validation prose and v1/v2 development history. Evidence
[quick log](os-hardlockup-runtime-quick.log),
[actual graph](os-hardlockup-runtime-eval.json),
[mock outcomes](os-hardlockup-runtime-mock.log),
[commit hooks](os-hardlockup-runtime-commit.log).

Final reviewer0 assigned real new turn, retained read-only Sol/xhigh, all four
lanes at high risk; final source/runtime behavior/history acceptance pending.
No new local build, VM/fault test or unrelated upgrade repair selected.
Publication and automatic current-head CI will be reconciled independently;
old b81c CI cannot prove this new runtime activation path.

Publication baseline refresh: upstream staging advanced to
`55c5046514d06fe9398a022c1622bdaae5228841`, changing only flake.lock
nixpkgs_2 cd4ea8d→da6dc0e7. No source/activation/sysctl overlap; implementer2
owns clean rebase, patch-equivalence and affected real-module checks. Reviewer0
has no source finding so far and holds final freshness acceptance for that
new tuple/evidence, within the same review turn. No duplicate evaluator/CI.
Normal pre-rebase hook signature refusal is being resolved in the declared
environment without bypass. No shared/default history mutation occurred.

Withdrawal freshness: configuration branch remains frozen zero feature range
37a338b2..37a338b2. Today's origin/master has advanced to38e7c837; do not
claim that the withdrawal branch equals today's default. This does not
reintroduce the withdrawn setting or require unrelated configuration updates.

Final refreshed tuple supplied to reviewer0: base55c5046514d06fe9398a022c1622bdaae5228841
→ head14cdf1caec606bb6bc88fcb32ac48f707f5dabb0, tree70b0e11688686a490d5d81c96bba03250ec9f333,
same moduleblob80566cb122af59df22540c195ea11de203b584ee, one coherent commit,
clean. Range-diff old10f31 policy patch equals14cdf. Real full-graph enabled/
disabled/0/null/false, generated snippets/sysctl/bootparams equality across
rebase, specialfs order/dry exclusion, isolated mock arguments+failure status
all pass on refreshed input. Prerebase receipts retained; native comparison
captured exact final range. Publication next; review in same active turn.

Reviewer Advisory provenance finding accepted: i0 lifecycle note mislabels
historical b81c root Nixpkgs as e4bae1bd, which is a nested node. Exact root
inputs.nixpkgs→nixpkgs_2 at b81c selects cd4ea8d57de16f4810bc5f14207bac45fbf19f67.
Substantive no-live-sysctl proof already traced that source and remains valid.
I0 owns a documentation-only correction; lead will verify before handoff.
No new evaluation/source test/runtime action is justified by this label fix.

Fresh publication verified: SSH feature14cdf1caec606bb6bc88fcb32ac48f707f5dabb0,
staging55c5046514d06fe9398a022c1622bdaae5228841 unchanged, exact lease fromb81c
and normal hooks pass; source clean. Two automatically triggered exact-head
workflows are pending: CI39744127896 and RSpec39744127815. Implementer2 owns
one fresh retained Luna/low watcher for the existing related batch, no manual
workflow/duplicate observer. Source handoff need not await the whole broad CI;
state must explicitly retain pending status and no full-green claim.

Advisory evidence correction verified by lead: hardlockup-sysctl-lifecycle.md
now labels b81c root/site Nixpkgs cd4ea8d5 correctly, and e4bae1bd as nested
impermanence-only corroboration. Same no-live-apply conclusion, no source or
check change. Reviewer0 has the corrected evidence and final published tuple.

Runtime final independent acceptance: reviewer0 allfourlanes on exact
55c504→14cdf, highrisk, no findings after direct Advisory provenance closure.
[Preserved final review](os-hardlockup-runtime-final-review.md). Ref check
confirms clean HEAD=SSH feature14cdf and staging55c504. Lead accepts source,
checks and whole-history/migration conclusions; no remediation remains.
New CI/RSpec remain pending; current policy hasn't been deployed/applied on
hosts and switch exit alone cannot prove readback. Source handoff is ready
with these explicit limits, separate merge/deployment approval still required.
No broad verification or rerun is selected by the lead; implementer2 retains
existing automatic workflow batch and failure diagnosis responsibility.

Source handoff finalized: architect design/synthesis agree with final14cdf
publication/review, evidence links/whitespace/newlines checked, portal packet
and final review registered. Fresh exact-policy watcher `/root/os_runtime_ci_14cdf`
confirmed owned batch CI39744127896 and RSpec39744127815 for14cdf, retained
Luna/low/fresh context/full-access policy verified; per-run watch logs/exits
captured. Implementer2 retains terminal/failure follow-up; no second observer.
Both workflows pending, no automatic success/deployment claim. User handoff
reports configured activation plus mandatory runtime readback on any future
rollout; session left open and feature remains unmerged.

## User-directed simplification: ordinary hard and soft sysctls only

User rejects the custom system activation script and explicitly asks to set
kernel.sysctl for both hard and soft lockups. Direct bounded lead brief to
implementer2: remove hook/helper/activation-specific description, retain boot
arguments and NMI comment, ordinary integer1 for hard+soft sysctls under same
crashdump gate. No generic service fix or alternate activation mechanism.
Architect0 reconciles concise design/synthesis; no new investigation needed.

User's NixOS comparison answered: its systemd-sysctl service restart trigger
on generated config applies changed values at switch; imported compatibility
attrs are inert under vpsAdminOS runit. The simpler requested declaration-only
implementation does not close that OS live-switch application gap. Do not
claim it updates a running kernel automatically. No runtime write or deploy
has occurred. Existing14cdf CI/watchers must be reconciled as superseded only
after replacement publish, preserving exact heads/failure evidence and no
orphan observer. All new behavioral changes require committed final review.

## Generic sysctl live-switch solution proposal requested

User accepts the NixOS/runit distinction and requests a suggested generic
vpsAdminOS solution for sysctl updates during configuration switch. This is a
new design-proposal task, not authority to implement another mechanism yet.
Architect0 owns a concise source-supported generic recommendation and boundaries;
implementer0 independently checks existing runit one-shot/restart-trigger and
switch ordering/error contracts. No new source mutation/test/CI observer in
those lanes. Implementer2's prior authorized declaration-only panic cleanup
continues independently, with no generic service/hook code added.

The proposal should make `boot.kernel.sysctl` work through one OS-owned generic
path, compare existing runit service triggers versus activation, preserve boot
stage1 timing, cover switch/test and nonmutating dry activation, state failure
visibility and removed-key/runtime-reset limits, and define proportional tests.
If later implemented, generic infrastructure should be a separate logical
commit from panic-policy declarations. No new daemon, watcher or polling
framework is justified. No runtime/production operation was authorized.

Generic proposal refinement: i0's final read-only
[contract comparison](generic-sysctl-contract.md) identifies service-specific
stale-marker/retry/runlevel/protected-service complications. For synchronous
switch/test application only, a checked generic step after successful activation
and before service restarts is smaller than a new service. Lead asked architect
to prefer that approach unless concrete incompatibility, preserve early stage1
boot apply, skip dry/boot-only, and decide every-switch versus changed-only /
all-system input scope. Proposal only, no generic implementation authorized.

Declaration cleanup separately committed/published v3 at
8528262315b0794a8f50917cf33c53a07fd14030 over55c504, one coherent owner,
sole module+7/-1. Hard+soft ordinary sysctls, no activation hook/helper, retained
bootargs/comment. Actual enabled/disabled/paired0/null/nohook checks/hooks pass.
Reviewer0 assigned affected final all-four-lane review on complete v3 history;
publication/current CI follow-up owned by implementer2, no full-green claim.

Final declaration-only source acceptance: reviewer0 Sol/xhigh/read_only, all
four affected lanes on exact55c504→852826, no findings. [Review](os-hardlockup-v3-final-review.md).
Published clean single v3 owner, paired declarations/no custom activation;
actual enabled/disabled/paired0/null/generated/nohook checks and hooks pass.
Source status distinct from generic proposal and pending automatic CI.

Generic recommendation accepted for USER PROPOSAL ONLY: generate an explicit
procps `sysctl -w --system` helper in the new system closure; invoke every real
switch/test after successful activation installs new/etc and before changed
service restarts. Keep early boot stage1 apply and skip dry/boot-only actions.
No new runit service, trigger registry, marker or retry loop. Complete normal
service restarts/recovery after a sysctl error, then return nonzero; failed
activation prevents application against uncertain/etc. All existing sysctl-file
precedence applies, unchanged configured values overwrite manual live overrides,
removed keys remain unchanged and partial writes have no automatic rollback.
Future implementation is a separate logical commit with focused ordering/error
specs and one benign disposable live-switch test after approval. No generic
implementation, runtime write or new test has been launched for this proposal.

Old14cdf workflow accounting complete by implementer2: RSpec39744127815
passed naturally (watch0); CI39744127896 was verified stale and cancelled
after852826 publication (watch1), no reported failed test before cancellation.
Old watcher ended/no owned processes remain. New852826 CI39745935323 remains
pending under fresh retained watcher launch; no duplicate workflow/observer.
No old successful or cancelled check is presented as current-head evidence.
