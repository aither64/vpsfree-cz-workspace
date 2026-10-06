# 2026-08-19-abusix-reports

## Goal

Parse Abusix XARF spam reports received through the abuse RT queue and create
incident reports for the user who held the reported IP address at the event
time. Reject malformed, unsupported, or irrelevant reports without forwarding
them.

## Affected repositories

- `vpsfree-cz-configuration`: vpsAdmin incident-report parser configuration and
  parser specifications.

## Approach

Recommended design:

1. Add a generic XARF JSON decoder, separate from the permissive legacy `XArf`
   subject parser. Recognize the XARF feedback MIME marker and JSON attachment
   from message content instead of a provider-specific subject.
2. Normalize supported wire versions into one internal report shape containing
   the version, report ID when present, source IP, event time, category/type,
   sender/reporter metadata, disclosure setting, and evidence.
3. Implement a v3 adapter for the supplied messages and a v4 adapter against
   the current official schema. In v3, accept the observed singular
   `Report.Sample` evidence object and the standard `Report.Samples` array.
4. Keep acceptance and automatic-forwarding policy separate from format
   decoding. Initially trust only configured RT originators such as Abusix and
   auto-forward only explicitly allowed IP-based report types and textual
   evidence content types. Unsupported senders, source identifiers, categories,
   or binary evidence remain available for manual handling.
5. Validate the source IP and require an RFC 3339 event time with an explicit
   UTC designator or numeric offset, then resolve the historical IP assignment
   at that absolute time. An absent assignment makes the report irrelevant and
   produces no incident.
6. Render a small plain-text incident containing the report type, source,
   timestamp, relevant protocol fields, and allowed decoded evidence. Do not
   include reporter or complainant contact metadata. Treat malformed or
   unexpectedly large JSON/evidence payloads as unparseable.
7. Keep the legacy `XArf` parser unchanged until its existing fixtures establish
   whether it can later be folded into the same normalized representation.

Alternative designs considered:

- Add an Abusix-specific parser. This is the smallest change, but duplicates a
  standard format and would require another parser for every XARF sender.
- Accept every schema-valid XARF report for automatic forwarding. Reporter and
  sender fields inside JSON are self-asserted, and XARF supports sensitive and
  binary evidence, so schema validity and IP ownership alone are insufficient
  trust and disclosure controls.
- Extend the existing `XArf` class with a second unrelated wire format. This
  shares a name but combines broad sender matching with MIME/JSON processing,
  making review and failure behavior harder to reason about.
- Forward only the human-readable RT text. This identifies the IP and time but
  discards the attached redacted mail headers that users need to investigate.

## Compatibility and deployment

- No database, persisted-state, API, generated-client, or protocol changes.
- Existing abuse parsers and their forwarding behavior remain unchanged.
- API instances can be updated independently. Old instances will continue to
  leave Abusix reports unparsed; updated instances will create incidents.
- Rollback is safe: incidents already created remain readable, while later
  Abusix messages return to manual handling.
- XARF v3 is deprecated upstream in favor of v4, but Abusix still emitted v3 in
  the supplied August 2026 examples. Version adapters isolate the incompatible
  field layouts. Official v4 fixtures can test generic decoding, while an
  unobserved Abusix v4 delivery should still be monitored before relying on it
  operationally.
- The v4 forwarding policy accepts only schema-valid SMTP spam-trap reports:
  `protocol` must be `smtp`, `evidence_source` must be `spamtrap`, and
  the envelope sender and valid source port must be present. Other v4 messaging
  channels and user complaints remain for manual handling.
- Both samples set `Disclosure` to false and already replace complainant
  identity and message bodies with redacted values. Until the flag's operational
  meaning is confirmed, forward only the minimum technical fields and the
  already-redacted evidence, not the full JSON metadata.

## Testing plan

- Create synthetic fixtures based on the observed MIME structure; do not copy
  production IPs, addresses, message identifiers, or evidence into git.
- Cover a valid Abusix v3 spam-trap report with singular `Sample`, a standard
  v3 `Samples` array variant, and official synthetic v4 IP-based examples.
- Cover invalid JSON/base64, missing fields, unsupported version/type,
  unexpected sender/MIME structure, invalid IP/date, non-IP source identifiers,
  disallowed evidence content types, and no historical IP assignment.
- Assert that decoded evidence is included, institutional metadata is omitted,
  assignment lookup uses the JSON event time, and a valid report from an
  untrusted originator is not automatically forwarded.
- Run focused and full RSpec, RuboCop, and repository hooks before the mandatory
  independent change review. Build the relevant API configurations after the
  review, then push the feature branch and monitor CI.
