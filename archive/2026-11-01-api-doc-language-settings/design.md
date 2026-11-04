# Czech and English HTML documentation

Status: **implementation brief**, 2026-11-01. The user authorized implementation
with “Proceed with implementation”; the latest exact selector labels are
**English / Česky**. The lead creates the feature worktree from fresh
`origin/master` at `worktrees/2026-11-01-api-doc-language-settings/haveapi`
and records its base. This authorization does not include deployment or
integration. The architect owns this brief; implementers own application edits.

## Agreed behavior

Localize documentation on the Ruby server, using the existing HaveAPI translation
catalog. Add **Language: English / Česky** in Settings immediately above Theme.
Before a choice is saved, follow the browser's language with English fallback;
an explicit user choice persists. Changing it reloads the current documentation
page. Apply the same choice to the API reference and linked HaveAPI internal
articles, with symmetric English and Czech source directories.

This fits the existing server-rendered pages and their localized API metadata.
It avoids a second browser translation system for descriptions, Markdown and
search results. JavaScript receives only the resolved messages it needs for
dynamic controls. Generated executable code remains unchanged; framework-authored
explanatory comments are translated as required by the later user milestone below.

## Evidence and current flow

Inspected the canonical bare repository, without accessing another worktree.
Source links below pin cached `origin/master`
`391b0190241cf195a69b06f7297d3e4eebec5a83`; bare local `master`
`7835acafdda19779815a0f1ba905d78e0085456d` is older. This was not a fresh remote
verification. Implementers must check the relevant contracts against the lead's
fresh base and report material drift before changing this design. Relevant
repository instructions, README, documentation UI/client
example guides and localization/development procedures were read.

- [Rendering and authorization](https://github.com/vpsfreecz/haveapi/blob/391b0190241cf195a69b06f7297d3e4eebec5a83/servers/ruby/lib/haveapi/documentation_helpers.rb#L44): authenticate the documentation reader, describe their authorized API, select the page, then render ERB. Shared/index pages use [the same layout](https://github.com/vpsfreecz/haveapi/blob/391b0190241cf195a69b06f7297d3e4eebec5a83/servers/ruby/lib/haveapi/shared_documentation_helpers.rb#L3).
- [Settings](https://github.com/vpsfreecz/haveapi/blob/391b0190241cf195a69b06f7297d3e4eebec5a83/servers/ruby/lib/haveapi/views/version_sidebar/brand.erb#L4) is a native disclosure with Theme first, followed by account controls. [Browser preferences](https://github.com/vpsfreecz/haveapi/blob/391b0190241cf195a69b06f7297d3e4eebec5a83/servers/ruby/lib/haveapi/public/js/documentation.js#L4) use `haveapi.docs.preferences.v1`; its `language` means **programming language**, alongside theme, client variant and example detail.
- [Request locale handling](https://github.com/vpsfreecz/haveapi/blob/391b0190241cf195a69b06f7297d3e4eebec5a83/servers/ruby/lib/haveapi/server.rb#L67) already affects API requests. [Locale helpers](https://github.com/vpsfreecz/haveapi/blob/391b0190241cf195a69b06f7297d3e4eebec5a83/servers/ruby/lib/haveapi/i18n.rb#L63) parse language weights and normalize regional tags. [Parameter metadata](https://github.com/vpsfreecz/haveapi/blob/391b0190241cf195a69b06f7297d3e4eebec5a83/servers/ruby/lib/haveapi/parameters/metadata_i18n.rb#L22) supports application translations with declared-text fallback.
- [Example rendering](https://github.com/vpsfreecz/haveapi/blob/391b0190241cf195a69b06f7297d3e4eebec5a83/servers/ruby/lib/haveapi/server.rb#L254) builds request-local contexts and renderer results; [the result template](https://github.com/vpsfreecz/haveapi/blob/391b0190241cf195a69b06f7297d3e4eebec5a83/servers/ruby/lib/haveapi/views/version_page/client_result.erb#L1) separately escapes code and limitation prose. Browser copying uses displayed code text.
- [Search](https://github.com/vpsfreecz/haveapi/blob/391b0190241cf195a69b06f7297d3e4eebec5a83/servers/ruby/lib/haveapi/documentation_search.rb#L145) builds an authorized index whose content key already includes locale. Keyed responses are private and vary by cookies/credentials; locale changes must remain consistent with that contract.
- [Internal routes](https://github.com/vpsfreecz/haveapi/blob/391b0190241cf195a69b06f7297d3e4eebec5a83/servers/ruby/lib/haveapi/server.rb#L622) render copied Markdown and generated JSON-schema HTML. [Shared navigation](https://github.com/vpsfreecz/haveapi/blob/391b0190241cf195a69b06f7297d3e4eebec5a83/servers/ruby/lib/haveapi/views/shared_sidebar.erb#L18) links Protocol, JSON schema, Create a client and Client examples. The internals landing page reads the server's README. [copydoc.sh](https://github.com/vpsfreecz/haveapi/blob/391b0190241cf195a69b06f7297d3e4eebec5a83/utils/copydoc.sh#L5) currently copies only top-level documents; [gem packaging](https://github.com/vpsfreecz/haveapi/blob/391b0190241cf195a69b06f7297d3e4eebec5a83/servers/ruby/haveapi.gemspec#L13) also uses a shallow documentation glob.

## Locale and presentation contract

Use a documentation-specific locale, independent of the API's configurable
locale resolver/header/default and any account language. Resolve it from a valid
explicit documentation query such as `doc_lang`, then a saved documentation
cookie, then the browser's `Accept-Language`, finally **English**. Restrict the
supported set to `en` and `cs`. The selector displays the effective language;
initial rendering does not save the detected choice. Browser detection applies
while no explicit choice is saved, without a visible automatic/reset option or
an `auto` query value.

Use a nonsecret, host-only cookie scoped to the API mount, with SameSite=Lax and
Secure on HTTPS, for manual persistence. Keep it separate from the existing
example preferences; do not rename or reuse their `language` field. Settings
selection preserves the current path, page/resource selector, query and fragment
when reloading. A validated query override makes the selected page work even
when cookies are unavailable; persistence then cannot be promised. Only an
explicit user selection saves the preference. A native select and GET fallback
can support keyboard and JavaScript-disabled selection.

Use weighted `Accept-Language` negotiation, supporting `cs-CZ` → `cs`,
`en-GB`/`en-US` → `en`, case-insensitively. Consider supported entries in quality
order, skip zero-quality entries and unsupported languages, and use English
when no supported language is selected; a lone wildcard also resolves to
English. The existing parser can be reused, with these cases verified.

Apply the selected locale only inside documentation description/rendering and
documentation search, with guaranteed restoration on errors. Resolve it after
documentation authentication so its locale resolution cannot overwrite the
choice. Do not change OPTIONS, action requests, API payloads, client locale
settings, user preferences or authentication. Pin search fetches to the page's
effective locale, using a read-only documentation locale selector; search must
not overwrite the saved choice. Preserve index-key validation and private cache
rules. Normal navigation uses the same mount-scoped cookie, including links
between the reference and `/doc/...` pages.

Put framework text under `haveapi.documentation` in `i18n/haveapi.yml` and
regenerate server catalogs using the existing task. Translate ERB/helper labels,
headings, navigation, settings, authentication/visibility notices, validator
presentation and accessibility text. Supply the selected messages to browser
code through the existing safe JSON embedding helper: copy feedback, example
fallback notices, detail labels and search statuses need translation too.
Do not duplicate a hand-maintained browser catalog. Missing framework keys fall
back to English, and translation coverage checks should catch omissions.

Set `<html lang="cs|en">`; label the select explicitly and retain native focus,
disclosure and status behavior. Use the exact labels `English` and `Česky` as
language names. The Czech example-language label is exactly **Jazyk**, per the
latest user request. Keep identifiers, DOM IDs, URLs,
HTTP verbs and code-language names stable. Escape interpolated text and JSON;
do not insert translated text with `innerHTML`.

## Content boundaries and internal articles

Framework localization cannot translate arbitrary API-authored strings.
Resource/action descriptions already support `HaveAPI::LocalizedMessage`, and
parameters support `parameter_i18n_scope` and explicit keys. Render those through
the existing mechanisms in the selected documentation locale. Plain descriptions,
example titles/comments and custom renderer prose retain their supplied text
unless their author provides a translation. No automatic translation or new
API description schema is proposed.

Move the public English articles currently in top-level `doc/*.md` to `doc/en/`
so article lookup has one uniform source layout. Translate the agreed set under
`doc/cs/`: `protocol.md`, `create-client.md`,
`typed-input-validation.md` (linked from the protocol), and `client-examples.md`.
Give the internals landing article the same layout, `doc/en/readme.md` and
`doc/cs/readme.md`; the server README can become a short entry point linking to
the English article instead of duplicating its prose. A small locale-aware
article lookup selects `doc/<locale>/<article>` and falls back to
`doc/en/<article>`. Keep public URLs and page identities separate from source
paths and translated titles. English fallback content gets `lang="en"` and a
short notice while the surrounding UI remains Czech.

Known consumers to update with this source reorganization are `utils/copydoc.sh`
(copy both locale trees), `servers/ruby/haveapi.gemspec` (include nested files),
the server's `doc` helper and shared README/article lookup, and documentation
packaging/shared-page specs. Update repository README/guide links to the moved
English articles and relative links inside both locale trees, including links
to code, shared assets and untranslated guides. Keep online article links mapped
to the existing public routes rather than exposing source-directory paths.
Shared schema definitions/templates and technical assets may stay outside the
locale trees. No obsolete English source copies are required.

Preserve the current English fragment IDs explicitly when translating headings;
do not derive link targets from Czech text. Localize the existing TOC labels.
Keep relative article links and mounted asset URLs working in both languages;
the locale directory is a source layout, not a required new public route prefix.
The protocol's diagram retains protocol class/field names; surrounding prose and
alternative text can explain it in Czech.

For [JSON schema](https://github.com/vpsfreecz/haveapi/blob/391b0190241cf195a69b06f7297d3e4eebec5a83/doc/json-schema.erb#L431), localize the surrounding heading/TOC prose while generating both presentations
from the same schema data. **The displayed machine representation, including
its keys, values, references and embedded schema titles, stays unchanged.**
Do not maintain a second translated schema. Extend documentation copying and
gem inclusion to carry the localized articles/generated presentation; verify an
extracted gem, not only a source checkout.

Keep all noncomment executable source and protocol/JSON/HTTP samples
byte-equivalent across UI locales. Variable names, imports, calls, URLs, headers,
literals and sample data are not translation targets. Framework-authored
explanatory comments must now be translated at their authored emission boundaries;
this supersedes the initial optional-comments decision. Never regex-translate a
rendered program.
When translating comments in authored Markdown examples, preserve syntax and
all noncomment content; do not add comments to JSON/HTTP payloads. Limitations
outside code are prose. Framework-owned generated-client limitation messages
must also be translated under the later generated-client addendum; third-party
custom reasons without a translation retain their supplied text.

## Implementation boundaries and verification

The lead assigns two packages with independent authored files. Both can start
from this contract; complete-page and packaged-gem checks depend on both landing.

**A — Runtime/UI/catalog/search and article lookup.** Own all changes under
`servers/ruby/lib/haveapi/`, including shared helpers, routing, locale handling,
ERB views/TOCs, CSS, JavaScript, generated locale files and any new article
lookup helper. Own `i18n/haveapi.yml`, `utils/i18n/catalog.rb` and associated
catalog tests. Own browser tests under
`servers/ruby/spec/client_examples/assets/` and documentation specs **except**
`servers/ruby/spec/documentation/shared_pages_spec.rb`. Add locale integration
coverage in a separate spec; do not edit package B's shared-page spec. Own any
needed runtime/i18n specs outside that directory. The catalog scanner must cover
server ERB and documentation JavaScript consumers. Package A alone changes
article/link rendering and translated TOC labels in server views.

The lead has subdivided A into independent file owners:

- **A1 — implementer0:** request/cookie handling, search, article and link lookup,
  shared runtime helpers, CSS/JavaScript, browser tests and runtime specs.
- **A2 — implementer3:** all `servers/ruby/lib/haveapi/views/**`,
  `documentation_validators.rb`, catalog source/scanner/catalog specs and generated
  locales. A1/A2 coordinate the flat JavaScript message keys; neither edits the
  other's files. This split leaves package B's boundary unchanged.

**B — Articles/source layout/packaging.** Own `doc/en/`, `doc/cs/`, the moved
top-level Markdown sources, `doc/json-schema.erb`, `utils/copydoc.sh`,
`servers/ruby/haveapi.gemspec`, `servers/ruby/README.md`,
`servers/ruby/spec/packaging_spec.rb` and
`servers/ruby/spec/documentation/shared_pages_spec.rb`. Own Markdown-only link
updates in repository READMEs/guides/instructions and documentation build/packaging
path consumers, including the relevant Makefile/release-tool assertions if
required. Do not edit `servers/ruby/lib/haveapi/`, the catalog source or A's
tests. Report a newly discovered conflicting consumer to the lead for assignment;
do not edit the other package's files. Generated server documentation is build
output, not another authored source tree.

The shared interface is the on-disk article contract, not shared editing:

- Package B supplies `doc/{en,cs}/<article>.md`, copied to
  `servers/ruby/doc/{en,cs}/<article>.md`; the landing ID is `readme`.
  Move all existing public Markdown articles to English's tree, but add Czech
  translations only for the agreed set above and `readme`. Other articles use
  English fallback. Agent procedures and shared technical assets stay outside
  the article trees.
- Package A maps existing public article IDs/aliases to those files, selects
  the effective locale, and falls back to `en`. Validate IDs and locale before
  path construction; never use an arbitrary user path. Existing `.md` aliases,
  mounted URLs and stable English anchor IDs keep working. All runtime HTML
  link adaptation and fallback notices belong to A.
- Package B generates `doc/{en,cs}/json-schema.html` in the **server output
  directory** from the one shared schema template/data. Only surrounding prose
  varies; code blocks are identical. Package A loads this representation using
  the same locale/fallback rule. The generated Envelope heading reads the
  canonical key `haveapi.documentation.schema.envelope`, supplied by A in both
  locales; B must not add a separate translation dictionary. Other schema
  headings are machine strings such as `OPTIONS /` and stay unchanged.
- Package A's exact preference contract is `doc_lang=en|cs` for a one-request
  selector and a distinct `haveapi.docs.locale` cookie for saved choice. Browser
  detection and read-only search requests never save it. Keep the existing
  `haveapi.docs.preferences.v1` object unchanged. Use a native submitted language
  form so confirming the already displayed language can also save that choice;
  JavaScript may enhance switching while preserving the fragment.

Package A can test locale/UI logic independently; B can translate and check
source links/anchor/sample equivalence independently. Catalog generation and
documentation copying precede their joint checks. No compatibility shim for the
old source layout is needed while the two packages are unfinished. The lead
serializes commits/generated-output operations and performs the final
context-aware English/Czech writing pass before commits; implementers retain
ownership of their technical fixes. Neither package adds client/protocol work.

The user also requested a temporary server after completion. **implementer2**
prepares the existing in-memory fixture with a session-local preload on the
existing internal allowed port **4567**, and waits for the lead's final
review/check signal before launch. This preview does not authorize integration
or deployment; its startup and verification results belong in the lead's state.

Acceptance cases: exactly English/Česky above Theme; unsaved choice following
Czech/English regional preferences and weighted lists without saving detection;
unsupported/missing/wildcard headers; explicit choice persisting and winning over
browser language; invalid cookies; cookie-disabled
one-request selection; reload retaining the current fragment and example/theme
preferences; keyboard/no-JavaScript reading; localized dynamic feedback and
screen-reader labels; reference → protocol → reference navigation; stable article
anchors, English fallback from `doc/en/`, updated repository links and mounted
links; search matching the page locale
without changing authorization; unchanged executable samples and API behavior.

Quick checks during implementation: focused Ruby documentation/i18n specs,
`make test-documentation-assets`, catalog generation/health checks and relevant
RuboCop checks in the declared Nix environment. After committed implementation
and independent review, run `make test-documentation`, the applicable server
suite including extracted-gem packaging, and browser checks in both locales.
Verify translated article links/anchors and noncomment sample equivalence.
Use the repository's existing performance checks if rendering/search changes
affect their contract; no separate benchmark campaign is added by this brief.

Compatibility: no database, schema, daemon/client protocol or configuration
migration. The only new persisted state is a documentation preference cookie;
older servers can ignore it after rollback. Ship matching server assets,
catalogs and articles together. The authorized source reorganization changes
repository paths and their consumers in one change; existing public URLs and
fragment IDs remain valid. Roll back the complete server package, including
its matching article layout. No coordinated client rollout is required. Application-authored
translation completeness and behavior of third-party renderers remain dependent
on their owners; this change does not promise to translate those strings.

Verification at brief handoff: source inspection and contract checks only. No
runtime behavior or browser interaction has yet been tested by the architect.
Implementation/check results belong in the lead's state and implementation
reports. Scope remains HaveAPI; no application-wide or API/client protocol
localization is included.

## CI follow-up: build inputs and packaging provenance

Design delta after final review, scoped to the reported CI failures. The retained
`ci-performance-41345966685/performance-41345966685-1/dependency-compatibility.json`
shows identical evaluated gemspec dependencies. Its only differing comparison
input is `servers/ruby/haveapi.gemspec`: the documentation file-list assignment
changed from shallow to recursive selection. The paired run failed before
measurements; the all-client contract passed. This is a source-packaging change,
not a changed benchmark environment or a measured performance regression.

**B build correction (implementer1):** generate schema HTML with Ruby's bundled
YAML/ERB facilities, reading `haveapi.documentation.schema.envelope` directly
from canonical `i18n/haveapi.yml` into the ERB binding. Escape this presentation
variable in `doc/json-schema.erb`. Remove the build-time dependency on requiring
`haveapi/i18n` outside Bundler; do not add a translation dictionary or gem
dependency. Keep schema code bytes identical. Own `utils/copydoc.sh`, the shared
schema template and the associated packaging/build regression. Verify generation
outside Bundler with isolated empty gem search directories (not an empty shell
`PATH`), plus English/Czech headings and schema-byte equality.

**Guard correction (implementer3):** use the existing shared capture/validation
path in `servers/ruby/benchmarks/performance_compare.rb`. CI preparation calls
`SourceVersions.capture` from `utils/performance_ci.rb`; live worker inputs call
it from `servers/ruby/benchmarks/endpoints.rb`; replay recomputes the receipt in
`SourceVersions.validate_inputs`. Normalize only these two exact, anchored,
once-only server-gemspec statements to the same comparison bytes:

```ruby
  s.files       = `git ls-files -z`.split("\x0") + Dir.glob('doc/*')
  s.files       = `git ls-files -z`.split("\x0") + Dir.glob('doc/**/*').select { |path| File.file?(path) }
```

This explicitly reviewed two-form transition replaces the earlier suggestion
to recognize a general file-enumeration expression. Do not add a Ruby expression
parser, support future shapes, drop gemspecs from comparison, or rely only on
evaluated dependency metadata. Keep every other byte strict, including external
dependencies, Ruby requirements, unrelated gemspec metadata and comments.
Ambiguous/duplicate declarations must not receive the normalization. Preserve
raw manifest contents/hashes bound to source identity, evaluated dependency
checks, exact activated runtime/lock graphs, all budgets and the fixed reference.

Use the smallest receipt discriminator necessary to distinguish this new
normalization from legacy raw-file-selection receipts. Replay must recompute the
chosen transformation, reject a stripped/tampered normalization marker, and
continue accepting valid legacy receipts under their original rule. Apply the
same helper wherever this new policy is captured, including preparation and live
inputs; do not patch only the CI comparison. The current failure uses ordinary
`source_versions`, not the maintenance-lineage branch. Preserve that branch's
existing strict behavior unless a demonstrated consumer requires the identical
reviewed handling; do not broaden lineage policy speculatively.

Guard scope: `performance_compare.rb`, focused performance/source-version and
replay specs, and the policy explanation in `doc/en/performance.md`; change
`utils/performance_ci.rb` or `endpoints.rb` only if shared wiring requires it.
Tests must accept the exact old/new pair in preparation, live input capture and
replay, while rejecting changed dependencies, other bytes, duplicate statements
and tampered/stripped/unbound receipts. Retain legacy replay coverage. No
environment migration, benchmark recalibration or exception keyed to a commit
is warranted.

The lead reports the full-suite watcher complete, so B's build fix and A1's two
search-assertion corrections may proceed independently. Guard work belongs to
implementer3 and does not overlap those files. Once these follow-ups are committed
and focused checks pass, the same independent reviewer must assess the newly
introduced guard boundary in the general, architecture, scope/proportionality,
and risk/compatibility lanes before repeat broad checks. Review the affected
delta and its whole-branch implications; do not restart unrelated investigation.
The existing failed run remains evidence of a preparation failure, not a timing
result. A subsequent successful preparation must still run the measured gate.

## Measured allocation follow-up

The explicit original-base comparison in run `41348052141` measured
`391b0190241cf195a69b06f7297d3e4eebec5a83` →
`e7ac8578a2ffd07b3ac7da05a27996191619a8f9`. The retained
`ci-watch-artifacts/41348052141/performance-41348052141-1/results/report.json`
reports allocation regressions for `docs.html_resources` (13,730.60 → 15,630.62,
+13.84%) and `docs.html_actions` (12,940.63 → 14,810.36, +14.45%). Correctness
passed; timing was inconclusive with 3/5 regression agreement, not a measured
timing pass. The existing allocation budget remains authoritative despite green
push-pair CI and the other passing cases.

Source diagnosis: `DocumentationLocale#documentation_t` in
`servers/ruby/lib/haveapi/documentation_locale.rb` eagerly resolves English and
then performs another `I18n.t` for the current locale on every call. The English
HTML path repeats the same lookup throughout templates. This is a concrete
avoidable cost; its contribution must be measured rather than assumed sufficient.

**Minimal fix, implementer0:** return the already resolved English result when
the active `::I18n.locale` is `:en`, before the second translation call. Keep the
existing non-English lookup and English/default fallback behavior. This needs no
`exists?` probe, cache, new service, backend change, catalog rewrite or broader
template refactor. Keep keys/interpolation/default arguments and the callers'
HTML/JSON escaping boundaries intact; do not mutate locale, API metadata,
translation strings or catalogs. The request locale remains controlled and
restored by the existing documentation scope.

Own only `documentation_locale.rb` and focused tests in
`servers/ruby/spec/documentation/locale_spec.rb` (or one small helper spec there).
Cover English and Czech translations, interpolation, missing Czech → English,
missing framework key with explicit default and absent default, and repeated
English/Czech/English calls with distinct interpolated values. Retain existing
HTML/JSON escaping, request-locale restoration, API/OPTIONS independence and
example-equivalence coverage. Do not add a global mutable translation cache.

Use the existing documentation endpoint fixture for a bounded local allocation
probe before/after at the same runtime, fixture dimensions and warmed request
count, keeping setup outside measurement. A0 records exact source/patch, both
HTML shapes, allocations and output equality for English, plus Czech output
equality. Session-local probe evidence is sufficient; add no benchmark framework
or new budget. Compare the saved e7 source with the candidate without modifying
or restarting its live preview. If removing the duplicate English lookup is
insufficient, report the remaining measured gap before expanding this fix.

After focused tests and the bounded probe, commit the narrow change and send the
affected translation/performance delta to the retained independent reviewer
(general, architecture and scope/proportionality; include risk/compatibility if
implementation changes locale/fallback boundaries beyond this fast path). Repeat
the explicit original-base → exact-final-head performance pair after acceptance;
a small local probe or green incremental push pair cannot replace that result.
No reference/budget changes, benchmark graph changes or timing-pass claim from an
inconclusive outcome. Refresh the preview only after the successor is finally
verified, under the lead's existing preview authorization.

## Added milestone: selector presentation and generated comments

The user now requires a select-only language switch when JavaScript works,
localized framework-owned comments in every documentation example, and the Czech
sidebar label **Jazyk**. Their follow-up “i18n:health is what I remembered” settles
the guard question: retain the current health checks and extend recognized key
extraction for the new helpers only. No raw-literal classification subsystem or
further vpsAdmin research is part of this milestone. Catalog key completeness
does not prove that arbitrary prose has been extracted; application-authored
strings and machine data retain the existing boundary.

The English-lookup optimization is completed separately at head
`613c83a76fce94a9b13122ca74540291d361242f`, per implementer0's report (19 focused
specs, style/hooks and an existing-fixture diagnostic probe with equal en/cs
bodies). Its source/spec files remain exclusive to that owner; this milestone
does not reopen the helper or change performance budgets.

**Comment interface, owned by B (implementer1).** Add optional `locale: :en` to
the immutable `ClientExample::Context`; `with` retains it. Set it from the active
documentation locale in `ServerHelpers#documentation_context`. Expose
`context.example_comment(key, default:, **values)`, returning plain translated
prose from `haveapi.documentation.comments.<key>` with explicit captured locale
and the English default. No mutable translator state is stored on the frozen,
shared Go/Rust/TypeScript adapters. The `default:` at an emission site retains
its original English prose and agrees with the English catalog; generator gems
need no new server dependency or separate translation dictionary.

Server renderers use a small `example_comment(key, default:, **values)` helper
on `ClientExample`. It delegates to the context; direct calls without a context
retain English defaults. Each external documentation adapter uses the same
duck-typed context method when available and otherwise formats the English
default. Keep adapter `render(kind:, context:, mode:, ...)` signatures unchanged;
old custom adapters may ignore the additive context capability. Pass context
through only helpers that actually emit comments. Do not touch generated client
implementation/templates outside documentation examples.

Renderers retain ownership of comment markers, indentation and line endings;
translation supplies only human prose. Translate full-line and inline explanatory
comments in initialization, authentication and action examples, both detail
levels and inherited sync/async/blocking variants. This includes Ruby's “Reuse
an existing token” and corresponding PHP/JS/Python/CLI/curl/HTTP/Go/Rust/TypeScript
explanations. Keep commented-out commands, installation snippets, response
transcripts and literal sample data unchanged. Mixed comments interpolate
unchanged identifiers/types/code fragments into translated prose. Prefix every
physical line of translated comment text with the language's existing comment
syntax; never let an interpolated newline create executable text. Keep HTTP
explanations at their existing annotation boundaries, outside wire messages.
Use no postprocessing of complete rendered source.

**B's exact files:** `servers/ruby/lib/haveapi/client_example.rb`,
`documentation_context.rb`, `client_examples/*.rb`, and only
`ServerHelpers#documentation_context` in `server.rb`; the three existing
`clients/{go,rust,typescript}/lib/haveapi/*/documentation.rb` adapters; their
focused documentation/example/context specs; the owning client-examples guide
paragraphs. B sends a bounded list of literal comment keys, English defaults,
placeholders and suggested Czech wording to A2. B does not edit catalogs,
views, browser assets, `documentation_locale.rb` or `locale_spec.rb`.

**A2 (implementer3) owns UI and all catalog writes.** Own
`views/version_sidebar/brand.erb`, relevant sidebar presentation, the language
enhancement in `public/js/documentation.js`, its browser tests and the UI guide.
The existing JS already binds `change` to navigation; hide the submit button
only after that form's enhancement is installed. Native GET select+submit remains
visible and usable without JavaScript. Retain current path/query/fragment handling
and exact English/Česky options; no new settings behavior. Update the Czech
example selector label to Jazyk. Use a focused UI spec rather than editing A0's
exclusive locale spec.

A2 alone edits `i18n/haveapi.yml`, generated catalogs, `utils/i18n/catalog.rb` and
its specs. Add B's comments beneath `haveapi.documentation.comments`, preserving
locale/placeholder parity and generated-file checks. Recognize literal
`example_comment` keys in server renderers and the three documentation adapters;
add those actual adapter files to extraction. Keep existing
`documentation_t`/`documentationMessage` recognition. This is sufficient for the
accepted health requirement. No new translation registry or broad scanner.
The catalog can change now that A0 has released its commit/hooks slot. B can
work from the interface concurrently; joint checks wait for A2's keys/generation.

Acceptance/checks: enhanced UI shows only the select and switches on change;
no-JS form submits correctly; Czech sidebar says Jazyk. Render the existing
supported example matrix in en/cs, covering all renderer variants and emitted
comment-bearing init/auth/action paths. Verify actual Czech comments, English
defaults for old/direct contexts, and **exact noncomment source bytes** across
locales. Use language-aware comment recognition or explicit emission-boundary
fixtures for parity, never a regex that could discard comment-looking literals.
Keep existing syntax/compile and shell-argument safety checks for affected
renderers; commented commands and data also require unchanged-value assertions.
Run existing i18n health and focused browser/renderer/adapter checks, then obtain
independent review of this new behavior before the required broader checks and
the final explicit original-base performance pair. Reuse existing tests and
fixtures; add no benchmark framework. Lead performs final context-aware wording.
The running e7 preview stays unchanged until a final verified successor.

## Generated-client prose and preview addendum

The user explicitly requires Go/Rust/TypeScript documentation text as well as
comments to be translated and these clients to appear in the preview. This
supersedes any earlier allowance for built-in adapter prose to remain English.
Keep scope to actual HTML documentation output, not client runtime diagnostics
or generated library implementation.

**Actual visible-source inventory:**

- `views/version_page/client_overview.erb`, `client_init.erb`, `client_auth.erb`,
  `client_example.erb`, `example_panels.erb` and `version_sidebar.erb` display
  registry labels/variants; `documentation_client_metadata` also sends variants
  to JS selectors. Translate **Go API client**, **Rust API client (async)**,
  **Rust API client (blocking)**, **TypeScript API client**, and the corresponding
  Async/Blocking/API client display variants. Language names, IDs and configured
  package names/versions remain exact. Overview/usage headings and wrapper
  missing-profile notices already use framework catalog keys; retain and verify
  those rather than introduce duplicate messages.
- `clients/go/lib/haveapi/go_client/documentation.rb`: every literal passed to
  `unsupported!` or returned by `limitation` is visible through `result[:reason]`.
  Cover mode/section availability, action availability, structured samples,
  route/layout/metadata mismatches, list input, unavailable responses, output
  layouts, Custom fields, name collisions, undeclared response-field paths,
  response-field mismatch, null-versus-zero ambiguity, associated response
  object/visibility, missing path arguments, int64 range/path type, object input,
  unavailable input/input-field/null, authentication availability/mismatch/support,
  and unrepresentable field values. Preserve the interpolated response-field
  path as data. Repeated identical reasons share one key.
- `clients/rust/lib/haveapi/rust_client/documentation.rb`: every `Unsupported`
  reason returned by `render` is visible. Cover execution mode, API version,
  documentation section, authentication availability/description/header/support,
  action availability, structured sample/path arguments, required authentication,
  action route/method/layout, missing action/sample metadata, input representation,
  GET list input, input layout, changed parameter/value representation, nested
  Custom GET query values, required input and response/layout mismatch.
- `clients/typescript/lib/haveapi/typescript_client/documentation.rb` exposes
  one generic unavailable/incompatible-sample limitation. Translate that single
  message; do not expose detailed private-schema reasons currently hidden by it.
  Setup explanations in all three adapters are the comment-emission sites
  already owned by B, including package/setup/authentication/context guidance.
  `documentation_clients.rb` profile-registration/validation exceptions happen
  during server setup, outside HTML output; their operator diagnostics are not
  a new translation project here.

**Small context extension, B owner:** add
`context.documentation_message(key, default:, **values)` for keys relative to
`haveapi.documentation`, using the same captured locale and English-default
contract as comments. `example_comment` can delegate with `comments.<key>`.
Use `generated.go.<reason>`, `generated.rust.<reason>` and
`generated.typescript.unavailable` for adapter prose. Keep the optional
duck-typed context capability and English fallback for standalone/old contexts;
add no server dependency to generator gems and do not change adapter render
signatures. Built-in adapter errors may carry a literal key, English default and
interpolation values, then resolve once in `render`'s rescue where context is
available. This avoids passing locale through every validation method or storing
request data on a shared adapter. Preserve the English error message for direct
adapter usage and the existing frozen `{status: :limitation, reason: String}`
result contract. Never translate a raw exception string by text matching.

**Ownership/keys:** B extends its existing Context/adapter package and focused
adapter specs, supplying A2 the exact key/default/placeholder list for the
inventory above. A2 remains the only catalog/scanner/generated-file writer and
adds extraction for the literal new message/error-key calls in these exact
adapter sources. A2 also owns runtime display helpers in
`documentation_helpers.rb` and the listed views: use a small mapping for the
four known generated-client IDs to `generated.labels.*`/`generated.variants.*`
keys, with custom-renderer labels unchanged. Apply these same display helpers to
HTML and JS metadata; keep stable IDs, `language`, modes and data attributes used
as machine identifiers unchanged. Avoid locale-dependent class registration or
mutating renderer classes. A0's performance helper/spec remain untouched.

**Preview and checks:** implementer2 supplies actual Go, Rust (async/blocking)
and TypeScript documentation profiles in the existing preview fixture. Exercise
overview/init/authentication/action pages in both locales with their real
adapters, including representative limitation paths, and verify profile/package
identities and commands remain unchanged. B's inventory plus catalog health
covers all message keys; use focused existing adapter failures to prove translated
results, missing-key English fallback and private-data-safe TypeScript behavior.
Extend the existing HTML/metadata tests for localized labels/variants and escaped
dynamic values. Noncomment code-byte parity still applies. Lead reviews wording;
changed behavior receives affected independent review and required final checks
before the verified successor replaces the preview. No production profile,
configuration deployment or repository integration is authorized by this request.

## Native example selector addendum

The user now requires a working **Apply** action for programming language,
client variant and example detail without JavaScript. This is a separate
milestone after A2's current UI commit; it must not delay that commit or preview
checkpoint. A0 owns this complete package once the overlapping files are released.

**Evidence and smallest mechanism:** `views/version_sidebar.erb:47` currently
renders unnamed selects outside a form; `public/css/documentation.css:119`
hides their container without JS. `views/version_page/example_panels.erb:13`
opens every Simple disclosure. `public/js/documentation.js:704-775` selects
one client/detail using metadata, with per-group Simple fallback. Retain these
existing panels and metadata. A native GET reload opens the selected panel in
each group and closes the others; their summaries remain accessible without JS.
Keep every panel and legacy anchor ID, including collapsed alternatives. With
JS, the existing immediate hide/show behavior remains. No renderer prepass or
second rendering is needed: `server.rb:290-307` already returns each group's
variants and collects the page detail union before the sidebar is rendered.

**Request contract:** use only `example_language`, `example_client` and
`example_detail` as the new HTML presentation query keys. Language and client
values are exact strings from the current request's `documentation_clients`;
detail is `simple` or `thorough`. Parse duplicate/bracketed/non-scalar keys and
invalid encoding as 400 using the existing selection-error message. Unknown or
now-unavailable scalar choices fall back without loading a renderer/profile by
name: choose the first available language/client in existing registry order,
then Simple. A valid language wins over a client from another language; choose
that language's first client. If language is absent and client is valid, infer
its language. Validate against current available profiles and the same authorized
description; no hidden action or private generator schema becomes selectable.
With no explicit choices, use the same first-client/Simple default in the form
and open panels. With no available clients, omit or disable the example form.

Resolve client once per HTML request. Use each already-rendered group's detail
list to apply Thorough only where supported, otherwise Simple. If the selected
client has no result in a group, show the existing localized unavailable notice;
do not open another client's code as its replacement. Existing limitation panels
remain valid selected results. After content renders, use the collected page
union for the detail selector. This mirrors JS `clientChoice`, `effectiveDetail`
and `exampleDetail`; no changes to renderers, Context or their source bytes.

**Native form and enhancement:** wrap the sidebar controls in one GET form with
the current mounted `request.path` as action, named selects and a visible submit
button. Preserve only validated `page` or `resource`, search `q`, and a valid
explicit `doc_lang` in escaped hidden inputs. Do not carry arbitrary query keys
or credentials and do not add a detected locale as an explicit saved preference.
The native Client menu contains variants of the applied language; changing
language and pressing Apply first loads that language's choices. Keep its
single-choice behavior and supply a hidden value when a disabled control must
submit its effective choice. Detail options use the current page union.
Native submission may lose an unknown fragment, as the existing locale form
does; fragment IDs and direct disclosure access remain stable.

Stop hiding `.docs-preferences` merely because JS is absent; retain existing
no-JS hiding for JS-only theme controls. Install an example-form submit handler
alongside the existing immediate change handlers, then hide its Apply button.
Prevent an enhanced form's Enter submission from unexpectedly navigating.
Explicit native query choices must initialize JS consistently ahead of saved
example preferences on that page: expose their normalized selection through the
form's data attributes (or the existing safely encoded JSON mechanism), only
when these keys were supplied. Do not write it to localStorage on load. Without
an explicit query, retain existing saved-preference precedence; actual JS user
changes retain existing persistence. Do not add cookies, storage keys, settings
reset behavior or query propagation to unrelated navigation.

Interpret these keys only while rendering ordinary version HTML, after the
existing search-index early return. They must not change root version selection,
API action dispatch, OPTIONS, search-index data/cache identity, OAuth identity or
API locale. Existing mounted-path redirects retain queries normally. No data
migration, deployment ordering or recovery procedure changes; rollback simply
ignores the extra HTML query keys.

**Exact ownership/dependency:** A0 owns changes in
`servers/ruby/lib/haveapi/documentation_helpers.rb`,
`views/version_sidebar.erb`, `views/version_page/example_panels.erb`,
`public/js/documentation.js`, `public/css/documentation.css` (paths relative to
`servers/ruby/lib/haveapi` after the first), focused
`servers/ruby/spec/documentation/example_selection_spec.rb`, existing
`servers/ruby/spec/client_examples/assets/documentation_test.cjs`, and the native
selection paragraph in `doc/en/documentation-ui.md`. Use existing helper/view
boundaries; no new preference module. A2 remains sole catalog owner: supply
`haveapi.documentation.labels.apply_examples` (English **Apply**, Czech
**Použít**, subject to lead wording). A0 consumes it after A2's serialized
catalog update. Lead serializes A2's current UI commit and any later overlapping
view/helper work before A0 starts; B's Context/renderers/adapters remain separate.

**Focused acceptance:** HTTP specs verify native form names/action/preserved
fields; valid selections and language/client mismatch; unavailable profile,
unknown scalar and malformed duplicate/array inputs; per-group Thorough/Simple
and limitation behavior; stable IDs and unchanged code; no example-preference
cookie/storage writes or API/OPTIONS/search-index change (existing explicit
`doc_lang` cookie behavior remains). Extend existing JS tests for explicit
query initialization, unchanged saved-state precedence, immediate selection and
hidden Apply only after enhancement. Use the existing browser/preview fixture
with JavaScript genuinely disabled: choose a language, click Apply, choose its
variant/detail and submit again; confirm selected code opens on the same resource
or authentication page and locale/query survives. Cover an available generated
profile and singleton detail, then verify immediate switches with JS enabled.
Lead owns final wording and affected independent review before the verified
successor preview; existing exact-head final/performance checks remain required.

## Repeated static-label allocation follow-up

The combined UI/comment snapshot consumed part of the earlier English fast-path
savings. `combined-allocation-summary.json` records only 450/458 fewer objects
than e7 for the two HTML cases; this is diagnostic evidence, not a final hosted
pass or a portable margin calculation. Native selection is still being added.
Leave budgets, reference, fixture dimensions and dependency guards unchanged.

**Measured narrow target:** the existing `DocumentationScenario` size-8 pages
make 78 eligible `documentation_t` calls for 46 distinct keys. Repeats include
`labels.simple` (12), `labels.thorough` (7), `client.and` (5), initialization (3),
and other static sidebar/overview labels (2). An in-memory request-local memo
prototype on retained source snapshot
`8822add9eaef11a378f614400014399d0e620e8cc5bb03dd2fd4207a106e8bc9`
saved about 241 allocations/request in both English shapes and 498/497 in Czech,
with identical complete HTML hashes for each locale/shape. Evidence:
`static-label-memo-probe.json`; setup excluded, two warmups, three batches of
eight, same instrumentation wrapper with memo disabled/enabled. Absolute counts
differ from A0's earlier environment. The snapshot predates native selection;
this proves the focused opportunity, not final performance acceptance.

**Contract:** keep the existing `DocumentationLocale#documentation_t` signature
and English/Czech fallback path. Only String keys with `default.nil?` and no
extra keyword values may use a memo; explicit `default: nil` retains its current
meaning. Other defaults, interpolation/options and non-String keys always use
the original lookup. Store only successful String results, including an English
fallback; never retain nil, hashes, other result types or raised errors. Do not
introduce an extra existence lookup or skip the canonical catalog for English.

Use one helper-instance hash keyed first by the active `::I18n.locale`, then
the original key. It belongs to the current request/render scope, never a class,
thread, process-global backend or immutable example Context. Start a fresh memo
on entry to `with_documentation_locale` and clear it in `ensure`, alongside the
existing locale restoration; nested rendering may safely lose outer memo hits.
Store an owned frozen copy of each String and return a fresh copy on hits, so
caller mutation cannot poison later labels. Keep the first result's existing
behavior and all escaping at the existing consumers. No catalog, template,
adapter, profile or generated-code changes are part of this optimization.

**Owner and checks:** implementer3 may own only
`servers/ruby/lib/haveapi/documentation_locale.rb` and focused additions to
`servers/ruby/spec/documentation/locale_spec.rb`, after any B edits to that spec
are committed/released. A0's native helpers/views/JS package remains independent.
Verify repeated static-label lookup counts, per-locale separation, fresh-request
and exception cleanup, caller mutation isolation, unchanged default/interpolation
behavior, missing nil and hash results, English fallback and locale restoration.
Run existing focused locale checks and style/hooks; preserve existing security
and body-parity evidence rather than adding a benchmark framework. Affected
independent review covers cache lifetime/isolation, output semantics and checks.
After native selection and this change are complete, repeat one bounded combined
probe on the exact final source, then the required original-base/exact-final-head
comparison. Do not infer hosted success from this prototype or retry inconclusive
timing automatically. No further optimization family is released by this brief.

## Available-renderer list follow-up

The complete `699197892372982e797010f166b97176268deec6` diagnostic, including
native selection and static labels, still exceeded e7 by 151/122 allocations
(`final-combined-allocation-summary.json`). Earlier partial probes therefore do
not establish final acceptance. The next bounded target is repeated renderer
availability, not further translation or template changes.

`ServerHelpers#documentation_clients` (`server.rb:279`) filters all 15 registered
renderers on every call, deriving a profile Context for each. Overview, panel,
native selection, sidebar metadata, layout metadata and legacy links reuse the
same version, authorized description and profiles within the request. The actual
699 probe found seven list evaluations and 116 Context calls. A single
request-instance list memo reduced evaluations to one and Context calls to 26,
saving 834/828 English and 831/829 Czech allocations/request with identical
complete HTML hashes. `available-clients-memo-probe.json` binds this in-memory
prototype to source snapshot
`36dd8429c389545aa90bb47f9b402df1cd0e42277e20412c70cccd947bc6402a`;
existing size-8 scenarios, two warmups, three batches of eight, setup excluded.
This remains diagnostic evidence, not the final hosted comparison.

**Minimal contract:** memoize only the filtered list in the Sinatra request
helper instance (e.g. `@documentation_available_clients`). Compute it lazily
using the existing filter and Context construction after the request's authorized
description exists. Preserve registry order and profile checks, including an
empty list; consumers treat the list as read-only. Every new request independently
evaluates availability, including a different identity, version, locale or profile
configuration. No class/thread/global state, Context mutation or cross-request
cache. Availability is a property of that request's snapshot; per-action rendering
and limitations still execute normally. Do not memoize `documentation_client_metadata`:
its detail union grows as panels render (`example_variants_spec.rb:39` explicitly
requires this), and its labels retain their existing locale lookup behavior.

**Bounded execution:** lead may assign the change to A0 after the current source
slot is released. Source scope is only `documentation_clients` in
`servers/ruby/lib/haveapi/server.rb`, with focused coverage in
`servers/ruby/spec/documentation/client_overview_spec.rb` (or one focused
availability spec). Verify availability once per renderer per request, fresh
decisions on consecutive requests with different available profiles/authorized
descriptions, unchanged order/empty behavior and live page detail accumulation.
Reuse native selector, profile, authorization and HTML/code parity checks.
Any useful extension-contract sentence belongs beside `available?(context)` in
`doc/en/client-examples.md`; do not change adapter interfaces. Apply ordinary
style/hooks and affected independent review for request isolation and preserved
availability semantics. Probe the completed combined source once, then run the
required exact-head original-base comparison; no budget/reference/harness
changes, alternative optimization package or preview replacement is implied.

## Three UI/example refinements after 51047

Baseline: clean published `51047a211d71f817ab25f2def1692517f00c15c6`.
One complete narrow package belongs to implementer0; no parallel source split
or new catalog/interface is needed. Lead explicitly accepted the shared Ruby
wrapper consequence below. The existing 51047 preview stays running until a
committed, reviewed and checked successor is ready.

1. **Hide singleton example detail.** In `version_sidebar.erb:71`, hide the
   entire `data-detail-control` label/select when the selected client's page
   detail union has fewer than two entries. Keep the disabled singleton select
   and existing hidden `example_detail` scalar for native GET submission. In
   `documentation.js:725`, derive the wrapper's `hidden` state from the same
   count on every update instead of always assigning false. Retain the DOM so
   switching to a two-detail client immediately reveals the control; preserve
   saved Thorough preference, per-group Simple fallback and current immediate
   selection. Do not change language/client selector behavior or persistence.
2. **Load the Ruby client before rescue scope.** `ruby_client.rb:16-35` embeds
   `require 'haveapi/client'` in `initialization`, which all three thorough
   callers pass into `with_error_handling` (init, auth and action examples).
   Separate the authored load preamble from constructor/setup statements at
   these existing assembly boundaries; emit the require once, unindented,
   followed by a blank line and `begin`. Constructor, `api.setup`, authentication
   and action operations stay inside the existing rescue scope. Do not split
   or rewrite already-rendered source. The shared fix intentionally changes
   require placement in all three thorough call sites, as accepted by lead;
   this is the sole exception to exact old English program bytes. Preserve
   Simple output, current handlers, literals and comment emission/localization.
   Basic, token credentials, token continuations and reuse-token comments use
   the corrected auth path. OAuth2 remains its localized unsupported comment;
   malformed/unsupported authentication remains a limitation, not a fabricated
   program. Loading errors propagate before rescue constants are evaluated.
3. **Switch user before Sign out.** In
   `version_sidebar/authentication_control.erb:7-18`, move the existing
   conditional switch-user form before the ordinary logout form. Preserve
   signed-in/capability conditions, POST target, CSRF field, `switch_user=1`,
   localization keys and logout semantics. DOM order supplies visual and
   keyboard order; no CSS ordering or OAuth implementation change.

**Files and checks:** source paths above are under
`servers/ruby/lib/haveapi` (`public/js/documentation.js` and
`client_examples/ruby_client.rb` respectively). Update existing focused
`spec/documentation/example_selection_spec.rb`,
`spec/client_examples/assets/documentation_test.cjs`,
`spec/client_examples/detail_spec.rb`/`syntax_spec.rb` and the appropriate
`spec/documentation/oauth_spec.rb` rendering assertion. Correct the now-obsolete
“Examples stays visible” sentence in `doc/en/documentation-ui.md`. No catalog,
generated adapter, locale helper, query parser or storage changes are needed.

Verify hidden singleton and visible two-choice controls in server HTML and JS,
including two→one→two switching without erasing saved detail; native Apply must
submit exactly one `example_detail` and retain page/resource/q/doclocale.
Cover Ruby Basic/token (including continuations) plus init/public/protected
actions in both detail modes: parse emitted Ruby, assert require precedes begin
exactly once and setup stays inside, and use a focused load-failure execution
check so loading cannot enter an application rescue handler. Retain existing
en/cs noncomment parity and comment-inertness tests; only scoped old-baseline
require-position assertions may change. Assert account form order with both
capability states and unchanged method/action/CSRF fields; reuse existing
switch-user/logout security tests. Run affected Ruby/JS checks, style and hooks,
then affected independent review and required exact-head checks. Use the
existing browser harness with JS enabled and disabled to confirm selector
visibility/submission and account order before preview refresh. No API, schema,
dependency or persisted-state change; ordinary code rollback remains valid.
No integration or lifecycle action is authorized by this refinement.

## Go/HTTP visibility report: retained asset diagnosis

On published/live `ef4c0cdcb349815538bb93cedab9d3964c565998`, the singleton
selection logic is correct in fresh browsers. Architect and owner2 reproduced
real Go/HTTP states across overview, authentication and public Test pages, with
and without JS; owner2 additionally covered both locales (24 states). All have
`details: [simple]`, hidden wrapper, computed `display: none` and zero geometry.
See `singleton-live-diagnosis.json` and `preview-go-http-live-probe.json`.
HTTP declares Simple only; Go's adapter offers two choices only for a successful
action whose operation-status metadata is visible (`clients/go/.../documentation.rb:74`).
The current fixture's Go groups are Simple only. Preserve these capabilities;
a real page union with two formats must still show the selector.

**Reproduced cause of the reported appearance:** `views/main_layout.erb:8-9`
uses stable `/js/documentation.js` and `/css/documentation.css` URLs. Actual live
responses have Last-Modified, but no Cache-Control or ETag. HaveAPI leaves
Sinatra 4.2.1's `static_cache_control` at its false default; `static!` delegates
to Rack file serving without a cache directive. Browsers may heuristically reuse
these assets after fetching fresh `private, no-store` HTML. In a disposable
loopback server, current ef4 HTML with actual 510→ef4 asset bytes and original
file timestamps reproduced exactly this: Chromium requested the assets once,
then reused old JS after the server switched to ef4. Both Go and HTTP Simple-only
selectors became visible because 510 JS assigns `hidden = false`. Giving the
script a new URL fetched ef4 and hid both. Evidence:
`singleton-warm-cache-diagnosis.json`. This proves the failure mode, not the
contents of the user's own browser cache; no live source/service changed.

**Small fix, implementer0:** give the two built-in documentation entry assets
content-based query versions. In `documentation_helpers.rb`, compute a fixed,
frozen map of SHA-256 digests for `public/js/documentation.js` and
`public/css/documentation.css` once when the code is loaded, with paths relative
to that installed file. In `views/main_layout.erb`, append each file's digest
as `?v=<digest>` to its existing mount-aware URL and keep normal escaping. No
per-request file reads, dynamic asset discovery, mutable process cache, build
manifest, package-version substitution or timestamp versioning. No public
interface or static route changes; existing direct URLs remain valid. Changing
either asset changes its own URL on the next application load, including rollback.
Do not rely solely on adding cache headers now: already-fresh old cache entries
would still be used for unchanged URLs. Leave worker assets, renderer metadata,
visibility logic, preferences and OAuth behavior alone.

The independent label request is canonical English
`haveapi.documentation.labels.programming_language: Language`; Czech remains
`Jazyk`. A0 reports this already committed as `50ae16c6`, with canonical catalog,
generated server locale and focused assertion only. Preserve that work and do
not introduce a duplicate label key or revise unrelated prose.

**Acceptance and boundary:** one A0 package, limited to the fixed digest map,
main layout and focused assertions in `spec/documentation/navigation_spec.rb`
and `shared_pages_spec.rb` (both already assert exact mounted asset URLs).
Verify emitted digests against
actual files, stable URLs for unchanged bytes, changed URL for changed asset,
mounted-prefix preservation, escaping and ordinary static retrieval with query.
Using the existing Chromium tooling, warm the previous stable script URL and
then navigate to candidate HTML: it must request the digest URL and hide real
Go/HTTP singleton wrappers; retain zero geometry and valid one-scalar native
Apply. Test en/cs and two-choice reappearance without changing capability data.
Fresh-context visibility checks alone do not cover this regression. Reuse the
existing browser asset, label, native selection and JS checks; ordinary focused
style/hooks, affected independent review and exact-head final checks precede
preview refresh. Preview remains ef4 until released. No dependency, API, schema,
persistent preference, lifecycle or integration change.
