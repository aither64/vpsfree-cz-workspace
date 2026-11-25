# Scheduler capture: actual 13b runtime audit

Subsequent source-only work: the lead released the one-file early-prepare/
late-release remedy. Its [current preparation receipt](package-c-scheduler-hotplug-preparation.md#current-uncommitted-lifetimeorder-remedy)
records frozen uncommitted source and 44 host controls. No second runtime
attempt is implied; the failed 13b observations below remain unchanged.

**CI RED; diagnostic data INCOMPLETE.** Run `41938327930`, attempt 1, exact
`13b658f67c37418d6bbf91316ea7b3c6db99fe17`, completed failure at 00:42:41Z.
Build job `126952373971` passed; only target job `126962748765` ran its one
`kernel/livepatch-qualification@amd-scale-aged-v5/default` script. Native was
skipped. The example failed in 717.06s; test total was 807.59s. This audit uses
retained local evidence only: binding/env, retained Sol/xhigh workspace-write
roster and current verification guidance were reverified. No network, Git,
source edit, new ELF query, test, build, evaluation, VM or lifecycle action.

## Primary and phase

The primary is **new diagnostic event-enable timeout**, not the original
CPU127 cumulative kernel-health warning. Runner lines 5–9 retain the timeout
from `echo 1 > .../events/lp95_dying/scheduler_dying/enable`; line 4 reports
`scheduler diagnostic INCOMPLETE: setup did not complete`, plus secondary
disable/delete timeouts. The wrapper's original error message remains the
enable timeout despite those cleanup failures. The old health exception was
not reached and therefore cannot be described as retained or reproduced here.

| Event, all times UTC | Original shell evidence |
| --- | --- |
| Last aging health read, 00:40:56 | 9068–9078: only v5 transition/taint and nonmatching hrtimer notice |
| Frozen notes guard succeeds | 9081–9085 |
| Active predecessor `6.12.95.5` guard succeeds | 9090–9094 |
| Exact native symbol lookup succeeds, 00:40:57–41:05 | 9099–9105: U/u excluded, exact name, NF3, one `0xffffffffa1ced060` |
| Instance, buffer, clock and CPU mask setup succeeds | 9126–9179: 64 KiB, mono, overwrite off, CPU127 mask |
| Full finite probe definition accepted, 00:41:25–26 | 9180–9184: `p:lp95_dying/scheduler_dying 0xffffffffa1ced123 ...`, status 0 |
| `rq_cpu == 127` filter accepted; trace cleared | 9189–9202, status 0 |
| Event-enable command fails, 00:41:30–38 | 9207–9224: status -1, elapsed 7.78s; protocol-timeout, `replies_consumed`, reply prefix ends `:124` |
| Ensure turns tracing off successfully | 9227–9231, status 0 |
| Event disable / global definition deletion time out | 9236–9273: status -1, 8.0/7.8s, matching `:124` reply prefixes |
| Owned instance removal succeeds | 9276–9280, status 0 |
| Example failure / generic wrapper / final test summary | Runner 5 at 00:41:57, 12–13 at 00:42:11; raw target 269–272 at 00:42:31 |

The source uses a 10-second budget for these observation-control commands;
the guest-log elapsed values above are not a measured full kernel wait time.
Status 124 in the timeout reply buffer does not identify a kernel wait path
or a protocol defect. No original command guest PID is tied to a kernel
stack in the retained selected evidence. Later diagnostic stack lines
3223–3231 show one unassociated worker thread and one vanished PID, not the
event-enable caller. There is no later successful command-completion record
or event-state readback proving what the timed-out writes ultimately did.
In particular, the Ruby setup flag being false **does not prove the kernel
event remained disabled**.

Runner 24–27 reports 100000 tasks / 128 CPUs and age 102.704, 197.201,
292.385 and **389.800 seconds**: the declared 300s diagnostic age was reached.
No `tracing_on=1`, pre-transition hotplug-start marker, CPU127 offline/online
command, trace/stats/profile read, normal v7 insertion or callback/disable
phase appears in the phase index. The timeout occurs before the hotplug
body is invoked. The selected console has no scheduler/lockup warning;
that absence supplies no success for an unexecuted hotplug/health phase.

## Actual field acceptance

Definition and filter writes demonstrate accepted **syntax/registration
preparation**. They do not demonstrate a completed arm operation or executed
fetches. The registered address is exact unique native base + `0xc3`; its
fetch declaration matches the retained frozen BTF/RDI/RBX fields.

| Required actual observation | Result |
| --- | --- |
| PRECALL event / exact function+offset / header CPU / monotonic event time | No record available |
| RDI server, RBX rq, entity->rq, embedded fair-server relation | Unavailable |
| Raw rb-parent/color and `on_dl_rq` membership | Unavailable; no membership decode possible |
| `nr_running`, `nr_pinned`, CFS/RT/DL counts | Unavailable, **not zero** |
| Raw flags; active/throttled/defer/armed/running | Unavailable |
| Displayed span presentation | No event display to evaluate; static/host formatter proof remains separate |
| Record count, profile hits/misses and ring-loss counters | Not collected; zero misses/losses cannot be claimed |

There is no new scheduler snapshot to explain, and no independent field decode
can be performed. The fair-server hypothesis remains unproven for this run
and for the old uncaptured warning. Earlier 20 host controls, metadata and
the lead-accepted no-finding combined 13b review retain their actual scope;
they are not guest capture proof.

## Artifact and input binding

Actual discovered ZIP:
`ci-scheduler-capture-41938327930/os-test-logs-41938327930-1-livepatch-amd-scale-aged-v5.zip`.
Independently verified **215626 bytes**, SHA256
`37754ee9260f48f701581ef7f6ff5e118c443c677afd58c9aa1f2514ff353388`;
raw target lines 323–326 agree for artifact `13376149496`. All 16 unique ZIP
members were independently checked as safe relative regular entries before
selected extraction into `package-c-scheduler-capture-runtime-evidence/`.
Only runner/result/test/identity/sites, small console/launch files and bounded
numbered shell/diagnostic excerpts were saved. No full shell, whole-case or
production-package artifact was extracted/read.

- Raw target 108–136 and 245–250 bind full source 13b above and lock SHA256
  `604e01bde4cf21e1532e9ed6e6cfb993da28439355ad7dceb5560447827c5baa`.
- Normal producer `/nix/store/qi47yi2g9kp89dv0h8jxwndm89vbq6az-livepatch_7-6.12.95`,
  `lib/modules/6.12.95/extra/livepatch_7.ko`, module SHA256
  `7c4da9d643d45ad9c07bde72b0180175519c5e7a15a6f2aec9e54831aee8455f`.
- Sites `/nix/store/aiqijlwh2w2wz79d6hvcqm1p9kzl4lv3-livepatch-candidate-sites`;
  extracted JSON hash independently
  `093cf255a38db5275b62370da8bac1297781e48e2ae3245c1c5b5e1ceeb23ed1`.
  Schema 1, matching module SHA, ELF64/EM_X86_64, build ID
  `fd8cbfe4c314ddac8f35d87bee4bb8b909e479d5`, ABI 0/56/96/1600.
- Shell 89–124 verifies guest module/sites and fixed v5
  `b31f64403d9d55f62e3d59e4bbefcbddcbda4fa66a2dc0689f9bb7cd7e927984`
  and v6 `960b13f1b461b95e29cccff58ddf0d3f3badf151046eb46eba36a9c8c7e5efe3`.
  V5 insertion and console transition complete; the active-release guard
  confirms `.95.5`, not candidate activation.
- Guest `/sys/kernel/notes` guard actually passes SHA256
  `1e4432629c0f1a1e9c6b175495217859279f98ded2beca091834ec059e42108a`.
  This is the retained frozen ELF notes binding, not a whole guest-image SHA.
- Launch: QEMU PID 1227368 / start ticks 147071173, QEMU store `kanckc6...10.2.4`;
  frozen boot `/nix/store/050sh2hfrnpc8j5abr2npp7bnlxvpb8a-linux-6.12.95-frozen-boot/bzImage`;
  initrd `/nix/store/h3v4nwmsn39wph7apj7q6bg8hn58rv3x-initrd/initrd`;
  system `/nix/store/zyp50w4psw3jig1m28yjlxcqjb1zr89f-vpsadminos-system-vpsadminos-26.05.git.13b658f`;
  squashfs `/nix/store/60phpcnj4dmpbzl126v5i3bm55wapy4p-squashfs.img`;
  direct boot, 16384 MiB, 128 CPUs/cores, one thread/core, one socket.

These are actual scoped inputs, not whole-input equality with bda1 or old
5235. The later snapshot has `.95.5`, load 140.62/125.59/71.17 and 9313 MiB
available; it does not establish why the command timed out.

## Cleanup, limit and smallest next owner

The original setup-timeout exception is preserved. Owned tracing-off and
instance removal succeed; **global event disable/deletion are unconfirmed**
after their timeouts. Native teardown then starts at 00:42:19; QEMU exits 0
at 00:42:31, records `kill SIGNAL: NONE` and destroy. Console records ordinary
stage-3/power-down. This is successful failed-case VM teardown, not proof of
in-guest observer cleanup or lifecycle qualification.

The next proposal is one C/architect **diagnostic activation/lifetime** package:
source-classify the timed-out enable/disable/delete path and its command/protocol
budget under the full population, then choose the smallest lifecycle correction
that can complete observation setup before the same locked CPU127 point.
Preparing/enabling with recording off before population growth is a candidate
ordering change to assess, not an established cause or released fix. Retain the
same capture window, inputs, workload, warning/health guard and original-error
contract. There is no basis here for a scheduler write, warning waiver,
resource/flakiness classification or another blind retry. The bda1 scheduler
warning and old 5235 loader/CSD fault remain distinct failed evidence.

This completes the read-only audit at the known boundary. No new check/run,
source/metadata mutation or cleanup action was performed. All audit clients
are terminal; C owns no background process. The run is completed with no
active watcher per the lead's retained final status. Root owns any next release.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-03-livepatch-fixture-failures/>
