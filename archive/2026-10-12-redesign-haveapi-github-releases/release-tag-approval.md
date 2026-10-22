# Historical 0.29.10 approval gate

Subsequently approved by aither64, then failed during draft-asset preparation
before registry/PHP writes. This record describes the earlier gate and retained
originals; current recovery is in state.md. It is not a pending approval request.

[GitHub Actions run 39291918638](https://github.com/vpsfreecz/haveapi/actions/runs/39291918638),
attempt 2, tag v0.29.10, source b27a031fa03d8d985a3abd2679ce2fc14fe53602.
The activation check, all maintained-component tests, packaging, artifact upload
and verification passed. Publish approved artifacts is waiting for the protected
release environment, required reviewer aither64. The lead has not approved it.

Original Actions artifact: release-39291918638, ID 12206004265, not expired,
702334 compressed bytes. A saved download is retained in release-tag-artifacts/.
It contains three gems, npm tarball, browser bundle, PHP archive, release notes
and release-manifest.json. These are the tag run's own artifacts, separate from
local and branch-run builds.

The lead downloaded the original artifact and verified it using the repository
CLI with GITHUB_RUN_ID=39291918638 under the declared Nix tools shell. Exit 0:
Verified retained artifacts: v0.29.10 at b27a031fa03d8d985a3abd2679ce2fc14fe53602.
Manifest source/version/tag/run identity and all package hashes/content checks
passed. Manifest SHA-256:
b0b8600ee048019a48ef15d7e418c766eba8e7e300edc57e83a93428dc2755e4.
Release notes describe only release automation and the npm repository correction.

Human next action: open the run, select Review deployments, choose release,
then Approve and deploy. This allows the single publishing job to use the saved
artifacts for the three RubyGems packages, npm package and PHP mirror master/tag,
then complete the GitHub Release. Actual credential use and Packagist indexing
will be verified after publication. No package has been published at this gate.

The fresh Luna/low observer completed its bounded observation (exit 0 indicates
approval boundary found, not publication success). Lead acknowledged ownership
of pending approval and subsequent publication verification. Attempt-1 failure
and attempt-2 evidence are retained separately; no source or tag was changed.
