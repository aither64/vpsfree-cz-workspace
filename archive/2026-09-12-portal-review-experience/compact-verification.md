# Compact file tree and scrolling details verification

## Implementation

The file navigator shows one-line names with colored status letters and native
folder disclosures/icons. It contains no file counts, repeated totals or copy
controls. Diff headers retain colored counts and path copying. Commit/branch
details scroll with files; a compact toolbar retains identity/navigation/layout.
The full message has no independent cap/scrollbar. Implicit first-file selection
stays internal; file/line targets and Back/Forward retain explicit navigation.

Runtime UI commits are 2414ffa and e35cf0b. The independent test-only commit dc8d6cf
corrects an existing CI timing assumption. Final organization b37edd0/site 7985e12
pin that runtime. Provider de83e9c is unchanged. No dependency, API, URL keys,
protocol, canonical/private state or system configuration changes. Normal user
profile deployment/rollback remains compatible; no coordinated node update.

## Quick verification

- Actual Chromium component acceptance passed 21 checks for the standalone tree
  commit and 23 for final UI. It uses pinned Playwright/Chromium, CodeMirror/Shiki
  assets and shared provider copy controls. A 70-line message scrolls away while
  toolbar geometry stays fixed; commit/branch entry stays at details, Back restores
  details, and explicit files/old-new lines, parents/root/merge, full-file return,
  keyboard/folder state, retained header copying/counts, mobile/no overflow, strict
  CSP, lazy assets and eight-editor retention all pass.
- JS parsing and committed whitespace checks passed. Workspace deployment-contract
  Ruby tests passed 3 runs/14 assertions with no failures/errors/skips.
- Browser tooling and editor assets had been collected since the previous handoff;
  pinned Nix builds restored them under task-owned outlinks. The first mobile
  toolbar check caught default generic-button sizing; scoped compact sizing fixed
  it and all 23 component checks passed.
- Organization CI 34713657833 returned expected 303 from session creation but failed
  the previous 500 ms wall-clock assertion. The fixture keeps validation blocked,
  establishing asynchronous ordering. Runtime 34713615190 on the same UI passed.
  The test now uses a response channel and 5s deadlock guards. Twenty focused runs
  passed 0.546s; five race runs passed 1.430s. See compact-ci-investigation.md.
- All four final worktrees are clean; exact downstream lock revisions were checked.
  Runtime and organization include current fetched upstream bases. Site rebase
  onto f106e8c preserved all four prior pin patches exactly by range-diff.

## Review and acceptance status

All four mandatory lanes found no issues, including General review of the test
supplement and Scope/Risk review of final ranges. Exact-package and live acceptance
followed completed reconciliation. The live harness is compact-live-browser.cjs.
The previous extreme-depth recursion advisory is unchanged; no 5,000-file, shallow
repository or live-rollback claim is made.

## Exact package

After review reconciliation, site 7985e12 built package
`/nix/store/8ivw1xqshnhk12qwgkvwwqql4jm5d851-dev-workspace-0.2.0`.
Full Go tests passed, including repository 10.015s and web 30.566s. Session checks
passed 296 runs/2,979 assertions with 12 existing skips; host checks passed 73
runs/438 assertions with 3 existing skips. Zero failures/errors; check phase
2m14s. Site nix flake check passed deployment-contract 3/14, no skips. Final runtime
CI 34713959840 passed; organization 34714047616 passed its flake/package checks and
its devcluster check also passed. No local kernel build was started.

## Deployment

Normal workspace-host switch installed profile 32 with compatible Codex 0.154.0.
The actual portal process executable matches the built 8ivw1xq package, and router,
portal, Codex and tmux services are active. Ordinary generation/runtime/cluster and
protocol checks passed; no forced interruption or system-configuration mutation.
Profile 31 retains package 4zjl93s. Live acceptance passed against the new package.

The first live harness reached cold file/line links, header clipboard and parent
new-tab/history checks, then timed out measuring long-message scrolling. Its
screenshot showed both file editors still loading when it sent the sole wheel
event; the pane had only placeholder height and clamped the scroll. The harness
was changed to wait for real editors, syntax readiness and sufficient scroll
range. The second attempt passed desktop scrolling but exposed an overconstraint
in that wait on mobile: it required both editors although the second is outside
the lazy-load margin. A targeted measurement showed one loaded editor, 20,494px
scroll height, a 566px pane and 965px details, with the second section explicitly
waiting to enter view. The final helper waits for at least one loaded editor,
syntax readiness and sufficient scroll range. No product change was required.
The first diagnostic used networkidle, which cannot settle while the portal SSE
connection is open; domcontentloaded plus explicit DOM readiness was used instead.

## Live acceptance

The final browser run passed all 27 checks in 160.498 seconds on runtime dc8d6cf.
It covered compact one-line trees without counts/copy controls, folder icons and
native keyboard/collapse behavior, retained colored header totals/path copying,
syntax, explicit cold old/new diff lines and full-file links, exact back arrows,
complete messages at entry, parent new-tab/reload/history/older-than-base links,
long-message mouse-wheel scrolling on desktop and 390px mobile, lazy assets and
an eight-editor retention bound across eleven files. Zero page errors or CSP
violations occurred. Root inspected desktop, long-message before/after, full-file,
parent and mobile screenshots. The browser ignores certificate errors; independent
strict-TLS smoke passed. No live Git refs or conversation state were changed.
Frozen URLs and measured geometry are in artifacts/compact/compact-live-browser-results.json.

The user subsequently authorized integration into all four default branches.
Fast-forward results and post-merge CI are tracked in compact-integration-results.json.
Feature branches and the session are retained; no archive/delete is authorized.

All four repositories were fast-forwarded into remote master at the exact reviewed
heads. Clean integration checkouts passed provider packaged checks, runtime full
Go tests, organization source/config/host-contract and Ruby checks (224 runs,
2,031 assertions, one existing skip), and site flake checks (3/14, no skips).
Provider master CI 34715291207 and runtime master CI 34715304238 passed. Organization
master CI 34715439692 was still running at the last observation; the user explicitly
requested no wait. All four feature and three temporary integration worktrees were
removed cleanly after exact local/remote ancestry proof. Branches and session remain.
