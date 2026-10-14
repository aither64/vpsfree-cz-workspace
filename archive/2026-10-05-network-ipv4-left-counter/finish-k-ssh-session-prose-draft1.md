# Technical prose draft for root reconciliation after source freeze

Runner processes establish their own POSIX session before starting machines.
They retain the recorded PID, executable and argument vector. This separates
ordinary terminal and process-group signals from guest lifetime; a containing
cgroup, supervisor or host failure can still end the run. A failed session
handoff refuses before starting machines. Cleanup still requires the recorded
ownership and complete exit proof.

The runner's boot marker confirms its test shell. The engine separately waits
for valid SSH host keys from each recorded machine within one absolute
readiness deadline. Empty or unavailable key discovery may wait within that
budget. Invalid keys, a wrong endpoint, runner identity loss or a retained-key
mismatch refuse immediately. The engine writes initial trust only after every
machine succeeds and never changes retained trust to accept a replacement key.
Host-key discovery does not replace strict authentication or the guest source
and system-closure checks.

Failed discovery identifies the machine, endpoint and private native diagnostic
record. That record retains bounded output and native command outcome beneath
the owned run and is excluded from artifact exports. A failed or timed-out
verification keeps the run non-ready with its claims and diagnostic evidence;
it does not replay lifecycle work or authorize orphan cleanup.

Confirm the final source's exact diagnostics path and timeout behavior before
copying this text into cluster/runtime-contract.md. This draft asserts supported
semantics proposed for the correction, not a hosted or real-guest result.
