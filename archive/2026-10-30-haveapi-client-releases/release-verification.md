# HaveAPI 0.32.0 tagged release verification

Owner: implementer0, verification/observation only. Lead owns Git refs and
protected publication approval under the user's explicit release direction.

## Exact source and run

- Integrated master and `haveapi-0.32` source:
  `0e7166a0f8f15827bfac051666a53bf449e999ec`.
- Annotated `v0.32.0` tag object:
  `e78e4b398819a82961cabb7c7ceea59c773c6a64`, peels to that exact source.
- Primary tag-push `release.yml` run:
  [41056909572](https://github.com/vpsfreecz/haveapi/actions/runs/41056909572),
  `headBranch=v0.32.0`, exact source above. Build job `124066630934`.
- Same-source master build-only release `41056402168` and prior feature
  dispatch `41049401404` remain separate historical verification. Their
  artifacts cannot replace the tag run's new immutable release artifact.
- Same-source master push/dynamic CI inventory contains twelve completed
  successes, including maintained component tests, translations, RuboCop,
  performance and build-only release. Exact run IDs and conclusions retained in
  [same-source-ci-inventory.json](haveapi-logs/tag-41056909572/same-source-ci-inventory.json).

## Build and protected-environment milestone

Fresh standalone verification utility uses pinned catalog
`495ef6620926420612ee4988e69d03a4e975e41734a1a5e3208db65fcd731db7`,
`gpt-6-luna` / `low`, explicit `danger-full-access` and approval `never`.
Launch policy verified in
[watcher.log](haveapi-logs/tag-41056909572/watcher.log); narrow instructions in
[watcher-brief.txt](haveapi-logs/tag-41056909572/watcher-brief.txt).

The utility observes only the tag run, downloads its artifact/logs/metadata and
returns at successful build plus protected publication waiting, or on failure.
It never approves, dispatches, retries, rebuilds, retags or writes registries.
Lead takes ownership of the pending publication milestone. A later publication
phase requires a fresh monitoring identity.

Build job `124066630934` succeeded at 2026-10-30 12:44:05 UTC (5m12s).
`Test and build maintained packages`, `Verify retained artifacts` and
`Summarize candidate release` steps all passed. Publication job `124068866573`
is waiting on protected environment `release`; `current_user_can_approve=true`.
Watcher completed its operation and handed the pending run back to the lead.
No approval or publication occurred in this verification phase.

New tag artifact ID **12977097967**, `release-41056909572`, GitHub archive digest:
`8cb1bf77b5b27abe82b2d1b9d0199894d6ef66493b244959b65bee4af7ced05a`.
Retained at [release-41056909572](haveapi-logs/tag-41056909572/release-41056909572/).
Manifest SHA-256:
`0fa2c61cc13a9b80f67f5d18eb7a23681851fe9e869c760040fe8a2cf1dfdfc8`.
Verified source/tag/version/run ID and all eleven payload hashes independently.
The original manifest and exact dependency-lock texts are retained intact.

The watcher initially could not fetch whole-run logs while the protected job
waited. Parent retrieved the completed job's direct logs endpoint with
`gh api .../actions/jobs/124066630934/logs --allow-escape-sequences` into
[build-job-direct.log](haveapi-logs/tag-41056909572/build-job-direct.log),
293,112 bytes, SHA-256
`56d3167e5ee6969a746b0ae1a0f864918049d56bc4b8fcb9d65c52d0e27f2297`.
This is log download only; no workflow retry or duplicate tests.

## Concrete artifact acceptance

- All 46 frozen Go executable/library/template/metadata and sibling shared
  Ruby-schema input hashes match the retained Go/Ruby gems. Exact Go lock:
  `bb4b5eab29bef661b4b3b5cd64a26852eee795105d0a1d872a37623ffb70450d`.
- Reconstructed extracted shared-schema identity:
  `e12f7989a028bb529f4a78a510af8e09411bbeb5eec9c782feb1fbf20862533c`,
  package `haveapi-client` 0.32.0; matches final SDK source receipts.
- Extracted TypeScript generator:
  `947a98d704dca737f8bef2e1042f710e77396a0a793cb7233e8093887a713d6e`;
  Prettier `3.9.10`, config
  `ca3d163bab055381827226140568f3bef7eaac187cebd76878e0b63e9e442356`.
  These match the final TypeScript SDK generator/toolchain pins. The SDK runtime
  stays 0.30.2; generator 0.32.0 does not alter that supported peer contract.
- Extracted Rust generator:
  `923716b5f3eaca6352d82c8cbd8c194c9a8e4a7a743cf0cb8ce7c491dd08ddce`;
  copied runtime
  `9c50b8167a8b82118ba42372633e3b004276ba49fbdfed75d4979a913feea739`;
  packaged/prepared lock
  `86c1d8b1846dee4046e59518585a6ab0a52b6c66f1394729ab767c0411dd942c`.
  Match final Rust SDK provenance. No Rust SDK release is selected.
- All ten external dependency graphs match preparation. Eight lock texts are
  byte-identical; npm differs only in whitespace and PHP only in own manifest
  `content-hash`, with all package records identical. Actual tag-run lock bytes
  stay authoritative for these artifacts; no separate-build byte identity is
  assumed.
- Exact receipts:
  [input-graph-verification.json](haveapi-logs/tag-41056909572/input-graph-verification.json)
  and [Go correspondence](haveapi-logs/tag-41056909572/go-retained-package-correspondence.json).

**No artifact/input mismatch or build blocker found. Concrete retained artifacts
are accepted for the lead's protected publication approval.** Lead owns approval
and pending run state; any subsequent publication monitoring uses a fresh utility.
No duplicate suite, accepted-artifact rebuild or retag is permitted.

No publication approval or helper invocation by implementer0. No ref mutation,
repository claim, secret/publisher change, deployment or session cleanup.

## Approved publication phase

Lead approved protected environment `24722193856` under the recorded user
publication direction; confirmed deployment `7438557678`. Existing exact run
`41056909572`, publication job `124068866573`, is now owned for observation by
a **fresh** standalone Luna/low utility (explicit full access/never, same pinned
catalog utility policy). Build-phase utility is not reused.

Narrow publication brief and actual launch policy:
[publication watcher](haveapi-logs/tag-41056909572/publication/watcher.log).
The utility only observes the existing run to terminal state and retains logs,
steps and public release/asset metadata; it cannot approve, upload, retry,
dispatch or change refs. Parent verifies live destination identities and hashes
against original tag artifact `12977097967`, with complete PHP mirror file/mode
comparison and Packagist source/dist indexing. Any failure or partial state
returns to lead before recovery; accepted uploads are never repeated by these
checks. Final all-destination verification is pending.

### Publication completed and all destinations verified

Exact run `41056909572` and publication job `124068866573` completed
successfully. Publication ran 2026-10-30 12:47:34–12:51:21 UTC; run completed
12:51:22 UTC. Deployment `7438557678` has a success status. New publication
utility finished; no process or claim remains owned by this package.

Independent current read-only checks against **original tagged artifact
12977097967** and manifest
`0fa2c61cc13a9b80f67f5d18eb7a23681851fe9e869c760040fe8a2cf1dfdfc8`:

- All five RubyGems versions have exact expected name, `0.32.0`, `ruby` platform
  and original gem SHA-256. npm identity is exact and its SHA-512 integrity
  matches the original retained tarball. Both PyPI files have exact expected
  filenames, package/version and original SHA-256; no unexpected Python files.
- [GitHub Release v0.32.0](https://github.com/vpsfreecz/haveapi/releases/tag/v0.32.0)
  is public, non-draft and non-prerelease, published 2026-10-30 12:51:18 UTC.
  All twelve expected assets exist; all eleven payload digests match the
  manifest, and the downloaded public manifest is byte-identical to the
  original tagged build's manifest. No build-only artifact substitution.
- PHP mirror master and `v0.32.0` both select
  `d0d51d09ada7beb863d2cd726ca446504312579a`; annotated tag object
  `7c56769028abc9ea3f32f0e9003bdb69399c4055`, tree
  `c5ea7301b278b43be7a67d14cb9225082295c6d5`. Commit and tag messages record
  exact HaveAPI source `0e7166a0f8f15827bfac051666a53bf449e999ec`.
  Every one of 36 released files matches retained PHP snapshot blob bytes and
  tracked executable mode, preserving mirror-owned metadata exclusions.
- Retained PHP archive SHA-256:
  `42c98ba1519af090cfcd2e7ac5bf93689a8353b8051f57649ba078cf74e6514c`;
  verified path/blob/mode graph SHA-256:
  `3966657a625890ab7cdc755f13e9fbfd44c47fd6390df8fdf57406283982d843`.
  Initial inspection compared git-archive permission `0664` literally to Git
  tracked `100644`; all bytes/file lists already matched. Corrected the
  inspection to Git's stored executable bit, with no publication/source repair.
- Packagist `haveapi/client` **0.32.0 is indexed**, with both source and dist
  reference `d0d51d09ada7beb863d2cd726ca446504312579a`.

Full destination identities/checksums and PHP source graph:
[destination-verification.json](haveapi-logs/tag-41056909572/publication/destination-verification.json).
Original public manifest copy, final run/job/deployment/release metadata and
complete logs are alongside that receipt. Every destination is verified;
no partial/uncertain publication remains. The lead may proceed with the separately
approved Go and TypeScript release tags. No Rust SDK release is selected.

No approval, upload, recovery helper, retry, rebuild, retag or ref mutation was
performed by implementer0 or its utilities; the existing approved workflow owns
publication. No physical machine or session lifecycle action was involved.
