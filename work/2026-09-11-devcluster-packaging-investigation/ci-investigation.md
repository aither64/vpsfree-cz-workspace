# Broader vpsAdminOS CI investigation

Feature run: [34630335805](https://github.com/vpsfreecz/vpsadminos/actions/runs/34630335805),
commit e6c4c5cfa27ce3b139bba6475be80cfead4b8df4.
The suite job103366606722 completed after49m15s:76 of79 tests passed, with three
unexpectedly failing test scripts among269 scripts. Artifact
`os-test-logs-34630335805` was downloaded and inspected before making any rerun
or causality decision. No rerun was used as validation.

Comparison run: [34398676068](https://github.com/vpsfreecz/vpsadminos/actions/runs/34398676068),
staging commit c3f219a385e605ac00f2864c9c311902620271cd. Downloaded its full
`os-test-logs-34398676068` artifact as well.

| Test | Observed failure | Assessment |
| --- | --- | --- |
| kernel/livepatch-kernel-identity | `cat /etc/vpsadminos/livepatch-monitor.json` returns1 because the file is absent | Same command and missing-file failure in the previous staging artifact. |
| osctl/nfs-cancellation | Fixture expects mount option `hard`, but sees `soft` | Same mismatch in staging (NFSv3 there, NFSv4.2 here). Current cleanup additionally faults in `rpc_cancel_tasks+0x4f/0xb0`, NULL address0x28, via shutdown_store. The kernel fault is recorded separately; the prior artifact did not show that stack. |
| kernel/vpsadminos#memory-view-cgroups-v2 | Installing Python3 with apk fails: index refresh reports transient DNS error, then xz-libs5.8.3-r0 returns HTTP404 | External package/index setup failure before the remaining memory-view assertions. Do not attribute it to a memory-virtualization assertion. |

These failing fixtures instantiate the vpsAdminOS machine class. The feature
changes only `OsVm::NixosMachine` plus its unit-test support and documentation;
no kernel, container daemon, networking, test fixture or vpsAdminOS machine code
changed. The NixOS driver integration test passed with the default fresh-root
policy, as did the vpsAdminOS driver test. Both final packaged development
clusters passed live lifecycle/data-retention acceptance independently.

This is evidence that the suite failures are outside the devcluster repair. It
is not a claim that upstream OS CI is green or that the kernel teardown fault is
harmless. Keep the feature branches unmerged as requested and retain these
results for the separate OS test/kernel work.

Follow-up directions: reconcile the livepatch fixture with when the module
provides monitor configuration; reconcile the NFS fixture's hard-mount contract
and investigate the rpc_cancel_tasks teardown fault; make the memory-view test's
Python dependency independent of stale container indexes or failed index refresh.
Do not broaden this packaging initiative into kernel or NFS behavior changes.

OSVM RSpec and RuboCop workflows passed. The build/cache job and AMD livepatch
job passed. Intel livepatch job103366606729 remains running; its artifact/result
must be assessed when available. Direct read-only SSH access to the two runner
accounts was unavailable. GitHub exposes the completed suite artifact while
other jobs in the workflow are still running.
