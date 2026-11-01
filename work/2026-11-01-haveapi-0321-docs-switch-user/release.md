# HaveAPI 0.32.1 release record

## Authorization and boundary

The current user request explicitly authorizes the HaveAPI fix/backports and
patch release, including required repository integration, tags and package
publication under the ordinary protected procedures. After live policy
inspection this maps to vpsfreecz/haveapi targets master (general fix/notes,
VERSION remains 0.32.0) and haveapi-0.32 (backports/patch metadata), annotated
v0.32.1 and coordinated registries/PHP mirror. No production deployment or
session lifecycle cleanup. Required protected environment review is retained.

## Inspected starting points

- master: 209a7ac0c2fe6cd1b78735f50b5e60d979309543.
- haveapi-0.32 / v0.32.0 source: 0e7166a0f8f15827bfac051666a53bf449e999ec.
- v0.32.0 tag object: e78e4b398819a82961cabb7c7ceea59c773c6a64.
- Newest supported line confirmed by live remote refs; no v0.32.1 tag at design
  inspection and no published 0.32.1 registry entries at preparation inspection.
- Only pre-existing master-only fix: 209a7ac0 performance CI baseline handling,
  accepted for cherry-pick -x. No broader source backlog.

## Required evidence before release

- [x] Final master/stable commit series, exact heads and no-migration inventory.
- [x] Required hooks and focused OAuth/CI-baseline/metadata quick checks green.
- [x] Independent final review and resolved findings.
- [x] Separate recovery refs for inspected pre-integration master/stable heads.
- [x] Final comparisons captured, feature branches published.
- [x] Fresh target proof, short repository claim, ff-only integration and SSH
      remote proof; explicitly release claim before CI and records.
- [x] Tag/source validation and protected workflow tests/build/artifact manifest.
- [x] Inspect retained candidate before protected publication approval.
- [x] Registry hashes, install availability, PHP mirror/source and Packagist.
- [x] Downstream readiness message with exact master/stable/tag/package evidence.

## Compatibility and recovery

No migrations or persisted-state changes. Default behavior and ordinary logout
remain unchanged; provider-specific static revoke parameters apply only after
validated Switch user. Old libraries reject the new option; consumer must enable
it after upgrading and remove it before rollback. Docs cookie expiry remains
fixed at initial issuance. No whole-account logout guarantee is introduced.
Partial publication preserves original tag, artifacts, manifest and draft release;
never replace a published version, retag or rebuild accepted artifacts.

## Actual integration and publication

Pending. A tag or committed candidate alone is not release readiness.

## Committed candidate

Master final cc06cb8c2a6305f13d3b80ebc0a461507055b14c, stable final
c54404c0818284135add1e77f43feb92e192116c. Independent final review assigned to
verified reviewer0 Astra/xhigh (fresh user-directed restart) on both full ranges. No long checks, target refs or
tags mutated. Separate recovery branches retained locally:
2026-11-01-haveapi-0321-docs-switch-user-recovery-master -> 209a7ac0 and
2026-11-01-haveapi-0321-docs-switch-user-recovery-stable -> 0e7166a0.
Final comparison receipts captured for both registered worktrees.

Final independent review is complete at both candidate heads: Astra/xhigh, all
four lanes, no findings and explicit whole-history/no-migration conclusions.
See review.md; prior incomplete Sol assignment is superseded.

## Release fixture CI correction

Original branch checks20/21success; build-only release41329778485 failed two
fixture examples before artifact retention. No publication/accepted artifacts.
One test-file correction commits master391b0190241cf195a69b06f7297d3e4eebec5a83
and stable9efeadf91d894e01d1d4f4a3e3fc64c6309785c7(-x391b0190). Original heads
cc06cb8c/c54404c0 retained in separate recovery-*-ci refs. No production guard,
runtime or metadata changes; quick fixture/guard/lint/hooks/metadata green. Same
Astra reviewer assessing affected lanes before another CI run. Final tag will
use reviewed successor stable head, never failed candidate head.

## Actual integration

2026-11-01T17:49UTC: reviewed final master391b0190241cf195a69b06f7297d3e4eebec5a83
and stable9efeadf91d894e01d1d4f4a3e3fc64c6309785c7 integrated ff-only from clean
own detached target checkouts; atomic ordinary SSH push. Fresh remote exact refs
matched both, command exit0. Claimfa07fe1a-a137-4739-a23b-ab2382746080 explicitly
released and verified released before records/CI. Source/tag/package next.

Tagv0.32.1 objectceebc179cd4266ac4353360acf248f8d7493d5bf -> exact stable
9efeadf91d894e01d1d4f4a3e3fc64c6309785c7 pushed, clean/tag metadata validation
passed in required top-level shell. Authoritative tag workflow41333460242.
No publication approval yet; tag alone is not readiness.

## Retained candidate inspected before protected approval

Tag workflow41333460242 build/test/metadata/activation setup/artifact verification
all succeeded. Artifact13094149459 release-41333460242,1244757bytes, unexpired,
GitHub artifact digestsha256:ff1718d5ced5b338a65e172c70f77446dab766c560d67595aa6fdff5eb2512d8.
Downloaded original candidate evidence/release-41333460242. ManifestSHA256
37d48672acfbef768f10bb1b86787880a215056b5dc092e48ee8b6db348abe0d,
source9efeadf91d894e01d1d4f4a3e3fc64c6309785c7,version0.32.1,tagv0.32.1,
run41333460242. Notes match accepted scope/prose. Five coordinated gems, npm,
browserJS, PHP archive, Python wheel+sdist and tools/dependency receipts present.
Lead ran repository tools-only retained-artifact verify against exact tagged
checkout. Protected release environment24722193856 current user can approve;
required reviewer aither64 retained. Existing explicit user patch-publication
authorization applies; approve this concrete retained candidate only, no rebuild.

## Published artifact SHA-256 inventory

All files below are version 0.32.1 (browser bundle follows the same release).
The original manifest includes exact resolved dependency locks and tool versions.

| File | SHA-256 |
| --- | --- |
| haveapi-client-0.32.1.gem | fd4de589cc10ff0a446a906318b170abf22e6628771181cfb5d8a7b2a87533d4 |
| haveapi-0.32.1.gem | fc93f449080dc3e62d938e6d5a21f4cbed0b28dade75f5314d1fe918c16ecf18 |
| haveapi-go-client-0.32.1.gem | d5de7f957f9f116099ac7e69dfdd3a22ec6bedcc8f9ab464d7b74509d0ad21ba |
| haveapi-rust-client-0.32.1.gem | 04198e0be8d68e6edb1966a05e9c6c087ed36dee20dcd3fb5d22c489a4fd4277 |
| haveapi-typescript-client-0.32.1.gem | c85fd88ccebc8a12a5781ecc0e3c2f9f153c062e2c70de8dc70f438dc6274090 |
| haveapi-client-0.32.1.tgz | bd7f01c18ab3e000cf1f6fc7f614b89152c9613a19c4f1bcbcff09c32dbd0166 |
| haveapi-client.js | 352e238d4af956999aafe02e55597d8a1a162da3f97c433a6f8b40bcd0223554 |
| haveapi-client-php-0.32.1.tar | 70efb88c15e23c72ee8ddb287610de9d643f13397cc7276a1c7f608feb57595b |
| release-notes.md | 231bf993dfd83b6b9f31e3109e61c74d975a6662df64cb8073da33b868adb4c7 |
| haveapi_client-0.32.1-py3-none-any.whl | 2dffc07808e7c325f7254182b0c8a6939665118df74c729e984d4acbc4c4ecb0 |
| haveapi_client-0.32.1.tar.gz | 38031fe34556007f28f3c0a0393623427ad59fb4f17116319a41d7d0c2166d48 |
| release-manifest.json | 37d48672acfbef768f10bb1b86787880a215056b5dc092e48ee8b6db348abe0d |

Public manifest: https://github.com/vpsfreecz/haveapi/releases/download/v0.32.1/release-manifest.json

Fresh post-publication remote fetch/ancestry checks pass for both registered exact
final heads in their configured targets. Remote master/stable equal the recorded
final heads; tag object/peeled source unchanged. GitHub Release is public (not
draft), published 2026-11-01T18:03:26Z; every public asset digest matches retained
manifest, including its own digest. Isolated registry/install proof pending.

## Final release result

Published GitHub Release 430757245 at 2026-11-01T18:03:26Z; original publish job
completed 18:03:29Z, workflow success 18:03:30Z. Actual five-gem registry bytes,
isolated install/activation/load/new constructor proof pass; npm and both PyPI
artifacts match manifest. PHP mirror/master/tag and Packagist 0.32.1 bind commit
4b3260d36a070ad9590ff6c3ee8a91eb873b4e84 and exact HaveAPI source; mirror snapshot
matches retained PHP payload. Public assets/public manifest match original.
See artifact-verification.md. No package split, migration, production deployment,
held resource or remaining command. Final readiness message
511b9047-108b-44d3-9a29-15b5142193d4 delivered through authorized runtime pair.
Session remains open, all refs/worktrees/evidence retained; no lifecycle cleanup.
