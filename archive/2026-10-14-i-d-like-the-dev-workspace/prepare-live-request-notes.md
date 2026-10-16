# Live verification notes

Prepared test harness is session evidence, not product source. Run after profile
activation under browser-verification-env.sh, with actual vendor push enabled
(no mocked subscription/showNotification). Profiles are disposable; only their
own registrations may be removed. Headless getNotifications can establish worker
notification creation on Linux but cannot establish OS display on macOS.

No credentials/subscription endpoints/keys belong in logs. Read Basic credentials
in process memory from trusted root@172.16.106.40 only. Use the installed public
CA for ordinary HTTPS health; Playwright context ignores host CA validation in
its disposable profiles. These settings are never persisted to the user's browser.

The test action is delayed ten seconds. Close all portal tabs, leave a different
page active, and keep browser running. Reopen to inspect generic provider status
and notification presence; distinguish provider acceptance from worker receipt
and OS display. A provider network failure must remain explicit, with no product
fallback to page-dependent notifications. User's actual Firefox/macOS and Chrome
builds still need their own explicit permission/test action.
