# Deploy and verify the private mx2 candidate

Updated 2026-11-03. The user installed the requested access key and authorized:
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

## Concrete deployment prerequisite

Source preparation, review and build can proceed. **Agent activation is blocked
until the exact candidate has a supported configured-machine claim mapping.**
The installed coordination catalog currently lists only aitherdev, with no mx2,
VPS27627 or proven physical-node mapping. Its guide requires machine ownership
for deployment and supplies no guest-only exception or dynamic registration
command. Do not reserve aitherdev as a substitute or bypass the claim.

The lead owns resolving this prerequisite after the candidate is reviewable;
this package does not expand into runtime/catalog changes. Before activation,
obtain authoritative held ownership for the exact target. Preserve ownership
through uncertain effects and the installed verification/integrated-lineage
release conditions. Deployment approval does not authorize default integration.

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
