---
lifecycle: archived
---

# mx2 migration: deployed and merged

## Current phase (2026-11-06): approved migration integrated; monitoring rollout remains separate

- [x] Public cutover and delivery accepted, including user-confirmed mailbox receipt.
- [x] Managed aither.aitherdev key removed and deployed; manual key file untouched.
- [x] Final three logical commits independently reviewed, built and merged to master.
- [x] Fresh remote exact-head proof captured; repository and mx2 claims released.
- [ ] Monitoring-consumer activation remains unapproved and separately scoped.

Remote master and retained feature both equal
5941cdb3dda259e91c6a988a7dbf08c84700b326, proven at 21:43Z. The user authorized
"okay, you can merge it when done" for vpsfree-cz-configuration/master. Lead
performed the ordinary fast-forward from 85b38f1cd07d6b3a0fde3eefd32258f747e757e5
in the prepared clean target, with native environment/hooks enabled and no hook
error, then a normal SSH push. Exact-head GitHub Actions query returned no runs;
no CI success is claimed. The temporary target checkout was removed; feature
and recovery refs remain. No merge/deployment command is active.

The final series has three implementation commits: d40952e0 final configuration,
7084114a DNS correction, 5941cdb3 tests/final operations docs. No standalone key
cleanup or rollout-stage commit remains. The earlier claim that deployment
history must constrain Git ancestry was wrong and is superseded in
[staging-review.md](staging-review.md). No migrations or repeated feature-owned
input update streams. Old deployment identities survive in records/refs only.

The clean rebase onto fresh master preserves every ordered stable patch ID and
complete feature-diff byte; master lock SHA256 is
9ed71bd9511c7b4e16e0fd9f4de483e0fe4cf54d2556e715392d28e6e60eacd8.
Retained reviewer0 (Sol/xhigh, read-only) independently accepted patch, history,
input, runtime and deployed-lineage equivalence with no findings. Compared to
actual fe7, only configuration-info/inputs-info and their propagated store paths
change; packages, units, SSH keys/config, mail/TLS/firewall remain identical.
The same provenance-only comparison holds for both DNS and all four monitoring
consumers. Exact VM8pan and its4038-node graph reuse retain the historical-pass/
currently-unavailable-output qualification; no repeat mail/VM campaign was run.

The fresh one-host build passed exit0 in51s, native generation
2026-11-06--22-40-31. Actual output is
/nix/store/nsxwf7wd0d53cwds6bll58bzdhlgkrb2-nixos-system-mx2-26.05.20261026.718f670,
deriver qb3gvij7i0grwn1g15x15k823mxdl7y0, NAR
sha256-2CyWvkVaTz3/oAm8nkpLuVkjS7EiDRHeHLanm/Wp9EI=.
Native generation/source/role/input proof passed. The separately advertised
confctl log was absent; complete watcher output and exit evidence are retained.
No new deployment was necessary solely for equivalent provenance metadata.

Actual current/profile deployment remains fe7a8c1130356bc185b0c2b8f17916645277e976,
system /nix/store/5gjb3k3arwkvn5hq2y27d8jgfnwmgsjj-nixos-system-mx2-26.05.20261026.718f670,
native generation2026-11-06--22-24-51, system profile7. Managed fingerprint
SHA256:38gX47C2LkQgccktDtHa27hPk8wXo3kXLMGUQSnswK0 is absent; all other managed
keys are retained. Manual /root/.ssh/authorized_keys remains byte/metadata-identical:
SHA256 ccb82af6b6b6b1e7baa9aaa815701119a5521b3ed7c2a15305788134f7dcd689,
regular root:root0600, size834, inode137146, original Nov3 mtime, requested key
present once. The user owns its later removal and may now do so. Both manual
and managed AuthorizedKeysFile paths remain supported. Last actual check proves
healthy SSH/Postfix/Postgrey/firewall, system running, no jobs, queue0. Booted4pc5
and bootIDce6c77e2 remained unchanged; no second reboot.

The independently proven equivalent successor is now integrated; fe7 is not
claimed as a literal ancestor or 5941 as activated. All prior rollout states are
superseded by verified fe7. Repository claim c9e49ef9-e2c5-4d71-b893-59232f8b0b7f
released at21:43:36Z immediately after remote proof. Machine claim
13ba611e-2f87-4036-b958-b0e056e13da7 released at21:43:45Z and status verified,
after deployment effects and complete equivalent deployed lineage were proven.

The user's spam question was answered using the actual test boundary:
unauthenticated unrelated-domain relay rejection passed over IPv4 and IPv6.
This does not prove comprehensive spam filtering or SPF/DMARC enforcement.
Domain-wide recipient acceptance still allows later rejection/bounce backscatter;
changing recipient/filter policy remains separate work, not a new merge gate.

Remaining separately scoped work is monitoring activation for prg/int.mon1,
prg/int.mon2, prg/int.alerts1 and prg/int.alerts2. Their earlier builds remain
valid for behavior, but none was activated. Keep old VPS2992/disk/independent
shell and Postgrey backup for recovery. Its old queue count was not independently
measured here. No old-host retirement, additional mail, archive, deletion or
session-stop action is authorized. Session stays active for the remaining rollout.

Evidence: [deployment receipt](public-profile-preparation.md),
[review record](staging-review.md), public-integration-preparation.json,
public-integration-built.json, public-integration-build.log/result JSON,
public-integration-remote-proof.json and public-key-final-activation-verification.json.
Reusable host operations remain in the configuration repository's
docs/operations/mx2.md; no further product documentation change was needed.

### Additional public forwarding test: PASS

The user explicitly requested one additional message through public mx2 to
verify forwarding to the primary, extending the earlier two-message scope by
one. Implementer0 sent the fixed 513-byte message once through 37.205.11.114:25
with trusted TLS, from/to podpora@vpsfree.cz. Subject:
`[mx2 public TEST] forwarding to primary`.
Message-ID: `<mx2-public-forward-0690f053dba14e0780132288d76e1693@vpsfree.cz>`.

At 20:52:59Z mx2 returned final DATA `250 2.0.0 Ok: queued as 8521868783`.
Its own queue log then proved forwarding to
`prasiatko-mail.vpsfree.cz[37.205.15.53]:25`, `dsn=2.0.0`, `status=sent`, and primary
response `250 2.0.0 Ok: queued as ED634234C3B`, followed by queue-entry removal.
Delivery delay was 0.65s. The bounded read-only observation at 20:53:22Z found
both the own queue entry count and total mx2 queue count zero. No greylisting,
resend, queue flush, fault or source/runtime change was needed. Exactly one
additional DATA payload was accepted; cumulative authorized test messages are
three, including the previous two staging messages.

Primary handoff and mailbox receipt are proven: the user confirms the new
message arrived. The log's `tls=may` is a policy indicator, not proof of a negotiated
outgoing cipher; egress source is not independently shown in this message log.
Evidence: public-forwarding-test.json and public-forwarding-test.eml, summarized
in [the existing deployment receipt](public-profile-preparation.md). The owner
package is accepted and no operation remains active. This request grants no
monitoring deployment, default integration or cleanup authority.

At the public-cutover checkpoint, VPS 27627 ran the reviewed final public configuration, source
b120342c4517b6faa1a519913ab92acafbc506f3, system 9ywq4 and profile system-6-link.
Both public addresses, 37.205.11.114 and 2a03:3b40:100::1:95, are installed with
working routes; private management 172.19.9.22 remains available. Public A/AAAA
and both PTR records match mx2.vpsfree.cz. No reboot or input update was needed.
Booted-system remains staging 4pc5; the actual current/profile system is final.

The lead activated the exact bootstrap generation 2026-11-05--13-04-34, verified
a real trusted Let's Encrypt certificate and Postfix's use of it while SMTP was
restricted, then activated final generation 2026-11-05--13-11-54. Both dry runs
and switches passed. Actual system identity, mail/SSH/firewall/exporter/syslog
health, no pending jobs and an empty queue were verified at 20:36:28Z. Renewal is
scheduled; the certificate is valid through 2027-02-04. Full source, input, output
and activation evidence is linked in [the deployment receipt](public-profile-preparation.md).

Public IPv4 SMTP, trusted STARTTLS and unrelated relay denial passed in the
owner's reply-aware client. The user independently supplied external IPv6 TLS
chain/hostname verification, then the corrected SMTP client's exact result:
`554 5.7.1 <mx2-check@example.org>: Relay access denied`.
This closes the remaining external IPv6 relay check. The initial piped OpenSSL
probe's protocol-synchronization error was a client-command error, corrected
without server changes. No DATA or additional message was sent by these probes.
The prior two staging payloads both arrived, including the queue-persistence test.

Actual established sockets also proved primary SMTP greeting/EHLO/QUIT from
both public source addresses. This proves the forwarding connection, not a new
public-source message delivery. The shared recipient/filter baseline remains
unchanged; known domain-wide recipient acceptance/backscatter and broader
SPF/DMARC policy are separate follow-ups.

All public-cutover acceptance checks are complete. No activation, probe or
verification command remains active. Implementer0's package is accepted; no
source fix, build rerun, extra mail, reboot or further test is needed for cutover.
Both bootstrap 27fc and final b120 retain the frozen deployed 084488 input graph.

This is the historical public-cutover checkpoint. Its then-pending key removal,
merge and claim release are superseded by the current section above. Monitoring
activation and old-host retirement remain separately scoped.

## Nov5 preparation snapshot (superseded by Nov6 checkpoint)

The user corrected the unnecessary reboot requirement and requested clear steps
and ownership, then explicitly said "agreed, proceed". Lead released one bounded
public-profile package. Preparation uses the private172.19.9.22 endpoint and the
currently deployed NixOS inputs. No extra publicIP, input upgrade or planned
reboot is required. The normal configuration-switch path replaces the obsolete
boot-plus-reboot wording for this phase.

Architect0 owns the corrected sufficient brief and cutover ordering;
implementer0 owns source, quickchecks, commits, publication and generated evidence;
lead owns scope, independentreview, builds and the eventual operator handover.
Two native generations are planned: TLS bootstrap retains the current source-only
SMTP ACL, then the final generation opens public SMTP after trustedcertificate
verification. Prepare/review/build/copy privately. ActualHTTP01 issuance follows
old/new publicaddress handover; source metadata itself does not allocate anIP.
The user confirms old CentOS VPS2992 and shell access independent of its public
addresses; candidate is27627. The operator can select exact allocations/interface
in vpsAdmin at handover. Keep the oldqueue/disk and deployed084488 provenance.
Current final preparation commit is b120342c4517b6faa1a519913ab92acafbc506f3;
bootstrap is retained by the separate tls-bootstrap ref. Both passed quick checks and independent review; both required build batches completed successfully;
actual-output verification, both private copies and the final read-only guest
verification passed. No new activation has run.
No publictransfer, primary
or oldhost change, defaultintegration or extra testmessage has occurred.

Retain existing tested shared recipient/filter policy as the migration baseline.
Domain-wide backup acceptance and backscatter remain known limitations; recipient
export/sync and a broader SPF/DMARC audit are separate followups, not preparation
gates. The original primary-observed source/NAT remains unknown.

| Package | Owner | Dependency and acceptance | Status |
| --- | --- | --- | --- |
| Correct public-profile brief and numbered handover | architect0 | Pinned native ACME/startup semantics; no reboot/inputrefresh | Accepted; released directly to implementer0 |
| Bootstrap/final source and generated checks | implementer0 | Recorded sufficient brief; hostname/TLS/ACL/keys/policy/input proof | Accepted: both heads published; hooks/generated checks/consumer proof complete |
| Independent final review then required builds | lead / reviewer0 | Committed complete package and quickchecks | Accepted: review, six builds, exact-output proof, both copies and remote verification pass |
| Public IP handover, certificate and final switch | lead / user in vpsAdmin | User moved both allocations; actual guest networking and trusted TLS verified | Accepted: final runtime, both public SMTP/TLS/relay checks and both primary connection paths pass |

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
- [x] User confirms both marked messages reached podpora@vpsfree.cz.
- [x] Prepare and independently review public TLS-bootstrap and final sources at frozen inputs.
- [x] Build bootstrap mx2 and final mx2/mon1/mon2/alerts1/alerts2 successfully.
- [x] Verify actual generations/outputs and copy both mx2 systems privately without activation.
- [x] Confirm remote copied hashes and unchanged staging runtime/queue by one read-only check.
- [x] Verify user-reported public-address transfer and both guest routes.
- [x] Activate bootstrap and verify real trusted certificate plus SMTP gate.
- [x] Execute final ordinary switch; native health checks pass.
- [x] Verify final source/services/queue, public IPv4 TLS and relay denial, DNS/PTR and both source routes to primary.
- [x] Verify external IPv6 SMTP connectivity and trusted TLS from user-provided output.
- [x] Correct and validate reply-aware SMTP command sequencing on public IPv4.
- [x] User confirms external IPv6 RCPT denial with the corrected reply-aware client.
- [x] User confirms public forwarding delivery; managed key removal deployed and verified.
- [x] Consolidate final history into three implementation commits; user approves configuration/master integration.
- [x] Rebase onto fresh master; independent patch/runtime/input/history equivalence accepted.
- [x] Build and verify exact final 5941 output, then merge/push/prove remote integration.
- [x] Release repository and mx2 claims after verified deployment and equivalent integrated lineage.
- [ ] Monitoring-consumer activation remains separately scoped and unapproved.


Prepared native mx2 generations: bootstrap `2026-11-05--13-04-34` ->
`/nix/store/yyq4710fi3nz3mxb60b51z8q04mqkki7-nixos-system-mx2-26.05.20261026.718f670`;
final `2026-11-05--13-11-54` ->
`/nix/store/9ywq4mzx32rmplnn8nyc7hpql8vjf3sa-nixos-system-mx2-26.05.20261026.718f670`.
Full source/roles/output NARs and all five final consumers are bound in
public-built-systems.json and [public-profile-preparation.md](public-profile-preparation.md).
Lead verified held machine mapping at finalb120, then copy-only transferred both
generations with strict SSH (27.718s and14.088s, both exit0). Both copy commands
are closed; public-copy-result.json and per-copy logs retain evidence. The new
systems have not been activated. Bootstrap used fresh Luna/low utility; final
build used the monitoring skill's visible parent fallback and a complete process
log, with exact exit0/162.881s. No extra VM run or DNS behavioral build.

Final remote verification at2026-11-05T12:22:35Z completed in0.693s (one strict
SSH call, no retry). Both copied toplevel NARs/derivers, clean source metadata and
embedded input revisions match local built receipts. Current/profile/booted still
point to4pc5/clean084488; only private172.19.9.22 is present, no transferred publicIP.
System/mail/firewall/SSH healthy, queue0; ACME base/order/timer not loaded/active.
No new certificate issuance, service switch, reboot or mail. Remote absence of
vpsadminOS build-sourcec24mbj... is explicit: runtime closures were copied, not
every build source. Full source/input graph and NAR proof remains local and linked.
[Preparation receipt](public-profile-preparation.md) and
public-copy-guest-verification.json contain the exact proof. No operation remains
active. Claim13ba remains held because deployed lineage is not integrated.

Next operator action: on2992 account for/drain its queue and stop the old SMTP
service at handover; preserve disk and IP-independent shell. In vpsAdmin unassign
only the two intended public allocations, wait for completed removal, then assign
their routes and same host addresses to27627's existing interface, retaining
172.19.9.22. User execution/report of that handover will release the prepared
bootstrap switch, trusted-certificate verification and final switch. If old mail
is still queued, retain it and resolve delivery before proceeding. No default merge
or lifecycle action follows automatically.

## Exact source, artifact and ownership

Repository vpsfree-cz-configuration, canonical origin
`git@github.com:vpsfreecz/vpsfree-cz-configuration.git`.
Branch2026-11-01-mx2-nixos-migration, owned worktree
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-01-mx2-nixos-migration/vpsfree-cz-configuration`.

| Boundary | Exact identity |
| --- | --- |
| Reviewed and actually deployed staging head | `0844881779d62d9a6a86d2bacd61d21565b33932` |
| Tree | `34dc1820c5feda2a0d875f60c964b8375de0af49` |
| Reviewed base | `c4107822060e9e34b24a83950d618c9f28a7722b` |
| Fresh observed remote master | `f4069909b55fbed907cb658f350ec6a59f97e05a` |
| Native built generation | `2026-11-03--15-47-12` |
| Deployed toplevel | `/nix/store/4pc5mic0rp9h5qb2lhgmdh2x8z50pqd2-nixos-system-mx2-26.05.20261026.718f670` |
| Deriver | `/nix/store/bpyiq4bfdmd9anf96zqyg8kqmyd3d9b0-nixos-system-mx2-26.05.20261026.718f670.drv` |
| Toplevel NAR | `sha256-dGOqT6fHxNlWSfrfMGRzPem0RqpuLSzHLoWJ/CG5cjg=` |

At staging completion the worktree was clean; the exploratory DNS prepend draft was removed after clean
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
interruption or mailbox credential access. Primary acceptance and user-confirmed
mailbox receipt are proven. No uncertain DATA resubmission occurred.

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

## Sender-authentication question after receipt confirmation

User confirmed both messages arrived and asked why sender authentication allowed
this and whether primary accepts arbitrary forwarding. Bounded public DNS lookup
at2026-11-04T17:11:25Z found existing vpsfree.cz SPF with a/mx/explicit-host
mechanisms ending -all, and DMARC p=none reporting to podpora. Exact records are
in mail-auth-public-dns.json and the owner final result. Both submitted test files
claimed podpora as envelope and visible sender and contained no DKIM signature.
No primary-facing/NAT source or delivered Authentication-Results/Received-SPF
headers were captured. Therefore sender-authentication outcome and why the primary
accepted those particular messages are not established. Primary unrelated-domain
relay was not tested; own-mailbox reception is distinct from open relaying.
No new primary contact, SMTP payload, source change or security campaign occurred.
