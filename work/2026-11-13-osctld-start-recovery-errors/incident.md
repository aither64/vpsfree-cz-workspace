# User-provided incident handoff (not independently observed here)

Fleet userspace switched on 2026-11-13 to vpsAdminOS c0ad0ad8f970e04099830ff1c2ebfda01e8c9d62 (26.05.git.c0ad0ad), kernel stayed 6.12.113. All 12 nodes imported baseline 3,236 containers; no listed impermanence-related omissions/attachment/authentication/reclamation errors. Scope is CT1391, dozer, node25.prg, venet0.

Ordinary start, stop --kill and rescue ct boot --force did not clear the blocked state. User confirmed start worked after:

```
osctl --pool dozer ct recover forget-host-link 1391 venet0 &&
osctl --pool dozer ct recover cleanup 1391
```

This is incident recovery evidence, not a universal recovery instruction. User's explanation: "the user must've initiated shutdown from the inside at the moment osctld was already down". Initiator intent is unproved. Guest shutdown overlap and stale-link lockout have supplied log evidence.

## Timeline (CET, supplied)

- 23:04:16.856734 old osctld PID19606: Stopping daemon.
- 23:04:18.616088: Daemon stopped successfully.
- 23:04:46.967761 guest [1391-87c1] journald[73]: Received SIGTERM from PID 1 (systemd-shutdow).
- 23:04:46.996927 new osctld PID1736045: [pool=dozer] Loading container 1391.
- 23:04:47.155460 received veth_down.
- 23:04:47.158548 LXC PID27784/CT1391: script exited status 1.
- 23:04:47.284027 received ct_post_stop.
- 23:04:47.286684/.286719: Script exited with status 1; Failed to run lxc.hook.post-stop for container "1391".
- 23:04:48.429888 still preparing CT: zfs get -H -o value mountpoint dozer/ct/1391.
- 23:06:59 both node25 pools completed import.
- 23:07:21.973990 nodectld requested osctl -j ct start --wait "infinity" 1391.
- 23:07:23.904409 veth interface coming up: ct=venet0, host=vethjPIcYT.
- 23:07:24.397192 error: host veth identity changed from vethxxOnPg(20) to vethjPIcYT(1180).
- LXC creation/spawn failed, ABORTING -> STOPPING -> STOPPED.
- 23:07:25.688001 recovery failed netif down: OsCtld::NetInterface::Veth::InvalidHostLink: recorded network interface "vethxxOnPg" (ifindex 20, kind "veth") is absent.
- 23:07:25.906924 failed released-host-link verification: HostLinkClaimError: container dozer:1391 still owns host links through network interface "venet0".
- 23:08:07 restart returned start not available.

Hypothesis: callbacks arrived before DB::Containers publication and returned container not found. Exact callback response text was not captured. Missing normal veth-down execution log is consistent with early lookup failure, not proof of exact response.

## Supplied source pointers to independently verify

At c0ad0ad: commands/container/start.rb ~84 generic error before force; container.rb ~413 can_start? staged/error/container taint/netif taint/pool active; container/recovery.rb ~96 cleanup_or_taint. net_interface/veth.rb ~164 setup preserves persisted missing identity, ~269/354 up rejects changed identity/tainted ownership, ~438 forget_absent_host_link! verifies name AND index and IFB. pool.rb ~692 load_container preparation/monitor/console before DB.add. user_control/commands/{veth_down,ct_post_stop}.rb DB lookup; osctld/hooks/{veth-down,ct-post-stop} response errors; container/stop_handler.rb; commands/container/{recover_forget_host_link,recover_cleanup}.rb. osctl cli/app.rb ~2064 and man/man8/osctl.8.md ~2647 recovery commands/protections.

## July comparison pointers (verify)

Read only work/2026-07-24-ct-start-hang/{plan.md,state.md,portal.yml} and committed canonical bare refs. vpsadminos local+origin branch recorded 9b88a3903404ea6b5d14b2c0624bd75a69eb5d44; last review base 23cf4fc36f15ce510c63b5134f4ea8038b706e31, initial base 4476942c4e33092e20e4faa91f32dfcca9a3ea7d. Relevant commits e7b17285486fa4aac1bec774484eef3326c3a221 (durable lifecycle reducer), bf8b62eb72e77d64105cebf4e4d5b080c21a69f7 (generations), later cgroup transaction/policy changes. vpsadmin same branch recorded 807e9d7f1277217d3cf2d49b7c4b2525dc441c10. Old state reported active/unmerged, published and green exact-head CI. Do not alter old refs, worktrees, manifests or records, resume or contact old team. Do not import/rebase old branch here.
