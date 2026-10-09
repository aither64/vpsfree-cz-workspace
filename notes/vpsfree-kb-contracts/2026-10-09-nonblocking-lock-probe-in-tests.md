# A lock probe can interfere with a nonblocking operation

The delayed-shutdown machine fixture started public `Engine.stop`, then repeatedly
acquired the same operation lock with `wait:false` to detect that the stop had
begun. Public stop also acquires that lock nonblocking. The probe can take the
lock first and make the operation return Busy; the probe then waits for a lock
that remains free. The five-second timeout hides the waiter's actual result.

K Check37990835413 at09229a73 timed out in that probe, while a same-head runtime
Check passed. Its native log did not record the waiter result, so this exact
scheduling is an inference, not a reproduced native cause.

The bounded correction uses a per-fixture wrapper around the real authenticated
control call. It signals after the actual acknowledgement and preserves the
returned handoff. It must surface waiter failures without contending for the
operation lock, extending timeouts or bypassing public stop. Both exact replacement source Checks passed at K922e71e5; machine19/667
including the original delayed cases has zero failures/errors/skips. This
verifies the correction without proving the old native scheduling inference.

Session: work/2026-10-05-network-ipv4-left-counter/state.md.
