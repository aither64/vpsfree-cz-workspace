# C3: HaveAPI npm 0.30.2 refresh

Owner implementer1. Session identity/environment verified 2026-10-26:
`2026-10-24-vpsadmin-haveapi-upgrade`, `/home/aither/workspace/ai/vpsfree.cz`.
Architect C3 dated 2026-10-26 read in full and accepted by lead before edits.
Current repo AGENTS and routed sessions/Git/documentation/verification/commits
procedures read; unchanged earlier scope/lifecycle/KB boundaries retained.

Repository `git@github.com:vpsfreecz/vpsadmin-webui.git`, target main,
branch `dev/vpsadmin-haveapi-upgrade`, base
`5a2d2bdc3ad7a827038f877d75959916528db844`.
Starting reviewed/R2-closed head `014f7b9c9f451d6275af73c4af30a24668b77b7b`.
Preserved local ref `refs/heads/dev/vpsadmin-haveapi-upgrade-reviewed-0301`
points exactly there. Old packet/map/series/diff/R2 and PR74 plan copied to
`old-reviewed/` before refreshing current outputs. Existing old session source
refs/worktrees/records and published PR74/PR63 are untouched. Fresh remote
main remains 5a2d2bdc; PR74 remains 5dd2333b; own remote branch absent.

Registry tarball SHA256
`e6fc12590ebabd05b09d579cfcd62344bf60dfa0b3b05b3c75d7015e2bd5cbfa`;
SHA512 agrees with npm metadata and the published SLSA subject. Attestation
binds canonical source `321ce8256ad4704efaed04f4f2aa1ea4c2a3b4b8`,
refs/tags/v0.30.2, .github/workflows/release.yml, run40238928168/attempt1.
All 53 packed files match canonical clients/js source byte for byte. Between
0.30.1 and0.30.2, only package.json and dist/haveapi-client.js differ and both
are exactly a 0.30.1->0.30.2 string replacement. No declaration/behavior delta.
Registry/source evidence: npm-metadata.json, npm-attestations.json,
npm-provenance-statement.json, packed-source-comparison.json.

Implementation scope: exact root pin/lock, provenance, frontend npm hash and
current technical docs/dated work log. Source guards are data-driven and need
no edit. All app adapter/auth/uncertainty R2 and current-main overlaps remain
byte-identical. No BFF lock, database/schema/persisted/wire change, migration,
deployment or external consumer. No server performance acceptance claim.

Setup/quick results, final consolidated two-commit head and exact old/new
range-diff will be appended. Full units/build/Nix/browser checks remain deferred
until independent final review. No push, PR update, merge or lifecycle action.

Setup passed under fresh pinned Luna/low watcher (38s, exit0): Node24.21.0,
npm11.19.0, root lock regeneration, clean npm ci, ordinary dependency prefetch.
Root new npmDepsHash sha256-sY3OQDFdisOzhJO4dhwlsjvGxlhog8crhqU3tHcI4IY=.
Lock object comparison proves only root package and node_modules/haveapi-client
changed; xmlhttprequest1.8.0 URL/integrity and all unrelated entries retained.
All53 installed package files match the verified tarball. Source guard scripts
remain byte-identical and data-driven; BFF lock and every src file unchanged.
Npm install repeats existing dev-audit/esbuild allowScripts warnings and prefetch
reports six bundled optional unresolved URLs; package-build proof deferred.

## Final quick checks and consolidated history

Quick watcher passed (132s,exit0): eight focused files/123cases, six package-
source tests, fullci:quick, production audit0 vulnerabilities,409 verified npm
signatures and101 attestations. Source-security scripts/tests and all src/BFF
files remain byte-identical to old014f7b9c. No new behavior/design requested.
Only verification prose changed after the broad quick gate; final design audit
passed again (136docs,75requirements), inventory257routes/64API modules.
Actual Gitless cleaned Nix source `/nix/store/6pjw8m1fx4c0v24yvhxw78mj1kfg5193-source`
passed check-package-source with15required files. That was source evaluation/
checking only, not a Nix package build. Exact log final-source-quick.log.

Consolidated final range:
`5a2d2bdc3ad7a827038f877d75959916528db844..757f7fd8c2d5d3a4d1f6ee464acd29a5a2502176`.
Final dependency `02b45a7de7eec8966b6a2ade16a46fbb9e1b6c83`.
Final production `757f7fd8c2d5d3a4d1f6ee464acd29a5a2502176`.
One selected0.30.2 dependency stream and one production adaptation; no superseded
pin/fixup history. Both author names/emails/dates match oldcd3577a6/014f7b9c
exactly. Pre/post-rebase finaltree equality proven at
`0aa1152064b123562dceb311fc56efa50fd7fc05`. See consolidation.json/log,
range-diff.txt,old-new.diff, emptyruntime-unchanged.diff and complete final.diff/
commit-series.txt/final-stat.txt/content-mapping.json. Current root packet and
PR74concrete plan refreshed with finalhead; prior evidence retained under
old-reviewed. Clean worktree, no runtime/R2/current-main overlap changes.

No migrations, persisted/schema/wire change or supported released/deployed/
external-consumer boundary. Own0.30.1reviewref retained unchanged; PR74head
5dd2333b and main5a2d2bdc unchanged, ownremote branch absent. No branch push,
PRupdate/rewrite,merge,deployment,cleanup or lifecycle action. Longunit/build/
Nix/browser suites remain for independent finalreview and lead coordination;
serverR1performance acceptance is not this React package's proof.

## Postreview f10 execution

Retained final review and direct narrow OPTIONS correction were accepted.
Current exact f10/two commits remain unchanged/clean. Full unit/normal build
and ordinary Nix package/provenance/source/contents passed; browser launch
blocked by NixOS generic Linux loader before all62app assertions.
See postreview-results.md, final-nix-identity.json, postreview-reconciliation.json
and browser-runtime-blocker.md. No retry/publication/deployment/lifecycle action.
