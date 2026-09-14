# Kernel history fix validation

The tested vpsAdmin head is `337c9257f5e11f36afe81eba4951e267b83e2fc7` (pushed).
Configuration `09b3370c2d628bcc7ab5eb7bbdf19edbcf8be347` and KB `61aaf95d3dc0968728131a2cf4d4740dae6e9250`
are pushed and pin that exact revision. Remote heads and final portal comparisons
were verified. The final pin consistency review passed with no findings. All 11 final consumer builds and all final-head GitHub Actions passed.

## Local checks

| Check | Result |
| --- | --- |
| Recorder, repair, supervisor and shared-state RSpec | 106 examples, 0 failures; final API tree is identical to tested feaa1524 |
| Isolated additive migration RSpec | 1 example, 0 failures |
| Core schema load, migration and regeneration | Passed; only the new nullable column is a semantic change |
| Touched Ruby lint and commit hooks | Passed |
| CI selector | 16 runs, 55 assertions, passed |
| Migration/spec coverage and exact workflow expansion | Passed; all 404 non-migration specs covered once |
| Standalone synthetic payload preflight | Passed through parser, persistence, transitions, restart and public Rake repair |
| Supervisor/runtime-ingestion at final 337c9257 | All 11 examples passed; 935.48s total, synthetic example 123.27s |
| webui#admin-cluster | Passed; 459s browser flow, 1483s total; rendering code unchanged since this run |
| Canonical KB bin/check at final 337c9257 | Passed; no prose or capture changes |
| All 11 final consumer input assertions | Passed; only vpsadminServices, exact 337c9257 |
| All 11 final consumer builds | Passed, generation 2026-09-14--13-07-10 |
| Prepared rollout shell blocks | bash -n passed; commands not executed |

The KB contract validates 45 controls, 36 paths, 35 capture concepts, 3 semantic
selectors, 94 bindings/9 exceptions, 4 pages/8 variants, 12 tests and 21 executable
samples. Its checker suites pass 60 runs/194 assertions and validate 120 PNGs.
Existing vpsAdminOS and nixpkgs pins are preserved.

## Review

General, architecture, scope and compatibility lanes completed at gpt-5.6-sol
xhigh. Blocking/Important findings were resolved with focused checks; decisions
and bounded follow-up reviews are in review-reconciliation.md. The final exact-pin
consistency review passed with no findings; see review-final-pin.md. No deployment or repair is authorized.

## GitHub Actions

| Workflow | Run | Result |
| --- | --- | --- |
| Final vpsAdmin integration CI | [34836306209](https://github.com/vpsfreecz/vpsadmin/actions/runs/34836306209) | Passed; 135 scripts across 118 tests |
| Final vpsAdmin API Specs | [34836306199](https://github.com/vpsfreecz/vpsadmin/actions/runs/34836306199) | Passed; 26 topic jobs and coverage check |
| Final vpsAdmin RuboCop | [34836306248](https://github.com/vpsfreecz/vpsadmin/actions/runs/34836306248) | Passed |
| Final vpsAdmin i18n | [34836306232](https://github.com/vpsfreecz/vpsadmin/actions/runs/34836306232) | Passed |
| Migration specs, unchanged migration | [34827227517](https://github.com/vpsfreecz/vpsadmin/actions/runs/34827227517) | Passed |
| libnodectld specs, unchanged source | [34827227454](https://github.com/vpsfreecz/vpsadmin/actions/runs/34827227454) | Passed |
| Final KB Check | [34837590578](https://github.com/vpsfreecz/vpsfree-kb-contracts/actions/runs/34837590578) | Passed |
| Final KB Managed page runtime | [34837590575](https://github.com/vpsfreecz/vpsfree-kb-contracts/actions/runs/34837590575) | Passed; 12 scripts across 4 tests |

Final integration CI completed 135 scripts across 118 tests in 17951.35 seconds,
with all 118 tests successful and no unexpected results. The completed log was
inspected. The initial implementation API run 34827227593 passed all 26 topic jobs.
Intermediate running workflows were cancelled only after superseding pushes;
completed results were preserved. Downloaded cancelled integration artifacts
show 18/19/9 retained expected-success results respectively and no reported
unexpected failures before cancellation. These are partial results, not full
suite passes. The configuration repository has no branch workflows; its gate is
the complete 11-consumer build.

## Investigated integration failures

- Long state paths exceeded Linux's Unix socket limit before examples. Use short,
  isolated state directories.
- Runit's seven-second default wait failed before report publication. Explicit
  waits now cover the wrapper's existing stop deadline and restore the reporter
  even after a failed stop.
- The synthetic version exceeded its 25-character DB limit. Corrected and
  reproduced the failure in a disposable DB before rerunning.
- Public Rake dispatch singularized the internal task class name. Fixed the name
  and added a public preview/apply/idempotence regression.
- Copying current evidence after a legacy report depended on reporter timing.
  Replaced it with a complete standalone synthetic payload. The final full VM
  run passed. No real patch unload or local kernel compilation was needed.

## Delivery boundary

No production deployment or history repair, node upgrade/reboot, default-branch
merge, or session lifecycle operation was performed. Production history rows
were not inspected. Repair can only tighten intervals supported by retained,
intact event snapshots; missing evidence leaves an interval unchanged.
Prepared commands are in [rollout.md](rollout.md). The session stays active and
open at [its portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-09-14-kernel-history-fix/).

## Follow-up status timestamp audit

The requested audit passed 13 database-backed examples. Normal software,
deployment, sysctl, module and eBPF inventory paths use recent confirmations.
A separate existing rejected-evidence recovery path loses those confirmations;
six examples reproduce it, including the livepatch-application special case. System-state first/last observations remain correct.
See [status-timestamp-audit.md](status-timestamp-audit.md). This finding is
unfixed and does not change the tested kernel-specific feature or pin.
