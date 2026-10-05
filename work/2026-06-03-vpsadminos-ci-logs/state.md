---
lifecycle: active
---
# vpsAdminOS CI log investigation state

## Status

- 2026-06-03: Investigated recent `ci.yml` failures and identified the
  recurring root cause as oversized EL8 container images from the live image
  repository, especially AlmaLinux 8 and Rocky 8 images published on
  2026-05-30.

## Branches and worktrees

- Bare repository: `repos/vpsadminos.git`.
- Detached investigation worktree, removed after investigation:
  `worktrees/2026-06-03-vpsadminos-ci-logs/vpsadminos` at
  `cb665cd2688c3b2d69e37585449c2ba26276a417`.
- No repository source changes were made.

## Commands and results

- `gh run list -R vpsfreecz/vpsadminos --workflow ci.yml --limit 30 --json ...`
  showed recent failures in the `Run test suite` job. Run
  `26889296877` failed on `staging` at SHA `cb665cd2688c`, while run
  `26887953161` passed on branch `2026-05-31-vpsadminos-firewall-notrack` at
  the same SHA. This points away from a deterministic code regression.
- Downloaded failed test artifacts with `gh run download` for runs
  `26889296877`, `26885780878`, and `26884642104` under
  `/tmp/vpsadminos-ci-logs/`.
- Failed scripts repeatedly died during:
  `osctl ct new --distribution almalinux --version 8 ...` or
  `osctl ct new --distribution rocky --version 8 ...`.
- Client-visible failure in artifacts:
  `error: internal error`, after progress lines `Importing rootfs` and
  `Writing data stream`, followed by `Error occurred, cleaning up`.
- The uploaded artifacts do not include `/var/log/osctld`, where the
  server-side exception and exact `zfs recv` stderr are logged.
- Checked published repository metadata:
  `https://images.vpsadminos.org/v1/INDEX.json` resolves `almalinux:8` and
  `rocky:8` to:
  `vpsadminos/minimal/x86_64/almalinux/8/image-stream.tar` and
  `vpsadminos/minimal/x86_64/rocky/8/image-stream.tar`.
- HTTP headers show the EL8 streams were published on Saturday, 2026-05-30:
  AlmaLinux 8 `content-length: 1217316864`,
  Rocky 8 `content-length: 1222046208`.
- Validated both published EL8 streams with:
  `curl .../image-stream.tar | tar -xOf - rootfs/base.dat.gz | gzip -dc |
  nix shell nixpkgs#zfs -c zstreamdump`.
  Both streams are structurally valid, so the artifacts are not simply
  truncated or corrupt.
- Checked upstream EL8 `core` comps metadata for AlmaLinux 8 and Rocky 8.
  The group includes firmware as default packages:
  `linux-firmware`, multiple `iwl*-firmware` packages, and `microcode_ctl`.
- Ran isolated local reproductions from the detached worktree:
  - `./test-runner.sh test --test-config tests/test-configs/ci.nix
    --state-dir /tmp/vpsadminos-local-repro-el8 -f -t ci
    'cgroups/mount-v1#almalinux-8'`
    passed. The script took 312.44s; the `ct new` import took 66.02s.
  - `./test-runner.sh test --test-config tests/test-configs/ci.nix
    --state-dir /tmp/vpsadminos-local-repro-rocky8 -f -t ci
    'cgroups/mount-v1#rocky-8'`
    passed. The script took 306.27s.
- A too-broad local run of `cgroups/mount-v1*` was started, then stopped after
  user feedback. No useful result came from that run.

## Findings

- The recurring `ci.yml` failures are not caused by the individual cgroups,
  dist-config, systemd, or Docker assertions. They fail before those assertions,
  while creating AlmaLinux 8 or Rocky 8 containers from the live image
  repository.
- The failures started after the Saturday image repository publication on
  2026-05-30 and affect different branches/commits, including a same-SHA pass
  and fail, which makes an external image/test-load issue more likely than a
  repository code regression.
- The new EL8 images are large because the EL8 `core` group installs firmware
  packages by default. These packages are not useful inside containers.
- In isolation, the exact failing EL8 scripts pass locally but take just over
  five minutes. Under CI parallelism, the same oversized imports intermittently
  fail at the image import pipeline:
  `tar -xOf image-stream.tar rootfs/base.dat.gz | gunzip | zfs recv -F ...`.
- Recommended image-side fix: avoid installing firmware in the EL8 container
  images, for example by adding an optional `exclude=` setting to the Red Hat
  image helper's generated yum config and setting
  `EXCLUDEPKGS='*-firmware microcode_ctl'` for `almalinux-8` and `rocky-8`.
- Recommended CI/logging follow-up: include `/var/log/osctld` in failed test
  artifacts, because client-side artifacts flatten server exceptions to
  `error: internal error`.

## Cleanup

- Temporary GitHub Action logs remain under `/tmp/vpsadminos-ci-logs/`.
- Temporary local test state remains under:
  `/tmp/vpsadminos-local-repro-el8`,
  `/tmp/vpsadminos-local-repro-rocky8`, and
  `/tmp/vpsadminos-local-repro-mount-v1`.
- Detached investigation worktree was removed.
