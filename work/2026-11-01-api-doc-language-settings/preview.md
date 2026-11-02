# Temporary API documentation preview

Status: final verified preview running. The lead released the final refresh
after independent review, exact-head local checks and all 11 applicable hosted checks passed.
Leave the preview running for user review. The session remains open.

Final reviewed head `eb91a4d031c2c1f1c6ec6dd1aaed62e1f320eea7`, tree
`d6b39fec8fe094471b47ac9054d890df6abf767c`, is now live from its isolated export.
See the [asset-cache live receipt](preview-cachefix-live.md) and
[current exact runtime identity](preview-cachefix-live-runtime.json).
[Cache-fix candidate receipt](preview-cachefix-candidate.md) retains preparation
evidence; prior [ef4 live](preview-nov2-live.md) and [51047 live](preview-final-live.md)
receipts remain recovery records.

Meaningful same-context warm-cache acceptance passed: old stable 51047 JS/CSS
were reused, then genuine live HTML fetched both new content-digest URLs without
hard refresh. Direct reported URL Go/HTTP controls are hidden in en/cs with zero
geometry; native Go/HTTP Apply retains one detail scalar and query/locale. Ruby
two choices return. The English sidebar label is Language; Czech remains Jazyk.
[Warm-cache/direct-state evidence](preview-cachefix-warm-live.json).

Nov 2 refinement checks passed on candidate and live: singleton detail label/
select hidden while native form retains one scalar, two→one→two visibility keeps
saved Thorough, and Ruby Thorough loads its client once before `begin` with setup
inside. Separate exact-source signed-in OAuth fixture DOM evidence confirms
Switch user before Sign out when supported, preserving POST/CSRF fields.
[Refinement evidence](preview-cachefix-refinements-live.json).

Native example-selection browser acceptance passed on the loopback candidate
and the live URL. With JavaScript disabled, resource and authentication pages
support language Apply, client/detail Apply, real generated TypeScript and Go
singleton client/detail values. Page/resource, `q` and explicit `doc_lang` survive
submission. Selected code is open; alternatives start collapsed and their native
summaries can open them. When the current client has a singleton detail (such as
the authentication callback client), Apply the new client first to obtain its
available detail options, then choose the detail and Apply again.

With JavaScript enabled, explicit Rust/blocking/simple URL selection overrides
stored Python/thorough on load without changing storage. Both Apply buttons are
hidden; example language/client/detail changes update immediately without
navigation. The translated Ruby token comment remains present. Current receipts:
[native live check](preview-cachefix-native-live.json),
[native candidate check](preview-cachefix-native-candidate.json),
[UI live check](preview-cachefix-ui-live.json),
[exact source](preview-cachefix-source.json).

Two initial smoke-script assumptions needed correction: opening an alternative
changed which element matched a dynamic `:not([open])` locator, so the script
now retains its ID; the authentication singleton requires a client Apply before
choosing a new detail. The corrected native candidate/live runs passed. Neither
required a product change.

URL: <http://aitherdev.int.vpsfree.cz:4567/v1.0/>.

Current source: isolated Git export of
`eb91a4d031c2c1f1c6ec6dd1aaed62e1f320eea7` at
`work/2026-11-01-api-doc-language-settings/preview-source-eb91a4d0`.
All 933 exported Git blobs match the commit, with zero missing/mismatched files.
The preview remains on this verified revision while the feature worktree changes.
No application source or Git/index mutations were made by this package.

The final committed source includes native example selection, complete translated
example comments/generated prose, select-only language UI, Czech breadcrumb CSS,
Jazyk label, overview wording and static memo changes. No worktree-uncommitted
inputs are loaded. Repository integration status is owned by the lead; this
receipt proves the final preview runtime and its acceptance checks.

Translated-comment browser checks passed on the loopback candidate and live URL
in both locales. Ruby token authentication includes
`# Použití existujícího tokenu` in Czech. Go token comments, Rust Async/Blocking
comments/notices, and TypeScript package/context notices and generated labels are
localized. Command/package literals remain unchanged; after excluding prose
comment lines, the five token-auth executable snippets are identical across
English/Czech. The representative TypeScript limitation is generic and localized,
without schema/sample names in its reason.

The limitation uses an inert example added only to protected Project::Create in
the session preload. The real generated profile is built from the anonymous
schema and does not represent that protected action; a fixture-authenticated
browser therefore sees the normal generic adapter limitation. Resource visibility
and API execution behavior are unchanged. Public Echo/EchoChoice samples still
render all three generated clients.

Earlier d7 evidence: [comment/code checks](preview-d7-comments-live.json),
[UI checks](preview-d7-ui-live.json),
[generated-profile checks](preview-d7-generated-live.json),
[exact source](preview-d7-source.json).
Direct Czech comment review:
<http://aitherdev.int.vpsfree.cz:4567/v1.0/?page=authentication&doc_lang=cs>.

Actual Chromium checks passed on loopback before the authorized replacement,
then again on the live URL:

- With JavaScript, the language select is visible and the Apply button has
  `hidden=true` and computed `display:none`; selection navigates immediately and
  preserves the fragment.
- Without JavaScript, Apply stays visible and native GET submission changes
  language while retaining the resource.
- Czech breadcrumbs have computed `display:flex`, `list-style-type:none` and
  horizontally aligned items. The example-language label is Jazyk.
- The edited overview has the API version/address, no standalone GitHub link and
  no permissions reminder. Intentional client-library documentation links and
  the HaveAPI footer remain.
- Go, Rust Async/Blocking and TypeScript API client all remain selectable with
  visible executable examples and initialization identities in English and Czech.

Earlier A2 evidence: [A2 browser](preview-a2-live.json),
[A2 generated profiles](preview-a2-generated-live.json),
[A2 exact source](preview-a2-source.json). The first candidate harness assertion
included the H1 permalink `#` in its expected title; excluding the permalink
corrected that assertion, and the full candidate/live checks passed. No product
source changed during verification.

Generated clients are now configured and visible on the public
[EchoChoice sample](http://aitherdev.int.vpsfree.cz:4567/v1.0/?resource=test#root-test-echo_choice):

- Programming language **Go**.
- Programming language **Rust**, client **Async** or **Blocking**.
- Programming language **TypeScript**, client **API client**.

Profiles use placeholder identities `example.test/preview/client`,
`preview_client` and `preview-client`. Nothing is published. Actual browser
checks passed all four selections with visible executable samples and all three
initialization identities in both English and Czech, first on the loopback
candidate and then on the live URL. Browser errors: none.
[Live profile evidence](preview-generated-live.json),
[candidate evidence](preview-generated-candidate.json),
[source/profile receipt](preview-profile-source.json).
Final profile evidence: [preview-cachefix-generated-live.json](preview-cachefix-generated-live.json).
Final comment/privacy/code evidence: [preview-cachefix-comments-live.json](preview-cachefix-comments-live.json).

Runtime identity:

- User service: `haveapi-doc-language-preview-20261101.service`.
- Ruby PID: `1688000`, listening on `0.0.0.0:4567`.
- Invocation ID: `3ba77a243dc247feb7e4b1e1a13afb38`.
- Refreshed: `2026-11-02 14:45:35 CET`.
- Log: [preview.log](preview.log); service stdout/stderr append to this file.
- Working directory: the isolated final eb91 source export above.
- Fresh final proof: service `active/running`; health `ok` both through the
  hostname and with the hostname resolved explicitly to LAN `172.16.106.40`.

The durable user service has no scheduled cleanup or stop action. Leave it
running for user review. No host/firewall/proxy/configuration changes were made.

The user explicitly requested generated clients in the preview. The lead
authorized the bounded preview refresh, with the existing live service retained
until the candidate passed. Earlier intermediate loopback candidates were stopped
after their replacements passed. At this final handoff, both the live service and
all loopback candidates remain running; no cleanup was performed or scheduled.
The old 51047 candidate is PID `29112`, invocation `4398ca8e9b6b4ffaa81e64947146bfdf`,
on `127.0.0.1:14567`. The Nov 2 candidate is PID `1339526`, invocation
`9ea3f8d382784e33ab4adb9e480c3657`, on `127.0.0.1:14568`.
The cache-fix candidate is PID `1615810`, invocation
`9c909eceefe0408fb251077c08886a2f`, on `127.0.0.1:14569`.
The preceding ef4 live service was PID `1487623`, invocation
`96e0ddd440174bf0a9461552b149f7a9`, started `2026-11-02 14:15:21 CET`.
Its exact export, [service definition](preview-ef4-service.txt) and
[preload](preview_profiles-ef4.rb) remain for recovery.
The preceding 51047 live service was PID `139933`, invocation
`0689ec0c763940f685fa8b97299e38e6`, started `2026-11-01 23:14:04 CET`.
Its exact source export, [service definition](preview-51047-service.txt) and
[preload](preview_profiles-51047.rb) remain for recovery.
The preceding ebc native service was PID `4037161`, invocation
`91d236936a5e464e9f1ce7714aeb8623`, started `22:39:32 CET`.
Its [service definition](preview-ebc-service.txt), exact source export and
[preload](preview_profiles-ebc.rb) remain for recovery.
The preceding d7 comment service was PID `3988350`, invocation
`b3c0b9a663964c45aa2d1b367dcb5d3c`, started `22:34:00 CET`.
Its [service definition](preview-d7-service.txt), exact source export and
[preload](preview_profiles-d7.rb) remain for recovery. The preload SHA-256 is
`b10a4863e2d119f5e5aa954b8279b808b5a40aa467827c0e776b9e855cc0828d`.
The preceding b3 UI service was PID `3903390`, invocation
`efcbdec36b294a22a763a43f7561130b`, started `22:21:02 CET`.
Its [service definition](preview-b3-service.txt) and exact source export remain.
For b3/e7 recovery use `HAVEAPI_PREVIEW_PRELOAD` pointing to
[preview_profiles-b3.rb](preview_profiles-b3.rb), retained byte-for-byte with the
original SHA-256 `792b68b87bb1c27334bdd4643afc558e47d1092711b69d8badc9b570da260dc2`.
The preceding e7 profile service was PID `3853175`, invocation
`3b91f74f079644b79ebe6dbf1e9b94a1`, started `22:13:18 CET`; its exact source
export and [service definition](preview-e7-profile-service.txt) remain available
for recovery with the same profile launcher. Original service identity was PID `3602829`, invocation
`c461dfe3db7b47b4b3062982c6c65bf4`, started `21:47:23 CET`.

Current launch payload is [preview_launch.sh](preview_launch.sh), using the
existing unbundled benchmark shell and prepared third-party gem home. It clears
Bundler through the declared shell and loads the five source component libraries
from the exact export. [preview_profiles.rb](preview_profiles.rb) adds the three
real profiles and the original scalar samples. Two association-specific test
actions reference protected Project metadata; their fixture authentication flag
is set to match that protection so the anonymous generator schema stays
self-contained. The public Echo/EchoChoice samples and protected Project/Task
behavior are retained. No dependencies were installed.

```sh
HAVEAPI_PREVIEW_SOURCE_ROOT=/home/aither/workspace/ai/vpsfree.cz/work/2026-11-01-api-doc-language-settings/preview-source-eb91a4d0 \
  /bin/sh /home/aither/workspace/ai/vpsfree.cz/work/2026-11-01-api-doc-language-settings/preview_launch.sh
```

Recovery contract: [preview-original-service.txt](preview-original-service.txt)
retains the original service definition and the original payload is recorded
below. To recover its fixture behavior from the exact e7 snapshot, the current
launcher accepts `HAVEAPI_PREVIEW_PRELOAD` pointing to
[preview_recovery_samples.rb](preview_recovery_samples.rb), which retains the
original samples without generated profiles. A runtime refresh requires its own
explicit preview authorization; this receipt does not authorize session lifecycle
actions. Any later source successor must be verified and exported explicitly
before another authorized refresh.

Original e7 language/navigation acceptance, before adding profiles:

- Actual Chromium 147.0.7727.15 with Playwright 1.59.1 passed Czech browser
  detection without saving a cookie, exact English/Česky options above Theme,
  real selector navigation, fragment/resource retention, manual cookie
  persistence across query removal and reload, and unsupported-language fallback
  to English.
- English and Czech reference → versions → protocol → reference navigation
  preserved the selected locale. Python example selection and its stored
  preferences remained unchanged across UI-language switches. The localized
  Echo description and Czech choice labels rendered correctly.
- Browser page errors and local HTTP responses at or above 400: none.
- HTTP passed 12 localized pages: versions, overview, authentication, Test
  resource, README and protocol, each in English and Czech. Manual language
  selection created a path `/` cookie which also selected the protocol locale.
  Mounted `/js/documentation.js`, `/js/highlighter.js` and
  `/css/documentation.css` all returned 200 with nonempty content.
- Browser evidence: [preview-browser-results.json](preview-browser-results.json).
  HTTP evidence: [preview-http-results.json](preview-http-results.json).
  Disposable browser script: [preview_browser_check.cjs](preview_browser_check.cjs).

The first browser run reached the protocol page but the smoke script incorrectly
expected “HaveAPI” in its H1. The actual headings are “Protocol definition” and
“Definice protokolu”. Correcting that harness assertion produced a complete
passing rerun; no product change was needed.

Access limit: this is an internal HTTP preview on the existing allowed
`172.16.106.0/24` and `172.16.107.0/24` routes. Same-host name/LAN requests and
the existing firewall policy were verified; a connection from the user's own
browser/network cannot be established from this session. CI is tracked separately
by the lead and is not part of this preview receipt.

Preparation checks: Ruby syntax passed and both current fixture action constants
accepted exactly one sample through their existing `example(title, &block)` DSL.
Fixture construction/mount passed without opening a socket. The first inspection
command used `size` on `ExampleList`; it exposes Enumerable `count` instead, and
the corrected inspection passed. No application changes were needed.
Both localized Echo descriptions also passed in-process HTML requests (HTTP 200,
English and Czech text present). Rack::MockRequest needs an explicit `HTTP_HOST`
for HaveAPI rendering. Sinatra's default development environment rejects the
external preview host with 403; using the existing `RACK_ENV=production` runtime
setting accepts it without changing source or host configuration. Both conditions
were applied in the passing check and are included in the launch approach.

The preview reuses `servers/ruby/test_support/client_test_server.rb` from this
session's HaveAPI worktree. [preview_samples.rb](preview_samples.rb) adds two
examples to its existing public Echo and EchoChoice actions. All state is
in-memory fixture data; no database or production credentials are used.
The same preload uses the existing `HaveAPI.message`/`I18n.store_translations`
application hooks for one Echo action description: “Return the supplied values.”
/ “Vrátí zadané hodnoty.” No framework catalogs or executable samples change.

Selected visual review pages:

- Overview: <http://aitherdev.int.vpsfree.cz:4567/v1.0/>.
- Samples and translated metadata:
  <http://aitherdev.int.vpsfree.cz:4567/v1.0/?resource=test#root-test-echo>.
- Authentication:
  <http://aitherdev.int.vpsfree.cz:4567/v1.0/?page=authentication>.
- Shared protocol: <http://aitherdev.int.vpsfree.cz:4567/doc/protocol>.

Select English or Česky through Settings; use `doc_lang=en` or `doc_lang=cs`
in a direct link when a particular initial language is useful. Browser checks
must also remove that query override and prove the saved language persists.

Original service payload before the profile refresh, from
`worktrees/2026-11-01-api-doc-language-settings/haveapi`:

```sh
RACK_ENV=production HAVEAPI_RELEASE_TOOLS_ONLY=1 nix develop -c bash -c '
  export BUNDLE_GEMFILE="$PWD/servers/ruby/Gemfile"
  exec bundle exec ruby -Iservers/ruby/lib \
    -r /home/aither/workspace/ai/vpsfree.cz/work/2026-11-01-api-doc-language-settings/preview_samples.rb \
    servers/ruby/test_support/client_test_server.rb --bind 0.0.0.0 --port 4567
'
```

The declared root shell has already been prepared by implementer0. The
`HAVEAPI_RELEASE_TOOLS_ONLY=1` setting skips repeated dependency installation.
The server also needs the final `make doc` output already produced by the
implementation checks.

Planned URL: <http://aitherdev.int.vpsfree.cz:4567/v1.0/>. Port 4567 was free
during preparation. The selected host's existing firewall start script allows
this port from `172.16.106.0/24` and `172.16.107.0/24`; it is intended for the
existing internal network/VPN access. No host, firewall, proxy or configuration
changes are needed. Self-resolution of the host name is `127.0.0.2`; the host's
LAN address is `172.16.106.40`.

The public Test resource provides the examples and localized choice labels.
The fixture filters protected Project/Task documentation for anonymous readers.
Fixture-only Basic credentials are `user` / `pass` or `admin` / `pass` when
reviewing protected resources. The authentication reference documents Basic and
token methods; no production identity provider is connected.

Actual browser tooling is already present; read-only availability checks passed
without installing packages. Use
`/nix/store/l07gdbxylzfl8pbx9pxy6fyg95w4hjwy-nodejs-24.19.0/bin/node`
with Playwright 1.59.1 from
`/nix/store/fg778x0631ld4xd8fim2kbvxll5715xp-playwright-test-1.59.1/lib/node_modules/playwright`
and explicit `executablePath`
`/nix/store/1wah8z2gydp6d4yd3hz7xwakx3zkmzh7-playwright-chromium-headless-shell/chrome-headless-shell-linux64/chrome-headless-shell`.
The executable reports Chromium 147.0.7727.15, matching that Playwright package's
browser descriptor. Actual browser interaction passed as recorded above.

[Stable session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-01-api-doc-language-settings/).
