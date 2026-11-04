# Rust Phase 1 prose approved by lead

Lead applied vpsfree-user-facing-writing and humanizer-en; approved wording.
Reconcile against generated output before committing. The final
release version depends on the full public-interface diff. The candidate is
0.2.0 under this crate's compatibility policy.

## README: replace public-snapshot coverage paragraph

Successful calls return typed `output`, action metadata in `meta` and
`http_status`. Output fields use `Option`: a missing or null field becomes
`None`. Related objects can be partial; the client does not fetch them
automatically. The generated client describes API 7.0 from vpsAdmin source, including
all six bundled plugins. Server permissions and installation-specific plugin
availability still apply.

## Crate documentation opening

Typed client for the declared vpsAdmin API 7.0 with all bundled plugins.

See the repository README for API coverage, authentication and regeneration
instructions. Enable `blocking` for synchronous callers.

## Development guide: saved schema section

`schema/api-7.0.json` is the canonical sanitized API 7.0 schema exported from a
clean, committed vpsAdmin checkout by `tools/export-api-schema`. The exporter
mounts the API with all six bundled plugins and English fixture data in a new
temporary database. Profile `vpsadmin-full-fixture` describes declared operations
and parameters. It does not describe a user's permissions or certify a deployed
installation's capabilities. Exporting does not contact a deployed API.

`schema/source-provenance.json` retains the exporter's source revision, plugin
and fixture/configuration hashes, dependency identities and schema digest.
`schema/tooling.Gemfile.lock` retains its exact dependency graph.
`schema/provenance.json` binds that receipt and schema to this client's generator,
copied runtime, generator dependency lock and toolchain. `schema/inventory.json`
describes the exported resources, actions and parameters.

To refresh the schema, follow vpsAdmin's
`docs/api-schema-export.md`, review the source export and retain its schema,
provenance and tooling lock together. Update client provenance and inventory,
then regenerate from the saved schema using the pinned generator. Never save
credentials, database URLs, login responses or transient tokens.

The sanitizer removes prose, examples, validator messages and protected defaults
while preserving wire names, paths, validators, namespaces and nullability.
Canonical JSON sorts object keys, uses two-space indentation and LF newlines,
and ends with a newline. Arrays keep their order.

## Changelog: new release additions

- Regenerate API 7.0 from the vpsAdmin source fixture with all bundled plugins,
  retaining the exact source and exporter provenance.
- Add advisory retraction and deletion operations and `expected_state` inputs
  for advisory, CVE and node-status mutations.

Move the existing Unreleased generator-maintenance entries into this release.
Add concrete compatibility notes after the complete generated diff is assessed.
No publication or server deployment is implied by this draft.
