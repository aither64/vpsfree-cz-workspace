# Final C7 source and CI handoff

All seven source worktrees remain clean at the exact independently reviewed and
published heads. HEAD, tree, complete base-to-head commit series, lock identity
and full-index binary diff match reviewed inventory
`821181a5dad2340b149f1013846cf1430c8373bec8258c881da49caf6bc833ab` and completed review
`6bb7afca1cd0b1794fb97bb3f8bcd20453a6ed94ae346fc0d375d4a27d4e92dd`. Fresh canonical SSH reads show exact feature-head
equality and no target movement beyond accepted HaveAPI master1103/base7ac
divergence. No fetch, source/ref mutation, target chase or configuration/env/
authentication read was performed.

| Repository | Exact reviewed/published/source head | Full branch commits |
| --- | --- | --- |
| haveapi | `c7bfc1aa5af956b6057be8e623f9035c00ccb268` | 1 |
| terraform-provider-vpsadmin | `c3f20203a5ba6200d0ff6b77f500bff6473f2c11` | 1 |
| vpsadminos | `889f14e5f964c85eac0dbffdff96909a46ab35c6` | 1 |
| vpsf-status | `018b700f06cf216a125a70ac9bfedddaabf07b92` | 3 |
| vpsfree-irc-bot | `0a160463a4ee12ec5f6c45e38eaba11592787d9f` | 1 |
| vpsfree-cz-configuration | `5f0f4466adb175ed4fcac9b6d5c8909e87a1fec1` | 1 |
| vpsadminos-org-configuration | `ca96c95a1fee04793468785d8323a759615b2b4e` | 1 |

[Final combined receipt](verification/c7-git-cache-final-observation-2/final.json)
links the one [original observation](verification/c7-git-cache-final-observation-2/receipt.json)
and [full-index completion](verification/c7-git-cache-final-observation-2/full-index-comparison.json).
The initial diff comparison used abbreviated index object IDs, so its preserved
comparison flags were false. All other source comparisons already matched.
Seven immutable-commit diffs with the review's exact `--full-index` serialization
then matched byte-for-byte. Only that missing serialization was completed;
source/ref/status/CI observations were not repeated, and no test was rerun.
The original result is retained for provenance. History remains one adoption
per consumer, plus status's two independent unchanged fixes; no obsolete pins,
fixups or migrations remain.

## Final bounded CI snapshot

Every observed final-head run completed successfully, including the previously
pending status Integration run. No final-head failure required log/artifact
investigation. No waits, reruns, dispatches, cancellations or second CI poll
occurred; all prior snapshots remain preserved.

- haveapi servers/ruby RSpec: success; [40119250404](https://github.com/vpsfreecz/haveapi/actions/runs/40119250404).
- terraform-provider-vpsadmin Go Tests: success; [40119322279](https://github.com/vpsfreecz/terraform-provider-vpsadmin/actions/runs/40119322279).
- vpsadminos: no matching exact-head CI run observed.
- vpsf-status i18n health: success; [40119441601](https://github.com/vpsfreecz/vpsf-status/actions/runs/40119441601).
- vpsf-status Integration Tests: success; [40119441548](https://github.com/vpsfreecz/vpsf-status/actions/runs/40119441548).
- vpsfree-irc-bot RSpec: success; [40119496297](https://github.com/vpsfreecz/vpsfree-irc-bot/actions/runs/40119496297).
- vpsfree-cz-configuration: no matching exact-head CI run observed.
- vpsadminos-org-configuration: no matching exact-head CI run observed.

Absence of matching OS/configuration runs is explicit; those repositories are
not labeled CI-green by absence.

## Accepted runtime evidence and limits

Lead accepted six original selected paths plus the org-only successor in
[the selected-path receipt](verification/git-cache-selected.json). Org2 passed0
in about69s with195 child commands0, strict final clean/index/HEAD/lock and
unchanged warm-cache snapshot, equality/no generated commits. Its original
149-command postflight failure2 and `.bundle/config` evidence remain intact.
The successor added only the exact local `/.bundle/config` exclude before
snapshots. Complete launcher aggregate and child stdout/stderr are retained;
no repeat is needed for a redundant separate watcher log. Lead retained406
files and complete graphs. C did not inspect the active org2 operation or cache.

[The real local Git race](verification/git-cache-race.json) passed59 commands0
in10.149s. No duplicate runtime/cache operation was launched or read by C.
Lead reports no operation remains.

[Completed-path facts](package-c7-git-cache-completed-path-facts.json) retain:
HaveAPI equality skipped the existing conditional inline `nix flake check` and
commit arm; status created the canonical nixpkgs mirror once; IRC and later
paths reused the same directory/device/inode. vpsFree's llm-agents update arm
ran and verified its version. Lead recorded final shared-cache size5879009280
bytes, status updater2328.24s and IRC warm updater12.58s; these are complete
command timings, not isolated Git-transfer benchmarks. Org2 reused that cache
and does not relabel the original cold result.

These are seven selected guarded updater/commit/final-lock paths, caller shells
and cache/race checks, not seven full new workflow reruns. Unchanged dependency
refresh/application build stages and TF8VM remain omitted under the accepted
brief; R's full workflow/VM receipts remain historical at their exact inputs.
Actual GitHub Actions cache upload/restore was not exercised by these local
runs. Provider822c's published exact exported203 passed under lead's watcher;
source/package/check graphs and owned links are retained. All production source,
review, original attempts and receipts remain unchanged. This session remains
active/open/unmerged; integration, deployment and cleanup were not authorized.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-flake-update-downgrade-guard-replacement/)
