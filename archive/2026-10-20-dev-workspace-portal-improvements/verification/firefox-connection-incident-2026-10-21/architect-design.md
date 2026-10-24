# Firefox connection incident: bounded architectural disposition

Date: 2026-10-21. Owner: architect0. Investigation and proposed verification only.
The lead owns the independent incident log timeline and any execution decisions.

## Decision

No fact established a necessary host-contract change. Retain the accepted
user-profile-only deployment plan. Continue the independently demonstrated
frontend fixes through their existing affected review, browser and package gates;
this unresolved transport incident is not an additional deployment gate.
Do not describe those fixes as a proven remedy for the connection incident.

No application, configuration, source, Git/index, live setting or ownership
mutation, test, build, request probe, restart or connection reset was performed
by this investigation. The only write is this session-owned evidence note.
The separate pending-read freshness correction remains with its assigned
implementer and retains its existing brief and verification budgets.

## Evidence and limits

The user/lead reported Firefox 158 on macOS through the VPN recovered at
2026-10-21 19:28:48 UTC (21:28:48 CEST) immediately after root reset only nine
established connections belonging to that client. No service restarted.
Fresh TLS and a direct transcript request succeeded while old browser pages
failed with NS_BINDING_CANCELLED. Resource health was normal; some retained
connections had TCP traffic without completed ordinary application requests.
These are reported incident observations, not an independently reproduced trace.
The independent implementer owns the time/client-bounded log correlation.

Selective reset strongly implicates retained client/connection/transport state.
It does not identify nginx versus Firefox versus VPN, prove GOAWAY, or exclude
flow-control or stream-admission problems. A successful fresh connection does
not exercise the failing pooled connection. Cancellation labels, TCP ACKs and
long-lived SSE completions alone cannot establish HTTP/2 frame progress.
Coordinator CPU, lifecycle contention and older transcript failures have no
established causal link to this recovery.

## Exact installed configuration and source mechanism

Local immutable inspection found these installed identities:

- System: `/nix/store/jwnd3m223qh1lanig1ndxprk04qbim06-nixos-system-aitherdev-26.05.20261020.cd4ea8d`.
- nginx binary: `/nix/store/smpkfhyjj22b4zy1f0cprzfhr0nimllr-nginx-1.30.6/bin/nginx`; version-only output confirmed 1.30.6.
- Config selected by installed nginx unit:
  `/nix/store/j1jvhxfsdzybjfb3qj57i4la4lxmi7ii-nginx.conf`.
  SHA256: `9863e8a77e434fd384a419e685978572c19e749bac1e857fd6ae41a7175a830b`.
- Reported live workspace: `/nix/store/hzf9qda2ckjsv72b689bclc6p3v8ap9l-dev-workspace-0.2.0`, with shared source `852e8c51091512bc79ca6c921ef1f5ccc46a9535` (A852), not the candidate.

This establishes installed unit/config provenance; it is not a separate live
process-argv attestation. Only allowlisted transport directives were extracted;
no complete config or credential contents were printed.

The generated config has HTTP/2 enabled, portal response buffering disabled,
upstream HTTP/1.1 and portal proxy_read_timeout 1h. There is no explicit
keepalive_requests, keepalive_time, keepalive_timeout, HTTP/2 stream-limit or
ssl_early_data override in the inspected config/includes.

[nginx release-1.30.6 core source](https://github.com/nginx/nginx/blob/release-1.30.6/src/http/ngx_http_core_module.c#L3912)
sets defaults of 1000 keepalive requests, one-hour keepalive time and 75-second
idle keepalive timeout. Source SHA256:
`b950dcdc2521d8d128ff305262dfc3b0bb92382048bd44505f22dce91c06fac1`.

[HTTP/2 admission](https://github.com/nginx/nginx/blob/release-1.30.6/src/http/v2/ngx_http_v2.c#L1348)
checks count/elapsed-time after admitting a request and sends GOAWAY with
NO_ERROR on reaching the applicable limit. The connection handling path retains
active processing/output before closing a draining connection. Thus the one-hour
limit is not an absolute kill timer for an accepted SSE stream. This mechanism
permits old streams to finish while a compliant client moves new work elsewhere.
Source SHA256:
`27077f505f68d5acd8ab9d6553bb9ffdc83bec172bcdbd5ca8602fe4a46cdd2d`.

Deployed A852 `conversation/handler.go` sends a heartbeat every 20 seconds and
has no absolute SSE stream-age limit. Cancellation, write failure, shutdown or
closed events end the stream. The [proxy read timeout](https://nginx.org/en/docs/http/ngx_http_proxy_module.html#proxy_read_timeout)
limits silence between upstream reads, not total response duration, so a healthy
heartbeat permits the stream to outlive that timeout. This is expected behavior,
not itself a demonstrated defect.

[Firefox 158 Http2Session.cpp](https://github.com/mozilla-firefox/firefox/blob/FIREFOX_158_0_RELEASE/netwerk/protocol/http/Http2Session.cpp#L2044)
marks a received-GOAWAY session unavailable for new streams. It restarts streams
not accepted by the peer and queued streams; existing accepted streams can drain.
RoomForMoreStreams checks the GOAWAY flag. Therefore retaining an old SSE alone
does not establish that Firefox cannot create a replacement connection.
Source SHA256:
`4fc44cee43edfababa4a784cd436aeee99c04285d3299e36f371a5cef4afac83`.

## Relevant upstream limits

No applicable current upstream fix was established by this bounded lookup.
[Mozilla 1050329](https://bugzilla.mozilla.org/show_bug.cgi?id=1050329), a historic
nginx GOAWAY/concurrent-stream bug, was fixed in Firefox 65.
[Mozilla 2065319](https://bugzilla.mozilla.org/show_bug.cgi?id=2065319) concerns
unclean pooled HTTP/2 shutdown without GOAWAY and received its retry fix in
Firefox 158, the reported client version. Its corrected analysis does not
establish this incident's long stall or exact cancellation code.
[Mozilla 2074493](https://bugzilla.mozilla.org/show_bug.cgi?id=2074493) concerns
TLS 1.3 early-data exhaustion on connection resumption; that trigger is not
established here, and nginx [early data defaults off](https://nginx.org/en/docs/http/ngx_http_ssl_module.html#ssl_early_data).
The [nginx 1.30 changelog](https://nginx.org/en/CHANGES-1.30) lists an HTTP/2
flow-control fix in already-installed 1.30.6. None of these is proof that a
version change will fix this incident. Upstream HTTP/2-proxy bugs do not directly
match the inspected HTTP/1.1 upstream path.

## Smallest decisive next proof, proposed only

If the lead needs to pursue the GOAWAY hypothesis, use one disposable synthetic
fixture with nginx 1.30.6 and Firefox 158, a 20-second heartbeat SSE and ordinary
idempotent GETs. Use no real portal authentication, transcripts or session state.
Lower only the test request threshold to trigger GOAWAY quickly; separately
exercise a short test keepalive-time threshold if needed. Keep production
configuration unchanged. Observe whether the old SSE remains open while the
first post-GOAWAY GET gets a fresh TLS connection and succeeds. Capture one
failure/control pair rather than start a broad version or load campaign.
Matching macOS matters if Firefox on Linux cannot reproduce it.

The decisive evidence is connection identity and frame ordering: GOAWAY direction,
error and last-stream-ID; whether a new GET was admitted/sent, queued locally or
moved to a new connection; and response completion. If there is no GOAWAY,
inspect stream-count/SETTINGS, RST_STREAM and WINDOW_UPDATE state before naming a
GOAWAY failure. Ending only the synthetic SSE can then test whether drain
completion changes the stuck state. A passing accelerated fixture would narrow
this hypothesis, not prove the original incident impossible.

For any separately authorized recurrence capture, stop after the first
failure/recovery pair, at 120 seconds or at 5 MiB, whichever comes first. Limit
to the one affected client/origin and retain only timestamps, pseudonymous
connection/stream IDs, frame type/control fields, counts, timing and status.
Do not collect headers, cookies, authorization, request paths/query strings,
bodies, real TLS secrets or full HAR/debug logs. If available tooling cannot
filter before capture, use the synthetic fixture instead. TLS packet metadata
alone and ordinary nginx access logs cannot prove GOAWAY; access logs describe
request completion and an open SSE need not have a completed entry. No capture
or fixture was run here.

## Boundaries and reconsideration

Do not add timer inflation, blanket HTTP/2 disablement, periodic connection kills,
service restarts or forced SSE turnover on this evidence. The candidate's
hidden-tab stream closure and bounded read scheduling address independently
proved fanout/recovery defects, without proving the transport hypothesis.

A reproducible client defect would favor a narrowly demonstrated client remedy.
A proved nginx/site setting defect would create a separate configuration package
and require affected review plus host-contract/deployment reassessment. A proved
need for SSE turnover would belong to the shared handler/client contract with
reconnect and no-duplicate-control acceptance. None is an implementation package
authorized by the current findings. Preserve profile-only deployment, native
Codex policy, existing held machine claim and all prior deployment receipts.
No integration, release or lifecycle permission follows from this note.
