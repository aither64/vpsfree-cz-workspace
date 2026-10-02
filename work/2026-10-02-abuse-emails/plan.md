# Abuse email parsing extension

## Goal and authorized scope

Inspect the nine user-supplied RT abuse messages and the existing
`vpsfree-cz-configuration` parsers, then propose an extension that creates
correctly attributed incident reports. This turn is investigation and design.
Implementation, sending reports, deployment and integration are future work.
Keep the supplied emails and any raw copies outside version control.

## Affected repositories

- `vpsfree-cz-configuration`: `configs/vpsadmin/api/incident_reports.rb`,
  provider parsers, parser specifications and API configuration documentation.
- Coordination workspace: this session's plan, state and architect brief.
- vpsAdmin's incident-array interface is a compatibility boundary; changes to
  vpsAdmin are not currently expected.

## Approach

The retained architect owns the technical proposal and verification brief in
[design.md](design.md). The lead independently inspects the inputs and routing,
reconciles the proposal, and obtains independent review before presenting it.
Classify structured X-ARF attachments, inline structured reports and prose/log
reports. Prefer narrowly recognized formats with explicit offending addresses
and event timestamps over broad subject or arbitrary-IP extraction.

## Decisions and compatibility

Preserve historical IP assignment lookup, existing provider handling and dry-run
semantics. Distinguish event time from receipt time, source from victim address,
and allegation from verified activity. Keep reports scoped to their owner.
No schema, on-disk format, API/client, CLI/Terraform, daemon protocol or node
configuration changes are expected. Parser deployment belongs to API
configuration; mixed API versions retain the incident-array contract. A rollback
restores old recognition behavior without retracting existing incidents or mail.
The detailed proposal must identify any exception to these assumptions.

## Documentation

Readers: maintainers implementing the parsers and operators validating rollout.
Current proposal and temporary evidence belong in this session. After
implementation, supported parser behavior and recovery guidance belong in
`configs/vpsadmin/api/README.md`; entry point is the repository README.

## Verification plan

Map all nine tickets to routing gaps and expected source IP/event time without
creating reports. Independently review the committed proposal. Future
implementation needs sanitized synthetic fixtures, handler-level routing tests,
timestamp and assignment assertions, malformed-input and privacy cases, legacy
regressions, and a dry-run replay of the external originals. Run the documented
RSpec suite in the repository Nix shell. Longer verification uses the mandatory
fresh watcher workflow; no build or deployment is needed for this proposal.
