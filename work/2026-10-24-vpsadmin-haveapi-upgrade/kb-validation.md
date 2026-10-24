# KB local preparation receipt

Package D, implementer3, 2026-10-24. Local preparation and quick checks complete;
independent final review and staging/rendered verification remain with the lead.
No project repository was edited. No staging or production write was performed.

Session identity: `dev-session current` and both environment values matched
`2026-10-24-vpsadmin-haveapi-upgrade` in
`/home/aither/workspace/ai/vpsfree.cz` before session work.

## Exact review artifacts

| Language | Candidate | Candidate SHA256 |
| --- | --- | --- |
| cs | `kb-candidates/cs/navody/vps/api.txt` | `a5c9ef5f88396f265ebca39be22ee3f0c752b1ea03863eb103b01135136ef158` |
| en | `kb-candidates/en/manuals/vps/api.txt` | `358f8da3ffef7538bb6d31d6d49f1fac226797914bc320c96a1c850ef908fd21` |

| Manifest | Manifest SHA256 |
| --- | --- |
| `kb-release-cs.yml` | `a2b256bd7c616b82df73af806b34d7d8bf9cccf2bf7e8f52662a4104f9b82411` |
| `kb-release-en.yml` | `3b9a4f9c717a52ed4ea644a8ad6942b4a4a38adf9d11f30a1894e75b53d7ed13` |

`release-changes.yml` supplies both accepted localized summaries. The manifests
are generated schema5, one write each, with no media, deletion or managed-code
provenance. The lead supplied final prose and directly applied the writing skill
and both pinned humanizers. Candidate bytes equal those supplied final files.

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
  syntax-compiled and executed using the actual PyPI 0.30.1 wheel on Python 3.12.12
  with controlled HTTPX. Token header, discovered `vps.list` alias, limit query
  and mapping response were asserted. Sync/async methods were separately checked.
  Wheel SHA256: `3d44949f4d545c07ea54fbb35229e74a084d5324da89866e6d4d7a91b95eb0c0`.
- Exact final TypeScript snippets extracted from both languages are identical.
  Strict TS 6.0.3 compilation passed against npm 0.30.1 bundled declarations with
  Node 24.21. Both compiled outputs executed against its actual UMD library with
  controlled XHR, asserting fake-token authentication, request route/query and
  resource results. The article uses the checked `result.value` return form.
  npm integrity: `sha512-n4RMhSbaJZLRm9390wz+M1759h06sEOfh3XVG3t/wGrE0mr97uf+ozERXdJfGXGqxdxelkk765vidheYwUJBWw==`.
- Both final Cargo TOML blocks parse to the exact HTTPS Git dependency and
  revision `ff876abe17e3301da62c1b6afbda055ec89db9d2`. An isolated consumer
  compiled async and blocking examples against that dependency in the SDK's
  pinned Nix shell; fresh Luna/low watcher returned exit 0 after 129 s. Its lock
  records that exact Git source/revision and SDK 0.1.0. First attempts failed
  due to absent C compiler and a command argument error; the final clean check
  passed. No long project integration tests were run.
- All six new/corrected external package/source/SDK links checked returned
  HTTP 200. crates.io's `vpsadmin-client` metadata endpoint returned 404, matching
  the Git installation guidance. No minimum Node runtime was invented.
- A fresh unauthenticated OPTIONS read from `https://api.vpsfree.cz/v7.0/`
  supplied the TypeScript fixture description, SHA256
  `40f5a78d3156551abdfea7b1225669bcc79c70ba342de7f74f55595567dfb72e`.
  All token examples ran with fake fixture credentials. No live authenticated
  read, token creation or member mutation was exercised.

Detailed local evidence is under `package-d/`: `technical-facts.md`,
`release-local-check.json`, `final-extraction-check.json`,
`final-python-check.txt`, `final-typescript-check.txt`, `link-check.json`,
`rust-final-status.json` and `rust-final-check.log`.

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
`networking.host-addresses.add` tag and still contain older text. The final
checker failure is byte-identical to that baseline failure. Source discovery
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
