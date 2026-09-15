# Review cluster DNS secondary failed during RabbitMQ bootstrap

Initiative: work/2026-09-09-ip-release-mechanism.

After starting a single/bridge review cluster, PTR setup rolled back because
BIND rejected the reverse zone: `zone has no NS records`. Its public secondary's
`vpsadmin-nodectld.service` had exhausted the systemd restart limit while
RabbitMQ still refused its vhost access. The hidden primary had no completed
public-secondary NS registration. This was a disposable startup dependency
failure, not a PTR release-chain failure.

Inspect the actual unit `vpsadmin-nodectld.service` on DNS machines; querying
`nodectld.service` reports an unrelated nonexistent unit. Restarting the failed
unit after RabbitMQ permissions were ready restored transaction processing.
The secondary zone associations were recreated through normal API delete/create
chains and awaited to completion. No DNS files or transaction confirmations were
edited directly.

Verify against the configured DNS listen address, not 127.0.0.1. In this cluster,
NS queries then returned the public server, PTR creation completed, and an IP
release removed the smoke PTR while preserving a separate review PTR.
