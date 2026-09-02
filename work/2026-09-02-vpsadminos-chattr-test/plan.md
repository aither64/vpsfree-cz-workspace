# 2026-09-02-vpsadminos-chattr-test

## Goal

Make the vpsAdminOS kernel attribute test exercise the advertised ability for
container root to set and clear immutable and append-only flags. Fix the
underlying OpenZFS native/idmapped-mount behavior instead of masking it in the
test.

This initiative is independent of `2026-06-15-vpsadmin-events` and is intended
to merge first. The events work must then rebase onto the updated vpsAdminOS
staging branch.

## Affected repositories

- `zfs`: add mount-idmap-aware file-attribute ownership and setattr handling
  on top of the exact ZFS revision pinned by vpsAdminOS staging,
  `6f5f54c3bfd68c1e52b0b6f454ee9679aaa9e83d`.
- `vpsadminos`: update the active kernel's ZFS pin and strengthen
  `kernel/vpsadminos#misc-attrs`.

## Approach

1. Preserve the existing first-level-user-namespace
   `CAP_LINUX_IMMUTABLE` policy and nested namespace restriction.
2. Change only the existing `FS_IOC_SETFLAGS` path used by `chattr`. Obtain the
   file mount's idmap and use it for the inode-owner check and `zfs_setattr()`.
   Leave VFS callbacks, extended attributes, DOS attributes, and fallocate
   unchanged.
3. Publish the focused ZFS commit, then pin that exact revision in the active
   vpsAdminOS 6.12.95 kernel definition.
4. Test both `native` and `zfs` map modes explicitly. After every set or clear,
   use `lsattr` and real write/delete operations as the oracle because BusyBox
   1.37.0 reports ioctl errors but returns success from `chattr`.

## Compatibility and deployment

- No userspace API, schema, protocol, dataset format, or other persisted format
  changes.
- The fix allows an inode owner as seen through an idmapped mount to set
  supported flags when the existing namespace capability policy permits it.
  Host and legacy ZFS-map behavior remain unchanged.
- Rolling upgrades are safe. A rolled-back kernel can read the flags but may
  again be unable to clear them from inside a native-map container; host root
  can clear them.
- No coordinated all-node update is required. Nodes gain the behavior when
  they boot the updated vpsAdminOS kernel.

## Testing plan

- Run OpenZFS source/style and commit checks, then build the changed ZFS kernel
  integration through the vpsAdminOS workflow.
- Run `kernel/vpsadminos#misc-attrs` with immutable and append-only semantic
  assertions in explicit native- and ZFS-map containers.
- Run the OpenZFS positive and negative chattr tests and the relevant
  vpsAdminOS kernel aggregate after mandatory change review.
- The OpenZFS full-suite VM uses an ext4 work image while module autoloading is
  disabled. Explicitly load the ext4 module in that test VM so the selected
  upstream cases can reach their test bodies.
- Use GitHub Actions for the changed kernel build and full feedback. Inspect
  every failure and cancel only superseded runs for old branch heads.
