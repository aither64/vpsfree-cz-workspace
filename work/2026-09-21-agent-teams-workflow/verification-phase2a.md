# Phase 2A verification

## Accepted revisions

- `codex-web`: `52b8ca6e9ddf2175d1a9163996fa9073f9c1882d`
  over base `0a75d720171c52719679c7dd2e356d50f4b81f16`
- Generic `dev-workspace`:
  `729e5e08a9d57e537250da157d74720af50003eb`
  over base `39bfa664298443334d12b08dd42a475eef1c38e4`

Both worktrees were clean for final exact-head checks. All tests and builds were
run and monitored by fresh operation-scoped Luna/low watchers; no retained team
member waited on a verification process.

## Focused checks

- `codex-web`: `nix develop path:<codex-web> -c env
  TMPDIR=/tmp/cw-go-test go -C <codex-web> test -mod=mod ./codex` passed in
  0.975 seconds on exact head. Log: `logs/phase2a-codex-tests-exact.log`.
- Generic before review: focused `./internal/agentteams` passed on the initial
  exact head. Mandatory review then required revision-validation fixes and a
  coherent one-commit range.
- Generic remediation: `nix develop path:. -c go -C portal test -mod=mod
  ./internal/agentteams` passed in 35 seconds before the commit rewrite.
  Log: `logs/phase2a-review-fix-tests.log`.
- Generic final: the same command passed in 33 seconds on exact head `729e5e08`,
  with exactly one commit in the reviewed range and clean pre/post status. Log:
  `logs/phase2a-review-fix-tests-final-exact.log`.

An earlier generic run found a real unused import, which was fixed before
commit. A later watcher copied the `-C` path incorrectly; that invocation never
ran Go and is not acceptance evidence. Both failures are preserved in the logs.

## Mandatory review

The retained independent Sol/xhigh reviewer covered general correctness,
architecture/repetition, scope/proportionality and
risk/security/compatibility. It found one Blocking commit-structure problem and
two Important history-validation problems. The retained implementer resolved
all three, a fresh Luna watcher passed the exact-head focused test, and the same
reviewer accepted the rerun with all lanes clean. Full evidence is in
`review-packet-phase2a.md` and `review-results-phase2a.md`.

## Packaged suites

- `codex-web`: `nix flake check --print-build-logs` passed in 48 seconds on
  exact head `52b8ca6e`. Go checks and 46 browser tests passed. Log:
  `logs/phase2a-codex-flake-check.log`.
- Generic: `nix flake check --print-build-logs` passed in 273 seconds on exact
  head `729e5e08`. Reported suites had zero failures/errors. Log:
  `logs/phase2a-generic-flake-check.log`.

Both package worktrees remained clean, no process remained after either run,
and neither operation attempted an unexpected local kernel build.

## Outcome and remaining boundaries

Phase 2A is accepted. It remains dormant: no agent manager, managed state
emission, UI/route, native child creation, package-retention action, deployment,
push or default-branch integration exists in this slice. Phase 2B owns native
registration and creation; Phase 2C owns transitions/dispatch; Phase 2D owns
member observation and lifecycle compatibility.
