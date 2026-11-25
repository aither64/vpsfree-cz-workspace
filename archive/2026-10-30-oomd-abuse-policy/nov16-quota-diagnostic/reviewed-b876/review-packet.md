# Quota discriminator preparation — committed local diagnostic

Prepared for root's affected independent review; no physical run is released or
claimed here. The architect brief is at the top of `../design.md`.

## Exact source and retained history

- Local branch `2026-11-16-quota-ci-diagnostic`, clean head
  `b876a52f80593405bd6c4d81c8d68975ec4b8cd0`, tree
  `c5e67e90bea555eb26857e7d9df96fded55a66ab`.
- Isolated review range `f9a523731700dfdef44ee96381091ce6930409a6..b876a52f80593405bd6c4d81c8d68975ec4b8cd0`.
  Preserved diagnostic ref:
  `refs/review/2026-10-30-oomd-abuse-policy/nov16-quota-diagnostic`.
- The ordinary feature branch remains at accepted SMTP-only correction `f9a5237`.
  Its published predecessor remains `1ada4b`; no remote mutation occurred.
- Exactly three files change, 117 insertions/11 deletions:
  `api/lib/vpsadmin/api/tasks/dataset_expansion.rb`,
  `tests/suite/tasks/common.nix`, and
  `tests/suite/tasks/dataset-expansion-enforce-and-resolve.nix`.
  `diagnostic-committed.diff` SHA256
  `e96bd906e04131756cda7ecbb5d46ccc1890d9f03f1da1f6efe4e88f753f9f3b`
  equals the tracked input exercised by the passing unit batch.
- No migration/schema/public API/dependency/flake/threshold/timeout change.
  `diagnostic-final-receipt.json` records unchanged schema/input hashes and the
  retained original/additive migration bytes. No historical lineage rewrite.
  Final feature consolidation remains held until the discriminator settles.

## Diagnostic boundary

The existing fixture passes its exact expansion ID only to the existing enforcer
rake process. The task preserves its original relation, predicate fragments,
getter order, short circuits, writes, locks, effects and exceptions. Target-only
buffered JSON records selected/not_selected, original expansion/count/constants,
branch/outcome, and detached already-loaded association values captured before
submission effects. Unloaded/missing values and uncertain getter attribution stay
explicit. There is no diagnostic query/reload/preload/getter replay. Fixture write
telemetry uses the objects updated by the existing four helper calls.

This is observation, not a quota eligibility fix. A non-reproduction does not
explain the historical failure. Changed property metadata does not authenticate
its writer. Returning from fire does not prove a physical stop. Preserve the
known failing attempt and its accepted exact-attempt terminal-effects conclusion.

## Quick checks and original failure

The original utility attempts 5cecc80d and 4e1fb5c0 never ran tests; their immutable
INCOMPLETE outcomes and root reconciliation receipts remain separate.
890b4e44 ran once, failed after 11 private observation controls, and did not reach
the original five examples. Its first fixture-helper test used the capture local
`output`, which the evaluated fixture Ruby legitimately replaced with its result
Hash. All original inputs/results are retained in `unit-890b4e44-failed/`.

Only that private capture local was renamed to `captured_stdout`; assertions and
tracked diagnostic source were unchanged. The same batch then passed native
session 68411/exit0, 20 examples/0 failures/0 pending, seed50834, RSpec24.4059s:
11 observation controls, four helper enabled/disabled controls, and all five
original stop_vps examples. It covers original-vs-disabled/enabled order and
writes, no extra SQL, detached pre-effect snapshot, rejection/short circuit,
unloaded/missing status, submission/suspension/locking, original error identity,
diagnostic failure isolation, wrong/invalid target and fixture-only metadata.
See `unit-final-receipt.json`, `quick.log`, `quick.json`, `quick.exit`, and private
`diagnostic_spec.rb` SHA256
`fd80bc5f2762c0a19e8ed0ac0561874f13a997219911773223090153c3b4eb22`.

Task Ruby syntax, Nix parse/format, extracted common/scenario Ruby syntax,
RuboCop and whitespace checks passed during preparation. Normal commit hooks
passed Nixfmt/MigrationSpecs/WebuiI18n/RuboCop/ApiI18n and commit-message checks;
the latter emitted advisory >72-column warnings, with all lines <=80. The branch
checkout's stale Overcommit signature refusal and consequent unprepared commit
failure are retained in `commit-setup-failed.*`; actual branch/index effects were
reconciled before signing unchanged trusted configuration normally and committing.
No hook was bypassed. All own cells/native sessions are terminal.

## Single later runner invocation and prerequisites

From the exact clean diagnostic checkout:

```sh
./test-runner.sh test tasks/dataset-expansion-enforce-and-resolve
```

This is the normal repository wrapper, using its unchanged flake.lock and
vpsAdminOS test framework. It needs the normal Nix/QEMU/KVM runner capacity,
substitutable pinned VM/package inputs and the existing services+one-node fixture;
no sibling checkout, NIX_PATH, production/private configuration or extra service
is needed. Root must assess build/capacity and assign the sole long-run owner.
Unexpected local kernel builds retain the repository/workspace stop-and-escalate
rule. Retained warm runtime is about20–25minutes (1209.16s); this is not a new
check timeout. Existing rake600/chain900 bounds and all final assertions remain.

Source selection is preserved at tests/all-tests.nix:43; explicit ci/tasks tags
remain, with existing tests/ci-selection.yml tasks mapping. No selector or test
identity changed. This was a static source confirmation, not a new runner call.

Root owns independent affected review and separate admission of this ONE run.
Accept only fixture/task identity, branch evidence, original assertions and actual
terminal-effects receipts. Stop after that result. Retain diagnostic ref/evidence,
then remove temporary task instrumentation and fixture opt-ins before final
feature publication/integration. No automatic retry, speculative quota fix,
physical run/build, push/export/client/pin stream or lifecycle action was taken.

No product-document update is useful for this temporary diagnostic; intent,
limitations and removal live here with its execution evidence. Main session
plan/state/design remain root/architect-owned.

Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-30-oomd-abuse-policy/
