# Automated mx2 verification implementation

Batch 6 passed the complete VM check and actual mx2 plus both DNS-server builds
at preserved predecessor `8d4e03d5`. mon1 then exposed missing exporter metadata
on the new mx2 host. The current [metadata correction](monitor-metadata-remediation.md)
adds the standard declaration; both complete monitor configurations now evaluate.
The actual target is `mx2.vpsfree.cz:9100`, separate from its metadata service
address. Targeted metadata review is clear; native exact-five-system
batch 7 passed at the final head (exit 0, 161.55s). The VM check has the exact passed derivation/input identity and can reuse
that result; the receipt preserves earlier NAR verification and later unavailable
artifact status separately. Historical failures and their bounded corrections
remain in their original reports. No deployment or integration has occurred. Final publication/comparison proof
and accepted reuse qualifications are in the metadata receipt; the authoritative native generation/NAR table is retained in the metadata
receipt. Earlier direct absolute-path predictions are marked unbuilt and their
source-context difference is reconciled there.

## Review candidate and history

Repository: `git@github.com:vpsfreecz/vpsfree-cz-configuration.git`.
Owned branch: `2026-11-01-mx2-nixos-migration`.
Base: `c040c14cdbacc07998700b524996a89306188d7f`, freshly fetched and unchanged.
Final candidate: `1e3afc478fb72b54a25a0147910463f060fee88f`.
Tree: `77d73449040aba400215ca81843c3d6a2173593c`.

Published with an exact `--force-with-lease` against independently reviewed
remote head `8d4e03d53699d80f46030b0ee6eb213151b8ae30`, using the repository
shell/hooks. The earlier consolidation used the exact reviewed-import head lease.
Fresh `git ls-remote` confirms the final feature head and unchanged default above.
Owned worktree is clean. CI inspection returned no runs on this branch, so no
superseded run needed cancellation. Final native repository comparison captured
the exact base/head pair.

The complete final series contains three logical commits:

1. `9c6e36135192f65baed975e3b127160f068e0b0d`, `cluster: configure mx2 backup mail relay`.
   Imported host and metadata, final shared mail policy, exact relay-domain
   authorization, parent-domain exclusion, TCP25 and 100 MiB limit.
2. `a5848319ae19d1bcd348ab3837683dec71c90e01`,
   `internal-dns: align mail records with public DNS`.
3. `1e3afc478fb72b54a25a0147910463f060fee88f`,
   `tests: verify mx2 relay and queue behavior in isolated VMs`.

Complete final diff: 13 paths, 733 additions and four deletions. The test uses
one conventional NixOS three-VM check, a Python driver and a small SMTP client;
there is no new framework, input update, CI workflow or second repository.
There are no database/schema migrations or dependency-pin update streams.
Postfix/Postgrey persistent paths and container stateVersion remain unchanged.

Explicit retained refs preserve prior evidence:

- `2026-11-01-mx2-nixos-migration-source` at original
  `40411d67ee97cea800bcccd89b0473432b4502c4`.
- `2026-11-01-mx2-nixos-migration-reviewed-import` at reviewed/built
  `e4c1ac0c5ae7426fb019b79ba936b30ce63e6e6c`.
- `2026-11-01-mx2-nixos-migration-verified-runtime` at passed VM/three-system
  predecessor `8d4e03d53699d80f46030b0ee6eb213151b8ae30`.

The separate source checkout remains untouched. See the original
[import provenance](import-rebase.md) for historical base/head and identical
source before/after snapshots. The reviewed import is not an ancestor of the
consolidated candidate; its original patch was refreshed with substantive policy
corrections and requires the new review/build. No deployed lineage is claimed.

Implementer1 released source/Git ownership after DNS commit
`655851e595c57efbedb45588f0cca28509f00907`; implementer0 preserved that logical
change during consolidation. Old/new DNS patch IDs both equal
`87bf97c34572a6e79d3635773555be5e77ca9fd1`. Its independent checks are in
[DNS reconciliation](internal-dns-reconciliation.md).

The complete pre-consolidation working head
`13e0ad185a7254ca3814167d28832d6276b107e0` has exactly the same tree as the
independently reviewed pre-remediation head
`f3789413a53bcd12e2352940a0ec3e88009c5d9f`. The superseded host-policy fixup was folded into the imported host;
DNS and tests/docs remain distinct. Both reviewed-import evolution and full
consolidation comparisons are retained in
[verification range-diff](verification-range-diff.md). No obsolete policy-fix
commit remains in the final series. Narrow review fixes are recorded in
[remediation evidence](verification-remediation.md) and its linked source delta;
the original [independent review](verification-review.md) retains its exact range.

## Shared production policy and fixture fidelity

Production host and test MX both import `configs/mx2.nix`. The only MX fixture
mail-setting overrides are the following. Production values below come from
the generated configuration and, where unset there, the pinned Postfix 3.11.7
`postconf -d` defaults. The full generated main.cf comparison independently
confirmed that these are the only differences (plus explicit fixture hostname).

| Postfix setting | Production | Fixture |
| --- | --- | --- |
| `minimal_backoff_time` | unset; default `300s` | `5s` |
| `maximal_backoff_time` | unset; default `4000s` | `10s` |
| `queue_run_delay` | unset; default `300s` | `5s` |
| `smtp_connect_timeout` | unset; default `30s` | `5s` |
| `smtpd_policy_service_timeout` | unset; default `100s` | `3s` |
| `smtpd_policy_service_try_limit` | unset; default `2` | `1` |
| `smtpd_policy_service_retry_delay` | unset; default `1s` | explicit `1s` (default-equivalent) |

`myhostname` is host-derived in production and explicitly `mx2.vpsfree.cz` in
the fixture. `services.postgrey.delay` is 300 seconds in production and two
seconds in the fixture. Interface addresses, node names and resolver plumbing
are fixture-specific. There is no candidate certificate override or scanning
service. The test keeps Postgrey's subnet/auto-whitelist semantics unchanged
and performs the first-seen assertions before normal delivery cases.

Independent generated-derivation comparison passed for:

- Identical transport text and destination `smtp:prasiatko-mail.vpsfree.cz`.
- All other main.cf settings, including exact relay domains, parent-domain
  exclusion, trust defaults, relay/recipient restrictions, both original DNSBLs,
  104857600-byte limit, localhost milter and failure action, inbound/outbound TLS,
  `/var/lib/postfix/queue` and `/var/lib/postfix/data`.
- Postgrey unit text identical after replacing only `--delay=300` with
  `--delay=2`: socket `/run/postgrey.sock`, mode 0777, DB `/var/postgrey`, owners,
  privacy, subnet and whitelist settings unchanged.
- TCP25 present in each generated enabled firewall configuration. Production
  also retains unrelated shared-profile firewall exceptions.

Disposable full comparison: `mail-fidelity-generated.json`; selected fixture
configuration: `fixture-mail-evaluated.json`. The durable conclusions and actual
override values are recorded above, so retention does not depend on raw JSON.

The primary and sender services are controlled fixtures: Postfix pipe capture
records envelope/content; primary has a runtime 4xx/5xx response map and a
self-signed test certificate. Local DNS answers the original transport/domain
and DNSBL names. Unrelated and arbitrary-subdomain denial cases explicitly
assert local A records, separately from the unknown-domain case. All VMs use
restricted networking, no default gateway/port forwarding and nonforwarding DNS;
runtime assertions verify resolver/routes. No production IP is bound.

## Quick checks and exact evaluated identities

Passed before review:

- Normal repository Nixfmt pre-commit and commit-msg hooks on source/tests
  commits and final host amendment. Advisory 72-column message warnings only;
  messages meet the required 80-column limit. No hook bypass.
- Nixfmt check and Nix parsing for all touched Nix files.
- Python compilation and pyflakes-F lint using the standard NixOS test machine
  hints. The test retains the upstream driver's runtime lint/type-check gates.
- Full final base-to-head `git diff --check`, clean worktree and consolidation
  tree equality; no lock change.
- Test and actual production toplevel derivation evaluation, repeated at the
  exact final committed head. The touched deprecated Postfix option is now
  `settings.main`; no rename warning remains.
- Generated production/fixture comparison above. Final fixture system
  derivation was re-evaluated at final head.

| Item | Derivation | Expected output |
| --- | --- | --- |
| Isolated check | `/nix/store/8pan3ddqairw3js87iaysvjqwzalxgls-vm-test-run-mx2.drv` | `/nix/store/jgq1lk68xjj40j2h4wnw403pc3nylni4-vm-test-run-mx2` |
| Production MX | `/nix/store/4wz0nkyqx44hiilgv4q6a1fm8c6mrrx1-nixos-system-mx2-26.05.20261026.718f670.drv` | `/nix/store/r3y0rddwn8mkpvbdd7wyymsfzgdn3vz8-nixos-system-mx2-26.05.20261026.718f670` |

The earlier fidelity snapshot retains its own fixture identity; the complete
current VM input graph is bound by the exact VM-check derivation above.
The production MX identity above is the actual native batch-7 build; the earlier
absolute-path evaluation identities are not the realized graph. The VM identity is bound to
the actual successful batch-6 run. Earlier registered/NAR-verified VM output is
currently unavailable, as qualified in the monitor metadata receipt. Implementer0
has not realized these new systems, launched a runtime rerun or contacted production.
The earlier imported configuration build is separate evidence and is not reused
as validation of this substantive successor.

Input graph is unchanged: final `flake.lock` blob
`ec3d5aea9a7e55e69778e3ae4136cf2b3bb84e86`, SHA-256
`505f6c89e18972827beecc29a0c7c85e1df2576ed4074205501167a3dd6f326a`.
The complete graph is recoverable with `git show
1e3afc478fb72b54a25a0147910463f060fee88f:flake.lock`, including all transitive
nodes/follows edges. Root test/dev packages use `nixpkgsStable`
`718f670e845328e9c2cecdd832835712b2cbd065`; production additionally selects
`vpsadminosOsStaging` `b45b27b4330a08d85f413999e4bf66ba4503eee1`. Confctl remains
`7bee58a52372b95c2198ce3f2a719807a3c2c66b`.

## Review and execution handoff

Lead owns independent final review and fresh policy utility execution after
review reconciliation. Exact commands, from the owned worktree at final head:

```sh
nix build -L .#checks.x86_64-linux.mx2
nix develop -c confctl build --yes cz.vpsfree/containers/mx2
```

Use the retained catalog's fresh Luna/low verification utility and full-access,
never-approval execution policy. Separate substitution/build preparation from
runtime (30-minute ceiling). Stop on network escape, unexpected kernel build,
repeated boot failure or the first assertion failure; preserve logs/state for
implementer diagnosis. No blind retry. The standard test driver owns VM shutdown.

Production acceptance still requires inbound certificates, agreed recipient
handling/backscatter policy, real-primary acceptance, container/network identity,
propagated DNS and queue-safe cutover/recovery. No deployment, primary changes,
real-recipient mail, default integration or session lifecycle action is performed.
