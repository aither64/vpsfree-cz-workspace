# Candidate export boot lockup

The export attempt stalled before a guest shell, pool readiness or candidate
container startup. It does not invalidate the complete primary image run at
`aa963dce42859ae4251cdfaded91920d67b3a46e` (15/15 guest tests passed).
No candidate archive was exported. Successful primary logs are separately
preserved in `successful-leap-16.0-{test-runner,machine-shell,machine-console}.log`.

## Bounded evidence and limits

The [watcher result](candidate-extract-result.md) reconciles normal native exit
after interrupting the blocked readiness call. Exact script/runner/QEMU PIDs
1347506/1347520/1352555 are gone; the run directory and 10 GiB data disk remain.
The implementer's process reads found no QEMU for this exact state by either
absolute argv or CWD; no process was controlled by the implementer.

Preserved [console](export-lockup-console.log), SHA256
`b373a4799f194ed0b751e41f7eb59ac55bbcd11337438fbe583e36d18d437096`,
contains all four CPUs stuck for 22, 48, 74 and 100 seconds at guest time
425–509s. Tasks are three `kworker/u16` threads and `pgdatinit0`. It contains
**no kernel stack traces, instruction pointers or register dumps**; exact
KVM/kernel failure attribution is unavailable. The shell log was empty at
inspection. [Startup/shutdown log](export-lockup-startup.log), SHA256
`ffcfda3395ed66385c17b8ba19f12807cb9ee1d848a8a5633ce5f569b4a3d80a`,
preserves this failed export's native operation.

The existing native config JSON is
`/nix/store/bcgp7x7g4ky97a2zjbqr1yskby4h4dvy-os-test-image-scripts-test-opensuse-leap-16.1.json`,
matching the passing primary. It declares 24576 MiB RAM and four vCPUs, kernel
`/nix/store/b043pwyanxjfz22hbiibv5wipqqcl932-linux-6.12.113/bzImage`, initrd
`/nix/store/p1a2p526kvg1zsz7j5wwmg68i9m1z2zm-initrd/initrd`, QEMU
`/nix/store/kanckc6ljipqzjsrvj4aqaf87a4rhswr-qemu-host-cpu-only-for-vm-tests-10.2.4`,
and squashfs `/nix/store/9q2lb2sn2jm7zqkz3kl82rigdycfpjz9-squashfs.img`.
The candidate filesystem is merely data on the retained disk at this point.

A single host snapshot at 19:57:19 +0100 measured 41141 MiB available RAM,
11728 MiB free `/dev/shm`, load 19.24 on the stated 64 CPUs, CPU PSI avg10
0.10%, memory PSI 0.25% and IO PSI 1.60%. These near/after-stop measurements
do not prove resource conditions during the lockup or sustained CPU starvation.
OsVm uses `/dev/shm` for the virtiofs shared guest RAM backend. The measured
shared-memory headroom is below another 24 GiB VM's requirement and supports
reducing this helper's size; it does not prove the lockup's root cause.

The supported conclusion is an early vpsAdminOS guest-boot/environment failure,
not an observed candidate-image failure. Do not call it proven random, a known
KVM defect or a fixed kernel issue. No source/kernel/pin changes are justified.

## One bounded recovery, not launched

Use separate [export-only config](export-revision-aa963dce4.nix), which imports
the unchanged primary revision module and forces only `boot.qemu.memory` to
8192 MiB. The option is an ordinary integer option; `lib.mkForce` overrides
the image-test template's 24576 MiB definition. CPU count, kernel, initrd,
candidate source and existing test implementation stay selected as before.
Eight GiB matches the focused fixtures and is for metadata/export, not an image
rebuild or repeat of the primary verification.

`TestState.directory` depends only on test path and the supplied state base.
Using the same arguments below selects the same owned directory and
`machine-sda.img` (10737418240 bytes). Native `debug` sets `destructive: false`;
without `--fresh`, default disk preservation reuses that disk. Do not add
`--fresh`, delete/reset/import the disk elsewhere, or run a lifecycle command.

```sh
env VPSADMINOS_CONFIG=/home/aither/workspace/ai/vpsfree.cz/work/2026-11-03-opensuse-leap-image-build/export-revision-aa963dce4.nix ./test-runner.sh debug --state-dir /tmp/2026-11-03-opensuse-leap-image-build-image image-scripts/test@opensuse-leap-16.1
```

Lead assigns a fresh watcher and PTY/live stdin. Check fresh RAM/shm headroom
for the 8 GiB guest before launching, and verify the new native JSON's memory,
kernel/initrd and retained disk identity before sending the unchanged fixed
extraction eval from `candidate-checks.md`. Capture `candidate-extract-recovery.log`.
Watch the guest console from startup; the first watchdog/lockup message is an
immediate escalation. Interrupt the blocked eval, return to Pry and exit
normally through native cleanup as before. Preserve the disk and stop this
recovery batch on another boot failure; do not retry automatically or enter
kernel/KVM development. Exact cause remains unknown even if export succeeds.

After successful export and confirmed native VM exit, use the existing HTTP and
manual focused plan. Its two-VM 16 GiB shared-memory budget needs a fresh check;
the old 11728 MiB snapshot alone does not admit two focused VMs concurrently.
