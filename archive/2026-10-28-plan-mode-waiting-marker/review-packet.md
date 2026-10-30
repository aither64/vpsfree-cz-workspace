# Final independent review packet

## User scope and acceptance

User: "I noticed that when codex in plan mode asks the user a question and
waits for its answer, html document title of that tab is not given the
appropriate marker, so it is not clear that it's waiting on input. investigate
and implement a solution."

Restore existing unseen blocking-input `?` title marker; preserve focused-visit
acknowledgement, resolution, separate consecutive question identities,
nonblocking questions, approval/completion handling and reservation prefixes.
No merge, activation, deployment or session closure authorized. No production
browser renderer change, Codex release change or new request registry intended.

Session: `2026-10-28-plan-mode-waiting-marker`, workspace
`/home/aither/workspace/ai/vpsfree.cz`. Read [plan](plan.md), [design](design.md),
[state](state.md) and [implementation evidence](implementation-evidence.md).
Lead started tracking at `1085b570d`. Architect0 designed; implementer0 alone
owns both application repositories serially. Working period began about
17:19 UTC, 2026-10-29; design reached root cause and a stable brief before edits.

## Risk and lanes

Overall high under the skill because optional metadata enters persisted
activity checkpoints and the reusable library's provider/consumer snapshot
contract. Scope remains a bounded compatible fix. Review **general**,
**architecture/repetition**, **scope/proportionality**, and **risk/compatibility**.
Read mandatory-change-review/SKILL.md and all four lane references in full.
Local operator is trusted per dev-workspace AGENTS; remote clients remain
untrusted. No new answer authority or private question/command/answer storage.

Selected reviewer0, independent read-only purpose review, ready, native thread
`01a188ac-be29-7da2-813c-e3cb96f773d9`, retained `gpt-6.1-sol`/xhigh; no fallback.
Reviewer performs review directly without nested agents.

## Ownership, interfaces and compatibility

codex-web owns native request observation and ActivitySnapshot. dev-workspace
pins/imports that provider for its passive activity client and attention endpoint.
Current dev-workspace upstream base pins codex-web base f6f4a187. New portal needs
new provider compile-time API, while old callers ignore the optional field.
Discover representative consumers from imports, exact pins, docs and wrappers.
Observe request identity without interactive Prompts. Request resolution,
terminal/unknown states, stale snapshots and reconnect must suppress obsolete
identities. Keep exact native event digest and existing acknowledgement reducer.

Persist optional itemId/method in existing schema 1; predecessor uses ordinary
json.Unmarshal (ignores additions), new code accepts absent fields. No migration,
schema version bump or state rewrite. Missing identity contributes timing but
cannot invent an attention event. Existing byte/count bounds remain.

## Final branch inventory

See final heads/commit series/diffstat appended below and implementation evidence.
Both worktrees are under `worktrees/2026-10-28-plan-mode-waiting-marker/`.
Review complete base-to-head series and final diff for each. Single logical
provider fix with support tests/docs, followed in the consumer repository by one
logical attention fix with necessary exact provider pins and support tests/docs.
No obsolete branch iterations, follow-up/fixup commits or repeated dependency
streams intended; independently confirm. Only dependency stream is codex-web
source/library selected in flake.nix/flake.lock, portal/go.mod/sum and vendorHash;
no unrelated input changes. No migrations, merged/released/deployed migration
versions or transitional paths. Feature publication is dependency availability,
not release or integration evidence. Explicitly conclude whole-branch history,
repeated streams/consolidation, and "no migrations".

## Documentation and quick checks

Provider docs/reference.md#recorded-activity describes optional identity fields,
privacy/observer authority and schema-1 compatibility. Consumer
 docs/browser-notifications.md links the owning contract. Individual runtime
activation remains unperformed; no deployment procedure change needed.
Lead applied user-facing writing skill to consumer explanation, with no rewrite.

Quick checks and failure diagnosis are detailed in implementation-evidence.md:
provider Test(Activity|Observer) passes with real passive Unix transport fixture;
consumer Test(Attention|Notifications) passes; browser harness 75/75 passes.
Formatting and diff checks pass. No declared hook framework or hook bypass.
Earlier provider check failed during setup due to absent gcc; same pinned gcc
resolved it once. Vendor hash discovery's fake-hash mismatch is intentional;
final successful dependency verification recorded before review starts.
Long flake suites and CI waits are assigned by lead only after this review.

## Reviewer output

Write review-report.md in this session directory, then report to lead. Findings
first with severity, lane, file/line and commit evidence. If none, state no
findings plus residual risks/test gaps. Do not edit application code or run long
integration tests. Confirm reviewed exact ranges and actual retained settings.

## Exact completed ranges

- codex-web base `f6f4a187509b3bebfc81585c535be856eaab0d04`,
  head `9d337b70987fdf1dd42a5d8efff31f755a122550`.
  Complete series: `9d337b7 activity: expose passive blocking request identities`.
  Final diff: 6 files, 252 insertions, 33 deletions (includes gofmt alignment).
- dev-workspace base `cc0d452a0653a112c8a013492c1734d9554bb909`,
  head `5f4f1c1c52cc009970a2697f5dbc330c0a4dd7a3`.
  Complete series: `5f4f1c1c portal: use passive request identities for attention`.
  Final diff: 10 files, 109 insertions, 35 deletions.

Both final changes committed; focused checks cover unchanged final source.
No obsolete commits or migrations in either single-commit series. Full diffs:
`git diff BASE HEAD` in the corresponding registered worktree. Downstream locks
select upstream exact head/NAR `sha256-IGseAWlpopeTARLDeSI5NcWG6QiXBCrmbN6OjqnYw6c=`;
Go version `v0.0.0-20261029173332-9d337b70987f`; vendor hash
`sha256-2f7iuoBO4KsjNKQH4iAOtjWwKuNC9O4H+YfLPtAZy0E=`.
