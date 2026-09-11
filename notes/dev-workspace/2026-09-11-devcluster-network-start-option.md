# Development-cluster providers have different network defaults

Related initiative: `work/2026-09-11-devcluster-packaging-investigation/`.

The OS provider parses an omitted `start --network` as `local`, including when
an existing cluster was configured for bridge networking. vpsAdmin instead
uses bridge by default. Pass `--network bridge` explicitly on both providers
to follow workspace policy and avoid confusing these defaults. Neither parser
uses the previous start's network selection as its command default.

Omitting the option in final OS acceptance started the owned VM locally; it
was stopped normally and restarted explicitly on bridge. The vpsAdmin start
was already on bridge, as confirmed by its QEMU network arguments, despite
an initial mistaken assumption that both defaults matched. It was also
interrupted and repeated. Retained NixOS image inodes/sizes were unchanged.
