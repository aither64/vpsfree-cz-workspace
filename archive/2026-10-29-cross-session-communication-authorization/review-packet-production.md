# Affected final review: production activity composition

Review is requested after all intended code/docs/tests are committed and quick
checks pass. Original independent report remains review-report.md (no findings,
all four lanes, base08f3dbb9..c43904a7). This is required final review of new C and
changed B native composition, not an advisory early review.

Requested user outcome remains one explicit approval in either exact session,
bidirectional deliberate messages, trusted registry context without local
reapproval, no peer-claim authority or wider access, exact incarnation,
revocation/lifecycle/recovery and held delivery semantics. Read full plan.md,
state.md and design.md including the production-composition addendum.

## Exact source/history

Only generic dev-workspace. Worktree:
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-29-cross-session-communication-authorization/dev-workspace`.
Base: `08f3dbb92bc8585929edee85a824d44dfb3b0846`.
Final head: `a6c0e10f4d0c828631a4bbf02da16fa3b6d556f5`. Fresh origin fetch leaves origin/master at base.
Worktree/index clean; full range diff --check passes.

```text
ed16c606b8b3a5ae1624e1f8dd5e7bcccf3cc387 communication: attach verified grant context to deliveries
99da3951e621d0424f8c7ae74b30662501a1ddef communication: clarify bidirectional runtime authorization
a6c0e10f4d0c828631a4bbf02da16fa3b6d556f5 communication: use fresh observer activity for delivery admission
```

```text
 docs/session-communication-upgrade.md              |  25 ++
 docs/session-communication.md                      |  30 +-
 .../session_communication_integration_test.go      | 261 +++++++++++++
 ...ession_communication_native_integration_test.go | 434 +++++++++++++++++++++
 portal/cmd/workspace-portal/team_mcp.go            |   2 +-
 portal/cmd/workspace-portal/team_mcp_test.go       |  21 +
 .../communication/authorization_context.go         |  44 +++
 .../communication/authorization_context_test.go    | 395 +++++++++++++++++++
 portal/internal/communication/service.go           |   9 +-
 portal/internal/web/activity.go                    |  11 +
 portal/internal/web/communication.go               |  27 +-
 portal/internal/web/communication_activity_test.go | 313 +++++++++++++++
 portal/internal/workspacecodex/lead_policy.go      |  15 +-
 portal/internal/workspacecodex/lead_policy_test.go |  23 ++
 14 files changed, 1599 insertions(+), 11 deletions(-)
```

Complete series is A runtime context/recovery tests; B policy/docs and production
command/native tests; C fresh activity web composition and focused tests. B's
native case is a regression requiring C's production wiring for active delivery.
All obsolete fixture iterations were folded into owning B, with no intermediate
fixup left. C retains one separate coherent production fix. Tree before/after
consolidation is exactly 7177a7a43218f4f91ad23d5be12430a1742a65d7; diff empty.
Range-diff maps A equal, B final fixture adaptation, C equal, fixup absorbed.
Detailed old/intermediate heads and red/green history: implementation-b.md.
No migrations, dependency/channel/input streams, pins or generated artifacts.
No feature release, deployment or external consumption; no integration approved.
Require explicit independent whole-series/consolidation/migration conclusions.

## New production behavior and evidence

Original full native run proved idle context/reverse reply but active remained
held before Send. B diagnosed absent real activity observation. Architect proved
production main's operational workspacecodex.Client lacks recorder; web owns a
separate ObserverOnly recorder/subscription client, but communicationService
passed the recorder-free operational client directly to Native.Ready.

C adds 37 production lines and removes one. A private web NativeClient adapter
overrides only activity reading. It uses the existing monitor observer under the
existing global/per-thread read gates, bypasses UI cached/stale/backoff success,
rejects stale/wrong-thread results, and delegates metadata/send/reconcile to the
original operational client. No recorder/global client/API/registry/schema or
scheduler change. Native.Ready/provider/runtime/socket/recovery/metadata checks
remain unchanged. No monitor means existing direct activity plus identity/stale
guard; no manufactured observation. Incomplete history alone adds no hold.

C failing-before actual communicationService test (0.099s): fresh working
observer plus poisoned recorder-free operational read resulted held/no send.
Focused green TestCommunication|TestActivity 2.133s; strengthened valid provider
reservation/exact-reason rerun0.261s. Tests cover operational delegation and
reconciliation, fresh/cache/backoff/error/wait/stale/mismatch states, existing
pre-activity holds and gate cancellation. Exact commands in implementation-c.md.

B native now uses real newCodexClientWithHistory, recorder-free operational
client, public portalweb.NewContext(ObserveActivity:true, RecoverSessions:true),
portal-owned observer and actual background communication worker. No manual
recorder/subscription/decorated Native/direct Dispatch. Public activity endpoint
confirms exact working native turn; stored native receipts establish start or
steer. Model developer context JSON is checked against the recorded grant and
separate from forged peer text; synthetic backend then emits reverse MCP reply.
One grant and retained settings are checked. Inspect actual constructor/worker,
provider isolation, generation guard and cleanup dependencies; constructor health
alone is not delivery proof. Private state is outside disposable workspace,
profile is an owned symlink, scope/socket/version explicit, provider catalog
absent, active recovery permits execution but automatic tmux restoration disabled.

Short constructor/health check1.415s, tagged compile0.050s, focused MCP/real-command
0.500s, gofmt/diff checks pass. Compilation/health are NOT native acceptance.
Required full native execution remains after this review. Prior failures are
preserved; known fixture MCP env/first-turn/activity/cleanup omissions corrected
using existing public contracts, not simulated success. Strict checked host
selection adapter still substitutes for unchanged Ruby wrapper, whose complete
packaged checks remain required.

## Risk, documentation and review scope

High risk: authorization/current activity admission and durable retry identity.
Same retained independent reviewer0, codex-lb Sol/xhigh/read_only, no fallback or
settings changes. Applicable affected lanes: general, architecture/repetition,
scope/proportionality, risk/compatibility. Read mandatory-change-review skill and
all four references again if no longer in context. Focus detailed re-review on C
and new production-native fixture; preserve original A/B conclusions where
unchanged while checking complete final history and integration of the delta.

Existing feature/upgrade guides remain accurate, source comments explain fresh
admission versus UI cache. No extra guide needed for fixing promised working
lead delivery; owner rationale in implementation-c.md. Lead final writing pass
already accepted original docs/policy/context; no later visible copy change.
Schema-1 saved options/envelopes stay exact; grant/current-state/limits unchanged.
Old compatible packages can read options but omit improved context/new wiring.

No broader authority or hostile-local-operator hardening is requested. No
cross-project expansion, incident-private access, deployments, merges or session
lifecycle actions. Do not run long tests or edit source; return report for lead
to persist (retained read-only role). No nested agents. Report concrete severities,
residual limits and whether longer native/packaged verification may begin.

Long native command is in implementation-b.md; exact pinned Codex0.165.0. Full
packaged Go/workspacecodex/Ruby checks and ordinary feature CI still pending,
including closure of the prior45s broad-package timeout. Ready/usable/deployed
must not be conflated. Original review report, followups and evidence stay intact.
