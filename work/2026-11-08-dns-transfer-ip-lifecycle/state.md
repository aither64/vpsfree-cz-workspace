---
lifecycle: active
---

# 2026-11-08-dns-transfer-ip-lifecycle

## Status

- User clarification incorporated: emails are a consequence of the failed transfer classification; root investigation remains why that classification persisted despite equal serials. Monitoring trace explains impact. Missing-user-primary monitoring is a separate improvement. Architect0 and implementer1/2 are steering current packages; no new package or application implementation.

- Phase: investigation and proposed design complete; no implementation or production mutation. Session remains open with active lifecycle for follow-up.
- All four investigation/design packages accepted. Recommendation: repair status reconciliation using a proven positive freshness signal; independently monitor missing user primaries; retain primary references while explicit ownership survives detach.
- Identity verified: `dev-session current` and both environment markers exactly match the thread-bound slug/workspace.
- Saved roster/access verified; architect and three implementers accepted their independent evidence packages.

## Phase checklist

- [x] Verify identity, guidance, roster and investigation scope.
- [x] Correlate central BIND logs with supplied events.
- [x] Trace transfer status and IP ownership behavior.
- [x] Accept evidence and architect's proposed solution.
- [x] Reconcile findings and hand off recommendations.
- Implementation, application checks, independent final change review and deployment: outside current investigation scope.

## Packages and timeline

Dispatch and acceptance occurred around 2026-11-08 14:53–14:54 UTC; precise start times are unavailable. First evidence milestone is approximately ten minutes after dispatch. No overlapping role times are added together.

| Package / deliverable | Owner | Dependencies / acceptance | Status / next evidence |
| --- | --- | --- | --- |
| LOGS / [log-evidence.md](log-evidence.md) | implementer0 | Authorized central log reads; bounded chronology with timezone and gaps | Accepted around 15:01 UTC; both-end peer-transfer evidence, real failures, duplicates and collection limits |
| STATUS / [status-evidence.md](status-evidence.md) | implementer1 | Canonical source reads; exact revisions and status semantics | Accepted around 15:04 UTC; last-attempt projection, monitor predicate/repeats, positive-signal limits |
| IP / [ip-lifecycle-evidence.md](ip-lifecycle-evidence.md) | implementer2 | Canonical source reads; ownership/detach/revocation invariants | Accepted around 15:01 UTC; explicit ownership boundary, deferred cleanup, routed prefixes and direct-owner-transfer guard |
| DESIGN / [design.md](design.md) | architect0 | Combine above reports; minimal proposals, compatibility and checks | Accepted around 15:08 UTC; ranked proposals, proof prerequisite, independent boundaries and explicit evidence limits |

## Next actions

Investigation handoff is complete. Proposed next work is the status-recovery signal proof, explicit-owned IP retention and independent zero-user-primary monitoring condition. Before later implementation, prove a successful same-serial refresh signal using the pinned BIND version and controls for retry/reload/peer effects. This is proposed follow-up, not a currently authorized implementation package. Lead owns tracking and final writing.

## Documentation

- [Combined diagnosis and proposal](design.md): accepted architect synthesis. Lead accepts the conservative referenced A→B rejection as a suitable proposed boundary; this is not an implementation assignment or deployed policy.
- Stable session URL: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-08-dns-transfer-ip-lifecycle/

See [plan.md](plan.md) for scope, evidence destinations and constraints. Evidence is investigation material, so no product documentation update or automatic final change review is triggered.

- [Central BIND chronology](log-evidence.md): accepted LOGS package. Source times are UTC+01:00; manual retransfer came from peer ns4 and fetched the existing serial.
- [IP lifecycle evidence](ip-lifecycle-evidence.md): accepted IP package. Retain explicit-owned detach, preserve existing disown recovery, remove unowned references, and guard ownership reassignment; proposals only.

- [Transfer status and monitoring evidence](status-evidence.md): accepted STATUS packet, including precise predicates, framework behavior and remaining recovery-signal proof.

## Repositories

No session worktrees or feature branches created. Canonical bare source inspection only.

## Commands run

- `dev-session current`: exact expected slug.
- `env | rg '^DEV_SESSION_(SLUG|WORKSPACE)='`: both values match.
- `dev-session team list <verified-slug> --as-is`: retained design/implementation roles have workspace-write access.
- Same-session team assignments: accepted after replacing rejected descriptive message IDs with stable UUIDs. No uncertain dispatch remains.
- Shared workspace status inspected; unrelated dirty paths and index are preserved.

## Results

Final STATUS acceptance: the monitor only fails for the last failed address when still in configured user primaries; zero user primaries pass. It does not use serial/stats/age. One old projection can sustain a monitor event (30-minute confirmation, daily repeats); the two IPv6 raw messages are not two monitor identities. A peer success can clear it without proving original-primary recovery. Missing-primary monitoring must be independent and inspect user associations, not peer-inclusive BIND primaries. Silent-refresh recovery cannot safely be inferred from numeric timer movement without pinned-BIND evidence.

Preliminary evidence checkpoints, 2026-11-08 approximately 14:56–14:58 UTC:

- Central logs: both ns3/ns4 obtained serial `2026110501` November 5; November 6 ns3 unreachable failures match the UI. November 8 manual retransfer obtained the same serial from the replacement address. Absence of zone-specific intervening logs does not prove successful refresh.
- Source: transfer event fields and current serial/loaded/expiry/refresh stats are separate. Stats updates do not clear old transfer errors; some positive notify/up-to-date events are recognized, while transfer-summary messages are intentionally ignored.
- IP route deletion unconditionally removes DNS transfer references even if explicit ownership remains. Disown separately performs asynchronous DNS cleanup before confirming owner/quota changes.
- Proposed retention must account for privileged direct ownership changes. Peer secondaries may remain effective BIND primary sources after the last user-supplied primary is removed; do not equate zero user primaries with zero effective sources.
- Canonical source evidence uses vpsAdmin `origin/master` at `e5e39bf380ebbb469d201f92d62434cd6ebca230` and configuration `origin/master` at `5941cdb3dda259e91c6a988a7dbf08c84700b326`, without fetching or implying these are the exact deployed revisions.

## Remaining evidence limits

- Logs do not prove silent SOA recovery, continuous serving, exact zone-content equality or intended external-primary recovery. Equal serials alone cannot establish these.
- Exact deployed application/configuration revisions, incident-time primary association history and monitoring event history were not queried. Inspected monitor suppresses removed-primary failures, so email persistence cannot be attributed specifically to a removed address without that history.
- Global reloads succeeded but generated include history is unavailable; exact primary-removal time and which other zones received later positive events remain unproven.
- Numeric BIND refresh/expiry timer movement has not been established as a reliable successful-contact signal. A focused pinned-version reproduction is the shortest proof before choosing reconciliation logic.

## Review and checks

- Read-only source/spec/history and central log correlation completed; no application tests, builds or CI were run because there are no application changes.
- Mandatory-change-review skill inspected: investigation, evidence, design reconciliation and tracking alone do not trigger automatic final review; no substantive implementation/configuration/product-documentation deliverable was produced.
- Evidence whitespace/newline checks reported no errors; raw log artifacts are ignored and will not be staged.
- Shared workspace origin fetched before initial investigation tracking commit; local master is ahead of origin/master and not behind. No unrelated commits will be pushed or rewritten. All owned Markdown/evidence links and trailing whitespace checked. No hook framework is declared in the workspace; ordinary Git hooks remain enabled.
- Initial substantive tracking commit contains only this session’s plan/state/portal and investigation/design records. No second same-day tracking commit planned.

## Cleanup

No machines, clusters, temporary services or feature worktrees acquired. Session remains open.
