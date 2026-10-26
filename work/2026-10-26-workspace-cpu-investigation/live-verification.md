# Live deployment verification

Implementer0 owns read-only pre/post measurements. Lead owns deployment,
machine reservations, exact rollout receipts and integration. No deployment or
machine ownership is implied by these measurements.

## Pre-deployment baseline

Bound session/current/environment reverified before sampling. Exactly one fresh
measurement was taken from `2026-10-26T20:29:00.259422Z` to
`2026-10-26T20:29:30.264522Z`, monotonic duration **30.005000 s**.

Main CPU uses `/proc/<pid>/stat` user+system tick deltas and `SC_CLK_TCK`;
service CPU uses corresponding cgroup v2 `cpu.stat usage_usec` deltas, including
all descendants. **100% = one CPU core**, on this 64-logical-CPU host. Two
boundary snapshots, no ongoing process polling or command-count collection.

| Service | Main PID | Main CPU | Whole-service CPU | End RSS KiB | Threads |
| --- | ---: | ---: | ---: | ---: | ---: |
| `workspace-portal@vpsfree-cz.service` | 2017250 | 87.152% | 215.300% | 151696 | 66 |
| `workspace-coordinator.service` | 2017256 | 72.288% | 88.012% | 58552 | 2 |
| `workspace-router.service` | 2016996 | 1.133% | 1.132% | 21164 | 30 |

Portal plus coordinator total: **3.03312 CPU cores**. Router is listed separately.
End cgroup `memory.current` snapshots were 840806400, 117161984 and 15507456
bytes respectively; these include charged cache and are distinct from process RSS.

Portal/router executable remained
`/nix/store/vq113xqpwhz09sc7myd9zciyqvn1lsvv-dev-workspace-0.2.0/bin/workspace-portal`.
Coordinator executable remained
`/nix/store/5shv7ihqxa98r1psfz995q3j2cwk22sa-ruby-3.4.9/bin/ruby`.
Selected runtime source association is the already established
`7e6d7c9cdb3388ab7abc720c034c15c21afbd686`, immutable source
`/nix/store/xzh3s2660hw9p1klfh26ck93l9msjy3w-source`; see
[original identity evidence](process-findings.md).

Cgroup paths retain the existing user service layout under
`/user.slice/user-1000.slice/user@1000.service/app.slice/`:
`app-workspace\x2dportal.slice/workspace-portal@vpsfree-cz.service`,
`workspace-coordinator.service` and `workspace-router.service` respectively.
No process start identity changed between sample boundaries. All three units
reported `active/running`, `Result=success`, `NRestarts=0` both before and after.
Portal/coordinator start timestamps remained 2026-10-26 19:54:32 CET; router
19:54:08 CET. This tool/report exchange confirms this member conversation could
continue during the baseline; it does not prove all browser/native workflows.

Sampler consumed **0.004647 CPU seconds**, **0.015487% of one core** over the
interval, measured with Python `resource.getrusage(RUSAGE_SELF)`. This excludes
the two boundary `systemctl --user show` health commands outside the interval.
There was no source test, synthetic traffic, profiling, tracing, browser/service
change or foreign-session content access. Existing workspace/team activity
continued; tab counts and native workload were not controlled. A later sample
can show observed change, but cannot establish a causal equal-workload speedup.

Compact raw summary is disposable local
`/tmp/workspace-cpu-investigation-pre-deploy.json`.

## Post-deployment measurement

The lead subsequently reported that another session selected application package
`vky6fqna...` and system `njn47...` during this campaign. The 20:29 measurement
above remains a historical observation of `vq113...`, rather than an immediate
baseline for our eventual deployment. Any pre/post comparison is therefore
uncontrolled with a changed intervening baseline, as well as an uncontrolled
workload. Exact intermediate paths and source lineage remain with the lead's
rollout records; these abbreviated identifiers are only the relayed context.

After the lead's explicit deployment-verified signal, exactly one sample used
the identical three-service boundary-delta method from
`2026-10-26T22:59:45.647024Z` to `2026-10-26T23:00:15.652289Z`, monotonic duration
**30.005083 s**. Session/current/environment matched the bound session first.

| Service | Main PID | Main CPU | Whole-service CPU | End RSS KiB | Threads |
| --- | ---: | ---: | ---: | ---: | ---: |
| `workspace-portal@vpsfree-cz.service` | 2667180 | 134.810% | 153.122% | 90232 | 46 |
| `workspace-coordinator.service` | 2667188 | 41.826% | 50.830% | 63100 | 5 |
| `workspace-router.service` | 2667124 | 0.233% | 0.211% | 21100 | 22 |

Portal plus coordinator total: **2.03952 CPU cores**, versus the historical
20:29 observation of 3.03312 cores. The observed whole-service total is lower,
while portal main-process CPU is higher. The intervening package deployment and
uncontrolled live workload prevent attributing these changes precisely to this
optimization. Controlled fixture comparisons belong to the separate benchmark
evidence; this single live sample is deployment observation only.

Portal/router executable is
`/nix/store/lm7xpfxxzr2012y80wq2fnvirlyfakzz-dev-workspace-0.2.0/bin/workspace-portal`,
matching the lead's expected deployed package. Coordinator Ruby executable is
unchanged. Lead relayed final system `lk9lkpcn...`, generation
`2026-10-26--23-38-24`, with runtime `fff...`, workspace `718b...` and configuration
`530e...`; exact source/input and system paths remain in the lead's rollout
receipt. All three measured units were `active/running`, `Result=success`,
`NRestarts=0` at both boundaries. Their PIDs and `/proc` start identities remained
stable. Portal/coordinator start timestamps were 2026-10-26 23:58:38 CET, router
23:58:37 CET. No unit restart occurred during this sample.

End service `memory.current` was 285806592, 67420160 and 10952704 bytes respectively,
distinct from RSS and including cache. Sampler CPU was **0.005020 s**,
**0.016730% of one core**, excluding the two boundary systemctl health commands,
as in the baseline. No command counts, profiling, additional checks, traffic or
source/service/browser changes were introduced.

The lead separately verified deployment driver exit zero, two confctl health
checks, all five services active and portal `/healthz` OK. The lead also compared
pre/post native Codex/tmux PIDs, start times, restart counters and application/tmux
socket device/inode/ctime identities and reported them unchanged. This member's
conversation and tool exchange continued through the sample. These relayed
continuity checks are distinguished from the three-service metadata measured
here; no other sessions' contents were accessed.

Compact raw summary is disposable local
`/tmp/workspace-cpu-investigation-post-deploy.json`. This completes the assigned
single post-deployment CPU/health observation; no further sampling is scheduled.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-26-workspace-cpu-investigation/>
