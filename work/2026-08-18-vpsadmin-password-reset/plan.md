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
