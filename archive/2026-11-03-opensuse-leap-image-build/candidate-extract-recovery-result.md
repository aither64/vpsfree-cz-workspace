# Candidate extraction recovery result

Result: completed successfully; no watchdog or soft-lockup message appeared.
The guest booted through stages 1–2, the fixed extraction eval printed
`Candidate repository exported`, and Pry exited normally. Native debug runner
exited 0 at 20:14:38 +0100. VM and exact debug runner processes are closed.

- Tested head: `aa963dce42859ae4251cdfaded91920d67b3a46e`.
- Command: `env VPSADMINOS_CONFIG=/home/aither/workspace/ai/vpsfree.cz/work/2026-11-03-opensuse-leap-image-build/export-revision-aa963dce4.nix ./test-runner.sh debug --state-dir /tmp/2026-11-03-opensuse-leap-image-build-image image-scripts/test@opensuse-leap-16.1`.
- Config: `/nix/store/8vnrdmp1xjdj4jnl21ynjvzahamsd9l5-os-test-image-scripts-test-opensuse-leap-16.1.json`, SHA256 `a13371204163888ce6725a904b213ceda6cbf8c16c0f568c4eb3e4fb7aad2a77`; memory 8192 MiB, 4 CPUs, expected kernel/initrd, 10 GiB file disk.
- Retained disk: `/tmp/2026-11-03-opensuse-leap-image-build-image/os-test-image-scripts__test__opensuse-leap-16.1-90ada9d4/machine-sda.img`, 10,737,418,240 bytes; device 64769, inode 33618419. Disk remains present.
- Builder: openSUSE Leap 16.0, RPM 4.20.1, builder `d5ddc633`.
- Cached builder archive: `/tank/repository/default/v1/vpsadminos/minimal/x86_64/opensuse/leap-16.0/image-stream.tar`, SHA256 `d279c082fb997e17996af6fe00f8b54d23a847247c2498090a24b3f26538dbe2`.
- Candidate image archive: `/tank/image-scripts/output/opensuse-leap-16.1-x86_64-vpsadminos-minimal-archive.tar`, SHA256 `254523b59106db1d27bcf98e43e942c8ea1d7f0c15238542ca17e21612017214`.
- Exported repository: `/tmp/2026-11-03-opensuse-leap-image-build-candidate-repo.tar`, 169,820,160 bytes, SHA256 `36069c59b286fdeb81988e87482b519bb8fcea62a916e0a1d0eaac819e0c57d3`.
- Full PTY transcript: `candidate-extract-recovery.log`. Native shell log SHA256 `b674243c4d2247285741808d5135b4b904722ede3dd6f56a53f965dc1634769d`; console log SHA256 `0698c4bfdea11ff7041205b90f3ab3143bae9792a7e9b3d0f22e50fde369436f`.

The prior 15/15 primary test remains valid. This recovery established candidate
export only; it does not establish a kernel or KVM fix and did not run focused
candidate-image tests. Logs, exported tar and disk are retained.
