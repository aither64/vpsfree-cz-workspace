# Independent committed remediation review

Reviewer: retained reviewer0, gpt-6.1-sol/xhigh/read_only, no overrides or nested
agents. Report returned to lead; this durable record preserves its finding,
dispositions, exact revisions, history conclusions and qualifications.

Scope: affected recorder shutdown/completeness/error handling, architecture,
proportionality, exact-host compatibility and all-eight message/history
provenance. Earlier conclusions on unchanged source are retained.

## Important: BPF dispatch drops omitted from completeness

Final recorder owner19562b6449f01ca4939d57f70ee59de8af13880f,
tests/suite/kernel/livepatch-6.12.95/hotplug-recorder.c:220-243,328-348.

report_missed_hits reads only bpf_link_info.perf_event.kprobe.missed for eleven
perf links. Four raw links have no native missed-dispatch check. Map/emitted/byte
checks cover invocations reaching the BPF program; they cannot account for
invocations suppressed before record().

Exact frozen Linux source a2384967b90f24d2470c9eb15f0e66d938df7e08 distinguishes:

- kernel/trace/trace_kprobe.c:1350-1353,1739-1762: queried kprobe counter is
  kp.nmissed plus rp.nmissed for return probes, excluding program recursion
  suppression. The ordinary perf-kprobe path calls trace_call_bpf at1669.
- kernel/trace/bpf_trace.c:116-126: trace_call_bpf skips programs when
  bpf_prog_active is already set and increments attached programs' misses.
- kernel/trace/bpf_trace.c:2315-2330: raw __bpf_trace_run separately skips an
  active same-program invocation and increments that program's misses.
- kernel/bpf/syscall.c:2279-2291,2294-2320,4614-4617: these per-program counters
  are exposed as bpf_prog_info.recursion_misses. Increments do not require
  enabling run-time statistics. Normal userspace-loaded programs allocate
  statistics in kernel/bpf/core.c:139-163; syscall.c:2767 uses that path.
- include/linux/bpf.h:2223-2238 documents/implements instrumentation suppression
  through bpf_prog_active; perf-event BPF also uses that per-CPU guard at
  kernel/events/core.c:9809-9819.

This is a reachable dispatch boundary. A suppressed invocation updates neither
ring nor emitted/kind/error maps. If earlier records supplied required kinds,
current counters can remain zero/equal and report success despite a missing
scheduler operation. Both grace periods may complete correctly; quiescence does
not make the kprobe counter include every BPF dispatch loss.

Smallest supported correction: retain exact-kernel loader, two barriers, links
and object lifetime. Check native recursion_misses evidence for EVERY recorder
program, raw and perf, using existing loaded-program descriptors before object
close. After successful detachment and grace two, program counters can be read
as stable lifetime evidence while the object owns program FDs. Link-specific
kprobe snapshots remain distinct evidence and still precede link destruction.
Reject nonzero or unavailable/unvalidated program-counter evidence. Conservatively
include setup/disabled-window misses and document whole-loaded-program-lifetime
scope; do not claim CPU127-only or capture-window program counters.

No global tracing registry, kernel patch, stats-toggle framework or callback
redesign is required. Extend the small actual-C regression so raw/perf program
misses fail despite zero kprobe misses and matching map/byte totals; failed or
missing reads must remain incomplete. PASS41 fakes only link missed counters
and cannot establish this obligation.

No actual recursion drop, CPU127 lost record or connection to the WARN was
observed. This source-supported false-completeness omission predates the two
GLOBAL patch and was uncovered in changed loss-reporting review. It is not a
claim that membarrier introduced the issue. No Blocking or additional unchanged
writer/reader/GC finding established; no waiver supplied. Recorder completeness
and affected independent review remain OPEN.

## Original findings

The specific shutdown-order race is corrected at SOURCE level under the exact
kernel assumptions: QUERY before output creation/attachment; disable; GLOBAL1;
live perf-link missed snapshots; every acquired perf/raw destruction attempted
once and handle nulled; GLOBAL2; final drain/accounting with maps/ring/output
open. Failed barriers/destructors prevent stable completeness. Error and monotonic
abort cannot become success after SIGUSR1. Partial/null attachments and closes
are covered by source inspection and actual-C mocks.

Reviewer independently inspected kernel/sched/membarrier.c:649-656 GLOBAL
synchronize_rcu implementation for multiple online CPUs, normal-RCU BPF dispatch,
tracepoint preemption exclusion, raw/perf link releases. Support QUERY and fixed
build-ID boundary are essential; no portability to arbitrary kernels is proven.
Barrier may stall with the kernel; no new sleep/fallback/deadline guarantee.
Real barrier/attachment/capture remains unexecuted. Overall completeness remains
open because of the new Important finding.

Validation provenance is FIXED for this exact committed series. All eight
messages state actual validation/material limits, preserving subjects/body
prefixes, authors/dates and <=80 columns. Recorder distinguishes corrected
compile/rejected-CLI evidence from guard INCOMPLETE and real kernel/BPF gaps;
offset/missing-argument exits are not successful offset/load validation. Other
messages preserve nonreproduction/failed captures, synthetic fields and missing
production runtime. Normal hooks passed; width-preference warnings not suppressed.

## Exact range and equivalence

Base846bb469505789ba0b2a405fa5905ba6d8253006; reviewed detached head
19562b6449f01ca4939d57f70ee59de8af13880f; tree
3e04ce2bd85f871c3f40f86db5668f30684100a4; checkout
worktrees/2026-10-22-ci-failure-analysis/vpsadminos-validation-messages.

Reviewer verified bound dev-session current first; both environment variables
absent. Read mandatory review/all four references, original report, supplementary
packet/series/diff/stat, local instructions/policy, design/kernel evidence,
actual-C mock/results, full corrected-build validation and Stage1 assessment.

Independent read-only Git/object comparisons establish all eight old/pure/final
owners, exact unchanged first-seven source trees; equal old/pure full-index
patches/trees; original authors/name/email/date preserved. Pure head
db42571928c08debf2485485bec4c7e5ac92d641 has exact oldtree
04b33b688828b55c8d91deef51c49392de78495c and empty diff from9bea; dated backup
points exactly to old9bea. Only recorder owner8 differs from pure tree: C plus
eight docs lines,128insertions/34deletions, full-index delta SHA256
56f36d35c469b57480b10c704af89a40b47571510033ac270d62d5fec6c613dd.
Full base-to-final diff equals artifact SHA256
b37f8c9ccc8be575514223e91830581855c1a09dd56f4658d6aebe9106f21db0;
25files/3631insertions/89deletions. Isolated status/index clean; shared ref still
old9bea. CAS unselected; review supplies no CAS authority.

## Final history, migrations and repeated streams

Final eight logical owners:

1. ae33b06b0: future writer persistence.
2. be4ec430d: authenticated existing-state recovery/import-publication/GC safety.
3. 50a796f28: manual predecessor DHCP fixture.
4. 247c091e6: manual first-switch evidence capture.
5. a1c4dc932: historical discovery/manual-selection gate.
6. a2e4c0971: production-origin v1/v2 impermanence case.
7. 39b6f68f2: cumulative qualification health.
8. 19562b644: standalone experimental recorder, shutdown repair folded in.

Whole history remains coherent: no obsolete shipping approach, fixup/WIP owner,
chronological repair, reverted experiment or transitional shim. Pure-message
and backup objects preserve old lineage without shipping old recorder followed
by repair. No existing version identity lowered/reused or published patch
lineage discarded in this unpublished reconstruction. New finding belongs in
owner8, not a ninth fixup.

NO MIGRATIONS: no database/schema migration/new persisted-format version;
no transitional/merged/released/deployed/externally consumed migration boundary.
Prior YAML/run-ID compatibility conclusions unchanged.

NO REPEATED dependency/channel/input/kernel-pin/generated update streams. No
changed lockfile/dependency/kernel/channel pins; predecessor/diagnostic target/
production baseline are distinct roles. No redundant intermediate pin retained.

## Architecture and compatibility

Correction remains standalone recorder plus owning docs; native exact-kernel
synchronization, unchanged BPF/header/Nix/qualification bytes, event ABI, limits,
build-ID/CPU127 predicate. No generic framework, runner change, persisted format
or coordinated fleet update; unsupported syscall fails closed. Program-counter
obligation is existing complete-capture contract, not broader orchestration.
Earlier root ownership, GC fence, publication identity and production-test
conclusions stand because their trees/patches are unchanged. No second unrelated
full review performed.

## Retained verification and operational limits

- PASS41 exercises actual C cleanup with fake boundaries and reproduces old
  false completion; no program recursion misses or real RCU/membarrier/BPF.
- Exact C4bf11e25/packagezm13->kpkc C+BPF compile/helpPASS. Missing/offset
  nonzero emptylogs; --seconds rejected. No offset/duration/load semantics.
  BPF/header/recipe unchanged.
- Build4 guard INCOMPLETE; native compile success separate. Protected/capped
  effects and hidden allocation unknown; assessment/effects hashes verified.
- Full Stage1 assessmentea4186cf read: nine hook pairsPASS,44.1393859386s wall
  trace span (not monotonic/cadence proof), one1520process scan/no positive
  canonical refs/protected/fourFDcaps, scope/cgroupabsent, historicalbirthsmissing.
  Lead accepted bounded current reconciliation and released its Gitwindow;
  no repeat scan or monitoring-PASS claim.
- Final-head selector/source/input proof and packaged production/candidate
  bytes held. Old4de STOP preserved; inmh/vp408 mismatch not equivalence.
- Production-origin v1/v2 recovery/data/retirement, real recorder barrier/
  verifier/load/attach/count/loss/hotplug/aging and DHCP attribution unproven.
  Historical boot rejection remains binding.
- No readiness, CAS, publication, integration, deployment, cleanup or lifecycle
  authority. Reviewer wrote no files, ran no tests/builds/Nix/probes/live effects
  scans/Git mutations/cleanup and returned report to lead.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-ci-failure-analysis/
