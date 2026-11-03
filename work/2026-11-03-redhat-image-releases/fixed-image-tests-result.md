# Fixed Red Hat family image verification

- Result: incomplete, interrupted by authorized watcher cancellation after guest boot failure evidence. This is not an RPM image test result; only `centos-10-stream` started and it did not reach the test script.
- Tested head: `1a637e9eac4311adba2b08d60dfa7a17d07bcb52` (tree `49b8a7879e6b363349ae70808c4cdecc996e578e`).
- Original command:

```sh
nix develop .#test-runner --command env -u VPSADMINOS_CONFIG -u TEST_RUNNER_SOURCE_INFO -u TEST_RUNNER_REPO_ROOT RUBYLIB=/nix/store/givmi31xrbr231gxnry1xc2ggb5s4imf-libosctl-native-local/lib TEST_RUNNER_REPO_REV=1a637e9eac4311adba2b08d60dfa7a17d07bcb52 bundle exec ./test-runner/bin/test-runner test --state-dir /tmp/redhat-image-releases-2026-11-03-fixed --jobs 2 --stop-on-failure 'image-scripts/test@{centos-9-stream,centos-10-stream,rocky-9,rocky-10}'
```

- The native runner exit status is `1`; it reported `centos-10-stream` failed after `791.89 seconds`. On parent authorization, SIGINT was sent to the owned nested test-runner PID `1332952`; its QEMU and virtiofs children stopped, and no owned batch process remained. The other three tests were not scheduled.
- Guest console evidence: watchdog soft-lockup warnings on CPU 1 and CPU 3 at guest times 489, 517, 545 and 573 seconds, each on `kworker/u16` workers. Latest captured excerpt is in `fixed-image-test-artifacts/centos-10-stream/machine-console.log`.
- Captured VM configuration: `/nix/store/28j5v77lm2dbb0mz4x5f2hf92fcgpzr7-os-test-image-scripts-test-centos-10-stream.json`; host source `/nix/store/91nflgfhifb631q7816j30smqm76afjv-source`; toplevel `/nix/store/m057pgvaaf9f7cwvdwzb3c25wrlbmbn4-vpsadminos-system-vpsadminos-26.05.git.1a637e9`; squashfs `/nix/store/gzxwwxir19348vqka5zxk60w3pl1xz97-squashfs.img`. Guest command carried `OSCTL_IMAGE_VPSADMINOS_REV=1a637e9eac4311adba2b08d60dfa7a17d07bcb52`.
- Complete top-level log: `fixed-image-tests.log`; captured per-test runner, console, shell, stage and host virtiofs logs plus JSON config: `fixed-image-test-artifacts/centos-10-stream/`. Original state remains under `/tmp/redhat-image-releases-2026-11-03-fixed/`.
