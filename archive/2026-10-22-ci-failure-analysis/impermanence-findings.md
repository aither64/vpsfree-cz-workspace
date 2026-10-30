# Retained impermanent guest state: findings

Owner: implementer0. Investigation only; no source changes, Git mutations,
tests, builds, VMs, reruns, remote collection, deployment or lifecycle actions.
The session and both environment markers matched the trusted binding before
work. The lead owns shared tracking and commits. This is ready for lead
reconciliation, with the runtime gaps below preserved.

## Conclusion and test purpose

There is a definite product persistence defect in both pinned predecessor
daemons and the current target: normal container start saves runtime metadata
**before** selecting the impermanent root, then depends on an incidental CPU
scheduler save to persist that selection. The scheduler does no assignment on
a single-package system. All five current failed cases explicitly report four
CPUs in one package and no assigned CPU package. Reloading the originally saved
base dataset explains the pre-switch ephemeral/post-switch base API values,
while the existing container init keeps running.

This is the strongest source-supported mechanism for the failures, not proof
of the actual saved bytes or actual root after activation: neither runtime YAML
nor the impermanent guest's before/after mount table was uploaded. Missing or
replaced metadata followed by the base fallback remains an alternative. Actual
data loss, actual root replacement and harmless reporting are all unproved.
The current generic sysctl service is reachable after activation; historical
recurrence and unchanged loader source do not exclude an additional current
contribution.

The tests check whether a host userspace upgrade can replace osctld while real
guests keep running. An impermanent NixOS guest intentionally gets a fresh,
temporary ZFS root on a **container start**, with selected data backed by its
ordinary persistent dataset. Replacing the host daemon must retain that same
live root and its temporary contents. A later intentional container restart
must discard temporary contents, retain persistent contents, and clean the old
temporary dataset. This matters to members because a host upgrade must not
silently restart workloads, redirect management actions to another root, or
retire storage still used by a running guest. Keep this contract and revise
the implementation and diagnostics; do not waive the dataset assertion.

## Exact source identities and causal chain

All sources were read from local `repos/vpsadminos.git` objects. Full revisions:

| Role | Revision |
| --- | --- |
| 6.12 predecessor writer | `3cc31e39ba2880a311a1a5889521d2bc0d7e3e0f` |
| 6.18 predecessor writer | `3cb830e596a7fed900bec49f50c9b6cf51e76bb5` |
| Historical failing target | `b81c43ff6865a033268072f55cd94ad763d0630b` |
| Current feature base | `55c5046514d06fe9398a022c1622bdaae5228841` |
| Current failing target | `846bb469505789ba0b2a405fa5905ba6d8253006` |

Numbered, hashed excerpts for every revision are in
[evidence/impermanence](evidence/impermanence/source-manifest.json).
[Source comparison](evidence/impermanence/source-diff-receipt.json) verifies
zero diff from b81c to 846bb, and base to 846bb, in the inspected upgrade common
fixture, container, run configuration, start, CPU scheduler and pool loader.
That is source continuity, not a controlled runtime comparison.

1. **Old writer saves the base first.** In both predecessors,
   `commands/container/start.rb:83–112` calls `ct.init_run_conf` at 91, selects
   impermanence at 94–95, mounts it, then calls the scheduler at 112.
   `Container#init_run_conf` saves at
   [3cc31e39 `container.rb:241–258`](https://github.com/vpsfreecz/vpsadminos/blob/3cc31e39ba2880a311a1a5889521d2bc0d7e3e0f/osctld/lib/osctld/container.rb#L241)
   and [3cb830e5 `container.rb:245–262`](https://github.com/vpsfreecz/vpsadminos/blob/3cb830e596a7fed900bec49f50c9b6cf51e76bb5/osctld/lib/osctld/container.rb#L245).
   A fresh run configuration starts with `ct.dataset` as its dataset.

2. **Selecting the temporary root changes memory without saving.** Both old
   `start.rb:295–328` methods create a new, initially empty ZFS filesystem named
   `<base>.impermanence-<hex>`, register it with GC, call `boot_from`, and prepare
   its directories. This is `zfs create`, not `zfs clone`; the test/handoff's
   “clone” wording describes the name shape, not a demonstrated ZFS clone.
   [3cc31e39 `run_configuration.rb:64–75`](https://github.com/vpsfreecz/vpsadminos/blob/3cc31e39ba2880a311a1a5889521d2bc0d7e3e0f/osctld/lib/osctld/container/run_configuration.rb#L64)
   and [3cb830e5 `run_configuration.rb:103–114`](https://github.com/vpsfreecz/vpsadminos/blob/3cb830e596a7fed900bec49f50c9b6cf51e76bb5/osctld/lib/osctld/container/run_configuration.rb#L103)
   assign the dataset and `destroy_dataset_on_stop` only in memory. Current
   `start.rb:293–324`, `container.rb:260–274` and
   `run_configuration.rb:108–118` preserve this ordering.

3. **A topology-dependent save can mask it.** In all inspected old/new versions,
   `cpu_scheduler.rb:233–236` saves only when `do_schedule_ct` returns a schedule;
   `358–394` returns without one when no package is assigned;
   `412–435` returns for configured `none` or `!use?`;
   [173–185](https://github.com/vpsfreecz/vpsadminos/blob/846bb469505789ba0b2a405fa5905ba6d8253006/osctld/lib/osctld/cpu_scheduler.rb#L173)
   defines `use?` as enabled and **more than one CPU package**. Successful
   assignment on multiple packages incidentally saves the selected temporary
   dataset and cleanup flag. Persistence must not depend on scheduling.

4. **Other direct callers do not rescue this fixture.** Scoped direct-call
   inspection found `RunConfiguration#set_distribution` saves (old lines
   77–86 / 116–125; current 121–129); `Container#set(:distribution)` calls it
   (old 564–571; current 660–667). The fixture sets DNS after start, not the
   distribution. DNS writes ordinary container configuration and guest resolver
   state, not runtime YAML. NixOS `post_mount` creates the init symlink in the
   initially empty root; it does not save runtime metadata. The other
   `boot_from` caller, custom `ct boot`, selects a next-run configuration before
   `start` reaches `init_run_conf`, so its initial save already contains that
   selection (`commands/container/boot.rb:68–108`). This explains why blindly
   adding a save to every `boot_from` caller needs lifecycle review.

5. **The daemon replacement reloads metadata, not the running root.** Current
   `daemon.rb:219–240` drains management and stops daemon services, pools,
   scheduler and monitors. It does not itself stop all container init processes
   or save each live run configuration. Startup imports pools
   (`daemon.rb:154–158`; `commands/pool/import.rb:83–107`).
   [Current `pool.rb:668–705`](https://github.com/vpsfreecz/vpsadminos/blob/846bb469505789ba0b2a405fa5905ba6d8253006/osctld/lib/osctld/pool.rb#L668)
   constructs the container, prepares its LXC home, reconfigures it, probes
   state, ensures a runtime configuration for a running container, and
   reconnects monitoring and console. The two old pool loaders have the same
   `ensure_run_conf` call at 701. No inspected ordinary stop/import path proves
   that the runtime directory must disappear on activation.

6. **Two metadata paths give the same exported symptom.**
   `container.rb:1115` calls
   [current `RunConfiguration.load:45–52`](https://github.com/vpsfreecz/vpsadminos/blob/846bb469505789ba0b2a405fa5905ba6d8253006/osctld/lib/osctld/container/run_configuration.rb#L45).
   A present file supplies its `dataset` verbatim (`327–345`): a stale base
   value is not a missing-key fallback. A missing file returns nil; the running
   state probe/`set_init_pid` can call `ensure_run_conf`, creating and saving a
   new base-backed configuration (`container.rb:278–281,369–377,438–453`). A
   file without `dataset` also falls back to `ct.dataset`. None of these paths
   authenticates the selected dataset against the live root. Old readers use
   the same basic format: 3cc `load_conf:187–219`, 3cb `295–327`.

7. **API output follows this model.** Current
   [container export:839–854](https://github.com/vpsfreecz/vpsadminos/blob/846bb469505789ba0b2a405fa5905ba6d8253006/osctld/lib/osctld/container.rb#L839)
   exports the runtime dataset when available, otherwise the ordinary dataset.
   Old exports do the same (3cc:742–755; 3cb:820–835). This predicts the reported
   base while the previously started init remains alive. Rewriting LXC config
   describes future management/start behavior; it does not itself prove that
   an existing container pivoted its root.

8. **GC makes this more than a cosmetic contract.** Registration persists the
   selected temporary dataset with the run ID (`garbage_collector.rb:114–118`).
   `container_run_dataset_in_use?:210–218` protects it by matching the active or
   next run **ID**, not active `dataset`. Stale dataset metadata with the old ID
   can therefore retain the temporary filesystem; missing-file fallback with a
   new ID has different retirement implications. `container/stop_handler.rb:
   88–104` uses the cleanup flag for writeback and explicit GC release. The
   regular GC also retires runs no longer referenced. This is a source safety
   distinction, not evidence that current CI deleted a live root. Never
   re-register a live dataset under a fresh run ID without reconciling retained
   GC ownership.

Runtime file path follows `RunState::POOL_DIR` → `Pool#ct_dir` →
`RunConfiguration#file_path`:
`/run/osctl/pools/tank/containers/niximpermanent/config.yml`
(`run_state.rb:5–6`, `pool.rb:490–500`, `run_configuration.rb:420–425`).
Persistent GC ownership is `/tank/conf/pool/garbage-collector.yml` for this
fixture (`Pool::CONF_DS`, `GarbageCollector#initialize:75`).

## Current observations and first-error ordering

Source run [39767770407](https://github.com/vpsfreecz/vpsadminos/actions/runs/39767770407),
attempt 1, product job
[119793311317](https://github.com/vpsfreecz/vpsadminos/actions/runs/39767770407/job/119793311317).
Only its already-preserved native artifact was read. The exact paths, raw-file
hashes, selected records, process births, boot IDs and system store paths are in
[observations](evidence/impermanence/current-observations.json),
[numbered log excerpts](evidence/impermanence/current-log-excerpts.txt) and
[input hashes](evidence/impermanence/current-log-manifest.json).

All expected names below have prefix `tank/ct/niximpermanent.`; every actual
post-switch value is `tank/ct/niximpermanent`.

| Test | Expected suffix | Init PID | Birth starttime before = after | Script seconds |
| --- | --- | --- | --- | --- |
| from-6.12-guests | impermanence-4febac | 6191 | 24812 | 395.33 |
| from-6.12-guests-v1 | impermanence-bd3a1e | 6280 | 23689 | 369.30 |
| from-6.12-inherited-guests | impermanence-931fb2 | 6158 | 23570 | 475.97 |
| from-6.18-guests | impermanence-798605 | 7370 | 54011 | 858.49 |
| from-6.18-guests-v1 | impermanence-7b3ada | 6802 | 53379 | 859.33 |

The first assertion exception in every script is the dataset equality. Before
it, predecessor setup successfully created the guest, wrote both markers and
observed the temporary dataset. Activation returned 0; kernel, host boot ID and
booted-system stayed unchanged, current-system changed to the exact target,
and daemon identity changed. The retained assertion verified init PID, DNS
configuration and PID birth before checking `boot_dataset`
(`common.nix:1528–1534,1678–1686`). The persistent/temporary marker checks at
1535–1538 occur **after** the failing comparison and did not execute for this
guest. Existing mount snapshots at 1513 describe the synthetic `upgrade1/2`
workloads, not this real impermanent guest.

For example, from-6.12-guests `machine-shell.log:1922/1940` supplies the
temporary-dataset API records; `1967` and `3259` give equal births;
`2854` is activation; `3250` supplies the base-dataset API record.
Its diagnostics `2615/3122` record one package in the old/new daemons, and
`48` still lists the temporary dataset mounted on the host. Equivalent exact
records for all cases are in the linked excerpts. Host-mounted availability
does not prove which root the guest still uses.

Generic sysctl `runsv` and its logger are present after each failure; preserved
service status is down after a one-shot attempt. Service log contents,
`applied/done`, custom-check status and managed-value readbacks are missing.
The new service can execute asynchronously during this userspace switch.
Its actual timing and outcomes, and any contribution beyond the write-order
defect, remain unknown.

| Candidate classification | Finding |
| --- | --- |
| Product bug | Proven writer persistence defect; strongest explanation under all five observed single-package topologies. Additional reader/state-loss mechanisms remain possible. |
| Assertion mismatch | No evidence that retaining the same live root is a wrong contract. API equality alone cannot certify data continuity, so supplement it instead of deleting it. |
| Setup defect | No demonstrated setup error explains these five first failures: precursor guest creation, readiness and marker writes succeeded. Separate historical readiness failures are not this signature. |
| Evidence gap | Exact pre/post YAML, live impermanent-root identity and post-switch markers are absent. Current sysctl attempt/completion/value evidence is also absent. |

## Recurrence and why passing history differs

Implementer3 owns collection and the full
[recurrence table](recurrence.tsv),
[fixed latest-15 sampling rule](evidence/history/sample-lock.json) and
[denominators](evidence/history/counts.json). The current run is context outside
that sample. Per-test **unique run** counts, excluding the benchmark's second
within-run repetition:

| Test | Eligible runs | Started / known outcome | Pass | Exact mismatch | Other failure |
| --- | --- | --- | --- | --- | --- |
| 6.12-guests | 15 | 8 / 8 | 5 | 3 | 0 |
| 6.12-guests-v1 | 15 | 8 / 8 | 5 | 3 | 0 |
| 6.12-inherited-guests | 15 | 7 / 7 | 4 | 3 | 0 |
| 6.18-guests | 15 | 8 / 8 | 4 | 2 | 2 |
| 6.18-guests-v1 | 15 | 7 / 7 | 3 | 3 | 1 |

The other seven/eight eligible runs per test have cancellation, prebuild or
harness limits; they are not executed passes. There are 14 exact historical
test observations across three runs and only two target heads: staging
[39414347376](https://github.com/vpsfreecz/vpsadminos/actions/runs/39414347376)
and feature [39413777406](https://github.com/vpsfreecz/vpsadminos/actions/runs/39413777406)
both target `49636f902704ce6019a7a8ae47ec0b3ca6902f68`; seed
[39600028637](https://github.com/vpsfreecz/vpsadminos/actions/runs/39600028637)
targets b81c. The feature run's 6.18-guests case fails earlier in nixold
readiness, rather than reaching this comparison. The five variants in one run
are correlated observations, not five independent reruns.

Earlier successes used a materially different reader. For example, target
`3ae196d60b2811e52cbb75a204108df629dca42d` has
`container.rb:292–306` (`adopt_run_conf`),
`run_configuration.rb:137–170` (`adopt_live_root`), and
`pool.rb:701` calls adoption. It scans `/proc/self/mountinfo` for the first
dataset beginning with the impermanence prefix, changes the runtime selection,
re-registers GC ownership and saves. This can mask the old writer defect even
if a stale file exists; it is not limited by an actual missing-file check.

[Commit 2abbe3cc1c102a4b39022d3f73ef4a432ad4d616](https://github.com/vpsfreecz/vpsadminos/commit/2abbe3cc1c102a4b39022d3f73ef4a432ad4d616)
removes that mechanism. Its source and rationale explain the hazards:
unauthenticated first-prefix selection can choose an old run or descendant,
and fresh-ID GC registration can conflict with persisted ownership.
[The exact removal](evidence/impermanence/unsafe-adoption-removal.txt) is
preserved; do not restore it. This explains why passing history does not
establish equivalence with the current reader. It does not identify every
runtime condition in those historical runs.

[Source classification](evidence/impermanence/history-source-boundaries.json)
separates the seven older workflow heads with adoption from eight newer ones
without it. The benchmark run 39305352549's actual product checkout is
`a2ccd72d08dc67f678d7f115a92ed5eeca50c1a1`, not its workflow head; it also has
`adopt_live_root:137`. Its A/B successes are repeated observations in one run
and product head. No flakiness rate or safe baseline equivalence follows.

## Utility, coverage and cost

Keep all supported boundaries. Four cases cover two immutable daemon/kernel
predecessors crossed with cgroup v1/v2. The 6.12-inherited case adds reverse
activation, operations in flight, cross-generation transfer and old-peer
consumers, not another kernel predecessor. The 6.18-v2 guest case also enables
inherited recovery-taint checks. They share this same early impermanence
assertion, so these failures supply no independent result for their later
specialized phases. Retirement should require an explicit support decision or
proven redundant contract, not repeated red output.

Current source already checks persistent and temporary marker integrity,
guest readiness and DNS, repeated activation (`common.nix:2633–2637`), graceful
and abrupt daemon restart (`2650–2663`), then real container restart,
temporary-marker disappearance, persistent-marker retention and old dataset
removal (`3183–3208`). The failing runs reach none of those later impermanent
guest checks. Current coverage lacks runtime-file contents, authentic live-root
identity, explicit scheduler/no-assignment coverage, and safe multiple-candidate
or missing-metadata recovery coverage.

Measured current script execution to the first failure totals 2,958.42 seconds
(49m18s summed guest-test time, not wall time), ranging from 6m09s to 14m19s per
case. This excludes closure builds and does not measure full successful-case
cost. Each builds predecessor and target generations and provisions Fedora,
old NixOS, impermanent NixOS and synthetic continuity workloads; inherited mode
adds a peer and transfer fixtures. Cases request 4 GiB guest RAM
(`common.nix:371`). Recurring early failure consumes that setup while hiding
later coverage. Fixed source boundaries and a recurring concrete invariant
violation make “noise” an inadequate reason to remove the tests. Independent
DNS/readiness failures do exist in history and should be classified separately.

Historical successes also show substantial complete-scenario cost. The table
separates the existing recurrence rows by duration kind; all values are seconds.
The 11 script observations exclude later cleanup. Five ordinary runner
whole-test observations and ten benchmark A/B whole-test observations include
runner preparation/cleanup and must not be pooled with script durations. The
two benchmark legs share one run and product head; each cell lists A then B.
No pooled median is used.

| Test | Script completion range (observations) | Ordinary runner whole-test (one observation) | Benchmark whole-test A / B |
| --- | --- | --- | --- |
| 6.12-guests | 1500.50–2266.74 (3) | 2162.37 | 2057.58 / 1907.47 |
| 6.12-guests-v1 | 1446.53–2256.38 (3) | 2156.99 | 1815.49 / 1849.92 |
| 6.12-inherited-guests | 1758.98–3424.09 (2) | 2716.29 | 2158.23 / 2327.01 |
| 6.18-guests | 4449.07–7599.45 (2) | 6918.83 | 5798.70 / 5365.03 |
| 6.18-guests-v1 | 4180.55 (1) | 6203.32 | 5914.17 / 5209.48 |

[Timing reconciliation](evidence/impermanence/historical-timing-by-kind.json)
binds these groups to the unchanged local recurrence table and its SHA256.

## Prioritized proposals and compatibility limits

1. **Repair the writer invariant in osctld.** Persist the final selected runtime
   dataset, run ID, distribution and destruction flag before a container starts
   using that root, independently of CPU scheduling. Keep run initialization
   and custom boot ordering coherent; handle failed preparation without
   publishing false live state. This needs source changes and tests in a later
   authorized package. A target-only writer fix cannot repair bytes already
   written by these immutable predecessor pins.
2. **Design authenticated old-state handling.** The target reader must handle
   old writer output if these upgrade paths remain supported. Distinguish
   valid saved state, stale base metadata, missing metadata and conflicting
   evidence. Authenticate init identity and its mount namespace/root, reconcile
   that with the exact dataset and existing GC/run-ID ownership, and reject
   ambiguity without retiring live roots. Do not guess by dataset-name prefix,
   rewrite the historical pins, or call any mounted dataset the guest root.
   Recovery is a separate design obligation; neither a first-match scan nor
   merely suppressing the API comparison satisfies it.
3. **Improve evidence and phase isolation.** Preserve both marker results and
   actual root identity even when the API equality fails, while retaining that
   failure. Add a small focused runtime persistence/reload regression before
   the broader guest upgrade matrix. Separating diagnostics from the assertion
   permits a useful failure report without silently continuing the scenario.

No new YAML format is required merely to save already-supported fields. Any
later reader/recovery change must support old-writer/new-reader and supported
downgrade readers, retain run IDs/GC ownership, and leave live mounts intact.
It must specify recovery for already-stale records; no current deployment,
schema migration or coordinated fleet update is selected. Rolling deployment
must account for affected old writers, rather than assuming only new starts.

## Smallest discriminating diagnostic — proposed, not executed

Use one disposable **upgrade/from-6.12-guests** case with the same immutable
predecessor and exact selected target/input graph. Stop at the first activation
and retained assertion; do not run the whole later matrix or change scheduling.
Capture at (a) immediately after impermanent guest start, (b) immediately before
switch, and (c) immediately after pool import, before the equality assertion.
Use the existing test transport and preserve its outputs outside the guest.

At each boundary, timestamp and collect these read-only observations. Resolve
`ct_pid` from `osctl -j ct show niximpermanent`, record it, and verify the same
PID **and full `/proc/<pid>/stat` birth** before and after collecting. A later
instrumented implementation should use descriptor-authenticated identity for
race resistance; a numeric PID alone is insufficient.

```sh
date --iso-8601=ns
osctl -j ct show niximpermanent
stat -c '%d:%i %s %y %z %a %U:%G' /run/osctl/pools/tank/containers/niximpermanent/config.yml
sha256sum /run/osctl/pools/tank/containers/niximpermanent/config.yml
cat /run/osctl/pools/tank/containers/niximpermanent/config.yml
cat /tank/conf/pool/garbage-collector.yml
cat /proc/"$ct_pid"/stat /proc/"$ct_pid"/mountinfo
readlink /proc/"$ct_pid"/ns/mnt
stat -L -c '%d:%i' /proc/"$ct_pid"/root
cat /proc/"$ct_pid"/root/persistent/upgrade-retained
cat /proc/"$ct_pid"/root/upgrade-ephemeral
cat /proc/self/mountinfo
zfs list -Hp -o name,mountpoint,mounted,origin -r tank/ct
uname -r
cat /proc/sys/kernel/random/boot_id
readlink -f /run/booted-system /run/current-system
pgrep -f '^osctld: main$'
```

For each exact candidate found in the guest's mount table, also capture
`zfs get -Hp -o name,property,value guid,mountpoint,mounted,origin <exact-dataset>`
and `stat -L -c '%d:%i' <mountpoint>/private`, comparing with the authenticated
guest root. Preserve missing-file/error statuses instead of substituting empty
files or re-creating metadata. Root `readlink` output alone is not sufficient
after LXC pivot_root. Capture daemon `/proc/<daemon-pid>/stat` too, and the exact
activation command, status and interval.

At these same boundaries capture the generic sysctl evidence without applying
it again:

```sh
date --iso-8601=ns
sv status sysctl
cat /var/log/sysctl/current
stat /run/service/sysctl/applied /run/service/sysctl/done
cat /run/service/sysctl/applied /run/service/sysctl/done
/service/sysctl/check
sysctl -a
```

Record each command's exit status, including absent predecessor service/state.
Preserve `/etc/sysctl.conf`, `/etc/sysctl.d/*.conf` and their resolved source
identities, then compare the managed keys with the read-only `sysctl -a`
snapshot. `/service/sysctl/check` is the target's existing read-only check path
used by `tests/suite/system/sysctl.nix:117,126`; target module
`os/modules/config/sysctl.nix:37–70` defines status and application behavior.
Never invoke `sv once/start/restart`, `sysctl -w` or `sysctl --system` as a
diagnostic readback. Timestamped existing logs distinguish an observed attempt
from mere supervision; completion alone does not establish causal contribution.

Discriminating outcomes:

| Observation | Supported conclusion |
| --- | --- |
| YAML already names base before activation; API names temporary; actual root is temporary | Old writer defect realized in this run; subsequent stale reload is sufficient for the API mismatch |
| YAML names temporary before switch and disappears/changes during switch | Additional state-loss/overwrite path; locate it within that interval |
| YAML retains correct temporary identity; API becomes base | Reader/object selection/export defect; trace loaded object and file identity |
| API changes but root identity and both markers remain intact | Reporting/model mismatch observed for this diagnostic; management/cleanup safety still needs verification |
| Actual root or marker changes with the same process identity | Real mount/data continuity failure; trace the first change, preserving the failed artifact |

## Regression acceptance for a later repair

- Finalized runtime bytes match the selected live root before launch, with one
  package, scheduler disabled, configured `none`, failed/no assignment, and a
  successful multi-package assignment. Scheduling must not mask persistence.
- Test old writer/new reader with the exact two predecessor formats and stale
  base selection, correct saved temporary selection, missing file/field, and
  conflicting metadata. Supported old/downgrade readers retain compatible
  fields and ownership. Corrupt or ambiguous input must preserve live roots.
- Do not select another container's root, an old run, a similarly prefixed
  descendant, or the first of multiple mounted candidates. Simulate PID reuse
  and init death during discovery; reject stale process identities.
- All five supported upgrade variants retain init PID **and birth**, actual
  root/mount and ZFS identity, API dataset and both markers through activation,
  repeat activation, graceful daemon restart and abrupt daemon death. Assert
  unchanged host boot/kernel and changed daemon identity separately.
- A normal container restart creates a new temporary root and process identity,
  removes its temporary marker, preserves the persistent marker and guest
  generation, and eventually cleans only retired roots. Verify GC/run-ID
  ownership during adoption, failed start, concurrent stop and final deletion;
  no live dataset may be trashed or re-registered under conflicting ownership.

## Evidence checks and handoff

Checked exact Git object availability, source excerpt hashes, old/new line
anchors, zero-diff boundaries, all five native first-error sequences, equal
PID births and host boot IDs, successful switches, topology, script durations,
and historical source classification. Raw source/log manifests make the
checks repeatable without remote retrieval or product test execution.
[Evidence check receipt](evidence/impermanence/evidence-checks.json) records
68 source-file hashes, 20 raw log hashes, all five identity/boot comparisons,
duration accounting and local-link existence.
Investigation findings/evidence alone do not trigger automatic final review.
No product documentation was edited: these are unresolved incident findings
and proposals, appropriately retained here until a repair design is accepted.

Remaining: lead reconciliation of the shared recurrence table and these
proposals; separately authorized diagnostic/design/implementation if selected.
Runtime YAML, live root/data continuity and timed generic-service execution
remain material gaps. Session stays open.

[Stable session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-ci-failure-analysis/)
