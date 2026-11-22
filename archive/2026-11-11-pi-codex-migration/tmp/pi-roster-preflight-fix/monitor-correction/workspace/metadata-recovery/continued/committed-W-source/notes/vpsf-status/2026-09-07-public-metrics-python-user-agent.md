# Public metrics reject the default Python user agent

Initiative: `archive/2026-09-07-vpsfstatus-index-stale-2/`.

On 2026-09-07, `urllib.request.urlopen('https://status.vpsf.cz/metrics')`
returned HTTP 403 with Cloudflare error code 1010. Ordinary curl returned HTTP
200 and live metrics with `cf-cache-status: DYNAMIC`.

A focused comparison returned HTTP 200 for curl over HTTP/1.1 and HTTP/2,
HTTP 403 for curl using `Python-urllib/3.13`, and HTTP 200 for curl using
`Prometheus/3.5.0`. The Python collection failure depended on the user agent;
it did not establish that the metrics endpoint or production Prometheus scrape
was failing. Use the working ordinary curl request for direct read-only
collection and keep the client difference explicit in evidence.
