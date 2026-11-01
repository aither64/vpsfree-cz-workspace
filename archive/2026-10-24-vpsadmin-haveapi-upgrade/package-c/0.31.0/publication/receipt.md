# C4 final checks and own-branch publication

Lead accepted the bounded current-correctness disposition and released ordinary
publication. The new own branch `dev/vpsadmin-haveapi-031` is published at exact
`baf00acc31d34ab37720643c5833b4476a341f3b`, tree
`2e7b4cb5eba6bc96f34f834c49fc097d5fdd987b`. Base/default main remains
`5a2d2bdc3ad7a827038f877d75959916528db844`. The reviewed two-commit series is
`4d040e0357e405761432075a23783b4d0d779432` followed by `baf00acc`;
original carried authorship/dates, R2 and OPTIONS corrections are retained.
Whole-history review accepted consolidation and no migrations.

Fresh canonical SSH fetch, remote reads, clean exact source/tree/hash checks and
normal hook/identity checks passed. No hook framework or active non-sample hook
is declared/configured; no bypass was used. The only push was:

```text
git push --porcelain --no-force origin \
  baf00acc31d34ab37720643c5833b4476a341f3b:refs/heads/dev/vpsadmin-haveapi-031
```

[Push log](push.log) records exit 0/new branch. An independent canonical SSH
[remote read](remote-after.txt) proves exact published head and unchanged main,
LIVE f10 branch, PR74 alias/head and PR63 head. The public
`dev-session worktree capture-comparison` command succeeded for registered
`vpsadmin-webui-031`, recording exact 5a..baf
[comparison](capture-comparison.json). No PR was created or updated.

## Accepted evidence and limits

Quick checks, independent final four-lane review, 228 script/57 BFF cases,
303 unit files/1899 cases, normal production build and all five ordinary Nix
outputs passed at this exact head. Full evidence remains in
[postreview results](../postreview-results.md) and the
[review packet](../review-packet.md). No source/test/review change followed.

Browser results remain distinct: first bounded batch 3/6; corrected batch 5/6;
then the authorized sole desktop expiry comparison passed once at both exact
f10 and baf with cold isolated original sources/dependencies, identical rooted
FHS/browser and unchanged root URL, public overview and fresh-notice assertions.
Lead accepts the other five actual passing cases plus the separate current
expiry pass for this scoped upgrade. There is no synthetic 6/6 result, claim of
an exact cold-load cause, or claim that the earlier failures were preexisting.
[Paired receipt](../expiry-paired/receipt.md) preserves both outcomes and all
earlier failure artifacts. Historical 60/62 mobile expansion limits remain
separate. Mocked fixtures do not certify actual TLS/BFF/OAuth behavior.

| Artifact | Exact output | NAR |
| --- | --- | --- |
| Frontend | `/nix/store/729jjifw96nb2hvh902563jfh7mjma00-vpsadmin-webui-frontend-1.0.0` | `sha256-fcxN91fpQaDJP4vZdtNWnlwjs32AQKo5TgXcwf7ULwQ=` |
| BFF | `/nix/store/l93gg2jcx91ir8qrrbv8x1zl5f4q7izh-vpsadmin-webui-bff-0.1.0` | `sha256-zonVCNBbQpuKId85O8Nbs3CL/b20FH4jH2dbWXvSoWY=` |

Frontend drv is `/nix/store/gymypz5zs55blbgc8c9i6j9s73am6075-vpsadmin-webui-frontend-1.0.0.drv`;
BFF drv is `/nix/store/chikr6wq47a4298hjmdnywdiy6xn0jxg-vpsadmin-webui-bff-0.1.0.drv`.
All five output derivations/paths are in
[output identities](../nix-output-identities.json), with the
[complete recursive derivation/input graph](../nix-recursive-input-graph.json)
and [locked flake metadata](../final-flake-metadata.json).
Frontend/BFF [build metadata](../nix-build-info.json) is exact baf, dirty false.
Filtered source `/nix/store/z283lwwdi70gdqbfdclkm34kgp0zvgyq-source` has NAR
`sha256-aRkO/aTZzx3NmVDkr45L+UyroUlUeVgUrl8AcvYiSWM=`;
the source root and toolchain profile remain retained.

[Owned output roots](../nix-root-map.json) retain frontend/BFF/provenance/source
and package-content outputs through ordinary persistent out-links. Fresh
[output reconciliation](nix-output-reconcile.json) confirms all five paths
exist and NAR/reference identities match the original passing proof;
[registered roots](nix-registered-roots.txt) remain present. The retained browser
FHS root and all 185 NAR/reference identities were checked after the paired run.
No build/input/policy change or restoration was needed during publication.

Root npm selects exact HaveAPI 0.31.0 from released source
`c9124da141adc258fbbaf67d4ec19ee3f8580849`, release run 40554625752 attempt 1.
Packed archive SHA256 is
`1f01aea5cd29415013b21cbe763ae5823d6889d8b6a93567916801ac50705af3`;
53 packed source files, registry integrity and SLSA source/subject were verified.
Root npm dependency hash is
`sha256-G2LFBs0USqvIXPDiGyra2uXGHxsr557BUrh7Fft0roo=`.
The [review packet](../review-packet.md) links artifact/provenance receipts;
adapter/application/E2E source remains unchanged from f10.

## CI discovery and handoff boundary

One bounded exact-head discovery found zero workflow runs, zero check runs and
zero commit statuses. GitHub's aggregate status reads `pending` with zero
contexts; this is not a running or successful CI result. Captured responses:
[actions](ci-runs.json), [checks](ci-check-runs.json), [status](ci-status.json),
[query time](ci-discovery-time.txt). Declared workflows trigger feature checks
on pull requests, main pushes or manual dispatch, not this own-branch push.
No manual dispatch or additional CI wait was assigned or performed.

[Final source checks](source-after.json) prove exact head/clean tracked worktree
and tested hashes. No C source-writer, build, browser or network command remains
active. [Process reconciliation](owned-processes-after.json) records an idle
terminal bash without children, retained without signals. No project commit,
source-path move, private config/ignored lock/node_modules mutation, PR74/PR63
rewrite, default integration, deployment, provider/runtime/lifecycle or cluster
action occurred. The original live f10 checkout/ref remains intact. C has no
source operation blocking E3; any later movement/redeployment remains under the
lead/E3 release and remaining A gates. No merge/install/live readiness is claimed.

Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-vpsadmin-haveapi-upgrade/
