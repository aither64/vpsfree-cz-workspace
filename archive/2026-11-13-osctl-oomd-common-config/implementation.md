# Package I implementation evidence

Owner: `implementer0`. Implemented the accepted [design](design.md) without
deviations. Independent final review and required node builds remain with lead;
this is implementation evidence, not a completed review/build result.

## Revisions and scope

- Repository: `git@github.com:vpsfreecz/vpsfree-cz-configuration.git`.
- Branch: `2026-11-13-osctl-oomd-common-config`.
- Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-13-osctl-oomd-common-config/vpsfree-cz-configuration`.
- Freshly fetched base/target: `08d68a85f24a95b70b2d806f995f04b236e4d89a`.
- Final head: `48e94d18b467d1a3999fb906f0fd726968146267`.
- SSH push completed. Fresh `git ls-remote --heads origin master 2026-11-13-osctl-oomd-common-config`
  confirms remote feature head equals the final head and remote master equals
  the base; local upstream matches. No rebase was needed; worktree is clean.
- Complete base-to-head series: one commit, `cluster: share osctl-oomd tuning across nodes`.
- Diffstat: `common/all.nix` +2; `prg/node25/config.nix` -5; exactly two files,
  two insertions and five deletions. Full diff: `git diff 08d68a85f24a95b70b2d806f995f04b236e4d89a..48e94d18b467d1a3999fb906f0fd726968146267`.
- Shared settings gain `restart_hits = 4;` and `load_multiplier = 1.5;`;
  node25's duplicate block disappears. Existing enable/verbose values remain.
- No migrations, persisted formats, compatibility paths, dependency/pin update
  streams or superseded source approaches. No history consolidation needed;
  the unpublished commit message was rewrapped to satisfy TextWidth warning.

## Quick checks and hooks

All checks passed in the repository's `nix develop --no-write-lock-file` shell:

- `bundle check`; `bundle exec overcommit --version`: locked dependencies
  satisfied, Overcommit 0.76.0.
- `bundle exec overcommit --install`; `bundle exec overcommit --sign`:
  installed and signed the declared configuration; executable hooks verified.
- Initial worktree creation returned 78 from the existing post-checkout hook
  before gems existed. Verified the created branch, exact base, clean files and
  portal registration; shell installed the pinned bundle. Reran the installed
  `post-checkout` hook with zero old head, the exact base above and branch flag 1:
  passed. No hook bypass. This follows the existing November 10 worktree note.
- `nixfmt --check cluster/cz.vpsfree/nodes/common/all.nix cluster/cz.vpsfree/nodes/prg/node25/config.nix`: passed (nixfmt 1.5.0).
- `nix-instantiate --parse` for each changed file, output discarded: passed.
- `git diff --check`, final `git diff --check origin/master..HEAD`, complete diff
  inspection and clean final worktree: passed.
- Commit ran installed Nixfmt and commit-message TextWidth, SingleLineSubject
  and TrailingPeriod hooks: all passed without warnings on the final head.
- `rg -n 'restart_hits|load_multiplier|osctl\.oomd' --glob '*.nix'`:
  only the common oomd block and one occurrence of each tuning value remain.

## Existing node import coverage

Inspected each config's imports, its intermediate module's imports, matching
module registration and channel selection: all 13 routes reach `common/all.nix`.
This is source coverage; full node evaluation/build remains pending.

| Nodes | Existing intermediate import | Channel |
| --- | --- | --- |
| `brq/node5`, `brq/node6` | `brq/common.nix` | production |
| `pgnd/node1` | `pgnd/common.nix` | production |
| `prg/node19`, `prg/node20`, `prg/node21`, `prg/node22`, `prg/node23`, `prg/node24`, `prg/node25` | `prg/common.nix` | production |
| `prg/backuper2` | `common/storage.nix` | production |
| `stg/node1`, `stg/node2` | `stg/common.nix` | staging |

## Unchanged input fingerprint and later build command

`git diff --exit-code BASE -- flake.nix flake.lock` passed; both files are byte
identical to the base. SHA-256 fingerprints:

- `flake.nix`: `fd49c6a1506e5241e93f817060736f63d8930554f5bc499462468d9de5fe1e71`.
- `flake.lock` (complete locked input graph): `d6a45cb62482eb2f321d551595325da1b44b1095284abe2acf6f4af57f487877`.
- Locked confctl: `ff5e017780a35fb97b549db2a51b570193867c3b`, NAR hash `sha256-Y7vwZfDEpElVUxEyDdpwHC8/1IapvkMz3/0AFr7U+yw=`.
- Production and staging vpsAdminOS: `c0ad0ad8f970e04099830ff1c2ebfda01e8c9d62`, NAR hash `sha256-zO0kjnP8CR2RaBLjK7Nwwl1PqrtohJCSaFflMS4Dc+Y=`.

`confctl build --help` confirms command option `--yes` for noninteractive use.
After final review, lead's fresh watcher can run from the worktree above:

```sh
nix develop --no-write-lock-file -c confctl build --yes 'cz.vpsfree/nodes/*'
```

Exact argv: `["nix", "develop", "--no-write-lock-file", "-c", "confctl", "build", "--yes", "cz.vpsfree/nodes/*"]`.
No node build, deployment, dry activation, runtime check, claim or integration
was run. The only workflow is daily-update (schedule/manual); no push CI applies.
No project documentation change is useful for this direct two-setting move;
rationale and review evidence stay in this session.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-13-osctl-oomd-common-config/)

## Required-build environment diagnosis

After source acceptance and final review (per lead), the watcher selected all
13 nodes but failed in 41 seconds, exit 1, while forcing node5.brq's top-level
derivation: `/secrets/nodes/initrd/ssh_host_ed25519_key` does not exist. See
[configuration-build.log](configuration-build.log). This is incomplete build
verification, not a passing all-node build.

The unchanged `cluster/cz.vpsfree/nodes/common/netboot.nix:19` enables initrd SSH
and references external RSA and Ed25519 host-key paths. Its import routes cover
all 13 nodes. README and the operations index provide no alternative local
secrets setup. The existing [applicable setup note](../../notes/vpsfree-cz-configuration/2026-07-13-confctl-node-build-initrd-secret.md)
records this exact failure and requires the deployment secrets environment for
a complete build. No already available sanctioned local workaround was found
within this bounded evidence. A documented environment with the required keys
available to Nix evaluation is the missing prerequisite; selecting or preparing
one needs separate direction. The previously recorded build argv remains valid
once that prerequisite is satisfied, but no retry is justified in this environment.

No credential contents or `/secrets` files were read, copied or changed; no
override, source/input change or build retry was made. Netboot and both flake
files remain identical to base; head stays `48e94d18b467d1a3999fb906f0fd726968146267`
and the feature worktree is clean. Dependent full-build verification is blocked;
no two-file implementation defect was found by this diagnosis.
