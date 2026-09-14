# Portal reliability validation

Implemented and deployed on September 14, 2026. All feature branches remain
unmerged and the initiative stays open.

| Project | Final head |
| --- | --- |
| codex-web | `6335da93acdcc82cc26200d2fbc7f479655aa7c3` |
| dev-workspace | `e9ed544bf66ba8be07b4fca27aede6e6fd1bfe0a` |
| vpsfree-dev-workspace | `916223fce1c5b7b78578ca8a16aaaa472c68b08c` |
| workspace | `242af5caa10832436a55f953df2c5001274dd31f` |
| vpsfree-cz-configuration | `249bed1ee28e69a907edd09ea97a1144dbcdefeb` |

## User-visible results

- Auth-email initializes successfully. Its authoritative thread lookup took
  61.265 seconds during diagnosis, exceeding the old 60-second limit. Thread,
  dev-session and receipt deadlines are now 180/210/240 seconds. Recovery took
  57.26 seconds and preserved one original user prompt, verified by matching text
  and SHA256 digest. Its existing receipt is ready and the thread is
  01a09dca-ba5b-7f80-8d5e-ccade3fb0823.
- Failed creation shows the saved request with Copy. Form failures retain the
  prompt, name, date, model and reasoning effort through reloads. Accepted
  requests remain immutable and retry uses the same receipt.
- Brief reconnections stay quiet for ten visible seconds. A healthy stream
  survives tab focus; access errors remain immediate.
- Cluster status changes appear beside the affected cluster/session. Complete
  refresh removes absent cards and old credentials; reset also retires cached
  provider observations. Independent guests stop concurrently with shared
  provider-owned 120/10/20-second shutdown budgets.
- Password-reset repository histories now show their exact recorded comparisons
  without a fallback warning: vpsadmin 45 commits, mail templates 8, KB contracts 6,
  configuration 7. Final comparison capture is required by both workspace and
  project integration workflows; ordinary status inspection also captures exact
  unmerged comparisons. The first exact pair per head is immutable.

## Verification

- Current-head CI passed: [codex-web](https://github.com/aither64/codex-web/actions/runs/34783125339),
  [dev-workspace](https://github.com/aither64/dev-workspace/actions/runs/34799915781),
  [organization](https://github.com/vpsfreecz/dev-workspace/actions/runs/34799978709).
  The organization run includes both packaged provider evaluations and runner loading.
- Packaged Go suite and Ruby suites passed. Unsandboxed session tests passed
  297 tests/3126 assertions; packaged suite has the expected sandbox skips.
  Organization runner/status/command tests passed, including concurrent slow
  shutdown, stuck poweroff, busy status and both providers.
- Creation Playwright acceptance passed HTTP failure, connection loss, reload,
  model/effort retention, copy and unchanged retry. Repository browser acceptance
  passed 23 checks after supplying the missing sync.js route in its existing
  fixture server. This adjustment was only in a temporary harness copy.
- A real dual-node vpsAdminOS cluster used bridge networking and a cached kernel.
  Both stop actions began at 04:50:30 CEST; QEMU exited successfully at 04:51:51
  and 04:51:55. The standard stop command returned success in 86.46 seconds.
  Neither guest needed the runner's forced-kill fallback; the wrapper did not
  terminate the runner after its deadline. The VMs were still booting when stop
  was requested, so this also exercised waiting for the guest shell.
- A live browser observed changing, running/not-ready, stopped, reset-changing,
  and absent cluster states without browser errors. Reset removed the card and
  all owned VM/runner/socket/state resources. Recreated/busy cache eviction is
  covered by focused Go regressions.

## Deployment and rollback

Workspace profile generation 38 runs
`/nix/store/mk77xsg4qrk075smiyazc2vqb18p5b2y-dev-workspace-0.2.0`.
The shared Codex App Server stayed at PID 1090021; only the portal restarted.
Auth-email's runtime environment was rebound to the deployed executable after
one-time recovery, so it does not depend on the temporary candidate binary.

The configuration feature branch built generation `2026-09-14--04-42-31`.
`confctl deploy --yes cz.vpsfree/machines/aitherdev dry-activate` and `switch`
succeeded; systemd and firewall health checks passed. The system is
`/nix/store/rpi2qkdsi5s2x7g0lslljca62a5q3359-nixos-system-aitherdev-26.05.20260911.21a67dc`.
No kernel was rebuilt. Previous profile/system generations remain available.
Persisted receipts, manifests, comparison schema and cluster ownership formats
remain compatible with rollback.

Four mandatory review lanes used gpt-5.6-sol/xhigh. Architecture/risk reruns
reviewed the additive provider contract and complete cluster refresh. All
Blocking and Important findings were fixed; see state.md and the retained reports.
