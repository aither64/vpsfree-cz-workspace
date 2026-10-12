# Functional review reconciliation

Reviewed functional heads and full findings are in review-packet.md and the four
lane artifacts. Reviewers used gpt-5.6-sol with xhigh effort and fresh context.
Risk was high because of live-table indexes and the cross-repository payload.

- General: no findings.
- Scope: no findings.
- Risk: one Advisory about missing MailTemplate variable metadata. Added the four
  Hash keys and checked the registry alongside the generated sections.
- Architecture: three Advisory findings for duplicated active-session policy,
  recovery-stage/deadline logic, and auth-type catalogs. Initially the first two
  were Important; evidence-based reconciliation established verified current
  parity and no narrow extraction that actually removes duplication without
  modifying auth or cleanup callers. The architecture reviewer revised both
  to Advisory. Retain report-owned SQL, boundary fixtures, and explicit comments.
  A dedicated domain refactor is deferred until those rules change.

Final narrow edits also add a Storage heading after the new HTML sections.
They add no new behavior beyond the reviewed payload; focused checks suffice
under the review skill's rerun criteria. All 17 report specs and the template
flake check pass after these edits. No Blocking or Important findings remain.

Residual limits: separate eager queries can observe concurrent state changes;
the report is a generation-time snapshot, not exact historical reconstruction.
Synthetic EXPLAIN verifies index selection, not production index-build cost or
latency. Explicit database migration is needed on the API hosts, where autoSetup
is disabled. No live migration/deployment is authorized here.

Configuration pins will receive a separate committed-range review once the
functional heads are pushed and available to Nix.

Final functional heads after narrow fixes:

- vpsAdmin: `9456fae6f181cef2e8982eed462e873095fd49da`
- templates: `08402ffd8010384f950b1ec4a1b95de8e5410ba3`

Both are pushed on `2026-09-14-daily-report-sessions`, based on freshly fetched
unchanged origin/master revisions. Commit hooks passed. Local delivered-mail
integration has started with short state directory `/tmp/dr-test.Y0gjeo`.

## Final configuration review

Range: 249bed1ee28e69a907edd09ea97a1144dbcdefeb..5036135728832d5c375705e3b69949c33460ff7e.
Fresh general and risk agents used gpt-5.6-sol/xhigh; both returned no findings.
See review-pins-general.md and review-pins-risk.md. Exact remote heads, follows,
unchanged unrelated inputs, and API1/API2 topology were verified. Configuration
push and both API builds can proceed.
