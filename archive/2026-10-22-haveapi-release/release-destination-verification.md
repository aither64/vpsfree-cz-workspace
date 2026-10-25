# HaveAPI 0.30.0: final destination verification

**Passed: all 18 checks.** The public destinations and all eleven GitHub Release
assets match the original tagged-run artifacts. No missing destination, hash
conflict or Packagist indexing lag was observed.

- Source/tag: `b64fb25bea8d8222fb3263b99956c0b61438a859`, `v0.30.0`.
- Run **39849807897, attempt 3**: terminal success; publish job
  **120082754287** and retained-successful build job **120082756581** succeeded.
- Sole unexpired original artifact: **12455689943**, `release-39849807897`.
  Original artifact directory and all eleven files were preserved.
- Original manifest SHA-256:
  `f75323d63fec4f3b88a70845bffc39ca4440dd0b7fd94000f95054708e0a7890`.
- Annotated source tag resolves to the exact run/source commit. The original
  manifest schema/version/tag/run/source and ten-file checksum catalog pass.
- Verification completed **2026-10-22 21:03:40 UTC**.

## Registry hash proof

Each exact-version endpoint returned HTTP 200 with package/version 0.30.0.
All hashes below match the original manifest and retained files.

| Destination/file | Confirmed SHA-256 |
| --- | --- |
| RubyGems haveapi-client | `6c3cddfaeb7403476f4791f33d6138dbdd9a3d3493e1bca824c5c92245098de8` |
| RubyGems haveapi | `c83fdb6ef243015c2e2563931787132f15c297f19a4c4956703f15d4a99b427e` |
| RubyGems haveapi-go-client | `58a64586643b8d9b6f3762f96127d946f91c613cac2fe7685b76e0e726b16f18` |
| RubyGems haveapi-rust-client | `3aa3e2363a533460e12cadf97bb8300c25877d524bf06ea8648f7fe744336e0a` |
| PyPI haveapi_client-0.30.0-py3-none-any.whl | `90af1ca01d4bde30bf6cea681a6fb74cd820ac0c308dfe249f679784c58552b7` |
| PyPI haveapi_client-0.30.0.tar.gz | `312ce9d921aca907c57143ee627d8864278140dd92a19323977f9f5c025cd962` |

npm `haveapi-client@0.30.0` identity and exact tarball integrity match:

```text
sha512-k55/kZn5RmXX6na29yAguUyZLxgqGnwyuzIKK5IA/SjNqRg3S603jyF868EA+pmyed1fEeE0cBwHkTNLu6xYiA==
```

PyPI lists exactly the expected wheel and sdist, with no extra or duplicate files.
Raw official endpoint responses and source URLs are retained in the JSON/evidence.

## PHP and Packagist

PHP mirror `master` and `v0.30.0` resolve to
`397c95ff71ded9db98b214d58ea14a61c9973442`; annotated tag object is
`f3afe7d18520ac1157d03473558435ad8a1a1fbb`. Commit message contains exactly:

```text
Release 0.30.0

HaveAPI-Source: b64fb25bea8d8222fb3263b99956c0b61438a859
```

The immutable GitHub snapshot was downloaded into the new evidence directory
and read without extraction into a checkout. After removing its archive root and
mirror-owned AGENTS/.github files, **all 36 paths, contents and normalized executable
modes match** the original tagged-run PHP tar. Composer identity is
`haveapi/client` version `0.30.0`. Packagist's exact 0.30.0 source URL and commit
reference match this mirror commit; indexing is confirmed.

## Public GitHub Release

[HaveAPI 0.30.0](https://github.com/vpsfreecz/haveapi/releases/tag/v0.30.0),
Release ID **421179188**, is public (`draft=false`, `prerelease=false`), published
at `2026-10-22T20:58:50Z`. Its body matches original release notes modulo outer
whitespace. Exactly eleven uploaded assets were downloaded into a fresh separate
session directory; every SHA-256 matches the corresponding original artifact,
including the manifest itself. No earlier local/branch bytes were substituted.

## Evidence and operation boundaries

- Full result: [release-destination-verification.json](release-destination-verification.json).
- Raw metadata, immutable PHP snapshot, comparison receipt and eleven downloaded
  assets: `release-destination-evidence-39849807897-attempt3/`.
- Existing failed-attempt logs, original artifacts and previous receipts remain
  preserved. Only new session evidence paths were written.
- Initial local comparison hit a Python argument-name collision after saving all
  metadata. It was corrected by continuing from saved responses: no registry
  endpoint was re-probed and no destination retry occurred.
- No source/ref/config/credential mutation, build/test/install, publication,
  workflow rerun, polling, separate crate action or lifecycle/cleanup action.
  No operation remains running. This receipt establishes publication verification;
  any later source followup has a separate scope and design.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-haveapi-release/
