# 2026-06-15-vpsadmin-events

## Goal

Design a general vpsAdmin event system that sits above e-mail delivery.

Today many code paths directly call `MailTemplate.send_mail!` through
transaction chains. Users can globally disable some mail, override role or
template recipients, configure OOM report rules, and, on the incident-filtering
feature branch, configure incident report rules. These controls solve adjacent
problems with separate models and separate WebUI pages.

The target design is:

- vpsAdmin generates typed events first.
- Each user can route their own events from one page.
- A route can perform zero, one, or multiple actions.
- The first actions are e-mail and webhooks.
- The action/receiver model must stay prepared for Telegram and other later
  delivery protocols.
- Events carry typed parameters that routes can match.
- Users can inspect a log of events and the delivery actions taken.
- Incident report rules, OOM report rules, and advanced e-mail settings are
  migrated into this system and then removed from the WebUI.

## Event Time Intervals And User Documentation Addendum

Requested on 2026-07-22: add reusable, account-owned time intervals to event
routes and replace the obsolete knowledge-base guidance for role and template
e-mail recipients with documentation of the event system.

Design decisions:

- Users define named intervals once and assign them to routes in `active` or
  `mute` mode. Multiple active references are ORed, multiple mute references
  are ORed, and a matching mute reference takes precedence.
- A gated route still counts as matched and preserves normal child traversal
  and sibling `continue` behavior. Only that route's own receiver is skipped;
  schedules are not inherited by descendants.
- Intervals support Alertmanager-style repeatable specifications with time
  ranges, weekdays, days of month, months, and years. Specifications are ORed,
  dimensions are ANDed, and ranges within one dimension are ORed.
- Every interval stores one stable IANA time zone, defaulted at creation from
  the owner's profile or UTC. Time ranges are start-inclusive/end-exclusive,
  cannot cross midnight, and must be split explicitly for overnight windows.
- Interval deletion is blocked while routes reference it. Existing routes
  have no interval references and remain always active.
- Route-match audit records snapshot interval names, modes, time zones, and
  match results at the event's routing time.
- The bilingual event-system guide will use `navody:notifikace` and
  `manuals:notifications`. The old user-account articles will retain a concise
  primary-address explanation and link to the new guide.
- New screenshots use `notifications/*` semantic IDs. The legacy role and
  advanced-recipient media remain untouched in production.
- Production KB publication remains approval-gated. This initiative prepares,
  stages, and verifies exact Czech and English releases but does not promote
  them without a later direct approval.

Affected components for this addendum:

- `vpsadmin`: schema, interval evaluator, routing audit, HaveAPI resources,
  WebUI, localization, and tests.
- `vpsadmin-kb-captures`: exact vpsAdmin pin, navigation contract, fixtures,
  bilingual scenarios, and generated PNGs.
- `vpsfree-cz-configuration`: exact generated vpsAdmin input pin.
- Top-level workspace tooling: guarded create-only KB pages and checksummed
  capture media in candidate/release manifests.

Compatibility and deployment:

- The schema is additive. Old vpsAdmin versions ignore interval assignments,
  so all event-routing API/supervisor processes must be updated before users
  can rely on schedules.
- Dispatchers require no protocol change because interval gating happens before
  delivery preparation.
- Rolling application rollback after intervals are configured can deliver
  notifications that the old version would not mute. Do not drop persisted
  interval data; disable configuration and account for this semantic rollback
  before reverting application code.
- Editing an interval affects every referencing route immediately. Historical
  route matches keep the recorded outcome, but events are never queued for a
  later active window or rerouted retroactively.

Current implementation checkpoint:

- The current `vpsadmin` slice is implemented on top of `origin/master`, not
  on top of the discarded incident-filtering branch.
- The user-facing model now follows the Alertmanager-style wording:
  event routes, nested routes, receivers, and receiver actions.
- The current in-development model splits reusable delivery destinations from
  receiver membership: users own notification targets, and receivers link to
  those targets. This lets one verified Telegram chat, SMS number, webhook, or
  e-mail target be reused by multiple receivers/routes without pairing or
  verification duplication.
- Receivers can contain multiple actions. Implemented actions are e-mail and
  webhook; a muted receiver is the explicit "deliver nowhere" target.
- Routes can be nested. A parent route delegates to the first matching child
  subtree; if no child matches, the parent receiver is used. Sibling routing
  stops after a match unless `continue = true`, in which case later siblings
  can add more receiver actions. There is no separate discard decision in this
  revision; suppression is represented by routing to a muted receiver.
- Event deliveries are prepared while the event is routed, then released by a
  transaction-chain transaction or by the API after commit. Dedicated
  long-running dispatcher processes consume released deliveries through
  RabbitMQ wakeups and database reconciliation.
- Telegram notification templates can have an optional HTML part in addition
  to their required text part. vpsAdmin prefers the HTML body for Telegram
  sends using Telegram HTML parse mode and keeps text as the fallback for
  text-only templates, oversized HTML, and older queued payloads.
- Webhook dispatchers send static JSON payload snapshots, sign with
  `X-VpsAdmin-Signature-256` when a receiver action secret is configured,
  retry with backoff, record response status/body/error summary in generic
  delivery attempts, and block private/link-local webhook targets by default.
- E-mail actions render through the generic `NotificationTemplate`/`MailLog`
  machinery when delivery is prepared. The e-mail dispatcher later reconstructs
  the rendered message from `MailLog`, sends it through SMTP, and records the
  delivery attempt. Custom e-mail actions send only to their configured target,
  while default e-mail actions preserve existing user/template recipient
  behavior.
- Telegram delivery/pairing work was moved out of the current implementation
  frame and preserved on backup branch
  `2026-06-15-vpsadmin-events-telegram-backup` for later reference.
- Event types are registered for user account/security mail events, common
  VPS lifecycle/resource mail events, `vps.incident_report`,
  `vps.oom_report`, `vps.oom_prevention`, and `user.test_notification`.
  Converted mail paths emit these events before scheduling e-mail.
- New or converted event sources should use the declarative typed event DSL in
  `VpsAdmin::API::Events.define`, passing domain objects such as `UserSession`
  or `MonitoredEvent` to `route_event!`/`emit!`. The event declaration owns
  derived user/VPS/source/summary/parameter values and per-action delivery
  data, keeping call sites small and avoiding large central switch statements.
- Plugins register their own event declarations from plugin code. Core
  vpsAdmin must not list plugin event types directly, so plugin availability
  continues to control plugin event metadata.
- Delivery actions are declared through
  `VpsAdmin::API::Notifications::Actions`. Receiver actions, deliveries, and
  delivery attempts store action names as strings (`email`, `webhook`,
  `telegram`, etc.) rather than integer enums.
- User-facing copy for event-backed messages should use "notification" rather
  than "e-mail" or "mail". E-mail wording remains appropriate for actual
  e-mail addresses, e-mail receiver actions, rendered e-mail snapshots, and
  mail logs.
- Legacy OOM report rules are backfilled into event routes. Their API
  create/update/delete actions are intentionally deprecated/read-only in the
  compatibility phase, and the old WebUI rule actions redirect users to
  notification routes.
- `vps.oom_report` events carry a `parameters.stage` value. Supervisor-side
  report ingestion uses `raw` so legacy ignore routes can suppress only raw
  OOM reports. User-facing OOM report e-mails use `notification` so later
  recipient routes can target notification delivery without altering raw
  suppression decisions.
- Advanced e-mail template and role recipient settings for event-backed mail
  templates are backfilled into explicit notification routes and receivers.
  Template-specific routes are ordered before role routes, OOM report recipient
  routes match only `parameters.stage == notification`, and users whose legacy
  mailer switch was disabled keep muted default routing.
- The old advanced e-mail WebUI entry points now point users at the unified
  Notifications page. The compatibility API and tables remain for old direct
  mail fallback and rollback while the remaining mail senders are migrated.
- The WebUI has one Notifications page with Routes, Receivers, Event Log,
  Event Types, and Test Event views. Route ordering uses drag-and-drop plus
  up/down links, following the interaction from the incident-filtering branch
  without inheriting that branch.

## Event Field Metadata Addendum

Requested on 2026-07-01: revise the Event Types page and route matcher
metadata so users can understand exactly which event fields can be used in
route matchers.

Design decisions:

- Matchable route fields are distinct from template variables.
- Event declarations use `field` for explicitly typed matchable scalar/list
  fields, `payload` for persisted JSON-safe event payload data, and delivery
  `vars` for rich template context.
- The old `parameter`/`parameters` event-field DSL is intentionally removed;
  this development branch does not need compatibility aliases.
- Every matchable field declares its type explicitly. No inferred field type
  fallback is allowed.
- Route matcher names are flat, such as `vps_id`, `stage`, and
  `subject_relation`; the long `parameters.` matcher prefix is removed.
- List fields are supported only as typed lists (`string_list` and
  `integer_list`) and are matched with `contains`/`not_contains`.
- Object payloads can still be stored for audit/template fallback, but object
  values are not exposed directly as matchable route fields. Events that need
  object-derived matching publish scalar/list derivatives such as
  `affected_vps_ids`, `affected_vps_hostnames`, `concern_classes`, or
  `changed_fields`.
- Webhook payloads expose both the persisted `payload` and a flat `fields`
  object containing the route-matchable values.
- The database column remains `events.parameters` for now, but API/WebUI copy
  and new code paths call it payload.

User-facing WebUI requirements:

- Event Types are grouped by category using collapsible sections.
- Each event has its own detail table instead of severity/default-routed
  consuming horizontal table columns.
- Severity and default routed are displayed as vertical rows.
- Each matchable field row shows field name, type, usable operators, an
  example value, and a description of the field's meaning.
- The Event Types sidebar includes per-event quick links.
- The matcher add/edit UI filters operators by selected field and shows a
  compact operator/type reference table.

Compatibility and deployment:

- No backward compatibility is required for this branch. Existing route
  matcher field names, event test payload inputs, webhook payload keys, and
  event emission call sites can be updated in place.
- Persisted development data with old `parameters.*` matchers should be
  recreated or migrated by the updated development migrations/spec fixtures.

## Event Roles And Template Context Addendum

Requested on 2026-07-05: revise the event design so event routing roles,
matchable fields, and template variables have separate, explicit jobs.

Design decisions:

- Event definitions declare delivery roles explicitly with `roles`, for
  example `account` or `admin`. Notification templates no longer decide the
  event role.
- The old `recipient_roles` matcher plan is superseded. Public route matchers
  use the flat event fields declared by each event type, and role selection is
  part of routing context rather than another user-facing field.
- Matchable event fields are JSON-safe scalars or typed lists declared for
  route matching. Template variables are separate delivery context and may
  still contain richer objects needed by renderers.
- Request events always use event role `account`. Admins receive request
  notifications through admin-visible/default routes; users receive their own
  change-request events and registration accept/deny events. Ignored requests
  do not notify the requester/applicant.
- Outage events no longer expose an outage `role` field. Generic outage
  notifications are system/admin events and user outage notifications are
  account events.
- The core monitoring plugin provides support code only. Concrete monitoring
  alert event definitions live in production configuration, where all current
  vpsFree.cz monitoring events are declared with event role `admin`.
- Monitoring template names no longer encode the old admin/user role naming or
  receive an `alert_role` template argument.
- Plugin-specific domain values can still use clear names such as `pool_role`
  when they describe the monitored object rather than notification routing.

Compatibility and deployment:

- No compatibility aliases are kept in this development branch. Event
  declarations, migrations, specs, templates, and configuration are updated in
  place.
- Deploy the matching `vpsadmin`, `vpsfree-notification-templates`, and
  `vpsfree-cz-configuration` revisions together so template IDs, event types,
  and monitoring action names agree.

## Notification Template Managed Deployment Addendum

Requested on 2026-06-29: make the external notification templates authoritative
for vpsFree.cz deployments, rename the local template repository to
`vpsfree-notification-templates`, improve Telegram rendering, and replace the
standalone uploader with an API-side managed installer.

Affected repositories for this slice:

- `vpsadmin`
  - Adds safe Markdown helpers for HTML e-mail/Telegram template rendering.
  - Adds a managed notification template install rake task that reads template
    packages from the filesystem and writes directly to the database.
  - Adds a NixOS option so API machines can install managed template packages
    after database setup during service start.
  - Removes the old standalone uploader utility from the source tree.
- `vpsfree-notification-templates`
  - Renamed from the historical local `vpsfree-mail-templates` worktree.
  - Exposes the `templates/` tree as the flake default package.
  - Keeps Telegram text templates as fallbacks while updating Telegram HTML
    templates for readable links, spacing, and Markdown-rendered reasons.
- `vpsfree-cz-configuration`
  - Adds a `vpsfree-notification-templates` confctl channel/role and flake
    input named `vpsfreeNotificationTemplates`.
  - Configures vpsAdmin API machines to consume the template package and use
    the flake input revision as the managed installer source id.

Compatibility and deployment:

- Managed install is additive/update-only: it creates or updates templates and
  variants found in the package, but does not delete unrelated database
  templates or variants.
- The last installed source id is stored in `sysconfig`; unchanged redeploys
  skip database writes. A row lock protects concurrent API starts.
- Built-in template seeding remains conservative and separate from managed
  installation, so rollback to the old built-in defaults remains possible.
- No database schema changes are required for this slice. Rollback can read
  the managed template rows already stored in the database; reverting the API
  service simply stops future managed installs.
- Deployment order should pin and deploy the new vpsAdmin revision before or
  together with the managed template package. Old vpsAdmin versions ignore
  the new NixOS option and cannot run the managed installer.
- `vpsfree-cz-configuration` input pins must be updated with
  `confctl inputs channel set --commit`, not by manually editing
  `flake.lock`.

Verification plan for this slice:

- Focused vpsAdmin API specs for managed install, Telegram resource-change
  rendering, Markdown sanitization, and synthetic test notifications.
- RuboCop for touched API files and nixfmt for touched Nix files.
- `bundle exec rake check` and `nix build .#` in
  `vpsfree-notification-templates`.
- `confctl build` for affected vpsAdmin API machines after the vpsAdmin and
  template revisions are pinned.
- Mandatory fresh-context change review after commits and quick local
  verification, before longer deployment checks.

## Affected repositories

- `vpsadmin`
  - Core event registry, models, migrations, routing evaluator, delivery
    planner, delivery transactions/adapters, API resources, WebUI, tests.
  - Migration path from `incident_report_rules`, `oom_report_rules`,
    `user_mail_role_recipients`, `user_mail_template_recipients`, and
    removed `users.mailer_enabled`.
- `vpsfree-mail-templates`
  - Existing e-mail templates remain the initial event e-mail action
    templates.
  - SMS protocol templates are added alongside existing e-mail and Telegram
    protocol variants for SMS-routable event notifications.
  - Telegram protocol variants keep `telegram/<lang>.text.erb` as the
    required fallback and add `telegram/<lang>.html.erb` for user-friendly
    rich Telegram messages with WebUI links.
  - A later slice may still rename/structure templates consistently beyond the
    historical `mail` naming.
  - Webhook payloads are static JSON generated by vpsAdmin and do not need
    templates.
- `vpsfree-cz-configuration`
  - Production vpsAdmin config owns monitoring definitions and abuse notice
    parsers. It may need event registration/config updates and webhook
    delivery policy settings.
  - If vpsAdmin is pinned from this configuration before upstream merge,
    update the pin with `confctl inputs channel set --commit`, not by editing
    `flake.lock` manually.
- `vpsfree-sms-gateway`
  - New dedicated Go service for GSM modem SMS sending/receiving on the two
    APU machines.
  - Replaces sachet for alertmanager SMS delivery and provides a native
    low-priority vpsAdmin SMS API with final-status callbacks.
  - The GitHub repository now exists at
    `git@github.com:vpsfreecz/vpsfree-sms-gateway.git`.
  - vpsAdmin callbacks use per-message HMAC signatures. vpsAdmin sends a
    generated `callback_secret` with each event SMS request; the gateway stores
    it and signs final-status callbacks. vpsAdmin accepts signatures whose
    timestamp is within 20 minutes.
  - Inbound SMS persistence is configurable and disabled by default. Incoming
    modem messages must be drained even when persistence is off, so the modem
    receive path cannot block on unused inbound messages.
  - Gateway schema management starts at version 1. Current development SQLite
    databases may be recreated; unversioned old DBs should fail with a clear
    recreate-database error rather than being migrated.
- DokuWiki user documentation
  - Later documentation for the unified notification page, route examples, and
    webhook delivery flow.

## Telegram HTML Template Compatibility

The Telegram HTML slice is additive. The database schema and API shape already
store an `html` variant body, so no migration is needed. Telegram text remains
required and old text-only templates continue to render and send exactly as
before. New queued Telegram payloads may include `parse_mode: HTML` and
`link_preview_options`, while the dispatcher still accepts old payloads with
only `chat_id` and `text`.

External `vpsfree-mail-templates` HTML bodies intentionally use only helpers
that already existed in the renderer (`webui_url`) plus `ERB::Util` escaping.
This lets the templates be installed before the new sender code without
breaking rendering; old vpsAdmin versions would simply render and ignore the
HTML body, while the new version sends it to Telegram.

Deployment order is therefore flexible for template installation, but the
running service must use the new vpsAdmin revision before users will receive
Telegram HTML. For the dev cluster, update the vpsAdmin services input in
`vpsfree-cz-configuration` and run
`dev-clusters/vpsadmin/bin/devcluster update 2026-06-15-vpsadmin-events
services`; the cluster seed copies and imports the local
`vpsfree-mail-templates` worktree during the services update.

Potential follow-up repositories:

- `vpsfree-client` and generated clients if users should manage event routes
  from CLI clients. The first implementation can rely on HaveAPI
  self-description and WebUI.
- `vpsadmin-go-client` and `terraform-provider-vpsadmin` only if there is an
  explicit requirement to expose event configuration there.

## Approach

### Per-user delivery method controls

Event delivery method enablement is stored outside `users` in
`user_notification_delivery_methods`. Each row belongs to one user and one
delivery method name (`email`, `webhook`, `telegram`, `sms`) and carries an
`enabled` boolean. Missing rows default to enabled for current methods.

Admins may update these settings through a nested user API and the member
administration UI. Ordinary users cannot update method settings. Users may
configure receivers only for methods enabled for their account. Existing
receiver actions for disabled methods stay visible and deletable, but event
routing skips them and already queued receiver-backed deliveries are canceled
before dispatch.

The legacy `users.mailer_enabled` column is migrated into event delivery
settings and generated default routing, then removed. Users who had disabled
mail keep e-mail delivery disabled and receive a generated muted default route;
all users get a generated `Mute` receiver so selected events can be muted
without special hidden state.

### Existing Notification Surface

Current event-like mail sources found in vpsAdmin and plugins:

- Account and authentication:
  - user create/suspend/resume/revive/soft-delete
  - new login, new access token, TOTP recovery code used
  - failed login report
- VPS lifecycle and resources:
  - suspend/resume, migration planned/begun/finished, replacement
  - resource changes, DNS resolver changes
  - network disabled/enabled
  - dataset expanded/shrunk, stopped over quota
- Incidents and OOM:
  - VPS incident report
  - VPS OOM report
  - VPS OOM prevention action
- Operational/monitoring alerts:
  - disk space, outgoing data flow, paid/unpaid CPU, unpaid data flow
  - zombie processes, VPS in rescue, DNS secondary transfer failure
  - dataset expansion alerts
- Outages and advisories:
  - user and generic outage announcements/updates
  - security advisory announcements/updates
- Payments and requests:
  - payment accepted, payments overview
  - request create/update/resolve variants
- Admin/system:
  - daily report and admin monitoring alerts

The first user-facing milestone should cover all public/user-configurable
mail template notifications plus incident and OOM rules. Admin/system mail can
remain on the old direct mail path until a later milestone unless it blocks
the common delivery API.

### Core Concepts

Add a typed event registry in `vpsadmin`, similar in spirit to
`MailTemplate.register`.

Each event type has:

- stable name, e.g. `vps.incident_report`, `vps.oom_report`,
  `auth.new_login`, `outage.announce`;
- label, description, category, default severity;
- audience, initially `user` or `admin`;
- mutability flag, so security-critical events can be made non-discardable if
  operators decide that is required;
- default delivery policy, initially usually e-mail;
- parameter schema with names, labels, types, and matcher operators;
- default resource references, e.g. user, VPS, dataset, IP address, outage;
- action template mapping.

Persist generated events in a new `events` table:

- `user_id`, nullable for admin/system events;
- `event_type`, `category`, `severity`;
- `source_class`, `source_id`, optional source object such as
  `IncidentReport` or `OomReport`;
- common references for fast filtering: `vps_id`, `dataset_id`,
  `ip_address_id`, `outage_id` where available;
- `subject`, `summary`, and a bounded serialized parameter payload;
- `routing_state`, currently `pending`, `routed`, `suppressed`, or `failed`;
- timestamps.

Matched-route attribution is represented separately in `event_route_matches`,
because one event can match a parent/child chain and multiple continuing
sibling routes.

Use a text/JSON payload on MariaDB rather than relying on DB-specific JSON
matching. Rule evaluation happens when the event is generated; event log
filtering should use typed columns and event type, not arbitrary JSON scans.

Persist delivery actions in a new `event_deliveries` table:

- `event_id`;
- `event_route_id`, nullable;
- `notification_receiver_id`, nullable;
- `notification_receiver_action_id`, nullable;
- `action`, initially `email` and `webhook`, with Telegram added by the
  event-delivery slice and room for later protocols;
- `target_kind` and safe display label;
- `template_name`;
- `state`: `prepared`, `released`, `sending`, `sent`, `skipped`, `failed`,
  `canceled`;
- `mail_log_id` for e-mail;
- `transaction_id` retained for compatibility with older queued mail-delivery
  experiments and rollback analysis;
- `released_at`, attempt count, next/last attempt timestamps, response
  status/body, error summary, provider message id, timestamps;
- `payload` snapshot for static webhook JSON.

Persist individual delivery attempts in `event_delivery_attempts`:

- `event_delivery_id`;
- `action`, `state`, and `attempt_number`;
- `started_at`, `finished_at`;
- provider message id, response status/body, error summary, timestamps.

This gives users a log of "event happened" even when the routing result is
"deliver nowhere".

### Receivers And Actions

Add `notification_receivers` as user-owned named delivery targets:

- `user_id`;
- `label`, `description`;
- `enabled`, `mute`;
- timestamps.

A receiver groups zero or more `notification_receiver_actions`:

- `notification_receiver_id`;
- `action`: `email`, `webhook`, `telegram`, and later protocols;
- `label`;
- `target_kind`: `default_recipient` or `custom`;
- `target_value` for custom e-mail addresses or webhook URLs. Future protocol
  actions can use `target_value` and `config` for protocol-specific addressing;
- `template_name` for action-specific rendering later;
- `config` JSON for protocol-specific options;
- optional webhook `secret`;
- `verification_token`, `verified_at`, `enabled`, `last_error`, timestamps.

For e-mail, the initial default receiver action points to the user's existing
account e-mail. Custom e-mail addresses are stored as action targets. The old
role/template recipient settings remain for now and are migrated in a later
slice.

For future protocols:

- The current schema keeps `config`, `verification_token`, `verified_at`, and
  `last_error` on receiver actions so protocols that require pairing or
  verification can be added without redesigning receivers.
- Telegram can work with our own bot as long as the user initiates contact
  with the bot first. Bots cannot start a private conversation with arbitrary
  users. Group chats can be supported later by deliberately pairing the group.
- Telegram webhooks should be preferred over frequent rake polling. The backup
  branch contains the earlier exploratory pairing/delivery work.

For webhooks:

- the action stores URL, enabled flag, and optional signing secret;
- vpsAdmin signs requests with
  `X-VpsAdmin-Signature-256: sha256=<hmac>` over the JSON body;
- delivery is always asynchronous and retryable through `event_deliveries`;
- private/link-local targets are blocked by default, with an explicit local
  override only for trusted development or tests;
- webhook response status, bounded response body, and error summary are stored
  for the event log;
- users should be able to disable a failing receiver/action without deleting
  it.

### Routes And Matching

Replace event-specific settings with generic user-owned `event_routes`.

Route fields:

- `user_id`;
- `parent_id`, nullable for root routes;
- `notification_receiver_id`, nullable;
- `label`;
- `position`;
- `enabled`;
- `event_type` or `event_type_pattern`, nullable for a catch-all rule;
- `continue`, boolean, default false;
- `hit_count`;
- timestamps.

Nested `event_route_matchers`:

- `event_route_id`;
- `field`, e.g. `event.type`, `severity`, `vps.id`, `vps.hostname`,
  `ip.addr`, `parameters.subject`, `parameters.codename`,
  `parameters.cgroup`;
- `operator`;
- `value`.

Operators:

- `==`, `!=`;
- `=~`, `!~`, with regexp timeout and validation;
- `contains`, `!contains`;
- `>`, `>=`, `<`, `<=` for numeric values.

Evaluation:

1. Generate and persist the event.
2. Ensure the user has default notification routing.
3. Load enabled routes for the event user, grouped by `parent_id`, ordered by
   `position, id`.
4. Evaluate root sibling routes in order. If a route matches, evaluate its
   matching child subtree first.
5. When a matching route has at least one matching child, the child subtree
   decides delivery. When no child matches, the matching route's receiver is
   used.
6. `continue = true` continues to the next sibling at the same level and adds
   more receiver actions. The default `continue = false` stops sibling
   evaluation after the match.
7. A muted receiver creates a skipped delivery and marks the event suppressed.
8. If no route matches, create a skipped delivery explaining that no route
   matched.
9. Deduplicate equivalent action targets within the same action type.
10. Persist prepared `event_deliveries`; e-mail deliveries render a `MailLog`
    snapshot immediately and webhook deliveries snapshot their JSON payload.
11. Release prepared deliveries either through
    `Transactions::EventDelivery::Release` in a transaction chain, or after
    commit for direct API events.
12. Long-running dispatchers deliver released rows and record
    `event_delivery_attempts`.

`continue` is useful for additive fan-out routes. For example, one broad route
can send every incident by e-mail and continue, while a later narrow route can
add a webhook for one VPS. Suppression is understandable to users because it
is an ordinary receiver named `Mute`, not a hidden route decision.

### Default-Routed And Opt-In Events

Event types carry explicit `default_routed` metadata.

Existing mail-equivalent event types are default-routed so new and migrated
users keep receiving the same e-mail notifications as before. New high-volume
or workflow-oriented events are opt-in: they are visible in the event type list
and can be matched by explicit routes, but the generated default route ignores
them. This lets vpsAdmin expose useful event data without suddenly spamming
users.

`severity` remains the importance of a concrete event, not the routing policy.
Some event types have dynamic severity based on their parameters. The registry
can describe this in `severity_description` so users understand why, for
example, a transaction-chain state event may be informational for success and
an error for failure.

Transaction chains use one event type:

- `transaction_chain.state_changed`
- parameters include `state`, `previous_state`, `terminal`, `successful`,
  `failed`, chain size/progress, concern labels, user session, and node;
- terminal states are matched with `parameters.terminal == true`;
- failed/fatal states get higher severity, successful terminal states stay
  informational.

This single event type is easier to explain and route than separate created,
finished, failed, and resolved event types. Users can still match exact states
with `parameters.state == done` or failure-like conditions with
`parameters.failed == true`.

Single-use routes support workflow requests such as "notify me when this
transaction chain is done":

- a single-use route is inserted at the top of the user's root routes;
- it matches the chain id and `parameters.terminal == true`;
- after it matches, it is marked spent and disabled rather than deleted, so the
  event log remains explainable;
- if the chain is already terminal when the route is created, vpsAdmin emits a
  current state event immediately and spends the route.

DNS secondary transfer events are also opt-in:

- `dns.zone_transfer.failed`
- `dns.zone_transfer.recovered`

These are meant for users who want immediate operational hooks, especially
webhooks, without turning every DNS transfer status update into default mail.

### Delivery Adapters and Templates

Create a small event delivery service, for example
`VpsAdmin::API::Events.emit!` and `VpsAdmin::API::Events::Router`.

E-mail adapter:

- Reuse `MailTemplate.send_mail!` and `MailLog`.
- Associate the generated `MailLog` with the event delivery.
- Preserve current `message_id`, `in_reply_to`, and `references` threading for
  incidents, outages, advisories, and monitoring alerts.
- Keep existing e-mail templates in `vpsadmin` and `vpsfree-mail-templates` as
  the initial e-mail action templates.
- Current slice prepares routed e-mail for the converted event types by
  rendering `MailLog` snapshots during event preparation. Actual SMTP
  transport is performed by the e-mail notification dispatcher after the
  delivery is released.

Webhook action adapter:

- Always enqueue asynchronously from the event router; never perform HTTP
  calls inline with the user/API operation that generated the event.
- Build a JSON payload containing event id, event type, timestamp, subject,
  summary, resource references, and bounded parameters.
- Sign payloads with `X-VpsAdmin-Signature-256` when a receiver action secret
  is configured.
- Use retry state on `event_deliveries`, with exponential backoff and a maximum
  attempt count.
- Store only bounded response metadata, never large response bodies.
- Current slice implements webhook and e-mail as long-running
  `vpsadmin-notification-dispatcher webhook` and
  `vpsadmin-notification-dispatcher email` services. Compatibility rake tasks
  remain for one-shot reconciliation, but they are not the deployment model.

Template strategy:

- V1: map each event type to the existing e-mail template. Webhook payloads
  are static JSON in vpsAdmin and do not use templates.
- Keep action templates under a predictable directory such as
  `event_templates/<event_type>/<action>/<lang>.plain.erb`, or extend the
  existing template installer in a compatible way when a later non-email
  action needs templates. This detail needs review before implementation
  because `vpsfree-mail-templates` currently deploys only mail templates.
- Rename existing template keys to a consistent event-oriented scheme as part
  of the `vpsfree-mail-templates` slice, with compatibility aliases or a
  migration path for production translations.
- The registry should expose required variables per action so missing
  templates fail in tests, not at runtime.

### API Design

Add resources:

- `event_type#index`
  - registry-backed, read-only metadata for WebUI and clients.
- `event#index` and `event#show`
  - users see their own events; admins can filter by user.
  - filters: user, event_type, category, severity, routing_state, action,
    delivery_state, resource references, created_at range.
- `event.delivery#index` and `event.delivery#show`
  - nested under an event.
- `notification_receiver`
  - CRUD for user receivers.
- `notification_receiver.action`
  - CRUD for e-mail and webhook actions.
- `event_route`
  - CRUD, order, enable/disable.
- `event_route.matcher`
  - nested CRUD.

Keep old resources during migration:

- `oom_report_rule`
- `incident_report_rule`
- `user.mail_role_recipient`
- `user.mail_template_recipient`

They can become compatibility shims or remain read/write until the WebUI no
longer links to them and data migration has run.

### WebUI Design

Create one notification page reachable from the user profile and main
navigation, for example `?page=notifications`.

Views:

- Routes
  - ordered list with enabled toggle, event type/category, matcher summary,
    receiver summary, hit count, edit/delete.
  - nested routes, drag-and-drop ordering, and up/down links.
  - add/edit route with inline matchers.
- Receivers
  - default e-mail receiver;
  - custom e-mail actions;
  - webhook actions, optional secret, and recent failure status.
- Event Log
  - event type, time, resource, matched route, routing state.
  - detail page shows parameters and all delivery actions.
- Event Types
  - show event type labels and the fields available for matching so users do
    not have to guess field names.
- Test Event
  - create a `user.test_notification` event for the current user and inspect
    the route/delivery result.
- Migration/compatibility helpers
  - while old settings still exist, show migrated routes/receivers instead of
    linking to advanced e-mail configuration, incident report rules, or OOM
    report rules.

Do not make a landing page. The first screen should be the actual route list or
event log with tabs.

### Migration Plan

Phase 1: foundation and compatibility

- Add event registry, event/event_delivery tables, receiver/route tables, API
  resources, and WebUI skeleton.
- Backfill default receiver/route configuration from `users.mailer_enabled`
  and remove the column once the event delivery method table is present.
- Implement webhook queuing and asynchronous webhook delivery worker.
- Keep e-mail and webhook delivery rows visible in logs with their delivery
  state.
- Implement event emission for a small set:
  - `vps.incident_report`
  - `vps.oom_report`
  - `vps.oom_prevention`
- Migrate the incident-filtering feature idea to generic `event_routes`,
  without depending on or merging the incident-filtering branch.
- Migrate OOM report rules:
  - per-VPS rule becomes event route for `vps.oom_report`;
  - matcher `vps.id == <id>`;
  - matcher `parameters.cgroup =~ <pattern>` or an equivalent glob operator if
    compatibility requires it;
  - action `notify` becomes a receiver with default e-mail;
  - action `ignore` becomes a mute receiver.
- Preserve incident and OOM report columns for compatibility at first, but
  derive new behavior from events.

Phase 2: advanced e-mail settings replacement

- For each public/user-visible mail template, register a corresponding event
  type.
- Convert `user_mail_template_recipients`:
  - `enabled = false` becomes a mute route for that event type;
  - custom `to` becomes an e-mail receiver/action for that event type.
- Convert `user_mail_role_recipients` into default e-mail receiver groups or
  default route configuration.
- Map `users.mailer_enabled = false` to disabled e-mail delivery plus the
  default mute receiver. The user attribute and old WebUI controls are removed
  in the same migration slice.
- Hide/remove the old advanced e-mail settings page once migrated.

Phase 3: webhook production hardening

- Extend the existing webhook worker with any production policy discovered in
  review, such as allow-lists, proxying, timeout tuning, or operator metrics.
- Keep generic JSON payloads for every event type; do not add webhook
  templates unless there is a concrete need.

Phase 4: broaden event emission

- Move remaining user-facing `mail(...)` call sites to `Events.emit!`.
- Convert monitoring actions so operational side effects remain in the monitor
  action while notification delivery goes through event routing.
- Decide whether admin/system events should use the same page for admins or a
  separate admin notification policy.

### Compatibility Notes

Database changes are additive at first. Existing code can continue using
direct mail while event-enabled call sites are migrated.

Existing mail templates and uploaded production translations remain valid for
the e-mail action. The e-mail adapter must preserve role recipients, template
recipients, language, time zone, and message threading until the migration
replaces those settings.

Existing user behavior must be preserved by data migration:

- no explicit route/settings means the user receives the same default e-mail
  as today;
- `users.mailer_enabled = false` migrates to disabled e-mail delivery plus a
  muted default receiver. Newly event-routed mail paths therefore consistently
  honor the old global disabled-mail setting, including paths that previously
  sent direct mail without checking it;
- disabled template notification remains disabled;
- custom template recipients keep overriding defaults;
- OOM ignored reports remain ignored;
- incident reports from automated parsers remain user-filterable on the
  current feature branch until replaced by event routes.

Rollback:

- While old columns/tables remain, rolling back code should still be able to
  deliver direct mail and read old OOM/incident settings.
- New event logs and webhook receiver actions would be ignored by old code.
- Do not drop old tables or WebUI entry points until after at least one stable
  deployment cycle and an explicit cleanup plan.

Mixed versions:

- API/webui instances running old code must not be required to understand new
  event tables.
- If webhook signing or future protocol integrations require new secret/config
  options, deploy configuration first, then enable the adapter in vpsAdmin.
- If multiple vpsAdmin API workers emit events concurrently, route evaluation
  and delivery creation must be idempotent for source objects that may retry.

Security and privacy:

- Users can only view and route their own user-audience events.
- Admins can inspect all events.
- Event parameter payloads must be bounded and should avoid storing raw
  secrets or complete provider payloads.
- Future compact protocols should be concise by default and link back to
  vpsAdmin for full incident detail.
- Future pairing tokens must be short-lived and single-use.
- Webhook secrets must not be exposed through API output after creation.
- Webhook delivery must not allow users to reach internal services through the
  API worker. The current worker blocks private/link-local targets by default;
  production rollout should review whether to add proxying or allow-lists.

## Compatibility and deployment

- Implement most event-system changes behind additive migrations and
  feature-compatible code paths. There are explicit non-additive cleanup
  exceptions where the old schema cannot represent the new behavior:
  - `users.mailer_enabled` removal: new code can run before the column is
    dropped, but old API/WebUI/model code cannot run after the removal
    migration.
  - singular matched-route attribution removal: new code backfills
    `event_route_matches` and then drops `events.matched_event_route_id` and
    `event_routing_contexts.matched_event_route_id`; old API/WebUI/model code
    cannot run after that migration because it still reads/writes the old
    columns.
  For these cleanup migrations, deployment must restart old app processes onto
  the new revision when the migration is run; rollback to old code requires
  migrating down first.
- Deploy schema and event-capable code before switching broad call sites from
  direct mail to events.
- Keep old APIs and WebUI pages during the migration; remove them only after
  migrated data is verified.
- For webhook signing defaults, add secret/config deployment in
  `vpsfree-cz-configuration` before enabling production delivery where needed.
- No vpsAdminOS node-wide coordinated update should be required. The change is
  in vpsAdmin API/WebUI/nodectld dispatcher release handling, supervisor, and
  production configuration.
- Deploy the nodectld/libnodectld release handler before switching the API to
  emit `Transactions::EventDelivery::Release` in transaction chains. Mixed
  operation with an old nodectld and a new API can otherwise leave chain
  transactions unprocessable because old nodectld does not know transaction
  type `9002`. Dispatcher services may be deployed before or after this step,
  but event deliveries will not leave `released` until a dispatcher is
  available.
- If production configuration pins a feature revision, update it through
  `confctl`, not by hand-editing locks.

## SMS gateway implementation plan

This section records the approved SMS slice as implemented on 2026-06-22.

- Run a small dedicated `vpsfree-sms-gateway` service next to each GSM modem on
  `apu.int.prg` and `apu.int.brq`, replacing the patched sachet deployment for
  Alertmanager SMS.
- Keep priority local to each modem. Alertmanager submits to the same gateway
  with priority `0`; vpsAdmin submits with priority `10`. A single per-modem
  worker always sends the lowest priority queue item first, so vpsAdmin SMSes
  are sent only when that modem has no queued Alertmanager SMS.
- Preserve normal independence by ordering producers differently:
  Alertmanager prefers PRG then BRQ, while vpsAdmin prefers BRQ then PRG. Both
  still fall back to the other APU if their preferred gateway is unavailable.
- Store outbound SMSes in SQLite, retry modem sends with configured attempt,
  timeout, and cooldown settings, and expose final status through gateway
  callbacks to vpsAdmin.
- Support inbound SMS in the gateway from day one by persisting received
  messages and forwarding them to configured webhooks with retry, even though no
  production reader is planned for the first rollout.
- Monitor the gateway with Prometheus through `/metrics` plus `/-/live` and
  `/-/ready`.
- Require phone verification before user-configured vpsAdmin SMS delivery:
  admins must enable SMS notifications on the user account, the user configures
  an E.164 number on an SMS receiver action, vpsAdmin sends a short-lived SMS
  code, and delivery is allowed only after the code is confirmed.
- Render vpsAdmin SMS body text through `vpsfree-mail-templates` `sms/*.text.erb`
  protocol variants, matching the existing email/Telegram template model.
- Production rollout requires secrets for Alertmanager gateway auth, vpsAdmin
  gateway auth, gateway status API, and vpsAdmin callback auth on both APUs and
  vpsAdmin API hosts.
- Rollback can point Alertmanager back to sachet while vpsAdmin SMS actions stay
  disabled. Existing email, webhook, and Telegram delivery paths are unaffected.

## Telegram and generic template plan

This section is the approved direction for the Telegram delivery and template
generalization slice as of 2026-06-21.

### Telegram operating model

Telegram bots have two relevant Bot API modes:

- outbound delivery: vpsAdmin calls Bot API methods such as `sendMessage`;
- inbound updates: the bot can receive messages from users either by
  long-polling `getUpdates` or by configuring a public HTTPS webhook.

For this slice, use outgoing `sendMessage` for delivery and a dedicated
long-running Telegram receiver service for inbound pairing updates. The
receiver supports both:

- `polling`: long-poll Telegram `getUpdates`, storing the last update offset
  in `SysConfig`;
- `webhook`: serve the Telegram webhook endpoint and register it with Telegram
  through `setWebhook`.

The old rake task remains only as a compatibility/manual one-shot wrapper
around the receiver's `poll_once`; it is not the deployment model. Production
uses webhook mode. Dev clusters default to polling, because it works without a
public callback, but can switch to webhook mode for end-to-end testing.

Telegram cannot let the bot start an arbitrary private conversation with a
user. The user must first open the bot and send a command, so the pairing flow
has to be explicit:

1. User creates a Telegram receiver action in vpsAdmin.
2. vpsAdmin generates a short-lived, single-use pairing token.
3. WebUI shows a command such as `/start <token>`.
4. User sends the command to the bot in a private Telegram chat.
5. The Telegram receiver service receives the update by polling or webhook,
   validates the token, stores the Telegram chat ID as the receiver action
   target, and marks the action verified.
6. Event routing can then plan Telegram deliveries for that receiver action.

Group chats should be rejected for the first version. The first supported
target is one private chat per receiver action. Multi-device delivery is
handled by Telegram itself.

### vpsAdmin implementation

Add Telegram as a first-class notification receiver action, next to e-mail and
webhook:

- action name: `telegram`;
- target kind: custom only, with `target_value` storing the paired chat ID;
- `verification_token`, `verified_at`, and `last_error` drive pairing state;
- direct edits to the target or action reset verification;
- dispatch is disabled unless the action is enabled, verified, and has a chat
  ID.

Add a small Bot API client in vpsAdmin:

- token from explicit config, environment, or a token file;
- default API base URL `https://api.telegram.org`;
- JSON POST helper for `sendMessage` and `getUpdates`;
- no token value is exposed through API output, WebUI, logs, or notes.

Add delivery planning/rendering:

- event routing creates Telegram `event_deliveries` only for verified actions;
- delivery payload is snapshotted before dispatch, like webhooks;
- message text is concise by default: severity, subject, event type, optional
  VPS reference, and a WebUI event link;
- do not include full incident/OOM bodies or arbitrary parameter dumps in the
  first version;
- respect Telegram's 4096 character text limit;
- store provider message ID and bounded response/error data in the existing
  generic delivery attempt fields.

Add dispatcher support:

- new dispatcher action `telegram`;
- queue/routing key for Telegram deliveries;
- action-specific concurrency setting, defaulting conservatively;
- retry/backoff follows the existing generic delivery dispatcher behavior;
- missing bot token or Bot API errors leave deliveries retryable.

Add receiver service support:

- executable `bin/vpsadmin-telegram-receiver`;
- NixOS service `vpsadmin-telegram-receiver.service`;
- configurable receive mode: `polling` or `webhook`;
- polling stores the last Telegram update offset in `SysConfig`;
- long-poll timeout and update limit are configurable;
- webhook mode validates `X-Telegram-Bot-Api-Secret-Token` when configured;
- webhook mode can register the public endpoint with Telegram on startup;
- failed Bot API responses do not advance the offset;
- expired or invalid tokens do not pair a chat;
- rejected pairing attempts update `last_error` and rotate the token when it
  helps the user recover.

Add availability gating:

- the API advertises and accepts Telegram receiver actions only when Telegram
  is configured with a token or token file;
- existing Telegram actions become non-deliverable when configuration is
  removed;
- pairing-token creation fails with a clear configuration error when Telegram
  is unavailable.

Add API/WebUI support:

- receiver action forms expose Telegram as an action type;
- unpaired actions show pairing status and the `/start <token>` command;
- paired actions show verified status without exposing secrets;
- users can rotate/create a new pairing token from the receiver action view;
- event delivery detail shows the Telegram delivery state, chat label, bounded
  payload text, provider message ID, and response/error information.

### Dev-cluster testing

Testing from a dev cluster should use a dedicated development Telegram bot.
The Telegram Bot API test environment is intentionally not used for now,
because it adds a separate API host/token shape without improving the main
dev-cluster pairing and delivery workflow.

Required operator steps:

- create a bot with BotFather and store its token outside git at
  `.dev-clusters/vpsadmin/telegram/bot-token`;
- run `devcluster update <slug> services` after creating, changing, or
  removing the token file so the services VM picks up the virtiofs mount and
  service configuration;
- create a Telegram receiver action in WebUI and send `/start <token>` to the
  dev bot;
- trigger the existing test notification event and verify delivery.

Dev clusters default to polling. To exercise webhook mode, set
`telegram.receiveMode = "webhook"` in the dev-cluster JSON config and create
`.dev-clusters/vpsadmin/telegram/webhook-secret`. The dev cluster then enables
the API-domain webhook route at
`https://api.aitherdev.int.vpsfree.cz/_telegram/webhook`.

### Telegram production routing

Use the existing public API domain for the Telegram webhook endpoint, not a
separate Telegram domain:

```text
https://api.vpsfree.cz/_telegram/webhook
```

The production path is:

```text
nginx api.vpsfree.cz exact /_telegram/webhook location
  -> HAProxy telegram-receiver socket
  -> vpsadmin-telegram-receiver.service on int.api1/int.api2
```

The endpoint bypasses Varnish and HaveAPI. This keeps the unauthenticated
Telegram endpoint outside the API app while reusing the existing API TLS
certificate, ACME setup, and public domain.

### Generic template repository and model naming

The current repository and vpsAdmin component are named around mail:
`vpsfree-mail-templates`, `mail_templates`, `MailTemplate`, and related API
resources. The goal is to evolve toward notification templates that can hold
e-mail and Telegram bodies now, with room for additional protocols later.

The redesigned template concept is implemented directly, without keeping
legacy source names:

- vpsAdmin uses `NotificationTemplate`, `NotificationTemplateVariant`,
  `EmailRecipient`, `NotificationTemplateEmailRecipient`,
  `UserEmailRoleRecipient`, and `UserNotificationTemplateRecipient`;
- the API exposes `/notification_templates`, nested variant and e-mail
  recipient resources, `/email_recipients`, and the renamed user recipient
  resources;
- database tables are renamed from the old mail-template names to generic
  notification-template names, with variant rows carrying `protocol` and
  `options`;
- the upload utility is `notification_templates/` with executable
  `vpsadmin-notification-templates`;
- template bodies use the shared filename part `text` for plain-text e-mail
  and Telegram messages.

The repository layout is:

```text
templates/<template-name>/
  meta.rb
  email/<lang>.subject.erb
  email/<lang>.text.erb
  email/<lang>.html.erb
  telegram/<lang>.text.erb
```

`meta.rb` defines shared template metadata and protocol-specific per-language
options. Subjects are template files, so e-mail can interpolate the same local
variables as text/html bodies:

```ruby
template do
  label 'User created'
  user_visibility true

  protocol :email do
    lang :en do
      from 'support@vpsfree.org'
      reply_to 'support@vpsfree.org'
      return_path 'support@vpsfree.org'
    end
  end
end
```

Built-in vpsAdmin templates and plugin templates use the same layout under
`api/notification_templates/templates/` and
`plugins/<plugin>/notification_templates/templates/`.

This rename is intentionally not mixed-version compatible at the API/source
name level. Deployment must update vpsAdmin, run the rename migration, and use
the new upload utility for external templates. Rollback requires migrating the
schema down before old vpsAdmin code can read the template tables again.

### Compatibility and rollback

Event delivery remains additive, but the template rename is a deliberate
schema/API/source rename:

- vpsAdmin and template upload tooling must be deployed together;
- the template rename migration runs before the event-delivery migration on a
  fresh database and renames existing production tables/columns in place;
- e-mail templates are preserved as protocol `email` variants, so rendered
  e-mail behavior is unchanged after the migration;
- Telegram delivery stays opt-in through receiver actions and bot token
  configuration;
- rollback to old vpsAdmin code requires migrating the schema down first;
- external template repositories must use the new layout and upload command.

### Review questions

- Resolved: production pairing uses webhook mode in
  `vpsadmin-telegram-receiver.service`; polling is still supported by the same
  long-running service for development or fallback.
- Should the first Telegram message include only summary/link data, or should
  any specific event types include more detail?
- Is one private chat per receiver action enough for V1?
- Should the historical repository name `vpsfree-mail-templates` be renamed as
  a repository after the generic layout has landed, or kept for continuity?

## Testing plan

- API model specs:
  - event registry validation;
  - event emission, parameter serialization, source references;
  - route matching for all operators and typed fields;
  - ordered routing with `continue`;
  - multi-action delivery plan deduplication;
  - muted/suppressed events;
  - migration equivalence for OOM and incident routes.
- API resource specs:
  - event/event_delivery visibility and filtering;
  - receiver/action CRUD and authorization;
  - webhook action validation and secret redaction;
  - route/matcher CRUD, reorder, limits, and non-owner denial.
- Transaction/delivery specs:
  - e-mail delivery prepares `MailLog`, releases through the event-delivery
    transaction, sends by SMTP in the dispatcher, and records generic delivery
    attempts;
  - webhook async delivery, `X-VpsAdmin-*` headers, signing, failure, and
    retry state;
  - existing message threading for incident/outage/security messages.
- WebUI tests:
  - manage receivers and actions;
  - create/edit/reorder/delete routes;
  - matchers and multi-action deliveries;
  - event log detail with delivery states;
  - old advanced e-mail/OOM/incident links replaced by notifications page.
- Migration specs:
  - convert `oom_report_rules`;
  - convert incident report rules from the feature branch;
  - convert user mail role/template recipient settings;
  - preserve `mailer_enabled` behavior.
- CI metadata:
  - update API spec topic coverage for new specs;
  - update CI selection rules/tags for touched API/WebUI/runtime paths.
- Later integration:
  - targeted WebUI Playwright scenario;
  - optional dev-cluster mail/webhook smoke test.

Run the mandatory standalone change review after implementation commits and
quick local verification, before long integration tests.

## Decisions Proposed For Review

- Use a generic event log plus delivery log, not just "mail log with actions".
- Use nested route semantics with `continue = false` by default; one receiver
  can perform multiple actions, and additive sibling routes can opt into
  `continue = true`.
- Keep e-mail rendering on existing `MailTemplate` for V1.
- Keep webhook JSON static in vpsAdmin. Add a separate action-template
  mechanism only when a future non-email action needs templates.
- Migrate old settings compatibly and keep old APIs until after deployment.
- Keep generic receiver-action verification fields for future protocols that
  need pairing.
- Keep persisted action enums on explicit numeric mappings. Future protocols
  must append new values rather than reordering existing e-mail/webhook values.
- Include webhooks as a first-class asynchronous action.

## 2026-06-25 Reusable Target Follow-up

- Receiver actions now link to reusable notification targets rather than owning
  protocol targets directly. This allows several receivers to share the same
  Telegram chat, SMS number, webhook, or custom e-mail target without repeating
  pairing or verification.
- Link-level enablement is removed. Recreating a receiver-target link is cheap,
  while target-level enablement and delivery-method enablement are the durable
  controls that matter for delivery.
- Telegram exposes bot metadata through the API so the WebUI can show automatic
  pairing first and manual pairing instructions, including the bot name, as the
  fallback.
- SMS targets and custom e-mail targets require verification before delivery.
  Admin saves may mark either kind verified to support operational overrides.
  E-mail verification tokens are stored server-side, hidden from the API, and
  consumed through a link sent to the custom address.
- Custom e-mail targets intentionally contain one e-mail address. Multiple
  recipients should be represented by multiple targets/receiver links/routes,
  which keeps verification and delivery status attributable to one endpoint.
- Compatibility: this remains development-only for the current branch. The
  existing migration may be rewritten and the dev cluster may be reset before
  production deployment. Migrated advanced custom e-mail targets are marked
  verified to preserve existing delivery semantics on fresh dev rebuilds.

## 2026-06-27 Clean Recipient Model Follow-up

The final notification model should not keep the legacy e-mail recipient
surfaces. `email_recipients`,
`notification_template_email_recipients`,
`user_email_role_recipients`, and
`user_notification_template_recipients` should be migrated into the event
system and then removed.

The route-scope idea (`user` vs `global`) is superseded. It solves the current
admin-copy problem, but it hard-codes a special "global admin" exception where
the system really needs permission-aware event visibility.

The initial `event_recipients` idea is also refined: do not materialize every
user that may observe an event. Admins should be able to see all events, while
ordinary users see only their own events. Materializing that full admin audience
would create a large number of rows with no delivery or user-visible state.
Event visibility should be computed from current permissions. Persist
per-user/per-event rows only when there is durable state, such as a routed
delivery, suppression, failure, acknowledgement, bookmark, or read marker.

### Concepts

- Event: one immutable fact that happened. `events.user_id` remains the subject
  user/account for now: the user the event is about. Userless/system events
  need an explicit system relation in the routing context.
- Event visibility: an authorization/audience policy, not a recipient table.
  A user can see:
  - their own subject events;
  - all events when their current user level/permissions make them an admin;
  - later, events allowed by RBAC grants.
- Route owner: the user whose route tree is being evaluated.
- Route context: the event plus the route owner and computed relationship
  between them. This context exposes virtual matcher fields such as
  `context.subject_relation`, `context.subject_user_id`,
  `context.subject_is_self`, and `context.subject_is_admin_visible`.
- Direct event: an event whose subject user is the route owner.
- Indirect event: an event visible to the route owner but whose subject user is
  someone else. Today that means admin-visible events; later it can include
  RBAC/delegated events.
- Route: still owned by a user. Routes can opt into direct, indirect, or system
  events through first-class route scope/context fields and matchers.
- Delivery: a delivery produced by a matched route for one route owner.
- Materialized routing context: a persisted per-user/per-event row only when
  a route matched or some durable per-user state must be stored.

This design lets admins see all events without enabling notifications by
default. Only explicit routes send notifications. Later RBAC can replace or
extend the visibility policy without changing the delivery model.

### Schema Changes

- Add a route scope/context selector to `event_routes`, defaulting existing
  routes to direct/self events only:
  - `subject_scope = self`: only route events whose subject user is the route
    owner;
  - `subject_scope = visible`: route any event the owner can observe,
    including direct, indirect, admin-visible, RBAC/delegated, and system
    events where allowed;
  - optional narrower values can be added later if the UI needs them.
- Add virtual route matcher fields under `context.*`:
  - `context.subject_relation`, e.g. `self`, `other_user`, `system`, and later
    `rbac`;
  - `context.subject_user_id`;
  - `context.subject_is_self`;
  - `context.subject_is_admin_visible`.
- Add matcher operators that can test array parameters:
  - `contains`, true when an array parameter contains the expected string;
  - `not_contains`, inverse of `contains`.
- Add a materialized routing-context table, preferably named
  `event_routing_contexts` rather than `event_recipients`, because the table
  does not represent every user that could observe an event:
  - `event_id`;
  - `user_id`, the route owner/recipient user;
  - `subject_relation`, snapshot of the route context relation at routing
    time;
  - `source`, enum/string such as `direct_route`, `indirect_route`,
    `system_route`, `migration`, and later `rbac_route`;
  - optional later `event_stream_id`, nullable, if saved streams need to mark
    the origin of a route match;
  - `routing_state`, enum/string such as `routed`, `suppressed`, `failed`,
    `read`, `acknowledged`, or `bookmarked`;
  - timestamps;
  - unique index on `[event_id, user_id]`.
- Add `event_route_matches` to persist every matched route for an event:
  - `event_id`;
  - `event_route_id`;
  - `route_owner_id`;
  - `subject_relation`;
  - `source`;
  - `match_order`.
- Add `event_deliveries.event_routing_context_id`, set for all routed
  deliveries.
  Keep `event_deliveries.event_id` as a denormalized compatibility/query column
  until a later cleanup.
- Add `EventDelivery#event_routing_context` and
  `EventRoutingContext#recipient_user`.
- Optional later: add `event_streams`/`event_subscriptions` as saved views over
  events the owner can already see. They should not grant visibility and should
  not materialize per-event rows by themselves.

### Event Metadata

- Add a stable event parameter for old template-role intent, preferably
  `recipient_roles`, an array of strings such as `account` and `admin`.
- Do not overload existing domain-specific `parameters.role` fields used by
  requests, outages, and monitoring.
- Populate `recipient_roles` on events that historically used
  `NotificationTemplate.register(... roles: ...)`:
  - account lifecycle and expiration/payment events: `account`;
  - account access/security events that used admin role: `admin`;
  - VPS suspend/resume: both `account` and `admin`;
  - VPS/resource/dataset/snapshot/incident/OOM events according to the current
    registered template roles.
- Keep existing domain parameters like request `role=user/admin` and outage
  `role=user/generic` for template selection and detailed filtering.

### Visibility And Candidate Routing

- Add an `Event.visible_to(user)` authorization scope/service. Initially it can
  use current user levels/permissions:
  - direct events: `events.user_id == user.id`;
  - admin-visible events: admin-level users can see every event;
  - system events: admin-level users can see userless/system events;
  - ordinary users do not see other users' events or userless/system events.
- Visibility is evaluated from current permissions, not snapshotted at event
  creation time. If a user's level changes, their event visibility changes with
  it.
- Do not create rows for passive visibility. An admin can list all events
  through the authorization scope without an `event_routing_context`.
- On event emission, route the direct subject event as today when
  `events.user_id` is present.
- For indirect/system routing, find only users with enabled routes that opt into
  indirect or visible/system events, prefiltered by event type/profile where
  possible. Then verify `Event.visible_to?(route_owner, event)` and evaluate
  the route with a route context.
- If no indirect route matches, persist nothing for that route owner. The event
  remains visible through permissions, but it has no per-user routing state.
- Future RBAC should plug into the visibility service and route-context
  relation calculation. It should not require bulk-recipient materialization.

### Routing Engine

- Route in a `RouteContext` containing the event, route owner, subject user,
  and computed subject relation.
- Default routes apply only to `subject_scope = self` direct events.
- Indirect and system events require explicit routes. This prevents admins from
  receiving every event just because they have a default e-mail route.
- Route matchers can use both event fields/parameters and `context.*` fields,
  e.g.:
  - `context.subject_relation == other_user`;
  - `context.subject_relation == self`;
  - `context.subject_relation == system`;
  - `parameters.recipient_roles contains admin`.
- When a route matches, persist an ordered `event_route_match`. When the match
  produces durable per-owner state, create or reuse an
  `event_routing_context` for `[event_id, route_owner_user_id]` and attach
  deliveries to it.
- Combine deliveries across all route owners. Deduplicate by
  `event_routing_context_id`, action, target, template, and state.
- `events.routing_state` remains the event-level summary. The old singular
  `matched_event_route_id` fields are migrated into `event_route_matches` and
  removed from the current schema.
- Increment `event_routes.hit_count` for every matched route in every
  route context.

### E-mail Rendering

- All routed e-mail deliveries should render to the route target only.
  `NotificationTemplate.send_email!` should receive explicit recipients and
  should not include template/global recipients or default user recipients for
  routed deliveries.
- For custom e-mail targets, continue using the custom target address.
- For default-recipient e-mail targets, use the route owner/recipient user, not
  necessarily the event subject user.
- Template variables continue to describe the event subject. For example, an
  operational copy of `user_suspend` to Kerry still renders the suspended user,
  while sending to Kerry's selected target.
- Template language/time zone should keep current event/template behavior for
  compatibility. Operational copies of user messages therefore render like the
  original user-facing message unless a later per-target render preference is
  intentionally added.

### API And WebUI

- Event listing should use `Event.visible_to(current_user)`, not a materialized
  recipient table. Ordinary users list only their own events. Admins list all
  events.
- Expose computed route-context fields on event detail/listing, especially
  `subject_relation`, so the UI can distinguish direct and indirect events.
- Add filters for direct/indirect/system events. For the current permission
  model, indirect means another user's event visible to an admin.
- Admin event listing can inspect all events allowed by admin permissions, and
  should support filtering by subject user and by route owner/delivery owner.
- Nested event deliveries for ordinary users must be restricted to deliveries
  whose `event_routing_context.user_id` is the current user and whose event is
  currently visible to the user. This preserves old BCC privacy after BCC
  copies become separate deliveries and prevents a demoted admin from browsing
  old other-user event delivery rows through the API.
- Expose routing state and matched route only for the current user's
  materialized routing context, if one exists.
- Route forms should support `contains` / `not_contains` for array parameters
  such as `parameters.recipient_roles`.
- Route forms should support context matchers such as direct, other-user, and
  system events.

### Migration From `user_email_role_recipients`

- Backfill each existing `user_email_role_recipients` row into explicit routes
  owned by that user with `subject_scope = self`.
- Use the existing event/template mapping from
  `ADVANCED_NOTIFICATION_EVENT_TEMPLATES` to preserve old behavior exactly,
  especially events that had both `account` and `admin` roles.
- Generated routes should match `parameters.recipient_roles contains <role>`
  plus event-specific filters where needed.
- Keep generated role routes before the default route. Use `continue` between
  multiple generated role routes only when the old recipient resolution would
  have delivered to more than one role recipient for the same event.
- After backfill and verification, remove the API resources, models, specs, and
  table for `user_email_role_recipients`.

### Migration From Template E-mail Recipients

Production inventory showed these active operational recipients:

- monitoring admin templates for monthly traffic and unpaid CPU/data-flow
  alerts to `aither`, `kerry`, and `snajpa`;
- user paid CPU alert copies to `snajpa` and `aither`;
- `daily_report` to `aither`, `kerry`, and `snajpa`;
- `payments_overview` to `aither` and `kerry`;
- account lifecycle and user expiration copies to `vpsadmin@kerrycze.net`.

Migration rules:

- Split every legacy `to`, `cc`, and `bcc` address into individual deliveries.
  Old BCC privacy is preserved by recipient/delivery API filtering, not by
  putting multiple recipients in one SMTP message.
- Resolve each address to a recipient user:
  - if it matches exactly one admin user's current e-mail, use that admin and
    their default e-mail target;
  - if it is an operational alias, use an explicit migration mapping, e.g.
    `vpsadmin@kerrycze.net` owned by Kerry as a verified custom e-mail target;
  - if an address cannot be resolved deterministically, abort the migration or
    report it through a preflight rake task before dropping the old tables.
- For every operational copy, create:
  - a reusable receiver/target for the address if needed;
  - an explicit route owned by the recipient user with the same matcher set and
    linked to that receiver;
  - `subject_scope = visible` with `context.subject_relation == other_user` for
    user/account/resource events about other users;
  - `subject_scope = visible` with `context.subject_relation == system` for
    userless reports.
- Migration/preflight must verify that every resolved operational recipient has
  current admin visibility for the other-user/system route it receives.
- Map each legacy template name to event route filters:
  - `daily_report` -> `system.daily_report`;
  - `payments_overview` -> `payments.overview`;
  - lifecycle templates -> their account lifecycle event types;
  - `expiration_user_active` -> `lifetime.expiration_warning` with
    `parameters.object == user` and `parameters.state == active`;
  - monitoring alert templates -> the existing monitoring event profile
    matchers used by the current migration;
  - user paid CPU copies -> the matching user paid CPU monitoring events.
- Set route `template_name` to the registered generic template id where the
  route needs to force a specific template.
- After backfill and verification, remove:
  - `/email_recipients`;
  - `/notification_templates/:id/email_recipients`;
  - `email_recipients`;
  - `notification_template_email_recipients`;
  - template-recipient inclusion from `NotificationTemplate.send_email!`.

### Direct/System Events

- Userless system events such as `system.daily_report` and
  `payments.overview` should rely on explicit visible/system routes after
  migration.
- Remove the "template recipients" direct-delivery fallback once routes are
  installed.
- If no route matches a userless report event, the event should remain visible
  to users with system-event permissions but have no deliveries, rather than
  silently falling back to removed template recipients.

### Testing

- Model specs for:
  - event visibility by current permissions: ordinary users see their own
    events only, admins see all events, and userless/system events are
    admin-only;
  - visibility changes when user level/permissions change;
  - passive admin visibility creating no materialized routing contexts;
  - subject default route still working as today;
  - default routes not applying to indirect/system events;
  - explicit indirect routes producing routing contexts and deliveries;
  - default e-mail target using the route owner's address, not the subject
    user's address;
  - affected non-admin users not seeing operational-copy delivery rows;
  - context matcher behavior for direct/other-user/system relations;
  - `contains` / `not_contains` matcher behavior on array parameters;
  - role-recipient migration preserving multi-role behavior and default-route
    suppression.
- API specs for:
  - ordinary users listing direct events through `Event.visible_to`;
  - admins listing all events through `Event.visible_to`;
  - direct/indirect/system filters;
  - admin filtering by subject user and delivery/route owner;
  - event delivery output and filtering by routing context owner;
  - demoted admins no longer seeing other-user events or their old other-user
    delivery rows through the API;
  - removed legacy e-mail recipient endpoints.
- Migration specs for:
  - production-shaped `mail_template_recipients` rows;
  - unknown operational recipient preflight failure/reporting;
  - generated direct/indirect/system routes for daily report, payments
    overview, monitoring alerts, paid CPU copies, and lifecycle/expiration
    copies.
- WebUI checks for:
  - direct/indirect/system event filters;
  - route matcher array operators;
  - route context matchers;
  - event detail hiding operational-copy deliveries from ordinary users.

### Deployment And Rollback

- Because vpsAdmin is live infrastructure, prefer a two-step production
  deployment even though the final model removes compatibility surfaces:
  1. additive schema/code: add route subject scopes, route context matchers,
     routing contexts, delivery links, array matchers, and backfilled routes
     while old tables still exist;
  2. destructive cleanup: after verification, remove legacy APIs/code/tables.
- On the current undeployed feature branch, the existing migrations may be
  rewritten before production deployment if that produces a simpler schema.
- Rollback after the destructive cleanup would require restoring the dropped
  legacy tables from backup or a reverse migration that reconstructs them from
  generated routes. Record this explicitly in final deployment notes.
- Also fix the standalone `notification_templates` uploader protocol list so
  it accepts `sms`, matching the API built-in template installer.

## Delivery Rate Limits And Event Noise

This slice adds generic delivery-action rate limits for all current event
delivery methods: `email`, `webhook`, `telegram`, and `sms`.

Design decisions:

- Limits are evaluated per recipient user and delivery method/action.
- Windows are rolling, not calendar aligned, with periods `minute`, `hour`,
  `day`, and `week`.
- Defaults are configured centrally but can be overridden per user/method/
  period by admins. Missing override rows use the configured default.
- Default limits are intentionally generous enough for normal operation but
  small enough to stop accidental notification storms:
  - e-mail: 30/min, 300/hour, 2000/day, 5000/week;
  - webhook: 60/min, 1000/hour, 10000/day, 25000/week;
  - Telegram: 20/min, 200/hour, 1000/day, 2500/week;
  - SMS: 3/min, 30/hour, 150/day, 300/week.
- Dispatchers count started delivery attempts in the relevant rolling window.
  When a limit is reached, the delivery is released again with
  `next_attempt_at` set to the first time enough attempts leave the limiting
  window. No failed attempt is recorded just for waiting on the limiter.
- A per-user/method state row is locked while checking and claiming a delivery
  attempt, so concurrent dispatcher workers cannot all consume the same
  apparent remaining slot.
- WebUI exposes a `Limits` view on the Notifications page and admin member
  pages link to it. Ordinary users can inspect effective limits and usage;
  admins can override limits.
- NixOS module options expose default limits for both API and notification
  dispatchers through the shared notifications configuration.

Event persistence is adjusted at the same time:

- Normal event emission now persists only when routing prepares at least one
  releasable delivery. Events that only match disabled, muted, skipped, or no
  routes are omitted to avoid filling the event log with discovery noise.
- Explicit diagnostic/test events still use `persist: :always`, so users and
  admins can inspect test-event behavior even when a delivery method is
  disabled or no delivery is prepared.
- Route hit counters are updated when a routed event is persisted. Plan-only
  callers do not mutate route metadata unless they opt in explicitly; raw OOM
  report evaluation opts in so suppression routes keep meaningful hit counts
  without persisting the raw event.

Compatibility and deployment notes:

- The schema change is additive: new limit override/state tables and a
  nullable `event_delivery_attempts.recipient_user_id` column with indexes.
- The route-match attribution cleanup is intentionally non-additive in this
  same feature branch. It backfills `event_route_matches` and removes old
  singular matched-route columns that cannot represent multiple continuing
  route matches. API/WebUI/model processes must be activated on this revision
  together with that migration.
- Deploy migrations before starting the new dispatcher code. Old dispatchers
  ignore the new tables/column; new dispatchers need them for counting and
  serialization.
- Rolling back rate-limit code after the additive migration leaves harmless
  extra tables/columns. Attempts written by new code keep a recipient user id,
  but old code can ignore it. Rolling back after the route-match cleanup
  requires migrating down first so old code sees the singular columns again;
  rollback restores only the first recorded match because the old schema cannot
  store all matches.
- Rolling back the persistence behavior means old code may again persist
  skipped-only events; no data migration is required.

The dev-cluster Telegram startup path is also fixed in this slice. When a
token exists under `.dev-cluster/telegram`, `devcluster start` performs a
post-ready services update so the token can enable Telegram services on the
first boot, not only after a later manual update.

## Mailer Node Retirement

The legacy vpsAdmin mailer node is removed from both the dev-cluster topology
and production `vpsfree-cz-configuration`. Event and notification dispatchers
now own new notification delivery. Mailpit remains only as a local/test mail
capture service on the services VM; it is no longer coupled to a `mailer`
container or production mailer host.

Compatibility and deployment notes:

- New direct `TransactionChain#mail` scheduling is intentionally rejected so
  remaining callers are converted to event-backed notifications instead of
  silently depending on a removed node role.
- Historical mail transaction classes remain loadable for existing records.
  There is no database schema change in this slice, but a data migration
  deactivates existing `mailer` role nodes so old mailer rows cannot be
  selected after deployment.
- Event-delivery release transactions select only fresh active node/storage
  transaction runners. This avoids a stale active mailer status row receiving
  new notification-release transactions during mixed deployment.
- Production removes `cz.vpsfree/vpsadmin/int.vpsadmin1` and related database
  and RabbitMQ allowlist entries. A rollback to older code that still expects
  node mail delivery would require restoring that host configuration.
- The running dev cluster must be updated and checked for stale mailer
  containers, stale RabbitMQ mailer consumers/queues, Mailpit health on the
  services VM, and `nodectld` responsiveness on node VMs.

## Open Questions

- Should any event types be mandatory and non-discardable, especially security
  or account-access notifications?
- Where should non-email action templates live long term:
  `vpsadmin`, `vpsfree-mail-templates`, or a renamed/new notification-template
  repository?
- Should admin/system notifications be configurable by admin users in the same
  system now, or left as a follow-up after user-facing events?
- Should Telegram delivery include full incident bodies, or only summaries and
  links by default?
- Which webhook signing format should be standardized for users?

## Migration Retimestamp and Integration Follow-up

- Keep the final event-system migration dependency order, but assign the nine
  unmerged core migrations contiguous versions `20260722120000` through
  `20260722120800`, after current vpsAdmin master.
- Keep retimestamping as one independently reviewable mechanical commit.
  Integration regressions caused by the flat-field/payload contract belong in
  the historical commit that introduced that final contract.
- No production compatibility migration is required because these versions
  have not been merged or deployed. Development databases that recorded the
  old versions must be recreated; do not edit production `schema_migrations`.
- Rebuild the configuration branch on current master with one final generated
  pin per event-system source input. The temporarily disabled shared
  `dev-clusters/vpsadmin/nix/test.nix` wiring remains untouched.

## Time Interval Form Follow-up

- Render the interval time zone with the existing shared WebUI
  `time_zone_options()` generator used by the user-profile form. Preserve the
  target user's time zone as the default, falling back to UTC.
- Separate dynamically repeatable time specifications with a horizontal rule.
  Hide the rule on whichever specification is currently first so adding and
  removing rows preserves the intended visual structure.
- Extend PHP source regression and Playwright coverage for the select control,
  representative IANA options, and dynamic separator visibility. Regenerate
  gettext catalogs and deterministic Czech/English interval screenshots.
- This is a WebUI-only follow-up: there is no API, database, persisted-state,
  protocol, or generated-client change. Mixed-version operation and rollback
  retain the compatibility properties of the existing interval resources.
- Pin only the development `vpsadminServices` channel and the capture
  repository to the final vpsAdmin revision. Production and staging inputs
  remain unchanged. Refresh and verify the complete KB review manifests, but
  do not write to production without direct user approval.

## OOM Report Rule Final Cutover

Requested on 2026-07-23: finish replacing OOM report rules with event routes.
The compatibility fallback is removed in one direct database migration.

Design decisions:

- Move the OOM backfill out of the initial event-table migration into a
  dedicated migration after the complete event-routing schema.
- Convert every legacy rule into an ordered top-level `vps.oom_report` route
  with `vps_id`, `stage = raw`, and `cgroup =*` matchers. Notify rules use the
  generated default receiver; ignore rules use one enabled muted receiver per
  account. Routes stop after the first match and inherit the legacy hit count.
- Insert migrated routes before generated default routes while preserving
  legacy rule ID order per account. The migration writes rows directly, so all
  legacy rules are retained even when the resulting account exceeds the normal
  100-route creation limit.
- Verify that every source rule has a VPS owner, receiver, route, and three
  matchers before deleting legacy data. Then drop `oom_report_rules`,
  `oom_reports.oom_report_rule_id`, and
  `vpses.implicit_oom_report_rule_hit_count`; retain `oom_reports.ignored`.
- Always plan a transient raw OOM event in the supervisor and set `ignored`
  only when the final plan is suppressed by an enabled muted receiver or a
  matching mute interval. Raw planning records route hit counts but does not
  persist event or delivery audit rows.
- Delete the legacy OOM rule model and API resource, the OOM report rule
  relation/filter, the VPS implicit counter, dead WebUI forms/helpers, and
  associated localization/tests. Keep old WebUI `rule_*` URLs as redirects to
  notification routes.
- Regenerate `vpsadmin-go-client` from the resulting API contract. Removing the
  OOM rule resource and fields is an intentional client-breaking change.
- Fix the HaveAPI Go generator so resources or actions named `test` remain
  normal package sources instead of being hidden by Go's `_test.go` filename
  convention. Use a collision-resistant suffix so legitimate sibling API
  names cannot overwrite the rewritten source.

Compatibility and deployment:

- This is an intentional direct cutover. Database migration must run before
  the new API and supervisor processes. Brief mixed-version failures or lost
  OOM reports during deployment are accepted; no expand/contract compatibility
  layer is retained.
- Migration rollback recreates only an empty legacy table and empty legacy
  columns. It cannot reconstruct deleted rule rows, associations, or the
  discarded implicit hit counter; restoring those values requires a database
  backup.
- Accounts migrated above the active-route limit keep all routes and continue
  routing, but cannot create another route until their active count is below
  the limit.
- No vpsAdminOS, RabbitMQ, notification dispatcher, or persisted raw-event
  protocol changes are required.
- The HaveAPI filename fix changes only generated filenames whose unsuffixed
  names would end in `_test.go`; generated Go types and API behavior are
  unchanged. Existing generated clients can adopt it independently.

## Notification Guide Practical Examples

- Rebuild the guarded Czech `navody:notifikace` and English
  `manuals:notifications` candidates around five independent, task-first,
  step-by-step recipes: role-based routing, selected-event muting, Telegram
  delivery, suspension SMS, and a signed webhook.
- Begin with the event → route → receiver → target mental model and then the
  small account-contact receiver used by the first recipe. Retire the
  overwhelming all-routes overview from the article and from release media;
  keep reference material after the practical recipes.
- Keep normal e-mail delivery for role, Telegram, SMS, and webhook examples by
  enabling route continuation. Put mute routes first and disable continuation
  so they also stop later custom and default routes.
- Document exact route selectors and matchers, including transient raw OOM
  matching by VPS, stage, and cgroup; incident matching by VPS and codename;
  `monitoring.*`; suspension event types; and `vps.resources_changed`.
- Use 21 focused tutorial concepts per language to show receiver/target setup,
  each relevant route, and representative route-match results. Together with
  four reference images, each language release contains 25 media objects.
  Fixtures use only reserved/example identities and never contact providers.
- Show a dependency-free Python 3 webhook server that verifies
  `X-VpsAdmin-Signature-256`, prints the event and delivery IDs plus the
  complete JSON shape (including flattened matcher fields), and returns a
  successful 2xx response.
- Test role and mute routing with persisted deterministic fixture events.
  Explain where a generic test event is safe and where a real source object is
  required by Telegram, SMS, or e-mail delivery templates.
- Rebuild the complete guarded candidate trees and checksummed manifests,
  restage both languages in the session-owned KB staging mirror, and leave
  production untouched.
- This slice changes documentation and reproducible captures only. It adds no
  runtime API, schema, protocol, client, or deployment change and remains
  pinned to vpsAdmin revision
  `681a7a41b66dbae3dbdf4f318c45e9aca4489b9f`.

## General Notification Grouping And Single OOM Event

Requested on 2026-07-24: replace the OOM-specific two-stage batching workflow
with reusable Alertmanager-style grouping on event routes.

Design decisions:

- Grouping is explicitly configured on each delivery-producing route with
  `group_by`, `group_wait_seconds`, and `group_interval_seconds`; it is never
  inherited by child routes.
- A route may group on at most ten scalar common or event-specific matcher
  fields. Empty `group_by` groups all events for that route. Pattern and
  catch-all routes may use only common fields.
- Group identity includes the route, route owner/routing context, action,
  destination, template, grouping configuration, and canonical group label
  values. Muted or otherwise skipped routing results never join a group.
- The first pending member waits `group_wait`. Later batches become due at the
  later of `first_member_at + group_wait` and
  `last_sealed_at + group_interval`. Sealed payloads are immutable, retries do
  not absorb new events, and no notification repeats without a new event.
- Routing membership is persisted separately from the outbound delivery.
  Transaction-backed events prepare/release members; dispatchers atomically
  seal due members into one delivery and retain database reconciliation.
- Grouped e-mail, Telegram, and SMS use an event-specific grouped template when
  available and a generic grouped-event template otherwise. Webhooks use one
  versioned `events` array shape for both grouped and ungrouped deliveries.
- `vps.oom_report` represents exactly one persisted OOM report. The `stage`
  field, synthetic notification event, periodic batching transaction, timer,
  and `oom_reports.reported_at` state are removed.
- Migrated OOM rules remain ordered terminal routes. Ignore rules use a mute
  receiver; notify rules use the effective legacy OOM recipient. A grouped
  catch-all route precedes generated defaults. Notify and catch-all routes
  group by `vps_id`, wait 60 seconds initially, and use a three-hour interval.
- The unmerged migrations and branch history will be rewritten so the final
  series introduces only the final schema and protocol. The direct cutover is
  not mixed-version compatible; deploy from a database backup during a
  coordinated maintenance window. Update libnodectld on every affected node
  before grouped routes are enabled, because old node code neither understands
  grouping delivery state 9 nor participates in transaction-chain
  serialization. Then activate the matching API, supervisor, dispatchers,
  WebUI, templates, and configuration together.
- Route-selector cleanup and the broader notification KB article split are
  deferred. The visible WebUI change still requires an updated capture
  contract and screenshots, but no KB page or production wiki write.

Affected repositories:

- `vpsadmin`: schema, routing/grouping, dispatchers, OOM ingress and migration,
  API, WebUI, localization, Nix service configuration, and tests.
- `vpsfree-notification-templates`: generic grouped notification and grouped
  OOM rendering.
- `haveapi`: Go client generation for custom-valued API parameters, including
  grouping field lists and delivery group metadata.
- `vpsadmin-go-client`: generated grouping, membership, and delivery contract.
- `vpsadmin-kb-captures`: exact vpsAdmin pin, grouping controls, deterministic
  fixtures, bilingual captures, and contract validation.
- `vpsfree-cz-configuration`: exact final vpsAdmin services and notification
  template pins through `confctl`.

Verification and review:

- Cover route validation, timing, concurrency, transaction release/abort,
  immutable retries, destination changes, all delivery actions, webhook
  signing, rate limits, OOM ordering/migration, and tenant visibility.
- Run quick component checks and hooks, commit all intended changes, then run
  exactly one fresh standalone mandatory change review before long integration
  tests.
- Regenerate downstream repositories only from the committed final vpsAdmin
  head, monitor GitHub Actions, and record all results in `state.md`.
