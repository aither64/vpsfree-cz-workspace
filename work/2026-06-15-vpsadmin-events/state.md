# 2026-06-15-vpsadmin-events

## Repositories

- `vpsadmin`
  - Worktree:
    `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-06-15-vpsadmin-events/vpsadmin`
  - Branch: `2026-06-15-vpsadmin-events`
  - Base: `origin/master`
  - Current base/head before local commits:
    `6351e273ed257f5e3233a99ffa7d8eae9221856a`
  - Current feature head:
    `4c6d0dc01803a9e0f1b7c6739c0e2d00060d7358`
  - Remote: `git@github.com:vpsfreecz/vpsadmin.git`
- `vpsfree-notification-templates`
  - Worktree:
    `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-06-15-vpsadmin-events/vpsfree-notification-templates`
  - Branch: `2026-06-15-vpsadmin-events`
  - Base: `origin/master`
  - Current head:
    `2074fe28446ec43212e4e2f2fa9001d2624bd6d3`
  - Remote: `git@github.com:vpsfreecz/vpsfree-notification-templates.git`
  - Note: local worktree/reference renamed from the historical
    `vpsfree-mail-templates` naming for this managed template deployment
    slice.
- `vpsfree-cz-configuration`
  - Worktree:
    `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-06-15-vpsadmin-events/vpsfree-cz-configuration`
  - Branch: `2026-06-15-vpsadmin-events`
  - Base: `origin/master`
  - Current head:
    `b58aa05c0e95a3e46dcd49909261847e16e366ed`
  - Remote: `git@github.com:vpsfreecz/vpsfree-cz-configuration.git`
- `vpsfree-sms-gateway`
  - Worktree:
    `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-06-15-vpsadmin-events/vpsfree-sms-gateway`
  - Branch: `2026-06-15-vpsadmin-events`
  - Base: new local repository, no upstream commits
  - Current head:
    `730b35c652d0efb596bfe290d0afea76e494a678`
  - Remote: `git@github.com:vpsfreecz/vpsfree-sms-gateway.git`
  - Note: GitHub reported repository not found earlier on 2026-06-22; user
    created it later. The feature branch was pushed successfully.
- `vpsadmin-kb-captures`
  - Worktree:
    `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-06-15-vpsadmin-events/vpsadmin-kb-captures`
  - Branch: `2026-06-15-vpsadmin-events`
  - Base: `origin/master`
  - Initial head: `7248a8b`
  - Remote: `git@github.com:vpsfreecz/vpsadmin-kb-captures.git`

## Status

- Active workspace session: `2026-06-15-vpsadmin-events`.
- 2026-07-22 reusable event time-interval and KB documentation slice started.
  - The existing initiative and vpsAdmin branch are being extended; no new
    initiative slug was created.
  - Product decisions: full Alertmanager-style calendar fields, stable time
    zone per named interval, same-day start-inclusive/end-exclusive time
    ranges, Alertmanager-like route-tree behavior, blocked deletion while
    referenced, and dedicated top-level bilingual Notifications articles.
  - New documentation page IDs are `navody:notifikace` and
    `manuals:notifications`.
  - Prepared the dedicated `vpsadmin-kb-captures` worktree listed above from
    current `origin/master`; its local `AGENTS.md` and canonical WebUI change
    workflow were read before changes.
- 2026-06-30 event routing cleanup slice started in `vpsadmin` only.
  - Requested outcome: implement the finalized route/event plan: replace
    special default-route matching with a `default_routed` matcher, make
    parent/child receiver delivery additive, stamp notification release
    transactions on deliveries, abort unsent transaction-gated deliveries when
    chains fail or roll back, and clean up related WebUI display issues.
  - Worktree:
    `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-06-15-vpsadmin-events/vpsadmin`
  - Branch: `2026-06-15-vpsadmin-events`
  - Current pre-change head:
    `94fd280ddcacff729568c74137e2733e9f4e8ead`
    (`notification_templates: install managed templates from API`)
  - Compatibility decision: this branch is still in development; dev-cluster
    state may be reset and no migration transition period is required.
  - Design decisions:
    - use matcher key `default_routed`, not `event.default` or
      `event_type.default_routed`;
    - keep events as audit records when transaction chains fail;
    - use only `event_deliveries.transaction_id` for notification transaction
      provenance and derive transaction-chain links through that relation;
    - abort unsent transaction-gated deliveries instead of deleting events.
- Worktrees prepared for `vpsadmin`, `vpsfree-notification-templates`, and
  `vpsfree-cz-configuration`.
- Repository-local `AGENTS.md` files read for all prepared worktrees.
- Existing incident-filtering session notes were reviewed for context.
- Current `vpsadmin` branch is based on `origin/master`; the discarded
  incident-filtering branch was used only as inspiration.
- Previous `vpsadmin` implementation head:
  `ac7f8a2617ae3e7c440ffd55ee44c03f52c0768f`
  (`notifications: add event routing foundation`).
- Previous `vpsadmin` implementation head:
  `dbf5caeabeba857215e06eee3de8b2148fcbaeb6`
  (`notifications: harden routed delivery edge cases`).
- Current `vpsadmin` head:
  `252d7f635a1684d449d9b2b4b0b593e2ef2fb0bc`.
- Current `vpsadmin` worktree is clean after splitting the migration test
  infrastructure, migration specs, routing-context migration, legacy-recipient
  migration, WebUI route-scope work, SMS template registration, and a direct
  event e-mail delivery fix into separate commits.
- Revised design implemented in `vpsadmin`:
  - Alertmanager-style routes and receivers replace the earlier
    rules/endpoints naming.
  - Additive migration/schema for `notification_receivers`,
    `notification_receiver_actions`, `event_routes`,
    `event_route_matchers`, `events`, and `event_deliveries`.
  - Default receiver/route backfill preserves `users.mailer_enabled`: enabled
    users get a default e-mail receiver/action; disabled users get a muted
    "Do not notify" receiver.
  - `User` creates default notification routing lazily/after create when the
    new tables exist.
  - `VpsAdmin::API::Events` registry/router supports typed event fields,
    nested routes, receiver fallback, sibling `continue`, muted receivers,
    multi-action fan-out, delivery deduplication, and event log attribution.
  - Event types now include `user.test_notification`, user account/security
    mail events, `vps.incident_report`, `vps.oom_report`, and
    `vps.oom_prevention`; converted mail paths emit these events before
    e-mail delivery is prepared and later released.
  - HaveAPI resources expose `event`, `event.delivery`, `event_type`,
    `event_route`, `event_route.matcher`, `notification_receiver`, and
    `notification_receiver.action`.
  - Webhook action secrets are redacted from API output, but `secret_present`
    is exposed for UI display.
  - Event deliveries are now prepared during routing and then released either
    by `Transactions::EventDelivery::Release` in transaction chains or by the
    API after commit for direct events.
  - Webhooks are delivered by a long-running notification dispatcher, with
    static JSON payload snapshots, `X-VpsAdmin-Signature-256`,
    retries/backoff, generic delivery-attempt tracking, response tracking, and
    private address blocking by default.
  - Telegram receiver actions were removed from the current implementation
    frame. The schema and dispatcher design remain prepared for future
    actions.
  - E-mail receiver actions render through existing `MailTemplate`/`MailLog`
    templates at preparation time; the long-running e-mail dispatcher later
    sends the `MailLog` snapshot via SMTP and records generic delivery
    attempts. Custom e-mail targets send only to the configured target.
  - OOM report rules are now represented in event routing:
    - matcher operators include glob sigils `=*` and `!*`, using the same
      `File.fnmatch?` flags as legacy OOM cgroup rules;
    - the events migration backfills legacy OOM `ignore` rules to muted
      receivers and OOM `notify` rules to the generated default receiver;
    - the supervisor plans a transient `vps.oom_report` event for users with
      OOM-specific event routes, and marks the stored raw OOM report as
      ignored only when the final plan is suppressed by an enabled muted
      receiver;
    - legacy OOM report rule API write actions are deprecated and left
      read-only, and the old WebUI rule actions redirect to notification
      routes;
    - users without OOM-specific event routes still use the legacy
      `oom_report_rules` lookup.
- WebUI revised:
  - one Notifications page with Routes, Receivers, Event Log, Event Types, and
    Test Event views;
  - route ordering with drag-and-drop plus up/down links;
  - matcher field dropdown sourced from event type metadata;
  - receiver action forms for e-mail, Telegram, and webhook, including webhook
    optional secret;
  - event detail shows delivery state/action/receiver/result metadata;
  - old `rules`/`endpoints` actions redirect to `routes`/`receivers`;
  - user admin page no longer exposes the old mailer-enabled checkbox;
  - old advanced e-mail role/template WebUI actions redirect users to
    Notifications.
- `vpsfree-mail-templates` and `vpsfree-cz-configuration` worktrees remain
  clean; template normalization and production config changes are deferred to
  later slices.
- Remaining gaps recorded in `plan.md`:
  - remove the legacy OOM rule table/API/WebUI helpers after deployment;
  - remove `users.mailer_enabled` after all senders use events;
  - migrate remaining mail call sites to emit events;
  - implement the Telegram bot and Telegram delivery adapter;
  - rework mail-template machinery and template naming for non-mail actions.
- Historical command entries below that mention `event_rule` or
  `notification_endpoint` are from the superseded first prototype. The current
  implementation and commit use `event_route` and `notification_receiver`.

## Latest checkpoint

- 2026-07-08 `vpsadmin` was rebased onto current `origin/master`.
  - New `vpsadmin` base:
    `6351e273ed257f5e3233a99ffa7d8eae9221856a`
    (`i18n: capitalize Czech privileges label`).
  - New `vpsadmin` head after rebase:
    `4c6d0dc01803a9e0f1b7c6739c0e2d00060d7358`
    (`hooks: isolate API i18n bundle`).
  - Conflict decisions:
    - removed obsolete e-mail role/template recipient WebUI and Playwright
      flows where master and the feature branch now use notification routes;
    - kept deletion of the standalone notification-template uploader gem in
      favor of API-managed templates;
    - regenerated API and WebUI locale catalogs after taking the parseable
      rebased side of generated translation conflicts, then restored/fixed all
      event metadata translations before continuing;
    - merged the event metadata i18n defaults into master's
      `runtime_i18n_defaults` API catalog path instead of preserving the
      older feature-branch helper name.
  - Verification after rebase:
    - `nix develop .#api -c bundle exec rake vpsadmin:i18n:health`: passed;
    - `nix develop -c webui/lang/scripts/locales-health`: passed, with the
      existing gettext warning about an embedded URL in
      `forms/oom_reports.forms.php`;
    - `ruby -c api/lib/vpsadmin/api/i18n/catalog.rb`: passed;
    - `git diff --check`: passed;
    - targeted scans found no conflict markers or untranslated/fuzzy entries
      in the conflicted locale/catalog files.
  - The dev cluster was not started.
  - Current `vpsadmin` worktree is clean after rebase. The local branch is
    intentionally ahead of and behind the old remote feature branch because
    the rebase rewrote history and was not pushed.

- 2026-07-08 pushed the rebased `vpsadmin` branch and watched GitHub Actions.
  - Pushed `2026-06-15-vpsadmin-events` with `--force-with-lease` from old
    remote head `94fd280dd` to `4c6d0dc01803a9e0f1b7c6739c0e2d00060d7358`.
  - No superseded queued or in-progress old-head workflow runs were present
    immediately after the push.
  - New-head workflow results before the follow-up fix:
    - passed: Client Specs, RuboCop, API Migration Specs, Console Router
      Specs, Webui PHPUnit, Download Mounter Specs, i18n health, and
      libnodectld Specs;
    - failed: API Specs (topic parallel), run `28951361200`;
    - still running at the time the API failure was triaged: CI run
      `28951362473`.
  - API Specs failed in both engine jobs:
    - `85898670174` API specs (core) - engine;
    - `85898670316` API specs (full) - engine.
  - Failed examples were traced to real branch/rebase drift, not GitHub
    infrastructure:
    - `NotificationTemplate.send_email!` no longer fell back to English when
      the selected user language lacked a variant;
    - the full-engine default-template check treated request type/state
      candidate templates such as `request_create_user_registration` as
      required shipped defaults even though request events intentionally fall
      back to generic request templates;
    - stale specs still expected `parameters` instead of `payload`;
    - stale muted-delivery expectations still looked for `does not notify`
      while the current skipped reason for disabled delivery methods is
      `delivery method is disabled`.
  - Follow-up commit:
    `560f6e430c658e5435c300c734619a5035c86e59`
    `api: fix notification template fallback`.
  - Fix summary:
    - notification template rendering now falls back to English variants for
      e-mail, Telegram, and SMS when the requested language variant is
      missing;
    - request plugin type/state-specific template registrations are marked
      `default: false`, and `required_default_templates` ignores optional
      registrations so only shipped fallback defaults are required;
    - stale engine specs were updated for event `payload` naming and current
      skipped-delivery error summaries.
  - Local verification for the follow-up:
    - `ruby -c` passed for `api/models/notification_template.rb`,
      `api/lib/vpsadmin/api/notification_templates.rb`, and
      `plugins/requests/meta.rb`;
    - `git diff --check`: passed;
    - focused RuboCop on the touched API/plugin/spec files: 9 files
      inspected, no offenses;
    - targeted reproduced failures: 6 examples, 0 failures;
    - `VPSADMIN_PLUGINS=none nix develop .#api -c bundle exec rspec
      --format progress spec/models`: 945 examples, 0 failures, 63 pending;
    - `VPSADMIN_PLUGINS=all nix develop .#api -c bundle exec rspec
      --format progress spec/models`: 945 examples, 0 failures, 3 pending.
  - Commit hooks passed in `nix develop .#vpsadmin`: Nixfmt,
    MigrationSpecs, VpsadminWebuiI18n, RuboCop, VpsadminApiI18n; commit-msg
    hooks passed with warnings only at the repository's stricter 72-column
    threshold, while all commit message lines were verified to be at most
    80 columns.
  - Mandatory change review for commit `560f6e430` was launched with
    standalone reviewer `Carver`
    (`019f425b-783a-7361-bd0d-4ef1332203e3`).

- 2026-07-05 `vpsadmin` was rebased onto current `origin/master`.
  - New `vpsadmin` head after rebase:
    `155b6197a` (`webui: refine event type matcher reference`).
  - Rebase preserved master API/WebUI localization and migration-spec harness.
    Duplicate migration-spec commits from the feature branch were skipped or
    reduced to no-ops where master already contained the implementation.
  - Conflict decisions:
    - `api/db/schema.rb` keeps the master schema version
      `2026_07_03_120000` while retaining feature migration effects.
    - protocol-aware `NotificationTemplate` code replaced legacy
      `MailTemplate` conflicts.
    - old e-mail recipient API/resources/specs were removed only in the
      legacy-recipient-to-route migration commit, and the API spec matrix was
      adjusted there.
    - `notification_templates/` standalone gem files were deleted in favor of
      API-managed templates under `api/notification_templates`.
    - master's localized WebUI language/time-zone form was kept while merging
      notification delivery method controls.
  - Current `vpsadmin` worktree is clean after rebase.

- 2026-07-01 Event Types / route matcher usability slice implemented and
  committed in `vpsadmin`:
  `252d7f635a1684d449d9b2b4b0b593e2ef2fb0bc`
  (`notifications: clarify event matcher fields`).
  - Requested outcome: make the Event Types page useful as a route matcher
    reference, remove the old event-field `parameter()`/`parameters()` DSL,
    require explicit field types, flatten matcher field names, distinguish
    matchable fields from payload/template vars, and support list matching
    with `contains`/`not_contains`.
  - Compatibility decision: no compatibility aliases or old
    `parameters:`/`parameters.*` route matcher surface were preserved because
    the branch is still development-only.
  - API/model changes:
    - `VpsAdmin::API::Events` now exposes typed `field`, `payload`, and
      `extra_payload` declarations; all field definitions require explicit
      types and there is no type inference fallback.
    - The old event-field `parameter()`/`parameters()` DSL was removed rather
      than kept as a compatibility alias.
    - Event emission/planning call sites now pass `payload:` instead of
      `parameters:`.
    - Event route matchers use flat matchable field names and validate
      operators against field type metadata.
    - Supported list field types are `string_list` and `integer_list`, with
      `contains`/`not_contains` operators.
    - Object/list payloads that are not directly matchable remain in payload
      only; matchable scalar/list derivatives were added where needed.
    - Webhook payloads now include `payload` and route-matchable `fields`,
      not `parameters`.
    - API resources expose event type `fields` metadata with name,
      description, type, example, operators, and choices.
  - Event catalog work:
    - core and plugin event declarations were converted from
      `parameter(...)` to explicitly typed `field(...)`;
    - derived matchable fields were added for concerns, affected VPS lists,
      outage changed fields, OOM cgroups/reports, OOM VPS identity, security
      advisory VPS lists, and dataset migration affected VPS lists.
  - WebUI changes:
    - Event Types page now groups events by collapsible category, renders one
      event block per event, moves severity/default routed to vertical rows,
      shows field type/operators/example/meaning, and includes sidebar quick
      links for all events;
    - matcher add/edit forms filter operator choices by selected field;
    - matcher forms show an operator/type reference table;
    - event detail and test-event forms use payload wording/API fields.
  - Mandatory change review:
    - standalone reviewer `Franklin`
      (`019f1f8c-c543-7df0-822d-0e3c691d3bb1`) reviewed the committed slice
      after quick local verification;
    - blocking findings fixed before final commit:
      WebUI test-event submit still posted `parameters_json`, raw undeclared
      payload keys could match when another event type declared the same key,
      and the WebUI regression expectation still used the previous helper
      surface;
    - important finding fixed before final commit:
      webhook `event.fields` now includes persisted routing-context fields by
      passing `delivery.event_routing_context` to
      `matchable_field_values(...)`;
    - the review also noted that the large commit was acceptable for this
      branch because the changes are tightly coupled around the matcher-field
      contract.
  - Verification:
    - stale public/event-facing scan found no `parameter()`/`parameters()` DSL,
      `parameters_json`, `extra_parameters`, or `infer_type`;
    - `php -l webui/forms/notifications.forms.php`: passed;
    - Ruby syntax check on changed Ruby files: passed;
    - `git diff --check`: passed;
    - `nix develop .#api -c bundle exec rubocop`: passed for 1394 files;
    - Overcommit hooks ran during commit from the root Nix shell after the
      ambient shell reported the `overcommit` gem missing; final pre-commit
      hooks passed: Nixfmt, MigrationSpecs, PhpCsFixer, RuboCop; commit-msg
      hooks passed: SingleLineSubject, TrailingPeriod, TextWidth;
    - focused event/matcher specs:
      `nix develop .#api -c bundle exec rspec --format progress
      spec/models/event_route_spec.rb
      spec/api/resources/event_routing_spec.rb
      spec/api/resources/transaction_chain_read_spec.rb
      spec/supervisor/node/oom_reports_spec.rb
      spec/models/notification_templates_spec.rb:524`
      passed with 105 examples, 0 failures, 1 expected pending;
    - broader affected non-migration specs:
      `spec/models/tasks/event_delivery_spec.rb`,
      `spec/models/notification_templates_spec.rb`,
      `spec/models/notification_events_spec.rb`,
      `spec/models/security_advisory_spec.rb`,
      `spec/models/transaction_chain_spec.rb`,
      `spec/models/transaction_chains/lifetimes/expiration_warning_spec.rb`,
      `spec/models/transaction_chains/plugins/requests/create_spec.rb`,
      `spec/supervisor/node/transaction_chain_events_spec.rb`, and
      `spec/api/resources/user_write_spec.rb`
      passed with 185 examples, 0 failures, 1 expected pending;
    - migration specs run separately to avoid migration DB contamination:
      `spec/migrations/20260615110000_add_events_spec.rb` and
      `spec/migrations/20260624121000_migrate_legacy_email_recipients_to_routes_spec.rb`
      passed with 8 examples, 0 failures.
    - after review fixes, syntax checks passed for
      `webui/pages/page_notifications.php`,
      `webui/tests/Regression/NotificationRouteUiTest.php`, and all changed
      Ruby files;
    - after review fixes,
      `nix develop .#webui -c composer test -- --filter
      NotificationRouteUiTest` passed with 10 tests and 84 assertions;
    - after review fixes, focused API regression examples passed:
      `spec/models/event_route_spec.rb:235`,
      `spec/models/event_route_spec.rb:267`, and
      `spec/models/tasks/event_delivery_spec.rb:1812`;
    - after review fixes, wider affected API specs passed with 186 examples,
      0 failures, and 1 expected pending:
      `spec/models/event_route_spec.rb`,
      `spec/api/resources/event_routing_spec.rb`,
      `spec/api/resources/transaction_chain_read_spec.rb`,
      `spec/supervisor/node/oom_reports_spec.rb`, and
      `spec/models/tasks/event_delivery_spec.rb`;
    - after review fixes,
      `nix develop .#api -c bundle exec rubocop` passed for 1394 files;
    - final `php -l` checks, `git diff --check`, and the stale public scan for
      `parameters_json`, event-field `parameter()`/`parameters()` DSL,
      `extra_parameters`, and `infer_type` passed with no remaining matches.
  - Pending: push if this slice should be published for CI/review.

- 2026-06-29 notification template managed deployment slice implemented and
  pushed:
  - requested outcome: rename/deploy notification templates from a flake
    input, improve Telegram rendering, render admin reasons as safe Markdown
    in HTML-capable templates, and remove the standalone uploader in favor of
    an API rake task;
  - active worktrees:
    - `vpsadmin`:
      `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-06-15-vpsadmin-events/vpsadmin`
      on branch `2026-06-15-vpsadmin-events`;
    - `vpsfree-notification-templates`:
      `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-06-15-vpsadmin-events/vpsfree-notification-templates`
      on branch `2026-06-15-vpsadmin-events`;
    - `vpsfree-cz-configuration`:
      `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-06-15-vpsadmin-events/vpsfree-cz-configuration`
      on branch `2026-06-15-vpsadmin-events`;
  - repository-local `AGENTS.md` files were re-read for all three worktrees.
  - `vpsadmin` local changes:
    - added `VpsAdmin::API::NotificationTemplates.install_managed!`, source id
      tracking in `sysconfig`, and a database row lock for concurrent API
      service starts;
    - added `vpsadmin:notification_templates:install_managed`, reading
      `TEMPLATE_PATH`/`TEMPLATE_PATHS` and `SOURCE_ID`;
    - added `markdown_html` and `markdown_telegram_html` template helpers
      using Redcarpet with raw HTML/images/styles disabled and Telegram HTML
      sanitized to supported tags;
    - made generic Telegram HTML keep useful blank lines and descriptive link
      labels such as `VPS details`, `event details`, and
      `security advisory`;
    - made `vps_resources_change` Telegram HTML render as the requested block:
      linked title, current CPU/memory/swap limits, reason/changed-by, and
      `Link: VPS details`;
    - changed synthetic `user.test_notification` deliveries to ignore
      route-specific/event-specific template names for e-mail, Telegram, and
      SMS rendering, avoiding missing-variable failures;
    - removed the standalone `notification_templates/` uploader directory and
      updated internal references;
    - added NixOS option `vpsadmin.api.managedNotificationTemplates` and
      service `preStart` install after API database setup.
  - `vpsfree-notification-templates` local changes:
    - remote/worktree use the new
      `git@github.com:vpsfreecz/vpsfree-notification-templates.git` name;
    - removed uploader dependencies/tasks from the template repo;
    - exposed the `templates/` tree as the flake default package;
    - updated README/AGENTS for managed API-side installation;
    - updated Telegram HTML templates for descriptive WebUI link labels and
      Markdown-rendered reasons, while leaving text templates as fallbacks;
    - changed `vps_resources_change` Telegram HTML in English and Czech to the
      requested readable block layout.
  - `vpsfree-cz-configuration` local changes:
    - added flake input `vpsfreeNotificationTemplates` pointing at the new
      GitHub repository and feature branch;
    - added confctl channel/role `vpsfree-notification-templates`;
    - added that channel to `int.api1` and `int.api2`;
    - configured common vpsAdmin API settings to pass the template package and
      flake revision source id to the new managed install option;
    - flake input pins were updated through `confctl inputs channel set
      --commit`, not by manually editing `flake.lock`.
  - quick checks already run:
    - `git diff --check` passed in all three worktrees;
    - template stale-label searches found no `open in vpsAdmin` or Czech
      equivalent in managed templates;
    - stale uploader reference searches in `vpsadmin` found no remaining
      `vpsadmin-notification-templates`, `notification_templates/vpsadmin`,
      `NotificationTemplates::VERSION`, or uploader wording;
    - API syntax checks passed for
      `lib/vpsadmin/api/notifications.rb`,
      `models/notification_template_variant.rb`, and
      `lib/vpsadmin/api/notification_templates.rb`;
    - focused API specs passed:
      `nix develop .#api -c bundle exec rspec --format documentation
      spec/models/notification_templates_spec.rb
      spec/models/tasks/event_delivery_spec.rb`: 103 examples, 0 failures;
    - focused API RuboCop passed for touched API files;
    - template repo `nix develop -c bundle exec rake check` passed, checking
      664 template files;
    - template repo `nix build .#` passed;
    - nixfmt was run on touched Nix files in `vpsadmin`,
      `vpsfree-notification-templates`, and `vpsfree-cz-configuration`.
  - pending:
    - aggregate GitHub Actions `CI` for `vpsadmin` head `f942e79bd` is still
      running at the time of this note; it was monitored for about ten
      minutes with `gh run watch 28404844693 --exit-status` and remained in
      the selected integration-test `Run tests` step.
  - completed after the initial checkpoint:
    - Overcommit hooks installed and verified in `vpsadmin` and
      `vpsfree-cz-configuration`;
    - final focused API specs after the Telegram sanitizer patch:
      `nix develop ..#api -c bundle exec rspec --format documentation
      spec/models/notification_templates_spec.rb
      spec/models/tasks/event_delivery_spec.rb`: 103 examples, 0 failures;
    - final focused API RuboCop passed for touched API files;
    - final template repo `nix develop -c bundle exec rake check` passed,
      checking 664 files;
    - final template repo `nix build .#` passed;
    - `vpsadmin` committed and pushed:
      `f942e79bd316d022143addb0dc4fdd54b7e3a724`
      (`notification_templates: install managed templates from API`);
    - `vpsfree-notification-templates` committed and pushed, then amended and
      force-pushed with an explicit lease after review:
      `2074fe28446ec43212e4e2f2fa9001d2624bd6d3`
      (`templates: expose managed notification package`);
    - `vpsfree-cz-configuration` committed and pushed:
      `b8a882b988be794b6f749ee185ce1740c9d925a0`
      (`vpsadmin-config: install managed notification templates`);
    - confctl generated the template input pin, then it was amended during a
      non-interactive rebase after the template advisory fix:
      `c0c2875b` (`inputs: set vpsfreeNotificationTemplates to 2074fe28`);
    - confctl generated and pushed vpsAdmin input pin, replayed by that
      rebase:
      `b58aa05c0e95a3e46dcd49909261847e16e366ed`
      (`inputs: set vpsadminServices to f942e79b`);
    - `nix flake metadata --json .` in `vpsfree-cz-configuration`
      confirmed `vpsfreeNotificationTemplates.locked.rev` is
      `2074fe28446ec43212e4e2f2fa9001d2624bd6d3` and
      `vpsadminServices.locked.rev` is
      `f942e79bd316d022143addb0dc4fdd54b7e3a724`;
    - `git diff --check HEAD~3..HEAD` passed in
      `vpsfree-cz-configuration`;
    - GitHub Actions after pushing `vpsadmin` head `f942e79bd`:
      `RuboCop` and `API Specs (topic parallel)` passed; aggregate `CI` is
      still running at the time of this note;
    - superseded older `vpsadmin` CI run `28396757927` for head
      `9a2b377ed0ae2eaf84aa479efaeb6de87c52c4a1` was cancelled after the
      follow-up push;
    - `gh run list` showed no GitHub Actions runs for the pushed
      `vpsfree-notification-templates` or `vpsfree-cz-configuration`
      branches.
  - mandatory change review:
    - reviewer `Dirac` reviewed the committed cross-repository slice after
      quick verification and before `confctl build`;
    - result: no blocking or important findings;
    - advisory finding: `vpsfree-notification-templates/AGENTS.md` still had
      uploader-era PR/security guidance about upload/authentication testing
      and `API=...` upload targeting;
    - fix: amended the template commit to replace that guidance with
      managed-install/deployment validation and explicit `SOURCE_ID` wording;
    - configuration was rebased so the template input pin remains a single
      confctl-style input update commit.
  - build verification after review:
    - initial `confctl build "cz.vpsfree/vpsadmin/int.api1"` attempt exited at
      the confirmation prompt with `end of file reached`; rerun with explicit
      `y` on stdin;
    - `printf 'y\n' | nix develop -c confctl build
      "cz.vpsfree/vpsadmin/int.api1"` passed and built generation
      `2026-06-30--00-12-16`;
    - the `int.api1` build log showed the expected source/package derivations:
      `vpsadmin-source-f942e79bd316d022143addb0dc4fdd54b7e3a724` and
      `vpsfree-notification-templates-2074fe28446ec43212e4e2f2fa9001d2624bd6d3`;
    - `printf 'y\n' | nix develop -c confctl build
      "cz.vpsfree/vpsadmin/int.api2"` passed and built generation
      `2026-06-30--00-14-34`.
  - dev-cluster verification after review:
    - active cluster `2026-06-15-vpsadmin-events` is running with topology
      `single`, bridge networking, and `ready: yes`;
    - first `devcluster update 2026-06-15-vpsadmin-events services` attempt
      failed while copying the closure because the services VM had no free
      blocks/inodes on `/nix/store`;
    - freed space by vacuuming the journal, removing only stale temporary
      template-upload directories under `/tmp`, and running
      `nix-collect-garbage -d` inside the services VM; `/` recovered to about
      813 MiB free and 153k free inodes before retry;
    - retry of `devcluster update 2026-06-15-vpsadmin-events services`
      completed successfully and restarted API plus notification dispatcher
      services;
    - post-update checks passed: `devcluster status` reported ready,
      `vpsadmin-api`, Telegram, e-mail, and SMS dispatcher services were
      active, and the HTTPS API endpoint returned the HaveAPI description;
    - emitted a real `vps.resources_changed` event in the dev cluster using
      `vpsadmin-api-ruby`; the event routed as `event_id=28`;
    - resulting Telegram delivery `48` was sent successfully with provider
      HTTP status `200` and message id `41`; the Telegram response text had
      the requested block layout:
      title, blank line, current limits, blank line, reason/changed-by,
      blank line, `Link: VPS details`;
    - the response also showed the VPS title and `VPS details` as WebUI
      text links and rendered Markdown reason emphasis as Telegram-supported
      bold text;
    - devcluster service configuration does not consume the production
      `vpsfreeNotificationTemplates` flake input; managed package wiring and
      source-id install-on-change behavior were verified by API specs and the
      production `confctl build` closure, not by devcluster redeploy.
  - final worktree status:
    - `vpsadmin` is clean and tracking
      `origin/2026-06-15-vpsadmin-events`;
    - `vpsfree-notification-templates` is clean;
    - `vpsfree-cz-configuration` is clean except for pre-existing untracked
      `.bin/` and `.bundle/` local development directories.
- 2026-06-29 Telegram HTML template slice in progress:
  - requested outcome: add user-friendly Telegram HTML notification templates
    with WebUI links, keep text fallbacks, and deploy to the running dev
    cluster;
  - implementation approach:
    - `vpsadmin` now has template HTML helpers and will send Telegram
      `html` bodies with `parse_mode: HTML` plus disabled link previews when
      the rendered body fits the Telegram message limit;
    - Telegram payload parsing remains backward-compatible with queued JSON
      that contains only `chat_id` and `text`;
    - `vpsfree-mail-templates` adds `telegram/<lang>.html.erb` beside every
      existing Telegram text template and keeps the text templates required;
    - external HTML templates use only the existing `webui_url` helper and
      `ERB::Util.html_escape`, so installing them before the new sender code
      does not break old vpsAdmin rendering;
    - the new vpsAdmin sender is still required before users receive Telegram
      HTML instead of text.
  - local edits made so far:
    - `vpsadmin`: Telegram HTML payload selection, safe template helpers,
      dispatcher payload preservation, specs, and template docs;
    - `vpsfree-mail-templates`: generated 128 Telegram HTML templates,
      added `bundle exec rake check`, and updated README/AGENTS guidance.
  - verification, commits, mandatory review, configuration pin update, and
    dev-cluster deployment are still pending.
- Latest completed slice on 2026-06-28: the review follow-up was folded into
  the relevant split commits instead of left as a standalone compatibility
  fix. A follow-up CI workflow commit was added after GitHub showed that the
  new migration-spec workflow failed on force-pushed branches when
  `github.event.before` was no longer available in the checkout.
- Current local commit stack above `origin/master` ends with:
  - `ec3a01b62 api: add migration spec harness`
  - `98d9592e5 api: cover notification migrations`
  - `e0da946bc notifications: add routing contexts`
  - `6ab7bc2b3 notifications: migrate legacy recipients to routes`
  - `d15935a7e webui: expose notification route scopes`
  - `ee510dfd9 notification_templates: register sms protocol`
  - `4603b9de6 ci: harden migration spec base detection`
- The split is intentional:
  - generic migration spec harness and hooks/workflow live in their own
    commit;
  - migration specs for existing/new migrations live in their own commit;
  - the routing-context migration is separate from the legacy recipient
    conversion;
  - the legacy recipient conversion commit owns removal of old recipient API
    and WebUI surfaces.
- Mandatory change review result and follow-up:
  - reviewer agreed the generic/spec/feature split was the right review shape;
  - blocking issue fixed: admin member detail still called the removed
    `email_role_recipient` API and the XSS source assertion still referenced
    the removed endpoint;
  - important issue fixed: the legacy recipient migration now maps all known
    event-backed legacy template names and fails fast only for templates that
    cannot be represented as events;
  - important issue fixed: API notification SMTP password handling now uses
    systemd credentials instead of reading the password file directly;
  - important follow-up fixed: direct e-mail deliveries without an
    `event_routing_context` are visible to admins through the nested
    delivery-attempt API while ordinary users remain restricted;
  - reviewer concern about routing-context state mapping was checked against
    `delivery_context_state` and the migration spec; the existing mapping is
    intentional and covered by the migration test.
- The former standalone commit
  `eba77c192 notifications: preserve direct event e-mail delivery` was
  squashed into `e0da946bc notifications: add routing contexts`, together with
  the nested direct-delivery attempt regression spec and the verified custom
  e-mail fixture for the OOM supervisor spec.
- Migration compatibility notes:
  - `users.mailer_enabled` is preserved through generated delivery method
    settings/default routes in migration specs;
  - legacy role/template recipient overrides are converted into explicit
    event routes and reusable notification targets where a unique admin user
    can be resolved;
  - rollback recreates the removed legacy recipient tables but intentionally
    does not reconstruct recipient rows, so operators must rely on backup if a
    data-preserving rollback of those removed tables is required.
- Local verification before the history rewrite:
  - selected migration specs:
    `nix develop ..#api -c xargs -a tmp/migration-specs.txt bundle exec
    rspec --options /dev/null --format documentation`: 21 examples,
    0 failures;
  - broader notification/API specs:
    `nix develop ..#api -c bundle exec rspec --format progress
    spec/api/resources/event_routing_spec.rb
    spec/models/event_route_spec.rb
    spec/models/transaction_chains/mail/daily_report_spec.rb
    spec/models/transaction_chains/plugins/payments/mail_overview_spec.rb
    spec/models/transaction_chains/plugins/outage_reports/update_spec.rb
    spec/api/resources/lifecycle_bypass_spec.rb
    spec/api/resources/notification_template_spec.rb`: 148 examples,
    0 failures, 1 expected pending;
  - WebUI regression slice:
    `nix develop .#webui -c composer test -- --filter
    'XssReportSinksTest|NotificationRouteUiTest'`: 5 tests,
    53 assertions, 0 failures;
  - Nix parse checks passed for
    `nixos/modules/vpsadmin/api/default.nix`,
    `tests/suite/alerts/common.nix`, and `tests/suite/webui.nix`.
- GitHub Actions on the previously pushed split heads:
  - head `05ce69e5c`: `API Migration Specs`, `RuboCop`,
    `Webui PHPUnit`, and `libnodectld Specs` passed; `API Specs (topic
    parallel)` failed on direct e-mail events and the OOM custom-target
    fixture;
  - head `eba77c192`: `RuboCop` and `API Specs (topic parallel)` passed;
    the aggregate `CI` run became superseded by the history rewrite.
- Local verification after rebasing/squashing onto `origin/master`:
  - targeted API/spec slice covering direct deliveries, nested direct
    delivery attempts, OOM fallback routing, and direct request/incident
    event mail: 10 examples, 0 failures;
  - `nix develop ..#api -c bundle exec rspec --format documentation
    spec/migrations/20260624120000_add_event_routing_contexts_spec.rb`:
    2 examples, 0 failures;
  - `nix develop ..#api -c bundle exec rubocop
    lib/vpsadmin/api/events.rb lib/vpsadmin/api/resources/event.rb
    spec/api/resources/event_routing_spec.rb
    spec/supervisor/node/oom_reports_spec.rb`: no offenses;
  - `git diff --check`: passed;
  - `tools/check_migration_specs.rb --base
    origin/2026-06-15-vpsadmin-events --head HEAD`: passed.
- The rewritten `vpsadmin` branch was force-pushed from `eba77c192` to
  `ee510dfd9`, then fast-forwarded to `4603b9de6` with the workflow fix.
- GitHub Actions after the rewrite:
  - `API Migration Specs` initially failed on `ee510dfd9` before running
    specs because `git diff eba77c192...HEAD` could not resolve the
    force-pushed-away base commit in the checkout;
  - workflow fix `4603b9de6` validates the event base ref and falls back to
    the default-branch merge-base when needed;
  - `API Migration Specs` passed on `4603b9de6`;
  - superseded `ee510dfd9` `CI` and `API Specs (topic parallel)` runs were
    cancelled after the follow-up push;
  - `RuboCop`, `Webui PHPUnit`, and `libnodectld Specs` passed on
    `ee510dfd9`; `API Specs (topic parallel)` passed on `eba77c192`, and the
    later local targeted direct-delivery slice passed after the review fix.
- Mandatory change review after the final workflow fix:
  - reviewer `Rawls` reviewed head `4603b9de6` against `origin/master`;
  - result: no blocking, important, or advisory findings;
  - reviewer confirmed the requested commit split is intact and that the
    direct e-mail delivery fix is folded into `e0da946bc`;
  - reviewer-ran checks passed:
    `ruby tests/ci-selection-test.rb`, `git diff --check
    origin/master..HEAD`, `tools/check_migration_specs.rb --base
    origin/master --head HEAD`, and commit-message line length scan;
  - residual risks: full API topic specs were not rerun by CI on final
    workflow-only head `4603b9de6`; long integration/dev-cluster coverage was
    not rerun after the final history cleanup; legacy recipient rollback
    remains schema-only as recorded.

- Latest completed slice: the 2026-06-22 Telegram token deployment fix below.
- Current requested slice: finish notification target verification/UI polish.
  - Fix reusable target list status so plain `NotificationTarget` rows use
    `enabled`, not receiver-link-only `target_enabled`.
  - Remove mixed right-aligned text cells from notification forms.
  - Make the SMS phone number input width match the label input.
  - Require verification for custom e-mail targets, with one custom e-mail
    address per target.
  - Keep default-recipient e-mail targets trusted.
  - Auto-verify custom e-mail and SMS targets when admins create or update
    them.
- Current requested slice: replace the SMS-only user flag with a scalable
  per-user event delivery method settings table.
  - Admins control whether each user may use event delivery methods:
    `email`, `webhook`, `telegram`, and `sms`.
  - Users must not be able to enable or disable delivery methods themselves.
  - Missing per-user method rows default to enabled for all current methods,
    including SMS.
  - Existing receiver actions for disabled methods remain visible/deletable,
    but users cannot create or update actions to a disabled method and
    deliveries are skipped/canceled.
  - Admin create/update of a receiver action for a disabled method should
    auto-enable the method for the target user.
  - `users.mailer_enabled` remains as a legacy default e-mail routing switch
    and should not be extended into the new delivery-method matrix.
- Current requested slice: refine and implement SMS delivery testing and
  callback authentication.
  - Gateway callbacks should use per-message HMAC signatures, not a shared
    bearer callback token.
  - vpsAdmin should generate a per-message `callback_secret`, store it in the
    delivery payload, send it to the gateway, and verify gateway callbacks
    using a 20 minute timestamp window.
  - `vpsfree-sms-gateway` may recreate current development SQLite databases;
    add versioned schema/bootstrap support now, but do not add an ALTER
    migration for unversioned dev DBs.
  - Gateway inbound SMS persistence should be configurable and disabled by
    default. The gateway must still drain inbound modem messages when disabled.
  - Dev-cluster outbound SMS testing should run by default with the gateway
    fake driver. Inbound persistence in dev cluster remains a separate
    opt-in flag, default false.
  - No dev-only inbound injection HTTP API is needed; keep inbound injection in
    Go unit tests.

## 2026-06-22 Telegram token deployment fix

- User reported that `devcluster update 2026-06-15-vpsadmin-events services`
  failed after adding a Telegram bot token:
  `vpsadmin-notification-dispatcher-email.service` and
  `vpsadmin-notification-dispatcher-webhook.service` failed to start, while
  the new Telegram dispatcher and receiver were started.
- Root causes found on the services VM:
  - the dev cluster copies the Telegram token into
    `/var/lib/vpsadmin/devcluster-telegram/bot-token` as `root:root` `0600`;
  - dispatcher and receiver `preStart` scripts read `botTokenFile` directly
    while running as their service users, so all Telegram-enabled services
    failed with `Permission denied`;
  - after fixing token access, polling startup failed because
    `TelegramReceiver#prepare_polling!` passed `drop_pending_updates:` as a
    Ruby keyword to `TelegramBot#post_json`, which expects an explicit payload
    argument.
- Fixed in `vpsadmin`:
  - `nixos/modules/vpsadmin/notification-dispatcher.nix` and
    `nixos/modules/vpsadmin/telegram-receiver.nix` now load Telegram token and
    webhook secret files through systemd `LoadCredential` and read from
    `CREDENTIALS_DIRECTORY`;
  - `api/lib/vpsadmin/api/telegram_receiver.rb` now calls
    `post_json('deleteWebhook', { drop_pending_updates: false })`;
  - `api/spec/models/tasks/telegram_spec.rb` covers deleting webhooks before
    polling starts.
- Verification for the fix:
  - `nix develop .#api -c bundle exec rspec
    spec/models/tasks/telegram_spec.rb`: 9 examples, 0 failures;
  - `nix-instantiate --parse` passed for the two changed vpsAdmin Nix modules;
  - `git diff --check` passed;
  - Overcommit hooks passed on commit: `Nixfmt` and `RuboCop`.
- Dev-cluster deployment:
  - first retry got past the token permission issue and exposed the Ruby
    `post_json` arity bug;
  - second retry initially hit a full services VM `/nix/store`; ran
    `nix-collect-garbage -d` in the services VM and retried;
  - final `devcluster update 2026-06-15-vpsadmin-events services` succeeded;
  - `systemctl --failed --no-pager` on the services VM reported no failed
    units;
  - active services include `vpsadmin-api.service`,
    `vpsadmin-notification-dispatcher-email.service`,
    `vpsadmin-notification-dispatcher-webhook.service`,
    `vpsadmin-notification-dispatcher-telegram.service`, and
    `vpsadmin-telegram-receiver.service`;
  - HTTPS smoke checks for
    `https://api.aitherdev.int.vpsfree.cz/` and
    `https://webui.aitherdev.int.vpsfree.cz/` returned HTTP 200.
- Commits and pushes:
  - `vpsadmin` commit
    `e900fc205020160314bf4828921cdc41584bde60`
    (`notifications: load Telegram secrets as credentials`) pushed to
    `origin/2026-06-15-vpsadmin-events`;
  - `vpsfree-cz-configuration` generated pin commit
    `89ad323979f9b0dd03a919c5c7be3e565996fa09`
    set `vpsadminProduction`, `vpsadminServices`, and `vpsadminStaging` to
    vpsAdmin `e900fc20` and was pushed to
    `origin/2026-06-15-vpsadmin-events`.
- Production configuration verification after the refreshed pin:
  - `nix develop -c confctl build -y cz.vpsfree/vpsadmin/int.api1` passed and
    built vpsAdmin API, Telegram receiver, and notification dispatcher
    derivations at `e900fc20`;
  - `nix develop -c confctl build -y cz.vpsfree/vpsadmin/int.vpsadmin1`
    passed for the frontend/services host;
  - the first build attempt without `-y` exited at the confirmation prompt and
    did not build anything.
- Push note: pushing `vpsfree-cz-configuration` showed GitHub's existing
  Dependabot vulnerability banner for the default branch; it was unrelated to
  this feature branch push.
- GitHub Actions after the `e900fc20` vpsAdmin push:
  - `RuboCop`: success;
  - `API Specs (topic parallel)`: success;
  - aggregate `CI` workflow `27965036747` was still in progress in the
    `Run tests` step after about 40 minutes of local watching; no failed step
    was available to inspect at that time;
  - `vpsfree-cz-configuration` listed no branch workflow runs after the
    `89ad3239` push.

- Declarative event/action refactor slice implemented on 2026-06-19:
  - `VpsAdmin::API::Events` now has a declarative typed event DSL with
    per-event arguments, derived event attributes, parameter definitions,
    plugin-local helpers, and per-action delivery data blocks;
  - `user.new_login` was converted to the typed DSL and now calls
    `route_event!` with the `UserSession` and `Oauth2Authorization` objects
    instead of enumerating all event fields at the call site;
  - the monitoring plugin now registers `monitoring.alert` from
    `plugins/monitoring/api/events/alert.rb`, keeping plugin event
    declarations out of vpsAdmin core;
  - notification delivery actions are now registered through
    `VpsAdmin::API::Notifications::Actions`;
  - notification receiver actions, deliveries, and delivery attempts now store
    action registry names (`email`, `webhook`) instead of integer enums, so
    future protocols can be added through registry definitions;
  - the one events-session migration and core schema were adjusted to use
    string action columns for the new notification tables.
- Declarative refactor verification on 2026-06-19:
  - syntax checks passed for touched Ruby files;
  - `nix develop .#api --command bash -lc 'bundle exec rubocop ...'` passed
    for the touched API and monitoring Ruby files;
  - focused notification/action/monitoring specs passed:
    54 examples, 0 failures;
  - core-only plugin leak check passed:
    `VPSADMIN_PLUGINS=none bundle exec rspec
    spec/api/resources/event_routing_spec.rb:706`;
  - post-RuboCop focused rerun passed: 18 examples, 0 failures;
  - post-review monitoring regression run passed: 9 examples, 0 failures;
  - post-review focused notification/action rerun passed:
    19 examples, 0 failures;
  - `git diff --check` passed.
- Mandatory review for Telegram object-link follow-up:
  - reviewer reported one blocker: the first default Telegram HTML body called
    `telegram_notification_html` directly, so once an upgraded process
    backfilled DB rows, an old mixed-version API/dispatcher process could try
    to render the HTML and fail before falling back to text;
  - fixed by storing default Telegram HTML as
    `<%= telegram_notification_html if respond_to?(:telegram_notification_html) %>`,
    which new code renders richly and old builders render as blank HTML so
    delivery falls back to the existing text template;
  - added regression coverage that the guarded default renders blank under an
    old minimal builder, that newly installed Telegram variants receive the
    guarded default, and that missing WebUI base URL degrades VPS titles to
    escaped plain text without a footer link;
  - post-fix validation passed:
    `nix develop .#api -c bundle exec rspec
    spec/models/notification_templates_spec.rb` (15 examples);
  - post-fix validation passed:
    `nix develop .#api -c bundle exec rspec
    spec/models/notification_templates_spec.rb
    spec/models/tasks/event_delivery_spec.rb:1217
    spec/models/tasks/event_delivery_spec.rb:1246
    spec/models/tasks/event_delivery_spec.rb:1270
    spec/models/tasks/event_delivery_spec.rb:1301
    spec/models/tasks/event_delivery_spec.rb:1329
    spec/models/tasks/event_delivery_spec.rb:1353` (21 examples);
  - `nix develop .#api -c bundle exec rubocop
    models/notification_template_variant.rb models/notification_template.rb
    lib/vpsadmin/api/events.rb lib/vpsadmin/api/notification_templates.rb
    lib/vpsadmin/api/notifications.rb spec/models/notification_templates_spec.rb
    spec/models/tasks/event_delivery_spec.rb` passed with no offenses;
  - `git diff --check` passed.
- Telegram object-link finalization:
  - after the first dev-cluster deploy, live DB setup updated 7 remaining
    legacy Telegram HTML variants and the DB reported
    `{telegram: 98, legacy_html: 0, default_html: 54}`;
  - deployed resource-change render showed the intended VPS details and links
    but revealed `Reason:` was duplicated, because unrelated detail builders
    also emitted plain `@reason`;
  - vpsAdmin final head is `9a2b377ed0ae2eaf84aa479efaeb6de87c52c4a1`
    (`notifications: replace legacy Telegram link-label HTML`), amended to
    centralize the generic `@reason` line and assert resource-change renders
    exactly one `Reason:`;
  - local verification passed:
    `nix develop .#api -c bundle exec rspec
    spec/models/notification_templates_spec.rb` (20 examples, 0 failures);
  - local verification passed:
    `nix develop .#api -c bundle exec rubocop
    models/notification_template_variant.rb
    spec/models/notification_templates_spec.rb` (no offenses);
  - `git diff --check` passed in vpsAdmin;
  - vpsAdmin branch was force-pushed to origin at `9a2b377ed`;
  - mandatory change review by Darwin initially found no vpsAdmin/template
    blockers, but found a stale squashed generated pin message and a leftover
    internal DNS `vpsadmin1.int` record in production configuration;
  - rewrote `vpsfree-cz-configuration` locally so mailer removal is
    `38814606ba4ec776e285f0c3c60c8638dde855b8`
    (`vpsadmin-config: remove mailer host`) and now also removes
    `configs/internal-dns/zone.vpsfree.cz.` `vpsadmin1.int`;
  - regenerated the final pin through
    `confctl inputs channel set --commit vpsadmin vpsadmin 9a2b377ed`;
    config head is now `70a95dffc40cab2ac4988cd0833e1bacdb1ebf78`
    (`inputs: set vpsadminServices to 9a2b377e`) and its generated body says
    `vpsadminServices: d8b138c3 -> 9a2b377e`;
  - `rg -n "vpsadmin1|int\.vpsadmin1|common/mailer" cluster
    data/vpsadmin configs/internal-dns -g '*.nix' -g 'zone.*'` returned no
    matches;
  - `git diff --check HEAD~2..HEAD` passed in
    `vpsfree-cz-configuration`;
  - Darwin's focused re-check found no Blocking, Important, or Advisory
    findings; residual work is final config build, push, and dev-cluster
    redeploy/verification.
- Final build/deploy verification:
  - pushed `vpsfree-cz-configuration` branch
    `2026-06-15-vpsadmin-events` to origin at `70a95dff`;
  - production config builds passed:
    `cz.vpsfree/vpsadmin/int.api1` generation
    `2026-06-29--21-40-09`, `int.api2`
    `2026-06-29--21-41-56`, `int.db`
    `2026-06-29--21-42-51`, `int.rabbitmq1`
    `2026-06-29--21-43-39`, `int.rabbitmq2`
    `2026-06-29--21-44-37`, `int.rabbitmq3`
    `2026-06-29--21-45-33`, `int.redis1`
    `2026-06-29--21-46-28`, `int.webui1`
    `2026-06-29--21-47-24`, `int.webui2`
    `2026-06-29--21-48-30`, `int.webui-dev`
    `2026-06-29--21-49-24`, `containers/brq/int.ns1`
    `2026-06-29--21-50-22`, `containers/prg/int.ns1`
    `2026-06-29--21-51-25`, `containers/prg/int.mon1`
    `2026-06-29--21-52-25`, and `containers/prg/int.mon2`
    `2026-06-29--21-53-41`;
  - final dev-cluster services update completed for
    `2026-06-15-vpsadmin-events` with vpsAdmin source
    `9a2b377ed`; unlike the previous deploy, console router stopped cleanly
    without manual kill;
  - dev cluster reports `status: running`, `ready: yes`, bridge network,
    with no failed systemd units;
  - running vpsAdmin services include API, console router, notification
    dispatchers for email/sms/telegram/webhook, scheduler, supervisor,
    Telegram receiver, and webhook test server;
  - `vpsadmin-database-setup.service` exited successfully after installing
    built-in notification templates; no variants needed updating because the
    previous deploy already converted the remaining legacy rows;
  - node1 reports `osctld` and `nodectld` running, `nodectl ping` returns
    `pong`, `nodectl status` is `State: running`, and all queues are empty;
  - live DB check using deployed API store
    `/nix/store/7iqj72nkm379ha3rdzzly6zx6dfj079x-vpsadmin-api-dev` reports
    `{telegram: 98, legacy_html: 0, default_html: 54}`;
  - deployed resource-change Telegram render is:
    `<b>VPS resources changed: <a ...>spec-vps (#123)</a></b>`,
    `Changed by: admin &lt;user&gt;`, `<b>Current limits:</b>`,
    `CPU: 3`, `CPU limit: unlimited`, `Memory: 4 GB`, `Swap: 256 MB`,
    `Reason: scale up &amp; test`, and
    `Link: <a ...>VPS details</a>`;
  - deployed render check reports `REASON_COUNT=1` and `LEGACY_LINK=false`;
  - GitHub Actions for vpsAdmin head `9a2b377ed`: `RuboCop` and
    `API Specs (topic parallel)` are green, aggregate `CI`
    run `28396757927` is queued;
  - superseded aggregate CI runs `28395531566`, `28394402823`,
    `28393524516`, and `28391729265` were requested for cancellation;
  - GitHub reports no workflow runs for the
    `vpsfree-cz-configuration` branch.
- Telegram legacy-link follow-up after live DB verification:
  - deployed DB after the first template upgrade still had 22 Telegram HTML
    variants containing the old `open in vpsAdmin` link label; the
    `vps_resources_change` row itself had already been replaced with the
    shared renderer;
  - added vpsAdmin commit `79ba0e28b`:
    `notifications: replace legacy Telegram link-label HTML`;
  - the installer now also replaces old packaged Telegram HTML containing
    `open in vpsAdmin` when the packaged default HTML is the shared renderer
    and the stored Telegram text still matches the packaged text; this is
    intended to update old built-in rows without overwriting customized text;
  - quick verification passed:
    `nix develop .#api -c bundle exec rspec
    spec/models/notification_templates_spec.rb` (18 examples, 0 failures);
  - quick verification passed:
    `nix develop .#api -c bundle exec rubocop
    lib/vpsadmin/api/notification_templates.rb
    spec/models/notification_templates_spec.rb` (no offenses);
  - `git diff --check` passed;
  - vpsAdmin commit hooks passed from the root Nix shell (`Nixfmt`,
    `MigrationSpecs`, `RuboCop`, and commit-msg hooks);
  - branch `origin/2026-06-15-vpsadmin-events` is pushed at
    `79ba0e28b5052b1da3960c5af99833bb1530f1a0`;
  - updated `vpsfree-cz-configuration` with generated commit `af884e4d`
    `inputs: set vpsadminServices to 79ba0e28`, produced by
    `confctl inputs channel set --commit vpsadmin vpsadmin 79ba0e28b`;
  - config branch `origin/2026-06-15-vpsadmin-events` is pushed at
    `af884e4dd1ffe36e02ccb782cc9629f86291c78d`;
  - config `git diff --check HEAD~1..HEAD` passed; `.bin/` and `.bundle/`
    remain untracked local helper directories in the config worktree;
  - mandatory follow-up review launched with standalone reviewer Volta
    (`019f149f-c3a4-7a80-9dbf-5f3f479d21a3`) before rebuilding and
    redeploying the dev cluster.
  - Volta reported one Blocking issue: the initial link-label predicate would
    have replaced customized Telegram HTML when the text fallback still matched
    the packaged text and the custom HTML contained `open in vpsAdmin`;
  - fixed by replacing the broad phrase match with SHA-256 fingerprints of the
    normalized legacy packaged HTML bodies observed in the dev DB;
  - added a regression that keeps customized HTML containing the old phrase
    when it does not match a known packaged fingerprint;
  - amended vpsAdmin follow-up commit and force-pushed branch at
    `7a4c718ab190c06c86080fec82fc7833ad5d4489`;
  - post-fix verification passed:
    `nix develop .#api -c bundle exec rspec
    spec/models/notification_templates_spec.rb` (19 examples, 0 failures);
  - post-fix verification passed:
    `nix develop .#api -c bundle exec rubocop
    lib/vpsadmin/api/notification_templates.rb
    spec/models/notification_templates_spec.rb` (no offenses);
  - post-fix `git diff --check` passed and amend commit hooks passed
    (`Nixfmt`, `MigrationSpecs`, `RuboCop`, and commit-msg hooks);
  - regenerated the configuration pin to `7a4c718a`, then squashed the
    superseded intermediate pin commits into one final generated pin commit
    after `fcc543a7`; config branch is force-pushed at
    `a0131547d446e3ebe5b8e72988f8d2179d576f13`;
  - config `git diff --check HEAD~1..HEAD` passed; the generated commit
    message still has the expected text-width warning from confctl.
  - Volta re-check after the fix reported no Blocking or Important findings;
    advisory was only to correct the copied full SHAs in this state file.
  - Live dev DB verification after deploying `7a4c718a` showed the
    VPS-specific legacy rows had been replaced but 7 concrete request-template
    rows still contained `open in vpsAdmin`; these rows were not reached by
    the directory-backed template loop;
  - amended the vpsAdmin follow-up again to run a global exact-fingerprint
    sweep for legacy Telegram HTML variants inside `install_defaults!`;
  - added a regression for legacy Telegram HTML outside configured directory
    templates;
  - post-sweep verification passed:
    `nix develop .#api -c bundle exec rspec
    spec/models/notification_templates_spec.rb` (20 examples, 0 failures);
  - post-sweep verification passed:
    `nix develop .#api -c bundle exec rubocop
    lib/vpsadmin/api/notification_templates.rb
    spec/models/notification_templates_spec.rb` (no offenses);
  - post-sweep `git diff --check` passed and amend commit hooks passed
    (`Nixfmt`, `MigrationSpecs`, `RuboCop`, and commit-msg hooks);
  - vpsAdmin branch is force-pushed at
    `9909b17003e1e34a95dfd18af3a12354fdf56b6a`;
  - regenerated and squashed the configuration pin again; config branch is
    force-pushed at `0f17396253b35d701372fe7d960b61a58dc918f6`, pinning
    `vpsadminServices` to `9909b170`.
  - mandatory review initially found that the default Telegram HTML template
    was not mixed-version safe for old template builders; fixed by guarding
    the helper call with `respond_to?`, added regression coverage, and the
    reviewer re-check reported no findings;
  - committed and pushed vpsAdmin
    `1978906790900a83e72d34fc5488efee27c0485f`
    (`notifications: enrich Telegram template HTML`);
  - pinned `vpsfree-cz-configuration` to that revision with generated commit
    `9de62f24`, built `cz.vpsfree/vpsadmin/int.api1` and `int.api2`
    successfully, then deployed services in the running dev cluster;
  - deployed verification showed the services VM healthy, nodectld healthy,
    but the DB still contained 54 legacy explicit Telegram HTML rows from the
    first HTML implementation, including `vps_resources_change` with the old
    `open in vpsAdmin` link label;
  - GitHub Actions RuboCop on pushed vpsAdmin head `462158980` reported
    `Style/RedundantStructKeywordInit` in the notification template spec;
    removed redundant `keyword_init: true`, verified the exact CI RuboCop
    command locally, and autosquashed the fix into the first Telegram HTML
    commit;
  - force-pushed the cleaned vpsAdmin branch with final commits
    `d4a12668cb1f5f3d085fb68f486733ddb1ac7026`
    (`notifications: enrich Telegram template HTML`) and
    `e699f7ec26fc04dcb44c87c551f050d0ec25901d`
    (`notifications: replace legacy Telegram HTML templates`);
  - follow-up validation passed:
    `nix develop .#api -c ruby -c
    lib/vpsadmin/api/notification_templates.rb`, `git diff --check`,
    `nix develop .#api -c bundle exec rspec
    spec/models/notification_templates_spec.rb` (17 examples),
    `nix develop .#api -c bundle exec rspec
    spec/models/tasks/event_delivery_spec.rb:1217
    spec/models/tasks/event_delivery_spec.rb:1246
    spec/models/tasks/event_delivery_spec.rb:1270
    spec/models/tasks/event_delivery_spec.rb:1301
    spec/models/tasks/event_delivery_spec.rb:1329
    spec/models/tasks/event_delivery_spec.rb:1353` (6 examples), and the
    focused RuboCop command above (7 files, no offenses), and later
    `nix develop .#api -c bundle exec rubocop --parallel --force-exclusion`
    (1398 files, no offenses);
  - after mandatory review advisories, updated operator-facing install text in
    `database-setup.nix` and `vpsadmin.rake`, and rewrapped the second
    vpsAdmin commit message so the local commit-msg hook passed without
    warnings;
  - updated `vpsfree-cz-configuration` to final vpsAdmin revision
    `e699f7ec2` and squashed repeated generated pin commits into one final
    generated commit `be66df40f6ad4ea49d150f74f16c1e51f46808a9`
    (`inputs: set vpsadminServices to e699f7ec`); local status contains only
    untracked `.bin/` and `.bundle/`;
  - second mandatory review by Leibniz reported no blocking or important
    findings; previous advisories are resolved. Residual risk is final config
    build, dev-cluster redeploy, and live DB render verification pending.
  - same reviewer re-checked amended head `197890679` and reported no
    blocking, important, or advisory findings; residual gap is that only the
    focused template/rendering and Telegram delivery paths were re-run locally,
    not the full API or dev-cluster integration suite.
- Declarative refactor commit on 2026-06-19:
  - commit `d891d892e14ae7b2b2abaf5478290ae10a8955ea`, later amended to
    `ee4598e214e4a28a39bdae96d5de03fdc6f87767`
    (`notifications: declare events and actions`);
  - Overcommit hooks were active and passed during commit (`Nixfmt`,
    `RuboCop`);
  - the ambient shell commit attempt failed because the Overcommit gem is not
    available there, so the final commit was made from the repository-root
    `nix develop` shell where the hook dependencies are installed;
  - commit-msg text-width hook warned at its 72-column threshold but passed;
    the message is within the workspace 80-column rule.
- Mandatory change review requested from standalone agent `Chandrasekhar`
  (`019ee184-5044-7c50-a549-43a064b7bb59`) against
  `542d30dcc..d891d892e`.
- Mandatory change review result:
  - blocking findings: none;
  - important: custom monitoring `email_vars:` were swallowed by the legacy
    `Events.emit!` keyword before they could reach the typed event definition;
  - important: the typed monitoring declaration narrowed accepted
    `template_name`/`severity` values compared with the old helper path.
- Mandatory review follow-up:
  - monitoring typed arguments now use `template_vars` and `template_options`
    internally, avoiding `emit!`'s legacy `email_vars`/`email_options`
    keywords while preserving the public `route_monitoring_alert!` interface;
  - scalar typed event arguments can declare explicit unions, used by
    monitoring to accept both string and symbol template/severity values;
  - monitoring alert specs cover custom mail vars, string template names, and
    symbol severities reaching the rendered e-mail delivery.
- Monitoring alert helper redesign on 2026-06-19:
  - user feedback on config commit `aa2804e6` was addressed by removing
    delivery-specific public arguments from `route_monitoring_alert!`;
  - new helper signature accepts event-domain arguments only:
    `recipient`, `role`, `alert_kind`, `variant`, `context`, `severity`,
    `subject`, `summary`, and `parameters`;
  - monitoring alert e-mail template selection, params, options, and vars now
    live in `plugins/monitoring/api/events/alert.rb` next to the
    `monitoring.alert` declaration;
  - production monitoring config now passes only variants and contextual
    monitoring facts such as disk pool role, selected VPS, restart window, and
    admin language;
  - old helper keywords `user`, `template_name`, `template_params`,
    `email_vars`, and `email_options` are intentionally not accepted by the
    new helper.
- Monitoring helper redesign heads on 2026-06-19:
  - `vpsadmin` amended head:
    `5b27330842595e0623fede94ea02e26e05cd9579`
    (`notifications: declare events and actions`);
  - `vpsfree-cz-configuration` functional head:
    `85434c37abc859998b5de5ea0e78a2618e0a12fb`
    (`vpsadmin-config: route monitoring alerts`);
  - the obsolete config pin commit to vpsAdmin `542d30dc` was dropped locally;
    a fresh `confctl inputs channel set --commit` pin will be generated after
    the amended vpsAdmin head is pushed to GitHub.
- Monitoring helper redesign verification on 2026-06-19:
  - Ruby syntax checks passed for touched vpsAdmin monitoring files and the
    production monitoring config;
  - `nix develop .#api --command bash -lc 'bundle exec rubocop ...'` passed
    for touched vpsAdmin API/monitoring Ruby files;
  - `nix develop --command bash -lc 'bundle exec rubocop
    configs/vpsadmin/api/monitoring.rb'` passed;
  - `nix develop .#api --command bash -lc 'bundle exec rspec
    spec/models/transaction_chains/plugins/monitoring/alert_spec.rb'` passed:
    10 examples, 0 failures;
  - focused notification/action/event routing rerun passed:
    20 examples, 0 failures;
  - core-only plugin leak guard passed:
    `VPSADMIN_PLUGINS=none bundle exec rspec
    spec/api/resources/event_routing_spec.rb:706`, 1 example, 0 failures.
- Mandatory change review for the monitoring helper redesign:
  - requested from standalone reviewer `Ptolemy`
    (`019ee1c6-576a-72f1-812a-5925ba96b646`);
  - review packet covered `vpsadmin`
    `542d30dccdc9440d46be72d23541ac64e40b2e13..5b27330842595e0623fede94ea02e26e05cd9579`
    and `vpsfree-cz-configuration`
    `e05006142374563123beb10db8b44bb214e44e0b..85434c37abc859998b5de5ea0e78a2618e0a12fb`;
  - result: no blocking or important findings;
  - advisory finding: initial `state.md` entry contained wrong full SHAs while
    the short prefixes were correct; the hashes above were corrected after
    verifying them with `git rev-parse HEAD`;
  - residual risk: no long integration/dev-cluster test was run for this
    slice.
- Delivery detail and test-server slice implemented on 2026-06-18:
  - webhook deliveries and attempts now store response headers;
  - e-mail deliveries now record SMTP status/body where the Mail SMTP adapter
    returns a response;
  - event delivery `show` exposes action-specific details: e-mail recipients,
    subject and bodies, webhook payload, response status, response headers, and
    response body;
  - e-mail Bcc recipients are intentionally not exposed through the user-facing
    delivery detail resource, because the existing `mail_log` resource that can
    show Bcc is admin-only;
  - WebUI event delivery rows link to a dedicated delivery detail page, with
    e-mail body/source/HTML preview and webhook request/response sections;
  - receiver and receiver-action rows link to the event log filtered by
    receiver/action;
  - `tools/webhook-test-server.rb` provides a small VM-local HTTP endpoint for
    manual webhook testing;
  - test/dev WebUI OAuth client now uses `renewable_auto` tokens with a
    20-minute access token lifetime, relying on existing transaction-chain
    polling to renew active sessions.
- Delivery detail verification on 2026-06-18:
  - `nix develop .#api --command bash -lc 'bundle exec rspec
    spec/models/tasks/event_delivery_spec.rb
    spec/api/resources/event_routing_spec.rb'`: 39 examples, 0 failures;
  - `nix develop .#api --command bash -lc 'bundle exec rubocop ...'`:
    no offenses for the touched API Ruby files;
  - `./test-runner.sh test alerts/notification-routing`: successful in
    391.52 seconds;
  - `./test-runner.sh test 'webui#support-pages'`: successful in
    1091.62 seconds;
  - `ruby tests/ci-selection-test.rb`: 15 runs, 54 assertions, 0 failures;
  - `php -l webui/forms/notifications.forms.php` and
    `php -l webui/pages/page_notifications.php`: no syntax errors;
  - `ruby -c tools/webhook-test-server.rb`: syntax OK;
  - `nix-instantiate --parse api/db/seeds/test.nix`,
    `nix-instantiate --parse tests/all-tests.nix`, and
    `nix-instantiate --parse tests/suite/alerts/notification-routing.nix`:
    parse OK;
  - `git diff --check`: passed.
- OOM routing replacement slice committed on 2026-06-16:
  - commit `56f2876b67c9792563de8e9f90870e6a57fb6e14`
    (`notifications: route OOM report suppression`);
  - added glob route matcher sigils `=*` and `!*` for legacy cgroup-style
    matching;
  - added transient event planning through `VpsAdmin::API::Events.plan`;
  - supervisor OOM ingestion now evaluates OOM-specific event routes before
    falling back to legacy `OomReportRule`;
  - the events migration backfills old OOM report rules into event routes,
    preserving ignored reports as muted receivers and notify rules as default
    receiver routes;
  - legacy OOM report rule API create/update/delete now return a deprecation
    error after authorization/lifecycle checks instead of mutating stale
    rules;
  - old OOM rule WebUI actions and sidebar links now send users to
    notification routes;
  - dev cluster remains stopped, per user request.
- OOM routing verification:
  - syntax checks passed for the changed migration, router, supervisor,
    matcher, and specs;
  - focused specs passed before review: 36 examples, 0 failures;
  - broader notification/OOM quick suite passed before review: 81 examples,
    0 failures;
  - final post-review focused specs passed: 61 examples, 0 failures;
  - final post-review broader notification/OOM quick suite passed: 132 examples,
    0 failures;
  - RuboCop passed for the changed Ruby files;
  - PHP syntax passed for the changed OOM/WebUI sidebar files;
  - `git diff --check` passed;
  - direct migration smoke passed by schema-loading a test DB, dropping only
    notification/event tables, inserting a legacy OOM ignore rule, running
    `AddEvents#up`, and verifying the generated OOM route, glob matcher, and
    muted receiver.
- OOM routing mandatory review:
  - Blocking: OOM reports could be marked ignored for non-mute route failures
    such as disabled receivers or unverified actions.
  - Blocking: legacy OOM report rule API/WebUI writes remained available but
    became stale for users migrated to event routes.
  - Important: disabled mailer users may now consistently suppress direct
    incident/OOM/OOM-prevention e-mails that old call sites did not always
    guard with `mailer_enabled`.
- OOM routing review follow-up:
  - raw OOM reports are marked ignored only when the final route plan is
    suppressed and at least one matched delivery used an enabled muted
    receiver;
  - disabled muted receivers do not mark raw OOM reports ignored;
  - muted routes with `continue = true` do not mark reports ignored when a
    later route still delivers the event;
  - non-mute skipped OOM routes do not mark reports ignored;
  - legacy OOM report rule create/update/delete are deprecated/read-only, and
    old WebUI rule actions redirect to notification routes;
  - the mailer-disabled compatibility change is intentional: the new routing
    layer preserves the old user setting as a muted default receiver and
    therefore applies it consistently to newly routed event e-mails.
- Follow-up mandatory review requested from standalone agent `Beauvoir`
  (`019ed281-f539-7202-9fa4-f2c72ecf49bf`) using
  `skills/mandatory-change-review/SKILL.md` against
  `f3e1ff0..2f4f2bbf`.
- Follow-up mandatory review result:
  - Blocking: disabled receivers that were also muted still made raw OOM
    reports ignored.
  - Advisory: the state/review packet recorded an incorrect amended head hash.
- Follow-up mandatory review fix:
  - `RouteResult#suppressed_by_mute?` now requires the muted receiver to be
    enabled;
  - supervisor regression coverage now checks disabled muted receivers.
- Full historical `rake db:migrate` from an empty DB is currently blocked by
  old repository migrations that inherit bare `ActiveRecord::Migration` under
  ActiveRecord 8.1. The new migration was therefore verified directly against
  the schema-loaded test DB.
- Follow-up implementation committed on 2026-06-16:
  - added `TransactionChains::EventDelivery::Email` to render event e-mail
    deliveries through `MailTemplate` or custom `MailLog` and queue the
    existing mail transaction. This was superseded on 2026-06-17 by the
    release-transaction and long-running dispatcher design;
  - added `vpsadmin:event_delivery:emails` and a default Nix timer to queue
    planned e-mail deliveries and reconcile queued deliveries to sent/failed
    based on the mail transaction state. This was superseded on 2026-06-17 by
    `vpsadmin-notification-dispatcher email`;
  - event type metadata now records the default e-mail template for
    incident/OOM events and exposes it through `event_type#index`;
  - `MailTemplate.send_mail!` can skip default/template recipients for custom
    routed e-mail actions while preserving old behavior for default account
    e-mail;
  - incident report send/process/new chains emit `vps.incident_report` events
    and then schedule routed e-mail deliveries;
  - OOM report notifications emit a batched `vps.oom_report` event with
    bounded selected report ids, batch boundaries, counts, cgroups, and
    selected process data before marking reports as reported;
  - OOM prevention emits `vps.oom_prevention` before appending the restart/stop
    subchain;
  - the dev cluster remains stopped, per user request, and long integration
    tests are skipped until the implementation is further along.
- Follow-up focused verification:
  - Ruby syntax passed for changed event, delivery task, transaction chain,
    incident/OOM chain, mail template, and e-mail delivery spec files.
  - `git diff --check` passed.
  - `nix develop -c nixfmt --check nixos/modules/vpsadmin/api/rake-tasks.nix`
    passed.

## 2026-06-17 checkpoints

- WebUI advanced e-mail cleanup committed:
  - commit `83c02b24d` (`webui: point advanced e-mail settings to notifications`);
  - member detail page now links to notification routes/receivers instead of
    rendering the legacy role-recipient form;
  - the old advanced e-mail sidebar entry and legacy `role_recipients` /
    `template_recipients` actions redirect to Notifications;
  - legacy API/tables remain for compatibility with direct-mail fallback and
    rollback.
- WebUI cleanup verification:
  - `nix develop .#webui -c php -l pages/page_adminm.php` passed;
  - `nix develop .#webui -c bash -lc 'composer install && composer test --
    tests/Regression/CsrfContextSwitchTest.php
    tests/Regression/XssReportSinksTest.php'` passed: 4 tests,
    35 assertions;
  - `git diff --check` passed;
  - Overcommit hooks passed on commit.

## 2026-06-17 request plugin routing

- Request-plugin notification routing committed and amended:
  - commit `5463d2bc3f29f02acea12be5f6808f3bd9e5632e`
    (`notifications: route request plugin mails`);
  - request create/update/resolve mail paths now emit `request.created`,
    `request.updated`, and `request.resolved` events;
  - request event metadata supports routing by request type, state, action,
    role, mail id, recipient, admin, and target user;
  - request mail rendering keeps the legacy template fallback order and mail
    threading headers from persisted event parameters;
  - advanced e-mail template overrides for request templates are migrated to
    matcher-backed routes ordered by the same fallback specificity.

## 2026-06-17 notification WebUI and integration coverage

- Workspace note: `bin/dev-session current` reports
  `2026-06-10-vpsadminos-nftables-bug`, but this request continued in the
  existing `/worktrees/2026-06-15-vpsadmin-events/vpsadmin` worktree and
  `/work/2026-06-15-vpsadmin-events` notes.
- Implemented notification WebUI follow-up:
  - Notifications main-menu default now opens Event log; Routes stay first in
    the Notifications sidebar.
  - Route drag-and-drop starts only from the first-column drag handle, moves a
    parent route together with its child rows, and rejects drops that would
    move a route beneath its own descendant.
  - Existing matcher fields are shown as raw, non-editable field names.
  - Adding a matcher now first selects an event type when needed, then offers
    fields for that event type plus common fields; operator labels include
    descriptions such as `== (equals)`.
  - Route edit no longer renders the all-event matchable field tables.
  - Event types are grouped by category with nested matchable-field tables.
  - Event log filters can scope by notification receiver or receiver action;
    receiver/action rows link to those scoped event logs.
  - Webhook receiver action URL inputs were shortened to avoid widening the
    action form table.
- Added API event log filters for `notification_receiver_id` and
  `notification_receiver_action_id`, backed by delivery joins and distinct
  event results.
- Added notification system integration coverage:
  - `tests/suite/alerts/notification-routing.nix` creates a real receiver with
    e-mail and webhook actions, routes a `user.test_notification` event by a
    matcher, verifies Mailpit delivery, verifies the webhook POST body and
    signature headers, and checks delivery/attempt response state.
  - The webhook test service enables private localhost webhook targets only in
    the test VM through `VPSADMIN_EVENT_WEBHOOK_ALLOW_PRIVATE=1`.
- Updated the support-pages browser test:
  - covers the notification Event log default, Event types grouping, shortened
    webhook URL input, receiver/action scoped event-log links, matcher add
    flow, drag-handle-only route reordering, child-route persistence, and
    parent-under-child prevention;
  - updates stale OOM rule CRUD expectations to verify the intentional redirect
    from old OOM rule URLs to notification routes.
- Validation:
  - `php -l webui/forms/notifications.forms.php && php -l
    webui/pages/page_notifications.php` passed.
  - `nix shell nixpkgs#nodejs -c node --check
    tests/playwright/webui/specs/support-pages.spec.cjs` passed.
  - `nix-instantiate --parse tests/suite/alerts/notification-routing.nix
    >/dev/null && nix-instantiate --parse tests/all-tests.nix >/dev/null &&
    git diff --check` passed.
  - `./test-runner.sh test 'webui#support-pages'` passed: 1 script successful
    in 818.68 seconds.
  - `./test-runner.sh test alerts/notification-routing` passed: 1 example,
    0 failures, 1 script successful in 379.06 seconds.
  - `nix develop .#api -c bash -lc 'bundle exec rspec
    spec/api/resources/event_routing_spec.rb
    spec/models/tasks/event_delivery_spec.rb'` passed: 38 examples,
    0 failures.
- Mandatory review by standalone agent `019ed36f-9b94-7861-998e-d2b33bdc33b5`
  found:
  - Blocking: public registration owner e-mails could be dropped because
    those requests have no current user and therefore no user-owned routes;
  - Important: grouped admin request notifications could choose a disabled
    duplicate e-mail account instead of an enabled admin with the same e-mail.
- Request-plugin review fixes:
  - nil-user request-owner events with a persisted recipient are delivered as
    direct e-mail deliveries using the snapshotted recipient and template;
  - delayed request rendering allows nil-user public registration events only
    when the persisted recipient still matches the request owner e-mail;
  - grouped admin recipients now prefer enabled admins when multiple admin
    accounts share one e-mail address, while disabled-only addresses still
    produce muted delivery logs.
- Request-plugin verification:
  - Ruby syntax passed for the changed router, delivery models, request utils,
    and request specs;
  - focused request specs passed: 9 examples, 0 failures;
  - broader request/routing/delivery quick suite passed:
    62 examples, 0 failures;
  - standalone RuboCop passed: 13 files inspected, no offenses;
  - `git diff --check` passed;
  - `ruby tests/ci-selection-test.rb` passed: 15 runs, 54 assertions;
  - amend commit hooks passed: Nixfmt and RuboCop; commit-message text width
    warned at 72 columns, but lines remain within the repository's 80-column
    limit.
- Follow-up mandatory review by standalone agent
  `019ed381-5fb5-7751-a7d4-f8bdb1bb7d32`:
  - Blocking findings: none.
  - Important finding: direct public-registration e-mail deliveries skipped
    the shared e-mail claim bookkeeping, so a missing mail server left
    `attempt_count` unchanged and could retry forever.
  - Advisory finding: the state/review packet had an incorrect amended head
    hash; actual reviewed head was
    `2ee118bf801006b8e1e26ad8de6b8e33d67a6c6c`.
- Follow-up review fix:
  - direct e-mail deliveries now pass through the same queued/attempt update
    as receiver-action e-mail deliveries;
  - delivery task coverage now checks direct e-mail retry behavior when no
    mail server is available.
  - amended head before the final follow-up fix:
    `80054b787135daba798de288c82247352da383bd`.
- Follow-up review fix verification:
  - serial Ruby syntax passed for the changed e-mail delivery chain and
    delivery task spec;
  - focused delivery/request specs passed: 28 examples, 0 failures;
  - broader request/routing/delivery quick suite passed:
    63 examples, 0 failures;
  - RuboCop passed for the changed e-mail delivery chain and delivery task
    spec: 2 files inspected, no offenses;
  - `git diff --check` passed;
  - `ruby tests/ci-selection-test.rb` passed: 15 runs, 54 assertions;
  - amend commit hooks passed: Nixfmt and RuboCop; commit-message text width
    warned at 72 columns, but lines remain within the repository's 80-column
    limit.
- Final follow-up mandatory review by standalone agent
  `019ed38d-e8cc-7131-bd65-9c5499c57250`:
  - Blocking findings: none.
  - Important finding: receiver-backed e-mail deliveries could be reclassified
    as direct after receiver/action nullification, allowing delivery after the
    receiver was deleted.
- Final follow-up review fix:
  - direct e-mail delivery recognition is narrowed to nil-user request-owner
    events whose target matches the persisted `recipient_email`;
  - delivery task coverage now checks that receiver-backed e-mail deliveries
    are canceled, not sent, after receiver deletion.
  - final amended head:
    `5463d2bc3f29f02acea12be5f6808f3bd9e5632e`.
- Final follow-up review fix verification:
  - Ruby syntax passed for `api/models/event_delivery.rb` and
    `api/spec/models/tasks/event_delivery_spec.rb`;
  - focused delivery/request specs passed: 29 examples, 0 failures;
  - broader request/routing/delivery quick suite passed:
    64 examples, 0 failures;
  - RuboCop passed for `api/models/event_delivery.rb` and
    `api/spec/models/tasks/event_delivery_spec.rb`: 2 files inspected,
    no offenses;
  - `git diff --check` passed;
  - `ruby tests/ci-selection-test.rb` passed: 15 runs, 54 assertions;
  - amend commit hooks passed: Nixfmt and RuboCop; commit-message text width
    warned at 72 columns, but lines remain within the repository's 80-column
    limit.
- Final follow-up mandatory review by standalone agent
  `019ed399-74c5-76b0-a651-7fbd5d8edcb2`:
  - Blocking findings: none.
  - Important findings: none.
  - Advisory findings: none.
  - Residual risk: long integration/dev-cluster coverage remains intentionally
    skipped, and remaining notification conversions are outside this slice.
- User account/security notification slice committed:
  - commit `e0cdbd05b`
    (`notifications: route user account mail events`);
  - added event types for account creation, suspend/resume/revive/soft-delete,
    new sign-in, new access token, TOTP recovery-code use, and failed-login
    reports;
  - converted the matching user transaction chains to `route_event!`;
  - added transient `runtime_email_vars` so immediate routed e-mail delivery
    can render the existing templates with the same non-JSON objects as the
    old direct mail path, while stored event parameters remain safe for
    matching/webhooks/log display;
  - extended the advanced e-mail migration list so account/admin role and
    template recipient settings for these templates become explicit routes.
- User account/security verification:
  - Ruby syntax passed for the touched event, migration, model, transaction
    chain, and spec files;
  - focused user-chain specs passed: 13 examples, 0 failures;
  - routing/API specs passed: 31 examples, 0 failures;
  - post-lint TOTP/routing model rerun passed: 18 examples, 0 failures;
  - RuboCop passed for 23 touched Ruby files;
  - `git diff --check` passed;
  - post-review focused regressions passed: 17 examples, 0 failures;
  - post-review broad focused pass covered user chains, route models, and API
    routing specs: 46 examples, 0 failures;
  - Overcommit hooks passed on the amended commit.
- User account/security mandatory review:
  - Blocking: `event#test` accepted arbitrary registered event types and
    parameter payloads, and some e-mail variable builders rehydrated
    parameter ids without scoping them to the event user. A user could craft a
    test event that referenced another user's failed-login rows or TOTP device
    and leak details into an e-mail render.
  - Important: failed-login attempts could be marked reported when routed
    e-mail rendering failed locally before any mail transaction was queued.
- User account/security review follow-up:
  - parameter-based source rehydration now scopes user-owned objects and
    failed-login lookup to the event user;
  - user-owned event sources are ignored if they do not belong to the event
    user;
  - failed-login reports now raise before setting `reported_at` unless the
    routed event produced a handled delivery outcome, preserving retryability
    for local e-mail rendering/queue failures;
  - regression specs cover malicious test-event parameter ids and failed-login
    retry behavior.
- VPS/resource notification slice committed:
  - commit `1f2a74af0`
    (`notifications: route VPS resource mail events`);
  - added event types for VPS suspend/resume, resource changes, DNS resolver
    changes, network enabled/disabled, and stopped-over-quota notices;
  - converted the matching transaction chains to `route_event!`;
  - added safe persisted parameter snapshots for delayed rendering and
    webhook payloads while keeping runtime mail vars for the existing e-mail
    templates;
  - extended advanced e-mail backfill so existing role/template recipients for
    these templates become explicit notification routes;
  - added direct specs for VPS block/unblock routed events and updated VPS
    update, DNS resolver update, and over-quota specs to assert routed events
    and queued mail deliveries.
- VPS/resource notification verification:
  - Ruby syntax passed for the changed event registry, migration,
    transaction chains, and specs;
  - focused route/VPS-resource specs passed: 44 examples, 0 failures;
  - broad quick routing/delivery/user/VPS-resource pass passed:
    76 examples, 0 failures;
  - RuboCop passed for 13 touched Ruby files;
  - `git diff --check` passed;
  - `ruby tests/ci-selection-test.rb` passed: 15 runs, 54 assertions;
  - local API topic mapping check verified the two new VPS specs map only to
    the existing `engine` topic;
  - Overcommit hooks passed on commit. The TextWidth hook warned at 72
    columns, but all commit-message lines are 80 columns or fewer.
- VPS/resource notification mandatory review:
  - Standalone reviewer `Mill`
    (`019ed2e6-968c-7bf0-9593-33f3a7965d62`) reviewed the slice before the
    final amend. The review packet accidentally contained malformed full
    commit hashes; the actual reviewed range was
    `e0cdbd05b3d963a673a74442912eb3c2d48b8ee4..32cd506b3a784f465161460d123a2ee9adc89bf1`.
  - Blocking: delayed fallback rendering for new VPS events used the live
    `event.vps` without checking that the VPS still belonged to the event
    user.
  - Blocking: advanced-mail role backfill produced separate
    `vps_suspend`/`vps_resume` role routes, but routes stopped at the first
    match and therefore lost a second matching role recipient.
  - Important: migrated custom recipient routes intentionally do not append
    global mail-template recipients. This matches explicit receiver/action
    routing semantics and avoids hidden extra recipients; old template
    recipient settings are represented as their own generated actions where
    they are migrated.
- VPS/resource notification review follow-up:
  - delayed VPS e-mail rendering now fails before creating mail if the source
    VPS has been reassigned away from the event user;
  - migrated multi-role template routes set `continue = true` for earlier
    matching role routes when another eligible role recipient must also be
    delivered for the same event;
  - regression specs cover both the delayed-rendering ownership guard and
    account+admin role delivery for `vps.suspended`.
- VPS/resource notification post-review verification:
  - full `spec/models/event_route_spec.rb` and
    `spec/models/tasks/event_delivery_spec.rb` passed:
    35 examples, 0 failures;
  - broader routing/delivery/user/VPS-resource quick pass passed:
    78 examples, 0 failures;
  - RuboCop passed for the four review-fix Ruby files;
  - `git diff --check` passed;
  - `ruby tests/ci-selection-test.rb` passed: 15 runs, 54 assertions;
  - amended commit hooks passed. The TextWidth hook warned at 72 columns, but
    all commit-message lines are 80 columns or fewer.
- VPS/resource notification follow-up mandatory review:
  - Standalone reviewer `Popper`
    (`019ed2f9-bd08-77b0-b1f1-8f8e5fa6f7c0`) reviewed
    `e0cdbd05b3d963a673a74442912eb3c2d48b8ee4..1f2a74af01dd9c0e0a5bac7ce95445ef69f148c0`
    after the final amend.
  - Result: no blocking, important, or advisory findings.
  - Residual risks: dev cluster and long integration tests remain skipped by
    user request; `vps.network_enabled` positive coverage is mostly through
    shared enable-network behavior; full historical migration is still limited
    by pre-existing old migration-stack issues.
- VPS/storage lifecycle notification slice committed:
  - commit `722da56cc10001a35795917af8e7c5a6687cace1`
    (`notifications: route VPS lifecycle mail events`);
  - added event types and matcher metadata for dataset expand/shrink,
    snapshot download readiness, dataset migration begun/finished, VPS
    migration planned/begun/finished, and VPS replacement;
  - converted the matching transaction chains from direct
    `MailTemplate.send_mail!` calls to `route_event!`, preserving existing
    e-mail templates through runtime vars and safe persisted parameters;
  - extended advanced e-mail migration backfill for the newly covered
    templates;
  - fixed delayed VPS migration rendering to validate `VpsMigration` ownership
    through the migrated VPS owner, since `vps_migrations` has no `user_id`
    column.
  - delayed fallback data now keeps collection parameters bounded: dataset
    migration events store `affected_vps_count` plus a 30-item sample, and
    fallback e-mail vars clamp generated placeholder arrays to 100 items.
- VPS/storage lifecycle verification:
  - `git diff --check` passed;
  - Ruby syntax passed for the changed event registry, migration, and
    transaction-chain files;
  - focused lifecycle/routing spec pass covered event routes, event delivery,
    dataset expand/shrink, snapshot download, dataset migration, VPS
    migration, migration-plan mail, and VPS replacement:
    81 examples, 0 failures, 1 known pre-existing pending
    migration-network-interface example;
  - RuboCop passed for the 19 changed Ruby/spec files;
  - post-review RuboCop passed for the four changed review-fix files;
  - `ruby tests/ci-selection-test.rb` passed: 15 runs, 54 assertions;
  - Overcommit hooks passed on commit. The TextWidth hook warned at 72
    columns, but all commit-message lines are 80 columns or fewer.
- VPS/storage lifecycle mandatory review:
  - Standalone reviewer `Faraday`
    (`019ed319-cea5-7bd0-8525-4e2bc0f96a66`) reviewed the original
    lifecycle commit
    `1f2a74af01dd9c0e0a5bac7ce95445ef69f148c0..4998c6af3990b7ee4e1017046d6aa1c6c90d75ec`.
  - Blocking: dataset migrations with more than 100 affected VPSes could fail
    event validation because all affected VPSes were stored in
    `parameters.affected_vpses`.
  - Blocking: delayed dataset-migration fallback rendering used
    `Array.new(parameters.export_count)`, allowing a user-created test event
    to make the e-mail worker allocate an attacker-controlled array.
  - Advisory: delayed fallback renderers should have direct worker coverage.
  - Review follow-up:
    - dataset migration event parameters now store `affected_vps_count` and a
      bounded `affected_vpses` sample while keeping the full runtime VPS list
      for immediate e-mail rendering;
    - delayed fallback collection counts are clamped before arrays are
      allocated;
    - regression coverage verifies the bounded affected-VPS sample and the
      delayed dataset-migration e-mail worker path with a huge `export_count`.
  - Follow-up mandatory review requested after amending the lifecycle commit to
    `722da56cc10001a35795917af8e7c5a6687cace1`.
  - Follow-up reviewer `Einstein`
    (`019ed32a-5c35-7d60-8c3e-503618b6043f`) found no blocking, important,
    or advisory issues.
  - Residual risks: dev cluster/long integration tests remain skipped by user
    request; full historical migration remains limited by pre-existing old
    migration-stack issues; delayed worker coverage is strongest for the
    dataset-migration fallback path that caused the blocker.
  - Dev cluster remains stopped and long integration tests remain skipped per
    user request.
- Security advisory notification slice implemented:
  - added event types and matcher metadata for
    `security_advisory.announced` and `security_advisory.updated`;
  - converted `TransactionChains::SecurityAdvisories::Mail` from direct
    `MailTemplate.send_mail!` calls to per-user routed events;
  - affected users with disabled mailer settings now get persisted suppressed
    event/delivery log rows through their muted default receiver instead of
    being filtered out before notification routing;
  - existing security advisory mail templates remain in use through runtime
    e-mail vars, with delayed fallback lookup scoped by
    `SecurityAdvisory.visible_to(event.user)` and affected VPS rows scoped to
    the event user;
  - persisted parameters include advisory/update ids, CVEs, state,
    publication time, affected VPS count, and a bounded affected-VPS sample;
  - advanced e-mail migration backfill now covers the security advisory
    announce/update templates.
- Security advisory verification:
  - `git diff --check` passed;
  - Ruby syntax passed for the changed event registry, migration, transaction
    chain, and spec file;
  - focused `spec/models/security_advisory_spec.rb` passed:
    5 examples, 0 failures;
  - RuboCop passed for the four changed Ruby/spec files;
  - `ruby tests/ci-selection-test.rb` passed: 15 runs, 54 assertions.
  - Overcommit hooks passed on commit. The TextWidth hook warned at 72
    columns, but all commit-message lines are 80 columns or fewer.
  - commit `dd1bd3625cbc9a797f4c670523abe93c3187b665`
    (`notifications: route security advisory mail events`).
- Security advisory mandatory review:
  - Standalone reviewer `Curie`
    (`019ed342-a67f-7b70-a468-1715b5ab5f94`) reviewed
    `722da56cc10001a35795917af8e7c5a6687cace1..dd1bd3625cbc9a797f4c670523abe93c3187b665`.
  - Result: no blocking, important, or advisory findings.
  - Residual risks: dev-cluster/long integration verification remains skipped;
    advisory coverage does not yet include a full async worker render; there
    is no explicit non-admin draft-advisory parameter-event regression, though
    `SecurityAdvisory.visible_to(event.user)` guards that fallback path.
  - Dev cluster remains stopped and long integration tests remain skipped per
    user request.
- Lifetime expiration warning slice committed:
  - commit `0abf2db206ad8c9d8cb4e40a7f494b92836ca3ca`
    (`notifications: route expiration warning mails`);
  - registered `lifetime.expiration_warning` with account/warning metadata
    and matchable parameters for object type, object id/label, lifecycle
    state, dates, and day helper values;
  - converted `TransactionChains::Lifetimes::ExpirationWarning` from direct
    `mail(:expiration_warning, ...)` calls to routed events with runtime
    e-mail vars for immediate rendering and safe persisted parameters for
    delayed delivery/log display/webhooks;
  - disabled-mailer users now get persisted suppressed event/delivery rows
    through the generated muted receiver instead of being skipped before
    routing;
  - delayed e-mail rendering passes persisted `object` and `state` template
    params back into `MailTemplate.resolve_name`, preserving existing
    `expiration_user_active` and `expiration_vps_active` concrete templates;
  - advanced e-mail migration now maps legacy concrete expiration template
    recipient overrides to generic expiration-warning routes with
    `parameters.object` and `parameters.state` matchers.
- Lifetime expiration warning verification:
  - Ruby syntax passed for the changed event registry, migration,
    expiration-warning chain, and specs;
  - focused `spec/models/transaction_chains/lifetimes/expiration_warning_spec.rb`
    passed: 6 examples, 0 failures;
  - `spec/models/event_route_spec.rb` plus the expiration-warning spec passed:
    25 examples, 0 failures;
  - broad corrected quick suite covering event routes, event delivery,
    lifetime tasks, and expiration warnings passed: 54 examples, 0 failures;
  - an earlier broad command used stale spec paths and failed before examples;
    the corrected paths were
    `spec/models/tasks/event_delivery_spec.rb` and
    `spec/models/tasks/lifetimes_spec.rb`;
  - RuboCop passed for the five changed Ruby/spec/migration files;
  - `git diff --check` passed;
  - `ruby tests/ci-selection-test.rb` passed: 15 runs, 54 assertions;
  - Overcommit hooks passed on commit. The TextWidth hook warned at 72
    columns, but all commit-message lines are 80 columns or fewer.
  - Dev cluster remains stopped and long integration tests remain skipped per
    user request.
- Lifetime expiration warning mandatory review:
  - Standalone reviewer `Hegel`
    (`019ed358-d96b-7cb3-a3ee-ddb47fc32ac8`) reviewed
    `dd1bd3625cbc9a797f4c670523abe93c3187b665..0abf2db206ad8c9d8cb4e40a7f494b92836ca3ca`.
  - Result: no blocking, important, or advisory findings.
  - Residual risks: dev-cluster/long integration verification remains
    skipped; delayed worker coverage directly checks user expiration but not a
    dedicated VPS-expiration reassignment/deletion case, relying on the shared
    `required_vps` guard; expiration-specific role-recipient migration is not
    directly covered.
  - Dev cluster remains stopped and long integration tests remain skipped per
    user request.
- Requests plugin notification slice committed:
  - commit `a672f909e9c950eff7e8dbe75b482a4de2bfd146`
    (`notifications: route request plugin mails`);
  - registered request event types for create, update, and resolve
    notifications with matchable `parameters.role`, action, request type,
    request state, request id/label, recipient e-mail, and mail-thread ids;
  - converted Requests plugin create/update/resolve chains from direct mail
    calls to routed per-recipient events for request owners and admins;
  - preserved the existing parameterized mail-template fallback order:
    action+role+type before action+role, and for resolves
    role+type+state, action+role+type, role+state, then action+role;
  - persisted request mail thread ids and reconstructs `Message-ID`,
    `In-Reply-To`, and `References` during e-mail rendering;
  - request-owner events keep the request e-mail address as an explicit
    default-recipient target so registration requests still mail the address
    on the request;
  - disabled admin mailer settings now produce muted suppressed event/delivery
    rows instead of being filtered out before routing;
  - delayed/test-event request rehydration is scoped: user-role events require
    the request to belong to the event user, and admin-role events require an
    admin event user;
  - legacy request template recipient overrides migrate to matcher-backed
    routes ordered by fallback specificity, so specific type/state overrides
    win before generic request overrides.
- Requests plugin notification verification:
  - Ruby syntax passed for the changed event registry, migration, request
    chains, helper, and specs;
  - focused request chain specs passed: 5 examples, 0 failures;
  - focused request chain plus event-route migration specs passed:
    26 examples, 0 failures;
  - broader routing/delivery/API request quick pass passed:
    59 examples, 0 failures;
  - RuboCop passed for the 11 changed Ruby/spec/migration files;
  - `git diff --check` passed;
  - `ruby tests/ci-selection-test.rb` passed: 15 runs, 54 assertions;
  - Overcommit hooks passed on commit. The TextWidth hook warned at 72
    columns, but all commit-message lines are 80 columns or fewer.
  - Dev cluster remains stopped and long integration tests remain skipped per
    user request.
- Payment accepted notification slice committed:
  - commit `9d6cba3ac8270ef02628d2ffda6657bc25edc084`
    (`notifications: route payment accepted mails`);
  - registered `payment.accepted` with payment/accounting matcher metadata;
  - converted the Payments plugin create chain from direct
    `payment_accepted` mail guarded by `mailer_enabled` to a routed event
    with runtime e-mail vars and persisted routing/webhook parameters;
  - the generated default routing/mute receiver now preserves the old
    mailer-enabled behavior while still logging suppressed payment events;
  - delayed e-mail rendering can use the live `UserPayment` source when
    available, or reconstruct a bounded fallback payment object from stored
    event parameters;
  - advanced e-mail migration now maps legacy `payment_accepted` template
    recipient overrides to explicit notification routes.
- Payment accepted notification verification:
  - Ruby syntax passed for the changed event registry, migration, payment
    chain, and specs;
  - focused payment create plus event-route specs passed:
    26 examples, 0 failures;
  - broader payment/routing/delivery/API quick suite passed:
    62 examples, 0 failures;
  - RuboCop passed for the five changed Ruby/spec/migration files;
  - `git diff --check` passed;
  - `ruby tests/ci-selection-test.rb` passed: 15 runs, 54 assertions;
  - Overcommit hooks passed on commit. The TextWidth hook warned at 72
    columns, but all commit-message lines are 80 columns or fewer.
  - Dev cluster remains stopped and long integration tests remain skipped per
    user request.
- Payment accepted mandatory review:
  - Standalone reviewer `Erdos`
    (`019ed3ad-3d83-75d0-96a3-63d8a5179265`) reviewed
    `5463d2bc3f29f02acea12be5f6808f3bd9e5632e..9d6cba3ac8270ef02628d2ffda6657bc25edc084`.
  - Result: no blocking, important, or advisory findings.
  - Reviewer also ran
    `spec/api/plugins/payments/user_payment_spec.rb`: 15 examples,
    0 failures.
  - Residual risks: dev-cluster/long integration verification remains
    skipped; delayed async worker rendering for `payment.accepted` is covered
    by shared delivery machinery rather than a payment-specific worker spec;
    full historical migration remains limited by pre-existing old
    migration-stack issues.
  - Dev cluster remains stopped and long integration tests remain skipped per
    user request.
- Outage report notification slice committed:
  - commit `9c3c837d4e3611d695cfacfcf30e9014bcb7a53a`
    (`notifications: route outage report mails`);
  - registered `outage.announced` and `outage.updated` with role, event,
    outage, update, affected-resource, CVE, threading, and admin metadata;
  - converted the Outage reports plugin update chain from direct template
    mail to routed events;
  - generic outage mail is logged as a direct system-template delivery that
    still uses global template recipients;
  - affected-user outage mail is routed through each user's notification
    routes, so disabled mailer settings now produce visible suppressed
    delivery rows instead of being filtered before routing;
  - delayed e-mail rendering scopes live outage rehydration to affected users
    or admins and uses compact fallback objects from stored parameters;
  - advanced e-mail migration now maps legacy
    `outage_report_user_announce` and `outage_report_user_update` overrides
    to notification routes, with update overrides applying to update,
    cancel, and resolve events as the old template fallback did.
- Outage report notification verification:
  - Ruby syntax passed for the changed event registry, delivery model,
    migration, outage chain, and specs;
  - focused outage update plus event-route specs passed:
    26 examples, 0 failures;
  - broader outage/routing/delivery/API quick suite passed:
    135 examples, 0 failures;
  - RuboCop passed for the six changed Ruby/spec/migration files;
  - `git diff --check` passed;
  - `ruby tests/ci-selection-test.rb` passed: 15 runs, 54 assertions;
  - Overcommit hooks passed on commit. The TextWidth hook warned at 72
    columns, but all commit-message lines are 80 columns or fewer.
  - Dev cluster remains stopped and long integration tests remain skipped per
    user request.
- Outage report mandatory review:
  - Standalone reviewer `Pauli`
    (`019ed3c2-3f0d-7ca0-a373-9e2f669097a4`) reviewed
    `9d6cba3ac8270ef02628d2ffda6657bc25edc084..9c3c837d4e3611d695cfacfcf30e9014bcb7a53a`.
  - Result: no blocking, important, or advisory findings.
  - Residual risks: delayed outage fallback rendering is privacy-oriented but
    not deeply covered against every external template method if the live
    outage/update is gone; generic direct-system retry through the e-mail
    delivery rake task has no dedicated outage-specific spec; dev-cluster and
    long integration verification remain skipped by user request.
  - Dev cluster remains stopped and long integration tests remain skipped per
    user request.
- Routed event e-mail follow-up details from the previous slice:
  - `nix develop .#api -c bash -lc 'bundle exec rubocop lib/vpsadmin/api/events.rb lib/vpsadmin/api/resources/event_type.rb lib/vpsadmin/api/tasks/event_delivery.rb models/mail_template.rb models/transaction_chain.rb models/transaction_chains/event_delivery/email.rb models/transaction_chains/incident_report/send.rb models/transaction_chains/vps/oom_reports.rb models/transaction_chains/vps/oom_prevention.rb spec/models/tasks/event_delivery_spec.rb'`
    passed.
  - `nix develop .#api -c bash -lc 'bundle exec rspec spec/models/event_route_spec.rb spec/api/resources/event_routing_spec.rb spec/models/tasks/event_delivery_spec.rb spec/models/transaction_chains/incident_report/send_spec.rb spec/models/transaction_chains/incident_report/process_spec.rb spec/models/transaction_chains/incident_report/new_spec.rb spec/models/transaction_chains/vps/oom_reports_spec.rb spec/models/transaction_chains/vps/oom_prevention_spec.rb spec/api/endpoint_coverage_spec.rb spec/api/custom_routes_coverage_spec.rb'`
    passed: 51 examples, 0 failures.
  - After narrowing default template names to e-mail deliveries only,
    `nix develop .#api -c bash -lc 'bundle exec rspec spec/models/event_route_spec.rb spec/models/tasks/event_delivery_spec.rb'`
    passed: 14 examples, 0 failures.
  - Mandatory review found a cross-tenant OOM report rendering path through
    user-created test events and an event parameter array limit failure when a
    VPS had more than 100 unreported OOM report rows.
  - Review fixes:
    - OOM e-mail rendering now scopes report lookup to the event user and,
      when present, the event VPS.
    - OOM event payloads no longer persist an unbounded `report_ids` array;
      they store a bounded sample plus `last_reported_id`,
      `batch_reported_at`, and aggregate counts.
  - Review-fix verification:
    - `nix develop .#api -c bash -lc 'bundle exec rspec spec/models/tasks/event_delivery_spec.rb spec/models/transaction_chains/vps/oom_reports_spec.rb'`
      passed: 13 examples, 0 failures.
    - `nix develop .#api -c bash -lc 'ruby -c lib/vpsadmin/api/events.rb && ruby -c models/transaction_chains/vps/oom_reports.rb && ruby -c spec/models/tasks/event_delivery_spec.rb && ruby -c spec/models/transaction_chains/vps/oom_reports_spec.rb'`
      passed.
    - `git diff --check` passed.
    - `nix develop .#api -c bash -lc 'bundle exec rubocop lib/vpsadmin/api/events.rb models/transaction_chains/vps/oom_reports.rb spec/models/tasks/event_delivery_spec.rb spec/models/transaction_chains/vps/oom_reports_spec.rb'`
      passed: 4 files inspected, no offenses.
    - `nix develop .#api -c bash -lc 'bundle exec rspec spec/models/event_route_spec.rb spec/api/resources/event_routing_spec.rb spec/models/tasks/event_delivery_spec.rb spec/models/transaction_chains/incident_report/send_spec.rb spec/models/transaction_chains/incident_report/process_spec.rb spec/models/transaction_chains/incident_report/new_spec.rb spec/models/transaction_chains/vps/oom_reports_spec.rb spec/models/transaction_chains/vps/oom_prevention_spec.rb spec/api/endpoint_coverage_spec.rb spec/api/custom_routes_coverage_spec.rb'`
      passed: 53 examples, 0 failures.
  - No long integration tests or dev cluster start were run for this follow-up
    slice.
- Follow-up commit:
  `13f32c409a5bd3f98fdd0f963da04f7db5bede15`
  (`notifications: deliver routed event e-mails`).
- Review hardening commit:
  `dbf5caeabeba857215e06eee3de8b2148fcbaeb6`
  (`notifications: harden routed delivery edge cases`).
- Follow-up mandatory review requested from standalone agent `Raman`
  (`019ed1e9-55bf-76e0-a608-276aba0e0751`) using
  `skills/mandatory-change-review/SKILL.md` against `ac7f8a..c07b617`.
- Follow-up mandatory review result:
  - Blocking: e-mail delivery sync treated any finished transaction as sent,
    even when the mail transaction finished with failed status.
  - Important: disabling or muting a receiver/action did not stop already
    planned or retryable deliveries.
- Review follow-up fixes:
  - e-mail sync now marks deliveries sent only for finished mail transactions
    with success status and marks failed finished transactions as failed;
  - planned/reclaimable e-mail deliveries and retryable webhooks cancel when
    their receiver is disabled/muted or their action is unavailable;
  - the e-mail queue worker also reclaims crash-left `queued` deliveries that
    have no mail transaction id yet.
- Review follow-up verification:
  - `nix develop .#api -c bash -lc 'ruby -c models/event_delivery.rb && ruby -c lib/vpsadmin/api/tasks/event_delivery.rb && ruby -c models/transaction_chains/event_delivery/email.rb && ruby -c spec/models/tasks/event_delivery_spec.rb'`
    passed.
  - `nix develop .#api -c bash -lc 'bundle exec rspec spec/models/tasks/event_delivery_spec.rb'`
    passed: 11 examples, 0 failures.
  - `git diff --check` passed.
  - `nix develop .#api -c bash -lc 'bundle exec rubocop models/event_delivery.rb lib/vpsadmin/api/tasks/event_delivery.rb models/transaction_chains/event_delivery/email.rb spec/models/tasks/event_delivery_spec.rb'`
    passed: 4 files inspected, no offenses.
  - `nix develop .#api -c bash -lc 'bundle exec rspec spec/models/event_route_spec.rb spec/api/resources/event_routing_spec.rb spec/models/tasks/event_delivery_spec.rb spec/models/transaction_chains/incident_report/send_spec.rb spec/models/transaction_chains/incident_report/process_spec.rb spec/models/transaction_chains/incident_report/new_spec.rb spec/models/transaction_chains/vps/oom_reports_spec.rb spec/models/transaction_chains/vps/oom_prevention_spec.rb spec/api/endpoint_coverage_spec.rb spec/api/custom_routes_coverage_spec.rb'`
    passed: 57 examples, 0 failures.
- Final mandatory review requested from standalone agent `McClintock`
  (`019ed1f8-36da-7041-863b-c6e10b01fa24`) using
  `skills/mandatory-change-review/SKILL.md` against `ac7f8a..eb77b31`.
- Final mandatory review result:
  - Blocking: custom e-mail receiver targets had no length cap. Routing copied
    the custom target into `event_deliveries.target_label`, so stale or long
    user configuration could make event delivery creation fail. In OOM
    prevention, that could abort the chain before restart/stop was appended.
  - Advisory: custom e-mail target normalization was looser than the existing
    user mail-recipient settings.
- Final review follow-up fixes:
  - custom e-mail receiver action targets are normalized like the older mail
    recipient settings by removing whitespace;
  - custom e-mail receiver action targets are capped at the existing
    `mail_logs.to` limit of 500 characters;
  - router delivery labels are defensively capped at 255 characters so stale
    configuration cannot make event emission fail;
  - OOM prevention has regression coverage that stale overlong custom e-mail
    labels do not block appending the restart transaction.
- Final review follow-up verification:
  - `nix develop .#api -c bash -lc 'ruby -c models/notification_receiver_action.rb && ruby -c lib/vpsadmin/api/events.rb && ruby -c spec/models/notification_receiver_action_spec.rb && ruby -c spec/models/transaction_chains/vps/oom_prevention_spec.rb'`
    passed.
  - `nix develop .#api -c bash -lc 'bundle exec rspec spec/models/notification_receiver_action_spec.rb spec/models/transaction_chains/vps/oom_prevention_spec.rb'`
    passed: 7 examples, 0 failures.
  - `git diff --check` passed.
  - `nix develop .#api -c bash -lc 'bundle exec rubocop models/notification_receiver_action.rb lib/vpsadmin/api/events.rb spec/models/notification_receiver_action_spec.rb spec/models/transaction_chains/vps/oom_prevention_spec.rb'`
    passed: 4 files inspected, no offenses.
  - `nix develop .#api -c bash -lc 'bundle exec rspec spec/models/notification_receiver_action_spec.rb spec/models/event_route_spec.rb spec/api/resources/event_routing_spec.rb spec/models/tasks/event_delivery_spec.rb spec/models/transaction_chains/incident_report/send_spec.rb spec/models/transaction_chains/incident_report/process_spec.rb spec/models/transaction_chains/incident_report/new_spec.rb spec/models/transaction_chains/vps/oom_reports_spec.rb spec/models/transaction_chains/vps/oom_prevention_spec.rb spec/api/endpoint_coverage_spec.rb spec/api/custom_routes_coverage_spec.rb'`
    passed: 60 examples, 0 failures.
- Post-fix mandatory review requested from standalone agent `Tesla`
  (`019ed206-34dc-7803-98e6-70d7dfd96bc3`) using
  `skills/mandatory-change-review/SKILL.md` against `ac7f8a..624a4c4`.
- Post-fix mandatory review result:
  - Blocking: none.
  - Important: OOM reports could be marked `reported_at` even when an intended
    e-mail delivery failed during local render/save before any mail transaction
    was queued.
- Post-fix review follow-up:
  - OOM report notification now raises before marking rows reported when any
    routed e-mail delivery failed during inline queueing.
  - Muted/skipped/canceled routing choices remain handled; only local failed
    e-mail queue attempts keep reports retryable.
  - Added regression coverage that a mail rendering failure rolls back the
    event and leaves OOM reports unreported for retry.
- Post-fix review follow-up verification:
  - `nix develop .#api -c bash -lc 'ruby -c models/transaction_chains/vps/oom_reports.rb && ruby -c spec/models/transaction_chains/vps/oom_reports_spec.rb'`
    passed.
  - `nix develop .#api -c bash -lc 'bundle exec rspec spec/models/transaction_chains/vps/oom_reports_spec.rb'`
    passed: 7 examples, 0 failures.
  - `git diff --check` passed.
  - `nix develop .#api -c bash -lc 'bundle exec rubocop models/transaction_chains/vps/oom_reports.rb spec/models/transaction_chains/vps/oom_reports_spec.rb'`
    passed: 2 files inspected, no offenses.
  - `nix develop .#api -c bash -lc 'bundle exec rspec spec/models/notification_receiver_action_spec.rb spec/models/event_route_spec.rb spec/api/resources/event_routing_spec.rb spec/models/tasks/event_delivery_spec.rb spec/models/transaction_chains/incident_report/send_spec.rb spec/models/transaction_chains/incident_report/process_spec.rb spec/models/transaction_chains/incident_report/new_spec.rb spec/models/transaction_chains/vps/oom_reports_spec.rb spec/models/transaction_chains/vps/oom_prevention_spec.rb spec/api/endpoint_coverage_spec.rb spec/api/custom_routes_coverage_spec.rb'`
    passed: 61 examples, 0 failures.
- Final post-fix mandatory review requested from standalone agent `Ohm`
  (`019ed214-e4f3-7fb3-87d0-45a2bfda3ec2`) using
  `skills/mandatory-change-review/SKILL.md` against `ac7f8a..b688487`.
- Final post-fix mandatory review result:
  - Blocking: none.
  - Important: e-mail delivery rendered and saved a `MailLog` before selecting
    a mail server. If mail server selection raised, the delivery was marked
    permanently failed and the `MailLog` was left orphaned without a
    transaction.
- Final post-fix review follow-up:
  - e-mail delivery now selects the mail server before rendering/saving the
    message;
  - missing mail servers keep the delivery queued with exponential backoff
    until the e-mail retry limit is reached;
  - local pre-append failures destroy any unlinked `MailLog` before marking
    the delivery failed.
- Final post-fix review follow-up verification:
  - `nix develop .#api -c bash -lc 'ruby -c models/transaction_chains/event_delivery/email.rb && ruby -c spec/models/tasks/event_delivery_spec.rb'`
    passed.
  - `nix develop .#api -c bash -lc 'bundle exec rspec spec/models/tasks/event_delivery_spec.rb'`
    passed: 12 examples, 0 failures.
  - `git diff --check` passed.
  - `nix develop .#api -c bash -lc 'bundle exec rubocop models/transaction_chains/event_delivery/email.rb spec/models/tasks/event_delivery_spec.rb'`
    passed: 2 files inspected, no offenses.
  - `nix develop .#api -c bash -lc 'bundle exec rspec spec/models/notification_receiver_action_spec.rb spec/models/event_route_spec.rb spec/api/resources/event_routing_spec.rb spec/models/tasks/event_delivery_spec.rb spec/models/transaction_chains/incident_report/send_spec.rb spec/models/transaction_chains/incident_report/process_spec.rb spec/models/transaction_chains/incident_report/new_spec.rb spec/models/transaction_chains/vps/oom_reports_spec.rb spec/models/transaction_chains/vps/oom_prevention_spec.rb spec/api/endpoint_coverage_spec.rb spec/api/custom_routes_coverage_spec.rb'`
    passed: 62 examples, 0 failures.
- Final amend:
  - `nix develop -c git commit --amend -F /tmp/vpsadmin-events-email-commit-message.txt`
    passed hooks: Nixfmt and RuboCop; the TextWidth hook warned at 72
    columns, but all commit-message lines are 80 columns or fewer.
  - Current `vpsadmin` head is
    `13f32c409a5bd3f98fdd0f963da04f7db5bede15`.
- Final mandatory review requested from standalone agent `James`
  (`019ed225-c523-75d3-b7d8-965ad4803416`) using
  `skills/mandatory-change-review/SKILL.md` against
  `f3e1ff0..13f32c4`.
- Final mandatory review result:
  - Blocking: `users.mailer_enabled` remained writable but event-routed
    e-mail defaults did not follow later toggles.
  - Blocking: webhook delivery claims were not exclusive across concurrent
    workers, so two workers could deliver the same due webhook.
  - Important: incident reports could be marked reported when local e-mail
    rendering/queueing failed.
  - Important: queued webhook/e-mail deliveries used current receiver action
    values rather than the delivery snapshot recorded on the event.
  - Important: delivery deduplication used receiver/action ids and did not
    deduplicate equivalent targets from different receivers.
  - Advisory: nested route drag-and-drop can imply parent changes that the
    current flat reorder endpoint does not persist.
- Final review follow-up fixes:
  - generated default notification routing now follows later
    `users.mailer_enabled` changes by muting/unmuting the generated default
    receiver and ensuring its default e-mail action exists when enabled;
  - webhook delivery claims now re-check due state under the row lock and push
    `next_attempt_at` forward while the worker owns the delivery, preventing
    concurrent workers from sending the same due webhook;
  - incident report sending now raises when local e-mail queueing/rendering
    creates a failed e-mail delivery, keeping incidents unreported and
    retryable;
  - webhook delivery uses the snapshotted `event_deliveries.target_value`
    rather than the current receiver action target;
  - e-mail delivery uses the snapshotted delivery target and template name;
  - default e-mail deliveries snapshot the concrete account e-mail address;
  - delivery deduplication now keys deliverable actions by action, target
    kind, snapshotted target, template, and state, so equivalent targets across
    different receivers are emitted once.
- Final review follow-up verification:
  - Ruby syntax passed for changed user, receiver, router, delivery task,
    e-mail delivery chain, incident send chain, and affected specs.
  - `nix develop .#api -c bash -lc 'bundle exec rspec spec/models/event_route_spec.rb spec/models/tasks/event_delivery_spec.rb spec/models/transaction_chains/incident_report/process_spec.rb'`
    passed: 30 examples, 0 failures.
  - `git diff --check` passed.
  - `nix develop .#api -c bash -lc 'bundle exec rubocop models/user.rb models/notification_receiver.rb lib/vpsadmin/api/events.rb lib/vpsadmin/api/tasks/event_delivery.rb models/transaction_chains/event_delivery/email.rb models/transaction_chains/incident_report/send.rb spec/models/event_route_spec.rb spec/models/tasks/event_delivery_spec.rb spec/models/transaction_chains/incident_report/process_spec.rb'`
    passed: 9 files inspected, no offenses.
  - `nix develop .#api -c bash -lc 'bundle exec rspec spec/models/notification_receiver_action_spec.rb spec/models/event_route_spec.rb spec/api/resources/event_routing_spec.rb spec/models/tasks/event_delivery_spec.rb spec/models/transaction_chains/incident_report/send_spec.rb spec/models/transaction_chains/incident_report/process_spec.rb spec/models/transaction_chains/incident_report/new_spec.rb spec/models/transaction_chains/vps/oom_reports_spec.rb spec/models/transaction_chains/vps/oom_prevention_spec.rb spec/api/endpoint_coverage_spec.rb spec/api/custom_routes_coverage_spec.rb'`
    passed: 68 examples, 0 failures.
- Review hardening commit:
  - `nix develop -c git commit -F /tmp/vpsadmin-events-review-fix-commit-message.txt`
    passed hooks: Nixfmt and RuboCop; the TextWidth hook warned at 72
    columns, but all commit-message lines are 80 columns or fewer.
  - Current `vpsadmin` head is
    `dbf5caeabeba857215e06eee3de8b2148fcbaeb6`.
- Final follow-up mandatory review requested from standalone agent `Poincare`
  (`019ed244-9d42-7ab2-8861-2891367c4e90`) using
  `skills/mandatory-change-review/SKILL.md` against
  `f3e1ff0..6351645`.
- Final follow-up mandatory review result:
  - Blocking: none.
  - Important: default-recipient e-mail was snapshotted for delivery
    metadata/deduplication but still rendered through late-bound
    `MailTemplate` recipients, so actual `MailLog.to` could diverge from the
    delivery row.
  - Important: legacy `mailer_enabled` sync could mutate a user-managed
    receiver after the generated default route was repointed to that receiver.
  - Advisory: the known nested route drag/drop limitation remains; flat
    reorder persists positions only and does not reparent routes.
- Final follow-up fixes:
  - default e-mail actions are explicitly late-bound until advanced e-mail
    settings are migrated: delivery rows use `target_value = 'default'` and
    `target_label = 'Default recipient'`, while `MailTemplate` resolves the
    current template/role/account recipients when the e-mail is queued;
  - legacy `mailer_enabled` sync now finds only the generated default receiver
    by its generated label and description, so repointing the default route to
    a normal receiver does not let the old switch rename, mute, or add actions
    to that receiver.
- Final follow-up verification:
  - Ruby syntax passed for changed router, receiver, and affected specs.
  - `nix develop .#api -c bash -lc 'bundle exec rspec spec/models/event_route_spec.rb spec/models/tasks/event_delivery_spec.rb'`
    passed: 27 examples, 0 failures.
  - `git diff --check` passed.
  - `nix develop .#api -c bash -lc 'bundle exec rubocop models/notification_receiver.rb lib/vpsadmin/api/events.rb spec/models/event_route_spec.rb spec/models/tasks/event_delivery_spec.rb'`
    passed: 4 files inspected, no offenses.
  - `nix develop .#api -c bash -lc 'bundle exec rspec spec/models/notification_receiver_action_spec.rb spec/models/event_route_spec.rb spec/api/resources/event_routing_spec.rb spec/models/tasks/event_delivery_spec.rb spec/models/transaction_chains/incident_report/send_spec.rb spec/models/transaction_chains/incident_report/process_spec.rb spec/models/transaction_chains/incident_report/new_spec.rb spec/models/transaction_chains/vps/oom_reports_spec.rb spec/models/transaction_chains/vps/oom_prevention_spec.rb spec/api/endpoint_coverage_spec.rb spec/api/custom_routes_coverage_spec.rb'`
    passed: 70 examples, 0 failures.
- Dev cluster status after commit:
  `dev-clusters/vpsadmin/bin/devcluster status 2026-06-15-vpsadmin-events`
  reports `status: stopped`.

- Previous foundation implementation commit:
  `ac7f8a2617ae3e7c440ffd55ee44c03f52c0768f`
  (`notifications: add event routing foundation`).
- Mandatory change review requested from standalone agent `Lorentz`
  (`019ed17f-9948-79d3-86c0-5dcea6a2e715`) using
  `skills/mandatory-change-review/SKILL.md`.
- Mandatory change review result:
  - Blocking: default catch-all route at position 0 shadowed newly created
    user routes.
  - Blocking: webhook SSRF guard resolved the host before delivery but let
    `Net::HTTP` resolve again, leaving a DNS-rebinding gap.
  - Important: Telegram actions could not be created before a chat id was
    known, so the planned bot pairing flow could not bootstrap.
  - Important: receiver/action fan-out and `event#test` enqueueing were
    uncapped.
  - Advisory: add webhook SSRF coverage for the pinned-address fix.
- Follow-up fixes applied:
  - default routes are last-resort catch-alls at position 10000 for new
    migrations/defaults;
  - route creation without an explicit root position inserts before the
    default catch-all and shifts existing defaults if needed;
  - the WebUI smoke now expects the created webhook route to handle the test
    event;
  - webhook delivery resolves and validates host addresses, then passes the
    selected address to `Net::HTTP.start` via `ipaddr:` while keeping the
    original host for Host/SNI/certificate handling;
  - webhook special/private address ranges now include IPv6 unspecified,
    IPv4-mapped, documentation, and multicast ranges;
  - Telegram actions normalize to custom targets and can be created without a
    chat id; they remain non-deliverable until paired/verified;
  - users are capped at 50 receivers and receivers at 20 actions;
  - `event#test` tags generated events and limits each user to 20 test events
    per rolling hour.
- Follow-up verification:
  - `nix develop .#api -c bash -lc 'bundle exec rspec spec/models/event_route_spec.rb spec/api/resources/event_routing_spec.rb spec/models/tasks/event_delivery_spec.rb'`
    passed: 25 examples, 0 failures.
  - `nix develop .#api -c bash -lc 'bundle exec rspec spec/api/endpoint_coverage_spec.rb spec/api/custom_routes_coverage_spec.rb'`
    passed: 2 examples, 0 failures.
  - `nix develop .#api -c bash -lc 'bundle exec rubocop models/event_route.rb models/notification_receiver.rb models/notification_receiver_action.rb lib/vpsadmin/api/events.rb lib/vpsadmin/api/resources/event.rb lib/vpsadmin/api/resources/event_route.rb lib/vpsadmin/api/tasks/event_delivery.rb spec/api/resources/event_routing_spec.rb spec/models/tasks/event_delivery_spec.rb'`
    passed: 9 files inspected, no offenses.
  - Ruby syntax passed for the changed event/resource/model/task/spec files.
  - `nix develop .#webui -c bash -lc 'php -l pages/page_notifications.php && php -l forms/notifications.forms.php && php -l pages/page_adminm.php'`
    passed.
  - `nix shell nixpkgs#nodejs -c node --check tests/playwright/webui/specs/support-pages.spec.cjs`
    passed.
  - `git diff --check` passed.
  - `./test-runner.sh test 'webui#support-pages'`
    passed: 1 test script successful in 810.04 seconds.
- Final amend:
  - `nix develop -c git commit --amend -F <tmpfile>` passed hooks:
    Nixfmt, PhpCsFixer, and RuboCop.
  - Current `vpsadmin` head is
    `ac7f8a2617ae3e7c440ffd55ee44c03f52c0768f`.
  - Commit-message hook still warns at 72 columns, but all lines are 80
    columns or fewer.
- Dev cluster refreshed:
  - `dev-clusters/vpsadmin/bin/devcluster update 2026-06-15-vpsadmin-events services`
    completed successfully.
  - `dev-clusters/vpsadmin/bin/devcluster status 2026-06-15-vpsadmin-events`
    reports running, topology `single`, network `bridge`, ready `yes`.
  - `curl -k -I --max-time 15 https://webui.aitherdev.int.vpsfree.cz/`
    returned HTTP 200.
  - `curl -k -I --max-time 15 https://api.aitherdev.int.vpsfree.cz/`
    returned HTTP 200.
  - `systemctl is-active` on the services host reported
    `vpsadmin-api-event-webhooks.timer` active, the one-shot webhook service
    inactive after its run, and `vpsadmin-api.service` active.
  - Review URLs:
    - Web UI: `https://webui.aitherdev.int.vpsfree.cz/`
    - API: `https://api.aitherdev.int.vpsfree.cz/`
    - Mailpit: `https://mailpit.aitherdev.int.vpsfree.cz/`
- User reported on 2026-06-16 that the running dev cluster's Notifications
  page was broken. Logs showed the persisted dev database was missing the
  `event_routes` table, so the cluster had stale DB state from an older
  activation where migrations had not run.
- A `devcluster reset 2026-06-15-vpsadmin-events` command was started, but the
  user then asked not to reset and to stop the dev cluster for now. The reset
  completed before it could be interrupted:
  - `cluster 2026-06-15-vpsadmin-events stopped`
  - `cluster 2026-06-15-vpsadmin-events state removed`
- Current cluster status is stopped. Do not restart it until the implementation
  has all intended pieces; skip long integration tests meanwhile.
- Worktrees:
  - `vpsadmin`: clean on `2026-06-15-vpsadmin-events`.
  - `vpsfree-mail-templates`: clean on `2026-06-15-vpsadmin-events`.
  - `vpsfree-cz-configuration`: clean on
    `2026-06-15-vpsadmin-events`.
- Root Overcommit hooks were installed in the `vpsadmin` worktree through the
  repository Nix shell. Ambient `git commit --amend` could not load Overcommit,
  so final commits were made through `nix develop -c git commit ...`.
- Pre-commit hooks passed for the final amend:
  - Nixfmt OK;
  - RuboCop OK;
  - PhpCsFixer OK.
- Commit-message hooks passed. The TextWidth hook warned at 72 columns, but
  all commit-message lines are 80 columns or fewer as required by the
  workspace.
- Final UI/browser smoke:
  `./test-runner.sh test 'webui#support-pages'`
  - Passed: 1 test script successful in 733.8 seconds.
  - The added notification flow creates a receiver, webhook action, route,
    test event, verifies delivery log output, and cleans up the receiver and
    route.
- Follow-up stale-name scan:
  `rg "Notification endpoints|Default endpoint|endpoint_new|endpoint_edit|endpoint_delete|notification_endpoint|NotificationEndpoint|event_rule|EventRule|matched_event_rule|discard rule" api webui tests .github nixos -n`
  - No current implementation references found after replacing the Playwright
    and CI-selection test references.

## Commands run

- `bin/dev-session current`
  - Returned active slug `2026-06-15-vpsadmin-events`.
- `dev-clusters/vpsadmin/bin/devcluster status 2026-06-15-vpsadmin-events`
  - Status: stopped.
- `nix develop .#api -c bash -lc 'ruby -c models/event_route_matcher.rb && ruby -c lib/vpsadmin/api/events.rb && ruby -c lib/vpsadmin/supervisor/node/oom_reports.rb && ruby -c db/migrate/20260615110000_add_events.rb && ruby -c spec/models/event_route_spec.rb && ruby -c spec/supervisor/node/oom_reports_spec.rb'`
  - Ruby syntax checks passed.
- `nix develop .#api -c bash -lc 'bundle exec rspec spec/models/event_route_spec.rb spec/supervisor/node/oom_reports_spec.rb spec/api/resources/event_routing_spec.rb'`
  - Passed: 36 examples, 0 failures.
- `git diff --check`
  - Passed with no whitespace errors.
- `nix develop .#api -c bash -lc 'bundle exec rubocop models/event_route_matcher.rb lib/vpsadmin/api/events.rb lib/vpsadmin/supervisor/node/oom_reports.rb db/migrate/20260615110000_add_events.rb spec/models/event_route_spec.rb spec/supervisor/node/oom_reports_spec.rb'`
  - Passed: 6 files inspected, no offenses.
- `nix develop .#api -c bash -lc 'bundle exec rspec spec/models/notification_receiver_action_spec.rb spec/models/event_route_spec.rb spec/api/resources/event_routing_spec.rb spec/models/tasks/event_delivery_spec.rb spec/models/transaction_chains/incident_report/send_spec.rb spec/models/transaction_chains/incident_report/process_spec.rb spec/models/transaction_chains/incident_report/new_spec.rb spec/models/transaction_chains/vps/oom_reports_spec.rb spec/models/transaction_chains/vps/oom_prevention_spec.rb spec/api/endpoint_coverage_spec.rb spec/api/custom_routes_coverage_spec.rb spec/supervisor/node/oom_reports_spec.rb'`
  - Passed: 81 examples, 0 failures.
- `nix develop .#api -c bash -lc 'RACK_ENV=test VPSADMIN_PLUGINS=none bundle exec ruby /tmp/vpsadmin_events_migration_smoke.rb'`
  - Passed direct `AddEvents#up` migration smoke against a schema-loaded test
    DB with a legacy OOM ignore rule.
  - Verified generated output:
    - route: `OOM report ignore /user.slice/*` for `vps.oom_report`;
    - matchers: `vps_id == 1`, `parameters.cgroup =* /user.slice/*`;
    - receivers: muted `Do not notify` and muted `Ignored OOM reports`.
- `nix develop -c bash -lc 'bundle exec overcommit --sign'`
  - Updated Overcommit signature for the current config.
- `nix develop -c git commit -F /tmp/vpsadmin-events-oom-routes-commit-message.txt`
  - First commit attempt ran hooks successfully but failed because files were
    not staged.
  - After staging the six intended files, hooks passed and commit
    `ffef1f5867ad470ac0e64c63416227713b7c0c12` was created.
- Full historical migration smoke:
  - `nix develop .#api -c bash -lc '... bundle exec rake db:drop db:create db:migrate ...'`
    is blocked before reaching this migration by old migrations inheriting
    bare `ActiveRecord::Migration` under ActiveRecord 8.1.
  - This was treated as a pre-existing migration-stack limitation; see the
    direct `AddEvents#up` smoke above for this slice.

- `bin/dev-session current`
  - Returned active slug `2026-06-15-vpsadmin-events`.
- `git status --short` in `vpsadmin`
  - Dirty with the revised route/receiver/action implementation on top of
    `origin/master`.
- `git diff -- api/Gemfile.lock Gemfile.lock`
  - No lockfile changes from local Bundler/Nix runs.
- `rg "EventRule|event_rule|NotificationEndpoint|notification_endpoint|matched_event_rule|event_rule_action" api webui nixos -n`
  - No stale implementation references found.
- `nix develop .#api -c bash -lc 'bundle exec rspec spec/models/event_route_spec.rb spec/api/resources/event_routing_spec.rb spec/models/tasks/event_delivery_spec.rb'`
  - Passed: 21 examples, 0 failures.
- `nix develop .#api -c bash -lc 'bundle exec rspec spec/api/endpoint_coverage_spec.rb spec/api/custom_routes_coverage_spec.rb'`
  - Passed: 2 examples, 0 failures.
- `nix develop .#api -c bash -lc 'ruby -c lib/vpsadmin/api/tasks/event_delivery.rb && ruby -c models/event_route.rb && ruby -c models/user.rb && ruby -c spec/models/tasks/event_delivery_spec.rb'`
  - Ruby syntax checks passed.
- `nix develop .#api -c bash -lc 'bundle exec rubocop models/event_route.rb models/user.rb lib/vpsadmin/api/tasks/event_delivery.rb spec/models/event_route_spec.rb spec/api/resources/event_routing_spec.rb spec/models/tasks/event_delivery_spec.rb'`
  - First run found one empty-line offense in
    `lib/vpsadmin/api/tasks/event_delivery.rb`; fixed.
  - Final run passed: 6 files inspected, no offenses.
- `nix develop .#webui -c bash -lc 'php -l pages/page_notifications.php && php -l forms/notifications.forms.php && php -l pages/page_adminm.php'`
  - PHP syntax checks passed.
- `git diff --check`
  - Passed with no whitespace errors.
- `git status --short --branch` in `vpsfree-mail-templates` and
  `vpsfree-cz-configuration`
  - Both worktrees are clean on branch `2026-06-15-vpsadmin-events`.

Earlier command history:

- `bin/dev-session current`
  - Returned active slug `2026-06-15-vpsadmin-events`.
- `ls -la work/2026-06-15-vpsadmin-events`
  - Existing placeholder `plan.md` and `state.md`.
- `find worktrees/2026-06-15-vpsadmin-events -maxdepth 2 -type d -print`
  - Initially no repository worktrees.
- `sed -n ... work/2026-06-14-vpsadmin-incident-filtering/{plan,state}.md`
  - Reviewed prior incident filtering implementation and decisions.
- `bin/dev-session worktree add 2026-06-15-vpsadmin-events vpsadmin --as-is --base 2026-06-14-vpsadmin-incident-filtering`
  - Worktree created.
  - Command exited non-zero because the checkout hook could not load
    Overcommit from the ambient shell.
- `bin/dev-session worktree add 2026-06-15-vpsadmin-events vpsfree-mail-templates --as-is --base 2026-06-14-vpsadmin-incident-filtering`
  - Worktree created successfully.
- `bin/dev-session worktree add 2026-06-15-vpsadmin-events vpsfree-cz-configuration --as-is --base 2026-06-14-vpsadmin-incident-filtering`
  - Worktree created.
  - Command exited non-zero because the checkout hook could not load the
    repository's pinned Bundler gems from the ambient shell.
- `git status --short --branch`, `git remote -v`, `git rev-parse HEAD`
  - Verified clean prepared branches and SSH remotes.
- `rg --files -g 'AGENTS.md'` and `sed -n ... AGENTS.md`
  - Read repository-local instructions.
- `rg`/`find`/`sed` inspections in `vpsadmin`
  - Mail templates, `MailTemplate`, user mail recipient models/resources,
    OOM rules, incident report rules, event-like transaction chains, mail log,
    monitoring/outage/security advisory paths.
- `rg`/`find` inspections in `vpsfree-mail-templates`
  - Template directories, `meta.rb` labels/subjects, user visibility flags.
- `rg`/`sed` inspections in `vpsfree-cz-configuration`
  - vpsAdmin API config, abuse notice parser config, monitoring definitions,
    Telegram Alertmanager configuration, and production API module settings.
- `ruby -c` on new event migration, models, registry/router, and resources
  - Syntax checks passed.
- `nix develop .#api -c bundle exec rspec spec/models/event_rule_spec.rb`
  - Passed: 5 examples, 0 failures.
- `nix develop .#api -c bundle exec rspec spec/api/resources/event_routing_spec.rb`
  - Passed: 5 examples, 0 failures.
- `nix develop .#api -c bundle exec rspec spec/models/event_rule_spec.rb spec/api/resources/event_routing_spec.rb`
  - Passed: 10 examples, 0 failures.
- `nix develop .#api -c bundle exec rspec spec/api/endpoint_coverage_spec.rb spec/api/custom_routes_coverage_spec.rb`
  - Passed: 2 examples, 0 failures.
- `git status --short` in the `vpsadmin` worktree
  - Clean after amending commit `dd9acccf62c54a77baffa377bd72b11d89f322db`.
- `dev-clusters/vpsadmin/bin/devcluster update 2026-06-15-vpsadmin-events services`
  - Completed successfully after rebuilding and activating the updated
    services closure from the amended vpsAdmin worktree.
- `dev-clusters/vpsadmin/bin/devcluster status 2026-06-15-vpsadmin-events`
  - Status: running, topology `single`, network `bridge`, ready `yes`.
- `curl -k -I --max-time 15 https://webui.aitherdev.int.vpsfree.cz/`
  - Returned HTTP 200 after the services update.
- `curl -k -I --max-time 15 https://api.aitherdev.int.vpsfree.cz/`
  - Returned HTTP 200 after the services update.
- `dev-clusters/vpsadmin/bin/devcluster ssh 2026-06-15-vpsadmin-events node1 -- sv status osctld nodectld`
  - Both services are running after the services update.
- `nix develop .#api -c bundle exec rubocop ...`
  - First run failed because paths were prefixed with `api/`; the API dev
    shell already starts in `api`, so RuboCop looked for `api/api/...`.
  - Reran with paths relative to the API shell; fixed two alignment offenses.
  - Final run passed: 13 files inspected, no offenses.
- `nix develop .#api -c bundle exec rspec spec/models/incident_report_rule_spec.rb spec/api/resources/incident_report_rule_spec.rb`
  - Passed: 21 examples, 0 failures.
- `dev-clusters/vpsadmin/bin/devcluster start 2026-06-15-vpsadmin-events --topology single --network bridge`
  - Started the dev cluster using the feature `vpsadmin` worktree as input.
  - The runner is active under PID recorded in
    `.dev-clusters/vpsadmin/clusters/2026-06-15-vpsadmin-events/runner.pid`.
  - The initial start command exited non-zero after API/WebUI readiness while
    preparing `node1`, because `/run/osctl/osctld.sock` was not present yet.
    `node1` finished booting shortly afterwards and `osctld` started.
- `dev-clusters/vpsadmin/bin/devcluster update 2026-06-15-vpsadmin-events node1`
  - Reran node activation after `osctld` was up; completed successfully.
- `dev-clusters/vpsadmin/bin/devcluster status 2026-06-15-vpsadmin-events`
  - Status: running, topology `single`, network `bridge`.
- `dev-clusters/vpsadmin/bin/devcluster ssh 2026-06-15-vpsadmin-events node1 -- sv status osctld nodectld`
  - Both services are running.
- `dev-clusters/vpsadmin/bin/devcluster urls 2026-06-15-vpsadmin-events`
  - Listed review URLs and seeded credentials.
- `curl -k -I --max-time 10 https://api.aitherdev.int.vpsfree.cz/`
  - Returned HTTP 200.
- `curl -k -I --max-time 10 https://webui.aitherdev.int.vpsfree.cz/`
  - Returned HTTP 200.
- User correction on 2026-06-16:
  - stopped the old dev cluster;
  - stashed local work;
  - reset `vpsadmin` branch `2026-06-15-vpsadmin-events` to `origin/master`
    (`f3e1ff0d099d742b72831e881e53c27ee90a337c`);
  - reapplied the event-system work and resolved conflicts without keeping
    the incident-filtering branch commits;
  - reset the unused `vpsfree-mail-templates` and
    `vpsfree-cz-configuration` initiative branches to their `origin/master`
    heads.
- `nix develop .#api -c bundle exec rspec spec/models/event_rule_spec.rb spec/api/resources/event_routing_spec.rb spec/api/endpoint_coverage_spec.rb spec/api/custom_routes_coverage_spec.rb`
  - Passed: 14 examples, 0 failures.
- `nix develop .#webui -c bash -lc 'pwd; php -l forms/notifications.forms.php; php -l pages/page_notifications.php; php -l public/index.php'`
  - PHP syntax passed for the new notifications forms/page and changed
    `public/index.php`.
- `nix develop .#api -c bundle exec rubocop ...`
  - Passed: 15 touched API files inspected, no offenses.
- `nix develop -c ruby tests/ci-selection-test.rb`
  - Passed: 15 runs, 54 assertions, 0 failures.
- `printf ... | nix develop -c ruby tools/select_ci_tests.rb`
  - Selected support/alerts WebUI CI tags for the new notification/event
    runtime paths.
- `./test-runner.sh ls --filter 'tag=ci && (tag=alerts || tag=monitoring || tag=support || tag=webui-security-advisories || tag=webui-support-pages)'`
  - Resolved expected scripts including `webui#support-pages`.
- `nix shell nixpkgs#nodejs -c node --check tests/playwright/webui/specs/support-pages.spec.cjs`
  - JavaScript syntax passed.
- `./test-runner.sh test 'webui#support-pages'`
  - First two reruns exposed test issues in the newly added notification
    smoke (sidebar assertion and missing helper import).
  - Third rerun exposed a confirm-dialog test cleanup issue.
  - Final rerun passed: 1 test script successful; the Playwright example
    covered 9 support/status browser tests including the new notifications
    flow.
- `dev-clusters/vpsadmin/bin/devcluster start 2026-06-15-vpsadmin-events --topology single --network bridge`
  - Cluster started on the bridge network using the corrected vpsAdmin
    worktree.
  - The command exited non-zero during post-start `node1` preparation because
    `/run/osctl/osctld.sock` was not ready yet. The cluster itself reported
    `ready: yes`.
- `dev-clusters/vpsadmin/bin/devcluster update 2026-06-15-vpsadmin-events node1`
  - Completed node activation successfully after `osctld` was up.
- `dev-clusters/vpsadmin/bin/devcluster status 2026-06-15-vpsadmin-events`
  - Status: running, topology `single`, network `bridge`, ready `yes`.
- `dev-clusters/vpsadmin/bin/devcluster ssh 2026-06-15-vpsadmin-events node1 -- sv status osctld nodectld`
  - Both services are running.
- `curl -k -I --max-time 10 https://webui.aitherdev.int.vpsfree.cz/`
  - Returned HTTP 200.
- `curl -k -I --max-time 10 https://api.aitherdev.int.vpsfree.cz/`
  - Returned HTTP 200.
- `dev-clusters/vpsadmin/bin/devcluster urls 2026-06-15-vpsadmin-events`
  - Review URLs:
    - Web UI: `https://webui.aitherdev.int.vpsfree.cz/`
    - API: `https://api.aitherdev.int.vpsfree.cz/`
    - Mailpit: `https://mailpit.aitherdev.int.vpsfree.cz/`
  - Seeded credentials:
    - Admin: `test-admin` / `testAdminPassword`
    - User 1: `test-user1` / `testUser1Password`
    - User 2: `test-user2` / `testUser2Password`
- Mandatory change review by standalone agent
  `019ecf62-79db-7f73-a582-7b1e19b15e78`
  - Blocking findings: none.
  - Important findings fixed:
    - `Events.emit!` now rejects a supplied `user` and `vps` when the VPS
      owner differs from the event user.
    - A suppressing discard rule is now stored as `matched_event_rule`, so
      event-log filters and hit context point at the rule that made the
      terminal decision.
    - `Event` now validates summary length and JSON-object parameter shape
      and size; `event#test` rejects oversized parameter JSON before parsing.
  - Advisory findings deferred:
    - webhook SSRF policy before enabling real webhook delivery;
    - Telegram pairing token expiry/single-use fields before bot consumption.
- `nix develop .#api -c bundle exec rspec spec/models/event_rule_spec.rb spec/api/resources/event_routing_spec.rb`
  - Passed: 16 examples, 0 failures.
- `nix develop .#api -c ruby -c models/event.rb`
  - Syntax OK.
- `nix develop .#api -c ruby -c lib/vpsadmin/api/events.rb`
  - Syntax OK.
- `nix develop .#api -c ruby -c lib/vpsadmin/api/resources/event.rb`
  - Syntax OK.
- `nix develop .#api -c bundle exec rubocop models/event.rb lib/vpsadmin/api/events.rb lib/vpsadmin/api/resources/event.rb spec/models/event_rule_spec.rb spec/api/resources/event_routing_spec.rb`
  - Passed: 5 files inspected, no offenses.
- `nix develop .#api -c bundle exec rspec spec/api/endpoint_coverage_spec.rb spec/api/custom_routes_coverage_spec.rb`
  - Passed: 2 examples, 0 failures.

## 2026-06-16 OOM review amend

- `git status --short` in `vpsadmin`
  - Clean after amend.
- `nix develop .#webui -c bash -lc 'php -l pages/page_oom_reports.php && php -l forms/oom_reports.forms.php && php -l forms/vps.forms.php'`
  - PHP syntax checks passed.
- `nix develop .#api -c bash -lc 'ruby -c lib/vpsadmin/api/events.rb && ruby -c lib/vpsadmin/supervisor/node/oom_reports.rb && ruby -c lib/vpsadmin/api/resources/oom_report_rule.rb && ruby -c spec/supervisor/node/oom_reports_spec.rb && ruby -c spec/api/resources/oom_report_rule_spec.rb'`
  - Ruby syntax checks passed.
- `nix develop .#api -c bash -lc 'bundle exec rubocop lib/vpsadmin/api/events.rb lib/vpsadmin/supervisor/node/oom_reports.rb lib/vpsadmin/api/resources/oom_report_rule.rb spec/supervisor/node/oom_reports_spec.rb spec/api/resources/oom_report_rule_spec.rb'`
  - Passed: 5 files inspected, no offenses.
- `git diff --check`
  - Passed with no whitespace errors.
- `nix develop .#api -c bash -lc 'bundle exec rspec spec/supervisor/node/oom_reports_spec.rb spec/api/resources/oom_report_rule_spec.rb spec/api/resources/lifecycle_bypass_spec.rb'`
  - Passed: 60 examples, 0 failures.
- `nix develop .#api -c bash -lc 'bundle exec rspec spec/models/notification_receiver_action_spec.rb spec/models/event_route_spec.rb spec/api/resources/event_routing_spec.rb spec/models/tasks/event_delivery_spec.rb spec/models/transaction_chains/incident_report/send_spec.rb spec/models/transaction_chains/incident_report/process_spec.rb spec/models/transaction_chains/incident_report/new_spec.rb spec/models/transaction_chains/vps/oom_reports_spec.rb spec/models/transaction_chains/vps/oom_prevention_spec.rb spec/api/endpoint_coverage_spec.rb spec/api/custom_routes_coverage_spec.rb spec/supervisor/node/oom_reports_spec.rb spec/api/resources/oom_report_rule_spec.rb spec/api/resources/lifecycle_bypass_spec.rb'`
  - Passed: 131 examples, 0 failures.
- `nix develop -c git commit --amend -F /tmp/vpsadmin-oom-route-commit-message`
  - Passed hooks: Nixfmt, PhpCsFixer, and RuboCop.
  - Commit-message hook warned at 72 columns, but all lines are 80 columns or
    fewer.
  - New `vpsadmin` head:
    `2f4f2bbfbcfa16f8f8694bd3ab6c72946d08466b`
    (`notifications: route OOM report suppression`).
- Final OOM review fix:
  - `nix develop .#api -c bash -lc 'ruby -c lib/vpsadmin/api/events.rb && ruby -c spec/supervisor/node/oom_reports_spec.rb'`
    passed.
  - `nix develop .#api -c bash -lc 'bundle exec rubocop lib/vpsadmin/api/events.rb spec/supervisor/node/oom_reports_spec.rb'`
    passed: 2 files inspected, no offenses.
  - `git diff --check` passed.
  - `nix develop .#api -c bash -lc 'bundle exec rspec spec/supervisor/node/oom_reports_spec.rb spec/api/resources/oom_report_rule_spec.rb spec/api/resources/lifecycle_bypass_spec.rb'`
    passed: 61 examples, 0 failures.
  - `nix develop .#api -c bash -lc 'bundle exec rspec spec/models/notification_receiver_action_spec.rb spec/models/event_route_spec.rb spec/api/resources/event_routing_spec.rb spec/models/tasks/event_delivery_spec.rb spec/models/transaction_chains/incident_report/send_spec.rb spec/models/transaction_chains/incident_report/process_spec.rb spec/models/transaction_chains/incident_report/new_spec.rb spec/models/transaction_chains/vps/oom_reports_spec.rb spec/models/transaction_chains/vps/oom_prevention_spec.rb spec/api/endpoint_coverage_spec.rb spec/api/custom_routes_coverage_spec.rb spec/supervisor/node/oom_reports_spec.rb spec/api/resources/oom_report_rule_spec.rb spec/api/resources/lifecycle_bypass_spec.rb'`
    passed: 132 examples, 0 failures.
  - `nix develop -c git commit --amend -F /tmp/vpsadmin-oom-route-commit-message`
    passed hooks: Nixfmt, PhpCsFixer, and RuboCop; TextWidth warned at 72
    columns, but all commit-message lines are 80 columns or fewer.
  - Current `vpsadmin` head:
    `56f2876b67c9792563de8e9f90870e6a57fb6e14`.
- OOM event stage split committed on 2026-06-17:
  - commit `7dbced6968daebe22ea362c309896292934d3c3e`
    (`notifications: distinguish raw OOM route events`);
  - raw supervisor-side OOM planning now emits `parameters.stage = raw`;
  - user-facing OOM notification summaries now emit
    `parameters.stage = notification`;
  - migrated legacy OOM ignore routes match `parameters.stage == raw` so
    notification e-mail routes can target `vps.oom_report` later without
    suppressing raw report ingestion;
  - event type metadata exposes `parameters.stage` for OOM matching;
  - regression coverage verifies that raw ignore routes do not match
    notification-stage OOM events.
- OOM event stage verification:
  - syntax/RuboCop/whitespace verification passed for the changed Ruby and
    spec files before commit;
  - focused OOM/event routing specs passed: 47 examples, 0 failures;
  - direct migration smoke passed by schema-loading a test DB, creating a
    legacy OOM ignore rule, running `AddEvents#up`, and verifying matchers
    `vps_id == <id>`, `parameters.stage == raw`, and
    `parameters.cgroup =* /user.slice/*`;
  - `git diff --check` passed;
  - broader notification/OOM quick suite passed: 133 examples, 0 failures;
  - `nix develop -c git commit -F /tmp/vpsadmin_events_oom_stage_commit.txt`
    passed hooks: Nixfmt and RuboCop; TextWidth warned at 72 columns, but all
    commit-message lines are 80 columns or fewer.
- Advanced e-mail migration slice committed on 2026-06-17:
  - commit `f3113a8e6b1f6e4a676ea820597ddf0729fd8af6`
    (`notifications: migrate advanced e-mail settings`);
  - the events migration now backfills event-backed
    `user_mail_template_recipients` and `user_mail_role_recipients` into
    explicit notification receivers and event routes;
  - template-specific overrides are positioned before role overrides so
    disabled/custom template settings keep the old precedence;
  - `vps_oom_report` advanced-mail routes match
    `parameters.stage == notification`, keeping them separate from raw OOM
    ingestion/suppression routes;
  - users with `mailer_enabled = false` keep the generated muted default route
    and do not receive custom advanced-mail delivery routes during migration;
  - legacy advanced-mail tables and APIs remain for rollback and remaining
    direct-mail call sites.
- Advanced e-mail verification:
  - Ruby syntax passed for `db/migrate/20260615110000_add_events.rb` and
    `spec/models/event_route_spec.rb`;
  - RuboCop passed for the changed migration and spec files;
  - `git diff --check` passed;
  - focused `spec/models/event_route_spec.rb` passed: 16 examples, 0 failures;
  - broader notification/OOM/legacy mail API quick suite passed:
    180 examples, 0 failures;
  - direct migration smoke passed by schema-loading a test DB, seeding one
    custom incident template recipient, one disabled OOM template recipient,
    one admin role recipient, and one legacy raw OOM ignore rule, then running
    `AddEvents#up` after dropping only the event/notification tables and
    verifying generated routes/matchers/actions.
  - `nix develop -c git commit -F /tmp/vpsadmin_events_advanced_mail_commit.txt`
    passed hooks: Nixfmt and RuboCop; TextWidth warned at 72 columns, but all
    commit-message lines are 80 columns or fewer.

## Results

- `vpsadmin` current mail delivery is centered on
  `MailTemplate.send_mail!`, `MailLog`, and `TransactionChain#mail`.
- User mail customization currently has:
  - `users.mailer_enabled`;
  - `users.enable_new_login_notification`;
  - `user_mail_role_recipients`;
  - `user_mail_template_recipients`.
- The incident-filtering branch already added a richer rule model:
  ordered user rules, matchers, recipients, ignore/report action, custom
  e-mail recipients, and WebUI management.
- OOM report rules are narrower:
  per-VPS `cgroup_pattern` with `notify` or `ignore`.
- Production monitoring config sends many user alert mails from configurable
  Ruby action blocks. Some actions also have side effects, e.g. zombie-process
  restart scheduling, so a generalized event system must route notifications
  without swallowing those side effects.
- Production configuration already uses Telegram for Alertmanager team alerts,
  but vpsAdmin does not have per-user Telegram receiver actions wired to a bot
  yet.
- The proposed design is in
  `/home/aither/workspace/ai/vpsfree.cz/work/2026-06-15-vpsadmin-events/plan.md`.
- Current implementation is a routing/logging/UI foundation with routed e-mail
  delivery and the first real webhook worker. Webhook deliveries are queued
  and retryable; Telegram deliveries are still persisted as planned/skipped
  rows until the adapter is implemented.
- Route evaluation is nested and receiver-based. Matching routes choose a
  receiver; muted receivers suppress delivery. `continue = true` adds matching
  sibling routes at the same level, which keeps additive fan-out visible to
  users without a separate discard decision.
- The event log records `matched_event_route_id`, so filtering by route shows
  events for which that route or its selected subtree made the routing
  decision.

## Open questions

- Should any event types be mandatory and non-discardable?
- V1 keeps `continue = false` by default. `continue = true` is useful for
  additive routes. If users need a more explicit exception model later, it
  should be designed as a route/receiver concept rather than restoring hidden
  discard decisions.
- Where should non-email action templates live long term?
- Should admin/system notifications be configurable now or later?
- Should Telegram include full incident bodies or default to summaries and
  vpsAdmin links?
- Before any commits in `vpsadmin` or `vpsfree-cz-configuration`, enter the
  repository Nix shell and verify hook setup. Ambient shell checkout hooks
  reported missing Overcommit/Bundler gems.

## Cleanup

- No cleanup needed yet.
- Worktrees should remain until the design is reviewed and either implemented
  or abandoned.
- Dev cluster is currently stopped, per user request. Do not restart it until
  the implementation has all intended pieces.

## 2026-06-17 incident reply slice

- `vpsadmin` commit `8c1e25120015232ba63e77249693e7426ddf70b8`
  (`notifications: route incident reply mails`).
- Converted `TransactionChains::IncidentReport::Reply` from a direct
  `mail_custom` call to event `incident_report.reply`.
- Added a narrow direct custom e-mail delivery path for nil-user events whose
  target recipient is carried in event parameters.
- Preserved the existing incident reply sender, recipient, subject, plain-text
  body, `In-Reply-To`, and `References` headers when queued by the event
  delivery worker.
- Scoped incident reply `from`, body and threading parameter rendering to this
  direct nil-user delivery path so user-routed/test events cannot spoof custom
  mail headers.
- Added a reply-chain guard that raises when the event e-mail delivery was
  marked failed while being queued, matching the existing active incident
  report mail behavior.
- Added event type metadata for incident reply parameters so the event log and
  routing UI can expose the available fields.
- Verification:
  - Ruby syntax passed for touched files;
  - focused incident reply/event delivery specs passed: 26 examples,
    0 failures;
  - broader incident send/reply/event delivery/event routing quick suite
    passed: 44 examples, 0 failures;
  - RuboCop passed for the touched files;
  - `git diff --check` passed;
  - `ruby tests/ci-selection-test.rb` passed: 15 runs, 54 assertions,
    0 failures;
  - pre-commit hooks passed: Nixfmt and RuboCop; commit-msg TextWidth warned
    at 72 columns, but all commit-message lines are 80 columns or fewer.
- Mandatory review by `Plato` on pre-amend commit
  `717dfee23a3d546f28b688ca8ce1cca7593ef373` found:
  - blocking: user-routed/test `incident_report.reply` events could spoof
    custom-mail sender/threading/body parameters;
  - important: direct incident reply delivery render failures were recorded as
    failed delivery rows without failing the reply chain.
  Both findings were fixed before amending to commit
  `8c1e25120015232ba63e77249693e7426ddf70b8`.
- Mandatory review by `Gibbs` on amended commit
  `8c1e25120015232ba63e77249693e7426ddf70b8` found no blocking,
  important, or advisory findings. Reviewer also ran the focused
  incident-reply/event-delivery specs: 26 examples, 0 failures.
- Note: running multiple Ruby/Bundler checks concurrently against the same
  worktree `.gems` directory can race while `nix develop` installs Bundler.
  Avoid parallel Bundler-backed commands in this worktree.

## 2026-06-17 system report mail slice

- `vpsadmin` commit `7696c254f542af85c4657043c87c4c6fed21aeeb`
  (`notifications: route report mails`).
- Converted scheduled daily reports and payments overviews from direct
  `TransactionChain#mail` calls to nil-user events:
  - `system.daily_report`;
  - `payments.overview`.
- These report events use direct system-template e-mail deliveries so existing
  template recipients, template names, language selection, and mail-log
  tracking are preserved.
- User-created/user-routed `system.daily_report` events are intentionally not
  treated as direct system-template mails; they render as generic custom event
  e-mails through configured receiver actions.
- Runtime template variables are preserved across `Event#lock!` and
  `EventDelivery#lock!` reloads for immediate in-chain delivery. This keeps
  report hook payloads available to `MailTemplate.send_mail!` without trying
  to persist heavyweight ActiveRecord relations in event parameters.
- Verification before commit:
  - Ruby syntax passed for touched report/event files;
  - focused report/event-delivery specs passed: 31 examples, 0 failures;
  - RuboCop passed for 9 touched API files;
  - broader nearby report/mail/payment/routing quick suite passed:
    60 examples, 0 failures;
  - `git diff --check` passed;
  - `ruby tests/ci-selection-test.rb` passed: 15 runs, 54 assertions,
    0 failures.
- Commit hooks passed in `nix develop -c git commit -F
  /tmp/vpsadmin_events_report_mails_commit.txt`: Nixfmt, RuboCop,
  TrailingPeriod, SingleLineSubject, and TextWidth.
- Mandatory review by `Dalton` on commit
  `7696c254f542af85c4657043c87c4c6fed21aeeb` found no blocking,
  important, or advisory findings. Reviewer also reran the focused
  report/event-delivery specs: 31 examples, 0 failures.

## 2026-06-17 Telegram delivery worker slice

- `vpsadmin` commit `75ff055130524a64e0c057f16f04fb156da606c3`
  (`notifications: deliver Telegram events`).
- Added `VpsAdmin::API::Tasks::EventDelivery#deliver_telegrams`, which picks
  due `telegram` event deliveries, claims them with a stale-worker timeout,
  posts plain-text messages to Telegram Bot API `sendMessage`, and records
  delivery state, attempts, response status/body, provider message id, and
  error summaries in `event_deliveries`.
- Added rake task `vpsadmin:event_delivery:telegrams`.
- Telegram delivery uses:
  - `VPSADMIN_TELEGRAM_BOT_TOKEN` for the bot token;
  - optional `VPSADMIN_TELEGRAM_API_URL`, defaulting to
    `https://api.telegram.org`.
- The worker deliberately sends plain text without parse mode. The generic
  Telegram body includes only severity, subject, event type, and VPS context;
  it omits summaries and arbitrary event parameters until explicit Telegram
  templates or safe allowlists exist. Per-action notification templates remain
  a later slice.
- This slice only sends to already linked and verified Telegram receiver
  actions. Bot webhook/polling update handling for pairing tokens is still a
  follow-up.
- Verification before commit:
  - Ruby syntax passed for touched Telegram task/rake/spec files;
  - focused event-delivery specs passed: 31 examples, 0 failures;
  - RuboCop passed for 3 touched files;
  - combined event-delivery and event-routing quick specs passed:
    46 examples, 0 failures;
  - `git diff --check` passed;
  - `ruby tests/ci-selection-test.rb` passed: 15 runs, 54 assertions,
    0 failures.
- Commit hooks passed in `nix develop -c git commit -F
  /tmp/vpsadmin_events_telegram_commit.txt`: Nixfmt, RuboCop,
  TrailingPeriod, SingleLineSubject, and TextWidth (warning only at
  72 columns; all lines remain within the workspace 80-column rule).
- Mandatory review by `Gauss` on pre-amend commit
  `0ced629bebb975521441fa4e9b1734edd417d6a3` found no blocking findings and
  one important finding: the initial default Telegram text included all event
  parameters, including sensitive incident report bodies.
- Review follow-up:
  - amended the commit so default Telegram messages omit event parameters
    entirely until explicit Telegram templates or safe allowlists exist;
  - added a regression spec asserting that `note` and sensitive `text`
    parameters are not sent in Telegram fallback messages;
  - corrected the previously mistyped full commit hash in this state file.
- Post-review verification before amending:
  - Ruby syntax passed for touched Telegram task/spec files;
  - focused event-delivery specs passed: 31 examples, 0 failures;
  - RuboCop passed for 2 touched files;
  - combined event-delivery and event-routing quick specs passed:
    46 examples, 0 failures;
  - `git diff --check` passed;
  - `ruby tests/ci-selection-test.rb` passed: 15 runs, 54 assertions,
    0 failures.
- Commit amend hooks passed in `nix develop -c git commit --amend -F
  /tmp/vpsadmin_events_telegram_commit.txt`: Nixfmt, RuboCop,
  TrailingPeriod, SingleLineSubject, and TextWidth (warning only at
  72 columns; all lines remain within the workspace 80-column rule).
- Follow-up mandatory review by `Sagan` on commit
  `d56f59e54fd4bacce2e6b7c2b8c3c882771d4c6c` found no blocking findings and
  one important finding: incident report body text could still leak through
  `event.summary`, because incident reports use the report body as summary.
- Second review follow-up:
  - amended the commit so default Telegram messages omit summaries as well as
    event parameters;
  - strengthened the regression spec so the sensitive string is present in
    both `summary` and `parameters[:text]` and absent from the sent Telegram
    text.
- Second post-review verification before amending:
  - Ruby syntax passed for touched Telegram task/spec files;
  - focused event-delivery specs passed: 31 examples, 0 failures;
  - RuboCop passed for 2 touched files;
  - combined event-delivery and event-routing quick specs passed:
    46 examples, 0 failures;
  - `git diff --check` passed;
  - `ruby tests/ci-selection-test.rb` passed: 15 runs, 54 assertions,
    0 failures.
- Second commit amend hooks passed in `nix develop -c git commit --amend -F
  /tmp/vpsadmin_events_telegram_commit.txt`: Nixfmt, RuboCop,
  TrailingPeriod, SingleLineSubject, and TextWidth (warning only at
  72 columns; all lines remain within the workspace 80-column rule).
- Final follow-up mandatory review by `Parfit` on commit
  `75ff055130524a64e0c057f16f04fb156da606c3` found no blocking, important,
  or advisory findings. Reviewer confirmed the formatter no longer reads
  `event.summary` or `event.parameters`, and reran:
  - `git diff --check 7696c254..75ff055`: passed;
  - focused event-delivery specs: 31 examples, 0 failures.

## 2026-06-17 Telegram pairing worker slice

- `vpsadmin` commit `1d7b99732b821af6ec0cbf1d53d7aed642736ddc`
  (`notifications: pair Telegram receiver actions`).
- Added shared `VpsAdmin::API::TelegramBot` HTTP helper and switched Telegram
  delivery to use it.
- Added `VpsAdmin::API::Tasks::Telegram#poll_pairing_updates`, exposed as
  rake task `vpsadmin:telegram:poll_pairing_updates`.
- The polling task calls Bot API `getUpdates`, persists a durable update
  offset in `sysconfig` as `notifications/telegram_update_offset`, and pairs
  pending Telegram receiver actions from private `/start <token>` messages.
- Pairing writes the private chat id to `target_value`, marks the action
  verified, clears the verification token, and clears previous errors.
- Pairing attempts from groups/channels are rejected, rotate the now-exposed
  token, and store a visible `last_error`. Unknown tokens and non-command
  messages are ignored while still advancing the Telegram offset after a
  successful poll.
- Telegram receiver actions now clear verification when their target/action
  fields are edited outside the bot pairing path. Existing planned deliveries
  still use their snapshotted, previously verified chat id when the later edit
  changed the live target.
- The web UI receiver action table now shows pending Telegram `/start <token>`
  commands and the last pairing error next to the verified icon.
- Operational note: avoid concurrent `nix develop`/Bundler commands in this
  worktree. An attempted parallel check hit the known shared `.gems` race again;
  subsequent verification was run sequentially.
- Verification before commit:
  - Ruby/PHP syntax passed for touched Telegram task/client/rake/spec/UI files;
  - focused Telegram pairing specs passed: 5 examples, 0 failures;
  - combined delivery and Telegram pairing specs passed:
    36 examples, 0 failures;
  - RuboCop passed for touched API files;
  - broader delivery, Telegram pairing, and event-routing quick specs passed:
    51 examples, 0 failures;
  - `git diff --check` passed;
  - `ruby tests/ci-selection-test.rb` passed: 15 runs, 54 assertions,
    0 failures.
- Commit hooks passed in `nix develop -c git commit -F
  /tmp/vpsadmin_events_telegram_pairing_commit.txt`: Nixfmt,
  PhpCsFixer, RuboCop, TrailingPeriod, SingleLineSubject, and TextWidth
  (warning only at 72 columns; all lines remain within the workspace
  80-column rule).
- Mandatory review by `Fermat` on pre-amend commit
  `8291b0b887b6c34bd35ed511495c90afd2d0016b` found no blocking findings,
  two important findings, and one advisory finding:
  - verified Telegram targets could be edited afterward without clearing
    verification;
  - group/channel `/start <token>` attempts left a disclosed token usable;
  - the full commit hash recorded in this state file and review packet was
    wrong.
- Review follow-up:
  - added model-level Telegram pairing methods so the bot worker is the only
    path that can set a verified chat target;
  - direct Telegram target/action edits now clear verification and create a
    fresh pairing token;
  - group/channel pairing attempts now rotate the token while preserving the
    visible `last_error`;
  - Telegram delivery preserves already-planned delivery snapshots when a later
    target edit changed the live target, while still canceling deliveries for
    actions that are simply unverified.
- Post-review verification before amending:
  - Ruby syntax passed for touched Telegram delivery/task/model files and specs;
  - focused receiver-action and Telegram pairing specs passed:
    9 examples, 0 failures;
  - focused delivery, Telegram pairing, and receiver-action specs passed:
    40 examples, 0 failures;
  - broader delivery, Telegram pairing, event-routing, and receiver-action
    quick specs passed: 55 examples, 0 failures;
  - RuboCop passed for 6 touched API files;
  - `git diff --check` passed;
  - `ruby tests/ci-selection-test.rb` passed: 15 runs, 54 assertions,
    0 failures.
- Commit amend hooks passed in `nix develop -c git commit --amend -F
  /tmp/vpsadmin_events_telegram_pairing_commit.txt`: Nixfmt, PhpCsFixer,
  RuboCop, TrailingPeriod, SingleLineSubject, and TextWidth (warning only at
  72 columns; all lines remain within the workspace 80-column rule).
- Follow-up mandatory review by `Descartes` on commit
  `ce800a8522784a794072915a36afe5fd0c711ffa` found no blocking findings, one
  important finding, and one advisory finding:
  - `getUpdates` allowed long-poll timeouts up to 50 seconds but the shared
    Telegram HTTP helper always used a 15-second read timeout;
  - pending pairing tokens were high entropy and single-use, but otherwise
    remained redeemable indefinitely.
- Second review follow-up:
  - `TelegramBot#post_json` now accepts per-call HTTP timeouts;
  - Telegram `getUpdates` uses a read timeout of at least 15 seconds and at
    least five seconds longer than the configured long-poll timeout;
  - pending Telegram verification tokens expire after 24 hours using existing
    timestamps, and the poller rotates expired tokens with a visible
    `last_error`;
  - Telegram delivery now passes its `sendMessage` payload as an explicit hash
    to avoid Ruby keyword argument ambiguity after the timeout change.
- Second post-review verification before amending:
  - Ruby syntax passed for touched Telegram helper/task/model/delivery files
    and specs;
  - focused Telegram pairing and receiver-action specs passed:
    12 examples, 0 failures;
  - focused delivery, Telegram pairing, and receiver-action specs passed:
    43 examples, 0 failures;
  - broader delivery, Telegram pairing, event-routing, and receiver-action
    quick specs passed: 58 examples, 0 failures;
  - RuboCop passed for 5 touched API files;
  - `git diff --check` passed;
  - `ruby tests/ci-selection-test.rb` passed: 15 runs, 54 assertions,
    0 failures.
- Second commit amend hooks passed in `nix develop -c git commit --amend -F
  /tmp/vpsadmin_events_telegram_pairing_commit.txt`: Nixfmt, PhpCsFixer,
  RuboCop, TrailingPeriod, SingleLineSubject, and TextWidth (warning only at
  72 columns; all lines remain within the workspace 80-column rule).
- Final follow-up mandatory review by `Meitner` on commit
  `1d7b99732b821af6ec0cbf1d53d7aed642736ddc` found no blocking, important,
  or advisory findings. Reviewer specifically checked that:
  - Telegram target/action edits clear verification;
  - group and expired-token attempts rotate tokens;
  - `getUpdates` read timeout stays above the long-poll timeout;
  - planned Telegram deliveries keep only the intended snapshotted-chat
    behavior.
- Residual gaps called out by the reviewer: no live Telegram Bot API or
  webhook-mode integration coverage, no browser-level UI rendering test for
  token/error display, and concurrent update consumers remain an operational
  constraint rather than being enforced by the worker.

## 2026-06-16 - Telegram worker deployment wiring

- In progress in `vpsadmin` worktree
  `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-06-15-vpsadmin-events/vpsadmin`
  on branch `2026-06-15-vpsadmin-events`.
- Added `VPSADMIN_TELEGRAM_BOT_TOKEN_FILE` support to
  `VpsAdmin::API::TelegramBot` so deployment units can pass the bot token via
  systemd credentials instead of a plain token environment variable. Explicit
  constructor tokens and `VPSADMIN_TELEGRAM_BOT_TOKEN` still take precedence.
- Added focused `TelegramBot` specs for token-file loading and explicit-token
  precedence.
- Extended the generic API rake-task NixOS module with per-task service
  environment variables.
- Added `vpsadmin.api.notifications.telegram` options:
  `botTokenFile`, `apiUrl`, `updatesTimeout`, and `updatesLimit`.
- Added default `event-telegrams` and `telegram-pairing` rake timers. They are
  enabled by default only when `botTokenFile` is configured, load the token via
  `LoadCredential`, and point workers at `%d/telegram-bot-token`.
- Dev cluster remains stopped per user instruction.
- Committed in `vpsadmin` as
  `bc97453293dafdd36cf598d94889fe3fe3f1cccc`
  (`notifications: schedule Telegram workers`) on top of
  `1d7b99732b821af6ec0cbf1d53d7aed642736ddc`.
- Verification run before commit:
  - ambient Bundler spec attempt failed because the ambient gem set was
    missing dependencies; rerun used the repository Nix dev shell;
  - `ruby -c` passed for `api/lib/vpsadmin/api/telegram_bot.rb` and
    `api/spec/lib/vpsadmin/api/telegram_bot_spec.rb`;
  - `nix-instantiate --parse nixos/modules/vpsadmin/api/rake-tasks.nix`
    passed;
  - focused specs passed in Nix dev shell:
    `spec/lib/vpsadmin/api/telegram_bot_spec.rb`,
    `spec/models/tasks/telegram_spec.rb`, and
    `spec/models/tasks/event_delivery_spec.rb`: 40 examples, 0 failures;
  - RuboCop passed for the touched Telegram helper and spec;
  - NixOS module eval with `botTokenFile` configured produced
    `vpsadmin-api-event-telegrams` and `vpsadmin-api-telegram-pairing`
    settings with the expected `LoadCredential`, `%d` token path, rake task,
    timeout, and timer;
  - NixOS module eval with no `botTokenFile` produced no default Telegram
    worker units;
  - `ruby tests/ci-selection-test.rb` passed: 15 runs, 54 assertions,
    0 failures;
  - `nixfmt --check nixos/modules/vpsadmin/api/rake-tasks.nix` passed;
  - `git diff --check` passed.
- Commit hooks passed in `nix develop -c git commit -F
  /tmp/vpsadmin_events_telegram_workers_commit.txt`: Nixfmt and RuboCop
  passed. Commit-msg hooks passed with TextWidth warnings at 72 columns; all
  commit message lines remain within the workspace 80-column rule.
- Mandatory review by `Kuhn` on commit
  `bc97453293dafdd36cf598d94889fe3fe3f1cccc` found no blocking, important,
  or advisory findings. Reviewer reran `nix-instantiate --parse`, `git diff
  --check`, and focused specs: 40 examples, 0 failures.
- Reviewer residual gaps: no live Telegram Bot API coverage, `getUpdates`
  remains operationally single-consumer, and operators must provide the bot
  token as a runtime secret path rather than a Nix-store materialized secret.

## 2026-06-16 - Route matcher field UI refinement

- Started next slice in `vpsadmin` on top of
  `bc97453293dafdd36cf598d94889fe3fe3f1cccc`.
- Goal: make WebUI route matchers easier to understand by narrowing the field
  choices to the selected concrete event type when possible, and by showing
  all matchable fields in the Event Types view.
- Changed `webui/forms/notifications.forms.php` so route matcher field selects
  use the selected route `event_type`'s field list when the route targets one
  concrete event type. Existing matcher fields are preserved in the select even
  if they are outside the current event type's narrowed field list.
- The Event Types view now lists all matchable fields from the API
  `fields` metadata, including core event fields, not only `parameters.*`.
- Committed in `vpsadmin` as
  `85f65dfdeeedf1048cbbd993403d145eb7a2299c`
  (`webui: narrow notification matcher fields`) on top of
  `bc97453293dafdd36cf598d94889fe3fe3f1cccc`.
- Verification before commit:
  - `php -l webui/forms/notifications.forms.php` passed;
  - `php-cs-fixer fix --dry-run --diff webui/forms/notifications.forms.php`
    passed in the Nix dev shell;
  - `ruby tests/ci-selection-test.rb` passed: 15 runs, 54 assertions,
    0 failures;
  - `git diff --check` passed.
- Commit hooks passed in `nix develop -c git commit -F
  /tmp/vpsadmin_events_matcher_fields_commit.txt`: Nixfmt and PhpCsFixer
  passed. Commit-msg hooks passed with TextWidth warnings at 72 columns; all
  commit message lines remain within the workspace 80-column rule.
- Mandatory review by `Harvey` on commits
  `bc97453293dafdd36cf598d94889fe3fe3f1cccc..85f65dfdeeedf1048cbbd993403d145eb7a2299c`
  found no blocking, important, or advisory findings. Reviewer reran
  `php -l webui/forms/notifications.forms.php`, `git diff --check`, and
  checked the commit message length and clean status.
- Reviewer residual gaps: no browser/Playwright run, and changing a route's
  event type narrows matcher fields only after save/reload.

## 2026-06-16 - Telegram pairing service revision

- User rejected the 5-second `vpsadmin:telegram:poll_pairing_updates` rake
  timer because repeatedly booting Ruby is too expensive.
- New direction: replace the timer with a long-running polling service for
  fallback/development use and add Telegram webhook support for production.
- Telegram's Bot API documentation confirms `setWebhook` accepts
  `secret_token` and sends it back as
  `X-Telegram-Bot-Api-Secret-Token`, which matches the desired GitHub-style
  shared-secret verification model.

## 2026-06-16 - Telegram moved out of current scope

- User decided Telegram is distracting for the current implementation frame.
  Current scope is e-mail and webhooks only, while keeping the generic
  receiver-action design prepared for Telegram and other future protocols.
- Saved the Telegram-inclusive branch state as local backup branch
  `2026-06-15-vpsadmin-events-telegram-backup` at commit
  `85f65dfdeeedf1048cbbd993403d145eb7a2299c`.
- Rebasing the active branch in the ambient shell first failed because the
  Overcommit pre-rebase hook could not find the `overcommit` gem. Reran the
  rebase inside `nix develop`, where the hook framework was available.
- Active branch `2026-06-15-vpsadmin-events` was rebased to drop the Telegram
  commits `75ff05513`, `1d7b99732`, and `bc9745329`, while replaying the WebUI
  matcher-field refinement as
  `42c69706fe8f67541a1258a55f1a76e7b490d30e`.
- Removed remaining Telegram action/pairing support from the current active
  tree: model/API action choices, event delivery planning, WebUI receiver
  pairing controls, notification page action, and event-routing specs.
- Updated `plan.md` to describe the current implementation as e-mail +
  webhook, with Telegram and similar protocols as future extensions.
- Cleanup touched eight `vpsadmin` files, mostly deleting Telegram-specific
  branches from models, API resources, routing, WebUI, endpoint coverage, and
  specs.
- Verification before commit:
  - Ruby syntax passed for touched Ruby files and PHP syntax passed for
    touched notification WebUI files;
  - focused API specs passed in the Nix dev shell:
    `spec/api/resources/event_routing_spec.rb`,
    `spec/models/event_route_spec.rb`,
    `spec/models/notification_receiver_action_spec.rb`, and
    `spec/models/tasks/event_delivery_spec.rb`: 61 examples, 0 failures;
  - first RuboCop run used incorrect `app/models/...` paths and failed before
    inspecting those files; rerun with repository paths passed: 8 files,
    0 offenses;
  - `php-cs-fixer fix --dry-run --diff --config=.php-cs-fixer.dist.php`
    passed for `webui/forms/notifications.forms.php` and
    `webui/pages/page_notifications.php`;
  - `ruby tests/ci-selection-test.rb` passed: 15 runs, 54 assertions,
    0 failures;
  - `git diff --check` passed;
  - `rg -n "Telegram|telegram" api webui nixos db packages tests .github`
    returned no matches in the active tree.
- Initially committed in `vpsadmin` as
  `9f2f29e76fe04abaef053f4671f30cd05beba632`
  (`notifications: remove Telegram from current slice`) on top of
  `42c69706fe8f67541a1258a55f1a76e7b490d30e`.
- First commit attempt failed because files were not staged. The pre-commit
  hook still ran and passed before git reported "no changes added to commit".
- Commit hooks passed in `nix develop -c git commit -F
  /tmp/vpsadmin_events_remove_telegram_commit.txt`: Nixfmt, PhpCsFixer, and
  RuboCop passed. Commit-msg hooks passed with TextWidth warnings at 72
  columns; all commit message lines remain within the workspace 80-column
  rule.
- Mandatory review requested from standalone reviewer `Linnaeus` for range
  `42c69706f9e0da38392aad7e0d3b9eb760d6f374..9f2f29e76fe04abaef053f4671f30cd05beba632`.
  The first hash was a typo in the review packet; the actual parent is
  `42c69706fe8f67541a1258a55f1a76e7b490d30e`.
- Mandatory review result:
  - Blocking: `api/spec/api/covered_endpoints.yml` still listed removed scope
    `notification_receiver.action#create_pairing_token`; reviewer confirmed
    `bundle exec rspec spec/api/endpoint_coverage_spec.rb` failed.
  - Important: none.
  - Advisory: review packet used a non-resolving full base hash; reviewer used
    the actual parent commit.
- Fixed the blocking finding by removing
  `notification_receiver.action#create_pairing_token` from
  `api/spec/api/covered_endpoints.yml`.
- Verification after the fix:
  - endpoint coverage plus focused API specs passed in the Nix dev shell:
    `spec/api/endpoint_coverage_spec.rb`,
    `spec/api/resources/event_routing_spec.rb`,
    `spec/models/event_route_spec.rb`,
    `spec/models/notification_receiver_action_spec.rb`, and
    `spec/models/tasks/event_delivery_spec.rb`: 62 examples, 0 failures;
  - a RuboCop run that included the YAML coverage manifest failed because
    RuboCop tried to parse YAML as Ruby; rerun on Ruby/spec files only passed:
    9 files, 0 offenses;
  - `ruby tests/ci-selection-test.rb` passed: 15 runs, 54 assertions,
    0 failures;
  - `git diff --check` passed;
  - `rg -n "Telegram|telegram|create_pairing_token" api webui nixos db
    packages tests .github` returned no matches in the active tree.
- Amended the cleanup commit; final `vpsadmin` commit is
  `06816403df47600ab2caa9558702fb5d3deb33ce`
  (`notifications: remove Telegram from current slice`).
- Amend hooks passed in `nix develop -c git commit --amend --no-edit`:
  Nixfmt, PhpCsFixer, and RuboCop passed. Commit-msg hooks passed with
  TextWidth warnings at 72 columns; all commit message lines remain within the
  workspace 80-column rule.
- Added one more future-protocol hardening tweak before closing: changed
  `NotificationReceiverAction` and `EventDelivery` action enums from arrays to
  explicit numeric mappings (`email: 0`, `webhook: 1`). When Telegram or
  another protocol is added later, it can be appended as a new numeric value
  without changing existing webhook rows.
- Verification after explicit enum mapping:
  - Ruby syntax passed for `api/models/notification_receiver_action.rb` and
    `api/models/event_delivery.rb`;
  - endpoint coverage plus focused API specs passed in the Nix dev shell:
    `spec/api/endpoint_coverage_spec.rb`,
    `spec/api/resources/event_routing_spec.rb`,
    `spec/models/event_route_spec.rb`,
    `spec/models/notification_receiver_action_spec.rb`, and
    `spec/models/tasks/event_delivery_spec.rb`: 62 examples, 0 failures;
  - RuboCop passed for the touched Ruby/spec files: 9 files, 0 offenses;
  - `ruby tests/ci-selection-test.rb` passed: 15 runs, 54 assertions,
    0 failures;
  - `git diff --check` passed;
  - `rg -n "Telegram|telegram|create_pairing_token" api webui nixos db
    packages tests .github` returned no matches in the active tree.
- Amended the cleanup commit again; final `vpsadmin` commit is
  `fdd541472b1fe4f5a8b8b7b6944d3d86d1f265f4`
  (`notifications: remove Telegram from current slice`).
- Final amend hooks passed in `nix develop -c git commit --amend --no-edit`:
  Nixfmt, PhpCsFixer, and RuboCop passed. Commit-msg hooks passed with
  TextWidth warnings at 72 columns; all commit message lines remain within the
  workspace 80-column rule.
- Final `vpsadmin` worktree status is clean. Long integration tests and dev
  cluster startup remain skipped/stopped per user instruction.

## 2026-06-17 - Dev cluster restarted for review

- User requested starting the dev cluster and an explanation of e-mail and
  webhook dispatch.
- `dev-clusters/vpsadmin/bin/devcluster status 2026-06-15-vpsadmin-events`
  initially reported `status: stopped`.
- Started the cluster with the required bridge network:
  `dev-clusters/vpsadmin/bin/devcluster start 2026-06-15-vpsadmin-events
  --topology single --network bridge`.
- The start command rebuilt the feature `vpsadmin` worktree into the services
  closure and started the runner. As before, the command exited non-zero during
  `node1` preparation because `/run/osctl/osctld.sock` was not ready yet.
- Post-start checks:
  - `devcluster status` reported `status: running`, topology `single`,
    network `bridge`, `ready: yes`;
  - `devcluster ssh ... node1 -- sv status osctld nodectld` showed both
    services running;
  - `devcluster ssh ... services -- systemctl --no-pager --failed` showed
    no failed units.
- Ran the known workaround:
  `dev-clusters/vpsadmin/bin/devcluster update 2026-06-15-vpsadmin-events
  node1`, which completed successfully and ran `osctl activate --system`.
- Final verification:
  - `devcluster status` reports `running`, `single`, `bridge`, `ready: yes`;
  - `node1` `osctld` and `nodectld` are running;
  - `curl -k -I https://webui.aitherdev.int.vpsfree.cz/` returned HTTP 200;
  - `curl -k -I https://api.aitherdev.int.vpsfree.cz/` returned HTTP 200;
  - `curl -k -I https://mailpit.aitherdev.int.vpsfree.cz/` returned HTTP 401
    with basic auth, which is expected.
- Review URLs printed by `devcluster urls`:
  - Web UI: `https://webui.aitherdev.int.vpsfree.cz/`
  - API: `https://api.aitherdev.int.vpsfree.cz/`
  - Mailpit: `https://mailpit.aitherdev.int.vpsfree.cz/`
  - Adminer: `https://adminer.aitherdev.int.vpsfree.cz/`
- Seeded credentials:
  - Admin: `test-admin` / `testAdminPassword`
  - User 1: `test-user1` / `testUser1Password`
  - User 2: `test-user2` / `testUser2Password`
  - Mailpit: `mailpit` / `mailpitPassword`
  - Adminer: `adminer` / `adminerPassword`

## 2026-06-17 - Release transaction and dispatcher implementation

- Reworked the dispatcher slice away from timer-driven rake delivery.
- Event routing now creates prepared deliveries. E-mail deliveries render and
  save their `MailLog` snapshot while the event is prepared; webhook
  deliveries save a static JSON payload snapshot.
- Transaction chains append `Transactions::EventDelivery::Release` as the
  go-ahead marker. The nodectld handler for transaction type `9002` moves
  prepared deliveries to `released`, sets `released_at` and `next_attempt_at`,
  and publishes RabbitMQ wakeups for the appropriate action.
- Direct API events still route immediately, but release prepared deliveries
  after commit through `VpsAdmin::API::Notifications::Release`.
- Added `VpsAdmin::API::Notifications::Dispatcher` and
  `api/bin/vpsadmin-notification-dispatcher`. The dispatcher is long-running,
  consumes RabbitMQ messages when configured, and periodically reconciles due
  rows from the database so delivery is durable even if a wakeup is missed.
- Added generic `event_delivery_attempts` and exposed attempts under
  `event.delivery.attempt` in the API. The WebUI event detail now shows
  released time, last attempt, next retry, result, and per-delivery attempts.
- Stale `sending` deliveries that are reclaimed by another dispatcher now mark
  the previous running attempt as failed with `delivery attempt timed out`
  before creating the next attempt.
- E-mail dispatch now reconstructs the rendered message from `MailLog`, sends
  through SMTP, and marks the delivery/attempt sent or retryable/failed.
- Webhook dispatch uses `X-VpsAdmin-Event`, `X-VpsAdmin-Delivery`, and optional
  `X-VpsAdmin-Signature-256`; `X-Hub-*` headers are no longer used.
- Added Nix module `vpsadmin.notificationDispatcher` with one systemd service
  per enabled action. Removed the default event e-mail/webhook timer entries
  from the API rake-task module; compatibility rake tasks remain as one-shot
  reconciliation helpers only.
- The dev cluster remains running from the previous review start, but this
  implementation pass has not rebuilt or restarted it with the dispatcher
  changes.
- Verification for this pass:
  - `nix develop .#api -c bundle exec rubocop ...` passed for 17 changed
    Ruby/spec files;
  - additional RuboCop passed for the changed libnodectld command files;
  - focused notification/transaction specs passed: 61 examples, 0 failures;
  - event-routing API resource specs passed: 14 examples, 0 failures;
  - event-delivery task spec alone passed: 23 examples, 0 failures;
  - PHP syntax passed for `webui/forms/notifications.forms.php` and
    `webui/pages/page_notifications.php`;
  - libnodectld Ruby syntax passed for the changed command files;
  - Nixfmt check passed for `nixos/modules/module-list.nix`,
    `nixos/modules/vpsadmin/api/rake-tasks.nix`, and
    `nixos/modules/vpsadmin/notification-dispatcher.nix`;
  - `git diff --check` passed.
- Commit:
  - `d0d93de41ee7fad4f8b12148f0ddeefad3920c36`
    (`notifications: release events through dispatchers`);
  - plain `git commit -F ...` failed because the Overcommit hook could not
    find the `overcommit` gem outside the Nix shell;
  - reran the same commit through `nix develop -c git commit -F ...`; hooks
    passed. Commit-msg TextWidth warnings were only for the hook's 72-column
    preference; the maximum commit message line is 79 characters, satisfying
    the workspace 80-column rule.
- Worktree status after commit is clean.

## 2026-06-17 - Dispatcher review follow-up

- Mandatory change review of
  `d0d93de41ee7fad4f8b12148f0ddeefad3920c36`
  (`notifications: release events through dispatchers`) found three blocking
  issues:
  - several transaction chains prepared and released routed events before
    appending the later transactions that the notifications described, e.g.
    user suspend/resume, OOM prevention, DNS resolver updates, VPS resource
    changes, and dataset shrink;
  - the Nix dispatcher service wrote `notifications.yml` into its own state
    directory but used the `vpsadmin-api` package app directory by default,
    which meant the Ruby process could read the wrong `config` symlink;
  - broad transaction-chain specs still expected `Transactions::Mail::Send`
    or old `queued`/`planned` delivery states after the dispatcher redesign.
- Follow-up implementation:
  - added `TransactionChain#prepare_event!` and made
    `release_event_deliveries!` a no-op for nil events;
  - moved releases to the end of chains where the event describes later work:
    user suspend/resume/soft-delete/revive, OOM prevention, DNS resolver
    update, dataset shrink, and VPS resource-change notifications;
  - added ordering assertions so release transactions must appear after the
    relevant stop/start/DNS/resource/NoOp transactions;
  - updated stale specs from `Transactions::Mail::Send` to
    `Transactions::EventDelivery::Release` and from `queued`/`planned` to the
    new prepared/released/sent lifecycle;
  - added a dedicated `pkgs.vpsadmin-notification-dispatcher` package using
    the `notificationDispatcher` app directory, set the dispatcher systemd
    working directory to that app, and exported
    `VPSADMIN_NOTIFICATIONS_CONFIG` explicitly;
  - added a dispatcher cache tmpfiles directory for `SCHEMA`;
  - included `vpsadmin.notificationDispatcher.enable` in the read-only
    `vpsadmin.databaseSetup.enable` default so dispatcher-only mailer
    replacement nodes also provide the required setup service.
- Verification after fixes:
  - focused release-order/stale-expectation suite passed:
    48 examples, 0 failures;
  - all touched transaction-chain spec files passed:
    111 examples, 0 failures, 1 existing pending VPS migration interface
    example;
  - RuboCop passed for 41 changed API Ruby/spec files;
  - Ruby syntax passed for representative changed transaction-chain files;
  - `nixfmt --check` passed for `packages/api/notification-dispatcher.nix`,
    `nixos/modules/vpsadmin/notification-dispatcher.nix`,
    `nixos/modules/vpsadmin/database-setup.nix`, and
    `nixos/overlays/default.nix`;
  - overlay evaluation of `pkgs.vpsadmin-notification-dispatcher.pname`
    returned `vpsadmin-notificationDispatcher`;
  - `git diff --check` passed.
- Amended dispatcher commit after the follow-up fixes:
  `2b7dd23a095629affe0082b263beeb8940b92432`
  (`notifications: release events through dispatchers`).
- Amend hooks passed in `nix develop -c git commit --amend -F ...`:
  Nixfmt, PhpCsFixer, and RuboCop passed. Commit-msg TextWidth warnings were
  only for the hook's 72-column preference; all commit message lines remain
  within the workspace 80-column rule.

## 2026-06-17 - Second dispatcher review follow-up

- Mandatory change review of
  `2b7dd23a095629affe0082b263beeb8940b92432`
  (`notifications: release events through dispatchers`) found:
  - blocking: `api/spec/models/security_advisory_spec.rb` still expected the
    old `queued` delivery state and `Transactions::Mail::Send`;
  - important: the new transaction type `9002`
    (`Transactions::EventDelivery::Release`) requires nodectld/libnodectld to
    be deployed before the API emits release transactions.
- Follow-up implementation:
  - updated the advisory spec to expect prepared event deliveries and the
    event-delivery release transaction;
  - documented the mixed-version deployment order in the initiative plan:
    nodectld/libnodectld release handling must be deployed before switching
    API transaction chains to emit `Transactions::EventDelivery::Release`.
- Verification after fixes:
  - `nix develop .#api -c bundle exec rspec spec/models/security_advisory_spec.rb`
    passed: 5 examples, 0 failures;
  - stale spec search for `be_queued_state`, `be_planned_state`, and
    `Transactions::Mail::Send` returned no results;
  - `nix develop .#api -c bundle exec rubocop spec/models/security_advisory_spec.rb`
    passed;
  - `git diff --check` passed.
- Amended dispatcher commit after this follow-up:
  `0416493d7c25d48df15a3ead6e1f30843f0c66d3`
  (`notifications: release events through dispatchers`).
- Amend hooks passed in `nix develop -c git commit --amend -F ...`:
  Nixfmt, PhpCsFixer, and RuboCop passed. Commit-msg TextWidth warnings were
  only for the hook's 72-column preference; all commit message lines remain
  within the workspace 80-column rule.

## 2026-06-17 - Dispatcher dev-cluster wiring

- Dev-cluster activation exposed two missing pieces in the dispatcher design:
  - direct API event releases had no RabbitMQ notification config, so they
    could only rely on dispatcher database polling instead of immediate
    wakeups;
  - e-mail and webhook dispatcher units shared one generated app state
    directory, so concurrent `preStart` runs could replace config/plugin
    symlinks under each other.
- Follow-up implementation:
  - added `vpsadmin.api.notifications.rabbitmq.*` options and generated
    `VPSADMIN_NOTIFICATIONS_CONFIG` for API processes when wakeups are
    enabled;
  - added a dedicated RabbitMQ `notification` user profile to
    `tools/rabbitmqcfg.rb`, with permissions for the notification exchange
    and per-action queues;
  - allowed nodectld node users to configure/write the
    `vpsadmin.notifications` exchange so release transactions can publish
    wakeups;
  - configured the dev services VM with the notification RabbitMQ user, API
    notification wakeups, and long-running e-mail/webhook dispatcher units;
  - changed dispatcher Nix state layout so each action uses its own generated
    app state directory under `notification-dispatcher/email` or
    `notification-dispatcher/webhook`.
- Dev-cluster result:
  - `dev-clusters/vpsadmin/bin/devcluster update 2026-06-15-vpsadmin-events services`
    completed successfully after the fixes;
  - `dev-clusters/vpsadmin/bin/devcluster status 2026-06-15-vpsadmin-events`
    reports running, topology `single`, network `bridge`, ready `yes`;
  - `systemctl is-active` on the services VM reports
    `vpsadmin-api.service`,
    `vpsadmin-notification-dispatcher-email.service`,
    `vpsadmin-notification-dispatcher-webhook.service`, and
    `rabbitmq.service` active;
  - `curl -k -I --max-time 15` returned HTTP 200 for WebUI, the
    Notifications URL, and the API;
  - `rabbitmqctl list_permissions -p vpsadmin_test` shows the `notification`
    user can access the notification exchange/queues, and node users can
    configure/write the notification exchange.
- Verification for this follow-up:
  - `nix develop -c nixfmt --check` passed for the changed Nix module and
    dev-cluster config files;
  - `ruby -c tools/rabbitmqcfg.rb` passed;
  - `nix develop -c ruby tools/rabbitmqcfg.rb user --perms notification ...`
    printed the expected notification exchange/queue permissions;
  - `git diff --check` passed.
- Amended dispatcher commit after this dev-cluster wiring follow-up:
  `6dd92a35422f9fdd9ab6afbf001d2c246d90dc1f`
  (`notifications: release events through dispatchers`).
- Amend hooks passed in `nix develop -c git commit --amend -F ...`:
  Nixfmt, PhpCsFixer, and RuboCop passed. Commit-msg TextWidth warnings were
  only for the hook's 72-column preference; all commit message lines remain
  within the workspace 80-column rule.
- Mandatory follow-up review requested from standalone agent `Euler`
  (`019ed582-6f75-7d51-a354-2cc6d5bfce18`) using
  `skills/mandatory-change-review/SKILL.md` against the focused delta from
  `0416493d7c25d48df15a3ead6e1f30843f0c66d3` to
  `6dd92a35422f9fdd9ab6afbf001d2c246d90dc1f`.
- Mandatory follow-up review result:
  - blocking: none;
  - important: none;
  - advisory: dispatcher action state directories were separate, but the
    generated package app still resolved `config`/`plugins` through the
    shared `/run/vpsadmin/notificationDispatcher` symlinks, leaving a small
    boot-order/config-read risk.
- Advisory follow-up implementation:
  - `VpsAdmin::API.root` can now be overridden with `VPSADMIN_ROOT`;
  - `api-app.nix` can skip `/run/vpsadmin/<name>` links for callers that
    provide their own runtime app root;
  - notification dispatcher action services now build per-action runtime app
    roots under `notification-dispatcher/email/app` and
    `notification-dispatcher/webhook/app`, set `VPSADMIN_ROOT` to that path,
    and run with that path as their working directory.
- Advisory follow-up verification:
  - Ruby syntax passed for `api/lib/vpsadmin/api.rb`;
  - RuboCop passed for `api/lib/vpsadmin/api.rb`;
  - Nixfmt check passed for `nixos/modules/vpsadmin/api-app.nix`,
    `nixos/modules/vpsadmin/notification-dispatcher.nix`, and the already
    changed dispatcher/API dev-cluster Nix files;
  - `git diff --check` passed;
  - `dev-clusters/vpsadmin/bin/devcluster update 2026-06-15-vpsadmin-events services`
    completed successfully with the runtime-root fix;
  - WebUI, the Notifications URL, and API returned HTTP 200;
  - `systemctl is-active` reports the API, e-mail dispatcher, webhook
    dispatcher, and RabbitMQ active;
  - `systemctl show` reports the e-mail dispatcher running with
    `VPSADMIN_ROOT=/var/lib/vpsadmin/notification-dispatcher/email/app` and
    the webhook dispatcher running with
    `VPSADMIN_ROOT=/var/lib/vpsadmin/notification-dispatcher/webhook/app`.
- Amended dispatcher commit after advisory follow-up:
  `bb83dfaae4c40996e37d23ba53c293f119bbf690`
  (`notifications: release events through dispatchers`).
- Amend hooks passed in `nix develop -c git commit --amend -F ...`:
  Nixfmt, PhpCsFixer, and RuboCop passed. Commit-msg TextWidth warnings were
  only for the hook's 72-column preference; all commit message lines remain
  within the workspace 80-column rule.
- Final focused mandatory review requested from standalone agent `Averroes`
  (`019ed59f-7c11-74c1-a051-052ae8c9448d`) against
  `6dd92a35422f9fdd9ab6afbf001d2c246d90dc1f..bb83dfaae4c40996e37d23ba53c293f119bbf690`.
- Final focused mandatory review result:
  - blocking: none;
  - important: none;
  - advisory: none;
  - residual risks: long integration tests remain skipped; smoke verification
    does not exercise a full released event through RabbitMQ to both
    dispatchers; runtime-root isolation is verified by dev-cluster/systemctl
    checks rather than a dedicated automated regression.
- Worktree status after amend is clean.

## 2026-06-17 - Clean dev-cluster reset and WebUI notification fixes

- User requested clean migrations only and explicitly asked for just one
  database migration for this session.
- Removed the temporary conditional repair migration that had been used only
  to patch an old dev-cluster database state.
- Confirmed the notification/event system still uses only one new migration:
  `api/db/migrate/20260615110000_add_events.rb`.
- Reset the dev cluster state with
  `dev-clusters/vpsadmin/bin/devcluster reset 2026-06-15-vpsadmin-events`
  and restarted it with topology `single` on the bridge network.
- The restart command hit a late node-preparation race while connecting to
  `/run/osctl/osctld.sock`, but `devcluster status` afterwards reported the
  cluster running and ready.
- Fixed WebUI notification pages that were broken on a clean dev cluster:
  - `event_type#index` returns a HaveAPI response object because it is a
    `hash_list`; the WebUI now normalizes API list/response objects before
    iterating them, fixing Event types and route edit pages;
  - the Event log page no longer forwards the WebUI router parameter
    `action=events` as the event-delivery action filter. The filter field is
    rendered as `delivery_action` and translated to API input `action`.
- Added Playwright regression coverage to the existing support-pages
  notification test for:
  - Event types page and matchable fields;
  - Event log page and the `delivery_action` filter;
  - editing the generated default route.
- Verification:
  - `php -l webui/forms/notifications.forms.php` passed;
  - `nix shell nixpkgs#nodejs -c node --check
    tests/playwright/webui/specs/support-pages.spec.cjs` passed;
  - focused one-off Playwright smoke against the reset dev cluster passed:
    login as `test-user1`, Event types, Event log, and default-route edit all
    returned HTTP 200 with the expected headings;
  - running the repository Playwright test directly was not completed because
    the standalone runner requires the fixture JSON normally generated by the
    full integration harness, and long harness runs remain intentionally
    skipped for now.
- Current dev cluster status: running, topology `single`, bridge network,
  ready `yes`.
- Committed follow-up as
  `5c26c2dbbc3ccc865f38bc8459904e969792f995`
  (`webui: fix notification event pages`).
- Commit hooks passed:
  - Nixfmt OK;
  - PhpCsFixer OK;
  - commit-msg hooks passed with TextWidth warnings for the hook's 72-column
    preference only; all lines remain within the workspace 80-column rule.
- Mandatory change review requested from standalone reviewer `Leibniz`
  (`019ed5fb-0e14-7640-820b-d09cfcb668a1`) for range
  `bb83dfaae4c40996e37d23ba53c293f119bbf690..5c26c2dbbc3ccc865f38bc8459904e969792f995`.
- Mandatory change review result:
  - blocking: none;
  - important: none;
  - advisory: none;
  - residual risks: the full Playwright/integration harness remains skipped
    because it needs generated `VPSADMIN_WEBUI_FIXTURES`; coverage verifies
    page rendering and field wiring, but not a submitted `delivery_action`
    filter round-trip against the API.

## 2026-06-17 - Notification route/action WebUI follow-up

- User feedback on the dev cluster:
  - the route-list add-subroute icon used the wrong `m_add.png` member icon;
  - subroute visualization in the route list was not acceptable;
  - firing a test notification event still returned HTTP 500.
- Fixed route list affordances:
  - route and receiver-action add links now use the plain green
    `vps_add.png` icon;
  - route rows are rendered in tree order with sibling-only drag/drop
    reordering;
  - subroute labels show a muted `Parent: <route>` hint above the route label
    instead of ASCII tree characters;
  - route edit pages list their subroutes, and the plus icon opens the
    standalone add-route page with the parent preselected.
- Reworked receiver action forms in the WebUI:
  - removed inline action edit/add controls from receiver edit;
  - added standalone add/edit pages;
  - add action is now a two-step flow: choose action type, then fill the
    action-specific form.
- Fixed test-event event detail rendering:
  - event creation was succeeding, but `event_show` crashed while loading
    delivery attempts because attempts were listed from a delivery instance
    without all nested HaveAPI path arguments;
  - attempts are now loaded through the parent event resource as
    `event->delivery(delivery_id)->attempt->list()`.
- Kept the session keepalive correction narrow:
  - `keepalive.php` only touches the PHP session file;
  - the browser timeout countdown is not reset, preserving automatic logout.
- Deployed the updated services to the running dev cluster with
  `dev-clusters/vpsadmin/bin/devcluster update 2026-06-15-vpsadmin-events services`.
- Final dev cluster health after deployment:
  - `devcluster status` reports running, topology `single`, network `bridge`,
    ready `yes`;
  - WebUI and API both return HTTP 200;
  - `systemctl --failed --no-pager` on the services machine lists 0 failed
    units.
- Verification:
  - `php -l webui/forms/notifications.forms.php` passed;
  - `php -l webui/pages/page_notifications.php` passed;
  - `php -l webui/public/keepalive.php` passed;
  - `nix shell nixpkgs#nodejs -c node --check
    tests/playwright/webui/specs/support-pages.spec.cjs` passed;
  - `git diff --check` passed;
  - focused one-off Playwright smoke against the dev cluster passed: login as
    `test-user1`, verify route list uses `vps_add.png`, create a temporary
    subroute under the default route and verify the parent hint, create a test
    notification event through the form, verify the redirected event detail page
    renders deliveries without HTTP 500, and delete the temporary route.
- Long integration test runs remain skipped as requested while implementation
  slices are still settling.
- Committed follow-up as
  `23fcb6da1c8c78d5c2a3536e6709ab922965079a`
  (`webui: improve notification route editing`).
- Commit hooks passed:
  - Nixfmt OK;
  - PhpCsFixer OK;
  - commit-msg hooks passed with TextWidth warnings for the hook's 72-column
    preference only; all lines remain within the workspace 80-column rule.
- Mandatory change review requested from standalone reviewer `Helmholtz`
  (`019ed66f-cd14-7be3-97f6-3410b2a531c8`) for range
  `5c26c2dbbc3ccc865f38bc8459904e969792f995..23fcb6da1c8c78d5c2a3536e6709ab922965079a`.
- Mandatory change review result:
  - blocking: none;
  - important: none;
  - advisory: none;
  - residual risks: long integration tests remain intentionally skipped; the
    committed Playwright test covers the notification flow broadly, but the
    exact green plus icon and subroute parent-hint rendering are covered by the
    focused one-off dev-cluster smoke rather than permanent narrow assertions;
    keepalive countdown behavior was checked as separate from PHP session touch.

## 2026-06-17 - Mailpit delivery and route dragging follow-up

- Implemented the requested notification follow-up:
  - devcluster Mailpit capture now also overrides
    `vpsadmin.notificationDispatcher.smtp` to `127.0.0.1:1025` when
    `mail.capture.enable` is true;
  - e-mail delivery uses `Mail#deliver!` with `return_response: true` and
    persists the SMTP status/body on both the delivery and attempt;
  - `Net::SMTPError#response` is captured for failed SMTP deliveries when
    available;
  - WebUI delivery result/attempt text now labels e-mail statuses as `SMTP NNN`
    and message ids as `Message-ID ...`;
  - the bundled TableDnD plugin now copies `onAllowDrop` and `dragHandle` into
    its config, binds row dragging only to `.notification-drag-handle` when a
    handle is configured, and applies the move cursor only to that handle.
- Verification:
  - `nix develop .#api -c bundle exec rspec
    spec/models/tasks/event_delivery_spec.rb` passed with 24 examples;
  - `nix develop .#api -c bundle exec rubocop
    lib/vpsadmin/api/notifications.rb
    spec/models/tasks/event_delivery_spec.rb` passed;
  - `nix shell nixpkgs#nodejs -c node --check
    webui/public/js/jquery.tablednd.js` passed;
  - `nix develop .#webui -c php -l forms/notifications.forms.php` passed;
  - `nix shell nixpkgs#nixfmt-rfc-style -c nixfmt --check
    dev-clusters/vpsadmin/nix/test.nix` passed;
  - `git diff --check` passed for the vpsadmin worktree and the devcluster
    Nix file.
- Deployed the final tree to the running services VM with
  `dev-clusters/vpsadmin/bin/devcluster update
  2026-06-15-vpsadmin-events services`.
- The first update attempt failed while copying the new services generation
  because the services VM exhausted inodes in `/nix/store`; `/` had about
  134 MiB free but 0 free inodes.
- Recovery:
  - remounted `/nix/store` writable;
  - removed the incomplete failed-copy path
    `/nix/store/ji1s2q38w48nksazci63b5rxy9dbzxxv-system-path`;
  - ran `nix-store --gc`, which deleted 615 unreferenced store paths and freed
    285.1 MiB;
  - retried `devcluster update`, which completed successfully.
- Post-update health:
  - `vpsadmin-api.service`,
    `vpsadmin-notification-dispatcher-email.service`,
    `vpsadmin-notification-dispatcher-webhook.service`, and `rabbitmq.service`
    are active;
  - `systemctl --failed` lists 0 failed units;
  - dispatcher config contains SMTP `address: 127.0.0.1` and `port: 1025`;
  - the services VM has about 830 MiB free and 133k free inodes after the
    successful retry.
- Runtime smoke after the final deployment:
  - cleared Mailpit messages via `DELETE /api/v1/messages`;
  - emitted `user.test_notification` for `test-user1`;
  - event `20` produced delivery `24` in state `sent`;
  - stored `provider_message_id`
    `6a32df4934718_ddf36a8-439@vpsadmin-services.mail`;
  - stored SMTP `response_status: 250` and response body
    `250 2.0.0 Ok: queued as 2YuKA20MBKxGWXIAL9dtgU`;
  - Mailpit reported one accepted message to `test-user1@example.test` with the
    same Message-ID and queue id `2YuKA20MBKxGWXIAL9dtgU`.
- Note: remounting `/nix/store` back to read-only after the update returned
  `mount point is busy`; the services are healthy, but the devcluster services
  VM currently has `/nix/store` mounted writable due to the recovery step.

## 2026-06-18 - Delivery detail recovery from parallel session

- Audited the uncommitted changes left by another Codex instance.
- Kept the useful parts:
  - delivery detail API fields for e-mail snapshots and webhook payload/results;
  - persisted response headers on deliveries and attempts;
  - SMTP response status/body capture for e-mail dispatch;
  - receiver/action filters in the event log;
  - WebUI delivery detail pages and direct delivery links;
  - manual `tools/webhook-test-server.rb`;
  - new `alerts/notification-routing` integration test definition.
- Fixed the session migration shape:
  - folded `response_headers` into
    `api/db/migrate/20260615110000_add_events.rb`;
  - removed the accidental second migration;
  - kept `api/db/schema.rb` at version `2026_06_15_110000`.
- Fixed/expanded delivery details:
  - WebUI delivery show now fetches the nested delivery as
    `event->delivery(delivery_id)->show()`;
  - event-log delivery chips link directly to the delivery detail page;
  - e-mail delivery detail shows To/Cc/From/Reply-To/Return-Path,
    Message-ID, subject, and plain/html bodies when present;
  - empty e-mail details now show an explicit "No e-mail snapshot" row.
- Fixed the new integration test helper startup:
  - `systemctl show` now uses `vpsadmin-api.service`, which returns the
    correct working directory in the running services VM.
- Manual webhook testing note:
  - run `tools/webhook-test-server.rb` inside the services VM from
    `/mnt/vpsadmin`;
  - configure webhook receiver actions with
    `http://127.0.0.1:18080/events`;
  - the latest request is written to
    `/tmp/vpsadmin-webhook-test/request.json` in the services VM.
- Quick verification passed:
  - `nix develop .#api -c bash -lc 'bundle exec rspec
    spec/api/resources/event_routing_spec.rb
    spec/models/tasks/event_delivery_spec.rb'`: 41 examples, 0 failures;
  - `nix develop .#api -c bash -lc 'bundle exec rubocop
    models/event_delivery.rb models/event_delivery_attempt.rb
    lib/vpsadmin/api/notifications.rb lib/vpsadmin/api/resources/event.rb
    spec/api/resources/event_routing_spec.rb
    spec/models/tasks/event_delivery_spec.rb'`: no offenses;
  - `nix develop .#webui -c bash -lc 'php -l
    forms/notifications.forms.php && php -l pages/page_notifications.php'`:
    no syntax errors;
  - `nix shell nixpkgs#nodejs -c bash -lc 'node --check
    webui/public/js/jquery.tablednd.js && node --check
    tests/playwright/webui/specs/support-pages.spec.cjs'`: passed;
  - `ruby -c tools/webhook-test-server.rb`: syntax OK;
  - `nix shell nixpkgs#nixfmt-rfc-style -c nixfmt --check
    tests/suite/alerts/notification-routing.nix`: passed;
  - `ruby tests/ci-selection-test.rb`: 15 runs, 54 assertions, 0 failures;
  - `./test-runner.sh ls alerts/notification-routing`: listed the new test;
  - `git diff --check`: passed.
- Mandatory review by standalone agent `Kant`
  (`019edb2f-bbe0-7b11-8d97-823094548876`) found:
  - Blocking: e-mail Bcc was exposed through user-facing delivery details;
  - Important: folding `response_headers` into the single session migration
    requires a dev-cluster DB reset for any state that already ran the older
    migration draft;
  - Important: webhook response headers needed storage bounds;
  - Advisory: manual webhook-test docs should avoid local absolute paths and
    hard-coded cluster slug;
  - Residual risk: add explicit negative delivery-detail authorization
    coverage.
- Mandatory review follow-up:
  - removed `mail_bcc` from the user-facing event-delivery API, model helper,
    WebUI delivery detail, and specs;
  - added a cross-user delivery-detail/attempt authorization regression;
  - bounded stored webhook response headers by total size, name size, value
    size, and value count, and mark truncated snapshots with
    `x-vpsadmin-truncated`;
  - added a webhook response-header bounds regression;
  - changed manual webhook-test instructions to use placeholder workspace and
    cluster names.
- The one-migration requirement is preserved. The dev cluster must be reset
  before the next review smoke, because older dev DB state may be missing the
  folded `response_headers` columns.
- Post-review verification and dev cluster smoke:
  - amended `vpsadmin` head:
    `647e06790a91126707857aab7accc564b4d5814b`;
  - Overcommit hooks passed on amend: Nixfmt, PhpCsFixer, and RuboCop; the
    commit-message width hook warned at 72 columns, but all lines are within
    the workspace 80-column limit;
  - reset the dev cluster state with
    `dev-clusters/vpsadmin/bin/devcluster reset 2026-06-15-vpsadmin-events`;
  - restarted it with `--topology single --network bridge`;
  - first fresh start hit the known node `osctld.sock` readiness race after
    the cluster was otherwise ready; `devcluster update ... node1` completed
    the node activation successfully;
  - cluster status is `running`, `ready: yes`, on the bridge network;
  - `systemctl --failed` in the services VM lists 0 failed units;
  - `vpsadmin-api.service`,
    `vpsadmin-notification-dispatcher-email.service`,
    `vpsadmin-notification-dispatcher-webhook.service`, and `rabbitmq.service`
    are active;
  - live Playwright smoke against
    `https://webui.aitherdev.int.vpsfree.cz/` logged in as `test-user1`,
    loaded Notifications, Event types, Event log, Routes, Receivers, and Test
    event pages, created a test event, opened delivery detail, and verified
    the e-mail snapshot is visible without Bcc.
- Manual webhook test server instructions were corrected:
  - the services VM does not put Ruby in the default login `PATH`;
  - after `devcluster ssh <cluster-slug> services`, run from `/mnt/vpsadmin`:
    `ruby_bin=$(find /nix/store -maxdepth 3 -type f -path '*/bin/ruby' |
    grep 'ruby-[0-9]' | head -n 1)`;
  - then run
    `"$ruby_bin" tools/webhook-test-server.rb --host 127.0.0.1 --port
    18080`;
  - configure the webhook receiver action URL as
    `http://127.0.0.1:18080/events`;
  - received requests are written under `/tmp/vpsadmin-webhook-test` in the
    services VM.
- Long VM integration test execution remains intentionally skipped while this
  implementation slice is being settled.

## 2026-06-18 - Webhook private destination allowlist

- User reported manual webhook delivery to `127.0.0.1` failed with
  `ArgumentError: webhook host resolves to a private address`.
- Implemented committed vpsadmin follow-up:
  - commit `82311a427` (`notifications: allow configured private webhooks`);
  - replaced the blunt `VPSADMIN_EVENT_WEBHOOK_ALLOW_PRIVATE=1` bypass with
    `webhook.allowed_private_ranges` in notification dispatcher config;
  - added NixOS option
    `vpsadmin.notificationDispatcher.webhook.allowedPrivateRanges`, defaulting
    to an empty list;
  - test services now allow only loopback ranges for webhook delivery;
  - `alerts/notification-routing` no longer enables an all-private-address
    environment bypass;
  - focused specs cover default private-address blocking, configured loopback
    delivery, and rejecting private addresses outside the allowlist.
- Security decision:
  - webhook URLs remain an SSRF-sensitive surface even with static payloads,
    because users control destination hosts and can observe delivery
    success/failure;
  - default deny for private/special-use destinations stays in place;
  - deployments that want users to reach private VPS address space must opt in
    with explicit CIDR ranges, e.g. the production configuration can allow the
    relevant vpsFree private range when that deployment slice is added.
- Quick verification:
  - `nix develop .#api -c bash -lc 'bundle exec rspec
    spec/models/tasks/event_delivery_spec.rb'`: 27 examples, 0 failures;
  - `nix develop .#api -c bash -lc 'bundle exec rubocop
    lib/vpsadmin/api/notifications.rb
    spec/models/tasks/event_delivery_spec.rb'`: no offenses;
  - `nix shell nixpkgs#nixfmt-rfc-style -c nixfmt --check ...`: passed for
    the notification dispatcher module, service test config, alert routing
    test, and workspace devcluster config;
  - Ruby syntax and `git diff --check`: passed;
  - Nix parse checks passed for the touched Nix files;
  - `ruby tests/ci-selection-test.rb`: 15 runs, 54 assertions, 0 failures;
  - `./test-runner.sh ls alerts/notification-routing`: listed the test.
- Mandatory change review by standalone agent `Ramanujan`
  (`019edb85-7bcb-7103-9f9c-4f3d80589dea`):
  - Blocking findings: none;
  - Important findings: none;
  - Advisory: local dev-cluster loopback allowlist currently lives as an
    uncommitted workspace edit in `dev-clusters/vpsadmin/nix/test.nix`, so a
    fresh workspace would need equivalent dev-cluster config for the manual
    localhost webhook docs to be true;
  - Residual gaps: long VM `alerts/notification-routing` has not been rerun
    for this follow-up; unit coverage does not explicitly test allowlisted
    IPv6 loopback or mixed DNS answers.
- Dev-cluster deployment after review:
  - updated `2026-06-15-vpsadmin-events` services VM to vpsadmin head
    `82311a427`;
  - removed the temporary workspace-local webhook allowlist override from
    `dev-clusters/vpsadmin/nix/test.nix`, because the committed vpsadmin
    test-services config now supplies the loopback allowlist;
  - generated webhook dispatcher config now has exactly
    `["127.0.0.0/8", "::1/128"]` in `webhook.allowed_private_ranges`;
  - cluster is running/ready, `systemctl --failed` reports 0 failed units, and
    API/e-mail dispatcher/webhook dispatcher/RabbitMQ are active.
- Live webhook smoke:
  - started `tools/webhook-test-server.rb` in the services VM on
    `127.0.0.1:18080`;
  - used WebUI as `test-user1` to create receiver `#4`, webhook action `#5`
    pointing to `http://127.0.0.1:18080/events`, route `#5`, and a
    `user.test_notification` event;
  - webhook dispatcher delivered HTTP POST to `/events` from `127.0.0.1`;
  - captured request included `X-VpsAdmin-Event: user.test_notification`,
    `X-VpsAdmin-Delivery: 9`, and `X-VpsAdmin-Signature-256`;
  - captured payload subject was `Codex webhook smoke mqjq4dfk`;
  - database shows delivery `9` state `sent`, response `202 accepted`, and
    attempt `13` succeeded;
  - stopped the temporary webhook test server afterward.

## 2026-06-18 - vpsAdmin-managed webhook destination ownership

- User clarified that vpsAdmin-managed internal destinations should be allowed
  only when the destination IP belongs to the same user, and that checking
  `IpAddress` is sufficient because `HostIpAddress` is a subset.
- Implemented ownership-aware webhook destination policy in vpsadmin:
  - committed as `86f31e3` (`notifications: guard managed webhook
    destinations`);
  - all resolved webhook A/AAAA results are validated before connecting;
  - vpsAdmin-managed `IpAddress` destinations are allowed only when
    `IpAddress#current_owner` matches `delivery.event.user_id`;
  - vpsAdmin-managed destinations owned by another user, unowned, or used by
    ownerless events are rejected before any private-range exception;
  - untracked public destinations remain allowed;
  - untracked private/special destinations remain denied unless they match the
    dispatcher exception list;
  - the dispatcher still connects with `Net::HTTP.start(... ipaddr:)` to the
    vetted address.
- Renamed the webhook exception config:
  - YAML key `webhook.allowed_untracked_private_ranges`;
  - NixOS option
    `vpsadmin.notificationDispatcher.webhook.allowedUntrackedPrivateRanges`;
  - dev/test services continue allowing only `127.0.0.0/8` and `::1/128` as
    untracked private exceptions for local webhook testing.
- Updated manual webhook testing docs to explain that production should rely on
  vpsAdmin IP ownership for managed VPS addresses and reserve private
  exceptions for deliberate non-vpsAdmin targets.
- Quick verification:
  - `nix develop .#api -c bash -lc 'bundle exec rspec
    spec/models/tasks/event_delivery_spec.rb'`: 32 examples, 0 failures;
  - `nix develop .#api -c bash -lc 'bundle exec rubocop
    lib/vpsadmin/api/notifications.rb
    spec/models/tasks/event_delivery_spec.rb'`: no offenses;
  - `nix shell nixpkgs#nixfmt-rfc-style -c nixfmt --check
    nixos/modules/vpsadmin/notification-dispatcher.nix
    tests/configs/nixos/vpsadmin-services.nix`: passed;
  - `ruby -c` on the touched Ruby files: syntax OK;
  - `git diff --check`: passed;
  - `ruby tests/ci-selection-test.rb`: 15 runs, 54 assertions, 0 failures.
- Attempted `./test-runner.sh ls alerts/notification-routing` as a lightweight
  Nix/test configuration evaluation, but it spent several minutes in
  `nix-instantiate`; the check was intentionally interrupted and no long VM
  integration test was run.
- Commit/hook note:
  - the first `git commit` attempts failed because the Overcommit hook was
    installed but the ambient shell and `nix develop .#api` did not expose the
    root `overcommit` gem to the hook;
  - final commit ran with Overcommit enabled by exporting root `.gems` in
    `GEM_HOME`, `GEM_PATH`, and `PATH`, plus `nixfmt` from
    `nixpkgs#nixfmt-rfc-style`;
  - Overcommit pre-commit hooks passed (`Nixfmt`, `RuboCop`); commit-msg hooks
    passed with only the repository's stricter 72-column warning, while the
    commit message still satisfies the workspace 80-column rule.
- Mandatory change review:
  - standalone reviewer `Carver`
    (`019edbd7-9d2b-7a53-a221-a8f0450d2e4c`);
  - blocking finding: `managed_webhook_ip_address` checked only the first
    containing `Network`, so overlapping vpsAdmin networks could make a later
    managed allocation look untracked and allow cross-user delivery;
  - important findings: none;
  - advisory: exact `IpAddress.find_by(ip_addr:)` has no schema index; deferred
    because this session must keep one migration and this path already had to
    use existing IP/network tables for ownership policy.
- Review follow-up:
  - fixed lookup to collect all matching `IpAddress` rows across all containing
    networks and allow delivery only when every match currently belongs to the
    event user;
  - matching managed addresses with no event user, no owner, another owner, or
    conflicting owners now fail closed;
  - added specs for ownerless managed events, ownership through VPS network
    interfaces, later overlapping networks, and conflicting overlapping
    allocations;
  - reran `nix develop .#api -c bash -lc 'bundle exec rspec
    spec/models/tasks/event_delivery_spec.rb'`: 36 examples, 0 failures;
  - reran `nix develop .#api -c bash -lc 'bundle exec rubocop
    lib/vpsadmin/api/notifications.rb
    spec/models/tasks/event_delivery_spec.rb'`: no offenses;
  - reran Ruby syntax checks and `git diff --check`: passed.
  - amended the commit to include the review fix; final commit is `86f31e3`.
  - reran `ruby tests/ci-selection-test.rb`: 15 runs, 54 assertions,
    0 failures.
- Final mandatory change review:
  - standalone reviewer `Boole`
    (`019edbe3-0e68-7421-948b-1e440d68d99e`);
  - reviewed final commit `86f31e3` against `82311a4`;
  - blocking findings: none;
  - important findings: none;
  - advisory findings: none;
  - residual risks noted: long VM integration test not run; production config
    was not part of this slice; ownership lookup may deserve indexing/SQL
    optimization under high webhook volume.

## 2026-06-18 - Manual webhook test server

- User noticed the manual webhook test server was not running.
- Checked dev cluster `2026-06-15-vpsadmin-events`: running and ready on bridge
  networking.
- Started `tools/webhook-test-server.rb` inside the services VM:
  - bind address: `127.0.0.1`;
  - port: `18080`;
  - PID: `40666`;
  - URL for receiver actions: `http://127.0.0.1:18080/events`;
  - log directory: `/tmp/vpsadmin-webhook-test`.
- Verified with a local POST from the services VM:
  - response: HTTP `202 Accepted`, body `accepted`;
  - latest request file: `/tmp/vpsadmin-webhook-test/request.json`.
- Updated services VM afterward to vpsadmin commit `86f31e3` using
  `devcluster update 2026-06-15-vpsadmin-events services`.
- Post-update checks:
  - cluster remains running/ready;
  - `systemctl --failed` reports 0 failed units;
  - `vpsadmin-api.service`,
    `vpsadmin-notification-dispatcher-webhook.service`,
    `vpsadmin-notification-dispatcher-email.service`, and `rabbitmq.service`
    are active;
  - generated webhook dispatcher config now uses
    `webhook.allowed_untracked_private_ranges`;
  - test server still listens on `127.0.0.1:18080` as PID `40666`;
  - post-update local POST returned HTTP `202 Accepted`.

## 2026-06-18 - Notification WebUI polish and retry

- Implemented user-facing notification UI follow-ups in the vpsadmin worktree:
  - delivery details now show linked receiver and receiver-action labels instead
    of textual `#id` placeholders;
  - event details delivery rows link to the receiver using its label;
  - event parameters render as wrapped pretty JSON instead of overflowing the
    table on one long line;
  - the notifications sidebar submenu is static, with `Event log` first and
    the current page kept visible;
  - webhook secret fields use a visible text input while preserving the existing
    redaction/empty-value behavior for stored secrets;
  - failed deliveries can be manually retried from the delivery details page.
- Added API support for manual retry:
  - `event.delivery#retry` moves failed deliveries back to `released`, clears
    the error summary, schedules immediate processing, and publishes the retry
    request through RabbitMQ after commit;
  - retry rejects non-failed deliveries.
- Added derived API fields on event deliveries for receiver/action labels and
  action display target so WebUI pages do not have to display raw ids.
- Added Playwright assertions for the sidebar, visible webhook secret input,
  pretty parameters, and linked receiver/action labels.
- Integrated the webhook test server into the dev cluster services VM:
  - systemd unit: `vpsadmin-webhook-test-server.service`;
  - URL for receiver actions: `http://127.0.0.1:18080/events`;
  - latest request log: `/tmp/vpsadmin-webhook-test/request.json`;
  - documented in `dev-clusters/vpsadmin/README.md`.
- Verification:
  - `nix develop .#api -c bundle exec rspec
    spec/api/resources/event_routing_spec.rb`: 18 examples, 0 failures;
  - PHP syntax checks for `forms/notifications.forms.php` and
    `pages/page_notifications.php`: no syntax errors;
  - Ruby syntax checks for touched API/model/spec files: Syntax OK;
  - `nix shell nixpkgs#nodejs -c node --check
    tests/playwright/webui/specs/support-pages.spec.cjs`: passed;
  - `nix shell nixpkgs#nixfmt-rfc-style -c nixfmt --check
    dev-clusters/vpsadmin/nix/test.nix`: passed;
  - `nix develop .#api -c bundle exec rubocop
    lib/vpsadmin/api/notifications.rb
    lib/vpsadmin/api/resources/event.rb
    models/event_delivery.rb
    spec/api/resources/event_routing_spec.rb`: no offenses;
  - `ruby tests/ci-selection-test.rb`: 15 runs, 54 assertions, 0 failures;
  - `git diff --check` in the vpsadmin worktree: passed;
  - `git diff --check -- README.md nix/test.nix` in `dev-clusters/vpsadmin`:
    passed.
- Commit:
  - committed vpsadmin API/WebUI changes as `2f25ccfe4`, then amended to
    `366d8301c` after mandatory review follow-up:
    `notifications: polish delivery pages and retry failed deliveries`;
  - Overcommit pre-commit hooks passed (`Nixfmt`, `PhpCsFixer`, `RuboCop`);
  - commit-msg hooks passed with repository-local warnings about the stricter
    72-column message width; the message still satisfies the workspace
    80-column rule.
- Dev cluster update:
  - ran `devcluster update 2026-06-15-vpsadmin-events services`;
  - stopped the old manually-started webhook test server that had PID `40666`;
  - `vpsadmin-webhook-test-server.service` is active with PID `52614`;
  - local request to `http://127.0.0.1:18080/events` returns HTTP
    `202 Accepted`;
  - `systemctl list-units --state=failed --no-legend --no-pager` reports no
    failed units.
- Long integration/Playwright browser runs remain skipped until the remaining
  notification pieces are ready for a broader end-to-end pass.
- Mandatory change review:
  - launched standalone reviewer `Hubble`
    (`019edc20-e8c6-7850-9b0f-a25f4a6d85b9`) for commit `2f25ccfe4` and the
    local dev-cluster support diff;
  - blocking findings: none;
  - important finding: event detail delivery rows linked the receiver but did
    not link the receiver action, so users had to open delivery details to find
    the configured action;
  - advisory finding: the dev-cluster support diff is sound, but remains a
    local change in the shared workspace checkout because that checkout is on
    an unrelated active branch and includes unrelated dirt; keep this explicit
    until it can be landed on the appropriate workspace branch.
- Review follow-up:
  - added a `Receiver action` column to event detail delivery rows, linking to
    the receiver-action edit page;
  - updated expanded-row colspans in that table;
  - extended the Playwright assertion to require the receiver-action edit link
    in the event detail table;
  - reran `nix develop ..#webui -c php -l forms/notifications.forms.php`: no
    syntax errors;
  - reran `nix shell nixpkgs#nodejs -c node --check
    tests/playwright/webui/specs/support-pages.spec.cjs`: passed;
  - reran `nix develop .#api -c bundle exec rspec
    spec/api/resources/event_routing_spec.rb`: 18 examples, 0 failures;
  - reran `git diff --check`: passed;
  - amended vpsadmin commit to `366d8301c`; Overcommit hooks passed again.
- Mandatory review follow-up result:
  - Hubble re-checked amended commit `366d8301c`;
  - blocking findings: none;
  - important findings: none;
  - confirmed the receiver-action event-table finding is resolved;
  - residual risks unchanged: long browser/VM integration remains deferred, and
    the dev-cluster support diff is still a local workspace process item.

## 2026-06-18 template visibility follow-up

- User feedback: e-mail templates must not be a receiver-action setting.
  Users do not care which template was used; template names may appear only in
  delivery details for admins.
- Implemented in the vpsadmin worktree:
  - removed `template_name` from notification receiver actions in the schema,
    migration, API resource, model validation, WebUI forms, receiver action
    lists, and related tests;
  - added hidden `event_routes.email_template_name` metadata for migrated
    advanced mail routes, so legacy template-specific recipients still select
    the same mail template without exposing a template field to users;
  - route delivery planning copies that hidden route template into
    `event_deliveries.template_name`, preserving the dispatcher snapshot;
  - non-admin event delivery API responses now blacklist `template_name`;
  - WebUI delivery details show `Template` only for admins and only for e-mail
    deliveries with a recorded template;
  - Playwright coverage asserts the e-mail receiver-action form has no
    `template_name` input.
- Verification:
  - Ruby syntax checks for touched API/model/spec files: Syntax OK;
  - `nix develop ..#webui -c php -l forms/notifications.forms.php`: no syntax
    errors;
  - `nix shell nixpkgs#nodejs -c node --check
    tests/playwright/webui/specs/support-pages.spec.cjs`: passed;
  - `nix develop .#api -c bundle exec rspec
    spec/models/event_route_spec.rb spec/models/tasks/event_delivery_spec.rb
    spec/models/notification_receiver_action_spec.rb`: 60 examples,
    0 failures;
  - `nix develop .#api -c bundle exec rspec
    spec/api/resources/event_routing_spec.rb`: 18 examples, 0 failures;
  - `nix develop .#api -c bundle exec rubocop ...`: no offenses for the
    touched Ruby files;
  - `ruby tests/ci-selection-test.rb`: 15 runs, 54 assertions, 0 failures;
  - `git diff --check` in the vpsadmin worktree: passed.
- Note: a direct `bundle exec rubocop` run outside the Nix shell failed due to
  missing local native gems; the proper Nix-shell RuboCop run passed.
- Commit:
  - committed vpsadmin changes as `23a68e5c8`
    (`notifications: hide e-mail templates from users`);
  - Overcommit pre-commit hooks passed (`Nixfmt`, `PhpCsFixer`, `RuboCop`);
  - commit-msg hooks passed after amending the message to satisfy the
    repository text-width hook.
- Mandatory change review:
  - launched standalone reviewer `Maxwell`
    (`019edc62-6e89-7691-bedf-e5babef36bdb`) for commit `f1343078c`;
  - blocking findings: none;
  - important finding: migrated routes keep hidden
    `event_routes.email_template_name`, but user-facing route/matcher edits
    could repurpose the route while leaving that hidden template marker active.
- Review follow-up:
  - route updates now clear `email_template_name` when the parent or event
    selector changes;
  - matcher create/update/delete now clear `email_template_name` when route
    matching is changed;
  - label-only route updates preserve the hidden marker;
  - added API resource regression coverage for route selector edits and matcher
    create/update/delete;
  - reran Ruby syntax checks for `resources/event_route.rb` and
    `event_routing_spec.rb`: Syntax OK;
  - reran `nix develop .#api -c bundle exec rubocop
    lib/vpsadmin/api/resources/event_route.rb
    spec/api/resources/event_routing_spec.rb`: no offenses;
  - reran `nix develop .#api -c bundle exec rspec
    spec/api/resources/event_routing_spec.rb`: 19 examples, 0 failures;
  - reran `ruby tests/ci-selection-test.rb`: 15 runs, 54 assertions,
    0 failures;
  - reran `git diff --check`: passed.
  - amended vpsadmin commit to `23a68e5c8`; Overcommit hooks passed again.
- Mandatory review follow-up result:
  - Maxwell re-checked amended commit `23a68e5c8`;
  - blocking findings: none;
  - important findings: none;
  - advisory findings: none;
  - confirmed the hidden-template route/matcher edit finding is resolved.
- Dev cluster update:
  - ran `devcluster update 2026-06-15-vpsadmin-events services` after the
    amended commit;
  - status is `running`, `ready: yes`, topology `single`, network `bridge`;
  - `systemctl list-units --state=failed --no-legend --no-pager` on
    `services` reports no failed units;
  - webhook test server on `services` returned HTTP `202` for
    `http://127.0.0.1:18080/events`.
  - review URLs from `devcluster urls`:
    - Web UI: `https://webui.aitherdev.int.vpsfree.cz/`;
    - API: `https://api.aitherdev.int.vpsfree.cz/`;
    - Mailpit: `https://mailpit.aitherdev.int.vpsfree.cz/`;
    - admin login: `test-admin` / `testAdminPassword`;
    - user login: `test-user1` / `testUser1Password`.

## 2026-06-19 e-mail delivery preview

- Implemented e-mail delivery detail polish in `vpsadmin`:
  - HTML preview now renders as a scoped, sandboxed iframe block sized to fill
    the content column without overlapping the sidebar;
  - preview height is increased with `min-height: 650px`, `height: 70vh`, and
    `max-height: 900px`;
  - HTML source remains available but is hidden by default in a closed
    `<details>` block;
  - preview/source rows span the delivery table columns and override the
    legacy global table-cell width cap for those rows.
- Verification:
  - `nix develop ..#webui -c php -l forms/notifications.forms.php`: no syntax
    errors;
  - `nix develop ..#webui -c php -l
    tests/Regression/NotificationDeliveryHtmlDetailsTest.php`: no syntax
    errors;
  - `nix develop ..#webui -c vendor/bin/phpunit
    tests/Regression/NotificationDeliveryHtmlDetailsTest.php`: 3 tests,
    13 assertions, OK;
  - `ruby tests/ci-selection-test.rb`: 15 runs, 54 assertions, 0 failures;
  - `git diff --check`: passed.
- Test note:
  - used focused PHPUnit coverage for the helper markup and CSS contract
    because the current WebUI test notification event has no e-mail template
    and does not guarantee an HTML e-mail snapshot for Playwright.
- Commit:
  - committed vpsadmin changes as `5ea78dee7`
    (`notifications: widen e-mail delivery preview`);
  - Overcommit pre-commit hooks passed (`Nixfmt`, `PhpCsFixer`);
  - commit-msg hooks passed with text-width warnings only.
- Mandatory change review:
  - launched standalone reviewer `Hooke`
    (`019edf36-fb87-71d1-ad1c-5b3521380a40`) for commit `5ea78dee7`;
  - review result: no blocking, important, or advisory findings;
  - reviewer independently reran `git diff --check 6d9edf4..5ea78dee` and the
    focused PHPUnit regression; both passed;
  - residual risk: no live browser layout screenshot was run for this slice.
- Dev-cluster update:
  - ran `devcluster update 2026-06-15-vpsadmin-events services` after commit
    `5ea78dee7`;
  - status is `running`, `ready: yes`, topology `single`, network `bridge`;
  - `systemctl list-units --state=failed --no-legend --no-pager` on
    `services` reports no failed units;
  - `vpsadmin-api.service`, `vpsadmin-notification-dispatcher-email.service`,
    `vpsadmin-notification-dispatcher-webhook.service`, and
    `vpsadmin-webhook-test-server.service` are active;
  - webhook test server on `services` returned HTTP `202` with body
    `accepted` for `http://127.0.0.1:18080/events`;
  - review URLs remain:
    - Web UI: `https://webui.aitherdev.int.vpsfree.cz/`;
    - API: `https://api.aitherdev.int.vpsfree.cz/`;
    - Mailpit: `https://mailpit.aitherdev.int.vpsfree.cz/`;
    - admin login: `test-admin` / `testAdminPassword`;
    - user login: `test-user1` / `testUser1Password`.

## 2026-06-19 admin delivery queues

- Implemented admin-only delivery queue/log visibility in `vpsadmin`:
  - added top-level `event_delivery#index` for admins, with filters for
    queued/log state group, state, action, user, event type, route, receiver,
    receiver action, and limit;
  - queue group is limited to `prepared`, `released`, and `sending`, ordered
    by dispatcher urgency;
  - log group is limited to `sent`, `failed`, `canceled`, and `skipped`,
    ordered by latest attempt/release/update time;
  - delivery rows now expose event/user/VPS metadata and receiver/action
    labels so admin tables can link to existing detail pages;
  - WebUI Notifications sidebar now shows admin-only `Delivery queue` and
    `Delivery log` entries after `Event log`;
  - admin delivery queue/log pages list current queued work and completed
    deliveries with filters and links to event and delivery details;
  - Playwright support-page coverage now includes the two admin pages.
- Verification:
  - `nix develop .#api -c bundle exec rspec
    spec/api/resources/event_routing_spec.rb`: 20 examples, 0 failures;
  - `nix develop .#api -c bundle exec rubocop
    models/event_delivery.rb lib/vpsadmin/api/resources/event_delivery.rb
    spec/api/resources/event_routing_spec.rb`: no offenses;
  - `nix develop ..#webui -c php -l forms/notifications.forms.php`: no
    syntax errors;
  - `nix develop ..#webui -c php -l pages/page_notifications.php`: no syntax
    errors;
  - `nix shell nixpkgs#nodejs -c node --check
    tests/playwright/webui/specs/support-pages.spec.cjs`: passed;
  - `ruby tests/ci-selection-test.rb`: 15 runs, 54 assertions, 0 failures;
  - `git diff --check`: passed.
- One initial spec run failed because the new direct API spec passed index
  filters as bare query parameters instead of the resource-nested HaveAPI
  shape; the test was corrected to use `event_delivery: {...}`, matching other
  direct index specs and leaving the PHP client path unchanged.
- Commit:
  - committed vpsadmin changes as `a61385a`, then amended to `6d9edf4`
    (`notifications: add admin delivery queues`);
  - Overcommit pre-commit hooks passed (`Nixfmt`, `PhpCsFixer`, `RuboCop`);
  - commit-msg hooks passed with text-width warnings only.
- Mandatory change review:
  - launched standalone reviewer `Mendel`
    (`019edea8-8408-7fb2-9c48-33176042d042`) for commit `a61385a`;
  - blocking finding: admin-only delivery queue/log Playwright assertions were
    placed in the normal-user notification test, which would fail
    `webui#support-pages`;
  - fix: the user notification test now asserts the normal sidebar entries and
    forbidden queue/log access, while a separate admin test asserts the
    delivery queue/log sidebar entries and pages;
  - follow-up verification after the fix:
    - `nix shell nixpkgs#nodejs -c node --check
      tests/playwright/webui/specs/support-pages.spec.cjs`: passed;
    - `ruby tests/ci-selection-test.rb`: 15 runs, 54 assertions, 0 failures;
    - `git diff --check`: passed;
    - amended commit hooks passed (`Nixfmt`, `PhpCsFixer`, `RuboCop`);
  - follow-up review requested from `Mendel` for amended commit `6d9edf4`;
  - follow-up review result: previous blocking finding is resolved; no
    remaining blocking, important, or advisory findings.
- Dev cluster update:
  - ran `devcluster update 2026-06-15-vpsadmin-events services` after the
    amended commit;
  - status is `running`, `ready: yes`, topology `single`, network `bridge`;
  - `systemctl list-units --state=failed --no-legend --no-pager` on
    `services` reports no failed units;
  - `vpsadmin-api.service`, `vpsadmin-notification-dispatcher-email.service`,
    `vpsadmin-notification-dispatcher-webhook.service`, and
    `vpsadmin-webhook-test-server.service` are active;
  - webhook test server on `services` returned HTTP `202` with body
    `accepted` for `http://127.0.0.1:18080/events`;
  - an attempted unauthenticated `vpsadminctl` metadata probe returned
    `401 Unauthorized`, so it was not used as a deployment health signal.
  - review URLs from `devcluster urls`:
    - Web UI: `https://webui.aitherdev.int.vpsfree.cz/`;
    - API: `https://api.aitherdev.int.vpsfree.cz/`;
    - Mailpit: `https://mailpit.aitherdev.int.vpsfree.cz/`;
    - admin login: `test-admin` / `testAdminPassword`;
    - user login: `test-user1` / `testUser1Password`.

## 2026-06-19 delivery preview/layout follow-up

- Implemented corrective WebUI layout changes in `vpsadmin`:
  - e-mail HTML preview/source now render in a dedicated one-column table
    instead of the two-column delivery detail table;
  - the preview table has scoped CSS to use the full content width and avoid
    the legacy global `td` width cap;
  - HTML source remains collapsed by default;
  - admin Delivery queue/log index tables no longer show the wide `Target` and
    `Result` columns; those details remain available on individual delivery
    pages.
- Verification:
  - `nix develop ..#webui -c php -l forms/notifications.forms.php`: no syntax
    errors;
  - `nix develop ..#webui -c php -l
    tests/Regression/NotificationDeliveryHtmlDetailsTest.php`: no syntax
    errors;
  - `nix develop ..#webui -c vendor/bin/phpunit
    tests/Regression/NotificationDeliveryHtmlDetailsTest.php`: 4 tests,
    21 assertions, OK;
  - `ruby tests/ci-selection-test.rb`: 15 runs, 54 assertions, 0 failures;
  - `git diff --check`: passed.
- Commit:
  - committed vpsadmin changes as `dda507087`, then amended to `2fa88f421`
    (`notifications: fix delivery preview layout`);
  - Overcommit pre-commit hooks passed (`Nixfmt`, `PhpCsFixer`);
  - commit-msg hooks passed with text-width warnings only.
- Mandatory change review:
  - launched standalone reviewer `Laplace`
    (`019edf7d-7b35-7341-aa0b-ae73c16e3a4f`) for commit `dda507087`;
  - blocking finding: `support-pages.spec.cjs` still expected `Result` on the
    admin Delivery log page;
  - fix: amended the commit so the admin notification delivery queue/log
    browser test asserts the new table headers without `Target` and `Result`;
  - follow-up review requested for amended commit `2fa88f421`;
  - follow-up review result: previous blocking finding is resolved; no
    remaining blocking, important, or advisory findings;
  - reviewer independently reran `node --check` for the Playwright file and
    `git diff --check` on the reviewed range; both passed;
  - residual risk: full Playwright browser scenario not run.
- Dev-cluster update:
  - first `devcluster update 2026-06-15-vpsadmin-events services` after the
    amended commit failed while copying to the services VM with `No space left
    on device`;
  - services VM was at 100% inode use; removed only the incomplete failed-copy
    path `/nix/store/b9nkd0nf96cphbcg4dk7dy64nkw0smwf-system-path`, then ran
    `nix-store --gc`, freeing 619 store paths and 262.4 MiB;
  - retried `devcluster update 2026-06-15-vpsadmin-events services`
    successfully;
  - status is `running`, `ready: yes`, topology `single`, network `bridge`;
  - `systemctl list-units --state=failed --no-legend --no-pager` on
    `services` reports no failed units;
  - `vpsadmin-api.service`, `vpsadmin-notification-dispatcher-email.service`,
    `vpsadmin-notification-dispatcher-webhook.service`, and
    `vpsadmin-webhook-test-server.service` are active;
  - webhook test server on `services` returned HTTP `202` with body
    `accepted` for `http://127.0.0.1:18080/events`;
  - live WebUI CSS at
    `https://webui.aitherdev.int.vpsfree.cz/template/css/main.css` contains
    `#notification-delivery-html` and no filtered `width: 790px` match.

## 2026-06-19 direct event-only release slice

- Implemented in `vpsadmin` commit `76925352d`
  (`notifications: release event-only mail directly`).
- Added `VpsAdmin::API::NotificationEvents`:
  - runs event-only transaction-chain builders inside a normal database
    transaction;
  - redirects `route_event!`/`prepare_event!` to direct
    `Events.emit!(release: true)`;
  - no-ops transaction-chain concerns;
  - raises if a supposedly direct builder tries to append a real transaction
    or acquire a lock.
- Converted pure notification senders from queued transaction chains to direct
  event release:
  - OOM report notifications;
  - daily report and payments overview;
  - dataset-expanded notifications from tasks and supervisor events;
  - new login, new token, TOTP recovery-code, and failed-login reports;
  - security advisory mail;
  - outage updates while preserving the existing `[chain, result]` return
    shape with `chain = nil`.
- Incident reports now choose explicitly:
  - incidents with CPU limits or VPS actions other than `none` still use real
    transaction chains;
  - direct-only incidents are released through the direct event runner;
  - incoming incident send/reply notifications are direct;
  - API `state_id` is nil-safe for direct incident creation.
- Verification:
  - `nix develop .#api --command bash -lc 'bundle exec rspec ...'` focused
    notification/API suite: 120 examples, 0 failures;
  - `nix develop .#api --command bash -lc 'bundle exec rspec
    spec/api/plugins/outage_reports/outage_update_spec.rb
    spec/models/transaction_chains/plugins/outage_reports/update_spec.rb'`:
    22 examples, 0 failures;
  - post-review targeted run:
    `nix develop .#api --command bash -lc 'bundle exec rspec
    spec/api/resources/incident_report_spec.rb:438
    spec/models/notification_events_spec.rb'`: 3 examples, 0 failures;
  - post-review broader targeted run:
    `nix develop .#api --command bash -lc 'bundle exec rspec
    spec/api/resources/incident_report_spec.rb
    spec/models/notification_events_spec.rb
    spec/models/tasks/incident_report_spec.rb'`: 29 examples, 0 failures;
  - `nix develop .#api --command bash -lc 'bundle exec rubocop ...'` on 31
    touched Ruby files/specs: no offenses;
  - post-review RuboCop on
    `models/notification_events.rb`,
    `spec/models/notification_events_spec.rb`, and
    `spec/api/resources/incident_report_spec.rb`: no offenses;
  - `ruby -c api/models/notification_events.rb` and
    `ruby -c api/models/transaction_chains/incident_report/utils.rb`: syntax
    OK;
  - `git diff --check`: passed.
- Commit hooks:
  - first commit attempt from the ambient shell failed because the Overcommit
    gem was unavailable there;
  - retried from `nix develop`, where Overcommit is available;
  - pre-commit hooks passed (`Nixfmt`, `RuboCop`);
  - commit-msg hooks passed with text-width warnings only.
- Mandatory change review:
  - launched standalone reviewer `Boyle`
    (`019edfe5-2d69-7303-b78c-53c3852ae5b9`) for commit `b348e0163`;
  - blocking finding: the incident-report create API spec still expected a
    positive `action_state_id` for minimal direct-only incident creation;
  - advisory: add focused coverage for `NotificationEvents.run_chain`;
  - fix: amended the commit so minimal incident creation expects no
    transaction state, added a separate chain-backed create case using a
    standalone VPS fixture, and added `NotificationEvents` specs covering
    direct release and the guard against appending real transactions.
  - follow-up review requested for amended commit `76925352d`;
  - follow-up review result: previous blocking finding is resolved; no
    remaining blocking, important, or advisory findings;
  - reviewer independently reran:
    `nix develop .#api --command bash -lc 'bundle exec rspec
    spec/api/resources/incident_report_spec.rb:438
    spec/models/notification_events_spec.rb'`: 3 examples, 0 failures;
  - residual risk: long integration/dev-cluster tests and live dispatcher
    behavior remain outside this quick follow-up review.
- Dev-cluster update:
  - ran `devcluster update 2026-06-15-vpsadmin-events services` after the
    amended commit;
  - status is `running`, `ready: yes`, topology `single`, network `bridge`;
  - `systemctl list-units --state=failed --no-legend --no-pager` on
    `services` reports no failed units;
  - `vpsadmin-api.service`,
    `vpsadmin-notification-dispatcher-email.service`,
    `vpsadmin-notification-dispatcher-webhook.service`, and
    `vpsadmin-webhook-test-server.service` are active;
  - review URLs from `devcluster urls` remain:
    - Web UI: `https://webui.aitherdev.int.vpsfree.cz/`;
    - API: `https://api.aitherdev.int.vpsfree.cz/`;
    - Mailpit: `https://mailpit.aitherdev.int.vpsfree.cz/`;
    - admin login: `test-admin` / `testAdminPassword`;
    - user login: `test-user1` / `testUser1Password`.

## 2026-06-19 opt-in lifecycle events slice

- Implemented in the `vpsadmin` worktree, not yet committed:
  - event types now carry `default_routed` metadata and optional severity
    descriptions;
  - generated default routes match only default-routed event types, preserving
    the current mail-equivalent behavior while making noisy/lifecycle events
    opt-in;
  - `event_routes` gained `default_route`, `single_use`, `spent_at`, and
    `expires_at` in the existing session migration and schema;
  - active route lookup ignores spent/expired routes;
  - matched single-use routes are marked disabled/spent after routing instead
    of being deleted;
  - transaction-chain lifecycle is represented by one opt-in event type,
    `transaction_chain.state_changed`, with `state`, `previous_state`,
    `terminal`, `successful`, `failed`, chain size/progress, concern, session,
    and node parameters;
  - route metadata exposes `default_routed` and severity descriptions to the
    API and WebUI event type list;
  - users can create a single-use "notify me when done" route from a
    transaction chain; it is inserted at the top of the route list and spends
    immediately when the chain is already terminal;
  - nodectld publishes transaction-chain state changes over RabbitMQ after DB
    save, and the API supervisor consumes those messages to emit lifecycle
    events;
  - DNS transfer failures and recoveries now emit opt-in
    `dns.zone_transfer.failed` and `dns.zone_transfer.recovered` events.
- Compatibility notes:
  - default routes remain mail-compatible because only existing mail-equivalent
    event types are default-routed;
  - new transaction-chain and DNS transfer events are opt-in and should not
    spam existing users;
  - nodectld/API mixed-version operation is additive: old nodectld simply will
    not publish lifecycle messages, while new API supervisor can consume them.
- Test setup note:
  - added detached test-dependency worktree
    `worktrees/2026-06-15-vpsadmin-events/vpsadminos` at the flake-pinned
    revision `e2b5a7a987e5c57b31a67344c885c5b5dac2da7d`;
  - `libosctl` native extension was compiled there for libnodectld specs;
    the checkout only contains ignored build outputs
    `libosctl/Gemfile.lock` and `libosctl/lib/libosctl/native.so`.
- Verification:
  - `nix develop .#api --command bash -lc 'bundle exec rspec
    spec/models/event_route_spec.rb
    spec/api/resources/event_routing_spec.rb
    spec/api/resources/transaction_chain_read_spec.rb
    spec/supervisor/node/dns_transfer_log_spec.rb
    spec/supervisor/node/transaction_chain_events_spec.rb
    spec/models/transaction_chains/vps/oom_reports_spec.rb
    spec/models/transaction_chains/vps/oom_prevention_spec.rb'`:
    82 examples, 0 failures;
  - `nix develop .#api --command bash -lc 'bundle exec rspec
    spec/supervisor/node/dns_transfer_log_spec.rb'`: 4 examples, 0 failures
    after the final matcher-format edit;
  - `VPSADMINOS_PATH=worktrees/2026-06-15-vpsadmin-events/vpsadminos
    nix develop .#libnodectld --command bash -lc 'bundle exec rspec
    spec/nodectld/command_spec.rb
    spec/nodectld/remote_commands/chain_spec.rb'`: 41 examples, 0 failures;
  - Ruby syntax checks passed for touched API and libnodectld Ruby files;
  - PHP syntax passed for `webui/forms/notifications.forms.php` and
    `webui/pages/page_transactions.php`;
  - API RuboCop on 18 touched Ruby files/specs: no offenses;
  - libnodectld RuboCop on 4 touched Ruby files/specs via the API RuboCop
    bundle: no offenses;
  - `git diff --check`: passed.
- Notes:
  - `api/spec/supervisor/node/transaction_chain_events_spec.rb` is covered by
    the existing `.github/workflows/api-specs.yml` supervisor topic pattern
    `spec/supervisor/**/*_spec.rb`, so no workflow pattern update was needed.

## 2026-06-19 plan update

- Updated `plan.md` to document the revised lifecycle-event design:
  default-routed vs opt-in event types, dynamic severity descriptions,
  single `transaction_chain.state_changed` event with state parameters,
  single-use/spent routes for "notify me when done", and opt-in DNS transfer
  failed/recovered events.

## 2026-06-19 lifecycle events commit

- Committed the opt-in lifecycle events slice in `vpsadmin`:
  - amended commit `397cbaaf9`
    (`notifications: add opt-in lifecycle events`);
  - hooks run by `git commit` inside `nix develop .`: Nixfmt, PhpCsFixer,
    RuboCop, and commit-msg hooks passed.
- Mandatory change review:
  - launched standalone reviewer `Confucius`
    (`019ee055-a3cc-72e3-beda-f36e3584830e`) for commit `94b71dcab`;
  - review found one blocking STI source-class mismatch for single-use
    transaction-chain routes, important issues for route creation racing a
    terminal state change and boolean `false` matcher values, and an advisory
    about missing default receiver repair;
  - fixed by amending the commit to store transaction-chain events with stable
    `source_class = "TransactionChain"`, lock/reload the chain while creating
    the one-shot route, use key-presence checks for nested event parameters,
    and repair/create the default receiver when no receiver is selected;
  - added regressions for STI chain source matching, boolean `false` matcher
    matching, and default receiver repair;
  - sent a follow-up check to the same reviewer for amended commit
    `397cbaaf9`;
  - follow-up result: no blocking, important, or advisory findings remain;
    reviewer noted only the existing residual risk that full
    RabbitMQ/nodectld/API supervisor behavior still needs longer
    integration/dev-cluster validation.
- Post-review verification:
  - `nix develop .#api --command bash -lc 'bundle exec rspec
    spec/models/event_route_spec.rb
    spec/api/resources/transaction_chain_read_spec.rb'`: 47 examples,
    0 failures;
  - `nix develop .#api --command bash -lc 'bundle exec rspec
    spec/models/event_route_spec.rb
    spec/api/resources/event_routing_spec.rb
    spec/api/resources/transaction_chain_read_spec.rb
    spec/supervisor/node/dns_transfer_log_spec.rb
    spec/supervisor/node/transaction_chain_events_spec.rb
    spec/models/transaction_chains/vps/oom_reports_spec.rb
    spec/models/transaction_chains/vps/oom_prevention_spec.rb'`: 84 examples,
    0 failures;
  - Ruby syntax OK for touched fix files;
  - RuboCop on touched fix files: no offenses;
  - `git diff --check`: passed;
  - amend hooks passed: Nixfmt, PhpCsFixer, RuboCop, commit-msg hooks.
- Follow-up review result:
  - no blocking, important, or advisory findings remain;
  - residual risk noted by reviewer: timestamp guard assumes sane API/node wall
    clocks, and full RabbitMQ/dev-cluster validation remains outside the
    focused review.

## 2026-06-19 explicit default-routed policy

- Amended the lifecycle-events commit again:
  - new commit `14e1703b5`
    (`notifications: add opt-in lifecycle events`);
  - `VpsAdmin::API::Events.register` now requires explicit
    `default_routed:`;
  - all 44 event registrations specify `default_routed`;
  - mail-equivalent events and `user.test_notification` use
    `default_routed: true`;
  - opt-in lifecycle/DNS events remain `default_routed: false`.
- Verification:
  - Ruby syntax OK for `api/lib/vpsadmin/api/events.rb` and
    `api/spec/api/resources/event_routing_spec.rb`;
  - `nix develop .#api --command bash -lc 'bundle exec rspec
    spec/api/resources/event_routing_spec.rb
    spec/models/event_route_spec.rb'`: 46 examples, 0 failures;
  - RuboCop on touched API files: no offenses;
  - `git diff --check`: passed before amend;
  - commit hooks passed during amend: Nixfmt, PhpCsFixer, RuboCop,
    commit-msg hooks;
  - local registration scan found 44 register blocks and zero missing
    `default_routed:` keywords.
- Mandatory change review:
  - launched standalone reviewer `Noether`
    (`019ee092-d306-74f2-825e-4cff87cd5fae`) for amended commit
    `14e1703b5`;
  - review found no issue in the explicit `default_routed` amend, but flagged
    an important delayed-terminal-event edge for "notify when done" routes and
    an advisory that expired routes still counted toward `MAX_ROUTES`;
  - amended again to commit `674e005e7`;
  - fixed by publishing subsecond transaction-chain event time from nodectld,
    preferring it in the API supervisor, adding numeric
    `parameters.changed_at_timestamp`, matching one-shot routes only against
    state changes at or after route creation, and counting only active routes
    for route limits;
  - added regressions for stale terminal events not spending fresh one-shot
    routes, fresh terminal events spending them, expired routes not counting
    toward the route limit, supervisor timestamp parameters, and libnodectld
    `time_f` publication;
  - follow-up sent to reviewer `Noether`.
- Post-fix verification:
  - Ruby syntax OK for touched API/libnodectld Ruby files/specs;
  - `nix develop .#api --command bash -lc 'bundle exec rspec
    spec/api/resources/event_routing_spec.rb
    spec/api/resources/transaction_chain_read_spec.rb
    spec/supervisor/node/transaction_chain_events_spec.rb
    spec/models/event_route_spec.rb'`: 70 examples, 0 failures;
  - `VPSADMINOS_PATH=worktrees/2026-06-15-vpsadmin-events/vpsadminos
    nix develop .#libnodectld --command bash -lc 'bundle exec rspec
    spec/nodectld/command_spec.rb
    spec/nodectld/remote_commands/chain_spec.rb'`: 42 examples, 0 failures;
  - RuboCop on touched API files: no offenses;
  - RuboCop on touched libnodectld files via the API bundle: no offenses;
  - `git diff --check`: passed;
  - amend hooks passed: Nixfmt, PhpCsFixer, RuboCop, commit-msg hooks.
- Follow-up review result:
  - reviewer `Noether` found no blocking, important, or advisory findings in
    commit `674e005e7`;
  - residual risk: the one-shot timestamp guard assumes sane API/node clocks,
    and full RabbitMQ/dev-cluster validation remains outside the focused
    review.

## 2026-06-19 dev cluster reset

- Reset the dev cluster state per request because the previous database was
  missing the new `event_routes.default_route` column:
  - `dev-clusters/vpsadmin/bin/devcluster reset
    2026-06-15-vpsadmin-events`;
  - output reported the old cluster was killed after timeout and the cluster
    state was removed.
- Started a fresh bridge-network dev cluster:
  - `dev-clusters/vpsadmin/bin/devcluster start
    2026-06-15-vpsadmin-events`;
  - cluster is running and ready at PID `1045732`;
  - URLs include `https://webui.aitherdev.int.vpsfree.cz/`,
    `https://api.aitherdev.int.vpsfree.cz/`, and
    `https://adminer.aitherdev.int.vpsfree.cz/`.
- Fresh-cluster checks:
  - `devcluster status`: running, topology `single`, network `bridge`,
    ready `yes`;
  - `systemctl list-units --state=failed` on `services`: no failed units;
  - `curl -k -I https://webui.aitherdev.int.vpsfree.cz/`: HTTP 200;
  - `curl -k -I https://api.aitherdev.int.vpsfree.cz/`: HTTP 200;
  - MariaDB schema check inside `services` confirmed
    `event_routes.default_route tinyint(1) NOT NULL DEFAULT 0`.
- Command note:
  - for direct DB checks over `devcluster ssh`, pass the whole remote command
    as one quoted argument; local root socket access works inside `services`,
    while `vpsadmin` credentials printed for Adminer were rejected when tried
    directly over SSH/TCP.

## 2026-06-19 mail HTML preview sizing

- Committed focused webui fix:
  - commit `e2d621adf`
    (`webui: make notification mail preview resizable`);
  - `notifications_html_preview()` now wraps the sandboxed iframe in a
    `.notification-delivery-html-frame`;
  - notification-specific CSS removes the preview table-cell width/padding
    limits, makes the preview frame full width, and gives the frame a native
    vertical resize handle;
  - HTML source remains collapsed by default.
- Quick verification:
  - PHP syntax passed for `webui/forms/notifications.forms.php` and
    `webui/tests/Regression/NotificationDeliveryHtmlDetailsTest.php`;
  - `nix develop .#webui --command bash -lc 'cd .../webui &&
    vendor/bin/phpunit tests/Regression/NotificationDeliveryHtmlDetailsTest.php'`:
    4 tests, 26 assertions, 0 failures;
  - `git diff --check`: passed;
  - commit hooks passed from `nix develop`: Nixfmt and PhpCsFixer OK;
    commit-msg hooks passed with warnings for lines over 72 characters, while
    remaining within the workspace 80-character rule.
- Live dev-cluster verification:
  - generated a real daily report with
    `systemctl start vpsadmin-api-daily-report.service`;
  - delivery `#10` for event `#10` was sent and had an HTML body length of
    5508 bytes;
  - refreshed the running services VM with
    `dev-clusters/vpsadmin/bin/devcluster update
    2026-06-15-vpsadmin-events services`;
  - `systemctl list-units --state=failed` on `services`: no failed units;
  - `curl -k -I https://webui.aitherdev.int.vpsfree.cz/`: HTTP 200;
  - served CSS includes `.notification-delivery-html-frame`,
    `min-height: 650px`, `resize: vertical`, `padding: 0`, and
    `height: calc(100% - 12px)`;
  - one-off Chromium/Playwright smoke as `test-admin` opened delivery `#10`;
    the preview table measured 805px wide, the frame 803px, and the iframe
    801px; HTML source was collapsed; dragging the bottom-right frame handle
    grew the frame from 675px to 799px.
- Mandatory change review:
  - launched reviewer `Hilbert`
    (`019ee0e7-eaef-7e42-9f2f-9dddaae88a3e`) for commit `e2d621adf`;
  - result: no blocking, important, or advisory findings;
  - residual risks/test gaps: native resize behavior was live-checked in
    Chromium only, and the full webui Playwright suite was not run.

## 2026-06-19 monitoring event routing

- Implemented monitoring alerts on top of notification events in `vpsadmin`:
  - added `monitoring.alert` event type metadata with `default_routed: true`
    and matchable monitoring parameters such as monitor name, state, object,
    VPS, dataset, DNS transfer status, and alert timing fields;
  - extended runtime e-mail context on `Event` so transaction chains can pass
    the existing monitoring mail template, template parameters, template vars,
    and mail headers into routed e-mail delivery rendering;
  - added `route_monitoring_alert!` and monitoring helper methods to the
    monitoring alert transaction chain, preserving old Message-ID/threading
    semantics and marking template recipients as excluded for routed e-mail;
  - focused specs cover webhook routing, generated default-route e-mail
    routing, retained non-notification transactions, alert counts, and event
    type metadata exposure.
- Updated `vpsfree-cz-configuration` monitoring actions:
  - replaced direct `mail(...)` calls for user/admin monitoring alerts,
    diskspace alerts, zombie-process alerts and restart notices, rescue-mode
    alerts, and VPS dataset quota alerts with `route_monitoring_alert!`;
  - admin monitoring alerts are emitted as one event per admin account so each
    admin's own notification routes decide whether to deliver e-mail,
    webhook, or nothing;
  - old cooldown, locking, maintenance-window restart transactions, and
    closed-state skips are preserved.
- Compatibility/deployment notes:
  - no database migration is part of this slice;
  - the vpsAdmin code introducing `monitoring.alert` and
    `route_monitoring_alert!` must be deployed before this configuration
    change;
  - old vpsAdmin code remains compatible with the old configuration, and new
    vpsAdmin code remains compatible with monitoring actions that still use
    direct mail until the configuration is updated.
- Quick verification:
  - `nix develop .#api --command bash -lc 'bundle exec rubocop
    models/event.rb lib/vpsadmin/api/events.rb
    ../plugins/monitoring/api/models/transaction_chains/monitoring/alert.rb
    spec/models/transaction_chains/plugins/monitoring/alert_spec.rb
    spec/api/resources/event_routing_spec.rb'`: 5 files, no offenses;
  - `nix develop .#api --command bash -lc 'bundle exec rspec
    spec/models/transaction_chains/plugins/monitoring/alert_spec.rb
    spec/api/resources/event_routing_spec.rb:675'`: 6 examples, 0 failures;
  - `ruby -c configs/vpsadmin/api/monitoring.rb`: Syntax OK;
  - `nix develop --command bash -lc 'bundle exec rubocop
    configs/vpsadmin/api/monitoring.rb'`: 1 file, no offenses;
  - `git diff --check` passed in both changed repositories.
- Commits:
  - `vpsadmin`: `3e07b8da97ea1bbf593df410a76dfd7bbf88d56a`
    (`notifications: route monitoring alerts`);
  - `vpsfree-cz-configuration`:
    `aa2804e60f7c7efabf8eee75f7ba531ff7e9daaa`
    (`vpsadmin-config: route monitoring alerts`);
  - `vpsfree-cz-configuration`:
    `e9c1f1d97ad31e97d97e12cf6d2f8c568eda7a9c`
    (`inputs: set vpsadminProduction, vpsadminServices, vpsadminStaging to
    3e07b8da`);
  - Overcommit hooks passed for both commits. The commit-msg hook warned
    about its 72-column text-width preference, while all message lines remain
    within the workspace 80-column rule.
- Mandatory change review:
  - launched standalone reviewer `Locke`
    (`019ee11e-f49d-7571-9fb9-7fe91ae98d11`) for the monitoring routing
    slice against `vpsadmin` `e2d621adf..1585659e9` and
    `vpsfree-cz-configuration` `e0500614..aa2804e6`.
  - review result:
    - blocking: `vpsfree-cz-configuration` still pinned production,
      staging, and services vpsAdmin inputs to `f3e1ff0d`, which does not
      contain `route_monitoring_alert!` or `monitoring.alert`;
    - important: monitoring admin recipients used `level > 90`, while the app
      treats `level >= 90` as admin and should avoid suspended/soft-deleted
      accounts;
    - advisory: no smoke test currently loads the real production monitoring
      config action blocks under vpsAdmin.
- Review follow-up fixes:
  - amended `vpsadmin` monitoring commit to
    `3e07b8da97ea1bbf593df410a76dfd7bbf88d56a`;
  - `monitoring_admin_recipients` now uses active users with `level >= 90`;
  - added focused regression coverage for active level-90 admins and suspended
    admins;
  - pushed branch `2026-06-15-vpsadmin-events` to GitHub so the exact
    revision can be pinned by the configuration repository;
  - generated config input commit `e9c1f1d9`
    (`inputs: set vpsadminProduction, vpsadminServices, vpsadminStaging to
    3e07b8da`) with
    `confctl inputs channel set --commit production,staging,vpsadmin vpsadmin
    3e07b8da97ea1bbf593df410a76dfd7bbf88d56a`.
- Follow-up quick verification:
  - `nix develop .#api --command bash -lc 'bundle exec rubocop
    models/event.rb lib/vpsadmin/api/events.rb
    ../plugins/monitoring/api/models/transaction_chains/monitoring/alert.rb
    spec/models/transaction_chains/plugins/monitoring/alert_spec.rb
    spec/api/resources/event_routing_spec.rb'`: 5 files, no offenses;
  - `nix develop .#api --command bash -lc 'bundle exec rspec
    spec/models/transaction_chains/plugins/monitoring/alert_spec.rb
    spec/api/resources/event_routing_spec.rb:675'`: 7 examples, 0 failures;
  - `git diff --check` passed in `vpsadmin`;
  - `confctl inputs channel ls` shows `production`, `staging`, and
    `vpsadmin` channel vpsAdmin inputs all at `3e07b8da`.
- Follow-up mandatory review:
  - launched standalone reviewer `Volta`
    (`019ee12f-a00a-7a03-a1f1-e1130af6954b`) against final heads
    `vpsadmin` `3e07b8da` and `vpsfree-cz-configuration` `e9c1f1d9`.
  - result: no blocking or important findings;
  - advisory/residual gaps: no smoke test currently loads and executes the
    real production monitoring config action blocks under vpsAdmin, no
    dispatcher-level integration test covers a real monitoring alert through
    e-mail/webhook, and no `confctl build` or dry-activate was run for this
    slice.

## 2026-06-19 monitoring plugin ownership cleanup

- Implemented the requested cleanup in `vpsadmin`:
  - moved `monitoring.alert` event registration from core
    `api/lib/vpsadmin/api/events.rb` into the monitoring plugin metadata;
  - added plugin sysconfig key `plugin_monitoring.alert_message_id` for the
    monitoring alert Message-ID format, removing the hardcoded domain from the
    monitoring alert transaction chain;
  - kept the existing `email_vars` naming, matching the surrounding mail
    delivery code;
  - added specs proving that monitoring event metadata is available when the
    plugin is enabled and absent in core-only mode.
- Updated workspace `skills/mandatory-change-review/SKILL.md` so reviewers
  explicitly check that vpsAdmin API plugin-owned event registrations,
  sysconfig keys, routes, metrics, templates, and transaction behavior do not
  leak into core files without rationale.
- Quick verification before commit:
  - `git diff --check` passed in `vpsadmin` and workspace root;
  - `nix develop .#api --command bash -lc 'bundle exec rubocop
    lib/vpsadmin/api/events.rb ../plugins/monitoring/meta.rb
    ../plugins/monitoring/api/models/transaction_chains/monitoring/alert.rb
    spec/api/resources/event_routing_spec.rb
    spec/models/transaction_chains/plugins/monitoring/alert_spec.rb'`:
    5 files, no offenses;
  - `nix develop .#api --command bash -lc 'bundle exec rspec
    spec/models/transaction_chains/plugins/monitoring/alert_spec.rb
    spec/api/resources/event_routing_spec.rb:675
    spec/api/resources/event_routing_spec.rb:694'`: 10 examples,
    0 failures;
  - `nix develop .#api --command bash -lc 'VPSADMIN_PLUGINS=none bundle exec
    rspec spec/api/resources/event_routing_spec.rb:706'`: 1 example,
    0 failures.
- Commits/pushes:
  - amended `vpsadmin` monitoring commit to
    `542d30dccdc9440d46be72d23541ac64e40b2e13`
    (`notifications: route monitoring alerts`) and force-with-lease pushed
    branch `2026-06-15-vpsadmin-events`;
  - updated `vpsfree-cz-configuration` vpsAdmin input pin through `confctl`,
    amended the existing generated input commit to
    `322eff860c3cce1d2fee1b3ec793dbd0c2cebc93`
    (`inputs: set vpsadminProduction, vpsadminServices, vpsadminStaging to
    542d30dc`), and pushed branch `2026-06-15-vpsadmin-events`;
  - committed workspace review-skill update as
    `6117203730cab8f68c1beaaefaedf1f504622b35`
    (`skills: check vpsAdmin plugin isolation`) on the current workspace
    branch; unrelated root workspace changes remain untouched.
- Config pin verification:
  - `nix develop --command confctl inputs channel ls | rg
    'vpsadmin(Production|Staging|Services)|production|staging|vpsadmin'`
    shows `production`, `staging`, and `vpsadmin` channel vpsAdmin inputs all
    at `542d30dc`.
- Mandatory change review:
  - launched standalone reviewer `Pasteur`
    (`019ee152-23f0-7962-9c34-85f7ad9d0c91`) for the cleanup ranges
    `vpsadmin` `3e07b8da..542d30dc`,
    `vpsfree-cz-configuration` `e9c1f1d9..322eff86`, and workspace
    `aefd23f..6117203`.
  - result: no blocking, important, or advisory findings;
  - residual risks/test gaps: no long dev-cluster/dispatcher integration was
    rerun for this cleanup, no real production monitoring config smoke or
    `confctl build`/dry-activate was run, and the configurable Message-ID
    format uses existing plugin SysConfig formatting behavior without adding
    new validation.

## 2026-06-19 declarative event/action refactor follow-up

- Addressed review feedback about the monitoring config not using the new
  declarative event routing shape:
  - `vpsadmin` head:
    `b89a86424786d55db9947cb6b8ea043807e7f8f3`
    (`notifications: declare events and actions`);
  - `vpsfree-cz-configuration` head:
    `3fd73506` (`inputs: set vpsadminProduction, vpsadminServices,
    vpsadminStaging to b89a8642`);
  - config branch also contains `85434c37`
    (`vpsadmin-config: route monitoring alerts`), which updates
    `route_monitoring_alert!` calls to pass event-domain arguments plus
    variant/context instead of delivery-specific template options.
- Final fixes before pushing:
  - added missing endpoint coverage entries for
    `event.delivery.attempt#index`, `event.delivery.attempt#show`, and
    `event_delivery#index`;
  - restored `dataset_actions.action` in `api/db/schema.rb` to integer. The
    migration and model enum always used integer values; the accidental schema
    drift made test databases treat `DatasetAction#backup?` as false and broke
    VPS replace backup-plan rewiring specs.
- Local verification after final fixes:
  - `nix develop .#api --command bash -lc 'bundle exec rspec
    spec/models/transaction_chains/vps/replace/os_spec.rb:400 --seed 48339'`:
    1 example, 0 failures;
  - `nix develop .#api --command bash -lc 'bundle exec rspec
    spec/models/transaction_chains/vps/replace/os_spec.rb'`: 12 examples,
    0 failures;
  - `nix develop .#api --command bash -lc 'bundle exec rspec
    spec/models/transaction_chains/plugins/monitoring/alert_spec.rb'`:
    10 examples, 0 failures;
  - `nix develop .#api --command bash -lc 'bundle exec rspec
    spec/api/custom_routes_coverage_spec.rb
    spec/api/endpoint_coverage_spec.rb
    spec/api/generate_pending_endpoints_spec.rb'`: 2 examples, 0 failures;
  - `nix develop .#api --command bash -lc 'bundle exec rubocop --parallel
    --force-exclusion'`: 1369 files, no offenses;
  - `nix develop --command confctl inputs channel ls` shows production,
    staging, and vpsadmin channel vpsAdmin inputs all at `b89a8642`.
- Hooks/pushes:
  - `vpsadmin` amend used Overcommit from the general Nix dev shell; hooks
    passed with only commit-message width warnings;
  - `vpsadmin` branch force-with-lease pushed to GitHub:
    `f3e66b359...b89a86424`;
  - cancelled obsolete GitHub run `27849634252` for `f3e66b35`;
  - regenerated the config pin with
    `confctl inputs channel set --commit production,staging,vpsadmin vpsadmin
    b89a86424786d55db9947cb6b8ea043807e7f8f3`;
  - `vpsfree-cz-configuration` branch force-with-lease pushed to GitHub:
    `4f97f92b...3fd73506`.
- GitHub status after push:
  - `vpsadmin` `b89a8642`: RuboCop and libnodectld Specs passed;
  - `vpsadmin` `b89a8642`: API Specs and CI were still running when checked;
  - previous `f3e66b35` API Specs failed due the endpoint coverage/schema
    issues fixed above.
- Mandatory change review:
  - launched standalone reviewer `Newton`
    (`019ee1ef-a66d-7783-b715-6c59d8135bf4`) for final pushed heads:
    `vpsadmin` `b89a8642` and `vpsfree-cz-configuration` `3fd73506`.
  - result: no blocking or important findings; one advisory about unknown
    future action names degrading poorly if a future plugin/protocol action is
    disabled or unknown before validation catches it.

## 2026-06-20 final declarative refactor CI fixes

- Fixed the three API engine failures seen on pushed `vpsadmin` head
  `b89a8642`:
  - preserved the historical incident report queue error wording when rendered
    e-mail delivery preparation fails;
  - fixed the expiration warning dispatcher spec to stub `Mail#deliver!`,
    matching the dispatcher implementation;
  - fixed outage update state normalization so already-normalized enum integer
    values are not converted through the enum map again.
- Local verification:
  - `VPSADMIN_PLUGINS=none bundle exec rspec
    spec/models/transaction_chains/lifetimes/expiration_warning_spec.rb:96
    spec/models/transaction_chains/incident_report/process_spec.rb:82
    --seed 13928`: 2 examples, 0 failures;
  - `bundle exec rspec
    spec/models/transaction_chains/lifetimes/expiration_warning_spec.rb:96
    spec/models/transaction_chains/incident_report/process_spec.rb:82
    spec/models/tasks/plugins/outage_reports_spec.rb:25 --seed 64376`:
    3 examples, 0 failures;
  - `VPSADMIN_PLUGINS=none bundle exec rspec
    spec/models/transaction_chains/lifetimes/expiration_warning_spec.rb
    spec/models/transaction_chains/incident_report/process_spec.rb
    --seed 13928`: 11 examples, 0 failures;
  - `bundle exec rspec
    spec/models/transaction_chains/lifetimes/expiration_warning_spec.rb
    spec/models/transaction_chains/incident_report/process_spec.rb
    spec/models/tasks/plugins/outage_reports_spec.rb --seed 64376`:
    12 examples, 0 failures;
  - `bundle exec rubocop models/transaction_chains/incident_report/send.rb
    ../plugins/outage_reports/api/models/outage.rb
    spec/models/transaction_chains/lifetimes/expiration_warning_spec.rb
    --force-exclusion`: no offenses.
- Amended and pushed `vpsadmin` branch to
  `9ad6cf18cf34686ecef6a4890b8a4b564b8b9d47`.
- Replaced the generated config pin commit using
  `confctl inputs channel set --commit production,staging,vpsadmin vpsadmin
  9ad6cf18cf34686ecef6a4890b8a4b564b8b9d47`; new
  `vpsfree-cz-configuration` head is
  `b63ed09f617782bc24afe16774246643309cc994`.
- `confctl inputs channel ls` verifies `vpsadminProduction`,
  `vpsadminStaging`, and `vpsadminServices` all at `9ad6cf18`.
- Cancelled obsolete vpsAdmin umbrella CI run `27850541744`.
- Current vpsAdmin CI for `9ad6cf18`:
  - RuboCop passed;
  - libnodectld Specs passed;
  - API Specs and umbrella CI are still running.
- Mandatory change review:
  - closed stale reviewer `Newton`
    (`019ee1ef-a66d-7783-b715-6c59d8135bf4`);
  - launched fresh standalone reviewer `Dirac`
    (`019ee201-658f-7c73-85c5-952d091f2efe`) for final committed heads
    `vpsadmin` `9ad6cf18` and `vpsfree-cz-configuration` `b63ed09f`.

## 2026-06-20 final WebUI event type follow-up

- Mandatory reviewer `Dirac` reported no blocking or important findings for
  `vpsadmin` `9ad6cf18` plus config `b63ed09f`; one advisory noted that
  plugin-declared event types could be absent from WebUI selects backed by
  static HaveAPI parameter metadata.
- Fixed that advisory in `webui/forms/notifications.forms.php`:
  - `notifications_event_type_labels()` now builds choices from
    `event_type#index`, so plugin registrations such as `monitoring.alert`
    appear in route, matcher, log-filter, delivery-filter, and test-event UI;
  - static API metadata is left unchanged for API compatibility.
- Quick verification:
  - `php -l webui/forms/notifications.forms.php`: no syntax errors;
  - grep confirmed no remaining static `event_type` form rendering in
    `notifications.forms.php`;
  - vpsAdmin Overcommit hooks passed while amending, including Nixfmt,
    PHP CS Fixer, and RuboCop.
- Current heads:
  - `vpsadmin`: `c4ac49726be5109b47b437e07155d89af6c12f52`
    (`notifications: declare events and actions`);
  - `vpsfree-cz-configuration`:
    `977aa6f3e59fc4f46bab7771c54cd4d861f67fae`
    (`inputs: set vpsadminProduction, vpsadminServices, vpsadminStaging to
    c4ac4972`).
- Config verification:
  - `nix develop --command confctl inputs channel ls` shows
    `vpsadminProduction`, `vpsadminStaging`, and `vpsadminServices` all at
    `c4ac4972`.
- Push/CI:
  - `vpsadmin` was force-with-lease pushed to GitHub at `c4ac49726`;
  - cancelled obsolete umbrella CI run `27851226541`;
  - fresh CI for `c4ac49726` has RuboCop passed; Webui PHPUnit,
    libnodectld Specs, API Specs, and the umbrella CI were still running when
    checked.
- Mandatory change review:
  - launched standalone reviewer `Godel`
    (`019ee211-84af-7393-9d19-b31119a644f3`) for final committed heads
    `vpsadmin` `c4ac49726` and `vpsfree-cz-configuration` `977aa6f3`;
  - result: no blocking, important, or advisory findings;
  - residual risks noted by the reviewer: long integration/dev-cluster
    coverage and remaining GitHub CI still need to finish green, and
    production config must be deployed with the pinned vpsAdmin revision that
    contains `monitoring.alert` and the new `route_monitoring_alert!`.
- Pushed `vpsfree-cz-configuration` branch with force-with-lease:
  `3fd73506...977aa6f3`.
- `gh run list --branch 2026-06-15-vpsadmin-events` in
  `vpsfree-cz-configuration` returned no workflow runs.
- Final GitHub CI status check for vpsAdmin `c4ac49726`:
  - RuboCop `27851771484`: success;
  - Webui PHPUnit `27851771487`: success;
  - libnodectld Specs `27851771486`: success;
  - API Specs (topic parallel) `27851771491`: success;
  - umbrella CI `27851771495`: still in progress, running selected
    `ci`-tagged integration tests (`Run tests` step).

## 2026-06-20 CI follow-up for event tests

- Checked vpsAdmin GitHub run `27851771495` for `c4ac49726`:
  - RuboCop, Webui PHPUnit, libnodectld Specs, and API Specs were green;
  - umbrella CI failed after selected `ci` integration tests.
- Downloaded artifact `vpsadmin-test-logs-27851771495` to
  `/tmp/vpsadmin-ci-27851771495` and inspected failed logs:
  - `alerts/lifetime-and-daily-report`: expiration half succeeded and Mailpit
    received the expected expiration mail; daily report failed because the test
    still expected a transaction chain, but `NotificationEvents.run_chain`
    correctly releases event-only mail directly;
  - `tasks/auth-session-housekeeping`: failed-login reporting marked failed
    login rows as reported, but the test still expected
    `TransactionChains::User::ReportFailedLogins`; the new implementation
    emits `user.failed_logins` events directly;
  - `webui#users-self-service` and `webui#users-admin`: Playwright still
    expected removed advanced mail recipient UI (`template_recipients` and
    `role_recipients`);
  - `storage/dataset-migrate-same-node`: failed before test execution while
    building the test VM (`nix-store path ... unit-dhcpcd.service is not
    valid`), which appears unrelated to this branch.
- Amended vpsAdmin tests:
  - alert task helper now returns both new transaction chain IDs and event IDs;
  - daily report test expects direct event-only delivery instead of a chain;
  - auth/session housekeeping test counts `user.failed_logins` events and
    event deliveries instead of the removed report chain;
  - user/member Playwright coverage no longer exercises removed advanced mail
    recipient pages.
- Quick verification:
  - `nix develop --command nixfmt ...` on touched Nix test files: OK;
  - `nix shell nixpkgs#nodejs --command node --check ...` on touched CJS
    Playwright specs: OK;
  - `git diff --check`: OK;
  - vpsAdmin Overcommit hooks passed while amending, including Nixfmt,
    PHP CS Fixer, and RuboCop.
- Current heads:
  - `vpsadmin`: `9cab00885efe755e356c1414653dfcdce7900987`
    (`notifications: declare events and actions`);
  - `vpsfree-cz-configuration`:
    `e58e75307fb58e64a15b33e32f30728a2507c9c8`
    (`inputs: set vpsadminProduction, vpsadminServices, vpsadminStaging to
    9cab0088`).
- Config verification:
  - `nix develop --command confctl inputs channel ls` shows
    `vpsadminProduction`, `vpsadminStaging`, and `vpsadminServices` all at
    `9cab0088`.
- Push/CI:
  - `vpsadmin` was force-with-lease pushed to GitHub at `9cab00885`;
  - fresh vpsAdmin CI started:
    - RuboCop `27861856654`: success;
    - Webui PHPUnit `27861856668`, libnodectld Specs `27861856649`, API Specs
      `27861856659`, and umbrella CI `27861856660` were running or queued when
      checked.
- Mandatory change review:
  - launched standalone reviewer `Arendt`
    (`019ee38f-712c-73b0-a202-f145d7018b35`) for committed heads
    `vpsadmin` `9cab00885` and `vpsfree-cz-configuration` `e58e7530`;
  - result: no blocking, important, or advisory findings;
  - reviewer noted that the config pin commit is clean/generated-shaped and
    ready to push, with residual risk limited to still-running GitHub CI and
    the previous unrelated Nix store/build failure possibly recurring.
- Pushed `vpsfree-cz-configuration` branch with force-with-lease:
  `977aa6f3...e58e7530`.
- Latest vpsAdmin CI status for `9cab00885`:
  - RuboCop `27861856654`: success;
  - Webui PHPUnit `27861856668`: success;
  - libnodectld Specs `27861856649`: success;
  - API Specs `27861856659`: success;
  - umbrella CI `27861856660`: still in progress after about 3h12m, job
    `Run selected ci-tagged tests` is in step `Run tests`.

## 2026-06-20 declarative event ownership follow-up

- User feedback on the declarative refactor:
  - `api/lib/vpsadmin/api/events.rb` still mixed core vpsAdmin declarations
    with plugin events such as outages;
  - core events and plugin events should use the same declarative DSL;
  - event/action-specific delivery helpers should live with the event
    declarations instead of in central switch helpers;
  - monitoring should expose separate routable event types for alert shapes
    instead of one generic `monitoring.alert` surface.
- Implemented in `vpsadmin` worktree on top of pushed head
  `9cab00885efe755e356c1414653dfcdce7900987`:
  - moved core event definitions to `api/lib/vpsadmin/api/events/core.rb`
    and loaded them from the registry;
  - moved request, outage report, and payment event definitions into their
    plugin directories, loaded from plugin `init.rb`;
  - replaced the central plugin-aware e-mail template/vars switchboard with
    per-event `deliver :email` declarations for template name, params,
    options, default/custom targets, system-template mode, custom body, and
    vars;
  - removed runtime `Event` e-mail-template/vars accessors; persisted events
    now rebuild delivery contexts from their declarative event definitions;
  - made direct e-mail delivery detection delegate to the event declaration
    instead of hardcoded request/outage/report/custom event-type lists;
  - converted remaining event-only mail call sites to pass only domain event
    facts or typed report vars, leaving delivery-specific data in the event
    declaration;
  - split monitoring into event types such as
    `monitoring.monitor_state_changed`, `monitoring.diskspace_low`,
    `monitoring.zombie_processes`, `monitoring.vps_in_rescue`,
    `monitoring.dataset_over_quota`, and
    `monitoring.dns_secondary_transfer_failed`.
- `vpsfree-cz-configuration` and `vpsfree-mail-templates` worktrees remained
  clean for this slice.
- Untracked file `everity:` exists in the vpsAdmin worktree from outside this
  change and was intentionally left untouched.
- Quick verification:
  - Ruby syntax checks passed for the event registry and new event definition
    files;
  - touched-file RuboCop passed: 44 files, no offenses;
  - stale-reference scan found only the intentional `monitoring.alert`
    core-only assertion, the intentional old-argument rejection spec, and
    unrelated non-event `register` methods;
  - focused notification/routing specs passed:
    95 examples, 0 failures, 1 expected pending;
  - converted mail-source specs passed:
    51 examples, 0 failures;
  - `git diff --check` passed.
- Committed vpsAdmin slice:
  - `6bf3bf1e23c82115cdf2d0c151786a80cb711773`
    (`notifications: move event declarations to owners`);
  - Overcommit hooks passed during commit (`Nixfmt`, `RuboCop`);
  - commit-message hook warned only at its stricter 72-column threshold; all
    commit-message lines are within the workspace 80-column rule.
- Mandatory change review:
  - launched standalone reviewer `Avicenna`
    (`019ee488-1770-7dd1-8bb9-750d6b8aa5af`);
  - result: no blocking or important findings;
  - advisory: the pre-existing one-session core migration still contains
    plugin-template backfill policy for legacy request/payment/outage mail
    settings. This predates `6bf3bf1e2`; keep it as an explicit compatibility
    exception for the deployment migration, or move the backfill behind
    plugin-owned hooks in a later cleanup;
  - residual risk: long integration/dev-cluster tests were not rerun for this
    slice, and full-service plugin load order plus real mail rendering should
    still be covered by CI/dev-cluster validation.

## 2026-06-20 history cleanup

- User requested a branch history review and cleanup, explicitly allowing
  squashes/rewrite and requiring a backup before rewriting.
- Created and pushed backup branches before any rewrite:
  - `vpsadmin`:
    `backup/2026-06-15-vpsadmin-events-before-history-cleanup-2026-06-20`
    at `6bf3bf1e23c82115cdf2d0c151786a80cb711773`;
  - `vpsfree-cz-configuration`:
    `backup/2026-06-15-vpsadmin-events-config-before-history-cleanup-2026-06-20`
    at `e58e75307fb58e64a15b33e32f30728a2507c9c8`.
- Rewrote `vpsadmin` onto current `origin/master`
  `c75cc5d254dc9e9fec3ca7cfe97e8053a2bf71df`, preserving upstream
  dependency refreshes and the VPS chown IP-accounting fix.
- Rebuilt the vpsAdmin feature stack as 11 commits:
  - `9ed41e719` `notifications: add event routing foundation`;
  - `740ab1853` `notifications: expose routes and receivers`;
  - `53193ed3a` `notifications: dispatch event deliveries`;
  - `6e989baf8` `webui: point mail settings to notifications`;
  - `73c76bfc9` `notifications: route OOM and incident events`;
  - `4222018d9` `notifications: route user account events`;
  - `7158b206e` `notifications: route VPS notification events`;
  - `c3b99e806` `notifications: route advisory and report events`;
  - `73d3994ff` `notifications: route plugin notification events`;
  - `4d2f51651` `notifications: add opt-in operational events`;
  - `3b8e0a47d` `notifications: route monitoring alerts`.
- The rewritten history removes commits that only introduced later-replaced
  Telegram UI, integer action enums, centralized plugin event declarations,
  monitoring delivery-specific helper arguments, and narrow UI/layout fixups.
- `git diff --name-only origin/master..HEAD -- packages/... webui/...`
  verified that the rewritten feature diff no longer carries generated
  dependency lockfile reversions.
- Quick verification for rewritten `vpsadmin`:
  - `git diff --check origin/master..HEAD`: OK;
  - broad RuboCop first failed only because generated `api/db/schema.rb` was
    included in the file list;
  - rerun excluding `api/db/schema.rb` passed: 167 files, no offenses;
  - focused specs passed:
    `bundle exec rspec spec/models/event_route_spec.rb
    spec/models/notification_events_spec.rb
    spec/models/notification_receiver_action_spec.rb
    spec/models/tasks/event_delivery_spec.rb
    spec/api/resources/event_routing_spec.rb
    spec/api/resources/oom_report_rule_spec.rb
    spec/supervisor/node/oom_reports_spec.rb
    spec/models/transaction_chains/vps/update_spec.rb
    spec/models/transaction_chains/plugins/monitoring/alert_spec.rb`:
    157 examples, 0 failures, 1 expected pending.
- Force-with-lease pushed rewritten `vpsadmin` branch:
  `9cab00885...3b8e0a47d`.
- Replaced stale generated config pin commit:
  - reset `vpsfree-cz-configuration` branch to functional config commit
    `85434c37abc859998b5de5ea0e78a2618e0a12fb`;
  - ran `confctl inputs channel set --commit production,staging,vpsadmin
    vpsadmin 3b8e0a47d9ee8b3474164edea92ce9fdd8dfdc25`;
  - new generated config pin commit is
    `8d67a29c968f04582affafd8862cb915726d10ea`.
- `confctl inputs channel ls` verifies `vpsadminProduction`,
  `vpsadminStaging`, and `vpsadminServices` all at `3b8e0a47`.
- Force-with-lease pushed rewritten `vpsfree-cz-configuration` branch:
  `e58e7530...8d67a29c`.
- Current heads:
  - `vpsadmin`: `3b8e0a47d9ee8b3474164edea92ce9fdd8dfdc25`;
  - `vpsfree-cz-configuration`:
    `8d67a29c968f04582affafd8862cb915726d10ea`.
- Untracked local artifacts intentionally left untouched:
  - `vpsadmin`: `everity:`;
  - `vpsfree-cz-configuration`: `.bin/rubocop`, `.bundle/config`.

## 2026-06-20 notification dispatcher throttling commit

- Committed dispatcher throttling/concurrency slice in `vpsadmin`:
  - `ea30f6a3e27b31db1d3d456de1f2e458293cd2cf`
    (`notifications: throttle dispatcher deliveries`).
- Commit hooks passed:
  - Nixfmt: OK;
  - RuboCop: OK;
  - commit-msg hooks passed with TextWidth warnings at the hook's advisory
    72-column threshold; all lines remain within the workspace 80-column rule.
- Mandatory change review requested from standalone reviewer `Noether`
  (`019ee685-8c8a-7233-905b-e8c5e60c6fb7`) against
  `36c14c83eb2ec0643d1a673f1531cfaf37d98011..ea30f6a3e27b31db1d3d456de1f2e458293cd2cf`.
- Current `vpsadmin` head:
  `ea30f6a3e27b31db1d3d456de1f2e458293cd2cf`.
- Untracked local artifact intentionally left untouched:
  - `vpsadmin`: `everity:`.

## 2026-06-20 dispatcher throttling finalization

- Corrected current `vpsadmin` throttling head before the final amend:
  `90bebb85d08793145db5e36ffff92019892ca297`
  (`notifications: throttle dispatcher deliveries`).
- Noether follow-up review of that head:
  - Blocking: none;
  - Important: bounded backpressure made e-mail due selection too narrow
    when only one in-process slot was open, allowing a throttled same-domain
    delivery to hide later different-domain mail;
  - Important: e-mail due selection could continue scanning until the entire
    due backlog was exhausted when a large same-domain backlog existed.
- Fixed those review findings before re-amending:
  - kept in-process backpressure as the delivery cap;
  - separated delivery capacity from the e-mail due scan window;
  - bounded the e-mail scan window to a small multiple of the requested
    dispatcher limit;
  - added a read-only domain-limiter delay check so selection prefers
    currently sendable domains without consuming a rate-limit reservation.
- Added regression coverage for a one-open-slot dispatcher preferring a
  sendable `fastmail.com` delivery over an older throttled `gmail.com`
  delivery.
- Verification after the selector fix:
  - focused RSpec for sendable-domain preference, scan-past-one-domain, and
    in-process backpressure:
    3 examples, 0 failures;
  - full `spec/models/tasks/event_delivery_spec.rb`:
    47 examples, 0 failures;
  - touched-file RuboCop:
    2 files, no offenses;
  - Ruby syntax for touched files, Nix parse for notification dispatcher
    module, and `git diff --check`: OK.
- Amended the selector/backpressure follow-up into the throttling commit.
- Current `vpsadmin` head:
  `3c4cbc1fa5b60845a1c3de586272e9632cab980a`
  (`notifications: throttle dispatcher deliveries`).
- Amend hooks passed inside `nix develop`:
  - Nixfmt: OK;
  - RuboCop: OK;
  - commit-msg hooks: OK.
- Final Noether follow-up review of
  `3c4cbc1fa5b60845a1c3de586272e9632cab980a`:
  - Blocking: none;
  - Important: none;
  - Advisory: none.
- Reviewer confirmed the previous one-slot e-mail fairness and whole-backlog
  scanning findings are fixed, duplicate prevention still relies on both
  in-process tracking and the database row-lock claim gate, and the throttling
  commit history is clean.
- Residual risks accepted for this slice:
  - no real RabbitMQ/systemd shutdown integration test was run;
  - no multi-process duplicate stress test beyond the existing database claim
    semantics;
  - bounded scanning means a different-domain delivery beyond the scan window
    can still wait behind a very large same-domain backlog by design;
  - higher operator-configured concurrency still needs matching database pool
    sizing.

## 2026-06-20 dispatcher throttling CI correction

- Pushed `vpsadmin` throttling head
  `3c4cbc1fa5b60845a1c3de586272e9632cab980a`.
- Rewrote and pushed the generated `vpsfree-cz-configuration` pin commit:
  - `4817f708e4ab0e58d3204a553942420458cce469`;
  - only `flake.lock` changed;
  - `vpsadminProduction`, `vpsadminStaging`, and `vpsadminServices` pinned to
    `3c4cbc1fa5b60845a1c3de586272e9632cab980a`;
  - config backup branch remains
    `backup/2026-06-15-vpsadmin-events-config-before-throttling-pin-2026-06-20`
    at `c2cb36de366a1165dbfa270a1819fcb9bf1f4928`.
- GitHub Actions for the pushed `vpsadmin` head reported RuboCop failure
  `27883311867`. Investigated the log before rerunning:
  - CI full-repo RuboCop on Ruby 3.4 flagged two
    `Style/RedundantStructKeywordInit` offenses in
    `api/spec/models/tasks/event_delivery_spec.rb`;
  - the offenses were in the spec helper `Struct` declarations used by the
    new dispatcher throttling specs.
- Fixed by switching the fake e-mail delivery helper to positional
  `Struct` initialization and amended it into the throttling commit.
- Verification after the CI correction:
  - CI-style `bundle exec rubocop --parallel --force-exclusion`:
    1995 files inspected, no offenses;
  - focused RSpec for sendable-domain preference and throttled-domain worker
    occupancy:
    2 examples, 0 failures;
  - Ruby syntax for the touched spec and `git diff --check`: OK;
  - amend hooks inside `nix develop`: Nixfmt OK, RuboCop OK, commit-msg OK.
- Current `vpsadmin` head after the CI correction:
  `98d7d6d0eead67cd85611e0d5f17be3b869c69b9`
  (`notifications: throttle dispatcher deliveries`).
- Force-pushed corrected `vpsadmin` branch:
  `3c4cbc1fa...98d7d6d0e`.
- Rewrote and force-pushed the generated `vpsfree-cz-configuration` pin:
  - `a2aa397e663d849e92f1258d1150dbad46f16356`;
  - only `flake.lock` changed from `origin/master`;
  - merge-base with `origin/master` remains
    `e550af53968aa19ac53bf634ed389f674bd93c05`;
  - `vpsadminProduction`, `vpsadminStaging`, and `vpsadminServices` pinned to
    `98d7d6d0eead67cd85611e0d5f17be3b869c69b9`;
  - config backup branch still points to
    `c2cb36de366a1165dbfa270a1819fcb9bf1f4928`.
- GitHub Actions after the corrected push:
  - `vpsadmin` RuboCop `27883429278`: success;
  - `vpsadmin` API Specs topic parallel `27883429258`: success;
  - `vpsadmin` CI `27883429281`: still in progress, job
    `Run selected ci-tagged tests`;
  - previous failed RuboCop run `27883311867` was inspected and fixed as
    described above;
  - `vpsfree-cz-configuration` has no workflow runs listed for the branch.

## 2026-06-20 dispatcher throttling finalization

- Corrected current `vpsadmin` throttling head before the final amend:
  `90bebb85d08793145db5e36ffff92019892ca297`
  (`notifications: throttle dispatcher deliveries`).
- Noether follow-up review of that head:
  - Blocking: none;
  - Important: bounded backpressure made e-mail due selection too narrow
    when only one in-process slot was open, allowing a throttled same-domain
    delivery to hide later different-domain mail;
  - Important: e-mail due selection could continue scanning until the entire
    due backlog was exhausted when a large same-domain backlog existed.
- Fixed those review findings before re-amending:
  - kept in-process backpressure as the delivery cap;
  - separated delivery capacity from the e-mail due scan window;
  - bounded the e-mail scan window to a small multiple of the requested
    dispatcher limit;
  - added a read-only domain-limiter delay check so selection prefers
    currently sendable domains without consuming a rate-limit reservation.
- Added regression coverage for a one-open-slot dispatcher preferring a
  sendable `fastmail.com` delivery over an older throttled `gmail.com`
  delivery.
- Verification after the selector fix:
  - focused RSpec for sendable-domain preference, scan-past-one-domain, and
    in-process backpressure:
    3 examples, 0 failures;
  - full `spec/models/tasks/event_delivery_spec.rb`:
    47 examples, 0 failures;
  - touched-file RuboCop:
    2 files, no offenses;
  - Ruby syntax for touched files, Nix parse for notification dispatcher
    module, and `git diff --check`: OK.

## 2026-06-20 dispatcher throttling follow-up

- Noether reviewed `10455bb27a9addae43bd5a9c6eb61e9efe1fc12a`
  (`notifications: throttle dispatcher deliveries`) and found no duplicate
  send/call safety blocker. The advisory still relied on the row-level
  `EventDelivery#claim_delivery` gate.
- Important follow-up from the review: the domain fairness change excluded
  queued/delayed delivery IDs from the due query, but the dispatcher queue was
  unbounded. A long-running process could therefore keep reserving delayed
  e-mail deliveries while reconciliation/RabbitMQ kept calling `dispatch_due`.
- Fixed by adding dispatcher backpressure:
  - `dispatch_due` now only fetches delivery rows when in-process capacity is
    available;
  - `submit_delivery_id` refuses new IDs when queued, running, and delayed work
    already reaches the dispatcher `LIMIT`;
  - throttled e-mails still release the worker thread and wait in the delayed
    scheduler, but remain counted against in-flight process capacity until they
    are delivered or released.
- Added regression coverage that a dispatcher with limit 2 refuses a third
  queued delivery while one worker is active and one delivery is still queued.
- Verification after the fix:
  - focused RSpec for the new backpressure regression plus domain scanning:
    2 examples, 0 failures;
  - full `spec/models/tasks/event_delivery_spec.rb`:
    46 examples, 0 failures;
  - touched-file RuboCop:
    2 files, no offenses;
  - Ruby syntax for touched files, Nix parse for notification dispatcher
    module, and `git diff --check`: OK.
- Amended the backpressure fix into the dispatcher throttling commit.
- Current `vpsadmin` head:
  `90bebb85d2dd12b873a05080c91c7da1a20eaa1fa`
  (`notifications: throttle dispatcher deliveries`).
- Amend hooks passed inside `nix develop`:
  - Nixfmt: OK;
  - RuboCop: OK;
  - commit-msg hooks: OK.
- Follow-up Noether review for amended throttling commit
  `01a8dd4dc4a049c8176b05e13b93a761b39c00c8` found one blocking issue:
  worker threads treated any truthy `dispatch_delivery_id` return value as a
  throttle delay. Real success/failure paths can return truthy `update!`
  results, so workers could raise `NoMethodError` on `true > 0`; with
  `Thread.abort_on_exception = true`, this could terminate the dispatcher.
- Fixed the blocker by making `dispatch_delivery` return only a numeric delay
  or `nil` and by checking for numeric positive delays in the worker loop.
  Added regression coverage for a threaded worker result that returns `true`.
- Verification after the blocker fix:
  - `ruby -c api/lib/vpsadmin/api/notifications.rb`: OK;
  - `ruby -c api/spec/models/tasks/event_delivery_spec.rb`: OK;
  - `bundle exec rubocop lib/vpsadmin/api/notifications.rb
    spec/models/tasks/event_delivery_spec.rb`: no offenses;
  - `bundle exec rspec spec/models/tasks/event_delivery_spec.rb`:
    44 examples, 0 failures;
  - `git diff --check`: OK.
- Second follow-up Noether review for `04e9353678dbf96861e5d6a42849d1bfa8f0cf7f`
  found no blocker, but one important fairness issue: DB reconciliation and
  one-shot dispatch selected only the first due page by id, so many older
  same-domain e-mails could hide a later different-domain delivery outside
  that page.
- Fixed the fairness issue by making e-mail due-row selection domain-aware:
  newly seen recipient domains are selected before same-domain overflow, then
  the remaining batch is filled up to the requested limit. Already queued or
  delayed IDs in the same dispatcher process are excluded from reconciliation
  selection.
- Added regression coverage proving that with three older `gmail.com`
  deliveries and one newer `fastmail.com` delivery, a limit-3 selection still
  includes the `fastmail.com` row.
- Verification after the fairness fix:
  - `ruby -c api/lib/vpsadmin/api/notifications.rb`: OK;
  - `ruby -c api/spec/models/tasks/event_delivery_spec.rb`: OK;
  - `bundle exec rubocop lib/vpsadmin/api/notifications.rb
    spec/models/tasks/event_delivery_spec.rb`: no offenses;
  - targeted regression run:
    2 examples, 0 failures;
  - `bundle exec rspec spec/models/tasks/event_delivery_spec.rb`:
    45 examples, 0 failures;
  - `nix-instantiate --parse
    nixos/modules/vpsadmin/notification-dispatcher.nix`: OK;
  - `git diff --check`: OK.
- Noether review result for the throttling commit:
  - blocking findings: none;
  - important finding: a FIFO worker queue could let same-domain throttled
    e-mails occupy all workers and delay unrelated recipient domains;
  - advisory finding: domain and worker throttles are charged before
    `claim_delivery`, so a stale or already-claimed row can consume a throttle
    slot.
- Follow-up fix:
  - added a delayed scheduler for throttled e-mail delivery ids, keeping those
    ids reserved inside the dispatcher process while workers remain available
    for other domains;
  - added a regression spec proving a blocked `gmail.com` backlog does not
    stop a `fastmail.com` delivery from starting with available concurrency.
- Decision on the advisory:
  - accepted the pre-claim throttle reservation tradeoff for now. Sleeping
    after `claim_delivery` would hold rows in `sending` during throttles and
    can interact badly with `CLAIM_TIMEOUT`, making duplicate sends more
    likely if delays are long or the worker stalls.
- Verification after the follow-up fix:
  - `ruby -c api/lib/vpsadmin/api/notifications.rb`: OK;
  - `ruby -c api/spec/models/tasks/event_delivery_spec.rb`: OK;
  - `bundle exec rubocop lib/vpsadmin/api/notifications.rb
    spec/models/tasks/event_delivery_spec.rb`: no offenses;
  - `bundle exec rspec spec/models/tasks/event_delivery_spec.rb`:
    43 examples, 0 failures;
  - `nix-instantiate --parse
    nixos/modules/vpsadmin/notification-dispatcher.nix`: OK;
  - `git diff --check`: OK.

## 2026-06-20 notification dispatcher throttling slice

- Implemented dispatcher concurrency and throttling in `vpsadmin`:
  - e-mail dispatcher default concurrency is 2 workers;
  - webhook dispatcher default concurrency is 4 workers;
  - e-mail workers keep a configurable 1-second default delay between
    delivery starts by the same worker;
  - e-mail recipient domains from To, Cc, and Bcc are throttled to a
    configurable 1-second default interval per dispatcher process;
  - in-process queued/running delivery IDs are deduplicated so RabbitMQ
    wakeups and database reconciliation do not submit the same delivery twice
    to one dispatcher process.
- Duplicate-safety decision:
  - retained existing retry semantics for uncertain send/call outcomes;
  - concurrency duplicates are prevented by the existing database
    `claim_delivery` row lock plus the new in-process ID deduplication.
- Nix module options added under
  `vpsadmin.notificationDispatcher.email` and `.webhook`; generated
  `notifications.yml` now includes the new action concurrency/throttle keys.
- Verification:
  - `ruby -c api/lib/vpsadmin/api/notifications.rb`;
  - `ruby -c api/spec/models/tasks/event_delivery_spec.rb`;
  - `nix develop .#api --command bash -lc 'bundle exec rubocop lib/vpsadmin/api/notifications.rb spec/models/tasks/event_delivery_spec.rb'`;
  - `nix develop .#api --command bash -lc 'bundle exec rspec spec/models/tasks/event_delivery_spec.rb'`;
  - `nix-instantiate --parse nixos/modules/vpsadmin/notification-dispatcher.nix`;
  - `git diff --check`.
- Focused spec result: 42 examples, 0 failures.
- Untracked local artifact intentionally left untouched:
  - `vpsadmin`: `everity:`.

## 2026-06-20 final history cleanup review

- Launched fresh mandatory review after the final pushed heads:
  - reviewer `Nash` (`019ee5a2-bd2d-7e72-b47b-451bf3271d76`);
  - reviewed `vpsadmin` `36c14c83eb2ec0643d1a673f1531cfaf37d98011`
    and `vpsfree-cz-configuration`
    `c2cb36de366a1165dbfa270a1819fcb9bf1f4928`.
- Review result:
  - Blocking: none;
  - Important: none;
  - Advisory: none.
- Reviewer specifically verified that the previous config blocker is resolved:
  - config merge-base is
    `e550af53968aa19ac53bf634ed389f674bd93c05`;
  - config branch is exactly one commit ahead;
  - config diff is only `flake.lock`;
  - only `vpsadminProduction`, `vpsadminServices`, and
    `vpsadminStaging` changed, all pinned to
    `36c14c83eb2ec0643d1a673f1531cfaf37d98011`.
- Reviewer also verified that pushed refs match local heads, both backup
  branches exist at the recorded old heads, and vpsAdmin is the intended
  11-commit series from `origin/master` with no extra fixup/churn commits.
- Final-head GitHub CI status when recorded:
  - vpsAdmin RuboCop `27875370918`: success;
  - vpsAdmin Webui PHPUnit `27875370921`: success;
  - vpsAdmin libnodectld Specs `27875370925`: success;
  - vpsAdmin API Specs topic parallel `27875370920`: success;
  - vpsAdmin umbrella CI `27875370926`: still in progress, with job
    `Run selected ci-tagged tests` running;
  - `vpsfree-cz-configuration` has no workflow runs for the branch.
- Residual risk/test gap:
  - long selected integration coverage is still running on GitHub;
  - deployment ordering still matters: nodectld/libnodectld release handling
    must be deployed before API code emits the new event-delivery transaction
    type.

## 2026-06-20 history cleanup CI/review corrections

- vpsAdmin CI for the first cleaned head `3b8e0a47` found two API spec
  regressions in the rewritten history:
  - `spec/models/tasks/event_delivery_spec.rb` depended on the requests
    plugin helper in a core-only API topic job;
  - `spec/models/transaction_chains/dataset/migrate_spec.rb` still expected
    the removed `email_vars` routing argument.
- Fixed and autosquashed those changes into the existing cleaned commits:
  - `notifications: dispatch event deliveries` now uses a core
    `incident_report.reply` direct custom e-mail delivery for the direct retry
    spec;
  - `notifications: route VPS notification events` now passes affected VPSes
    as a transient typed event argument for dataset migration mail rendering,
    while persisted event parameters keep only the bounded sample.
- Quick verification after the fix, before autosquash:
  - targeted rerun of the two failed spec areas:
    3 examples, 0 failures;
  - focused event-system specs including dataset migration:
    166 examples, 0 failures, 1 expected pending;
  - touched-file RuboCop:
    4 files, no offenses;
  - `git diff --check`: OK.
- Overcommit hooks passed for the two temporary fixup commits; autosquash
  completed cleanly.
- Re-pushed `vpsadmin` with force-with-lease:
  `3b8e0a47d...36c14c83e`.
- Updated cleaned vpsAdmin stack:
  - `9ed41e719` `notifications: add event routing foundation`;
  - `740ab1853` `notifications: expose routes and receivers`;
  - `07e4722ee` `notifications: dispatch event deliveries`;
  - `4e3b7670b` `webui: point mail settings to notifications`;
  - `6a14c47d9` `notifications: route OOM and incident events`;
  - `6aa4e9ad5` `notifications: route user account events`;
  - `e8cede341` `notifications: route VPS notification events`;
  - `588295cde` `notifications: route advisory and report events`;
  - `0cfc9a3c5` `notifications: route plugin notification events`;
  - `88fe83620` `notifications: add opt-in operational events`;
  - `36c14c83e` `notifications: route monitoring alerts`.
- First mandatory review pass (`Planck`,
  `019ee590-cd93-7861-bf55-2c7c932beaca`) found one blocking issue in
  `vpsfree-cz-configuration`: the generated pin commit had been replayed from
  old base `e0500614` instead of current `origin/master` `e550af53`, which
  would have rolled back unrelated input/package updates.
- Fixed config branch:
  - reset the feature branch with `git reset --keep origin/master`;
  - ran `confctl inputs channel set --commit production,staging,vpsadmin
    vpsadmin 36c14c83eb2ec0643d1a673f1531cfaf37d98011`;
  - new generated config pin commit is
    `c2cb36de366a1165dbfa270a1819fcb9bf1f4928`.
- Config verification:
  - merge-base of `origin/master` and `HEAD` is now
    `e550af53968aa19ac53bf634ed389f674bd93c05`;
  - `git diff --name-only origin/master..HEAD` shows only `flake.lock`;
  - `git diff --check origin/master..HEAD`: OK;
  - `confctl inputs channel ls` shows `vpsadminProduction`,
    `vpsadminStaging`, and `vpsadminServices` all at `36c14c83`.
- Re-pushed `vpsfree-cz-configuration` with force-with-lease:
  `8d67a29c...c2cb36de`.
- Current heads:
  - `vpsadmin`: `36c14c83eb2ec0643d1a673f1531cfaf37d98011`;
  - `vpsfree-cz-configuration`:
    `c2cb36de366a1165dbfa270a1819fcb9bf1f4928`.
- Untracked local artifacts intentionally left untouched:
  - `vpsadmin`: `everity:`;
  - `vpsfree-cz-configuration`: `.bin/rubocop`, `.bundle/config`.

## 2026-06-20 notification dispatcher throttling commit

- Committed dispatcher throttling/concurrency slice in `vpsadmin`:
  - `ea30f6a3e27b31db1d3d456de1f2e458293cd2cf`
    (`notifications: throttle dispatcher deliveries`).
- Commit hooks passed:
  - Nixfmt: OK;
  - RuboCop: OK;
  - commit-msg hooks passed with TextWidth warnings at the hook's advisory
    72-column threshold; all lines remain within the workspace 80-column rule.
- Mandatory change review requested from standalone reviewer `Noether`
  (`019ee685-8c8a-7233-905b-e8c5e60c6fb7`) against
  `36c14c83eb2ec0643d1a673f1531cfaf37d98011..ea30f6a3e27b31db1d3d456de1f2e458293cd2cf`.
- Current `vpsadmin` head:
  `ea30f6a3e27b31db1d3d456de1f2e458293cd2cf`.
- Untracked local artifact intentionally left untouched:
  - `vpsadmin`: `everity:`.

## 2026-06-20 dispatcher throttling finalization

- Corrected current `vpsadmin` throttling head before the final amend:
  `90bebb85d08793145db5e36ffff92019892ca297`
  (`notifications: throttle dispatcher deliveries`).
- Noether follow-up review of that head:
  - Blocking: none;
  - Important: bounded backpressure made e-mail due selection too narrow
    when only one in-process slot was open, allowing a throttled same-domain
    delivery to hide later different-domain mail;
  - Important: e-mail due selection could continue scanning until the entire
    due backlog was exhausted when a large same-domain backlog existed.
- Fixed those review findings before re-amending:
  - kept in-process backpressure as the delivery cap;
  - separated delivery capacity from the e-mail due scan window;
  - bounded the e-mail scan window to a small multiple of the requested
    dispatcher limit;
  - added a read-only domain-limiter delay check so selection prefers
    currently sendable domains without consuming a rate-limit reservation.
- Added regression coverage for a one-open-slot dispatcher preferring a
  sendable `fastmail.com` delivery over an older throttled `gmail.com`
  delivery.
- Verification after the selector fix:
  - focused RSpec for sendable-domain preference, scan-past-one-domain, and
    in-process backpressure:
    3 examples, 0 failures;
  - full `spec/models/tasks/event_delivery_spec.rb`:
    47 examples, 0 failures;
  - touched-file RuboCop:
    2 files, no offenses;
  - Ruby syntax for touched files, Nix parse for notification dispatcher
    module, and `git diff --check`: OK.

## 2026-06-20 dispatcher throttling final pushed state

- Final pushed `vpsadmin` head:
  `98d7d6d0eead67cd85611e0d5f17be3b869c69b9`
  (`notifications: throttle dispatcher deliveries`).
- Final pushed `vpsfree-cz-configuration` head:
  `a2aa397e663d849e92f1258d1150dbad46f16356`
  (`inputs: set vpsadminProduction, vpsadminServices, vpsadminStaging to 98d7d6d0`).
- Config backup branch remains pushed at the pre-rewrite pin:
  `backup/2026-06-15-vpsadmin-events-config-before-throttling-pin-2026-06-20`
  -> `c2cb36de366a1165dbfa270a1819fcb9bf1f4928`.
- Final config verification:
  - merge-base with `origin/master`:
    `e550af53968aa19ac53bf634ed389f674bd93c05`;
  - diff from `origin/master` changes only `flake.lock`;
  - `confctl inputs channel ls` shows `vpsadminProduction`,
    `vpsadminStaging`, and `vpsadminServices` at `98d7d6d0`.
- Local untracked config artifacts intentionally left untouched:
  `.bin/`, `.bundle/`, `.swp`.
- GitHub Actions final branch status when last checked:
  - `vpsadmin` RuboCop `27883429278`: success;
  - `vpsadmin` API Specs topic parallel `27883429258`: success;
  - `vpsadmin` CI `27883429281`: still running the selected ci-tagged
    integration job;
  - previous RuboCop failure `27883311867` was inspected, fixed, and replaced
    by the successful RuboCop run above;
  - no `vpsfree-cz-configuration` workflow runs were listed for this branch.

## 2026-06-21 Telegram planning pause

- User requested a reviewable implementation plan before continuing Telegram
  work.
- Added review draft section `Telegram and generic template plan` to
  `work/2026-06-15-vpsadmin-events/plan.md`.
- Implementation work is paused pending plan review.
- A local uncommitted Telegram prototype exists in the `vpsadmin` worktree and
  must not be treated as approved until the plan is accepted or revised.
- Quick checks already run on that prototype before the pause:
  - Ruby syntax for touched Ruby files: OK;
  - PHP syntax for touched WebUI files: OK;
  - Nix parse for the notification dispatcher module: OK;
  - `git diff --check`: OK;
  - touched-file RuboCop in the API Nix shell: OK.

## 2026-06-21 Telegram implementation

- User approved proceeding with the plan.
- Official Telegram Bot API documentation was checked while resuming:
  - `getUpdates` supports offsets, 1-100 limits, and long-poll timeout;
  - `getUpdates` does not work while an outgoing webhook is configured;
  - `setWebhook` configures Telegram to POST updates to a public HTTPS URL;
  - `sendMessage` is the outbound Bot API method used for delivery.
- Implemented in `vpsadmin`:
  - new Telegram receiver action `telegram`, backed by the existing generic
    notification receiver action/delivery schema;
  - Telegram action validation requires custom target kind;
  - pairing tokens are single-use, expire after 24 hours, and store token
    creation time in action `config` without a schema change;
  - direct edits to Telegram target/action clear verification and create a new
    pairing token;
  - bot-mediated pairing stores the Telegram private chat ID and preserves
    verification;
  - `VpsAdmin::API::TelegramBot` posts JSON to the Bot API, taking the token
    from explicit config, environment, or a token file;
  - event routing prepares Telegram deliveries only for linked and verified
    receiver actions;
  - Telegram delivery payloads are snapshotted and kept concise: severity,
    subject, event type, optional VPS reference, and optional WebUI event link;
  - dispatcher support for action `telegram` with its own queue/routing key,
    concurrency setting, retry handling, provider response logging, and
    provider message ID capture;
  - `vpsadmin:event_delivery:telegrams` and
    `vpsadmin:telegram:poll_pairing_updates` rake tasks;
  - WebUI support for Telegram receiver actions, pairing command display,
    pairing-token rotation, delivery status labels, and Telegram delivery
    detail;
  - Nix notification dispatcher options for Telegram concurrency, bot token
    file, API base URL, and polling bounds;
  - CI selection rules now map notification runtime files to the alerts/support
    integration tags.
- Implemented in `vpsadmin` mail-template component:
  - added `mail_templates/bin/vpsadmin-notification-templates` as a compatible
    alias for the existing uploader;
  - updated the component README to describe notification templates while
    keeping the e-mail format and old command supported.
- Implemented in `vpsfree-mail-templates`:
  - README now presents the repository as vpsAdmin notification templates while
    clarifying that current files are e-mail templates;
  - flake description/dev shell now use notification-template wording;
  - dev shell provides both `vpsadmin-mail-templates` and
    `vpsadmin-notification-templates`;
  - Rake task description now says notification templates, with optional
    `INSTALLER` override defaulting to the old command.
- Compatibility/deployment notes:
  - no table, API resource, or Ruby model rename was done in this slice;
  - old `mail_template` API/DB/model names remain the compatibility surface;
  - Telegram is opt-in through dispatcher action/config and bot token file;
  - rollback leaves Telegram receiver actions/deliveries in the DB, but old
    e-mail and webhook behavior remains usable;
  - production can test pairing with polling before any public webhook endpoint
    exists.
- Verification after implementation:
  - Ruby syntax for touched Ruby files and new alias binary: OK;
  - PHP syntax for touched WebUI files: OK;
  - Nix parse for vpsAdmin notification dispatcher module: OK;
  - `git diff --check` in `vpsadmin`: OK;
  - `ruby tests/ci-selection-test.rb`: 15 runs, 54 assertions, 0 failures;
  - touched-file RuboCop in the API Nix shell: 13 files, no offenses;
  - focused API specs:
    `bundle exec rspec spec/models/notification_receiver_action_spec.rb
    spec/models/tasks/telegram_spec.rb
    spec/lib/vpsadmin/api/telegram_bot_spec.rb
    spec/models/tasks/event_delivery_spec.rb
    spec/api/resources/event_routing_spec.rb`
    passed: 95 examples, 0 failures, 1 expected pending;
  - `vpsfree-mail-templates` Ruby syntax for `Rakefile`: OK;
  - `vpsfree-mail-templates` flake parse: OK;
  - `nix shell nixpkgs#nixfmt-rfc-style -c nixfmt --check flake.nix`: OK;
  - `git diff --check` in `vpsfree-mail-templates`: OK.
- Commits created after verification:
  - `vpsadmin`
    `7d6a2edf7c6c98f53c91e9b750c41d799bb32c62`
    (`notifications: add Telegram delivery`);
  - `vpsadmin`
    `b0ff2aa5a1894dfe07d6ddd45d7fb89357d0f196`
    (`mail_templates: add notification template alias`);
  - `vpsfree-mail-templates`
    `1b659d73d7db87f9464fd165842fe0eaae4d5a89`
    (`docs: present templates as notifications`).
- Overcommit hooks were installed and active for `vpsadmin`; both vpsAdmin
  commits passed pre-commit and commit-msg hooks.
- `vpsfree-mail-templates` has no declared hook framework in the worktree.
- Mandatory change review requested from standalone reviewer `Fermat`
  (`019ee9a8-43ba-7250-92a9-05785a388a9e`) against:
  - `vpsadmin`
    `98d7d6d0eead67cd85611e0d5f17be3b869c69b9..b0ff2aa5a1894dfe07d6ddd45d7fb89357d0f196`;
  - `vpsfree-mail-templates`
    `7da522e060fc18d5426e1dd6cd305b6847faf5ed..1b659d73d7db87f9464fd165842fe0eaae4d5a89`.
- Mandatory change review result:
  - Blocking: none;
  - Important: none;
  - Advisory: none.
- Reviewer residual risks/test gaps:
  - no live Telegram Bot API or dev-cluster smoke test has run yet for
    `/start <token>` pairing plus `sendMessage` delivery;
  - no browser-level WebUI test covers creating a Telegram receiver action,
    rotating the pairing token, or viewing Telegram delivery detail;
  - production pairing is currently a rake polling task rather than a
    dedicated service/webhook path, so rollout needs an explicit operator
    workflow for scheduling it with bot token config;
  - mixed-version behavior is additive, but old code only ignores unknown
    `telegram` actions/deliveries; editing those rollback-created records is
    not meaningfully supported until new code is restored.
- Pushed branches after review:
  - `vpsadmin`
    `2026-06-15-vpsadmin-events`
    `98d7d6d0e..b0ff2aa5a`;
  - `vpsfree-mail-templates`
    `2026-06-15-vpsadmin-events`
    created at `1b659d73d7db87f9464fd165842fe0eaae4d5a89`.
- The first vpsAdmin push attempt from the ambient shell failed before
  sending refs because the Overcommit push hook could not find the
  `overcommit` gem; reran the same push from `nix develop`, where hook
  dependencies are installed, and it succeeded.
- GitHub Actions observed after push:
  - `vpsadmin` run IDs started for commit `b0ff2aa5a`:
    API Specs topic parallel `27901259849`, CI `27901259846`,
    Webui PHPUnit `27901259852`, RuboCop `27901259850`;
  - no workflow runs were listed for the `vpsfree-mail-templates` branch.
- GitHub Actions status after monitoring:
  - `vpsadmin` RuboCop `27901259850`: success;
  - `vpsadmin` Webui PHPUnit `27901259852`: success;
  - `vpsadmin` API Specs topic parallel `27901259849`: success;
  - `vpsadmin` CI `27901259846`: still running selected ci-tagged tests
    when last checked;
  - `vpsfree-mail-templates`: no branch workflow runs listed.

## Notification Template Rename Implementation Checkpoint

- User requested replacing the compatibility-alias plan with a direct redesign:
  no legacy mail-template source names, generic notification-template models
  and API resources, and protocol-aware template files.
- User also requested using the shared body part name `text` instead of mixing
  `plain` for e-mail and `text` for Telegram.
- User clarified that source code should not mention an unimplemented compact
  protocol yet. Source scans in both changed repositories are clean for those
  terms.
- Updated `plan.md` to describe future protocols generically and to record the
  direct rename/deployment behavior instead of the older additive alias plan.
- Implemented in `vpsadmin`:
  - renamed mail-template models/resources/uploader to notification-template
    names, with e-mail-specific recipient names where appropriate;
  - added
    `api/db/migrate/20260615100000_rename_mail_templates_to_notification_templates.rb`
    before the event migration so fresh databases create the generic schema in
    the intended order;
  - added `protocol` and `options` to notification template variants, with
    current protocols `email` and `telegram`;
  - renamed event route template references to generic `template_name`;
  - moved built-in and plugin templates to
    `notification_templates/templates/<name>/<protocol>/<lang>.<part>.erb`;
  - e-mail subjects are now ERB files under `email/<lang>.subject.erb`;
  - e-mail and Telegram text bodies both use `<lang>.text.erb`;
  - generated concise Telegram template bodies for current built-in and plugin
    event-backed templates;
  - updated Nix, release task, API specs, workflow topic paths, and local
    helper skill references to the new names.
- Implemented in `vpsfree-mail-templates`:
  - moved template directories under `templates/<name>/`;
  - moved e-mail files under `email/`, renaming `.plain.erb` to `.text.erb`;
  - moved subjects out of `meta.rb` into `email/<lang>.subject.erb`;
  - added `telegram/<lang>.text.erb` variants;
  - redesigned `meta.rb` around `template` and `protocol :email` blocks;
  - renamed docs, flake wrapper, and rake usage to
    `vpsadmin-notification-templates`.
- Verification after implementation:
  - `vpsadmin` Ruby syntax sweep over changed Ruby files: OK;
  - `vpsadmin` ERB compile check over 204 built-in/plugin notification
    templates: OK;
  - `vpsadmin` `git diff --check`: OK;
  - `vpsadmin` focused resource/model specs:
    `bundle exec rspec spec/models/notification_templates_spec.rb
    spec/api/resources/notification_template_spec.rb
    spec/api/resources/email_recipient_spec.rb
    spec/api/resources/user_email_role_recipient_spec.rb
    spec/api/resources/user_notification_template_recipient_spec.rb
    spec/api/resources/mail_log_spec`
    passed: 166 examples, 0 failures;
  - `vpsadmin` event routing/delivery/lifecycle specs:
    `bundle exec rspec spec/models/event_route_spec.rb
    spec/models/tasks/event_delivery_spec.rb
    spec/api/resources/event_routing_spec.rb
    spec/api/resources/lifecycle_bypass_spec.rb`
    passed: 120 examples, 0 failures, 1 pending;
  - `vpsadmin` helper-rename follow-up specs:
    `bundle exec rspec spec/models/security_advisory_spec.rb
    spec/models/notification_events_spec.rb
    spec/models/transaction_chains/plugins/requests/create_spec.rb`
    passed: 13 examples, 0 failures;
  - `vpsfree-mail-templates` Ruby syntax checks for `Rakefile` and
    `templates/user_create/meta.rb`: OK;
  - `vpsfree-mail-templates` ERB compile check over 396 template files: OK;
  - `vpsfree-mail-templates` `git diff --check`: OK.
- Dev cluster deployment/testing has not been run for this template rename
  slice. The prior Telegram implementation can be tested from a dev cluster,
  but this rename still needs commit, mandatory change review, and then any
  requested integration/dev-cluster smoke test.

## Notification Template Rename Commits

- Created commits:
  - `vpsadmin`
    `d3b2766cf520bcf332c5bfddcd15f5235b5536c8`
    (`notification_templates: make templates protocol-aware`);
  - `vpsfree-mail-templates`
    `f46694bedb72434ea942b54da716d56000efe86e`
    (`templates: redesign layout for notification protocols`).
- `vpsadmin` Overcommit hooks were installed and active. The first commit
  attempt failed on correctable RuboCop offenses. Applied `bundle exec rubocop
  -A` to the touched files, restaged, and the second commit passed pre-commit
  hooks (`Nixfmt`, `RuboCop`) and commit-msg hooks with non-blocking 72-column
  warnings only. All commit-message lines remain within the workspace
  80-column limit.
- `vpsfree-mail-templates` has no declared hook framework in the worktree.
- Post-commit verification:
  - `vpsadmin` committed Ruby syntax sweep: OK, 162 files;
  - `vpsadmin` built-in/plugin notification-template ERB compile: OK, 204
    files;
  - `vpsadmin` focused specs in the API Nix shell:
    `bundle exec rspec spec/models/notification_templates_spec.rb
    spec/api/resources/notification_template_spec.rb
    spec/api/resources/email_recipient_spec.rb
    spec/api/resources/user_email_role_recipient_spec.rb
    spec/api/resources/user_notification_template_recipient_spec.rb
    spec/api/resources/mail_log_spec.rb spec/models/event_route_spec.rb
    spec/models/tasks/event_delivery_spec.rb
    spec/api/resources/event_routing_spec.rb
    spec/api/resources/lifecycle_bypass_spec.rb
    spec/models/security_advisory_spec.rb
    spec/models/notification_events_spec.rb
    spec/models/transaction_chains/plugins/requests/create_spec.rb`
    passed: 299 examples, 0 failures, 1 expected pending;
  - `vpsfree-mail-templates` Ruby syntax checks for `Rakefile` and
    `templates/user_create/meta.rb`: OK;
  - `vpsfree-mail-templates` ERB compile check: OK, 396 files;
  - `find -L templates -type l` found no broken symlinks;
  - workspace scan across plan, state, and both changed source trees found no
    unimplemented compact-protocol terms.
- Mandatory standalone change review by `Arendt`
  (`019eeb0b-a3f8-7d02-a79d-c1079fd46aa2`) found:
  - blocking: stale WebUI `mail_role_recipient` /
    `mail_template_recipient` references and legacy redirect aliases;
  - important: `vpsfree-mail-templates` `flake.lock` pinned a vpsAdmin
    revision without the renamed uploader;
  - advisory: notes still used old future-protocol wording.
- Follow-up fixes:
  - amended `vpsadmin` commit to use `email_role_recipient` in the member
    edit page, delete obsolete recipient redirect aliases, delete the dead
    template-recipient form, and update the XSS regression test wording;
  - verified changed PHP files with `php -l` in the WebUI Nix shell;
  - ran `composer --working-dir=webui test -- --filter XssReportSinksTest`,
    passing 1 test / 24 assertions;
  - pushed amended `vpsadmin` branch to
    `d3b2766cf520bcf332c5bfddcd15f5235b5536c8`;
  - updated `vpsfree-mail-templates` `flake.lock` to pin the pushed vpsAdmin
    commit and amended/pushed the template repo commit to
    `f46694bedb72434ea942b54da716d56000efe86e`;
  - verified `nix develop` in `vpsfree-mail-templates` resolves
    `vpsadmin-notification-templates` and prints its usage;
  - re-ran `vpsfree-mail-templates` syntax/ERB/broken-symlink checks;
  - re-ran scans for unimplemented compact-protocol terms and old
    template/uploader names in current code paths, excluding historical
    migrations and changelog/release entries where relevant.
- GitHub Actions after amended push:
  - `vpsadmin` RuboCop `27911139311`: success;
  - `vpsadmin` Webui PHPUnit `27911139304`: success;
  - `vpsadmin` libnodectld Specs `27911139307`: success;
  - `vpsadmin` API Specs topic parallel `27911139291`: success;
  - `vpsadmin` CI `27911139299`: in progress in job `Run selected
    ci-tagged tests`, step `Run tests`, when last checked;
  - `vpsfree-mail-templates`: no branch workflow runs listed.

## Dev Cluster Deployment Retry

- Dev cluster status before deployment:
  - slug: `2026-06-15-vpsadmin-events`;
  - topology: `single`;
  - network: `bridge`;
  - status: running and ready.
- Rebuilt packaged vpsAdmin gems with
  `nix develop -c rake vpsadmin:gems`.
- First services update attempted with
  `dev-clusters/vpsadmin/bin/devcluster update
  2026-06-15-vpsadmin-events services`.
- The update built and copied the new services closure, then failed during
  `switch-to-configuration` because `vpsadmin-database-setup.service` failed
  in `db:migrate`:
  - `NameError: uninitialized constant
    RenameMailTemplatesToNotificationTemplates`;
  - ActiveRecord derived the old class name from the migration filename
    `20260615100000_rename_mail_templates_to_notification_templates.rb`;
  - the migration class had already been renamed to
    `RenameNotificationTemplateTables`.
- Services VM disk/inode check after the failed switch showed `/` and
  `/nix/store` at about 91% space used and 20% inode use, so this was not the
  earlier inode-exhaustion problem.
- Fixed the deployment blocker in `vpsadmin` by amending the notification
  template commit:
  - renamed the migration file to
    `api/db/migrate/20260615100000_rename_notification_template_tables.rb`;
  - kept the migration timestamp and body unchanged;
  - verified Ruby syntax and an ActiveRecord/ActiveSupport constantization
    probe in `nix develop`;
  - amended the commit with Overcommit active in `nix develop`, with
    pre-commit hooks passing;
  - pushed the amended branch to
    `fbc10201cf02404e844cf04791400f8b7f2d20e4`.
- Refreshed `vpsfree-mail-templates` `flake.lock` to pin vpsAdmin commit
  `fbc10201cf02404e844cf04791400f8b7f2d20e4`, verified
  `nix develop -c vpsadmin-notification-templates` prints usage, amended the
  template repo commit, and pushed the branch to `f0a638e`.
- Required standalone review by `Galileo`
  (`019eeb3e-a925-7bf1-a547-d23541d6681a`) reported no blocking, important,
  or advisory findings:
  - vpsAdmin delta is exactly the migration file rename, with the timestamp
    and migration class preserved;
  - template repo delta is only the vpsAdmin flake input repin;
  - residual risk is to make sure the deployment retry uses a fresh closure
    containing `fbc10201`.
- GitHub Actions after the amended vpsAdmin push:
  - RuboCop `27912105440`: success;
  - Webui PHPUnit `27912105443`: success;
  - API Specs topic parallel, libnodectld Specs, and CI were in progress when
    last checked.

## Dev Cluster Deployment Retry, Nullable Variant Fields

- The second services update with vpsAdmin
  `fbc10201cf02404e844cf04791400f8b7f2d20e4` got past
  `db:migrate`; the rename migration was applied on the services VM.
- The same switch then failed in
  `vpsadmin:notification_templates:install_defaults`:
  - `ActiveRecord::NotNullViolation: Mysql2::Error: Field 'from' doesn't have
    a default value`;
  - Telegram template variants have no e-mail sender or subject, but upgraded
    databases still had `notification_template_variants.from` and `subject`
    marked `NOT NULL` after the table rename.
- Fixed in `vpsadmin` by amending the notification-template commit:
  - added migration
    `api/db/migrate/20260615101000_relax_notification_template_variant_email_columns.rb`;
  - the migration makes `notification_template_variants.from` and `subject`
    nullable, and its rollback deletes non-email variants before restoring
    the old constraints;
  - kept this as a separate migration because the dev cluster had already
    recorded the table-rename migration as applied before the installer failed;
  - added a focused model spec asserting default Telegram variants have nil
    `from` and `subject` fields and populated text content.
- Verification for the follow-up migration:
  - `ruby -c
    api/db/migrate/20260615101000_relax_notification_template_variant_email_columns.rb`:
    OK;
  - `ruby -c api/spec/models/notification_templates_spec.rb`: OK;
  - `git diff --check`: OK;
  - ActiveRecord/ActiveSupport constantization in `nix develop` resolved the
    migration class name correctly;
  - `nix develop .#api -c bundle exec rspec
    spec/models/notification_templates_spec.rb` passed:
    8 examples, 0 failures;
  - Overcommit hooks passed during the amend in `nix develop`.
- Pushed amended `vpsadmin` branch to
  `7c35af2b2bc89cfe70e6226c819cb15f5aa080b4`.
- Refreshed `vpsfree-mail-templates` `flake.lock` to pin vpsAdmin commit
  `7c35af2b2bc89cfe70e6226c819cb15f5aa080b4`, verified
  `nix develop -c vpsadmin-notification-templates` prints usage, amended the
  template repo commit, and pushed the branch to
  `6230429c2caff54ff1b7706310554936fb155588`.
- A fresh mandatory review was requested from standalone reviewer `Beauvoir`
  (`019eeb52-03ab-76f2-b735-92bf4e0093f0`) before retrying the dev-cluster
  deployment.
- Required standalone review by `Beauvoir`
  (`019eeb52-03ab-76f2-b735-92bf4e0093f0`) reported no blocking, important,
  or advisory findings:
  - the vpsAdmin delta is narrowly scoped to the nullable-column migration and
    focused installer spec;
  - e-mail variants still have application-level presence validation for
    `from` and `subject`;
  - the template repo delta is only the vpsAdmin flake input repin;
  - residual risk is the intended dev-cluster retry against the partially
    migrated database.
- Rebuilt packaged vpsAdmin gems with
  `nix develop -c rake vpsadmin:gems`; the worktree remained clean.
- Services update with vpsAdmin
  `7c35af2b2bc89cfe70e6226c819cb15f5aa080b4` reached activation:
  - `vpsadmin-database-setup.service` succeeded;
  - the new nullable-column migration fixed the previous template installer
    failure;
  - built-in notification template installation reported 49 new variants.
- The same update still exited nonzero because activation exposed stale
  runtime/development wiring:
  - `vpsadmin-api-mail-process.service` loaded an old payment plugin symlink
    from `/var/lib/vpsadmin/api/plugins/payments` and failed on
    `MailTemplate.register`;
  - `vpsadmin-devcluster-seed.service` used the old
    `VpsAdmin::API::MailTemplates` helper and old recipient model names when
    installing external templates.
- Follow-up fixes after that deployment failure:
  - amended `vpsadmin` so API rake-task services run the same API app setup as
    the main API service before loading the app, refreshing config and plugin
    links for timer/manual rake tasks;
  - updated the local dev-cluster generator
    `dev-clusters/vpsadmin/nix/test.nix` so external template seed overrides
    use `VpsAdmin::API::NotificationTemplates`, `NotificationTemplate`,
    `NotificationTemplateVariant`, `EmailRecipient`, and
    `NotificationTemplateEmailRecipient`;
  - kept the dev-cluster input variables named after the
    `vpsfree-mail-templates` repository path.
- Verification for the follow-up deployment fixes:
  - formatted the changed vpsAdmin Nix module and dev-cluster Nix file with
    `nixfmt` from the vpsAdmin Nix shell;
  - `git diff --check` passed in `vpsadmin`;
  - `git diff --check -- dev-clusters/vpsadmin/nix/test.nix` passed in the
    workspace root;
  - `nix eval --impure --expr 'let f = import
    ./dev-clusters/vpsadmin/nix/test.nix; in builtins.isFunction f'` returned
    `true`;
  - `nix eval --impure --expr 'let f = import
    ./nixos/modules/vpsadmin/api/rake-tasks.nix; in builtins.isFunction f'`
    returned `true`;
  - scans of current `vpsadmin` and `vpsfree-mail-templates` source trees,
    excluding lock/vendor/gem-cache paths, found no future-protocol wording.
- Pushed amended `vpsadmin` branch to
  `457d0bb0bcf60a173ed59ffbf426408bd336c426`.
- Refreshed `vpsfree-mail-templates` `flake.lock` to pin vpsAdmin commit
  `457d0bb0bcf60a173ed59ffbf426408bd336c426`, verified
  `nix develop -c vpsadmin-notification-templates` prints usage, amended the
  template repo commit, and pushed the branch to
  `8d269a143282b560f05f5c63a1ed600ee1682a8b`.
- Required standalone review by `Hume`
  (`019eeb66-7a18-77f2-b505-2848158308b2`) reported no blocking, important,
  or advisory findings:
  - the rake-task setup change matches the existing API runtime refresh path;
  - the dev-cluster seed update matches the renamed
    notification-template/model surface and upserts variants by language and
    protocol;
  - the template repo delta is only the vpsAdmin flake input repin;
  - residual risk is the actual activation retry, and the dev-cluster support
    change remains a workspace-root diff for this local deployment test.

## Dev Cluster Deployment Retry, RabbitMQ Repair

- The next services update initially failed because the services VM filesystem
  was full:
  - `/`, `/nix/store`, and `/var/lib/vpsadmin` were at 100% used with no free
    blocks;
  - `vpsadmin-database-setup.service` could not create state-directory symlinks
    and exited with `No space left on device`.
- Ran `nix-collect-garbage -d` on the services VM:
  - removed stale system generations and old store paths;
  - free space improved to about 740 MiB, and inode usage dropped to about 55%.
- Retried the services update with vpsAdmin
  `457d0bb0bcf60a173ed59ffbf426408bd336c426`:
  - `vpsadmin-database-setup.service` succeeded;
  - notification template installation reported `Created 0 templates and 0
    variants`, as the built-in templates had already been installed;
  - main API, console router, scheduler, webhook test server, supervisor, and
    email/webhook dispatchers eventually settled after RabbitMQ was repaired.
- RabbitMQ state on the services VM was inconsistent after the full-disk
  episode:
  - RabbitMQ initially reported no users, no vhosts, and no listeners while the
    service was still considered active;
  - restarted `rabbitmq.service`, removed the stale
    `/var/lib/vpsadmin-rabbitmq/rabbitmq-initialized` marker, and reconciled the
    dev-cluster users/passwords/permissions from `/etc/vpsadmin-test`;
  - confirmed the `notification` RabbitMQ user now has permissions for
    `vpsadmin.notifications.(email|telegram|webhook)`.
- Follow-up code/config updates after the RabbitMQ deployment finding:
  - amended `vpsadmin` so `tools/rabbitmqcfg.rb` grants the notification user
    access to the Telegram notification queue as well as e-mail and webhook
    queues;
  - pushed amended `vpsadmin` branch to
    `dfef1d14b5eb8645bd152b76d3f26ab8f173245e`;
  - refreshed `vpsfree-mail-templates` `flake.lock` to pin vpsAdmin commit
    `dfef1d14b5eb8645bd152b76d3f26ab8f173245e`, committed
    `ad168846b52ce00ed1afbfc89cac9d0019d83ce8`, and pushed the branch.
- Verification for the RabbitMQ permission follow-up:
  - `ruby -c tools/rabbitmqcfg.rb`: OK;
  - `./tools/rabbitmqcfg.rb user --vhost vpsadmin_test --perms notification
    notification` prints a permission regexp containing
    `vpsadmin\\.notifications\\.(email|telegram|webhook)`;
  - `git diff --check` passed in both affected repositories;
  - `nix develop -c vpsadmin-notification-templates --help` exited 0;
  - scans of current `vpsadmin` and `vpsfree-mail-templates` source trees,
    excluding lock/vendor/gem-cache paths, found no future-protocol wording.
- Required standalone review by `Halley`
  (`019eeb84-4336-7cd3-8e41-8b2c326ebc4b`) reported no blocking or important
  findings:
  - advisory only: the RabbitMQ permission change is bundled into the
    notification-template commit but not mentioned in that commit message;
  - the reviewer confirmed the permission regexp matches the runtime Telegram
    queue names and that the template repo resolves vpsAdmin to
    `dfef1d14b5eb8645bd152b76d3f26ab8f173245e`;
  - residual risk is the final dev-cluster switch to `dfef1d14`, plus explicit
    Telegram delivery still requiring configured Telegram credentials because
    the dispatcher action remains opt-in.

## Dev Cluster Deployment Retry, Serialized Runtime Setup

- Services update with vpsAdmin
  `dfef1d14b5eb8645bd152b76d3f26ab8f173245e` built and copied the intended
  closure, then exited nonzero during activation:
  - `vpsadmin-api-outage-reports-auto-resolve.service` failed in
    `ExecStartPre` with `ln: failed to create symbolic link
    '/var/lib/vpsadmin/api/plugins/monitoring/monitoring': Read-only file
    system`;
  - `vpsadmin-api-requests-ipqs.service` failed in `ExecStartPre` because
    `deployment.json` was missing while another setup process was rewriting the
    shared API config directory.
- Root cause:
  - the previous rake-task stale-plugin fix made all API rake-task services run
    `apiApp.setup`;
  - several rake services and the main API service can start at the same time
    during activation;
  - concurrent setup against the same `/var/lib/vpsadmin/api` state directory
    can race over plugin/config symlink cleanup and recreation;
  - `ln -sf` follows an existing symlink to a directory, so one concurrent
    setup tried to create a nested link inside the read-only Nix store plugin
    directory.
- Follow-up fix in `vpsadmin`:
  - moved `apiApp.setup` into a generated setup script;
  - wrapped each setup invocation with `flock` on
    `${stateDirectory}/.setup.lock`;
  - changed managed plugin cleanup to `rm -rf "${stateDirectory}/plugins/"*`;
  - changed config/plugin symlink writes to `ln -sfn`;
  - updated the commit message to mention serialized runtime setup and the
    RabbitMQ Telegram queue permission.
- Verification for the serialized setup fix:
  - `nix develop -c nixfmt nixos/modules/vpsadmin/api-app.nix`: passed;
  - `nix eval --impure --expr 'let f = import
    ./nixos/modules/vpsadmin/api-app.nix; in builtins.isFunction f'` returned
    `true`;
  - `git diff --check` passed in `vpsadmin`;
  - local shell simulation confirmed `ln -sfn` does not create a nested link
    inside a symlinked directory;
  - scans of current `vpsadmin` and `vpsfree-mail-templates` source trees,
    excluding lock/vendor/gem-cache paths, found no future-protocol wording.
- Pushed amended `vpsadmin` branch to
  `b578ea2f7463d0084f5c044cc6d9b46c99e661c7`.
- Refreshed `vpsfree-mail-templates` `flake.lock` to pin vpsAdmin commit
  `b578ea2f7463d0084f5c044cc6d9b46c99e661c7`, amended the lock-pin commit to
  `2405d3969c40c1e8ef2651fd552f04340c3d6c32`, and pushed the branch.
- A fresh mandatory review was requested from standalone reviewer `Descartes`
  (`019eeb93-186c-7fc3-acd5-8c29615a1f67`) before retrying the services
  update.
- Required standalone review by `Descartes`
  (`019eeb93-186c-7fc3-acd5-8c29615a1f67`) reported no blocking, important,
  or advisory findings:
  - the reviewer confirmed the latest vpsAdmin delta is limited to
    `nixos/modules/vpsadmin/api-app.nix`;
  - the reviewer confirmed `flock`, `rm -rf` plugin cleanup, and `ln -sfn`
    address the reported activation race;
  - the reviewer confirmed the template repo lock resolves vpsAdmin to
    `b578ea2f7463d0084f5c044cc6d9b46c99e661c7`;
  - residual risk is the actual services switch with `b578ea2f` and Telegram
    end-to-end delivery still requiring configured Bot API credentials.

## Dev Cluster Deployment Success

- Retried `dev-clusters/vpsadmin/bin/devcluster update
  2026-06-15-vpsadmin-events services` with vpsAdmin
  `b578ea2f7463d0084f5c044cc6d9b46c99e661c7`.
- The services update completed successfully:
  - system generation:
    `/nix/store/0fxxh3mq7vv7rbm2irzlyc2q0nkkzkj9-nixos-system-vpsadmin-services-26.05pre-git`;
  - the previously failing rake task service
    `vpsadmin-api-requests-ipqs.service` started successfully during
    activation;
  - the updater exited with code 0.
- Post-deployment verification:
  - `systemctl --failed --no-pager`: 0 failed units;
  - active services: `vpsadmin-api.service`,
    `vpsadmin-console-router.service`, `vpsadmin-scheduler.service`,
    `vpsadmin-webhook-test-server.service`, `vpsadmin-supervisor.service`,
    `vpsadmin-notification-dispatcher-email.service`,
    `vpsadmin-notification-dispatcher-webhook.service`,
    `vpsadmin-database-setup.service`, and
    `vpsadmin-rabbitmq-setup.service`;
  - `vpsadmin-database-setup.service` succeeded, ran migrations and plugin
    migrations, and the built-in notification template installer reported
    `Created 0 templates and 0 variants` on the final switch;
  - `notification_template_variants.from` and `subject` are nullable;
  - DB counts: 54 notification templates, 98 e-mail variants, 49 Telegram
    variants;
  - API plugin links under `/var/lib/vpsadmin/api/plugins` all point to the new
    vpsAdmin store path
    `/nix/store/mbjabd8z1wmgcf08sgymck67566slg7k-vpsadmin-api-dev`;
  - RabbitMQ `notification` user permissions include
    `vpsadmin.notifications.(email|telegram|webhook)`;
  - `curl -k -I https://api.aitherdev.int.vpsfree.cz/`: HTTP 200;
  - `curl -k -I https://webui.aitherdev.int.vpsfree.cz/`: HTTP 200.
- Services VM capacity after the final switch:
  - `/`, `/nix/store`, and `/var/lib/vpsadmin`: about 4.1 GiB used of 4.9 GiB,
    474 MiB free, 90% used;
  - inodes: about 236280 used of 326400, 73% used.
- Git branch heads after deployment:
  - `vpsadmin`: `b578ea2f7463d0084f5c044cc6d9b46c99e661c7`;
  - `vpsfree-mail-templates`:
    `2405d3969c40c1e8ef2651fd552f04340c3d6c32`;
  - the template repo `flake.lock` resolves vpsAdmin to
    `b578ea2f7463d0084f5c044cc6d9b46c99e661c7`.
- GitHub Actions after the latest vpsAdmin push:
  - RuboCop: success;
  - Webui PHPUnit: success;
  - libnodectld Specs: success;
  - API Specs (topic parallel): success;
  - long `CI` workflow is still queued at the time of this note.

## Telegram Receiver Service Implementation

- User feedback after the initial Telegram slice changed the deployment model:
  - pairing updates must be received by a long-running service, not frequent
    rake polling;
  - Telegram receiver actions must not be offered by the API when Telegram is
    not configured;
  - the Telegram bot token must live in a file and be picked up automatically
    by the dev cluster;
  - both polling and webhook receive modes are supported;
  - the production webhook uses the existing API domain at
    `https://api.vpsfree.cz/_telegram/webhook`.
- `vpsadmin` changes in progress:
  - added `VpsAdmin::API::TelegramReceiver`, used by
    `bin/vpsadmin-telegram-receiver`;
  - polling mode long-polls `getUpdates`, deletes any configured webhook on
    startup by default, and stores the update offset in `SysConfig`;
  - webhook mode serves a Rack app, validates
    `X-Telegram-Bot-Api-Secret-Token` when configured, and can register the
    public webhook with Telegram on startup;
  - the old `vpsadmin:telegram:poll_pairing_updates` task now wraps
    `TelegramReceiver#poll_once` for manual compatibility only;
  - Telegram receiver actions are available only when
    `VpsAdmin::API::Notifications.telegram_configured?` is true;
  - existing Telegram actions become non-deliverable when Telegram is not
    configured, and pairing-token creation reports that Telegram delivery is
    not configured;
  - added NixOS modules/options for shared Telegram notification config,
    `vpsadmin-telegram-receiver.service`, HAProxy
    `telegram-receiver` frontends, and API frontend exact webhook locations.
- Dev-cluster changes in progress:
  - `devcluster` exports `.dev-clusters/vpsadmin/telegram` to Nix as
    `VPSADMIN_DEVCLUSTER_TELEGRAM_SECRETS`;
  - if `bot-token` exists there, the services VM mounts it, enables Telegram
    delivery, enables `vpsadmin-telegram-receiver.service`, and includes the
    Telegram dispatcher action;
  - default receive mode is polling;
  - when `telegram.receiveMode` is `webhook`, the dev cluster also enables the
    API-domain exact webhook proxy route and a local HAProxy receiver backend;
  - README instructions document bot-token and webhook-secret file setup.
- `vpsfree-cz-configuration` changes in progress:
  - API hosts enable shared Telegram config in webhook mode, using
    `/private/vpsadmin-telegram-bot-token` and
    `/private/vpsadmin-telegram-webhook-secret`;
  - API hosts enable `vpsadmin-telegram-receiver.service` on their primary
    addresses, port `9293`, accessible only from the production proxy;
  - production frontend adds HAProxy routing for receiver backends on api1/api2
    and an exact nginx API-domain webhook location that bypasses Varnish.
- Deployment notes:
  - new production secrets are required before enabling the config:
    `/private/vpsadmin-telegram-bot-token`,
    `/private/vpsadmin-telegram-webhook-secret`, and the notification RabbitMQ
    password `/private/vpsadmin-notification-rabbitmq.pw`;
  - the RabbitMQ `notification` user must have permissions for
    `vpsadmin.notifications.(email|telegram|webhook)`;
  - `vpsfree-cz-configuration` must pin the vpsAdmin feature commit through
    `confctl inputs channel set --commit` before production evaluation can
    succeed with the new module options.
- Verification so far:
  - Ruby syntax OK for the receiver, binary, notifications registry, model,
    task wrapper, and Telegram spec;
  - `nix develop .#api -c bundle exec rubocop ...`: 9 files inspected, no
    offenses;
  - focused API specs with Telegram Bot/receiver/action/delivery/resource
    coverage passed: 99 examples, 0 failures, 1 expected pending;
  - vpsAdmin Nix files, dev-cluster Nix files, and production config Nix files
    formatted with project Nix shells;
  - `git diff --check` passed in `vpsadmin`, `vpsfree-cz-configuration`, and
    the touched dev-cluster files;
  - `nix-instantiate --parse` passed for the touched Nix files;
  - synthetic NixOS module eval passed for API + Telegram receiver + Telegram
    dispatcher + HAProxy + nginx webhook route, producing receiver mode
    `webhook`, the exact webhook proxy upstream, and e-mail/Telegram/webhook
    dispatcher services;
  - direct overlay package build passed for `pkgs.vpsadmin-telegram-receiver`
    using `vpsadminRev = "dev"`;
  - scans over the changed vpsAdmin, dev-cluster, and production-config files
    found no compact-message protocol wording.
- Commits and pushes for this slice:
  - `vpsadmin` commit
    `7f99fc47ca6497d03c28214cc8f90f13ac6f5221`
    (`notifications: add Telegram receiver service`) was committed with
    Overcommit hooks active in `nix develop` and pushed to
    `origin/2026-06-15-vpsadmin-events`;
  - `vpsfree-cz-configuration` generated pin commit
    `edc22ee28d0b36a525ff19b283a48733dd95b20d`
    set `vpsadminProduction`, `vpsadminServices`, and `vpsadminStaging` to
    vpsAdmin `7f99fc47` through
    `confctl inputs channel set --commit production,staging,vpsadmin
    vpsadmin 7f99fc47ca6497d03c28214cc8f90f13ac6f5221`;
  - `vpsfree-cz-configuration` functional commit
    `70abd0a8c2f292db1643d713aa97959e668f668b`
    (`vpsadmin-config: enable Telegram notifications`) was committed with
    Overcommit hooks active in `nix develop` and pushed to
    `origin/2026-06-15-vpsadmin-events`;
  - workspace dev-cluster commit
    `a16294d6fc99c9b4c38d80d01b2f222c058b2598`
    (`devcluster: update vpsAdmin notification testing`) was committed on the
    workspace branch `2026-06-15-vpsadmin-events` and pushed to
    `git@github.com:aither64/vpsfree-cz-workspace.git`.
- Production config verification after pinning vpsAdmin:
  - initial `confctl build 'cz.vpsfree/vpsadmin/int.api*'
    'cz.vpsfree/containers/prg/proxy'` failed before building because
    `confctl build` prompted for confirmation in a noninteractive shell;
  - reran with `-y`;
  - `confctl build -y 'cz.vpsfree/vpsadmin/int.api*'` passed and built
    generations for `cz.vpsfree/vpsadmin/int.api1` and
    `cz.vpsfree/vpsadmin/int.api2`;
  - `confctl build -y 'cz.vpsfree/containers/prg/proxy'` passed and built a
    generation for `cz.vpsfree/containers/prg/proxy`;
  - the API build log showed the new
    `vpsadmin-telegramReceiver-7f99fc47...` package, receiver pre-start
    scripts, `vpsadmin-telegram-receiver.service`, and Telegram dispatcher
    service being generated.
- Workspace branch note:
  - the workspace repo was initially on local branch
    `2026-06-13-vps-replace-backups` when the dev-cluster commit was made;
  - created and switched to `2026-06-15-vpsadmin-events` at that commit before
    pushing, and did not push the older branch name.
- Mandatory change review:
  - requested from standalone reviewer `Aquinas`
    (`019eec11-72bf-7983-aa31-0c5ef644378e`) after commits and quick
    verification, before dev-cluster deployment;
  - result: no blocking, important, or advisory findings;
  - reviewer confirmed the receiver-service model, polling/webhook
    configurability, API availability gating, dev-cluster token-file pickup,
    and production API-domain webhook route match the request;
  - reviewer considered the workspace dev-cluster commit bundling acceptable
    because the template seed rename, SMTP capture override, webhook test
    server, and Telegram support are all part of making notification testing
    work;
  - residual risks/test gaps: no live Telegram Bot API integration test, no
    full dev-cluster deployment/smoke after this slice yet, no browser-level
    configured/unconfigured Telegram UI test, and production activation still
    depends on operator-provided secret files plus RabbitMQ permissions.
- Dev-cluster deployment follow-up:
  - first `devcluster update 2026-06-15-vpsadmin-events services` failed with
    `mnt-devcluster-telegram.mount` because the dev-cluster update tried to add
    a new Telegram virtiofs share to an already-running VM even though no bot
    token was configured;
  - reworked dev-cluster Telegram secrets handling to avoid the virtiofs share:
    host token files remain under `.dev-clusters/vpsadmin/telegram/`, and
    `devcluster update <slug> services` copies them into the services VM under
    `/var/lib/vpsadmin/devcluster-telegram` before switching the system
    configuration;
  - the Nix cluster config now enables Telegram only when
    `VPSADMIN_DEVCLUSTER_TELEGRAM_ENABLE=1` and a host `bot-token` file exists,
    so a fresh cluster can still start if a token file already exists and can
    be enabled by a follow-up services update;
  - reran `devcluster update 2026-06-15-vpsadmin-events services`: passed;
  - `devcluster status 2026-06-15-vpsadmin-events`: running, bridge network,
    ready `yes`;
  - services VM `systemctl --failed --no-pager`: `0 loaded units listed`;
  - with no host bot token present, services VM has no active Telegram mount,
    no Telegram unit files, and no Telegram units;
  - `vpsadmin-api.service`,
    `vpsadmin-notification-dispatcher-email.service`,
    `vpsadmin-notification-dispatcher-webhook.service`, and
    `vpsadmin-webhook-test-server.service` are active;
  - HTTP smoke checks returned `200` for
    `https://api.aitherdev.int.vpsfree.cz/` and
    `https://webui.aitherdev.int.vpsfree.cz/`.
  - mandatory standalone change review for this follow-up was not launched
    because the available subagent tool for this turn allowed spawning only
    when explicitly requested by the user; request an explicit review if this
    follow-up should be audited separately from the earlier completed review.
  - amended workspace commit `a16294d6fc99c9b4c38d80d01b2f222c058b2598` was
    pushed to `origin/2026-06-15-vpsadmin-events` with `--force-with-lease`.
- Telegram action validation fix:
  - user reported that adding a Telegram action in the dev cluster failed with
    `action: is not included in the list, is not available`;
  - root cause: the dev DB had already run an earlier prototype of
    `20260615110000_add_events.rb` where `notification_receiver_actions.action`,
    `event_deliveries.action`, and `event_delivery_attempts.action` were
    integer columns, while the final code/schema stores action registry names
    as strings; Rails therefore cast submitted `telegram` to integer `0` and
    the action registry validator rejected it;
  - added vpsAdmin migration
    `20260622161000_convert_notification_action_columns_to_strings.rb` to
    convert already-migrated integer action columns to `varchar(50)` and map
    existing `0/1/2` values to `email/webhook/telegram`; fresh databases with
    current string columns are left unchanged;
  - added a model spec asserting that notification action columns are strings;
  - verification in vpsAdmin:
    `ruby -c` for the new migration/spec, `git diff --check`,
    `nix develop .#api -c bundle exec rspec
    spec/models/notification_receiver_action_spec.rb` (12 examples, 0
    failures), and targeted RuboCop (2 files, no offenses);
  - committed vpsAdmin fix
    `b0f5c086cdacd1a1721b8992eec71a75a9c5c38c`
    (`notifications: migrate action columns to strings`) with Overcommit hooks
    active in `nix develop` and pushed to
    `origin/2026-06-15-vpsadmin-events`;
  - updated `vpsfree-cz-configuration` with generated pin commit
    `91024d55` setting `vpsadminProduction`, `vpsadminServices`, and
    `vpsadminStaging` to vpsAdmin `b0f5c086`, then pushed
    `origin/2026-06-15-vpsadmin-events`;
  - `confctl build -y cz.vpsfree/vpsadmin/int.api1` passed and built
    generation `2026-06-22--18-55-21`;
  - redeployed the services VM from the clean vpsAdmin branch with
    `devcluster update 2026-06-15-vpsadmin-events services`;
  - post-deploy services VM checks: no failed systemd units; API, e-mail
    dispatcher, webhook dispatcher, Telegram dispatcher, and Telegram receiver
    all active;
  - post-deploy DB check: all three action columns are `varchar(50)`, existing
    delivery rows are `email`, and the attempted Telegram receiver action is
    stored as `telegram`;
  - deployed Rails probe against
    `/nix/store/z9m95s1gs0y3gs79avlak5z5c4fricm2-vpsadmin-api-dev` confirmed
    `NotificationReceiverAction.action` type `string`, submitted action
    `"telegram"`, Telegram registry availability `true`, and no validation
    errors;
  - HTTP smoke checks returned `200` for
    `https://api.aitherdev.int.vpsfree.cz/` and
    `https://webui.aitherdev.int.vpsfree.cz/`.
- Telegram pairing UX follow-up:
  - implemented and committed vpsAdmin
    `527cc7cc30d8326d4f40ab5a413c0648ed1d6a2d`
    (`notifications: guide Telegram pairing`);
  - implemented and committed workspace/dev-cluster
    `24ee78f2c37d7b0d9dbd0c67cc9174c826f9cb8b`
    (`devcluster: expose Telegram bot username`);
  - changes add API pairing metadata, WebUI redirect/instructions and
    explicit re-pair wording, best-effort Telegram bot replies for pairing
    success/failure, and dev-cluster bot username loading from a non-secret
    `bot-username` file;
  - quick verification passed:
    - API focused specs:
      `nix develop .#api -c bundle exec rspec
      spec/models/notification_receiver_action_spec.rb
      spec/models/tasks/telegram_spec.rb
      spec/api/resources/event_routing_spec.rb`
      (51 examples, 0 failures, 1 existing pending monitoring-plugin example);
    - targeted RuboCop:
      `nix develop .#api -c bundle exec rubocop ...`
      (6 files, no offenses);
    - WebUI regression:
      `nix develop ..#webui -c bash -lc 'composer install --no-interaction
      && vendor/bin/phpunit -c phpunit.xml.dist --filter
      NotificationDeliveryHtmlDetailsTest'`
      (6 tests, 40 assertions);
    - Ruby/PHP syntax checks, Nix parse checks for touched modules, and
      `git diff --check` passed;
  - mandatory standalone change review by subagent
    `019ef06a-3d73-7303-8762-2ca11188e6e9` reported no blocking, important,
    or advisory findings; residual follow-up is to smoke-test after deploy and
    verify that `botUsername` is configured where t.me links should render.
  - pushed vpsAdmin `527cc7cc3` to
    `origin/2026-06-15-vpsadmin-events`;
  - first dev-cluster deploy attempt failed during Nix evaluation because the
    workspace dev-cluster merge placed `botUsername` under
    `vpsadmin.notifications.telegram.webhook.botUsername`; fixed the merge so
    `botUsername` is set on `vpsadmin.notifications.telegram`, amended the
    workspace commit to `24ee78f2`, verified
    `nix-instantiate --parse dev-clusters/vpsadmin/nix/test.nix` and
    `git diff --check`, then pushed with `--force-with-lease`;
  - updated `vpsfree-cz-configuration` with generated pin commit
    `995d80a6` setting `vpsadminProduction`, `vpsadminServices`, and
    `vpsadminStaging` to vpsAdmin `527cc7cc`, then pushed
    `origin/2026-06-15-vpsadmin-events`;
  - `confctl build -y cz.vpsfree/vpsadmin/int.api1` passed and built
    generation `2026-06-22--19-50-45`, including vpsAdmin packages at
    `527cc7cc`;
  - redeployed the services VM with
    `devcluster update 2026-06-15-vpsadmin-events services`;
  - post-deploy checks:
    - `devcluster status 2026-06-15-vpsadmin-events`: running, bridge network,
      ready `yes`;
    - services VM `systemctl --failed --no-pager`: `0 loaded units listed`;
    - `vpsadmin-api.service`,
      `vpsadmin-notification-dispatcher-email.service`,
      `vpsadmin-notification-dispatcher-webhook.service`,
      `vpsadmin-notification-dispatcher-telegram.service`, and
      `vpsadmin-telegram-receiver.service` are active;
    - generated notification configs contain
      `bot_username":"vpsadmin_aitherdev_bot"`; the probe extracted only the
      username fragment to avoid printing token-adjacent JSON;
    - `journalctl -u vpsadmin-telegram-receiver.service -n 20` shows the
      receiver stopped and started cleanly during deployments with no recent
      failure entries;
    - HTTP smoke checks returned `200` for
      `https://api.aitherdev.int.vpsfree.cz/` and
      `https://webui.aitherdev.int.vpsfree.cz/`.
  - GitHub Actions after the `527cc7cc3` vpsAdmin push:
    - `RuboCop`: success;
    - `API Specs (topic parallel)`: success;
    - `Webui PHPUnit`: success;
    - aggregate `CI` workflow `27972587204` still in progress after local
      deployment verification; older aggregate CI runs for previous commits
      were also still in progress.
  - `vpsfree-cz-configuration` listed no branch workflow runs after the
    `995d80a6` push; pushing showed GitHub's existing Dependabot
    vulnerability banner for the default branch, unrelated to this feature
    branch.
- Receiver action deletion confirmation follow-up:
  - implemented WebUI confirmation for `receiver_action_delete` links using
    existing `notifications_confirm_onclick()` helper with message
    `Do you really wish to delete this notification receiver action?`;
  - added focused WebUI regression coverage in
    `NotificationDeliveryHtmlDetailsTest`;
  - quick verification passed:
    - `php -l webui/forms/notifications.forms.php`;
    - `php -l webui/tests/Regression/NotificationDeliveryHtmlDetailsTest.php`;
    - `nix develop ..#webui -c bash -lc 'composer install --no-interaction
      && vendor/bin/phpunit -c phpunit.xml.dist --filter
      NotificationDeliveryHtmlDetailsTest'`
      (7 tests, 45 assertions);
    - `git diff --check`.
  - committed vpsAdmin
    `9956b0c0b68bce97ca4f1995544e1a1fa180f44c`
    (`webui: confirm receiver action deletion`);
  - mandatory standalone change review by subagent
    `019ef0a9-a213-7b80-8dfe-60811156691f` reported no blocking,
    important, or advisory findings. Residual risk is only that coverage is
    source-level rather than browser-click coverage; direct valid-CSRF delete
    requests remain possible by design.
  - first plain `git push` failed because the shared Overcommit pre-push hook
    could not find the `overcommit` gem outside the dev shell; retried with
    `nix develop . -c git push origin 2026-06-15-vpsadmin-events`
    successfully, pushing `527cc7cc3..9956b0c0b`.
  - GitHub Actions after push:
    - `Webui PHPUnit` run `27976323127`: success;
    - aggregate `CI` run `27976323117`: queued at last check.

## 2026-06-22 SMS notification design investigation

- User asked for design proposals for adding SMS receiver actions to
  vpsAdmin notifications while preserving alertmanager SMS priority.
- Relevant repositories:
  - `vpsadmin` for the `sms` notification action, delivery dispatcher,
    templates/API/WebUI/tests, and production Nix module options;
  - `vpsfree-cz-configuration` for wiring vpsAdmin to the production sachet
    topology and opening only the required network access;
  - the vpsFree fork of `sachet` if reliable cross-source priority requires a
    queue/status API or explicit source priorities.
- Current vpsAdmin notification design is suitable for another action:
  `VpsAdmin::API::Notifications::Actions` defines `email`, `webhook`, and
  `telegram`; dispatchers consume per-action `EventDelivery` rows through
  RabbitMQ/database reconciliation; the production config currently enables
  `email`, `telegram`, and `webhook`.
- Production SMS topology in `vpsfree-cz-configuration`:
  - `apu.int.prg` and `apu.int.brq` run `services.sachet` with provider
    `modem`, using `/dev/ttyUSB-EC25-at`;
  - APUs currently allow sachet access only from the alertmanager hosts;
  - alertmanager uses local HAProxy on the alerter containers at
    `127.0.0.1:5000`, with backend order `apu-prg`, `apu-brq`, then local
    Nexmo fallback and `balance first`;
  - alertmanager receivers `sms-aither` and `sms-snajpa` POST to
    `http://127.0.0.1:5000/alert`.
- Pinned sachet package is `vpsfreecz/sachet` commit `670ac3c7`
  (`vpsfree-0.3.2`). Its `/alert` handler decodes Alertmanager webhook JSON,
  finds a receiver by `data.Receiver`, and calls `provider.Send`.
- In the vpsFree modem provider, `Send` enqueues into an in-memory queue and
  returns success immediately; the modem dispatcher later sends SMS
  sequentially with retry/cooldown. The queue has a configurable `queue_size`
  defaulting to 5 and drops the oldest queued message when congested.
- The pinned sachet exposes `/metrics`, `/-/live`, and `/-/ready`, but no
  documented queue-depth/status API and no distinction between alertmanager
  and non-alertmanager enqueue priority. This is the key design constraint for
  guaranteeing that vpsAdmin sends only when the alertmanager SMS queue is
  empty.
- Refined implementation direction:
  - create a dedicated Go `vpsfree-sms-gateway` instead of extending sachet;
  - run one gateway per APU modem with per-modem priority only;
  - alertmanager uses PRG first then BRQ, while vpsAdmin uses BRQ first then
    PRG so both producers normally use different modems but can fail over;
  - use durable SQLite queues, modem send retries, inbound SMS reception, and
    Prometheus metrics;
  - vpsAdmin SMS receiver actions are admin-gated, user-managed numbers
    require SMS code verification, and gateway final-status callbacks update
    vpsAdmin deliveries;
  - SMS content is rendered from `vpsfree-mail-templates` `sms/*.text.erb`
    protocol variants.

## 2026-06-22 SMS gateway implementation

- Implemented and pushed new repository `vpsfree-sms-gateway`:
  - worktree:
    `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-06-15-vpsadmin-events/vpsfree-sms-gateway`;
  - branch: `2026-06-15-vpsadmin-events`;
  - head: `730b35c652d0efb596bfe290d0afea76e494a678`
    (`Add SMS gateway service`);
  - remote: `git@github.com:vpsfreecz/vpsfree-sms-gateway.git`.
- Gateway behavior:
  - Go service with SQLite-backed outbound queue, one worker per gateway/modem,
    retry/cooldown/timeout settings, and priority ordering where Alertmanager
    uses priority `0` and vpsAdmin uses priority `10`;
  - Alertmanager-compatible `POST /alert`, native vpsAdmin `POST /v1/sms`,
    status `GET /v1/messages/{id}`, `/-/live`, `/-/ready`, and `/metrics`;
  - bearer tokens for Alertmanager, vpsAdmin, status, and callbacks;
  - real modem driver using `github.com/warthog618/modem` plus fake modem for
    development/tests;
  - startup recovery requeues abandoned outbound sends, inbound webhook
    deliveries, and vpsAdmin callbacks left in `sending` by a crash or
    restart;
  - final vpsAdmin callbacks are delivered through a persisted retry queue;
  - inbound SMS persistence and webhook forwarding with retry;
  - Prometheus metrics for queue depth, modem readiness, attempts, final
    states, vpsAdmin callback queue state, inbound messages, and inbound
    webhook delivery;
  - modem sends are synchronous under the modem lock so a send timeout cannot
    start a second concurrent AT send while the first modem operation is still
    running;
  - SMS segment limits use GSM-7/UCS-2 segment estimation.
- Gateway verification:
  - `CGO_ENABLED=0 go test ./...` passed;
  - `nix build .#default` passed;
  - `result` symlink removed after the Nix build.
- Implemented and pushed `vpsadmin` SMS delivery:
  - worktree:
    `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-06-15-vpsadmin-events/vpsadmin`;
  - branch: `2026-06-15-vpsadmin-events`;
  - base for this feature series: `c75cc5d254dc9e9fec3ca7cfe97e8053a2bf71df`;
  - heads:
    - `8c9aabaa6a513db5129a4a95c3f5cbf102d28a5f`
      (`Add SMS notification delivery support`);
    - `bdf748ea58292bb533fb361a3662cd308e78f4f9`
      (`Add SMS templates for bundled plugins`);
  - branch pushed to `origin/2026-06-15-vpsadmin-events`.
- vpsAdmin behavior:
  - new `sms` notification action/protocol, dispatcher queue, delivery context,
    SMS rendering, and gateway fallback client;
  - new `users.sms_notifications_enabled` admin-controlled flag;
  - user SMS receiver actions require E.164 numbers, admin enablement, and
    short-lived six-digit verification codes before event delivery;
  - SMS verification codes lock out after repeated invalid attempts and clear
    that state only on successful verification or regenerated code state;
  - API subactions send and confirm SMS verification codes;
  - internal bearer-protected callback route marks accepted gateway messages as
    sent or failed;
  - WebUI supports SMS receiver action creation, verification-code sending and
    confirmation, and SMS delivery details;
  - Nix module options configure SMS gateways, callback URL/token, timeout
    values, and dispatcher action `sms`.
- vpsAdmin verification:
  - focused API/model/template/delivery specs passed:
    `nix develop .#api -c bundle exec rspec
    spec/models/notification_receiver_action_spec.rb
    spec/models/tasks/event_delivery_spec.rb
    spec/models/notification_templates_spec.rb
    spec/api/resources/event_routing_spec.rb`
    initially passed before review fixes (111 examples, 0 failures, 1
    pending), and passed again after the verification lockout fix (112
    examples, 0 failures, 1 pending);
  - focused WebUI regression passed:
    `nix develop .#webui -c composer test -- --filter
    NotificationDeliveryHtmlDetailsTest`
    (9 tests, 58 assertions);
  - full RuboCop passed before review fixes:
    `nix develop .#api -c bundle exec rubocop`
    (1380 files, no offenses);
  - touched-file RuboCop passed after review fixes:
    `nix develop .#api -c bundle exec rubocop
    models/notification_receiver_action.rb
    spec/models/notification_receiver_action_spec.rb`;
  - PHP syntax checks passed for
    `webui/forms/notifications.forms.php`,
    `webui/pages/page_notifications.php`, and
    `webui/tests/Regression/NotificationDeliveryHtmlDetailsTest.php`;
  - touched-file PHP-CS-Fixer dry run passed for those WebUI files;
  - full PHP-CS-Fixer scan still reports unrelated pre-existing formatting
    diffs elsewhere in the repository, so only touched files were checked;
  - SMS plugin templates were ERB-parsed with Ruby before committing the
    follow-up template commit.
- Implemented and pushed `vpsfree-mail-templates` SMS templates:
  - worktree:
    `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-06-15-vpsadmin-events/vpsfree-mail-templates`;
  - branch: `2026-06-15-vpsadmin-events`;
  - base: `7da522e060fc18d5426e1dd6cd305b6847faf5ed`;
  - head: `21b893ded2fafd83dba3ae9c3a29fe8ec5c422ac`
    (`Add SMS notification templates`);
  - branch pushed to `origin/2026-06-15-vpsadmin-events`.
- Mail template verification:
  - all `templates/*/sms/*.erb` files parsed through `ERB.new(...,
    trim_mode: "-")` successfully;
  - the command emitted Bundler/Gem platform redefinition warnings, but no ERB
    failures.
- Implemented and pushed `vpsfree-cz-configuration` SMS gateway routing:
  - worktree:
    `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-06-15-vpsadmin-events/vpsfree-cz-configuration`;
  - branch: `2026-06-15-vpsadmin-events`;
  - base: `e550af53968aa19ac53bf634ed389f674bd93c05`;
  - heads:
    - `220ebf87c712d8f17a07271ecf5254b5f93a7446`
      (`vpsadmin-config: add SMS gateway routing`);
    - `444571dee2b06ca3fd0fe8308e9928dfb173bf1f`
      (`inputs: set vpsadminServices to bdf748ea`);
    - `e5fd40dc0000b86ad1353bc8bd5155e6a4ad6176`
      (`inputs: set vpsfreeSmsGateway to 730b35c6`);
  - branch pushed to `origin/2026-06-15-vpsadmin-events`.
- Production configuration behavior:
  - added `vpsfreeSmsGateway` flake input from the new GitHub repository and a
    `vpsfree-sms-gateway` channel;
  - added NixOS service module for `vpsfree-sms-gateway` with runtime secret
    loading, systemd service, state directory, package override, and token
    file options;
  - APUs now run `vpsfree-sms-gateway` on the modem device
    `/dev/ttyUSB-EC25-at`, allow the relevant Alertmanager/vpsAdmin/monitoring
    clients to port `9876`, and bind to the LTE modem device;
  - Alertmanager webhook receivers use gateway auth and HAProxy keeps PRG then
    BRQ ordering, with the existing local fallback retained;
  - vpsAdmin SMS gateways are ordered BRQ then PRG and use the internal
    callback URL `https://api.vpsfree.cz/internal/notifications/sms/callback`;
  - Prometheus scrapes the SMS gateways.
- Configuration verification:
  - `nix shell nixpkgs#nixfmt-rfc-style -c nixfmt --check ...` passed for the
    changed Nix files;
  - `git diff --check` passed;
  - `nix develop -c confctl build --yes 'cz.vpsfree/vpsadmin/int.api*'`
    passed before the final pin and built generation
    `2026-06-22--23-32-20`;
  - `nix develop -c confctl build --yes
    'cz.vpsfree/containers/prg/int.alerts*'` passed and built generation
    `2026-06-22--23-34-52`;
  - after the first `vpsadminServices` pin to `1b219bb4`,
    `nix develop -c confctl build --yes 'cz.vpsfree/vpsadmin/int.api*'`
    passed again and built generation `2026-06-22--23-45-49`;
  - after review fixes and final pins to vpsAdmin `bdf748ea` and gateway
    `730b35c6`, `nix develop -c confctl build --yes
    'cz.vpsfree/vpsadmin/int.api*'` passed and built generation
    `2026-06-23--00-19-39`;
  - `nix develop -c confctl build --yes 'cz.vpsfree/machines/*/apu'` reached
    SMS module evaluation but failed on unrelated local state:
    `/srv/iso-images/systemrescue-11.01-amd64.iso` was missing.
    The relevant logs are
    `.confctl/logs/2026-06-22--23-21-39-confctl-build.log`,
    `.confctl/logs/2026-06-22--23-22-50-confctl-build.log`, and
    `.confctl/logs/2026-06-22--23-24-00-confctl-build.log`.
- Deployment and compatibility notes:
  - deploy the gateway package/config and secrets on both APUs before routing
    producers to it;
  - Alertmanager can be switched to the gateway independently of vpsAdmin SMS
    receiver creation because Alertmanager uses the high-priority queue;
  - vpsAdmin code/schema must be deployed before enabling user SMS receiver
    actions; old code ignores `users.sms_notifications_enabled`;
  - existing e-mail, webhook, and Telegram notification behavior is unchanged;
  - rollback can disable vpsAdmin SMS actions and point Alertmanager back to
    sachet while preserving the additive vpsAdmin schema until a later cleanup.
- Mandatory standalone change review:
  - requested from standalone reviewer `Hooke`
    (`019ef151-137e-7471-b510-ba6caf2a791f`) with the committed SMS gateway
    implementation packet covering all four affected repositories;
  - blocking findings:
    - gateway outbound and inbound webhook rows could remain stuck in
      `sending` after a crash/restart;
    - modem timeout handling could allow a retry or later SMS to start while
      the first modem send goroutine was still using the modem;
  - important findings:
    - gateway final vpsAdmin callbacks were best-effort and could leave
      vpsAdmin deliveries in `accepted`;
    - vpsAdmin SMS code confirmation had no failed-attempt throttling;
  - advisory findings:
    - gateway segment limiting counted runes rather than GSM-7/UCS-2
      segments;
    - the bundled-plugin SMS template commit body exceeded the workspace
      80-column rule;
  - follow-up:
    - amended the gateway commit to add restart recovery, persistent callback
      retry, synchronous modem sends under the modem lock, GSM-7/UCS-2 segment
      estimation, callback metrics, and regression tests;
    - autosquashed SMS verification lockout into the vpsAdmin SMS delivery
      commit and amended the bundled-plugin template commit message;
    - force-pushed rewritten `vpsfree-sms-gateway` and `vpsadmin` feature
      branches with lease;
    - amended the `vpsadminServices` config pin and added a generated
      `vpsfreeSmsGateway` pin update, then force-pushed
      `vpsfree-cz-configuration` with lease.

## 2026-06-23 SMS HMAC and dev-cluster refinement

- User refined the SMS plan:
  - gateway callbacks must use per-message HMAC signatures instead of
    predictable `client_message_id` or shared callback bearer tokens;
  - callback timestamps are accepted within a 20 minute window;
  - inbound SMS persistence remains supported by the gateway, but must be
    configurable and disabled by default;
  - current development gateway SQLite databases may be recreated, but the
    gateway should start versioned schema management for future migrations;
  - dev-cluster outbound SMS testing should use the fake gateway driver by
    default, with inbound persistence still opt-in.
- Implemented in `vpsfree-sms-gateway`:
  - vpsAdmin requests can include `callback_secret`;
  - queued outbound messages persist `callback_secret` but do not expose it in
    the status API;
  - final callbacks are signed with `X-VpsAdmin-SMS-Signature-Version`,
    `X-VpsAdmin-SMS-Timestamp`, and `X-VpsAdmin-SMS-Signature`;
  - signature input is version, HTTP method, callback path, timestamp, and the
    SHA256 hex digest of the raw JSON body, signed with HMAC-SHA256;
  - legacy shared bearer callbacks remain available only when a queued message
    has no `callback_secret`;
  - inbound persistence is controlled by `inbound.enabled`, defaults to false,
    and drops/drains modem inbound messages with a Prometheus counter when off;
  - fresh SQLite databases bootstrap `schema_migrations` version 1, while
    unversioned non-empty development databases fail with a recreate hint.
- Implemented in `vpsadmin`:
  - SMS payloads now include a generated per-message `callback_secret`;
  - the internal SMS callback endpoint verifies HMAC callbacks before applying
    final state;
  - legacy bearer callbacks are accepted only for old delivery payloads without
    a callback secret;
  - stale/future timestamps beyond 20 minutes, tampered bodies, invalid HMACs,
    and conflicting duplicate final callbacks are rejected;
  - duplicate same-state final callbacks are idempotent;
  - a fast gateway callback cannot be overwritten by the later accepted state;
  - SMS callback secrets are redacted from event delivery API detail payloads.
  - the endpoint coverage manifest lists the SMS verification send/confirm
    subactions that are covered by `event_routing_spec`.
- Implemented in dev-cluster support:
  - added `vpsfreeSmsGateway` flake input and local sibling worktree override;
  - services VM runs `vpsfree-sms-gateway.service` with the fake driver when
    the selected vpsAdmin checkout supports SMS notifications;
  - vpsAdmin SMS is enabled by default against
    `http://127.0.0.1:9876/v1/sms`;
  - seeded dev users have `smsNotificationsEnabled = true`;
  - `sms.inbound.enable` remains false by default and is documented as opt-in.
- Implemented in `vpsfree-cz-configuration`:
  - the `services.vpsfreeSmsGateway.callbackTokenFile` option is now optional;
  - callback bearer token rendering happens only when the option is set;
  - production APUs keep the legacy callback token configured for rollout
    compatibility and explicitly set `inbound.enabled = false`.
- Verification:
  - `CGO_ENABLED=0 go test ./...` passed in `vpsfree-sms-gateway`;
  - vpsAdmin focused specs passed:
    `nix develop .#api -c bundle exec rspec
    spec/models/tasks/event_delivery_spec.rb
    spec/api/resources/event_routing_spec.rb`
    before review (91 examples, 0 failures, 1 pending);
  - vpsAdmin touched-file RuboCop passed:
    `nix develop .#api -c bundle exec rubocop ...`;
  - Ruby syntax checks passed for touched API/model/spec files;
  - `jq empty dev-clusters/vpsadmin/default-config.json` passed;
  - `bash -n dev-clusters/vpsadmin/bin/devcluster` passed;
  - `nix-instantiate --parse` passed for touched vpsAdmin modules,
    dev-cluster Nix files, and production configuration Nix files;
  - `git diff --check` passed in the gateway, vpsAdmin, production config, and
    for the touched dev-cluster files.
- Commits:
  - `vpsfree-sms-gateway`
    `f68b1ba405cb693b7cfb426bcaf668a99bf4599c`
    (`Add HMAC SMS callbacks`);
  - `vpsadmin`
    `9fc16f62b6ad1339772055dfb6bec11784149a01`
    (`notifications: verify SMS callbacks with HMAC`);
  - workspace/dev-cluster
    `413a413140864992b31b2a5d6429f85266e74f81`
    (`devcluster: run fake SMS gateway`);
  - `vpsfree-cz-configuration`
    `573202f6bd0539baf68edb916286c1c4b94411f8`
    (`vpsadmin-config: make SMS callback token optional`);
  - `vpsfree-cz-configuration`
    `3aa2c5d5438aa9095ac2b10f790b5195c58ea6ee`
    (`inputs: set vpsfreeSmsGateway to f68b1ba4`);
  - `vpsfree-cz-configuration`
    `f7b07aaba57774482f3315db3115e9b32b22f5b5`
    (`inputs: set vpsadminServices to b4fbebe1`);
  - `vpsfree-cz-configuration`
    `8bf74b5d1ff64f13f1af584dc3bcf8afb4b4ac37`
    (`inputs: set vpsadminServices to 9fc16f62`).
- Mandatory change review requested from standalone reviewer `Poincare`
  (`019ef548-5832-71f0-a60e-79ec31715253`) with the four committed SMS HMAC,
  dev-cluster, and configuration commits listed above.
- Review findings and follow-up:
  - fixed the blocking vpsAdmin callback state race by locking SMS deliveries
    while transitioning from queued/running/accepted to final callback states
    and while recording accepted gateway handoff results;
  - hardened the public callback endpoint by authenticating unknown or non-SMS
    `client_message_id` values as generic SMS callback authorization failures
    and by limiting callback request bodies to 16 KiB;
  - added a future-timestamp HMAC regression test;
  - made the dev-cluster SMS gateway support check tolerate older vpsAdmin
    checkouts without `nixos/modules/vpsadmin/notifications.nix`;
  - added a dev-cluster legacy callback token file for pre-HMAC vpsAdmin
    checkouts and pointed the gateway flake input at the pushed feature branch
    instead of a non-existent upstream `master` branch;
  - amended and pushed `vpsadmin` and `vpsfree-sms-gateway` branches, then
    updated production config pins with `confctl` in gateway-first order.
  - after GitHub Actions reported missing endpoint coverage entries for
    `notification_receiver.action#send_sms_verification_code` and
    `notification_receiver.action#confirm_sms_verification_code`, amended the
    vpsAdmin commit, force-pushed with lease, and repinned `vpsadminServices`
    to `9fc16f62`.
- Post-review verification:
  - `nix develop .#api -c bundle exec rspec
    spec/models/tasks/event_delivery_spec.rb
    spec/api/resources/event_routing_spec.rb` passed after fixes
    (94 examples, 0 failures, 1 pending);
  - `nix develop .#api -c bundle exec rubocop
    lib/vpsadmin/api.rb lib/vpsadmin/api/notifications.rb
    spec/models/tasks/event_delivery_spec.rb` passed;
  - `nix develop .#api -c bundle exec rspec
    spec/api/endpoint_coverage_spec.rb` passed after adding the endpoint
    manifest entries (1 example, 0 failures);
  - Ruby syntax checks passed for the touched vpsAdmin API/spec files;
  - `git diff --check` passed in vpsAdmin and for touched dev-cluster files;
  - `jq empty dev-clusters/vpsadmin/default-config.json`,
    `bash -n dev-clusters/vpsadmin/bin/devcluster`, and
    `nix-instantiate --parse` on touched dev-cluster Nix files passed;
  - production config parse checks passed for `flake.nix` and
    `modules/services/vpsfree-sms-gateway.nix`;
  - `nix develop -c confctl build -y
    'cz.vpsfree/vpsadmin/int.api{1,2}'` passed and built generation
    `2026-06-23--19-13-47` with vpsAdmin `9fc16f62`;
  - `nix develop -c confctl build -y
    'cz.vpsfree/machines/{brq,prg}/apu'` was attempted but remains blocked by
    the unrelated missing local file
    `/srv/iso-images/systemrescue-11.01-amd64.iso`;
  - `nix build .#default` passed in `vpsfree-sms-gateway`.
- Deployment compatibility after the HMAC refinement:
  - deploy/pin the HMAC-capable gateway revision before deploying the vpsAdmin
    Services revision that sends `callback_secret`;
  - production APUs keep the legacy callback token for queued/pre-HMAC
    messages, but new per-message HMAC callbacks are preferred;
  - dev-cluster SMS testing can use the fake gateway by default, with inbound
    persistence still disabled unless `sms.inbound.enable = true`.

## 2026-06-23 final SMS gateway follow-up

- While validating the dev-cluster SMS dispatcher, found that RabbitMQ
  notification-user permissions still allowed only
  `vpsadmin.notifications.(email|telegram|webhook)`. This prevented the SMS
  dispatcher from declaring `vpsadmin.notifications.sms`.
- Fixed and pushed vpsAdmin commit
  `936b9e26a987f006321e80bf4d642858c061b998`
  (`notifications: allow SMS RabbitMQ queue access`).
- Updated and pushed production config pin
  `ddefd817f624d57b7bc1f4bf6fa1f85191f3e8bc`
  (`inputs: set vpsadminServices to 936b9e26`).
- Dev-cluster validation:
  - first `devcluster update 2026-06-15-vpsadmin-events services` attempt
    failed because the services VM `/nix/store` was full;
  - ran `nix-collect-garbage -d` in the services VM, reducing `/nix/store`
    usage from 100% to 88%, then retried the update;
  - the retry started `vpsfree-sms-gateway.service`, but RabbitMQ had no
    visible users/vhosts while its bootstrap marker existed, so dispatchers
    failed authentication;
  - restarted `rabbitmq.service`, restored the dev bootstrap marker after
    confirming the vhost/users existed, and applied the updated notification
    queue permissions manually to the running VM;
  - final service check showed `vpsadmin-notification-dispatcher-{email,sms,
    telegram,webhook}.service`, `vpsadmin-supervisor.service`,
    `vpsfree-sms-gateway.service`, and `rabbitmq.service` all active;
  - `rabbitmqctl list_queues -p vpsadmin_test name` includes
    `vpsadmin.notifications.sms`;
  - `curl -fsS http://127.0.0.1:9876/metrics` from the services VM returns
    gateway metrics including inbound counters, modem readiness, outbound
    gauges, and callback counters.
- Additional verification:
  - `ruby -c tools/rabbitmqcfg.rb` passed;
  - `ruby tools/rabbitmqcfg.rb user --vhost vpsadmin_test --perms
    notification notification:test` emits the SMS-aware queue regex;
  - vpsAdmin hooks passed on the RabbitMQ permission commit;
  - `nix develop -c confctl build -y
    'cz.vpsfree/vpsadmin/int.api{1,2}'` passed with vpsAdmin
    `936b9e26a987f006321e80bf4d642858c061b998`, building generation
    `2026-06-23--19-53-23`.
- GitHub Actions:
  - latest vpsAdmin RuboCop for `936b9e26` completed successfully;
  - latest aggregate vpsAdmin CI for `936b9e26` is still in progress as of
    this update.

## 2026-06-23 per-user delivery method controls

- User asked to replace the SMS-specific user flag with a scalable per-user
  configuration table for all event delivery methods: `email`, `webhook`,
  `telegram`, and `sms`.
- Implemented and committed vpsAdmin commit
  `fb120863ea8ff08e997bbeccd8aa54ea169ac985`
  (`notifications: add per-user delivery method controls`) on branch
  `2026-06-15-vpsadmin-events`.
- Implementation details:
  - replaced the pending SMS-only migration with
    `user_notification_delivery_methods`;
  - missing rows default to enabled, while legacy `users.mailer_enabled = 0`
    users are backfilled to `email = false`;
  - added `UserNotificationDeliveryMethod` and user helpers for querying and
    setting delivery method enablement;
  - exposed `user.notification_delivery_method` HaveAPI index/show/update
    actions, with update restricted to admins and read access allowed for
    admins or the affected user;
  - removed non-admin user updates of legacy `mailer_enabled`;
  - receiver action create/update rejects disabled methods for ordinary users,
    while admin create/update auto-enables the method for the target user;
  - routing and dispatcher claim paths skip or cancel existing receiver actions
    when their method is disabled;
  - SMS verification send refuses disabled SMS for the target user;
  - WebUI admin member edit now shows admin-only delivery-method checkboxes;
  - WebUI notification receiver forms hide disabled methods for ordinary users
    and display disabled status on existing actions.
- Verification:
  - Ruby syntax checks passed for touched API/model/spec files;
  - `php -l webui/forms/notifications.forms.php` passed;
  - `php -l webui/pages/page_adminm.php` passed;
  - `git diff --check` passed;
  - focused specs passed:
    `nix develop .#api -c bundle exec rspec
    spec/models/notification_receiver_action_spec.rb
    spec/api/resources/user_write_spec.rb
    spec/api/resources/event_routing_spec.rb
    spec/models/tasks/event_delivery_spec.rb`
    (170 examples, 0 failures, 2 pending);
  - touched-file RuboCop passed:
    `nix develop .#api -c bundle exec rubocop ...`;
  - hooks passed:
    `nix develop -c overcommit --run pre-commit`.
- Commit note:
  - first commit attempt outside the Nix shell failed because the hook wrapper
    could not find `overcommit`; no commit was created;
  - final commit used `nix develop -c git commit -F <tmpfile>` and hooks
    passed.
- Mandatory change review:
  - requested from standalone reviewer `Boole`
    (`019ef61b-70d4-7cd0-ac1f-e64ffd388fd2`) using
    `skills/mandatory-change-review/SKILL.md`;
  - review found one blocking issue: lazy default receiver creation could fail
    when e-mail delivery was disabled and the user had no receivers, because
    the generated default e-mail action hit the new delivery-method
    validation;
  - review found one important issue: admin create/update enabled a delivery
    method before the receiver action save, so an invalid action could still
    re-enable the method;
  - review noted an advisory compatibility caveat: development or staging
    databases that already recorded the superseded SMS-only migration timestamp
    `20260622220000` must be recreated or have that migration record removed
    before running this branch, otherwise the replacement delivery-method table
    migration will be skipped.
- Review follow-up fixes:
  - vpsAdmin's lazy default e-mail action creation can bypass only the
    delivery-method validation, so disabled e-mail creates the existing action
    and event routing records a skipped delivery instead of raising;
  - admin receiver-action create/update now saves the action first with only
    delivery-method validation bypassed, then enables the method after a
    successful save, all inside one transaction;
  - added regression specs for disabled e-mail lazy defaults and failed admin
    receiver-action create/update preserving disabled method state.
- Post-review verification:
  - `nix develop .#api -c bundle exec rspec
    spec/api/resources/event_routing_spec.rb` passed
    (32 examples, 0 failures, 1 pending);
  - focused specs passed:
    `nix develop .#api -c bundle exec rspec
    spec/models/notification_receiver_action_spec.rb
    spec/api/resources/user_write_spec.rb
    spec/api/resources/event_routing_spec.rb
    spec/models/tasks/event_delivery_spec.rb`
    (173 examples, 0 failures, 2 pending);
  - touched-file RuboCop passed on 13 files;
  - PHP syntax checks passed for the two touched WebUI files;
  - `git diff --check` passed;
  - `nix develop -c overcommit --run pre-commit` passed.

## 2026-06-24 Dev-cluster Telegram notification diagnosis

- Investigated why Telegram receiver actions could not be created in the
  running dev cluster even though `.dev-clusters/vpsadmin/telegram/bot-token`
  exists on the host.
- Found that the live `services` VM had been evaluated without Telegram:
  - `vpsadmin-notification-dispatcher-telegram.service` was not present;
  - `vpsadmin-telegram-receiver.service` was not present;
  - `/var/lib/vpsadmin/devcluster-telegram` was absent;
  - generated notification configs had no active Telegram service config.
- Cause: the token directory is read by `dev-clusters/vpsadmin/bin/devcluster`
  during Nix evaluation. If the token is added after the cluster or services VM
  has already been built, the running VM is not updated automatically.
- Ran `dev-clusters/vpsadmin/bin/devcluster update
  2026-06-15-vpsadmin-events services`.
- Post-update verification:
  - `vpsadmin-api.service`,
    `vpsadmin-notification-dispatcher-telegram.service`, and
    `vpsadmin-telegram-receiver.service` are active;
  - `systemctl --failed --no-pager` listed 0 failed units;
  - `/var/lib/vpsadmin/devcluster-telegram/bot-token` exists as a root-only
    credential source;
  - API, Telegram dispatcher, and Telegram receiver notification configs all
    report Telegram enabled/configured for `vpsadmin_aitherdev_bot`;
  - fresh logs show both Telegram services started cleanly.
- Per-user delivery-method enablement is separate from global Telegram
  configuration: users cannot create actions for disabled methods, while an
  admin-created receiver action skips that validation and enables the method for
  the target user after successful creation.

## 2026-06-25 SMS gateway inspection CLI

- Implemented a read-only `vpsfree-sms-gatewayctl` companion command in
  `vpsfree-sms-gateway`:
  - opens the gateway SQLite database read-only and query-only;
  - validates the schema version without using the migratable store opener;
  - supports `stats`, `outbound list/show`, `callbacks list`,
    `inbound list/show`, and `inbound-webhooks list`;
  - table output is default, `--format json` is available for scripting;
  - JSON and table output do not expose outbound `callback_secret`.
- Added inspector and CLI tests covering queue reads, missing/unversioned/newer
  databases, query-only protection, JSON stats, table outbound listing, and
  callback-secret redaction.
- Updated `vpsfree-sms-gateway` packaging to include both
  `vpsfree-sms-gateway` and `vpsfree-sms-gatewayctl`.
- Updated dev-cluster wiring so the services VM installs the SMS gateway
  package into `PATH` when the fake SMS gateway is enabled, and documented the
  `devcluster ssh ... vpsfree-sms-gatewayctl outbound list --source vpsadmin`
  verification workflow.
- Updated the production `vpsfree-cz-configuration` SMS gateway module to add
  the configured gateway package to `environment.systemPackages` when enabled.
- Verification so far:
  - ambient `go test ./...` failed because the shell lacks `gcc` for the SQLite
    dependency;
  - `nix develop -c go test ./...` passed;
  - `nix build .#default` in `vpsfree-sms-gateway` passed after staging new
    files so the flake source included the new command;
  - built package contains both `vpsfree-sms-gateway` and
    `vpsfree-sms-gatewayctl`;
  - `git diff --check` passed for the touched gateway, dev-cluster, and
    configuration files.
- Commits:
  - `vpsfree-sms-gateway` `3cac063dc8c86402a3ade6e2384dd5334a00c300`
    (`sms: add read-only gateway inspection cli`), pushed to
    `origin/2026-06-15-vpsadmin-events`;
  - workspace/dev-cluster `84c83dd` (`devcluster: expose sms gateway
    inspection cli`);
  - `vpsfree-cz-configuration` `285f2c11` (`sms-gateway: install package tools
    on gateway hosts`);
  - `vpsfree-cz-configuration` `45410d75` (`inputs: set vpsfreeSmsGateway to
    3cac063d`) generated by `confctl inputs channel set --commit`.
- `confctl inputs channel set` first failed because I mistyped the full gateway
  commit hash; retrying with
  `3cac063dc8c86402a3ade6e2384dd5334a00c300` succeeded.
- Targeted production config build:
  - `confctl build 'cz.vpsfree/machines/{brq,prg}/apu'` without `-y` failed at
    the confirmation prompt in the noninteractive shell;
  - `nix develop --command confctl build -y
    'cz.vpsfree/machines/{brq,prg}/apu'` reached Nix system build and failed
    because `/srv/iso-images/systemrescue-11.01-amd64.iso` is missing. This
    appears unrelated to SMS gateway changes.
- Mandatory change review was launched with standalone reviewer
  `019efe2a-88e0-7733-a719-c0d33ec6d8b8` after the quick checks above and
  before the dev-cluster update.
- Mandatory change review result:
  - reviewer reported no blocking, important, or advisory findings;
  - independent checks passed: `nix develop -c go test ./...` in
    `vpsfree-sms-gateway`, `nix-instantiate --parse` for touched Nix files, and
    `git diff --check` for all three reviewed diffs;
  - residual gaps noted: dev-cluster update still pending, production
    `confctl build` blocked by missing SystemRescue ISO, and no explicit test
    for inspecting an actively running WAL database with uncheckpointed writes.
- Dev-cluster update:
  - `dev-clusters/vpsadmin/bin/devcluster update
    2026-06-15-vpsadmin-events services` completed successfully;
  - `/run/current-system/sw/bin/vpsfree-sms-gatewayctl` exists in the services
    VM;
  - `vpsfree-sms-gateway.service` is active and `systemctl --failed` lists 0
    failed units;
  - `vpsfree-sms-gatewayctl stats` reads the live gateway DB;
  - posting a dev vpsAdmin-style SMS directly to
    `http://127.0.0.1:9876/v1/sms` with the dev token returned queued message
    ID 1, and after 2 seconds `vpsfree-sms-gatewayctl outbound list --source
    vpsadmin --limit 5` showed it as `sent` with provider ID `fake-1`.
- Amended the wording commit with the review fixes. Final amended head is
  `d84bf1c67` (`notifications: update event wording`).
  Commit-msg `TextWidth` again reported 72-column warnings only; all message
  lines are under the workspace 80-column rule.
- Final mandatory change review:
  - Standalone reviewer `019ef9f2-554c-7433-9b1c-3ddefea690f5` reviewed
    `58c744d56c6db871539b3f4d178d4ef568e9e4d7..d84bf1c67`.
  - Result: no blocking, important, or advisory findings.
  - Reviewer confirmed the previous stale metadata/label findings were
    resolved and remaining e-mail/mail wording is e-mail-action, address,
    mail-log, Message-ID/thread, or rendering-internal specific.
  - Residual noted gaps: reviewer did not rerun full supplied RSpec/hooks or
    browser checks; WebUI gettext catalogs remain unregenerated, consistent
    with this slice.
- Pushed final amended head `d84bf1c67` to
  `origin/2026-06-15-vpsadmin-events`.
- GitHub Actions started for `d84bf1c67`:
  - API Specs (topic parallel) run `28104636107` queued;
  - RuboCop run `28104636187` in progress;
  - Webui PHPUnit run `28104636111` in progress;
  - aggregate CI run `28104636125` in progress.
- GitHub Actions update:
  - RuboCop run `28104636187` passed;
  - Webui PHPUnit run `28104636111` passed;
  - API Specs run `28104636107` is in progress;
  - aggregate CI run `28104636125` is in progress.
- API Specs run `28104636107` failed because job
  `API specs (full) - network` failed during `Install system dependencies`
  before Ruby setup or RSpec:
  - `apt-get update` received HTTP 403 from
    `https://packages.microsoft.com/repos/azure-cli` and
    `https://packages.microsoft.com/ubuntu/24.04/prod`;
  - Ubuntu/MariaDB repository fetches otherwise proceeded;
  - no project code or tests ran in the failed job.
  This is an external GitHub runner package-repository failure, not a code
  failure. Rerunning failed API jobs after recording the root cause.
- Rerun of failed API Specs jobs for run `28104636107` passed.
- Aggregate CI run `28104636125` remains in progress at about 30 minutes,
  running the selected ci-tagged tests.
- Aggregate CI run `28104636125` remains in progress after about 1h06m:
  selection/preview completed successfully and the `Run tests` step is still
  running. No failure log is available because the job has not completed.
- Push and GitHub Actions:
  - pushed vpsAdmin branch `2026-06-15-vpsadmin-events` to
    `origin` at `fb120863ea8ff08e997bbeccd8aa54ea169ac985`;
  - first push attempt outside the Nix shell failed before contacting GitHub
    because the local Overcommit pre-push hook could not find the gem;
  - retrying with `nix develop -c git push origin
    2026-06-15-vpsadmin-events` succeeded;
  - GitHub Actions for `fb120863e` at the last poll:
    `Webui PHPUnit`, `RuboCop`, and `libnodectld Specs` passed;
    `API Specs (topic parallel)` was in progress and aggregate `CI` was
    queued, with no failure available to inspect.

## 2026-06-23 remove legacy mailer switch and add default mute receiver

- User requested removal of the legacy `users.mailer_enabled` field and a
  default `Mute` receiver for every user, so selected event routes can be
  muted easily by routing to `Mute` with `continue = false`.
- Implemented in vpsAdmin commit
  `c3a0b69cd155bb1082d6d328f4be762a4c151ef1`
  (`notifications: remove legacy mailer switch`):
  - added migration `20260623210000_remove_users_mailer_enabled`;
  - removed `mailer_enabled` from `api/db/schema.rb`, `User`, the User API
    resource, and the admin member-create WebUI path;
  - migrated old disabled mailer state into
    `user_notification_delivery_methods(email=false)` and generated default
    routing;
  - generated default receivers are now `Default e-mail` plus `Mute` for every
    user, bypassing only receiver-count validation for generated rows;
  - default routes are still user-manageable: generated maintenance only fills
    a missing receiver and does not overwrite custom receivers;
  - normalized legacy generated muted receivers named `Do not notify` to
    `Mute`;
  - updated request-plugin admin recipient grouping to prefer admins whose
    e-mail delivery method is enabled without querying the removed column;
  - removed the lingering `mailer_enabled: true` assignment from registration
    approval;
  - updated specs/helpers to express muted notifications through the generated
    `Mute` receiver instead of the removed user column.
- Compatibility:
  - old deployments can migrate forward because `mailer_enabled` remains
    available to the new removal migration until it drops the column;
  - rollback re-adds `users.mailer_enabled` and sets it false for users with
    e-mail delivery disabled;
  - the earlier events migration tolerates schemas where `mailer_enabled` was
    already removed by treating missing values as enabled;
  - historical migrations still mention `mailer_enabled`; live schema/code no
    longer do.
- Verification run so far:
  - Ruby syntax checks passed for touched Ruby files, including the new
    migration and support helper;
  - `php -l webui/pages/page_adminm.php` passed;
  - `git diff --check` passed after adding intent-to-add entries for the new
    files;
  - focused notification/user specs passed:
    `nix develop .#api -c bundle exec rspec
    spec/models/event_route_spec.rb
    spec/api/resources/event_routing_spec.rb
    spec/api/resources/user_write_spec.rb
    spec/models/notification_receiver_action_spec.rb
    spec/models/tasks/event_delivery_spec.rb`
    (197 examples, 0 failures, 2 pending);
  - broader touched transaction/API specs passed:
    `nix develop .#api -c bundle exec rspec
    spec/api/plugins/payments/user_payment_spec.rb
    spec/api/resources/vps_write_spec.rb
    spec/models/security_advisory_spec.rb
    spec/models/transaction_chains/lifetimes/expiration_warning_spec.rb
    spec/models/transaction_chains/migration_plan/mail_spec.rb
    spec/models/transaction_chains/plugins/monitoring/alert_spec.rb
    spec/models/transaction_chains/plugins/outage_reports/update_spec.rb
    spec/models/transaction_chains/plugins/payments/create_spec.rb
    spec/models/transaction_chains/plugins/requests/create_spec.rb
    spec/models/transaction_chains/plugins/requests/resolve_spec.rb
    spec/models/transaction_chains/plugins/requests/update_spec.rb
    spec/models/transaction_chains/user/create_spec.rb
    spec/models/transaction_chains/vps/replace/os_spec.rb`
    (191 examples, 0 failures);
  - requests-create focused rerun passed after fixing the plugin recipient
    query (4 examples, 0 failures);
  - `nix develop .#api -c bundle exec rspec
    spec/smoke/core_schema_spec.rb` passed (2 examples, 0 failures);
  - RuboCop passed for 26 changed Ruby source/spec/migration files excluding
    generated `db/schema.rb`; including the generated schema reports the
    repository's existing schema style offenses.
- Commit/hook status:
  - `nix develop -c overcommit --run pre-commit` passed before the commit;
  - commit used `nix develop -c git commit -F <tmpfile>`;
  - commit-time hooks passed: Nixfmt, PhpCsFixer, RuboCop;
  - commit-msg hooks passed with TextWidth warnings at 72 columns; all
    commit-message lines remain within the workspace 80-column rule.
- Mandatory change review:
  - requested from standalone reviewer `Darwin`
    (`019ef664-5304-7553-acaa-fc89f7386461`) using
    `skills/mandatory-change-review/SKILL.md`;
  - blocking finding: integration tests still used the removed
    `mailer_enabled` attribute in user creation/setup helpers, which would
    fail after the current schema loaded;
  - important finding: deployment notes needed to explicitly state that this
    removal slice is not mixed-version compatible after the migration drops
    `users.mailer_enabled`;
  - advisory finding: direct up/down migration verification would further
    protect the exact production upgrade path.
- Review follow-up fixes:
  - integration test helper `set_user_mailer_enabled` was replaced by
    `set_user_default_email_enabled`, which disables/enables the e-mail
    delivery method and points the generated default route to either
    `Default e-mail` or `Mute`;
  - stale `mailer_enabled: true` user setup attributes were removed from
    network and user integration helpers;
  - the WebUI integration fixture now explicitly disables e-mail delivery and
    routes defaults to `Mute` after saving the user;
  - `plan.md` now records that old API/WebUI/model code cannot run after the
    removal migration and that rollback to old code requires migrating down
    first.
- Post-review verification:
  - parsed changed Nix test files with `nix-instantiate --parse`;
  - `ruby tests/ci-selection-test.rb` passed
    (15 runs, 54 assertions, 0 failures);
  - `git diff --check` passed;
  - live search for `mailer_enabled` now only finds historical migrations and
    compatibility migration code;
  - Overcommit pre-commit hooks passed after staging the review fixes;
  - amended commit used `nix develop -c git commit --amend -F <tmpfile>` and
    commit-time hooks passed again.
- Next steps:
  - push and inspect GitHub Actions;
  - deploy to the dev cluster, recreating it if the removed column or prior
    branch migrations make that simpler.

## 2026-06-23 dev-cluster deployment follow-up

- Pushed vpsAdmin commit:
  `c3a0b69cd155bb1082d6d328f4be762a4c151ef1`
  (`notifications: remove legacy mailer switch`).
- Initial dev-cluster update command:
  `dev-clusters/vpsadmin/bin/devcluster update
  2026-06-15-vpsadmin-events services`.
- The update failed because `vpsadmin-devcluster-seed.service` generated a
  seed file that still assigned `mailer_enabled: true`, which is no longer a
  valid `User` attribute after the removal migration. `vpsadmin-api.service`
  then failed only because it depends on the seed service.
- Fixed tracked workspace file `dev-clusters/vpsadmin/nix/test.nix` in commit
  `56d3ff59174a06762b8c2b4ab51dc8e65b01c7bd`
  (`devcluster: seed notification delivery methods`):
  - removed the legacy `mailer_enabled` assignment;
  - maps `smsNotificationsEnabled` seed data to the new per-user `sms`
    delivery method when the method/table exist;
  - ensures generated default notification receivers/routes for existing
    seeded users when the new notification tables exist;
  - keeps the code guarded for older vpsAdmin checkouts.
- Quick verification for the workspace seed commit:
  - `nix-instantiate --parse dev-clusters/vpsadmin/nix/test.nix` passed;
  - `git diff --check -- dev-clusters/vpsadmin/nix/test.nix` passed;
  - `rg -n "mailer_enabled"
    dev-clusters/vpsadmin/nix/test.nix
    dev-clusters/vpsadmin/default-config.json` found no matches.
- A fresh mandatory change review was requested from standalone reviewer
  `Maxwell` (`019ef676-cf12-7b20-9498-2b5ae26ebfdb`) before retrying the
  dev-cluster deployment.
- Review result from `Maxwell`:
  - no blocking or important findings;
  - advisory finding: the workspace commit message needed rewrapping to the
    80-column rule.
- Amended and pushed workspace commit:
  `7025b66253a3a39cd9116105d7d8853dbace2f9e`
  (`devcluster: seed notification delivery methods`).
- Retried `devcluster update 2026-06-15-vpsadmin-events services`; the update
  succeeded and cleared the original seed failure. Post-update checks:
  - `devcluster status 2026-06-15-vpsadmin-events` reported `ready: yes` on
    the bridge network;
  - `systemctl --failed` on `services` listed no failed units;
  - API and WebUI returned HTTP 200;
  - `vpsadmin-devcluster-seed.service` completed successfully;
  - `vpsadmin-api.service` and `vpsfree-sms-gateway.service` were active.
- A DB sanity check then found that the deployed DB was inconsistent:
  `schema_migrations` contained `20260622220000`, but the table
  `user_notification_delivery_methods` was missing. The packaged schema in
  the Nix store contained the table, but
  `/var/lib/vpsadmin/database/cache/schema.rb` was stale and did not contain
  it.
- Root cause: `nixos/modules/vpsadmin/database-setup.nix` copied the packaged
  schema into the mutable schema cache only when the cache did not already
  exist. The long-running services use this cache through `SCHEMA`, so service
  updates could keep an older schema body while migrations were marked as
  current.
- Initial fix in vpsAdmin commit
  `f2ffbfd5d0c86c9ea3ef88dbc0982d0e2bf05298`
  refreshed only the database setup cache.
- Quick verification for the schema-cache fix:
  - `nix-instantiate --parse nixos/modules/vpsadmin/database-setup.nix`
    passed;
  - `git diff --check HEAD~1..HEAD` passed;
  - `nix develop -c overcommit --run pre-commit` passed;
  - commit-time hooks passed.
- Mandatory change review from standalone reviewer `Galileo`
  (`019ef684-3576-7b90-86d4-6496bb212a25`) found no blocking issues, but
  reported one important gap: API, rake, notification dispatcher, Telegram
  receiver, and supervisor units have separate `SCHEMA` cache paths that are
  populated by shared `apiApp.setup`, so refreshing only the database setup
  cache would not keep runtime caches current.
- Addressed by amending the vpsAdmin fix to
  `5d3583b96d9e7a56b4510d1e9a3be45d87fb1368`
  (`nixos: refresh cached API schemas on setup`):
  - `apiApp.setup` now creates `${stateDirectory}/cache` and copies the
    packaged `${package}/${name}/db/schema.rb` into
    `${stateDirectory}/cache/schema.rb`;
  - the database-only duplicate refresh was removed so the shared setup owns
    the behavior for every app package.
- Quick verification for the amended schema-cache fix:
  - `nix-instantiate --parse nixos/modules/vpsadmin/api-app.nix` passed;
  - `nix-instantiate --parse nixos/modules/vpsadmin/database-setup.nix`
    passed;
  - `git diff --check HEAD~1..HEAD` passed;
  - `nix develop -c overcommit --run pre-commit` passed;
  - amend commit-time hooks passed.
- Final mandatory change review from standalone reviewer `Newton`
  (`019ef68a-b762-7fd2-adec-82f3172dde7a`) reported no blocking,
  important, or advisory findings for the amended commit. Residual risk was
  the lack of a fresh dev-cluster deployment, which was done next.
- Pushed vpsAdmin branch with latest head
  `5d3583b96d9e7a56b4510d1e9a3be45d87fb1368`.
- Reset and recreated the dev cluster:
  - `devcluster reset 2026-06-15-vpsadmin-events` stopped the previous
    cluster after timeout and removed its state;
  - `devcluster start 2026-06-15-vpsadmin-events --topology single
    --network bridge` rebuilt and started the fresh cluster.
- First fresh start reached node preparation and exited with
  `error: group not found` while adding devices to the node pool group
  `/default`. The cluster itself reported `ready: yes`, services were running,
  and a subsequent node probe showed `/default` existed and `nodectld` was
  running. Reran `devcluster refresh 2026-06-15-vpsadmin-events`, which passed.
- Final dev-cluster checks:
  - `devcluster status` reports running, topology `single`, network `bridge`,
    `ready: yes`;
  - `systemctl --failed` on `services` reports no failed units;
  - API `https://api.aitherdev.int.vpsfree.cz/` returns HTTP 200;
  - WebUI `https://webui.aitherdev.int.vpsfree.cz/` returns HTTP 200;
  - `vpsadmin-api.service`, e-mail/webhook/SMS notification dispatchers, and
    `vpsfree-sms-gateway.service` are active; the seed service is an inactive
    successful oneshot;
  - SMS gateway metrics on `127.0.0.1:9876/metrics` report modem ready and
    zero queued/sending/failed/sent messages for both alertmanager and
    vpsAdmin sources;
  - DB has `user_notification_delivery_methods`;
  - `users.mailer_enabled` is absent;
  - delivery method rows are `email=enabled` for 2 users and `sms=enabled` for
    2 users from the dev seed;
  - `Default e-mail` receivers exist for 3 users and `Mute` receivers exist
    for 3 users;
  - schema migrations `20260622220000` and `20260623210000` are present;
  - cached schemas for API, database setup, e-mail/SMS/webhook dispatchers,
    and supervisor all contain `user_notification_delivery_methods` and do
    not contain `mailer_enabled`;
  - node1 `nodectld` reports `State: running` and pool groups `/` and
    `/default` exist.
- GitHub Actions:
  - pushed commit `c3a0b69cd` had RuboCop, Webui PHPUnit, libnodectld Specs,
    and API Specs (topic parallel) successful;
  - pushed commit `5d3583b96` created CI run `28060815530`;
  - obsolete in-progress CI runs for superseded branch commits
    `28058949971`, `28055282976`, and `28043379238` were cancelled so the
    latest run could start;
  - latest CI run `28060815530` is in progress as of this note; setup,
    checkout, test selection, and selected-test preview steps passed, and the
    `Run tests` step started at 2026-06-23 22:34:34 UTC. GitHub does not
    expose logs for the running job until it completes.

## 2026-06-24 WebUI delivery method form

- Implemented commit `9e7569d4466111e0390f7b641518c8b8bd150c07`
  (`webui: split event delivery method settings`).
- Changed `webui/pages/page_adminm.php` so admin-only per-user event delivery
  method toggles are rendered as a standalone form below the `Contact`
  section instead of being embedded in the main profile form.
- Added a dedicated `notification_delivery_methods` POST action that is
  admin-only, CSRF-protected, and updates delivery methods through the
  existing user notification delivery method API.
- Removed the generic hint text
  `Allow this user to configure and receive this event delivery method.`;
  each row now mentions the concrete method label.
- Quick verification:
  - `php -l webui/pages/page_adminm.php` passed;
  - `git diff --check -- webui/pages/page_adminm.php` passed;
  - searched for the old generic hint and confirmed it is gone;
  - `nix develop -c overcommit --run pre-commit` passed;
  - commit-time hooks passed.
- Mandatory change review:
  - Standalone reviewer `019ef896-c5d2-76f2-be00-238e93ee1380` reviewed
    `5d3583b96d9e7a56b4510d1e9a3be45d87fb1368..9e7569d4466111e0390f7b641518c8b8bd150c07`.
  - Result: no blocking, important, or advisory findings.
  - Residual noted test gap: no browser integration test was run for this
    narrow PHP form reshaping.
- Pushed `9e7569d4466111e0390f7b641518c8b8bd150c07`; Webui PHPUnit run
  `28083574968` passed, while aggregate CI run `28083574984` was queued.
- Investigated earlier aggregate CI failure `28060815530` on
  `5d3583b96d9e7a56b4510d1e9a3be45d87fb1368` before trusting newer CI:
  - downloaded artifact `vpsadmin-test-logs-28060815530`;
  - `services-up` was waiting for exactly 3 template variant rows, but built-in
    templates now install e-mail, Telegram, and SMS variants, so the query
    returned 9;
  - alert tests had matching Mailpit messages, but subjects ended with an
    encoded trailing newline (`=0A`) from `.subject.erb` files;
  - WebUI support-pages failed because the fixture disabled e-mail delivery
    for every generated user while the test expected a regular user to create
    an e-mail receiver action.
- Implemented follow-up commit
  `3f6e57cfc65a78922560866a7225b337419f8bfd`
  (`notifications: fix delivery test assumptions`):
  - normalizes persisted/rendered notification template subjects before storing
    them in `MailLog`, including no-vars sends;
  - adds a no-vars static subject regression spec;
  - makes `services-up` count only e-mail template variants using explicit
    enum ordinal `0`;
  - enables e-mail delivery for the primary WebUI browser fixture user while
    leaving other generated users muted by default.
- Follow-up verification:
  - `ruby -c api/models/notification_template.rb` passed;
  - `ruby -c api/models/notification_template_variant.rb` passed;
  - `ruby -c api/spec/models/notification_templates_spec.rb` passed;
  - `nix-instantiate --parse tests/suite/services-up.nix` passed;
  - `nix-instantiate --parse tests/suite/webui.nix` passed;
  - `git diff --check` passed;
  - `nix develop .#api -c bundle exec rspec
    spec/models/notification_templates_spec.rb` passed with 9 examples;
  - `nix develop -c overcommit --run pre-commit` passed;
  - amend commit-time hooks passed (`Nixfmt`, `RuboCop`; `TextWidth` advisory
    warnings only, all commit message lines are under 80 columns).
- Mandatory change reviews for the follow-up:
  - Reviewer `019ef8a3-2c91-7f93-9cd8-f6ca178b1750` found one important
    subject-normalization gap for no-vars sends and one advisory enum coercion
    issue in the first follow-up commit; both were fixed before amend.
  - Final reviewer `019ef8ac-2db4-7240-ae1c-aa00420d9070` reviewed
    `5d3583b96d9e7a56b4510d1e9a3be45d87fb1368..3f6e57cfc65a78922560866a7225b337419f8bfd`
    and reported no blocking, important, or advisory findings.
  - Residual noted test gaps: no fresh browser integration or long alert/service
    integration run after the amended follow-up; the new admin delivery-method
    form has no browser-level regression coverage.
- Pushed final head `3f6e57cfc65a78922560866a7225b337419f8bfd`.
- GitHub Actions status after push:
  - RuboCop run `28084907268` passed;
  - API Specs (topic parallel) run `28084907200` passed;
  - obsolete aggregate CI run `28083574984` for the superseded WebUI-only head
    was cancelled;
  - aggregate CI run `28084907225` for final head
    `3f6e57cfc65a78922560866a7225b337419f8bfd` is still queued as of this
    note.

## 2026-06-24 WebUI delivery method hint cleanup

- Updated `webui/pages/page_adminm.php` to remove repeated per-method helper
  text from event delivery method checkboxes.
- Added one form-level sentence explaining that enabled methods allow the user
  to configure receivers and receive event notifications.
- Quick verification:
  - `php -l webui/pages/page_adminm.php` passed;
  - `rg` confirmed the old repeated helper sentence is gone and the new
    form-level sentence is present;
  - `git diff --check -- webui/pages/page_adminm.php` passed;
  - `nix develop -c overcommit --run pre-commit` passed.
- First ambient `git commit -F` attempt failed because the installed
  Overcommit hook could not find the `overcommit` gem outside the Nix shell.
  Retried inside `nix develop`; hooks ran and passed.
- Implemented commit `7d611cbd46180a5e6b4b5249e3cf79bb42e1f5d0`
  (`webui: deduplicate delivery method hint`).
  Commit-msg `TextWidth` reported 72-column warnings only; all message lines
  are under the workspace 80-column rule.
- Mandatory change review:
  - Standalone reviewer `019ef932-4f2e-7202-8b7c-8d1763dd0fe4` reviewed
    `3f6e57cfc65a78922560866a7225b337419f8bfd..7d611cbd46180a5e6b4b5249e3cf79bb42e1f5d0`.
  - Result: no blocking, important, or advisory findings.
  - Residual noted risk: no browser/Playwright render check; only PHP/table
    structure was reviewed, which is acceptable for this text-only cleanup.
- First ambient `git push` failed because the pre-push Overcommit hook could
  not find the `overcommit` gem outside the Nix shell. Retried with
  `nix develop -c git push origin 2026-06-15-vpsadmin-events`; push succeeded.
- GitHub Actions after push:
  - Webui PHPUnit run `28092583142` passed;
  - aggregate CI run `28092583135` for
    `7d611cbd46180a5e6b4b5249e3cf79bb42e1f5d0` is queued as of this note.

## 2026-06-24 WebUI delivery method description colspan

- Corrected the delivery method form-level description row so it spans all
  three table columns directly, instead of using a blank first cell plus a
  two-column span.
- Amended the previous WebUI hint cleanup commit to keep branch history clean:
  new head `58c744d56c6db871539b3f4d178d4ef568e9e4d7`
  (`webui: deduplicate delivery method hint`).
- Quick verification:
  - `php -l webui/pages/page_adminm.php` passed;
  - `rg` confirmed the old per-method sentence is absent, the form-level
    sentence is present, and the spacer cell was removed from the helper;
  - `git diff --check -- webui/pages/page_adminm.php` passed;
  - `nix develop -c overcommit --run pre-commit` passed;
  - amend commit hooks passed (`Nixfmt`, `PhpCsFixer`, commit-msg hooks);
    `TextWidth` reported 72-column warnings only, with all lines under the
    workspace 80-column rule.
- Mandatory change review:
  - Standalone reviewer `019ef95f-d744-7181-9a5a-933d5517e510` reviewed
    `3f6e57cfc65a78922560866a7225b337419f8bfd..58c744d56c6db871539b3f4d178d4ef568e9e4d7`.
  - Result: no blocking, important, or advisory findings.
  - Residual noted risk: no browser rendering tests; the review checked syntax,
    hooks, whitespace, text-level regression, and helper colspan behavior.
- Force-pushed amended head with an explicit lease from the previously pushed
  `7d611cbd46180a5e6b4b5249e3cf79bb42e1f5d0` to
  `58c744d56c6db871539b3f4d178d4ef568e9e4d7`.
- Cancelled obsolete aggregate CI run `28092583135` for the replaced head.
- GitHub Actions after amended push:
  - Webui PHPUnit run `28095166676` passed;
  - aggregate CI run `28095166698` for
    `58c744d56c6db871539b3f4d178d4ef568e9e4d7` is in progress as of this
    note.

## 2026-06-24 Event-backed notification wording

- Updated WebUI text that described event-backed deliveries as e-mail:
  - payment reminder link/form/success title now talks about notifications;
  - user profile time-zone and new-login descriptions now talk about
    notifications;
  - the profile event delivery section is titled `Notifications`;
  - snapshot download, VPS network toggle, VPS admin-modification, migration,
    outage, and security-advisory prompts use notification wording.
- Updated API metadata for event-backed fields while preserving compatibility
  names such as `send_mail`:
  - VPS, dataset, node evacuation, migration plan, snapshot download, outage,
    security advisory, dataset expansion, user language, and VPS change-reason
    labels/descriptions now say notification where appropriate;
  - e-mail-specific resources such as e-mail addresses, e-mail receiver
    actions, e-mail template recipients, and mail logs were intentionally left
    unchanged.
- Quick verification before commit:
  - `php -l` passed for all touched WebUI PHP files;
  - `ruby -c` passed for all touched Ruby resource/spec files;
  - stale-string `rg` checks confirmed the targeted e-mail/mail wording was
    removed from event-backed UI/API metadata;
  - broad `rg` showed only intentional e-mail-specific areas plus changelog
    history;
  - `git diff --check` passed;
  - `nix develop -c bash -lc 'cd api && bundle exec rspec
    spec/api/resources/security_advisory_spec.rb'` passed with 20 examples;
  - `nix develop -c overcommit --run pre-commit` passed.
- First commit attempt failed because files were not staged; hooks still ran
  and passed. Retried after explicit `git add`.
- Commit hooks passed in `nix develop`. `PhpCsFixer` then expanded several
  one-line callbacks in `webui/forms/outage.forms.php`; that hook output was
  syntax checked and amended into the same commit so the worktree stayed clean.
- Implemented commit `9ee15ed7e` (`notifications: update event wording`).
  Commit-msg `TextWidth` reported 72-column warnings only; all message lines
  are under the workspace 80-column rule.
- Mandatory change review:
  - Standalone reviewer `019ef9e2-b45f-78c0-91b0-816e9c4c593a` reviewed
    `58c744d56c6db871539b3f4d178d4ef568e9e4d7..9ee15ed7e`.
  - Blocking finding: event-type metadata still had stale mail wording for
    outage events and daily/payment report language parameters.
  - Important finding: human-facing transaction-chain labels still described
    migration-plan and security-advisory event routing as mail.
  - Advisory: the PhpCsFixer expansion in `webui/forms/outage.forms.php` is
    mechanical and acceptable in this commit.
- Follow-up fixes before amend:
  - updated event-type metadata to use notification wording;
  - renamed human-facing transaction-chain labels for migration,
    security-advisory, and payments overview notification chains;
  - updated stale notification comments/internal helper naming in outage and
    VPS migration chains while preserving compatibility names such as
    `send_mail`.
- Follow-up verification:
  - exact stale-string `rg` check for the review findings now only finds
    `Event e-mail delivery`, which is intentionally e-mail-action-specific;
  - `ruby -c` passed for all follow-up touched Ruby files;
  - `git diff --check` passed;
  - `nix develop -c bash -lc 'cd api && bundle exec rspec
    spec/api/resources/security_advisory_spec.rb
    spec/api/resources/event_routing_spec.rb
    spec/models/transaction_chains/plugins/outage_reports/update_spec.rb
    spec/models/transaction_chains/plugins/payments/mail_overview_spec.rb
    spec/models/transaction_chains/mail/daily_report_spec.rb
    spec/models/transaction_chains/migration_plan/mail_spec.rb'` passed with
    66 examples, 0 failures, 1 expected pending core-only plugin-mode case;
  - `nix develop -c overcommit --run pre-commit` passed.

## 2026-06-25 Telegram receiver creation and filters

- Improved Telegram receiver-action creation in the WebUI:
  - pending Telegram actions now show `Automatic pairing` with the `t.me` link
    first, noting that the link includes the start command;
  - manual fallback instructions are separate and show the `/start <token>`
    command for users who cannot open the link;
  - saved unverified actions keep the pairing command visible, verified
    actions still show the paired chat, and unsaved new actions explain that
    automatic pairing is available after saving.
- Removed the unused blank action column from the notification receivers table
  and adjusted the empty-table colspan.
- Removed right alignment from hand-written select boxes in notification
  filtering forms for deliveries and events.
- Regression coverage added in
  `webui/tests/Regression/NotificationDeliveryHtmlDetailsTest.php` for:
  - automatic/manual Telegram pairing separation;
  - absence of the unused receiver-table action column;
  - left-aligned notification filter selects.
- Quick verification:
  - first `nix develop .#webui -c ... webui/...` attempts failed because that
    development shell changes directory to `webui/`; reran commands with paths
    relative to `webui/`;
  - `nix develop .#webui -c php -l forms/notifications.forms.php` passed;
  - `nix develop .#webui -c composer test -- --filter
    NotificationDeliveryHtmlDetailsTest` passed with 12 tests and
    79 assertions;
  - `git diff --check` passed.
- Hooks and commit:
  - installed repository Overcommit hooks in the worktree with
    `nix develop -c overcommit --install`;
  - `nix develop -c overcommit --run` passed;
  - the hook run temporarily reformatted unrelated PHP files, which were
    reverted before committing;
  - first ambient `git commit -F` failed because the `overcommit` gem was not
    available outside the Nix shell; retrying through `nix develop` passed all
    commit hooks;
  - implemented commit `f2bafa0de6fb01eb94928cfe500d054fc65d6b58`
    (`webui: polish notification receiver setup`).
- Mandatory change review:
  - standalone reviewer `019efee3-d88b-7280-a84a-ac2a9dcf1677` reviewed
    `d84bf1c671aa9cfd1140463a681b3dbe4b869e04..f2bafa0de6fb01eb94928cfe500d054fc65d6b58`;
  - result: no blocking, important, or advisory findings;
  - reviewer reran the WebUI PHP lint, the targeted PHPUnit regression test,
    and `git diff --check`;
  - residual noted risk: no browser/Playwright render check for the table and
    form layout.
- Deployed to the running dev cluster:
  - cluster `2026-06-15-vpsadmin-events` was running on bridge networking and
    ready before deployment;
  - `dev-clusters/vpsadmin/bin/devcluster update
    2026-06-15-vpsadmin-events services` completed successfully;
  - the deployment built the local vpsadmin worktree input and switched the
    services VM to
    `/nix/store/zb6kfcwiz62bzyn8s0zdz5gn0y9zgriq-nixos-system-vpsadmin-services-26.05pre-git`.
- Post-deploy smoke verification:
  - `devcluster status 2026-06-15-vpsadmin-events` reports running, bridge
    networking, and ready;
  - `systemctl --failed --no-pager` on the services VM reported
    `0 loaded units listed`;
  - `curl -k -I https://webui.aitherdev.int.vpsfree.cz/` returned HTTP 200;
  - `curl -k -I https://api.aitherdev.int.vpsfree.cz/` returned HTTP 200;
  - `vpsadmin-api`, email/webhook/telegram notification dispatchers, and
    `vpsadmin-telegram-receiver` are active;
  - `vpsadmin-devcluster-seed.service` completed with `Result=success`;
  - deployed WebUI source in the services VM's Nix store contains the new
    `Automatic pairing` and `Manual pairing` text. Two quoted grep attempts
    tripped over the devcluster SSH wrapper quoting, then single-word probes
    confirmed the deployed source.
- Pushed the feature branch with
  `nix develop -c git push origin 2026-06-15-vpsadmin-events`; the remote
  advanced from `d84bf1c671aa9cfd1140463a681b3dbe4b869e04` to
  `f2bafa0de6fb01eb94928cfe500d054fc65d6b58`.
- GitHub Actions after push:
  - Webui PHPUnit run `28173312357` passed in 1m1s;
  - aggregate CI run `28173312336` was still in progress after roughly eight
    minutes, in the `Run tests` step of job `83442929155`;
  - stopped only the local `gh run watch` process after recording the status;
    the GitHub workflow itself remains running at
    https://github.com/vpsfreecz/vpsadmin/actions/runs/28173312336.

## 2026-06-25 Reusable notification targets

- User feedback after the Telegram pairing UI slice:
  - manual Telegram instructions must include the bot name, and the API should
    expose that bot name rather than hard-coding it in the WebUI;
  - receiver actions were too tightly coupled to destinations, because several
    receivers/routes may need to reuse the same Telegram chat, SMS number,
    webhook, or e-mail target;
  - development migrations and dev-cluster state may be reset, so existing
    event-delivery migrations can be rewritten for a cleaner model.
- Implemented design in `vpsadmin`:
  - added user-owned `notification_targets` for reusable destinations and
    verification state;
  - replaced the action table with `notification_receiver_targets` links while
    keeping `NotificationReceiverAction` as a Ruby compatibility alias for
    existing internal call sites/tests during this development branch;
  - moved Telegram pairing tokens, Telegram bot name/link helpers, SMS
    verification state, webhook secrets, target labels, and identity keys onto
    `NotificationTarget`;
  - added top-level HaveAPI `notification_target` resources for create/update,
    pairing token creation, SMS send/confirm, and delete;
  - changed nested `notification_receiver.action` APIs to
    `notification_receiver.target` link management APIs;
  - event deliveries now snapshot both the reusable target and the receiver
    target link so dispatch can cancel receiver-backed deliveries when the
    receiver or link is later disabled/deleted;
  - Telegram pairing now resolves pairing tokens against `NotificationTarget`
    and merges duplicate chat targets by relinking receiver-target rows;
  - Webhook payloads now identify `notification_target` and `receiver_target`
    instead of the old receiver action object.
- WebUI changes:
  - added a `Targets` tab to Notifications;
  - receiver edit pages link existing targets or create a target and link it;
  - target edit pages own Telegram pairing and SMS verification controls;
  - Telegram manual pairing instructions use `telegram_bot_name` from the API;
  - receiver lists and summaries now show linked targets;
  - event/delivery filters and detail links use notification target and
    receiver target IDs.
- Migration/schema changes:
  - rewrote `20260615110000_add_events.rb` to create
    `notification_targets` and `notification_receiver_targets`;
  - updated later event-delivery migrations and `api/db/schema.rb` for the
    new tables/foreign keys;
  - default e-mail receivers/routes and advanced-mail backfills now create or
    reuse targets and then link receivers to them.
- Compatibility decisions:
  - branch is still pre-merge development, so old migrations were rewritten
    instead of adding transitional ALTER migrations;
  - `NotificationReceiverAction` compatibility remains for internal code while
    API/WebUI surfaces move to targets;
  - reusable target identity is unique per user/action/destination, with link
    uniqueness per receiver/target.
- Verification:
  - `php -l webui/forms/notifications.forms.php` passed;
  - `php -l webui/pages/page_notifications.php` passed;
  - Ruby syntax checks passed for touched models/resources/event delivery and
    notification dispatch files;
  - `webui/vendor/bin/phpunit
    webui/tests/Regression/NotificationDeliveryHtmlDetailsTest.php` passed
    with 12 tests and 79 assertions;
  - `nix develop .#api -c bundle exec rspec
    spec/models/notification_receiver_action_spec.rb` passed with 21 examples;
  - `nix develop .#api -c bundle exec rspec
    spec/models/event_route_spec.rb` passed with 25 examples;
  - `nix develop .#api -c bundle exec rspec
    spec/models/tasks/telegram_spec.rb
    spec/models/tasks/event_delivery_spec.rb
    spec/models/notification_events_spec.rb
    spec/models/event_route_spec.rb` passed with 111 examples;
  - `nix develop .#api -c bundle exec rspec
    spec/api/resources/event_routing_spec.rb
    spec/api/endpoint_coverage_spec.rb` passed with 33 examples and one
    expected pending core-only plugin-mode case;
  - `git diff --check` passed;
  - `nix develop . -c bundle exec overcommit --diff HEAD` passed with
    Nixfmt, RuboCop, and PhpCsFixer.
- Hook note:
  - `nix develop . -c bundle exec overcommit --run` checks all tracked files
    and temporarily reformatted unrelated PHP files; those formatter-only
    changes were reverted and the diff-scoped hook run was used for this
    change.
- Commit and hooks:
  - committed `vpsadmin` change
    `5658ea8c3b6e8b590b4439bb9d9715897e4cf7cf`
    (`notifications: add reusable delivery targets`);
  - first commit attempt caught RuboCop indentation in the new
    `NotificationTarget#pair_telegram_chat!` query; fixed and retried;
  - final commit hooks passed with Nixfmt, RuboCop, and PhpCsFixer;
  - commit-msg TextWidth emitted a 72-column warning on a body line, but all
    message lines are under the workspace 80-column rule;
  - amended the commit after review follow-up; amend hooks passed with Nixfmt,
    PhpCsFixer, RuboCop, and the same commit-msg TextWidth warning;
  - amended the commit again after GitHub API specs exposed one stale test
    writing `target_value` directly on `NotificationReceiverAction`; the spec
    now mutates the underlying `NotificationTarget`, and amend hooks passed
    with Nixfmt, RuboCop, PhpCsFixer, and the same commit-msg TextWidth
    warning.
- Mandatory change review:
  - standalone reviewer `019eff4a-aa46-7b81-9386-6987ec0415e0` reviewed
    `f2bafa0de6fb01eb94928cfe500d054fc65d6b58..8f08d48911b460995c58306a715b82737a7d5596`;
  - result: no blocking findings;
  - important findings:
    - webhook deliveries to the same URL with different reusable target
      secrets were deduplicated too aggressively;
    - Telegram pairing into an already-existing duplicate chat target could
      relink receivers to an unverified target;
  - advisory findings:
    - target creation and receiver linking in the WebUI are not atomic;
    - the API exposed the internal reusable target `identity_key`.
- Review follow-up:
  - delivery deduplication now keys receiver-backed deliveries by reusable
    target ID, while direct value-backed deliveries still key by target value;
  - Telegram duplicate-target pairing now marks the existing target verified,
    clears its token/error state, and then relinks receiver-target rows;
  - removed `identity_key` from the public `notification_target` resource
    output;
  - added regression coverage for webhook targets with the same URL and
    different secrets, and for Telegram pairing into an existing duplicate
    chat target.
- Follow-up verification:
  - Ruby syntax checks passed for the changed model, event router, API
    resource, and specs;
  - `nix develop .#api -c bundle exec rspec
    spec/models/event_route_spec.rb spec/models/tasks/telegram_spec.rb
    --format progress` passed with 39 examples;
  - `nix develop .#api -c bundle exec rspec
    spec/api/resources/event_routing_spec.rb
    spec/api/endpoint_coverage_spec.rb --format progress` passed with
    33 examples and one expected pending core-only plugin-mode case;
  - `git diff --check` passed.
- Final mandatory change review:
  - standalone reviewer `019eff5e-7d1c-7430-9102-89c4d8554100` reviewed
    `f2bafa0de6fb01eb94928cfe500d054fc65d6b58..84f6dc0acb8093c21689fc64c135a249f7299874`;
  - result: no blocking, important, or advisory findings;
  - reviewer confirmed the webhook dedupe, Telegram duplicate pairing, hidden
    `identity_key`, Telegram pairing UI, receiver table, and select alignment
    fixes in the amended commit;
  - residual production decision: webhook deliveries snapshot URL/body but
    still sign retries with the current target secret, matching previous
    behavior; accept for this development deployment and revisit before
    production if queued delivery signatures should be immutable.
- GitHub Actions/API spec follow-up:
  - pushed `84f6dc0acb8093c21689fc64c135a249f7299874`; RuboCop, WebUI
    PHPUnit, and libnodectld Specs passed;
  - API Specs run `28181269705` failed for two reasons:
    - real branch issue: `API specs (full) - engine` failed in
      `spec/models/transaction_chains/vps/oom_prevention_spec.rb` because the
      stale-target test still called `update_columns(target_value: ...)` on the
      receiver-target link;
    - unrelated runner/environment issue: `API specs (core) - platform`
      failed during `apt-get update` with HTTP 403 from Microsoft package
      repositories;
  - fixed the real test issue and verified:
    - `nix develop .#api -c bundle exec rspec
      spec/models/transaction_chains/vps/oom_prevention_spec.rb:53
      --format progress` passed with 1 example;
    - `nix develop .#api -c bundle exec rspec
      spec/models/transaction_chains/vps/oom_prevention_spec.rb
      --format progress` passed with 5 examples;
    - `ruby -c
      api/spec/models/transaction_chains/vps/oom_prevention_spec.rb` passed;
    - `git diff --check` passed;
    - `nix develop . -c bundle exec overcommit --diff HEAD` passed.
- Final push/workflow cleanup:
  - force-pushed `5658ea8c3b6e8b590b4439bb9d9715897e4cf7cf` to
    `origin/2026-06-15-vpsadmin-events`;
  - updated the top-level `AGENTS.md` workflow guidance: after force-pushes or
    follow-up fix pushes, cancel superseded queued or in-progress GitHub
    Actions runs for the same branch only when their `headSha` no longer
    matches the current branch head;
  - applied that rule to the current branch by canceling superseded CI run
    `28181269780` from old head
    `84f6dc0acb8093c21689fc64c135a249f7299874`;
  - current-head GitHub Actions observed after the push:
    - RuboCop `28182444723` passed;
    - WebUI PHPUnit `28182445311` passed;
    - libnodectld Specs `28182444728` passed;
    - API Specs `28182445194` later passed on the final head;
    - CI `28182445014` remained in progress on the final head as of
      2026-06-25T16:21:07Z, still in the `Run tests` step for selected
      ci-tagged tests; GitHub did not expose live logs while the run was
      in progress.
- Dev cluster deployment:
  - reset and started dev cluster `2026-06-15-vpsadmin-events` on the bridge
    network after rewriting development migrations;
  - initial start hit the known node-preparation race connecting to
    `/run/osctl/osctld.sock`, but services were running and
    `devcluster refresh 2026-06-15-vpsadmin-events` completed successfully;
  - after the final spec-only amend, refreshed services with
    `devcluster update 2026-06-15-vpsadmin-events services`, which switched
    the services machine to the final worktree commit and started the new
    `vpsadmin-notification-dispatcher-telegram.service` and
    `vpsadmin-telegram-receiver.service`;
  - smoke checks after the final service update:
    - `devcluster status` reports running, bridge topology, ready;
    - `systemctl --failed --no-pager` on the services machine reports
      0 failed units;
    - `systemctl is-active` reports active for `vpsadmin-api`,
      e-mail/webhook/SMS/Telegram notification dispatchers,
      `vpsadmin-telegram-receiver`, `container@webui`, `rabbitmq`,
      `redis-vpsadmin`, `mysql`, `nginx`, and `haproxy`;
    - `vpsadmin-devcluster-seed.service` is inactive after successful
      completion with exit status 0;
    - WebUI and API both return HTTP 200:
      `https://webui.aitherdev.int.vpsfree.cz/` and
      `https://api.aitherdev.int.vpsfree.cz/`.

## 2026-06-25 receiver target link cleanup

- User feedback after dev-cluster testing:
  - receiver-target links had a separate `enabled` flag exposed as "Enable
    receiver link" / "Link enabled", which was not useful now that targets are
    reusable and links can be recreated;
  - receiver target rows showed "delivery method disabled" even when links and
    targets were enabled;
  - editing a target from receiver details offered "Back to targets" instead
    of returning to the receiver;
  - sidebar ordering should show Targets below Receivers;
  - notification tables should put edit/delete actions in separate cells.
- Implemented in `vpsadmin`:
  - rewrote the still-unmerged event migrations and schema to remove
    `notification_receiver_targets.enabled` completely;
  - removed the link-enabled API input/output and WebUI controls;
  - receiver-target deliverability now depends on the reusable target and the
    user's delivery-method setting, not on a separate link flag;
  - API output now exposes explicit target and delivery-method booleans for
    receiver target rows;
  - event routing no longer filters receiver targets by link enablement and
    reports empty receivers as having no linked targets;
  - target edit/pairing/SMS verification URLs preserve a receiver context when
    entered from receiver details, and the edit sidebar returns to that
    receiver;
  - the Notifications sidebar order is Routes, Receivers, Targets, Event
    types, Test event;
  - Targets, Receivers, and receiver detail target tables now use separate
    action cells for edit and delete/unlink links.
- Compatibility:
  - this is still pre-merge development, and the user explicitly allowed
    rewriting migrations and resetting the dev cluster state;
  - removing `notification_receiver_targets.enabled` is intentionally
    incompatible with the previous development database shape and requires a
    reset or fresh migration state on the dev cluster.
- Verification before commit:
  - `php -l webui/forms/notifications.forms.php` passed;
  - `php -l webui/pages/page_notifications.php` passed;
  - Ruby syntax checks passed for touched models, API resources, migrations,
    and specs;
  - `webui/vendor/bin/phpunit
    webui/tests/Regression/NotificationDeliveryHtmlDetailsTest.php` passed
    with 15 tests and 101 assertions;
  - `nix develop .#api -c bundle exec rspec
    spec/models/tasks/event_delivery_spec.rb:1087 --format progress` passed
    with 1 example;
  - `nix develop .#api -c bundle exec rspec
    spec/api/resources/event_routing_spec.rb:284
    spec/api/resources/event_routing_spec.rb:316 --format progress` passed
    with 2 examples;
  - `nix develop .#api -c bundle exec rspec
    spec/models/notification_receiver_action_spec.rb
    spec/models/event_route_spec.rb
    spec/models/tasks/event_delivery_spec.rb --format progress` passed with
    117 examples;
  - `nix develop .#api -c bundle exec rspec
    spec/api/resources/event_routing_spec.rb
    spec/api/endpoint_coverage_spec.rb --format progress` passed with
    33 examples and one expected pending core-only plugin-mode case;
  - `git diff --check` passed;
  - `nix develop . -c bundle exec overcommit --diff HEAD` passed with
    Nixfmt, PhpCsFixer, and RuboCop.
- Commit and hooks:
  - amended the existing reusable-target commit to include this cleanup,
    initially producing:
    `5c2f79e7bbef6d088cd3206837e9acc608fb50fb`
    (`notifications: add reusable delivery targets`);
  - the first plain-shell amend attempt did not run because the hook wrapper
    could not find the Overcommit gem; the commit was rerun through
    `nix develop . -c git commit --amend -F <tmpfile>`;
  - final commit hooks passed with Nixfmt, PhpCsFixer, RuboCop, and
    commit-msg TextWidth warnings for lines over 72 columns; all commit
    message lines remain under the workspace 80-column rule.
- Mandatory change review:
  - standalone reviewer `019effc4-e5b5-79d0-af2c-d01c0c3bdff6` reviewed
    `f2bafa0de6fb01eb94928cfe500d054fc65d6b58..5c2f79e7bbef6d088cd3206837e9acc608fb50fb`;
  - result: no blocking findings;
  - important finding: `NotificationTarget.identity_key_for` stored raw
    custom e-mail targets and raw webhook URLs in a 255-character
    `identity_key`, which could reject long but valid target values;
  - advisory finding: WebUI create-and-link target remains non-atomic if
    target creation succeeds but receiver linking fails. This is accepted for
    this development slice because the target is reusable and can be linked or
    deleted afterwards.
- Review follow-up:
  - `NotificationTarget.identity_key_for` now stores custom e-mail and webhook
    target identities as stable SHA-256 digests while keeping full values in
    `target_value`;
  - the advanced-mail migration helper uses the same custom e-mail digest
    identity;
  - regression coverage creates long custom e-mail targets and long webhook
    URLs with distinct secrets, asserting compact identities and target reuse
    or separation as appropriate;
  - amended final local `vpsadmin` head:
    `872c1bfb91877ad94e3c4b87bbf8b6c656eaadaa`.
- Follow-up verification:
  - Ruby syntax checks passed for `api/models/notification_target.rb`,
    `api/db/migrate/20260615110000_add_events.rb`, and
    `api/spec/models/notification_receiver_action_spec.rb`;
  - `nix develop .#api -c bundle exec rspec
    spec/models/notification_receiver_action_spec.rb --format progress`
    passed with 23 examples;
  - `php -l webui/forms/notifications.forms.php` passed;
  - `php -l webui/pages/page_notifications.php` passed;
  - `webui/vendor/bin/phpunit
    webui/tests/Regression/NotificationDeliveryHtmlDetailsTest.php` passed
    with 15 tests and 101 assertions;
  - `nix develop .#api -c bundle exec rspec
    spec/models/event_route_spec.rb spec/models/tasks/event_delivery_spec.rb
    --format progress` passed with 96 examples;
  - `nix develop .#api -c bundle exec rspec
    spec/api/resources/event_routing_spec.rb
    spec/api/endpoint_coverage_spec.rb --format progress` passed with
    33 examples and one expected pending core-only plugin-mode case;
  - `git diff --check` passed;
  - `nix develop . -c bundle exec overcommit --diff HEAD` passed with
    Nixfmt and RuboCop before the final amend; final amend hooks passed with
    Nixfmt, PhpCsFixer, RuboCop, and commit-msg TextWidth warnings for lines
    over 72 columns, with all lines under the workspace 80-column rule.
- Final mandatory change review:
  - standalone reviewer `019effd4-fa1b-75b2-80e1-43784e331976` reviewed
    `f2bafa0de6fb01eb94928cfe500d054fc65d6b58..872c1bfb91877ad94e3c4b87bbf8b6c656eaadaa`;
  - result: no blocking, important, or advisory findings;
  - residual accepted risks:
    - WebUI create-and-link target is still non-atomic if the target is
      created but receiver linking fails;
    - the new WebUI flows have PHP/HTML regression coverage, not live browser
      coverage;
    - the migration shape is development-only and requires a dev-cluster
      reset;
    - webhook retries still sign with the current reusable target secret
      rather than an immutable delivery-time secret snapshot.
- Push/workflow cleanup:
  - force-pushed `872c1bfb91877ad94e3c4b87bbf8b6c656eaadaa` to
    `origin/2026-06-15-vpsadmin-events`;
  - after the force-push, new-head GitHub Actions were created for
    `872c1bfb`:
    - API Specs `28188952530`;
    - WebUI PHPUnit `28188952538`;
    - RuboCop `28188952534`;
    - CI `28188952523`;
  - canceled superseded in-progress old-head CI run `28182445014` from
    `5658ea8c3b6e8b590b4439bb9d9715897e4cf7cf`, following the workspace rule
    to cancel only queued/in-progress workflows for the same branch whose
    `headSha` no longer matches the current branch head.

## 2026-06-25 final CI/deploy follow-up

- GitHub Actions API Specs failure on pushed head
  `872c1bfb91877ad94e3c4b87bbf8b6c656eaadaa` was investigated before
  accepting CI:
  - failed jobs were `API specs (full) - supervisor` and
    `API specs (core) - supervisor` in run `28188952530`;
  - both failed in
    `spec/supervisor/node/oom_reports_spec.rb:155` with
    `ActiveModel::UnknownAttributeError: unknown attribute 'enabled' for
    NotificationReceiverTarget`;
  - root cause was a stale spec fixture still disabling the removed
    receiver-target link-level `enabled` attribute;
  - fixed by creating the receiver target normally and disabling the reusable
    `NotificationTarget` instead.
- Local verification for the CI follow-up:
  - `ruby -c api/spec/supervisor/node/oom_reports_spec.rb` passed;
  - `nix develop .#api -c bundle exec rspec
    spec/supervisor/node/oom_reports_spec.rb:155 --format progress` passed
    with 1 example;
  - `nix develop .#api -c bundle exec rspec
    spec/supervisor/node/oom_reports_spec.rb --format progress` passed with
    14 examples;
  - `git diff --check` passed;
  - `nix develop . -c bundle exec overcommit --diff HEAD` passed with Nixfmt
    and RuboCop.
- Amended `notifications: add reusable delivery targets` through
  `nix develop . -c git commit --amend -F <tmpfile>` so hooks were available:
  - final local and remote `vpsadmin` head is
    `ef6ea585fd8bf5ef71182ff84b9d1722a9fa7aaf`;
  - commit hooks passed with Nixfmt, PhpCsFixer, RuboCop, and commit-msg
    TextWidth warnings for existing lines over 72 columns; all lines remain
    under the workspace 80-column rule;
  - no extra mandatory-change-review was run for this amend because the
    post-review delta was a spec-only update to a stale fixture after the
    runtime/API/schema/UI changes had already received a clean standalone
    review.
- Push/workflow cleanup after the amend:
  - ambient `git push` failed because the push hook could not find the
    Overcommit gem;
  - reran the force push through `nix develop . -c git push
    --force-with-lease origin 2026-06-15-vpsadmin-events`, which passed the
    hook environment and updated the remote from `872c1bfb` to `ef6ea585`;
  - canceled superseded same-branch in-progress run `28188952523` from old
    head `872c1bfb91877ad94e3c4b87bbf8b6c656eaadaa`;
  - current-head GitHub Actions for `ef6ea585`:
    - RuboCop `28190724233`: success;
    - Webui PHPUnit `28190724211`: success;
    - libnodectld Specs `28190724206`: success;
    - API Specs (topic parallel) `28190724230`: success;
    - CI `28190724236`: still in progress on job
      `Run selected ci-tagged tests` as of the last poll; GitHub did not
      expose logs for the running job via either `gh run view --job --log` or
      the lower-level job logs API.
- Dev cluster deployment refreshed after the amend:
  - ran `dev-clusters/vpsadmin/bin/devcluster update
    2026-06-15-vpsadmin-events services`;
  - update completed and picked up the amended vpsadmin worktree source hash;
  - `devcluster status` reports the cluster running on bridge networking and
    `ready: yes`;
  - `systemctl --failed --no-pager` on `services` reports 0 failed units;
  - `systemctl is-active` passed for `vpsadmin-api`,
    `vpsadmin-notification-dispatcher-email`,
    `vpsadmin-notification-dispatcher-webhook`,
    `vpsadmin-notification-dispatcher-sms`,
    `vpsadmin-notification-dispatcher-telegram`,
    `vpsadmin-telegram-receiver`, `container@webui`, `rabbitmq`,
    `redis-vpsadmin`, `mysql`, `nginx`, and `haproxy`;
  - HTTP smoke checks returned `webui 200` and `api 200`;
  - Telegram receiver and dispatcher journals show clean stop/start during the
    deploy and both units started successfully afterwards.

## 2026-06-25 target verification/UI follow-up

- Implemented the follow-up notification target changes in `vpsadmin` worktree
  `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-06-15-vpsadmin-events/vpsadmin`
  on branch `2026-06-15-vpsadmin-events`.
- API/model changes:
  - custom e-mail targets now require hidden-token verification before
    delivery;
  - SMS and custom e-mail targets saved by admins are marked verified;
  - custom e-mail target values are limited to one address;
  - e-mail verification links are sent by a new
    `notification_target#send_email_verification` action and confirmed by
    `notification_target#confirm_email_verification`;
  - unverified custom e-mail actions are skipped with
    `e-mail target is not verified`;
  - migrated advanced custom e-mail targets are marked verified in the
    development migration to preserve previous delivery behavior.
- WebUI changes:
  - target list status now uses target-level enabled/delivery-method fields,
    fixing the false `target disabled` display;
  - removed remaining right-aligned notification form content;
  - SMS phone input width now matches the label field;
  - custom e-mail target detail shows verification status and send controls;
  - custom e-mail target create/update redirects to target detail so the
    verification controls are visible.
- Local verification:
  - focused API endpoint run passed:
    `nix develop .#api -c bundle exec rspec
    spec/api/resources/event_routing_spec.rb` with 34 examples, 0 failures,
    one expected pending core-only plugin-mode case;
  - broader focused API run passed:
    `nix develop .#api -c bundle exec rspec
    spec/models/notification_receiver_action_spec.rb
    spec/models/event_route_spec.rb
    spec/api/resources/event_routing_spec.rb
    spec/models/tasks/event_delivery_spec.rb` with 157 examples, 0 failures,
    one expected pending core-only plugin-mode case;
  - WebUI regression run passed:
    `webui/vendor/bin/phpunit --configuration webui/phpunit.xml.dist
    webui/tests/Regression/NotificationDeliveryHtmlDetailsTest.php` with
    18 tests and 129 assertions;
  - Ruby syntax checks passed for touched API files;
  - PHP syntax checks passed for touched WebUI files;
  - `git diff --check` passed;
  - focused API RuboCop initially found one correctable string-literal offense
    in `notification_receiver_action_spec.rb`; fixed and reran successfully
    with 9 files and no offenses;
  - `nix develop .#webui -c php-cs-fixer ...` failed because the WebUI-only
    shell does not expose `php-cs-fixer`;
  - `nix develop -c php-cs-fixer fix --dry-run --diff
    --config=.php-cs-fixer.dist.php ...` passed from the root shell.
- Hook status:
  - `.overcommit.yml` is present;
  - `git rev-parse --git-path hooks/pre-commit` points to an installed,
    executable Overcommit hook in the canonical bare repository hook path.
- Commit:
  - committed `vpsadmin` change as
    `1120b0cd487e0af46b869d7667a365f11911378a`
    (`notifications: verify reusable custom targets`);
  - commit was created through `nix develop -c git commit -F <tmpfile>`;
  - pre-commit hooks passed with Nixfmt, PhpCsFixer, and RuboCop;
  - commit-msg hooks passed with TextWidth warnings for lines over 72 columns;
    verified the longest commit-message line is 77 columns, under the
    workspace 80-column rule.
- Mandatory change review:
  - spawned standalone reviewer `019f005a-02c0-71c1-81ac-a443353bdf08`
    after commit and quick verification;
  - review found one blocking issue and two important/advisory points:
    - custom e-mail validation rejected comma-separated addresses but still
      allowed semicolon-separated multiple addresses through the mail parser;
    - e-mail verification sends lacked a resend cooldown;
    - verification URLs are stored in admin-readable `MailLog` bodies;
    - WebUI e-mail verification coverage remains PHP/source-level rather than
      a live browser/API round trip;
  - fixed the blocking/mailer-abuse findings:
    - custom e-mail targets now use `Mail::AddressList`, require exactly one
      parsed address, and store the parsed address;
    - `mail` is listed as an explicit API dependency in `api/Gemfile`;
    - e-mail verification sends now record `email_verification_sent_at` and
      are rejected inside a one-minute cooldown;
    - model/API specs cover semicolon-separated addresses and repeated
      verification sends;
  - accepted admin-readable `MailLog` token exposure for this branch because
    admins can already mark custom e-mail and SMS targets verified;
  - accepted WebUI source-level regression coverage for now; browser/API
    round-trip coverage remains a follow-up integration-test gap.
- Reviewer-fix verification:
  - `nix develop .#api -c bundle exec rspec
    spec/models/notification_receiver_action_spec.rb
    spec/api/resources/event_routing_spec.rb` passed with 60 examples,
    0 failures, and one expected pending core-only plugin-mode case;
  - focused RuboCop for changed Ruby files passed after one guard-clause
    cleanup;
  - WebUI regression run passed again with 18 tests and 129 assertions;
  - Ruby syntax checks passed for touched API files;
  - PHP syntax checks passed for touched WebUI files;
  - `git diff --check` passed;
  - `nix develop .#api -c bundle exec rspec
    spec/models/notification_receiver_action_spec.rb
    spec/models/event_route_spec.rb
    spec/api/resources/event_routing_spec.rb
    spec/models/tasks/event_delivery_spec.rb` passed with 157 examples,
    0 failures, and one expected pending core-only plugin-mode case;
  - `nix develop -c bundle exec overcommit --diff HEAD` passed with Nixfmt
    and RuboCop for the reviewer-fix diff.
- Amended commit:
  - amended the change into
    `748eaaea8aad4a47eca10f45ab23bf54d5186063`
    (`notifications: verify reusable custom targets`);
  - amend hooks passed with Nixfmt, PhpCsFixer, RuboCop, and the same
    commit-msg TextWidth warnings for lines over 72 columns; longest line
    remains 77 columns, under the workspace 80-column rule;
  - worktree is clean after the amend.
- Second mandatory change review:
  - standalone reviewer `019f006d-6bcf-7b33-aa9d-463c4dc30e7e` reviewed
    amended head `748eaaea8aad4a47eca10f45ab23bf54d5186063`;
  - review found:
    - blocking: `Mail::AddressList` accepted local-only addresses such as
      `bad` and `root` unless domain/local parts are checked explicitly;
    - important: direct `mail` dependency was not propagated to
      `packages/api/Gemfile` and package lock metadata;
    - advisory: e-mail resend cooldown is per saved target and can be reset
      by editing the target address, not a global per-recipient throttle;
  - fixed the blocking/important findings:
    - parsed e-mail addresses now require both local and domain parts;
    - model specs reject `bad` and `root`;
    - `packages/api/Gemfile` and `packages/api/Gemfile.lock` now list `mail`
      as a direct dependency;
    - `bundix -l` was rerun from `packages/api` with root Bundler
      environment variables cleared; it produced no `gemset.nix` diff because
      `mail` was already present transitively;
    - a temporary root `gemset.nix` produced during the failed package refresh
      attempt was removed;
  - accepted the cooldown scope as sufficient for this follow-up because it
    rate-limits repeated sends for the same pending target, matching the SMS
    resend model; broader per-recipient throttling remains a possible
    hardening follow-up.
- Second-review-fix verification:
  - `nix develop .#api -c bundle exec rspec
    spec/models/notification_receiver_action_spec.rb` passed with 27 examples
    and 0 failures;
  - Ruby syntax checks passed for `api/models/notification_target.rb` and
    `api/models/notification_receiver_action.rb`;
  - `git diff --check` passed;
  - focused RuboCop passed for `models/notification_target.rb` and
    `spec/models/notification_receiver_action_spec.rb`;
  - `nix develop -c bundle exec overcommit --diff HEAD` passed with Nixfmt
    and RuboCop before amending.
- Final amended commit:
  - amended the change into
    `88de1475fd000a7a36d470880b74e19b59a7fdc6`
    (`notifications: verify reusable custom targets`);
  - amend hooks passed with Nixfmt, PhpCsFixer, RuboCop, and the same
    commit-msg TextWidth warnings for lines over 72 columns; longest line
    remains 77 columns, under the workspace 80-column rule;
  - worktree is clean after the amend.
- Third mandatory change review:
  - standalone reviewer `019f007e-9756-7e61-bedc-4b697409b68c` reviewed
    `88de1475fd000a7a36d470880b74e19b59a7fdc6`;
  - review found one blocking validation edge:
    - mixed invalid/local-only plus valid address lists such as
      `root,audit@example.test` were collapsed during normalization because
      invalid parsed addresses were filtered out before counting;
  - review also noted advisory resend-cooldown concurrency limits and the
    accepted admin-readable mail-log verification URL risk.
- Third-review-fix verification:
  - parsing and validation were split: all parsed addresses are counted first,
    and only a single address with both local and domain parts is normalized;
  - model specs now cover mixed local-only plus valid addresses separated by
    commas or semicolons;
  - `nix develop .#api -c bundle exec rspec
    spec/models/notification_receiver_action_spec.rb` passed with 27 examples
    and 0 failures;
  - Ruby syntax checks passed for `api/models/notification_target.rb` and
    `api/models/notification_receiver_action.rb`;
  - `git diff --check` passed;
  - focused RuboCop passed for `models/notification_target.rb` and
    `spec/models/notification_receiver_action_spec.rb`;
  - `nix develop -c bundle exec overcommit --diff HEAD` passed with Nixfmt
    and RuboCop before amending.
- Final amended commit after third review:
  - amended the change into
    `7e05f10821e62f79f100e4df02a433c126964507`
    (`notifications: verify reusable custom targets`);
  - amend hooks passed with Nixfmt, PhpCsFixer, RuboCop, and the same
    commit-msg TextWidth warnings for lines over 72 columns; longest line
    remains 77 columns, under the workspace 80-column rule;
  - worktree is clean after the amend.
- Final mandatory change review:
  - standalone reviewer `019f0087-edc7-7001-a1b6-d6eda6f59582` reviewed
    `7e05f10821e62f79f100e4df02a433c126964507`;
  - result: no blocking, important, or advisory findings;
  - accepted residual risks/test gaps:
    - verification URL tokens are persisted in admin-readable `MailLog`
      bodies, accepted because admins can already mark custom e-mail and SMS
      targets verified;
    - e-mail resend cooldown is per saved target and not row-locked, matching
      the existing SMS cooldown shape;
    - WebUI coverage is PHP/source-level regression coverage, not a live
      browser/API round trip.

## 2026-06-26 - Devcluster e-mail verification follow-up

- Investigated user report from the dev cluster:
  - admin-created custom e-mail target stayed unverified;
  - clicking `Send verification email` in WebUI returned HTTP 500;
  - no verification e-mail arrived.
- Found the services VM was initially running a stale API closure that did not
  contain the committed e-mail verification/admin-skip code:
  - running API store lacked `send_email_verification`,
    `admin_verification_skippable`, and related symbols;
  - deployed current vpsadmin branch with
    `dev-clusters/vpsadmin/bin/devcluster update
    2026-06-15-vpsadmin-events services`;
  - after deployment, running API store contained the expected symbols.
- Verified admin custom e-mail target creation through the live API:
  - POST `/v7.0/notification_targets` as `test-admin` for user 1 created
    target `#6`;
  - response had `verified=true`, `verified_at` set, no exposed
    `verification_token`, and `delivery_method_enabled=true`.
- Verified regular user custom e-mail target send path before the SMTP fix:
  - POST as `test-user1` created target `#7` pending/unverified;
  - POST `/v7.0/notification_targets/7/send_email_verification` returned
    HTTP 200 and API JSON `status=true`;
  - Mailpit still had zero messages, revealing a second configuration bug.
- Root cause of the no-mail issue:
  - `send_email_verification!` delivers immediately from the API process via
    `Notifications::Config.load`;
  - the API module generated `notifications.yml` without SMTP settings, so the
    API fell back to localhost port 25 instead of the devcluster Mailpit SMTP
    capture port;
  - the async notification dispatcher already had Mailpit SMTP settings, but
    that did not affect API-side verification delivery.
- Implemented and committed fixes:
  - vpsadmin commit
    `0fc58bbbce9f5b31edd6e3e9e918b14a6ddf6d39`
    (`nixos: configure API notification SMTP`) adds optional
    `vpsadmin.api.notifications.smtp` settings and writes an SMTP block to the
    API notifications config when enabled;
  - workspace commit
    `a4078a132a14dd1ffa5a5eaa5cb451fe4958a479`
    (`devcluster: route API notification SMTP to Mailpit`) enables that API
    SMTP config for the dev cluster and points it at Mailpit.
- Verification after SMTP fix:
  - redeployed services with `devcluster update`;
  - generated API config included SMTP address `127.0.0.1` and Mailpit SMTP
    port `1025`;
  - cleared Mailpit through `DELETE /api/v1/messages`, HTTP 200;
  - created target `#8` as `test-user1`, pending/unverified and delivery
    method enabled;
  - POST `/v7.0/notification_targets/8/send_email_verification` returned
    HTTP 200, API JSON `status=true`, `last_error=null`, and a sent timestamp;
  - Mailpit reported one matching verification e-mail with subject
    `Verify your vpsAdmin notification e-mail target`;
  - `vpsadmin-api.service`, `vpsadmin-notification-dispatcher-email.service`,
    and `container@mailer.service` were active;
  - short API journal scan after verification had no 500/Error/Exception
    matches.
- Checks:
  - `git diff --check` passed in vpsadmin;
  - workspace `git diff --check -- dev-clusters/vpsadmin/nix/test.nix`
    passed;
  - `nix develop .#vpsadmin -c nixfmt --check
    nixos/modules/vpsadmin/api/default.nix
    /home/aither/workspace/ai/vpsfree.cz/dev-clusters/vpsadmin/nix/test.nix`
    passed after formatting;
  - vpsadmin Overcommit was installed/signed before commit;
  - vpsadmin commit hooks passed with Nixfmt and commit-message checks;
  - workspace repo has no declared hook framework.
- Mandatory change review:
  - launched standalone reviewer `019f0541-6a05-79a0-b98a-60e0c23e0146`
    against vpsadmin `7e05f108..0fc58bbbc` and workspace
    `84c83dd2..a4078a1`;
  - result: no blocking, important, or advisory findings;
  - accepted residual risks/test gaps:
    - no automated regression test currently asserts API-side e-mail
      verification reaches SMTP/Mailpit;
    - live verification did not cover SMTP auth, password, or STARTTLS option
      combinations;
    - workspace devcluster commit depends on deploying a vpsadmin revision that
      contains the new `vpsadmin.api.notifications.smtp` option.
- Follow-up still planned:
  - redeploy once more after review so the running dev cluster is tied to the
    committed, formatted source tree.
- Final post-review deployment:
  - ran `dev-clusters/vpsadmin/bin/devcluster update
    2026-06-15-vpsadmin-events services` again after both commits and review;
  - command completed successfully;
  - cluster status was `running` and `ready: yes`;
  - `vpsadmin-api.service`,
    `vpsadmin-notification-dispatcher-email.service`, and
    `container@mailer.service` were active;
  - API notifications config still included SMTP address `127.0.0.1` and
    Mailpit SMTP port `1025`;
  - final admin smoke created target `#9`, verified immediately with
    `verification_token=null`;
  - final regular-user smoke created pending target `#10`;
  - POST `/v7.0/notification_targets/10/send_email_verification` returned
    HTTP 200, `status=true`, `last_error=null`;
  - Mailpit reported one matching verification e-mail with subject
    `Verify your vpsAdmin notification e-mail target`;
  - API journal scan over the final smoke window had no 500/Error/Exception
    matches.

## 2026-06-26 - Automatic user e-mail verification and WebUI polish

- User follow-up after the admin SMTP fix:
  - regular users should receive the custom e-mail target verification message
    automatically when saving the target;
  - the custom e-mail address field should only be visible when `custom` is
    selected in the Recipient dropdown, with a smooth JavaScript transition;
  - the user-list context-switch link works on user details but not from the
    members list.
- Implemented in `vpsadmin`:
  - `NotificationTarget::Create` now sends the verification e-mail after the
    create transaction for non-admin custom e-mail targets;
  - `NotificationTarget::Update` resends the verification e-mail after changing
    a non-admin custom e-mail target kind or address;
  - automatic send failures keep the target pending and record `last_error`,
    so the user can retry from the form instead of losing the target;
  - admins still skip custom e-mail and SMS verification and do not trigger an
    automatic verification e-mail;
  - the WebUI e-mail target form now wraps the custom address, verification,
    and last-error rows in a custom class and toggles them with
    `fadeIn(150)`/`fadeOut(150)` when the Recipient select changes;
  - the hidden custom address input is disabled while the default account
    e-mail target is selected;
  - the members-list context switch now renders the username inside the
    context-switch form submit button;
  - the member filter form state is reset before rendering the members table,
    fixing the browser's dropped nested context-switch forms from that page.
- Checks:
  - initial `nix develop .#api` and `nix develop .#webui` attempts used paths
    with an extra component after the shell hook changed into the component
    directory; reran from the component-relative paths below;
  - `nix develop .#webui --command bash -lc 'php -l
    forms/notifications.forms.php && php -l pages/page_adminm.php && php -l
    tests/Regression/NotificationDeliveryHtmlDetailsTest.php && php -l
    tests/Regression/CsrfContextSwitchTest.php'` passed;
  - `nix develop .#webui --command bash -lc 'vendor/bin/phpunit
    tests/Regression/NotificationDeliveryHtmlDetailsTest.php
    tests/Regression/CsrfContextSwitchTest.php'` first exposed a brittle
    source-slice assertion, then passed with 22 tests and 149 assertions;
  - after fixing the members-list nested-form issue, the same PHPUnit command
    passed with 22 tests and 152 assertions;
  - `nix develop .#api --command bash -lc 'bundle exec rspec
    spec/api/resources/event_routing_spec.rb'` first exposed an unstubbed
    WebUI URL in the send-failure spec; after stubbing it, the command passed
    with 37 examples, 0 failures, and one expected pending plugin-mode case;
  - `nix develop .#api --command bash -lc 'bundle exec rubocop
    lib/vpsadmin/api/resources/notification_target.rb
    spec/api/resources/event_routing_spec.rb'` passed with no offenses;
  - `./test-runner.sh ls 'webui#*'` listed the available WebUI browser
    scripts, including `webui#auth`;
  - first `./test-runner.sh test 'webui#auth'` run failed because the new
    direct-list assertion did not find the expected context-switch form;
  - the second `webui#auth` run used the member-list helper and reproduced the
    real bug: the target row existed, but the context-switch form was missing
    because the filter form wrapper leaked around the results table;
  - after resetting the form wrapper before rendering the members list, the
    third `./test-runner.sh test 'webui#auth'` passed in 721.58 seconds;
  - final `git diff --check` passed.
- Commits:
  - vpsadmin commit
    `826626d757d242ad3540a06ee8dfa9725425acc6`
    (`notifications: send custom e-mail verification on save`) contains the
    API automatic send behavior, e-mail form toggle, and related API/PHP
    regression coverage;
  - vpsadmin commit
    `9efb4c6b036783d5e8cdf94bfc5f0ac60f04a06b`
    (`webui: fix context switch from members list`) contains the member-list
    form-wrapper reset, clickable username submit button, PHP regression, and
    Playwright coverage;
  - initial ambient `git commit` failed because Overcommit hooks were
    installed but the plain shell did not have the `overcommit` gem;
  - both commits were run inside `nix develop`, and Overcommit hooks passed;
  - PhpCsFixer reformatted one PHP regression helper during the second commit,
    and the formatted diff was amended into
    `9efb4c6b036783d5e8cdf94bfc5f0ac60f04a06b`;
  - commit-msg hooks warned about the repository's 72-column text-width
    preference, but all commit message lines stayed under the workspace
    80-column rule;
  - vpsadmin worktree is clean after the commits;
  - `git diff --check HEAD~2..HEAD` passed and both new commit messages have no
    lines longer than 80 columns.
- Mandatory change review:
  - standalone reviewer `019f05d8-ef8b-7d23-94b0-34e41337d449` reviewed
    vpsadmin `0fc58bbbce9f5b31edd6e3e9e918b14a6ddf6d39..9efb4c6b0e3cc78ae105118131790016f8532ba3`;
  - result: no blocking, important, or code/security/compatibility/deployment
    findings;
  - advisory: the first new commit hash recorded in this state file was
    incorrect; corrected to
    `826626d757d242ad3540a06ee8dfa9725425acc6`;
  - accepted residual risks/test gaps:
    - notification form fade behavior is covered by PHP/source regression
      checks rather than a browser interaction test;
    - the reviewer did not rerun the already completed long `webui#auth` or
      full suites.

## 2026-06-27 notification template/recipient model review

- Reviewed the current vpsAdmin notification model after the generic
  template, target, SMS, and Telegram changes.
- Current findings:
  - `notification_template_variants` is already the protocol-specific template
    store: rows are unique by template, protocol, and language, and carry
    render fields plus serialized `options`;
  - `notification_templates` remains protocol-neutral template identity and
    user visibility metadata;
  - `email_recipients` and
    `notification_template_email_recipients` are still only legacy/admin
    e-mail recipient groups used by `NotificationTemplate.send_email!`;
  - `user_email_role_recipients` and
    `user_notification_template_recipients` are still active only in legacy
    e-mail recipient resolution, and the event migration backfills them into
    explicit e-mail notification receivers/routes for advanced settings;
  - routed SMS and Telegram delivery does not use role recipient rows; it uses
    event routes, notification receivers, and action-specific
    notification targets.
- Recommendation for later implementation:
  - do not add a protocol-specific `custom` column to
    `notification_templates`; keep template-level data protocol-neutral;
  - keep protocol render metadata on `notification_template_variants.options`
    or a future normalized variant-settings table if it needs validation;
  - move remaining recipient policy out of template tables and into
    notification routes/receivers/targets;
  - retire the legacy e-mail recipient APIs after a compatibility window, or
    keep them explicitly named as e-mail-only compatibility surfaces until
    removed;
  - if role-based defaults are still desired, reintroduce them as a
    protocol-neutral route preset/default receiver concept, not as
    `user_email_role_recipients`.
- Adjacent issue noticed: the API built-in template installer supports
  `email`, `telegram`, and `sms`, but the standalone
  `notification_templates` uploader still advertises only `email` and
  `telegram` in its protocol list.
- No code changes or tests were run for this investigation.

Follow-up direction from 2026-06-27:

- The target design should not keep legacy e-mail compatibility APIs/tables.
- `user_email_role_recipients` can be removed after migration if the event
  stream exposes stable route-filter parameters for the old account/admin
  recipient intent.
- Prefer a new explicit event parameter such as `recipient_role` for old
  template roles (`account`, `admin`) instead of overloading existing
  domain-specific `role` parameters used by requests, outages, and monitoring.
- Existing `user_email_role_recipients` rows should be migrated to concrete
  event routes, notification receivers, and e-mail targets, then the table/API
  can be dropped.
- Template-level e-mail recipients are global recipient configurations. The
  clean replacement must model global notification policy explicitly, separate
  from user-owned routes for the event subject/user.
- Production use of `email_recipients` and
  `notification_template_email_recipients` should be inventoried before
  deciding how to migrate system/admin recipient groups such as daily report,
  payments overview, request admin messages, and old generic outage reports.
- Keep the standalone `notification_templates` uploader protocol-list issue on
  the implementation checklist.

Production `mail_template_recipients` inventory supplied by user:

- Alert admin templates for monthly traffic and unpaid CPU/data-flow alerts
  send directly to `aither`, `kerry`, and `snajpa`.
- User paid CPU alert templates BCC `admins_bcc`
  (`snajpa@snajpa.net,aither@havefun.cz`).
- `daily_report` goes to `aither`, `kerry`, and `snajpa`.
- `payments_overview` goes to `aither` and `kerry`.
- Account lifecycle/payment templates (`expiration_user_active`,
  `user_create`, `user_suspend`, `user_soft_delete`, `user_resume`,
  `user_revive`) BCC `vpsadmin@kerrycze.net`; this is an operational/global
  recipient configuration for mail rendered for arbitrary users, not Kerry's
  per-user account/admin role routing.
- No request or generic outage template recipients appeared in this production
  inventory.
- Added detailed implementation plan to `plan.md` under
  `2026-06-27 Clean Recipient Model Follow-up`. The route-scope/global-route
  idea was superseded by a permission-aware visibility/routing model: ordinary
  users see only their own events, admins see all events, and deliveries are
  tied to materialized routing contexts. The plan covers `recipient_roles`
  event metadata, array-contains route matchers, context matchers for
  direct/other-user/system events, legacy recipient migrations, delivery
  visibility filtering, and the standalone template uploader SMS protocol fix.
- Refined the follow-up plan after confirming visibility requirements:
  visibility uses current permissions, not snapshots. Current behavior should
  be ordinary users seeing their own events and admins seeing all events.
  Persist per-user event rows only as `event_routing_contexts` when routes
  produce durable state such as deliveries, suppression, failure, or
  read/ack/bookmark state. Routes get subject scopes/context matchers for
  direct, other-user, visible, and system events; default routes remain
  direct-only so admins do not receive all events unless they create explicit
  routes. API delivery visibility must also check current event visibility, so
  demoted admins cannot browse old other-user events/deliveries.

Implementation progress on 2026-06-27:

- Implemented routing contexts in `vpsadmin`:
  - added `event_routing_contexts`;
  - added optional `event_deliveries.event_routing_context_id`;
  - added `event_routes.subject_scope` with `self` and `visible` scopes;
  - backfilled existing deliveries into direct routing contexts.
- Reworked event visibility and routing:
  - ordinary users can see their own events;
  - admins can see all events through current permissions;
  - default routes remain direct/self-only;
  - admin-visible routes can tap into other users' visible events and system
    events, but contexts are materialized only when a route produces durable
    state;
  - routed e-mail deliveries now address the route owner or route receiver
    target, not global template recipients.
- Added route matcher support for routing context fields and array matching:
  - `context.subject_relation`;
  - `context.subject_user_id`;
  - `context.subject_is_self`;
  - `context.subject_is_admin_visible`;
  - `parameters.recipient_roles`;
  - `contains` and `not_contains` operators.
- Added `recipient_roles` event metadata from notification template role
  metadata without rendering dynamic templates.
- Removed legacy e-mail recipient runtime surfaces:
  - `EmailRecipient`;
  - `NotificationTemplateEmailRecipient`;
  - `UserEmailRoleRecipient`;
  - `UserNotificationTemplateRecipient`;
  - corresponding API resources and specs.
- Added migration `20260624121000_migrate_legacy_email_recipients_to_routes.rb`
  to convert production `email_recipients` and
  `notification_template_email_recipients` rows into admin-owned visible
  routes, receivers, and e-mail notification targets, then drop the old
  recipient tables.
- Updated the older event migration so existing `user_email_role_recipients`
  are converted to route matchers on `parameters.recipient_roles contains
  <role>`.
- Updated daily report, payments overview, outage report, event routing, event
  route, and notification template specs for the new route-context model.
- Kept event subject data and delivery recipient data separate in template
  rendering:
  - template variables continue to describe the event subject/user;
  - `opts[:user]` uses the delivery recipient for language, time zone, and
    mail-log ownership;
  - Telegram template rendering now passes the delivery just like e-mail and
    SMS.
- Fixed the adjacent standalone template uploader protocol list by adding
  `sms` to `notification_templates/lib/vpsadmin/notification_templates/meta.rb`.

Compatibility and deployment notes:

- This is intentionally incompatible with the old e-mail recipient API and
  tables. The user explicitly accepted removing legacy e-mail compatibility
  surfaces.
- The database migration order is important:
  - `20260615110000_add_events.rb` must still see
    `user_email_role_recipients` so it can migrate role recipients into event
    routes;
  - `20260624120000_add_event_routing_contexts.rb` adds routing contexts and
    backfills existing event deliveries;
  - `20260624121000_migrate_legacy_email_recipients_to_routes.rb` migrates
    global template recipients into admin-visible routes and drops the old
    tables.
- Rollback after the final migration would require restoring the dropped
  recipient tables from backup or adding a reverse compatibility migration.
  The new runtime does not read those tables.

Verification run on 2026-06-27:

- Ruby syntax checks passed for modified models, resources, migrations, specs,
  and notification template metadata.
- Focused API/model specs passed:
  `nix develop ..#api -c bundle exec rspec --format progress
  spec/models/event_route_spec.rb
  spec/api/resources/event_routing_spec.rb
  spec/api/resources/notification_template_spec.rb
  spec/models/transaction_chains/mail/daily_report_spec.rb
  spec/models/transaction_chains/plugins/payments/mail_overview_spec.rb
  spec/models/transaction_chains/plugins/outage_reports/update_spec.rb`
  with `131 examples, 0 failures, 1 pending`.
- After the recipient/subject template-rendering fix, the focused suite was
  rerun with the same result: `131 examples, 0 failures, 1 pending`.
- Endpoint coverage specs passed:
  `nix develop ..#api -c bundle exec rspec --format progress
  spec/api/endpoint_coverage_spec.rb
  spec/api/generate_pending_endpoints_spec.rb
  spec/api/custom_routes_coverage_spec.rb`
  with `2 examples, 0 failures`.
- Stale-reference scan for removed recipient models/resources found no runtime
  or spec references outside migration/schema history.
- Local equivalent of the API spec topic coverage check passed for current
  worktree contents:
  `OK: topic mapping covers all 382 current API spec files exactly once`.
- `git diff --check` passed.

Open status:

- Changes are implemented but not committed yet.
- Full API spec suite and GitHub Actions have not been run locally.
- The mandatory change review has not been run yet because the changes are not
  committed. Run it after committing and quick local verification, before any
  long integration test pass.

Devcluster deployment on 2026-06-27:

- Staged all `vpsadmin` worktree changes with `git add -A` before deployment so
  the local Nix flake source included new migration/model files.
- Updated `dev-clusters/vpsadmin/nix/test.nix` dev seed to support the new route
  model while still tolerating old checkouts:
  - when legacy e-mail recipient models exist, keep using the old seed path;
  - when event routes are available, create a custom e-mail target, receiver,
    and visible-scoped route for the seeded daily report recipient.
- First `devcluster update 2026-06-15-vpsadmin-events services` failed because
  the old dev database contained synthetic legacy recipient
  `dev-admin@example.test` / `Dev admins`, which intentionally cannot be
  resolved to exactly one admin user by the production migration.
- Reset the devcluster state as allowed by the user:
  `dev-clusters/vpsadmin/bin/devcluster reset 2026-06-15-vpsadmin-events`.
- Restarted with single topology on the bridge network:
  `dev-clusters/vpsadmin/bin/devcluster start 2026-06-15-vpsadmin-events
  --topology single --network bridge`.
- The start reached `ready: yes` but exited non-zero on the known late `node1`
  osctld socket race:
  `No such file or directory - connect(2) for /run/osctl/osctld.sock`.
  Verified `osctld` and `nodectld` were running, then recovered with
  `dev-clusters/vpsadmin/bin/devcluster update 2026-06-15-vpsadmin-events
  node1`.
- Deployment verification passed:
  - cluster status: running, topology `single`, network `bridge`, `ready: yes`;
  - `systemctl --failed` on `services`: `0 loaded units listed`;
  - `vpsadmin-api.service`: active/running;
  - `vpsadmin-database-setup.service`: active/exited successfully;
  - `vpsadmin-devcluster-seed.service`: exited successfully;
  - API endpoint `https://api.aitherdev.int.vpsfree.cz/v7.0/`: HTTP 200;
  - Web UI endpoint `https://webui.aitherdev.int.vpsfree.cz/`: HTTP 200;
  - database has `event_routing_contexts`;
  - database has `event_routes.subject_scope`;
  - legacy `email_recipients` and `notification_template_email_recipients`
    tables are absent;
  - seeded routes are three per-user default routes plus admin route
    `Dev admins daily_report` with `event_type = system.daily_report`,
    `template_name = daily_report`, and `subject_scope = visible`.

Follow-up implementation on 2026-06-27:

- Removed redundant `context.subject_relation == system` matchers from
  dedicated system report recipient migration output:
  - `daily_report` -> `system.daily_report`;
  - `payments_overview` -> `payments.overview`.
- Kept relation matchers for other migrated admin-visible routes that still
  need `other_user` narrowing.
- Updated the devcluster route seed so fresh new-style daily report routes no
  longer create the redundant system matcher.
- Added `subject_scope` Web UI support for notification routes:
  - route create/edit forms now expose a `Scope` select;
  - route/subroute tables show `Own events` or `Visible events`;
  - submitted route forms pass `subject_scope` to the API.
- Fixed notification event-log filters so submitted empty strings for optional
  enum filters are ignored:
  - `event_type`;
  - `category`;
  - `severity`;
  - `routing_state`;
  - delivery `action`.
  Severity and routing-state selects now include the empty `---` option.
- Added Web UI regression coverage for route-scope controls and event-log empty
  filters.

Verification run for follow-up on 2026-06-27:

- Ruby syntax checks passed for the changed migration and focused specs.
- PHP syntax checks passed for `webui/forms/notifications.forms.php` and
  `webui/tests/Regression/NotificationRouteUiTest.php`.
- Focused API specs passed:
  `nix develop ..#api -c bundle exec rspec --format progress
  spec/api/resources/event_routing_spec.rb
  spec/models/transaction_chains/mail/daily_report_spec.rb
  spec/models/transaction_chains/plugins/payments/mail_overview_spec.rb`
  with `47 examples, 0 failures, 1 pending`.
- Focused Web UI regression passed:
  `nix develop .#webui -c composer --working-dir=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-06-15-vpsadmin-events/vpsadmin/webui test -- --filter NotificationRouteUiTest`
  with `4 tests, 30 assertions`.
- Full Web UI PHPUnit suite passed functionally:
  `nix develop .#webui -c composer --working-dir=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-06-15-vpsadmin-events/vpsadmin/webui test`
  with `46 tests, 286 assertions`; PHPUnit reported 2 warnings from the
  existing `OutageDetailsReporterNameXssTest` fixture accessing missing
  security advisory properties in `webui/forms/outage.forms.php`.
- `git diff --check` passed in the `vpsadmin` worktree and for the workspace
  `dev-clusters/vpsadmin/nix/test.nix` diff.

## 2026-06-27 migration test harness

- Implemented generic vpsAdmin migration specs:
  - `api/spec/migration_helper.rb` sets up a standalone RSpec entrypoint that
    does not require the normal current-schema `spec_helper`;
  - specs use an isolated test DB suffix and inline old schemas/data;
  - specs run migrations directly and inspect rows through raw ActiveRecord
    connection helpers, avoiding current application models.
- Added migration-test enforcement:
  - `tools/check_migration_specs.rb` checks added migrations against matching
    `api/spec/migrations/<timestamp>_<name>_spec.rb` files;
  - Overcommit pre-commit hook `MigrationSpecs` runs the staged check;
  - `.github/workflows/api-migration-specs.yml` runs affected migration specs
    on PR/push and all migration specs weekly/manual;
  - API topic coverage now excludes `spec/migrations/**/*_spec.rb`, since
    those specs are owned by the dedicated migration workflow.
- Added migration specs for the event-notification branch migrations:
  - legacy mail table renames;
  - notification template variant e-mail-column relaxation;
  - event table creation and advanced user recipient/role recipient backfill;
  - action integer/string conversion and irreversible unknown-action rollback;
  - user notification delivery method creation from `users.mailer_enabled`;
  - removal/rollback of `users.mailer_enabled`;
  - routing context schema/backfill;
  - global legacy e-mail recipients to visible admin event routes.
- The routing-context migration now backfills system-event contexts with
  `source = system_route`, matching runtime routing behavior.
- Verified current upstream action tags before editing workflows:
  - `actions/checkout` latest major is `v7`, used in touched workflows;
  - `actions/upload-artifact@v7`, `actions/download-artifact@v8`, and
    `ruby/setup-ruby@v1` remain compatible with the existing workflow shape.
- Verification:
  - Ruby syntax checks passed for the new helper, specs, hook, script, and
    touched migration.
  - Workflow YAML parsed with Ruby YAML aliases enabled.
  - Standalone migration specs passed:
    `nix develop .#api -c bundle exec rspec --options /dev/null --format
    documentation spec/migrations` with `21 examples, 0 failures`.
  - Targeted RuboCop passed for the new migration-test files and touched event
    files.
  - `tools/check_migration_specs.rb --cached` passed.
  - `tools/check_migration_specs.rb --base origin/master --head HEAD` passed.
  - `git diff --cached --check` passed.
  - Overcommit hooks passed after signing the updated local hook signatures:
    `MigrationSpecs`, `Nixfmt`, `RuboCop`, and `PhpCsFixer`.

Follow-up cleanup on 2026-06-28:

- Removed personal production names and domains from the legacy global
  recipient migration spec, replacing them with neutral admin fixture accounts
  and `example.test` addresses.
- Verified no `aither`, `kerry`, `snajpa`, `havefun`, or `kerrycze` strings
  remain in `api/spec/migrations` or `api/spec/migration_helper.rb`.
- Focused verification passed:
  `nix develop .#api -c bundle exec rspec --options /dev/null --format
  documentation
  spec/migrations/20260624121000_migrate_legacy_email_recipients_to_routes_spec.rb`
  with `5 examples, 0 failures`.
- Targeted RuboCop passed for the changed migration spec.

## 2026-06-28 delivery rate limits and event-noise cleanup

Requested changes implemented in the `vpsadmin` worktree:

- Added generic event delivery rate limits for `email`, `webhook`,
  `telegram`, and `sms` with rolling `minute`, `hour`, `day`, and `week`
  windows.
- Added default limit configuration through the notifications NixOS module and
  passed it to both API and notification dispatcher configs.
- Added per-user admin overrides through nested
  `user.notification_rate_limit` API resources and the WebUI Notifications
  `Limits` view.
- Added usage/reset/remaining fields to the API output so the WebUI can show
  effective default vs overridden limits.
- Added `recipient_user_id` to delivery attempts for efficient per-user/action
  counting.
- Added a `notification_rate_limit_states` table used as a per-user/action lock
  so the dispatcher rate-limit check and delivery-attempt claim happen
  atomically for parallel workers.
- Changed normal event emission to skip persistence when routing prepares no
  releasable delivery. Explicit test/diagnostic events still persist with
  `persist: :always`.
- Moved route hit-counter updates to persisted routing results only.
- Moved the WebUI `Notifications` menu item to the last logged-in menu entry.
- Fixed dev-cluster Telegram startup: when a bot token exists under the
  dev-cluster Telegram secret directory, `devcluster start` now performs a
  post-ready services update so Telegram is enabled on first start.

Compatibility notes:

- Database changes are additive. The new dispatcher code requires the
  migration before it starts, but old code can run with the new tables/column
  present.
- Old code ignores `event_delivery_attempts.recipient_user_id` if rolled back.
- The event persistence change is behavioral only. Rolling back to old code
  can resume storing skipped-only events without a data migration.
- Per-user override rows are optional. Missing rows fall back to configured
  defaults for all current delivery methods and periods.

Schema/migration notes:

- An ambient `bundle exec rake db:migrate db:schema:dump` failed because gems
  were missing outside the Nix API shell.
- Replaying all migrations in the temporary test DB failed on old migration
  classes under Rails 8.1, which matches the existing need for migration-spec
  harnesses in this branch.
- A temporary schema dump attempt after applying only the new migration created
  a noisy table-order diff and was discarded. `api/db/schema.rb` was restored
  from the previous head and manually patched for the additive schema delta.
- The new migration was successfully applied on top of the restored schema in
  a temporary DB before the manual schema patch.

Verification before commit:

- Ruby syntax checks passed for the changed notification/event model and API
  files and the focused specs.
- PHP syntax checks passed for:
  - `webui/forms/notifications.forms.php`;
  - `webui/pages/page_notifications.php`;
  - `webui/pages/page_adminm.php`;
  - `webui/public/index.php`.
- Bash syntax passed for `dev-clusters/vpsadmin/bin/devcluster`.
- Nix parse checks passed for:
  - `nixos/modules/vpsadmin/notifications.nix`;
  - `nixos/modules/vpsadmin/api/default.nix`;
  - `nixos/modules/vpsadmin/notification-dispatcher.nix`.
- Focused single regression passed:
  `nix develop .#api -c bash -lc 'bundle exec rspec
  spec/models/tasks/event_delivery_spec.rb:1697'` with 1 example,
  0 failures.
- Standalone migration spec passed:
  `nix develop .#api -c bash -lc 'bundle exec rspec --options /dev/null
  --format documentation
  spec/migrations/20260628120000_add_notification_rate_limits_spec.rb'` with
  2 examples, 0 failures.
- Broader focused API/model suite passed:
  `nix develop .#api -c bash -lc 'bundle exec rspec
  spec/api/resources/user_write_spec.rb
  spec/models/tasks/event_delivery_spec.rb spec/models/event_route_spec.rb
  spec/api/resources/event_routing_spec.rb'` with 185 examples, 0 failures,
  2 expected pending examples.
- `git diff --check` passed in the `vpsadmin` worktree.

Open status:

- vpsAdmin implementation committed as
  `8fc7171c9 notifications: rate limit event deliveries`.
- Workspace devcluster helper committed as
  `f782154 devcluster: enable telegram after first start`.
- vpsAdmin Overcommit hooks passed during commit:
  `Nixfmt`, `MigrationSpecs`, `RuboCop`, `PhpCsFixer`, and commit-message
  hooks.
- Hook setup note: the first vpsAdmin commit attempts failed before hooks ran
  because the ambient shell could not load the Overcommit gem. The root
  development bundle was refreshed in the default Nix shell and the final
  commit was made with hooks enabled through that bundle.
- Mandatory change review launched with standalone reviewer `Kierkegaard`
  against vpsAdmin `4603b9de6..7da8e59b6` and workspace
  `a4078a1..f782154`.
- Mandatory review result:
  - blocking finding: `Events.emit!` can now return `nil` for skipped-only
    routing, but several transaction chains still dereferenced the returned
    event and could raise `NoMethodError` instead of treating suppression as
    handled;
  - blocking finding: existing transaction-chain specs still expected a
    persisted suppressed expiration event;
  - important finding: rate-limit coverage did not exercise the weekly window
    or the lock boundary that prevents parallel workers from overshooting a
    limit.
- Follow-up fixes before amend:
  - nil-safe delivery-preparation guards added for incident reports, incident
    replies, daily reports, failed-login reports, and OOM reports;
  - notification-only chains that can now legitimately produce no transaction
    were marked `allow_empty`;
  - suppressed expiration, incident, failed-login, and OOM specs now assert no
    event persistence and no retry loop where applicable;
  - dispatcher specs now cover weekly windows, single-slot consumption across
    two webhook deliveries, and that stale reclaim work runs inside the
    rate-limit claim lock.
- Follow-up verification:
  - focused transaction-chain and dispatcher regression suite:
    `nix develop .#api -c bash -lc 'bundle exec rspec --format
    documentation spec/models/transaction_chains/incident_report/send_spec.rb
    spec/models/transaction_chains/incident_report/reply_spec.rb
    spec/models/transaction_chains/vps/oom_reports_spec.rb
    spec/models/transaction_chains/user/report_failed_logins_spec.rb
    spec/models/transaction_chains/lifetimes/expiration_warning_spec.rb
    spec/models/tasks/event_delivery_spec.rb'` with 99 examples, 0 failures;
  - original broader focused notification/API suite:
    `nix develop .#api -c bash -lc 'bundle exec rspec
    spec/api/resources/user_write_spec.rb spec/models/tasks/event_delivery_spec.rb
    spec/models/event_route_spec.rb spec/api/resources/event_routing_spec.rb'`
    with 188 examples, 0 failures, 2 expected pending examples;
  - targeted RuboCop passed for the changed transaction-chain and dispatcher
    files/specs;
  - `git diff --check` passed.
- The vpsAdmin commit was amended from `7da8e59b6` to `b9a30e863` with the
  review fixes. Overcommit hooks passed again during amend.
- Same-reviewer follow-up confirmed the prior blocking and important findings
  are addressed on `b9a30e863`. Residual risk remains that long
  integration/dev-cluster tests and full CI were not rerun after the amend.

## 2026-06-28 WebUI Limits 500 Follow-up

User reported that the dev-cluster WebUI returned HTTP 500 when opening
`Notifications -> Limits`.

Diagnosis:

- Dev cluster `2026-06-15-vpsadmin-events` was running and ready on the bridge
  network.
- WebUI nginx/PHP-FPM logs in the `webui` container showed:
  `PHP Fatal error: Uncaught Error: Call to a member function list() on false
  in /mnt/vpsadmin/webui/forms/notifications.forms.php:2777`.
- The failing code called `$user->notification_rate_limit->list()` on a shown
  user object. In the PHP HaveAPI client, the new nested resource is available
  reliably through the nested user handle, matching existing nearby code:
  `$api->user($id)->notification_rate_limit`.
- A raw API request initially returned `Action not found` for
  `/v7.0/users/1/notification_rate_limits` because `vpsadmin-api.service` runs
  from a Nix store build. Restarting Puma alone kept the stale store revision;
  `devcluster update 2026-06-15-vpsadmin-events services` was required to
  rebuild and activate the services VM with the current worktree.

Changes made:

- WebUI rate-limit listing now uses
  `$api->user($user->id)->notification_rate_limit->list()`.
- WebUI rate-limit updates now use
  `$api->user($user_id)->notification_rate_limit($limit->id)->update(...)`.
- Added a PHPUnit regression that reproduces the shown-user nested resource
  being `false` and verifies the direct nested API handle is used instead.

Verification:

- `nix develop .#webui -c composer test -- --filter
  NotificationDeliveryHtmlDetailsTest`: 20 tests, 143 assertions, 0 failures.
- PHP syntax checks passed for:
  - `webui/forms/notifications.forms.php`;
  - `webui/pages/page_notifications.php`;
  - `webui/tests/Regression/NotificationDeliveryHtmlDetailsTest.php`.
- `nix develop .#api -c bundle exec rspec --format progress
  spec/api/resources/user_write_spec.rb`: 52 examples, 0 failures,
  1 expected pending example.
- `git diff --check` passed.
- `devcluster update 2026-06-15-vpsadmin-events services` completed and
  activated the rebuilt services system.
- Raw API verification after activation:
  `GET https://api.aitherdev.int.vpsfree.cz/v7.0/users/1/notification_rate_limits`
  returned HTTP 200 with all email/webhook/telegram/sms minute/hour/day/week
  default limits.
- Authenticated WebUI verification as `test-admin`:
  `GET https://webui.aitherdev.int.vpsfree.cz/?page=notifications&action=limits&user=1`
  returned HTTP 200 and rendered `Notification delivery limits` with weekly
  rows for webhook, Telegram, and SMS.
- Fresh webui logs after the authenticated request showed no recurrence of the
  `notifications.forms.php:2777` fatal. The request still emits an existing
  unrelated `cluster.lib.php` sidebar warning.
- The rate-limit commit was amended again from `b9a30e863` to `c3faa7490`
  with the WebUI nested-resource fix. Overcommit hooks passed during amend.
- Mandatory change review launched with standalone reviewer `Kuhn` against
  bugfix delta `b9a30e863..c3faa7490` and surrounding rate-limit commit
  context `4603b9de6..c3faa7490`.
- Mandatory review result:
  - no blocking, important, or advisory findings;
  - reviewer confirmed the nested user API handle fix matches the API route
    and covers the shown-resource nested handle being `false`;
  - reviewer reran
    `nix develop .#webui -c composer test -- --filter
    NotificationDeliveryHtmlDetailsTest` with 20 tests, 143 assertions,
    0 failures;
  - residual gap: no full browser/POST flow was added; dev-cluster manual
    GET verification remains the evidence for the reported 500.

## 2026-06-28 User Detail Delivery Methods Colspan Follow-up

User reported that the WebUI user-detail form `Event delivery methods` has
rows with too-wide `colspan=3`, while the form otherwise has only two columns.

Changes made:

- `adminm_print_notification_delivery_methods()` now defines two table
  columns instead of three.
- The explanatory row and `Delivery limits` link row now use `colspan=2`.
- Added a PHPUnit source regression that checks the helper keeps a two-column
  shape.

Verification:

- PHP syntax checks passed for:
  - `webui/pages/page_adminm.php`;
  - `webui/tests/Regression/NotificationDeliveryHtmlDetailsTest.php`.
- `nix develop .#webui -c composer test -- --filter
  NotificationDeliveryHtmlDetailsTest`: 21 tests, 149 assertions,
  0 failures.
- `git diff --check` passed.
- Restarted dev-cluster `webui` PHP-FPM and authenticated as `test-admin`;
  `GET https://webui.aitherdev.int.vpsfree.cz/?page=adminm&section=members&action=edit&id=1`
  rendered `Event delivery methods` with two headers, intro/link rows using
  `colspan="2"`, and checkbox rows using one label cell plus one value cell.
- The rate-limit commit was amended from `c3faa7490` to `8fc7171c9` with
  this colspan fix. Overcommit hooks passed during amend.
- Mandatory change review launched with standalone reviewer `Boole` against
  the focused colspan fix and surrounding rate-limit commit context.
- Mandatory review result:
  - no blocking, important, or advisory findings;
  - reviewer confirmed `page_adminm.php` now defines two header cells and uses
    `colspan='2'` for the intro and `Delivery limits` rows;
  - reviewer confirmed the source regression covers the two-column shape and
    absence of `colspan='3'`;
  - residual gap: automated coverage is source-level rather than rendered-DOM
    coverage; dev-cluster manual verification covers the actual rendered page.

## 2026-06-28 Route Match And Test Event Follow-up

User asked to extend test notifications so admins can fire notifications with
different subject scopes, and asked whether `events.matched_event_route_id` is
correct when multiple routes can match through `continue=true`.

Finding:

- The singular `events.matched_event_route_id` was imprecise. Routing can
  match a parent and child route and can also match multiple sibling routes
  when `continue` is true. `event_routing_contexts.matched_event_route_id`
  had the same limitation for a user's routing context.

Changes made in `vpsadmin`:

- Added `event_route_matches` as the persisted route-attribution model with
  route owner, subject relation, source, and match order.
- Removed runtime use of singular matched-route columns from `events` and
  `event_routing_contexts`; added a migration that backfills the new table,
  drops the old columns on upgrade, and restores a first-match approximation
  on rollback.
- Added nested event API endpoints `event.route_match#index` and
  `event.route_match#show`, plus event-log filtering by `event_route_id`.
- Updated routing persistence so matched routes are recorded before deliveries
  and plan-only OOM evaluation can explicitly increment matched route hit
  counts without persisting events.
- Extended `Event::Test` with admin-only `subject_scope` values:
  `self`, `visible`, and `system`.
- Updated the WebUI event detail page to show a `Matched routes` table instead
  of one `Matched route`, and changed route hit links/event filtering to use
  `event_route_id`.
- Changed generated default e-mail receiver/target labels from
  `Default e-mail` to `Default`, including lazy normalization of legacy
  generated rows and a migration for existing data.
- Adjusted receiver action status rendering so receiver details read
  receiver-action `target_enabled`/`delivery_method_enabled` fields instead of
  treating the link row itself as the reusable target.
- Added source/API/model/migration regressions for the new route-match model,
  test event scopes, default-label normalization, and receiver action status.

Compatibility notes:

- Upgrade preserves old singular attribution by backfilling one or more
  `event_route_matches` rows before dropping the old columns.
- Rollback recreates `matched_event_route_id` columns and restores the first
  recorded route per event/context as a best-effort approximation; multiple
  route matches cannot be represented in the old schema.
- Old generated `Default e-mail` labels are normalized to `Default` only for
  generated default receivers/targets. Custom labels are left unchanged.
- Unrouted events may remain unpersisted, matching the current design choice;
  tests now expect stale unmatched transaction-chain state events to return
  `nil`.

Verification:

- API syntax:
  - `nix develop .#api -c ruby -c db/migrate/20260628130000_refine_event_route_matches.rb`
  - `nix develop .#api -c ruby -c models/event_route_match.rb`
  - `nix develop .#api -c ruby -c lib/vpsadmin/api/events.rb`
  - `nix develop .#api -c ruby -c lib/vpsadmin/api/resources/event.rb`
  - `nix develop .#api -c ruby -c lib/vpsadmin/supervisor/node/oom_reports.rb`
- WebUI syntax:
  - `nix develop .#webui -c php -l forms/notifications.forms.php`
  - `nix develop .#webui -c php -l pages/page_notifications.php`
  - `nix develop .#webui -c php -l tests/Regression/NotificationRouteUiTest.php`
- Migration spec:
  - `nix develop .#api -c bundle exec rspec --format progress
    spec/migrations/20260628130000_refine_event_route_matches_spec.rb`:
    2 examples, 0 failures.
- Focused runtime API specs:
  - `nix develop .#api -c bundle exec rspec --format progress
    spec/models/event_route_spec.rb
    spec/api/resources/event_routing_spec.rb
    spec/api/resources/transaction_chain_read_spec.rb
    spec/models/notification_events_spec.rb
    spec/models/transaction_chains/plugins/monitoring/alert_spec.rb
    spec/supervisor/node/oom_reports_spec.rb`: 116 examples, 0 failures,
    1 expected pending.
- WebUI regression:
  - `nix develop .#webui -c composer test -- --filter
    NotificationRouteUiTest`: 7 tests, 54 assertions, 0 failures.
- Endpoint coverage:
  - `nix develop .#api -c bundle exec rspec --format progress
    spec/api/endpoint_coverage_spec.rb`: 1 example, 0 failures.
- Targeted RuboCop:
  - `nix develop .#api -c bundle exec rubocop ...`: 12 files inspected,
    no offenses detected.
- `git diff --check` passed.
- Overcommit hooks are installed in
  `/home/aither/workspace/ai/vpsfree.cz/repos/vpsadmin.git/hooks` and the
  repository has signed Overcommit configuration entries.
- The rate-limit commit was amended from `8fc7171c9` to `a78d11095` with the
  route-match, test-scope, default-label, and receiver status fixes.
  Overcommit hooks passed during amend:
  `MigrationSpecs`, `Nixfmt`, `PhpCsFixer`, `RuboCop`, and commit-message
  hooks, with only a non-blocking 72-column warning from the commit-message
  hook.
- Mandatory change review launched with standalone reviewer `Hypatia` against
  focused delta `8fc7171c9..a78d11095` and surrounding rate-limit commit
  context `4603b9de6..a78d11095`.
- Mandatory review result:
  - no blocking findings;
  - one important finding: the route-match migration is non-additive because
    it drops `events.matched_event_route_id` and
    `event_routing_contexts.matched_event_route_id`, while the plan still
    described this slice as additive;
  - no advisory findings;
  - reviewer agreed the amend is acceptable because the delta fixes behavior
    introduced by the same unmerged feature commit.
- Review follow-up:
  - chose not to retain the old singular columns for a compatibility cycle,
    because they cannot represent continuing parent/child/sibling matches and
    this branch already has coordinated app+DB activation requirements;
  - updated `plan.md` compatibility notes to explicitly call out the
    non-additive route-match cleanup and the requirement to activate API/WebUI
    processes on the new revision together with that migration.
- Dev-cluster activation and live verification:
  - `devcluster update 2026-06-15-vpsadmin-events services` rebuilt and
    activated the services host; the command exited with status 1 after the
    final `Preparing node1 pool runtime and restarting nodectld` helper step,
    without a diagnostic line.
  - Post-activation status showed the cluster still `running`, `bridge`, and
    `ready: yes`; `services` had no failed systemd units.
  - `vpsadmin-api.service`, `vpsadmin-telegram-receiver.service`, and
    `vpsadmin-notification-dispatcher-telegram.service` are active. This
    confirms Telegram is enabled in the dev cluster with the configured token.
  - Schema check on `services` showed latest migration `20260628130000`,
    `event_route_matches` exists, and `events.matched_event_route_id` is gone.
  - Ran the known follow-up node refresh
    `devcluster update 2026-06-15-vpsadmin-events node1`; it completed
    successfully, restarted `nodectld`, and ran `osctl activate --system`.
  - Final `devcluster status` reports `running`, topology `single`, network
    `bridge`, `ready: yes`; `services` has 0 failed units; node1
    `nodectld` reports `State: running`.
- Raw API live checks:
  - `GET /v7.0/users/1/notification_rate_limits` as `test-admin` returned
    HTTP 200 with email/webhook/telegram/sms minute/hour/day/week defaults.
  - `GET /v7.0/events/16/route_matches` returned HTTP 200 and the new plural
    route match row for `event_route_id=1`, `subject_relation=self`, source
    `direct_route`.
  - `POST /v7.0/events/test` with `subject_scope=system` returned HTTP 200
    and created event `#17` with `user=nil`, `subject_relation=system`, and
    routing state `suppressed`.
  - `GET /v7.0/events?event[event_route_id]=1` returned only events with the
    recorded route match filter applied.
- Authenticated WebUI live checks as `test-admin`:
  - `GET ?page=notifications&action=limits&user=1` returned HTTP 200 and
    rendered `Notification delivery limits` with weekly rows.
  - `GET ?page=adminm&section=members&action=edit&id=1` returned HTTP 200,
    rendered `Event delivery methods`, had no `colspan="3"`, and had
    `colspan="2"` rows where expected.
  - Main navigation renders `Notifications` as the last item.
  - `GET ?page=notifications&action=routes&user=1` returned HTTP 200 and
    rendered `Default` labels without `Default e-mail`.
  - Targets, receivers, and receiver `#1` detail/edit pages returned HTTP 200
    and did not render `target disabled` for enabled linked targets.
  - `GET ?page=notifications&action=test&user=1` returned HTTP 200 and
    rendered admin subject-scope options `Own routes`, `Admin visible routes`,
    and `Admin system routes`.
  - Event detail `#17` rendered the plural `Matched routes` section with
    `No routes matched`; event detail `#16` rendered `Matched routes` with
    `Default route`, `self`, and `direct_route`.

GitHub push and CI watch:

- Pushed `a78d11095` to `origin/2026-06-15-vpsadmin-events`.
- Initial GitHub Actions results for `a78d11095`:
  - success: `API Migration Specs` `28335027602`, `RuboCop` `28335027644`,
    `Webui PHPUnit` `28335027603`, `libnodectld Specs` `28335027622`;
  - failure: `API Specs (topic parallel)` `28335027612`;
  - old aggregate `CI` run `28335027608` was still active after the branch was
    superseded.
- Inspected failed API spec logs with
  `gh run view 28335027612 --log-failed`.
- Failure root cause:
  - event persistence had been tied only to releasable deliveries, so events
    with matched routes but muted or suppressed deliveries were dropped;
  - truly unrouted internal events were also no longer persisted, which is the
    desired behavior and required several spec expectation updates.
- Fix:
  - amended routing result persistence to keep events with at least one matched
    route, even when all deliveries are skipped;
  - kept truly unrouted events unpersisted;
  - updated outage, DNS transfer, and transaction-chain supervisor specs to
    expect no event rows for unconfigured/unrouted notifications.
- Local verification after the fix:
  - `nix develop .#api -c bundle exec rspec --format progress
    spec/models/transaction_chains/migration_plan/mail_spec.rb
    spec/models/transaction_chains/vps/oom_prevention_spec.rb
    spec/models/transaction_chains/vps/replace/os_spec.rb
    spec/models/security_advisory_spec.rb
    spec/models/transaction_chains/plugins/requests/create_spec.rb
    spec/models/transaction_chains/plugins/outage_reports/update_spec.rb
    spec/supervisor/node/dns_transfer_log_spec.rb
    spec/supervisor/node/transaction_chain_events_spec.rb`: 37 examples,
    0 failures.
  - `git diff --check` passed.
  - `nix develop .#api -c ruby -c lib/vpsadmin/api/events.rb`: syntax OK.
  - `nix develop .#api -c bundle exec rubocop
    lib/vpsadmin/api/events.rb
    spec/models/transaction_chains/plugins/outage_reports/update_spec.rb
    spec/supervisor/node/dns_transfer_log_spec.rb
    spec/supervisor/node/transaction_chain_events_spec.rb`: 4 files
    inspected, no offenses.
- Amended the feature commit to `886e8ef8e49cccacf754737e3a9f859b55215feb`.
  Overcommit hooks passed during amend:
  `MigrationSpecs`, `Nixfmt`, `PhpCsFixer`, `RuboCop`, and commit-message
  hooks, with only the pre-existing non-blocking 72-column warning.
- Force-pushed the amended head with
  `nix develop . -c git push --force-with-lease origin
  2026-06-15-vpsadmin-events`.
- Cancelled superseded old-head aggregate `CI` run `28335027608`.
- Watching current-head GitHub Actions for
  `886e8ef8e49cccacf754737e3a9f859b55215feb`:
  - `API Migration Specs` `28335592358`
  - `API Specs (topic parallel)` `28335592364`
  - `CI` `28335592345`
  - `RuboCop` `28335592372`
  - `Webui PHPUnit` `28335592365`
  - `libnodectld Specs` `28335592375`

Second GitHub CI pass:

- Current-head run `886e8ef8e49cccacf754737e3a9f859b55215feb` results:
  - success: `API Migration Specs` `28335592358`, `RuboCop` `28335592372`,
    `Webui PHPUnit` `28335592365`, `libnodectld Specs` `28335592375`;
  - failure: `API Specs (topic parallel)` `28335592364`;
  - aggregate `CI` `28335592345` was still active after the branch was
    superseded.
- Inspected completed failed job `API specs (core) - engine`
  `83941137211` via
  `gh api /repos/vpsfreecz/vpsadmin/actions/jobs/83941137211/logs`.
- Failure root cause:
  - additional specs still expected matched muted/skipped routes to leave no
    persisted event;
  - the intended behavior is that truly unrouted events disappear, while
    matched routes with only skipped deliveries persist as suppressed events
    with route-match and skipped-delivery audit data.
- Fix:
  - added `expect_suppressed_event!` test helper;
  - updated event-route, expiration-warning, OOM-report, incident-report, and
    failed-login specs to expect persisted suppressed events for muted or
    skipped-but-matched routes;
  - adjusted route hit-count expectation for a matched mute receiver.
- Local verification after the fix:
  - `nix develop .#api -c bundle exec rspec --format progress
    spec/models/event_route_spec.rb
    spec/models/transaction_chains/lifetimes/expiration_warning_spec.rb
    spec/models/transaction_chains/vps/oom_reports_spec.rb
    spec/models/transaction_chains/incident_report/send_spec.rb
    spec/models/transaction_chains/user/report_failed_logins_spec.rb`:
    44 examples, 0 failures.
  - `git diff --check` passed.
  - `nix develop .#api -c ruby -c ...`: syntax OK for the six changed spec
    files.
  - `nix develop .#api -c bundle exec rubocop ...`: 6 files inspected,
    no offenses.
- Amended the feature commit to `a6e9e0a6dac37dd9a36774c981737e53ce74a769`.
  Overcommit hooks passed during amend:
  `Nixfmt`, `MigrationSpecs`, `RuboCop`, `PhpCsFixer`, and commit-message
  hooks, with only the pre-existing non-blocking 72-column warning.
- Force-pushed the amended head with
  `nix develop . -c git push --force-with-lease origin
  2026-06-15-vpsadmin-events`.
- Cancelled superseded old-head aggregate `CI` run `28335592345`.
- Watching current-head GitHub Actions for
  `a6e9e0a6dac37dd9a36774c981737e53ce74a769`:
  - `API Migration Specs` `28336053242`
  - `API Specs (topic parallel)` `28336053258`
  - `CI` `28336053231`
  - `RuboCop` `28336053237`
  - `Webui PHPUnit` `28336053246`
  - `libnodectld Specs` `28336053227`

Third GitHub CI pass:

- Current-head run `a6e9e0a6dac37dd9a36774c981737e53ce74a769` results:
  - success: `API Migration Specs` `28336053242`, `RuboCop` `28336053237`,
    `Webui PHPUnit` `28336053246`, `libnodectld Specs` `28336053227`;
  - failure: `API Specs (topic parallel)` `28336053258`;
  - aggregate `CI` `28336053231` was still active after the branch was
    superseded.
- Inspected failed platform jobs:
  - `API specs (core) - platform` `83942347580`;
  - `API specs (full) - platform` `83942347609`.
- Failure root cause:
  - two `event_routing_spec` examples still expected disabled delivery-method
    routes to leave no persisted event;
  - disabled delivery methods are matched routes with skipped deliveries, so
    they should persist as suppressed events.
- Fix:
  - updated lazy default e-mail and existing receiver-target delivery-method
    disabled API resource specs to expect persisted suppressed events,
    skipped deliveries, route matches, and the `delivery method is disabled`
    skip reason.
- Local verification after the fix:
  - `nix develop .#api -c bundle exec rspec --format progress
    spec/api/resources/event_routing_spec.rb:1118
    spec/api/resources/event_routing_spec.rb:1136`: 1 example, 0 failures
    after one line-number filter shifted.
  - `nix develop .#api -c bundle exec rspec --format progress
    spec/api/resources/event_routing_spec.rb -e
    'skips lazy default e-mail actions when the delivery method is disabled'
    -e 'skips existing receiver targets when their delivery method is
    disabled'`: 2 examples, 0 failures.
  - `nix develop .#api -c bundle exec rspec --format progress
    spec/api/resources/event_routing_spec.rb`: 43 examples, 0 failures,
    1 expected pending.
  - `git diff --check` passed.
  - `nix develop .#api -c ruby -c spec/api/resources/event_routing_spec.rb`:
    syntax OK.
  - `nix develop .#api -c bundle exec rubocop
    spec/api/resources/event_routing_spec.rb`: 1 file inspected,
    no offenses.
- Amended the feature commit to `ce17e0fcf70886e84159000cae2afc8423743c3c`.
  Overcommit hooks passed during amend:
  `MigrationSpecs`, `Nixfmt`, `RuboCop`, `PhpCsFixer`, and commit-message
  hooks, with only the pre-existing non-blocking 72-column warning.
- Force-pushed the amended head with
  `nix develop . -c git push --force-with-lease origin
  2026-06-15-vpsadmin-events`.
- Cancelled superseded old-head aggregate `CI` run `28336053231`.
- Watching current-head GitHub Actions for
  `ce17e0fcf70886e84159000cae2afc8423743c3c`:
  - `API Migration Specs` `28336525862`
  - `API Specs (topic parallel)` `28336525874`
  - `CI` `28336525865`
  - `RuboCop` `28336525863`
  - `Webui PHPUnit` `28336525866`
  - `libnodectld Specs` `28336525861`

Fourth GitHub CI pass:

- Current-head run `ce17e0fcf70886e84159000cae2afc8423743c3c` results:
  - success: `API Migration Specs` `28336525862`,
    `API Specs (topic parallel)` `28336525874`, `RuboCop` `28336525863`,
    `Webui PHPUnit` `28336525866`, `libnodectld Specs` `28336525861`;
  - failure: aggregate `CI` `28336525865`.
- Downloaded aggregate test artifacts with
  `gh run download --repo vpsfreecz/vpsadmin 28336525865 --dir
  /tmp/vpsadmin-ci-28336525865-artifacts`.
- Failure root cause:
  - `alerts/notification-routing` still expected webhook delivery payloads and
    local helper rows to use `receiver_action`;
  - `webui#misc-pages` still expected the old reminder title and flash text;
  - `webui#support-pages` still used the removed receiver-action flow instead
    of notification targets, and delivery tables still expected the old
    `Receiver action` column;
  - `admin/cluster-resource-package-assignment` failed before test logic while
    evaluating a Nix store path for `unit-dhcpcd.service`; this appears
    unrelated to the notification changes and is being left to the rerun for
    confirmation.
- Fix:
  - updated notification-routing test helpers and webhook assertions to use
    `receiver_target` and `notification_receiver_target_id`;
  - updated misc page expectations for the new notification reminder wording;
  - rewrote the support-page notification flow to create/edit targets, assert
    target links and event filters, and expect delivery queue/log `Target`
    columns.
- Local verification after the fix:
  - `nix develop . -c ./test-runner.sh test alerts/notification-routing`:
    1 test successful.
  - `nix develop . -c ./test-runner.sh test 'webui#misc-pages'`:
    1 test successful.
  - `nix develop . -c ./test-runner.sh test 'webui#support-pages'`:
    1 test successful.
  - `nix develop . -c nix-instantiate --parse
    tests/suite/alerts/notification-routing.nix >/dev/null`: passed.
  - `nix shell nixpkgs#nodejs -c node --check
    tests/playwright/webui/specs/misc-pages.spec.cjs`: passed.
  - `nix shell nixpkgs#nodejs -c node --check
    tests/playwright/webui/specs/support-pages.spec.cjs`: passed.
  - `git diff --check` passed.
- Amended the feature commit to `93cd5961357db68b35de35202f54d85bb1d899eb`.
  Overcommit hooks passed during amend:
  `MigrationSpecs`, `Nixfmt`, `RuboCop`, `PhpCsFixer`, and commit-message
  hooks, with only the pre-existing non-blocking 72-column warning.
- Force-pushed the amended head with
  `nix develop . -c git push --force-with-lease origin
  2026-06-15-vpsadmin-events`.
- No superseded old-head runs were active after the force-push.
- Watching current-head GitHub Actions for
  `93cd5961357db68b35de35202f54d85bb1d899eb`:
  - `API Migration Specs` `28346347318`
  - `API Specs (topic parallel)` `28346347329`
  - `CI` `28346347307`
  - `RuboCop` `28346347323`
  - `Webui PHPUnit` `28346347315`
  - `libnodectld Specs` `28346347326`
- Individual workflow status for
  `93cd5961357db68b35de35202f54d85bb1d899eb`:
  - success: `API Migration Specs` `28346347318`,
    `API Specs (topic parallel)` `28346347329`, `RuboCop` `28346347323`,
    `Webui PHPUnit` `28346347315`, `libnodectld Specs` `28346347326`.
  - success: aggregate `CI` `28346347307`; selected ci-tagged tests job
    `83970323505` completed successfully in 14m55s.

## Telegram HTML notification template slice

Final commits prepared on 2026-06-29:

- `vpsadmin`:
  `1e3e3bd6c17bb37f01be995e720116ff55d8af42`
  (`notifications: render Telegram HTML templates`).
- `vpsfree-mail-templates`:
  `e62e9eba228a6e95314349f10470f562cc7c843c`
  (`telegram: add HTML notification templates`).
- `vpsfree-cz-configuration`:
  `b708d7fd7956d7138381ac624b5ff01abf55f69b`
  (`inputs: set vpsadminServices to 1e3e3bd6`).

Implementation notes:

- Telegram text templates remain required. HTML templates are optional and are
  used only by the new vpsAdmin sender when present and within Telegram's
  message length limit.
- New Telegram payloads can carry `parse_mode: HTML` and disabled
  `link_preview_options`; old queued JSON payloads with only `chat_id` and
  `text` remain accepted.
- Template helpers escape labels/URLs before producing Telegram HTML links.
- Telegram and SMS template lookup now fall back to the event's e-mail
  delivery context when a protocol-specific context is not declared. This is
  required for ordinary default routes, because most event declarations map
  templates under `deliver :email`.
- External template HTML bodies use old-compatible renderer pieces
  (`webui_url` and `ERB::Util.html_escape`), so installing the templates before
  the new sender code is not expected to break older vpsAdmin versions.
- The configuration pin was updated through `confctl`. An intermediate local
  generated pin was folded away before push, leaving a single generated-style
  update for the `vpsadminServices` input from `936b9e26` to `1e3e3bd6`.

Quick verification:

- `vpsfree-mail-templates`:
  `nix develop -c bundle exec rake check` passed and reported
  `Checked 652 template files`.
- `vpsadmin`:
  `nix develop .#api -c bundle exec rspec --format progress
  spec/models/notification_templates_spec.rb
  spec/models/tasks/event_delivery_spec.rb` passed with 87 examples and
  0 failures after the default Telegram template mapping fix.
- `vpsadmin`:
  `nix develop ..#api -c bundle exec rubocop
  models/notification_template_variant.rb
  lib/vpsadmin/api/events.rb
  lib/vpsadmin/api/notifications.rb
  spec/models/notification_templates_spec.rb
  spec/models/tasks/event_delivery_spec.rb` passed with 5 files inspected and
  no offenses.
- `vpsadmin`: targeted Telegram examples
  `spec/models/tasks/event_delivery_spec.rb:1220`,
  `spec/models/tasks/event_delivery_spec.rb:1251`, and
  `spec/models/tasks/event_delivery_spec.rb:1278` passed with 3 examples and
  0 failures after the default template mapping fix.
- `vpsadmin`: `git diff --check` passed.
- `vpsadmin`: Overcommit hooks passed during commit/amend.
- `vpsfree-cz-configuration`: `confctl` commit hooks passed with Nixfmt OK.
  The generated commit message triggered only the accepted text-width warning.

Push and CI state:

- Force-pushed `vpsadmin` from superseded head `ac941458` to
  `07ec2978c360b0b05bd5b416694146d7ff0cb956`, then to the final fixed head
  `1e3e3bd6c17bb37f01be995e720116ff55d8af42`.
- Pushed `vpsfree-mail-templates` head
  `e62e9eba228a6e95314349f10470f562cc7c843c`.
- Pushed `vpsfree-cz-configuration` head
  `d20c9d81a0ab2034913d6b6b4f48d2e8e7068a6b`, then force-pushed the final
  single-pin commit
  `b708d7fd7956d7138381ac624b5ff01abf55f69b`.
- Cancelled stale old-head vpsAdmin aggregate CI runs `28357855586` and
  `28358744272`.
- Current-head vpsAdmin GitHub Actions for `1e3e3bd6` were in progress when
  this checkpoint was updated:
  - aggregate `CI` `28359952197`;
  - `API Specs (topic parallel)` `28359952215`;
  - `RuboCop` `28359952211` completed successfully.

Mandatory review:

- First standalone review found no blockers. It raised one important test gap:
  the Telegram HTML dispatch spec cleared the stored JSON payload and therefore
  tested recomputation, not normal queued payload preservation.
- Fixed by amending the vpsAdmin commit so the spec leaves persisted JSON
  intact and asserts that `parse_mode` and disabled link previews survive
  dispatch.
- A fresh standalone review of the post-test-fix heads found one blocking
  issue: ordinary default Telegram routes still missed HTML templates because
  they had no protocol-specific `deliver :telegram` mapping and the fallback
  lookup did not actually reach the e-mail delivery context.
- Fixed by making missing delivery definitions return `nil`, adding Telegram
  to the SMS-style e-mail-template fallback path, and adding a regression for a
  default `user.suspended` Telegram route that sends the `user_suspend` HTML
  template without an explicit route template override.
- The same review also noted that the squashed config commit body described an
  intermediate pin range. Fixed by replacing the config history with one
  generated-style pin commit describing `936b9e26 -> 1e3e3bd6`.
- The review packet initially had a typo in the full
  `vpsfree-cz-configuration` base hash; it was corrected to
  `45410d75ae319a0ea5b5eb2f24ea01cbc4e572d7`.
- Narrow follow-up check with the same reviewer confirmed that the blocking
  default Telegram template-path issue and the config-message advisory are
  fixed. The reviewer found no new blocking, important, or advisory issues in
  the incremental fix. Remaining deployment checks are live Telegram behavior
  and confirming that the dev-cluster `webui/base_url` used in links is
  absolute.

Dev-cluster deployment:

- Pending after the clean follow-up review.

### Telegram HTML deployment follow-up

- Deployed the previously reviewed heads to the running dev cluster with
  `dev-clusters/vpsadmin/bin/devcluster update
  2026-06-15-vpsadmin-events services`.
- Post-switch checks showed no failed systemd units and all notification
  dispatcher/receiver services active.
- Database verification then showed that the deployed template package
  contained 128 `telegram/*.html.erb` files, but existing Telegram template
  variants still had empty `html` columns:
  `protocol=1 count=49 html_count=0`.
- Root cause: the built-in API installer intentionally skipped existing
  variants. That preserved customized text, but also prevented newly packaged
  HTML bodies from reaching already-initialized clusters.
- Implemented a conservative backfill in `vpsadmin`:
  `VpsAdmin::API::NotificationTemplates.install_defaults!` now updates only
  the `html` field of an existing variant when it is blank and the packaged
  template has an HTML body. Existing text, subject, sender metadata, options,
  and template labels remain unchanged.
- Added a regression spec proving existing custom Telegram text is preserved
  while missing HTML is filled.
- Updated installer docs and the NixOS database-setup option text to describe
  the missing-HTML exception.

Follow-up commits:

- `vpsadmin` amended from `1e3e3bd6c17bb37f01be995e720116ff55d8af42` to
  `356bd2d00ecb989c24baabc21e930cb4a0d44851`, then to
  `0864f254f993b627b83e1d138f4c3a0e25eab034`
  (`notifications: render Telegram HTML templates`).
- `vpsfree-cz-configuration` generated a new `confctl` pin commit
  `7881a974c4d3a1e674612db48cec1924c915f711`
  (`inputs: set vpsadminServices to 356bd2d0`), then replaced that unpushed
  generated commit with
  `7b2733b122125d56568724fec9bfa48ad5657cdf`
  (`inputs: set vpsadminServices to 0864f254`).
- Direct `confctl inputs channel set --commit vpsadmin vpsadmin
  356bd2d00ecb989c24baabc21e930cb4a0d44851` failed because Nix's direct
  `github:` SHA tarball fetch returned HTTP 400 from GitHub. Re-running
  `confctl` with the feature branch name
  `2026-06-15-vpsadmin-events` succeeded; the resulting `flake.lock` records
  the exact resolved revision
  `356bd2d00ecb989c24baabc21e930cb4a0d44851` and nar hash
  `sha256-76RBs696tp7e8lHM62oq1q0BiTc28jtiGnyWw3yxeWk=`.
- The same GitHub codeload issue repeated after the final vpsAdmin amend.
  `nix flake metadata github:vpsfreecz/vpsadmin/2026-06-15-vpsadmin-events`
  resolved and cached the branch at
  `0864f254f993b627b83e1d138f4c3a0e25eab034`; a subsequent `confctl` retry
  succeeded. Final `flake.lock` records nar hash
  `sha256-tdLEi1HoKBATy4MVTAqy8X5CqYl6IFMWWL0wOr8QacE=`.

Follow-up verification:

- `nix develop .#api -c bundle exec rspec --format documentation
  spec/models/notification_templates_spec.rb`: 11 examples, 0 failures.
- `nix develop ..#api -c bundle exec rubocop
  lib/vpsadmin/api/notification_templates.rb
  lib/vpsadmin/api/tasks/vpsadmin.rake
  spec/models/notification_templates_spec.rb`: no offenses.
- `git diff --check`: passed.
- vpsAdmin root-shell amend ran Overcommit hooks successfully:
  `Nixfmt`, `MigrationSpecs`, `RuboCop`, and commit-message hooks; only
  non-blocking text-width warnings were reported.
- `nix develop .#api -c bundle exec rspec --format progress
  spec/models/notification_templates_spec.rb
  spec/models/tasks/event_delivery_spec.rb`: 88 examples, 0 failures.
- After the reviewer finding was fixed:
  `nix develop .#api -c bundle exec rspec --format documentation
  spec/models/notification_templates_spec.rb`: 13 examples, 0 failures.
- After the reviewer finding was fixed:
  `nix develop ..#api -c bundle exec rubocop
  lib/vpsadmin/api/notification_templates.rb
  lib/vpsadmin/api/tasks/vpsadmin.rake
  spec/models/notification_templates_spec.rb`: no offenses.
- After the reviewer finding was fixed: `git diff --check` passed.
- After the reviewer finding was fixed:
  `nix develop .#api -c bundle exec rspec --format progress
  spec/models/notification_templates_spec.rb
  spec/models/tasks/event_delivery_spec.rb`: 90 examples, 0 failures.
- `vpsfree-cz-configuration` `confctl` pin commit ran the Nixfmt hook
  successfully; the generated commit message produced only the accepted
  text-width warning.

Follow-up mandatory review:

- Launched standalone reviewer `Newton`
  (`019f12ae-4acd-7763-8665-b28d30c1ce29`) for the incremental
  `vpsadmin` and `vpsfree-cz-configuration` changes before redeploying.
- Newton found an important issue in the first follow-up: backfilling HTML into
  a customized Telegram text variant would make delivery prefer packaged HTML
  over the customized text. Newton also noted that the backfill was broader
  than needed because it applied to all protocols.
- Fixed by narrowing the backfill to Telegram variants whose existing text
  still exactly matches the packaged text. Added specs that matching packaged
  Telegram text is backfilled, customized Telegram text is not backfilled, and
  existing e-mail variants are not backfilled.
- Sent the narrowed fix back to Newton for a focused follow-up check.
- Newton's focused follow-up check found no new blocking, important, or
  advisory findings. The prior important finding and advisory finding are
  resolved. Remaining checks are live Telegram behavior and post-redeploy
  DB/service verification.

### Final Telegram HTML deployment

- Added one more `vpsfree-mail-templates` commit after live DB verification
  revealed six generic fallback Telegram variants without HTML:
  `32e0b4098eae78470ee9a309535bd2bb3e111c5d`
  (`telegram: add fallback event templates`).
- The six added fallback directories are:
  `outage_report_generic`, `outage_report_user`, `request_create_admin`,
  `request_resolve_user`, `request_update_admin`, and
  `request_update_user`.
- `vpsfree-mail-templates` quick verification:
  `nix develop -c bundle exec rake check`: passed,
  `Checked 664 template files`.
- `git diff --check e62e9eba228a6e95314349f10470f562cc7c843c..HEAD`:
  passed.
- Follow-up mandatory review with standalone reviewer `Leibniz`
  (`019f12d1-6ffa-7783-96ec-563215139aaa`) found no blocking or important
  issues. It reported one advisory commit-message line-length issue, which was
  fixed by amending the commit before push.
- Pushed `vpsfree-mail-templates` branch
  `2026-06-15-vpsadmin-events` at
  `32e0b4098eae78470ee9a309535bd2bb3e111c5d`.
- GitHub Actions check for `vpsfree-mail-templates` returned no runs for this
  branch.

Running dev-cluster deployment:

- The services VM already had the final vpsAdmin code deployed via
  `vpsfree-cz-configuration` commit
  `7b2733b122125d56568724fec9bfa48ad5657cdf`, which pins
  `vpsadminServices` to
  `0864f254f993b627b83e1d138f4c3a0e25eab034`.
- The dev-cluster seed unit in the active VM did not include the local
  `install_notification_templates_from` helper even though the local
  `dev-clusters/vpsadmin/nix/test.nix` contains it, so template loading was
  performed directly through the deployed ActiveRecord installer.
- First live import used the deployed Nix-store template package
  `/nix/store/3zynhy1dydd1k2mn3fkwpa55zsl8hz9a-vpsfree-mail-templates`
  and reported:
  `{templates_created: 7, variants_created: 112, variants_updated: 43}`.
- After adding the six fallback directories, copied the updated template tree
  from the worktree to `/tmp/vpsfree-mail-templates-new` on the services VM
  and reran
  `VpsAdmin::API::NotificationTemplates.install_defaults!(paths: [path])`.
  The second import reported:
  `{templates_created: 0, variants_created: 0, variants_updated: 6}`.
- Final DB coverage:
  - e-mail protocol `0`: `count=98`, `html_count=3`;
  - Telegram protocol `1`: `count=98`, `html_count=98`;
  - SMS protocol `2`: `count=98`, `html_count=0`.
- A sample query confirmed HTML bodies were present for
  `outage_report_generic`, `request_create_admin`, and
  `request_resolve_user`, including escaped subject/summary ERB and WebUI link
  markup.
- `systemctl is-active` for `vpsadmin-api.service`,
  `vpsadmin-notification-dispatcher-telegram.service`,
  `vpsadmin-telegram-receiver.service`,
  `vpsadmin-notification-dispatcher-email.service`,
  `vpsadmin-notification-dispatcher-sms.service`, and
  `vpsadmin-notification-dispatcher-webhook.service`: all `active`.
- `systemctl --failed --no-pager`: initially showed a transient
  `vpsadmin-api-payments-process.service` failure from the timer while the
  deployed API package was being refreshed. The task was available in the
  current package, rerunning `systemctl start
  vpsadmin-api-payments-process.service` succeeded, and the final
  `systemctl --failed --no-pager` returned `0 loaded units listed`.
- Dev cluster status remained running and ready on the bridge network.

GitHub Actions after final pushes:

- `vpsadmin` current head
  `0864f254f993b627b83e1d138f4c3a0e25eab034`:
  `RuboCop` run `28362326803` succeeded and
  `API Specs (topic parallel)` run `28362326754` succeeded.
  Aggregate `CI` run `28362326775` was still in progress in the
  `Run tests` step when this checkpoint was recorded.
- `vpsfree-cz-configuration` returned no runs for this branch.

### Rich Telegram VPS template follow-up

- User tested `vps.resources_changed` in the dev cluster and saw plain/generic
  content without limits. New requested outcome:
  - Telegram VPS templates should be richer, closer to the e-mail details;
  - all VPS-related Telegram notifications should put hostname/ID in the
    header;
  - `vps_resources_change` must include CPU, CPU limit, memory, swap, an
    explicit `Reason:`, changed-by admin, and a vpsAdmin object link;
  - link labels should be `Link: open in vpsAdmin` / localized Czech
    equivalent instead of `Open: event detail`.
- Current local edits:
  - `vpsadmin` generic Telegram fallback now puts VPS hostname/ID in the
    header, links to the VPS detail page when possible, and uses
    `Link: open in vpsAdmin`.
  - `vpsfree-mail-templates` generic Telegram skeletons now use VPS-in-header
    when `@event.vps` exists, link to the VPS object when available, and no
    longer use the old `Open: event detail` wording.
  - Rich Telegram HTML/text bodies were added for core VPS templates including
    resource changes, suspend/resume, network changes, DNS resolver changes,
    dataset expansion/quota notices, migrations, replacement, OOM reports and
    prevention, incident reports, and rescue-mode alerts.
- Quick verification:
  - `nix develop -c bundle exec rake check` in `vpsfree-mail-templates`:
    passed, `Checked 664 template files`.
  - `rg -n "Open:|event detail|Otevrit|detail udalosti"
    templates/*/telegram`: no matches.
  - standalone ERB preview of
    `templates/vps_resources_change/telegram/en.{html,text}.erb` confirmed
    hostname, CPU, CPU limit, memory, swap, `Reason:`, changed-by, and
    vpsAdmin link are rendered.
  - `nix develop .#api -c bundle exec rspec --format documentation
    spec/models/tasks/event_delivery_spec.rb`: 78 examples, 0 failures.
  - `nix develop .#api -c bundle exec rubocop
    lib/vpsadmin/api/notifications.rb
    spec/models/tasks/event_delivery_spec.rb`: no offenses.
  - `git diff --check` passed in both `vpsadmin` and
    `vpsfree-mail-templates`.
- Commits created:
  - `vpsadmin` `8b9aa01fa2507a4934adf84325bd6359ff1a1b58`
    (`notifications: improve generic Telegram links`);
  - `vpsfree-mail-templates`
    `c6fb85eba436ee2ad322644818ec2d888af4794c`
    (`telegram: enrich VPS notifications`).
- Mandatory review:
  - standalone reviewer `Dirac`
    (`019f135f-1ab6-7093-ac4f-6ccd23680c50`) reviewed the committed slice;
  - no blocking, important, or advisory findings;
  - residual risk noted by reviewer: stale installed templates in the dev
    cluster until the template import/update step is performed.
- Pushed after review:
  - `vpsadmin` branch `2026-06-15-vpsadmin-events` at `8b9aa01f`;
  - `vpsfree-mail-templates` branch `2026-06-15-vpsadmin-events` at
    `c6fb85e`;
  - `vpsfree-cz-configuration` branch `2026-06-15-vpsadmin-events` at
    `432783c5` (`inputs: set vpsadminServices to 8b9aa01f`).
- GitHub Actions:
  - new vpsAdmin runs started for head `8b9aa01f`;
  - superseded old `CI` run `28370519222` on head `d573b6a2` was cancelled;
  - `vpsfree-mail-templates` reported no workflow runs for this branch.
  - later check: vpsAdmin `CI`, `API Specs (topic parallel)`, and `RuboCop`
    all completed successfully for head `8b9aa01f`; `vpsfree-mail-templates`
    still reported no workflow runs for this branch.
- Dev-cluster deployment for the rich Telegram follow-up:
  - `dev-clusters/vpsadmin/bin/devcluster update
    2026-06-15-vpsadmin-events services` switched the services VM to the
    `vpsadminServices` pin at `8b9aa01f` and copied the updated
    `vpsfree-mail-templates` closure.
  - The normal seed/import path was not enough for this follow-up because
    `NotificationTemplates.install_defaults!` only backfills missing Telegram
    HTML and intentionally does not overwrite existing variant content.
  - Copied the current `vpsfree-mail-templates/templates` tree to
    `/tmp/vpsfree-mail-templates-rich` on the services VM and ran a
    seed-style ActiveRecord importer that assigns template and variant
    attributes unconditionally.
  - Import result: `templates=54 templates_created=0 variants_created=0
    variants_updated=282`.
  - Live DB verification:
    - `NotificationTemplateVariant.where(protocol: 'telegram')`:
      `count=98`, all `98` have HTML;
    - `vps_resources_change` English Telegram HTML in the DB contains the VPS
      hostname/id header, `Current limits:`, CPU cores/limit, memory, swap,
      explicit `Reason:`, changed-by admin, and `Link: open in vpsAdmin`.
  - Rendered live payload check for `vps.resources_changed` with an existing
    dev VPS produced:
    - `parse_mode: "HTML"`;
    - header `<b>VPS hh (#1): resources changed</b>`;
    - CPU `4 cores, limit 400 %`, memory `8192 MB`, swap `1024 MB`;
    - `Reason: test resize`;
    - `Link: <a href="https://webui.aitherdev.int.vpsfree.cz/?page=adminvps...">open in vpsAdmin</a>`.
  - Services health after deployment:
    - `vpsadmin-api.service`,
      `vpsadmin-notification-dispatcher-telegram.service`, and
      `vpsadmin-telegram-receiver.service` were active;
    - HTTPS `HEAD` checks for the API and WebUI returned HTTP 200;
    - `systemctl --failed --no-pager` on services returned
      `0 loaded units listed`.
  - Cluster status remained `running`, `ready: yes`, topology `single`,
    bridge network.
- Node refresh follow-up:
  - The services update exited non-zero after the services switch because
    `refresh_nodes_after_seed` could not connect to `nodectld` on `node1`.
  - `nodectld` was running but `nodectl status` returned
    `Connection refused - connect(2) for /run/nodectl/nodectld.sock`.
  - `devcluster update 2026-06-15-vpsadmin-events node1` succeeded and moved
    node1 to the new `nodectld` store path, but `nodectld` still hung on
    `get_node_config`.
  - Restarted `vpsadmin-supervisor.service` on services and restarted
    `nodectld` again; the node continued to log repeated
    `request waiting ... command=get_node_config` messages.
  - RabbitMQ accepted the node connection and `vpsadmin-supervisor.service`
    was active. This appears to be a separate node RPC/runtime issue; it did
    not block the Telegram services-side deployment and payload verification.

## Mailer node removal and dev-cluster repair

- 2026-06-29 requested outcome:
  - remove the obsolete vpsAdmin mailer node from the dev cluster and from
    production `vpsfree-cz-configuration`;
  - keep Mailpit only as a mail-capture service for tests/dev;
  - repair the running dev cluster where all node `nodectld` instances stopped
    responding after the previous services update.
- Compatibility/deployment notes:
  - no schema shape or persisted-state format change is introduced by this
    slice, but a data migration deactivates existing `mailer` role nodes;
  - old queued mail transactions and legacy mail transaction classes are left
    loadable for historical records, but new `TransactionChain#mail` calls now
    fail fast and must be converted to event delivery;
  - event-delivery release transactions now choose only fresh active
    transaction-runner nodes, so stale active mailer status rows cannot attract
    notification release work after the host is removed;
  - removing the NixOS mailer host is a config/topology change only; RabbitMQ
    and database allowlists drop the retired `int.vpsadmin1` host;
  - rolling deployment order is API/services first, then config hosts; the
    final `vpsfree-cz-configuration` branch keeps the `vpsadminServices` pin
    update before the host removal commit;
  - rollback to an older vpsAdmin revision would require restoring the mailer
    host config if any old code path still expects node mail delivery.
- Commits created:
  - `vpsadmin` `d8b138c385f7c844e427e28158b80d99ab332cf0`
    (`notifications: retire node mail delivery`), pushed to
    `origin/2026-06-15-vpsadmin-events`;
  - workspace/devcluster `aa01e45d957270bdf764a5e02e26bf7ab5148315`
    (`devcluster: remove vpsAdmin mailer node`);
  - `vpsfree-cz-configuration`
    `c7880d31`
    (`inputs: set vpsadminServices to d8b138c3`), generated by
    `confctl inputs channel set --commit vpsadmin vpsadmin d8b138c3`;
  - `vpsfree-cz-configuration`
    `fcc543a7`
    (`vpsadmin-config: remove mailer host`);
- Quick verification before mandatory review:
  - `nix develop -c nixfmt ...` passed for touched vpsAdmin and
    `vpsfree-cz-configuration` Nix files;
  - `nix develop .#api -c bundle exec rspec
    spec/models/transaction_chain_spec.rb
    spec/models/transaction_chains/mail/daily_report_spec.rb
    spec/models/transaction_chains/mail/vps_dataset_expanded_spec.rb
    spec/models/tasks/mail_spec.rb
    spec/models/tasks/dataset_expansion_spec.rb
    spec/supervisor/node/dataset_expansions_spec.rb`: 45 examples,
    0 failures;
  - `nix develop .#api -c bundle exec rspec
    spec/models/transaction_chains/mail/daily_report_spec.rb`: 6 examples,
    0 failures;
  - `nix develop .#api -c bundle exec rubocop
    models/transaction_chain.rb spec/models/transaction_chain_spec.rb
    spec/models/transaction_chains/mail/daily_report_spec.rb`: no offenses;
  - `nix develop -c bundle exec rubocop
    tests/runner/extensions/vpsadmin_services.rb`: no offenses;
  - `./test-runner.sh ls services-up` and `./test-runner.sh ls 'alerts/*'`
    both evaluated successfully;
  - `git diff --check` passed in the affected repositories/workspace paths;
  - `confctl ls` no longer lists
    `cz.vpsfree/vpsadmin/int.vpsadmin1`;
  - `confctl build -y` succeeded for
    `cz.vpsfree/vpsadmin/int.api1`, `int.api2`, `int.db`,
    `int.rabbitmq1`, `int.rabbitmq2`, and `int.rabbitmq3` after the mailer
    host removal;
  - after the `vpsadminServices` pin bump to `6d0eab84`, `confctl build -y`
    succeeded again for `int.api1` and `int.api2`.
- Mandatory change review result and follow-up:
  - reviewer found a blocker: event-delivery release transactions still used
    `Node.first_available`, so stale active mailer status could strand
    notification release work after the mailer host/container was removed;
  - fixed by adding `Node.first_available_transaction_runner` and using it
    from transaction-chain node selection, with a regression spec where the
    mailer status is fresh and the runner status is older;
  - reviewer found the production config commit order unsafe; rebuilt the
    `vpsfree-cz-configuration` branch so the `vpsadminServices` pin to
    `d8b138c3` precedes host removal;
  - reviewer found stale `data/vpsadmin/containers.nix` placement for
    `vpsadmin1.int.vpsfree.cz`; removed it from the host-removal commit;
  - reviewer requested checking pending legacy mail transactions before host
    removal; the dev cluster has zero waiting `Transactions::Mail::Send`
    transactions and no waiting event-release transaction assigned to a
    mailer node.
- Additional vpsAdmin verification after review fixes:
  - `nix develop .#api -c bundle exec rspec
    spec/models/transaction_chain_spec.rb`: 14 examples, 0 failures;
  - `nix develop .#api -c bundle exec rspec
    spec/migrations/20260629170000_retire_mailer_nodes_spec.rb`:
    2 examples, 0 failures;
  - combined normal and migration spec execution was not valid because the
    migration spec switches to the `_migration` database; keep those commands
    separate;
  - `nix develop .#api -c bundle exec rubocop models/node.rb
    models/transaction_chain.rb spec/models/transaction_chain_spec.rb
    spec/migrations/20260629170000_retire_mailer_nodes_spec.rb
    db/migrate/20260629170000_retire_mailer_nodes.rb`: no offenses;
  - `nix develop -c ruby tools/check_migration_specs.rb --base
    origin/2026-06-15-vpsadmin-events --head HEAD`: passed;
  - broader API slice covering mail/event delivery call sites:
    64 examples, 0 failures.
- Production configuration verification:
  - final pushed order on `origin/2026-06-15-vpsadmin-events` is
    `c7880d31 inputs: set vpsadminServices to d8b138c3` followed by
    `fcc543a7 vpsadmin-config: remove mailer host`;
  - `confctl ls` lists `int.api1`, `int.api2`, `int.db`, and
    `int.rabbitmq1`-`int.rabbitmq3`, with no `int.vpsadmin1`;
  - `rg -n "vpsadmin1|int\.vpsadmin1|common/mailer" cluster
    data/vpsadmin -g '*.nix'` has no matches;
  - `confctl build -y` succeeded for `cz.vpsfree/vpsadmin/int.api1`,
    `int.api2`, `int.db`, `int.rabbitmq1`, `int.rabbitmq2`, and
    `int.rabbitmq3` after the final branch reorder.
- Dev-cluster deployment and repair:
  - direct `nix build --impure ... #cluster-config` succeeded for the running
    dev cluster before deployment;
  - initial `devcluster update 2026-06-15-vpsadmin-events all` failed while
    copying to services because `/nix/store` had zero free blocks and almost
    no free inodes; removed only the incomplete failed-copy `system-path`
    store path and ran `nix-store --gc`, freeing about 214 MiB and 142k
    inodes;
  - retry switched services successfully and removed the obsolete
    `/etc/nixos-containers/mailer.conf`, but RabbitMQ was left with corrupted
    or missing users/vhosts after the disk-full incident;
  - stopped Ruby clients, ran `rabbitmqctl stop_app`, `rabbitmqctl reset`,
    `rabbitmqctl start_app`, removed the RabbitMQ setup marker, and restarted
    `vpsadmin-rabbitmq-setup.service`;
  - RabbitMQ now has `api`, `console`, `notification`, `supervisor`,
    `dev-node1.lab`, `dev-dns-primary.lab`, and `dev-dns-secondary.lab`
    users, with no mailer user;
  - restarted API, supervisor, console router, notification dispatchers,
    Telegram receiver, Mailpit, RabbitMQ, MySQL, and nginx; all are active;
  - updated node1, `dns-primary`, and `dns-secondary`, then ran
    `devcluster refresh 2026-06-15-vpsadmin-events`; node1 and both DNS
    nodes answer `nodectl ping` and report `State: running`;
  - `nixos-container list` on services shows only `webui`; the mailer
    container is gone;
  - RabbitMQ queues contain node/DNS queues and notification queues only,
    with no mailer queues and no queued messages;
  - deployed DB check: schema version `20260629170000`, old
    `vpsadmin-mailer` node row is inactive, active mailer node count is 0,
    waiting legacy mail-send transaction count is 0, and no waiting event
    release is assigned to a mailer node;
  - transaction chain 15 was still queued on the removed mailer through an
    initial `Transactions::Utils::NoOp` transaction. Updating only the
    relational `transactions.node_id` to `dev-node1` caused nodectld to reject
    it because the signed `transactions.input` payload still contained
    `node: 100`; nodectld failed the chain with `Signed options do not match
    relational options`. The chain is intentionally left failed after operator
    confirmation that this is acceptable;
  - HTTP smoke checks passed: Mailpit API returned JSON, API HTTP returned
    200, and nginx HTTPS API route returned 200.
  - Telegram template sanity check: deployed DB has Telegram HTML variants for
    `vps_resources_change`; the English variant contains current limits,
    `Reason:`, and `Link:` markers, while the other language is localized.
- GitHub Actions and push checkpoint:
  - workspace/devcluster branch was pushed to
    `aither64/vpsfree-cz-workspace` branch
    `2026-06-15-vpsadmin-events` at `aa01e45`;
  - `vpsfree-cz-configuration` branch is pushed at `fcc543a7`; GitHub reports
    no workflow runs for this branch;
  - current-head vpsAdmin runs for `d8b138c3` are green for `RuboCop`,
    `API Migration Specs`, `libnodectld Specs`, and
    `API Specs (topic parallel)`;
  - current-head vpsAdmin aggregate `CI` run `28383215524` is still
    in progress, specifically in the selected integration test step;
  - superseded aggregate `CI` run `28381104043` for old head `6d0eab84` was
    requested for cancellation;
  - unrelated dirty `AGENTS.md` and untracked historical notes/work
    directories were not staged or modified.
- Telegram object-link follow-up:
  - added default Telegram HTML rendering for directory-backed templates
    through `telegram_notification_html`, leaving the text templates as
    fallback content;
  - added template-builder helpers that link the primary object in the title
    and footer when a WebUI base URL is configured; VPS notifications use the
    human-friendly `hostname (#id)` label and link to VPS details;
  - resource-change Telegram HTML now includes changed-by, current CPU, CPU
    limit, memory, swap, explicit `Reason:`, and `Link: VPS details`;
  - generic Telegram fallback links are labelled `VPS details` or
    `event details`, instead of the ambiguous `open in vpsAdmin`;
  - injected the original notification event separately as
    `notification_event` so templates that use another `event` object, such as
    monitoring alerts, can still link to the delivery event when needed;
  - local validation passed:
    `nix develop .#api -c bundle exec rspec
    spec/models/notification_templates_spec.rb` (14 examples);
  - local validation passed:
    `nix develop .#api -c bundle exec rspec
    spec/models/notification_templates_spec.rb
    spec/models/tasks/event_delivery_spec.rb:1217
    spec/models/tasks/event_delivery_spec.rb:1246
    spec/models/tasks/event_delivery_spec.rb:1270
    spec/models/tasks/event_delivery_spec.rb:1301
    spec/models/tasks/event_delivery_spec.rb:1329
    spec/models/tasks/event_delivery_spec.rb:1353` (20 examples);
  - `nix develop .#api -c bundle exec rubocop
    models/notification_template_variant.rb models/notification_template.rb
    lib/vpsadmin/api/events.rb lib/vpsadmin/api/notification_templates.rb
    lib/vpsadmin/api/notifications.rb spec/models/notification_templates_spec.rb
    spec/models/tasks/event_delivery_spec.rb` passed with no offenses;
  - `git diff --check` passed.
- VPS resource-change CPU-limit follow-up:
  - user clarified that Telegram must match the existing e-mail expression:
    `@vps.cpu_limit || (@vps.cpu * 100)`, not render an unset CPU limit as
    unlimited and not branch defensively around missing `cpu_limit`;
  - `vpsadmin` commit:
    `c70b8874ef462761788dbeee04ac649fb46026f2`
    (`notification_templates: match e-mail CPU limit in Telegram`);
  - `vpsfree-notification-templates` commit:
    `83565d6ebce95fc8d208454e76845af1735c25e7`
    (`vps_resources_change: match e-mail CPU limit in Telegram`);
  - `vpsfree-cz-configuration` confctl-generated commits:
    `f04cd3aa` (`inputs: set vpsfreeNotificationTemplates to 83565d6e`) and
    `1568bdec` (`inputs: set vpsadminServices to c70b8874`);
  - `nix flake metadata --json .` in `vpsfree-cz-configuration` confirmed
    `vpsfreeNotificationTemplates.locked.rev` is
    `83565d6ebce95fc8d208454e76845af1735c25e7` and
    `vpsadminServices.locked.rev` is
    `c70b8874ef462761788dbeee04ac649fb46026f2`;
  - local validation passed:
    `nix develop ..#api -c bundle exec rspec --format documentation
    spec/models/notification_templates_spec.rb` (22 examples);
  - local validation passed:
    `nix develop ..#api -c bundle exec rubocop
    models/notification_template_variant.rb
    spec/models/notification_templates_spec.rb`;
  - template repo validation passed:
    `nix develop -c bundle exec rake check` (664 template files);
  - `git diff --check` passed in `vpsadmin` and
    `vpsfree-notification-templates`;
  - source branches are pushed; configuration commits are local pending final
    build verification;
  - mandatory change review by standalone reviewer `Leibniz` reported no
    blocking, important, or advisory findings; residual notes were that
    `confctl build` for `int.api1`/`int.api2` remained pending and that the
    spec covers nil and explicit nonzero `cpu_limit`, but not explicit zero
    (Ruby's `||` expression would render `0 %` because `0` is truthy).
  - final configuration build verification passed:
    - `nix develop -c confctl build -y cz.vpsfree/vpsadmin/int.api1`
      built generation `2026-06-30--08-59-41`;
    - `nix develop -c confctl build -y cz.vpsfree/vpsadmin/int.api2`
      built generation `2026-06-30--09-01-39`.
  - `vpsfree-cz-configuration` branch was pushed at
    `1568bdec52ddae5e356c521fa554ada74789d21c`;
  - GitHub Actions status after pushing:
    - `vpsadmin` current head `c70b8874` has green RuboCop and
      `API Specs (topic parallel)`;
    - current-head aggregate `CI` run `28425877718` is still in progress in
      `Run selected ci-tagged tests`;
    - previous-head aggregate `CI` run `28404844693` failed one selected
      test, `webui#support-pages`; its uploaded logs show a Playwright
      timeout clicking the `receiver_delete` link at
      `tests/playwright/webui/specs/support-pages.spec.cjs:554` after the
      locator resolved, with 117/118 selected tests passing. No trace/context
      artifacts were included in the uploaded logs. This failure predates the
      CPU-limit follow-up and is in the broader notifications WebUI flow;
    - `vpsfree-notification-templates` and `vpsfree-cz-configuration` report
      no GitHub Actions runs for this branch.

## Final history cleanup checkpoint

- 2026-06-30 requested outcome:
  - rewrite active development branch history into logical commits on top of
    current upstream default branches;
  - remove legacy Telegram HTML template replacement support while preserving
    normal managed-template installation and Telegram HTML rendering;
  - collapse intermediate flake input pin churn in configuration;
  - reset and deploy the resulting vpsAdmin to the dev cluster.
- Branch tips were backed up before any history rewrite:
  - `vpsadmin`:
    `backup/2026-06-15-vpsadmin-events-vpsadmin-before-final-history-cleanup-2026-06-30`
    at `c70b8874ef462761788dbeee04ac649fb46026f2`;
  - `vpsfree-notification-templates`:
    `backup/2026-06-15-vpsadmin-events-templates-before-final-history-cleanup-2026-06-30`
    at `83565d6ebce95fc8d208454e76845af1735c25e7`;
  - `vpsfree-cz-configuration`:
    `backup/2026-06-15-vpsadmin-events-config-before-final-history-cleanup-2026-06-30`
    at `1568bdec52ddae5e356c521fa554ada74789d21c`;
  - `vpsfree-sms-gateway`:
    `backup/2026-06-15-vpsadmin-events-sms-gateway-before-final-history-cleanup-2026-06-30`
    at `3cac063dc8c86402a3ade6e2384dd5334a00c300`.
- Backup refs were pushed to their respective GitHub repositories.
- `vpsadmin` backup push initially failed because the Overcommit hook could
  not load from the ambient shell. Running `nix develop .#vpsadmin -c bundle
  install` refreshed the repo-local gem environment and the backup push then
  succeeded with hooks active.
- `vpsfree-sms-gateway` history was rewritten to three logical commits:
  - `1cbdf180` `sms: add gateway service`;
  - `37f95303` `sms: verify callbacks with HMAC`;
  - `af7b3faf` `sms: add read-only gateway inspection CLI`.
- SMS gateway verification passed:
  - `git diff --check`;
  - commit-message line-length scan of the rewritten messages;
  - `nix develop -c go test ./...`;
  - `nix build .#` (Nix printed an ignored busy eval-cache SQLite warning,
    but exited successfully).
- `vpsfree-notification-templates` history was reset to current
  `origin/master` (`7da522e`) and rewritten to five logical commits:
  - `2f1b43a4` `templates: redesign layout for notification protocols`;
  - `abb2a32d` `templates: add SMS notification variants`;
  - `53ccbee4` `telegram: add HTML notification variants`;
  - `ecacbed6` `telegram: enrich VPS notification variants`;
  - `8e2ad51d` `templates: expose managed notification package`.
- The obsolete intermediate vpsAdmin flake-pin commit was omitted. The final
  tree is identical to the backed-up template branch tip
  `83565d6ebce95fc8d208454e76845af1735c25e7`.
- Template repo verification passed:
  - `git diff --check`;
  - commit-message line-length scan of the rewritten messages;
  - `nix flake check --no-build`;
  - `nix develop -c bundle exec rake check` (664 template files);
  - `nix build .#` (Nix printed an ignored busy eval-cache SQLite warning,
    but exited successfully).
- `vpsadmin` was rebased onto current `origin/master`
  (`1ea40c5f81aea7fda033892b4b0f542c2e0fc8f6`) and rewritten to end at
  `a2a17e092f834307e7ab18bebccd89ac4bc54e97`.
- The two legacy Telegram HTML replacement commits were dropped. The useful
  generic Telegram link rendering behavior was preserved, while the backfill
  logic that identified and replaced legacy packaged HTML by SHA256 or static
  default bodies was removed.
- The final vpsAdmin commit split includes:
  - `5022c9f97` `notifications: render Telegram HTML templates`;
  - `4cefdefb2` `notifications: improve generic Telegram links`;
  - `12875ed6d` `notifications: enrich Telegram template HTML`;
  - `de97a4b2d` `notification_templates: install managed templates from API`;
  - `a2a17e092` `notification_templates: remove legacy Telegram HTML backfill`.
- The redundant vpsAdmin migrations for relaxing notification-template e-mail
  columns and converting notification-action columns to strings were folded
  into the earlier logical migration/schema commits where applicable. The
  final branch no longer carries the deleted migration files.
- vpsAdmin verification passed:
  - `git diff --check`;
  - commit-message line-length scan of rewritten non-generated messages;
  - `nix develop .#vpsadmin -c ruby tools/check_migration_specs.rb --base
    origin/master --head HEAD`;
  - targeted migration specs for the notification/event migration series
    (22 examples, 0 failures);
  - `nix develop .#api -c bundle exec rspec --format documentation
    spec/models/notification_templates_spec.rb` (17 examples, 0 failures);
  - `nix develop .#api -c bundle exec rspec --format documentation
    spec/models/tasks/event_delivery_spec.rb` (81 examples, 0 failures);
  - focused RuboCop over changed API files/specs;
  - `nix develop .#vpsadmin -c nixfmt --check` over changed Nix files.
- Rewritten code branches were force-pushed with leases:
  - `vpsfree-sms-gateway`:
    `3cac063dc8c86402a3ade6e2384dd5334a00c300` ->
    `af7b3fafb780c849ae03e31712128ecb0749ec0b`;
  - `vpsfree-notification-templates`:
    `83565d6ebce95fc8d208454e76845af1735c25e7` ->
    `8e2ad51de9e50b9a5483e6e52bc666c30d2f0b8c`;
  - `vpsadmin`:
    `c70b8874ef462761788dbeee04ac649fb46026f2` ->
    `a2a17e092f834307e7ab18bebccd89ac4bc54e97`.
- `vpsfree-cz-configuration` was reset to current `origin/master`
  (`6e60a75132886a9e5349861ce3f1b125021a037a`) and rewritten to:
  - `e55e4590` `vpsadmin-config: enable Telegram notifications`;
  - `f4ae6b61` `vpsadmin-config: add SMS gateway routing`;
  - `e4973caf` `vpsadmin-config: remove mailer host`;
  - `9093a194` `inputs: set vpsfreeSmsGateway to af7b3faf`;
  - `66081733` `vpsadmin-config: install managed notification templates`;
  - `07255752` `inputs: set vpsfreeNotificationTemplates to 8e2ad51d`;
  - `cd8b00c2` `inputs: set vpsadminServices to a2a17e09`.
- Configuration pin churn was collapsed. `vpsadminProduction` and
  `vpsadminStaging` remain on the upstream default revision
  `f3e1ff0d099d742b72831e881e53c27ee90a337c`; only `vpsadminServices` is
  pinned to the feature branch for dev-cluster/services deployment.
- Configuration quick verification passed:
  - hooks ran through Overcommit for every rewritten config commit;
  - `git diff --check origin/master..HEAD`;
  - `nix flake metadata --no-write-lock-file --json`, confirming
    `vpsadminServices=a2a17e092f834307e7ab18bebccd89ac4bc54e97`,
    `vpsfreeNotificationTemplates=8e2ad51de9e50b9a5483e6e52bc666c30d2f0b8c`,
    and `vpsfreeSmsGateway=af7b3fafb780c849ae03e31712128ecb0749ec0b`.

## Review-fix history cleanup checkpoint

- The mandatory standalone review of the first cleaned history reported
  blocking history-quality issues:
  - `vpsfree-cz-configuration` had not been pushed and was still based on
    old `origin/master` `6e60a751`, while upstream had advanced to
    `aa78a03a`;
  - vpsAdmin migration cleanup was still represented by a final cleanup commit
    instead of being folded into the original logical migration commits;
  - vpsAdmin managed-template installation still bundled independently
    reviewable Telegram rendering, synthetic test delivery, and uploader
    cleanup behavior;
  - the notification-template package commit still bundled Telegram link label
    edits with package/uploader exposure.
- `vpsfree-notification-templates` was rewritten again on
  `origin/master` `7da522e060fc18d5426e1dd6cd305b6847faf5ed`:
  - `2f1b43a` `templates: redesign layout for notification protocols`;
  - `abb2a32` `templates: add SMS notification variants`;
  - `53ccbee` `telegram: add HTML notification variants`;
  - `ecacbed` `telegram: enrich VPS notification variants`;
  - `cfc9928` `telegram: clarify managed link labels`;
  - `e39472a` `templates: expose managed notification package`.
- The template final tree matches the previously reviewed final tree, but the
  132 Telegram label edits are now isolated in `cfc9928` and the package
  exposure/uploader removal is isolated in `e39472a`.
- Template verification after the second rewrite passed:
  - `git diff --check`;
  - commit-message line-length scan;
  - `nix develop -c bundle exec rake check` (664 template files).
- `vpsadmin` was rewritten again on `origin/master`
  `1ea40c5f81aea7fda033892b4b0f542c2e0fc8f6`:
  - the standalone notification-template e-mail nullability migration and
    action-column string conversion migration were removed from the branch
    history and folded into their earlier logical migrations/schema changes;
  - the managed-template installer tail was split into:
    - `9b305d3cf` `notifications: render Telegram HTML templates`;
    - `1a29a9efb` `notifications: improve generic Telegram links`;
    - `c3168de83` `notifications: retire node mail delivery`;
    - `e45b8923c` `notifications: enrich Telegram template HTML`;
    - `a20d3ebeb` `notifications: refine Telegram template rendering`;
    - `2da9cfa5d` `notifications: render test deliveries with generic content`;
    - `94fd280dd` `notification_templates: install managed templates from API`.
- The final vpsAdmin tree matches the previous cleaned final tree. Searches
  for legacy Telegram replacement/backfill markers found no remaining legacy
  HTML support; remaining `Digest::SHA256` usages belong to SMS callback HMAC
  and notification-target identity keys.
- vpsAdmin verification after the second rewrite passed:
  - `git diff --check`;
  - commit-message line-length scan;
  - `nix develop .#vpsadmin -c ruby tools/check_migration_specs.rb --base
    origin/master --head HEAD`;
  - targeted migration specs for the notification/event migration series
    (22 examples, 0 failures);
  - `nix develop .#api -c bundle exec rspec --format documentation
    spec/models/notification_templates_spec.rb` (17 examples, 0 failures);
  - `nix develop .#api -c bundle exec rspec --format documentation
    spec/models/tasks/event_delivery_spec.rb` (81 examples, 0 failures).
- The corrected code branches were force-pushed with leases:
  - `vpsfree-notification-templates`:
    `8e2ad51de9e50b9a5483e6e52bc666c30d2f0b8c` ->
    `e39472a6b9dc0f4acd5b554a4b89496cc3ab4786`;
  - `vpsadmin`:
    `a2a17e092f834307e7ab18bebccd89ac4bc54e97` ->
    `94fd280ddcacff729568c74137e2733e9f4e8ead`.
- Superseded vpsAdmin GitHub Actions run `28432855340` for old head
  `a2a17e092f834307e7ab18bebccd89ac4bc54e97` was requested for
  cancellation. Remaining active vpsAdmin runs are on current head
  `94fd280ddcacff729568c74137e2733e9f4e8ead`.
- `vpsfree-cz-configuration` was rebuilt on current `origin/master`
  `aa78a03a3799069c779f2365bc492216654ab994` and force-pushed with a lease:
  - `13473e63` `vpsadmin-config: enable Telegram notifications`;
  - `5d8306b7` `vpsadmin-config: add SMS gateway routing`;
  - `8e10d4de` `inputs: set vpsfreeSmsGateway to af7b3faf`;
  - `a0569206` `vpsadmin-config: remove mailer host`;
  - `fe065d34` `vpsadmin-config: install managed notification templates`;
  - `9f1a0e07` `inputs: set vpsfreeNotificationTemplates to e39472a6`;
  - `fce712cf` `inputs: set vpsadminServices to 94fd280d`.
- Configuration pin verification passed with
  `nix flake metadata --no-write-lock-file --json`:
  - `vpsadminServices=94fd280ddcacff729568c74137e2733e9f4e8ead`;
  - `vpsfreeNotificationTemplates=e39472a6b9dc0f4acd5b554a4b89496cc3ab4786`;
  - `vpsfreeSmsGateway=af7b3fafb780c849ae03e31712128ecb0749ec0b`;
  - `vpsadminProduction` and `vpsadminStaging` remain on upstream
    `f3e1ff0d099d742b72831e881e53c27ee90a337c`.
- Configuration quick verification after the rebuild passed:
  - Overcommit hooks ran for the hand-written and generated commits;
  - `git diff --check`;
  - generated `confctl` commit messages retained their generated changelog
    lines even where the commit-msg hook warns about text width.
- Fresh mandatory change review was run by standalone reviewer `Herschel`
  after the review-fix rewrites. Result: no blocking, important, or advisory
  findings.
- The reviewer verified the active pushed heads and bases, the repaired
  vpsAdmin tail split, the isolated notification-template Telegram label
  commit, collapsed configuration pin churn, lack of merge/fixup commits, lack
  of deleted standalone migration cleanup files in the vpsAdmin range, and the
  absence of the legacy Telegram SHA/static-body replacement path.
- Residual review notes:
  - full long config builds and dev-cluster deployment were intentionally
    pending until after review;
  - the earlier explicit-zero CPU-limit rendering coverage gap remains a
    residual template test gap, not a history-cleanup finding.
- Final configuration build verification:
  - `nix develop -c confctl build -y cz.vpsfree/vpsadmin/int.api1` built
    generation `2026-06-30--12-04-38`;
  - the first concurrent `int.api2` build also built generation
    `2026-06-30--12-04-38`, but exited non-zero after a confctl log-file
    collision with the parallel `int.api1` build;
  - rerunning `nix develop -c confctl build -y cz.vpsfree/vpsadmin/int.api2`
    alone succeeded and reported generation `2026-06-30--12-04-38`.

## Dev-cluster reset and deployment

- Prepared the vpsAdmin worktree for local dev-cluster builds with
  `nix develop .#vpsadmin -c rake vpsadmin:gems`; the command completed and
  left the repository clean.
- Reset the existing `2026-06-15-vpsadmin-events` dev cluster. The old runner
  did not stop on its own before the helper timeout, so the reset helper killed
  it and removed the saved cluster state.
- Started a fresh dev cluster with bridge networking:
  `dev-clusters/vpsadmin/bin/devcluster start 2026-06-15-vpsadmin-events
  --topology single --network bridge`.
- The cluster is running and ready:
  - pid `3899674`;
  - topology `single`;
  - network `bridge`;
  - ready `yes`.
- Dev-cluster URLs:
  - Web UI: `https://webui.aitherdev.int.vpsfree.cz/`;
  - API: `https://api.aitherdev.int.vpsfree.cz/`;
  - Auth: `https://auth.aitherdev.int.vpsfree.cz/`;
  - Console: `https://console.aitherdev.int.vpsfree.cz/`;
  - Mailpit: `https://mailpit.aitherdev.int.vpsfree.cz/`;
  - Status: `https://status.aitherdev.int.vpsfree.cz/`;
  - Adminer: `https://adminer.aitherdev.int.vpsfree.cz/`.
- Services VM checks passed:
  - no failed systemd units were listed;
  - `vpsadmin-api.service` is active;
  - all notification dispatchers for email, SMS, Telegram, and webhook are
    active;
  - `vpsadmin-telegram-receiver.service` and `vpsfree-sms-gateway.service`
    are active;
  - `vpsadmin-devcluster-seed.service` is inactive with `Result=success`,
    as expected for a completed oneshot seed service.
- HTTP smoke checks passed:
  - API root returned HTTP 200;
  - Web UI returned HTTP 200;
  - Mailpit returned HTTP 401, expected due basic authentication.
- Node VM runtime checks passed:
  - `osctld` supervisor/main processes are running;
  - `nodectld` processes are running;
  - `/run/osctl/osctld.sock` exists.
- Initial database template check after reset:
  - e-mail variants: 49, HTML variants: 0;
  - Telegram variants: 49, HTML variants: 49;
  - SMS variants: 84, HTML variants: 0.
- The initial reset exposed a dev-cluster tooling gap: the workspace helper
  still looked for the old `vpsfree-mail-templates` worktree, even though that
  repository has been renamed to `vpsfree-notification-templates`.
- Fixed dev-cluster tooling so `worktrees/<slug>/vpsfree-notification-templates`
  is copied into the Nix closure and installed through
  `vpsadmin.api.managedNotificationTemplates`.
- Removed the old `vpsfree-mail-templates` compatibility path from the
  dev-cluster wrapper, flake, test module, default config, and README.
- Re-ran
  `dev-clusters/vpsadmin/bin/devcluster update 2026-06-15-vpsadmin-events
  services`; the update copied
  `/nix/store/r4ax0l885dk7g1ly14944b5hg81whw5b-vpsfree-notification-templates`
  to the services VM and switched the services system.
- Post-update verification:
  - `vpsadmin-api.service`, `vpsadmin-database-setup.service`,
    `vpsadmin-notification-dispatcher-telegram.service`, and
    `vpsfree-sms-gateway.service` are active;
  - API logs show `Installing managed notification templates`, followed by
    `Created 220 variants, updated 92 variants`; a later restart reported
    `Managed notification templates are already installed`;
  - `sysconfig` contains `notifications.managed_templates_source_id` with
    value
    `"devcluster:/nix/store/r4ax0l885dk7g1ly14944b5hg81whw5b-vpsfree-notification-templates"`;
  - e-mail variants: 134, HTML variants: 22;
  - Telegram variants: 134, HTML variants: 134;
  - SMS variants: 134, HTML variants: 0.
- Dev-cluster tooling commit was pushed to the workspace repository:
  `c40d7f6` `devcluster: install notification template worktrees`.
- Final post-update checks:
  - `devcluster status 2026-06-15-vpsadmin-events` reports running, topology
    `single`, network `bridge`, ready `yes`;
  - API root returned HTTP 200;
  - Web UI returned HTTP 200.
- GitHub Actions for current vpsAdmin head
  `94fd280ddcacff729568c74137e2733e9f4e8ead`:
  - API Migration Specs: success;
  - Webui PHPUnit: success;
  - RuboCop: success;
  - libnodectld Specs: success;
  - API Specs (topic parallel): success;
  - CI integration workflow `28435263743`: still in progress, running
    selected ci-tagged tests.

## 2026-06-30 Event Route Follow-Ups

- Implemented the finalized route/default/event-delivery plan in the vpsAdmin
  worktree
  `worktrees/2026-06-15-vpsadmin-events/vpsadmin`.
- Default routes no longer use a dedicated `event_routes.default_route` flag.
  Generated default routes are now ordinary root routes with a
  `default_routed == true` matcher, using the uniform top-level matcher field
  name `default_routed`.
- Route processing is additive across matching parent and child routes. When a
  parent and child both match and both have receivers, both receiver sets are
  considered; the user can leave the parent without a receiver to avoid parent
  delivery.
- Boolean matcher support was added for core fields and typed event
  parameters, including `true`/`false` UI choices and normalized matcher
  comparisons.
- Transaction-gated notification delivery release now uses the transaction
  name `Notify` for handle `9002`. Prepared deliveries are stamped with the
  release transaction when the transaction is appended.
- If a transaction chain fails or becomes fatal before a transaction-gated
  notification is attempted, the unsent delivery is kept and moved to the new
  `aborted` delivery state. The event and routing context are moved to
  `aborted` only when every delivery in their scope is a non-delivered final
  state (`skipped`, `canceled`, or `aborted`). Already attempted/released
  deliveries are preserved.
- The same abort behavior is implemented in both API supervisor processing and
  libnodectld chain rollback/failure handling, so it works whether the chain
  state transition is observed from the supervisor event path or node command
  persistence path.
- WebUI follow-ups implemented:
  - parameter labels and event type field metadata are exposed for prettier
    matcher labels;
  - route lifecycle information is shown for custom routes as well as default
    catch-all routes;
  - target edit forms show the target user login as a user link;
  - Event Types hover highlighting is disabled;
  - delivery details show route labels and transaction chain links;
  - event delivery rows use vertical result/attempt/status detail rows to avoid
    wide-table overflow;
  - matched route tables hide the confusing Source/Order columns;
  - route list labels use `Hits`.
- Verification:
  - `ruby -c api/models/event_delivery.rb`: OK;
  - `ruby -c api/models/event_route_matcher.rb`: OK;
  - `ruby -c api/lib/vpsadmin/api/events.rb`: OK;
  - `ruby -c api/lib/vpsadmin/supervisor/node/transaction_chain_events.rb`:
    OK;
  - `ruby -c libnodectld/lib/nodectld/command.rb`: OK;
  - `php -l webui/forms/notifications.forms.php`: OK;
  - `nix develop .#api -c bundle exec rspec
    spec/models/event_route_spec.rb spec/models/transaction_chain_spec.rb
    spec/supervisor/node/transaction_chain_events_spec.rb
    spec/api/resources/event_routing_spec.rb`: 83 examples, 0 failures,
    1 expected pending example for core-only monitoring plugin registration;
  - `nix develop .#api -c bundle exec rspec
    spec/migrations/20260615110000_add_events_spec.rb
    spec/migrations/20260623210000_remove_users_mailer_enabled_spec.rb
    spec/migrations/20260624120000_add_event_routing_contexts_spec.rb
    spec/migrations/20260624121000_migrate_legacy_email_recipients_to_routes_spec.rb`:
    12 examples, 0 failures;
  - `VPSADMINOS_PATH=worktrees/2026-06-15-vpsadmin-events/vpsadminos
    nix develop .#libnodectld -c bundle exec rspec
    spec/nodectld/command_spec.rb`: 33 examples, 0 failures;
  - `nix develop .#webui -c composer test --
    tests/Regression/NotificationRouteUiTest.php
    tests/Regression/NotificationDeliveryHtmlDetailsTest.php`: 34 tests,
    247 assertions, OK;
  - `git diff --check`: OK;
  - `nix develop .#api -c bundle exec rubocop <touched API Ruby files except
    generated db/schema.rb>`: 62 files inspected, no offenses;
  - `nix develop .#vpsadmin -c bundle exec rubocop
    libnodectld/lib/nodectld/command.rb
    libnodectld/spec/nodectld/command_spec.rb`: 2 files inspected, no
    offenses.
- libnodectld spec setup note:
  - running with the flake-pinned immutable vpsAdminOS source failed before
    examples loaded because `libosctl/native` was missing;
  - rerunning with
    `VPSADMINOS_PATH=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-06-15-vpsadmin-events/vpsadminos`
    used the already compiled local native extension and the focused
    libnodectld suite passed.

## 2026-06-30 Event Route Follow-Ups, Post-Review

- A mandatory standalone review of the initial committed implementation found
  four actionable items:
  - unsent transaction-gated e-mail deliveries with a prepared `mail_log_id`
    were skipped by abort handling;
  - the implementation was committed as one broad commit rather than focused
    reviewable commits;
  - API-side abort handling selected delivery IDs and then updated by ID only,
    leaving a race window for an attempted delivery to be overwritten;
  - generated default route detection could treat custom receiverless
    `default_routed` grouping routes as the generated catch-all.
- Fixes applied:
  - removed the `mail_log_id IS NULL` filter from API and libnodectld abort
    handling and added regression coverage for prepared mail-log deliveries;
  - locked selected API delivery rows and rechecked state, attempt count,
    provider message ID, and absence of delivery attempts before aborting;
  - restricted generated default route detection to root self-scope routes
    with label `Default route`, no event selector, and exactly the
    `default_routed == true` matcher;
  - rewrote the local history into three focused commits:
    - `7bda9bc0c` `notifications: route defaults through matchers`;
    - `41879953e` `notifications: abort unsent gated deliveries`;
    - `ddf261808` `webui: refine notification route views`.
- Current head:
  `ddf261808908ff24895e61a87e6cdde6e1ff52a18`.
- The vpsAdmin worktree is clean after removing PHPUnit's generated
  `webui/.phpunit.cache/` directory.

## 2026-07-02 Event Type Reference And Matcher Form Follow-Up

- Follow-up goal: refine the Event types reference layout and matcher form
  usability after live WebUI review:
  - Event type categories now render as collapsible header-like summaries with
    separate title and event count spans.
  - Event metadata now uses inline label/value text such as `Severity:` and
    `Default routed:` instead of a grid of columns.
  - Per-event field tables no longer include an Operators column; operators
    remain documented once in the matcher form reference table.
  - Matcher field selects now show both the field name and description, e.g.
    `cgroups - Affected cgroup paths included in the event`.
  - Matcher value/reference table cells no longer request right alignment.
  - The matcher form JavaScript now selects the first allowed operator when
    changing to a field whose previous operator is invalid, which makes list
    fields switch to `contains`/`not_contains`.
- Verification before commit:
  - `php -l webui/forms/notifications.forms.php &&
    php -l webui/tests/Regression/NotificationRouteUiTest.php`: OK.
  - `ruby -c api/models/event_route_matcher.rb &&
    ruby -c api/spec/models/event_route_spec.rb`: OK.
  - `nix develop .#webui -c composer test -- --filter
    NotificationRouteUiTest`: 12 tests, 122 assertions, OK.
  - `nix develop .#api -c bundle exec rspec spec/models/event_route_spec.rb`
    from `api/`: 28 examples, 0 failures.
  - `git diff --check`: OK.
  - Removed generated `webui/.phpunit.cache/`.
- Devcluster verification:
  - `dev-clusters/vpsadmin/bin/devcluster update
    2026-06-15-vpsadmin-events services` completed successfully.
  - `dev-clusters/vpsadmin/bin/devcluster status
    2026-06-15-vpsadmin-events` reported `status: running`, bridge network,
    and `ready: yes`.
  - `curl -k -I https://webui.aitherdev.int.vpsfree.cz/` and
    `curl -k -I https://api.aitherdev.int.vpsfree.cz/` returned HTTP 200.
  - Authenticated WebUI fetches as the seeded admin:
    - `GET /?page=notifications&action=event_types&user=1`: HTTP 200.
    - `GET /?page=notifications&action=matcher_new&route=1&event_type=vps.oom_report&user=1`:
      HTTP 200.
  - Rendered Event types page checks:
    - `No matchable fields were reported by the API`: 0 occurrences.
    - `<th>Operators</th>`: 0 occurrences.
    - `<details class="notification-event-type-category" open`: 0 occurrences.
    - Category summaries include separate
      `notification-event-type-category-title` and
      `notification-event-type-category-count` spans, e.g. `account` and
      `6 events`.
  - Rendered matcher form checks:
    - Field option includes
      `<option value="cgroups">cgroups - Affected cgroup paths included in the event`.
    - Embedded operator metadata includes
      `"cgroups":["contains","not_contains"]`.
    - Operator reference includes typed parsing guidance for integer, number,
      boolean, datetime, `string_list`, and `integer_list`.
    - Value and matcher reference rows have no matched right-alignment style.
  - A one-off Playwright/Node browser probe was not run because the local
    `.#webui` and root dev shells do not provide `node`; the rendered HTML and
    focused regression tests cover the form metadata and JavaScript source.
- Hook status:
  - Overcommit pre-commit hook is installed at the Git-resolved hook path
    `/home/aither/workspace/ai/vpsfree.cz/repos/vpsadmin.git/hooks/pre-commit`.
  - `nix develop .#vpsadmin -c bundle exec overcommit --version` reports
    `overcommit 0.71.0`.

## 2026-07-02 Event Types Devcluster Runtime Refresh

- User reported the Event Types page still showed no matchable fields after the
  WebUI/API metadata changes.
- Root cause found by fetching the live page and API:
  - WebUI was serving the current worktree layout from `/mnt/vpsadmin/webui`;
  - the API process was still running from an older Nix store package at
    `/nix/store/06fnd5pzxb5xnvzy0qlr35dxym3cyric-vpsadmin-api-dev/api`;
  - live `/event_types` returned the old shape with `parameters`, `fields` as a
    label map, and sparse `field_types`, so WebUI dropped the fields as invalid
    metadata and rendered "No matchable fields were reported by the API."
- Ran:
  `dev-clusters/vpsadmin/bin/devcluster update 2026-06-15-vpsadmin-events services`.
- Services VM switched to the new toplevel and restarted API/WebUI services.
  The API now runs from
  `/nix/store/7d0h48ig91xg0s1xqrj1vp9w8a6icwv1-vpsadmin-api-dev/api`.
- Verification:
  - authenticated `/event_types` API fetch now returns `fields` as an array of
    metadata objects and no longer includes top-level `parameters` or
    `field_types`;
  - authenticated fetch of
    `https://webui.aitherdev.int.vpsfree.cz/?page=notifications&action=event_types&user=1`
    returned field rows, including 51 `event_type` rows and one `cgroups` row;
  - fallback count for "No matchable fields were reported by the API" is 0.

## 2026-07-02 Event Types WebUI Layout Follow-Up

- Requested outcome:
  - fix the Event Types page showing "No event-specific matchable fields" for
    every event;
  - stop rendering the page as one outer xtpl table containing nested event
    tables;
  - move event names out of metadata rows and make them title each event
    section;
  - hide template names from normal users while retaining admin visibility;
  - split the sidebar event index from the normal Notifications menu and group
    event links by category.
- Implementation prepared in `vpsadmin`:
  - added a trusted main-content fragment block/helper to xtpl so pages can
    render structured HTML without wrapping it in a synthetic table row;
  - reworked `notifications_event_types()` to render category `<details>`
    blocks, event `<section>` blocks, metadata as a `dl.inline`, and one field
    table per event;
  - hardened event field metadata normalization to accept array/object/list
    shapes, JSON-encoded custom metadata, and HaveAPI PHP resource attributes
    exposed through `__get()` without `__isset()`;
  - added a grouped Event Types sidebar fragment after the normal
    Notifications sidebar;
  - amended the layout after user feedback so categories start collapsed,
    category counts render as literal text such as `account (6)`, event labels
    render on their own line, and hash links open and scroll to collapsed event
    sections;
  - moved layout styling to the existing WebUI CSS files.
- Committed in `vpsadmin`:
  `7abfd953579fdfb78578d30e512598eedeca00d0`
  (`webui: improve event type reference layout`).
- Verification before commit:
  - `php -l webui/forms/notifications.forms.php
    webui/lib/xtemplate.lib.php
    webui/tests/Regression/NotificationRouteUiTest.php`: OK;
  - `git diff --check`: OK;
  - `nix develop .#webui -c composer test -- --filter
    NotificationRouteUiTest`: 12 tests, 111 assertions, OK;
  - `nix develop .#webui -c composer test -- --display-warnings`: 61 tests,
    401 assertions, exit
    status 0, with 2 unrelated existing warnings from
    `OutageDetailsReporterNameXssTest` mock objects missing
    `outage_security_advisory` and `security_advisory` properties.
  - Removed generated `webui/.phpunit.cache/`.
- Mandatory review:
  - launched standalone reviewer `Erdos`
    (`019f2306-993f-7500-8db1-3f10a893d306`) against
    `252d7f635a1684d449d9b2b4b0b593e2ef2fb0bc..7abfd953579fdfb78578d30e512598eedeca00d0`.
  - result: no blocking, important, or advisory findings;
  - reviewer reran
    `nix develop .#webui -c composer test -- --filter
    NotificationRouteUiTest`: 12 tests, 111 assertions, OK;
  - residual risk: live authenticated browser rendering was not verified by
    the reviewer, so CSS/details scrolling behavior is covered by source
    inspection and PHP regression tests rather than Playwright/browser output.

## 2026-06-30 Devcluster Redeploy After Default-Route Removal

- User reported that the current event-route branch did not appear deployed to
  the dev cluster and allowed a reset.
- Ran:
  `dev-clusters/vpsadmin/bin/devcluster reset 2026-06-15-vpsadmin-events`
  followed by
  `dev-clusters/vpsadmin/bin/devcluster start
  2026-06-15-vpsadmin-events --topology single --network bridge`.
- The reset completed and removed cluster state. The start reached `ready: yes`
  and used the current vpsAdmin worktree at head
  `8379a869b5306820230d32ef5d49a5fef67c31d3`, but the services switch then
  failed because `vpsadmin-devcluster-seed.service` still assigned the removed
  `EventRoute#default_route` attribute.
- Fixed the devcluster seed source in `dev-clusters/vpsadmin/nix/test.nix` by
  removing `default_route: false` from the explicit mail-recipient route seed.
  Those routes are already scoped by `event_type` and `template_name`; adding a
  `default_routed` matcher would have changed their meaning.
- Ran:
  `dev-clusters/vpsadmin/bin/devcluster update
  2026-06-15-vpsadmin-events services`.
  The update rebuilt and copied a new
  `/nix/store/...-vpsadmin-devcluster-seed.rb`, switched services, reran the
  seed, and refreshed node runtime state.
- Deployment verification:
  - `dev-clusters/vpsadmin/bin/devcluster status
    2026-06-15-vpsadmin-events`: running, bridge network, `ready: yes`;
  - `systemctl --failed --no-pager` on `services`: `0 loaded units listed`;
  - `systemctl is-active` reported active for `vpsadmin-api.service`,
    `vpsadmin-database-setup.service`, the e-mail/webhook/SMS/Telegram
    notification dispatchers, and `vpsadmin-telegram-receiver.service`;
  - `vpsadmin-devcluster-seed.service` is inactive after successful completion
    with `Result=success` and `ExecMainStatus=0`;
  - `vpsadmin-api-wait-online.service` finished successfully;
  - `curl -k` smoke checks returned HTTP 200 for both
    `https://api.aitherdev.int.vpsfree.cz/` and
    `https://webui.aitherdev.int.vpsfree.cz/`;
  - DB schema/routing check on the services VM:
    `event_routes` has 4 rows, `event_route_matchers` has 3 rows,
    all three matchers are `default_routed == true`, and
    `information_schema.columns` reports 0 `event_routes.default_route`
    columns.
- Dev cluster URLs from `devcluster urls`:
  - Web UI: `https://webui.aitherdev.int.vpsfree.cz/`
  - API: `https://api.aitherdev.int.vpsfree.cz/`
- Committed workspace devcluster fix:
  - `1051bf3` `devcluster: drop removed route default flag`.
- Mandatory standalone review requested from agent `019f1a04-2141-7e30-8260-846098f0ad25`
  for the devcluster seed follow-up.
- Mandatory standalone review result for `1051bf3`:
  - Blocking: none;
  - Important: none;
  - Advisory: none.
  - Reviewer confirmed the commit is focused, the seeded route remains scoped
    by `event_type`, `template_name`, and `subject_scope`, and the absence of a
    `default_routed` matcher is correct because this is an explicit
    mail-recipient route rather than a generated default route.
  - Residual risk: reviewer did not rerun the live devcluster update and
    relied on the recorded successful redeploy, service checks, HTTP smoke
    checks, DB verification, and `git diff --check 1051bf3^ 1051bf3`.

## 2026-06-30 Event Delivery Table Colspan Fix

- User reported that the event details Deliveries table had an incorrect
  colspan: the detail rows with `Result`, `Delivery attempts`, and `Response`
  were short by one column.
- Root cause:
  - the Deliveries table has 8 visible columns;
  - vertical detail rows used a label cell spanning 2 columns and a value cell
    spanning only 5 columns;
  - the empty deliveries row also spanned only 7 columns.
- Fixed in the vpsAdmin WebUI:
  - `webui/forms/notifications.forms.php` now uses value colspan 6 for
    `Result`, `Delivery attempts`, and `Response` rows;
  - the `No deliveries recorded.` row now spans all 8 columns;
  - `webui/tests/Regression/NotificationDeliveryHtmlDetailsTest.php` now
    asserts the 6-column detail value cells and 8-column empty row.
- Folded the fix into the existing WebUI commit because the branch is still in
  development and the change belongs to the WebUI route-view refinement slice.
- New vpsAdmin head:
  `4202f7ce81eb54c19cbf8a0b8474ddb31d71ebc9`
  `webui: refine notification route views`.
- Verification:
  - `git diff --check -- webui/forms/notifications.forms.php
    webui/tests/Regression/NotificationDeliveryHtmlDetailsTest.php`: OK;
  - `nix develop .#webui -c composer test --
    tests/Regression/NotificationDeliveryHtmlDetailsTest.php`: 25 tests,
    171 assertions, OK;
  - amended commit inside `nix develop .#vpsadmin`; Overcommit pre-commit
    hooks passed: Nixfmt OK, MigrationSpecs OK, PhpCsFixer OK;
  - commit-msg hooks passed with warnings for the repo's stricter 72-column
    preference; checked manually that all commit-message lines are <=80
    columns;
  - `git diff --check HEAD^ HEAD -- webui/forms/notifications.forms.php
    webui/tests/Regression/NotificationDeliveryHtmlDetailsTest.php`: OK.
- Deployed to the dev cluster with:
  `dev-clusters/vpsadmin/bin/devcluster update
  2026-06-15-vpsadmin-events services`.
- Deployment verification:
  - devcluster status: running, bridge network, `ready: yes`;
  - services VM `systemctl --failed --no-pager`: 0 failed units;
  - HTTP smoke checks: WebUI 200 and API 200;
  - deployed WebUI store path
    `/nix/store/0n7lc6g2ys77i7hyq9mf94hfnhampbck-vpsadmin-webui`
    contains `false, false, 6` for the Result/Response value cells,
    `false, true, 6` for the Delivery attempts value cell, and
    `false, false, 8` for the empty deliveries row.
- Mandatory standalone review requested from agent
  `019f1a1a-a8d9-7d31-a67b-628613d2d179` for the amended colspan fix.
- Mandatory standalone review result for `4202f7ce81eb54c19cbf8a0b8474ddb31d71ebc9`:
  - Blocking: none;
  - Important: none;
  - Advisory: none.
  - Reviewer confirmed the Deliveries table has 8 visible columns, the detail
    rows now use label colspan 2 plus value colspan 6, and the empty deliveries
    row spans 8 columns.
  - Residual risk: test coverage is source-level rather than a rendered browser
    DOM/layout assertion, but the table arithmetic and deployed-store
    verification are straightforward.

## 2026-07-01 Event Types Hover Fix

- User reported that the WebUI `Event types` table still had a distracting row
  hover background effect.
- Found that the page already had an inline override using `background: inherit`
  for `.notification-event-types tr:hover`, but that was too weak in practice.
  A first follow-up using `background: transparent` was also insufficient,
  because the Event types table is nested inside another row under
  `#transactions`, so the parent hover background still showed through.
- Fixed `webui/forms/notifications.forms.php` to use a scoped white
  background override for `.notification-event-types tr:hover` and
  `.notification-event-types tr:hover td`.
- User reported that the standalone Event types page still showed the hover
  effect. Found the proper source: XTemplate renders table rows with inline
  `onmouseover="this.className='bg'"`, and `#transactions tr.bg td` then
  colors all descendant cells. Changed the wrapper row emitted by
  `notifications_event_types()` to use `table_tr('#fff', false, 'nohover')`
  so that the custom nested table is not put into the global `bg` hover state.
- Updated `webui/tests/Regression/NotificationRouteUiTest.php` to assert the
  stronger white hover override and the `nohover` wrapper row.
- Folded the fix into the existing WebUI commit because it belongs to the
  WebUI route-view refinement slice.
- New vpsAdmin head:
  `5fad7f85ece528808dbd743088091e19768da1b5`
  `webui: refine notification route views`.
- Verification:
  - `git diff --check -- webui/forms/notifications.forms.php
    webui/tests/Regression/NotificationRouteUiTest.php`: OK;
  - `nix develop .#webui -c composer test --
    tests/Regression/NotificationRouteUiTest.php`: 10 tests, 82 assertions,
    OK;
  - amended commit inside `nix develop .#vpsadmin`; Overcommit pre-commit
    hooks passed: Nixfmt OK, MigrationSpecs OK, PhpCsFixer OK;
  - commit-msg hooks passed with warnings for the repo's stricter 72-column
    preference; checked manually that all commit-message lines are <=80
    columns;
  - `git diff --check HEAD^ HEAD -- webui/forms/notifications.forms.php
    webui/tests/Regression/NotificationRouteUiTest.php`: OK.
- Deployed to the dev cluster with:
  `dev-clusters/vpsadmin/bin/devcluster update
  2026-06-15-vpsadmin-events services`.
- Deployment verification:
  - devcluster status: running, bridge network, `ready: yes`;
  - services VM `systemctl --failed --no-pager`: 0 failed units;
  - HTTP smoke checks: WebUI 200 and API 200;
  - services VM `/mnt/vpsadmin/webui/forms/notifications.forms.php` sees the
    amended worktree source through the live virtiofs mount;
  - services VM grep confirms both the `.notification-event-types` white hover
    rules and `table_tr('#fff', false, 'nohover')` are present in the mounted
    live WebUI source;
  - user confirmed the standalone Event types page no longer shows the hover
    effect. No additional full services rebuild was needed for the final PHP
    source edit because the WebUI source tree is live-mounted.
- Mandatory change review for the hover follow-up:
  - Reviewer `019f1c43-950e-7293-b4c7-fecdc530131b` found no blocking,
    important, or advisory findings.
  - Reviewer reran `nix develop .#webui -c composer test --
    tests/Regression/NotificationRouteUiTest.php`: 10 tests, 82 assertions,
    OK.
  - Reviewer also checked PHP syntax for touched WebUI files and
    `git diff --check` for the latest WebUI diff.
  - Residual risk: hover regression is covered by source-level PHPUnit
    assertions plus live user confirmation, not an automated browser visual
    assertion.
- Final quick verification after the commit split:
  - pre-commit hooks passed for all three commits, including Nixfmt,
    MigrationSpecs, RuboCop, and PhpCsFixer as applicable;
  - `git diff --check 94fd280ddcacff729568c74137e2733e9f4e8ead..HEAD`: OK;
  - syntax checks for touched Ruby files and
    `webui/forms/notifications.forms.php`: OK;
  - `nix develop .#api -c bundle exec rspec
    spec/models/event_route_spec.rb spec/models/transaction_chain_spec.rb
    spec/supervisor/node/transaction_chain_events_spec.rb
    spec/api/resources/event_routing_spec.rb`: 84 examples, 0 failures,
    1 expected pending example for core-only monitoring plugin registration;
  - `nix develop .#api -c bundle exec rspec
    spec/migrations/20260615110000_add_events_spec.rb
    spec/migrations/20260623210000_remove_users_mailer_enabled_spec.rb
    spec/migrations/20260624120000_add_event_routing_contexts_spec.rb
    spec/migrations/20260624121000_migrate_legacy_email_recipients_to_routes_spec.rb`:
    12 examples, 0 failures;
  - `VPSADMINOS_PATH=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-06-15-vpsadmin-events/vpsadminos
    nix develop .#libnodectld -c bundle exec rspec
    spec/nodectld/command_spec.rb`: 33 examples, 0 failures;
  - `nix develop .#webui -c composer test --
    tests/Regression/NotificationRouteUiTest.php
    tests/Regression/NotificationDeliveryHtmlDetailsTest.php`: 34 tests,
    247 assertions, OK;
  - `nix develop ..#api -c bundle exec rubocop <touched API Ruby files except
    generated db/schema.rb>` from the `api/` directory: 62 files inspected,
    no offenses;
  - `nix develop .#vpsadmin -c bundle exec rubocop
    libnodectld/lib/nodectld/command.rb
    libnodectld/spec/nodectld/command_spec.rb`: 2 files inspected, no
    offenses.

## 2026-06-30 Event Route Follow-Ups, Final Review Resolution

- A second standalone mandatory review of the committed event-route series
  found:
  - blocking: the first post-review commit still bundled default-route matcher
    semantics with the independent parent/child receiver fan-out behavior;
  - important: libnodectld event-delivery release wakeups used integer action
    mapping even though `event_deliveries.action` is now stored as strings,
    causing non-email immediate wakeups to publish to the wrong routing key;
  - advisory: the WebUI delivery-log state filter omitted the new `aborted`
    delivery state.
- Resolution:
  - rewrote the local series again to split parent/child fan-out into its own
    commit;
  - changed `NodeCtld::Commands::EventDelivery::Release` to preserve string
    delivery actions and publish to the matching `delivery.<action>` routing
    key, with a focused command spec covering both e-mail and webhook
    deliveries;
  - added `aborted` to the WebUI delivery-log state filter and pinned it with
    a regression assertion.
- Final vpsAdmin commit series for this slice:
  - `9471223aa` `notifications: route defaults through matchers`;
  - `9d167f2e9` `notifications: deliver matching parent and child routes`;
  - `3bcc3d56f` `notifications: abort unsent gated deliveries`;
  - `8379a869b` `webui: refine notification route views`.
- Current vpsAdmin head:
  `8379a869b5306820230d32ef5d49a5fef67c31d3`.
- Final quick verification after resolving the second review:
  - pre-commit hooks passed for all four commits;
  - `nix develop .#api -c bundle exec rspec
    spec/models/event_route_spec.rb spec/models/transaction_chain_spec.rb
    spec/supervisor/node/transaction_chain_events_spec.rb
    spec/api/resources/event_routing_spec.rb`: 84 examples, 0 failures,
    1 expected pending example for core-only monitoring plugin registration;
  - `nix develop .#api -c bundle exec rspec
    spec/migrations/20260615110000_add_events_spec.rb
    spec/migrations/20260623210000_remove_users_mailer_enabled_spec.rb
    spec/migrations/20260624120000_add_event_routing_contexts_spec.rb
    spec/migrations/20260624121000_migrate_legacy_email_recipients_to_routes_spec.rb`:
    12 examples, 0 failures;
  - `VPSADMINOS_PATH=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-06-15-vpsadmin-events/vpsadminos
    nix develop .#libnodectld -c bundle exec rspec
    spec/nodectld/commands/event_delivery/release_spec.rb
    spec/nodectld/command_spec.rb`: 34 examples, 0 failures;
  - `nix develop .#webui -c composer test --
    tests/Regression/NotificationDeliveryHtmlDetailsTest.php
    tests/Regression/NotificationRouteUiTest.php`: 35 tests,
    250 assertions, OK;
  - syntax checks for touched Ruby files and
    `webui/forms/notifications.forms.php`: OK;
  - `git diff --check 94fd280ddcacff729568c74137e2733e9f4e8ead..HEAD`: OK;
  - `nix develop ..#api -c bundle exec rubocop <touched API Ruby files except
    generated db/schema.rb>` from the `api/` directory: 62 files inspected,
    no offenses;
  - `nix develop .#vpsadmin -c bundle exec rubocop
    libnodectld/lib/nodectld/command.rb
    libnodectld/lib/nodectld/commands/event_delivery/release.rb
    libnodectld/spec/nodectld/command_spec.rb
    libnodectld/spec/nodectld/commands/event_delivery/release_spec.rb
    libnodectld/spec/support/runtime_helpers.rb`: 5 files inspected, no
    offenses.
- The vpsAdmin worktree is clean after removing PHPUnit's generated
  `webui/.phpunit.cache/` directory.

## 2026-07-02 Event Type Reference Follow-Up Final State

- Committed vpsAdmin follow-up:
  - `431e0256b` `webui: refine event type matcher reference`.
- The commit refines the Event types and matcher-reference UI:
  - collapsible category summaries use separate title/count spans and are not
    expanded by default;
  - event metadata uses compact `Severity:` and `Default routed:` rows;
  - per-event field tables show Field, Type, Example, and Meaning only;
  - matcher field selects include both field name and description;
  - list fields expose `contains`/`not_contains` through the embedded
    field-operator metadata and the operator select now falls back to the
    first valid operator after field changes;
  - matcher value and reference rows are left-aligned.
- Verification for this follow-up:
  - `php -l webui/forms/notifications.forms.php &&
    php -l webui/tests/Regression/NotificationRouteUiTest.php`: OK;
  - `ruby -c api/models/event_route_matcher.rb &&
    ruby -c api/spec/models/event_route_spec.rb`: OK;
  - `nix develop .#webui -c composer test -- --filter
    NotificationRouteUiTest`: 12 tests, 122 assertions, OK;
  - `nix develop .#api -c bundle exec rspec spec/models/event_route_spec.rb`
    from `api/`: 28 examples, 0 failures;
  - `nix develop .#api -c bundle exec rubocop spec/models/event_route_spec.rb`
    from `api/`: 1 file inspected, no offenses;
  - `git diff --check`: OK;
  - Overcommit hooks passed during commit: Nixfmt, MigrationSpecs,
    PhpCsFixer, RuboCop, and commit message hooks. The commit message hook
    warned about its 72-column preference, but all lines are under the
    workspace's 80-column requirement.
- Live devcluster verification:
  - `dev-clusters/vpsadmin/bin/devcluster update
    2026-06-15-vpsadmin-events services` completed successfully;
  - devcluster status: running, bridge network, `ready: yes`;
  - WebUI and API roots returned HTTP 200;
  - authenticated WebUI Event types fetch returned HTTP 200 and had:
    - 0 occurrences of `No matchable fields were reported by the API`;
    - 0 occurrences of `<th>Operators</th>`;
    - 0 forced-open event category `<details>`;
    - category title/count spans such as `account` and `6 events`;
  - authenticated matcher form fetch for route `1` and event
    `vps.oom_report` returned HTTP 200 and had:
    - `cgroups - Affected cgroup paths included in the event` in the field
      select;
    - `"cgroups":["contains","not_contains"]` in field operator metadata;
    - typed matcher value reference text for integer, number, boolean,
      datetime, `string_list`, and `integer_list`;
    - 0 matched right-aligned value/reference rows.
- A one-off Playwright/Node browser probe was not run because the local
  `.#webui` and root dev shells do not provide `node`; the rendered HTML and
  focused regression tests cover the metadata and JavaScript source used by
  the dropdown.
- Mandatory change review:
  - Reviewer `019f2351-cd92-7623-b61f-6a23f8316c34` found no Blocking or
    Important issues.
  - Advisory: direct typed matcher parsing coverage omitted `integer_list`.
  - Resolution: amended the commit with `selected_report_ids`
    `contains`/`not_contains` examples and an invalid integer-list matcher
    closed-failure example.
  - Post-resolution verification:
    - `ruby -c api/spec/models/event_route_spec.rb`: OK;
    - `nix develop .#api -c bundle exec rubocop
      spec/models/event_route_spec.rb` from `api/`: 1 file inspected, no
      offenses;
    - `nix develop .#api -c bundle exec rspec
      spec/models/event_route_spec.rb` from `api/`: 28 examples, 0 failures;
    - amend commit hooks passed: Nixfmt, MigrationSpecs, PhpCsFixer, RuboCop,
      and commit message hooks. The same 72-column warning remains, but all
      message lines are under 80 columns.

## 2026-07-05 Event Roles And Monitoring Definitions

- Requested outcome: implement the approved event-role/template-context plan
  after the rebase onto current `vpsadmin` master:
  - event definitions declare explicit `roles`;
  - templates no longer decide event role;
  - matchable fields remain distinct from template variables;
  - no `infer_type`, `parameter()`, or `parameters()` compatibility API is
    kept;
  - request events use role `account`, with admin visibility handled through
    admin routes and ignored requests not notifying requesters/applicants;
  - outage generic events are system/admin events and user outage events are
    account events, without a public outage `role` field;
  - concrete monitoring event definitions move out of the core monitoring
    plugin and into `vpsfree-cz-configuration`, with current vpsFree.cz
    monitoring events using role `admin`;
  - monitoring templates are renamed away from the old admin/user role naming
    and no longer receive `alert_role`.
- Current pre-commit heads:
  - `vpsadmin`: `155b6197a0ba82106888cebffbf86b6c1537bbf4`;
  - `vpsfree-cz-configuration`:
    `fce712cfc7aaf73198a6869c855e2cf458f1624e`;
  - `vpsfree-notification-templates`:
    `e39472a6b9dc0f4acd5b554a4b89496cc3ab4786`.
- `vpsadmin` implementation summary:
  - updated the event DSL to localize field metadata with event/family/common
    fallback keys;
  - added explicit role metadata to event definitions and routing context;
  - kept matchable fields typed and flat, with API/WebUI metadata exposing
    names, types, examples, choices, and allowed operators;
  - removed event-field `parameter()`/`parameters()` aliases and verified no
    `infer_type` fallback exists;
  - reworked request, outage, payment, and monitoring event declarations and
    their specs around explicit roles and matchable fields;
  - adjusted request transaction chains so admin/requester notification
    behavior follows request action semantics and ignored requests do not
    notify requesters/applicants;
  - changed outage routing to use concrete generic/user event candidates
    instead of a public outage role field;
  - rewrote the monitoring support event profile DSL so production
    configuration registers concrete alert events;
  - updated built-in notification template IDs and migration/spec fixtures;
  - regenerated API locale YAML and WebUI gettext catalogs and added Czech
    translations for the notification/event routing UI text.
- `vpsfree-cz-configuration` implementation summary:
  - `configs/vpsadmin/api/monitoring.rb` now declares concrete monitoring
    alert event types and notification template IDs used in production;
  - current monitoring events are declared with role `admin`;
  - internal monitoring action names were renamed from old `alert_user` /
    `alert_admins` wording to neutral route/action names.
- `vpsfree-notification-templates` implementation summary:
  - monitoring alert template directories and `meta.rb` IDs were renamed to
    event-oriented names without old admin/user role wording;
  - the tracked `AGENTS.md` example was updated to the new template naming.
- Verification:
  - API locale YAML parses with `YAML.load_file`;
  - `nix develop .#api --command bash -lc 'cd api && bundle exec rake
    vpsadmin:i18n:update'`: OK;
  - `nix develop .#webui --command bash -lc
    'webui/lang/scripts/locales-update --check'`: OK, with the pre-existing
    warning about the gettext string containing the KB URL in
    `forms/oom_reports.forms.php:382`;
  - `nix develop .#webui --command bash -lc
    'php -l webui/forms/notifications.forms.php'`: no syntax errors;
  - API migration specs run separately:
    `bundle exec rspec
    spec/migrations/20260615110000_add_events_spec.rb
    spec/migrations/20260624121000_migrate_legacy_email_recipients_to_routes_spec.rb`:
    8 examples, 0 failures;
  - API event/routing/plugin specs:
    `bundle exec rspec spec/api/resources/event_routing_spec.rb
    spec/models/event_route_spec.rb
    spec/models/transaction_chains/plugins/monitoring/alert_spec.rb
    spec/models/transaction_chains/plugins/outage_reports/update_spec.rb
    spec/models/transaction_chains/plugins/requests/create_spec.rb
    spec/models/transaction_chains/plugins/requests/update_spec.rb
    spec/models/transaction_chains/plugins/requests/resolve_spec.rb`:
    94 examples, 0 failures, 1 expected pending core-only monitoring example;
  - a combined migration+normal spec run was discarded because the migration
    spec harness left the process connected to the migration test database
    before normal specs tried to read `sysconfig`; rerunning the same specs in
    separate processes passed as above;
  - `ruby -c configs/vpsadmin/api/monitoring.rb`: Syntax OK;
  - `nix develop --command bash -lc 'cd vpsfree-notification-templates &&
    bundle exec rake check'`: checked 664 template files;
  - `rg` scans found no `infer_type`, event-field `parameter()`/
    `parameters()` definitions, or old monitoring template names outside
    intentionally excluded migration specs;
  - `git diff --check` passed in `vpsadmin`,
    `vpsfree-cz-configuration`, and `vpsfree-notification-templates`;
  - `git diff --cached --check` passed for staged template renames in
    `vpsfree-notification-templates`.
- Current cleanup/commit notes:
  - `vpsfree-cz-configuration` still has untracked local `.bin/` and
    `.bundle/` directories; they are unrelated generated/local state and will
    not be committed.
  - Next step is to verify hook setup, stage focused changes in the three
    repositories, commit with temp-file messages, then run the mandatory
    change review.

## 2026-07-05 Event Roles And Monitoring Definitions Commits

- Committed `vpsadmin`:
  - `47b1aa78588dc83ed5f7aacf905023f1705097f8`
    `notifications: declare event roles explicitly`.
  - First commit attempt was blocked by hooks:
    - RuboCop requested style fixes in
      `api/lib/vpsadmin/api/events.rb`,
      `api/spec/api/resources/event_routing_spec.rb`, and
      `plugins/monitoring/api/lib/vpsadmin/api/plugins/monitoring.rb`;
    - `VpsadminApiI18n` required generated Czech API metadata labels to be
      translated instead of left as `TODO`.
  - Resolution:
    - fixed the reported RuboCop offenses;
    - filled the generated Czech API catalog entries, especially event
      matcher field descriptions, then reran API i18n normalization and
      health checks.
  - Final hooks passed during commit:
    Nixfmt, MigrationSpecs, VpsadminWebuiI18n, PhpCsFixer, RuboCop,
    VpsadminApiI18n, and commit-msg hooks.
- Committed `vpsfree-cz-configuration`:
  - `ef282e94f541ef13ff54a6d9e18ad8e8c405af5a`
    `vpsadmin-config: define monitoring notification events`.
  - Hooks passed during commit: Nixfmt, RuboCop, and commit-msg hooks.
  - Local untracked `.bin/`, `.bundle/`, and `.rubocop_cache/` remain
    ignored as tooling state.
- Committed `vpsfree-notification-templates`:
  - `58bc7afe97ab52fffbcf0b1e41b9073200d32aa9`
    `monitoring: rename alert templates by event`.
  - This repository does not declare a hook framework; the repo-local required
    `bundle exec rake check` had already passed with 664 template files
    checked.
- Mandatory change review launched:
  - Reviewer: `Huygens`
    (`019f34c6-c4d6-76d0-8362-76c0271bf318`).
  - Review packet included plan/state files, all three base/head commit pairs,
    commit split rationale, verification results, compatibility assumptions,
    and the instruction not to start nested reviewers or long integration
    tests.

## 2026-07-05 Mandatory Review Follow-Up

- Review findings:
  - Blocking: `vpsfree-cz-configuration` still used removed monitoring action
    `:alert_user` for `outgoing_data_flow` and
    `dns_secondary_transfer_failure`.
  - Important: monitoring events declared with role `admin` could still be
    delivered through the affected account's generated catch-all default route,
    so the generated defaults did not reflect event roles.
  - Advisory: external request/outage templates still had old generic
    `template_id` metadata such as `request_action_role` and
    `outage_report_role_event`.
- Fixes made:
  - `vpsadmin` generated self-default routes are now role-aware:
    `Default route` matches `default_routed == true` and
    `roles contains account`, while `Default admin route` matches
    `default_routed == true` and `roles contains admin`.
  - Default route creation and the undeployed default-route migrations now
    create both generated role routes. Route insertion uses the earliest
    generated default so user routes still appear before generated defaults.
  - Monitoring event support now uses `affected_user` for template/event
    subject context instead of the misleading `recipient` keyword.
  - `configs/vpsadmin/api/monitoring.rb` now uses existing routed actions for
    the two stale monitors and the renamed `affected_user` keyword.
  - External request/outage template `meta.rb` files now use concrete template
    IDs matching their directory names and vpsAdmin built-ins.
  - `plugins/monitoring/README.md` no longer documents the removed
    `alert_user` action.
- Verification after fixes:
  - API focused normal specs, run separately from migration specs:
    `bundle exec rspec spec/models/event_route_spec.rb
    spec/models/transaction_chains/plugins/monitoring/alert_spec.rb
    spec/api/resources/event_routing_spec.rb`: 81 examples, 0 failures,
    1 expected pending core-only monitoring example.
  - API migration specs, run in a separate process:
    `bundle exec rspec spec/migrations/20260615110000_add_events_spec.rb
    spec/migrations/20260623210000_remove_users_mailer_enabled_spec.rb`:
    5 examples, 0 failures.
  - A combined migration+normal spec run was again discarded because the
    migration harness left ActiveRecord connected to
    `vpsadmin_test_migration`.
  - Focused API RuboCop:
    `bundle exec rubocop models/event_route.rb models/notification_receiver.rb
    ../plugins/monitoring/api/models/transaction_chains/monitoring/alert.rb
    ../plugins/monitoring/api/events/alert.rb
    db/migrate/20260615110000_add_events.rb
    db/migrate/20260623210000_remove_users_mailer_enabled.rb
    spec/support/notification_routing_spec_helpers.rb
    spec/models/event_route_spec.rb
    spec/models/transaction_chains/plugins/monitoring/alert_spec.rb
    spec/api/resources/event_routing_spec.rb
    spec/migrations/20260615110000_add_events_spec.rb
    spec/migrations/20260623210000_remove_users_mailer_enabled_spec.rb`:
    12 files inspected, no offenses.
  - `vpsfree-cz-configuration`:
    `nix develop --command bundle exec rubocop
    configs/vpsadmin/api/monitoring.rb`: 1 file inspected, no offenses.
  - `vpsfree-notification-templates`:
    `nix develop --command bundle exec rake check`: checked 664 template
    files.
  - `ruby -c` passed for touched API Ruby files and
    `configs/vpsadmin/api/monitoring.rb`.
  - `rg` scans found no stale monitoring `recipient:`/`alert_user` action
    references in the changed code paths and no old generic request/outage
    template IDs in external template metadata.
- Follow-up commits:
  - `vpsadmin`:
    `31fe94f4d` `notifications: split generated defaults by role`.
    The first commit attempt was intentionally rejected by hooks because it
    was run outside the Nix shell and lacked RuboCop, gettext, and MariaDB
    tools. The commit was rerun inside `nix develop .#vpsadmin`; hooks passed
    (Nixfmt, MigrationSpecs, VpsadminWebuiI18n, RuboCop, VpsadminApiI18n,
    commit-msg). The commit-msg hook warned at its stricter 72-column limit,
    but all message lines remain under the workspace's 80-column requirement.
  - `vpsfree-cz-configuration`:
    `0542c90b` `vpsadmin-config: fix monitoring alert routing actions`.
    Hooks passed: Nixfmt, RuboCop, commit-msg.
  - `vpsfree-notification-templates`:
    `d94a914` `templates: use concrete request and outage IDs`.
    The repository declares no hook framework; `bundle exec rake check`
    passed before commit.
- Second mandatory change review launched:
  - Reviewer: `Averroes`
    (`019f34ef-0655-7292-b2d8-53ee2617e531`).
  - Review packet included the previous review findings, new follow-up heads,
    role-semantics clarification, quick verification, and deployment
    assumptions.
- Second mandatory change review result:
  - Blocking: none.
  - Important: none.
  - Advisory: none.
  - Reviewer confirmed the three prior findings were addressed:
    role-specific generated defaults in `vpsadmin`, stale monitoring action
    references and renamed `affected_user` keyword in
    `vpsfree-cz-configuration`, and concrete request/outage template IDs in
    `vpsfree-notification-templates`.
  - Residual gaps noted by reviewer:
    full supplied suites/long integration checks were not rerun by the
    reviewer, and existing development databases that already ran older
    in-development migrations may need reset/reapply, consistent with the
    no-compatibility branch assumption.

## 2026-07-06 Event Metadata Translations

- Goal resumed after user asked to translate event field descriptions and
  event labels, including configuration-owned monitoring events, and to add
  stale-translation protection to `vpsfree-cz-configuration`.
- `vpsadmin` changes:
  - API i18n now loads bundled locale files and optional external locale files
    from `config/locales/*.yml`, allowing deployment configuration to localize
    events it defines itself.
  - Event type labels, severity descriptions, common matcher field
    descriptions, and event-specific field descriptions are now represented as
    runtime i18n defaults in the API catalog.
  - Monitoring event field descriptions are declared explicitly in the
    monitoring plugin and exposed for dynamic monitoring event definitions.
  - `en.yml` and `cs.yml` were regenerated with full event metadata
    translation keys; Czech event labels and field descriptions were filled.
  - The `VpsadminApiI18n` Overcommit hook was made robust for nested bundle
    execution by leaving the root Bundler environment before invoking the API
    bundle.
- `vpsfree-cz-configuration` changes:
  - Added generated locale files under `configs/vpsadmin/api/locales/` for
    configuration-defined monitoring event labels.
  - Added `VpsAdminConfig::EventI18n::Catalog`, which uses Ripper/token
    parsing to extract literal `alert_event` names and labels from
    `configs/vpsadmin/api/monitoring.rb` without evaluating production
    configuration.
  - Added rake tasks `vpsadmin:events:i18n:update` and
    `vpsadmin:events:i18n:health`.
  - Added an Overcommit `RakeTarget` pre-commit hook for the health task and a
    GitHub Actions workflow that runs the health task and the new specs in the
    Nix development shell.
  - Added `csv` to the test bundle because the Ruby 3.4 environment no longer
    provides it as a bundled default gem for the existing spec helper path.
- Verification:
  - `nix develop .#api -c bundle exec rspec
    spec/api/resources/event_routing_spec.rb`: 46 examples, 0 failures,
    1 expected pending core-only monitoring example.
  - `nix develop .#api -c bundle exec rspec
    spec/api/resources/event_routing_spec.rb:1389
    spec/api/resources/event_routing_spec.rb:1422
    spec/api/resources/event_routing_spec.rb:1443`: 3 examples, 0 failures.
  - `nix develop .#api -c bundle exec rake vpsadmin:i18n:health`: passed.
  - Focused API RuboCop:
    `nix develop .#api -c bundle exec rubocop
    lib/vpsadmin/api/i18n.rb lib/vpsadmin/api/events.rb
    lib/vpsadmin/api/i18n/catalog.rb
    ../plugins/monitoring/api/events/alert.rb
    spec/api/resources/event_routing_spec.rb`: 5 files inspected, no
    offenses.
  - `nix develop -c bundle exec rake vpsadmin:events:i18n:health`: passed.
  - `nix develop -c bundle exec rspec spec/vpsadmin_config/event_i18n`:
    8 examples, 0 failures.
  - Focused configuration RuboCop:
    `nix develop -c bundle exec rubocop
    lib/vpsadmin_config/event_i18n/catalog.rb
    spec/vpsadmin_config/event_i18n/catalog_spec.rb Rakefile`: 3 files
    inspected, no offenses.
  - Configuration Overcommit pre-commit suite passed in the Nix shell:
    RakeTarget, Nixfmt, RuboCop.
  - vpsAdmin Overcommit pre-commit suite passed in the default Nix shell:
    MigrationSpecs, VpsadminApiI18n, VpsadminWebuiI18n, Nixfmt, PhpCsFixer,
    RuboCop.
- Hook notes:
  - A first configuration Overcommit run outside `nix develop` failed only
    because `nixfmt` was missing; the Nix-shell run passed.
  - A first vpsAdmin Overcommit run exposed that `VpsadminApiI18n` inherited
    the root Bundler environment while invoking the API bundle. The custom
    hook was updated and signed, then the full pre-commit suite passed.
  - `PhpCsFixer` reformatted unrelated WebUI files during one hook run; those
    formatter-only edits were reverted, leaving the vpsAdmin worktree focused
    on event/i18n files.
- Local tooling state:
  - `vpsfree-cz-configuration` still has untracked `.bin/`, `.bundle/`, and
    `.rubocop_cache/` directories; they are local tool/cache state and are not
    part of the intended commit.
- Commits:
  - `vpsadmin`: `485bd9530451b3bb2ff5b0fb6e87c1bf09182000`
    `api: localize event metadata`.
    Base for this commit was
    `31fe94f4d5652e952c7407266965f21484fa0f2e`.
  - `vpsadmin`: `4bc5f3d41e71f00b2aa34d92a8e6c21fbaa1284f`
    `hooks: isolate API i18n bundle`.
    Base for this commit was
    `485bd9530451b3bb2ff5b0fb6e87c1bf09182000`.
  - `vpsfree-cz-configuration`:
    `3ef604cd9ccdba4756632943ec69ebbd4485b10c`
    `vpsadmin-config: guard event label translations`.
    Base for this commit was
    `0542c90b20e7d54a1196795e77759a037afae1c7`.
  - All commits were made with hooks enabled in their Nix development shells.
    Commit-msg hooks warned at their stricter 72-column threshold for the API
    and configuration commits, while the messages still satisfy the workspace
    80-column rule.
  - One attempted vpsAdmin commit outside the Nix shell was rejected by hooks
    because RuboCop, gettext, and MariaDB were unavailable; the same staged
    changes were committed successfully inside `nix develop`.
  - The initially combined vpsAdmin commit was split before review so the API
    metadata work and hook robustness fix are independently reviewable.
- Mandatory change review:
  - Reviewer: `Anscombe`
    (`019f36a1-04c2-72e0-a844-93bdfb87a614`).
  - Initial result:
    - Blocking: none.
    - Important: none.
    - Advisory: the new GitHub Actions workflow used `actions/checkout@v6`
      even though the official releases list `v7.0.0` as the latest
      compatible version; `cachix/install-nix-action@v31` was accepted as
      current.
  - Follow-up:
    - Updated `.github/workflows/event-i18n-health.yml` to
      `actions/checkout@v7`.
    - Reran `nix develop -c bundle exec overcommit --run`: RakeTarget,
      Nixfmt, and RuboCop passed.
    - Amended the configuration commit to
      `3ef604cd9ccdba4756632943ec69ebbd4485b10c`; hooks passed during amend.
    - The same reviewer confirmed that the amended commit now uses
      `actions/checkout@v7`, that the only advisory is addressed, and that the
      one-line amendment introduced no new issue.

## 2026-07-08 vpsAdmin Rebase and CI Follow-up

- Rebased `vpsadmin` branch `2026-06-15-vpsadmin-events` onto
  `origin/master` at `6351e273ed257f5e3233a99ffa7d8eae9221856a`.
- Force-pushed the rebased branch at
  `4c6d0dc01803a9e0f1b7c6739c0e2d00060d7358` and watched GitHub Actions.
  API Specs failed on notification template fallback/default-template checks
  and stale event-engine spec expectations.
- Replaced the initially combined local fix commit with three focused commits:
  - `839b5f161caeb9e17620debe7544062976e34df5`
    `api: restore notification template language fallback`.
  - `d2fd2140537f2025f6e6a733314ab0ab19a6fc73`
    `notifications: make request candidates optional defaults`.
  - `7d4464072982b29ac2f325c6db04b0ed3c5653cc`
    `specs: align event engine expectations`.
- Review follow-up fixes:
  - `Events.template_available?` now uses
    `NotificationTemplate.find_variant`, so candidate availability follows the
    same English fallback semantics as actual rendering.
  - Notification template specs now cover e-mail, Telegram, SMS, and
    `Events.template_available?` language fallback.
  - Added coverage that registered `default: false` template candidates are not
    required shipped defaults.
- Verification before push:
  - Overcommit hooks passed for all three commits inside
    `nix develop .#vpsadmin`: Nixfmt, MigrationSpecs, VpsadminWebuiI18n,
    RuboCop, and VpsadminApiI18n.
  - `git diff --check`: passed.
  - `VPSADMIN_PLUGINS=all nix develop .#api -c bundle exec rspec --format
    progress spec/models/notification_templates_spec.rb
    spec/models/transaction_chains/plugins/requests/create_spec.rb
    spec/models/transaction_chains/dataset/migrate_spec.rb:244
    spec/models/transaction_chains/incident_report/send_spec.rb:82
    spec/models/security_advisory_spec.rb:194
    spec/models/transaction_chains/vps/oom_reports_spec.rb:65`: 27 examples,
    0 failures.
  - `nix develop .#api -c bundle exec rubocop` on the 10 touched Ruby/spec
    files: 10 files inspected, no offenses.
  - One focused RuboCop attempt used repository-root paths while the API shell
    runs from `api/`; it failed with doubled `api/api/...` paths and was
    rerun successfully with API-relative paths.
- Mandatory change review follow-up:
  - Reviewer: `Carver`
    (`019f425b-783a-7361-bd0d-4ef1332203e3`).
  - Initial findings:
    - Blocking: split the broad local fix commit.
    - Important: make `Events.template_available?` mirror renderer language
      fallback.
    - Advisory: add Telegram/SMS fallback coverage and focused
      `default: false` coverage.
  - Follow-up result: blocking and important findings resolved; no new
    blockers before push/CI watch. Reviewer did not rerun RSpec/RuboCop
    personally and accepted the supplied local verification plus mechanical
    diff checks.
- Push/watch follow-up:
  - Force-pushed head `7d4464072982b29ac2f325c6db04b0ed3c5653cc`.
  - Cancelled superseded in-progress CI run `28951362473` from old head
    `4c6d0dc01803a9e0f1b7c6739c0e2d00060d7358`.
  - New RuboCop run `28956380206` passed.
  - New i18n health run `28956379869` passed.
  - New API Specs run `28956380098` passed all shards except the two
    platform shards, which were cancelled while RSpec was still printing
    progress:
    - `API specs (core) - engine` passed.
    - `API specs (full) - engine` passed.
    - `API specs (core) - platform` was cancelled at about the 30-minute
      job timeout during the `Run RSpec (topic)` step.
    - `API specs (full) - platform` was cancelled at about the 30-minute
      job timeout during the `Run RSpec (topic)` step.
    - `API specs - topic coverage` passed.
  - Added commit `9edfb7615a4496a0bfb164fcb2005c5be9d1775b`
    `ci: extend API spec shard timeout`, changing the API spec full/core job
    timeout from 30 minutes to 60 minutes. This is intended to allow the
    platform shards to finish; it does not change spec selection or runtime
    code.
  - Overcommit hooks passed for the timeout commit inside
    `nix develop .#vpsadmin`: Nixfmt, MigrationSpecs, VpsadminWebuiI18n,
    VpsadminApiI18n, and commit-msg hooks.
  - Mandatory review for the timeout commit:
    - Reviewer: `Meitner`
      (`019f4291-a106-7252-b76b-562a71f3b9ce`).
    - Scope: `7d4464072a5271bffc8e55d6f5e5a4d59af453c9..9edfb7615`.
    - Result: no blocking or important findings. Commit split and message were
      accepted; the only residual risk is that the 60-minute timeout now
      applies to all API spec topics, not only `platform`.
  - Force-pushed head `9edfb761572de400cbdb974ed27d480d9c3cb6df`.
  - Cancelled superseded in-progress CI run `28956379948` from old head
    `7d4464072982b29ac2f325c6db04b0ed3c5653cc`.
  - Current-head API Specs run `28959117725` completed successfully. The
    platform shards passed under the 60-minute timeout.

## 2026-07-21 Default-Branch Rebase

- User requested rebasing all event-system development branches onto their
  current repository default branches and explicitly requested backups before
  rewriting history.
- Verified active session `2026-06-15-vpsadmin-events` using both
  `bin/dev-session current` and `VPSFREE_DEV_SESSION_SLUG`.
- Preserved the shared top-level workspace changes. In particular,
  `dev-clusters/vpsadmin/nix/test.nix` currently has event-system Telegram,
  SMS, dispatcher, SMTP, and webhook test-server wiring temporarily disabled
  by other initiatives; this rebase will not overwrite or commit that shared
  top-level diff.
- Fetched all branch-bearing repositories and created/pushed the backup branch
  `backup/2026-06-15-vpsadmin-events-before-default-rebase-2026-07-21` at:
  - `vpsadmin`: `9edfb761572de400cbdb974ed27d480d9c3cb6df`;
  - `vpsfree-notification-templates`:
    `d94a914b69ee71f7b465f6ca21e49640f9eaeaf6`;
  - `vpsfree-cz-configuration`:
    `3ef604cd9ccdba4756632943ec69ebbd4485b10c`;
  - `vpsfree-sms-gateway`:
    `af7b3fafb780c849ae03e31712128ecb0749ec0b`.
- The first configuration backup push was blocked because the Overcommit
  configuration signature was stale. Ran `nix develop -c overcommit --sign`
  after verifying the branch's hook configuration, retried the push, and
  confirmed the exact remote backup ref with `git ls-remote`.
- Default-branch shape before rebasing:
  - `vpsadmin`, `vpsfree-notification-templates`, and
    `vpsfree-cz-configuration` use `master`;
  - `vpsfree-sms-gateway` uses the event-system branch itself as its GitHub
    default and therefore has no separate default branch to rebase onto;
  - the initiative `vpsadminos` worktree is a detached dependency checkout,
    not an event-system development branch.
- Rebase results before updating dependency pins:
  - `vpsadmin` rebased onto `origin/master` at
    `19e613c2ae72103fc04265002402544f387e08c0`; current local head is
    `394b96cdeda1f2c434eeced7279552c9fc825dc7`.
  - `vpsfree-notification-templates` rebased cleanly onto `origin/master` at
    `04921d75ab5321962b207bb380deff90906bd662`; current local head is
    `96d21929fa8caf41d303223272716d8cad940f85`.
  - `vpsfree-cz-configuration` rebased onto `origin/master` at
    `3313c5841d4be30327294c1f5ee215405cf24817`; current pre-pin local head is
    `6c27d7b6d10f645ce64956da1e09d19d10c1e574`.
  - `vpsfree-sms-gateway` remains unchanged at
    `af7b3fafb780c849ae03e31712128ecb0749ec0b`, which is already its default
    branch head.
- vpsAdmin conflict decisions:
  - Preserved documentation identifiers added on master while retaining the
    Notifications menu and member-navigation replacement.
  - Preserved master's broader OOM validation-message assertion together with
    the event branch's no-write assertions.
  - Preserved the deletion of the obsolete advanced-recipient form and the
    removed standalone notification-template uploader.
  - Preserved master's newer security-advisory terminology, changing only the
    delivery wording from e-mail to notification.
  - Kept master's `Set reminder` submit label and the event branch's
    `Notification reminder set` success message.
  - Kept the Notifications menu last and retained the branch's 60-minute API
    shard timeout over master's newer 45-minute value.
- Configuration rebase details:
  - Re-signed verified Overcommit configuration when rebased hook definitions
    changed; hooks passed for the manually resumed commits.
  - Dropped the obsolete generated vpsAdmin input-pin commit during rebase.
    A fresh exact pin will be produced with `confctl` after the rebased source
    heads are reviewable remotely.
  - Preserved untracked local `.bin/`, `.bundle/`, and `.rubocop_cache/`
    directories without staging or modifying them.
- Generated catalog reconciliation:
  - Regenerated API and WebUI catalogs from the rebased tree, merged exact
    Czech translations from current master and the backup branch, resolved 36
    context-dependent labels, and restored the event-delivery transaction
    label in both languages.
  - Added commit `394b96cdeda1f2c434eeced7279552c9fc825dc7`
    `i18n: reconcile notification catalogs after rebase`.
  - The first commit attempt correctly stopped on the changed custom API i18n
    hook signature. Inspected the hook, signed it with
    `overcommit --sign pre-commit` in the repository Nix shell, and committed
    with all hooks enabled.
- Quick verification before mandatory review:
  - vpsAdmin API locale generation and health: passed; no `TODO` placeholders
    remain.
  - vpsAdmin WebUI locale health: passed. It reported only the existing
    embedded-URL gettext warnings in `oom_reports.forms.php` and
    `page_index.php`.
  - vpsAdmin commit hooks passed: Nixfmt, migration specs, API i18n health,
    WebUI i18n health, and commit-message hooks. The message-width hook warned
    at 72 columns; all lines satisfy the workspace 80-column rule.
  - vpsAdmin and configuration `git diff --check`: passed.
  - Notification-template repository `nix develop -c bundle exec rake check`:
    checked 664 template files successfully.
  - Configuration event i18n health: passed.
- Mandatory default-branch rebase review:
  - Reviewer: standalone agent `mandatory_rebase_review`.
  - Initial result: one blocking rebase regression, no important or advisory
    findings. A feature-added security-advisory example still called
    `publish!` without the `expected_content_revision:` keyword required by
    current master. The reviewer reproduced the failure at
    `spec/models/security_advisory_spec.rb:245`.
  - Fixed the call by passing `advisory.content_revision` and committed
    `b44c1490e` `specs: follow advisory publish revision contract`.
  - Full `spec/models/security_advisory_spec.rb`: 7 examples, 0 failures.
  - All enabled vpsAdmin Overcommit hooks passed for the fix commit. The
    commit-message hook again warned at 72 columns; all lines satisfy the
    workspace 80-column rule.
  - The reviewer otherwise confirmed the exact remote backups, intended
    conflict resolutions, patch-identical notification-template replay,
    patch-identical configuration replay apart from the deliberately dropped
    stale pin, stable non-generated event-role patch, generated-only catalog
    commit, and cross-repository template/event/action contract.
  - Residual gaps before integration: generate exact vpsAdmin/template pins;
    the shared dev-cluster event wiring remains temporarily disabled; long
    integration and WebUI KB documentation-contract checks remain pending.
  - Follow-up review confirmed `b44c1490e` resolves the blocker, is focused,
    and introduces no new significant finding. The reviewer cleared the
    branches for force-push, exact pin generation, and longer tests.
- Rewritten source branches published with exact leases:
  - Force-pushed `vpsadmin` from remote head `9edfb761572de400cbdb974ed27d480d9c3cb6df`
    to `b44c1490ec87f3d378faa15ca8f33d89dae0b4d3`.
  - Force-pushed `vpsfree-notification-templates` from remote head
    `e39472a6b9dc0f4acd5b554a4b89496cc3ab4786` to
    `96d21929fa8caf41d303223272716d8cad940f85`.
  - No superseded queued or running workflows existed for the rewritten old
    heads, so no workflow cancellation was needed.
- Regenerated exact configuration pins with `confctl` after the source heads
  were remotely resolvable:
  - `6e09aa9b` `inputs: set vpsadminServices to b44c1490`;
  - `1dd99e07` `inputs: set vpsfreeNotificationTemplates to 96d21929`.
  - `flake.lock` now resolves the vpsAdmin, notification-template, and SMS
    gateway inputs exactly to `b44c1490ec87f3d378faa15ca8f33d89dae0b4d3`,
    `96d21929fa8caf41d303223272716d8cad940f85`, and
    `af7b3fafb780c849ae03e31712128ecb0749ec0b`, respectively.
  - Both generated commits passed configuration Nixfmt and RakeTarget hooks.
  - Force-pushed the configuration branch with an exact lease from remote head
    `fce712cfc7aaf73198a6869c855e2cf458f1624e` to
    `1dd99e07fb2069955802f264495a5a1efb61325d`.
- Current-head GitHub Actions started for vpsAdmin and configuration. No
  notification-template workflows are configured for this branch push.
- Current-head GitHub Actions results at handoff:
  - vpsAdmin `API Specs (topic parallel)` run `29868399048`: passed all 27
    matrix/coverage jobs, including both slow platform shards.
  - vpsAdmin passed `API Migration Specs` `29868399029`, `Client Specs`
    `29868399060`, `Console Router Specs` `29868399016`, `Download Mounter
    Specs` `29868399179`, `RuboCop` `29868399066`, `Webui PHPUnit`
    `29868399201`, `i18n health` `29868399027`, and `libnodectld Specs`
    `29868399020`.
  - Configuration `Event i18n health` run `29868526418`: passed.
  - vpsAdmin aggregate `CI` run `29868399081` remained in progress in its
    selected integration-test step after about 1h07m. It had not reported a
    failure, and the workflow deliberately allows up to 12 hours for this
    broad test step. All other current-head workflows had completed green.
- Final remote verification:
  - Each local source/configuration head exactly matches its remote development
    branch head.
  - All four remote backup refs still resolve to the documented original
    pre-rebase commits.
  - `vpsadmin` and `vpsfree-notification-templates` worktrees are clean;
    configuration contains only the preserved pre-existing untracked cache
    directories.

## 2026-07-22 Integration Failure and Migration Retimestamp

- Aggregate vpsAdmin CI run `29868399081` completed after about five hours
  with 116 selected tests passing and two failures:
  - `alerts/notification-routing` still created matcher field
    `parameters.note` although the final event contract exposes flat field
    `note`; its direct emitter also still used removed keyword `parameters:`
    instead of `payload:`.
  - `webui#support-pages` still expected the removed `Matchable fields` label
    and used `parameters.note` in the route matcher form.
- Downloaded and inspected the full integration artifact before changing or
  rerunning anything. All other workflows for old head `b44c1490e` passed.
- Created and pushed exact pre-rewrite backup branch
  `backup/2026-06-15-vpsadmin-events-before-migration-retimestamp-2026-07-22`:
  - `vpsadmin`: `b44c1490ec87f3d378faa15ca8f33d89dae0b4d3`;
  - `vpsfree-cz-configuration`:
    `1dd99e07fb2069955802f264495a5a1efb61325d`.
- Squashed the integration corrections into rewritten commit `88ca63a87`
  `notifications: clarify event matcher fields`. The final test now verifies
  the Event Types field table structurally and uses flat field `note` plus the
  `payload:` emitter keyword.
- Added focused commit `90291d533` `api: retimestamp event migrations`:
  - renamed the nine event-system migrations and matching specs to contiguous
    versions `20260722120000` through `20260722120800`;
  - updated every `require_migration` and the direct migration path in the
    event-routing API spec;
  - regenerated the core-only schema at version `2026_07_22_120800`.
- Fresh schema generation now runs the event migrations after current master,
  so ActiveRecord reordered some declarations in `schema.rb`. A canonical
  comparison found zero table, index, or foreign-key semantic differences.
- Quick verification:
  - all nine migration specs plus core-schema smoke coverage: 24 examples,
    0 failures;
  - full `api/spec/api/resources/event_routing_spec.rb`: 46 examples,
    0 failures, 1 expected pending example;
  - `tools/check_migration_specs.rb --base origin/master --head HEAD`: passed;
  - no old migration versions or stale `parameters.note` references remain;
  - final full Overcommit run passed MigrationSpecs, Nixfmt, API/WebUI i18n,
    PhpCsFixer, and RuboCop without leaving worktree changes;
  - `git range-diff` shows only the intended amended event-field commit and
    the new focused migration-retimestamp commit.
- Local command notes:
  - starting `tools/test-db` in one short-lived `nix develop -c` and running
    Rake in another lets the detached MariaDB process die between commands;
    run start and migration commands inside one `nix develop -c bash` process;
  - migration specs need `--options /dev/null`, but API specs must use the
    repository `.rspec` options so request helpers are loaded.
- Mandatory fresh-context change review:
  - the initial review found one blocking commit-coherence issue: the
    Playwright regression check used CSS classes introduced by the following
    commit;
  - amended the matcher-fields commit to anchor the generated event ID and
    identify the generic fields table by its exact `Field` header, which is
    valid in that commit and remains valid at the final head;
  - the same reviewer confirmed the blocker is resolved with no blocking,
    important, or advisory findings remaining;
  - the final full Overcommit run passed all enabled hooks after the rewrite.
- First focused `alerts/notification-routing` rerun failed in the webhook
  assertion with `key not found: "parameters"`. The saved VM artifact showed
  that delivery itself succeeded; the test still expected the old webhook
  member name even though the same matcher-fields commit changed it to
  `payload`.
- Updated that assertion to read `event.payload.note`, committed through the
  hooks, and autosquashed it into the matcher-fields commit. The focused rerun
  then passed its end-to-end e-mail and webhook delivery example.
- First focused `webui#support-pages` rerun completed 9 of 10 Playwright tests
  successfully. Its notification test reached the event detail page and found
  the correct payload JSON, but still searched for the old `Parameters` row
  label while the page rendered `Payload`.
- Updated the row label and local test variable, committed through hooks, and
  autosquashed into final matcher-fields commit `88ca63a87`.
- Final focused integration results:
  - `alerts/notification-routing`: 1 example passed; full test successful in
    349.87 seconds;
  - `webui#support-pages`: all 10 Playwright tests passed; selected script
    successful in 713.13 seconds and full test teardown in 941.1 seconds.
- Published vpsAdmin with an exact lease from `b44c1490e` to final head
  `90291d533325774079e1e26a5b09d3a576f5abd6`. The remote backup ref still
  resolves to `b44c1490ec87f3d378faa15ca8f33d89dae0b4d3`.
- Rebuilt `vpsfree-cz-configuration` on current `origin/master` `8a605f6f`:
  - replayed the seven functional commits with their original patches and
    messages through active hooks;
  - replaced the duplicate/stale input history with one `confctl --commit`
    commit per source;
  - final generated pins resolve vpsAdmin to `90291d533325774079e1e26a5b09d3a576f5abd6`,
    templates to `96d21929fa8caf41d303223272716d8cad940f85`,
    and the SMS gateway to `af7b3fafb780c849ae03e31712128ecb0749ec0b`;
  - full Overcommit passed RakeTarget, Nixfmt, and RuboCop; flake metadata
    evaluation resolved the same three exact revisions without lock changes.
- Published configuration with an exact lease from `1dd99e07` to final head
  `6a5fee419edc1bcbc1d14d47fcc1cc0e88905a5d`. The remote backup ref still
  resolves to `1dd99e07fb2069955802f264495a5a1efb61325d`.
- No superseded queued or running workflows existed after either force-push.
- Current-head GitHub Actions completed so far:
  - configuration `Event i18n health` run `29909170667`: passed translation
    health and event-i18n specs;
  - vpsAdmin `API Specs (topic parallel)` run `29908412914`: all 27
    matrix/coverage jobs passed, including both platform shards;
  - vpsAdmin `API Migration Specs` `29908412917`, `Webui PHPUnit`
    `29908412994`, `i18n health` `29908413020`, `RuboCop` `29908412907`, and
    `libnodectld Specs` `29908412951`: passed.
- Pending at this checkpoint: aggregate vpsAdmin integration run
  `29908412949`, currently executing selected ci-tagged tests.

## 2026-07-22 Dev Cluster Startup

- Restored the event-system runtime wiring that another initiative had
  temporarily removed from `dev-clusters/vpsadmin/nix/test.nix`:
  - Telegram webhook frontend and HAProxy backend;
  - Telegram, SMS, e-mail, and webhook notification dispatchers;
  - Telegram receiver;
  - SMS gateway;
  - SMTP overrides and webhook test server.
- Preserved the concurrent managed-template change that relocates
  `vpsadmin.api.managedNotificationTemplates` into an optional imported module.
  After restoration, this relocation is the only remaining top-level diff in
  `test.nix`; the restored event wiring matches top-level `HEAD`.
- `git diff --check` passed for the shared top-level checkout.
- The first bridge-network start failed during Nix evaluation because the
  initiative's clean, detached `vpsadminos` worktree was at stale revision
  `e2b5a7a98`, which predates the `system.vpsadminos.revisionDirty` option used
  by the current dev-cluster configuration.
- Switched the detached `vpsadminos` worktree to exact revision
  `736f689391bc3f920e808eb574662ed6a9e6c955`, which is the revision pinned by
  the event branch's vpsAdmin flake and defines the required option. The
  worktree remains clean and detached.
- Started the cluster successfully with the required bridge network:

  ```sh
  dev-clusters/vpsadmin/bin/devcluster start \
    2026-06-15-vpsadmin-events --topology single --network bridge
  ```

- Final cluster status is `running`, `ready: yes`, single topology, bridge
  network. Public API and WebUI endpoints returned HTTP 200; the status endpoint
  returned its expected HTTP 302 redirect.
- The local Telegram token was detected during startup. The cluster applied a
  second services configuration that enabled both Telegram runtime units.
- Runtime verification on the services VM:
  - `vpsadmin-api`, e-mail/webhook/SMS/Telegram dispatchers, Telegram receiver,
    SMS gateway, and webhook test server are active and running;
  - database setup completed successfully;
  - the dev-cluster seed completed successfully and published `tank/ct`;
  - no systemd units are failed;
  - `sv status nodectld` on `node1` reports the service running.
- Managed notification-template installation created 28 templates and 220
  variants, updating 16 templates and 92 variants. Subsequent API restarts
  reported that the same managed source was already installed, confirming the
  idempotent startup path.
- Current-head aggregate integration workflow `29908412949` remains in
  progress in `Run tests` at commit
  `90291d533325774079e1e26a5b09d3a576f5abd6`; it has not reported a failure.

## 2026-07-22 Time Interval Implementation

- Added reusable account-owned calendar intervals, active/mute route
  assignments, event-time evaluation, route-match audit snapshots, OOM mute
  correctness, API/WebUI management, and browser/integration coverage.
- Committed and pushed vpsAdmin revision
  `02a599dffc71b4c8ae07900de39fe80be18cdd75` on branch
  `2026-06-15-vpsadmin-events`; `origin/master` is an ancestor of the branch.
- Quick verification before publication:
  - application model/routing/OOM/API specs: 55 examples, 0 failures;
  - focused interval model specs after the limit case: 9 examples, 0 failures;
  - migration specs in an isolated process: 2 examples, 0 failures;
  - WebUI PHPUnit: 123 tests, 647 assertions, 0 failures;
  - CI selection: 16 tests, 55 assertions, 0 failures;
  - migration coverage, API/WebUI locale health, RuboCop, Nixfmt,
    PhpCsFixer, and all enabled pre-commit hooks passed.
- Migration specs must remain in their dedicated workflow. An attempted API
  engine topic mapping was removed because that workflow deliberately excludes
  migration specs to preserve database-process isolation.
- A direct `git commit` outside the development shell invoked active hooks but
  lacked Nix-provided binaries. Re-running the exact commit as
  `nix develop .#vpsadmin --command git commit -F FILE` passed every hook; this
  is consistent with the existing root-devshell Overcommit note.
- The first schema-generation attempt incorrectly addressed
  `./tools/test-db` from the API dev shell. The shell automatically enters
  `api/`, so the correct path is `../tools/test-db`; this behavior is already
  documented in `notes/vpsadmin/2026-07-20-api-devshell-working-directory.md`.

## 2026-07-22 Time Interval Documentation and Final CI Fixes

- The first current-head vpsAdmin push exposed one RuboCop layout offense in
  `EventTimeInterval`. Commit `50c549797c41c465ab0ebc93d18776aa9c1c0234`
  fixed it; full RuboCop inspected 2,135 files without offenses, the focused
  interval specs passed 9 examples, and every enabled hook passed.
- The aggregate CI run `29932180850` at `50c549797` failed two newly added
  integration assertions. Its failed logs and downloaded VM/Playwright
  artifacts were inspected before changing the tests:
  - the notification-routing test called Active Support's `Array#sole` from a
    standalone API Ruby process where that extension is not loaded;
  - the Playwright assertion used an unscoped documentation ID shared by the
    time-interval heading and sidebar link, causing a strict-mode collision.
- The correction replaced `sole` with explicit cardinality checks and scoped
  the landmark assertion to page content. Nix parsing, JavaScript syntax, CI
  selection tests (16 tests and 55 assertions), and all enabled commit hooks
  passed.
- Before mandatory review, the unmerged feature, layout correction, and CI-test
  correction were squashed into final vpsAdmin commit
  `5d24b42b39e386f0de4d619f45c07047abb38f62`
  (`events: add scheduled route intervals`). It was force-pushed with an exact
  lease, and the superseded running workflow for `91db9d52` was canceled.
- The capture repository now contains deterministic Czech and English
  notification screenshots for routes, a receiver, interval editing, route
  interval assignment, and a scheduled-out event. The ten images were reviewed
  visually and all inventory checksums validate.
  - The functional capture changes and repeated vpsAdmin pin corrections were
    squashed before review into commit
    `c191b39` (`document notification routes and scheduled intervals`).
  - Full `nix develop -c bin/check` passes: 64 concepts, 128 variants, 128
    PNGs, 47 controls, 34 paths, 77 KB bindings, and 9 exceptions; contract
    tests pass 8/50 and annotation tests pass 9/19.
- A dedicated bridge capture cluster was used under slug
  `2026-06-15-vpsadmin-events-captures` with checked-free addresses. The
  services seed and node refresh completed against the final runtime. A durable
  concurrency note is in
  `notes/vpsadmin-kb-captures/2026-07-22-parallel-bridge-clusters.md`.
- Final KB candidates were built from guarded production sources:
  - create `navody:notifikace` and `manuals:notifications`;
  - replace the obsolete e-mail-role and advanced e-mail configuration sections
    in `navody:vps:uzivatele` and `manuals:vps:users`;
  - create five checksum-pinned notification media objects per language.
- Release manifests are
  `work/2026-06-15-vpsadmin-events/kb-release-cs.yml` and
  `work/2026-06-15-vpsadmin-events/kb-release-en.yml`. Both use schema 3,
  create-only policies for the new pages/media, update policies for the two
  existing pages, and informative localized production summaries. No
  production KB write has been made.
- Top-level KB tooling now supports guarded new pages, structural page
  replacements, and selected checksum-verified capture media. Quick tests pass:
  11 runs/56 assertions for contract tools and 22 runs/67 assertions for KB
  staging/release behavior.
- The development `vpsadminServices` configuration pin was regenerated through
  `confctl` as one clean generated commit `7ea8d069` at exact vpsAdmin revision
  `5d24b42b39e386f0de4d619f45c07047abb38f62`. Production and staging pins are
  unchanged. The configuration worktree retains only its pre-existing ignored
  local cache directories.
- Pending before long integration/staging: mandatory standalone change review,
  focused reruns of `alerts/notification-routing` and `webui#support-pages`,
  current-head GitHub Actions, repository branch pushes, and staging of both KB
  manifests. Production promotion remains explicitly out of scope without
  direct user approval.

## 2026-07-22 Mandatory Review Follow-up

- The standalone mandatory reviewer found three blocking vpsAdmin issues:
  - ten new CRUD scopes were absent from the endpoint coverage inventory;
  - a matching mute interval did not count as OOM suppression, and raw OOM
    schedules used processing time instead of the report occurrence time;
  - interval count/delete checks were not serialized and the assignment table
    lacked database referential integrity.
- The final vpsAdmin implementation now lists all ten scopes, evaluates raw OOM
  schedules at the payload timestamp, recognizes interval muting without
  treating a continued delivery as ignored, serializes bounded interval and
  assignment creation with row locks, locks interval deletion, and adds
  cascade/restrict assignment foreign keys. Regression coverage includes a
  delayed 2024 OOM report, scheduled mute continuation, lock ordering, and
  actual MariaDB restrict/cascade behavior.
- Follow-up vpsAdmin verification passed:
  - endpoint inventory plus the complete routing request spec: 48 examples,
    0 failures, 1 expected pending example;
  - interval model and OOM supervisor specs: 27 examples, 0 failures;
  - final OOM supervisor rerun: 17 examples, 0 failures;
  - interval migration specs: 3 examples, 0 failures;
  - focused interval API request: 1 example, 0 failures;
  - targeted RuboCop checks and all enabled commit hooks passed.
- An attempted parallel invocation of three API Nix shells was discarded: the
  shells share the worktree bundle lock and temporary test-database lifecycle,
  causing one process to terminate another. All reported verification above
  comes from sequential reruns.
- The reviewer also found two advisory documentation/tooling issues. New KB
  pages now require DokuWiki create permission rather than edit permission,
  with a low-ACL regression (23 runs, 71 assertions). Receiver captions now
  describe the visible receiver form rather than an e-mail target that is not
  present in the image; both candidate trees and manifests were regenerated,
  and contract-tool tests pass 11 runs and 56 assertions.
- Final committed heads for follow-up review are:
  - vpsAdmin `4eb064ddf9a6832bbd0b96beeb8ae4241d04bd3a`;
  - vpsadmin-kb-captures `c3732d36637ad66644b6ea8f13888b802ab0730a`;
  - vpsfree-cz-configuration
    `398db459b37bc0f85e848058eb1a16e77c729d74`;
  - workspace master `5a65141c749ce122aef8f67d53c85c3aaab86c59`
    before this state update.
- The capture repository's full `nix develop -c bin/check` passed again on the
  final vpsAdmin pin. The configuration branch contains one generated pin
  commit from `90291d53` to `4eb064dd`; production and staging inputs remain
  unchanged. A first `confctl` attempt had the channel and role reversed,
  matched no channel, and made no changes; the corrected invocation and final
  squashed pin both passed the repository hooks.
- vpsAdmin `4eb064dd` has been force-pushed with an exact lease. Capture,
  configuration, and workspace pushes remain pending until the review
  follow-up is complete. Long integration tests and KB staging have not yet
  started.

## 2026-07-22 Mandatory Review Result

- The standalone reviewer passed the exact final heads with no remaining
  blocking, important, or advisory findings:
  - vpsAdmin `4eb064ddf9a6832bbd0b96beeb8ae4241d04bd3a`;
  - vpsadmin-kb-captures
    `c3732d36637ad66644b6ea8f13888b802ab0730a`;
  - vpsfree-cz-configuration
    `398db459b37bc0f85e848058eb1a16e77c729d74`;
  - workspace master `609478e86d9e0ee64cfdd8053a8dc977e8a03d43`.
- The reviewer confirmed that endpoint coverage, OOM timestamp and mute
  handling, referential integrity, concurrency locks, KB create ACLs, capture
  captions, and commit history are resolved. Reviewed paths are clean, diffs
  pass whitespace checks, captures pin the exact vpsAdmin head, and the
  configuration branch contains one generated input-pin commit.
- Residual risks are accepted and already reflected in the plan: long
  notification integration tests and KB staging must still run; old routing
  workers can ignore interval assignments during a mixed-version rollout; and
  locking has focused model and database coverage but no threaded concurrency
  stress test.

## 2026-07-22 Long Integration Follow-up

- `./test-runner.sh test alerts/notification-routing` first exposed a defect in
  the new scheduled-suppression example: exception-message interpolation ran in
  the outer test evaluator, where `deliveries` and `matches` did not exist. The
  embedded API Ruby now uses string concatenation for those diagnostics. The
  final rerun passed both examples and the complete test script in 373.68
  seconds.
- `./test-runner.sh test 'webui#support-pages'` exposed two successive scope
  mistakes in the new matched-route assertion:
  - the documentation ID is intentionally rendered on the matched-routes
    heading, not inside the following table;
  - the shared `rowWithText` helper searches for a table below its scope and
    therefore cannot be passed an already selected table.
- The final Playwright assertion anchors on the documented heading, selects its
  following table, and locates the route row directly within that table. The
  final bridge-network rerun passed the complete support-pages script, including
  all ten Playwright cases, in 1022.45 seconds. The two failed attempts were
  investigated from their retained Playwright error contexts and traces; nine
  unaffected cases passed on each attempt.
- Each vpsAdmin amendment ran inside `nix develop .#vpsadmin`; all pre-commit
  hooks passed. One initial ambient-shell amend attempt was rejected because
  Nixfmt, RuboCop, PHP CS Fixer, gettext, and MariaDB were unavailable; it made
  no commit and was replaced by the successful Nix-shell invocation.
- Final post-integration heads are:
  - vpsAdmin `394064e71baaed8b3ab96ebbefac4b81f1f5520d`;
  - vpsadmin-kb-captures
    `22c57638bf3ee4a9b6842a900308be24ff25bfca`;
  - vpsfree-cz-configuration
    `f3d4a2fa9219d7ade59737bf5f1c71c6fd736bb0`.
- vpsAdmin was force-pushed from reviewed head `4eb064dd` to `394064e71` with
  an exact lease so Nix could compute immutable downstream hashes. The capture
  flake now pins that exact revision and its full `nix develop -c bin/check`
  passes: 47 controls, 34 paths, 35 concepts, 8 semantic selectors; 77
  annotation bindings and 9 exceptions; test sets 8/50 and 9/19; 64 concepts,
  128 variants, and 128 PNGs.
- The prior generated configuration pin was replaced from its base with one
  `confctl inputs channel set --commit vpsadmin vpsadmin 394064e71...`
  commit. Repository hooks passed. Only `vpsadminServices` moved from
  `90291d53` to `394064e71`; production and staging remain on `88f03da4`.
- Capture, configuration, workspace, and KB review staging remain pending until
  the independent reviewer validates this post-review test-only delta and the
  updated exact pins.
