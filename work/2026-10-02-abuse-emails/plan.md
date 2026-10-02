# Abuse email parsing and content preservation

## Goal and authorization

Support all nine supplied report formats with one incident per incoming report:
extract its declared source IP and event time, look up the historical assignment
once, and preserve the original readable content. User authorized the replacement
plan with "Implement the plan." after choosing all-nine scope and human-readable
body/text evidence without a raw JSON dump. Original inputs and raw copies stay
outside version control. No merge, deployment or live replay authorization.

## Implementation contract

Architect owns the revised [design](design.md); implementer owns configuration
parsers, tests and owning API README. Lead owns plan/state, writing pass, review
and verification coordination. Existing legacy provider paths remain supported.

Metadata only: Blocklist/CEDO structured Source/Date; Provider.tools Source and
Last seen; Burina subject IP and maximum timestamp prefix in its log section;
LRob JSON source/timestamp; Cisilino matching subject IP slots and UTC Last seen;
Custom Visuals subject IP and precise numeric-offset last-record prefix. Keep
existing narrow identity/profile and required source/date/MIME validation.
Preserve the nine expected instants, fractions and accepted yearless 31-day rule.

Use original subject without RT prefix and decoded human body/plain attachments;
append LRob decoded textual evidence. No individual-attempt interpretation,
source extraction from logs, ownership-range checks, A/B/A rejection, filtering,
counts or generated summaries. Unused optional fields are forwarded, not
validated. Original wrapping/wording stays, with existing decoding/newline/edge
whitespace handling. Keep storage bounds, no silent truncation or fallback.

Whole-body forwarding intentionally retains earlier/repeated/unrelated records.
The event owner receives the entire report; per-record ownership isolation is
not a requirement. Source-like text in usernames/victim logs never selects an IP.

## Compatibility and documentation

Only vpsfree-cz-configuration API hook/spec/docs change. Unchanged vpsAdmin
incident-array interface, schema, clients/CLI, daemons, Nix options and pins.
Older code can read saved reports; no node coordination or migration. Rollback
restores recognition behavior without retracting existing incidents/mail.
Supported behavior belongs in configs/vpsadmin/api/README.md; exact revision,
verification and rollout state remain here. Superseded restrictive policy will
be replaced in current design/docs and unmerged feature history.

## Verification and delivery

Prove all nine routes/times, original subject/full readable content, one event-
time lookup, unknown SSH wording/other-IP text preservation, dry-run no saves,
normal persistence, required metadata errors, storage bounds and legacy behavior.
Replace range/filter tests with accepted forwarding and selected-time ownership
checks. Originals remain private; committed fixtures are independently synthetic.

After quick RSpec/lint/hooks and lead writing pass, consolidate the undeployed,
unmerged feature into one coherent rewritten commit. Reconfirm provenance and
fetch/rebase as needed; do not rewrite master. Independent retained reviewer
reviews complete base-to-head history/diff and no-migrations inventory across
all four lanes, with explicit accepted whole-body forwarding policy.

Then fresh Luna/low watchers run adapted isolated pinned-schema database/original
checks and targeted int.api1 configuration build at final head. Verify exact
subject/text/timestamp roundtrips, historical owner and inclusive boundary;
cross-history cases now succeed. Capture comparison and guarded force-with-lease
feature push after checking expected remote head. Leave session/branches open.
