# Testing an immediate checkbox rollback

In session `2026-09-30-portal-review-improvements`, the Firefox presentation
fixture failed at Playwright `uncheck()` after an intentional HTTP 503. The
portal correctly restored the saved Keep open value before Playwright checked
that the checkbox was unchecked. Chromium passed the same fixture.

For an action that intentionally rolls back immediately, assert its initial
state, register a response observer, and use a normal click. Verify the exact
request method/path/body and expected error response, then assert the restored
state and visible error. Requiring the temporary state after the failed request
adds a race with correct recovery behavior.

The corrected fixture verified POST `hold:false`, status 503, and the saved
checked state with its error diagnostics. Both Chromium and Firefox passed in
the repository's Nix environment. The change is test-only; no delay, retry or
production adjustment was needed.

Related initiative: [design and verification brief](../../work/2026-09-30-portal-review-improvements/design.md).
