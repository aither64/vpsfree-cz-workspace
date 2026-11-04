# AA package-only device-unit experiment

The first single-package preflight stopped safely before installation; the
revised native dependency-closure experiment below is prepared, not executed.
This is diagnosis of the original retained 16.1 image, not final-source image
verification.

The bounded native observation read establishes:

- Leap 16.1, systemd/libudev1 `257.13-160100.3.5`; `udev` is not installed.
- No udevadm/udevd command, no udevd process and no udev journal entries.
  All udev service/socket/trigger units are `LoadState=not-found`.
- `/run/udev/control` is the expected pre-PID1 regular stub. There is no
  `/run/udev/data` or `/run/udev/tags`.
- eth0 exists, is up, and resolves to `/sys/devices/virtual/net/eth0`. Its
  real and subsystem-alias device units are loaded/inactive with empty SysFSPath.
  The installed `99-systemd.rules` does tag non-loopback net devices correctly.
- The final native command has END `2026-11-03 21:00:28 +0100`, status 0 and
  complete output. OsVm logs that only after reading and validating command
  completion. The earlier missing PTY marker therefore did not imply a pending
  guest RPC. The lead's later host-only probe reached Pry prompt `[3]`.

This is sufficient to test absent udev processing as the cause. No evidence
calls for a host privilege, namespace or event rule change.

Use the same already-owned debug PTY. The fixed input
[device-unit-package-restart-aa963dce4.rb](device-unit-package-restart-aa963dce4.rb)
first preserves the completed native baseline logs, rechecks inactive eth0 and
no IPv4 address, then copies an exact signed udev RPM offline. It checks package
signature and dependency satisfaction before installing. Stop on any failure;
do not force dependencies, suppress scripts, import arbitrary keys or retry.

The host-side prepared package is
`/tmp/2026-11-03-opensuse-leap-image-build-udev-257.13-160100.3.5.x86_64.rpm`,
2,542,928 bytes, SHA256
`8bf941306f3878331df5c3f6853b3f720114fe5197bbe0082135e934734b7abf`.
It was downloaded from the official
[Leap 16.1 repository](https://download.opensuse.org/distribution/leap/16.1/repo/oss/x86_64/udev-257.13-160100.3.5.x86_64.rpm),
which redirected to ftp.sh.cvut.cz. The version exactly matches the retained
systemd/libudev1 packages. No repository or container network changes are needed.

Only udev may be added; the script compares full package inventories before and
after, rejecting removals or another added package. It then stops and starts
the container normally, verifying stopped state and a changed init PID. It does
not issue daemon-reload, manually start udev or trigger device events. Normal
package-maintainer scripts remain enabled.

After clean startup, require eth0.device active, dummy0.device absent before
creation and active after `ip link add dummy0 type dummy`. Record RPM versions,
udev service state, real control socket/database/tags, device properties and
the normal boot journal. Remove only the experiment's dummy interface, and
leave the same VM and modified diagnostic container owned for the lead's next
step. A pass would establish the minimal image-package fix; it would not replace
rebuilding the final source and running its original full assertions.

```ruby
eval(File.read('/home/aither/workspace/ai/vpsfree.cz/work/2026-11-03-opensuse-leap-image-build/device-unit-package-restart-aa963dce4.rb'), binding, 'device-unit-package-restart-aa963dce4.rb')
```

## Required dependency closure

The single-package `rpm --install --test` correctly rejected missing
`group(kvm)`, `group(lp)`, `kmod`, `libcryptsetup.so.12` (2.0/2.4/2.7 symbol
versions), `libkmod2` and `system-group-hardware`. No package, config or network
change occurred. Signature/hash checks passed; the baseline copies now exist
and must not be overwritten or recreated by rerunning that original input.

The revised fixed input is
[device-unit-closure-restart-aa963dce4.rb](device-unit-closure-restart-aa963dce4.rb).
It uses native `zypper install --download-only --no-recommends --details`, pinned
to `udev=257.13-160100.3.5` and the existing `openSUSE-oss` repository, with a new
isolated package cache. The official [zypper manual](https://manpages.opensuse.org/Leap-15.6/zypper/zypper.8.en.html)
documents these options and `--pkg-cache-dir`. No custom dependency solver,
forced dependency handling or recommendation expansion is used.

The source fixture already enables lxcbr0 with NAT/DNS at 192.168.1.1. The input
temporarily adds only pkg0 on that bridge, uses static 192.168.1.240 outside
the DHCP pool, and saves the original resolver bytes. It proves eth0 remains
inactive with udev absent after this network-only change. After native download,
it restores the original resolver, removes pkg0 and verifies unchanged installed
packages, no IPv4 on eth0 and inactive eth0 before installation. Restoration
also runs when download fails. An uncertain restoration stops the experiment.

The exact allowed package delta is the signed native solver's downloaded RPM
closure, printed as `DEVICE_UNIT_CLOSURE_ALLOWED_DELTA` before installation.
Every downloaded package must have a unique name absent from the original
installed inventory; upgrades, reinstalls and removals are rejected. The exact
udev version is mandatory. Each package's hash/signature is recorded, and native
RPM validates the whole bundle with `--install --test` before any installation.
The resulting installed delta must exactly equal that declared closure.

The same normal container stop/start and eth0/dummy assertions then run with
pkg0 absent and eth0 still without IPv4. No manual daemon start, reload, trigger
or service mask is added. All earlier AA inputs remain unchanged.

```ruby
eval(File.read('/home/aither/workspace/ai/vpsfree.cz/work/2026-11-03-opensuse-leap-image-build/device-unit-closure-restart-aa963dce4.rb'), binding, 'device-unit-closure-restart-aa963dce4.rb')
```

The bridge revision stopped before download: `netif new bridge` requires a
stopped container. Its ensure restored resolver bytes; no interface, package
or persistent network configuration was changed. Retain that fixed input.

The replacement is
[device-unit-runtime-closure-restart-aa963dce4.rb](device-unit-runtime-closure-restart-aa963dce4.rb),
SHA256 `81c36a5e2b01539953b71af440d80b9e724930810949db80d86b84ee9f3aeed1`.
It uses only standard runtime `ip` operations on existing eth0 and its existing
host veth. Source confirms the routed gateway is `255.255.255.254/32` on
`osrtr0`; the fixture already masquerades outbound traffic on host eth0.
`netif ls -H -o name,type,veth` is supported by the immutable CLI source.

The replacement checks no original guest IPv4/default route and no conflicting
host route, then temporarily adds `192.0.2.240/32` to guest eth0, its gateway and
default route, and a matching host return route on the existing veth. All are
removed in reverse order, with original routes, resolver and no-IP state checked
before offline installation. The native solver, signature/dependency checks,
strict package delta and final clean-restart assertions remain unchanged.
Both generated RPM query-format arguments were checked with host Ruby and
Shellwords; each ends in exactly one backslash followed by n. Syntax passes.
No guest action was taken while preparing this correction.
