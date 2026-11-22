# Wait for scrollable content in repository browser acceptance

Live acceptance initially sent a wheel event while comparison editors still had
placeholder height. The pane clamped scrolling before lazy content arrived.
Requiring every editor then deadlocked the mobile check because offscreen files
intentionally remain unloaded.

Wait for at least one real `.review-code-view`, completed syntax highlighting in
loaded views, and a scroll range large enough to move the details out of view.
Do not require offscreen editors to load. Navigate with `domcontentloaded` and
explicit DOM readiness: `networkidle` cannot settle while the portal SSE
connection remains open. Diagnostic geometry distinguished harness readiness
from product behavior; no product fix was needed.

Related initiative: work/2026-09-12-portal-review-experience/compact-verification.md.
