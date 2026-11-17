---
lifecycle: archived
---

# Stable kernel update

## Status

The requested configuration update is merged into remote `master` at
`15e3b9af90276e41d19e6a33477add58e5f9a8c9`. Channels `staging`, `os-staging`
and `production` all pin vpsAdminOS `f33f5fd10b53232b5670862f832f4ec5ea835e84`,
selecting stable kernel 6.12.118. Checks and independent history review passed;
normal fast-forward/push and fresh remote proof succeeded. Merge claim released
and verified at 21:28:04 UTC. No machines were deployed.

Earlier delivery: OS staging `f33f5fd1`, workspace master `9610ea74`, Linux
version branch `vpsadminos-6.12.118` at `3bba2729`, all 50 patches preserved.
Original full CI passed 110 tests. Post-integration OS CI `44167132711` failed on `f33f5fd1`. Architect0 owns
completed diagnosis (D5/I5). Build/cache passed; the test runner aborted after
"Disk quota exceeded" writing its diagnostic log. Automatic GC later freed
360.3 GiB. Runner service remains failed; no original job survives and no
terminal test results were recoverable. Exact-head runtime suite is incomplete. User accepts the earlier passing
branch evidence and explicitly directs leaving CI/runner as-is; no recovery
or rerun remains in this task. The session stays active/open.

[Configuration evidence](C4-evidence.md), [C4 review](review-c4.md),
[integration](integration.md), [handoff](handoff.md), [verification](verification.md).

## Phases

- [x] Verified session identity and required guidance
- [x] Architect design and dynamic full patch inventory
- [x] Skill/process committed before use
- [x] Complete 6.12.118 port and patch accounting
- [x] Quick checks, hooks and final logical commits
- [x] Independent final review and history/migration conclusions
- [x] Review Advisory fixed and focused verification passed
- [x] Published exact feature heads and remote proof
- [x] Exact-target build/cache and selected runtime CI evidence accepted
- [x] Unrelated qualification failure diagnosed and documented
- [x] vpsadminos staging integrated; Linux version branch published
- [x] Workspace instruction master integrated under separate user approval
- [x] Configuration three-channel pins checked, reviewed and merged
- [x] Post-integration OS CI disposition: runner failure diagnosed; user accepts prior pass and requests no further action
- [ ] Deployment: not requested

## Final repositories and identities

All feature worktrees are under `worktrees/2026-11-17-stable-kernel-update/`.
Feature and recovery refs remain retained. Current delivery endpoints:

| Repository | Final head | Verified endpoint |
| --- | --- | --- |
| vpsadminos | `f33f5fd10b53232b5670862f832f4ec5ea835e84` | remote `staging` |
| linux | `3bba27296b6f4f4a2b1568d65cea6037368f229b` | remote `vpsadminos-6.12.118`, published only |
| workspace | `9610ea74a70d4b9b9d0f2d9296ea4908c0d4725b` | remote `master` |
| vpsfree-cz-configuration | `15e3b9af90276e41d19e6a33477add58e5f9a8c9` | remote `master` |

OS final series: process `2352449568afa3b2f5bd500dba3fbed1c1163e0b`, then
catalog `f33f5fd1`, on baseline `42baba6117bebcde3d04555a71377381df197925`.
Linux has 50 unchanged commits above upstream
`b869a5313cbfe7102873d3de318ddb68675146d0`. Configuration has one generated
lock-only commit above `9c6a0313d1689099c1dfcb065171a4aead44f183`.
[Linux correspondence](linux-port.md) and [integration](integration.md) retain
original/rebased ranges, exact receipts and recovery refs.

## Packages and acceptance

| Package / deliverable | Owner | Dependencies / acceptance | Final status / evidence |
| --- | --- | --- | --- |
| D: investigation/design | architect0 | Exact pinned predecessor, upstream and package interfaces | Accepted; [design](design.md), first brief accepted before implementation |
| P: dynamic skill/process | implementer0; lead prose pass | D; no fixed patch list; conflicts/correspondence/selectors/hash/recovery | Accepted; [process evidence](process-evidence.md), final logical owner above |
| K: full Linux port | implementer1 | Accepted P used before replay; every old patch retained | Accepted/published; [Linux evidence](linux-port.md), all 50 native range-diff pairs equal |
| R: catalog/stable selector and demonstrated process corrections | implementer0 | K final source; raw archive hash; unchanged retained entries/ZFS/inputs | Accepted; [catalog evidence](catalog-evidence.md), all tools joined, write window released |
| Review: all four high-risk lanes | reviewer0 | Committed intended deliverables and passing quick checks | Passed with one narrow Advisory; [review](review.md), A1 fixed/directly verified |
| D2: qualification failure diagnosis | architect0 | Failed exact-attempt producer logs/plan/guard/unchanged inputs | Accepted; [failure diagnosis](qualification-failure.md), no app or remote mutation |
| V: actual completed build/test evidence | implementer0; lead acceptance | Exact final-head CI jobs/logs and selected test outcomes | Accepted; [verification](verification.md#final-completed-ci-evidence--package-v), no new tests/source changes |
| M-prep: refreshed OS integration preparation | implementer0 | User merge approval; staging42baba disjoint exporter baseline | Accepted; refreshed final OS integrated, equivalence receipts retained |
| L-publish: version Linux branch | implementer1 | User accepted version naming and verified source | Accepted; version branch exact3bba2729, no merge/tag |
| D3: publication-policy design | architect0 | User branch-only clarification, workspace rule contradiction | Accepted; [design](design.md#d3-uniform-linux-publication-instructions) |
| D3-OS: repo process/router instruction | implementer0 | Sufficient D3 brief and lead prose pass | Accepted, reviewed and integrated; three OS files only |
| D3-W: narrow workspace Linux exception | implementer2 | Same settled D3 contract | Accepted, reviewed and integrated; three policy files only |
| D4: configuration channel mapping/check brief | architect0 | New user update+merge scope, published OSsource | Accepted; exact mappings and generated update brief |
| D5: post-integration CI failure diagnosis | architect0 | Exact run44167132711/attempt1; first causal error/affected input proof | Accepted; communication loss, build passed, same kernel/tests; verification.md |
| I5: read-only runner evidence | implementer0 | Accepted D5 host/path brief; preserve any running original job | Accepted; quota-write error caused runner ABRT; no runtime terminal results; verification.md |
| C4: three channel vpsadminos update/merge prep | implementer0 | D4 sufficient brief before pins; independent hook setup allowed | Accepted; checks/history review passed, merged and remote verified |

All members retained saved settings and access. One executing package per owner;
OS and Linux mutation windows were separately owned. No team reconfiguration.
Identity repeatedly verified by `dev-session current`, matching both environment
markers and trusted thread binding. Initial tracking commit: `066f7b2c4`.

## Review, history and preservation

Retained reviewer0 (`gpt-6.1-sol`/xhigh/read_only; thread
`01a1ea07-46de-7650-b81d-f9ac09c416df`) independently covered general,
architecture/repetition, scope/proportionality and risk/compatibility. Reviewed
OS initial base..`5a59f3059ca6ada368deeeeca6dba5034468be93` and full old/new
Linux series. All 50 patch messages/authors/dates and range-diff pairs match.
All 86,724 union paths and seven overlapping native three-way merges preserve
both upstream and downstream behavior; final source tree is
`944e5a57917938df529d6eebb3e30eba40e4afef`.

No Blocking/Important finding, obsolete history, intermediate pins, fixups,
transitional compatibility paths, repeated update stream or migrations.
Advisory A1 clarified owned-shell `export GIT_NO_LAZY_FETCH=1`. Lead verified
old reviewed range -> final same-base..ba7e99b5: only requested process paragraph
changes, catalog range-diff `=`; source/catalog/flake unchanged. Focused checks
passed; no full rerun required under narrow-fix policy. [Review packet](review-packet.md)
retains exact old/new ranges and migration/equivalence provenance.

The user reversed an unpublished README-link removal request. Original link and
exact published ba7e99b5 were restored; canceled head94e9e13d is backed up. No
replacement push, CI cancellation, policy edit or revert/fix history was needed.

## Final verification and limits

[Main run44120817659 attempt1](https://github.com/vpsfreecz/vpsadminos/actions/runs/44120817659/attempts/1)
passed on final OS head. Build job134171356716 succeeded 16:00:37–17:17:43 UTC;
test job134223368327 succeeded 17:17:45–19:37:07 UTC. Actual normal/explicit
6.12.118 closure derivation and cached realized system:

- `/nix/store/1xz2kh8yvxaijd57mwkdk2wb0d1mgif8-vpsadminos-system-vpsadminos-26.05.git.ba7e99b.drv`
- `/nix/store/8abp9lh9skqgrjz2j3zm5spi1cnky5qv-vpsadminos-system-vpsadminos-26.05.git.ba7e99b`

Selected actual passing cases: NFS cancellation: 66 examples across NFS3/4.0/4.1/4.2,
stage-2 boot: 4, module autoload: 16, ZFS boot modes: 2 (external+builtin). Overall 324
scripts from 110 tests, 110 expected successes, zero unexpected results. Build
and dev outputs copied to binary cache. Full input/source graph, raw archive
hash, test source/config/identity and practical stdout limits are in
[verification](verification.md) and [catalog evidence](catalog-evidence.md).
Do not claim all CI guests use stable, full ZFS qualification, a production
rollout or exercised mixed-version rollback.

Documentation run44120817623 passed. Qualification run44120818064 failed at
pre-existing capture evidence guard for explicit retained 6.12.113, before any
producer realization; [causality proof](qualification-failure.md) establishes
unchanged workflow/tools/target/input blobs. No coverage inferred from that run.

Runtime-ci observers e499c41c-7ad3-48cb-a40b-aef8502bcaf9 (main),
34708386-f302-4679-99e4-1cc1fc8fdc2d (docs), and
21973214-5205-477b-a4f5-f0ba3dc97d15 (qualification) delivered exact-attempt
terminal outcomes. Supported CLI registration used verified native caller after
MCP caller refusal; no duplicate watcher or identity adoption. All native member
commands/downloads joined; no unknown effects or physical-machine reservations.
No additional checks or source changes are needed for the stated scope.

## Documentation, recovery and next action

Maintained process: `vpsadminos/docs/os/kernel-updates.md`; agent entry:
`vpsadminos/skills/update-kernel/SKILL.md`, discoverable through AGENTS, README and
MkDocs. It dynamically derives prior pinned range, preserves package layers,
requires semantic conflict resolution/full correspondence, hashes raw archive
bytes and moves/verifies the applicable stable/unstable selector. Actual port
had no source conflicts/adaptations; diagnosed partial-clone replay handling was
incorporated. No fixed patch inventory is in the reusable process.

Keep old catalog identities/ZFS pairing and OS generations; no pool features
changed. External modules/dev outputs were rebuilt; livepatches stay bound to
exact targets. No fleet-wide coordinated update required by this unchanged
contract; deployment/recovery execution remains separate. [Preflight lesson](../../notes/vpsadminos/2026-11-17-kernel-update-preflight.md).

Next: explicit integration direction if desired. Preserve refs/worktrees/session
and all recovery contracts. No archive/delete/stop/cleanup is authorized.
[Handoff](handoff.md) and [plan](plan.md).

https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-17-stable-kernel-update/

## Integration authorization and fresh baseline

User explicitly directed "yeah you can merge your work" in the current chat
after passing CI readiness. Interpreted as vpsadminos -> existing target staging;
no deployment/lifecycle authority. M-prep assigned implementer0, outside claims,
for fresh baseline/clean target/hooks/feature evidence. Selected coordination
package now3shank2g0lxy3xnlh282djq0kjsbzanr; complete installed guide read.
Fresh SSH staging advanced to42baba6117bebcde3d04555a71377381df197925;
preparation owner investigates overlap/patch-equivalent rebase/check receipts
before claim. No claim held, no default mutation yet.
Linux default master and stale maintenance refs require separate correct kernel
promotion semantics; no forced unrelated history update inferred from merge.

## Latest user scope: Linux publication only

User clarified Linux is not merged anywhere and asked uniform instructions;
accepted proposed `vpsadminos-<upstream-version>`/no automatic tags with "yup".
L-publish implementer1 completed normal new-ref SSH publication at
refs/heads/vpsadminos-6.12.118 ->3bba27296b6f4f4a2b1568d65cea6037368f229b.
Fresh exact version/dated refs match; Linux master/floating alias unchanged.
No tags or source edits. [Publication receipt](linux-port.md) accepted.
D3 architect brief accepted: three OS instruction files plus narrowly scoped
three workspace instruction files, not runtime/schema/lifecycle redesign.
D3-OS owner implementer0; D3-W owner implementer2 in own workspace feature
worktree. Parallel disjoint repository/index windows. OS M-prep parked until
new docs committed/checked/affected review; no claim held. Lead applied required
prose pass to OS publication wording. Workspace default merge requires separate
explicit named-target approval after concrete final reviewed diff.
Source/build identity unchanged; existing kernel/runtime evidence retained.
Do not fake lifecycle completion if installed exact-default runtime contract
cannot express publication-only Linux; keep active and preserve recovery.

D3-OS final instruction headf33f5fd10b53232b5670862f832f4ec5ea835e84 on
42baba6117bebcde3d04555a71377381df197925, P2352449568afa3b2f5bd500dba3fbed1c1163e0b
and one catalog commit. Only three instruction files differ from prepared
ba6837de; source/kernel/catalog/flake/ZFS unchanged. Focused docs/skill/hooks
and exact identities pass; target remains clean42baba; no force-push/claim/merge.
D3-W three-policy-file diff adds Linux-only exception/crossrefs. AGENTS cap
regression corrected only in new completion bullet;16,381 bytes, declared
agent-instructions10tests/220assertions pass. Final commit and clean shared-base
rebase pending; no broader cleanup/runtime change. Lead writing pass accepted.

## D3 committed instruction deliverables and affected review

D3-OS accepted final committed/check evidence atf33f5fd10b53232b5670862f832f4ec5ea835e84
on42baba6117bebcde3d04555a71377381df197925; P2352449568afa3b2f5bd500dba3fbed1c1163e0b.
All source/catalog/inputs unchanged; only three instruction files added to
previous accepted process. M target clean42baba and hooks prepared.
D3-W accepted9610ea74a70d4b9b9d0f2d9296ea4908c0d4725b on shared master066f7b2c;
one three-file policy commit+31/-7, 16,381byte AGENTS, declared10tests/220assertions
and link/anchor/diff checks pass, clean hooks untouched. Initial remote-base
5cde..68eb cleanly rebased066f..9610 with range-diff'='; no tracking copied.
Same retained reviewer0gpt-6.1-sol/xhigh/read_only assigned affected final review
on both committed D3 ranges, all applicable lanes; reuse unchanged prior kernel
review/CI exact scope, no new source audit/full tests. No claims held.
Workspace integration approval not yet requested; required concrete review first.
OS existing integration approval remains valid for user-directed publication
instructions and disjoint clean baseline rebase; source pin unchanged.

D3 affected review[review-d3.md](review-d3.md) PASS/NOFINDINGS, same verified
reviewer settings, exactOSf33f5fd/workspace9610. All intended D3 docs committed
and quick checks pass. Complete histories/migrations/update streams accepted.
M owner released to publish final OS topic with exact old-head lease; lead
will acquire short vpsadminos claim only after publication/preparation complete.
Separate workspace-master merge approval requested after review, no claim
held while waiting. No kernel source change or new manual product build.

## OS integrated

vpsadminos remote staging now exactf33f5fd10b53232b5670862f832f4ec5ea835e84,
ordinary ff-only merge/push fresh remote proof. Merge claim18d77fd8-4316-4a4c-906f-e9b12874698a
verified held then explicitly released/verified20:14:23UTC. All effects known.
Linux version branch publication complete, no Linux merge. Workspace policy
commit9610ea74 reviewed/checked; its separate master-approval question pending.
No archive/delete/stop/deployment authorization. [Integration receipt](integration.md).

## Final integration checkpoint

OS remote stagingf33f5fd confirmed and repo claim18d77fd8 released/verified.
Linux version publication3bba2729 exact and oldrefs retained. Workspace feature
9610ea74 published SSH, fresh ref exact, comparison066f..9610 captured, clean.
Only new workspace default integration remains approval-gated; no claim across
that wait. Post-integration main run44167132711 workflow162100852 attempt1 on
f33f5fd runtime-ci observera4162505-8c79-4f38-89d7-f611018ed671 durably observing.
No deployment/session cleanup, no unknown command effects.

## Workspace master integration authorized

User explicitly answered "ok, yes merge it" after the question/explanation
identified the reviewed three-file workspace instruction change and target
master. Approval scope: aither64/vpsfree-cz-workspace refs/heads/master, final
reviewed policy head9610ea74a70d4b9b9d0f2d9296ea4908c0d4725b. Original OS
approval/integration remains separate and complete. Review-D3 full series
066f7b2c..9610ea74 PASS/NOFINDINGS; one focused commit, no migrations/obsolete
history/repeated streams. Quick10tests/220assertions and links/size checks pass.
Fresh preclaim inspection: shared master066f7b2c, feature9610ea74 clean; owned
policy files clean in shared checkout and index empty. Selected coordination
guide unchanged by SHA2562d83395295266c0693bddc3e3af9b8bedd5305858be12f37bf26d036be5ffa43.
No claim held while preparing; acquire workspace only then try tracking lock
nonblocking, fresh refs/fast-forward/hooks/SSH push/remote proof, release before
records/CI. Preserve all unrelated dirty shared paths/index. No lifecycle action.

## Workspace master integration complete

User explicit approval "ok, yes merge it" applied to reviewed three-file
workspace instruction change and master target. Claim
c7e63d4c-333b-49b5-9704-4067ce988154 acquired/held verified. Took shared
dev-session-tracking.lock nonblocking after claim, confirmed master066f7b2c,
feature9610ea74, fresh remote master5cde17b6/topic9610, clean owned policy paths
and empty index. Ordinary ff-only merge to9610 succeeded; shared unrelated
tracked dirty path status unchanged and index remained empty. SSH normal
HEAD:refs/heads/master push succeeded, fresh exact remote proof
9610ea74a70d4b9b9d0f2d9296ea4908c0d4725b. Tracking lock released, claim
explicitly released and authoritative status verified released21:13:14UTC
before records/CI. No uncertain mutations, branch deletion or lifecycle action.

Final delivery: OS remote stagingf33f5fd10b53232b5670862f832f4ec5ea835e84,
workspace remote master9610ea74a70d4b9b9d0f2d9296ea4908c0d4725b, Linux
version branchvpsadminos-6.12.118 exact3bba27296b6f4f4a2b1568d65cea6037368f229b.
Linux was published, not merged; default/floating aliases unchanged. New
post-integration OS CI44167132711 attempt1 remains in progress, runtime
observera4162505-8c79-4f38-89d7-f611018ed671 retained. Previous complete110test
CI/source review and D3 docs review remain accepted within proven scope.
Session lifecycle remains active/open; no archive/delete/stop/deploy/cleanup
was requested. All repository claims released; no machine claim exists.

## New user-authorized configuration update

User request: update vpsadminos in vpsfree-cz-configuration channels staging,
os-staging, production, and merge it. Defaultmaster integration authorized,
no deployment. D4 architect0 assigned bounded channelmapping/command/check
brief; C4 implementer0 capacity confirmed, owns config source/index window,
prepares declared hooks now, actual role updates wait accepted sufficientbrief.
Own worktreeworktrees/<slug>/vpsfree-cz-configuration created at9c6a0313d1689099c1dfcb065171a4aead44f183.
Checkout clean, hookexit78 missing freshbundle; no bypass/mutation, setup
owner resolving before ordinary registration retry. No claim held.
SourcepublishedOSf33f5fd verified; postmergeCI44167132711 still active, exact
previous kernel/source CI and review receipts retained.

D4 brief accepted/gate released: role-only grouped confctl update
'{staging,os-staging,production}' vpsadminos, alltargetf33f5fd published staging.
Old stage/os-stagea7d71a54; old productione643cbef. Preserve distinct Nixpkgs
follows and all unrelated logical input identities; matching target transitive
OSlock graph implies no extra revisionchanges expected. One generated lock-only
commit/changelog, quick channel/inventory/sourcecatalog/kernel eval + hooks;
no fleetbuild/deploy. C4 owns complete execution nowafter hooksetup, including
semantic graph evidence and clean target preparation. [D4 design](design.md).

C4 hooksetup ready: declarednixshell/bundle pass~65s, Ruby3.4.12/confctl/
overcommit/nixfmt available, tracked/indexclean; allsetupwatcher effectsjoined.
Lead ordinary worktree add retryexit0 configregistered; unrelateddetachedOS
merge-target warning left untouched. C4 actual grouped role update proceeds.

C4 generated commit15e3b9af90276e41d19e6a33477add58e5f9a8c9 completed with
normal hooks, generated changelog intact. Lead direct diff inspection: only
flake.lock+9/-9, locked revision/hash/timestamp for exactly three selected
roleinputs to publishedf33f5fd1; no substantive handwritten change. Content
review mechanical-dependency exemption applies subject final graph/eval checks;
independent final history/no-migrations/update-stream conclusion will still
precede merge. Config worktree clean, no claim held, quickchecks in progress.

## C4 integration complete — 21:28 UTC

User explicitly requested the three configuration channel updates and "and merge
it". Accepted C4 commit and reviewer0 whole-history PASS/NO FINDINGS before
claim acquisition. Claim `c73b14ea-802c-4727-a744-1d3b772d8fd7` verified held;
fresh SSH master remained `9c6a0313`, topic exact `15e3b9af`. Clean prepared
detached target fast-forwarded normally, with no hook errors. Ordinary SSH push
and fresh ls-remote prove remote master exact `15e3b9af90276e41d19e6a33477add58e5f9a8c9`.
All command effects joined, target clean; claim explicitly released and status
verified released at 21:28:04 UTC before records. No machine claim or deployment.
No remaining C4 implementation/review/integration work. Existing OS CI observer
continues; no duplicate watcher or session lifecycle action.

## Post-integration CI failure received

Runtime operation `a4162505-8c79-4f38-89d7-f611018ed671` reported run
`44167132711`, attempt1, workflow162100852 on exact `f33f5fd1` failed.
D5 assigned architect0 after saved roster/access verification; earlier D4
accepted. First milestone: failed job/step and causal error from completed logs,
then bounded source/input comparison and smallest next action. No blind rerun,
new watcher, source fix or deployment. Config integration remains delivered,
but current OS CI qualification is failed pending diagnosis.

D5 first milestone: build/cache job134336075924 passed (20:32:50–20:37:38 UTC).
Test job134350733756 on gh-runner1 started20:39:45; GitHub marked failure21:39:53
with annotation "The self-hosted runner lost communication with the server".
Run-tests step has no completion; later steps pending, logs404 BlobNotFound,
no artifacts. No assertion failure or runner root cause established. Prior
passing test job used same runner. D5 architect finishes exact source proof and
bounded authoritative runner-access/log-path brief, then implementer will inspect
read-only evidence if accessible. No rerun, source change or deployment yet.

D5 accepted: exact current build passed; runtime unknown after runner loss.
Workflow/tests/flake+lock/Linux/ZFS identical to prior passing head; publication
prose and exporter Puma bump are sole old/new delta. Config proves intended
SSH endpoint root@gh-runner1.int.vpsadminos.org (172.16.4.21), no access tried
by architect. I5 assigned implementer0 after capacity/roster check: read-only
runner state, exact test-state and bounded journals; no service repair/rerun/kill.

I5 causal milestone: trusted runner SSH reachable, uptime30days. Actual
github-runner-runner.service failed with ABRT/ExecMainStatus6. At21:39:53.387UTC
System.IO.IOException "Disk quota exceeded" occurred writing its _diag log,
service failed21:39:57. No matching kernel/OOM entries in bounded journal.
Existing GC active/later deletions observed; no recovery was performed here.
Exact test-state/process and current capacity evidence remain pending.

## D5/I5 accepted: runner capacity failure, runtime qualification incomplete

Read final [verification](verification.md#i5-runner-local-causal-inspection)
evidence. At21:39:53.387UTC the runner failed a diagnostic write with "Disk quota
exceeded" and aborted; unit remains failed/MainPID0. Existing automatic GC
subsequently finished21:47:51UTC, deleting46756storepaths/freeing360.3GiB;
current24Gused/329Gfree. Exact failed-time quota consumption is unknown. No
surviving runner/test/QEMU processes, exact private attempt state or terminal
results were found. No service restart, cleanup, CI rerun or code change done.
All three bounded SSH reads joined with no uncertain effects. Diagnosis accepted;
no kernel/source fix justified. Earlier110-test results retain original scope.

Next operational work, if undertaken: runner capacity/headroom assessment and
owned service recovery, then intentional CI rerun. These are not executed or
claimed authorized deployments. Integrated refs unchanged. Session remains
active/open; no lifecycle or cleanup action. All merge claims remain released.

## User disposition: leave failed post-integration CI as-is

User: "well it already passed on the previous branch, so let it be".
Retain original passing110-test result and proven unchanged kernel/ZFS/test input
scope; do not relabel failed run44167132711 as passed. No further runner
assessment, recovery, CI rerun or source change is requested. All requested
source/publication/integration work is delivered. Session stays open with
lifecycle front matter unchanged; no archival/stop/cleanup authorization.
