# Required runtime-availability coverage inventory

Refreshed source inventory for published B
`556a6e51b141fa419d620ad0d4ccd629fd2be6f5`, based on deployed/current
`b3a6eb2fc0b41cf0cb965bf4c39991815d9df734`, exact client `6e469863a69c`.
The old inventory and complete verification provenance remain in
`package-b-before-forward-refresh-2026-10-24/`.

The final exact-pin quick selection now **passes every Go component test in the
table below**, including the `TestSessionPreparation` generation/confirmation
cases, admission and accepted-fork recovery. Naming/preparation package time
36.625s; admission/fork package time 5.963s. Commands, complete logs and final
checked-tree identity are in `package-b-forward-{naming,admission-fork}-result.json`
and matching `.log` files. No new product test was added for this inventory.
Ruby/package/native checks on refreshed inputs await independent review and the
lead's fresh watcher. Historical full-check success does not certify this head.

| Requirement | Existing exact test and scope | Check membership/status |
| --- | --- | --- |
| Session admission/handoff while a collection-compatible shared generation lock is held | `portal/internal/web/creation_test.go:29`, `TestCreationAdmissionSharesGenerationWithPayloadCollection`: actual `/sessions` acceptance and handoff with a manually held shared lock. It does not start an actual collector. | Final `admission-fork` quick PASS; ordinary package Go suite also includes it. |
| Collection admission shares generation with sessions but excludes preparation and activation | `test/workspace_coordination_test.rb:16`, `WorkspaceCoordinationTest#test_collection_shares_generation_with_sessions_but_excludes_preparation_and_switches`: real host command/locking, waits for an admitted preparation; while collection is paused, shared generation admission succeeds and exclusive activation/new preparation fail. The collector body is a controlled stub. | `ruby-workspace_coordination-0`, from SHA-256 identity modulo 2 in `test/run_ruby_suite.rb`. Included in aggregate/package; pending final-head evidence. |
| Actual collector excludes candidate publication/retained grants during payload removal | `test/workspace_coordination_test.rb:62`, `WorkspaceCoordinationTest#test_admitted_collection_excludes_candidate_publication_and_retained_job_grants`: runs the actual collector, pauses at Git worktree removal, proves candidate publication waits and retained job grants do not pass. It does not submit a portal creation request. | `ruby-workspace_coordination-1`; included in aggregate/package; pending final-head evidence. |
| Portal refuses admission while package activation owns the exclusive lock | `portal/internal/web/creation_test.go:51`, `TestCreationAdmissionDistinguishesRuntimeUpdateFromUnavailableLock`: exact HTTP 503 reasons for exclusive-lock contention vs unavailable lock. | Final naming/preparation or admission/fork quick PASS; ordinary package Go suite also includes it. |
| Naming result cannot reserve after its package generation changes | `portal/internal/web/preparation_test.go:818`, `TestSessionPreparationGenerationChangeCannotReserve`: pauses naming, changes profile generation and proves no base/slug is saved. | Final naming/preparation or admission/fork quick PASS; ordinary package Go suite also includes it. |
| Waiting initialization cannot execute after generation switch | `portal/internal/web/creation_test.go:798`, `TestCreationRechecksGenerationAfterWorkerTransitionLock`: worker waits on exclusive transition, profile changes, worker rejects as superseded. | Final naming/preparation or admission/fork quick PASS; ordinary package Go suite also includes it. |
| Pending preparation confirmation cannot write/dispatch after generation change | `portal/internal/web/preparation_test.go:1526`, `TestSessionPreparationPendingConfirmationRejectsSupersededGeneration`: injected pending sync then changed profile, all status/replay confirmation refuses without naming or new sync. | Final naming/preparation or admission/fork quick PASS; ordinary package Go suite also includes it. |

Supporting collector safety tests:
`CoordinationGcTest#test_integration_preparation_excludes_collection_and_retains_hook_dependencies`
at `test/coordination_gc_test.rb:185`, and
`#test_running_preparation_defers_all_collection` at `:640`, belong to
`ruby-coordination_gc-0`. The latter substitutes process-inventory evidence;
it is not actual-process/VM proof.

## Exact existing commands

The existing narrower Go-only component command (all selected cases already pass in the broader final quick checks):

```sh
nix develop --command go -C portal test -mod=readonly ./internal/web \
  -run '^(TestCreationAdmissionSharesGenerationWithPayloadCollection|TestCreationAdmissionDistinguishesRuntimeUpdateFromUnavailableLock|TestCreationRechecksGenerationAfterWorkerTransitionLock|TestSessionPreparationGenerationChangeCannotReserve|TestSessionPreparationPendingConfirmationRejectsSupersededGeneration)$' \
  -count=1 -timeout=20s
```

The existing Ruby membership can be executed by the lead's watcher through:

```sh
nix build --no-link --print-build-logs \
  .#checks.x86_64-linux.ruby-workspace_coordination-0 \
  .#checks.x86_64-linux.ruby-workspace_coordination-1 \
  .#checks.x86_64-linux.ruby-coordination_gc-0
```

`nix/ruby-checks.nix` defines those names and complete shard coverage;
`test/check_ruby_shards.py` verifies the aggregate. The package's
`nix/workspace-portal.nix:305` check phase requires `${rubyChecks.all}` and runs
`go test ./...` at `:321`. Therefore
`nix build --no-link --print-build-logs .#checks.x86_64-linux.package` supplies
both Go and complete Ruby coverage. The `session-creation` VM builds its custom
`mkPackage` with that same package check phase; these tests are an indirect
package dependency, not concurrency scenarios inside the VM script. Current-head
CI's `fast` job also builds package and Ruby checks. A prior provisional fast
job passed, but that is not claimed as final-head execution proof.

The naming-backend-failure VM cases are explicit in
`nix/tests/session-creation.nix`: `native naming retry reaches success without
manual choice`, `settled terminal transient naming error permits one fresh call`,
`persistent transient naming error stops after two utility calls`, and `failed
naming stops before reservation and keeps manual recovery`. Their corrected native execution on refreshed inputs remains pending the final review/watcher gate.

## Explicit coverage limit

No existing single fixture was found that submits a real portal `/sessions`
request while the **actual collector sweep** is paused in payload removal, or
combines that real request with an actual package activation attempt. Existing
coverage composes real portal admission under the same shared lock, host command
lock/exclusion tests, and a real collector/candidate-publication race. The VM
script itself does not close that end-to-end concurrency gap. If acceptance
requires that combined real-collector/portal scenario, it needs a separately
assigned bounded test follow-up before final readiness; it must not be inferred
from a green `.session-creation` alone.


## Newer deployed recovery coverage retained

`test/workspace_host/profile_transition_test.rb` is byte-identical to deployed
baseline. Its existing tests include:

- `test_retry_policy_blocks_selected_preparation_and_preserves_the_selected_profile`
- `test_retry_policy_created_after_preparation_is_rechecked_before_selection`
- `test_retry_policy_candidate_self_activation_cannot_bypass_the_guard`
- `test_retry_records_require_a_compatible_forward_package`
- `test_forward_retry_preserves_pending_evidence_when_the_candidate_was_already_selected`

`test/workspace_host/failed_creation_delete_recovery_test.rb` also remains
byte-identical, including interrupted ordinary deletion replay, exact current
operation/history, original confirmation, missing native retirement and start
provenance refusal. These are included by `test/workspace_host_test.rb` and
`nix/ruby-checks.nix` in `.#checks.x86_64-linux.ruby-workspace_host-0`, then the
aggregate/package checks. Refreshed execution is pending the lead's watcher;
no live records or package selection were inspected or mutated by B.

Architect statically rechecked and rebound `collection-probe-plan.md` to exact
final B556a6e51. Its executable prototype files are unchanged and compile-only
passed; actual collector/portal execution remains pending. It proves custom-name
admission/reservation/handoff with preparation/switch exclusion, not a usable
native conversation during collection. Separate packaged native readiness is
required. Do not infer that stronger claim from `.session-creation` alone.
