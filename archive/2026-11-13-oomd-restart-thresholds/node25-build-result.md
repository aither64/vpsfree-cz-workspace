# node25 configuration build result

- Command: `nix develop -c confctl build cz.vpsfree/nodes/prg/node25`
- Revision: `08d68a85f24a95b70b2d806f995f04b236e4d89a`
- Result: failed, exit status 1. `confctl` listed `cz.vpsfree/nodes/prg/node25` and then reached EOF while awaiting its `Continue? [y/N]` confirmation. No node configuration build receipt or system path was produced.
- The confctl log records successful settings evaluation and machine-list evaluation, including `/nix/store/5z8s8rq1sdifp28x3r0c0vykbhsgfrpf-machine-list.json`; these are preparatory evaluations, not the node build.
- Complete command output: `node25-build.log`
- confctl log: `../worktrees/2026-11-13-oomd-restart-thresholds/vpsfree-cz-configuration/.confctl/logs/2026-11-13--22-21-26-confctl-build.log`
- The command process session 88438 and its operation cell completed; exit status captured. No other operation-owned sessions or cells were started.
