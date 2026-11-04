# Assignment and report transport findings

Read-only package A, implementer0, 2026-10-31. Advice for architect0 and lead;
this is investigation evidence, not an implementation or accepted design.

## Scope and revision

- `dev-session current` returned `2026-10-31-team-workload-parallelization`.
  Both identity environment values matched the bound slug and workspace.
- Source: canonical `repos/dev-workspace.git`, commit
  `6f54d0c7fdb974705c120b3c1ef5372f5897d544`, selected by the architect as the
  workspace flake pin. Earlier discovery at bare `master`
  `52dcd471186ef874c5c93f4133744195d4815454` was superseded; all line references
  below name the pinned commit.
- Installed CLI resolved to
  `/nix/store/413w4bai6br4c2vq08gx9diq55iasvqk-dev-workspace-0.2.0/bin/dev-session`.
  This identifies the selected executable, not its exact source revision or
  the running daemon generation. Neither was independently proven here.
- Inspected source through canonical Git objects only. No peer worktrees,
  roster records, transcripts or files were read. No fetch/push, source edits,
  runtime tests, team reconfiguration or lifecycle operations.

## Existing capability and its limits

| Topic | Current behavior and evidence at the pinned commit |
| --- | --- |
| `ready` | Retained member creation state. Creation writes `ready` after the thread is resumed/named (`portal/internal/teamruntime/runtime.go:1484-1494`). Allowed roster states are `creating`, `ready`, `archived`, `removed` (`:534-541`). It does **not** establish idle execution or spare package capacity. |
| Busy delivery | A busy member receives a steer of its current turn (`docs/workspace-portal.md:1403-1409,1457-1468`). `Assign` validates a ready recipient and calls `SendWithOptions`; it has no package-level idle gate or enqueue selector (`runtime.go:2375-2428`). |
| Native queue | A separate input-delivery facility. Docs distinguish Send/Steer from Queue next and do not promise combined order across steers, queued turns and clients (`docs/workspace-portal.md:518-523`). Cold recovery durably queues before activation and can return `QueuedSubmissionID` (`portal/internal/workspacecodex/recovery.go:34-35,67-114`). A queue receipt is not task completion. |
| Peer coordination | Already supported through `team assign --from ACTUAL_ADDRESS --to PEER --message-id ID` within the session (`docs/workspace-portal.md:1457-1468`). CLI checks the member's own session and sender address (`libexec/dev-session:1872-1879`); service resolves sender and target against the selected roster (`runtime.go:2338-2376`). Saved model/effort are defaults (`:2405-2409`). |
| Lead reporting | `report_to_lead` accepts only message and stable ID; native caller metadata resolves a current unique ready member. Host delivery revalidates caller and lead under locks. Completed turns are **not automatically forwarded** (`docs/workspace-portal.md:1630-1646`; `runtime.go:2343-2350`; `portal/cmd/workspace-portal/team_mcp.go:146-169,300-320`). |
| Retry identity | Stable message ID is required (`runtime.go:2326-2327`). Accepted option compaction retains request digests and receipts; same-ID retries must preserve original text/options and package generation (`docs/workspace-portal.md:1605-1617`; `runtime.go:2422-2428`). |
| Delivery concurrency | CLI holds the slug lock around assignment (`libexec/dev-session:1885-1897`). `Assign` also holds one per-session operation lock through App Server delivery (`runtime.go:641-654,2329-2335`). This serializes submission critical sections, not subsequent model execution. Existing regression checks assert assignment/removal serialization (`portal/internal/teamruntime/runtime_test.go:1953-1988`) and report identity revalidation after lock acquisition (`reporting_test.go:97-132`). These checks were read, not run. |
| Status visibility | `team list` returns roster/presets/access before client construction (`portal/cmd/workspace-portal/main.go:603-633`). Browser team statistics separately join roster state and activity snapshots (`portal/internal/web/team_stats.go:14-17,47-77`). Browser activity is approximate/stale-aware and explicitly is not a dependency or wake-up promise (`docs/workspace-portal.md:1428-1435`). |

There is no task/package scheduler in the inspected roster and assignment path:
`Member` records identity, retained settings and lifecycle fields, with no task
ID, owner queue, dependency graph, capacity reservation or completion state
(`runtime.go:92-110`). An assignment carries a text envelope, recipient and
submission ID (`:2418-2428`). Delivery receipts establish submission acceptance;
the lead still assesses completed work (`docs/dev-sessions.md:375-382`). This is
a scoped conclusion about these paths, not a survey of every subsystem.

## Shortest useful improvements

1. **Use existing transport now.** Put explicit peer coordination permission,
   addresses, package boundaries and report destinations in the lead's bounded
   assignment. Let architect and implementers resolve technical questions
   directly, then report acceptance-relevant results to lead. Preserve lead
   ownership of scope, approvals and overlapping edits/Git operations. No new
   bus or roster change is needed.
2. **Clarify readiness and assignment intent.** Document `ready` as initialized;
   distinguish idle execution from available capacity. Treat a busy-target send
   as steering the existing package. If independent queued work is wanted,
   specify a new queue mode explicitly rather than silently changing `Assign`.
3. **Keep package scheduling explicit first.** A small lead-owned package table
   (owner, dependencies, acceptance, status, blockers, next report) can reduce
   repeated routing without a persistent runtime scheduler. Native activity
   alone cannot prove that a package is finished or dependencies are satisfied.
4. **Only add scheduler state if justified.** A future task ledger or native MCP
   peer-message tool would be new capability. It needs caller/session binding,
   idempotent acceptance, explicit steer-versus-queue semantics, restart recovery
   and completion acknowledgments. Do not weaken identity revalidation or
   lifecycle locks merely to make message sends concurrent.

## Observed delivery and limitations

Two authorized technical messages from implementer0 to architect0 returned
`steered: true`, using IDs `9a1e6403-593e-46e3-8cb6-88daa0825ce0` and
`1aabce46-fbe0-4415-9811-d3b46c735520`. This is direct evidence of installed peer
submission acceptance, not proof that the architect read/accepted the content.
The preliminary lead report `70f7ab14-394c-4c88-a758-2ad1df578d9a` also received a
steered receipt. No broad runtime test was requested or run. Native queue
implementation in the codex-web dependency was outside this package's scope.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-31-team-workload-parallelization/>.
