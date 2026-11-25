# Watchdog policy history

Bounded read-only follow-up by implementer4, 2026-10-20. Session/environment
identity reverified. No source, configuration, ref or production change.

## Introduction and rationale

The incident-ancestor history introduces `softlockup_panic=1` in vpsAdminOS
commit `5e7a0d7af5bd92fb8ac11778ed570d5cc32400ee`, **2022-05-21**
(author 16:08:11 +02:00; commit 16:10:00 +02:00), by Pavel Snajdr:

> os: kernel crashDump dmesg extraction

It adds `os/modules/misc/crashdump.nix` as a new file. Under enabled crashdump,
the original module adds `crashkernel=...` and `softlockup_panic=1` together.
The only commit-message body is a Signed-off-by line; it does not explain why
the soft detector panics while the hard detector retains its default.

`git log --follow -Ssoftlockup_panic 2abbe3cc -- os/modules/misc/crashdump.nix`
finds that introduction, without a later policy change in the incident lineage.
Bounded incident-ancestor history searches found no explicit hard-panic override
or documented comparison rationale in the applicable vpsAdminOS OS modules/kernel
configuration or configuration-repository configs/modules/cluster/environments/
profiles. Current project documentation adds no such explanation.

The introducing option description retains NixOS/systemd wording and says the
option activates the NMI watchdog. Neither the commit nor file explicitly
attributes copied source. That wording alone does not prove historical NixOS
provenance or a deliberate reason to omit hard-lockup panic.

**Historical reason for leaving hard-lockup panic at zero: undocumented/unknown
in the examined evidence.** The supported statement is that soft panic was
explicitly enabled with crashdump in 2022, while hard panic retains the kernel
default. Do not recast the missing override as an intentional recorded tradeoff.

## Detector terminology checked against the incident source

At Linux `1dfea587`, `kernel/watchdog.c:658-700` uses a per-CPU hrtimer to queue
`softlockup_fn` through `stop_one_cpu_nowait`; that scheduled CPU-stop work
updates the progress timestamp. A soft lockup means this work cannot run for
roughly `2 * watchdog_thresh`, **about 20 seconds** at the configured threshold
10, while the timer callback can still execute and detect the starvation.
It is kernel watchdog work, not the userspace crashdump service or merely one
ordinary blocked application.

The PMU NMI callback (`kernel/watchdog_perf.c:104-116`) calls the hard-lockup
check. `kernel/watchdog.c:131-150` compares the local hrtimer heartbeat counter
and increments that counter from the hrtimer. Missing heartbeat progress is
checked on the **roughly 10-second** hard-watchdog interval; timestamp filters,
sampling and watchdog touches mean these are approximate detection intervals.

The panic switches control the respective detector's response independently;
soft detection does not escalate into hard detection. Exact configured values
and the no-runtime-changes user attestation remain in
[upstream-platform-audit.md](upstream-platform-audit.md).
