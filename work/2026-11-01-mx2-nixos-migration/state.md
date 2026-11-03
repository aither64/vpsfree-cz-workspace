---
lifecycle: active
---

# mx2 private staging

The private staging candidate is implemented, independently reviewed, published
and built successfully. **It has not been deployed.** Container27627 at172.19.9.22
still runs its original NixOS25.05 system. Agent activation awaits exact-target
admission in the workspace machine-reservation catalog. User approval for that
separate workspace catalog/user-package update has been requested; no such source
or package change has occurred.

The user authorized agent deployment: "done. well, with this access, you can
deploy mx2 yourself." This covers the private candidate only. CentOS/public IP
transfer, public DNS, primary configuration and default-branch integration remain
excluded. The feature is ready, awaiting merge approval; the session stays active.

## Phase checklist

- [x] Recover/rebase source; preserve original/import/runtime/reviewed refs.
- [x] Shared mail corrections, internal DNS source correction and VM suite.
- [x] Prior independent reviews and five production/DNS-consumer builds.
- [x] Verify supplied candidate host fingerprint and establish root SSH access.
- [x] Bounded read-only candidate/source-address preflight.
- [x] Architect minimal private staging contract; implement two host files.
- [x] Quick checks, normal hooks, generated mail/firewall/resolver/key assertions.
- [x] Clean rebase, consolidated history, exact publication/comparison.
- [x] Independent final staging review with no Blocking/Important findings.
- [x] Exact VM consumed-graph reuse and scoped consumer-build proof.
- [x] Five-system native staging build and registered-output verification.
- [ ] Resolve configured candidate admission and acquire exact machine ownership.
- [ ] Copy/dry-activate/switch exact new system; verify runtime and installed identity.
- [ ] At most two controlled podpora messages and candidate-only queue/reboot test.
- [ ] User confirms receipt; record live result and remaining public-cutover gates.
- [ ] Separately approved default integration and public-address cutover.

## Current repository and source

Repository vpsfree-cz-configuration, SSH origin
`git@github.com:vpsfreecz/vpsfree-cz-configuration.git`.
Branch2026-11-01-mx2-nixos-migration, worktree
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-01-mx2-nixos-migration/vpsfree-cz-configuration`.

| Boundary | Exact revision |
| --- | --- |
| Fresh remote master/base | `c4107822060e9e34b24a83950d618c9f28a7722b` |
| Current local/published staging head | `0844881779d62d9a6a86d2bacd61d21565b33932` |
| Tree | `34dc1820c5feda2a0d875f60c964b8375de0af49` |
| Host/shared/private staging | `548514a9e573ccbc3f145d49d7d307c3e23b5aa5` |
| DNS source correction | `e7cd91d881fce72fe15339a8df736a6481d7000d` |
| Tests/docs | `0844881779d62d9a6a86d2bacd61d21565b33932` |

Worktree clean, remote exact, comparison captured, feature CI empty. Final range
13paths/740 additions/four deletions. Only two host files differ from prior
reviewed1e behavior; the inherited upstream lock change is separate. Original
source40411, reviewed importe4, successful VM runtime8d and reviewed-mail1e refs
remain preserved. None is claimed literally merged/deployed in refreshed ancestry.
No obsolete final host/key/exporter iteration, migrations, queue conversion or
feature-owned repeated dependency stream remains; independent review agrees.

Full final lock equals current default: blob
`f6b87ab2ca27a72c3fe1bdd134129ff1e4a9f7e9`, SHA256
`507e781c2fa52da5a389e6eab824efe68baa72b1727de0fc162ea0a5e6b4c098`.
Only upstream vpsadminServices changed from the old root lock; mx2/test selected
roles remain nixpkgsStable718f670e and vpsadminosOsStagingb45b27b4. Do not describe
the entire root lock as unchanged. Full graph is recoverable from final flake.lock
and recorded in staging-input-graph.json.

## Actual candidate and staging behavior

[Candidate preflight](candidate-preflight.md) preserves both initial refusals and
subsequent success. User-supplied ED25519 fingerprint exactly matched; only the
verified exact-host known_hosts entry was added locally. The user installed the
existing workspace public key; strict pinned-key root SSH then worked.

Observed: NixOS25.05/LXC, hostname mx2, stateVersion25.05 from installed source,
persistent ZFS tank/ct/27627 root/var/nix, private172.19.9.22/32, IPv4 default route,
link-local IPv6 only, no old public address, active Postfix/Postgrey and zero queue.
Workspace source172.16.106.40 is confirmed. Physical node, NAT and actual primary
DNS/SMTP connectivity remain unverified. The guest lacked dig; no tool was
installed or fabricated DNS answer recorded.

Still-installed current/profile/booted rollback reference:
`/nix/store/98n9xjgm42pjmzi9vy430qilp2hqbzvb-nixos-system-mx2-25.05.git.7c43f080a`.

Staging preserves ID/target/hostname/stateVersion, host networking and tested mail
policy. It uses private metadata, no auto-update or production monitoring/logging,
sole resolver1.1.1.1 and TCP25 only from172.16.106.40/32, retaining SSH22 and enabled
firewall. It does not add the source to Postfix trusted networks. Generated key
inspection caught an omitted workspace key; the existing confData reference is
now explicitly included locally for the candidate, preserving all previous keys.
No global credentials or administrator settings changed.

## Review, tests and native build

[Staging implementation](staging-implementation.md) holds exact generated/settings,
source/inputs, consumer, publication and build-target receipts.
[Independent staging review](staging-review.md), retained reviewer0
Sol/xhigh/read_only, clears all four applicable lanes with no Blocking/Important
finding. It includes explicit whole-history/migration/update-stream conclusions.
Prior [mail review](verification-review.md) and [metadata review](monitor-review.md)
remain applicable to unchanged content.

Generated main.cf/transport/Postgrey/Postfix derivations/text equal reviewed1e;
firewall, resolver, approved keys, private metadata and absent exporter/rsyslog
were verified. Actual selected-consumer comparison changes only mx2 Prometheus
scrape/ping entries and Alertmanager node-down inhibition. Both DNS consumers
change only revision metadata; their new revision-bearing closures are not claimed
built. Build set is mx2,mon1,mon2,alerts1,alerts2; none of those consumers is deployed.

The final VM check is exactly the historical passing8pan3ddqairw3js87iaysvjqwzalxgls
derivation. Root canonical SHA256d1e739bbeefe29f257dbb3a5e27558bb2183fe48314d324fa59a7ee661191255
and4038-node consumed graph SHA256e366b1480f8650a403de926389d537a45e9652f37ea962422ba2117ba0915c96
were independently confirmed. Reuse is immutable graph proof, not tree equality;
inherited vpsadminServices is not consumed. Historical VM output was realized/NAR
verified then later absent locally; current presence is not claimed and no rerun
was needed. See [prior results](verification-results.md) and batch6 record.

The native five-system batch completed exit0 in154.13s (parent handle43854).
Actual generation/output/deriver/NAR and input/configuration-info checks passed.
All current generation links select2026-11-03--15-47-12: confctl reuses an existing
matching toplevel/input generation, so the later invocation did not make a new
15-50 generation. Actual mx2 built output:
`/nix/store/4pc5mic0rp9h5qb2lhgmdh2x8z50pqd2-nixos-system-mx2-26.05.20261026.718f670`.
Full five-system bindings are in staging-built-systems.json and
staging-build-result.md. These are build outputs, not deployed profiles.

Execution reconciliation: the fresh watcher was interrupted after lead mistakenly
assumed it had not started. A parent fallback duplicated a local build invocation.
The earlier watcher-created generation was subsequently reused. Preserve the
mixed/NUL-containing raw log and actual registration/generation proof; no extra
build, deployment or cleanup was performed to hide this. Parent's exit0/status is
retained. No owned build or uncertain remote mutation remains.

## Admission and live verification still pending

[Deployment admission proposal](deployment-admission.md) describes the additional
workspace catalog/user-package update requested from the user. Installed catalog
contains only aitherdev. Mandatory guide requires a held claim for the exact
configured machine; no candidate/physical-node mapping or documented dynamic
registration/guest exemption exists. No surrogate claim or bypass is allowed.
The proposal has not changed workspace source or selected package, and default
integration remains separately unapproved.

After admission, acquire exact ownership near activation; preserve rollback
state/key access and empty/accounted queue. Lead copies and dry-activates then
switches only the reviewed built mx2 target and checks new current/profile/source,
SSH/network/firewall/DNS/units/persistence. No consumer/DNS/primary/CentOS activation.

User supplied important mailbox podpora@vpsfree.cz. Send at most two marked small
messages, same return address, normal delivery then candidate-only temporary
SMTP egress outage/restart/reboot recovery. No deliberate live DSNs, primary
interruption, invalid-recipient campaign or mailbox credentials. User confirms
receipt. No live test mail has been sent yet.

Public IPv4/IPv6 ingress, final outbound identity, inbound TLS, recipient/backscatter
and absent-milter policy remain cutover gates. Keep CentOS and NixOS queues
independent; preserve/drain accepted NixOS mail even if ingress rolls back. No
CentOS spool/database conversion is implemented. The internal DNS correction is
source only. Keep original host/public DNS unchanged throughout private staging.

Owners: architect0 completed bounded design/staging contract; implementer0 owns
completed source and final build-receipt validation; reviewer0 completed independent
review; lead owns admission, activation and acceptance. Reusable project guidance
remains docs/operations/mx2.md; temporary rollout evidence remains here. No session
lifecycle action is authorized or performed. Session and worktree stay open.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-01-mx2-nixos-migration/).
