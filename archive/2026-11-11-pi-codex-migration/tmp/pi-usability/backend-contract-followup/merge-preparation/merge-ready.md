# Final merge preparation

User approval covers the four reviewed projects into master. Preparation only;
lead owns each short claim, fresh check, FF, SSH push, remote proof and release.
All preparation handles are joined. No default merge/push, claim, deployment,
source check/build or lifecycle action was run by implementer0.

| Project / alias | Exact final head | Tree | Fresh prepared base |
| --- | --- | --- | --- |
| C / codex-web-transcript-display-key | 3209aa7bf93e2c7067b07494d1b254741812d714 | 6796425ac255f2223272c0ef1c34c8591222777c | 91a17d00a737d59a91b5e7bb420aa89e7ec52d93 |
| R / dev-workspace-pi-lifecycle-recovery | 0abe5fe48955b1bcdc8cc368fcb27e11e0676f70 | adc03f21755dba2a91c102852f293579586b72d5 | 9241a342a6ef4ca69148594e98cce7ddcfb459a6 |
| W / workspace | f6bcb4c4d7c4d3275657734bebc28e763e11a52a | 4e5413f05c031409ee58d1ade01477f9f91fa545 | shared0962457516392d6bb0ccb114b34cf59b8b8f2f94 |
| H / vpsfree-cz-configuration-pi-lifecycle-recovery | 58cbe758efb9b38c8b0a423bb6fa89ddcc418d62 | 0050025e1799fe5242ceba6a9bb9c96eb1c2ae01 | d06f9a4ba4217d9b6fd065ffa41d6c1c5ca35853 |

All paths below are relative to
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-11-pi-codex-migration/`.
C and R readiness was released independently; main reports C integrated and owns
R integration. Do not repeat their completed operations.

| Project | Clean merge target | Final source worktree | Canonical SSH origin |
| --- | --- | --- | --- |
| C | codex-web-merge-target-20261122 | codex-web-transcript-display-key | git@github.com:aither64/codex-web.git |
| R | dev-workspace-merge-target-20261122 | dev-workspace-pi-lifecycle-recovery | git@github.com:aither64/dev-workspace.git |
| W | shared workspace master only | workspace-final-integration; registered workspace also exact final | git@github.com:aither64/vpsfree-cz-workspace.git |
| H | vpsfree-cz-configuration-merge-target-20261122 | configuration-final-integration; registered vpsfree-cz-configuration-pi-lifecycle-recovery also exact final | git@github.com:vpsfreecz/vpsfree-cz-configuration.git |

C/R/W declare no relevant hook framework or active merge/push hooks. H has active
Overcommit wrappers. Use its target's own `nix develop --no-write-lock-file
--command git merge --ff-only 58cbe758efb9b38c8b0a423bb6fa89ddcc418d62`,
then its same Nix environment for ordinary SSH `git push ORIGIN
HEAD:refs/heads/master`. Hooks and generated messages remain enabled. PreCommit
Nixfmt passed the generated pin commit; generated message width warnings were
retained under the documented exemption. Target d06 is clean and detached.
Registered H's old local gem cache is unsuitable for its new Ruby shell; the
checkout hook was successfully replayed there using the already prepared final
Nix environment's absolute gem paths. Use the fresh target for main's merge.
See H-final-environment-post-checkout.log and H-readiness.json.

W has six purposes, refreshed onto exact shared096. Remote9610 is an ancestor of
shared096, not the reverse. The earlier c21 readiness statement was incorrect
and is retained explicitly superseded. All ten local tracking commits survive.
Old fcbed..deployedcc626 and shared096..f6b have byte-identical whole full-index
binary patches, identical ordered stable patch IDs and six `=` range-diff rows.
Old/final source-head differences are tracking only. Evidence:
W-readiness.json, W-shared-range-diff.txt, W-shared-final.patch. Shared master and
its index/files were untouched by preparation. Main takes its repository claim,
then nonwaiting dev-session-tracking.lock, rechecks and FF merges f6b from shared
master, preserving unrelated files/index entries.

H retains three purposes. Its generated first commit uses the normal owning
`confctl inputs channel set --commit dev-workspace devWorkspace
0abe5fe48955b1bcdc8cc368fcb27e11e0676f70` in the declared Nix shell. Every
non-devWorkspace root dependency graph equals fresh d06; the devWorkspace graph
exactly equals reviewed42c. Host configuration and both docs equal42c byte for
byte, and both host/docs commits have `=` range-diff rows. The generated pin row
changes only for upstream lock context and its correct9241..0abe generated log.
See H-semantic-lock.json, H-range-diff.txt, H-final.patch and
H-channel-generation.log. All upstream dependencies, including confctl and
nixpkgs changes, survive. This is final configuration SOURCE; actual deployed
H9acd/systemc77/helperrpd/native0.169 is unchanged. H599/base8b29/native0.170
remains preserved and unactivated. No new physical-output equivalence or
activation is claimed for the refreshed upstream configuration baseline.

Both new final feature refs were pushed over canonical SSH with absent leases
and fetched back with exact head/tree equality:

- W: refs/heads/2026-11-22-pi-codex-migration-workspace-shared-master-integration
- H: refs/heads/2026-11-22-pi-codex-migration-configuration-final-integration

Original published branches were not force-pushed. Authorized empty-range
rebases refreshed the clean registered local branches only. Distinct retained
provenance refs preserve their previous exact heads:

- W95442f: refs/heads/2026-11-22-pi-codex-migration-preserved-workspace95442f
- H42c: refs/heads/2026-11-22-pi-codex-migration-preserved-configuration42c89512

All earlier deployed/direct/final refs, including cc626/c21 and H599, remain.
Manifest identities and initial_base values were unchanged. Exact supported
capture now passes for W shared096..f6b and H d06..58c through the existing
registered aliases: W-final-comparison.json and H-final-comparison.json. The
historical W alias limitation is resolved for this final integration; original
refusal/mismatch evidence is retained. Exact C91a..3209 and R9241..0abe saved
comparisons already exist in the portal store, as reported. Reuse accepted final
review5112, full158 R history/migration conclusion, existing C/W/H final review,
CI and deployment evidence; no new source test/build/review campaign was run.
No source documentation change is useful for these mechanical history refreshes.

No preparation blocker remains. Main owns fresh default checks, integration and
machine release. Session remains open.

https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-11-pi-codex-migration/
