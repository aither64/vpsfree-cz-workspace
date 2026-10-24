# Live Firefox connection stall: user incident evidence

Priority changed by user on2026-10-21: verification has taken too long;
investigate the supplied actual incident while the already-assigned bounded
pending-read fix continues. Original implementation/deployment objective remains.

These are USER-REPORTED observations, not yet independently reproduced or frame
traced. Recovery21:28:48CEST/19:28:48UTC. Firefox158/macOS, VPN172.16.107.34,
portal pages stalled with NS_BINDING_CANCELLED. Server nginx/router/portal/Codex
running; direct portal requests including transcriptHTTP200<1s, freshTLS accepted
immediately, memory/disk sufficient. Nine established clientHTTPS connections
continued TCP data/ACKs but some had no application data for hours. Last ordinary
completed browser requests around20:26:54CEST; later mostly event streams ending.

User reports resetting exactly those nine connections as root using
`ss -K state established '( sport = :443 and dst = 172.16.107.34 )'`. Firefox
immediately reconnected and became responsive, requestsHTTP200. No nginx/portal/
Codex restart. This command was performed by the user; no agent repetition is
authorized or has been performed.

nginx1.30.6, HTTP2 enabled, bufferingoff, proxy_read_timeout1h; no explicit
keepalive settings in generated configuration. Live packagehzf9 and embedded
A852, not the undeployed follow-up. Access log /var/log/nginx/access.log, many
SSE completions at reset followed by ordinary success. SSE timestamps describe
completion. HTTP2 draining/GOAWAY with long-lived SSE is a strong hypothesis,
not confirmed without frame evidence. CoordinatorCPU68%, lifecycle contention
and earlier transcript failures have no established relation to this incident.

Architect0 owns bounded nginx/generated-config/defaults/upstream HTTP2+SSE
mechanism investigation; imp1 owns client/time-bounded aggregate log timeline and
log-format evidence limits. Read-only, no connection kills/restarts/config or
profile changes, no broad logs/transcripts/credentials, no duplicated log scan.
Imp2 retains sole B source/Git for separately proven pending-failure freshness
correction. Imp0 retains tracking-only lifecycle/Team fixture candidate.
No current browser/package rerun is launched. Pins/activation remainHOLD;
profile-only rollout decision must be reassessed if necessary host changes emerge.
Machine755910ab staysheld; no integration/release/lifecycle permission inferred.


## Bounded investigation outcome

Imp1 independently aggregated3,918 client completions for20:20–21:35CEST, all
Firefox/HTTP2. Ordinary3,902, URL-classifiedevents16. Last ordinary completion
before reset20:26:54CEST; first afterward21:28:48CEST, gap61m54s. Thirteen
events completed in21:28minute; ordinary121 thatminute then400 in21:29. This
corroborates reset/recovery correlation. Combined log has no durations, connection
IDs/request ordinals/stream IDs/GOAWAY evidence; SSE timestamps are completions.
[Aggregate and limitations](verification/incident-firefox-20261021-192848/aggregate.json),
read-only successful collector3.818s. An earlier inefficient text scan hit35s bound
without aggregate output; retained failed-attempt evidence, no service effects.

[Architect exact configuration/source disposition](verification/firefox-connection-incident-2026-10-21/architect-design.md):
nginx1.30.6 defaults1000requests/1hkeepalive/75sidle. Reaching request/time limit
on new admission sendsGOAWAY/NO_ERROR, accepted activeSSE can retain draining
connection. A852 heartbeat20s has no max stream age; proxy_read_timeout1h is an
inter-read silence limit. Firefox158 source excludesGOAWAY sessions from new
streams and retries queued/unaccepted work elsewhere. The failure of that
replacement, or even whetherGOAWAY occurred here, is NOT established. No matched
current upstream fix or required host change established. No speculative nginx
setting, HTTP2disable, repeated connectionkill or SSEturnover change assigned.

Incident investigation is bounded and not a new frontend rollout gate. Profile-only
rollout remains; independent pending/fanout/recovery fixes retain their own proof.
Smallest optional nextproof is disposable nginx1.30.6/Firefox158 accelerated
GOAWAY+heartbeatSSE+ordinaryGET failure/control trace; no real traffic/secrets,
no campaign launched. macOS-specific behavior remains unreplicated.
