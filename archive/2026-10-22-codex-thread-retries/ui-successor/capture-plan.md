# B retry presentation capture

Owner: lead-selected fresh verification watcher, after committed affected review.
No capture run has started. The fixture uses the real TestQuestionBrowser HTTPS
server, session template, CSP and bundled assets. Its API responses are synthetic
and do not prove backend delivery, scheduling or session-policy persistence.

Run only `capture.sh` from this directory. It enters the B repository's locked
Nix development shell, changes to `portal`, and selects the single
`TestQuestionBrowser/retry_activity_browser_test.cjs` subtest with 240s Go timeout.
`environment.json` records evaluated, already-present Node/Playwright/browser
store paths from B's locked nixpkgs. No package build or browser installation is
needed. The full unrelated browser list remains unselected.

Store stdout/stderr and process exit/elapsed receipts here. The fixture writes
PNG images under `screenshots/`. Preserve a failed attempt before any correction;
return bounded evidence to implementer1 for source diagnosis, without retrying.

Expected desktop and mobile image names: capacity, cybersecurity, unconfirmed,
running, success, stopped, exhausted, dismissed, settings, member, idle, short,
and empty. The clock is installed and paused before navigation. Capacity capture
has exactly 3 confirmed starts, 15 seconds remaining and 70 seconds total
elapsed. Explicit later timer advances are assertions, never native dispatch.

The fixture also checks keyboard actions and Settings, revision conflicts,
shared root/member policy route, optional capability absence, browser-local
reload dismissal/new chain, composer focus/selection, live transcript updates,
filters, history prepend, legacy full render, short/empty bottom placement and
zero-height hidden/dismissed footer. Capture is presentation evidence only.
