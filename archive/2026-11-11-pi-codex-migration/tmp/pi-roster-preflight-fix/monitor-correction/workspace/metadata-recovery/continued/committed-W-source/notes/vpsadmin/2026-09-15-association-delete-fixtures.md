# Deleting membership rows in API fixtures

In the IP allocation race specs, `network.location_networks.delete_all` raised
`ActiveRecord::NotNullViolation: Column 'network_id' cannot be null`.
The association defaults to nullifying its foreign key when removing members;
this is different from a class-level relation's `delete_all`.

For a fixture deliberately simulating a completed membership removal, use
`LocationNetwork.where(network_id: network.id).delete_all`. Keep normal model
or operation paths for behavior whose callbacks are part of the test.

Related initiative: `work/2026-09-09-ip-release-mechanism/`. The first writer run
passed its product assertions; these two fixture failures were then corrected.
