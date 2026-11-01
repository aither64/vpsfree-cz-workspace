# Compact status row integration

The user approved the three repository/master integrations with "merge it" on
2026-10-11, replying to the handoff naming this exact scope. Fresh fetch and
complete series/diff comparison found no head changes or required rebase.
Each branch retained one reviewed/focused-verified commit and one consolidated
consumer update per stream; no migrations or compatibility shims.

All three integrations used `git merge --ff-only` followed by direct SSH pushes:

| Repository | Previous master | Integrated head |
| --- | --- | --- |
| dev-workspace | 27ff7949944f79322b810fae7dd1a6e359d985c4 | 17222c374bf48c65edc36895e07408c65f1e7b53 |
| workspace | 12f3a91725b2a3565476c8184bd8a92fcf1c8f61 | 7c54c132420ed367cfe0ed8445c8baf925b12d4d |
| vpsfree-cz-configuration | 14cd296ad24cec0d62161f691c7d0374bda9e35c | d1f0ce5a9a292039def259fef53c2f17bede4cac |

Each push's remote proof found master and the retained feature branch at the
exact integrated head. Runtime and configuration used fresh detached temporary
target worktrees; only those clean targets were removed. Workspace integrated
from shared master, preserving the index and unrelated tracked changes.
Feature branches and registered feature worktrees remain.

Configuration's initial worktree creation invoked its checkout hook outside the
Nix shell and exited 78 for missing ambient Ruby gems after creating the target.
The parent inspected that clean owned target, entered the declared Nix shell and
repeated checkout with the hook enabled. Hook recovery, merge and push passed;
no hook was bypassed. Reusable lesson is in
[worktree hook note](../../notes/vpsfree-cz-configuration/2026-10-11-worktree-hooks-in-nix-shell.md).

Evidence: [preflight](integration-preflight.json),
[runtime push](integration-dev-workspace.json),
[workspace push](integration-workspace.json),
[configuration push](integration-vpsfree-cz-configuration.json).
Saved portal comparisons retain the pre-integration bases and exact final heads.
Final fresh fetched ancestry/ref proof is in
[integration-final-refs.json](integration-final-refs.json). A later global
tracked-diff digest differs from preflight in the concurrently shared checkout;
the immediate before/after integration check preserved unrelated changes and
the index. Those ongoing shared changes remain untouched.
Deployment remains the same verified application/host; no source rewrite or
second deployment was needed.

Post-merge master [CI 38127097132](https://github.com/aither64/dev-workspace/actions/runs/38127097132)
passed for exact runtime head 17222c374bf48c65edc36895e07408c65f1e7b53. A fresh
Luna/low one-operation utility observed both fast package/focused checks and host
activation/renewal/rollback/user-service VM checks. The watch exited 0 in 11m42s;
no operation remains running. Evidence: [merge-ci-result.json](merge-ci-result.json)
and merge-ci.status. The initiative is complete; its session and feature branches
remain retained without archive, deletion or session stop.
