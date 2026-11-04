# CentOS Stream 10 boot diagnostic result

- Result: incomplete diagnostic; runner exited 1 after 603.99 seconds.
- Revision: `1a637e9eac4311adba2b08d60dfa7a17d07bcb52`.
- Cached input: `boot-diagnostic.json`, SHA-256 `979baef5c043d88fa5b6eb26a1e377498bdcb81fb1f39f183d775f3d5f966038`.
- Resource preflight passed; requested 24 GiB memory and 24 GiB shared memory fit available capacity.
- Guest reached `vpsadminos login: root (automatic login)`; shell commands subsequently ran. Guest kernel log timestamps reached about 475 seconds and it powered down at 513.57 seconds.
- No watchdog, Call Trace, or RIP was present in the retained console.
- The subsequent test command failed with status 64: `/mnt/vpsadminos` is not a vpsadminos checkout. The image test did not pass.
- Runner completed and its owned QEMU/virtiofs processes are gone. Test artifacts and disk image are retained.

Artifacts:

- Full runner output: `work/2026-11-03-redhat-image-releases/boot-trace.log`
- Full raw guest console: `/tmp/redhat-image-releases-2026-11-03-boot-trace/os-test-image-scripts__test__centos-10-stream-150f32eb/machine-console.log`
- Shell command log: `/tmp/redhat-image-releases-2026-11-03-boot-trace/os-test-image-scripts__test__centos-10-stream-150f32eb/machine-shell.log`
- Per-test runner log: `/tmp/redhat-image-releases-2026-11-03-boot-trace/os-test-image-scripts__test__centos-10-stream-150f32eb/test-runner.log`
