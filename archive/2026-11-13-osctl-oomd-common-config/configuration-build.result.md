# All-node configuration build

- Operation: `543371f6-4043-42ec-a05a-df9ab34d4ad7`
- Result: failed, exit status 1
- Revision: `48e94d18b467d1a3999fb906f0fd726968146267`
- Command: `nix develop --no-write-lock-file -c confctl build --yes cz.vpsfree/nodes/*`
- Working directory: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-13-osctl-oomd-common-config/vpsfree-cz-configuration`
- Elapsed: approximately 41 seconds
- Selected targets: 13 (`brq/node5`, `brq/node6`, `pgnd/node1`, `prg/backuper2`, `prg/node19` through `node25`, `stg/node1`, `stg/node2`)
- Output evidence: Nix evaluation ended with `error: path '/secrets/nodes/initrd/ssh_host_ed25519_key' does not exist`.
- Complete captured output: `configuration-build.log`
- Exit status record: `configuration-build.exit`
- confctl log: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-13-osctl-oomd-common-config/vpsfree-cz-configuration/.confctl/logs/2026-11-13--23-11-09-confctl-build.log`
