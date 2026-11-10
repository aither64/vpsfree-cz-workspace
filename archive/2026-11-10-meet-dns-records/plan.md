# Meet DNS aliases

## Goal and scope

Add the requested CNAMEs to both public and private vpsfree.cz zones in
vpsfree-cz-configuration:

- auth.meet -> meet.vpsfree.cz.
- auth.test-meet -> test-meet.vpsfree.cz.
- turn.meet -> jvb1.vpsfree.cz.
- turn.test-meet -> test-jvb01.vpsfree.cz.

Compare existing meet records and fix only confirmed relevant private-zone drift
needed for these aliases. Preserve intentional private addresses and unrelated DNS.

## Delivery

Architect investigates the relevant definitions and records a bounded brief in
[design.md](design.md), accepted for implementation. One implementer owns zone edits, relevant quick checks,
hooks, commit, feature publication and evidence. Lead accepts the package and
assigns independent final review after the commit and quick checks. Publish the
feature branch; user approved integration into configuration master once verified.
User will deploy; no deployment is assigned to this session.

## Compatibility and recovery

Additive DNS aliases should work with existing services and split DNS. Verify
that alias targets exist in each view, avoid CNAME conflicts and preserve address
families. No database, persisted format, API/client or service protocol change is
planned. No coordinated node update is needed. DNS activation follows the
repository's normal zone deployment; rollback restores the previous zone data,
subject to DNS cache TTLs. No deployment is performed in this package.

## Documentation and verification

Readers are DNS maintainers. Record drift findings and checks in session records;
the zone data itself should suffice as durable reference for a small alias change.
Use repository instructions and Nix environment. Run syntax/format and targeted
zone validation, including both DNS views and target existence, then independent
final review. Broader checks only if local guidance or findings require them.
