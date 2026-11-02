# Node-exporter metadata for imported NixOS containers

The shared system monitoring module enables the exporter independently of the
cluster inventory. A new container can therefore build with the exporter
listening on 9100 while breaking both monitor builds because its cluster module
omits `services.node-exporter = { };`.

The monitor's infrastructure target generation requires the declared service;
`modules/services/definitions.nix` owns the default port. Follow neighboring
container declarations rather than weakening the consumer with a fallback.
Validate the real enabled service/port and evaluate the monitor consumers, not
only the new host. With no explicit monitoring target, the consumer uses the
host FQDN; the service metadata address is a separate value.

Evidence: [mx2 metadata correction](../../work/2026-11-01-mx2-nixos-migration/monitor-metadata-remediation.md).
