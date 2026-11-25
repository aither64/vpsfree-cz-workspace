# Cluster hard-lockup detection history

## Question and current status

Determine whether retained central logs show kernel **hard-lockup detections**
followed by survival or recovery, to inform the tradeoff of enabling panic on
hard-lockup detection. This record distinguishes detector reports, continued
logging, and recovery of the specific reported CPU. It does not treat a missing
match as evidence that the cluster has never had a hard lockup.

Collection is read-only as `root@log.int.prg.vpsfree.cz`. Session identity and
both environment markers match `2026-10-20-kernel-check` in the bound workspace;
retained instructions and same-session roster were checked before this work.
No production configuration, trust, service, workload, repository source or
refs changed. One sequential scanner is used; no parallel remote scanners.

**A historical detection was found; recovery is not established.** The
current-file pass and 78-file historical tranche contain no matching detection.
The first additional legacy file contains two CPU reports in one episode on
`stg/node1` in October 2022, followed by a different boot. The wider search is
stopped while that episode receives context and chronology analysis. The two
remaining already-budgeted legacy files were then checked at the lead's
direction and have no detections. This does not provide an example of harmless
detection or affected-CPU recovery.

## Inventory and search boundaries

At 2026-10-20 20:50 CEST, metadata inventory beneath
`/var/log/remote/cz.vpsfree/nodes/` found:

- 26 host directories in `brq`, `pgnd`, `prg`, and `stg`; this includes three
  storage/backup names rather than assuming every directory is a current VPS
  node.
- 3,477 files, 1,185,675,318,674 bytes (about 1.08 TiB).
- 3,461 uncompressed `log-YYYYMMDD` rotations with suffixes from 20221102 to
  20261020. Retention is host-specific and discontinuous across the cluster.
- 13 growing current `log` files, 3,821,943,532 bytes at inventory time.
- Three other uncompressed files (`log.3` twice and `log-cisty` once), totaling
  861,203,528 bytes, later checked in the separate legacy passes.
- No compressed node files in this bounded-depth metadata inventory.

`rg` and `locate` are unavailable on the central server. GNU grep, timeout,
Perl and compressed-text grep helpers are available. No obvious Loki, Graylog,
Elasticsearch, OpenSearch or locate index directory was found at their usual
locations. A local journal directory exists; it has not been established as an
index of forwarded node records. This is not an exhaustive inventory of every
possible external indexing service.

The 13 active sources are `brq/node5`, `brq/node6`, `pgnd/node1`,
`prg/backuper2`, `prg/node19` through `prg/node25`, `stg/node1`, and `stg/node2`.
Their sampled current first lines are October 20 00:00:01 CEST; sampled last
lines at the boundary check range from 20:52:01 to 20:52:05 CEST. The initial
scan completed earlier than that last-line sampling, so that sampling does not
extend the certified search to later append events. Current files can grow.

The newest seven completed rotation dates cost 43,408,972,958 bytes, exceeding
the lead's 30 GiB historical budget. The selected tranche therefore contains:

- Five completed rotations per active source: suffixes 20261016–20261020,
  normally actual contents October 15–19, with first/last timestamps recorded
  per file during the scan.
- One newest retained rotation for each of the 13 inactive host directories,
  allowing all 26 retained host directories to be represented. These are
  **sparse older samples**, not a continuous window: `brq/node2` 20240630,
  `brq/node4` 20230914, `pgnd/node2` 20221209, `prg/backuper` 20240104,
  `prg/nasbox` 20251014, `prg/node15` 20231112, and `prg/node1`, `node7`,
  `node8`, `node9`, `node10`, `node11`, `node13` all 20221201.

The exact selected 78 files total **30,118,840,414 bytes (28.050 GiB)**;
[selection and byte sizes](cluster-hardlockup-selection.tsv) preserve the
planned sources. The [search record](cluster-hardlockup-search-output.txt)
records each started/completed file, actual content boundaries, elapsed seconds,
return code, and any candidate lines. Only completed files count toward coverage;
a timeout or error must remain explicit. The full 1.08 TiB retention is not being
searched.

## Completed search results

| Pass | Completed coverage | Result and timing |
| --- | --- | --- |
| Current logs | 13 active sources, approximately 3.822 GB at inventory; growing files | No matching detection; all return 1; no timeout/error; exact timer not retained |
| Selected historical tranche | All 78 files, all 26 retained host directories; 30,118,840,414 bytes | No matching detection; every return 1; 119 seconds server wall time, approximately 253.10 MB/s; no timeout/error |
| Legacy sample, stopped on first candidate file | `stg/node1/log.3`, 689,725,792 bytes, actual October 25–30, 2022 | Two detection lines, one episode; return 0; full single-file scan in 3 seconds |
| Remaining legacy files, resumed at lead direction | `prg/node23/log.3`, 97,173,915 bytes, October 26–30, 2022; `stg/node1/log-cisty`, 74,303,821 bytes, April 16, 2025 | No matching detection; both return 1; 1 second server wall time; no timeout/error |

Completed historical search coverage is **30,980,043,942 bytes (28.852 GiB)**,
across 81 files. No started file has partial coverage, a timeout or a read error.
The first legacy loop stopped after the candidate file as instructed; the lead
then explicitly directed the remaining two files to be checked.
[Legacy scan record](cluster-hardlockup-legacy-search-output.txt) preserves the
two hit lines and stop status;
[remaining legacy scan record](cluster-hardlockup-legacy-remaining-search-output.txt)
preserves the resumed no-match results. No wider calendar tranche was launched.

The 78-file content timestamps establish continuous October 15–19 coverage for
the 13 active sources, with individual rotations sometimes ending just after
midnight. Inactive samples cover only their recorded single retained day.
These negative samples cannot answer whether hard lockups occurred at other
times, were not forwarded, or occurred on machines outside this hierarchy.

## Historical episode: stg/node1, October 28, 2022

Source: `/var/log/remote/cz.vpsfree/nodes/stg/node1/log.3`.
The [bounded kernel context](cluster-hardlockup-stg-node1-20221028-context.txt)
retains exact original line numbers, excluding unrelated network payloads.

| Source line | Log timestamp / uptime | Fact |
| --- | --- | --- |
| `2586235` | `13:27:15.443287+02:00` / 0 | Boot message: Linux 5.10.147; repeated buffered copy at `2587022` is not another boot |
| `2590049` | `13:28:16.420494+02:00` / 108.280440 | Kernel page-fault BUG for address `0x3fe0` before the watchdog reports |
| `2590055` | `13:28:16.420512+02:00` / 129.298213 | `NMI watchdog: Watchdog detected hard LOCKUP on cpu 25` |
| `2590056` | `13:28:16.420514+02:00` / 129.298213 | CPU 25, PID 3028, `z_livelist_dest`, `Kdump: loaded`, runtime `5.10.147.8 #1-vpsAdminOS`, livepatch taint `K` |
| `2590059` | `13:28:16.420519+02:00` / 129.298216 | CPU 25 RIP `native_queued_spin_lock_slowpath+0x128/0x1e0` |
| `2590091` | `13:28:16.420575+02:00` / 129.298239 | `NMI watchdog: Watchdog detected hard LOCKUP on cpu 33` |
| `2590092` | `13:28:16.420576+02:00` / 129.298240 | CPU 33, PID 2801, `mmp`, same runtime and `Kdump: loaded` |
| `2590095` | `13:28:16.420579+02:00` / 129.298242 | CPU 33 RIP `native_queued_spin_lock_slowpath+0x63/0x1e0` |
| `2590124` | `13:38:38.635140+02:00` / 0 | Subsequent boot message: Linux 5.10.149 |

The host hardware record identifies Supermicro X10DDW-iN and Intel Xeon
E5-2630 v4; it is a historical staging node, not node24's current AMD platform.
Both CPU dumps have EFLAGS `0x2`, RCU reports CPU 25 stalled, and the RIPs are
spinlock slow paths. The displayed `Call Trace:` headings do not contain a
complete symbolic caller stack for those two CPUs in the retained context.
The RCU kthread does have its separate scheduling stack. Do not substitute that
stack for the affected CPU's missing callers.

Count this as **two detector CPU reports in one short episode**, not two
independent incidents or repeated same-CPU warnings. The full file's signature
scan returned only those two lines. It therefore supplies no fresh repeated
same-CPU report from which an intervening healthy heartbeat can be inferred.
The next boot record follows roughly 10m22s later in central timestamp order.
The reset mechanism, whether a panic was attempted, and the disposition of
CPUs 25/33 before reset are not established by these excerpts. A later 5.10.149
boot cannot be counted as same-boot survival of the reported 5.10.147.8 kernel.
No benign/nonfatal recovery conclusion is supported by this candidate alone.

## Exact signatures and commands

The initial current-file pass used this case-insensitive diagnostic expression:

```sh
timeout 15s env LC_ALL=C grep -aHnEi 'hard[ _-]?lockup.*detect|detect.*hard[ _-]?lockup|hard LOCKUP on|NMI watchdog:.*hard.?lockup' "$file"
```

All 13 files returned grep status 1 (no match), with no timeout/error. No precise
whole-pass timer was retained for this first pass; no throughput is inferred
from an invented elapsed value.

The selected historical pass uses faster case-insensitive literal matching:

```sh
timeout 20s env LC_ALL=C grep -aHnFi -e 'hard LOCKUP' -e 'hardlockup detected' -e 'detected hardlockup' "$file"
```

The incident Linux source emits `Watchdog detected hard LOCKUP on cpu %d`
(`kernel/watchdog.c:194` at `1dfea587406b7dd79973831d1677fb2418e5e9aa`), which
this literal set includes. Matched text is a candidate until its kernel context
is checked; command/configuration mentions are not detector episodes. Soft
lockups, RCU stalls and hung tasks are excluded from the event definition.

Each historical grep has a 20-second timeout; the loop stops on the first match
or any status greater than 1. A hit redirects work to bounded context and
chronology rather than continuing to maximize scanned bytes. Single-file and
whole-pass elapsed times are captured on the central server.

## Evidence needed for survival classification

For a real detection, retain host, timestamp/timezone, affected CPU, running
kernel, stack/interrupt context, and matching panic/watchdog policy when known.
Count fresh reports and distinct episodes separately, and account for duplicated
forwarding/boot replay. Establish boot boundaries with actual boot records and
chronology, rather than assuming every later line shares the same boot.

Later host/control/network logging proves only that some execution/forwarding
continued. It does not prove that the affected CPU resumed heartbeat interrupts.
The platform lane identified a stronger possible discriminator: an accepted
hard-lockup report sets the affected CPU's `warned` flag, later still-stalled
checks suppress repeated reports, and a healthy-heartbeat check clears the flag
without a recovery message. Fresh repeated reports for the same CPU in the same
boot can therefore establish an intervening healthy check **only after excluding
CPU hotplug, watchdog disable/re-enable/reinitialization and replay/reset paths**.
The architect/platform owner must check that state machine against each event's
actual kernel source. No such recovery is inferred solely from quiet logs.

No proposal to change the panic setting is authorized by this read-only search.
Any absence, surviving detection or recovered CPU must be stated at its actual
confidence and coverage before discussing operational consequences.
