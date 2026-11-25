# NFS cancellation protocol candidate: independent committed review

Root's saved reconciliation of reviewer0's complete delivered report, received
2026-11-05. The complete original report is retained in this session conversation.

**COMPLETE — no findings.** No Blocking, Important or Advisory implementation or
history finding. Root ACCEPTS the affected review. This grants no publication,
execution, integration or deployment. Candidate N remains unpublished and has no
VM/runtime qualification. Both exact-F functional failures remain unwaived.

## Reviewer identity and scope

reviewer0, thread01a1a24e-920c-7b82-9fff-7754d1f947ab, saved gpt-6.1-sol/xhigh,
review purpose/reviewer behavior/read_only, ready/independent/capacity free.
Current session and both environment markers matched exact
2026-11-03-livepatch-fixture-failures/workspace /home/aither/workspace/ai/vpsfree.cz.
No fallback/settings override/source authorship/nested reviewer. Mandatory skill
and all FOUR full references applied: general, architecture/repetition,
scope/proportionality, risk/compatibility, overall HIGH for privileged guest
namespace/sysfs cancellation/recovery. Workspace/repository/patch policy and full
packet/current A/design/brief/native audit/shipping review/read-only source/history
and saved receipts inspected. Prior review reused only for unchanged first3 scope.
No source/session writes, checks/test/eval/build/ELF/network/API/CI/VM/Git mutations,
service/lifecycle/cleanup or nested agent occurred.

## Exact bindings and inventory

Repo vpsfreecz/vpsadminos, eventual target staging. Branch
2026-11-03-livepatch-fixture-failures-native-nfs-protocol, isolated unregistered
checkout /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-03-livepatch-fixture-failures/vpsadminos-native-nfs-protocol.
Complete base d2fe1489f0b0b213fb247aeee6e081d349adaf42;
exact parent F56b9363db1f1039e5d684dadc260cdffe7497e08;
N74297e22953f5f3186d7fcdcfe304eba10fb84f7;
Ntree c2899100faba19cdd022229b60693f4cc88391ce.
Complete range4purposes/25paths/+3679/-239. F..N sole path
 tests/suite/osctl/nfs-cancellation-common.nix,+42/-2,100644,
blob0a15d61db8e524323e25076cabd64dc8b9e9de5a.
Actual HEAD/parent/base/branch/history/modes/source/index/nonignored-untracked
clean verified. Primary remains clean exactF; no CI status polled.

Independent bindings:

- Source SHA2beb7a7299de0f744edb4ec84e79648795be98aa39c48736192990a3b54ce103.
- Actual38line writer SHAc17bc4c34fe480df26e5353f3342c48594bd83b63ce2819ee16b5f7fa157a2b6,
  byte-equal to controls. All source outside replacement block byte-equalF.
- Binarydiff SHAef9ddeac7aa722af18f764f43df9e4a235a6cb3a843a4a0fe68eb2eba2cdb32e.
- Rawmessage SHA50a0d2c5d3b91fdcae5ec0c3f801d1cc98a3c34ef49fe5573465738d371d66aa.
- Lock unchanged67487674fa38049fede8047dbf8d7302971a3b19ea2866cf6f954e3a2e5ad656.

## Protocol correctness

F's default NFS3 example62/65 required host echo failed EBUSY; later examples
63–65 do not complete it. Existing production patch source3481 rejects inactive
facility EBUSY, validates host authority/noninitial userns/value1, invokes subtree
cancellation and returns fullcount only on success.2453 propagates RPC cancellation
failure;14078 explicitly returns retryableEBUSY if pernet write trylock fails before
barrier publication;3515 readback returns exact0-newline/1-newline or fails if
inactive. Existing daemon nfs_cancellation.rb326 retriesEBUSY with <=50ms sleeps
under30s worker budget; adjacent specs cover transient/permanentbusy/no fallback.
These files have no feature delta d2fe..F: preexisting contract, not proof of the
specific F EBUSY branch/lockholder/inactive-module/scheduler/kernel cause.

Reviewer finds new writer813 correct: monotonic30s budget checked before each
attempt, remaining-capped <=50ms sleeps; permanentbusy fails. Only inner open/
syswrite block rescuesEBUSY. Samecontrol/namespace/fullpayload each attempt.
Descriptor closes in ensure; close errors escape rescue, so no retry after close
failure. Unbuffered syswrite1-newline must return2; partialwrites fail without
writing remainder. Close followed by immediate exact1-newline readback; read
errors/false/malformed barrier fail without another write. Othererrno/interruption
escape, outcome line does not convert exception to success. Partial-effect failure
keeps outage-rule ensure.30s bounds returned-EBUSY retry attempts, not a blocked
syscall; original outertimeout unchanged. This is protocol operation retry inside
one execution, not test rerun or EBUSY-as-success.

## Consumers and preserved assertions

Host853–855 uses explicit existing ruby_vpsadminos provider and ordinary nested
Shellwords escaping; test_evaluator already requires Shellwords. Ruby3.4 overlay
is existing osctld runtime, not ambient/fetched/new package. Original root route
enters sameinit network namespace, one private mountnamespace, make-rslave/sysfs
mount once. No perattempt namespace, tenant-sys traversal, new privilege or foreign
cleanup. Inline process owns only its control fd and fixed outcome/count/time log.

Actual consumers inspected: patched frozen.95 nfs-cancellation.nix, native6.12.110
nfs-cancellation-native110.nix, unpatched frozen.95 baseline, commonNFS3/4.0/4.1/4.2
and current selection. Changedwriter is nonbaseline only; baseline absence/softIO
expectations unchanged. Common file is correct owner. Small inline writer avoids
coupling direct authority test to internal daemon object; shared production
abstraction unwarranted merely for30s/50ms correspondence.

Outside-block equality preserves race/setup/init/control/options/two2049 DROP
rules, readiness30s, mounttermination60s, reachable-network admission15s, stopped
state/neighborwrite/clientrestart/remount/later integrity/idempotence/cycles/rule
ensure, negativepermission/value/readability/baseline tests, fullnative/all65,
fullworkflow/native+ALL9/original14400/semanticidentity/CPU127/health/deadline/
stop/recovery/teardown. No new assertions invented for F's failed body.

## Scope, compatibility, docs and checks

Conventional concrete one-file baseline test-caller repair, separate from approved
shutdown and semanticresolver. No kernel/daemon/provider/runnerAPI/schema/persisted
state/publicprotocol/Nixoption/deploymentorder/fleetupdate change. Existing control
protocol, changed test caller only. Rollbackcontent F onefile; no rollback run.
Actual native110 runtime/provider remains gate. Commit/local code and session
brief explain rationale/constraints; new productmanual/upgrade/migrationguide not
useful for this isolated caller repair. Unchangedfirst3 docs retain prior review.

Reviewer inspected saved20/20 controls of actualextractedwriter: immediate,
transient open/write/bothbusy, perpetualopen/write,EPERM/ENOENT,partial0/1,
false/malformedbarrier,readEBUSY/EIO,closeEBUSY/EIO,deadline-before-retry,remaining
sleepcap,actualselfSIGINT. Controls inspect payload/attempttimes/close/readcounts/
error/outcome; no openat/afterbudget and no close/read-write retry. Caller controls,
not copiedalgorithm/kernelmodel; no sysfs scheduling/faultcause proof.
Hostassembly control checks originalnamespace/mounts, decodedargv/exactpayload,
renderedBash syntax. CachedRuby substitutes Nixinterpolation without moduleeval/
guestprovider/VM proof. Nixparse(noeval)/Nixfmt1.5/Ruby3.4.11parse+RuboCop/
whitespace/normalcommitmessagehooks pass. Initialfilename lint/messagewidthwarnings
resolved/retained; sourceidenticalmessageamend finalhooks clean. Standard hook
trustsign updated sharedbareconfiguration-signature key normally, no copy/bypass;
primarysource/index/ignoredinputs unchanged. Later primaryhooks may need normal
trustsetup. GitRELEASE21:39:34.549318Z before records/review. Broad osctld preloadgap
unchanged/unavailable beforeexamples, notgreen, no daemondelta to rebuild it.

## Independent whole-history, streams and migration conclusions

Complete ordered d2fe..N:

1.32d7687402b6d4ff6bc2cf583f6431a6ad6dbeee currentmodule witnesses.
2.ee32b9cf5b6c88bfbbb6944eff911f69d26664ea boundedOSVMboot.
3.56b9363db1f1039e5d684dadc260cdffe7497e08 approvedshutdown.
4.74297e22953f5f3186d7fcdcfe304eba10fb84f7 independentNFScallerrepair.

First3 exactobjects/messages unchanged, not reconstructed. N independently
meaningful baseline repair, not regressioncaused byfirst3; separate review/bisect
boundary. Earlierwrapstate foldedowner. **No obsolete implementation,fixup/WIP,
revert,diagnosticcollector/age/selection ancestry or skipmarker remains.**
**No repeateddependency/channel/input/generatedupdate stream d2fe..N.** Canonical
unstableupdate already baseline, N no pin/lockchange. No redundantintermediate.
**No migrations** in completeinventory, no database/schema/seed/persistedprotocol
transition, no migration merged/released/deployed/externallyconsumed or predecessor
lineage. Runtime F receipts are not migrations and remain preserved. Actual refs
confirm tested645927+13provenance, ordinary802898,instrumented08e,detached5235;
QEMUsource/patchretention recordedunchanged. No old-object literalmerge/publication
or successor qualification claimed.

## Disposition and runtime gates

Affected review COMPLETE, nofixesrequested; rootacceptance does not release run.
After separate release require actualprovider/fullwrite/close/exactbarrier in
selecteddefault/native110,all65examples/integrity/isolation/stop/restart/remount/
health/cleanup/VMrecovery. Busycount is evidence, notcause. Permanentbusy/inactive/
timeout/othererrno/laterfailure gets namedassessment, no blindretry/budgetgrowth/
healthwaiver/kernelguess. Fnative321/323 two bodyfailures still unwaived; Nlocal
controls/native110comparisons do not repairF62/65. Miscmonitorpidfd/setnsESRCH
is separate, heldobservation/targetgap unsolved. SixLeap16.1passedF, oldexception
covers neither. PrimaryF/run42079730277/solewatchci_final_resume untouched.
Full exactFINALnative+ALL9/original14400,then-currenttarget/input/history and
ordinaryhooks/integration checks remain before conditionalstagingmerge. Source/
closure/runtimeidentity not transferred byunchangedlock/oldtuple. SessionOPEN.
No reviewer clarification pending.

Stable session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-03-livepatch-fixture-failures/
