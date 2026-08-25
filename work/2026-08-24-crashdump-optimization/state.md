# 2026-08-24-crashdump-optimization

## Repository

- Project: `vpsadminos`
- Branch: `2026-08-24-crashdump-optimization`
- Branch head retained locally: `3e936050a10cedc9e6cde7d10e42d779657d4bda`
- Worktree removed after abandonment:
  `worktrees/2026-08-24-crashdump-optimization/vpsadminos`
- Validation branch: `2026-08-24-crashdump-optimization-validation`
- Validation branch head retained locally:
  `3a823e5a2c1ba84fc01d3c962e8113b474f8dbca`
- Validation worktree removed after abandonment:
  `worktrees/2026-08-24-crashdump-optimization/vpsadminos-validation`
- Rewrite branch retained locally:
  `2026-08-24-crashdump-optimization-rewrite` at
  `9169a6dba3d65993e4296b3234cb7dc3d25e6246`
- Rewrite worktree removed after abandonment:
  `worktrees/2026-08-24-crashdump-optimization/vpsadminos-rewrite`
- Base: `origin/staging` at `399cc60d215fb9427447c37133b5eb27e9879a4e`
- Remote: `git@github.com:vpsfreecz/vpsadminos.git`

No production access or `vpsfree-cz-configuration` change is in scope.

## Progress

- Created the isolated feature branch and worktree.
- Implemented the single-session collector, bounded direct writer, local crash
  patches, telemetry, 512-process regression load, and NFS checks.
- Extended the implementation to collect crash essentials first, flush them
  with `syncfs(2)`, and publish `inspect/priority-complete` before the large
  supplementary reports. Report payloads still write directly to their final
  destination and are not staged in tmpfs.
- Rewrote the merge branch to exclude comparison-only code. The legacy
  collector, equivalence test, and six-case benchmark are committed only on
  the validation branch, which is based on the finalized merge-tree code.
- The earlier review and validation results below apply to the original report
  order. Quick checks and the mandatory review for the priority extension
  completed, but its inspection VM test later exposed an unresolved collector
  failure.
- The user ended this initiative on 2026-08-25 because a colleague implemented
  the required solution in commit
  `b0e1a4dee54efda0075904b31d6b87e003aaa41b`. The active diagnostic rerun was
  interrupted, no rewritten branch was pushed, and none of these local heads
  is ready to merge.

## Priority extension implementation

- Merge branch final abandoned head: `3e936050a`.
- Validation branch head: `3a823e5a2`, based directly on merge draft
  `10159f00c`.
- Priority order is `bt-panic.txt`, `log.txt`, `sys.txt`,
  `bt-active-nonidle.txt`, `bt-active.txt`, and
  `bt-sleeping-uninterruptible.txt`.
- Supplementary order is `ps-active.txt`, `ps-summary.txt`, `ps.txt`,
  `bt-sleeping-interruptible.txt`, and `ps-last-run.txt`.
- `crash-buffer --syncfs --complete PATH` flushes the destination filesystem,
  then atomically renames a complete marker containing `0`. It removes a stale
  marker before processing and does not publish one on open, write, sync, or
  timing failure.
- Collector metadata is version 3 and identifies the priority marker, report
  set, and `syncfs` barrier. The README explains that supplementary collection
  can still be running when the marker appears.
- Routine inspection checks exact report order, marker metadata, and stale
  marker removal. Direct-NFS inspection observes the marker and all essential
  files from the server while `inspect.exit-status` is still absent.
- Comparison-only files and their `tests/all-tests.nix` registrations are
  absent from the merge branch and present on the validation branch.

## Priority extension quick checks

- Formatted all changed Nix files and parsed them with `nix-instantiate`.
- Compiled `crash-buffer.c` with `-Wall -Wextra -Werror`.
- Built the `crash-buffer` derivation at
  `/nix/store/rf9p9ny1abwlkcmb5sf7ksxl9pkg2igw-crash-buffer-1`; install checks
  passed for streaming, atomic markers, `syncfs`, append, invalid options,
  unavailable output, and post-open write failure.
- Merge-branch discovery lists only `crashdump/default`, `crashdump/inspect`,
  and `crashdump/nfs-inspect`. Validation-branch discovery additionally lists
  equivalence and all six benchmark instances.
- Evaluated the generated optimized and legacy benchmark, equivalence, and NFS
  inspection test scripts from their Nix derivations and checked each with
  `ruby -c`; all reported `Syntax OK`.
- `nix develop --command overcommit --run` passed Nixfmt and RuboCop in both
  worktrees. An initial amend outside the development shell was blocked because
  ambient `nixfmt` was unavailable; rerunning inside `nix develop` passed all
  pre-commit and commit-message hooks.

## Priority extension mandatory review

The required fresh standalone reviewer reported two blocking findings, one
important finding, and one advisory before long tests:

- a final priority writer could publish the marker even when an earlier
  essential writer failed, and setup ignored stale-marker removal or report
  truncation errors;
- the two crash process optimizations, the session and priority changes, and
  the equivalence and benchmark validation were not split finely enough;
- `origin/staging` advanced to `399cc60d2` with a flake input update;
- process-farm children inherited a SIGTERM handler that prevented clean test
  cleanup.

All findings were addressed before VM testing:

- added repeatable `crash-buffer --require PATH`; the final essential writer
  now requires completion markers from every preceding priority command before
  `syncfs` and publication;
- made output-directory creation, stale-marker invalidation, control-file
  initialization, and report pre-truncation fail closed;
- added package coverage in which the final writer succeeds but a required
  earlier marker is absent, and routine coverage for an unremovable stale
  marker;
- reset SIGINT and SIGTERM to their defaults in process-farm children and
  manually verified that a two-child farm terminates cleanly;
- rebased onto `origin/staging` at `399cc60d2` and rebuilt both crash patch
  variants independently against the updated Nix inputs;
- rewrote the merge history into four focused commits:
  `e5d976935` (`ps -A`), `be2d89228` (`ps -m`), `4662f69e1`
  (single-session collector), and `10159f00c` (priority boundary);
- rewrote validation as `05988dc31` (legacy collector and same-vmcore
  equivalence) and `3a823e5a2` (benchmark).

The updated `crash-buffer` derivation built at
`/nix/store/zpvnr2j5k5daxpak6f8l48mk1jismj8b-crash-buffer-1`. All rewritten
commits passed installed pre-commit and commit-message hooks. A focused
reviewer follow-up found that the first validation commit referenced the legacy
collector added by the second commit, and noted that `mktemp` was unchecked.
Moved the helper to its first consumer and made temporary-directory creation
fail closed. The same standalone reviewer confirmed that all Blocking,
Important, and Advisory findings are resolved, both histories are coherent and
clean, and long VM tests may proceed.

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

- Before the priority-extension reruns, waited for an unrelated
  `vps/autostart-monitoring` VM test to release `/dev/shm`. The first polling
  expression matched its own shell after the test exited; documented the
  self-excluding `pgrep -f '/tmp/[o]sctld-...'` pattern in
  `notes/cross-project/2026-08-25-pgrep-self-match.md`.
- A second unrelated instance started while `crashdump/default` was evaluating.
  Interrupted the crashdump runner before it launched a VM and continued to
  wait for an uncontended host. No validation result came from that interrupted
  invocation.
- The later priority-order `crashdump/default` rerun passed all six examples in
  374.27 seconds; its crash and post-reboot artifact check took 53.38 seconds.
- The first priority-order `crashdump/inspect` run reached the crash kernel but
  inspection returned collector exit status 1 without the expected diagnostic
  artifact. This is an unresolved functional failure in the abandoned branch.
- Added diagnostic capture and started a fresh inspection rerun. Interrupted it
  when the user superseded the initiative; it produced no accepted result.

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

- None. The initiative is abandoned in favor of
  `b0e1a4dee54efda0075904b31d6b87e003aaa41b`. Do not resume, push, or merge the
  retained local branches without a new explicit request and fresh validation.

## Compatibility

Existing report filenames and status rows remain. New `session.txt`, `timings`,
`priority-complete`, and manifest keys are additive. Report payloads are written
directly to the destination with at most one 256 KiB writer; tmpfs contains
only tiny control files. Mixed versions and rollback require no coordination or
conversion.

## Cleanup

All three initiative worktrees were clean and removed after abandonment. The
local feature, validation, and rewrite branches remain recoverable as listed
above. The previously pushed remote feature branch still points to the older
validated implementation at `efba51db6`; no priority-extension rewrite was
pushed. No production configuration or deployment was changed.
