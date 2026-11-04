---
lifecycle: active
---

# Current state

Phase: final candidate extraction and runtime verification.
All product changes are committed and published at
`742eb30cb1a8b6766c85e915d26b0400e38244b1`, tree
`19f423e70ff439867d4bb27e8ed07b9c95fdb703`. The clean feature branch has three
logical commits, seven files (+27/-14). Source syntax, formatting, full
Overcommit and active hooks pass. Fresh utility final_image_batch_native owns the running four-image batch;
no candidate runtime assertion has run yet.

The user approved integration: “when done, you can merge it”. This covers the
sole affected repository vpsadminos into its default `staging` after checks and
review. It does not authorize production image publication, deployment or any
session lifecycle action. Leave this session open.

## Phase checklist

- [x] Session/environment identity and retained team/access verified.
- [x] Replace shared Leap 15.5 builder with explicit 16.0; add 16.1 support.
- [x] Prove device-unit root cause and commit explicit udev plus xfail removal.
- [x] Complete final series and source quick checks/hooks; publish feature.
- [x] Restore/GC-root exact immutable source and fixed native runner input.
- [x] Final selector discovery: exactly four images and both openSUSE device cases.
- [x] Independent whole-branch final review; no Blocking/Important findings.
- [x] Fresh normal image tests: all four passed15/15, batch exit0.
- [ ] Original device assertions against each rebuilt artifact; final 16.1
      start/stop, /run, routed networking and cgroup v1/v2 checks.
- [ ] Reconcile final-head GitHub feedback and public-image prerequisite.
- [x] Conditional merge approval and clean target/hook preparation.
- [ ] Short claimed integration, remote ancestry proof and claim release.

## Repository and ownership

SSH origin `git@github.com:vpsfreecz/vpsadminos.git`; default `staging`.
Feature `2026-11-03-opensuse-leap-image-build` in
`worktrees/2026-11-03-opensuse-leap-image-build/vpsadminos`.
Base `dd188397abe37d0bc33f4c5dfb3605206ce5e326`.

1. `4c2a38bc02d1d10c208d478c01ec90057995825e`: shared builder upgrade.
2. `57871a8e3f8f429e86e3ad6abf16de99a44e9416`: new 16.1 scripts/registration/matrix.
3. `742eb30cb1a8b6766c85e915d26b0400e38244b1`: udev and original device assertions.

No migrations, repeated pin/input updates, kernel/host/API/protocol changes or
coordinated fleet update. The dedicated-builder trial is absent from this
series; old refs and evidence remain recovery history. Final message predecessor
c856 has the identical tree; prior AA is substantively superseded.

Architect0 owns design briefs; implementer0 completed source Milestone1 and
clean integration preparation, then relinquished Git ownership. Implementer1
completed Milestone2 and now owns the bounded test-input correction only.
Reviewer0 (retained gpt-6.1-sol/xhigh/read-only) completed all four final-review
lanes, conservatively high risk for shared image/init/rollout behavior.
[Final review](review-final-result.md) has no Blocking/Important findings. Its
builder-refresh documentation advisory is accepted as nonblocking follow-up;
the existing reuse behavior and fresh-state requirement remain explicit. Lead
owns acceptance, tracking and approved integration. No repository or machine
claim has been acquired; no commands remain active from target preparation.

## Evidence and next steps

[Final review packet](review-final-packet.md) includes the complete series/diff,
history/migration inventory, quick checks and acceptance criteria. Earlier AA
reviews do not cover this final series. [Device result](device-unit-result.md)
records causal proof: absent udev, strict 15-new-package closure, restored
network, ordinary restart, eth0 active and dummy absent→active. The live-install
reload warning is explained; fresh bootstrap must still be clean.

[Verification preparation](final-checks-742eb30cb.md) defines one fresh-state
four-image batch and candidate assertions. Fresh state prevents name-keyed old
15.5 builder reuse. The first global mkForce memory input conflicted with an
unrelated forced fixture before any VM. V2 priority60 passed native evaluation
(image8192/namespaces4096); its listing then found the recorded immutable source
path missing. No build/VM ran. Implementer1 restored the exact source and proved2371 files/modes/noextras plus
unchanged NAR, rooted source and runner, and checked all wrapper dependencies.
Fixed final-runner-742eb30cb-v3.sh hash
c13929304f04033528bba1b5e98bd24bde862a35b2d6d6d9aa234631790c4e06
is the execution input. Product source is unchanged. See [first discovery](final-discovery-result.md)
and [v2 discovery](final-discovery-v2-result.md). No blind runtime retry.

[Merge preparation](merge-preparation.md) records a clean detached target at
`/tmp/2026-11-03-opensuse-leap-image-build-vpsadminos-target`, matching staging
at the base, with Nix environment/hooks trusted and active. The merge waits for
final review and verification; acquire no claim while waiting.

Final-head CI runs 41714889091 and 41714888844 are both queued in the fresh
read-only [CI snapshot](final-ci-feedback.md); current-head runs remain untouched.
The final comparison was captured at base dd188397a and head742eb30cb. Public latest still represents an older
image, and changed-image CI does not publish. Local candidate proof must be
kept distinct from public-image availability. Source integration cannot update
existing containers or public images; publication is separate authorized work.

The nearby helper comment supplies lasting package rationale; conventional
image addition needs no broader project documentation. Individual experiments,
input identities, rollout constraints and superseded receipts remain here.
[Earlier state](state-prior-final-review.md) and the linked implementation,
review and runtime records preserve the detailed history. All diagnostic
VMs/server/locks were closed normally; retained disks and logs remain intact.

Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-03-opensuse-leap-image-build/

Final batch preflight: available RAM65442MiB and shm35222MiB; fresh state path
absent. Utility will recheck before two8GiB guests. Implementer1 prepares only
the dependent final candidate inputs while utility owns active verification.

Discovery v3 passed both selectors (final-discovery-v3.log/result). First batch
launch failed before runner invocation because utility added unavailable
/usr/bin/time; no VM/state existed and operation closed. Fresh utility
final_image_batch_native launched the exact fixed native command without that
wrapper, retaining full final-images-native-742.log and fresh-state path. Do not
duplicate this run or poll its logs while utility owns it. Implementer1 prepares
one export and one focused input only, no concurrent guest/server/test action.

Runtime milestone (owned utility receipt): final742 native Leap16.1 and16.0
image tests each passed15/15, runner successful at1245.64s and1293.28s.
Leap15.6/Tumbleweed now running in the same owned batch. Full source/scriptlet
acceptance and artifact receipts wait for completed batch; no export/focused VM
or server started. User explicitly directed waiting for results; do not yield
with another intermediate final response while required results are pending.

Final normal batch completed at742:60/60checks,4passed,0failed, noexpected
failures. All guests/runner closed normally. Exact primaryJSONSHA and realized
system/kernel/initrd/source identities are in
[batch result](session/final-images-native-742-result.md).
Implementer1 accepted frozen16.0/16.1 bootstrap audit and is auditing frozen
15.6/TW. Preexisting ineffective900s timeout sed adjustment is explained in
final-completed-case-audit-742eb30cb.md; it is unrelated to udev and accepted
as a nonblocking coverage limit, with no unrelated source edit.
Fresh utility final_candidate_exports owns four serialized retained-debug
exports using fixedinputf5a280a7..., primaryJSONhash guards before VM work,
no downloads/rebuilds. Candidatepacket final-candidate-checks-742eb30cb.md and
focusedinputcab2b7ce... accepted. No HTTPserver/focusedVM started yet.

All four final exports passed with normalVM/PTYclosure. [Export receipt](final-candidate-export-742-result.md) binds actualrelease/archive/repository hashes and successfulprimaryJSON guards. Frozen bootstrap audits accepted for allfour targets. Fresh utility final_candidate_runtime now owns the localforegroundHTTPserver and9focusedcandidate cases (atmost2VMs), fixedinputcab2b7ce...; no publicfallback or sourcechange. User instructedwaitingforresults; do not endturn prematurely.

Runtime utility final_candidate_runtime stopped before anyserver/VM with an
incorrect missing-candidate preflight report. Lead literal ls/find and complete
SHA256 of all4hostarchives prove candidatepresence+exactexporthashes; runtime
resultoutputfile is not an inputprerequisite. No candidate recovery/rebuild or
source edit needed. Fresh utility final_runtime_verified_inputs now owns the
9-case runtime/server batch with explicitrawfilesystemguards. No previous
focused/server operation remains live. Do not inherit the falseabsence claim.

Progress response final-candidate-launch-loop: two runtime launches stopped
before VM action (falseabsence; inventedselectorprefix), not productfailures.
Literal final-candidate-commands-742.json now contains exactninecommandstrings,
pryEval and freshfocused2states; utility focused_literal_commands executes
verbatim, firstcasealone beforemax2remaining. Previousserverclosed/portfree.
Next observable milestone is firstoriginaldevice script completion; any further
launch failure is a specificfixtureblocker requiring diagnosis, not genericretry.
All accepted source/build/export evidence and architectbriefs remain unchanged.

Socketfixture correction: implementerproved original117-bytepath; manifest
now d37ff138a5be07b4ae23dd46e7ee0571a17eaff26b0c88117df97213009f2b98
uses unused /tmp/osl742-{d156,d160,d161,dtw,ss,run,net,cg1,cg2}, max59bytes.
Oldlongmanifest preserved. PreviousPry/server closed; leadnonblockingflock
proved oldstatelock released. Active utility focused_short_paths owns server
and9casebatch, newtranscripts session/focused-short-742/. FIRSTCASEPASSED
on15.6: INPUT/JSONsuccess/PASSEDmatchsource+SHA, eth0status0,dummybefore3,
create0,dummyafter0,cleanup0, normalVMclosure. Remaining8startedmax2atatime.
Progress response final-candidate-launch-loop resolved by this actualnative
result; no source/payloadchange. Do not start a duplicate runtime/server batch.

Pre-merge acceptance: ALL9focusedcasespassed at742, raw INPUT/JSON/PASSED
markers independently inspected and matched expectedartifact/source hashes.
Leadproved all9statelocks released with nonblockingflock; serverport18080closed.
Utilityfinalreceipt writing is routineevidence, no source/packagecontractchange.
Complete source inventory rechecked:3logicalcommits,7files+27/-14, exacttree19f,
cleanfeature742, no obsoleteupdates/migrations perindependentreview. TargetNix
environmentready (Overcommit0.74,Ruby3.4.11,nixfmt1.5.0), samepreparedtoolpaths.
LatestCIread: changedimages41714889091 queued; CI41714888844 in_progress, exact742.
No CIgreenclaim; publicimageavailability remains separaterolloutprerequisite.
Usermergeapproval applies to vpsadminos/staging; sourceintegration mayproceed
with knownpublicCIlimit after localcandidateproof, as reviewed. Next is short
repositoryclaim/freshtargetcheck/ffhooks/SSHpush/remoteproof/release only.
