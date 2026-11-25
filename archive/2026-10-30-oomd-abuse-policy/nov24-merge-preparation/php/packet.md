# vpsAdmin merge preparation

Frozen clean nonmounted candidate: **81e930b25fa3252d7e849aff4819e663cec37b07**,
tree **a68c6ce1a8307a39aa02b15a6e7c1fb61c2933d0**, branch
`2026-11-24-incident-admin-merge-prep` in `vpsadmin-nov24-ux`.
It contains exactly two feature purposes on fresh master
`95860bc2432844b243741532d165b79e5b973488`:

1. API `3a89945f4f772f1d474a3a6e8a2ec9c9a97d77b7`.
2. PHP UI `81e930b25fa3252d7e849aff4819e663cec37b07`.

Both replayed without conflict. [Range-diff](range-diff.txt) marks both `=`.
The two ordered patches and complete feature binary diff are byte-equal to
`4062..669fb9`; original authors, committer identities/dates and messages remain.
[Proof](proof.json), [old history](old-history.txt), [new history](new-history.txt),
[old feature diff](old-feature.diff) and [new feature diff](new-feature.diff)
bind the exact ranges. The complete diff SHA256 remains
`cad5e723a27804aec737c2c8ee99948ab2bbc2429ca73b329e7a5e6788bd8594`.

The successor differs from669fb9 only by the upstream twelve package lock/gemset
paths, byte-equal to the [baseline diff](baseline.diff). API JWT changes3.3.0→3.3.1;
client/download-mounter/libnodectld/nodectl/nodectld JSON changes3.1.0→3.2.0.
[Exact paths](baseline-paths.txt) and [paired dependency source checks](dependency-source-check.json)
record six matching lock/gemset versions and source hashes. All six literal local
Nix expressions evaluated successfully without realization, download or regeneration.
**Execution with these new packaged gem versions remains unverified.** The normal
hooks use the admitted resident component environment; their pass does not certify
the changed Nix gemsets. Old Ruby/API CI and runtime evidence retains its actual
effective bundle/input scope.

Full WebUI tree `38e14f49d304c61f3d818b10c74aa2828d45cdc2` equals deployeda25b,
including all Git file modes. API, tools, tests and plugins trees equal669fb9.
No HaveAPI declaration, PHP/Composer input, exporter, fixture, schema or migration
changed. Consumed migration20261030180000 remains blob
`ff9dd726f935aabef487ad7b9b8b047756eeefcc`, SHA256
`2eec970fb3620ad25f3ac01c06a9eae61af2d208f88184e995c74b8ad2ba2c1e`;
obsolete20261115120000 stays absent. Prior consumed/deployed lineage and source
review are retained in the [accepted history packet](../../nov24-history-consolidation/php/packet.md)
and [independent history review](../../nov24-history-consolidation/review.md).
No earlier purpose, integrated base or consumed migration was rewritten.

Normal API hooks passed in68.221s; normal PHP hooks passed in70.061s. Retained API
message warnings remain within the repository80column rule. Both source commands,
fresh installed-policy Luna/low utilities and all seven utility command items are
terminal0 with turn completion. Ordinary0022umask applied to every Git mutation.
No app/DB/API/export/browser/build campaign ran. Architect0's bounded dependency
brief calls for exact source/patch and paired lock/gemset checks, without new
product checks or dependency regeneration.

[Original74c0 and corrected8846 raw exports](retained-export-inputs.json) are
preserved unchanged: schema SHA7e2a529787c06944f1ad0cdf3369edd8b4650d79826f3bbda9101af2dfb67628;
tooling lock SHA2e9a124eff7b80d6fd57cd0f03cb2809847c67cc7f1af6364911c3622d7242a0.
Their raw provenance keeps its original source revision. Successor API declarations,
exporter/fixture/plugin/config sources and tooling input declarations are exact;
upstream packaged JWT is separate from the locked exporter toolchain. This supports
the precise no-contract-change freshness rationale without relabeling an old raw
export as a new run. There is no local exporter tooling lock in this preparation
checkout; no install or export was needed or attempted. SDK release/adoption and
final-head check disposition remain separately owned by root.

Canonical live-mounted `vpsadmin` stays clean at669fb9/treec833. Inspection used
`GIT_OPTIONAL_LOCKS=0`; actual index bytes matched before/after. No canonical file,
mode, index or ref mutation occurred. [Frozen canonical proof](canonical-frozen.json)
and [final remote read](remote-final.txt) record canonical/public feature669fb9,
public UXa25b and master95860. Publica25b and all prior review/deployed refs remain;
create-only local `2026-11-24-merge-prep-preserved-669fb9` also retains the former
feature. No successor publication occurred. Old-head CI45448900148/45448900123
was not awaited or rechecked and is not candidate81e930 evidence.

## Proposed later source selection, requiring root release

The final tree differs from669fb9, so a metadata-only ref move alone is insufficient.
After root accepts the final candidate and explicitly releases its canonical
source/publication window, the narrow recipe is:

- Recheck master95860, remote feature669fb9, old publica25b, candidate head/clean
  index and canonical clean669fb9; stop on any drift.
- Under ordinary0022umask, apply only the saved exact twelve-path
  `final-vs-669.diff` with ordinary `git apply --index` in canonical. Verify the
  resulting logical index tree is a68c6ce1 and no unstaged changes exist.
- Update only the canonical feature ref with expected-old669fb9 to81e930;
  prove clean head/index/tree, exact twelve package changes, and untouched WebUI
  content/modes. Never checkout/replay intermediate commits or use reset/clean/stash.
- Publish from the nonmounted worktree with a fresh explicit669fb9 lease and exact
  SSH/default/publica25b readback, then capture comparison and finite CI inventory.

This is proposed, **not executed**. It changes only package inputs, while mounted
PHP remains byte/mode identical and the already deployed API store artifact stays
immutable. It performs no build, service update, activation or default integration.
Root can instead publish the nonmounted candidate on its own branch while retaining
canonical source until a later source window; no registration was changed here.

All owned effects are joined; source/index/Git preparation windows and capacity
return to root. Final source is frozen. Root owns acceptance, affected review,
publication timing and any later integration approval. No product documentation
edit is useful because only the baseline and commit parentage changed. The session
and existing runtime remain open and untouched.

[Receipt](receipt.json) · [Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-30-oomd-abuse-policy/)
