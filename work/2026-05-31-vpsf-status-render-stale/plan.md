# vpsf-status index render freshness and CPU use

## Goal

Investigate intermittent `VpsfStatusIndexRenderStale` alerts and reduce CPU
cost from the per-second pre-render of the vpsf-status index page.

## Affected repositories

- `vpsf-status`: primary code changes for index rendering, metrics, and tests.
- `vpsfree-cz-configuration`: prepared for deployment/configuration pinning if
  a vpsf-status revision needs to be rolled out.

## Initial approach

1. Inspect the vpsf-status render loop, alert-related metrics, and Prometheus
   alert definition or deployment configuration.
2. Identify why renders can become stale: long render duration, blocking
   refresh path, timer drift, expensive template execution, data fetch latency,
   or metric semantics.
3. Optimize the index pre-render path while preserving current HTTP behavior.
4. Add focused tests or benchmarks for changed rendering logic where feasible.
5. Record any required deployment ordering or configuration pin updates.

## Compatibility analysis

- Persisted state/on-disk formats: expected none unless vpsf-status keeps local
  cache files; verify in code.
- Database schemas: expected none.
- API contracts: preserve existing public status page responses, status JSON or
  monitoring endpoints unless an intentional change is recorded here.
- Protocol/message formats: preserve Prometheus metric names and semantics
  unless alert correctness requires a compatible addition or documented change.
- Configuration/Nix: if only vpsf-status code changes, deployment should be a
  normal service revision update. If configuration pins are changed, update via
  the configuration repository's established tooling.
- Rolling deployment: vpsf-status instances should be independently deployable.
  Mixed versions should be acceptable if HTTP/API/metric compatibility is kept.
- Rollback: old versions must be able to serve after rollback without needing
  to understand state created by the new version.

## Testing plan

- Run repository-local unit tests or targeted Go tests for vpsf-status.
- Add and run benchmark/profiling commands if useful to quantify index render
  cost before and after changes.
- If deployment configuration changes are made, run the repository-local check
  or evaluation command documented by `vpsfree-cz-configuration`.
