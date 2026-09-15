# Block background queue reconciliation in read-only review probes

Opening a repository comparison also starts the session page's background
`POST /api/sessions/<slug>/queue/reconcile`. A browser probe that blocked all
non-GET/HEAD requests correctly prevented writes, but its assertion that the
page would attempt no writes failed after the actual diff checks passed.

Keep the route block, record the blocked requests, and assert that any expected
background attempts have exactly that method/path. Continue rejecting other
mutation attempts. Do not allow queue reconciliation on a foreign session merely
to make a read-only rendering test pass. The retried Chromium candidate probe
passed both layouts, continuous character spans, line link, totals and asset checks.

Related: `work/2026-09-15-portal-diff-highlighting/verify-browser.cjs`.
