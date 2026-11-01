# Coordinator package

Implementer0 commit: `24f8870a0f9b2dcb871c8bc717424ec1906da817`
(`coordination: skip retained owners without scheduler work`). Shared worktree:
`worktrees/2026-10-26-workspace-cpu-investigation/dev-workspace`.

The accepted design's coordinator package is implemented in
`libexec/workspace-coordination-host.rb`. `coordinate_workspace(entry, engine)`
reconciles uncertain attempts first, inventories validated ledger/claims/journals
once, and selects work in persisted owner order. Idle owners incur no native
verification. Claims, nonterminal jobs, eligible background continuations, due
outbox events and due handoff reminders are included. Completed reminders use
`notification_owner`; bootstrap owners process claims only. Active work rereads
claimed jobs under admission and checks live ownership. Fresh notification
eligibility after owner work includes newly generated events in the same pass.
Existing wake fallback, grant fairness, collection and persistent formats remain.

The five owned paths are the host file, `test/workspace_coordination_test.rb`,
`test/integration_test.rb`, `docs/coordination.md` and the narrow scheduler paragraph
in `docs/integration.md`. Diff: 379 additions, 22 deletions, mostly focused tests.
Architect0 confirmed report-level alignment with the accepted brief; this is not
independent code review.

Focused checks ran through `nix develop --no-update-lock-file --command`:

- `ruby test/workspace_coordination_test.rb --name '/test_scheduler_|test_state_change_wakes_scheduler_and_missing_listener_is_harmless|test_retained_notification_admission_preserves_completion_and_lifecycle_guards/'`: 12 tests, 80 assertions, 3.801 s, pass.
- `ruby test/workspace_coordination_test.rb --name '/test_scheduler_bootstrap_owner_processes_only_claims/'`: 1 test, 3 assertions, 0.357 s, pass.
- `ruby test/integration_test.rb --name '/test_scheduler_dispatches_background_preparation_without_pending_jobs|test_attention_requires_pickup_after_delivery_and_scheduler_reminds_without_replaying_work|test_supervision_failure_stays_attached_and_only_explicit_background_resume_releases_it/'`: 3 tests, 35 assertions, 1.938 s, pass.
- `ruby test/coordination_claims_test.rb --name '/test_fifo_grants_and_durable_notification_follow_explicit_release|test_notification_publication_failure_keeps_grant_and_retries_once/'`: 2 tests, 15 assertions, 1.108 s, pass.
- Ruby host syntax and owned-path `git diff --check`: pass.

The idle test uses a valid ledger exceeding 3,000,000 bytes with 1, 10 and 100
owners. Each real workspace pass performs two ledger reads (including uncertain
reconciliation), one claims read and one journal inventory, with no owner
verification/helper commands or state mutation. Other tests cover every job
state, retry/reminder deadlines, background preparation without jobs, pause and
supervision, bootstrap claims-only, completed reminder delivery, newly generated
claim notices, blocked-owner fairness, malformed inventory and stale generation,
identity, fence, suspension and reconciliation-job selection.

Initial test-only failures were corrected before commit: explicit hash braces
for Ruby keyword separation and asserting persisted ledger order rather than
fixture registration order. No source-level check failure remains. No hook
framework is declared; `core.hooksPath` is unset and canonical hooks contain only
sample files. Commit used the assigned nonblocking Git flock, empty-index guard,
owned-path staging and `git commit -F`; no hooks were bypassed.

No branch fetch/rebase/push, deployment, service action or lifecycle mutation was
performed. Lead owns consolidated final review, broader Ruby/package verification,
controlled benchmarks, publication and deployment. Actual CPU improvement remains
to be measured; deterministic idle work counts are established locally.

## Packaged-check fixture correction

Full packaged check at runtime head `31157fafde754a6ebd8a413f1e91ff4d0f97da1b`
failed its `workspace_host` shard: 229 tests, 2507 assertions, zero failures,
one error, three skips, 82.466 s. Full failed derivation log:
`package-checks/flake-check-failing-derivation.log`; derivation
`/nix/store/55qbv5vh8vqlp7ha1fcrq93v1mg2h9a3-dev-workspace-workspace_host-0-of-1.drv`.

Exact error was `Errno::ENOENT: No such file or directory - systemd-run` from
`dispatch_coordination_collection`; `Store#lock` was only an enclosing stack
frame. `test_coordination_accepts_and_preserves_completed_managed_creation_receipt`
stopped the scheduler via a throw from notification dispatch for an otherwise
idle owner. Intended idle skipping removed that exit path, so the fixture entered
unrelated collection. The hermetic lack of systemd-run exposed this obsolete
fixture assumption; adding a systemd dependency would not fix its logic.

Fix commit `217e3e51dac86db9871fadfe59fae9d5185882ac` changes only
`test/workspace_host/live_switch_test.rb` (+14/-2). It seeds a real due event,
checks dispatch to the retained owner for active and completed tracking, retains
no-ordinary-claim and unchanged-creation-receipt assertions, and refuses unrelated
collection fallthrough. No product source, package dependencies or state contract
changed. Published history was not rewritten; commit used the assigned Git flock,
empty-index guard, owned-path staging and ordinary hooks.

Focused Nix check on the final fixture:
`ruby test/workspace_host_test.rb --name '/test_coordination_accepts_and_preserves_completed_managed_creation_receipt|test_coordination_rejects_unfinished_malformed_and_mismatched_creation_receipts/'`
passed **2 tests, 25 assertions, 0.291 s**, plus owned-path diff check. A prior
focused pass before the final guard wording also passed. This is evidence of a
diagnosed fixture fix, not acceptance of an unexplained rerun. Lead owns narrow
postreview disposition and the known-long affected packaged shard rerun.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-26-workspace-cpu-investigation/>
