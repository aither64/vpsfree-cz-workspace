# Firefox portal incident: bounded historical nginx evidence

Evidence owner: implementer1. Session/environment verified exactly as
`2026-10-20-dev-workspace-portal-improvements` at
`/home/aither/workspace/ai/vpsfree.cz`; live retained roster has implementer1
ready, workspace_write, gpt-6.1-sol/xhigh. No member settings changed.

Scope: client `172.16.107.34`, 2026-10-21 20:20:00–21:35:00 CEST
(18:20:00–19:35:00 UTC). Parent-supplied recovery anchor: 21:28:48 CEST,
after root reset only the client's nine TCP/443 connections. This investigator
did not reset or count live connections, probe HTTP, read credentials, change
services/settings/source/Git/pins/claims, launch tests/builds, or select a profile.
C482/config9ab and final operational guards remain HOLD.

## Observed completion timeline

All times below are CEST on 2026-10-21. These are COMPLETION times,
including the events/SSE routes, never inferred stream start times.

| Period/anchor | Observed access-log completions |
| --- | --- |
| 20:20:00–20:26:54 | 1,740 ordinary requests; last at 20:26:54 |
| 20:24:03 | One events-route/SSE completion, HTTP 200 |
| 21:13:43 | One events-route/SSE completion, HTTP 200 |
| After 20:26:54, before 21:28:48 | Zero ordinary completions; the 21:13:43 SSE completion is the only completion in this gap |
| 21:28:48 | First resumed ordinary completion and first reset-era SSE completion; same second as parent recovery anchor |
| 21:28 minute | 121 ordinary and 13 SSE completions |
| 21:29 minute | 400 ordinary completions and one SSE completion (21:29:21) |
| 21:30–21:34 | 366, 369, 349, 283 and 267 ordinary completions per minute |

The ordinary-completion gap between 20:26:54 and 21:28:48 is 3,714 seconds
(61m54s). This strongly correlates the transport reset with observed recovery.
A gap in completed requests does not show whether requests were unsent,
queued in the browser, already on the wire, or unfinished at nginx/upstream.

Across the bounded window: 3,918 completions, comprising 3,902 ordinary
and 16 URL-classified events/SSE requests. All 3,918 have Firefox user agents
and `HTTP/2.0` in the request protocol field. Firefox158/macOS is the user's
reported client; this aggregate retained only the Firefox-family predicate,
not the full user-agent or exact version. Every events-route completion is
HTTP 200; content type and frame/stream history are not logged. A logged SSE
200 does not establish uninterrupted event delivery. These are request/stream
completion counts, not TCP connection counts; the log cannot map them to the
parent-reported nine reset connections.

Status totals: 3,905 HTTP200, six499, one201, two202, four 500; no 502/504.
The four 500 completions have static-asset-shaped paths: 20:24:06, 21:28:49,
21:28:50 and 21:29:23. They are not established as causal or harmless by this
aggregate. Three 499 completions occur 20:24:03–04; the other three occur
21:29:21 (two) and 21:33:11. A 499 is not proof of a specific HTTP2 mechanism.
No raw URLs, query strings, referrers, IDs, payloads, user names or full user
agents are retained.

## Log coverage and error evidence

The nginx.service unit resolves configuration to
`/nix/store/j1jvhxfsdzybjfb3qj57i4la4lxmi7ii-nginx.conf`.
Its SHA256 is
`9863e8a77e434fd384a419e685978572c19e749bac1e857fd6ae41a7175a830b`.
There are no explicit log_format/access_log directives in that config;
matched access records have the default combined structure. Its listed include paths
are named MIME/fastcgi/uwsgi/header fragments; the collector did not expand
their contents. The observed records, not those names, establish the retained
combined-record field structure.
Error output is configured as `stderr`; `/var/log/nginx/error.log` is empty,
with mtime 2026-09-06. The relevant stderr destination is the nginx unit journal.

The bounded unit-journal query for this client plus upstream timeouts,
worker/fd exhaustion, no-live-upstreams and emerg/alert/crit patterns returned
no entries (journalctl exit 1, no stdout or stderr). The grep has the intended
literal-IP/escaped-bracket syntax; the saved argv has nine backslashes.
This means no matching retained entries were found, not that nginx retained
HTTP2 control frames or that no unlogged error occurred. This is not a complete
journal-retention/rate-limit audit.

Access-log collection finished in 3.818 seconds, remote command exit 0,
captured at 19:37:26 UTC after the entire target interval. It reads a fixed
250,388,562-byte prefix; inode 20578420 was unchanged and the live log grew
to 250,391,805 bytes during collection. No rotation was observed in that read.
The prefix is an observation boundary, not an immutable original whole-file
receipt. Raw log contents were neither copied nor hashed/stored locally.

## What remains unproven

The combined format has no request duration, upstream timings, connection ID,
connection request ordinal, HTTP2 stream ID, TLS/control-frame history, or
record of still-open/incomplete requests. It cannot establish GOAWAY, draining,
stream age, pending-request receipt or a browser/Firefox/VPN/nginx cause.
The original nine connections no longer exist; fresh live counts would not
reconstruct their identity or state. Parent-reported healthy direct/fresh-TLS
reads and TCP-alive/no-data observations are separate incident evidence, not
new measurements by this collector. Coordinator CPU, lifecycle contention and
old transcript failures are not established causes by this evidence.

## Minimum useful evidence at the next recurrence (proposal only)

Before transport intervention, preserve the exact first-stall time/timezone,
client address and selected browser version, plus a bounded client TCP443
snapshot with queues/timers/byte and retransmission counters. Pair it with
sanitized browser request-state/timing categories to distinguish unsent/queued
work from received unfinished requests; omit request headers, cookies, bodies,
full URLs and session IDs. Preserve before/after reset timestamps and scope.

Prospective payload-free nginx completion logging could add time_iso8601,
server_protocol, connection, connection_requests, request_time,
upstream_connect_time/upstream_header_time/upstream_response_time, status and
byte counts with a fixed route category instead of full URLs/referrers.
Connection request ordinals are not HTTP2 stream IDs. Such logging can improve
correlation but still cannot prove GOAWAY or expose open-stream state.
If the architect still needs frame proof, an explicitly scoped control-frame
metadata capture should retain only GOAWAY error/last-stream identifiers and
frame/connection timestamps, with headers and payload excluded. No logging or
capture configuration was changed or launched here.

## Retained commands and diagnostics

- `collect-remote.py`: executed payload-free collector, with remote 25s alarm.
- `collect.py`: exact strict fixed-key SSH argv, 35s client bound, verified
  session/environment, short nonblocking tracking lock for receipts.
- `aggregate.json`: bounded aggregate and journal argv/results.
- `command-receipt.json`: exact interpreter/argv, times, exit and code/output SHA256.
- `attempts-diagnostic.json` and `collect-remote-v1-timeout.py`: initial tooling
  failures and inefficient 35s scan preserved. Root's PATH lacked python3;
  the exact existing Python store executable was used without installation.
  NixOS config was resolved from the unit rather than `/etc/nginx/nginx.conf`.
  Binary iteration/date prefilter replaced per-line text-position/date work;
  the resulting bounded collection passed. No blind repeated full scan.

No product documentation change is appropriate before the mechanism is known;
this is session incident evidence for the lead and architect, not an accepted
operational change or an assertion of deployment/browser convergence.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-20-dev-workspace-portal-improvements/
