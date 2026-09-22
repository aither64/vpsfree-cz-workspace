# Phase 2B.3 verification

## Scope

This evidence covers the committed managed-creation series above generic
`dev-workspace` base `285e998f4aae703f1d6b639a7bf23f7e111a660c`, ending at
`6aa9be1969b428f67c63e04d0c60171305f70d83`. Early Go
checks used a temporary local workspace to bind the reviewed `codex-web` head
`52b8ca6e9ddf2175d1a9163996fa9073f9c1882d`. That feature head is published and
the generic Go and Nix pins use it. The final pinned-package build below proves
that the locked dependency graph is reproducible.

Every test, build or browser wait was owned by a fresh Luna/low watcher. The
retained lead, designer and implementer did not wait on those processes, and no
watcher was reused.

## Final passing checks

- Focused Go packages:
  `go -C portal test -mod=readonly ./internal/agentteams ./internal/session ./cmd/workspace-portal ./internal/web`.
  All four packages passed. Log: `logs/phase2b3-focused-go-final.log`.
- Managed stale-catalog HTTP boundary:
  `TestBrowserManagedCreationRejectsStaleCatalogBeforeReceipt` passed. Log:
  `logs/phase2b3-stale-http.log`.
- Chromium creation acceptance passed for new and plan-to-new forms, including
  independent plan drafts, stale-catalog reset and acknowledgment across reload,
  failed-request retention and accepted-receipt cleanup. Log:
  `logs/phase2b3-creation-browser-final.log`.
- Final full Ruby host suite passed: 91 runs, 512 assertions, no failures,
  errors or skips. Log: `logs/phase2b3-ruby-host-final.log`.
- Full Ruby dev-session suite passed: 325 runs, 3,514 assertions, no failures or
  errors and 12 intentional skips. Log: `logs/phase2b3-ruby-dev-final.log`.
- Focused receipt-race, replay-order and path-integrity regressions passed. Logs:
  `logs/phase2b3-receipt-race-final.log`,
  `logs/phase2b3-replay-order-final.log` and
  `logs/phase2b3-path-integrity-final-pass.log`.
- Earlier command-boundary proof passed with no remaining process. Log:
  `logs/phase2b3-command-boundary-final.log`.
- Post-pin focused host registration and creation tests passed: 18 runs, 81
  assertions, then 7 runs, 115 assertions; neither had a failure, error or
  skip. Logs: `logs/phase2b3-host-sandbox-final.log` and
  `logs/phase2b3-agent-team-creation-final.log`.
- The final pinned package build passed with no local compiler or kernel build:
  `nix build .#packages.x86_64-linux.default --no-link`. Log:
  `logs/phase2b3-pinned-package-final.log`.
- Final remediation coverage passed: four Go packages, host 91/520, dev-session
  325/3,513 with 12 intentional skips, and Chromium creation acceptance. Logs:
  `logs/phase2b3-final-remediation-go.log`,
  `logs/phase2b3-final-remediation-host-rerun.log`,
  `logs/phase2b3-second-remediation-rerun-dev.log`, and
  `logs/phase2b3-final-remediation-browser.log`.
- The final package build took 225 seconds and `nix flake check --print-build-logs`
  took 279 seconds; both passed. Log:
  `logs/phase2b3-packaged-default.log` and `logs/phase2b3-flake-check.log`.

## Failures resolved during verification

- Chromium exposed an acknowledgment checkbox that was immediately unchecked;
  the production UI now preserves explicit confirmation and both forms prove
  reload recovery.
- Strict schema-1 host validation exposed an obsolete fixture expectation; the
  fixture now distinguishes malformed input from a valid unfinished creation.
- The aggregate dev-session suite exposed command doubles that did not implement
  the new resolver and lifecycle-guard contracts. They now return the exact
  unmanaged result or empty guard output instead of relying on permissive
  fallbacks.
- Receipt disappearance was wrapped before the caller could classify it. The
  strict reader now maps only genuine `ENOENT` to the existing no-longer-current
  conflict; permission, symlink, non-directory, malformed and replacement
  failures remain fatal.
- Managed-state absence checks now reject symlinked and wrong-type parent paths
  instead of misclassifying them as unmanaged absence.
- Codex executable validation now occurs at live team resolution, so it cannot
  preempt persisted-history or runtime-provenance checks on replay paths.
- The Nix test sandbox has no `/usr/bin/env`; generated Ruby test helpers now
  use the configured Ruby executable. This preserves their real subprocess
  coverage rather than weakening the host test.

## Review state

Mandatory review classified this as high risk and covered General,
Architecture/repetition, Scope/proportionality, and Risk/compatibility at
Sol/xhigh because the user prohibited Astra. It found and resolved managed
receipt recovery gaps, portal/CLI launch-evidence parity, the published scalar
bound, strict schema discrimination, and terminal cancellation invariants.
The final affected-lane reruns have no findings. Full findings, decisions and
reruns are recorded in `review-results-phase2b3.md`.
