# Affected review: lifecycle CLI store ownership

Reuse the retained reviewer/settings and prior baseline-review.md. All intended changes are committed and quick checks pass. Four affected lanes for the small integration correction; reuse previously assessed unchanged behavior, baseline equivalence, source waiting and history. No new schemas, APIs or migrations. Review only; no source edits, long tests or live mutations. Write retirement-review.md.

CI 40189655484 (runtime101a1850) was cancelled as superseded, but its full logs retain an actual late creation failure before cancellation: ordinary deletion's thread retirement tried to decode a schema-4 fence as old JSON (unknown field storage). The fork/plan creation scenarios had progressed successfully. --log-failed was empty because overall run was cancelled; full log /tmp/message-delivery-reliability-2026-10-25/cancelled-baseline-all.log contains the error at line14633. No blind retry is accepted.

The Ruby thread retire helper omitted --user-state-root. threadCommand passes its empty flag explicitly to newCodexClient, selecting socket-adjacent legacy JSON, despite an ambient state root. Correct retire to pass the exact runner-owned workspace and persistent state root. The caller audit found ensure_portal_thread_idle! also reads durable receipts through RequireThreadIdle; pass the same owner flags there. Other store-consuming CLI callers (create/fork, provider, coordinator, observation, teams, explicit archive, frozen settings) already pass the selected state root. Set-name/materialization/initial-message/archive-proof paths do not consume ordinary receipts. Do not change the generic standalone constructor's fallback contract.

Strengthened existing Ruby/Go deletion bridge requires exact owner flags on retirement. It fails before fix (retirement lost selected state root), passes after (~1.5s), preserving team ordering/tombstone proof. Existing Ruby stop/idle fixture now requires exact namespace while proving the late active turn still prevents stop; 1 test/6 assertions passes (~0.42s) using test/dev_session_test.rb aggregate. Directly running its subfile failed because ManagedTmux is supplied by aggregate fixtures; corrected invocation passed. Focused accepted-fork tests still pass (~4.4s), including cancellation and changed source. Ruby syntax and composed-lock validation pass.

The baseline review's Important plan-wait finding was resolved narrowly: the shared verifier defaults to nonblocking, and only accepted fork opts into waiting before destination/provider admission. Plan creation retains its old nonblocking check. Feature docs and design now state that boundary. This removes unintended scope under mandatory-review step9, with focused source/fork and existing plan tests passing (~4.56s); no confirmation review of this narrow reduction is requested. Inspect as context for the retirement integration fix if needed.

Retirement/idle changes are folded into their owning runtime storage-integration commit. The source-wait correction remains its separate logical commit; no fixup commit remains. The library is unchanged8b60554; schema1 migration/fences and orphan guard unchanged and not yet deployed. Configuration/workspace retain one final generated pin each, with prior superseded pins removed. Baseline storage lineage is unchanged from your verified raw blob/delta comparisons. No machine claim or activation or original-attempt recovery has occurred; aitherdev remains owned by the other initiative.

Final exact heads:
{
  "codex-web": "8b60554bc10c2a6bcbf9732a8b77ad959c317036",
  "dev-workspace": "9634151b9836311c331a58880fbb4c46133fd98f",
  "vpsfree-cz-configuration": "45683e38d3dc8e3ced20eae553f879e46ec84348",
  "workspace": "72e15700b241d75bcbc1eb8abf04542f70d9792f"
}

Runtime complete series above ec53874b:
902f7554f1d33722dfdd23402d2275c2bce07cd6 deps: select transactional message delivery support
d6f3f214d3adc0ad4c0e9eb14ad092ce55213c76 portal: use transactional shared submission receipts
6416433640f753ce904302b9b233a2e19acf19d7 portal: finish admitted sends and retry transient failures
9634151b9836311c331a58880fbb4c46133fd98f session: wait for accepted fork source readers

Compare prior reviewed101a1850 against current runtime; obtain final pin diffs from Git. Preserve explicit whole-history/pin consolidation and migration conclusions from the previous report, updating changed ranges. Docs remain codex-web/docs/submission-storage.md, runtime docs/dev-sessions.md and docs/workspace-portal.md; current operational evidence rollout.md. No new feature-doc section is useful for forwarding existing owner flags, because user-visible semantics are unchanged.
