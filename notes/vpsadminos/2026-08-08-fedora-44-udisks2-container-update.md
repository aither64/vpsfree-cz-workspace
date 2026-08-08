# Fedora 44 udisks2 update fails in unprivileged containers

Related initiative: `work/2026-08-07-vpsadminos-test-failures`

## Symptom

Fedora variants of otherwise unrelated container-engine tests fail together
while running `dnf -y update`. In CI run 31251769077, this affected Docker,
Incus, Podman, and both Snap scripts, while their non-Fedora variants passed.

## Cause

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

## Response

Do not accept an immediate rerun as validation while the same package remains
in the Fedora repository. Preferred resolution is an updated Fedora package
whose scriptlet tolerates device-scan restrictions in containers.

If CI must be restored before that package is available, a narrow temporary
workaround is to exclude `udisks2` and `libudisks2` from the `dnf update` in
the four Fedora test definitions. Keep the exclusion Fedora-specific and
remove it after the package is fixed. Validate all five affected scripts first,
then the full VM suite.
