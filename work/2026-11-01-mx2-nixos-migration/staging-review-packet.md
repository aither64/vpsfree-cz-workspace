# Private staging candidate final review packet

Prepared 2026-11-03. Exact-head generated quick assertions passed; see
staging-implementation.md and staging-generated-assertions.json. This packet
covers the new staging delta and clean rebase;
prior completed mail/DNS reviews remain applicable to unchanged content.

## Outcome and boundary

The user supplied candidate VPS27627 at 172.19.9.22, verified its ED25519 host
identity, installed the workspace public key, then explicitly authorized:
"done. well, with this access, you can deploy mx2 yourself."
The user also reminded us to deploy the new system because the guest still runs
the original branch configuration. Read-only preflight is not deployment success.

Prepare, review and build the private staging candidate; activate it only after
the required configured-machine ownership is available. No CentOS modification,
public IP transfer, public DNS change, primary configuration or default merge.
Live test scope is at most two clearly marked small messages to the supplied
important mailbox podpora@vpsfree.cz, with the same return address. No deliberate
live failure/DSN campaign. Receipt needs the user's confirmation.

## Source, history and input provenance

Repository/worktree: vpsfree-cz-configuration at
/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-01-mx2-nixos-migration/vpsfree-cz-configuration.
Published feature name: 2026-11-01-mx2-nixos-migration.

- Prior reviewed base/head: c040c14cdbacc07998700b524996a89306188d7f /
  1e3afc478fb72b54a25a0147910463f060fee88f.
- Current fresh base: c4107822060e9e34b24a83950d618c9f28a7722b.
- Current committed head: 0844881779d62d9a6a86d2bacd61d21565b33932.
- Current tree: 34dc1820c5feda2a0d875f60c964b8375de0af49.
- Complete final series: 548514a9e573ccbc3f145d49d7d307c3e23b5aa5 host/shared
  policy/staging; e7cd91d881fce72fe15339a8df736a6481d7000d DNS correction;
  0844881779d62d9a6a86d2bacd61d21565b33932 tests/docs.
- Full final diff: 13 paths, 740 additions/four deletions.

The staging change is folded into its owning host commit; no obsolete public
metadata, exporter follow-up or staging fixup remains. DNS/test patch IDs are
unchanged. Original source40411, reviewed importe4, successful runtime8d and
reviewed mail1e refs remain preserved. None is claimed literally merged/deployed
in the refreshed ancestry. The candidate's actually running original system is
recorded separately below; do not claim any new feature head was deployed.

No database/schema migration or CentOS state conversion. StateVersion25.05 and
Postfix/Postgrey paths remain unchanged. No new dependency update stream is
introduced by this feature. Upstream advanced via two vpsadminServices updates;
the clean rebase inherits them. Final feature flake.lock equals current default.
Only vpsadminServices changed from the previous root lock; selected mx2/test roles
remain unchanged. New lock blob f6b87ab2ca27a72c3fe1bdd134129ff1e4a9f7e9,
SHA256507e781c2fa52da5a389e6eab824efe68baa72b1727de0fc162ea0a5e6b4c098.
Do not call the whole root lock unchanged. Test-result reuse needs exact test
derivation and its complete dependency graph, independently of root-lock edits.

## Actual candidate and implementation boundary

See candidate-preflight.md for strict trust/authentication history and facts.
Actual guest: NixOS25.05/LXC, hostname mx2, persistent ZFS tank/ct/27627, direct
installed stateVersion25.05, venet0 172.19.9.22/32, IPv4 default route, link-local
IPv6 only, neither old public address, active Postfix/Postgrey and empty queue.
Current/profile/booted rollback reference:
/nix/store/98n9xjgm42pjmzi9vy430qilp2hqbzvb-nixos-system-mx2-25.05.git.7c43f080a.
Observed workspace SSH source is 172.16.106.40. Guest lacked dig, so no resolver
answer is claimed from the follow-up. Physical placement is not newly verified.

Only two host files change from the reviewed policy beyond inherited lock input:

- module.nix retains confirmed ID/target/name/channels; private address metadata,
  no global IPv6 metadata, no auto-update, monitoring/logging disabled and no
  node-exporter service metadata. Host-supplied networking is not rewritten.
- config.nix retains imports/stateVersion/admin access/shared mail policy;
  candidate-only nameserver1.1.1.1, enabled firewall, forced TCP22 allowance and
  standard source-specific IPv4 TCP25 acceptance for 172.16.106.40/32. Source is
  not added to Postfix mynetworks. No global SMTP or exporter opening.

Shared mail module, tests, DNS correction, container profile and placement data
are unchanged. Generated-key inspection disproved the initial shared-admin-key
assumption: the existing workspace key was declared but not selected. The final
candidate must explicitly reference that existing confData key in root access;
no new credential or shared administrator change is introduced.
Resolver override follows recorded split-DNS NXDOMAIN evidence and is a staging
choice, not a claim that the guest has already successfully resolved the primary.

## Checks, consumers and deployment limits

Implementer0 owns exact-head quick/generated-setting/consumer receipts and
publication proof; use those alongside this packet. Normal hooks, format/parse
and full-range whitespace passed before assignment. Inspect actual generated
firewall ordering, effective mail equality, approved key preservation, disabled
monitor/logging, private metadata and resolver results from the receipt.

Actual shared consumers include both mon1/mon2 and alerts1/alerts2 (alerter selects
monitored containers), plus the two DNS consumers. Determine build set from actual
native Git-self derivation changes; do not rebuild unrelated fleet or activate
these consumers. Reuse the previous VM pass only if exact derivation and full
consumed-input graph match, with existing output-unavailability qualification.

After independent review, run required builds with a fresh policy watcher or
documented parent fallback. No long check or new deployment has started.

Activation remains blocked on configured-machine admission: installed catalog
contains only aitherdev. No mx2/27627 or proven physical-node mapping, supported
dynamic registration or guest exemption is documented. Do not use aitherdev as a
surrogate or bypass ownership. Prepare the concrete candidate before resolving
this prerequisite. Deployment authorization does not approve workspace package
changes, source default integration or public cutover.

Before activation: held valid exact-target claim, known host/key, exact built
generation, empty/accounted queue, rollback path/access retained, dry activation.
After activation: actual new current/profile/configuration-info and runtime
identity, SSH/firewall/units/network/DNS/persistence checked. Live tests and
candidate-only egress/reboot recovery follow staging-plan.md. Missing inbound
TLS/recipient-backscatter/milter policy and public/final-address coverage remain
cutover gates. Preserve both old/new queues on any ingress rollback.

## Review assignment

High risk: real host deployment, firewall/SSH, accepted mail and persistent state.
Retained independent reviewer0, saved gpt-6.1-sol/xhigh/read_only; no override.
Review general, architecture/repetition, scope/proportionality and risk/compatibility
for affected staging/base/history lanes. Reuse prior mail/DNS review for unchanged
content. Require explicit whole-branch history/migration/update-stream conclusions.

Read mandatory-change-review skill and all four lane references; project AGENTS,
current plan/state/design, staging-plan.md, candidate-preflight.md, prior
verification-review.md and monitor-review.md, and owner staging receipt. Review
only committed/quick-checked final source, do not build/probe/mutate or launch
nested agents. Lead records the read-only report as staging-review.md.

Routine planning/evidence is intentionally session-local. Existing reusable
project guide docs/operations/mx2.md remains valid for shared policy and public
cutover limits; temporary ACL/resolver/identity belongs in this rollout record.
