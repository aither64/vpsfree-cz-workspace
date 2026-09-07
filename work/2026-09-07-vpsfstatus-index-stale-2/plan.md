# 2026-09-07-vpsfstatus-index-stale-2

## Goal

I keep getting the VpsfStatusIndexRenderStale alert (see vpsfree-cz-configuration) and I don't understand why. When I look at the graph in prometheus, I don't understand why it is so jagged and so close to the alert threshold regularly -- see screenshot in /home/aither/workspace/ai/vpsfree.cz/tmp/prometheus-vpsfstatus-index-render.png. I'd expect it to remain a straight line. Please investigate.

## Affected repositories

- `vpsfree-cz-configuration`: alert expression, scrape schedule, deployed service
  settings and source revision.
- `vpsf-status`: index rendering, caching, metrics and scheduling.
- Workspace: investigation record only; project repositories are read-only
  unless the investigation establishes a need for a separately scoped fix.

## Approach

1. Inspect the supplied screenshot and trace the alert to its metric producer.
2. Compare configured rendering and scrape intervals with the observed graph.
3. Query live metrics, alert history and service logs where access permits,
   distinguishing expected age-counter behavior from actual render delays.
4. Record evidence, explain the repeated alerts and propose a concrete remedy.

## Compatibility and deployment

This request is an investigation. No production writes, restarts, source changes
or deployments are planned. Persisted data, database schemas, API/CLI contracts,
service protocols and NixOS options remain unchanged. Any recommended fix must
identify mixed-version behavior and rollback implications before implementation.

## Testing plan

Validate explanations against source and live data rather than the screenshot
alone. Correlate successful/attempted renders, durations, errors, scrape timing
and alert state. Use focused local reproduction only if source and production
evidence leave an ambiguous mechanism. No integration build is needed for a
read-only diagnosis.
