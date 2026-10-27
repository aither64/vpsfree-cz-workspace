# Naming-high workspace package

Source and ordinary profile build passed. No live selection or activation was performed by this package.

- Final workspace: `61cd6566f269101acb6a5469b9e803546c5bf5b3`, tree `c15bc3d8df5763d5342bfd09a9ee70fc347ff857`, base `433b3b61f6cbad336c3a7b8ce1d010f5b7f1e5f1`.
- Matched clean configuration: `843be64072f04e6352447980a26dbf68bb0666e0`; existing deployment checker passed once.
- Runtime: `b44fb1a86af8ba2706a9d722b151c096ac3ef827`, source `/nix/store/f9a2xjlviyvw12a64mq4q0l1lscwa5y8-source`, actual NAR `sha256-kcNP0dJAp/j8kCbzPz7NNbT5z4YrvL5MG27M1I9wuqA=` matches the generated lock.

## History and publication

Old deployed range `367abb7f9..af6d9c133`; final range `433b3b61f..61cd6566f`. Ordinary range-diff pairs one logical two-file pin, with only the runtime target/NAR/time/URL and explanatory commit message changed. The three intervening shared-master commits contain tracking records only. No conflicts or migrations. Final history retains one pin stream; prior deployed content is preserved by explicit feature refs and output roots, not redundant intermediate pin commits.

The generated lock preserves its full node set, root/version, every input/follows edge, extension `767dfd587`, siblings, client `255f0b4f`, llm-agents `ea188d2f` and transitive nixpkgs `f20cd90e`. Full graphs are the committed base and final `flake.lock` files. Semantic checks and `git diff --check` passed. No hook framework is declared; the ordinary commit did not bypass hooks.

SSH publication used exact old feature lease `af6d9c133726c49332e99239b624f7646dab7d68`; push exited 0 and fresh remote proof showed final `61cd6566f` with default `051c8b769` unchanged. Deployed `af6d9c133` is retained at `2026-10-26-codex-upgrade-naming-deployed-before-naming-high`; all earlier refs, roots and failure evidence remain intact.

## Actual build and output

`nix build --out-link /home/aither/workspace/ai/vpsfree.cz/work/2026-10-26-codex-upgrade-naming/workspace-profile-naming-b44 --print-out-paths .#packages.x86_64-linux.default`

Original parent-fallback handle `59827`: exit 0, 656 seconds. No fresh watcher was callable; the monitor skill's visible parent fallback retained this original operation. Logs: `profile-naming-b44-build.log` and full `profile-naming-b44-package.log`.

- Output: `/nix/store/yi4hlb3s8lmm8w2bv34z35yhy6fmqk29-dev-workspace-0.2.0`.
- Producer: `/nix/store/mxjsrcc523ir5kswgh7np50a42xsw8cg-dev-workspace-0.2.0.drv`.
- Output NAR: `sha256-6GKg2abbRtP5W2zGi6T+dTQvrjFcNPPLV8ReOzl+Ycw=`.
- Normal checkPhase passed in 3m23s, including Go and browser groups 17/75/14/19 with zero failures/skips.
- Exact committed `git+file` evaluation at final `61cd6566f` returned the identical actual producer. The original sparse Git metadata warning is retained; this establishes committed application computation equivalence without a rebuild or index investigation.
- Actual native assembly is the same immutable `/nix/store/5rm5bizqzrc1sjlpbdnwps2cf16dxys0-codex-package-0.164.0` as deployed `7pa7…`. Native and Luna catalog bytes compare equal, reusing recorded native SHA256 `d2af1cd0ea4187d413c237e80204e94ffcd5c7d8142840a662156b89750f54ae` and catalog `049042aaadcf2f19722fa1e893f926d2bdbd4d0ff092d80704ff4256e2a45fb1`.
- Full runtime contract, full team catalog, client source and protocol validator compare byte-equal to deployed `7pa7…`; live-switch/reporting policy 1 and native capacity 9 remain unchanged. Static comparison is not a live launch-marker read.
- Vendor hash remains `sha256-r8pfbA22N3RNLZZDcbYNcpgPeU3fzSG+3Zvz+r4/TrQ=`; existing proof reused, no forced rebuild.

All original build and assessment commands settled successfully; no watcher or uncertain operation remains. Owner1 is released for its already-authorized system deployment. Lead owns the later application switch. No CI wait, browser/VM/native/provider/recovery campaign, naming inference, CPU action, merge, release, lifecycle change or cleanup was performed.
