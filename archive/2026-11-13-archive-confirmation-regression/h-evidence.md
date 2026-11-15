# Package H: runtime pins and deployment parity

Owner: implementer1. Package H accepted; pin implementation, quick checks,
publication, source fidelity and retained-output identity checks are complete.
Lead reports final G/H heads deployed and integrated. Lead owns rollout/state;
this package performed no build, deployment, integration, resource claim or
lifecycle action.

Current final G selection: `9241a342a6ef4ca69148594e98cce7ddcfb459a6`.
Final workspace range:
`aa9333916fdc1062755a88e1b8298b845ec2ccc4..5cde17b6ea854264f3cc8ecd8430f62c3d758688`.
Final configuration range:
`5447fac5342404678d2f72094995ce43e41d7602..111973876df886739be5abe330f58ff6062bf03a`.
Both contain one final pin commit. Earlier reviewed ranges and first configuration
refresh proofs below are historical evidence; no intermediate pin commit is
retained in either final range. Combined narrow review remains lead-owned.

## Baseline

Identity was verified with `dev-session current` from this session's tracking
directory; both session environment identity variables were absent. The saved
roster retains implementer1 as GPT-6.1 Sol/xhigh with workspace-write access and
full-access execution policy.

| Repository | Registered worktree under `worktrees/2026-11-13-archive-confirmation-regression/` | Branch | Fresh remote master / initial base |
| --- | --- | --- | --- |
| Workspace | `workspace` | `2026-11-13-archive-confirmation-regression` | `aa9333916fdc1062755a88e1b8298b845ec2ccc4` |
| Configuration | `vpsfree-cz-configuration` | `2026-11-13-archive-confirmation-regression` | `11ef63c5e173019b5312d672570158a0b0fb6dad` |

Both worktrees were clean after preparation. SSH remotes are
`git@github.com:aither64/vpsfree-cz-workspace.git` and
`git@github.com:vpsfreecz/vpsfree-cz-configuration.git`. Configuration's bare
local master was older; the new branch starts at fetched `origin/master`, without
changing local master.

Workspace's direct nested runtime URL and configuration's `devWorkspace` lock
both select `458c7857b942fb592607c83af7b5287a6c93ea96`, with
`narHash = sha256-fhwNBiEuS0HoMz1Pjxirl1Co9Wl4gEm5c69h9huFBlw=`.
The extension remains `d76bd681c6db981907a52c187a3298549af87ab0`, with
`narHash = sha256-tmO9w6PYaUUHawwFUocsGJES4tSLXl3cf85hZtejE0M=`.
Workspace root nixpkgs follows `vpsfree-dev-workspace/nixpkgs`. The generated
locks are the complete baseline graphs; compare semantic paths, identities and
follows against these recorded base commits after generation.

Configuration channel `dev-workspace` maps role `devWorkspace` to input
`devWorkspace`; `cz.vpsfree/machines/aitherdev` selects that channel.
Its host module and Codex package constructor use
`inputsInfo.devWorkspace.input`. The workspace application remains supplied by
the composed user-profile package. Existing provider operations documentation
already describes this pin/parity contract; routine pins need no product-doc
changes or configuration rollout logs.

## Preparation and checks

- Workspace has no declared root hook framework and no installed custom hooks.
- Configuration's first worktree creation returned exit 78 after making its clean
  checkout because ambient Ruby lacked pinned gems. Inspected the exact owned
  checkout, HEAD, status and common Git directory, then entered `nix develop`.
  `bundle exec overcommit --install`, `bundle exec overcommit --sign` and checkout
  of the same owned branch passed. No hook bypass or ambient gem installation.
- Baseline `bin/check-dev-workspace-deployment --workspace-root WORKSPACE_WT
  --configuration-root CONFIG_WT` passed for the canonical aitherdev workspace
  host at runtime `458c7857b942fb592607c83af7b5287a6c93ea96` (0.13 seconds).
- Configuration shell `confctl inputs channel ls dev-workspace` confirms the
  role/input/revision above.

## Initial pin implementation and review material

Lead released exact published G head
`e96284d1a0484a01888a6d7166fcbd5f68855659`; SSH `ls-remote` independently
confirmed that feature head. Architect H brief is in [design.md](design.md#package-h--runtime-selection-and-deployment-preparation).
No G dependency files changed between runtime base and this head.

| Repository | Complete base-to-head range | Sole commit / final head | Changed files |
| --- | --- | --- | --- |
| Workspace | `aa9333916fdc1062755a88e1b8298b845ec2ccc4..da432f0a2928bf296c497ec66a282e4ee61af960` | `da432f0a2928bf296c497ec66a282e4ee61af960` — `inputs: select provider helper proof fix` | `flake.nix`, `flake.lock`; 5 insertions, 5 deletions |
| Configuration | `11ef63c5e173019b5312d672570158a0b0fb6dad..9f7679c90bb3c7dc2070a611685e631a25e06a51` | `9f7679c90bb3c7dc2070a611685e631a25e06a51` — generated `inputs: set devWorkspace to e96284d1` | `flake.lock`; 3 insertions, 3 deletions |

Workspace was generated using the direct nested exact URL followed by
`nix flake update vpsfree-dev-workspace/dev-workspace`. Configuration used
`nix develop --command confctl inputs channel set --commit dev-workspace
devWorkspace e96284d1a0484a01888a6d7166fcbd5f68855659`, retaining the generated
message and changelog exactly. Workspace used a temporary-file commit message.
Each repository contains one final logical pin commit; no intermediate pins,
follow-up fixes, superseded approaches or retained compatibility paths exist.
There are no migrations in either H range; none were merged, released, deployed
or externally consumed. H performs no state transformation.

Final runtime locked identity is equal in both graphs: GitHub owner `aither64`,
repository `dev-workspace`, revision `e96284d1a0484a01888a6d7166fcbd5f68855659`,
timestamp `1794735740`, and
`narHash = sha256-7J2yBTO+gdq+B1bl9HWyPHOjaXXQKbjDbkKNviR8AT8=`.
Semantic comparison to each exact base proved equal node sets and equal graph
content except this runtime's locked revision/hash/timestamp (plus workspace's
original exact revision). Every input edge/follows and all sibling/transitive
identities, including extension, codex-web, llm-agents, nixpkgs, KB and devcluster
inputs, are unchanged. No generated transitive change was needed.

Complete source/input graphs remain in each exact committed `flake.lock`:

- Workspace lock SHA-256: `37622d11fe1b9f116794755bc2116ab8195fbe1962a19583c3ba6b3189aee38f`.
- Configuration lock SHA-256: `5ebd2b162fe19f23727436e8ea87a7382e7f47ea2f75bdc3e64605319f630d91`.

Quick verification passed:

- Final deployment parity command with both absolute worktree roots: PASS at
  `e96284d1a0484a01888a6d7166fcbd5f68855659` (0.19 seconds).
- Strict lock comparison described above: PASS for both complete graphs.
- Workspace `git diff --check` and `nix-instantiate --parse --quiet flake.nix`:
  PASS; committed range whitespace check also passed.
- Configuration declared-shell channel inventory: `dev-workspace` / `devWorkspace`
  / `devWorkspace` / `e96284d1`; exact `confctl ls cz.vpsfree/machines/aitherdev`
  returned the expected NixOS machine. No other host was selected.
- Configuration Nixfmt pre-commit hook: PASS. Commit-message hooks: PASS with
  the generated-history width warning; message preserved under its explicit
  exception. No hooks bypassed. Push ran in the declared Nix shell.
- Both feature pushes completed over SSH, without changing default branches.
  Fresh `ls-remote --heads` confirmed workspace feature
  `da432f0a2928bf296c497ec66a282e4ee61af960` / master
  `aa9333916fdc1062755a88e1b8298b845ec2ccc4` and configuration feature
  `9f7679c90bb3c7dc2070a611685e631a25e06a51` / master
  `11ef63c5e173019b5312d672570158a0b0fb6dad`. Both final worktrees are clean.
  Workspace defines no GitHub workflow; configuration's sole workflow is
  schedule/manual-only, so these pushes trigger no CI run.

Documentation routing: runtime-selection contract → maintainers / reference →
workspace deployment procedure and configuration
`docs/operations/codex-providers-aitherdev.md` → checked against unchanged
channel/selector and passing parity. Individual execution/review evidence →
lead/reviewer / session record → this file. Routine pin changes require no new
product docs; no configuration rollout receipts were committed.

Remaining limits: independent final whole-branch/history review is lead-owned;
no long build/integration check, application activation, system generation
comparison, deployment or default-branch integration has run in H. Preserve
the architect's host/application distinction and all existing recovery contracts.

## Pre-deployment default drift assessment

Lead identified configuration master advancement while build batch
`b5cf9579` reads the H configuration worktree. Inspection used only the canonical
bare repository; H's worktree and generated outputs remain untouched until lead
confirms the build has ended.

Fetched new default: `5447fac5342404678d2f72094995ce43e41d7602`. Exactly three
commits intervene after reviewed base `11ef63c5e173019b5312d672570158a0b0fb6dad`:

- `acd1a835d389d4ab98a818fbfea9ede821867805`: staging vpsAdminOS input update.
- `723fa6cf0f610d20047a5bcab7e05c925c5dacc3`: production vpsAdminOS input update.
- `5447fac5342404678d2f72094995ce43e41d7602`: enable standalone RTNL watchdog
  in nodes/common/all.nix and remove duplicate staging node settings.

The complete intervening diff is four files, 8 insertions and 10 deletions:
`flake.lock`, nodes/common/all.nix and staging node1/node2 config.nix.
Configuration `flake.nix`, aitherdev subtree, shared modules/profiles/environments
are unchanged. No migrations are present.

Whole-lock comparison proved identical node sets and all edges/follows, with
only `vpsadminosProduction` and `vpsadminosStaging` locked identities changing to
`7554720e640c763639a1ed207b1621143b483025`. H's sole `devWorkspace` node remains
unchanged in the new base, as do aitherdev's selected nixos-stable/home-manager/
llm-agents dependencies. A clean disjoint replay of H's generated pin is expected.

After build-terminal release: rebase the single generated commit in the declared
environment, preserve its message, prove range-diff/patch-ID equivalence and exact
graph reconstruction, rerun scoped quick checks/hooks, then publish using an
exact old-head lease. Lead owns the independent narrow refresh review and later
target-system evidence. No direct aitherdev effect was found, but changed full
configuration source/input identity means the old build alone does not prove the
refreshed exact system derivation or permit claiming target-system equality.

## First configuration refresh execution

Lead released the worktree after confirming the prior monitor's source command
never started and canceling its owning utility. No old-configuration build output
is assumed or reused here. The rebase ran outside claims in the configuration's
declared Nix shell and completed cleanly, retaining one generated pin commit.

- Original reviewed base/head:
  `11ef63c5e173019b5312d672570158a0b0fb6dad` /
  `9f7679c90bb3c7dc2070a611685e631a25e06a51`.
- Refreshed base/head:
  `5447fac5342404678d2f72094995ce43e41d7602` /
  `2ac8f287a7da783cda73fc6ef814527b875071fe`.
- `git range-diff` reports `1: 9f7679c9 = 1: 2ac8f287`.
- Both ranges have stable patch ID
  `650a3de9858e13ad91c7c980c705e5ee1cb6d835`.
- Generated commit messages compare byte-identical. Sole changed path relative
  to the new base is `flake.lock`, with 3 insertions and 3 deletions.
- Strict reconstruction takes the complete new-base graph and replaces only its
  `devWorkspace` node with the reviewed old-head node; the result exactly equals
  the refreshed committed graph. All upstream changes are retained and every
  edge/follows and other node is unchanged relative to the new base.
- New configuration `flake.lock` SHA-256:
  `8260b9f06ab8afd4373caa608fb08242daebdabe6fd5c56ab604940ee66ed874`.
- Deployment parity passed against unchanged workspace head
  `da432f0a2928bf296c497ec66a282e4ee61af960`, selecting the same exact G runtime
  `e96284d1a0484a01888a6d7166fcbd5f68855659` (0.08 seconds).
- Range whitespace check passed. Declared-shell
  `bundle exec overcommit --diff 5447fac5342404678d2f72094995ce43e41d7602`
  passed Nixfmt; no hook bypass. Channel inventory still resolves
  `dev-workspace` / `devWorkspace` / `devWorkspace` / `e96284d1`.
  Exact `confctl ls cz.vpsfree/machines/aitherdev` inventory also passed.
- Declared-shell SSH force-push with an exact lease expecting old remote head
  `9f7679c90bb3c7dc2070a611685e631a25e06a51` succeeded. Fresh remote heads
  confirmed feature `2ac8f287a7da783cda73fc6ef814527b875071fe` and default
  `5447fac5342404678d2f72094995ce43e41d7602`. Worktree remains clean.
  GitHub branch run inventory returned `[]`; no superseded workflow run exists
  to cancel and no CI wait was started.
- No migrations, state transformations, conflict resolutions, new compatibility
  paths or repeated H pin streams were introduced. Neither old nor new H pin was
  deployed, merged, released or externally consumed by this package.

Host-effect conclusion is unchanged from the drift assessment: no direct
aitherdev change was found, while exact refreshed system identity requires new
lead-owned evaluation/build evidence. H did not run a long check or build.

## Final G refresh and consolidation

Lead released published final G head
`9241a342a6ef4ca69148594e98cce7ddcfb459a6`; independent SSH remote lookup
confirmed it. Its child delta from the original provider fix changes only
`portal/cmd/workspace-portal/maintenance_continuation_timeout_test.go` (4+/1-).
Runtime dependency manifests and locks are unchanged.

Workspace amended its sole pin after the prescribed nested flake update, using
a temporary-file message and ordinary hooks. Configuration used a clean rebase
to drop the intermediate pin back to final base `5447fac...`, then the prescribed
declared-shell confctl channel set generated its sole final pin. No lockfile was
hand-edited; no reset, clean, stash, claim, build or deployment was used.

| Repository | Final sole commit / head | Base | Paths / diffstat |
| --- | --- | --- | --- |
| Workspace | `5cde17b6ea854264f3cc8ecd8430f62c3d758688` | `aa9333916fdc1062755a88e1b8298b845ec2ccc4` | `flake.nix`, `flake.lock`; 5+/5- |
| Configuration | `111973876df886739be5abe330f58ff6062bf03a` | `5447fac5342404678d2f72094995ce43e41d7602` | `flake.lock`; 3+/3- |

Configuration's generated message is preserved and states
`devWorkspace: 458c7857 -> 9241a342`, with both G commits in its changelog.
Workspace's prior `da432f0a...` and configuration's prior `9f7679c9...` /
`2ac8f287...` are evidence only, replaced by these final pins. No migrations,
state transformations or retained compatibility paths exist in the final ranges.
No H head has been deployed, released, merged or externally consumed by H.

Strict full-lock reconstruction against each final base passed: only runtime
locked rev/hash/timestamp changes, plus workspace's original exact revision.
Replacing the new runtime node with the prior H node exactly reconstructs each
prior H lock. All extension/sibling/transitive identities and graph edges/follows
are unchanged. Both final runtime objects equal: GitHub `aither64/dev-workspace`,
revision `9241a342a6ef4ca69148594e98cce7ddcfb459a6`, lastModified `1794738296`,
narHash `sha256-Be50ECDhDhL/Q0yAlkAIa2GrWVZgdZ8oIW1sZJaP6D4=`.

Final complete lock SHA-256 identities:

- Workspace: `96ced7da8029c53ef17413d6fa244fbdb43f115b7b92689e72acd7be8be280a6`.
- Configuration: `e162ed9b2375487a460b6ee7b393b0f6a0595c6472113bf6734b785be9fabd1b`.

Range-diff against the prior workspace pin and rebased configuration pin shows
only the final runtime metadata and exact URL substitution; configuration also
has the expected generated subject/changelog update. The earlier clean
configuration base-refresh equality and stable patch-ID proofs remain above.

Quick checks: final parity PASS at exact `9241a342...` (0.09 seconds); strict
graphs PASS; workspace Nix parse and both range whitespace checks PASS;
configuration Nixfmt/commit-message hooks PASS (generated width warning retained);
declared-shell channel inventory selects `9241a342`, and exact aitherdev selector
inventory PASS. Both exact-lease SSH force-pushes succeeded, expecting old
workspace `da432f0a...` and configuration `2ac8f287...` respectively.
Fresh remote heads confirmed final workspace `5cde17b6...` / master `aa933391...`
and final configuration `11197387...` / master `5447fac5...`. Both worktrees are
clean. Configuration branch CI inventory returned `[]`; no superseded run exists.

No substantive H behavior changed. Prior host-effect caveat and documentation
routing still apply; the lead owns independent narrow review and first actual
build/system output evidence.

## Read-only workspace source fidelity

Metadata source `/nix/store/ndckn4nnqnafbpmswvnk21lfk0zy6mly-source` and the
workspace checkout both exactly match committed `5cde17b6...` outside the
reviewed `work/` and `archive/` exclusions: 653 files, zero missing/extra/content
or Git-normalized mode mismatches, four executable files and zero symlinks.
The normalized path/mode/blob manifest SHA-256 is
`9b3d993c2bae05365fefc1bbe62ae6c18eca1d9234a8f5d3af59554c7036f9c9`.
Complete index blob/mode entries equal the commit. All 65,045 excluded tracking
entries are both skip-worktree and absent; all 653 remaining entries are present
and not skipped. Thus the sole full-tree departure is intentionally omitted
tracking, and `dirtyRevision` does not indicate package-relevant source drift.
No private tracking contents were read or retained.

Saved workspace/configuration metadata locks exactly equal their final committed
locks. The saved application derivation and a fresh read of the stored derivation
compare equal as complete JSON. Canonical JSON SHA-256:
`40d62dcfd2e0649766b7071607f80d4b005e2ba9ece6ebe68e610541101db609`.
Observed Nix 2.34.9 format is top-level `version: 4` and `derivations`, keyed by
derivation basename. Entries also have `version: 4` and `inputs`, containing
`drvs` (82) and `srcs` (6); store basenames require `/nix/store/` when resolving.

Exact derivation `/nix/store/kimsqz1nvqqk13mhf23yiardvn87jssx-dev-workspace-0.2.0.drv`
binds the proven workspace source above. Its `env.src` is
`/nix/store/f1qnjr31rlflkxf7h7q260ij7s0af2zn-source`; read-only store NAR identity
equals the final runtime 9241 lock hash. Other source inputs independently match
the final extension and codex-web locked NAR hashes. The expected application
output remains `/nix/store/qxclq96999l3ccs39mj5vw0m5k8hwllx-dev-workspace-0.2.0`.

At this proof boundary the parent-owned restore had not yet populated
`application-retained.path`, and that output was absent. Source/derivation/input
identity passes; retained realized-output verification remains dependent on the
parent's restore completion. No build or Git/index/flag/worktree mutation was
performed by this follow-up.

### Retained realized-output identity

After the lead's restore-complete release, the bounded read-only check passed:
`application-retained.status` is `0`; `application-retained.path` and persistent
out-link `/tmp/2026-11-13-archive-confirmation-regression-builds/candidate-package`
both resolve to the expected
`/nix/store/qxclq96999l3ccs39mj5vw0m5k8hwllx-dev-workspace-0.2.0`.
The registered output's deriver equals the previously proven
`/nix/store/kimsqz1nvqqk13mhf23yiardvn87jssx-dev-workspace-0.2.0.drv`.
Output NAR hash is `sha256-7mKze1jKA6leKkKQiCOCm8aoBR5B+sCswPGvhmsyH+w=`;
NAR size is 30,328,872 bytes. No remaining H provenance dependency or mismatch
was found. Deployment and integration evidence remains lead-owned.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-13-archive-confirmation-regression/>.
