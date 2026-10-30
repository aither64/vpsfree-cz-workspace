# HaveAPI HTML documentation redesign

Status: accepted implementation brief for the documentation UI and examples.
The latest user-feedback milestone is recorded at the end. Milestone 5 explicitly
resumes bounded OAuth fixes/account design and official partner coordination;
it supersedes the earlier hold only within that scope. Partner-owned HTTPS
deployment is separate from this session's HTTP preview. Architect0
owns this brief. The lead accepts material revisions and assigns application
edits. The original screenshot remains outside Git.

## Scope and result

HaveAPI owns the reusable documentation renderer, navigation, preferences and
examples. Render an overview and individual resource pages from the real,
current user's description. Provide a synchronized resource/action sidebar,
light/dark/automatic themes, and independent language, client variant and
simple/thorough example controls. The default examples show the operation
clearly; thorough examples add useful error handling. vpsAdmin supplies its
actual declaration and configured SDK profiles for preview.

Do not change API action routes, OPTIONS descriptions, SDK request behavior,
schemas, migrations or authorization rules. Do not publish a release or change
production configuration as part of this implementation assignment.

## Stable example contract (packages can start)

`HaveAPI::ClientExample::Context` gains `detail`, an immutable reader included
in `FIELDS`, construction and `with`. Values are exactly `:simple` and
`:thorough`; the default is `:simple`. Reject other values. Context derivation
continues to share unchanged owned fields and copies only supplied subtrees.
Neither detail renders nor user requests may mutate shared descriptions or
generator adapters. Do not derive detail from an unvalidated query parameter.

Renderers read `context.detail`. Keep the existing positional constructors,
`init`, `auth(method, description)`, `example(sample)` and request/response
methods, result shape and stable client IDs. The base renderer exposes a small
`thorough?` helper; a legacy positional renderer without `with_context` uses
simple behavior. Generated adapters continue their existing
`render(kind:, context:, mode:, ...)` signature and explicitly consume the new
context reader; update small Struct test contexts to include detail rather than
adding speculative capability fallbacks. A third-party older adapter can ignore
the additive reader and render identical output for both levels.

Renderer classes own presentation metadata, avoiding a parallel UI registry:
add class DSL readers `language` (stable lower-case group ID), `language_label`
and `variant` (short display label or nil). These describe presentation, while
existing `id` identifies the exact client and `code` remains the syntax lexer.
Allow unspecified metadata on third-party classes to default to their own
stable ID/label and no variant. Existing built-ins retain their IDs:

| Group | Label | Variants |
| --- | --- | --- |
| ruby | Ruby | none |
| javascript | JavaScript | Async, Callback |
| typescript | TypeScript | Async, Callback, Generated |
| python | Python | Sync, Async |
| go | Go | none |
| rust | Rust | Async, Blocking |
| php | PHP | none |
| cli | CLI | none |
| curl | curl | none |
| http | HTTP | none |

Each built-in class declares its own group and variant. Metadata owner is
implementer1, including the small Go/Rust/generated-TypeScript wrapper classes
under `servers/ruby/lib/haveapi/client_examples/`; implementer2 owns generator
adapter files under `clients/`. Preserve existing registry order and use the
first available variant as fallback unless the saved exact variant is available.
Unavailable profiles never appear merely because their group exists.

For simple action examples, assume the documented initialization/authentication
has established `api`; show the actual call and the relevant result, without
repeated environment loaders, whole-program scaffolding, generic catches,
success banners or unrelated metadata dumps. Provide initialization and auth
examples separately on the overview/authentication pages and link them from
resource examples. Keep exact method names, parents/path arguments, types,
sample values, nullable values and blocking-operation semantics. Go still checks
the returned error; Rust may use `?` with a short enclosing-context note when
needed. No swallowing failures or invented APIs to shorten snippets.

Thorough examples may show complete setup and real error handling, request
metadata and operation waiting when relevant. Share sample translation and
validation between detail levels; never implement simplicity by deleting lines
from generated source. Unsupported samples show the same honest limitation.
Ruby/PHP/CLI/curl/HTTP may keep identical detail output where there is no useful
extra handling; do not add artificial noise to distinguish the modes.

Python has no `if __name__ == "__main__"` guard in either detail. Sync code is
top-level. Async setup uses only the needed `async def main()` and
`asyncio.run(main())`; simple action fragments can use `await` with a clear
async-context note. Imports are only those used by that example. Thorough sync
uses top-level try/except, not an unnecessary `main` function.

## Routes and server rendering

Use the existing version HTML endpoint as the canonical page URL. Examples:
`/v7.0/` (overview), `/v7.0/?page=authentication`,
`/v7.0/?resource=vps` and `/v7.0/?resource=vps.snapshot` (nested resource).
The API mount prefix must work as well, e.g. `/api/v7.0/?resource=vps`.
Keep the existing unselected root versions/index page. A root URL with page or
resource selection renders the default version and uses canonical version links.
Query page selection applies only to HTML
GET handling, never OPTIONS or action endpoints. Reject malformed/ambiguous
selection and return 404 for a resource absent from the current description.

Resource resolution traverses validated description keys, not constants/files.
Every resource, including a nested one, gets its own page. Render only its own
actions and link its children; do not recursively render descendants' examples.
Overview contains concise getting-started/init content and a resource index;
authentication gets its own page. Authentication-provider resources remain inline
on that page, with their existing anchors; do not introduce a new selector
namespace for them. Shared protocol/client docs remain available.

Construct navigation and content from the same current-user-filtered `@help`.
The private complete schema used by SDK name resolution must never supply UI
navigation, hidden parameter values or a missing resource's page. Preserve
current authorized and anonymous description semantics and escaping boundaries.
Keep `Cache-Control: private, no-store` on HTML that can contain a user's view.

Retain existing resource/action IDs (`root-vps`, `root-vps-show`, including nested
paths) and existing example IDs on the resource page. Resource-typed parameter
links become page-qualified URLs. The overview supplies an escaped anchor-to-page
map derived solely from visible resources/actions so old `/v7.0/#root-...` links
redirect to the matching resource page. Resolve exact resource/action IDs and
example prefixes from known entries, longest match first; do not guess by splitting
hyphens. Preserve the fragment and browser history semantics, avoiding loops.
Unknown fragments remain harmless. No-JS legacy overview should give a useful
resource index; new page-qualified links work without JavaScript. Authentication
and authentication-resource fragments map to the authentication page.

## Stable DOM and browser contract

Implementer0 owns ERB/route helpers and emits the following structure.
Implementer3 owns behavior/styles and must coordinate changes to this contract.
Use ordinary server-rendered links; no SPA, client schema renderer or extra API.

- Root documentation element: `[data-docs]`, with `data-page` equal to
  `overview`, `authentication` or `resource`, and `data-resource` the full
  dot-separated resource key when selected.
- Resource directory navigation: `[data-resource-nav]` on the dedicated
  `?page=resources` page (see the visual-feedback amendment below); links use
  `data-resource-link="vps.snapshot"`, ordinary `href`, and current-page
  `aria-current="page"` where applicable. A labelled `[data-resource-filter]` input filters the
  already-authorized resource list. Keep parent context for nested matches.
- Action navigation: `[data-action-nav]`, with same-page fragment links. Action
  containers have `data-doc-section` and their stable `id`. Scroll observation
  updates `aria-current="location"` on the active action. Do not append every
  action of every resource to the global sidebar.
- Theme controls: compact `[data-theme-choice="auto|light|dark"]` buttons in
  the sidebar, replacing the initial `[data-theme-select]` dropdown as specified
  by the visual-feedback amendment below.
- OAuth login links: `[data-documentation-login]`. Browser code may add the
  current fragment (at most 256 characters) as the structured `fragment` query
  field on the server-generated login link. Encode it once using URL query APIs;
  the server independently validates it. Never submit an arbitrary return URL.
- Synchronized preference controls: `[data-language-select]`,
  `[data-variant-select]` (option values are stable exact client IDs),
  `[data-detail-select]` (values `simple`, `thorough`). Render these in the
  sidebar/global toolbar; optional compact copies next to examples use the same
  selectors. Hide or disable variant selection for a single-variant language.
- Example container: `[data-example]` with a stable ID. Each rendered variant
  and detail panel has `data-example-panel`, `data-client`, `data-language`,
  `data-variant` and `data-detail`. Client/group labels come from class metadata.
  Use unique panel IDs; preserve old client panel IDs for simple panels and add
  a `-thorough` suffix for the other level. Keep source escaped as text.
- An escaped JSON data element `[data-documentation-clients]` contains the
  available `{id, language, language_label, variant}` records, with no code or
  private model content. `[data-legacy-anchors]` carries the authorized legacy
  anchor-to-page mapping. Serialize safely for HTML script text (`<` escaped).
- Use semantic header/nav/main, visible focus, labelled form controls, accessible
  expanded state for the mobile navigation and a skip-to-content link.

Preference state is one versioned localStorage record (`haveapi.docs.preferences.v1`)
containing theme, language, selected client per language and detail. Persist only
these non-secret choices, never tokens or document bodies. Storage failures
must leave working in-memory preferences. Default theme auto and detail simple;
the existing first available client is the initial language. Validate restored
values against the current available metadata; retain preference for a client
temporarily absent from another API while showing an explicit available fallback.

Any language, variant or detail change updates all examples and mirrored controls
on the current page. Before updating, capture the nearest visible stable example
or action section and its viewport offset; after layout settles, compensate
scroll by that element's new offset. Prefer the example containing the initiating
control. Preserve focus, URL fragment and sidebar scroll. Do not restore only
absolute scrollY, jump to the page top, or create browser history entries for
preferences. Navigation uses normal browser back/forward and fragment behavior.

Without JS, readable simple content and links remain; variants/thorough content
can be disclosed using native details as needed. Theme auto follows OS changes;
apply saved theme early to avoid a light flash. Local CSS assets style readable
tables/code in both themes. Wide code/table content scrolls within its container,
not the whole viewport. At narrow widths navigation collapses behind an accessible
toggle and global example preferences remain reachable.

Avoid highlighting every hidden panel on load. Highlight visible/newly selected
source only, with escaped text intact if the worker fails. Remove old per-example
inline nojsTabs initialization from redesigned pages. Keep existing shared-doc
pages working when modifying main layout or old main.js behavior.

## Implementation boundaries and acceptance

| Owner | Complete package and file boundary | Dependencies and checks |
| --- | --- | --- |
| implementer0 | HTML routing/helpers in `server.rb` or a focused new helper; `views/main_layout.erb`, `doc_layout.erb`, version templates/sidebar/partials; server HTML/resource/deep-link tests; existing `benchmarks/spec/client_examples_spec.rb` page/detail extraction | Metadata/detail from 1; emits DOM above for 3. Check overview excludes resource bodies, selected nested resource, missing/forbidden resource, mounted API, old anchors, auth-filtered navigation, resource links and shared docs. Preserve all 15 clients, both detail levels, isolation and existing performance budgets. |
| implementer1 | `documentation_context.rb`, `client_example.rb`, dynamic example renderers and server wrapper metadata; dynamic/context specs and relevant Python emitted checks | No template/asset ownership. Check both details, no Python guard, exact request values, same limitations, immutable derivation, metadata/stable IDs and legacy positional use. |
| implementer2 | `clients/{go,rust,typescript}/lib/haveapi/*/documentation.rb` and their documentation specs/harnesses | Explicit context.detail above; no server wrapper edits. Check simple/thorough generated API calls and representative source compilation/wire behavior; keep generator names/resolution unchanged. |
| implementer3 | New local docs CSS/JS, focused browser harness/specs, highlighter integration | No template edits without 0's agreement. Check persisted/synchronized language/variant/detail, scroll stability, active action, back/forward/deep links, themes, mobile/keyboard and failed storage/worker fallback. |
| implementer4 | Session-owned real vpsAdmin preview launcher/bundle/receipts; bounded vpsAdmin integration only after lead assignment | Consume this session's actual HaveAPI/generator sources and real all-plugin fixture bootstrap. Prove origin/source heads, all available profiles, endpoint health and auth isolation. |

Lead serializes overlapping Git operations and owns final user-visible wording
acceptance before implementation commits. Implementers may complete code/checks
while that pass is pending. Architect owns design amendments, not application
edits. Any change to URL scheme, Context contract, metadata ownership or OAuth
boundary returns through the lead.

## Preview and OAuth status

The chosen early preview is a session-owned Rack process on existing development
port 4567, using isolated disposable MariaDB and the real vpsAdmin all-plugin
bootstrap. It is not an existing shared cluster. Candidate source paths must be
verified from loaded gems; merely mounting a checkout does not select it.
Review origin is `http://172.16.106.40:4567/v7.0/`, subject to actual health proof
in `preview-infrastructure.md`. Queries above require no new route namespace.

Profiles use supported `documentation_clients('7.0', ...)` before mount with
matching local generator gems. The session-only pre-mount wrapper proposed by
implementer4 is sufficient; no permanent schema-export refactor is needed.
Use actual SDK package identity, including Go's `/client` import path, and do not
claim a released package matches unverified current source. Preserve actual API
prose/examples by rendering the mounted API, not sanitized export schema.json.

HTTP preview must not accept credentials, login or mutations. A verified HTTPS
origin is required before OAuth review. Never repurpose occupied default cluster
IPs/domains or another session's runtime.

OAuth is a separate accepted milestone after the full-profile visual preview.
Existing HaveAPI supports authorization code and
PKCE, but token and revoke endpoints require a client secret. A pure browser
client would expose that secret or require an unrelated public-client protocol
change. The selected solution is an optional server-side
confidential documentation client, using existing provider endpoints and
current-user filtering. No provider/public-client semantics change is accepted.
Its exact contract follows. UI packages leave an authentication-control partial
seam and preserve existing Basic fallback for unconfigured consumers.

## Optional OAuth milestone

This is a confidential documentation client of the existing OAuth provider,
not a new provider or browser SDK. It adds no refresh flow, public-client
semantics, token-storage database, API executor or production configuration.
The lead accepted this direction and session-local TLS review on 2026-10-28;
implementation starts only after the lead assigns its package.

### Ownership and configuration

Implementer4 owns a focused new
`servers/ruby/lib/haveapi/documentation_oauth.rb`, corresponding documentation
OAuth specs, a metadata-only `Authentication::Chain#provider_descriptions(version)`
reader and focused spec, and its session-local HTTPS/client setup. Implementer0 owns the
small integration into `server.rb` and the authentication-control partial;
agree the short handover before either touches those files. Implementer0 owns
`doc/documentation-ui.md`; implementer4 owns `doc/documentation-oauth.md` for
durable OAuth setup/security semantics. Link the OAuth guide from the UI guide
and existing client-example guide, coordinating link edits with their owners
and the lead's wording pass. Do not create a third HTML-documentation guide or
duplicate the UI design in the OAuth guide. No permanent vpsAdmin
changes are needed for the preview; use its existing pre-mount configuration
seam or the already-working session-only wrapper.

Proposed public API, before mount:

```ruby
api.documentation_oauth(
  client_id: ..., client_secret: ...,
  redirect_uri: 'https://docs.example.test/api/_documentation/oauth/callback',
  session_secret: ..., scope: ['all'], session_lifetime: 3600
)
```

`scope` defaults to an empty array; `session_lifetime` defaults to 3600 seconds
and must be positive and at most 86400. `session_secret` is at least 64 bytes of
cryptographically random secret material supplied by the application/operator,
never generated on each worker startup. Require scalar nonempty client ID/secret,
bounded scalar scope values and a strong length-validated session secret. Reject
unknown configuration keys. Never put secrets in exception strings or inspect
output. Repeated configuration or configuration after mount is an error.

The exact callback path is `<API mount>_documentation/oauth/callback`; fixed
`redirect_uri` must be absolute HTTPS with that path, no userinfo, query or
fragment. Its origin is the documentation origin. At mount, obtain the default
version's OAuth authorize/token/revoke URLs from the configured auth chain's
provider description, without rendering a whole resource description. Validate
absolute HTTPS endpoints without userinfo/fragments and preserve their explicit
configured origin (which may differ from the documentation origin). Fail startup
if OAuth is absent or required metadata is malformed. No dynamic discovery,
redirect following, request-Host endpoint construction or client-supplied issuer.
The additive chain reader returns provider-name-to-description metadata for only
the requested version, without authentication-resource traversal. Call it after
providers/routes are initialized. Do not expose provider/config objects or mutate
provider-owned data; the docs module validates and copies only the fields it uses.
Existing `Chain#describe(context)` behavior stays unchanged.

The default version selects the authorization issuer. A documentation request at
another API version still validates the resulting bearer token through that
version's ordinary auth chain; it must never inherit identity just because a
different version accepted the token. Single-version vpsAdmin has no ambiguity.

Mount GET `<root>_documentation/oauth/login`, GET callback and POST
`<root>_documentation/oauth/logout`. When configured, the auth-control partial
uses these routes. Existing `_login`, `_logout` and authentication providers
remain compatible for consumers without this configuration. Expose
`DocumentationOAuth::Helpers#documentation_authenticated?(version)` in the HTML
handler. It wraps ordinary `authenticated?` only for documentation GET at the
configured origin, supplies a cookie bearer only without explicit credentials,
and restores the original request environment in `ensure`. Presence of explicit
Authorization, provider custom credential headers or credential query fields
keeps ordinary behavior, including errors for invalid/conflicting credentials.
It must not add cookie interpretation to the global auth chain. The public
control hash contains login/logout UI state and CSRF data, never a bearer token.

### Authorization and browser session

Login generates independent cryptographically random state, S256 PKCE verifier
and a short-lived encrypted pending cookie (10 minutes). It redirects to the
fixed provider authorize URL with the configured client ID, exact callback,
scope, state and S256 challenge. The pending cookie stores state/verifier and
the intended documentation location; nothing secret goes into the URL except
the ordinary one-use authorization code returned by the provider.

Represent the return location as validated documentation fields (version, page,
resource, optional fragment), then rebuild its URL from the fixed documentation
origin and known route helper. Do not accept an arbitrary return URL. Preserve
valid resource/action/example links through login. Reject non-scalar, oversized
or malformed callback inputs; cancellation, missing/mismatched/expired state,
missing code, and PKCE failures leave the user unauthenticated and show a concise
retryable error. Use constant-time state comparison. Consume/clear the pending
cookie before processing success or failure; successful provider codes are also
single-use. Do not expose provider response bodies or exception details to users.

Exchange the code server-side using the existing OAuth token endpoint with
client credentials and PKCE verifier. Use an established HTTP/OAuth library or
Ruby Net::HTTP, bounded open/read timeouts, verified HTTPS, bounded response size
and no redirects. Treat non-success/malformed responses as authentication failure.
The server must support a concurrent token/revoke request when its own public
URL serves the issuer (WEBrick is threaded; single-request production servers
need suitable workers). Never bypass certificate verification. Unit tests stub
the transport rather than contacting production.

Keep only access token, absolute expiry and CSRF nonce in an authenticated,
encrypted cookie, not localStorage or JavaScript-visible state. Use existing
ActiveSupport MessageEncryptor with AES-256-GCM and a JSON serializer, deriving
its key from `session_secret` with a fixed documentation-specific salt. Separate
purposes for pending state and authenticated sessions bind the configured client
ID/callback and mounted API. Do not implement custom cryptography or use Marshal.
All workers use the same secret; rotating it logs documentation sessions out.

Both cookies use Secure, HttpOnly, SameSite=Lax, an explicit mount-scoped path,
no Domain and a mount-specific name. They are ignored unless the request is on
the configured HTTPS documentation origin. Ensure complete serialized cookies
fit a conservative 3800-byte ceiling before setting them; reject oversized token
responses with a generic sign-in error rather than issuing a truncated cookie.
Cookie expiry is the earlier of the provider's positive finite `expires_in` and
configured session lifetime. Validate decrypted shape/purpose/expiry on every
read, and clear malformed or expired cookies without a server error.

Do not store or refresh a refresh token. Register the dedicated vpsAdmin docs
client with `access_token_lifetime: fixed`, `issue_refresh_token: false`, a
bounded access lifetime and the exact callback URI. It must not replace the
existing default OAuth client. Existing optional SSO may be used by the provider.
The provider handles passwords, MFA, account recovery and SSO unchanged.
For the vpsAdmin documentation profile, `scope: ['all']` is needed to describe
all actions authorized for that user's role; this is a real API-capable bearer
token held encrypted by the documentation client. Cookie isolation below is
therefore essential, and no token may enter examples or HTML source.

### Identity, logout and failures

Only the existing HTML documentation GET route may consume the session cookie
to supply an OAuth bearer credential. Shared read-only documentation pages may
display neutral login controls but need not use identity. API actions, OPTIONS,
unrelated routes and mutations must ignore this cookie completely. Do not turn
it into general API cookie authentication. Explicit request credentials retain
their existing semantics; do not combine a cookie bearer with an explicit
Authorization/custom-token/query credential. Query bearer tokens are not a new
login mechanism. Never accept a token in documentation redirect URLs.

Each personalized page invokes the ordinary provider authentication and
post-authenticated hooks; recheck token validity, account restrictions and roles.
Then describe/filter/navigation/render with that current user. Do not trust a
user ID cached in the cookie or bypass current authorization. An expired/revoked
session clears the cookie and displays the public page with a sign-in-again
message; a currently selected now-invisible resource is 404, not an exposure.
No personalized HTML or bearer data is put in shared caches. Use private,
no-store responses and `Referrer-Policy: no-referrer` on docs/auth routes.
Callback responses promptly redirect to a clean documentation URL without code
or state. Raw query strings, tokens and credentials must not appear in preview
access logs or retained diagnostics.

Logout is POST with a session-bound CSRF token and same-origin validation.
Missing/incorrect CSRF or foreign origin fails before revocation. On valid
logout, attempt server-side revocation using the configured client credentials
and access token; clear local auth/pending cookies regardless of the network
outcome. On success show signed-out public documentation. On revoke failure,
show that local sign-out succeeded but the server session may remain until
expiry, with a sign-in link; never claim successful server revocation. This
bounded first version does not retain tokens in a retry queue or background job.
Do not request `close_sso` or claim to sign out the entire API/SSO account;
vpsAdmin's existing user logout policy may close this client's other sessions.

### TLS preview and acceptance

Keep HTTP visual review at the existing link while building/testing this module.
After module review/readiness and an announced cutover, implementer4 may change
only the owned listener to `https://172.16.106.40:4567`. Use a session-local CA and
leaf with the exact IP SAN; private keys and secrets stay untracked and private.
Supply only the public CA file, its SHA-256 fingerprint and explicit browser
trust instructions to the user. The user must choose to trust it before login;
do not silently modify trust stores. Verify backend requests with that same CA
through the standard trust mechanism. No `verify: false`, curl `-k`, shared
certificate borrowing, firewall/DNS mutation or physical host deployment.

Configure fixture API/auth origins and the dedicated OAuth client to that exact
HTTPS origin. Allow only the needed OAuth paths and documentation routes through
the session preview guard; keep ordinary API action execution blocked. HTTP must
never receive credentials and must not continue serving an authenticated mode.
User interaction uses isolated fixture accounts, never production passwords.
Record exact loaded source heads, client settings without secrets, public cert
fingerprint, listener identity and successful callback/revocation evidence.

Quick tests cover configuration/cookie bounds, valid code+PKCE, callback state
failure/replay/cancel, tampered/expired cookie, malformed/oversized token response,
logout CSRF and revoke failure, configured mount prefixes, role changes, and
cookie exclusion from OPTIONS and mutating action routes. Verify no secrets in
HTML/errors/URLs. A generic API without OAuth configuration retains its old
behavior. Following committed implementation and independent review, exercise the
real fixture HTTPS authorize/callback, filtered resource navigation, re-login
after expiry and logout. No production endpoint or credentials enter these tests.

Rollback removes optional config and serves prior documentation code; no database
schema rollback is needed. Existing docs OAuth client can be disabled/revoked by
normal administration, but do not delete it automatically. Restoring old code
with unsupported new configuration requires removing that opt-in configuration
first. Browser cookies expire or are ignored; old software can read all API data.

## Compatibility, deployment and recovery

No persisted API data or database migration changes. Old and new workers can
serve different HTML without changing client requests, protocol descriptions,
CLI/Terraform behavior or node coordination. New browser preferences are
namespaced and ignored by the old UI; rollback can load all existing API state.
Keep stable fragments and externally reachable documentation routes as described.
Additive Context metadata does not change legacy positional renderer signatures.
Paired new server/generator source is needed to review the new detail behavior;
older adapters can continue returning their existing code.

Preview refresh is an owned development-process restart with unchanged fixture
isolation; record actual loaded heads and the retained previous launcher/source
for recovery. Production adoption and release packaging are separate lead-owned
steps. No physical deployment, merge or session lifecycle action is authorized
by this brief. Future OAuth rollout must remain optional and rollback-compatible.

## Bounded verification plan

Quick checks: syntax/lint in repository Nix shells, focused context/renderer/HTML
specs, DOM/assets checks and a minimal real-preview smoke of overview, one large
resource, one nested resource and authentication. Run `make doc` before server
packaging tests. Preserve existing current-user/host escaping regressions.

After committed implementation and mandatory independent review, run the affected
documentation integration/compilation contracts (`make test-documentation`,
Python encoder checks and generated-adapter checks as applicable), with a fresh
watcher for long/uncertain runs. Existing performance contracts remain required;
do not change budgets to accommodate the redesign. Prove deterministic scope:
overview renders no resource action examples, a resource page renders only that
resource, and hidden/absent profiles are not rendered. Compare baseline and
candidate representative real vpsAdmin response size/time diagnostically; avoid
a new benchmark project or arbitrary wall-clock unit limits.

Browser acceptance: desktop/mobile, all three themes, at least Python sync/async,
Rust and generated TypeScript; both details; mid-resource global changes preserve
the visible example/section; action navigation follows scroll; back/forward and
old/new deep links work; page reload retains preferences; filtered users cannot
learn hidden resources/fields through navigation or panels. OAuth acceptance is
specified in its later amendment, not implied by the visual HTTP preview.

## Performance harness adaptation

Architect investigation on 2026-10-28 read `doc/performance.md` in full and
inspected `DocumentationScenario`, the worker measurement/validation loop,
comparator/replay and optional documentation runner. Implementer0 owns this
bounded follow-up after its UI commit; the lead accepted the scope. This changes
response-shape validation and candidate resource coverage, not benchmark policy.

### Preserve the calibrated request

`DocumentationScenario#call` sends exactly one GET to
`http://example.test/benchmark/api/v1/` for each `docs.html_resources`,
`docs.html_actions` and `docs.html_rust` operation. Dimensions change the fixture,
not that request. Keep this request, inventory IDs/dimensions, operation counts,
authorization/query/execution expectations, pilot/count/warmup rules, runtime,
dependency graph, immutable reference, timeouts and all budget bytes unchanged.
Do not replace an operation with a concatenated overview/auth/resource request
suite or normalize its result as equivalent to one historical request.

The old endpoint renders the entire resource body; the new endpoint intentionally
renders the overview. The policy explicitly permits different response bodies
between verified revisions while enforcing each revision's own response
stability, counters and limits. Thus the paired result remains a valid comparison
of the same endpoint request. It no longer represents equal all-resource example
rendering work. State this limit in the owning performance guide and keep byte
deltas visible. Do not claim a smaller overview proves resource rendering faster.

Leave historical `DocumentationPerformanceFixture` unchanged. The same entire
authorized description is still computed, so existing expected authorization
counts remain valid. OPTIONS and direct Rust adapter lanes keep their existing
requests and validation. New detail defaults can change direct adapter source
output; that remains governed by per-revision stability and unchanged budgets.

### Validate two explicit HTML shapes

Adapt `DocumentationScenario#validate_body!` to recognize the documented
`data-docs` page envelope and validate one of two explicit shapes. Presence of
the new envelope selects the strict new overview contract; absence selects the
existing strict monolithic contract. Never rescue a failed new validator by
trying the old one, and never accept an empty page just because it has a marker.
Reject duplicate/malformed new roots, wrong page kinds and mixed overview/action
content. No source-version exception or permissive third shape is needed.

Keep old monolithic sample, initialization, privilege, Rust panel and full
example-inventory checks intact. For the new overview require:

- A usable link to the dedicated resource directory under the mounted API
  prefix, plus the exact expected resource targets in the legacy-anchor map.
  The full visible resource tree now belongs to the separately tested directory.
- Actual initialization panels (including Python sync and both simple/thorough
  levels). Rust workloads require both Rust variants and configured package
  identity; do not mistake a selector label for a rendered code panel.
- A parseable legacy-anchor map containing the expected resource/action targets
  from fixture dimensions. The `resource0/admin_only` action and its example
  prefix are present only for admin. Reject missing/wrong/foreign targets.
- No action-example containers, action sample values, privileged parameter names,
  defaults or response/request values in the overview, for either role. Privileged
  action IDs in the admin's authorized legacy-link map are permitted; distinguish
  those navigation keys from rendered action bodies and parameter/sample data.

The admin/member body-proof substitution regression now uses that exact
role-filtered anchor-map inventory, not `ADMIN_ONLY_REQUEST`, which is absent
from both valid overviews. Retain every-operation counter/status/content-type
checks and per-sample raw-body proof boundaries. Body validation remains outside
the timed loop; do not add setup HTTP requests to choose a representation or
renderer calls inside validation that distort warmed state.

Where page metadata is retained, identify monolithic versus overview explicitly.
An overview has zero rendered action examples; do not label its link inventory
as rendered examples. Raw bytes/digests, canonical identity, source/input hashes,
sample occurrence counts, comparator policy and replay format stay intact.
Keep the existing exact framework-footer normalization; no broader HTML
normalization or response-equality waiver is needed. Existing synthetic replay
fixtures still test their original raw-body integrity and instability behavior.

The optional `benchmarks/documentation.rb` keeps its existing root `html` lane
and request shape. Adapt `html_output` to validate the real overview or legacy
monolith rather than requiring sample and initialization on the same page. It
is a diagnostic runner, not a new resource timing gate. No new CLI, route-suite
aggregator, benchmark service or shared validation framework is needed.

### Candidate resource-rendering and allocation coverage

Keep the all-client matrix exactly equal to the 15 registered clients and both
details. Its complete-page correctness helper separately requests overview,
resource directory, authentication and every resource and compares each actual panel with renderer
output, including limitations/failures and admin/member/admin isolation. New
resource pages must contain only their selected resource's action examples.
Keep direct per-render 128-unrelated-subtree checks and their +32 object/call
allowance unchanged.

Use two bounded allocation-growth dimensions at the existing 2.5 increment
ratio, using the existing three batches/measurement helper:

1. Unrelated-resource growth: 2, 4 and 8 resources with fixed selected action
   count. Measure a fixed request set (overview, resource directory,
   authentication, resource0) or
   each page kind separately. Never measure all N resource pages together under
   a linear bound: N separate pages each contain N-resource navigation, which
   creates inherent quadratic aggregate work. Record bytes for the measured
   request set, separately from optional complete-documentation correctness data.
2. Within-resource panel growth: one resource with 2, 4 and 8 ordinary actions,
   constant parameters/samples, all profiles and both details, measuring only
   `?resource=resource0`. Verify exact panel counts and increasing output before
   accepting allocation growth. This preserves detection of whole-resource or
   whole-description copying per rendered example, which the first dimension
   alone cannot detect when selected panel count is constant.

Extend only `AllClientPerformanceFixture` with a default-compatible ordinary
action count. Keep its existing Public/Protected defaults, scalar examples,
failed/admin samples and admin-only action; added actions use unique names and
the corresponding public/protected auth behavior. Derive expected sample counts
from the explicit fixture dimensions instead of retaining a hardcoded two-action
formula. Do not weaken either growth threshold if the new lane exposes a defect.

### Request-owned resource snapshot

Inspection found that the HTML helper currently passes the entire selected raw
resource (including all actions) into `Context#with` for each client/detail/sample.
Each supplied subtree must be copied by the Context ownership contract, causing
unnecessary repeated full-resource copies as action count grows.

Fix this only in the server documentation helper: derive an owned resource
context once from the request's root context, before selecting client profile or
detail. Cache it for that request under raw resource identity plus canonical
resource path; do not use the whole mutable Hash as a hash key. Derive
action/sample/profile/detail contexts from that resource context, sharing the
unchanged resource and description snapshots. Cache lifetime is the Sinatra
request, never the server, class, generator or adapter. Distinct raw resources
at the same path cannot alias, and neither input nor shared adapter is mutated.

`Context.new` and `Context#with` retain all supplied-subtree copying rules.
No reader/signature change, capability registry or cross-request cache is added.
Focused assertions prove one resource snapshot per request, identity sharing
across its panels, separate snapshots for distinct raw resources, unchanged
caller data, and admin/member/admin isolation. The new action-growth lane then
checks the rendered request consequence.

### Files and checks

Implementer0 owns `benchmarks/endpoints.rb`, `benchmarks/documentation.rb`,
`benchmarks/spec/client_examples_spec.rb`, `test_support/all_client_performance_fixture.rb`,
affected `spec/performance/*` and documentation performance specs, the narrow
server-helper snapshot fix, and the relevant `doc/performance.md` explanation.
Coordinate any edit to `doc/client-examples.md` with implementer1. All Ruby paths
above are relative to `servers/ruby/`. No budget/reference/lock/workflow changes
are authorized by this amendment.

Before final review, focused tests must accept a valid legacy full page and
actual new overview, reject a missing navigation resource/init panel, wrong
role-map entry, injected private sample, mixed/wrong page shape and corrupted
proof/counter, and retain the exact footer/replay integrity checks. Synthetic
legacy cases alone do not prove historical source compatibility. Pre-review
quick checks are focused shape/role-proof and request-owned snapshot
identity/isolation specs plus syntax/lint in the prescribed environments.

After all intended changes are committed, quick checks pass and independent
review accepts the complete branch, run the required paired comparison with the
actual selected exact baseline and candidate exports through the one neutral
updated harness and locked environment. Also run the full frozen candidate
all-client/resource/action scaling contracts with real generators, recording
each lane and both details; these integration gates belong after final review.
Their environment may be prepared earlier through a watcher. The paired
legacy source run establishes the
historical shape compatibility, while the candidate run validates overview
semantics. Use the monitoring skill for long checks. Preserve complete receipts
and classify failures/inconclusive timing under existing policy; no automatic
budget/reference updates or retry-until-green loop.

## Visual-feedback milestone: navigation and shared shell

This is new user-requested work after the first live visual preview, not an
optional expansion of the initial design. The user supplied a second screenshot
(kept outside Git), identified wasted space in the version header, unreadable
validator values, a buried resource list with nested scrolling, inconsistent
root/shared-doc styling and incorrect Create/Clone action highlighting. The user
also requested restoring links to dynamic client libraries on the overview.
The lead accepted the direction below. This amendment supersedes the earlier
full-resource sidebar and overview resource-index placement and the original
theme-select/top-header assumptions; all example/auth/security contracts remain.

### Navigation and shell contract

Add `?page=resources` to the validated HTML page selector. It is the complete
resource directory, with the heading/anchor `resources`, a prominent labelled
filter and the full authorized resource hierarchy in the main document flow.
Reuse `[data-resource-nav]`, `[data-resource-filter]`, `[data-resource-item]` and
`[data-resource-link]` there. No fixed-height list, nested scrollbox or virtual
scrolling: browser page scrolling reaches every resource. Filtering retains
ancestor context and the original hierarchy and gives an accessible empty-result
message. The unfiltered directory works without JS.

Do not repeat that full tree on overview, authentication, resource or shared-guide
pages. Every versioned page has a prominent Resources link in the sidebar.
The overview has getting-started content, all available client libraries, init
examples and a short resource-directory link. Existing `/vN/#resources` links
resolve to the directory; old resource/action/example fragments still resolve
through the exact authorized legacy map on the overview. Keep that map even
though the visible resource list moves; it is required for compatibility and
for role-aware overview validation. Directory URLs are mount-aware and work via
the existing root default-version selector as other page kinds do.

Remove the full-width sticky API version bar. Put the API version/identity in the
sidebar brand area, linked to the API versions index. Immediately accessible
sidebar links are Overview, Resources and Authentication on versioned pages.
Below them show only current-page context: this resource's action links, or the
authentication/provider TOC. Then show example preferences and authentication
controls. The sidebar can have one viewport-height overflow area if needed, but
action/context lists have no independent height cap or scrollbox.

Resource pages start with semantic linked hierarchy breadcrumbs in main content:
Resources, each ancestor resource, then current resource. Use
`nav[aria-label="Breadcrumb"]` and `data-resource-breadcrumbs`; mark the current
item with `aria-current="page"`. Parent links select actual parent resource pages.
Keep current resource children as ordinary contextual links in its body, without
fetching/rendering their examples. Authentication breadcrumbs return to Overview;
shared guides return to Documentation/API versions. Do not add a search overlay,
SPA, new routing subsystem or duplicate full-resource navigation in breadcrumbs.

Keep a compact mobile navigation button available without restoring a desktop
header bar. Place it in a small mobile-only toolbar or at the content edge; its
geometry is shared with anchor offsets below. Retain skip link, keyboard focus,
Escape/drawer focus handling, sidebar access and browser history behavior.

### Compact theme and active navigation

Use three native buttons with local inline icons for Auto, Light and Dark in the
sidebar brand/control area. Each has `data-theme-choice` equal to `auto`, `light`
or `dark`, `type="button"`, an accessible name and title; the selected button
has `aria-pressed="true"`. Use a labelled group rather than a custom popup.
Icons are decorative to assistive technology. Preserve the existing persisted
theme values, automatic OS tracking and early theme application. Shared pages
use the same controls and storage; no second preference implementation.

Implementer3 reproduced the action bug: CSS root scroll padding and section
scroll margin sum to 160px, while JS had a hardcoded 120px active threshold.
Its focused computed-offset fix is accepted. Active targets are the actual
elements referenced by current-page TOC links; do not let an unrelated nested
section clear the current link. Derive the active boundary from the browser's
computed root scroll padding plus that target's scroll margin, with a small
rounding tolerance. Prefer one deliberate offset after removing the header,
but support the actual combined geometry. Clicking Create must highlight Create
at the native anchor landing; scrolling back above its boundary selects Clone
even if the hash still names Create. No sticky clicked-link override. Recheck
after resize, preference changes, initial deep links and back/forward.

The same target-based tracking supports headings referenced by shared-guide TOCs,
without rewriting Markdown content to add section wrappers. Preserve existing
heading IDs and correct broken TOC links against actual rendered headings.
Actual protocol/create-client rendering showed Markdown headings had no IDs,
so those legacy TOCs had no targets. The lead accepted a bounded renderer change:
implementer0 updates the existing `DocHelpers#doc` path to enable Redcarpet
`with_toc_data: true` and `tables: true`. This supplies generated heading anchors
and semantic Markdown tables without changing document text or schema content.
Preserve explicit HTML IDs; implementer1 verifies real protocol/create-client
headings, TOC targets and a table-bearing guide rather than only synthetic HTML.

### Parameter and validator presentation

The screenshot's validator values are squeezed by the global `.docs-main dl`
two-column metadata grid nested inside a narrow seven-column table. Replace
that accidental coupling with explicit semantic classes:

- Input table: Parameter, Type, Required, Details. Parameter includes machine
  name and the human label when different. Details contains description,
  default value when present, then labelled validator rules/options.
- Output table: Parameter, Type, Description, with the same name/label treatment.
- Retain every existing type/resource link, required flag, meaningful default,
  validator option/value and description. Empty/default sentinel handling remains
  exact; do not omit `false`, `0`, empty strings or nullable values accidentally.
- Action metadata and input/output layout metadata use `dl.docs-metadata`.
  Validator output uses its own `.docs-validators`/`.docs-validator` classes and
  ordinary flowing key/value rows. Keys can be emphasized and values wrap at
  word boundaries; never impose the global metadata grid on validator content.

Keep a real semantic table (`display: table`, normal table layout) in a labelled
`.docs-table-scroll` wrapper. Give Parameter and Details enough minimum width
for readable content (roughly 10rem and 20rem respectively); on narrow viewports
the wrapper scrolls horizontally without widening the document. Do not force
prose into two-character columns or set a table to `display:block;width:max-content`.
The wrapper is keyboard-scrollable where necessary. Ordinary shared-doc definition
lists use natural flow unless explicitly marked as metadata; style rules cannot
silently reintroduce this problem into protocol docs.

### Shared index and guide integration

The root API versions index and all existing `/doc`, `/doc/readme`,
`/doc/json-schema`, `/doc/<name>` and `.md` HTML aliases use the same theme,
sidebar/content shell, typography, code and table styling as resource pages.
Keep their URLs, protocol text, heading IDs, missing-document behavior, packaged
content and root/OPTIONS contracts. This task changes presentation, not protocol
meaning, generated schema contents or authentication-provider consent pages.

Common shell remains `main_layout.erb` + `doc_layout.erb`, with `[data-docs]` on
all documentation pages. Extend `data-page` to `versions`, `guide` and `resources`
in addition to the existing kinds. Static shared pages have no selected resource
and emit empty client/legacy-map arrays/objects instead of calling helpers that
require `@help`. Use `@documentation_title` for a meaningful document title when
no API version is selected; do not display a guessed `API v` heading.

Retain existing `@content`/`@sidebar` rendering. A focused new
`shared_documentation_helpers.rb` provides `render_documentation_index` (consumes
the root handler's existing `@api`) and
`render_shared_documentation(content:, title:, sidebar: nil)` (consumes already
rendered trusted repository documentation). Both select the common shell with
`@documentation_ui = true`, appropriate page/title, nil selected resource and
no current-user resource description. They must not rerun API discovery merely
to render a guide sidebar. The shared sidebar has API versions, default-version
reference/directory links where appropriate, shared guide links and the supplied
page TOC. Generic branding is API documentation, with no invented current
version. Reuse a common sidebar-brand/theme partial owned by the shell owner.

The root handler retains its current authentication/version discovery and passes
its result to the index renderer; shared guide routes retain their existing
content-loading/rescue behavior. The route owner wires the helper into Sinatra
and replaces only the final presentation calls. Shared TOCs use
`[data-action-nav]`; JS resolves their links to the existing heading elements.
Do not retain a second Bootstrap/jQuery presentation for these pages. Assets stay
local and mounted Rack prefixes remain supported. Keep the exact generated
HaveAPI footer contract used by performance provenance.

### Complete client overview

A new `version_page/client_overview.erb` partial restores links to Ruby/CLI,
JavaScript and dynamic TypeScript (callback/async), Python (sync/async), and PHP,
alongside the available configured Go/Rust/generated-TypeScript SDK identities.
Keep curl and raw HTTP examples discoverable without inventing a standalone
client package for them. These are library/setup links, distinct from the
language/variant preference controls. Filter by existing renderer availability
and actual configured profiles; an unconfigured generated SDK never appears.

Use the existing renderer metadata/profile interfaces and ordinary supported
library URLs. Restoring the small static library-link inventory is acceptable;
do not introduce a second variant registry, generalized client catalog or
unnecessary metadata/API expansion. Keep package identity/version wording honest
and preserve generated profile limitations. Owner0 wires this partial once into
the overview; it replaces the generated-only list, not the example controls.

### Independent implementation packages

| Owner proposed to the lead | Files and interface boundary | Checks/dependencies |
| --- | --- | --- |
| implementer0 | Common `main_layout.erb`/`doc_layout.erb`, common sidebar brand/theme partial, version page/sidebar, directory partial, breadcrumbs, resource/auth table markup; `documentation_helpers.rb`, narrow `DocHelpers#format_validators` and route/include seams in `server.rb`; UI guide | Owns shell contract. Wire shared renderer helper from 1 and client overview partial from 2. Coordinate `server.rb` with 4's OAuth hook window. Keeps existing performance follow-up ownership. |
| implementer1 | New `shared_documentation_helpers.rb`, shared sidebar, `index.erb`, `doc_sidebars/*`, focused shared/index rendering/packaging tests | Uses common shell inputs above. Does not edit common layouts/server.rb; send exact require/helper/route wiring to 0. Preserve root discovery and document loading. |
| implementer2 | New `views/version_page/client_overview.erb` and focused client-overview specs | Existing metadata/profile APIs only; send one partial-render seam to 0. Dynamic libraries present, configured SDKs present, absent SDKs absent, curl/HTTP discoverable. |
| implementer3 | Existing documentation CSS/JS and focused asset/browser checks | Consumes exact DOM above; compact icon theme controls, directory filtering, no nested list scroll, readable table/validator styling, computed active-target offsets, shared-guide highlighting and mobile navigation. |
| implementer4 | Existing OAuth package unchanged | Continue independently; no consent-flow redesign or TLS cutover implied by visual feedback. Coordinate narrow shared-file hooks through 0/lead. |

These are package boundaries for lead assignment, not an automatic ownership
transfer. The lead retains commit/hook quiet-window serialization and the final
user-visible wording pass. No writer may disturb implementer4's current hook
window. Performance ownership remains with 0 unless the lead explicitly hands
it over; the already implemented follow-up must not be re-investigated by a new
owner merely to populate the roster.

The lead subsequently paused all actual hooks/commits until every source owner
is ready, followed by one explicitly acknowledged quiet-window batch. An actual
Overcommit run isolated unstaged work and restored over a concurrent owner0 spec
edit during owner2's commit; owner0 reapplies its own tests. This incident does
not authorize resets or discarding other work. Source owners retain their edits
and package boundaries; the lead coordinates the quiet window and verifies the
intended final tree. No agent settings changed.

### Acceptance and verification

Quick checks cover new page selector/default root behavior, resource directory
visibility/filter hierarchy, mount-aware breadcrumbs/links and resource-type
links, complete available library overview, uniform shell on root and all shared
doc aliases, unchanged missing-doc/OPTIONS behavior, safe metadata defaults and
HTML escaping. Update the previous test that expected legacy `/js/main.js` on
protocol docs: uniform styling is now an explicit user requirement.

Browser checks reproduce the screenshot's token-lifetime validators at desktop
and 390px mobile widths; words/values remain readable, page-wide horizontal
overflow is absent, and narrow-table overflow is locally accessible. Check all
three icon themes on version/resource/directory/protocol pages with reload
persistence. Verify that the directory has no height cap, late resources are
reachable, the sidebar has no nested list scrollbar, and breadcrumbs navigate
parent/child resources. Reproduce Clone/Create native click and passive scroll
behavior at both widths, including scroll-up with an unchanged Create hash.
Check shared guide TOC tracking and heading deep links with the same geometry.

Update performance shape validation to require directory links plus complete
authorized legacy-map resource/action targets on the overview; full visible
resource inventory is now validated on the directory. Candidate complete-page
correctness includes that directory, and its fixed unrelated-resource allocation
request set may include the directory as a fourth fixed page kind. Paired timing
requests, dimensions, reference, budgets, runtime and normalization remain
unchanged. Full all-client/scaling and paired gates run after final committed
review; targeted shape/identity checks and lint precede it.

Refresh the existing session preview with the completed visual milestone and
record browser evidence before declaring the user feedback addressed. No release,
production deployment, default-branch integration or lifecycle change is
authorized. Rollback restores prior HTML/CSS/JS; API data and database state remain
unchanged, and existing persisted preferences still have the same valid values.

## User-feedback milestone 3: explanations, identity and quick search

New user requests follow the previous consolidated source range
`2f515626..415fc521`: meaningful validators, compact identity with explicit
visibility semantics, quick resource/action/parameter search on every page,
language-grouped client links, overview usage instructions and end-user
navigation cleanup. These additions precede final review/long checks; they do
not replace the accepted existing renderer, resource-page or performance scope.
The lead accepted the technical direction below and owns final user-facing
wording after facts are settled. No application edits were made by the architect.

### OAuth hold and boundaries

The user explicitly wants to wait for official cross-session communication
before continuing OAuth. Retain existing OAuth source/config contracts; stop
further implementation, offline preparation, return-location extensions and
local TLS activation. Current HTTP visual preview continues with its credential
and mutation guard. Implementer4 is held on that package. This is a work-item
dependency, not a paused/closed development session.

Future coordination is intended with `2026-10-24-vpsadmin-haveapi-upgrade` after
`2026-10-28-cross-session-messaging` deploys. Those names are future routing
intent only: do not inspect their records/teams/cluster, borrow their runtime or
communicate through an unofficial route. A future unreleased HaveAPI dependency
must be explicitly selected and verified. No such action is authorized now.
Identity/visibility markup may consume existing `current_user`/control data;
search must work through existing HTML docs authentication without changing
OAuth code, adding token parameters or general API cookie authentication.

### Validator meaning and representation

Authoritative source is `validators/*.rb`, `ValidatorChain`,
`Parameters::MetadataI18n` and `Params#validate`. These validators run after
parameter type conversion for supplied non-null values; required/default/null
handling also occurs in Params. Describe the advertised rule, not an invented
validator or a promise about all runtime action checks. Inclusion Hash keys are
the accepted machine values and values are human labels; localization can turn
an Array into such a Hash. Preserve their types and labels separately.

Implementer0 replaces raw option-to-string rendering with a focused presentation
helper (`documentation_validators.rb` is a suitable isolated home), called by
the existing `format_validators` seam. Give it the optional parameter type for
accurate length wording. It consumes only already filtered/localized metadata,
never changes validator classes, descriptions, translations or wire semantics.

| Advertised validator | Explanation/data that must remain visible |
| --- | --- |
| `present` | Parameter is required. `empty: false` disallows empty collections and empty/whitespace-only strings; `empty: true` permits emptiness, not an absent required value. Keep the separate Required column. |
| `include` | Allowed machine values, each as a typed literal; Hash entries pair that literal with its existing label. Arrays list their literal alternatives. An empty allowed set remains explicit. |
| `exclude` | Disallowed/reserved literal values; do not render them as allowed choices. |
| `accept` | The single required literal value, preserving false/zero/null/string distinctions. |
| `confirm` | Same as, or different from, the named parameter according to `equal`; show the machine parameter name. |
| `number` | Inclusive minimum/maximum; step measured from `min` or zero; `mod` requires a multiple from zero; odd/even where advertised. These constraints act on converted values; numeric strings accepted by this validator contain only digits. Do not confuse step with modulo. |
| `length` | Exact/minimum/maximum length (inclusive), characters for String/Text and neutral length/items wording only when type supports it. Do not invent byte limits. |
| `format` | Must match / must not match the supplied regex source, plus any advertised description. Show source as code; metadata does not include all Regexp flags, so do not invent them or translate arbitrary patterns into prose. |
| `custom` | The supplied application-specific description, labelled as such. Generic Custom#valid? always passes; enforcement belongs to application code. Do not claim generic enforcement from the description alone. |

Presence wording clarification: an active built-in Presence validator does make
a Typed parameter required, even when configured through the `present:` alias.
`ValidatorChain` sets its required flag for useful Presence instances;
`Typed#required?` delegates to it. `Params#validate` rejects missing or explicit
nil input before filling defaults or invoking individual validators. Therefore
ordinary optional input cannot retain an active Presence validator: false/nil
disables/removes that rule. `nullable: true` does not override requiredness
(`Typed#nullable?` also requires optional input).

The Required column remains the primary presence indicator. The rule's concise
text can emphasize the additional constraint: `empty: false` means the value
must not be empty (strings cannot consist only of whitespace); `empty: true`
means empty values are allowed. If mentioning presence explicitly, say the
parameter must be supplied and cannot be null. Do not say "when supplied" in a
way that implies an active Presence parameter may be omitted. Defaults do not
satisfy a missing required value in this pipeline. No validation behavior is
changed by this wording clarification.

Each built-in's configured `message` remains accessible as the validation error
message; it is supporting metadata, not the sole rule explanation. Preserve
additional/unrecognized keys even on a known validator under a clearly labelled
details area. Unknown extension names retain their actual name and complete
supplied description/options; make no guess about their behavior. Known fields
with an unexpected shape also use the honest fallback rather than disappearing.

Use readable lists or value/label rows for choices, not Ruby Hash inspection in
paragraphs. Format literals as JSON-style code where lossless (`"active"`, `0`,
`false`, `null`), so display labels cannot be mistaken for values sent to the API.
For unfamiliar structured metadata, use a labelled escaped pre/code block:
pretty JSON for compatible data; a clearly labelled Ruby inspection fallback
only when JSON would erase a value/key type. No evaluation, HTML trust, dynamic
formatter execution or lossy coercion. Preserve insertion order and every
option/value, including empty/false/zero values. Escape exactly once.

### Identity and visibility

Source evidence: `Action.describe` runs action authorization only for endpoint
descriptions or a non-nil `current_user`; `Params#describe` filters through that
authorization; example restrictions also skip anonymous users. vpsAdmin's
pre-authorize hook applies token scopes only to authenticated users. Therefore
anonymous version docs describe the whole declared API; signed-in version docs
show the permitted subset of resources, actions and parameters. Neither is a
guarantee that an object-specific operation will succeed for a particular ID.
Do not change these existing semantics or suggest anonymous users can execute
every listed operation. Authorization-filtered omissions must never reappear
through a search result or choice renderer.

Versioned pages show a compact sign-in icon link when signed out, with visible
focus, accessible name/title and decorative icon. When signed in, show the
actual escaped `current_user.login` with the existing sign-out control; do not
substitute token fields, OAuth client ID or a generic account label. The presence
of `current_user` determines displayed identity even if the existing OAuth
control hash has no session CSRF token (for example explicit Basic credentials).
Use the existing supported logout path for that mode; no authentication-flow
changes while held.

Show an explicit concise visibility note alongside identity: signed out means
all resources/actions/parameters; signed in means only those accessible to the
account. Keep the distinction visible, not only in a tooltip. If authentication
is disabled, no unusable sign-in action is shown, but the all-declared visibility
note remains. Neutral shared pages do not infer one identity from several API
versions; the search destination version resolves its own identity and displays
the proper visibility mode when visited.

### Search: existing HTML directory, no index service

Use the existing version directory URL as the only search destination:
`/v7.0/?page=resources&q=...`. Empty/missing q shows the normal full resource
directory; nonempty q shows resources/actions/parameters matching that query.
There is no new page enum, JSON endpoint, schema endpoint, bulk browser index or
OAuth return-location change. The existing OAuth return page is `resources`;
discarding the optional search query on re-login is acceptable during the hold.

Every docs page contains the same small GET search form. On versioned pages its
action is the canonical current version URL. On the API versions index and
neutral internal guides it targets the server's default version and explicitly
labels that version; it does not remember a guessed version in localStorage or
rerun full API discovery merely to render the form. Users can choose another
version through the existing version index. The search covers API reference
metadata, not protocol/guide content.

Form contract: `[data-documentation-search]`, ordinary `method="get"`, canonical
same-origin version action, hidden `page=resources`, a labelled `input[type=search]`
with `name=q`/`data-search-query`, and a submit button. Render it near the top of
the sidebar on desktop and keep it reachable in mobile navigation. Directory
main content may have a second instance with unique label/result IDs. This
replaces the old directory-only resource filter with a single coherent search;
unfiltered browsing still preserves full hierarchy and natural page scrolling.

Validate q independently of the page/resource selector: one scalar valid UTF-8
value, at most 256 characters, trimmed; reject duplicate/array/non-scalar forms.
No credentials in q. Search one already-produced request `@help`; do not issue
an OPTIONS request, describe twice, or use the private generated-client schema.
Build a transient result list only when a nonempty search is requested, not on
each overview/resource render. No shared cache or client persistence.

A focused `DocumentationSearch` helper consumes filtered description plus query
and returns plain result records; templates own final URLs/escaping. Search
resource path/name/humanized label, action name/aliases/HTTP method/path, and
input/output parameter machine name/label/type with parent context. Do not index
examples, defaults, validator values/messages, credentials, entire descriptions
or generator-private fields. Include authentication-provider resources/actions
from the filtered authentication description when their existing HTML targets
are available; label that context and link to the authentication page.

Use case-insensitive whitespace-token matching: all query tokens must match a
record's combined searchable metadata. Rank exact machine/name/path matches,
then prefix matches, then remaining matches, with deterministic kind/path/name
tie breaking. No fuzzy engine or external search dependency. Return at most 20
results plus an explicit more-matches/refine-query indication; never claim the
capped list is the entire API. Each result shows kind, resource/action context
and parameter direction/type where applicable. No result is authorized by its
presence: destination HTML still recomputes/filter-checks current permissions.

Resource results link to resource pages; action results include their stable
action anchor. Parameter results link to new additive stable row anchors that
include resource/action, input/output direction and parameter name. Owner1
supplies a single `documentation_parameter_anchor(...)` helper used by search
and owner0's row markup. It must be unambiguous for separators/unusual machine
names, HTML-safe and URL-fragment-safe; test colliding-looking names. Existing
resource/action/example IDs remain unchanged. Parameter landing keeps its owning
action highlighted.

Result template emits `[data-search-results]` containing ordinary safe links
and a concise count/status, including empty/refine states. On normal submission
it is part of the directory's full HTML page; direct URLs work without JS. The
page title/query and input preserve the escaped query; the page stays private,
no-store and uses the existing documentation HTML authentication boundary.

Implementer3 adds only progressive enhancement: debounce typing, abort obsolete
same-origin GETs, request the ordinary HTML directory with `cache: no-store`,
and parse/extract its known result region without executing returned scripts.
Use sequence checks so out-of-order completions cannot replace current results.
No search fetch for empty input; clearing restores the local neutral state.
Results remain ordinary links in a labelled region with an accessible status;
native Tab reaches them, Enter submits the form, Escape closes them. Do not
invent a partial ARIA combobox. Failures retain the normal submit action and
show a retry/open-results hint rather than a blank broken control. Clear
ephemeral results on page restore/search refocus before fetching fresh results;
do not reuse results across requests, auth changes or pages. Query/results are
not stored in localStorage/sessionStorage and are never placed in preference
records. No background authentication polling or cross-session infrastructure.

### Overview and navigation copy

Overview usage instructions briefly explain language and client variant,
Simple versus error-handling examples, resources/actions, search and the two
visibility modes. The lead writes the final prose from these facts; renderer
implementation details do not belong in those end-user instructions.

Client overview has one entry per language: Python links the words sync/async;
JavaScript callback/async; TypeScript callback/async and generated when configured;
Rust async/blocking when configured. Ruby library/CLI can share one entry; PHP
and Go retain their own. Existing profile identities/versions appear once per
generated SDK, including when TypeScript has dynamic and generated choices.
Use available renderer metadata plus the existing small URL mapping; no new
variant registry/catalog. Absent profiles stay absent. curl/raw HTTP remain
discoverable as request formats, not invented installable client libraries.

Version API navigation has no Guides, Protocol or Client examples/internal link
section. API index sidebar retains technical entry points under the explicit
label `HaveAPI internals`; remove its misleading main-content Documentation
heading/link. Direct internal pages keep the uniform shell and their sidebar
can use `HaveAPI internals` instead of Guides. Preserve all technical URLs and
protocol content. Enable Redcarpet `fenced_code_blocks: true` alongside the
accepted heading/table options (also consistently for the README rendering path)
so real fenced examples render as code. Preserve existing heading IDs and HTML
escaping; no prose rewrite or protocol/schema change.

### Implementation ownership and checks

| Owner for lead assignment | Independent package/files | Seams and acceptance |
| --- | --- | --- |
| implementer0 | Validator presentation helper/specs; existing validator delegation/Markdown options in server.rb; identity/visibility partial; version sidebar/overview usage slots; index/shared-sidebar navigation cleanup; common form and row-anchor wiring | Owns shared server/templates. Requires 1's small search/anchor/form interfaces, 2's client partial; preserves existing OAuth flow. Lead supplies final prose before commits. |
| implementer1 | New documentation search helper, search form/results partials, focused metadata/route tests; directory search integration through documentation_helpers.rb/resource_directory.erb | Owns search model/query parsing, result shape and anchor helper. Sends require/helper/HTML-form wiring and parameter-row call to 0. No duplicate describe or bulk index. Does not edit server.rb/common layouts or resource_body.erb directly. |
| implementer2 | Grouped client_overview.erb and its focused tests; previously assigned bounded Go fixture correction | Metadata/profile availability remains authoritative; one language entry and linked variants, exact generated identities. No server/JS edits. |
| implementer3 | Existing documentation.js/css and focused Node/browser tests | Debounced HTML search, accessible result region, responsive identity/validator/overview styling. No token/auth-flow changes or search framework. |
| implementer4 | OAuth package held | No preparation, activation, cross-session access or return-location edits until explicit resumed assignment. |

Before independent implementation, 1 confirms result/anchor helper names and
partial locals with 0/3 through the lead-approved package boundaries. The lead
serializes shared edits and actual hook windows; previous source quiet remains
until formal assignments. No application ownership transfer is implied here.

Quick tests: all built-in validator meanings, typed value/label choices,
zero/false/empty/default distinctions, unknown/malformed extension fallback and
escaping; anonymous vs member/admin current-user parameter visibility and actual
identity; search matching/rank/cap/mounted URLs/parameter anchors; duplicate/bad
q; no hidden member fields/actions/values in results; no second describe and no
search extraction for unqueried pages. Check actual fenced `/doc/client-examples`
and README code rendering, internal navigation placement and grouped library
availability. UI labels alone cannot satisfy these behavior tests.

Browser checks exercise resource/action/input/output lookups from overview,
resource and internal pages; default-version label on neutral pages; native
submit/no-JS fallback, stale-request ordering, keyboard/Escape/focus, empty and
network-error states; parameter deep links and action tracking. Verify search
does not mutate scroll/preferences before navigation. Repeat validator readability,
visibility-note/icon accessibility, theme persistence and mobile layouts on the
real HTTP vpsAdmin preview. Do not test live OAuth while held.

All original required review/performance/integration gates remain. New search
must not prebuild a growing action/parameter index on calibrated unqueried
overview requests; do not alter performance limits/reference/runtime. Final
review follows all committed intended additions and quick checks, then long
gates. Report the held OAuth rollout separately from visual readiness. No new
database state/migration, external index, production deployment, feature merge,
session pause or lifecycle action is introduced by this milestone.

## Milestone 4: compact controls, reusable search and responsive details

This is a new user-feedback milestone after the exact `82a7f2abcc1ecfc361097d30de39e93aca026d64`
review snapshot. Preserve that review's scope/evidence; these additions need
their own completed-source checks and final review coverage. This amendment
supersedes milestone 3's per-query HTML enhancement, cross-kind exact-match
ranking, three persistent theme buttons and prohibition on extracting search
metadata during an ordinary versioned page render. It does not change client
examples, API/OPTIONS contracts, authentication flows or performance policy.

The user additionally requires phone and tablet usability. The lead accepts
page-snapshot freshness and a narrow private HTTP-cache exception for the
compact search representation. OAuth implementation, preparation, activation,
TLS and cross-session/cluster work remain held. No application edits belong to
the architect. The lead owns final labels/prose and formal source assignments.

### Stable presentation package

- Keep the existing sidebar brand/version location, without restoring the
  removed version bar. Its top controls group contains one theme dropdown and
  the account controls. Move the existing versioned account partial here rather
  than duplicating it at the bottom of the sidebar.
- Theme uses a native `details` disclosure, `summary` with the current theme's
  decorative icon and accessible name, and the three existing
  `[data-theme-choice]` buttons inside. Retain their `auto|light|dark` values and
  selected-state behavior. Add `[data-theme-menu]` to the disclosure and
  `[data-theme-current]` to the summary's accessible-current-choice slot. Use
  ordinary disclosure/button semantics, not an incomplete ARIA menu. Selecting
  a choice closes it; Escape closes and returns focus to its summary. Keyboard,
  touch and outside-click dismissal must work without interfering with mobile
  navigation's existing focus handling. Existing preference storage and early
  theme application are unchanged.
- Signed-out versioned pages show the existing accessible sign-in icon when
  authentication is available. Signed-in pages show an account icon, the actual
  escaped `current_user.login`, and a compact sign-out control beside theme.
  Preserve the existing link/form, HTTP method, hidden CSRF field and
  `[data-documentation-login]` hook exactly. Long account names may wrap or
  ellipsize visually, with the complete name accessible. Keep the visibility
  note and any existing status message immediately below this controls group;
  do not hide the all-declared/accessible-subset distinction in a tooltip.
- Neutral index/internal pages have no authoritative version-specific identity.
  Their brand still has the theme dropdown; do not display a fabricated signed-in
  or signed-out state or authenticate extra versions to fill the controls.
  An ordinary account/reference link may target the labelled default version's
  authentication documentation, without claiming identity or changing login.
- Above the resource page's local Actions list, render the selected resource's
  full human-readable path and machine path from `@documentation_resource` in
  `[data-current-resource]`. Use its existing canonical resource URL if linked.
  This is context, not another global resource list. Preserve breadcrumbs,
  action anchors/tracking and the Overview, Authentication, Resources order.
- Search placeholder is exactly `Resources, actions, parameters`. Keep the
  explicit selected/default API-version label; the placeholder is not its
  accessible-label replacement.
- `DocumentationValidators.render` keeps its input/output helper contract and
  all milestone 3 meaning, escaping and fallback rules. Render one semantic
  `table.docs-validator-table` inside parameter Details: caption `Validation
  rules`, columns Rule and Details, one row per validator, with its rule name
  in `th scope="row"` and explanation in `td`. Retain typed allowed/disallowed
  value lists with separate labels, messages, false/zero/empty values and
  additional/unknown metadata. Structured fallback stays escaped `pre/code`,
  labelled JSON or Ruby as appropriate. No additional deeply nested choice
  table or lossy raw-Hash prose is needed.
- Scope outer parameter table column-width selectors to direct rows/cells so
  they cannot apply to the inner table. The rule-name column stays modest and
  the explanation retains useful width. Long code/metadata scrolls locally;
  the existing outer parameter-table region provides touch/keyboard horizontal
  scrolling on narrow screens. Do not squeeze explanations into two-character
  columns or make the entire page scroll sideways. Preserve semantic tables.

Owner0 owns these templates/helper markup and relevant Ruby/HTML specs; owner3
owns CSS/JS and asset/browser checks. They can implement this stable portion
independently of the search cache, after the lead's formal assignment.

### Search evidence and freshness decision

Current enhancement waits 250 ms, requests the ordinary resources search page,
then parses its result region. Each query authenticates, runs `describe_version`
and renders HTML. The own preview's milestone 3 receipt recorded 3.56 seconds
for a search. A read-only diagnostic in this investigation measured 3.12 seconds
TTFB for `?page=resources&q=vps` (14,241 bytes). These are preview observations,
not calibrated performance-gate results.

The same fixture's anonymous OPTIONS response was 2,162,195 bytes and contained
152 resources, 524 actions and 6,358 parameters. A diagnostic metadata projection
before URLs/matching strings was 581,888 bytes. This supports keeping parent
references in the compact representation rather than repeating complete paths,
URLs and ancestor matching text on every parameter. It is not a final payload
size claim. Existing browser smoke receipts verify behavior, not per-keystroke
latency. No additional broad benchmark is needed to choose the architecture.

HaveAPI exposes no permission revision or authorization-cache invalidation API.
Its small Params caches cover static layout/namespace, not current authorized
views. Authorization may depend on application hooks/current user. A user ID,
role label, TTL or source revision alone cannot prove that metadata is current.

Chosen contract, explicitly accepted by the lead: search matches the authorized
metadata snapshot of the rendered page. A fresh versioned HTML response already
computes authorized `@help`; derive a deterministic compact projection and
SHA-256 fingerprint from that same object once per request. No second describe,
OPTIONS call, generator schema or shared server cache is introduced. This adds
an intentional O(searchable-metadata) pass and transient projection allocation
to ordinary versioned HTML. Evaluate it under the unchanged performance gates;
the earlier no-extraction invariant no longer applies.

The page emits only the fingerprint and compact-index URL, not the bulk index.
The browser lazily loads that URL on search focus/intent, then matches all typing
locally. A subsequent freshly rendered page with the same version/view can reuse
the private browser HTTP-cache entry without a second describe/network roundtrip.
A changed searchable projection, version, mount, locale or visibility mode has
a different key. The HTTP cache's retention time is not a permission TTL.

Already-rendered pages and their loaded index can remain stale while open, just
as their displayed documentation can. There is no instant revocation/push or
background permission polling promise. New destination HTML always authenticates
and describes again. Login/logout retain normal full-page navigation, destroying
the old document's JavaScript state. A cached index is not authorization to call
an API action. This is a deliberate documentation-snapshot contract, not an API
authorization cache.

### Compact projection and route contract (owners 1 and 0)

Owner1 owns a small `DocumentationSearch::Index` in the existing search component
(a sibling `documentation_search_index.rb` is acceptable). It is constructed
from filtered `@help`, canonical version base path, version, resolved locale and
`anonymous|authenticated` visibility. It exposes `payload` and `key`; key is the
lowercase SHA-256 hex digest of the deterministic JSON payload bytes. Format 1
is an internal browser/server contract, not a general API schema service.

Payload fields are `format: 1`, `version`, `base_path`, `locale`, `visibility`,
`resources`, `actions`, `parameters`. Use named JSON object fields and parent
indices to avoid repeated ancestry on every parameter:

| Collection | Record fields |
| --- | --- |
| resources | `path` (machine-name array), `label` (existing display label), `authentication` (provider name or null), `search` (resource path/name/humanized/custom-label metadata used by current matching) |
| actions | `resource` (resource-array index), `name`, `label`, `identifiers` (existing exact/prefix candidates: name, dotted action path, aliases, HTTP path), `search` (own humanized name, method and advertised label) |
| parameters | `action` (action-array index), `name`, `label`, `type`, `direction` (`input|output`), `humanized_name` (existing additional name matching term) |

All strings come from the existing explicit metadata whitelist. Index no
examples, defaults, validator values/messages, prose descriptions, object data,
account identities, CSRF values, tokens or generator-private metadata. Include
authorized authentication-provider resource trees as today. Sort traversal
deterministically and keep parent indices valid. No silent truncation of the
index: the 20-result cap belongs to matching, not extraction. Exclude unknown
metadata by construction rather than serializing `@help` and deleting fields.

Build matching context from the resource/action parent references. Resources
use their leaf/path identifiers; actions use `identifiers`; parameters use their
machine name. All whitespace tokens must match case-insensitively as before.
Sort by kind **resource, action, parameter first**, then exact/prefix/remaining
match strength within that kind, then existing deterministic provider/resource/
action/name/direction ties. Preserve cap 20 plus explicit more-matches state.
Use the same projection for Ruby fallback matching and browser matching; owner1
and owner3 share representative expected ordering fixtures. The internal search
constructor may be refactored to consume Index, with owned callers/specs updated;
do not maintain duplicate enumeration or a second metadata registry.

Preserve existing ordinary GET search: `/v7.0/?page=resources&q=...`, query
validation, native submission and result anchors/URLs. Add a representation of
that same documentation route:

`/v7.0/?page=resources&search_index=<64-lowercase-hex-key>`

Validate this selector as one scalar, with no duplicates/arrays, and only with
`page=resources`, without `q` or `resource`. `search_index=current` is the one
explicit bootstrap form described below. Invalid combinations return 400. Use
canonical mounted, explicit-version URLs in emitted forms; preserve root's
ordinary default-version selection behavior and all OPTIONS/machine endpoints.

After the existing documentation authentication and one describe, compute the
current projection. A requested hex key must equal its key. On mismatch return
409 with a small safe reload/open-search hint, `private, no-store`, and **no
index payload**. Do not serve historical server snapshots, redirect to a new
key or treat possession of a hash as permission. Authentication/error handling
runs before cache success. A fresh conditional request must also pass current
authorization and key equality before any 304 response.

Successful compact output is minimal `text/html; charset=utf-8`, containing
exactly one inert `script[type="application/json"][data-documentation-search-index]`
whose JSON is `{key, index: payload}`. Escape `<`, `>` and `&` using the existing
documentation JSON helper. Do not include layout, examples, resource bodies,
identity/control markup or executable assets. This is an HTML documentation
representation through the existing `documentation_authenticated?` boundary;
do not change OAuth code, scopes, cookies, return locations, API authentication
or OPTIONS to implement it. Owner1 owns the partial and dispatch helper;
owner0 provides only the narrow early-return seam after authorized `@help`.

For a matching keyed successful response only, set
`Cache-Control: private, max-age=86400, immutable` and an ETag derived from key.
Merge `Vary: Cookie, Authorization` with the existing configured locale-header
Vary; do not overwrite it. Preserve other existing security headers. Never
cache response bodies with authentication errors or Set-Cookie state changes;
those remain `private, no-store`. Ordinary full HTML and query-results pages,
bootstrap output, login/logout/callback and all errors remain no-store.

This narrowly permits browser retention of filtered metadata that previously
arrived only in no-store pages. It is private HTTP caching, not a shared/public
cache; logout does not promise physical erasure of browser cache files. A fresh
page may reference an old entry only if its newly authorized projection is
identical. Different accounts with identical permitted metadata may safely
produce the same content key; no identity is present in that data. Credential
Vary adds ordinary browser partitioning. Do not persist index/query/results in
localStorage, sessionStorage, preferences, Cache API or a service worker.

### Browser loading and neutral pages (owners 1 and 3)

`documentation_search_form_options` supplies `index_url` and `view_key` as well
as its existing locals. Forms emit `[data-search-index-url]` and
`[data-search-view-key]`; all forms in one versioned document share the memoized
projection/key. The index URL is same-origin, canonical, contains no credentials
and never copies arbitrary document query parameters.

Do not fetch the index on every page load. Search focus/pointer intent starts
one deduplicated fetch shared by forms for the page's selected version/key;
typing uses the loaded data immediately without the old 250 ms/network debounce.
If data is cold, show loading status and apply the latest input when it arrives.
Use ordinary HTTP-cache behavior (`cache: default`), `credentials: same-origin`,
`redirect: error`, and `Accept: text/html`. Validate the response representation,
format, version, canonical base path, row types/parent bounds and expected key.
Parse its inert JSON without executing/adopting returned HTML. Reconstruct
result text/links with DOM APIs, preserving the existing URL/anchor contract and
unambiguous UTF-8 parameter-anchor encoding. No external or arbitrary result URL
may be accepted from metadata.

Clearing/Escape, query changes and obsolete completions must not resurrect old
suggestions. Keep ordinary focusable links, region/status announcements, native
Enter submission and the safe submit/reload fallback on error/key mismatch. No
query/result persistence. A loaded snapshot can remain in document memory; no
automatic live permission refresh is implied by refocusing the same document.

Neutral index/internal pages still label and target the default API version,
without a second discovery merely to render their shell. They have no fresh
authorized default-version `@help` proof for this docs authentication boundary;
do not invent one from root's multi-version discovery or persisted preference.
Their `view_key` is empty and `index_url` uses `search_index=current`. This form
authenticates/describes once on search intent and returns the same compact
envelope with `private, no-store`. It is used only in that document's memory.
Consequently neutral-page navigation cannot promise zero-request reuse; safe
reuse without obtaining a fresh authorized view cannot be proven there. This
bounded exception avoids extra page-load discovery or a cache-validation service.

A BFCache-restored document likewise lacks a freshly rendered view proof:
`pageshow.persisted` clears its loaded index/suggestions and switches its next
search load to the no-store `current` representation. Normal new-document loads
use their fresh HTML key. Do not change OAuth/login-return behavior for search.

### Boundaries, acceptance and delivery

| Owner for formal lead assignment | Files/package | Dependencies |
| --- | --- | --- |
| 0 | `views/version_sidebar/{brand,authentication_control}.erb`, `version_sidebar.erb`, common shell seam as needed; `documentation_validators.rb` and focused specs; narrow `documentation_helpers.rb` authorized index early return; `doc/documentation-ui.md` | Presentation DOM above is stable. Preserve existing auth forms/links. Owner1 supplies dispatch/helper names and form locals before the shared seam edit. |
| 1 | `documentation_search.rb`, optional sibling index helper, `views/documentation/{search_form,search_results,search_index}.erb`, focused search/route/index specs | Owns canonical extraction, fingerprint/cache headers/selector validation, fallback ranking and form locals. Coordinate only the narrow shared require/dispatch seam with 0. No OAuth source edits. |
| 3 | `public/js/documentation.js`, `public/css/documentation.css`, focused Node/browser tests | Consumes the exact form/index contract; owns dropdown behavior, local matching, cache consumption, responsive controls/tables and real preview validation. |
| 2 | No new client-links package | Existing client inventory/grouping is unchanged; use only for a separately assigned independent check if useful. |
| 4 | Held | No OAuth preparation, activation, TLS, cluster or cross-session work. |

Quick checks prove deterministic key stability; changed visible resource/action/
parameter, label/alias/path, version, mount or locale changes key; private metadata
never enters payload. Anonymous/member/admin and permission-change fixtures must
show fresh-page keys and index membership from the same authorized description.
Prove exactly one describe and one projection per ordinary versioned request,
correct/mismatching key behavior, bootstrap and error no-store, keyed-only private
cache headers, Vary preservation, Set-Cookie no-store and authentication before
conditional reuse. No optional live OAuth verification while held.

Matching tests must prove resource-first ordering even against an exact action/
parameter, within-kind strengths, cap/more, nested/auth-provider paths, input/
output anchors, Unicode, malformed payload rejection and safe rendering. Add a
representative shared Ruby/browser result-order fixture, not a parallel framework.
Retain existing no-JS normal GET search and account/validator semantics tests.

Browser acceptance on real fixture: cold first search, repeated local queries
with no extra network requests, navigation to another same-view resource using
the cached keyed representation (prove no second server index request), changed
key causing a cold load, mismatching view returning a safe fallback, neutral
page and BFCache bootstrap, no query/result storage, and no scroll/preference
movement until a result is followed. Record payload bytes, cold-load timing,
warm input-to-results timing and actual request counts as diagnostics. Do not
claim instantaneous cold loads or replace calibrated gates with these numbers.

Check 390 px phone, 768 px and 1024 px tablet, and 1440 px desktop, including
touch and keyboard. Sidebar/navigation, search suggestions, account controls and
theme disclosure must remain reachable with useful touch targets and no overlap.
Keep full resource browsing natural, breadcrumbs/current resource/action tracking
clear, snippets readable with local horizontal scrolling, and validator tables
readable with local scrolling where necessary. Assert document width does not
exceed viewport width. Test dark/light/auto, long account/resource names, long
regex/unknown metadata and keyboard focus through disclosure/mobile navigation.

Quick focused checks and lint precede commits/review; existing long all-client,
allocation/scaling and paired performance gates follow final committed review
under the established watcher procedure. Reference, budgets, fixtures, runtime
and provenance requirements remain unchanged. A fingerprint pass that fails a
gate needs diagnosis and implementation adjustment, not a waived limit.

No database/migration, public API/client protocol, persistent server state or
deployment ordering changes are introduced. Browser data is format/content
keyed; incompatible projection changes increment format, rollback simply stops
emitting new keys. Cache eviction/disabled caching/mixed asset versions degrade
to a cold load or normal GET fallback. No production deployment, integration or
session lifecycle action is authorized by this amendment. Current HTTP visual
preview continues; the held OAuth rollout remains a separate dependency.

## Bounded upstream 0.31 reconciliation

The milestone 4 same-base head is `4f80b23c2ad02f0d227a000ced1b99d6d42a57f3`
(tree `0f551c74ceb590cdff9b19980fc480ceb9d314e5`), tree-identical to prior
`09ef7905430e67042a6f047a0eb78c587189ff75` above base
`2f5156262baaf137800c17a9321e617c2b5df1d5`. Fresh upstream is
`f6e5c3750c747b33ec869c54ca220bf6f1d9d2d0`: `29fae9e0` isolates historical
maintenance-version test fixtures, `ae909bef` synchronizes source packages to
0.31.0, and `f6e5c375` enforces master `X.Y.0` release policy. Their 24 changed
paths have **no overlap** with the feature's 109 changed paths. No protocol,
runtime dependency range beyond internal HaveAPI constraints, Nix pin, MSRV,
benchmark graph/budget or feature-source repair is indicated by this inspection.

### Source and evidence boundary (owner2)

After lead grants the exclusive Git window, rebase the existing five logical
feature commits onto exact fresh upstream, retaining all old refs/receipts.
Follow upstream 0.31.0 and `~> 0.31.0` internal constraints; do not run a version
bump, edit upstream metadata back to 0.30, choose a release line or publish.
Prove old/new feature patch equivalence with range-diff and full-index aggregate
diffs, and prove the old-final/new-final delta is exactly the upstream delta.
Final trees necessarily differ; the earlier exact-tree proof remains historical.
Unexpected conflict or extra delta requires inspection before further writes.
Retain exact new base/head/tree, clean status, whole-series/no-migrations inventory
and unchanged held-OAuth flow bytes for final independent review. No new feature
commit is needed solely to adopt already committed upstream version metadata.

### Prepared input reconciliation (owner1, then owner0 checks)

Before changing ignored inputs, preserve their current locks/hashes and existing
receipts under this session; create a new source-bound refresh receipt rather
than overwrite `verification/generated-inputs/` or `performance-82a7f2ab/` proof.
Use the unchanged repository Nix tools and each declared Gemfile/gem home; keep
workspace CLI identity checks outside the component Ruby environment. Serialize
writers to the shared root gem home and no concurrent hooks/bundle installation.

| Input | Required disposition |
| --- | --- |
| Root tools `Gemfile.lock` / `.gems` | No HaveAPI package or upstream declaration change. Reuse after lock/tool/availability verification; no blanket dependency update. |
| `servers/ruby/Gemfile.lock` | Refresh local path package versions/constraint from 0.30.0 to 0.31.0 using Bundler local resolution, then verify/install from that retained resolution. Explicit sibling Ruby client remains selected. |
| `clients/go/spec/documentation.Gemfile.lock` | Same bounded refresh for server, Ruby client and Go generator path packages. Keep its distinct external graph (including JSON 3.1.0); do not replace it with the server/benchmark graph. |
| `clients/rust/Gemfile.lock` / isolated `.gems` | Refresh local Ruby-client/generator versions and constraint; preserve external graph including JSON 2.21.2 and Fiddle. Use the existing isolated Rust environment. |
| Other component locks | Standalone Ruby-client, Go and TypeScript locks are currently absent. Prepare only when the assigned command actually uses those bundles. Existing root-bundle TypeScript checks use explicit sibling `-I` paths and do not require inventing a release build or all missing locks. |
| Local JavaScript | `package-lock.json` and installed-package metadata still identify 0.30.0. Refresh with the ordinary npm install against the retained lock, without upgrade flags; require unchanged external package resolutions/integrities. Rebuild with `npm run build` so bundle/declarations come from final 0.31.0 source. The tracked bundle must agree with upstream; diagnose any extra tracked delta. |
| Python | Run ordinary `uv sync` against the retained lock, without upgrade flags, to update editable `haveapi-client` to 0.31.0 and its installed metadata. Preserve external resolutions; subsequent commands remain `uv run --locked`. No stale 0.30 wheel/installed distribution counts as current source. |
| HTTP preview, owner4 only at later refresh | Own `preview/Gemfile` explicitly selects all five sibling HaveAPI source gems while leaving vpsAdmin's installed `~> 0.29.9` pin untouched. Its separate `preview/Gemfile.lock` currently records all five as 0.30.0 and internal `~> 0.30.0` constraints. During the separately granted final-head HTTP refresh after review, preserve that lock/graph, reconcile its source-package records to 0.31.0 within its own gem home, preserve external resolutions, and prove all five loaded paths/versions. Neither a source mount nor another bundle's successful refresh proves selection. Keep this graph distinct from root/server, Go, Rust and frozen benchmarks. |
| Generated artifacts | Prior extracted gems, generated SDK/manifests, compile outputs and source identities remain historical. Regenerate for final-source checks; cache directories may accelerate builds but are not verification receipts. Run `make doc` before fresh server packaging/specs. |

Prefer `bundle lock --local` with the exact component Gemfile before any needed
install. Retain full before/after locks, not just package-version text; unexpected
external dependency changes are a preparation deviation to resolve, not silently
accepted input equivalence. Verify loaded HaveAPI/server/client/generator paths
and 0.31.0 constants, plus Python/JS installed identities. The old prepared 0.30
path locks cannot be relabelled as successful 0.31 preparation. Do not invoke
`make version` or the broad `make release-deps`/release build for this refresh.

The separate published **TypeScript runtime stays exactly 0.30.2**, SHA-256
`96450c40a55ec7b7af4fca903d045bd0fc7ba1216efe12c3fee9b3e6a09e9198`.
Upstream release instructions explicitly distinguish it from candidate source
VERSION; retain it and its declarations for the prescribed wire/consumer checks.
Do not substitute the newly rebuilt local 0.31 bundle in that lane. Independent
Rust 1.95.0 MSRV binaries/manifest and development 1.99 toolchain remain reusable
after identity verification; Cargo inputs/MSRV policy did not change. No tool
redownload, compiler upgrade or generated-crate version redesign is needed.

### Verification and shortest delivery path

Owner0 prepares **new** final-source performance exports: manual quick baseline
is fresh upstream `f6e5c375...`, candidate is the rebased final head, and neutral
harness is that final reviewed candidate. The earlier `2f515626...`/`82a7f2ab...`
exports prove only their recorded preparation, not the new pair or a measured
result. Keep the existing frozen benchmark Gemfile/lock/shell/gem store after
hash/tool verification, then let ordinary workers prove the complete activated
graph and loaded paths. Existing `SourceVersions` receipts already verify
synchronized 0.31 metadata; do not use/broaden the historical 0.30 maintenance
normalizer. All budgets, counters, reference and timing policy remain unchanged.
Weekly, if required by the existing workflow, still uses immutable reference
`b85ec364057f536940d689b09e612512ffffaf82`; event CI uses its documented pair.

Sequence: owner2 rebase/equivalence receipt; owner1 bounded input refresh and
loaded-source proof; owner0 `make doc`, source metadata
`ruby utils/release/cli.rb check-clean --master`, focused
`spec/performance/release_lineage_spec.rb`, profile registration/mount specs
(`profiles_spec.rb`, `typescript_profiles_spec.rb`, `profile_mount_spec.rb`) and
the existing three packaging specs against a newly built 0.31 server gem.
Check current JS build output and Python locked identity as above. Prior
unchanged UI/asset unit results keep their exact source/input scope; no blanket
rerun solely for rewritten SHAs. No release-tag validation/publication or new
release-tool project is needed. If a check is long/uncertain, use the existing
watcher procedure and preserve final-review ordering for integration gates.

Final independent review covers the refreshed range and material input boundary;
then the already-required final HTTP preview/browser acceptance, generated
compiler/wire/MSRV checks, full documentation/all-client/scaling and paired
performance gates run with fresh source receipts. Input reuse is not result
reuse. Keep live preview and its old graph unchanged until its separately
assigned final-source HTTP refresh; that refresh must select local 0.31 paths.
Owner4's later HTTP-only grant covers this preview bundle reconciliation; it does
not resume private OAuth fixture preparation, TLS or other held work. Preserve
the current unit until that explicit refresh and retain its original health/
source receipt; this design authorizes no activation or preview mutation.
No new app behavior, migration, production rollout or recovery format is added.
Old source/input evidence remains available for diagnosis; integration remains
separately unauthorized. OAuth/TLS/cross-session work and open R1 remain held.

## Milestone 5: coherent identity, navigation and account controls

New user feedback follows the reviewed milestone 4 tree, now represented by
clean `9f68dad5436799d82e9c9e1c69e73866a279e9a6`; R2's history correction did
not alter final source. Screenshot 3 was inspected outside Git. Its sidebar
shows both `Vps` and `vps` under an unnecessarily inset Resource heading. Actual
root markup still adds `API description` above Available versions; actual
`/doc` renders a four-link list already repeated by its sidebar. These are
whole-page navigation issues, not just words to substitute.

This amendment is the stable brief for owners0/1/3. Their packages can proceed
after the lead's formal grant without waiting for partner account configuration.
Owner4's narrow R1 fix is independent; its account-flow extension follows the
explicit interface below and lead sequencing. Main owns final prose. The user
requires the literal placeholder `...`, overriding milestone 4's long text.

### One identity and one navigation structure (owner0)

Add optional display-only `HaveAPI::Server#documentation_name`, configured before
mount. Its setter accepts nil (use fallback) or a nonempty trimmed valid UTF-8
String of at most 256 bytes without control characters; copy/freeze the value
and reject other shapes. No HTML, URL or authority semantics attach to it.
The helper `documentation_identity_name` returns this name, otherwise the
display value of the current request's host with nondefault port. Escape at
rendering, not in the stored value. The fallback describes the current host;
it must not infer a production domain from a preview IP or module name.

Source inspection found no existing framework API label/canonical-domain option.
vpsAdmin already has `SysConfig.get(:core, :api_url)` and `API.configure` before
mount. The partner can set `api.documentation_name` from its chosen application
name or the validated canonical API URL's host/port. HaveAPI must not contain
`api.vpsfree.cz` as a default. This property does not rewrite request examples,
API paths, OAuth origins, redirects, proxy trust or search-cache identities.

Use this identity consistently in the brand and document title: brand links
to the mounted versions index; a versioned page shows its version as a separate
small line/element rather than replacing the API identity. Keep specific page
titles, adding the identity for browser tabs. Avoid duplicating the name in
multiple main-content headings. Long names wrap/ellipsize accessibly without
pushing account/theme controls offscreen. No new header/version bar.

Root main content is a single `API versions` heading and the existing available
version links/default marker. Remove `API description` and the redundant second
heading. Preserve version filtering, actual version values and mounted links.
Shared sidebar keeps API versions, default API reference and default Resources.
Its `HaveAPI internals` heading itself links to `/doc`; remove the separate
`Overview` item. Retain its direct links to HaveAPI/README, protocol, JSON schema,
client construction and client examples. This sidebar is the internal menu.

`/doc` and its existing `/doc/index[.md]` aliases become a concise introductory
page headed `HaveAPI internals`, explaining that these are framework/protocol
and client-development references; remove their duplicate link list. Preserve
all technical URLs/content elsewhere. Internal breadcrumbs are API versions →
HaveAPI internals → current article; on the internal overview, its final current
crumb is HaveAPI internals only, not a duplicate link and current crumb. Version
API pages still contain no internals/Guides menu. Owner0 edits the tracked
`servers/ruby/doc/index.md`, not a generated copy of a different source.

For a selected resource, `[data-current-resource]` becomes one natural full
human-readable resource path (for example `Vps / Snapshot`) above local Actions.
Remove the generic Resource heading and redundant machine-path line. Align its
text with the primary navigation/action headings, using the same content inset.
Preserve the canonical resource link, breadcrumbs, action anchors and active
tracking. Exact machine names remain available in paths/examples; the sidebar
does not need a second rendering of the same identity.

### Search presentation and neutral cache correction (owner1 + owner3)

Every search form uses placeholder exactly `...`; preserve the selected/default
version's explicit accessible label and normal GET submission. Resource result
primary titles use the complete dotted machine path, e.g.
`Resource: vps.snapshot`, never only `snapshot`. Resource result context uses the
full display-label hierarchy, including ancestors, when useful; do not repeat
the identical machine path merely to fill a second line. Action/parameter titles
retain their action/parameter name, with the **complete** resource path in their
context, plus existing action/direction/type/provider information.

Native HTML and browser suggestions must produce the same names and context.
Derive resource display hierarchy from existing index resource paths/labels;
do not add raw description metadata or a second catalog. The matcher may return
an additional derived presentation field, but serialized format 1, its whitelist,
fingerprint, permissions, matching/ranking, 20-result cap and result URLs remain
unchanged. Owner1 supplies Ruby presentation helpers/result fields and expected
display fixtures; owner3 uses that same documented rule in JS. Keep Unicode,
escaped labels and authentication-provider context unambiguous.

Owner1 also owns the identified one-header repair in
`SharedDocumentationHelpers#render_neutral_documentation`: ordinary neutral
success pages must explicitly use `Cache-Control: private, no-store`, with
existing route assertions extended to index/internal aliases. This does not
change the keyed-index private cache exception or bootstrap behavior. Owner0
does not edit this helper file concurrently; its shell changes can use server,
documentation helpers and templates instead. Neutral pages retain lazy
`search_index=current`; no extra full discovery to render their search form.

### Authoritative account presentation (owner0)

Use the same person silhouette for signed-out and signed-in account controls,
replacing the entry arrow. Signed-out link has accessible name `Sign in`.
Signed-in control is native `<details data-account-menu>` with a summary named
`Account` and a decorative person icon. Inside, show the actual escaped account
login once, then `Sign out` and, when supported, `Switch user`. Preserve status
messages and the explicit visibility note outside/below the menu. Do not infer
identity from a token, provider name or OAuth configuration alone.

Define one request-local presentation helper, `documentation_account_context`,
returning nil or `{version:, user:, authentication:, controls:}`. `user` is the
actual authenticated object; `authentication` is existing provider description
metadata; `controls` is the existing public OAuth controls hash or nil. It does
not authenticate, describe or read credentials itself. Pass these locals to
brand/account/status partials instead of assuming every page has `@v`/`@help`.
For versioned pages, derive them from the existing authenticated `@v`, `@help`
and `current_user`; memoize the controls once.

For a root versions index with **one declared API version**, owner0 changes only
that HTML route's authentication setup: call
`documentation_authenticated?(default_version)` once, reuse that actual user in
the existing `auth_users_by_version` map and existing `describe` call, and expose
the resulting default-version account context. No second describe/discovery or
second authentication for the controls. Its existing version overview login
destination is acceptable; do not add root return-location semantics.

For multiple declared versions, retain the existing cross-version ordinary
authentication/description path and hide index account controls; this is the
bounded safe choice for incompatible providers. Do not guess compatibility from
matching provider names or use one user's identity for another version. Keep
OPTIONS and API action authentication unchanged. Root/full HTML stays no-store.

Internal guides do not acquire or imply an identity. Where the default version
is unambiguous, they may show a neutral person link named `Account` to that
version's authentication page, not a false signed-out state. They do not invoke
authentication/discovery solely to fill the shell. Multi-version neutral pages
can omit that account link. The single-version index is the authoritative
neutral-page account entry requested by the user.

Basic/current explicit credentials retain their actual identity and existing
sign-out link where available. Source shows the legacy `_logout`/401 URL-userinfo
workaround; it cannot promise portable credential erasure or user switching.
Do not invent an XHR bad-password reset, changing realm, credential-storage form
or fake Switch user action for Basic. Keep those historical routes unchanged
and document the browser limitation. OAuth-session sign-out retains its existing
same-origin POST and hidden CSRF field. Explicit credentials still take priority
over any documentation cookie; menu actions must reflect the actual mode.

### Optional OAuth switch and independent R1 fix (owner4)

The user lifted the earlier coordination hold for this bounded work. It does
not authorize a provider protocol redesign, refresh support, local TLS fixture,
new public-client semantics or whole-account SSO logout. R1 remains its own fix:
an invalid/cancelled/failed callback must not clear an already-valid docs session;
pending-cookie clearing, successful replacement and established failures remain.
Its focused source/spec package can finish independently of switching.

Add optional strict Boolean `switch_user: false` to `documentation_oauth(...)`.
It is an operator assertion that a fresh authorization for this dedicated client
lets the reader select credentials/account, not a discovered OAuth feature.
When false, omit the Switch user form. When true and the current identity is a
validated documentation-cookie session, controls expose `switch_user: true`.
Owner0 renders a second form to the existing `logout_url`, with the same CSRF
nonce and hidden `switch_user=1`. Normal Sign out submits no switch field.

Owner4 validates this optional field as one scalar exact `1` and requires the
configured capability before any state mutation; reject duplicate/array/other
forms and disabled capability. The existing same-origin and session CSRF checks
still apply before clearing cookies or revocation. A successful switch performs
the existing local sign-out/revoke sequence, then 303 to the fixed documentation
login route for the default version, starting fresh state/PKCE. Do not accept
arbitrary return URLs, extend OAuth scopes or send invented prompt parameters.
Switch deliberately ends the old docs session before reauthorization; cancelling
the next login leaves the reader signed out. This does not undo R1's protection
against unsolicited callback logout.

Revocation failure retains the current honest 502/local-sign-out behavior and
does not silently continue to login or claim switching succeeded. No retries,
stored revocation queue, refresh or SSO-wide side effects. Ordinary Sign out's
behavior and default-version destination remain unchanged. Capability off must
preserve existing consumers and cookies; no new cookie schema is required.

Read-only local vpsAdmin source shows no implemented `prompt=login` or
`select_account` contract. A dedicated OAuth client with
`allow_single_sign_on=false` makes `find_sso` return nil and presents editable
credentials, which is the bounded proposed integration. The lead has since
received official peer source confirmation that a dedicated nondefault client
with SSO disabled presents editable credentials independently of account-wide
SSO; endpoint base is `core.auth_url || core.api_url`, with unversioned routes.
This proves support, not actual live SysConfig/client configuration. Configured
client confirmation and acceptance are still required before enabling
`switch_user: true`; do not
claim an account chooser from merely redirecting through OAuth again.

### Ownership, partner boundary and checks

| Owner | Complete package and files | Dependency |
| --- | --- | --- |
| 0 | `server.rb` display-name setter and single-version root seam; `documentation_helpers.rb` identity/account helpers; brand/account/status/version/shared/index/main-layout templates; tracked `servers/ruby/doc/index.md`; focused identity/navigation/shared-shell specs | Stable now. Exclude `shared_documentation_helpers.rb` from concurrent edits. Consume owner4's optional `controls[:switch_user]`; absent means hidden. Coordinate partial locals with3. |
| 1 | Search result/form Ruby helpers/partial and display fixtures/specs; one no-store header in `shared_documentation_helpers.rb` and existing neutral route assertions | Stable now. Send full-resource title/context fixtures to3. No schema/cache-service redesign or account-flow edits. |
| 3 | Existing documentation JS/CSS and focused asset/browser tests | Native account disclosure, menu dismissal/focus/touch, resource alignment, exact search presentation parity and responsive identity. No JS credential or sign-out implementation. |
| 4 | R1 module/spec fix, then the agreed Boolean/control/logout switch extension in `documentation_oauth.rb` and focused specs; `doc/documentation-oauth.md` technical contract | Separate source/hook window from0's shared server seam; capability disabled until partner configuration proves account selection. No local TLS/cluster work. |
| lead | Final visible wording/guide pass, formal grants, Git serialization and official partner coordination | Preserve ownership; no feature release implied. |

Partner session owns vpsAdmin integration and HTTPS devcluster deployment through
the official channel. Lead reports its public API origin as
`https://api.aitherdev.int.vpsfree.cz/v7.0/`, intent to pin all five HaveAPI source
siblings together, and retained deployed 0.31.2 rollback. Issuer/client/callback
configuration and dedicated-client SSO-off confirmation remain pending; no secret
or guessed endpoint belongs here. Our development source metadata is 0.31.0;
published patch ordering does not substitute for exact source selection.
Owner2 separately verifies the retained released Go transport and TypeScript
selection fixes in the source lineage. Keep TS SDK 0.1.1/runtime 0.30.2 pairing.
No HaveAPI release/publication, peer records/team/cluster access or unofficial
message fallback is authorized. Report HaveAPI defects here; peer owns its
dependency selection and deployment evidence.

Quick checks: configured/fallback/escaped/long API names without changed action
URLs; root and mounted index/internal overview hierarchy with all technical
destinations reachable once in the menu; one current-resource identity;
native/browser nested-resource display parity; literal placeholder plus label;
neutral success no-store; single-version root docs-cookie/explicit-auth/anonymous
identity and one authentication/describe call; multiversion isolation and hidden
account; OPTIONS/API cookie exclusion. Prove account details/actual username,
CSRF form retention, capability-off hiding, enabled switch order/new state,
malformed/disabled/foreign-origin/bad-CSRF refusal without effects, revocation
failure and R1 existing-session preservation. No credential-bearing screenshots
or request dumps. Main reviews wording before commits.

After committed-source review, run the new final UI acceptance at phone390,
tablet768/1024 and desktop1440: whole index and `/doc`, resource hierarchy/search,
keyboard/touch account/theme menus, focus/Escape, long names, no page-wide
overflow and existing local table/code scrolling. Retain previous cache results
for their exact source; the old responsive harness race was not a product failure
and its campaign is superseded rather than retried against old layout. Recheck
affected cache/auth behavior with the final source and retain ordinary GET
fallback. Existing compiler/wire/performance gates and frozen budgets remain.
Partner HTTPS acceptance additionally proves real login, actual account/subset,
sign-out and a change to a different user when capability is enabled. No local
preview activation or new dependency preparation is part of this design task.

This milestone adds optional display/configuration metadata and an opt-in docs
logout continuation; no database, API protocol, search-index or cookie migration.
Older consumers keep defaults; before rolling back to code without the optional
settings, remove those settings. Preserve development/deployed source proofs and
existing rollback. Integration still requires separate approval.

### Milestone 5 addition: copy client examples (owner3)

The user adds a copy icon in the corner of HTML client examples. Owner3 owns
this small JS/CSS/asset-test package; no shared-template seam is required.
Read-only template inspection and owner0 confirm the exact selector
`[data-example] > [data-example-panel] > pre > code`. Owner3 confirms it before
source writes. Limitation panels contain no code and get no button; protocol
and other guide code blocks are outside scope.

Create one native `button type="button"` per matching panel, with a decorative
copy icon, accessible name/title `Copy example`, and panel-local live status.
Place button/status as siblings of `pre`, never inside `code`; retain highlighter
ownership. The click copies that currently visible/open panel's exact
`code.textContent`, including whitespace, from the selected language/client/detail.
Never copy syntax HTML, summaries, controls, another hidden panel or trimmed text.
Do not execute/evaluate examples, send code over the network or store it.

Use `navigator.clipboard.writeText` on supported secure contexts, initiated by
the user gesture. For the HTTP preview without that API, a narrow native copy
fallback may use a temporary textarea and `document.execCommand('copy')` when
supported; success requires its true result. This command copies text only.
Remove the temporary element and restore focus, text/document selection and
scroll in all outcomes. If unavailable, denied or unsuccessful, announce
`Select the code and copy it.`; success announces `Copied`. Do not claim clipboard
success from merely selecting text. Preference state and navigation stay unchanged.

Keep the corner control reachable with keyboard and a useful touch target,
without covering code or causing page-wide overflow. Clear stale status when
appropriate; an asynchronous completion for an old panel must not announce a
different panel as copied. Focused asset tests cover secure-copy success/rejection,
native fallback success/failure, exact current-panel text and exclusion of guide/
limitation blocks, plus focus/selection/scroll preservation. Include a bounded
real HTTP preview copy check and secure-context browser check when the partner
HTTPS preview is available, without adding a clipboard framework or local TLS.

### Milestone 5 addition: renderer-owned example detail capability

The user requests the detail selector only for clients with distinct supported
levels. Add `ClientExample.detail_levels(*values)` as class-owned presentation
metadata. Supported declarations are `detail_levels :simple` and
`detail_levels :simple, :thorough`; reject other/duplicate/reversed declarations
and retain a frozen copy. The no-argument reader inherits the nearest superclass
declaration, falling back to frozen `[:simple, :thorough]`. This compatibility
default preserves existing custom renderers' two-level behavior until they
explicitly declare a single level; no output-equality heuristic can infer their
intent.

Owner1 confirms actual renderer facts: Http, Curl and RubyCli do not inspect
detail and produce one format. Declare `:simple` on Http (inherited by Curl) and
RubyCli. Other built-ins retain the existing pair. This does not change
`Context.detail`, positional/class render calls, code generation, panel IDs or
direct simple/thorough compatibility. Keep existing panel generation in this
small UI change; do not prune historical panels or expand performance fixtures.

Producer: owner0 adds `details: client.detail_levels.map(&:to_s)` to each existing
`documentation_client_metadata` record and `[data-detail-control]` to the Examples
label wrapper. No new central renderer registry. Owner1 owns the bounded base
method/declarations and focused metadata tests after lead grant;0 keeps its
existing helper/template ownership. The producer/consumer proposal was sent
directly to0/3 for confirmation; their other milestone5 work continues independently.

Consumer: owner3 reads that metadata. Missing `details` retains the old pair for
mixed/custom markup; malformed values use the safe simple-only UI without
discarding the renderer. Hide the wrapper and disable the select when there is
one supported level. Compute `effectiveDetail` from the saved preference when
supported, otherwise `simple`, and select the matching panel. Never overwrite
or persist a different `state.detail` merely because the selected client lacks
that level. Switching back to a capable client restores the reader's saved
thorough choice. Keep language/client/detail preferences distinct, existing
scroll capture/restore, deep-link handling and the current-panel copy rule.

Quick checks cover frozen/inherited/overridden declarations, undeclared custom
compatibility, Http/Curl/CLI single-level metadata, no registry duplication,
saved-thorough → single-level → capable-client restoration, hidden/disabled
control, effective simple panel, missing/malformed metadata and preserved
scroll/preferences. Real responsive acceptance includes this transition.
No server schema, auth, index-cache or persistence format change is introduced.

### Post-review verification reuse plan for final 35c1fb96

Static planning only, after the no-findings final review. Candidate is
`35c1fb964735639c0873aacf078e18569f05f9bc`, tree
`756b61de87833d8ded478b5d7785618671b4ddcb`; paired baseline remains
`f6e5c3750c747b33ec869c54ca220bf6f1d9d2d0`. The cached publication observation
at 2026-10-28 16:15:02 UTC is not a fresh CI result. Six runs were pending;
no additional query, download or execution was performed for this plan.
Do not repeat accepted 42/61/59, asset or exact-final 10-example packaging
checks merely because history changed. Existing final HTTP/browser evidence
has its own scope and remains separate from compiler and performance proof.

| Required contract | Existing current-head CI path | Remaining proof or local fallback |
| --- | --- | --- |
| Complete documentation/renderers/HTML and assets | `servers/ruby RSpec` run40723980063: shared Ruby3.2/3.3/3.4 jobs build JS declarations, `make doc`, then unrestricted server `bundle exec rspec`; `documentation-assets` runs all three Node scripts and highlighter check. Branch `release` run40723979876 also runs `make test`, containing the same server suite/assets plus generated-profile target. | Successful executed steps, actual spec discovery/counts and loaded current source/declarations. These cover `make test-documentation` without rerunning the same suite. If absent, use that existing target; use `make test-documentation-generated` only if its separate profile lane is not proved by release. |
| Real Python encoder checks | Branch release's `make test` invokes `make test-documentation-python`, including both `test_support/dynamic_*_spec.rb` files. | Require that exact supplemental target in logs; Python workflow run40723979835's unit/integration/package smokes alone do not cover it. Fallback: `make test-documentation-python` in the prepared locked environment. |
| Installed local npm plus Python wheel and sdist documentation snippets | No workflow/Makefile invokes `servers/ruby/spec/client_examples/dynamic_acceptance.rb`. Python CI's package smoke checks isolated installation/version/py.typed, not snippets. Release's npm smoke and Python smoke do not substitute. | Run the existing dynamic acceptance harness twice, once with the current-source wheel and once with sdist, using the same retained current-source npm tarball. Reuse verified release artifacts if available rather than rebuild them. The harness explicitly executes thorough panels for six dynamic variants; simple snippets have parsing/strict-TypeScript/serializer and all-client coverage, not a falsely claimed installed simple-program wire pass. |
| Generated Go/TypeScript documentation wire | Go run40723980008 runs component RSpec, not the standalone documentation acceptance. Release `make test-typescript` compiles simple/thorough snippets; its extracted-generator smoke uses published runtime0.30.2 with a mocked adapter, not the documentation wire listener. | Run `clients/go/spec/documentation_acceptance.rb` with its existing acceptance Gemfile, and `clients/typescript/spec/documentation/wire.rb` with the retained published0.30.2 bundle/types. Both exercise simple/thorough; TS covers root/mounted public/Basic/token and action/error/alias cases. `documentation_wire_check.rb` is a pure verifier regression, not the Go wire run. |
| Rust documentation development/MSRV | Rust run40723979663 and release `make test-rust` cover ordinary generator/runtime/integration; neither invokes `clients/rust/spec/documentation/run.rb`. | Run the existing documentation harness once with development1.99 and the independent1.95 compiler/Cargo. It runs both tools over the same generated lock, async/blocking, simple/thorough and root/mounted cases. Ordinary cargo success or a source package smoke cannot stand in for this. |
| Ordinary deterministic performance | Unrestricted server RSpec above includes `spec/performance`; release repeats it. | Require complete discovery/no excluded performance examples. Otherwise `make test-performance` in the ordinary server bundle, separate from the frozen measurement graph. |
| All clients, both details, both growth dimensions and exact paired quick | Performance run40723979715 first runs `make test-performance-clients`, then the selected pair via `utils/performance_ci.rb run` in the frozen benchmark shell. | Inspect retained `performance-40723979715-<attempt>` artifact. All-client log must prove all15, both details, isolation, +32 direct bounds and both resource/action2.5 scaling lanes. Pair selection must actually be f6→35c, quick/relevant, through the candidate neutral harness. If valid, no local duplicate campaign; otherwise use the already prepared `performance-35c1fb96/commands.md` for uncovered gates after diagnosis. |

Release is branch-build-only: the publish job requires a version-tag push.
Its build step executes `make release-deps`, `make release-test`, `make release`,
`make test`, npm smoke and Python package smoke. Inspect whether this step really
executed or artifacts were restored; artifact verification alone does not prove
test execution. Reused artifacts require the exact source-bound manifest and
hashes. Do not start a release/publish command just to obtain evidence. No new
workflow, acceptance runner or artifact registry is needed.

Existing local commands for the uncovered snippet packages (in their declared
prepared Nix environments, with absolute artifact/evidence paths supplied by
the owner):

- Dynamic: from `servers/ruby`, `bundle exec ruby
  spec/client_examples/dynamic_acceptance.rb --npm-artifact NPM_TARBALL
  --python-artifact WHEEL_OR_SDIST --typescript TSC --node-types NODE_TYPES
  --output NEW_EVIDENCE_DIR`, twice. See the existing dynamic acceptance guide.
- Go: from repository root, `BUNDLE_GEMFILE=clients/go/spec/documentation.Gemfile
  bundle exec ruby clients/go/spec/documentation_acceptance.rb` using the retained
  exact acceptance graph, not the root/server bundle.
- TS: from root, `HAVEAPI_TYPESCRIPT_RUNTIME=PUBLISHED_RUNTIME_JS bundle exec ruby
  clients/typescript/spec/documentation/wire.rb`. Verify runtime0.30.2 SHA256
  `96450c40a55ec7b7af4fca903d045bd0fc7ba1216efe12c3fee9b3e6a09e9198`, adjacent
  declarations and current compiler/generator/shared-schema identities.
- Rust: from root in the isolated Rust component environment, set
  `HAVEAPI_RUST_DOCUMENTATION=1`, `HAVEAPI_RUST_MSRV_CARGO`,
  `HAVEAPI_RUST_MSRV_RUSTC` and `HAVEAPI_RUST_DOCUMENTATION_EVIDENCE`, then
  `ruby clients/rust/spec/documentation/run.rb`. Reuse the prepared independent
  binary paths/manifest from `verification/generated-inputs/receipt.md`; clear
  inherited compiler overrides as the harness requires. That receipt's old local
  source version is historical; later0.31 input receipts and final-source binding
  establish current inputs.

CI reuse requires full run/head/attempt, executed command and exit/result, scoped
logs, tool versions, actual resolved locks/loaded source and relevant package
hashes. Root/server/Go/Rust/Python/JS graphs remain distinct. Do not describe a
CI graph as equal to the prepared local graph without its lock/input evidence;
accept it only for the contract it actually exercised. For cached Nix reuse,
retain the applicable derivation/input identity, not merely a green status.
Unknown actual CI locks, restored-artifact provenance, step completion and
coverage counts remain evidence tasks for the execution owners, not inferred
passes in this static plan.

The new-branch resolver uses zero `before` plus the captured default SHA's
merge-base, so f6 is expected but must be proved from `selection.json` and event.
Require source/archive/manifests, `dependency-compatibility.json`, retained
input hashes/locks, runner command/exit, all-client log and `results/report.json`
plus samples/worker identities. Preserve calibrated Ruby3.4.11, JSON2.21.2,
Bundler4.0.23, fixed reference and budget hashes. A green gate/exit0 can include
inconclusive timing; record that honestly, never as a measured pass or a reason
to retry automatically. Prepared35c exports are not executed measurements.

Proposed complete execution packages after owner3 releases utility capacity:
owner1 reconciles CI documentation/encoder/package coverage and runs only the
uncovered dynamic-artifact checks; owner2 owns generated Go/TS/Rust documentation
acceptance; owner0 reconciles deterministic/performance CI artifacts and runs
only uncovered required performance gates. Lead grants/serializes these packages
and retains real-provider coordination; no additional provider action is part
of this plan. Each long or uncertain package uses a fresh policy watcher.
Stop on a failure for diagnosis; preserve prior evidence and unchanged budgets,
dependencies and source. No app/Git/network/test/dependency/service/lifecycle
action was performed by this planning package.

## Milestone 6: OAuth-only reference identity and final navigation corrections

New explicit user feedback supersedes M5's literal `...`, hidden singleton
selectors, separate theme/account menus and explicit-API-credentials-first
documentation identity. Starting application evidence remains35c1fb96/tree756b;
266dcb1852c8bac8735af684ce48380d2851a658 is a subsequent test-only Ruby-version
portability correction. Prior completed browser/HTTP evidence is historical
evidence for that application, not proof of the new auth contract. No source,
test, Git, dependency, HTTP/browser or service operation accompanies this design.

### Presentation and routes (stable independent package)

- Search placeholder is exactly `Resource...`; retain the accessible version
  label, query bounds, ranking, index schema/fingerprint and native GET fallback.
- Keep Language, Client and Examples controls present. Client options contain
  only renderers of the selected language; Examples options contain only that
  renderer's declared `detail_levels`. Rebuild those options on selection.
  A one-option select remains enabled and visible. Keep existing missing/custom
  metadata defaults; malformed details still resolve to simple. Effective
  selection does not overwrite the saved preferred detail or other-language
  client choice. Thorough→HTTP/curl/CLI→capable-client restores thorough, with
  existing position preservation and exact current-panel copy behavior.
- Resource identity is the existing canonical dotted machine key, e.g.
  `vps.snapshot`. Use it in current-resource sidebar, resource-page heading/title
  and resource-directory links; no second redundant identity line. Breadcrumbs
  remain humanized parent links with their existing visual separator. Native
  and browser search retain full dotted primary resource titles; their optional
  secondary human-label hierarchy uses ` · `, not a competing slash path.
  Action/parameter context retains the dotted resource key. This is presentation
  only: do not change search projection, matching/ranking, URLs or anchor IDs.
- Remove exactly `The sidebar follows the action in view; breadcrumbs link to
  parent resources.` from the overview, without replacement. Main owns the
  remaining concise wording, including sign-in guidance conditional on actual
  docs OAuth availability.
- Register a GET/HEAD canonical redirect for each declared explicit version's
  slashless root, including mounted roots. Destination is the server-built
  slash URL plus the original query bytes, with Rack SCRIPT_NAME included once;
  use308, relative same-origin Location, and private/no-store. Guard the exact
  slashless PATH_INFO before redirecting because Sinatra may match optional
  trailing slashes. A slash URL must not loop. Reject literal header-control
  bytes rather than constructing an invalid Location. Do not redirect unknown
  versions, arbitrary action paths, OPTIONS or mutation methods, or introduce
  host/proxy-derived redirect targets.
- `/doc`, `/doc/index[.md]` and `/doc/readme` share the actual existing packaged
  README renderer. Source inspection confirms current `/doc/readme` reads
  `servers/ruby/README.md`; reuse that file/content/Markdown options, not a new
  introduction or a copied repository-root README. Preserve direct technical
  aliases, fenced blocks, tables, shared shell and private/no-store. The canonical
  internal landing breadcrumb is API versions→HaveAPI internals; the sidebar's
  HaveAPI internals heading links to `/doc`, with the duplicate HaveAPI/readme
  item removed. Other technical sidebar links remain. No neutral guide authenticates.

### One title-adjacent menu, unchanged sidebar width

Retained `browser/milestone5-final-35c1fb96-run2/versions-1440.png` confirms the
preview host wraps beside two controls. Keep the existing18.5rem/17rem sidebar
widths and1100/900px breakpoints. Replace both disclosures with one native
`details[data-documentation-menu]`, a single44px icon summary beside the title,
and one `[data-documentation-menu-content]` panel. Suggested accessible name is
`Documentation settings`, subject to main's final copy. No icon row below the
title, nested account/theme disclosure, hidden/truncated required host or wider
sidebar. A compact brand font/spacing adjustment within the freed one-icon
space is acceptable; arbitrary longer configured identities may wrap safely.

The panel directly contains the existing `[data-theme-choice]` buttons grouped
and labelled as theme choices (Light/Dark/Automatic, pressed state), followed
by conditional OAuth sign-in or actual escaped username and existing POST
Sign out/Switch user forms. Keep person/theme SVGs as useful inline imagery,
without a second trigger. Controls remain usable with keyboard, touch, Escape,
outside dismissal and focus return. Theme selection retains current persistence;
the single summary does not change its accessible name into a theme-only name.
Owner3 adapts the existing disclosure helper/positioning to the single selector
and content node, with no menu framework. No-JS account links/forms remain native;
unusable JS theme/preference controls retain their established no-JS fallback.
Neutral pages may offer an Account navigation link only when docs OAuth is
configured; they do not fetch identity. Without OAuth the menu contains themes
only. The visibility/status line stays outside the disclosure.

### Documentation authentication boundary (C core; D optional)

HTML GET/HEAD reference/index routes and their existing search-index
representations use one documentation-specific identity path. No configuration,
wrong origin, absent/invalid/expired/revoked cookie or unsupported-version OAuth
provider means anonymous documentation, never fallback to Basic, token headers,
Bearer headers, query credentials or a default/custom API authenticator. BasicA
plus valid docs-cookieB displays/filters/searches as B; BasicA plus invalid cookie
is anonymous. Ordinary API actions, OPTIONS and provider endpoints retain their
existing complete auth chain, conflict detection, challenges and credentials;
the documentation cookie never authenticates those routes. Basic/token/OAuth
provider descriptions and example code remain in the reference.

Core C owns `DocumentationHelpers#documentation_authenticated?(version)` as
the orchestration point: reset/set request `@current_user` from a small
`documentation_authenticate(version)` hook (default nil), run the existing
post-authenticated hook once for that attempt and resolve locale from that user.
It must not reuse an API-authenticated user or call `authenticated?` as fallback.
C supplies nil controls by default. Optional D overrides only the private
identity hook and controls producer. Single-version index reuses its one actual
docs identity in the existing describe map; multiversion index resolves docs
identity separately per declared version, describes once with that map and
continues hiding ambiguous account controls. No ordinary auth call is needed
when OAuth is absent. Selected/default-version search stays on this same path.

Use an explicit token-validation seam rather than temporarily replacing Rack
headers. Add `OAuth2::Provider#authenticate_access_token(request, token)` wrapping
the existing `config.find_user_by_access_token` and its AuthenticationError→nil
semantics; ordinary `authenticate(request)` retains all existing token extraction
and conflict rules before calling it. Add narrow
`Chain#authenticate_oauth2_token(version, request, token)` selecting only that
version's OAuth2 provider(s), preserving registration order/deny handling and
never falling through to Basic/token/other providers. Custom providers named
oauth2 need this explicit token-validation capability for docs sessions;
absence fails closed, without changing their ordinary API authentication.
The standard OAuth2.with_config provider used by vpsAdmin already owns the
callback being reused. No OAuth wire protocol, token storage or config flag is
added. The original request remains available to the provider callback for
request policy, but credential selection uses only the validated cookie token;
do not mutate its headers/params/caches or inject a cookie bearer into Rack env.

D's existing cookie decode, purpose/origin/expiry validation and token lookup
run on every network documentation request, including conditional search-index
requests. Successful validation alone sets CSRF/account/switch provenance;
invalid tokens clear the session with existing reauthorization messaging.
Logout/switch continue using the docs cookie, configured origin, strict scalar
switch capability and CSRF. Remove the explicit-credentials refusal from switch:
cached Basic is irrelevant to this docs-only operation. Preserve pending/state/
PKCE, R1 valid-session preservation on bad callbacks, clear/revoke ordering,
failure502 and no-refresh behavior. No cookie-format/key/lifetime changes.

Local source consumer search found `_login`/`_logout` and URL-userinfo logout
used only by the docs helper/template/JS; same-session vpsAdmin API/WebUI has no
matching route consumer. Preserve these GET URLs as compatibility redirects303
to the canonical default-version overview, without authentication, challenge,
cookie clearing/revocation or `back`/external redirects. Remove the docs Basic
XHR helper/listeners/tests and unsafe logout_url builder. Existing API Basic
challenges and OAuth provider authorize/token/revoke endpoints are untouched.
The account partial requires signed_in controls plus actual docs user; no
Basic sign-in/logout branch remains. All HTML/auth redirects remain no-store;
the existing exact-view private index-cache exception remains unchanged.

### Verification fixture compatibility and independent ownership

Existing role-filtering/search/all-client fixtures use Basic for HTML. Update
them to real docs-cookie authentication; do not keep a production Basic switch
or weaken role-isolation assertions. A small test-only fixture helper may mint
an encrypted cookie through the actual configured cookie writer outside the
request measurement, with deterministic fixture token/CSRF and a valid fixed
fixture lifetime. Each measured/requested page still decrypts, checks expiry/
purpose, invokes the actual OAuth provider lookup and performs authorization.
No cached user or mocked `documentation_authenticated?` in acceptance gates.
Keep CSRF stable per fixture role across repeated source samples so raw HTML
stability is meaningful; never normalize it out, omit controls or mint fresh
CSRF inside each page request. Synthetic secrets/cookies are fixture inputs only.

Neutral paired harness retains f6 as old baseline and the final M6 source as
candidate. In neutral setup, only documentation HTML scenarios on source that
supports the optional docs client receive a real configured docs OAuth fixture
and cookie; f6 retains its genuine Basic path. API/OPTIONS and direct renderer
lanes retain their old setup. Explicit fixture capability branching belongs
only in the neutral test harness, with identity/provenance recorded. Compare
the same requested role, fixture dimensions, endpoint and authorization counts;
per-page crypto/token-validation cost remains inside measurements. Candidate
response/account/provider presentation can differ under the existing per-source
stability policy. All-client candidate gates use real OAuth roles for both
details and both scaling dimensions. Frozen graph, calibrated runtime, budgets,
fixed reference, source/fixture integrity and failure rules remain unchanged.
An actual regression needs diagnosis, never a rewritten budget or removed work.

| Owner | Files/package | Dependencies |
| --- | --- | --- |
| 0 | Core `server.rb` routes/root map; `documentation_helpers.rb` C auth hook and identity; brand/account/sidebar/resource/usage/shared templates; focused route/identity/auth-filtering tests; subsequent existing performance fixture/harness/spec adaptation | Own all shared server/template writes. Agree hook with4 first; consume1's shared README helper. Menu DOM contract above releases3 independently. |
| 1 | `documentation_search.rb` and search form/fixtures; `shared_documentation_helpers.rb` README renderer; shared/packaging/search-route specs | Literal placeholder and native display parity; keep projection/index/key/rank unchanged. Reuse4's real-cookie fixture for authenticated search cases, never Basic fallback.0 wires README aliases in server.rb. |
| 3 | Existing documentation JS/CSS and asset tests | Visible supported-option selectors, single disclosure and browser search label parity; delete Basic XHR handling. Keep copy/navigation/scroll/cache code behavior. Confirm title fit and menus on phone/tablet/desktop after final-source refresh. |
| 4 | `documentation_oauth.rb`, `authentication/chain.rb`, `authentication/oauth2/provider.rb`, focused OAuth/chain/provider specs and small reusable fixture-cookie support; OAuth guide technical amendment | Direct token seam plus docs-only controls/logout/switch, standard API auth regression coverage. Coordinate hook/test support with0/1; no shared server/template edits or real provider deployment. |
| lead | Final prose, grants/serialization, affected final review, partner successor handoff and long-check scheduling | No broad remaining M5 gates/history folding before M6 source completion.0 performance follow-up may be separately sequenced after UI/auth sources settle. |

Quick checks before review: visible enabled singleton options and preference/
scroll restoration; exact placeholder and native/browser dotted-label fixtures;
README aliases/package extraction/no-store/no duplicate navigation; canonical
slash redirects at root, mounted and SCRIPT_NAME paths with byte-preserved query,
no loop/unknown-version/action/OPTIONS regression. Auth checks cross valid cookieB
with Basic/Bearer/custom/queryA, then absent/invalid/expired cookie; prove B or
anonymous, no fallback lookup/challenge, original request unchanged, ordinary
API/OPTIONS still A or their original conflict/error. Include different-version
cookie lookup, root map/no duplicate describe, keyed-index current/mismatch and
Set-Cookie cache behavior, logout/switch with cached Basic and wrong origin/CSRF,
R1 callback preservation. Run role/counter/stability fixture checks without
timing before affected review. Keep the Ruby3.2/3.3 validator-sidecar correction.

After all intended changes are committed and affected independent review passes,
apply the preceding CI-reuse plan to the exact successor, with new auth/runtime
and fixture identities: required documentation/Python/package/generated gates,
all-client/scaling and exact f6→successor paired campaign under normal watcher
policy. Browser acceptance at390/768/1024/1440 checks unchanged sidebar widths,
one title-adjacent trigger, untruncated `172.16.106.40:4567` and `api.vpsfree.cz`
on normal desktop, long-name safe wrapping, touch/keyboard/theme/account flow,
visible singleton selectors, scroll/copy, dotted paths and no page-wide overflow.
Real configured-provider acceptance remains peer-owned through lead; no live
configuration or private state is inferred here.

Compatibility: API wire/schema/client behavior and persisted OAuth cookies stay
compatible. Basic-only documentation consumers intentionally become anonymous;
they can retain authenticated machine descriptions through ordinary OPTIONS.
Legacy docs login/logout URLs no longer trigger browser credentials. Reverting
to M5 restores its old explicit-credential docs priority and UI, so rollback
reintroduces that superseded behavior; it requires no data migration. Preserve
source-selected sibling gems and partner rollback evidence; no release, default
integration or service activation is authorized by this amendment. There is no
remaining product ambiguity; final wording and implementation grants belong to lead.

### M6 publication: exact-pair correction to CI reuse

The planned replacement of remote35c1fb964735639c0873aacf078e18569f05f9bc with
reviewed a06b0cfa2abd7560f10cb58ebe99d8eb3f10b8f9 is an **existing-branch push**.
`utils/performance_ci.rb` selects nonzero event `before` literally: expected
baseline35c1fb96, candidatea06b0cfa, profilequick, reason
`push event before/after batch`, with the exact `push_pair` receipt. The shared
B260e3ea8 ancestor is not selected; neither is the default-branch merge-base f6.
The resolver and campaign explicitly allow this nonancestor quick push pair.
The earlier new-branch f6 expectation applies only to the original zero-before
publication and is superseded for this replacement.

Shortest completion: let the ordinary automatic push campaign retain its own
event contract. Once available, owner0 inspects actual event/selection, candidate
all-client log and input/runtime/harness artifacts. Reuse a successful exact-a06b
all-client/both-detail/both-scaling result instead of repeating it locally.
Then execute only the still-uncovered **f6→a06b quick pair** using the existing
native command in `performance-a06b0cfa/commands.md`, its prepared exports and
one final neutral harness, after the required all-client gate passes. The
automatic35c→a06b comparison is not duplicated locally. Do not dispatch an
additional hosted workflow, rewrite the event/selection, create a new branch,
cancel required current-head work or edit workflow/runtime/budgets to force f6.

An automatic green status alone proves neither selected endpoints nor a measured
pass. Actual `selection.json`, `push-event.json`, runner command and report must
agree; preserve pass versus inconclusive. Its35c→a06b result cannot satisfy the
required f6→a06b contract, and prior f6→35c evidence cannot be composed into that
measurement. If all-client execution fails or is absent, diagnose and run only
that uncovered existing gate before the local exact pair. No status query,
download, gate or other operational action was performed for this correction.

### Frozen worker activation correction after CI40745814060

Read the retained diagnosis/evidence/receipt in
`verification/postreview-performance-a06b0cfa-20261028/`. The failed baseline35c
pilot differs from the required calibrated graph only by absent activated
`io-console`0.9.4/platformruby. Availability/lock proof succeeds; PP lazily loads
`io/console` when action examples call `PP.width_for`, whereas overview HTML
omits those bodies. This is an activation dependency on page contents, not
evidence for changing the frozen runtime. The original calibration's precise
call order is unknown. Exit3 produced no paired samples or measured result.

Owner0's minimal correction belongs in `benchmarks/endpoints.rb`, in
`Worker#run` after runtime-policy setup and before source loading, fixture
construction, warmups or measurements: for the existing strict Boolean
`@request['benchmark'] == true`, activate `gem 'io-console', '= 0.9.4'` then
`require 'io/console'`. A small private bootstrap method is acceptable for a
focused test; no generalized dependency loader is needed. The real paired
CLI already sends `benchmark: true` to every baseline/candidate worker.
Use the same unconditional bootstrap for both source roles and profiles;
never branch on workload, source revision or presence of action examples.

Keep this out of the shared comparator's top-level requires: ordinary Ruby
3.2/3.3/3.4 test workers intentionally use their own component environments and
omit the frozen-benchmark flag. The correction must not require them to install
calibration-only0.9.4 or affect offline sample replay. Add no Gemfile/lock,
runtime/reference/budget or source-normalization change. Verify the explicit
pin against both existing calibration environment entries and the frozen lock.
Missing or already-conflicting activation must fail clearly, with no rescue,
replacement version, graph filtering or deletion of mismatched evidence.
`CLI#verify_runtime` availability and the subsequent exact full activated-graph
comparison remain unchanged.

Focused verification after the browser source hold is released: an isolated
bootstrap control proves exact0.9.4 is selected even if a newer spec is visible,
without invoking PP/action rendering; missing/conflicting versions fail and
ordinary unflagged workers retain their prior behavior. A bounded existing
worker control for each selected source runs one real overview request (no
pilot or paired campaign) and compares its complete observed environment to
the unchanged weekly calibration, while retaining correct role/counter/source
receipts. This checks the actual old/new loader paths, not a manufactured graph.
Check that every real CLI worker request carries the flag and bootstrap precedes
workload construction. Timings from such controls are diagnostic only.

The deliberate setup change moves exact native-library activation/loading out
of incidental first-render work for both sources. It does not remove PP calls,
OAuth decryption/provider lookup, authorization or any request work; counters,
measured loops, comparison policy and bounds stay intact. Record this in the
existing performance guide beside the frozen-runtime contract. Owner0 owns
only the runner, focused activation/worker specs and that small guide update;
ordinary amendment belongs in E, with C/D unchanged. No implementation before
owner3's browser hold is explicitly released. This is a narrow verification
correction, not a calibration migration or new review framework.

After source/quicks and the lead's normal final-input binding, run the required
direct f6→exact-final quick campaign once through the existing command/watcher
path. Retain actual complete worker graphs and unchanged budget/reference hashes.
CI all-client214/0 remains evidence for a06b and its recorded inputs; reuse for
the successor needs affected-input equivalence, not relabeling. The failed
automatic35c→a06b campaign remains failed; no retry is implied. This design
correction performed only local static reads and a design-document update.

## Milestone 7 — client examples and reference navigation

This is the next user-feedback milestone, based on published/browser-accepted
M6 `d67bebcb37f2d4558a97caa208465147da19dbef` (tree `cd91bf06…`). The exact
requests are retained in `milestone7-user-feedback.md`. Lead has released the
M6 installed-client source/utility hold: both npm+wheel and npm+sdist batches
passed on d67 with their actual 36 thorough panels/six variants and challenge
reruns. Those receipts retain that scope; they are not new M7 acceptance.
This brief permits lead to assign the independent packages below. It does not
authorize architect application edits or any deployment/release.

### Client facts, resulting behavior and ownership of sample data

* The TypeScript generator already emits typed resource properties and action
  functions through `createClient`, resource interfaces and `RequestResult`
  output types. `clients/typescript/lib/haveapi/typescript_client/documentation.rb`
  unnecessarily renders all access with brackets. Use `.name` for valid
  JavaScript identifier members and bracketed, correctly escaped literals for
  other members. Resource/action names come from the existing normalized IR;
  output fields retain their actual wire names. Thus `api.vps.create(...)` and
  `result.data.id` are natural, while `result.data["wire-name"]` remains correct.
  Apply the same member-access helper to single/list response output. Preserve
  existing naming, aliases, reserved-name checks, prototype-key handling,
  authorization/layout/type checks and emitted request semantics. This changes
  documentation rendering, not the generated public API or runtime.
* Remove the precise hardcoded runtime version from example comments. The
  renderer currently copies the compatibility-test version into a line that
  appears to describe the consumer's installation; no profile field proves it.
  Retain the configured package/import identity and its explicitly supplied
  package version where already useful. Do not introduce runtime metadata or a
  new version option to replace the removed literal. The independently pinned
  published `haveapi-client`0.30.2 package/hash remains the existing release and
  compatibility-test input. Its supported-version documentation remains factual;
  it must not be interpolated as a detected consumer runtime.
* Visible client wording is **API client**, never SDK or generated API client.
  Use Go API client/TypeScript API client where language distinguishes the
  choice. Preserve machine IDs (`typescript-generated` included), profile keys,
  package names, config APIs and pins. The typed TypeScript variant can say
  `API client`, alongside the existing callback/async variants; do not merge
  these different interfaces. Rust async/blocking remain distinct. Update
  visible limitation/comment/profile-label prose within the owned documentation
  paths; do not rename internal classes or perform a repository-wide API rename.
* Go recursively validates association examples against the associated resource's
  Show output. The retained VPS.Index example has `user.name`; User Show exposes
  `login` and `full_name`, not `name`. This is a consumer sample/schema mismatch,
  not evidence that VPS.Index is absent from the Go client. Extend the existing
  Go output-validation traversal with a response path (including list indices),
  so its missing-field limitation identifies `response[0].user.name` and says
  that the sample field is absent from the configured Go API client schema.
  Paths contain only names/indices present in the supplied visible sample;
  never print values, private model names, available-field lists or guessed
  replacements. Use dotted identifier segments and quoted bracket notation for
  other names. Existing HTML escaping handles the resulting plain-text reason.
  Preserve the rejection, all saved/live contract checks, input immutability
  and generic privacy-sensitive diagnostics; do not drop or rename fields.

The current isolated preview explicitly selects all five same-source path gems
and registers Go `github.com/vpsfreecz/vpsadmin-go-client/client`, Rust
`vpsadmin-client` and TypeScript `vpsadmin-typescript-client` before mount. With
no saved overrides these profiles derive structural models from that mount;
package names alone make no claim about an installed published client.

Official peer confirmation `1f9885cf-0428-460b-a0d7-7fe54b97ae14` establishes that
its VPS/User source has the same mismatch and that `login: 'somebody'` is the
intended sample, whereas `full_name` changes its meaning. Peer lead owns the
single-key vpsAdmin correction and a real mounted VPS.Index Go regression;
result is pending. No same-session vpsAdmin edit is assigned. HaveAPI's pathful
diagnostic remains useful independently. Final example acceptance needs the
peer's corrected sample/source receipt (and an explicitly selected corrected
consumer source for any later local preview); no renderer workaround substitutes
for it. Lead owns coordination and any subsequent preview refresh grant.

### Reference anchors and sidebar DOM

Owner0 derives sidebar links and heading targets from the same current `@help`
resource/action/provider descriptions already used by the body. No extra
describe, unfiltered model traversal, search-index field or persistent catalog.

1. Keep application resource/action IDs, provider `auth-NAME` IDs, parameter-row
   IDs and example-panel IDs stable. Add deterministic subsection targets for
   Input parameters, Output parameters, Examples and Child resources only where
   those sections exist. Input/output remain linkable even when their body says
   No parameters. Individual existing example titles also receive targets.
   A small `documentation_reference_anchor` helper owns new IDs: `reference-`
   plus the hex UTF-8 JSON encoding of a typed tuple containing provider (or
   null), resource path, action (or null), section kind and optional example
   index. This follows the existing parameter-anchor encoding, avoids delimiter
   collisions, and is shared by templates; JS never reconstructs IDs.
2. Authentication resource/action headings need provider-scoped canonical
   targets because legacy `root-PATH-ACTION` IDs omit provider identity. Use
   the new helper for their canonical heading/permalink/sidebar targets while
   retaining each old target as a compatibility anchor at its original heading
   location. Emit a repeated legacy alias only at its first document occurrence,
   preserving the old browser's first-match destination; new canonical targets
   are unique across providers. No search projection/key/rank or old anchor-map
   migration is needed: old search/deep links still reach their legacy targets.
   Existing app IDs and provider top-level IDs are not renamed.
3. On a resource page show its direct child resources in a separate Subresources
   list, linking their pages with full dotted identities. Descendants remain
   discoverable through their own pages and the full directory. Do not duplicate
   the complete resource tree or add a nested scrolling box.
4. In `[data-action-nav]`, each primary action/provider link gets
   `data-doc-primary`; its containing item gets `data-doc-nav-owner="TARGET_ID"`.
   Its nested list gets `data-doc-subnav="TARGET_ID"`; subsection links get
   `data-doc-subsection`. Targets are plain escaped native fragment hrefs.
   Application action submenus contain Input parameters, Output parameters and
   Examples when present. Authentication provider submenus expose its existing
   Resources group and resource/action headings with their existing parameter/
   example sections, plus the provider's authentication examples. Add an Examples
   heading for that existing panel group, not new instructional content. Do not
   manufacture empty Resources groups or unsupported provider operations.
5. Owner3 treats primary targets separately from subsection targets. Geometry
   selects the current primary action/provider; only that owner's submenu is
   expanded after JS enhancement. Subsection scrolling cannot accidentally
   select a different parent. Within the current owner, geometry selects the
   current subsection. Preserve `aria-current="location"` for the primary link
   and, in its nested set, the current subsection; no clicked-item lock or stale
   hash priority. Use the existing computed root padding/target scroll-margin
   threshold and one-pixel rounding tolerance. Recompute on scroll, resize,
   fragment navigation, pageshow and example preference changes. Defer hiding
   a submenu containing keyboard focus until focus leaves; do not move focus
   just because the document scrolls.
6. Render all applicable submenu links without `hidden` in server HTML. Without
   JS they remain accessible native navigation; automatic current-only expansion
   is the enhancement. New reference headings use native permalink anchors with
   an accessible `Link to …` name and unobtrusive visible affordance on hover,
   focus and touch. Reuse an existing target where it is already unambiguous;
   do not duplicate an ID on its heading and section. Cover overview/reference
   sections, resource/action/subsection/example headings and authentication
   headings, not arbitrary prose inside Markdown descriptions or neutral guides.
   Existing parameter row anchors remain intact. No new URL-copy control.

Owner0 also replaces only the sliders SVG in
`views/version_sidebar/brand.erb` with a conventional settings gear. Keep the
single native summary, `Documentation settings` accessible name, 44px target,
sidebar width, title fit, theme/account content and disclosure behavior.

### Copy containment and search shortcut

Owner3 creates a `.docs-code-block[data-example-code-block]` wrapper around each
existing direct `pre > code` found by
`[data-example] > [data-example-panel] > pre > code`. The wrapper contains the
unchanged `pre > code` plus the existing copy button and status as siblings.
The wrapper owns the continuous code background/border; its top-right button
is visually inside it. The pre owns horizontal code scrolling. Reserve interior
space for the 44px button/status without covering the first line, header or
wrapping failure message; the button stays visible when code scrolls sideways.
Remove the old outside-panel toolbar space. Do not wrap the details summary or
turn the whole example panel into the code block.

Update the local source lookup to the explicit wrapper path, preserving exact
`code.textContent` copying, current client/detail visibility checks, async-result
invalidation and lazy highlighting. No text node, button, status or line control
is inserted into `code`. Initialization is idempotent; unsupported/limitation
panels and protocol-guide code get no controls. Existing HTTP fallback, HTTPS
clipboard policy, honest status strings, selection/focus/scroll restoration and
no-storage/no-network behavior remain. No server template seam is needed.

Add one conventional document keydown handler for plain `/`: ignore prevented
events, composition, Ctrl/Meta/Alt, and editing targets (input, textarea, select
or contenteditable, including descendants). With an existing usable search form,
open the existing mobile/tablet navigation drawer through its normal path when
needed, then focus the search input and prevent the slash's default insertion.
Keep its query unchanged. If no usable input exists, do nothing. No modal,
shortcut framework, query persistence or new search request. Use the existing
drawer focus/close behavior and test composed/editor targets honestly.

### Independent implementation packages and verification

| Owner | Exclusive application paths and deliverable | Coordination/check boundary |
| --- | --- | --- |
| 0 | `documentation_helpers.rb`; `views/version_sidebar.erb`, sidebar nav/brand partials; `views/version_page.erb`, resource/auth/client-overview and related reference partials; `spec/documentation/navigation_spec.rb` and heading/HTML fixtures | New anchor helper, aliases, subresources, primary/subsection DOM, permalinks, gear and template wording. Publish an actual representative DOM fixture to3; no OAuth/server route/search changes. |
| 3 | `public/js/documentation.js`, `public/css/documentation.css` and existing asset tests | Consume0's metadata, current-owner/subsection tracking, copy wrapper, slash shortcut and responsive/focus styling. No template edits or invented ID catalog. |
| 2 | Go and TypeScript `lib/.../documentation.rb`; their focused documentation specs/compile fixtures and `servers/ruby/spec/client_examples/{go,ts_generated_client,typescript_profiles}_spec.rb` as affected | Typed dot access/fallback, remove runtime-version claim, Go path diagnostics; include API-client wording in these owned renderer files. Keep emitter/runtime/package/version contracts unchanged. |
| 1 | Server `client_examples/{go_client,rust_client,ts_generated_client}.rb`, `documentation_clients.rb` only where visible strings require it; Rust documentation renderer string changes and its affected unit expectations; server wrapper-label/presentation/overview specs; `doc/{client-examples,documentation-ui}.md` | API-client wording and typed-variant metadata, no config-key/API renaming; technical guide reconciliation. Do not edit0's templates or2's adapter specs. Main owns final visible prose. |
| lead / peer | Final wording, source-write grants and serialization, consumer sample correction/receipt, affected review, publication and separately granted preview refresh | No HaveAPI release or peer checkout/cluster access. Owner4 has no new auth package. |

Owners agree actual shared-spec boundaries before writes; a shared file stays
with its listed owner. No new registry, navigation framework, clipboard system,
runtime metadata field or benchmark harness. Quick checks before affected final
review cover valid/invalid TypeScript member names and preserved wire literals,
absence of an emitted hardcoded runtime claim, configured identity/version
truthfulness, Go top-level/list/nested missing paths and quoted/HTML-sensitive
names, no private-field/value leak and unchanged failure/snapshot ownership.
Use the existing strict TypeScript compile fixture for dot calls and nonidentifier
output access; classify compilation as a watcher batch if duration is uncertain.

Server/asset checks prove target uniqueness and deterministic IDs, compatibility
aliases including two providers with the same resource/action names, no hidden
resource leakage, empty-section rules, direct-child links and complete native
no-JS navigation. Exercise primary/subsection geometry on click/deep-link/up/down
scroll, keyboard focus, preference changes and provider transitions. Copy tests
prove wrapper containment, exact selected code, no duplicate buttons, no status
contamination and success/failure across existing clipboard paths. Slash tests
cover editor/composition/modifier exclusions, drawer opening and retained query.
Run appropriate scoped Ruby/Node checks and lint; do not repeat unrelated auth
or completed package checks merely because history later changes.

After intended source is committed and affected independent review passes, finish
the still-required final documentation/assets/Python, generated Go/TypeScript
compile+wire and published TypeScript runtime0.30.2, Rust development/MSRV1.95,
ordinary deterministic performance, all-client/both-detail/both-scaling and
exact `f6e5c3750c747b33ec869c54ca220bf6f1d9d2d0`→final quick paired gates using
the existing commands and watcher policy. Actual final CI artifacts can satisfy
their exact covered contracts; status alone cannot. Preserve frozen runtime,
locks, budgets, fixed reference, worker activation and fixture authorization
work. New anchors/sidebar increase HTML work and must meet the unchanged gates.
Retain d67 installed-dynamic success with its input receipts; reuse for M7 only
after comparing the affected snippet/renderer/package inputs, never by SHA
relabeling or by treating thorough-only execution as both-detail execution.

Final browser acceptance at390/768/1024/1440 checks nested action/provider
navigation and deep links, subresources, gear/title fit, no widened sidebar or
page-wide overflow, touch/keyboard permalinks, inside-block copy with long code
and wrapping status, and slash focus with closed mobile navigation. Check both
themes and retained language/detail preferences. Useful VPS.Index Go rendering
requires the peer's corrected consumer sample; an old fixture's honest pathful
limitation is not that acceptance.

Compatibility/recovery: no wire/schema/profile/cookie/search-cache format,
authentication/authorization, database, generated public API or dependency pin
changes. Native links and old parameter/example targets survive; ambiguous old
auth aliases preserve their first target while new links are provider-specific.
Reverting HaveAPI restores old wording/navigation/rendering without data migration;
the corrected consumer sample is independently valid with either version.
Deployment ordering is only the existing explicit same-source sibling selection
plus a separately selected consumer source for preview; no publication, service
activation, configuration change or lifecycle action follows from this design.

### M7 follow-up — meaningful detail choices, after the 15-client audit

The user explicitly retains the M6 control behavior: **Examples stays visible
and enabled; offer only meaningful choices, including a single Simple option**.
Do not add error boilerplate to manufacture a difference. This supersedes the
old assumption that a renderer-wide two-value declaration is sufficient for
every page and example kind.

A bounded in-process audit rendered all15 registered clients through the existing
`AllClientPerformanceFixture.build(resources: 2)`, actual mounted Go/Rust/TS
profiles and init/basic/token/oauth2/public/protected/failure lanes at both
details:210 renders, Ruby3.4.11,1.24s render phase, exit0, original description
unchanged. It ran on d67 in the existing prepared
`nix-shell servers/ruby/benchmarks/shell.nix`, using all five source library paths;
no compiler, dependency preparation, performance campaign or application edit.
The semantic classification also reads each renderer's actual branches, rather
than inferring usefulness from differing bytes:

| Clients | Initialization and provider examples | Action examples; advertised result |
| --- | --- | --- |
| Ruby, PHP | Exact simple/thorough duplicates | Thorough only prepends initialization. Simple only for every kind; retain direct thorough calls for compatibility. |
| CLI, curl, HTTP | Exact duplicates | Exact duplicates; retain existing Simple-only capability. |
| JS callback, TS callback | Different bytes, but only a success log and a try/catch around that log; discovery/authentication failure handling is already identical. Simple only. | Both: thorough handles synchronous lookup/invocation failures and includes setup/authentication and response metadata. Ordinary reply-error checks remain in Simple. |
| JS async, TS async | Both: thorough catches actual awaited discovery/authentication failures and exposes AsyncError diagnostics. | Both: real awaited-action failure handling and metadata, beyond repeated setup. |
| Python sync, Python async | Both: thorough catches actual client/context-manager/discovery/authentication exceptions. | Both: ActionError/HaveAPIError handling around the actual operation. |
| Go API client | Exact duplicates; Simple only. | Ordinary success/protected/failure lanes differ only by full-program setup or metadata comments; Simple already checks transport and API errors. Both only for a successful blocking sample for which the existing `operation_visible?` permits the real operation-status call and its error branches. Otherwise Simple only. |
| Rust async, Rust blocking | Exact duplicates; Simple only. | Successful samples retain the same `?` propagation and output handling; setup/metadata alone is not a second error-handling mode. Simple only. Failed samples (status false or HTTP status >=400) can offer both: thorough additionally demonstrates explicit server-message/validation-error inspection, preserving its sensitive-diagnostics caution. |
| TypeScript API client | Exact duplicates; Simple only. OAuth2 is the same limitation at both details. | Both: successful samples add AsyncError catching and guarded output inspection; failed samples add explicit error/envelope/response diagnostic access. |

All applicable built-in limitation results have one Simple panel, regardless of
the usual capability for that kind. Unsupported OAuth text in Ruby/CLI is also
single. These rules concern the presented alternatives: keep mandatory error
checks, authentication validation, operation-completion warnings and wire
handling in Simple. Do not edit existing emitted programs just to create a
difference, or silently replace a known useful full error path with a fragment.

#### Producer interface and compatibility

Owner1 adds the class-owned query
`detail_levels_for(kind, context:, result:, auth_method: nil, auth_description: nil)`
to `HaveAPI::ClientExample`. `result` is the already-rendered **Simple** result.
It returns a frozen `[:simple]` or `[:simple, :thorough]`, with the same strict
validation as the existing `detail_levels` reader/declaration. The base default
returns the existing class declaration unchanged, ignoring the new context;
third-party/custom renderers therefore retain their old two-level default and
any explicit global declaration. No capability probing or client-ID catalog.
Legacy positional calls, direct `.render` at either Context detail, Context's
immutable contract and direct `documentation_panels(..., detail:)` behavior
remain supported even when the UI advertises only Simple.

Built-in families own the semantic overrides in the table. Shared static
behavior can use ordinary inherited class methods; no new registration DSL is
needed. Dynamic callback/async classes and Ruby/PHP declare their own behavior.
Generated wrappers delegate relevant decisions to their owned adapter via
`detail_levels_for(kind:, context:, result:, mode:, auth_method: nil,
auth_description: nil)`. Go uses the same existing operation-visibility predicate
as its renderer, after successful Simple validation, without rendering again or
walking unrelated resources. Rust uses its existing failed-sample predicate;
TypeScript uses kind and the validated result. Built-in overrides return Simple
for limitations. Custom base behavior does not assume a Simple limitation means
the custom thorough result is identical; its explicit declaration stays the
authority. Return nil/invalid values is an implementation error, not a fallback.

Owner0 adds one HTML orchestration helper,
`documentation_example_variants(kind, auth_method: nil, auth_description: nil, **changes)`,
returning `[client, detail, result]` triples for the current example group. For
each available client it derives the owned Simple context and renders once;
nil retains the existing absent-result behavior. It asks the class query with
that result, and renders thorough only when declared. It emits each supported
result once and records the declared levels in request-local group metadata.
No output-equality comparison, render-both probe, global cache or new description
walk. Retain the existing request-local resource Context sharing.

The example wrapper carries `data-example-details`, JSON mapping actual client
IDs in that group to its supported level strings. This map and its panels come
from the same helper result, not independently maintained logic. Missing result
has no map entry; a limitation has Simple for built-ins. While rendering the
body, collect each client's ordered union of these declared values for this
page. `documentation_client_metadata[:details]` publishes that page union;
available clients with no example group on the page get `['simple']`. The
existing render order already builds `@content` before sidebar and layout JSON,
so no second render or speculative page prepass is required. Do not memoize
client metadata before body completion. Page/group metadata contains only the
current authorized description's rendered groups.

Owner3 populates the visible, enabled Examples selector from the page union.
Keep saved preferred `state.detail` separate from effective page detail: choosing
a singleton page/client never overwrites a saved thorough preference. For each
example group, use its declared supported levels: requested thorough selects
thorough only there; otherwise use that group's Simple panel. A mixed auth page
may therefore offer both because an auth-resource action supports both while
provider-initialization groups stay Simple. Do not relabel Simple code as With
error handling or emit a hidden duplicate to make switching work. Do not infer
capability from byte equality, panel counts or hardcoded client names. Preserve
the explicit unavailable-client message and existing scroll/focus/copy/highlight
behavior. A page with no examples still has its existing enabled singleton
selector; this does not create new controls on neutral pages.

#### Packages and checks added to M7

* **1:** owns `client_example.rb`, built-in server class capability overrides,
  their focused detail/presentation tests, and the Rust adapter's capability
  implementation/tests in addition to its already assigned string changes.
* **2:** owns Go and TypeScript adapter queries/tests in its existing renderer
  package. Coordinate the exact signature with1; do not edit1's wrapper files.
* **0:** owns `server.rb` HTML orchestration, helper/page metadata and
  `example_panels.erb`, HTML tests and the existing all-client/neutral-harness
  panel assertions. Keep full direct all15×7×both-details coverage. HTML checks
  must require exactly each declared meaningful panel, while singleton groups
  are represented once; remove only obsolete duplicate-count expectations.
  Preserve every role/resource/action sample, both scaling dimensions, budgets,
  runtime, source integrity and exact-pair policy. No gate waiver.
* **3:** owns the page/group metadata consumer and visible singleton/mixed-group
  behavior in existing JS/asset tests; no independent capabilities table.

Quick tests pin representative semantic reasons, not merely code inequality:
Go ordinary/failure versus eligible/ineligible blocking status helpers; Rust
success versus failed diagnostics; callback setup versus action invocation;
async/Python actual catches; typed TypeScript init/auth versus action catches;
Ruby/PHP setup-only differences. Include a custom renderer with unchanged global
defaults and a Simple limitation with distinct thorough output. Check each
group is rendered at most once per advertised detail, no duplicate singleton
panel, metadata/panel consistency and no profile or description mutation.
Browser/assets cover saved thorough → Simple-only overview → meaningful action
page, mixed provider/action auth groups, language/client changes, no-example
directory, visible enabled singleton controls and scroll continuity. Existing
15-client fixture provides the complete correctness matrix; no new runner or
long campaign is introduced for this audit. Final affected review and the
previously required final long gates still apply after implementation.

### M7 small navigation corrections

Owner0 removes only the duplicate main-content API search form on Resources.
Keep the sidebar form, current query, normal GET results and existing projection,
key, ranking and permission behavior. No replacement copy or new search route.

Authentication resources can also collide in their legacy example-panel IDs.
Use the same `documentation_reference_anchor` tuple/encoding already specified,
with section kind `example` and sample index, as the provider-scoped **baseid**
passed by `resource_body.erb` to `example_panels.erb` for auth resources. Application
baseids stay unchanged. `example_panels.erb` retains its existing suffix contract
(`-examples`, `-CLIENT`, `-CLIENT-thorough`) on this canonical base. Forward the
old base separately as `legacy_baseid` for native compatibility aliases, emitted
only at the first original occurrence through0's same alias helper. For a now
singleton panel, its old thorough target aliases the Simple panel location;
there is no duplicate code panel. Apply this removed-thorough alias rule also
to ordinary application and initialization groups using their unchanged baseid
when no separate legacy_baseid exists. Canonical example heading/permalink targets
and rendered panels remain distinct IDs; do not assign the base to two elements.
Provider initialization groups already have unique `auth-PROVIDER` bases and
keep them. No parallel encoding, application-ID rename, search migration or
direct renderer API change. Owner3 selects panels by the declared metadata and
data attributes, not an ID construction rule. Owner0's all-ID uniqueness test
covers two providers with matching resource/action/example names, canonical
headings/groups/panels and every retained legacy alias. Test old native links
and current copy/detail controls on that fixture.

### M7 compatibility correction — older profile adapters

Static source inspection confirms a supported external boundary, not merely
test duck typing. `Profiles#profile` requires only `resolve` and `render`.
`generator_version` is checked against the loaded generator's version, not
forced to the server's version when explicitly configured. Existing specs
accept a pinned older Go adapter and preserve Rust's saved snapshot+TOML
constructor without the new automatic/inline factories. The guide explicitly
promises those legacy file profiles and adapters that ignore additive Context
detail. TypeScript retains its existing factory requirements; this correction
does not relax them. Saved files alone are not evidence that an arbitrary older
generator is compatible: all current version/schema/factory checks still apply.

The unconditional new adapter capability call would break these supported
paths. Owner1 therefore adds **one shared class helper** on `ClientExample`,
`adapter_detail_levels_for(adapter:, kind:, context:, result:, mode:,
auth_method: nil, auth_description: nil)`, used by all three generated wrappers.
It checks this external adapter's `respond_to?(:detail_levels_for)` once per
query. If present, delegate the exact keywords and validate its returned levels
with the existing strict validator. If absent, return the wrapper's existing
inherited `detail_levels` declaration. Do not wrap/replace the adapter, mutate
Profile, inspect generator version numbers, rerender, compare source strings,
walk descriptions, or duplicate this probe in each wrapper. This small shared
capability probe is justified by the actual older-generator contract; it is
not a general permissive duck-type fallback for owned interfaces.

Remove the generated wrappers' pre-delegation Simple-limitation shortcut:
the **current** Go/Rust/TypeScript adapters already declare Simple for limitations.
An older/custom adapter may return a Simple limitation and a useful thorough
result; its unknown semantics must keep the inherited global declaration.
Do not rescue a modern query's exceptions or invalid return as legacy behavior.
Direct render/context APIs, profile.adapter identity/freeze, old profile settings
and all factory/startup failures remain unchanged. Current same-source adapters
continue applying the audited M7 semantics. A legacy adapter lacking the query
can still present both levels, even if identical; document this explicit
compatibility limit instead of claiming that unknown third-party output has been
semantically audited. Its author can implement the optional query or its custom
renderer can declare one level. No new user configuration is added.

Owner1 owns the helper, three wrapper call-site changes, focused wrapper/profile
regressions and guide correction. Keep the existing older-generator registration
tests; extend one accepted saved-profile path through actual wrapper capability
selection and HTML/panel production as practical with owner0. Test a render/resolve
adapter without the query, preserved direct output and identity, both inherited
defaults, a Simple limitation with distinct thorough output, and an explicit
single-level wrapper declaration. Test modern delegation including limitation
results, exact modes/auth keywords, strict invalid-return/exception propagation,
no extra render/resolve calls and unchanged current built-in semantic cases.
No need install an old gem or add a dependency graph to prove this interface.
Owner0 coordinates only any shared HTML assertion. The material guide change
requires refreshing its packaged copy again before final packaging checks;
the earlier `make doc` receipt remains valid for its earlier input. No broad
tests or application edits were performed for this design correction.

### M7 final history partition

Reconstruct five coherent commits on exact base
`f6e5c3750c747b33ec869c54ca220bf6f1d9d2d0`, after all four serial M7 source
commits finish and their accepted final tree is frozen. This is consolidation,
not another source change. Original A4363d111/B260e3ea8 contain the renderer and
adapter work; C222812c0/D07c0d0a6/Ed67 contain UI, optional OAuth and performance.
M7 genuinely changes A/B logic, so the earlier requirement to retain A/B SHAs
does not apply. Do not retain four superseded M7 fixup commits merely because
the branch was published. Preserve their source/quicks/provenance in the existing
handoff receipts and recovery refs.

| Final group | Coherent final ownership | Intermediate boundary |
| --- | --- | --- |
| A — renderer contracts and dynamic examples | Original A paths plus final `client_example.rb`, all server renderer wrappers/metadata/capability policies, Context, dynamic snippets/harness and core detail/presentation specs. Fold the old C global detail declarations for HTTP/CLI into A with the new query/legacy-adapter fallback. | Base generator adapters may lack the query; the accepted shared fallback makes A work with them. Core specs use owned contracts and explicit external-adapter fixtures. Keep original A's complete `doc/client-examples.md` snapshot until C restores the revised guide; no dangling UI/OAuth link or half-guide deletion. |
| B — Go/Rust/TypeScript documentation adapters | Original B component paths with final M7 adapter semantics, pathful diagnostics, typed property access, truthful comments, component docs and compile/wire fixtures. Place final server `client_examples/{go,ts_generated_client,typescript_profiles,rust_client}_spec.rb` integration expectations here. | Modern-query expectations belong with these adapters, even though their wrappers were introduced in A. At A those existing spec paths keep the appropriate preceding passing version; B restores their final complete bytes. No production API/query implementation is deferred to a test-only commit. |
| C — complete HTML reference | Final navigation/helper/templates/assets, meaningful panel producer and page/group metadata, search/permalinks/subresources/copy/shortcut/menu, shared guides/README and UI tests. Restore final `doc/client-examples.md` except D's optional-OAuth pointer; introduce final `doc/documentation-ui.md` with its anonymous-core projection. | Optional OAuth module, config/accessor, require/helper registration/mount and real-cookie fixture remain absent. Core identity hook and controls default to nil; Basic credentials do not authenticate HTML. Retain the full C UI and current M7 panel logic when projecting only the optional seams and E cache. |
| D — complete optional OAuth | Existing D production module, Chain/Provider token validation, four server seams, actual-cookie helper/tests, optional guide and guide pointers. | M7 changes no OAuth behavior. Preserve D-owned source bytes; reapply its narrow seams to new C context with exact owner-approved projections. Auth-dependent sections of mixed UI specs arrive here, not as broken C tests. |
| E — performance contracts | Existing E runtime/bootstrap/neutral fixture/provenance work and final M7 declared-panel HTML assertions in endpoints/all-client specs; final request-local resource Context cache and performance guide/specs. | Preserve all15 direct renderers×7lanes×both details, all roles/resources/samples, both scaling dimensions, +32/2.5 limits, frozen graph/runtime/reference/budgets and old-f6/new-candidate authorization work. C/D retain the known pre-cache Context derivation; E restores only that exact optimization. |

Minimal projection requests, assigned by lead:

* Owner1 supplies A's final owned core path list, keeps the original A complete
  client-examples guide snapshot, and identifies any single modern-adapter test
  block needing B. Prefer placing the four integration-spec files wholly in B
  over scattering dependent expectations or disabling tests. Current core detail
  and presentation specs use dynamic clients/mock adapters and belong in A.
  No wholesale reversion of final renderer files to original A.
* Owner0 supplies final-source C/D/E snapshots only for genuinely mixed files:
  server.rb, mixed auth/UI specs (including new M7 heading/variant specs if their
  setup uses the real-cookie helper), and guide projections coordinated with
  main. Reuse the M6 seam inventory, but derive replacements from the accepted
  M7 tree; old artifact bytes are historical inputs, not a substitute for new
  templates. Anonymous C keeps applicable M7 assertions with native core fixture
  setup; cookie-only cases are deferred intact to D. A wholly cookie-dependent
  test file can first appear in D. Keep the stale Basic HTML performance spec
  absent through C/D; E introduces its complete replacement. Main approves the
  two guide projections and restores final guide bytes in D.
* Owner2 owns serialized reconstruction with ordinary hooks after collective
  source/Git quiet, using these small owner projections and the original path
  inventories. Owner3's complete assets belong in C; no asset projection is
  needed. The final accepted full tree and aggregate f6→final patch must match
  byte-for-byte before moving the feature ref. Differences are errors to resolve
  with the owning implementer, not history-time product edits.

Run the existing bounded C/D runtime smoke once on each actual reconstructed
commit because the templates/panel producer changed. Bind loaded paths to that
commit: four mounted HTML routes (root, overview, resource, authentication), C
anonymous/full despite Basic with no optional module or cookie lookup; D real
member cookie plus Basic admin yields member, missing/invalid cookie yields
anonymous, and per-request token validation occurs. API GET/OPTIONS retain Basic
admin and cookie-only API remains unauthorized. Preserve counters/native controls
and current panel/alias metadata. Setup and synthetic cookie issuance remain
outside requests. Prior M6 smoke proves its old snapshots only, not these new
trees. Reuse unchanged module and prior focused source checks only with explicit
affected-input equivalence. Full final packaging follows the restored guide
inputs; long gates remain after affected independent final review.

Exact externally selected M6
`d67bebcb37f2d4558a97caa208465147da19dbef` must remain reachable through the
existing local and remote recovery contract. Peer reported its c342 local
Bundler/bundix graph pins all five siblings to d67; deployment was not reported.
Retaining that exact ref supports the consumer without retaining d67 as an
ancestor in the new feature series. Lead later publishes the successor with
the existing exact-old lease/recovery procedure and coordinates a deliberate
peer input refresh; reconstruction itself does not switch consumer pins or
authorize publication/deployment. Never call nonancestor d67 literally merged
or deployed, nor call the changed M7 tree source-equivalent to M6. Equality is
between accepted pre-consolidation M7 final and reconstructed M7 final.

The independent reviewer receives the complete f6→A/B/C/D/E history, final diff,
old/new range mapping, owner projections, d67 consumer/ref evidence and all scoped
quick receipts. Require explicit whole-history/obsolete-approach and migration
conclusions. Expected inventory remains no migrations and no feature dependency,
version or channel-pin update stream; verify against the actual final range.
Retain all original receipts and recovery refs. No additional framework, generic
manifest subsystem, broad intermediate campaign or lifecycle action is needed.

### M7 acceptance follow-through — installed dynamic HTML extraction

Static inspection finds a concrete remaining interface break in
`servers/ruby/spec/client_examples/dynamic_acceptance.rb`: `extract` filters
every panel to `data-detail=thorough`, and the installed runner requires init
and Basic panel presence for every variant. It would fail for callback JS/TS,
whose init and three provider groups now have only Simple. Merely relaxing the
coverage count would silently omit these lanes. Merely selecting Simple is also
insufficient: their valid setup/auth code omits the success-only stdout messages
that the runner currently requires, including its separate token-challenge run.
No tests or installed execution were run to reach this finding.

Owner1 adapts this existing harness/spec/guide and its existing
`test_support/dynamic_documentation_api.rb` fixture after serial hooks finish:

* Extract by actual `[data-example]` group and decode its escaped
  `data-example-details` map. For each expected variant choose requested
  `:thorough` if declared, otherwise declared `:simple`, exactly as the UI does.
  Select exactly one matching real `details[data-example-panel]` and its code;
  native legacy alias spans are never panels. Record group, variant, requested
  detail and effective detail with the actual source/id. Missing/malformed map,
  unknown levels, duplicate selected panels, unexpected limitation or missing
  code in this supported fixture fail explicitly; do not skip a lane or infer
  capability from ID suffixes. Keep parsing bounded to the existing emitted HTML
  shape using available tools, with no new dependency/DOM framework.
* Pin the fixture's complete matrix: six variants, each with init, Basic,
  token, OAuth2, successful action and failed action. Requested thorough yields
  **36 executed panels:8 effective Simple and28 thorough**, plus all six separate
  token-challenge reruns. The eight Simple panels are callback JS/TS setup and
  provider examples; action programs remain thorough. Check identities/kinds,
  not only an overall count. Selecting requested Simple for extractor tests
  remains valid; overlap with thorough-request selection is now expected for
  singleton groups. Do not execute uncomposed Simple action fragments or claim
  complete-program acceptance of all Simple action variants.
* Preserve the source exactly as extracted. Do not append success prints,
  rewrite programs, duplicate HTML panels or add probes to application clients.
  Prove callback setup/auth completion using the fixture's actual network/auth
  result instead of an absent presentation message. Extend the existing fixture
  receipt endpoint with separate action and event collections, e.g.
  `{actions: [...], events: [...]}`; its internal action receipt array and exact
  request-value assertions remain. Record only bounded method/path/status,
  provider name, authenticated Boolean and token request/verification completion
  events from the existing fixture provider/handlers/RequestTrace. Never record
  headers, queries, credentials, tokens, challenge values or extra request bodies.
  This is test-only instrumentation in the already existing mounted fixture,
  not a production route, authentication shortcut or new harness.
* Snapshot receipts separately before/after each snippet **and** challenge rerun.
  Init requires successful mounted/versioned OPTIONS discovery; Basic/token/
  OAuth require successful actual provider authentication and discovery, and
  token challenge requires the request→verification→authenticated-completion
  sequence. A200anonymous OPTIONS alone is insufficient. A process failure,
  auth failure/failed callback message or missing required receipt fails even
  if another run previously succeeded. Keep existing stdout markers where the
  selected code emits them; callback Simple uses the stronger actual receipts.
  Action success/failure still require exactly one action receipt, preserved
  path/input values and DOC_SUCCESS/DOC_FAILURE output. Do not weaken installed
  import isolation, compiler settings, mounted-path/HTTP/provider contracts or
  per-run output retention.

Focused quick specs render the actual current HTML and assert the36-entry
requested/effective matrix, both action samples and all provider/init lanes;
malformed/missing/duplicate declarations fail. Exercise fixture receipts for
valid and rejected credentials, anonymous discovery versus authenticated
discovery, completed versus incomplete challenge, clean logs and independent
snapshot deltas. Keep subprocess nonzero/output retention tests. No installed
package batch is needed before affected review; the required final npm+wheel
and npm+sdist runs later execute this unchanged-size complete matrix. The result
receipt records requested/effective details and challenge counts honestly. M6's
d67 36-thorough batches retain their actual old scope; they do not prove this new
selection/instrumentation behavior.

Go's `documentation_acceptance.rb`, TypeScript's `spec/documentation/{wire,
compilation}.rb` and Rust's `spec/documentation/run.rb` call adapters/wrappers
directly with Context details. They retain both-level loops and explicit
Simple-fragment composition; none extracts missing HTML Thorough panels.
No adaptation or coverage reduction is indicated in those helpers. Likewise
preserve the all15×7×both direct-render gate and existing compiler/wire/runtime
pins. This correction applies only to the installed dynamic HTML consumer.

History consequence: final dynamic acceptance harness/spec/fixture/guide changes
belong in **C**, with the HTML metadata they consume. A retains its existing
complete legacy extractor/spec/guide snapshot, as it has no page/group producer
yet; C restores their final bytes. Owner1 supplies that tiny path disposition to
owner2. This is a necessary verification dependency of M7, not new product scope.

### Final24ec verification environment — exact output restoration

Reviewed final application authority remains
`24ec424c9592951da38584379b43379b0c39f115` / tree
`288376a727deb3905d2c368150543a6d7cfc0971`. Read the existing generated24ec
preflight/static-inputs and installed-dynamic24ec receipt/input proof, retained
d67 installed success and declared-shell derivation metadata. This bounded
diagnosis changes no source, test, lock, package selection or verification gate.

All four reported missing outputs are still absent locally. Their exact
identities appear in the retained root `haveapi-env` derivation inputs from
locked nixpkgs `3ec636362e1816bc2f0888fa0fa2c69f1bc9e504`. The full shell is
unnecessary for these gates and would pull unrelated PHP and install hooks.
Do not realize it or substitute another same-version Cargo/rustfmt directory.

Read-only queries to the currently configured caches found **all four exact
outputs at cache.nixos.org**, HTTP200 narinfo, matching StorePath and Deriver,
with cache.nixos.org-1 signatures advertised. cache.vpsadminos.org returned404;
cache.numtide.com returned403. No trust/configuration change is needed.

| Exact output under `/nix/store/` | Retained/advertised derivation basename | Advertised NAR SHA256 |
| --- | --- | --- |
| `fkz7zn1a0yiryf9kri2yh1s12k1sv557-go-1.26.10` | `mxqlh07a9kdcabldzlwwrpacvf4qnnzq-go-1.26.10.drv` | `TFzcmMB2/qWIp6RZmgoKHEqmLMA1TY0A8tIVh7US6w0=` |
| `l3jrya2cdjmzxgdpnxzwvx3h416lcbr6-cargo-1.99.0` | `45ial5wyx19y9hbfz1asqbzyx1vq4gdz-cargo-1.99.0.drv` | `xeAl+jN8MZRUIkWQKKLAuU/ER3xOoo5WKHVJZi7pvxg=` |
| `vwgbz9vm1gyxqn6z4fg1jd6va2nzfa3m-rustfmt-1.99.0` | `s4cslhsi7814q0a8ph8pk9z64i5sigjz-rustfmt-1.99.0.drv` | `M7Xd9Ib6to0rJTCz9NU6GBr29emGo0UnNVPPfz0RNu0=` |
| `lgrjxh2j5dqvdifh2lhrj2w0c0g5i1jg-uv-0.13.4` | `j99d3cz8m58bz6bf7fpfq8rjcqjcvnmp-uv-0.13.4.drv` | `F9JrOlA1CmUl4RQwjF+iuEt1t+Ns9KsKo5E2ldyX//s=` |

`nix path-info --store https://cache.nixos.org --recursive --json` resolved the
four roots' metadata closure:33 unique paths,2,100,758,160 uncompressed NAR bytes
in total. Only those four paths were absent by filesystem observation:
339,127,832 uncompressed NAR bytes. This is metadata availability, not downloaded
payload or cryptographic verification. Subsequent Nix copying must verify the
existing trusted signatures/hashes and registered closure; do not use
`--no-check-sigs` or disable `require-sigs`. Missing local derivation files do not
prevent direct substitution of these exact output paths.

Shortest execution package after owner3 releases capacity: owner2 coordinates
one bounded restoration+remaining acceptance batch through the ordinary fresh
watcher policy. Use `nix copy --from https://cache.nixos.org` with these four
literal output paths and their runtime closures. This operation cannot build
the missing tools or run the root shell hooks. Keep default trust enforcement,
record completion and compare resulting store paths/NAR hashes to the table.
Then use the existing24ec pending commands, adding the restored immutable bin
directories to their declared PATH. Do not resolve/update any component bundle.
Normal later tool-identity probes belong to that execution, not this diagnosis.

Retain the already declared Rust wrapper
`/nix/store/6l9kbzxwq9ij2lcmwl2qb1jdpqisjr8l-rustc-wrapper-1.99.0`.
Its inspected script explicitly executes
`/nix/store/1qg7z7i461qsv0lczc40nyi8ps6snlca-rustc-1.99.0/bin/rustc`;
this is a proven selected compiler relationship, not a same-version guess.
Both are in the exact remote closure. Clear inherited Rust compiler/loader
overrides as prescribed. Bind any required linker/pkg-config/OpenSSL support to
the retained declared stdenv/component inputs before launch; presence of a
compiler executable alone does not certify a usable build environment. Stop on
an unproved ambient linker or missing closure instead of changing toolchains.

Existing Ruby3.4.11, Node24.21/npm11.19, Python3.11.17 and prepared compiler/types
remain selected. Go acceptance keeps its distinct frozen bundle/JSON3.1.0;
root/server/Rust bundle graphs retain their own identities. TypeScript continues
using the separately hashed published0.30.2 runtime and declarations, never the
local0.31 runtime in its place. Independent Rust1.95 binaries/manifests stay
separate. Preserve Cargo offline, local Go toolchain/no proxy and installed
npm/uv offline/no-Python-download policy. Cache-directory presence does not
prove isolated-install or Cargo-lock completeness; a cache miss is a reported
prerequisite failure, not permission for a network dependency refresh.

After exact restoration, TypeScript wire has no dependency on Go/uv/Rust and
can use its already complete inputs in the granted batch. Go, Rust dev+MSRV and
installed npm+wheel/sdist execute their existing required cases without reducing
counts or relabeling d67 results. Any actual unavailable/signature/hash mismatch,
closure/input drift, source drift, dependency cache miss or first real gate
failure stops the affected batch for bounded diagnosis; no automatic retry,
new compiler, build-from-source, channel/lock update or budget adjustment.
The calibrated performance Ruby7b77/frozen graph/reference remains wholly
separate and untouched. Retain failed preflights and prior successful receipts.

Diagnosis performed only local static reads and trusted-cache metadata queries;
no NAR fetch/copy/realization, tool version execution, compiler/test/fixture,
utility, Git, service/preview or lifecycle action. All commands have completed.
No product re-review or new environment framework is implied; restoration and
gates require lead's later complete execution grant after the current sourcehold.

## Milestone 8 — simpler examples and meaningful error handling

This is new user scope after reviewed M7 `24ec424c9592951da38584379b43379b0c39f115`
(tree `288376a727deb3905d2c368150543a6d7cfc0971`). Retain that evidence for its
actual scope. The separately completed capture-mock correction is
`463e503db3611cc0f37958ad522801eb17bff361`; do not repeat or replace it with a
production capability fallback. Implementation begins only through lead's owner
grants. Architect changes this record only; no application edits or checks.

### Stable presentation packages — ready independently of renderer work

The existing renderer-owned per-kind capability query, page/group detail
metadata, panel IDs and preference format remain the interfaces. No client-ID
catalog, render-both comparison or new template/asset framework is needed.

* Copy: keep the existing client-example-only wrapper and exact `code.textContent`
  source. Make its button a smaller visible icon at the upper-right **inside**
  the code surface, positioned out of document flow. Remove the extra grid
  toolbar row; neither button nor status adds top padding, margin or line-height
  to the code. Preserve the original code's first-line vertical position. Reserve
  only an inline end gutter in the scroll viewport so code can be panned clear
  of the overlay; no page overflow or hidden code. Keep a 44px usable hit area
  (the glyph can shrink), visible keyboard focus, exact current-panel copying,
  existing HTTP fallback/HTTPS clipboard behavior and honest failure status.
  The status remains a live region outside `code`, out of layout flow; announce
  success/failure without shifting or covering readable code. No new storage,
  network, selection/focus/scroll changes or protocol-guide copy controls.
* Selectors: Language remains primary. Hide the complete Client label/control
  when the selected language has one available client; show it with only that
  language's available variants when there are multiple. **Examples remains
  visible and disabled for one supported value**, showing that value. This
  explicitly supersedes M6/M7's enabled singleton. Disable Language too if its
  complete available set has one value. Effective group fallback and saved
  preferred Thorough/client remain separate: a singleton page/client must not
  erase the preference, which returns when supported. Preserve scroll and native
  no-JS details/summary access; no hidden/disabled content panel workaround.
* Settings: retain the gear and single 44px native details trigger, current
  sidebar width and menu behavior. Add the visible label **Theme** to the existing
  theme choice group, with a semantic group/legend association. No nested menu.
* Validators: only top-level String values in Include/Exclude choices render
  their exact contents, HTML-escaped, inside the existing `code` tag, without
  added JSON quotes. Literal quote characters in the value remain. Do not strip
  quotes from serialized text or change the generic `literal` function globally.
  Preserve typed nonstrings, nested/complex serialization, hash labels, messages,
  unknown options and escaping. Empty string remains an empty string, distinct
  from an empty choice set; no data/type/validation/schema change.

| Owner | Exclusive ready paths | Acceptance and quick checks |
| --- | --- | --- |
| 0 | `servers/ruby/lib/haveapi/documentation_validators.rb`, `views/version_sidebar/brand.erb`, `spec/documentation/validators_spec.rb`, existing owning settings/template HTML assertions | Narrow choice-string formatter; Theme's visible and accessible association. Cases: embedded quotes, HTML/Unicode/empty strings, include hash labels, exclusion arrays, booleans/numbers/null and nested values. Retain existing unknown-option and local-overflow markup. The completed capture mock declares its own synthetic capabilities; no nil-profile fallback. |
| 3 | `servers/ruby/lib/haveapi/public/{css/documentation.css,js/documentation.js}`, `spec/client_examples/assets/documentation_test.cjs` (and existing directly affected asset specs) | Absolute copy overlay/no vertical shift, current code-only success/failure, theme-group styling, singleton/multiple option transitions, preference restoration, scrolling and no-JS baseline. Consume the unchanged group/page capability metadata; coordinate only Theme markup with0. |

Paths in the table lacking a component prefix are beneath
`servers/ruby/lib/haveapi/` for views and `servers/ruby/` for specs. Owner3 owns
all CSS/JS; owner0 need not edit assets or renderer files. Source-independent
DOM assertions and lint are quick; final browser acceptance checks desktop,
390px phone and tablet widths, long lines, touch/keyboard/focus, local code
panning and no page-wide overflow. No source-wide hook window until owners quiet.

### Remaining renderer contract and verification boundaries

The following source-backed contract releases owner1's dynamic/Ruby/PHP package
and owner2's modern Go/Rust/TypeScript package independently of0/3. This is a
static audit, not a new rendering/compilation result. It inspected the current
15 renderer modes, their init/basic/token/oauth2/public/protected/failure branches,
and actual Ruby/JS/Python/PHP/Go/Rust runtime interfaces. Prior M7 audit results
describe the old programs only. No runtime/provider API change is required.

| Family (15 modes total) | Meaningful M8 detail choices and actual runtime boundary |
| --- | --- |
| Ruby (1) | Add Both for init, supported Basic/token and all representable actions. Constructor is lazy: Thorough initialization explicitly calls `api.setup` inside the handler. Rescue `HaveAPI::Client::ValidationError` before its `ActionFailed` parent; use `.errors` for validation and `.response` only when it is a real response. `Authentication::AuthenticationFailed`, `ProtocolError`, actual RestClient failures and JSON decoding failures can occur during setup/authentication. Handle these around the operation, not merely around sample comments. Simple keeps its idiomatic calls/fragments. OAuth remains its existing unsupported singleton. |
| PHP (1) | Add Both for init, Basic/token/OAuth and actions. Constructor is lazy: Thorough calls `$api->setup()`. Catch actual `HaveAPI\Client\Exception\ValidationError`/`ActionFailed` for `getErrors()` and `Base` for framework authentication/protocol errors; do not invent a common Ruby-style response API. OAuth's existing state/PKCE/session/redirect flow remains intact; wrap the operation, including token exchange, without substituting an access-token-only flow. HTTPful `send()` and League/Guzzle acquisition may also throw dependency exceptions. A final application-boundary `\Exception` handler may report and rethrow these; do not swallow unknown failures or catch all `\Throwable` as successful completion. No provider implementation changes. |
| JS callback + TS callback (2) | Init/auth stay Simple-only: Simple already checks the actual `(api, ready)` result. The callback runtime has no richer async error callback; outer `try/catch` cannot catch later asynchronous throws. Actions retain Both: reply failure checks remain in Simple, Thorough additionally catches real synchronous lookup/invocation errors. Do not add Promise conversion, global uncaught handlers, fake callback parameters or success logs to manufacture another setup mode. |
| JS async + TS async (2) | Both for all supported kinds already have real awaited discovery/auth/action `AsyncError` handling. Preserve it, including known-error diagnostics and propagation of unknown exceptions; only replace credential acquisition. |
| Python sync + async (2) | Both for all supported kinds already use actual context-manager/discovery and `ActionError`/`HaveAPIError` handling. Preserve this and operation waiting. Replace env credential branches, leaving Simple fragments and async context requirements intact. |
| Go API client (1) | Init and Basic/existing-token/existing-OAuth setters return no error and do no request: singleton. Ordinary action Simple already checks Go transport/encoding error and `response.Status`/API errors. Keep singleton unless the existing successful blocking/visible-operation case adds the real operation-status call and its failure handling. Do not remove Simple checks or add a redundant wrapper merely to enable Thorough. No token-acquisition/provider feature expansion. |
| Rust async + blocking (2) | Add Both for every representable code kind. Actual `.build()` and `.send()` return the re-exported runtime `Error`. Simple retains `?` propagation and existing failed-sample checking. Thorough uses an explicit `match` on fallible construction/send with a real error arm, safe `Display`/HTTP/timeout diagnostics and propagation, and returns the same successful response for output processing. The `Error` enum is non-exhaustive: do not invent exhaustive variants. Keep explicit server-message/validation access and its existing caution; do not dump raw request data. Auth setter examples demonstrate configuration failure only, not an authentication request or token validity check. |
| TypeScript API client (1) | Init stays Simple-only: it constructs a runtime and typed facade, with no discovery or action to await; do not add a redundant request to create a variant. Add Both for supported Basic/token auth, catching actual awaited `AsyncError`; OAuth remains a limitation. Action Thorough must cover its auth/setup as well as action errors, preserving current typed property calls, failed-sample assertions and unknown-error propagation. No runtime pin in visible code. |
| HTTP, curl, CLI (3) | Stay singleton. HTTP/curl are request/response transcripts, including actual failure status/envelope, and CLI already prints validation/API failures and exits nonzero. A new shell wrapper adds little to the CLI example. curl HTTP exit status alone cannot establish HaveAPI envelope success; do not claim otherwise or add a JSON-parser dependency just for a second selector value. Existing transcript/error semantics remain. |

“Both” means frozen `[:simple, :thorough]` only after the renderer's Simple result
is representable; limitations remain Simple. Per-kind queries stay with their
existing owning class/adapter. No global capability change, HTML byte comparison
or extra render to infer capability. Keep legacy positional/direct Context calls
at either detail and shared render-only legacy-adapter fallback. The custom
renderer compatibility promise remains; all15×7×both direct calls still run.

#### Harmless literals and existing acceptance fixtures

Use ordinary language literals, escaped by the existing renderer serializer:
Basic `user` / `secret`, existing token `example-token`, existing OAuth access
token `example-access-token`. These are deliberately public example strings, not
detected credentials. Keep configured package/import identities and endpoint URLs;
no reads of current-user state, real configuration secrets, environment secrets,
private parameter defaults, profile credentials or response examples to obtain
them. Remove unused env/JSON-loader helpers/imports. Do not add runtime-version or
credential configuration. Ruby/PHP saved-token placeholders become explicit
literal examples; interactive CLI/curl forms can retain their ordinary prompts,
with literal answers. Raw HTTP OAuth metavariables for client secret/code/state
become harmless illustrative literal values with correct URL/form encoding;
runtime session/state/PKCE values in a real PHP flow still come from that flow.

Owner1 extends the existing auth example helpers, not a new catalog: derive
login/challenge **names and types only** from the authorized advertised token
resource. Reuse password-name handling (`password`/`pass`/`passwd` → `secret`),
ordinary String/Text field-name placeholders, numeric/Boolean/Resource/Datetime/
Custom typed literals, and advertised finite machine include/accept constraints
when applicable. Never use defaults or prose as credentials. Keep all required
inputs and explicit supported lifetime (`fixed`); preserve unusual names with
language-safe object keys. These are replaceable example values, not a promise
to satisfy arbitrary custom/regex credential policies. No constraint solver.
Unknown/unrepresentable required input types retain an honest limitation rather
than silently dropping a field or guessing a private value.

For dynamic JS/TS/Python token examples with declared login inputs, emit actual
literal credential login. Derive small literal input maps for advertised
continuation actions (excluding the internally supplied token); callback JS/TS
selects by its real `action` callback argument, Python by `step.next_action` and
calls real `step.submit(values)` until authenticated. Do not fabricate `.action`
on Python challenges. Unknown continuation/input names fail explicitly; no
silent empty object or fabricated token. The existing callback/onChallenge and
Python challenge objects retain control of token propagation. With no described
login shape, use the existing-token literal form. Do not add extra panel IDs,
an auth-mode preference or runtime credential branching.

Lead accepts the dynamic acceptance direction: six token-auth programs perform
real credential login and challenge completion, while the twelve protected
success/failure action programs perform existing-token authentication. The
existing36-program installed matrix then contains six challenge completions;
only the six obsolete env-toggle duplicate runs disappear. Prove provider and
mounted discovery, ordered challenge and exact action values/errors per run;
never rewrite code, inject output or claim M7's old36+6 execution identity or
complete Simple-program coverage. Literal examples must never use real secrets,
current-user values or private defaults.

Owner1 adapts `dynamic_acceptance.rb`, its spec and the existing mounted
`dynamic_documentation_api.rb` fixture: accept the above public literals through
its actual Basic/token/OAuth providers and token request/verification handlers.
Snapshot receipts separately for all36 programs. Require each of the six token
programs to show request→verification→authenticated mounted OPTIONS in order;
require all12 protected action programs to show successful existing-token
provider/discovery and exactly one action with the unchanged paths/values and
success/failure marker. No challenge events may stand in for existing-token
proof. Invalid/rejected credentials and missing/incorrect receipts must fail.
Remove secret env overrides, preserve installed import isolation, strict TS
compilation, actual HTML source byte execution and output/receipt redaction.
Record `challenge_completions: 6` inside36 programs, not six reruns. Current
dynamic capabilities still select8 Simple +28 Thorough panels; assert the actual
declared matrix rather than silently ignoring absent or duplicate groups.

Owner2 adapts the **existing** Go and TS wire expected credential literals and
removes their env-secret injection, retaining exact header/path/body/count checks
and fixed published TS0.30.2 runtime/hash. Rust needs the same explicit treatment:
its current fixture accepts `admin/pass`, obtains `token-admin` via the real
token endpoint and injects it through env; this cannot certify literal examples.
Add a narrow, opt-in documentation-example mode to the existing Rust
`integration/run.rb` → `support/haveapi_server.rb` → `support/haveapi_fixture.rb`
fixture path. In that mode only, its normal provider handlers accept the public
example credentials for the existing fixture roles and issue `example-token`
through the actual token request action. The runner obtains it normally and
asserts equality with the advertised literal; never seed tokens, accept arbitrary
credentials, rewrite rendered code or bypass the provider. OAuth accepts only
the example access token for its existing fixture user. Existing non-doc fixture
behavior remains unchanged. Root/mounted routes and both Rust modes/toolchains
remain required. The context already supplies the loopback base URL, so examples
need no base-URL env override either.

Rust's existing `cases.rb` composition currently splits Thorough source at
`.build()?`; explicit error handling invalidates that incidental marker. Keep
the established composition contract by composing an explicitly rendered Simple
action fragment into an explicitly rendered init/auth program at the existing
`let _ = &api` seam. Retain output assertions and exact fragment bytes. No
general source rewriter/parser or weakening of response/typed-value checks.
Generated acceptance remains separate from dynamic HTML exact-source execution.

#### Complete remaining owner packages and checks

| Owner | Exclusive implementation boundary | Focused proof before final review |
| --- | --- | --- |
| 1 | `servers/ruby/lib/haveapi/client_example.rb` auth helper only; `client_examples/{dynamic_helpers,js_client,js_async_client,ts_client,ts_async_client,python_client,python_async_client,ruby_client,php_client,ruby_cli,http,curl}.rb`; owning dynamic/detail/syntax specs; `dynamic_acceptance.{rb,md}` + spec; `test_support/dynamic_documentation_api.rb`; technical facts in `doc/client-examples.md` | Correct literal rendering/escaping/types, metadata-only generation, unchanged action samples, required/custom challenge inputs and missing-continuation failure. Real Ruby/PHP known-exception tests (validation/API/auth/protocol), specific-before-base order, unknown failure propagation; PHP syntax and real runtime types, no fictional APIs. Dynamic installed-fixture selection/receipt specs prove36/eightSimple/28Thorough, six challenges and12 existing-token actions. Callback/async distinction and legacy custom behavior remain explicit. |
| 2 | `clients/{go,rust,typescript}/lib/haveapi/*/documentation.rb`, their documentation unit/build/wire helpers/specs; existing Rust fixture path above; `servers/ruby/spec/client_examples/{go,rust_client,ts_generated_client}_spec.rb` when adapter expectations change | Literals and removed env helpers; unchanged generated API and profile/schema validation. Rust real fallible construction/send branches in both modes; strict TS auth error branches against the prescribed runtime types; Go mandatory Simple checks. Update Rust factory/performance **stale message expectations only** from SDK to API client (13+2 current CI cases). Retain separate direct both-detail compilation and wire coverage. |
| 0 | Presentation package above; existing `spec/documentation/example_variants_spec.rb`/owning HTML assertions if capability expectations change | Group/page metadata follows new class declarations without new schema or extra discovery; only meaningful panels, unique IDs and existing per-group fallback. No production fixture workaround for the already fixed capture mock. |
| 3 | Presentation package above | Consume metadata as supplied; no client-ID capability guesses. Recheck singleton transitions with newly useful Ruby/PHP/Rust/auth variants. |

Owner1 owns shared `detail_spec.rb` and the single technical guide edit; owner2
sends adapter facts rather than editing those paths concurrently. Main owns final
visible prose. Owner0 runs the single necessary `make doc` after final guide
bytes; generated packaged copies are not independent source edits. These are
complete packages, not per-command approvals. A concrete unsupported dependency
exception/compiler or fixture issue goes to lead; do not change runtime inputs
or weaken output checks to make examples pass.

Quick checks: owner-focused Ruby specs/lint/assets; actual Ruby/PHP handler and
syntax tests; existing strict TS and representative Go/Rust generated-snippet
compile checks for changed handlers using declared restored tools (uncertain
duration uses a fresh watcher). Demonstrate runtime error arms with known real
exception/Result objects and fixture failures, not source-substring differences
alone. No new compiled integration campaign before review. Post-review: complete
documentation/assets/Python encoder checks, actual installed npm+wheel and
npm+sdist36-program matrices, unchanged Go/TS wire and published0.30.2 proof,
Rust development1.99 and independent1.95 root/mounted/both-mode acceptance,
ordinary deterministic performance, all-client/both-detail/both-scaling gate,
and exact retained `f6e5c3750c747b33ec869c54ca220bf6f1d9d2d0`→M8-final paired
quick through the prescribed neutral harness.
Preserve frozen locks/runtime/reference/budgets and strict mismatch failures.
Record new source/input identities; successful historical results retain only
their genuine scope. Final responsive/browser/HTTP proof covers the new controls,
copy placement and literal/error panels; peer HTTPS/provider testing is a
separate downstream acceptance dependency, not a reason to alter local inputs.

No provider/authentication, search, API schema, dependencies, runtime pins,
benchmark reference/budget or public configuration-key change. Retain all15×7×2
direct renderer coverage, roles and both scaling dimensions. After all M8 source
and focused checks, perform affected independent final review, then required
installed/wire/compiler/performance and browser gates on the final source. M7
receipts remain historical; do not run its pending long gates on obsolete source.

The user requests peer deployment after M8: lead sends the exact reviewed final
SHA/tree, all-five source selection and documentation packaging facts through the
official channel. The vpsAdmin peer owns development fixtures, the dedicated
confidential documentation OAuth client, protected configuration, HTTPS cluster
deployment and real integration/OAuth acceptance. Concrete production registration,
configuration and deployment-order notes belong in **vpsfree-cz-configuration**,
under peer coordination. HaveAPI retains generic registration-before-configuration,
HTTPS/callback/scope/secret-handling guidance only. No production activation,
release/default-branch integration, peer checkout access or local TLS work is
authorized here. Existing d67 consumer selection/recovery remains intact until
the peer explicitly selects and verifies its successor. M8 is code/presentation
only, with no persisted-state migration; reverting HaveAPI restores old examples
and controls while the existing preference keys remain readable.

### M8 final history — three complete feature boundaries

This supersedes the five-group M8 projection proposal. **Do not implement the
A-only legacy extractor, forced-Thorough fixture, predecessor tests or A guide
snapshot.** They were proposed but not granted or executed. Five groups were an
internal arrangement, not a compatibility or Git requirement. Combining their
coupled core removes the need for verification code that would exist only during
history reconstruction.

The static finding remains: retained M7 A had a C-shaped extractor before C's
HTML producer, and its old env-credential fixture cannot validate M8 literals.
The solution is to introduce the complete producer/consumer feature together.
No product source or supported runtime interface changes to accommodate history.

| Final commit on exact f6 | Complete contents and boundary |
| --- | --- |
| Core documentation | Former A+B+C together: final renderer/Context/capability/legacy-adapter contracts, modern Go/Rust/TypeScript adapters, literal credentials and meaningful handlers, component and wrapper tests, complete reference HTML/assets/navigation/search/validators, final strict group-metadata installed harness/spec/md and literal fixture. All four dynamic files and all modern tests use final accepted bytes immediately. Apply only the already required optional-OAuth and performance exclusions described below. |
| Optional documentation OAuth | Former D: complete module, Chain/Provider token-validation seam, four server integration seams, real-cookie fixture and auth-dependent tests, generic OAuth guide and its technical/UI pointers. This adds optional account behavior to the complete anonymous core; ordinary API/OPTIONS credentials remain unchanged. |
| Documentation performance | Former E: exact final request-local resource Context cache, frozen worker/bootstrap/neutral authorization fixtures, deterministic and all-client contracts, scaling checks and performance guide. Core/optional retain the existing pre-cache helper until this commit. No runtime, reference, budget, role or measured-authentication-work change. |

No concrete independent release/state boundary requires splitting the core.
The generator adapters here implement documentation rendering, not a new client
wire protocol or separately published release. Their capabilities and literal
programs determine the HTML groups, and the installed consumer requires those
same declarations/programs and fixture values. Modern compiler/wire tests belong
with their actual adapter outputs. Retained file/owner inventories still let the
reviewer examine each family independently within this complete feature commit.
There is no migration, dependency/channel update stream or supported intermediate
consumer pin that requires the discarded A/B boundaries. Optional OAuth and the
performance/cache change remain independently meaningful and separate.

Only existing semantic projections remain. Owner0 prepares final-source
core/optional/performance snapshots for the genuinely mixed server and UI/auth
spec paths using the established C/D/E seam inventory. Core has no optional
module/config/require/helper registration/mount/cookie fixture, its identity
hook/controls default anonymous, and Basic never authenticates documentation.
Optional introduces its complete real-cookie cases. Keep the old stale Basic
HTML performance spec absent until its complete performance replacement arrives.
Preserve current final templates, capture-mock correction and all unrelated
assertions; no new fixture override or source fallback. Main supplies only the
existing anonymous-core/optional guide projections and final guide bytes,
checking that each snapshot describes its actual feature boundary. No separate
renderer-era guide or owner1 dynamic projection is needed.

Owner1 finishes its ordinary PHP/dynamic source and quicks; owner0 completes the
single final documentation copy/HTML quick; owner2 completes its already assigned
input work. After all source commits and collective quiet, owner2 reconstructs
these **three** commits with ordinary hooks from the frozen accepted final tree.
The history packet maps old A/B/C into Core, old D into Optional and old E into
Performance, includes owner/path inventories, and explains the producer/consumer
coupling. Do not preserve obsolete fixup approaches as extra ancestry.

Run the existing bounded source-bound four-route smoke once on actual Core and
once on actual Optional: Core is anonymous/full despite Basic, with no optional
module/token lookup; Optional uses the real cookie, revalidates its token per
request and preserves Basic-versus-cookie/API/OPTIONS isolation. Both exercise
the actual final panel/group producer and changed renderers/templates. Retain
final packaging after the final guide copy. There is no A-only quick, installed
batch, compiler campaign or broad intermediate suite. Owner quick evidence keeps
its actual input scope; final independent review and required long gates remain
on the complete final source.

Before moving the feature ref, require reconstructed final-tree and aggregate
`f6e5c3750c747b33ec869c54ca220bf6f1d9d2d0`→final patch equality against the accepted
M8 snapshot. Preserve exact externally selected
`d67bebcb37f2d4558a97caa208465147da19dbef`, published24ec and all retained source,
review and recovery receipts. Reconstruction does not select peer inputs, deploy,
publish or integrate; nonancestor pins are not literally merged/deployed.
Independent review explicitly assesses the complete three-commit history,
consolidation and no-migrations/no-update-stream conclusion. This amendment
changes design only; no product/projection/Git/test/service action was executed.

## M8 Rust CI correction — prepared fixture contract boundary

Static diagnosis of published `e5ea07028e48a6936b947c172fa89eca15e3a416`
and CI40789709969 confirms a verification-order defect. The new real-Rack case
in `clients/rust/spec/unit/documentation_harness_spec.rb:55` starts the frozen
server bundle during generator units, before the workflow prepares that bundle.
Bundler rejects platforms `[]` versus `x86_64-linux` before any fixture request;
162 units/1 failure does not establish a renderer/provider defect. See
`verification/current-CI-e5ea/receipt.md` and its retained raw unit log.

Owner2 moves only that real-fixture case into the existing
`clients/rust/spec/integration/fixture_actions_spec.rb`, adjusting its relative
fixture path. Preserve both normal/documentation modes, actual Basic requests,
invalid-Basic rejection, OPTIONS-discovered token-request action, issued-token
value and authentication, and valid/arbitrary OAuth-token outcomes. Keep the
child's explicit `SERVER_GEMFILE`, `SERVER_GEM_HOME`, cleared `GEM_PATH`,
`Bundler.with_unbundled_env` and `BUNDLE_FROZEN=true`; failures remain fatal.
The existing fixture-action validation case stays intact. No fixture or harness
implementation change is needed.

Wire this existing spec into both owning full-check entry points; moving the
case without wiring would lose automatic coverage:

- `.github/workflows/clients-rust.yml`: leave generator units, runtime checks
  and `Prepare fixture server dependencies` in their existing order. In the
  following prepared protocol stage, run `bundle exec rspec
  clients/rust/spec/integration/fixture_actions_spec.rb` in the Rust component
  shell, then the existing `HAVEAPI_RUST_INTEGRATION=1 ruby
  clients/rust/spec/integration/run.rb`, with shell fail-fast behavior. Keep
  action refs and preparation commands unchanged.
- `Makefile`: add `$(RUST_ENV) bundle exec rspec
  clients/rust/spec/integration/fixture_actions_spec.rb` to `test-rust` before
  its protocol runner. Leave `test-rust-unit` unchanged. Full checks already
  require separately prepared Rust/server bundles; do not install from tests.
- Clarify these same commands/boundaries in
  `clients/rust/docs/development.md` and `clients/rust/spec/integration/README.md`:
  the Rack contract loads the real server application under its prepared bundle,
  without a listener or Cargo. Quick units need only their component bundle.

Moving preparation ahead of units would mask the misplaced dependency while
making the documented quick-unit command require server preparation too. The
existing fixture spec is the narrower owning boundary; no new runner, skip,
fallback, lock/platform change or dependency resolution is justified.

After owner3 releases the source/utility hold and owner0's first correction
commit completes, main grants owner2 implementation and focused checks: unchanged
`bundle exec rspec spec/unit` in the Rust component context; the prepared fixture
spec command above; and RuboCop on the two changed specs. Expect 161 unit cases
and 2 fixture cases if no other cases change; record actual results, including
both fixture modes. Check CI/local wiring against the exact commands. The later
required runtime/compiler/protocol gates remain required, not inferred from this
quick proof. No checks ran during this design amendment.

This changes verification placement only: production source, fixture behavior,
dependency/lock inputs, generated programs, compatibility and rollback remain
unchanged; no migration/deployment action follows. Retain e5ea installed/browser
evidence for its actual inputs and use scoped final-source rebinding, not a blind
rerun. Main owns narrow review/history disposition and final skipped-gate coverage.

## M8 final direct quick — completed check with inconclusive timing

The single required `f6e5c3750c747b33ec869c54ca220bf6f1d9d2d0` →
`fb07c1378e4267bdfd54fa8fbfcfc57b6ec53413` quick completed on 2026-10-29
at 02:15:05 UTC in 509.874 seconds, exit0/report **inconclusive**. Original
commands, report, samples, calibration and reconciliation remain in
`performance-fb07c137/`. Eight cases pass; six retain timing uncertainty.
All14 response/counter and allocation checks pass. This is neither an all14
measured pass nor evidence of a classified product regression.

Static inspection of `performance_compare.rb:721` confirms the exact decision:
for each wall/CPU metric, noise is the largest absolute difference among the
three baseline/self pairs (or its tiny floor); excess is candidate minus
baseline minus the greater of 20% of baseline or 50ms/batch. Passing needs at
least four of five excesses below negative noise; regression needs four above
positive noise. Both require baseline median batch duration ≥0.75s. No retained
sample or classification was changed or replayed.

| Inconclusive case | Requests/batch | Baseline median wall/CPU seconds | Self-noise wall/CPU µs per request | Pass agreement wall/CPU |
| --- | ---: | --- | --- | --- |
| api.public_get | 850 | 0.628718 / 0.627520 | 73.456 / 72.992 | 4/5 / 4/5; inadequate duration |
| api.basic_get | 1330 | 0.971458 / 0.971351 | 73.947 / 74.104 | 2/5 / 2/5 |
| api.token_get | 1393 | 1.033071 / 1.031306 | 143.172 / 142.367 | 2/5 / 2/5 |
| api.typed_post | 1151 | 0.913005 / 0.911952 | 173.330 / 172.286 | 1/5 / 1/5 |
| api.invalid_post | 1064 | 0.925112 / 0.923853 | 221.259 / 221.178 | 0/5 / 0/5 |
| sqlite.page | 183 | 0.777101 / 0.776449 | 1045.555 / 1047.820 | 1/5 / 1/5 |

Every listed metric has zero regression agreement. Typed POST nevertheless has
two raw pair increases above20% (29.54%,22.39% wall), and SQLite page one
(26.57%); these do not clear retained self-noise. They must not be described as
proof of no slowdown. Public GET's initial one-request pilot was0.265671s,
selecting four operations; warmed calibration was0.004709s total. The allowed
single adjustment selected850, whose adjusted calibration was0.671121s. The
runner followed its bounded policy and left inadequate signal explicit; this
does not justify another adjustment or prove a runner defect. Its warmups use
the original pilot-derived count, as implemented for both revisions.

For these six cases, wall exceeds CPU by less than0.50% in every retained
self/pair observation. Variation appears in CPU too; the records do not identify
host contention, descheduling, CPU frequency, GC, or another specific cause.
No environment repair or host investigation is justified by this evidence.
All19 worker environments match the frozen87-gem graph; normalized manifest,
lock and benchmark inputs match, loaded-source digests belong to each declared
revision, and six neutral file hashes plus consumed samples hash match. Owner0's
completed final reconciliation preserves908 source blobs/2148 inputs and confirms
no active operation. These checks provide no attribution of timing variation.

**Disposition recommended to main:** accept the SINGLE direct quick as executed
under the existing policy while retaining its INCONCLUSIVE timing limitation;
do not claim measured performance acceptance. `doc/performance.md` explicitly
allows a completed comparison with inconclusive timings and passing deterministic
checks. `utils/performance_ci.rb` accepts exit0 with `pass` or `inconclusive`,
and the aggregate requires a completed successful comparison. The lead-created
all14-pass preview condition is stricter than this repository contract and does
not authorize a timing-policy project. Main can remove that additional condition
and separately release owner4's existing preview package; architect does not
release it here. Other required acceptance/package gates retain their own scope.

No implementation files, quick tests or additional long measurement are needed
for this diagnosis. Owner0 retains the original result and completed reconciliation;
main owns final wording/disposition and preview grant. Weekly is not a direct
replacement: both guide and `validate_source_pair` require fixed reference
`b85ec364057f536940d689b09e612512ffffaf82`, not f6. No existing longer direct
profile is available. Do not compose incremental e5ea/511 evidence, substitute
baselines, replay to seek a pass, alter budgets/graphs/calibration, or rerun until
green. Stop performance work at this recorded uncertainty unless new concrete
evidence or a separately authorized requirement changes the question. Source,
compatibility, deployment and recovery contracts remain unchanged. This section
is diagnosis/planning evidence, not a new deliverable or review gate.

## Final devtrial OAuth correction — native form Origin and referrer policy

The deliberately shared peer diagnostic de47264a establishes that deployed
`5114746f3a9f87e91c704147c0d99dd4f0d32f02` receives a native Chromium switch
POST with its cookie, matching43-character CSRF and valid scalar switch field,
but literal `Origin: null`; the exact-origin guard returns403 before revocation.
Rack's form parser is not the cause. Own retained511 and fb07 exports plus current
source have identical OAuth module, server, docs helper, brand and JavaScript;
the form partial also matches511/fb07. OAuth module SHA256 is
`c69c1a871c7f99ddc96850a012d6a0c6039849e9f6a1a2b09cd4d7b0c7dd6312`.

`DocumentationOAuth#authenticate` calls `protect_response`, which puts
`Referrer-Policy: no-referrer` on the document owning both native POST forms in
`version_sidebar/authentication_control.erb`. The account forms have no JS
submission interception. The [Fetch Origin-header algorithm](https://fetch.spec.whatwg.org/#append-a-request-origin-header)
sets Origin to null for non-CORS methods other than GET/HEAD under no-referrer;
ordinary form navigation follows that branch. This is a source-backed browser
policy conflict, not grounds to accept opaque origins or weaken CSRF.

**Owner4 fix boundary:** in `servers/ruby/lib/haveapi/documentation_oauth.rb`,
make the existing `authenticate` documentation-response call select
`Referrer-Policy: strict-origin`. Keep `protect_response` defaulting to
`no-referrer` for login, callback, logout, their redirects/errors and
`failure_page`; use a small private keyword/default, not a new public setting.
All paths retain their existing cache headers and the private search-index cache
exception. No template, JS, parser, provider, cookie format or API change.
The docs hook also covers the single-version index containing account forms.

[Strict-origin policy](https://www.w3.org/TR/referrer-policy/#referrer-policy-strict-origin)
sends at most scheme/host/port as Referer, never document path/query/fragment,
including on same-origin requests; it suppresses referrer information on
non-trustworthy downgrades. The corresponding Fetch rule preserves the actual
Origin on same-origin HTTPS POST. The deliberate privacy change is disclosure
of the documentation origin to eligible HTTPS destinations instead of no
Referer; callback codes/state, resource/search queries and credentials cannot
appear in that header. Authentication responses retain no-referrer unchanged.
Avoid same-origin or strict-origin-when-cross-origin here because they permit a
full same-origin referrer URL, and plain origin because it permits downgrades.
Logging redaction remains required independently of referrer policy.

Preserve exact configured HTTPS primary-origin comparison, valid cookie plus
constant-time session-CSRF checks, switch opt-in/strict parsing, cookie host-only
Secure/HttpOnly/SameSite=Lax attributes, fixed redirects, R1 callback preservation,
clear/revoke/fresh-login ordering and honest502 failure. Missing, null, foreign,
wrong-scheme and wrong-port Origins stay rejected; no Referer/Sec-Fetch fallback,
forged header or browser-credential workaround. HTTP docs remain anonymous;
HTTP cannot become an OAuth acceptance path. Open pages carrying the old policy
need navigation/reload. Existing encrypted sessions, provider/client config and
rollback inputs remain compatible; rollback restores the old browser defect.

Owner4 also owns focused `servers/ruby/spec/documentation/oauth_spec.rb`
regressions and the technical correction to `doc/documentation-oauth.md:119`;
main owns final prose and the normal single documentation copy/package binding.
Quick checks: existing prepared server-bundle OAuth spec and changed-Ruby lint;
assert strict-origin on root/version/resource/authentication HTML (including
signed-out/signed-in and HEAD coverage as applicable), unchanged no-store/cache
boundary, and no-referrer on login/callback/logout success/refusal/failure.
Exercise both native-form encodings with exact Origin+valid CSRF, and missing/
null/foreign Origin with otherwise valid cookie/CSRF:403, no revoke, valid session
preserved. Retain wrong-CSRF, parser, cookie, API/OPTIONS and revoke-failure cases.
Rack validates server behavior/headers; manually supplying Origin in Rack is
not proof of browser-generated Origin.

After quick checks and commit, main assigns affected general plus high-risk
auth/security review before real browser verification. Peer owns refreshed HTTPS
deployment and ordinary native clicks on Sign out and Switch user, with no
header injection/interception: verify effective docs strict-origin header (no
proxy/meta override), actual matching POST Origin, successful revoke/clear and
fresh login to a different user, clean callback destination, preserved failure
semantics and redacted logs. No raw credentials/cookies/CSRF/code are recorded.
Old tab requires reload before the trial. Stop on403, unexpected header policy,
revoke failure or sensitive logging; report rather than introduce a fallback.

No additional peer facts are required for implementation; effective deployed
policy and successful native browser flow remain acceptance evidence. Main
retains exact511 deployment/recovery and prior review/evidence scopes, then
selects the reviewed successor. No release, merge, TLS/config change, broad
installed/compiler/performance rerun or new test framework follows from this
header correction. Only design changed here; source, tests, browser/HTTP and
peer state were untouched. Official standards were read without runtime probes.

## Client-example language style — isolated follow-up to 2f6

User feedback at17:39 requests consistent language style, especially PHP quotes
and excess blank lines, explicitly without delaying the OAuth devtrial. Static
inspection confirms original HaveAPI HEAD
`2f6c18a80f3a5f8ce46449ff81183b100b60f34c` is clean. **Owner1 alone** implements
in a distinct same-session HaveAPI worktree/feature branch based on that exact
commit, prepared under the ordinary worktree procedure. Keep the original
worktree/ref, peer update2512, preview and all consumer pins untouched. No style
successor becomes a deployment prerequisite; no release/default integration.

The source registry (`ClientExample.label/clients`, confirmed by existing
`presentation_spec.rb`) contains15 renderers: Ruby; JavaScript callback/async;
TypeScript callback/async/API client; Python sync/async; Go; Rust async/blocking;
PHP; CLI; curl; HTTP. Review their actual init, Basic/token/OAuth auth and public/
protected/success/failure action lanes at both direct detail inputs, including
existing limitations. Do not turn identical or unsupported lanes into new choices.
Callback JS/TS init/auth, Go init/auth and typed-TS init remain Simple-only;
Go's extra action detail remains conditional on the existing operation helper.
CLI/curl/HTTP remain Simple-only; all M8 real handlers and capability queries stay.

| Owning source path (relative to HaveAPI) | Concrete formatting correction / basis |
| --- | --- |
| `servers/ruby/lib/haveapi/client_examples/php_client.rb` | Use single quotes for static non-interpolated provider names, keys, messages and public credentials, consistent with existing `value`, PHP client source and user preference. Keep semantic escaped newline strings where needed. Use4-space block/array indentation (`.editorconfig`, PHP source, PER-CS config), spaces around concatenation, and no empty line immediately before `else`/`catch`/closing block. Fix duplicate separators from newline-terminated initialization plus heredocs, optional credentials and wrapper assembly. |
| `servers/ruby/lib/haveapi/client_examples/ruby_client.rb` | Keep2-space Ruby indentation and prefer single quotes for authored plain static strings. Remove excess separation caused by joining initialization with an empty optional setup fragment and adding newlines to already-terminated strings. Preserve `dump`/`inspect`/PP data encoders and their necessary escaping; do not rewrite arbitrary Ruby data literals for cosmetic uniformity. |
| `servers/ruby/lib/haveapi/client_examples/python_client.rb` | Assemble imports without a leading empty line when stdlib is absent. Use one blank line before module-level executable sync code, two around a top-level async function as in the Python client. Keep4-space suites and safe double-quoted literals; Ruff defaults/client code support this, not PHP quote rules. Both sync/async inherit this producer. |
| `clients/go/lib/haveapi/go_client/documentation.rb` | Replace authored2-space nesting with Go tabs at its known program/import/conditional/loop assembly sites; keep native double-quoted string encoder and conventional Go spacing. No runtime gofmt subprocess. |
| `clients/typescript/lib/haveapi/typescript_client/documentation.rb` | Add ordinary spaces after comma/colon and within authored import/object braces in the compact literal/program assembly; keep2-space blocks. Make authored import quoting consistent within examples using the existing safe literal encoder, retaining computed `__proto__` keys and identifier/nonidentifier access. No generator-template/runtime change. |

Dynamic JS/TS already have consistent double-quoted data, semicolons and2-space
example blocks; Rust already uses4-space blocks and its dedicated string encoder.
CLI/curl shell quoting and HTTP/JSON separators have distinct syntax requirements.
No demonstrated additional style change is assigned to these families. Their
runtime source may use different valid presentation conventions (JS runtime uses
tabs); that alone does not justify a new formatter or broad rewrite. Existing
inheritance covers all variants. Optional idiom rewrites remain out of scope.

PHP literal correctness is a required invariant, not a textual quote replacement.
Retain escaping of apostrophe/backslash and literal `$` in single-quoted ordinary
strings. For strings containing control characters, use a narrowly escaped
double-quoted representation when necessary: escape backslash, quote and dollar,
and encode controls with PHP-valid fixed-width escapes (for example `\xNN`).
Do not use JSON `\u` escapes as PHP strings or change newline into literal
backslash-n. No physical control/newline may be changed by wrapper indentation.
Preserve exact Unicode, quotes that are data, empty values, trailing backslashes,
false/null/zero, array/hash shape, field order and existing public-literal choice.
Retain semantic `"\n"` in error output; no blanket ban on double quotes.

Normalize only known assembly boundaries: trim a fragment's boundary newline or
omit an empty optional fragment before joining logical blocks, leaving one useful
blank line. Indent nonempty source lines without adding whitespace to empty ones.
Never run a whole-rendered-source regex/formatter that could alter string contents,
comments, shell continuation, HTTP header/body separators or custom renderers.
No common `ClientExample.render` transformation, new formatter dependency/service,
line-width project, schema/config/profile key, request value/order, error branch,
authentication, environment-secret or HTML/JS control change.

Owner1 updates only affected assertions in existing owning specs:
`servers/ruby/spec/client_examples/{syntax,detail,presentation,dynamic_python}_spec.rb`
and Go/TypeScript `spec/unit/documentation_spec.rb` as needed. Use the existing
fixtures/registry for small representative formatting assertions across the15
entries and both details; assert zero leading/trailing blank padding and no
duplicate **assembly** separators, with explicit Python/HTTP/data exceptions.
Do not enforce whitespace rules inside arbitrary literal content.

Proportional quick checks in the isolated checkout/prepared declared graphs:
affected server specs above (existing PHP/Ruby syntax and handler execution,
Python AST), changed-Ruby RuboCop, and owning Go/TS documentation units. Extend
existing PHP execution tests to round-trip normal and hostile/control literals
through actual emitted expressions, including inside the Thorough wrapper;
retain real exception ordering/unknown-error propagation. Use installed gofmt
only as a check of representative complete/fragment Go output, not a production
dependency; existing TS syntax/type-check helper verifies changed literal/program
spacing. No toolchain installation or broad compile/wire/installed/performance/
browser campaign. Unexpected semantic failure stops the style package for owner
diagnosis; it does not delay or mutate the independent OAuth trial.

All public renderer/adapter/Context/direct-call interfaces and external custom
renderer compatibility remain unchanged. Only snippet presentation bytes change;
no persisted state/migration or deployment ordering requirement. Rollback is the
retained2f6 ref. Ordinary commit/hooks, affected final review and separate branch
publication follow the lead's complete grant. Main need not author new visible
labels/prose; preserve existing explanatory comments and guide contracts, asking
main only if a concrete technical wording change becomes necessary. No source,
test/runtime, Git mutation or peer action was performed for this brief.

### Formatting deployment after accepted OAuth trial

The user confirms: “I tested oauth in the dev cluster and it works just fine.
Continue deploying formatting fixes.” Advance the development deployment from
HaveAPI `2f6c18a80f3a5f8ce46449ff81183b100b60f34c` to accepted target
`1b264e25a73a0ab9bca5f847bd52254f74e0931c`, tree
`dcdba06a92fe0d8a577f4cffe46ea69fc8d73a40`. The five-renderer/six-spec change
preserves dependencies, schemas, authentication, public interfaces and literal
values; no state migration or coordinated component upgrade is required.

Reuse the lead's accepted focused 150/0 and TypeScript 63/0 results, independent
review of `6e09` with no findings followed by the narrow one-line stale-oracle
correction, and all 11 successful final CI runs. The peer lead for
`2026-10-24-vpsadmin-haveapi-upgrade` owns the consumer pin/hash, locks, package,
affected review, normal public update and service acceptance under official
handoff `f0af62a4`. Its receipt must identify the actual applied HaveAPI lineage,
consumer revision and package identity. Deployment remains pending that receipt.

Retain the existing consumer `90e2` / HaveAPI `2f6` rollback and preserve OAuth
client 3, encryption key, configuration, PHP and private state. This presentation
update requires no credential/key rotation or state reset and adds no credential
logging. Existing session/cookie and authentication contracts remain unchanged;
recovery uses the retained package/configuration pair without migrating data.

Bounded rendered acceptance covers representative PHP Simple and With error
handling examples (single quotes where valid, preserved escaping, useful block
separation without excess blank lines), plus affected Ruby, Python, Go and typed
TypeScript snippets. Consumer package/service gates remain with their owner;
there is no additional producer-test, native/browser matrix, full OAuth or
performance campaign for this formatting deployment. Stop and report a concrete
lineage, package/service or rendered-output mismatch through the lead, preserving
the rollback state rather than expanding scope.

No design blocker is known. This addendum authorizes no merge, release,
production activation or session lifecycle action. Architect scope ends with this
design-only update; main owns plan/state/current-delivery records and peer
coordination. No code, Git, network, runtime or verification action was performed
for the addendum.

## Durable client-example formatting instructions

The user requests instructions to prevent future formatting regressions. Record
the accepted `1b264e25a73a0ab9bca5f847bd52254f74e0931c` conventions, without a new
renderer audit or behavior change. **Owner1 alone** owns this complete docs
package after main's grant. Use a separate same-session HaveAPI docs worktree/
feature branch from exact `1b264e25` (for example `haveapi-example-instructions`);
keep the delivered style branch, original worktree and consumer inputs immutable.
Deployment91432 and its pending installed/served acceptance remain independent;
these instructions require no consumer repin, package rebuild or update gate.

Only two authored paths are needed: add one required-reading link in root
`AGENTS.md` for changes to example renderers/adapters or their source assertions,
and add `## Example source style` before Verification in
`doc/client-examples.md`. That section owns the rules and proportional check
guidance; do not duplicate them in component instructions or a new policy file.
The existing `make doc` copies the guide into ignored
`servers/ruby/doc/client-examples.md`; never author or commit that copy.

Use a compact convention table covering the existing language families and all
their variants, distinguishing authored syntax from encoded sample data:

| Language family | Preserve the accepted example-source convention |
| --- | --- |
| PHP | Four-space blocks/arrays, single quotes for ordinary static strings without interpolation, spaces around concatenation. Escaped double quotes remain necessary for some control strings and semantic newline output. |
| Ruby | Two-space blocks; single quotes for plain authored strings. Keep `dump`/`inspect`/PP encoders where data requires escaping. |
| JavaScript / TypeScript | Two-space blocks, double-quoted authored strings/import specifiers, semicolons, conventional comma/colon/import/object spacing; preserve safe computed keys and typed property access. |
| Python | Four-space suites and existing double-quoted data encoding. No leading blank when optional imports are absent; one blank before module-level executable code, two around top-level async definitions. |
| Go | Tabs and gofmt-compatible spacing/import groups; native double-quoted string encoding. A test may use gofmt; rendering must not execute it. |
| Rust | Four-space blocks, conventional Rust spacing/imports and the existing string encoder for both async/blocking variants. |
| CLI / curl / HTTP | Preserve shell quoting/continuations and protocol/JSON whitespace, especially the HTTP header/body separator; other languages' quote/blank-line rules do not apply. |

At known assembly boundaries, omit absent fragments and join logical blocks with
one useful blank line; avoid padding, duplicate separators and whitespace on
empty lines. Preserve language-specific separation above. Never normalize whole
rendered programs or custom-renderer output with a shared regex/formatter.
Literal values, Unicode, apostrophes, backslashes, dollar signs, control bytes,
false/zero/empty/null and encoded request data must retain their runtime meaning.
Explain PHP's narrow escaped double-quote exception: escape dollar/backslash/quote
and use PHP-valid control escapes, not JSON `\u` escapes. Preserve public literal
credentials, real error handlers, direct-call/custom-adapter compatibility and
meaningful detail choices; formatting cannot remove inputs, change control flow
or manufacture extra panels. Add no formatter, dependency or blanket quote rule.

Future renderer changes select checks by affected language, kind and inherited
mode: inspect relevant init/auth/action output at both direct detail inputs,
including empty optional fragments and encoded literal edge cases. Link to
existing owning checks: server `spec/client_examples/{syntax,detail,presentation,
dynamic_python}_spec.rb` (PHP literal round trips/real handlers, custom whitespace,
Python AST and separation); Go `spec/unit/documentation_spec.rb` (gofmt equality);
TypeScript `spec/unit/documentation{,_compile,_performance}_spec.rb` (source,
strict compilation and bounded work). Rust owns its corresponding
`clients/rust/spec/unit/documentation{,_factory,_harness,_performance}_spec.rb`
checks; select the affected cases when Rust changes. Search adjacent HTML,
fixture and performance assertions for
exact source spelling, not just the directly named style test. The `1b264e25`
Basic-auth quote correction is evidence for this instruction, not history to
embed in the public guide. Update intentional spelling expectations while
retaining semantic assertions, traversal/allocation bounds and compiler checks.
Do not require every language toolchain for an unrelated edit; existing broader
verification policy remains authoritative.

For this **docs-only** package: review the diff against accepted source, verify
relative links/heading anchors, run `make doc`, compare the copied guide with its
source, and run `git diff --check` plus normal mandatory hooks in the prepared
declared environment. The existing focused rendered-guide check is, from
`servers/ruby`, `bundle exec rspec spec/documentation/shared_pages_spec.rb
--example 'serves /doc/client-examples'` (both guide aliases). No new test harness
or application tests are needed; no compiler, native/browser, installed-client,
OAuth or performance campaign is added. Main applies the final prose pass.

Commit one coherent docs change, then main assigns mandatory independent final
general review of the committed instructions and complete branch history before
publication/readiness. Include the unchanged accepted `1b264e25` boundary and
prior review provenance; explicitly record no migrations or dependency/update
streams. Check that the only authored delta is the two documentation files and
that none of the new wording weakens existing checks. No runtime/interface,
dependency, auth, schema or stored-state change means no deployment ordering or
data rollback requirement; retain all existing `90e2`/`2f6`/`1b264e25` recovery
references and protected state. No default integration, release, production or
lifecycle authority follows. No design blocker remains; this brief changed only
design.md and launches no implementation, checks or peer action.

## Security remediation — CLI and curl shell arguments

The user authorized fixing appropriate introduced and pre-existing audit findings,
then independent re-audit. Daybreak's deliberately shared `e47d852b` report and
`security-audit-shared-fixtures.md` (`9df6f470`) confirm two pre-existing MEDIUM
copy-and-run shell injections, with two successful local PoCs per renderer.
This static assessment agrees with their mechanisms; it does not claim a new
PoC execution. In `ruby_cli.rb`, `init` interpolates base URL/version, `example`
joins raw resource/action/path arguments, and `input_param` wraps unescaped data
in single quotes. In `curl.rb`, `request` embeds Ruby-escaped JSON in shell double
quotes (which still evaluate substitutions), and init/auth/request URLs plus the
token header use unescaped single-quoted interpolation. Existing token-login
escaping protects only that payload. HTML escaping in `client_result.erb` and
copying `code.textContent` preserve these shell metacharacters.

Impact requires a user to run the displayed command and attacker influence over
its data, URL or description. `server.rb` derives the URL from the Rack scheme/
Host and mount; real Host influence depends on the deployment/proxy boundary.
This is local shell execution, not execution by the server or browser merely
rendering a page. Fix serialization at the renderer; do not change Host routing,
proxy trust, authorization, HTTP encoding or provider behavior to mask it.

**Owner1 alone**, after main's grant, prepares a separate same-session fixes
worktree/branch from exact `ae46cf27a9afb6558d386c293cec7231dd6c423d` /
tree `27dcf148f9b03867a3dfc65a29c76e77a87682ec`. Preserve the user-review checkout,
all prior refs and deployed `1b264e25`/preview. Complete source, regression checks,
technical docs, hooks and one coherent security commit there. Owning paths:

- `servers/ruby/lib/haveapi/client_examples/ruby_cli.rb`: serialize each dynamic
  argument exactly once with existing stdlib `Shellwords.escape` (or its argv
  join), after existing value conversion. Cover base URL, version, the complete
  dotted resource name, action, every path argument, complete option names and
  values in init/auth/actions. Retain option order, Boolean flag selection and
  the action `--` delimiter. Do not shell-escape the composed command, `$ ` prompt
  or authored continuation syntax, and do not double-escape token-login fields.
- `servers/ruby/lib/haveapi/client_examples/curl.rb`: the same token rule covers
  every init/auth/action URL, action method and complete dynamic header. Serialize
  request bodies with `JSON.generate`, then shell-escape the entire JSON argument
  once. Retain the token login envelope and general request namespace, method,
  URL/query construction and `--data-binary` behavior, including existing GET
  behavior. Remove the PP-based shell-body construction; keep readable authored
  command continuations and normal JSON response display.
- Add focused cases in existing `servers/ruby/spec/client_examples/` (one
  `shell_spec.rb` is sufficient), adjusting existing affected syntax/detail/
  presentation or HTML spelling assertions only where necessary. Narrowly amend
  `doc/client-examples.md#example-source-style`: CLI/curl require shell-token
  encoding after data serialization; raw HTTP is a transcript, not shell source.
  Main owns final visible prose; `make doc` alone refreshes the ignored copy.

Share stdlib Shellwords, not a new production formatter/base-class transform or
service. Preserve public method shapes, Context/custom-renderer output, existing
single-detail capability and success/failure display. CLI string interpolation
currently means `to_s` for non-Boolean values, including arrays/hashes and nil;
preserve those argument strings rather than inventing JSON/list parsing or
claiming new nested-value support. The real CLI's existing `@file`/`@@` and
OptionParser semantics remain unchanged. Empty/nil CLI arguments remain present;
curl JSON retains arrays, nested objects, false, zero, empty strings and null.
No new binary/NUL-in-argv capability is claimed. This shell-boundary fix does not
assert that an entire prompt-and-response transcript is an executable script.

Acceptance uses the four supplied reproductions plus bounded edge cases for
all command-producing lanes: quotes, apostrophes, backslashes, dollar signs,
backticks, substitutions, separators, spaces, tabs/newlines, Unicode and empty
arguments; test Boolean true/false, numeric zero and structured/null values at
their existing serialization boundary. Run the declared environment's `sh` with temporary fake
`haveapi-cli`/`curl` executables, capturing NUL-delimited argv and harmless markers.
Require successful shell exit, exact intended argv/count/order and absent markers;
parse captured curl JSON and compare complete values. Remove only the authored
leading `$ ` when executing a command; preserve its continuations and embedded
newlines. For auth transcripts, select each known command span intact, excluding
display-only output without rewriting argument data. Syntax checks alone and
marker absence without argv equality are insufficient. Use no real client,
network, real credentials, user config or live services.

Quicks in the prepared declared environment: focused new shell cases plus
existing `syntax_spec.rb`, `detail_spec.rb` and `presentation_spec.rb`, changed
Ruby lint, affected exact-source assertions, `make doc`/copy equality and normal
hooks. Use the existing Ruby CLI parser only for a concrete argument-contract
question; do not turn this into a client-runtime redesign or full suite campaign.
No additional compiler, installed-client, browser/OAuth, performance or wire batch
is required by this delta. Stop on a changed argument/value or unsupported shell
case and diagnose rather than weakening the assertions.

After commit/quicks, main assigns mandatory HIGH-risk final review with all four
affected lanes (general, architecture/repetition, scope/proportionality, risk/
compatibility), including full history and explicit no-migrations/no-repeated-
update-stream conclusions. Then publish the exact corrected source and arrange
the separately authorized Daybreak re-audit through the lead. Reuse earlier
evidence only at its actual scope. No dependencies, schema, API, provider or
persisted state change is intended; rollback needs no migration, but an older
renderer restores the known unsafe example behavior. Keep existing recovery refs
and protected state. No merge/default/release/deployment/production/lifecycle
authority is added. Architect work is design/static reading only; implementation,
local PoCs and re-audit remain pending their owners.

## Security remediation, cycle 2 — CLI help and copied responses

Daybreak's shared `5b5b0cc0`/`0b932` report confirms VULN-01/02 fixed at
`ddf836fbb33ec6f920c3edfd9a4a53c2c2eb494b` (tree
`30efb19e02a756036771767745a9858fe968f95b`), with no new ddf regression. Its
additional MEDIUM VULN-03/04 cases and synthetic fixtures are recorded in own
`security-audit-round2-shared-fixtures.md` (`f2e6d33d`). Static source confirms:
CLI help consumes server examples through `Action#examples` and
`Cli#print_examples`, then interpolates executable/resource/action and ad-hoc
quoted values in `cli/example_formatter.rb`. Server RubyCli appends raw table or
failure text; the common renderer combines curl request and raw JSON response.
The Copy control copies all `code.textContent`. These require attacker-controlled
example/response data plus victim copy/run, not server-side evaluation. VULN-03
is pre-existing; VULN-04 has old sinks with material exposure from Core510's Copy
control. Preserve this mixed provenance and the peer's 1+2 confirmed local PoCs;
this architect pass performs no new execution.

**Settled response choice: retain one block and comment every response line in
the owning shell renderer.** Responses remain visible and are copied as inert
comments. Separate request/response DOM/result fields would require common result,
template, language and clipboard interfaces for the same security outcome; they
are unnecessary here. Do not change `ClientExample.render`, result shapes,
templates, CSS, production JavaScript, selectors, highlighting language, copy
fallbacks or direct-detail/custom-renderer behavior. Copy continues to take exact
visible `code.textContent`, including comments, without filtering or rewriting.

Owner1 prepares one separate same-session worktree/branch from exact ddf; retain
the published ddf, review ae46, deployed1b and all earlier recovery refs unchanged.
Use two coherent commits: independent Ruby-client CLI-help quoting first, then
server transcript composition and its tests/guide. Both need the complete final
review before publication; no obsolete attempts or fixups are retained.

1. **CLI-help commit:** `clients/ruby/lib/haveapi/cli/example_formatter.rb` and
   focused `clients/ruby/spec/cli_example_formatter_spec.rb`. Require stdlib
   Shellwords and encode each complete dynamic token once after existing string
   conversion: executable name, joined dotted resource, action, dashed option
   names and values. Keep Boolean flags, order, delimiter, unknown-parameter
   filtering, `to_s`/empty/zero/nil/structured values and runtime `@`/`@@` parsing
   unchanged. Preserve `format_examples(cli, action, out)` and output routing,
   title/response display and calls to `cli.format_output`. No CLI parser or
   client request changes, global formatter or server-library dependency.
2. **Transcript commit:** own `servers/ruby/lib/haveapi/client_examples/
   {ruby_cli,curl}.rb`, existing `spec/client_examples/shell_spec.rb`, affected
   source assertions, `spec/documentation/client_examples_spec.rb`, and the
   existing asset `spec/client_examples/assets/documentation_test.cjs`. RubyCli
   comments the entire formatted success table (including labels/headings) and
   complete failure message/error text at their append boundary. Curl adds an
   owning `example(sample)` composition method so common render dispatch uses
   request plus commented response; retain its existing direct `request(sample)`
   and raw-JSON `response(sample)` contracts. This avoids changing shared Http or
   custom renderers. Comment static `Password: secret` display lines in these
   two shell renderers as well. Existing escaped command arguments, prompts and
   useful continuations remain intact.

For the owned display fragment only, treat LF, CRLF and bare CR as physical line
boundaries, normalize them to LF, then prefix **each** line with `# `, including
embedded lines in values/labels/messages/error keys. HTML parsing normalizes CR
to LF, so prefixing only existing LF-separated lines would leave an escape route.
Finish the comment block with a newline and separate it from the complete command.
Do not trim or transform executable source or shell-encoded literal arguments;
do not merely quote response data or comment only its first line. A tiny private
fragment helper in the owning renderer is enough; no new shared framework.
Keep output readable, including false/zero/empty/null/structured response values
and useful failure diagnostics. Curl's direct response remains JSON-parseable;
only its composed shell example displays the comment prefixes.

Regression acceptance uses the supplied three new cases and bounded extensions:

- CLI help: temporary fake executable, captured complete argv and absent markers
  for hostile program/resource/action/option/value tokens, spaces, quotes,
  substitutions, backticks, separators, LF and Unicode; preserve Boolean flags
  and existing conversions. Restore `$PROGRAM_NAME` in `ensure`. Keep this unit
  independent of `clients/ruby/spec/spec_helper.rb`, which starts a real fixture
  server: require the ordinary CLI library directly and use the synthetic action
  and output receiver. No actual client/network/config access is needed.
- Server: exercise real class `render(:example, context:)` at both direct details,
  success and failure, with hostile multiline table labels/data and message/error
  fields, CR/CRLF/LF, quotes, substitutions, leading shell syntax and trailing
  backslashes. Execute the **whole** returned transcript with the existing fake
  commands, removing only the authored leading `$ ` as in the supplied PoC; never
  remove or repair response lines. Require shell exit success, exact request argv
  (and parsed curl request JSON), absent markers and visible complete diagnostics.
  This proves the full transcript after ordinary prompt removal, not a new claim
  that unchanged display prompts are literal executable commands.
- Check actual rendered HTML preserves the comment prefixes after entity/line
  decoding. Extend the existing real Copy-handler asset fixture with a full safe
  shell transcript containing hostile response text: clipboard payload must equal
  the entire selected code text, comments included, through secure and native
  fallback paths. Keep existing focus/selection/scroll/failure assertions. The
  renderer shell execution and unchanged Copy identity checks together cover the
  copied tail; do not substitute a request-only test or duplicate copy algorithm.
  Verify direct curl response JSON and raw HTTP/unrelated custom-renderer output
  unchanged; subclasses inheriting a built-in renderer inherit its safe display.

Quicks are the isolated CLI-help spec, server shell/syntax/detail/presentation and
affected HTML specs, existing documentation asset test, changed Ruby lint and
normal hooks. Retain first-cycle negative regressions; prove the three new
reported cases fail on ddf and pass with the corrections using only controlled
fake executables. Narrowly update `doc/client-examples.md#example-source-style`
to distinguish shell argument encoding from inert displayed response comments;
main owns final wording, and `make doc`/copy equality handles the ignored copy.
No full runtime/compiler/installed/browser/OAuth/performance/wire campaign follows.

No material product decision remains. After all intended commits and quicks,
main assigns HIGH/all-four-lane independent final change/history review, then
exact-source publication and authorized Daybreak re-audit. Inventory the complete
series, retaining previous accepted source boundaries; no migrations, repeated
dependency/update streams, runtime/API/auth/provider/state or dependency changes.
Rollback needs no data migration but restores known unsafe display behavior;
old deployed source is not equivalent to corrected source. No merge, release,
deployment, production or lifecycle authority is added. This is a design-only
update; all implementation, checks, publication and re-audit remain with owners.
