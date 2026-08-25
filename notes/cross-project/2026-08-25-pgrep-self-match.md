# Avoid matching a polling command with `pgrep -f`

## Symptom

A loop waiting for a VM test state directory kept reporting the test as active
after its test-runner and QEMU processes had exited.

## Cause

`pgrep -f '/tmp/example-state'` also matched the polling shell because the
literal search string appeared in that shell's own command line.

## Workaround

Use a regular expression that matches the target but not its literal spelling
in the poller, for example `pgrep -f '/tmp/[e]xample-state'`. Verify the final
state with a separate process listing and shared-memory usage check.

## Verification

The self-excluding expression stopped matching the poller and correctly showed
that the original VM test had exited. Related initiative:
`work/2026-08-24-crashdump-optimization`.
