# Go 0.2.0 release verification

Verified public module metadata on 2026-11-03 at 16:06 UTC. Phase 1 Go source is
integrated and release `v0.2.0` is available through the public Go module proxy.
The lead performed approved integration/publication and released the merge claim;
implementer0 performed only the bounded read-only verification below.

| Identity | Exact value |
| --- | --- |
| Module | `github.com/vpsfreecz/vpsadmin-go-client` |
| Public version | `v0.2.0` |
| Reviewed/integrated source | `7bc136e1d72f15174229bea2bb7de284174512f2` |
| Annotated tag object | `5f7c8a8e00a37dbcdddee222f059d32ec9fc91cc` |
| Peeled remote tag | `7bc136e1d72f15174229bea2bb7de284174512f2` |
| Proxy Origin.Ref | `refs/tags/v0.2.0` |
| Proxy Origin.Hash | `7bc136e1d72f15174229bea2bb7de284174512f2` |
| Proxy Origin.VCS/URL | `git`, `https://github.com/vpsfreecz/vpsadmin-go-client` |
| Proxy version time | `2026-11-03T15:38:54Z` |

Both [public version metadata](https://proxy.golang.org/github.com/vpsfreecz/vpsadmin-go-client/@v/v0.2.0.info)
and [module metadata](https://proxy.golang.org/github.com/vpsfreecz/vpsadmin-go-client/@v/v0.2.0.mod)
returned HTTP 200. The `.info` origin matches the exact independently reviewed
source and published tag. The `.mod` bytes equal the reviewed repository
`go.mod`, including `go 1.16`. Fresh `git ls-remote` over existing SSH origin
confirmed remote master, tag object and peeled tag as listed above.

The [public checksum lookup](https://sum.golang.org/lookup/github.com/vpsfreecz/vpsadmin-go-client@v0.2.0)
returned HTTP 200, record `70730200`, with:

```text
github.com/vpsfreecz/vpsadmin-go-client v0.2.0 h1:PX6DNAvmJpeehFuoWOFb3K5QaZOFJ9XKNcXHO3iBkv0=
github.com/vpsfreecz/vpsadmin-go-client v0.2.0/go.mod h1:n7aZvL8Z1XGeKF6lDkdmsfGdBOh8SiKxl07FXjpGygw=
```

Retained response hashes:

| Response | SHA-256 |
| --- | --- |
| `.info`, 204 bytes | `41e8d706ebed447211154ce3712e913af93a24c105cb84be1e39a12d4d878d37` |
| `.mod`, 56 bytes | `b6512dde7aae8cef8a81d4e3630db5194e851338c0abf2acb7b2f016b7173e2a` |
| checksum lookup, 395 bytes | `c8f93754c5a3835f06f4e8246a25d4ff667d4741d597e55912f2895d8a48498a` |

Raw responses and structured URL/status/hash evidence are retained under
[go-release-public](go-release-public/), including `public-metadata.json`.
Markdown preserves the useful release identities and sums independently of those
disposable artifacts. There was no propagation failure, tag retry or replacement.

This is public metadata/source-identity verification, as authorized by the lead.
It did not download or recompile the module zip or independently validate the
checksum database's signature. Existing generation and offline quick-check
evidence remains in [go-review-packet.md](go-review-packet.md). No source/ref
mutation, machine/deployment operation, Phase 2 rule work, cleanup or lifecycle
action occurred. Source and feature refs remain retained.
