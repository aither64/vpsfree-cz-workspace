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
- Replace the Debian Guix 1.4 bootstrap with a self-hosted builder based on the
  last published vpsAdminOS Guix image. Run an exact authenticated channel
  revision with `guix time-machine` instead of mutating the builder through two
  rolling pulls. Select channel revisions with pull substitutes available and
  commit the resolved revision so ordinary image builds remain reproducible.
- Qualify the custom Guix service list across Guix's delayed operating-system
  evaluation. Current Guix loads the configuration into fresh anonymous
  modules, so the formerly imported `%ct-services` binding is no longer in
  scope when the services field is forced.
- Keep the 1 GiB rootfs limit unchanged. Add a temporary musl-only Portage
  depclean for the unneeded Rust build dependency, with an explicit removal
  comment for when upstream stage3 archives are corrected.
- Run quick local checks, mandatory fresh-agent review, then push and use the
  resource-aware GitHub image workflow for expensive integration tests.
- Make changes to the image detector trigger its own workflow and select every
  concrete image so detector regressions cannot silently skip coverage.

## Integration plan after run 32094157385

### 1. Integrate the verified slice

- Fetch current `origin/staging` and use a fresh temporary integration
  worktree. The target advanced by one mechanical `flake.lock` update to
  `7f50e2d43`; rebase the reviewed changes onto that commit without altering
  the scheduled update.
- Cherry-pick every non-Guix commit from the feature branch in its original
  order. This includes Fedora retirement and updates, the fail-closed common
  runtime and its Arch/OpenSUSE callers, Slackware hardening, the temporary
  Gentoo musl workaround, and the workflow/detector changes.
- Run the quick checks and hooks again on the exact integrated tree, then run a
  fresh mandatory change review against current `origin/staging`.
- Fast-forward `staging` and push it. Add the documented GitHub
  `skip-checks: true` trailer to the final integration commit so the push does
  not repeat the same six-and-a-half-hour matrix. This is limited to the
  integration push: run `32094157385` exercised all 51 images at reviewed head
  `b0eeed852`, 49 passed, and the two failures are independently classified
  below; RuboCop run `32094157381` also passed. The one intervening staging
  commit changes only `flake.lock`.

### 2. Rewrite the feature branch to Guix only

- Build a new feature head from the integrated `origin/staging` instead of
  carrying the obsolete Debian bridge commits forward.
- Add `image-scripts/builders/guix` using `DISTNAME=guix` and
  `RELVER=latest`, point the Guix image at it, and remove the now-unused
  `debian-guix` builder.
- Replace the Guix 1.4 bridge, version probe, retry loop, and rolling pull with
  one authenticated, repository-pinned channel and
  `guix time-machine -C channels.scm -- system init ...`. Choose the initial
  revision only after Guix CI has substitutes for its package definitions.
- Module-qualify `%ct-services` in the delayed services field. Self-hosting
  removes the old bootstrap cost, but does not by itself fix this compatibility
  break.
- Preserve the last known-good dated Guix image. There will be no standing
  NixOS or foreign-distribution recovery builder; an exceptional recovery can
  explicitly select that dated image if it is ever needed.
- After quick checks and mandatory review, force-update the still-unmerged
  feature branch with `--force-with-lease`. Its GitHub diff will then contain
  only Guix image/builder files, so change detection will schedule only the
  Guix image test.

### 3. Validate and integrate Guix

- Inspect the Guix-only artifact even if the job passes, confirming that the
  base is the published Guix image, only the pinned time-machine generation is
  realized, the custom service list resolves, the image imports, and runtime
  tests pass.
- Fast-forward the verified Guix commits into `staging`. Do not skip this
  Guix-only workflow because it is new implementation rather than already
  exercised code.

### 4. Separate exporter hardening

- Do not change Arch for run `32094157385`. Its build and all new chroot/mount
  checks returned success; the later runtime-test import found a truncated
  `rootfs/base.dat.gz`. The same Arch bootstrap passed all 15 runtime tests in
  prior run `32037034898`.
- Track general `libosctl`/`osctl-image` hardening separately: validate each
  gzip/ZFS stream before accepting an archive, write exports atomically, and
  report or retry a corrupt export explicitly. This is existing exporter
  fragility, not an Arch image-script fix.

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
- Self-hosted Guix builds depend on the previously published image remaining
  available. A failed candidate is never promoted to replace that base. If
  recovery is ever required, select a known-good dated artifact manually;
  there is intentionally no continuously maintained secondary builder.

## Testing plan

- Run shell, Ruby, Nix, channel, detector, and failure-propagation checks
  locally, followed by Overcommit.
- Run the mandatory standalone review after all intended commits and quick
  verification, before any expensive image tests.
- Push the Guix-only rewritten feature branch and let
  `.github/workflows/image-scripts.yml` build and test only Guix with
  resource-aware `--jobs auto`.
- Inspect logs and artifacts for every failure, fix causes, and cancel
  superseded runs after follow-up pushes.
