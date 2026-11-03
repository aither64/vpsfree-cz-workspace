# Managed member report delivery

2026-11-03; bounded source-only architect0 investigation.

**Conclusion:** an authenticated same-session member `report_to_lead` call
uses active native submission. An idle lead is a supported target: the normal
path starts a turn; the cold-recovery path queues the report durably and
activates the recipient. This is stronger than passive inbox delivery.
It does not establish that a utility's final text automatically wakes the lead.

## Exact selected source

Installed package:
`/nix/store/0q7rc75dh4mjrxpb37m1hchfwcbmpa7a-dev-workspace-0.2.0`.
Its derivation is
`/nix/store/2jvhgyq2ilxa4cprlswc7fwh93b3snpx-dev-workspace-0.2.0.drv`;
the derivation's `src` is
`/nix/store/pw7ffd5bsg55wvcbqwc3vs91h9f1894i-source` (called SOURCE below).
SOURCE `flake.lock` and `portal/go.mod` agree on codex-web
`d3a29bee90ef00a08816920408c596152339a637`; `nix/workspace-portal.nix:278`
checks that module pin during packaging. The codex-web source was read from
that exact commit in the canonical bare repository. Mutable repository HEAD
was not used for the final implementation conclusion.

## Delivery trace

1. SOURCE `portal/cmd/workspace-portal/team_mcp.go:146` constructs the host
   invocation `team assign ... --from MEMBER --to lead --message-stdin
   --message-id ID`. Caller identity comes from native metadata and is
   revalidated; tool arguments cannot choose the session or sender.
2. Installed `libexec/workspace-portal/.dev-session-wrapped:1920` reads the
   bound lead thread and passes it as `--root-thread-id`, retaining expected
   member/lead identity checks. This is the same team assignment entry point.
3. SOURCE `portal/internal/teamruntime/runtime.go:2320–2428` validates the
   sender, selects `rootThreadID` when `to == "lead"`, and calls the same
   `Client.SendWithOptions` used for member assignments. No check requires
   an already-running lead turn. Session-active identity checks concern the
   valid nonterminal session, not an actively sampling turn.
4. SOURCE `portal/internal/workspacecodex/turn_retry.go:305–363` applies the
   ordinary submission/retry admission and calls `sendWithRecovery`.
5. SOURCE `portal/internal/workspacecodex/recovery.go:36–114`: without a cold
   recovery boundary, dispatches to the pinned client's `SendWithOptions`.
   At the cold boundary, records `PrepareSendWithOptions`, calls
   `QueueWithPolicy`, then `ActivateThreadWithSettings`, updates the recipient's
   recovery activation, and returns its `queuedSubmissionId`.
6. Pinned [codex-web `codex/client.go:5277–5438`](https://github.com/aither64/codex-web/blob/d3a29bee90ef00a08816920408c596152339a637/codex/client.go#L5277-L5438)
   resumes the thread, reads `ActiveTurnID`, and sends `turn/steer` for an active
   turn or **`turn/start` for an idle thread**. It records the native accepted
   receipt. Its `ActivateThreadWithSettings` at lines 4512–4539 loads the
   exact retained thread; the documented contract permits native queued work
   to execute on that load.

SOURCE `docs/workspace-portal.md:1630–1647` documents authenticated host
delivery, native submission receipts and same-ID deduplication, and explicitly
states: “Completed turns are not automatically forwarded.” The older observer
rule that idle sessions stay idle concerns automatic progress checks, not this
explicit member-report route.

## What is and is not established

The installed implementation supports a retained member reporting into an idle
lead through a new native turn. The existing `steered=true` receipt proves
delivery into an active turn only. A `queuedSubmissionId` establishes native
queue acceptance; it alone is not evidence that the queued turn has started
or completed. No idle-lead runtime test was performed in this investigation.

Identity changes, recovery holds, pending original submissions, transport
failures and uncertain outcomes can still refuse or delay delivery. They are
not bypassed by the report tool. Retry an uncertain report with its same ID
and exact content under the existing protocol; do not manufacture a second
message to claim delivery.

The supported ownership arrangement is therefore: the retained member owns
the verification package, receives its utility result, and actually invokes
authenticated `report_to_lead`. Do not infer this behavior from a passive
utility finishing. This finding does not direct the lead to end its turn.

No live roster, peer session files, transcripts or credentials were read; no
self-message test, CI observation, runtime mutation, lifecycle action, utility
or source change was performed. Only installed/committed source and public
documentation were inspected.
