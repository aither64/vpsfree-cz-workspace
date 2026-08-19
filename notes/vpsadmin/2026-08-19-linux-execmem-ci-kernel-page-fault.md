# Linux 6.18 execmem page fault in vpsAdmin integration tests

## Symptom

The `vps/replace-remote` integration test in vpsAdmin GitHub Actions run
`32233193143`, attempt 2, failed while the services guest was booting. The
guest reported a supervisor write-protection fault in `memset_orig()` from
`__execmem_cache_free()`:

```text
BUG: unable to handle page fault for address: ffffffffc119f000
#PF: supervisor write access in kernel mode
#PF: error_code(0x0003) - permissions violation
CPU: 3 UID: 0 PID: 457 Comm: (udev-worker)
Not tainted 6.18.43 #1-NixOS PREEMPT(lazy)
RIP: memset_orig+0x33/0xb0

RAX: cccccccccccccccc
RDX: 0000000000001000
RSI: 00000000000000cc
RDI: ffffffffc119f000

Call Trace:
 __execmem_cache_free+0x6c/0xc0
 execmem_free+0x9d/0x180
 load_module+0x15f9/0x25c0
 __do_sys_init_module+0x1a8/0x1e0
```

The `0xcc` byte, one-page length, and fault address matching the destination
identify the x86 executable-memory trapping-instruction fill performed while
freeing module memory.

## Cause

Linux 6.18 has a race in the executable-memory cache allocation path. Cache
population and the following allocation are not atomic. A competing module
loader can consume the newly populated area before the original loader retries
its allocation. Error cleanup can then restore and free earlier allocations in
a state whose page permissions no longer permit the trapping-instruction
write.

Upstream commit
[`1871d548fc4f`](https://github.com/torvalds/linux/commit/1871d548fc4feb007644efb6d669c93a4e191254),
`mm/execmem: make the populate and alloc atomic`, fixes this matching race.
Linux 6.18.45 and the `linux-6.18.y` branch did not yet contain the fix when
this was investigated on 2026-08-19, so a 6.18.43 to 6.18.45 version bump
alone is insufficient.

The failure is unrelated to password recovery. It occurred 8.5 guest-seconds
after boot, before vpsAdmin API readiness. The feature branch did not change
the guest kernel, QEMU, or module configuration, and the same test passed at
the same feature revision in the preceding CI attempt. Closely related VPS
replacement tests also passed.

The uncertain `trusted_tee_seal` frame was prefixed with `?` and does not prove
that the `trusted` module triggered the race. Do not blacklist that module on
this evidence.

## Durable fix

Backport upstream commit `1871d548fc4feb007644efb6d669c93a4e191254` into
the NixOS kernel used by generated vpsAdminOS test VMs, then update vpsAdmin's
vpsAdminOS pin. Also request inclusion in the Linux 6.18 stable series.

Do not disable the test runner's kernel-failure detector. It correctly exposed
the guest-kernel failure.

## Temporary mitigation

Retrying the affected test is reasonable after confirming that the runner's
Nix store is healthy. The race is timing-dependent and the same-head test
already passed once.

For test VMs only, `clearcpuid=pse` bypasses the x86 ROX executable-memory
cache that contains the bug. Linux documents `clearcpuid` as a testing option
and it taints the kernel, so this is not a production or durable fix.

## Verification

Build otherwise identical test kernels with and without the backport. Stress
parallel loading of initially unloaded modules for at least 100 KVM boot
cycles, retaining the debug `vmlinux` and recording the guest kernel
derivation, `uname -a`, `/proc/cmdline`, and `/proc/cpuinfo`. The patched kernel
must complete without allocation errors, Oopses, page faults, or
`__execmem_cache_free` failures.

Then run:

```sh
./test-runner.sh test -f --jobs 1 services-up
./test-runner.sh test -f --jobs 1 vps/replace-remote
./test-runner.sh test -f --jobs auto --filter 'tag=ci'
```

Repeat `vps/replace-remote` at least 20 times while other VM tests run, then run
the full CI selection twice.

Related initiative:
`work/2026-08-18-vpsadmin-password-reset/`.
