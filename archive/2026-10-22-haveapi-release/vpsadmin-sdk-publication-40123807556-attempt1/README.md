# Release observation: failed before publication

Run 40123807556, attempt 1, source `63b87e9a`, immutable tag `v0.1.0` finished with publisher failure. The exact credential-free Cargo dry-run packaged and compiled successfully. Its following Python archive inspection failed because `target/package/vpsadmin-client-0.1.0.crate` was absent. These logs do not establish Cargo’s actual temporary archive location or lifetime. Bootstrap prerequisites and native publishing were skipped. There was no upload by this run.

Full original terminal logs and exact publisher log are retained beside [result.json](result.json); see [parent-assessment.json](parent-assessment.json) for coverage, warnings and exact hashes. Candidate and native publish artifacts are absent. The previous run-specific CI package remains valid verification evidence and is not a substitute publish archive. [public-verifier-handoff.json](public-verifier-handoff.json) records this incomplete contract honestly.

The fresh watcher and its command have ended; no remote jobs remain active. Utility/runtime ownership is yielded. No retry, tag movement, source change, registry probe or lifecycle action occurred. Lead/architect must route the narrow archive-contract repair and immutable-tag recovery before another release execution. Existing successful compiler/MSRV/regeneration/package results are retained; no new test campaign was run. No project documentation change is useful for this read-only failure receipt.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-haveapi-release/)
