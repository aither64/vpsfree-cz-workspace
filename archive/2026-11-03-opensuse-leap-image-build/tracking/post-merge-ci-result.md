# Post-merge CI observation (in progress)

Expected head: `742eb30cb1a8b6766c85e915d26b0400e38244b1`.

| Run | Name | Current status | Conclusion |
| --- | --- | --- | --- |
| 41737858313 | staging CI | queued | pending |
| 41737858352 | staging changed images | queued | pending |
| 41714889091 | feature changed images | in progress | pending |
| 41714888844 | feature CI | in progress | pending; nine visible Livepatch lifecycle matrix jobs failed |

For run 41714888844, `gh run watch --compact` emitted: `Test log '/tmp/os-test-runner-109335108-41714888844-1/test.log' not found` and `Process completed with exit code 1` for the failed lifecycle jobs. The aggregate `Run test suite` job and workflow run remain marked in progress, so GitHub has not yet exposed terminal logs. The attempt to fetch failed-job logs reported: `run 41714888844 is still in progress; logs will be available when it is complete`.

Evidence: `post-merge-ci-41714888844.json` (run and job metadata), `post-merge-ci-41714888844.log` (GitHub CLI log availability responses). Four `gh run watch` processes remain active for the listed run IDs. No CI mutations were made.
