---
lifecycle: active
---

# Red Hat-family image releases

## Current status

Phase: refreshed branch published/reviewed; exact-head CI queued and monitored.
At reviewed head `1a637e9eac4311adba2b08d60dfa7a17d07bcb52`, all four
image tests passed locally and in native 24 GiB CI, and the full core suite
passed 317 scripts / 109 tests. RSpec and RuboCop passed. Generic CI remains
red on nine identical pre-existing livepatch fixture failures; accepted as
unrelated failures, never represented as passes. [CI receipt](ci-managed-result.md).

Fresh target check found `origin/staging` advanced from `dd188397` to
`742eb30cb1a8b6766c85e915d26b0400e38244b1` with three openSUSE commits.
No feature paths overlap. No claim was acquired and no merge occurred.
Refreshed committed head: `54b4313404cea35b58ebb9df951ae75e27c44971`, tree
`5c03648e084e907957b37263846bc5763abdac1f`. Rebase was conflict-free;
all six patches and total diff are byte-identical. Source-version/channel Nix
evals, four bash syntax checks, whitespace and Nixfmt/RuboCop/hooks passed.
Detached target is clean at new base; shell dependencies are retained by the
untracked refresh-hook-shell profile. [Refresh receipt](refresh-result.md).
Same retained reviewer0 (Sol/xhigh/read_only) completed all four lanes with
no findings. Complete refreshed series/history/no migrations accepted; all six
patches independently reconstructed byte-identical. [Review](review-result-refresh.md).
Implementer2 completed leased SSH feature publication; remote feature is54b43134,
staging remains742eb30. It owns exact-head push runs generic41741634771 and
image41741634791, both queued at initial snapshot. Fresh Luna/low/full_access
utility /root/ci_refresh_watch owns native handles7050/79291 and PIDs913471/913599.
Lead independently verified both exact run heads and both live30-second observer
commands. No duplicate dispatch; actual detector coverage remains pending.
RSpec41741634539 was running; RuboCop41741634674 passed in discovery.
[Current CI receipt](ci-refresh-result.md) retains policy, logs and managed receipts.
Implementer2 remains active and explicitly reports substantive/final outcomes via
its authenticated managed route, which has already resumed this idle lead.
No Git/index writer, source mutation or default integration is active.
Previous successful checks retain their exact old-head scope; tree/patch equality
alone does not establish Nix derivation/input equivalence.

- Original final tested tree: `49b8a7879e6b363349ae70808c4cdecc996e578e`.
- Four per-image commits plus nullable channel and source-identity correction.
- Existing user approval covers vpsadminos/staging and patch-equivalent rebases.
- No repository/machine claim, VM or deployment is active; only the owned CI batch.
- Session remains open; no lifecycle action is authorized.

## Phase checklist

- [x] All-family upstream inventory and design accepted
- [x] Four image-release commits and source-identity/channel fixes
- [x] Focused Ruby/Nix checks, hooks and independent review; findings resolved
- [x] Four local and four native-CI image tests at original final head
- [x] Original exact-head core CI passed 109 tests; baseline failures disposition
- [x] Patch-equivalent refresh and independent full-range review
- [ ] Necessary exact-head CI at refreshed54b43134 accepted
- [ ] Final head fast-forwarded into remote staging; ancestry verified
- [ ] Final evidence/handoff retained; session remains open

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

Wait for the owned refreshed exact-head CI batch, handle distinct failures within
scope, then fresh-check staging742eb30 and the complete54b43134 final series.
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
