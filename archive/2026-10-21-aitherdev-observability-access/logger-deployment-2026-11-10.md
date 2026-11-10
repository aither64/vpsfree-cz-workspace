# Logger deployment, 2026-11-10

Logger delivery was accepted by the lead. No logger command remains active.
Machine claim `1f42a96d-27e1-4841-a830-c89ebda51f89` remains held for the lead;
this package does not release it or integrate the configuration.

## Exact deployed identity and recovery

- Repository/selector: `git@github.com:vpsfreecz/vpsfree-cz-configuration.git`,
  `cz.vpsfree/containers/prg/int.log`, SSH `log.int.prg.vpsfree.cz` (VPS 14004).
- Source: `959e1d54cabc7ac5530dac6179acacb077a57754`, base
  `0f3897b5b7dc53edee33f1289cbda25ec28910f5`, lock blob
  `9b6b86a9000a4411bb82c9623c3762f096d3325e`; full graph/reviewed rebase lineage
  is retained in [the refresh receipt](rebase-refresh-2026-11-10.md).
- Local confctl NAME: `2026-11-10--16-12-51`.
- Both running system and profile `system-143-link` resolve to
  `/nix/store/kgrfplplhrhhj4idvzx172lqh4hiyimq-nixos-system-log-26.05.20261026.718f670`.
- Retained rollback: `system-142-link` points to
  `/nix/store/wpffkjx6cmnhm5ql9n4xv9nf62a9kl6f-nixos-system-log-26.05.20261026.718f670`.
  No matching local confctl NAME was invented. The architect/lead accepted native
  `nix-env --profile /nix/var/nix/profiles/system --switch-generation 142`, followed
  by that exact old closure's `bin/switch-to-configuration switch`, if recovery is
  needed. Both profile and running-system identity plus services must then pass;
  a profile pointer alone is not recovery. No rollback or pruning occurred.

## Execution and acceptance

Native dry-activate exited 0 in 32.531s. Its non-TTY preview did not retain a unit
job list; the pinned CLI removes successful internal logs. The lead explicitly
accepted the complete static comparison plus this successful native result.
No preview was rerun. Native switch used the same NAME, `--yes`,
`--enable-auto-rollback` and `--health-checks`, with no reboot. It exited 0 in
26.497s; all four native health checks passed. A fresh Luna/low observer and the
parent joined all owned work. The native switch log was retained before the
CLI's ordinary successful-log unlink.

The approved inherited change permits mx2 `37.205.11.114` to TCP 11514/UDP 11515
and adds its exporter mapping. D-Bus policy/include trees are unchanged after
system-path normalization. No compiled binary, interface, route, DNS or reboot
change was introduced. Static comparison is in `deployment-comparison-2026-11-10.json`.

Historical inventory/review/apply and restoration completed in 2.201s,
15:57:49–15:57:51 UTC. All 4,397 selected entries passed bounded aggregate review
and were reconciled. Original private inventory remains on the logger at
`/root/log-reader-recovery/before-2026-11-10-logger-143.json`, mode 0600, SHA256
`0a7587f80c29fa6746be58f75fdbaf25a442735174ebe131100f6854936885ee`.
The restart trap restored syslog socket/service and rotation timer successfully.
No blanket chmod, FIFO change, forced rotation or root-key edit occurred.

Actual `log-reader` SSH opened current/archive remote logs and current/archive
messages with contents discarded. The remote-tree check covered 4,382 entries
and 95 subdirectories: root-owned, GID 989, files 0640/directories 0750, with
write predicates false. UID 1000 has only `log-readers`; effective public-key-only
SSH restrictions, root-managed `restrict` key, no sudo grant and Nix trust
(`trusted-users = root`) passed. Home and `/tmp` remain writable as designed.
Two verification-probe assumptions were corrected without source changes:
this sshd emits capitalized option names, and native sudo lists an explicit denial
with exit 0. Failed probe evidence remains; no real permission failure was masked.

Normal mx2 input created its directory and log as root:989 0750/0640 before
reconciliation, as recorded in the original inventory. No health marker was
needed or emitted. After restoration, normal node23 log metadata advanced to
16:06:36.795159 UTC. Exporter HTTP checks succeeded; FIFO remains root:GID991
0640. Syslog socket/service, exporter and rotation timer were healthy at final check.

The scheduled logrotate timer/service ran successfully at 17:00 CET (16:00 UTC),
after maintenance. No new archive path or rename pair was observed: this proves
the scheduled invocation, not an actual file rollover. Deployed rules/tests
cover rotation policy; no live rotation was forced. Next timer invocation was
18:00 CET when checked. Actual future rollover remains an observation, not a
claim made by this deployment.

Detailed evidence: `deploy-logger-{dry-activate,switch,reconcile}-2026-11-10`
logs/results, `deploy-logger-switch-native-2026-11-10.log`, final acceptance
`deploy-logger-acceptance-2026-11-10-result-03.json`, and
`deploy-logger-final-health-2026-11-10.json`. Root authorized keys were neither
inspected nor edited; the user owns manual root-key removal after acceptance.
