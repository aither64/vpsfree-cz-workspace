# Fedora udisks2 update fails in vpsAdminOS containers

Related initiative: `work/2026-08-07-vpsadminos-test-failures`

## Symptom

Fedora variants of otherwise unrelated container-engine tests fail together
while running `dnf -y update`. In CI run 31251769077, this affected Docker,
Incus, Podman, and both Snap scripts, while their non-Fedora variants passed.

## Timeline and classification

Fedora update `FEDORA-2026-ae4aff6b6f` moved
`udisks2-2.11.2-1.fc44` to stable on 2026-08-08 at 01:36 UTC. The failing CI
job began later that morning, so an unchanged vpsAdminOS commit saw a newer
Fedora repository than the preceding successful run.

The release bump did not intentionally change container behavior. Fedora's
2.11.2 dist-git commit changes the version, source archive, an upstreamed
patch, and changelog, but leaves the `%post` scriptlet unchanged. Upstream
2.11.2 is a bug and security-fix release; the failing scriptlet is Fedora
packaging, not upstream udisks code.

This is a latent Fedora packaging bug. The scriptlet has this logic:

```spec
if [ -S /run/udev/control ]; then
    udevadm control --reload
    udevadm trigger
fi
```

The socket guard was added in 2019 specifically to skip environments such as
containers and rpm-ostree systems when udev is not accessible. A vpsAdminOS
container is a valid case the guard does not cover: it deliberately has
`/run/udev/control`, because systemd needs udev events for device units, while
its unprivileged sysfs remains restricted. The socket is therefore accessible,
but a global `udevadm trigger` device scan is not permitted.

The 2.11.2 upgrade exposed the old bug because it caused the existing
scriptlet to execute. It is not a DNF transaction-planning bug. RPM reports a
nonzero `%post` as an error after package files have been installed, and RPM
scriptlets are expected to return zero rather than aborting an otherwise
successful transaction.

## Failure mechanism

The Fedora 44 repository began serving `udisks2-2.11.2-1.fc44`. Its `%post`
scriptlet tries to scan devices, receives `Permission denied` inside an
unprivileged container, exits with status 1, and makes the complete RPM
transaction fail. The relevant output is:

```text
Running %post scriptlet: udisks2-2.11.2-1.fc44.x86_64
Failed to scan devices: Permission denied
%post(udisks2-2.11.2-1.fc44.x86_64) scriptlet failed, exit status 1
Transaction failed: Rpm transaction failed.
```

This is distinct from runner memory exhaustion. All affected test VMs exited
normally with QEMU status 0, and 71 other tests completed successfully under
the reduced scheduler limit.

## Image build impact

The normal Fedora 44 image build is not expected to hit this bug:

- `image-scripts` runs `dnf -y update` in a chroot with `/proc`, `/sys`, and
  `/dev` mounted, but does not bind a live `/run` or udev control socket;
- Fedora's socket guard therefore skips both `udevadm` commands;
- the current image builder is Fedora 42, whose repositories do not yet carry
  udisks 2.11.2; and
- the post-build image test inventories packages but does not run a live
  `dnf update` inside a booted container.

A Fedora 44 image build should still be tested, but rebuilding the image is a
useful mitigation rather than another expected failure. A refreshed image can
install 2.11.2 safely in the chroot. Booted test containers then start with the
new package already installed, so their `dnf update` does not invoke the
broken upgrade scriptlet.

Any other build or update workflow that runs `dnf upgrade` inside a *booted*
Fedora container with `/run/udev/control` can still fail. Fedora 43 carries the
same 2.11.2 update in testing, so the problem can spread when that update is
promoted.

## Recommended response

### Fedora package

Report the failure to Fedora with a vpsAdminOS reproducer and the CI log. The
package should explicitly skip containers and make udev refresh best-effort,
for example:

```spec
if [ -S /run/udev/control ] &&
   ! systemd-detect-virt --quiet --container; then
    udevadm control --reload || :
    udevadm trigger || :
fi
```

At minimum, both `udevadm` calls should tolerate failure. This matches the
original maintainer's Bugzilla analysis that these return codes should be
ignored. Fedora should publish corrected Fedora 44 and Fedora 43 builds and add
a container gating test; the Bodhi host tests and positive karma did not cover
this environment.

### vpsAdminOS

The preferred immediate mitigation is to rebuild and publish the Fedora 44
container image, verify that it contains `udisks2-2.11.2-1.fc44`, run
`image-scripts/test@fedora-44`, and then rerun the five affected scripts or the
full VM suite.

If image publication cannot happen promptly, a narrow test-only workaround is
to exclude `udisks2*` from `dnf upgrade` in Fedora variants. Remove the
exclusion after Fedora publishes a fixed build. Version 2.11.2 includes a fix
for CVE-2026-7867, so retaining an old udisks build is inappropriate for
published images and should be short-lived even in CI.

A retry can also work because RPM may have installed the new package before the
`%post` failure. Do not hide the first result with an unconditional
`dnf || dnf`: verify the installed `udisks2` and `libudisks2` versions, run
`dnf check`, and require the second upgrade to succeed. This is less clear and
less robust than refreshing the base image.

### Existing containers

For a container that has not upgraded, temporarily exclude `udisks2*` until a
fixed Fedora package is available, with the security tradeoff recorded. For a
container where the transaction already failed, first check the installed
versions with `rpm -q udisks2 libudisks2`, run `dnf check`, then rerun the
upgrade. Use an internally rebuilt fixed RPM when the security update is
urgent.

Do not globally disable RPM scriptlets and do not grant containers broader
sysfs or device access. Stopping or hiding the udev socket is also unsuitable
as a general workaround because vpsAdminOS creates it for systemd device-unit
handling.

## Sources

- Fedora 44 update: <https://bodhi.fedoraproject.org/updates/FEDORA-2026-ae4aff6b6f>
- Fedora 43 testing update: <https://bodhi.fedoraproject.org/updates/FEDORA-2026-1925a10b0b>
- Fedora 2.11.2 commit: <https://src.fedoraproject.org/rpms/udisks2/c/61b4ef491e00ab65dc83b23437364285f83cbbb1?branch=f44>
- Current Fedora 44 spec: <https://src.fedoraproject.org/rpms/udisks2/blob/f44/f/udisks2.spec>
- Original socket-guard commit: <https://src.fedoraproject.org/rpms/udisks2/c/f651544b5437457335e7b40e4c1275bc24fbbc40?branch=f44>
- Original Fedora bug: <https://bugzilla.redhat.com/show_bug.cgi?id=1753786>
- Upstream 2.11.2 release notes: <https://github.com/storaged-project/udisks/blob/udisks-2.11.2/NEWS>
- RPM scriptlet semantics: <https://rpm.org/docs/latest/manual/triggers.html>
