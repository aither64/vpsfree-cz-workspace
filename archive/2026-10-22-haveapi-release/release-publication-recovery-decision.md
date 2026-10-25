# Resume the original 0.30.0 publishing job

Lead accepts bounded diagnosis and authorizes **one failed-job rerun** of
`vpsfreecz/haveapi` run `39849807897`, preserving tag `v0.30.0` and source
`b64fb25bea8d8222fb3263b99956c0b61438a859`. User authorized making this release.

Evidence before retry:

- Original attempt 1 build succeeded. Its complete logs/jobs/artifact and failed
  step outputs are retained by [diagnosis](release-publication-failure-diagnosis.md).
- Official PyPA upload logs show HTTP 200 for both exact Python distributions.
  The helper's single-read completeness guard failed about two seconds later.
  A fresh official PyPI JSON response now returns exactly both expected names
  and original manifest hashes. This supports immediate metadata incompleteness
  after upload; the original HTTP response is unlogged, so a specific 404,
  partial response or cache cause is not claimed.
- The [independent partial inventory](release-partial-destinations.md) confirms
  all four gems/npm version absent, PHP mirror unchanged at 0.29.12, and no
  public release. Private draft assets are unreadable to this API credential;
  attempt 1 successfully prepared them and the helper checks them on retry.
- Original retained artifact `12455689943`, `release-39849807897`, remains intact.
  Lead downloaded its eleven files into `official-release-39849807897/`, verified
  exact schema/source/version/tag/run and every catalog SHA-256, then passed the
  existing package verifier in the declared Nix environment (exit 0).
  [Inventory](release-official-candidate-inventory.json),
  [verifier log](release-official-candidate-verify.log).
- Manifest SHA-256 is
  `f75323d63fec4f3b88a70845bffc39ca4440dd0b7fd94000f95054708e0a7890`.
  No artifacts are substituted from a local or branch build.
- GitHub approval history shows environment `release` approved by `aither64` in
  attempt 1; lead issued no approval then. Renewed ordinary approval, if needed,
  remains covered by the user's publication authorization and this exact-byte
  acceptance. No environment protection bypass or configuration change.

Repository recovery explicitly permits rerunning failed publishing jobs with
original artifacts. `gh run rerun 39849807897 --failed --repo vpsfreecz/haveapi`
will retry only failed publication; build must remain the successful original
job and artifact ID. Existing matching Python files must be verified and skipped.
The helper must refuse changed/conflicting registry bytes rather than overwrite.

A fresh Luna/low watcher observes attempt 2. No cancellation, blind retry,
source correction, new release/tag, rebuild or registry/account changes are
included. A further failure is preserved and diagnosed before any further action.
