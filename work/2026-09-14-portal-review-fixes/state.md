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
The initial fixes are deployed and verified against the original user URL.
The presentation follow-up is committed and passes browser checks in both engines.
The complete presentation follow-up, including the mobile heading correction,
is deployed as 243g1pc and live checks pass. Provider, runtime and organization
CI all pass, including the development-cluster check. All required reviews and
verification are complete. Feature branches and this session remain open.

## Repositories

All branches: 2026-09-14-portal-review-fixes. Worktrees: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-14-portal-review-fixes/<name>.

| Repository | Review base | Current head |
| --- | --- | --- |
| codex-web | `6335da93acdcc82cc26200d2fbc7f479655aa7c3` | `882c88ccfbebfb646fb2cafbe9bc6790141b2d13` |
| dev-workspace | `83136101866eb42d9e079f47191308c0549ac9e7` | `227bcfc1b989407582d3b022f8b388ac29972c16` |
| vpsfree-dev-workspace | `a08a40eeff124bdbcc1ce6b6b06aed1839a9d9fc` | `08d691cfd239260ce5bf7c269a44a49ce8de41e7` |
| workspace | `d926aa2` | `d53014fd4b589a9de56febfc880aae7c4179b11c` |

Workspace registration originally started at efd65e4; the branch is now rebased
onto shared master d926aa2. All code changes and dependency pins are committed and pushed on the four
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

## Presentation follow-up in progress

User approved implementation on the existing initiative. Explicit session
environment resolves dev-session current to 2026-09-14-portal-review-fixes.
Baseline deployed heads: runtime b837f0d, provider 882c88c, organization f6050a4,
workspace 1c3f3e1. Provider behavior should remain unchanged. Initial inspection
confirms file headers lack top: 0 and archival UI concatenates stored CLI errors.
Three focused presentation commits and downstream pin commits are planned.

Presentation implementation: runtime 774db12 (28a49ea sticky headings,
88955af compact sidebar, 774db12 archival presentation). Focused Go web suite
passes (32.128s); JS syntax and diff whitespace checks pass. Browser acceptance
was extended for both engines, sticky file transitions, narrow line links,
sidebar/history/limits/keyboard and archival failure/hold states. The Node browser
contract script requires its Go fixture URL; invoke it via go test, not directly.
Workspace feature rebased onto current shared master d926aa2. Package pin updates
are being consolidated into the existing unmerged pin commits; deployed baseline
revisions remain recorded above for differential review and rollback.

Presentation review candidate is committed and pushed: runtime 774db1205a0cd653b687cec34e788eabd6a9f1c1,
organization 109e9ded49d9b336a25f44ebfdbe19e5ed598b90,
workspace a24742ab2e999cabafe81926a4271af436546b19. Codex-web unchanged.
Package names evaluate successfully; no changed state or host compatibility
contract. Review is Medium risk with General, Architecture, Scope and Risk
lanes (the latter covers downstream pins/deployment); fresh agents use
 gpt-6-astra / xhigh. Reports and packet are under review-presentation/.
CI started on current heads: runtime 34884115403, organization 34884177967.
No superseded queued/in-progress run exists; prior baseline runs completed.

Architecture and Scope reviews found no Blocking/Important findings. Architecture
A1 (Advisory): linked-line reveal uses the runtime editor's highlight selector
and existing frame timing. Accepted for this bounded presentation fix; both
modules are packaged together and browser acceptance covers all three views.
Do not expand the editor API solely for this follow-up. Revisit an explicit
completion/inset contract when the editor boundary changes. Add an index-mobile
sidebar/limits smoke because those shared selectors also moved.
Runtime CI 34884115403 passed; organization flake checks passed and its existing
devcluster-check is running.

General review found no Blocking/Important findings. G1 (Advisory) fixed:
automatic read-back after a failed Keep open save now retains the save error
and diagnostic while displaying the last confirmed checkbox value. Extended
browser acceptance to assert this and test the index sidebar/limits at 600px.
These are direct bounded review corrections; no review rerun is required.

Risk review completed without findings. All four lanes are complete with no
Blocking/Important findings. General remediation is committed at runtime
438a708c7c00f20943823d596858ba59a6c7c375; focused shipped-browser HTTP contract
passes (0.816s). Browser acceptance now starts, followed by packaged validation.

Browser results: Chromium passes repository acceptance, including exact OAuth2
counts and new sticky/line-link scenarios. Real-template presentation acceptance
passes Chromium and Firefox (14.373s), including retained save errors, complete
settings states, index/mobile limits and session sidebar transitions. Keyboard
navigation exposed Firefox's deferred native fragment focus; keyboard tab changes
now update the same URL/history and dispatch the existing hash handler without
native fragment focusing, then focus the selected tab. Same-tab keys do not add
history entries. This is a bounded correction within the accepted keyboard scope.

Fixture corrections: Split contains two editors, so wait for its first editor;
repository detail scrolling now chooses an explicit position (Firefox caps a
large wheel delta at about one viewport). Firefox fractional geometry requires
scrolling past the rounded detail height. The lifecycle fixture now retries its
focus stimulus until the held read starts, since a previous read can coalesce a
focus refresh; both lifecycle engines pass. Named Go subtests allow focused
browser reruns. These corrections do not alter production network behavior.
Runtime packaged flake check passed including its host activation/rollback VM.
Firefox's broader pre-existing parent/back/reload fixture is still under
investigation before acceptance is declared complete.

Final runtime head: 63cbc32173f73da313e4f11c9c2214884f6161d5. The three
presentation commits remain separate (4f1c176 sticky headings, 876d9e2 compact
sidebar, 9b7000e archival settings); 63cbc32 is a separate correction to the
previously deployed lifecycle test stimulus. Reconciled tests during autosquash;
final tree exactly matches the tested pre-rebase tree. Focused web suite passes
again (33.639s). Real-template presentation acceptance passes both engines at
final source (15.277s), including repeated End not adding history entries.
Repository acceptance passes all 31 scenarios in both Chromium and Firefox.
The Firefox reload/back issue reproduced on a plain HTML server without any
portal code; its test now checks reload in a separate tab from history traversal.
No production workaround for browser history internals was added.

The final downstream pins are being updated and pushed with exact explicit
leases. Prior candidate CI runs both completed successfully; none was rerun to
mask failures. No superseded running workflow remains.

Final organization CI 34886053176 failed in the unchanged Git history-count
fixture at count 101: total=0, Git exit 128. Downloaded and inspected failed logs;
its companion compatibility-package repository suite passed in the same run.
Runtime CI 34886015212 and the local final workspace package build passed.
The failing runner captured stderr but discarded it, so the old CI artifact
cannot identify Git's reason. No blind rerun was requested. A bounded local
reproduction run and diagnostic improvement are in progress: retain stderr on
the existing exec.ExitError and print it in this test's failure report, leaving
the public error text and API unchanged. The original failure remains an
unresolved transient until diagnostic evidence identifies a cause.


CI investigation result: Git stderr was recovered in a 50-run reproduction,
with one missing-object/revision-walk failure at 101 commits. A second 100-run
series passed, confirming intermittency. Write-side trace records automatic
commit-graph maintenance at that boundary; the maintenance race explanation is
supported but not proved as an upstream root cause. Disabling maintenance only
in the fixture gives 50 passing runs (68.786s), with complete repository suite
passing (11.536s). The final test retains stderr and revision-pair diagnostics.
General/Architecture reruns cover the 22-line diagnostic/test addition plus
fixture maintenance setting; UI behavior and external contracts are unchanged.
Superseded organization CI 34886782741 was cancelled after its head changed.


Final bounded reviews completed at cdcaafa/6f59c30/5bd3d8b, with no findings.
Reports: review-presentation/ci-general.md and ci-architecture.md. General's
independent diagnostic/pagination check passed (1.491s). Final workspace flake
check passes (3 runs, 14 assertions). Runtime CI 34887329390 passes; organization
CI 34887373731 has passed flake checks and is running devcluster-check.
Final comparison snapshots captured for runtime, organization and workspace
at their exact final heads. No integration is performed.

Final organization CI 34887373731 passed, including flake checks and
devcluster-check. The workspace package built successfully as
/nix/store/qm6w27rw94vdn6pwwqyg61baksg30s4f-dev-workspace-0.2.0.
Authorized user-profile switch is applying this exact candidate; no system
configuration or default branch was changed.

Live deployment at qm6w27r passed the read-only original-URL smoke: +116/-6,
sticky headings, 58px comparison sidebar and 250px Codex sidebar, formatted
settings, no page errors or external mutations. Portal PID 744878; Codex
retained PID 1090021 and exact 0.154.0 binary. Served app.js matches source.

Visual inspection caught a mobile-only heading problem: the collapse control
shrunk into multiple lines. A narrow correction prevents control shrinking,
gives the file name row full width on mobile and hides the directory there
(the full path remains in the heading tooltip/accessible name and copy action).
The existing browser acceptance now asserts control height; all 31 scenarios
pass in Chromium and Firefox. An overlay against the deployed template confirms
the geometry. This is a bounded correction within the reviewed mobile-heading
behavior, with no new design or contract; no review rerun under steps 9–10.
A final package refresh and live verification will include this correction.

Mobile correction final heads: runtime 227bcfc, organization 08d691c, workspace
d53014f. Pins changed only to consume this correction. The final overlay smoke
passes and the mobile screenshot was visually inspected: one-line control,
complete OAuth2 basename, no overflow, two compact header rows.
Comparison snapshots were recaptured at all three final heads.
Runtime CI 34888828914 and organization CI 34888892734 are current.
Cancellation of superseded runtime run 34888765809 returned HTTP 403 (token
lacks Actions write permission); do not retry cancellation or confuse its result
with current-head CI. This matches the existing 2026-09-10 cancellation note.

At final runtime 227bcfc, both Chromium and Firefox again pass all 31 repository
acceptance scenarios, including the complete mobile correction. Final workspace
flake check passes (3 tests, 14 assertions). Runtime CI 34888828914 passed. The
superseded 34888765809 finished successfully after cancellation was refused;
there is no remaining stale runtime run to cancel.

Final user-profile activation succeeded from workspace d53014f. Installed:
/nix/store/243g1pcykrjq7alpvk9f1n81yfxcfimd-dev-workspace-0.2.0. Portal is active
as PID 805994; shared Codex remains PID 1090021 with the exact 0.154.0 binary.
Served repository-review.css SHA-256 matches committed source; it is no-store.
Final read-only live smoke passes on the original OAuth2 URL, both layouts,
sticky headings, 58/250px sidebar transitions, narrow-screen toggle geometry,
no mobile overflow and formatted settings. No page errors or external mutations.
Unified, Split, mobile and settings screenshots are retained as portal artifacts.
The live settings scan currently has only an uncommitted-worktree blocker; raw
CLI diagnostic disclosure behavior is covered by the real-template fixtures.

## Presentation handoff

All final-head CI passed: provider 34878642980, runtime 34888828914 and
organization 34888892734, including devcluster-check. There are no unresolved
Blocking or Important findings, failed checks, or pending deployment work.
The four feature worktrees are clean and all feature heads are pushed.
The final workspace source is d53014f, based on d926aa2; another session's
coordination commit advanced shared master during verification and is preserved.
No default branch integration, worktree removal, archival or session stop was
performed. Keep the active lifecycle because the feature branches are unmerged.
Next user action: reload the portal and review the deployed changes; integration
remains a separate decision. Final screenshots and review reports are linked in
portal.yml. The shared-root checkpoint records this genuine presentation handoff.
Temporary browser/proxy processes ended, and only this task's temporary Nix
GC-root symlinks were removed. Runtime profile retains the deployed package.
Stable URL: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-09-14-portal-review-fixes/
