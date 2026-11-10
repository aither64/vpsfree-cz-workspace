# Meet DNS aliases

Design owner: `architect0`. Package A is complete; package B has a sufficient
settled brief and is ready for lead acceptance/allocation to `implementer0`.
The lead accepted the minimal private target-chain correction and preservation
of the existing `meet-dev` route in the current-package clarification.

## Scope and evidence

Add these records to both `vpsfree.cz.` views, with explicit 300-second TTLs:

| Owner relative to vpsfree.cz. | Type | Absolute target |
| --- | --- | --- |
| `auth.meet` | CNAME | `meet.vpsfree.cz.` |
| `auth.test-meet` | CNAME | `test-meet.vpsfree.cz.` |
| `turn.meet` | CNAME | `jvb1.vpsfree.cz.` |
| `turn.test-meet` | CNAME | `test-jvb01.vpsfree.cz.` |

Only `vpsfree-cz-configuration` is affected. Investigation used its canonical bare
repository without checking out, fetching or modifying application files. The
inspected remote-tracking baseline is `origin/master` at
`959e1d54cabc7ac5530dac6179acacb077a57754`; local bare `HEAD`/`master` is older,
`86e19685313270d88e4db30038c056ce4b807abd`. The relevant zone/inventory comparison
shows unchanged Meet data between these refs. Use a fresh fetched remote master
for implementation; do not base the feature on the older local master.

| Relevant owner(s) | Public view | Private view | Decision |
| --- | --- | --- | --- |
| `auth.meet`, `auth.test-meet`, `turn.test-meet` | Absent | Absent | Add requested CNAMEs in both views. |
| `turn.meet` | Absent | A `37.205.14.152`; AAAA `2a03:3b40:fe:76::1` | Replace both private address records with the requested CNAME; add public CNAME. |
| `meet` | CNAME `meet-nixos.vpsfree.cz.` | CNAME `meet-dev.vpsfree.cz.` | Preserve both existing routes: each ends at `37.205.14.113`. |
| `meet-dev` | CNAME `meet-nixos.vpsfree.cz.` | A `37.205.14.113` | Preserve this harmless structural difference. |
| `meet-nixos`, `meet-dev1` | A `37.205.14.113`; CNAME `meet-nixos.vpsfree.cz.` respectively | Absent | Not needed by the requested private chains; do not add. |
| `jvb1` | A `37.205.14.138` | A `37.205.14.138` | Preserve. `data/meet.nix` independently agrees. |
| `test-meet` | CNAME `test-meet-nixos.vpsfree.cz.` | Absent | Add the same private CNAME. |
| `test-meet-nixos` | A `37.205.13.90` | Absent | Add the same private A record. |
| `test-jvb01` | A `37.205.14.250` | Absent | Add the same private A record. |

Use 300-second TTLs for the three added private target-chain records, matching
their public definitions. The private view is authoritative for the entire
zone, so its missing targets cannot be repaired by forwarding public queries.

Bounded history confirms public test records were added by
`347cf749c6f54b1fe21ec4498dc71034a52114fb` on 2024-11-20 without private equivalents.
Commit `149bd34ac2acf6d886163461995686e2f552a19d` on 2024-01-08 removed old public
Meet records, including already-commented legacy `turn.meet` addresses that
remain active privately. Private `conference.meet`, `jicofo.meet`, `jvb1.meet`
and `jitsi-videobridge*.meet` also retain old-installation records. Their current
use was not audited, and deleting them is unnecessary for the requested aliases.
The existing `jvb1` through `jvb11` address inventory agrees across the views.

No live DNS or service-health claim is made by this source investigation.

## Package B: zone implementation and review evidence

Owner: `implementer0`; routine technical clarification peer: `architect0`.
Lead owns scope, allocation, acceptance, plan/state/portal and review dispatch.

Deliverables and exclusive application file boundary:

- `configs/public-dns/zone.vpsfree.cz.`: four CNAME additions and SOA serial bump.
- `configs/internal-dns/zone.vpsfree.cz.`: three CNAME additions, replacement of
  the existing `turn.meet` A/AAAA pair with its CNAME, three missing test-chain
  records, and SOA serial bump.
- Compact check and branch evidence under this session's existing tracking
  directory for the lead's review packet; no generated artifacts or rollout
  receipts committed to the configuration repository.

No Nix modules, inputs, inventory, persistent test framework or unrelated zone
records need changing. Match nearby zone formatting and record grouping.
Current observed serials are public `2026092800` and private `2026110600`.
Use `2026111000` in each if still greater than the fresh baseline, otherwise
advance each serial appropriately; never lower a serial. Preserve private
`@fqdn@` substitution and the existing SOA/NS policy.

Dependencies: lead acceptance of this brief; initial plan/state commit (lead
reports `df71e511f`); fresh remote-base inspection and registered initiative
worktree. All technical decisions relevant to these files are settled. No
other package or investigation blocks implementation.

The package includes normal feature setup, required hooks, edits, quick checks,
commit, SSH branch publication and final evidence. Before those phases read
the workspace Git, commits, lifecycle (worktree registration), verification
procedures and repository AGENTS.md in full. Register/use only this session's
`worktrees/2026-11-10-meet-dns-records/vpsfree-cz-configuration` worktree and dated
feature branch. `implementer0` owns its edit/index/commit/push window; no other
member is assigned edits there. No repository merge claim is needed for this
feature work. No deployment or default-branch integration is included.

Acceptance:

1. All eight requested view/alias combinations have exactly the requested CNAME,
   absolute trailing-dot target, and 300-second TTL.
2. Each target chain terminates within its view at the expected IPv4 address:
   `auth.meet` → `37.205.14.113`, `auth.test-meet` → `37.205.13.90`,
   `turn.meet` → `37.205.14.138`, `turn.test-meet` → `37.205.14.250`.
3. No CNAME coexists with A/AAAA or other ordinary record data at its owner;
   specifically both old private `turn.meet` address records are removed.
4. The existing private `meet`/`meet-dev` route, intentional private addresses,
   unrelated legacy Meet records and all other zone records remain unchanged.
5. Both zones parse, SOA serials advance, hooks pass, and evidence identifies
   exact base/final head and published branch. Any fresh-baseline change affecting
   these contracts is reported before implementation is broadened.

## Verification plan

Quick batch: inspect final diff and `git diff --check`; run BIND
`named-checkzone vpsfree.cz. <zone-file>` on the public file and temporary private
renderings. Replace `@fqdn@` using the same literal substitution as
`configs/internal-dns/default.nix`, separately for `ns1.int.prg.vpsfree.cz`,
`ns1.int.brq.vpsfree.cz`, `mon1.int.prg.vpsfree.cz` and
`mon2.int.prg.vpsfree.cz`. Do not edit the checked-in template for validation.
Use the repository's pinned Nix environment; if BIND utilities are absent,
resolve `nixpkgs#bind` with `nix shell --inputs-from .` rather than selecting an
unrelated tool version or changing inputs.

Use BIND's canonical dump (`named-checkzone -D -o <temporary-output>`) or direct
record inspection to establish all eight exact CNAME mappings, the three added
private target records, absence of old private `turn.meet` A/AAAA, and resolution
of each chain to the four addresses above. Check the before/after diff to prove
unrelated private records remain unchanged. This is direct data validation;
do not add a committed test suite that mirrors these few zone records.

Evidence includes exact command/results, tested revision, changed-file inventory,
base-to-head commit list, final diff, remote published head and gaps. State
explicitly: no database migrations, no schema/input changes, no deployment by
this package. Preserve warnings with context; CNAME-to-CNAME paths are intentional.

After intended changes are committed and quick checks pass, the lead invokes
mandatory independent review including whole-branch history/migration conclusion.
No long integration test or full machine build is needed solely for a static
zone-data edit. If deployment is later assigned, build only its affected DNS
consumers, after final review, using the required fresh verification watcher for
long or uncertain builds. New module changes or failed checks require revisiting
that scope, not launching broad fleet verification.

## Compatibility, deployment and recovery

This changes standard DNS data only: no persisted application format, database,
API/client/CLI/Terraform contract, daemon protocol, Nix module option or input
version changes. Existing BIND versions accept the new records. Rollback can
read existing state. No coordinated node/OS upgrade is needed.

The intentional behavior change is private `turn.meet`: it stops returning the
old IPv4/IPv6 pair and follows `jvb1` to `37.205.14.138`, with no IPv6 address at
that target. New auth/test aliases are additive. TLS certificates, HTTP/XMPP/TURN
configuration and endpoint availability remain separate from DNS correctness.

For a later authorized rollout, public zone content is consumed by
`cz.vpsfree/containers/ns1`; the existing public secondary configuration transfers
it to ns0/ns2/ns3/ns4. Private template consumers are
`cz.vpsfree/containers/{prg,brq}/int.ns1` and
`cz.vpsfree/containers/prg/int.mon{1,2}`; the monitors also serve local authoritative
copies and must be considered when checking private consistency. No secondary
configuration edit is needed. Follow installed coordination guidance and machine
ownership before any activation; this brief is not deployment/merge approval.

Roll out incrementally and inspect SOA/authoritative CNAME and terminal A answers
against the updated servers, then verify public secondary propagation and all
private copies. Existing private positive and negative caching can preserve old
answers or missing names for up to one hour; new 300-second TTLs do not flush old
caches. Temporary mixed views during rolling reloads are expected, not a schema
incompatibility. Keep existing service checks plus targeted alias queries; do
not claim conference or TURN functionality from DNS answers alone.

If a correction must be undone after publication, restore previous record content
with a new SOA serial higher than the highest published serial. Simply deploying
an old generation/zone serial can prevent secondary refresh. Validate restored
data and propagation in both views. This preserves the DNS recovery rule already
documented in `docs/operations/newadmin-webui.md`.

The zone data and existing operational guidance are sufficient long-lived
documentation for this small change; no new project runbook is warranted.
Investigation/rollout evidence belongs in this session. Lead should link this
brief from plan/state under the ordinary tracking cadence.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-10-meet-dns-records/>
