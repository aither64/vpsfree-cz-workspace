# Hard-lockup reporting, continued operation and recovery

Bounded read-only follow-up by implementer4, 2026-10-20. Session/environment and
same-session roster verified before writing. Exact source:
Linux `1dfea587406b7dd79973831d1677fb2418e5e9aa` (incident 6.12.113).
No configuration change, forced hang, test/build, fetch or production mutation.
Cluster-log searches belong to implementer1; this record makes no claim that
recoverable reports or false positives have occurred in the cluster.

## Direct source conclusion

**A reported hard lockup need not be permanent.** With `hardlockup_panic=0`,
the reporting function can return normally and interrupted execution can resume.
The detector does not repair the stall, force progress or prove future recovery.
A finite stall may end; an actual permanent stall may remain stuck.
With `hardlockup_panic=1` from the start, the first accepted report requests
panic even if the underlying stall would eventually have cleared. This is not
an escalation after multiple failed reports.

`kernel/watchdog.c:131-223` implements these states:

| Observation/state | Behavior |
| --- | --- |
| Hrtimer heartbeat counter advanced | `is_hardlockup()` saves the new counter and returns false; the check clears the per-CPU `watchdog_hardlockup_warned` flag. No recovery message is printed. |
| No heartbeat advance, CPU not already warned | Print the hard-lockup message, collect diagnostics, then call `nmi_panic()` only if the panic switch is true. On the nonpanic return path, set the per-CPU warning flag true. |
| No heartbeat advance, CPU already warned | Return before printing, stack collection **and** the panic check. This suppresses repeated reports during the same failed-heartbeat episode. |
| Explicit watchdog touch | Clear the touched flag and skip this sample; this branch does not itself clear the warning flag or prove recovery. |

The PMU callback resets its interrupt-throttling counter, applies timestamp
filtering and invokes the per-CPU check (`kernel/watchdog_perf.c:104-116`).
Filtering and the optional all-CPU-backtrace serialization gate can also skip
a sample before a report is accepted.

Counterfactual `panic=1` must therefore be stated precisely. If it was enabled
at the first accepted report and the diagnostic path completes, that report
would invoke panic, including a report of a later-recoverable stall. Changing
the switch after `warned=true` does not retroactively panic an already
suppressed episode. A healthy heartbeat check must rearm it before a new
accepted report takes that branch. No setting was changed in this investigation.

## Diagnostic output can affect progress

The report is printed **before** acquiring the printk CPU synchronization lock
(`watchdog.c:183-196`). The adjacent source comment explicitly aims to retain
at least that message if another CPU locked up holding the synchronization lock.
`include/linux/printk.h:338-366` and
`kernel/printk/printk.c:5129-5133` show that acquisition can spin waiting for
another CPU to release ownership. Stack/backtrace collection also precedes
the conditional `nmi_panic()` at `watchdog.c:216-217`.
Thus a printed warning does not prove that diagnostics completed, the detector
returned, panic was reached, or a crash image executed. This is a pre-existing
progress dependency, not a newly demonstrated regression or incident cause.

## Timing and false-positive limits

The check observes a missing timer heartbeat around the configured watchdog
interval, not a proof that a CPU can never make progress again. A genuine but
finite period without local timer interrupts is distinct from a detector false
positive; both matter when evaluating a policy that panics on first detection.

`watchdog_perf.c:34-63` explicitly documents one timing false-positive mechanism:
the PMU counts unhalted CPU cycles, so frequency boost can deliver NMIs earlier
than expected relative to the hrtimer. Its timestamp filter enforces a minimum
sample interval to mitigate this. `watchdog.c:68-73` also recognizes hypervisor
guest contexts where hard detection may be disabled by default. These source
comments describe mechanisms/mitigations, not evidence of cluster events or
evidence that the node24 report was a false positive. The detection intervals
remain approximate rather than exact wall-clock promises.

## Log signatures and recovery evidence

The exact incident source combines `pr_fmt("watchdog: ...")` at
`kernel/watchdog.c:13` with the format at `:194`:

```text
watchdog: Watchdog detected hard LOCKUP on cpu <number>
```

The same two detector files have no difference between compared boot trees
6.12.95 `a2384967b90f24d2470c9eb15f0e66d938df7e08` and 6.12.113
`1dfea587`; the stable-boundary comparison is also empty for those files.
This does not establish every historical livepatch's loaded function identity.
An older local `v4.19` tag resolves to `84df9525b0c27f3ebc2ebb1864fa62a97fdedb7d`,
but its watchdog source blob was unavailable under the required no-lazy-fetch
read. No historical source was fetched, and no exact older-version signature
or reset logic is asserted here. Case-insensitive searches for `hard LOCKUP`
and `hardlockup` avoid requiring the current prefix, but any historical match
needs its own version/policy interpretation.

| Historical observation | What it establishes |
| --- | --- |
| Later logs in the same boot | Some logging/CPU/transport paths operated; this alone does not prove the reported CPU resumed. |
| No subsequent hard-lockup message | Ambiguous: silent suppression and silent recovery are both possible. |
| A later **new report for the same CPU**, same checked reset logic, with no boot/reinitialization ambiguity | The warning state was rearmed through a healthy heartbeat check between accepted reports. This proves sampled heartbeat progress, not complete workload health. Do not apply this inference to an unexamined older detector implementation. |
| Later trustworthy execution/progress evidence attributed to the reported CPU | Evidence that this CPU resumed at that time, with strength depending on the measurement. |
| Continued uptime and successful representative services | Evidence of operational survival; it need not prove every CPU or workload was healthy. |

The source alone cannot estimate how many cluster events a panic policy would
have converted into outages. Keep the actual event records, boot continuity,
kernel/panic policy and recovery evidence separate. All-CPU backtraces are a
diagnostic path that exists independently of panic, but collection itself has
progress costs and is not a configuration change recommended or performed here.
