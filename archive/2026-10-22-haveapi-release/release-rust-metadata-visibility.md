# Rust gem metadata visibility controls

Implementer2, bounded read-only observation at 2026-10-22 20:52:22 UTC. Session
current/environment and saved ownership were reverified. Original tag/head,
run/artifact and prior observations remain unchanged. Complete URLs, safe request
headers, response headers, metadata bodies and payload hash are retained in
[release-rust-metadata-visibility.json](release-rust-metadata-visibility.json).

## Exact artifact binding

Source `b64fb25bea8d8222fb3263b99956c0b61438a859`, tag `v0.30.0`, run
`39849807897`, artifact `12455689943`, original directory
`official-release-39849807897`. Expected Rust gem SHA-256 from that manifest:

```text
3aa3e2363a533460e12cadf97bb8300c25877d524bf06ea8648f7fe744336e0a
```

## One-shot official-host observations

All requests used public HTTPS at `rubygems.org`, without credentials or a
private/alternate origin. Each endpoint/control was requested once.

| Request | HTTP/cache response | Result |
| --- | --- | --- |
| Canonical `/api/v2/rubygems/haveapi-rust-client/versions/0.30.0.json`, request `Cache-Control: no-cache` | 200; `X-Cache: HIT`, `Age: 155` | Correct package/version and original manifest SHA. Response cache policy `max-age=60, public`. |
| `/api/v1/gems/haveapi-rust-client.json` | 200; `MISS`, `Age: 0` | Correct package/version and original manifest SHA. |
| `/api/v1/versions/haveapi-rust-client.json` | 200; `MISS`, `Age: 0` | Contains 0.30.0 with original manifest SHA; `created_at: 2026-10-22T20:46:33.047Z`. |
| `/downloads/haveapi-rust-client-0.30.0.gem` | 200; `HIT, HIT`, `Age: 348` | Downloaded once into memory: 44,544 bytes, SHA-256 exactly matches original manifest. Only size/hash retained; original local artifacts untouched. |
| Paired v2 URL with unique `visibility_probe=b85abd743dd140f08cfa10877d00b679` query | 200; `MISS`, `Age: 0` | Same correct package/version and original manifest SHA. |

The payload is published and the exact canonical v2 metadata endpoint is now
visible with the expected hash. No conflict was observed.

## Cache evidence and limits

The previous snapshot at 20:49:46 UTC returned canonical v2 HTTP 404 with
`X-Cache: HIT`, `Age: 398`, response `Cache-Control: no-cache`, and body
`This gem could not be found`. That response's stated age predates the successful
Rust registration at 20:46:33. The prior snapshot is retained unchanged in
[the gem confirmation diagnosis](release-gem-confirmation-diagnosis.json).

These observations establish a cached negative after upload and later matching
public metadata/payload. The current canonical response is itself a cache HIT;
the unique-query response is a public cache MISS. There was no simultaneous
canonical-404/unique-query-200 pair. Do not infer that the no-cache request caused
recovery, that the MISS bypassed every backend cache, or that the exact original
12 confirmation responses had a known cache/origin cause. Those responses were
not logged. Preserve the distinction between current visibility and the earlier
confirmation failure.

Concrete evidence was sent directly to architect0 for future design work; no
additional probes were requested. This diagnosis does not authorize changing
publisher acceptance filters, relaxing hash checks, purging caches, reuploading
or rerunning a job.

## Yield

Lead owns any separately authorized failed-job resume. No source, registry, ref,
configuration, credential or cache mutation occurred; no repeated polling,
PyPI probe, build/test/install or application change occurred. Only the explicitly
authorized public gem download was performed, and only after HTTP 200 was its
payload hashed. No command remains active for this observation.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-haveapi-release/
