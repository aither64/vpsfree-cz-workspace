# Browser download acceptance fixtures

Initiative: work/2026-09-14-portal-review-fixes.

A Playwright attachment download against the portal test server failed with
`download.delete: canceled` when the attachment was fulfilled by routing on a
self-signed HTTPS origin. Page-level `ignoreHTTPSErrors` alone did not make that fixture complete. Serve the attachment from the actual fixture HTTP
handler and launch isolated Chromium with `--ignore-certificate-errors` for
that test. Retain the normal portal TLS policy. Chromium and Firefox then
completed the download and verified that focus/visibility continued page reads.
