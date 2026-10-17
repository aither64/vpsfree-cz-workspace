---
lifecycle: active
---

# 2026-10-17-impermanence-test-failures

## Status

- User confirmed on 2026-10-17 that the failed build was killed by OOM.
  Source/log investigation established the shared fixture failure and purpose;
  implementation is now authorized for opt-in staged image preparation.
  Architect0 owns the design brief; implementer0 will own application changes.
- All 12 reported script failures belong to one failed shared fixture build;
  no test VM or impermanence assertion ran.

## Phase checklist

- [x] Verify session identity and retained same-session roster.
- [x] Retrieve original job and native test logs.
- [x] Locate shared failure before VM startup.
- [x] Complete source-level purpose and failure-mechanism investigation available
  from original CI evidence and source.
- [x] Reconcile architect0's source trace with build failure evidence.
- [x] OOM cause confirmed by user (host logs not supplied here).
- [x] Recommend bounded VM/build resource allocation and validation.
- [x] Reconcile recommendations with user's automatic-throughput constraint.
- [x] Agree on smaller staged preparation plan and explicit opt-in CLI flag.
- [x] Architect records implementation and verification brief; lead accepted it.
- [ ] Implement and pass quick checks/hooks; commit complete deliverable.
- [ ] Independent final review, including branch history and no-migrations conclusion.
- [ ] Longer cold/warm verification; publish exact branch and integrate evidence.

## Next actions

- Implementer0 is editing from the accepted architect brief in the registered
  session worktree. Hooks are installed and signed in the repository environment.
- No default-branch integration or deployment requested.

## Documentation

- [Implementation design and verification brief](design.md) is architect-owned
  and accepted by the lead before application edits.
- [Architect source investigation](source-investigation.md) records the exact
  source paths, assertion guarantees and fixture/compression cost contributors.
- Source explanation at failed revision: `docs/containers/nixos.md`, section
  "Persistent allocation state" (lines 121-181).
- Incident-specific findings stay here; no product documentation change is
  needed for an investigation with no implementation change.

## Repositories

- vpsadminos canonical bare repository, target `0081fc01f13236a098380094ddbd00539a9c8dae`.
- Feature branch `2026-10-17-impermanence-test-failures`, initial base
  `0081fc01f13236a098380094ddbd00539a9c8dae` from origin/staging.
- Worktree `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-17-impermanence-test-failures/vpsadminos`.
- Initial native worktree-add created the checkout, then its post-checkout hook
  refused an inherited Overcommit signature. Utility is installing/signing the
  inspected hook config in the repository Nix environment; no hook bypass used.
  Hook setup passed (exit 0, 223 seconds). Native registration retry succeeded;
  no hook bypass or application edit by the lead was used.

## Commands run

- Official latest release check before CI workflow edits: checkout v7.0.1
  (2026-07-20), upload-artifact v7.0.2 (2026-10-07), via GitHub releases API.
  Existing `@v7` refs already select the latest compatible major; retain them.
  Member shell DNS was unavailable; lead performed the read-only check.

## Implementation decisions

- Lead accepted architect design before application edits. Strict memory
  admission covers both nominal RAM and `/dev/shm`; only CPU overage retains
  the existing run-alone exception when both memory constraints fit. Requests
  remain unchanged and oversized requests fail with specific capacity evidence.
- Temporary utility policy resolved from catalog digest
  `437585347ac8b2cdbf498a169d8871e684f3f61ccf1dd48e8589d79ef9629abd`:
  verification_watcher `gpt-6-luna`/low, native utility
  `dw_024841fba072af1d79bd78026612eaeca055acfa31ecc89f`.
- Hook setup passed with declared Overcommit hooks enabled. A separate fresh
  utility warmed the test-runner Nix shell/dependencies successfully: bundle
  check exit 0 in 62 seconds, 29 gems installed. No integration images have
  been built before the final-review gate.
- Representative external consumer inspected read-only: vpsadmin exports
  `tests`/`testsMeta` using the pinned vpsadminos framework and launches the
  runner via `nix run .#test-runner`; it does not re-export `lib.testFramework`.
  Batch compatibility must support these exports without requiring a local
  test-runner Nix helper. No consumer pin or repository changes are planned.

## Results

- Job 117240569669 ran on gh-runner2.int.vpsadminos.org. Test
  `dist-config/nixos-persistence-upgrade` failed building its configuration after
  680.75 seconds at 02:01:27 UTC. Its 12 scripts are reported failed together.
- Artifact 12088228750 contains only test-runner.log and test-result.txt for this
  test: no console, shell or VM logs. Final build output is squashfs compression,
  reporting 42 processors. Ruby raises `nix-build ... failed ()`.
- NixCli#run! interpolates Process::Status#exitstatus, which is nil when a process
  exits due to a signal. The diagnostic drops termsig; SIGKILL/OOM is plausible
  but not established by this log alone.
- At test admission 10 tests were running with reserved guest memory 80 GiB out
  of 86.5 GiB. These are reservations, not measured RSS. Resource admission has
  a default 8 GiB global reserve but no separate per-build memory estimate.
- Final native summary: 126 test groups successful; one group failed and all its
  12 scripts were marked failed. Executor fills absent results as failure after
  the shared evaluator/build child exits (`executor.rb:734-741`).
- Architect0 confirmed the shared image includes 48 generation references plus
  10 fault-generation references before Nix deduplication: four generations per
  variant, 12 variants across 25.11/26.05/unstable. These are references, not 58
  separate machines. All enter `system.extraDependencies` of one host VM.
- Image construction is `make-squashfs.nix:68-79`, tar piped to sqfstar for
  noStrip=true. Default compression is zstd level 10 with 1 MiB blocks and no
  explicit processor/memory cap. Its progress uses the mksquashfs wording.
  This and concurrent guest load support memory pressure as a hypothesis;
  neither proves OOM or establishes which process consumed excess memory.
- Selecting one script still retains the complete shared fixture image. The
  architect's completed source trace and line references are linked above.
  Portal registration succeeded on the resource-tuning follow-up after the
  earlier package transition. The architect's sandbox had refused opening the
  transition lock; the lead's previous attempt correctly rejected a superseded
  generation and its retry was cancelled while waiting. No member access
  settings changed and no private-state workaround was used.

## What these tests protect

- Impermanence keeps only declared state on durable backing storage; the
  container's ephemeral filesystem can be recreated on restart.
- LXC supplies /proc before NixOS init, so NixOS may skip its first early-mount
  path. Legacy account allocation must see persisted /var/lib/nixos uid-map and
  gid-map before assigning IDs. Late mounts can expose the original saved maps
  after passwd/group already contain fresh IDs, breaking numeric ownership.
- Tests create dynamically allocated preservation-test and a known owned payload,
  add earlier-sorting a-preservation-test, adopt the new compatibility module,
  activate again, then restart and compare identities, maps, machine-id, payload
  checksum, ownership, bind identity and source metadata.
- Coverage includes old-to-new adoption on 25.11/26.05/unstable, fresh source
  initialization, root/declared/dependent backing, /var and /var/lib ancestors,
  direct fileSystems binds, and failures that must abort before allocation while
  preserving accounts, maps and data. It exercises guest compatibility-module
  adoption, not a NixOS release upgrade or 12 independent impermanence failures.

## Resource-tuning recommendations (unimplemented)

The initial fixed four-job and reduced CPU/Nix parallelism suggestions below
are superseded by the user's throughput clarification. Keep `--jobs auto`, CPU
overcommit 1.5 and existing kernel/Nix CPU settings. Revised proposal: keep the
8 GiB base host reserve, account for active build memory and QEMU overhead in
the same admission pool, bound compressor cache explicitly (candidate 4 GiB,
not total RSS) while retaining available CPUs, and measure cold-build peaks.
An increased global reserve is only a temporary coarse workaround, not the
preferred adaptive allocator. Current failed-run baseline is 96 GiB assigned,
94.5 GiB available initially, 8 GiB reserve, 86.5 GiB guest budget, 42 CPUs and
63 guest-vCPU budget; 10 groups had 80 GiB guest memory reserved at admission.
The original proposal is retained below as superseded investigation history.

Architect0 confirmed the revised invariant: phase-aware guest configured memory
+ estimated VM overhead + active build peak reservations must fit the current
86.5 GiB envelope. Build-only preparation can reserve its peak then transition
to guest+overhead; overlapping phases reserve both. Live pressure is an extra
admission gate accounting for unresident committed growth, not a replacement
that subtracts existing reservations twice. Shared Nix builders/executors need
common ownership/partitioning. Keep zstd10 initially; only benchmark a test-only
zstd3 alternative if useful. Kernel build CPU settings stay unchanged.

- Source/architect assessment: native CI explicitly sets `--jobs auto`, while
  the CLI default alone is 1. Jobs count admitted test groups and their build
  phase, not VMs, scripts, Nix jobs or compressor workers.
- Provisional settings for this 96 GiB/42-CPU runner's native CI only:
  `--jobs 4 --memory-reserve-mib 24576 --memory-overcommit 1
  --cpu-overcommit 1 --cpu-reserve 4`. At logged 94.5 GiB initial headroom this
  yields a 70.5 GiB guest reservation ceiling and 38 guest vCPUs; four groups
  may use substantially less. These are unmeasured starting values.
- Do not apply this CPU policy blindly to intentionally oversubscribed 128-vCPU
  livepatch cases. Do not shrink guest RAM solely to increase concurrency.
- Memory configured maximum is applied BEFORE subtracting reserve; e.g.
  max-memory 65536 MiB with 24576 reserve leaves 40 GiB. There is no jobs
  environment override, though TEST_RUNNER_* resource overrides exist.
- The failed nixpkgs pin 26f4107e47e3ad0ffd0db220469ba83b6f6d96e8 packages
  squashfsTools 4.7.5. Its exact upstream sqfstar manual documents all available
  processors by default and 25% physical memory cache default. Propose explicit
  `-processors 4 -mem 4G` (possibly 8 processors after measurements) in test image
  construction. Cache memory is not a total RSS cap; metadata/dictionaries add
  overhead. Current builder does not wire NIX_BUILD_CORES into these options.
- Nix daemon max-jobs 1-2 and cores 4-8 are additional build-throughput controls,
  not sufficient compressor limits. Reserve/build budgets must encompass
  evaluator memory and every concurrently active derivation, not only sqfstar.
- Medium term: bound image-build concurrency and reserve build memory separately
  from guest RAM, or construct images in a bounded phase before VM execution.
  Executor-local pools cannot coordinate separate simultaneous invocations;
  serialize or partition their shared runner budget.
- Initial available memory is captured once; later refreshes recheck assigned
  capacity, not live headroom. Add a pressure gate deliberately; replacing the
  reservation ceiling with live available RAM can double-count existing guests.
- Current oversized-test fallback admits a test alone despite failed limits.
  Prefer a strict memory refusal with a supported explicit CPU exception for
  intentional oversubscription; current flags are not hard enforcement.
- Verification when authorized: original fixture cold-build plus ordinary VM
  load, record cgroup peak/oom_kill counters and Nix/QEMU memory peaks, retain
  safety margin and check longer suite runtime against workflow deadlines.
  A warm-cache pass alone does not measure the former failure condition.

## Open questions

- User has confirmed OOM. Exact victim details, peak memory and compressor
  allocation are unmeasured. Runner SSH refused both local-user and
  root key authentication. The configured physical host node1.pgnd.vpsfree.cz
  has no trusted host key locally; no trust bypass attempted. Asked user for
  runner/host evidence asynchronously.

## Cleanup

- Downloaded job.log, native-logs.zip, and extracted ci-logs are session-owned
  diagnostic data. No guests, test runners, CI reruns or deployments launched.
- Keep session open; no lifecycle action requested.
- No application edits, local verification runs, independent final review or
  deployment performed. Routine investigation/evidence does not trigger final
  change review.
