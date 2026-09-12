---
lifecycle: active
---

# Portal review experience

## Current status

All requested UI changes are implemented, reviewed, committed, pushed and deployed
to aitherdev as user profile 32. The exact package is
`/nix/store/8ivw1xqshnhk12qwgkvwwqql4jm5d851-dev-workspace-0.2.0`.
All four mandatory review lanes, exact-package checks, feature CI and all 27 live
browser checks pass. The user authorized merging into default branches after
completion. All four exact feature heads are now merged into remote master.
Provider/runtime default CI passed; organization default CI was still running
at the final observation. The user explicitly requested no wait for CI.
Cleanup is complete; active lifecycle is retained while that CI is unconfirmed.
See compact-verification.md, compact-review-reconciliation.md and
compact-integration-results.json.

Keep the initiative and all feature branches open for follow-up. No archive,
delete, session stop or branch deletion was requested. Shared coordination
checkout stays on master; preserve unrelated working-tree and index changes.

Stable portal:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-09-12-portal-review-experience/

## Session and repositories

Slug: `2026-09-12-portal-review-experience`.
Workspace: `/home/aither/workspace/ai/vpsfree.cz`.
Shared thread: `01a09541-d1ba-7e32-a634-6f915c2da0a4`.
Initial tracking commit: e0d3dee; profile 29 checkpoint: 2a83eff;
profile 30 handoff: 44cfd5f; profile 31 handoff: f106e8c.
The retained session was verified using matching DEV_SESSION_SLUG and
DEV_SESSION_WORKSPACE with dev-session current. No new session was created.

All feature branches are `2026-09-12-portal-review-experience`; registered
worktrees are under `worktrees/2026-09-12-portal-review-experience/`:

| Project/worktree | Exact final feature head |
| --- | --- |
| codex-web | de83e9c72dec6cb5ff8ec13d5b0b21ed60148117 |
| dev-workspace | dc8d6cf7628a6a8db240f2e11ad61e8bc31ddacd |
| vpsfree-dev-workspace | b37edd0f63fb7a984ba634c2d52d08e9344304b4 |
| workspace | 7985e127b55b48683457fdfe12a894e983d32890 |

All remain registered in portal.yml with retained local/remote feature branches.
Their clean worktrees were removed at the user's request after exact remote merge
proof. The paths above are historical locations, available for later recreation.
Upstream was fetched
before feature pushes. The site feature was rebased onto shared master f106e8c;
range-diff proved all four earlier pin patches unchanged. Source-equivalent prior
site head is c6daa04. No deployed or merged commit was rewritten.

## Delivered behavior

The diff navigator uses single-line filenames, colored status letters, ellipsis
and full-path tooltips. Native open/closed directory icons accompany keyboard
accessible disclosures. Collapse choices survive layout/version changes and
history/file navigation reveals the selected path. Tree rows have no statistics
or copy buttons; full file/diff headers retain colored statistics and path copying.

A compact fixed toolbar keeps repository/commit identity, navigation, comparison
link copying and Split/Unified controls. Full commit messages, author/date, hashes,
parents and comparison totals scroll away with the diffs. Messages have no
independent height cap or scrollbar. Initial branch/commit entry starts at details;
explicit file/line links reveal their target. Mobile retains the stacked tree.

Parent hashes open standard commit pages, including all merge parents and
ancestors before the feature base. Root commits show No parent; diffs remain
first-parent. Parent URLs clear file/view/version/line selection while preserving
the frozen review and layout. Full-file back arrows restore the exact comparison.

Earlier deliveries remain in place: accepted-steer receipts, Waiting for
instructions, icon copy actions, fast native repository metadata/cache/batches,
full messages, Shiki syntax with split/unified/full-file views, statistics/status,
and frozen commit/file/source-line links. Profile 29 supplied usable questions,
immediate session creation with initialization progress, local repository diffs,
web-search/subagent rendering, turn counters/timing and the Messages default.

## Compatibility, review and verification

Compact UI commits are 2414ffa and e35cf0b; test-only dc8d6cf removes a flaky 500ms
creation timing assertion. It proves response order while validation stays blocked,
with 5s deadlock guards. Twenty focused runs and five race runs pass. CI failure
34713657833 was investigated before changing the test, rather than rerun blindly.
See compact-ci-investigation.md and notes/dev-workspace/2026-09-12-creation-test-ordering.md.

This follow-up adds no dependency, API, URL key, state/schema/protocol or system
configuration change. Normal package switch and rollback remain compatible;
no coordinated node update or migration. The previous parents array is additive.
Older packages ignore it and report ancestors outside their old range as
unavailable until rollforward.

All four fresh mandatory reviewers used gpt-5.6-sol with xhigh effort. No Blocking,
Important or Advisory findings in the compact follow-up. General also reviewed
the CI test fix/final pins; Scope/Risk reviewed final full ranges. Reconciliation
preceded manual package/live acceptance. Prior tree scope finding (unwanted
view=diff on parent URLs) was fixed and reviewed before profile 31.

Actual Chromium component acceptance passed 21 checks for the tree commit and
23 for the final UI, including a 70-line message, toolbar bounds, native clipboard,
parent/root/merge cases, old/new anchors, keyboard/collapse/history, mobile, strict
CSP, lazy assets and eight-editor retention. JS parsing and whitespace checks pass.
Site deployment-contract Ruby checks pass 3 runs/14 assertions, no skips.

The exact final package passed full Go (repository 10.015s, web 30.566s), session
296 runs/2,979 assertions with 12 existing skips, host 73 runs/438 assertions with
3 existing skips, zero failures/errors. Check phase 2m14s. Site nix flake check
passed 3/14. Feature runtime CI 34713959840 and organization CI 34714047616 pass;
organization includes devcluster. All superseded runs had completed before
replacement pushes. No local kernel build was needed. See compact-ci-results.json.

## Deployment and live acceptance

Normal workspace-host switch from the site feature worktree installed profile 32.
Generation/runtime/cluster checks and Codex protocol validation passed; Codex stays
0.154.0. Router, portal, Codex and tmux services are active. The portal process's
actual executable matches package 8ivw1xq. Strict TLS/authentication smoke passes,
including unauthenticated 401 and exact shared conversation identity. Profile 31
retains package 4zjl93s. No forced interruption, system configuration mutation or
live rollback was used. See compact-deployment-results.json and
compact-live-smoke-results.json.

Final live browser acceptance passed 27 checks in 160.498 seconds on exact dc8d6cf.
It verifies tree/keyboard/icons, no tree stats/copy controls, retained header copy
and colors, cold diff/full-file line anchors/back arrows, parent new-tab/history,
complete messages and real wheel scrolling on desktop/mobile, lazy assets and
<=8 retained editors across 11 files. Zero page errors/CSP violations. Root
inspected screenshots; measured geometry and URLs are retained under artifacts/compact.
No live Git refs/conversation state were changed. Browser TLS errors were ignored
only within that context; independent strict TLS validation passed.

Two harness readiness errors were corrected: scrolling before lazy content gave
placeholder height, and waiting for all editors blocked on an intentional
offscreen placeholder on mobile. Wait for loaded syntax and sufficient scroll
range instead. Networkidle also cannot settle with SSE; use DOM readiness.
No product change was needed. Pinned browser/asset GC roots were restored for
acceptance. Reusable lessons are recorded under notes/dev-workspace/.

## Integration and cleanup

The user explicitly approved default-branch merges on 2026-09-12. Clean detached
target worktrees integration-codex-web, integration-dev-workspace and
integration-vpsfree-dev-workspace were created from freshly fetched origin/master,
then fast-forwarded to the exact reviewed feature heads. Provider packaged checks
and runtime full Go checks pass in those checkouts. The focused runtime shell
needed nixpkgs#gcc alongside Go for cgo; the complete shell passes. Organization
contract/source/Ruby checks passed: 224 runs/2,031 assertions, zero failures/errors,
one existing migration skip. The deployed exact package/feature CI
remain applicable to these unchanged Git objects.

The site was fast-forwarded from shared master f106e8c to 7985e12 without staging
any paths. Its post-merge nix flake check passed 3 runs/14 assertions, no skips.
All four remote master branches contain their exact final local/remote feature
heads; integration required no new feature commits or merge commits. Provider
master CI 34715291207 and runtime master CI 34715304238 passed, including activation,
renewal and rollback VM smoke. Organization master CI 34715439692 was still running
at the last observation; the user requested no further waiting. Workspace has no
matching Actions workflow. Final feature CI was already green for all components.

At the user's cleanup request, all four clean registered feature worktrees and
three clean integration worktrees were removed with non-force git worktree remove.
Local and remote feature branches are retained. The session/tracking remain open;
no archive, delete or stop was performed. Task-owned temporary browser/assets/build
outlinks, logs, diagnostic files and commit-message files were removed. Installed
profiles and curated evidence remain. One consolidated coordination handoff is
committed after integration and cleanup, preserving unrelated shared changes.

The organization bare clone had no remote feature tracking ref. A plain named
fetch populated FETCH_HEAD without supplying that absent ref; explicit source:
destination fetches established the exact remote master and feature identities
before removal. No removal occurred until every worktree passed the merge/clean
preflight. See notes/cross-project/2026-09-12-bare-fetch-integration-proof.md.

No user action is needed for the delivered UI. The organization CI result remains
unconfirmed by request; no delayed cleanup or automatic session closure is set.

## Preserved evidence and limitations

Profile 31/tree verification and reconciliation remain in tree-verification.md
and tree-review-reconciliation.md. Profile 30's direct metadata median improved
615.8ms to 24.98ms; HTTPS retained about 0.4s overhead. This is not a whole-page
latency claim. See follow-up-verification.md. Original creation, conversation,
protocol and packaged evidence remains in the original reports.

The existing recursive tree may exceed the browser stack for historical Git paths
thousands of directories deep. This accepted availability advisory is unchanged.
No real 5,000-file DOM stress, shallow-repository, live-rollback or already-open
browser package-switch coverage is claimed. Root/merge/status edge cases are
covered by component/Go fixtures rather than mutating live Git refs.

Earlier real blocking-question observation passed, but answering after its
isolated portal reconnected was unverified; controlled answer tests passed.
Large-history missing-cwd and private Plan-mode reconnect limitations remain in
creation-integration-results.md. No shared Codex settings changed. Unobserved
timing stays unclassified; private retention and missing Git object bounds remain.
