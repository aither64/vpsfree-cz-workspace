# Kernel group setup warning checkpoint

2026-11-04; architect0, read-only. One continued operation, handle 50754;
source `54b4313404cea35b58ebb9df951ae75e27c44971`. No new test or guest command.

**Recommendation: no change to the existing continuation direction.** Retain
the native timeouts and owner callback. The current warnings do not reproduce
the earlier `misc-attrs` LXC ESRCH and do not justify a configuration change.

Selection is intentional: `tests/suite/kernel/vpsadminos/common.nix:99–101`
enables the unstable line for its 6.18 contracts; `os/packages/linux/packages.nix:89`
selects the unstable default, currently 6.18.49 in `available-kernels.nix:5`.
The generated config records both guests using
`/nix/store/x64477x3mxlzqkmvijvakf33an9vcbrz-linux-6.18.49/bzImage`, initrd
`/nix/store/9j0cbhab4gvxvvcbx4kg4865drp45jfh-initrd/initrd`, eight CPUs,
8192 MiB, six shells and no extra QEMU options. The failed CI guest independently
reports Linux 6.18.49 and OS suffix `.git.54b4313` in its cgv2 diagnostics.
That establishes intended version selection, not complete VM/input equivalence.

The bounded current log read finds six scripts dispatched at 07:47:09 UTC,
without completed examples. `cgv2-shell4.log` begins a single setup command
at **07:49:28 UTC**: `mkdir -p "/run/osvm/shared-dir"`, with no completion in
that snapshot. Other cgv2 shell logs are empty. The guest console reaches a
prompt, then records RCU preempt grace-period/timer starvation and soft lockups
on CPU7 with `bash:1401` (44 through 190 guest seconds in the inspected range).
These are observed guest scheduling/progress problems. They do not identify
host contention, a kernel defect, resource insufficiency, a permanent deadlock,
or a causal relationship to the previous namespace-attach failure.

The exact setup chain is:

```text
ensure_kernel_machine
  -> wait_for_osctl_pool('tank')
  -> wait_for_boot -> Shell#wait
  -> test-shell-ready marker -> mount_shared_dir_once
  -> SharedDir#mount -> mkdir -p /run/osvm/shared-dir
  -> mount -t virtiofs vmSharedDir /run/osvm/shared-dir
```

Sources: `common.nix:127–130`, `osvm/lib/osvm/vpsadminos_machine.rb:27–46`,
`machine.rb:457–461,1211–1220`, `shell.rb:136–148`, `shared_dir.rb:41–46`.
The shared-directory lock serializes first mounting across shells. The logged
`mkdir` has not yet demonstrated completion; this is before pool polling and
container attribute assertions on that setup path.

The native CLI/machine default command timeout is **900 seconds**. `Shell#execute`
establishes its monotonic deadline and wraps waiting/locking/execution in
`Timeout.timeout` (`shell.rb:156–188,501–524`). The enclosing
`wait_for_osctl_pool` has a **20-minute budget including boot readiness**, then
probes with up to **60 seconds per command** within that budget. A subsequent
`wait_until_online` has its own **20-minute budget**. These are stage budgets,
not a single group deadline; wall-clock script-dispatch time alone does not
establish their exact monotonic start instants. The local command has no
workflow-level 350-minute step timeout.

RCU stalls and these soft-lockup messages do not match the existing fatal
kernel classifier (`machine.rb:9–17`); panics/oops and its other listed faults
do. The normal command/setup timeout still supplies a concrete failure outcome
if progress does not resume. Let the owner preserve that outcome and reconcile
the run. A setup timeout before assertions is **local verification blocked**,
not reproduction or resolution of the CI `misc-attrs` ESRCH.

No kernel/security/resource tweaks, cancellation, retry, source edit, evaluation,
build or further live observation is proposed by this checkpoint.
