# Two-path readiness candidate — PREPARED ONLY

Base: **965aadc51dfb4a7d838a401b20ecafa38c8a70db**, the exact source inspected
with the failed corrected-run receipts. Imp3 owns only its disjoint recovery
fixture and B Git; neither these source paths nor any B state were changed here.
No interim source head, pins or guards were consumed. No test, syntax/browser
check, build, probe, Git mutation or CI wait ran during this preparation.

`candidate.patch` changes ONLY:

- `page_lifecycle_browser_test.cjs`: synchronize fresh details admission and
  positively identify the actual stale reply through construction, fulfillment
  and application to the browser DOM.
- `team_settings_browser_test.cjs`: scope the Team tab to the exact named
  Session sections tablist, preserving the separate transcript Team filter.

`manifest.json` records exact base/candidate hashes. `base-965/` preserves the
originals; `candidate/` holds proposed contents; `inverse.patch` and
`inverse-reconstructed-base/` retain inverse provenance. The generated per-file
forward/inverse unified hunks were independently applied **in memory** to prove
candidate and base reconstruction; `inverse-reconstruction.json` binds the
identical base SHA256 values. No patch was applied to B.

## Nonvacuous stale-read proof

The existing count increments before `route.fetch()`/`response.json()`, so request
start is not stale-response completion. The candidate captures state, notice ID,
dismissal and stale-case classification BEFORE those awaits. A reply is assigned
an incrementing fixture-only number after its normal details body arrives, and
must contradict a completed dismissal. The route deliberately returns
`noticeDismissed:false`, with its original notice ID, and appends a hidden numeric
marker to the existing mocked `repositoriesHTML`. Fulfilled count advances only
AFTER awaited `route.fulfill`.

The ONE existing default **5-second** `expect.poll` requires all four phases:
new request started, stale body constructed, stale reply fulfilled and its exact
marker present under `#repositories`. Ordinary focus is redispatched only while
no successor request is admitted, preserving the production singleflight lane.
The numeric `details > beforeStaleRefresh` assertion is retained explicitly.

Marker consumption proves real details application: current app.js3382 applies
recovery status BEFORE installing `repositoriesHTML` at3403. This is an existing
fixture response field and normal DOM consumer, not a production hook/helper or
new protocol. The marker is hidden, carries only an incrementing number and does
not touch the composer or live state. `staleNoticeRead` stays true until all four
phases and the hidden-panel assertion complete, then clears at the original point.
Existing draft/same-composer/no-send/hidden assertions remain unchanged.
Diagnostics are only phase booleans/counters. There is no longer deadline, sleep,
transport retry, forced action, new live request or weaker assertion.

The source/log supports a possible one-shot-focus/admission race; it does not
prove the exact old runtime slot interleaving. The strengthened fixture must
establish that evidence during the later authorized run. A fresh failure still
needs diagnosis; no product or universal-performance conclusion is inferred.

## Commands after explicit source transfer and committed inspection

Quick, NOT RUN:

```sh
nix develop --no-update-lock-file -c bash -c 'set -e
node --check portal/internal/web/page_lifecycle_browser_test.cjs
node --check portal/internal/web/team_settings_browser_test.cjs
git diff --check
'
```

Parent fresh-Luna runtime, NOT RUN, from B with the final exact source guard and
paired session markers verified before exports:

```sh
PORTAL_BROWSER_TEST=1 \
DEV_WORKSPACES_CODEX_PROVIDERS=/tmp/portal-followup-absent-providers.json \
NODE_PATH=/nix/store/fg778x0631ld4xd8fim2kbvxll5715xp-playwright-test-1.59.1/lib/node_modules \
PLAYWRIGHT_BROWSERS_PATH=/nix/store/f0rap655j6wmqbfvqdw445kwcxkxwf7n-playwright-browsers \
nix develop --no-update-lock-file -c go -C portal test -mod=readonly \
 -overlay /tmp/portal-followup-browser-assets-overlay.json ./internal/web \
 -run '^TestQuestionBrowser$/^(page_lifecycle_browser_test[.]cjs|team_settings_browser_test[.]cjs)$' \
 -count=1 -timeout=20m -v
```

Retain the same rooted matched browser/review assets, absent provider sentinel
and independent fresh logs/status/time. Existing failed965 receipts are untouched.
All later lifecycle stale/reload/new-notice/timing/navigation checks and the full
Firefox iteration, plus later Team metrics/member settings, remain unverified.
Imp2 Firefox-pending and imp3 delivery-recovery work remain separate. No product,
API, schema, authority, visible prose or design change is proposed.
