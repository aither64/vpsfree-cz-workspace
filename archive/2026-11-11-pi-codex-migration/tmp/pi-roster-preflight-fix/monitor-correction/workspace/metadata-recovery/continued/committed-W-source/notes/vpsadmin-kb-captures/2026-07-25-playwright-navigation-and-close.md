# Playwright notification capture navigation and close

Related initiative: `work/2026-06-15-vpsadmin-events`.

## Symptom

Repeated full notification capture runs occasionally failed during
`page.goto()` with `net::ERR_ABORTED; maybe frame was detached?`, even though
the WebUI container had not restarted and continued returning HTTP 200.
Successful runs could also print `Captured 26 checkpoint(s)` and write
`tmp/capture-results.json`, then remain in browser shutdown until the wrapper
was terminated.

## Finding

The WebUI container, nginx, and PHP-FPM stayed active throughout the failures.
The abort was transient browser navigation behavior while the development
cluster was responding slowly, not an application or fixture assertion.
The shutdown hang happened after all checkpoint output and result metadata had
already been written.

## Workaround and verification

Rerun the complete language scenario after a navigation abort; fixture
preparation is idempotent. After a run prints the complete checkpoint count,
it is safe to terminate only the idle wrapper if the browser process is gone.
Immediately run `nix develop -c bin/validate --update` for that language, then
run `nix develop -c bin/check` after both languages.

For this initiative, both final language runs produced all 26 checkpoints.
The final inventory contained 86 concepts and 172 PNG variants, and both
contract test suites passed with 69 total assertions.
