---
lifecycle: active
---

# Portal review experience

## Current status

The approved follow-up is implemented, committed, reviewed, pushed and deployed
to aitherdev as user profile 30. All final CI, package and browser checks pass.
The deployed package is
`/nix/store/8a2c8nbpkfig5vc71jl5ir4wbxpxqkpr-dev-workspace-0.2.0`.
See follow-up-verification.md for exact results, commands, limits and screenshots.
This is a consolidated handoff of the deployed follow-up for user review.

The initiative remains active: all feature branches are unmerged and retained,
and the session stays open for follow-up. No merge, archive, delete, branch
removal or system-configuration change was performed. Shared coordination
checkout remains on master; preserve unrelated changes.

Stable portal:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-09-12-portal-review-experience/

## Session and repositories

Session slug: `2026-09-12-portal-review-experience`.
Workspace: `/home/aither/workspace/ai/vpsfree.cz`.
Shared thread: `01a09541-d1ba-7e32-a634-6f915c2da0a4`.
Initial tracking commit: `e0d3dee`; baseline deployment checkpoint: `2a83eff`.
Explicit approval reused this initiative after shell environment was lost.
Setting DEV_SESSION_SLUG and DEV_SESSION_WORKSPACE to the recorded values makes
`dev-session current` match. `dev-session url <slug> --as-is` confirms the link.

All branches are named `2026-09-12-portal-review-experience`. Worktrees remain in
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/`.
All four are registered in portal.yml, clean and pushed over SSH.

| Project/worktree | Final head |
| --- | --- |
| codex-web | de83e9c72dec6cb5ff8ec13d5b0b21ed60148117 |
| dev-workspace | 820277e6cc3aa7ff9acb0396feb3314e7f84996a |
| vpsfree-dev-workspace | ee9c55b3c25fd0b0002b3ce4796167d27378cd3a |
| workspace | 082c4c920f80ac8ef882bb59647bada4324094ce |

Upstreams were fetched before final feature pushes and had not advanced.
The workspace feature rebased onto coordination master 2a83eff with its two
previous feature patches unchanged. Initial repository bases remain in portal.yml.
Follow-up ranges and the source-identical runtime commit reconstruction are in
follow-up-review-packet.md and follow-up-series-reconstruction.md/json.

## Delivered follow-up

- Accepted steers appear immediately above the composer and survive same-tab
  reload until their exact message ID and digest appear in the transcript.
  Queue deletion remains separate. Waiting says "Waiting for instructions".
- Shared accessible copy icons copy Codex Markdown, full commit hashes and
  comparison links. Commit lists use subject/ellipsis/arrow controls; details
  show the full commit message. The branch action says Compare.
- Comparison totals and each file show changed-file/line counts and change
  status. Split, unified and whole-file Before/After views have language syntax.
- Frozen URLs identify comparisons, commits, files, layout, file version and
  old/new source lines. Direct navigation, Back/Forward and hidden context work.
- Registered lookups avoid broad workspace discovery. Batches, first-file
  previews, bounded immutable caches and coalescing reduce repeated Git work.

Native Git is retained. Maintained Shiki 4.4.3 joins CodeMirror as a bundled,
same-origin worker using its JS regex engine. No diff2html, CDN, WASM or eval.
Dependency maintenance and rejected alternatives are in follow-up-plan.md.

## Review and verification

All four mandatory lanes used fresh gpt-5.6-sol reviewers at xhigh. Every
Blocking/Important finding is resolved. Fixed editor retention, eager asset
loading, logical-line boundary, added/deleted URL normalization, license
whitespace and independently reversible commit ordering. Accepted small helper
API and durable-record retention advisories are documented in
follow-up-review-reconciliation.md. No unresolved implementation blocker remains.

Provider and runtime Go/contracts, focused race checks, seven packaged editor
tests, fifteen actual Chromium component checks and all committed-range
whitespace checks pass. Runtime full Go verification used GOWORK=off.
Runtime, organization and workspace `nix flake check --print-build-logs` pass.
The host-module VM passed in 193.93 seconds with a substituted kernel. The exact
site `nix build` passes; expected existing Ruby skips are recorded in the report.

Full-handler Firefox acceptance with controlled Codex RPC passed immediate
steers, reload without resending, exact observation, acknowledgement-failure
recovery, native clipboard, copy errors and waiting time. The private fixture
was removed; useful evidence is under artifacts/follow-up/.

Live Chromium checks passed branch/commit views, syntax, full-file Before,
reload at an old-line anchor, full-hash clipboard, full messages, unified,
read-only behavior, desktop/mobile layout and zero CSP/page errors. Root inspected
all three screenshots. Two initial harness selector/fixture mistakes were
corrected after diagnosis; no product change was needed.

Live TLS/authentication, assets and exact conversation identity checks pass.
Direct repository-state median improved from 615.8 ms to 24.98 ms (95.94%),
exceeding the 75% target. HTTPS metadata median is 429.20 ms; authentication/
proxy/TLS overhead remains. This is not a whole-page loading improvement claim.
Branch plus preview took 102.12 ms direct/402.99 ms HTTPS; commit first-open
78.58/388.14 ms and repeat-open median 18.28/384.19 ms. Full samples are retained.

Final CI passed: provider 34707084076, runtime 34708694751 and organization 34708731240
(including devcluster). The workspace has no matching workflow. No superseded
queued/in-progress run remains. Exact links are in follow-up-verification.md.

## Deployment, compatibility and cleanup

`workspace-host switch --source <initiative>/workspace` installed profile 30
through normal runtime/cluster/generation and Codex preflights. Router, portal,
Codex and tmux user services are healthy. Installed Codex remains 0.154.0.
Previous profile 29 retains
`/nix/store/prpvck3v35xbvyz60gfwprz9p3lsagal-dev-workspace-0.2.0`.
No live rollback or forced interruption was attempted for this follow-up.

Canonical session/lifecycle/journal formats are unchanged. New private comparison
descriptors are additive and older packages ignore them. They deliberately have
no automatic expiry; missing Git objects show an unavailable result and are not
fetched/pinned solely to preserve links. Blob/syntax/cache/editor limits remain
bounded. Full behavior and compatibility decisions are in follow-up-plan.md.

The detached series-reconstruction worktree and private conversation fixture are
removed. Root removed 22 owned temporary files/directories and GC roots after final
acceptance and checking process references, including ignored node_modules/dist. Registered worktrees, all branches and the installed profile remain.

## Previous delivery and retained limitations

Profile 29 delivered the larger question layout with fixed actions, immediate
new/fork/plan-new navigation and initialization progress, two-column repository
histories with local comparisons, typed web-search/subagent events, root-turn
message/tool counters, working/closed-wait/current-wait timing and Messages as
the initial filter. Its detailed evidence remains in packaged-validation.md,
conversation-browser-verification.md, repository-review-verification.md,
creation-integration-results.md, deployment-results.md and ci-final.json.

The earlier real blocking-question check proved waiting observation; answering
after its isolated portal reconnected was unverified. Controlled answer tests
passed. A large-history missing-cwd lookup timeout and private Plan-mode reconnect
inconsistency are documented in creation-integration-results.md. No shared Codex
settings were changed. Timing without complete observation stays unclassified;
retained timing/descriptors have documented scaling limits. Those prior limits
are not claimed resolved by this follow-up.

Next action: user review of the deployed follow-up. Keep the initiative active
and open; do not merge or archive without an explicit request.
