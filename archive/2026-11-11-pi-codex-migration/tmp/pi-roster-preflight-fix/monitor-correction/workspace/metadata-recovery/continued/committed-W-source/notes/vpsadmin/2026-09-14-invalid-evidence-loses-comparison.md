# Invalid evidence can lose recent history confirmations

At vpsAdmin 337c9257, normal software/deployment, sysctl, module and inferred eBPF
changes use the latest accepted evidence observation. After a rejected security
evidence report, however, the supervisor overwrites the current snapshot with an
invalid placeholder. SnapshotReader.comparison then falls back to the most recent
immutable event, losing later unchanged observations from the comparison.

A disposable DB reproduction used: state A on April 5, unchanged A on April 25,
invalid evidence 30 seconds later, then state B after a supervisor restart. All
five history categories used April 5 as the lower bound instead of April 25.
The livepatch-application special case also overwrote its newer kernel
confirmation with the stale preceding-report time.
Without the invalid report, each used April 25 correctly. System-state capacity
and cgroup first/last observations remained correct in both cases.

This remains unfixed. A follow-up needs to retain the last valid comparison report
and its observation time while preserving honest invalid-current-evidence status.
Kernel last_confirmed_at cannot substitute for component-specific evidence.
The delivered historical repair intentionally covers only public kernel events.

Verification: 13 real supervisor/MariaDB examples pass, including assertions that
reproduce the defect. Details and executable reproduction:
work/2026-09-14-kernel-history-fix/status-timestamp-audit.md and
status-timestamp-audit_spec.rb.
