# CI observation handoff

- Exact head: `1a637e9eac4311adba2b08d60dfa7a17d07bcb52`
- Image workflow run [41695651867](https://github.com/vpsfreecz/vpsadminos/actions/runs/41695651867): OS closure build and changed image script detection passed; `Build and test changed images` job 126192300407 remains queued. No selected image names or per-case summary are available yet.
- Generic CI run [41695511680](https://github.com/vpsfreecz/vpsadminos/actions/runs/41695511680): `Run test suite` job 126191147285 remains in progress; plain Intel lifecycle job 126191147653 remains queued. Six AMD and two Intel representative lifecycle jobs failed on the same `livepatch_7-exact-candidate.ko.drv` builder failure as baseline `dd188397` (architect comparison); these are failed checks, not passes.
- Raw job logs for representative failures are `ci-job-126191147517.log`, `ci-job-126191147584.log`, `ci-job-126191147641.log`, `ci-job-126191147559.log`, and `ci-job-126191147819.log`. Job-specific artifact for 126191147517 is under `ci-artifact-126191147517/`.
- Full status observation log: `ci-wait.log` in this initiative directory.
- Observation ended at the lead's handoff request. Existing CI jobs were not canceled, retried, or changed.
