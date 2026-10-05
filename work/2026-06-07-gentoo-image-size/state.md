---
lifecycle: active
---
# 2026-06-07-gentoo-image-size

## Repositories

- `vpsadminos`
  - Worktree: `worktrees/2026-06-07-gentoo-image-size/vpsadminos`
  - Branch: `2026-06-07-gentoo-image-size`
  - Base: `origin/staging` at `62de2d8b0`

## Status

- Gentoo image cleanup is implemented and measured.
- Current failures reported by user:
  - `gentoo-openrc`: 1,100,633,600 bytes used vs 1,073,741,824 limit.
  - `gentoo-systemd`: 1,139,144,192 bytes used vs 1,073,741,824 limit.
- Current upstream stage3 metadata from vpsFree Gentoo mirror:
  - `stage3-amd64-openrc-20260606T160131Z.tar.xz`: 301,363,636 bytes.
  - `stage3-amd64-systemd-20260531T160106Z.tar.xz`: 300,483,616 bytes.
- The stage3 payload has empty `/boot` and no installed kernel modules,
  kernel sources, or firmware payload. It contains only `sys-kernel/linux-headers`.
- Extracted stage3 directory breakdown shows the size is mostly Gentoo's
  source-based userland (`gcc`, Python, docs, locales, SGML/docbook data, etc.),
  not a kernel or firmware package.
- Candidate cleanup: remove Portage build/download/cache artifacts after the
  image update while preserving `/var/db/repos/gentoo`.
- An earlier trial that also removed `/var/db/repos/gentoo` finished the image
  build but failed during image import with `error: internal error`, before
  the `rootfs_size` test ran. The test was run with the default destructive
  mode, so the VM disk was removed before it could be inspected.

## Commands run

- `bin/dev-session current`
- `git --git-dir=repos/vpsadminos.git fetch origin`
- `bin/dev-session worktree add 2026-06-07-gentoo-image-size vpsadminos --as-is --branch 2026-06-07-gentoo-image-size --base origin/staging --no-fetch`
- `find worktrees/2026-06-07-gentoo-image-size/vpsadminos -name AGENTS.md -print`
- `sed -n '1,240p' AGENTS.md`
- `sed -n '1,260p' image-scripts/include/gentoo.sh`
- `sed -n '1,220p' image-scripts/images/gentoo-openrc/build.sh`
- `sed -n '1,220p' image-scripts/images/gentoo-systemd/build.sh`
- `rg -n "rootfs_size|1073741824|limit|size" image-scripts tests osctl-image osctl-repo osctld -g '*.rb' -g '*.sh' -g '*.nix'`
- `sed -n '1,120p' image-scripts/tests/rootfs_size.sh`
- `./test-runner.sh ls 'image-scripts/*gentoo*'`
- `curl -fsSL https://mirror.vpsfree.cz/gentoo/releases/amd64/autobuilds/latest-stage3-amd64-openrc.txt`
- `curl -fsSL https://mirror.vpsfree.cz/gentoo/releases/amd64/autobuilds/latest-stage3-amd64-systemd.txt`
- Downloaded current OpenRC and systemd stage3 tarballs under `/tmp/vpsadminos-gentoo-size/`.
- Extracted stage3 tarballs under `/tmp/vpsadminos-gentoo-size/` for local
  size inspection, excluding `/dev/*` because unprivileged extraction cannot
  create device nodes.
- `tar -tf ... | rg -n '(^|/)(boot|lib/modules|usr/src|firmware|linux|kernel)'`
- `du -xhd1 /tmp/vpsadminos-gentoo-size/{openrc,systemd} | sort -h`
- `du -xhd2 /tmp/vpsadminos-gentoo-size/{openrc,systemd}/{usr,var} | sort -h`
- `bash -n image-scripts/include/gentoo.sh image-scripts/images/gentoo-openrc/build.sh image-scripts/images/gentoo-systemd/build.sh`
- `./test-runner.sh test --no-destructive image-scripts/test@gentoo-openrc`
  (interrupted)
- Temporarily lowered `tests/suite/image-scripts/test.nix` VM memory to
  12 GiB to test whether the earlier boot hang was `/dev/shm` related. The VM
  booted and reached `osctl-image`, confirming the diagnosis. The temporary
  harness change was then reverted before continuing.
- `./test-runner.sh test --fresh --no-destructive image-scripts/test@gentoo-openrc`
  (interrupted after confirming the 12 GiB VM booted)
- `./test-runner.sh test --fresh --no-destructive image-scripts/test@gentoo-openrc`
  (normal 24 GiB run passed)
- `./test-runner.sh test --fresh --no-destructive image-scripts/test@gentoo-systemd`
  (normal 24 GiB run passed)
- Temporarily instrumented `tests/suite/image-scripts/test.nix` to instantiate
  Gentoo images and print ZFS dataset usage after the image build, without
  running the image test suite.
- `./test-runner.sh test --fresh --no-destructive image-scripts/test@gentoo-openrc`
  with the temporary measurement harness. The combined OpenRC/systemd probe was
  interrupted after recording the OpenRC size.
- `./test-runner.sh test --fresh --no-destructive image-scripts/test@gentoo-systemd`
  with the temporary measurement harness.
- Reverted the temporary measurement harness before committing.
- `nix develop --command overcommit --install`
- `nix develop --command overcommit --run`
- `nix develop --command git commit -F /tmp/vpsadminos-gentoo-image-size-commit-msg.txt`
- `git fetch origin staging`
- `nix develop --command git rebase origin/staging`
- `nix develop --command git commit --amend -F /tmp/vpsadminos-gentoo-image-size-commit-msg.txt`
- `nix develop --command git commit --amend -F /tmp/vpsadminos-gentoo-image-size-commit-msg.txt`
  (amended the commit message to round MiB values to one decimal place)
- `git fetch origin staging`
- `nix develop --command git rebase origin/staging`
- `nix develop --command git -C /home/aither/workspace/ai/vpsfree.cz/repos/vpsadminos.git worktree add /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-06-07-gentoo-image-size/vpsadminos-staging-merge staging`
- `nix develop --command git merge --ff-only 2026-06-07-gentoo-image-size`
- `nix develop --command git push origin staging`
- `git worktree remove /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-06-07-gentoo-image-size/vpsadminos-staging-merge`
- `git worktree remove /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-06-07-gentoo-image-size/vpsadminos`

## Results

- `./test-runner.sh ls 'image-scripts/*gentoo*'` listed:
  - `image-scripts/test@gentoo-musl-openrc`
  - `image-scripts/test@gentoo-musl-systemd`
  - `image-scripts/test@gentoo-openrc`
  - `image-scripts/test@gentoo-systemd`
- `rootfs_size.sh` uses a global 1 GiB limit for all images.
- Local stage3 extraction sizes:
  - OpenRC: 1.5G apparent filesystem usage, mostly `/usr`.
  - Systemd: 1.4G apparent filesystem usage, mostly `/usr`.
- Large stage3 directories include GCC, Python, docs, man pages, locales, SGML,
  and headers. These are normal for a Gentoo stage3 and predate the image
  build script.
- Stage3 already includes `net-misc/dhcpcd` and `sys-apps/iproute2`; the
  image script additionally installs `app-editors/vim`.
- The current cleanup removes `/usr/portage/distfiles/*`, which is the old
  Portage distfiles path and does not cover current Gentoo defaults such as
  `/var/cache/distfiles`, `/var/cache/binpkgs`, `/var/cache/binhost`, and
  `/var/tmp/portage`.
- The patch now removes those cache/build directories and recreates them, but
  keeps the synced Portage repository so package management remains usable in
  the image.
- A rerun of `gentoo-openrc` with `--no-destructive` was interrupted before
  the image script started. Another vpsAdminOS image test VM was already
  running, both VMs allocated 24 GiB under `/dev/shm`, `/dev/shm` reached
  100%, and the Gentoo VM reported kernel soft lockups during early boot. This
  was treated as an infrastructure/resource-contention failure, not a Gentoo
  image result.
- Added `notes/vpsadminos/2026-06-07-os-test-runner-dev-shm-contention.md`
  with the `/dev/shm` contention symptom and workaround.
- `gentoo-openrc` passed all 15 image tests in 5984.63 seconds with the
  unchanged 1 GiB rootfs size limit. The successful `rootfs_size` test does
  not print the exact byte count, but it passed where the original reported
  build exceeded the limit.
- `gentoo-systemd` passed all 15 image tests in 8129.27 seconds with the
  unchanged 1 GiB rootfs size limit. The successful `rootfs_size` test does
  not print the exact byte count, but it passed where the original reported
  build exceeded the limit.
- Exact rootfs size comparison against the 1,073,741,824 byte test limit:
  - `gentoo-openrc`: 1,100,633,600 bytes before; 960,751,616 bytes after.
    Savings: 139,881,984 bytes. Margin below limit: 112,990,208 bytes.
  - `gentoo-systemd`: 1,139,144,192 bytes before; 991,100,928 bytes after.
    Savings: 148,043,264 bytes. Margin below limit: 82,640,896 bytes.
- Local commit after rebase and message amend:
  `4d972179a0411fbd359d13f52fbfcf7466f73877`.
  The commit message uses one-decimal MiB values for the before/after
  comparison, savings, and remaining margins.
- Merged to `staging` with a fast-forward merge and pushed to `origin/staging`.
  Local `staging`, `origin/staging`, and branch
  `2026-06-07-gentoo-image-size` all point to
  `4d972179a0411fbd359d13f52fbfcf7466f73877`.

## Open questions

- None.

## Cleanup

- Removed `/tmp/vpsadminos-gentoo-size/`.
- Removed preserved `machine-sda.img` files from successful `--no-destructive`
  OpenRC/systemd test runs after recording results.
- Removed `machine-sda.img` files left by the temporary measurement/debug runs:
  `/tmp/os-test-runner/os-test-image-scripts__test__gentoo-openrc-0f02f1ae/`
  and
  `/tmp/os-test-runner/os-test-image-scripts__test__gentoo-systemd-4d7b5760/`.
- Removed the full temporary measurement state directories for OpenRC and
  systemd from `/tmp/os-test-runner/`.
- Removed `/tmp/vpsadminos-gentoo-image-size-commit-msg.txt`.
- Removed the feature and temporary staging merge worktrees under
  `worktrees/2026-06-07-gentoo-image-size/`, then removed the empty parent
  directory. Branch refs were left intact.
