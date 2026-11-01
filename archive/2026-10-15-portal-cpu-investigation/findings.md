# Portal CPU and response failures

Investigated on 2026-10-15, approximately 20:30–20:39 UTC. The portal is spending
most of its CPU repeatedly parsing session records. Reconnecting its shared
activity observer multiplies that cost across watched conversations. Oversized
activity replies are an observed source of connection failures.

## Measurements

- Service: `workspace-portal@vpsfree-cz.service`, PID 2704317; no restarts during
  inspection. A separate 10-second `/proc` sample measured **36.35 CPU seconds,
  or 363.5% CPU**. Its lifetime average was approximately 380%.
- Two 10-second, 49 Hz `cpu-clock:u` profiles show the same hot paths. The table
  below filters out inherited Ruby/GitHub helper samples and normalizes to the
  portal itself. These are inclusive stack percentages; rows overlap.

| Portal stack | First sample | Confirmation |
| --- | ---: | ---: |
| `session.loadSummary` | 60.82% | 58.19% |
| `session.decodeManifest` | 53.11% | 52.87% |
| `RecoveryStore.AllowsImplicitResume` | 37.54% | 34.15% |
| `Server.recoveryHeld` | 12.95% | 14.55% |
| Background garbage collector | 20.34% | 22.13% |

- Workspace inventory: 80 active-directory and 194 archived-directory manifests;
  approximately 472 KB of manifest YAML and 8.21 MB of state Markdown in total.
  The largest manifest is approximately 90 KB. Each full scan rereads state too.
- Recent service logs contained ten `message too big: read limited at 67108865
  bytes` errors for the `evaluate-confctl-rewrite-language` activity route between
  20:32:18 and 20:36:55 UTC, alongside cancellations and other disconnect errors.
  That conversation's rollout file was approximately 582 MB; this is context,
  not proof of the size of an individual RPC reply.
- Direct Unix-socket reads bypassed nginx/TLS/authentication. Root HTML took
  29 ms, cached index status 7 ms, and one activity request 244 ms. Another
  conversation's activity request returned **503 after 2.443 seconds**, with
  `Codex service is unavailable`. The problem is intermittent and concentrated
  in conversation/backend work; these measurements do not assess browser render
  cost or rule out additional proxy overhead.

Raw evidence: [CPU sample](cpu-sample.json), [HTTP sample](endpoint-sample.json),
[first profile](portal-only-profile.txt), and
[confirmation profile](portal-only-confirm-profile.txt). Raw perf recordings and
stack exports remain local to this investigation.

## Confirmed expensive path

The running output is
`/nix/store/mng4ibsyn17yihqgms6l8y3znkl7j2mz-dev-workspace-0.2.0`.
Its derivation identifies source
`/nix/store/6cnfr77kid4i6gqzi2x34ws3jxyv9c67-source`; the inspected session,
recovery, activity and notification files match the current canonical repository
HEAD byte for byte. The binary and source pin codex-web at
`5f15b9293f9b1eef7469a34d7b2044c743160283`, with Codex 0.160.0.

1. In dev-workspace, `portal/internal/session/recovery.go:272`,
   `AllowsImplicitResume(socket, thread)` calls `session.List(workspace)` for
   **each individual watched thread**. That list parses every manifest under
   both `work/` and `archive/` and reads its `state.md`.
2. In codex-web, `codex/client.go:1591` and `codex/observer.go`, each connection
   generation restores watched threads through this callback. Four restoration
   workers bound concurrency, but still repeat the full scan for every thread.
   The profile directly captures these restoration workers consuming CPU here.
3. `portal/internal/web/recovery.go:38` calls `session.Find` again even when the
   caller has already loaded a summary. Notification reconciliation runs every
   two seconds and activity reconciliation every five seconds, adding more
   whole-workspace scans and per-session reparsing.
4. `portal/internal/session/manifest.go:493` parses each YAML document twice,
   first for structural validation and then for typed decoding. This amplifies
   allocation cost; validation must be preserved if decoding is optimized.

The expensive resume-admission work scales approximately with watched threads
times total retained sessions per reconnect. The cumulative cost persists even
with browser tabs closed because observation belongs to the portal service.

## Connection failure and likely amplifier

In the pinned codex-web, `codex/activity.go:161` requests turn history with
`firstView: "full"`. `codex/turn_history.go:145` pages by **20 turns**, including
full items; a turn can contain arbitrarily large accumulated tool output.
The WebSocket connection has a 64 MiB message cap (`codex/client.go:29`). Paging
by turn count therefore does not provide a suitable byte bound.

An oversized reply closes the shared connection and fails its other in-flight
RPCs. Restoration then invokes the expensive admission scans above. In
dev-workspace `portal/internal/web/activity.go:96`, a failed read removes its
snapshot; there is no per-thread negative cache or circuit breaker to prevent
repeated expensive attempts. The browser also polls active activity every five
seconds, while idle polling uses 30 seconds.

The oversized errors, reconnect work and full-item request shape are confirmed.
The exact oversized RPC response was not captured, so attributing every
disconnect to a particular turn page remains an inference. No traffic payloads
or conversation content were recorded.

## Recommended solution

Implement both parts; the session-index change addresses the largest measured
CPU cost, while bounded activity processing removes a recurring failure source.

1. **dev-workspace: share a validated session catalog and resolve a thread's
   owner directly.** Build a thread-to-session index for lead and team threads;
   refresh it incrementally when manifest/lifecycle/team identity changes.
   Do not run `session.List` inside each resume decision. Validate the selected
   owner's current recovery record, socket epoch, lifecycle and runtime identity
   before allowing resume; a stale index must fail closed or rebuild. Cache
   parsed summaries against file identity/change metadata, pass loaded summaries
   through `recoveryHeld`, and let activity, notification and display readers
   share snapshots. Display caching must not become TTL-only authorization.
2. **codex-web: calculate activity without repeatedly loading full turn payloads.**
   Use metadata and event-driven incremental counters, with bounded item paging
   for initial backfill. Cache immutable completed-turn aggregates and process
   only new/current items thereafter. Bound bytes as well as item counts; handle
   a single oversized item through explicit truncation/metadata support or
   incomplete statistics. Never silently present partial counts as complete.
3. **Contain failures per thread.** Apply cancellation-aware backoff with jitter
   and a circuit breaker for repeated oversized reads. Retain the last good
   snapshot as explicitly stale, isolate heavy history/backfill traffic from
   the live observer connection, and keep interactive requests responsive.
   Add counters for reconnects, rejected message sizes, scan counts, parse/cache
   hits and activity read latency. Do not merely increase the 64 MiB limit.

For temporary relief, closing tabs repeatedly requesting the failing
conversation can remove browser-driven work, but the background observer remains
active. A service restart would not correct either source path. No mitigation,
restart, configuration change or deployment was performed.

## Verification for an implementation

- Benchmark at least the current 274-session catalog plus realistic team
  membership, including repeated reconnects. Assert one shared inventory refresh
  rather than a full scan per watched thread, and no reparse of unchanged files.
- Exercise archive/revive, deletion, changed team membership, pending lifecycle,
  socket replacement and package transitions; stale ownership must never allow
  a resume. Preserve strict YAML and file validation.
- Include a conversation whose full turn page exceeds 64 MiB and a single huge
  item. Activity should degrade locally without disconnecting healthy sessions,
  and cancelled backfills must stop promptly.
- Compare CPU, allocations and p95/p99 interaction latency before and after
  under the same session/tab load; verify counters and timing totals remain
  accurate. No numerical improvement is claimed before this measurement.

These changes can be in-memory and preserve persisted formats. Deploy the
codex-web client fix through its dev-workspace dependency and then the normal
user-profile package transition, keeping Codex protocol validation at 0.160.0.
Use the supported forward recovery workflow if a package correction is needed.
No schema migration or coordinated node update is proposed.

This deliverable is investigation findings only. No application code or reusable
project documentation was changed, and no builds, integration tests or mandatory
change review were needed.
