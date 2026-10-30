# First-switch old-writer capture1

The pre-switch capture establishes the stale writer state in this declared
experiment: persisted run selection names the base dataset while the same run's
GC ownership and authenticated live root identify the temporary dataset. Target
activation returned0 and the pool reached active. The post-import recorder then
failed on an empty-file read, before the original equality assertion; this run
does not establish post-switch root/data/API state or a repair pass.

This is the [accepted newly packaged baseline](../identity-comparison.md), not
incident-exact target/image equivalence or generic-service causal exclusion.
All compact raw native evidence is retained here, bound by [receipt](receipt.json).
No disk image was copied. Native result unexpected_failure; script799.55s,
guardian830.624s, status1/reasonnull, no resource guard breach. Watcher shorthand
“timeout800” describes context/elapsed time, not an observed timeout exception.

## Before switch

- [Runtime YAML](first-switch-capture/before-switch/runtime_yaml.raw),256bytes,
  SHA256 `66e3e2dfdfb6d1cec3ad3fbf83b894618a416b1e446013545663d25978afe2c9`:
  run ID tank/niximpermanent/timestamp1792700667.9359279; dataset
  `tank/ct/niximpermanent`, destroy_dataset_on_stopfalse and null cpu_package.
- [GC YAML](first-switch-capture/before-switch/garbage_collector_yaml.raw),179bytes,
  SHA256 `3fe1e7ffe9769b50aff162a362f2f8f7cb12e8b45245b743b393a547a56b7bea`:
  identical run ID owns `tank/ct/niximpermanent.impermanence-4014fb`.
- [Full capture](first-switch-capture/before-switch/capture.json): held init6498,
  birth60064, stable rootdev99/inode2 and mount namespace4026532949. API reports
  running/init6498 and temporary boot_dataset.4CPUs/1socket, no assigned package.
- [Mountinfo](first-switch-capture/before-switch/init_mountinfo.raw) root739:
  `0:99 /private / rw,relatime,idmapped ... - zfs tank/ct/niximpermanent.impermanence-4014fb`.
  Temporary dataset GUID5076182134290402100, mountpoint99:34, private99:2 matches
  held live root. Base GUID7464274597901698647, private97:128 is distinct;
  `/persistent` mounts the base dataset's `/private`. Both origins are `-`.
- [Persistent marker](first-switch-capture/before-switch/persistent_marker.raw)
  is `inherited-persistent\n`; [temporary marker](first-switch-capture/before-switch/ephemeral_marker.raw)
  is `inherited-ephemeral\n`, read through held process root. After-start capture
  has the same stale YAML/GC and root identity; marker absence then is expected.

Raw stat before/after and full init/daemon stat, host mountinfo, managed sysctls,
boot/current identities and command results are in each phase's capture.json.
Predecessor has no generic sysctl service path; ENOENT is preserved explicitly.
This is not evidence of target-service application history after activation.

## First error and correction

[machine-shell.log](machine-shell.log:3580) records activation30.48s, STATUS0.
Pool state reaches active at3721–3730. The guest recorder then returns1 in0.59s,
and shell3852 delivers the Ruby NoMethodError trace. Its saved
[after-import capture.json](first-switch-capture/after-pool-import/capture.json)
is250bytes of traceback, **not valid JSON**; capture.stderr is empty because the
native shell combines output. No post-import raw phase fields were decoded.

Immutable helper captured_file line16 uses File#read(limit+1), which returnsnil
for a zero-length file; line18 calls bytesize and raises NoMethodError. Only
SystemCallError is rescued. The standalone exactRuby reproduction and actual
function regression reproduce this failure. The trace does not name which file
was empty. Empty sysctl sentinels are plausible candidates, not a captured fact.
Normalizing nil to an empty binary string fixes the helper in the owned working
tree; empty file hash/stat remain distinguishable from missing-file errors.
The immutable snapshot/JSON/raw capture stay unchanged. No equivalent baseline
rerun is required to unblock the reader and no retry is selected.

## Effects ended and retained data

[Independent final reconciliation](post-result-reconciliation.json), observed
20:31:36UTC: own canonical process references across all3declared attempts empty;
recorded native PID4118923/birth1200776138 no longer live; no managed disk,
filesystem socket, kernel UNIX socket or open FD to this exact attempt. The
remaining zero-byte .lock admits an exclusive nonblocking flock. These checks
supplement the watcher's final evidence and establish owned effects-ended;
guardian exit alone was insufficient. Lead was notified promptly for slot release.

Only exact empty stopped vm-scratch was removed via rmdir after reconciliation;
see [cleanup receipt](scratch-cleanup.txt). Native logs/capture remain. Frozen
source and roots stay for concrete helper/regression/reader validation needs;
shared runner root remains owner1/lead-owned. No global GC, foreign cleanup,
process signal, source-session mutation or lifecycle action occurred.
