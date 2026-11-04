# Focused candidate matrix result

Partial batch; further cases were not started after the lead relayed the user's
scope clarification. Evidence is for source `aa963dce42859ae4251cdfaded91920d67b3a46e`
and the fixed input
`candidate-focused-aa963dce4.rb` (SHA256
`260bf1802900fdb8c3842788928feef0a31c906e66ec587b33d53509e9bf9987`).

Candidate repository tar:
`/tmp/2026-11-03-opensuse-leap-image-build-candidate-repo.tar`, SHA256
`36069c59b286fdeb81988e87482b519bb8fcea62a916e0a1d0eaac819e0c57d3`.
Extracted image archive:
`/tmp/2026-11-03-opensuse-leap-image-build-candidate-repo/v1/vpsadminos/minimal/x86_64/opensuse/leap-16.1/image-archive.tar`, SHA256
`254523b59106db1d27bcf98e43e942c8ea1d7f0c15238542ca17e21612017214`.
The loopback server on `127.0.0.1:18080` served `/v1/INDEX.json` byte-for-byte
equal to the extracted index. Its full log is
`candidate-http.log`; it was stopped with Ctrl-C and port 18080 is no longer
listening.

| Case | Exact command | Result evidence | PTY / native state |
|---|---|---|---|
| `systemd/device-units#opensuse-leap-16.1` | `env VPSADMINOS_CONFIG=/home/aither/workspace/ai/vpsfree.cz/work/2026-11-03-opensuse-leap-image-build/test-revision.nix ./test-runner.sh debug --state-dir /tmp/2026-11-03-opensuse-leap-image-build-device-units systemd/device-units#opensuse-leap-16.1` | JSON `success=false`, `elapsed_time=86.294370068`, `expected_to_succeed=true`; no pass marker. Raw raised failure: `OsVm::TimeoutError` running `osctl ct exec testct-553b systemctl status sys-devices-virtual-net-eth0.device`, empty output. PTY wrapper exit 0 after normal Pry exit; no retry. | `candidate-device-units.log`; native state `/tmp/2026-11-03-opensuse-leap-image-build-device-units/os-test-systemd__device-units-e983cb16`; runner and matching QEMU process closed. Retained disk and state files. |
| `dist-config/start-stop#opensuse-leap-16.1` | `env VPSADMINOS_CONFIG=/home/aither/workspace/ai/vpsfree.cz/work/2026-11-03-opensuse-leap-image-build/test-revision.nix ./test-runner.sh debug --state-dir /tmp/2026-11-03-opensuse-leap-image-build-start-stop dist-config/start-stop#opensuse-leap-16.1` | JSON `success=true`, `elapsed_time=248.382413708`, `expected_to_succeed=true`; marker `CANDIDATE_FOCUSED_PASSED dist-config/start-stop#opensuse-leap-16.1 source=aa963dce42859ae4251cdfaded91920d67b3a46e`. PTY wrapper exit 0 after normal Pry exit. | `candidate-start-stop.log`; native state `/tmp/2026-11-03-opensuse-leap-image-build-start-stop/os-test-dist-config__start-stop-3c0e3c48`; runner and matching QEMU process closed. Retained disk and state files. |

Not started: `cgroups/mount-v1#opensuse-leap-16.1` (state
`/tmp/2026-11-03-opensuse-leap-image-build-cgroup-v1`),
`cgroups/mount-v2#opensuse-leap-16.1` (state
`/tmp/2026-11-03-opensuse-leap-image-build-cgroup-v2`),
`dist-config/systemd-rundir#opensuse-leap-16.1` (state
`/tmp/2026-11-03-opensuse-leap-image-build-rundir`), and
`dist-config/netif-routed#opensuse-leap-16.1` (state
`/tmp/2026-11-03-opensuse-leap-image-build-netif-routed`).

At batch close, port 18080 was closed and no QEMU or test-runner debug process
was present. The candidate tar, extracted repository, both native state trees,
VM disks, native logs, and `.lock`/socket-pid files remain for the lead's cleanup
decision. The vpsadminos worktree remains clean at the tested head.
