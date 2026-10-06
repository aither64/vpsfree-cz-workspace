# Committed SQL concurrency fixtures

Related initiative: work/2026-10-05-network-ipv4-left-counter/.

The network-admission parallel fixture used TransactionChain.create! with only
name/state/size/user/session plus a manual global_locks array. MariaDB rejected
its missing STI type before the admission code ran. Adding type alone would
still leave runtime lock arrays uninitialized. Use the existing
build_transaction_chain! test helper, which initializes both.

The foundation CI jobs then reported duplicate fixed fixture addresses and one
Create selection mismatch. Those observations are consistent with cross-example
leakage; the exact historical leak mechanism was not established. Do not describe
a green focused run as proof of that causal explanation.

Committed multi-connection fixtures need cleanup even when a worker's assertion
or join raises. Track and join every owned worker before restoring scoped rows;
retain the original worker error until restoration completes. Record the fixture
pool ID immediately after it is saved. Check reservations, parent/host rows,
seed allocations and quota snapshots, then raise restoration diagnostics after
cleanup. Avoid expectations in RSpec teardown hooks where the repository lint
forbids them. Never delete arbitrary rows outside the fixture scope.

After this repair, all 13 concurrency and five Create examples passed in core
and full-plugin modes at the original failing CI seeds 36954 and 9346. Full-topic
CI remains separate evidence from this focused reproduction. The final-head
core and full foundation CI jobs subsequently passed as well; that result
does not establish the historical leak mechanism.
