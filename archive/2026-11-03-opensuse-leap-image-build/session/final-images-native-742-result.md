# Final native image batch

- Result: passed; command exit status 0. All four selected tests completed successfully after one attempt. No retry or cancellation occurred.
- Tested source revision: `742eb30cb1a8b6766c85e915d26b0400e38244b1`.
- Command: `/home/aither/workspace/ai/vpsfree.cz/work/2026-11-03-opensuse-leap-image-build/final-runner-742eb30cb-v3.sh test --jobs 2 --stop-on-failure --no-destructive --state-dir /tmp/2026-11-03-opensuse-leap-image-build-final-742eb30cb-images 'image-scripts/test@opensuse-{leap-15.6,leap-16.0,leap-16.1,tumbleweed}'`
- Runner elapsed: 2,564 seconds (command launched 22:11:34; final guest completed 22:53:22, runner returned 22:54:18). Runner output log: `session/final-images-native-742.log`.
- Final outcome counts: 4 passed; 0 failed; 0 expected failures; 0 unexpected successes.

| Selector | Result | Runner elapsed | Primary test JSON | SHA256 |
| --- | --- | ---: | --- | --- |
| `image-scripts/test@opensuse-leap-15.6` | 15/15 passed | 1184.54s | `/nix/store/fbn2vwka2qdnbyrkqsp3jpqqgmjjhgsq-os-test-image-scripts-test-opensuse-leap-15.6.json` | `4e08e5486ab3df102f681a001158e6245e7541bcf058fababb2ea2d55af715f5` |
| `image-scripts/test@opensuse-leap-16.0` | 15/15 passed | 1146.70s | `/nix/store/dw0qknr27z2gyqv4k7b6glrhy988dk8g-os-test-image-scripts-test-opensuse-leap-16.0.json` | `07052fb31996fd48b84c4e9f48ab9e9b7c60c9569e2d6cc00a9fd6ae9099f8fa` |
| `image-scripts/test@opensuse-leap-16.1` | 15/15 passed | 1111.67s | `/nix/store/j50dk28jfqwz1nvlmrm8s0nbg3jln0i0-os-test-image-scripts-test-opensuse-leap-16.1.json` | `aadb815caca564460f176718719ed8eba3608b0b059d61c7f6dcb7389144aae9` |
| `image-scripts/test@opensuse-tumbleweed` | 15/15 passed | 1037.08s | `/nix/store/a6z3vcbfx1j1qycms0rzk1bmllqsbbj7-os-test-image-scripts-test-opensuse-tumbleweed.json` | `cc959e564a7119d3a8360b25e5d3a393a4007a02aadd2231a6a2f03f496c4942` |

## Common realized VM identity

Extracted from the four actual native test JSON files:

- System: `/nix/store/hq96hymxp4wp8j9bhcy51lp6j5nffnpf-vpsadminos-system-vpsadminos-26.05pre-git`
- Kernel: `/nix/store/b043pwyanxjfz22hbiibv5wipqqcl932-linux-6.12.113/bzImage`
- Initrd: `/nix/store/p1a2p526kvg1zsz7j5wwmg68i9m1z2zm-initrd/initrd`
- Source mounted into each guest: `/nix/store/m1n49nc1qdf1f3j298zcmjjb5ni43iag-source`
- Common squashfs: `/nix/store/97xwp1v7pc4xxdjv6xghdk5g0iyvfdh0-squashfs.img`

## Retained evidence and effects

- Native state: `/tmp/2026-11-03-opensuse-leap-image-build-final-742eb30cb-images`
- Complete root runner output: `/home/aither/workspace/ai/vpsfree.cz/work/2026-11-03-opensuse-leap-image-build/session/final-images-native-742.log`
- Per-case full machine console, shell, machine, filesystem, and test-runner logs and result markers are copied to `session/native-completed-{15.6,16.0,16.1,tumbleweed}/`. Each folder also contains a byte-identical `primary-test.json` copy.
- Guests powered off normally after tests. Runner exited; no active batch process or guest remains. The non-destructive state and image artifacts are retained.
- No kernel panic, watchdog, OOM, bootstrap error, or local kernel compilation was observed. Tumbleweed console included the raw warning `systemd-journald[30]: Failed to send stream file descriptor to service manager: Connection refused` at guest uptime 732s; all 15 Tumbleweed tests passed. It was reported to the parent for owner assessment.
