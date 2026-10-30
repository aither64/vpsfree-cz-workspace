**Result: publication workflow succeeded; npm registry availability remains uncertain.** Run 41059048868 completed successfully for source `e5786f69b7c223c3bb5b1de99b7f97186eec368a`, tag `v0.2.0`. Total run time was about 5m 48s; the publish job took about 33 seconds.

The `publish` job’s “Verify and publish the approved archive” step succeeded. Its log says npm accepted `vpsadmin-typescript-client@0.2.0` and that the package “may take a few minutes to become available.” The read-only version endpoint returned HTTP 404 (“version not found: 0.2.0”), so registry availability is not yet confirmed. No upload was attempted.

Evidence is saved under `/home/aither/workspace/ai/vpsfree.cz/work/2026-10-30-haveapi-client-releases/typescript-publication-41059048868/`:

- [Run and job summary](</home/aither/workspace/ai/vpsfree.cz/work/2026-10-30-haveapi-client-releases/typescript-publication-41059048868/summary.json>)
- [Full workflow log](</home/aither/workspace/ai/vpsfree.cz/work/2026-10-30-haveapi-client-releases/typescript-publication-41059048868/run.log>)
- [Job metadata](</home/aither/workspace/ai/vpsfree.cz/work/2026-10-30-haveapi-client-releases/typescript-publication-41059048868/jobs.json>)
- [Deployment records](</home/aither/workspace/ai/vpsfree.cz/work/2026-10-30-haveapi-client-releases/typescript-publication-41059048868/deployments.json>) show deployment 7438799627 for `release`, ref `v0.2.0`, and the specified source SHA.
- [Registry 404 response](</home/aither/workspace/ai/vpsfree.cz/work/2026-10-30-haveapi-client-releases/typescript-publication-41059048868/registry.json>), [response headers](</home/aither/workspace/ai/vpsfree.cz/work/2026-10-30-haveapi-client-releases/typescript-publication-41059048868/registry-headers.txt>), and [package metadata snapshot](</home/aither/workspace/ai/vpsfree.cz/work/2026-10-30-haveapi-client-releases/typescript-publication-41059048868/registry-package.json>) are retained. The snapshot did not contain version `0.2.0`; no public tarball or registry dist integrity was available to record.

The original accepted tag artifact was left unchanged. Its receipt is at `/home/aither/workspace/ai/vpsfree.cz/work/2026-10-30-haveapi-client-releases/typescript-tag-41059048868/artifact/receipt.json` (SHA-256 `a0fdad3e6cd4c3d6a13c0a3e7384d9d6910e31a1a9390167ad39876b4509decd`). No operation remains running.