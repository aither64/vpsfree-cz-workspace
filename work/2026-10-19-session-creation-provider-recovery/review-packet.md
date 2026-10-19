# Final runtime review packet

Review both commits as the final completed deliverable. Read the mandatory review
skill and its general, architecture, scope and risk references in full.

- Initiative `2026-10-19-session-creation-provider-recovery`, tracking root
  `/home/aither/workspace/ai/vpsfree.cz/work/2026-10-19-session-creation-provider-recovery`.
- Worktree `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-19-session-creation-provider-recovery/dev-workspace`.
- Runtime base `8385699aabcc2cfc74b585ca653a4658ff3eef75`.
- Runtime head `3c0b459a4c1aee818d001c10404df121bfe27630`.
- Complete series: `8920252` session provider receipt/initialization correction,
  `3c0b459` selectable errors/Copy error/browser test. Independent behaviors are
  separate commits; each owns corresponding tests/docs. No superseded approaches,
  migrations, repeated pins, generated artifacts or dependency updates in series.
  Existing merged histories stay untouched. Explicitly assess whole history and
  conclude on migration lineage and repeated streams.

User reports that after creation admission/redirect, initialization fails with
`direct team creation request is no longer current; start a new request` and
polling clears selected error text every second. Read-only live inspection found
two failed schema-3 requests with `provider=codex-lb`, including the Oct 19 HaveAPI
request. Both have the exact downstream error. Real Ruby validation of that
receipt before editing reproduced the refusal. No live request was retried.

Acceptance: current portal-written receipts reach Ruby receipt preparation,
initialization retains provider intent and exact retry identity, no duplicate
lead/team/first turn, invalid or changed provider intent still refuses, omitted
provider remains valid. Plan-only destinationSettings remains boolean. Error text
selection survives repeated polling and is easily copied. No Codex patch/rebuild.

Read plan/design/state for detailed invariants and recovery. Main changes forward
provider from Ruby start to the existing receipt validator, compare intent for
all creation kinds, allow provider and plan's optional destination flag in strict
direct receipts. Retired virtual-team creation remains retired. Schemas unchanged;
preceding package still has its known refusal for affected explicit selections.
Provider transition fences remain. No database changes or coordinated node update.

Quick checks passed in repository Nix environment:

- `TestCreationReceiptRubyInitializerContract`: 15 Go-serialized receipt cases,
  real Ruby preparation twice, Go rereads resulting binding, changed-provider
  negatives, 15.95s. No mocked serializer/receipt validator.
- `ruby test/dev_session/agent_team_creation_test.rb`: 17 tests, 208 assertions.
  New direct full-initialization check uses real receipt/journal/retry, external
  native/host effects doubled, confirms one root and initial turn for 3 providers.
- Aggregate-harness focused legacy/provider initialization selection: 5 tests,
  152 assertions. Direct execution of session_initialization_test.rb previously
  failed because its fixtures live in the aggregate harness; diagnosed, no code
  changed to conceal that failed invocation.
- Shipped browser HTTP admission and preparation page Go checks passed (0.949s).
- Node syntax, gofmt and diff whitespace checks passed.
- Real Playwright selection/copy check is prepared and will run after review;
  no browser success or deployed fix is claimed yet.

High risk classification for persisted acceptance/CLI/provider consistency, all
four review lanes. Operator is trusted per repository AGENTS; remote browser
inputs remain untrusted. Preserve wrong-session, concurrency, integrity and
interruption checks; do not add compromised-local-operator defenses.

Documentation: README already links docs/session-preparations.md; that guide owns
the changed request/selection behavior and retry invariants. Individual deployment
and evidence belong in this initiative, not project behavior docs. No KB changes.
Runtime owns the portal serializer and Ruby CLI. Consumers are workspace's direct
nested runtime pin and configuration's devWorkspace channel, currently selecting
5c799c1. No public field/schema is introduced; companion pin work will follow.

No eligible retained reviewer: this external initiative was created with
--no-codex and has no team. Installed schema-6 catalog
`/nix/store/a5dcgj4hxcf6q87agjnpp20ls9jn004d-dev-workspace-0.2.0/share/dev-workspace/agent-teams.json`,
digest ffaf9deb97720995ad1d662badae7645eba1fede5068eef529c9024efa7e7376,
default lead_reviewed reviewer is gpt-6-astra/xhigh. Fallback independent reviewer
must retain those settings. Remain read-only; do not spawn nested reviewers.
Write findings to final-review.md under this tracking directory and report the
actual model/effort, final head, whole-history and migration conclusions.
