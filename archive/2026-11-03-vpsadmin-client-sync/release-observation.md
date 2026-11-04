# Phase 1 publication observation

Both native publication workflows completed successfully at the approved release
heads. TypeScript's canonical public metadata and installable tarball are now
verified against the original tagged artifact and receipt. This observation
package is complete; both utilities finished and released their capacity.

| Client | Release | Exact source head | Native run |
| --- | --- | --- | --- |
| Rust | `v0.2.0` | `49e45527a5683ffe4c03d1b46a74ac137ffa2f9f` | [41670222864](https://github.com/vpsfreecz/vpsadmin-rust-client/actions/runs/41670222864) |
| TypeScript | `v0.4.0` | `c53cb4dabb0b3aac8d05834478872d2cfa698fa7` | [41670211965](https://github.com/vpsfreecz/vpsadmin-typescript-client/actions/runs/41670211965) |

The lead reported approved integrations and tag publication. Go `v0.2.0` at
`7bc136e1` was independently verified by owner0; this observation package did not
duplicate that check.

## Native gates and terminal results

Both workflows paused at their existing protected `release` environments after
validation/build success. The watcher immediately reported their pending gates
and `current_user_can_approve=true`. The lead then approved them through the
supported pending-deployments API using the user's publication authorization:

- Rust environment `25229528835`, deployment `7523913028`, publish job
  `126038258497`, ref `v0.2.0`.
- TypeScript environment `25494232596`, deployment `7523855223`, publish job
  `126036887175`, ref `v0.4.0`.

No protection, authentication setting or publication workflow was bypassed or
changed. Final run metadata shows both workflows successful and both pending
deployment lists empty. Rust's trusted-publishing token and publication steps
succeeded; bootstrap publication was skipped. Rust retained no workflow artifacts.

The operation used a fresh `gpt-6-luna`/low utility with catalog
`495ef6620926420612ee4988e69d03a4e975e41734a1a5e3208db65fcd731db7`, native
identity `dw_af6ea530112c2a5e816254d08d217be90f4f5c713a51db96`, full-access
policy and approval `never`. It finished with no running effects or pending gates;
its capacity was released. Complete run logs and initial/final metadata remain in
[release-observation/rust](release-observation/rust/) and
[release-observation/typescript](release-observation/typescript/).

## TypeScript retained artifact

Immutable Actions artifact `13249160261`, named
`npm-package-c53cb4dabb0b3aac8d05834478872d2cfa698fa7`, retains the original
tagged tarball and receipt under
[typescript/artifacts/extracted](release-observation/typescript/artifacts/extracted/).
The receipt binds package `vpsadmin-typescript-client`, version `0.4.0`, tag
`v0.4.0` and the full source head above. Its archive identity checks pass:

- Tarball SHA-256:
  `3a6f2a2a6f4eaeb31f490035b312e9b5403cf21589d649dc1fd31d60b64e1906`.
- Receipt SHA-256:
  `e54eaf240db11b9503f90b08c51e37da1d111274cb4baf35a62cf3f04dae642c`.
- SHA-512 integrity:
  `sha512-xvTQ9z/vheBmzBxuaJ50x8YsOa8ywZdFvLH6MXy/KNNgJ9tes4v3RfhhuxIHm6MaZDeTv+NYIN22sFXLCh3Oig==`.

## Public visibility reconciliation

The exact publish log records publication to `https://registry.npmjs.org/`,
signed provenance, transparency-log entry `3674324810`, and success for
`vpsadmin-typescript-client@0.4.0` at 16:09:25 UTC. It also explicitly says:
"Your package is being processed and may take a few minutes to become available."

Initial canonical version and tarball GETs returned HTTP 404. At 16:12:49 UTC,
the full public packument still omitted `0.4.0` and reported `latest: 0.3.0`;
the canonical `0.4.0` tarball also returned 404. A cache-refreshed version lookup
at 16:13:25 UTC returned 404 with a current Date header and no Age/CF-cache-status
header. These responses establish missing public visibility at those moments;
they do not identify a CDN failure or establish a failed registry upload.
Original status evidence is retained under
[typescript/registry](release-observation/typescript/registry/).

The lead assigned a finite visibility observation: at most three scheduled
samples of the standard public full packument, version endpoint and canonical
tarball, 60 seconds apart. A new one-operation Luna/low standalone utility uses
the same pinned native instructions and explicit full-access/approval-never
flags. It retains complete response bodies, headers and hashes and compares
visible metadata/tarball to the original immutable artifact and receipt.
No publication retry, rebuild, repack, authentication workaround or settings
change is authorized by this observation. A finite unsuccessful sample batch
means incomplete public evidence, not proof of permanent publication failure.

The fresh standalone utility completed with exit 0 after 60 seconds. Its first
sample at 16:17:27 UTC saw public packument and version metadata (HTTP 200), while
the tarball still returned 404. Its second sample at 16:18:27 UTC saw HTTP 200 for
all three canonical endpoints. Public metadata's SHA-512 integrity and downloaded
tarball bytes match the original tagged artifact and receipt above. The parent
independently rechecked the saved packument/version metadata, byte equality,
SHA-256, SHA-512 and source receipt after the utility finished. No new publication
or registry mutation was needed. These observations establish delayed public
availability; they do not identify a particular CDN or processing mechanism.

Canonical public endpoints for independent verification:

- [Package metadata](https://registry.npmjs.org/vpsadmin-typescript-client)
- [Version 0.4.0 metadata](https://registry.npmjs.org/vpsadmin-typescript-client/0.4.0)
- [Original published tarball](https://registry.npmjs.org/vpsadmin-typescript-client/-/vpsadmin-typescript-client-0.4.0.tgz)

The compact [registry verification receipt](release-observation/typescript/registry/verification.json)
binds these URLs, exact source/tag, native run, immutable artifact ID and archive
hashes. Complete positive and negative response bodies, status, headers and body
hashes remain under
[observations](release-observation/typescript/registry/observations/), with the
[sample result](release-observation/typescript/registry/observations/result.json).
The [launch policy](release-observation/typescript/registry/watcher-launch.json),
event log, [watcher result](release-observation/typescript/registry/watcher-result.md),
operation log, numeric exit and elapsed-time receipts remain alongside them.
No operation or protected environment gate remains active. Phase 2 remains
lead-coordinated after consolidation of all three client release receipts.
