# C forward refresh — 2026-10-24

Published and frozen after owner quick checks:

| Repository | Exact final head | Effective base |
| --- | --- | --- |
| Workspace | `c8709037fa5bd2920051e7ce690f037ed31b3078` | `ceca96a4932a17512ab96c741f5396136747471a` |
| Configuration | `de4d60d95dee0934a266e1f2fe80a48eeade3475` | `25258cd3f483f0116dbab35c7acf89b16eff4bbc` |

Both select runtime `556a6e51b141fa419d620ad0d4ccd629fd2be6f5` and client
`6e469863a69c7d35941ca2e15de9514223b58f4f`. Extension
`767dfd587e346168e1443e65ccdb67ce748f3fe3`, native inputs, sibling nodes,
node identities/edges and follows are preserved against current bases. Each
consumer has one authored final pin stream; obsolete pins are absent from the
new series. Config retains confctl’s proper b3a6 predecessor, three-commit
changelog and normal hooks. No product prose changed and no migrations exist.

- [Inventory and exact SSH proof](inventory.json), including registered initial
  bases, complete authored series and inherited commit/path metadata.
- [Quick results](quick-checks.json) and [semantic graph proof](semantic-check.json).
- `*-final.diff`, `*-final-history.txt`, `*-own-range-diff.txt` and
  `*-old-to-new-source.diff` describe the final streams and original review ranges.
- [Prepared activation recipe](activation-recipe.md), unexecuted by implementer0.
- [Preserved old source/receipts](original-candidate/manifest.json). The prior
  reviewed/built c740/4383 candidate was not activated and is stale for deployment.
- [Preparation provenance](preparation.json). Selected immutable workspace
  source flake/lock match the effective current input graph; its own installed
  Git SHA remains unproved. No other-session record contents were copied.

Current baseline includes newer deployed failed-turn recovery and schema-1 retry
capabilities. The old-to-new configuration lock also inherits upstream
impermanence/vpsAdminWebUI/vpsAdminOS updates; the authored delta changes only
runtime/client nodes. Four workspace coordination/artifact ancestors above
remote default are retained and inventoried by metadata only.

Pending: lead-owned affected-lane independent review, exact-head long/native/
package verification, composed derivation/input proof, fresh builds and rollout.
No build, copy, activation, claim, default merge, CI wait/rerun or lifecycle action
was performed by this execution package. Old successful receipts do not certify
the refreshed source graph.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-20-workspace-session-naming/>.
