# VM tests using an extra filesystem must include its kernel module

## Symptom

An os-test VM can successfully run `mkfs.ext4` on a test device, but mounting
it then fails with:

```text
mount: unknown filesystem type 'ext4'
```

## Cause

The vpsAdminOS VM test machine does not include every filesystem module merely
because the userspace formatting tool is in `environment.systemPackages`.
Tests creating an additional filesystem outside the machine's normal storage
configuration must request that filesystem in the test machine configuration.

## Fix

For an ext4-backed fixture, add both:

```nix
boot.kernelModules = [ "ext4" ];
boot.supportedFilesystems.ext4 = true;
```

Then keep `e2fsprogs` in `environment.systemPackages` for `mkfs.ext4`.

## Verification

The initial `osctld/lifecycle` run for
`work/2026-07-24-ct-start-hang/` failed before its lifecycle assertions at the
mount step. The retained runner log was
`/tmp/os-test-runner/os-test-osctld__lifecycle-000573c0/test-runner.log`.
