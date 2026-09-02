# 2026-09-02-vpsadminos-chattr-test

## Goal

Make the vpsAdminOS kernel attribute test exercise the advertised ability for
container root to set and clear immutable and append-only flags. Fix the
underlying OpenZFS native/idmapped-mount behavior instead of masking it in the
test.

This initiative is independent of `2026-06-15-vpsadmin-events` and is intended
to merge first. The events branches must then be rebased onto the resulting
default branches.

## Affected repositories

- `zfs`: backport mount-idmap-aware file-attribute ownership and setattr
  handling to the current `vpsadminos-release-next` lineage.
- `vpsadminos`: strengthen `kernel/vpsadminos#misc-attrs` and update the ZFS
  source pin after the ZFS change is committed.

## Approach

1. Preserve the existing first-level-user-namespace
   `CAP_LINUX_IMMUTABLE` policy.
2. In OpenZFS, obtain the mount idmap from the opened file and use it for both
   `zpl_inode_owner_or_capable()` and `zfs_setattr()` on file-attribute setter
   paths. Adapt the focused implementation in historical fork commit
   `454a692c3` to the current 2.3.5-based default branch. Do not pull in the
   unrelated fallocate part of later commit `8374426f6` merely to fix attrs.
3. Reconcile ZFS default `f53469bdc` with `6f5f54c3b` before adding the fix.
   The latter is a direct descendant already pinned by vpsAdminOS staging, so
   retaining it avoids regressing the current fallocate fix while keeping the
   initiative rooted in the fetched ZFS default branch.
4. Update the vpsAdminOS ZFS revision and hash to the committed ZFS fix.
5. Replace status-only `chattr` examples with state and behavior assertions:
   verify `lsattr` after every set/clear, immutable write/unlink denial, and
   append-only append/truncate/unlink behavior.

Recommended invocation strategy: keep the image-provided BusyBox tools, but
treat `lsattr` state and file operations as the test oracle. BusyBox 1.37.0
prints ioctl errors yet always returns success from `chattr_main()`, so its
exit status cannot be trusted.

Alternatives:

- Install Alpine `e2fsprogs-extra` and use its `chattr`, which returns nonzero
  when `FS_IOC_SETFLAGS` fails. This gives honest command status but adds a
  repository/network dependency and still does not prove attribute semantics.
- Push a small compiled ioctl helper from the Nix test closure. This is the
  most deterministic way to assert flags and errno without image tooling, but
  adds helper code that is unnecessary if `lsattr` plus behavior checks are
  sufficient.
- Force the test container to legacy `--map-mode zfs`. This is useful only as
  a diagnostic control; it would stop testing the default native map mode.
- Expect permission denial or change LXC capabilities. Both contradict the
  stated feature and evidence: the container already has
  `CAP_LINUX_IMMUTABLE`, and only the mount-idmap ownership check fails.

## Compatibility and deployment

- On-disk ZFS flags and dataset formats do not change.
- The fix affects authorization through idmapped mounts: an inode owner as
  seen through the mount may set supported flags when the existing namespace
  capability policy also permits it. Host behavior and legacy ZFS map mode
  remain unchanged.
- Keep the existing restriction to first-level user namespaces; nested user
  namespaces must not gain this authority accidentally.
- Rollback can read all state created by the fix. A rolled-back kernel may be
  unable to clear flags from inside a native-map container, while host root can
  still clear them.
- Merge and publish ZFS first, then update and merge vpsAdminOS. No coordinated
  all-node update is required; nodes gain the behavior when they boot the new
  vpsAdminOS kernel/ZFS build. Rebase the events work onto both resulting
  defaults afterward.

## Testing plan

- Reproduce denial on a default native-map Alpine container and success on a
  legacy ZFS-map control container.
- Build the changed ZFS module/kernel output through the vpsAdminOS workflow;
  do not accept an unexplained local kernel build or cache miss.
- Run `./test-runner.sh test 'kernel/vpsadminos#misc-attrs'` with assertions for
  both flags and their filesystem effects.
- Run focused OpenZFS attribute tests if present, plus the relevant vpsAdminOS
  kernel aggregate after quick verification and mandatory change review.
- Verify a nested user namespace still cannot use the first-level allowance.
