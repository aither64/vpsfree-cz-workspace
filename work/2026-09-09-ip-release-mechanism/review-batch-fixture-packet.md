# Concurrency fixture isolation review

Read review-batch-packet.md/review-batch-results.md for initiative context,
repositories, accepted bounds, owning docs and the completed four-lane review.
Review only vpsAdmin d2ebb98f4..2a9fdf2dd, currently committed, in the registered
vpsAdmin worktree. The fixup will fold into its owning campaign API commit.
KB2006e6d0/templatesf275bf35 unchanged here; KB exact pin will refresh mechanically.

Hosted API engine jobs104986484024/104986484549 failed three migration-key specs.
Concurrency fixtures commit outside ordinary RSpec rollback. Their liveness
helper refreshed shared seeded Node/NodeCurrentStatus rows, making a seeded pool
eligible in later discovery. An ordered concurrency suite followed by the three
GenerateMigrationKeys specs reproduced all three failures:17 examples/3failures.
The same ordered run passes17/0 after restoring node/status/audit fixture rows.
All commit hooks pass. No migration-key assertion or production code is changed.

Goal: independent committed concurrency tests leave the shared database seed
unchanged for later specs. Inspect original setup/teardown and helper writes.
Non-goals: change resource locking, migration keys, generic test infrastructure,
DB schema, API, user text or deployment. Risk low: isolated test fixture cleanup,
no production/persisted contract changes. General and architecture lanes apply
(handwritten setup/teardown); scope/risk lanes add no new production boundary.
Model gpt-6-astra/xhigh. Direct review, no edits/nested agents/deployments.

The d2ebb98f4 runtime integrations were already running when CI found the leak;
they continue because this delta changes only API unit-test fixture teardown.
No new long integration run has started after this test change. Existing owning
docs stay correct; root cause and verification are recorded in state.md and
notes/vpsadmin/2026-09-16-committed-concurrency-fixture-isolation.md.
