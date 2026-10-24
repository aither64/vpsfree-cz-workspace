# Warm prebuild benchmark interpretation

20 October 2026. Read-only interpretation of benchmark run `39305352549`,
following [the accepted brief](performance-plan.md). Product revision:
`a2ccd72d08dc67f678d7f115a92ed5eeca50c1a1`; isolated benchmark harness:
`295b814ad3aadca80ee10c043327c4676d71913c`.

The completed pair is useful as a **qualified exploratory warm-cache
comparison**. Prebuild took 217.50 seconds longer overall, an observed increase
of 1.77%. This does not establish a causal regression of that size or performance
equivalence. No rerun or additional acceptance gate is required to report the
observation with its qualifications.

## Observed timings

Source: [timings.json](benchmark-ci-39305352549/artifact/prebuild-benchmark-39305352549-1/timings.json).
Whole-command times use the harness's monotonic clock around the complete CLI,
including cleanup; phase markers use log receipt times.

| Measurement | A: `--no-prebuild` | B: `--prebuild` |
| --- | ---: | ---: |
| Whole CLI wall time | 12,297.60 s (3h24m57.60s) | 12,515.11 s (3h28m35.11s) |
| CLI prefix before executor | 66.51 s | 1,656.56 s |
| Global preparation, within prefix | Not a separate phase | 1,571.26 s |
| Executor-reported span | 12,231.06 s | 10,858.52 s |
| Tail after summary receipt | 0.027 s | 0.022 s |

The exact wall difference is `217.5035916500201` seconds, or
`1.7686667310522042%`. Warmup was separate: `3369.9232990579912` seconds.

B's 26m11.26s preparation interval includes aggregate evaluation and build
checks; neither measured leg recorded image builds, so it is not compression
time. A performs per-test evaluation/preparation inside its executor span,
overlapping VMs. B's executor span was 1,372.54 seconds shorter, while its prefix
was 1,590.05 seconds longer. Those changes account for the roughly 217.50-second
net increase. Comparing only the executor spans would incorrectly describe the
result as a runtime speedup. Receipt precision and buffering mean phase sums
need not exactly equal whole-command wall time.

## Matching work and the capacity qualification

Both legs completed 127 tests/335 scripts with exit status 0. Selection digests,
all 127 test outcomes, and retry records match. Both contain the same
`driver/rspec#script-attempts` retry to attempt 2. Neither recorded unexpected
outcomes, kernel failures, image builds, resource-limit updates, forced cleanup,
or remaining owned processes. The sampled runner cgroup OOM delta was zero in
both legs.

The harness's comparison predicate at
`.github/workflows/scripts/prebuild_benchmark.rb:70–82` in the harness revision
above was checked against the artifact. **The only failing condition is equality
of `initial_resource_limits`: A has 89.4 GiB memory, B 90.4 GiB.** The generic
`comparable_work=false` qualification does not indicate unequal test work or
failures here.

The full before snapshots agree on runner `gh-runner3`, machine identity,
48 available CPUs, 100 GiB assigned memory, affinity, Nix settings
(`max-jobs=48`, `cores=0`), and relevant environment. Runtime CPU capacity remains
72 and shared-memory capacity 367.1 GiB. Before-leg available memory was
99,751 MiB for A and 100,746 MiB for B; the runner takes its own slightly later
snapshot and subtracts the unchanged 8 GiB reserve.
See [A.log](benchmark-ci-39305352549/artifact/prebuild-benchmark-39305352549-1/A.log)
lines 338–340 and
[B.log](benchmark-ci-39305352549/artifact/prebuild-benchmark-39305352549-1/B.log)
lines 338–343. B selected 11 preparation jobs.

The extra approximately 1 GiB could affect admission. The evidence does not
establish whether it did, and no numerical correction is justified. Before
snapshots also differ in observation time, cumulative CPU counters and available
disk bytes (about 287.0 versus 286.7 GiB); these are not additional failed
comparison predicates. Memory/CPU/I/O pressure readings and physical-host ID
are unavailable, so this does not prove absence of neighboring load.

This single sequential A/B pair also retains random test order, filesystem
cache, thermal and guest-network variation. It supports reporting a modest
observed whole-suite increase on this runner with warm closures. It does not
measure cold build/VM overlap, compare the old compressor-cache default, or
establish arbitrary-build memory safety. Both flags used the same product
revision and its test-image cache policy.
