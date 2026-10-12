# Portal recovery implementation review

Initiative 2026-09-13-portal-recovery. Read plan.md and state.md beside this file.
All worktrees are under /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-13-portal-recovery/<name>.
All feature branches have that same slug. Review committed series; read repository AGENTS.md.

## Goal and acceptance

Recover conversations after laptop sleep/network loss without reload; visibly report stale/error state and retry until a bounded snapshot refresh succeeds. Preserve drafts, attachments, pending answers, scroll, submission/receipt semantics and usable message controls. Hide repository pagination when page zero has no more rows; retain Previous on final pages. Display entire comparison's commit count and net line additions/deletions, using the same immutable base/head as history and Compare including preserved integrated comparisons. Single and batched API consumers must agree; summary failures leave history usable.

## Commits

| Repository | Base | Head |
| --- | --- | --- |
| codex-web | ee9ab42791a84b79315d952501264a6cbafc8695 | 9151c2b862c04775f2562a77365103380772ee04 |
| dev-workspace | 8a43d3b09ddd9fa3b2c5f6c9aaba3ef7efc0ad0f | 723ff4a79d2d6d705364fbfdfa7509337f4df8aa |
| vpsfree-dev-workspace | 37f3bfa21079b217aef15a4c2e75ed7451b9d156 | 71229ca9c0ea5a3cd0af6e6bf1e2b6d283d95c92 |
| workspace | 5d5137959467555675529aeab7df91c719b8a0c4 | 569a71dae07e71f7a369451f31579f69f2ebed2f |
| vpsfree-cz-configuration | b0252827958a4cc231a2a0bb56ae3a1844db8ae8 | 6cb0894a958a67357c7b72f230c4675dd4590a9f |

codex-web has one functional commit for shared bounded recovery, SSE and standalone mounted UI, with supporting tests/docs. dev-workspace separates repository summaries/pagination from conversation recovery. The latter includes the provider Go/flake/vendor pin because the consumer imports its new API and cannot stand alone without that pin. Organization and workspace have only their consuming package pins; configuration has an unchanged generated confctl commit. All intended changes are committed and pushed. Workspace was fetched and rebased on current shared master before review.

## Scope, decisions and compatibility

No merge, session archive/delete or real session stop; user authorized aitherdev deployment. Keep send controls usable during outages. No offline submission replay changes. No new session state, schema, receipt format, App Server version/protocol, option, host ownership or lifecycle behavior. No sum of individual commit churn or always compare against current master: totals preserve the existing comparison contract. Queue reconciliation is inside the read deadline; receipt acknowledgement after awaits must not apply superseded snapshots.

Owning shared provider: codex-web conversation/assets/sync.js, reexported from conversation.js. Public createConversationSync read(signal), apply(snapshot,{signal,isCurrent}), freshness callback and refresh/retry/schedule/destroy. Shared createConversationClient read methods accept optional signal and have GET deadlines. SSE ready/heartbeat are named additive events with existing update hints retained. Heartbeat enforcement requires server advertisement, preserving old servers; older clients ignore new events. Codex-web mountConversation and dev-workspace portal/internal/web/static/app.js are the current browser consumers discovered from imports. Runtime's Go and flake pins select this same provider. Organization flake wraps runtime; workspace consumes organization; config devWorkspace pin supplies host module only. App remains installed through workspace-host user profile. New history summary/summaryError fields are optional and additive. No migrations or rollback state conversion. Existing tabs need one reload to acquire new JS.

Trust boundary: local operator trusted to administer host; retain ordinary ownership/configuration checks, concurrency and rollback. Remote clients remain untrusted. This does not weaken security of projects/VMs being developed.

## Quick checks and risk

High risk classification due shared SSE/browser contract, deployment ordering, mixed versions and rollback. All four lanes, gpt-5.6-sol xhigh. Provider full go test ./... passed; node --test test/*test.cjs passed 19 tests, including 14 sync contracts. Runtime go test ./internal/web ./internal/repository from portal passed against actual pinned provider (not a replacement), node --check portal/internal/web/static/app.js passed, all diff whitespace checks passed. Node fixture updated to capture sync.js and assert named readiness. Tests include stalled requests, quiet failures, heartbeats/CLOSED, races/wake/BFCache/late apply/backoff and GET cancellation; repo 0/1/50/51/101, net cancellation, renames,binary,rebase,integrated snapshots,batch equivalence and summary-limit failure. Package vendor hash measured with Nix's fixed-output validation; workspace/config deployment contract passed.

Long integration not started. After review resolve findings, then run flake/package checks, CI current heads, Firefox and Chromium acceptance with actual served modules and outage injection, and system build/dry activation. Record old generations, switch user package, then confctl switch aitherdev from feature configuration. No unexpected local kernel build permitted. Validate live auth/assets/SSE/summary and rollback if needed.

## Review task

Read the mandatory-change-review skill and assigned lane reference. Perform review yourself, no subagents. Write findings with severity, evidence, file/line and commit refs, plus residual gaps to the requested report path. Do not modify implementation. Use committed source; the coordinating agent may prepare untracked temporary acceptance fixtures during review. Those are evidence preparation, outside project changes.
