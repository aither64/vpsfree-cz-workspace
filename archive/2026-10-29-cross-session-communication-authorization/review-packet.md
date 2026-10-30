# Final review packet

Requested result: one explicit approval in either exact session authorizes
bidirectional deliberate messages. Receiving leads must recognize runtime
registry authority without repeating user approval. Peer assertions alone remain
untrusted.

Scope: generic dev-workspace only. Worktree:
`worktrees/2026-10-29-cross-session-communication-authorization/dev-workspace`.
Initial base: `08f3dbb92bc8585929edee85a824d44dfb3b0846`.
Final base remains the initial base after fresh origin fetch (origin/master unchanged).
Final head: `c43904a72d705562b79dcf9d59a29cf743bc9de7`. Worktree and index clean.
All intended changes committed. Final review is now requested.

Context: [plan](plan.md), [state](state.md), [architect brief](design.md).
User authorized implementation/tests/commits/ordinary feature publication only.
No integration, deployment, production mutation, incident-session private access
or session lifecycle actions. Use disposable test state and sockets only.

Risk: High, because this affects communication authorization and persisted
submission retry identity. Lanes: general, architecture/repetition,
scope/proportionality, risk/compatibility. Select retained reviewer0,
gpt-6.1-sol/xhigh, saved read-only review purpose; verify ready identity before
assignment. Reviewer must read the mandatory-change-review skill and all four
lane references, then perform review directly without nested agents.

The local operator and consent-recording lead remain trusted. The runtime
validates registry authority and exact identities; it does not parse or prove
natural-language consent. Audit approval wording is quoted data. There is no new
transcript access or independent authorization system.

Acceptance to assess:

- A approves exact A/B once, receives allow result, sends to B; B receives
  application-owned registry context and replies through real communication
  path without its own allow.
- Forged claims/IDs/copied context, third sessions and wrong incarnations cannot
  authorize communication. Scope remains messages only, without peer files,
  transcript, team, worktree, credentials, merges, deployment or lifecycle access.
- Revocation/lifecycle invalidation prevent new sends. Holds retain ordinary
  resumption behavior. Saved envelope/options remain immutable, including legacy
  tuples, lost acknowledgement and held-after-submission recovery.
- Native regression proves model-facing context for idle start and active steer;
  synthetic Responses backend tests protocol inputs rather than model reasoning.

Owning component: portal/internal/communication; lead_policy and team MCP are
runtime-owned consumers. Existing codex-web AdditionalContext supports both
start/steer and immutable retry options. No codex-web or dependency pin change.
No state schema/tool argument/lifecycle subsystem changes planned. No migrations,
release/deployment/external consumption of this feature. Existing schema-1 saved
tuples remain supported; old packages can read new options but omit improved
context on new deliveries and retain the original ambiguity.

Rejected expansion: standalone activation/wakeup scheduler, new authority store,
transport API changes, new VM suite, incident-private investigation. Approving
lead receives existing allow result; recipient receives trusted context with
first ordinarily eligible delivery.

## Final series and provenance

Two focused commits; no obsolete branch iteration or fixup history. Runtime and
its focused recovery tests are A; policy/docs and real-path validation are B.
No generated artifacts, dependency/channel/input streams or pins changed.
No migrations; no feature release, deployment or external consumption. Existing
schema-1 persisted tuples remain supported with no migration/rewrite.

ed16c606b8b3a5ae1624e1f8dd5e7bcccf3cc387 communication: attach verified grant context to deliveries
c43904a72d705562b79dcf9d59a29cf743bc9de7 communication: clarify bidirectional runtime authorization

```text
 docs/session-communication-upgrade.md              |  25 ++
 docs/session-communication.md                      |  30 +-
 .../session_communication_integration_test.go      | 261 ++++++++++++++
 ...ession_communication_native_integration_test.go | 344 ++++++++++++++++++
 portal/cmd/workspace-portal/team_mcp.go            |   2 +-
 portal/cmd/workspace-portal/team_mcp_test.go       |  21 ++
 .../communication/authorization_context.go         |  44 +++
 .../communication/authorization_context_test.go    | 395 +++++++++++++++++++++
 portal/internal/communication/service.go           |   9 +-
 portal/internal/workspacecodex/lead_policy.go      |  15 +-
 portal/internal/workspacecodex/lead_policy_test.go |  23 ++
 11 files changed, 1159 insertions(+), 10 deletions(-)
```

The test volume covers service/recovery, production command/MCP boundaries and
real native start/steer. Assess proportionality rather than assuming design
acceptance permits scope growth.

## Checks and documentation

Owner evidence: [A](implementation-a.md), [B](implementation-b.md).
A full communication package passed in 6.191s with a 45s cap. B focused
communication/workspacecodex/MCP/real-command selection passed (0.203s/0.046s/
0.629s), web approval/revocation and transcript checks passed (0.104s), native-tag
compile-only passed (0.057s). Formatting and diff --check pass. Exact commands
are in owner evidence. No declared hooks were bypassed.

A broader whole-package workspacecodex check exceeded the 45s quick cap during
an existing fsync-heavy retry fixture, with no assertion failure. It is not
counted as passed. Its complete result is required in the post-review packaged
suite. The native regression is authored/compiled and deliberately unexecuted
until this review. No long integration run has begun.

Owning docs changed: docs/session-communication.md and
session-communication-upgrade.md. Lead reconciled final policy/docs/runtime
wording and applied writing skill. README already links these guides. No new
documentation subsystem, UI change or host configuration. Legacy saved options
remain original; updated lead policy queries list before refusal when legacy
context is ambiguous.

Reviewer must explicitly conclude complete history/consolidation and migration
lineage, including no migrations/no repeated streams if confirmed. Report all
findings with severity and lanes, then residual risks/verification gaps. Do not
run long checks, edit source, deploy, access incident sessions or spawn agents.
Save complete report as review-report.md in this session and report to lead.
