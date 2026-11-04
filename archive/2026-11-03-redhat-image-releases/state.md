---
lifecycle: archived
---

# Red Hat-family image releases

## Current status

Phase: COMPLETE. Requested release updates and approved source-identity fix are
reviewed, verified and integrated. Post-push feedback is accepted; no owned
operation or remaining delivery/review/CI/deployment/approval action. Session stays open.

- Exact final source: `54b4313404cea35b58ebb9df951ae75e27c44971`, tree
  `5c03648e084e907957b37263846bc5763abdac1f`, merged normally over SSH into
  staging. Fresh completion fetch/SSH proof finds default
  `2951a632c4254a44747a8da326e3dde897eaa0e2`; final54 is its ancestor.
  Results below are for54, not a claim of verifying later default commits.
- Four image-specific commits update CentOS Stream9/10 and Rocky9/10 RPM suffixes;
  eight other inventoried recipes required no update. Two separate correction
  commits preserve captured source identity and tolerate unknown channel revision.
  Full-range independent review/no-migrations accepted; no source edits after review.
- Actual staging54 post-push results: core109tests/323scripts PASS, zero failed or
  unexpected outcomes; four required images PASS at normal24GiB; RSpec13components /
  3297examples/0failures; RuboCop PASS. Focused full14/native6 kernel group also
  passed, including misc-attrs; no claim the earlier intermittent ESRCH race is fixed.
- Generic41822392601 terminal COMPLETED/FAILURE16:25:20UTC: nine lifecycle raw
  logs match the unchanged pre-existing vg23drv/kmm41output fixture build failure,
  before assertions. These remain FAILED, not passes. Expected hash retained;
  underlying checksum/read cause remains unknown and outside this update.
- One provider metadata inconsistency retained: final job-list/targeted amd-fresh604
  still says in_progress/no conclusion despite terminal workflow and its full failed
  log/artifact. No fabricated job completion or extra polling to force agreement.
  Image original full native reply unavailable; wrapper0/finalsuccess/rawcasepasses
  independently prove image outcome. Generic authentic original reply recovered:
  chunk23c34a/exit1/no session_id/full4668char output, matching terminal workflow.
- Lead checked exact terminal run/head, all9 raw failure signatures and94-entry
  complete log ZIP SHA; all original observer PIDs absent. Owner confirmed no
  operations remain. Earlier failed/blocked attempts remain historical evidence,
  never relabeled passes or input-equivalence proofs.
- Both repository claims released/verified; successful retry11:36:33–11:37:27UTC.
  No physical deployment/machine claim. Only disposable merge checkout removed;
  feature worktree/local+remote refs and recovery/evidence retained. No archive,
  delete, stop, private lifecycle helper or delayed session cleanup performed.
- Owning framework docs: docs/os/test-framework-integration.md, included in reviewed
  source. Existing release guidance sufficed for RPM-only bumps. Reusable environment/
  observation notes retained; no product/KB publication or coordinated node update.

[Final CI evidence](post-merge-ci-result.md), [integration proof](merge-result.md),
[focused kernel](kernel-group-verification-result.md), [review](review-result-refresh.md),
[original diagnosis](root-cause-report.md). Earlier checkpoints below are historical.

## Phase checklist

- [x] All-family upstream inventory and design accepted
- [x] Four image-release commits and source-identity/channel fixes
- [x] Focused Ruby/Nix checks, hooks and independent review; findings resolved
- [x] Four local and four native-CI image tests at original final head
- [x] Original exact-head core CI passed 109 tests; baseline failures disposition
- [x] Patch-equivalent refresh and independent full-range review
- [x] Refreshed54b43134 image CI passed all4 required cases (plus4 upstream)
- [x] Refreshed exact-head RSpec3297 examples and RuboCop passed
- [x] Exact-base openSUSE failures diagnosed and accepted as unrelated FAILED checks
- [x] Focused CI full14/native6 kernel group accepted; prior ESRCH preserved/not fixed
- [x] Final exact-head verification accepted with explicit failed-check dispositions
- [x] Final54 fast-forwarded into remote staging; exact remote/ancestry verified
- [x] Integration evidence retained; source refs/session remain open
- [x] Post-push actual core109/images4/RSpec3297/RuboCop passed
- [x] Terminal lifecycle feedback accepted with explicit failures/metadata limit; no owned operation

## Authorization and scope

Initial user request: update Red Hat-family releases in vpsadminos;
"when verified, you can merge it." After root-cause diagnosis the user approved
"aha I see, implement your suggested solution and continue". This resumes
verified staging integration including the proposed source-identity and channel
corrections. No other repository, kernel project, SSH timing change, downstream
pin update or production deployment is in scope.

## Repository and original tested history

- Bare clone: `repos/vpsadminos.git`, SSH origin
  `git@github.com:vpsfreecz/vpsadminos.git`.
- Feature worktree: `worktrees/2026-11-03-redhat-image-releases/vpsadminos`.
- Clean detached merge checkout prepared at
  `worktrees/2026-11-03-redhat-image-releases/vpsadminos-merge-target`, base
  `742eb30cb1a8b6766c85e915d26b0400e38244b1`; hooks validated after base-only ff.
- Native comparison recaptured at54b43134 against742eb30 before integration.
- Refreshed final six-SHA mapping and patch proof: [refresh-result.md](refresh-result.md).
  Original tested series below is historical evidence, not the refreshed ancestry.

Complete original tested series (before patch-equivalent rebase):

1. `09f209688616b60155e9ac99fa8431a11b9e20a0`: CentOS Stream 9, release 36→38.
2. `a3c7c77459762d1a45f323de0f3f8dd5d8447323`: CentOS Stream 10, release 21→23.
3. `6ede3bd22b2ed28fb28a5a912f3a7daf7743fb6a`: Rocky 9, release 1.1→1.2.
4. `3307df52ea5bf875e1d8a23318a64f569d8b3ebc`: Rocky 10, release 1.1→1.2.
5. `52fba5ee5aac2e171375a780d3860a86e71e5d65`: nullable channel consumer.
6. `1a637e9eac4311adba2b08d60dfa7a17d07bcb52`: captured source identity.

Eight other image recipes were already current. No migrations, repeated update
streams, obsolete approaches or repair commits remain. Four image commits retain
the required split. Parent of the metadata owner remains channel commit52fba5ee.
See [CentOS result](centos-result.md), [Rocky result](rocky-result.md),
[channel result](channel-result.md) and [metadata result](metadata-result.md).

## Review and focused acceptance

Same independent reviewer0, saved gpt-6.1-sol/xhigh/read_only, reviewed all four
lanes at base `dd188397` through original metadata head
`58aae8d54887a14f59fada178a833b33a6ebfa81`. High risk classification for framework
compatibility/provenance and generated OS metadata. See
[expanded packet](review-packet-expanded.md) and
[expanded report](review-result-expanded.md).

Two findings were corrected within the reviewed boundary: legacy Git defaults
now have priority1100 below known-source defaults1000 and explicit settings100;
security evidence honors authoritative/explicit revision rather than copied Git
HEAD. Real-module regressions cover capture A with copied HEAD B, full/short/null
overrides, native provider identity and legacy fallback. The original conflict
was reproduced before correction. Lead inspected the exact two-file narrow fix,
then accepted it under the review skill without an automatic full rerun.

Old/new heads and exact diff are retained in metadata-result.md and
[metadata-review-fix.patch](metadata-review-fix.patch), SHA256
`41e5e7e4c8316eab34a08b68cc06df2b6e1ebcddcc9404398a2fd979ce3c8789`.
Old head is retained at exact-session local backup branch
`2026-11-03-redhat-image-releases-reviewed-metadata`; it is not claimed integrated.

Focused checks: 42 Ruby examples pass; source-version and real known/null channel
Nix checks pass, including final real-module evidence regressions. Final hooks
Nixfmt/RuboCop/commit message and committed whitespace checks pass. Ruby source
unchanged by narrow Nix corrections. Native libosctl dependency, shell commands,
logs/hashes and reviewed/final mapping are in metadata-result.md. Existing CI
launcher packages the updated local runner Ruby; no packaging/workflow fix needed.

## Final normal verification batch

Artifact [verification-memory.nix](verification-memory.nix), SHA256
`adef87cd3c928b4a5687150fc5a43f271e64f1fceeb64745bcc4639aad62b582`, contains only:

```nix
{ config, lib, ... }:
{
  boot.qemu.memory = lib.mkIf (lib.hasAttrByPath [
    "boot"
    "zfs"
    "pools"
    "tank"
    "datasets"
    "image-scripts/build"
  ] config) (lib.mkForce (8 * 1024));
}
```

Architect rationale/limits are appended to [design.md](design.md). This is a
supported resource-only test environment; peak sufficiency is unmeasured, all
assertions/timeouts remain, and no 24 GiB success or kernel diagnosis is implied.
OOM and actual failures still require investigation. No reserve bypass.

Normal local-code invocation uses `nix develop .#test-runner --command env`,
sets native RUBYLIB inside the command (the shell overwrites an outer value),
sets exact `TEST_RUNNER_REPO_REV`, sets only the memory VPSADMINOS_CONFIG above,
and runs all four `image-scripts/test@...` cases with `--jobs 2 --stop-on-failure`.
State: `/tmp/redhat-image-releases-2026-11-03-verified8g`.
Logs/result: verified-image-tests.log and verified-image-tests-result.md.
The utility records exact command, generated resource requirements, captured
source, system/kernel/input paths and per-case results. Source-info metadata is
produced by the real runner; no manual source metadata override is used.

Source-only final push did not trigger the image path filter, so image workflow
41695651867 was dispatched explicitly at final head. Superseded old-head image
run41683688934 was cancelled; no other branch workflows were cancelled.

## Earlier failures and diagnostics

- Original linked-worktree evaluation failed before boot with
  `cannot coerce null to a string: null`. Cause and approved correction:
  [root cause](root-cause-report.md),
  [detailed diagnosis](verification-diagnosis.md). Resolved by committed code.
- First fixed 24 GiB normal batch reached VM startup but was interrupted after
  kernel watchdog warnings; three cases never started. This was not an RPM
  failure. [Result](fixed-image-tests-result.md), artifacts under
  fixed-image-test-artifacts/centos-10-stream. Exact children were stopped.
- First cached diagnostic was incorrectly stopped by its watcher after57s,
  before a watchdog event. Parent acknowledged and corrected stop conditions.
- Longer cached diagnostic reached root shell after slow boot, with no watchdog
  trace. Its later checkout check failed because the shared source was unrooted
  and GC collected it during the diagnostic: deletion20:08:32, mount20:14:11,
  guard failure20:14:15. The guard correctly checks required directories, not
  Git metadata. [Observation](boot-observation.md),
  [trace result](boot-trace-result.md). No guard weakening or kernel/security
  change was needed. Normal CLI source lifetime covers the whole batch.
- No diagnostic counts as a passing image test. Historical Fedora45 GitHub null
  error was not found in retained attempts; the located SSH failure is separate.

## Next action and retention

Architect diagnosis is complete: seven openSUSE failures are exact-base and
unrelated; LXC attach error remains unresolved. Implementer2 owns one unchanged
full kernel-group repeat (14 scripts, six concurrent workers), with native resource
admission and fresh watcher. Preserve prior failures and passing evidence. After
result acceptance, fresh-check staging and complete final history before integration.
The original1a four-image/core results are completed evidence, not pending or
relabeled successes. No new merge approval is required. Read the
selected runtime coordination guide before the approved merge. Prepare hooks
outside ownership; acquire one short repository claim only for fresh target
check, fast-forward merge/hooks, SSH push and remote proof, then release before
CI/records/cleanup. Preserve unrelated shared workspace changes and all feature
refs. No machine deployment/claim is needed.

Useful project documentation is docs/os/test-framework-integration.md; session
plan/design/evidence own temporary verification instructions. Reusable setup and
cached-lifetime lessons are in
notes/vpsadminos/2026-11-03-local-runner-verification-environment.md.
Retain compact evidence; stop owned processes natively before removing disposable
test data. No archive/delete/stop or delayed session cleanup is authorized.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-03-redhat-image-releases/)

## Memory metadata setup failure

Global mkForce8GiB conflicted with a separate fixture's mkForce4GiB during
metadata-all evaluation, before any selected case. Receipt final-image-tests-result.md,
full final-image-tests.log retained. This is not an app/image failure. The
operational override will select only the image suite using its existing
`boot.zfs.pools.tank.datasets."image-scripts/build"` marker. Require successful
normal metadata/list evaluation, four8GiB resources and unchanged non-image
fixture before launching a fresh batch. No global stronger priority or new test
framework. Old dbb827... override hash is superseded, not current accepted input.

## Progress response verification-setup-churn

Concern accepted: premature cached diagnostic stop, unrooted cached source and
unscoped memory override caused setup churn without an image pass. Each cause
is now resolved operationally; no further setup/kernel/source expansion planned.
Scoped metadata preflight PASSED99s with selected8192 and preserved4096 fixtures.
One normal rooted four-image batch launched at unchanged reviewed source. Next
observable milestone is first completed per-image result, then allfour results.
Concern resolved after actual CentOS9/10 image passes in the normal rooted batch.

## Image verification milestone

Normal scoped8GiB batch delivered successful CentOS Stream9 (1299.36s) and
CentOS Stream10 (1300.69s) at exact final app head. Both actual image commands
and assertions passed, clearing prior source-evaluation/diagnostic-setup issues.
Rocky9 and Rocky10 admitted next in same rooted invocation, each8GiB RAM/shm,
4CPUs. No setup or source changes; source root remains held across whole batch.
Progress response verification-setup-churn resolved with two delivered image
passes. Remaining: Rocky9/10 results and relevant exact-head CI before merge.

- Rocky9 passed in1391.3s. Normal batch now3 successes/0 failures; Rocky10
  still active. No source/configuration changes during verification.

## Ready pending external CI

CentOS9/10 and Rocky9/10 all passed:1299.36s,1300.69s,1391.30s,1415.45s.
Normal rooted batch exit0, total2716.16s. [Receipt](verified-image-tests-result.md)
and verified-image-tests.log retain evidence. Scoped module hash stayed
adef87cd3c928b4a5687150fc5a43f271e64f1fceeb64745bcc4639aad62b582.
Fresh fetch confirms staging stilldd188397, final feature1a637e9e clean; complete
six-commit series and whitespace inspected again, no migrations/obsolete streams.

RSpec41695511664 and RuboCop41695511719 passed. Image41695651867 and generic
CI41695511680 remain QUEUED at final head. No approval is missing: integration
is already authorized. Native CI utility will observe queued workflows and
notify lead automatically; resolve any concrete failures before integration.
Do not hold a repository claim while waiting for CI or ask user to restart.
After success, prepare hooks outside claim, recheck target/head/history, capture
comparison, acquire short vpsadminos repository claim, ff-only merge/SSH push/
remote proof and explicit release. Leave session open and preserve feature refs.

## External queue handoff

All implementation/check evidence checkpointed in workspace commit5bac395ed.
Fresh utility `/root/ci_wait` (pinned Luna/low/full_access) now owns observation
of existing exact-head image41695651867 and generic41695511680. No local tests
or VM processes remain; no repository/machine claim held. Only external CI
queue remains, so lead yields instead of polling or requesting new approval.
Monitor will report substantive outcomes. Automatic restart of an ended lead
turn was not verified; lead remains active to receive the report, handle any
concrete failures, then perform approved staging integration.
Lifecycle stays active; no archive/delete/stop/cleanup action is implied.

## Monitor wake-up correction

User challenged whether an active monitor existed and whether it would wake the
lead after final. Verified `/root/ci_wait` running and native gh watch PID2107515
alive; generic CI transitioned to running, image workflow still queued. However,
a live subprocess and collaboration progress messages do not prove a durable
lead-turn restart after final. The automatic-resume promise was unverified.
Lead acknowledged this and is keeping the turn active until the CI outcome;
existing watcher reports directly, with no runtime changes or identity workaround.

## CI failure investigation

GenericCI41695511680 progressed through toplevel build/cache, then matrix jobs
amd-low-memory-v5 (126191147517) and amd (126191147584) failed building
livepatch_7-exact-candidate.ko; run still active. Exact logs ci-job-126191147517.log
and ci-job-126191147584.log, small artifact ci-artifact-126191147517. Missing
test.log is a later consequence; cause not yet classified. Architect0 owns
bounded read-only comparison with baseline evidence/derivations before any
source edit or rerun. No kernel project/automatic baseline waiver. Image workflow
41695651867 has completed OS/cache build and advanced to detection/helpers.
Lead remains active; /root/ci_wait observes existing jobs, no claim held.

## Accepted baseline CI failure disposition

Architect report [ci-failure-diagnosis.md](ci-failure-diagnosis.md) proves current
AMD and AMD-low-memory-v5 failures match same-platform baseline dd188397 jobs
126034272312/126034272155: exact same
vg23dzka1i0dw28fy3kl4wssyms484yx-livepatch_7-exact-candidate.ko.drv and
kmm41zgxg3ai8r84jqm2mk02r4py6cdv output, pre-runner fixture build exit1.
Related workflow/fixture/kernel recipes/base config/flake.lock unchanged.
This establishes unchanged declared recipe/inputs and no source-fix link.
Root accepts these as pre-existing failures for this feature's check disposition,
NOT as passing tests. No hash update/retry/kernel project is in scope.
Exact underlying checksum/read failure remains unobserved (--status suppresses
it); any fixture-contract repair belongs to separately scoped work.
Continue generic Run test suite and image workflow; collect any distinct failure.
No repository claim held, root remains active for outcome/integration.

- Intel representative v5/v6 CI jobs126191147695/126191147819 also failed;
  v6 rawlog ci-job-126191147819.log shows same unchanged vg23dz... fixture.
  This matches established baseline disposition, not a new source regression.
  Generic Run test suite126191147285 remains running; plain Intel126191147653
  and image-test job remain queued. Watch observers now use30s intervals
  (PIDs2464930/2464931 at restart); no CI runs were cancelled/retried.

## CI duration reassessment

[Duration checkpoint](ci-duration-checkpoint.md) establishes no elapsed-time
stall evidence: exact-baseline job126034272635 took4h10m06s (317 scripts,
109tests,108pass/1fail), including~159min startup/prebuild before first VM and
~91min execution. Two prior staging samples took2h18m26s and2h30m12s; these
are failed-run duration observations, not passing benchmarks. Current step
started20:42:44UTC, configured350min bound Nov4 02:32:44UTC (03:32:44CET),
job360min bound02:42:40UTC. Baseline-elapsed checkpoint00:52:50UTC. Active
job logs endpoint404 and no artifact, so no current case-progress claim.
No checks waived or CI mutations; monitor watches actual outcomes while root
stays active. Queued Intel/image jobs have no ETA from job timeouts.

## Managed reporting handoff and verified contract

Existing implementer2 (saved Sol/xhigh/workspace_write unchanged) owns the full
CI evidence package. Managed readiness report was delivered via report_to_lead,
receipt de35f0f2-1c26-4c6d-b9c3-a716d91b4d12, current leadturn steered=true.
Old generichelper /root/ci_wait stopped only its observer processes and released
soleutilityslot; CIjobs unchanged. implementer2 must launch one fresh Luna/low
utility, keep own member turn active, then explicitly report result via own
managed tool (utility must not impersonate member identity).

[Reporting contract](reporting-contract-checkpoint.md) traces EXACT installed
runtime0q7 through immutable source and pinned codex-web: member-to-lead uses
rootThreadID + SendWithOptions; active lead gets turn/steer, idle lead gets
turn/start; cold path durably queues then activates. Completed turns are not
automatically forwarded. This supports explicit managed reporting, unlike the
old passive helper. No live idle test was performed and steered receipt proves
active delivery only; no absolute guaranteed-delivery claim. Uncertain sends
must reconcile/retry same messageID. No runtime/team changes were made.

New utility /root/ci_managed_watch failed shell setup before usable observers;
member reports no gh watch/handle/CI effects. implementer2 is reconciling and
preparing corrected bounded commands for fresh utility. ROOT STAYS ACTIVE until
actual replacement observer readiness and managed callback ownership verified.
See ci-managed-result.md. No CI mutation, source edits or integration yet.

## Verified managed ownership transfer

Implementer2 now owns the complete CI evidence package, saved Sol/xhigh/access
unchanged, stays active while fresh Luna/low utility `/root/ci_managed_observe`
observes exact runs. Lead independently verified PIDs2868129/2876309 alive with
--interval30 and exact IDs41695511680/41695651867. Managed readiness/ownership
receipts and source-policy verification are in [ci-managed-result.md](ci-managed-result.md).
Explicit owner report_to_lead is required on outcome/blocker; utility completion
alone is not forwarded. Source-verified installed code starts an idle lead turn
(or cold queue-then-activate), so lead can now yield after genuine ownership
handoff. No live idle test or absolute delivery guarantee is claimed. Uncertain
reports reconcile/retry same ID; no root/member identity impersonation.

[Source contract](reporting-contract-checkpoint.md) uses exact installed runtime
source and pinned codex-web, not mutable HEAD. This replaces the earlier
unverified automatic-resume promise with an explicit managed reporting path.
Lead standing integration approval is unchanged. On managed outcome: verify
current session, exact head/test evidence, fresh staging target and full series,
read current selected coordination guide, prepare hooks outside claim, acquire
short single-repository ownership, ff-only merge/push/remote proof, release
before CI/records/cleanup. No claims held while waiting; no session closure.

Completed image detection evidence: ci-managed-job-126191399031.log selects
centos-10-stream,centos-9-stream,rocky-10,rocky-9. This proves selection only;
CI execution/pass still pending. All4 local image passes remain recorded.
This tracking checkpoint is a genuine CI evidence-package ownership handoff.

## Managed idle continuation and image CI success (Nov4)

Authenticated member report465f3de5-62b3-415a-9eb5-4b95b972472a returned
turn01a1a3aa-9f30-7892-9c83-f65e3890722a with steered=false and actually resumed
this lead, which independently verified current binding/roster/head/status.
This is now operational evidence of the managed idle-lead path. It does not
claim universal delivery guarantees or change the earlier source-only finding.

Image41695651867 completed SUCCESS at exact1a637e9e, all3jobs green. Job
126192300407 ran22:33:01–23:05:22UTCNov3; four selected/executed/passed cases:
CentOS9 982.18s, CentOS10 993.49s, Rocky9 858.68s, Rocky10 972.43s;
batch1831.14s, exit0, nativeCI24GiB. Evidence ci-managed-result.md plus full
ci-managed-job-126192300407.log and ci-managed-41695651867-final.json.
Local8GiB and nativeCI24GiB image verification now both complete. Generic core
suite still running at last snapshot; known unchanged fixture failures remain
failed/accepted-baseline disposition, not green. Implementer2 retains active
member turn and remaining generic watch, must explicitly report substantive
outcome through managed tool. No new source, CI rerun or lifecycle action.
Lead retains original approval and awaits generic acceptance before ff merge.

## Progress response refreshed-ci-checkpoint-gap

Resolved with concrete evidence: implementer2 delivered one exact-head jobs
snapshot, actual core step/job start and configured bounds, and completed
plain-Intel failure log matching immutable baseline fixture/output. Lead
independently checked these local receipts; CI receipt and current state now
supersede queued-only text. All9 refreshed lifecycle raw logs are now independently classified against the
immutable baseline signature and retain FAILED/pre-existing disposition. No case-level
core claim from unavailable live logs. Existing design/source scope unchanged;
no duplicate watcher, retry or approval gate. Any distinct signature routes to
architect-owned diagnosis. Next native milestone is core completion or distinct
failure, reported immediately via active implementer2 managed callback.

## Distinct refreshed core failure (Nov4)

Accepted managed report eadc75d7-ece0-4992-96c1-45c2680b509c; final generic
run failed with core102pass/7fail. Lead independently checked final run/head,
actual job completion before native bounds and raw323-script summary. Eight
failed scripts include new openSUSE cases and kernel metadata assertion; names
alone do not establish upstream or feature attribution. Architect0 assigned
bounded read-only diagnosis, no retry or source edits. Implementer2 retains
artifact-completion package only. Session remains open, original merge approval
persists but verification is not accepted.

## Distinct-failure diagnosis checkpoint

Artifacts separate missing public Leap16.1 container images (6scripts), older
openSUSE device status polling timeout (1script), and failed lxc-attach before
kernel immutable assertion (1script). Exact-base742 core comparisons are in
progress, bounded to two completed jobs. These observations do not establish a
source-provenance regression, baseline attribution or a flaky-test waiver. No
application edit, rebuild, retry, claim or integration is authorized by this
checkpoint. Architect0 retains diagnosis ownership.

## Exact-base attribution checkpoint

Architect reports two completed exact742 base suites independently reproduce all
seven openSUSE failing scripts (103pass/6fail), including same-runner staging
job. Both baseline misc-attrs tests pass. Thus the unresolved current difference
is the kernel pidfd attach failure before its assertion; names alone do not
establish its cause. Architect retains capped artifact comparison/diagnosis,
no test/VM/kernel work launched. Production/published container image availability
is distinct from successful local image-workflow builds.

## Kernel-group count correction

The unchanged group has14 scripts and testScriptJobs=6 concurrency. Earlier
architect/lead references to six scripts were incorrect. Implementer2 verified
source and exact-head CI selection before VM admission; lead accepted full14 /6
unchanged execution. No test filtering, new design, source/configuration edit or
additional permission gate. Metadata/resource preflight and watcher readiness are
pending; no VM/test/build is claimed launched by that preparation report.

## Premature kernel-group preparation stop

The first local group invocation was interrupted by its utility during STATIC
HEADER preparation, before VM boot or scripts. Exit1/119.27s and full log retained,
cleanup reconciled. No local kernel-image build was established. Corrective
continuation is authorized without a new user permission gate: fresh watcher,
same source/config/full group, fresh guard/state, corrected exact-derivation stop
condition. Do not classify this setup interruption as a failed kernel assertion,
attach-race reproduction or resource/cache blocker.

## Verified kernel continuation ownership

Readiness message52c7a5f8 belonged to the prematurely interrupted first invocation;
continuation handle50754 is separate and actually live. Lead checked current
shell2003123/Ruby2003126, actual continued-state command, native full14 selection
and16GiB reservation. Current operation utility /root/kernel_group_continue and
active managed owner implementer2 retain sole ownership until result/cleanup.
No VM/script success is claimed from test-system preparation. Selected runtime
coordination guide9f239ylk... /catalog25e251... was read in full for eventual
short merge preparation; no repository claim acquired while verification runs.

## Kernel continuation dependency checkpoint07:45UTC

Original continuation handle50754 remains singly owned and progressing through
declared i686 GCC/libstdc++ static cross-toolchain compilation, about25min after
native admission. No config.json, VM boot, script result or actual boot-kernel
image build is established. This proves an incomplete local cached dependency
closure, not a capacity/source/test failure. Static-header preparation progressed.
Lead continues this existing normal build; no duplicate CI path or extra setup
is launched. Next milestone: config completion/actual VM start, then14 results.
If still preparing at08:00UTC, owner reports exact active derivation/build phase
and concrete progress for reassessment; this is not a cancellation/quiet timeout.
No alternate CI run has been dispatched.

## Kernel VM milestone07:47:09UTC

Current operation progressed beyond missing local cached cross-toolchain into
actual guest/script dispatch. Full group/context retained, no second path.
Ambiguous RCU warnings do not establish source regression, attach reproduction
or a failing test. Architect checks existing artifacts only; implementer2 keeps
sole run/monitor ownership and explicit result callback. Native deadlines and
concrete-failure stop rules remain; no timeout or kernel/security/resource tweak
is invented from these warnings.

## Guest warning/selection classification

Architect confirmed kernel6.18.49 is intentional: common.nix enableUnstable for
this group; failed CI cgv2 reports the same6.18.49 /26.05.git.54b4313. No image
kernel mismatch is evidenced, full input equality remains unclaimed. Current
local console progressed from RCU starvation to CPU7/bash soft-lockup reports
(44–190s observed). First shell4 setup `mkdir -p /run/osvm/shared-dir` started
08:49:28CET with no completion at the bounded read; other shell logs empty.
No actual ESRCH, assertion or native test result yet. Architect identifies the
exact existing setup deadline; no guessed deadline or guest commands. Parent
continues current native budgets, no settings/kernel/resource tweak or second
path. If setup fails, classify its scope separately from misc-attrs reproduction.

## Native setup deadline classified

[Architect checkpoint](kernel-group-warning-checkpoint.md) completes bounded
read-only classification. Intentional6.18.49 matches failed-CI kernel; full input
equality still not claimed. Exact path: common.ensure_kernel_machine ->
wait_for_osctl_pool20min (includes boot) -> ready shell marker -> serialized
SharedDir#mount. Shell4 mkdir at07:49:28UTC has no completion in snapshot.
This is BEFORE pool polling/container assertions. Nested command default900s
monotonic timeout and enclosing20min pool budget remain; later online wait has
its own20min. No invented overall local-group deadline or CI350min limit.
Warnings are not native fatal-classifier matches and prove progress trouble only,
not host/resource/kernel cause or ESRCH link. Parent preserves actual native
setup result and continues same owned handle. A setup failure cannot count as
misc-attrs reproduction or resolution. Architect investigation ends; implementer2
sole operation owner, no extra diagnostics/settings/source/checks.

## Local outcome and focused CI path

Local continuation ended after concrete native setup failures. memory-view-cgroups-v2
reported UnrecoverableTimeoutError on shared-dir mkdir at08:04:28UTC (1039.22s
script elapsed); five initial scripts hit pool setup timeouts at08:07:10 (~1201s).
No completed assertions. misc-attrs dispatch after setup failures/interrupt at
08:07:41 has NO outcome; this does not reproduce or resolve the CI attach error.
Original complete native status kernel-group-continued-native-completion.json
records exit130/^C/chunk0ddf25. Lead read that exact status and independently
confirmed all reported shell/runner/executor/evaluator/QEMU/virtiofs PIDs absent.
No local operation remains. Inputs/LXC receipts are reconciled from host artifacts
only; no new guest commands/builds. Earlier header-preparation stop remains separate.

Lead authorized ONE existing focused ci.yml workflow on unchanged published54,
suiteci/tagci/pattern kernel/vpsadminos#*/prebuildtrue/stop_on_failuretrue. It
preserves full14/native6/ordinary two-VM context and avoids another local setup
attempt. No local+CI overlap or duplicate full/image run. Implementer2 owns fresh
Luna/low/full_access CI operation, bounded existing-run discovery then single
dispatch if missing, exact run/input/selection/monitor readiness and managed result.
No source/workflow/settings/Git edit, claim, deployment or lifecycle action.
Fresh SSH proof still feature54/staging742 and local tracked worktree clean.
Focused CI launch/readiness is pending; no CI execution/result claimed yet.
Full genericCI remains FAILED102/7; seven openSUSE scripts and nine separate
fixture failures retain FAILED/exact-base or pre-existing dispositions, not passes.
A focused success would be bounded verification evidence, not a claim the attach
race is fixed. Parent holds integration until result acceptance and fresh merge
preparation. Existing standing merge approval remains valid.

## Merge environment preparation outside ownership

Lead prepared the repository default Nix shell with retained refresh-hook-shell
profile, before any claim. Tool PTY22641 is an idle ready bash in feature cwd;
Ruby3.4.11 /feature .gems/bin/overcommit available, signature verification1.
Overcommit hook inventory loads without trust failure; Nixfmt/RuboCop enabled.
Clean detached target remains742eb30. No feature merge or default push occurred,
no repository ownership acquired. Recheck shell/feature/target/current runtime
and accepted verification before using it; a stale shell is repaired outside claim.
This preparatory shell is distinct from ended local test/guest processes.

## Focused CI verified ownership

One dispatch returned actual run41798971522 at54b43134, workflow_dispatch,
CI (ci: kernel/vpsadminos#*). Lead independently read initial JSON and exact
remote-ref/dispatch receipts and verified shell2620725/gh2620728 watching only
this run at30s/exit-status. Handle92162 belongs to fresh utility
/root/kernel_focused_ci, pinned Luna/low/danger-full-access/approvalnever.
Build/cache126469791914 active; actual focused selection/execution/results and
matrix skip remain pending. Implementer2 stays active and explicitly reports
substantive/final outcomes, not passive utility completion. No local run/claim.
Local receipt is complete with actual exit130 and986-path read-only closure /
configured LXC6.0.6; no graph-equivalence claim or new build was made.

## Focused CI test-start milestone

Exact54 run41798971522 build/cache passed. Core126479225372 has prepared state
and entered Run tests at08:44:41UTC; unrelated lifecycle126479227313 skipped.
Focused nonempty-pattern job/step uses240min; saved actual job start08:44:36
and step start08:44:41 give12:44:36/12:44:41UTC bounds. No completion ETA. Existing handle92162/gh2620728 stays solely
utility-owned with active implementer2 callback. Actual14 selection/native6,
misc-attrs and complete results still await native logs; no pass is claimed.
No local runner, duplicate watch, source/workflow/settings change or claim.

## Approved integration preparation

[Integration receipt](merge-result.md) records standing approval, exact54 checks,
known failures and bounded attach disposition, refreshed whole-branch/history/
no-migrations acceptance, matching reviewed diff digest and prepared hooks.
No new source or scope change. Claim request drafted only; no target mutation
or repository ownership yet. Lead performs short ff-only integration and explicit
release, then records/feedback. Session stays open.

## Transport diagnosis milestone

Implementer0 bounded read-only probes reproduce SSH255/publickey and Git128.
No SSH_AUTH_SOCK or Git SSH overrides/core.sshCommand in its shell; default
id_ed25519 exists UID1000/mode0600, no user SSH config. No private key material
or credentials printed. API authenticates aither64 with admin/push=true; default
staging remains742eb30. Effective staging rules=[], repo/parent rulesets=[],
protected=false/enforcement off. No branch-rule violation is established.
Bounded verbose/public-fingerprint comparison continues to distinguish rejected
key versus signing failure. No credentials/rules/runtime/Git change, upload,
retry push or repository claim. Source54 verification remains accepted.

## Transport exception proposal (not executed)

Implementer0 completed bounded diagnosis: same usable key is publicly registered
but rejected before signing on both verified SSH22/443; no client/key/rule repair
is established. API still reports staging742 and admin/push permission. All
probes ended; no claim held or mutation pending. [Diagnosis](integration-transport-diagnosis.md).

Workspace AGENTS.md:56 and Git procedure:109 require SSH cloning/pushing.
Lead is asking the user for a one-time HTTPS transport exception for the SAME
approved reviewed/tested54 -> vpsadminos/staging integration retry, using existing
gh authentication and per-command credential helper, leaving canonical origin
SSH and no key/rule/global Git config changes. No HTTPS push, auth refresh or
credential upload has been performed. This asks for a transport exception, not
repeat merge approval. All implementation/review/check/ordinary SSH preparation
and known remote-effect reconciliation are already complete. Approval would be
followed by fresh exact ref/cleanliness checks, NEW short repository claim,
normal non-force push, authoritative remote proof and explicit release. No
ownership while awaiting the user's decision; session remains open.

## SSH recovery / approved retry

User directed: "fyi github should be fixed, so retry ssh". Fresh bounded ordinary
SSH origin read now succeeds, proving default staging742eb30 and feature54b43134.
Source54 and retained locally fast-forwarded target54 are clean. Same selected
runtime9f239/cat25e251 instructions byte-identical; ready hook shell22641 still
works with Ruby3.4.11/signatures1. Complete six-commit range and matching reviewed
full-index diff digest rechecked; no source/history change or new verification.
HTTPS exception proposal is SUPERSEDED, not approved or used. Canonical SSH
origin remains unchanged. Fresh request 1be23311-7e39-4123-b416-98b47ecc4010 is prepared for only the
same approved ordinary SSH push, fresh exact checks/remote proof and release.
Old released claim is not reused. No ownership while preparing this retry.

## Verified post-push CI handoff

Lead checked exact54 initial generic/image JSONs, final RSpec/RuboCop successes,
live native observer PIDs402745/402752 and actual detector selection of precisely
CentOS Stream9/10 + Rocky9/10. Implementer2 retains active package ownership and
explicit managed callbacks. Source delivery/integration done; lifecycle remains
active only while automatic feedback is outstanding. No new approval or user
action is needed. Session stays open and feature refs/worktree retained.

## Post-push Ruby checks complete

New staging/head54 RSpec41822392741/job126548484137 reports13 unique PASS
components and3297examples/0failures; final408examples are test-runner only.
RuboCop41822392684/job126548483585 succeeded. Lead checked final exact-head
JSONs and actual raw component summary. Generic41822392601 and image41822392604
remain with the original owned observers; no new run/check/mutation. Merge is
already delivered, feedback remains active.

## Post-push image CI complete

Actual automatic staging54 image41822392604 completed SUCCESS/all3jobs; raw
four-case selected/executed/pass evidence and ordinary24GiB resources retained.
No upstream extras or new dispatch. No failure-only artifact expected for success.
Image observer ended; wrapper exit_status0/original tool reply metadata separately
reconciled by owner, not invented. Lead checked image gh402752 absent and generic
402745 still live. Only generic41822392601/core/lifecycle outcomes and final
observer cleanup remain with existing active managed owner; no new operation.

Image observer receipt limit clarified: actual wrapper exit_status0 retained;
original native wait exit_code0 was seen but its complete tool result object was
not preserved after truncated display. No reconstruction or rewatch. Authoritative
staging/head54 success JSON and all4 actual raw passes independently establish
image result. Remaining generic owner will persist complete original terminal
poll object before display plus shell status; no new operation or result change.

## Post-push generic checkpoint14:47UTC

Exact54/staging/push generic41822392601 remains solely observed through original
handle75277/utility with active implementer2. Core126551401008 remains in Run tests;
upload/evaluate/summarize/cleanup not started, no new core outcome. AMD126551401115
started, five other AMD variants queued, zero AMD terminal. Three Intel failures
retain matched pre-existing vg23 fixture disposition. Native core step350min /
job360min bounds17:33:40/17:43:34UTC unchanged; queue times do not provide an ETA
or proof of a stall. No new failure/pass inference, check/retry/source action or
claim. Already merged source54 and post-push image4/RSpec3297/RuboCop passes stand.
Next callback is actual core/AMD outcome or distinct failure, then final observer
cleanup. Session remains open with feedback active.

## Progress response post-merge-core-checkpoint-gap

Accepted: observer0 reports completed core126551401008 success in existing live
watch across two observations, while saved11:47 snapshot and lead/owner records
lag execution. This is a missed reporting milestone, not a source or elapsed-time
failure. Existing owner implementer2 assigned one completed-job JSON/raw summary
capture NOW, actual source/coverage/outcome reconciliation and explicit managed
report without waiting for AMD/workflow final. Original lifecycle observer remains
owned/running; no duplicate poller, new test or source action. Await primary receipt
before asserting exact test totals. Earlier active-core checkpoints are historical.
Source54 is already integrated; session stays open for remaining feedback.

## Progress response post-merge-core-checkpoint-gap resolved

Actual completed core126551401008 JSON/raw log now retained and reconciled,
exact54/staging/push. Job11:43:34–14:43:45UTC, step11:43:40–14:43:38, below
native limits. Native totals323scripts/109tests/8037.71s,109successful with zero
expected/unexpected failures or unexpected successes. Lead independently checked
exact source/tree and109unique successful test names; owner reconciled full
323-script selection/109-test selected=success sets. misc-attrs93.27s and combined
kernel/vpsadminos1609.93s passed; no ESRCH recurrence or race-fix claim.
Earlier14:47 active-core statement was STALE after14:43 completion, now explicitly
superseded. New actual core success does not relabel prior102/7 failures or prove
input equivalence. Only lifecycle remains: one AMD running/five queued/zero AMD
terminal in latest snapshot, three Intel pre-existing fixture failures. Same
utility/75277 continues, no new watcher/API loop/check/source action.

## Authoritative remaining queue correction15:33UTC

Owner took one bounded all-jobs API snapshot, lead independently checked exact54/
run41822392601, total11jobs/5completed/6queued/0inprogress and all six empty runner/
step assignments. IDs126551401115/307/316/365/442/604 remain queued. Watch'*' means
nonterminal, not running; older one-running/five-queued statements are superseded.
Populated queued started_at is not actual execution start, and native350min step/
360min job limits are not running yet. No runtime ETA/deadline or stall/test failure
inferred. Core109/images4/RSpec3297/RuboCop already passed; three Intel fixture
failures remain FAILED/pre-existing. Same active utility/75277 owns external
runner-assignment wait, no duplicate watcher/new CI/source action or claim.

## Completion acceptance

All registered exact final feature heads are integrated: sole repository vpsadminos,
final54b43134 is freshly proven ancestor of current staging2951a632. No migrations,
deployment or coordinated node rollout. Main post-push checks passed; terminal
workflow failure is fully attributed to unchanged fixture setup logs, with one
inconsistent job-status API field preserved. Complete native observer reply and
all exact observer cleanup reconciled. No new source fix, test, retry, claim or
operator action is required for this update. Tracking lifecycle complete leaves
this session open; no session lifecycle command was invoked.
