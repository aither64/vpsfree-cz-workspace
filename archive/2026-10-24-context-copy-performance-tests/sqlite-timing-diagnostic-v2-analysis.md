# V2 diagnostic completed; quick remains blocking

The renewed exact direct command ran once, exit0 in28.135934s. All six workers
completed in B0,B1,B2,C0,C1,B3 order. Independent pure-JSON validation confirms
18batches/288responses,32ordered fully typed rows per response, exact raw bytes
and canonical digests, and3queries/65authorizations/1execution for EVERY operation.
All six loaded84gem graphs/RubyABI/runtimepolicy, selected source bytes and
resolved inputs match. Exact io-console0.9.4 activation is recorded for parent
and each worker. All28frozen files and772/793exported blobs remain unchanged;
HEAD38e/treec6cf3c68 and index are clean. There is no performance gate classification.

| Observed worker | Wall ms/op | CPU ms/op | Objects/op | GC ms/batch |
| --- | ---: | ---: | ---: | ---: |
| B0 | 18.449 | 18.440 | 11255.0625 | 11.154 |
| B1 | 20.754 | 20.749 | 11255.0625 | 10.735 |
| B2 | 18.982 | 18.964 | 11255.0625 | 11.382 |
| C0 | 19.064 | 19.041 | 11275.0625 | 10.374 |
| C1 | 20.035 | 20.034 | 11275.0625 | 12.147 |
| B3 | 19.243 | 19.193 | 11255.0625 | 11.230 |

All observed batches have exactly1minor GC,0major GC and unchanged heap-page
counts. GC time recording was already enabled and stayed enabled. B1 vs B0
same-source CPU rises36.942ms/batch while recordedGC falls0.418ms. That local
difference is not explained by measuredGCtime. First warmups allocate more and
have2minor collections with~51–57msGC; the original two-warmup contract is intact.

Observed scheduler wait is0.0175–0.8046ms/batch and wall-minus-CPU is
0.0137–0.8011ms/batch against~295–332msCPU. Observed minorfaults0–1/majorfaults0,
with matching pre/post CPU placement (intermediate migration is unobserved). This does not support pure waiting/faults as
the dominant local mechanism. CPU throughput/cache/heap variation remains
compatible with same-source variation, but no frequency or host fault is proven.
Recorded logical CPU IDs differ across workers; this establishes no physical core topology. Frequency snapshots and leaf cgroup
quota/weight/cpuset files are unavailable with explicitENOENT reasons. Readable
shared cpu.stat lacks throttling fields; missing counters do not exclude throttling
or establish unlimited CPU.

Outside-timer snapshot portions are~0.68–1.15ms before and~0.52–0.83ms after.
They still perturb heap/cache state. Observed baseline/candidate allocations
11255.0625/11275.0625 are retained without calling the20object difference a defect.
Earlier hosted full-profile11265.0625 results used different history and host.

This host is aitherdev/EPYC7551/Linux6.18.34; original hosted quick used
EPYC7763/AzureLinux. Explicit console preload and omitted earlier profile cases
also change startup/history. The direct launcher binds declared runtime fields,
not every inherited environment variable. It executed no Nix command/build.
This single local experiment cannot establish original-host causality, waive
quick's7/9agreement, or authorize another required campaign.

The watcher initially captured PGID4046708 before GNUtimeout established its own
group and treated the reaped PID's absence as uncertainty. Original probe parent
and all six child witnesses consistently show actualPGID4046710; all children
were waited/reaped with exit0. Independent scans of BOTH groups found no members
or own-UID observation errors. [Parent reconciliation](sqlite-timing-diagnostic-v2-parent-drain.json)
retains the raw watcher uncertainty and resolves it. Utility slot released; no
operation remains. No signals/timeout/retry occurred. Earlier no-launch history
is preserved; actual v2 execution count1, local paired campaign count0.

[Structured analysis](sqlite-timing-diagnostic-v2-analysis.json),
[all18batch telemetry](sqlite-timing-diagnostic-v2-telemetry-rows.json),
[independent response validation](sqlite-timing-diagnostic-v2-validation.json),
[raw watcher receipt](sqlite-timing-diagnostic-v2-watcher-result-run2.json) and
[complete log](sqlite-timing-diagnostic-v2-once-run2.log) retain the evidence.
The original required quick remains blocking; weekly remains accepted. No
application remedy or unchanged required-campaign rerun follows from this probe.
