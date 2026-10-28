# C0311 checked and published handoff

Lead accepted reviewer0's all-four-lane affected final review with no findings,
including complete history/consolidation and **no migrations**, at exact
`9113caa0915b2908373ecd616f8f752e779ed4c9..e468ca48406bde1bd99cc42a05e1832fb42162f4`.
The released checks passed and own branch `dev/vpsadmin-haveapi-0311` is now
published at exact **`e468ca48406bde1bd99cc42a05e1832fb42162f4`**, tree
`13db539707ae88c8635e194ca04f3e36c6e3d76a`. Tracked source remains clean.
No source/test change followed review. [Original packet](review-packet.md),
[complete series](commit-series.txt), [mapping](content-mapping.json) and
[old/new ranges](old-new-range-diff.txt) retain both logical commits and the
original carried author/email/dates. No intermediate0.30/0.31.0 pin or fixup.

## Actual checks

- Required `ci:tests` aggregate and normal production build: **PASS0/313.446s**,
  228 script cases,57 BFF cases,307 unit files/1923 cases. BFF repeated only
  within this required aggregate; no manual extra suite. Local production
  metadata is exact e468/dirtyfalse/sourcegit.
  [Command](batch1-tests-build-command.json), [log](batch1-tests-build.log),
  [exit](batch1-tests-build.exit), [summary](batch1-summary.json),
  [metadata](normal-build-info.json).
- Ordinary frontend/BFF/provenance/source/package-content outputs:
  **PASS0/74.985s**. Contents372 public assets, exact matching e468 provenance;
  source guard15 required files. [Command](batch2-nix-command.json),
  [log](batch2-nix.log), [results](batch2-nix-results.json),
  [exit](batch2-nix.exit). No VM or unexpected kernel compilation.

| Artifact | Exact output | NAR |
| --- | --- | --- |
| Frontend | `/nix/store/ijy7b2705w5ayn4n10s8nri50f2h3czz-vpsadmin-webui-frontend-1.0.0` | `sha256-ZtZ0OIdjccJ0jjSyM4Nl5XNkPYY2lnGtuz4UcFCQElc=` |
| BFF | `/nix/store/b8v1ahw1n0f5085f7lkmkn67ysvbr764-vpsadmin-webui-bff-0.1.0` | `sha256-li0nVD9Pzr8c+6W2dWh4N1L4MP6NxN1wX8WkDF0pdhc=` |

Frontend drv `/nix/store/24masz19pd1clmw5sj00qi8qwwichalk-vpsadmin-webui-frontend-1.0.0.drv`;
BFF drv `/nix/store/740avakafhp8war1y4kx6pwvklgvw2vd-vpsadmin-webui-bff-0.1.0.drv`.
[All five identities](nix-output-identities.json),
[NAR/references](nix-output-nar-info.json),
[frontend/BFF metadata](nix-build-info.json). Both Nix metadata files agree at
e468/dirtyfalse/sourceenvironment. Current main's BFF security manifest/lock/hash
are preserved; this proves the new current BFF package, not the old C31 output.

Persistent ordinary [root map](nix-root-map.json) and
[registered roots](nix-registered-roots.txt) cover all five outputs.
Source root `/nix/store/6p46phpszswrwq6029rmj1gyyi7ynm44-source`, NAR
`sha256-v8sM+hBV76YE1COTvEorTg0OUSvWd4OkPzi2006mPmw=`, and the toolchain
profile remain retained. [Full locked inputs](postreview-flake-metadata.json),
[complete recursive derivation/input graph](nix-recursive-input-graph.json)
(1799 nodes), [recursive output closure](nix-output-recursive-closure.json)
(63 paths), [graph validation](nix-graph-proof.json). The first inspection
expected legacy top-level derivation keys; Nix emits a version4 envelope with
basename keys. The same capture was validated for every root/input/source;
there was no build/check rerun or source failure.

Generic npm0.31.1 artifact/provenance proof remains linked from the review packet:
source `d49cfa3f3b8ee42f6cd8a6b7de8b7d551215cd42`, release40592240342/attempt1,
actual archiveSHA256 `08383df15f590e319d0140c7fda6c096b04a8237ca316e609424bf7745e31d54`,
53 packed/source matches, registry/SLSA field checks, version-only actual bundle
delta and identical declarations. Root normal npm hash is
`sha256-1b+5uUE4OHl47aOHSxV3Ea1VYk14soGFk48beqmmlkM=`.
No signature-verification or server-performance claim is added.

## Monitor ownership and publication

Fresh retained-policy startup selected Luna/low with the matching840 catalog
and native utility identity. The ready utility reported its actual model as
Sol/low, so it was assigned **no workload** and ended after readiness. No model
substitution was accepted. Lead-authorized visible parent fallback owned both
commands, full logs/status/elapsed and handles57636/PID1218760 and59987/PID1241494
through completion. CPU60–63/nice5/Nix1job2cores applied; no arbitrary timeout.
[Policy/preflight receipt](postreview-preflight.json). No active watcher or
verification operation remains; the utility slot is released.

After both passes, fresh canonical SSH fetch/read confirmed main911 and an
absent own0311ref. Exact source/head/clean/hash/normal identity/hook checks
passed; publishedbaf and LIVEf10 checkouts remained clean at retained heads.
One ordinary push was executed:

```text
git push --porcelain --no-force origin \
  e468ca48406bde1bd99cc42a05e1832fb42162f4:refs/heads/dev/vpsadmin-haveapi-0311
```

[Push log](publication/push.log) records exit0/new branch.
Independent canonical SSH [remote proof](publication/remote-proof.json) confirms
exact own head and unchanged main911, publishedbaf, LIVEf10, PR74 alias/head5dd
and PR63 head. Native public [capture comparison](publication/capture-comparison.log)
succeeded at exact911..e468. No force, PR creation/update or default integration.

One bounded exact-head CI discovery found **zero workflow runs, zero check runs
and zero status contexts**. Aggregate `pending` with zero contexts is not an
active or successful CI run. [Actions](publication/ci-runs.json),
[checks](publication/ci-check-runs.json), [status](publication/ci-status.json),
[query time](publication/ci-discovery-time.txt). Declared workflows trigger
PR/main/manual execution rather than this feature push. No manual dispatch or
additional CI wait was assigned/performed.

## Preserved acceptance limits and next owner

No new browser/SDK/base campaign was run. Earlier browser3/6 and5/6 failures,
then separate exactf10/baf expiry passes, remain preserved under lead's accepted
bounded C31 disposition. They are not a synthetic6/6 result, a proven exact
cold cause or a preexisting-failure claim. Old60/62 mobile expansion limits are
historical and do not certify the newer transaction UI. Current package
unit/build/Nix proof above is fresh; actual deployed TLS/BFF/OAuth/login and
both interfaces' acceptance belong to lead/E3 after the other lane gates.

[Final reconciliation](publication/final-reconciliation.json) confirms clean
exacte468, tested hashes unchanged, all five roots present, every command handle
complete and **no C source-writer operation**. One idle terminal bash without
children remains, with no signals sent. No private config/ignored live locks/
node_modules, old refs/checkouts, source paths, provider/runtime, live guest,
cluster, lifecycle, deployment or merge changed. No additional source writer is
held for this package; E3 may act only after the parent's operational release.
PR74's exact protected rewrite remains a separate explicit approval gate.

Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-vpsadmin-haveapi-upgrade/
