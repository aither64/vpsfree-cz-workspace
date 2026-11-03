# Private staging build result

PASS: native exact-five build at`0844881779d62d9a6a86d2bacd61d21565b33932`, parenthandle43854,
exit0 in154.13s. Status start1793717414.6602743, finish1793717568.7934775,
runningnull. Command:

```sh
nix develop --no-write-lock-file -c confctl build --yes 'cz.vpsfree/containers/{mx2,prg/int.mon1,prg/int.mon2,prg/int.alerts1,prg/int.alerts2}'
```

All five registered outputs and derivers match final native evaluation. Every
output configuration-info records exact clean084488; output inputs-info equals
its native generationJSON. Generation/input/toplevel symlinks agree. Complete
paths, NARs and generationJSON hashes are in`staging-built-systems.json`.

| Target | Output basename | Output NAR |
| --- | --- | --- |
| mx2 | `4pc5mic0rp9h5qb2lhgmdh2x8z50pqd2-nixos-system-mx2-26.05.20261026.718f670` | `sha256-dGOqT6fHxNlWSfrfMGRzPem0RqpuLSzHLoWJ/CG5cjg=` |
| int.mon1 | `8wyx524fsyyxpqid9ynrxrhrvn0kga65-nixos-system-mon1-26.05.20261026.718f670` | `sha256-oQ1ooAh0ACaVQffMArkc8Scb/PfCOQMLUkCERtUf4gc=` |
| int.mon2 | `085v7hqkq1nc2vc8inrynmyvxa8xk9md-nixos-system-mon2-26.05.20261026.718f670` | `sha256-hQi85+XqyLl1vy979Q48YxcNjeQYMoTxzWhdXDTvmdM=` |
| int.alerts1 | `6qn8kzpgmrs3syxpqiqyvxhn8gvki9wj-nixos-system-alerts1-26.05.20261026.718f670` | `sha256-77zcitIxq7Z3Zw3R0A656M/7Oyw/+4/d2T1Uwt4BLKE=` |
| int.alerts2 | `id1cj8xkg84wscfi30jb4ajdsp18bhxy-nixos-system-alerts2-26.05.20261026.718f670` | `sha256-v+22osqU0dmlDXdWA/41Y64WFmGJ9EpgDRKYsPJAGaM=` |

Current generation for every target is`2026-11-03--15-47-12`, predating the
parent run and consistent with the earlier watcher invocation. Pinned confctl`nix_flake.rb:134` finds existing generations by
toplevel+inputpaths and selects them; parent15-50 success reuses that identity.
It does not imply a new15-50 generation.

Source`/nix/store/vvbb8n2imsc3gssza91lszb5gss5mxyh-source` has exact084488 revision, clean metadata and
registered NAR`sha256-R2rH+/SVez0E8tLkdahFZwbZNkyccOVSpeBVNNLMhBQ=`, matching nativeGit metadata.
Source/current lockSHA256 both
`507e781c2fa52da5a389e6eab824efe68baa72b1727de0fc162ea0a5e6b4c098`.
Both role source paths have registered NARs matching locked nixpkgsStable718f670e
and vpsadminosOsStagingb45b27b4; generation/input-info bindings match. Complete
final input graph remains`staging-input-graph.json`.

The original watcher did start; a mistaken readiness interpretation led to a
duplicate parent local invocation. Do not interpret the status monitor prose
as proof the watcher never executed. Authoritative parent status records exit0.
Raw`staging-build.log` is preserved unchanged:10983bytes,9781NULbytes,
SHA256`5f1f0b30721dd8dd5544b60e78d0dd7ada9034f6c62c9fee781db86bfa4232e7`.
It contains mixed writes/file-offset gaps and is not a complete single-run log.
The referenced separate native parent log15-50-19 is currently absent; no
replacement log was fabricated. No cleanup was performed.

No new build, test, Git/source or remote operation was run for this receipt.
No process scan was needed to validate local output identity; completion uses
the lead-owned parent status. Candidate deployment is still pending admission;
the last observed remote system remains original98n9, not this built4pc5output.
