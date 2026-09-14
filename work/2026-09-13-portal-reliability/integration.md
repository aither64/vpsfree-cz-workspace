# Default-branch integration — September 14

The user explicitly requested merging all affected repositories into their
default branches. All five use `master`. Four project branches were already
descendants of freshly fetched origin/master. The workspace feature was rebased
from 242af5c to 9638606 over shared master bf177af. Both functional patches are
identical according to git range-diff; AGENTS.md, flake.nix and flake.lock have no
content difference between the reviewed and rebased heads. Existing four-lane
review remains applicable; no new implementation or dependency change was made.

## Final heads and captured comparisons

| Project | Saved base | Final feature head |
| --- | --- | --- |
| codex-web | aec4ea2ff13a053e340a2a47616d6fbc89aeeac1 | 6335da93acdcc82cc26200d2fbc7f479655aa7c3 |
| dev-workspace | f41d4220dd1d5ade08ba3bb28f964e9570a11ed9 | e9ed544bf66ba8be07b4fca27aede6e6fd1bfe0a |
| vpsfree-dev-workspace | 9f3142248f6e40d602115aa0fad66701595ef232 | 916223fce1c5b7b78578ca8a16aaaa472c68b08c |
| vpsfree-cz-configuration | 3d9ffa45c7e0388c96434fd3a6127d0a54c0b9ea | 249bed1ee28e69a907edd09ea97a1144dbcdefeb |
| workspace | 47bcd603fbd35f999369ddbcfa9c64a74f094376 | 9638606e9a6070def6604eac07dfe9c0d300e64f |

`dev-session worktree capture-comparison` saved every final pair before default
integration. The workspace pair starts at the remote default before pushing; it
includes the existing committed coordination records as well as the two feature
commits. Its local fast-forward started at bf177af.

Independent projects use fresh detached integration worktrees created from
origin/master, `git merge --ff-only`, validation and normal HEAD:master pushes.
The workspace used the shared master checkout with an empty index and preserved
all unrelated dirty and untracked files. Feature branches and feature worktrees
remain available.

## Integration verification

- codex-web: packaged flake checks passed, including 24 browser contracts.
- dev-workspace: full flake checks passed, including the host-module activation,
  certificate renewal and rollback VM test (123.84 seconds). Packaged Ruby tests
  have the same documented sandbox skips; no failures or errors.
- workspace: deployment contract passed (3 tests, 14 assertions). The resulting
  package is exactly the deployed mk77xsg4qrk075smiyazc2vqb18p5b2y package.
- Organization: full flake checks passed, including both packaged runtime variants,
  provider shutdown/status tests and the organization tool suite.
- Configuration: `confctl build --yes cz.vpsfree/machines/aitherdev` passed, producing
  generation 2026-09-14--09-57-37 and the exact deployed system
  rpi2qkdsi5s2x7g0lslljca62a5q3359. No redeployment is needed.

Configuration checkout initially triggered Overcommit outside its Nix shell and
could not load the pinned gems. The worktree was created successfully; entering
its Nix shell installed the expected gems and the fast-forward completed with
hooks active. The short confctl selector `aitherdev` matches no machines; use the
exact inventory path `cz.vpsfree/machines/aitherdev`. The corrected build passed.

## Default-branch CI

- codex-web [Check 34820231658](https://github.com/aither64/codex-web/actions/runs/34820231658): passed.
- Runtime [Check 34820446172](https://github.com/aither64/dev-workspace/actions/runs/34820446172): fast and host jobs passed.
- Organization [Check 34820482649](https://github.com/vpsfreecz/dev-workspace/actions/runs/34820482649): passed, including packaged provider smoke tests.
- Workspace has no GitHub workflow; configuration only has a scheduled input
  update workflow. Their integration checks run locally.

## Merge proof and cleanup

All five final feature heads equal their remote feature refs and are ancestors of
the fetched remote master heads. At verification, each master equalled its final
feature head. `merge-verification.json` records the exact refs and portal responses.
All five post-merge repository histories show the saved exact comparison without
warnings or summary errors. The four temporary integration worktrees and their
generated configuration helpers have been removed with non-force cleanup. The
original feature worktrees are clean; feature refs and the open session remain.

`merge-ci.json` records all three successful default-branch runs and their exact
heads. No superseded active workflows remained. The initiative is complete and
remains open under work/; no archival or session shutdown was requested.
