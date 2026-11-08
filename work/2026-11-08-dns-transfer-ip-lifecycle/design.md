# DNS transfer classification and IP ownership: findings and proposal

Owner: architect0. Investigation and design only, 2026-11-08. This document
proposes future work; no application change, migration, test run, deployment or
production repair has been performed. Lead owns package acceptance, plan/state
and the response to the user. Implementation requires a subsequent assignment.

## Scope and evidence

Explain the `avting.cz` ns3 failures, unchanged ns3/ns4 serial and effect of the
manual retransfer; explain resulting repeated monitoring mail without treating
email as the underlying defect. Propose preserving DNS primary references while
an allocation stays owned, and monitoring missing user-primary configuration.

The bounded evidence packages are:

- [BIND chronology](log-evidence.md), implementer0: retained central ns3/ns4
  logs, November 5–8, explicit `+01:00` timestamps and collection limits.
- [Status and monitoring](status-evidence.md), implementer1: parser, supervisor,
  statistics, monitor lifecycle and UI semantics.
- [IP lifecycle](ip-lifecycle-evidence.md), implementer2: ownership, cleanup,
  rendering, visibility and transaction guarantees.

Source findings use locally available remote-tracking revisions:
`vpsadmin` `e5e39bf380ebbb469d201f92d62434cd6ebca230` and
`vpsfree-cz-configuration` `5941cdb3dda259e91c6a988a7dbf08c84700b326`.
They were not fetched or verified as deployed revisions. Exact file/line
references and commands are in the evidence packages. No other session's
worktree or records were used.

## Diagnosis and confidence

The November 6 contacts really failed. The misleading part is interpreting the
latest recorded failed attempt as the zone's continuing synchronization state.
The application stores these separately: BIND statistics can report a loaded
zone and unchanged serial while `last_transfer_*` still describes that failure.
Only a later recognized positive event replaces it. The inspected site monitor
uses that last result as an ongoing error condition when its address remains a
configured user primary.

| Evidence | Conclusion and limit |
| --- | --- |
| Nov 5 17:38:36: ns3 transfers serial `2026110501` from `2a03:3b40:fe:2ef::1`; ns4 obtains the same serial from ns3. | Both acquired that serial before the incident. |
| Nov 6 06:36:33/35: IPv6 connection and IPv4 refresh report `host unreachable`. | Real failed primary contacts; neither proves an expired, unavailable or out-of-date served zone. Two IPv6 rows correspond to two messages from one BIND transfer handle. |
| No subsequent zone-specific line until Nov 8 15:42:21; all 88 incident-hour buckets contain other named messages on each host. | No recognized logged recovery is available in the retained interval. This cannot establish what silent SOA refreshes did or exclude selective log loss. |
| Nov 8 forced transfer fetches `2026110501` from `37.205.11.85`; ns4 logs the matching outgoing AXFR. | Retransfer obtains the same serial from peer ns4 and supplies a positive completion event. It does not demonstrate recovery of either original user primary. |
| Statistics update serial/loaded/expires/refresh independently of transfer events. | Matching serials do not clear the recorded failure. They also do not prove primary reachability, freshness or exact content equality. |
| Monitor fails only for a last failed address still present in existing user-primary associations. | A historical failure can cause daily repeats without new failures. A removed primary, zero user primaries or a peer success passes this check. |

The stale-classification mechanism is established in source and consistent with
the chronology. A successful silent refresh before the manual retransfer is
**not proven**. Neither are continuous serving, historical configuration,
incident-time associations, deployed code/configuration, or monitor event history.
In particular, repeated emails cannot be attributed to an address after its
removal unless it remained/reappeared in the database or deployed monitoring
behaved differently. A peer transfer can clear the inspected monitor while the
intended upstream is still unreachable or absent.

The report that only this zone had the problem is compatible with per-zone
differences in primary lists, later NOTIFY/completion events or monitor state.
Other-zone histories were not inspected, so this is an explanation to test,
not an established cause. Earlier BADKEY messages precede a successful TSIG
transfer and do not explain the later `host unreachable` result.

## Ranked recommendations

### 1. Reconcile current synchronization from positive evidence

Keep transfer history and `last_transfer_*` as facts about the last recorded
attempt. Do not erase actual failures, mark success because serials match, or
hide failures after an arbitrary timeout. The corrective goal is to stop using
one old per-primary attempt as the sole continuing zone-health classification.
Email behavior follows the corrected classification; UI wording alone does not
solve it.

Use three distinct questions in the existing status/monitoring paths:

1. What was the last recorded attempt and its address/time/result?
2. What do recent observations establish about this secondary's synchronization
   and ability to serve the zone?
3. Does the zone still have its intended user-configured source, and what is
   actually known about reaching that source?

A peer success answers a narrower question than successful contact with a user
primary. Local BIND collection and a loaded serial answer neither contact
question. Preserve those limits in any resulting state or message.

**One prerequisite remains before choosing implementation:** reproduce one
failed contact followed by a real successful same-serial SOA refresh with the
deployed/pinned BIND version; capture its logs and statistics XML. Determine
whether an existing reliable positive signal can be consumed. The current code
only passes through XML timers. No safe numerical rule for `expires_at` or
`refresh_at` has been established; advancing next-refresh may just be a retry.
Test reset/reload and peer-refresh effects before relying on expiry advancement.
This focused proof is future work, not a prerequisite for this investigation's
handoff or a reason to build a new monitoring subsystem now.

An explicit `Transfer status: up to date` could be treated as a positive
no-change outcome instead of ignored. This is a small parser candidate, but
normal following completion already produces success, and this line was absent
from the incident interval. It does not fix a genuinely silent refresh and must
not be presented as the incident fix. Consider duplicate positive outcomes if
both status and completion are consumed.

### 2. Alert independently when no user primary is configured

Add a condition through the existing monitoring framework for an enabled,
external zone belonging to an active user with zero existing user primary
associations: `dns_zone_transfers.primary_type.existing`. Use the established
`confirm_create`/`confirmed` boundary; exclude pending destruction. Prefer one
monitor event per `DnsZone`, so the same configuration problem is not repeated
once per secondary. Clear it when a valid user-primary association returns.

Do not use `DnsServerZone#primaries.empty?`: that list also contains peer
vpsAdmin secondaries. Peer transfers and a current loaded serial cannot clear
missing-source configuration. The existing transfer-failure monitor explicitly
passes when no matching user primary exists, which explains this coverage gap.
Reuse existing confirmation/repeat/cooldown machinery; no new notification
subsystem or history migration is needed.

### 3. Preserve DNS primary references across owned detach and move

Ownership belongs to the parent `IpAddress` allocation, including routed
prefixes. Preserve host records and DNS associations while that allocation has
an explicit `user_id`; detach does not remove that owner or its quota. A move
between VPSes owned by the same user should retain the same transfer/TSIG
references without re-adding them zone by zone.

Gate both destructive paths in `NetworkInterface::DelRoute`: the unconditional
DNS transfer-removal loop and shared host cleanup. Environment ownership policy
is not a substitute for the actual owner: an explicitly owned allocation must
survive even if the environment currently disables new ownership. Preserve
unowned cleanup, disown, account release, host deletion and VPS-owner-change
behavior. With no explicit owner, detachment ends inherited VPS ownership and
must remove the references before reuse by another user.

Keep the retained address in BIND's primary list. Show a per-reference
configuration warning when its **parent allocation** has no network interface.
Do not use the host's `assigned?` flag: an unassigned host inside an attached
routed prefix can be a valid DNS endpoint. Reattachment clears the diagnostic;
detachment itself does not fabricate a transfer-failure event. Missing all user
primaries remains a separate configuration error and monitor condition.

Use existing transfer association expansion for the warning. Direct user
HostIpAddress Show/list currently excludes detached hosts through an inner
interface join; included associations have different visibility. Do not make
the warning depend on a direct detached-host lookup or broaden API visibility
incidentally. Expanding the add-primary selector is not required for retention.

**Ownership-change boundary:** direct administrator A→B transfer of a detached
allocation currently changes owner/quota without DNS cleanup. The smallest
proposed guard is to reject that change while DNS references remain, under the
existing IP reservation, requiring explicit reference removal first. Preserve
same-owner no-ops and reference-free transfers. Lead acceptance is required for
this consequential behavior choice. Automatic cleanup before transfer is an
alternative, but would need deferred owner and both quota changes behind one
chain; it is unnecessary for the smaller proposal. Never split cleanup and
ownership change into independently confirmed chains.

## Invariants and interfaces

- Historical failed attempts remain auditable. Same serial, local collection,
  reload or elapsed time is not synthesized as successful primary contact.
- Any current synchronization recovery must be supported by a newer observation
  with explicitly documented meaning. Peer recovery does not certify upstream
  reachability or resolve absent user configuration.
- Explicit owned detach preserves references, host identity, TSIG and quota;
  unowned detach or ownership release/change cannot carry old-owner references
  into another user's allocation.
- Preserve parent-IP-before-host reservation order, current ownership checks,
  DNS configuration rollback, and deferred disown ownership/quota confirmation.
  Failed cleanup retains ownership/accounting; fatal chains retain recovery
  reservations. Do not weaken existing recovery by clearing locks.
- Configuration diagnostics describe allocation attachment separately from
  BIND reachability. Peer sources remain useful failover sources, not substitutes
  for a configured user source.
- Existing API/protocol fields retain their meaning. No migration, generated
  client interface change, DNS wire change or vpsAdminOS change is selected.
  Any later need for an additional freshness field must return to the design
  owner/lead with the positive-signal proof and compatibility impact.

## Proposed packages and release boundaries

These are future allocation candidates, not currently executing assignments.
Lead accepts releases and confirms owner capacity. Routine clarification stays
between the named same-session peers. Sequence shared files and Git mutation
windows under lead ownership.

| Package / proposed owner | Deliverable and file boundary | Dependencies and acceptance |
| --- | --- | --- |
| Recovery-signal proof / implementer1 | Bounded real-BIND scenario and compact observations; existing `libnodectld` DNS parser/status specs and `tests/suite/dns/secondary-transfer-errors.nix` are candidate homes. | Needs exact BIND/runtime identity and one failure→same-serial recovery. Stop after identifying reliable signal or proving current telemetry insufficient. Not a broad test campaign. |
| Classification reconciliation / implementer1 | Small change to existing `libnodectld/.../dns_transfer_log.rb` or `dns_status.rb`, API DNS supervisor consumers and site `configs/vpsadmin/api/monitoring.rb`, only as required by proven signal. | **Blocked:** reliable recovery contract not settled. Preserve audit and origin distinction; do not select a timer threshold or state schema now. |
| Missing-user-primary condition / implementer1 | Existing site monitoring definition, focused condition fixture and operational explanation. | Predicate is settled and independent of signal proof. Must fail for peer-only configuration, produce one zone event and clear on valid user-primary restoration. Lead accepts exact persistence/repeat settings before release. |
| Owned-reference retention / implementer2 | `api/models/transaction_chains/network_interface/del_route.rb`, shared cleanup only if necessary, `ip/update.rb` guard, focused specs, `docs/ip-locking.md`. | Ownership boundary settled; lead must accept A→B guard choice. Test both cleanup entry points, policy/owner mismatch, rollback and inherited callers. Independent of freshness proof. |
| Configuration diagnostic / implementer2, text finalized by lead | `webui/forms/dns.forms.php`, existing association expansion, localized catalogs and relevant browser/documentation checks. | Depends on retained-reference behavior and exact UI query ownership. Parent-interface absence is settled; no new API field assumed. Lead owns user-facing writing. |

No package is released by this document alone. Unrelated open freshness design
need not delay the independent missing-primary or retention work if the lead
later authorizes implementation. No separate role, service or subsystem is
proposed.

## Compatibility, deployment and recovery proposal

Retention and a site monitor can use existing data formats, DNS node commands
and monitor storage. Old clients can read the same associations. API behavior
work still requires the repository's final-source Go/Rust/TypeScript generated
client assessment even if the schema remains unchanged. Visible diagnostics
require localization and the external KB contract workflow. No client release
or public KB publication is authorized here.

Deploy all API ownership writers with the same retention/ownership-change
boundary before promising it to users; old writers can still delete on detach
or transfer an allocation without the new guard. Drain/reconcile in-flight
ownership/DNS chains when coordinating that transition. Deploy any consumer
support before relying on a new producer signal. The recovery-signal package
must define its mixed-version behavior after selecting its actual interface;
no coordinated update of all VPS nodes is indicated by present proposals.

The independent missing-primary monitor can use existing API data and should be
rolled out with an inventory of affected enabled external zones, since it will
surface previously unreported configuration. Preserve established monitor event
identities and document closure of an old condition rather than editing audit
history. Any rollout requires the selected package/coordination procedures and
separate deployment authorization; this is only a proposal.

Software rollback can read retained associations because their format does not
change; it resumes old destructive detach behavior. Reverting code cannot
recover already deleted associations. Do not reconstruct incident configuration
from current IP ownership guesses. Restore an association only with explicit
current authority and intended address/TSIG established. Existing failed-chain
and ownership-accounting recovery contracts remain unchanged.

## Acceptance and checks for later implementation

Quick checks use each repository's declared Nix environment, focused RSpec/lint
and required hooks. No checks below were executed during this investigation.

- Replay actual log forms: preserve the two messages from one failed IPv6
  attempt, reject zero-record serial-0 completion as recovery, accept genuine
  completion/NOTIFY recovery and keep event-key delivery idempotence.
- For a selected recovery signal, test true same-serial recovery, retry-only
  timer movement, reload without contact, stale/reordered samples and peer
  recovery. Assert the signal's meaning before implementing a predicate.
- Monitor: stale failure with and without verified later recovery; removed and
  re-added failed primary; no user primary despite peer-fed loaded zone;
  pending-destroy exclusion; restoration; disabled/internal-zone scope. Reuse
  framework tests for confirmation/repeat/close instead of changing its engine.
- Retention: owned IPv4 and routed IPv6 prefix detach/move preserve transfers
  and quota; detached diagnostic clears on reattach; host order alone causes
  no false warning. Include explicit-owner/environment-policy disagreement.
- Cleanup: unowned detach, disown, host deletion, VPS-owner change and account
  release remove references. Exercise last user primary with peers present,
  multiple primaries, cleanup failure/rollback and reservation protection.
- Ownership transfer: referenced detached A→B rejects before quota/owner
  mutation; concurrent reference creation cannot bypass the guard; same-owner
  and reference-free cases retain supported behavior.

Longer checks, after committed deliverables, quick checks and mandatory review,
should extend the existing DNS integration scenario and relevant network/IP
scenario only as needed. Include real BIND refresh for the unresolved signal;
synthetic injected success logs cannot prove silent-refresh behavior. Use the
required verification watcher for long/uncertain tests. Final evidence must name
exact source/runtime inputs, commands/results and remaining production limits.

## Handoff

Investigation deliverables are ready for lead acceptance. There are no feature
heads, migrations, deployment receipts or application test results to report.
The remaining technical uncertainty is the positive signal needed for faithful
freshness reconciliation; historical deployment/association/monitor state also
limits incident attribution. No further broad investigation is proposed.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-08-dns-transfer-ip-lifecycle/
