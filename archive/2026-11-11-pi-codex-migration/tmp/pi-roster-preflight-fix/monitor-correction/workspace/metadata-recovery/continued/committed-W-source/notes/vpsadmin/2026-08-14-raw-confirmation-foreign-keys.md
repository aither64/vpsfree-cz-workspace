# Raw transaction confirmations need database integrity rules

Initiative: `work/2026-08-12-dns-secondary-zone-transfer-failure`

vpsAdmin transaction confirmations may delete parent rows with raw SQL. This
bypasses ActiveRecord dependency callbacks. Explicitly registering the child
rows visible when a destroy transaction is constructed is insufficient when a
daemon can insert related rows asynchronously, or when a pending create later
rolls back after the child was inserted.

For asynchronously maintained child data, enforce the final relationship at
the database boundary. Use a cascade when the child has no meaning without the
parent, and nullify when diagnostic history should survive without claiming an
association to a deleted object. Keep transaction-confirmation cleanup for the
intended operation and rollback semantics, but do not rely on callbacks alone
for referential integrity.

Verify both pending-create and pending-destroy races with raw parent deletion,
then recreate the same logical endpoint and prove that it starts cleanly.
