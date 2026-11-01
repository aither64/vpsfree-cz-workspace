# Corrected provider: final acceptance and writer handoff

Published **d632caf4b6d617ee8495b8132332fc56a82bdfe5**, tree **884bc3eb0e9d758cc1025e1a12f5130eaa0c84d9**, passed both required final-source checks. The branch is `2026-10-24-vpsadmin-haveapi-upgrade-services-os` in `git@github.com:vpsfreecz/dev-workspace.git`. Its sole parent is selected default `767dfd587e346168e1443e65ccdb67ce748f3fe3`.

| Original handle95771 phase | Actual result | Duration |
| --- | --- | --- |
| `nix flake check --print-build-logs` | exit0; full48 commands:48 tests/661 assertions/0 failures/errors/skips |2653.562s |
| `nix run .#devcluster-check` | exit0; real services projection, all8 configuration variants, WebUI acceptance/refusal and both runners built/loaded |513.856s |

All21 ordinary extension Ruby suites completed:375 tests/3510 assertions/0 failures/0 errors/1 skip. The sole inherited skip is `migration_test.rb:86`, whose supplementary-group case skips when the test process has no supplementary group. That file is unchanged. The required full48 has no skips. Quick suites were not repeated.

The [compact bound receipt](postreview-receipt.json) records each actual check derivation/output, runner derivation/output/executable hash, source/input graph, root and process effect. [Input graph](postreview-input-graph.json) binds all34 locked nodes to the exact packaged lock. [Package binding](postreview-package-binding.json) binds provider, maintenance, flake and README bytes; only the ordinary provider shebang differs. The rooted app embeds the exact tracked smoke script. Source `/nix/store/x7m62a1r0gbf6rzl3xnysqmhsllrlvmg-source`, app `/nix/store/72nw2qb8qj7fbdbzlcnqndlakr7g5q3n-devcluster-check` and tools `/nix/store/3g3gbnk19iv49kvcwk4nwzwg74zm9vqg-vpsfree-dev-workspace-tools-0.1.0` are verification outputs, not the selected installed runtime or deployed cluster.

Thirteen new `final-d632-check-*` roots retain source, app, nine passed check outputs and both runners. The app runtime closure has201 paths; each runner closure has38. The independent source root is retained because the runtime closure alone does not retain the full source/build graph. Older3fdec roots remain unchanged. Raw logs/results/derivations remain private0700/0600 under `/tmp/e0os-d632-checks-a8rcqi1j`; only sanitized facts and hash references are included here.

[Publication proof](publication/receipt.json) records ordinary recovery-first publication, the explicit lease from3fdec to finald632, independent canonical SSH readback and unchanged default767. Remote/local same-selector recovery retains3fdec, and older applied-pin recovery retainsacc. The [accepted review](review-acceptance.md) covers the narrow two-test change and complete history; unchanged implementation/docs retain prior all-four-lane HIGH review. The complete767..d632 series is one coherent commit/seven paths;111 entries outside the two-test delta equal3fdec, and105 entries outside the final scope equal767. **NO MIGRATIONS.** The original failed3fdec full48/645/2F attempt remains preserved in the [review inventory](inventory.json), with no relabeling.

All seven recorded driver/phase identities are gone; original95771 completed0, both check phases were reaped, and final source is clean at exactd632/tree884bc. Resource bounds remained CPU60–63/nice5/Nix1job2cores. The retained840-unavailable owner-monitor fallback was used without bootstrapping a substitute. No unexpected local kernel build, capacity failure, duplicate verification run, live cluster query/update, activation, default integration, CI, export retarget, storage collection/deletion or lifecycle action occurred.

**Source/Git writer ownership is released.** E1 and lead received actual0/0 acceptance before receipt assembly; E1 may bind the exact final published SHA for its consumer package. Parent/E1 own later consumer acceptance and approved aitherdev workspace deployment. This provider branch is ready, awaiting merge approval; no integration was performed. Keep the session, all roots, refs and recovery evidence open and intact.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-vpsadmin-haveapi-upgrade/
