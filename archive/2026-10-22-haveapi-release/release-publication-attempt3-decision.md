# Resume after confirmed gem publication

The user authorized completing 0.30.0; later fixes must stay on a development
branch with no further release without approval. This is recovery of the original
0.30.0 run/artifact, not a new release or new source.

Attempt 2's complete failed log and job/artifact metadata are retained. All four
gem pushes reported successful registration. The first three were confirmed;
Rust confirmation timed out after 12 missing-metadata checks. Owner2's diagnosis
binds original logs and fresh official responses without claiming unlogged
original cache behavior: `release-gem-confirmation-diagnosis.{md,json}`.

Owner2 then proved the Rust gem's official public download (44,544 bytes) and
v1/v2 metadata match original SHA-256
`3aa3e2363a533460e12cadf97bb8300c25877d524bf06ea8648f7fe744336e0a`.
Prior negative metadata response had X-Cache HIT/Age398; current metadata is
positive. These are successive observations, not proof of a specific past CDN
failure. `release-rust-metadata-visibility.{md,json}` retains the controls.

Lead independently performed one normal canonical v2 GET with no special cache
headers or query. It returned 200 with exact original Rust gem version/hash;
`release-rust-metadata-lead-normal-read.json`. Other three gem hashes and both
Python filenames/hashes are independently confirmed against the same original
tagged-run manifest. npm and PHP 0.30.0 remain unattempted/absent.

Authorize one further failed-publication-only rerun of run `39849807897`, retaining
source `b64fb25bea8d8222fb3263b99956c0b61438a859`, immutable tag `v0.30.0`,
artifact `12455689943` and original manifest SHA-256
`f75323d63fec4f3b88a70845bffc39ca4440dd0b7fd94000f95054708e0a7890`.
No source/tag movement, artifact rebuild/substitution, overwrite or account
configuration is authorized. Already matching gems/Python must be verified and
skipped. Original helper retains npm/PHP/public-release conflict defenses.

Fresh observation and destination verification follow. GitHub protected approval
must use the ordinary UI because the available API token returned 403; the
user's release authorization remains standing. Preserve another failure and
investigate before any additional retry.
