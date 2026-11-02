---
lifecycle: active
---

# mx2 migration and automated verification

Implementation, independent review, automated mail verification and all five
affected-system builds are complete. The published feature is ready, awaiting
merge approval. It is ready for controlled staging; production replacement still
requires the live checks below. This session remains open and active.

The user authorized autonomous verification and internal mail-zone source
correction against public DNS. No deployment, DNS reload, real mail submission,
primary changes or default-branch integration occurred.

## Phase checklist

- [x] Recover/rebase the old branch; preserve original source and import refs.
- [x] Record Debian 13 primary outside this repository and bounded live baseline.
- [x] Architect the isolated verification package and implement shared mail policy.
- [x] Correct internal mail-zone source and validate all four template variants.
- [x] Commit/consolidate history; pass quick checks, hooks and fidelity checks.
- [x] Complete full independent review and reconcile R1/R2 and narrow test fixes.
- [x] Pass the full three-VM mail matrix, including queue/reboot recovery.
- [x] Repair exporter metadata; complete affected-lane independent review.
- [x] Build final mx2 and all four DNS consumers; reconcile actual source/inputs.
- [x] Publish final branch, capture comparison and prepare verification handoff.
- [ ] Separately authorized controlled staging and live production acceptance.
- [ ] Explicitly approved integration into configuration master.
- [ ] Separately authorized cutover with queue-safe rollback.

## Final repository and history

Repository: `vpsfree-cz-configuration`, SSH origin
`git@github.com:vpsfreecz/vpsfree-cz-configuration.git`.
Branch: `2026-11-01-mx2-nixos-migration`.
Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-01-mx2-nixos-migration/vpsfree-cz-configuration`.

| Boundary | Exact revision |
| --- | --- |
| Fresh unchanged remote master/base | `c040c14cdbacc07998700b524996a89306188d7f` |
| Final local/published head | `1e3afc478fb72b54a25a0147910463f060fee88f` |
| Final tree | `77d73449040aba400215ca81843c3d6a2173593c` |
| Host/shared mail/exporter metadata | `9c6e36135192f65baed975e3b127160f068e0b0d` |
| Internal DNS source | `a5848319ae19d1bcd348ab3837683dec71c90e01` |
| Tests and documentation | `1e3afc478fb72b54a25a0147910463f060fee88f` |

Fresh remote proof confirms the exact feature and base; worktree is clean,
comparison captured, feature CI run list empty. Final diff: 13 paths,
733 additions/four deletions. No migrations, dependency/input changes or repeated
update streams. Independent review explicitly cleared complete history and
migration provenance; no obsolete final implementation history remains.

Preserved refs under the session prefix retain original source
`40411d67ee97cea800bcccd89b0473432b4502c4`, reviewed import
`e4c1ac0c5ae7426fb019b79ba936b30ce63e6e6c`, and successful runtime head
`8d4e03d53699d80f46030b0ee6eb213151b8ae30`. These nonancestor revisions are not
claimed literally merged or deployed. The source checkout remains untouched.

## Verification and actual build provenance

[Verification results](verification-results.md) is the authoritative final
summary, with full realized system paths, derivations, NAR hashes and generation
bindings. [Batch 6](verification-run-6.md) passed the full mail test in 227.03 s
(script 202.93 s): IPv4/IPv6 relay authorization, envelope/content integrity,
greylisting and filtering failures, accepted queues through service restart and
same-disk reboot, recovery/drain, primary 450/550 behavior, DSN, TLS/fallback and
SIZE boundary. All guests used restricted networking and local nonforwarding DNS;
native cleanup completed.

The final metadata-only successor has the identical successful test derivation
`/nix/store/8pan3ddqairw3js87iaysvjqwzalxgls-vm-test-run-mx2.drv` and complete
input graph. Independent review accepted reuse. The output was realized and
NAR-verified immediately after success but is now absent/unregistered locally;
cause unknown, no session-owned store deletion. Historical pass and exact graph
proof remain valid; current artifact presence is not claimed.

[Batch 7](verification-run-7.md) passed the final native five-system build,
exit 0 in 161.55 s:

```sh
nix develop --no-write-lock-file -c confctl build --yes \
  'cz.vpsfree/containers/{mx2,brq/int.ns1,prg/int.ns1,prg/int.mon1,prg/int.mon2}'
```

Inventory selected exactly those five. All native generations are
`2026-11-02--18-26-56`; generation JSON, symlinks and registered output/NARs agree.
Actual mx2 output:
`/nix/store/r3y0rddwn8mkpvbdd7wyymsfzgdn3vz8-nixos-system-mx2-26.05.20261026.718f670`.
These are built outputs, not deployed profiles.

[Metadata remediation](monitor-metadata-remediation.md) resolves the difference
from earlier unbuilt standalone predictions: absolute-path flake self has no Git
revision and omits configuration-info, while native confctl uses clean Git `.#`
and embeds it. All five actual outputs report final head `1e3afc47`,
`revisionDirty=false`, schema 1, and locked input roles. Native source content
matches HEAD. No source/argument/input mismatch remains and no further build is
needed for this evidence reconciliation.

Complete graph: final lock blob `ec3d5aea9a7e55e69778e3ae4136cf2b3bb84e86`,
SHA-256 `505f6c89e18972827beecc29a0c7c85e1df2576ed4074205501167a3dd6f326a`.
Exact graph remains recoverable from final HEAD's `flake.lock`.

## Reviews, owners and retained evidence

Architect0 owned [design](design.md). Implementer1 owned the bounded
[primary baseline](primary-baseline.md) and
[DNS reconciliation](internal-dns-reconciliation.md); implementer0 owned shared
configuration, tests, docs, quick checks, commits and follow-up diagnosis/fixes.
Repository/Git writes were serialized. All packages are accepted and complete;
no new member work remains assigned. Lead owns this handoff and approval-bound
next steps.

Retained reviewer0, saved Sol/xhigh/read_only, independently completed
[full review](verification-review.md) and
[targeted metadata review](monitor-review.md). R1 IPv6 negative coverage and R2
queue-bound temporary response checks are fixed. Native type/address/reboot/reply
format corrections were directly inspected under the narrow-fix rule; no checks
were suppressed or production policy weakened. No unresolved finding remains.
[Implementation receipt](verification-implementation.md) and individual
remediation/run records retain the exact reviewed ranges, failed attempts and
accepted fixes. Their earlier active/pending statuses are historical and are
superseded by this state and the final results.

The fresh utility could not pass readiness before executing checks; the documented
parent-monitoring fallback ran the actual batches. No owned command, VM,
machine/repository claim or uncertain production operation remains. Owned native
quick-check directories and standalone scratch file were removed by their owner;
source, branches, generations, evidence and the session remain retained.

## Remaining live rollout gates

The actual Debian 13 primary is outside this repository. Strict administrative
SSH access was unavailable; the bounded protocol baseline observed Postfix,
100 MiB SIZE and self-signed STARTTLS. No real MAIL/RCPT/DATA/AUTH was sent.
Recipient/trust/filter policy equivalence remains unknown.

Before replacing CentOS, verify actual container/host placement, address ownership,
resolver propagation, both address families, and candidate delivery/acceptance by
the real primary using agreed test recipients. Resolve inbound certificate and
recipient/backscatter policy and the absent-milter scanning behavior. Keep old
and new queues independent; retain and drain accepted NixOS mail even if ingress
is rolled back. No CentOS spool/state conversion is implemented or certified.

The internal DNS correction is source only; it preserves unrelated split-DNS
records and the mail alias. Public DNS remains the operator-designated authority.
The actual monitor endpoint is `mx2.vpsfree.cz:9100`; service metadata address
`37.205.11.114` is separate. Live DNS/exporter reachability must be verified during
an approved rollout.

Repeatable operations are documented in
[project mx2 guide](../../worktrees/2026-11-01-mx2-nixos-migration/vpsfree-cz-configuration/docs/operations/mx2.md),
linked from the project README. Reusable fixture/exporter lessons are in workspace
notes. Next step is controlled staging and its approval/access preparation;
merge, deployment and lifecycle actions need their own explicit direction.

[Stable session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-01-mx2-nixos-migration/).
