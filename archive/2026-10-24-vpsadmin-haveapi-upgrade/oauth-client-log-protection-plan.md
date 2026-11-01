# OAuth client log protection plan

Protect OAuth callback data in logs for the legacy PHP WebUI, preserving useful
diagnostics and existing login behavior. Earlier API/auth protection stays;
React stays unchanged.

Status: implementation remains authorized, but the user's subsequent instruction
“drop the KB and discourse oauth changes” cancels both those packages. Their
unshipped source, quick/build evidence and earlier design below are historical,
not remaining deliverables, blockers or required checks. No further KB/Discourse
diagnosis, scan proof, fixtures or builds are authorized by this plan. E1 owns
the lead-directed stop/reconciliation of its exact Discourse build and removal
of canceled source/config/packages/overlays/tests/history, preserving recovery
refs and the generated P0 pin. E2 retains only the minimal P0 transport check;
E3's Discourse package stops. Deployment, real production acceptance and default
integration still require separate authorization. No credential changes or log
deletion are proposed.

## Scope and source boundary

Protect the legacy PHP WebUI at its callback proxies and application log sinks.
Keep React's existing protection unchanged. The current PHP-only disposition
below overrides the wider original scope and six-system execution split retained
later in this record; those historical sections do not reauthorize canceled work.
The shared API/auth proposal protects the OAuth server side for every client;
it does not protect these separate client origins. Docs are different because
their callback shares the API origin. Reuse the coverage matrix in
[design.md](design.md#2026-10-30-bounded-oauth-logging-coverage-shared-server-and-four-clients).

- Owning site repository: `vpsfreecz/vpsfree-cz-configuration`, base
  `fcc7fc97be79df92ed39b4a7bfcc8ba21dc6c627`, inspected proposal
  `249f2eb5896b0a2697ed94e44657294847b3e606`. Implementer1 alone prepares/registers
  `worktrees/2026-10-24-vpsadmin-haveapi-upgrade/vpsfree-cz-configuration-oauth-clients`
  on `2026-10-24-vpsadmin-haveapi-upgrade-oauth-client-logs`, starting at exact249f.
  Existing249f stays unchanged; no automatic rebase or input refresh.
- PHP/module reference: `vpsfreecz/vpsadmin`
  `33d6c7723b392c828de2165854d106d9528f9305`; prior base4a21 has the same inspected
  PHP callback handling. Product changes belong in a separate vpsAdmin worktree
  only if the focused application checks establish a necessary change.
- React reference remains `606a02c19f328c69298dd30780c805211fb5cb27`.
- Exact selected nixpkgsStable: `718f670e845328e9c2cecdd832835712b2cbd065`, read
  locally from `/nix/store/z40fynbhnw0d06q05mw2mznn49h1y9pk-source`.
  No nixpkgs/application/dependency version update is part of this plan.

Current update3922, canonical33d6, config249f and their recovery references remain
untouched. Lead reports the independent default-spec task published at a089 with
34/34 services checks; this plan neither repeats nor holds that work.

## Current PHP-only correction and execution boundary

Inspected failure boundary is configuration
`7fdb12aeddf5bab0d4406b185b1097950867525f`, selecting reviewed/published P0
`75c691b17c48115f929b57ef55f78935be006ea6`. E1 alone changes configuration after
the lead confirms the frozen batch's safe reconciled boundary. Apart from the
separately instructed cancellation and guide reduction, only these two source
corrections are needed:

1. In `cluster/cz.vpsfree/vpsadmin/common/webui.nix`, use the existing pool option:

   ```nix
   services.phpfpm.pools.vpsadmin-webui.settings."php_admin_value[error_log]" =
     lib.mkForce "syslog";
   ```

   The selected vpsAdmin module (`nixos/modules/vpsadmin/webui.nix:216–228`)
   assigns ordinary-priority `"stderr"`; `mkForce` overrides that assignment.
   PHP treats it as a filename, not the stderr stream: installed FPM returned
   `/nix/store/ah4r14myrgr1xm80j434l93aj2wp07nx-php-8.4.27/stderr` from
   `ini_get('error_log')`. Attempt2 preserved pool logging options and captured
   FPM master syslog, but neither the fixed callback category nor the benign
   ordinary initiation error appeared. This is a selected sink defect, distinct
   from earlier scratch PATH/UID readiness failures. FastCGI fallback suppressed
   by nginx is consistent with the evidence, not a traced mechanism.
   `syslog` is PHP's supported special destination (selected ini:587–601), and
   FPM already uses syslog for master diagnostics. Preserve `log_errors`, worker
   capture, scoped nginx error suppression and all auth inputs. This changes only
   the WebUI pool destination: no global PHP policy, files/rotation or P0 product
   change. Fixed callback categories and ordinary nonsecret diagnostics must
   actually arrive, rather than passing solely because logs are empty.

2. In `cluster/cz.vpsfree/vpsadmin/common/frontend.nix`, preserve the generated
   dev vhost when adding its existing Basic auth file. Replace the rightmost
   shallow override with this literal per-vhost merge:

   ```nix
   ${config.vpsadmin.frontend.webui.dev.virtualHost} =
     phpClientVirtualHosts.${config.vpsadmin.frontend.webui.dev.virtualHost}
     // { basicAuthFile = "/private/nginx/mon.htpasswd"; };
   ```

   The existing `// { dev.basicAuthFile = ...; }` discards the generated dev
   `forceSSL`/`onlySSL`/`extraConfig` policy. Actual nginx9x7w has an unsafe
   automatic HTTP server, unsafe TLS log and a second safe HTTP server. The
   literal merge restores the intended protected TLS + explicit HTTP pair while
   retaining Basic auth, names/aliases, backend, listeners, ACME and redirects.
   No recursive/global abstraction or authentication change is needed.

Evidence remains in `oauth-client-logs/postreview/php/attempt-2/p0/`
(`result.json`, request results, `adaptations.json`, captured sinks), and
`oauth-client-logs/postreview/systems/attempt-1/`
(`webui1-runtime-paths.json`, `proxy-dev-policy-blocker.json`). Preserve failed
attempts as failed; do not label7fdb as runtime accepted. The earlier KB
base-ini-only diagnosis was withdrawn; cancellation now removes all KB acceptance
obligations rather than turning that interpretation into a fix or success claim.

**Checks and handoff.** E1 runs normal format/hooks and the retained PHP/proxy
quick cases after scope reduction, then commits the coherent PHP-only series.
Independent affected source/security/history review must cover these new fixes,
canceled-code removal, guide and final pin/history; old review does not cover
the changed boundary. Expect no schemas/migrations, dependency/client/secret
changes; preserve P075c product evidence and prior recovery refs. No new P0
source review or native34 is required solely for this config correction.

After that review, E1 uses normal `confctl build` for exactly
`cz.vpsfree/containers/prg/proxy`, `cz.vpsfree/vpsadmin/int.webui1`,
`cz.vpsfree/vpsadmin/int.webui2` and `cz.vpsfree/vpsadmin/int.webui-dev`, retaining
final source/input/derivation/output graphs. Reuse prior results only for exact
unchanged relevant derivation/runtime inputs, never by relabeling old outputs.
Generated config must show one intended HTTP and one TLS dev server, safe
access/error/referrer policy and unchanged Basic auth/aliases/ACME/maintenance
and backend selection. All three WebUI pools must select `error_log=syslog`.
Earlier API/auth protection and unchanged React remain in the effective proof.

E2 then repeats only the existing minimal installed P0 fixture with actual final
FPM/nginx/ini/pool and installed P075c page, protected private syslog and the
recorded path/UID/worker adaptations. Prove effective `error_log=syslog`, fixed
callback diagnostic presence, benign ordinary native diagnostic presence and
sentinel absence across captured sinks; preserve setup/provider Exception and
TypeError containment, success redirect/raw inputs and ordinary noncallback
failure behavior. Equal production runtime inputs need one actual sequence;
dev's mutable checkout remains separately bound before any later real acceptance.
Retain the existing bounded waits, first-failure reporting and owned-effect
reconciliation contract. No canceled app rebuild, broad OAuth/browser campaign
or production action is added. Rollback remains the recorded system generation;
reverting these policies can reopen log exposure, without changing persisted
state, protocol, client configuration or sessions.

## Historical source facts and original package detail

KB/Discourse content below records the canceled design and evidence only.
PHP controls remain applicable where consistent with the current boundary above.

| Client | Actual callback and transport | Application/error facts relevant to the plan |
| --- | --- | --- |
| PHP | `https://vpsadmin.vpsfree.cz/?page=login&action=callback`; maintenance `vpsadmin-admin.vpsfree.cz` shares the prod webui backend. Edge nginx → webui HAProxy → backend nginx → PHP-FPM. | `webui/pages/page_login.php:41–63` catches ordinary token-exchange exceptions and displays a generic message; it does not log that exception. PHP-FPM enables error logging and captures worker output (`nixos/modules/vpsadmin/webui.nix:216–228`). Other application exceptions are not covered by the callback catch. |
| KB, cz + org | `https://kb.vpsfree.cz/doku.php` and `https://kb.vpsfree.org/doku.php`, with code/state query. Edge nginx → internal nginx → PHP-FPM/DokuWiki. No Varnish or HAProxy in this callback route. | Exact oauth `helper.php:38–44` returns `DOKU_URL . DOKU_SCRIPT`; core `inc/init.php:149` defines `doku.php`. `OAuthManager.php:50–87` reads code and normally redirects to the saved page; missing session/error cases may render at the callback URL. `auth.php:50–53` catches OAuth exceptions; `helper.php:111–133` displays their messages, with traces when allowdebug is on. Core ErrorHandler logs uncaught messages/traces; Logger exposes `LOGGER_DATA_FORMAT`. |
| Discourse | `https://discourse.vpsfree.cz/auth/oauth2_basic/callback`; failure continues through `/auth/failure`. Its own nginx → Unicorn/Rack/OmniAuth. | Exact plugin README and strategy define the callback. The OAuth strategy and user-info fetch log raw exception messages even with debug off. Debug mode additionally logs request headers/body and token/user responses. Rails' selected filter list lacks code/state; Logster copies params except password and retains REQUEST_URI/Referer. Rate-limit warnings also use raw REQUEST_URI. |

The PHP development alias `vpsadmin-dev.vpsfree.cz` uses the same common WebUI
configuration, shared auth origin and its own HAProxy instance. Include its
proxy/backend logging configuration in the PHP package, without changing the
mutable application checkout on that host. Its actual application revision is
an acceptance-time input, not inferred from33d6.

Additional exact references: configuration `common/frontend.nix:214–237,320–339`
selects PHP HAProxy instances; `common/webui.nix` is the shared backend site
configuration. `containers/prg/proxy/config.nix:138,258–267` selects combined KB
logs. KB config `containers/int.kb/config.nix:16–75,220–277` includes Matomo
`trackPageView`; a callback document must not report its full URL to analytics.
DokuWiki `inc/actions.php:23` uses strict-origin-when-cross-origin, which still
allows full same-origin Referer URLs. Discourse anchors are
`plugins/discourse-oauth2-basic/lib/omniauth/strategies/oauth2_basic.rb:27–43`,
`lib/oauth2_basic_authenticator.rb:197–239`, `lib/oauth2_faraday_formatter.rb`,
`config/initializers/filter_parameter_logging.rb`,
`lib/middleware/request_tracker.rb:520–544`, and
`lib/discourse_logstash_logger.rb:38–45,80–99` within its pinned source.

## Intended controls and diagnostics

1. **Proxy access logs:** retain method, path without query, status, byte count
   and supported timing/upstream-status fields. Omit raw request target/query,
   Referer, User-Agent and arbitrary request/response headers or bodies. Standard
   combined logs currently expose query and selected headers; this is not a claim
   that they automatically record Cookie, Authorization or response headers.
2. **Proxy error logs:** nginx has no equivalent per-value error-log redactor.
   Suppress raw error output for the explicitly selected client virtual hosts,
   including their HTTP redirect servers, while retaining the safe access/status
   records, service startup failures, health checks and application diagnostics.
   This deliberately loses detailed nginx error messages for these sites. Do not
   disable nginx logging globally or claim pre-vhost/TLS-parser errors are covered.
3. **PHP scope:** the callback is selected by query at the ordinary root and
   internally becomes index.php. A new path or a query-matching location is not
   needed. Use the safe access format across each PHP virtual host and suppress
   its nginx error output; this also prevents later same-site asset requests from
   logging a callback Referer. Set existing
   `vpsadmin.haproxy.webui.{prod,dev}.logRequests = false`; retain metrics and
   nginx status/timing records. No Varnish change is needed for client callbacks.
4. **Headers and redirects:** preserve original OAuth inputs, Cookie,
   Authorization, request bodies, Location and Set-Cookie on the wire; protection
   concerns their logging. Never strip auth/CSRF inputs to make a test pass.
   Retain hostnames, aliases, backend choice, maintenance behavior and ACME.
   As in249f, replace automatic forceSSL redirect servers only where necessary
   with explicit HTTP redirect vhosts carrying the same scoped log policy and
   shared certificate/ACME settings. Keep the original redirect destination/query.
5. **Referrer:** use an effective `Referrer-Policy: strict-origin` on participating
   callback documents/redirects, including errors, after resolving duplicate
   upstream headers through ordinary nginx interfaces. It prevents full callback
   URLs becoming Referer while retaining an origin for legitimate form guards.
   Do not use no-referrer blindly or change React. Header protection does not
   stop JavaScript from sending location.href; separately suppress KB analytics
   on callback/error documents until the URL is clean.
6. **Application logging:** preserve useful severity, operation, fixed error
   category, source location and status where available. Do not retain raw
   exception strings, parameter dumps, provider bodies or HTTP headers for the
   protected OAuth flow. Avoid a global logger replacement, token-regex scrubber,
   provider rewrite, new middleware framework or disabling every application log.

Use one small site-owned nginx configuration fragment for the common safe format
and log directives where needed across hosts; callers explicitly select vhosts.
Do not refactor React or duplicate the reviewed API/provider machinery. Check
nginx inheritance and internal redirects, not just the text of the new fragment.

## Released implementation boundaries

**P1 — implementer1, site proxies and configuration integration.** Own
`cluster/cz.vpsfree/vpsadmin/common/frontend.nix`, `common/webui.nix`,
`cluster/cz.vpsfree/containers/prg/proxy/config.nix`,
`containers/int.kb/config.nix`, `containers/discourse/config.nix` and the small
shared fragment `configs/nginx/oauth-client-logs.nix`, `overlays/packages.nix`, and
integration checks under `tests/oauth-client-log-protection/`. Apply edge and backend policy together, covering PHP
prod/maintenance/dev, both KB names and Discourse HTTP/TLS. The existing249f
HAProxy option is the supported seam. Reuse normal nginx vhost/location options;
do not copy an nginx module. Keep static/media/cache rules and ACME locations.

**P2 — implementer2, only `packages/dokuwiki-oauth-log-protection/**`.** Put
source, any narrowly required patch and focused tests inside this directory;
do not edit shared configuration or run Git mutations. `default.nix` must be
callable by `pkgs.callPackage` and return a normal DokuWiki plugin derivation
with installation name `oauthlogprotection`, suitable for the existing
`services.dokuwiki.sites.<site>.plugins` list. Use existing PHP/DokuWiki tools;
do not package a new runtime dependency. Report PHP/pool settings and any required
core/plugin patch wiring to E1 rather than changing those files. Pin the existing
`allowdebug = 0` explicitly for both sites and retain ordinary useful error logs.
Use the existing per-site `phpOptions`/pool options for production error display
and `zend.exception_ignore_args`, preserving diagnostics outside the OAuth flow.
The callback's normal OAuth catch currently displays, rather than logs, its error;
do not invent a leak at that catch. Uncaught callback/provider failures require
categorical logs with safe source location and no raw details/trace. The selected
early-logging remedy below supersedes the initial event-hook-only candidate.
E2's actual pinned-handler sentinel check confirmed native duplication for
E_USER_WARNING/E_USER_ERROR; hidewarnings only covers E_WARNING. The selected
remedy is a callback-only `bootstrap.php` exposed from this plugin package through
the existing per-site PHP `auto_prepend_file` directive. Classify sensitive
requests from parameter **presence**, including malformed/empty/array callback
keys; never inspect/log their values or alter request data. Set native log_errors
off only for that request before DokuWiki bootstrap, verify the setting took
effect, and preserve normal-request native logging. Do not replace ordinary
error handlers or return handled for E_USER_ERROR: fatal termination must remain.
A small shutdown callback may emit a fixed fatal category for failures before
DokuWiki's handlers exist, never raw error_get_last message/trace/request data.

The event hook is also too late for core Logger calls before EventHandler exists.
E2 therefore owns `dokuwiki-callback-logs.patch` in its package directory: put the
same marker-guarded categorical message/details handling at the existing
`inc/Logger.php::log` entry, before event/default formatting. This supersedes a
redundant action-plugin log filter; it is not a replacement logger. E1 applies
the carried patch through each site's ordinary DokuWiki package override while
preserving the selected source and all existing patches/plugins. E2's default.nix
still returns the installable plugin package containing bootstrap.php; E1 wires
the additional source patch and prepend path. No additional dependency is needed.

The policy begins at auto_prepend execution. PHP engine/request-startup failures
before any user code remain an explicit residual, like pre-vhost proxy failures;
do not silently disable all pool logging to claim otherwise. Later isolated FPM
acceptance must check native file/syslog/FastCGI stderr transport and representative
early malformed-input failures. Evidence of sensitive output before prepend goes
to the lead for a bounded policy revision, not a waived test. CLI proof alone is
not FPM proof. The existing manual fatal HTML is separate from logging:
display_errors does not suppress it; do not claim it does or broaden this into a
general error-page rewrite. Keep unrelated warning handling intact.
Ensure callback/error documents do not send full query URLs
through the existing Matomo injection; prefer skipping that pageview until clean
navigation, rather than changing analytics for normal wiki pages. Keep registered
redirects, state validation, local/wiki login and content unchanged.

**P3 — implementer3, only `packages/discourse-oauth-log-protection/**`.** Put
source, any narrowly required patch and focused tests inside this directory;
do not edit shared configuration or run Git mutations. Preferred wiring is a
normal `discourse.mkDiscoursePlugin` derivation returned by `default.nix` through
`pkgs.callPackage`, with name `discourse-oauth-log-protection`; E1 adds it to
the existing `services.discourse.plugins` list. The preflight selects a combined
plugin plus owned `patches/discourse-oauth-logging.patch` interface. Exact pinned
`config/application.rb:218` activates plugin.rb before Rails initializers, so
logging-copy adapters can install there before requests. The two raw OAuth
warning expressions, debug formatter/log sites and scoped rate-limit URI
arguments are patched at their owning source; do not copy authentication methods
or intercept Rails.logger globally. E1 sets the per-service package to
`pkgs.discourse.overrideAttrs (old: { patches = (old.patches or []) ++ [
  <owned-package-directory>/patches/discourse-oauth-logging.patch ]; })`
and separately retains/appends the site plugin list. This is conventional package
wiring, not a new overlay or gem override. Preserve src/version/inputs, existing
patches and the module's plugin merge; prove both survive the final effective
package selection. Pinned nixpkgs `discourse/default.nix:476–570` applies patches
then copies that application tree, including the built-in OAuth plugin, into
`share/discourse`; the separate asset output does not replace these Ruby files.
No parallel assets/dependency patch is justified by this logging-only change.
Use normal per-service package override/site-plugin packaging in the configuration repo;
keep the existing signup-policy plugin separate and unchanged. The concrete
changes are OAuth parameter filtering (code, state, tokens, secret, verifier and
callback error payload), removal of raw exception messages from the two OAuth
failure logs, and query-free rate-limit logging for the affected auth paths.
Logster2.21's `Message.populate_env_helper` needs sanitized *logging copies* of
params/REQUEST_URI/Referer; its current scrub_params only fixes string encoding.
Cover the separate Logstash web-exception serialization if enabled. Use a small
component-local initializer or narrowly carried package patch at these exact
sinks; no global gem override or copied logger. E3 owns the initialization preflight and must
confirm the earliest supported initialization/patch seam and exercise both
ordinary and exception logging before calling this closed. Rails filters alone
are insufficient. Set the `oauth2_debug_auth` default false and make its existing
formatter/user-info debug calls retain only safe operation/status information:
Nix siteSettings is UI-overridable, so the default alone is not a lasting guard.
Do not infer or change the live DB setting now. Include `/auth/failure` and
rejected/rate-limited callbacks, preserving state/CSRF and current GitHub login.

**P0 — minimal PHP callback fix, implementer0.** The conditional gate is concrete:
`oauth-client-logs/php-callback-gate-v2/result.json` shows provider Exception
handled with generic output/exit0, but setup failure and provider TypeError
exit255 with the synthetic detail in native output. Retain the original
missing-gettext fixture attempt. This establishes a callback-boundary defect,
not a live disclosure.

A0 creates/registers NEW `vpsadmin-oauth-client-logs` worktree and branch
`2026-10-24-vpsadmin-haveapi-upgrade-oauth-client-logs` from published
`a089b530376ca645456597df6a3533f720d24670`, preserving that default-spec successor
and frozen33d6/update3922/rollback refs. Own only `webui/pages/page_login.php` and
NEW `webui/tests/Regression/OAuthCallbackErrorHandlingTest.php`. No helper,
framework, dependency, Composer/vendor, lock/pin, translation or API change.

Move setupOAuth2ForLogin and provider lookup into the existing code-bearing GET
callback try block; catch `\Throwable` there instead of Exception. Keep
requestAccessToken then loginUser order and the exact existing translated generic
error response. Emit one fixed category through ordinary error_log, such as
`vpsAdmin OAuth callback failed`, without exception message/trace or request,
header, response or token data. Leave login initiation, logout/switch, the no-code
provider-error branch and unrelated errors unchanged. Add no session reset,
state/PKCE cleanup, redirect/status change or success marker; the provider/login
implementation continues to own those. This covers setup through loginUser in
that callback block, not earlier PHP bootstrap failures.

Use existing process-isolated PHPUnit style to include the actual page with
synthetic API/provider/template stubs and a real temporary PHP error_log. Cover
setup failure, provider-lookup failure, ordinary provider Exception, TypeError/Error
and loginUser failure: generic response, exactly one fixed category, no sentinel
in native log/stdout/stderr, and no later success call after earlier failure.
Success proves unchanged call order, code/state/session inputs and redirect
destination. A redirect fixture must use normal return/exit control flow, not an
exception newly caught by the product. Confirm no-code behavior unchanged and
noncallback failure still propagates with ordinary diagnostics; do not disable
logging in the tests.

Quick checks in the declared webui shell: PHP syntax for both files, new regression
plus existing LoginRedirectTarget/LogoutExpiredSession regressions, ordinary WebUI
PHPUnit suite and normal hooks. Existing phpunit.xml.dist discovers this path;
existing CI maps page_login.php to webui-auth/auth and excludes test-only files
from native selection, so no selector/workflow edit is needed. Preserve those
rules. No native34/API/core/provider audit or duplicate browser campaign solely
for this PHP change. After quick success: independent affected product/security/
test-correctness and complete-history/no-migrations review, then normal feature
publication. Prior default-spec review/checks retain only their actual unchanged
scope; include a089's supported history in the complete-range inventory.

E1 then selects exact published P0 through the normal confctl vpsadmin services
channel in ONE final generated input update, preserving unrelated pins/follows.
Configuration final all-source/history review precedes its targeted builds and
installed-stack PHP callback checks, which must bind the new package/system
identity. Do not relabel33d6/a089 outputs as P0 proof. P1/P2/P3 continue independently;
only final channel selection depends on P0 publication. Production acceptance,
deployment and default integration remain separately unapproved.

All three use the ONE new worktree after E1 supplies its verified identity.
E1 alone owns its Git/index/ref mutations, hook setup, wiring and coherent commits;
E2/E3 edit only the disjoint package paths above and hand over path lists, focused
check evidence and remaining limitations. They may read the shared source and
run isolated quick checks but must not stage, commit, rebase or run mutating
repository-wide hooks. E1 coordinates final formatting/hooks after handover.
Parent-owned operational prose is wired/committed by E1 after the parent supplies
it; application owners do not author a competing guide. P0 is the separately
released PHP product package above; further product scope returns to the lead.

**Shared fragment contract (E1):** `configs/nginx/oauth-client-logs.nix` is a small
Nix attribute set of strings, not a new module/options framework. `httpConfig`
declares the safe access format once per nginx instance; `serverConfig` selects
that access format and scoped error suppression; `referrerConfig` emits the
strict-origin response header. E1 applies these only to the explicit client
vhosts and their HTTP redirects, resolving proxy/FastCGI duplicate headers and
location inheritance at the call sites. No global enable, request-header rewrite
or React/API refactor belongs in it. P2/P3 do not import this fragment: E1 owns
all nginx/FPM/config wiring. Existing selected-source snapshots under
`oauth-log-source-inspection/` remain read-only evidence.

The P2/P3 preflights are delegated parts of their complete execution packages,
not new per-command approval gates. They may settle ordinary details and add
focused synthetic regression checks autonomously. A need to disable unrelated
application logs, change auth inputs, replace a logger/provider, update a
dependency or cross an assigned file boundary is a material deviation for the
lead. A hook-only KB result must not be called complete until native duplicate
output is resolved; a Rails-filter-only Discourse result is insufficient. E1
owns the conditional legacy-PHP escaping-error check; its concrete result releases
only P0 above. These preflights do not hold unrelated completed work.

## Verification and acceptance

Before edits, record the exact intended base/head and changed inputs; preserve
all current deployment/recovery refs. Only source-reading gates above remain;
do not launch a broader dependency or application audit.

Quick checks follow each owning repository's shell/hooks: syntax/format and
focused tests of the real callback/error/logging interfaces using synthetic
sentinel code, state, access/refresh token, client secret, Cookie, Authorization,
Referer, response Location and Set-Cookie. Assert controls leave the original
values available to auth and preserve success/failure status and redirects.
Cover missing/mismatched state, duplicate/malformed params, rejected code,
provider HTTP error/timeout, unexpected exception and Discourse rate limiting.
Assert no sentinel in the actual logger outputs, not merely a mock redactor's
return value; a benign unrelated request/error must retain useful diagnostics.

After all intended edits are committed and quick checks pass, run mandatory
independent affected source/security/history review. Inventory complete final
base-to-head ranges, pin/package streams and the migration lineage; expect no
schema/migration changes, and explicitly verify that conclusion. Retain old
published/deployed references; no default merge follows from review. This plan
itself requires no automatic review, commit or build campaign.

Then build only the affected systems through the configuration repository's
normal contract: `cz.vpsfree/containers/prg/proxy`,
`cz.vpsfree/vpsadmin/int.webui1`, `int.webui2`, `int.webui-dev`,
`cz.vpsfree/containers/int.kb`, `cz.vpsfree/containers/discourse` (expand full
paths, not an unbounded wildcard). Inspect the generated effective nginx and
HAProxy configuration and runtime PHP/application logging settings. Check every
HTTP/TLS/name/maintenance/internal-redirect path, ACME challenge handling,
upstream/socket selection, log inheritance and unchanged React/API behavior.
Use a focused isolated installed-stack fixture with the same nginx/FPM/Rack
configuration and a synthetic OAuth responder to inspect actual scoped access,
error, app file, journal/stderr and Logster outputs. Exercise response-header and
provider-body failures as well as successful callbacks. No full cluster/client
matrix or unrelated API34 rerun is implied unless affected repository rules or
changed inputs require it. Long/uncertain checks use the normal watcher policy.

Only later, after separate authorization, use controlled real login/logout and
bounded nonsensitive log-presence/absence checks. Bind source/config/output
identities and inspect the effective debug setting without collecting private
values. Confirm PHP prod/maintenance/dev as applicable, KB cz/org and Discourse;
retain React's existing evidence where inputs remain unchanged. Synthetic proof
does not claim historical or production absence of disclosure.

### Postreview execution split (E1/E2/E3)

Launch condition is the lead's release of the final committed configuration
head after its all-affected/history review, including the published/reviewed P0
pin. No launches during source assembly. This section is an execution refinement,
not another source/test framework. Preserve existing quick evidence, including
P2's ten native CLI cases, P3's source-sink fixture, P1's nginx/Matomo checks and
P0's reported focused16/full116 results; they do not establish installed behavior.
All runtime fixtures and evidence go outside product source under distinct
`oauth-client-logs/postreview/{systems,php,discourse}/<attempt>/` directories.
Keep old attempts, commands, statuses and unfinished effects identifiable. E1 is
still the only configuration Git writer; no owner edits frozen product/store
files to make verification pass. Scratch configs/drivers may adapt existing test
interfaces, with their exact changes recorded; a required product correction
returns to the source owner and affected review before the relevant retry.

**E1: six systems, generated configuration and output handoff.** From the exact
reviewed configuration checkout use its normal `nix develop` environment and
`confctl build <target>` once for each exact target listed above. Do not deploy,
dry-activate or run any generated production preStart script. Use the admitted
bounded build settings, not six independent competing build trees. Keep normal
substitution/build behavior; no arbitrary80GiB/no-new-build guard. The six-output
set is the milestone, not six successful command exits without identities.

For each target record selected configuration SHA/tree, final P0 and complete
locked input graph, top-level derivation/store output, build command/status/log
and the graph of realized dependencies (`nix path-info --json --recursive <out>`
and `nix derivation show --recursive <drv>` or the same existing receipt commands).
Use actual output symlinks/service ExecStart arguments and selected evaluation
results to identify the effective nginx/HAProxy config, nginx binary, PHP-FPM
binary+ini+pool config for each PHP/KB instance, installed PHP WebUI root/vendor,
combined DokuWiki roots/bootstrap/config paths for both sites, and Discourse
app/plugin/rubyEnv/runtimeEnv plus PostgreSQL/Redis outputs. Report specific paths,
not guessed hash prefixes. Preserve the existing root retention procedure.

Inspect generated config for every HTTP/TLS/name/alias/maintenance/internal
redirect path, ACME precedence, safe access/error inheritance, one effective
strict-origin header, API249f protection and unchanged React. Bind P0's installed
page_login bytes and P2/P3 installed patch/plugin bytes to the reviewed sources.
Check that service plugin merging has not lost the Discourse override. In a
private fixture, use the selected `nginx -t/-T -c <fixture-config> -p <scratch>`
and `haproxy -c -f <fixture-config>` with recorded path-only adaptations for
certificates, sockets, logs and local listeners; syntax evidence for an adapted
config is not a claim that production credentials were read. Existing
`tests/oauth-client-log-protection/nginx.py --nginx <selected-bin>
--fragment-values <final-evaluated-json> --output-dir <fresh-run>` is reusable
only where final fragment/binary inputs changed; do not repeat the prior quick
run merely to rename it installed-host proof. Its synthetic responder is the
existing wire/log oracle; generated whole-host topology is the separate proof.

Give E2/E3 their realized subset as soon as available with this identity/config
receipt; they need not wait for unrelated targets. Final acceptance still needs
all six. E1 also supplies a byte comparison of the two PHP production backends
and both KB configurations so equal runtime binaries need not be exercised
twice; differing prepend/template/pool/site settings must each be checked.

**E2: installed KB transport and smallest installed P0 fixture.** Use the exact
PHP-FPM/nginx/built application outputs from E1, not ambient PHP or repatched
source. Start a foreground owned FPM using its ordinary interface:
`<php-output>/bin/php-fpm --nodaemonize -y <scratch-pool.conf> -c <selected-php.ini>`.
Copy only generated pool configuration for isolation: owned pid/listen/log paths,
fixture uid and bounded workers. Preserve logging/catch_workers_output settings,
extensions, auto_prepend and security options; record each adaptation. Connect
through the selected nginx FastCGI configuration on a private socket/loopback.
Retain actual FPM master/worker stdout/stderr, nginx FastCGI errors, wiki logs and
native PHP logs. Syslog output must go to an owned datagram collector on a private
`/dev/log` inside an unshared mount/network namespace; never the host syslog.
If the ordinary namespace facility is unavailable, report it before launch;
do not redirect a real host socket or silently drop the syslog acceptance.

Reuse the P2 `tests/request.php` cases through a small scratch FastCGI bridge,
pointed at the installed combined wiki and its already-patched Logger. Do not
rerun `tests/run.py` against/repatch an installed output. Feed actual HTTP/FastCGI
query/header inputs, rather than pretending CLI-populated superglobals prove
SAPI behavior. Also make one real installed doku.php bootstrap with disposable
wiki/session/data and synthetic OAuth config to establish effective prepend,
callback handling and JS+noscript Matomo absence; repeat the two site's rendered
configuration distinction. Cover native warning, user warning/error, early
exception/fatal, rejected/missing/array/duplicate callback keys and native-policy
unavailable. An ordinary request must retain useful native/wiki diagnostics;
same-worker callback→ordinary must restore the ordinary request's log settings.
Capture known fatal HTML separately: its unchanged message is not falsely counted
as a log failure or claimed sanitized. Test representative pre-prepend malformed
requests; a sensitive log there is an explicit unresolved result, not a waiver.

For P0 use the installed WebUI page_login from E1 with the reviewed PHPUnit case
logic adapted only as a scratch request bridge, running under its actual FPM
ini/pool. Exercise setup/provider Throwable, ordinary provider Exception and
success redirect, plus a noncallback failure control; capture native/FastCGI/
worker/syslog outputs. Stub only the provider/API responses with public sentinels;
do not copy/alter the product page. This supplies installed-output/transport
proof without another whole WebUI/API/provider matrix. The mutable PHP dev-host
checkout is not asserted equal to P0: verify its generated log policy, and retain
its source-binding prerequisite for any later authorized real acceptance.

**E3: installed Rails/OmniAuth boot and sink sequence.** Use E1's exact app,
rubyEnv and runtimeEnv in a private mount/network/process namespace with the
store read-only and fresh writable `/run/discourse`, `/var/lib/discourse`,
`/var/log/discourse` and fixture home. Prepare runtime config from that app's
`config.dist` with synthetic hostname/client/key and owned database/Redis paths;
no private production config or service preStart. Start the selected PostgreSQL
with `initdb -D <scratch-data>` and `pg_ctl -D <scratch-data> -o <private-socket-options> start`,
and Redis with `redis-server --port 0 --unixsocket <owned-socket> --save ''
--appendonly no`. Keep their listeners and data private to this attempt. Populate
only the disposable schema required by normal Discourse boot, using the installed
Ruby/Bundler in `<app>/share/discourse`; no production DB helper or seeds.

Run ordinary `bundle exec rake db:create db:migrate` only against those synthetic
settings if needed, then `bundle exec ruby -r ./config/environment <scratch-driver.rb>`
with production logging settings. Use the bundle executable from E1's rubyEnv.
Do not assume the passthru `discourse-rake` wrapper follows overrideAttrs: the
selected nixpkgs wrapper embeds its source Rakefile path. Record `$LOADED_FEATURES`,
Ruby method source locations, actual plugin inclusion, logger classes and settings
to prove the patched final app was loaded before assertions. The scratch driver
uses real Rails/Rack/OmniAuth and real Logster/Redis, not the source fixture's Rails,
Rack or store doubles. Reuse its sentinel cases/assertions, injecting only a local
synthetic provider transport. No need to start extra Puma/Unicorn workers for this
in-process Rack proof; nginx topology is E1's responsibility.

Exercise rejected/missing state, provider error/timeout, debug off/on, unexpected
exception and rate-limit diagnostics, plus a successful synthetic callback/control.
Collect actual Rails file/chained stderr, Logster Redis records and Logstash
serialization when enabled, then compare original request/header/session values
to show sanitization changes logging copies only. Test an ordinary request after
the callback in the same thread and preserve benign diagnostics. Any additional
enabled sink discovered at boot is assessed narrowly before claiming completion;
do not replace an unavailable sink with a mock and call it installed proof.

**Batch limits and completion.** E1 expects output/config progress at each target;
report the first concrete build/evaluation failure without automatic retries.
E2/E3 first milestone is an identity-bound daemon/boot-ready receipt, then one
bounded sentinel batch. Reassess after30 working minutes without that milestone
or60 minutes without a result, identifying the exact blocker and smallest next
step; these are reporting checkpoints, not kill timeouts. Bound individual local
HTTP/FastCGI/provider waits (normally5–10s) and record deliberate timeout tests.
Stop the relevant batch on a credential-bearing sink, wrong loaded source,
unexpected external connection, auth-input mutation or product defect. Do not
continue broadening tests to compensate. Use normal exact-owned-process shutdown
and report process/socket/state reconciliation; no session/cluster lifecycle
operation or cross-owner cleanup. Builds are not killed merely for silence.
Known watcher840 is unavailable: use the documented visible owner-monitoring
fallback once, retaining handles/log/status; no repeated watcher setup attempts.
Do not poll another owner's operation. Parent owns acceptance/retry decisions.

Completion receipts distinguish source quick tests, generated configuration,
installed fixture behavior and still-unperformed production acceptance. No
native34/provider/browser replay, CI campaign, real client creation/login,
production access, existing-cluster action or deployment is added by this split.

## Deployment, compatibility and rollback

The shared-server249f protection (or reviewed equivalent) and client protections
are complementary dependencies for a complete result. Prepare/build all outputs
before an authorized rollout. Prefer edge/HAProxy safe logs first, then PHP/KB
backend/application protection, then Discourse's combined host/application
generation. Keep partially protected phases short and report them honestly;
do not declare the end-to-end flow protected until every hop passes. Use ordinary
confctl deployment/health checks, with exact prior system generations recorded.
No token/client/secret/session-key regeneration or callback-registration change
is expected; sessions, content, DB schema and credentials remain compatible.

Rollback each changed system/package through its recorded generation and restore
only the affected configuration. Prefer retaining independent proxy protections
when reverting an application patch. Reverting a log policy can reopen that sink;
state this explicitly. There is no retrospective log deletion or rotation plan:
actual exposure would require separate evidence and an authorized response.
Implementation, real acceptance/deployment and default-branch integration have
separate authorization boundaries; none is supplied by this plan-only request.

## Read-only source provenance and limits

Pinned sources absent from the local store were downloaded only for inspection
under `oauth-log-source-inspection/`, without build/eval/install/Git/ref changes.
Both GitHub plugin archives matched the configured recursive source hashes:
oauth d9f53e6a → `sha256-jyyKEhKp6LyHIq8vmaS1WOc+uyNxwHMt0kmSTSuOGKo=`;
oauthgeneric602a0fb6 → `sha256-fVsAczzl0PCUT6J/SAZjtfx++GDJBEknv9W9vFt4Kf8=`.
The first Discourse tag archive did not match the selected hash and was not used
as exact evidence. The pinned source was then downloaded from its Nix cache NAR
and restored only into the session inspection directory; its recursive hash is
`sha256-j3JjLYNcv3lluoCekyUUKMfkSX/ExeDsa8zrQ+pDrwg=`. DokuWiki core likewise
matches `sha256-84kMuFTWYo6Cjd6qpkZsLZoECIP9IzSrc9dX1uKMp0M=`. The one Logster
source gem matches Discourse's locked SHA256
`5edc71ea98d5f89fe081556893f77b7c4d2617341dae7d421fc37539cfb13a02`.
Raw downloads are disposable untracked evidence, not project deliverables.

No production/live requests, logs, registered client records, secrets, browser
runs, tests or builds were accessed/run. No existing operation was interrupted.
This is a source-backed plan, not a finding of actual disclosure or a new incident.
