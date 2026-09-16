# Selection and member-view refinement review

Reviewed vpsAdmin 9840cdf08b9dbdb825bac0da04aa74281d3c4e2a (API 3fb0ab7f5),
KB e098f68845397a510dd4ed6638f0d50e8f52428c and unchanged notification overlay
715c063396fa49277852b98d36347c8bec5160d3. High risk: persisted schema, member
isolation and new public API fields. All four lanes used fresh gpt-6-astra/xhigh
contexts; general/architecture via collaboration, risk/scope via read-only
standalone CLI after the retained agent-thread limit refused another spawn.

## Findings and reconciliation

- **Blocking, general/risk (Important, scope): GET filter transport.** The
  pinned PHP client 0.29.6 casts custom array-valued query parameters to the
  string `Array`. Default preview and multi-select preview therefore fail.
  An in-memory sender reproduced the actual client's coercion/serialization.
  Fix: the campaign endpoint declares comma-separated String filters; the UI
  converts its multi-selections before calling that endpoint. The shared model
  normalizer accepts the scalar wire format and internal arrays. No generic
  HaveAPI/client change. PHP regression covers default and multi-value requests
  through the installed client. API request specs cover defaults, valid multiple
  values and invalid input. Owning docs and EN/CS metadata describe the format.
- **Advisory, architecture: member Notice history whitelist.** Existing fields
  were safe, but a blacklist would require future admin fields to be recorded
  separately. Fix: explicitly allow id, event, subject and created_at; assert
  exact response keys. Request/address member outputs already use whitelists.
- **Advisory test gap:** selection bookkeeping is covered across 1101 rows;
  browser coverage does not exercise multiple preview pages and settings through
  the complete POST/redirect path. The controller and saved-settings rendering
  were inspected; final integration covers normal selection, restoration,
  creation, notices, retention, assignment, release and closure. No claim of
  completed multi-page browser coverage is made.

No other findings. All reviewers confirmed the eight-commit split, unchanged
first six prerequisites and narrow companion KB pin. No node/runtime protocol
or generic lock changes are introduced by this refinement.

## Focused remediation verification

- Pinned PHP client transport: 1 test/2 cases passed (no network).
- API defaults/multi-select/invalid filters and member Notice history: 3/0,
  seed 10265, 1m40.54s plus loading.
- Commit hooks: lint, translations and migration coverage pass.

Transport correction is folded into vpsAdmin be21bc8b9e4101ca6b35654ad6f52147dea87213
(API ad203b205); the first six commits remain unchanged. General, architecture
and risk reruns on this committed correction completed with no findings. All
three used fresh read-only gpt-6-astra/xhigh contexts and independently checked
the pinned PHP client. The scope boundary is unchanged, so that lane was not
repeated. Deployment proceeded after reconciliation; the live campaign list and
500-address details now pass. Final isolated browser integration passed all five Playwright tests in8.7
minutes. The runner completed successfully including teardown (1518.56s total).
