# 2026-08-18-vpsadmin-password-reset

## Goal

Add self-service password recovery to the vpsAdmin OAuth server. Recovery is
available only to accounts with effective TOTP or WebAuthn configuration. The
public request form accepts a login or primary email address and never reveals
whether an account exists or can use recovery.

## Affected repositories

- `vpsadmin`: schema, recovery state and operations, OAuth forms and routes,
  MFA integration, mail queue integration, localization, and tests.
- `vpsfree-mail-templates`: Czech and English production recovery template.
- `vpsfree-kb-contracts`: pin the exact vpsAdmin feature revision and run the
  visible-WebUI impact contract; update captures or managed documentation only
  if the contract reports the OAuth/recovery screens as covered concepts.
- `vpsfree-cz-configuration`: pin the exact vpsAdmin feature revision and add
  an operator deployment guide with the production OAuth authorization start
  URI for WebUI, both DokuWiki clients, and Discourse.
- workspace dev-cluster tooling: seed external notification templates through
  the same declarative reconciler as deployed systems so the acceptance
  cluster can run the rebased vpsAdmin revision.

## Approach

- Resolve an exact login first. Otherwise find all users with the submitted
  primary email, using the database's case-insensitive collation.
- Make the public POST account-independent by inserting one
  `PasswordRecoverySubmission` for every non-empty identifier. A dedicated API
  worker claims submissions with row locking, resolves accounts, and performs
  mail work after the HTTP response. Failed work is retried up to three times;
  processed rows are deleted and abandoned rows are retained for at most one
  day. Admission is serialized and bounded globally and per source address so
  the uniform queue cannot grow without limit.
- Send one combined message per destination. It lists every matching login and
  contains a separate one-hour, single-use link for each eligible account. An
  account without MFA gets a support notice instead of a link.
- Represent one delivery with `PasswordRecoveryRequest` and one child
  `PasswordRecovery` per account. Link tokens are scoped to a child recovery.
- Queue one normal `MailLog`/mail transaction with no single user association,
  explicit language and destination, and no configured alternate recipients.
  The persistent mail body necessarily contains the rendered one-hour links;
  recovery records store only token digests and MFA is always required.
- Exchange a link for a 15-minute recovery session. Verify TOTP, an existing
  recovery code, or WebAuthn before showing the password form. Invalid MFA does
  not require re-entering the password, and password validation errors do not
  require repeating MFA while the recovery session remains valid.
- Offer the existing session-logout choice, checked by default. When unchecked,
  existing token, OAuth authorization-code, and SSO state remains usable, while
  incomplete password/TOTP continuations are invalidated by every password
  change. A successful reset invalidates all other recovery state for that
  account, sets a 15-minute host-only completion marker, and starts a fresh
  authorization through the configured client authorization start URI. The
  matching OAuth client consumes the marker, bypasses SSO for that request,
  and shows the normal credential form with a Bootstrap success alert. A
  client without a start URI falls back to a minimal internal confirmation
  page. Successful password
  authentication and OAuth token issuance carry a per-user generation and
  revalidate it under the user row lock so concurrent password changes cannot
  publish stale credentials.
- Gate all new public behavior behind `core.password_recovery_enabled`, which
  defaults to false.

## Compatibility and deployment

- Schema additions are backward compatible: new recovery and submission
  tables, a nullable OAuth client start URI, recovery context on WebAuthn
  challenges, a non-unique user email index, and a defaulted non-null
  authentication generation on users.
- Old API processes ignore the new schema. Keep the feature disabled until all
  OAuth API instances, the password-recovery workers, and templates are updated
  and client start URIs are set. The worker discards queued submissions while
  the feature is disabled, so disabling the flag is also the first rollback
  step.
- Deploy the additive migrations first, then the templates and API/auth/WebUI
  application configuration, verify the workers and OAuth client start URIs,
  and enable the feature last. All application instances includes every
  process that can perform Basic/token authentication or update passwords, not
  only the OAuth frontend. For rollback, disable the feature, stop the new
  workers, return all application instances to the old version, and only then
  migrate down; new processes must not run after their required columns are
  removed.
- WebUI clients must list the separate authentication origin in
  `api.oauth2TrustedOrigins`. The production and development configurations
  already do so; the integration fixture carries the same explicit trust so it
  exercises the deployed cross-origin OAuth description safely.
- Production deployment and merging are out of scope for this session. The
  production configuration will pin the feature revision and include an
  operator guide for deployment ordering, client start URIs, verification, and
  rollback by disabling the feature first.
- No vpsAdminOS protocol change is expected. The admin API adds the optional
  OAuth client authorization-start URI and permits an account-neutral mail log
  to expose `user: null`. These changes are additive and existing consumers
  remain compatible. The current generated Go client does not expose the new
  OAuth setting, so operators must configure it through another admin API/WebUI
  path; regeneration is deferred until that client is otherwise refreshed.
  The KB contract impact check is required because the OAuth sign-in page
  changes; any resulting capture or documentation changes remain
  deployment-independent.

## Testing plan

- Add model, worker, operation, route, mail, token, MFA, OAuth redirect,
  localization, and migration specs, including shared-email, asynchronous
  non-disclosure, retry, and feature-disable scenarios.
- Run focused API specs, migration checks, i18n maintenance, RuboCop, active
  Overcommit hooks, mail-template rendering, and CI selection coverage.
- Commit quick-verified changes, then run the mandatory fresh-agent change
  review before long integration tests.
- Run the OAuth/WebUI authentication integration test through the dedicated
  auth frontend and deploy a single-node bridge-network dev cluster. Seed
  shared-email accounts with TOTP and without MFA, verify the worker and the
  combined message in Mailpit, and leave the cluster running for user
  acceptance.
- After pushing the vpsAdmin feature commit, pin that exact revision in
  `vpsfree-kb-contracts` and run `nix develop -c bin/check`. Regenerate only the
  bilingual screenshots or page contracts that are actually reported.
- Pin the same exact revision in the `vpsadmin` services channel using
  `confctl`, add the deployment guide in a separate configuration commit, and
  run the configuration repository's required checks and relevant builds.

## User-acceptance follow-up

- Keep the request form concise: state the TOTP/passkey requirement and ask for
  the login or primary address, without explaining the non-disclosure policy or
  the support-only outcome in advance. Keep the submitted response neutral.
- Do not mention TOTP recovery codes in password-recovery forms, validation
  errors, or messages. Recovery codes remain accepted internally so existing
  MFA recovery behavior is compatible.
- Show the configured vpsFree.cz logo on every recovery state, as on the OAuth
  sign-in and WebAuthn registration forms. Permit only a validated HTTP(S) logo
  origin in the recovery page's content security policy.
- Make “Back to sign in” start a fresh OAuth authorization through WebUI's
  `page=login&action=login` entry point and center the link. After a successful
  reset, start the saved client's authorization flow, bypass SSO once, and show
  “Password changed.” / “Heslo změněno.” as a Bootstrap success alert above
  the normal login fields. The previous standalone completion page made the
  next step look like missing login fields, and its full-width link overflowed
  the form.
- Add bilingual HTML recovery messages with one clear action button per
  recoverable account. Keep the plain-text alternative, the one-hour validity,
  grouped shared-address behavior, and support-only account entries.
- Re-run focused verification, a fresh mandatory review, the WebUI OAuth test,
  the KB contract at the new exact vpsAdmin revision, and current-head CI. Then
  update the existing bridge dev cluster and leave it running for acceptance.
- The Linux executable-memory page fault is explicitly out of scope by user
  decision. Do not patch or repin the kernel or vpsAdminOS in this initiative.

## Mail notification and throttling follow-up

- Restore the established automated-mail notice verbatim in the plain and HTML
  recovery templates. Record the exact English and Czech wording in the local
  contributor rules for both template repositories so future member-facing
  mail keeps the notice uniform.
- Send a plain-text security notification after every successful self-service
  password change: recovery, an authenticated user changing their own password,
  and a forced OAuth or token password change. Include the login, time, source
  address, and user agent. Do not notify for an administrator changing another
  user's password or for maintenance code.
- Remove the recipient-address throttle. Rate-limit the normalized submitted
  login or email value before account lookup, regardless of whether it exists,
  so different logins sharing one primary email remain independent and the
  public response does not disclose account existence.
- Admit one request per submitted value per 10 minutes and at most 10 requests
  per source address per 10 minutes. Limit the worker queue to 100 unfinished
  submissions. Return an explicit HTTP 429 with `Retry-After` for either rolling
  limit and HTTP 503 when queue admission is unavailable.
- Retain finished submission ledgers for one day so processed work still counts
  toward rolling limits, while clearing the raw identifier and user agent after
  processing. Before every claim, terminalize and scrub an exhausted claim that
  remained stale after a worker process was terminated, so it cannot consume
  one of the 100 queue slots until daily cleanup. Rewrite the unreleased
  migration directly and reset disposable development databases.
- Re-run focused checks, mandatory review, exact-head CI and WebUI integration,
  repin the KB contract, then reset and deploy the bridge-network development
  cluster. Production deployment remains an operator task.

## Final deployment and trust-boundary decisions

- Publish `/oauth2/password-reset` on the real production auth frontend,
  `cz.vpsfree/containers/prg/proxy`. Its protected vpsAdmin baseline can remain
  on the stable revision; a low-priority route in shared production frontend
  configuration proxies this path to `auth_production` and retains the
  maintenance response.
- Install both new production mail templates before starting either upgraded
  API. The password-change security notice is not controlled by the recovery
  feature flag, so making its template available first preserves existing
  password-change behavior throughout a rolling deployment.
- Treat nginx `X-Real-IP` as the trusted client address for password-change
  notices and recovery WebAuthn challenges. Do not use caller-controlled
  `Client-IP` for security metadata.
- Build both production API nodes and the production auth proxy before the
  operator rollout. Keep the feature disabled until schema, templates, both
  APIs, the worker, the proxy route, and each OAuth client's authorization
  start URI have been verified.
- Production deployment remains exclusively an operator action. This
  initiative updates and leaves the exact `vpsadminServices` revision and
  deployment runbook on the feature branch, without deploying production.

## OAuth client completion behavior

- Add a default-off OAuth client setting for authorization start URLs that
  require another user action before they return to vpsAdmin. WebUI and both
  DokuWiki clients keep the immediate redirect flow; enable the setting only
  for Discourse in production.
- For an interactive client, show the successful password-change message on
  the internal recovery page before leaving vpsAdmin. Link to the validated,
  stored authorization start URI and explain that the vpsAdmin sign-in form is
  reached through that service.
- Keep the completed-recovery marker so the matching authorization still
  bypasses SSO once. Add a short-lived, host-only marker bound to that recovery
  when the internal message is shown; suppress the duplicate OAuth alert only
  when both markers match.
- Require a valid recent completion marker before the internal page reports
  success. Clients without a start URI retain the internal confirmation without
  a continuation button. Invalid, expired, or cross-client markers never expose
  a continuation target.
- Rewrite the unreleased migration directly, reset the disposable development
  database, and configure the development WebUI client in interactive mode so
  the completion and no-repeat behavior can be tested without Discourse.
- Update the production runbook and exact vpsAdmin pins after focused tests and
  the mandatory fresh-agent review. Do not change mail templates or deploy
  production.

## Password recovery metrics and acceptance refinements

- Export durable global counters for recovery admission outcomes, queue-capacity
  events, and committed password changes. Export the unfinished queue depth and
  configured limit as gauges. Persist only fixed event names, aggregate counts,
  and last-occurrence timestamps; do not persist identifiers or user IDs in the
  event table.
- Record password-change sources centrally as authenticated self-service,
  forced reset, recovery, administrator, or other. Keep the event update in the
  same database transaction as the password update so rollbacks do not count.
- Extend the user-owned metrics-token endpoint with password generation,
  forced-reset state, account MFA enablement, and enabled TOTP/passkey counts.
  Bump the additive metrics contract from version 1.0 to 1.1.
- Alert by warning email when the unfinished recovery queue reaches its global
  limit of 100 or reached that limit within the preceding ten minutes. Preserve
  the transition as a durable event so a fast worker drain cannot hide it.
- Label the read-only login value on the password form. Choose the MFA
  explanation from the actual available method set so TOTP-only, passkey-only,
  and combined accounts see accurate English and Czech text, including after a
  failed verification.
- Return the development WebUI OAuth client to the direct completion mode used
  by production WebUI and DokuWiki. Keep the interactive completion mode for
  Discourse and retain its route-level coverage.
- Keep recovery user-agent metadata as bounded raw snapshots. Do not populate
  the permanent `user_agents` dictionary from the anonymous submission queue;
  document and test the retention distinction.
- Update the bilingual metrics KB pages, the deployment runbook, both monitor
  builds, the exact KB vpsAdmin pin, and the production `vpsadminServices`
  channel pin. Stage KB changes for review but do not publish them. Production
  deployment remains an operator action.

## Recovery password visibility follow-up

- Add keyboard-accessible eye controls to both new-password fields on the
  recovery password form. Either control reveals or masks both fields together,
  matching the existing forced-password-change behavior. Passwords remain
  masked by default and the form remains usable without JavaScript.
- Add concise English and Czech accessibility labels for showing and hiding the
  passwords. Keep the recovery page self-contained and do not add a third-party
  icon or stylesheet dependency.
- Add route and browser coverage for the recovery toggle and regression coverage
  for the already-supported forced-password-change controls. No schema, API,
  mail-template, or authentication-policy change is required.
- After focused checks and the mandatory fresh-agent review, repin the exact
  vpsAdmin revision in the KB contract and production configuration, update the
  runbook's embedded revision, and refresh the existing bridge development
  cluster. Production deployment and KB publication remain out of scope.

## Password change history follow-up

- Leave the database-backed password-recovery worker and its polling behavior
  unchanged. Add an append-only password-change log containing the affected
  user, the stable change source, the creation time, and the exact initiating
  user session when one exists.
- Keep `user_session_id` nullable because recovery and forced-password-change
  flows run before an authenticated user session exists. Do not create a
  synthetic session or copy IP address and user-agent snapshots into the log.
- Create the detailed log and increment the existing durable global counter in
  the same transaction as the password update. Keep the counter as the
  Prometheus source so deleting detailed rows never makes metrics decrease.
- Retain history through soft deletion and remove it when the account enters
  hard deletion. Do not backfill changes from before the new migration.
- Expose a read-only password-change-log API. Account owners can list their own
  history and administrators can list all history; the existing user-session
  resource authorization controls whether a related session can be resolved.
- Add **Password changes** / **Změny hesla** after **Sessions** / **Relace** in
  the profile sidebar. Show newest entries first with the change time, localized
  method, and an authorized link to the exact session when available.
- Add a semantic WebUI documentation ID and Czech/English user-documentation
  candidates. The simple audit table does not need a new screenshot concept;
  stage the documentation for review without publishing it.
- Add a fourth additive migration to the deployment runbook, update the exact
  vpsAdmin pins, and deploy both API hosts before both WebUI hosts. Preserve the
  chosen rolling deployment: accept and quantify the brief interval in which
  an old API can increment the global counter without writing a detailed row.
- Production deployment and KB publication remain operator-only. Update the
  existing bridge-network development cluster and leave it running for user
  acceptance.

## Expired recovery page follow-up

- Render every browser-facing invalid or expired recovery state inside the
  existing branded password-recovery layout. A stale CSRF cookie must never
  fall back to Sinatra's plain-text halt response.
- Show a primary **Request a new link** / **Požádat o nový odkaz** action on
  every failure page. When the originating OAuth client is known, also show the
  configured, centered **Back to sign in** / **Zpět na přihlášení** link.
- Carry the public OAuth client ID and selected locale through recovery email
  links, redirects, and form actions. Keep the recovery token in the URL
  fragment. For a valid recovery, use the client stored with the recovery
  request as the authority; never accept a caller-provided redirect URI.
- Keep HTTP 400, no-store and browser security headers, the one-hour email-link
  lifetime, and the 15-minute recovery-session lifetime. WebAuthn failures must
  remain structured JSON responses.
- No schema, API resource, generated-client, or production mail-template change
  is required. Existing recovery links without context query parameters remain
  compatible.
- Add route and Playwright coverage for a form left open past cookie expiry,
  invalid and reused links, missing client context, bilingual copy, and safe
  client-aware actions. Repin the KB contract and production configuration,
  run the mandatory review, update the existing bridge cluster, and leave
  production deployment and KB publication to the operator.

## Default OAuth client follow-up

- Add the general-purpose nullable boolean `oauth2_clients.is_default` and a
  unique index that permits any number of non-default clients but at most one
  default. Expose it through the administrator OAuth-client API and switch the
  default atomically when another client is selected.
- Require a default client to have a validated authorization start URI. Resolve
  a recovery client from persisted recovery state first, an explicit valid
  client second, and the default client last. Never accept a return URI from a
  public request.
- Use the resolved default for the complete queryless flow, including the
  submission, confirmation page, mail link, failure pages, and completion.
  Existing flows with an explicit or persisted client keep that client.
- Configure the development WebUI client as default and document selecting the
  production WebUI client after the additive migration. Older API versions
  ignore the new column, and a newer API without a default keeps the existing
  safe behavior.
- Restore the development-only account MFA flag for `test-user1` after the
  cluster update. Reuse its existing enabled and confirmed `Acceptance TOTP`
  device and leave production deployment and KB publication to the operator.

## Password reset and history UI follow-up

- Redesign the OAuth forced-password-reset step to match the recovery password
  form: show the trusted account login in a labelled read-only field, add
  visible labels to both new-password fields, retain the shared show-password
  control, and keep the existing OAuth client, cancellation, and submission
  behavior.
- Show an **Admin** column only in the administrator view of password-change
  history. Resolve the administrator through the recorded initiating session
  and link to that administrator's profile when the nested relation is
  authorized. Do not request or disclose the nested user relation to members.
- Increase only the password-recovery worker's idle polling interval from one
  second to five seconds. Continue processing queued work immediately and keep
  the existing error backoff unchanged.
- Use `Login` as the Czech label for the account identifier throughout WebUI,
  password recovery, embedded and production mail templates, tests, and the
  Czech terminology guide. Keep `Přezdívka` only as the translation of the
  separate `Nickname` field.
- Make the shared development seed idempotent for unchanged passwords by
  checking the configured plaintext against the stored password hash before
  calling `set_password`. This avoids password-change history, authentication
  generation changes, and session revocation when the seed is rerun.
- After deploying the reviewed revision to the existing bridge development
  cluster, remove only the password-change rows proven to have been created by
  previous seed reruns. Preserve all real recovery, signed-in, forced-reset,
  and administrator changes, then rerun the seed twice to prove it is a no-op.
- Keep schema and public API shapes unchanged. Repin the exact vpsAdmin revision
  in the KB contract and production configuration, and update the deployment
  runbook. Do not publish KB pages or deploy production systems.

## Administrator recovery restriction and history fix

- Fix the administrator password-change history view so rows without an
  initiating session never cause the PHP client to resolve `user_session#show`
  without an ID. Keep administrator attribution for rows with a session.
- Limit self-service password recovery to accounts whose API role is `user`.
  Treat both `support` and `admin` roles as administrator accounts for this
  policy. The public form and neutral confirmation remain unchanged.
- Send the normal grouped recovery email for matching administrator accounts,
  but never create a reset token. Give administrator status precedence over
  MFA and other account eligibility and tell the recipient to ask another
  administrator to change the password.
- Keep the stored recovery outcome `unavailable` and use an
  administrator-specific mail outcome. This avoids a schema, persisted enum,
  API, generated-client, or metrics change while preserving the rendered
  reason in the mail log.
- Revalidate the shared policy before consuming a recovery link and in the
  locked final password transaction. Invalidate active recoveries whenever an
  account crosses the ordinary-user and privileged-account boundary, so links
  issued before a promotion cannot be used later.
- Update embedded and production Czech/English plain-text and HTML templates,
  preserving the exact automated-mail footer. Install production templates
  before starting the updated API.
- Add API, model, template, PHP, and browser regressions for privileged
  accounts, shared addresses, stale links, privilege transitions, and
  sessionless history rows. Run mandatory review, repin the KB contract and
  production configuration, refresh the existing bridge development cluster,
  and leave production deployment and KB publication to the operator.

## Password change client audit follow-up

- Supersede the earlier decision not to snapshot sessionless client metadata.
  Store an immutable client IP address, server-resolved PTR, and normalized
  user agent on every password-change log. Copy the snapshot from the exact
  initiating session when one exists; otherwise derive it from trusted
  `X-Real-IP` or the connection address and the current request user agent.
- Keep the existing session relation nullable. Required token resets attach the
  session atomically when token issuance succeeds. Required OAuth resets carry
  the exact log through the pending authorization and attach the session during
  authorization-code exchange. Do not create an OAuth session before exchange;
  abandoned flows remain sessionless with their client snapshot intact.
- Keep password recovery sessionless because its later sign-in is a separate
  authentication flow. Record its final password request metadata, and also
  cover transparent password-hash upgrades. Maintenance changes without a
  session or request may retain null client fields.
- Expose the nullable snapshot fields through the existing owner/admin
  password-change API. Administrators can inspect every snapshot; account
  owners can inspect their own and sessionless events, but client details from
  another user's initiating session remain redacted. In WebUI, keep the compact
  primary columns and render IP, PTR, and user agent in a wrapping full-width
  detail row below each event so a long user agent cannot widen the table.
- Rewrite the unreleased password-change migration, reset the disposable
  development database, and preserve rolling compatibility by migrating before
  starting new API processes. Reconcile an OAuth password-change link if an old
  process exchanges its code during a rolling deployment, using the existing
  idempotent authentication-maintenance timer. Old processes remain compatible
  but cannot populate the new snapshots, so drain them promptly and document
  the short, irreversible audit-detail gap. Update the runbook and exact
  downstream pins; production deployment and KB publication remain
  operator-only.
- Run focused API, migration, i18n, PHP, browser, and layout-overflow checks,
  then the mandatory fresh-agent review before long integration. Repin the KB
  contract and production configuration and redeploy the bridge development
  cluster for acceptance.

## MFA revocation and recovery-state hardening

- Amend the unreleased password-recovery schema with nullable identifiers for
  the exact TOTP device or passkey that completed recovery MFA. Keep them as
  audit/revocation snapshots without foreign keys so deleting the factor can
  invalidate the recovery while retaining which factor was used.
- Share only factor-level TOTP and WebAuthn proof verification, replay/counter
  updates, and enabled-state revalidation. Keep ordinary authentication and
  password recovery as separate authority state machines. Serialize both
  verification and supported factor management in the lock order user, then
  authority, then factor.
- Disabling or deleting a factor invalidates active recoveries verified with
  that exact factor. Unrelated factor changes remain usable. Disabling MFA for
  the whole account invalidates every active recovery and MFA authentication
  token. A TOTP fallback code may disable its own factor and still complete the
  recovery currently using it; other active recoveries verified by that factor
  are invalidated. Using the fallback code in ordinary authentication has no
  current recovery to preserve, so it invalidates every active recovery tied
  to the disabled factor. Lock the current recovery and every relevant
  recovery authority together in one ID-ordered query before the factor.
- Keep WebAuthn failure accounting schema-free. Permit exactly one outstanding
  two-minute passkey challenge per recovery: a new begin replaces the previous
  recovery challenge and any recognized finish attempt consumes it, including
  assertion type or ID mismatches reported by the WebAuthn library. Ordinary
  authentication challenges remain independent. Normalize failures only around
  the untrusted WebAuthn parser and verifier calls so every malformed assertion
  follows the handled failure path without hiding database failures.
- Deleting an OAuth client invalidates its active recoveries before nullifying
  the request association and finishes and scrubs queued submissions linked to
  it. Enqueue and deletion share the global queue lock, and the worker locks
  and rechecks its submission before the client row, so queued work cannot
  become a generic recovery after client deletion. A recovery completed before
  deletion can show its completion alert only through the current default
  client; active flows do not silently move to another client.
- Deploy the amended additive migration before the new API code and keep the
  password-recovery feature disabled until every API process runs the new
  revision. Older code ignores the nullable columns, but it cannot record the
  exact factor, so no mixed-version recovery must be admitted. Rolling back to
  older code remains compatible; the down migration discards only the new
  factor snapshots.
- Add deterministic two-connection MariaDB coverage for both verification-first
  and revocation-first TOTP/passkey schedules, plus route, model, migration,
  OAuth-client deletion, challenge replacement, and ordinary-authentication
  regressions. Run mandatory fresh-agent review before long integration, repin
  downstream revisions, and reset/redeploy the bridge development cluster.
  Production deployment and KB publication remain operator-only.

## Pending lifecycle authentication and recovery prefill

- Treat a user's latest requested lifecycle state as part of login eligibility.
  Permit only active and suspended materialized/requested states for new Basic,
  token, OAuth, MFA continuation, required-reset, and password-recovery
  authority. Recheck this predicate under the existing user locks before
  consuming an MFA factor, issuing credentials, or writing a password. Keep
  already-issued API and OAuth sessions resumable until the lifecycle
  transaction chain closes them, while rejecting new OAuth codes and refreshes
  after a destructive state is requested.
- Keep public authentication errors neutral and retain the existing localized
  invalid-login result. Do not add schema, API, mail-template, or user-facing
  copy changes.
- When a failed OAuth credential form retains its login value, append that exact
  bounded value to the password-recovery link as an encoded `identifier` query
  parameter. Never copy the submitted password, resolve the value to an
  account, or disclose whether it exists. The recovery request form uses the
  existing escaped identifier value and continues to preserve OAuth client and
  locale context.
- Keep the lifecycle guard and UI convenience in separate commits. Run focused
  model, route, OAuth, queue, lint, and browser coverage, then mandatory
  fresh-agent review before long integration. Repin the exact vpsAdmin revision
  in the KB contract and production configuration, refresh the existing bridge
  development cluster without a schema reset, and leave production deployment
  and KB publication to the operator.

## Current-default rebase and declarative notification templates

- Rebase all four feature branches onto their current upstream default
  branches. Preserve the password-recovery feature as an additive layer over
  the new security-advisory and notification-template work on vpsAdmin master.
- Move the built-in recovery and password-change mails from the removed legacy
  `api/mail_templates` layout into
  `api/notification_templates/templates/<name>/email`. Keep subjects in
  channel-specific `*.subject.erb` variants and adapt the loader specs to the
  new parsed-variant API. Do not change the reviewed Czech or English copy.
- Move the branded templates into the external repository's new
  `templates/<name>/email` package layout. Keep its sender metadata and exact
  automated-mail footer contract, and validate the complete package with the
  vpsAdmin notification-template checker.
- Pin both exact primary revisions in production configuration. `int.api1`
  packages the branded source and runs
  `vpsadmin-notification-templates.service`, which transactionally reconciles
  the shared database before the API or supervisor can start. The
  password-change template must exist before either upgraded API runs because
  that notification is independent of the recovery feature flag.
- Keep api1 masked during the configuration switch. Verify successful template
  reconciliation and both language variants in the database before running the
  additive migrations or starting the new API. Switch api2 immediately after
  api1 is healthy, then deploy both WebUI instances, the auth proxy, and
  monitoring. Enable recovery only after OAuth client settings are verified.
- Rollback remains compatible. Disable recovery first and return every process
  to the preceding configuration. The additive schema can remain, and
  reconciliation deliberately preserves template rows omitted by the restored
  source, so the recovery and password-change templates are harmless to old
  application code. Reversing migrations remains destructive and requires the
  existing database-backup procedure.
- Repin the independent KB contract to the exact rebased vpsAdmin revision
  while retaining the new default-branch security-advisory contract. The
  password-history navigation remains additive and requires no new screenshot
  concept or reader-visible managed-page change.
- Run quick API, migration, template, PHP, localization, lint, hook, KB, and
  documentation checks on the committed heads. Obtain the mandatory
  fresh-context review before the long WebUI VM tests, seven configuration
  builds, bridge-cluster refresh, and current-head CI closure.
- Refresh the existing bridge cluster without resetting its database. If the
  current template API exposes a dev-cluster seed incompatibility, update the
  workspace seed to call the public transactional reconciler, verify its Nix
  syntax and real activation, commit it on workspace `master`, and obtain a
  fresh mandatory review of that additional code change.
- Shared dev-cluster template installation supports the declarative API and
  package layout introduced by vpsAdmin `ea956e5e`. Reject an older paired
  worktree during Nix evaluation with instructions to disable external template
  installation. Production rollback is unaffected because it does not use the
  workspace seed.
