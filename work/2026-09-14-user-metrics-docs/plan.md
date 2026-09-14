# User metrics documentation proposal

## Goal and scope

Provide a complete metric reference through the vpsAdmin API and WebUI, and
selected monitoring examples in the bilingual KB metrics article. Bind the
examples to the implementation through vpsfree-kb-contracts.

The current request is to suggest solutions. This document proposes a design;
implementation, deployment, and production KB writes have not been requested.

## Affected repositories

- `vpsadmin`: shared metric definitions, documentation resource, plugin support,
  translations, WebUI reference, and regression tests.
- `vpsfree-kb-contracts`: managed Czech/English metrics pages, executable
  Prometheus configuration and rules, semantic checks, runtime tests,
  navigation bindings, and any selected screenshots.
- No database, vpsAdminOS, HaveAPI, DokuWiki plugin, or configuration repository
  change is expected. Reassess only if implementation identifies a missing
  capability.

## Verified current behavior

Inspected fetched remote `master` on 2026-09-14:

- vpsAdmin: `791ab3aa89e2f613979da6090b89785c78245db5`.
- vpsfree-kb-contracts: `919577d0c770e47b623c591f8bf0cce4e8d30666`.

The user exporter is `api/lib/vpsadmin/api/metrics.rb`, served by `/metrics`
using metrics access tokens. `api/lib/vpsadmin/api/tasks/prometheus.rb` is a
separate infrastructure exporter and is outside this reference's scope.

Core and payments/outage plugin exporters already register names, types,
labels, and brief HELP strings. The token supplies the prefix, which defaults
to `vpsadmin_`. The current metrics version is 1.1. Registration follows token
authentication, which updates usage statistics; documentation must avoid that
authentication and computation path.

Details the reference must explain:

- Network transfer metrics are gauges populated from monthly accounting, with
  year, month, and direction labels. They are not instantaneous bandwidth
  counters. All currently registered user metrics are gauges, including values
  whose names resemble cumulative counters.
- Active nodes and their pools are included independently of a member's VPS
  placement. Other families have their own ownership and presence conditions.
- Conditional series need absence semantics: VPS expiration is set only when
  an expiration date exists. Defaults such as zero for an unknown boot time
  also need explanation.
- Outage labels include `outage_summary_<language>` for configured languages.
- Pool scan HELP has incorrect values. `Pool::SCAN_VALUES` yields 0 unknown,
  1 none, 2 scrub, 3 resilver, 4 error.
- DNS record priority HELP incorrectly describes priority in seconds.

Production pages were read through `kb-page get`: English
`manuals:vps:metrics` and Czech `navody:vps:metriky`. Both use the translation
marker `<page>manuals:vps:metrics</page>` and cover access setup, account
security, and versioning. Their navigation is contracted, but the pages are
not yet managed sources in `contract/pages.yml`.

## Alternatives

| Design | Advantage | Limitation |
| --- | --- | --- |
| Build from scrape HELP/TYPE | Small initial change | A member's scrape does not establish every possible value or presence condition. Categories and explanations still need another source. Requires a token and member data. |
| YAML documentation beside existing registrations | Easy to introduce and author | Duplicates names, labels, and types unless strict checks bind every registration. A viable transitional design. |
| Shared declarative metric definitions | Exporter, API reference, and contracts use the same definitions | Requires a contained registration refactor and preservation tests. Recommended. |

## Recommended API design

Introduce a small Ruby catalogue shared by core and plugin exporters. Keep
computations in the existing exporter classes. Registrations resolve their
name, type, labels, and HELP text from the catalogue. Avoid another list of
those fields in PHP or the KB repository.

Each definition provides a stable ID and basename; category and ordering;
short help and localized explanation; Prometheus type and unit; label
descriptions and finite allowed values; boolean/enum mappings, meaningful
bounds and sentinel values; resource scope; presence/default/reset behavior;
collection cadence where verified; and supplying plugin.

Distinguish timestamps, durations, ratios, percentages, counts, and currency
where applicable. Open-ended label values need descriptions and safe examples,
not a list of actual member resources. Reuse model enums and exporter constants
for finite values. Resolve dynamic labels with shared configuration-aware code.
Enabled plugins contribute definitions without a token or member records.
Validate duplicate IDs/names, missing descriptions, and incomplete label data.

Expose a read-only HaveAPI resource, tentatively `MetricDocumentation`, with a
versioned structured category/metric response. Recommend regular API
authentication initially; no metrics token should be needed, so members can
read the reference before creating one. Public access is an optional policy
choice for this definitions-only payload.

Separate the response schema version from metrics version 1.1. Localize prose
using existing API Czech/English locale handling and English fallback. Keep
names, label keys, enum codes, and IDs stable across languages. Extend locale
extraction if required so regeneration preserves the new strings. Keep scrape
HELP independent of the browser's locale.

Return basenames and the default prefix. The WebUI can offer a prefix field,
pre-filled from token details when entered there, without sending the secret
token to documentation requests. Stable anchors use IDs without the prefix.

Proposed categories: exporter/version; nodes and pools; VPS lifecycle; CPU and
load; memory and swap; processes; network transfers; datasets; incidents and
OOM; transactions; account security; DNS; payments; outages. Only enabled
plugin categories appear. Category membership belongs to the API catalogue.

## Recommended WebUI

Add a Metrics reference page linked from the token list and token details, with
a link to KB examples.

- Categories start collapsed and show title, summary, and metric count.
- The sidebar lists every category and metric, with its own scrolling region
  and filtering by metric name, label, or explanation.
- Selecting a metric expands its category, scrolls and focuses its heading,
  and updates a stable URL fragment. Direct links and back/forward do the same.
- Search reveals matching categories and entries. Provide expand-all and
  collapse-all controls and predictable behavior when clearing search.
- Entries show full name, type/unit, meaning, label/value tables, and presence
  or reset notes. Provide copy-name and copy-link controls.
- Use accessible disclosures, a compact index on narrow screens, and an
  expanded fallback without JavaScript. Escape API text and constrain markup.

Fetch the catalogue once per page. Cache only with deployment/catalogue revision
and locale, accounting for enabled plugins and configured language changes.

## KB examples and implementation contract

Keep an overview and scrape setup, followed by selected useful scenarios.
Link scenarios to stable WebUI metric anchors for the full reference. Preserve
the current account security and versioning content.

Suggested initial scenarios: scrape failure; a VPS stopped for a sustained
period; high memory use with guarded division; dataset free space; monthly
inbound/outbound traffic; approaching payment expiry; password generation
changes and a required password reset. Thresholds and durations are adjustable
examples. Explain custom prefixes, scope by scrape job, and avoid counting the
same account twice through multiple tokens. Distinguish scrape failure, absent
series, and a reported negative condition. Verify update cadence before
repeating the current KB's blanket two-minute guidance. Do not infer counter
behavior from names.

Register `metrics` in `contract/pages.yml` with both existing IDs, canonical
sources, claims, executable samples, and a `kb/metrics` suite. Preserve the
language mapping and add the existing `<kb-managed>` marker. Bind reference
navigation using the established WebUI documentation workflow; no new
DokuWiki syntax is needed.

Use three complementary checks:

1. Export deterministic JSON from the same catalogue code at the pinned
   vpsAdmin commit. Bind each KB scenario to its metric IDs and relevant types,
   units, labels, values, scope, and presence behavior. Detect relevant drift
   without making unrelated new metrics invalidate every example. Bind
   important computation semantics to focused source fingerprints and runtime
   checks; unchanged metadata does not prove unchanged exporter behavior.
2. Store displayed scrape configuration, recording rules, and alerts as actual
   fixtures. Existing sample checksums and localized comments keep both pages
   synchronized. Run `promtool check config`, `promtool check rules`, and
   `promtool test rules`. Test firing, non-firing, recovery, absent/stale
   series, zero limits, and monthly boundaries where applicable.
3. Use the pinned test cluster with controlled member fixtures and a metrics
   token. Scrape the actual endpoint with Prometheus and evaluate documented
   expressions. Check prefixes, plugin coverage, conditional series, and
   tenant isolation. Use synthetic series for long alert windows rather than
   waiting hours in integration tests.

vpsAdmin CI should validate catalogue completeness locally. Metric-affecting
changes must also update the exact vpsAdmin pin and run the external KB checks,
even if WebUI labels remain unchanged. The current cross-repository workflow
is operator-invoked; automatic cross-repository triggering is a separate option.

## Compatibility and deployment

- Preserve names, prefixes, types, labels, values, and access rules. Correct
  inaccurate HELP descriptions without changing numeric values. Any behavior
  change discovered during the work needs an explicit compatibility decision.
- No database migration, persisted format change, daemon protocol change,
  coordinated node rollout, or vpsAdminOS update is expected. Rollback has no
  new stored state to interpret.
- The API resource is additive. Existing API/CLI/Terraform clients and older
  WebUI versions continue to work. Verify the PHP client's structured response
  handling; no generated client change is expected.
- Deploy API support before WebUI. New WebUI should detect an older API and
  offer the KB link if the catalogue resource is absent.
- Keep metrics version 1.1 if export semantics are preserved. Version the
  documentation response independently.
- Pin committed vpsAdmin changes in vpsfree-kb-contracts. Run required adaptive
  review after commits and quick checks, before long integration tests, with
  xhigh review effort as required by workspace rules.
- Prepare complete bilingual candidates through kb-contract-fetch/build and
  schema-5 manifests with localized summaries. Stage and verify exact releases.
  Integrate contract changes before production promotion, which requires direct
  approval of the staged candidates.

## Testing plan and implementation sequence

1. Inventory every core/plugin metric's semantics, add the catalogue, and verify
   actual scrape parity with meaningful API specs on controlled fixtures.
2. Add localized API documentation. Check complete metadata, enum mappings,
   dynamic labels, and lack of token usage side effects.
3. Add the WebUI and focused browser checks for disclosures, filtering, direct
   links, keyboard navigation, localization, prefixes, and older APIs.
4. Adopt the bilingual KB pages and executable examples; check rendered sample
   parity, semantic dependencies, and Prometheus rule behavior.
5. Commit, run the required review, then affected browser/exporter/KB integration
   suites. Review staged pages and selected screenshots before publication.

## Primary references

- [User exporter](https://github.com/vpsfreecz/vpsadmin/blob/791ab3aa89e2f613979da6090b89785c78245db5/api/lib/vpsadmin/api/metrics.rb)
- [Pool enum definitions](https://github.com/vpsfreecz/vpsadmin/blob/791ab3aa89e2f613979da6090b89785c78245db5/api/models/pool.rb)
- [Managed KB contract](https://github.com/vpsfreecz/vpsfree-kb-contracts/blob/919577d0c770e47b623c591f8bf0cce4e8d30666/README.md#managed-page-contract)
- [WebUI documentation workflow](https://github.com/vpsfreecz/vpsfree-kb-contracts/blob/919577d0c770e47b623c591f8bf0cce4e8d30666/docs/webui-change-workflow.md)
- [Prometheus rule tests](https://prometheus.io/docs/prometheus/latest/configuration/unit_testing_rules/)
- [promtool checks](https://prometheus.io/docs/prometheus/latest/command-line/promtool/)
