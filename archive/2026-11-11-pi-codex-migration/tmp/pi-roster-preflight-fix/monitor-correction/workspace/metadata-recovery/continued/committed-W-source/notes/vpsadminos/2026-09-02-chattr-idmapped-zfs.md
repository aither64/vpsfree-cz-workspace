# OpenZFS chattr checks must use the mount idmap

## Symptom

In a default native-map vpsAdminOS container, BusyBox `chattr +i` and `+a`
print `Permission denied`, but return status 0 and leave the flags unset. The
status-only `kernel/vpsadminos#misc-attrs` examples therefore pass without
testing their stated behavior.

## Cause

The vpsFree OpenZFS patch allowing `CAP_LINUX_IMMUTABLE` in a first-level user
namespace is present and its capability check passes. The next ownership check
and the eventual `zfs_setattr()` still use `zfs_init_idmap` instead of the
idmap of the file's mount.

Native-map container files are reached through an idmapped bind mount while
the underlying ZFS inode remains host-owned. Ignoring the mount idmap makes
container root appear not to own the inode, so OpenZFS returns `EACCES`.
Legacy ZFS map mode works because inode ownership is physically shifted.

## Fix direction

In the existing `FS_IOC_SETFLAGS` handler, pass
`mnt_idmap(filp->f_path.mnt)` to the inode-owner check and `zfs_setattr()` while
retaining the existing first-level namespace capability restriction. The wider
historical callback implementation in commit `454a692c3` is not required for
this issue.

Do not trust BusyBox 1.37.0 `chattr` status: its implementation reports ioctl
errors but unconditionally returns success. Assert `lsattr` state and immutable
or append-only filesystem behavior. e2fsprogs `chattr` returns nonzero on these
failures, but installing it adds a package/repository dependency and still
does not replace semantic assertions.

Related initiative:
`work/2026-09-02-vpsadminos-chattr-test`.
