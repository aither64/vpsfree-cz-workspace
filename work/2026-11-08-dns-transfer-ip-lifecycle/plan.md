# 2026-11-08-dns-transfer-ip-lifecycle

## Goal

I'd like you to investigate allegedly failed DNS secondary transfer in vpsAdmin.

Here's transfer log in vpsadmin:

```
2026-11-08 15:42:21 	avting.cz. 	ns3.vpsfree.cz 	Successful 	37.205.11.85 	2026110501

Reason code:
    -
Reason:
    -
Message:
    Transfer completed successfully

2026-11-06 06:36:35 	avting.cz. 	ns3.vpsfree.cz 	Failed 	37.205.14.125 	-

Reason code:
    connection_failed
Reason:
    The primary DNS server could not be reached
Message:
    host unreachable

2026-11-06 06:36:33 	avting.cz. 	ns3.vpsfree.cz 	Failed 	2a03:3b40:fe:2ef::1 	-

Reason code:
    connection_failed
Reason:
    The primary DNS server could not be reached
Message:
    host unreachable

2026-11-06 06:36:33 	avting.cz. 	ns3.vpsfree.cz 	Failed 	2a03:3b40:fe:2ef::1 	-

Reason code:
    connection_failed
Reason:
    The primary DNS server could not be reached
Message:
    host unreachable
```

I fixed it by running rndc retransfer on ns3. all the time, both ns3 and ns4 had the same serial.

The user was playing with his VPS & IPs... he removed the IP that was used as his primary DNS server from the VPS, which lead to the IP being removed from the DNS zone. It may be related to this problem, although he has multiple zones and only this one had an issue.

You can read bind logs on central log server at log.int.prg.vpsfree.cz. Please investigate and try to find the problem & suggest a solution. WHile we're at it, I think that removing IP from VPS doesn't have to immediately remove it from secondary zones... it can certainly warn the user and the zone can shown an error in configuration... but as long as the user owns the IP, we don't have to touch the DNS zones. We should definitely handle it on disown... or right away when the IP are not owned at all. Switching the IP to another VPS is legitimate usecase and as it is, we burden the user with readding his IP to all secondary zones. So suggest a solution to this as well.

## Affected repositories

- `vpsadmin`: secondary DNS transfer event/status handling and IP lifecycle.
- `vpsfree-cz-configuration`: read-only reference for BIND logging/collector configuration if needed.
- Coordination workspace: this session's investigation evidence and proposed design only.

## Approach

Investigate and propose solutions; application implementation and production changes are outside this request's current scope. Correlate the supplied incident with central BIND logs and source behavior. Separate failed transfer attempts, current zone contents, current reachability, and historical UI status. Establish timestamp timezone and evidence gaps explicitly.

The architect owns the synthesis in [design.md](design.md). Independent bounded packages collect central logs, status/parser behavior, and detach/disown semantics. Start with November 5–8 and the named zone/addresses; broaden only when a concrete missing fact requires it. First package evidence checkpoint is approximately ten minutes after dispatch. Do not run rndc, reload services, alter configuration, query unrelated tenants, or access another session's worktrees.

## Decisions

- User clarification: monitoring emails are a consequence, not the main defect. The root question remains why the zone was classified as transfer failed despite matching serials; investigate classification/reconciliation and actual reachability without assuming serial equality proves freshness. Trace monitoring to explain impact. Separately, missing all user-configured primaries must raise a monitoring alert even when peer secondaries can still serve/transfer cached data.

- Preserve the user's distinction between temporary VPS attachment and IP ownership when evaluating primary retention.
- Revocation of ownership must prevent old-owner DNS references from continuing to use a reassigned IP.
- Proposed solutions must distinguish operational recovery from permanent behavior changes.
- No feature branches, merges, deployments, or long tests are needed for this evidence-only phase.

## Compatibility and deployment

Assess existing database associations, API/WebUI state semantics, BIND/collector events, transaction ordering, mixed-version deployment, and rollback before recommending implementation. Preserve actual historical failures; do not infer current health merely from equal serials. Any future API additions need generated-client compatibility assessment. No deployment will be executed during investigation.

## Documentation

Readers: operators diagnosing the incident and developers implementing a later approved fix. Keep incident evidence and proposed implementation packages in this session; do not document proposed behavior as an implemented product contract.

- [log-evidence.md](log-evidence.md): central logs, timestamps and limits.
- [status-evidence.md](status-evidence.md): event ingestion and status rendering.
- [ip-lifecycle-evidence.md](ip-lifecycle-evidence.md): ownership and attachment paths.
- [design.md](design.md): combined diagnosis and proposed solutions.

## Testing plan

Use read-only evidence inspection and focused source tracing. No application tests are required without application edits. The proposed design must specify regression cases for unchanged SOA refresh after a failed attempt, changed primary sets, owned detach/reattach/move, disown, and unowned detach. Record unproven hypotheses rather than presenting unexecuted tests as evidence.
