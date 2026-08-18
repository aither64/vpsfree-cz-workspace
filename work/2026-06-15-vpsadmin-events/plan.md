# 2026-06-15-vpsadmin-events

## Declarative Event And Delivery Architecture

Requested on 2026-08-03: replace the branch's manually maintained resource and
action policy catalogs, split notification delivery protocols into explicit
classes, and teach the mandatory review to catch the same architecture smells.

Decisions:

- Add vpsAdmin-local DSLs to HaveAPI resources/actions and API operations. Keep
  generated CRUD inference, but colocate exceptional event policy, ownership,
  redaction, cascade and plugin declarations with their owning code.
- Reject missing, duplicate and conflicting declarations at API finalization;
  retain central registries only for authoritative public topics, persisted
  states and protocol identifiers.
- Replace receiver-changing delivery closures with explicit e-mail, webhook,
  Telegram and SMS action classes. Keep routing and dispatch orchestration
  generic and derive delivery metadata from the registered classes. Require a
  closed `DeliveryResult` or generic `DeliveryFailure` at the transport
  boundary so malformed provider results cannot be recorded as success.
- Keep event policy kinds and option combinations closed, validate declared
  redactions against auditable model attributes at catalog finalization, and
  derive external-boundary wrappers from one owner mapping.
- Keep the Nix action selector open to safe registered names. Where Nix must
  duplicate evaluation-time concurrency and rate-limit defaults, emit an
  internal deployment contract and reject drift against the Ruby registry at
  process startup. New actions without Nix overrides use their Ruby defaults.
- Split the event recorders and notification services into focused load units
  after behavior has moved behind explicit interfaces.
- Extend `mandatory-change-review` with source-of-truth, hidden-protocol,
  plugin-ownership and change-locality checks. Validate it independently on the
  current pre-refactor diff before using it for the final review.
- Preserve the existing feature history and add focused refactor commits on
  top. The unrelated one-commit WebUI dependency advance on `origin/master`
  does not justify rewriting the initiative's pinned 111-commit history now.

Compatibility and deployment:

- The architecture refactor changes no schema, persisted values, API/Event
  Type contract, RabbitMQ topology or message, operator-facing configuration
  key/default, rendering, retry/rate-limit or transport behavior.
- A separate functional commit corrects one callback-bypassing cascade:
  deleting an outage or security advisory can now emit the already-public
  `outage_security_advisory.deleted` fact for removed join rows. This is an
  additive event stream correction, not a new event type or message format.
- Generated notification configuration gains an optional internal
  `delivery_contract`. Old processes ignore it; new processes accept it as
  absent and validate it when present. Existing action concurrency and rate
  limits remain unchanged.
- Old and new API/worker processes remain compatible with the same rows and
  queue messages. Mixed versions can consume the additional deletion facts;
  rollback merely stops producing them and has no ordering or data-format
  constraint.
- HaveAPI, generated clients, configuration pins, WebUI and KB content are not
  changed.

Verification:

- Compare Event Type/resource descriptors, policy classifications and delivery
  metadata before and after the refactor in core-only and all-plugin modes.
- Forward-test a syntactically valid new delivery action through Nix worker
  generation and Ruby defaults, and negatively test policy, redaction,
  target-label, result-shape, OAuth wrapper and deployment-contract drift.
- Run focused API specs, RuboCop, selector coverage and Overcommit before the
  mandatory fresh-context review.
- After review, run the full API suite, notification routing/grouping VM tests,
  a bridge-cluster service smoke test and current-head CI.

## KB Home-Page Notification Links

Requested on 2026-08-03: link the pending notification documentation from the
main page of each Knowledge Base under the VPS manuals.

Decisions:

- Add `[[navody:notifikace|Notifikace]]` to the Czech **Návody → Ovládání
  VPS** list immediately after account settings. Add
  `[[manuals:notifications|Notifications]]` to the equivalent English
  **Manuals → VPS** list in the same position.
- Fold the links into a fresh, complete release of the pending notification
  bundle. Both notification roots are still absent from production, so a home
  link must never be published separately from its target article.
- Extend the immutable candidate builder with guarded literal content
  replacements. A Knowledge Base article link is not a vpsAdmin WebUI
  navigation path and must not be represented by a `vpsadmin-nav` annotation.
- Fetch a new all-page production source inventory with exact missing-page
  guards, rebuild both languages, run the annotation checker, and generate new
  checksummed manifests. The expected release contains 12 pages and 31 media
  objects per language.
- Make no screenshot, scenario or capture-metadata changes. Reconcile the
  independent navigation inventory only if the fresh candidate exposes stale
  contract discoveries. Commit and run the mandatory fresh-context review
  before staging.
- Reset only the disposable staging environment owned by this verified
  development session, stage and verify both manifests, and inspect the source
  and rendered home/article pages. Leave staging available for review.
- Do not modify either production wiki without a later, explicit production
  approval for the exact staged manifests.

Compatibility and deployment:

- The home-page changes are guarded by the current production revisions and
  exact adjacent list entries, so concurrent edits fail instead of being
  overwritten.
- Create policies remain in force for every notification article and media
  object. Promotion therefore stops if any target has appeared in production.
- Czech and English releases are independently guarded but form one logical
  documentation release; production promotion must include both reviewed
  manifests.

## Dedicated API RabbitMQ Identity and Infrastructure-First Rollout

Requested on 2026-08-02: keep RabbitMQ topology declaration with the
publishers and consumers, give the API a standalone RabbitMQ identity, deploy
the SMS/Alertmanager/Prometheus infrastructure before vpsAdmin, and reset the
development cluster to validate the final configuration.

Decisions:

- Continue to declare the fixed durable exchange, quorum queues and bindings
  idempotently from the API and notification workers. Do not introduce a
  topology-reconciliation service.
- Reuse RabbitMQ user `api`. It can configure and write the notification
  exchange and fixed queues, but its read permission matches only the source
  exchange required by queue bindings. It cannot consume notification queues.
- Keep the grouper and all action dispatchers on the shared `notification`
  identity. Per-worker identities are outside this change.
- Give the API a dedicated `/private/vpsadmin-api-rabbitmq.pw` secret in
  production. Provision or rotate the broker password operationally; use Nix
  to reconcile only permissions.
- Split production operations into a standalone infrastructure runbook and the
  later maintenance cutover. Upgrade Alertmanager first, then BRQ and PRG APUs,
  then both Prometheus instances. Record one real `sms-aither` proof and stop
  for the operator's decision.
- New Alertmanager is compatible with old Sachet because the additional bearer
  header is ignored. Old Alertmanager is not compatible with the authenticated
  new gateways, so a full rollback restores both APUs before Alertmanager.
- Reset the existing single-node bridge development cluster after review,
  rebuild it from empty MariaDB and RabbitMQ state, prove the API connects as
  `api`, prove workers remain `notification`, and leave the cluster ready.

Compatibility and deployment:

- The identity split introduces no database, API wire, message-format or queue
  topology change. Existing equivalent durable RabbitMQ resources are reused.
- The API user and its permissions can be prepared while the old API is still
  running. Activate the permission reconciler before the new API generation.
- The event-system database migration and rollback boundary remain unchanged.
- Production commands remain operator-run; implementation does not activate
  any production generation.

Verification:

- Cover the permission regex in unit specs, including denied queue reads.
- Build both APIs, all three brokers, both Alertmanagers and both Prometheus
  instances; build APUs where their external SystemRescue ISO input is
  available.
- Strict-build MkDocs and syntax-check every shell example.
- Run the mandatory standalone review before resetting and exercising the
  development cluster end to end.

## Production Deployment Runbook Addendum

Requested on 2026-08-02: start the event-system development cluster and
document everything required for the first production deployment.

Decisions:

- Add a release-specific operations runbook to `vpsfree-cz-configuration`;
  this task documents the rollout but does not update channel pins, secrets,
  RabbitMQ, the production database, or running production machines.
- Treat the schema change as a coordinated maintenance cutover. The old API
  cannot use the renamed mail tables, and the final OOM migration is
  irreversible. Stop all writers and use a pre-migration snapshot as the
  authoritative rollback artifact.
- Supplement the snapshot with a small, checksummed logical export of only the
  destructively changed legacy mail, user setting, mailer Node, VPS, and OOM
  data. Do not take a full logical dump.
- Deploy the new `nodectld` transaction handler to every Node, storage/backup
  host, and DNS consumer before the new API can emit event-delivery release
  handle `9002`. This requires fleet-wide coverage but no vpsAdminOS reboot.
- Create the RabbitMQ `notification` user before broker activation. Reapply
  permissions to `console-router` and every verified live nodectld account
  because the state-file-gated initial setup does not update existing users.
- Reconcile the production proxy's temporary vpsAdmin baseline override before
  rollout. Prepare reviewed maintenance-on and release proxy generations so
  public writes can be closed and reopened with exact, prebuilt closures while
  retaining a known rollback generation.
- Classify every per-user template/role recipient row before migration. The
  event migration deliberately skips disabled-mailer, empty-target, and
  unsupported rows before the source tables are dropped; require explicit
  acceptance or a separately reviewed conversion for every skipped class and
  reconcile all expected new receivers, targets, and routes.
- Deploy and verify both physical SMS gateways before the cutover. Preserve the
  existing sachet/Nexmo Alertmanager fallback.
- During maintenance, drain mail handle `9001`, stop the old mailer, snapshot
  and export the database, activate the database/RabbitMQ configuration, run
  all core and plugin migrations once from the reviewed database package on
  api1, then start api1, api2, and both WebUIs.
- Keep the old mailer container powered off until acceptance. Before traffic
  reopens, rollback means restoring the snapshot and old generations. After
  traffic reopens, prefer a forward fix because snapshot restoration loses new
  writes.

Compatibility and deployment:

- The vpsAdmin services, staging, and production channels must all pin the same
  approved event revision. Managed templates and the SMS gateway must also
  match their reviewed revisions.
- New nodectld code and widened RabbitMQ permissions are backward-compatible
  with the old API and can remain during an application rollback.
- The removed OOM-rule API is a downstream client compatibility break.
  Generated clients and automation updates follow server acceptance.
- Production KB publication remains separately approval-gated.

Verification:

- Start the existing single-node bridge dev cluster without resetting it.
- Verify all event services, API/WebUI HTTPS, all twelve migrations, RabbitMQ
  permissions/resources/connections, and Node/DNS nodectld health.
- Strict-build the MkDocs site, run repository hooks, commit scoped changes,
  and perform the mandatory fresh-context standalone review.
- Validate the proxy input/maintenance sequence, recipient classification
  generators, rollback unmask ordering, and absence of rake-timer activation
  on api2 as part of the review follow-up.

## Report-based muting shortcuts addendum

Requested on 2026-07-31: let users prepare mute routes directly from OOM and
incident reports and from their notification messages, with an optional expiry.

Decisions:

- Add review-first WebUI composers for OOM and incident reports. The composers
  create one top-level, prepended route using the owner's built-in Mute receiver
  and redirect to the ordinary route editor for further tuning.
- OOM routes can match VPS, cgroup, invoking process, and killed process. The
  safe default is VPS plus cgroup. Incident routes can match VPS, IP address,
  codename, and subject; the safe default is VPS plus codename, with IP as the
  fallback when no codename exists.
- Grouped OOM notifications contain one non-mutating link carrying at most the
  displayed report IDs. The composer lets the user select one authorized report
  as the matcher-value source.
- Detail-page links default to the report account. Notification links default
  to the route recipient. Administrators can select the report account or an
  administrator as route owner; ordinary users can act only for themselves.
- Temporary mute presets are one hour, one day (default), one week, one calendar
  month, forever, and a custom local date/time. Ordinary event-route create and
  update operations also gain nullable expiry input. Single-use remains a
  specialized read-only lifecycle property.
- Add mute links to built-in and managed Czech/English e-mail and Telegram
  templates. SMS remains compact and unchanged. GET links never mutate state;
  the CSRF-protected POST creates the complete route and matchers atomically.

Compatibility and deployment:

- The existing event-route schema and router already support `expires_at`; no
  migration is required. Routes created by the new UI remain readable and keep
  expiring after rollback to the existing router.
- `invoked_by_name` is an additive OOM event field. Old producers omit it, so
  only events emitted by updated supervisors can match that optional field;
  all existing routes and events remain valid.
- New templates guard the mute URL and therefore render with an older API.
  Deploy API instances before WebUI instances during a rolling update, then
  deploy the managed templates. No vpsAdminOS-wide coordination is required.
- Regenerate the Go client, pin final vpsAdmin and managed-template revisions
  through `confctl`, and refresh the bilingual WebUI capture/documentation
  contract. Production KB promotion remains separately approval-gated.

Verification:

- Cover API authorization, owner scope, atomic creation, matcher validation,
  limits, prepend ordering, expiry, and actual delivery suppression.
- Cover WebUI defaults, grouped selection, expiry presets, CSRF behavior,
  expired-route rendering, redirects, escaping, and translations.
- Render-check built-in and managed e-mail/Telegram variants, regenerate and
  compile the Go client, rebuild captures/candidates, evaluate deployment
  configuration, and monitor CI.
- Commit all intended changes and run the mandatory fresh-context standalone
  review after quick checks and before long integration tests.

## Concept-First Notification Documentation Addendum

Requested on 2026-07-31: make the bilingual notification articles explain
the event-routing model before asking members to follow delivery recipes.

Decisions:

- Keep `navody:notifikace` and `manuals:notifications` as concise entry
  points. Add focused bilingual references for events, routing and matchers,
  and targets and receivers; keep the existing recipes task-oriented.
- Describe event families and teach the live Event Types view instead of
  copying its deployment- and role-dependent catalog into DokuWiki.
- Separate Event Type catalog visibility from notification roles. Event
  definitions gain an explicit account/admin audience; account-owned OOM,
  incident, monitoring, VPS, and similar types remain visible to ordinary
  users even when their notification role is `admin`. Operator-only types
  remain administrator-only.
- Preserve event roles, default routing, route evaluation, delivery
  authorization, API wire output, and persisted data. The visibility change
  only broadens the ordinary user's Event Types catalog and selectors with
  types that the account can already route.
- Add stable documentation landmarks for Event Types, matcher creation, and
  Test notification. Correct contract paths so list and edit-form navigation
  are distinct.
- Restore a clean basic route-list capture; add Event Types, matcher-form, and
  target-list captures; expand the generic receiver capture to include linked
  targets. Every capture remains deterministic and bilingual.
- Build a fresh guarded candidate/release set rather than overwriting the
  already staged delivery-only bundle. Production remains approval-gated.

Compatibility and deployment:

- There is no schema, generated-client, daemon protocol, node, vpsAdminOS, or
  persistent-format change. Generated resource types inherit their existing
  catalog audience and bundled semantic events declare theirs explicitly.
- Unspecified external event definitions default to administrator-only
  catalog visibility, which is backward compatible and avoids leaking type
  metadata until the extension opts into account visibility.
- A rollback can read and execute routes created for newly visible event
  types; an older WebUI merely stops offering those types in its selector.
- Deploy the matching vpsAdmin API/WebUI revision before publishing KB pages
  that depend on the corrected catalog and documentation landmarks.

Verification:

- Test audience validation and ordinary/support/admin Event Type filtering,
  including OOM, incident, monitoring, and infrastructure-only examples.
- Test WebUI landmarks and ordinary-user exact-type/matcher selection.
- Regenerate and inspect the selected Czech and English notification
  checkpoints, then run the complete capture contract.
- Build, validate, stage, and render-check fresh bilingual guarded releases.
- Run the mandatory standalone fresh-context review after focused commits and
  quick verification, before final staging checks.

## Routing Guide Follow-up

Requested on 2026-07-31 after review of the staged articles: make the matcher
section read as one coherent explanation and restore the grouping and
time-interval material that had been compressed into the overview.

Decisions:

- Keep the notification overview descriptive. Replace the instructional
  "Read these concepts first" wording with a neutral concepts section and
  replace "Advanced options" with a short link to routing features.
- Document matcher operators directly instead of organizing them by a field
  type column. Give `=*` and `!*` explicit glob meanings, show independent
  matcher examples, and state separately that all matchers on one route use
  logical AND.
- Protect literal operators and glob examples with DokuWiki no-format spans
  inside inline code. This prevents `**` from opening bold markup and protects
  comparison operators such as `<=` from typography substitution.
- Put full event-grouping and time-interval sections in the bilingual routing
  article. Cover grouping keys, initial wait, repeat interval, per-route
  ownership, skipped deliveries, group inspection, schedule syntax, boolean
  combination rules, active/mute precedence, and child-route traversal.
- Reuse the existing deterministic grouping and time-interval captures and
  move their semantic page bindings from the overview to the routing guide.
- Rebuild both guarded manifests, run a fresh standalone review, then replace
  and verify the session-owned staging bundle. Production publication remains
  out of scope without direct approval.

Compatibility and deployment:

- This follow-up changes documentation candidates and capture-contract page
  mappings only. It has no schema, API, protocol, generated-client, runtime,
  or persistent-state effect.
- The documented behavior is checked against the existing matcher, grouping,
  and interval implementation at the pinned vpsAdmin revision. Deployment
  ordering and rollback constraints from the concept-first addendum are
  unchanged.

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

## Final History Cleanup

Requested on 2026-07-30: rebase every active event-system branch onto its
current default branch and rewrite unpublished feature history into a clean,
reviewable sequence. Preserve every pre-rewrite tip locally and remotely before
changing a branch.

Decisions:

- Keep HaveAPI's five feature commits individually because three are already
  represented by cherry-picks in the released `v0.29.7`/`v0.29.8` history and
  the remaining two are separate Go-generator corrections. Rebase only the
  development branch; do not rewrite release branches or tags.
- Remove vpsAdmin commits whose files are deleted by the final design, and fold
  directly additive follow-ups into their owning features. Keep the late event
  producer commits separate where transaction completion, resource typing, and
  operation correlation have real replay-order dependencies.
- Store the generated Go client in one commit so consumers never see
  intermediary schemas.
- Keep the KB history as four layers: exact vpsAdmin pin, routes and intervals,
  practical recipes, and the final capture/contract refresh.
- Keep generated configuration pins as standalone `confctl` commits. Combine
  the three grouped-OOM follow-ups into one deployment-policy commit.
- Preserve the released HaveAPI branch/tag, standalone PHP client release, and
  SMS gateway default branch. They are inputs to the final stack, not rewrite
  targets.

Compatibility:

- Rewriting commit identities does not change the final application, template,
  generated-client, or capture-contract content. Downstream exact pins must be
  regenerated to the rewritten source commits before deployment.
- Default-branch dependency updates are accepted as part of each rebase and
  verified through repository tests and CI.
- The event schema and migration contract remain the same as the backed-up
  implementation. Disposable development databases should be reset rather
  than adding guards for superseded in-branch migration shapes.
- Production KB content is not changed by this cleanup. The capture repository
  continues to prepare reviewable local artifacts only.

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

## Shared Notification Groups And Route UX

Requested on 2026-07-25: make grouping an action-neutral routing decision,
move group coordination out of action dispatchers, simplify route management,
and provision the vpsFree.cz OOM policy outside core vpsAdmin.

This section supersedes the action-specific group identity and dispatcher
coordination described above.

Design decisions:

- One route match produces one logical group per route, routing owner,
  receiver, grouping configuration, and canonical group label set. The group
  does not include the delivery action or destination in its identity.
- Every surviving receiver target receives the same logical batch. Each target
  keeps its own stream key, payload snapshot, attempt history, retry schedule,
  rate limits, and failure outcome. Receiver or target edits intentionally form
  a new group identity so an already-open group keeps its original fan-out.
- A dedicated notification grouper consumes a durable RabbitMQ grouping queue
  and also reconciles due database state. It activates all target streams for
  an event together, seals one leader per stream from the same event set, and
  releases all leaders together to the existing action queues.
- The grouper is safe to run concurrently on both API hosts. Database unique
  constraints and row locks provide coordination; no singleton lease or
  leader-election service is introduced. If all groupers are unavailable,
  grouped notifications wait while ungrouped action delivery continues.
- Action dispatchers no longer decide group membership or seal groups. They
  lazily prepare their stream's immutable payload after claiming a released
  grouped leader, so preparation or delivery failure affects only that stream.
- New routes without an explicit position are prepended at their level.
  Explicit positions and subroute parents remain unchanged.
- Core vpsAdmin no longer creates or repairs a special OOM route. The
  vpsFree.cz configuration user-create hook idempotently creates an ordinary
  exact `vps.oom_report` route named `OOM report notifications`, copies the
  generated administrator route's receiver, groups by `vps_id`, waits 60
  seconds, uses a three-hour group interval, and prepends the route.
- During a rolling core/configuration transition, the hook accepts a matching
  route already created by the old core. Existing accounts continue to receive
  the migration-created route; users may later edit or delete the hook-created
  route without it being recreated.
- Route creation in the WebUI contains only ordinary route fields. Route
  details show grouping in a separate form. The route list is reduced to seven
  compact columns: ordering, route, conditions, receiver, behavior, hits, and
  actions.

Compatibility and deployment:

- The event schema is still unmerged, so the original migration is rewritten
  to add the internal stream key and remove the action from delivery groups.
  The development database must be rebuilt. Production remains a coordinated
  migration-window deployment from backup as already documented.
- The RabbitMQ grouping queue is additive. New publishers and groupers must be
  deployed with the rewritten schema; old action dispatchers must not run
  against it. The service module starts one grouper on every host where the
  notification dispatcher is enabled.
- Fresh RabbitMQ clusters receive the grouping-queue permission from
  vpsAdmin's initialization tool. Existing vpsFree.cz clusters retain their
  one-time initialization marker, so production configuration also reconciles
  the notification user's permissions on every RabbitMQ node after the broker
  and its initial setup unit. Deploy RabbitMQ nodes before enabling groupers on
  API hosts.
- The configuration hook is mixed-version safe with the preceding core route
  creation behavior and does not depend on vpsFree.cz-specific constants in
  the new core.
- No public event or delivery payload shape changes. The stream key remains an
  internal persistence detail. `EventRoute` gains the additive, read-only
  `matcher_count` field used by the compact WebUI summary; existing clients can
  ignore it. All protocols receive the same logical event membership, although
  protocol-specific size limits may render different truncation summaries.

Affected repositories:

- `vpsadmin`: schema, routing plans, grouping queue and service, action
  dispatchers, route ordering, removal of the core OOM default, WebUI,
  localization, Nix service health, and tests.
- `vpsfree-cz-configuration`: idempotent new-user OOM route hook and exact
  final vpsAdmin pin.
- `vpsadmin-kb-captures`: exact final vpsAdmin pin, compact route-list and
  standalone-grouping capture, bilingual generated images, and contract
  validation. The broad route-list capture stays retired; the grouping form
  has its own semantic documentation control.

Verification:

- Cover shared cross-action membership, independent preparation failure,
  receiver edits, concurrent groupers, missing RabbitMQ wakeups, route
  prepend ordering, core default removal, configuration-hook idempotence, and
  WebUI form/list regressions.
- Run quick checks and repository hooks, commit the intended changes, then
  perform a fresh standalone mandatory change review before long integration.
- Rebuild the development cluster on the bridge network for the rewritten
  migration, run focused API/WebUI/service and OOM integration checks, push
  exact heads, update configuration and capture pins, regenerate bilingual
  captures, and monitor current-head GitHub Actions.

## Notification Group Observability And Route Form Guidance

Requested on 2026-07-25: expose reusable notification groups directly in the
API and WebUI, and finish the compact route/grouping form usability work.

Design decisions:

- Route owners can list and inspect their own logical notification groups;
  administrators can inspect all groups. The list defaults to open groups
  while filters retain access to overdue, idle, and all reusable groups.
- A group is a reusable bucket rather than one immutable batch. Its state is
  `waiting`, `overdue`, or `idle`; group detail shows the current pending
  events and links to the complete event and, for administrators, delivery
  history.
- The group API records the receiver directly, publishes route/owner/receiver
  identity, labels, timing, aggregate event/stream counts, actions, and state,
  and adds group filters to event and administrative delivery indexes.
- Event field metadata identifies common and groupable fields. Exact routes
  may group by scalar fields for that event type; wildcard and catch-all routes
  may group only by common scalar fields. List fields remain invalid.
- Every editable route and grouping parameter receives localized HaveAPI
  descriptions. WebUI-specific Event Types links are appended by the WebUI,
  while the API descriptions remain presentation-neutral plain text.
- The grouping explanation is the first row of the standalone grouping form
  and spans all three label/input/description columns.
- Route and subroute tables use separate narrow Add subroute and Delete icon
  columns. The retired broad route-list KB screenshot stays retired.
- Dedicated Prometheus/service metrics and group-retention policy are deferred;
  this slice provides API/WebUI observability and keeps existing systemd and
  RabbitMQ monitoring.

Affected repositories:

- `vpsadmin`: group schema/model/API, event metadata, WebUI, localization, and
  tests.
- `vpsadmin-go-client`: regenerated additive group and filter API.
- `vpsadmin-kb-captures`: exact vpsAdmin pin and refreshed bilingual route and
  grouping form captures.
- `vpsfree-cz-configuration`: exact generated vpsAdmin services pin.

Compatibility and verification:

- The events schema remains unmerged, so the initial events migration is
  updated in place and development databases must be rebuilt. Production keeps
  the existing coordinated maintenance-window deployment requirement.
- The API changes are additive. Existing grouping and delivery behavior is
  unchanged, and existing clients may ignore the new resource and metadata.
- Cover group state, aggregates, tenant isolation, event/delivery filters,
  route action columns, API-driven descriptions, groupable field selection,
  localized captures, generated-client compilation, and browser group
  lifecycle inspection.
- Commit all intended repositories after quick checks, run the mandatory fresh
  standalone review, then rebuild the owned bridge-network development cluster
  and run longer integration checks.

## Strict Draft Migrations, Existing OOM Defaults, And Split KB Guide

Requested on 2026-07-25: finish the existing-account OOM default, remove
development-database compatibility guards from the unreleased migration chain,
and turn the notification guide into a reference page with standalone examples.

This section supersedes the earlier combined notification-guide recipe and all
remaining references to an OOM event `stage` field.

Design decisions:

- The unreleased `2026072212*` migration chain assumes exactly the schema
  produced by its immediately preceding migration. It does not probe for
  tables, columns, or indexes to accommodate stale disposable databases.
  Development databases are reset after migration rewrites.
- Data-conversion validation remains strict. In particular, the final OOM
  migration refuses to delete legacy data unless every existing account has
  the generated administrator route and receiver required for its grouped
  catch-all OOM route.
- The migration creates the ordinary grouped `vps.oom_report` catch-all for
  every account that exists at migration time, including accounts without
  legacy OOM rules. The vpsFree.cz configuration hook remains responsible only
  for accounts created later.
- The vpsFree.cz OOM-default helper is one idempotent configuration fragment
  shared by the user-create hook and the disposable development seed. The seed
  loads it only when a configuration source is mounted, then reconciles every
  seeded user after default receivers and routes exist. This is development
  wiring, not a recurring production repair job.
- Route and subroute tables keep separate Add-subroute and Delete action
  columns, but both column headers are empty because the icon links already
  carry accessible titles.
- `navody:notifikace` and `manuals:notifications` become reference pages for
  routes, receivers, grouping, time intervals, group observability, and
  delivery inspection. They link to six independent bilingual tutorials:
  event-role routing, OOM muting, incident muting, Telegram delivery, suspension
  SMS, and a signed webhook.
- Tutorial progress uses explicit `Krok/Step N` headings, so screenshots cannot
  reset ordered-list numbering. OOM and incident muting are separate pages.
- OOM matching uses the single persisted `vps.oom_report` event with `vps_id`
  and `cgroup`; no `stage = raw` matcher or two-stage event is documented.
- The webhook example consumes the version-1 `group`, `events`, and `delivery`
  payload shared by grouped and ungrouped notifications. It verifies the HMAC
  over the original body and treats signed `delivery.id` as the idempotency
  key.
- Existing route-specific tutorial images and the standalone grouping-form
  image are regenerated from the final vpsAdmin revision. The retired broad
  route-list screenshot remains excluded.

Compatibility and deployment:

- No released predecessor schema is added by these migration edits. The
  production cutover and backup requirements described for the event system
  are unchanged; only disposable databases created from an older draft chain
  need resetting.
- Existing production accounts receive their grouped OOM route from the data
  migration. New accounts receive the same route from the configuration hook.
  The helper accepts a matching active route and does not overwrite user edits.
- The development seed is conditional on the mounted vpsFree.cz configuration,
  so generic vpsAdmin development clusters retain their existing behavior.
- KB pages and media are staged at their final page IDs in the session-owned
  mirror. Production wiki writes remain forbidden without a later direct user
  approval.

Verification:

- Cover strict predecessor migration behavior, migration refusal when an
  existing user lacks defaults, grouped catch-all creation for users without
  legacy rules, helper idempotence and exact route attributes, compact empty
  action headers, annotation/capture contracts, rendered bilingual pages, and
  the reset bridge-network development seed.
- Commit quick-verified changes and exact downstream pins, then run one fresh
  standalone mandatory change review before starting a new long integration
  run. The already-running superseded-head integration run is allowed to
  finish and its result is recorded before any branch update.

## User-Facing KB Corrections And Verifiable Examples

Requested on 2026-07-26: correct the staged notification documentation and
route list, and make both KB code samples and generated HaveAPI examples
verifiable.

Design decisions:

- Notification KB pages describe only facilities available to ordinary users.
  Administrator delivery queues and logs are not mentioned.
- Event roles describe the intended audience, not vpsAdmin permissions.
  `account` covers membership, payment, account lifecycle, request, and account
  security events. `admin` covers VPS operation, configuration, monitoring,
  incident, OOM, migration, and backup events. Event types remain the
  authoritative inventory and an event may have both roles.
- Newly created top-level routes and subroutes are prepended. Tutorials do not
  instruct users to move them; they explain only the relevant `Continue`
  behavior.
- DokuWiki list items in the notification pages stay on one physical source
  line. Candidate and rendered-page checks verify that list text remains
  inside the expected list item.
- The route list has four data columns followed by separate Edit, Add
  subroute, and Delete columns. All three action headers are empty. Browser
  auto-layout sizes the table; fixed percentage widths are removed.
- Canonical runnable notification examples live with vpsAdmin. The bilingual
  KB contract references the same files and refuses unresolved or divergent
  samples.
- The documented Python webhook receiver is covered with valid single/grouped
  requests and invalid signature/delivery-ID cases, then used by the real
  notification-routing integration test.
- HaveAPI validates structured documentation examples against action metadata
  and syntax-checks generated Ruby, JavaScript, PHP, shell, curl, and HTTP
  fragments. Arbitrary mutating examples are not executed against shared
  infrastructure.
- The HaveAPI changes are released as the next 0.29 patch and consumed by
  vpsAdmin. Package publication and production KB promotion retain their
  explicit approval gates.

Affected components for this addendum:

- `haveapi`: structured example validation, generated-fragment syntax checks,
  and the coordinated 0.29.7 release.
- `haveapi-client-php`: standalone Composer mirror and matching 0.29.7 tag.
- `vpsadmin`: canonical examples, published HaveAPI dependencies, API metadata,
  route-table actions, tests, and integration coverage.
- `vpsadmin-kb-captures`: updated route-table contract and regenerated
  screenshots pinned to the final vpsAdmin revision.
- Top-level workspace tooling and KB candidates: canonical code injection,
  list-shape checks, bilingual content, and staged manifests.

Compatibility and deployment:

- There is no notification protocol or database change. Webhook version 1
  continues to use the `events` array for single and grouped deliveries.
- HaveAPI gains stricter developer-facing example validation. Invalid examples
  fail API definition validation with their resource, action, and title;
  public API requests and responses are unchanged.
- HaveAPI must be released before the final vpsAdmin dependency update.
  Capture and production-configuration pins are updated only after the final
  vpsAdmin revision is fixed.

Verification:

- Cover malformed example layouts, unknown fields, required inputs, path
  parameters, primitive/resource shapes, prose-only examples, and syntax for
  every generated client style.
- Cover the human-friendly routing-state label, seven-column route tables,
  compact action columns, explicit edit links, and viewport overflow in PHP
  and Playwright tests.
- Parse all KB JSON/shell/Python samples, validate event fixtures against event
  metadata, verify canonical sample identity in both languages, and inspect
  the rendered list DOM on staging.
- After quick checks and focused commits, run one mandatory fresh standalone
  review before renewed exact-head integration tests.

## Complete Audit Event Coverage Addendum

Requested on 2026-07-28: extend the event system from notification-oriented
coverage to a reconstructible audit stream. Every logical mutating API
operation must have either an audit declaration or a documented exemption.
Sensitive access operations and background/system transitions also require
events even when they are not CRUD actions.

### Current behavior and correctness constraints

- `Events.emit!` defaults to persistence only when at least one route matches.
  Audit facts must persist independently of notification routing.
- `Event.user_id` currently identifies the affected owner/audience, not the
  actor. It cannot distinguish an account action, an administrator acting for
  that account, an impersonated session, a node, or a background task.
- `TransactionChain.fire2` constructs the chain and provisional objects in a
  database transaction. An exception from `link_chain` rolls back the chain,
  transactions, confirmations, provisional objects, and audit intent. This is
  the correct boundary for the requirement that a rejected chain creation
  emits no event.
- Successful node confirmations and the terminal chain state are committed in
  one database transaction. This is the first safe point for facts named
  `created`, `updated`, or `deleted`.
- A failed `confirm_create` removes the provisional row, failed `edit_before`
  restores the old values, `edit_after` applies only on success, and destroy
  confirmation deletes only on success.
- Existing `route_event!` calls persist past-tense events while the chain is
  still being assembled. Aborting an unsent delivery on later failure cannot
  retract the Event row or a delivery that ran before a later transaction.
- `rollbacking` is intermediate, `failed` means rollback completed, and
  `fatal` means rollback itself failed. `resolved` is an administrator
  acknowledgement of a failure, not a successful outcome. The current event
  helper's terminal/success calculation must be corrected accordingly.
- A chain can reach `done` with failed `keep_going` transactions. The
  operation declaration must state which transactions determine domain
  success; the chain result may also be reported as completed with warnings.
- Retrying currently rewrites the same chain and transaction state. An
  immutable attempt/run identity is required to retain failure followed by a
  successful retry.
- RabbitMQ publications happen after database commits and may be dropped.
  Broker messages can wake a projector, but cannot be the durable audit
  source.
- `allow_empty` chains can commit synchronous changes and then discard the
  empty chain. Audit finalization must preserve the operation without creating
  a synthetic notification transaction or requiring a surviving chain row.
- Some link methods commit auxiliary synchronous changes before asynchronous
  execution, for example VPS destruction removes selected auxiliary rows.
  Those changes need their own facts or must eventually move behind
  confirmations; a generic failure event must not claim a complete rollback
  when that is not true.

### Audit operation and event lifecycle

Use an explicit logical-operation declaration instead of inferring public
semantics from low-level confirmation rows:

```text
API/background request
  -> construct mutation and AuditOperation in one transaction
     -> construction error: both roll back, no event
     -> synchronous/allow-empty success: finalize in that transaction
     -> queued chain: persist an honest requested event
        -> done: emit the past-tense success fact
        -> failed: emit operation failure after rollback
        -> fatal: emit failure with rollback_failed
        -> retry: create a new immutable attempt
```

For example:

- `vps.create_requested` means a durable request and provisional target were
  accepted. It does not claim the VPS exists.
- `vps.created` is emitted exactly once after successful create confirmation.
- `vps.create_failed` is emitted after failed/fatal execution with an immutable
  target snapshot, even when confirmation removed the provisional VPS.
- A link-time exception emits none of these because the operation did not
  become durable.

Keep generic, always-persisted transaction-chain/run state events for
diagnostics and correlation. Domain event types remain the stable audit
interface; consumers should not have to reverse-map low-level transaction
names to discover that a VPS creation failed.

### Data model

Add an `AuditOperation`-style model with:

- stable operation ID, operation name, ordinal, requested time, and outcome;
- optional transaction-chain ID and immutable execution-attempt/run ID;
- intended requested, success, and failure event types;
- subject class/ID plus immutable label and owner snapshots;
- explicitly allowlisted before/after values and changed fields;
- effective account, actual actor, impersonating administrator, session,
  authentication type, client/API IPs, user agent, request/action name, and
  request/correlation ID;
- failure class and bounded/redacted summary, rollback outcome, and failed
  noncritical transaction IDs;
- accepted and terminal Event IDs and an idempotency key.

The operation is created inside the same transaction as chain construction.
Its chain relation must be optional and must not cascade away when an allowed
empty chain is discarded. Enforce uniqueness for the operation key and for
each `(operation, attempt, phase)` event.

Extend Event, or add a normalized companion context/audience model, so the API
can filter by actor, subject, operation, chain, and correlation ID. Keep
affected owner/audience distinct from actor. Cross-owner swap, clone,
ownership-transfer, and administrator actions need either multiple audience
rows or owner-visible events sharing one operation ID.

Deleted targets must remain understandable without resolving a live foreign
key. Store immutable subject and owner labels on the operation/event.
Historical users and sessions can also disappear, so snapshot the identifying
actor fields in addition to retaining nullable references.

Add immutable `TransactionChainRun` and append-only
`TransactionChainStateChange`/outbox rows. Every state transition writer,
including NodeCtld terminal transitions, writes the row in the same database
transaction as chain state and confirmations. The API projector claims rows
under a lock, creates Events idempotently, and marks rows projected in the same
transaction. RabbitMQ is only a wakeup; periodic reconciliation handles lost
wakeups. Stale and duplicate messages are rejected by run and sequence.

For synchronous mutations, persist the domain change, operation, and terminal
Event in one ActiveRecord transaction. Prepare/release notification delivery
only after commit. A plain `after_commit` callback without an outbox is not a
complete durability mechanism.

Audit persistence uses an explicit `persist: :always`/`audit: true` path.
Routing remains optional and must not control whether the fact exists.
Creating, routing, dispatching, or retrying an audit Event must not recursively
audit internal Event delivery rows.

### Actor, payload, and retention policy

Use a common audit envelope across all event types:

- operation ID/name/phase, event occurrence time, and recording time;
- subject type/ID/label and affected owner snapshot;
- actor kind (`user`, `system`, `anonymous`, or `node`), effective user,
  impersonating administrator, session/authentication context, and source;
- request/action/correlation/chain/run IDs;
- changed-field names and an explicitly allowlisted before/after map;
- outcome, reason, and bounded failure metadata.

Never persist passwords, console/access/refresh/verification/pairing tokens,
TOTP or TSIG secrets, OAuth client secrets, signing-key passphrases, private
key material, raw public-key bodies, webhook secrets, raw user data, or secret
system-configuration values. Use IDs, booleans, content hashes, or
non-reversible fingerprints where correlation is useful.

Audit retention is independent of notification delivery retention. Define the
retention/index/partition policy before enabling high-volume sources. There is
no claim of complete historical coverage before the deployment marker; any
best-effort import from `ObjectHistory` must be labeled as such.

### P0 VPS event coverage

Primary VPS actions:

- create: `vps.create_requested`, `vps.created`, `vps.create_failed`;
- general update: `vps.update_requested`, `vps.updated`,
  `vps.update_failed`, with safe changed fields for hostname, template,
  resolver, namespace/map mode, resources, start menu, autostart, network,
  owner, cgroup, and administrator flags;
- lifecycle: `vps.suspended`, `vps.resumed`, `vps.soft_deleted`,
  `vps.revived`, `vps.destroyed`, plus the matching failed operation event and
  old/new state and trigger;
- runtime actions: start, stop, restart, rescue/template boot, and their
  failures;
- reinstall, restore, migration, clone, swap, and replacement, each with
  requested, terminal success, and failure facts;
- root-password change, SSH public-key deployment, and user-data deployment,
  recording only generated/provided mode, key ID/label/fingerprint, or data
  ID/label/format/digest;
- feature changes, mount create/update/delete, and maintenance-window changes;
- ownership changes and cross-VPS operations use shared operation IDs and
  correct visibility for every affected owner.

Existing `vps.replaced` and migration-finished events move from link time to
terminal success. Existing migration-planned/begun events remain milestones
only if their names and payload clearly describe an intermediate fact.
`vps.resources_changed` must cover every resource change, not only changes
having `change_reason`. Direct VPS resolver selection and resolver-object
configuration changes are separate facts.

Related VPS network/storage coverage:

- network-interface update;
- IP and host-IP create/update/delete/assign/unassign;
- reverse-DNS update;
- dataset create/update/delete/property inheritance;
- snapshot create/delete/rollback and VPS restore;
- backup request/success/failure;
- snapshot-download request/ready/failure/delete/expiry;
- dataset migration, expansion, shrink, and over-quota failures.

Background/runtime coverage:

- expiration setting changed and expiration reached;
- the lifecycle operation initiated by expiration, with `system` actor and
  scheduler reason;
- unsolicited node-reported halt, reboot, OOMD stop, and OOMD restart;
- automatic quota, dataset-expansion, OS-release, and autostart changes with
  component/task attribution.

### VPS console events

Token lifecycle and actual console use are different:

- API token operations: `vps.console_access.issued`,
  `vps.console_access.reused`, `vps.console_access.revoked`, and
  `vps.console_access.expired`; never include the token.
- Actual use: `vps.console_session.opened` and
  `vps.console_session.closed`, one per authenticated client session, with a
  generated non-secret session ID, VPS/user/console row/node IDs, timestamps,
  duration, router-observed IP when available, and close reason.

The authoritative open/close point is the NodeCtld console server, not the API
token row or console-router cache. Persist session lifecycle/outbox state so a
node or broker crash does not lose events. Add an additive console
authentication RPC returning VPS, user, and console-row IDs; deploy the API
method before nodes use it and retain the old method during mixed-version
operation.

Close reasons include explicit user/admin revoke, disconnect, idle expiry,
token expiry, VPS state change, console process exit, service shutdown, and
node loss. Current token revocation does not terminate an authenticated
session, so truthful revoked-close events require a revocation channel or
periodic revalidation. An expiry/reconciliation task must close sessions left
open by crashes.

### P0 cross-cutting and security coverage

Instrument common facilities once:

- `lifetime.state_changed` and `lifetime.expiration_changed` for User, VPS,
  Dataset, Export, Mount, and SnapshotDownload;
- `maintenance.locked` and `maintenance.unlocked` for cluster, environment,
  location, node, pool, and VPS;
- user update/password/authentication-setting changes;
- user sessions, OAuth authorizations, remembered devices, TOTP devices,
  WebAuthn credentials, public keys, metrics access tokens, OAuth clients, and
  transaction-signing-key unlock;
- user allocation/resource/package assignment changes;
- notification targets, receivers/actions, receiver-target links, event
  routes/matchers/time intervals, notification templates/variants, and
  explicit delivery retry requests.

Session/token events include IDs, labels, authentication type, scope, client,
safe network/user-agent context, close reason, and actor, but never bearer
material. Do not emit public audit events for renewable-token extension,
`last_seen_at`, or use counters.

Notification configuration events are security-relevant because they change
where audit and account messages are delivered. Target secrets, verification
codes, webhook credentials, and full template bodies remain redacted; record
content revision/hash where needed.

### P1 infrastructure, storage, and plugin coverage

Add logical CRUD/action events for:

- locations and location-network policy;
- networks, IP addresses, host IP addresses, interfaces, nodes, node transfer
  connections, evacuations, clusters, cluster resources/packages/defaults,
  and user namespace maps;
- DNS zones, records including authenticated dynamic updates, resolvers,
  servers, server-zone links, TSIG keys, and zone-transfer configuration;
- environments, OS families/templates, pools, datasets/snapshots/exports,
  expansion requests, and migration plans;
- payments and incoming-payment state, retaining `payment.accepted` with the
  correct user/system actor;
- requests, with the actual approve/deny/ignore/correction resolution rather
  than the current generic `resolve`, and correlated `user.updated` on
  approved change requests;
- outages, affected objects, entities, handlers, updates, and advisory links;
  audit persistence must not depend on `send_mail`;
- monitoring acknowledge/ignore actions, without logging every sample;
- security-advisory draft/publish/update/CVE/node-status actions and incident
  creation;
- system configuration, mailboxes/handlers, news log, help boxes, and WebUI
  user settings, with strict configuration-value allowlists.

This inventory is intentionally logical rather than one Event for every
internal row. Existing notification events such as DNS transfer
failed/recovered, snapshot download ready, OOM reports, incidents, outage
announcements, and monitoring detected/resolved alerts remain, but become
always-persisted audit facts where appropriate and receive the common actor,
subject, and correlation envelope.

### Explicit exemptions

Require an `audit_exempt` declaration with a reason for intentionally noisy or
internal rows:

- Event routing/delivery attempt/group/context/match internals, except an
  explicit user/admin retry request;
- transaction rows and confirmation rows, while preserving chain/run state
  and logical outcomes;
- maintenance/resource lock implementation rows, represented by semantic
  lock/unlock facts;
- raw token/challenge/user-agent/failed-login and rate-limit counter rows;
- session renewal, touch/last-seen, use counters, accounting, monitoring
  samples, process/status metrics, node evidence, and polling/progress rows;
- dataset/snapshot pool-placement, branch/clone/property-history and expansion
  queue implementation rows;
- generated DNSSEC and transfer-log rows;
- OOM usage/stat/task/counter and mail-log rows;
- automatically rebuilt advisory/outage joins, represented by one rebuild
  summary.

### Coverage enforcement

Extend the vpsAdmin action DSL with an explicit audit declaration for each
mutating action, for example a synchronous event or a transaction-chain
operation mapping. Sensitive read/access actions such as console and snapshot
download are declared explicitly too.

A definition/spec check enumerates POST/PUT/PATCH/DELETE HaveAPI actions and
fails when an action has neither `audit` nor `audit_exempt(reason:)`.
Top-level transaction chains similarly declare their logical operation;
nested `use_chain` calls inherit/correlate with that operation so internal
start/stop steps during create or reinstall do not masquerade as independent
user actions.

Use `ObjectHistory` as a comparison oracle during conversion, especially for
VPS changes, but not as the audit API. It lacks failed attempts and broad
non-VPS coverage.

### Implementation sequence

1. Add the common audit envelope, audience/subject snapshots, always-persist
   emitter, idempotency, and coverage declaration/exemption framework.
2. Add immutable operation intents, chain runs, durable state-change outbox,
   projector/reconciliation, and correct state semantics. Cover synchronous
   and `allow_empty` finalization.
3. Convert existing link-time past-tense events to terminal projection and
   harden existing event types without changing notification meaning.
4. Cover primary VPS CRUD/lifecycle/runtime and complex operations first.
5. Cover console, VPS-associated network/storage, expiration, and node/runtime
   sources.
6. Cover account/security and notification-routing configuration.
7. Cover infrastructure, DNS, storage, plugins, and lower-priority
   administrative/UI configuration; finish the exemption manifest.
8. Update generated clients, Event/Event Types API and WebUI, the independent
   capture/documentation contract, and production configuration pins.

Keep commits reviewable by separating schema/foundation, chain projection,
VPS families, other resource families, generated clients, WebUI/docs, and
configuration pins. Run mandatory change review after the intended commits and
quick verification, before long integration tests.

### Verification

Foundation and transaction tests:

- link-time failure and an outer transaction rollback leave no object, chain,
  operation, or Event;
- successful create emits exactly one `created` after confirmation;
- failed/fatal create removes the provisional object, preserves its snapshot,
  emits one failure, and never emits `created`;
- failed update restores old values and emits no successful update;
- successful delete remains understandable after the target row is gone;
- synchronous and allowed-empty changes commit mutation and Event atomically;
- no terminal notification is deliverable before terminal confirmation;
- `done` with failed `keep_going` work reports warnings according to declared
  domain-success criteria;
- failed attempt, retry, and success preserve both immutable run outcomes;
- `resolved` never becomes success;
- lost wakeups, duplicate/stale broker messages, crashes, and concurrent
  projectors remain idempotent and recover by reconciliation.

Coverage and security tests:

- every mutating API action has an audit declaration or reasoned exemption;
- ordinary user, administrator-on-behalf-of-user, impersonated, anonymous,
  node, and background actors are attributed correctly;
- owner visibility is correct for transfer, clone, swap, and admin actions;
- audit persistence succeeds with no matching route;
- secret fixtures never appear in payload, delivery snapshots, or failure
  summaries;
- console covers concurrent sessions, revoke, idle/token expiry, disconnect,
  process death, service shutdown, and node-loss reconciliation;
- existing notification routes fire only for the intended phase, normally
  terminal semantic success or explicit failure, not provisional intent.

### Compatibility and deployment

- Schema and API changes are additive. The current event migrations are still
  unreleased development history, so amend the draft migration chain rather
  than adding existence guards for stale disposable databases; reset those
  databases.
- Do not reorder the existing transaction-chain state enum. Add run/sequence
  data around it and fix `resolved` interpretation.
- Deploy schema, API projector/reconciliation, and the additive console RPC
  before updated NodeCtld/console producers. Retain old RPC behavior during a
  mixed-version window. Exact transition history is guaranteed only after all
  producers write the durable outbox; record that audit-coverage start marker.
- Old application versions ignore additive audit tables. Rolling back after
  new events exist must preserve them for forward recovery. A rollback may
  temporarily stop projection but must not discard operation/outbox data.
- Event type and field additions are API-compatible for generated clients.
  Consumers must tolerate new event types. Any pagination/retention behavior
  is documented before production use.
- Event Types/Event Log and visible WebUI changes require the canonical
  `vpsadmin-kb-captures` WebUI documentation workflow and exact downstream
  pins. Production KB publication remains separately approval-gated.

## 2026-07-28 Scope Correction: Consumer Events, Not An Audit Ledger

The complete-audit addendum above over-interpreted the request. It is
superseded for implementation by this section.

The requested outcome is additional ordinary vpsAdmin events. Consumers can
persist those events and construct their own audit logs. vpsAdmin will not add
an internal audit-operation ledger, actor/audience tables, transaction-chain
run or state-change outbox tables, console-session fact tables, or an audit
coverage DSL.

Implementation boundaries:

- use the existing `Event` model, event definition DSL, Event API, and routing
  system without schema changes;
- persist audit-relevant events even when no notification route matches, so
  Event API consumers can observe them;
- emit synchronous mutation events only after the mutation succeeds, in the
  same database transaction where practical;
- emit transaction-chain success only from the existing `done` state
  notification, and failure from existing `failed` or `fatal` notifications;
- do not emit a creation event when chain construction rolls back;
- when chain execution fails after a provisional object was removed, identify
  the attempted object by the existing transaction-chain concern class and row
  ID rather than adding an audit snapshot table;
- represent retries as the naturally occurring sequence of failed and later
  successful events for the same transaction-chain ID;
- add VPS operation, expiration/runtime, and console open/close events using
  the existing event payload for relevant identifiers and non-secret context;
- preserve the existing mixed-version protocol behavior. Any new node message
  field or message kind must be additive, and the API must continue accepting
  messages from old nodes.

The first implementation tranche covers all identifiable VPS operations,
console lifecycle, and VPS expiration/runtime observations. Further resource
families will use the same small pattern after this tranche is verified.

Compatibility:

- no database migration or persisted-format change is introduced;
- new event types are additive API data, and consumers must tolerate event
  types unknown to older clients;
- node message fields are additive and the new API consumer accepts legacy
  messages, but owner attribution for destructive in-flight chains requires
  ordered deployment: update API request workers first, drain chains created
  by old workers, then enable the new supervisor projection and node
  producers;
- console close signaling adds a per-node RabbitMQ control exchange. Deploy
  the corrected `rabbitmqcfg` generator with the services configuration, then
  explicitly reapply `--perms` for the console and node accounts, selecting the
  deployment's actual virtual host instead of relying on the tool's
  `vpsadmin_dev` default, before starting updated NodeCtld. The initial
  RabbitMQ setup unit is state-file gated and does not update permissions on an
  existing broker. The new permissions are restricted to publishing control
  messages and reading each node's own control queue; leaving them in place
  during rollback is harmless;
- rollback stops producing the new events but does not make existing Event rows
  unreadable.

### Lean first tranche

The first implementation commit is limited to producers using the existing
Event system:

- always persist the existing transaction-chain state event after successful
  chain construction and for node-reported state changes;
- emit `vps.operation_succeeded` only for `done` and
  `vps.operation_failed` only for `failed` or `fatal`, using existing VPS and
  User concerns to retain object and owner identity after deletion;
- treat the shared lifetime wrapper as a VPS lifecycle operation only when its
  concerns identify a VPS;
- emit VPS expiration, observed runtime, maintenance-window, and user-data
  events with no user-data content;
- emit console open/close events from actual NodeCtld sessions, with an
  additive actor-aware authentication RPC and legacy fallback;
- provide small `resource.created`, `resource.updated`, and
  `resource.deleted` helpers for explicitly instrumented synchronous actions,
  recording field names but not values.

No audit-operation model, audit ledger, outbox, event-audience table, action
coverage DSL, migration, or schema update is part of this tranche.

## Cross-API Event Coverage Addendum

Requested on 2026-07-29: supersede the VPS-only outcome projection with
ordinary events covering mutations across the complete API. External
consumers, not vpsAdmin, construct the audit log.

Decisions:

- add no database table, column, migration, or internal audit ledger;
- emit `operation.started`, `operation.succeeded`, `operation.failed`, and
  `operation.resolved` for every accepted non-empty transaction chain;
- use the existing transaction-chain/action-state ID as `operation_id`, and
  use a one-based `attempt` for same-chain retries;
- retain `transaction_chain.state_changed` as the low-level admin diagnostic;
- emit synchronous `resource.created`, `resource.updated`, and
  `resource.deleted` only after successful mutations;
- emit chain-backed resource and domain completion events only after `done`;
- keep immediate security or observation facts distinct from completion
  claims, while automatically correlating them to their chain;
- do not emit generic events for invalid input or denied requests, but add
  explicit security events for useful observations such as failed sign-ins;
- require every core, plugin, authentication, and callback mutation surface to
  declare its event policy or a documented exclusion;
- remove the unmerged `vps.operation_succeeded` and
  `vps.operation_failed` types.

Implementation:

- create the initial operation event inside `TransactionChain.fire2`'s
  database transaction so construction rollback leaves no Event and accepted
  chains cannot lack their start;
- derive stable operation keys from the transaction-chain namespace, with
  explicit overrides for wrappers and implementation variants;
- keep success-only result descriptors in existing signed transaction input,
  not hidden Event rows, and materialize them idempotently at `done`;
- correlate all domain results with `operation_id`; successful outcomes list
  `result_event_ids`, while failures expose no completed facts;
- generalize affected-owner resolution through explicit resource metadata,
  keeping owner, effective actor, impersonating administrator, and session
  separate;
- introduce a vpsAdmin action event-policy contract for synchronous,
  chain-backed, domain/security, and intentionally excluded mutations;
- correct Event Types examples at the API source: exact type name, category,
  severity, roles, and default routing; event-specific subject/summary samples
  where truthful; no OOM-derived fallback for unrelated types.

Compatibility and deployment:

- event types and payload fields are additive except for removal of the
  dev-only VPS outcome types;
- existing nodes accept the additive signed no-op input, so no coordinated
  node protocol upgrade is required;
- deploy the updated supervisor before API request workers, then drain newly
  started chains before any rollback;
- run the mandatory standalone change review after focused commits and quick
  verification, before integration tests;
- deploy the reviewed head to the existing
  `2026-06-15-vpsadmin-events` bridge-network development cluster and verify
  representative synchronous, successful, failed, retried, and security
  events.

## Implementation completion

Implemented as a five-commit vpsadmin series with no schema, migration,
dependency, generated-client, or cross-service protocol changes:

- transaction-chain operations have correlated start and terminal events using
  the existing chain ID as `operation_id`;
- successful chain completion materializes deferred, idempotent resource and
  domain facts, while failed chains emit no false completion facts;
- committed synchronous create, update, and delete mutations emit generic
  resource events across the API policy inventory;
- immediate domain and security events retain their typed payloads while
  gaining authoritative operation correlation where applicable;
- failed sign-ins emit explicit security observations;
- Event Type field examples describe each actual event type and field contract;
- VPS console lifecycle events from the earlier tranche remain included.

The exact reviewed and published head is
`71396e3e98860cdb2fb85efefb44b25b5ff34d37`. The mandatory standalone review
accepted the final range with no findings. Local hooks, focused core/full
regressions, RuboCop, i18n, WebUI PHPUnit, and the complete final-head API
matrix passed. The same exact clean revision is active on the existing
bridge-network development cluster and passed service, HTTP, journal,
transaction-chain, live consumer, correlation, routing, and metadata checks.

The hours-long aggregate integration workflow was intentionally left running
at the user's request not to wait for it; it was not canceled.

## Typed resource event revision

Requested on 2026-07-29: replace the generic resource event family with a
consumer-visible contract that identifies every logical resource and describes
its actual fields. This section supersedes references above to
`resource.created`, `resource.updated`, and `resource.deleted`.

Decisions:

- name completed resource facts `<logical_resource>.created`,
  `<logical_resource>.updated`, and `<logical_resource>.deleted`, without a
  `resource.` prefix;
- reserve those CRUD names for generated resource facts; notification or
  workflow events with another payload contract use distinct semantic names
  such as `user.account_created`, `request.submitted`, and
  `outage.update_reported`;
- expose a versioned resource descriptor through Event Types with the logical
  resource name, action, ID type, and each attribute's type, nullability, enum
  values, payload value policy, and available old/new route matcher;
- include per-field old/new envelopes in event payloads, preserving explicit
  nulls; redact sensitive values and replace oversized values with a SHA-256
  digest and byte count;
- cap individual inline values at 4 KiB and the complete resource payload at
  48 KiB;
- publish successful chain facts before `operation.succeeded`, whose
  `result_event_ids` correlate the terminal event with those facts; failed
  chains publish `operation.failed` without completion facts;
- generate typed resource definitions from loaded Active Record models and
  enforce mutation coverage through the existing strict action-policy
  inventory;
- document the producer contract and new-resource checklist in
  `doc/events.mdwn` and the repository `AGENTS.md`;
- add no database table, column, migration, internal audit ledger, or outbox.

Compatibility and deployment:

- this revises only the unmerged development event contract; consumers and
  routes using the generic development names must switch to the typed names;
- persisted Event rows require no conversion because event names and payloads
  are stored as ordinary data;
- old application processes ignore the additional payload metadata, while
  mixed old/new API processes could expose different Event Type catalogs, so
  request workers should be restarted together in the development deployment;
- no node protocol or vpsAdminOS update is required;
- update the pinned WebUI documentation contract because Event Types gains a
  visible resource schema table;
- deploy the reviewed revision to the existing bridge-network development
  cluster and validate typed synchronous and chain-backed events.

### Final typed-event outcome

The typed-resource revision is complete at vpsadmin commit
`eb847e89c71128f829f313916f56389c66993544`. The exact mandatory review range
`71396e3e98860cdb2fb85efefb44b25b5ff34d37..eb847e89c71128f829f313916f56389c66993544`
was accepted with no Blocking or Important findings. The same clean revision
is pushed and active on the existing bridge-network development cluster.

The deployed Event Type registry contains 546 generated resource event types:
`created`, `updated`, and `deleted` for each of 182 logical resources. There
are no `resource.`-prefixed types. Semantic notifications that previously
collided with generated CRUD names use distinct names, including
`user.account_created`, `request.submitted`, and
`request.update_submitted`.

A reversible live VPS hostname update and restore verified both directions of
the completed contract:

- each accepted chain first emitted `operation.started`;
- each terminal success emitted a typed `vps.updated` result followed by
  `operation.succeeded`;
- the resource fact and terminal fact used the same `operation_id`;
- the resource fact contained both old and new hostname values;
- `operation.succeeded.result_event_ids` named the resource fact;
- the restore completed and left the VPS at its original hostname.

The documentation contract is pinned to the exact vpsadmin revision by
vpsadmin-kb-captures commit
`e818726968a89e66cc4de1fc90daea436809cb39`. No schema, node protocol, or
dependency change is part of this revision. The deliberately hours-long
integration workflows were not awaited, as requested; focused local checks,
all hooks, mandatory review, deployment acceptance, and the quick GitHub
workflows provide the bounded validation for this handoff.

## Public resource event catalog correction

Requested on 2026-07-30: generated CRUD event types must describe
outside-visible API resources, not every Active Record model. The Event Types
API and WebUI must also expose only event types usable by the caller and group
them by stable product topics.

Decisions:

- replace discovery of every loaded Active Record model with an explicit
  catalog of mounted, externally meaningful HaveAPI resources;
- catalog entries declare the logical resource, model, supported CRUD actions,
  stable topic, and audience (`account` or `admin`);
- account entries require an owner resolver and publish roles
  `account, admin`; admin entries publish role `admin`;
- ordinary and support users see only account-usable event types, while
  administrators see the complete catalog; unauthenticated Event Type listing
  is denied;
- exclude storage implementation rows such as snapshot placement/clone
  internals, authentication implementation rows such as generic tokens and
  challenges, translation/join rows, delivery internals, and network
  accounting;
- read-only projections do not receive CRUD event types merely because their
  backing model is loaded;
- the recorder silently ignores uncataloged model callbacks so internal
  persistence remains implementation detail; direct attempts to define or emit
  an uncataloged resource event fail in development and tests;
- transaction chains still emit the generic operation lifecycle even when
  their mutations are entirely internal, but materialize typed CRUD result
  facts only for cataloged resources;
- preserve existing public typed event names, payload envelopes, operation
  correlation, and stored Event rows; do not rewrite or delete historical
  development events;
- use curated machine topics:
  `vps`, `storage`, `network`, `dns`, `account`, `notifications`, `mail`,
  `security`, `infrastructure`, `operating_systems`, `monitoring`,
  `incidents`, `outages`, `payments`, `requests`, and `system`;
- make generated resource event category equal its catalog topic, expose an
  additive localized `category_label`, and have the WebUI group/sort Event
  Types by that label instead of a single `resource` group;
- update `doc/events.mdwn` and repository `AGENTS.md` with the public-catalog
  rule and the checklist for every new outside-visible mutable resource;
- add no schema, migration, node protocol, dependency, or generated-client
  change.

Verification:

- catalog unit tests cover representative account/admin resources and reject
  internal storage, auth, and network-accounting models;
- recorder and transaction-chain tests prove internal callbacks do not
  materialize CRUD results while public facts retain operation correlation;
- Event Type API tests cover authentication, account/support/admin filtering,
  matching filtered counts, localized topic labels, and stable categories;
- WebUI regression tests cover per-topic grouping and use of
  `category_label`;
- run focused core/full API specs, WebUI PHPUnit, RuboCop, i18n health, all
  repository hooks, and the mandatory standalone review;
- amend the unmerged typed-resource commit, force-push with lease, update and
  verify the exact `vpsadmin-kb-captures` pin, deploy the reviewed clean head to
  the existing bridge-network development cluster, and perform bounded API and
  live-event checks;
- do not wait for the hours-long aggregate integration workflow.

Compatibility and deployment:

- this narrows a development-only generated catalog and removes internal event
  types that should never have been public; legitimate public names and
  payloads remain compatible;
- old stored rows remain readable, but removed internal names are no longer
  advertised or emitted after all API workers restart;
- mixed old/new API workers could expose different catalogs, so restart API
  request workers together in the development deployment;
- ordinary clients gain the additive `category_label` output field and receive
  a role-filtered Event Type list; administrators retain access to all public
  account and administrative types;
- no coordinated vpsAdminOS or node rollout is required.

### Final public-catalog outcome

The corrected implementation is complete at vpsAdmin commit
`a1321b2485ce5f14087d4d93429a97ea8cf28306`, with the WebUI documentation
contract pinned by vpsadmin-kb-captures commit
`eb7d7272df43d15cab1cf685eda50e5053c43faa`. Both exact revisions are pushed
and their worktrees are clean.

The mandatory fresh-context review first found that a target-model restriction
could omit public snapshot facts from a cascading dataset deletion. The
correction records every cataloged public model encountered by a transaction
chain while applying the requested CRUD intent only to the action's target
models. The same reviewer then accepted the exact final range with no Blocking,
Important, or Advisory findings.

Live deployment subsequently exposed an OAuth repeat-login regression: a known
device's incidental `last_seen_at` update was captured even though
`user_known_device.updated` is not a published action. The final recorder
filters by each model's effective catalog action, ignoring unsupported natural
mutations while preserving transaction-chain target-action overrides. A second
fresh-context review accepted that correction without findings.

Inspection of the superseded API topic workflow then found four expectations
left over from earlier designs. The final specs remove synthetic internal
snapshot-placement events, keep node-kernel projection changes internal, and
require a successful VPS-create operation to link all five committed public
result facts. The final delta is test-only. A third fresh-context review
accepted the exact final range without findings.

The exact clean vpsAdmin revision is active on the existing bridge-network
development cluster. Its runtime publishes 172 typed resource event types
across 12 populated product topics. Internal snapshot-placement and clone
models, generic token and WebAuthn challenge rows, and network-accounting rows
are absent. The per-type common-field examples match the actual event name,
category, severity, roles, and default-routing value.

Browser-style live acceptance completed OAuth authorization twice with the same
device cookie; both requests returned the successful redirect, including the
known-device path that had previously returned HTTP 400 `invalid_request`.

No database migration, node protocol update, dependency change, or generated
client update was introduced. The hours-long aggregate integration workflow
was deliberately not awaited, as requested.

## Delivery-only persistence correction

Requested on 2026-07-30: Events are notification delivery history, not an
internal audit log. Users that need an audit log construct it externally by
catching a deliberately routed event stream.

Implementation decisions:

- persist an Event only when routing produces at least one executable,
  non-skipped delivery;
- unmatched, muted-only, disabled-only, inactive-only, and otherwise
  skipped-only candidates leave no Event, delivery, match, or routing-context
  rows;
- remove persistence overrides from resource, lifecycle, security, console,
  OOM, outage, and test-event producers;
- keep delivery outcome and retry state on EventDelivery for events that
  entered the delivery pipeline;
- treat operation lifecycle events as independently routed facts correlated by
  `operation_id`, without `attempt` or `operation_attempt` counters;
- materialize successful transaction result facts only after `done`, route
  them before `operation.succeeded`, and reference only result events that
  were actually persisted;
- make the Test Event action fail clearly when no enabled route produces a
  delivery;
- retain OOM mute evaluation in the transient routing plan without persisting
  a suppressed Event;
- describe the Event API and WebUI as delivery history, and document that a
  complete external record requires an explicit catch-all route with suitable
  account or administrator visibility.

Compatibility and deployment:

- the Events feature is unreleased and the development database is
  disposable, so draft migrations and API choices may be corrected in place;
- add no audit table, operation-attempt counter, or compatibility migration;
- reset and recreate the existing single-topology development cluster on its
  default bridge network after the reviewed revision is published;
- update the exact vpsAdmin pin and retire the suppressed-event concept in
  vpsadmin-kb-captures, rebuilding bilingual review candidates without
  publishing production KB changes;
- run focused API/WebUI verification, repository hooks, and mandatory
  fresh-context review, while continuing to skip the hours-long aggregate
  integration workflow.

## API topic-spec follow-up

Requested on 2026-07-30 after the completed topic-parallel workflow reported
failures.

Approach:

- use the failed GitHub Actions attempt as the authoritative failure inventory
  instead of rerunning it without investigation;
- make Event-row assertions arrange an explicit webhook delivery route, so the
  specs model delivery history rather than implicit audit persistence;
- preserve explicit no-route examples and update them to assert that rejected
  route matches leave no Event rows;
- correct independent test defects exposed by the run, including invalid RSpec
  `change` matcher syntax and a stale e-mail fixture that leaves delivery
  disabled;
- remove the obsolete operation-attempt expectation from the remaining
  lifecycle example;
- run every failed example locally with the shared route helper, plus RuboCop
  and repository hooks, before mandatory fresh-context review;
- commit and push a test-only follow-up, cancel superseded workflow attempts
  for older branch heads, and inspect the replacement API Specs result.

Compatibility:

- this follow-up changes tests only and does not alter runtime behavior,
  persisted state, API contracts, deployment ordering, the running development
  cluster, or the already reviewed WebUI/KB capture contract;
- no capture regeneration, database reset, or development-cluster redeployment
  is required for a test-only correction.

## Aggregate CI early-failure feedback

Requested on 2026-08-01 while investigating the replacement aggregate run.

Affected repositories:

- `vpsadminos`: improve periodic test-runner status output so it names test
  scripts with unexpected results, clarify the existing opt-in stop-on-failure
  behavior, and align both framework-backed workflows;
- `vpsadmin`, `confctl`, `terraform-provider-vpsadmin`, and
  `vpsfree-irc-bot`: make cancellation upload runner logs and expose the
  existing stop-on-failure mode as an opt-in manual-workflow input.

Approach:

- keep normal push, pull-request, schedule, and manual CI exhaustive by
  default across every repository that uses the framework;
- retain the existing `--stop-on-failure` runner switch as an explicit
  development choice that stops scheduling new tests only after an unexpected
  failure or unexpected success;
- include the unexpected script paths in every periodic failed-suite status so
  a developer or monitoring agent can decide to cancel without waiting for the
  final aggregate summary;
- use the same explicit manual input and runner argument handling in all
  framework-backed workflows;
- run cancellation log upload before result evaluation in every workflow and
  guard it for both failure and cancellation, preserving runner-local per-test
  evidence after a normal GitHub Actions cancellation;
- clear the dedicated test-runner state directory in a separate identified
  preparation step before each framework-backed workflow; derive the directory
  from the GitHub repository ID, run ID, and attempt so jobs from different
  repositories on one shared runner, as well as sequential and overlapping
  attempts, cannot share evidence; publish results only when preparation
  succeeded and the test step started;
- remove an isolated state directory after a successful runner, a skipped
  runner, or a successful failure/cancellation artifact upload; retain it when
  both the runner and artifact upload fail so operators still have a local
  recovery path without allowing another run to consume that directory;
- implement directory derivation, stale-state removal, validation, export, and
  outcome-aware cleanup once as vpsAdminOS composite actions. Every framework
  consumer calls those actions instead of duplicating path construction and
  shell deletion, and pins the complete shared action set to one exact
  vpsAdminOS revision;
- add focused runner specs and workflow syntax/selection checks, commit both
  repositories, run mandatory fresh-context review, then validate the behavior
  in GitHub Actions.

The first exact-head vpsAdminOS run identified `kernel/module-autoload` as an
unexpected failure. Its assertion found the expected module-wrapper record and
then copied the complete `/var/log/messages`. The newline-free base64 response
stalled mid-frame after 227,328 encoded bytes and hit the 15-minute command
timeout; the exact lower-level reason for the transport stall is not proven.
Replace that unbounded diagnostic capture with one bounded fixed-string match
that includes both the `kernel.modprobe` logger and expected payload, then run
the isolated integration test before accepting a rerun.

The first live cancellation proved that GitHub runs the upload, evaluation, and
summary steps after interrupting the runner, but its artifact also demonstrated
why the historical global `/tmp/os-test-runner` is unsafe: it contained logs
from jobs completed hours before the canceled job started. Every workflow must
pass its run-specific state directory to the runner and to artifact/summary
actions; cleanup and guards alone are insufficient evidence isolation.

While validating every framework consumer, the IRC integration suite exposed a
separate stale fixture contract. Security-advisory publication now requires the
reviewed content revision, so the fixture must pass its current revision before
testing the IRC announcement and dependent update path.

The protected historical vpsAdmin aggregate must run to completion because its
older workflow cannot preserve per-test artifacts after cancellation. Classify
every unexpected result from that artifact and fix actionable causes before
accepting a replacement run. Recover self-hosted-runner infrastructure failures
centrally in vpsAdminOS: repair and retry one exact invalid Nix store path, and
serialize initrd udev workers in framework-created NixOS test VMs to avoid the
observed concurrent x86 module text-patching crash. Keep genuine scenario fixes
in their owning repository, including the explicit completion assertion for the
WebUI logout flow. Propagate the reviewed framework revision through every
direct and transitive consumer lock before exhaustive validation.

The ensuing exact-head vpsAdminOS aggregate identified the same Arch Linux
mirror throughput failure in Docker, Podman, and Incus package installation.
Add one explicit, bounded command-retry primitive to osvm without changing
existing command semantics. Opt only those three idempotent Pacman setup
commands into three attempts with fixed delays and per-attempt timeouts. Cover
the helper and Machine forwarding with framework specs, review it independently,
then validate all three real VM scenarios concurrently before publishing the
final direct and transitive lock graph.

Compatibility and deployment:

- the runner output is additive and its existing final summary remains
  unchanged, so consumers that parse the final counts remain compatible;
- the new workflow input defaults to false and therefore does not change
  exhaustive CI behavior unless a developer opts in;
- no schema, API, protocol, persistent-state, node rollout, or WebUI/KB change
  is involved;
- `vpsadmin` and `confctl` must pin the reviewed vpsAdminOS test-runner
  revision before the enhanced status appears in their CI. The Terraform
  provider and IRC bot inherit `vpsadminos` through their `vpsadmin` input, so
  they must instead pin the resulting vpsAdmin revision. Runtime nodes do not
  need coordinated updates because the changed component is development and
  CI tooling;
- the shared actions must be published in vpsAdminOS before consumer workflow
  heads can execute. Consumer workflows use an immutable action revision, so
  they remain valid independently of later changes to the `staging` branch.
- the Nix repair is bounded to one exact path and one retry; an unrepairable
  path or a repeated build failure remains visible as a test failure. Serialized
  udev coldplug applies only to generated test guests, not deployed machines.
- the Arch retry primitive is additive and opt-in. Each selected test setup is
  bounded to three 900-second attempts with two 15-second gaps; final failures
  retain the last command's status and output. It changes no production image,
  package source, persistent format, runtime protocol, or node deployment.

## Default-branch test framework integration

The final integration is tracked in
`work/2026-08-01-test-framework-ci/{plan,state}.md`. The one-path Nix store
repair was dropped because garbage collection can invalidate paths repeatedly;
runner job hooks and a shared GC lock solve the lifecycle centrally instead.
The shared framework and workflow commits were merged into every affected
default branch, while the event feature commits remained on this initiative's
branches.

After default integration, rebase every existing
`2026-06-15-vpsadmin-events` branch onto its repository's actual GitHub
default. Remove framework-only commits now present on defaults, preserve the
event-specific ranges, and regenerate exact capture and deployment pins.

## Compact notification delivery tables

Requested on 2026-08-03 after observing that the administrator delivery-log
table overflows the fixed-width WebUI content area. Apply the same presentation
to the delivery queue because both pages share one renderer and contain the
same fields.

Replace the current thirteen-column table with six grouped columns:

1. `Delivery`: the existing delivery link and action.
2. `Event`: the existing event link, type, and subject.
3. `Context`: vertically stacked Group, User, and VPS values.
4. `Destination`: vertically stacked Receiver and Target values.
5. `State`: vertically stacked State and Attempts values.
6. `Times`: vertically stacked Released, Last attempt, and Next retry values.

Use a table-specific identifier, fixed table layout, explicit proportional
column widths, top-aligned cells, and wrapping inside long values. Remove the
redundant icon-only detail column because the Delivery value already links to
the same detail page. Keep filtering, pagination, API requests, and delivery
detail pages unchanged.

Affected repositories:

- `vpsadmin`: shared queue/log markup, scoped CSS, Czech translations, and
  focused source and browser regression coverage;
- `vpsadmin-kb-captures`: exact vpsAdmin revision pin and documentation
  contract validation for the visible WebUI change. The admin-only pages have
  no screenshot binding, so no PNG or KB article candidate is expected.

Compatibility and deployment:

- there is no database migration, persisted-state change, API or message
  contract change, or RabbitMQ impact;
- old and new WebUI processes can coexist because this is presentation-only;
- rollback can use the preceding WebUI revision without data conversion;
- after review, push the exact vpsAdmin revision, update and validate the
  capture contract pin, update the already-running bridge dev cluster's
  services, and verify both pages in English and Czech with a populated row;
- do not reset or alter the independently staged notification KB release,
  because this layout has no corresponding KB page or captured image.

Quick verification consists of PHP syntax, focused PHPUnit regression tests,
locale generation/health checks, hook-managed checks, and the capture
repository's `nix develop -c bin/check`. After the mandatory standalone change
review, run the targeted WebUI Playwright scenario against the updated dev
cluster and inspect the table geometry at the WebUI's minimum supported width.

## Event route expiration metadata

Give the shared `EventRoute.expires_at` API parameter an explicit
human-friendly label and a description explaining that the optional timestamp
ends event matching. Regenerate and translate the API metadata catalog, then
squash the correction into `api: describe notification route behavior`, where
the other route parameter labels and descriptions were introduced.

Add a general API-parameter metadata rule to vpsAdmin's `AGENTS.md` and the
mandatory-change-review checklist: labels must always be human-friendly, and
descriptions must explain meaning or purpose unless the parameter is already
obvious and a description would add nothing. Keep the repository rule as a
separate policy commit because it applies beyond this route feature.

This is documentation and API self-description metadata only. It changes no
request/response value, database schema, persisted state, RabbitMQ message, or
deployment ordering. Mixed old and new API/WebUI processes remain compatible,
and rollback requires no data conversion. Refresh the WebUI documentation
contract pin and update the bridge development cluster after review.

## Workspace dev-cluster isolation

Requested on 2026-08-18: keep the complex, unmerged event-aware vpsAdmin
development cluster from imposing its module, schema, template, and helper
service assumptions on unrelated workspace initiatives.

- Restore the generic vpsAdmin development cluster on workspace `master` by
  reversing the complete event-specific cluster stack. Keep later generic
  improvements, including source revision reporting, larger service storage,
  and stale Nix-root cleanup.
- Rebase the existing workspace branch `2026-06-15-vpsadmin-events` onto the
  cleaned `master` and restore the exact event-aware cluster there as one
  branch-owned commit.
- Use the dedicated top-level workspace worktree at
  `worktrees/2026-06-15-vpsadmin-events/workspace`. Set
  `VPSADMIN_DEVCLUSTER_WORKSPACE` to the canonical coordination checkout so the
  runner, Nix definitions, and shared runner library come from the branch while
  project inputs and runtime state use direct, non-symlinked paths. Keep the
  source and coordination roots distinct in the runner environment.
- Shared `master` keeps the generic Mailpit/mailer container and legacy seed
  contract. The event branch keeps Telegram, SMS, webhook, notification
  dispatcher, managed-template, delivery-method, and OOM-route support.
- This changes no production API, schema, protocol, configuration pin, or
  deployment. Do not start, update, or reset the stopped initiative cluster as
  part of the isolation.

Verify shell, JSON, and Nix syntax on both trees; assert that the branch's
dev-cluster files exactly match pre-isolation `master`; evaluate both cluster
configurations without starting VMs; and run the mandatory standalone review
before publishing the workspace branches.
