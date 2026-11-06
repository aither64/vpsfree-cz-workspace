# Current boundary: private staging verified; primary filtering interpretation

Private staging at source084488 is complete: both marked messages reached
`podpora@vpsfree.cz`, including queue persistence through service/VPS restart;
services are healthy and the queue is empty. See [state.md](state.md) for current
evidence. Public cutover and default integration remain unapproved. The recovery
checkpoint below is historical, not an outstanding Postgrey failure.

## Released Nov5 package: public configuration, prepared on the private IP

Owner: implementer0, with architect0 for routine clarification and lead for scope,
review, activation and user coordination. User agreed to proceed with source
preparation/review/build/copy. Public transfer, old-host/primary changes, activation
at cutover, additional mail and default integration remain outside this release.
No public IP is needed to edit, review, build or copy either prepared generation.

Keep the actually deployed084488 ref/closure/input receipts. Keep its selected
nixpkgsStable718f670e and vpsadminosOsStagingb45b27b4 inputs and complete lock fixed:
no channel refresh or rebase-induced OS upgrade. The heavy upgrade is complete.
Use ordinary service switches; **no second reboot is planned or required**.
A new concrete reboot requirement would go to the lead, not be assumed.

Implement one small package in the existing host `config.nix`, `module.nix` and
`docs/operations/mx2.md`; leave shared `configs/mx2.nix` and test policy unchanged:

1. In config.nix set `services.postfix.settings.main.myhostname` to
   `mx2.vpsfree.cz`. Retain VPS27627, private management172.19.9.22, stateVersion25.05,
   approved root keys, current resolver and all queue/Postgrey state.
2. Reuse `profiles/ct.nix` ACME account defaults. Define
   `security.acme.certs."mx2.vpsfree.cz"` with native `listenHTTP = ":80"`,
   group matching Postfix, and `reloadServices = [ "postfix.service" ]`.
   Configure `smtpd_tls_chain_files` with `/var/lib/acme/mx2.vpsfree.cz/key.pem`
   followed by `fullchain.pem`, and `smtpd_tls_security_level = "may"`.
   Add Postfix `requires`/`after` on **acme-mx2.vpsfree.cz.service**, the native
   local certificate bootstrap unit, not the order/renew network unit. Preserve
   outbound opportunistic TLS; no mandatory TLS for arbitrary Internet senders.
3. Native pinned ACME always creates preliminary self-signed files in the base
   unit, then starts separate `acme-order-renew-mx2.vpsfree.cz.service` for real
   issuance; renewal uses `acme-renew-mx2.vpsfree.cz.timer`. Postfix otherwise has
   no ACME dependency. Therefore private activation could start with a provisional
   certificate and failed HTTP-01 jobs: **do not activate this preparation before
   public handover**. Build/copy privately; activate after public port80 routes
   here. Do not add a new issuance gate, timer, wrapper, web server or DNS-01 setup.
4. In module.nix prepare public metadata37.205.11.114/32 and
   2a03:3b40:100::1:95/128; preserve private SSH target172.19.9.22 and ID27627.
   These records do not assign guest addresses. Restore ordinary monitoring and
   logging plus the repository's normal node-exporter service metadata/monitor
   ACLs. Preserve existing placement data; do not invent a physical node or
   broaden exporter ingress. Keep auto-update disabled. No monitor/DNS consumer
   deployment follows from preparing its source.
5. Prepare two ordinary native generations, reviewed together. **Bootstrap**
   includes hostname/TLS/metadata/monitoring and TCP80 but retains the exact
   existing SMTP rule allowing only172.16.106.40/32, with general TCP25 closed on
   both families. **Final** differs only by removing that temporary rule and
   allowing Internet TCP25 on both families; SSH/HTTP80/monitor ACLs stay intact.
   Use allowed-port values preserving monitor-specific rules: bootstrap22/80,
   final22/25/80. No custom lifecycle service or permanent staging option.

The final feature history should introduce the final public behavior cleanly.
Preserve bootstrap source under a separate explicit cutover ref and retain both
exact source identities; it is an intentionally consumed transition, not an
unreferenced draft. Owner chooses the smallest ordinary Git construction without
changing inputs or unrelated commits. Review the complete final branch and the
bootstrap-vs-final diff. Record native confctl generations and exact derivation/
output/source/input identities for both; owner resolves the pinned native
build/ref-selection interface as part of execution, without a new launcher.
Never select a later "latest" generation implicitly during cutover.

Retain the tested shared recipient/filter behavior as the migration baseline,
including domain-wide acceptance and possible later bounces for unknown
recipients, absent fail-open milter, Postgrey/RBLs, and the three-domain primary
transport. Primary virtual recipient checks do not eliminate backup backscatter.
Recipient export/sync and SPF/DMARC changes are separate follow-up work, not a
prerequisite for this preparation. No policy-equivalence claim about old CentOS
or proof of primary sender authentication is made.

Acceptance: parse/format/hooks and generated checks cover both host variants,
exact lock/selected-input equality to084488, hostname/HELO, key/chain ordering and
permissions, native ACME/Postfix dependencies and renewal reload, source-restricted
bootstrap vs public final IPv4/IPv6 ingress, unchanged SSH/mail/queue policy, and
normal monitoring metadata/ACLs. Commit all intended source and pass quick checks
before independent review of both source identities. After review build both mx2
variants and only consumers whose actual delta requires a build. Reuse the passed
isolated suite only with exact derivation/input proof; rerun it only if consumed
inputs/config changed. Long checks use the normal watcher policy. Deliver compact
review/build/copy receipts through the existing records; no new framework/bundle.
Lead owns the ordered later switches in [staging-plan.md](staging-plan.md).

## Interpretation of the supplied primary configuration

The following interprets the user-supplied primary Postfix3.10.13 fragment relayed
by the lead; it is not a live effective-configuration audit:

- `reject_unauth_destination` rejects unauthorized relay destinations. An owned
  local/virtual or authorized relay domain continues to later restrictions
  (DUNNO); this does not authenticate its sender or skip later policy/RBL checks.
- In each restriction list, matching `permit_mynetworks` or
  `permit_sasl_authenticated` stops that list. In the supplied recipient list,
  those permits bypass later sender-access, policy60000 and RBL checks.
  `check_sender_access` returning OK/PERMIT likewise skips later checks;
  DUNNO/no match continues. A policy-service OK can skip subsequent RBLs too.
  A permit in one list does not globally bypass other lists or configured milters.
  The candidate's primary-observed/NAT source and resulting trust match are
  unknown. Successful delivery does not establish an open relay or SPF pass.
- The user identified listener60000 as Postgrey and listener12301 as OpenDKIM.
  Postgrey supplies greylisting; OpenDKIM signs/verifies DKIM, not SPF or DMARC.
  No SPF/DMARC enforcement is visible in the supplied Postfix path; this is not
  proof that no other component enforces it. RBL checks concern client reputation,
  not sender-domain authentication.
  `milter_default_action=accept` permits mail when the filter errors/is unavailable;
  it does not nullify an explicit rejection from a working filter. Existing
  DMARC `p=none` requests no rejection solely for DMARC failure; actual checking
  and local enforcement remain unproved.
- The user confirmed effective `smtpd_reject_unlisted_recipient=yes`. The virtual
  MySQL mailbox/alias maps therefore participate in automatic validation, even
  without an explicit restriction; actual map matches/catchalls remain unknown.
  Empty `relay_recipient_maps` does not disable virtual-mailbox validation, but
  provides no recipient list for a Mailman domain handled as a relay domain.
  The misspelled
  `local_recipients_maps` is unused; it does not establish the effective correctly
  spelled `local_recipient_maps`. The unused Mailman limit warning alone explains
  neither delivery nor sender authentication.

The supplied headers explicitly describe delivery through Request Tracker.
`mail.havefun.cz` reports DKIM pass for `d=vpsfree.cz`, selector `mail`; SPF pass
for envelope sender `www-data@rt.vpsfree.cz` from37.205.15.53; and DMARC pass for
visible From domain `vpsfree.cz` with policy none. These authenticate the later
RT/outbound hop as observed by that receiver. They do not establish the original
mx2 client IP/envelope, its authentication result, or why the primary accepted it.
The marked messages originally sent through mx2 had no DKIM signature; these
headers cannot retroactively authenticate that earlier submission.

If the user wants to resolve the remaining source/trust question, the smallest
additional evidence is the original primary Postfix `client=` log line for queue
ID `55F35A7ED` or `C5F44F212`, retaining client IP and any SASL indication. That
identifies the peer seen by the primary for comparison with its trust rules;
the outbound RT headers cannot supply it. No keys, SQL credentials, full logs,
whole configuration or map contents are needed. This explanatory uncertainty
creates no new staging gate or implementation package and authorizes no probe,
message, source change or cutover.

# Historical recovery checkpoint: unused Postgrey database reset authorized

2026-11-04: system/profile now run actually deployed
`0844881779d62d9a6a86d2bacd61d21565b33932`, closure
`/nix/store/4pc5mic0rp9h5qb2lhgmdh2x8z50pqd2-nixos-system-mx2-26.05.20261026.718f670`.
Activation needed bounded D-Bus recovery. The user's subsequent clean reboot
confirmed current/profile/BOOTED all equal this closure/source, fast strict SSH,
and active broker/logind/resolver/Postfix/firewall. Actual DNS now contains only
1.1.1.1 and resolves the canonical primary to 37.205.15.53 and
2a03:3b40:fe:1c3::1. Postgrey DB environment opening is the sole remaining readiness
failure. No mail was accepted; the queue is empty. Lead holds claim
`13ba611e-2f87-4036-b958-b0e056e13da7`.

**The earlier DNS-only source proposal is superseded and must not be applied.**
The clean boot proves the existing nameservers setting achieves the required
outcome. Owner0 removes only its own uncommitted draft line below; no DNS source
fix, additional review or build is needed:

```nix
networking.resolvconf.extraConfig = "name_servers='1.1.1.1'\n";
```

The proposal used a supported openresolv override, but residual live-switch state
made it appear necessary. Do not preserve that draft as a speculative workaround
or blacklist interfaces. Existing DNS evidence after clean boot is sufficient.

Owner0 proved a library downgrade: the old Postgrey1.37/Perl5.40 binding uses
Berkeley DB5.3.28, while deployed Postgrey1.37/Perl5.42 uses DB4.8.30. A separate
clone fails under4.8 with unsupported log version19/DB_RUNRECOVERY; matching5.3
opens the environment and both Btree files. The live files and verified complete
root-only backup remained unchanged. See
[candidate-deployment-preparation.md](candidate-deployment-preparation.md) and
`postgrey-backup-clone.json` for the proof and backup location.

The user then explicitly directed: "let's not waste time with this... mx2 was
never used, so the db can be reset". This supersedes the matching5.3 package
proposal. Implementer0 owns the bounded reset: keep Postgrey stopped, retain the
verified complete protected backup, move the old environment into that protected
backup base, and let the native deployed Postgrey service create a fresh database
at its existing path. **Never reset or move the Postfix queue/spool.** Source084488
and its package remain unchanged; no source edit, review or rebuild is needed.
This intentionally discards unused greylisting history, not a format conversion
or database-equivalence claim. Preserve the old environment and backup for recovery;
do not assume a software rollback also restores or validates database state.
Owner0 verifies service/socket health and the existing runtime prerequisites before
the bounded normal SMTP test. The unchanged live-mail limits still apply. No
duplicate reset, probe or package investigation belongs to architect0.

Recovery lesson: for a system transition that replaces the live D-Bus service,
prepare a boot generation and planned candidate reboot when authorized, retaining
console/SSH recovery, instead of relying on a live switch across the bus change.
Verify BOOTED/current/profile, service health and generated resolver state after
boot before concluding a source correction is necessary. The user's clean reboot
already supplied that recovery here; no further operator instruction is pending.

If clone findings justify a later source correction, keep it bounded and preserve
the existing explicit ref to deployed084488
and its complete source/input/closure receipt before folding/rebasing history.
Record old/new ranges and do not call a nonancestor deployed head merged. Commit
any necessary final correction, run affected-lane independent review once it is
complete, then build the new candidate. Reuse VM evidence only with exact unchanged
test derivation/input proof; no new full campaign by default. Before the next
committed activation batch, lead verifies the same held repository-machine binding
with verify-machine. Preserve queue/disk and both predeployment98n9 and deployed4pc5
recovery identities; no blind repeated activation or clearing retained effects.
The original live-mail limit and all production/default/lifecycle exclusions remain.

# Previous package: initial corrected private mx2 candidate

Ready for implementer0; 2026-11-03. This block supersedes earlier staging
instructions below. User authorized agent deployment: "done. well, with this
access, you can deploy mx2 yourself." Scope is VPS 27627 / 172.19.9.22 only.
Old CentOS, public DNS/IP transfer, primary configuration and master integration
remain excluded. The objective is activation of the newly prepared branch system;
the current original-branch guest and preflight are not that deployment.

## Accepted live facts and minimal source boundary

Owner0 strict preflight succeeded. Candidate is LXC NixOS 25.05, hostname mx2,
stateVersion 25.05 from installed configuration, persistent ZFS tank/ct/27627
root/var/nix, private venet0 172.19.9.22/32, IPv4 default via 255.255.255.254,
link-local IPv6 only, no global IPv6 and neither old public address. Postfix and
Postgrey are active, rspamd absent, queue count zero. Existing current/profile/
booted system is `/nix/store/98n9xjgm42pjmzi9vy430qilp2hqbzvb-nixos-system-mx2-25.05.git.7c43f080a`.
Exact host-key trust and pinned-key root access work. One allowed followup
confirmed SSH client source 172.16.106.40. Guest lacks dig, so DNS answers remain
unobserved; do not run more discovery or install tooling before this package.
See [candidate-preflight.md](candidate-preflight.md) and owner probe receipts.

Implementer0 owns exactly two application source files:

1. `cluster/cz.vpsfree/containers/mx2/module.nix`: keep ID 27627, target
   172.19.9.22, host name/domain and channels. Replace public address metadata
   with 172.19.9.22/32 and an empty global IPv6 list. Remove auto-update, set
   monitoring.enable=false and logging.enable=false; remove dormant node-exporter
   service metadata. Do not guess physical placement or edit its data record.
   Address metadata does not allocate guest IPs: actual networking remains
   host-supplied /ifcfg.add. These edits prevent misleading consumers, not a
   claimed fix to an observed public-IP collision.
2. `cluster/cz.vpsfree/containers/mx2/config.nix`: keep imports, installed-compatible
   stateVersion25.05 and hostname behavior; keep all existing authorized admin
   keys, and explicitly reference the already approved workspace deployment public
   key through its existing confData entry. The generated candidate authorized_keys
   check proved that declaring the key in confData does not include it through
   shared administrator settings. Keep this reference candidate-local; no global
   key change or new credential. Require the exact approved key in generated root
   authorized_keys before deployment.
   Apply a candidate-only resolver override to `[ "1.1.1.1" ]`. This bounded
   staging choice is justified by the independently observed internal split-DNS
   NXDOMAIN for the canonical primary and the identical inherited resolver order;
   it does not claim a successful query from this guest. Do not change shared DNS
   sources/servers or hardcode the primary IP. Actual DNS resolution is a required
   postactivation check before mail, and failure stops the mail phase.

   Restrict SMTP to observed workspace source 172.16.106.40/32. Keep the firewall
   enabled; override this host's public allowedTCPPorts to `[ 22 ]` using mkForce
   and add a standard iptables extraCommands source-specific TCP25 ACCEPT rule
   through nixos-fw-accept. Preserve SSH, do not add the source to Postfix mynetworks,
   and do not open IPv6 SMTP or exporter ports. Confirm generated firewall ordering
   and source selection in quick checks. This is a staging host restriction;
   `configs/mx2.nix`, transport/relay/filter/queue policy and tests stay unchanged.

Do not expand to workspace/catalog source, deployment scripts, new modules,
frameworks or docs bundles. Key preservation must be established from generated
authorized_keys, not inferred from a confData declaration or shared administrator
membership. Shared base/ct profiles,
input locks, existing DNS correction and data placement remain untouched.

## Checks, release and deployment contract

Run formatting, normal hooks, full-range whitespace, production evaluation,
selected effective mail-policy equality against reviewed1e3afc47, private metadata,
SSH key presence, resolver and firewall assertions. Save exact new head/input graph
and changed consumer derivations. Commit and obtain required independent review
before longer checks. Build exactly the candidate and only shared consumers whose
actual evaluated derivations changed; monitoring metadata can affect consumers,
so prove scope rather than automatically rebuilding all previous five systems.
Reuse successful VM evidence only with identical test derivation and complete
input graph; host-only staging ACL/DNS are separately covered by live checks.
Lead uses the required fresh watcher or documented fallback for long work.
Preserve reviewed1e3afc47 and original/import/runtime refs and exact range evidence.

Lead owns the already authorized activation and verification, using the prepared
exact source/closure and rollback receipt. Update 2026-11-04: the installed package
supports schema-2 configured-machine claims; the former static-catalog blocker is
superseded. Select registered repository `vpsfree-cz-configuration`, exact
Machine.name `cz.vpsfree/containers/mx2`, adapter `confctl`, with repositories=[]
and that single typed machine entry. No catalog edit, physical-node alias or
additional workspace project is needed. See [deployment-admission.md](deployment-admission.md).

The resolver reads the registered feature branch's exact committed metadata and
prepared local locked inputs. Lead acquires near activation, confirms the claim
is held, then runs verify-machine for this repository/selector once for the intended
committed batch. The target remains candidate27627/private172.19.9.22; logical
claim identity is repository origin plus configured Machine.name, not the SSH IP.
Artifact/target/key/queue/recovery checks still apply. No extra approval is needed
for the already authorized candidate deployment. Integration remains separately
unapproved; machine retention and verified deployed-lineage requirements remain.

After admission, use ordinary confctl at the exact new built generation for
`cz.vpsfree/containers/mx2`, pinned existing SSH key and strict known-host trust.
Prepare copies before ownership when supported; acquire/verify exact ownership
near activation. Run dry activation first, inspect its effects, then switch only
this target; never run deploy-infra/wildcards or deploy DNS/monitor consumers.
Record new source/input graph, native build generation, exact system derivation/
closure and current/profile paths; compare installed configuration-info to the
new head. The old98n9 closure is the rollback target, never the claimed new result.
Before switch retain its generation and verify rollback activation path; preserve
on-disk state and workspace SSH access. Stop and reconcile uncertain effects rather
than replaying commands or releasing ownership.

## Bounded live acceptance and recovery

After activation verify strict SSH, source/system/profile identity, systemd units,
private-only addresses/routes, 25.05 stateVersion, persistent paths, enabled
firewall (TCP25 only from172.16.106.40), no exporter/central-log side effects and
canonical-primary DNS through the actual selected resolver. Record actual outbound
source/NAT where available; no globalIPv6 or public Internet acceptance is claimed.
Source-restricted staging may retain missing inboundTLS/milter/recipient-policy
cutover gates. Public DNSBL effects are observed, not bypassed to force a pass.

User supplied important support mailbox `podpora@vpsfree.cz`. Send at most TWO
small, clearly marked synthetic messages there from the same return address:
one normal delivery and one candidate-only outage/queue/recovery message. No
attachments/sensitive content, deliberate invalid recipient or live DSN campaign.
User receipt confirmation suffices; no mailbox credentials needed. Unrelated-domain
RCPT rejection uses no DATA. If unexpected DSN occurs, it returns to the agreed
support address; stop and diagnose rather than repeatedly sending.

Before queue test require zero/unambiguously owned queue and record the temporary
fault/removal. Block only candidate SMTP egress to the primary (all resolved
addresses/usable families), leave SSH/DNS and real primary unaffected, and retain
the block across candidate reboot. Require final DATA250 before proving queued
marker/envelope survives Postfix restart and same-disk container reboot. Restore
candidate egress, flush normally, obtain receipt and prove queue drain. Do not
modify host networking or restart a physical node. Every wait is bounded; abort
on unexpected real mail, uncertain fault-rule effect or lost management access.

On failure close staging ingress, reconcile commands and retain queues/disk.
Restore old98n9 generation only after checking state compatibility; do not copy
CentOS state or delete accepted messages. Remove only owned fault rules. Keep
CentOS/public routing unchanged. Full cutover still needs inbound certificate,
recipient/backscatter/milter choices, final public v4/v6/firewall/PTR/source-path
checks and a separately ordered IP move. Do not mark task complete after build or
preflight: report actual activation plus live acceptance, or its exact remaining
deployment prerequisite.

---

# Earlier planning checkpoint (superseded by active package above)

The isolated verification phase below has completed; exact results are in
[verification-results.md](verification-results.md). The user's next step is a
separate staging deployment using its existing private IP, with old mx2/public
DNS unchanged. No new public allocation is required for initial tests if the
workspace can reach the candidate and it can resolve/reach the real primary on
TCP25. The user confirms candidate ID `27627` and management `172.19.9.22`,
matching existing source. Implementer0's [strict preflight](candidate-preflight.md)
verified the supplied ED25519 fingerprint and installed exact-host trust, then
root authentication failed. No remote command executed. The immediate prerequisite
is restoring the intended root access using the single existing public key being
identified locally by implementer0; no fingerprint re-request, duplicate probe,
key generation or alternate-credential exploration is needed.
Installed-state/network/access facts remain unknown; no source package is released
until root access is restored and the owner completes preflight. Follow
[staging-plan.md](staging-plan.md): preserve
confirmed identity and actual stateVersion, prepare/review necessary staging
metadata and restrictions before activation, then verify the actual
container and primary path. Current production-address metadata is not a ready
staging target. Test the reachable families and record outbound/NAT identity;
external public IPv4/IPv6, PTR and final-source acceptance remain later gates.
The user owns deployment; this planning update performs none.

# Executable isolated mx2 verification

Status: bounded implementation package ready, 2026-11-02. This phase supersedes
the proposal-only scope below. The user now authorizes autonomous isolated tests
and necessary candidate fixes, plus narrow internal DNS source reconciliation
against public mail records. No live DNS deployment, production deployment/cutover,
primary-server changes or default-branch integration is included. Architect0 owns
this brief. Implementer1 owns the DNS source package and repository writes first;
after direct handoff, implementer0 owns the overlapping mail configuration/test
edits and repository writes. Lead coordinates that sequence and final review.

## Starting evidence and boundaries

Retain reviewed import head `e4c1ac0c5ae7426fb019b79ba936b30ce63e6e6c` and original
source head/ref recorded below before consolidating history. Imported configuration
build passed, but generated evidence proves empty relay_domains and no TCP25
firewall exception. These are candidate defects to correct in this package.
Current pinned nixpkgsStable provides `pkgs.testers.runNixOSTest`, Postfix 3.11.7
and Postgrey. Local `/dev/kvm` is readable/writable. No input update is needed.

Read [primary-baseline.md](primary-baseline.md) for independent discovery:
public DNS still points all three domains to prasiatko-mail/mx2, while the internal
resolver omits prasiatko-mail and has a different mx1 IPv6. Existing transport is
not proven stale. Primary probe found Debian Postfix, STARTTLS with a self-signed
certificate, and SIZE 104857600. Recipient, trust, filtering and queue policies
remain unknown. The fixture models SMTP responses; it is not a Debian reproduction.
Do not change upstream destination to mx1 on the strength of the internal alias.

## Separately approved internal DNS source package

The user explicitly authorized: "you can fixup the internal zone if the mail
records do not correspond to the public DNS -- the public DNS is correct, the
internal is probably stale". Implementer1 owns narrow changes to
`configs/internal-dns/zone.vpsfree.cz.`: reconcile relevant mail MX and host
address records against the observed public view, increment the zone serial,
validate with the repository's zone parser/tooling, and commit before handing
repository write ownership directly to implementer0. Preserve unrelated internal
records and public zones; no general DNS cleanup or live reload is included.

Acceptance: changed MX targets/preferences and supporting A/AAAA mail records
match the public evidence, aliases remain internally consistent, serial advances,
zone validation passes, and the final diff contains only the authorized records
and serial. Record the evidence used and any intentionally retained difference.
Do not invent a vpsfree.org internal zone if none is owned here. The core isolated
test interface remains unchanged and continues using only fixture DNS answers.
Correcting source does not prove the real resolver has loaded it: after a future
authorized DNS deployment, query the candidate's actual configured resolvers and
verify primary/backup resolution and IPv4/IPv6 reachability before cutover.

## One implementation package: shared policy plus ordinary NixOS test

Own these files only unless a concrete implementation need is reported to lead:

- New `configs/mx2.nix`: move the existing Postfix/Postgrey policy here, including
  its socket linkage/transport map, and own SMTP firewall allowance here. Import
  this exact module from both production host and test node. No role framework,
  new public module API, shared container profile change or dependency campaign.
- Existing `cluster/cz.vpsfree/containers/mx2/config.nix`: import shared mail module;
  retain base/container imports, root authorization and stateVersion 25.05.
- `tests/mx2.nix`, with a small adjacent Python driver/helper only if clearer:
  conventional NixOS Python test driver, standard Postfix/DNS tools and smtplib
  or swaks. Add `checks.x86_64-linux.mx2` in existing flake checks using devPkgs.
- A short reusable explanation in `docs/operations/mx2.md`, linked from README,
  describing check invocation, tested behavior, fixture exceptions and deployment
  limits. Per-run output, source receipts and deployment evidence stay in session.

Correct relay authorization with explicit `settings.main.relay_domains` for
`vpsfree.cz`, `lists.vpsfree.cz`, `vpsfree.org`; migrate touched legacy Postfix
`config` to current `settings.main`. Keep untrusted relay decisions independent
of greylisting: conventional `smtpd_relay_restrictions` with trusted/SASL permits
then `reject_unauth_destination`. Do not broaden trusted networks or enable SASL.
Set TCP25 allowance in the shared production module, leaving firewall enabled.
Postfix default `parent_domain_matches_subdomains` includes relay_domains:
exclude that item while preserving the other defaults, so arbitrary subdomains
are not authorized by adding the three relay domains. Test this explicitly.

Keep historical transport destination and milter fail-open setting pending real
policy evidence. Do not invent a recipient directory or enforce online primary
verification, which would defeat outage queueing. Unknown recipients may be
accepted then bounced by the primary; this backscatter risk remains explicit.
Align candidate advertised message limit to the observed primary 104857600 bytes,
with a comment explaining the equality and tests of EHLO/SIZE preflight rejection;
no 100MB payload is needed. This is a bounded mail-compatibility correction.
Production inbound TLS stays an explicit unresolved certificate-provisioning
requirement; do not put fixture keys in the production config or add ACME guesses.
Retain outbound opportunistic TLS (`may`), compatible with observed self-signed
primary. No policy requires verified/publicly trusted primary TLS in this phase.

## Fixture topology and fidelity invariants

Three VMs: `sender` (untrusted SMTP client and DSN sink), `mx` (shared candidate
mail module), `primary` (Postfix receiver, controlled recipient response map,
local authoritative DNS). Separate test-only addresses on a private test VLAN;
configure IPv4 and IPv6. Do not bind production addresses on host interfaces.
Set `virtualisation.restrictNetwork = true` for every VM, no host port forwards,
no external gateway and DNS with recursion/upstream forwarding disabled. Resolve
all production-spelled test domains/upstream names only to fixture addresses.
Tests must fail if required names lack fixture answers, never query public DNSBLs
or contact real primary/mx2. Assert effective resolver and route configuration.

The MX fixture must NOT override relay domains, transport map, trust/relay or
recipient restrictions, TCP25 rules, queue location, persistent directories or
Postfix/Postgrey enablement. It imports the production module unchanged. Allowed
fixture differences: hostname/interface/resolver plumbing, shorter Postgrey delay,
optional shorter retry/policy timeouts, and test certificates only for a separately
identified TLS-capability case. Enumerate each actual override in the test. Keep
Postgrey whitelist semantics unchanged and use fresh client/sender/recipient tuples
for first-seen assertions so auto-whitelisting cannot hide a broken greylist test.

Use controlled DNS answers for the *original* Spamhaus/Barracuda queries: negative
answers normally and a positive fixture answer for a dedicated rejection case.
Do not delete their restrictions to make tests pass. Keep missing milter endpoint
and prove original `milter_default_action=accept` behavior; do not imply scanning
happened. A later milter implementation is separate scope unless real evidence
establishes the required current service.

Prove fidelity in review and quick evaluation: compare the real confctl MX's
selected effective Postfix settings, transport map, TCP25 allowance, queue/data
paths and Postgrey persistence/socket to the test node, accounting only for listed
fixture differences. Runtime assertions also check effective `postconf` and
firewall state. The full production confctl build remains required; this VM test
does not exercise the vpsAdminOS container profile, host networking or placement.

## Runtime acceptance matrix

Use unique Message-ID/body markers and controlled envelopes, not log-only success.
Bound every wait. Sender connects from its own address, outside candidate's
mynetworks, over IPv4 and IPv6; never send only via loopback.

1. Confirm listener reachable through enabled firewall and exact three relay
   domains accepted after greylisting. Verify primary receives envelope recipient,
   envelope sender and full marker/content for each domain, on declared transport.
   Deny unrelated domain and arbitrary subdomain at RCPT (5xx) and prove no queue
   acceptance. Verify invalid recipient syntax/unknown DNS domain rejection.
   EHLO limit equals primary limit; oversized declared SIZE is rejected early.
2. Fresh tuple gets temporary Postgrey response; retry after short fixture delay
   succeeds. Persist whitelist state across service and VM restart. Stop Postgrey
   and assert bounded temporary failure rather than accepting or losing mail.
   Deterministic DNSBL positive rejects; missing milter still follows fail-open
   acceptance. Record these as observed behavior, not an anti-spam certification.
3. Stop only primary SMTP (keep DNS running). Submit and require final DATA 250;
   capture queue ID and queued envelope/content. Restart Postfix, then reboot MX
   using the same VM disk, and prove message still queued. Restore primary, flush
   with normal Postfix tool, observe content/envelope delivery and empty queue.
4. Primary returns explicit temporary 4xx for a controlled recipient: accepted
   mail remains deferred, survives restart if combined with step 3, then delivers
   when response is changed. Permanent 5xx causes the expected DSN to controlled
   sender/sink and removal of original queue item; verify failure status and
   original recipient/marker, rather than confusing bounce with successful mail.
   SMTP can duplicate after ambiguous acknowledgment; do not assert global
   exactly-once semantics or delete queues to obtain an empty-queue result.
5. Primary offers self-signed STARTTLS: prove candidate negotiates encryption
   under unchanged outbound `may`; with primary STARTTLS disabled, prove plaintext
   fallback still delivers. Record protocol evidence from both ends. Assert
   production inbound STARTTLS is currently absent. An optional isolated case
   may install an ephemeral test cert and test STARTTLS capability, clearly
   separated from production certificate readiness; core tests must not depend
   on that override. No need to implement issuance infrastructure.

## Checks, sequence, limits and recovery

Quick checks before final review: normal formatting/hooks, Nix parsing,
`git diff --check`, test derivation evaluation without realization, Python syntax,
MX production evaluation, fixture-difference inventory and complete range-diff.
Ensure final full series includes original import lineage, corrected host policy
and coherent tests/docs; preserve reviewed-import/source refs before rewriting
unmerged followup history. No database/schema migration exists; Postgrey and
Postfix persisted paths must remain unchanged. Reconcile new live facts through
lead before altering settled external interfaces or source scope.

Commit intended changes and obtain independent final review BEFORE long runtime
checks. Lead launches a fresh policy watcher for exact-head `nix build -L
.#checks.x86_64-linux.mx2` and targeted `nix develop -c confctl build --yes
cz.vpsfree/containers/mx2`. Retain lock/input/derivation/output identities and
logs under session; do not claim reuse from mere source equality. No CI expansion.

Plan one runtime batch, target under 15 minutes once closures exist, 30-minute
runtime ceiling; allow a separately reported substitution/build preparation window.
Use at most 3 VMs, about 1GiB RAM/1 vCPU each initially; increase only for observed
needs. Per-step waits normally 30-90s, queue drain up to 120s. Stop on external
network escape, unexpected kernel compilation, repeated boot failure or first
assertion failure; preserve relevant logs/state, return diagnosis to implementer,
then rerun only justified checks after fixes/review. No blind retry loop.
Use native test-driver shutdown for owned VMs; retain compact receipts, then
remove only owned disposable test artifacts per policy. No production machine
claim or session lifecycle action is needed for this isolated test.

Success means the corrected candidate passes isolated relay/queue/policy checks
and full build, and the internal mail-zone source passes the reconciliation checks
above. Limits remain for real recipient policy, production TLS, deployment of the
corrected internal zone and actual resolver behavior, container hosting and eventual
cutover. It does not mean the CentOS replacement has been deployed or is already
production-accepted.

---

# Original import brief (retained historical scope and provenance)

# mx2 branch import and verification brief

Status: execution package ready; runtime verification below is a proposal, not
performed evidence. Architect: architect0. Scope is branch recovery/rebase and
verification advice. No production access, mail sending, deployment, integration,
or new test subsystem is authorized by this brief.

## Settled source evidence

Read-only source: `/home/aither/workspace/vpsfree.cz/vpsfree-cz-configuration`.
Source checkout stays on master; preserve every original ref and untracked file.

| Ref or boundary | Exact commit |
| --- | --- |
| Local `2025-05-30-mx2` | `40411d67ee97cea800bcccd89b0473432b4502c4` |
| Cached `origin/2025-05-30-mx2` | `be8435d1d4f3e656af1d7d090d867797d2713a66` |
| Common ancestor with source master | `0bcc165f13059782bf686da39a3a9b5698b10275` |
| Source master and cached origin/master at inspection | `e6685e6076bf2262e3faf5308d11845d0d746c69` |

Exactly two source-only commits exist above that ancestor:

1. `be8435d1d4f3e656af1d7d090d867797d2713a66`, 2025-05-30,
   `cluster: add mx2.vpsfree.cz`: five paths, 68 added lines.
2. `40411d67ee97cea800bcccd89b0473432b4502c4`, 2025-06-06,
   `environments/deploy: use cache.vpsadminos.org`: two added lines.
   `git cherry master 2025-05-30-mx2` marks this patch already upstream;
   master commit `17ac0d2b842a88ae7f7b76b1651f36d984dadb2c` has the same
   subject and additions. Do not duplicate or revert current cache policy.

No branch-specific input changes or unmerged cross-repository dependency were
found. The historical branch consumes published nixos-stable nixpkgs
`7c43f080a7f28b2774f3b3f43234ca11661bf334` (25.05) and os-staging vpsAdminOS
`27b7693f13544b2aeb6bcb9b413221d62c97ceb7`. These are historical context,
not requested pins. Current master owns modern flake inputs and the container
profile. No database/schema migration exists in the source feature.

## Implementation package and boundaries

One implementer owns the dependent configuration package. No second repository
or parallel application package is needed. Lead owns plan/state and registration
coordination; architect owns this design. Implementation can start immediately.

1. Import the exact local source feature history into the workspace canonical
   bare repository without updating the source checkout, its refs or index.
   Preserve an explicit original head/reference and record the imported range.
2. Fetch canonical SSH upstream in the workspace and determine its actual default
   branch/current head. Rebase the session feature branch onto that fetched head.
   Use the session worktree and dated branch. Do not change any default branch.
3. Resolve only import/rebase and current-module compatibility issues. Rename
   mx2 metadata `swpins.channels` to the current `inputs.channels`, using existing
   `nixos-stable` and `os-staging` channels. Retain current shared profiles,
   generated container metadata shape, and flake inputs. Format changed Nix files.
   The cache commit should drop as an already-applied patch after fresh evidence.
4. Preserve the existing mx2 behavior and identifiers; do not silently fix mail
   policy, change addresses/target/container ID, refresh old admin keys, remove
   `auto-update`, change stateVersion, or add a test harness. Escalate material
   functional decisions through lead. Record production shortcomings as residuals.
5. Publish only the session feature branch under ordinary workspace policy after
   quick checks and review coordination. Preserve source feature refs. Record
   the exact new base/head, old/new range-diff and every resolved conflict.

Files owned by this package:

- `cluster/cluster.nix`: add mx2 module import, preserving current neighboring hosts.
- `cluster/cz.vpsfree/containers/mx2/{config,module}.nix`: imported host and service
  configuration; current option spelling/formatting only.
- `data/ssh-keys.nix`: preserve the branch's public `toms` key definition if absent.
- `data/vpsadmin/containers.nix`: add mx2 placement metadata without regenerating
  unrelated production state.
- `environments/deploy.nix`: expected no final delta because the cache patch is
  already upstream. Preserve newer upstream fallback/settings.

Current master should supply `flake.nix`, `flake.lock`, `profiles/ct.nix` and
shared modules without feature changes. If evaluation exposes a new dependency,
report the concrete option/input failure before widening scope.

## Interfaces, invariants and known limits

The source config describes a NixOS container, ID 27627, placed on
`node5.brq.vpsfree.cz` (node 214), host name `mx2.vpsfree.cz`, SSH target
`172.19.9.22`, public IPv4 `37.205.11.114/32`, IPv6
`2a03:3b40:100::1:95/128`. It retains `stateVersion = "25.05"` and tags
`mx`, `auto-update`. These are historical declarations, not verified current
infrastructure facts. Never deploy to the inherited target as a test.

Postfix transports `vpsfree.cz`, `lists.vpsfree.cz`, and `vpsfree.org` to
`smtp:prasiatko-mail.vpsfree.cz`. Recipient restrictions include trusted-network
and SASL permits, syntax/domain/destination/unlisted checks, Postgrey policy,
and Spamhaus/Barracuda DNSBL lookups. The milter points at `localhost:11332`
with failure action `accept`; no milter service is enabled by the host file.
Postgrey is enabled. Source includes no explicit relay domain/recipient table,
TLS certificate, SMTP listener/firewall policy, or SASL server setup. A transport
map alone does not authorize relay. Effective defaults must be examined after
rebase before deciding what works; compilation alone is not mail acceptance.

Repository public DNS declares vpsfree.cz and lists MX preference 10 for
prasiatko-mail and 15 for mx2. It matches the branch's public IPv4/IPv6. Internal
DNS has a different mx2 IPv6 (`2a00:cb40:2::1:95`), an operational discrepancy to
resolve before cutover. The repository is not proof of live DNS or .org policy.

No source evidence establishes a successful historical mx2 deployment, production
queue contents, active TLS policy, recipient map, or current placement. One mx2
commit is present in Git history; branch publication and the extra cache commit
are not deployment receipts. Keep provenance honestly unknown; preserve original
refs and do not classify this as a verified undeployed production migration.

## Compatibility and recovery contract

This import changes a host configuration, not APIs, clients, Terraform, message
formats or database schemas. SMTP is the boundary to the unchanged primary MX.
No fleet-wide vpsAdminOS update is implied. The new container consumes current
master's NixOS/vpsAdminOS inputs, so a successful historical 25.05 build would not
prove current compatibility. Keep 25.05 stateVersion unless a separately reviewed
state migration requires otherwise.

Postfix queues, Postgrey state, TLS keys and local aliases are persisted state.
Do not assume CentOS 6 spool/database files can be copied to modern NixOS or back.
Prefer independent hosts and SMTP queue draining; retain the old host's own disk
and configuration. A NixOS generation rollback cannot restore the CentOS system.
After traffic reaches NixOS, queued accepted messages remain its responsibility
when ingress is reverted. Do not delete either queue or claim exactly-once SMTP
semantics. No recovery operation is executed by this task.

## Acceptance and checks for this import

Quick checks, using repository tools/environment:

- Source remains unchanged and imported original range matches exact source SHAs.
- Rebased branch descends from freshly fetched default; final diff contains only
  the bounded host additions and necessary option/format compatibility.
- `git diff --check`, declared formatting/hooks, and targeted Nix syntax/evaluation
  checks pass. Confirm mx2 appears once in inventory and uses current channels.
- Inspect effective Postfix configuration where evaluation permits; record gaps
  without silently changing policy. Capture final source/input identities.
- Review complete old/new commit series and range-diff; explicitly account for
  the dropped cache patch, compatibility edits and no database migrations.

Independent final review follows committed substantive changes and quick checks.
The repository-required targeted `confctl build cz.vpsfree/containers/mx2` is a
longer check coordinated by lead and a fresh verification watcher after review;
architect does not launch it. A successful build is build evidence only. Never
use `confctl deploy ... dry-activate` in this request: it contacts/acts on a target.

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

## Proposed staged mail verification before replacement

Use existing tools (`swaks`, `openssl s_client`, Postfix queue/config commands)
and a disposable isolated network with candidate, controlled SMTP sender,
controlled primary/sink, and local DNS. Keep production IPs, DNS, secrets and
outbound SMTP inaccessible. Exercise the imported config plus explicitly recorded
fixture overrides. No new permanent testing subsystem is needed for this proposal.

1. **Static/build gate:** inspect generated `postconf -n` and master services,
   relay domains/recipient maps, trusted networks, transport resolution, TLS
   configuration, policy socket permissions and service ordering. Verify intended
   IPv4/IPv6 listeners/firewall. Decide whether the absent milter is intentional
   fail-open behavior or incomplete configuration. Establish desired domain and
   recipient acceptance before expecting runtime success.
2. **Normal delivery and relay denial:** untrusted sender delivers a unique test
   message for each intended domain to the controlled primary. Confirm envelope,
   headers/body and transport destination; no loop. Reject an unrelated-domain
   RCPT before queueing. Test non-FQDN/unknown domains and unauthorized clients
   from both address families. Test trusted/SASL bypasses only where deliberately
   supported. Define invalid-recipient behavior and prevent avoidable backscatter;
   `reject_unlisted_recipient` alone is not a populated recipient directory.
3. **Queue and restart:** make the primary unavailable or return temporary SMTP
   errors; once the candidate accepts DATA, prove the message remains in queue
   across Postfix restart and container restart. Restore the primary and verify
   queued content is delivered and the queue drains. Exercise permanent upstream
   rejection and queue expiry with controlled sender/sink and shortened fixture
   limits. Record queue IDs and distinguish normal SMTP retransmission duplicates
   from loss. Test resource exhaustion only in a bounded disposable fixture.
4. **Policy and TLS:** new Postgrey tuple temporarily rejects, retry after its
   delay succeeds, and policy state survives restart. Stop Postgrey and verify
   understood temporary-failure behavior. Simulate DNSBL positive, negative and
   DNS failure locally; do not depend on public DNSBL queries for deterministic
   tests. Test unavailable milter behavior against the declared `accept` policy.
   Verify STARTTLS, certificate name/chain/expiry and agreed inbound/outbound
   TLS fallback. Public MX encryption policy must be explicit, not accidentally
   changed to mandatory TLS. Exercise DNS failure and IPv6 transport behavior.
5. **Controlled preproduction:** after separate authorization, boot the exact
   candidate closure on a distinct address in the real container environment.
   Restrict senders and domains/recipients to agreed test fixtures, including a
   primary-side test mailbox/sink if authorized. Verify resolver views, routing,
   PTR/HELO, certificate delivery, monitoring and alerts for service/queue/disk
   trouble. Temporarily deny only the candidate's path to the primary to verify
   store-and-forward; do not interrupt production mail delivery for a test.
6. **Cutover and rollback rehearsal:** obtain actual CentOS configuration and
   queue inventory through an authorized operator; reconcile all domain, recipient,
   alias, anti-spam and TLS policies before cutover. Record old/new host identity,
   exact configuration head/input graph and system closure, DNS/routing steps,
   monitoring, owner and rollback triggers. Drain the old queue, prevent duplicate
   IP ownership, and change only the agreed ingress route/address/DNS. If DNS
   changes, account for TTL overlap; lower preference numbers mean preferred MX.
   Preserve old host recovery. On failure restore old ingress while retaining and
   safely draining accepted NixOS messages. Require observed delivery and queue
   health before calling the replacement successful. Deployment/integration
   approvals and machine reservation/release rules remain separate future gates.

Import delivery may proceed despite these runtime unknowns. Production readiness
cannot be claimed until the effective mail-policy gaps and staged acceptance
criteria are resolved and verified under separately authorized operations.
