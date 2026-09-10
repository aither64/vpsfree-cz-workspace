# 2026-09-10-netcraft-abuse-reports

## Goal

Recognize Netcraft extortion-mail abuse reports received through the abuse RT
queue and create one incident report for the member who held the source IP at
the reported event time. Repeated Netcraft reminders for the same case must be
processed without creating another incident or member notification.

## Affected repositories

- `vpsfree-cz-configuration`: extend the deployed JSON XARF decoder, provider
  policy, incident renderer, and parser specifications.

## Approach

1. Extend the existing generic JSON XARF decoder with an explicit adapter for
   the official legacy XARF version 1 shape used by Netcraft. Keep versions 1,
   3, and 4 as explicit adapters so unsupported versions continue to fail
   closed.
2. Normalize the version 1 reporter email, reporter case ID, reporter notes,
   disclosure flag, source IP, event timestamp, classification, and plural
   evidence samples. Preserve the existing strict IP, timestamp, Base64, JSON
   size, and decoded-evidence size validation.
3. Keep wire-format decoding separate from automatic-forwarding policy. Add a
   Netcraft provider policy alongside the existing Abusix policy. By default,
   require an RT originator of the form
   `takedown-response+<case-id>@netcraft.com`, matching reporter email and
   domain in the JSON, a matching reporter case ID, `Disclosure: true`, and the
   observed `Activity` / `Spam` / `Extortion Mail Server` classification.
4. Preserve the existing `CHECK_SENDER=0` operational override for sender
   identity checks without bypassing format, classification, evidence, IP, or
   timestamp validation.
5. Resolve the historical IP assignment using the JSON event timestamp. Render
   a stable subject and concise English incident text containing the source,
   UTC timestamp, Netcraft case ID, reporter notes, and decoded textual
   evidence. Do not forward delivery headers or reporter contact metadata.
6. Suppress repeated reminders by looking up an existing incident with the
   same user, VPS, IP assignment, stable subject, and detection timestamp.
   Return no incident for a duplicate while allowing the dispatcher to mark
   the incoming message as processed.
7. Base committed tests on a synthetic, redacted MIME fixture. Use the supplied
   messages under `tmp/netcraft-emails/` only for local dry-run verification.

Rejected alternatives:

- A Netcraft-specific prose parser would ignore the structured XARF attachment
  and duplicate the existing generic decoder.
- Accepting every Netcraft subtype or every XARF version would expand automatic
  member notification beyond the observed and reviewed report type.
- Adding an external-report-ID database column would require a cross-repository
  migration for a duplicate pattern that can be identified from existing
  incident fields.

## Compatibility and deployment

- No database, persisted-state, public API, generated-client, or protocol
  changes are required.
- Existing Abusix XARF v3/v4 behavior and all other abuse parsers remain
  unchanged.
- API instances can be updated independently. Old configurations leave
  Netcraft reports for manual handling; updated configurations create
  incidents and suppress later identical reminders.
- Rollback is safe. Existing incident rows remain readable and later Netcraft
  messages return to manual handling.
- The implementation, review, push, integration, deployment, and archival are
  separate gates. Do not merge, deploy, or archive without explicit user
  direction.

## Testing plan

- Add decoder coverage for a valid version 1 report, plural evidence, normalized
  reporter metadata, and rejected malformed or unsupported fields.
- Add parser coverage for valid Netcraft identity correlation, the exact
  allowed classification, historical assignment lookup, stable member-facing
  output, disclosure handling, unsupported evidence, and missing assignments.
- Add a duplicate-reminder test which seeds the first incident and verifies
  that a `Re:` message carrying the same JSON is processed without creating a
  second incident.
- Add dispatcher coverage proving that the recognized Netcraft message is
  routed by MIME content and that sender mismatches remain unidentified under
  the default sender policy.
- Run focused RSpec and RuboCop, then full RSpec and RuboCop. Dry-run both
  supplied messages with a synthetic assignment.
- Commit all intended changes and run the mandatory high-risk change review
  with general, architecture, scope, and risk lanes at `xhigh` before the long
  configuration builds.
- Build `cz.vpsfree/vpsadmin/int.api1` and
  `cz.vpsfree/vpsadmin/int.api2`, then push the reviewed feature branch over
  SSH and inspect any GitHub Actions feedback for its exact head.
