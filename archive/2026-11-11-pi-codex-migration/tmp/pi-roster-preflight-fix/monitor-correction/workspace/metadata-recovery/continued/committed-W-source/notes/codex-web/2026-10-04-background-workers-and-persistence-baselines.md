# Turn completion does not quiesce native background writers

Initiative: `work/2026-10-03-automatic-session-slugs/`.
Inspected source: pinned Codex0.160.0. Actual static-profile native check at
provider1be5ba65 failed strict shell-snapshot/memory comparisons after a positive
ordinary control completed. Later prompt/identity diagnostics separately failed
in logs_2.sqlite/logs. No assertion or logging policy was waived.

The ordinary turn processor starts an unjoined memory pipeline. It can prune
old seeded stage-1 rows, write job accounting and start a separate consolidation
agent whose shell snapshot is created/deleted asynchronously. A completed root
turn does not join that work. The changed snapshot's ID in this run matched
neither the control root nor recorded utility threads, so source eligibility
alone cannot identify its actual writer. A whole memory SQL dump difference
also does not prove that the seeded row changed. Go map iteration chooses the
first reported mismatch; alternating filenames are not write-order evidence.

For a whole-home persistence oracle, prove ordinary inference/tool eligibility
before one fixture-only process quiescence boundary. Stop and positively join
owned native processes and descendants, restart the same profiles/home, use
only persisted thread/read on the retained ordinary root, then seed unchanged
sensitive rows once and capture one immutable baseline. Retain the original
fixed deny counter across restart and all later utilities. This selected
correction is committed, pure-checked and independently reviewed. Actual
namespace control passed two cycles with both direct waits, two adopted reaps,
ECHILD and live init. At corrected providerde874, the native matrix no longer
reported snapshot/memory mismatches, but still failed strict diagnostic-logging
retention. This does not attribute the original writer or prove all later gates.

Leader-group termination is insufficient because pinned shell-snapshot helpers
start new sessions and MCP helpers start new groups. The selected finite fixture
boundary adds a PID namespace to the existing reexec, with the test as namespace
init and a fresh proc mount. Validate private ownership before each namespace
signal, fence/drain helper callbacks, finish both single direct Wait owners, then
reap adopted children until ECHILD under one fixed stop deadline. WNOHANG zero
and ESRCH are not empty-domain proofs. Wildcard reaping before direct waits can
steal their exit status; repeated sleeps or PPID scans cannot replace ownership.
No unvalidated host wildcard kill or separate process-manager service is used.

Do not substitute a sleep, repeated stable snapshots, changed seed timestamps,
rebaseline/reseeding after calls, separate utility home or ignored directories/
tables. Keep marker/ID scans and exact sensitive-row checks. If a mismatch
remains after positive quiescence, use bounded table/count/owner classifications
without dumping rows or assuming that timing attributes a writer.

Source-backed design and remaining limits:
`work/2026-10-03-automatic-session-slugs/design.md`, section "Static-profile
persistence diagnostic: ordinary background work". Native result:
`work/2026-10-03-automatic-session-slugs/static-profile-native-observation.md`.

Execution: `work/2026-10-03-automatic-session-slugs/pid-native-observation.md`.
