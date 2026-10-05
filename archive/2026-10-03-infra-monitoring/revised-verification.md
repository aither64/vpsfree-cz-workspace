# Final verification and integration

Verified and merged into remote vpsfree-cz-configuration/master at
`657cc0a8e087f8c4bed7fe8d7176cb9f06a6e2da`, tree
`c3a20ba419ff6bc8e2b3ed2a6d4600087d143af9`. Both remote master and retained
feature branch point to that exact head. Feature and integration target
checkouts are clean. No deployment occurred; the user owns deployment.

## Checks and review

| Evidence | Result |
| --- | --- |
| Pinned Nixfmt/RuboCop, Bash syntax, whitespace, active declared hooks | Passed on final tree and both final commits |
| infra-monitoring-config + infra-monitoring-rules | Exit 0, 6.760 seconds |
| vps-autostart-prometheus-rules + process-count-prometheus-rules | Exit 0, 2.929 seconds |
| Final committed tree versus check snapshot | Identical |
| Independent whole-branch review, all four lanes, reviewer0 gpt-6.1-sol/xhigh | No Blocking, Important or Advisory findings |
| Complete cleaned history/migration lineage | Two logical commits, no obsolete approaches, no migrations |

[Check result](revised-quick-checks-2-result.json),
[implementation](implementation-result.md), [review](revised-review.md),
[branch inventory](revised-branch-inventory.md). Initial revision failure was
only two warning assertion selectors including the unrelated missing-job VM
case; exactly those query selectors were narrowed and the actual rerun passed.
Production did not change for the correction. Earlier warning-boundary R1 is
closed by selected root 20%/19% tests and the revised independent review.
Historical SMS-only evidence is preserved separately and does not establish
this revision's verification.

## Full central builds and generated configuration

Fresh utility /root/revised_central_builds_watcher used pinned catalog
verification_watcher gpt-6-luna/low, owned the exact local commands and completed
after the mandatory review gate. Inventory selected exactly both intended
replicas. Both full builds passed on the reviewed head/tree:

| Build selector | Exit | Elapsed | Generation |
| --- | --- | --- | --- |
| cz.vpsfree/containers/prg/int.mon[12] | 0 | 74.2 seconds | 2026-10-03--19-14-38 |
| cz.vpsfree/containers/prg/int.alerts[12] | 0 | 61.9 seconds | 2026-10-03--19-16-01 |

Commands: `nix develop --no-write-lock-file --command confctl build --yes`
with each selector above. [Structured results](revised-central-builds-result.json)
record inventory/command exits, source identity, generations and confctl log
paths. Complete local output is revised-central-builds.log. No operation remains
running. These are built generations, not deployed generations.

Lead independently read only sanitized fields from both built Prometheus YAMLs,
checking all filesystem target groups and actual critical rule/hold/labels:

| Job | Groups and machine types, on both monitors |
| --- | --- |
| infra | 44 VPS, 3 VM, 3 physical |
| nodes | 13 physical |
| mon | 2 VPS |
| meet-jvbs | 11 VPS |

All configured node-exporter groups have the intended type. The built rule has
the positive vm|physical selector, five-minute hold and original critical/class/
hourly labels. [Generated audit](generated-monitor-audit.json) records actual
built toplevel paths, counts and that rule, without credentials or whole YAML.

## Publication, approved integration and CI

User explicitly authorized verification followed by default-branch merge and
retained deployment personally. Fresh origin/master stayed b66c929b, so no
rebase was required. Feature publication used an exact old-head lease on f725dd3f
and succeeded. A clean detached checkout from origin/master then fast-forwarded
to 657cc0a8 and pushed normally, without force, to refs/heads/master. Actual
remote master/feature refs were independently verified equal to final head.
[Integration result](integration-result.json) and [record](integration.md)
retain exact revisions and command evidence. Stale local master b6e650ad remains
unchanged, both feature refs retained, comparison saved as base b66/head 657.

Scoped GitHub Actions lookups returned no feature runs and no master runs for
the final SHA; there were no superseded active runs to cancel. The unchanged
repository workflow is schedule/dispatch-driven. No CI run was treated as a
substitute for local verification.

## User-owned rollout and residual limits

Update both monitor replicas with labels/rule together. During mixed versions,
an old monitor can still emit VPS criticals; finish both updates before judging
the new policy. Label identities may reset pending/rate windows and prevent
HA deduplication across old/new label sets. Existing alerts may resolve normally.
No alerter-first policy step or exporter/node/VM/JVB update is required.

No live scrape/reload/notification-delivery test or fleet/unknown-consumer audit
was performed. Offline amtool covers receiver selection, not transport,
activation/repeat timers or executed inhibition. Missing/invalid types are
intentionally ineligible for the critical rule; warnings and node-fatal behavior
remain unchanged. /run remains selected and is not expanded by dataset growth.
State is rollback-readable with no migration/deletion needed. Lasting policy and
recovery constraints are in the project's monitoring page; prepared rollout is
in design.md. Session remains active/open for user rollout and follow-up; no
lifecycle operation, branch removal or cleanup is scheduled.
