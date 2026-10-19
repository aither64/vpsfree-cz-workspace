# Staging reboot verification, 2026-10-18 after 22:10

**Autostart succeeded on both nodes: 107 selected containers, 107 unique starts, 107 successful outcomes, no observed failed or unresolved starts.** Neither new boot repeats the morning's child `EMFILE` opening `/proc/self/fd` followed by the parent's executor EOF. This is central-log verification of these boots, not a live state query or a guarantee of application health inside the containers.

All times below are Europe/Amsterdam, CEST (`+02:00`). Runit's embedded `20:xx` prefix is UTC; the outer `22:xx+02:00` timestamp controls chronology. Buffered records and duplicate boot banners were reconciled by timestamp and container ID, not line order.

| Observation | node1.stg | node2.stg |
| --- | --- | --- |
| Shutdown begins | 22:10:23.935944 | 22:19:41.728697 |
| New Linux boot | 22:14:08.078434 | 22:23:02.658636 |
| Logged system | 26.05.git.2abbe3c, Linux 6.12.113; generation 192 | 26.05.git.2abbe3c, Linux 6.12.113; generation 41 |
| Autostart selection | 47 at 22:15:06.830781; parallelism 8 | 60 at 22:24:07.924511; parallelism 16 |
| Selected / unique attempts / successful outcomes | 47 / 47 / 47 | 60 / 60 / 60 |
| Observed failed / unresolved starts | 0 / 0 | 0 / 0 |
| Final successful outcome | 22:16:45.843060 | 22:25:26.757208 |
| Capture cutoff | 22:28:48 inclusive second | 22:29:16 inclusive second |

For node1, every attempt has a matching success-delay marker and there are 47 `ct_on_start` commands. For node2, selection, attempt and `RUNNING` ID sets are identical, with no duplicates or later new-boot `STOPPED` marker. These totals concern the selected autostart set, not every imported container. Both logs identify vpsAdminOS input `2abbe3cc`, vpsAdmin `ff730be4` and nixpkgs `26f4107e`; the full kernel source revision is not logged.

Key evidence, with line numbers in the retained files:

- [Node1 host](reboot-2210-node1-host.log): L524 shutdown; L5198 boot; L6961–6964 versions; L12233–12234 `Auto-starting containers, 8 containers at a time` / `47 containers to start`; L12423 first attempt; L17097 final success. L1176–4524 contain the 47 shutdown TTY EOF closures, all before the new boot.
- [Node2 host](reboot-2210-node2-host.log): L797 shutdown; L2749 boot; L4849–4852 versions; L6244–6245 `Auto-starting containers, 16 containers at a time` / `60 containers to start`; L6385 first attempt; L10657 final `RUNNING`. L1095–2735 contain the 60 shutdown TTY EOF closures, all before the new boot. The 22:15 kmsg-parser exception also belongs to the old boot.
- The morning comparison is [node1-host-since-102109.log](node1-host-since-102109.log), L8531: `2026-10-18T10:22:53.239004+02:00 ... Too many open files ... /proc/self/fd (Errno::EMFILE)`, followed by executor EOF at L8556. Neither signature recurs after either evening boot. Neither new boot shows a swap allocator trace, OOM, BUG or panic in the captured host/runit evidence.

Startup dependency errors recovered: early missing osctld sockets and network-unreachable messages precede successful pool import, nodectld resume and periodic status processing. Node1 pool import completes at 22:15:06.899675, node2 at 22:24:07.990759. One later `ct top`-missing batch appears per node (47 IDs at 22:17:18; 60 at 22:26:14), without recurrence before cutoff. This does not contradict the start outcomes, but a subsequent successful `ct top` sample was not established. Recurring Munin IRQ-permission/sensors errors, plus node1 Tomcat parsing errors, remain separate monitoring faults. The previously known histfile/getent issue persists and remains excluded from work at the user's direction.

Swap is separate and noncritical for this assessment. Node1's initial `swapon` calls fail with **Device or resource busy**, not the morning allocation failure, at 22:14:09; both services nevertheless report success ([node1 runit](reboot-2210-node1-runit.log), L84–87). Later kernel records show `Adding 195360980k swap` on `/dev/sda` at 22:18:46.502453 and `/dev/sdb` at 22:19:04.522428 (node1 host L18308/L18316). Node2 logs actual activation of both devices, `Adding 234431060k swap`, at 22:23:43.110846/.115839 (node2 host L2792–2793), corroborating service success ([node2 runit](reboot-2210-node2-runit.log), L293–294). These establish activation events, not current `/proc/swaps` state or whether later activation was operator initiated. No swap fixes or recovery were attempted.

Both owners collected complete bounded timestamp windows without a line cap. Node1 retained 22,645 host and 1,049 runit lines; latest entries are 22:28:46.998558 and 22:28:46.449485. Node2 retained 11,071 host and 1,325 runit lines; latest entries are 22:29:14.620309 and 22:29:15.526427. Host filtering excludes sshd and container-kernel records; runit filtering matches each exact node FQDN. Collection metadata is in `reboot-2210-node1-{host,runit}-meta.log` and `reboot-2210-node2-{host,runit}-collection.log`. [Node2 detailed reconciliation](reboot-2210-node2-analysis.log) retains all 60 IDs. Later log arrivals and health beyond the cutoffs remain outside this evidence.

Implementer0 collected/analyzed node1; implementer1 collected/analyzed node2; architect0 reconciled the reports. Only read-only remote queries and local findings were used: no service actions, recovery, builds, application/design edits or lifecycle changes. Lead owns registration and session tracking.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-18-autostart-log-analysis/)
