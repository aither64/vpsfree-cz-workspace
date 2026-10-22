# HaveAPI 0.29.12: completed publication approval

Status: aither64 approved release; run39313082898 completed successfully and all
publication destinations passed verification. This approval checkpoint is
historical. Current result: [execution record](release-0.29.12.md) and
[verification receipt](patch12-publication-verification.json).

## Original pre-publication checkpoint

Master fixc58704a is integrated and release355c299 is the annotated v0.29.12.
The user authorized both target integrations and the new version. The tag run
has passed its tests, package build and original-artifact checks, and now awaits
human approval by aither64 in the protected release environment.

Open [Actions run 39313082898](https://github.com/vpsfreecz/haveapi/actions/runs/39313082898),
choose Review deployments, select release, then Approve and deploy to authorize
registry publication and PHP mirror synchronization. The lead has not submitted
an environment approval. Until that happens publication remains pending.

All seven ordinary tag workflows pass: server39313083110, Ruby39313083098,
Go39313083068, JS39313082925, PHP39313082918, i18n39313082941, RuboCop39313083014.
Tag run39313082898 build job is successful; pending-deployment response names release
and revieweraither64. The fresh Luna/low observer returned0 at this boundary,
transferred responsibility to the lead and finished. No verification process
remains running. Evidence: patch12-ci-results.json, patch12-tag-final-gate.json,
patch12-tag-final-pending.json, patch12-watch-wrapper.status and observer logs.

Original Actions artifact12217296363, release-39313082898,702386bytes, archive digest
sha256:cf9d43f8a216c759f5d6ddea7c4963c2dd2780648055f5f59bf2225c04d1c78d.
Saved unmodified in patch12-tag-artifacts/. Its manifest binds exact source
355c2990a4bfd3940d3234cb2077ad0127f43551 /version0.29.12 /tagv0.29.12 /run39313082898.
Manifest SHA256563ed9d468a5357a8a290a0e5ef6f6a973b844fd5b9b0db443b7ea732797a00c. Parent independently rehashed all7files and ran the
repository CLI verifier with GITHUB_RUN_ID=39313082898; both pass. Receipt:
patch12-tag-artifact-verification.json. The local pre-tag packages are separate;
no original was rebuilt or substituted. Both earlier failed sources/artifact
sets remain preserved.

Actual registry OIDC, PHP deploy-key push rights and Packagist indexing remain
first-publication checks. Publishing is non-atomic across destinations; diagnose
any failure and preserve these exact originals before retrying. A source change
needs another authorized version. Session stays open.
