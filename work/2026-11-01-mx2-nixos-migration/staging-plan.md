# Nov6 execution complete

The public cutover is verified: the transferred IPv4/IPv6 addresses and routes,
restricted bootstrap, real trusted ACME/Postfix certificate, final ordinary switch,
services/queue, DNS/PTR and both primary connection paths passed. Public IPv4 SMTP,
trusted TLS and unrelated relay denial were checked by the owner. The user's
external IPv6 TLS verification and corrected-client `554 5.7.1 Relay access denied`
close the corresponding IPv6 checks. No reboot or additional message was needed.

See [current state](state.md) and [deployment evidence](public-profile-preparation.md).
The numbered Nov5 checklist below is the retained completed execution contract.
Monitoring-consumer activation and default integration remain separately scoped;
keep old VPS 2992/disk and the active machine claim until their recovery/release
conditions are satisfied. No further cutover test or cleanup is requested.

# Nov5 owner checklist: prepare privately, hand over later

Private staging is complete at084488/4pc5: both marked messages arrived, queue
persistence passed through service/VPS restart, services are healthy and the queue
is empty. Keep those results and the protected original Postgrey backup. The
large NixOS upgrade is already complete; **no further reboot or input refresh is
planned**. Public IPs are not needed for edit/review/build/copy. The user agreed to
that preparation; public handover/old-host actions still need concrete approved
execution instructions. No additional mail or default integration is authorized.

1. **Implementer0: prepare two configurations now on the private workspace.**
   Implement the released [design.md](design.md) package using the exact deployed
   inputs. Bootstrap keeps the existing SMTP source ACL while adding hostname,
   native ACME/TLS, HTTP80 and normal metadata/monitoring. Final differs only by
   opening TCP25/removing that temporary ACL. Done when both source identities
   and refs are preserved, quick checks pass and the final history is reviewable.
2. **Lead: coordinate independent review, builds and private copy.** Review both
   variants; build and copy their exact native generations through172.19.9.22,
   retaining084488 recovery and all source/input/output receipts. Done when both
   prepared generations are verified and named explicitly. Leave084488 running;
   do not start HTTP-01 attempts while public DNS still routes to CentOS. The
   recipient-export/SPF/DMARC discussion does not block this preparation.
3. **Lead + authorized VPS operator: agree and execute the later handover.**
   First inspect/drain the old CentOS VPS2992 queue through normal SMTP, retain
   its disk and a path to deliver any remaining queue. The user confirmed shell
   access to2992 remains available without its IPs.
   The single transfer action for the operator is: in vpsAdmin, remove the exact
   public37.205.11.114 and2a03:3b40:100::1:95 allocations from VPS2992, wait for
   successful removal transactions, then assign their routes **and host addresses**
   to VPS27627's existing interface; retain its separate172.19.9.22 allocation.
   Use native IP `free` then `assign_with_host_address` actions, or their normal
   WebUI equivalents. Do not choose disown/release ownership, route-only assignment,
   interface removal or network disable. Confirm the selected allocation/prefix
   contains only the intended addresses; a confctl /128 does not prove the size of
   the API allocation. Never overlap ownership. Keep public DNS unchanged when
   reusing the same IPs. Done when both transaction chains finish and v4/v6 routes,
   guest addresses and private management reach the intended guest. The
   still-running084488 firewall retains the exact SMTP source restriction during
   transfer, so general public SMTP is not exposed at this step.
4. **Lead: ordinary-switch the reviewed bootstrap generation AFTER handover.**
   No reboot. HTTP80 becomes reachable for native ACME; general SMTP remains
   restricted even while the provisional self-signed certificate exists. Verify
   actual addresses/routes/PTR, hostname, DNS, services and native HTTP-01 issuance.
   Done when the real certificate has the correct hostname/trusted chain and
   Postfix uses it, with renewal/reload configured. On issuance failure retain the
   gate and diagnose; do not switch final or relax certificate validation.
5. **Lead: ordinary-switch the exact reviewed final generation.** This removes
   only the temporary SMTP restriction. Done when public IPv4/IPv6 SMTP and
   STARTTLS, unrelated-relay denial without DATA, final-source primary forwarding
   path, queue health and normal monitoring are verified. No new message campaign
   or primary outage. Activate only the separately scoped monitoring consumers.
6. **Lead: recover if needed without discarding mail.** Close new ingress and
   reconcile both queues; reverse address ownership without overlap if necessary.
   Keep/drain anything NixOS has accepted even if CentOS resumes ingress. Never
   copy/delete spools or assume generation rollback restores database contents or
   IP ownership. Preserve the Postgrey backup and recorded system generations;
   select rollback only after checking current-state compatibility.

Lead verifies the exact held machine binding before each later committed
activation batch. Preparation does not grant public cutover, primary changes,
default integration or session lifecycle actions. The older boot/reboot proposal
is superseded by this ordinary-switch sequence; historical material below is not
an additional operator checklist.

Local-source handover evidence: vpsAdmin `IpAddress.Free` removes an allocation's
host addresses and route; `AssignWithHostAddress` adds the route and selected host
address. Their native chains use address-specific `osctl ct netif route`/`ip`
operations, not VPS stop/reboot or whole-interface replacement. This supports a
live transfer preserving an unrelated private allocation; it is not proof of
the deployed old backend or current network eligibility. Source references are
`api/lib/vpsadmin/api/resources/ip_address.rb`, the network-interface AddRoute/
DelRoute chains and `libnodectld/lib/nodectld/network_interface.rb`, read from the
configuration's existing pinned vpsAdmin input. Assignment rejects an allocation
already in use, with incompatible ownership or unavailable in the target location.

**Operator-confirmed handover:** the user stated, "old vps id is 2992. I can get
its shell without IPs, yes." Transfer is therefore from old2992 to candidate27627,
whose private management172.19.9.22 is retained. The two API allocation IDs/prefixes
and target interface ID are ordinary operator selections in the existing vpsAdmin
view at handover, not information needed now. Confirm location/ownership eligibility
before removal; no node or CLI command is invented. No vpsAdmin CLI was present
under the ordinary command names checked;
no tool was installed and no API/login/host probe occurred. This does not delay
the released build package; lead will present the one transfer step with those
concrete selections after both generations are ready.

# Historical plan: deploy and verify the private mx2 candidate

Current readiness: after the user's clean reboot, BOOTED/current/profile all run
the deployed084488/4pc5 system. Strict SSH and broker/logind/resolver/Postfix/firewall
are healthy; actual resolver is only1.1.1.1 and canonical-primary A/AAAA queries
pass. The earlier DNS-only draft is superseded and needs no source fix/build.
Only Postgrey DB environment opening remains unresolved. Clone evidence proves
the deployed DB4.8 cannot open the old DB5.3 log environment; matching5.3 can.
The user explicitly authorized resetting the unused database: "mx2 was never
used, so the db can be reset". Owner0 retains the verified complete root-only
backup, moves the old Postgrey environment into its protected backup base, then
lets the native deployed service create a fresh database. The Postfix queue/spool
must remain untouched. Source084488 stays unchanged; the package override proposal
is superseded and needs no source edit/review/build. This is an intentional reset
of unused greylisting history, not database equivalence. Verify Postgrey health
before the bounded normal SMTP test; preserve old state for recovery. Claim13ba
stays held. No further operator action is requested.

Updated 2026-11-04. The user installed the requested access key and authorized:
"done. well, with this access, you can deploy mx2 yourself." The lead now owns
agent deployment of candidate VPS **27627**, **172.19.9.22**. No further user
installation action is currently needed. Old CentOS mx2, public DNS, public-IP
transfer, primary configuration and master integration remain outside scope.

The executable two-file implementation and deployment contract is the first
section of [design.md](design.md). This plan supersedes earlier user-deploy-only,
unknown-host and new-address assumptions.

## Confirmed candidate and existing evidence

[Strict preflight](candidate-preflight.md) confirmed root access with the verified
ED25519 host key and the installed workspace credential. The candidate runs NixOS
25.05 in LXC, hostname mx2, with installed stateVersion25.05 and persistent ZFS
root/var/nix under tank/ct/27627. It has 172.19.9.22/32, an IPv4 default route,
link-local IPv6 only, and neither old mx2 public address. Postfix/Postgrey are
active, rspamd is absent, and queue count was zero. The observed workspace source
is **172.16.106.40**. Installed current/profile/booted paths all resolve to:

`/nix/store/98n9xjgm42pjmzi9vy430qilp2hqbzvb-nixos-system-mx2-25.05.git.7c43f080a`

That is the original-branch system and rollback reference, not deployment of the
new branch. Physical node placement, NAT source and actual resolver answers were
not established. The guest lacked dig; no new tooling was installed to investigate.

Independent review, isolated SMTP/queue tests and affected builds previously
passed at `1e3afc478fb72b54a25a0147910463f060fee88f`; see
[verification-results.md](verification-results.md). The staging delta needs its
own checks/review/build; unchanged VM coverage is reused only with exact test
derivation and complete input proof.

## Work we perform next

1. Implementer0 changes only the host's config.nix/module.nix: retain confirmed
   ID, target, name and stateVersion; use verified private address metadata; remove
   auto-update and production monitoring/logging effects. Keep host-provided
   networking, placement data, tested shared mail module and inputs unchanged.
   Preserve approved administrative SSH access after activation: the generated
   candidate omitted the existing workspace key, so explicitly reference its
   existing confData entry in this host and verify generated root authorized_keys.
   No global key change or new credential is needed.
2. Use a candidate-only 1.1.1.1 resolver setting for staging, based on the proven
   internal split-DNS problem. Do not deploy DNS infrastructure or alter transport.
   Verify canonical-primary resolution on the actual guest before test mail;
   configured fallback after an internal NXDOMAIN is insufficient.
3. Preserve SSH and restrict candidate TCP25 to 172.16.106.40/32 at its firewall,
   without trusting that address as a Postfix relay network. Keep IPv6 SMTP and
   exporter ports closed for this private IPv4 stage. Do not widen the network or
   attach public addresses to obtain more coverage.
4. Complete quick checks, committed independent review, exact candidate build and
   only consumer builds justified by changed derivations. Preserve prior heads,
   complete source/input graph, native generation and exact closure receipts.
5. After coordination admission below, verify exact target/key/queue and retain
   rollback state. The lead uses the reviewed built generation with ordinary
   single-target confctl dry activation followed by switch. No wildcard updater,
   DNS/monitor activation or source default merge. Verify actual installed current/
   profile/source identity against the new receipt; preflight/build alone is not
   deployment success.

## Supported deployment admission

The former static-catalog blocker is superseded by the updated installed runtime.
Lead uses a schema-2 claim for registered repository `vpsfree-cz-configuration`,
exact selector `cz.vpsfree/containers/mx2`, adapter `confctl`, with no repository
merge claim. Ordinary configured targets need no catalog entry or package change.
The request resolves committed feature metadata with prepared local locked inputs;
it does not build, fetch, probe or activate the machine.

Near activation, lead acquires and confirms held ownership, then verifies that
same repository/selector binding once for the intended committed deployment batch.
[Deployment admission](deployment-admission.md) records the changed contract.
The authorized private candidate, exact build/SSH/rollback checks and live scope
remain unchanged. Missing ownership or an actual resolver refusal would be handled
on its evidence; absence from the legacy static catalog is no longer a blocker.
Normal effect/verification/integrated-lineage retention still applies; deployment
approval grants no default integration or lifecycle action.

## Small live verification batch

After actual new-system activation, the lead checks identity, private addresses,
routes, persistence, SSH, Postfix/Postgrey/firewall health, resolver answers,
source-restricted SMTP and the absence of unintended monitoring/log forwarding.
Record outbound source/NAT where observable; private access does not prove public
Internet routing or acceptance from future production addresses.

The supplied mailbox is the important support address **podpora@vpsfree.cz**.
Use at most **two small, clearly marked synthetic messages**, with that same return
address: one normal delivery and one temporary-outage recovery message. No
attachments, sensitive content, invalid-recipient campaign or deliberate live
DSNs. Unexpected notices may return to that address; stop and diagnose instead of
repeating messages. The user confirms receipt; no mailbox credentials are needed.
Other-domain relay rejection is tested at RCPT without DATA. All three-domain
forwarding and deliberate failure/DSN behavior already passed in isolation.

For the second message, first prove the queue is empty or entirely owned test
mail. Block only candidate SMTP egress to the primary across every usable resolved
path, keeping SSH/DNS working and the rule effective across reboot. After final
DATA250, verify the queued marker survives Postfix restart and a full same-disk
candidate-container reboot. Restore only the recorded candidate egress rule,
flush normally, confirm receipt and queue drain. Never stop the real primary,
change host networking, restart a physical node or copy CentOS state.

## Acceptance and recovery

Success requires the new exact branch system actually activated, working private
IPv4 SMTP/DNS to the primary, relay denial, confirmed controlled delivery, and
queue persistence/drain through candidate-only outage/restart. Record the real
result and any missing coverage; no global IPv6 capability is claimed.

If activation or verification fails, stop submissions and isolate ingress;
reconcile effects and preserve disk/queues. Restore the recorded98n9 generation
only after checking state compatibility, preserving administrative access. Remove
only owned fault rules. Unexpected real mail stays retained for operator recovery;
never delete the queue or reprovision around uncertain effects.

Before any later public cutover, settle inbound TLS, recipient/backscatter and
intentional absent-milter policy. Verify public IPv4/IPv6 ingress, firewall, PTR/
HELO and final outbound identity, then plan the separate old-IP transfer with no
address collision and both queues retained. None of those future changes or any
session lifecycle action is authorized by this staging deployment.

[Session](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-01-mx2-nixos-migration/).
