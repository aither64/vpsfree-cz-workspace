---
lifecycle: active
---

# Portal review and recovery fixes

## Status

Implementation is committed on all four feature branches. Initial tracking was
committed as 8f31bab. This shell-only session belongs to the current API
conversation (tmux $29; no separate Codex thread). Current session commands use
matching DEV_SESSION_SLUG and DEV_SESSION_WORKSPACE. Shared master and unrelated
working-tree changes are preserved.

The user additionally requested gpt-6-astra for reviews (retain xhigh) and moved
Automatic archival under a sidebar Session settings tab. Both are implemented.
Deployed and verified against the original user URL. Mandatory review, browser
acceptance, packaged checks and live App Server validation pass. Provider, runtime and organization CI are green.

## Repositories

All branches: 2026-09-14-portal-review-fixes. Worktrees: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-14-portal-review-fixes/<name>.

| Repository | Review base | Current head |
| --- | --- | --- |
| codex-web | `6335da93acdcc82cc26200d2fbc7f479655aa7c3` | `882c88ccfbebfb646fb2cafbe9bc6790141b2d13` |
| dev-workspace | `83136101866eb42d9e079f47191308c0549ac9e7` | `b837f0d974a98857daef7e4cc09d8f3039a059a0` |
| vpsfree-dev-workspace | `a08a40eeff124bdbcc1ce6b6b06aed1839a9d9fc` | `f6050a4d661be7c923518e0b962a4372ebad7f50` |
| workspace | `8f31bab` | `1c3f3e156cad0f84090ec1934acbb867eb723345` |

Workspace registration originally started at efd65e4; the branch is now rebased
onto shared master 8f31bab. All code changes and dependency pins are committed and pushed on the four
feature branches. No default branch integration is authorized.

## Investigation and commands

Read local project rules and the mandatory review, handoff, user-facing writing
and English Humanizer skills. Inspected deployed assets, GitHub's raw patch,
local Git objects and HTTP responses through the portal Unix socket. Compared
rendered line classification using an in-memory export from the deployed bundle.
Ran isolated Chromium and Firefox navigation probes through a temporary local
proxy; proxies and browsers were stopped. Inspected recent portal logs without
recording question answers or credentials. Findings and acceptance cases are in
plan.md. No production conversation was answered or interrupted by investigation.

## Validation, review and deployment

Focused provider Go tests and 20 Node contracts pass. Runtime repository, web
and workspacecodex Go packages pass with the updated provider. The editor build
and nine unit tests pass, including the real OAuth2 +116/-6 in both projections.
The new large-preview HTTP test covers 2001 changed lines and explicit loading.
The initial browser acceptance fixtures cover collapse, exact DOM counts and
bounded answer recovery; final results appear below. Packaged editor assets built while
regenerating vendorHash; the expected fake-hash discovery mismatch produced
sha256-qePokxlu5Stpek9I49ckR9HO44/8Y/zn5v4VBZJQZRU=, now recorded in Nix.

Provider CI 34875990096 and runtime CI 34876413264 pass at their current heads.
Workspace and organization flake evaluation pass. Review
packet: review/packet.md. High risk; all four mandatory lanes, gpt-6-astra/xhigh.
Deployment is recorded below. No default-branch integration has occurred.

## Cleanup and handoff

Keep feature branches and the session open. No archive/delete/stop authorization.
Stable portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-09-14-portal-review-fixes/

## Mandatory review reconciliation

All four lanes finished against review/packet.md: General, Architecture, Risk
and Scope, each fresh gpt-6-astra with xhigh. High risk due to answer delivery,
connection retirement and mixed browser generations. Reports are in review/.

Blocking G1/R1 fixed: validate the exact claimed offer after acquiring the
writer lock, and serialize retirement/reissue with the response write. The
real-WebSocket regression holds a claim, resolves/reissues its ID, then verifies
that the obsolete response is definitely unsent and only the replacement answer
arrives. Focused provider Go and browser contracts pass; CI 34878642980 passes.
Important A2/R2/scope fixed: updated built-in answer/approval/snooze controls send
tokens; tokenless HTTP actions against PromptResponder return reload_required.
Legacy direct Go calls and external implementations retain their supported API.
All three HTTP actions and mounted controls have focused regression coverage.

Important A1/G3/R3 fixed: each offer owns its snooze state independently of
persistent logical drafts. Late failures cannot affect a replacement. Explicit
Refresh question retries failed snoozes, including an unchanged restored token.
Focused Node tests pass; real browser fixtures cover both sequences.
Important R4/scope fixed: artifact Download has the download attribute so it is
excluded from document-navigation suspension. Added Chromium/Firefox acceptance
for downloads, hidden-tab timing and departing-document failures.
Advisory R5 fixed: changed cacheable conversation module URL from v7 to v8.

Blocking G2 fixed: split automatic histories from exact/lazy rendering and
page read/timing lifecycle from question recovery. Supporting tests accompany
the behaviors; the provider pins remain with the consuming question change.
Used ordinary commits in a temporary detached worktree, proved final tree
identity, atomically updated only this feature ref, and removed the clean
temporary worktree. No shared index/reset/stash or default branch was changed.
The differing Scope assessment was reconciled by applying General's explicit
commit-series requirement. Direct requested remediations required no new review
lane or public contract design; no routine rerun under skill steps 9-10.

Provider final head: 882c88ccfbebfb646fb2cafbe9bc6790141b2d13.
Runtime series and final heads recorded below. Quick runtime Go web and
workspacecodex tests pass with the new provider. Vendor hash regenerated through
an expected fake-hash mismatch: sha256-dzNU/tQRYnhJP88XdJTN+usjgZCHFtK0PWbRXil39Ac=.
All Blocking and Important findings are addressed. Browser acceptance and
packaged checks may now run; deployment and final downstream pins remain pending.
3584eb5 portal: recover planning answers against current prompt offers
c498d6f portal: preserve page reads and timing across navigation
40434ff portal: refresh repository histories when branches move
1741603 portal: render exact Git diffs and collapse large files
b18a82d portal: move automatic archival into sidebar session settings

## Browser and packaged validation

Repository acceptance passes all 29 scenarios: original OAuth2 +116/-6 in both
rendered layouts, 2000/2001-line threshold, collapse/reopen/layout retention,
explicit file/line links, stale/out-of-order history refresh, eight mounted
editors, keyboard navigation, strict CSP and responsive geometry.
Runtime nix flake check passes, including all Go/Ruby/browser contracts and the
NixOS host activation/rollback VM. No kernel was built locally.
The configured live Codex 0.154.0 fresh-thread contract passes against an
isolated App Server and private temporary home; it did not touch shared threads.

Browser question acceptance exposed two draft/focus issues: disabling the old
focused control before replacing its DOM lost focus restoration, and an optional
note typed before selecting a choice was discarded. Restore logical question
focus only when focus remains on the body, and retain unselected notes using
the existing serialized empty-kind representation. Secret notes remain excluded
from storage. All question scenarios now pass, including same-token snooze retry,
late old-token failure, unchanged/changed question recovery and 5 responsive
viewports. These narrow corrections remain in the question behavior commit.

Chromium and Firefox lifecycle acceptance passes: an actual artifact attachment
download leaves reads running; timing retains its value across a hidden/visible
transition with a failed fresh read; navigating away during an in-flight failing
read shows no old-page warning; back navigation resumes details reads.
The first download fixture used an intercepted attachment on self-signed TLS and
Chromium cancelled it. The fixture now serves the real HTTP attachment from the
Go server and explicitly trusts its test certificate in Chromium. This is a
test-only transport fix; it does not change portal TLS/security behavior.

## Final candidate

All four final feature heads are committed and pushed. Provider CI 34878642980
and runtime CI 34879637501 pass. Organization CI 34879806786 has passed its
flake checks and is finishing devcluster-check. Workspace flake evaluation
passes. Provider go test -race ./codex ./conversation passes. Final quick web
contracts pass after browser-driven focus and note corrections.

The organization bare clone has no wildcard fetch refspec. A force-with-lease
push initially refused because its feature remote-tracking ref was absent.
Verified remote head 7dc4ea2, fetched that exact feature ref, then pushed with an
explicit lease requiring 7dc4ea2. No foreign branch advancement was overwritten.

Before deployment, the user profile remains
/nix/store/smwr2xjkf9qz2v6hmdf2hh7g9iaqdvga-dev-workspace-0.2.0.
Portal PID 4090817; shared Codex PID 1090021, active binary
/nix/store/8vfvwkn3biviq6lmyj1r886fqcd5lkjn-codex-0.154.0.
The application is being built from the final workspace feature revision.

## Deployment result

workspace-host switch --source <initiative>/workspace succeeded. Installed
package: /nix/store/sg9slm5yppln3l7s8pgg8yhxfk6b38l4-dev-workspace-0.2.0.
Portal restarted as PID 393983; shared Codex retained PID 1090021 and the exact
0.154.0 binary. The old package generation is retained for rollback. Installed
mandatory-change-review now contains gpt-6-astra in both model instructions.
The served app.js SHA256 exactly matches the committed feature source.

A read-only Unix-socket browser proxy verified the original user URL and file:
116 additions and 6 deletions in both Unified and Split, collapse/reopen, and
sidebar Session settings. Using deployed templates/assets with isolated browser
HTTP fixtures, the answer recovery sent exactly twice with the restored offer
token and identical answers. The proxy rejected every external mutation; no
real question was answered. No browser page errors or window alerts occurred.

Comparison snapshots were captured for all four final heads. The workspace
capture uses efd65e4 (the actual origin/master merge base), so it includes the
initial coordination commit before the workspace pin. An attempted recapture
with local-master base 8f31bab was refused because a different immutable
comparison already exists for this head. The valid original capture is retained;
review/packet.md records the narrower reviewed workspace base explicitly.

Verification and review reports are registered as portal artifacts. The session
remains active because all four branches are unmerged. No integration, archive,
delete, worktree removal or session stop is requested. The consolidated coordination checkpoint records this handoff.

Visual inspection of the deployed Unified and Split screenshots confirms
aligned unchanged rows/context and focused change regions. Registered the two
screenshots as durable verification artifacts. The live browser proxy and all
isolated browser/App Server test processes have exited.

## Final handoff

Final CI: codex-web 34878642980, dev-workspace 34879637501 and
vpsfree-dev-workspace 34879806786 all pass. The organization devcluster check
completed successfully in the original attempt. No superseded queued or running
workflow remained after any force-push; prior attempts had already completed.
No failed CI rerun was used as validation.

All project worktrees are clean. Temporary tool roots were removed after tests;
logs and test drivers were moved outside tracking to temporary local storage.
Only plan/state, portal metadata, the verification report, review reports and
two intentionally retained screenshots remain under the initiative directory.
The session and all feature worktrees/branches stay open. Integration requires a
separate user decision; current lifecycle remains active.

Workspace nix flake check also passes at 1c3f3e1, including its deployment
contract (3 tests, 14 assertions). All required validation is complete.
