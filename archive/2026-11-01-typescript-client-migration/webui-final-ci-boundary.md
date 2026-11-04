# Lead CI escalation disposition

Exact PR126/head14cfdcb6. CI run41366168908 completed success; all required
nonbrowser checks, production build and Chromium script regression passed.
Playwright smoke41366168907 remains active with jobs125026671252(chromium),
125026671379(mobile-webkit),125026671433(mobile-chrome).

The watcher's20-minute native timeout statement applies to the separate CI.yml
jobs and is incorrect for these smoke jobs. Actual committed
e2e-smoke.yml sets timeout-minutes40 and documents desktop smoke at about30min.
Lead disposition at escalation: continue the same exact jobs under the actual
40-minute bound, without cancellation, retry or source change. Running logs
are not yet available; no failure or pass is inferred from elapsed time.
The watcher retains this independently observable GitHub operation. This
record corrects the boundary without overwriting an active owner's snapshot.
