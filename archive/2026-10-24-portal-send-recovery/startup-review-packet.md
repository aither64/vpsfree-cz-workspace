# Composer startup admission review

Retain your saved model/effort and independence. Review only the new startup
boundary, affected general/architecture/risk lanes, and final runtime series.
Read mandatory review and packet. No edits or long checks.

Runtime previous1b562996 -> final10bb047513c82d1310e8fcaa797e8772f948dd8a;
base b3a6eb2f. Provider872c7ad remains unchanged and accepted. Runtime stays two
commits: functional2c847e6d plus one final dependency update10bb0475. No migrations.
Prior findings and cancellation fixes unchanged; no repeated pin stream.

Final-browser.log revealed composer_handoff_browser_test line224 after reload:
no new message request, no page error; upload controls mounted only after the
click. Initial HTML enables Send for an interactive session, while app.js awaits
conversation asset import before installing form submit handler. Thus a fast
post-reload click can native-submit before durable JavaScript handoff. This is a
real startup admission gap, not a delivery response timeout.

Fix: render Send disabled unconditionally; existing updateMessageActions enables
it after composer/submit listeners are installed. No other control/copy/API or
persisted-state changes. Browser regression now delays conversation.js, checks
Send disabled in initial DOM, releases asset and checks normal Send enabled,
then runs original unknown/success/replacement/retry scenario in Chromium/Firefox.
Route barrier is removed after first load to preserve reload coverage.

Focused Go Composer|SubmissionNotice|Conversation checks pass (1.224s), provider
package/native tests passed exact872c7ad, runtime CI fast+archive passed at1b562996
before this template correction. New runtime CI will replace the old run. No
activation or deployment has happened. Conditional user merge direction unchanged.

Write startup-review-report.md here; assess startup gap, enable ordering and
regression validity. Final runtime package/browser/composition/system builds
and new exact CI remain required after review.
