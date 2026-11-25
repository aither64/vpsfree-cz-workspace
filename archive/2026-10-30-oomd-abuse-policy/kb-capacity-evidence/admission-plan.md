# Bounded full screenshot capture admission proposal

Source/history is cleared at KB7bdee285d62343c653b5a8c5cfdeab2d97ef7f4d, selecting
appf60d41a453b1703e42de4341285bdc6ba339aff0 and unchanged OS6bdf458f. Ordinary
source CI41187229857 passed separately. Original local fullcheck remains FAILED
with architect/lead/reviewer accepted pin-only baseline exception; targeted PASS
and suffix PASS remain separate. No further source changes or pins planned.

This is a measured, read-only plan, not build/runtime admission. The sole active
Luna/low utility watches exact Managed41187229710 (parenthandle22007). It is allowed
to continue normally; its guarded CI allocation does not qualify four PNGs.

## Owned inputs and immutable identities

Private config/state/output/logs stay beneath
work/2026-10-30-oomd-abuse-policy/kb-capture-private. Root0700/config0600, ownerUID1000,
configSHA25630c820f3abf8212ae063a40d6d3f8709072fe9820bd1dbe1c3a493b4c18f8958.
Config uses synthetic example.test domains/users and namespace blocks1/9/17,8each.
Bridgebr0/gateway172.16.106.1; dedicated requested addresses181–184. DNS guests are
disabled as already prepared. No reduced profile or extra nodes.

Exact immutable source /nix/store/ay80icp9ic32kiz768w8h1h72w1p0wxa-source.
Runtime output /nix/store/sy0lmmncppg4aq2rw87c8hghfkz2n1bg-vpsfree-kb-devcluster;
runtime drv /nix/store/x6061r7bq5qi1fdignczmvicpl5axbs5-vpsfree-kb-devcluster.drv.
Capture+validator output /nix/store/l5jjw7nz1k1kryadshhf3zwxw8li6sda-vpsfree-kb-capture;
drv /nix/store/4mpj34ral62dqb8lwg8ch8b0008qc9hx-vpsfree-kb-capture.drv.
Validator executable is vpsfree-kb-validate in that same immutable package.
Runner /nix/store/psqb6ijqfapg37kpdvz9fzlp3qn3x2a3-vpsadmin-kb-capture-cluster-runner.
Full drv/output identities in package-projection.json, complete input graph in
../kb-shared-source-evidence/full-graph.json. None of these outputs was realized.

Public Nix projection uses this config and documented screenshots/bridge topology.
Actual native credentials/instance/artifact identity do not exist yet, so projected
system/image outputs are planning identities, not future guest attestation. Do not
build that placeholder image. Public start must create/build/attest its own exact
artifact; record its real source/config/closures before fixture mutation.

## Current prerequisites and capacity observations

Native public status reports schema2foundfalse/stateabsent for exact ownstate.
No KB guest/image/runtime ever consumed old1119/197pins; only unit-test synthetic
fixtures ran. KVM exists+r/w; br0UP at172.16.106.40/24, helperavailable. Four probes
181–184 got no reply; this is not dedication/reservation proof. Native publicstart
will atomically check its resource registry/responding-address refusals. No foreign
private state, reservation, cleanup or lifecycle operation was accessed.

Observed RAMavailable89754890240B(~83.6GiB), sharedmemoryfree50613551104B(~47.1GiB),
64affinityCPUs. Full topology: services4096MiB/4CPU, node1+node2 each4096MiB/4CPU,
backuper12048MiB/4CPU:14GiBguestRAM/16vCPU. Builder is4096MiB and completes before
guests start. Proposed positive overhead4GiBRAM/2GiBshm yields18/16GiB admission
checks, comfortably below current availability; refresh at actual start. Workload
fit still must succeed natively; no profile changes or minimum-fit guarantee.

State/store/tmp share root filesystem; observed available163173642240B(~152.0GiB),
46,286,540availableinodes. Ownprivatepreparation40KiB, no guestdisks. Owner0 confirms
no active/pendingheavyLOCAL allocation/reservation; its existing smallgems/IFD/logs
already reduce measuredfree and must not be deducted twice. Previous owner0
25/28/48GiB unadmitted estimates are not reservations. HostedManaged native future
allocation/growth must finish or be explicitly accounted before ownlocalstart.

## Cache and physical staging assessment

Exact projected source/package dryrun exited0:421derivations,223substitutions,
539.5MiBdownload/1.3GiBunpacked. Rounded2GiB substitution allowance. Services kernel
6.12.107/nodekernel6.12.95 and builderclosure6.18.48 all have positive exactpath
narinfo at cache.vpsadminos.org. Module-copy/shrink/initrd derivations remain to
build; no local kernel compilation authorized. Stop/investigate any unexpected
kernel build rather than consuming it. No closure/image/browser realized by plan.

Image builder inspected:12GiB rawimage, stagingroot populated by nixos-install,
then cptofs copies stagingroot into rawimage and postVM moves it to output. Its
builderRAM4GiB. Native fixedsize payloadfit check remains required; it can fail.
Scratch is not bounded by NAR sizes or clientTMPDIR; daemonbuilddir unspecified.
We therefore assess24GiB scratch/overlap (12GiBstagingcopy plus12GiB otherbuilder
headroom), plus12GiBfinalimage,10GiBnew Nix outputs including2GiBsubstitutions,
and2GiBprivateoutput/logs:48GiBnewbuildpeak. Add shared20GiBfloor:68GiB, leaving
about84GiB against current observation. This is conservative assessed headroom,
not a proven maximum; refresh and preserve native failures.

Runtime keeps12GiBimage+12GiBwritablecopy+10GiBnewclosures+32GiBphysicaltankgrowth
allowance+2GiBoutput/logs=68GiBnewpeak; with20GiBfloor88GiB, about64GiBmargin now.
Three320GiBtanks are sparse960GiBlogical, not960GiBcurrentallocation. The finite
32GiBcampaign allowance is explicitly a monitored physical budget, not full
future logical-growth protection or general capacity certification. Full fixtures
remain unchanged: production+playground VPS default120GiBquotas, mounted1GiBdata,
preseeded NAS and real snapshot. Thin quotas do not preallocate full contents.
Afterboot require nativepool/quota admission,≥1GiBservicesfree, actualtemplate/
poolheadroom and measuredfileblocks. Do not change package/pool/quota checks.
If actual growth exceeds allowance, stop advancing and report measured evidence;
no cleanup, resize, tmpfs, foreignstore changes or reduced fixture fallback.

## Proposed shortest supported execution package

After lead release, build only exact immutable runtime/capture-validator/runner
packages with normalNix max-jobs1/cores4; measure realized closures/rootfree. Then
refresh RAM/shm/disk/inodes/bridge/other-allocations and invoke the public start
once with existing private config, screenshotstopology, bridge and explicitstate.
Set process-localNIX_CONFIG max-jobs1/cores4 so native exactguest builds remain
sequential. Native start creates actual credentials/artifact, builds12GiBservices
image once, then claims resources and boots. No privateprepare or postbuildpause.
A fresh watcher owns each uncertain build/start/capture batch after currentCI
watcher finishes or policy permits; no parallel utility beyond cataloglimit.

Preserve shared20GiBfloor plus remaining assessed obligations at each stage;
refresh beforefixture/capture and refuse unaccounted competing allocation.
Record actualsparsefilelength/allocatedblocks once perinode/filesystem, guest
servicesfree/inodes/ZFSavailable and sourceclosureattestation. No guarantee from
boot alone. Native admission/source/ownership failure stops affectedwork unchanged.

OnlyfourPNGs: getting-started/vps-list and restore-backups/playground-vps-list,cs/en
into one explicitprivateoutputroot. Existingzero counts0/5+0/10; no newscenario.
Then update+strict exportedinventoryvalidation, visualreview all4, separate
generatedmedia/provenance commit retaining exactgenerator7bdee revision, publish
normallease and required exactmediahead hostedstrictCheck. No productionpagewrite,
merge, deployment or session lifecycle operation.

Evidence: package-projection.json, guest-projection.json, dry-run.log/result.json,
kernel-cache-proof.json, services-image-build-projection.json, host-observation.json,
owner0-allocation-coordination.json, admission-proposal.json.

## Approved generic-build actuals

Lead released the bounded execution package subject to native conditions. Fresh
prebuild root available170922590208B/RAM91874402304B/shm50613551104B passed assessed
thresholds. Exact generic runtime/capture-validator/runner build completed exit0
in28.78s using1job/4cores and ownedprivateoutlinks. No guest/config/image/kernel
built. Selected outputs allocate12,288+16,384+12,288B; deduplicated531path closure
allocates2,971,127,808B including preexisting/shared paths. Postbuild rootavailable
170856288256B, RAM91573821440B, shm50613551104B. Runtime source metadata independently
confirms exactKB7bdee/appf60. These measures are not attributed package-only free
space deltas because other host activity is concurrent.

Publicstart waits Managed41187229710 remaining physicalgrowth terminal or explicit
authoritative different-host/filesystem/accounting evidence. Watcher22007 remains
sole observer; parent has not queried CI inparallel. Owner0 no-local-allocation
report does not account hostedCI growth. No further approval question is needed
after conditions prove true; fresh postbuild admission will be repeated then.

## Managed terminal and actual public-start admission

ExactManaged41187229710 completed success at7bdee285, all12scripts/4tests successful,
test/evaluation/cleanupsteps passed. SourceCheckstepalso passed perfinaljobsJSON.
Watcher22007 exited; no overlapping observer. Fresh prestart rootavailable
170854756352B/RAM92743069696B/shm50613551104B and46550335inodes, KVMrw, bridgeUP,
config exacthash, nativeownstatusabsent. Accepted88GiBdisk/18GiBRAM/16GiBshm
thresholds pass. Released publicstart automatically launched through fresh
Luna/lowutility parenthandle47933, nativepackage7bdee/screenshots/bridge/private
configstate,maxjobs1/cores4. No placeholderimage or privateprepare. Actual
artifact/closures/readiness remain pending native success; fixtures not touched.

## Native execution outcome and held recovery

Genericbuildpassed. Freshutilityrefusedbeforestart dueincorrectabsentenv handling;
receiptpreserved. Lead acceptedvisibleparentfallback, bothliteralverifiedmarkers,
exactpublicstartonce. Actualstartreturned0after1567.1748s, guardedstatusreadytrue,
instancef66a2056-c6e7-4300-904a-c7d2758addae/runea841826-207a-4419-8e21-ea61bf3ea678/
artifact18190571-ae21-4206-94ef-c774e04f188c. No fixturemutation or capture.

Periodicprocess tracker died with EACCES reading/proc/2989738/exe; failedchild
identityunproven/nowabsent, bridgehelpercandidateunproven. Sourcepermitsmainstartup
readydespitetrackerdeath; knownincompleteownershipinvalidatedcapture. DirectUTC
artifact10:09:01/spawn10:09:05 (earlier09:49manualconversionwrong/superseded).

Lead authorizedonlyguardedpublicstoponceaftercontrollerreturn. Stopreturned1
after900.30199s: owned shutdown incomplete; processes, paths and claims retained.
All4guestQEMUexitstatus0; all29recordedPIDsthenabsent. TrackerjoinrethrowsEACCES,
processrecordcomplete=false. Finalpublicstatusstopping/readyfalse. Exactnative
registryclaimstillpresent/matchesreservation; socketnamespacecontainscontrol.sock.
No nativecompletion/claimreleaseauthority, so nocleanup/reset/force/retry or
source/permissionchanges. Allparentcommandsareterminal, recoveryevidenceretained.

Userchoiceforseparatereviewedruntimecompatibility/recoveryextensionversusblocked
KBrefreshispending. Existingpin/media packageheldatthisconcreteblocker, notabandoned.
No4PNGs, mediaacceptance, strictfinalmediaCheck or productionwriteclaimed.
Fullterminaleffects: public-stop-terminal-effects.json, public-stop-result.json,
runner-native-failure.log/.sha256, tracker-failure-diagnosis.md.

## Fixed-source follow-up (2026-10-31)

The historical7bdee attempt and its incomplete claims remain immutable. User
authorized root-cause repair; independent review and the narrow K1 fix are cleared.
Final corrected source56d716e0806fe9c5167f4b55750e5532767ae0ba has tested tree
9bf384bc70f34d8ec34d0216bfda85c7b3a376c6. Fresh full-source checker is still pending;
no new runtime/image/capture has started. Prior pin-only exception is not reused.

Read-only exact generic package projection/dry-run is in
../kb-tracker-repair-evidence/fixed-generic-projection.json and dry-run receipts:
6 tiny derivations,18.7KiBdownload/7.7MiBunpacked missing tools, no image/kernel.
Private fixed-source preparation uses a separate ignored0700root/config0600;
requested bridge addresses185–188 are disjoint from old181–184 claims. They are
not yet natively reserved or certified available. Old private disks allocate
12,892,549,120B, already deducted from observed146,834,071,552B free. Preserve a
separate32GiB old remaining growth obligation plus20GiBshared floor; prior48GiB
build/68GiBnew-runtime assessed peaks still fit this preliminary snapshot. Exact
fresh KVM/bridge/ownership/native claims and remaining hosted growth must pass
before public start. No old state/artifact/claim conversion or cleanup permitted.
Full current numbers/config hash/roots are in fixed-capacity-plan.json under the
repair evidence directory. These are measured planning facts, not reservations
or future capacity guarantees.
