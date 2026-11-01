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


## Read-only follow-up, 2026-10-27

User requested several minutes of observation and suggestions only. One passive
sample covered 08:03:36–08:08:36 UTC, 300.045 seconds, ten 30-second bins,
selected lm7x package unchanged. No product, settings, service, browser or package
changes, injected traffic, profiling, tests or benchmarks. Fresh Luna/low watcher
executed the single sample successfully. All 33 service boundaries were
active/running, successful, with zero restarts and stable main-process identities.

| Service | Mean main CPU | Mean whole-service CPU | Whole-service 30s range |
| --- | ---: | ---: | ---: |
| Portal | 80.818% | 177.537% | 118.475–241.758% |
| Coordinator | 35.835% | 42.885% | 32.786–52.481% |
| Router | 1.296% | 1.295% | 0.742–2.459% |

100% means one core. Portal helpers account for approximately 96.719 percentage
points, about 54.5% of its service CPU. First-bin 0.5s observations found at least
23 portal coordination-status wrapper PIDs and 19 tmux PIDs (18 classified as
display-message); these are lower bounds, not exact calls or CPU attribution.
144 reporting MCP processes stayed present and together used 1.720%; 38 native
Codex processes used 175.747%, separately from portal cgroup CPU. Native counters
cover surviving endpoint processes. A separate 310-second all-portal endpoint
comparison found the older root-scoped serve PID1798541 used 0.142%, making it a
minor CPU contributor; its ownership or retirement was not investigated.

Observation is uncontrolled live workload. No per-function CPU attribution or
causal savings claim. Sampler self overhead was 0.091% of one core, excluding
boundary systemctl child CPU. Raw temporary evidence:
/tmp/workspace-cpu-five-minutes.jsonl and
/tmp/workspace-cpu-all-portals-result.json; stderr empty.

Suggestions: prioritize recurring display-status/helper work and shared fresh
health observations; then combine overlapping fresh retry RPCs (three to two).
Preserve action-time authority, recovery detection and uncertainty handling.
Process count alone does not justify stopping the MCP helpers or older server.
No implementation or further observation is scheduled.


## Ten-minute read-only follow-up, 2026-10-28

User requested another sample after portal changes: observe ten minutes, then
recommendations only. Session identity matched from the tracking directory;
both DEV_SESSION environment markers were absent. No product, settings, service,
browser, package or lifecycle changes; no injected traffic, profiling, tests,
builds or benchmark runs. A fresh Luna/low watcher executed exactly one passive
sample, 08:18:02.778–08:28:02.940 UTC, 600.063 seconds, twenty 30-second bins.

Selected package: /nix/store/pq2jwjcv4hbyiwzcam50x6j9fv008qiq-dev-workspace-0.2.0.
Architect0 traced its derivation source to
/nix/store/l4y0gzsc3xc7s4x0kwd1jaj3pk5xl0wl-source and matched its NAR hash
sha256-iLRC4iVO7NpHcBdzupkwlmzKwDMFhxNcO3Nmmi+tD68= to runtime revision
d5d2b39b13a6875a26b218ffaf7b589b9d71a1fb. codex-web is
58300182763a01de7248ddf7c6cb9a4f0c6216cb. This identity is distinct from the
original deployment recorded above.

| Service | Mean main CPU | Mean whole-service CPU | Whole-service 30s range |
| --- | ---: | ---: | ---: |
| Portal | 66.935% | 171.307% | 121.964–226.493% |
| Coordinator | 36.305% | 43.475% | 35.673–54.520% |
| Router | 1.838% | 1.840% | 1.129–2.926% |

100% means one core. Portal helpers contribute approximately104.372 percentage
points, 60.9% of portal service CPU. Every interval exceeded1.21cores total;
this is sustained load, with variation. All63service boundaries were healthy,
active/running, Resultsuccess, NRestarts0; main PID/start identities stable.
Portal PID629079 RSS varied97260–106080KiB; this sample cannot establish a leak.

First30seconds at0.5s cadence observed at least35tmux display-message PIDs,
one other tmux PID,31coordination/status wrapper PIDs,22GitHub CLI PIDs,
6devcluster PIDs and smaller jq/git/readlink groups. These are lower bounds,
miss short-lived/exec stages and do not assign CPU to a command family.
Two actual serve processes persisted: current66.933% endpoint CPU and older
root-scoped1798541 at0.143%. Reporting MCP endpoint count rose36to44; the36
survivors used0.542% combined, excluding CPU of8new processes. NativeCodex
count19to20; survivors138.130%, separate from portal service CPU and not
attributable solely to the portal. No process was stopped or ownership inferred
from age/count. Sampler self0.344734CPU-s,0.05745%core, excluding boundary
systemctl helper overhead. Exit0, stderrempty, no discontinuities.

Compared with Oct27, observed main portal CPU80.818->66.935% and service
177.537->171.307%; workloads, package and other native activity differ. This is
not a controlled regression/speedup claim. The prior fixture excluded real
native/activity/browser costs and remains a separate exact-source experiment.

Current-source suggestions, not implementation or measured savings estimates:

1. Share display-only repository/cluster refreshes for matching identity/scopes.
   Visible details refresh every15s and enriches repository/cluster status even
   when those panels are unselected. Repository TTL5s(active)/60s(archived)
   lacks miss coalescing; cluster display inspection has no TTL/singleflight.
   On-demand or slower remote enrichment would be an explicit freshness choice.
   Preserve exact-head CI identity, unavailable warnings and fresh action checks.
2. Reduce coordination display helper repetition. Existing2s same-key cache
   cannot reuse isolated5s polls; coalesce eligible consumers and minimize each
   helper's validated projection work. Longer reuse changes freshness unless
   independently validated by current authoritative change identity.
3. Share concurrent read-only recovery/display health observations at the exact
   authority/socket/package identity, preserving5s recovery detection and fresh
   pre/post-lock action checks. Current recovery checks health before backoff;
   preserve that correction and uncertainty handling.
4. Combine overlapping retry identity/latest-turn reads: still3freshRPCs per
   successful unchanged probe, with a possible2RPC combined flow. Metadata is
   already selected as metadata-only; do not claim full-history fetching.

Source-cost hypotheses are not function-level CPU attribution. No MCP cleanup,
blind polling slowdown, broad cache/catalog redesign or implementation was run.
Raw temporary evidence: /tmp/workspace-cpu-ten-minutes.jsonl,
/tmp/workspace-cpu-ten-minutes-summary.json and watcher final/log files.
