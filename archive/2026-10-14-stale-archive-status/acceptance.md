# Live acceptance

Verified after both original coordinated deployment jobs succeeded, against the
combined already integrated sources: runtime 92b2576d, workspace 5a2119d4,
configuration ac001928. Independent composition review found no issues; focused
Go, Chromium/Firefox regression checks and both exact builds passed.

Actual application:
`/nix/store/13s6kwhliihnnby7rxym6wsbafv6cxh6-dev-workspace-0.2.0`.
Actual current system and system profile both match the exact built generation:
`/nix/store/xf0i8ryhpx575282m5hlq2vavq56vms8-nixos-system-aitherdev-26.05.20261012.7993f34`.
Both jobs completed successfully under this session's reservation, preserving the
original dependency graph and retained failed pre-effect attempt. The system job
succeeded on attempt 016c3f05-1df4-489e-a895-038780e16e42; application job on
36f43c21-a51a-426d-922f-8319e13e74eb. See `deployment-watch-v5.json` and the
request/snapshot/approval/refresh receipts in `coordination/`.

The GET-only live browser probe uses the actual original archived session
`2026-10-11-diagnose-vpsadmin-api-exception`, its live document/assets and details/
operation responses. Native endpoints are stubbed and all non-GET requests are
blocked. Each browser starts with an injected stale pending marker. Chromium and
Firefox each observe exactly one reconciliation reload (two documents total),
empty pendingLifecycle, hidden Retry/Archive controls and zero mutation requests.
See `live-browser-after.json`. In-flight details GET cancellation during reload
is expected and was observed in both engines. Target ID and retained conversation
match the original archive; no archive/revive or recovery mutation was performed.
The authoritative session index independently shows archived=true with no pending
lifecycle marker; see `live-index-provider.json`.

All three user services remain active. Native Codex PID 2615996 and tmux PID
435397 match the final pre-activation baseline, with their socket device/inode
identities unchanged. The portal restarted normally. Compare
`runtime-predeployment-v5.json` with `runtime-after.json`. The actual running
native executable reports 0.160.0, and active provider is codex-lb. An initial
check accidentally used the ambient terminal client (0.162.1); the corrected
check resolves the retained service process executable directly. It did not
change any provider or native process.

Deployment and technical review work are finished. No separate manual UI review
was requested. This evidence authorizes no unrelated operation. Finish only the
owned reservation with the three exact current integrated feature heads and
settled jobs/deliveries. Existing tabs using the old JavaScript need one refresh
to load the updated client. Keep this session and its branches available.


Reservation finish succeeded and is recorded in `coordination/finished.json`.
Final `coordination/status-finished.json` confirms released revision 5, all five
jobs succeeded and all 14 notifications delivered. Acceptance and deployment
work are complete; no remaining blocker or operator action beyond refreshing an
old browser tab once.
