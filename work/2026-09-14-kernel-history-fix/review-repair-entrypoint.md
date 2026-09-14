# Focused general review: repair entrypoint corrections

Reviewed the replacement delta
`b851ea971ed1cdcec2548395ec1ea493e8344cb6` to
`feaa152436cf66e980c4e53f86a541bb10daae16` in vpsAdmin. Both repair commits
share parent `7b4aec6bb9b948ab3d1bdf90a886b99a4ebd4ff5`; the corrections are folded into
the unmerged commit that owns the repair task and its integration coverage.

## Findings

No Blocking, Important, or Advisory findings.

The renamed file, class, Rake dispatch key, and explicit CI path consistently
use `NodeKernelHistoryBoundsRepair` / `node_kernel_history_bounds_repair`, which
matches `VpsAdmin::API::Tasks.run` and its `classify` lookup. The public command
remains `vpsadmin:node:repair_kernel_history_bounds`, so the operator
documentation and command contract remain valid.

The new RSpec example loads that public Rake task through the existing isolated
Rake/environment helpers. `invoke_rake_task` reenables the task before each
call, so the example actually covers preview, apply, and a second idempotent
apply rather than relying on Rake's once-per-process invocation behavior. The
VM scenario now uses the same packaged `bundle exec rake` construction as the
existing task scenarios. Its 19-character synthetic `vpsadmin_version` fits the
schema's 25-character limit and changes no behavior under test.

The five-file correction delta is limited to the entrypoint repair, its direct
regression, the matching selector path, and the invalid integration fixture.
The existing repair commit message still describes the final result and the
two-commit feature split remains coherent.

## Verification and residual gaps

- Focused repair spec: 26 examples, 0 failures, including the public Rake
  preview/apply/idempotence regression.
- CI selector test: 16 runs, 55 assertions, 0 failures.
- Coordinating-agent evidence at the reviewed head: combined
  recorder/repair/StableState/supervisor suite, 106 examples, 0 failures.
- `git diff --check` passed and the project worktree was clean after review.

The long `supervisor-runtime-ingestion` VM scenario remains the integration
gate for the exact packaged command path, RabbitMQ ingestion, supervisor
restart, and disposable repair sequence. The focused RSpec regression proves
dispatch and database behavior but cannot validate those packaged runtime
boundaries by itself.
