# Check action metadata permissions and association expansion

Three new API expectations failed during the network visibility follow-up even
though the list predicates returned the expected rows.

HaveAPI 0.29.8 applies an action's input authorization whitelist to global
metadata too. `IpAddress.Index` omits `count` for non-admins, so their request for
`_meta.count` is ignored and the response has no `total_count`. Verify the real
restricted query's count and cursor traversal without adding an API capability
just to satisfy a new test.

Requested includes also depend on the action's existing expansion path.
`IpAddress.Show` and `IpAddressAssignment.Index` do not call `with_includes`;
their association references remain unresolved. An association ID and its
`_meta.resolved=false` marker are different from an expanded resource object.
Check direct permitted Show access separately, and test expanded associations
through actions that already support them, such as IP and host-address Index.
Do not silently change Show or association permissions to repair a test's
assumption about the response shape.

The evidence is in
`work/2026-10-05-network-ipv4-left-counter/visibility-quick3-api-core.json`.
These are source-established contracts at V `be136b6c` and the installed HaveAPI
version; they are not claims about every action or later framework release.
