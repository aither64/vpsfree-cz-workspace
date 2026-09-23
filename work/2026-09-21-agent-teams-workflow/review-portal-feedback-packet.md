# Agent-team portal feedback review packet

Review one coherent follow-up to the deployed direct-thread team design. The
user requested: counted, human-readable team-preset options; an Add member
control and populated model/effort selectors after Team refresh; collapsed
removed members; reliable member-message scrolling and timestamps; a Codex-tab
selector for ready members with their complete conversation and direct chat;
`Settings` as the shorter tab name; and a live new-session CLI command preview.
The CLI still obtains an initial request interactively. Preserve the session's
tmux-attached `lead` thread and per-member policy; do not change the team
transport, package-master integration, or unrelated sessions.

Initiative: `2026-09-21-agent-teams-workflow`.
Plan and live state: `work/2026-09-21-agent-teams-workflow/{plan,state}.md`.
Stable portal URL: `https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-09-21-agent-teams-workflow/`.

Review feature commits against their immediately preceding heads:

| Project | Worktree under `worktrees/2026-09-21-agent-teams-workflow/` | Base | Head |
| --- | --- | --- | --- |
| codex-web | `codex-web` | `ef4cd581b1c0` | `d542e767310d` |
| generic dev-workspace | `dev-workspace` | `b7883bee18fb` | `58fa8d52b382` |
| vpsFree extension | `vpsfree-dev-workspace` | `08f576a8e8c4` | `160a86837571` |
| workspace configuration | `workspace` | `7db87792ccbb` | `a9767ac137a8` |

The codex-web commit adds a policy-aware queued-turn start and snapshots
nonempty send options in the submission ledger for retry after policy changes.
The generic series separates creation controls (`e473547`), existing Team-tab
controls (`55b44f6`), and ready-member conversation access (`58fa8d5`) with
the matching server-side resolver, policy and uploads. The extension and
workspace commits only advance downstream pins, in deployment order. The
reusable API owner is
codex-web (`codex.Client.StartQueueWithPolicy`); the generic portal consumes it
through its `conversation.Client` integration. The extension and workspace
consume the generic package through Nix pins. Other codex-web consumers retain
the unchanged `StartQueue` method and its empty-policy behavior.

Risk classification: **High**, review effort **xhigh**. The opaque browser
conversation ID resolves a privileged App Server thread and permits mutations;
policy binding, session isolation, runtime locking, and deployment pins are
security and cross-project boundaries. Review General, Architecture and
repetition, Scope and proportionality, and Risk and compatibility lanes. The
roster schema, creation receipt, CLI contract, App Server thread format, and
session lifecycle format do not change. The codex-web submission ledger gains
an optional options snapshot without a schema bump; old zero-option attempts
still load and nonzero attempts without a snapshot fail closed. Existing ready
members become
selectable; removed or unknown members must fail closed. This is the sole
forward-only development host; previous package rollback is not supported.
No database, API client, Terraform, vpsAdminOS node, or cluster schema changes
are intended. Do not reset clusters or modify `2026-09-22-team-test-2`.

Documentation: generic `docs/workspace-portal.md` and `docs/dev-sessions.md`
describe lasting behavior; initiative plan/state record decisions and rollout.
The earlier transport review and deployment evidence in the state file are
historical, not a review of this follow-up.

Quick verification after fixes: codex-web focused retry and queue tests with
`CGO_ENABLED=0`; generic portal `nix develop -c ... go test
./internal/teamruntime ./internal/web` and JavaScript syntax; extension and
workspace `nix flake check --no-build`; whitespace checks. All passed.
Packaged browser/integration checks remain deferred until after review. The
updated Nix vendoring hash is
`sha256-kmiA4qvzb1KhxOrng67/otu+pSvqfOgccnZvZw275Dg=`.

This is a rerun after the first consolidated Sol/xhigh review (packet digest
`bc7e3a3c`). Confirm its findings are resolved: retry options remain bound
after member setting changes; wrapped clients retain prompt and attachment
queue-delete capabilities; unrelated portal concerns are now separate commits;
effort selection preserves the saved member value; the codex-web reference
documents the new API. Also review the new persisted-option logic and all
changed hunks for regressions. Use all four lanes again, independently, not
as a rubber stamp. No live switch has occurred for these heads yet.

Report findings in severity order with file/line and commit references where
possible, and identify the originating lane. Inspect all four commit series
and relevant repository instructions, not only the final tree. Do not author
fixes or launch nested agents. If no findings, say so and list residual gaps.
