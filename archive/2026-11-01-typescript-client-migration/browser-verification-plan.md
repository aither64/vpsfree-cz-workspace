# Prepared synthetic browser verification

Prepared by implementer7 on 2026-11-01; accepted by the lead as a deferred A → B
batch. **Not executed.** Mandatory review is still active. This record authorizes
no browser, build, test, server, dependency installation, source change, or Git
mutation. The parent launches a fresh Luna/low verification watcher only after
review clears and the lead releases execution.

Preparation inspected WebUI HEAD
`aef727cff377c8368268bf61c881d173efe88ef5`, based on `63d`. On execution, the
parent must record and verify the reviewed source head. These exact commands and
artifact names describe the prepared head; a later reviewed head needs a distinct
artifact directory and recorded command identity, without overwriting this run.

Working directory for both commands:

```text
/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-01-typescript-client-migration/vpsadmin-webui
```

## Environment and ownership

- Use the repository's pinned Nix Node environment and installed Playwright
  wrapper. `e2e/PLAYWRIGHT_VERSION` and the installed CLI are 1.61.0.
- `node_modules/playwright-core/browsers.json` pins Chromium and headless shell
  revision 1228, version 149.0.7827.55. Both corresponding directories were
  present under `/home/aither/.cache/ms-playwright` during preparation. No browser
  was launched to establish runtime availability.
- Use the pinned browser. Do not add `--container`, system Chromium, browser
  downloads, policy relaxation, dependency installation, or sandbox bypasses.
  Missing browser binaries or shared libraries are environment findings to report.
- Confirm `127.0.0.1:5187` is free immediately before launch. `CI=1` prevents the
  Playwright web-server configuration from reusing another server. The wrapper
  starts this checkout's Vite server; native Playwright shutdown owns its cleanup.
- Clear inherited `E2E_STORAGE_STATE`, `E2E_CHROMIUM_EXECUTABLE_PATH`,
  `E2E_AUTO_SYSTEM_CHROMIUM`, `E2E_NO_ARTIFACTS`, and
  `E2E_RELAX_CHROMIUM_POLICY`. Preserve the ordinary matching Playwright browser
  cache; investigate a different inherited `PLAYWRIGHT_BROWSERS_PATH` before use.
- Keep the explicit loopback base URL. No deployed API, real credentials, browser
  storage state, production audit, or VM is part of this package.
- After execution release, the watcher may create the artifact root and its
  `captures` subdirectory:
  `/home/aither/workspace/ai/vpsfree.cz/work/2026-11-01-typescript-client-migration/browser-aef727cf`.
  Logs, HTML reports, screenshots, traces and videos are untracked session
  artifacts. Do not write captures into tracked product documentation.

## A: Core source and synthetic API regression

Expected duration is 3–8 minutes, with a native 15-minute global budget. Two
workers run the existing desktop and mobile Chromium projects. There are no
retries; the first failed test stops the batch. Each selected spec installs its
own synthetic HaveAPI fixtures.

Coverage: public and authenticated entry, session expiry, read recovery, static
host-IP actions, VPS-first IP assignment, VPS networking and mounts, advisory
updates and node actions, public registration correction, member requests,
HelpBox administration and contextual help, keys/sessions, member payment
instructions, administrator finance failure recovery and actual payment links.

```sh
nix develop -c env CI=1 E2E_BASE_URL=http://127.0.0.1:5187 E2E_START_SERVER=1 E2E_RECORD_ARTIFACTS=1 PLAYWRIGHT_HTML_OPEN=never PLAYWRIGHT_HTML_OUTPUT_DIR=/home/aither/workspace/ai/vpsfree.cz/work/2026-11-01-typescript-client-migration/browser-aef727cf/core-report node scripts/playwright.mjs test e2e/specs/public/overview.spec.ts e2e/specs/app/authenticated_home_smoke.spec.ts e2e/specs/app/session_expiry_redirect.spec.ts e2e/specs/admin/request_detail_error_recovery.spec.ts e2e/specs/admin/host_ip_addresses_responsive_actions.spec.ts e2e/specs/admin/ip_assignment_vps_first.spec.ts e2e/specs/app/vps_network_tab_actions.spec.ts e2e/specs/app/vps_storage_tab_mounts.spec.ts e2e/specs/app/security_advisory_update_mutations.spec.ts e2e/specs/admin/security_advisory_nodes_mobile_actions.spec.ts e2e/specs/app/public_registration_correction_smoke.spec.ts e2e/specs/app/user_requests_smoke.spec.ts e2e/specs/admin/help_boxes_responsive_actions.spec.ts e2e/specs/app/contextual_help_boxes_smoke.spec.ts e2e/specs/app/profile_keys_sessions.spec.ts e2e/specs/app/payments_page.spec.ts e2e/specs/admin/user_payments_failure_feedback.spec.ts e2e/specs/app/member_payment_links.spec.ts --project=chromium --project=mobile-chrome --workers=2 --retries=0 --trace=on --max-failures=1 --global-timeout=900000 --reporter=line,html --output=/home/aither/workspace/ai/vpsfree.cz/work/2026-11-01-typescript-client-migration/browser-aef727cf/core-results
```

## B: Existing bilingual rendered scenes

Run only after A passes. This selects eight existing cases across the two
projects: Czech and English user-data editor scenes and request-detail scenes.
Expected duration is 1–3 minutes, with a native five-minute global budget and the
same first-failure/no-retry rule.

```sh
nix develop -c env CI=1 E2E_BASE_URL=http://127.0.0.1:5187 E2E_START_SERVER=1 E2E_RECORD_ARTIFACTS=1 E2E_CENTERED_SCREENSHOTS=/home/aither/workspace/ai/vpsfree.cz/work/2026-11-01-typescript-client-migration/browser-aef727cf/captures PLAYWRIGHT_HTML_OPEN=never PLAYWRIGHT_HTML_OUTPUT_DIR=/home/aither/workspace/ai/vpsfree.cz/work/2026-11-01-typescript-client-migration/browser-aef727cf/capture-report node scripts/playwright.mjs test e2e/specs/app/profile_user_data.spec.ts e2e/specs/admin/requests_operations_smoke.spec.ts --grep='centered template editor and supported filters|address copy and risk emphasis' --project=chromium --project=mobile-chrome --workers=2 --retries=0 --trace=on --max-failures=1 --global-timeout=300000 --reporter=line,html --output=/home/aither/workspace/ai/vpsfree.cz/work/2026-11-01-typescript-client-migration/browser-aef727cf/capture-results
```

## Evidence and capture limits

`--trace=on` uses the installed runner's existing screenshots, snapshots and
sources support. Passing and failing scenes retain actual browser screencast
frames and the action/DOM timeline. A selected frame, identified by its timestamp
and resource SHA in the trace, is an actual viewport image. It is not a full-page
capture. Keep the trace and label each selected image with source head, test title,
actual `html.lang`, project and frame dimensions.

Default Desktop Chrome viewport is 1280×720; Pixel 5 is 393×727 CSS pixels at
device scale 2.75. Tests override these values: HelpBox mobile uses 320×900,
host-IP uses 1280/320×900, request desktop uses 1024×900, and user-data later uses
390/1280×460. Record actual frame dimensions instead of assuming defaults.

Existing direct screenshots in A include cs/en VPS-first dialog PNGs under each
test's output path. Member-payment direct PNGs are Czech only; English is
represented by its actual trace frames. B writes request-default-layout and
request-risk PNGs per locale and project. The user-data proof directory writes
Czech PNGs per project; English remains available in the trace. Do not set
single-file proof-image variables across projects, where output can overwrite.

The separate `screenshot_capture.spec.ts` supports only dashboard and
dataset-download scenes and forces a desktop viewport. It does not cover the
changed controls and is not needed for this batch.

These remain explicit capture gaps:

- The existing HelpBox scenario opens the localized editor, so its disabled clear
  option/explanation can appear in the actual trace. It uses default English and
  does not visit the stale `?language=` URL. There is no existing Czech reset scene.
- New template-unavailable gating, administrator paid-date clearing, traffic-search
  removal and OS-template-filter reset lack matching existing bilingual capture
  scenes in this batch.
- Existing traces and direct cs/en project PNGs are representative visual
  evidence. They do not establish full bilingual coverage for unvisited controls.
  Previously owner-checked rendered cs/en scenarios supplement these limits;
  review may identify a material remaining gap.
- Do not add a persistent capture framework or edit a spec to fill every gap.
  Any later required capture adaptation needs a bounded owner instruction.

## Failure handling and evidence boundaries

The parent selects and accepts commands. A fresh Luna/low watcher launches the
released batch, retains its execution handle and full logs, and reports exit
status, tested revision, elapsed time, last test and artifact paths. The watcher
does not diagnose, retry or edit. On a failure, stop before B and route evidence
to the original domain owner through the lead. Finance/content/correction
failures belong to implementer7; host/IP to implementer4/3, advisory to
implementer6, and user/session/account to implementer5. Shared policy and fixture
infrastructure findings go to implementer2.

Missing binaries/shared libraries, an unexpected nonlocal request, or native
budget expiry is incomplete evidence. Report the exact condition instead of
expanding the batch or changing dependencies. Native Playwright failure/timeout
owns stopping its local test/server operation; none of this authorizes a session
lifecycle action.

Read-only fixture hypotheses, **not observed test failures**:

- Host responsive fixture row 502 lacks its parent interface while expecting an
  Assign action.
- `payments_page.spec.ts` returns `hash.instructions` instead of canonical
  `user.instructions`.
- The advisory-update fixture has no parent revision.
- `profile_keys_sessions.spec.ts` contains the historical close action
  `POST user_sessions/1`.

Do not change these preemptively or widen production contracts. Diagnose only if
the actual released run fails.

These tests use Vite source and synthetic API replies. They do not certify a
production build, nginx/BFF deployment, API permissions or live backend behavior.
Package/build/bundle and isolated API checks remain separate parent-owned gates.
The KB workflow source is `873758fd6aec0c03f50a94600e0ceab97946f255`; its current
bindings describe legacy PHP rather than these React controls. Record actual
React impact and evidence in the owning WebUI work log; do not repin PHP
contracts to imply React coverage.
