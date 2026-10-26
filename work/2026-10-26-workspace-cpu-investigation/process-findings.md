# Live process measurements

Investigation only, 2026-10-26, implementer0. `dev-session current`,
`DEV_SESSION_SLUG` and `DEV_SESSION_WORKSPACE` agreed with the bound session
and `/home/aither/workspace/ai/vpsfree.cz` before session access. Required
workspace procedures, documentation skill, selected source AGENTS.md and
relevant README/portal documentation were read. No application, configuration,
service, package selection or lifecycle changes were made.

## Identity and method

The active user service main processes have parent PID 4239:

| PID | Service | Executable / role |
| --- | --- | --- |
| 2017250 | `workspace-portal@vpsfree-cz.service` | Selected package `bin/workspace-portal serve` |
| 2016996 | `workspace-router.service` | Selected package `bin/workspace-portal router` |
| 2017256 | `workspace-coordinator.service` | Ruby, selected package `libexec/.workspace-host-wrapped run-coordinator` |
| 1953671 | `workspace-codex-provider@vpsfree-cz.service` | Ruby, older package `run-provider-worker` |
| 435397 | `workspace-tmux@vpsfree-cz.service` | Ruby, older package `run-tmux` |

Selected package is
`/nix/store/vq113xqpwhz09sc7myd9zciyqvn1lsvv-dev-workspace-0.2.0`.
Ruby executable is
`/nix/store/5shv7ihqxa98r1psfz995q3j2cwk22sa-ruby-3.4.9/bin/ruby`.
Architect0 traced the selected package to derivation
`/nix/store/m723id7qwyfm1gq4mbbi65h11p83cxbk-dev-workspace-0.2.0.drv`,
whose `env.src` is
`/nix/store/xzh3s2660hw9p1klfh26ck93l9msjy3w-source`.
Provider worker package is `4cn1hh88xdpql5jp9pyrnf5fvnqsc829-dev-workspace-0.2.0`;
tmux worker package is `41mxyvi54bb6w1y5x959j184b6qlhlfi-dev-workspace-0.2.0`.
No conclusion about the correctness of these retained generations follows from
their age. All five user services reported `NRestarts=0`.

CPU uses deltas of `/proc/<pid>/stat` user+system ticks, divided by measured
monotonic elapsed time and `SC_CLK_TCK`. **100% means one CPU core**; the machine
reports 64 logical CPUs. Whole-service CPU uses matching cgroup v2 `cpu.stat`
`usage_usec` deltas, including short-lived descendants. This is interval CPU,
not `ps` lifetime `%CPU`. All times below are UTC.

Sampling read process/cgroup metadata only. Arguments were reduced to known
subcommand names; no environment, session conversation, request contents,
credentials, or foreign session records were inspected. There was no test
traffic or browser-state change, restart, kill, tracing, package download or
source build. Existing concurrent work continued, so this is a live workload
baseline, not an idle or controlled-tab benchmark.

## CPU, threads and process spawning

| Interval start / length | Portal self | Portal service total | Coordinator self | Coordinator service total | Router self |
| --- | ---: | ---: | ---: | ---: | ---: |
| 19:28:34.999 / 30.142 s | 88.91% | Not sampled | 69.14% | Not sampled | 1.33% |
| 19:30:46.622 / 30.017 s | 82.39% | 187.58% | 62.03% | 78.44% | 1.30% |

The second interval measured **2.66 cores combined** for portal and coordinator
services. Portal descendants account for roughly another core beyond its own
process. The first interval's reaped-child tick deltas were 120.73% for portal
and 17.98% for coordinator. Reaped-child accounting has exit-boundary effects
and must not be added to cgroup totals or treated as precise instantaneous
descendant CPU. An early report's “>3 cores” wording was imprecise; its
self+reaped arithmetic was 2.97 cores, while the second interval's cgroup
measurement is the more reliable complete-service figure.

In the first interval, older provider and tmux workers used 0.30% and 0.17%
self CPU respectively. A separate root-owned portal serve PID 1798541 from
package `0klh7dhca2dwyfwsz0m67pbjj2nml70d-dev-workspace-0.2.0` used 0.10% self
CPU; its unrelated scope was not investigated.

The second interval sampled the three user service cgroups every 200 ms:

| Owning service | Newly observed distinct PIDs / role | Lower-bound rate |
| --- | --- | ---: |
| Portal | 75 tmux clients, including 70 `display-message` | 2.50/s |
| Portal | 30 workspace-host processes/wrappers with `coordination status` | 1.00/s |
| Portal | 5 gh processes, including one observed `run list` | 0.17/s |
| Portal | 2 git and 3 dev-session processes/wrappers | 0.17/s |
| Coordinator | 18 workspace-portal helper processes | 0.60/s |

Portal total was at least 115 newly observed PIDs, 3.83/s. Short processes
between samples are missed. An exec can retain the same PID, so wrapper and
subcommand attribution is incomplete. These are process observations, not
request rates. Peak sampled portal cgroup process count was 8; coordinator 2.

A third interval, 19:32:07.065 for 20.066 s at 200 ms cadence, safely classified
**16 coordinator helper PIDs as `workspace-portal coordination-notify`**.
That includes any helper already present at the first sample; it is not an
exact launch count. No HTTP request counter or CPU stack profile was collected.
Implementer1 found no pprof handler in the selected source; ambient `perf` and
`pidstat` were absent. Existing `portal_read` timing diagnostics sample slow or
failed reads and cannot establish full request rate or CPU attribution.

Portal had 64 threads in both CPU samples; its hottest measured thread used
5.10% of one core in the second interval, with CPU distributed over many Go
threads. Coordinator had two threads; its main thread used 61.90%, accounting
for nearly all its 62.03% process CPU. Router had 28 threads. Read-only sampler
CPU overhead was 1.589% of one core for the second interval and 0.902% for the
third interval (excluding the third interval's later memory rollup reads).
The first sampler's own overhead was not measured.

## Memory and retained MCP processes

Portal RSS was 140,384 KiB at the second interval's end; coordinator 64,496 KiB;
router 21,772 KiB. Separate one-time `smaps_rollup` PSS readings were 142,514,
47,513 and 20,618 KiB respectively; the different timestamps and collection
methods matter when comparing these snapshots. All three reported zero swap.

At the third interval's end, portal cgroup `memory.current` was 2,152,513,536
bytes: about 253 MiB anonymous and 1,772 MiB file memory. Its approximately
2.00 GiB service memory is therefore mostly charged file cache, not a 2 GiB Go
process heap. Coordinator service was 134,156,288 bytes, about 54 MiB anonymous
and 65 MiB file memory. These cgroup categories and process RSS/PSS are different
views and should not be added together.

An initial inventory found 130 `workspace-portal team-mcp` processes; the third
interval found 131 at both boundaries, all with one common parent. That
20.066 s interval observed no MCP births/exits and 2.49% combined CPU for the
surviving MCP processes. They had 2,996 threads in total, summed RSS 1,409,564
KiB and summed PSS 1,081,818 KiB (about 1.03 GiB). PSS apportions shared pages;
RSS sums count them repeatedly. This is a sizable retained memory/thread
footprint, but the measured group is not the dominant CPU consumer. No leak or
incorrect ownership is established by this bounded observation.

Their executable is
`/nix/store/s4fbv3hya8l09jh4a67rd4brdkwx4piz-dev-workspace-0.2.0/bin/workspace-portal`;
their common parent is Codex PID 3387667 and their cgroup is
`workspace-codex@vpsfree-cz.service`. No per-session identities
or MCP payloads were read.

## Implications and useful follow-up tests

Measured priorities are portal work plus its helper children, then the
single-threaded coordinator loop. Repeated `coordination status`, tmux reads
and `coordination-notify` deserve source-level attribution. Caching/coalescing
status observations and avoiding unchanged notification work are hypotheses
for architect0/source owners to assess; these measurements do not prove which
source path dominates or authorize implementation.

Useful regression checks should count subprocess invocations and state/catalog
loads per fixed observation window under disposable fixtures, alongside CPU
and allocations. Include unchanged coordinator state, one real state change,
concurrent status readers, realistic retained-owner/session counts, and many
visible/hidden/disconnected browser clients. Preserve fresh authorization and
ownership validation when testing observation caches. Measure whole-service
CPU as well as process CPU so moving work into children cannot appear to be a
win. Establish controlled baseline/variance before choosing a numeric budget;
this live sample alone cannot supply a stable pass/fail threshold.

Raw compact summaries for intervals two and three are disposable local files
`/tmp/workspace-cpu-investigation-batch2.json` and
`/tmp/workspace-cpu-investigation-batch3.json`. No source tests were run because
this package makes no implementation change. Lead owns state/handoff synthesis.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-26-workspace-cpu-investigation/>
