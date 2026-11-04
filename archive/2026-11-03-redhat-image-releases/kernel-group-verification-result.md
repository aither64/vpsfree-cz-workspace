# Kernel group verification

**Focused CI passed all 14 unchanged kernel/vpsadminos scripts**, including
`misc-attrs`, at exact head54 below. Native six-worker execution and ordinary
two-VM resources are verified. The prior LXC attach ESRCH did not recur in this
run; its underlying cause remains unresolved. Both earlier local operations
remain blocked/interrupted before assertions. All owned operations ended.

- Exact source: `54b4313404cea35b58ebb9df951ae75e27c44971`.
- Tree: `5c03648e084e907957b37263846bc5763abdac1f`.
- Unchanged full group: 14 scripts, six script workers, ordinary cgv1/cgv2
  configuration (8 CPUs/8192 MiB each).
- [Full generic CI](ci-refresh-result.md) remains FAILED: 102 passed/seven failed
  test groups/eight failed scripts. Lead accepts the seven openSUSE script
  failures as FAILED/exact-base, and the nine separate livepatch fixture jobs
  as FAILED/pre-existing. They are not relabeled passes.
- Exact-54 image CI (four Red Hat plus four upstream cases), RSpec 3297 examples
  and RuboCop passes remain valid at their recorded scope.

[Initial failure diagnosis](ci-refresh-failure-diagnosis.md) and
[accepted warning/deadline checkpoint](kernel-group-warning-checkpoint.md)
record the bounded reasoning and limits. A future green focused run cannot
prove the underlying attach race fixed.

## Completed local continuation: native setup failure

The normal runner selected all 14 and admitted ordinary two-VM resources at
07:20:04 UTC; VM/script dispatch began 07:47:09 after declared static-toolchain
preparation. The first six scripts blocked during shared-directory/pool setup.

- At **08:04:28 UTC**, `memory-view-cgroups-v2` raised
  `OsVm::UnrecoverableTimeoutError` for
  `mkdir -p "/run/osvm/shared-dir"`; script elapsed 1039.22 s.
- At **08:07:10 UTC**, `misc-nice`, `misc-oom-kill`, `misc-mknod`,
  `misc-proc` and `tmpfs-cgroups-v2` raised pool-`tank` setup timeouts;
  script elapsed approximately 1201 s.
- These are observed script elapsed values. Native nested command budget was
  900 seconds; pool/online stages each have 20-minute budgets. No overall
  group/CI deadline was invented.
- No example/assertion completed. RCU starvation and soft-lockup console strings
  were retained; they did not match native fatal classification and did not
  cause cancellation.
- Utility interrupted original TTY `50754` after the concrete native failures.
  `misc-attrs` only logged dispatch at 08:07:41 after those failures; it has
  no completed outcome. Subsequent closed-stream errors are interruption
  effects, not additional kernel assertion results.

[Full native completion reply](kernel-group-continued-native-completion.json)
was independently read: **exit_code 130**, output `^C`, chunk `0ddf25`.
[Outer log](kernel-group-continued-verification.log) is complete. Preserved
[test-runner log](kernel-group-continued-artifacts/test-runner.log), lines
27406–27639, has original timeout stacks; 27686 onward records later dispatch
and interruption errors. It has zero completed example events or script-finish
lines. This is blocked local verification, not 14 failed assertions.

| Selected scripts | Actual observed local outcome |
| --- | --- |
| memory-view-cgroups-v2 | shared-directory mkdir setup timeout |
| misc-nice, misc-oom-kill, misc-mknod, misc-proc, tmpfs-cgroups-v2 | pool setup timeouts |
| loadavg, misc-attrs, tmpfs-cgroups-v1, uptime, cpu-view-cgroups-v2 | later dispatch after setup failures/interruption; no valid completed outcome |
| cpu-view-cgroups-v1, memory-view-cgroups-v1, syslogns | no dispatch/result recorded before termination |

All original named processes were independently absent after cleanup: shell
2003123, runner 2003126, executor 2010007, evaluator 2010010, QEMU 2410500,
virtiofsd 2410467/2410469. No process matched the owned state path. No active
collection/client operation remains; no unrelated daemon or process was killed.

Local artifacts are retained under `kernel-group-continued-artifacts/` (19
log/config files), including complete shell, console, shared-dir, diagnostic
and native runner logs. Original state is preserved at
`/tmp/redhat-image-releases-2026-11-03-kernel-group-continued/os-test-kernel__vpsadminos-f1b75a4a/`.
No disks or session records were manually deleted.

## Local source, resource and configured input receipts

[Full generated config](kernel-group-continued-config.json), also retained in
the artifact directory, is store JSON
`/nix/store/c08ra5rpk1a7b50pkqdi15k2pnbhgy63-os-test-kernel-vpsadminos.json`.
It independently confirms all 14 scripts/six workers and ordinary machines.
[Runtime input closure](kernel-group-continued-input-closure.txt) retains 986
paths from both toplevels/kernel/initrd, queried read-only without builds.

- Actual evaluator source: `/nix/store/2dzxhjlp71q905a48xg6q34wjys1zszz-source`.
- Kernel: `/nix/store/x64477x3mxlzqkmvijvakf33an9vcbrz-linux-6.18.49/bzImage`.
- Initrd: `/nix/store/9j0cbhab4gvxvvcbx4kg4865drp45jfh-initrd/initrd`.
- cgv1 toplevel: `/nix/store/idcdx9xswwgzp71srmisk7w3wbrxqqhs-vpsadminos-system-vpsadminos-26.05.git.54b4313`.
- cgv2 toplevel: `/nix/store/z2qzngmdna9m39fzpkpc6mminaspq9ar-vpsadminos-system-vpsadminos-26.05.git.54b4313`.
- Configured LXC: `/nix/store/792sra8cvp77dawyi0fck9ngprhx7jxx-lxc-6.0.6`
  (not exercised by the blocked attribute assertions).
- QEMU: `/nix/store/kanckc6ljipqzjsrvj4aqaf87a4rhswr-qemu-host-cpu-only-for-vm-tests-10.2.4`.
- virtiofsd: `/nix/store/1n70z14cr636nndi82qf18a1l142z9aq-virtiofsd-1.13.3`.

No manually supplied source metadata was used. Native source-info JSON was not
exposed by the live process environment and is not reconstructed. Recorded
source/config/closure identities do not claim complete equivalence to failed CI.

[Metadata](kernel-group-continued-metadata.json) and
[native guard](kernel-group-continued-resource-guard.json) preserve requirements:
two machines/16 CPUs/16384 MiB RAM/16384 MiB shared memory/max per-machine8192.
`can_reserve=true`; pool RAM65470 MiB/shm40076 MiB/CPU96 after native
8192 MiB RAM/shm reserves, CPU reserve0, native factors1.0/1.0/1.5 unchanged.
The real executor separately reserved matching resources; no oversized fallback,
memory/source override or increase was used.

Exact completed local command, from the clean exact-head worktree:

```sh
nix develop .#test-runner --command env RUBYLIB=/nix/store/givmi31xrbr231gxnry1xc2ggb5s4imf-libosctl-native-local/lib bundle exec ./test-runner/bin/test-runner test --test-config tests/test-configs/ci.nix --state-dir /tmp/redhat-image-releases-2026-11-03-kernel-group-continued --jobs 1 --stop-on-failure 'kernel/vpsadminos#*'
```

Ordinary ci.nix only sets Docker/Podman mirrors. No VPSADMINOS_CONFIG,
NIX_PATH adjustment, manual source metadata or cached JSON runner. Normal
RepositorySource lifetime rooted the capture through native cleanup.

## Preserved interrupted setup and guard correction

The first local operation, state `/tmp/redhat-image-releases-2026-11-03-kernel-group`,
handle87839, was prematurely interrupted after119.27s during
`/nix/store/qvrpr8247kyqj6dcgs9qwxkvcy5p9bpl-linux-headers-static-6.18.7.drv`.
Reported exit1; zero VMs/scripts. [Original stdout](kernel-group-verification.log)
and [full setup log](kernel-group-interrupted-setup.log) preserve header drv
42/1481, source unpack1530/2147/2171 and HDRINST. This was not proven
boot-kernel image compilation or a capacity/cache blocker. Original state and
logs remain untouched; old utility was not reused.

Lead authorized correction within the same verification package. Fresh
continuation utility initially hit unsupported `TestResources#to_h` while
serializing its already-successful metadata evaluation. No test/VM started.
[Failed probe](kernel-group-continued-preflight.log) is retained; parent
corrected only serialization using the existing metadata hash/native pool API.
[Corrected guard output](kernel-group-continued-resource-guard.log) exit0
preceded the actual single continuation. No source/helper/harness was added.

## Focused CI: verified PASS, all 14 scripts

One existing focused workflow was dispatched, without local overlap or source
change: [run 41798971522](https://github.com/vpsfreecz/vpsadminos/actions/runs/41798971522),
exact head `54b4313404cea35b58ebb9df951ae75e27c44971`,
event `workflow_dispatch`, title `CI (ci: kernel/vpsadminos#*)`.
[Initial full JSON](kernel-group-focused-41798971522-initial.json) was
independently read/asserted. [Bounded discovery](kernel-group-focused-discovery.json)
currently records this sole focused run plus the old full generic push;
no duplicate qualifying run is shown. [SSH ref receipt](kernel-group-focused-remote-ref.txt)
proves feature54 immediately before dispatch.

[Actual dispatch/request receipt](kernel-group-focused-dispatch.txt) retains
the command, requested inputs, returned run URL and exit status0:

```sh
gh workflow run ci.yml --repo vpsfreecz/vpsadminos --ref 2026-11-03-redhat-image-releases -f test_suite=ci -f test_pattern='kernel/vpsadminos#*' -f test_tag=ci -f prebuild=true -f stop_on_failure=true
```

[Final full JSON](kernel-group-focused-41798971522-final.json) was independently
read/asserted: exact54, workflow_dispatch, completed SUCCESS. Build/cache job
`126469791914` passed at 08:44:34 UTC; focused core job `126479225372` ran
08:44:36–09:24:16 UTC. `Run tests` ran **08:44:41–09:24:05 UTC**, 39m24s.
The earlier 09:24:10 checkpoint was the final cleanup/runner step timestamp;
final native job completion is 09:24:16. Lifecycle job `126479227313` is SKIPPED.
[Test-start JSON](kernel-group-focused-41798971522-test-start.json) retains the
intermediate state. Exact workflow's nonempty pattern has 240-minute job/step
bounds (12:44:36/12:44:41 UTC); build's configured bound is 480 minutes.

[Full test job log](kernel-group-focused-41798971522-job-126479225372.log)
independently proves suite ci/pattern/tag at lines246–251/350, exact source/tree
at250–251, complete14-script selection at354–368, and ordinary resource
reservation at374–378: **two VMs,16 CPUs,16 GiB RAM,16 GiB shared memory**.
Native 8 GiB RAM/shared-memory reserves remained in force. Ordinary exact-head
machine source config is cgv1/cgv2,8 CPUs/8192 MiB each, `testScriptJobs=6`.
The preserved native `test-runner.log` begins with six simultaneous script
dispatches at08:48:16 UTC, before any completed example: misc-attrs,
memory-view-cgroups-v1, cpu-view-cgroups-v1, tmpfs-cgroups-v2,
memory-view-cgroups-v2, uptime. This is the full concurrent group, not isolated
misc-attrs. No override, unrelated suite/image run or retry was used.

Independent static evidence reconciliation found exactly14 unique selected
scripts and exactly the same14 successful scripts. Native summary at job
lines2183–2185 is **14 scripts, one test,2148.99s, one test successful**;
native `test-result.txt` says `expected_success`.

| Script | Result | Seconds |
| --- | --- | ---: |
| cpu-view-cgroups-v1 | PASS | 705.13 |
| cpu-view-cgroups-v2 | PASS | 655.02 |
| loadavg | PASS | 1501.27 |
| memory-view-cgroups-v1 | PASS | 537.77 |
| memory-view-cgroups-v2 | PASS | 545.06 |
| misc-attrs | PASS | 165.08 |
| misc-mknod | PASS | 16.25 |
| misc-nice | PASS | 15.88 |
| misc-oom-kill | PASS | 140.07 |
| misc-proc | PASS | 14.84 |
| syslogns | PASS | 51.91 |
| tmpfs-cgroups-v1 | PASS | 644.52 |
| tmpfs-cgroups-v2 | PASS | 701.57 |
| uptime | PASS | 293.08 |

The previously failing immutable-file example now completed successfully:
`cgv2-shell.log:177` records `chattr +i /immutable-zfs.file`, status0;
`lsattr` shows immutable, and prohibited write/append/remove commands return
the expected errors before successful cleanup. Job line410 records that
example passed in27.35s; all four misc-attrs examples and its script pass.
This run did not reproduce the prior attach ESRCH. A passing repeat neither
fixes nor proves the underlying race or establishes complete input equivalence.

## Focused raw evidence and input limits

- [Full run log](kernel-group-focused-41798971522-run.log) and full job log
  above are retained. Before terminal completion, the live job-log endpoint
  returned404; no per-script outcome was inferred during that gap.
- Original native artifact **13310855821**,22 files/220878 compressed bytes,
  is retained as [raw ZIP](kernel-group-focused-41798971522-native-13310855821.zip)
  with [API metadata](kernel-group-focused-41798971522-artifact-13310855821.json).
  Its run/head binding and SHA256 were independently verified:
  `234b3d97c0de7642820af1a0158993d19fa300ecf1c085be06621968096060fb`.
- Complete extracted native files are under
  `kernel-group-focused-41798971522-artifacts/os-test-logs-41798971522-1-native/`,
  including test.log, prebuild build.log, test-result, test-runner, both
  console/log/shared-dir logs and all six shells per VM. The utility initially
  overlooked nested ignored files. Its23KB `...-artifact.zip` is only a local
  test.log repack; it is not the original22-file GitHub artifact.
- Actual cgv2 dmesg captured in `cgv2-shell4.log:4913–4914,5101,5366`
  reports Linux6.18.49,8 CPUs and OS26.05.git.54b4313. Its boot init is
  `/nix/store/3gdfga50x990b69lkbwnxvzvjw57wb74-vpsadminos-system-vpsadminos-26.05.git.54b4313/init`;
  line5104 reports8388072K physical memory. Prebuild log records both
  system derivations. These are observed CI receipts, distinct from local ones.
- Full generated CI config/source-info JSON, actual LXC store path, kernel
  image/initrd store paths and complete runtime input graph were not exported
  in these native artifacts. No graph certification, identity reconstruction,
  extra build or claimed equivalence fills that limit.

## Focused observer and managed receipts

Fresh utility `/root/kernel_focused_ci`, fork none, explicit `gpt-6-luna/low`,
matching pinned native config/full-access policy, owned only this operation.
Actual native watch handle `92162`, gh PID `2620728`, shell `2620725`
were independently verified alive:

```sh
gh run watch 41798971522 --repo vpsfreecz/vpsadminos --interval 30 --exit-status
```

[Full watch output](kernel-group-focused-41798971522-watch.log) is retained.
The utility confirmed danger-full-access/approval never; parent retained saved
settings and explicitly reported managed outcomes. No duplicate observer/poll
loop or second path was launched.
The utility briefly returned while its native watch was active; the parent
resumed the same utility/operation/handle without another watch or run.
[Complete original native completion reply](kernel-group-focused-41798971522-native-completion.json)
records `exit_code:0`, chunk `9a834a`, empty output. Original handle92162 ended.
Both utility and parent independently checked exact gh2620728/shell2620725:
absent. Utility completed collection; **no owned operation remains**. Native
CI cleanup step passed. No peer process or CI workflow was cancelled.

Actual managed readiness receipt:

```json
{"turnId":"01a1a59e-1d7f-7f12-a4ef-a97360b3556b","clientUserMessageId":"8c4c870a-e585-4f08-9279-65dca12548c2","steered":true}
```

Focused core-start managed report receipt (sent before waiting for final):

```json
{"turnId":"01a1a5bc-9ec8-78e2-8e80-5d58e094622b","clientUserMessageId":"edc5b922-978c-49ad-a2a2-48ecb45dd013","steered":false}
```

Terminal-workflow milestone managed receipt:

```json
{"turnId":"01a1a5e0-1124-7cb3-bb8a-7f337952271d","clientUserMessageId":"341d5b78-15b5-4df1-8a52-8f9665599fa4","steered":false}
```

Complete independently reconciled package was explicitly delivered through the
retained member's authenticated `report_to_lead` route. Actual final receipt:

```json
{"turnId":"01a1a5e0-1124-7cb3-bb8a-7f337952271d","clientUserMessageId":"1e79c7c5-d675-48f2-9493-506ad83945c7","steered":true}
```

Requested next action is lead assessment, then original approved staging
integration after independent fresh session/head/remote/history/hooks/claim
checks. This evidence report grants no new approval. No owned operation remains.

## Ownership and managed receipts

Retained implementer2 settings/session binding were verified unchanged:
`gpt-6.1-sol/xhigh/workspace_write`, full access. Local continuation utility was
fresh `/root/kernel_group_continue`, Luna/low, danger-full-access/never,
outside roster. Catalog
`495ef6620926420612ee4988e69d03a4e975e41734a1a5e3208db65fcd731db7`;
native utility identity `dw_af6ea530112c2a5e816254d08d217be90f4f5c713a51db96`.
No utility used member reporting identity.

| Managed report | Message ID | Receipt |
| --- | --- | --- |
| Actual continuation readiness | `42818e1c-99ed-4566-bedd-bfebd988c27d` | turn `01a1a553-5d48-76b2-acf8-19da1d7cd191`, steered true |
| 25-minute dependency checkpoint | `4fa7700d-75be-478b-b9d5-54d096ad71bd` | turn `01a1a586-8a7e-79b1-93a9-8999cdf15699`, false |
| Actual VM/input milestone | `355ec170-4082-4169-a5ec-c2985fca268e` | turn `01a1a58b-9952-7660-8c4f-2e23a61c2751`, false |
| Soft-lockup raw context | `530b7c95-83c5-489d-be68-2f6c425c24d8` | same turn, true |
| Concrete local blocked outcome | `fd4a7c82-80ce-4bc0-93e8-8dbfa9ee9a10` | turn `01a1a59e-1d7f-7f12-a4ef-a97360b3556b`, false |

Original interrupted report `c146e8f4-d64c-4cf1-aeb0-81c6ac6bb67c`,
corrected guard report `ec624e1e-7fc4-4308-9f60-ab7468547537`, and superseded
first readiness `52c7a5f8-7286-4ee0-9850-cf0b3f537f3f` remain in session
history; the old readiness was explicitly reconciled, not continued activity.

No Git/config writer, repository/machine claim, deployment, source/settings
change or session lifecycle action. Lead owns acceptance and any later
approved integration. Session stays open.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-03-redhat-image-releases/)
