# WebUI notification tests need ordinary mail enabled

In `tests/suite/webui.nix`, `ensure_webui_user` sets `mailer_enabled: false`
while leaving `enable_new_login_notification: true`. Mandatory authentication
mail still works, so a verification-code test alone does not reveal that
ordinary new-device notices are disabled.

When testing notification suppression, explicitly enable both settings on the
specific fixture account. Assert that an ordinary initial login produces one
new-device message before asserting that email verification produces no second
message. This prevents a vacuous passing suppression check.

The raw HaveAPI mail-log response exposes `mail_template` as an object with
`id`, `label` and `_meta`; compare `mail.mail_template.id` against the fixture's
actual `MailTemplate` ID rather than assuming a scalar or fixed database ID.

Related initiative: `work/2026-09-13-auth-email/`. Focused API notification tests
and the browser scenario with the positive baseline passed. The final browser
run completed on 2026-09-14 at 15:48:52 +0200, with the example taking 103.77s.
