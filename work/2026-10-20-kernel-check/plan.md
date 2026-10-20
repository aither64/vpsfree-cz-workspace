# Kernel hang investigation

Investigate whether custom vpsAdminOS kernel patches changed between Linux
6.12.95 and 6.12.113 can explain node24.prg becoming unresponsive while its
console cursor continued blinking at the login prompt. Upstream stable patch
regressions are deferred until the custom patch audit yields no supported cause;
the user subsequently authorized upstream investigation on that condition.

## Scope and approach

Read vpsadminos and linux canonical repositories for exact version provenance,
custom patch inventory and semantic comparison. Read production configuration
only if required to establish deployed versions. Examine node24 records on
log.int.prg.vpsfree.cz with bounded read-only queries. Preserve concise evidence
and exact revisions in this session, without exposing credentials or unrelated
container logs.

The architect owns design and causal synthesis; implementer0 owns patch
provenance/inventory; implementer1 owns central logs. Three added implementers
will own independent source-analysis packages identified by the architect.
Lead owns coordination, acceptance and session records. Findings require an
obvious concrete source failure chain with reachable conditions, or verification.
Keep code defects distinct from proof that they caused this incident.

## Compatibility and deployment

Investigation only: no application edits, kernel build, deployment, production
mutation, persistent format/API/schema change or coordinated node update.
Any later reproduction must use an isolated environment and an explicit brief.
No integration, lifecycle closure or cleanup is authorized by this investigation.

## Acceptance and verification

- Establish exact old/new custom patch revisions and distinguish context-only
  rebases from semantic changes.
- Establish incident/reboot window and kernel evidence from central logs.
- Audit changed custom paths for hangs, locking, lifetime and compatibility.
- Report supported conclusions, eliminated leads and remaining uncertainty with
  source references and log evidence; do not infer causality from symptoms alone.
- Evidence and findings remain session artifacts; no product documentation
  change is useful unless investigation leads to an implemented change.

## Scope and evidence decisions during investigation

- User added three retained implementers, used for independent source lanes.
- User authorized upstream Linux investigation if custom audit yielded no
  supported cause. Full custom delta accounted first; then targeted upstream
  memory, NFS/RPC, scheduler/RCU/locking, platform and printk intersections.
- User confirms normal panic should crashboot/upload and none occurred; user
  also confirms no runtime sysctl changes. Repo-configured policy therefore
  applies. Sources establish softlockup panic1 but hardlockup panic0; this
  explains a possible missing-dump path without proving hardlockup occurred.
- Kdump loaded is positively logged26.5min before lastlog. Hardware VGA cursor
  can blink independently of scheduler progress. Neither observation attributes
  the hang.
- Proven source bugs are documented separately from incident attribution; no
  candidate establishes a host-hang chain or justifies blind reproduction.
  No source/config changes, builds, tests, deployment or merge is planned.
