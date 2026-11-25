# Diagnostic 300-second aged-v5 failure classification

Read-only evidence classification for run `41921632759`, attempt 1, job
`126907163490`, diagnostic source `bda1f5d0d5dc302ff9b3002b9e9b20ee801553cf`.
This is separate from the primary feature's restored 14400-second policy.
Binding/env, retained implementer3 Sol/xhigh workspace-write roster, current
verification guidance and repository AGENTS were reverified. No fetch, polling,
source/Git action, evaluation, build, check rerun, VM or lifecycle action.

## Primary failure

**Different initiating failure from the old 5235 loader stall:** the existing
cumulative kernel-health assertion rejects a scheduler CPU-offline warning
during **pre-transition** hotplug, while exact v5 is active. Current runner
lines 4–8 report the assertion at **22:41:07Z**. The first matching fault is
runner lines 18–25, independently in console lines 140–148:

```text
[690.400049] process 31532 (task-population) no longer affine to cpu127
[697.996197] Dying CPU not properly vacated!
[697.996324] WARNING: CPU: 127 PID: 789 at kernel/sched/core.c:8333 sched_cpu_dying.cold+0xe/0xda
[698.009073] ... Comm: migration/127 ... 6.12.95.5
```

The stack contains `cpuhp_invoke_callback`, `take_cpu_down`, `multi_cpu_stop`
and `cpu_stopper_thread` (console 161–179). It does not locate this warning
in `module_enable_text_rox` / `smp_call_function_many_cond`, the old initiating
stack. The preceding affinity message is context, not independently proven
to be the cause. The CPU127 enqueued-task dump says two total but prints only
the migration thread; it does not identify the remaining task or full state.

## Phase and timing

All wall times below are UTC, converted from explicit `+0100` case logs.

| Event | Evidence |
| --- | --- |
| v5 inserted successfully, 22:29:37–39 | Original shell 4764–4772; console patch completion at guest 54.569903 |
| Population/aging checks reach 390.501 seconds | Runner 76–79: 100000 tasks, 128 CPUs; prior age reports 104.217, 199.338, 296.400 |
| Last pre-hotplug health read, 22:40:23–24 | Shell 9169–9179 has only v5 transition messages and the nonmatching hrtimer notice |
| CPU127 offline, 22:40:25–35 | Shell 9592–9600: write returns 0 in 9.62s; offline-state assertion returns 0 |
| CPU127 online / 128 online verified, 22:40:35–40 | Shell 9610–9627: both return 0 |
| Workload progress wait completes, 22:41:03–05 | Shell 9691–9698: polling predicate finally returns 0 |
| Cumulative health read / assertion | Shell 9700–9704 at 22:41:05–06; runner assertion 22:41:07 |
| Generic example wrapper exception | Runner 64–65 at 22:41:16, secondary |
| Test summary | Raw job 265–273: 1 unexpected failure, 792.98s total, example 690.41s |
| Artifact upload / result evaluation | Raw 319–324 upload succeeds; 391–392 evaluation propagates the failed test |

The declared 300-second diagnostic age was surpassed; this is not a
four-hour result. Runner 80–81 explicitly labels **pre-transition** hotplug.
Source `livepatch-6.12.95/qualification.rb:231–246` performs offline/online,
then workload progress, then the unchanged cumulative health assertion.
The caller is line 499, before trace start and normal candidate activation
at 501–504. Successful progress followed by the health marker is also direct
execution evidence that the progress wait returned; it does not erase the
warning. Normal v7 activation, its callback counts, post-transition hotplug,
replacement recovery and disable are **not reached**. No current `corrected.ko`
insertion appears in the case's recorded command index.

The lead states no current cancellation was requested. The retained job/case
logs show an ordinary test assertion and successful artifact upload; no
cancel/timeout exception explains this failure. This is not the old
post-transition assertion after eventual activation.

## Exact evidence and identity scope

Supplied directory: `ci-diagnostic-300s-41921632759/`. Independently verified
artifact `13369593168`, **230306 bytes**, SHA256
`cae3cdd9852998df6963492ee7611378a805d1d33664de79745a6d4119f7f595`;
raw job 319–322 agrees. All 16 ZIP members were independently checked for
unique safe relative names and regular-file types before selected extraction.
Own selected evidence is `package-c-diagnostic-300s-aged-v5-evidence/`:
runner/result/test log, identity/sites/path files, 8.4 KiB console, launch log,
numbered first 160 diagnostic lines and bounded numbered shell excerpts.
No full shell log or full diagnostic dump was extracted.

- Checkout/captured source is full `bda1f5d0d5dc302ff9b3002b9e9b20ee801553cf`
  (raw 112–130, 240–245); lock SHA256
  `604e01bde4cf21e1532e9ed6e6cfb993da28439355ad7dceb5560447827c5baa`.
- Normal producer `/nix/store/qi47yi2g9kp89dv0h8jxwndm89vbq6az-livepatch_7-6.12.95`,
  module `lib/modules/6.12.95/extra/livepatch_7.ko`, SHA256
  `7c4da9d643d45ad9c07bde72b0180175519c5e7a15a6f2aec9e54831aee8455f`.
- Sites `/nix/store/aiqijlwh2w2wz79d6hvcqm1p9kzl4lv3-livepatch-candidate-sites`;
  extracted JSON independently hashes to
  `093cf255a38db5275b62370da8bac1297781e48e2ae3245c1c5b5e1ceeb23ed1`.
  It is schema 1, that module digest, ELF64/EM_X86_64, build ID
  `fd8cbfe4c314ddac8f35d87bee4bb8b909e479d5` and the existing ABI 0/56/96/1600.
- Original shell 107–142 records successful guest checks of corrected module,
  sites, released-v5 `b31f64403d9d55f62e3d59e4bbefcbddcbda4fa66a2dc0689f9bb7cd7e927984`
  and predecessor-v6 `960b13f1b461b95e29cccff58ddf0d3f3badf151046eb46eba36a9c8c7e5efe3`.
  Checked/copied current-module bytes are not evidence of candidate activation.
- Launch log 9–21: QEMU PID 1194186, start ticks 146347251;
  `/nix/store/kanckc6ljipqzjsrvj4aqaf87a4rhswr-qemu-host-cpu-only-for-vm-tests-10.2.4/bin/qemu-kvm`;
  frozen `/nix/store/050sh2hfrnpc8j5abr2npp7bnlxvpb8a-linux-6.12.95-frozen-boot/bzImage`;
  initrd `/nix/store/h3v4nwmsn39wph7apj7q6bg8hn58rv3x-initrd/initrd`;
  system `/nix/store/jhyppcijv9lh9hrlc42jhvc798ha0ip4-vpsadminos-system-vpsadminos-26.05.git.bda1f5d`;
  squashfs `/nix/store/3r0m8kvfxnm1cg6azg7nfdyr0z57zx4k-squashfs.img`;
  direct boot, 16384 MiB, 128 cores/CPUs, one thread/core, one socket.
- Failure snapshot is still `6.12.95.5` with load 141.22/124.43/69.19 and
  approximately 9034 MiB available. These later guest observations establish
  neither host scheduling causality nor memory/resource failure.

Guest/model identity is scoped to these recorded values; there is no claim of
whole-input equality with old 5235 or an independent guest boot-byte/notes
check. Runner teardown starts 22:41:23; QEMU exits **0** at 22:41:37, with
`kill SIGNAL: NONE` and native destroy recorded. Console 185–196 records stage
3/power-down. These are normal failed-case cleanup, not a passed lifecycle.

## Boundary and minimum next owner

This is a genuine predecessor-phase scheduler/hotplug health failure under
the diagnostic envelope. The guard behaves as intended. The evidence does
not establish a C runtime-consumer defect, a harness bug, a kernel root cause,
flakiness, host starvation, or a current v7 callback/loader failure.

The old loader-specific CSD diagnostic trigger in `design.md` / the old-aged-v5
implementation-plan section is **not met by this initiating trace**. Do not
automatically implement that loader collection for this different warning.
The minimum next owner is architect/kernel-qualification: classify the
CPU127 evacuation invariant and task-population/affinity interaction, then
bound any missing contemporaneous runqueue/task identity and hotplug-progress
evidence. Owned-QEMU PID/start identity is available; aligned host-vCPU
scheduling/runqueue-delay facts are not. Existing all-CPU watchdog backtrace
capture was enabled (shell 1005–1011) and must stay enabled. No additional
instrumentation, dump, run, weaker health guard, retry or waiver is released
by this receipt. Investigation stops at this settled classification boundary.

C owns no background process; the root's sole CI watcher remains untouched.
Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-03-livepatch-fixture-failures/>
