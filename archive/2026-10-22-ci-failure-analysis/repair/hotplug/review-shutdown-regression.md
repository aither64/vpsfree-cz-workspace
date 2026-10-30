# Recorder shutdown finding: bounded preparation

Historical proposal, superseded by the selected exact-kernel two-GLOBAL contract
in `design.md` and the [prepared source/check packet](review-shutdown-fix.md).
The source correction passes selected native syntax/actual-helper compilation
and all41 controlled mocked cases; corrected packaged build/runtime remain
unselected.
The text below records the original read-only proposal and unresolved API state
at that point, rather than current design acceptance.

Read-only preparation for reviewer0's Important finding at reviewed head
`9bea27c93beb22d08c3be2eb481bce4ef57300a6`. Product sources, Git state, built
outputs and frozen admission inputs remain unchanged. No check, build, BPF
attachment or VM has run for this proposal. Architect owns the protocol decision;
lead must select source edits and execution separately.

## Confirmed source boundary

- `hotplug-recorder.c:407-420` disables the control map, consumes the ring and
  reports statistics/missed hits before destroying the eleven perf links and
  four raw links. Disabling recording does not itself wait for a prior invocation.
- `hotplug-recorder.bpf.c:50,65,147-150` checks enabled before reserving/filling
  and submitting an event. A producer that passed the check may still be in
  flight while the final consumer/report runs.
- `hotplug-recorder.bpf.c:251,256` updates pin-map errors outside `record()`'s
  enabled check. Stopping ring emission alone therefore does not stabilize all
  final counters. Both raw and perf producer families need the selected barrier.
- `hotplug-recorder.c:239-254` reads final missed-hit evidence through live link
  descriptors. Preserve that evidence across quiescence; do not assume a generic
  detach, duplicate descriptor, disconnect or close provides the needed semantics.

The exact frozen-kernel/libbpf detach and synchronization guarantees, including
retained counter-descriptor lifetime and failures/unsupported operations, remain
an architect design dependency. A fake producer test cannot establish those
kernel guarantees. No new accounting protocol or kernel change is proposed.

## Focused regression proposal, not an execution selection

Exercise the actual bounded cleanup function after the narrow extraction, if
needed, with small fakes at the selected libbpf/control/ring boundaries. Prefer
one native C check in the owning package over an alternate recorder or a generic
mock framework. A new test path/check-phase change needs explicit allocation.

1. Start with valid existing count/output data and a producer already past the
   enabled check. Hold its final submission until the selected quiescence call.
   Deliver that event and its statistics at that boundary. Require the real
   cleanup to retain the event, include its final totals and return success only
   when bytes and stable emitted count match. The old ordering must reproduce
   loss/false completeness in this controlled interleaving. Use no timing sleeps.
2. Raise a missed-hit value between disable and completed quiescence. Require
   final evidence to retain that value and fail completeness. Also delay a
   pin-map-error update without an event: it must make the final result fail.
3. Cover all producers, partial attachment and null handles. Every owned handle
   is attempted/closed once even when another stop/detach/counter call fails.
   Unsupported or unproved quiescence is non-success, not an implicit fallback.
4. Inject missing/non-perf counter evidence, drain/callback/output-cap/write
   failures, and preserve prior abort/error status despite successful cleanup.
   SIGINT/SIGTERM remain failures; SIGUSR1 can succeed only with complete data.
   Keep descriptor/ring/object lifetime valid through the final reads/drain.

The assertion is observable capture completeness and failure status, not merely
a prescribed list of function calls. Retain the existing CLI/build-ID/CPU127,
all required observations, output limits and loss semantics. No test executes
the BPF loader path, probes or a guest. Native compilation/check execution is
still unselected; propose its exact current-toolchain command/budget after the
bounded protocol and file scope are selected.

## Logical owner and remaining gates

Fold the caused correction and its meaningful regression into recorder owner
`9bea27c9` after reviewer0 completes and lead grants an isolated Git window.
First retain an exact backup ref, verify publication/consumption constraints,
keep parent `81235fe7` and unrelated bytes unchanged, and compare the revised
single owner/range and final tree. Preserve partial receipts; no fixup residue,
default merge, push or cleanup is implied. Lead owns final review treatment.

The old `q4is...` recorder build/CLI receipts do not validate changed source.
The existing admission image and frozen launcher embed that old binary. Hold
them; do not silently point them at a new build or claim new verifier/attachment
admission. The warning cause and first-hotplug orchestration remain unresolved
and outside this correction.
