# Isolate tests that replace osctld

Related initiative: `work/2026-07-24-ct-start-hang/`

## Symptom

`kernel/vpsadminos` failed in apparently unrelated uptime, memory, tmpfs,
loadavg, and OOM scripts. Logs showed commands racing with a missing
`/run/osctl/osctld.sock` and transient container start failures.

## Cause

Test scripts in one test definition share its machines and run concurrently up
to `testScriptJobs`. CPU-view coverage stopped, replaced, or restarted
`osctld` to test legacy adoption and policy reconstruction while sibling
scripts were using the same machines.

The test runner has a per-test script-job limit but no per-script exclusivity
setting.

## Resolution

Put scripts that intentionally disrupt a machine-wide daemon in a separate test
definition with dedicated machines. Do not accept a rerun as evidence that
cross-script daemon interference is harmless.

Verification for this instance is recorded in the initiative state.
