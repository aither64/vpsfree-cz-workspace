# Historical 0.29.11 approval gate

Subsequently approved by the user, then failed in draft preparation before any
registry/PHP write. Current investigation is in state.md; no approval remains
pending for this failed attempt. Original files below remain preserved.

[Actions run39305802582](https://github.com/vpsfreecz/haveapi/actions/runs/39305802582),
tag v0.29.11, exact source 7fb218e28a86ab1d27de74ccb92c2a45063a4f78.
All seven ordinary tag workflows passed; release build/test/package/upload and
artifact verification passed. Fresh API check confirms status waiting, publishing
job waiting and pending environment release with required reviewer aither64.
Lead has not approved it. Publication remains incomplete.

Human action: open the run, choose Review deployments, select release, then
Approve and deploy. This authorizes publication of the saved three gems and npm
package, source synchronization into haveapi-client-php/master with v0.29.11,
and final GitHub Release publication. It does not rebuild any package.

Original Actions artifact release-39305802582, ID 12212609441, not expired,
702369 compressed bytes. Saved original download: patch11-tag-artifacts/.
GitHub reports archive digest sha256:38b7f74afa676afcfd3d04117fbccec6337b569590144848c3fcf583950fab47.
The lead independently verified all extracted files through the release CLI with
GITHUB_RUN_ID=39305802582. Exit0: source/version/tag/run identity and artifact
content/hashes match. Manifest SHA256: 80006e3a986ba713401587f5067c58358f320bf54a681c55d27b31055779dfcf.
Contains three gems, npm tarball, browser bundle, PHP archive, notes and manifest.
These are the new tag run's files; no local/branch/0.29.10 substitution.
Verification receipt: patch11-tag-artifact-verification.json.

Fresh Luna/low watcher completed bounded observation (wrapper0; ordinary0;tag0),
then handed pending approval ownership to lead and received acknowledgement.
Evidence: patch11-tag-status.json, patch11-tag-pending.json, final-gate/final-pending
JSON and watch logs/status. Actual registry OIDC/PHP key use remains unexercised.
After approval, use a fresh observer for publication, diagnose any failure before
retrying, and verify live registry hashes/npm metadata/PHP provenance plus
Packagist indexing. Cross-registry publication is non-atomic.
