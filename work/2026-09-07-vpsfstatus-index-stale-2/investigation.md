# Repeated status index render alerts

The sawtooth is expected for the age of a cached render. The alert threshold
leaves too little room for the render schedule and Prometheus scrape delay.
This provides a concrete mechanism for brief false stale alerts during healthy
operation. Individual past notifications still need their values and scrape
history to distinguish that mechanism from a failed scrape or a longer stall.

The supplied screenshot omits its query. Its values and shape match the age
expression used by the rule:

```promql
time() - max_over_time(
  vpsfstatus_index_last_render_timestamp_seconds{job="vpsf-status"}[5m]
)
```

The underlying metric is a Unix timestamp. It changes only when an index body
finishes rendering. Subtracting it from the evaluation time makes the graph
climb by one second per second, then drop when Prometheus observes a new render.
For increasing timestamps, `max_over_time` selects the latest successful render
observed in the window; it does not smooth the graph. See the
[Prometheus function definitions](https://github.com/prometheus/prometheus/blob/main/docs/querying/functions.md).

## Why the cycle lasts about four minutes

The service caches the expensive index body. Probe and notice updates request
a render, but the renderer compares the visible content's signature and skips
unchanged bodies until a four-minute keepalive expires. A changed signature
causes an earlier render. The keepalive is checked on incoming render requests;
it is not a timer that guarantees completion at exactly 240 seconds.

The request loop coalesces work and allows attempts at most once per second.
The configured notice check requests work every 30 seconds, and other probe
completions request work too. Scheduling, time spent rendering and localized
body timings add some variation. English and Czech bodies have separate caches
but update one shared successful-render metric.

The page's displayed generation time belongs to the lightweight shell assembled
for each HTTP request. It can remain current while the cached body is older.
Opening the page therefore does not necessarily reset this metric.

This behavior was intentional in
[c6fab247](https://github.com/vpsfreecz/vpsf-status/commit/c6fab2476b3dfabf379b64a50d275b33b241f72a):
rendering the full page every second consumed too much CPU on small hosts. The
change chose a 240-second keepalive against the existing 300-second alert.

## Why the graph reaches 300 seconds

| Setting | Current source value |
| --- | --- |
| Unchanged-body keepalive | 240 seconds |
| Public metrics scrape interval | 60 seconds |
| Stale threshold | More than 300 seconds |
| Alert group evaluation interval | 300 seconds |
| Alert confirmation period (`for`) | None |

Before the next scrape arrives, Prometheus continues using the previous render
timestamp even if the service has already rendered a fresh body. The observed
peak can approach the render interval plus one scrape interval. Here that is
already 240 + 60 = 300 seconds, before scheduling and render duration are added.

Illustrative timing, using a healthy 242-second render interval:

| Time | Event |
| --- | --- |
| 12:00:00 | Body finishes rendering. |
| 12:04:01 | Scrape still reads the 12:00:00 render timestamp. |
| 12:04:02 | The next body finishes rendering successfully. |
| 12:05:00.5 | Rule evaluation still sees 12:00:00 and computes 300.5 seconds. |
| 12:05:01 | Next scrape discovers the 12:04:02 render. |

That evaluation can fire the alert although the body is only 58.5 seconds old.
Because the group evaluates every five minutes, Prometheus may not clear the
firing state until its next evaluation. Alertmanager's short notification waits
allow it to send a notification in the meantime. `frequency = "1h"` selects a
notification repeat interval; it is not a requirement to remain stale for an
hour. Prometheus documents the
[immediate firing behavior without `for`](https://prometheus.io/docs/prometheus/latest/configuration/alerting_rules/)
and the [rule group evaluation interval](https://prometheus.io/docs/prometheus/latest/configuration/recording_rules/).

A failed scrape can extend this further. The rule's five-minute range tolerates
brief metric absence, but it still computes age from the most recent timestamp
it has received. The range does not guarantee tolerance of a missed scrape when
that timestamp is already close to 300 seconds old.

## Evidence and limits

- Source inspected after fetching upstream: `vpsf-status`
  `587cd65bb02e6dddea7f6b6409e42a15f36ab4fb`; configuration
  `4d570e3053b114518ada59c2a45d5e9d8644347b`.
- The configuration's `vpsfStatus` flake input pins that same status revision.
  SSH access was unavailable, so the running binary's exact revision and live
  loaded Prometheus configuration could not be independently verified.
- Public metrics returned HTTP 200 through Cloudflare with
  `cf-cache-status: DYNAMIC`. The initial read at 14:27:40 UTC reported
  `vpsfstatus_up = 1`, zero render failures, a 0.943-second last render and
  692929 skips. A later read showed the skip counter advancing.
- Direct sampling from 14:30:22 to 14:35:27 UTC collected 62 successful reads.
  Failures remained zero; duration ranged from 0.856 to 0.943 seconds; attempts
  were at most 5.34 seconds old; the skip counter increased by 452. Render
  updates at 14:30:37 / 14:30:43 and 14:34:39 / 14:34:45 give a 242-second
  cycle between corresponding updates. The two nearby updates are consistent
  with the localized caches, although the metric does not label their locales.
  `metrics-summary.json` preserves the observations.
- Both public Prometheus APIs returned HTTP 401. Direct internal port 9090
  requests timed out, and SSH to the status host and mon1 rejected the available
  credentials. No production state was changed.
- A recent notification's timestamp and VALUE were requested. No historical
  alert or scrape data has been read. Zero failures in the current process does
  not establish that every past notification was false.

## Recommended follow-up

A monitoring-only fix can preserve body caching and the 300-second threshold:
scrape `vpsf-status` every 15 seconds, move this alert to a group evaluated every
30 seconds, and require one minute of sustained failure with `for = "1m"`.
This gives the normal render cycle more room and lets a fresh scrape clear a
brief crossing before notification. The confirmation period deliberately adds
one minute before notifying about a sustained problem. These values should be
validated against actual alert and scrape history before deployment.

Adding `for` to the existing five-minute group alone would defer confirmation
to the next five-minute evaluation. A smoother display would not address the
timing problem. A shorter application keepalive is another option, at the cost
of more render CPU time; raising the stale threshold changes the freshness
objective.

For correlation around a notification, graph the current age expression with:

```promql
time() - vpsfstatus_index_last_render_attempt_timestamp_seconds{job="vpsf-status"}
vpsfstatus_index_render_duration_seconds{job="vpsf-status"}
increase(vpsfstatus_index_render_failures_total{job="vpsf-status"}[15m])
up{job="vpsf-status"}
ALERTS{alertname="VpsfStatusIndexRenderStale",alertstate="firing"}
```

An alert VALUE just above 300 with fresh attempts and no failures fits the
sampling mechanism. VALUE 1 with only the `job` target label identifies the
`absent_over_time` branch; that needs a missing-metrics investigation. A large
age with stale attempts or new failures needs a renderer or service diagnosis.

No implementation or deployment was performed. Monitoring-only changes would
require no data migration or coordinated status-service update; they could be
deployed independently to both Prometheus instances and rolled back through
configuration.

## Source locations

- [Index caching and rendering](https://github.com/vpsfreecz/vpsf-status/blob/587cd65bb02e6dddea7f6b6409e42a15f36ab4fb/index.go#L17),
  especially lines 104, 168 and 258.
- [Alert rule and five-minute group](https://github.com/vpsfreecz/vpsfree-cz-configuration/blob/4d570e3053b114518ada59c2a45d5e9d8644347b/modules/clusterconf/monitor/rules/vpsfree-web.nix#L119).
- [60-second scrape schedule](https://github.com/vpsfreecz/vpsfree-cz-configuration/blob/4d570e3053b114518ada59c2a45d5e9d8644347b/modules/clusterconf/monitor/default.nix#L530).
- [30-second probe configuration](https://github.com/vpsfreecz/vpsfree-cz-configuration/blob/4d570e3053b114518ada59c2a45d5e9d8644347b/configs/vpsf-status.nix#L74).
