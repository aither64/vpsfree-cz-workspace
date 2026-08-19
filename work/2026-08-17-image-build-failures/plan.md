# 2026-08-17-image-build-failures

## Goal

Repair the container image build failures from build.vpsfree.cz. Retire
Fedora 42, update the shared builder and Rawhide bootstrap, make image
configuration and Slackware downloads fail closed, move Guix to its canonical
authenticated channel, and validate the affected images in GitHub Actions.

## Affected repositories

- `vpsadminos`
- `vpsfree-kb-contracts`

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
  last published vpsAdminOS Guix image. Resolve the newest authenticated
  default-branch revision for which Guix CI has pull substitutes, then run that
  revision with `guix time-machine` instead of mutating the builder through two
  rolling pulls. Keep the channel itself unpinned in the repository so it does
  not require manual revision updates; fail before the build if CI cannot
  supply a suitable revision.
- Capture both custom Guix service fields across delayed operating-system
  evaluation. Current Guix loads the configuration into fresh anonymous
  modules, so imports from the original user module are no longer in scope
  when those fields are forced.
- Keep the 1 GiB rootfs limit unchanged. Add a temporary musl-only Portage
  depclean for the unneeded Rust build dependency, with an explicit removal
  comment for when upstream stage3 archives are corrected.
- Run quick local checks, mandatory fresh-agent review, then push and use the
  resource-aware GitHub image workflow for expensive integration tests.
- Make changes to the image detector trigger its own workflow and select every
  concrete image so detector regressions cannot silently skip coverage.

## Integration plan after run 32094157385

### 1. Integrate the verified slice

Status: completed at `b6b57f486` on `staging`. The fresh mandatory review
returned PASS with no findings. The normal staging push started the complete
51-image workflow plus CI and RuboCop.

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
- Fast-forward `staging` and push it with the existing ordinary commit
  messages. Do not use GitHub commit-message skip directives. Because the
  slice changes the detector and shared runtime, the normal push is expected
  to schedule all 51 images again; monitor and diagnose that run normally.

### 2. Fix the Arch exporter corruption

- Replace the Ruby `Zlib::GzipWriter` path with an external gzip process. The
  exporter must check both `zfs send` and `gzip` status before accepting an
  archive member.
- Audit every supported libosctl caller for a declared GNU gzip runtime. Keep
  the retired OpenVZ converter out of scope. Record the conditional external
  requirement in the standalone libosctl gem metadata.
- Add a focused regression that reproduces producer exit and Ruby signal
  delivery while verifying the exact uncompressed payload. The test must fail
  against the old exporter and pass without relying on retries.
- Keep this independent artifact-integrity fix separate from Guix and from any
  outer tar-finalization cleanup.
- Run quick tests and mandatory review before targeted integration coverage.

### 3. Rewrite the feature branch to unresolved work only

- Build a new feature head from the integrated `origin/staging` instead of
  carrying the obsolete Debian bridge commits forward.
- Add `image-scripts/builders/guix` using `DISTNAME=guix` and
  `RELVER=latest`, point the Guix image at it, and remove the now-unused
  `debian-guix` builder.
- Replace the Guix 1.4 bridge, version probe, retry loop, and rolling pull with
  one authenticated `guix time-machine` invocation. At build time, use Guix's
  CI API to resolve the newest default-branch revision with package-definition
  substitutes, validate the returned commit, and pass it with `--commit`.
- Move the complete operating-system record and its delayed service
  construction into the retained named module as a platform base. Have the
  disposable wrapper resolve and inherit that base at run time without
  importing an alias into the anonymous configuration module. Keep literal
  user defaults such as host name, timezone, and locale visible and editable in
  `system.scm`; inherited delayed fields remain owned by the named module.
  Self-hosting removes the old bootstrap cost, but does not by itself fix this
  compatibility break.
- Replace the removed, deprecated ISC dhclient service with Guix's supported
  dhcpcd service while preserving automatic interface discovery and the
  `networking` Shepherd provision.
- Keep a custom module already supplied through Guix's load path and add the
  fixed `/etc/config` path only as an installed-system fallback. Image builds
  pass the current repository directory with `-L`, so the older copy in the
  published builder cannot shadow the replacement module.
- Preserve the last known-good dated Guix image. There will be no standing
  NixOS or foreign-distribution recovery builder; an exceptional recovery can
  explicitly select that dated image if it is ever needed.
- After quick checks and mandatory review, update the clean continuation
  branch with `--force-with-lease`; it is unmerged feature history and its
  Guix implementation was deliberately rewritten after review. Cancel only
  superseded workflow runs whose head no longer matches the branch.
- Retain the former feature branch as historical integrated development state,
  but treat the continuation branch as the active feature branch containing
  only unresolved work.

### 4. Validate and integrate Guix

- Inspect the Guix-only artifact even if the job passes, confirming that the
  base is the published Guix image, the CI-backed default-branch revision is
  selected, one time-machine generation is realized, the custom service list
  resolves, the image imports, and runtime tests pass.
- Fast-forward the verified Guix commits into `staging`. Do not skip this
  Guix-only workflow because it is new implementation rather than already
  exercised code.

### 5. Arch root-cause result

- The requested integration-first ordering is complete. The exporter bug is
  independently reproducible and is not Arch-specific: Ruby receives
  `SIGCHLD` as the `zfs send` child exits while `GzipWriter#close` is finishing
  the deflate stream.
- Ruby zlib 3.2.3 can return from interrupted `Z_FINISH` before
  `Z_STREAM_END` when no input remains. It then writes the correct CRC/ISIZE
  footer after an incomplete deflate payload, so export reports success and
  the later import reports unexpected EOF.
- Prevent the race with the external gzip pipeline in step 2. Do not use an
  Arch-specific workaround or a retry as the resolution.

## Compatibility and deployment

- The external-compressor change affects gzip-compressed ZFS exports made by
  osctld and osctl-image, including image building. The archive format is
  unchanged. Supported vpsAdminOS paths already declare GNU gzip, so no
  coordinated node rollout is required. The standalone libosctl gem records
  the conditional external requirement. The legacy OpenVZ converter is
  intentionally excluded.
- There are no API, schema, protocol, or persisted-state changes.
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
- The Guix image follows the authenticated default branch with a small CI
  substitute lag rather than a repository pin. Builds are less byte-for-byte
  reproducible across time, but they need no manual pin maintenance and fail
  closed when the CI-backed revision cannot be resolved.

## Testing plan

- Run shell, Ruby, Nix, channel, detector, and failure-propagation checks
  locally, followed by Overcommit.
- Run the mandatory standalone review after all intended commits and quick
  verification, before any expensive image tests.
- Push the rewritten follow-up branch and let
  `.github/workflows/image-scripts.yml` build and test only Guix with
  resource-aware `--jobs auto`.
- Inspect logs and artifacts for every failure, fix causes, and cancel
  superseded runs after follow-up pushes.

## Guix documentation follow-up

Status: the platform DNS fix and recovery bootstrap are integrated into
`staging` at `ce9d7dda3` after the exact feature head passed its Guix-only
workflow. Publication of the corrected Guix image is the next deployment gate;
the documentation runtime and release stay pending until that artifact exists.

- Update the managed Czech and English Guix pages for the deployed
  `guix/20260819` image. Explain that `system.scm` inherits the maintained
  `%ct-operating-system-base`, while member settings such as host name,
  timezone, locale, and packages remain visible in `system.scm`.
- Keep the complete `guix deploy` example, but inherit the platform base and
  construct the modified service list before the `operating-system` record.
  This keeps delayed Guix fields independent of the disposable configuration
  module and avoids duplicating bootloader, kernel, file-system, and essential
  service details.
- Update the executable fixture and Guix runtime contract to use image
  `20260819`, verify the new platform inheritance and dhcpcd integration, run
  the documented deployment dry run, and then perform the real deployment.
- Keep vpsAdminOS-managed resolver configuration intact. The published image's
  all-interface dhcpcd service currently invokes its resolver hook after
  osctld injects `/etc/resolv.conf`, replacing the configured nameserver with
  an empty generated file. Disable only dhcpcd's resolver hook so development
  DHCP and the `networking` Shepherd provision remain available.
- Bootstrap the corrective build from known-good `guix/20260613`, because the
  broken `20260819` artifact is currently both `latest` and `stable` and cannot
  repair itself before builder networking is checked. After publishing the
  correction, restore the builder to `latest` and run a second Guix-only build
  to prove the normal self-hosted path before integration.
- Run the contract's quick validation in its pinned Nix shell, commit the
  focused bilingual change, and obtain a fresh mandatory change review before
  pushing the feature branch for GitHub runtime testing.
- After the exact feature revision passes, build and stage bilingual managed
  KB candidates and a schema-5 release manifest. Production promotion remains
  approval-gated and requires the contract revision to be integrated into
  `master` first.

### Documentation compatibility and deployment

- The pages document only the current supported `guix/20260819` image. The
  runtime test does not retain compatibility branches for older untagged Guix
  images.
- The change affects documentation, its executable example, and test fixtures
  plus the Guix image's DHCP resolver integration. It changes no API, schema,
  protocol, or persisted-state format. Existing `20260819` containers keep the
  faulty service until they reconfigure from the corrected platform module;
  a corrected image must be built and published, and the managed runtime must
  target that exact corrected artifact, before the documentation release can
  advance.
- Staging can use the committed and pushed feature revision. Production will
  be updated only after explicit approval and after a fast-forward integration
  of the contract branch into `master`.
