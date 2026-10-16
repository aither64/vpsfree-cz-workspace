# Revised twelve-case runtime

Active attempt runtime-effective.yf2uje2x; exact clean published product
edb90d2fe2190d88d8b9d2d21bd0def79eedc898, tree66674e848f160c5dc7be63da6e14c590ef043ec5.
State /tmp/ni.p5mnmdxx; parent43016 owns execution, no duplicate.
Invocation: standard registered dist-config/nixos-persistence-upgrade#*,
short state root, empty test-config host-metadata route, no-destructive/jobs1.
Read ownership.json and invocation.json. Source review/I1 clearance is in
../effective-mounts-review/i1-disposition.md. No source changes during this run.

The actual source dependency closure and test JSON built without local kernel
compilation. QEMU boot was quiet at first, then completed host service startup;
no quiet-time cancellation or fixture/service repair was used.

| Case | Current result | Example elapsed |
| --- | --- | --- |
| fresh-ancestor-26.05 | PASS | 440.58s |
| direct-filesystem-bind-26.05 | PASS | 408.8s |
| upgrade-26.05 | PASS | 441.84s |
| fresh-26.05 | PASS | 378.54s |
| ancestor-var-26.05 | PASS | 428.49s |
| ancestor-var-lib-26.05 | PASS | 412.21s |
| dependent-mount-26.05 | PASS | 442.02s |
| declared-backing-26.05 | FAIL: old baseline payload-directory metadata | 138.24s |
| upgrade-unstable | PASS | 512.99s |
| root-backed-26.05 | PASS | 431.4s |
| storage-failures-26.05 | PASS | 1197.46s |
| upgrade-25.11 | PASS | 533.89s |

Fresh-ancestor runner reports success15:01:52+0200, script726.47s including first
host boot. The example proves fresh allocation through the ancestor without
exact state/log mounts, real account challenge/repeated activation/restart and
all maps/IDs/data/numeric-owner/machine-id/mount assertions. Actual source stats
remain0:0:755:128; parent remains0:1234:2775:6, exactly matching preboot metadata
and inode. This proves real SGID/group initialization without modifying the
pre-existing parent. Payload directory remains expected account-owned0750.

Original continuous logs live at
/tmp/ni.p5mnmdxx/os-test-dist-config__nixos-persistence-upgrade-8c45b496/
(test-runner.log, machine-shell.log, machine-console.log, machine-log.log).
They remain active; final hashes/results follow terminal completion. The parent
log/status is runtime.log/runtime.status in this attempt. No complete-matrix,
overallCI-green, integration/deployment/publication or lifecycle claim yet.

Second row direct-filesystem-bind26.05 PASS15:08:42+0200,408.8sexample/410.19s
script. Actual old baseline, earlier-sorting account, source-only candidate
switch/repeat/restart retain all identities/maps/data/metadata/mount assertions
without exact systemd state/log entries. Standard26.05 adoption is now active.

Third row standard26.05 adoption PASS15:16:05+0200,441.84sexample/443.4sscript.
Every old->new/repeat/restart, IDs/maps/data/owner/machine-id/metadata/mount
assertion passes at final source. Normal exact-source fresh initialization is
now active. Threeof12complete, no runtime failure or source change.

Fourth row exact fresh26.05 PASS15:22:25+0200,378.54sexample/379.84sscript.
Real first allocation uses the empty correct source with explicit root0755,
then account challenge/repeat/restart preserves all assertions. Sole/var old-to-new
adoption now active, with no exact state/log declarations. Fourof12complete.

Fifth row sole/var26.05 adoption PASS15:29:35+0200,428.49sexample/429.68sscript.
No exact state/log mount exists; the actual ancestor identity/count/options and
child map backing/IDs/data survive source-only switches/restart. Sole/var/lib
adoption is now active. Fiveof12complete, no runtime failure.

Sixth row sole/var/lib26.05 adoption PASS15:36:28+0200,412.21sexample/413.4sscript.
Both ancestor adoption rows, direct-filesystem adoption and fresh-ancestor now
pass at final source, without exact systemd state/log declarations. Fullmatrix
sixof12complete; dependent/usr layout is now active. No source changes/failures.

Seventh row dependent/usr26.05 PASS15:43:52+0200,442.02sexample/443.41sscript.
The selected state bind and later/usr consumer retain upstream global ordering;
all preservation/restart and final/usr identity/count assertions pass. Declared
backing adoption now active. Sevenof12complete, no runtime failure.

Declared-backing example FAILED15:46:11+0200 after138.24s, before candidate
adoption. New explicit payload-directory assertion expected997:997:750 but
actual0:0:755. Initial old boot/readiness succeeded; no source/service/data fix
was attempted. Original numbered failure/setup excerpts retained in
../persistence-declared-payload-diagnosis/. Architect0 owns read-only cause and
bounded correction design; source stays frozen while unaffected variants run.
Unstable adoption is now active. SevenPASS/oneFAIL; whole acceptance is open.

Unstable adoption PASS15:54:53+0200,512.99sexample/514.3sscript. EightPASS,
one declared fixture failure. Root-backed/failure/historical rows remain.
Architect source diagnosis and accepted correction: ../persistence-declared-payload-diagnosis/decision.md. No source edits while this immutable run remains active.

Root-backed adoption PASS16:02:06+0200,431.4sexample/432.86sscript.
NinePASS/one declared fixture failure; storage-failures is active, genuine25.11
remains. Observer effective_runtime_observer now owns bounded observation of
the existing operation without relaunch; parent43016 retains execution.

Expanded real storage-failure controls PASS16:22:05+0200,1197.46sexample/
1198.88sscript. This includes the new ancestor/nonbind/required-remount
executed-operation assertions and unchanged-state snapshots. TenPASS/one old
declared fixture failure; actual25.11 is the final running row. No code change.

Terminal status1,6931s wrapper/6813.26s runner. All11other rows PASS; only
declared-backing fails. Final25.11 example533.89s/script535.73s. Original
config/log hashes and lengths are retained in original-logs.sha256. Original
config is copied to original-config.json. Parent43016 terminal1 confirmed.
The old failed guest/disk is preserved; this run is not claimed wholly green.
The prepared test-only correction is now assigned for application.
