# Upstream platform, watchdog and crash-progress audit

Owner: implementer4. Authorized upstream follow-up after the custom-phase gate.
Read-only source/configuration investigation, 2026-10-20; no build, test,
fetch/ref change, production operation or host-trust change.

## Outcome and evidence boundary

**Not supported:** no source-proven new host-wide loss-of-progress defect was
identified in the bounded NMI/APIC/TSC/watchdog, timer-broadcast, ACPI idle and
AMD PMU/pstate changes inspected below. This is not certification of the whole
stable range or exclusion of a hard lockup. There is no incident stack, dump or
reproduction that identifies the stalled CPU or progress dependency.

The missing crash upload is material evidence, but it does not establish that
Linux never panicked. The configured policy has **hardlockup panic disabled,
softlockup panic enabled**. A crash image was positively reported loaded about
26.5 minutes before logging stopped. Crash entry, successful transfer and the
subsequent capture/network/upload stages remain unobserved.

The user explicitly confirmed that sysctls are defined by the configuration and
vpsAdminOS repositories and that **there were no runtime changes**. The policy
values below therefore use the traced repository/default values as incident
values; lack of a live `/proc/sys` read does not leave those values unspecified.
This attestation does not supply a final kernel `.config`, module byte identity,
panic stack or proof of successful crash-kernel execution.

## Source and hardware identity

Stable comparison:
`296aabce459470a4c1b68ffd0c0c0920e563aaad` (6.12.95) to
`7fdb7c1824a1f9979d648d7ae28ac446bcee9c6e` (6.12.113).
Final source was checked at incident Linux
`1dfea587406b7dd79973831d1677fb2418e5e9aa`.
vpsAdminOS source is `2abbe3cc1c102a4b39022d3f73ef4a432ad4d616`.
Configuration source `177a9305f00d1755c66d170b4fa500d3ad18b6c2` has the matching
production input pair; its applicable configs/modules/node/environments/profiles
have no changes against inspected configuration HEAD `b748fb08`.
See [packaging audit](packaging-audit.md) for package patches, ancestry and
source-derived configuration gates.

The log owner's [hardware excerpts](node24-hardware-boot-excerpts.txt) establish
AMD EPYC 7H12, family `0x17`, model `0x31`, stepping 0; 128 processors activated;
x2APIC routing; TSC clocksource; and an enabled PMU-based NMI watchdog at the
October 19 boot. Microcode was reported as `0x0830107c`. The single startup
spurious LAPIC-timer message is not evidence of an incident interrupt fault.
Observed command-line selections include `nosmt`, `preempt=full`,
`amd_pstate=guided`, `intel_idle.max_cstate=1`, `crashkernel=4096M` and
`softlockup_panic=1`. Driver selection and timer/PMU state at the hang are not
fully reconstructed from these startup records.

## Exact panic/watchdog policy

The source-precedence check covered vpsAdminOS kernel/common-config, tunables,
defaults, imported Nixpkgs `kernel.nix`/`config/sysctl.nix`, crashdump integration,
and configuration configs/modules/cluster/environments/profiles. No applicable
sysctl assignment overrides the defaults below. The crashdump module explicitly
adds `softlockup_panic=1`. The observed full command line has no `nmi_watchdog`
panic/disable switch, watchdog threshold/disable switch, `panic=`,
`panic_on_warn`, `oops=panic` or `crash_kexec_post_notifiers` override.
`modules/system/serial-console.nix:29-35` contains `panic=-1` only inside its
enable condition; that inactive option must not be applied to node24 merely
because the definition exists.

| Value | Incident policy and exact source proof |
| --- | --- |
| `kernel.hardlockup_panic` | **0.** `kernel/watchdog.c:65-66` initializes it from `CONFIG_BOOTPARAM_HARDLOCKUP_PANIC`. This is an off-by-default boolean (`lib/Kconfig.debug:1204-1213`), absent from recipe/defconfig overrides; initial realized `.113` config has it unset and all relevant config-generation inputs are unchanged in the incident repin. No repository/sysctl or `nmi_watchdog=panic` override. |
| `kernel.softlockup_panic` | **1.** vpsAdminOS `os/modules/misc/crashdump.nix:416-419` adds the observed `softlockup_panic=1`; `kernel/watchdog.c:323-328` parses it. No later configured sysctl override. |
| `kernel.watchdog` | **1.** `watchdog_user_enabled = 1` at `kernel/watchdog.c:46`; no configured override/`nowatchdog`. |
| `kernel.nmi_watchdog` | **Enabled.** Boot explicitly says `NMI watchdog: Enabled. Permanently consumes one hw-PMU counter.`; no configured disabling override and user confirms no runtime changes. This does not measure whether NMIs still arrived at the failure. |
| `kernel.watchdog_thresh` | **10 seconds.** `kernel/watchdog.c:49`; no configured override. Softlockup threshold uses twice this value (`:540-542`). |
| `kernel.panic` | **0.** `kernel/panic.c:69` uses `CONFIG_PANIC_TIMEOUT`; normal recipe default and unchanged configuration lineage give 0, corroborated by the initial realized `.113` config. No configured/command-line override. This disables a subsequent automatic panic-timeout reboot; it does not disable the earlier kdump attempt. |
| `kernel.panic_on_warn` | **0.** zero-initialized `kernel/panic.c:62`, no configured override. |
| `kernel.panic_on_oops` | **0.** `kernel/panic.c:55` uses the off/default-zero `CONFIG_PANIC_ON_OOPS_VALUE`; initial realized config is 0 and configuration inputs are unchanged. No configured override. Fatal exceptions can still invoke crash handling through other conditions. |
| `kernel.panic_on_rcu_stall` | **0.** zero-initialized `kernel/rcu/tree_stall.h:20`, no configured override. Stall reporting alone does not imply panic. |
| `kernel.hung_task_panic` | **0.** `kernel/hung_task.c:76-77` uses off-by-default `CONFIG_BOOTPARAM_HUNG_TASK_PANIC`; initial config has it unset, no recipe/config override. Node source instead explicitly sets `kernel.hung_task_warnings = -1`. |
| `crash_kexec_post_notifiers` | **false.** zero-initialized `kernel/panic.c:61`; no configured/command-line override. Normal panic attempts crash kexec before later panic notifiers (`:417-426`). |
| crashdump enable/reservation | **Enabled, 4096M requested.** Configuration common `netboot.nix:105-107` enables `clusterconf.crashdump`, enables inspection and sets reserved memory. `modules/clusterconf/crashdump.nix:311-315` enables `boot.crashDump`; boot logs positively show reserved 4096 MB plus a low-memory reservation. Reservation alone would not prove an image was loaded. |

The off/default-zero Kconfig conclusions are source-derived configuration
conclusions, not an assertion that the initial local `.113` config is the
incident file. [Packaging audit](packaging-audit.md#upstream-phase-applicability-handoff)
records the unchanged Kconfig/defconfig/generator lineage and the distinction.

SPL policy was checked separately because it is a module parameter, not a
sysctl. Node24 imports `common/tunables-2t.nix`, which imports
`tunables-common.nix:16-19` and sets `spl_panic_halt = 1`.
vpsAdminOS's ZFS module forwards these settings both to modprobe configuration
and its `spl-module-parameters` service (`os/modules/tasks/filesystems/zfs/default.nix:870-873,943-946`).
At exact ZFS `481845fca6ae3f61ca2262c1a5693a58ae364650`,
`module/os/linux/spl/spl-err.c:67-68,102-103` calls Linux `panic()` when this
value is true. Only the false branch reaches the uninterruptible `schedule()`
loop. **Excluded within this configured scope:** deliberate assertion-thread
freezing through `spl_panic_halt=0`. No SPL assertion at this incident is proven.

## Why the missing upload does not locate the failure

The source has distinct stages; none can be inferred solely from a later stage
being absent:

1. The soft watchdog checks thread progress from its hrtimer callback. Its
   panic branch is `kernel/watchdog.c:769-771`. If that callback cannot execute,
   `softlockup_panic=1` does not independently force progress. The PMU NMI
   watchdog checks hrtimer progress, but at `:216-217` calls `nmi_panic()` only
   if `hardlockup_panic` is true. Under the configured zero policy, detecting a
   hard lockup can report it without entering panic/kdump. This is not evidence
   that a hard lockup happened.
2. `panic()` elects a single CPU, performs initial printing/debug handling and
   attempts `__crash_kexec` (`kernel/panic.c:383-426`). In
   `kernel/crash_core.c:105-125`, the crash attempt needs a non-null
   `kexec_crash_image` and successful **nonblocking** `kexec_trylock`; otherwise
   it returns. This existing fallback is not a newly demonstrated regression.
3. The x86 crash path stops other CPUs, disables virtualization/APIC state and
   transfers into the crash image (`arch/x86/kernel/crash.c:99-143`,
   `kernel/crash_core.c:119-122`). Source inspection does not show that this
   transition completed during the incident.
4. Configuration's default destination is NFS. The crash script mounts its
   destination before creating the target directory and saving metadata
   (`modules/clusterconf/crashdump.nix:101-112,315-376`); inspection and optional
   memory collection happen later. Crash-kernel boot, device/network setup or
   capture/upload can therefore fail before any uploaded crashinfo appears.
   No such failure has been observed here.

There is now stronger positive pre-incident evidence than reservation:
`log:1279760` at `18:31:57.333383+02:00` and `:1279973` at
`18:31:59.183362+02:00` report **`Kdump: loaded` on 6.12.113**.
`lib/dump_stack.c:62` prints this marker only when `kexec_crash_loaded()` is
true; `kernel/crash_core.c:94-96` tests `kexec_crash_image`.
See [crash-state excerpts](node24-crash-state-excerpts.txt) and the log owner's
coverage limits. This proves an image was present about 26.5 minutes before
the final log; it is not byte attestation or proof of later execution.
Bounded initial/recovery scans found no explicit loader/upload result, and the
loader's successful return has no explicit success echo
(`os/modules/misc/crashdump.nix:480-497`). Missing forwarded output must not be
converted into proof of failure or success.

## Bounded upstream source findings

| Examined area | Source result and applicability limit |
| --- | --- |
| NMI/APIC/TSC/watchdogs | No stable-range source delta in `arch/x86/kernel/nmi.c`, `arch/x86/kernel/apic`, `arch/x86/kernel/tsc.c`, `arch/x86/kernel/time.c`, `kernel/watchdog.c`, `kernel/watchdog_perf.c`; also no delta in hrtimer/timer-migration files. This excludes a new direct edit in these files, not a failure entering through their callers. |
| Panic/crash transfer | `kernel/crash_core.c`, `kexec_core.c`, x86 `crash.c`, `machine_kexec_64.c`, `reboot.c`, `smp.c` have no stable-range delta. `panic.c` adds ownership-query APIs; its existing `panic()`/crash-attempt control flow is unchanged. Broader printk/driver behavior is not certified by that result. |
| Timer-broadcast replacement | `kernel/time/tick-broadcast.c:163-211` newly serializes replacement under `tick_broadcast_lock`. Direct registration caller holds `clockevents_lock` (`clockevents.c:461-465`): order is clockevents then broadcast. Replacement detaches/shuts devices under that lock, releases it before the old broadcast provider's `module_put` and before oneshot switching. Immediate broadcast handlers/control paths use the broadcast lock without a demonstrated reverse acquisition of `clockevents_lock`. No concrete lock cycle or new wait-for-CPU loop was found in the inspected path. |
| Other timer changes | Clocksource sysfs change is init/error cleanup; jiffies registration and initial clock enable changes are boot-time. Tick idle accounting bounds negative deltas; NTP adjustment updates error accounting; `timer.c` adds debug activation on migration. No source-proven host-wide progress failure found. CPU-time-timer/scheduler semantics remain with the architect. |
| ACPI idle | `processor_idle.c` moves driver registration before per-processor device registration; `processor_driver.c` wires matching init/error/unregister paths. LPI changes add package bounds checks and idle annotations. No source-proven lost wakeup, reference failure or lock cycle found in these changes. Actual idle driver/state use is not recovered. On this AMD CPU, the `intel_idle.max_cstate` argument alone must not be treated as a bound on ACPI idle states: `intel_idle_init()` matches Intel-specific CPU tables before registering. |
| AMD PMU | Checked changed `arch/x86/events/amd/{core,brs,ibs,lbr,uncore}.c` and immediate NMI-window use. Moving `perf_nmi_window` initialization before a feature early-return changes claiming of delayed PMU NMIs; `amd_pmu_adjust_nmi_window():874-889` compares timestamps and does not wait. Other changed paths cover branch filtering, callback arguments, event/group/topology validation and PMUv2 register reload. No new concrete unbounded-progress chain established; branch/uncore/IBS event use is not proved by the watchdog's boot message. |
| AMD pstate/CPU/MCE | pstate changes move boost-ratio validation and preserve per-core ranking; their error returns/initialization do not demonstrate a host hang. The added Zen5 CPU model range is inapplicable to observed family 0x17. MCE changes move debug-register save/restore and complete initialization before enabling machine checks; no newly introduced wait was found. Intel microcode/Intel PMU changes are outside this AMD applicability scope. |
| BPF IBPB/Safe-RET | These security changes occur in the stable range but are already present in old v6 cumulative source. Inventory owner mapped BPF IBPB backport `209fc038` to stable `9354248f`, Safe-RET backport `71fce134` to stable `e262f28a` plus v6 adaptation owners. See [upstream provenance](upstream-provenance.md). Stable-range membership alone does not establish a newly introduced upgrade regression or actual old module coverage. |

No later-fix match or controlled old/new/fix comparison was established in this
lane. No generic passing test would resolve the missing incident trigger.
Useful discriminating evidence is a panic/NMI/CPU stack, proof of whether the
crash kernel entered and where capture stopped, or a source-specific isolated
reproduction once a concrete mechanism exists. This investigation does not
authorize changing watchdog policy, forcing a crash or modifying capture setup.
