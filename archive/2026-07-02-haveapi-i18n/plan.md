# 2026-07-02-haveapi-i18n

## Goal

Add localization/i18n support to HaveAPI so API responses can use the
language requested by the client, with Czech as the first non-English target.
The first implementation target is the HaveAPI Ruby server. vpsAdmin API will
then consume the HaveAPI support and gradually translate its own messages.

## Latest Decision

Parameter labels and descriptions are localized by HaveAPI itself, not by a
vpsAdmin monkey patch. HaveAPI treats `parameter_i18n_scope` as the application
root, derives exact resource/action keys without an inner `parameters` segment,
and falls back through shared resource input/output keys, resource attributes,
and global attributes. Metadata parameters use exact, resource meta, and global
meta keys.

vpsAdmin sets the scope to `vpsadmin`, generates compact parameter catalog
entries from HaveAPI's in-process parameter metadata helper, and keeps
framework-owned HaveAPI parameters in HaveAPI locales instead of duplicating
them in vpsAdmin. This keeps the protocol unchanged and avoids copying every
exact action parameter path when a shared translation is enough.

Choice labels are also localized by HaveAPI parameter metadata, not by
application-level helper methods. Choices declared as maps keep their internal
values and receive localized labels in the existing `validators.include.values`
map. Choices declared as arrays stay arrays when untranslated, preserving the
old metadata shape, and are promoted to the existing `{value: label}` map only
when a locale supplies a label. Translation lookup uses the same fallback ladder
as parameter labels/descriptions with `choices.<value>.label` appended.

vpsAdmin consumes these labels from API metadata in the WebUI for outage,
transaction, and security-advisory states. The WebUI also gains generic plural
gettext helpers before Czech plural strings are added.

## Affected repositories

- `haveapi`
  - Ruby server framework response envelope messages.
  - Input validation and type coercion errors.
  - Default validator messages exposed in action self-description.
  - Authentication/token/action-state framework messages.
  - Protocol documentation and server specs.
- `vpsadmin`
  - Later consumer of the HaveAPI server feature.
  - Existing `Language` and `User#language` data can select a default locale.
  - Large number of application-level `error!` calls and ActiveModel validation
    strings will need an incremental migration, not a single large rewrite.
- `vpsf-status`
  - Consumes vpsAdmin outage reports and has its own English/Czech UI catalogs.
  - Outage report section headers should stay terminology-compatible with the
    vpsAdmin WebUI while using the status page's reported/recent sections.

## Later wording decisions

- Outage-list headers should use shorter parallel wording.
  - English uses `maintenance` for planned outage headers and `outages` for
    unplanned outage headers.
  - Czech keeps `odstávky` for planned outages and `výpadky` for unplanned
    outages.
  - vpsAdmin index page uses:
    `Upcoming maintenance`, `Upcoming outages`,
    `Upcoming maintenance and outages`, `Ongoing maintenance`,
    `Ongoing outages`, `Ongoing maintenance and outages`,
    `Recent maintenance`, `Recent outages`, and
    `Recent maintenance and outages`.
  - vpsf-status uses:
    `Reported maintenance`, `Reported outages`,
    `Reported maintenance and outages`, `Recent maintenance`,
    `Recent outages`, and `Recent maintenance and outages`.

## Approach

### Context found

HaveAPI currently exposes only strings in the public response envelope:

- `message` for action/request errors;
- `errors` as parameter-name to array-of-string validation messages;
- validator `message` strings in self-description.

The current protocol/schema already describes these as strings. Localization can
therefore keep the response shape unchanged.

HaveAPI framework strings are produced mainly by:

- `HaveAPI::Server` for routing, JSON/content negotiation, authorization, and
  request exceptions;
- `HaveAPI::Action#error!` and validation handling;
- `HaveAPI::Params`, `Parameters::Typed`, `Parameters::Resource`,
  `ModelAdapters::ActiveRecord::Input`;
- built-in validators and action-state/token resources.

vpsAdmin has existing language records and `User#language`, but most API errors
are direct English strings. Current counts from a quick grep:

- over 300 direct `error!` calls in vpsAdmin API resources/plugins;
- over 100 model validation custom messages via `errors.add` or `message:`;
- many messages interpolate object names, limits, or exception messages.

### Proposed solution A: HaveAPI i18n layer with unchanged protocol

This is the recommended approach.

- Add an explicit `i18n` dependency to the HaveAPI Ruby server gem.
- Add a small HaveAPI translation wrapper and bundled locale files:
  `en.yml` and `cs.yml`.
- Select a request locale from:
  1. an explicit request language header or standard `Accept-Language`;
  2. an application-provided resolver block that can inspect the request and
     authenticated user;
  3. server default locale, English by default.
- Normalize common language tags, e.g. `cs-CZ` to `cs`, and fall back to the
  default locale when unsupported or malformed.
- Run each request under the selected locale, e.g. through `I18n.with_locale`.
- Translate HaveAPI-owned framework messages at the point they are returned.
- Keep arbitrary string messages backward-compatible: existing `error!("...")`
  and validator `message: "..."` continue to pass through unchanged.
- Add a lazy message object or helper for framework/default validator messages,
  so validators initialized at boot can still render in the request locale.
- Add action/helper APIs for applications, for example:
  - `tr("vpsadmin.errors.access_denied", default: "access denied")`;
  - `message("vpsadmin.errors.limit", default: "...", limit: max)`;
  - optional support for passing a HaveAPI message object to `error!` and
    validator `message:`.
- Add `Vary: Accept-Language` for localized API/documentation responses where
  appropriate.

Benefits:

- No response envelope/protocol change.
- Existing clients continue to receive strings.
- English remains the default, so deployments are backward-compatible until a
  client or user preference requests Czech.
- vpsAdmin can migrate gradually.

Tradeoffs:

- Clients do not receive stable machine-readable error codes.
- Application-level messages are translated only after vpsAdmin adopts the new
  helpers or ActiveModel translation patterns.
- A few tests that assert exact English messages need either default-locale
  assertions or localized variants.

### Solution B: structured error keys/codes in the protocol

Add error objects or side-channel fields containing stable keys/codes and
interpolation metadata, while still including the localized string.

Example shapes:

- `message: "..."`, `message_key: "haveapi.errors.action_not_found"`;
- `errors: { name: [{ key: "...", message: "...", values: {...} }] }`;
- or `error_details` alongside the existing `message` and `errors`.

Benefits:

- Clients can reason about error categories without matching strings.
- Future client-side localization becomes possible.

Tradeoffs:

- Protocol/schema/client changes are larger.
- Existing clients expect `errors[param]` to be an array of strings.
- HaveAPI client libraries in multiple languages would need follow-up support.

This could be a later additive extension after solution A. It should not block
server-side Czech localization.

### Solution C: vpsAdmin-only localization

Set `I18n.locale` in vpsAdmin and manually translate vpsAdmin messages without
changing HaveAPI.

Benefits:

- Very small HaveAPI surface.

Tradeoffs:

- HaveAPI framework messages remain English.
- vpsAdmin must work around validation and token/action-state messages.
- Other HaveAPI users cannot reuse the work.

This is not recommended.

### Recommended first implementation slice

Implement solution A in HaveAPI first:

1. Add locale negotiation/configuration and request-local locale handling.
2. Translate HaveAPI-owned framework messages in `Server`, `Action`, params,
   type/resource coercion, ActiveRecord input adapter, token provider, and
   action-state resource.
3. Convert built-in validator defaults to lazy/localized messages while keeping
   custom string messages unchanged.
4. Add bundled English and Czech translations.
5. Add specs for:
   - default English behavior;
   - `Accept-Language: cs` and `cs-CZ`;
   - unsupported/malformed language fallback;
   - validation errors and validator self-description in Czech;
   - application string messages remaining unchanged.
6. Update protocol/server docs to describe request language selection and the
   unchanged envelope shape.

### Source-shaped HaveAPI design

The preferred design is Rails-like internally and protocol-compatible
externally:

- internally, framework-owned errors are represented as symbolic keys with
  interpolation values;
- at the response boundary, HaveAPI renders those objects to localized strings;
- the JSON envelope remains unchanged.

The public response still looks like today:

```json
{
  "status": false,
  "response": null,
  "message": "input parameters not valid",
  "errors": {
    "name": ["must be present"]
  }
}
```

Only the language of the strings changes.

#### Core classes

Add `HaveAPI::I18n` / `HaveAPI::LocalizedMessage`:

```ruby
HaveAPI.message(:required_parameter_missing)
HaveAPI.message("haveapi.errors.action_not_found")
HaveAPI.t("haveapi.errors.action_not_found")
```

`LocalizedMessage` stores:

- translation key;
- interpolation values;
- optional default English text;
- optional scope, e.g. `haveapi.errors` or `haveapi.validators.length`.

It renders with the current `::I18n.locale` only when HaveAPI is preparing the
response. This is important because validators are initialized when resources
are built, but the locale is known only per request.

Add a renderer:

```ruby
HaveAPI.localize(value)
```

It recursively turns:

- `LocalizedMessage` into a translated string;
- arrays/hashes into arrays/hashes with translated values;
- plain strings into themselves.

This renderer is called before `OutputFormatter` serializes the envelope. That
keeps JSON clients unchanged and prevents custom objects from leaking into
formatters.

#### Server locale selection

Add server configuration:

```ruby
api.default_locale = :en
api.available_locales = %i[en cs]
api.locale_header = "Accept-Language"

api.locale do |request:, current_user:, default_locale:|
  current_user&.language&.code || default_locale
end
```

Request locale precedence for HaveAPI itself:

1. explicit client request, initially standard `Accept-Language`;
2. app resolver block;
3. `default_locale`.

For vpsAdmin, the resolver can return `current_user.language.code` when the
client did not request a locale explicitly.

Implementation points in `HaveAPI::Server`:

- parse and normalize language tags before handling a request;
- wrap endpoint execution in `::I18n.with_locale(locale)`;
- set `Vary: Accept-Language` when using `Accept-Language`;
- keep malformed or unsupported languages as a fallback to default locale,
  not a request failure.

The parser only needs enough RFC behavior to rank common values, e.g.
`cs-CZ,cs;q=0.9,en;q=0.5`. It can normalize to the primary tag (`cs`) when that
is the supported locale.

#### Framework errors

Convert HaveAPI-owned framework messages to symbolic messages:

- `HaveAPI::Server`
  - action not found;
  - bad Accept header;
  - unsupported content type;
  - bad JSON syntax;
  - JSON body must be an object;
  - action requires authentication;
  - insufficient permissions;
  - server error occurred.
- `HaveAPI::Action`
  - validation wrapper messages;
  - default server error fallback.
- `HaveAPI::Params`
  - invalid input layout;
  - input parameters not valid;
  - required parameter missing.
- `HaveAPI::Parameters::Typed`
  - cannot be null;
  - invalid string encoding;
  - invalid integer/float/boolean/datetime/string.
- `HaveAPI::Parameters::Resource`
  - cannot be null;
  - invalid string encoding;
  - resource not found.
- `HaveAPI::ModelAdapters::ActiveRecord::Input`
  - invalid id;
  - resource not found;
  - invalid includes value.
- built-in token/action-state messages where they are framework-owned.

Application-provided exception messages remain strings unless the application
opts into keys.

#### Validators

Change built-in validators so default messages are lazy `LocalizedMessage`
objects. Custom `message:` stays exactly as it is today.

Examples:

```ruby
@message = take(
  :message,
  HaveAPI.message("haveapi.validators.presence.non_empty")
)

@message = take(
  :message,
  HaveAPI.message("haveapi.validators.length.range", min: @min, max: @max)
)
```

`ValidatorChain#validate` should render/interpolate through HaveAPI instead of
plain `format(validator.message, value:)`. That lets both styles work:

- localized default messages receive `value:` as interpolation;
- existing custom strings containing `%{value}` still use current formatting;
- existing custom strings without placeholders still pass through.

`Validator#describe` should return localized strings when description is built
inside a localized request. This means `OPTIONS` self-description can also be
localized without changing its shape.

#### ValidationError

Keep `HaveAPI::ValidationError` compatible, but allow localized values:

```ruby
raise HaveAPI::ValidationError.new(
  HaveAPI.message("haveapi.validation.input_parameters_not_valid"),
  name: [HaveAPI.message("haveapi.validation.required_parameter_missing")]
)
```

The class can continue to expose `#message` and `#to_hash`. Rendering happens
later through `HaveAPI.localize`, so code that rescues and passes errors onward
does not need to know about the locale.

#### vpsAdmin adoption

The initial vpsAdmin integration should not rewrite every error.

First phase:

- configure HaveAPI locale selection from `Accept-Language` and
  `current_user.language.code`;
- load vpsAdmin locale files into `I18n.load_path`;
- translate HaveAPI framework errors automatically;
- add a helper for API actions, e.g. `api_message(:access_denied)`.

Second phase:

- migrate high-frequency direct messages like `access denied`, `create failed`,
  `update failed`, and common quota/state errors;
- migrate ActiveModel validations to Rails-style symbolic errors where possible:
  `errors.add(:field, :invalid_foo, value:)`;
- leave low-value exception pass-throughs and deeply technical messages in
  English until they are touched for other reasons.

This keeps the rollout incremental while making every converted message
maintainable.

### Translation maintenance workflow

Translations should be maintained from explicit translation keys, not by
blindly extracting every string literal from Ruby source. A raw string scan
would mix user-facing API errors with logs, spec data, internal exception
messages, labels, documentation, and generated examples. The project needs a
clear convention for "this string is user-facing and must be translated".

Rails/ActiveRecord follows this same key-based model for validation errors.
Validators add symbolic error types, such as `:blank`, `:too_short`, or custom
symbols. When messages are rendered, Rails looks up increasingly general I18n
keys, from model+attribute-specific keys down to generic `errors.messages.*`.
Custom string messages remain possible, but they are effectively caller-owned
text and do not give the framework a stable key to translate. HaveAPI should
mirror this approach: framework validators/errors should have stable keys and
interpolation values; application-provided strings should remain supported but
should be migrated to keys when translation is desired.

For HaveAPI:

1. Add a tiny key-based API around `I18n`, for example:
   - `HaveAPI.t("haveapi.errors.action_not_found")`;
   - `HaveAPI.message("haveapi.validation.required_parameter_missing")` for
     lazy/request-local rendering;
   - `tr(...)`/`message(...)` instance helpers for actions.
2. Convert every HaveAPI-owned user-facing framework message to one of those
   calls. English fallback text may be present during migration, but the source
   of truth should be `config/locales/en.yml`.
3. Add `i18n-tasks` as a development/test dependency and configure it to scan:
   - `I18n.t`;
   - the HaveAPI wrapper/helper calls;
   - locale files under the server package.
4. Add Rake tasks, probably in `servers/ruby/Rakefile`, such as:
   - `rake i18n:health` to fail on missing, unused, or unnormalized keys;
   - `rake i18n:missing` to print missing translations;
   - `rake i18n:normalize` to sort/normalize locale files.
5. Add a lightweight repository check for HaveAPI-owned message call sites so
   new direct strings in `report_error`, `error!`, `ValidationError`, built-in
   validator defaults, and action-state/token framework messages are noticed.
   This can start as an RSpec example or a small script. The point is to make
   new framework errors use keys from day one.

For dynamic messages, do not build English strings in Ruby and then translate
the result. Use interpolation keys:

- `haveapi.validators.length.equals` with `%{equals}`;
- `haveapi.validators.length.range` with `%{min}` and `%{max}`;
- `haveapi.types.invalid_integer` with `%{value}`;
- `haveapi.errors.resource_locked` with `%{id}` or `%{label}` where needed.

Custom strings supplied by applications remain application-owned:

- `error!("...")` still works and passes through unchanged;
- validator `message: "..."` still works and passes through unchanged;
- applications can opt in by passing a HaveAPI message object/helper result.

For vpsAdmin:

1. Add a vpsAdmin API locale directory, e.g. `api/config/locales`.
2. Configure `i18n-tasks` for vpsAdmin to scan `api/lib`, `api/models`, and
   `plugins/*/api`.
3. Add a candidate-extraction/report task for legacy strings in:
   - `error!("...")`;
   - `errors.add(..., "...")`;
   - ActiveModel validation `message: "..."`.
4. Treat that report as a triage list, not an automatic locale generator.
   Dynamic messages and exception pass-throughs need human-chosen keys and
   interpolation variables.
5. Enforce missing/unused/normalized locale keys only for converted messages at
   first. A stricter "no new raw API error strings" check can come later after
   enough of vpsAdmin has moved to key-based messages.

Then update vpsAdmin API:

1. Configure HaveAPI locale resolution:
   - explicit client language request wins;
   - otherwise authenticated `current_user.language.code`;
   - otherwise English or current vpsAdmin default.
2. Start with common framework-driven and high-frequency vpsAdmin messages,
   not every `error!` call.
3. Add Czech translations under vpsAdmin API locale files.
4. Gradually replace direct messages with translation helpers and convert
   ActiveModel validations where practical.

## Parameter metadata addendum

Action parameter labels and descriptions should be localized by HaveAPI itself,
not by patching `HaveAPI::Params` from vpsAdmin.

HaveAPI provides the generic mechanism:

- `HaveAPI::Server#parameter_i18n_scope` enables application-owned parameter
  metadata keys.
- Keys are derived from the self-description context:
  `resources.<resource_path>.actions.<action>.<input|output|meta>.parameters.<name>`.
- Plain string labels/descriptions are the English fallback.
- Explicit `HaveAPI.message(...)` metadata keeps its own key, which protects
  HaveAPI framework-owned parameters from accidental application-scope
  shadowing.
- `label_key` and `desc_key` exist for parameters that need an explicit key.

vpsAdmin should consume this by setting a vpsAdmin parameter metadata scope and
generating/updating its parameter locale entries from HaveAPI self-description
or an equivalent framework-aware extractor. The vpsAdmin source should not be
rewritten to call local `api_param_label`/`api_param_desc` helpers, and it
should not keep a separate Ruby translation seed.

## Compatibility and deployment

- vpsAdmin API implementation addendum:
  - Existing vpsAdmin API strings should be migrated to keyed locale YAML over
    time. The rejected source-string/Ruby-seed catalog is not the target design.
  - Parameter labels/descriptions should use HaveAPI's
    `parameter_i18n_scope`-based lookup, with locale YAML as the only
    translation store.
  - The updater/health task should check locale freshness, missing keys,
    interpolation placeholder parity, and untranslated Czech values.
  - Runtime translation is applied through HaveAPI message/error/metadata
    localization and explicitly localized custom routes, so normal output data
    from the database remains untouched.
  - Keyed `VpsAdmin::API::I18n.message/t` helpers remain available for
    application errors and places where ActiveModel/Rails-style keys are not
    expressive enough.
- HaveAPI response shape remains unchanged: strings stay strings.
- English is the default locale, preserving current behavior for clients that do
  not request a language.
- New Czech translations are additive.
- No database changes are needed in HaveAPI.
- vpsAdmin already has `languages` and user language references, so the later
  vpsAdmin step should not require a schema change for locale selection.
- Deployment order:
  1. release/update HaveAPI with i18n support;
  2. bump vpsAdmin to the new HaveAPI;
  3. enable vpsAdmin locale resolver and translations.
- Mixed versions:
  - old clients work against new servers because the envelope is unchanged;
  - new vpsAdmin code using HaveAPI i18n helpers must not run with an older
    HaveAPI gem, so the gem dependency/pin must enforce the minimum version.
- Rollback:
  - rolling back HaveAPI removes Czech localization but does not create
    incompatible persisted state;
  - rolling back vpsAdmin is safe if no schema change is introduced.

## WebUI localization addendum

The WebUI keeps gettext at runtime, but its maintenance flow is replaced:

- Source strings remain `_()` calls in PHP. Template-only literals are assigned
  from PHP so gettext can extract them.
- `webui/lang/locale/vpsAdmin.pot` is generated from PHP sources.
- Translations live in
  `webui/lang/locale/<locale>/LC_MESSAGES/vpsAdmin.po`; compiled `.mo` files
  are generated artifacts.
- Legacy unmanaged locale files are removed. English uses msgids directly and
  does not need a duplicate PO/MO catalog.
- The WebUI health hook checks that the POT is fresh, configured non-English
  locales have PO/MO files, PO files have no fuzzy or untranslated entries, and
  MO files match their PO source.
- Guests select locale from `Accept-Language`, then a language cookie when one
  was explicitly chosen. Logged-in users use `User.language`.
- The top-right language switcher writes the user's language preference through
  the API for normal sessions. During admin context switch it changes only the
  borrowed session and cookie.
- PHP and JS HaveAPI clients receive the selected API language. The JS bundled
  client is refreshed from the HaveAPI i18n branch. The PHP package path remains
  deployment-gated on releasing/pinning a HaveAPI PHP client version that
  implements the `language` option; vpsAdmin passes the option in a way that
  older 0.28.4 clients ignore safely.
- Czech WebUI translations and the Czech `Language` seed are committed
  separately from the generic runtime/maintenance support.

## vpsf-status localization addendum

vpsf-status will use Go-native i18n support without changing public JSON or
Prometheus contracts:

- Add `github.com/nicksnyder/go-i18n/v2` with TOML message files and
  `golang.org/x/text/language` matching.
- Keep English source messages in Go as the canonical catalog; generated
  message files are checked for freshness and should not be edited manually.
- Encode selected language in HTML URLs as `?lang=<code>`. HTML routes redirect
  missing or unsupported language requests to a canonical URL chosen from
  `Accept-Language`, falling back to English.
- Localize rendered HTML, template strings, status labels, history labels,
  outage labels, and Go-built page labels. Keep JSON, metrics, static routes,
  status code values, and API field names unchanged.
- Split commits into generic i18n/runtime/maintenance support first, then Czech
  translation enablement.
- Add a language switcher that preserves the current route/query and replaces
  only `lang`.
- Add `make i18n-update`, `make i18n-health`, and a Lefthook pre-commit hook
  for translation freshness/completeness.

## Testing plan

- HaveAPI quick verification:
  - `cd servers/ruby && bundle exec rspec` or targeted specs during
    development;
  - `bundle exec rubocop` in `servers/ruby`;
  - broader `make test` from the repository root if the change touches shared
    protocol/client behavior.
- vpsAdmin follow-up verification:
  - targeted API specs around locale resolution and translated errors;
  - `cd api && bundle exec rspec` for changed API areas;
  - `bundle exec rubocop` in `api`;
  - update API spec topic coverage only if new spec files are added.
- vpsAdmin WebUI verification:
  - WebUI PHPUnit regressions for locale selection and API client options;
  - WebUI gettext health hook;
  - targeted browser coverage for Czech guest/login language behavior when the
    Czech catalog is added;
  - broader Playwright webui scripts when practical before merging.
- vpsf-status verification:
  - route tests for language redirect/canonicalization, switch links, and cache
    separation;
  - rendering tests for English and Czech visible text;
  - `make i18n-health`;
  - `go test ./...`;
  - `make`;
  - `nix build .#vpsf-status` after dependency/vendor hash updates.

## GC roots and devcluster cleanup addendum

- Identify stale Nix GC roots that are safe to remove on the development
  machine, with special attention to old devcluster/test-runner outputs and
  workspace `result` links.
- Do not remove roots automatically; prepare an explicit candidate list first.
- Update the shared devcluster tooling so cluster stop/reset/cleanup paths
  remove tool-owned GC roots when clusters are no longer used.
- Keep the change compatible with existing cluster state directories: old
  clusters may have stale roots, but new tooling should be able to clean them
  without requiring a full cluster recreation.
- Verification should include shell/Ruby syntax checks and a dry-run style
  command path that lists roots without deleting them where possible.
