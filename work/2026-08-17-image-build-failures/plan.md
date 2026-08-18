# 2026-08-17-image-build-failures

## Goal

Repair the container image build failures from build.vpsfree.cz. Retire
Fedora 42, update the shared builder and Rawhide bootstrap, make image
configuration and Slackware downloads fail closed, move Guix to its canonical
authenticated channel, and validate the affected images in GitHub Actions.

## Affected repositories

- `vpsadminos`

## Approach

- Remove the Fedora 42 image script and repository schedule entry.
- Update the shared Fedora builder to Fedora 44 and teach CI change detection
  to select images that consume changed builders.
- Discover and apply the current Fedora Rawhide release RPM version in its own
  release commit; make Red Hat release downloads fail on HTTP errors.
- Preserve chroot configuration and partial-mount failures through cleanup,
  and contain all image-build mounts in a disposable private namespace so a
  failed cleanup cannot poison the reusable builder.
- Extract and harden the shared Slackware bootstrap: exact package selection,
  atomic/retried downloads, mandatory checksums, deterministic installation,
  and fail-fast chroot configuration.
- Configure Guix to pull the authenticated official channel through
  `https://git.guix.gnu.org/guix.git` with bounded retries. When bootstrapping
  from Debian's Guix 1.4, first use an authenticated pre-`spawn` bridge whose
  self-build upgrades Guile, then retain the unpinned rolling pull. Keep both
  channel files compatible with Guix's isolated safe-binding evaluation.
- Keep the 1 GiB rootfs limit unchanged. Add a temporary musl-only Portage
  depclean for the unneeded Rust build dependency, with an explicit removal
  comment for when upstream stage3 archives are corrected.
- Run quick local checks, mandatory fresh-agent review, then push and use the
  resource-aware GitHub image workflow for expensive integration tests.
- Make changes to the image detector trigger its own workflow and select every
  concrete image so detector regressions cannot silently skip coverage.

## Compatibility and deployment

- Changes affect image building only; there are no API, schema, protocol, or
  persisted-state changes and no coordinated node rollout is required.
- Removing Fedora 42 stops future builds but does not delete published images.
- Fedora 44 remains the stable/latest Fedora image and becomes the base for the
  shared Fedora builder.
- Fail-closed behavior can expose existing hidden build errors, intentionally.
- The mount namespace wrapper is supplied through the existing bind-mounted
  image scripts, so it requires no coordinated host or builder rollout. All
  supported builder bases normally provide `unshare`; a missing command fails
  the build before it changes state. An unusually old or minimized reusable
  builder would need util-linux installed or the builder recreated.
- Existing containers remain unchanged. No production image deletion or
  repository promotion is part of this initiative.

## Testing plan

- Run shell, Ruby, Nix, channel, detector, and failure-propagation checks
  locally, followed by Overcommit.
- Run the mandatory standalone review after all intended commits and quick
  verification, before any expensive image tests.
- Push the feature branch and let `.github/workflows/image-scripts.yml` build
  and test the detected image set with resource-aware `--jobs auto`.
- Inspect logs and artifacts for every failure, fix causes, and cancel
  superseded runs after follow-up pushes.
