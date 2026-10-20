**Result: failed** — exit status `1`. The isolated VM test `vpsadmin-events` failed after 72.64 seconds. I did not diagnose or retry it; CI observation was not started.

- Tested revision: `94ac4eb5a7caf0456fff7df86a44cae198463276`
- Command: the supplied `run-isolated-verification.sh`, run once
- Elapsed time: about 2 minutes
- Status and log: [isolated-runtime.exit](/home/aither/workspace/ai/vpsfree.cz/work/2026-10-19-security-advisory-notifications/isolated-runtime.exit), [isolated-runtime.log](/home/aither/workspace/ai/vpsfree.cz/work/2026-10-19-security-advisory-notifications/isolated-runtime.log)
- Test state: `/tmp/2026-10-19-security-advisory-notifications-94ac4eb-isolated/os-test-vpsadmin-events-8aba1688`

The log records: “Test ‘vpsadmin-events’ failed after 72.64 seconds.” No owned operation remains running.