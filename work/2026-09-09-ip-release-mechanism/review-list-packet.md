# Campaign list invocation follow-up review

Initiative: 2026-09-09-ip-release-mechanism; tracking plan.md/state.md in this directory.
Repository: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-09-ip-release-mechanism/vpsadmin
Delta base: aa9ac1e3af0acde65e15fd2c9758d1613689fed0
Head: resolve the current branch HEAD after the completed amend; the only delta is in
webui/forms/ip_release.forms.php and tests/playwright/webui/specs/networking.spec.cjs.
Compare the two trees, not an ancestor range. The existing eight-commit series is retained.

The user reported a server error at ?page=ip_release&action=list in the running review
cluster. A real administrator browser reproduced the failed navigation. The page
selected a HaveAPI Client Action object and invoked it as a PHP function. The installed
Action class implements call(), not __invoke(); Resource::__call delegates to call().
The one-line fix uses $action->call with unchanged arguments and resource selection.

The existing campaign browser scenario started at creation, missing this entry point.
It now opens the initial admin list, checks a populated campaign list and detail link,
and checks the member list after real email login, including absence of the admin
create link and navigation to its own request.

No API, authorization policy, schema, accounting, locking, mail, node or shared PHP
client changes. No new abstraction or exception suppression. Admin and member resource
selection remains unchanged. A live read-only check now returns 200 for admin, CS member
and EN member, shows only each member's respective campaign and follows correct links.
The user's campaign/address decisions are preserved; no reseeding or services update is
part of this fix. The WebUI reads the initiative worktree live.

Quick checks: PHP syntax, JS syntax, diff whitespace and capacity PHPUnit test pass
(PHPUnit 13.3.4, one test/two assertions); all commit hooks must pass before this packet
is dispatched. Before this delta, all eight integration scenarios, a separate updated
browser run, actual API/NodeCtld confirmation checks and live smoke flow passed.
The new full browser scenario will run after review. Earlier results are in
review-split-results.md and review-form-results.md.

Risk: high conservatively because the list is the entry point for administrator campaign
operations and member request discovery. Four lanes, gpt-6-astra/xhigh. This fix is
read-only and restores existing role-scoped API calls. No persisted-state or mixed-version
contract changes, migration or node update. No new prose or documented control change;
current docs/ip-release.md already describes these lists. A mechanical KB exact pin update
will follow publication. Overlay 715c063396 is unchanged; KB currently243b158 pins the base.

Review this bounded committed delta and its test gap directly. Read the mandatory-change-
review skill and your lane reference; do not spawn subagents or edit code. Report findings
with severity, or explicitly none, and residual validation gaps.
