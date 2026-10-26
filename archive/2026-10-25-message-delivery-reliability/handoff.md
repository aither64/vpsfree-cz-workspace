# Message delivery merged and released

Complete: all four approved feature branches are integrated and proved on remote
master. aitherdev and all repository claims are released. Independent review and
post-merge CI passed, including runtime archive, creation and host checks. No
work, blockers or owned commands remain; no user action is needed.

The fix is live. Send/retry deduplication, naming, lifecycle recovery, portal health
and database integrity passed. Native Codex 0.163.0 remains at its original PID.
The original blocked session can accept new messages; its stale attempt was
recovered without resending obsolete input.

Final pins preserve the exact deployed runtime/library and application artifact.
Old deployed source refs and all feature branches remain retained. No extra
system activation, session archive/delete/stop or branch deletion occurred.
The session remains open for follow-up. SQLite recovery remains forward-only;
never restore old forensic backups over newer receipts.

See [state](state.md), [refresh review](integration-refresh-review.md),
[post-merge CI](post-merge-ci.md), [rollout](rollout.md), integrated-lineage.json
and aitherdev-released.json for exact revisions and evidence.

https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-25-message-delivery-reliability/
