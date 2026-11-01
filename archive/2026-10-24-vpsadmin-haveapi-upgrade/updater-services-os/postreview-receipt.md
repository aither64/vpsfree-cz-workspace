# Services-only OS selection: postreview result

Exact published source **acc495827de81cce0fa7a7cf3f34e9f15c9516b1**, tree **c3fb82f170a9757d5c5e0928cc3381ba90233bdd**, is clean and unchanged from accepted reviewer0 native01a18ed0. One coherent commit above767dfd5, five paths, no repeated update stream, **NO MIGRATIONS**. [Publication proof](publication.json), [complete source/history review packet](review-packet.md).

| Operation | Actual result |
| --- | --- |
| Normal flake check | Exit0,2190.229s; all nine declared checks passed |
| Full command suite | 49 tests,646 assertions,zero failures/errors/skips |
| Extension aggregate | 21 suites,378 tests,3528 assertions,zero failures/errors,one migration skip |
| First installed-flake check | Exit1,417.683s; packaged source disappeared after five positive evaluations |
| Exact-app output retention | Exit0,4.242s; original derivation/output identities preserved |
| One installed-flake retry | Exit0,374.665s; both provider flakes and both runners passed |

The original availability failure and unknown collector/actor remain recorded. No source or assertion changed. The successful flake check was not repeated. The earlier connection-interrupted preliminary query had no required-check result; [reconciliation](postreview-original-reconciliation.json).

The smoke check covered bridge/local defaults and overrides for vpsAdmin and vpsAdminOS, enabled bridge WebUI, invalid metadata and enabled-local refusal, and building/loading both runners. It evaluated configuration derivations without realizing VM closures or starting VMs.

The normal package output is `/nix/store/as6yslflzg41s6ab2dzas2c4wy408pah-dev-workspace-0.2.0`. The smoke check used actual tools `/nix/store/zhhxbkqqvw0g7cy117b01x4z0npmwfny-vpsfree-dev-workspace-tools-0.1.0`: the maintenance helper matches source bytes; the provider script has only normal shebang substitution.

The exact check app `/nix/store/fqkz3b3rmn62y7h4pdggd7d2a6lxpvc7-devcluster-check` is registered under `/tmp/e0os.24tn_hwj/roots/postreview-devcluster-check`, retaining its201-path runtime closure. Source provenance is separately bound through `/nix/store/9p418mkd3l0qx798fmhyi3247iwnrq9l-source` and [all34 locked input nodes](postreview-input-graph.json); the source is present but is not a runtime-closure member. No extra source root was inferred.

Actual runners:
- `/nix/store/r0c94v4q8cpzpppkwfim5ccglq54jvhx-vpsadmin-devcluster-runner` (drv`fs6jlw28lpzxaxgwg6a4x2ps1hd1sr9s`)
- `/nix/store/ssg9nz3vzz411imbgp47bf16jj6kg5vr-vpsadminos-devcluster-runner` (drv`hf1vgczg419h1p69w255v2bmswiybbfi`)

[Full compact receipt](postreview-final.json) binds the nine check derivations/outputs/NAR facts, source/input graph, app root/closure, runner identities and every original/retry outcome. All recorded owned processes ended; source/Git writer ownership is released. All roots and evidence remain. Raw diagnostics stay0700/0600 outside the portal in `/tmp/e0os-postreview-0siudjgz`; tracking contains sanitized facts and hash references.

No installed profile preparation/activation, live cluster query/update, default integration, CI, collection/deletion or session lifecycle action occurred. The installed runtime and live cluster remain unchanged. Lead/E1 own subsequent consumer preparation and any separately authorized activation.

Session remains open: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-vpsadmin-haveapi-upgrade/
