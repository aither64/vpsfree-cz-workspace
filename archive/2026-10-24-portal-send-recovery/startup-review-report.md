# Composer startup admission review

**No Blocking, Important or Advisory findings. Review gate clear for final
runtime/browser/composition verification.** No deployment result is certified.

Reviewed runtime `10bb047513c82d1310e8fcaa797e8772f948dd8a` against previous
`1b56299642e3cc7abdcc77fb63369a1abaf91412`, and checked its complete series
from `b3a6eb2fc0b41cf0cb965bf4c39991815d9df734`. The incremental diff is limited
to the initial Send disabled attribute in `templates/session.html` and the
startup barrier in `message_delivery_browser_test.cjs`. Runtime worktree is
clean and complete-range `git diff --check` passes.

## Startup behavior and ordering

The failure evidence supports a real admission gap: the retained browser log
shows no new message request or page error after the post-reload click, with
upload controls mounting afterwards. The previous template enabled Send based
on server interactivity before the asynchronous conversation-module import and
form-handler registration. At that point the browser could invoke the form's
native submission path instead of the durable JavaScript handoff.

Rendering Send disabled initially closes that gap using the existing control
state. `app.js` retains the disabled state while its conversation asset is
loading. Its normal startup then registers the composer keyboard, submit and
queue handlers before the explicit `updateMessageActions()` at the end of
composer setup. That function enables Send using existing interactivity,
attachment-readiness, settings and in-flight conditions.

The upload controller can invoke its readiness callback during mounting, which
also calls `updateMessageActions`. A synchronous callback cannot expose a
user-click window: mounting and the following listener registrations execute
in the same JavaScript task without an intervening await. Asynchronous metadata
completion runs after that task. Later transcript/recovery updates likewise
run through the existing action-state policy after setup. I found no early
asynchronous yield between mounting and submit-handler installation that would
reopen admission.

The change also prevents activation of a disabled default submit button before
the handler exists. It preserves early typing in the textarea and does not
alter the saved message, attachment or retry identity contract. If the required
JavaScript fails to initialize, leaving Send disabled is appropriate because
the native form path does not implement this application's delivery operation.

## Regression and compatibility

The browser regression delays the real `conversation.js` response and waits
for DOM content independently. It checks Send is disabled while that response
is held, releases the asset, and requires Send to become enabled before running
the existing recovery scenario. This would detect the old template behavior
deterministically. Removing the route barrier after the initial load preserves
the later reload/unknown/retry checks without reintroducing an unresolved
asset hold. Both Chromium and Firefox execute the same scenario.

This is a local template admission fix. Existing JavaScript remains the owner
of action eligibility; no parallel readiness framework is introduced. Server
authorization/origin checks, execution policy, provider delivery evidence and
persistence formats are unchanged. Established disabled-control styling and
interaction are reused. No new public API, user copy, compatibility shim or
upgrade procedure is needed. The initiative design records why the startup
default is conservative; the browser regression protects that invariant.

## History and remaining verification

The final runtime series is consolidated into exactly:

1. `2c847e6d265d2361cc7146b688dd9869353c1e53` — portal recovery behavior,
   startup correction, tests and owning documentation.
2. `10bb047513c82d1310e8fcaa797e8772f948dd8a` — one final provider dependency
   selection.

No obsolete branch iteration, follow-up fixup commit or repeated pin stream
remains in that series. Go and Nix both retain the previously accepted provider
`872c7ad3962f9fa9b17358244e27f3e3fac59fc5`; provider source is unchanged.
**Migration lineage: no migrations.** Schema 3 and the native protocol remain
unchanged. Downstream configuration/workspace pins still need final matching
identities and their ordinary consolidated-series checks.

Reviewer remains independent `/root/final_review` under saved
`gpt-6.1-sol/xhigh` settings. I read the packet, relevant guidance/review lanes,
design addendum, failure evidence, final diff and neighboring startup code.
Review used inspection and quick diff checks only; no source changes, long
tests or nested reviewers were used.

The packet's focused Go results permit proceeding, but prior runtime results
do not certify this final template/test revision. Remaining verification is
the final runtime package, real Chromium/Firefox startup and composer flows,
composition/system builds and exact new runtime CI. Deployment and live
continuity/recovery checks follow those results. The user's integration
authorization remains conditional on successful deployment and verification.
