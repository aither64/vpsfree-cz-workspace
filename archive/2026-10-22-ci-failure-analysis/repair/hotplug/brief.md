# Hotplug recorder and repair execution brief

Current review remediation: **selected shutdown correction passes native syntax,
actual-helper compilation and all41 mocked protocol cases, exit0/2.287s**. See
[source fix and exact bounded command](review-shutdown-fix.md). Only recorder C
and its diagnostics documentation section differ from reviewed `9bea27c9`;
Git/head and frozen runtime inputs are unchanged. The q4 binary and existing
admission image contain the pre-fix recorder and remain held. No corrected-source
packaged C/BPF build, BPF admission or warning attribution is claimed. Corrected
metadata ran once and failed its JSON-v4 key assumption; the retained-only
checker passes native0/0.159s without Nix replay. Exact build/cache/CLI driver is
prepared. Lead selected the architect's coarse whole-daemon+client memory
tripwire; the frozen gated driver/guard package and inert checks are ready for
lead inspection in [the exact watcher brief](recorder-fixed-build-1-watcher-brief.md).
No guard run/realization is selected; protected effects and unknown cumulative
allocation remain qualified. Details are in the linked source/check packet.
The checkpoint and assembly readiness below describes the pre-review state.

Current readiness: **both source units on feature9bea27c9; stage2 completed once
and its Git window released. Native image assembly1 completed once, exit0/68s** under frozen driver
`88dd09d72982c9b8e453132e43d27a06ff83d72ab9ba02d6eefde74349c6468a`.
[Commit packet](commit-packet.md) records health81235fe7 and recorder/docs9bea27c9,
the exact six paths/checks/hashes and retained isolated source/effect proofs.
Normal pre-commit/commit-msg exit0 (advisory TextWidth warnings; all message lines
remain<=80). Feature FF4de50f to9bea27c9 preserved all six bytes/modes and7647peer
paths; index empty, final effects reconciled. Authoritative receipts are
`commit-stage2-result.json` and `commit-stage2-final-effects.json`; Git window
released through reportd905e800. Lead owns whole-branch final review. No push,
default merge, build, cleanup or runtime followed. Runtime admission remains unproven.
First-hotplug orchestration is unimplemented and held.
No VM, BPF attachment, hotplug, population or aging has run. The short probe-only
external guard/package is prepared and frozen below, awaiting lead inspection
and selection. It does not block the separate source commit packet.

Assembly receipts are retained as `probe-assembly-1-*`. JSON SHA256 is
`daafd11dde916f90772276902b2b1acd7a73e99451e109442a88d4bfb147256a`;
its native closure has626paths/2020835392 NAR bytes. The native precompression
upper was2639048650B/4GiB; final owned allocated upper563941376B. The watcher
omitted required continuous disk/RSS/daemon-builder sampling: peaks and aggregate
enforcement are **unproved**, despite native allocation gates and exit0.
Final exact scope/client/builder reconciliation and owned scratch cleanup are
recorded separately below. Preserve JSON/boot/recorder runtime roots.

Owner: implementer2. Authorized repair phase; lead owns operation scheduling,
fresh watchers and all Git windows. No merge/deploy/pin/lifecycle action is
selected. Verified session/environment/thread identity, owned writable worktree
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-22-ci-failure-analysis/vpsadminos`,
branch `2026-10-22-ci-failure-analysis`, clean initial HEAD/base
`846bb469505789ba0b2a405fa5905ba6d8253006`. Hook release arrived from lead and
architect; source preparation may proceed, staging/commits remain with windows.
Saved roster is implementer2 Sol/xhigh, workspace_write.

## First operation — archived binary inspection only

Do not substitute or restore a complete SDK. Expected frozen output paths are
not present locally. The owned worktree already contains the frozen compressed
NAR parts (295608320 physically allocated bytes, boot+dev families). Inspect
their exact bytes by streaming the dev NAR through a bounded parser and retaining
only `vmlinux` in a memory-backed file descriptor. Verify the complete dev NAR
SHA-256 `1b8ee65eed800b9ad10219936c50aa9b62fdae4f78ff9adcfaf2051eec40c229`
and vmlinux SHA-256
`6e63a63c8fd2fbaa92a51fd5bbcbd002909b33e0fa70ba77163075ab2014c5ab`
before emitting BTF/header/disassembly. No SDK files are restored to disk.

The selected first command, from workspace root, is:

```sh
/nix/store/kmzlca218j6j1ar292fxj7707qzypij8-systemd-260.5/bin/systemd-run \
  --user --scope --unit=ci-hotplug-probe-preflight-2 \
  -p MemoryMax=3G -p MemorySwapMax=0 \
  /nix/store/kpw5lyh32ysqswlxhdhh9hgfqdkcm7rh-coreutils-full-9.11/bin/timeout \
  --signal=TERM --kill-after=5s 300s \
  /nix/store/jy00n3jp5xj8s40n1fbldmkcr5n7avxc-python3-3.13.15/bin/python3.13 \
  /home/aither/workspace/ai/vpsfree.cz/work/2026-10-22-ci-failure-analysis/repair/hotplug/inspect-frozen.py \
  --worktree /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-22-ci-failure-analysis/vpsadminos \
  --output /tmp/ci-failure-analysis-2026-10-22/hotplug/probe-preflight-2
```

The output directory is reserved exclusively to this session/lane/attempt and
must not preexist. This Markdown is its ownership record, written before its
creation. The script, after lead acceptance, creates that exact ordinary path,
rejects path/symlink escapes, checks 40-GiB free floor, records start/end `df`
and physical/apparent `du`, and never removes data. Tool executables are existing
Nix store Python/Zstd, binutils2.46 and bpftools6.18.7; exact resolved paths,
versions and hashes enter the text output. No package mutation or substitution
is selected for this first operation. Source script SHA-256 must be recorded
by the watcher before launch, together with HEAD and tracked/untracked owned
source diffs/hashes. This is a dedicated binary-inspection helper, not a review
ledger or general execution harness.

Hard budget: 300s elapsed plus5s kill grace, 2-GiB maximum vmlinux memory-backed
file, 8-GiB maximum uncompressed NAR traversal, 64-MiB combined file output,
4-MiB stdout/stderr, conservatively 96MiB physical disk growth including logs.
Peak RAM forecast <=3GiB, enforced for the process tree by the foreground user
scope's3GiB memory and zero swap caps; no VM, sparse disk, Nix derivation, full kernel/SDK
copy or kernel build. Start available space was113906958336 bytes (~106.1GiB)
on the shared filesystem; this is an observation, not a reservation. Recheck
immediately before launch and reject if96MiB growth would cross40GiB. Stop owned
processes on deadline/floor/cap, retain incomplete output explicitly, and wait
for the inspector/decompressor to exit before any cleanup. Native cleanup is
normal script exit and child reaping; timeout owns the entire foreground
operation. Removal of the stopped owned attempt needs lead coordination and
retention of its compact text/hash evidence; no global GC or foreign cleanup.

Expected outputs: bounded `inspection.txt`, original `.BTF` bytes, generated
`vmlinux.h`, narrow symbol disassembly, start/end usage text. They establish
whether the exact ELF has BTF/DWARF, named probeable symbols and exact locations
for the locked rq predicate. BTF presence does not establish guest BPF verifier
or kprobe admission; those remain an explicit pre-aging gate.

## Recorder feasibility and exact next commands

Source configuration advertises BTF/BPF/KPROBES, and retained tests already use
tracefs probes. The successful inspection below establishes exact binary layout;
guest probe admission remains unmeasured. The recorder is one narrowly named
libbpf loader plus CO-RE BPF object, built from root-selected repository-locked
nixpkgs `da6dc0e7b26060f2f71ce3ef7088fb56ee44fa36` (`nixpkgs_2` in `flake.lock`).
New assigned files are
`tests/suite/kernel/livepatch-6.12.95/hotplug-recorder.{nix,c,bpf.c,h}`.
Keep exact boot/module checks; do not rebuild or replace the boot kernel.

After source preparation and metadata/cache acceptance, the exact derivation
selection is:

```sh
nix-instantiate tests/suite/kernel/livepatch-6.12.95/hotplug-recorder.nix \
  --argstr vmlinuxHeader /home/aither/workspace/ai/vpsfree.cz/work/2026-10-22-ci-failure-analysis/repair/hotplug/frozen/vmlinux.h
```

The fresh watcher records the resulting exact drv, then `nix-store --query
--outputs <recorded-drv>` and `nix-store --query --requisites <recorded-drv>`.
Use `nix-build --dry-run` for substitution/build selection **before** any
uncertain realization. Report cache sizes and missing outputs; no kernel drv
is allowed in the recorder's build graph. Conservative initial toolchain+
recorder growth ceiling is4GiB, to be replaced with the measured closure
forecast before the lead selects a build. Stop if required incremental outputs
exceed4GiB or the40-GiB floor; no unplanned SDK/kernel substitution.

Proposed build/syntax operation (not launched):

```sh
nix-build tests/suite/kernel/livepatch-6.12.95/hotplug-recorder.nix \
  --argstr vmlinuxHeader /home/aither/workspace/ai/vpsfree.cz/work/2026-10-22-ci-failure-analysis/repair/hotplug/frozen/vmlinux.h \
  --no-out-link
```

The Nix build runs Clang `-target bpf -D__TARGET_ARCH_x86 -O2 -g -Wall -Werror`
for the object and the package compiler with `-O2 -g -Wall -Wextra -Werror`
for the loader, linking libbpf/libelf/zlib. Native `--help` and strict rejection
of malformed/cap-exceeding arguments are quick loader checks. The frozen
header hash is a build input. Build deadline10min,4GiB physical growth ceiling,
64MiB build-log cap, no VM or kernel build; the watcher owns exact completion,
deadline/space cancellation and log/df/du evidence. These commands are proposed
until files exist and their exact source hashes have been sent to lead.

## Capture contract and acceptance before aging

Trace only first hotplug under v6. Use original128-vCPU/16-GiB/100000-task/four-
hour preparation,5h outer runtime,120s trace window,128MiB tracefs+64MiB BPF
buffers and256MiB combined output. No lower age/CPU/task substitute or retry.
Physical VM/Nix/share-backing forecast remains unmeasured and blocks VM launch.
Prepare pre-aging probe/attach/detach checks in the exact guest before creating
the population; they must not perform an unnoticed hotplug or enable tracing
during four-hour aging. Any rejection stops before expensive aging.

Use raw `sched_update_nr_running_tp` (not a fictitious tracefs event) to retain
CPU127 rq pointers, count deltas and stacks. Snapshot locked rq state at the
validated predicate site and/or `dump_rq_tasks` entry under the rq lock, including
`nr_running`, `nr_pinned`, CFS/DL/RT counts, `curr` TID/comm and fair-server
on-rq/active/throttled/defer/timer state. Match `dl_server_start/stop/timer`
entity identity and enter/leave pin depth, plus task affinity/on-rq/migration,
hotplug callback ordering/return and wake/enqueue/dequeue stacks. The exact
predicate site is established in the successful inspection below. Never
reuse an offset from another build or the post-WARN register dump. A later
source-only inference is not runtime proof.

Count-output, map-capacity, stack-capacity, ring reserve, kprobe missed-hit and
tracefs overrun/loss counters are required. Capture current values and actual
sysctl service/state history at phase boundaries without reapplying it. Preserve
cumulative dmesg. Add health checkpoint directly after first hotplug (before
v7) and after second, with explicit phases and original no-fault pattern.
Eventual acceptance still includes both hotplugs, all progress/transition bounds,
A/B migrations, disable/unload/stopped-task checks and full final health.

If the exact binary cannot safely expose required locked-rq/entity/pin state,
report a separately scoped diagnostic-kernel/ABI proposal with paths, proven
need and budget. No silent kernel rebuild or manual identity bypass. A proven
kernel repair needs its exact Linux owner/base/paths/provenance/version and
compatibility design before its own worktree/build is selected. Quarantine,
no-force recovery and ordinary exact-final-head review remain intact.

## Attempt 1 failure and narrow preparation correction

Lead's fresh watcher ran the original exact helper hash once in
`ci-hotplug-probe-preflight-1.scope`, invocation
`8358811cffed46409c2b677f256daac1`. It returned1 in2.4s at the memfd write,
`OSError: [Errno27] File too large`. The64-MiB `RLIMIT_FSIZE` unintentionally
also limited the memory-backed vmlinux; no BTF/header/probe result was produced.
Raw failure/status and watcher receipt are retained as `inspection-run.log`,
`inspection-run.exit`, `inspection-run-result.md` and
`inspection-watcher-result.md` beside this brief. This is a helper defect, not
kernel/probe evidence. No build, SDK restore or VM began.

Correction: `RLIMIT_FSIZE` now permits the2-GiB maximum memfd ELF; disk writes
remain independently limited before every write to a combined63MiB content
budget plus1MiB final usage/error allowance. The foreground process-tree scope
still enforces3GiB RAM/zero swap, with the original300s/96MiB physical limits.
The new attempt is `probe-preflight-2`, explicitly nonoverwriting. Attempt1
contained only `usage-start.txt`266bytes and `usage-end.txt`267bytes,12288
physical bytes including directory blocks. Its usage observations are retained
here: start available114595123200bytes, end114594926592bytes; physical du rose
8192→12288bytes, apparent200→467bytes at the recorded sampling points. Changes
in shared free space cannot all be attributed to this operation.

Cleanup after lead authorization: verified scope inactive/dead with no cgroup,
no matching inspector and no open descriptor into the exact nonsymlinked owned
attempt1 path; removed only its two ordinary usage files and then its empty
directory. Their blocks plus directory occupied12288bytes, now freed. No other
disposable or Nix data was touched.

## Source preparation checkpoint

Lead reports current shared feature HEAD `274e826d` after the independent writer
commit; that does not change the frozen kernel or this lane's initial source
boundary. No Git window has been selected for hotplug. The owned
`qualification.rb` edit labels pre/post-transition hotplugs and runs the existing
health helper after original CPU-state/progress checks with the unchanged
example-wide dmesg baseline. Exact prepared Ruby3.4.9 `-c`, direct declared-env
RuboCop and `git diff --check` pass. The existing obsolete RuboCop cop-name
warning is unrelated and unchanged. Recorder Nix syntax and Nixfmt pass;
Clang/loader build and all kernel attachment remain unexecuted.

The four narrow recorder files are drafts pending exact BTF field/symbol and
locked-instruction evidence. The draft has an original GNU-notes build-ID guard,
explicit required locked-symbol/offset, bounded raw count/wake/migration and
server/pin probes, per-CPU loss counters,4096-entry pin-origin map,32-frame
stacks with truncation reporting,64MiB ring and128MiB binary-output ceiling.
It distinguishes normal SIGUSR1 stop from SIGTERM/SIGINT abort, and refuses a
complete normal capture without count/wait/dying/locked events or when output
count/loss accounting disagrees. Its offline decoder prints at most4096 relevant
post-wait rows. None of these source features is runtime-admission evidence.

Architect accepted a narrow opt-in first-hotplug-only mode: validate actual
attachment before aging, arm only immediately before first hotplug, stop/drain
in ensure before cumulative health assessment, preserve an original hotplug/
WARN failure ahead of cleanup errors, and on a healthy first cycle emit a
clearly labelled diagnostic-stop failure before v7. This is not expected-failure
qualification or a pass. Later replacement, second hotplug, migrations,
disable/unload and final health are explicitly unexecuted in that mode.
Wiring waits for binary/probe/build feasibility and lead scheduling.

## Successful exact-binary inspection and next metadata operation

The corrected helper passed once in9s, exact exit0, scope
`ci-hotplug-probe-preflight-2`, invocation
`adc7f3ec20ae42fa94ea97f80c3056a3`; lead retains its raw log/exit/watcher result.
The complete307758104-byte dev NAR and213869480-byte vmlinux match their
expected original SHA-256 hashes. The GNU notes match build ID
`7801779436291880089e3407e50e5813f80d76f1`. `.BTF` is5219665bytes and
`.debug_info` is133928519bytes. No kernel/SDK restoration or build occurred.

Disassembly proves `sched_cpu_dying+0xa4` is the `cmpl $1,0x4(%rbx)` predicate
at0xffffffff810ed104, after `_raw_spin_lock` and `update_rq_clock`, with rq in
RBX and interrupts disabled. The subsequent pin read uses0xcf0; fair_server
starts at rq+0x968 and is stopped only after the predicate. The recorder now
accepts only this symbol/offset and reads rq directly from saved RBX there,
rather than relying on a previously cached pointer at the critical snapshot.
The original header confirms all required rq/task/CFS/DL/RT/entity/timer fields,
including16-bit task migration depth. This is binary-layout evidence, not yet
runtime probe admission or a demonstrated hotplug cause.

`dump_rq_tasks`, `dl_server_timer`, `inc_dl_tasks` and `dec_dl_tasks` have no
standalone symbols in this binary. Do not attach those names. Available
`dl_server_start/stop` calls prove the named `enqueue_dl_entity` and
`__dequeue_dl_entity` entry sites with entity in RDI. Use those entity probes
and positive-count stacks to distinguish timer/enqueue paths; retain timer
queued/expiry state at each snapshot. Missing optional inline sites do not
justify a kernel rebuild. Runtime attachment/CO-RE checks still gate aging.

All compact evidence was moved, without copying the SDK, into `frozen/` next
to this brief. Header SHA-256 is
`82ac9ea144b1f92f35b8cc2eb947ce672cfca6d06a60fe9e925a40ff30e51484`;
BTF SHA-256 is
`035c4fbe9bb2cab75c0f45366552729ca19e17df6a0c1814bc8747d1131de947`.
Original scratch allocation was8085504bytes. After scope inactive/dead/no
cgroup and no owner/open descriptor were verified, same-filesystem renames
retained the files and the empty scratch directory was removed (4096directory
bytes reclaimed; file data remains retained). Do not rerun attempt2.

The next requested operation is **metadata/dry-run only**, not realization.
Reserve `/tmp/ci-failure-analysis-2026-10-22/hotplug/recorder-metadata-1` to this
session/lane/attempt before creation. Run the exact `nix-instantiate` above from
the owned worktree; retain its drv string and query outputs/requisites with
`nix-store --query --outputs` / `--query --requisites` for that recorded drv.
Then run the exact `nix-build` above with **`--dry-run`**. No build/load/VM is
selected by this metadata request. Reject an unexpected frozen-kernel/SDK
derivation or component build from the recorder graph; Linux libc headers do
not constitute a kernel image build. Deadline300s/5s kill,1GiB physical growth
ceiling for Nix source snapshots/header/derivations,64MiB total logs,40GiB free
floor. Record start/end df and physical/apparent du for the new attempt plus
Nix copy/output sizes. If it fails or forecasts >4GiB incremental realization,
report before any build. A later accepted compile operation gets its own fresh
watcher and10min/4GiB bound; it may use only the checked drv/source/header.

Minimum runtime admission, after build/preparation acceptance, is the exact
recorder `--probe-only` on the original guest with the fixed locked site. It
loads/attaches every required probe, warms one short-lived CPU127 child before
enabling capture so raw count updates establish the real rq pointer, then
observes a second short child in a2s window and detaches. This performs no
hotplug and precedes population aging. A nonzero result or missing required
count data stops preparation. Actual capture is capped in BPF by monotonic
deadline as well as by the loader, and before count-two attribution must show
the required wait/dying/locked records plus complete loss accounting. No runtime
admission or four-hour operation has yet been selected or performed.

## Accepted metadata: bounded recorder build proposal

Batch2 recorder metadata and dry-run passed, exit0 in14s; the independent
original-fixture query failure in that batch does not change this result.
Authoritative receipts are `../support/preflight-batch2-recorder-{sources,
requisites,outputs}.txt`, `preflight-batch2-recorder-dryrun.log` and the matching
exit/elapsed files. All four source hashes and the frozen header hash were
rechecked unchanged after receipt. Selected derivation and sole output are:

```text
/nix/store/v9f0794pzylhgc7r9lj7afw37b6l8wgy-livepatch-first-hotplug-recorder-1.drv
/nix/store/q4isqny2rdrj41ivcj400sd3p4fpnjmi-livepatch-first-hotplug-recorder-1
```

The actual recorder package set follows the flake root's `nixpkgs` input to
`nixpkgs_2`, revision `da6dc0e7b26060f2f71ce3ef7088fb56ee44fa36`, NAR hash
`sha256-MlvRfa1O5Cqc2/a+gG+l9TSuowEoCKCmrJ1d9oAVm0I=`. The selected native
compiler is GCC15.3.0 (`dy6j7267wrgjlr2z748sbx83zj16vs3c-gcc-wrapper-15.3.0`);
BPF compiler is Clang21.1.8, with libbpf1.7.0, elfutils0.194 and zlib1.3.2.
This corrects the earlier unrelated `nixpkgs` lock-node citation, without changing
an input. Independently, producing OS `c065fa2f...:flake.lock` root selects
`nixpkgs_2` at `21a67dc470149f337cecafbe965d8d252a390518`; the findings citation
has been corrected. Original GCC15.2.0, binary hashes and frozen ABI assertions
are unchanged.

Direct derivation inputs are elfutils-dev, zlib-dev, pkg-config-wrapper, bash,
stdenv, Clang-dev and libbpf-out, plus the narrow recorder source and original
header. The1619-entry recursive derivation ancestry contains compiler bootstrap
recipes and Linux libc-header sources6.5.6/6.18.7. It contains no frozen6.12.95
kernel/SDK, ZFS-builtin or v6-module derivation. The actual dry-run selects only
the recorder for a local build and11 substitutions (Clang/LLVM, elfutils,
pkg-config, response-params, debug-info hook, zlib-dev):136.0MiB compressed,
1.4GiB unpacked. Header input is2769509bytes and C/header/Nix sources total
27479bytes. This is a userspace/BPF-object build; it does not build a boot kernel
or load/attach a probe.

Conservative **incremental physical allocation forecast**, not a measured peak:

| New allocation | Reserved ceiling |
| --- | ---: |
| Eleven unpacked cache outputs, block/metadata margin | 1.75GiB |
| Download/unpack staging including transient duplication | 0.50GiB |
| Compiler/build scratch and recorder output | 0.75GiB |
| Reinstantiation/source/header copies and metadata | 0.50GiB |
| Combined retained/watcher/daemon build logs | 0.0625GiB |
| Remaining contingency | 0.4375GiB |
| Total physical growth ceiling | 4GiB |

The1.4GiB NAR figure is logical unpacked content, not physical `du`. No full SDK,
VM disk or boot image belongs in this allocation. Last observed available space
was111263555584bytes; remeasure at launch. Require at least44GiB free before
starting, preserve40GiB floor, and cancel at observed4GiB growth or before the
floor would be crossed. Shared growth/free-space changes cannot all be attributed
to this operation; record both allocation and filesystem observations.

Reserve `/tmp/ci-failure-analysis-2026-10-22/hotplug/recorder-build-1/` exclusively
to this session/lane/attempt before creation, with native Nix build scratch in
its `build/` child and bounded operation logs in the attempt. Also reserve the
previously absent ordinary directory
`/tmp/ci-failure-analysis-2026-10-22/hotplug/gcroots/` and only its
`recorder.drv`/`recorder` links to this operation. Reject preexisting attempt,
links, symlinked parents or changed source hashes. No source edit or Git mutation
is included. The following is the exact native sequence for the lead's fresh
watcher, from the owned vpsadminos worktree, **not yet executed**:

```sh
/nix/store/kpw5lyh32ysqswlxhdhh9hgfqdkcm7rh-coreutils-full-9.11/bin/sha256sum \
  --check /home/aither/workspace/ai/vpsfree.cz/work/2026-10-22-ci-failure-analysis/repair/support/preflight-batch2-recorder-sources.txt
/nix/store/kpw5lyh32ysqswlxhdhh9hgfqdkcm7rh-coreutils-full-9.11/bin/mkdir \
  /tmp/ci-failure-analysis-2026-10-22/hotplug/recorder-build-1 \
  /tmp/ci-failure-analysis-2026-10-22/hotplug/gcroots
/nix/store/kpw5lyh32ysqswlxhdhh9hgfqdkcm7rh-coreutils-full-9.11/bin/mkdir \
  /tmp/ci-failure-analysis-2026-10-22/hotplug/recorder-build-1/build
/nix/store/z4wkkj3ncr69vgrb3020saqx1c8mfsjj-nix-2.34.9/bin/nix-instantiate \
  --add-root /tmp/ci-failure-analysis-2026-10-22/hotplug/gcroots/recorder.drv --indirect \
  tests/suite/kernel/livepatch-6.12.95/hotplug-recorder.nix \
  --argstr vmlinuxHeader /home/aither/workspace/ai/vpsfree.cz/work/2026-10-22-ci-failure-analysis/repair/hotplug/frozen/vmlinux.h
test "$(/nix/store/kpw5lyh32ysqswlxhdhh9hgfqdkcm7rh-coreutils-full-9.11/bin/readlink /tmp/ci-failure-analysis-2026-10-22/hotplug/gcroots/recorder.drv)" = \
  /nix/store/v9f0794pzylhgc7r9lj7afw37b6l8wgy-livepatch-first-hotplug-recorder-1.drv
/nix/store/z4wkkj3ncr69vgrb3020saqx1c8mfsjj-nix-2.34.9/bin/nix-build \
  /nix/store/v9f0794pzylhgc7r9lj7afw37b6l8wgy-livepatch-first-hotplug-recorder-1.drv \
  --dry-run --no-out-link --option fallback false
```

Stop unless the root resolves to the exact selected drv and the refreshed plan
has no additional local builds, kernel/SDK output or growth beyond the forecast.
Fewer substitutions after independent cache filling are acceptable. A changed
plan requiring more space or a missing dependency source build returns to lead;
do not continue on a failed registration/query. Root registration above performs
no realization; `nix-store -r` is not a registration command.

After that gate in the same bounded operation:

```sh
/nix/store/z4wkkj3ncr69vgrb3020saqx1c8mfsjj-nix-2.34.9/bin/nix-build \
  /nix/store/v9f0794pzylhgc7r9lj7afw37b6l8wgy-livepatch-first-hotplug-recorder-1.drv \
  --out-link /tmp/ci-failure-analysis-2026-10-22/hotplug/gcroots/recorder \
  --max-jobs 1 --cores 2 --option builders '' --option fallback false \
  --option keep-failed false --option max-build-log-size 16777216 \
  --option build-dir /tmp/ci-failure-analysis-2026-10-22/hotplug/recorder-build-1/build
```

Run the complete operation under the lead's bounded foreground runner with a
600s total deadline/5s kill grace, external logs capped at48MiB, and native Nix
build log capped at16MiB (64MiB combined). No retry or kernel build is admitted.
Capture start/end `df -B1` for `/nix/store` and the attempt, physical `du -s -B1`
and apparent `du -s -B1 --apparent-size` for attempt/new cache paths/output,
plus final exit/elapsed and output binary/object hashes. Sample the40GiB floor
and growth through the watcher, without launching a second observer. If native
Nix ignores the requested scratch path or any resource limit, stop and report
that gap; do not silently change the command. Daemon RAM is outside a client's
scope cap; no3GiB build-tree claim is made for this operation.

After success, only these native CLI checks are selected (each rejection must
return1, before boot-note checks or any BPF call):

```sh
/nix/store/q4isqny2rdrj41ivcj400sd3p4fpnjmi-livepatch-first-hotplug-recorder-1/bin/hotplug-recorder --help
/nix/store/q4isqny2rdrj41ivcj400sd3p4fpnjmi-livepatch-first-hotplug-recorder-1/bin/hotplug-recorder
/nix/store/q4isqny2rdrj41ivcj400sd3p4fpnjmi-livepatch-first-hotplug-recorder-1/bin/hotplug-recorder --locked-offset 0xa5
/nix/store/q4isqny2rdrj41ivcj400sd3p4fpnjmi-livepatch-first-hotplug-recorder-1/bin/hotplug-recorder --seconds 121
```

The watcher checks those expected nonzero statuses explicitly, rather than
treating them as operation failure or ignoring a different status. No
`--probe-only`, BPF load or attachment on this host. Preserve
the output link until those checks and evidence retention finish. On cancellation,
terminate only this Nix client through the foreground runner, wait for native
build cleanup, and reconcile any still-running daemon job; never kill the shared
daemon. Once effects have ended and root targets are checked, remove only the
drv metadata root with native `rm`. Retain the recorder output root for planned
admission, as refined by lead below; Nix manages indirect-root entries and store
reclamation. Remove only stopped owned disposable scratch after compact
logs/identities are retained. No global GC or direct store deletion. Compilation
and runtime admission remain unproved until the corresponding results arrive.

## Prepared build-1 script for fresh watcher

Lead provisionally accepted the4GiB/600s rooted userspace build and requested
the exact task-specific shell script, to be inspected/launched only after
support batch3 finishes. Prepared `run-recorder-build-1.sh` SHA-256:
`d45e9fe657b5184a9b565a5d8c895b6c3482eec79161951cd2d0a07f34cc5b97`
(supersedes896d366... only for the output-root retention correction).
It has **not been executed**. The exact launch from workspace root is:

```sh
DEV_SESSION_SLUG=2026-10-22-ci-failure-analysis \
DEV_SESSION_WORKSPACE=/home/aither/workspace/ai/vpsfree.cz \
  /nix/store/pwxj9ycwqd117yra6czifh3xfx5p88lh-bash-interactive-5.3p9/bin/bash \
  /home/aither/workspace/ai/vpsfree.cz/work/2026-10-22-ci-failure-analysis/repair/hotplug/run-recorder-build-1.sh
```

The script verifies `current`/environment/canonical writable worktree and refuses
preexisting attempt/root directories. It retains exact HEAD, checks the original
source-receipt hash and every source/header hash, registers only the checked drv,
and verifies its output. Its dry-run gate requires exactly the selected recorder
as the sole local build and permits only a subset of the11 approved substituted
store paths. A changed plan stops before realization. Build uses explicit
`--builders ''`, the owned build directory, one job/two cores, native540s build
timeout inside the whole600s deadline, and no fallback. There is no VM, admission
or tracing command. Native CLI checks require help exit0 and the three parser
rejections exit1.

The operation log is hard capped at32MiB and fresh dry-run log at8MiB through
inherited Bash file-size limits; native Nix build log is16MiB. Small status/usage
receipts fit the remaining8MiB of the64MiB combined budget. These limits apply
to this Nix client too; no large binary is extracted or copied by the client.
Native daemon build scratch uses the explicitly owned directory, not a client
RAM-cap claim. The script records start/end filesystem and physical/apparent
attempt/output/cache sizes, samples free space every second during the build,
and terminates its Nix client at the40GiB floor or a4GiB net free-space decline.
Shared GC can offset net filesystem decline; the immutable allowed cache plan
and retained per-output physical usage are additional allocation evidence,
not a filesystem quota or exclusive reservation.

On success it removes only the verified drv metadata link after CLI checks and
hash retention, keeping the output root for planned admission. On
failure/interruption it retains roots and compact receipts
for lead reconciliation, waits for its Nix client, and never kills the shared
daemon or deletes store paths. The outer foreground timeout supplies5s kill
grace; any daemon effects after interrupted client exit must be reconciled by
lead before releasing roots or deleting owned scratch. No automatic retry or
global cleanup is present.

Lead's prelaunch refinement retains this exact output root **pending admission**:
`/tmp/ci-failure-analysis-2026-10-22/hotplug/gcroots/recorder` pointing to
`/nix/store/q4isqny2rdrj41ivcj400sd3p4fpnjmi-livepatch-first-hotplug-recorder-1`.
It protects the recorder runtime closure from shared GC; the compiler/derivation
closure need not remain rooted. The later admission owner verifies the link and
binary/object hashes before use. Remove this owned output link, then its empty
`gcroots/` directory, only after the runtime data has been copied/used and all
owned effects have ended. This is bounded retention for the selected next step,
not an indefinite artifact hold or authorization to launch admission. This was
the prelaunch contract; the failed first execution is recorded below.

Preparation checks passed: absolute prepared Bash `-n`; embedded Python AST
parse; offline gate against the retained successful dry-run; rejection of an
in-memory extra frozen-kernel drv and unapproved SDK substitute. These checks
do not invoke Nix, the script worker, recorder, BPF or a VM. The watcher must
verify the final script hash before launch and report exact exit/elapsed and
`recorder-build-1/{operation.log,dry-run.log,exit,elapsed,df-end.txt,du-end.txt}`.

## Build-1 setup failure and corrected build-2 preparation

Lead's watcher ran the exact d45e9fe... script once: exit1 after27s. Source/header
checks, root identity and the sole-recorder/eleven-substitute dry-run gate passed.
All eleven cache outputs were fetched, then Nix rejected the selected build
directory: `Path "/tmp" is world-writable or a symlink. That's not allowed for
security.` Compilation never began and the output is absent. This is a build
setup failure, not kernel/BPF/compiler admission or product-cause evidence.
Do not chmod `/tmp` or disable Nix's check.

Before cleanup, the source-selected client/script/drv had no exact argv, cwd,
root or accessible fd match in `/proc`; the exact owned `build/` directory was
empty. Together with the native pre-builder error/exit, no owned builder or
client remained. Unrelated daemon work is untouched; inaccessible foreign fd
tables are not claimed inspected. Lead authorized retaining compact failed logs
and identities before removing only this stopped scratch and its checked
metadata root. Preserve all eight ordinary receipt files with
`recorder-build-1-` prefixes beside this brief, including full operation/cache-du
and dry-run logs; record their hashes. The existing watcher receipt remains.

Reserve new diagnostic state
`/tmp/ci-failure-analysis-2026-10-22/hotplug/recorder-build-2/`, the same two exact
`hotplug/gcroots/{recorder.drv,recorder}` links after reconciled build-1 root
removal, and **only native Nix build scratch** at
`/home/aither/workspace/ai/vpsfree.cz/work/2026-10-22-ci-failure-analysis/repair/hotplug/recorder-build-2-scratch/`.
This Markdown records ownership before creation. All workspace scratch ancestors
were canonical directories, owned by root or aither, mode0755 except aither's
home0711. The corrected script must recheck these properties, including no
world-write bit, then require the new scratch path absent. No component source,
header, derivation or output identity changes. Keep build-1 script immutable.
The new short task script is `run-recorder-build-2.sh`; no retry is selected by
preparing it.

Same bound:600s+5s grace,4GiB physical growth,64MiB combined logs,44GiB minimum
launch/40GiB floor, one job/two cores, no remote builder/fallback, kernel/SDK,
VM or attachment. Fresh dry-run still requires the same sole recorder drv and
permits a subset of the11 approved cache outputs, including zero fetched paths
when the already-fetched cache remains valid. Current additional compile and
scratch forecast is below1GiB if those outputs remain; retain the4GiB worst-case
ceiling to cover re-substitution after shared GC and the earlier metadata margin.
Record physical/apparent usage for both the `/tmp` attempt and workspace scratch.
Native Nix removes its build children on exit; after effects end, remove only
the empty owned scratch parent with `rmdir`, preserving logs and the output root
pending admission. Failed/nonempty scratch requires reconciliation, no recursive
blind removal. Lead will inspect/select a fresh watcher; no assumption of
sub-minute compilation is justified by this precompile failure.

Reconciliation/cleanup completed: all eight receipt files were copied byte-for-
byte and rehashed before deletion of the exact stopped attempt and old metadata
root/directory. No exact owned process references remained at deletion; build
scratch was empty. Removed53248physical bytes including directory/root-link
blocks, while preserving receipt content beside this brief. Full log
`recorder-build-1-operation.log` SHA-256
`2d05d01b178b50591ad01cb2ff62a4bacc07a100cda6b5b9f0df61d4d573c302`;
dry-run `recorder-build-1-dry-run.log` SHA-256
`932c962b5840241739d3ec769fd3ba8ec36125541b1cc39658452f69478ce873`.
The full log retains eleven cache outputs'1516564480physical bytes (~1.412GiB),
with corresponding apparent sizes. Shared free space fell112830988288→
110058381312bytes; that net change includes other activity and is not assigned
entirely to this operation. No Nix store path was deleted.

Corrected `run-recorder-build-2.sh` SHA-256:
`c8dc12b65584808daf2d9ca63a6548e596b38b16c026520d36252ad5944e0f86`.
Absolute launch, from workspace root, after lead inspection and fresh-watcher
selection:

```sh
DEV_SESSION_SLUG=2026-10-22-ci-failure-analysis \
DEV_SESSION_WORKSPACE=/home/aither/workspace/ai/vpsfree.cz \
  /nix/store/pwxj9ycwqd117yra6czifh3xfx5p88lh-bash-interactive-5.3p9/bin/bash \
  /home/aither/workspace/ai/vpsfree.cz/work/2026-10-22-ci-failure-analysis/repair/hotplug/run-recorder-build-2.sh
```

Only differences from the retained build-1 script are new attempt/script names,
secure workspace build scratch/ancestor ownership checks, its physical/apparent
usage and empty-parent cleanup. All component source/header checks, selected
v9f0794...drv/q4isqny2...output, dry-run gate, deadlines, limits and output-root
retention are unchanged. Prepared Bash `-n` and Python AST pass; offline parser
checks accept11 and0 approved substitutions, reject another local kernel build
and an unapproved SDK substitute. Source/header hashes were rechecked from the
owned worktree and remain identical. No corrected attempt, Nix realization,
compiler invocation, BPF load/attach or VM has been launched by this preparation.

## Build-2 passed; admission still pending

Lead's fresh watcher ran the exact c8dc12... script once: exit0 after12s,
HEAD274e826d. All sources/header matched; fresh plan built only the recorder,
with0additional substitutions. Compilation and native CLI checks passed. Nix's
generic fixup emitted `patchelf: wrong ELF type` for the relocatable BPF object;
the build succeeded, and independent `readelf` confirms `.BTF`/`.BTF.ext` remain.
This is preparation evidence only, not probe admission or a demonstrated cause.

Independent output hashes match the raw log:

```text
098fa4cacfee98cc6427b721c9a349da08833864ac42adfe663db0c44e8980a5 bin/hotplug-recorder
4aab6cc08451097034be7fae91857b6b324e8352701afe206d61c5b3b29cbb8b lib/hotplug-recorder.bpf.o
```

The exact q4isqny2... output occupies1171456physical/1153792apparent bytes;
its runtime closure has25paths/74685784NAR bytes. Metadata root and empty
workspace scratch were natively removed, while the exact output link remains
pending admission. Preserve all eight ordinary build-2 receipts with
`recorder-build-2-` prefixes beside this brief, verify their copies, then remove
only the stopped `/tmp/.../hotplug/recorder-build-2` attempt after a final
targeted owned-process check. Do not alter the output root or shared cache.

Build-2 retention/reconciliation is complete. No exact owned argv/cwd/root or
accessible fd reference remained; the workspace scratch was already absent.
All eight receipts were copied and rehashed before removing only the stopped
attempt (36864physical bytes freed). Full retained log
`recorder-build-2-operation.log` SHA-256
`0ed7a1b45e7418e910cbeafbd3ce20bc61ca92dcfb35ded7451795433b7a2ba3`,
dry-run log SHA-256
`44419f65515221741f712d32786c2558f229ac4fc642b6daa95860c66a203b31`.
The q4isqny2... output root remains verified and unchanged.

## Minimal guest admission: metadata selection first

Architect selected `probe-admission.nix` and `probe_admission.rb` in this lane's
session directory; ordinary qualification/common wiring stays held. The recipe
imports native `tests/make-test.nix`/test framework, OS846bb469... locked inputs,
the original frozen boot configuration and only the hash-verified shipped v6
fixture plus the already-built recorder. It does not import full qualification
or v5/v7, helper modules, stressors or task population. It preserves128vCPUs,
128cores/one thread/one socket,16384MiB and qualification's console boot flags.
It explicitly requests0managed disks and `virtserialport` with one diagnostic
shell. Native JSON must independently confirm all of these, including every
root/additional disk and actual store/squashfs/transport configuration. This
smaller image is admission-only, not equivalent qualification; repeat admission
in the later exact aged guest before creating its population.

The v6 store file is absent. Its immutable input is OS846bb's
`tests/fixtures/livepatch/shipped-v6-960b13f1.ko.zst`, compressed SHA-256
`9e213c68b1e017c1212a603a02ab5e1bb632d8d15b4c1488e1ba8fd7424572bd`,
expanded module SHA-256
`960b13f1b461b95e29cccff58ddf0d3f3badf151046eb46eba36a9c8c7e5efe3`.
Its existing native fixture recipe verifies/decompresses these bytes; it is not
a module rebuild. First query the native cache/build plan. No v7 compilation,
SDK copy or kernel build is selected. If frozen-boot cache misses require the
original multi-output binary restore (including dev), report its exact bounded
cost/need before realizing it; do not silently build the kernel or waive ABI.

Reserve `/tmp/ci-failure-analysis-2026-10-22/hotplug/probe-metadata-1/` exclusively
to this session/lane/attempt and only
`/tmp/ci-failure-analysis-2026-10-22/hotplug/gcroots/probe-json.drv` as its native
metadata root. The existing recorder root stays intact; shared native runner
root is held by owner1 at `podman/attempt-1/gcroots/runner`, so no duplicate root
or build. This is ownership recorded before creation. The next operation is
no-build metadata only: instantiate with IFD disabled, retain the exact drv,
native JSON from its derivation text, outputs/requisites and dry-run cache plan.
No `nix-store -r`, build, BPF, VM or aging command executes. Ceiling300s+5s grace,
1GiB additional physical allocation for immutable source snapshots/derivations,
64MiB combined output,41GiB minimum launch/40GiB floor. Per-file8MiB caps across
five metadata/log outputs keep below64MiB; native start/end df and physical/
apparent du are retained. Any IFD need or resource/identity mismatch stops and
returns to lead. Actual guest closure/cache/physical forecast is pending this
result, and blocks realization/VM launch.

Prepared runtime entrypoint, after separately selected image/closure preparation
and external resource admission, is the existing stock wrapper:

```text
/nix/store/mjlc8sc8qp6vpzf08r65jwl1y38jbgjm-test-runner/bin/test-json-runner <exact-prepared-json> /tmp/ci-failure-analysis-2026-10-22/hotplug/probe-admission-1/state
```

Set `TEST_PATH=kernel/hotplug-probe-admission`, `TEST_TIMEOUT=180`, `TEST_JOBS=1`,
`TEST_RECREATE_DISKS=1`, `TEST_DESTRUCTIVE=1`, `TEST_SYSTEM=x86_64-linux`; unset
`TEST_RUNNER_REPO_ROOT`. Owner1/3 verified wrapper SHA-256
`c90f4d93145671d8cc0c6434b5b6cdeb65c84971f2f6fdfed87e23abd587d5f2` and its
37-path/313125960-NAR-byte closure. Direct JSON execution reports scheduler
resource0: lead must separately admit actual128CPUs,16GiB guest RAM plus host
overhead (proposed20GiB RAM reservation), and at least16GiB available `/dev/shm`
for native shared backing. Shared RAM and SHM are overlapping capacity constraints,
not32GiB guest RAM. Machine JSON/store paths, no-disk confirmation, source/JSON
hash and full incremental physical allocation remain required before this
command becomes launchable. Do not inherit host `RLIMIT_FSIZE` into QEMU: its
16GiB shared-memory backing is a file too.

The RSpec admission script checks AMD/online topology/memory, expected boot image
SHA and original GNU notes build ID, exact v6 bytes, then original test semantics
of v6 enabled1/transition0 with no force. Baseline health is checked and final
health uses the same cumulative baseline/pattern, with primary errors retained
if collection also fails. Recorder only runs `--probe-only`: attach all required
probes, warm/count a short CPU127 child,2s capture and detach. Native30s command
timeout plus5s grace bounds admission; the default2s deadline is unchanged.
For this short admission only, an8MiB per-file guest limit bounds both binary
and probe log, and a limit hit fails admission. Ring is64MiB plus bounded
auxiliary BPF maps; tracefs tracing is not armed. Require recorder exit0,
ready/probe-only receipt, positive count events, all11 missed-hit counters0 and
the loader's complete loss/read/stack/map/output accounting. Locked teardown
records are attached but not expected to fire without hotplug; no task/entity
attribution is claimed from admission.

Runtime plan proposes a900s whole-VM deadline including boot, v6 transition,
admission, retention and native shutdown,64MiB combined retained runtime output
with an explicit per-log cap before selection. Native executor shutdown/kill,
destroy/finalize/cleanup own the VM; no forced v6 transition/unload. Parent
watcher retains exact owned QEMU/virtiofs process identities until all effects
end, then cleans only owned stopped data and finally releases recorder output
root after its bytes have been copied/used. No4h run is selected, and actual
image/closure/disk and cap implementation remain gates, not inferred success.

Final no-build metadata readiness was sent to lead as
`ebec6d9f-7f20-48a3-8f52-df1f37c5f62d`. Frozen SHA-256 identities:

```text
be889e35f14b4debeb5e97a84ea01b9066e9f0f869468014f31e59d6ade49b23 run-probe-metadata-1.sh
d0cb128260227156bdb1b86e28df6da7cd0465a5cdafd13126f00dd69d59777a probe-admission.nix
36a11c15bda36a271adcbc695f0ef9f45ebb168900fdade6ba99d5788f62e693 probe_admission.rb
```

Exact selected-next command, from workspace root, for a fresh watcher after lead
inspection (not self-launched):

```sh
DEV_SESSION_SLUG=2026-10-22-ci-failure-analysis \
DEV_SESSION_WORKSPACE=/home/aither/workspace/ai/vpsfree.cz \
  /nix/store/pwxj9ycwqd117yra6czifh3xfx5p88lh-bash-interactive-5.3p9/bin/bash \
  /home/aither/workspace/ai/vpsfree.cz/work/2026-10-22-ci-failure-analysis/repair/hotplug/run-probe-metadata-1.sh
```

Bash syntax, embedded Python AST, Nixfmt/parse, prepared Ruby syntax/direct
RuboCop and diff checks pass. The immutable846bb v6 archive hash above was
independently checked from its Git object. No metadata evaluation, realization,
VM or BPF execution has been run by this preparation. Owner1 has the declared
future `hotplug/probe-admission-1/state` native state path for session-owned
one-VM exclusion; it is not a reservation or launch selection.

## Watcher handoff refusals before metadata body

Watcher1 refused before command execution because it compared coordination HEAD
e8d72331 to product HEAD274e826d; the lead corrected the worktree `git -C` path.
Watcher2 invoked the script once with an erroneous literal trailing `.` argument
(events `probe-metadata-1-watcher2-events.jsonl`, completed command item11).
At script line13 this skips the zero-argument parent branch; line44 then rejects
the argument because it is not `--worker`. Exit1 occurred before creating any
attempt/log/root or invoking Nix. Both exact metadata-owned paths were independently
confirmed absent afterward. No cleanup or source correction is required.

The readiness report's separately spaced sentence period made the command
boundary ambiguous. Corrected authoritative argument vector has exactly two
entries, with **no trailing argument**:

```json
["/nix/store/pwxj9ycwqd117yra6czifh3xfx5p88lh-bash-interactive-5.3p9/bin/bash", "/home/aither/workspace/ai/vpsfree.cz/work/2026-10-22-ci-failure-analysis/repair/hotplug/run-probe-metadata-1.sh"]
```

Matching session environment and all three frozen hashes remain unchanged.
Report to lead: `22766fc4-3fc1-48d6-99c0-146003569c08`. No metadata body, build,
BPF or VM was run; any new watcher selection remains with lead. The active
first-switch VM and its observation remain outside this lane.

## Actual metadata1 result and exact boot substitution gate

Watcher3's actual two-entry command passed native0/33s. Shell environment had
both identity variables absent when diagnosis resumed; trusted thread binding
and `dev-session current` matched, with no conflict. Selected JSON drv is
`/nix/store/ydfkl27g12z5mivxh5k2lhpg3yfwzjdk-os-test-kernel-livepatch-hotplug-probe-admission.json.drv`,
output `cl0ls6bjz15pbz7yl2fz450sjh7q173w-...json`. Native unrealized JSON hash
`ddcd8d348c778652502f2901ab72e34472192ee72b616e224c25406fbf08f0ee`.
It confirms128CPUs/128cores/1thread/1socket,16384MiB,0managed/root disks,
two `virtserialport` shells including `diagnostics`, user network, no extra
shares/options. Direct boot paths:

```text
kernel /nix/store/050sh2hfrnpc8j5abr2npp7bnlxvpb8a-linux-6.12.95-frozen-boot/bzImage
initrd /nix/store/4g1i00pjc83qrbc51pmpb520gnyqd9xx-initrd/initrd
squashfs /nix/store/f1gxwakksazwsc2as0lzs7cb8zg0y8lh-squashfs.img
toplevel /nix/store/m1hw51wvfp6naiwkg73n437llcba772m-vpsadminos-system-vpsadminos-26.05pre-git
```

**Do not realize the reported full plan.** It selects46local derivations and
104cache paths (9.1MiB download/306.2MiB unpacked), including unexpected Linux/
ZFS compilation and Nix2.34.8 source/tests. The native metadata root remains;
the421888physical-byte attempt holds compact original receipts. No realization,
VM or BPF occurred. Actual free space101183143936→100508360704bytes includes
other activity; it is not attributed solely to metadata.

Specific graph paths proven by native `.drv` inspection:

- `k7h439...-etc-vpsadminos-security-evidence.json` embeds original config
  `np082...-linux-config-6.12.95`; its `kvn2...drv` depends on `sp29...-zfs-builtin`,
  which depends on `zv08...-linux-6.12.95` dev. This is a provenance/config input
  edge, not permission to rebuild or change the boot ABI.
- Frozen `hpjy...-linux-6.12.95-frozen-boot.drv` produces050...out andi1kpp...dev.
  It restores byte-checked archives and has no original-kernel drv dependency,
  but retains native Nix2.34.8-dev (`riy6...drv`, including functional tests)
  and old util-linux/toolchain inputs. A cache miss selects those builds before
  the archive restore. Architect owns any justified packaging/config refinement.
- `w229...-livepatch_6-exact-predecessor.ko.drv` only decompresses immutable v6
  archive `n9pr...` and verifies960b13...; no v6 module source build is required.

Next proposed operation: `run-boot-substitute-1.sh` queries only native remote
cache metadata for exact050...out and originalnp082...config, then (only after
both complete bounded closures are found) native `nix-store --realise` of those
**output paths**, max-jobs0,
builders empty and fallbackfalse, with the single selected cache and its
ordinary signature checks. No derivation argument, SDK restore, kernel/source
build, image assembly, VM or BPF. It tries the three already-configured caches
in order for each and stops125 without realization if either lacks a complete closure.
No substitution is presumed available merely because metadata preparation passed.
Require complete reference coverage, <=2GiB union remote NAR content and no
derivation/development output in that closure before substitution. Exact image
SHA3265b29... is checked afterward, and the output stays rooted for planned
admission/preparation. No changed kernel version/build identity is accepted.

Reserve new ordinary path
`/tmp/ci-failure-analysis-2026-10-22/hotplug/boot-substitute-1/` and only
`hotplug/gcroots/{boot,boot-config}` for this session/lane/attempt; all must not preexist.
Existing recorder and JSON metadata roots are preserved, shared runner untouched.
Budget300s+5s,4GiB physical growth,64MiB combined output,44GiB minimum launch/
40GiB floor. The cache closure gate allows at most2GiB logical NAR content;
the remaining2GiB covers transient compressed/unpack staging, block overhead,
logs and contingency. Fifteen4MiB-capped files plus small receipts fit64MiB.
The fresh watcher must enforce continuous deadline/free-space/growth/output
bounds while the client runs; this is not a hard store quota. Source cache
failure is not permission for fallback or a broader operation. Native client
exit and all owned effects must be reconciled before scratch cleanup/root
changes; no global GC/store deletion. After byte identity is retained, retain
the boot root only through already-planned image/admission use.

Only after exact boot/config packaging/cache obstacles are resolved can a
refreshed native image dry-run be accepted. Its local allowlist is restricted to
byte-verified v6 decompression and ordinary text/module-tree/initrd/system/
squashfs/JSON assembly, each inspected/budgeted. Linux/ZFS/Nix/util-linux source
builds, SDK restore or any unlisted derivation stop before execution. Full image
closure/compression/physical budget is still unmeasured and must be supplied
after that refreshed plan; this operation does not authorize small-image
assembly automatically.

Final script SHA-256:
`bc4b6c9dfd3c6ba05fc20fd6b1a24cf6b10bca1274999c69bffd59070e775041`.
Exact roots bind050...frozen out and
`/nix/store/np082gl8insab5lisjdhqlh4128jlm9m-linux-config-6.12.95`; the latter's
bytes/hash are retained after substitution rather than guessed. Both must pass
cache metadata/union admission before either is realized. After substitution,
one refreshed **dry-run only** of unchangedydf...JSON supplies the next plan.
No small-image realization is implicit. Bash syntax, embedded Python AST and
offline complete-two-closure acceptance plus SDK/oversize/missing-reference
rejection pass; files remain frozen. Report4aec3ef7-dd97-44b2-8b52-d4a4d8ba94fb.

```json
["/nix/store/pwxj9ycwqd117yra6czifh3xfx5p88lh-bash-interactive-5.3p9/bin/bash", "/home/aither/workspace/ai/vpsfree.cz/work/2026-10-22-ci-failure-analysis/repair/hotplug/run-boot-substitute-1.sh"]
```

Set both matchingliteral session environment variables for lead-selected launch.
If050...is absent, stop for a separately budgeted minimal byte restoration.
Ifnp082...is absent, stop with that concrete result; architect permits proposing
only a diagnostic configfile input from authenticated actual frozen `.config`
(archive or IKCONFIG), with exact provenance/hash, no empty evidence/suppression
or binary/v6/topology change. Neither fallback is selected by this script.

## Exact boot cache miss: bounded archive-only restoration preflight

Actual dual-output script ran once and safely stopped125 in0s. Each of the three
remote-store queries reports exact050...`is not valid` / `don't know how to build
these paths`, without CLI-option, TLS/network or timeout diagnostics. This
supports unavailability from the queried caches; it is not a diagnosed network
failure. No boot/config substitution or new root occurred, and config lookup
was not reached: np082...availability remains unknown. Preserve compact receipts
from `boot-substitute-1`, reconcile stopped owned client/scratch, then clean only
that attempt; keep recorder/JSON roots. No fallback build or blind retry.

The smallest restoration must know the actual frozen out size and config bytes
first. Prepared `inspect-boot-inputs.py` uses the same bounded NAR grammar as the
successful vmlinux inspector, streams the complete original out archive, checks
its full NAR SHAfd2ab2...and bzImage SHA3265b29..., measures regular content,
entry counts and a conservative rounded-block+metadata allocation upper bound,
and retains only a bounded entry manifest and actual root config if present.
If absent, it streams/verifies the original dev NAR SHA1b8ee6...and retains
only its actual root `.config` candidate, never a full SDK or vmlinux. No binary
output or build is restored in this preflight. Multiple/rootless candidates
remain evidence for selection; no config is guessed or used automatically.

Reserve `/tmp/ci-failure-analysis-2026-10-22/hotplug/boot-input-inspection-1/`
exclusively to this session/lane/attempt, before creation. Source is this owned
worktree's immutable boot archive parts; complete NAR hashes authenticate their
contents before retained config/manifests are written. Out parts are67108864+
36003923bytes, SHA-256dfb05b88.../8d11bedd...; the original dev parts were
already authenticated in exact-binary inspection and are rehashed in full here.
Record actual part hashes, full NAR bytes/hash, config origin/bytes/hash and
physical allocation forecast in compact output. Final selection of a new
diagnostic-only native out restore recipe/configfile override waits for these
actual bytes/sizes and architect/lead scope; no injection into the missing050
path or manual store-identity bypass.

Proposed exact command, from workspace root, for lead's fresh watcher:

```sh
DEV_SESSION_SLUG=2026-10-22-ci-failure-analysis \
DEV_SESSION_WORKSPACE=/home/aither/workspace/ai/vpsfree.cz \
  /nix/store/kmzlca218j6j1ar292fxj7707qzypij8-systemd-260.5/bin/systemd-run \
  --user --scope --unit=ci-hotplug-boot-input-inspection-1 \
  -p MemoryMax=512M -p MemorySwapMax=0 \
  /nix/store/kpw5lyh32ysqswlxhdhh9hgfqdkcm7rh-coreutils-full-9.11/bin/timeout \
  --signal=TERM --kill-after=5s 300s \
  /nix/store/jy00n3jp5xj8s40n1fbldmkcr5n7avxc-python3-3.13.15/bin/python3.13 \
  /home/aither/workspace/ai/vpsfree.cz/work/2026-10-22-ci-failure-analysis/repair/hotplug/inspect-boot-inputs.py
```

Hard bounds:300s+5s,512MiB process-tree RAM/no swap,8GiB uncompressed traversal
per archive,<=32MiB combined helper files (entry manifests<=8MiB each, config
candidate<=4MiB),<=64MiB all logs/retained output and<=96MiB physical disk growth.
Require40GiB floor plus96MiB reserve. Zstd decompression window is128MB, parser
reads<=1MiB; no full kernel/SDK disk or memory copy. Native normal exit reaps
both decompressor/source children; foreground timeout/watcher owns cancellation
of this exact operation group, then proves stopped before cleanup. No global GC,
foreign data or session lifecycle operation. Preserve compact manifests/config/
hash receipts before removing stopped own scratch. This is a scheduled archive
inspection needed to budget the separately selected binary restoration, not a
build/VM/BPF launch. Python AST passes without executing helper or archives.

Inspector SHA-256 is
`704ced365e9776ed99e914f29893331ceff7feff22f7878ced5e2425f253fda3`,
frozen and sent to lead with exact argv/resource plan in report
`56e594e2-eb0e-4095-b0ad-4b55fbe82462`. In-memory NAR tests additionally verify
exact config/content/hash retention and oversized/truncated metadata rejection;
these do not read an archived source or launch a child. The helper remains
unexecuted pending fresh watcher selection.

Cache-stop cleanup completed after targeted exact owned argv/cwd/root/accessible-
fd proof found no remaining client reference. All12ordinary attempt receipts
were copied/rehashed to `boot-substitute-1-*` beside this brief, including full
operation log SHA-256
`6c638fc8e25c90d84317747ddcbb677b1f3b2a3b6e078b19fbfa35ccc97a8534`.
Removed only the stopped exact attempt,40960physical bytes including directories;
no boot/config root existed, and recorder/JSON roots remain untouched. No store
path, foreign data or active VM was inspected/modified by cleanup.

## Actual config member and minimal native restore preparation

Archive inspection ran once, failed1 in3.309s only because the selector searched
for config at archive root. Both full original NAR hashes and bzImage hash
passed. Retained DEV manifest row12 proves a regular226335-byte member at
`lib/modules/6.12.95/build/.config`. OUT has0symlink entries,115172528NAR bytes,
114054036regular-content bytes,5788nodes and147918848conservative physical
allocation upper bound. DEV has307758104NAR bytes/20400nodes/417050624upper;
none of that SDK was restored. The stopped1.884MiB inspection evidence remains
temporarily retained for this exact restoration decision; scope inactive/no
helper per lead. Config availability through cache remains unqueried/unknown.

Architect accepted exact nested DEV-only extraction. Prepared
`extract-frozen-config.py` SHA-256
`0c265a9cb52920d8d030ea1532aca8ab00b2a7769af3fad86b724dab00221908`
authenticates the full original DEV NAR, selects only that exact path/type/size,
rejects duplicate members and writes226335bytes as `frozen.config` with origin/
SHA receipt. No OUT scan is repeated, and no SDK/vmlinux or alternative candidate
is copied. AST and in-memory exact-member/size checks pass without archives.

Prepared diagnostic-only `probe-boot.nix` SHA-256
`cc3fe546d5027b343af66a54a572567c3d3a46366667a90cab48eb4a0458335e`
uses846bb's root-selected current package set/stdenv and these already-cached
native output tools: Nix2.34.9 z4wkkj..., Zstd1.5.7-bin z8fp2..., Coreutils9.11
kpw5ly.... It uses no original hpjy restore recipe, Nix-dev, signing/compiler,
kernel/ZFS or SDK source build. Its sole future derivation restores only the
original OUT NAR into a **new diagnostic output**, checks full input NAR hash,
then dumps the restored tree and checks the identical full NAR hash again.
This verifies every boot/module byte and directory/executable shape; bzImage
SHA3265b29...is additionally checked. No reference is stripped or rewritten.
`allowedReferences = []` makes any embedded external/self store reference fail;
native postrestore reference/closure queries must also pass before image use.
No SDK or missing old store path may be pulled to satisfy an unknown reference.

The recipe also returns the exact config as a small native store input after
checking its actual extraction SHA (no guessed config). Its future use changes
only diagnostic packaging identity: a new declared boot out/module-tree path,
explicit configfile input and matching `ADMISSION_BOOT_IMAGE` path in the native
JSON. Original image/buildID/v6/ABI/128CPU/16GiB guards remain. Ordinary frozen
boot/common/qualification and product pins are unchanged. Fixture wiring waits
for exact resulting paths/graph and architect/lead selection; no claim that
same version string makes a rebuild equivalent.

Combined next package is **nested extraction plus no-build restore metadata**,
not the restore itself. `run-boot-restore-metadata-1.sh` SHA-256
`3e8fed075f0c998727dd29fd6a1a214da671297288999d57dce36cb997a05046`
checks helper/recipe hashes, extracts the exact nested config, records its actual
SHA/native config path, instantiates the new boot drv with IFDfalse and an
indirect metadata root, then records outputs/requisites/direct derivation and
one dry-run. No recipe realization is included. A full config/SDK/toolchain
build in that plan is a refusal, not permission to proceed.

Reserve `/tmp/ci-failure-analysis-2026-10-22/hotplug/boot-config-extraction-1/`,
`hotplug/boot-restore-metadata-1/` and only existing
`hotplug/gcroots/probe-boot.drv` to this session/lane/attempt before creation;
all are confirmed absent. Existing JSON/recorder/shared-runner roots remain.
Hard300s+5s,1GiB process-tree RAM/no swap (bounded native Nix evaluation after
streaming extraction),1GiB physical growth for source/config/derivation metadata,
64MiB combined output,41GiB launch/40GiB floor. Extraction's file output is
<=1MiB and metadata files each<=8MiB; actual selected config is226335bytes and
no full OUT/SDK is written. Native start/end df/physical+apparent du and exact
exit/elapsed are captured. Fresh watcher continuously enforces shared floor/
growth/output/deadline, owns exact cancellation/reaping and no foreign effects.
Metadata roots/receipts survive until parent diagnosis, no automatic retries.

Exact argv for lead-selected fresh watcher, with both literal matching session
environment variables and workspace CWD:

```json
["/nix/store/kmzlca218j6j1ar292fxj7707qzypij8-systemd-260.5/bin/systemd-run", "--user", "--scope", "--unit=ci-hotplug-boot-restore-metadata-1", "-p", "MemoryMax=1G", "-p", "MemorySwapMax=0", "/nix/store/kpw5lyh32ysqswlxhdhh9hgfqdkcm7rh-coreutils-full-9.11/bin/timeout", "--signal=TERM", "--kill-after=5s", "300s", "/nix/store/pwxj9ycwqd117yra6czifh3xfx5p88lh-bash-interactive-5.3p9/bin/bash", "/home/aither/workspace/ai/vpsfree.cz/work/2026-10-22-ci-failure-analysis/repair/hotplug/run-boot-restore-metadata-1.sh"]
```

Future OUT-only realization has measured147918848-byte data/metadata upper
bound; conservatively reserve512MiB for its output/scratch/native receipts,
plus separately measured missing cached tool/runtime closure if any. It remains
a separate selected operation after this exact dry-run, source/reference review
and final drv hash. No kernel/ZFS/Nix source build, SDK restoration, image/VM,
BPF or aging is selected by preparation. Shell syntax, Nixfmt/parse, Python AST
and exact nested-member/size parser checks pass; files frozen for inspection.

## Metadata1 limit failure and corrected metadata-only attempt2

The combined operation authenticated the complete original DEV NAR and the
unique regular `lib/modules/6.12.95/build/.config`: 226335 bytes, SHA-256
`c10922b492fdf39ed3027b9c8f7ce2846a5d3799d57d417a161595fa81a64969`.
It then failed153 after13.253s at the boot `nix-instantiate`, not during archive
extraction. The inherited8MiB `RLIMIT_FSIZE` applies to Nix's own files as well
as receipts. The exact failing file descriptor is not identified. Native
`coredumpctl info 683409` confirms signal25/XFSZ and the exact selected argv/
scope. This is a preparation-limit defect, not a frozen-ABI/cache/kernel result.

Owner reconciliation found no process argv/cwd/root/accessible-fd reference to
the exact old script, extraction or metadata attempt. Other Nix clients without
those references were left untouched. Lead already proved the scope inactive.
There is no local core in the lane or attempt. Systemd retained a root-owned
compressed core at
`/var/lib/systemd/coredump/core.nix-instantiate.1000.0104034e3a154772aa62aac7ee4ff6ef.683409.1792703427000000.zst`,
8296994 bytes /8302592 allocated; this is left untouched, not lane scratch.

`gcroots/probe-boot.drv` survived and points to the native-valid
`/nix/store/3lflyzssby6f211ki1fg4890shwy0r5q-livepatch-probe-exact-frozen-boot.drv`
(3231bytes, SHA-256
`27361fb16f7e75c0c6a6fdf10c1946ad4b970d2a47213d2b07198e506b6f3ec3`).
Its declared restored output
`/nix/store/caql6sk0mnbbrfp6cdfksas7hs903xf6-livepatch-probe-exact-frozen-boot`
is absent. `config-output.json` contains the evaluated path
`/nix/store/wqwahjqndks2l13xjgm7dvb2n4igfv70-livepatch-probe-exact-frozen.config`,
which is absent/not native-valid: `--eval` is not proof of its realization.
The authenticated extracted file is present and rehashed correctly. No recipe
realization was selected or invoked; no store path is removed. Retain this root
and small old attempt/extraction through the correction, rather than discarding
the required config or inferring that a failed command had no metadata effects.
All seven ordinary metadata receipts and the DEV provenance receipt are copied
beside this brief as `boot-restore-metadata-1-*` and
`boot-config-extraction-1-dev-receipt.txt`; the original inputs remain unchanged.

Prepared `run-boot-restore-metadata-2.sh` SHA-256
`3a8087dcef7cd8c2907200451d82f085099def3f867e539dca8b6cd0b885e10d`
reuses only that exact config, checking regular-file/canonical ownership, size
and SHA, and the unchanged `probe-boot.nix` SHA
`cc3fe546d5027b343af66a54a572567c3d3a46366667a90cab48eb4a0458335e`.
No extractor or DEV/OUT archive stream runs. Nix must inherit an unlimited
file-size limit; core dumps are disabled with `ulimit -c 0`. Six stdout receipts
and the shared operation/stderr stream each pass through an8MiB stream writer
(plus one overflow sentinel), for less than64MiB combined output. Native producer
and writer statuses are retained; truncation fails rather than becoming valid
metadata. The stream cap does not apply to Nix's store/cache/source writes.
Physical growth and shared free space remain continuously watched externally.

Reserve new canonical, initially absent session-owned paths
`/tmp/ci-failure-analysis-2026-10-22/hotplug/boot-restore-metadata-2/` and
`hotplug/gcroots/probe-boot-metadata-2.drv`. Original roots remain untouched.
Attempt2 must select the same3lf...drv; it records evaluated config path,
outputs/requisites/direct derivation and one native dry-run with IFDfalse,
max-jobs0, empty builders and fallbackfalse. The config evaluation is labelled
prospective, not realized. This is metadata only: no substitution, build,
restoration, SDK, VM or BPF. Bash syntax check passes; no operation was launched.

Exact argv for lead's fresh watcher, from the workspace root with both literal
matching session environment variables:

```json
["/nix/store/kmzlca218j6j1ar292fxj7707qzypij8-systemd-260.5/bin/systemd-run", "--user", "--scope", "--unit=ci-hotplug-boot-restore-metadata-2", "-p", "MemoryMax=1G", "-p", "MemorySwapMax=0", "/nix/store/kpw5lyh32ysqswlxhdhh9hgfqdkcm7rh-coreutils-full-9.11/bin/timeout", "--signal=TERM", "--kill-after=5s", "300s", "/nix/store/pwxj9ycwqd117yra6czifh3xfx5p88lh-bash-interactive-5.3p9/bin/bash", "/home/aither/workspace/ai/vpsfree.cz/work/2026-10-22-ci-failure-analysis/repair/hotplug/run-boot-restore-metadata-2.sh"]
```

Retain accepted300+5s/1GiB process-tree RAM/no swap,1GiB conservative physical
growth,64MiB total output,41GiB launch/40GiB reserve-floor bounds. Source metadata
already partly exists, but the1GiB allowance still covers Nix copies/cache
writes and receipts without assuming a zero-growth rerun. Native start/end df
and physical/apparent du are recorded. Watcher cancellation/reaping and owner
final exact-reference reconciliation precede cleanup. No old root or scratch
is automatically removed. ProductHEAD is freshly verified as
`c2c5a006b49730d8b72d103ff063a1e89bba1ee2`; selected immutable OS846bb/binary
inputs and the restoration recipe are unchanged. Lead selects execution and
later graph/restore admission separately.

## Metadata2 passed: selected OUT-only restore package

Lead's fresh watcher returned native0/4s, scope inactive/dead, with every native
producer/writer0. The watcher failed to create its separate outer log; the native
attempt and raw tool/events are the actual evidence, with no fabricated log or
rerun. All13 native files are retained beside this brief with prefix
`boot-restore-metadata-2-`. Native operation log SHA-256 is
`4e00ad72d62c6e6060e436cb039168a12d866f3dcd3a1f16640e66d19bdae9c0`,
direct derivation JSON SHA is
`7eab8095a68c26ce5230819f5c29acb4199608a06c3189bdf6cd5dfa39796d6b`,
and cache-plan SHA is
`4d40e1fc77f0a7afd37f7f9ace5148ebfc3d7d430828bc9c5e82df48fcfb63ee`.
The attempt occupies126976 physical/79294 apparent bytes. No native output was
restored or config store path realized by this metadata operation.

Exact native plan is one build,
`/nix/store/3lflyzssby6f211ki1fg4890shwy0r5q-livepatch-probe-exact-frozen-boot.drv`,
whose sole output is
`/nix/store/caql6sk0mnbbrfp6cdfksas7hs903xf6-livepatch-probe-exact-frozen-boot`.
Only missing substitute is
`/nix/store/4lgbwpg4r41kcsms7nlwrzdlmhw83skj-stdenv-linux`, reported59.9KiB
unpacked and0.0KiB download. Its current native Bash input is
`/nix/store/jnyfsf2mp08d1xyz2m72ic2vz2kcx0sd-bash-5.3p9`.
The drv's other direct inputs are existing current Nix/Coreutils/Zstd, exact
846bb source and builder scripts. The1133-path derivation requisites include
recipes; they are not1133 new realizations. No Linux/ZFS/Nix/compiler source
build or SDK restoration appears in the missing-output plan. Frozen image,
module and config identities remain unchanged.

Prepared `run-boot-restore-1.sh` SHA-256
`61a9cecefae1832e32db57635da710aafb3308d85a60a8c448c318b2093290c3`
uses only this immutable drv and already-cached native tools. It verifies the
recipe/drv hashes and existing metadata root, checks canonical owned paths,
refuses finite inherited FSIZE and disables cores. A fresh dry-run must contain
only3lf and at most the exact4lgb substitute. Direct stdenv/Bash input outputs
are rooted with max-jobs0/empty builders/fallbackfalse; a second dry-run must
require no substitution and only3lf. This protects existing direct input
closures from shared GC during the single allowed restore. No generalized
metadata cycle, original recipe or SDK is invoked.

Reserve these initially absent session-owned disposable paths before creation:
`/tmp/ci-failure-analysis-2026-10-22/hotplug/boot-restore-1/`, secure workspace
scratch `repair/hotplug/boot-restore-1-scratch/`, and only root names
`hotplug/gcroots/{boot-restore-stdenv,boot-restore-bash,probe-boot}`. The scratch's
complete parent chain must be canonical and not world writable; no `/tmp` mode
or native security check changes. The current recipe has `allowedReferences=[]`
and verifies the original full OUT NAR before restore and after native dump,
plus bzImage SHA3265b29.... The driver independently repeats the full restored
NAR/image checks, requires an empty native reference list and a one-path output
closure, and records native path-info/physical+apparent du. Full NAR equality
authenticates every module byte and tree shape, not just a version string.
Unknown references fail without stripping or pulling another output.

Physical forecast remains512MiB for restored output/possible native temporary
allocation/scratch/receipts, plus32MiB conservative allowance for the measured
59.9KiB missing stdenv output and metadata:544MiB maximum admitted growth.
The measured original OUT rounded upper is147918848bytes. No NAR or SDK is
materialized as a separate file; streams go through native hash/restore tools.
Fresh preparation df is103152885760 available bytes; launch repeats floor+
544MiB admission and retains40GiB. The watcher continuously samples aggregate
physical growth/floor, including store writes; this is not a filesystem quota.
Native start/end df and physical/apparent du cover attempt/scratch/output/
stdenv. Receipts have per-stream caps (build16MiB, four plan/input logs4MiB,
five verification files1MiB, operation4MiB), under64MiB total, with producer/
writer status and overflow failure. No file-size limit reaches Nix.

Exact fresh-watcher command, workspace CWD and both literal matching session
environment variables:

```json
["/nix/store/kmzlca218j6j1ar292fxj7707qzypij8-systemd-260.5/bin/systemd-run", "--user", "--scope", "--unit=ci-hotplug-boot-restore-1", "-p", "MemoryMax=1G", "-p", "MemorySwapMax=0", "/nix/store/kpw5lyh32ysqswlxhdhh9hgfqdkcm7rh-coreutils-full-9.11/bin/timeout", "--signal=TERM", "--kill-after=5s", "300s", "/nix/store/pwxj9ycwqd117yra6czifh3xfx5p88lh-bash-interactive-5.3p9/bin/bash", "/home/aither/workspace/ai/vpsfree.cz/work/2026-10-22-ci-failure-analysis/repair/hotplug/run-boot-restore-1.sh"]
```

The user scope limits the client to1GiB/no swap; Nix's daemon builder may be
outside that scope, so the watcher must separately admit/observe at most2GiB
aggregate owned client/builder RAM and cancel the authenticated native client
on excess. Native build is local max-jobs1/cores1,240s build timeout within the
300+5s outer limit. No VM/BPF/aging or other realization is authorized by this
prepared command. Bash syntax and embedded plan-check Python AST pass; no
operation was launched. Retain all roots/scratch on either result until exact
native client/builder/cwd/fd effects are reconciled. Afterwards remove only
stopped owned scratch and temporary input roots; retain caql output root through
planned image/admission use, then release it after that use ends. Do not remove
store outputs, foreign data or session state. Fixture wiring to the declared new
boot/config paths and image realization remain separately selected steps.

Actual restore1 failed1/1s before recipe execution: native build-environment
setup could not access `boot-restore-1-scratch/nix-889789-2794611120/build`
(`Permission denied`). The driver selected private workspace scratch; checking
that ancestors were not world writable did not establish native build-user
access. Both restricted plans and the59.9KiB stdenv substitution/rooting passed.
There is no OUT restore, NAR comparison or ABI result from this attempt. All12
native receipts are retained as `boot-restore-1-*`; build.log SHA-256 is
`1438dd766a143980398a92d5fe75f01674e97593ee72cb62b33cdd66c4c804c8`.
Lead proved the unit inactive; owner inspection found no exact selected-script/
attempt/scratch/drv/output argv/cwd/root/accessible-fd reference and no process
under a native nixbld UID. Scratch is empty, caql output absent; no cleanup or
root changes were performed. The retained input roots remain for reuse.

Narrow correction `run-boot-restore-2.sh`, SHA-256
`43911b480de8b883363c0858c5276a2c3a5b4e64aec9dad77b5a7e95d44afed0`,
removes the custom build-dir option and custom scratch entirely, using native
daemon-managed build scratch and cleanup. No home/workspace or `/tmp` modes are
weakened. It reuses/validates the existing exact stdenv/Bash roots and accepts
only the3lf local build with no new fetch in one fresh native dry-run. Original
script61a9cece and recipecc3fe54 remain unchanged; all full-NAR/image/reference
and source/hash guards remain. New owned attempt is
`/tmp/ci-failure-analysis-2026-10-22/hotplug/boot-restore-2/`; retain the same
544MiB physical/64MiB output/300+5s/1GiB client scope plus2GiB aggregate owned
RAM/40GiB reserve. Native scratch allocation is included in the existing
physical budget; only Nix manages that directory, with keep-failedfalse. Exact
launch argv is the previous command with unit `ci-hotplug-boot-restore-2` and
script `run-boot-restore-2.sh`. Bash syntax passes; ready and frozen, not launched.

Restore2 actually executed once and passed native0/4s. The watcher's final prose
incorrectly says it did not run; its event `item_4` records the exact selected
scope argv, completed exit0 and `NATIVE_EXIT=0`. Native attempt receipts agree.
All15 native files are preserved as `boot-restore-2-*`. Whole original NAR is
115172528bytes/SHAfd2ab2d102fdc7ec176aba6f6d5b99e8a45f0d1b099ebfcdfab1054b494dd70e;
bzImage SHA3265b29...passed. Native references are empty and the closure contains
only caql. Actual caql allocation is127807488bytes; apparent regular content is
114054036bytes. The attempt uses53248allocated/2351apparent bytes, and the
substituted stdenv uses69632allocated/60834apparent. No SDK was restored.
Owner reconciliation at2026-10-22T21:55:41.665071+00:00 found the exact scope
inactive/dead/success with empty ControlGroup, no selected script/attempt/drv/
output argv/cwd/root/accessible-fd reference and no nixbld-UID process. Proof is
`boot-restore-2-owner-effects.txt`; no retry or cleanup was performed. Retain
the caql output root for the selected admission preparation.

Architect accepted standalone fixture wiring at `probe-admission.nix` SHA-256
`ce22f0fa34866b7b3ddbbf09e4c1f63ae8ff9e2d264629efd2eae963739d602d`.
It imports the exact846bb boot-base package shape and changes only outPath/
modules to native-valid caql, configfile to the authenticated nested config,
and its override closure to return that diagnostic shape. The fixture-only
priority override takes precedence over the base force. Original dev/ABI
metadata remains lazy and unchanged; forcing it is a stop, not permission to
restore an SDK. The exact boot image/config hashes are checked at evaluation;
the generated Ruby boot-image guard uses caql. All original recorder, buildID,
notes, v6, topology, cumulative health and probe/loss checks remain. Ruby source
is unchanged at36a11c15bda36a271adcbc695f0ef9f45ebb168900fdade6ba99d5788f62e693.
This is diagnostic packaging, not a production pin or qualification equivalence.

Prepared/frozen `run-probe-metadata-2.sh` SHA-256
`18d4b5d5258841b08542ad1622d1cb967ac582f787815a77c9ef0ecf3f3b0f74`
checks those sources, cc3fe54 recipe and retained boot/recorder roots. It creates
only the new owned `/tmp/ci-failure-analysis-2026-10-22/hotplug/probe-metadata-2/`
and `hotplug/gcroots/probe-json-2.drv`, with IFDfalse instantiation, native
outputs/requisites/direct derivation, actual config hash and an unrealized JSON
copy. Assertions require128CPU/16GiB/128cores/1thread/1socket, zero disks/no root
disk or image, two virtserialport shells, exact caql boot path and the boot/
authenticated config inputs in the graph. One max-jobs0/empty-builder/
fallbackfalse dry-run records the actual remaining cache/assembly plan; no
realization occurs. A historical SDK/restore or Linux/ZFS/Nix/compiler source
build in that plan stops subsequent selection and requires its exact edge.

Exact command for the lead's fresh watcher, workspace CWD and both literal
matching session environment variables:

```json
["/nix/store/kmzlca218j6j1ar292fxj7707qzypij8-systemd-260.5/bin/systemd-run", "--user", "--scope", "--unit=ci-hotplug-probe-metadata-2", "-p", "MemoryMax=1G", "-p", "MemorySwapMax=0", "/nix/store/kpw5lyh32ysqswlxhdhh9hgfqdkcm7rh-coreutils-full-9.11/bin/timeout", "--signal=TERM", "--kill-after=5s", "300s", "/nix/store/pwxj9ycwqd117yra6czifh3xfx5p88lh-bash-interactive-5.3p9/bin/bash", "/home/aither/workspace/ai/vpsfree.cz/work/2026-10-22-ci-failure-analysis/repair/hotplug/run-probe-metadata-2.sh"]
```

Budget is300+5s,1GiB client process-tree RAM/no swap,1GiB incremental physical
allocation for Nix source/cache/config/derivation metadata,64MiB combined
receipts/logs,41GiB launch and40GiB reserve. Stream writers bound five stdout
receipts, unrealized JSON and operation/stderr to8MiB each; there is no inherited
FSIZE cap and cores are disabled. Native df and physical/apparent du accompany
exact exit/elapsed; the watcher continuously guards shared free space/growth and
reconciles owned client effects before any cleanup. No daemon builder, image,
SDK, VM/BPF/aging or second runner is launched by this package. Nix formatting,
Bash syntax and embedded Python AST checks pass. Future image/cache/physical
forecast and external128CPU/16GiB plus overhead/SHM admission wait for the actual
returned JSON/graph; current VM allocation remains zero.

## Native metadata2 result and bounded image assembly1 readiness

Metadata2 ran once, native0/17s. Actual JSON drv is
`/nix/store/af46in1r9ad9izm6j0ldd31yw8mbrwqp-os-test-kernel-livepatch-hotplug-probe-admission.json.drv`,
rooted at `hotplug/gcroots/probe-json-2.drv`; the watcher's other non-hotplug
root check was incorrect. Actual native JSON SHA-256 is
`daafd11dde916f90772276902b2b1acd7a73e99451e109442a88d4bfb147256a`.
It proves caql boot, authenticated native wq config,128CPU/16GiB/128cores/
1thread/1socket, zero managed/root disks and two virtserialport shells.
All13 native metadata files are retained as `probe-metadata-2-*`. A metadata
pass alone does not accept a realization plan or runtime probe admission.

The actual cache plan (`probe-metadata-2-cache-plan.log`, SHA-256
`c274e3434065d84f80c2b3508cc03201b55448648212d639de8e8b595e30ee54`)
has35 local assembly recipes and seven substitutes,2.3MiB unpacked/0.9KiB
reported download. Source inspection distinguishes the `48h45...-zfs.drv`
empty `mkdir -p $out` stub from a ZFS source build. `nuke-refs` and `builder.pl`
are script substitution; other work is text/symlink/module-tree/depmod, shrunken
initrd modules, copied utilities/initrd, system/closure-info, exact-v6 archive
decompression, squashfs and JSON. There is no historical SDK/restore recipe,
Linux/ZFS/Nix/compiler source build or module recompilation. Immutable drv
source identities and command excerpts are retained in
`probe-metadata-2-build-commands.txt`; structured attrs remain in the named
native drv sources. The original boot remains immutable. Initrd's native
`jskbszkqz0ajx8dfdgbl0r0dfvk6f2is-make-initrd.sh` copies its selected closure,
then streams cpio into Zstd; it does not write a second uncompressed archive.

Assembly uses exact preimage targets
`4zjf4jfp9kc600112m99s7jh9cjqybiq-initrd.drv` -> `rvnizvi1h8hqam4hfd5fqwq5qvz10kw3-initrd`,
and `pkffw9c6l7fpr724rpj5waksbldyw10n-closure-info.drv` ->
`vyr95d620vbi96kjnh37y8rnv6bzyr20-closure-info`. Their selected pending
dependencies are exactly33 of the35 recipes. Only
`2cmf2q4cmkdnalv2h2gs4kgpdsjj5iz9-squashfs.img.drv` and af46 JSON remain
after these targets; final outputs are kh5nb7...squashfs and
`/nix/store/4kkh0742658h9c2q5ckw7nb2iq5qxwic-os-test-kernel-livepatch-hotplug-probe-admission.json`.
No image plan is guessed from a filename alone.

Prepared `run-probe-assembly-1.sh` at the current-readiness hash above performs
only those native builds. It authenticates the frozen source/plan and these
literal native argument/accounting files (not a separate review system):

| File | Meaning | SHA-256 |
| --- | --- | --- |
| `probe-assembly-1-inputs.txt` |320 selected cached leaf output paths; root without substitutes/build fallback | `c7582dcf57b96346776a5dd554b213c3c2e5a6a4bea610d68bea9871fe00c77a` |
| `probe-assembly-1-substitutes.txt` | Only the seven approved cache outputs | `a16cf854ce284dfd4a34258e601e656c7c9c59d947127de2b902b9ec86300495` |
| `probe-assembly-1-outputs.txt` |35 selected assembly output paths for cumulative physical accounting | `90c0a82028a28844443f26ebb2180568cb2687fb1c44f40b37099ef4fd50bf2a` |

The cached leaves were selected by the exact pending drv input/output selectors,
stopping at native-present/cache-selected outputs; no unused SDK output is
added. Rooting cached leaves uses max-jobs0 and empty substituters/builders;
a GC race fails instead of refetching an unbudgeted replacement. Seven separate
substitute-only outputs use max-jobs0/builders-empty/fallbackfalse, with actual
copy messages restricted to the same seven. Native roots retain their runtime
closures. Fresh plans allow only subsets of the original35/seven, then35/no
fetch after rooting, and only the final two/no fetch after preimages. No
unexpected recipe is executed.

Reserve new canonical owned attempt
`/tmp/ci-failure-analysis-2026-10-22/hotplug/probe-assembly-1/`, root directory
`hotplug/gcroots/probe-assembly-inputs-1/` (native input/substitute root prefixes),
and root names `probe-initrd`, `probe-closure-info`, `probe-admission-json`.
All are new and guarded absent. Use native daemon build scratch with
keep-failedfalse; no private custom build-dir or permission change. Lead retains
all roots and compact receipts until owned client/builder/cwd/fd effects are
reconciled. Thereafter only these stopped temporary input/preimage roots may be
removed; retain JSON/boot/recorder roots for admission. No store/global cleanup.

The first-stage forecast is at most1GiB for module-tree/shrunk-module/initrd/
utility copying and temporary/output coexistence: original OUT is127.8MB
allocated, shrunken module data is bounded by the original module data, and
Busybox's entire missing package is within the seven-output2.3MiB NAR total.
Other first-stage outputs are text, symlinks and metadata. The true guest
closure/compressed image size is not yet measured. The driver obtains native
`total-nar-size`, `registration` and `store-paths` after preimages and records
actual guest-closure physical allocation before choosing compression.

The single4GiB budget is never reset. Let U be physical blocks of every selected
assembly output, seven cache outputs, attempt and input-root directory, plus
32MiB reserved for automatic root/database/native-log metadata. Existing or
hardlinked blocks are counted again conservatively. Let N be the measured guest
closure NAR bytes and R the registration bytes. Before compression require
`U + (2*N + 2*R + 256MiB) <= 4GiB` and
`freshFree - (2*N + 2*R + 256MiB) >= 40GiB`. Two N-sized allocations reserve
image/output/temp coexistence;256MiB covers encoder metadata, logs, JSON and
remaining native scratch. Actual encoded/output sizes are still verified after
assembly. Unrelated frees and store deduplication never reduce U. Failure stops
before squashfs/JSON with the native measured forecast, without increasing the
budget or retrying. All final output allocations are recounted; df is a separate
shared-floor observation, not the owned-growth counter. Fresh preparation df is
136176259072available bytes; launch requires at least44GiB.

Exact fresh-watcher command, workspace CWD and both literal matching session
environment variables:

```json
["/nix/store/kmzlca218j6j1ar292fxj7707qzypij8-systemd-260.5/bin/systemd-run", "--user", "--scope", "--unit=ci-hotplug-probe-assembly-1", "-p", "MemoryMax=1G", "-p", "MemorySwapMax=0", "/nix/store/kpw5lyh32ysqswlxhdhh9hgfqdkcm7rh-coreutils-full-9.11/bin/timeout", "--signal=TERM", "--kill-after=5s", "600s", "/nix/store/pwxj9ycwqd117yra6czifh3xfx5p88lh-bash-interactive-5.3p9/bin/bash", "/home/aither/workspace/ai/vpsfree.cz/work/2026-10-22-ci-failure-analysis/repair/hotplug/run-probe-assembly-1.sh"]
```

Limits:600+5s outer, native480s build timeout, max-jobs1/cores2,4GiB cumulative
physical/40GiB floor,64MiB combined output. Capped stdout/stderr receipts total
at most52MiB;35 native recipe logs are individually limited to256KiB (8.75MiB
total), leaving room for small control receipts. Overflow fails. No inherited
FSIZE and cores disabled. Native start/end df/physical+apparent du, exact exit,
allocation gate, actual JSON hash and complete native closure are retained.
Boot image/config/exact-v6 hashes and final JSON daafd11...must all pass.

The1GiB user scope limits clients, not daemon builders. Lead's fresh watcher
must sample at most4GiB aggregate owned client/builder RAM and shared space,
including native transient scratch where observable; these sampled thresholds
are not a hard tree/filesystem quota. Squashfs requests `-mem2048M`, which is not
aggregate RAM, and can autodetect all allowed host CPUs. Neither cores2 nor
NIX_BUILD_CORES is a2CPU enforcement claim. Cancel the authenticated native
client/scope on deadline/resource excess, retain native cancellation/cleanup,
then independently reconcile daemon builders and escaped cwd/fd effects before
cleanup. Remaining/inaccessible ownership or interrupted cleanup is incomplete
evidence requiring lead reconciliation, not proof that effects ended. No other
session-owned VM/full-host assembly runs concurrently; foreign workloads are
resource context only. No VM/BPF/aging/source change or automatic review is
selected. Bash syntax and all three embedded Python ASTs pass; files are frozen.

For the future short probe-only VM, lead explicitly selected a diagnostic2:1
CPU-overcommit exception. Actual measured launch affinity is64 on AuthenticAMD
EPYC7551; the earlier native count96 is superseded as effective launch-capacity
evidence. The ordinary1.5 rule/minimum86 is not met or claimed, and no product or
native default changes. Preserve guest128CPU/single-thread topology/16GiB.
The final external guard must record fresh actual launch-affinity IDs and require
at least64, with effective ancestor CPU quota/cpuset capacity also at least64;
established unlimited quota is acceptable, unknown or smaller capacity refuses.
Record fresh host load and declare a bounded saturation refusal in the final VM
package. Keep fresh non-overcommitted RAM/SHM/full-disk admission, one session VM
after exact effects release, and no overlapping owned full-host squashfs work.
Direct JSON reserves0. This exception covers only probe attachment/counts and
one2s count child within an overall900s operation: no hotplug, age, population,
v7, hardware/timing or qualification equivalence. The aged original workload
requires separate CPU/context selection. This source/brief direction selects
no VM execution or observation of another lane's VM. Assembly script88dd09d7
and its source/hash/resource contract remain frozen and unchanged.

## Assembly1 effects reconciliation and compact retention

Owner final proof is [probe-assembly-1-owner-final-effects.json](probe-assembly-1-owner-final-effects.json); cleanup is [probe-assembly-1-cleanup.json](probe-assembly-1-cleanup.json). At22:56:34UTC the selected scope was inactive/dead/success with empty cgroup. No exact selected client, build-user process or matching accessible cwd/fd references remained. The remaining root PID1299969 is the shared PPid1 `nix-daemon.service` main process, not an owned builder; its protected cwd/root/fds were inaccessible, and passwordless sudo was unavailable. Those privileged descriptors were not inspected. No foreign process was signalled.

All18 native attempt receipts and the guest closure-info registration/store-paths/total-nar-size are retained here. Removed only the stopped owned `hotplug/probe-assembly-1/` directory and327 exact input/substitute links under `hotplug/gcroots/probe-assembly-inputs-1/`, releasing1257472 allocated bytes; df delta1253376B is recorded separately, not attributed as a store-growth measure. Released flat temporary initrd/closure-info roots after retention; the JSON closure retains the runtime initrd. JSON/boot/recorder and shared runner roots remain. No store path deletion or global GC occurred.

Deviation: the earlier `nix-store --query --roots` observation intrinsically pruned already-stale foreign notification indirect auto-links `dgqpj7ql8bsg96yfswsrd5v162i4w2hg`, `m90hlf8ssa7lilmgrwzkcfwwjk0x5l2l`, `bzc4mihdj7hfkshpsrhf45nmjxp2bbq7`, `fg66mfvlnnlkzz5cb0qjzydiwgj2i5w9`. Their notification targets were absent. No data/store output was removed or guessed root recreated; the query was not repeated. Future observations use only exact owned links.

Assembly final physical receipts measure squashfs424976384B, initrd9789440B, closure-info258048B and JSON8192B. Native closure626paths/2020835392NAR bytes and final JSON SHA256daafd11 remain authoritative. Missing continuous watcher sampling prevents a peak-resource or aggregate-hard-cap claim. No AMD VM/BPF admission result exists.

## Short probe-only admission1 — prepared/frozen, not selected

Architect0 accepted the exact frozen guardian/launcher after full independent
inspection; no source correction or execution is selected. The22GiB scope is a
ceiling, not guaranteed capacity: the effective ancestor20GiB headroom gate may
bind earlier. The2GiB future regular-filesystem forecast applies only to this
zero-disk, read-only-squashfs short probe; it does not cover aging or other lanes.

Native assembly is complete; no further Nix operation is in this command. Final launcher [run-probe-admission-1.sh](run-probe-admission-1.sh) SHA256 `8662565f80d237d8d31b477e0c72e2c44f778b34657fd265e229e29a9ab96572`; fixed guardian [guard-probe-admission-1.py](guard-probe-admission-1.py) SHA256 `01dbef171620b4c7792f9984b9fb7bc1b3656d3ffe07ff1c79f891e9b13a48f1`. Bash-n/Python syntax pass. [Inert checks](probe-admission-1-inert-checks.json) cover64CPU/unlimited and exact64 quota, reject63CPU quota/cpuset, unknown active controller and hidden ancestors; fake native completion, detached-birth survival and final-scan failure; component-exact argv/fd references. No real host admission, runner, VM or signal occurred in those checks.

Lead alone may select this exact command from the session tracking directory, through a fresh watcher (two-entry Bash argv; no trailing dot):

```sh
/run/current-system/sw/bin/env DEV_SESSION_SLUG=2026-10-22-ci-failure-analysis DEV_SESSION_WORKSPACE=/home/aither/workspace/ai/vpsfree.cz CI_FAILURE_ANALYSIS_HOTPLUG_VM=probe-admission-1 /run/current-system/sw/bin/systemd-run --user --scope --unit=ci-hotplug-probe-admission-1 --property=MemoryMax=22G --property=MemorySwapMax=0 /home/aither/.nix-profile/bin/bash /home/aither/workspace/ai/vpsfree.cz/work/2026-10-22-ci-failure-analysis/repair/hotplug/run-probe-admission-1.sh
```

Owned new runtime directory is `/tmp/ci-failure-analysis-2026-10-22/hotplug/probe-admission-1/`; native state is its `state/`. Guardian refuses existing/symlinked attempts, checks canonical owner/ancestors, frozen source/JSON/boot/config/v6/recorder/initrd identities and626path native closure existence without querying or realizing Nix. The actual native argv is `/nix/store/mjlc8sc8qp6vpzf08r65jwl1y38jbgjm-test-runner/bin/test-json-runner /nix/store/4kkh0742658h9c2q5ckw7nb2iq5qxwic-os-test-kernel-livepatch-hotplug-probe-admission.json /tmp/ci-failure-analysis-2026-10-22/hotplug/probe-admission-1/state`. Shared runner root remains owner1/lead's; no duplicate root. Rooted runtime JSON/boot/recorder outputs remain untouched.

The fixed JSON remains SHA256daafd11, original846bb source/locks, restored byte-identical caql boot (original GNU7801779436291880089e3407e50e5813f80d76f1), authenticated wqwah config SHA256c10922, exact v6 SHA256960b13 and built q4 recorder. Initrd SHA256 is `73592d76c6fbaaebf919029d3686231c32d98ad6898a449a3d0ec2872b6b62fa`. Changed diagnostic packaging and smaller guest configuration are already declared above. Actual guest128CPU/128cores/1thread/1socket,16GiB, zero managed/root disks, two virtserialport shells are checked again. This is one2s child/probe-only attach/count/detach, with baseline/final cumulative health and loss assertions. No hotplug/population/age/v7/qualification or hardware/timing equivalence is claimed. Admission must repeat before population in the eventual exact aged configuration.

External resource predicates are implemented, since direct JSON reserves zero. Fresh affinity IDs, effective ancestor quota/cpuset and cgroup context must prove >=64 usable logical CPUs with no hidden/unknown limits. Lead's explicit short-only <=2:1 exception admits128guest/64effective; native1.5 and128physical are never claimed. Host vendor must be AMD. Two2s prelaunch samples each refuse affinity CPU busy>=90%, runnable>2*Ceff or CPU PSI some avg10>=25%; record load/runnable/pressure and IDs, without claiming idle or exclusive CPUs. A second capacity/headroom check immediately precedes native spawn. No own full-host assembly can coexist; all declared support/Podman/hotplug attempt refs are checked, with foreign workloads treated only as capacity context.

Fresh host MemAvailable>=24GiB admits the22GiB hard no-swap client/runner/guest scope plus2GiB host reserve; effective ancestor cgroup headroom must independently be>=20GiB (16GiB guest+4GiB overhead). SHM free>=17GiB independently admits the16GiB guest backing plus1GiB; shared backing is not counted twice as a second16GiB RAM demand. Available disk must be>=44GiB. Incremental regular-filesystem allocation forecast is2GiB (zero new disks, <=1GiB scratch,64MiB output and remaining conservative overhead); previously prepared563941376B store upper is retained, not discounted by unrelated frees. Temporary/output coexistence fits this future2GiB ceiling. SHM capacity is separate from regular-file growth. No cache/build growth is allowed.

Guardian continuously samples allocated blocks/output/free space, memory/swap, fresh CPU limits, native group births and canonical argv/cwd/root/accessible-fd references (target interval<=1s; actual scheduling can delay samples). It cancels on2GiB allocation,64MiB aggregate file-output threshold,42GiB disk stop margin, <2GiB MemAvailable, <1GiB SHM, new swap activity, unknown/reduced CPU capacity, unexpected disks, second owned QEMU or ambiguous own references. Main stdout/stderr writer is hard-capped32MiB and excess bytes counted/discarded while cancellation proceeds. Guest recorder alone inherits `ulimit -f8192` (at most8MiB per file); QEMU/Nix never inherit it. Native console/shell files and aggregate64MiB/physical2GiB thresholds are sampled cancellation bounds, not a filesystem quota; report overshoot/peaks honestly. Scope RAM/no-swap is hard only for processes remaining in that scope; escaped references retain incomplete status.

Architect accepted timing: monotonic runner launch, authenticated own-group INT at780s; at900s unresolved effects => incomplete/escalate and watcher retains responsibility. Earlier resource breach requests INT immediately and starts its own at-most120s escalation interval. No automatic broad TERM/KILL, foreign signal or deletion. Native Executor owns guest shutdown, quarantine remains, and v6 is not forced/unloaded. Pulls/teardown may outlast the interval; interrupted capture/cleanup is incomplete. The900s boundary does not guarantee total effects/resource-residence completion. Watcher must retain responsibility beyond it for surviving/ambiguous effects until lead-directed native reconciliation.

Canonical refs and retained observed process births are rechecked at parent exit, observer failure/lost identity and final result, independently of group emptiness. A detached known child, remaining socket, held lock or failed final scan forces incomplete. Path matches alone never authorize signalling. Exact root links, df start/end, allocated/apparent du, native status, cap losses and sampled peaks remain in wrapper/attempt receipts. Guardian performs no cleanup. Owner reconciliation and compact retention precede any later authorized removal of stopped owned state; no global GC, foreign cleanup or session lifecycle action. No launch/VM/BPF authorization is inferred from this preparation.
