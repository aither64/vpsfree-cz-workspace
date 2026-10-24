# Package D final R local source inventory

Both configuration adoptions now select provider
`5436d3d7c36d3d5174eab3c44e3578830749d3db` (R). Each branch retains one logical
adoption commit. The only P-to-R change in either workflow is the exact tool SHA.
All intended edits are committed and worktrees are clean. **Pushes are held for
the lead's final mechanical pin/history review.**

| Repository | Base | Local R head | Prior published P head / future feature lease |
| --- | --- | --- | --- |
| vpsfree-cz-configuration | `50d263d4127c05163d660fae1c4b9b887584032d` | `28ce92517be0151c0bd52f7ae6e64632474888e9` | `7b0609cf41fc9fe54b6d09129246ff100fb4197a` |
| vpsadminos-org-configuration | `6b04b48e9c076e5525ccb7c38ce174232414f0b5` | `949220c108d3c87341457aa96649dd92bad333b6` | `4352f16fb967e3b9da829972c9799157badd0494` |

Fresh SSH fetches before the pin edits and SSH `ls-remote` observations after
local consolidation confirmed unchanged default bases and the prior P feature
heads. They are point-in-time observations, not publication proof for R.
Exact refs, observation times, trees, series, paths, blob hashes and leases are
in [package-d-branches-r.json](package-d-branches-r.json).

Both full diffs touch only `.github/workflows/daily-update.yml`:

- [vpsFree full adoption](package-d-r-vpsfree-cz-configuration.diff),
  [P-to-R delta](package-d-r-vpsfree-cz-configuration-from-p.diff): 53 insertions,
  26 deletions across the complete base-to-head range.
- [org full adoption](package-d-r-vpsadminos-org-configuration.diff),
  [P-to-R delta](package-d-r-vpsadminos-org-configuration-from-p.diff): 37
  insertions, 9 deletions across the complete range.

`flake.nix` and `flake.lock` blobs equal their respective bases. Deployment-tool
inputs, runtime options and machine configurations are unchanged. There are no
migrations, released/deployed state boundaries or obsolete pin commits in either
final history. Earlier P publication, review and runtime evidence remain in
their original records; the remote feature branches still point to P adoptions.

## Checks and documentation

[package-d-quick-r.log](package-d-quick-r.log) records 20 actual workflow-body
fixture scenarios, YAML parsing and Bash syntax passing in the old vpsFree tools
shell. They cover exact pinned inner tool selection, channel selectors, llm-agents
condition/postcondition, hook and late-update failures, final rejection/error,
committed-lock validation despite working-tree drift and ordinary push refusal.
The successor fixture is [package-d-workflow-check-r.py](package-d-workflow-check-r.py).
It is static/mocked workflow proof, not a real final-R package or update run.

Ordinary declared-shell hooks passed during both local amends:
[vpsFree](package-d-r-commit-vpsfree.log), [org](package-d-r-commit-org.log).
Only the workflow was staged in each repository; no unstaged tracked files were
present during hooks. Commit-message warnings concern soft 72-column guidance;
all lines meet the required 80-column limit.

No user-visible wording, imported action refs or workflow commands changed from
the reviewed P adoptions. Existing lead prose review and action compatibility
evidence remain applicable. The owning technical behavior remains in confctl's
input guide/manual. Temporary source, history and execution evidence belongs
here, without configuration documentation or deployment receipts added to either
repository.

## Provider and remaining verification

R retains the guard commit plus one packaging fix. Published P to R changes only
the generated real-hook fixture's declared interpreter path, including preservation
of the multicall `env` dispatch name. The exact immutable local R exported check
passed 197 examples with zero failures or pending cases under the lead's watcher.
See [provider inventory](package-b-r-inventory.json) and
[fixture diagnosis](package-b-r-fixture-report.md).

The next gate is complete eight-history mechanical pin/affected review. After
approval and provider-first publication, final runtime manifests/drivers must bind
R and these exact heads. Fresh GitHub R source NAR/input graph, package and check
derivations must be compared with the successful local R exported check before
reusing that suite result. Real old-shell/config/IRC package boundaries, seven
nonpublishing patterns, Git race and Terraform VM remain root-serialized work.
No additional full suite is required without an identity mismatch or new change.
No integration, deployment or lifecycle action is authorized.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-flake-update-downgrade-guard-replacement/
