# Aged-scale v5: unchanged published wakeup counter during predecessor aging

Run [40133879811](https://github.com/vpsfreecz/vpsadminos/actions/runs/40133879811),
attempt1, head `75836892e5d446d7c1f76411654a4c1809ceb3a0`,
job [120996309853](https://github.com/vpsfreecz/vpsadminos/actions/runs/40133879811/job/120996309853),
`Livepatch lifecycle (amd-scale-aged-v5)`. API metadata matched those identities
before artifact download. The failing script is
`kernel/livepatch-qualification@amd-scale-aged-v5`; artifact directory suffix
`cb9686d6`. `test-result.txt` is `unexpected_failure`; test-runner.log:6-9 records
one failed example with assertion message `wakeups`.

The exact failure is the second predecessor-aging progress comparison, before
the first pre-transition CPU hotplug or corrected-patch activation. It did not
reach the four-hour age target. Predecessor `livepatch_5` had already completed
activation and remained enabled with transition0 in the failure diagnostics
(machine-shell1.log:1159-1160). No CPU online writes or corrected module insertion
were reached. Do not classify this as the prior hotplug warning, transition,
cleanup or separate prebuild HTTP429 failure.

## Retained values and failing assertion

| Snapshot (machine-shell.log output line) | elapsed | wakeups | fork_exec |
| --- | --- | --- | --- |
| initial population,5808 | 89.050 | 35 | 1 |
| first aging read,6299 | 126.735 | 128 | 2 |
| second aging read,6906 | 166.928 | 128 | 3 |

Each snapshot reports state=running, tasks100000, ready99999, CPUs128. Between
the last two snapshots all256 per-CPU progress/perf fields advanced and fork_exec
advanced; `wakeups` alone failed the strict progress predicate (128 is not >128).
This is a new publication with a lagging field, not a wholly unchanged snapshot.
Structured comparison and complete values are retained in snapshot-comparison.json
and the original shell log. No estimate from artifact filesystem times is used.
The first complete age iteration printed age116.6542077580234s in test-runner.log;
that is the qualification clock, distinct from population elapsed.

Exact-head source was read through the official GitHub contents API, not a
mutable working tree. [qualification.rb:73-76](https://github.com/vpsfreecz/vpsadminos/blob/75836892e5d446d7c1f76411654a4c1809ceb3a0/tests/suite/kernel/livepatch-6.12.95/qualification.rb#L73)
requires every selected counter strictly greater. Its aging loop at475-477 sleeps
60 host seconds, reads once, then immediately asserts. The first hotplug call is
after that loop at497, so the phase is unambiguous. Earlier failed population-file
reads are ordinary readiness polling; the population eventually reached its
required count. The later NFS flock status1 is the expected held-lock assertion
and not the example's failing operation.

## Producer semantics and what the evidence proves

[task_population.c:143-148](https://github.com/vpsfreecz/vpsadminos/blob/75836892e5d446d7c1f76411654a4c1809ceb3a0/tests/suite/kernel/livepatch-6.12.95/task_population.c#L143)
increments wakeups when a sleeper returns from its futex wait. The controller
serializes each fork/exec, polls its pidfd and waits for successful child exit
before incrementing fork_exec (lines367-424). Then it increments one cohort's
sequence, requests a bounded FUTEX_WAKE and immediately publishes all counters
(lines427-431). It does not wait for those awakened workers to run/increment
wakeups before publication. No publication happens while the controller waits
for its next fork/exec child. Therefore a newer elapsed/fork_exec value does not
guarantee a newer published wakeup count, even if the assertion reads much later.

The failure-time diagnostic captures controller30425 with100000 threads, sleeping
in do_sys_poll (machine-shell1.log:41-124), and its child137475 running with one
thread and4KiB VmSize (lines126-180). It supports slow or outstanding serialized
fork/exec at that snapshot, which prevents another publication. The child's
syscall/stack contents are empty; its precise kernel path/cause is not established.
It does not prove a permanently stuck controller, failed futex wake, starvation,
OOM, or v5 kernel defect. No relevant BUG/WARNING/softlockup/RCU-stall/OOM/bad-RSS
signature was found in the retained console/dmesg diagnostics. This limited log
observation is not a complete kernel-health or eventual-progress proof.

The test already documents and handles the same publication ordering in
[qualification_wait_for_progress:79-96](https://github.com/vpsfreecz/vpsadminos/blob/75836892e5d446d7c1f76411654a4c1809ceb3a0/tests/suite/kernel/livepatch-6.12.95/qualification.rb#L79):
wait, with a60s bound, for elapsed AND every counter needed by the hard assertion.
The aging call bypasses that helper. The evidence establishes an invalid
single-publication progress assumption in the test; it leaves unresolved whether
a bounded all-counter wait would pass on this exact run or expose true ongoing
lack of progress. Do not infer harmlessness, frequency, or guaranteed recovery.

## Minimal next step for architect/lead selection

Consider a source-only correction confined to the aging observation in
qualification.rb and its focused helper spec: use the existing bounded all-counter
wait before obtaining/strictly checking the aging snapshot. Preserve strict
wakeups/fork_exec/all per-CPU progress/perf checks, CPU identity/task count, age,
network/NFS/TUN/health and failure/cleanup contracts. Do not drop wakeups, accept
equality, lengthen timeouts automatically or patch the kernel from this evidence.
A focused fake-snapshot check should show a newer elapsed/fork count with equal
wakeups stays pending, later genuine all-counter advancement passes, and a counter
that never advances still times out/fails. Any extra per-iteration waiting and
its existing60s bound need explicit design acceptance. No change is implemented
or test selected by this recommendation. If that wait expires in later authorized
verification, preserve the producer/child diagnostics as a real liveness failure;
no blind rerun or broader kernel campaign follows.

## Bounds, provenance and retained evidence

Only artifact12579606773, `os-test-logs-40133879811-1-livepatch-amd-scale-aged-v5`,
was downloaded:193054 bytes, SHA256
4a739815ac324a9445063557e59ece7d93712c37546496019745fb47f5bc7c5a,
matching the API digest.14 text/log members total1209800 uncompressed bytes;
download+unpack1402854 bytes, below128MiB; logs/text below16MiB. No images or
other artifact was downloaded. Three small exact-head named sources were read
separately. Raw run/job/artifact metadata, member sizes, extraction hashes and
all retained file hashes are in evidence.json/extraction.json. No live process,
cache/capacity query, source probe, VM/rerun/build, application/Git/ref edit,
workflow/cancellation, push/merge or cleanup occurred. No historical failure
from another version is used as proof of this one.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-ci-failure-analysis/
