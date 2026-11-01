# Independent final review: stable Codex mode refresh

Read plan.md, state.md, branch-inventory.md and final-heads.json here. Inspect
all three complete committed base-to-head series and final diffs, plus relevant
code and project instructions directly. No uncommitted deliverable changes.

User outcome: no replacement of confirmed mode by Checking mode during ordinary
metadata refresh or returning to an inactive tab. Explicit mode buttons remain
usable (user decision). Existing shared notice policy owns initial loading and
continuous-visible warning grace. Fresh server metadata/generation remains
required for plan-dependent actions. Thread replacement clears retained display.

The reusable owning component is dev-workspace's custom portal browser. It uses
codex-web's existing createRefreshNotice/refreshPolicy at pinned 7aff163; neither
that API nor its generic mount is changed. Workspace composition consumes the
runtime through the nested vpsfree-dev-workspace/dev-workspace input; host
configuration consumes the same runtime through devWorkspace in the existing
dev-workspace confctl channel. Extension revision, sibling inputs and native
Codex version/launch policy are preserved.

Quick checks: JS syntax checks for app.js and the new browser regression pass in
the runtime Nix environment. TestShippedBrowserClientMatchesSessionAPI passed
(1.068 s, then 1.085 s after the plan-generation guard). Git diff --check passed.
Matching lock identities and deployment contract passed. Configuration checkout,
pre-commit Nixfmt and commit-message hooks passed through its Nix shell.
Long browser and packaged checks have not been manually started and must follow
this review. Source publication automatically started GitHub CI. Superseded
run cancellation was attempted but the current GitHub token refused with 403;
only final-head results will count.

High overall risk classification because the deliverable includes cross-project
application/host selection, mixed browser versions and live package deployment.
Review general, architecture/repetition, scope/proportionality, and risk/compatibility
lanes, reading every skill lane reference in full. The implementation itself is
a bounded UI-only fix. Trusted local operator boundary applies; remote clients
remain untrusted. No auth, HTTP/protocol, schema or persisted-state changes.
No migrations, including no transitional migration versions.

Documentation: dev-workspace/docs/workspace-portal.md owns lasting mode behavior
and current refresh contracts. Existing profile-switch and deployment guides
were checked. Exact live rollout evidence will be recorded here separately.
No KB content/publication or other controls are in scope. No generic settings
framework, new persistence, changed freshness budgets or native Codex upgrade.

Deploy the matching host configuration on aitherdev from the feature branch,
then use the composed workspace user-profile package via stable workspace-host
switch. Preserve live native/tmux identity and obey transition refusals. Do not
stop other sessions to unblock deployment. Package recovery is forward-only
with a corrected newer package. No default-branch integration is authorized.

Selected standalone reviewer: installed default-development-team's sole/first
review-purpose role reviewer, gpt-6-astra / xhigh, catalog digest
437585347ac8b2cdbf498a169d8871e684f3f61ccf1dd48e8589d79ef9629abd.
Fallback reason: session intentionally started --no-codex and has no retained
roster or native lead; team-list reports no valid lead rather than a reviewer.
The parent directly owns application edits under the ordinary no-roster rule.

Return severity-ordered concrete findings with file/line and commit evidence.
Explicitly conclude whole-branch history cleanliness, stream consolidation,
and migration lineage, including no migrations. Also state residual test gaps.
Remain read-only; do not launch nested agents, tests/builds, or deployment.
