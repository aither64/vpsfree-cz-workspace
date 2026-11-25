# node24.prg central-log evidence

Collected on 2026-10-20 by implementer1 using read-only SSH queries as
`root@log.int.prg.vpsfree.cz`. No production state, services, kernel settings,
or workloads were changed. Session identity and both environment markers were
verified before collection. This is an incident evidence record, not a cause
determination.

## Sources and time interpretation

Node directory: `/var/log/remote/cz.vpsfree/nodes/prg/node24/` on the central
log server. `log` contains October 20; `log-20261020` contains October 19.
The rotation suffix is the rotation date, not the date of all contained events.
Reported timestamps below retain the log's `+02:00` offset (CEST).
Line references are one-based and refer to these files as read on October 20.
The current `log` is append-only during collection, so its earlier line numbers
were stable in repeated queries. Boot messages are buffered/replayed in groups
and some appear twice; their central timestamps establish the observed boot
output, not the exact moment firmware or the kernel started.

## Incident boundary

The full October 20 log scan found a single gap over 30 seconds before recovery:

| Boundary | Source | Timestamp | Evidence |
| --- | --- | --- | --- |
| Last host control message shown before the gap | `log:1309599` | `2026-10-20T18:58:24.708409+02:00` | osctld received `netif_list` |
| Last message of any kind before the gap | `log:1309622` | `2026-10-20T18:58:26.658330+02:00` | container-tagged kernel network log |
| Next message | `log:1309623` | `2026-10-20T19:12:04.761663+02:00` | `Linux version 6.12.113 ...` |

The timestamp difference is **818.103333 seconds (13m 38.103333s)**.
This bounds the observed loss of node24 logging and subsequent recovery boot.
It does not independently establish when an operator noticed the unresponsive
console, the reset time, or whether every missing event was lost at the node
rather than in transport. Immediately before the gap, an SSH health check
completed at 18:58:24.572631, and osctld answered control traffic at 18:58:24.
No graceful host shutdown appeared in that final displayed context.

The collector received neighboring-node messages during the node24 gap:

| Node | Continuity timestamps |
| --- | --- |
| node23 | `18:58:27.039839+02:00`, `19:00:00.136563+02:00` |
| node25 | `18:58:27.022717+02:00`, `19:00:00.022138+02:00` |

This rules out a complete collector outage at those sampled moments. It does
not rule out loss of node24's logging connection or network path.

## Deployed kernel and system

`log-20261020:213372` records the first observed 6.12.113 boot on October 19:

```text
2026-10-19T02:19:43.503662+02:00 ... kernel Linux version 6.12.113 (nixbld@localhost) (gcc (GCC) 15.3.0, GNU ld (GNU Binutils) 2.46) #1-vpsAdminOS SMP PREEMPT_DYNAMIC Sun Oct 18 17:47:47 UTC 2026
```

`log-20261020:215497-215498` explicitly identify the system revision:

```text
2026-10-19T02:19:43.506855+02:00 ... kernel input vpsadminos=2abbe3cc
2026-10-19T02:19:43.506855+02:00 ... kernel vpsAdminOS 26.05.git.2abbe3c with kernel 6.12.113
```

A later bounded query of adjacent boot records (`:215450–215530`) also found
`input nixpkgs=26f4107e` at line 215495 and `input vpsadmin=ff730be4` at line
215496, both timestamped `2026-10-19T02:19:43.506854+02:00`. That range contains
no configuration-revision input. These are boot input labels, with package
resolution and loaded-byte identity owned by the packaging audit.

The October 19 boot command line and October 20 recovery command line both
point to boot generation **144** and the same system init:

```text
/nix/store/39yak5qzbm4fya40zg8nw4za6x8k3xir-vpsadminos-system-node24.prg.vpsfree.cz-26.05.git.2abbe3c/init
```

The recovery boot repeats the same 6.12.113 build timestamp. Relevant command
line settings include `preempt=full`, `crashkernel=4096M`,
`softlockup_panic=1`, `cgroup.memory=nokmem`, `nosmt`,
`amd_pstate=guided`, and `intel_idle.max_cstate=1`. The source provenance owner
maps vpsAdminOS `2abbe3cc` to Linux
`1dfea587406b7dd79973831d1677fb2418e5e9aa` (reported by the lead's provenance
lane; source proof belongs in its provenance record). That is the later of the
two 6.12.113 candidates, after proactive-swap/DAMON retirement. The kernel
version number alone cannot distinguish those candidates.

These are **boot-log observations**, including the pre-hang deployment boot and
the recovery boot. Direct inspection of the current recovery runtime was
blocked: `root@node24.prg.vpsfree.cz` failed host-key verification; the alternate
short name `node24.prg` did not resolve. Host trust was preserved. Consequently
no `uname`, booted/current-system symlink, kernel store derivation, running
configuration, or livepatch sysfs/module evidence was retrieved from node24.

## Earlier diagnostics that must not be attributed to the later hang

On October 19 at 02:15:51, before the 02:19 upgrade boot, three tasks in one
container were reported blocked for over 122 seconds. All three reports state
**6.12.95.6**, not 6.12.113 (`log-20261020:212839-212959`). They wait through
`folio_wait_writeback`, `filemap_write_and_wait_range`, `nfs_wb_all`,
`nfs_file_flush`, and close/exit paths. At 02:16:32 the kernel reports an NFS
server not responding. Host SSH health checks and osctld traffic still continued
at 02:16. These are evidence of an earlier NFS problem during the old-kernel
period and do not prove a cause for the October 20 machine hang.

## Console driver evidence

The pre-hang deployment's October 19 boot records:

```text
log-20261020:214109:2026-10-19T02:19:43.504366+02:00 ... kernel Console: colour VGA+ 80x25
log-20261020:214110:2026-10-19T02:19:43.504366+02:00 ... kernel printk: legacy console [tty0] enabled
log-20261020:214812:2026-10-19T02:19:43.505552+02:00 ... kernel pci 0000:62:00.0: vgaarb: setting as boot VGA device
```

A bounded boot-range search (`log-20261020:213372-216000`) found no fbcon,
simpledrm or AST takeover message. This establishes VGA text console at early
boot; it is not live proof of the console driver at the incident. The architect
owns the source-based interpretation of cursor blinking. Blinking alone should
not be used to classify scheduler/interrupt progress or rule out a CPU lockup.

## Boot CPU, APIC, clocksource and watchdog evidence

A later source-directed query stayed within the original deployment boot range
`log-20261020:213372–216000`. It establishes actual boot CPU identity rather
than inferring it from configuration. [Selected raw records](node24-hardware-boot-excerpts.txt)
retain the exact messages and timestamps; all are October 19 at 02:19:43 CEST
in the buffered boot output.

| Source line | Exact diagnostic fact |
| --- | --- |
| `:214170` | `smpboot: CPU0: AMD EPYC 7H12 64-Core Processor (family: 0x17, model: 0x31, stepping: 0x0)` |
| `:214232` | `smpboot: Total of 128 processors activated (664348.16 BogoMIPS)` |
| `:213601` | `x2apic: enabled by BIOS, switching to x2apic ops` |
| `:213812` | `APIC: Switched APIC routing to: cluster x2apic` |
| `:214274` | `ACPI: Using IOAPIC for interrupt routing` |
| `:214108` | `Spurious LAPIC timer interrupt on cpu 0` (startup message) |
| `:214193` | `NMI watchdog: Enabled. Permanently consumes one hw-PMU counter.` |
| `:215305` | `microcode: Current revision: 0x0830107c` |
| `:215306` | `microcode: Updated early from: 0x0830107c` (literal recorded value) |
| `:215337` | `tsc: Refined TSC clocksource calibration: 2595.125 MHz` |
| `:215339` | `clocksource: Switched to clocksource tsc` |

These identify the boot platform and startup selections. They do not establish
the APIC, clocksource or watchdog state at the later incident, and the startup
spurious-interrupt message alone does not establish an interrupt fault during
the hang. CPU-family, microcode and NMI/idle code applicability are owned by
the platform investigator. No new runtime access or hardware probe was made.

## Diagnostics before the gap

A completed scan covered **2,717,608 kernel log records** from the observed
October 19 02:19:43 upgrade boot through October 20 18:58:26. Patterns covered
RCU stall/starvation, soft and hard lockups, blocked tasks, kernel
BUG/WARNING/Oops/panic, allocation failures and global OOM, block/NVMe/ATA/ZFS
errors, hardware errors, memory-cgroup OOM and NFS timeouts. Results:

| Diagnostic | Observed result |
| --- | --- |
| RCU stalls/starvation; soft/hard lockups; blocked tasks | No matching records |
| Kernel BUG/WARNING/Oops/panic | No matching records after the upgrade boot |
| Host OOM or page-allocation failure | No matching records |
| I/O/block errors; NVMe timeout/reset/error; ATA failure/error; ZFS fault/suspend; hardware error | No matching records |
| Memory-cgroup OOM | 174 `CONSTRAINT_MEMCG` records; first October 19 05:57:00, last October 20 18:31:59.186442 |
| NFS server not responding | 21 records; first October 20 06:43:51, last **18:58:18.238314**, 8.420016 seconds before the final log |
| Userspace general-protection faults | Container-tagged faults occur, including php-fpm7.4 in `mysqli.so` at 18:47:53 and 18:50:50; these are not kernel Oops reports |

The final NFS timeout is `log:1309459`, tagged container `19770-7a95`, naming
server `172.16.129.141`. It is an observed adjacent symptom with **no verified
causal link** to the machine hang. A bounded final-context check reproduced it
and the boundary lines; see [selected excerpts](node24-log-excerpts.txt). The
latest cgroup OOM preceded the gap by over 26 minutes and does not establish
global host memory exhaustion. No non-kernel daemon record matching
error/warn/fail/timeout/unresponsive/pressure/panic appeared from 18:45 through
the gap. Host control and SSH health-check traffic still completed afterward.

## Coverage limits

Missing forwarded diagnostics do not prove that a corresponding failure could
not have occurred: a hang can prevent logging, transport or storage may lose
events, and these are text-pattern checks rather than full telemetry analysis.
The incident has no captured panic/backtrace, RCU stall, lockup stack, crash dump
or live runtime inspection in this evidence package. The logged
`softlockup_panic=1` and `crashkernel=4096M` settings do not prove that a watchdog
fired or that a dump exists. The log gap is an observation, not proof of a
specific CPU, scheduler, memory, storage or network mechanism.

No cause is claimed. The source audit must supply an obvious failure mechanism
or a controlled verification before naming a custom patch as causal. No code,
configuration or deployment changed, so compatibility, migration and rollback
behavior are unaffected. Automated change review does not apply to this
investigation/evidence record alone.

## Crash-image state and crash-upload follow-up

At the lead's request, targeted queries checked the original deployment boot
(`log-20261020:213372–300000`), recovery boot (`log:1309623–1405000`), and the
already identified last pre-incident memory-cgroup OOM records
(`log:1279759–1280154`). The latter provide **positive loaded-image evidence**:

| Source | Timestamp (October 20, CEST) | Kernel record |
| --- | --- | --- |
| `log:1279760` | `18:31:57.333383` | `Comm: ib_io_rd-1 Kdump: loaded Not tainted 6.12.113 #1-vpsAdminOS` |
| `log:1279973` | `18:31:59.183362` | `Comm: containerd Kdump: loaded Not tainted 6.12.113 #1-vpsAdminOS` |

[Exact selected records](node24-crash-state-excerpts.txt) retain both lines.
This marker is distinct from reserved crash memory: at incident Linux
`1dfea587406b7dd79973831d1677fb2418e5e9aa`, `lib/dump_stack.c:62` prints
`Kdump: loaded` only when `kexec_crash_loaded()` is true;
`kernel/crash_core.c:94–96` implements that as `!!kexec_crash_image`.
Thus the running kernel reported a non-null crash image about 26½ minutes
before logging stopped. This does not identify that image's bytes or parameters,
prove it remained loaded at the hang, or establish that crash execution,
capture or upload subsequently succeeded.

The two boot ranges contain the command-line reservation plus low/high memory
reservation messages: original `:213834–213835` (256 MiB low, 4096 MiB high),
recovery `:1310161–1310162` (same sizes). They contain no forwarded explicit
kexec/kdump loader result, `crashinfo`, crash-upload or `vmcore` output in the
checked patterns. A supplementary `crashdump`/`savecore`/`makedumpfile` search
only found pstore compression setup and a megaraid firmware crash-dump
capability message; those do not establish host crash-image loading or upload.

The packaging owner supplied the exact loader strings from the incident OS:
`params=$crashdumpParams`, then `kexec --load-panic`, with failure text
`Unable to load crashdump kernel, kexec failed with $rc`, and no explicit
success echo. Additional queries of the same two boot ranges found zero matches
for that failure text, `kexec ... --load-panic`, or `params=` records containing
the crash/boot parameter signatures. Parameters alone would not prove success.
Missing forwarded records do not prove that the service did not run, nor that
loading/upload succeeded or failed. The positive pre-incident kernel markers
are the loaded-state evidence; they do not explain the reported lack of a
crashkernel boot/upload. No production, runtime, sysctl or trust changes were
made, and no broader historical scan was performed.

## Targeted RPC transport applicability follow-up

At the lead's request, a later bounded check looked for applicability of the
NFS owner's RPC TLS cancellation candidate. It does not establish a defect.
The October 19 startup context identifies container 19770 auto-starting at
02:29:19 (`log-20261020:273251`) and reaching RUNNING at 02:30:35 (`:277212`).
Host `zfs mount tank/ct/19770` messages describe the container filesystem, not
its guest NFS transport. At `:277397` the kernel reports:

```text
2026-10-19T02:30:40.697313+02:00 ... kernel [ 19770-7a95 ] new mount options do not match the existing superblock, will be ignored
```

The options are not printed, so this warning cannot identify the transport or
security mode. A complete, uncapped discriminator check of boot/startup lines
`log-20261020:213372–280000` and pre-gap lines `log:1285000–1309622` found zero
matches for the following literal signatures/patterns supplied by the NFS lane:

- `xprtsec=tls` / `xprtsec=mtls`;
- `proto=rdma` or a mount helper command with `-o ... rdma`;
- `tlshd`, `xs_tls_handshake_sync`, `xs_tcp_tls_setup_socket`, or a handshake
  cancellation message;
- pNFS, layout-driver or data-server messages.

**Actual NFS transport, TLS mode and pNFS use remain unknown.** The bounded
absence does not establish that any feature was disabled or unused; container
service startup and mount options need not be forwarded to these host logs.
NFS version 4.1/4.2 alone would not establish pNFS, and `sec=krb5*`/GSS would
not establish transport TLS. No trusted live mount options were obtained and
no runtime/trust changes or additional broad scans were made. Configuration
applicability remains with implementer4; source mechanics remain with
implementer3.

## Reproduction of key read-only queries

On the central log server, with `node24` set to the directory above:

```sh
grep -nE 'Linux version|kernel input vpsadminos=|kernel vpsAdminOS' "$node24/log-20261020" "$node24/log"
awk '{t=substr($0,12,2)*3600+substr($0,15,2)*60+substr($0,18,2); if(NR>1 && t-p>30) print "GAP seconds=" t-p, "before_line=" NR-1, pt, "after_line=" NR, substr($0,1,32); p=t;pt=substr($0,1,32)}' "$node24/log"
```

The gap query uses the same-day timestamp components and is appropriate to the
October 20 `log` file. Remote `rg` was unavailable, so queries used grep/awk.
Default SSH user `aither` was denied; the authorized `root` identity worked.
The multi-pattern awk aggregate was unexpectedly CPU-expensive (about two
minutes on one log-server CPU) and completed before an attempted cancellation
found it gone. Do not repeat that broad scan for this package; narrower grep
queries and incident-adjacent line ranges were fast and sufficient to reproduce
the key evidence. An initial broad `swap.*fail` pattern also matched ordinary
`memory+swap ... failcnt` lines; those matches were excluded from conclusions
and do not indicate proactive-swap activity.
