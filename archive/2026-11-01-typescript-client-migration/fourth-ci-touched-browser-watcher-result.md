The single authorized browser operation finished with **exit 1** on HEAD `b1b37ccf5dc5d000baed3d77d49fab6f5b84b663` after 35.091 seconds: 6 passed, 1 failed, 1 interrupted, and 128 did not run. It stopped at the configured maximum of one failure.

The first failure was `vps_power_stop_confirm.spec.ts:85`; its assertion expected the request body to equal `{}`. The trace and interrupted case are recorded in the observer log and artifact directory.

Compact raw evidence is saved at [fourth-ci-touched-native-result.md](/home/aither/workspace/ai/vpsfree.cz/work/2026-11-01-typescript-client-migration/fourth-ci-touched-native-result.md). No retry, diagnosis, or cleanup was performed.