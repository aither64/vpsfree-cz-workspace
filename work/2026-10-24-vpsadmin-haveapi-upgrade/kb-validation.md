# KB local preparation receipt

Package D, implementer3, updated 2026-10-25 for published Rust registry support.
Focused local checks complete; affected independent final review and
staging/rendered verification remain with the lead.
No project repository was edited. No staging or production write was performed.

Session identity: `dev-session current` and both environment values matched
`2026-10-24-vpsadmin-haveapi-upgrade` in
`/home/aither/workspace/ai/vpsfree.cz` before session work.

## Exact review artifacts

| Language | Candidate | Candidate SHA256 |
| --- | --- | --- |
| cs | `kb-candidates/cs/navody/vps/api.txt` | `d9da4386169db2b40001a6e1c465c366072ed4bf1e622c4657705541661c14c6` |
| en | `kb-candidates/en/manuals/vps/api.txt` | `5671c4858dfd9766d506e28b7545354fe380b44fdd2d8a9beb62be855e98d737` |

| Manifest | Manifest SHA256 |
| --- | --- |
| `kb-release-cs.yml` | `915552d729311e1acf4c54032bbf16512379555b6586355b0eec642328f8e99c` |
| `kb-release-en.yml` | `1da2ae629d6bb11ae0160d4c276a8d5544a02e7bc2319aa9a64bac371d94d3ed` |

`release-changes.yml` supplies both accepted localized summaries. The manifests
are generated schema5, one write each, with no media, deletion or managed-code
provenance. The lead supplied final prose and directly applied the writing skill
and both pinned humanizers. Candidate bytes equal those supplied final files.
The existing summaries still describe the complete two-page release. Only the
Rust subsections differ from the prior prepared bundle; Python/TypeScript code,
other article content, originals and summaries are unchanged.

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
Read-only production checks on 2026-10-25 at 07:23:14 UTC found the same exact
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
The old bundle was never staged, published or externally consumed. This
follow-up changes documentation installation source only; no migrations or
persisted formats exist. The lead records the new commit in the review packet.

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
- Both new Cargo TOML blocks parse as `vpsadmin-client = "0.1"`. The blocking
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
  It does not constitute a registry-consumer compile. No expensive compiler
  rerun or long integration test was run for this installation-source update;
  the external R1 documentation performance blocker remains unresolved here.
- The earlier six package/source/SDK links returned HTTP 200 on 2026-10-24.
  On 2026-10-25 the new canonical
  `https://crates.io/crates/vpsadmin-client` link returned HTTP 404 for both
  HEAD and GET. The registry API
  `https://crates.io/api/v1/crates/vpsadmin-client` returned HTTP 200 and
  confirms 0.1.0; its metadata checksum agrees with the downloaded archive.
  The canonical link is retained by lead direction and the repository/README
  links remain available. The browser-facing link check is a recorded gap;
  no cause is asserted and no all-links-pass claim is made.
- A fresh unauthenticated OPTIONS read from `https://api.vpsfree.cz/v7.0/`
  supplied the TypeScript fixture description, SHA256
  `40f5a78d3156551abdfea7b1225669bcc79c70ba342de7f74f55595567dfb72e`.
  All token examples ran with fake fixture credentials. No live authenticated
  read, token creation or member mutation was exercised.

Detailed local evidence is under `package-d/`: `technical-facts.md`,
`release-local-check.json`, `final-extraction-check.json`,
`final-python-check.txt`, `final-typescript-check.txt`, `link-check.json`,
`rust-final-status.json` and `rust-final-check.log`.
The focused 2026-10-25 evidence is
`followup-2026-10-25/{production-source-recheck,focused-check}.json`,
the old/new per-language diffs beside them, and
`staging-status-2026-10-25.json`. The Python/TypeScript code is byte-identical
to the previously tested final snippets; those checks were not repeated.

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
