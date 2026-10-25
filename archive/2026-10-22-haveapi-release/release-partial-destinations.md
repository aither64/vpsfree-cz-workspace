# Partial release destination inventory

Implementer2, 2026-10-22, bounded read-only observation around
20:43:08–20:43:50 UTC. Session current, both environment bindings and saved
workspace-write access matched before work. Required workspace verification/Git
and HaveAPI repository/release guidance was read. Complete API bodies and response
status/header evidence are retained in
[release-partial-destinations.json](release-partial-destinations.json).

## Exact source and operation binding

- Repository: `vpsfreecz/haveapi`; shared version `0.30.0`, tag `v0.30.0`.
- Official tag-ref API returned annotated tag object
  `81a896f97b75781f62c5850a6e8df7932c92782b`. The tag-object API resolves it to
  commit `b64fb25bea8d8222fb3263b99956c0b61438a859`.
- Official run API binds run `39849807897`, attempt 1, to that same commit,
  branch/tag `v0.30.0`, push event, completed/failure.
- Lead reported build and PyPA publish-step success before the final helper
  failed. Retained failure log:
  `release-publication-watch-39849807897-failed.log`; line 16 reports
  `PyPI publication is incomplete; upload the retained Python artifacts first`.
  PyPI diagnosis/probes belong to implementer1 and were not duplicated here.

## Direct destination observations

| Destination | Official response | Observed state |
| --- | --- | --- |
| RubyGems `haveapi-client` 0.30.0 | Version API HTTP 404 | Version absent at observation. |
| RubyGems `haveapi` 0.30.0 | Version API HTTP 404 | Version absent at observation. |
| RubyGems `haveapi-go-client` 0.30.0 | Version API HTTP 404 | Version absent at observation. |
| RubyGems `haveapi-rust-client` 0.30.0 | Version API HTTP 404 | Version absent at observation. |
| npm `haveapi-client` 0.30.0 | Version metadata HTTP 404 | Version absent at observation. |
| PHP mirror `master` | Commit API HTTP 200 | Still release 0.29.12 at `84c46343171d3839c5de011035d96a0f50425a86`; commit records `HaveAPI-Source: 355c2990a4bfd3940d3234cb2077ad0127f43551`. |
| PHP mirror `v0.30.0` | Tag-ref API HTTP 404 | Tag absent at observation. |
| Packagist `haveapi/client` 0.30.0 | Composer p2 metadata HTTP 200 | Stable version list contains no 0.30.0/v0.30.0; latest listed version is 0.29.12. |
| Public GitHub Release `v0.30.0` | Unauthenticated release-by-tag API HTTP 404 | No public release returned at observation. |
| Private GitHub draft/assets | Corrected GraphQL lookup denied | Unknown: saved PAT cannot access this release resource; draft presence and asset inventory could not be established. |

These are destination API observations, not deductions from workflow step order.
The 404 registry responses establish no remote 0.30.0 artifact to compare there;
no artifact-byte/hash verification is claimed. Packagist indexing and the PHP
mirror are separate observations.

## GitHub draft visibility limitation

The first GraphQL request included unsupported `Release.targetCommitish` and
returned a schema error. It was corrected once, retaining both responses. The
valid lookup for `release(tagName: "v0.30.0")` then returned
`Resource not accessible by personal access token` (`FORBIDDEN`). Its null result
is not evidence that a draft is absent. A separate unauthenticated public
release-by-tag lookup returned HTTP 404, establishing only public visibility.

The exact private draft/publication state and asset names/sizes/digests require
a suitably authorized read-only caller. No asset content or whole asset batch
was downloaded. Lead owns download of the original tagged run artifact into
`official-release-39849807897` and subsequent verification of those exact bytes.

## Yield

Bounded inventory is complete with the private draft/assets access gap reported
to lead. No publication/rerun, registry mutation, source/index/ref/tag/config or
credential change, test/build/listener/install, polling, PyPI request or separate
Rust-crate operation was performed. Existing local dist and all prior evidence
remain untouched. No command or runner remains active for this inventory.

No further remote observation or recovery action is authorized by this report.
Preserve the original tag/run artifacts and diagnose the failure before any
separately authorized recovery operation.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-haveapi-release/
