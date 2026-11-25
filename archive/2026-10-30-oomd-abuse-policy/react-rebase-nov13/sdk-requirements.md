# React incident SDK boundary, 2026-11-13

Main `88ac13b89d6421c914cd57e18153de1fee6fc7b7` uses generated
`vpsadmin-typescript-client@0.4.0` with `haveapi-client@0.32.0`. The incident
feature must use its generated operations through existing `getApi` policy;
no raw transport, type cast, local unknown-field shim or copied generated SDK.

Required existing operations/types:

- `getApi().vps.index`: `Vps__IndexInput` adds optional read selector
  `incident_policy`, status and boolean `incident_enforcement_enabled` filters.
  Initial reads omit all three; generated input must not force the selector
  onto initial calls to older APIs.
- `getApi().vps.show`: `Vps__ShowInput` accepts optional `incident_policy`.
- `getApi().vps.update`: `Vps__UpdateInput` accepts `incident_policy` plus
  nullable positive integer `incident_warning_limit_override`,
  `incident_stop_limit_override`, and non-null boolean
  `incident_enforcement_enabled`. Existing unrelated updates still work.
  Backend validates explicit selector/isolated writes atomically. Null reset
  must survive actual generated serialization.
- `Vps__IndexOutput[number]` and `Vps__ShowOutput` preserve the full selected
  flat summary: `incident_policy`, `incident_policy_label`,
  `incident_count_7d`, `incident_count_30d`, `incident_warning_limit`,
  `incident_stop_limit`, nullable admin raw overrides,
  `incident_enforcement_enabled`, `incident_mode`, `incident_stop_enforced`,
  `incident_status`, nullable `incident_last_incident_at`,
  `incident_last_warning_at`, `incident_last_stop_at`,
  `incident_next_stop_allowed_at`, `incident_accounting_since`,
  `incident_action_state`, nullable integer `incident_action_chain_id`.
  Missing capability fields remain unavailable, never invented defaults.
- Update result/meta retains synchronous absent/null action state; any supplied
  receipt remains validated by current WebUI helpers.

The source contract is the existing released `implementation-contract.md`.
New ordinary incident-report localization is stored backend message text and
requires no React locale fields or selector changes. Do not invent a client
release/version or claim publication. Please supply exact generated source,
schema/generator provenance and, for development, a verified packed artifact
with SHA-256; main's SDK contract permits an explicit temporary local artifact.
Before merge a published registry release with provenance is required.

Testing uses main's existing `apiWire` controlled XHR through the actual client,
not `fetch` stubs. Representative current snapshot must preserve wire selectors,
nullable resets, owner scope, all fields and old-API reads. Synthetic second-rule
test responses stay test-only and do not add a production registry entry.

Owner1 inspected retained generator1ef9b204: selector/status emit primitive
strings and descriptors carry kind/required/nullable; backend include validators
are not generated client enums. Preserve that existing provider boundary. Earlier
"preserve generated choices" wording was not a request to add enum validation.
The server remains authoritative for registered keys/status choices. Verify
generated primitive/null validation, selector omission and actual server rejection
separately; do not infer registry acceptance from a mock synchronous response.
Architect/lead confirmation of this interpretation was requested directly. No
generator correction or client-side shim has been requested from this fact alone.

Architect confirmed this exact boundary in `design.md`, “Generated choices
clarification (2026-11-14)”. Actual generated primitive/null errors are tested as
`ClientInputError` without HTTP sends; unknown string registry refusals use the
normal server error path. Existing defensive synchronous acknowledgement tests
retain their scope and never certify server registry acceptance. Owner0 has
published API7919441 with unchanged raw schema/provenance; owner1 is preparing
the exact package.

Rebase local preliminary head `574b1166e648d9edb360bb233b87bbd8883be3e7` is
not yet verified or published. Exact old source/review/failure/capture evidence
retained; main's SDK migration makes adapter resolution substantive. Lead owns
affected-review gate before publication.
