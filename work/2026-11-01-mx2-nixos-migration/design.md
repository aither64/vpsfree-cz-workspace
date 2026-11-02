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
