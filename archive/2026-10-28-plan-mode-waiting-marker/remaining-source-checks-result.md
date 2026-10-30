# Remaining source checks result

- Revision: `5f4f1c1c52cc009970a2697f5dbc330c0a4dd7a3`
- Exact archive derivation: `/nix/store/vz97cs3j9qy94sv4pa1z0pqqgfp2ad4f-vm-test-run-dev-workspace-session-archive-lifecycle.drv`
- Result: failed, exit 1, approximately 17 minutes.
- Output expected: `/nix/store/dl2zyvy4q9n2yj76yw1q94x041zna1ym-vm-test-run-dev-workspace-session-archive-lifecycle`
- The archive browser acceptance failed during its open-page phase before any archive click or POST. Earlier Ruby, Go and browser package checks passed. The VM trace shows the page read/transport activity, followed by the acceptance command exiting 1.
- No retries, remaining derivations, or aggregate check were run after the failure.
- Full derivation log: `logs/archive-isolated-check.log`.
