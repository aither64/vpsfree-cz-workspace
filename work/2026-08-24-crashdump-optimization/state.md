# 2026-08-24-crashdump-optimization

## Repository

- Project: `vpsadminos`
- Branch: `2026-08-24-crashdump-optimization`
- Worktree:
  `worktrees/2026-08-24-crashdump-optimization/vpsadminos`
- Base: `origin/staging` at `8e44a5124439b1f3048ffc56b1717614a5360358`
- Remote: `git@github.com:vpsfreecz/vpsadminos.git`

No production access or `vpsfree-cz-configuration` change is in scope.

## Progress

- Created the isolated feature branch and worktree.
- Implemented the single-session collector, bounded direct writer, local crash
  patches, telemetry, 512-process regression load, NFS checks, manual
  equivalence test, and six-case 5,000-process benchmark template.
- Quick validation and the mandatory review/fixes are complete. A focused
  reviewer follow-up found no unresolved blocking or important issues. VM
  validation, the replacement benchmark, and GitHub Actions are complete. The
  branch is pushed and ready for review.

## Commands and results

- Fetched `origin/staging` and created the worktree with `bin/dev-session`.
- Formatted and parsed changed Nix files with `nixfmt-rfc-style` and
  `nix-instantiate --parse`.
- Compiled both new C programs with `-Wall -Wextra -Werror` in `nix develop`.
- Built `crash-buffer`; its install checks passed for a 600 KiB stream, append,
  telemetry/marker creation, and an unavailable destination.
- The first crash build exposed malformed hand-written patch metadata. Corrected
  the hunk counts and rebuilt `crash-9.0.1` successfully at
  `/nix/store/v6dm7f3dq4yqxn9bylhsqxpcmwcb5adm-crash-9.0.1`.
- `./test-runner.sh ls 'crashdump/*'` discovered the three routine tests, the
  equivalence test, and all six benchmark instances.
- Installed the repository Overcommit hooks. `nix develop --command overcommit
  --run` passed Nixfmt and the full RuboCop hook.
- The initial commit `dad736d11` passed hooks and was submitted to the mandatory
  standalone review before any VM tests.

## Mandatory change review

The standalone reviewer reported two blocking and three important findings:

- report files could remain stale when reusing an output directory and crash
  initialization failed;
- the independent `ps -A` and `ps -m` patches had to be split from the session
  implementation;
- dirty dmesg data could contaminate the collector-plus-sync benchmark;
- the NFS test did not wait through sync and QEMU shutdown;
- the writer test covered open failure but not a post-open write failure.

The reviewer also advised centralizing the duplicated process-farm derivation.
All findings were addressed before VM tests:

- pre-truncate all eleven destinations and test a failed retry over seeded
  stale files;
- rewrite the branch as `abdf15465` (`os: speed up crash process reports`) and
  `efba51db6` (`os: reuse crash session for inspection`);
- sync after dmesg and before the benchmark start timestamp;
- wait for both NFS crash-kernel tail markers and machine shutdown;
- test ENOSPC through `/dev/full` and require the completion marker to remain
  absent;
- import one shared process-farm derivation in all three tests.

Both rewritten commits passed the installed hooks. The session commit was
amended after long validation with the benchmark medians; the amendment also
passed the installed pre-commit and commit-message hooks.

The same standalone reviewer completed the focused follow-up and confirmed
that all six findings were resolved, with no remaining blocking or important
findings.

## VM validation

- `./test-runner.sh test --fresh crashdump/default` passed all six examples in
  425.37 seconds. The test used the cached vpsAdminOS Linux 6.12.95 derivation;
  no local kernel compilation was scheduled.
- The first `crashdump/inspect` run exercised inspection successfully: it
  recorded 512 interruptible backtraces and last-run rows in one crash session,
  and the failed retry cleared all stale reports. The surrounding preparation
  example failed because `grep` raced with unrelated disappearing procfs
  entries while counting the already-ready process farm. Replaced the procfs
  glob in both inspection and benchmark tests with `pgrep -xc crash-load`.
- The fresh `crashdump/inspect` rerun passed all seven examples in 421.56
  seconds. Its crash-kernel collection example, including 512 sleepers and the
  failed-retry regression, completed in 106.45 seconds. The harness correction
  was folded into the session commit, which passed all installed hooks.
- `./test-runner.sh test --fresh crashdump/nfs-inspect` passed all five
  examples in 727.56 seconds. The full panic, direct NFS collection, final
  filesystem sync, reboot, QEMU shutdown, and server-side persisted-artifact
  verification example completed in 161.45 seconds.
- The first `crashdump/equivalence` run stopped at `sys.txt` because the test
  normalizer recognized the optimized `crash>` prompt but not the deliberately
  renamed baseline binary's `crash-legacy>` prompt. Read-only `debugfs`
  inspection of the preserved ext4 report disk confirmed the legacy report was
  complete and its normalized file alone was empty. Updated the normalizer to
  accept both explicit prompts and canonicalize them.
- The fresh `crashdump/equivalence` rerun passed in 683.26 seconds. All eleven
  normalized reports from the unpatched eleven-session collector and the
  patched single-session collector matched on one vmcore with 512 synthetic
  sleepers.
- Started the six fresh benchmark cases sequentially with
  `./test-runner.sh test -j 1 --fresh -t crashdump-benchmark`. The runner
  detected 63.5 GiB usable memory and 27.3 GiB usable shared memory after its
  reserves; each two-VM case reserves 12 GiB of each and six vCPUs.
- Benchmark `optimized-2` passed with 5,000/5,000 synthetic tasks:
  `collect_sync_ms=106130`, `panic_to_reboot_ms=247345`, and
  `output_bytes=5700668`.
- Benchmark `legacy-3` passed with 5,000/5,000 synthetic tasks:
  `collect_sync_ms=375060`, `panic_to_reboot_ms=524099`, and
  `output_bytes=5722641`. This first non-paired run comparison is 3.53x faster
  for collection and 2.12x faster for panic-to-shutdown; final claims will use
  the requested medians. The runner then started fresh `legacy-2`.
- Benchmark `legacy-2` passed with 5,000/5,000 synthetic tasks:
  `collect_sync_ms=347050`, `panic_to_reboot_ms=494380`, and
  `output_bytes=5722869`. The runner then started fresh `legacy-1`.
- Benchmark `legacy-1` passed with 5,000/5,000 synthetic tasks:
  `collect_sync_ms=356900`, `panic_to_reboot_ms=529943`, and
  `output_bytes=5722523`.
- The three-run legacy medians are `collect_sync_ms=356900` and
  `panic_to_reboot_ms=524099`. The runner then started fresh `optimized-3`.
- `optimized-3` failed before entering its crash kernel. The panic line lacked
  `Kdump: loaded`, QEMU exited two seconds later, and no collector timer or
  result file was created. `wait_for_service('crashdump')` had accepted the
  completed one-shot service without verifying `/sys/kernel/kexec_crash_loaded`.
  The retained logs do not contain the underlying kexec-load error. Added the
  same explicit kernel-loaded assertion and diagnostic capture used by routine
  crashdump tests to the benchmark and equivalence setups. The suite continued
  with `optimized-1`; rerun only fresh `optimized-3` afterward.
- `optimized-1`, instantiated before the assertion was added, failed in the
  same way: 5,000 tasks were ready, the panic line lacked `Kdump: loaded`, and
  QEMU exited before entering the crash kernel. No result was created. The
  initial six-case command therefore finished after 4,431.96 seconds with all
  three legacy cases and `optimized-2` successful; rerun fresh `optimized-1`
  and `optimized-3` with the explicit loaded-state gate.
- The guarded fresh `optimized-1` rerun confirmed
  `/sys/kernel/kexec_crash_loaded=1`, the panic line contained `Kdump: loaded`,
  and the benchmark passed with 5,000/5,000 tasks:
  `collect_sync_ms=82210`, `panic_to_reboot_ms=222490`, and
  `output_bytes=5700233`.
- The guarded `optimized-3` rerun stopped before creating the process farm and
  captured the root cause: the 8 GiB QEMU E820 map has about 3 GiB below 4 GiB,
  dmesg reported `cannot allocate crashkernel (size:0x100000000)`, and kexec
  reported that crashkernel memory was not reserved. A 4 GiB plain reservation
  is therefore layout-dependent in this guest. Changed the benchmark to the
  vpsAdminOS default 2 GiB crash reserve, which routine inspection tests already
  exercise and which better represents the constrained crash environment. This
  changes the benchmark environment, so discard all earlier benchmark timings
  and rerun all six fresh cases before making comparison claims.
- Started the replacement six-case sequential run from clean revision
  `54b1f8f85`, using 2 GiB crash memory and the explicit loaded-state gate.
  Only results from this run count toward final medians.
- Replacement `legacy-3` passed with the crash kernel loaded and 5,000/5,000
  synthetic tasks: `collect_sync_ms=331960`, `panic_to_reboot_ms=404527`, and
  `output_bytes=5722374`.
- Replacement `legacy-1` passed with the crash kernel loaded and 5,000/5,000
  synthetic tasks: `collect_sync_ms=402500`, `panic_to_reboot_ms=499807`, and
  `output_bytes=5722805`.
- Replacement `legacy-2` passed with the crash kernel loaded and 5,000/5,000
  synthetic tasks: `collect_sync_ms=337230`, `panic_to_reboot_ms=430011`, and
  `output_bytes=5722492`.
- The accepted replacement legacy medians are `collect_sync_ms=337230` and
  `panic_to_reboot_ms=430011`.
- Replacement `optimized-2` passed with the crash kernel loaded and
  5,000/5,000 synthetic tasks: `collect_sync_ms=191710`,
  `panic_to_reboot_ms=304659`, and `output_bytes=5700115`.
- Replacement `optimized-1` passed with the crash kernel loaded and
  5,000/5,000 synthetic tasks: `collect_sync_ms=106860`,
  `panic_to_reboot_ms=254620`, and `output_bytes=5699988`.
- Replacement `optimized-3` passed with the crash kernel loaded and
  5,000/5,000 synthetic tasks: `collect_sync_ms=84120`,
  `panic_to_reboot_ms=166799`, and `output_bytes=5699944`.
- The replacement six-case benchmark passed in 5,088.1 seconds. The accepted
  optimized medians are `collect_sync_ms=106860` and
  `panic_to_reboot_ms=254620`. Compared with the accepted legacy medians,
  collection plus sync fell from 337.230 to 106.860 seconds: 230.370 seconds
  saved, a 68.3% reduction and 3.16x speedup. Panic to QEMU shutdown fell from
  430.011 to 254.620 seconds: 175.391 seconds saved, a 40.8% reduction and
  1.69x speedup. Each median uses three fresh 4-vCPU, 8-GiB guests with 2 GiB
  crash memory, 5,000 verified tasks, direct NFS output, and final sync.
- Amended the metadata-only session commit to `efba51db6`, adding those exact
  medians and benchmark parameters to its body. Benchmark logs retain the
  pre-amend tree-equivalent revision `54b1f8f85`.
- Fetched unchanged `origin/staging` at `8e44a5124` and pushed
  `2026-08-24-crashdump-optimization` at `efba51db6` over SSH. GitHub Actions
  CI run `32800258240` started for that exact head.
- GitHub Actions CI run `32800258240` passed on `efba51db6`. The OS/cache build,
  AMD livepatch lifecycle, Intel livepatch lifecycle, and complete vpsAdminOS
  test suite all succeeded. The run completed in 68 minutes 54 seconds; its
  longer suite time is consistent with the added routine crashdump VM tests.

## Remaining

- Await review and integration. No production deployment or configuration pin
  is part of this initiative.

## Compatibility

Existing report filenames and status rows remain. New `session.txt`, `timings`,
and manifest keys are additive. Report payloads are written directly to the
destination with at most one 256 KiB writer; tmpfs contains only tiny control
files. Mixed versions and rollback require no coordination or conversion.

## Cleanup

Keep the feature branch after integration. Remove the worktree only after the
work is merged or abandoned.
