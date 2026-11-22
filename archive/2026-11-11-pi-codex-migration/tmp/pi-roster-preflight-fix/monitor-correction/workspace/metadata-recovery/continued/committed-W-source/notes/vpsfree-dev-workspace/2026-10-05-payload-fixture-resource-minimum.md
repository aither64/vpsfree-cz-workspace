# Verify fixture requests against the guest seed

The retained storage-profile payload trial stopped during VPS preparation because
its request used 512 MiB of memory. The selected vpsAdmin guest seed required at
least 1024 MiB. Ordinary API spec bootstrap used a 128-MiB minimum, so a test
against that bootstrap alone would miss the incompatibility.

For provider fixtures, derive resource constraints from the selected API's
`api/db/seeds/test.nix`. Project only the relevant numeric fields through Nix;
the complete seed contains credentials. Exercise the actual fixture request
against those constraints. Keep API limits and existing resource packages intact.

The failure raised `ClusterResourceAllocationError` inside VPS staging. The
previous user chain completed, while the rejected VPS transaction rolled back.
Preserve admitted IDs and inspect their state before considering a new run.
An installed guest wrapper embeds an immutable provider script, so a worktree
edit requires normal package selection and services delivery before it can
correct a retained trial.

Related initiative: [storage redesign](../../work/2026-09-23-storage-redesign/state.md).
Verification results and the actual delivery checkpoint are tracked in that record.
