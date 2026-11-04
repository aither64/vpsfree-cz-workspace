# openSUSE Leap device unit native runtime result

## Operation and inputs

The operation used the retained native test runner and its prepared AA revision configuration through one PTY (`exec session 50302`). Source revision: `aa963dce42859ae4251cdfaded91920d67b3a46e`. The fixed launcher SHA256 was `b8e08ab5fd5e8402a2a3e09a017fe43baf2b8630a11a6ae1e265306f101dcc9d`; observation input SHA256 was `cbbd2c22114446dd93ddf01b6ad95269ca809aac23faa39191999c7e1effa6f`. The expected prepared config SHA256 `5e2de9fef94e2b08c0d65d0a06f590a43265a3a35a7dde4018875d859705a5eb` was checked by the reopen input and by each experiment.

Full returned PTY chunks are in [device-unit-runtime-fixed.log](device-unit-runtime-fixed.log). Native baseline command and console output was copied before experiments to [device-unit-baseline-aa963dce4-shell.log](device-unit-baseline-aa963dce4-shell.log) and [device-unit-baseline-aa963dce4-console.log](device-unit-baseline-aa963dce4-console.log). The runner's retained authoritative state is `/tmp/2026-11-03-opensuse-leap-image-build-device-units/os-test-systemd__device-units-e983cb16`.

## Observation

The preserved guest was openSUSE Leap 16.1 Micro, systemd `257.13-suse.131.g575b4807b7`. `rpm -q systemd udev libudev1` returned status 1: systemd and libudev1 were installed, while `udev` was absent. The initial nonzero read-only command was reported by the observer as an expected command failure. Baseline console output showed `eudev-trigger not started` messages during boot, followed by successful service starts. No guest watchdog, softlockup, or panic was observed.

## Bounded experiments

1. A fixed package-only experiment (`device-unit-package-restart-aa963dce4.rb`, SHA256 `8d6ea5d3613a32c948e2a2bc90811f7294d8888b00ff54df3a883c14fb6b528c`) verified baseline eth0 inactive/no IPv4 and copied the specified signed udev RPM into the guest. `rpm --checksig` passed. `rpm --install --test` stopped with status 1 because dependencies were missing: `group(kvm)`, `group(lp)`, `kmod`, `libcryptsetup.so.12` (CRYPTSETUP_2.0/2.4/2.7), `libkmod2`, and `system-group-hardware`. No package installation occurred.

2. A fixed zypper closure attempt using a temporary `pkg0` bridge interface (`device-unit-closure-restart-aa963dce4.rb`, SHA256 `a1c600328d3ac9f9ca0a4666498bd02c9434116484731e719ac40b4f05e49d17`) stopped at its first action because `osctl ct netif new bridge --link lxcbr0 testct-553b pkg0` reported `the container must be stopped to add network interface`. Its `ensure` restored `/etc/resolv.conf`; `pkg0` was never created. No install or retry followed.

3. The authorized fixed runtime-address closure experiment (`device-unit-runtime-closure-restart-aa963dce4.rb`, SHA256 `81c36a5e2b01539953b71af440d80b9e724930810949db80d86b84ee9f3aeed1`) used only temporary runtime IP/routes on the existing routed eth0 and a temporary host return route. The network-only check kept eth0's systemd device unit inactive and udev absent. `zypper --download-only --no-recommends` fetched exactly 15 packages from the signed `openSUSE-oss` repo. Its ensure removed the temporary guest address/routes and host route and restored original DNS before package validation or installation. Subsequent checks confirmed the original package set and guest routes, no IPv4 address, eth0 inactive, and no temporary host route.

   All 15 RPMs passed digest/signature checks; `rpm --install --test` passed. The exact added package set was: `device-mapper-2.03.38_1.02.212-160100.2.1.x86_64`, `gzip-1.14-160100.2.1.x86_64`, `kmod-34.2-160100.2.1.x86_64`, `libcryptsetup12-2.8.4-160100.2.1.x86_64`, `libdevmapper-event1_03-2.03.38_1.02.212-160100.2.1.x86_64`, `libdevmapper1_03-2.03.38_1.02.212-160100.2.1.x86_64`, `libjson-c5-0.17-160100.2.1.x86_64`, `libkmod2-34.2-160100.2.1.x86_64`, `suse-module-tools-16.1.6-160100.2.1.x86_64`, `system-group-hardware-20170617-160100.2.1.noarch`, `system-group-kvm-20170617-160100.2.1.noarch`, `system-user-lp-20170617-160100.2.1.noarch`, `systemd-rpm-macros-26-160100.2.1.noarch`, `thin-provisioning-tools-1.1.0-160100.2.2.x86_64`, and `udev-257.13-160100.3.5.x86_64`. Actual delta matched exactly: 15 added, none removed.

   During installation, output included `Failed to send reload request: Connection refused` and a Lua transfiletrigger error. Despite those messages, the declared package delta was present, the clean container stop/start completed, and all subsequent assertions passed. Container init PID changed from `3134` to `6034`; eth0 remained without IPv4 and temporary `pkg0` was absent. `systemd-udevd.service` was loaded/active/running; `systemd-udev-trigger.service` was loaded/active/exited. `/run/udev/control`, `/run/udev/data`, and `/run/udev/tags/systemd` existed. `udevadm info` returned status 0 for eth0 and a temporary dummy0, with both devices carrying `TAGS=:systemd:` and `CURRENT_TAGS=:systemd:`. The script deleted dummy0 and printed `DEVICE_UNIT_CLOSURE_RESTART_PASS`.

## Closure

The exact same Pry session exited normally after lead authorization; the PTY command returned exit status 0. No matching evaluator, QEMU, or virtiofsd process remained. `lslocks` showed no lock owner for the retained state lock; the lock file remains present. The 10 GiB retained `machine-sda.img` remains present and was not deleted or reset. Baseline and experiment logs are preserved above.

This is native runtime evidence for the retained AA configuration and guest. It does not verify a final source change or establish that any kernel fix is present.
