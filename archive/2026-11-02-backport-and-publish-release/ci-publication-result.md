Result: **passed** for the two assigned runs on `1ef9b204ba45bb261d3334be5c555cc1856b713b`.

- Tagged release run [41529223599, attempt 1](https://github.com/vpsfreecz/haveapi/actions/runs/41529223599): **success**. Build and publish jobs succeeded; the protected release had already been approved. The final [GitHub Release v0.32.2](https://github.com/vpsfreecz/haveapi/releases/tag/v0.32.2) is published with 12 uploaded assets, including the original approved artifact `13181726847`.
- Build-only run [41528866548, attempt 2](https://github.com/vpsfreecz/haveapi/actions/runs/41528866548): **success**. Its publish job was skipped. The earlier attempt 1 failure is historical and was not counted as the current result.

The publication log confirms PyPI `haveapi-client 0.32.2`, RubyGems packages (`haveapi-client`, `haveapi`, Go, Rust, and TypeScript clients), and npm `haveapi-client 0.32.2`. It records PHP tag `v0.32.2` at source commit `f6b7f98` and says Packagist indexing follows its configured webhook. I did not independently verify public registry usability.

Evidence is retained in [ci-publication-evidence](/home/aither/workspace/ai/vpsfree.cz/work/2026-11-02-backport-and-publish-release/ci-publication-evidence), including the full run and publication-job logs, final run metadata, and GitHub Release asset metadata. The publication job ran from 21:42:21 to 21:46:34 UTC.