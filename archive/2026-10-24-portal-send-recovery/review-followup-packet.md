# Final source review follow-up

Reuse your independent reviewer identity and read the previous report. Read the
mandatory review skill and general, architecture, scope and risk references.
Remain read-only and review directly without subagents.

Complete final ranges (clean committed worktrees):
- codex-web: 11ec57d2203fc735696fe75a837d47da55a5c6af..f66a8b2f46a6d43115327f42edbdaf58581e3c25
- dev-workspace: b3a6eb2fc0b41cf0cb965bf4c39991815d9df734..13308f030bd1e88c5cbb94cf1aa308cfc814f2c2

All three original Important findings are corrected: normal composer retires
unsent before HTTP and shows sending; failed browser storage preserves original
uncertainty; queue-start uses the operation token. Focused Node and Go checks
pass; the real browser regression also now reloads a retried unsent message
while its response is held. Inspect these narrow remediations directly.

An additional parent audit found shared-ledger concurrency at write admission:
two independent clients can both observe prepared before either reaches its
writer. markSendSubmitting previously accepted an already-submitting record.
It now atomically requires prepared and no queued delegation. A losing writer
reconciles current shared state instead of emitting another mutation or claiming
non-delivery. TestSharedLedgerAdmitsOnlyOnePreparedSender uses two connections
and a held native reply to prove exactly one mutation, uncertain losing caller,
and subsequent accepted-receipt recovery. Review all applicable lanes for this
added boundary, including the existing SendAttemptedWithOptions consumer.

The same-ID message/options bindings, schema-3 ledger and native protocol remain
unchanged. No migrations. Parent folded corrections into owning commits: final
codex-web series is one functional commit; runtime series is functional + one
final dependency update. No repeated pin streams remain. Compare final complete
series and final diff, and explicitly assess history/migration conclusion.
Old reviewed codex-web head 2c4c3460ac6d109699d05115b0ebb9e6eb3410df and runtime
8ccdd2e43b6bb78ce474e19c69d232442db2562a remain available for comparison. Neither
was deployed by this initiative. New exact Go/Nix provider selections match.

Long integration checks are still held. Mechanical matching workspace/config
pins will be refreshed to the final reviewed runtime, checked and committed;
no functional host/coordination changes are planned. User now also authorizes
merging this fix's affected master branches AFTER deployment and verification.

Write review-followup-report.md alongside this packet. Report findings and
remaining test gaps; do not run long tests or deploy.
