# Concurrency fixtures under REPEATABLE READ

Independent connections in IP ownership specs exposed three fixture pitfalls:
root RSpec transactions cannot see later committed fixtures through their old
snapshot; uncommitted quota/export fixtures hold locks needed by concurrent
writers; ordinary reload can still read the old snapshot after the race.

Run race scenarios in separate-connection rollback transactions, keep fixtures
minimal, and use locked current reads for final state assertions. A narrow
resource-lock plus ownership update can isolate a stale-reader protocol when
full-chain cleanup is already covered separately. Do not leave committed
fixtures behind after failed examples. The corrected focused run passed all
40 examples. Related initiative: work/2026-09-09-ip-release-mechanism.
