# Use the packaged full Chromium for layout probes

A standalone Playwright `chromium.launch({headless: true})` probe failed because
its Nix browser directory contained Chromium but not chromium_headless_shell.
Setting `channel: "chromium"` selected the existing full Chromium package and
passed the four-viewport portal layout reproduction. Keep NODE_PATH and
PLAYWRIGHT_BROWSERS_PATH from the matching Nix wrapper; do not download another
browser to work around the missing optional shell output.

Related initiative: `archive/2026-09-14-portal-planning-question-controls/`.
