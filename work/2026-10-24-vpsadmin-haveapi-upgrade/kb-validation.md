# KB local preparation receipt

Current restructuring editorial snapshot **1/3: remove haveapi-fs** is prepared
locally. Canonical schema-5 manifests preserve the recorded production guards;
191 pages remain inventoried, exactly2 change and189 remain unchanged. Installed
manifest parsing and candidate checksum reads pass. No fresh production query,
staging write or publication is claimed. The matching intended publication
revision starts at `kb-original` and is saved under
`kb-restructure/publication/01-remove-fs/`.

Previous [0.31.2 checks](package-0.31.2/kb-checks.md) and
[staging receipt](package-0.31.2/staging/receipt.md) remain historical evidence.
The text below retains the historical0.30.2 checks and their original limits.

## Historical 0.30.2 receipt

Package D, implementer3, updated 2026-10-26 for published HaveAPI 0.30.2.
Focused local checks complete; affected independent final review and
staging/rendered verification remain with the lead.
No project repository was edited. No staging or production write was performed.

Session identity: `dev-session current` and both environment values matched
`2026-10-24-vpsadmin-haveapi-upgrade` in
`/home/aither/workspace/ai/vpsfree.cz` before session work.

## Exact review artifacts

| Language | Candidate | Candidate SHA256 |
| --- | --- | --- |
| cs | `kb-candidates/cs/navody/vps/api.txt` | `62ba43fdcd6c046008ce28a322147eab2f53289278497921b92dfeb313acc5d0` |
| en | `kb-candidates/en/manuals/vps/api.txt` | `5eb9eeac2c3efed06d2ec69993c6f387144659a27ddb38696c5c1028a4a1e9ec` |

| Manifest | Manifest SHA256 |
| --- | --- |
| `kb-release-cs.yml` | `9973a3d985ac6003b1b177a7f3ad5dde6affa0ea2ea5082f8ca49c62010c8703` |
| `kb-release-en.yml` | `75189c55e4fd8a83124ae7ada5d7cc9e9703bb6d8a608127e4dddfa751484c27` |

`release-changes.yml` supplies both accepted localized summaries. The manifests
are generated schema5, one write each, with no media, deletion or managed-code
provenance. The lead supplied final prose and directly applied the writing skill
and both pinned humanizers. Candidate bytes equal those supplied final files.
The existing summaries still describe the complete two-page release. Exactly
three version fields per language differ from the reviewed registry bundle:
the PyPI version link, pip installation version and npm installation version.
All change 0.30.1 to 0.30.2. Python/TypeScript executable snippet bytes, Rust
registry guidance, other article content, originals and summaries are unchanged.

| Page / original | Production source revision | Original SHA256 |
| --- | ---: | --- |
| `navody:vps:api` / `kb-original/cs/navody/vps/api.txt` | 1783860648 | `8ea88de825d7b3823aee1d4ff8fd2704c9eb2f431cfbb944643927eabde3fd13` |
| `manuals:vps:api` / `kb-original/en/manuals/vps/api.txt` | 1777543182 | `8006293f735a7e6f45c04d2d59ad82a003afa4547db1ddb38f380504e1e107d3` |

The source snapshot index SHA256 is
`87c999835a1015665ed985ce2f85e8f05348ae7f11e7c93625538933af6709d7`.
Canonical `kb-contract-fetch` fetched the complete accessible production
inventory: 114 Czech + 77 English pages. Canonical `kb-contract-build` used
schema3 full-page guarded `content_replacements`; `kb-contract-manifest
--changes` generated schema5. Both indexes retain exactly 191 unique page IDs.
Exactly two pages change; the other 189 pages are byte-for-byte unchanged.
Originals match the fetched source, including their captured revision guards.
Read-only production checks on 2026-10-26 at 08:11:14–15 UTC found the same exact
revisions and content hashes. `getPageInfo` before and after each page read
agreed. Neither the original files nor source snapshot was refreshed.

Before regeneration, the complete old eight-file bundle was preserved under
`package-d/history/2026-10-24-git-rust/`, with `receipt.json` binding every old
hash to workspace commit `87c5e6f9683bfcea1d82401100ea33be57df8de7`.
That commit also retains the original reviewable files. Historical candidate
hashes were CS `a5c9ef5f88396f265ebca39be22ee3f0c752b1ea03863eb103b01135136ef158`
and EN `358f8da3ffef7538bb6d31d6d49f1fac226797914bc320c96a1c850ef908fd21`;
historical manifest hashes were CS
`a2b256bd7c616b82df73af806b34d7d8bf9cccf2bf7e8f52662a4104f9b82411` and EN
`3b9a4f9c717a52ed4ea644a8ad6942b4a4a38adf9d11f30a1894e75b53d7ed13`.
The old bundle was never staged, published or externally consumed.

Before the 0.30.2 regeneration, all eight artifacts from the reviewed registry
bundle at `df1944a2004282d5eb988323e25c9c3010791b8d` were also preserved under
`package-d/history/2026-10-25-haveapi-0.30.1-registry/`. Its `receipt.json`
binds each old artifact hash before any current output changed. Prior candidate
hashes were CS `d9da4386169db2b40001a6e1c465c366072ed4bf1e622c4657705541661c14c6`
and EN `5671c4858dfd9766d506e28b7545354fe380b44fdd2d8a9beb62be855e98d737`;
prior manifest hashes were CS
`915552d729311e1acf4c54032bbf16512379555b6586355b0eec642328f8e99c` and EN
`1da2ae629d6bb11ae0160d4c276a8d5544a02e7bc2319aa9a64bac371d94d3ed`.
That bundle likewise was not staged or published. Current follow-up changes
version references only; no migrations or persisted formats exist. The lead
records the new commit in the review packet.

Reproduction after any lead content change:

```sh
ruby work/2026-10-24-vpsadmin-haveapi-upgrade/package-d/prepare-release.rb \
  work/2026-10-24-vpsadmin-haveapi-upgrade/kb-final/cs/navody/vps/api.txt \
  work/2026-10-24-vpsadmin-haveapi-upgrade/kb-final/en/manuals/vps/api.txt \
  work/2026-10-24-vpsadmin-haveapi-upgrade/release-changes.yml
```

The full snapshots, replacement plan, candidate index, reference tools and large
logs remain local evidence. Commit the two candidate pages, two originals, two
manifests, changes file and this receipt for final review; do not bulk-add mirrors.

## Verification

- Both manifests pass the installed `KbRelease::Manifest` parser and candidate
  checksum reads. Each retains the source revision/checksum above. Both pages
  contain exactly one `<page>manuals:vps:api</page>` translation marker.
- The installed generator intentionally emits `language_counterpart` only for
  English. It derives the Czech/English pair from Czech candidate `<page>` tags.
  The release verifier reads the Czech candidate marker and English manifest
  field. English records `navody:vps:api`; no field was manually added to Czech.
- Neither API page is managed in `contract/pages.yml` at contract reference
  `ce2c8cd9358c3636e5d39343e595df813a0b197f`. No new contract repository scope or
  `<kb-managed>` marker was introduced.
- The introductory documentation/login paragraphs remain unchanged. Both
  authentication sections through the end remain byte-for-byte unchanged.
  Only the client overview, three client subsections and English translation
  marker change. `git diff --no-index --check` found no whitespace errors.
- Exact final Python snippets extracted from both languages are identical,
  syntax-compiled and executed using a fresh install of the actual PyPI 0.30.2
  wheel on Python 3.12.12
  with controlled HTTPX. Token header, discovered `vps.list` alias, limit query
  and mapping response were asserted. Sync/async methods were separately checked.
  Wheel SHA256: `4332346ea2923edd2764107e900f87b3fba780c287869432ab1cfdd265646d50`.
  Its released metadata still requires Python >=3.11. These are new 0.30.2
  checks; the earlier 0.30.1 checks remain historical evidence.
- Exact final TypeScript snippets extracted from both languages are identical.
  Strict TS 6.0.3 compilation passed against a fresh npm 0.30.2 install and its
  bundled declarations with
  Node 24.21. Both compiled outputs executed against its actual UMD library with
  controlled XHR, asserting fake-token authentication, request route/query and
  resource results. The article uses the checked `result.value` return form.
  npm integrity: `sha512-o2geRdCaZe9gH93GPLMdGCxeIflyuERt3dN0oErVe3xzdLfPV2A+UwDI62LbUSOEzd2XgMZLCa/BbmhwZBQ/6Q==`.
  All 53 installed package files match the digest-checked registry tarball;
  tarball SHA256 is `e6fc12590ebabd05b09d579cfcd62344bf60dfa0b3b05b3c75d7015e2bd5cbfa`.
  The recorded SLSA statement's subject digest matches that archive and records
  source `321ce8256ad4704efaed04f4f2aa1ea4c2a3b4b8`, tag `v0.30.2`, release
  workflow run `40238928168`, attempt 1. This package has no npm `gitHead`.
  Tests used the installed published runtime, not the earlier 0.30.1 package.
- Both unchanged Cargo TOML blocks parse as `vpsadmin-client = "0.1"`. The blocking
  variant in both prose examples parses with `version = "0.1"` and
  `features = ["blocking"]`. No Git source/revision remains in the candidates.
  The architect verified non-yanked crates.io 0.1.0, Rust >=1.95, API7.0 and
  its optional blocking feature. The downloaded archive checksum is
  `2099d96e698e23912879cc15a32097c920f0db96976c2bee671a5ce2239777d0`;
  the local artifact matches it. Architect evidence under
  `package-b/rust-crates-2026-10-25/` records 690 unchanged packaged files
  against the previous source, including the runtime and examples.
- The 2026-10-24 async/blocking consumer compile against Git revision
  `ff876abe17e3301da62c1b6afbda055ec89db9d2` is historical evidence only.
  It does not constitute a registry-consumer compile. The Rust guidance is
  byte-identical to the reviewed registry bundle; no Rust compilation or long
  integration test was rerun. HaveAPI generator 0.30.2 does not imply SDK 0.30.2.
  R1 performance acceptance remains owned by the other packages/lead; these KB
  checks make no consumer-performance or readiness claim.
- The earlier six package/source/SDK links returned HTTP 200 on 2026-10-24.
  On 2026-10-26 the canonical
  `https://crates.io/crates/vpsadmin-client` link returned HTTP 404 for both
  HEAD and GET. The registry API
  `https://crates.io/api/v1/crates/vpsadmin-client` returned HTTP 200 and
  confirmed 0.1.0 on 2026-10-25; its metadata checksum agrees with the downloaded archive.
  The canonical link is retained by lead direction and the repository/README
  links remain available. Fresh 2026-10-26 checks of the exact PyPI 0.30.2 link
  returned HTTP 200 for HEAD/GET; the npm 0.30.2 package UI URL returned HTTP 403
  for HEAD/GET. npm registry publication/archive/provenance were independently
  verified. These browser-facing checks are recorded gaps, not inferred package
  absence; no cause is asserted and no all-links-pass claim is made.
- A 2026-10-24 unauthenticated OPTIONS capture from `https://api.vpsfree.cz/v7.0/`
  supplied the public-schema fixture reused by the 0.30.2 tests, SHA256
  `40f5a78d3156551abdfea7b1225669bcc79c70ba342de7f74f55595567dfb72e`.
  All token examples ran with fake fixture credentials. No live authenticated
  read, token creation or member mutation was exercised.

Detailed local evidence is under `package-d/`: `technical-facts.md`,
`release-local-check.json`, `final-extraction-check.json`,
`final-python-check.txt`, `final-typescript-check.txt`, `link-check.json`,
`rust-final-status.json` and `rust-final-check.log`.
Historical focused 2026-10-25 evidence is
`followup-2026-10-25/{production-source-recheck,focused-check}.json`,
the old/new per-language diffs beside them, and
`staging-status-2026-10-25.json`. Current evidence is under
`followup-2026-10-26/`: `production-source-recheck.json`, `artifact-check.json`,
`focused-diff-check.json`, `python-check.json`, `typescript-check.json`,
`link-check.json`, and the bounded Python verifier. Current staging status is
`staging-status-2026-10-26.json`. Full mirrors, archives and raw test tooling stay
local; only the two current candidates, two manifests and this receipt change.

## Navigation applicability and existing checker limitation

Manual full-article inspection found no instruction to operate a vpsAdmin WebUI
control. The top-right login instruction concerns HaveAPI documentation at
`api.vpsfree.cz`; legacy PHP `session.login.open` is inapplicable. Opening
WebUI/API equivalence and scope-default references are explanatory. Other
actions are CLI, Ruby, shell or FUSE. No new annotation or screenshot is needed.

Independent discovery finds three English target paragraphs: API/WebUI
equivalence, generic-versus-generated API explanation, and the FUSE README
reference. All have truthful non-WebUI-action classifications in local
`package-d/api-navigation-applicability.yml`. Unrelated discoveries are unchanged.

The canonical all-page annotation checker fails on the unchanged production
baseline: both IP-address articles lack the expected
`networking.host-addresses.add` tag and still contain older text. The 2026-10-24
final checker failure was byte-identical to that baseline failure. Source discovery
likewise differs from the contract only at those two IP-address paragraphs;
target paragraph additions/offsets are reviewed separately. This is an existing
cross-repository/production drift, not a full annotation-check pass. Do not
rewrite those articles or claim newly introduced semantic bindings. Evidence:
`annotation-baseline-delta.json`, `discovery-baseline-delta.json`,
`baseline-canonical-annotation-check.log` and
`final-canonical-annotation-check.log` under `package-d/`.

## Release state and recovery

Read-only staging status still reports owner `2026-09-13-auth-email` and its
pending English review bundle. No start, reset, stage, release or promote command
was run. The lead must legitimately obtain staging before rendering either page,
checking both translation links and reviewing exact revision summaries/history
URLs. Those checks remain unverified until staging is available.

Production promotion needs direct approval for these exact staged manifests.
Staging/promotion will recheck production revision/content guards; concurrent
changes require a fresh source and candidate review. Before promotion, recovery
is local candidate revision. After a separately approved promotion, use the
captured original pages through the same guarded release workflow for rollback.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-vpsadmin-haveapi-upgrade/>
