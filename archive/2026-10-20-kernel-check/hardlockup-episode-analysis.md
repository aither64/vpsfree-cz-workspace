# Historical hard-lockup episode classification

Independent local analysis by implementer2, 2026-10-20, following the
[follow-up brief](design.md) and its evidence tiers. Exact current session,
both environment markers and retained workspace-write roster identity were
reconfirmed. Workspace guidance was unchanged from the earlier read.
No remote collection, source/ref/configuration mutation or test was performed.
The sole collector is implementer1.

## Classification

**Two hard-lockup detector reports on different CPUs in one near-simultaneous
kernel-fault/RCU-stall episode, followed by a new boot. Recovery before reset
is unknown.** This is neither a demonstrated benign/recoverable detection nor
proof that the affected CPUs could never have recovered. The reset mechanism
and historical panic policy are not established.

| Evidence tier | Disposition |
| --- | --- |
| Hard-lockup report observed | Established for CPU 25 and CPU 33, high confidence. |
| Later meaningful host operation | Not established by the supplied post-report records. Later diagnostic output exists, but is not successful service/control activity. |
| Same-boot operational continuation | Not established. Diagnostic uptime continues for only microseconds; the next boot has a different kernel and uptime zero. |
| Affected CPU resumed ordinary execution | Not established for either CPU. NMI stack output is not a normal-context heartbeat. |
| Sustained recovery | Not established; no qualifying interval exists in this evidence. |
| Irreversible/fatal stall or panic-caused reboot | Not established. A later reboot alone cannot settle these counterfactuals. |

This episode cannot quantify how often enabling `hardlockup_panic=1` would
crash a machine that otherwise recovers. It also cannot show that enabling
panic would have successfully produced a dump or shortened this outage.

## Local inputs and scope

- [Extracted context](cluster-hardlockup-stg-node1-20221028-context.txt): 75
  selected kernel records, retaining exact original path and line numbers.
- [Collector history](cluster-hardlockup-history.md): bounded source interval,
  boot context and collection limits.
- [Completed legacy signature search](cluster-hardlockup-legacy-search-output.txt):
  the complete `stg/node1/log.3` scan found exactly the two warning lines.
- [Detector semantics](hardlockup-recovery-semantics.md): source analysis of
  the 2026 `.95`/`.113` detector, with historical applicability explicitly
  unresolved. It is not proof of the exact 2022 state machine or policy.

Original source is
`/var/log/remote/cz.vpsfree/nodes/stg/node1/log.3` on the central collector.
Implementer1 inspected original lines 2589950–2590125 for this context and
reports that original line 2590123 is the last old diagnostic and the
immediately following line 2590124 is the next boot. This analysis relies on
that collector boundary statement as well as the retained numbered records;
the local file is a selected excerpt, not a complete copy of every intervening
pre-report line. There was no independent remote re-scan.

The runtime headings identify `5.10.147.8 #1-vpsAdminOS`, `Kdump: loaded`,
taint `G ... OE K`, and Supermicro X10DDW-iN, BIOS 3.0a. The collector's hardware
context identifies Intel Xeon E5-2630 v4. This historical staging platform and
livepatched kernel are distinct from the 2026 node24 incident. The heading does
not identify exact livepatch module bytes or the loaded watchdog panic setting.
No boot ID was collected.

## Timeline: outer timestamps are batched

The following times preserve the source's `+02:00` offset on October 28, 2022.
Uptime values are the kernel's embedded timestamps.

| Original line | Outer timestamp / kernel uptime | Observation |
| --- | --- | --- |
| 2586235; repeated at 2587022 | `13:27:15.443287` / `0` for first boot heading | Collector identifies a Linux 5.10.147 boot and buffered duplicate, not two boots. These headings are described in the collector record rather than reproduced in the 75-line excerpt. |
| 2590049 | `13:28:16.420494` / `108.280440` | Page-fault BUG for address `0x3fe0`. |
| 2590051–2590054 | `13:28:16.420506–.420511` / `129.297194–129.297203` | RCU stall names CPU 25; CPU 29 requests an NMI backtrace from CPU 25. |
| 2590055 | `13:28:16.420512` / `129.298213` | Hard-lockup detector reports CPU 25. |
| 2590073–2590074 | `13:28:16.420552–.420553` / `129.298226` | Additional NMI backtrace heading for CPU 25. |
| 2590091 | `13:28:16.420575` / `129.298239` | Hard-lockup detector reports CPU 33. |
| 2590109–2590123 | `13:28:16.420597–.420613` / `129.298254–129.298292` | RCU grace-period kthread starvation and its scheduling stack. |
| 2590124 | `13:38:38.635140` / `0.000000` | Linux 5.10.149 boot heading. |

The page-fault and first hard-lockup messages are **21.017773 kernel seconds**
apart, but their outer timestamps differ by only **18 microseconds**. These
outer timestamps therefore cannot be treated as original execution times for
the diagnostic records. They establish collector-record order and a batch
arrival/forwarding interval. There is no reason to interpret the fault and
watchdog as 18 microseconds apart in execution.

The reports for CPUs 25 and 33 are 26 microseconds apart in embedded uptime
and 63 microseconds apart in outer time. Same runtime, hardware, contiguous
diagnostics and matching monotonic uptime strongly support grouping them as
one multi-CPU incident. This grouping does not require claiming either CPU
had recovered before the other warning.

After the first warning, the displayed old-boot diagnostic uptime advances
only **79 microseconds**, to 129.298292. The next original record arrives
**622.214527 seconds (10m22.214527s)** after that last diagnostic in outer
timestamp order and resets uptime to zero with a different kernel version.
That is an observed reboot boundary, not a measured duration of continuous
CPU lockup. Delivery buffering, reset time, operator action and any unforwarded
activity remain unknown. Do not estimate the original boot's wall-clock start
by subtracting these buffered uptimes from the collector timestamps.

## Reports, duplicate disposition and CPU attribution

The valid detector emissions are original lines 2590055 and 2590091:

`NMI watchdog: Watchdog detected hard LOCKUP on cpu 25`

`NMI watchdog: Watchdog detected hard LOCKUP on cpu 33`

They target different CPUs and have different task/register contexts. They are
not duplicated forwarding of one warning. Local parsing found 75 unique original
line numbers and no exactly duplicated complete context record. The completed
whole-file signature search contains only these two hard-lockup emissions;
it supplies no later warning for the same CPU.

CPU 25's additional heading at 2590073 says **NMI backtrace**, following the
RCU diagnostic's backtrace request at 2590054. Its PID, RIP, RSP and register
context match the nearby CPU 25 dump while diagnostic uptimes advance slightly.
Count it as another diagnostic view of that CPU, not another watchdog detection
or a reset/rearm event. CPU 29's RCU detection/reporting activity must not be
misattributed to CPU 25 making ordinary progress.

CPU 25 is PID 3028, `z_livelist_dest`, at
`native_queued_spin_lock_slowpath+0x128/0x1e0`; CPU 33 is PID 2801, `mmp`, at
`native_queued_spin_lock_slowpath+0x63/0x1e0`. Their saved EFLAGS value is `0x2`
(IF clear). These are consistent with spin-wait contexts that lack ordinary
timer progress; they do not by themselves prove permanence or identify a lock
owner. Their register contexts differ, without identifying the lock objects or
their owners. No complete symbolic caller
frames follow the affected CPUs' `Call Trace:` headings in this excerpt, so
there is no proof of one shared lock, mutual wait cycle, or initiating ZFS bug.
The task names alone cannot provide that chain.

The earlier page-fault record and CPU 25 RCU stall make a benign isolated
watchdog artifact an unsupported classification. However, the earlier fault's
initiating task/stack is not retained here. Matching `CR2=0x3fe0` in later
register dumps is insufficient to assign fault causality or prove that the
watchdog caused it. The RCU kthread's scheduling stack is a third diagnostic;
it must not be substituted for the missing CPU 25/33 callers. Its text that
OOM is expected behavior is a starvation warning, not an observed OOM event.

## Recovery and panic-policy limits

The affected CPUs produced NMI diagnostics, and the collector received them.
That establishes some diagnostic execution/transport, not that local timer
interrupts resumed or either interrupted task left its spin loop. There is
no fresh normal-context CPU-bound event, recovery indication or meaningful
same-boot service interval after the reports in the supplied evidence.

Silence until a reboot establishes neither recovery nor uninterrupted failure.
The modern detector has suppression and silent rearm behavior, but the exact
2022 implementation/reset alternatives require the source owner's historical
check before using any such inference. Even if the modern logic happened to
match, these are warnings for different CPUs, not a repeated same-CPU warning
from which rearm could be inferred.

`Kdump: loaded` establishes that the diagnostic heading reported a loaded crash
image. It does not prove a panic, crash-kexec transfer, saved vmcore or successful
capture. The supplied context has no explicit panic/reset mechanism record.
A new ordinary Linux 5.10.149 boot after a 5.10.147.8 event does not prove which
operator or automatic recovery action occurred. Historical
`hardlockup_panic`, `panic_on_oops`, panic timeout and dump disposition remain
unknown; no 2026 defaults are projected backward.

For the user's policy question, this is a **retained real detector episode
with recovery unproven**, not evidence that a recoverable event would or would
not have been sacrificed by enabling panic. Its useful contribution is the
positive observation that the fleet's retained history contains hard-lockup
reports. Fleet frequency, the recoverable fraction and the policy's outage/dump
benefit require additional evidence and denominators; two CPU reports from one
episode cannot supply those quantities.

No additional remote query is necessary to give this bounded classification.
Evidence that could change it includes trustworthy same-boot service records,
affected-CPU ordinary progress, exact historical detector/config/module identity,
or reset/dump records. Any further collection remains the lead's and sole
collector's bounded decision. The session remains open.
