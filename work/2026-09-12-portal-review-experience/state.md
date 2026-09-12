---
lifecycle: active
---

# Portal review experience

## Current status

The approved file-tree and parent-navigation extension is implemented, reviewed,
committed, pushed and deployed to aitherdev as user profile 31. The exact package
is `/nix/store/4zjl93s2i42zzdbfv4jv1b8s0000b8wd-dev-workspace-0.2.0`.
Package, quick checks, live browser acceptance and both final CI runs pass.
See tree-verification.md and tree-review-reconciliation.md.

The initiative stays active and open. All feature branches remain unmerged and
retained. No merge, archive, delete or branch deletion was performed or authorized.
Shared coordination checkout remains on master; preserve unrelated working-tree
and index changes. The deployed extension is ready for user review.

Stable portal:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-09-12-portal-review-experience/

## Session and repositories

Slug: `2026-09-12-portal-review-experience`.
Workspace: `/home/aither/workspace/ai/vpsfree.cz`.
Shared thread: `01a09541-d1ba-7e32-a634-6f915c2da0a4`.
Initial tracking commit: `e0d3dee`; profile 29 checkpoint: `2a83eff`;
profile 30 handoff: `44cfd5f`. This approved follow-up reuses the verified session
and branches. DEV_SESSION_SLUG and DEV_SESSION_WORKSPACE set to these values make
`dev-session current` match. New session creation is not needed.

All branches are `2026-09-12-portal-review-experience`. Worktrees are under
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/`.
All four remain registered in portal.yml and are clean/pushed over SSH.

| Project/worktree | Final head |
| --- | --- |
| codex-web | de83e9c72dec6cb5ff8ec13d5b0b21ed60148117 |
| dev-workspace | 41c6d75e8f7cdea1e5cbced7d0106d072d56484d |
| vpsfree-dev-workspace | 6c98b3676a46c9a9c2830198eae9042b064a71e7 |
| workspace | cd648e2bd31e3b5d43703320be7967a92bd1e06b |

Upstream master was explicitly fetched before final feature pushes. Runtime and
organization heads include their current upstream bases. The workspace feature
was rebased onto shared master 44cfd5f; range-diff proved all three prior deployment
patches unchanged. Its source-equivalent predecessor is cc5f495. Only its new pin
commit changes the source for this extension. Shared master has no feature merge.

## Current delivered behavior

Directories in branch/commit file trees start expanded, support native keyboard
and collapse controls, and retain collapse choices through layout/version changes.
File/history navigation reveals the selected path. Compact colored status letters,
green/red statistics and repository-relative path copy icons keep the navigator
small; headers retain full status descriptions. The full-file back arrow returns
to the exact file/comparison/layout and clears version/line selection.

Parent hashes open complete commit pages, including all parents of merges and
ancestors before the feature base. Root commits show No parent; diffs stay
first-parent. Parent links clear file/view/version/line while retaining the frozen
review and layout. Feature commit history remains limited to its comparison range.
No dependency, API route, URL key, persisted format or system configuration changed.
The JSON parents array is additive. Older packages ignore it and report new
ancestor links outside their old range as unavailable until rollforward.

## Review and validation

The runtime series is dependency ordered: native backend 4e714b7, parent UI 9490e1e,
then tree/controls 41c6d75. The intermediate parent UI was tested separately in a
clean detached worktree and removed afterward. No prior deployed commit was
rewritten. Only the current extension's unmerged parent/tree and downstream pin
commits were amended, using exact force-with-lease pushes.

All four required reviewers were fresh gpt-5.6-sol at xhigh. General and architecture
found no issues. Scope found one Important URL mismatch: view=diff was present in
parent links despite the plan's cleared selection. It was omitted, the browser
assertion strengthened, all 21 checks passed, and the fix folded into its owner.
Risk found no Blocking/Important issue. Its Advisory on recursive trees for Git
paths thousands of directories deep is accepted as a comparison-local availability
limit. Normal filesystem paths are constrained; this does not claim the server's
4 MiB/5,000-file bounds also constrain Git directory depth. Iterative rendering of
such historical paths is a possible future improvement. No real 5,000-file DOM
stress or shallow-repository acceptance is claimed.

Quick checks passed: full Go (repository 7.722s/web 27.742s), focused parent/durable
checks 0.630s/1.147s after final native simplification, review-related race checks
6.125s/6.939s, JS parsing, committed-range whitespace and workspace Ruby 3/14.
Actual Chromium component acceptance passed 21 checks with real pinned editor,
syntax and clipboard code, including tree/keyboard/history, paths/colors/arrows,
parent/root/merge links, frozen lines, responsive layout, CSP and 8-editor retention.
Root inspected desktop/mobile screenshots. A launch-path harness mistake was
fixed by using Chromium's bin/chromium executable; no product change was needed.

All required reviews were reconciled before manual package/live acceptance.
The exact package passed Go (repository 10.278s/web 32.932s), session 296 runs/2,979
assertions with 12 existing skips, and host 73 runs/438 assertions with 3 existing
skips. There were zero failures/errors. Its check phase took 2 minutes 13 seconds.
The final workspace flake deployment-contract check passed 3/14. Generic runtime
and organization flake checks are supplied by exact feature-head CI, avoiding
redundant local runs. No local kernel build was needed.

Final runtime CI 34711167462 passed on 41c6d75. Organization CI 34711209482 passed
on 6c98b36, including flake and devcluster checks. Earlier original candidate CI
34710527917 and 34710592527 both passed;
all superseded runs had already completed, so none needed cancellation. Workspace
has no matching Actions workflow. Exact results/links are in tree-ci-results.json.

## Deployment and cleanup

Normal `workspace-host switch --source <initiative>/workspace` installed profile 31.
Generation/runtime/cluster checks and the Codex App Server contract passed. Codex
remains 0.154.0. Router, portal, Codex and tmux services are active; the actual portal
executable matches the expected 4zjl93s package. Strict-TLS/authentication smoke
passed, including unauthenticated 401, Messages default, counters/assets and exact
conversation identity. tree-deployment-results.json records the installed package.
Previous profile 30 retains 8a2c8nb; no live rollback or forced interruption was used.

The first live browser run passed all 16 checks in 139.141 seconds on exact runtime
41c6d75. It verified native clipboard copying, expanded tree/collapse/keyboard,
colored statuses/counts, retained syntax, layout/history navigation, cold full-file
links and back arrows, actual parent new-tab opening, full parent messages,
reload/Back/Forward, navigation before the saved base, and 390px mobile layout.
No page errors or CSP violations occurred. Root inspected all four screenshots.
The browser ignored certificate errors; strict TLS was checked independently.
No Git refs or conversation state were changed. Evidence and frozen URLs are in
artifacts/tree/tree-live-browser-results.json; merge/root/status edges remain
covered by component/Go fixtures.

The temporary detached parent worktree, browser/component processes, build
outlink, logs, temporary screenshots, duplicate harness and commit-message files
were cleaned. Registered worktrees, branches and the installed package remain.
One consolidated coordination handoff records the delivered extension; no feature
integration or session cleanup is implied.

## Previous deliveries and preserved limitations

Profile 30 delivered immediate accepted-steer receipts, Waiting for instructions,
shared copy icons, faster native repository lookup/batches/cache, full messages,
syntax-highlighted split/unified/full-file views, statistics/statuses and frozen
URLs for commits/files/source lines. Direct metadata median improved from 615.8 ms
to 24.98 ms; HTTPS still had about 0.4s overhead. This was not a whole-page latency
claim. Evidence is retained in follow-up-verification.md and linked artifacts.

Profile 29 delivered fixed question actions, immediate new/fork/plan navigation
with initialization progress, repository histories/local diffs, web-search and
subagent events, root-turn counters/timing, and the Messages default. Earlier
real creation/recovery, protocol and browser evidence remains in the original
verification reports. The real blocking-question observation passed but answering
after its isolated portal reconnected was unverified; controlled answer tests
passed. Large-history missing-cwd and private Plan-mode reconnect limitations
remain documented in creation-integration-results.md. No shared Codex settings
were changed. Unobserved timing stays unclassified; private timing/comparison
retention and missing Git object limits remain documented.

Next action: user review of the deployed extension. Keep the initiative open.
Do not merge or archive without a request.
