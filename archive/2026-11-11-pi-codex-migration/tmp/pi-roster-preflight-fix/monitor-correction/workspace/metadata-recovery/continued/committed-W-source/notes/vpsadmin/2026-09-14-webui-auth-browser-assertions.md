# Use the existing WebUI login and notification assertions

Initiative: `work/2026-09-13-auth-email/`.

The new email-login browser scenario reached the WebUI, but an exact logout
value failed because the rendered value includes the account-menu dropdown
marker. Existing login helpers use a regex around `Logout (username)` and a
60-second transition timeout. Reuse that convention for staged login flows.

The subsequent enrollment succeeded, but looking for its success message in
`#content-in` failed. Notifications render in `#perex`, outside that content
area. Use `expectNotification` from `lib/pages/webui.cjs`; the broader content
assertion also produced a large diff dominated by the profile's time-zone list.

Keep a substantial new authentication scenario independently selectable when
iterating. This feature uses `webui#auth-email`, mapped to `auth` / `webui-auth`
CI tags; the existing 24 auth scenarios passed in both preceding runs.
