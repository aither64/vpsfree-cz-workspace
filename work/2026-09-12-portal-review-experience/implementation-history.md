---
lifecycle: active
---

# Portal review experience

## Status

The approved features are implemented, committed and pushed on the initiative
branches. Current heads: codex-web 8377021, dev-workspace d3bfd0f,
vpsfree-dev-workspace a30de6c, workspace 9edf553. The runtime CI passes.
All mandatory review lanes completed, including a targeted architecture/risk
review of causal deletion identity with no findings. Real creation acceptance
found a goal-normalization mismatch; its narrow fix and targeted review are in progress.

Final package output is /nix/store/pwi8v7sgbjb92n7kgfkzh6pdrikf60y5-dev-workspace-0.2.0.
It is deployed as profile28 and passes installed Codex0.154protocol/model validation.
The retained previous profile27 is /nix/store/aamx7bqmg406w3zrfnvpd60knhrgps4s-dev-workspace-0.2.0.
Controlled conversation browser and generic flake/VM checks pass. Real creation
acceptance is ongoing. Live rollback was refused safely because another session is active; profile28 remains healthy. The current session is verified and remains open; no default
branches are merged. Shared root stays on master; preserve unrelated changes.

## Repositories and worktrees

Branch in each repository: 2026-09-12-portal-review-experience.
Worktree group: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience.
Repositories: codex-web, dev-workspace, vpsfree-dev-workspace, workspace.
- codex-web: base 269962eb65007581ba69c205634f9e6c14cc39d3.
- dev-workspace: base bcbaf825d71285cbbd05b56e78bc386f2df480bd.
- vpsfree-dev-workspace: base 0a9c974.
- workspace: base da639eb (upstream master); rebase on shared master before review.

Initial tracking committed as e0d3dee. All four worktrees are registered.
The session started with --as-is --goal-file and --no-attach. Its shared thread
is 01a09541-d1ba-7e32-a634-6f915c2da0a4. Stable URL:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-09-12-portal-review-experience/

Verified current-session lookup with both DEV_SESSION_SLUG and
DEV_SESSION_WORKSPACE set to this slug and the canonical workspace root.
Startup briefly reconnected its terminal after the App Server disconnected.

Implementation owners: root handles question layout, initial filter, portal
activity integration and delivery; implement_codex owns generic event/timing;
implement_creation owns asynchronous creation; implement_repositories owns
local Git review and the CodeMirror bundle. All use isolated initiative worktrees.

## Verification

- Planning inspections and dependency maintenance research were read-only.
- Focused implementation and remediation checks pass. Causal review, full generic flake/VM checks, controlled browser acceptance, installed Codex compatibility and profile28 HTTPS checks pass. Real creation acceptance and its goal-normalization repair remain in progress.

## Cleanup and next actions

Finish the real creation acceptance repair and targeted review; refresh consumer pins and package, then complete the same isolated fixture and deploy when the normal host preflight allows it. Curate results, remove only owned test fixtures/GC roots, and commit one consolidated tracking checkpoint. Do not interrupt concurrent work to force deployment or rollback.
Retain branches and keep the session open. No archive or deletion is authorized.

## Implementation checkpoint

- Root UI changes: Messages is selected in HTML/JS; pending questions sit outside
  the composer scroll container, with scrolling body and fixed action footer.
  Short viewports use a compact composer while answering. Plan-new captures the
  exact plan/settings when its dialog opens. CodeMirror style nonce and lazy
  repository mount hooks are connected.
- Service activity monitor uses a separate observer client and private recorder,
  owns only matching ready session authorities, subscribes without a browser,
  reconciles ownership every five seconds, debounces activity reads to one per
  second, and polls idle threads less often. UI separates work, completed waits,
  current wait, counts, and unclassified time.
- Implementation agents have creation receipts/worker/CLI evidence, local Git
  backend, and typed events/timing APIs in the shared feature worktrees.
  Repository UI now has stacked file diffs with lazy loading and navigation that scrolls.
- Quick checks: portal web Go suite passed (6.346s) using temporary Go workspace
  /tmp/portal-review.go.work to link the uncommitted codex-web API. Browser JS
  unit contract passed with current shared module. CSS geometry fixture passed
  at 1440x1000, 1280x720, 1024x600, 390x844, 390x600, and 780x422, including the
  timing summary. This was a focused CSS fixture, not full portal acceptance.
- Browser tools built from the selected nixpkgs: Firefox 155, GeckoDriver,
  Python/Selenium. Tool bundle is /nix/store/aklba75zn5fpld8y81ifqxx7j8vmj376-portal-browser-tools.
- During concurrent edits Nix temporarily could not see an untracked imported
  review-ui.nix, then found a string/path fileset mismatch. Use pinned
  `nix shell --inputs-from . nixpkgs#go nixpkgs#gcc nixpkgs#nodejs` for focused
  checks while packaging changes are incomplete. The repository agent fixed the
  path mismatch and is checking the reproducible assets derivation.
- dev-workspace feature commits: 4bc9e73 async creation, 664cfdc Messages default,
  d068b17 question layout, 060496a local Git review, 13f5cc6 typed event rendering,
  90feac1 service observation and timing UI. Provider/delivery pins are in progress.
- codex-web typed event commit d56ad40 and timing implementation are committed.
  First feature CI exposed a reconnect timing regression after a successful
  thread/resume response; the agent inspected logs and is correcting successful
  Subscribe acceptance while refusing stale activity coverage. Current provider
  head will be rewritten before dependent branches are pushed.
- Current pinned-provider portal Go ./... and browser unit contract passed again.
  Focused creation Ruby checks: 25 runs/239 assertions; Go race/syntax pass.
  Local Git browser harness passes split/unified, 30 stacked files/lazy loads,
  last-file scrolling, read-only behavior, two/one card layout, preserved expanded
  bodies and comparison scroll, and zero CSP violations. See separate evidence.
- Canonical extension fetch needed an explicit master refspec: generic `fetch`
  had refreshed only FETCH_HEAD. Rebased extension on c4df383 and workspace on
  shared master e0d3dee. Their upcoming changes are delivery pins only.
- Only feature branch focused CI is being run before review; dev-workspace VM
  workflow does not run on ordinary feature pushes. Long VM, live App Server,
  browser acceptance and deployment remain after mandatory review.

## Exact reviewed commit ranges

- codex-web: `269962eb65007581ba69c205634f9e6c14cc39d3..bba2ae1d9796dc7267c0bfc5ee9f072f43d6e92e`
  Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/codex-web`
- dev-workspace: `bcbaf825d71285cbbd05b56e78bc386f2df480bd..774c2083333b9b71d4abb04d4aa7c79ea0aa897d`
  Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/dev-workspace`
- vpsfree-dev-workspace: `c4df3838de8b42083bd43e86bfdff7d45a7e952f..d0ebe39e4cc2e41cb791ad048c60eb1e940c023e`
  Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/vpsfree-dev-workspace`
- workspace: `e0d3dee52ac637a96a7d73299aecd753759b484b..bfc80f25864528b5b954daf84c6e8a7d4a8348c7`
  Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/workspace`

- All intended code and delivery pins are committed; all four worktrees clean.
- codex-web Check CI passed at bba2ae1, runtime fast CI passed at774c208; VM skipped.
- Mandatory review classified HIGH for persistence/protocol/recovery/rollback.
  Four fresh standalone gpt-5.6-sol/xhigh lanes: general, architecture, scope, risk.
  Packet: review-packet.md. Reviews starting; long integration remains pending.

- Collaboration spawn capacity refused a third fresh reviewer even after the
  planning agent completed. Risk lane runs as a fresh ephemeral standalone
  `codex exec -m gpt-5.6-sol -c model_reasoning_effort=\"xhigh\" -s read-only`
  with only the packet prompt; output goes to review-risk.md. General and
  architecture use fresh collaboration agents. Scope will run when capacity
  is available, with the same model/effort and fresh context. No lane is omitted.
- Current retained user-profile output before delivery:
  /nix/store/aamx7bqmg406w3zrfnvpd60knhrgps4s-dev-workspace-0.2.0.
  Router, portal, App Server and tmux units were active before delivery.

## Review findings in progress

- General and architecture independently confirmed Important: completed creation
  receipts have no retirement path and consume a512 lifetime cap, eventually
  rejecting new requests. Fix required before deployment/integration.
- General confirmed Important candidate: Git diff -l1000 can silently skip
  exhaustive rename detection for supported comparisons up to5000files. Preserve
  metadata or explicitly report bounded unavailable/degraded review; fix pending.
- Risk lane is still examining source/journal recovery. Architecture is examining
  activity-ledger lifetime/contention. These are not yet reconciled findings.
- Root prepared artifacts/conversation-browser-fixture.go and browser-check.py
  for real handler/asset UI acceptance with controlled protocol responses. Not run.

- General review complete:0Blocking,2Important (receipt retention and rename
  detection). Architecture complete:0Blocking,3Important (receipt retention,
  ledger lifetime/global rewrites, global history/snapshot contention),1Advisory
  (duplicate typed-kind whitelist / exact-pinned export optional probe).
- Root narrow fixes committed as fixups, pending final autosquash/pin cascade:
  only ready receipts may retire at capacity (pending/failed/paused retained);
  restart/cross-capacity/old-destination protection/attempt identity regression
  passes. README documents bounded completed-receipt retry cache.
  Git uses-l0 and existing4seconddeadline;1001modified-renames regression passes
  in1.164s. Test disables auto maintenance after a reproduced temporary-directory
  cleanup race (durable note recorded). Portal calls exact-pinned shared export
  directly. Creation suite passes2.700s.
- Provider agent owns activity storage and synchronization remediation without
  new dependencies. New undeployed persistence design will receive affected-lane
  review after commit; no compatibility shims for earlier unmerged iteration.
- Scope review runs fresh ephemeral codex exec gpt-5.6-sol/xhigh, output
  review-scope.md. Risk review remains running; no long integration begun.

- Risk review complete (fresh standalone CLI, exit0):1Blocking,4Important,
  1Advisory. Blocking is prebinding receipt/oldpackage same-slug creation/
  rollforward shadowing a valid session. Additional Important: established
  forkjournal recovery incorrectly requires an active source. Retention findings
  also include deleted readyreceipt slug reuse. Other findings duplicate
  rename/ledger/history synchronization; retain architecture's Important severity
  for shared locking based on readloop eventcapture impact.
- Creation owner now fixes mixed-generation conflict handling, exactforkjournal
  recovery after source archive/delete, and readyreceipt lifecycle retirement.
  Root retains bounded-cache fix; no concurrent edits to creation files.
- Provider repair design accepted: private per-thread storage, bounded hot
  checkpoint/current outstanding requests, immutable compact per-turn summaries,
  per-thread coalesced durablewrites outside readloop locks, per-thread cancellable
  history synchronization and linear aggregation outside recorder lock. No new
  dependencies. Historical archived timing remains available; unknown coverage
  and fork/revert identity remain authoritative. Detailed delta review required.
- Organization Check CI success at d0ebe39:
  https://github.com/vpsfreecz/dev-workspace/actions/runs/34691604197.
  Includes focused flake and installed-runner evaluation checks, no VM startup.

- Scope review complete:0Blocking,3Important (retention, ordinary transcript
  fullhistory, rename metadata),1Advisory (unusedclosedrequestregistry).
  Fullhistorypayload finding is accepted: provider restores latest20 transcript,
  keeps complete timing metadata internal and removes unused publicturnarrays.
- All initial review lanes complete. Consolidated distinct findings and current
  ownership are in review-reconciliation.md. No initial finding is waived.

## Review remediation verification

- Provider repair folded into typed commit0522aa2 and timing commit4dde3c6.
  Full Go and race suites, browser contract, exact0.154experimental protocol
  validation pass. Stress covers25,000requestcycles/250turns, durable restart
  totals, stalled writers/history RPC isolation and resumable pagination.
  Exact feature CI passed: https://github.com/aither64/codex-web/actions/runs/34693913115.
- Runtime pins now select v0.0.0-20260912123014-4dde3c6aaa1d and matching Nix
  source. Fresh vendor derivation gives
  sha256-TXo4Wd1OI7+voHwR8InNxlu/P9fCwvn1LyYbyl8MHO4=.
  Full portal Go packages and browser unit contract pass against this exact pin.
- Creation owner committed explicit conflict reconciliation, lifecycle-aware
  terminal cache retirement, deleted slug reuse and established fork recovery.
  Full web race17.949s and Ruby26runs255assertions passed; adjacent binding-before-
  journal rollback regressions passed8.336s. An additional exact fork binding
  without journal/evidence was confirmed unrecoverable and receives a narrow
  conflict regression before final commit folding.
- Prepared actual packaged four-thread creation harness and controlled handler
  conversation browser harness. Neither has run; long acceptance waits for
  required delta reviews. No deployment or default branch integration performed.

## Remediated committed ranges

- codex-web: `269962eb65007581ba69c205634f9e6c14cc39d3..4dde3c6aaa1d038c518563762fa7ac480b650cd2`
  Original reviewed to final tree: `bba2ae1d9796dc7267c0bfc5ee9f072f43d6e92e..4dde3c6aaa1d038c518563762fa7ac480b650cd2`.
  Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/codex-web`.
- dev-workspace: `bcbaf825d71285cbbd05b56e78bc386f2df480bd..40837d245e867aa0edd35f59f72b63bba80034d1`
  Original reviewed to final tree: `774c2083333b9b71d4abb04d4aa7c79ea0aa897d..40837d245e867aa0edd35f59f72b63bba80034d1`.
  Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/dev-workspace`.
- vpsfree-dev-workspace: `c4df3838de8b42083bd43e86bfdff7d45a7e952f..4e03a3f0a3fd439ae2c645ab41fa736051c5b8c9`
  Original reviewed to final tree: `d0ebe39e4cc2e41cb791ad048c60eb1e940c023e..4e03a3f0a3fd439ae2c645ab41fa736051c5b8c9`.
  Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/vpsfree-dev-workspace`.
- workspace: `e0d3dee52ac637a96a7d73299aecd753759b484b..ea6cc34a303dc2c8d9027f109a2212d1ebea02c5`
  Original reviewed to final tree: `bfc80f25864528b5b954daf84c6e8a7d4a8348c7..ea6cc34a303dc2c8d9027f109a2212d1ebea02c5`.
  Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/workspace`.

Vendor hash: `sha256-TXo4Wd1OI7+voHwR8InNxlu/P9fCwvn1LyYbyl8MHO4=`.
Creation final narrow fork boundary race regression passed8.730s.
All four code/pin worktrees are committed and clean. Runtime autosquash
resolved only README context and preserved exactly the tested final tree.

All four affected lanes will rerun on the committed design delta. No initial
finding was waived. Long integration remains pending.

- Remediated runtime40837d2 exact feature CI passed:
  https://github.com/aither64/dev-workspace/actions/runs/34694116427.
  No superseded runs remain queued/running on provider/runtime branches.
  Organization4e03a3f CI is still running.
- Final consuming package derivation evaluates; organization checks.package
  evaluates. Extension intentionally exports a package constructor and has no
  packages.default; use checks.package for its fixture derivation.
- Controlled browser fixture compiled in an isolated archive of runtime40837d2
  against its real provider pin (no tests run yet, no project files changed).
- Before deployment, exact existing units workspace-router, workspace-portal@vpsfree-cz,
  workspace-codex@vpsfree-cz and workspace-tmux@vpsfree-cz are active. HTTPS with
  retained CA: unauthorized401, authenticated /healthz200 and initiative200.
  Credentials read only in process memory; no values copied to notes or output.

- Prepared consuming package output (evaluation only):
  /nix/store/6w5ba2pf6w4shswach7r3gd4wi58d3a0-dev-workspace-0.2.0.
  Prior retained package remains
  /nix/store/aamx7bqmg406w3zrfnvpd60knhrgps4s-dev-workspace-0.2.0.
- Creation harness inspection corrected four assertions to the actual public
  userMessage entry kind before execution. It uses a transparent fixture-local
  Unix relay, keeping submission retry ledgers private; no auth credentials
  are copied. Four intended fixture threads, no model calls have run yet.

## Final ownership and recovery remediation

- Delta general completed with1Blocking (plan destination ready/evidence gap after
  source archive/delete) and1Important cache lifecycle. Architecture completed
  with4Important; risk1Important archived canonical shadowing and1Advisory storage
  retention. Full reconciliation and the explicit retained-history decision are
  in review-reconciliation.md.
- Provider now committed/pushed bdd79be2deea3431092b42f15890e95cee40f3a0; typed
 0522aa2 unchanged. Go all packages and15 repeated ownership/backfill race tests
  pass; setup-error release3 repeated races and exact0.154experimental schema
  pass. Completed no-watch histories retire; only8 idle incomplete histories
  retain retry progress. Watched/active/queued readers keep one gate.
- Root monitor fixups0cb6b89/d0ce3f7 share4 authority-local read slots, stop
  observation after thread verification fails, and stop successful noninteractive
  snapshot polling/projection. Three-repeat focused activity race4.590s and
  browser unit pass; a40-worker test covers queue progress/cancellation/concurrency.
- Creation owner is finishing exact CLI-only journal recovery and archived
  canonical access tests. No strict journal schema remains duplicated in Go.
- The final architecture/scope packet is review-final-packet.md; exact final
  commit/pin verification will be appended before launching. Long acceptance and
  deployment remain pending.

## Final review ranges

## Exact final ranges

- codex-web: `269962eb65007581ba69c205634f9e6c14cc39d3..bdd79be2deea3431092b42f15890e95cee40f3a0`
  Prior delta review to final tree: `4dde3c6aaa1d038c518563762fa7ac480b650cd2..bdd79be2deea3431092b42f15890e95cee40f3a0`.
  Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/codex-web`.
- dev-workspace: `bcbaf825d71285cbbd05b56e78bc386f2df480bd..8760619776cb89936a50d07237a1323b22553bba`
  Prior delta review to final tree: `40837d245e867aa0edd35f59f72b63bba80034d1..8760619776cb89936a50d07237a1323b22553bba`.
  Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/dev-workspace`.
- vpsfree-dev-workspace: `c4df3838de8b42083bd43e86bfdff7d45a7e952f..db25c77e7d622d71a2e0c9d44b4a20a5aecb27fd`
  Prior delta review to final tree: `4e03a3f0a3fd439ae2c645ab41fa736051c5b8c9..db25c77e7d622d71a2e0c9d44b4a20a5aecb27fd`.
  Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/vpsfree-dev-workspace`.
- workspace: `e0d3dee52ac637a96a7d73299aecd753759b484b..584ea0f6180cbc82fb8b17047303607259686dbd`
  Prior delta review to final tree: `ea6cc34a303dc2c8d9027f109a2212d1ebea02c5..584ea0f6180cbc82fb8b17047303607259686dbd`.
  Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/workspace`.

All four intended code/pin worktrees are committed and clean. Final runtime
autosquash preserved exactly the tested tree. Provider CI atbdd79be passed:
https://github.com/aither64/codex-web/actions/runs/34695650528.

Final provider all-Go suite passes; history lifetime/backfill/overlap tests pass
15 race repeats (6.128s), recorder-setup-error ownership3 race repeats, and exact
0.154experimental schema passes. Runtime all Go packages and browser unit pass
against actual bdd79be pin (web13.324s). Creation focused Go race8.136s, Ruby
28runs299assertions5.884s pass. These include source archive/delete at the exact
evidence-write crash, no duplicate initial turn, binding/journal mismatch
rejection, fresh-source validation, and six archive-destination new/plan/fork
combinations with evidence present/absent and pending lifecycle preservation.

Final vendorHash: `sha256-oaihmUfwPnYLdHjYSx2rSZIM57gS7s0t4TwLaIbs5RM=`.
Provider Go pseudo-version: `v0.0.0-20260912130915-bdd79be2deea`.
The final package dependency graph evaluates. All branches remain unmerged.

Final architecture/scope review is starting. General/risk narrow follow-up
findings are directly verified; no further full rerun merely to confirm them.

## Final review findings and focused follow-up

Both final lanes completed at providerbdd79be/runtime8760619. Architecture found
1Important reconnect admission issue (provider restores bypass portal slots,
duplicate browser reads consume slots while queued per thread). Scope found
1Important interrupted creation receipt surviving completed destination deletion.
Both also found an Advisory archived notice inaccurate after revive. Retention
reconciliation is supported by both reviewers and remains Advisory.

Root queues reads per thread before authority admission, with ref-counted gate
lifetime and cancellation. Three race repeats of all activity monitor tests pass
4.736s, including40 duplicate browser requests plus unrelated worker progress.
Provider owner is bounding passive reconnect RPCs; creation owner is tying stale
receipt retirement to existing verified completed-deletion recovery evidence.
The latter may add preserved receipt/binding files to existing deletion recovery
without changing strict schemas. All changes will be committed and quick-tested
before the affected architecture/risk review, then long acceptance.

Pre-follow-up exact-head CI is green for providerbdd79be, runtime8760619 and
organizationdb25c77 (run34695832993, including devcluster-check). Controlled
conversation fixture now uses actual userInput prompt kind and compiles against
actual pinnedprovider; actual browser execution remains pending.

## Exact committed ranges

- codex-web: `269962eb65007581ba69c205634f9e6c14cc39d3..83770217d63f2c206689d2c569e1c81950544504`.
  Reviewed delta: `bdd79be2deea3431092b42f15890e95cee40f3a0..83770217d63f2c206689d2c569e1c81950544504`.
  Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/codex-web`.

- dev-workspace: `bcbaf825d71285cbbd05b56e78bc386f2df480bd..c350274225e2886209f4d92e5f01f464bc1caf1a`.
  Reviewed delta: `8760619776cb89936a50d07237a1323b22553bba..c350274225e2886209f4d92e5f01f464bc1caf1a`.
  Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/dev-workspace`.

- vpsfree-dev-workspace: `c4df3838de8b42083bd43e86bfdff7d45a7e952f..a0d7fdca3ccfe20fa920cfba5e4e880caf9cc1da`.
  Reviewed delta: `db25c77e7d622d71a2e0c9d44b4a20a5aecb27fd..a0d7fdca3ccfe20fa920cfba5e4e880caf9cc1da`.
  Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/vpsfree-dev-workspace`.

- workspace: `e0d3dee52ac637a96a7d73299aecd753759b484b..ef75f045f1a0a496c23251a25306a98e32438a2f`.
  Reviewed delta: `584ea0f6180cbc82fb8b17047303607259686dbd..ef75f045f1a0a496c23251a25306a98e32438a2f`.
  Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/workspace`.

All worktrees are clean. Consumer autosquash preserved the tested tree.
Go pseudo-version: `v0.0.0-20260912134208-83770217d63f`.
Fresh vendor hash: `sha256-8NzgurFJHLPL2ITTeXbXuD33afPxj3i+hmQKIQcWOVE=`.
Provider CI passed at the exact final head:
https://github.com/aither64/codex-web/actions/runs/34697189123.
The runtime, organization and workspace pins select this exact dependency chain.

The focused admission/deletion scope review completed with no findings. Provider
and runtime exact-head CI are green (34697189123 and34697306931). Architecture
and risk reviews are finishing; organization CI is still running. Final evaluated
workspace output: /nix/store/54n3yigv3j44cdljq04w6d42rf9a9hzw-dev-workspace-0.2.0.
Superseded temporary conversation fixture checkouts were removed; final fixture
compiles against the exact committed runtime and selectedprovider. Its archive
identity check and selected-version fixture provenance were corrected before
execution. No live fixture or deployment has run.

## Causal deletion repair committed

The admission review found capacity cleanup and wall-clock ordering defects.
Both are fixed. Creation records now freeze verified deletion operation history,
and queued CLI calls require the exact still-current receipt. This removes the
intermediate timestamp/mtime and retired-file mechanism. Root reviewed final
user-facing copy directly. Fresh architecture/risk review covers only the new
causal replacement; all other required lanes remain complete.

## Committed final delta and quick checks

- codex-web: `83770217d63f2c206689d2c569e1c81950544504..83770217d63f2c206689d2c569e1c81950544504`; worktree `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/codex-web`.
- dev-workspace: `c350274225e2886209f4d92e5f01f464bc1caf1a..f2512c1c1466a206d903b21cb80384e8dd59f72f`; worktree `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/dev-workspace`.
- vpsfree-dev-workspace: `a0d7fdca3ccfe20fa920cfba5e4e880caf9cc1da..eaf4a21a77b5accfacd0a44193383fbc6277f506`; worktree `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/vpsfree-dev-workspace`.
- workspace: `ef75f045f1a0a496c23251a25306a98e32438a2f..8456d0980bbb974595c3efb96cec4e857ae4def2`; worktree `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/workspace`.

The runtime contains seven functional commits; the creation fixes are folded
into the early-navigation commit. The other feature commits are unchanged in
content. Autosquash preserved tested tree 1e8bb7bc401683ac887e817b042b169fbe8e3aeb.
Provider is unchanged at 8377021. Consumers only refresh exact pins.

Focused Ruby: `nix shell --inputs-from . nixpkgs#ruby nixpkgs#git -c ruby
test/dev_session_test.rb --name '/portal_(fork|creation|start|plan_start)|fork|exclusive_browser_start|start_seeds|removal|delete/'`: 40 runs,495 assertions,0 failures/errors/skips.
Focused Go: from runtime portal, with Nix Go/GCC/Git/Ruby,
`GOWORK=off GOFLAGS=-mod=mod go test -race ./internal/session ./internal/web
-run "TestCompletedRemoval|TestCreation|TestSessionCreation|TestForkSessionInvokes|TestImplementPlan" -count=1`: session2.073s,web28.704s.
Exact removal confirmation regression also passes session race1.892s.
Prior capacity tests cover512 retired receipts,513 startup records and protected
running/unresolved/locked/journal-owned requests. Git diff whitespace check passes.
Full packaged/browser/live rollback acceptance follows this review.

Final causal architecture and risk reviews completed on f2512c1/eaf4a21/8456d09
with no findings (fresh gpt-5.6-sol/xhigh). All mandatory lanes are satisfied.
Residual very-large deletion recovery enumeration latency is unbenchmarked;
this is an operational scaling gap, with bounded receipt capacity regression
coverage and no arbitrary retention/purge change. Runtime CI34699256023 and
organization CI34699288252 both pass on exact final heads. Long packaged, VM,
browser, live App Server and rollback acceptance is now authorized to start.

## Browser-discovered activity route omission

The controlled full-handler browser rendered messages, typed search/subagent
items and questions, but timing showed unavailable. Network inspection proved
the browser uses the existing /api/sessions/:slug conversation base, whose
GET alias list omitted activity. Direct /codex/conversations/:slug/activity
returned the expected snapshot. Runtime8d3d44c adds that single established
read alias and extends its existing route contract. Focused alias, canonical
path rejection and activity checks pass1.150s. No authorization, persistence,
protocol or new design changes; root inspected forwarding through the same
reviewed resolver, so no full review rerun merely to confirm this wiring fix.
Controlled browser acceptance is rerunning against the corrected committed
server. Package pins are refreshing; the host VM test remains on f2512c1
because host configuration and lifecycle contracts are unchanged by this alias.
The old browser-tools store path was unavailable; rebuilt the same tools from
final Nix inputs, now mwsbfwdhqp9kw51sd51fnndpk7c968wr, using bin/python3.

## Installed protocol source repair

Final5jdpackage built successfully: all Go packages,296Rubytests/2979assertions
and73hosttests/438assertions pass. Actual check-codex then exposed a packaging
input gap: provider corpus reads all sibling production Go sources, but the
installed artifact included only client.go. Source coverage passed, installed
coverage omitted one thread/read and one thread/turns/list call.

Runtimef5d5878 installs the complete production source directory (excluding
tests), points the private host checker there, and runs installed coverage
during packaging. No application, observer, creation, API, state, Codex pin or
rollback-format change. Ruby syntax/Nixfmt pass; an exact staged installed
source set passes the full0.154experimental schema validator. Root inspected
this as delivery of the already-reviewed scanner input contract; no new design
or expanded boundary requires another reviewer rerun. Final pins/build update.
The live creation/browser acceptance on8d3d44c/5jd remains valid for unchanged
application behavior. Final package will also execute check-codex before switch.

## Live acceptance progress and environment findings

Controlled conversation browser passed fully on runtime8d3d44c. Actual initial
creation form redirected in18.8ms and browser navigated in307ms, with shell
GET2.8ms while CLI was held; heartbeat advanced. Harness initially expected409
from canonical conversation mutation, but shared resolver intentionally returns
masked404; corrected artifact expectation, preserving legacy fork409. No thread
was allocated in that run.

The next run reached real CLI preallocation recovery lookup and timed out60s.
The worker retained its receipt/journal and showed failure. Direct shared-socket
thread/list for the exact fixture cwd also stalled8and10seconds, while initialize
was10ms, loaded/list2.3ms and13loaded metadata reads8–31ms. Read-only exact-cwd
SQLite metadata query returned zero threads. This excludes duplicate allocation
before fallback. Creation owner is testing a fixture-owned selected0.154server
under the existing authenticated home and will retry the same saved request
only after lookup succeeds. No shared service restart or credential copy.

Concurrent nix-collect-garbage removed unrooted browser tools between commands.
Tools rebuilt and protected with registered out-link;5jdacceptance and final
pwi8delivery packages have registered indirect GC roots. Leave them until
fixture/deployment checks finish, then remove only task-owned temporary roots.

## Deployment checkpoint

Profile28 now runs pwi8v7s from workspaceabd0cbd, with finalf5d5878 runtime.
Installed compatibility and initial HTTPS/feature/service checks passed.
Exact final provider/runtime/organization CI is green. Rollback attempted once
and correctly refused before profile mutation: concurrent NFS session has an
active turn. Helper restored terminal clients. Do not interrupt that work or
retry merely to obtain a green live rollback. Final HTTPS/service recheck is
running; the isolated old/new fixture remains the rollback acceptance path.
The creation owner now uses a clean private Codex metadata home and owned
server; exact filtered lookup is3.9ms with no thread allocated before resume.

## Real plan creation regression

The isolated fixture now uses one consistent private CODEX_HOME for App Server,
CLI and native TUI. Its existing source completed one bounded diagnostic after
an initial interrupted turn; ordinary settings API restored the requested model
and effort. Fork retry preserved its receipt and inherited history without a
new initial turn. A real Plan-mode response produced a captured plan; plan-new
returned202 and navigated immediately.

After source advancement and portal restart/retry, the CLI created exactly the
intended plan session and its initial turn completed in2922ms. The portal then
rejected completion because its frozen derived goal retained the plan's trailing
newline while Ruby read_goal strips it. The source PlanText/turn/digest must
remain byte-exact; the derived initial goal and its evidence digest must use
the existing CLI normalization. Profile28 has been deployed, so recovery must
also accept its already-frozen raw goal after applying that same normalization.
No receipt, binding, journal or proof is to be fabricated or manually edited.
The creation owner implements this narrow regression and focused tests before
targeted general/risk review and resumption of the same fixture. Three of four
fixture threads are allocated; no replacement thread is authorized for this fix.

Goal normalization is committed as d3bfd0f with clean runtime tree. Focused
race tests passed in 1.912 s and broader creation coverage in 32.353 s. Fresh
general and risk reviews completed with no findings (gpt-5.6-sol/xhigh).
Organization a30de6c and workspace 9edf553 mechanically select that runtime;
all are pushed and contain freshly fetched default branches. Runtime CI
34702185008 passes; organization CI34702231264 is running. The final consuming
package is building with a registered GC root before the existing real fixture
resumes. Completed controlled-browser scratch copies have been removed after
confirming that no process references them.
