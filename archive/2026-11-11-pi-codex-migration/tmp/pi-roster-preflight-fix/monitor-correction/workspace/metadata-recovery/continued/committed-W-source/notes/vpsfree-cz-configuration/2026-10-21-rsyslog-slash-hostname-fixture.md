# Use production RFC5424 format for slash-containing syslog hostnames

An RFC3164-shaped fixture packet with a confMachine.name containing slashes was
parsed as localhost by pinned rsyslog8.2608.0, creating remote/localhost/log rather
than the expected cluster tree. Bounded protocol probes showed canonical RFC5424
for the same host creates the exact expected path0640 and preserves exporter data.
Production senders already use LocalHostName plus RSYSLOG_SyslogProtocol23Format.
Match that wire format; do not change production destinations to satisfy a fixture.

A single cat FIFO consumer also exits on EOF when rsyslog stops. Fixture consumers
must survive that lifecycle, and reconciliation tests must stop syslog.socket as
well as syslog.service or logging can auto-reactivate. Preserve original read
predicates with bounded waits and diagnostics. The missing-consumer hypothesis
was disproved as the filename cause; keep failed diagnosis records accurate.

Evidence: work/2026-10-21-aitherdev-observability-access/logger-runtime-diagnosis.md.
