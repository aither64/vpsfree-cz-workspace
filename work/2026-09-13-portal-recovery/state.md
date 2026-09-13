---
lifecycle: active
---

# Portal recovery state

Implemented and deployed to aitherdev on 2026-09-13. All review, quick checks,
package/system builds, CI and browser acceptance passed. All five feature heads are now merged and pushed to remote master. The
worktree/cache cleanup is finished. The user waived further workflow waiting;
the last cluster check was still running at handoff, so lifecycle stays active
pending that external result. No background monitoring or delayed cleanup is scheduled.
The user has now authorized default-branch merges and clean worktree/cache
cleanup. Session archival/deletion/stop and branch deletion remain unrequested.

## Repository identity

All use branch 2026-09-13-portal-recovery and worktree group
/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-13-portal-recovery/.
All five are registered in portal.yml with their final heads. Their feature
worktrees have been removed; the local and remote feature branches remain.
- codex-web: `aec4ea2ff13a053e340a2a47616d6fbc89aeeac1` (base `ee9ab42791a84b79315d952501264a6cbafc8695`).
- dev-workspace: `8f75ece30462b184065f21867508af5e14365c4a` (base `8a43d3b09ddd9fa3b2c5f6c9aaba3ef7efc0ad0f`).
- vpsfree-dev-workspace: `213a3db57dea9298f61309eb157c0853f2310e9b` (base `37f3bfa21079b217aef15a4c2e75ed7451b9d156`).
- workspace: `93b24afb6b42ad8c3131e84062d03d9202fe46d7` (rebased onto `7e92a43` before integration; deployed source was `d182305bf70c814eb5f3b4488bc36d66de6d2392`).
- vpsfree-cz-configuration: `8ef765d339ac792ef4f01a5c7a160e48600adcaf` (base `b0252827958a4cc231a2a0bb56ae3a1844db8ae8`).

Provider has one recovery commit. Runtime separates repository summaries from
conversation recovery; its provider pin is bundled with the consuming UI.
Organization and workspace have one pin commit each; config has one generated
confctl input commit, retaining its exact generated message. Remediations are
folded into owning commits. Upstream master refs were explicitly fetched again
before activation; all are unchanged and included. Shared workspace stays on
master, now including feature 93b24af and the unrelated tracking commit 7e92a43. Initial tracking was committed
as 5d51379 before code commits or deployment. Implementation updates were kept in
the working tree until the consolidated merge/cleanup handoff checkpoint.

## Investigation and resulting behavior

The running source had no browser GET deadline. A stuck read blocked the refresh
gate indefinitely; a failed read scheduled no retry. SSE comments were invisible
to JavaScript, and the mounted client waited for a ready event not emitted by
the server. Connection state shared the activity badge, concealing stale data.

The shared provider now owns bounded/cancellable snapshots, visible readiness
and heartbeat SSE events, wake/online/focus recovery, backoff, periodic snapshots,
late-response disposal and a separate connection notice with Retry now and last
refresh time. Failed grouped reads cancel siblings, including reconciliation.
Drafts, uploads, pending answers and paused transcript scroll survive recovery.
Send controls remain usable; authoritative acknowledgements clear only matching
unchanged composer text. Older servers use periodic snapshots without requiring
heartbeat support. Existing open tabs need one reload to acquire the new JS.

Repositories show the full comparison commit count and net file/line statistics,
using the same immutable base/head as history and Compare, including preserved
integrated comparisons. Optional summary errors retain usable history. Pagination
appears only when a previous or next page exists.

## Verification and review

See validation.md, review-packet.md, review-*.md, review-reconciliation.md,
ci-results.json, browser-results-{firefox,chromium}.json and live-results.json.
Review risk was high due the shared event/browser contract, deployment and mixed
versions. All four lanes ran as fresh gpt-5.6-sol xhigh agents. General/risk
sibling cancellation, risk composer race, architecture heartbeat and batch
contract findings are fixed with focused regressions. Provider wording advisory
is fixed. Scope advisory to keep native transient SSE retries was accepted with
recorded rationale: one controller owns the planned reconnection policy. No
Blocking/Important finding remains; direct fixes needed no confirmation reruns.

Provider full Go tests, 21 Node tests and nix flake check pass. Runtime repository
and web suites pass against the actual final provider pin. Workspace contract
checks and full package Go/Ruby suites pass (297/2989 and 73/438 runs/assertions,
with declared environment-dependent skips). Both browsers pass 9 acceptance
checks, including 35-second request expiry, silent heartbeat loss, missed final
replies, wake coalescing, offline recovery, preserved drafts/files/answers/scroll,
shared mounted UI, 50/51 pagination boundaries and 390px layout. Go/API tests also
cover 0/1/50/51/101, binary/rename/net-cancelling differences, rebases, integrated
snapshots, batch parity and summary-limit failures.

All configured CI is successful at final heads. Superseded organization run
34766698778 was cancelled; other old runs completed before final pushes. No
feature-branch workflows exist in workspace/configuration.

## Deployment

Actual deployment contract passed at runtime 8f75ece. Ran nix build .#default in
the workspace feature, confctl build -y cz.vpsfree/machines/aitherdev, confctl
deploy -y cz.vpsfree/machines/aitherdev dry-activate, then workspace-host switch
--source <workspace feature> and confctl deploy -y ... switch. Confctl commands
ran through the configuration Nix shell. No kernel compilation occurred.

User profile generation 36:
/nix/store/71bnn9hribjb5p3hj655xyzq33wki98l-dev-workspace-0.2.0.
System generation 2026-09-13--18-06-32:
/nix/store/z2p1f0l5w1fbqm4k17ibn27yzwmyd82g-nixos-system-aitherdev-26.05.20260911.21a67dc.
Previous profile 35 (cgllc6zfnab06ah8w17izn4hmj80mhia) and system generation
2026-09-13--11-33-55 (jvi5n2bbp0li9w2xikh5kgwqnnzgy7g7) remain for rollback.
No state, schema, App Server protocol or Nix option migration is involved.

Both deployment health checks pass; portal, router, nginx and Codex are active.
Codex 0.154.0 retained MainPID 1090021. Authenticated health/index/session/assets/
thread return 200; unauthenticated health returns 401. Named ready/heartbeat
arrive through nginx. All five live repository totals match local Git counts
and net diffstats. Application lives in the user profile, configuration changes
are now included in remote master after explicit user acceptance. Rollback was not needed.

## Session and cleanup

Stable portal:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-09-13-portal-recovery/

No initial DEV_SESSION_SLUG belonged to this process, so a separate session was
started with dev-session start ... --as-is --goal-file ... --no-attach --json.
It owns shared thread 01a09b5e-37ea-7501-b63d-946149f03071. Startup launched a
second terminal task; the owned duplicate was interrupted with Escape before
any code edits. The terminal remains available and idle. Helpers are scoped
with matching DEV_SESSION_SLUG and DEV_SESSION_WORKSPACE; current and url were
verified after activation.

All temporary browser servers stopped successfully; the untracked Go fixture
copy was removed. Retained fixture source, concise test results and screenshots
are intentional review evidence. Configuration .bin/.bundle/.gems/.confctl caches have been removed
from the feature and temporary merge worktrees during accepted cleanup. Temporary browser/tool/package roots and input files are
removed after final checks. All four temporary integration worktrees have been removed non-forcibly.
All five feature worktrees were removed with dev-session worktree remove,
which recorded their exact final heads. All branch refs are retained.

Setup failures and workarounds: config worktree hook required bundle install in
nix develop; direct go tests require flake-derived shell with GOWORK=off and
GOFLAGS=-mod=mod to avoid buildGoModule vendor environment; vendor hash was
measured using fixed-output mismatch. Bare org fetch did not update the lease
ref; force-push used the exact previously pushed head as its lease. Selenium
requires python.withPackages, and browser tools were rooted while tests ran.
Browser fixture issues and verified corrections are recorded in validation.md;
reusable lessons are in the dated notes for codex-web and dev-workspace.

## Integration progress

User requested merging into defaults and cleanup. Reusing this initiative with
explicit follow-up authorization; scoped current command confirms its identity.
Fetched all remote master and feature refs. The only required rebase was the
workspace pin onto shared master 7e92a43, preserving the other initiative's
tracking commit. The new feature head is 93b24af; flake files are byte-identical
to reviewed/deployed d182305. The feature push used an explicit old-head lease.
No implementation changed; existing mandatory review and acceptance remain valid.

All five master pushes succeeded as fast-forwards. Fresh explicit remote fetches
prove local feature == remote feature == origin/master for every repository.
Independent projects used fresh detached merge worktrees; root workspace merged
from shared master with an empty index and preserved unrelated changes.

Merge checks passed: provider full nix flake check (Go and 21 Node tests), runtime
all-check evaluation plus focused Go web/repository suites, organization and
configuration all-check evaluation, and merged workspace deployment-contract
check (3 runs/14 assertions). Required configuration hook setup ran through its
Nix development shell and bundle install. No kernel build occurred.

Default CI: provider 34769980925 passed; runtime 34769982021 package and host
VM jobs passed. Organization 34769983038 passed its flake checks and was running
devcluster-check when the user instructed not to wait for workflows. Workspace has no
workflow and configuration has no push-triggered validation. No reruns needed.
See merge-results.md for final integration and cleanup evidence.

## Final cleanup handoff

All five accepted default-branch merges are pushed, and all nine feature/merge
worktrees plus configuration caches are removed. The empty initiative worktree
group was removed. Non-force removal succeeded throughout; no branch refs were
deleted. Session tracking, conversation identity and curated evidence remain.
The local CI watcher was stopped without cancelling the GitHub workflow after
the user's explicit instruction not to wait. No further deployment is needed.

Merged live checks passed before worktree removal, including populated integrated
repository comparisons. After removal, the open session still serves conversation
and artifacts; live repository history/status requires restoring the retained
canonical worktrees until archival. No archive/delete/stop action was requested
or performed. A single consolidated coordination handoff records implementation,
review, deployment, merges and cleanup. Unrelated shared changes were preserved.

Post-cleanup authenticated health, session, assets and thread checks passed;
unauthorized health remains 401. See cleanup-live-results.json.
