---
lifecycle: active
---

# Automatic coordination storage cleanup

Phase: all master merges and system deployment succeeded; workspace profile activation in progress.
User explicitly authorized tracking after initially requesting untracked diagnosis.
User-approved three-repository master integration and no-reboot deployment are in progress.

## Phase checklist

- [x] Attribute disk growth and record compatibility/recovery design.
- [x] Implement, commit and publish automatic cleanup in its owning runtime.
- [x] Independent whole-branch review; reconcile both Important findings.
- [x] Publish matching, consolidated consumer pins; validate composition.
- [x] Complete packaged build, native profile exercise, configuration build and CI.
- [x] Obtain explicit integration/rollout direction and initialize native identity.
- [ ] Merge through native coordination; activate matching system and profile.
- [ ] Verify automatic collection, measure reclamation and finish reservation.

## Exact repositories

All use branch 2026-10-19-coordination-storage-cleanup and worktrees under
worktrees/2026-10-19-coordination-storage-cleanup/.

| Repository | Final review base after rebase | Published final head |
| --- | --- | --- |
| dev-workspace | f27925c43460066424dd8d6c4ab8ad93a267d60b | 7ceb6b943c7fa6e6db2b42b1fc2d9732c6413e03 |
| workspace | 8d821fff284602af954e2d3d9799641c70f941d7 | de3237e8b93b2d1de8f4ee1bb6835db229be92d0 |
| vpsfree-cz-configuration | a81c6e047606abb1427f10583810695cf59973f0 | 3195c4451dea8ffaff17d2974a5eca67d5d829a0 |

Runtime has two logical commits: f3a3f80 (scratch and worker-root lifetimes),
7ceb6b9 (profile history). Each consumer has one final pin update. Configuration
was regenerated from its original base with confctl; hooks pass and generated
message is preserved. Each lock changes exactly one intended runtime node.
Extension and other inputs stay selected as before. Composition contract passed
at final runtime 7ceb6b9. No migrations or repeated dependency-update streams.
Shared checkout remains on master; preserve its unrelated files and index.

## Diagnosis and implementation

Earlier checkpoint details below retain their original verification and rollout
revisions. The current heads and current phase above supersede those checkpoints.

At 09:32 CEST: 95% used / 50 GiB free. Since October 17, workspace Nix source
snapshots grew 40.7 -> 83.0 GiB, coordination 39.8 -> 80.1 GiB, worktrees
48.7 -> 64.7 GiB and session records/evidence 3.5 -> 14.5 GiB. Coordination
comprised 45.4 GiB of sources and 34.8 GiB of integration scratch. Repeated
workspace copies contain about 2.5 GiB of archive content. Complete integration
scratch and notification roots were explicitly excluded; profiles retained all
historical packages. Pressure GC recently freed only 2.8 GiB.

KB verification remains absent. Test images fell 96.3 -> 80.8 GiB. Legacy
root-owned ~/.osvm-qemu remains unchanged at about 246 GiB. Do not remove other
sessions' evidence (including about 10 GiB of Rust build data in confctl work).
At 10:17 CEST, filesystem use reached 97% / about 33 GiB free.

The existing five-minute collector now removes known completed detached scratch,
releases idle worker roots and prunes workspace profile generations. It preserves
selected/predecessor/live packages, explicit holds and native Git locks, active
processes, live recovery references, dirty first-admission checkouts and unknown
ownership. Compact journals and Git refs survive. Ordinary Nix GC owns store
path deletion. See design.md and runtime docs/coordination-operations.md.

## Review and verification

Risk: high (destructive cleanup, persistent recovery and profile retention).
Installed catalog ffaf9deb97720995ad1d662badae7645eba1fede5068eef529c9024efa7e7376
selects Astra/xhigh independent review and Luna/low/full-access verification.
No retained team exists; no members were invented.

Independent reviewer /root/retention_review, native thread
01a15329-cb74-7402-932a-efe55a1d4d93, verified Astra/xhigh/full access/approval never.
All four lanes completed; original exact ranges and history/migration conclusions
are retained in review-packet.md and review.md.

Important finding 1: a partially deleted checkout was readmitted as newly dirty,
stranding its pending cleanup. Fixed by resuming the recorded removal intent
under the saved exact path/common-directory/HEAD and unchanged detached Git
registration. Pending checkouts must not be reused. Process references and .keep
still postpone retry; replacement data without registration survives.
Both native remove and targeted repair refuse a surviving directory whose .git
is gone. The bounded fallback finishes that admitted directory deletion, then
uses Git to retire its registration. Affected general/risk review assessed that
new primitive; see review-remediation-packet.md and review-remediation.md.

Important finding 2: the fallback bypassed a native Git worktree lock. Fixed as
requested by preserving locked/locked-reason registrations during planning and
rechecking the fresh registration immediately before removal. Known ignored
contents survive pre-existing and newly acquired locks; unlocking permits cleanup.
This direct rejection-only fix is verified under mandatory-review step 9 without
another reviewer rerun. No actionable findings remain. Both fixes are folded into
959da49; the separately reviewable profile policy is retained.

Quick checks: syntax/diff checks pass. Initial full suite 30 tests/143 assertions;
recovery remediation 33/169; final implementation 35/179, zero failures. Strengthened
lock-content assertions pass their focused rerun (2 tests/13 assertions). The
packaged build covers the complete final test tree. Semantic lock checks and the
composed deployment contract pass for e1c71ff.

Fresh utility /root/retention_verification owns the batch in verification-brief.md:
composed package, disposable native profile, exact aitherdev system build and CI
39222150023 for e1c71ff. No activation is included. Keep full logs and compact results.
The utility initially stopped before execution because it could not find its
native metadata. Parent verified thread 01a15342-4450-7552-a4d1-96380774519c
from session_meta/turn_context, matching the agent path and all policy settings;
see watcher-native-settings.json. Continuing the same first operation, not
reusing a completed verification lifetime.

## Identity, recovery and execution notes

Created through dev-session start coordination-storage-cleanup --no-codex --no-attach.
Both verified literal DEV_SESSION values agree with current. The threadless
runtime has no valid retained lead conversation; ordinary lead work and installed
standalone review fallback apply. The earlier untracked checkout was moved into
this registered scope. A manifestless start correctly refused; no repair bypass.
At the initial checkpoint, native rollout ownership required stopping/restarting
only this empty runtime;
include that lifecycle action in the final approval request. See rollout.md and
notes/dev-workspace/2026-10-16-threadless-start-and-configuration-hooks.md.

An initial fixture run encountered another real host preparation; fixture mode now
skips external preparers, with separate production-guard coverage. Configuration
checkout initially lacked local gems; setup in its Nix shell restored declared
hooks and registration. No hook bypass.

During final history folding, a rebase conflict briefly published incomplete
feature head 6ff8560 because a subsequent push was not conditional on rebase
success. Resolved the conflict, proved final tree equality with tested a5442a8,
and corrected publication to e1c71ff with exact force-with-lease. No live selection
or master changed. Cancellation of superseded CI 39222056098 returned HTTP 403
(token lacks workflow cancellation access); do not claim cancellation. Prior
957dc29 and 926c669 CI passed. Final run is 39222150023.

## Next action

Supervise the approved native integration run, verify live automatic cleanup,
measure reclaimed space and finish its exact machine reservation.
Do not archive, delete or stop this session without the applicable direction.
Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-19-coordination-storage-cleanup/

## Verified rebase onto concurrent integration

Another session integrated four portal commits while the first batch ran. New
remote baselines are the exact bases in the table above. No libexec, Ruby tests,
Nix files or coordination guides changed in that baseline. Runtime rebase was
clean; both ordered stable patch IDs and all owned source/test/doc hashes match
exactly. See rebase-proof.json and runtime-range-diff.txt. Retain original review
and its narrow-fix verification under the Git procedure's patch-equivalent rebase
rule. No changed migration or new design. Each consumer pin was regenerated as
one final commit from its new remote baseline, changing only its runtime node;
extension/other inputs preserved. All final branches are published.

First utility's local checks all passed: composed package 331.47 s, real profile
exercise 13.17 s, system build 138.33 s. Exact artifacts, derivation and logs are
in verification-result.json. Its overall incomplete label only reflects the
parent-directed stop before CI observation when upstream advanced. No command
was left running. Old final e1c71ff CI also passed; the previously uncancelable
superseded run completed successfully.

The new composed Ruby aggregate is exactly the successful prior derivation,
including transitive inputs and unique shard coverage; see
ruby-verification-reuse.json. Generic and composed aggregates have different
consumer inputs, so only the composed-to-composed identity is reused. Native
profile behavior remains valid because the collector file is byte-identical.

A fresh standalone native utility owns final whole-package/system rebuilds and
CI 39223853984 for 5d59adb, per verification-refresh-brief.md. Thread
01a15351-670e-7ac3-9cee-11a34e198738 is verified Luna/low/full access/approval never;
see watcher-final-native-settings.json. This is a new one-operation utility,
not a reused watcher or a team member. It preserves final logs and
verification-final-result.json. Composed deployment contract and semantic pin
checks pass at 5d59adb. No activation or integration has run.

## Final verification and handoff

Final fresh utility completed the exact refreshed batch successfully, exit 0,
08:40:29–08:46:44 UTC (375 seconds). Package, aitherdev configuration and exact
CI run 39223853984 all passed. No operation remains running; no retries or
cancellations were performed in that batch. See verification-final-result.json,
final-artifacts.json and verification.md. Real profile exercise passed in the
first batch; exact composed Ruby aggregate reuse is recorded separately.

Final application output: /nix/store/m72n1y584cafyzi09na546ll751hwnpl-dev-workspace-0.2.0.
Final system output: /nix/store/bd52dj1ba0sai0bd2w2qmhjnmzxg1p8p-nixos-system-aitherdev-26.05.20261015.26f4107.
Configuration generation: 2026-10-19--10-43-01, built from exact 265ed92d.
Final comparison captures match the bases/heads in the repository table.
At handoff, filesystem reports 93% used / about 67 GiB free. That increase
occurred before this feature's activation and is not claimed as cleanup evidence.
No master integration, deployment, session stop or production collection ran.
This was the pre-approval checkpoint. User approval is now recorded below; keep
lifecycle active until coordinated integration and live acceptance finish.

Released only this initiative's superseded pre-rebase workspace-package output
root after the final candidate passed; retained the final candidate root and
compact verification/derivation receipts. No Nix store path was deleted.

## User-approved integration and deployment

User direction: "aha, ok. deploy and merge", replying to the prepared request.
Approval covers dev-workspace, workspace and vpsfree-cz-configuration into their
respective master branches, matching aitherdev system/user-profile activation
without reboot, and stopping/restarting only this empty runtime to establish
native ownership. See rollout-approval-source.json. No scope expansion.
Selected package advanced to nqhmww60 while awaiting approval; upstream runtime
now f27925c4 and both consumer defaults also advanced. Preserve this approval
through a proved patch-equivalent refresh; do not roll back concurrent changes.

Empty runtime initialization: authorized exact-slug stop retired the runtime,
then the legacy empty-thread recovery notification returned "exact recovery
identity is required", matching the documented threadless-start lesson.
Ordinary start must prove absence and create the managed identity; do not edit
authority or recovery metadata. This checkpoint hands retained tracking to that
new native conversation while the external lead retains rollout supervision.

Native initialization completed through ordinary start after the authorized stop:
retained lead 01a153ed-e471-7010-b678-dae0a7871d90, requested Sol/xhigh, no roster
created (team list roster null). Its initial goal acknowledges initialization
and leaves all rollout actions with this external lead. The App Server terminal
client reconnect was recovered by the native command. Current ownership is valid;
use foreground integration under a fresh status-only utility observer. Do not
spoof the external caller as the retained lead or bypass background admission.

Tracking handoff commit 26f791a6 was committed under the shared tracking lock.
Published the existing linear tracking-only master range through 8d821fff under
that same lock, after verifying every changed path was coordination tracking.
Unrelated files/index were preserved. Final consumers include that shared base.
User approval remains standing for all three master targets, matching no-reboot
aitherdev system/profile activation and the now-completed empty-runtime setup.
Do not request that approval again for a patch-equivalent refresh.

Refreshed heads/bases and semantic pin checks are in approved-refreshed-heads.json;
accepted review receipts preserve original reports and record narrow-fix/rebase
provenance. Matching contract passes. The fresh approved verification utility is
01a153f1-59d5-74b0-b95b-864e7b925156, verified Luna/low/full access/never. It owns
package/system/CI 39244860923 checks. Prepare the final native integrate-first
request after its result, retain reservation for actual cleanup acceptance and
finish explicitly afterward. Integration request was submitted as native foreground run fc106326-494a-4395-a530-72c9f547fbc7 after exact verification and shared tracking publication.


## Approved rollout execution

Fresh exact-head verification passed: package 335.597 seconds, system build
164.787 seconds and runtime CI 39244860923. See approved-verification-result.json.
Exact package receipt and independent review provenance are frozen in
integration-request.json. Native foreground driver 1 is supervised by a fresh
Luna/low/full-access/never status-only utility, thread
01a153fc-0afa-70e2-92e0-bec56b9eb920; actual turn_context proof is in
integration-observer-1-policy.json. Parent owns deployment and live maintenance;
the observer only reports authoritative status. Request intentionally omits
completion so aitherdev remains reserved for live acceptance.

The first observer returned an interim preparing snapshot prematurely; no driver
failure or timeout was inferred. A fresh replacement, thread
01a15400-0dbc-7d90-99c3-bff8124ef03d, is verified Luna/low/full-access/never and
retains observation until authoritative completion/action or actual driver exit.
Native semantic refresh over concurrent shared tracking produced workspace head
30c7945873caafb160513f515d28a0c63c230eed on base
392ae7c5bd5fb3d16ae7041741f5f400466601a0. Its generated-pin proof preserves
7ceb6b9 and all unmanaged inputs; original independent review remains frozen.

Driver 1 completed preparation and submitted all three merge jobs, then exited
75 with "integration driver is already running". No integration lock remained
when inspected; runtime job ca6ac738-a777-484e-b6be-bcf8c209b4ca succeeded and
the two consumer jobs were claimed. The parent resumed the SAME run through
the stable command, driver-2 logs/exit, under fresh observer 3. No new run or
merge job was created and no job was replayed. Observer 2's claimed timestamp
is inconsistent with the actual clock; use authoritative native receipts and
the parent command capture for timing.

Observer 3 reports all three exact merge jobs succeeded and the retained run
is in deploy. Runtime remains 7ceb6b9, workspace mechanically refreshed to
30c79458 and configuration remains 3195c445. Live activation/cleanup acceptance
and machine release remain outstanding.

System job 0e2a93ec-96ce-4944-ae43-94702a6bb7a6 succeeded without reboot.
Profile job 4a97cdc3-240d-4206-a58a-44f99f345ef1 advanced to claimed.
The parent now automatically retries only the verified exact exit-75 driver-lock
contention against the same run/stable command; any different error stops for
inspection. Driver 3 remains accounted for under fresh observer 4
(01a15404-e420-7230-9895-0dc9e2a5a7cd), native policy verified.

## Integration fc106326-494a-4395-a530-72c9f547fbc7

Requested exact feature heads are integrated. See integration/fc106326-494a-4395-a530-72c9f547fbc7/summary.md
and integration/fc106326-494a-4395-a530-72c9f547fbc7/result.json for operation receipts. Feature refs and session retained.
