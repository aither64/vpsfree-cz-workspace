# Selected immutable first-switch capture

Lead inspected and selected [guard-first-switch-vm.py](guard-first-switch-vm.py),
SHA256 `b122d8d0c4d6f40bf82e4bd82ac1aba214c313da4a79edd7017677fc28feec0d`.
Guardian and source are frozen. Lead's fresh watcher owns the one session
diagnostic VM slot, execution, observations and native cleanup; other lanes are
held. Implementer3 does not launch, poll or duplicate its logs/status observation.

Exact lead-selected launch from workspace root with matching session variables:

```sh
VPSADMINOS_SUPPORT_VM_ADMITTED=1 /home/aither/.nix-profile/bin/python3 /home/aither/workspace/ai/vpsfree.cz/work/2026-10-22-ci-failure-analysis/repair/support/guard-first-switch-vm.py
```

The native command is the existing rooted stock runner's
`/nix/store/mjlc8sc8qp6vpzf08r65jwl1y38jbgjm-test-runner/bin/test-json-runner`
with exact frozen JSON
`/nix/store/hd3by52cz1wrza2k28av89iflad1j4ly-os-test-upgrade-from-6.12-guests-first-switch.json`
and state `/tmp/ci-failure-analysis-2026-10-22/support/attempt-1`.
Cwd is the fresh attempt directory. TEST_PATH is
`upgrade/from-6.12-guests-first-switch`; TEST_TIMEOUT900 is a **per-command**
default, not total runtime. TEST_JOBS1, TEST_RECREATE_DISKS1,
TEST_DESTRUCTIVE1 and TEST_SYSTEMx86_64-linux preserve native single-case cleanup.
TEST_RUNNER_REPO_ROOT is unset. There is no Nix evaluation/build/prebuild command.

Native direct JSON omits scheduler resource metadata. The literal launch flag
records lead serial-slot selection, not a native reservation. External fresh
admission requires the exact actual1machine/8192MiB RAM and SHM/4CPU/one10G disk
JSON, at least16GiB host available RAM and SHM,4affinity CPUs, and free minus
the full24GiB forecast at least40GiB. Foreign QEMU is not excluded or signalled.
An exact native JSON argv with canonical state under this session's temporary
root refuses another session-owned lane command. Aggregate host pressure still
affects resource admission and cancellation.

Guardian checks exact JSON/kernel/service/wrapper hashes and existing shared
runner/config roots. During execution it observes only its native process tree,
retains birth identities/PGIDs, authenticates canonical argv/cwd before group
SIGINT, and tracks separate-group native descendants without directly signalling
them.1800s triggers cancellation; the script body also retains its1800s bound.
Other triggers:44GiB disk stop margin,24GiB conservative cumulative physical
budget,64MiB non-disk output,8GiB available host RAM/SHM reserves, aggregate
swapping or watcher interruption. All guards continue through cleanup.

Native TestEvaluator ensure owns guest kill/destroy/finalize/cleanup and managed
disk removal.120s incomplete cleanup is an escalation threshold: watcher retains
ownership and exact handles; guardian does not automatically TERM/KILL or delete.
Native own-VM cleanup may use its usual TERM/KILL. A client exit alone does not
prove cleanup. After the watcher delivers completion, reconcile known process
births/groups, managed disk absence, state lock/socket handles and retained
capture before any later own-data cleanup. No lifecycle action is selected.

## Completed preparation and checks

Preparation2 passed in99.113s, all10native clients exit0 and later exact-PID
observation found all absent. The synchronous successful Nix realization and
valid completed output closure show no preparation work outstanding; no shared
daemon or foreign builder was signalled. Logs were consumed once and hashed.
No further graph recovery or preparation is needed.

- JSON SHA256 `ad0f136d98a6e0e59ddf3c38facc1acf0846cc2e0bde0fd10295487b2ff86adf`.
- Guest closure NAR2186327896bytes; squashfs751865856apparent/allocated bytes.
- Full JSON-output closure physical3741839360bytes; support source/roots346873856bytes.
- Kernel image SHA256 `6932c113c93f0de9961401760a1a4ff9961c8317640eae765992ede73ffea70b`.
- Actual [service bytes](prepared-test-shell-services.json) and [policy](prepared-test-shell-policy.json):
  boot run c856fd... uses `/dev/hvc0`; target run b1f5dc... names
  `/dev/virtio-ports/org.osvm.shell0`. Both actual policies say onChangeignore,
  retaining the old active shell through first switch. No shell restart is
  selected. A newly started target shell would not match this VM's virtconsole.
- Stock wrapper c90f4d... and owner1's runner root are verified; root ownership
  stays with owner1/lead through consumers. No duplicate runner build/root.
- [Focused guardian checks](guardian-check-1/results.json): inert Python normal
  exit0 and output-cap/authenticated-SIGINT cancellation125, no remaining owned
  processes. Production argv/admission were overridden only in the inert test
  module; no VM/Nix operation occurred. The final additional flushed escalation
  notification was syntax checked without a guard/ownership logic change.

The [declared identity boundary](identity-comparison.md) remains unchanged:
immutable old writer/kernel and exact846bb source/locks with newly declared
packaging identity. This establishes old-writer/runtime facts in this execution,
not incident-exact binaries/images or generic-service causal exclusion. Legacy
virtconsole backpressure and malformed/missing capture remain evidence gaps.
An expected baseline equality failure is diagnostic evidence, not a repair pass.

After launch architect identified a sampled-ancestry orphan gap. Lead supplemented
the current watcher directly; the live b122 guardian/input remain unchanged.
[Separate correction](guardian2-correction.md) is prepared for later selection,
not an implicit capture retry. Its notes also qualify64MiB detection as sampled
with possible overshoot, rather than a filesystem quota. Current guardian exit
alone is insufficient: post-result disk/lock/socket/exact-process reconciliation
remains mandatory before accepting effects-ended.
