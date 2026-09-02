# 2026-09-02-vpsadminos-chattr-test

## Repositories

- `vpsadminos`
  - branch: `2026-09-02-vpsadminos-chattr-test`
  - worktree:
    `worktrees/2026-09-02-vpsadminos-chattr-test/vpsadminos`
  - base: fetched `origin/staging` at
    `f38b0018ee80bb2c36fb7940b4bcfd185f8e7194`
- `zfs`
  - branch: `2026-09-02-vpsadminos-chattr-test`
  - worktree: `worktrees/2026-09-02-vpsadminos-chattr-test/zfs`
  - base: fetched default `origin/vpsadminos-release-next` at
    `f53469bdcd88043b2bfe9a07ac80447f98b8e1e4`
  - current vpsAdminOS staging pin is direct descendant
    `6f5f54c3bfd68c1e52b0b6f454ee9679aaa9e83d`

## Status

- Separate session `2026-09-02-vpsadminos-chattr-test` created without
  attaching or starting another Codex process.
- Both project worktrees are based on their fetched default branches and are
  clean.
- Root cause is confirmed. No product changes or commits have been made yet.
- Recommended implementation and invocation alternatives are recorded in
  `plan.md`.

## Commands run

- `git --git-dir=repos/vpsadminos.git fetch origin`
- `bin/dev-session start 2026-09-02-vpsadminos-chattr-test --as-is
  --no-attach --no-codex`
- `bin/dev-session worktree add ... vpsadminos --base origin/staging`
- `git --git-dir=repos/zfs.git fetch origin`
- `bin/dev-session worktree add ... zfs
  --base origin/vpsadminos-release-next`
- Inspected vpsAdminOS test history, LXC capability configuration, pinned ZFS
  source, and historical fork implementations `454a692c3` and `8374426f6`.
- `./test-runner.sh ls '*misc*'`
- `./test-runner.sh debug 'kernel/vpsadminos#misc-attrs'`
- In the live cgroups-v2 VM, created native-map and ZFS-map Alpine containers,
  inspected capabilities/user namespaces, ran `chattr`/`lsattr`, and removed
  both containers before stopping the VM.
- Inspected BusyBox 1.37.0 and e2fsprogs 1.47.4 `chattr` sources from Nixpkgs
  source derivations.
- Checked whether historical OpenZFS patches apply cleanly to current default;
  they require a manual, focused backport because the histories diverged.

## Results

- Native-map container:
  - map mode `native`, init PID user namespace directly below init userns;
  - `CapEff=000001ffffffffff`, including `CAP_LINUX_IMMUTABLE`;
  - BusyBox `chattr +i /immutable.file` printed `Permission denied`, returned
    status 0, and `lsattr` showed no immutable flag.
- ZFS-map control container with the same effective capabilities:
  - `chattr +i` and `chattr -i` both returned 0;
  - `lsattr` showed the immutable flag set and then cleared.
- Existing OpenZFS first-level-userns patch passes the namespace capability
  gate, but the following ownership gate still uses `zfs_init_idmap`. On a
  native/idmapped mount it compares the container credential against the
  underlying host UID and returns `EACCES`.
- BusyBox 1.37.0 logs `EXT2_IOC_SETFLAGS` errors but unconditionally returns
  `EXIT_SUCCESS`. e2fsprogs propagates `change_attributes()` failures through
  a nonzero process exit.
- The isolated VM reused the cached 6.12.95 kernel. It rebuilt current
  userspace/test closures only; no local kernel build occurred.

## Open questions

- Confirm whether to implement the recommended focused OpenZFS backport plus
  semantic test rewrite, or choose the compiled ioctl-helper variant.
- Decide whether the broader historical fileattr callback coverage should be
  kept in the backport for forward kernel compatibility or reduced to the
  legacy ioctl path used by the current 6.12 kernel. The recommendation is to
  retain the focused callback/setter coverage from `454a692c3`.

## Cleanup

- Debug containers were deleted and both debug VMs were stopped normally.
- Project worktrees are intentionally retained for implementation.
- No branch has been pushed.
