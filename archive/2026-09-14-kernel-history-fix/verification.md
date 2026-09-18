# Kernel history and invalid-evidence recovery validation

The four feature heads are merged into their remote default branches:

| Repository | Merged revision |
| --- | --- |
| vpsadmin | `c38839d5be62e9d40d055b23a84844e2037ba4db` |
| vpsfree-maintenance-tasks | `2fdc9f2889ac419136cd0cde0e0955c015ae7107` |
| vpsfree-cz-configuration | `b792c50e3baa17a73989dda1129cb17ba0e63587` |
| vpsfree-kb-contracts | `8789cc1f5aeb3b19cbff13f741d6dd9960f14567` |

Both pins select that exact vpsAdmin revision. All feature branches are retained.
Before integration, V was rebased over the upstream DDNS fix. Range-diff proves
both feature patches unchanged. The rebased combination passed142 focused
examples, including DDNS/lifecycle, recorder, supervisor and maintenance cases.
K bin/check passed from its fresh integration worktree; all11 C consumers built
as generation `2026-09-15--10-59-39`. See [merge-validation.md](merge-validation.md).

Full CI for the preceding reviewed V/K heads passed, as recorded below.
CI triggered by the merges is still running: V master runs34950267566(CI),
34950267548(API),34950267587(migrations),34950267521(lint),34950267498(i18n),
34950267509(libnodectld); K master34950343075(Check),34950343064(runtime).
Migration, lint, i18n and libnodectld have passed on the merged V head. These
new runs are not represented as completed full-suite validation.

## Local checks

| Check | Result |
| --- | --- |
| Recorder/comparator/supervisor and relocated maintenance RSpec | 130 examples, 0 failures |
| API visibility and standalone CLI RSpec | 23 examples, 0 failures |
| Maintenance after installed-loader remediation | 29 examples, 0 failures; help, all-node preview, subset apply, all-node apply and rerun on disposable data |
| Checkpoint exclusion from historical repair proof | Passed |
| Additive migrations | 2 examples, 0 failures; nullable/no default/no backfill, empty private table, uniqueness, cascade and rollback |
| Full predecessor schema reproduction | Exact upstream014fbc784 plus both migrations reproduces core schema.rb byte for byte |
| Ruby lint and commit hooks | Passed; six maintenance Ruby files lint clean |
| CI selector | 16 runs, 55 assertions, passed |
| API topic coverage | All 403 non-migration specs covered exactly once; migration workflow glob covers both new migrations |
| Exact Nix integration fixture parser preflight | Both original and recovery fixture snippets accepted by PayloadParser |
| Supervisor/runtime-ingestion at final V | All 11 examples passed; 1067.52s total, new regression119.94s |
| webui#admin-cluster at V42984def6 | Passed; 1358.63s total, browser flow481.79s |
| Canonical KB bin/check | Passed; 60 runs/194 assertions, no semantic drift, all 120 PNG variants valid |
| Configuration input assertions | All 11 consumers use vpsadminServices at Vc38839d5; no other lock node changed |
| Configuration consumer builds | All 11 passed; generation 2026-09-15--10-59-39 |
| Prepared rollout shell blocks | All 14 parse with bash -n; none executed against production |
| Supervisor activation guard | Isolated systemd fixture proves blocked start survives base-unit replacement/reload; pinned NixOS activation source preserves runtime guard |

The maintenance suite validates dry-run/apply/idempotence, immutable evidence
selection, missing or altered proof, cross-boot rejection, concurrent changes,
revision invalidation, all eligible nodes including inactive storage hosts,
subset selection and the installed Ruby interpreter's `load` entry point.
No real host patch was unloaded. No local kernel compilation was needed.

The KB check validates 45 controls, 36 paths, 35 capture concepts, 3 semantic
selectors, 94 bindings/9 exceptions, 4 pages/8 variants, 12 page tests and 21
executable samples. No prose or capture changes are needed. Existing vpsAdminOS
and nixpkgs pins remain unchanged.

## Review

General, architecture, scope and compatibility reviews completed with fresh
GPT-6 Astra agents at xhigh, following the user's model correction. All required
findings are resolved; see recovery-review-reconciliation.md and the lane reports.
Final general and compatibility pin reviews cover the exact four heads and the
prepared rollout. They found the ineffective NixOS runtime-mask procedure and
accepted its replacement with a verified condition drop-in and marker.
The general report records the limited validation: an isolated live systemd
fixture plus exact built-unit/activation source inspection, not a full NixOS
activation rehearsal. No unresolved findings remain.

## Completed full validation before the final rebase

| Workflow | Run | Result |
| --- | --- | --- |
| vpsAdmin integration CI | [34877084413](https://github.com/vpsfreecz/vpsadmin/actions/runs/34877084413) | Passed; 135 scripts / 118 tests,17149.92s |
| vpsAdmin API topic specs | [34877084311](https://github.com/vpsfreecz/vpsadmin/actions/runs/34877084311) | Passed; all topic jobs |
| API migration specs | [34877084303](https://github.com/vpsfreecz/vpsadmin/actions/runs/34877084303) | Passed |
| RuboCop | [34877084338](https://github.com/vpsfreecz/vpsadmin/actions/runs/34877084338) | Passed |
| i18n health | [34877084302](https://github.com/vpsfreecz/vpsadmin/actions/runs/34877084302) | Passed |
| WebUI PHPUnit | [34877084305](https://github.com/vpsfreecz/vpsadmin/actions/runs/34877084305) | Passed |
| libnodectld specs | [34877084349](https://github.com/vpsfreecz/vpsadmin/actions/runs/34877084349) | Passed |
| KB Check | [34877456478](https://github.com/vpsfreecz/vpsfree-kb-contracts/actions/runs/34877456478) | Passed |
| KB managed page runtime | [34877456477](https://github.com/vpsfreecz/vpsfree-kb-contracts/actions/runs/34877456477) | Passed; 12 scripts / 4 tests,2337.54s |

The configuration and maintenance repositories have no workflow runs for these
feature heads. Their gates are the consumer builds and disposable maintenance
suite respectively. Prior-head workflows were already complete when superseded;
none required cancellation. Previous delivery CI was green but is not substituted
for validation of these final heads.

## Investigated issues

- Rebase crossed an upstream migration timestamp collision. Renumbered the two
  unmerged feature migrations to 20260914180000 and 20260914190000. Neither had
  been deployed. Full predecessor schema testing caught a lost upstream index
  after conflict resolution; the regenerated schema restores it.
- General review caught a non-SHA software revision in the synthetic recovery
  fixture. Corrected it and parsed the exact Nix fixture snippets successfully.
- Architecture review caught a CLI guard incompatible with the installed loader.
  Split the executable from importable code and tested the actual load semantics.
  The approved batch size is now explicitly1,000 instead of accidentally borrowing
  the unrelated HistoryBackfill default10,000.
- Final operator review caught NixOS /etc units outranking /run masks. The rollout
  now verifies a loaded false start condition on both hosts before and after
  activation; both deployments select the completed build generation explicitly.
- Earlier local integration setup issues (socket path length, nodectld stop wait,
  overlong synthetic version and reporter-dependent fixtures) were investigated
  and fixed before this final follow-up. Current runs use short isolated state
  paths and self-contained synthetic evidence.

## Delivery boundary

The user authorized the four default-branch merges on2026-09-15. No production
deployment or history repair, node upgrade/reboot, or session lifecycle action
was performed. Production history rows were
not inspected. The repair can tighten only intervals supported by intact retained
immutable event snapshots; insufficient evidence leaves them unchanged.
Prepared commands are in [rollout.md](rollout.md). The session remains active and
open at [its portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-09-14-kernel-history-fix/).
