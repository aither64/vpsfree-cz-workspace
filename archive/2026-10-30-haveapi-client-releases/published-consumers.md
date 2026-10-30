# Published consumer verification

Go v0.1.0 and TypeScript 0.2.0 public consumer verification passed. Both checks
ran once after the lead supplied publication confirmation and exact tag/archive
evidence. Source and canonical repositories remain unchanged. Disposable consumers,
copied repository Nix definitions, scripts, logs and receipts are under ignored
`consumer-verification/`.

## Go v0.1.0

Approved source: `134a9e69f9aa6ddec5c94b53744865c6f81ecdd0`.
The prepared ordinary Go module requires
`github.com/vpsfreecz/vpsadmin-go-client v0.1.0` without replacements or local
paths. Its program compiles constructors, language/header methods, VPS inputs
and output types. The program is built, never executed.

After the lead confirmed publication, the copied repository `shell.nix` ran
`consumer-verification/run-go.sh` through `launch-go.sh` in a fresh policy
watcher. It used empty
owned module/build caches, public `GOPROXY=https://proxy.golang.org` and
`GOSUMDB=sum.golang.org`, no private exemptions, local toolchain, workspaces
disabled, and CGO disabled. It downloads the exact module, records origin and
module/go.mod checksums, compares every downloaded module file to hashes read
from the approved exact source commit, runs `go mod verify`, and builds the
consumer with `-mod=readonly`. Resolved modules and embedded binary metadata
are retained. A supplied origin must name the canonical Git repository and
approved commit; source equality remains required independently.

Result: passed once, real exit 0, approximately 44 seconds, Go 1.26.8. The lead
provided annotated tag object `54a265db8d133cfebd58fb27a38dfdd5e5bba279`, peeled
to the approved source. Public module origin independently reports the same
canonical repository, commit and `refs/tags/v0.1.0`. All **687** downloaded files
match exact approved commit hashes; `go mod verify` reports all modules verified;
the ordinary consumer builds with `-mod=readonly` and no replacement/local path.
The executable was not run.

- Module checksum: `h1:lk18YreP1ygPjeVxchcsYVlyAPbKjxV4GJqYi8emlUM=`.
- go.mod checksum: `h1:n7aZvL8Z1XGeKF6lDkdmsfGdBOh8SiKxl07FXjpGygw=`.
- `receipts/go-download.json` SHA256:
  `71c0d0b66441da4a5765e59bc6d3941c2fc174356f678b0a5da91e430df4e404`.
- `receipts/go-source-verification.json` SHA256:
  `1dcdbd4843e9da42398c1ce80bd72e1baf6655f7012b676a54b5e7edc162d894`.
- Command log: `logs/go-consumer.log`; real status: `logs/go-consumer.exit-status`;
  watcher report: `logs/go-consumer-watcher-result.txt`.
- Complete module/proxy/toolchain evidence: `receipts/go-{environment,toolchain}.txt`,
  `go-resolved-modules.json`, `go-build-modules.txt`, and consumer `go.sum`.

The binary's dependency build metadata names v0.1.0 with the same module
checksum. Its main-program VCS metadata describes the containing coordination
workspace and is not used as SDK source evidence; the downloaded SDK's origin
and independent full-file comparison establish that identity. No propagation
failure or rerun occurred. No operation remains running.

## npm TypeScript 0.2.0

Approved source: `e5786f69b7c223c3bb5b1de99b7f97186eec368a`.
The isolated ESM consumer imports the public facade and its actual peer,
compiles README-style VPS page/options types under strict NodeNext/ES2022
settings, and imports/constructs the facade without invoking operations.

After publication confirmation and receipt delivery,
`consumer-verification/run-typescript.sh` ran through `launch-typescript.sh` in
the copied pinned repository Nix environment with a fresh policy watcher. It
queried only the exact public npm version, downloaded the registry archive
with scripts disabled, and installed exact
`vpsadmin-typescript-client@0.2.0` and TypeScript 6.0.3 from the public registry
with scripts disabled, then checks strict types and ESM imports. The automatically
installed exact `haveapi-client` 0.30.2 peer is verified.

`consumer-verification/verify-typescript.mjs` requires the final published tag
run's receipt to name package 0.2.0, tag `v0.2.0` and the approved source commit.
It compares registry integrity, downloaded archive SHA256/SHA512, installed npm
lock integrity/tarball URL and package identity to that receipt. The earlier
build-only artifact cannot satisfy this gate. Registry metadata, original
downloaded archive, install lock, dependency listing and results are retained.

Result: passed once, real exit 0, approximately 25.9 seconds; Node 24.21.0/npm
11.19.0. The lead confirmed public publication after propagation and supplied
the original accepted final tag artifact **12978397388**, workflow run
**41059048868**, publish job **124074200061**. The receipt copied from
`typescript-tag-41059048868/artifact/receipt.json` binds approved commit
`e5786f69b7c223c3bb5b1de99b7f97186eec368a` and tag `v0.2.0`; the lead's remote
tag proof names object `1b645b2190261268c566ed81c85543f4e51e6b55` at that commit.

- Published archive SHA256:
  `36e699738830303fe8e1d76d102eacda025653dc75c07ce88d65a134c6ff3e3b`.
- Final receipt, public registry metadata, downloaded archive and installed
  npm lock all agree on SHA512 integrity:
  `sha512-EugXnu4GEEdEXuaCh62MwCWQ4D9LkgmBuTnpLaSZM13NgwPbQkAWDiOdaQmr8Xt2lYsE4HrPuNEVrJsYuGJKkw==`.
- Installed package and public registry resolve exact version 0.2.0; npm's
  installed lock resolves its public registry tarball, without file/local links.
- Installed generator identity pins released HaveAPI
  `0e7166a0f8f15827bfac051666a53bf449e999ec`; installed schema SHA256 matches
  `476f0086726a443a6ef8ad9a9d499bd3feff6eb6c5b0b652dcc999192d638794`.
- Actual installed `haveapi-client` peer remains exact 0.30.2. Strict NodeNext
  TypeScript 6.0.3 type checking passed, as did actual ESM imports and facade
  construction; no operation/authentication/API request ran.
- Evidence: `logs/typescript-consumer.log`, `typescript-consumer.exit-status`,
  `typescript-consumer-watcher-result.txt`; `receipts/typescript-{publication,
  registry,pack,integrity-verification,installed}.json`, final tag receipt,
  original registry tarball, consumer `package-lock.json`, tool versions.

No propagation/network failure or retry occurred in this consumer check. The
upstream publication's earlier 404 propagation was already reconciled by the
lead/owner before this assignment and required no upload retry. No operation
remains running.

## Execution and failure boundary

No production API requests, source rebuilds, generator checks, protocol tests,
MSRV suites or provider tests are part of this package. Fresh Luna/low utilities
use the retained catalog's watcher identity and explicit full-access/never
execution policy. Run each package once, stop on its first failure, preserve
exit status and logs, and report propagation/network failures for parent
diagnosis. No retry-until-green. A bounded metadata read and diagnosis precede
any authorized rerun. No repository claims are held for these checks.

No consumer verification remains. The lead owns session state and portal
reconciliation. This package performed no source/ref mutation, repository
claim, release retry, production API call or session lifecycle action.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-30-haveapi-client-releases/
