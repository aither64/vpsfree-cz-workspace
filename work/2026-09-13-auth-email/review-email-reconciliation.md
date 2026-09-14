# Email refinement review reconciliation

All four required lanes used fresh `gpt-5.6-sol/xhigh` reviewers. No Blocking
finding was reported. General and architecture reported the same Important
DNS-locking issue; risk reported Important rollback ordering; scope found no
additional issues.

1. **DNS latency under the account lock — fixed.** `EmailLogin.start` checks
   current send budgets without taking row locks, resolves PTR outside the user
   lock, then enters the original authoritative user/budget/token transaction.
   The preliminary and locked checks share one limit/window definition.
   Inspection confirmed no reservation or authority is granted by the early
   read, and verification proves stale preliminary acceptance still loses to
   the locked budget check. Existing shared-IP concurrency coverage also passes.
2. **Rollback ordering — fixed.** The rollout documentation explicitly requires
   restoring earlier templates before any older API worker returns. New workers
   retain the older template variables. Pending challenges from undeployed
   intermediate feature revisions are not a supported upgrade format.

The 32-example remediation suite passed with zero failures. The preceding
96-example API suite, final four mail examples, template package checks,
syntax/lint hooks and all four plain-text/HTML preview comparisons passed.
These changes directly implement the requested review remediations; no new
public behavior, budget rule, storage layer or delivery mechanism was added.
Focused inspection and checks satisfy the narrow-fix rule; no reviewer rerun
is needed. Browser integration follows the committed reconciliation.
