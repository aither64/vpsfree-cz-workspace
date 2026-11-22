# Force-with-lease requires a known remote feature head

Initiative: work/2026-09-14-portal-review-fixes.

An organization bare clone had no wildcard fetch refspec. Fetching master did
not populate origin/<feature>, so a rewritten own feature push with the default
--force-with-lease failed with "stale info" despite the remote head being unchanged.

Inspect the remote head with git ls-remote, fetch that exact feature into its
remote-tracking ref, and push with --force-with-lease=refs/heads/<feature>:<known-SHA>.
The expected old head was verified before the successful push. Never replace
the lease with an unconditional force push.
