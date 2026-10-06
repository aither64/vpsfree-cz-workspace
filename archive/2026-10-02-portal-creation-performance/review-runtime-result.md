# Independent runtime review

Blocking: none. Important: none.

Advisory — the deferred prototype’s no-tool check is incomplete. [verify-creation.py:419](/home/aither/workspace/ai/vpsfree.cz/work/2026-10-02-portal-creation-performance/verify-creation.py:419) rejects only `function_call`, `custom_tool_call`, and `tool_call`. Selected Codex 0.160.0 also persists tool representations such as `local_shell_call`, `tool_search_call`, and `web_search_call`; `image_generation_call` is another supported variant. A run containing these can pass `wait_model` and be labelled passed despite the brief’s no-tool assertion. Extend the guard before relying on that assertion. This affects the prepared harness and does not block runtime publication.

Runtime head `7e4e62b9f7c785e9fc36b8fd3c75c0f864140c75` is ready to publish and proceed to longer verification. Deployment, performance acceptance, cross-project readiness, and merge approval remain separate gates. The complete report was sent to the lead.

The review used retained reviewer0’s verified `gpt-6.1-sol/xhigh/read_only` settings. Session identity matched the trusted binding; both environment identity variables were absent. I read all four mandatory lanes and inspected applicable guidance, session documents, complete commit bodies/diff, documentation, tests, consumers, and prototype. No edits, nested agents, long checks, publication, or lifecycle actions were performed.

[Fresh routing](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-02-portal-creation-performance/dev-workspace/libexec/dev-session:908) establishes freshness under the creation and slug locks before create-only journal publication. Tracking, worktrees, journals, tmux, authority, and retained rosters prevent the direct path. Retries lose that local proof. Tests reject discovery on fresh paths; fork source-idleness and ancestry checks remain intact. Root publication and durable initial-goal attempt ordering are preserved.

[Recovery](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-02-portal-creation-performance/dev-workspace/portal/internal/workspacecodex/client.go:132) checks loaded identities, re-reads indexed candidates, and requires complete discovery before adoption or replacement. Failed or incomplete scans refuse. Exact retained members require matching cwd/project identity; unknown project threads remain candidates. [CLI roster composition](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-02-portal-creation-performance/dev-workspace/portal/cmd/workspace-portal/main.go:994) validates the independently recorded root under the roster operation lock and releases it before new root submission. Retained rosters prevent retargeting; an undiscovered recorded root requires exact not-found before replacement. Retirement and lifecycle algorithms remain unchanged.

Progress preserves arguments, descriptors, diagnostics, stdout, timeouts, and exit status. Ruby drains pipes concurrently. Go bounds frames and rejected diagnostics, rejects malformed or ambiguous fields, and continues draining rejected records. The creation runner retains transition FD inheritance and process-group cancellation and joins callbacks before returning. [Receipt updates](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-02-portal-creation-performance/dev-workspace/portal/internal/web/creation.go:710) verify workspace, slug, receipt, attempt, and running state; merge only phase/time; coalesce duplicates; and cap writes. Final proof and upload binding still decide readiness. The flag is consumed before runtime inheritance, older silent helpers retain broad phases, and members remain sequential.

Ownership and scope are appropriate: runtime owns recovery, CLI owns roster composition, SDK owns the optional field, and the progress package owns ephemeral transport. No speculative framework, persisted schema, root project, member concurrency, or browser transport was added. Lasting explanations live in the owning session and portal guides; rollout and forward-generation recovery remain in the session record.

Go and Nix select reviewed SDK `4c170393a96ed0a6ac2e43488d073f6fcab36132`, matching its pseudo-version and vendor hash. Codex/llm-agents inputs are unchanged. Consumer inspection identified the extension’s package composition, workspace consumption, and configuration’s host-module/Codex-package use. Their locks still pin runtime `40838aa28c8433e42a4a3fbed4586a3df0146de9`; no private creation-helper override was found. The runtime state contract is unchanged across that revision, review base, and feature head. Downstream pin alignment and consuming-package validation remain for the readiness supplement.

The exact merge base is `4bec20165387d567b761e43b11fdeabb096618d7`; the worktree is clean at the reviewed head. Complete series:

1. `dfda7b8fc501c4a6f761f6d5bc8451da3cc853b8` — SDK pins/hash.
2. `bd18b321117ec144d66a06c5662a64004e413ae1` — locked fresh routing and conservative recovery.
3. `7e4e62b9f7c785e9fc36b8fd3c75c0f864140c75` — streamed initialization progress.

The final diff contains 26 files, 1,708 insertions, and 120 deletions. The commits are coherent and separately reviewable with owning tests/docs. **No obsolete history, superseded approach, follow-up iteration, unused compatibility path, or transitional migration remains. No migrations.** Persistent formats and package transition contracts are unchanged; no feature schema version was merged, released, deployed, or externally consumed.

I inspected the parent’s exact script and corrected passing log: five selected Go packages, 60 Ruby tests/624 assertions, syntax, and whitespace checks. I independently checked base-to-head whitespace and source/test/document consistency without rerunning suites. The failed fork fixture was corrected while preserving production validation. Full packaged/browser checks, integration and race behavior, live faults, five creation measurements, and the actual-history canary remain unverified.

Reviewed prototype SHA256: `acee63e1d3e1606b787f918ae04c6d571bcf53a745e5c6cdf59b64db6907780e`. Its private state/socket/auth isolation and retained-process policy match the brief. Synthetic history does not establish production-history equivalence. Root-response loss occurs at the helper/Ruby boundary; partial-member injection can miss its scheduling boundary and reports inconclusive. I did not execute it.

The lead should preserve this report, Advisory disposition, and exact head in `state.md`, address the prototype guard, publish the runtime, align downstream pins, and run longer checks before the readiness supplement. Merge approval remains outstanding; the session stays open.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-02-portal-creation-performance/)
