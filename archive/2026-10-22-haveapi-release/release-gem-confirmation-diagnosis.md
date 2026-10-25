# Attempt 2 RubyGems confirmation diagnosis

Implementer2, bounded read-only observation on 2026-10-22. Session/environment
and saved workspace-write access matched before work. Required release and
verification/Git guidance remains applicable. Complete fresh response bodies,
status/headers, hash comparisons and retained evidence metadata are saved in
[release-gem-confirmation-diagnosis.json](release-gem-confirmation-diagnosis.json).

## Exact operation and original artifacts

- Source/tag: `b64fb25bea8d8222fb3263b99956c0b61438a859`, `v0.30.0`.
- Run `39849807897`, attempt 2, completed/failure. Retained publish job
  `120078714229` failed; original build job `120078715920` succeeded.
- Original artifact `12455689943`, `release-39849807897`, remains unexpired in
  retained attempt-2 metadata. Its original local directory is
  `official-release-39849807897`; its manifest records the same source/tag/run.
- Complete failed publication log remains unchanged:
  [attempt 2 log](release-recovery-watch-run39849807897-attempt2-log-failed.txt).
  Complete job/step and artifact metadata remain in
  `release-recovery-watch-final.json`, `release-recovery-watch-final-result.json`
  and `release-recovery-watch-final-artifacts.json`. The diagnosis JSON preserves
  these metadata bodies and SHA-256 identities of all cited evidence, including
  the original manifest and log. No original evidence was overwritten.

## Logged upload and confirmation sequence

| Gem | Successful registration logged (UTC) | Confirmation logged (UTC) |
| --- | --- | --- |
| `haveapi-client` | 20:46:14.232 | 20:46:14.433 |
| `haveapi` | 20:46:16.212 | 20:46:21.528 |
| `haveapi-go-client` | 20:46:22.504 | 20:46:32.640 |
| `haveapi-rust-client` | 20:46:33.617 | None; confirmation timeout at 20:47:34.281 |

The final helper reports `Publication was not confirmed by the registry; rerun
with the retained artifacts`. This is a diagnosis of that failure, not a rerun
instruction. Lead reports existing Python files were verified and uploads
skipped; no PyPI probes were duplicated here. npm/PHP publication was not reached.

## Confirmation boundary

`utils/release/publish.rb#registry_json` returns nil only on HTTP 404; other
unsuccessful HTTP statuses raise. `gem_present?` queries the exact RubyGems version
endpoint, returns false for missing metadata, requires its `sha` to equal the
original manifest's gem SHA-256, and raises immediately on a hash conflict.

`confirm` makes up to 12 checks. Every false result is followed by a five-second
sleep, including the final false result, then it raises the observed timeout.
The roughly 60.66 seconds after Rust registration fit that bounded window.
Under this code, a non-404 HTTP error, transport exception or hash conflict would
raise instead of producing this final timeout. Individual original response
status/header/body values were not logged, so their exact contents and any
underlying visibility/cache cause cannot be independently established here.

## One fresh official metadata pass

All hashes below are the exact original run manifest's values. The three HTTP
200 responses return those same SHA-256 strings; Rust has no metadata hash to
compare because its exact version endpoint still returns 404.

| Gem 0.30.0 | Current response | Original SHA-256 / comparison |
| --- | --- | --- |
| `haveapi-client` | HTTP 200 | `6c3cddfaeb7403476f4791f33d6138dbdd9a3d3493e1bca824c5c92245098de8` — matches |
| `haveapi` | HTTP 200 | `c83fdb6ef243015c2e2563931787132f15c297f19a4c4956703f15d4a99b427e` — matches |
| `haveapi-go-client` | HTTP 200 | `58a64586643b8d9b6f3762f96127d946f91c613cac2fe7685b76e0e726b16f18` — matches |
| `haveapi-rust-client` | HTTP 404 | Expected `3aa3e2363a533460e12cadf97bb8300c25877d524bf06ea8648f7fe744336e0a`; unavailable, no observed conflict |

One fresh npm version request returned HTTP 404, and one PHP mirror `v0.30.0`
tag-ref request returned HTTP 404. These direct observations bind their current
unreached state without relying only on workflow ordering. Previous partial
destination inventory remains historical and unchanged.

## Yield

Current evidence establishes three matching published gem metadata entries and
a still-unavailable Rust version metadata entry following its logged successful
upload. It does not establish a conflicting Rust artifact, a particular cache
cause, or that reupload is necessary or safe.

Lead owns any separately authorized metadata wait or failed-job resume. No
polling, automatic rerun, source fix, registry/ref/config/credential mutation,
build/test/install or artifact download occurred. Original bytes and all earlier
logs/receipts remain untouched. No command remains active for this diagnosis.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-haveapi-release/
