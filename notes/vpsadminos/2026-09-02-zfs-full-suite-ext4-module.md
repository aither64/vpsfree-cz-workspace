# OpenZFS full-suite work image needs the ext4 module

## Symptom

`zfs/full-suite` builds and boots its VM, then fails before invoking any
selected OpenZFS test:

```text
mount: /tank/zfs-full-suite/work: unknown filesystem type 'ext4'.
```

## Cause

The harness formats a 48 GiB ext4 work image and mounts it inside vpsAdminOS.
The kernel has `CONFIG_EXT4_FS=m`, while vpsAdminOS disables kernel module
autoloading by default. Failure diagnostics contain the denied request:

```text
kernel.modprobe: action=deny -q -- fs-ext4
```

The test VM did not include `ext4` in `boot.kernelModules`, so its explicit
kernel-module service never loaded it.

## Fix

Add `boot.kernelModules = [ "ext4" ];` to the `zfs/full-suite` VM module. This
both retains the module in the VM closure and loads it before the harness
mounts the work image.

Observed while running the OpenZFS `chattr` tests for
`work/2026-09-02-vpsadminos-chattr-test`.
