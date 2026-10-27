# Runtime and configuration upstream rebase

Runtime now uses `ec93e57d34c038e551af53b8b0f7d26de3f07c03` (tree
`c6f45d0a22dad62763e3c7e6c39bb42c227572db`) on freshly fetched
`9baeea528f2e270332afa13786ec85a49a68e4c3`. The ordinary replay preserves all
11 feature units exactly by `git range-diff` against `960dd816..f520a395`.
Incoming observer behavior and dependencies remain intact. No migration was
introduced or modified. The existing single dependency-update stream is retained.
The old f520 ref and verified bundle remain preserved.

Six focused check commands passed: JavaScript syntax; pure Node observer,
composer handoff, composer retry and queue refresh contracts; and Go observer,
workspace client, web naming and retry-policy tests. Go completed in 29.327s,
with 69 test cases/subcases and no skips or failures. All command children were
reaped and their groups empty without signals. Declared previously selected
Go/Node/compiler tools were reused. No Nix command, native/provider request,
real browser, VM or package build ran. Final worktree/index are clean, with 617
tracked paths. See `dev-workspace/final.json`, `range-diff.stdout`, complete
`final-series.stdout`, `final-full-diff.stdout`, `final-paths.stdout`, and
`affected-quickchecks/summary.json` with `counts.json` and raw command logs.

Configuration's ordinary replay exposed the sole old generated pin's conflict:
incoming runtime9ba/+Ldc versus f520/K73. The exact paused state and all three
complete lock graphs were retained. Under lead's explicit same-scope disposition,
ordinary `git rebase --skip` skipped only that obsolete pin, completing in .721s.
The feature worktree is now clean at `7eaaafd718809e16867c9b4614f9b2e2d54fa62a`,
tree `663809784ff3c38e502aabc558fd1d28508f0a58`, with zero feature units.
Its complete 64-node graph equals incoming upstream. No lock/message was manually
changed, and no confctl/Nix regeneration ran. Old61af ref/bundle remain intact.
See `vpsfree-cz-configuration/final.json`, original rebase/conflict/skip receipts,
`semantic-lock-comparison.json`, and base/incoming/feature lock graphs.

Configuration's zero-feature range is preparation for one later coherent normal
pin to the reviewed/published combined runtime. It is not final consumer delivery.
Both refreshed repositories remain unpublished. The lead owns refreshed review,
publication and coherent consumer selection; no default integration, deployment,
claim or lifecycle action occurred. All old source/NAR/build evidence retains its
original input scope. No product documentation change is useful for this replay;
these operational facts remain session records. Lead owns shared state tracking.

Session remains open:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-workspace-session-ui/
