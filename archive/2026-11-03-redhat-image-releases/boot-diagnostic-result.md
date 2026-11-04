# CentOS 10 Stream boot diagnostic

- Result: incomplete, watchdog trace missing; this is not an image release pass.
- Revision: vpsadminos `1a637e9eac4311adba2b08d60dfa7a17d07bcb52`.
- Cached test JSON: `boot-diagnostic.json` (SHA256 `979baef5c043d88fa5b6eb26a1e377498bdcb81fb1f39f183d775f3d5f966038`).
- Preflight: passed. Pool reported shared memory available-at-start 34.5 GiB with 8.0 GiB reserve; requested one machine with 24 GiB memory, 24 GiB shm, 4 CPUs.
- Run: cached `test-json-runner`, `TEST_DESTRUCTIVE=0`, `TEST_JOBS=1`; elapsed 56.76 seconds; exit status 1 after authorized SIGINT.
- QEMU reached guest kernel startup. Serial output stopped at `mem auto-init: clearing system memory may take some time...`; no watchdog header, Call Trace, RIP dump, or shell/boot milestone appeared.
- Cancellation: SIGINT sent to nested runner PID 1457338. It exited and cleaned up. Runner PIDs 1457053/1457338, QEMU PID 1457850, and virtiofsd PIDs 1457356/1457359/1457367/1457370 are gone. No diagnostic processes or corresponding `/dev/shm` FDs remain.
- Full serial and runner evidence: `boot-diagnostic.log`. State directory retained at `/tmp/redhat-image-releases-2026-11-03-boot-diagnostic`.
