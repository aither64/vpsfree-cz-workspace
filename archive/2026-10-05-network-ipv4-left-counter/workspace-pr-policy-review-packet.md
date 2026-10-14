# Workspace PR policy final review

User request: ordinary workspace projects need development branches, not PRs;
retain PRs for vpsadmin-webui because its own instructions require them. Prevent
repository-specific instructions from affecting other repositories; preserve
fast-forward integration without GitHub merge commits. This is a bounded
follow-up in session 2026-10-05-network-ipv4-left-counter.

Owner/component: the shared coordination workspace owns orchestration and the
mandatory Git procedure. Consumers are agents following AGENTS.md across the
independent projects. No provider, application, package pin or runtime changed.

Worktree: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-05-network-ipv4-left-counter/workspace
Branch: 2026-10-05-network-ipv4-left-counter; target master.
Base: 8dfb2bf8fb249d9fb348cfee55ba255b0bd58f10
Head: 4f22fc750aab877e6fae64ceca869a49173412a1
Complete base-to-head history: workspace-pr-policy.history
Complete final diff: workspace-pr-policy.diff
One logical committed instruction clarification; no obsolete fixups or abandoned
approaches. No migrations; no schema, persisted state, release, deployment or
external consumption. No branch/default integration authorized.

Only AGENTS.md and docs/agent-instructions/git.md change. Core stays below its
16 KiB discovery budget (16239 bytes). Detailed policy lives in routed Git
procedure. Explicit user approval for default integration remains unchanged;
so do hooks, independent review, verification, worktree/SSH and retention rules.
PR-specific review requirements are not extended outside their owning repository.
Existing PRs remain untouched; creation, closure and management are out of scope.

Root inspected final wording. Existing quick check:
`nix shell --no-update-lock-file --inputs-from . nixpkgs#ruby --command ruby test/agent_instructions_test.rb`
Passed 8 runs / 144 assertions / 0 failures, errors or skips. Log/exit:
workspace-pr-policy-quick.log/.exit. Whitespace check passed; clean committed
worktree. No hook framework or active custom Git hooks are declared/installed;
normal git commit used without bypass. No new policy mirror tests or long builds.

Risk: low, bounded reversible documentation clarification preserving existing
authorization and integration boundaries. Documentation-only general lane;
no implementation/abstraction/protocol/deployment change warrants other lanes.
Reviewer: eligible retained reviewer0, review-purpose, read_only,
gpt-6.1-sol/xhigh, unchanged saved settings. Read mandatory-change-review and
references/general-review.md fully and perform direct final whole-branch review,
including explicit history and no-migration conclusion. Remain read-only; do not
edit, test, fetch, commit, push, merge, create/manage PRs, deploy, mutate lifecycle
or spawn nested agents. Current root plan/state explain this bounded task.

Final branch replayed onto concurrently advanced shared master containing only
unrelated session tracking/archive commits. Both changed document SHA256 values
remain identical to checked source; range-diff shows the one commit patch is
unchanged (workspace-pr-policy.range-diff). Quick evidence applies to identical
instruction and test bytes. No unrelated tracking changes are authored here.
