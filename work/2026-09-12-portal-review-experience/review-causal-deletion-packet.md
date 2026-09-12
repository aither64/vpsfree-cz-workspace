# Causal deletion identity review

Review only the committed creation-ordering replacement below and its direct
callers, recovery, locks and package compatibility. The user-approved portal
features and passive observer admission have already passed all required lanes;
do not reopen unrelated completed feature reviews. Original plan/state remain
at work/2026-09-12-portal-review-experience/{plan.md,state.md}. Earlier findings
and decisions are retained in review-reconciliation.md for reference.

The user asked for the portal improvements and then approved implementation,
including early navigation with progress/retry for new/fork/plan sessions, local
Git review with maintained CodeMirror, conversation events/counters/timing and
Messages default. This delta repairs a demonstrated deletion-retry defect inside
that approved scope. Root wall time and observer implementation are unchanged.

Risk is HIGH: persisted private request identity, concurrent initialization and
explicit deletion, recovery and package rollback. Fresh standalone architecture
and risk reviewers use gpt-5.6-sol/xhigh. Scope already reviewed the prior repair;
this replacement removes timestamp ordering and retired-request storage instead
of introducing a generalized lifecycle mechanism. The prior capacity finding is
a direct call-site reuse of reviewed cleanup and is verified by focused tests.
No general/scope rerun merely to confirm those reductions.

## Causal identity and ownership

The previous creation repair compared Go acceptance time to Ruby removed_at.
Ordinary backward clock corrections could allow stale retries after deletion;
future-skewed deletion time could prevent fresh reuse. That ordering and its
mtime fallback are removed. Timestamps remain presentation data.

At acceptance, the portal snapshots the sorted unique verified completed-removal
operation IDs for exactly one workspace+slug while holding its existing runtime
lock across absence/journal checks, snapshot and receipt save. The fixed SHA-256
fingerprint is frozen in the private receipt and CLI request binding.

Receipt-bound CLI calls require the exact current receipt ID/workspace/slug and
valid fingerprint; missing/replaced receipts reject. Under destination locks,
the fingerprint must still match completed deletion history, including both
fork destination-lock phases. Never regenerate a missing baseline from current
history. Manual CLI calls without private receipt flags are unaffected.

Portal startup/capacity/exact-slug reconciliation reuses its existing absence,
authority and pending-journal checks before retiring superseded non-running
receipts. Normal cache retirement suffices because a queued CLI worker requires
that live receipt. There is no new epoch file, index, unbounded ID list, retired
request bucket or arbitrary attachment to one deletion recovery directory.
Canonical tracking and strict creation journals remain in the actual deletion
recovery as before. 

## Compatibility and scope

Only portal/internal/web/creation.go and test fixtures use the private receipt
CLI flags (confirmed by source search). The installed predecessor at runtime
base bcbaf825 has no asynchronous receipt feature, flags or reader. It ignores
these new private files. This initiative has never been deployed; its interim
receipt/binding formats do not require a migration or a permissive fallback.
The supported old CLI still writes the existing schema-1 completed removal marker,
so deletion while the portal is offline is detectable without a clock assumption.
Existing session manifests and strict lifecycle/start/fork/removal formats remain
unchanged; no public flag, dependency, Codex protocol/version or host configuration
changes. Private current-receipt/binding validation belongs to the portal/CLI
process boundary within dev-workspace; the provider is unchanged. Downstream
organization/workspace commits only pin that exact runtime.

The local operator is trusted; retain ordinary concurrency, wrong-workspace,
crash, partial-state and rollback handling. Do not invent an adversarial local
filesystem boundary or unsupported history purge framework. Remote clients
remain untrusted. No integration, archive/delete of the initiative or system
configuration deployment is authorized. Feature user-profile deployment follows
provider -> runtime -> organization -> workspace after review and acceptance.

Perform the assigned review directly. No edits, Git mutations, tests or nested
agents. Report concrete Blocking/Important/Advisory findings with changed-code
and commit evidence, or state no findings with material remaining validation.
Exact heads, delta range and completed quick checks follow below.

## Committed final delta and quick checks

- codex-web: `83770217d63f2c206689d2c569e1c81950544504..83770217d63f2c206689d2c569e1c81950544504`; worktree `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/codex-web`.
- dev-workspace: `c350274225e2886209f4d92e5f01f464bc1caf1a..f2512c1c1466a206d903b21cb80384e8dd59f72f`; worktree `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/dev-workspace`.
- vpsfree-dev-workspace: `a0d7fdca3ccfe20fa920cfba5e4e880caf9cc1da..eaf4a21a77b5accfacd0a44193383fbc6277f506`; worktree `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/vpsfree-dev-workspace`.
- workspace: `ef75f045f1a0a496c23251a25306a98e32438a2f..8456d0980bbb974595c3efb96cec4e857ae4def2`; worktree `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/workspace`.

The runtime contains seven functional commits; the creation fixes are folded
into the early-navigation commit. The other feature commits are unchanged in
content. Autosquash preserved tested tree 1e8bb7bc401683ac887e817b042b169fbe8e3aeb.
Provider is unchanged at 8377021. Consumers only refresh exact pins.

Focused Ruby: `nix shell --inputs-from . nixpkgs#ruby nixpkgs#git -c ruby
test/dev_session_test.rb --name '/portal_(fork|creation|start|plan_start)|fork|exclusive_browser_start|start_seeds|removal|delete/'`: 40 runs,495 assertions,0 failures/errors/skips.
Focused Go: from runtime portal, with Nix Go/GCC/Git/Ruby,
`GOWORK=off GOFLAGS=-mod=mod go test -race ./internal/session ./internal/web
-run "TestCompletedRemoval|TestCreation|TestSessionCreation|TestForkSessionInvokes|TestImplementPlan" -count=1`: session2.073s,web28.704s.
Exact removal confirmation regression also passes session race1.892s.
Prior capacity tests cover512 retired receipts,513 startup records and protected
running/unresolved/locked/journal-owned requests. Git diff whitespace check passes.
Full packaged/browser/live rollback acceptance follows this review.

Root independently rechecked runtime after reviewer launch: `git status --short`,
`git diff --stat`, and `git diff --cached --stat` are empty. HEAD is f2512c1
and tree is1e8bb7b. The seven `M` lines from the batched initial inventory are
`git diff --name-status c350274..f2512c1` output, not working-tree status.
