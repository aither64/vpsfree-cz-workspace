# Final activation composition and refresh review

User explicitly "okay, so proceed with activation & merge" after five repository
merges + aitherdev user-profile application activation explanation. D3 accepted
in design.md. Retained reviewer0 Sol/xhigh/read_only, same independent reviewer.
Read installed mandatory-review skill and general + architecture/repetition +
scope + risk references. Risk high for package selection/retained host contracts,
though upstream generic/site delta remains docs/skills only. No full system
activation/runtime redesign or lifecycle action in scope.

Original final review.md and review-packet.md retain the five reviewed ranges,
source inventories, migration/history conclusions and passing docs/CI evidence.
New intended source changes are complete/committed/quick-checked, clean/published;
long package build has not run. Inspect whole final series and dependency graph,
not only latest pins. No source edits by reviewer, no nested agents or tests.

## Complete final ranges

Worktree root /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-08-documentation-governance-review/.

| Repository target | Final base | Final head / complete owned commits |
| --- | --- | --- |
| dev-workspace master | d2cb9975a88079d79f361c5b4c65836ba0835821 | 6587c4c1cedabee95bcc52f4667e7d33e3a82859 (original one commit, unchanged, now integrated) |
| vpsfree-dev-workspace master | f8da821e3c76e26e73aa9d89a712eab0e0faa319 | 0c7168f352f6d4f11c46368e702b9356d81012c6 (original one commit, unchanged, now integrated) |
| workspace master | 01c3a7bbd2893ae64e97fee52cd2cc16d98df29c | adc35b7fcb3888c1678638fb1d8bea05f4e213d2 docs + 894c1ebd8bbfaf67e96f927c16956a2f79ea7523 inputs: select reviewed documentation guidance |
| configuration master | 9e25b996034f8e05f4858dc5ec1f1246a516b109 | f3149765d2db49c5556983df2954cd368a7b0800 docs + 8d040ea216e1524c329abf6fa46691f8c7cdd6ac generated inputs: set devWorkspace to 6587c4c1 |
| vpsadminos staging | 640445ef40cb0daf75ff3b39a79a673f6721b53e | 14e1c7327d493b212e4c17d3cca053d23883cbba docs (rebased over scheduled unstable-nixpkgs lock update) |

Workspace remote master1134fb3c still predates inherited shared-master archive
4af26b17,992ce14f and this session's tracking checkpoint01c3a7bbd. Preserve all
inherited history; inspect metadata/stats only for peer archives, no contents.
Shared master must fast-forward feature including tracking. Feature workspace
has no work/archive checkout; tracking remains lead-owned in shared root.

## Refreshed docs equivalence and history

- Workspace old992ce14f..1a3a10d9 -> new01c3a7bbd..adc35b7f:
  range-diff '=', patch3bd014de698b74825b4edef693439cd8c905cf79.
- OS old4bfed8ba..6154dbcd -> new640445ef..14e1c732:
  range-diff '=', complete diff bytes equal SHA256
  738a7cf537b99948314e349180473787c370cd45c914af938bb0801a6d46208c,
  patcha069d417ba3f50ddcc5627727626c864b29adb53. Owner and lead independently proved.
- Config original docs unchanged exactly; extension/generic unchanged exactly.
- New workspace pin streams generic/site each have one final selection commit;
  config devWorkspace stream one generated commit. No superseded updates or
  migrations, no deployed/external consumption of new composition yet. Separate
  docs and generated pins retained intentionally for review/revert clarity.
Require explicit independent whole-history/migration/update-stream conclusion.

## New graph and deployment contract

Workspace only flake.nix+flake.lock after docs: direct extension URL0c7168f3,
nested runtime override6587c4c1 retained. Root nixpkgs follows extension/nixpkgs.
35 nodes: only generic+site locked/original identities changed; all sibling nodes,
input edges and follows preserved. Complete graph /tmp/p5-final-input-graph.json,
SHA2562f69dc4ea19e9fe943381f7cc48ebf6e9b0dcf87bd7e6f7570a78ac783b88f35;
independently inspect actual final vs base locks.
Config channel dev-workspace/roledevWorkspace set through documented confctl
command; only3 locked values changed (rev,lastModified,NAR). 64 nodes; normalized
graph outside sole node SHA2565277a5eb410b169feddec46b7a447c78c6c0c6f4d1c114ac87aeab6ecc1726b3.
Generated commit message/changelog kept unchanged; local width exemption used.

Final sources: generic6587c4c1
/nix/store/pfnyfqh3z37g4dpqq3pw04qhdgg98d55-source,
NARsha256-bgwQahEcT3ekDfMjmlDsgwhCdiKk+X6DDappoYKzknY=;
site0c7168f3 /nix/store/i251i1vmsy8q4i5qssn7ivl4s43ksbpx-source,
NARsha256-hhWrvLJFedS3B6Yd55gPcUQmyhChYMvxABg7yVRWGLw=;
Codex-web unchangeddd90fb4308ba85617ee2a4267cc835aa9a4f11ce
/nix/store/xhjvnra2pf6f65yjlplgqh56yxhxnsys-source,
NARsha256-JcQLZ4GPc5fOy2r4/iM4nhzqVTPWgZb6sNhJFd2nX+g=.
Committed workspace source /nix/store/ib36aa4c1knakjr4xzdyp3yvh4vni84d-source;
sparse tracking exclusion causes Nix dirty warning but Git feature status empty.

Selected profile baseline8p7fs26ja6flmlgc886ddfgpprdkhfjy-dev-workspace-0.2.0
(generation228) contains genericd2cb9975/sitef8da821e, verified NAR provenance by
D3; no regression to older unrelated source. Candidate composition changes only
upstream2 generic docs +2 site review files; generic flake.nix,lock,nix tree and
libexec tree exactly unchanged. Config host modules/options, Codex builder,
lifecycle/cluster/maintenance/claim/native contracts and dependencies unchanged.
Running systemxwldgxzayy9113ljd57ib70vwrbksgp0-nixos-system-aitherdev-26.05.20261026.718f670
will stay selected. No concrete new host/substrate requirement found. Retain all
profile transition/admission/recovery checks; don't waive unexpected refusals.

## Quick checks and prepared execution

P5: whitespace, flake parse, 35-node exact-delta graph assertion; actual
bin/check-dev-workspace-deployment --workspace-root <workspace-feature>
--configuration-root <config-feature> passed hostname + exactgeneric6587c4c1.
test/deployment_contract_test.rb4/19 and agent_instructions_test.rb10/217 pass in
pinned Ruby shell. P8: channel/lock64-node delta/NAR, original docs preservation,
required hooks passed; exact published config8d040ea2. Unchanged original review
and checks remain available. OS refreshed hook diff check passed, expected
RSpec CI auto-run42604952865 may need exact terminal collection before merge.

All source owners report clean/published complete heads. No candidate package
build yet. Optional candidate drv eval was interrupted during unchanged source
unpack (session22023 terminal exit1), no builds or uncertain runner. Post-review
watcher will realize package+selected local composition checks, retain exact
candidate drv, complete input graph/closure, compare installed skills/catalog/
cluster/native descriptors and baseline. This is prerequisite to activation.
No browser/VM/kernel/ZFS rerun for unchanged code; original runtime/site CI passed
exact reviewed upstream heads. New package still requires its own build evidence.

Lead integrated generic/site exact heads under separate claims0071/0070, fresh
remote proof and release verified; no claims currently held. Other three merge
claims only after final source/check preparation; machine reserved near ordinary
workspace-host switch after complete integrated lineage. No reboot/system switch.
Forward-only original recovery applies; verify profile/system/skills/portal/
conversation/native continuity and all effects before prompt machine release.

## Reviewer deliverable

Write activation-review.md in this session evidence directory only. Report exact
ranges, actual retained settings, ordered findings by lane/severity, whole-series
and pin-stream/migration conclusions, graph/source/host-profile boundary and
patch-equivalence conclusion, applicable remaining check limits. A narrow fix
can be directly verified; new design/contract change requires affected rerun.
No source edits or nested reviewer. Review remains independent; lead owns packet
acceptance, claim/activation scope and rollout receipt.
