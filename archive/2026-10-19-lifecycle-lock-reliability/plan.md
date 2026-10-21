# Lifecycle lock reliability

Implement the approved shared lifecycle repair in dev-workspace, the consuming workspace and vpsfree-cz-configuration. Explicit archive/revive/delete wait through ordinary creation/session contention with consistent lock ordering; automatic scans skip busy sessions without losing inactivity evidence. Revalidate accepted identity and journal ownership after waiting. Preserve existing archive/recovery/receipt formats, confirmation, capture and independent tracking-sync policy.

Remove the portal conversation-mutex/runtime-lock inversion. Archive reports waiting through existing presentation progress and retains its worker/receipt across portal restart. Never replay a mutation after lock acquisition; actual authorization, ownership, journal and filesystem errors remain errors.

Compatibility: no schema migration; old journals retain their saved policy, package generation guards remain held, old browser progress readers remain compatible. Deployment is forward-only: select the same published runtime through the workspace nested override and configuration dev-workspace/devWorkspace channel, validate composition, build exact commits, then coordinated system/profile activation under aitherdev reservation. Deployment direction is the user request and approved plan; no default-branch integration approval exists.

Verification: deterministic lock/barrier tests, opposite-lock-order regression, changed identity/conflicting journal while waiting, cancellation and restart, duplicates, auto-archive continuity, unrelated sessions and tracking deadlines. Quick Ruby/Go/browser checks precede committed whole-branch independent review; packaged suite and archive lifecycle VM follow review. Retry the original retained archive request after deployment and verify successful local closure plus recovery preservation.

Documentation readers are runtime maintainers and operators. Supported invariants go in dev-workspace/docs/session-archive-recovery.md; individual rollout evidence remains here in rollout.md.

User steering: successful archive must release its machine reservations. This
supersedes the previous retain-deployed-reservations lifecycle rule for archive.
Release at local archive completion atomically with the exact owner lifecycle
receipt, including idempotent completion replay of predecessor receipts. Keep
holds through incomplete cleanup and running/uncertain deployment recovery;
cancel queued jobs, retain deployment artifacts/history and do not reacquire on
revive. Deletion retains its prior semantics. No merge proof or review-finish
ceremony is required to release an explicitly archived session. Focused store
regressions pass (4 tests/19 assertions). Runtime coordinator docs own this policy.
