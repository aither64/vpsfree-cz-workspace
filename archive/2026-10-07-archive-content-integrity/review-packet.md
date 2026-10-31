# Final review packet

Outcome: reliable archive/revive record integrity without POSIX permission blockers, useful concrete failure + step + time in Settings, retained full error under collapsed details, and recovery of the original blocked session. User approved implementation and aitherdev deployment, not integration into master.

Read plan.md, design.md and state.md here; recovery-mode-proof.json and recovery-result.json document the executed single-mode correction and ordinary native retry. Original archived session is 2026-10-04-session-archive-reliability.

High risk: persisted lifecycle proofs, irreversible cleanup, old journals and deployment/rollback. Review all four lanes (general, architecture, scope, risk). Trusted local host operator; concurrent operations, wrong identity, data integrity, interrupted operations and remote client authentication/input checks remain in scope. Do not invent filesystem-adversary defenses against the trusted operator.

Ownership: generic dev-workspace owns the digest and archive worker/browser presentation. vpsfree-dev-workspace extension consumes the runtime through workspace's direct nested pin; configuration devWorkspace input consumes its host module. Downstream branches select 9f999f7f, preserving extension 0ff827df and Codex/Nixpkgs/sibling identities. Check final semantic locks and bin/check-dev-workspace-deployment.

Acceptance: new archives handle 0600 files, restrictive umask and permission changes on retry; changed content/path/type/link target still fails. Exact deployed legacy digest can recover archive prepared intents, moved targets and revive. No sidecar/journal rewrite. Actual valid UTF-8 exception survives worker/cold status, max16KiB. Settings shows one useful cause and next step/time, generic stale/pending notices suppressed only when real failure available, raw technical metadata collapsed. Real browser checks remain planned after review.

Compatibility: new writes content-only digest; dual comparison supports deployed legacy permission-inclusive proofs exactly. No schema bump/migration; older package refuses an unfamiliar new digest. Package transitions already refuse unfinished journals; finish with current package before transitions, forward-only recovery. Existing caches without concrete error retain current fallback. No coordinated node update needed. Deploy matching feature host configuration then separately selected application user profile. No force, relink, private state rewrite or default-branch integration.

Commit split: runtime archive integrity + its tests/docs; runtime saved errors + browser presentation + its tests/docs are one user-facing archive-failure flow. Independent generated downstream pin commits per consumer. No fixup/superseded commits. Legacy reader is required by installed/deployed journals, not abandoned branch design. No migrations, released or unreleased.

Non-goals/user decisions: remove permission comparison, do not require normalizing chmod for future archives, add no generalized permission framework, repair API, error taxonomy or new queue. Preserve exact existing old journal proofs. No new roster or borrowed target-session team.

Docs changed: dev-workspace/docs/session-archive-recovery.md (lasting digest compatibility/recovery), docs/dev-sessions.md (current Settings and failure behavior). Individual recovery evidence/rollout remains in this initiative.

Quick checks passed: seven focused Ruby lifecycle regressions, 182 assertions, zero failures/errors (quick-lifecycle-final.log); Ruby syntax for lifecycle/worker, node --check app.js, Go TestShippedBrowserClientMatchesSessionAPI (0.98s); git diff --check; matching downstream deployment contract. Configuration commit hooks Nixfmt and commit message checks passed (generated-width advisory retained).

Reviewer selection: no eligible retained roster (threadless lead; team list refuses missing lead thread). Installed catalog digest437585347ac8b2cdbf498a169d8871e684f3f61ccf1dd48e8589d79ef9629abd, default lead_reviewed role reviewer, gpt-6-astra/xhigh/read_only. Fresh standalone review, no nested agents, no source edits. Explicit whole-branch history and migration conclusions required.

## dev-workspace

Worktree: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-07-archive-content-integrity/dev-workspace
Base: a2bbf2f1c588de7eec0d7d52580a89a9d4bef984
Head: 9f999f7f713557b261a3d6d1597f8372eabf6518
Full series:

2275d99840aefebece9bc8554a64f51eaef59bfe archive: verify record contents without permission constraints
9f999f7f713557b261a3d6d1597f8372eabf6518 portal: show concrete archive failures in concise settings

Final diff: dev-workspace-final.diff

## workspace

Worktree: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-07-archive-content-integrity/workspace
Base: 2addfb2658af8e9d703a3fae9dd424919f245f19
Head: 4d0c62626c36332f7013ba8ff15c52a6f37e0218
Full series:

4d0c62626c36332f7013ba8ff15c52a6f37e0218 inputs: select archive content integrity runtime

Final diff: workspace-final.diff

## vpsfree-cz-configuration

Worktree: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-07-archive-content-integrity/vpsfree-cz-configuration
Base: 20cc8ae3292df24b519b9e4858d39660b362295e
Head: 23412037590f1d31b85a53410946a18b36db8bc8
Full series:

23412037590f1d31b85a53410946a18b36db8bc8 inputs: set devWorkspace to 9f999f7f

Final diff: vpsfree-cz-configuration-final.diff


Inventory refreshed after narrow fixes: review-report.md retains original reviewed heads, findings and direct remediation evidence. Final pins preserve the same semantic dependency graph. No full review rerun was needed for the explicitly assessed corrections.
