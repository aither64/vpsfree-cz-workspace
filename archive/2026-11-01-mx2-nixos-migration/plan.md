# mx2 NixOS migration and automated verification

## Nov6 current checkpoint: public cutover and managed-key removal verified

Public IPv4/IPv6 SMTP, trusted TLS, relay denial, DNS/PTR and both primary
connection paths passed. One additionally authorized message was forwarded to
the primary and the user confirmed receipt. No further mail test is needed.

The requested aither.aitherdev removal is now deployed at fe7a8c11/system5gjb;
actual managed absence, retained other keys, healthy SSH/mail and empty queue
passed. The user's manual authorized_keys file is byte/metadata-identical and
remains their later removal action. No reboot or additional source/input update.
The final feature series is three implementation-focused commits, not rollout
history. Prior mistaken history dispositions are superseded in the review record.

User "okay, you can merge it when done" authorized this feature into
vpsfree-cz-configuration/master. Exact final5941cdb3 was independently reviewed,
built and fast-forwarded/pushed to master on Nov6; fresh remote proof passes.
Rebase preserved the three patches and adopted master inputs without runtime
changes beyond provenance. Actual deployedfe7 remains healthy and equivalent;
no extra activation or reboot was needed. Repository and machine claims are
released. See [state](state.md), [review](staging-review.md) and
[deployment receipt](public-profile-preparation.md).

Monitoring-consumer activation and old-VPS retirement remain separate. Preserve
old2992 disk/shell and recovery state. The user may remove their manual SSH key;
the managed copy is already absent. Session remains active for the separately
scoped monitoring rollout; no archive/delete/stop action is authorized.

## Nov5 preparation snapshot

On 2026-11-04 the reviewed084488 build was deployed to VPS27627/private172.19.9.22.
Clean reboot completed the new system transition. User-authorized reset of unused
Postgrey state resolved the5.3→4.8 library/log incompatibility with original state
retained in a protected backup. No source/package correction was needed; a DNS
draft was removed after actual clean-boot DNS proved healthy.

The real primary accepted both marked podpora messages. The second retained its
exact full payload/envelope across a Postfix restart and VPS reboot while only
candidate-to-primary SMTP was blocked; the exact fault was removed and the queue
drained. [Final result](candidate-deployment-result.md) and [state](state.md) hold
source/artifact/claim and verification evidence. The user confirmed both messages arrived; mailbox receipt is verified.
Source/default integration and public-address cutover remain separate.

On Nov5 the user asked for concrete ownership/steps, corrected the unnecessary
second reboot, and said "agreed, proceed". Prepare/review/build/copy two native
configurations using the deployed inputs and private172.19.9.22: TLS bootstrap
with the current source-only SMTP ACL, and final public SMTP. Ordinary switches
are planned; no publicIP is needed during preparation, no new OS/input update or
reboot is planned. [Current owner checklist](staging-plan.md) gives the exact
order; [released design](design.md) owns source/check boundaries. Architect0 owns
the brief, implementer0 owns the complete source package, and lead owns review,
build/copy coordination and the eventual operator handover.

The user identifies the old CentOS VPS as2992 and confirms shell access without
its publicIPs. Candidate is27627. The later handover removes the exact public
routes/hostaddresses from2992 before assigning them to27627, preserving private
management and bothqueues/disks. Certificate issuance and the two ordinary
switches follow that transfer; final SMTP opens only after trustedTLS verification.
Use current tested shared mail policy for this migration; recipient export/sync
and broader SPF/DMARC changes remain followups. No more mailpayloads are authorized.

Public preparation is now complete: reviewed bootstrap27fcf245/native generation
2026-11-05--13-04-34 and finalb120342c/generation2026-11-05--13-11-54 built and
copied successfully. Final mx2 plus four actual monitoring consumers built; DNS
behavior and baseline VM coverage were reused with exact evidence. One strict
read-only guest check verifies both copied identities, unchanged running084488,
healthy services/private network and queue0. See
[public-profile-preparation.md](public-profile-preparation.md) for complete evidence.
The user-facing next step is the old2992 queue/IP handover, followed by lead-owned
bootstrap/certificate/final-switch verification. No source or build work remains
in this preparation package; source integration needs later fresh-target work.

## Prior staging preparation scope (executed)

On 2026-11-03 the user agreed to deploy a separate candidate with different IPs,
verify it, then replace the existing mx2 addresses after acceptance. They asked:
"create a plan and tell me what to do. I can deploy mx2 if it is ready and then
we can proceed with verification."

Architect0 completed the staging plan and the executable package at the top of
[design.md](design.md). The user subsequently authorized agent deployment:
“done. well, with this access, you can deploy mx2 yourself.” Lead owns candidate
deployment and verification; integration, public DNS/IP transfer, primary
configuration and old CentOS changes remain excluded.

Confirmed candidate: VPS27627, private172.19.9.22, hostname mx2, NixOS25.05/LXC,
installed stateVersion25.05 and persistent ZFS. Strict root SSH works with the
user-verified host fingerprint and approved workspace key. The current original
system is the rollback reference, not the intended new branch deployment.
Observed workspace source172.16.106.40 selects the staging SMTP firewall rule.
The guest has no public/globalIPv6 address. Public allocation is not required for
initial staging; public IPv4/IPv6 and final-source acceptance remain later gates.

Implementer0 owns the complete two-file staging package: confirmed identity and
shared mail policy retained, private address metadata, automatic updates and
production monitoring/logging disabled, candidate-only public resolver, SMTP only
from the observed workspace address. Quick checks/commits/history and publication
precede independent final review, then the necessary system/consumer builds.
Reuse prior mail test results only with exact derivation/input identity.

The user supplied podpora@vpsfree.cz as the important support mailbox. Live scope
is at most two clearly marked small synthetic messages (normal and temporary
queue/recovery), same return address, no deliberate live failure/DSN campaign.
User receipt confirmation suffices; no mailbox credentials are requested.

Historical admission was resolved by the user's workspace update and native
schema2 repository-machine identity. No catalog edit is needed. Claim13ba remains
held for the deployed target; private activation and the two controlled live
messages completed successfully, as recorded above and in state.md.

## Completed automated-verification phase

User now asks to minimize their input and let the agent perform verification.
Authorization wording: “not really sure how you suggest to proceed. I'd like to
minimize my input during the verification and let you do it.” This extends the
previous proposal-only scope to executable isolated tests and necessary candidate
fixes. Production cutover/deployment, default integration, mail submission to real
recipients and primary/old-MX reconfiguration remain outside the current work.

Additional user direction: “you can fixup the internal zone if the mail records
do not correspond to the public DNS -- the public DNS is correct, the internal
is probably stale”. Align source internal mail MX/A/AAAA records with current
public DNS as the operator-designated authority, preserving unrelated split-DNS
records and incrementing SOA serial. No live reload/deployment implied. This is a
separate logical source change and test/build acceptance package.

Deliver a repeatable conventional isolated SMTP test reusing production mx2 mail
configuration. Fix proven relay/firewall defects and any test-discovered candidate
failures without inventing a new mail architecture. Cover allowed/denied relay,
message content/envelope forwarding, outage queueing, restart persistence and
recovery, temporary/permanent SMTP responses, IPv4/IPv6 and relevant filtering/TLS
behavior. Explicitly record fixture overrides and remaining real-primary limits.
Prefer existing NixOS VM-test tooling; architect establishes available infrastructure
and stable implementation boundary first. No dependency refresh campaign.

Architect0 completed the executable brief in design.md. Implementer1 completed
the bounded baseline and DNS source package, then released repository writes/Git
to implementer0. Implementer0 completed configuration, tests, documentation,
quick checks, commits and follow-up fixes. Lead accepted the packages, coordinated
independent reviews and completed the required verification using the documented
parent fallback after utility readiness was unavailable.

The prior branch recovery/build remains delivered and its evidence is preserved.
The full isolated mail suite and all five affected-system builds passed.
[Final results](verification-results.md) and [state](state.md) record the final
published head, reviewed ranges, exact successful derivation/input reuse and
actual native build provenance. No further check or source change remains in
this phase. User input is reserved for genuinely unavailable essential
facts or production-affecting decisions; ordinary fixture/implementation choices
are autonomous.

## Goal and scope

Locate the NixOS backup-mail-server branch in
`/home/aither/workspace/vpsfree.cz/vpsfree-cz-configuration`, copy its committed
history into this workspace, and rebase onto current upstream defaults. Preserve
the source checkout and original refs. Suggest evidence needed before replacing
the CentOS 6 mx2. Production deployment and default-branch integration are outside
this request.

## Affected repositories

- `vpsfree-cz-configuration`: expected owner of mx2 configuration.
- Additional repositories only if source history proves an unmerged dependency;
  architect identifies these before expanding execution scope.

## Approach and owners

1. Architect `architect0`: locate source refs, inspect dependencies and mail
   behavior, record design and verification brief in `design.md`.
2. Implementer `implementer0`: import exact source history, create/register the
   session worktree, rebase onto fetched default, resolve bounded compatibility
   issues, run quick checks, preserve old/new ranges and publish feature branch.
3. Lead: accept evidence, maintain scope/tracking, coordinate independent final
   review of committed substantive configuration before long checks.

Use one implementer for this dependent repository package; other implementers
are retained and available only for demonstrated independent work.

## Primary mail server context

User clarification: the primary mail server runs Debian 13 and is managed outside
`vpsfree-cz-configuration`. This is operator-supplied topology information, not a
live inspection. The repository's references to `prasiatko-mail.vpsfree.cz` do not
provide its actual MTA configuration, recipient policy, TLS settings or trust rules.
Debian version alone does not establish the MTA or its configuration.

The isolated primary/sink should model the agreed SMTP responses. Final
preproduction verification must include delivery from candidate mx2 to the actual
Debian 13 primary using agreed test recipients, including recipient rejection,
TLS negotiation and acceptance of the candidate's sender/address identity.
Obtain actual primary-side behavior/configuration from its operator when preparing
those checks; no primary reconfiguration is implied by this clarification.

## Compatibility and deployment

Assess SMTP relay policy, primary-MX routing, TLS, IPv4/IPv6 and durable queue
behavior. Do not assume a CentOS Postfix spool can be copied to modern NixOS:
propose queue draining and retaining the old host for rollback. Establish any
supported mixed-version or input/module compatibility from source evidence.
No production credentials, live mail, network identity changes or deployments.

## Documentation and readers

Operators need a staged verification proposal and cutover/rollback acceptance
criteria; preserve these in session design/findings for this requested proposal.
Record exact refs, rebase resolutions, check results and unresolved risks in
session state and linked evidence. The new authorized verification phase adds only the smallest conventional repeatable test needed; avoid a generalized framework.

## Verification

Quick checks follow repository instructions and available declared tooling:
Git range/diff integrity, formatting and Nix evaluation for mx2 as feasible.
Independent review covers full branch history, final diff and migration provenance.
Long builds/tests use a fresh policy watcher if required. Proposed runtime tests
must distinguish isolated repeatable checks from production acceptance evidence.

## Decisions

- Initial scope: branch import/rebase and verification recommendation; delivered.
- Completed: isolated verification, private candidate deployment and two user-confirmed deliveries.
- Current scope: prepare/review/build/copy bootstrap and final public configurations at frozen inputs.
- Existing candidate deployment authority persists; no default integration or public-address transfer has been performed or approved by the preparation release.
- Session remains open and active.
