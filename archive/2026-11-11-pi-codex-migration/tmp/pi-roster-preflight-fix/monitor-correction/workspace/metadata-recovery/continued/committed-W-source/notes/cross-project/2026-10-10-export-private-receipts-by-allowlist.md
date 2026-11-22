# Export private operation receipts by allowlist

Related initiative: `work/2026-10-05-network-ipv4-left-counter`.

A failed verifier phase embeds its complete configuration under `inputs`.
Copying that phase into a limited startup proof also copied account and web-auth
passwords. Hashing a record does not make its contents safe for tracking or a
portal.

Export only the required scalar phase/result facts and native hashes. Keep the
original private receipt in owned0700 storage with0600 files. Never include the
configuration subtree or print a full nested receipt during review. Before
publishing evidence, inspect its actual nested content and scan the curated
files for exact generated credentials without printing their values.

The exported G13 proof was redacted before the handoff commit. Its original
hash remains recorded, and a streamed tracking scan found no other generated
account copies. The earlier portal/reviewer-output exposure is still recorded;
redaction cannot establish that nobody read it or erase an emitted tool result.
Generated exposed credentials must not be reused. Public synthetic fixture
defaults found in source diffs were distinguished from private account values,
without changing reviewed source or native evidence hashes.
