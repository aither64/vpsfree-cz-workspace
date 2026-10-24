# Prepared ordinary WebUI browser verification

PREPARED ONLY; no test/server/browser has launched. Wait for final-review
acceptance, explicit lead launch release, and owner0 utility-slot release.

Exact candidate: WebUI 8772bab21cd8739bf4672cdf4976aea2a6e59de3; HaveAPI
f94e65e35166a0bf8048a27c9d57c7d36957d65b through the committed normal dependency.
Any changed source/head/manifest/lock requires parent reassessment before launch.

Proposed watcher command: `bash ABS_PATH_TO_THIS_DIRECTORY/run.sh` once.
This only invokes the existing ordinary scripts/playwright.mjs/config and the
nine approved specs. CI=1 refuses reuse of an existing server; explicit retries=0
and max-failures=1 retain first-failure behavior. It starts the ordinary npm dev
server through the existing config and tests the normal application entry. No
pilot, alternate transport, source mode switch, host policy edit, system-browser
fallback, browser install or probe is added. Normal Playwright owns its webServer
process lifecycle. There is no separate cleanup operation.

Each run gets its own retained runs/ordinary.* directory with preflight log,
verification log, browser/operation exact exit statuses, Playwright JSON+HTML,
failed-test traces/screenshots/videos, and final source/lock status. The script
does not retry or diagnose. Metadata failures do not turn a browser failure green.

Retained Chromium/headless-shell revision1228, expected149.0.7827.55, and ffmpeg
paths exist and are executable. Installed and declared CLI are1.61.0; manifest
SHA256 is ee39bc924bc3d1bd895626c2910f1292d109bbfeeb5abd113acb45e1951cc942.
These are static identity/availability checks, not engine-launch proof.

The ordinary existing runner serves Vite dev. It has no production-preview
selection. The separately authorized default npm build checks BFF/minified
production output; this browser command does not claim to execute that minified
output or certify live OAuth, backend permissions or infrastructure operations.
Testing a production preview would require adapting ordinary BFF bootstrap
fixtures to /config.json and /session.json, rather than silently selecting legacy
mode. No such new fixture work or harness is included in this preparation.
