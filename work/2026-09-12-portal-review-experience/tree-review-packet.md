# File tree and parent-navigation review

Review only this approved extension to the deployed profile30 feature. Read
mandatory-change-review/SKILL.md and the assigned lane reference. Reviewer uses
fresh gpt-5.6-sol at xhigh; perform review directly, no nested delegation.

## Paths and exact committed ranges

Workspace: /home/aither/workspace/ai/vpsfree.cz
Initiative: work/2026-09-12-portal-review-experience
Feature worktrees: worktrees/2026-09-12-portal-review-experience/<project>
All branches: 2026-09-12-portal-review-experience
Plan: tree-navigation-plan.md; state.md holds current progress.

- dev-workspace: 820277e6cc3aa7ff9acb0396feb3314e7f84996a..cbe617df87c29bf02c64df4188c9ca0878d22601
- vpsfree-dev-workspace: ee9c55b3c25fd0b0002b3ce4796167d27378cd3a..e2aa14bf41d1c2d18d59f3d66ef3caee2c41c02b
- workspace: cc5f495c6485d76abeaf16087d1fe4b0069d6893..2d037e03c3eb28f514f0f84a4cb5f15a2c0640ef
- codex-web unchanged at de83e9c72dec6cb5ff8ec13d5b0b21ed60148117.

Workspace feature was rebased onto shared coordination master44cfd5f, preserving
all three old deployment commits byte-for-byte by range-diff. cc5f495 is the
source-equivalent predecessor of deployed082c4c9. Shared master is not a feature
integration target for this delivery. Project trees are clean and pushed.

## User intent and acceptance

Use native expanded-by-default directory tree for branch/commit changed files.
Directories precede files, sorted alphabetically within each directory; show
basenames and full-path tooltips, compact colored statuses with accessible
labels. Keep collapse choices through layout/version changes; selecting a file
or following history exposes its ancestors. Collapse affects navigator only.

Color additions/deletions green/red in all stats. Copy icons in tree and file
headers copy displayed repository-relative paths, without quotes/newline; copy
must not navigate. Full-file heading has a back arrow labelled Back to diff,
preserving exact review/file/layout, clearing version and line. Retain path and
status handling for root/deep/Unicode names and file-directory replacements.

Parent hashes open full standard commit pages. Merges link all parents; each
commit diff remains first-parent. Root says No parent, never links empty tree.
Preserve frozen review/layout, clear file/view/version/line when opening parent;
new tabs/reload/history and repeated navigation before feature base must work.

## Design and ownership

Generic runtime owns all behavior: browser repository-review.js/css plus native
ReviewReader. Parents becomes additive non-null JSON array; details accept only
commits reachable from saved immutable review head. Branch History range remains
unchanged. Invalid/unrelated/newer commits remain rejected, same session and
registered repository scope checks apply. No new endpoints, URL keys, persisted
records/schema, Git fetching/object retention, packages, icon or tree library.

Shared codex-web createCopyButton is reused unchanged (runtime app.js injects it).
CodeMirror/Shiki bundles, CSP, cache/coalescing/batching/editor bounds remain.
Tree uses Maps/nested lists/native details and temporary DOM expansion state.
Line-count parts are formatted once for existing text and colored DOM consumers.
Organization and workspace are mechanical downstream Nix pins, discovered from
flake inputs; site user profile is the deployment owner, not system configuration.

## Commit boundaries

1.4e714b7: native ancestor lookup, additive parents and Go tests.
2.233ee1c: parent-page UI, docs and actual browser coverage. Independently checked
  in a temporary detached worktree without the tree/controls changes.
3.cbe617d: comparison navigator/header presentation, native tree and aligned
  status/count/path-copy/back controls, docs and browser coverage. These controls
  share the tree leaf/file-heading layout; they form one compact comparison UI
  change with no independent backend, schema or resource policy.
4.e2aa14b and2d037e0: generated locks plus matching input pins only.

Earlier deployed feature history stays intact. No default-branch merge/archive/
delete is authorized. Relevant labels were reviewed by the root agent using the
workspace writing skill before committing.

## Quick verification before review

- Full Go suite passed: repository7.722s, web27.742s and every package green.
- Backend parent/durable checks after final simplification passed0.630s/1.147s.
- Review-related repository/web race checks passed6.125s/6.939s.
- Actual Chromium component acceptance passed all21 checks using final UI and
  previously packaged unchanged editor/worker assets. Covers tree keyboard and
  collapse/history, exact clipboard, colors, arrows, root/merge-parent links,
  existing frozen anchors/versions/CSP/mobile and8-file editor bounds.
- Parent-only intermediate commit also passed its component acceptance.
- JS parse and committed-range whitespace checks pass. Workspace deployment
  contract (Ruby, Nix tools) passes3 tests/14 assertions.
- Upstream master fetched explicitly; runtime/organization heads already include
  them. Workspace rebase proved identical old patches. Final CI is running.

No long manual integration/package/live tests have started. Candidate live script
is being prepared but awaits review reconciliation and deployment. Last deployed
profile remains30 (8a2c8nb). Browser command uses nix shell --inputs-from .
nixpkgs#nodejs and cached Playwright/Chromium, CODEX_WEB_SOURCE and unchanged
REVIEW_ASSETS_DIRECTORY; backend checks use go/git/gcc through the flake's Nix
inputs. Existing test sources provide invocation instructions.

## Risk and compatibility

High: deliberate widening of commit-detail selection within the recorded Git
ancestry, additive API and downstream deployment. All four lanes apply.
Trust boundary: local operator trusted to administer host; remote clients remain
untrusted. Preserve scope and object-ID verification, no alternate revision syntax
or arbitrary refs/objects. Tests include scope, unrelated/newer SHA, missing
objects, root/merge and cold service restore after both branch/default ref movement.

Old clients ignore parents. Old packages retain canonical/private state readability;
ancestor links outside old feature range report unavailable after rollback until
rollforward. No migrations/coordinated node updates or real live rollback required.
No new external dependency to assess. Existing missing-object, preview/timeout and
retention limits remain; no retention or repository-browser framework expansion.

Write report to tree-review-<lane>.md under this initiative. Order findings by
Blocking/Important/Advisory; cite files/commits and concrete evidence. If none,
state that with remaining test gaps. Do not edit project code or tracking state.
