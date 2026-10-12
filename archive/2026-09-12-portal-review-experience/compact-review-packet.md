# Compact comparison layout review packet

Read compact-plan.md and state.md under this directory. User approved removing
all tree counts/copy controls, adding folder icons, and letting full commit
messages scroll with diffs while a compact toolbar remains visible. File-header
copying/counts remain; new comparison entry starts at details; explicit targets,
parent navigation and browser history work. No new dependency/framework is wanted.

## Ownership and revisions

Initiative: 2026-09-12-portal-review-experience. Workspace root:
/home/aither/workspace/ai/vpsfree.cz. Worktree group: worktrees/<initiative>/.
All four retained feature branches have the initiative name. Review only this
follow-up's ranges, inspect earlier source where needed for context.

- dev-workspace: 41c6d75e8f7cdea1e5cbced7d0106d072d56484d..e35cf0b0bfc343d5a4d476340980e06ac252396b
- vpsfree-dev-workspace: 6c98b3676a46c9a9c2830198eae9042b064a71e7..2a3f442263ea614173c7eb540c55542a9373b71a
- workspace: c6daa04a9cbf6ce8611c7ae38dcfc7c4cc7a5636..6f10c36642ecb290ee0699ecff965779f37b9702
- codex-web is unchanged at de83e9c72dec6cb5ff8ec13d5b0b21ed60148117.

The site predecessor c6daa04 is source-equivalent to deployed cd648e2: the four
prior pin commits were rebased onto coordination master f106e8c, and range-diff
reported all four unchanged. Runtime and organization already include explicitly
fetched upstream master. All current project changes are committed; no hooks
framework is declared. Site branch push uses an exact lease; no master integration.

Runtime owns repository-review.js/css and the component browser fixture. Native
Git/API handlers, editor bundle and shared codex-web copy API are unchanged.
Organization imports the runtime package and supplies extensions; site calls the
organization mkPackage with siteConfig. Only exact input URLs and generated locks
change downstream. This dependency direction and existing public interfaces stay
intact. Remote clients remain untrusted; the local operator is trusted per AGENTS.

## Commit structure and compatibility

Runtime 2414ffa: compact tree with matching browser assertions/docs.
Runtime e35cf0b: scrolling details, compact toolbar and implicit selection, with
matching browser assertions/docs. Separate organization/site pin commits select
that runtime. These are independent behavior commits; no unrelated refactor.

No new API, URL keys, schema, journal/private/canonical state, Codex protocol,
configuration options, Git fetch/retention or dependency changes. Old and new
packages accept the same URL/state formats. The first implicit file stays out of
the URL so ordinary commit reload returns to details; actual file selections and
old explicit links still identify a file. No migration or coordinated node update.
Normal user-profile deploy order is runtime -> organization -> site, after reviews
and package verification. No forced interruption, system config edit, merge,
archive/delete or branch deletion. Keep this initiative open for user review.

## Verification and review selection

Quick verification passed before this review:
- Actual pinned Chromium/Playwright component acceptance: 21 checks for the tree
  commit, then 23 checks for final UI with real CodeMirror/Shiki and shared copy
  controls. Covers a 70-line message wheel-scrolling away, fixed toolbar geometry,
  no implicit file query, Back to details, native folder/keyboard states, retained
  path clipboard/count colors, full-file and both line sides, parent/root/merge,
  mobile geometry/no horizontal document overflow, strict CSP, lazy assets and
  eight-file editor retention. Final test was run on final runtime code.
- Nix Node JS parse and whitespace checks pass. Workspace Ruby deployment contract
  passes 3 runs/14 assertions, zero skips/failures/errors. The separate pin-only
  consumer change does not need new functional tests; exact package/CI comes next.
- Browser tools/assets from prior acceptance had been garbage-collected; restored
  through pinned Nix inputs with task-owned outlinks. Initial mobile toolbar check
  exposed large generic button padding; scoped compact button sizing fixed it.

Risk classification High because exact downstream deployment pins/order and
rollback are in scope; the UI logic itself is bounded and reversible. Use fresh
standalone gpt-5.6-sol at xhigh for General, Architecture, Scope and Risk lanes.
All lanes apply due hand-written UI/selection logic and downstream package pins.
Run the assigned lane directly; do not launch nested reviewers. Write findings
with severity and exact references to compact-review-<lane>.md here, and report
to root. No mutating code fixes or deployments during review.

Manual full package and live browser acceptance have not started. A live harness
is prepared at compact-live-browser.cjs; screenshots/real line geometry and exact
installed source verification remain. Automated branch CI starts on push.
Previous extreme-directory-depth recursion advisory remains in tree-review-risk.md;
this follow-up does not change tree recursion/server limits. No 5,000-file stress,
shallow-repo or live rollback exercise is claimed.
