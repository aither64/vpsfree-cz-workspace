# Reviewed branch refresh

Completed by implementer0 on 2026-11-04; session identity and saved
workspace_write access verified. No claim was acquired, no feature/default
integration or publication occurred, and no long test/system build was launched.
Git/index writer authority is released to the lead; all commands have exited.

- Repository/target: `git@github.com:vpsfreecz/vpsadminos.git`, `origin/staging`.
- Old reviewed/tested range: `dd188397abe37d0bc33f4c5dfb3605206ce5e326..1a637e9eac4311adba2b08d60dfa7a17d07bcb52`.
- New range: `742eb30cb1a8b6766c85e915d26b0400e38244b1..54b4313404cea35b58ebb9df951ae75e27c44971`.
- New tree: `5c03648e084e907957b37263846bc5763abdac1f`.
- Preserved old head: local branch `2026-11-03-redhat-image-releases-tested-1a637e9e`.
- Fetch confirmed staging exactly `742eb30`; its three openSUSE commits touch
  seven paths, none overlapping this feature. Replay was conflict-free.

| Logical owner | Old SHA | New SHA |
| --- | --- | --- |
| CentOS Stream 9 | `09f209688616b60155e9ac99fa8431a11b9e20a0` | `3aac965d5d6bdaa2fa8a139dd10159201c26b54f` |
| CentOS Stream 10 | `a3c7c77459762d1a45f323de0f3f8dd5d8447323` | `b436a06ba9c27bb3195f0d8ba32eed633d0e1fb8` |
| Rocky 9 | `6ede3bd22b2ed28fb28a5a912f3a7daf7743fb6a` | `31bfa71efd3ec4d223b61076b2376bebb784db56` |
| Rocky 10 | `3307df52ea5bf875e1d8a23318a64f569d8b3ebc` | `ea432db774500954351387fb8a10a112e98f13bf` |
| Nullable channel | `52fba5ee5aac2e171375a780d3860a86e71e5d65` | `b19dbec8bf90554569b1f0e6a9083443d17238e5` |
| Source identity, including final review fixes | `1a637e9eac4311adba2b08d60dfa7a17d07bcb52` | `54b4313404cea35b58ebb9df951ae75e27c44971` |

[Range-diff](refresh-range-diff.txt) has six `=` entries; SHA-256:
`18d50a56223a76c4557dcf41f3ca446181bca3b5caae64f49efd36d7defd2682`.
Every corresponding `git show --format= --binary` patch was also asserted
byte-identical. The complete base-to-head binary diff is byte-identical, SHA-256
`fad353998f3403cb5ec86bc7becffce937ffde4e377e3ecae0ca6ad64e0d350e`.
All six logical commits remain, with no repair/WIP residue or migrations.

## Quick checks and target preparation

Passed at the refreshed head: `bash -n` on all four changed image scripts,
committed whitespace check, `nix develop --command overcommit --diff 742eb30cb1a8b6766c85e915d26b0400e38244b1`
(Nixfmt and RuboCop), and both focused Nix checks:

```sh
nix eval --impure --raw --file tests/source-version-eval.nix
nix eval --impure --raw --file tests/channel-revision-eval.nix
```

Feature worktree and index are clean. The existing
`worktrees/2026-11-03-redhat-image-releases/vpsadminos-merge-target` was advanced
from `dd188397` to `742eb30` by an ordinary base-only `git merge --ff-only`.
It remains clean and detached; no feature content was merged there.
Its installed hook/config validation and empty-index pre-commit passed using the
feature's prepared Nix shell. Target and feature hook configuration/plugin hashes
match; signature verification remains enabled (`1`), with no disable/skip flags.

Reusable preparation, from the feature worktree, before any future claim:

```sh
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-03-redhat-image-releases/vpsadminos
nix develop --profile /home/aither/workspace/ai/vpsfree.cz/work/2026-11-03-redhat-image-releases/refresh-hook-shell --command bash
```

The native profile roots `/nix/store/sqm40mjssnj07w9zf18jk1nvvwp3sazf-vpsadminos-env`.
After shell setup finishes, use `git -C ../vpsadminos-merge-target ...` from that
ready environment. Acquire future integration ownership only after setup;
entering the shell runs the repository's Gem setup and belongs outside a claim.
Ruby is 3.4.11, Overcommit 0.74.0, Nixfmt 1.5.0; GEM_HOME and executable path use
the feature worktree's prepared `.gems`, not a second target gem installation.
Selected package coordination instructions were read via `workspace-host
coordination guide` before target preparation. No lifecycle action was performed.

## Verification inputs and next actions

[Original successful evidence](ci-managed-result.md) remains specifically at
`1a637e9e`: core 317 scripts / 109 tests, four native 24 GiB image cases, plus
RSpec/RuboCop success. Nine pre-existing fixture failures retain their separate
accepted disposition; they are not relabeled passes.

No old test result is claimed at the refreshed head. `flake.lock` remains
SHA-256 `604e01bde4cf21e1532e9ed6e6cfb993da28439355ad7dceb5560447827c5baa`,
and kernel declarations/configuration are unchanged. However, upstream adds
openSUSE recipe/helper content, image-repository selection, distributions and
device-unit behavior. Channel construction copies the whole OS/image-scripts
inputs (`channel.nix:17-37,68-75`); the captured source path and head-bound
revision/suffix/script input also change. Actual test-JSON/VM derivation and
complete input identity with old receipts were not established. Patch equality
therefore does not justify integration-test reuse. No system was built to seek
an equivalence claim.

Lead next: retained independent refresh scope/history review, then publish the
feature and obtain necessary exact-head CI. First inspect new-head runs:

```sh
gh run list --repo vpsfreecz/vpsadminos --branch 2026-11-03-redhat-image-releases --commit 54b4313404cea35b58ebb9df951ae75e27c44971 --json databaseId,workflowName,headSha,status,conclusion,url
```

If a qualifying current-head core or image workflow is missing, dispatch only
the missing workflow after publication/review, avoiding duplicate runs:

```sh
gh workflow run ci.yml --repo vpsfreecz/vpsadminos --ref 2026-11-03-redhat-image-releases -f test_suite=ci -f prebuild=true
gh workflow run image-scripts.yml --repo vpsfreecz/vpsadminos --ref 2026-11-03-redhat-image-releases -f stop_on_failure=true
```

Verify actual selection/execution of all four Red Hat cases. A force-push event
uses a nonancestor before-SHA, so the detector falls back to merge-base and may
also select the newly integrated openSUSE images; a manual dispatch compares
with current staging. RSpec/RuboCop have no workflow_dispatch trigger; their
old-head successes remain old-head evidence and further scope belongs to the
lead/reviewer. Monitor any long CI through a fresh native utility; this package
launched none of the commands above. Integration remains the lead's operation.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-03-redhat-image-releases/)
