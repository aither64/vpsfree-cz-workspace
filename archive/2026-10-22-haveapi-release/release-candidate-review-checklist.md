# Tagged candidate acceptance before publication

Authorized release: HaveAPI `v0.30.0`, exact source
`b64fb25bea8d8222fb3263b99956c0b61438a859`, tag object
`81a896f97b75781f62c5850a6e8df7932c92782b`, tagged workflow run
`39849807897`. User authorized making the release and confirmed new RubyGems/PyPI
publishers; the protected reviewer approval remains a separate workflow action
to perform after inspecting its concrete candidate.

Before approval, lead must establish:

- Run identity is exact source, push event and `v0.30.0`, with successful
  validate/test/build job and no failed required tag/master workflow.
- Retained original artifact is uniquely named `release-39849807897`, not
  expired, and comes from this exact run/source. Preserve its artifact ID and
  archive digest; download into a new session directory, retaining local final
  and earlier artifacts separately.
- `release-manifest.json` has schema 1, version `0.30.0`, tag `v0.30.0`, source
  equal to the reviewed commit and `run_id` equal to `39849807897`.
- All ten catalog files match their manifest SHA-256 values; inspect package
  identities/dependencies and the candidate release notes with the existing
  read-only verifier in the declared tools-only root Nix environment.
- Record the exact original manifest SHA-256 and eleven candidate file hashes
  (ten catalog files plus manifest). CI build outputs can differ from earlier
  local artifacts; the tagged run's retained files alone become approved bytes.
- Pending protected deployment is environment `release`, ID `24722193856`, and
  the authenticated required reviewer can approve. Use ordinary approval only;
  do not bypass protection. If API access refuses, request the exact browser
  approval with its run link and report the API refusal.

Approval grants publication of this retained artifact set through the existing
workflow; it does not permit a rebuild, source/tag movement or an unrelated
release. Preserve failures and partial outputs. Diagnose before any retry;
follow the source-tag/artifact recovery contract if publication is partial.

The fresh verification watcher observes only; the lead owns candidate acceptance
and protected approval. Implementer1 verifies destination hashes and PHP/GitHub
Release/Packagist after the publishing result. No session lifecycle action.
