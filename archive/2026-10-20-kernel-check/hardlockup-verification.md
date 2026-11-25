# All-node hard-lockup panic setting

Historical package, superseded and withdrawn by the user's OS-policy relocation.
The retained configuration branch now has zero diff and zero feature commits;
see [withdrawal and final refs](hardlockup-configuration-withdrawal.md). The
following results apply only to former commit `8515b682`.

Implementation, quick verification and final independent review complete;
the feature branch is published. Required all-node build was attempted and is
blocked by this host's missing provisioned initrd key. No deployment, live
sysctl write, reboot or crash test has occurred.

- Repository: `vpsfree-cz-configuration`.
- Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-20-kernel-check/vpsfree-cz-configuration`.
- Feature branch: `2026-10-20-kernel-check`.
- Final base: `d5c95e9315fb62cf38a172b303527c6553d752ba`.
- Final head: `8515b68288be7f6c78ed010f93d1424c377973fd`.
- Full branch series: one commit, `nodes: panic on hard lockups`.
- Final diff: one insertion in `cluster/cz.vpsfree/nodes/common/all.nix:63`,
  `"kernel.hardlockup_panic" = 1;`, in the existing `boot.kernel.sysctl` set.
- Source blob: `98be5724bbabc1bc9a561d7a0d5180243cf67f32`.

SSH publication was verified with `git ls-remote`: the feature branch is at
the final head and upstream master remains at the final base. The source
worktree is clean. Native comparison was captured, this evidence was registered
in the portal, and the repository claim was explicitly released at
`2026-10-21T11:09:50Z`.

The native registration retains its true initial base
`86e19685313270d88e4db30038c056ce4b807abd`. Upstream advanced during setup;
the branch was rebased before its first commit. The four intervening upstream
commits, including input updates, are baseline history, not feature changes.
The final feature range contains no input/channel/dependency updates,
superseded approaches, fixups, generated artifacts or migrations. No migration
was merged, released, deployed or externally consumed.

## Checks and scope

All commands used the repository's declared `nix develop` environment.
`nixfmt --check cluster/cz.vpsfree/nodes/common/all.nix`,
`nix-instantiate --parse cluster/cz.vpsfree/nodes/common/all.nix`,
`git diff --check` and `bundle check` succeeded. `confctl ls
"cz.vpsfree/nodes/*"` listed the accepted 13 nodes.

Overcommit hooks were installed and signed under held repository claim
`7705e877-96de-4d8f-a595-a8f4df22fc19`. The commit used `git commit -F`.
Pre-commit Nixfmt passed; commit-message hooks passed with an advisory text-width
warning on a body line longer than 72 but no longer than 80 characters.
See [commit log](hardlockup-commit.log).

The [session evaluation helper](hardlockup-eval.nix) imports the exact pinned
confctl evaluator after adding only an `audit` result accessor. It retains the
original `evalConfigFor`, system module lists, special arguments, channel/input
selection and real repository paths. It does not evaluate a reduced module
fragment. Evaluation command:

```sh
nix develop -c nix eval --impure --json --expr \
  'import /home/aither/workspace/ai/vpsfree.cz/work/2026-10-20-kernel-check/hardlockup-eval.nix { confDir = "/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-20-kernel-check/vpsfree-cz-configuration"; }'
```

Evaluation exited 0. The shell's stdout greeting is retained with the original
JSON in [raw output](hardlockup-effective-raw.txt); [strict JSON](hardlockup-effective.json)
contains only the decoded JSON object. [Stderr](hardlockup-effective.log) records
the dirty-tree notice and the newly pinned OS input unpacking. Evaluation ran
before commit against the identical final source blob and unchanged lockfile;
[identity/checksums](hardlockup-verification.json) bind those bytes to final head.

[Assertions](hardlockup-check-receipt.py) and their
[successful output](hardlockup-effective-check.log) establish:

| Inventory path under `cz.vpsfree/nodes/` | Effective integer | Generated line |
| --- | --- | --- |
| `brq/node5`, `brq/node6` | 1 | `kernel.hardlockup_panic=1` |
| `pgnd/node1` | 1 | `kernel.hardlockup_panic=1` |
| `prg/backuper2` | 1 | `kernel.hardlockup_panic=1` |
| `prg/node19`, `prg/node20`, `prg/node21`, `prg/node22` | 1 | `kernel.hardlockup_panic=1` |
| `prg/node23`, `prg/node24`, `prg/node25` | 1 | `kernel.hardlockup_panic=1` |
| `stg/node1`, `stg/node2` | 1 | `kernel.hardlockup_panic=1` |

The generated line is in each node's `sysctl.d/60-nixos.conf`. Evaluated
`cz.vpsfree/machines/aitherdev` and `cz.vpsfree/containers/prg/int.log` controls
have no configured hard-lockup panic value and no such generated assignment.
The authoritative ordinary inventory has 67 entries: 60 `cz.vpsfree` roots
and seven unmanaged `org.vpsadminos` metadata entries. Exactly 13 are nodes.
Implementer2 independently corroborated import coverage, no overrides, the
unchanged seven unmanaged metadata entries, the helper's full module path,
strict/raw output equality, pins and final one-line commit. They ran no second
evaluator or build.

The unchanged lockfile SHA-256 is
`e8a71f0423a400ce933a2338fa47a9e0fe77f73ad2c3dda69fd87b35350bc34c`.
Relevant pins:

| Input | Exact revision |
| --- | --- |
| confctl | `7bee58a52372b95c2198ce3f2a719807a3c2c66b` |
| nixpkgsStable/Production/Staging | `cd4ea8d57de16f4810bc5f14207bac45fbf19f67` |
| vpsadminosProduction | `2abbe3cc1c102a4b39022d3f73ef4a432ad4d616` |
| vpsadminosStaging/OsStaging | `252b80dfdb4bced0713e8423ef7ba3d5600d05dd` |

## Setup and check corrections

The first native `dev-session worktree add` fetched and created the worktree,
but an existing post-checkout Overcommit hook exited 78 because declared gems
were absent. The created checkout was preserved. Repeating the supported native
command with `--no-fetch` registered that existing checkout and exact initial
base; `nix develop` then installed the declared gems and `bundle check` passed.
No hook was bypassed. All subsequent shared Git/hook-trust operations ran under
the repository claim.

The first evaluation invocation incorrectly expected `nix eval --file` to apply
a function using `--argstr`; it failed with “cannot convert a function to JSON”.
[Initial quick-check log](hardlockup-quick-checks.log) retains that failure.
The explicit-import command above succeeded. A local assertion initially
expected 60 total inventory entries; the receipt correctly contained 67.
The assertion was corrected to distinguish 60 site roots and seven external
metadata entries. No application or input change addressed either check error.

## Review, build and activation limits

Final review packet: high risk because host failure policy changes; general,
architecture, scope and risk lanes. No separate repository documentation change
is useful for one standard sysctl. The architect-owned
[design brief](design.md#all-node-hardlockup-panic-configuration) records why the
policy was selected, its 13-node scope, compatibility, startup application and
runtime rollback caveats. Mixed old/new node configurations are supported; no
fleet-wide coordinated update or persisted-state migration is required.

The lead reported reviewer0's final acceptance of the exact base/head range
above, all four lanes, no findings, with explicit whole-history, no-migration
and no-repeated-update-stream conclusions. The retained reviewer used saved
Sol/xhigh settings. The only repository workflow is scheduled/manual daily
update; it has no push trigger. Exact-head `gh run list --commit 8515b682...`
returned no runs; see [CI receipt](hardlockup-ci.json).

After accepted final review, first dry-run the exact pinned confctl build
outputs (`toplevel` and `autoRollback`) for these 13 ordinary nodes and report
substitutions/cache gaps. Proposed required build:

```sh
nix develop -c confctl build --yes 'cz.vpsfree/nodes/*'
```

Each uncertain operation uses a fresh pinned Luna/low verification watcher.
Stop an unexpected local kernel build and investigate its missing substitution;
this edit changes neither kernel source nor kernel build configuration. Builds
and review do not authorize activation or default-branch integration. A future
authorized rollout must verify the actual running sysctl; source/evaluation
cannot prove that running nodes have applied it or that a panic will dump.

The post-review dry-run was attempted with fresh standalone utility thread
`01a15e2a-4457-7723-9026-9658eaaed74a`, pinned `gpt-6-luna`/low and explicit
`danger-full-access`/approval `never`. See its
[launch policy](hardlockup-dry-run-watcher-launch.json),
[report](hardlockup-dry-run-watcher-report.txt),
[full output](hardlockup-dry-run.log) and
[exit receipt](hardlockup-dry-run-watch-result.json). It exited 1 after
74.65 seconds (inner Nix dry-run: 54.72 seconds). Evaluating node5's top-level
failed because `/secrets/nodes/initrd/ssh_host_ed25519_key` is absent. No
substitution/kernel-cache plan was reached, so no cache availability conclusion
is possible and no kernel compilation started.

`common/netboot.nix:21–24` already requires both RSA and Ed25519 initrd host-key
paths; `common/all.nix:243` already names per-node image secrets. Local metadata
confirms `/secrets/nodes` is absent. The repository's deploy environment assumes
that provisioned secret tree; no documented already-authorized local retrieval
mechanism was found. Secret contents were never read or copied, and no
placeholder, alternate input, source workaround or production access was used.
The lead accepted this prerequisite limitation and directed one actual required
`confctl build` invocation under a separate fresh watcher to retain its status.
A missing build prerequisite does not undo the
successful full-module sysctl evaluation or imply a source error in this patch.

The required `nix develop -c confctl build --yes 'cz.vpsfree/nodes/*'` was
then attempted by fresh standalone utility thread
`01a15e2d-2ce1-7051-9380-f57813924c1a`, using the same pinned Luna/low and
explicit full-access policy. It selected all 13 nodes in one build group and
exited 1 after 58.12 seconds at the same missing key during node5 top-level
evaluation. No kernel compilation was observed. See the
[launch policy](hardlockup-build-watcher-launch.json),
[watcher report](hardlockup-build-watcher-report.txt),
[exit receipt](hardlockup-build-watch-result.json),
[combined log](hardlockup-build.log) and
[complete confctl log copy](hardlockup-confctl-internal.log).

Both verification operations and their standalone watchers have exited; no
owned build remains running. Final source head is unchanged and clean, the
repository claim remains released, and there was no default-branch or
production mutation. [No-active-operation receipt](hardlockup-no-active-operations.json)
binds this final status. A provisioned authorized build environment is needed
to complete system builds and inspect kernel substitutions; no speculative
retrieval or placeholder is proposed. The session remains open.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-20-kernel-check/>
