# Loaded-root recovery whole-branch review

Retained independent reviewer0, saved gpt-6.1-sol/xhigh/read_only, actual new
turn required with no overrides or nested reviewers. High risk because recovery
of persisted creation journals and preservation of frozen policy/identity are
in scope. General, architecture, scope and risk lanes all apply. Read the full
mandatory-change-review skill and all four lane references before reviewing.
Read applicable workspace/runtime AGENTS and routed procedures, plan/state,
design.md, recovery-design.md, original review-runtime.md/result and remediation.

## Outcome and exact inventory

The real lost-root-response case exposed an unsupported resume of a loaded
unmaterialized root. Keep the sole validated root with its original start-time
policy/environment; normal first-goal path materializes it. Preserve complete
filesystem discovery, ambiguity/identity/fork/roster/error controls, exact-one
initial-goal attempt, materialized policy/environment refresh and saved settings.
SDK missing-thread recognition must stay strict and unchanged.

Runtime base: 4bec20165387d567b761e43b11fdeabb096618d7
Final committed clean head: 924c0ec28c41dd8b56aaf17f2212b302ca614899
Earlier reviewed/measured head: 8ae46f9de6ea54b4dab7a4dbeb694593210cc7a1
Worktree: worktrees/2026-10-02-portal-creation-performance/dev-workspace
Complete base-to-head series:

```text
dfda7b8fc501c4a6f761f6d5bc8451da3cc853b8 inputs: select database-only Codex thread listing support
4262bb23aef3df579c14bf3d66b152b7cbaa3a0f sessions: bypass discovery only for locked fresh creation
924c0ec28c41dd8b56aaf17f2212b302ca614899 portal: stream initialization stages into creation receipts
```

The correction is folded into the owning unmerged core commit. SDK-pin commit
is unchanged; progress/browser patch is separately retained and patch-equivalent.
No superseded core approach, unused compatibility path or follow-up fix remains.
No migrations, schema, protocol/flag, helper contract, catalog, SDK revision or
Codex version changes. Original branch/consumer history inventories stand with
this updated runtime series; require explicit whole-branch/history and
no-migration conclusions. No master integration/deployment/session closure.

Exact earlier-to-final correction scope:

```text
docs/dev-sessions.md                               |  19 +-
 portal/internal/workspacecodex/client.go           |  10 +-
 portal/internal/workspacecodex/client_test.go      | 290 +++++++++++++++++----
 .../workspacecodex/recovery_candidates_test.go     |   3 +
 test/dev_session/agent_team_creation_test.rb       | 139 +++++++++-
 5 files changed, 391 insertions(+), 70 deletions(-)
```

Inspect both complete base-to-head series/diff and bounded old-to-new correction.
All five original fresh measurements remain at the old precise source/candidate:
6.1212149,6.4013488,6.3327301,6.5007339,6.4283412s; median6.4013488/max6.5007339.
Each completed one goal/model with no tools and full progress. These are not
new-head measurements. First root fault failed expected attempt1 after real Go
helper created root and JSON was withheld. Retry2 completed discovery then
failed -32600/no rollout in thread/resume. That form can describe a live root,
so broadening IsThreadNotFound was rejected. Member fault remains unattempted.
Actual fault/package activation/live-canary acceptance remain pending.

## Checks and owning contracts

Implementer source/core docs: docs/dev-sessions.md explains unmaterialized
adoption and materialized resume; owning portal progress contract remains
 docs/workspace-portal.md. Parent applied main-context writing pass to settled
recovery paragraph before commit. Individual execution/provenance remains in
rollout.md, verification-measurements.md and recovery-design.md.

Five Go packages compiled and non-socket checks passed. New socket fixtures were
blocked only by member tool setsockopt permission. Parent actual host/Nix focused
protocol run then PASSED: GOWORK=off GOFLAGS=-mod=readonly go -C portal test
./internal/workspacecodex ./cmd/workspace-portal -run
'^(TestRecover(Creating|Fork)|TestCreationRecovery|TestCreationRoster|TestFreshThreadCreateAndForkAvoidDiscovery|TestLeadThreadPolicy)'
-count=1 -timeout=45s. Package results0.278s and0.076s. No live/model RPC.
Ruby owning test13/144 assertions passed in0.82s; combined relevant selection
47 runs/558 assertions passed in10.39s, 4 environment tmux skips. New fixtures
cover original frozen Full lifecycle/lead policy, MCP/environment/model/effort,
loaded-only discovery with complete filesystem pagination, lost JSON and exact
recorded-ID adoption, real selected no-rollout-on-resume failure, materialized
policy/environment refresh without model/effort replacement, unknown/negative
history/read/fork/disappearance and goal-ledger conditions.

Public provider is existing Go thread-create CLI configured by Ruby
@portal_command. Old/new flags and frozen runtime/model/effort/lead inputs are
unchanged. Representative consumer is libexec/dev-session; teamruntime removal
and other SDK IsThreadNotFound consumers are unaffected. Main production code
change is the unmaterialized return condition and comments only. Check policy
retention rationale and ordinary wrong-identity risks under trusted local
operator boundary, not hypothetical hostile-operator filesystem manipulation.

## Review boundary and next steps

This is a consequential behavior refinement, requiring affected-lane review
(step10), not a requested-fix-only rerun. Reuse same retained reviewer. Confirm
actual native identity/model/effort/independence and public report. No tests,
builds, application edits, credentials/private rollout payload reads, RPC/model
execution, retries, profile manipulation, deployment, integration or cleanup.

Inspect directly, report severity/lane/exact refs, frozen policy and safety
conclusions, complete branch history/migration conclusion and residual limits.
Do not certify unexecuted faults or readiness/deployment. Consumer pins remain
at prior head until source publication; parent will update/review exact pins
and build the corrected package, with separate review of the bounded mixed
provider verification driver after architect preparation. No unaffected SDK
implementation review rerun is requested.
