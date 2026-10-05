# Filesystem scrape-job scope investigation

Investigated after the user requested critical alert removal by machine type
and asked the lead to check other relevant jobs. Current source/compiled-config
revision: f725dd3f407b0e5b82c9f9c1ad7720bbc7b14b68, prior local mon1 build generation
2026-10-03--17-18-19. This is configuration inspection, not live metric discovery
or deployment-state evidence.

| Job | Node-exporter endpoints | Configured machine types | Source |
| --- | --- | --- | --- |
| infra | 50 | 44 vps, 3 vm, 3 physical groups | Cluster inventory and infra exporter constructor |
| nodes | 13 | physical | Cluster node metadata/shared node labels |
| mon | 2 | vps: mon1 and mon2 | Managed container IDs 14005 and 19501 |
| meet-jvbs | 11 | unclassified; no machine_type | Address-only videoBridges in data/meet.nix |

Only modules/clusterconf/monitor/default.nix provides scrapeConfigs in the
repository. Its direct node-exporter references cover mon, infra and nodes.
The compiled Prometheus YAML also identifies meet-jvbs targets on port 9100;
data/meet.nix explicitly pairs that port with 9700 for each bridge. Architect
confirmed commit 0e8aeac7 introduced the node and Jitsi exporter pair. Other
configured jobs scrape service, ZFS, IPMI, log or probe metrics.

The same common FilesystemCritFreeSpace rule currently has no job restriction.
A global positive machine_type=~"vm|physical" numerator selector would remove
critical alerts from known VPS monitors as well as infra VPS, and would also
silently remove them from all eleven unclassified video bridges. Warning rule
is independent and can remain unchanged. NodeFatalRootfsFreeSpace is a separate
severity-fatal rule and remains outside this requested critical policy change.

No Meet/JVB host definitions or classifications were found in cluster/ or the
site data inventory. DNS/address records identify endpoints, not virtualization.
Do not infer a type from their public IPs. User saw the four-job inventory and authoritatively confirmed: "the video
bridges are VPS, you can add the label to them". Their classification is now
settled. Add machine_type=vps to Meet targets, then use a positive vm|physical
filter globally for the common critical alert, with no legacy-job fallback.
This intentionally removes that critical alert from mon and Meet VPS as well
as infra VPS; warning visibility remains.
