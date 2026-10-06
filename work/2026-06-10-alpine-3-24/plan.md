# 2026-06-10-alpine-3-24

## Goal

Add Alpine Linux 3.24 image build support to vpsAdminOS.

## Affected repositories

- `vpsadminos`

## Approach

- Reuse the existing Alpine image script pattern, where versioned images are
  symlinks to `image-scripts/images/alpine`.
- Add `image-scripts/images/alpine-3.24` as a symlink to `alpine`.
- Add Alpine 3.24 to `os/configs/image-repository.nix` and move the
  `latest`/`stable` tags from 3.23 to 3.24.
- Keep `tests/distributions.nix` unchanged because the Alpine distribution
  tests already target the `latest` repository tag.

## Compatibility and deployment

- This is additive for image builds: existing Alpine 3.20 through 3.23 image
  scripts remain available.
- Moving `latest` and `stable` changes the default Alpine image selected by
  image repository consumers from 3.23 to 3.24 after the image repository is
  rebuilt.
- The image still uses OpenRC and the existing Alpine container cgroup helper,
  so no mixed-version host/guest protocol or persisted state change is
  introduced.
- Rollback is possible by moving `latest`/`stable` tags back to Alpine 3.23 in
  the image repository config and rebuilding the repository.

## Testing plan

- Run shell syntax checks for the new symlinked image script and config.
- List `image-scripts/test@alpine-3.24` to verify test discovery.
- Run `./test-runner.sh test image-scripts/test@alpine-3.24`.
