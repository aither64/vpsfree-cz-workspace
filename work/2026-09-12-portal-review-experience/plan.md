# Portal improvements with CodeMirror Merge

## Goal and decisions

Implement the user-approved portal plan: larger question panels with always-visible
actions; immediate navigation with initialization progress for new, forked, and
implementation sessions; local commit and branch review; typed search and subagent
events; per-turn counters; accurate recorded working/user-waiting durations; and
Messages as the initial conversation filter.

The user authorized implementation and subagents. Implementation sessions preserve
the exact accepted plan. Fork timing excludes inherited history. Blocking questions
and approvals count as waiting; nonblocking questions do not. Completed waiting
intervals accumulate; the current open wait is separate. Missing historical or
offline observation is unclassified, never silently counted as working.

## Affected repositories

- codex-web: optional typed activity presentation and observation/statistics APIs.
- dev-workspace: portal UI, background creation, local Git review, activity monitor.
- vpsfree-dev-workspace: pin the tested generic runtime.
- workspace: consuming package pin and deployment verification.

All feature branches and worktrees use 2026-09-12-portal-review-experience. Project
worktrees live below worktrees/2026-09-12-portal-review-experience/. The shared
workspace checkout stays on master; reusable workspace changes use its own worktree.

## Repository review and dependencies

Use native Git through a bounded Go reader; no go-git or libgit2 dependency.
Two repository cards per desktop row, one on narrow screens. Commit subjects and
GitHub links appear by default, message bodies expand, and history pages contain
50 commits. Include unpushed local commits. GitHub Actions loads independently.

Open comparisons in a full-width Repositories view with files on the left and
comparisons on the right. Split is the remembered default. The user accepted
CodeMirror's standard numbering: both versions in split; current-file numbers and
unnumbered deleted-text blocks in unified. Use read-only MergeView and
unifiedMergeView, disable editing/merge controls, collapse unchanged stretches with
three context lines, and mount files on demand. Bound large blobs and deletion
blocks. Preserve rename/binary/mode/symlink/submodule/newline metadata.

Git supplies trusted before/after blobs and comparison metadata; CodeMirror computes
displayed text differences. Resolve immutable base/head identities for each view.
Use the merge base with the locally available default ref during development. Save
viewed comparisons; retain the latest saved pair for an integrated exact head.
Fallback to the original recorded base with an explicit label. Archived views use
the canonical repository and recorded final head without a worktree. Preserve
expanded messages and scroll/selection through status refresh; explicitly refresh
an open comparison when its branch changes.

Pin @codemirror/merge 6.12.2 and the complete dependency graph, bundle locally with
maintained esbuild through Nix, retain licenses, and lazy-load assets. Use the
supported CodeMirror style nonce under the existing CSP. Maintenance was checked
on 2026-09-12: merge released 2026-06-09, view/state released September; CodeMirror
moved to Forgejo in April. The eleven-package runtime graph has no deprecated
packages; its oldest small keyboard-name utility released in 2023. diff2html was
rejected for intermittent maintenance (last release/default commit 2026-01-31).
Pierre is active but was not chosen after finding a dormant cache dependency in
worker/editor integrations. Monaco is maintained but adds editor infrastructure
and officially does not support mobile browsers.

Sources: https://registry.npmjs.org/@codemirror%2fmerge ;
https://discuss.codemirror.net/t/codemirrors-migration-to-forgejo/9706 ;
https://github.com/evanw/esbuild/releases .

## Session creation and conversation

Persist private creation receipts after bounded local validation and immediately
return the final URL (303 new form, 202 JSON fork/plan-new). Render progress before
manifest discovery, polling each second. Workers perform slow validation and
existing journaled CLI initialization with unchanged identity/lock/generation
checks. Matching duplicates reuse receipts; recovery proves success or offers
explicit retry. Preserve exact plan/source/settings and fork completion evidence.
Do not enable conversation mutations before initialization is ready.

Give question content more height and keep Back/Next/Submit outside its scroll
region. Preserve drafts, validation, keyboard and snooze behavior. Set Messages in
both initial HTML and JS. Normalize webSearch, collabAgentToolCall, and
subAgentActivity with safe links, readable summaries and expandable details shared
by portal and standalone renderer. Do not authorize arbitrary child thread links.

Count distinct assistant messages and actual tool invocations in the current root
turn, independent of filters; exclude outputs/lifecycle markers/child tools. Use
server turn times. A browser-independent observer records the union of blocking
question/approval/permission waits without responding or changing request policy.
Persist identities, boundaries and coverage only, not prompts/answers. Accumulate
known work and closed waits, reconstruct between-turn gaps from all paginated turn
metadata, and show live open wait separately. Fork lineage determines own turns.
Observe terminal resolutions, reconnects, cancellations and overlapping requests;
unobserved intervals stay unclassified.

## Interfaces, compatibility and delivery

Add pre-manifest /api/sessions/{slug}/creation status/retry, session-scoped local
repository review endpoints, and optional read-authorized /codex/{id}/activity.
Preserve public client source compatibility and existing transcript fallback fields.
Validate consumed protocol fields against schemas from the exact selected Codex.
Keep that Codex version unchanged. New private receipts/comparisons/activity ledgers
are separate from existing strict manifests and journals, so old packages ignore
them. No database/schema migration, node protocol, generated node config, or
coordinated machine update is required. Test additive-state upgrade and rollback.

Delivery order: codex-web -> dev-workspace -> organization extension -> workspace
user-profile package. Build/deploy from feature worktrees; no system configuration
change. Keep feature refs and session open; do not archive/delete without a request.

## Verification and review

Focused Go, Ruby, JS/browser checks precede committed adaptive review. Apply all
required review lanes with fresh gpt-5.6-sol/xhigh reviewers before long integration
tests. Fix/reconcile findings, then packaged Nix checks, live browser/App Server
validation, CI and package upgrade/rollback. Use writing skill before interface
text commits and handoff skill after checkpoints.

Cover question geometry at desktop/short/mobile/zoom; creation slow-helper latency,
duplicate/stale source/plan/retry/crash/generation cases; Git rebase/merge/fallback,
unusual paths, missing worktrees, binary/nontext/large data, split/unified and CSP;
timing blocking vs nonblocking/overlap/terminal/replay/browser absent/restart/missing
history/more-than-20-turn/fork/revert cases. Verify local-only dependency assets and
reproducible bundle. Retain useful concise evidence in state/artifacts.
