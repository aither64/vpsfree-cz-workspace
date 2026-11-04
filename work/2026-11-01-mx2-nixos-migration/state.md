---
lifecycle: active
---

# mx2 private staging deployment

The reviewed mx2 build is deployed and the live private-network checks passed.
VPS27627 at172.19.9.22 is booted into the expected4pc5 system from clean source
08448817. Both controlled messages were accepted by the actual primary; the
outage message retained its exact envelope/full payload across a Postfix restart
and a VPS reboot. Temporary fault rules/units/drop-in are removed, services are
healthy and the queue is empty. Mailbox receipt confirmation from the user is
pending; no mailbox credentials were requested.

CentOS, public DNS and public addresses were unchanged. This is a private staging
result, not production replacement certification. The branch is ready, awaiting
merge approval; lifecycle remains active and this session stays open.

## Phase checklist

- [x] Recover/rebase original source and preserve source/import/runtime refs.
- [x] Correct mail policy and internal DNS source; pass isolated mail suite.
- [x] Complete independent source/history reviews and required system builds.
- [x] Prepare reviewed private staging identity/firewall/DNS/admin access.
- [x] Resolve workspace admission with updated schema2 configured-machine claims.
- [x] Deploy the reviewed generation; recover live D-Bus transition and clean boot.
- [x] Reset only unused Postgrey state with explicit user approval and backup.
- [x] Verify actual booted/current/profile/source, private network, services and DNS.
- [x] Verify SMTP/SIZE and unrelated-domain relay denial without DATA.
- [x] Normal controlled delivery to real primary after native greylisting.
- [x] Accepted queue/content persistence across service restart and VPS reboot.
- [x] Remove exact owned fault, restore delivery, verify primary acceptance/queue0.
- [ ] User confirms both marked messages reached podpora@vpsfree.cz.
- [ ] Separately approved default integration and public-address cutover checks.

## Exact source, artifact and ownership

Repository vpsfree-cz-configuration, canonical origin
`git@github.com:vpsfreecz/vpsfree-cz-configuration.git`.
Branch2026-11-01-mx2-nixos-migration, owned worktree
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-01-mx2-nixos-migration/vpsfree-cz-configuration`.

| Boundary | Exact identity |
| --- | --- |
| Reviewed/deployed/local/published head | `0844881779d62d9a6a86d2bacd61d21565b33932` |
| Tree | `34dc1820c5feda2a0d875f60c964b8375de0af49` |
| Reviewed base | `c4107822060e9e34b24a83950d618c9f28a7722b` |
| Fresh observed remote master | `f4069909b55fbed907cb658f350ec6a59f97e05a` |
| Native built generation | `2026-11-03--15-47-12` |
| Deployed toplevel | `/nix/store/4pc5mic0rp9h5qb2lhgmdh2x8z50pqd2-nixos-system-mx2-26.05.20261026.718f670` |
| Deriver | `/nix/store/bpyiq4bfdmd9anf96zqyg8kqmyd3d9b0-nixos-system-mx2-26.05.20261026.718f670.drv` |
| Toplevel NAR | `sha256-dGOqT6fHxNlWSfrfMGRzPem0RqpuLSzHLoWJ/CG5cjg=` |

The worktree is clean; the exploratory DNS prepend draft was removed after clean
boot proved actual resolver behavior correct. No corrective source/package change
or new build was required during deployment. Explicit deployed-staging ref retains
084488. Current/profile/booted all match the toplevel; configuration-info records
clean084488. Full role/source/input bindings are in staging-built-systems.json,
staging-input-graph.json and the final lock at084488. Lock blob
f6b87ab2ca27a72c3fe1bdd134129ff1e4a9f7e9, SHA256
507e781c2fa52da5a389e6eab824efe68baa72b1727de0fc162ea0a5e6b4c098.
Selected roles:nixpkgsStable718f670e, vpsadminosOsStagingb45b27b4. Full input graph
remains recoverable from the exact committed lock; no whole-lock-unchanged claim.

Schema2 claim13ba611e-2f87-4036-b958-b0e056e13da7 covers exact configured target
cz.vpsfree/containers/mx2 in the registered canonical repository. It was acquired
and verify-machine checked against084488 before activation. Logical identity:
machine:github.com/vpsfreecz/vpsfree-cz-configuration:cz.vpsfree/containers/mx2.
The claim remains held: remote ancestry proof shows084488 is not integrated into
current remote master, and integration approval is absent. Do not release merely
for turn completion or mailbox confirmation. No repository merge claim is held.
No workspace package/catalog change was performed by this session; the user's
workspace update supplied the needed native target resolution.

## Actual rollout and recovery

[Deployment preparation](candidate-deployment-preparation.md) and
[live execution contract](candidate-live-verification.md) record the bounded
commands. Lead copied the exact generation, acquired/verified ownership, dry
activated and switched with strict SSH and native rollback protection.

The live25.05→26.05 switch was the wrong choice for this D-Bus transition.
The old daemon remained running while the new unit expected broker notify-reload,
blocking activation. One broker restart cleared it, but disconnected the original
activator. Confctl returned0 while mail startup was unfinished; explicit checks
caught this. Native same-generation recovery consumed retained /run/nixos lists.
The user then rebooted the candidate; clean boot restored fast SSH sessions and
sole1.1.1.1 resolver behavior. No agent reboot was issued for that recovery.

Postgrey still failed because its underlying library changed5.3.28→4.8.30. A
complete protected backup and separate clones proved4.8 rejects log version19,
while matching5.3 opens both databases. Old/live file hashes stayed unchanged
through diagnosis. The user explicitly confirmed the candidate was never used
and authorized a database reset. Owner moved the old environment into protected
reset-original beside the untouched backup; native service startup created fresh
4.8 state and became healthy. Postfix queue/spool was never reset.

Protected backup base:/root/mx2-postgrey-recovery-20261104-57422c4b. No database
conversion/equivalence or automatic database rollback is claimed. Original system
98n9 remains a recorded recovery reference; accepted mail/state compatibility must
be reconciled before any software rollback. See the reusable
[recovery lesson](../../notes/vpsfree-cz-configuration/2026-11-04-mx2-boot-and-postgrey-recovery.md).

## Live verification evidence

Initial clean boot ID507276a8-af4c-4ff0-8769-d12f82669058 changed to
ce6c77e2-986c-42ac-af10-b77d3c8ef5ff during the one agent-issued persistence-test
reboot. The same persistent ZFS guest storage and exact source/system paths
survived. Actual private IPv4 is172.19.9.22/32, test client172.16.106.40; no old
public IP or usable global IPv6 is configured. Actual resolver1.1.1.1 returns
primary A37.205.15.53/AAAA2a03:3b40:fe:1c3::1. Private SMTP firewall restriction,
approved SSH access and disabled exporter/central logging are retained.

SMTP EHLO/SIZE104857600 and unrelated-domain RCPT5545.7.1 Relayaccessdenied passed
without DATA. Candidate and real primary both applied native greylisting; waits
and retries used the same message/tuple, without bypass or extra client DATA.

| Controlled message | Candidate queue ID | Result |
| --- | --- | --- |
| [mx2 staging TEST 1/2] normal delivery | `791FC69382` | Primary250 accepted as55F35A7ED; queue removed |
| [mx2 staging TEST 2/2] queue recovery | `D242768B88` | Full471-byte payload/envelope retained through restart/reboot; Primary250 accepted asC5F44F212 after restoration; queue removed |

Only two small client payloads were accepted, both sender/recipient
podpora@vpsfree.cz. No deliberate live DSNs/invalid-recipient campaign, primary
interruption or mailbox credential access. Primary acceptance is proven; user
mailbox receipt is requested separately. No uncertain DATA resubmission occurred.

The temporary native fault under/usr/local/lib/systemd/system blocked only the
candidate's TCP25 connections to the exact primary A/AAAA. Positive IPv4 reject
counter and the sole owned deferred queue item proved the block; a brittle
expected log string was corrected because final IPv6unreachable masked the IPv4
reason. Full own payload/envelope checks passed before/after restart and reboot.
PostfixRequires/After held the persistent fault in place before mail startup.
No general network/DNS/SSH or host-side change was made. Checksummed unit/drop-in,
OUTPUT jumps and both owned chains were removed; actual cleanup/queue drain and
service/access/DNS health were verified. No test fault or unfinished operation
remains. [Final deployment/live result](candidate-deployment-result.md) records exact
message/primary queue IDs, full payload hash, boot IDs, cleanup hashes, final
health timestamp and retained recovery data. Raw milestone evidence is
mx2-live-status.json and the linked delivery/persistence/cleanup receipts.

## Earlier review/build evidence and next boundary

[Staging review](staging-review.md), retained reviewer0 Sol/xhigh/read_only,
cleared all affected lanes and complete history/migration/update streams.
[Staging build result](staging-build-result.md) binds the exact five-system
realizations. Prior [verification results](verification-results.md) retain the
isolated three-VM pass. Final8pan test derivation and full consumed graph matched
that pass exactly, independently verified; historical output later absent locally
is an artifact availability qualification, not an invented new runtime failure.
Both DNS consumers differed only in revision metadata, so no DNS behavior rebuild
or activation was claimed. Monitor/alert consumers were built but not deployed.

Complete final series remains548514a9 host/shared/private policy,
e7cd91d8 internal DNS source,08448817 tests/docs. No migrations, obsolete final
fixups or feature-owned repeated input streams. Original40411, reviewed importe4,
runtime8d and reviewed-mail1e refs remain preserved without nonancestor literal
merge/deployment claims. Source baseline updates belong to upstream history.

Public cutover still needs final IP ownership/routing/PTR/HELO and real public
IPv4/IPv6 checks, intended inbound TLS and recipient/backscatter/filter policy.
Current runtime banner is mx2.localdomain and inbound STARTTLS is absent; the
milter is intentionally absent/fails open. Those are recorded public-use gates,
not hidden staging successes. Preserve independent CentOS/NixOS queues; retain
and drain accepted NixOS mail on ingress rollback. No CentOS spool conversion.
Internal DNS correction remains source-only; this session performed no live DNS
reload, CentOS change, public address transfer or default integration.

Owner0 executed preparation/diagnosis/reset/live checks and cleanup; architect0
owned bounded design reconciliation; reviewer0 provided independent source review;
lead owned claim/activation, acceptance, user communication and records. Session
and worktree remain open; no lifecycle cleanup is authorized or performed.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-01-mx2-nixos-migration/).
