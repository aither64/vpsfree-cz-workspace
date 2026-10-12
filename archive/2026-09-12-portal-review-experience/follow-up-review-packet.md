# Follow-up implementation review

## Outcome and boundaries

Implement the approved follow-up in follow-up-plan.md: visible accepted steers
until exact transcript observation, waiting text and icon copy controls; faster
local repository history and commit details; compact commit actions and complete
messages; syntax-highlighted split/unified/full-file views; comparison/file
statistics and statuses; durable exact-revision links through commit, file, view,
version and old/new line anchors, including cold load and browser Back/Forward.

The user chose frozen revisions for shared links and comparison-only statistics
(no per-commit statistics on the overview). Keep native Git and CodeMirror.
Shiki 4.4.3 is maintained (official release 2026-08-10, active 2026-09-11) and
bundled with its JS regex engine. diff2html was not selected. Pierre Diffs was
rejected because its output and theme handling do not satisfy the portal CSP.
Stock CodeMirror unifiedMergeView loses independent old/new syntax context, so
the unified view projects public Chunk.build results into a read-only EditorView.
No vendor fork, Git framework, CDN, WASM, eval, new icon library, mutable refs in
links, Git object retention, automatic fetch, editing or merge capability.

This is the existing initiative 2026-09-12-portal-review-experience. Tracking:
/home/aither/workspace/ai/vpsfree.cz/work/2026-09-12-portal-review-experience/
(plan.md, follow-up-plan.md, state.md). Shared master has unrelated working-tree
changes; reviewers must leave those untouched. Review directly; do not modify
production code, commit, launch subagents, or run long integration tests.

## Exact scope

All worktrees are under:
/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/
All branches are 2026-09-12-portal-review-experience.

| Repository | Base (exclusive) | Head |
| --- | --- | --- |
| codex-web | 83770217d63f2c206689d2c569e1c81950544504 | de83e9c72dec6cb5ff8ec13d5b0b21ed60148117 |
| dev-workspace | d3bfd0f5a7c419c9df0ed53aa5f1acb77f8e10c2 | ebc0e4a71b01e81d0d90a29b0ca7385a61b1bdd1 |
| vpsfree-dev-workspace | a30de6c62d2bcd1ff41ee48018c595140c6d4042 | 534d0f2c5530bbbbf36d8254d282a9945cef9bfc |
| workspace | 5dbe312b1edf6a4454c4e86ec06f68baa3b5f4b4 | 77ca31a5e3e5e4f44c907b34b0f30bd99aec6980 |

Workspace baseline is the equivalent of previously deployed 9edf553 after
rebasing its two existing feature commits onto current shared master 2a83eff.
Those two patches are unchanged; this review covers the final pin commit.
Baseline features were already reviewed/deployed as profile29. Do not reopen
unrelated baseline changes without a concrete regression in this follow-up.

## Commit series

Provider de83e9c adds the reusable accessible copy button, uses it for transcript
copy and documents the additive export. Runtime commits:

- 5bc5f02: accepted/observed receipt states, same-tab reload, exact digest handling,
  waiting label, query-aware tab navigation and shared helper wiring; accompanying
  browser contract tests and documentation.
- a10fcb6: repository view/navigation and public URL behavior; responsive styles,
  template copy, pure contracts and an actual Chromium component acceptance test.
- 8ad9f5e: native Git full-message and raw/numstat parsing, DTOs, fixture tests.
- b924a15: direct registration, discovery TTL, immutable cache/coalescing,
  bounded batches, inline first file, durable scoped descriptors and recovery
  tests. These are bundled because all routes share the same scoped snapshot
  lifetime and cancellation/admission/cache model; splitting implementations
  would require temporary duplicate lookup and response contracts.
- 5eeed4e: CodeMirror rendering and Shiki worker, limits/cancellation/queue/cache,
  syntax projection and browser line navigation. Build files, exact dependency
  lock, selected grammar/theme licenses and tests travel together so packaged
  deployments have the tested standalone bundles.
- ebc0e4a: matching provider Go/Nix/vendor pins. Organization and workspace
  commits are mechanical downstream exact-head pin propagation.

The UI commit precedes its backend and editor in the series; the final tree is
the deployable unit. Do not rewrite already deployed baseline history.

## Component contracts and consumers

codex-web owns conversation/assets/conversation.js. Its additive export is
createCopyButton({text: string|callback, getText?: callback, label?: string});
getText takes precedence. It returns the same accessible SVG copy/check/error
button used by createTranscriptCopyButton. The provider also ships a standalone
web demo/client. Runtime app.js imports this public module and supplies the
helper to mountRepositoryReviews; provider and runtime tests cover the contract.
conversation.js/css URLs use v=4 to avoid old 300-second browser caches.

Runtime owns native Git access, HTTP authorization, snapshot/descriptors, browser
routes, CodeMirror and Shiki. Existing single endpoints remain. New GET batch
endpoints repository-histories/states/files bound 8/32/4 entries; GET
repository-comparison restores a durable branch review plus optional full
commit SHA and issued file ID. Responses add review, full message, historyHead,
stats and optional first preview. Commit membership and file selection are
validated against the frozen pair. No caller-provided filesystem path or Git
revision is executed. Actual Git subprocesses and admitted requests each have
four slots; request deadlines include admission. Cache is 64MiB, with duplicate
work coalesced and cancellation after the last waiting client leaves.

New schema-1 descriptors are private additive state under
repository-comparisons/reviews, independent from old saved comparison records,
session manifests, lifecycle journals and Codex state. Scope binds tracking
directory identity, thread and repository registration. Archive rename retains
identity; replaced sessions/repositories reject old links. Missing objects fail
explicitly. No fetch or reference pin is attempted.

URL parameters: tab, repository, review, optional commit, file, view, layout,
version, with #old-L42/#new-L42. Real anchors support native open-in-new-tab.
Editor interface createReviewEditor returns {destroy, revealLine, ready}; plain
source renders immediately, syntax arrives asynchronously from a same-origin
worker. Full old/new sources tokenize independently. Eight mounted editors,
512KiB/12,000-line source limits, bounded worker pending/cache, hard8s timeout.
The grammar set includes Nix, Ruby, Go, JS/TS, shell, YAML, JSON, HCL and others.
Unknown languages remain readable plaintext.

Consumers found through imports/pins: runtime portal -> organization
vpsfree-dev-workspace.lib.mkPackage -> workspace flake deployment package.
Codex App Server protocol/version, schemas, cluster/runtime generations, system
configuration and public origin/auth configuration are unchanged.

## Verification before review

- Provider Go suite and shared browser contracts passed.
- Runtime focused Go web browser/API contracts passed with local provider through
  GOWORK=/tmp/portal-review-followup.go.work.
- Backend focused race suite passed: repository5.762s, web6.740s, session1.103s;
  scope/archive/replacement, restart/eviction, branch movement/missing objects,
  cancellation/coalescing/limits, unusual filenames, rename/binary numstats.
- Runtime Node --unit contract with explicit conversation module passed.
- Editor seven tests passed in final Nix asset build:
  /nix/store/lr547kgjsjnmgmxnhibk1mp5aga91l2r-workspace-repository-review-assets-1.0.0
  npmDepsHash sha256-1FxpNmLkv0o9MXQG/qbH7f59sYJkHHmsfW1gytAd0VI=.
- Actual Chromium component acceptance using real packaged editor and strict CSP
  passed: batched histories, full messages/copy, first preview reuse, frozen cold
  links, old/new collapsed line anchors, full-file versions, Back/Forward, stats,
  file status, branch movement notice, read-only and 2/1-column responsiveness.
  test/repository_browser.cjs retains the procedure; it mocks bounded API data.
- Workspace Ruby deployment contracts: 3 runs,14 assertions, no failure.
- Full runtime Go suite passed on ebc0e4a with the GOWORK above and pinned Nix
  Go/GCC/Git/Node/Ruby/tmux/OpenSSL tools: repository7.695s, session1.758s,
  web32.561s; remaining packages passed or cached.
- All source changes committed; git diff --check clean.

Long Nix package/VM and full-handler/live browser tests are deferred until review
findings are reconciled. Feature source was pushed to resolve canonical GitHub
pins; automatically triggered CI is feedback, not final acceptance. No follow-up
package has been deployed yet. New vendorHash is
sha256-6EnFgCX1+8LusBdlg/Yj8TVM785ZLOK/C7CEWRIlIBw=.

## Risk, compatibility and deployment

High risk because this adds persisted private state and cross-project/browser
contracts. All four lanes apply: general, architecture/repetition,
scope/proportionality, risk/compatibility. Each reviewer uses fresh context,
gpt-5.6-sol, xhigh, and performs its assigned review directly.

Local operator is trusted to administer the host per local AGENTS; preserve
ordinary scope, ownership, serialization and rollback checks without adding
anti-compromised-operator filesystem mechanisms. Remote clients are untrusted;
authentication, same-origin checks, issued identities, bounded data and Git/path
validation remain required. Old profile29 ignores new private records and can
load canonical persisted state unchanged. Rollout order is provider -> runtime
-> organization -> workspace user profile. Browser asset versions and atomic
profile package keep helper and consumer code coherent. No system config pins,
merge/default-branch integration, archive, delete or force interruption is
approved. Keep the session open after deployment.
