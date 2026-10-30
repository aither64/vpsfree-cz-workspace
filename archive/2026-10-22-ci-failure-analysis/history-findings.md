# Historical recurrence and independent test utility

The fixed historical sample confirms prior occurrence of the impermanent-root
API mismatch and AMD CPU-hotplug warning. It does not establish harmlessness,
flakiness or exclusion of a current interaction. Keep all three test families;
revise their evidence and phase diagnostics. No removal is justified by this
sample or the supported-transition contracts.

## Sampling and provenance

Before classification, selected the latest 15 **completed workflow runs**
created before `2026-10-22T11:03:56Z`, the creation time of current run
`39767770407`. GitHub's completed state includes cancelled runs. The immutable
[selection lock](evidence/history/sample-lock.json) records all IDs and the
[rule](evidence/history/sampling-rule.md); the window is October 19
15:18:40Z–October 22 10:35:03Z. It includes staging, feature branches and three
benchmark dispatches. Current-run details came only from the authorized
source-session handoff; no individual current-run API/log/artifact retrieval,
watcher or rerun occurred.

[recurrence.tsv](recurrence.tsv) contains 111 run/attempt/job/test observations.
Every sampled run is attempt 1. Benchmark `39305352549` has two native
experimental legs, A without prebuild and B with prebuild: these remain one run
and one tested product head, `a2ccd72d08dc67f678d7f115a92ed5eeca50c1a1`, rather
than workflow head `295b814ad3aadca80ee10c043327c4676d71913c`. The other two
benchmark runs also select that product head but fail before test execution.
The 15 workflow runs represent 14 workflow heads and 12 tested product heads;
repeat staging/feature runs at `49636f90` are not independent source revisions.

All 30 job/artifact metadata requests succeeded. Sixteen artifact ZIPs total
33,247,370 bytes; the seed native ZIP is reused read-only from the source
session, with SHA256
`85eadc310707dc36ffc4f1c662214172a1abf857fed9aef317d0176a7dab30fa`
and all 950 members verified. Fifteen ZIPs were downloaded once. Four additional
job logs establish successful native execution or benchmark setup/leg outcomes.
The [artifact index](evidence/history/artifact-index.tsv) links run/attempt/
artifact IDs, retrieval time, bytes and SHA256; adjacent receipts preserve API
URLs, retention expiry and errors. ZIPs retain complete artifacts; extracted
views contain relevant cases, suite logs and selected prebuild logs. No
expiration or download failure limited this sample. Conditional native upload
explains the absent ZIP for successful job `118493907810`; its downloaded
per-test log proves execution. Metadata alone is never counted as a test pass.

## Denominators and observations

Here **eligible** means the sampled workflow's selected native product suite
includes the case, even if setup/cancellation prevents execution; AMD excludes
three benchmark-only workflows. **Started** requires a native script start or
per-test completion proof. **Available outcome** requires a native result,
first script exception or explicit per-test success in the job log. **Phase**
means the dataset assertion, Podman readiness/upgrade path, or first AMD
hotplug was reached. Counts below are unique runs, not observations.

| Case | Eligible | Started | Available outcome | Phase reached | Pass | Exact signature | Other failure |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 6.12-guests | 15 | 8 | 8 | 8 | 5 | 3 | 0 |
| 6.12-guests-v1 | 15 | 8 | 8 | 8 | 5 | 3 | 0 |
| 6.12-inherited-guests | 15 | 7 | 7 | 7 | 4 | 3 | 0 |
| 6.18-guests | 15 | 8 | 8 | 6 | 4 | 2 | 2 |
| 6.18-guests-v1 | 15 | 7 | 7 | 6 | 3 | 3 | 1 |
| 6.18-nested-podman | 15 | 7 | 7 | 7 | 7 | 0 | 0 |
| AMD scale-aged-v6 | 12 | 7 | 5 | 4 | 3 | 1 | 1 |

Dataset family totals: 8/15 runs start at least one case, all 8 supply an
outcome; 43 case outcomes comprise 26 passes, 14 exact mismatches and three
other first errors. The extra benchmark leg accounts for five of those passes.
Podman has eight pass observations in seven runs. AMD has five completed
outcomes: three passes, one exact warning and one early progress failure. Its
two further started executions were cancelled without reaching hotplug; five
other eligible runs were cancelled before execution. The fixed sample therefore
cannot supply ten executions per family. Lead accepted this limit without
expansion. [Machine-readable counts](evidence/history/counts.json) preserve
observation and run totals separately.

`39745935323` native preparation failed downloading source archives with HTTP429;
zero selected native VMs ran. `39759039117` and `39764186292` native jobs were
cancelled during preparation. They are coverage exclusions. Their AMD status
must be assessed separately: two AMD cases started and were cancelled without
terminal results. Benchmark `39276852536` stops on setup `NoMethodError`;
`39296042103` completes warmup but leg A cannot start because geminabox is
missing. These are unexecuted, not negative signature observations.

### Impermanent dataset recurrence

Seed `39600028637` / `b81c43ff` and staging `39414347376` / `49636f90` each
have all five exact mismatches. Feature run `39413777406`, also at `49636f90`,
has four: `6.18-guests` fails earlier because nixold readiness is degraded with
failed firewall.service. This explains **14 matches in three runs, two heads**,
not five matches in every run. Each exact match follows successful first
userspace activation and reports the base dataset instead of the saved
`impermanence-*` temporary dataset. Native logs, shell traces and IDs are linked per row.

Older `39309610523`, `39358414083`, `39381114351`, benchmark A/B and two cases
in cancelled `39396698293` provide passes. However, lane0's exact source check
shows these targets contain `adopt_run_conf`/`adopt_live_root`; failing targets
follow unsafe-adoption revert `2abbe3cc1c102a4b39022d3f73ef4a432ad4d616`.
Actual benchmark product `a2ccd72d` also has adoption. The target recovery
implementation therefore differs. Passes can mask stale persisted metadata and
are not an equivalent baseline disproving the old writer defect. The inspected
upgrade common fixture and predecessor pins are unchanged across sample heads
([source hashes](evidence/history/source-identities.json)); that source
continuity does not imply equivalent recovery or runtime state.

Two other first errors mask the assertion: `39309610523` 6.18-v1 fails nmguest
readiness; `39396698293` 6.18-guests records nixold degraded readiness before
workflow cancellation, with no terminal test-result file. It remains a proven
other first error. Two completed 6.12 passes in that cancelled run remain valid
per-test passes. No raw pre/post runtime YAML or actual mount-source capture is
available to distinguish API fallback from a real root/data change.

### Podman recurrence

All seven historically executed runs pass the complete named test, including
staging `39414347376` and seed `39600028637`. There is no exact historical
DHCP-seccomp chain in this bounded sample. This is not a measured zero failure
rate for the current image: historical passes use Debian `latest`, install
trixie Podman `5.4.2+ds1-2+b2`, and lack image timestamp/archive digest,
`/etc/os-release`, dhcpcd-base version and effective policy. The current
preserved failure is specifically Debian13.7/dhcpcd10.1.0 with sandbox denial,
failed ifup, missing IPv4/default route and a readiness timeout before any
Podman installation or target activation. There is no same-image controlled
historical comparison and no package introducer is established.

### AMD recurrence

`39309610523` / `3ae196d60b2811e52cbb75a204108df629dca42d`, job
`118261936621`, has the exact warning during first CPU127 offline under v6,
before corrected v7 insertion. Console lines149/188–189 record the warning,
two enqueued entities and only `migration/127`; shell99483/100541/102074 order
first hotplug, insertion and second hotplug. Activation later succeeds in
780.880s. Lane2 verified the same predecessor module checksum and envelope.
No second task identity is established: runnable accounting can also include a
fair-server scheduler entity. A callback/task owner remains unresolved.

Three native expected-success results are retained for `39600028637`,
`39413777406` and `39381114351`, including successful hotplug and later
qualification phases. Staging `39414347376` instead fails a `wakeups` progress
check after 293.06s, before hotplug; it supplies no negative hotplug observation.
The two runs on `49636f90` thus have distinct qualification outcomes/phases.
Only four historical runs expose the first hotplug. The exact warning recurs
without the current generic sysctl service, but that does not exclude a current
interaction. The failure's post-transition health check prevents later
v7 disable/removal phases from executing; successful activation is
not a completed qualification or recovery result.

## Independent utility assessment

These conclusions follow the exact target test and documented contracts,
then reconcile with the causal owners; they do not depend on adopting a causal
verdict. No unresolved disposition disagreement remains.

| Family | Protected user behavior and actual measurement | Unique value and limits | Cost and disposition |
| --- | --- | --- | --- |
| Impermanent upgrades | Running system containers, process birth identities, persistent/ephemeral payloads and root identity must survive daemon/userspace activation. `common.nix:1152–1172,1528–1542` checks initial temporary dataset, saved API dataset, init birth, then both markers. | Fresh-boot tests do not exercise an old writer with a new daemon; cgroup v1/v2 and inherited cases protect different supported paths. The dataset assertion is valid observability/state consistency. Because it fails before marker reads, a mismatch does not prove actual data loss or successful continuity. | Native script passes take 24–127min per case; whole-test log passes take 30–115min and include runner preparation/cleanup. These are different duration kinds, not a pooled runtime estimate. Fourteen failures reach their first exception at 354–1799s. **Keep; revise** with a focused root-persistence regression and independent mount/marker capture at failure. Do not restore the unsafe prefix scan or weaken equality. |
| Nested Podman upgrade | Old OS must start a networked Debian system container, install/run Podman, preserve nested workload ID/PID/data through target activation, then create a working new nested workload (`common.nix:1234–1273,2288–2294`). | Fresh Podman tests cannot prove old-to-new continuity. The nested app uses `--network none`; outer DHCP/DNS/image/apt/registry setup adds substantial external dependencies and can prevent any Podman/upgrade exercise. Current readiness assertion protects a real prerequisite but obscures its first failing layer. | Five native script passes take 42.5–60.7min (median 43.8min); three whole-test log passes take 53.3–71.8min, including runner preparation/cleanup. Current failure spends 900s on readiness within a 1237.2s script. **Keep; revise** layered address/route/DNS/service diagnostics, immediate capture of permanent service failure, and reproducible image/package identity. Preserve supported-image breadth separately from a reproducible upgrade fixture. |
| AMD aged-scale v6 | Exact frozen kernel/module lineage must preserve workload progress and kernel health across four hours, 100000 tasks, 128 guest CPUs, two hotplugs and bounded transition; callback/loss counters, data witnesses and later migration/unload are asserted. | Small/fresh/v5/Intel profiles do not cover this old-v6 aged-scale boundary. Successful sysfs writes cannot prove scheduler teardown safety; the final WARN assertion measures an independent real invariant. It detects the warning but delays localization until after activation/migration. | Three passes take 4.66–4.78h of script runtime, plus preparation; 16GiB and 128 guest vCPUs, not 128 physical CPUs. One early wakeups failure prevents qualification. **Keep; revise** phase-local health snapshots and bounded hotplug/entity evidence. Do not drop hotplug, WARN matching, age/task envelope or add blind retries. |

The main maintenance costs are old-writer compatibility, evolving guest images
and external package/registry services, plus the frozen livepatch ABI/toolchain
and long stress fixture. The sample demonstrates mixed source recovery,
setup failures, cancellation and one competing progress error. It cannot
estimate a flake rate, show assertions are redundant or prove an unsupported
transition; removal lacks evidence. Retirement should follow the explicit
supported-version/case rule in `docs/os/testing.md`, not CI redness.

## Priorities and smallest next evidence

1. **Impermanent-state consistency:** retain lane0's source-proven old-writer
   write-order defect and unsafe-adoption boundary as the repair constraints.
   Propose one representative 6.12-guests diagnostic through the first switch:
   raw runtime YAML bytes/file identity, exported JSON, PID+birth, mountinfo and
   root/ZFS identity, plus persistent/ephemeral markers before/after. Timestamp
   current sysctl service output/stamps/check/value readbacks if attribution to
   that service is considered. A repair needs old writer/new reader and downgrade
   compatibility, one-/multi-package CPU paths, all five cases and graceful/
   abrupt daemon-restart and cleanup checks. Restore neither guessed roots nor
   live-root deletion. Runtime capture is still needed; no diagnostic was run.
2. **Podman prerequisite:** one exact predecessor/image case stopping before
   package installation/activation, recording image/package hashes, effective
   LXC/seccomp policy, credentials and bounded trace of the denied sandbox
   syscall/arguments/errno. This separates client/package behavior from outer
   policy. Regression acceptance must restore supported guest readiness,
   preserve confinement and then prove nested ID/PID/data continuity and a new
   workload after activation. DNS changes or disabled seccomp without that chain
   are not supported fixes.
3. **AMD teardown:** one explicitly bounded old-v6 aged-scale reproduction only
   if retained evidence cannot identify the accounting entity/callback. Capture
   hotplug/scheduler wake/migration and fair-server state with loss counters at
   first CPU127 offline, before v7, preserving boot/module/toolchain identities
   and actual service/stress sysctl values. Instrumentation needing a kernel
   build is a separate proposal. Acceptance keeps both hotplugs, transition
   bounds, progress/data checks, zero new faults and reachable later disable/removal and
   cleanup phases. A later activation pass alone is insufficient.

These are proposals for separate authorization and design, not executed work.
No application source, tests, builds, VM diagnostics, refs, index, production,
deployment, pins or lifecycle state were changed. Quick checks validated hashes,
row accounting, tested/workflow identities, current-run exclusion and phase
ordering. No automatic final change review applies to findings/evidence alone.
Lead owns final reconciliation, state/portal records and commits. The session
remains open: [stable portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-ci-failure-analysis/).
