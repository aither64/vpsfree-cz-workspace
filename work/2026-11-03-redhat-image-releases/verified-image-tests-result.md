# Verified Red Hat image tests

- Result: passed; all four selected image test cases succeeded.
- Tested revision: `vpsadminos` head `1a637e9eac4311adba2b08d60dfa7a17d07bcb52`, tree `49b8a7879e6b363349ae70808c4cdecc996e578e`.
- Command: the exact normal `nix develop .#test-runner --command env ... bundle exec ./test-runner/bin/test-runner test --state-dir /tmp/redhat-image-releases-2026-11-03-verified8g --jobs 2 --stop-on-failure 'image-scripts/test@{centos-9-stream,centos-10-stream,rocky-9,rocky-10}'`; full command and output are in `verified-image-tests.log`.
- Exit status: 0. Runner-reported batch duration: 2716.16 seconds.
- Scoped module: `/home/aither/workspace/ai/vpsfree.cz/work/2026-11-03-redhat-image-releases/verification-memory.nix`, SHA256 `adef87cd3c928b4a5687150fc5a43f271e64f1fceeb64745bcc4639aad62b582` before and after. This authorized resource-only module set image test memory to 8192 MiB; native maximum memory and shared-memory reservations remained 8192 MiB each. Each of the four generated configs recorded memory=8192, maxMachineMemoryMiB=8192, shmMiB=8192, cpus=4, machines=1.

| Image test | Result | Elapsed |
| --- | --- | ---: |
| `centos-9-stream` | passed | 1299.36 s |
| `centos-10-stream` | passed | 1300.69 s |
| `rocky-9` | passed | 1391.30 s |
| `rocky-10` | passed | 1415.45 s |

Generated VM configs identify the captured source `/nix/store/91nflgfhifb631q7816j30smqm76afjv-source`, kernel `/nix/store/b043pwyanxjfz22hbiibv5wipqqcl932-linux-6.12.113/bzImage`, OS toplevel `/nix/store/m057pgvaaf9f7cwvdwzb3c25wrlbmbn4-vpsadminos-system-vpsadminos-26.05.git.1a637e9`, initrd `/nix/store/p1a2p526kvg1zsz7j5wwmg68i9m1z2zm-initrd/initrd`, and QEMU `/nix/store/kanckc6ljipqzjsrvj4aqaf87a4rhswr-qemu-host-cpu-only-for-vm-tests-10.2.4`. Each case used its generated VM test configuration under `/nix/store` (exact derivation IDs and machine config are preserved in its `config.json` under `/tmp/redhat-image-releases-2026-11-03-verified8g/os-test-image-scripts__test__<image>-*/`). Input graphs were retained by the normal runner invocation for the full batch; no cached JSON was used.

Per-case raw evidence is in `/tmp/redhat-image-releases-2026-11-03-verified8g/`; full runner output and captured exact exit status are in `verified-image-tests.log`. The scoped runner/QEMU processes were verified absent after completion.

Existing GitHub workflows 41695651867 (image workflow) and 41695511680 (generic CI), both at the tested head, remained queued at final observation. No workflow was launched, retried, or cancelled.
