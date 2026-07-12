# Playwright assertions across HTML line breaks

## Symptom

`./test-runner.sh test 'webui#vps-user-core'` timed out in an exact warning
assertion even though the failure output showed all expected sentences.

## Cause

The warning used `<br>` between sentences. DOM `textContent` does not insert
spaces for `<br>`, so a single expected string containing spaces between the
sentences could never be a substring of the rendered form text.

## Fix

Assert each exact sentence independently against the same form locator. This
checks the wording without assuming how line-break elements contribute to DOM
text.

## Verification

After correcting and autosquashing the test, all declared hooks passed and the
same `webui#vps-user-core` VM scenario passed all four Playwright tests and the
complete test in 2,446.25 seconds.

Related initiative: `work/2026-07-10-czech-translation-fixes/`.
