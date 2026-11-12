# Writable Codex/Pi coexistence decision (Package G)

Owner: architect2. Investigation/design only, 2026-11-11. Only this file is
owned; architect0 synthesizes `design.md`, and the lead owns acceptance and
tracking. No previous package was executing. Session/current/environment and
the same-session roster were verified; required workspace procedures, D/C
repository instructions and the documentation skill were read. No application
edit, prototype, build, model call, migration or lifecycle operation occurred.

**Recommendation: add Pi alongside Codex, then retire Codex only when its
remaining execution and recovery dependencies have supported successors.**
This is simpler for preserving the current portal and existing working
sessions than direct replacement. It defers conversion of native execution
state rather than pretending transcript import solves it. Existing Codex
sessions retain ordinary writing, tools, queues, goals, teams and recovery.
This is a proposed transition, not authorization or a deployed topology.

The tradeoff is explicit: existing Codex remains workspace-shared during this
option and therefore outside the replacement's per-development-session process
accounting guarantee. New Pi sessions put their lead, retained workers and tool
descendants in one session cgroup and mount namespace, with no agent process
shared across development sessions. Per-session Codex rehosting is separate,
unproven work and was not investigated. This is not a user-approved exception.

## Decision and concrete routes

| Route | What remains usable / preserved | Cost and limitation | Decision |
| --- | --- | --- | --- |
| Unchanged legacy Codex, new Pi sessions | Old portal sessions continue on their original Codex authority, history and receipts; new Pi sessions use the same portal with Pi capabilities | Two pinned backends, compatibility tests and operating paths; shared legacy accounting remains | Smallest safe first phase |
| Pi continuation linked to original history | New Pi conversation identity linked to an exact original conversation/member and history boundary; old history remains attributable and original Codex path remains writable | Converted context is a derivative, not native resumption; avoid simultaneous writers to the same development resources | Optional next phase after lineage and admission contracts |
| Migrate the entire development session | Same slug/URL, tracking, worktrees, branches, exact heads, repository obligations, services/claims and retained roster policy; new Pi execution identities | Journaled authority transfer for lead and every member, explicit queues/goals/receipts mapping, tool/operation reconciliation; no demonstrated lossless converter | Later, separately specified migration; not needed for initial Pi adoption |
| New development session from selected context | Original remains fully workable; new slug has its own authority/resources and a history link | New worktrees/branches and explicit resource allocation; copying a transcript does not transfer ownership, reservations or completion obligations | Simplest independent Pi continuation, but does not migrate the original initiative |
| Direct replacement of all Codex execution | One eventual backend and immediate uniform isolation are possible targets | Must first solve all native-state migration, caller identity, recovery and old-session writability; keeping old sessions only as text violates scope | Reject as first step on current evidence |

For a continuation inside the **same** development session, preserve the
development-session identity and use a new backend/conversation identity with
an immutable source link. Select one active execution authority per member;
switching back must reconcile Pi effects and current files before Codex resumes.
The retained Codex conversation must remain activatable, not permanently
read-only. A link alone grants neither a second writer nor a second roster.
For a **new** development session, keep both usable with separate resources;
do not assign the old worktree, claims or completion receipts to it implicitly.

## Minimum actual seams and proposed compatibility surface

Fixed sources: D = dev-workspace `6587c4c1cedabee95bcc52f4667e7d33e3a82859`;
C = codex-web `dd90fb4308ba85617ee2a4267cc835aa9a4f11ce`;
P = Pi `a22b888a58fe55b668cc45b80749ec88d4eb4ddc`;
N = selected Codex 0.165.0 source
`360319d8dee62d87e2d59fc0c21805d79519cfed`. These describe fixed source,
not deployed-version equivalence. Existing inventories remain in
[current runtime](current-runtime-evidence.md), [Pi capabilities](pi-capabilities-evidence.md)
and [resource evidence](resource-evidence.md).

| Observed seam | Minimum change / invariant for coexistence |
| --- | --- |
| C [`conversation/handler.go:44–147`][target] resolves opaque app IDs to trusted client/thread/directory, capabilities and mutation lock; its interface and transcript/receipt types are Codex-specific | Preserve HTTP/browser workflows and trusted resolution; generalize just the operations the portal uses. Backend capabilities are separate from authorization. No socket/native ID/cwd supplied by browser; no full Codex wire emulation |
| D [`web/server.go:3877–4123`][routing] parses slug/member, takes transition/runtime locks, checks current profile and lifecycle, selects `s.config.Codex`, verifies retained member, returns capability-scoped target | Select backend from retained trusted state on every path, including member, retry, cold activation and events; preserve lock/order and profile rechecks. Backend selection is not provider selection |
| D [`session/authority.go:21–32,193–249,299–310`][authority] schema 1 rejects unknown fields; binds workspace/slug/tmux identity and all-or-none Codex thread/socket/client-version; live tmux must agree | Version the authority contract and migration deliberately. Proposed identity is workspace + development-session slug + member address + backend kind + native conversation ID + authority epoch + exact package/protocol contract; don't overload `codex_thread_id` with Pi IDs |
| D [`session/recovery.go:21–38,237–285`][recovery] grants execution only for exact socket generation and retained thread; [`runtime-contract.json`][contract] fences authorities, providers, teams, monitors, submissions and lifecycle | Backend-specific execution epoch and permission must survive restart; old journals/receipts remain with their original adapter. Unknown backend/schema/version fails closed. Old binaries must not write Pi state; retain forward recovery because package rollback is already forward-only in D README |
| C [`docs/submission-storage.md:16–38,82–112`][receipts] reserves exact digest/action/options; native IDs correlate without deduplication; uncertainty persists; SQLite v1 has schema-4 predecessor fences | Namespace receipts/history cursors/turn IDs by backend and authority, not just a reused string ID. Never retry an uncertain Codex effect through Pi. Reconcile using original backend; compatible package recovery must retain database/WAL/fences |
| D [`teamruntime/reporting.go:20–62`][reporting] derives actual reporter from native thread and exact active roster/root; side records contain settings/counters, never messages ([`thread_records.go:13–17`][records]) | Keep roster addresses/model/effort/instructions/access; map execution IDs explicitly. Host-bound tool identity must include backend and current member authority. Model arguments and copied transcript headers cannot establish caller identity |

The narrow interface therefore needs create/load/fork, models/settings,
history/page/events, send/steer/queue/cancel and durable outcome lookup,
pending questions/approvals, settled activity and trusted host-tool callbacks.
Lifecycle/team/monitor domain policy stays in dev-workspace; each backend
implements the required execution proofs. Renaming only the client socket is
insufficient. Keep original Codex receipts and supported recovery readers
available while corresponding histories or operations can return.

## Import feasibility: history is not execution state

Source-supported **Pi import exists**, but it imports **Pi JSONL**:
[`AgentSessionRuntime.importFromJsonl()`][import] copies the file, calls
`SessionManager.open`, then replaces the runtime and rebinds services.
[`loadEntriesFromFile()`][load] requires a first `type: "session"` header
with an ID; it is not a Codex decoder. Pi's [v3 format][format] uses
entry `id`/`parentId`, message/model/thinking/compaction/custom entries.
[`appendMessage()`][append] supports programmatic converted messages but
generates entry IDs/timestamps; preserve source identities separately.
`parentSession` is Pi file lineage, not portal authorization or a portable
cross-backend migration receipt. The documented SDK points to these APIs;
no Codex converter was found in this inspected import path.

| Source material | Feasible preservation / remaining gap |
| --- | --- |
| Completed user/assistant text and tool output | Transform into Pi messages or a clearly marked context summary; retain original exact source and attachments for display. Tool call/result pairing, types, unsupported media, compaction and provider reasoning require explicit mapping. Source permits a converter; no round-trip/lossless proof was run |
| Native turn/item history and lineage | N [`thread_history_migrations/0001`][history] stores thread/turn/item IDs, status/errors, ordinals and JSON; subsequent migrations add replay positions/timing. N [`SessionMeta`][native-meta] distinguishes session/thread/fork boundary and cwd. Preserve these as provenance; Pi's tree is a different schema |
| Native pending queue | N [`queue_migrations/0001`][queue] stores payload JSON, per-thread order and timestamps; `0002` adds change revisions. This is executable pending work, not transcript text. Needs exact admission/order/disposition mapping; do not copy and replay by default |
| Native goals | N [`goals_migrations/0001`][goals] stores objective/status/budget/usage/time, and `0002` stores continuation deferral. Recording the objective in context does not transfer scheduler state or remaining budget; automatic continuation needs an explicit equivalent contract |
| In-flight tools, approvals, yielded commands and native temporary agents | Historical output does not resume an OS process, pending tool response or authority. Settle/cancel through the original owner when separately authorized; unknown effects block transfer. No live-process migration demonstrated |
| Retained teams, utilities and operations | These are portal-owned members/settings plus native identities, durable delivery and launch/recovery proofs. Recreate execution with explicit old/new mapping while preserving policy and resource ownership; Pi's subagent example is not that contract |

Consequently **lossless historical text retention is plausible; lossless native
Codex-to-Pi execution import is not established and should not be promised**.
Even a byte-preserved original transcript does not imply identical model
context or resumed tools. Pi may omit prior-provider reasoning during handoff;
unknown item types and provider metadata require fixtures. No other sessions'
contents, rosters or transcripts were inspected to estimate actual migration
coverage. Codex state/version history, older Pi readers and downgrade safety
remain unverified; never rewrite originals to try an import.

## UI, maintenance and retirement

Keep the portal shell, Files, repositories, operations, composer and team views.
Expose backend identity and accurate capabilities where meaningful. Legacy
Codex keeps its present controls. Pi requires mapped item rendering,
thinking/model choices, planning policy, tool questions, queue/goals, quotas and
retry behavior before claiming parity. Unsupported controls need an explicit
unavailable state; silently dropping queue/goals/teams is not preservation.
Pi TUI is not an established attachment client for a portal-owned SDK runtime.

Dual backend costs include two package/protocol pins, state readers and upgrade
matrices; restart/delivery/cancel/provider tests for both; backend-aware
creation/authority/lifecycle/team/monitor paths; separate auth/catalog adapters;
and operator diagnosis. Existing Codex memory/disk/recovery obligations remain
while Pi adds workers; no saving estimate follows. Bound cost by keeping the
legacy adapter stable and implementing a small shared portal contract. Reused
extensions still need exact-source trust and maintenance checks; no third-party
extension or new substrate was selected here.

Retirement requires no remaining session that needs Codex execution, no pending
or uncertain native/portal operation requiring it, supported replacements for
retained teams/goals/queues/terminal access, and tested recovery of retained
archives/backups/restores that could reintroduce Codex. History may remain in
an attributable reader, but a reader alone cannot satisfy any still-writable
session. A default switch or completion of new Pi work proves none of these.
Stopping/removing Codex or closing sessions needs separately authorized action;
this recommendation performs none.

## Minimal phases and acceptance

1. Introduce versioned backend routing/authority and keep all existing sessions
   on writable Codex. Freeze the exact compatibility inputs. Quick checks:
   wrong backend/member/epoch rejection, capability enforcement, unchanged
   legacy resolution and unsupported-schema fencing.
2. Enable opt-in **new** Pi sessions with per-development-session containment.
   Before default selection, prove restart/reconnect, exact retry without
   duplicate effects, pending queue/goals policy, retained-team reporting,
   tool cancellation and provider switching against representative fixtures.
   Test existing Codex writes concurrently; do not restart it as a fixture.
3. Offer explicit derived continuations, initially into independent development
   sessions; add same-session transfer only after authority and resource
   reconciliation is implemented. Preserve original history and record exact
   source boundary, transformation version and omissions. Fault-inject transfer
   and recovery before considering whole-development-session migration.
4. Change the new-session default after parity acceptance. Retire Codex only
   after the dependency conditions above are proved; otherwise keep it usable.

These are future checks, not executed tests or released implementation packages.
The first-pass research stopped at the decisive routing/import/state seams;
no repeated full inventory, rehosting research or ecosystem search was needed.
Source links and the owned-file diff were checked. Lead acceptance and
architect0 synthesis are next. Routine evidence does not trigger automatic
independent change review.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-11-pi-codex-migration/>

[target]: https://github.com/aither64/codex-web/blob/dd90fb4308ba85617ee2a4267cc835aa9a4f11ce/conversation/handler.go#L44
[routing]: https://github.com/aither64/dev-workspace/blob/6587c4c1cedabee95bcc52f4667e7d33e3a82859/portal/internal/web/server.go#L3877
[authority]: https://github.com/aither64/dev-workspace/blob/6587c4c1cedabee95bcc52f4667e7d33e3a82859/portal/internal/session/authority.go#L21
[recovery]: https://github.com/aither64/dev-workspace/blob/6587c4c1cedabee95bcc52f4667e7d33e3a82859/portal/internal/session/recovery.go#L21
[contract]: https://github.com/aither64/dev-workspace/blob/6587c4c1cedabee95bcc52f4667e7d33e3a82859/portal/internal/session/runtime-contract.json
[receipts]: https://github.com/aither64/codex-web/blob/dd90fb4308ba85617ee2a4267cc835aa9a4f11ce/docs/submission-storage.md#L16
[reporting]: https://github.com/aither64/dev-workspace/blob/6587c4c1cedabee95bcc52f4667e7d33e3a82859/portal/internal/teamruntime/reporting.go#L20
[records]: https://github.com/aither64/dev-workspace/blob/6587c4c1cedabee95bcc52f4667e7d33e3a82859/portal/internal/web/thread_records.go#L13
[import]: https://github.com/earendil-works/pi/blob/a22b888a58fe55b668cc45b80749ec88d4eb4ddc/packages/coding-agent/src/core/agent-session-runtime.ts#L359
[load]: https://github.com/earendil-works/pi/blob/a22b888a58fe55b668cc45b80749ec88d4eb4ddc/packages/coding-agent/src/core/session-manager.ts#L628
[format]: https://github.com/earendil-works/pi/blob/a22b888a58fe55b668cc45b80749ec88d4eb4ddc/packages/coding-agent/docs/session-format.md
[append]: https://github.com/earendil-works/pi/blob/a22b888a58fe55b668cc45b80749ec88d4eb4ddc/packages/coding-agent/src/core/session-manager.ts#L1222
[history]: https://github.com/openai/codex/blob/360319d8dee62d87e2d59fc0c21805d79519cfed/codex-rs/state/thread_history_migrations/0001_thread_history.sql
[native-meta]: https://github.com/openai/codex/blob/360319d8dee62d87e2d59fc0c21805d79519cfed/codex-rs/protocol/src/protocol.rs#L3278
[queue]: https://github.com/openai/codex/blob/360319d8dee62d87e2d59fc0c21805d79519cfed/codex-rs/state/queue_migrations/0001_queued_items.sql
[goals]: https://github.com/openai/codex/blob/360319d8dee62d87e2d59fc0c21805d79519cfed/codex-rs/state/goals_migrations/0001_thread_goals.sql
