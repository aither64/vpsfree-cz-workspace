# 2026-09-07-vpsfstatus-index-stale-2

## Follow-up accepted on 2026-09-08

Keep Prometheus scrapes at 60 seconds. Prepare a configuration-only fix for the
normal render-cycle false positives: move `VpsfStatusIndexRenderStale` into its
own 60-second rule group and raise its observed-render-age threshold to 600
seconds. Keep the five-minute missing-metric window, alert name, severity and
notification frequency. Require `for = "2m"` on either condition. Assign the
existing public service's alias, instance and type labels to both branches so
missing metrics cannot reset an ongoing alert's confirmation or firing state.
The normal stale-render label set is preserved; absent alerts gain those same
service labels.
The user explicitly prefers a larger margin that signals a serious issue rather
than a fluke.

The observed healthy render cycle was about 242 seconds. A 60-second scrape
delay gives a peak around 302 seconds; one missed scrape can increase it to
about 362 seconds. Ten minutes leaves substantial margin for both. Sustained
rendering stalls are detected after two minutes of confirmation, roughly 12 to
13 minutes after the last observed render. Missing metrics alert after five
minutes without samples plus two minutes of confirmation, roughly seven to
eight minutes after the last sample. The graph remains a sawtooth, with a
threshold above its normal peaks.

Only `vpsfree-cz-configuration` needs changes. Keep the application's body-cache
policy, code, flake inputs and public metric semantics unchanged. Add focused
promtool tests using the production rule for healthy cadence, brief scrape loss,
stalled rendering, missing metrics and recovery. Run the existing hook checks,
mandatory change review, and scoped builds for both monitoring containers.

Compatibility: no persisted data, schemas, migrations, API/CLI/client contracts,
service protocols or NixOS option changes. Old and new status-service versions
can coexist with the rule. Both Prometheus instances can update independently,
but an instance on the old rule can continue sending noisy alerts until it is
updated. Rollback is a configuration rollback and restores the old timing.
Absent alerts from the old monitor lack service labels and may temporarily
group separately from new alerts during a mixed rollout. Both monitors use the
single `status.vpsf.cz:443` target for this job, so the fixed public service
labels apply to both conditions. Changing that target or its labels requires
updating this dedicated alert's service identity as well.
The later stale-age threshold is intentional; more frequent rule evaluation
removes the previous five-minute delay before recognizing recovery. Production
deployment is outside this preparation step.

## Original investigation plan: 2026-09-07

The following is the historical investigation scope. The September 8 follow-up
above supersedes its read-only boundary and verification plan.

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
