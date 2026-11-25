# Loader CSD / owned-vCPU evidence: final affected committed review

## Findings, ordered by severity

### LC1 — Blocking: noclobber prevents every real activation attempt from reaching insmod

**Commit:** 12df7c05ac72a48fac748b09f6f9c7660f3a1e0e.
**Source:** tests/suite/kernel/livepatch-6.12.95/qualification.rb:631-635, particularly the marker redirection at633.
**Coverage gap:** package-c-loader-controls.rb:26-29 and112-126.

qualification_loader_command enables `set -C` to protect the per-attempt PID file, then uses plain `>` to write that file into the existing trace_marker. Noclobber rejects replacement of an existing regular file. Because the generated command runs under `sh -ec`, the failed marker redirection terminates it **before exec insmod**. The intended candidate insertion and CSD diagnostic therefore cannot run.

This is not an unproved guest-format concern. In the pinned Linux source a2384967b90f24d2470c9eb15f0e66d938df7e08:
- kernel/trace/trace.c:9709 creates trace_marker for the instance.
- fs/tracefs/inode.c:657-659 supplies S_IFREG and requires a regular file.
- The new qualification_loader_clock(begin) at qualification.rb:622 writes that same existing marker before the attempts.

The positive actual-command host control does not represent this condition: it mkdirs the trace directory but leaves trace_marker absent. Its first marker redirection creates an ordinary fixture file, so the reported positive passes. The following duplicate-attempt negative then finds the earlier PID file; it does not test a distinct second attempt against an existing marker.

**Smallest correction:** keep exclusive/noclobber protection for each loader-attempt-N file, but explicitly override noclobber for the trace_marker write, e.g. `>|`, or use a supported append write. Do not disable PID-file protection or change activation semantics.

**Focused validation needed:** start with a preexisting regular marker fixture; prove attempt1 reaches the exec replacement with matching actual PID/locale/module, a distinct attempt2 also reaches exec while preserving attempt1's file, and duplicate attempt1 still refuses to overwrite its evidence or execute insertion. Fold the caused correction into the new loader-evidence owner.

I did not execute a reproduction or tests; this finding follows directly from committed shell semantics and the pinned tracefs file creation. It was reported promptly to lead in preliminary message254604fe37ee4a17a649e5fe4af7cdca; the precise final source anchor is631-635.

**Disposition: do not publish/start the next diagnostic execution on this head. Fix LC1 and reconcile focused checks first.** No additional Important or Advisory findings.

## Reviewed scope and risk

Complete range: **2951a632c4254a44747a8da326e3dde897eaa0e2..12df7c05ac72a48fac748b09f6f9c7660f3a1e0e**.
New substantive range: **b361b8c600bc1d50c237a68ca5413d38be9a0e99..12df7c05ac72a48fac748b09f6f9c7660f3a1e0e**.
All four lanes: general, architecture/repetition, scope/proportionality, risk/compatibility.
Overall **HIGH**: privileged guest tracing, owned-host proc identity/privacy, process lifetime/cancellation and CI execution.

I inspected all four changed files and necessary Linux/QEMU, OSVM, test metadata, workflow/state/artifact and qualification consumers. I reused scheduler-lifetime-review.md and the earlier source/reconciliation chain for the unchanged implementation; this is not a repeat of the original feature audit.

## Scope, architecture and current consumers

The actual delta is **four files,+645/-2**: guest loader evidence, one210-line host sampler, its CI owner wrapper and the narrow QEMU naming option. These form one diagnostic purpose: removing a side of the handoff would lose actual attempt/target history, aligned owned-host facts or reliable thread identity.

The recorded loader fault justifies the finite guest/owned-host capture. No kernel correction, new probe/resolver, runner API, privileges/SSH fallback, altered workload/deadline/health policy or generic framework is introduced. I found no speculative subsystem needing expansion.

Actual consumers are this qualification example/after-hook, the existing lifecycle job and its state directory, the normal machine metadata/OSVM argument forwarding and existing artifact handlers. No public or cross-project API changes. Near-owner comments explain identity, time/coverage and causal limits; temporary incident/execution history remains in session records. A permanent product manual is not needed for this diagnostic-only code.

LC1 is a correctness defect inside this accepted boundary, not a reason to replace the design with another framework.

## Guest capture, timing, ownership and causal limits

Subject to LC1, the source-level design preserves the intended contract:

- Preparation is before stress/population and requires v5/frozen notes, owned-host readiness and actual guest/APIC mapping. It creates one absent private nop/OFF instance, checks actual tracepoint fields/filter readbacks, and enables the three existing CSD plus two existing IPI events before load. It adds no kernel probe.
- CSD filters select do_flush_tlb_all/do_kernel_range_flush; IPI filters select generic_smp_call_function_single_interrupt using the existing unique native symbol lookup. I directly read the pinned include/trace/events/csd.h and ipi.h field/print declarations and compared them with the finite decoder.
- Recording is activation-only, global guest trace clock, all128 CPUs,64KiB per CPU and no overwrite. Original workload, hotplug/health baseline and shared1800-second attempt budget remain. Diagnostic setup/finish has additional bounded overhead; it is not proof that the entire outer helper returns within1800 seconds.
- The intended attempt file and marker identify the same shell PID that execs insmod, preserving locale/module and avoiding buffered stdout as the only PID evidence. LC1 currently prevents the final exec, so this must not be described as working guest evidence.
- Clock commands retain host wall/monotonic send/reply brackets plus guest uptime/trace markers. Host sample wall/uptime bounds remain separate. The code does not directly subtract guest trace time from host time or derive starvation from a later load/memory snapshot.
- A single example-owned observer reads public machine.console_output from the activation cursor, detects the first new softlockup text, and makes one bounded diagnostics-channel OFF attempt. Finish stops/joins it before end/freeze/read; failed freeze is not retried as a known clean operation. Original errors/cancellation prevail over subsequent StandardError diagnostics.
- Raw trace, actual attempt files and every CPU's buffer statistics are retained before existing failed-transition reporting. Missing clocks/markers, unsupported fields/header, PID disagreement, unacknowledged freeze, loss/saturation or incomplete host status prevent complete diagnostic acceptance.
- The decoder keeps the raw origin/target/PID/time/function/callsite/token evidence and distinguishes ordered token reuse, local NULL, unknown prior history and outstanding work. It rejects overlapping ambiguous reuse. Its summaries do not assert queue==dispatch, dispatch==hardware delivery, target PID==issuing insmod, or outstanding-at-freeze==permanent deadlock.
- Guest release remains owned and post-drain. Possible creation/enable/recording effects or failed drain prohibit destructive cleanup; one failed release is not blindly repeated. Earlier dying-observer behavior and its source prefix are unchanged.

The finite controls exercise these paths with synthetic guest I/O. Real trace formats, first-fault detection/freeze latency, loss-free capture and normal late cleanup are still runtime gates.

## Owned-host sampler and workflow lifetime

I inspected loader_host_sched.sh in full:

- It starts from the exact case qemu-launch record, not a process-name scan; checks declared topology/memory/direct boot/QEMU path; binds PID/start ticks/executable and ancestry to the wrapper's test-runner child.
- The job child is published before exec in the existing pipeline. The test-state slug function produces the exact case directory glob used by the helper. OSVM launch logging supplies the fields consumed; no private runner field/API is accessed.
- QEMU/child/TID proc directories are pinned and identities revalidated. PID/TID reuse, ancestry loss, thread-count changes, duplicate/missing CPU labels or changed TID/start mapping terminate evidence collection rather than reattach elsewhere.
- Reads are bounded owned stat/schedstat/exe plus necessary host uptime/schedstats capability. Output contains fixed numeric scheduling facts and finite labels; it does not emit raw comm, argv, environment, credentials or unrelated process data. No scheduler setting or privileges are changed.
- All128 named vCPUs must be identified with usable enabled stats before ready is published. The guest validates its observed logical/APIC/package/core facts and joins APIC slots to those TIDs, permitting logical CPU permutation.
- The sampler targets2-second intervals with actual start/end/gap anchors, caps256 threads/3600 seconds from QEMU launch/64MiB output, and explicitly marks lost ownership, capabilities, mapping or caps incomplete. It does not promise hard real-time sampling.
- Completion requires a final sample after the guest window marker. The wrapper's EXIT/cancel path requests stop and waits for its sampler. Existing nonzero/cancel status is preserved, including stop-marker write failure; nominal success becomes failure unless final status is complete. No independent daemon or delayed cleanup is introduced.

Existing build/captured identities, selector, resource admission, artifact/result and VM cleanup stay unchanged outside the wrapper. Host files enter the existing log/text artifacts; upload success is not qualification.

Actual runner interpreter/permissions/schedstats, task labels, timing gaps and final coverage have not been observed. These source-level ownership controls do not establish those runtime properties.

## QEMU naming and mapping contract

The new common.nix guard is null-safe and requires exact id amd-scale-aged-v5, amd/v5,128CPU/16384MiB/100000tasks/300s. Other profiles, including14400, exclude it. It composes only the literal -name/debug-threads=on pair with mkAfter.

I traced boot.qemu.extraQemuOptions (existing list option) through the machine with-empty configuration, tests/make-test.nix, MachineConfig and OSVM. This machine has no overriding extra-option list. OSVM's original guest name precedes the appended pair, which is forwarded unchanged.

I inspected the retained exact-source QEMU name/topology/thread paths and the source/patch binding receipt:
- merge_lists/implied guest and per-key parsing retain the original guest name when the later option supplies only debug-threads.
- Fixed topology determines APIC slots; x86-common assigns cpu_index from the slot, and KVM constructs CPU N/KVM from that index.
- Pinned Linux proc.c exposes logical processor and APIC identity separately; the guest validation does not assume their numbers equal.
- Debug labels are explicitly not a stable API, so the exact source/runtime path and actual128-CPU map remain necessary gates.

The supplied QEMU10.2.4 source SRI sha256-ghtUW5LxZeV93cysUHfXbU1DaiJllbiBOtWTBrv9B0Y= and four-patch/postPatch receipt bind these paths. No QEMU restore/build/launch or Nix module evaluation was performed. Naming changes launch input; whole-guest equivalence with b361 is unproved.

## Verification assessment

The raw recorded batch is **116 finite controls**:44 retained,34 loader,20 host/proc and18 selector/wrapper. I read the actual helper/proc/wrapper controls and source-check results. Parse, declared nixfmt/RuboCop, rendered Bash, whitespace and normal mandatory hooks pass on the frozen files. Shellcheck is unavailable and was not installed; official unchanged-action metadata was checked by the owner, not re-fetched by this reviewer.

**The current checks are not adequate to release the next runtime unchanged because they miss LC1's real preexisting marker condition.** Their other passing results retain scope;116 does not imply a functioning first activation. Correct the focused fixture and command, run the affected ordinary checks and fold the fix before release. A direct narrow correction can be reconciled under mandatory-change-review step9; a new design/contract would require affected lanes again.

Beyond LC1, these bounded preparation checks are an appropriate stage before one runtime experiment. They are not new-head guest execution, module evaluation, actual runner proc proof, trace coverage or a kernel model. The broad osctld suite remains unavailable before examples as previously assessed; it is unaffected by this diagnostic addition.

I independently matched all four working files to committed blobs and frozen hashes:
- workflow: **ffce88c8ad7a5e5654ff967c98f5e8218cbfa546bead738102c08c5f9cdf2ed7**
- common: **8acb93d5d59568b65e35e0a7fb436ce1354da149a5b882b7e66f9e94518c0509**
- qualification: **a6813d0b7ae8ec5f9eb0ff37d0053f21cadc5e2149dfe30d106b31b45208cc12**
- helper: **6b85cedda7222e0b37019d7040767204b4a306a5b9eb9c006d32822b1db8045c**

All saved C per-file patch sections equal Git's sections exactly. Whole concatenations differ only in section order; the saved SHA548431fe08cca9ab9dd10003eee0afe5154ae011bda850454c5a9c294c28985e is not falsely called the sorted Git diff hash. The helper is mode100644 and deliberately invoked through Bash.

These are precommit checks bound by exact bytes, not postcommit reruns by A or this reviewer.

## Actual previous runtime and remaining causal gaps

The full b361 runtime audit proves healthy sampled CPU127 state then RED activation. CPU114/142433 belongs to first EBUSY; second147541 also rejected; third timed out/PIDunknown under the shared budget. Loader/TLB/SMP context precedes that load's init. Later patch completion restores neither deadline nor health.

Actual target/function/CSD and aligned host scheduling facts remain missing. Registers/later snapshots do not prove target starvation, delivery or cause. Complete RED capture is diagnostic progress; a clean run does not explain old faults.

## Complete history, consolidation and migrations

Independent local inventory confirms:
1. 8169b8189c29f471b2ecf27a33b6f71dbde5e70e — normal module witnesses.
2. e1751c917f216897292ab0b893727a6e5553a540 — OSVM boot evidence.
3. 645927e22809a29c67ffd59c072e553e05e2a72b — production shutdown correction.
4. bda1f5d0d5dc302ff9b3002b9e9b20ee801553cf — temporary300s age.
5. 538706790c459bfefae4593bf963fa0d37961870 — dying-runqueue/lifetime observation.
6. b361b8c600bc1d50c237a68ca5413d38be9a0e99 — one-case diagnostic execution.
7. 12df7c05ac72a48fac748b09f6f9c7660f3a1e0e — loader CSD/owned-vCPU evidence.

Parent is exactb361; merge base is2951. Complete range is **27 paths,+4548/-274**. The prior six objects remain exact ancestors with unchanged messages/patches. The new independent purpose has four coupled files,+645/-2 and stable patch ID **e4da6ba2564aad7656b806004d383c44e07f8c6a**. All23 unaffected existing feature modes/blobs and the complete prior dying-observer prefix remain exact.

**No obsolete implementation, fixup/WIP, duplicate repair or transitional compatibility path remains in the current seven-purpose evidence series.** The new loader purpose is independently meaningful and correctly separate from dying-rq owner538706. LC1 is a present content defect to fold into its owner, not justification for a future final fixup commit.

**No repeated dependency/channel/input/pin/generated-update streams exist.** Canonical rake-compiler baseline2951 is not a feature update stream. Earlier diagnostic variants remain provenance refs outside the delivery series.

**No migrations.** No new schema/database/on-disk/protocol transition or migration merge/release/deployment/external-use provenance exists. Only ephemeral diagnostic state/launch behavior changes; no coordinated fleet update or production deployment is required.

Primary remains exact645927, clean, original14400/full workflow/skip-message state. All four diagnostic purposes remain outside primary ancestry and must remain outside final shipping ancestry; do not merge/cherry-pick them and add reverts. Nine local provenance refs were enumerated intact; prior detached/source-root retention is recorded in A/C receipts. No cleanup/deletion was performed. Current source/index/nonignored-untracked state is clean.

## Required disposition and completion

**LC1 blocks further diagnostic publication/runtime at12df.** Implementers own its narrow fix and representative controls; root owns reconciliation, folded final head and subsequent exact-head release. No review rerun solely to rubber-stamp that narrow correction is required by the skill.

After correction, the next separately released one-case runtime still must prove actual naming/APIC-to-owned-TID readiness, trace formats/filter acceptance, first-fault freeze/clock bounds, loss-free CSD/IPI history and full owned-host coverage alongside original deadline/health/drain/recovery/teardown. Missing or uncertain facts stay incomplete; no blind retry, timeout increase, warning waiver or14400 escalation.

Final shipping returns to primary lineage, excludes all temporary purposes, removes only the isolated skip directive through the authorized normal-hooked path and gets final history/equivalence/review plus **full exact-final-head native+all nine at14400**, semantic/identity/health/recovery proof and ordinary conditional integration checks. This review grants no merge, deployment, service or lifecycle action.

Session/current/env and live saved reviewer identity were freshly verified: both env markers absent, exact trusted developer binding, reviewer0/thread01a1a24e-920c-7b82-9fff-7754d1f947ab, ready/review-purpose **gpt-6.1-sol/xhigh/read_only**, no override/fallback/nested agent. Mandatory skill/all four lane references and applicable unchanged current workspace Git/verification/commits/docs/package workflow/repository/patch guidance were read or reused as allowed; latest relevant guidance2b5944e8 is unchanged.

Read-only source/history/receipt/pinned-source inspection only: no source/session writes, tests/eval/build/VM/network/API/CI operation, Git mutation, service or lifecycle action.

**Review package complete; disposition BLOCKED by LC1.** Root saves this complete report as loader-csd-review.md. Session remains open.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-03-livepatch-fixture-failures/
