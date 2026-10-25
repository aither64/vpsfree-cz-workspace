# Required runtime-availability coverage inventory

Read-only inventory originally taken at reviewed B
`ae0399b31746bc14ea2fcbe3185f36d8e4b04885`. Final mechanical refresh B
`4c6b9f177d5b205b21b45880c6ac1bc3c403eef6` preserves this source/test coverage
byte for byte; only dependency pins/hash changed. Latest head
`915b904101eca8170652a8dd198f63e3e3aae967` adds only the separate attention
fixture readiness correction. Current head
`e515437822e6a2ee7e61be7b613d1e058dad56d7` adds only archive-helper failure
diagnostics after915. Both follow-ups are outside the test paths inventoried
here and do not add usable-native-session-during-sweep proof.
No new source, test execution or long run was performed for this inventory.

The required locking semantics have existing component coverage. They were
**not selected by B's final naming-only quick regex**. Final package verification
must supply their current-head execution evidence. The session-creation VM has
no explicit collection-sweep or package-switch concurrency scenario.

| Requirement | Existing exact test and scope | Check membership/status |
| --- | --- | --- |
| Session admission/handoff while a collection-compatible shared generation lock is held | `portal/internal/web/creation_test.go:29`, `TestCreationAdmissionSharesGenerationWithPayloadCollection`: actual `/sessions` acceptance and handoff with a manually held shared lock. It does not start an actual collector. | Ordinary `go test ./...` in package check; not B's naming quick selector. Pending final packaged/current-head evidence. |
| Collection admission shares generation with sessions but excludes preparation and activation | `test/workspace_coordination_test.rb:16`, `WorkspaceCoordinationTest#test_collection_shares_generation_with_sessions_but_excludes_preparation_and_switches`: real host command/locking, waits for an admitted preparation; while collection is paused, shared generation admission succeeds and exclusive activation/new preparation fail. The collector body is a controlled stub. | `ruby-workspace_coordination-0`, from SHA-256 identity modulo 2 in `test/run_ruby_suite.rb`. Included in aggregate/package; pending final-head evidence. |
| Actual collector excludes candidate publication/retained grants during payload removal | `test/workspace_coordination_test.rb:62`, `WorkspaceCoordinationTest#test_admitted_collection_excludes_candidate_publication_and_retained_job_grants`: runs the actual collector, pauses at Git worktree removal, proves candidate publication waits and retained job grants do not pass. It does not submit a portal creation request. | `ruby-workspace_coordination-1`; included in aggregate/package; pending final-head evidence. |
| Portal refuses admission while package activation owns the exclusive lock | `portal/internal/web/creation_test.go:51`, `TestCreationAdmissionDistinguishesRuntimeUpdateFromUnavailableLock`: exact HTTP 503 reasons for exclusive-lock contention vs unavailable lock. | Ordinary package Go suite; not naming quick selector. |
| Naming result cannot reserve after its package generation changes | `portal/internal/web/preparation_test.go:818`, `TestSessionPreparationGenerationChangeCannotReserve`: pauses naming, changes profile generation and proves no base/slug is saved. | Ordinary package Go suite; not naming quick selector. |
| Waiting initialization cannot execute after generation switch | `portal/internal/web/creation_test.go:798`, `TestCreationRechecksGenerationAfterWorkerTransitionLock`: worker waits on exclusive transition, profile changes, worker rejects as superseded. | Ordinary package Go suite; not naming quick selector. |
| Pending preparation confirmation cannot write/dispatch after generation change | `portal/internal/web/preparation_test.go:1526`, `TestSessionPreparationPendingConfirmationRejectsSupersededGeneration`: injected pending sync then changed profile, all status/replay confirmation refuses without naming or new sync. | Ordinary package Go suite; not naming quick selector. |

Supporting collector safety tests:
`CoordinationGcTest#test_integration_preparation_excludes_collection_and_retains_hook_dependencies`
at `test/coordination_gc_test.rb:185`, and
`#test_running_preparation_defers_all_collection` at `:640`, belong to
`ruby-coordination_gc-0`. The latter substitutes process-inventory evidence;
it is not actual-process/VM proof.

## Exact existing commands

The bounded Go-only component selection, if assigned for an additional quick run:

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
naming stops before reservation and keeps manual recovery`. Their corrected
native execution remains pending the final review/watcher gate.

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
