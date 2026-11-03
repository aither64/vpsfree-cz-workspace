# Fedora 45 image test result

- Result: failed
- Exit status: 1
- Revision: `dd188397abe37d0bc33f4c5dfb3605206ce5e326`
- Command: `./test-runner.sh test image-scripts/test@fedora-45`
- Started (UTC): 2026-11-03T15:42:45Z
- Finished (UTC): 2026-11-03T15:43:25Z
- Elapsed: 40 seconds
- Test runner duration: 27.92 seconds
- Complete combined stdout/stderr: `work/2026-11-03-fedora-45-image-build/fedora-45-image-test.log`
- Native test state/log path: `/tmp/os-test-runner/os-test-image-scripts__test__fedora-45-07b223fa`
- Remaining operation: none; the runner exited.

Failure excerpt:

```text
Test 'image-scripts/test@fedora-45' failed after 27.9 seconds, see /tmp/os-test-runner/os-test-image-scripts__test__fedora-45-07b223fa
1 tests should have succeeded, but failed
Unexpectedly failed test scripts:
  image-scripts/test@fedora-45
error: one or more tests did not have expected results
```
