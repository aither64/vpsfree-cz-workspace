# 2026-06-14-vpsadmin-incident-filtering

## Goal

Add user-configurable filtering for vpsAdmin incident reports.

Each incident report gets a persisted boolean flag, proposed as
`allow_filtering`, that decides whether user rules may affect it. The flag is
visible in the API, visible in the admin incident report create form, and
defaults to `false` so existing reports and direct admin-created reports keep
the current behavior unless an admin deliberately opts in.

Eligible reports are evaluated against user-managed ordered rules. The first
matching rule decides whether to report or ignore the report. Reporting rules
may also choose the recipient policy for the user-facing mail. Ignored reports
remain saved in the database, do not send mail to the user, and are marked as
ignored. Reports store the deciding rule when one exists.

## Affected repositories

- `vpsadmin`
  - Core data model, migrations, filter evaluator, incident delivery paths.
  - HaveAPI resources/actions for rule and matcher management.
  - Existing incident report resource output/input fields.
  - PHP web UI pages/forms for rules and admin create/list/show views.
  - API, model, transaction chain, task, and web UI tests.
- `vpsfree-cz-configuration`
  - The deployed abuse notice parsers live here, including PROKI.
  - Automated parser-created incidents should set `allow_filtering: true`
    where filtering should be available.
- `vpsfree-mail-templates`
  - Filterable incident report mails should tell users near the end of the
    message that automated report delivery can be configured in vpsAdmin.
  - The note should link directly to the incident report rule management page.
- DokuWiki user documentation on `kb.vpsfree.cz` and `kb.vpsfree.org`
  - Existing incident pages should document rule behavior and examples.
  - Automation should use DokuWiki's remote API once a suitable token is
    available.

## Approach

### Data model

Add an additive migration in `vpsadmin/api`:

- `incident_reports.allow_filtering:boolean`, default `false`, not null.
- `incident_reports.ignored:boolean`, default `false`, not null.
- `incident_reports.incident_report_rule_id:bigint`, nullable.
- `incident_report_rules`
  - `user_id`, owner of the rule set.
  - `label`, optional user-visible name.
  - `position`, integer ordering within the user rule set.
  - `enabled`, default `true`.
  - `action`, enum: `report`, `ignore`.
  - `recipient_policy`, enum for report action, default `default`.
  - `hit_count`, incremented whenever the rule matches.
  - timestamps.
- `incident_report_rule_matchers`
  - `incident_report_rule_id`.
  - `field`, enum/string.
  - `operator`, enum/string.
  - `value`, string/text value.
  - timestamps.
- `incident_report_rule_recipients`
  - `incident_report_rule_id`.
  - `kind`, enum/string, initially `to` only unless `cc`/`bcc` is useful.
  - `address`, validated email address.
  - timestamps.

Suggested matcher fields for the first implementation:

- `vps_id`
- `ip_addr`
- `vps_hostname`
- `subject`
- `text`
- `codename`

Suggested operators:

- `equals`
- `not_equals`
- `contains`
- `excludes`
- `matches`
- `not_matches`

Rules are owned by users, not by VPSes. This keeps the feature genuinely
user-configurable across all of a user's VPSes, while still allowing a rule to
target one VPS with a `vps_id equals <id>` matcher. Admins can manage rules for
any user; normal users can manage only their own rules.

Multiple matchers on a rule are combined with AND. OR behavior is represented
by multiple rules. A rule with no matchers is a match-all rule; the implicit
fallback remains "report".

Recipient policy is used only when `action = report`:

- `default`: current behavior, deliver to the user's regular
  `vps_incident_report` recipients.
- `default_and_custom`: current recipients plus custom addresses stored on the
  matching rule.
- `custom`: only custom addresses stored on the matching rule.

For v1, custom recipients should be a small capped list, e.g. 10 addresses per
rule. Users can configure only their own rule recipients; admins can configure
any user's rule recipients.

### Evaluation semantics

Only reports with `allow_filtering = true` are evaluated. Reports with
`allow_filtering = false` are delivered exactly as today.

For an eligible report:

1. Load enabled rules for `incident_report.user`, ordered by `position, id`.
2. Find the first rule whose matchers all match and increment its `hit_count`.
   Rule evaluation has both per-regular-expression and per-incident time
   budgets; if the budget is exceeded, filtering falls back to the implicit
   `report` behavior.
3. If the matching rule action is `report`, set `incident_report_rule_id` to
   that rule, ensure `ignored = false`, and deliver according to that rule's
   recipient policy.
4. If the matching rule action is `ignore`, set `incident_report_rule_id` to
   that rule, set `ignored = true`, mark the report as processed/reported, and
   do not send mail or apply incident report side effects such as CPU limit or
   VPS action.
5. If no rule matches, use the implicit default action `report`. No rule link
   is stored for the implicit fallback.

This intentionally mirrors OOM report rules: no `continue` action in the first
version. A non-decisive observe/count action can be added later if there is a
clear operational need.

### Delivery integration

Filter evaluation has to cover both existing incident delivery paths:

- Mailbox/abuse parser path:
  - `VpsAdmin::API::IncidentReports::Handler` receives saved incidents from
    the configured parser and currently sends immediately through
    `TransactionChains::IncidentReport::Send`.
  - Evaluate eligible incidents before deciding whether to fire `Send` or only
    `Reply`.
  - Ignored incidents should still be included in the admin reply summary, but
    not in the user mail list.
- Custom recipients:
  - `MailTemplate.send_mail!` already accepts extra `to`, `cc`, and `bcc`
    arrays, which covers `default_and_custom`.
  - `custom` recipient policy needs a small extension to skip the default
    user/template recipients while still rendering the normal incident report
    template with the incident's user and VPS context.
- Direct/admin and pending task path:
  - `IncidentReport::Create` exposes `allow_filtering` to admins and defaults
    it to false.
  - `TransactionChains::IncidentReport::New` evaluates before sending and
    before applying side effects.
  - `VpsAdmin::API::Tasks::IncidentReport` and
    `TransactionChains::IncidentReport::Process` evaluate selected pending
    reports before sending or applying side effects.

The evaluator should be a small service object/module in the API layer, for
example `VpsAdmin::API::IncidentReportFilters`, rather than embedding the rule
logic directly in transaction chains.

### API design

Extend `incident_report`:

- Output fields: `allow_filtering`, `ignored`, `incident_report_rule`.
- Index filters: `allow_filtering`, `ignored`, `incident_report_rule`.
- Create input: `allow_filtering`, admin-only, default false.

Add resources:

- `incident_report_rule`
  - `index`, `show`, `create`, `update`, `delete`.
  - Fields: `user`, `label`, `position`, `enabled`, `action`,
    `recipient_policy`, `hit_count`, timestamps.
  - Authorization: admins can access all; users are restricted to their own
    `user_id`.
  - Limit rules per user, initially 100 like OOM report rules.
- `incident_report_rule.matcher`
  - Nested under a rule, like existing `mailbox.handler` and OOM subresources.
  - `index`, `show`, `create`, `update`, `delete`.
  - Fields: `field`, `operator`, `value`.
  - Authorization follows the parent rule.
  - Limit matchers per rule, initially 20.
- `incident_report_rule.recipient`
  - Nested under a rule.
  - `index`, `show`, `create`, `update`, `delete`.
  - Fields: `kind`, `address`.
  - Authorization follows the parent rule.
  - Limit recipients per rule, initially 10.

Use resource-level validation for field/operator compatibility. IDs should use
`equals`/`not_equals`; text-like fields can use all text and regular
expression operators. Provide human-friendly choice labels through HaveAPI
choice metadata (`choices: { values: ... }`) so clients can show labels such as
`default and custom` without hardcoding internal enum names.
Validate rule recipient configuration so `recipient_policy = custom` cannot be
saved without at least one recipient, and `action = ignore` does not require or
use recipients.

### Web UI design

Extend the existing `incidents` page instead of creating a new top-level page:

- `?page=incidents&action=rule_list`
  - Normal users see their own rules.
  - Admins open a specific user's rules from that user's profile; the list is
    always scoped to one user.
  - Table columns: enabled, action, label, matcher summary, hit count,
    recipient policy, edit, delete.
  - Ordering is adjusted by drag-and-drop when JavaScript is available and
    by up/down actions otherwise; direct position entry remains API-only.
  - Hit count links back to the incident list filtered by rule ID.
  - Show the implicit final rule as label `Implicit rule` with an enabled
    boolean icon and no toggle.
- `rule_new`, `rule_edit`, `rule_delete`
  - Manage the rule itself.
  - Manage matchers inline in the rule edit view with the add form as the
    final table row.
  - Manage custom recipients inline in the rule edit view with the add form
    as the final table row.
  - Confirm rule deletion because it removes nested matchers and recipients.
- Incident list filters add `ignored`, `allow_filtering`, and rule ID.
- Incident list rows show ignored status and the deciding rule when included.
- Incident show includes:
  - `Allow filtering`
  - `Ignored`
  - Deciding rule link, or `-` for no explicit rule.
- Admin new incident form includes an `allow_filtering` checkbox defaulting to
  unchecked.

### vpsfree-cz-configuration

The production PROKI parser and the other automated abuse notice parsers live
in `configs/vpsadmin/api/abuse_notice_parser/*.rb`. Update parser-created
incidents that should be user-filterable to set `allow_filtering: true`.

This should include PROKI. It can include the other automated abuse parsers
too, since they share the same mailbox/parser delivery path and represent
machine-generated abuse notices rather than direct admin reports.

### Mail templates and documentation

Update `vps_incident_report` in `vpsfree-mail-templates` so reports with
`allow_filtering = true` include a short note near the end of the plain text
mail. The report content and incident-specific action guidance must stay first.
The note links to:

`https://vpsadmin.vpsfree.cz/?page=incidents&action=rule_list`

Use a defensive `respond_to?(:allow_filtering)` guard in the template so the
template can be deployed before all vpsAdmin instances have the new attribute.

The WebUI rule list page is already addressable as
`?page=incidents&action=rule_list`. Existing help-box rendering keys off the
current `page` and `action`, so documentation links can be configured there
without adding more WebUI code.

Documentation should be added to the existing DokuWiki pages:

- English: `manuals:vps:incidents`
  (`https://kb.vpsfree.org/manuals/vps/incidents`)
- Czech: `navody:vps:incidenty`
  (`https://kb.vpsfree.cz/navody/vps/incidenty`)

The docs should explain that filtering applies only to automated reports,
admin-sent reports are always delivered, the first matching enabled rule wins,
multiple matchers in one rule are ANDed, the fallback is report, ignored
reports remain visible in vpsAdmin, report rules can set custom recipients,
and give concrete examples.

## Compatibility and deployment

- All vpsAdmin database changes are additive. Existing rows get
  `allow_filtering = false`, `ignored = false`, and no rule link, preserving
  current behavior.
- The new code can run with existing parser configuration: parser-created
  reports remain unfilterable until the configuration repo starts setting
  `allow_filtering: true`.
- Deployment order:
  1. Deploy vpsAdmin with the migration and API/web UI support, but ensure the
     database migration is applied before the new API/mailbox-processing code
     is allowed to process incident reports.
  2. Run migrations before starting or re-enabling vpsAdmin services that call
     the incident report filter evaluator.
  3. Update `vpsfree-cz-configuration` so selected automated parsers set
     `allow_filtering: true`.
- Do not deploy the configuration change before the vpsAdmin migration is
  available, otherwise parser code may try to assign an unknown or missing
  column.
- Mail template changes are forward compatible with old vpsAdmin versions
  because the filter-management note is guarded by
  `respond_to?(:allow_filtering)`.
- Rolling/mixed-version behavior:
  - Old reports and old parser output continue to report normally.
  - New reports with `allow_filtering = true` require new code to evaluate
    rules; once such reports exist, rollback should either keep the new schema
    columns or first stop setting `allow_filtering` in parser configuration.
- No vpsAdminOS node-wide coordinated update is expected. This is an API,
  database, mailbox-processing, and web UI feature.
- Ignored eligible reports should still be visible in incident history and in
  metrics/daily reporting unless a later implementation explicitly decides to
  exclude them.

## Testing plan

### vpsadmin quick tests

- API model specs for matcher operators, AND matcher evaluation, first-match
  ordering, report, ignore, implicit default report, and counter increments.
- Specs proving reports with `allow_filtering = false` bypass rules.
- Specs proving ignored reports are saved, linked to the deciding rule,
  marked `ignored`, and not mailed.
- Specs proving report rules can use default recipients, add custom
  recipients, or replace default recipients with custom recipients.
- `IncidentReports::Handler` specs for mailbox-created eligible incidents.
- `TransactionChains::IncidentReport::New` and `Process` specs for side-effect
  suppression on ignored reports.
- API resource specs for `incident_report_rule` and nested matchers,
  including normal-user authorization boundaries.
- Extend `incident_report` resource specs for new fields and create input.
- Update API endpoint coverage and `.github/workflows/api-specs.yml` topic
  patterns for any new spec files.
- Web UI tests where practical, likely extending existing support/incidents
  browser coverage.
- Update `tests/ci-selection.yml` if new runtime paths/specs need explicit
  integration CI selection.

### vpsfree-cz-configuration quick tests

- Extend parser specs to assert PROKI-created incidents have
  `allow_filtering = true`.
- If other abuse parsers are enabled, update their specs similarly.

### vpsfree-mail-templates quick tests

- Compile the changed ERB templates.
- There is no standalone template unit test suite; API-backed `rake test`
  requires credentials and an API endpoint.

### Commands to run during implementation

- In `vpsadmin`: use the appropriate Nix shell, then targeted API specs such
  as `bundle exec rspec api/spec/lib/vpsadmin/api/incident_reports_spec.rb`,
  rule resource specs, incident report resource specs, and transaction chain
  specs.
- In `vpsadmin`: run `ruby tests/ci-selection-test.rb` when changing CI
  selection rules.
- In `vpsadmin`: run relevant web UI test(s) with
  `./test-runner.sh test 'webui#<script-name>'` if web UI behavior is covered.
- In `vpsfree-cz-configuration`: run the relevant RSpec parser specs from the
  repository dev shell.
- Before committing: install/activate declared hook frameworks and let
  Overcommit run. The initial worktree creation showed Overcommit is present
  but not installed in the ambient shell.

### Mandatory review

After implementation commits and quick local verification, run the
`mandatory-change-review` skill with:

- this plan and `state.md`;
- affected worktrees and branches;
- base/head commits for all affected repositories;
- migration and compatibility assumptions;
- quick verification results;
- any known deployment ordering notes.
