# Configured openSUSE Leap image test

- Result: failed (exit 1).
- Tested revision: `fe9182dd2fb1ba627c30d54c39c1acd7b140df69` (tree `05b7f416e90b321f7d9c81a21198ed8d5b1625a5`).
- Command: `env VPSADMINOS_CONFIG=/home/aither/workspace/ai/vpsfree.cz/work/2026-11-03-opensuse-leap-image-build/test-revision.nix ./test-runner.sh test --no-destructive --state-dir /tmp/2026-11-03-opensuse-leap-image-build-image image-scripts/test@opensuse-leap-16.1`
- Elapsed: 713 seconds. Test script failed after 703.18 seconds.
- Full output: `image-test-configured.log`.
- Runner state and retained machine artifacts: `/tmp/2026-11-03-opensuse-leap-image-build-image/os-test-image-scripts__test__opensuse-leap-16.1-90ada9d4/`.

Bounded runner evidence:

```text
[2026-11-03 18:59:16 +0100] Test 'image-scripts/test@opensuse-leap-16.1' failed after 703.18 seconds
[2026-11-03 18:59:16 +0100] Unexpectedly failed test scripts:
[2026-11-03 18:59:16 +0100]   image-scripts/test@opensuse-leap-16.1
error: one or more tests did not have expected results
```

Bounded native test log evidence:

```text
++ bootstrap_status=8
++ umount-chroot /build/installdir.02e72793
++ '[' 8 -ne 0 ']'
++ exit 8
error: build of opensuse-leap-16.1 on opensuse-leap failed with exit status 8
```

The command has exited. No retry or cleanup was performed; state and disk artifacts remain available for extraction.
