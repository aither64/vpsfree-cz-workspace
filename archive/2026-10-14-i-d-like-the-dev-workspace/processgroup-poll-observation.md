# Recovery checkpoint observation

The watcher reported Python AssertionError output while the full6e1 operation
was still active. Lead inspected the exact reported log region and owning
wait_provider_result: nonterminal phases deliberately return a nonzero probe
status to wait_until_succeeds. The log records subsequent successful waits and
later scenarios. Those transient polling tracebacks do not establish VM failure.
Final wrapper/check status remains authoritative. No retry, cancellation,
source change or provider operation followed the preliminary report.
