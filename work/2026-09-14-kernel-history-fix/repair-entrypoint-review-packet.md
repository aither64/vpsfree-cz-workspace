# Focused repair command and fixture correction review

Owned session: 2026-09-14-kernel-history-fix.
Tracking: /home/aither/workspace/ai/vpsfree.cz/work/2026-09-14-kernel-history-fix.
Worktree: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-14-kernel-history-fix/vpsadmin.
Read its AGENTS.md and mandatory-change-review general lane instructions.
Do not edit project code or run production/lifecycle operations. No subagents.

Review the committed delta from b851ea971ed1cdcec2548395ec1ea493e8344cb6 to
the head appended below. Original base is 791ab3aa89e2f613979da6090b89785c78245db5.
Full general/architecture/scope/compatibility implementation reviews and
separate downstream general/compatibility review have completed; see
review-reconciliation.md for findings and resolutions. Overall risk remains
high (persisted history and operator repair). This rerun is the general lane
at gpt-5.6-sol xhigh for bounded corrections, with no changed state-comparison,
repair-proof, public-command, deployment, schema, or protocol contract.

The second local supervisor scenario passed the legacy case and nine others.
Its synthetic case timed out: vpsadmin_version had 26 characters against a
25-character DB column. A temporary DB preflight reproduced ValueTooLong, then
passed the full stable/transition/restart/removal/repair sequence with the
19-character kernel-history-test value.

Testing the same sequence through Rake found Tasks.run singularizes its class
name with classify: node_kernel_history_bounds resolves NodeKernelHistoryBound,
not the implemented class. Rename the internal class/file/dispatch key to
NodeKernelHistoryBoundsRepair / node_kernel_history_bounds_repair. Keep public
vpsadmin:node:repair_kernel_history_bounds and all argument semantics unchanged.
Update its explicit CI selection path. Add a public Rake regression for
preview/apply/idempotence using existing isolated Rake/environment helpers.
The VM scenario invokes packaged bundle exec rake through a shell, following
tests/suite/tasks/common.nix, instead of loading Rake inside api_ruby.

These corrections are folded into the unmerged owning repair/integration commit.
Recorder commit 7b4aec6bb9b948ab3d1bdf90a886b99a4ebd4ff5 is unchanged.
No deployment, production repair, merge, archive or other session changes.
Downstream pins will refresh through confctl/canonical KB workflow after local
integration passes; current config4145e961 and KB0770dcfa still pin2a312616.

Quick checks: repair spec plus exact-payload preflight28 examples0fail;
2-file Ruby lint clean; selector16runs55assertions0fail; Nixfmt/diff checks pass.
Standalone rake -T without DB failed in API initialization, as expected for a
local shell with no configured database; real invocation is covered by Rake
specs and the disposable packaged VM scenario. No production DB was accessed.
Report findings by severity with paths/lines and residual gaps, writing only
review-repair-entrypoint.md in this tracking directory.

Committed head: feaa152436cf66e980c4e53f86a541bb10daae16. All commit hooks passed; clean worktree.
