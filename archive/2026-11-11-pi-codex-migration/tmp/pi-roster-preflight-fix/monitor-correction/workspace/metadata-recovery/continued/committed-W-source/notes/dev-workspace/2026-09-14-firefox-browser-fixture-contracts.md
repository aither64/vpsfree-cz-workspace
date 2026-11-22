# Firefox browser fixture behavior

The portal repository fixture was originally Chromium-only. Running it with
Firefox exposed assumptions in its inputs, rather than a diff model failure:

- A 3,000px Playwright wheel event moved only 770px in an 808px pane. Choose an
  explicit scroll position when testing sticky geometry, and account for
  fractional element heights rather than comparing rounded offsetHeight exactly.
- Reloading after history.pushState retained an extra same-URL history entry.
  A minimal HTML server with no portal code reproduced root -> parent -> parent
  -> original across three page.goBack calls, after pushing parent, reloading,
  then pushing root. Test reload in a separate tab from the back-stack assertions;
  this preserves both contracts without assuming identical browser internals.
- A focus-triggered details refresh can coalesce with an in-flight refresh.
  The lifecycle fixture must stimulate focus until the deliberately held read
  starts, rather than wait for a read that it may never have triggered.

The real-template sidebar/settings acceptance passes both engines. The lifecycle
fixture also passes both engines with the corrected held-read stimulus.
Related initiative: work/2026-09-14-portal-review-fixes.
