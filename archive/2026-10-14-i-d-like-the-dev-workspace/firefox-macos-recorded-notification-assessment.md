# Firefox/macOS recorded notification, 2026-10-15

Bound session/environment and roster rev17 verified. Read-only source is clean
`469757183ba9491d642b56e91658dc64e390647b`; deployment identity is lead-reported.
The user's exact current Test result is:

> This test reached the browser and the browser accepted the display request. A matching notification is recorded. Check your screen to confirm it appeared.

This establishes a correlated Test receipt, resolved display call and a matching
browser notification record at the worker's post-display lookup. It is stronger
than provider acceptance and differs from the historical Linux API rejection.
It does not establish a visible banner or current presence in Notification Center.

Source findings in `portal/internal/web/static/`:

- `notification-worker.js:37-55` gives each explicit Test a fresh event-specific
  tag, attempts display, then records the matching lookup. Cleanup before display
  closes only strictly older Tests for that registration with different tags.
  It cannot close the Test currently being displayed. A later explicit Test can
  close this one; duplicate delivery replaces the same tag with `renotify:false`.
- `notification-worker.js:123-126` handles focus acknowledgement only for
  `session-<hex identity>` tags. Tests use a different identity/tag and are not
  closed by a focused document, session acknowledgement or presence. The Test
  branch also bypasses the session-status trust read.
- The other explicit close is `notificationclick` at line 104. Install/activate
  only skip waiting/claim clients; neither closes notifications. There is no
  Test expiry timer closing a displayed entry.
- `browser-notifications.js:29-43` cancels a local pending diagnostic, not the
  notification. Its result polling reads the saved post-display outcome; the
  quoted present status is historical evidence at that lookup, not continuous
  verification that the OS still shows the entry.

No immediate application-driven close is demonstrated for a single Test with no
later Test or click. The source does not establish an OS settings/Focus cause,
a Firefox defect, or a successful physical display. No application change is
justified by this evidence alone.

Smallest next check: inspect macOS Notification Center for the existing
`Workspace` / `Browser notification test` entry before sending another Test.
Presence there with no banner separates retained OS presentation from banner
visibility; absence leaves the browser-to-OS presentation boundary unresolved.
Lead owns official platform guidance and any later diagnostic. No repeat Test,
tab closure, settings reset or new probe is proposed here.

Only this tracking note was written. Historical assessments/sealed evidence,
design, product source, deployed state and active session remain unchanged.
