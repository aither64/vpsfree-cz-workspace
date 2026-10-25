# Tagged publication attempt 1: Python verification boundary

**Both Python files were uploaded and now match the original tagged-run bytes.**
The publishing helper failed at its immediate, single-read PyPI completeness
check before RubyGems/npm pushes, PHP synchronization or public Release
completion. The evidence supports transient metadata incompleteness after
successful upload; the original HTTP status/body was not logged, so a specific
404/CDN event cannot be proved. No naming, identity, hash or OIDC configuration
conflict is observed.

## Exact source and preserved evidence

- Repository/tag/source: `vpsfreecz/haveapi`, `v0.30.0`,
  `b64fb25bea8d8222fb3263b99956c0b61438a859`.
- [Run 39849807897, attempt 1](https://github.com/vpsfreecz/haveapi/actions/runs/39849807897):
  terminal failure. Build job `120072628557` succeeded; publish job
  `120075071682` failed.
- Original Actions artifact **12455689943**, **release-39849807897**, retained
  and unexpired; archive digest
  `38a9e7e0308acd56ff3637a5c28df8660d70cdec648912b0511266a6db7fb26c`.
- Used only `official-release-39849807897/` original artifacts. Manifest SHA-256
  `f75323d63fec4f3b88a70845bffc39ca4440dd0b7fd94000f95054708e0a7890`,
  source/run fields agree with the original tag/run.
- Full official attempt archive retained in
  `release-publication-failure-39849807897-attempt-1-logs.zip`; all entries also
  preserved in `release-publication-failure-39849807897-attempt-1-full.log`.
  Exact run/jobs/artifact API responses and the preflight/PyPA/final-helper step
  logs are retained separately. They contain GitHub-masked credential fields;
  no credential contents were requested or read.
- Detailed receipt: [release-publication-failure-diagnosis.json](release-publication-failure-diagnosis.json).
  One fresh official PyPI response, including headers and complete metadata:
  `release-publication-failure-pypi-once.json`.

Lead's approvals-API receipt records environment **24722193856** approval by
user **aither64**, empty comment. The lead did not submit approval; this was the
user's external approval.

## Successful steps and failure timeline

| Step | Result/time (UTC, 2026-10-22) |
| --- | --- |
| Validate/test/build and original artifact verification | Success; build completed 20:37:45 |
| Download approved artifacts | Success |
| Verify artifacts and retain draft Release assets | Success, 20:39:24 |
| Configure RubyGems OIDC | Success, 20:39:24; credential setup does not establish gem upload |
| Preflight registries and stage missing Python files | Success, 20:39:29 |
| Official PyPA OIDC upload | Success, completed 20:39:52 |
| Final publish helper | Failed at 20:39:54.1637367 with `PyPI publication is incomplete; upload the retained Python artifacts first` |

The original PyPA log prints the correct filenames and original SHA-256 values,
then records successful upload responses:

- Wheel upload response **200 OK**, `20:39:51.3338379Z`.
- Sdist upload response **200 OK**, `20:39:52.2947756Z`.
- Final helper starts `20:39:52.4345528Z`, fails about 1.87 seconds after the
  second upload response. No intervening rebuild or new Python bytes.

The SSH `Unsupported option "gssapiauthentication"` warning occurs before the
PyPI guard. It did not stop the clone or PHP preflight: execution reached the
specific later Python completeness error. It is not the immediate failure.

## One fresh official PyPI check

GET `https://pypi.org/pypi/haveapi-client/0.30.0/json` once, observed
**20:42:36 UTC**: HTTP **200**, identity **haveapi-client / 0.30.0**, exactly the
two expected files, no extras/duplicates. Both remote hashes equal the original
manifest and locally rehashed original files:

| File | SHA-256 (original manifest = retained file = PyPI) |
| --- | --- |
| haveapi_client-0.30.0-py3-none-any.whl | `90af1ca01d4bde30bf6cea681a6fb74cd820ac0c308dfe249f679784c58552b7` |
| haveapi_client-0.30.0.tar.gz | `312ce9d921aca907c57143ee627d8864278140dd92a19323977f9f5c025cd962` |

PyPI upload timestamps are `20:39:50.195159Z` and `20:39:51.481707Z`.
The later metadata response has `Cache-Control: max-age=900, public`,
`X-Cache: MISS, HIT, HIT`, and serial `42611876`. These show that the endpoint is
cacheable; they do not reconstruct the earlier helper's response or prove which
cache layer was stale.

## Helper interpretation and exact limits

`Publisher#registry_json` returns nil on HTTP 404, otherwise requires HTTP success
and parses JSON. `pypi_files` returns `{}` for absent metadata, checks exact
name/version, rejects unexpected/duplicate filenames and immediately rejects
hash mismatches. The final `publish` guard raises the observed message only
when the expected filenames minus confirmed filenames is nonempty.

Thus the actual helper read saw either absent metadata (404) or a successful
but incomplete file list. An identity/hash/unexpected-filename mismatch would
have produced a different error. No HTTP status/body/cache details from that
read are present in the logs. The source contains no retry or propagation wait
around this guard, even though its later gem/npm confirmation uses bounded
rechecks. Calling this a confirmed specific CDN 404 would exceed the evidence.

PyPI is a confirmed partial publication. This failed helper never reached
`publish_registries`, `sync_php` or `finish_github`; no gem/npm/PHP write or public
Release completion was attempted by that helper after the guard. Implementer2
independently maps other destination state; this owner did not duplicate those
queries. Draft asset preparation succeeded earlier and must be retained.

No rerun was issued or authorized by this diagnosis. Lead must reconcile the
other destinations and original artifact evidence before deciding recovery.
The unchanged helper's preflight should recognize these now-matching Python
files and stage no Python uploads, but that is a source-derived expected recovery
path, not an executed result or automatic rerun instruction. Preserve the tag,
original run/artifacts and draft; never rebuild/replace these published Python
bytes. Any source patch requires the release recovery/design boundary rather
than changing the tagged workflow in place.

Session binding matched. All operations were read-only metadata/log downloads
and hashing; only session evidence files were written. No source, refs, accounts,
registries or configuration changed; no tests/build/listener or polling ran.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-haveapi-release/
