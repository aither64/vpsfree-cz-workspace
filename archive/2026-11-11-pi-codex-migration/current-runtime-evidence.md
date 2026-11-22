# Current runtime coupling evidence (Package B)

Owner: implementer0. Bounded source investigation on 2026-11-11; first pass
started at 22:00:57 UTC. Purpose: establish what can retain the current portal
workings when replacing Codex, with provider switching as the primary motivation.
This is evidence for architect0, not an implementation or product redesign.

## Source identity and limits

Session identity was verified with `dev-session current`; both environment
identity values match `2026-11-11-pi-codex-migration` and
`/home/aither/workspace/ai/vpsfree.cz`. The same-session roster confirms the
assigned implementer/architect addresses and workspace-write access.

Sources below were read through canonical bare `origin/master` blobs, not
feature worktrees. Public GitHub commit lookups independently returned these
same default heads. Local bare `refs/heads/master` differ and were not used.

| Alias | Repository / exact source |
| --- | --- |
| D | [dev-workspace](https://github.com/aither64/dev-workspace/tree/6587c4c1cedabee95bcc52f4667e7d33e3a82859), `6587c4c1cedabee95bcc52f4667e7d33e3a82859` |
| C | [codex-web](https://github.com/aither64/codex-web/tree/dd90fb4308ba85617ee2a4267cc835aa9a4f11ce), `dd90fb4308ba85617ee2a4267cc835aa9a4f11ce` |
| L | [selected llm-agents](https://github.com/numtide/llm-agents.nix/tree/91ff550fe42d4dd51dcf8b6bad87a0134fe7f314), `91ff550fe42d4dd51dcf8b6bad87a0134fe7f314` |
| Native source | L `packages/codex/hashes.json` selects `0.165.0`; public `rust-v0.165.0` resolves to `360319d8dee62d87e2d59fc0c21805d79519cfed` |

D `flake.nix` / `flake.lock` select exactly C and L. D/C `AGENTS.md`, README,
relevant reference/package/provider/reporting guides and update procedures were
read. No old-session contents, refs or worktrees were inspected. No binaries,
credentials, live native state, builds, tests, services or deployments were
examined or changed. These findings describe sources and documented contracts;
they do not prove which executable is currently deployed or its live behavior.

## Decisive provider contract and patch distinction

The user reports a provider-switch-specific Codex patch as the replacement
motivation. The selected default source establishes the present switching
workaround, but does **not** establish the identity or disposition of that
reported patch. No conclusion about the user's live blocker follows from an
absence in these defaults. Further patch archaeology was outside this package.

D `docs/codex-providers.md`, `libexec/workspace-codex-providers.rb` and
`portal/internal/workspacecodex/client.go` establish:

- Provider selection is **per development session**, inherited from a workspace
  default or explicitly pinned. A switch covers the lead and every retained
  member, including idle members. There is no independent member-provider picker
  in this documented contract. Other sessions keep working.
- Loaded Codex threads cannot change provider. Native unsubscribe has a
  30-minute grace period, so the worker uses native **archive/unarchive** to
  close/reopen selected histories on the same daemon. This is distinct from
  archiving the development session. Temporary native subagents stop; retained
  leads/members reopen, keeping IDs, queues, goals, model/effort, permission and
  instruction policy. Interrupted work gets a durable continuation. Native goal
  activation is not replayed because it could duplicate completed work.
- The worker journals close, reopen, verify and continuation phases, fences the
  selected scope and recovers the same accepted operation. Partial failure can
  require forward recovery; ordinary provider selection is not a stateless API
  configuration change. The guide says it uses the selected upstream binary
  without an additional provider-switching patch; this is a **source statement**,
  not evidence disproving the reported deployed patch/blocker.
- Subscription allowance comes from the native Codex account. Custom pools use
  trusted catalog endpoints ending in `/v1`, private token-file authentication,
  `/v1/usage` metrics, `/v1/models` preflight, and native Responses inference.
  Browser input supplies neither endpoints nor executable paths. Quotas are
  previews, not switch admission; target model availability is checked.
- Per-provider model catalogs drive both picker and validation. Model-only
  private App Servers are needed because ordinary native discovery uses the
  daemon's configured provider. New-session/fork/plan selection belongs to the
  destination; accepted creation receipts preserve its exact choice.

The separately verified packaging patch is L
[`packages/codex/daemon-nix-store.patch`](https://github.com/numtide/llm-agents.nix/blob/91ff550fe42d4dd51dcf8b6bad87a0134fe7f314/packages/codex/daemon-nix-store.patch).
It selects the immutable Nix runtime instead of copying roughly 550 MB and
letting upstream update it, repairs a stale store selection when no daemon runs,
and attempts a GC root. It does not implement provider switching. L
`packages/codex/package.nix` also raises a Rust recursion limit, changes build
memory settings and conditionally applies `webpki-bump.patch` only below 0.164
(inactive for selected 0.165). D `nix/codex-package.nix` adds a complete manifest,
materialized helpers/resources and closure retention **without changing Rust**.
Do not conflate any of these with the reported provider patch.

## Keep the portal workings: inventory and adaptation boundary

“Unchanged” below means a plausible UX/domain boundary to preserve, not a claim
that the existing implementation has no Codex references. Adaptation judgments
are engineering inference grounded in the cited source contracts. Pi capability
and feasibility evidence belongs to implementer1; architect0 owns the choice.

| Area | What can stay as the user experiences it | Internal adaptation / runtime dependency | Representative exact-head paths |
| --- | --- | --- | --- |
| Portal shell and access | Existing layout/navigation, workspace identity, host TLS/basic auth, session URLs and access rules | Preserve trusted resolver and exact-origin authorization; replace runtime-specific composition | D `nix/host-module.nix`, `portal/internal/web/server.go`, `docs/workspace-portal.md`; C `conversation/handler.go:35` |
| Files, repositories, clusters, operations | Files and source links, repository comparison/review UI, cluster/service controls, machine/merge coordination | Largely independent domain systems; reconnect attention/status and agent notices to replacement runtime | D `portal/internal/repository/`, `portal/internal/cluster/`, `portal/internal/web/resources.go`, `libexec/workspace-coordination*.rb` |
| Conversation UI | Existing composer, transcript, paging, attachments, model/effort controls, questions, approvals, interruption | HTTP capability handler already separates opaque app ID from trusted runtime identity, but its Go types and browser item vocabulary are Codex-specific. Build a compatible projection/adapter rather than presume a socket swap | C `conversation/handler.go:59`, `conversation/assets/{conversation,sync,questions,uploads}.js`; D `portal/internal/web/{server,uploads}.go`, `static/app.js` |
| Transport and events | Current browser update and reconnect behavior | C opens WebSocket JSON-RPC over a Unix socket; initialize, subscriptions, pending request generation/authority, native events and reconnect/resume policy are Codex contracts | C `codex/client.go:1009`, `codex/{observer,observer_events,lifecycle,prompt_response}.go` |
| Thread/turn history | Existing session/member history, archived read views, forks, bounded paging | Native projects/threads/turns/queues own conversation state. Client combines native reads with local rollout-file metadata, cursor/lineage proof and item timestamps. Portal side records contain settings/counters, not transcript bodies | C `codex/{thread_page,page_metadata,timestamps,history_reader,turn_context}.go`; D `portal/internal/web/thread_records.go`, `docs/workspace-portal.md:454` |
| Durable delivery and queues | Stable retry behavior, queue order, no accidental repeated commands after lost acknowledgement | Reuse the contract, not an assumed native equivalent: reserve exact text digest/action/options; retain uncertain writes; native client IDs correlate **without deduplication**. SQLite WAL/full-sync records and native history establish outcomes. Queue add can execute immediately on loaded threads | C `docs/submission-storage.md`, `codex/{send_delivery,send_discovery,submission_database,submission_migration}.go`, `client.go:4836`; D `portal/internal/web/plan_delivery.go` |
| Plan/Default and implement plan | Existing Plan/Default switch, same-session or new-session implementation, stale-plan rejection | Native collaboration modes and plan item kinds must be reproduced. Acceptance binds completed plan turn ID + SHA-256 and stable message ID; delivery recovery runs before freshness checks; switching mode must not duplicate dispatch | D `portal/internal/web/server.go:2632`, `server.go:2695`, `creation.go:931`, `plan_delivery.go`; C `codex/client.go:4035`, `codex/plan_turn_test.go` |
| Teams and reviewers | Same retained roster, role/model/effort/instructions, compact addresses, independent reviewer assignment and member transcripts | Team policy, ownership and roster records are reusable; execution currently creates independent App Server threads, not native child agents. Busy assignment steers; idle assignment starts. Retained reviewer settings must survive. Native temporary agents are a separate concept | D `portal/internal/{agentteams,teamruntime}/`, `nix/agent-teams.nix`, `docs/workspace-portal.md:1442` |
| Reports and communication | `report_to_lead`, stable-ID retries, approved lead-to-lead communication and holds | Daemon-start MCP is required because late insertion is ignored by materialized warm threads. Actual native caller-thread metadata resolves the current roster/lead under locks; tool arguments cannot choose sender identity. Replacement needs equivalent unforgeable host binding | D `portal/cmd/workspace-portal/team_mcp.go`, `portal/internal/teamruntime/reporting.go`, `portal/internal/communication/{native,authorization_context,store}.go`, `docs/team-reporting-upgrade.md` |
| Utility watchers and progress | Fresh watcher policy, durable results, existing activity/progress view and reviewer workflow | Native project/thread creation, exact utility launch receipt, caller identity, turn terminal proof, native capacity and all yielded work are part of completion. Idle alone proves neither command completion nor a durable report | D `portal/internal/monitoroperation/{launch,native,delivery,authority}.go`, `portal/cmd/workspace-portal/monitor_mcp.go`, `portal/internal/progressobserver/`; C `codex/{activity,turn_state,capacity}.go` |
| Provider/account UX | Preserve session/default selection, preview, model validation and progress/recovery semantics | Provider mechanics, auth discovery, model capabilities and metrics adapters change. Subscription quota/reset data is Codex account API, whereas custom-pool metrics are already a separate source | D `docs/codex-providers.md`, `portal/internal/codexproviders/`, `portal/internal/web/{provider_models,provider_watches}.go`; C `codex/reset_credit_test.go` |
| Lifecycle and software transitions | Existing start/stop/recovery/creation/archive/revive semantics and protections | Authority includes Codex thread/socket/version plus tmux identity; recovery binds socket epoch. Journals, retirement proof, creation/fork receipts, private submission state and forward-only package fences must coexist with old runtime histories | D `portal/internal/session/{authority,recovery,runtime-contract.json}`, `libexec/{dev-session,workspace-host,workspace-archive-recovery.rb}`, `portal/internal/workspacecodex/{archive_proof,recovery,transition}.go` |

Potential visible differences need evidence before any commitment: exact model
and thinking-effort labels; native tool/result presentation; question/approval
behavior; temporary-agent interruption; history/fork boundaries; account limits
and credit-reset availability; and brief switching/recovery status. None implies
a portal redesign. Provider selection with retained history is the essential
replacement capability; exact subscription reset parity is a separate
prioritization decision. This package does not silently drop it.

## Why updates cost more than changing a version

1. **Several compatibility planes move together.** D's update procedure requires
   an exact upstream package plus matching C source, flake pin, Go pseudo-version
   and checksum, vendor hash and immutable model metadata. C validates requests
   against schemas from the exact packaged binary, not a version string.
2. **Native behavior changed an isolation guarantee.** C `docs/reference.md:1139`
   and `codex/ephemeral.go` retain strict tool isolation for 0.163 but use a
   separate prompted naming contract for raw 0.164/0.165; native tools can remain
   available. Static Luna catalog bytes/origin, advertised effort, bounded private
   daemon and teardown need exact-binary checks. D naming pins 0.165/Luna/high.
3. **Persistent state prevents simple rollback.** C's schema-1 SQLite migration
   publishes schema-4 JSON fences; older clients refuse them. Restoring old JSON
   loses newer receipts and can duplicate delivery. Native state upgrade tests
   separately probe old-reader behavior without claiming downgrade-write safety.
   D `session/runtime-contract.json` additionally gates provider, team, monitor,
   lifecycle, maintenance, authority and communication state compatibility.
4. **App and actual native daemon may differ.** Native selection/copies/store
   references, helpers and GC retention require independent identity evidence.
   Same-native application updates can remain live; changed native invocation
   requires the documented quiescence/maintenance/recovery contract.
5. **Recovery depends on native details.** Recent default history includes exact
   send discovery, observer streams, wrapped capacity failures and delivery
   admission/cancellation fixes. These are correctness obligations when changing
   runtimes, not optional UI polish.

Representative default-history evidence: D `7d116358` (0.165/state isolation,
22 files, 231 additions/101 deletions), `87228048` (prompted 0.164 naming),
`c96503ea` (delivery versus retry proof), `32a5e31b` (bounded managed discovery);
C `ba8dfdd` (0.165 naming and native state upgrade), `ccd2ce5` (raw 0.164 naming),
`643898a` (utility retries), `a9086b0` (durable admission recovery), and `dd90fb4`
(bounded exact send discovery). These establish changed surfaces, not measured
historical engineer time or proof that every change was caused by an upgrade.

## Rough surface and remaining questions

At D's exact head, raw tree counts are 225 files under `portal/internal/web/`,
37 under `workspacecodex/`, 12 under `teamruntime/`, 31 under `session/`, 14 under
`monitoroperation/`, 7 under `communication/` and 6 under `codexproviders/`.
C has 93 files under `codex/` and 25 under `conversation/`. Counts include tests
and assets and are **not** an edit estimate. Representative large integration
points are D `libexec/dev-session` (10,825 lines), `workspace-host` (4,068),
web `server.go` (4,251), `static/app.js` (7,214); C `codex/client.go` (5,981).
Reuse is strongest at portal/domain boundaries, with substantial runtime seams
inside those files. An exhaustive UI-file enumeration would not improve this
first-pass decision.

Unresolved: reported provider-patch provenance; deployed binary/daemon identity;
replacement equivalence for durable dispatch, native caller identity, loaded
switching with history/thinking/custom endpoints, permissions, pending tools,
retained queues/goals and history migration; and which account/reset capabilities
are essential parity. Implementer1 supplies Pi evidence and architect0 resolves
architecture. No live acceptance, migration or rollback proof is claimed.

Related evidence from implementer1:
[Pi capabilities](pi-capabilities-evidence.md), pinned to
`a22b888a58fe55b668cc45b80749ec88d4eb4ddc`, reports native same-conversation
`AgentSession.setModel()` with authentication checking, a persisted model-change
entry and model-dependent thinking adjustment. Cross-provider handoff retains
text/tool history but omits the previous model's thinking from the handoff.
Custom endpoint/provider definitions exist. Exact private Responses gateway,
token-file, dynamic catalog and quota/reset compatibility remain unverified;
retain the host-owned catalog/account UX boundary. These are the peer package's
source findings, not new live verification by Package B.

Package checks: source paths and public revisions inspected; no application
changes, commits, branches, builds, live checks or integration. Investigation
evidence alone does not require automatic independent change review. Lead owns
state/manifest linkage and final synthesis.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-11-pi-codex-migration/
