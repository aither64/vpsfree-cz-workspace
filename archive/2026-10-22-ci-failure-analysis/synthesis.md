# CI failure causes and test usefulness

The investigation found a definite impermanent-root persistence defect, a
predecessor DHCP sandbox-entry failure whose exact rejection remains unknown,
and a real CPU-hotplug scheduler warning whose triggering entity is unresolved.
**Keep all three test families and revise them.** None is demonstrated obsolete,
redundant or harmless. No fix, rerun, diagnostic VM, merge or deployment was run.

## Findings and recommendations

| Family | Cause and confidence | What users rely on; test value | Recommendation |
| --- | --- | --- | --- |
| Five impermanent guest upgrade cases | **Definite source defect, strongest incident explanation:** the old and current daemon saves run configuration before choosing the temporary ZFS root. A later save depends on CPU scheduling, which skips the observed single-package machines. A daemon reload can therefore report the base dataset while the same init continues. Actual saved YAML, guest mount identity and post-switch markers are missing, so incident-level state loss versus stale metadata and any additional current contribution remain unresolved. | Replacing host userspace must preserve a running guest's temporary root, processes and data, then discard only temporary data on an intentional guest restart. API state also controls safe management and cleanup. Equality is a valid invariant; failure occurs before the guest's marker checks, so it proves neither data loss nor intact data. The five variants cover two predecessors, cgroup v1/v2 and inherited operations. | **Keep; repair persistence and design safe old-state handling.** Save final selection independently of scheduling. A writer fix alone cannot repair old records from immutable predecessors. Authenticate live root/init and existing run/GC ownership when handling stale state; never restore the reverted first-prefix mount scan. Capture mounts and markers even when equality fails. |
| Nested Podman upgrade | **Predecessor setup failure:** dhcpcd sandbox entry fails, networking fails, no IPv4/default route, then 126 probes and a 900s timeout. Exact package source limits the error to PR_SET_NO_NEW_PRIVS or PR_SET_SECCOMP setup. The predecessor kernel has authority-guard EACCES paths, but failed call, effective configuration/credentials/filter and introducer are unproved. Target activation never occurs, excluding the incoming sysctl service from this executed path only. | Users run application containers inside VPS/system containers. This case protects nested process/data/overlay/cgroup continuity across userspace replacement and creation of a new memory-limited workload. Inner containers use --network none; outer DHCP/DNS is preparation, not nested-network coverage. This attempt never reaches Podman. | **Keep; revise setup provenance and readiness diagnostics.** Record image/package hashes and diagnose link/address/route/DNS/service layers promptly. Separate reproducible upgrade fixtures from latest-image compatibility coverage. Repair only the demonstrated client/policy/kernel owner; disabling confinement or changing DNS does not explain this error. |
| AMD aged-scale-v6 livepatch | **Real kernel invariant warning; trigger unresolved.** First CPU127 offline under v6 violates the dying runqueue predicate before v7 insertion. The callback warns, continues and returns zero, explaining successful offline. Count two with only migration/127 listed does not prove a second task: a deadline fair-server entity can contribute to runnable accounting. Pin state and the responsible wakeup/entity/callback were not captured. | A long-running busy host must accept patch replacement and CPU hotplug without stranding tasks or damaging kernel state. The four-hour, 100000-task, 128-guest-CPU envelope adds coverage beyond smoke tests. Successful sysfs writes and a successful 758s activation do not prove kernel health. Cumulative dmesg correctly catches the warning. | **Keep envelope and fatal no-fault checks; revise phase diagnostics.** Check immediately after each hotplug while retaining cumulative history. Capture task/class/server/pin accounting before selecting a kernel change. No evidence supports suppressing the WARN or changing sysctls, age, task/CPU counts or callback ordering as a fix. |

Impermanence current failed scripts total 49m18s of summed guest-test time,
6–14 minutes per case; this excludes builds and later phases. Podman historical
script times are 42.5–60.7 minutes, while separate whole-test observations are
53.3–71.8 minutes. AMD uses a 16-GiB/128-vCPU guest for about 4h22m in the
current runner. These are different timing scopes, not comparable physical CPU
consumption. Early failures waste setup and hide later coverage, supporting
smaller focused checks and better diagnostics rather than removal.

The AMD current attempt passed activation, second hotplug and A migration/
progress, then failed its health assertion. B migration, disable/unload,
stopped-task checks and normal complete teardown/shutdown checks **did not
execute**. The first-warning trace buffers were not active at the relevant time.
The impermanence failures likewise stop before later marker/restart/cleanup
checks. Do not count those phases as passed.

## Exact historical recurrence summary

Fixed sample: latest 15 completed workflows created before current run
39767770407, October 19–22, 2026; attempt 1 throughout. Cancelled runs remain in
the sample. Current-run preserved evidence is separate context, not a fresh
remote observation. The [111-row table](recurrence.tsv) supplies exact full
heads, jobs, attempts, first errors, timings, URLs and evidence paths; the
[history report](history-findings.md) supplies per-case denominators.

**P** = executed pass; **F** = exact signature; **O** = another first failure;
**C** = cancelled without a terminal outcome; **B** = prebuild failure;
**U** = no test execution/selection. Dataset numbers count case observations,
not independent runs. **N** = native result/runner/shell evidence;
**J** = explicit job-log test/setup evidence; **M** = metadata only;
**R** = started-runner evidence without a terminal result.

| Run | Tested product head | Five dataset cases | Podman | AMD | Evidence |
| --- | --- | --- | --- | --- | --- |
| [39764186292](https://github.com/vpsfreecz/vpsadminos/actions/runs/39764186292) | `89587060` | 5C | C | C | M/R |
| [39759039117](https://github.com/vpsfreecz/vpsadminos/actions/runs/39759039117) | `88486d43` | 5C | C | C | M |
| [39745935323](https://github.com/vpsfreecz/vpsadminos/actions/runs/39745935323) | `85282623` | 5B | B | C | J/R |
| [39744127896](https://github.com/vpsfreecz/vpsadminos/actions/runs/39744127896) | `14cdf1ca` | 5C | C | C | M |
| [39600028637](https://github.com/vpsfreecz/vpsadminos/actions/runs/39600028637) | `b81c43ff` | 5F | P | P | N |
| [39598560664](https://github.com/vpsfreecz/vpsadminos/actions/runs/39598560664) | `f3e91f62` | 5C | C | C | M |
| [39414347376](https://github.com/vpsfreecz/vpsadminos/actions/runs/39414347376) | `49636f90` | 5F | P | O | N |
| [39413777406](https://github.com/vpsfreecz/vpsadminos/actions/runs/39413777406) | `49636f90` | 4F, 1O | P | P | N |
| [39396698293](https://github.com/vpsfreecz/vpsadminos/actions/runs/39396698293) | `e32d5382` | 2P, 1O, 2C | C | C | M/N/R |
| [39381114351](https://github.com/vpsfreecz/vpsadminos/actions/runs/39381114351) | `e074a470` | 5P | P | P | J/N |
| [39358414083](https://github.com/vpsfreecz/vpsadminos/actions/runs/39358414083) | `8019b9ff` | 5P | P | C | M/N |
| [39309610523](https://github.com/vpsfreecz/vpsadminos/actions/runs/39309610523) | `3ae196d6` | 4P, 1O | P | F | N |
| [39305352549](https://github.com/vpsfreecz/vpsadminos/actions/runs/39305352549) | `a2ccd72d` | 10P | 2P | U | J |
| [39296042103](https://github.com/vpsfreecz/vpsadminos/actions/runs/39296042103) | `a2ccd72d` | 5U | U | U | J |
| [39276852536](https://github.com/vpsfreecz/vpsadminos/actions/runs/39276852536) | `a2ccd72d` | 5U | U | U | J |

Benchmark 39305352549 has two passing native legs, one product head and one
run. Its tested head a2ccd72d differs from workflow head 295b814a; the other
two benchmark dispatches also select a2ccd72d but never execute the tests.
Staging 39414347376 and feature 39413777406 share head 49636f90. Cancellation
39396698293 retains two completed passes and an observed earlier readiness
failure; cancellation does not erase those results.

Dataset history contains **14 exact case failures in three runs/two heads**.
Earlier passing targets contained live-root adoption, removed at 2abbe3cc as
unsafe; those passes are not an equivalent baseline against the current reader.
Podman has **seven passing historical runs/eight observations**, but image
archive/DHCP package identities were not retained, preventing a same-image
comparison. AMD has **12 eligible runs, seven starts, five known outcomes,
four first-hotplug exposures: three passes and one exact warning**. One other
outcome fails progress before hotplug. The same warning phase/v6 module is
confirmed at 39309610523. These mixed sources, setups and execution limits do
not establish a flake rate or common runtime cause.

## Prioritized next work — proposals only

1. **Impermanence:** first capture one representative from-6.12-guests case
   through its first activation: raw run YAML and file identity, API state,
   init PID/birth, guest mount/root/ZFS identity, both markers and GC/run IDs.
   Timestamp sysctl logs/stamps/check/managed values to retain the current
   contribution boundary. Then design independent writer persistence and safe
   old-record recovery. Acceptance includes one-/multi-package and disabled
   scheduler paths, old/new readers, all five upgrade variants, repeated
   activation, graceful/abrupt daemon restart and cleanup without live-root loss.
2. **Podman:** propose one predecessor-only container start, stopping before
   APT/target activation, with a 60s network observation cap and a trace of the
   two sandbox-entry calls. Preserve effective credentials/NNP/filter/guard
   state and immutable image/package identity. Ptrace can alter guard behavior;
   plain strace alone does not capture all effective state. A repair must retain
   confinement, restore DHCP/address/route and separately DNS/endpoints, then
   pass full nested workload/data/identity/memory-limit continuity assertions.
3. **AMD:** if selected separately, one original aged-scale-v6 envelope through
   first CPU127 offline, stopping before v7, with a 120s loss-accounted trace
   window inside an explicitly budgeted five-hour VM. Capture locked runqueue,
   class/entity/server/pin state and wakeup/callback ordering; record actual
   sysctl phase values. Recorder preparation or an unavailable safe probe needs
   separate work/ABI authorization. Full repair acceptance retains both hotplugs,
   transition bounds, A/B migrations, data/progress, disable/unload and zero
   faults through normal end/shutdown. A diagnostic is not full qualification.

Detailed source chains, exact diagnostic commands and regression criteria:
[impermanence](impermanence-findings.md), [Podman](podman-findings.md),
[AMD](hotplug-findings.md), and [independent historical utility assessment](history-findings.md).
All four retained lanes and architect reconciled the findings; no count or
recommendation disagreement remains. No automatic change review was triggered:
this deliverable consists of investigation findings/evidence, with no product
change. Original CI observation/integration stays with its source session.

[Open session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-ci-failure-analysis/)
