# Forked OpenZFS CI targets incompatible runner kernels

## Symptom

The standard `zloop`, CodeQL, checkstyle, and zfs-qemu GitHub workflows fail on
the vpsFree.cz ZFS fork even when a feature change compiles successfully.

## Cause

- The zloop runner uses Linux 6.17. It compiles `zpl_file.c`, then unchanged
  `zfs_vnops_os.c` fails because this fork still accesses removed
  `struct page.index`.
- The CodeQL runner uses Linux 6.8. It compiles `zpl_file.c`, then modpost rejects
  existing GPL-only `posix_acl_clone` and `init_user_ns` references.
- The checkstyle job completes its tooling and configure stages, then its generic
  `make` step fails at modpost on the same existing GPL-only symbols.
- Every zfs-qemu matrix job timed out after 20 minutes in `Setup QEMU`, before
  test preparation. Follow-up artifact and summary steps then failed because
  setup had not produced `env.txt`.

These failures are outside the changed file. The exact vpsAdminOS-pinned base
commit `6f5f54c3bfd68c1e52b0b6f454ee9679aaa9e83d` also has all four standard
workflows recorded as failed; its retained run logs have expired.

## Verification

Observed on current-head runs `33639482175` (zloop), `33639482139` (CodeQL),
`33639482242` (checkstyle), and `33639482189` (zfs-qemu) while working on
`work/2026-09-02-vpsadminos-chattr-test`. Inspect the failed logs before
accepting this diagnosis for a later change, because runner kernels and fork
compatibility may change.
