# Reboot recovery repair

Find why retained sessions cannot recover after aitherdev reboot, implement the
smallest compatible fix, verify it, deploy it and integrate the affected branches.
The user also directs resuming 2026-10-24-vpsadmin-haveapi-upgrade and
2026-10-30-linux-cve-review after the fix is verified, and subsequently added
2026-10-30-oomd-abuse-policy.

Initial scope: dev-workspace recovery authority and submission observation;
workspace runtime selection and vpsfree-cz-configuration only as deployment needs.
Read retained identity diagnostics without modifying session records. Reproduce
the failing precondition with disposable state before changing recovery behavior.
Preserve retained threads, journals, submission receipts and ownership checks.
No schema migration is planned; old/new packages must continue reading existing
state. Application selection is forward-only; recovery uses a compatible newer
package. Host deployment uses the configuration repository if required.

Verification: focused regression and negative identity/submission tests, quick
checks, committed independent whole-branch review, relevant package/integration
checks, deployed portal health and recovery. Continue only the three requested
sessions after verifying the fix. The user authorized merging the verified fix;
record the concrete affected repository/target set once root cause is known.

Documentation: keep investigation and rollout evidence here; explain lasting
recovery invariants in dev-workspace's existing session/recovery documentation.
This external conversation uses a newly created threadless maintenance session;
there is no retained roster, so the lead owns investigation and implementation.
