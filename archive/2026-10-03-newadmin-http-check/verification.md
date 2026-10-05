# Verification evidence

## Current result

All planned implementation checks passed at final feature head
`7e32833aca1cb65902b50f61eb76dd1022691591`: quick checks, mandatory independent
review and both exact monitoring-host builds. The clean, published feature
branch has that same remote head. After explicit user approval, remote master
was fast-forwarded to that exact revision; no patch changed. Production activation
was not performed. Production exporter/rule/notification checks remain for the
operator-owned prepared [rollout](rollout.md).

## Quick checks

[implementation-result.md](implementation-result.md) retains the exact commands
and artifact paths reported by implementer0.

- Promtool 3.12.0 checked 36 generated rules and passed all 17 rule scenarios:
  missing metrics, exporter/probe failures, BFF unit and certificate conditions,
  all-nine warning policy, and critical controls for API/console/legacy UI.
- The actual Nix rule-test name/count/warning assertions passed with only
  derivation creation stubbed.
- Fifteen fixtures passed against evaluated source patterns using Go regexp:
  compact/formatted/ASCII-whitespace metadata, schema delimiter cases and
  invalid schema/short/long/uppercase/nonhex commit cases.
- Generated base/final rule JSON differs only in seven dedicated Newadmin
  severity values. Expressions, durations, frequencies, annotations, groups
  and every non-Newadmin rule are identical.
- Both final commits passed required formatting and commit hooks without
  warnings or bypass. The worktree and final diff checks are clean.

## Independent review

Retained reviewer0 used saved GPT-6.1 Sol/xhigh/read-only settings and reviewed
all four lanes at the exact final head before host builds. No Blocking,
Important or Advisory findings. The complete two-commit history has no obsolete
functional approach, fixups, unused compatibility path or migration; empty
migration lineage is sound. The reviewer independently evaluated base/final
rule exports and confirmed the seven severity-only changes.
See [review.md](review.md) and [review-packet.md](review-packet.md).

## Host builds

Both commands ran from the registered configuration worktree at the reviewed
final head. Each operation had a fresh GPT-6 Luna/low utility watcher; all owned
operations have exited. Built generations were not activated.

| Target | Exact command | Result | Elapsed | Generation | Evidence |
| --- | --- | --- | --- | --- | --- |
| mon1 | `nix develop --command confctl build --yes cz.vpsfree/containers/prg/int.mon1` | exit 0 | 58.8 s | `2026-10-03--20-47-18` | `mon1-build-verified.log`, `.status`, `.elapsed` |
| mon2 | `nix develop --command confctl build --yes cz.vpsfree/containers/prg/int.mon2` | exit 0 | 58 s | `2026-10-03--20-51-51` | `mon2-build-final.log`, `.status`, `.elapsed` |

Mon1 built thirteen derivations including checked blackbox configuration,
checked Prometheus rules/configuration and its NixOS system. Mon2 completed
seven remaining derivations and its NixOS system, reusing shared inputs. Parent
inspection confirms the exact target and completed generation in each log.

## Publication and CI

The feature branch was pushed over canonical SSH after fetching unchanged
upstream and checking ancestry. The exact base/head comparison was captured.
`git ls-remote` verifies remote feature head
`7e32833aca1cb65902b50f61eb76dd1022691591`. Feature publication itself left
master unchanged; the later approved default-branch integration is recorded below.
`gh run list` returned no branch runs. The repository has a scheduled/manual
dependency-update workflow and no feature-push CI; no workflow was triggered.

## Environment and recovered harness failures

Fresh environment watcher ran declared `nix develop --command true` at base
`657cc0a8e087f8c4bed7fe8d7176cb9f06a6e2da`: exit 0 in 41 seconds. Local gems
then allowed supported worktree registration retry, without hook bypass.
Evidence: `environment-setup.log` and `environment-setup.status`.

The implementation sandbox could not connect to the Nix daemon. A private
cached print-dev-env snapshot supplied declared Ruby 3.4.9 and nixfmt 1.5.0.
Pure evaluation used already installed locked nixpkgs source, and promtool used
the installed locked Prometheus 3.12.0 CLI. No dependency or pin changes.

The first mon1 invocation stopped at confirmation EOF, exit 1 after 22 seconds,
before building (`mon1-build.log`, `.status`). The parent inspected the failure
and pinned help before assigning a fresh watcher with the documented build
command `--yes` option. A mon2 attempt then exited 127 in an unavailable
`/usr/bin/time` wrapper before its build (`mon2-build-verified.log`, `.status`).
The parent inspected that evidence and assigned a fresh mon2-only watcher with
built-in timing. Both issues are recovered; no source changes or redundant mon1
build were needed.

Reusable setup/build lessons are in workspace notes:
`notes/vpsfree-cz-configuration/2026-10-03-worktree-checkout-hooks.md`,
`2026-10-03-noninteractive-builds.md` and `2026-10-03-watcher-timing.md`.

## Verification limits

No production deployment, live exporter query, loaded production label check or
notification delivery check has been performed. The raw-body regex is a
lightweight metadata check, not full JSON validation. Metadata and BFF health
checks do not verify interactive login or all WebUI functionality. These
remaining checks belong to the authorized rollout phase, not implementation acceptance.

## Approved default-branch integration

The user directed “merge into the default branch” and retained deployment
ownership. Fresh upstream fetch confirmed the reviewed base was still master.
An isolated target worktree started at that base, then fast-forwarded to the
unchanged reviewed head and pushed normally over canonical SSH:

```sh
git merge --ff-only refs/heads/2026-10-03-newadmin-http-check
git push origin HEAD:refs/heads/master
```

Both commands passed. Target worktree cleanliness, exact HEAD and diff checks
passed. Post-push `git ls-remote` confirms remote master and feature refs both
at `7e32833aca1cb65902b50f61eb76dd1022691591`; local target HEAD and origin/master
match. No rebase, merge commit, source change or repeated build was needed.
GitHub master run metadata has only older completed Daily update runs, no run at
the integration head. No deployment, workflow launch, ref deletion or worktree
cleanup occurred. Session remains open.
