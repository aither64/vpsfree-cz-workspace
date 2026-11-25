# AMD scale-aged v5: first evidence handoff

Exact head `846bb469505789ba0b2a405fa5905ba6d8253006`, existing CI
[39767770407](https://github.com/vpsfreecz/vpsadminos/actions/runs/39767770407),
attempt1, job119793311416. The same sole watcher captured this new failure's
available artifacts20:44:01–13Z. Download exited0; per-job log retrieval exited1
because GitHub withholds it until the whole run completes. Original evidence
is retained unchanged; no new test, retry, cancellation or observer ran.

Test: `kernel/livepatch-qualification@amd-scale-aged-v5`.
Native result: `unexpected_failure`. One example fails at20:35:17Z after
16629.89s; runner starts15:57:03Z and finishes20:35:51Z after16728.08s.
API job start from the earlier bounded metadata receipt is15:54:58Z; active
test step starts15:55:02Z. These are separate clocks/stages, not a single
elapsed measurement. Guest exits naturally with QEMU status0 at20:35:51Z.

First assertion is the no-kernel-fault dmesg check; exact matching events in
`test-runner.log:138,189` are:

```text
[14822.947301] rcu: INFO: rcu_preempt self-detected stall on CPU
[14823.741817] rcu: INFO: rcu_preempt detected expedited stalls on CPUs/tasks: { 114-.... } 21202 jiffies s: 84857 root: 0x80/.
```

Lead additionally read CPU114, kernel6.12.95.5 and `Comm: insmod` from the
same preserved excerpt. This is a distinct RCU-stall signature from the v6
CPU127 scheduler-hotplug warning. No root cause, source repair, current-feature
relation or harmlessness conclusion is selected by this handoff.

Evidence root:
`generic-sysctl-ci-39767770407-600s-detail-failure-119793311416/artifacts/os-test-logs-39767770407-1-livepatch-amd-scale-aged-v5/`.
Case directory:
`os-test-kernel__livepatch-qualification__amd-scale-aged-v5-cb9686d6/`.
It retains `test-runner.log`, `test-result.txt`, console/shell/machine/failure
diagnostics and the parent `test.log`. The earlier raw job metadata is
`generic-sysctl-ci-39767770407-duration-jobs.json` at20:32:57Z.

[Shared first-failure note](generic-sysctl-ci-failure.md) records this later
failure separately from the merge's accepted exceptions. This artifact is
available for the separately assigned investigation to read; it is not a
claim of delivery to another session's lead. This session retains only the
original run's remaining two AMD jobs under the same600s observer. No further
root-cause investigation, Git/source change, revert or lifecycle action occurs.


Terminal update: original run39767770407 completed with failure at
2026-10-23T01:14:16Z; all 11 jobs are terminal (eight succeeded, three failed).
The v5 result above is unchanged. Full terminal job log is now available at
`generic-sysctl-ci-39767770407-terminal-failure-amd-scale-aged-v5/job.log`;
the corresponding native artifact is also retained at
`generic-sysctl-ci-39767770407-terminal-artifact-livepatch-amd-scale-aged-v5/files/`.
The original first evidence remains intact. Same watcher returned, exact watch
exit1/CLI exit0, with no active observer. No deeper diagnosis or rerun followed.
