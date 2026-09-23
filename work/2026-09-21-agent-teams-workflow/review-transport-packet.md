# Final member-report transport review packet

## Scope and outcome

Initiative `2026-09-21-agent-teams-workflow` is tracked by `plan.md` and
`state.md` in this directory. The four worktrees are
`worktrees/2026-09-21-agent-teams-workflow/{codex-web,dev-workspace,vpsfree-dev-workspace,workspace}`
under `/home/aither/workspace/ai/vpsfree.cz`. Accept the change only if a
ready member can report to its own lead from a read-only or workspace-write
sandbox, cannot select another session or sender, and retains the tool after
reconnect. Team selection, add/remove/configure, transcript visibility,
fork/archive/revive, cluster providers, and tmux lead attachment must retain
their already-implemented behavior.

The deployed direct-thread teams create and assign independent member threads,
but a member's Codex shell sandbox cannot open the host transition lock or
shared portal socket. This committed follow-up gives a member one package-owned
stdio MCP action, `report_to_lead`, instead of expanding shell permissions.
It is a scoped member-to-lead transport; ordinary lead-to-member assignments,
CLI and portal controls, and tmux lead attachment remain unchanged.

Review the new committed deltas and final trees only. The earlier broad
four-lane review and pinned-binary follow-up are in `review-headless-result.md`
and `review-pinned-binary-result.md`; unchanged implementation need not be
rediscovered.

## Committed ranges

- `codex-web`: `0f59be164036..2a228e70de42`. A thread policy can configure
  one enabled MCP tool with explicit approval on start, fork, resume, and the
  internal pre-send resume. The pinned-binary two-turn test is opt-in and is
  reserved for post-review verification.
- Generic `dev-workspace`: `98fc2b2c99fc..04bb52a1f901`. Runtime binds the
  exact workspace/session/root/member/thread on each assignment; the helper
  exposes only `report_to_lead(message,message_id)`; the host command checks
  the current lead root under the session lock. Reports cross both CLI hops
  through stdin, not process arguments. The generic package pins the client
  and fresh Go vendor hash.
- `vpsfree-dev-workspace`: `a24bbee2bc84..08f576a8e8c4` pins the generic
  package and preserves the vpsAdmin and vpsAdminOS cluster providers.
- Workspace configuration: `100eca5b2760..7db87792ccbb` pins extension
  `08f576a8e8c4`, generic `04bb52a1f901`, and codex-web `2a228e70de42`
  through its lock file. The feature head is local pending final integration.

After review, codex-web `86aaa2e39062` and generic `b7883bee18fb` add
documentation-only corrections for the review findings. Downstream package
pins intentionally remain at the reviewed code heads above.

The commit split separates the shared Codex client policy (`2a228e7`),
generic runtime binding (`1529d96`), generic helper/host guard (`81417a4`),
generic dependency pin and vendor hash (`04bb52a`), and downstream package
pins. Tests and permanent behavior documentation accompany their owning
implementation. The binding and helper are independently reviewable
mechanisms, but both are required for delivery.

## Risk and compatibility

High-risk surfaces are cross-session isolation, stale member or recreated
session slug, retry deduplication, approval semantics for read-only members,
MCP tool availability after reconnect, report privacy, and package-bound
host authority. The helper takes its workspace, session, root, address, and
thread only from its launch arguments; tool input cannot select a sender,
recipient, or session. It checks the ready roster before invoking the
installed `dev-session`; the latter checks the lead root under its lock.
An uncertain delivery asks the member to retry the same message ID.

The shared client owns the `ThreadPolicy.MCPServer` interface; generic runtime
is its current consumer through the pinned Go module and flake input. The
generic package owns the MCP helper and CLI host guard. The vpsFree extension
consumes that package and supplies the two cluster providers; workspace
configuration consumes the extension. No other importer of the new client
field was found. The existing portal and CLI consume generic teamruntime for
assignments; the member's tool calls that same host path.

Rejected alternatives were broad shell access to the host transition lock and
shared portal socket, and a separate message broker. These increase member
authority or add a redundant runtime. Non-goals are direct member tmux panes,
member-to-member tool messaging, migration of the old virtual-team ledger,
and aitherdev rollback. The user chose forward-only deployment and permits
restarting idle sessions.

This forward-only aitherdev change adds no roster schema, database, or service
protocol migration. Existing idle sessions can restart on the new package;
their root threads remain. The first assignment to a ready member from the
earlier package binds the tool to that exact thread. The user explicitly does
not require aitherdev rollback. It does not change vpsAdminOS nodes or
production infrastructure protocols. The site presets retain GPT-6 Sol at
their role-specific efforts, with a fresh Luna/low utility for long
verification; no Astra is selected.

## Evidence and remaining checks

- Codex-web quick Go and protocol coverage checks passed after its commit.
- Generic focused Go suites for `cmd/workspace-portal` and
  `internal/teamruntime`, focused Ruby host/CLI tests, and no-build flake
  evaluation passed. The fake-hash build identified the new dependency hash
  `sha256-9OBydqLWyJUNin2ubEKRmKd669SSzwOGHWStdQi6Wqw=`.
- Extension and workspace no-build flake evaluations passed at those heads.
- Representative commands were `nix develop --command go test -mod=readonly
  ./cmd/workspace-portal ./internal/teamruntime -count=1` from generic
  `portal/`, `nix develop --command ruby -Itest
  test/dev_session/team_mcp_binding_test.rb` from generic root, and
  `nix flake check --no-build --show-trace` in each package worktree.
- Deliberately after review: opt-in pinned Codex binary MCP contract, full
  packaged check, live read-only and workspace-write member reports to the
  right lead, wrong-session and stale-member rejection, and aitherdev switch.

Use the mandatory review's general, architecture, scope, and risk lanes at
Sol/xhigh. Overall risk is High because the tool crosses a read-only member
to host mutation boundary and changes shared Codex-client and package
contracts. The permanent design and operator behavior are documented in
generic `docs/workspace-portal.md` and codex-web `docs/reference.md`;
per-rollout evidence and limitations stay in this initiative's `state.md`.
Report actionable findings by severity and location; include
residual verification gaps separately. Do not mutate files or run long tests.
