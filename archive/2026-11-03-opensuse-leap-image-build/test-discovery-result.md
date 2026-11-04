# Test discovery

- Result: all three listing commands completed with exit status 0; total elapsed time 209 seconds.
- Tested worktree: `worktrees/2026-11-03-opensuse-leap-image-build/vpsadminos`; HEAD `dd188397abe37d0bc33f4c5dfb3605206ce5e326` (the four-file Leap 16.1 patch remained staged at start).
- `./test-runner.sh ls 'image-scripts/test@opensuse-leap-16.1'`: exit 0; discovered `image-scripts/test@opensuse-leap-16.1`.
- `./test-runner.sh ls 'dist-config/*#opensuse-leap-16.1'`: exit 0; discovered `dist-config/netif-routed#opensuse-leap-16.1`, `dist-config/start-stop#opensuse-leap-16.1`, `dist-config/systemd-rundir#opensuse-leap-16.1`.
- `./test-runner.sh ls 'cgroups/mount-*#opensuse-leap-16.1'`: exit 0; discovered `cgroups/mount-v1#opensuse-leap-16.1` and `cgroups/mount-v2#opensuse-leap-16.1`.
- Lead correction: the original watcher summary omitted these cgroup matches;
  the full raw log lists both on lines 19/20. No listing rerun needed.
- Complete stdout/stderr and per-command exit markers: `test-discovery.log`.
- This was test discovery only; no integration test was run. No operation remains running.
