# Default-branch integration

Complete. The user authorized: "merge it into the default branches when done.
no need to wait for CI." This covers all four registered repositories/remote
master branches. No CI wait, force-push, history rewrite, branch deletion,
additional deployment, archive or session stop was performed.

| Repository | Final feature head, now also remote master |
| --- | --- |
| dev-workspace | 4bec20165387d567b761e43b11fdeabb096618d7 |
| vpsfree-dev-workspace | c56f981a950ab763b71dc91c59e8b5256d478851 |
| vpsfree-cz-configuration | 028d70b233c5b100fea7f7aa0b945fb8b6d3ec4d |
| workspace | c5d8bed5fcd3bc01ce18831ea680aac7edfd68ee |

Fresh SSH symbolic-HEAD checks confirmed every default is master. Default heads
were869b8d4/074926d3/2758415c/29dcc1dd before integration; shared local workspace
master already contained the reviewed tracking ancestors at98389138.
No upstream target advanced and no rebase/conflict resolution was needed.

The source/provider follow-up commit adds all three upstream links to its helper
comment, package documentation and commit message:

- https://github.com/numtide/llm-agents.nix/issues/9887
- https://github.com/numtide/llm-agents.nix/pull/9889
- https://github.com/openai/codex/issues/48050

It labels assembly as a downstream packaging workaround and requires a complete,
daemon-copyable selected upstream package before removal. Migrate both workspace
and system consumers, retain dependency roots/regression coverage and verify
normal startup/resume/fork and package copying. Issue closure or a newer version
alone is insufficient. It changes no Rust source, runtime, pin or state format.
Nix parse is byte-identical to the deployed helper. See the completed independent
[follow-up review](upstream-reference-review-result.md), general lane, retained
gpt-6.1-sol/xhigh/read_only; no new findings and no migrations/obsolete history.

All complete comparisons were captured immediately before integration. The
three independent projects used clean detached temporary targets from freshly
fetched origin/master and `git merge --ff-only`. Configuration operations used
its declared Nix environment and installed hooks. Generic feature/master refs
were pushed atomically; extension/configuration masters were pushed normally.
Workspace master was fast-forwarded in the shared checkout and pushed last.
Pre/post working-tree and index binary-diff hashes were equal, preserving all
unrelated changes. No tracking files were staged during integration.

After pushing, fresh SSH fetches proved every exact local final head equals its
remote feature and is an ancestor of remote master (currently the same head).
All four feature worktrees are clean. Only the three owned temporary integration
checkouts were removed, non-force; their contents remain recoverable from Git.
The ordinary feature worktrees and local/remote feature branches are retained.

Original runtime/browser/protocol/state/daemon/CI and deployment acceptance is in
[rollout.md](rollout.md). New post-integration CI results are deliberately not
awaited or claimed. Consumers retain the deployed generic408 runtime because
4bec changes only comments/documentation; no pin cascade or redeployment is
needed. The live Codex0.160.0 system and workspace generations remain selected.

No required work or blockers remain. Lifecycle is complete, but the session is
not archived/stopped. Stable session:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-02-codex-package-portal-settings/
