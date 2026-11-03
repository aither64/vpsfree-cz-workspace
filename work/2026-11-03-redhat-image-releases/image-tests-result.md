# Red Hat family image tests

- Result: failed, exit status 1; stop-on-failure prevented remaining three tests from starting.
- Revision: `3307df52ea5bf875e1d8a23318a64f569d8b3ebc`.
- Command: `./test-runner.sh test --state-dir /tmp/redhat-image-releases-2026-11-03 --jobs 2 --stop-on-failure 'image-scripts/test@{centos-9-stream,centos-10-stream,rocky-9,rocky-10}'`
- Elapsed: about 2m 8s total (including runner setup); first test ran 27.64s.
- Complete log: `work/2026-11-03-redhat-image-releases/image-tests.log`.
- Failed case: `image-scripts/test@centos-10-stream`; runner log: `/tmp/redhat-image-releases-2026-11-03/os-test-image-scripts__test__centos-10-stream-150f32eb/test-runner.log`.
- Bounded output evidence: Nix evaluation reported `error: cannot coerce null to a string: null`; runner command was `nix-build .../evaluate-tests.nix ... --argstr testPath image-scripts/test@centos-10-stream ... failed (1)`.
- Exact-head image workflow CI: run `41683688934`, `Build and test changed container images`, head `3307df52ea5bf875e1d8a23318a64f569d8b3ebc`; observed queued.
- No kernel build was observed. No test process remains active.
