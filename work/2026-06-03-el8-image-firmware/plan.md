# EL8 image firmware exclusion

## Goal

Remove unnecessary firmware packages from the AlmaLinux 8 and Rocky 8
vpsAdminOS container images to reduce image size and avoid CI import failures
caused by oversized EL8 images.

## Affected repositories

- `vpsadminos`: Red Hat-family image script helper and EL8 image definitions.

## Approach

1. Add optional package exclusion support to the Red Hat-family image bootstrap
   yum/dnf configuration.
2. Configure AlmaLinux 8 and Rocky 8 images to exclude firmware and CPU
   microcode packages that are not useful inside containers.
3. Run focused image-script tests for `almalinux-8` and `rocky-8`.
4. Record validation and any remaining caveats.

## Compatibility and deployment

This changes only newly built container images. It does not change vpsAdminOS
runtime behavior, APIs, persisted host state, or existing deployed containers.
Existing published images remain unchanged until the image repository is rebuilt
and deployed.

The generated AlmaLinux 8 and Rocky 8 images will no longer contain hardware
firmware and microcode packages. That is compatible with container use because
containers use the host kernel and hardware initialization; firmware loading is
not performed from inside the container rootfs.

Rollback is straightforward: rebuild images without the exclusion if firmware
is unexpectedly needed.

## Testing plan

- `./test-runner.sh test image-scripts/test@almalinux-8`
- `./test-runner.sh test image-scripts/test@rocky-8`
