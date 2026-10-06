# 2026-06-06-vpsadmin-user-timezone

## Goal

Allow vpsAdmin users to configure an IANA time zone for their account. Use it
whenever vpsAdmin presents date/time values to that user, especially in e-mail
templates. Add the setting to the vpsAdmin web UI profile page and to the
public vpsFree.cz registration form, where it should default to the browser's
current time zone.

## Affected repositories

- `vpsadmin`
  - API user model/resource and migrations.
  - `requests` plugin registration request model/resource and migrations.
  - vpsAdmin PHP web UI profile form and request-local time zone setup.
  - Mail template rendering helpers and built-in/plugin templates that present
    dates.
  - API and web UI tests.
- `web`
  - Shared registration form classes.
  - English and Czech registration form fragments.
  - Registration form JavaScript.
  - Registration request submission.
  - Selenium/RSpec registration specs, or a replacement focused form test if
    practical.
- `vpsfree-mail-templates`
  - External vpsFree.cz mail templates consumed by vpsAdmin.
- `vpsfree-cz-configuration`
  - `aitherdev` host configuration.
  - Internal DNS zone records for the aitherdev devcluster web names.
- Workspace `dev-clusters/vpsadmin`
  - Devcluster default domains, URL output, source worktree detection, and
    services VM nginx/PHP-FPM configuration for the public web.

## Approach

1. Persist the user setting in vpsAdmin.
   - Add `users.time_zone`, stored as an IANA identifier string such as
     `Europe/Prague` or `America/New_York`.
   - Validate with `TZInfo::Timezone.get` or equivalent IANA identifier lookup.
   - Expose `time_zone` in `VpsAdmin::API::Resources::User` writable/common
     params.
   - Add it to `User` validations and PaperTrail tracked fields.
   - Include `time_zone` in the non-admin self-update whitelist, next to
     `language`, `mailer_enabled`, and other profile preferences.

2. Carry the setting through registration requests.
   - Add `user_requests.time_zone` in the `requests` plugin migration.
   - Add `time_zone` to `RegistrationRequest` validation and API request
     params.
   - Include it in preview/update output for correction resubmissions.
   - In `RegistrationRequest#approve`, copy `time_zone` to the newly created
     `User`.
   - Keep the field optional at API level during rollout unless we decide to
     force all registration clients to send it.

3. Make webui use the account time zone.
   - Add a Time zone field to `print_editm()` on `webui/pages/page_adminm.php`,
     in the account/profile settings section where normal users can already
     change language and mail notifications immediately.
   - Submit `time_zone` in the `edit_member` update params.
   - After authenticating the current user in `webui/public/index.php`, load
     or refresh the current user including `time_zone`, store it in the session,
     and call `date_default_timezone_set($timeZone)` for the request.
   - Ensure context switching sets the borrowed user's time zone and regaining
     admin restores the admin user's time zone.
   - `tolocaltz()` can remain the central formatter, because it already uses
     `date_default_timezone_get()`.

4. Make mail templates timezone-aware.
   - Extend `MailTemplateTranslation::TemplateBuilder` to accept the delivery
     user or an explicit time zone and expose helpers such as:
     - `local_time(value, format = '%Y-%m-%d %H:%M %Z')`
     - `local_date(value, format = '%Y-%m-%d')`
   - `MailTemplate.send_mail!` should pass `opts[:user]&.time_zone` into the
     builder. For mails without a user, preserve current server-local behavior
     or use an explicitly supplied `:time_zone`.
   - Update built-in and plugin mail templates that currently use
     `.localtime.strftime(...)` for user-visible date/time values. The highest
     impact templates found are:
     - account lifetime and VPS lifetime expiration templates;
     - login/token/TOTP/failed-login security mails;
     - snapshot download readiness;
     - VPS OOM, incident, migration and resource/change notifications;
     - security advisory announce/update templates;
     - outage report announce/update templates in `plugins/outage_reports`;
     - payment overview templates in `plugins/payments`.
   - Treat date-only payment period fields as dates and leave them unchanged
     unless they represent a moment in time.

5. Update the public website registration flow.
   - Add `time_zone` to `RegistrationForm` validation/data handling and
     correction preview restoration.
   - Add a time zone field to both English and Czech registration forms.
     Use `DateTimeZone::listIdentifiers()` for options.
   - Update `js/form.js` to set the field to
     `Intl.DateTimeFormat().resolvedOptions().timeZone` when the user has not
     already selected a value. The existing dynamic form reload state handling
     should preserve manual changes.
   - Include `time_zone` in `Registration#register()` request params.

6. Update external mail templates.
   - Convert timestamp/date-time rendering in `vpsfree-mail-templates` to the
     vpsAdmin `local_time` and `local_date` helpers.
   - Keep pure business dates such as membership validity and payment periods
     as date values unless they represent a specific timestamp.

7. Move aitherdev web domains to the vpsAdmin dev cluster.
   - Add `web-cs.aitherdev.int.vpsfree.cz` and
     `web-en.aitherdev.int.vpsfree.cz` to the devcluster default domains and
     certificate/URL handling.
   - Detect `worktrees/<slug>/web`, mount it into the services VM, generate a
     dev `config.php` pointing to the devcluster API, and serve Czech/English
     vhosts through nginx/PHP-FPM.
   - Remove the old local `containers.vpsfree-web` from the `aitherdev`
     machine in `vpsfree-cz-configuration`.
   - Change internal DNS CNAMEs for `web-cs.aitherdev.int` and
     `web-en.aitherdev.int` to point to
     `frontend.aitherdev.int.vpsfree.cz.`.

## Compatibility and deployment

- Database changes are additive. Existing users and registration requests can
  keep `time_zone = NULL` if we choose the conservative rollout.
- Decision: `NULL` means "use the deployment/server
  default", preserving current `.localtime` and PHP default-time-zone behavior
  until the user changes the setting.
- The registration API should initially accept missing `time_zone` so an older
  deployed `web` repository can continue to create registration requests while
  the vpsAdmin API is upgraded.
- The `web` repository can be deployed after vpsAdmin accepts the new field.
  Deploying `web` first would make registration submissions fail against an
  older API that does not know the new input parameter, depending on HaveAPI's
  unknown-parameter behavior.
- External `vpsfree-mail-templates` using `local_time`/`local_date` must be
  uploaded only after vpsAdmin with those helpers is deployed.
- Moving `web-cs.aitherdev.int` and `web-en.aitherdev.int` to the devcluster
  intentionally stops serving them from the standalone `aitherdev` web
  container. The devcluster certificate may need to be reissued to include the
  new names.
- Rollback of vpsAdmin code after new rows have `time_zone` populated is safe
  if the database column remains in place; old code will ignore the column.
- Removing the column during rollback is unsafe while newer `web` code sends
  the parameter or newer templates expect the helper, so rollback should keep
  additive migrations unless all application code has been rolled back.
- No vpsAdminOS coordinated node update is required. This is API/webui/mail
  rendering and website code only.

## Testing plan

- vpsAdmin API specs:
  - User create/update accepts valid IANA time zones and rejects invalid values.
  - Normal users can update their own `time_zone` but not another user's.
  - User show/current includes `time_zone`.
  - Registration create/preview/update persists `time_zone`.
  - Registration approval copies `time_zone` to the created user.
  - Mail template rendering formats a known UTC timestamp differently for two
    users with different time zones.
- vpsAdmin webui tests:
  - A focused regression test for API choice rendering or a page-level test that
    the profile form includes and submits `time_zone`.
  - If practical, a Playwright webui test for profile update and visible
    `tolocaltz()` output after changing the account time zone.
- vpsAdmin commands:
  - `cd api && bundle exec rspec api/spec/api/resources/user_write_spec.rb`
  - `cd api && bundle exec rspec api/spec/api/plugins/requests/registration_spec.rb`
  - a focused mail template spec file once added.
  - `composer install --working-dir=webui` if needed, then
    `composer --working-dir=webui test` or targeted PHPUnit.
  - `bundle exec rubocop` for touched Ruby code and the repository hook suite
    through Overcommit before committing.
- web repository:
  - Add/adjust registration specs to ensure the time zone field exists, defaults
    from browser JS, and is submitted.
  - Run `bundle exec rake spec` or the repository's Nix shell equivalent.
- vpsfree-mail-templates:
  - Compile all `meta.rb` files and ERB files in the repo Nix shell.
  - Run `bundle exec rake test API=<dev-api>` before uploading templates to a
    running API.
- devcluster/configuration:
  - `jq empty dev-clusters/vpsadmin/default-config.json`
  - `bash -n dev-clusters/vpsadmin/bin/devcluster`
  - `nix build --impure ... dev-clusters/vpsadmin#cluster-config` with the
    active source worktrees wired in.
  - `confctl build --yes cz.vpsfree/machines/aitherdev`
  - `confctl build --yes --tag all-internal-dns`

## Decisions

- Existing users keep `users.time_zone = NULL` until they configure their own
  time zone.
- The public registration form should show a visible time zone select and
  auto-select the browser-detected value when possible.
- Follow-up user notification:
  - Do not use a modal/pop-up. Show a non-intrusive sidebar tip only when the
    user's account time zone is unset, the browser reports a valid IANA time
    zone, and that browser time zone differs from the server default.
  - Remember the tip through a generic webui per-user key-value store rather
    than a dedicated one-off tips table.
  - Keep the store scoped to webui and current-user-owned settings. Limit it to
    registered namespaces and enforce server-side quotas: 64 keys per user,
    8 KiB per serialized value, and 64 KiB total serialized value data per
    user.
  - The time-zone tip should offer one-click use of the browser time zone and a
    dismiss action that keeps the server default.

## Follow-up: webui tips and key-value store

### Approach

1. Add `webui_user_settings` to the `webui` plugin instead of core schema.
   - Fields: `user_id`, `namespace`, `key`, serialized JSON `value`, and
     timestamps.
   - Unique key: `(user_id, namespace, key)`.
   - Allowed namespaces start as `forms`, `tips`, and `ui`.
   - Writes use an idempotent `PUT /webui_user_settings/{namespace}/{key}` API
     action scoped to the current user.

2. Add webui rendering and JavaScript for the time-zone tip.
   - Server renders the sidebar fragment hidden by default only when the user
     still has no configured time zone and has not dismissed the tip.
   - Browser JS validates `Intl.DateTimeFormat().resolvedOptions().timeZone`
     against PHP's `DateTimeZone::listIdentifiers()` before revealing the tip.
   - One-click apply updates the current user's `time_zone` through the
     existing self-update API and then remembers the tip.
   - Dismiss stores the tip state without changing the user's time zone.

3. Add test coverage.
   - API specs for current-user scoping, idempotent set, show/list/delete, and
     quota validation.
   - Existing webui self-service Playwright suite gets isolated users for:
     setting browser time zone, dismissing the tip, and suppressing it when the
     browser uses the server default.

### Compatibility

- This is additive to the `webui` plugin schema.
- Older webui code ignores the new resource/table.
- New webui code degrades safely against an API without the resource: the
  server may render a hidden candidate fragment, but browser JS will not reveal
  it without the `webui_user_setting.set` action.
- Rollback is safe with the table left in place. Deleting the table while new
  webui code is deployed would only break the optional tip persistence, not
  core account time-zone behavior.
