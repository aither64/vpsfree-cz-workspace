# Risk and compatibility review: email refinement follow-up

Lane: RISK AND COMPATIBILITY

Model/effort: `gpt-5.6-sol` / `xhigh`

Reviewed the exact follow-up series:

- vpsAdmin `cf2c8734c9091327cbc9157d43915695e9750bc5..d6f51b6e8ad9d78c68e6d0f0ce5276ca610e7bf8`
  (`95a67e55e9695b5a7f56b491af186840c389f444` and
  `d6f51b6e8ad9d78c68e6d0f0ce5276ca610e7bf8`)
- vpsfree-notification-templates
  `06f03bad4294b6f28ca9478e907f43967ebeb7d0..97ac666a390fc028c5b610b48c9963adb9e0b4ef`

I also inspected the authentication proof creation and code-exchange checks,
session/device trust transition, mail renderer and variable contract, DNS and
user-agent helpers, NixOS template reconciliation units, and the current
production topology in `vpsfree-cz-configuration` (`int.api1` and `int.api2`
as shared-database API backends, with replacement-template reconciliation on
`int.api1`).

## Findings

### Important: document and enforce template-first rollback before old API workers return

The forward mixed-version requirement is documented: new API workers support
the old text templates, and `doc/email-login-verification.mdwn:53` says to
update all API workers before installing templates that use the new details.
The reverse operation is not documented. The downgrade paragraph at
`doc/email-login-verification.mdwn:75` addresses pending challenges and loss of
email enforcement, but it does not state that the template revision must be
rolled back before any pre-follow-up worker serves requests.

That order is required. The revised templates render `@service_name`,
`@requested_at`, `@device`, and `@ip_ptr`; for example the built-in English
HTML template calls `local_time(@requested_at, ...)` at
`api/notification_templates/templates/user_login_email_verification/email/en.html.erb:23`.
The pre-follow-up chain at `cf2c8734c` supplies only `user`, `code`,
`expires_at`, `ip_address`, `user_agent`, and `support_mail`. A missing
`@requested_at` is `nil`, and `TimeZones.format_time` reaches
`Time.parse(value.to_s)` at `api/lib/vpsadmin/api/time_zones.rb:45`, which
raises for the empty string. An opted-in unknown-device login handled by that
worker therefore cannot render or send its verification mail. This fails
closed, but prevents the affected user from signing in.

The production consequence is cross-node: `int.api1` and `int.api2` both serve
API traffic from HAProxy and share the database, while `int.api1` reconciles
the replacement template source into that database. Rolling `int.api2` back
first, or otherwise returning any pre-follow-up worker while the revised
templates remain installed, creates the incompatible combination.

Record a rollback procedure that first reconciles the earlier templates while
all serving workers still run the new API, and only then rolls every API worker
back. For the current topology, a combined rollback must update the
template-owning `int.api1` first so it restores the old shared templates before
`int.api2` is downgraded. Also state that pending challenges created by the
pre-follow-up implementation do not support resend through the follow-up API,
consistent with the packet's explicit decision not to support intermediate
branch challenge formats.

## Residual risks and test gaps

- The new API remains compatible with old templates because it retains the old
  `ip_address` and `user_agent` variables. Existing mail is already rendered,
  so queued messages do not depend on a later template version.
- The packet explicitly excludes compatibility with pending challenges made by
  the undeployed intermediate feature. In such a mixed follow-up rollout, an
  old challenge has no `service_name`; verification can complete, but resend
  through the new chain raises at `opts.fetch('service_name')`. Production
  enrollment must therefore stay off until the final API and templates are in
  place, and an installation already running the intermediate feature must
  drain pending challenges before upgrading.
- Reverse DNS now occurs before the shared rate-bucket locks but still under the
  existing per-user lock. This adds resolver latency to challenge creation.
  It does not broaden address trust: the same proxy-derived client address and
  existing DNS helper are used, dynamic values are escaped in HTML, and a
  correct password plus policy checks are required before this path is reached.
- Notification suppression uses server-persisted authorization evidence and is
  reached only after `EmailLogin.check_authority!` rechecks the evidence at
  OAuth code exchange. The change does not mark a device known earlier: the
  device update remains after successful session creation. Password/device and
  MFA evidence still send the notice. I found no authorization bypass, trust
  regression, HTML injection, recipient expansion, schema change, or node
  compatibility issue in this follow-up.

No Blocking findings.
