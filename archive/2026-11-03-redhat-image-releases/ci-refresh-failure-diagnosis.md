# Refreshed core CI failure diagnosis

2026-11-04; architect0; bounded read-only investigation. Current head
`54b4313404cea35b58ebb9df951ae75e27c44971`, tree
`5c03648e084e907957b37263846bc5763abdac1f`, base
`742eb30cb1a8b6766c85e915d26b0400e38244b1`.

**Disposition:** seven openSUSE scripts reproduce failures in the exact base.
The eighth failed script has a distinct LXC namespace-attach error before its
immutable-file assertion. Its underlying cause remains unresolved; it is not
proven to be a metadata regression or a harmless flake. No metadata-contract
fix is warranted by the observed errors. The core run remains FAILED.

## Exact failure chains

Current run [41741634771 / core 126350677643](https://github.com/vpsfreecz/vpsadminos/actions/runs/41741634771/job/126350677643)
completed 323 scripts across 109 tests, with 102 successful and seven failed
test groups. The device-unit group contains two failed scripts.

| Scripts | First failing operation | Evidence under `ci-refresh-artifacts/native-failures/` |
| --- | --- | --- |
| cgroups/mount-v1, cgroups/mount-v2, dist-config/netif-routed, dist-config/start-stop, dist-config/systemd-rundir, systemd/device-units, all `#opensuse-leap-16.1` | `osctl ct new --distribution opensuse --version leap-16.1 …` exits 1: `container image opensuse:leap-16.1 (arch=x86_64, vendor=default, variant=default) not found in repositories: default` | Respective `test-runner.log` lines 8, 14, 64, 30, 36, 14 |
| systemd/device-units#opensuse-latest | `osctl ct exec testct-c580 systemctl status sys-devices-virtual-net-eth0.device` times out; empty command response | `systemd-device-units/test-runner.log:38–40` |
| kernel/vpsadminos#misc-attrs | `osctl ct exec kmisc-attrs-zfs-a9d2 chattr +i /immutable-zfs.file` exits 1: LXC `__attach_namespaces_pidfd:711 No such process`, then `Failed to enter namespaces` | `kernel-vpsadminos/test-runner.log:3140–3149`, `cgv2-shell4.log:1005–1014` |

The Leap scripts fail before booting their requested containers or evaluating
their cgroup/network/start-stop assertions. Netif cleanup additionally reports
the absent container; that is secondary to image creation failure.

The `latest` device-unit container is actually **Leap 16.0**, as its captured
`/etc/os-release` proves (`systemd-device-units/machine-failure-diagnostics.log:1851–1859`).
The test reaches its eth0 readiness poll, not the later dummy-device assertions.
The exception is raised by the unchanged shell transport after command timeout
(`osvm/lib/osvm/shell.rb:396–398`). The current evidence does not establish
whether the final blocked call is in systemctl, attach, or another command
layer. It is not evidence that the new Leap 16.1 image failed to build.

For `misc-attrs`, the shell log records this sequence in guest local time:

- 06:35:58–06:36:01: create `/immutable-zfs.file`, status 0.
- 06:36:01–06:36:03: `chattr +i`, status 1 because namespace attach fails.
- 06:36:03–06:36:05: ensure-cleanup `chattr -i`, status 0.
- Subsequent append-only operations and the other three examples pass.

No immutable-flag assertion is reached in the failed example. The container
entered RUNNING at 06:35:58 and has no recorded stop until cleanup at 06:37:07
(`cgv2-failure-diagnostics.log:6927,7336`). This is consistent with an
intermittent attach failure, but does not identify the kernel/LXC process race
or prove its root cause. The separate `kernel/misc` use of the same script and
machine constructor passes all four examples in this same run (core log
2080–2130). It has a different concurrent workload and is not a substitute for
the failed combined group.

## Exact-base comparison and attribution

Both existing base runs confirm source `742eb30…`, tree
`19f423e70ff439867d4bb27e8ed07b9c95fdb703`, and finish with **103 successful,
six failed test groups: exactly the seven openSUSE scripts above**.

| Base run / core job | Runner | `kernel/vpsadminos#misc-attrs` |
| --- | --- | --- |
| [41737858313 / 126297218026](https://github.com/vpsfreecz/vpsadminos/actions/runs/41737858313/job/126297218026), staging | gh-runner2, same as refreshed feature | passed, 90.17 s |
| [41714888844 / 126219010448](https://github.com/vpsfreecz/vpsadminos/actions/runs/41714888844/job/126219010448), upstream feature | gh-runner1 | passed, 103.44 s |

The staging-base native artifact independently matches the **actual errors**:
`base742-artifact/os-test-cgroups__mount-v1-1b384484/test-runner.log:14`
has the same missing Leap 16.1 image; device-units log lines 8 and 33 has the
same missing image and timeout at the same eth0 status command (its timeout
output is `error: SIGTERM`, rather than the refreshed empty output). Its guest
diagnostic also identifies `latest` as Leap 16.0. Other Leap failures are
matched by exact script lists and the unchanged shared image-creation path.

Upstream `dd188397..742eb30` added Leap 16.1 to the distribution lists and
changed device-unit coverage from expected failure/direct status to mandatory
polling, while adding `udev` to the openSUSE recipe. These are upstream changes
in `tests/distributions.nix`, `tests/suite/systemd/device-units.nix` and
`image-scripts/include/opensuse.sh`. The six feature replay patches touch none
of these files or failing test scripts.

Core containers use the published default repository
(`osctld/lib/osctld/db/repositories.rb:11`, `https://images.vpsadminos.org`).
Passing the separate image build/test workflow does not publish its output to
that repository. The failure evidence shows new tests/expectations preceding
availability of the corresponding published images. It does not establish
whether a separate publication has since occurred. Do not silently weaken the
upstream assertions or claim a retry will repair publication.

The metadata correction supplies provider revision/dirty/suffix and channel
metadata. None of these scripts compares those values. Base-to-head inspection
finds no changes in their scripts, distributions, machine configs, kernel/LXC
recipes, osctld, osvm or `flake.lock`. The old feature `1a637e9e` already passed
the full core suite with the same correction. This provides no causal link
from the correction to the attach error; it does not prove equivalence of
every runtime input. Actual full VM/input graph equality was not established,
and the attach failure did not occur in either inspected exact-base run.

## Smallest warranted next action

1. Give the seven openSUSE scripts an explicit **FAILED / exact-base failure**
   disposition. If resolving them is required for integration, the product
   decision belongs to the lead/user: complete upstream image publication and
   verify its image-selection contract, or authorize separate upstream repair.
   This investigation does not authorize an openSUSE delivery project.
2. Keep the additional attach failure unresolved. Recommend one
   verification-only package owned by implementer2 after lead authorization:
   run the unchanged **`kernel/vpsadminos` group** at the exact current head,
   retaining its six-script concurrency and ordinary machine configuration,
   with complete shell/console diagnostics and source/kernel/LXC receipts.
   This preserves the failed example's concurrent context; an isolated
   `#misc-attrs` pass would have a narrower meaning. Use the normal local-code
   runner and required fresh utility. Stop for an unexpected kernel build or
   a repeated attach failure; do not add retries, suppressions or code changes
   merely to obtain green. The lead must assess the result before integration.
3. No source patch or substantive design change is justified yet. Keep the six
   reviewed commits and the four release split intact. The nine previously
   classified livepatch fixture failures remain separate and unchanged.

No tests, VMs, builds, CI retries/cancellations, source edits, commits,
repository claims, deployment or lifecycle operations were performed.

## Retained evidence

- Current per-case artifact and exact-head receipts: [ci-refresh-result.md](ci-refresh-result.md).
- Base job logs: `ci-root-cause/ci-base742-staging-core-126297218026.log`
  (head/tree 248–249, misc result 5073, totals/failures 5405–5415) and
  `ci-base742-feature-core-126219010448.log` (249–250,4271,5431–5441).
- Base native artifact `13292369812`, metadata tied to run 41737858313/head
  742eb30, 3,211,541 bytes; ZIP `ci-root-cause/ci-base742-native-13292369812.zip`,
  SHA256 `f3ff8d71b63f38e47c56638e2ffeb7dff97a2c8ba8b07108a37a7bc6fc9e0602`.
  Selected original logs are under `ci-root-cause/base742-artifact/`.
- Current `cgv2-shell4.log` was extracted from the already-retained current
  native ZIP into its existing `native-failures/kernel-vpsadminos/` directory.
