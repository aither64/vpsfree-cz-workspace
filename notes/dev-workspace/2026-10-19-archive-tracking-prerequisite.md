# Archival refused tracking with no prior commit

Initiative: work/2026-10-19-session-archive-refresh-fix/.

The installed local-first archive path still called validate_tracking_committed!
in preflight and finalization. A valid portal-created session whose plan/state
were never committed failed with "tracking files have no prior commit", before
journal creation. The shared path also affects automatic archival, including its
empty-session tier.

The repair skips committed-history checks only for fresh local-first operations
and finalization under their local tracking journals. Local fsynced receipts bind
the exact archived tree before runtime retirement. Existing synchronous journals
retain their saved requirements; automatic inactivity, holds, ownership,
cleanliness and merge/publication proofs remain. Runtime docs and regressions
cover uncommitted/partial records, all automatic tiers, retries, sync and revival.

An operator can recover a specific failed pre-journal attempt on the old runtime
by preserving its existing active records in an owned-path tracking-only commit,
then using the ordinary saved Retry operation. Do not edit receipts or invent
missing tracking. This recovered 2026-09-22-team-test-2 before package deployment;
the archive completed and tracking sync succeeded.

Focused session tests load shared fixtures through test/dev_session_test.rb;
loading an individual test file directly can fail with undefined NullTmux.
