---
lifecycle: active
---

# Automatic coordination storage cleanup

Phase: ready, awaiting merge approval. All review and verification are complete.
User explicitly authorized tracking after initially requesting untracked diagnosis.
No production cleanup, deployment, master integration or unrelated-session mutation.

## Phase checklist

- [x] Attribute disk growth and record compatibility/recovery design.
- [x] Implement, commit and publish automatic cleanup in its owning runtime.
- [x] Independent whole-branch review; reconcile both Important findings.
- [x] Publish matching, consolidated consumer pins; validate composition.
- [x] Complete packaged build, native profile exercise, configuration build and CI.
- [ ] Obtain explicit integration/rollout direction; activate and measure.

## Exact repositories

All use branch 2026-10-19-coordination-storage-cleanup and worktrees under
worktrees/2026-10-19-coordination-storage-cleanup/.

| Repository | Final review base after rebase | Published final head |
| --- | --- | --- |
| dev-workspace | ff36d6153a6908751a18adfdf624c3619c1f397e | 5d59adbcdba420e5f127333097348ba1860c970d |
| workspace | b604f2c2d00d36e4f484b7b51a502f51b36f395b | 541d7f9ab937579b903e1f4d886ce6bc487f2bf4 |
| vpsfree-cz-configuration | 060ea03448af6f9083506d770315ad439279e76e | 265ed92ddf52570fa5414c7a4642b22229b3884a |

Runtime has two logical commits: 81e65dd (scratch and worker-root lifetimes),
5d59adb (profile history). Each consumer has one final pin update. Configuration
was regenerated from its original base with confctl; hooks pass and generated
message is preserved. Each lock changes exactly one intended runtime node.
Extension and other inputs stay selected as before. Composition contract passed
at final runtime 5d59adb. No migrations or repeated dependency-update streams.
Shared checkout remains on master; preserve its unrelated files and index.

## Diagnosis and implementation

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
Native rollout ownership may require stopping/restarting only this empty runtime;
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

Request the prepared approval for all three master targets, matching aitherdev
system/application activation and stopping/restarting only this empty runtime
for native coordination ownership. All independent work and checks are complete.
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
User approval is the only remaining gate; keep lifecycle active.

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
