# OAuth theme and declarative branding implementation brief

Status: accepted implementation brief, amended 2026-11-26.
User direction, relayed by the lead: "we don't need to keep core.logo_url sysctl
fallback. aside from that, implement it". This authorizes implementation with
declarative branding only; it does not authorize deployment or integration.
Owner: architect0. The lead accepts package release and implementation results.

## Scope and accepted behavior

Add light, dark and automatic appearance to vpsAdmin's OAuth browser pages,
using compact accessible sun/moon/system icon choices. Use the existing
vpsf-status palette and transparent site logos. Supply site branding through
vpsfree-cz-configuration, with bundled vpsAdmin branding when unconfigured.
Preserve the selected preference from React or HaveAPI documentation through
authorization and back to that client. A choice made on the OAuth page wins
on return. PHP does not participate in theme exchange.

Keep the existing authentication, forms, errors, MFA, recovery and redirect
mechanisms. No new theme service, UI framework, database preference, shared
domain cookie, status-service dependency or generated API-client work is
proposed. Existing React account settings remain the owner of its preference;
documentation and OAuth use browser-local preferences.

## Evidence baseline

Source inspection uses canonical bare clones; these are locally available
remote-tracking heads, not evidence of current production deployments. No
project worktrees, servers or test executions were needed for this proposal.

| Repository | Inspected head | Evidence owner |
| --- | --- | --- |
| vpsAdmin | `1bf7c120beaf21f7fd30f4b75441d4b835bc57af` (`origin/master`) | implementer0 |
| React vpsadmin-webui | `e311b1c0af0f50fa4c6f6ce83c514c1a866eb042` (`origin/main`) | implementer1 |
| HaveAPI | `cd6b1d1d0561ead050755171d25d0aa7269e2b82` (`origin/master`) | implementer1 |
| vpsfree-cz-configuration | `0b648b23c76977bc603bd57b671035920314b767` (`origin/master`) | implementer0 |
| vpsf-status, reference only | `8e17ccb9728bed308bbe7d67126eb84dfdf8a81c` (`origin/master`) | architect0 |
| web, dark-logo provenance only | `7fec3e3ccc5a1aa41bad7f06f83d01fa6cd15fe9` (`origin/master`) | architect0 |

The request is preserved verbatim in [plan.md](plan.md). Workspace project,
session, documentation, verification and team procedures, relevant repository
instructions and documentation entry points were read. Team identity/settings
were verified with `dev-session current` and `dev-session team list ... --as-is`:
`delegated_4`, architect0 Astra/xhigh; implementers Sol/xhigh with saved
workspace-write access. No peer-session material is used.

## Settled presentation contract

Use semantic CSS variables in the existing OAuth templates, including native
form controls, links, buttons, errors, warnings, focus and disabled states.
Cover each rendered authentication state rather than styling only the first
password screen. Keep the existing form hierarchy and feedback placement.

| Token | Light | Dark |
| --- | --- | --- |
| Page | `#f3f6fb` | `#111f33` |
| Panel | `#ffffff` | `#1f3959` |
| Raised surface | `#e8eef7` | `#294565` |
| Text | `#16273f` | `#f8fafc` |
| Muted text | `#475569` | `#c3cede` |
| Link / focus | `#9a450b` | `#ffb16c` |
| Border | `#68768a` | `#7186a2` |
| Danger text / surface | `#b91c1c` / `#fff0f0` | `#fca5a5` / `#4b232b` |

Source: vpsf-status `public/status.css`, `public/theme.js`,
`templates/layout.tmpl`, `docs/reference/appearance.md` at the head above.
Copy the relevant semantic colors, not the whole status-page stylesheet or
Bootstrap 5 integration into OAuth's Bootstrap 4 page. Test contrast in the
actual OAuth components; a palette alone does not prove their accessibility.

Use one compact native radio group, with nonvisual labels and visible focus
and selection, beside the existing page header. Make touch targets at least
44px while keeping the icons small. Avoid a new settings menu for three choices.
`auto` follows `prefers-color-scheme`, including later OS changes, without
becoming a stored explicit light/dark choice. Apply preference before first
paint; CSS supplies automatic fallback without JavaScript. Storage access is
guarded and failure must not block login or switching for the current flow.

The reusable files are `public/vpsfree.png` (540x185 RGBA, SHA256
`836faaf1594fbc750c5903f0b335f6556fae6fb93da77cfd124f1d6b6c02d740`)
and `public/vpsfree-dark.png` (173x50 RGBA, SHA256
`c843b27b0695fbcffc0d341a7a23194e025bb6ce8537a4fd23092fc624674e5a`).
Dark blob `41a78b8dc4f2ee76d847453b7d2da85ae4f037f6` exactly matches
`web:obrazky/vpsFree-bile.png`. Copy both into site configuration with a short
source note. Preserve each aspect ratio, fit them in a stable header box and
avoid a white backing plate for the supplied dark logo. No new artwork or
runtime/build dependency on vpsf-status is needed.

## Settled theme exchange contract

The preference enum is `light | dark | auto`. Effective scheme is only
`light | dark` and is resolved in the browser; do not send it in place of
`auto`. React maps its existing `system` value to/from `auto` at the boundary.

| Field | Meaning |
| --- | --- |
| Request `theme` | Initial allowlisted preference; optional cosmetic input |
| Request `theme_return=1` | Explicit support for a returned theme extension |
| Success response `theme` | Current selected preference, only for opted-in transactions |

The separate return capability is necessary: old HaveAPI documentation rejects
unknown callback fields. A server-side default or the OAuth selector must
never silently opt an older client in. Preserve the return bit separately from
the evolving preference in form/continuation fields. Only the exact scalar
`1` enables it. Reject or ignore malformed theme inputs according to each
endpoint's existing strict-query rules; never reflect arbitrary values into
HTML, CSS, scripts or redirect parameters. Normalize values at every boundary.

Incoming valid preference takes precedence over the OAuth origin's saved
preference; absent/invalid preference falls back to saved preference, then
`auto`. Merely arriving from a client does not overwrite the OAuth saved
preference. An explicit selector action updates the current flow and the
OAuth origin's saved preference. Forms/continuations retain that current value
even when browser storage is unavailable.

Only after a valid success callback, state validation and successful token
exchange does an opted-in client use the returned value; absent/invalid values
retain the initiating preference. A selector change therefore follows the user
back after successful sign-in. Cancellation, denial, token-exchange failure and
invalid/expired/mismatched state never apply a response theme. Errors and retry
links use the initiating preference, which the client retained separately from
opaque state. Provider error response payloads stay unchanged. This success-only
boundary was selected with the lead after considering error callback propagation.
Do not rewrite, encode theme inside, or weaken OAuth `state`, PKCE,
redirect-URI validation, origin checks, CSRF, scopes or callback replay handling.
Do not put tokens, credentials, state or return destinations in theme storage.

## Provider and complete browser flow

Source: vpsAdmin `api/lib/vpsadmin/api/authentication/oauth2_config.rb`
(`handle_get_authorize`, `handle_post_authorize`, `render_authorize_page`),
`oauth2_authorize.erb`, `password_recovery.rb` and `password_recovery.erb`;
HaveAPI `servers/ruby/lib/haveapi/authentication/oauth2/{provider,config}.rb`.

The current provider has credentials, TOTP/passkey MFA and forced password-reset
steps, plus cancel. It has no consent page; do not invent one. All existing
credential/MFA/reset errors and WebAuthn feedback stay in their normal template.
Preserve normalized theme and the independent return bit across every form,
rerender and method switch. Shared appearance code must update hidden values
when the selector changes. Existing passkey verification, CSRF/auth tokens,
password/recovery validation and retry limits remain unchanged.

HaveAPI currently validates client/redirect, invokes the configuration handler
and approves the Rack::OAuth2 response. Rack::OAuth2 2.2.1 has no `extra` response
API. Add one narrow config callback, defaulting to no extra parameters, at the
successful authorization boundary. A HaveAPI-owned per-response adapter extends
success `protocol_params` with the normalized `theme` field; it must preserve
the original `code`, `state` and `session_state` and never overwrite standard
OAuth fields. Initially allow only this explicit cosmetic extension. Do not
patch Rack globally, rewrite arbitrary Location headers or modify redirect_uri.
The vpsAdmin override returns theme only for exact `theme_return=1`. Apply the
same hook to successful GET/SSO and POST paths; SSO may never render a page.
Other Config subclasses retain their existing behavior through the empty default.

Recovery is included for visual continuity: request, sent, email landing,
verification, password, completion and invalid/error pages use the shared colors,
logos and selector. Carry the enum through same-origin links/forms/redirects.
Recovery is a separate flow, not continuation of an old OAuth state: keep the
registered `authorization_start_uri` unchanged on return to service; do not
append new fields to arbitrary external clients. Its new login starts normally.
Same-browser recovery can reuse the OAuth origin's saved choice. A fresh email
link on another browser uses that browser's saved choice or auto. Do not add
theme to recovery tokens, email URLs, database rows or authorization records.
The return-capability bit is needed only while continuing an OAuth transaction;
it does not grant a recovery flow authority to extend an external return URL.

Without JavaScript, CSS still follows the OS, valid explicit request themes
render correctly and native forms retain their fields. Hide enhanced switches
until their handlers are installed; no-script persistence of a newly selected
theme is not a new requirement. A later generic consent page, if one is added,
must follow the same contract, but is outside this implementation.

## Declarative branding and fallback

Reuse `vpsadmin.deploymentConfig` → `config/deployment.json` →
`API::DeploymentConfig.dig`. Sources are vpsAdmin
`nixos/modules/vpsadmin/{main,api-app}.nix`,
`api/lib/vpsadmin/api/deployment_config.rb`, `api/models/sys_config.rb`, and site
`cluster/cz.vpsfree/vpsadmin/common/{api,frontend}.nix`.

Use nullable strings under `deploymentConfig.authentication`:
`logo_url`, `light_logo_url`, `dark_logo_url`. Per-scheme precedence is its
override, declarative common logo, then bundled vpsAdmin wordmark. Empty entries
inherit. There is no `core.logo_url` fallback. Validate external logo URLs using the
existing recovery rule (absolute HTTP(S), host, no userinfo or fragment) and
escape them in HTML. Include both selected external origins in recovery's
existing CSP so automatic scheme changes work. Do not accept asset URLs from
browser parameters.

The concrete no-configuration fallback is a small bundled inline SVG vpsAdmin
wordmark under `api/lib/vpsadmin/api/authentication/assets/`, loaded only from
that fixed packaged path by the shared branding renderer. Its foreground uses
the page's theme color. This needs no new HTTP route, remote fetch, PHP asset
dependency or `data:` CSP exception. The API package already copies the API
tree. The existing PHP `webui/public/template/vpsAdmin-logo.png` is available
as visual reference but is not packaged by the API. Test that the bundled asset
is present in the packaged API and legible in both schemes.

Copy the two supplied site PNGs to `configs/vpsadmin/auth-assets/`. In site
`common/frontend.nix`, serve them with exact nginx locations, e.g.
`/auth-assets/vpsfree.png` and `/auth-assets/vpsfree-dark.png`, using immutable
Nix-store aliases. Derive the normal/maintenance auth vhost names from existing
`config.vpsadmin.frontend.auth.*.virtualHost` fields. Set absolute HTTPS logo
URLs in `common/api.nix` for both API instances. Assets and config are owned by
the configuration repository; there is no new status-service dependency.

The user explicitly accepted removal of the legacy setting's compatibility
behavior. Remove its registration in `api/models/sys_config.rb`, its runtime
reads and obsolete seed/test setup. The bounded source check also found a read
in `authentication/webauthn_register.rb` and its template/spec: use the shared
declarative/default branding resolver there so removal does not break that page.
This is a logo-source adjustment, not a new WebAuthn registration theme flow.
No PHP consumer was found at the inspected head.

Do not create a database migration solely to delete dormant setting rows; their
presence must not influence new-code branding. Installations that configured
only `core.logo_url` now use the bundled logo until declarative branding is set.
Document this user-directed compatibility change. A single declarative common
logo is reused for both schemes; automatic recoloring of arbitrary artwork is
unsupported. Operators wanting matched dark branding provide both variants.
No schema/data migration is needed.

## Client entry, return and persistence

### React and BFF

Sources: `index.html`, `src/app/{auth,uiSettings}.tsx`,
`src/app/uiSettingsModel.ts`, `src/lib/auth/oauth2Client.ts`,
`src/lib/runtimeBootstrap.ts`, `bff/server.js` and `bff/oauth-error-page.js`.
The UI stores `system|light|dark`; the ThemeProvider resolves the effective
scheme, and the head script applies it before paint. Account settings currently
replace local settings after login. `/session.json` accepts exactly its three
existing token/session fields, so adding a theme there would break older clients.

Use one shared entry-URL helper for public Sign in, login page, expired-session
and retry paths. Add the current preference and return opt-in to the BFF start
URL and its authorize redirect; cover the supported legacy browser OAuth path
as well. Retain the initial preference beside the existing pending state (not
inside its random value). Legacy sessionStorage validation remains fail-closed;
guarding optional localStorage never permits login without valid state storage.

After state consumption and successful code exchange, the BFF writes one
short-lived host-only cosmetic cookie with exactly two allowlisted preferences:
`selected` is the valid returned preference, or the initiating preference when
the response has none; `initiating` is the preference retained with this pending
login attempt. These are preference enums, not resolved colors. Both normalize
to `light|dark|auto`, with React's `system` mapped at the boundary. The bounded
two-value payload contains no auth data, state, return destination or extensible
metadata envelope. Validate both fields when writing and consuming it; ignore
and clear malformed payloads rather than guessing the initiating preference.

The cookie is Secure on HTTPS, SameSite=Lax, host-only, scoped to the application
and readable by the first-paint script. Use a dedicated name and a 120-second
Max-Age; clear on consumption, and clear stale values on a new flow/failure.
It is not an authentication authority. No `/session.json` schema, callback URL
trust, endpoint, second cookie or optional sessionStorage baseline is added.
The legacy browser callback uses the same handoff after its existing validation
and successful exchange, preserving the existing hard reload. Errors keep the
initial preference in their existing error/retry paths, never from failed
callback fields. Lead accepted this bounded two-value clarification on
2026-11-26: it preserves no-record save semantics even when optional browser
storage is denied. Document the meanings once in the client helper and its tests.

The head script reads but does not prematurely delete the handoff. The settings
provider consumes it into memory, applies it immediately, then merges only the
theme into the loaded account settings. Preserve every other server setting and
the original saved-server snapshot so the existing debounce writes a difference
once; retain the pending preference through settings-load retry and clear it
after incorporation. Guard localStorage acquisition/read/write. This also works
with localStorage denied and otherwise functional OAuth cookies.

Recommended visible persistence: the preference carried through successful
login wins for that login, including auto; it becomes the React browser setting
and the account theme through the existing settings save when account settings
are enabled. With an existing account record, save only if different. With no
record, retain the existing no-implicit-write behavior when selected equals
initiating; when they differ, the actual OAuth theme change can use the ordinary
explicit-settings save path. Compare preferences, so auto and explicit dark are
different even while the OS is dark. A missing/invalid initiating baseline is
not evidence of a change and must not create an account settings record.
An unchanged login therefore need not create an account settings record. With
server-backed settings disabled, persistence remains local. No new preference
service or separate synchronization loop is required.

Bounded package-C refinement approved by the lead: necessary optional-display-
storage guards brought the existing mutation-lock hook to 516 lines against its
500-line structural limit. Extract only the storage-event display reader into
the existing `localMutationLockStorage.ts`. Preserve storage-read timing, the
captured timestamp, per-object handling and corrupt-value parsing. Return only
the bounded display result or no update. Mutation acquisition, writes, reducer
behavior and OAuth remain unchanged; this does not introduce a general storage
abstraction or a structural-debt exception.

Implementer2 owns the focused storage-event, integrity, type and structural
checks and consolidates the successor before the same independent reviewer
assesses the affected architecture/risk lanes. This refinement does not change
package B's CI source-selection brief or require additional architect checks.

### HaveAPI documentation

Sources: `servers/ruby/lib/haveapi/documentation_oauth.rb`,
`public/js/documentation.js`, `views/version_sidebar/authentication_control.erb`,
and `doc/en/{documentation-ui,documentation-oauth}.md` (Ruby server paths are
relative to `servers/ruby/` where applicable).

Documentation uses ordinary same-window redirects, not auth postMessage or a
popup. Add theme/opt-in to the existing bounded login target builder and click/
auxclick path. Retain initiating theme as an optional bounded field in the
encrypted pending cookie. Accept old pending records without it; keep state,
PKCE, cookie purposes, lifetime, origin checks and bounded return fields intact.
Extend the strict callback allowlist only for scalar `theme`, and use it only
for a successful pending attempt that opted in. Duplicates and malformed
structures retain strict rejection. Invalid/unknown enum values cannot replace
the saved preference. Authenticated cookie shape and API credential isolation
remain unchanged.

After validated success/exchange, a short-lived host-only cosmetic handoff
cookie lets the existing documentation bootstrap merge only theme into
`haveapi.docs.preferences.v1`, before applying the page scheme, then clear it.
Keep language, client and example-detail preferences. This avoids adding a new
public return URL or changing documentation navigation selectors. Handle
storage failure in memory, with cookie-based handoff for the immediate return.

The existing callback error response is an unstyled paragraph and retry link.
Reuse a minimal existing documentation appearance wrapper and initiating theme
for that response/retry; do not build a separate status screen. Valid pending
return fields may be retained under the existing bounded return validator; never
take a return URL from an error. Switch user adds the current theme to its native
CSRF-protected form and the fixed login restart after successful revocation.
Ordinary logout retains its existing scope and behavior. Failure/cancel retains
the current/initiating docs preference and existing session rules.

## Compatibility, deployment and recovery

| Combination | Supported behavior |
| --- | --- |
| Old client → new provider | No opt-in means no new callback field; provider may use local/auto appearance |
| New client → old provider | Unknown request extras are ignored by current provider; client retains initial preference without response theme |
| New client → new provider | Successful callback returns selected preference; errors retain initiating preference |
| New BFF → old React | Existing bootstrap/session JSON unchanged; cosmetic cookie is safely ignored and expires |
| New React → old BFF | Missing handoff keeps local preference and existing login behavior; full round-trip requires paired rollout |
| Old docs pending cookie → new docs | Optional new fields absent; normal state/PKCE flow remains valid |
| New pending cookie → rolled-back docs | Old exact-key reader may reject this in-flight login; retry starts a fresh one |

PHP makes no request changes, shares no theme storage, and receives no callback
theme. OAuth itself can use its origin preference when PHP starts login; PHP
remains light. The `core.logo_url` setting is intentionally removed from the
registered public sysconfig surface. No generated SDK, protocol-version, token,
database-schema or node-interface change is otherwise expected. Assess the
final source diff, including any declarations derived from the sysconfig
registry; only actual declared-contract changes trigger client synchronization.

### HaveAPI source-package identity

The lead accepted an exact source pin through vpsAdmin's existing
`packages/ruby-source-gem-config.nix` helper, limited to the `haveapi` server
gem. Keep unrelated client gems unchanged. A fixed repository revision/hash
must identify the completed A+D source; its prepared derivation must include
shared documentation produced from that same source and an explicit shipped-file
inventory suitable for an archive without `.git`. Both packaged API and API dev
shell use that prepared input. Check actual packaged Ruby code, static assets and
documentation routes, not just successful Nix evaluation.

The inspected source declares HaveAPI 0.32.0, while vpsAdmin currently requires
the published 0.32.2 gem. Never relabel source as 0.32.2 only in Nix, patch version
strings to imply a release, or silently lower the ordinary registry requirement.
Before the final pin, package B must establish the source's relationship to
required 0.32.2 behavior and reconcile effective Gemfile/lock/runtime identity.
An isolated source override can use its honest source version; ordinary registry
installs retain their supported minimum. Any schema-export tooling guard remains
truthful to its selected declaration, with its deliberate published tooling
override assessed separately. No package publication is authorized or needed
merely to prepare this source-pinned implementation.

Settled package-B route (2026-11-26): use the existing source-gem normalization
pipeline in `tasks/gem_updates.rb`, not a second patch stream against the registry
gem. The owners' bounded comparison of source baseline
`4c126e3b0ed259b2be18a241a0c4c716046eb816` with `v0.32.2` found no lost server
runtime fixes: differences were the source version, compatible client constraint
and a documentation label. Keep the exact comparison and final A+D revision in
the package evidence; this source comparison is not packaged-runtime validation.

- `api/Gemfile` uses actual `= 0.32.0` with a path only when the explicit
  `VPSADMIN_HAVEAPI_PATH` override selects the prepared source; its ordinary
  branch retains `~> 0.32.2`.
- `write_api_gemfile` emits a deterministic package Gemfile with actual
  `= 0.32.0`, rather than retaining the environment-dependent branch. Generate
  its lock/gemset against the prepared source and reuse the existing
  `normalize_lockfile` / `normalize_gemset` handling. Final generated metadata
  contains no transient checkout path. The package's runtime effective Gemfile,
  lock, gemspec and `HaveAPI::VERSION` must agree without relying on a host
  environment override.
- The prepared fixed-source derivation copies the shared docs and replaces only
  the archive-unsafe Git-derived file list with an equivalent shipped-file
  inventory. The same derivation supplies the API dev-shell path and package
  gemConfig. Published 0.32.2 client gems remain unchanged.
- Keep the schema-export tooling's deliberate published `= 0.32.2` override
  and original ordinary-declaration guard. Since merely retaining that guard
  would not stop the new source branch from taking precedence, reject inherited
  `VPSADMIN_HAVEAPI_PATH` for this isolated exporter, or use its existing isolation
  boundary to remove it explicitly. A focused check must prove the exporter
  cannot silently resolve the source branch. No schema export/regeneration is
  required solely for this packaging change.

The selected route is implementation-ready; the final immutable pin and actual
packaged/dev verification remain package-B deliverables. Respect any lead-owned
source/check freeze before editing the affected Gemfiles.

Native API CI must select that same source before Bundler installs dependencies.
The initial full/core foundation jobs at vpsAdmin
`1d3f5bcae05f3d44ca9ad22011721202c48c0124` selected ordinary RubyGems HaveAPI
0.32.2 and failed the two success-callback theme cases. This is dependency
selection evidence; it does not establish a product defect in the tested source
package. The correction reuses the repository's existing Nix-install workflow
convention: evaluate the locked nixpkgs input, build only
`packages/haveapi-source.nix` with `callPackage`, and export the resulting
prepared path as `VPSADMIN_HAVEAPI_PATH` before `ruby/setup-ruby` invokes Bundler
in both API spec matrices. Keep the ordinary Gemfile branch intact.

No new metadata parser, fetch/unpack helper, pin authority, flake output or
general CI-runner conversion is needed. Key Bundler's cache by the selected
prepared-source identity so an unchanged 0.32.0 version string cannot reuse a
different source. Before database/spec setup, assert the loaded HaveAPI gem path
and expected response-hook interface come from that prepared input; append its
identity and loaded server/generator versions to the existing environment
receipt. Preserve full/core topic manifests and coverage aggregation. First
validate source selection and the two affected callback cases; let the normal
CI coverage run on the corrected committed head. Other Ruby components retain
their own dependency setup. The API owner retains diagnosis/checks and the lead
applies the existing narrow-fix/affected-lane review policy.

Bounded CI environment correction: the lead's corrected-B62 hosted evidence
passed source provenance for exact HaveAPI
`439beea801df3139b7154283a171f53c68295939` / server 0.32.0 / generators 0.32.2,
then ran zero examples because MariaDB received EACCES while creating files
under the inherited install-nix-action `TMPDIR` in `runner_work/_temp`. The
AppArmor explanation remains unproven; record the observed failure without
claiming that mechanism.

Set step-level `TMPDIR: /tmp` only on **Run RSpec** in both full/core jobs. This
restores the prior temporary-database location while preserving the selected
source, cache, runner and test contracts. Do not change database code, relax
permissions or alter the Nix installer environment. Package B owns a faithful
inherited-temp/step-environment `Dir.mktmpdir` proof and the official TMPDIR
assignment evidence, then hooks/history consolidation and the same reviewer's
affected general/risk lanes. Final hosted execution supplies the runtime proof;
do not repeat database/spec batches merely to diagnose this environment setting.
This note releases no held provider, user or empty-branding fixture work and
does not release package E before the lead's final-B disposition.

### Explicit documentation generator profiles

The first actual-source API check failed before any examples ran: the server
reports 0.32.0 while the installed Go generator reports 0.32.2. Rust and
TypeScript have the same mismatch. This exposed the implicit profile default,
not a requirement to source-package every generator. At HaveAPI
`439beea801df3139b7154283a171f53c68295939`,
`servers/ruby/lib/haveapi/documentation_clients.rb#validate_config` defaults
`generator_version` to the server version; each loader checks that configured
version against its actual installed generator. The existing explicit override
is documented in `doc/en/client-examples.md` under Configure an API client.

Lead decision, 2026-11-26: vpsAdmin sets fixed `generator_version: '0.32.2'`
on each of its existing Go, Rust and TypeScript profiles in
`api/lib/vpsadmin/api.rb`. Keep the exact source server's honest 0.32.0 identity
and published 0.32.2 generators/client runtime. The existing configured-versus-
installed mismatch checks remain active. Do not derive the expected value from
the loaded generator's VERSION, relabel versions or expand the source-gem
closure. This uses the supported explicit profile interface and avoids another
three source packages and their packaging requirements.

Replace vpsAdmin's old server/generator version-equality assertion and prose
with this independently pinned profile policy. Keep explicit profile versions,
installed dependency locks and actual generator interfaces aligned on future
updates; a mismatch must still fail clearly. This changes the bundle's previous
same-version convention, not generated SDK identities, API schemas or HaveAPI's
profile-validation behavior. Update `docs/api-client-examples.md` and the
focused `api/spec/lib/vpsadmin/api/documentation_clients_spec.rb`; the lead
applies the writing pass before commit. Include this contract/dependency change
in B's ordinary final review with all applicable lanes, without an extra review
gate or release.

Before another behavior batch, B must run a database-free check in the actual
selected environment which requires the real server and three real generators,
records their versions/source paths and registers all three unchanged package
identities with explicit 0.32.2 expectations. This must prove their profile
interfaces load, rather than merely printing version constants. Then run the
smallest existing mounted-profile/renderer examples needed to prove actual
rendering and resume the affected OAuth behavior checks. Do not repeat a broad
documentation suite to diagnose this known setup mismatch. B owns evidence and
failure diagnosis; source inspection here is not a passing runtime result.

Proposed rollout, under later deployment authority:

1. Land/package compatible HaveAPI response support and docs consumer changes;
   update vpsAdmin's pinned HaveAPI dependency using its existing packaging flow.
   A required public package release needs its own approval. Development can use
   an exact compatible source/package input without inventing a version.
2. Prepare and serve the static site logo paths on normal/maintenance frontends
   before enabling their URLs. Build the API workers with matching framework,
   provider, templates and bundled assets. Activate new branding only on workers
   with the new provider; restart all workers because deployment config is cached.
3. Roll out React frontend and BFF as their normal matched release. Enable docs
   theme exchange with the upgraded documentation package. Mixed-version fallback
   keeps authentication working but does not claim full theme round-trip until
   both ends are new. API docs live in that same API/package deployment.
4. Verify real chosen revisions/asset responses and the isolated browser matrix.
   No production accounts or mutations are needed to prepare these checks.

Site changes are prepared last against settled app/package interfaces; frontend
asset activation precedes their API configuration use. Use confctl channel
commands for exact input updates, and inspect the complete lock/input graph.
No vpsAdminOS or kernel change is required. Integration is a separate explicit
repository/target decision; implementation authorization performs none of these
operations by itself.

Rollback restores the previous matched API/HaveAPI/config and React/BFF releases;
older binaries use their previous configuration and setting semantics. Do not
preserve a legacy fallback in new code to support rollback. No setting-row
deletion is part of this change; exact old branding remains dependent on the
old deployment's configuration, not the new declarative keys. New JSON branding
keys are ignored by the old API. Extra static assets may remain harmlessly
available. Theme localStorage values and cosmetic cookies can be ignored/expire;
there is no auth/data conversion. An in-flight new documentation pending cookie
may require one fresh sign-in after rollback. Do not rotate auth secrets, delete
clients or clear authenticated sessions merely to roll appearance back.

## Implementation packages

These accepted briefs define authorized implementation scope. The lead allocates
packages, confirms capacity/current heads and coordinates short shared Git
mutation windows. All owners supply exact base/head, changed files, checks,
remaining gaps and whole-branch history/migration provenance. No migrations are
planned. Independent final review is lead-owned.

| Package / owner | Files and deliverable | Dependencies and acceptance |
| --- | --- | --- |
| A: HaveAPI response extension / implementer1 | `authentication/oauth2/{provider,config}.rb`, `spec/authentication/oauth2_spec.rb`, provider-facing contract documentation | First; safe success-only hook for POST and SSO GET, empty default, only bounded theme extension, unchanged state/code/redirect behavior |
| B: vpsAdmin OAuth and branding / implementer0 | `authentication/oauth2_config.rb`, both OAuth/recovery ERBs and recovery controller; small shared appearance/branding helper and bundled SVG; `api/models/sys_config.rb`, obsolete test seed/setup, WebAuthn registration controller/template/spec for logo source only; existing OAuth/recovery specs; `docs/oauth-appearance.md` plus index; dependency/package files for A | A interface settled; complete forms/errors/MFA/reset/recovery, enum/opt-in propagation, declarative/default branding with no legacy setting reads or registration, CSP and packaged assets |
| C: React/BFF exchange / implementer2 | `index.html`, `src/app/{auth,uiSettings}.tsx`, settings model, `src/lib/auth/oauth2Client.ts`, small enum/URL helper, `bff/{server,oauth-error-page}.js`; necessary entry/retry call sites; listed unit/BFF/browser tests and design/work log docs | Stable wire contract; may proceed alongside B/D; both OAuth paths, prepaint/memory handoff, account merge, errors/retries and old/new compatibility |
| D: HaveAPI docs exchange / implementer1 | `documentation_oauth.rb`, `public/js/documentation.js`, `views/version_sidebar/authentication_control.erb`, existing shared/error appearance pieces; docs OAuth/fixture/JS tests; `doc/en/{documentation-oauth,documentation-ui}.md` | After A owner has reported completion; stable wire contract; strict callback handling, optional pending data, clean return, switch/retry/local persistence |
| E: site assets/config / implementer3 | `configs/vpsadmin/auth-assets/*`, `cluster/cz.vpsfree/vpsadmin/common/{api,frontend}.nix`, config README and existing OAuth operations guide; exact channel pins after app acceptance | B/D interfaces and asset paths settled; logos served before reference, API1/API2 + auth frontends evaluate/build, source provenance and rollback preserved |

A and D share a repository/owner and run sequentially. B/C can proceed against
A's settled contract with compatible development dependencies; their final
integration checks require the actual shared package. E may prepare static assets
independently, but no config/pin activation occurs before compatible packages.
All application edits belong to implementers. Architect owns this brief and
consequential design clarification; lead owns scope/release/acceptance.

## Checks and acceptance evidence

Planning performed source inspection only. The commands below are future checks,
not reported passes. Implementers read the current repository procedures before
running them; uncertain/long checks use the monitor skill.

Quick checks, then committed independent review, then longer integration:

- vpsAdmin: inside `nix develop .#api`, touched-file RuboCop and focused
  `bundle exec rspec spec/lib/vpsadmin/api/authentication/oauth2_config_spec.rb
  spec/api/routes/password_recovery_route_spec.rb`, plus shared-helper specs.
  Use required full/core plugin modes and retain exact topic coverage. Assess
  custom-route coverage only if implementation adds routes; the inline default
  asset does not require one.
- HaveAPI: prepare docs with the repository's `make doc`; use the server Ruby
  shell and focused `spec/authentication/oauth2_spec.rb`,
  `spec/documentation/oauth_spec.rb`, `oauth_fixture_spec.rb`; run
  `node servers/ruby/spec/client_examples/assets/documentation_test.cjs`.
- React: pinned Nix environment, typecheck and focused OAuth/settings/layout
  tests (`oauth2Client.test.ts`, `OAuthPages.test.tsx`, `uiSettings.test.tsx`,
  `uiSettingsModel.test.ts`, `PublicLayout.test.tsx`), `npm run test:bff`,
  `npm run typecheck:bff:core`, and `npm run audit:design-docs`. Relevant BFF
  homes include `server.test.js`, `security.test.js`, `oauth-error-page.test.js`.
- Site: Nix formatting and selected configuration evaluation; after review,
  normal builds for API1/API2 and the auth frontend owners. Do not select node
  builds. Full HaveAPI docs checks, package builds, vpsAdmin `services-up`, and
  applicable browser suites follow final review under each repository's rules.

Browser acceptance uses isolated accounts/fixtures, desktop and narrow/touch
views, and captures actual rendered light/dark screens. Cover:

1. All three preferences at entry and return, automatic OS change, no unwanted
   first-paint flash, keyboard selection and accessible names, contrast,
   autocomplete attributes and filled-control appearance,
   disabled/loading/errors, blocked localStorage and no-script fallback.
2. Password, invalid credentials, TOTP and passkey success/failure/retry,
   forced reset, cancel and SSO without rendering; recovery request/email/MFA/
   password/completion/error continuity and unchanged registered service return.
3. React/BFF and legacy browser callbacks: state mismatch/expiry/replay, failed
   exchange, absent/invalid/duplicate theme, selector changes, account settings
   load/save retry, unchanged-login/no-record behavior with denied optional
   storage, malformed/timed-out handoff, direct/retry/new-tab entry and unrelated
   settings retained.
4. Docs success/cancel/error/retry/switch user, strict query/origin/CSRF checks,
   old pending cookie acceptance, preference JSON fields retained and clean
   return navigation. The docs cookie must never authenticate API actions.
5. Mixed-version rows above, PHP without theme opt-in, scheme/common/bundled
   logo precedence, dormant `core.logo_url` ignored and registration removed,
   WebAuthn registration logo rendering, both site-logo aspect ratios and
   recovery CSP in each scheme.

Add focused tests for semantic behavior, not copies of implementation details.
Source packet and final review must include complete base-to-head series, final
diff, actual dependency inputs, no-migration conclusion, API declaration-neutral
assessment, and screenshots/evidence limitations. Review scope includes auth
security invariants and consistency with existing forms/feedback.

### Remaining provider browser coverage: bounded B fixture brief

Lead accepted this verification refinement on 2026-11-26. Implementer0 owns
preparation within the existing B package; the parent owns the eventual native
driver. This closes unrun provider flows after C default (7 scenarios), C site
(6) and D (6). Reuse their terminal results and existing route/helper/framework,
installed-package and services proofs within their demonstrated scope. There
is no product change, old-provider stack, manual screen-reader campaign or
password-manager automation in this batch.

**Preparation is released; live work remains held.** Implementer0 may write
the disjoint ignored files under `browser-fixture/`:
`b-provider-fixture.rb`, `b-provider-acceptance.mjs`,
`b-private-manifest.json`, `b-recovery-links.json` and `captures-provider/`.
Verify they are Git-ignored and untracked before writing sensitive content;
private JSON files use mode 0600 and private capture directories mode 0700.
Do not edit the running `server.rb`, original `private-manifest.json`,
`branding.json`, C/D scripts or product source. Script preparation and static
syntax checks must not load the API, attach a database, authenticate, create
users, process mail, reload branding or launch a browser/service. The parent
launches the exact prepared driver only after all C/default/site/D work is
terminal and it explicitly opens the exclusive provider window.

**Attach only; no provider refresh.** The earlier proposed restart is withdrawn:
`server.rb` calls `SchemaExport::Bootstrap.load`, which starts a new TestDb,
loads schema and seeds data. Restarting would replace the protected C/D data;
SIGUSR1 reloads branding only. Use the current API/TLS/Chromium and existing
database, without restart, SchemaExport/SpecSeed bootstrap, schema loading,
new attach-existing-server mode, service, route or framework. The API sees new
rows through its existing model interfaces.

Before any live action, the parent verifies the registered provider's current
service ID, PID, argv/source and its owned MariaDB PID/datadir/database name,
loopback endpoint and TLS identity, plus `/v7.0/` readiness. Earlier receipt
`0bcd9c93-34e9-4e55-ac2f-12649061112e`, PID 1566923, backend 5190 and auth TLS
5189 identifies the candidate, not fresh readiness. Parse the exact owned
TestDb `state_dir/env` metadata (`DATABASE_URL`, `STATE_DIR`) privately; never
eval it, print connection secrets or accept arbitrary inherited connection
overrides. Attach failure must not fall back to creating a database. Bind the
helper to this verified instance and record sanitized before/after identity
and readiness evidence, rather than claiming a provider refresh.

Create only two additional low-privilege synthetic users (MFA/recovery and
forced reset) and one separate synthetic OAuth client through existing model
interfaces. Use `User.new` and canonical `User#set_password`; do not invoke
SpecSeed to create these rows. Reuse the existing local callback and a fixed registered
`authorization_start_uri`; do not add a callback route. The original manifest's
two normal users and C/D clients, credentials, settings and existing SSO records
are protected. Record private before/after comparisons and report only whether
they are unchanged. New B authentication/session/recovery records must belong
to B identities. No global reset, deletion/reseed or signing-key rotation is
allowed. Reuse the existing canonical mail-template/test-node prerequisites
only as needed in this isolated fixture; a prerequisite that would alter
protected data stops preparation/execution for owner diagnosis.

Owner0's subsequent full signer inspection corrected the presumed unlock
prerequisite: `TransactionSigner#can_sign?` currently always returns true, while
`#sign_base64` returns nil without an in-memory key. The operation specs unlock
for signature assertions; that setup alone does not establish a native recovery
requirement. Preserve the current optional-signature behavior. Do not install
keys, unlock the helper/Puma or authenticate an admin merely because bootstrap
has no unlock, and do not treat `can_sign?` as proof that a key is loaded.

The lead's conditional operator allowance remains dormant unless an actual
canonical prerequisite requires signing. Only then, in the parent-owned post-D
window, verify the requirement against the exact Puma process and use the
existing synthetic SpecSeed admin through the normal local authenticated
`ApiServer::UnlockTransactionSigningKey` action with the private fixture
passphrase. Unlocking the helper does not unlock Puma. No third user, new key,
rotation, unconditional unlock, production/external API or auth/CSRF bypass is
permitted. Preserve C/D SSO and isolate any operator credential/session from
browser captures and the low-privilege identities. Identity, permission or
prerequisite contradictions stop the batch; they do not authorize another
setup mechanism or an automatic retry.

**Canonical recovery and private mail capture.** Submit the ordinary HTTP
`POST /oauth2/password-reset`; it enqueues `PasswordRecoverySubmission`.
Use one bounded `PasswordRecoveryWorker#process_next` per dedicated submission,
which invokes `Operations::Authentication::RequestPasswordRecovery.run`.
The operation generates the real token, persists its digest/expiry and renders
the link through `Account#reset_url` and `TransactionChains::PasswordRecoveryMail`.
Read only that B request's `MailLog` rendered link into the private links file.
Verify no unrelated pending submission can be claimed before invoking the
worker. Leave `Transactions::Mail::Send` queued and unexecuted: no transaction
dispatcher, SMTP adapter, production mail or new daemon is needed.

Use at most two canonical recovery submissions/captures: one for the completed
flow, then one unused link for expiry. Expire only that second B recovery
record through the existing model interface before following its link. Reusing
the consumed first token proves replay rejection, not expiry. Do not fabricate
tokens, verification results or auth state. Use only the mail/test-node setup
actually required by these operations, preserving the optional-signature
behavior above; do not copy signature-specific assertions' setup or run global
test reset helpers against this shared fixture.

One native script executes these six sequential chains, with isolated B browser
contexts and the existing CDP virtual authenticator:

| Chain | Required observable result |
| --- | --- |
| 1. Credentials and controls | Invalid credentials rerender retains preference, return capability and normal feedback. Keyboard selection, accessible names, visible focus and 44px targets work at desktop/narrow widths. A no-JS context retains native login/forms and CSS fallback. Check autocomplete attributes and filled-control colors; synthetic filling is not real password-manager autofill evidence. |
| 2. TOTP | B MFA user reaches the real challenge; an invalid code displays the normal themed error, and a valid TOTP retry continues with the chosen preference. Method-switch coverage follows enrollment in chain 3. |
| 3. Passkey and registration | Enroll through the existing real registration flow with a CDP virtual authenticator; the light registration page renders declarative/default branding. After enrollment, verify method switching retains theme/continuation fields, then exercise a rejected/cancelled assertion and successful retry without stubbing verification. |
| 4. Forced reset | B reset user reaches the real forced-reset form; invalid confirmation/validation preserves themed feedback, then valid submission resumes authorization normally. |
| 5. Recovery | Request/sent and private email landing lead to an invalid TOTP attempt, then the real recovery passkey rejection/valid retry using chain 3's credential. This exercises recovery's distinct browser appearance/URL handling within the same token. Password error/retry, completion and a second unused expired-link rejection retain expected appearance. Same-origin steps retain preference; a fresh email context uses its own saved/auto mode. Check selected logo/CSP and the unchanged registered service-return URL, with no theme added to it. |
| 6. SSO and opt-out | Reuse only B's authenticated SSO session for GET authorization without the credentials page. Opt-in success returns the selected enum; the old-client-shaped request omits `theme_return` and receives no response theme. Preserve ordinary callback/state checks and avoid exposing code/state values. |

The TOTP-only fixture has no passkey method to switch to before chain 3;
do not fabricate that state. Chain 5 reuses the canonical enrolled credential
and existing authenticator, with no additional mail, recovery submission or
browser stack. Set the dedicated client's existing
`authorization_start_requires_user_action: true` so recovery completion and
the exact registered service-return link can both be observed through the
normal flow. This fixture choice changes no product behavior.

Exercise light/dark/auto across the chains rather than multiplying every flow
by every theme. Reuse C/site logo and preference evidence; do not mutate shared
branding to repeat it. The provider packet reports any needed but unavailable
branding condition before launch. DOM/keyboard evidence is not a claim of a
manual screen-reader run, and the virtual authenticator is not physical-key
coverage.

Disable raw auth traces, HAR, video and unsanitized URL/network/console dumps.
Never print passwords, OTP seeds/codes, credentials, cookies, auth/state/code
values, recovery links/fragments, mail bodies or DB connection metadata.
Captures contain only rendered UI with sensitive fields masked; do not capture
enrollment secrets/QRs or browser address bars. Driver errors must be sanitized
before leaving private output. Durable evidence contains scenario/assertion
names, sanitized results, tested heads/installed inputs, script hashes and
capture paths, without private values.

Plan one 5–10 minute native batch, with a 15-minute deadline, bounded element/
request waits and at most one TOTP-window wait. Fail fast on the first failed
precondition/assertion, unexpected request/destination, mail dispatch attempt or
protected-data change. Keep partial results and the exact stopped step; do not
automatically retry the batch, restart services or reset data. Owner0 diagnoses
failures and proposes only the smallest affected follow-up. Parent uses the
existing native monitoring policy. Preparation completion reports paths/hashes,
static-check results, prerequisite order and remaining unrun coverage to the
lead; no architect tests, service/data mutations or native execution are part
of this amendment.

### Accepted hostname companion for the remaining B chains

The lead accepted this narrowly scoped fixture exception after static origin
preflight. It supersedes the earlier no-new-service/no-auth-origin-change
boundary only as described here. Implementation preparation may proceed;
service, TLS, configuration and browser mutations remain parent-owned and held
until the exact prepared hashes, transition plan and recovery are accepted.
Implementer0 owns the companion and helper/runner successors; implementer2 owns
the existing TLS fixture's candidate and rollback configuration. Neither edits
the other's active files. Preparation has a 15-minute milestone; return an
actual contradiction instead of expanding the fixture.

The original IP origin is unsuitable for native WebAuthn credential creation.
This is a supported-origin constraint, not a proven diagnosis of attempt 1:
the failed callback's message was not retained and zero credentials persisted.
Preserve PASS1/2, existing B setup and the original helper/runner receipts
(`df1da4308a48d654a3a4f6e517283f6879856ac66e00acc298c151bff53c3e9a`
and `8805782fbe1db092e2b3a622047fed27ad9430ef9f3e54d599ea472b50c6a636`).
Run only the remaining four chains with normal fresh B authentication where
needed; do not repeat the passed chains or re-create B identities.

Source basis at vpsAdmin `913806a998d66f80fcc81757d402d1797f127c43`:
`API.default` configures WebAuthn once from `core.auth_url`; the fixture's only
reload signal changes branding. `tools/test_db.rb:364–379` registers an exit
handler that stops and prunes its TestDb. Therefore the original registered
provider must remain alive and untouched, including its database ownership.
No supported in-process WebAuthn reload was found. Do not inject code, alter
signals, restart/stop that provider, or call Bootstrap/schema/SpecSeed.

Use one separately registered B-only Puma companion from the same exact
installed API package and dependency closure. Attach to the freshly guarded
existing TestDb using the prior private connection/ownership checks; the
database owner remains the original provider PID and its direct MariaDB child,
not the companion. Require installed `api/lib/vpsadmin`, then call ordinary
`API.default`; omit the original fixture's client-creation/documentation
configuration block and all data setup. Mount the real app on free loopback
`127.0.0.1:5191`, with its own registration and PID receipt. No new product
route, API behavior, plugin migration or framework is introduced. Preserve
the current branding input and optional-signature behavior.

Before mounting, capture the existing `core.auth_url` row identity and value
privately and change only its value to `https://localhost:5189`, using
`SysConfig.find_by!(category: 'core', name: 'auth_url').update!(value: ...)`.
Do not use the currently broken `SysConfig.set` convenience method or fix it
as part of this task. Keep `core.api_url`, original manifests, all original
users/clients/SSO and branding unchanged. `SysConfig.get` is uncached, so this
temporary setting affects both processes: the exclusive window permits no
C/D or unrelated auth work. It is needed for canonical recovery mail links
(`RequestPasswordRecovery::Account#reset_url`) and OAuth action URLs; changing
only the runner or proxy would leave an inconsistent flow.

The existing certificate has `DNS:localhost` and `IP Address:127.0.0.1` SANs.
Add only a `localhost` SNI/Host vhost on the existing loopback TLS listener
5189, proxying to 5191 with fixed `Host: localhost:5189`, HTTPS forwarding and
the same existing loopback forwarding headers; clear forwarded Host as before.
Keep UI and IP-provider server blocks unchanged and retain their TLS identity.
The new vhost may reuse the exact existing logo aliases; configured IP logo
URLs remain valid under the existing CSP. No new certificate, DNS service or
trust bypass is needed. Confirm localhost resolves to the selected loopback
listener without changing browser security or accepting an unexpected host.

Browser origin, proxy Host, API allowed origin and recovery links must all be
`https://localhost:5189`. Leave the normal RP-ID configuration unset: WebAuthn
3.5.1 creation options use the normal caller hostname and verification derives
the RP ID from the single allowed origin when no explicit ID is set. Thus the
effective RP ID is `localhost`; do not substitute an IP ID, inject credentials,
override browser domain validation or broaden allowed origins. Original B
client callback/service-return URIs stay fixed. Use fresh B browser contexts;
do not copy C/D cookies or count old IP cookies as hostname SSO evidence.

Bounded successors may update only their explicit auth-origin checks, real
recovery-link validation, companion identity and existing-setup continuation.
Retain the original files/receipts and report successor paths/hashes. Keep the
original-provider/database binding in the helper; separately verify companion
registration/PID/package and TLS routing. Before any write, compare protected
records and capture the auth_url baseline. During the override, verify that
the only allowed settings difference is that exact row/value and report it
as active. A passing protected-user comparison is not a claim that settings
are restored. Do not rewrite baselines to hide the override.

Parent transition order: verify identities, current setup and free port;
retain the exact previous TLS configuration and private auth_url restoration
record; set the bounded origin, launch the registered companion, validate its
source/readiness, then apply the syntax-checked TLS candidate through the
existing registration. Check CA/hostname/routing agreement before the single
remaining-four browser batch. Keep the existing 5–10 minute expectation,
15-minute deadline, fail-fast, secret-output restrictions and two-recovery-
submission cap. Sanitized registration outcomes may distinguish browser create
failure from begin/finish rejection without dumping tokens or response bodies.

On success or failure, cease browser/auth requests, restore the exact previous
auth_url value on the same row and restore the prior TLS configuration before
final protected-settings/helper verification. Record original provider/DB
identity, original users/clients/SSO equality, settings restoration and original
IP/UI readiness. If an intervening value, ownership mismatch or uncertain
mutation prevents exact restoration, stop and report that recovery obligation;
do not overwrite unknown changes or claim completion. The companion remains
registered and retained without further auth traffic; session/services/roots
are not stopped or cleaned up by this brief.

Evidence must distinguish retained IP PASS1/2 from the hostname remaining-four
results, include the companion's actual installed source/dependency identity,
script/TLS hashes, real credential persistence, auth/recovery outcomes and
restoration proof. This changes disposable fixture configuration only. Product
heads and earlier reviewed code stay unchanged; no additional native run or
success is claimed by this source-backed design amendment.

### B virtual-credential checkpoint recovery

This is a bounded recovery of the existing real B credential, not another
enrollment or a product change. Attempt 3 completed registration and real
rejected/valid passkey MFA, method switching and OAuth return, then failed its
private checkpoint. Preserve those leaf results and the original mode-0600
credential file. Its counter predates the accepted assertion; do not reuse it
as current or infer a replacement from clicks. Remaining reset/recovery/SSO
execution stays held for the lead's frozen-plan acceptance.

The single authorized isolated CDP add/get probe completed in 1.624 seconds,
without navigation, network, assertions, database access or file writes. It
reproduced only removal of `userName`, `userDisplayName` and `userHandle`.
No fields were added or changed; key bytes, credential ID and RP ID were equal,
counter stayed 1, and `isResidentCredential`, `backupEligibility` and
`backupState` all remained false. The initial saved handle is nonempty. These
facts explain the overstrict whole-object checkpoint comparison; they do not
show an authentication defect or reconstruct the lost post-assertion counter.

Installed Playwright 1.61 `playwright-core/types/protocol.d.ts:19714–19738`
declares CDP `Credential.userHandle` optional. Its comment describes the user
mapping but does not claim a resident-only restriction. Both `addCredential`
and `getCredentials` use that type. The probe establishes omission for this
exact nonresident credential, not a general permission to discard handles.
At vpsAdmin `913806a998d66f80fcc81757d402d1797f127c43`,
`resources/webauthn.rb` Authentication::Begin resolves the user from the valid
MFA token and supplies only that user's enabled credential IDs. Recovery's
`webauthn_begin` does the same for the eligible locked recovery user;
`PasswordRecoveryWebauthn` locks the user/recovery/challenge and calls the same
`WebauthnFactor`. That factor matches the exact user's enabled external ID,
then verifies signature/challenge/origin/RP and the persisted counter under
lock. WebAuthn 3.5.1 permits an absent assertion userHandle. These known-user,
ID-bound paths support the observed omission without changing user authority.
No discoverable/resident or username-less flow is being certified.

The permitted checkpoint correction is specific: for this saved credential
and proven runtime, accept omission of those three fields only while
`isResidentCredential` stays false and the canonical known-user mapping above
remains in use. Preserve the original handle in the original private evidence;
do not fabricate it in an assertion or switch resident mode. A returned handle
must equal the saved bytes; an empty/different value is not the observed omission.
Keep credential ID, private key bytes, RP ID, resident flag, backup flags and
every other exported field unchanged, with only the separately checked counter
allowed to advance. Any other normalization needs owner disposition; do not
ignore all optional or identity fields.

With that concrete condition established, the lead's conditional release
permits one exact authoritative-counter read by owner0 under the existing
original-provider/DB and private credential provenance guards. Use a read-only
transaction and roll it back, matching the actual saved raw credential ID to
its canonical external ID and the exact B user; require exactly one enabled
row. Keep full matching data private. Return only the counter, match booleans
and sanitized guard proof. Require an unsigned 32-bit integer no lower than
the saved baseline. Missing, duplicate, disabled, mismatched or regressed state
stops recovery. No server-row update, key installation, admin authentication,
additional enrollment/deletion or second diagnostic probe is released.

That persisted value is the server's last accepted counter, not reconstructed
authenticator history. Restoring it into the existing virtual key and the next
normal assertion remain held until the continuation packet is accepted. The
packet preserves the original private file, identifies the observed baseline
and approved narrow comparison, and uses the existing checkpoint mechanism;
no new resumer or generic credential framework is needed. The native import
must retain the actual key/ID/RP and demonstrated flags. Its next genuine
assertion must advance beyond the observed baseline and pass the unchanged
server signature/counter check; never lower the database counter or bypass
validation. Save actual subsequent exports privately at existing boundaries.
If provenance becomes stale or an assertion/checkpoint fails, retain partial
evidence and stop rather than resetting state or retrying automatically.

Architect work for this amendment is source inspection and this brief only.
Owner0 retains preparation/diagnosis; the lead retains acceptance and actual
continuation authority. Existing hostname/settings restoration and protected
C/D data obligations remain unchanged.

### B continuation from the actual recovery session

Lead accepted this fixed-session continuation after attempt 5 saved actual flow
and CSRF cookies but failed at the landing/navigation boundary. The precise
driver failure remains unresolved; do not infer it from the stage label. The
saved mode-0600 snapshot has no completion cookie, and no subsequent MFA
assertion is reported. Preserve the real credential and its latest proven
counter; no new enrollment, mail or recovery token is part of this correction.

Source `password_recovery.rb#exchange` sets the flow cookie only after
`consume_email_token!` stores its SHA256 digest/expiry and clears the email-token
digest, then redirects to `/oauth2/password-reset/verify`. `current_recovery`
uses that flow-cookie digest; the later CSRF check compares the actual CSRF
cookie with the form/header value. The CSRF cookie is a double-submit value,
not a separate database-bound token. Normal GET of the existing verify route
with this actual session is supported; replaying the consumed email link is not.

Release one owner0 read-only transaction plus rollback against the exact
existing B recovery ID/user/request/client and SHA256 of the actual saved flow
cookie, under the existing private-file, original DB and retained-companion
provenance guards. Require one match, consumed email token with nil email-token
digest, recoverable outcome, usable session and future session expiry; require
nil MFA verification timestamp/factor IDs, completion and invalidation. Validate
the saved flow/CSRF cookie names, host-only localhost scope, recovery path,
Secure/HttpOnly/SameSite attributes and unmodified absolute expirations against
the actual snapshot. Observe current remaining cookie and database TTL; the
earlier reported 717 seconds is not a current validity guarantee. Return safe
match/state booleans and TTL only, never cookie values/digests or record IDs.
Do not call a controller that could invalidate state during this read.

Any expiry, missing/ambiguous row, provenance mismatch or inconsistent state
stops continuation. Do not refresh expiry, reset consumption/MFA, mint cookies,
resubmit mail or expand the two-submission cap. Positive observation permits
owner0 to prepare only the fixed same-session remaining-two driver, targeted
within three minutes; parent still accepts its frozen plan before importing
cookies or making a request. Import the exact captured snapshot into the
isolated B context without changing values, scopes or expiry, then ordinary
GET `/oauth2/password-reset/verify` with the same bounded client/locale/auto
parameters. Rendered forms provide normal CSRF values; no fabricated form or
auth state, CSRF bypass, first-link replay or transient response-body dependency
is permitted. Recheck expiration immediately before the parent launch.

Continue only the outstanding recovery and SSO acceptance, using the existing
canonical routes, real credential and fail-fast bounds. Retain all earlier
results and the same protected-data/settings restoration obligations. This
does not introduce a generic resumer or product change. Architect work remains
source inspection and documentation; no live query/browser action was performed.

### Prepared three-submission cap and native diagnostic condition

The lead accepted preparation of a bounded total-three-submission successor,
including the ignored helper's exact cap guard. This does not activate that
guard or release requests: actual execution waits for the frozen parent plan.
The saved first recovery session expired at 17:45:36; its consumed email token
cannot supply an unused-link expiry check. A fresh positive recovery and a
separate unused email-link expiry check need two more canonical submissions,
at most three total. Preserve the expired session; no import, reset, reopen or
lifetime extension is permitted.

The isolated full-DOM probe passed in 1.109 seconds with the canonical selector,
actual selection and appearance check. This establishes that those interfaces
work in the isolated document; it does not identify the earlier native error,
whose exact subtype remains unavailable. The next live check is one controlled
native MFA theme diagnostic with stable-frame readiness, separate click and DOM
stages, safe error classification and counts. Keep the original assertions;
do not force clicks or add a permissive fallback. Only if this checkpoint
passes may the same prepared browser continue the outstanding positive recovery
and SSO. On failure, stop with a precise sanitized artifact and do not spend
the third submission. Do not describe this as a proven fixture-root-cause fix
or run an unconditional two-flow batch.

At source `913806a998d66f80fcc81757d402d1797f127c43`,
`PasswordRecoverySubmission.enqueue!` trims/truncates identifiers to 127
characters and hashes their lowercase form. It permits at most one submission
per identifier per ten minutes and ten per source IP per ten minutes, with a
100-pending queue limit. Finished submissions still count toward cooldowns.
`request_submit` exposes 429 with Retry-After or 503 rather than bypassing them.
The canonical operation resolves exact login first, otherwise accounts with
that email; its inspected policy checks lifecycle/login eligibility and effective
MFA, without an additional account-wide recovery-request cooldown. These are
source rules, not a current database-rate/readiness claim.

Supported conditional order: use the existing B MFA user's actual unique email
for submission 2 and the native diagnostic, continue its real MFA/password/error/
service-return flow only on diagnostic success, then use that same user's
original login for submission 3 only after positive completion. The reported
first login submission at 17:08 predates the reported expired session by over
ten minutes; email and login have distinct canonical identifier digests.
Thus this order needs no artificial delay between submissions 2 and 3 if
there were no other recent submissions under those identifiers/source. Confirm
the existing private identity mapping and rate evidence in the parent packet;
an email matching another account or login is a blocker. Do not invent an alias,
change identifier case/source IP, delete rate records or reset timestamps.

Prepare the fixed driver fully before consuming submission 2's email link so
its real fifteen-minute session is spent on the bounded acceptance. Use normal
HTTP forms/CSRF and exactly one canonical worker turn per accepted submission,
capturing only the matching B MailLog link privately. Only after positive
completion create submission 3; leave its email token unused, expire only that
dedicated recovery's email expiry through the already-scoped model operation,
and test canonical rejection. An already-consumed token or expired session is
not equivalent evidence. Stop on another positive-flow failure without spending
the third request. No fourth request, automatic enqueue retry or worker retry
is part of the plan.

Real HTTP cooldown/queue responses take precedence over elapsed-time inference.
If waiting is required, record Retry-After and keep the parent wait interruptible
outside an active recovery session; if it exceeds the accepted window, return
the exact blocker. Do not hold a freshly consumed session while diagnosing setup.
For SSO, use normal B authentication with its actual post-recovery password and
reuse only the resulting B session; do not assume pre-reset authority survives.
Keep the same two B users, one client, existing real key and canonical counter
checks. All mail remains queued, with no SMTP/dispatcher, fabricated token,
counter/session reset, product change or protected C/D mutation. Original
provider/DB retention and exact hostname/settings restoration stay mandatory.

Architect inspected only the rate/operation/policy source and wrote/amended this
brief; the isolated DOM result is the owner's evidence. No architect DOM probe,
live rate query, auth/request, cap-guard edit or submission was performed.
Owner0 may prepare the ignored total-three successor now; live cap activation,
requests and browser execution remain held for parent acceptance.

## Documentation and remaining decisions

The provider's theme extension and preference/return semantics have one durable
home in HaveAPI; vpsAdmin and React reference it. vpsAdmin owns logo precedence,
appearance and recovery behavior; site config docs own assets/rollout/rollback.
React updates existing REQ-005, relevant workflow/configuration explanation and
a dated work-log entry. HaveAPI user docs explain local theme persistence.
The lead applies user-facing writing guidance before commits. Inspect the KB
contract's affected login/recovery captures and bilingual pages during
implementation; unchanged PHP does not establish that auth screenshots are
unaffected. Any production KB writes need exact staged-change approval.

No blocking product decision remains for implementation. Accepted defaults
are auto, successful-login theme wins, errors retain initiating preference,
browser-local OAuth/docs preferences and existing React account persistence.
Branding uses only declarative scheme/common values or the bundled wordmark.
Cookie names, helper names, SVG wordmark details and the pinned Rack response
adapter's smallest implementation are bounded implementation choices; they must
satisfy the settled contract and checks rather than adding a broader subsystem.
