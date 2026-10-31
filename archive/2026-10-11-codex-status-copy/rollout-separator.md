# Separator removal deployment and recovery

Executed and verified after final independent review, browser geometry/package/
host checks and exact-head CI passed. Merge approval remains pending for all
three master branches. This record describes the development deployment.

Final runtime: 356f6a9930bb8b0749079069038c67695404e825; workspace:
0835fb7f4e99fc8c9e36c5892e340c4bf7d5c16f; configuration:
b18412bfdbec545312469f581f2991bcf6c237d5. Candidate application profile:
/nix/store/46jr5jcmwjbagjpk2r0pap4md0hr40hm-dev-workspace-0.2.0.
Built confctl host generation: 2026-10-11--18-26-08.

Parent launched rollout-separator.sh in the owned transient user service
workspace-status-separator-rollout.service, invocation
c6574ba201c84b7eb4bba514f4a8787b, initial PID827445. Fresh catalog Luna/low utility
/root/monitor_separator_rollout observed that exact existing operation. The
wrapper ran confctl deploy with dry activation, no reboot and auto rollback,
then stable workspace-host switch from the feature workspace source to select
the application user profile. It completed in about2m40s (18:28:17–18:30:57 CEST).
Atomic rollout-separator.status is0 and phase complete; systemd reported
inactive/dead, Result=success, ExecMainStatus=0. No operation remains running.

Host health checks passed (2/2), followed by protocol compatibility and semantic
observation checks and the application switch. No failure or unexpected local
kernel compilation appeared. Complete wrapper output is rollout-separator.log;
invocation-filtered journal had no entries, so completion proof is the atomic
wrapper result plus retained systemd status. [Verification](verification-separator.md).

Pre-switch capture: pre-deploy-separator.json. Post-switch capture:
[post-deploy-separator-result.json](post-deploy-separator-result.json). Exact
served JS/CSS bytes match the final source; JS34/CSS11 and absent separator DOM
were verified. Profile matches the candidate. All four user services are active;
Codex/tmux PIDs and native root are preserved. Current system:
/nix/store/mcgwi7x6jchrvyhpg1xiadwcj0iqvpnk-nixos-system-aitherdev-26.05.20261010.6fcc160.

Read-only GET/HEAD browser checks passed under fresh /root/monitor_separator_live.
Parent inspected wide/narrow screenshots: no separator precedes the fixed timer;
the internal message/tool dot remains. Active counts stayed at the same x
coordinate across a live tick, and idle members showed the working peer without
attention. [Live evidence](live-separator-result.json).

No API/protocol/state/native contract or kernel change was introduced. Existing
forward-only application recovery remains: repeat a compatible switch or select
a newer reviewed package. Host auto rollback uses its retained generation. Keep
both candidate output roots and the previous deployed source-retention tags;
prior execution evidence remains in rollout.md. No archive/delete/stop/merge is
authorized. No recovery was needed or exercised in this rollout.
