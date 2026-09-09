# IP accounting audit

## Goal

Add a read-only vpsfree-maintenance-tasks script that exports users with IP
accounting discrepancies to JSON for administrators to reconcile later.

## Affected repositories

- vpsfree-maintenance-tasks: new dated task, documentation and focused tests.
- vpsadmin: reference checkout only; establishes accounting semantics and test
  runtime. No changes to API, nodes, clients or configuration are planned.

## Approach

Compare IP inventory, confirmed/enabled resource use, UserClusterResource
limits, and sums of assigned package items per user/environment/IP resource
(ipv4, ipv4_private, ipv6). Count IpAddress.size, not address rows or expanded
IPv6 hosts. Count owned addresses once, including unassigned reservations;
attribute userless VPS addresses to the VPS owner. Use charged_environment_id
for accounting. Report uncharged inventory separately rather than guessing its
environment. Include identifiers and contributing records in discrepancies.
Packages already determine UserClusterResource.value and must not be added to
it. Report package/limit drift as well as excess and inventory/usage drift.

Read a consistent database snapshot without data changes, locks, resource
reallocation, or automatic repairs. Write one versioned JSON document only
after collection succeeds, with deterministic ordering and exact integer
amounts encoded as decimal strings. Include a summary and documented exit codes.

## Compatibility and deployment

The script targets the current vpsAdmin model/schema and runs through the
existing vpsadmin-api-ruby wrapper. Existing scripts remain unchanged. No
schema, persisted-state, API, client, protocol, Nix option, or daemon changes;
no deployment ordering or coordinated node upgrade. Rollback removes the task.
The output is a new admin-facing contract, with no existing automated consumer.
A consistent snapshot can still observe transactions in progress; administrators
must review and rerun findings before reconciliation. No production execution,
repair, merge or deployment is requested by this development task.

## Testing plan

Use focused database-backed tests with the vpsAdmin API development runtime to
cover inventory overages despite stale usage, matching accounts, package drift,
resource-use confirmation/enabled states, ownership and charging environments,
IPv4/private IPv4/IPv6 size accounting, missing charging/resource records, exact
JSON values and output/error handling. Run syntax/diff checks, then commit and
perform the mandatory adaptive change review before any longer tests.
