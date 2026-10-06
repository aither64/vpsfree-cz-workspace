# 2026-06-07-gentoo-image-size

## Goal

Reduce the built rootfs size of the Gentoo container images in `vpsadminos`
so `image-scripts/test@gentoo-openrc` and `image-scripts/test@gentoo-systemd`
fit under the existing 1 GiB `rootfs_size` test limit. Prefer removing
unneeded image build artifacts over raising the global limit.

## Affected repositories

- `vpsadminos`

## Approach

1. Inspect the Gentoo image scripts and the upstream stage3 payloads.
2. Identify files that are not needed in a published container image.
3. Update the shared Gentoo image cleanup in `image-scripts/include/gentoo.sh`.
4. Run scoped Gentoo image tests, at least the two failing glibc variants.

## Compatibility and deployment

The change should only remove cache and temporary build artifacts from newly
built Gentoo images. It must not change the image format, image repository
format, osctld protocols, API contracts, persistent host state, database
schemas, NixOS module options, or vpsAdminOS deployment ordering.

The synced Gentoo ebuild repository in `/var/db/repos/gentoo` is preserved so
package management in a freshly created container remains usable. The cleanup
targets Portage distfiles, fetched binary package caches, local binary package
caches, and build work directories.

## Testing plan

- `./test-runner.sh ls 'image-scripts/*gentoo*'`
- Inspect current stage3 contents for kernel, firmware, and large directories.
- `./test-runner.sh test --fresh --no-destructive image-scripts/test@gentoo-openrc`
- `./test-runner.sh test --fresh --no-destructive image-scripts/test@gentoo-systemd`
