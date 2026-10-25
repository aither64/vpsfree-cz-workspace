# SDK registry 403: bounded observation and resume decision

Architect0, 2026-10-24; assignment `d4d4ce03-42d4-43a8-b22e-52207d46b5ab`.
Session binding and ready/Astra/xhigh/design/workspace-write settings verified.
Existing source procedures and exact owning workflow were read; no app execution.

**Conclusion:** the API 403 cause remains unknown. The single authorized sparse
read returns index absence, but from a response cached for about 30 minutes.
Do not describe it as fresh origin/exact-version absence or silently substitute
it for the stopped launcher's fresh-absence assertion. A single targeted read
of the workflow's actual crate-name endpoint is the smallest remaining useful
diagnostic; it requires lead routing, not another user publication/tag approval.

## Retained request and actual new observation

The stopped launcher's exact-version API request at 20:12:29.914507 UTC was
`GET https://crates.io/api/v1/crates/vpsadmin-client/0.1.0`. Its declared curl is
`/nix/store/x5ad8l4zpkg2dldjyqsknlcyypjmp0wp-curl-8.22.0-bin/bin/curl`, SHA-256
`e8222f4e3fa998fe9ba30c13e968412ef97d5aa82ceff93fb768d768537d9baf`.
`--disable` is the first option; HTTPS/TLS, 45-second limit and zero redirects
are explicit. No retry, authentication, netrc or custom user-agent option is
present. The subprocess receives only PATH, SSL_CERT_FILE and LANG: no inherited
proxy/auth environment. The URL and method match the intended public endpoint;
no request mistake is established.

Retained HTTP/2 403 headers show `content-length: 0`, `cache-control: no-store`,
`via: 1.1 varnish`, `x-cache: MISS`, and `cache-fra-etou8220024-FRA`. The empty
body hash is `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.
This proves neither absence nor an expired/invalid registry credential. There
was no credential in this request. CDN policy, rate limiting or user-agent
classification are possible explanations, **not findings**; no auth repair is
justified. Original evidence is unchanged under
`vpsadmin-sdk-recovery-release-b6f84679-to-pending/`.

One distinct canonical input was read using that same hash-verified curl and
minimal environment, no redirects/retries or authentication:

| Fact | Observation |
| --- | --- |
| Endpoint | `https://index.crates.io/vp/sa/vpsadmin-client` |
| Start / finish UTC | 20:15:34.813029 / 20:15:34.947522 |
| Native exit / HTTP | 0 / HTTP/2 404 |
| Cache | `x-cache: HIT`, `age: 1798` |
| Server / response type | AmazonS3 / application/xml |
| Body | 292 bytes, SHA-256 `88361616a8b4ce77f3950b8d37df111fb0e83293a378e91503424d2ba1627a58` |

[Observation and exact command](sdk-registry403-sparse-index/observation.json)
retain times, status, allowlisted response headers and hashes. No index record
was returned. The non-record body was hashed without retaining its text. No
other registry/API GET or native package operation was performed by architect.

The [Cargo index contract](https://doc.rust-lang.org/cargo/reference/registry-index.html)
maps this crate to `vp/sa/vpsadmin-client`; sparse files contain per-version
records/checksums. A nonexistent crate may return 404. Cargo also documents CDN
invalidation delays. This response is a current observation of a cached negative,
not proof that a newer publication could not exist. The lead's retained independent
20:02:30 API 404 (receipt prefix45c51d6b) and the proven absence of any session upload
strengthen the history; neither converts the later 403 into absence.

## Unchanged workflow boundary

At reviewed b6f84679, `.github/workflows/release.yml` first checks the bootstrap
secret's presence as a boolean, then uses Python `urllib.request` on the GitHub
Ubuntu runner to GET **`https://crates.io/api/v1/crates/vpsadmin-client`**, with
explicit `User-Agent: vpsadmin-rust-client-release` and timeout 30 seconds.
Only HTTPError 404 passes. HTTP 200, 403, other HTTP errors and network failures
stop before the bootstrap token is supplied to native Cargo.

This uses the same API hostname, but a different path, user agent, HTTP client
and execution network from the stopped local curl. Python's default redirect/
proxy handling is not explicitly overridden, and no cache-control or retry loop
is configured. No claim is made about its runner environment values. The local
403 may or may not recur there; the evidence cannot predict it. Do not weaken
this HTTP-404 predicate or change the workflow based on the index observation.

## Narrow next package

1. Lead may route **one** unauthenticated GET of the crate-name API URL above,
   with the existing qualified curl, the workflow's explicit user agent, the
   same minimal no-auth/no-proxy environment, no redirect/retry, and 45-second
   bound. An explicit `Cache-Control: no-cache` request is appropriate to seek
   revalidation; record it, and do not assume the server honored it. Retain
   status, Date/Age/cache headers and public body/hash. This is not an upload,
   token check or attempt to bypass a 403 with authentication. Not executed here.
2. If that ordinary API read returns a usable 404 without evidence of an older
   unrevalidated cache result, lead can accept it as a crate-name absence
   observation and bind it to a fresh session-only owner3 resume packet. It
   establishes neither name ownership nor transaction-wide atomicity. Preserve
   both old 403 and aged-index evidence. For 200, parse exact name/version facts
   and stop automatic bootstrap; for another error, preserve the failure and
   return to lead without polling or trying alternate credentials/endpoints.
3. The new packet must keep b6f84679 source/tree, all accepted review/CI/native
   inputs, exact old annotated tag object/source and one-time user exception
   bound. Recheck source/remote refs through the ordinary sole-owner path,
   preserve the old tag lineage, and perform only the already-authorized tag
   movement and dispatch after the accepted guard. Do not reset/reuse the
   stopped one-shot marker or revise its no-effects receipt.
4. The actual protected workflow still performs its independent bootstrap
   HTTP-404 guard and native immutable-version checks. A later 403 stops there;
   do not auto-retry or rewrite workflow behavior. Public verifier1 still needs
   actual native publish archive/checksum evidence after any successful upload.

If lead instead elects to accept the cached index negative solely as a
pre-dispatch operational observation, that would be an explicit change to the
launcher acceptance contract, **not equivalent fresh API proof**. This brief
recommends the single matching-endpoint read first because the same API service
is still a mandatory upload prerequisite and the cached response is older than
the retained API observation. No broader investigation or source change is needed.

User tag-movement authority remains valid. SDK main integration, new version,
credential changes, deployment and lifecycle actions are outside this package.
Original v0.1.0/ref state and source were not changed by this investigation.
