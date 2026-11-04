---
lifecycle: active
---

# Current state

Phase: final discovery/configuration preflight before independent final review.
All intended application changes are committed and published at
742eb30cb1a8b6766c85e915d26b0400e38244b1, tree
19f423e70ff439867d4bb27e8ed07b9c95fdb703. Three logical commits, seven files
(+27/-14), clean worktree and exact remote head verified. Source syntax, format,
whitespace, full Overcommit and active hooks pass. Fresh-image checks remain.

Final discovery failed before any VM because the test-only global mkForce8192
conflicted with an unrelated fixture mkForce4096. Implementer1 is correcting
only the override priority in a new versioned module; source742 is unchanged.
See final-discovery-result.md. Final review waits for corrected discovery. No merge, production image
publication, deployment or session lifecycle action is authorized. Integration
approval was subsequently granted below; it remains conditional on completion.

## User scope and phases

Milestone1: add Leap16.1 image scripts and repository registration, and replace
the existing opensuse-leap builder's Leap15.5 base with16.0. User clarified that
a separate versioned builder was not intended; the added separate builder has
been removed from final history.

Milestone2: user explicitly requested the root cause and a real resolution of
openSUSE's expected-failure device-unit test. Do not extend the expected-failure
exception to16.1. Missing udev is now runtime-proven: package-only dependency
installation plus clean restart activated eth0 and dummy0 with original network
state restored. Preserve isolation and fix the supported behavior.

- [x] Exact session/environment identity and retained team/access verified.
- [x] Milestone1 corrected source committed/published; quick checks/hooks pass.
- [ ] Milestone2 causal evidence, implementation and meaningful regression.
- [x] All intended application changes committed; source quick checks/hooks passed.
- [ ] Corrected final selector-discovery preflight.
- [ ] Final independent review of the complete final series.
- [ ] Fresh shared-builder image tests for supported Leap15.6/16.0/16.1.
- [ ] Candidate-backed focused runtime/cgroup/network/device checks.
- [ ] GitHub feedback reconciled; public-image prerequisite remains.
- [x] Explicit conditional vpsadminos/staging integration approval.
- [ ] Approved integration after final review/verification.
- [ ] Separately authorized production publication/deployment/usability.

## Current repository and owners

Repository: vpsadminos, default target origin/staging.
Branch: 2026-11-03-opensuse-leap-image-build.
Worktree: worktrees/2026-11-03-opensuse-leap-image-build/vpsadminos.
Base: dd188397abe37d0bc33f4c5dfb3605206ce5e326.
Milestone1 series:
1. 4c2a38bc02d1d10c208d478c01ec90057995825e: shared Leap builder upgrade.
2. 57871a8e3f8f429e86e3ad6abf16de99a44e9416: new Leap16.1 support/matrix.
Milestone1 tree: 7e88b628393dfd7771800d23a7bc423ef23b109e.
Final third commit742eb30cb adds explicitudev and removes the obsolete
expectedfailure path; finaltree/head are recorded at the top. Its message-only
predecessor c856 is retained, identical source tree; earlier AA is not equivalent.
Five paths,+23/-2; clean checkout and exact SSH remote head verified.
No dedicated builder, helper change or expectedFailure change in this package.

Implementer0 completed Milestone1 and relinquished application/Git ownership.
Implementer1 owns device diagnosis and eventual source/tests/docs/commits, after
causal confirmation and accepted design. Architect0 owns the shared-builder
[design](design.md) and separate [device-unit brief](device-unit-design.md).
Reviewer0 remains independent, retained gpt-6.1-sol/xhigh. Lead owns tracking,
acceptance inspection and approval-bound coordination. No physical machine claims.

Main package shell/Nix/native config parser/whitespace checks and active hooks
passed. Consumer search finds exactly shared-builder targets15.6/16.0/16.1.
Builder ID is name-derived and UseOrCreate does not validate cached release;
final regression must use fresh owned state to avoid cached15.5 reuse.
See [current implementation result](implementation-result.md). Prior complete AA
result is [preserved separately](implementation-result-aa963dce4.md).

Existing separate final-head metadata and8GiB verification modules bind57871a8e3;
AA modules/inputs remain unchanged for diagnosis. After any actual device fix,
new exact-head metadata must be created for the final tests. Planned native
three-image batch is in the current implementation result; no run yet.

## Device-unit evidence and active diagnostic operation

Original AA case repeatedly showed eth0.device loaded but inactive(dead), exit3.
The final poll exhausted its budget; dummy0 was never reached. This matches the
existing latest-tag exception but is now an actual fix request, not a reason to
extend it. [Diagnosis](device-unit-diagnosis.md) preserves raw lines and hashes.

AA image archive SHA256
254523b59106db1d27bcf98e43e942c8ea1d7f0c15238542ca17e21612017214
contains99-systemd.rules and our trigger drop-in, but no udevadm/udevd binaries
or main service/socket/trigger units. Shared opensuse.sh uses --no-recommends
and has no explicit udev package. Factory packaging confirms a split udev
package, but target RPM/runtime and clean-boot causal proof remain required.

Immutable diagnosis inputs are documented in [device inputs](device-unit-immutable-inputs.md).
Old source6n06 had a .git pointer to the moving worktree despite matching tracked
bytes; it was rejected before launch. Clean AA source f8b7db... matches all2373
tracked files/symlinks/modes with no extras. The native prepared-config debug API
uses the exact original drk2q5...JSON (SHA256
5e2de9fef94e2b08c0d65d0a06f590a43265a3a35a7dde4018875d859705a5eb),
retained8GiB device VM and container testct-553b, avoiding Nix/live-Git evaluation.

First launcher attempt failed LoadError from a transcribed RUBYLIB path before
any VM action. It was corrected once into a fixed wrapper-derived launch input;
exact-environment require preflight passed. Current fresh Luna/low utility
**device_unit_runtime_fixed** owns the continuous native diagnostic PTY, starting
with fixed launcher SHA256
b8e08ab5fd5e8402a2a3e09a017fe43baf2b8630a11a6ae1e265306f101dcc9d
and read-only observation input SHA256
cbbd2c22114446dd93eedf01b6ad95269ca809aac23faa39191999c7e1effa6f.
It will report raw results at Pry and retain ownership for lead-relayed exact
technical follow-up. Implementer1 diagnoses; utility does not make fixes or
acceptance decisions. No package installation/event trigger is authorized yet.
First watchdog/panic triggers native interruption/exit and preserved disks.
Baseline observation now complete in native log: udev absent, all four udev
units LoadState=not-found, no daemon/journal or data/tags, only the pre-PID1
control stub. Eth0 exists/up with the expected sysfs path; both device units
are loaded/inactive with empty SysFSPath. Final rules command completed
END21:00:28/STATUS0. Missing userspace event processing is established; the
package-only clean-restart experiment is being prepared to prove the fix.
PTY completion visibility is being reconciled with a host-only prompt probe;
the guest RPC itself is complete, no VM restart or guest mutation performed.
Host-only prompt probe established live Pry50302. The same owned operation is
now authorized to evaluate fixed package-only clean-restart input SHA256
8d6ea5d3613a32c948e2a2bc90811f7294d8888b00ff54df3a883c14fb6b528c.
It transfers exact signed official udev257.13 RPM SHA256
8bf941306f3878331df5c3f6853b3f720114fe5197bbe0082135e934734b7abf,
requires dependency/signature checks and sole package delta, then normal CT
stop/start, changed init PID, active eth0 and absent->active dummy0. No network
change, manual daemon/reload/event trigger or extra package is authorized.
This is diagnosis on the AA container, not final-source verification.
First package experiment stopped at RPM dependency preflight, BEFORE install.
Required closure includes kmod/libkmod2, libcryptsetup12 and hardware groups.
No package/network/config change; samePTY50302 is atPry[4]. Baseline logs copied
under device-unit-baseline-aa963dce4-*.log. Implementer1 is preparing a bounded
signed udev+strict-dependency transaction; no force or dependency bypass.
Revised download experiment stopped before changes because native interface-add
requires stopped CT. DNS restored, pkg0 never created, no solver/install ran.
Lead simplified the fixture plan to temporary runtime IPv4/route on existing
eth0, explicit network-only negativecontrol, and full restoration before offline
install/cleanrestart. No persistent network change or new framework permitted.

## Superseded trial evidence (not final-source verification)

AA dedicated-builder head aa963dce42859ae4251cdfaded91920d67b3a46e is retained in
backup refs. It is substantively superseded, not equivalent to57871a8e3. It had
passed independent all-lane review and the full image test:15/15 guest checks,
no earlier Lua/scriptlet/libgio unpack errors. Actual builder was Leap16.0 with
RPM4.20.1; cached stream SHA256
d279c082fb997e17996af6fe00f8b54d23a847247c2498090a24b3f26538dbe2.
Earlier15.5 bootstrap failure and original f0/fe reviews/refs are preserved.
No migrations, repeated pin/input streams or production consumers of these
feature revisions; obsolete trial source is absent from the current series.

AA manual focused batch completed only start-stop (pass,248.382s) and device
units (failure,86.294s). Four cases were not started after user clarification.
Both VMs/runners and the local HTTP server were closed. [Partial result](candidate-matrix-result.md)
contains actual JSON/marker/raw evidence. Native case logs were copied outside
state before subsequent reuse.

The AA export's first24GiB VM had early-boot CPU soft lockups; it was stopped
normally with retained disk. One bounded8GiB helper recovery passed boot and
exported the candidate without watchdogs; no kernel/KVM fix or exact cause is
claimed. [Export receipt](candidate-extract-recovery-result.md) records full
builder/candidate/config/disk identities. Repository tar is169,820,160bytes,
SHA25636069c59b286fdeb81988e87482b519bb8fcea62a916e0a1d0eaac819e0c57d3.
It and the extracted loopback repo remain owned test data, not production.

Revision metadata workaround for immutable runner sources is documented in
[runtime diagnosis](runtime-revision-diagnosis.md) and the reusable workspace
note. Do not repeat the unsuitable --eval --strict derivation traversal probe.

## Runtime ownership, CI and next action

Device diagnostic operation closed normally with exit0; evaluator/QEMU/virtiofsd
and state lock released. [Causal result](device-unit-runtime-result.md) records
full package/network/restart/device evidence, warnings and limits. No owned
runtime operation remains active. Retained owned state:
/tmp/2026-11-03-opensuse-leap-image-build-device-units (closed, modified diagnostic CT),
...-start-stop (closed), ...-image (closed). Exported tar/extracted repo retained.
No loopback server or prior matrix/export runner remains active.

Superseded f0/fe/AA GitHub runs were cancelled and verified. Current57871a8e3
runs41705503484/41705503560 remain untouched; conclusions not yet known.
General CI's explicit16.1 cases need a public16.1 image. Changed-image workflow
builds/tests but never publishes, with no publication ordering dependency.
Existing public images remain unmodified and can still exhibit the old bug.

Controlled experiment passed:15new signed packages,0removed, network restored
before install, CTinitPID3134->6034; udevdrunning, triggerexited, eth0anddummy0
active/taggedsystemd. No manualreload/start/trigger. Rawproof and runtimeinstall
warnings are being accepted; clean rebuiltimages must have no oldscriptleterrors.
Implementer1 now owns minimal explicitudev package + obsoleteexpectedfailure
removal as a coherent thirdcommit afterthe sharedbuilder/newimage commits.

Next: implement the proven minimal fix, then commit all
final work, review the full cleaned series, run bounded fresh-image and relevant
focused checks. No new expectedFailure extension, blind retry or kernel scope.

Initial tracking commit0998bb834; session remains active/open. No project prose
was needed for the conventional release addition; any new durable device-unit
rationale belongs next to its owning implementation after facts are settled.

Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-03-opensuse-leap-image-build/

## Integration approval

User: "when done, you can merge it" (current conversation, after the shared-builder
clarification and requested real device-unit fix). Scope is the sole affected
repository vpsfreecz/vpsadminos, target staging. Complete final review/checks
first; no further merge confirmation required. It does not authorize production
image publication/deployment or session lifecycle actions. Selected-package
coordination guide and workspace coordination procedure read for preparation;
no repository claim acquired while review/tests remain.
