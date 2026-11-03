# Final image batch result

- Result: **incomplete**, exit status 1; no image case ran.
- Revision/tree: `1a637e9eac4311adba2b08d60dfa7a17d07bcb52` / `49b8a7879e6b363349ae70808c4cdecc996e578e`.
- Invocation: the authorized four-image `test-runner test` batch with `--state-dir /tmp/redhat-image-releases-2026-11-03-final8g --jobs 2 --stop-on-failure` for CentOS Stream 9/10 and Rocky 9/10.
- Elapsed: approximately 1.5 minutes, including source capture and Nix evaluation.
- Complete stdout/stderr and exit marker: `final-image-tests.log`.
- Captured source: `/nix/store/91nflgfhifb631q7816j30smqm76afjv-source`.
- Resource override: `/home/aither/workspace/ai/vpsfree.cz/work/2026-11-03-redhat-image-releases/verification-memory.nix`, SHA256 before and after `dbb827bbd3f6382d6a83eb559a623a22acdefe138d25e5272568b82fc63a053d`.
- Failure evidence: Nix metadata evaluation reports conflicting `boot.qemu.memory` definitions `4096` and `8192`, then `nix-instantiate ... evaluate-tests.nix ... mode testsMetaAll failed (1)`.
- Per-case results and generated VM system/kernel/initrd paths: unavailable; evaluation failed before cases were scheduled. No state directory or machine-console/machine-shell logs were created.
- No retry or cancellation was performed.
