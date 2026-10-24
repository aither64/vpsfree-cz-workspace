---
lifecycle: archived
---

# Portal improvements

## Complete: generic reservation documentation cleanup

Deleted configuration's host-specific coordination runbook. Generic machine
ownership/release rules remain in dev-workspace's canonical coordination guide,
referenced by workspace instructions. Concrete host commands and system/profile
verification remain in the existing provider guide. The update skill's reference
to the deleted guide is replaced. Policy and runtime behavior are unchanged.

- [x] Workspace final9f6968eb: one six-path documentation/routing-test commit.
  Existing Ruby instruction checks passed10tests/206assertions, whitespace passed,
  AGENTS15682bytes. Three incoming tracking commits and unrelated shared changes
  preserved; exact patch/full-tree equivalence proved after rebase.
- [x] Configuration finalc1057731: one three-path relocation/deletion/reference
  commit. Normal cached Nix/Overcommit hooks, finite references and whitespace pass.
- [x] Retained reviewer0 Sol/xhigh/read_only completed general+architecture lanes:
  no findings, no obsolete history, no repeated pin streams, no migrations.
- [x] Both ordinary fast-forward integrations, normal hooks and nonforce SSH pushes
  passed. Parent independently verified exact remote master+retained-feature heads.
- [x] Workspace claima6ca8062 RELEASEDrev2; configuration claim2011b75a
  RELEASEDrev3; authoritative status verified. Initial config wait preserved.
- [x] No build, runtime pin or deployment needed. Generic runtime Bbf6d and selected
  package4cn1 remain deployed from the prior verified rollout. No machine claim.
- [x] All registered exact feature heads integrated; no remaining task or blocker.
  Session remains OPEN; no archive/delete/stop, branch deletion or cleanup.

| Repository | Current integrated exact head |
| --- | --- |
| codex-web | ea64ef57fdd2ff5fd60715b62f2d1696bc0133e5 |
| dev-workspace | bf6d4b0c49600c15e17fe71248807ef43424e932 |
| workspace | 9f6968ebae4f1fbb26ff548ddcbd6cf8332a5b8b |
| vpsfree-cz-configuration | c1057731d34513b6ee3bb1dfb4a3e4832fdc67c9 |

[Final review](generic-docs-final-review.md) /
[exact inventory](verification/generic-coordination-docs/review-inventory.json) /
[parent remote and release proof](verification/generic-coordination-docs/parent-remote-proof.json) /
[C integration](verification/generic-coordination-docs/integration-proof.json) /
[configuration integration](verification/config-generic-coordination-cleanup/integration-resumed-result.json).

User approved this placement plan with “Implement the plan”. Integration retains
existing explicit C/configuration master scope recorded in
verification/integration-parent/approval.json; no semantic policy, repository or
target expansion. All prior rollout evidence remains historical and unchanged.

## Complete: automatic-release instructions merged and deployed

User requested “release should be automatic after deploy and merge”, then directed
“deploy it already and finish up”. The corrected policy is implemented, checked,
independently reviewed, merged, deployed and verified. It requires prompt release
after successful deployment/effect verification and complete integrated deployed
lineage, without a separate UI-acceptance or release-direction confirmation.

- [x] Shared generated lead/member policy and generic, workspace and site guides fixed.
- [x] Focused Go policy/member tests and C instruction10/230 suite passed;
  normal hooks/Nixfmt/graph passed. Main-context English pass complete.
- [x] Retained reviewer0 Sol/xhigh/read_only HIGH/all4lanes: NO findings;
  complete5appendgroups/no obsoletehistory/no migrations; one new pin per consumer.
- [x] Ctracking-only refresh independently reconstructed with ordered2patchIDs;
  unrelated trackingblobs/sharedroot dirty/index entries preserved.
- [x] Actual composedpackage4cn1/715a +agentinstructionsldjd/3pl98 checks passed,
  normalbuiltinchecks enabled; exactinstalledguides/newbinding tests and unchanged
  native/catalog/host/contracts verified. Initial helper Nixv4-shape failure remains
  immutable; corrected helperactual431.7015s accepted, watcher315.5s estimate rejected.
- [x] New policy Bfeature CI39785243104 SUCCESS (fast/archive/creation; host skipped
  by featurepolicy). Unchanged host/native evidence reused only by exact owning
  source/input identity; no new browser/VM/native campaign or master-CI wait.
- [x] Exact remote master+retainedfeature refs verified: Aea64ef57, Bbf6d4b0c,
  C6bc355ba, configuration1d71ce14. All feature worktrees clean; normal FF/SSH/
  requiredhooks passed; all repository claims explicitly released.
- [x] Ordinary user-profile switch PASS93.584s with freshbefore/after continuity;
  selected4cn1, systemjwnd unchanged; no pendingtransition. Corrected guides match
  exact reviewedsource. Native/tmux/socket/root/roster/settings preserved.
- [x] Machineclaimd226a86c automatically RELEASED/recheckedrev2 at14:00:34UTC
  after deployment+integration proof, without another human confirmation.
- [x] No owned operation or remaining implementation/deployment work. Session
  stays OPEN; no archive/delete/stop, branch deletion or cleanup performed.

Final heads:

| Repository | Integrated exact head |
| --- | --- |
| codex-web | ea64ef57fdd2ff5fd60715b62f2d1696bc0133e5 |
| dev-workspace | bf6d4b0c49600c15e17fe71248807ef43424e932 |
| workspace | 6bc355ba27032f927e29fe50ed19afbbf2f7ba73 |
| vpsfree-cz-configuration | 1d71ce148d43e156d4f3be9193a2b8caad56e94a |

[Final receipt](verification/automatic-release-policy/final-result.json),
[deployment](verification/automatic-release-policy/deployment-receipt.json),
[final review](automatic-release-final-review.md),
[review packet](automatic-release-review-packet.md),
[design](design.md#automatic-machine-release-policy).
Older rollout receipts and nonancestor lineage remain immutable below. No new
system deployment was performed. Future deployments require fresh ownership;
release remains separate from session lifecycle permission.

Stable session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-20-dev-workspace-portal-improvements/

## Integration complete — all four remote masters verified

User explicitly said “yes, merge it” after the lead named all four master targets.
[Approval](verification/integration-parent/approval.json) /
[aggregate remote and claim proof](verification/integration-parent/final-integration.json).

| Repository | Exact integrated final feature head |
| --- | --- |
| codex-web | ea64ef57fdd2ff5fd60715b62f2d1696bc0133e5 |
| dev-workspace | 483d4e7eafeda974dfe19de45687795562072d7d |
| workspace | a9565d9536101c27690b338728514de41d7c3eeb |
| vpsfree-cz-configuration | ef2194e63367b3a8e4f5fbdd27002293d779becb |

- [x] Implementation, quick checks, independent HIGH/all-four-lane review,
  actual browser/archive-revive, package checks and user-profile deployment passed.
- [x] All four ordinary fast-forward merges and nonforce SSH master pushes passed.
  Parent independently verified fresh exact master/retained-feature refs, feature
  ancestry and clean feature worktrees. All four repository claims released rev2.
- [x] C/config refresh independently reconstructed over e71/8c2; ordered patch
  IDs match 5/5 and 2/2. No migrations, obsolete history or new pin streams.
  [Review-reuse certificate](verification/integration-parent/review-reuse-certificate.json).
- [x] Shared workspace stays on master; all 210 unrelated dirty tracked paths and
  unrelated index entries preserved. Normal configuration post-merge hook exit0
  proven through Git trace; no hook bypass. Feature and safety refs retained.
- [x] A master CI 39775953750 SUCCESS. Accepted identical-head B feature CI
  39744487759 fast/archive/creation SUCCESS; existing actual package/browser/
  lifecycle/deployment receipts remain bound to their exact sources.
- [x] B master CI 39776092273 COMPLETED/SUCCESS, including fast, archive,
  creation and host. A master CI 39775953750 also SUCCESS. Exact master/head/job
  snapshot checked 2026-10-22T13:02:34Z; no failed jobs or pending CI remains.
  [Current CI receipt](verification/integration-parent/ci-status-current.json).
  No workflow launch, rerun or CI wait was performed.
- [x] Original deployed result accepted; machine claim755 released and verified
  revision2 at13:04:53UTC. No original integration work remains. The new policy
  follow-up above keeps the session active/open.

C has no tracked GitHub workflows. Configuration's only workflow is scheduled/
manual Daily update, with no push trigger; latest observed older-head success
is not new-head verification. [CI snapshot](verification/integration-C-config/default-ci-snapshot.json).

C preserves upstream tracking; configuration preserves upstream rsyslog and all
five unrelated dependency-node changes. Its feature changes exactly the reviewed
devWorkspace and transitive codex-web nodes. The initial one-node expectation was
a proof-spec error, corrected without source edits. C12b/config354e remain retained
nonancestor deployed SHAs with proven equivalent integrated successors, rather
than literal ancestor claims. No new derivation or package pass is inferred.

## Deployment status

Files is deployed and verified on user-profile package `m8bqmkdzgk85vng42hcsavqmaz56rwgc`;
system jwnd/config450/runtimeBf8 stays unchanged. Native/tmux/socket/root/roster/
settings continuity and live Files/assets/preview/download passed. Notifications
returned HTTP200/availabletrue. [Deployment](files-deployment.md) /
[immutable receipt](files-deployment-receipt.json).

The user-confirmed codex-thread-retries session already exists and is ready;
no creation retry, replacement or initial request resend was needed or performed.
Integration commands are finished and both implementers returned ownership.
Original feature scope is complete. See the active automatic-release policy follow-up above.
Preserve branches, worktrees, roots and original receipts. No cleanup, lifecycle
action, system activation or profile change was part of integration.

Stable session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-20-dev-workspace-portal-improvements/

## Files correction — final package checks (2026-10-22)

The accepted correction restores the file tree and inline content pane, icon
controls, automatic discovery of regular session files (including ignored files),
and no-op registration commands. Archive/revive compatibility is tested only in
a disposable fixture. The live session stays open.

- [x] Exact session/environment, roster 34 and saved write access verified.
- [x] Architect brief: [Files contracts](design.md#files-inline-all-session-files).
- [x] imp0 backend committed `b0f3f2ea6140a7c8a107f93a7a894cad7e320f5c`;
  focused web/repository/session and Ruby syntax checks pass. Actual disposable
  archive/revive integration subsequently passed3.22s (see runtime receipts).
- [x] imp2 frontend committed `fc9c944afee16627f3f28e94ed73b8fa3e039368`;
  18/18 renderer/read-cycle Node cases and focused Go wrappers/cache/API checks
  pass. Main-context UI prose accepted; actual Files browser subsequently passed11.02s.
- [x] imp3: CLI/no-op and runtime docs/skill committed as `a44c585743811e2e6d97838eff6f9b4b343d182f`;
  Ruby 10 tests/62 assertions and syntax/whitespace pass. Main-context English
  pass complete; seven owned paths only, index returned empty.
- [x] imp1: C guidance paragraph published as `2f064a2f`; approved English,
  instruction checks 9 runs/166 assertions and whitespace pass. C clean; Git
  ownership returned; final pins/rebase subsequently completed.
- [x] B history consolidated/published `483d4e7eafeda974dfe19de45687795562072d7d`,
  19 groups, exact converged tree. CLI/backend/UI quicks and final syntax pass.
- [x] Reviewer0 final affected HIGH/all-four-lane review: NO findings, exact
 32commit inventory/history/migrations accepted. [Review](files-final-review.md).
- [x] Actual disposable archive/revive PASS3.22s and bounded Files browser
 PASS11.02s at exact B483d/Aea64; fresh Luna/low batch30.23s.
 [Runtime receipts](verification/files-runtime/operation-result.json).
- [x] Final package evaluation PASS77.23s: drv`v466ppdwhax565z8a53z5zmx0yp1dl34`,
 output`m8bqmkdzgk85vng42hcsavqmaz56rwgc`.
- [x] Initial launcher failure retained: stale app55 helper after successful
 workspace realization. Corrected app56 continuation subsequently passed only
 pending stages52.535s; original failure not relabeled. No native50.
- [x] Final C/config closure clean/published: `12b4491bd6e5bfa6799e938fd555c8f15d588a1d` /
 `354e944f9dcf071e4878f0a0bbf2e71f52693801`; exact parent reconstructions and
 graph checks pass, sole runtime streams retained.
- [x] Exact B483d CI39744487759 SUCCESS: fast/archive/creation; unchanged host
 exclusions retained. No duplicate local VM suite.
- [x] Actual composed package acceptance PASS: existing realized workspace reused
 with exact drv/input/output/NAR receipts; corrected metadata and7pending stages
 PASS52.535s. [Package receipt](verification/files-final-composition/parent-package-acceptance.json).
- [x] Earlier preflight refusals preserved; resumed normal guarded switch
 passed with fresh before/after continuity, native/tmux/socket identities retained.
- [x] Live Files/assets/preview/download/continuity verified; ready for user review.

B clean final `483d4e7e` has exact quick-tested tree
`930467237114bf6e2d953f8e34ea6c352388cfea`; parent independently compared all
mode/blob entries. Imp3 returned source/Git ownership. Deployedbc40 and convergence
fc9c refs retained. Final Files is projected into ownercd3c9db, read-cycle glue
into752f914, independent CLI483d; 19 groups, one unchanged A stream, no migrations.
Reviewer0 final review is complete. All implementers returned source/Git/helper
ownership; imp3 returned the bounded historical evidence reuse receipt; parent independently
verified45mode/blob/source-hash comparisons.
Runtime acceptance passed. Initial launcher attempt stopped before tests because
relative logpaths dirtied the source worktree; exact owned logs were preserved
under tracking and source cleanliness restored, then fresh corrected utility
passed. No test/product change. Evaluation utility90638 and package utility4023 completed; continuation utility32927 completed; source/pins remain frozen.
Current live f5h/Aea64/Bbc40/C40b0/config5a524 stays selected until the new
candidate passes. Machine claim 755 remains held. No native50, unrelated campaign,
live session lifecycle action or registration of new evidence is authorized.
No parent driver or verification utility remains running; final deployment verified. Prior deployment evidence is retained below.

### Prior deployed checkpoint

## Follow-up deployed and live verified

**Deployed 2026-10-21 23:50 CEST /21:50 UTC**, before the requested morning.
User profile now selects f5h1qmr03qva6khyijgc2wxd1ff4k4cw; normal profile switch
exit0/52.379s. Systemjwnd/config450/Bf8 unchanged. Native Codex0.163.0 and tmux
stayed continuous; own health/assets/Files/catalog/root/roster/settings/attempt
checks passed before/after. Parent independently verified effects and heldclaim.
[Rollout](followup-deployment.md) / [receipt](followup-deployment-receipt.json).

### Current phase checklist

- [x] Implementation committed/published; complete30logicalgroups, no migrations;
  independent HIGH all4lane review and requested narrow step9 corrections accepted.
- [x]107component cases PASS; actual two-tab Firefox regression PASS22.42s,
  hiddenzero/readbudget/singleSSE/wake/typedquestion/pending503retry, no mutations.
- [x] Targeted3Question + notification actual browser PASS receipts reused with
  independent unchanged-exercised-source/dependency proof; no repeat runs.
- [x] Exact Aea64 flakeCI and Bbc40 fast/creation/archiveCI SUCCESS. Two scoped
  unchanged-host VM exclusions retained; no literal all-flake-attributes pass.
- [x] Final composed package + eight rooted stages PASS574.088s; exact candidate
  drv i3zb1wpdy1f8l376q5ya36gny3fcmdmd, outputf5h1qmr03qva6khyijgc2wxd1ff4k4cw.
- [x] Parent profile deployment and before/after live passive continuity PASS.
- [ ] User UI acceptance and separately authorized default-branch integration.
  No merge approval supplied. Session stays active/open; no cleanup/lifecycle action.
- [ ] Machine release remains unauthorized: claim755910ab-a78b-4d30-a057-03b555b336db
  HELD until integrated deployed lineage, user acceptance and explicit release.

No operation, verification utility or source/Git writer remains running. Parent
successful driver91231 and observer13791 are CLOSED; utility
01a1606f-99a9-7ef1-9419-acf6cb73b702 actual low/fullaccess/approvalnever verified.
Successful attemptef8af949-0595-40d5-b50d-433ce41ddc8c in successor/
activation-roster-settings/attempts; original failed attempts retained unchanged.

### Verification boundary and user decisions

User explicitly cancelled further50-tab attempts and requested smaller targeted
performance regressions. Native50/discard/extendedsoak are withdrawn/unverified;
prior lost-response failure is retained, never converted to a pass. The committed
separately gated2tab test is the selected replacement; no new50tab run occurred.
Live macOSFirefox158 connection-reset incident cause/cure remains unproven;
no host tuning/restart/reset was performed. [Incident](followup-connection-incident.md).

Two initial pre-switch continuity attempts stopped before any switch command:
quotedYAMLsocket was parsed incorrectly, then optional transcript enrichment was
mistaken for ownership readiness. Minimal helper corrections use installed
validated YAMLreader + authoritative saved roster settings. All root/socket/
entries/roster/native/tmux/attempt checks remain, and the final real before/after
checks passed. No application/source/record change, guard bypass or rebuild.
Detailed failed/successful receipts remain in the rollout report.

### Final sources and package

| Component | Published final head | Unchanged remote default |
| --- | --- | --- |
| A |ea64ef57fdd2ff5fd60715b62f2d1696bc0133e5|57972192e30fe52ab33b867c8fe4d171f59a7fd5|
| B |bc40cdda2d28c9732396db4163daa244bba79acb|968646471b1190c16a8cf60ff50736cd0525fa3f|
| C |40b0c2b96e79a0ced3236a05e5569d5dc7142033|5276ad798d3dcf2c714f2336b0a50636bab900ae|
| configuration |5a524d26aafccfc93ed45bc1684c0a86fbc6b3bd|38e7c837893695999e588a73f5d2a0088b8257b1|

C/config final solepin streams selectBbc40/Aea64. Assets app55/store4/browser6/
mounted22/sync3/uploads7/copyhelper12. All sources clean/frozen; owners returned.
Parent independently reconstructed mechanical pin trees and actual candidate
roots/derivations, source reuse and host equivalence. Config5a524 remains a
source deliverable; installed system config450/runtimeBf8 remain unchanged with
equivalent host contracts. Preserve all refs, roots and receipts.

| Owner | Final status | Next action |
| --- | --- | --- |
| lead | Deployment/effects verified; tracking current | Await concrete user feedback; no additional work campaign |
| architect0 | Design and bounded test brief complete | Standby |
| implementer0..3 | Source/helper handoffs complete; no writes | Standby |
| reviewer0 | Independent complete/affected reviews accepted | No automatic review rerun |

### Retained prior checkpoints (historical)

Mandatory final review COMPLETE: reviewer0 saved Sol/xhigh/read_only, all4lanes,
HIGHrisk, exact reviewed A6e/B133/C755/configcc95. [Report](followup-final-review.md)
accepts histories/migrations/single pin streams/deployed lineage and found only
ImportantF1 (custom history retained canceled busy slot/old finally). F1 CLOSED
by [direct step9 correction inspection](followup-remediation.md), focused104Node/
Go checks and negative control on reviewed source. Six-file bounded fix folded
into lifecycle8cd67fe; notification added/removed lines identical despite adjacent
app53 context patchID difference. Final C/config pin-only closure independently
reconstructed by parent, [proof](verification/followup-composition-d617ef39/lead-mechanical-proof.json).
No new design/contract warranted review rerun; all unaffected conclusions retained.

No migrations; server schema1/IDBv1/catalog6/claim/session/journal/submission
formats unchanged. A852 literal ancestor. Deployed Bf8/C530/config450 are NOT
literal ancestors after accepted consolidation/rebase; exact safety refs, old
receipts/ranges/reviewed patch/reconstruction provenance remain. No literal merge
or semantic-equivalence claim for new behavior. No default integration approval.

Longer composed package batch PASS499seconds/exit0 via fresh retained Luna/low utility
01a15fb9-4f55-79a2-8915-bedbb34bb86b, native low/approvalnever/fullaccess verified.
Logs/status: verification/followup-composition-d617ef39/package-watcher; expected
drv72lyzcfqwb5sf05b3j7yndpaymjxwgx9/outputpvbdrx2n6x4zccpzg9qspfni28c564n3.
Parent independently verified all5 rooted drv/output identities and receipts;
metadata/nativeCodex/catalog/capacity8/reporting-only registration all pass.
No profile selected. Exact final ACI39634886832 flakeSUCCESS and
BCI39651301505 fast/archive/creationSUCCESS; host-only jobSKIPPED. Exact-head
job receipts saved in final packet/ci-final; no CI waits or reruns.
Display preparation/rooting PASS4.326s/0.827s through fresh Luna utility
01a15fc2-ec69-7543-9243-499fca67d09f. Fresh browser utility
01a15fc4-1b64-7011-8c40-5e99701bd356 completed notificationbrowserPASS46.949s
and ordinaryFirefox50FAIL84.645s (discard/restoration SSE count assertion).
Imp2 owns concrete read-only diagnosis, no rerun/source changes authorized yet.
Supplement utility01a15fc7-c34c-7793-9a86-649c5389a57b completed: fullBbrowser
FAIL411.16s (6Questionfixtures); ApagingPASS14.72s and3CattrsPASS5.14/38.27/19.39s.
Imp0/imp3 own disjoint read-only concrete failure diagnosis. Imp2 owns only
4Firefoxfixturepaths+BGit for approved synchronization correction; no other
source writes. All final pins/operational guards deferred until convergedB.
Actual50tab/fullbrowser acceptance unproven; no deployment until corrected/verified. [Current verification](followup-verification.md). Prior quick suites/source-vendor preparation are not
browser acceptance. Historical
incident-wide cause/universal cure unproven; recovery without reload is required.

User added implementer2/3; verified same-session ready/workspace_write Sol/xhigh,
no reconfiguration. Read-only Firefox/notification readiness completed, no missing
static prerequisite established; source edits only on routed failure and explicit
serialized boundary. Author source/Git/pins frozen during verification.

### Verification coverage and next batches

Architect mapped actual declarations: composed package covers full ordinary BGo/
Ruby13shard9suite aggregate, claims/collection/preparation/switch/naming; exactB
CI supplies additional contract/catalog/source-filter/namespace checks plus
session-creation and session-archive-lifecycleVMs. Adefault/generic pass and
exactACI flake passes. Cagent-team-policy passed. Supplemental required:
Cagent-instructions/deployment-contract/cluster-provider-composition, checked-in
A paging Node fixture, FULL13-subtest Question browser wrapper plus new-session
settings/index-selection/archive-failure UI, notification actual browser and
ordinaryFirefox50 native visibility/discard/recovery. Imp0 prepares session-only
supplement scripts; new fixtures remain unexecuted. Whole repo-pinnedPW output
includes both Chromium1217 and Firefox1511; root both for full wrapper.

Host-module-idempotency and session-recovery-boot are explicitly excluded from
this feature-only batch: CI runs them only default/dispatch, host substrate and
switch/units unchanged by exact blob proof, and no system activation is planned.
This is a recorded unchanged-host lane exclusion, NOT 'all flake attrs passed'.
Creation/archiveVMs are required and exactB CI PASSED them, not excluded. No
native-upgrade campaign is implied; bundled native version unchanged. This
scope preserves accepted full ordinary/browser checks without duplicateVM runs.

[Browser findings and approved bounded fixture corrections](followup-browser-findings.md)
record the exact first-stop causes. All six full-wrapper failures currently map
to stale selectors/scoped mocks or an overlay-era geometry expectation; later
steps still unverified. Imp2 correction published3671, parent directchecked four-testpath-only/no
productiondelta proof and meaningful positive/negative/Go checks. Real50 still
pending. Imp0 Files/teamsettings/paging fixes published bf477, three CJS only, all other
526 blob/modes unchanged. All fixes now converge at clean publishedB965,17groups; parent independently
proved ten-testpath-only delta vs d617 and production/assets/deps/docs identical.
Source/Git frozen; new fresh Luna corrected fullwrapper+rawFirefox50 batch running
in verification/browser-corrected-965aadc5/watcher. Final pins/activation still
HOLD until actual browser success; no parallel source edits. Superseded3671 CI cancellation denied
HTTP403; no repeated POST/credential change. Current final-head CI only will count. No
production/TLS/cache/API change is justified or authorized by this evidence.
Final pins/activation guards wait one convergedB.

### Deployment contract

Architect exact source/receipt check concludes USER-PROFILE-ONLY forward rollout.
B host-module/paths/stable switch/profile+coordination identity/claims-host adapter
and whole nix/systemd are byte-identical f8->d617; host contracts unchanged.
C machine/catalog/config unchanged; config450->9ab host config unchanged while
upstream nixpkgs/KB/PHP changes are unrelated to this rollout. Existing system
jwnd already supplies required socket/namespace/auth/TLS/machine contract. Keep
BOTH system links jwnd/config450/Bf8, do not claim they contain finald617.
Final config9ab is matching source/policy deliverable, not deployed system revision.

After package+browser/Firefox50 pass, parent verifies fresh selectedhzf9, both
systemlinksjwnd, exact held machine755, final graph/native/tmux/updated roster/
settings/attempt baseline and candidate host-contract equivalence. Use ordinary
selected workspace-host switch --source own C with exact session+claim env;
no system build/switch/private helper/native upgrade. Candidate selection must
be exact rootedpvbdrx, preserve claims/gates/attempts and let supported checks
refuse incompatibility. Preserve forward journals/generation on failure; no
rollback, record deletion or release to bypass refusal. Imp1 prepares guarded
session-only driver/smoke; parent owns actual activation. Machine755910ab freshly
verified HELD revision1; no repository claims for preparation/checks.

### Follow-up phase checklist

- [x] Investigation and user decisions complete; incident-wide root remains unproven.
- [x] Reacquired and verified retained aitherdev machine-only claim.
- [x] Architect recorded accepted follow-up design; both implementation packages released to source work.
- [x] Shared and portal source changes, documentation and quick checks committed/published.
- [x] Final actualconsumer/solepin/graph/derivation closure; parent independent tree reconstruction accepted.
- [x] Affected final review atB8675 complete; original conclusions/F1 retained.
- [x] PENDING-A1/FIXTURE-B1 requested narrow corrections directly verified under step9; runtime acceptance pending.
- [ ] Package/disposable browser checks including real Firefox50-tab visibility.
- [ ] Forward deployment and live continuity/source/catalog/files checks.
- [ ] Explicitly authorized integration, user acceptance and explicit machine release.

Earlier deployment evidence below remains bound to its original exact heads;
it does not certify this follow-up. Current changes must retain durable attempt,
roster, notification state, claim and citation compatibility. No schema migration
is planned; additive capability and backward-readable browser records need review.


## Earlier deployment — original heads only

Aitherdev deployment COMPLETE and verified, ready for use. All four feature
branches are ready, awaiting merge approval. Session remains active/open. Updated session
coordination rules are read and applied. No default integration, reboot or
session lifecycle operation is authorized. The session remains open.

| Component | Published deployment head | Baseline |
| --- | --- | --- |
| A codex-web |852e8c51091512bc79ca6c921ef1f5ccc46a9535 |57972192e30fe52ab33b867c8fe4d171f59a7fd5 |
| B dev-workspace |f8f2938b4e2cfd6e5b82657d08f014357817808f |968646471b1190c16a8cf60ff50736cd0525fa3f |
| C workspace |530038a8ee2bf6772144b07ca0cb02426fc1e6d6 |11d2a692951f2cd2f79460d4c04c40a43416e9df |
| configuration |450e1ff538c1e94c1ec74f57b50fbe2efb31502b |37a338b25192d9271ee211110800c2dc6a094a57 |

All four clean and published; parent independently SSH-verified exact refs and
unchanged defaults. B preserves installed short-merge policy through all8 exact
patch IDs and independent whole-tree reconstruction. C preserves integrated
coordination rules, compresses instructions to15873bytes/511headroom and keeps
one final runtime pin. Config one normal confctl-generated lock-only update.
Final C/config graph checker passes. No migrations or obsolete pin streams.

Independent affected review COMPLETE, no findings: retained reviewer0 saved
Sol/xhigh/read_only, general/risk, exact C530/Bf8/config450. Original unaffected
four-lane application review plus direct narrow-fix acceptance preserved. See
[refresh report](deployment-refresh-review.md), [packet](deployment-review-packet.md),
[reuse proof](deployment-refresh-proof.md), and [design](design.md). Final review
gate satisfied; verification reuse requires exact derivation/input identities.

Quick B/C/config checks pass, including explicit Overcommit0.73 fixture
1run52assertions10.425s and refreshed B exact-head CI39595263230 SUCCESS.
Final focused Chromium on Bf8/A852 PASS exit0/16.755s (test7.909s), evidence
verification/final-browser.log and final-browser-result.txt. Read-only authenticated
baseline smoke PASS5.094s against selected6bbj; native Codex/tmux PIDs3387667/435397,
same-session identity/model/effort/roster hash captured privately0600. No live turns
or roster mutation. RootSSH existing fixed key/strict-known-host route proven;
credential only in memory, no key/auth/sudo/host permission changes.

Exact C530 composed realization and metadata/registration/policy/source checks
PASSED. Native command receipt exit0; watcher approximate9m38s only (missed exact
summary timing); stage logs, extracted stdout and batch-evidence.json retained.
Candidate drv cscdy7ahywqp1lw8lc5jrmh3776n6y2q/output hzf9qda2ckjsv72b689bclc6p3v8ap9l
remain rooted. A852 checks reused by exact derivation/input receipts, not tree equality.
Host build+copy PASS186.353s: generation2026-10-21--14-31-08, topleveljwnd3m223...,
clean embedded config450/runtimef8 and roots/rollback retained.

ACTIVATED under machine-only claim759b3cc6-8d11-41d0-a17e-8107922db4c0, explicitly RELEASED revision2 at12:46:04UTC.
Parent driver dry22.965s/no-reboot system switch37.549s/stable profile switch,
overall110.376s. BOTH live/system-profile paths select jwnd3... (exact
jwnd3m223qh1lanig1ndxprk04qbim06); profile hzf9... selected from C530.
No private helper, rollback, merge, reboot, roster or session lifecycle action.

Live after smoke PASS11.877s: all9servedassets exact, catalog defaults/counts,
health/TLS/auth, same nativeCodex3387667/tmux435397, root/model/effort/entire retained
roster hash unchanged. Naming child/catalog ready; no naming/provider turn created.
Index ordinary-demand acceptance PASS3.415s: one normal GET, four progress reads,
two identical ready samples,322sessions/0operations, loadingfalse/authoritativetrue,
no warnings/notices/unknown cluster counts. Earlier cold progress-only snapshot
was uninitialized cache, not a service failure; no product source fix or broad
rerun. Evidence verification/deployment-index-publication/result.json.

All owned activation/verification processes completed. Machineclaim759b3cc6
explicitly RELEASED revision2 at12:46:04UTC; status independently rechecked.
No deployment blocker remains. Naming process/catalog ready; no new naming turn
or live send/Add test was made. Previous disposable interaction proofs remain.
All artifact/derivation roots and forward-recovery evidence retained. No merges,
reboot or session lifecycle actions; remaining integration requires explicit
user direction for named repositories/targets. [Exact receipt](deployment-receipt.json).

## Phase checklist

- [x] Verified session identity, updated coordination instructions and retained roster.
- [x] Implemented and locally checked portal, receipt recovery and team changes.
- [x] Independent original review; focused remediations and original package/browser checks.
- [x] Preserved selected short-merge baseline in refreshed B/C/config; final publication/quick checks.
- [x] Independent final affected general/risk review; exact runtime CI success.
- [x] Final refreshed Chromium acceptance and authenticated baseline smoke.
- [x] Rooted final composed package/metadata/registration checks passed (native command exit0).
- [x] Exact committed aitherdev generation build and copy passed186.353s.
- [x] Machine-only claim; system dry/no-reboot switch and stable profile selection passed110.376s.
- [x] Live source/catalog/naming/native/conversation checks PASS11.877s; index PASS3.415s; machine explicitly released.
- [ ] Merge named repositories into master only after explicit user direction.

Rollout actions/results: [deployment-rollout.md](deployment-rollout.md).
Stable session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-20-dev-workspace-portal-improvements/

## Prior verified composition (before deployment refresh)

Worktrees beneath `worktrees/2026-10-20-dev-workspace-portal-improvements/`:

| Repository | Base | Published head |
| --- | --- | --- |
| codex-web |57972192e30fe52ab33b867c8fe4d171f59a7fd5 |852e8c51091512bc79ca6c921ef1f5ccc46a9535 |
| dev-workspace |52dcd471186ef874c5c93f4133744195d4815454 |db25364999aa4bf12b67506662a08e9e464bee33 |
| workspace |0ea5682410a38fe19627bc731e13894c1e51db57 |3de65bbd0e90f0c3b19e0d64ed925158155647a6 |

Three/eight/three commits. Final SSH checks match these heads and unchanged remote
masters. All worktrees clean. Extension767dfd5, siblings/follows and Codex0.163.0
unchanged; B changes only shared lock node, C only runtime/shared nodes. No
migrations or obsolete/fixup/intermediate pin history. User confirmed existing
models/efforts for new presets; retained roster unchanged. Full team2 is new
selection default;3–6 variants, capacity8, direct nativechild0 and utility1 verified.

## Review and checks

[Independent review](final-review.md) reviewed A2ea01d5/B3f0eae0/Cd16483d8,
high risk, retained reviewer0 gpt-6.1-sol/xhigh, general/architecture/scope/risk.
F1 Blocking logical split and F2 Important stale notice were resolved through
pure split identity and bounded matching conversation/thread/attempt/action
reconciliation. Lead inspected code/docs/order tests, reran focused actual A/B
checks, and checked mechanical final pins. [Remediation record](review-remediation.md)
explains direct acceptance under skill steps9–10; no new contract/design warranted
review rerun. A1 conservative failed-enrichment count hiding accepted in design;
A2 stale pin commit body corrected. Original independent report retained unchanged.

A owner76 Node checks and focused Go pass; lead mounted/upload40checks1.014s.
B final combined web/runtime/catalog6.050s/0.422s/0.037s pass; lead notice test0.213s.
C instruction9/166 and deployment4/19 plus format/policy checks pass. Package
stages all pass; installed defaults/models/capacity/policy/source checks pass.
Original batch exit1 was an incorrect final argv[] assertion: CLI correctly adds
required reporting MCP settings after its empty native-role plan. Corrected pure
assertion validates original actual output with checksum/derivation/input proof,
owner0.954s and lead0.793s, no repeat builds/CLI. Details in final report.

Chromium full acceptance passes (15s; Go6.682s); native right-click, standard/Ctrl/
Enter supplement passes (18s; Go3.934s). Context menu item selection and macOS
Cmd-click are not exercised by headless Linux. Production POST502 cause remains
unproved; recovery contract is tested without live App Server restart claims.
A CI39505066197 and B CI39506876852 SUCCESS. No active stale CI remains.

Final source claims A6d2ab2a1/Bc5d089f2/C7cd1d35f explicitly released. No machine
claim or running utility remains. Built package was subsequently pressure-GCed;
original successful stage/metadata/registration evidence is preserved and bound
to exact derivation/source hashes. No realization or new GC root was necessary.
Future deployment can realize its approved candidate under normal procedures.

## Owners and next action

Implementer0 retains B follow-up diagnosis ownership; implementer1 retains A/C.
Architect owns material design deviations; reviewer0 retained for affected lanes
if scope changes. Lead owns acceptance, user-facing writing and session records.
No outstanding implementation/review/check work. Next action is user decision
on explicit codex-web/master, dev-workspace/master and workspace/master integration.
No session archival/deletion/stopping is authorized by this handoff.

[Plan](plan.md), [design](design.md), [original reviewed inventory](final-inventory.md),
[implementation checkpoint](implementation-checkpoint.md), [citation refresh](citation-refresh-checkpoint.md).
Project docs: codex-web docs/reference.md; runtime docs/workspace-portal.md;
workspace docs/agent-teams.md and bounded AGENTS compression (16313<16384).
Initial tracking commit900b71f6; subsequent records follow normal consolidated
checkpoint cadence and preserve unrelated shared changes.

https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-20-dev-workspace-portal-improvements/

### Implementer1 bounded historical incident evidence (2026-10-21)

Read-only client-scoped nginx aggregate confirms no ordinary completions from
20:26:54 until 21:28:48 CEST (61m54s); resumption matches parent-reported TCP reset
second. All 3,918 completions used HTTP2; SSE times are completions, never starts.
No matching bounded nginx journal entries; combined logging lacks duration,
connection/stream/frame evidence, so GOAWAY/draining remains unproven.
[Payload-free aggregate, exact commands/receipts and limits](verification/incident-firefox-20261021-192848/report.md).
C482/config9ab/pins/activation remain HOLD; no source/live state mutation.

### Coordinated final source closure (implementer1)

Aea64 / B0c0dd2d2 / Cc61d98f5 / config13e17a37 are clean and SSH-published;
all defaults unchanged. Complete30 groups; one B→A, C→B and config channel stream.
Exact ten-path B and pin-only C/config reconstruction, graph and focused checks pass.
[Final immutable packet and prepared argv](verification/final-coordinated-ea64ef57/handoff.md).
Source/Git now frozen for parent verification. Package/browser/CI coverage remains
pending; activation gate absent and HOLD. No deploy/claim/release/lifecycle action.

### Tracking-only smaller read-budget successor preparation

[Successor command/activation copies](verification/targeted-read-budget-successor/README.md)
prepared with final B/C/config/candidate identities pending and gate absent. Native50
withdrawn/unverified; old Question/notification/CI receipts retain exact0c0d identity,
reuse proof awaits actual final B. No source/pin/Git/check launch; imp2 owns B.

### Final two-tab composition handoff (implementer1)

Aea64/Bbc40/C40b0c2b9/config5a524d26 clean/published, defaults unchanged;
[final packet](verification/targeted-read-budget-successor/README.md) contains
sole-pin proofs/30series, exact browser reuse proof, actual reviewed2tab PASS
22.42s and evaluated candidate f5h1/i3zb. New package NOT realized; gate absent.
Parent owns package/finalCI binding/activation. Native50 withdrawn/unverified;
no reruns, claims/releases/lifecycle or deployment actions by implementer1.

### Before-smoke diagnostic copy prepared

[Diagnostic-only copy/one-shot passive argv](verification/continuity-before-diagnostic-4f375865/README.md)
adds safe fixed stage/check/source-line telemetry after original pre-switch failure.
Original helpers/driver/attempt/gates/hashes unchanged; no root cause yet established.
Syntax passes; no reproduction/GET/credential/profile action by implementer1.
Parent received bounded180s command for fresh utility because duration is uncertain.


### Files activation refusal (current follow-up)

Attempt3bc03a44 completed before continuity PASS, then normal switch exited1
in0.573s with195outputbytes hashed only. No profile/system selection change,
no pending marker and no remaining owned command. Installed source puts unfinished
lifecycle-operation guard first, before fingerprint/build/claim checks; absence
of a build log limits this to early preparation, but exact branch is unproved.
Imp1 checks for a supported strictly read-only preflight/finite sanitized error
capture; no journal clearing, lifecycle action, standalone restart or blind retry.

Switch refusal remains unclassified: installed unfinished-operation check is
private and has no supported read-only entrypoint; status does not perform it,
prepare mutates/builds. No private/reflective checker was invoked. A minimal
tracking-only successor will retain16KiB solely in memory and record fixed known
refusal booleans alongside existing output hash/length, with no raw text/IDs.
Parent authorized this diagnostic-only successor for one ordinary activation
attempt after no-effects reconciliation. All guards stay unchanged.

Diagnostic successor activation-switch-diagnostic ended at profile-switch with
exit1/0.376s, same195bytes/hash, fixed unfinishedSessionOperation=true and all
other refusal markersfalse. Prior no-effects state reconfirmed: f5h/jwnd selected,
no pending marker and no owned command. This is a proved unfinished-operation
block, not inferred from timing. Architect0 designs minimum portal-only storage
recovery and supported same-creation completion under held755; no guard bypass,
record clearing, native/tmux/session lifecycle action or foreign-session scan.
User attempted name is still pending. No further switch retry is running.

At09:20UTC lead repeated the concise async request for exact attempted session
name because unfinished-operation ownership now blocks deployment. Useful
independent work continues: architect validates portal-only restart/reload
semantics (no action yet), then exact notifications readonly poststatus and
normal same-receipt continuation. No lifecycle or foreign-session action inferred.
