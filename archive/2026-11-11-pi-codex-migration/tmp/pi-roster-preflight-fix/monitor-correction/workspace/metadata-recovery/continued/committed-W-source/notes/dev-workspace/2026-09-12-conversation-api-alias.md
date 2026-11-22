# Browser conversation API aliases

Related initiative: work/2026-09-12-portal-review-experience.

The shared conversation client can use a consumer-supplied conversationPath.
The portal uses /api/sessions/:slug, even though /codex/conversations/:slug
is also served. Adding an endpoint only to codex-web left the browser activity
request returning404 and the timing summary unavailable. Direct API tests
against /codex/conversations/:slug/activity had passed.

Keep the portal legacyConversationPath mapping current for browser-used
operations and verify the path requested by the actual page. The activity GET
now forwards through the shared resolver; route/canonical-path tests pass.
