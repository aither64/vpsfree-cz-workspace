# C0312 checked and published handoff

Lead accepted reviewer0 affected final review with no findings, complete
history/consolidation and **no migrations**, at accepted base
`9113caa0915b2908373ecd616f8f752e779ed4c9` through
**`2e32c814d3af70ac39257f2542075bd580ee38d4`**, tree
`ae4e282a33886faff151818255a99bd5710de832`. The complete released check and
conditional publication package is now finished. Tracked checkout remains clean;
no source change followed review. The two logical commits73070a17/2e32c814
retain original author/email/date, with no obsolete pin/fixup or migration.
[Original packet](review-packet.md), [series](commit-series.txt),
[mapping](content-mapping.json), [old/new range](old-new-range-diff.txt).

## Fresh required results

- **npm test → normal BFF-mode production build PASS0/295.233s**: all307 unit
  files/1923 cases, followed by build. No ci:tests aggregate or manual extra
  script/BFF/quick/focused/browser/SDK repeat. Local build metadata exact2e32,
  dirtyfalse/sourcegit. [Command](batch1-unit-build-command.json),
  [log](batch1-unit-build.log), [exit](batch1-unit-build.exit),
  [summary](batch1-summary.json), [metadata](normal-build-info.json).
- **Five normal Nix outputs PASS0/75.971s**: frontend, BFF, provenance,
  source-contents and package-contents. Contents372 public assets; source15
  required files; exact matching2e32 provenance. No VM/kernel build selected.
  [Command](batch2-nix-command.json), [log](batch2-nix.log),
  [results](batch2-nix-results.json), [exit](batch2-nix.exit).

| Artifact | Exact output | NAR |
| --- | --- | --- |
| Frontend | `/nix/store/c14hq17qmccd1bbzwgqnlx2yyg7cdc5x-vpsadmin-webui-frontend-1.0.0` | `sha256-6sJLB+JWZu/JMsqa0Kk69Djeq4FoKL4Hmco327Ikg+I=` |
| BFF | `/nix/store/pndb4jcckhwgcpfcnrilsjam4lv98haf-vpsadmin-webui-bff-0.1.0` | `sha256-rBi1yA/VYH1ZyejTZOcb4ASwq0If7ucWPW4gtFDHeHA=` |

Frontend drv `/nix/store/6nf89d22qbbb5kq797ys79vvw73xyinh-vpsadmin-webui-frontend-1.0.0.drv`;
BFF drv `/nix/store/42dlsq5kp5xvap3lmvmp1cph5hyj6lsi-vpsadmin-webui-bff-0.1.0.drv`.
[All five identities](nix-output-identities.json),
[NAR/references](nix-output-nar-info.json), [matching metadata](nix-build-info.json).
Both Nix package metadata files agree at exact2e32/dirtyfalse/sourceenvironment.

[Ordinary persistent roots](nix-root-map.json) and
[registered-root proof](nix-registered-roots.txt) retain all five outputs.
Source root `/nix/store/c054hj749wd59b2qv5784bmkaxb8yg4f-source`, NAR
`sha256-ZaLAoXcf21glVgdjvUQ47TqCxsMli1ZSXbS30DKF9eU=`, and toolchain profile
remain retained. [Complete locked metadata](postreview-flake-metadata.json),
[full recursive derivation/input graph](nix-recursive-input-graph.json)
(1799 nodes/no missing edges), [graph proof](nix-graph-proof.json),
[recursive output closure](nix-output-recursive-closure.json) (63 paths).

The installed actual npm0.31.2 archive/source proof remains in
[installed artifact proof](installed-artifact-proof.json) and E2's linked
release receipt: SHA2564fbe3543cea865aee70d858e3c65c2e182b2208aa977eb031ed49ff949a8118a,
all53 installed/tag files match, actual bundle Version-only and46 declarations
unchanged. Root npm hash is
`sha256-EPQkMRkwpmmQAsf2T2WbK2x9We9M78A/lT8R17x7+vs=`. Application, BFF,
fixtures, security graph, Node/flake/tooling scopes remain exact e468.
Old proof is reused only at that unchanged scope; no signature claim added.

## Ownership and ordinary publication

Explicit parent fallback while A0 owns the sole utility; no competing watcher,
model substitution or wait for utility capacity. CPU60–63/nice5/Nix1job2cores;
full logs/status/elapsed and handles69219/PID883415 and2400/PID913484 retained
through exit. No failure, retry, arbitrary timeout or source repair.
[Preflight](postreview-preflight.json), [second capacity check](batch2-preflight.json).

After both passes and effects reconciliation, fresh canonical SSH fetch and
source/head/clean/hash/lock/identity/hook checks passed. Observed main remained
`40653dffed4561dd6086716fd506a7223d3631d7`; it is intentionally excluded under
the accepted explicit911/e468 branch dependency. No default-readiness or rebase
claim. New0312 remote ref was absent. One ordinary push completed:

```text
git push --porcelain --no-force origin \
  2e32c814d3af70ac39257f2542075bd580ee38d4:refs/heads/dev/vpsadmin-haveapi-0312
```

[Push log](publication/push.log) records exit0/new branch. Independent canonical
SSH [remote proof](publication/remote-proof.json) confirms exact published2e32
and unchanged main40653, live/published e468, baf/f10, PR74 alias/head5dd and PR63.
Supported public [comparison capture](publication/capture-comparison.log)
completed exact911..2e32. No PR creation/update, protected rewrite or default push.

One bounded exact-head CI discovery found **0 workflow runs,0 check runs,0 status
contexts**. Aggregatepending/0 is not an active or successful CI result.
[Actions](publication/ci-runs.json), [checks](publication/ci-check-runs.json),
[statuses](publication/ci-status.json), [query time](publication/ci-discovery-time.txt).
Declared workflows trigger PR/main/manual execution rather than this own feature
push. No dispatch or CI waiting was performed.

## Handoff limits

[Final effects/source receipt](publication/final-reconciliation.json) confirms
exact2e32 clean, tested hashes/locks unchanged, all roots present, no active C
source command or Git index lock and **no C source/lock writer**. All command
handles are reconciled. One idle terminal bash without children is retained;
no signals or cleanup. Canonical live e468, its private configuration and ignored
files were untouched by C commands. No native/provider/runtime/KB/deployment/
source-path/lifecycle action occurred; later moves need the parent's release.

Prior3/6+5/6 failures, separate f10/baf expiry passes and old60/62 limits remain
at their original scopes, with no synthetic green/cause/preexisting claim.
Native unknown embeddedmetadata/manual-dev acceptance is separate: new native
outputs still need their own actual filtered-source/derivation/service proof,
not standalone binary equivalence. E3 owns later actual native Go-panel and
TLS/login acceptance. PR74/default integration remains unapproved and outside
this source package. Retain all roots and old evidence; leave session/cluster open.

Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-vpsadmin-haveapi-upgrade/
