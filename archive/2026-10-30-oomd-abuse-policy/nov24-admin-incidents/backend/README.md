# Nov24 backend implementation evidence

Base: `4062a8da3314aa7b48170b0d6f441446bad9b207`.

The projection/API/daily source uses the settled Nov24 design at design.md top.
No migration, engine mutator, schema, node or recipient change. Existing consumed
migration20261030180000 SHA256 remains2eec970fb3620ad25f3ac01c06a9eae61af2d208f88184e995c74b8ad2ba2c1e.

Focused logs/results preserve each native failure and its scope. They are not
summed as unique examples. Early corrected failures: resource constant VPS casing;
node domain is name+location.domain rather than a stored column; JSON_TYPE binary
collation; spec helper JSON double encoding; computed SQL time String UTC parse;
HaveAPI compatibility validation uses HTTP200 with status=false; render fixture
requires normal base_url and send-hook payload. Product assertions retained.

Catalog generation/health use ordinary distinct new fixture DBs and exact root
wording. Fresh watcher identity refusals are preflight limits, not check failures.
After those, active-parent native fallback owns remaining checks and joins.

The shared fixture is site7af51cd tests/fixtures/daily_report_incident_policy.rb,
SHA2569322962bb84636669e89bde6257791d56f55f5bb5cee9c027caa0d8d6b662c90;
HTML9c25a34f933742955709f50fd1a51e58c2b616602f41343848923c436d589cc3.
Focused9 actual full-mode shared TemplateBuilder seam and endpoint coverage:
2examples/0failures/native0,51.059s. No mail sent.

Final committed source/export/publication receipts follow in this same directory.
