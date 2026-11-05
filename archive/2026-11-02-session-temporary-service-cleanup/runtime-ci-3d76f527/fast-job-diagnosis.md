# Completed fast-job download failure

Static artifact for run `41518664500`, fast job `125528690375`, runtime
`3d76f527a6b88e9d32c202f729a1a0d673b341f2`:
[job-fast-logs.zip](job-fast-logs.zip). Despite its suffix, the captured content
is UTF-8 job-log text with a BOM, 1,546 lines and the normal job-cleanup footer.
It is not a ZIP archive. Size: 159,460 bytes. SHA256:
`8ebc5556be198b571d3cdfdd52eab317287d501c71d5d6eea0e220541b8f292d`.

The supported cause is a failed cache download, with no source-build defect
shown in this artifact:

- Line 1196 starts substituting `/nix/store/94pabrw3ff2xy0kg05rgxjch2p1g6ids-codex-0.165.0` from `https://cache.numtide.com`.
- Line 1475 reports HTTP 200 with curl's “Failure when receiving data from the peer” for NAR `1iqpxz1vx81zxwbv4ir83v8nxqxxsvs6fk4mzyw8g0a3ja7j8k2p.nar.zst`, then retries from offset 139,260,422.
- Line 1502 reports the same receive failure on the resumed HTTP 206 response.
- Lines 1503–1504 report no usable substituter for the required Codex output and failed substitutes for `/nix/store/c1ql1zd4dph4f28wrlx98ilkr1m3v4dg-codex-0.165.0.drv`.
- Lines 1505–1510 fail `assemble-codex-package` and `dev-workspace-codex-package` because a dependency failed.

No compiler, source assertion, hash/signature mismatch or test failure is reported.
The artifact cannot distinguish a network interruption from a cache-side transfer
problem. The downstream “no substituter” message does not establish persistent
package unavailability.

No source or pin change is indicated. After the entire run settles, the lead can
decide a targeted retry of this failed fast job. A performed no retry, network/cache
probe, fallback build or observation of the other jobs; the lead's watcher retains
that observation. Final configuration pin/handoff was reconciled first and stays
unchanged by this diagnosis.
