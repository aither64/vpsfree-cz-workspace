---
lifecycle: active
---

# 2026-10-17-impermanence-test-failures

## Status

- Investigation in progress. Original native artifact downloaded and inspected.
- All 12 reported script failures belong to one failed shared fixture build;
  no test VM or impermanence assertion ran.

## Phase checklist

- [x] Verify session identity and retained same-session roster.
- [x] Retrieve original job and native test logs.
- [x] Locate shared failure before VM startup.
- [ ] Complete source-level purpose and failure-mechanism investigation.
- [ ] Report supported conclusion and remaining uncertainty.

## Next actions

- Reconcile architect0's source trace with original build failure evidence.
- Seek OOM/signal evidence around 2026-10-17 02:01:27 UTC on gh-runner2.

## Documentation

## Repositories

- vpsadminos canonical bare repository, target `0081fc01f13236a098380094ddbd00539a9c8dae`.
- No feature branches or worktrees created; application files unchanged.

## Commands run

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
  of 86.5 GiB. Build memory is separate from these guest reservations.

## Open questions

- Which signal killed nix-build and why? Runner SSH refused both local-user and
  root key authentication. The configured physical host node1.pgnd.vpsfree.cz
  has no trusted host key locally; no trust bypass attempted. Asked user for
  runner/host evidence asynchronously.

## Cleanup

- Downloaded job.log, native-logs.zip, and extracted ci-logs are session-owned
  diagnostic data. No guests, test runners, CI reruns or deployments launched.
- Keep session open; no lifecycle action requested.
