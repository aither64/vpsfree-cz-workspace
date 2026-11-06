# mx2 verification results

## Outcome

Automated isolated mail verification passed. The final candidate and all four
consumers of its internal DNS source change built successfully. No production
mail, DNS reload, deployment or default integration occurred. This is readiness
for controlled staging, not certification of the CentOS replacement in production.

## Final source and review

Repository `vpsfreecz/vpsfree-cz-configuration`, published branch
`2026-11-01-mx2-nixos-migration`, final head
`1e3afc478fb72b54a25a0147910463f060fee88f`, tree
`77d73449040aba400215ca81843c3d6a2173593c`, base
`c040c14cdbacc07998700b524996a89306188d7f`. Fresh remote checks confirm both;
clean worktree, all source committed. Three coherent commits: final host/shared
mail policy/exporter metadata, independent internal DNS correction, tests/docs.
No migrations, input changes or superseded update streams. Original40411,
reviewede4 and runtime8d refs retained; no nonancestor literal-merge claim.

Independent full [review](verification-review.md) plus recorded narrow test
fixes and targeted [metadata review](monitor-review.md) are complete. No unresolved
findings. Actual runner failures were diagnosed and fixed without skipping
assertions; their separate receipts/logs remain. No source changes after final
review/build source freeze. Readiness history and full input bindings are in
[implementation](verification-implementation.md) and
[metadata remediation](monitor-metadata-remediation.md).

## Mail suite

[Batch6](verification-run-6.md) passed full three-VM suite in227.03s
(script202.93s), using actual SMTP, Postfix queues and a controlled primary:

- Exact intended-domain relay and unrelated/subdomain denial from IPv4/IPv6.
- Envelope, Message-ID, subject and body integrity through forwarding.
- Greylisting/retry/state persistence, DNSBL rejection, policy-service outage,
  missing-milter fail-open and advertised message-size boundary.
- Accepted mail surviving Postfix restart and same-disk VM reboot, then delivery
  and queue drain when the primary returns.
- Controlled primary450 deferral/recovery,550 rejection/DSN, self-signed outbound
  TLS and plaintext fallback when primary STARTTLS is absent.

The candidate shares production configs/mx2.nix; fixture exceptions are explicit
network/resolver settings and timing values. All three guests restrict network
access, no default route/forwarded ports, nonforwarding local DNS. No production
address or real recipient was used. Native cleanup stopped all guests.

The final metadata-only successor resolves the identical successful check drv
`/nix/store/8pan3ddqairw3js87iaysvjqwzalxgls-vm-test-run-mx2.drv` with unchanged
complete input graph. Reuse was independently accepted; no unnecessary VM rerun.
Canonical derivation JSON SHA256
`d1e739bbeefe29f257dbb3a5e27558bb2183fe48314d324fa59a7ee661191255`.
Expected check output was realized/NAR-verified immediately after pass, but later
became unavailable locally (unknown cause, no session-owned store deletion).
Current availability is not claimed; durable pass log/status and immutable exact
derivation/input evidence remain. This is distinct from a test failure.

## Final actual native system builds

[Batch7](verification-run-7.md) native five-target union completed exit0 in
161.55s. Native generation
`2026-11-02--18-26-56` for every target. Actual generation JSON, adjacent symlinks
and registered output/NARs were checked after success. These are build outputs,
not deployed profiles. Actual paths below are authoritative; standalone pure
flake evaluation paths are separately recorded evaluation artifacts.

| Exact confctl target | Realized output |
| --- | --- |
| `cz.vpsfree/containers/mx2` | `/nix/store/r3y0rddwn8mkpvbdd7wyymsfzgdn3vz8-nixos-system-mx2-26.05.20261026.718f670` |
| `cz.vpsfree/containers/brq/int.ns1` | `/nix/store/ff6c4raplcz51h867vlap3j3dlx0qkvg-nixos-system-ns1-26.05.20261026.718f670` |
| `cz.vpsfree/containers/prg/int.ns1` | `/nix/store/44sgccyp9sc8h2dh3glpnivh8cj2bcr4-nixos-system-ns1-26.05.20261026.718f670` |
| `cz.vpsfree/containers/prg/int.mon1` | `/nix/store/9dz8gzhvz03kva8647d2ph928i5w1v8b-nixos-system-mon1-26.05.20261026.718f670` |
| `cz.vpsfree/containers/prg/int.mon2` | `/nix/store/vfy97r42hjmdc9wpp5qkq9pnmbq6nvl6-nixos-system-mon2-26.05.20261026.718f670` |

Full native identities and generation JSON bindings:

### cz.vpsfree/containers/mx2

- Derivation: `/nix/store/4wz0nkyqx44hiilgv4q6a1fm8c6mrrx1-nixos-system-mx2-26.05.20261026.718f670.drv`.
- Output NAR: `sha256-Sb7O6rudD0FtfKvrCkWECVkiOueB3EnxltrESe+IJ4s=`.
- Generation JSON SHA256: `c2d64d392e27e541ae8551bd0e316526b13e1d9d323afb1dfed9befe77c74470`.

### cz.vpsfree/containers/brq/int.ns1

- Derivation: `/nix/store/1qqsyshbla0bbplmq3n4js9ngqmcdwk6-nixos-system-ns1-26.05.20261026.718f670.drv`.
- Output NAR: `sha256-c5cTcHWfnelMHBn+w7ra9fjl6zzhK6560ba1/QywneE=`.
- Generation JSON SHA256: `0d4a4927170cf1103125abbec9111e49440844308d1f89e8037d114a9d380eb7`.

### cz.vpsfree/containers/prg/int.ns1

- Derivation: `/nix/store/y70la10nsgcqgiynfk09c8c07y02q0xy-nixos-system-ns1-26.05.20261026.718f670.drv`.
- Output NAR: `sha256-JoAtSNXjXfzLR4+0Wvd/ERKNZgLwbh7bPHke/ATg9E8=`.
- Generation JSON SHA256: `2812a3836973740f77aec45f54c97d542b1a601d393631c1a61fcca1318a2fb2`.

### cz.vpsfree/containers/prg/int.mon1

- Derivation: `/nix/store/6q29p6sl3gwgfl5ngp8rh6pg6v8z3lsh-nixos-system-mon1-26.05.20261026.718f670.drv`.
- Output NAR: `sha256-t8WXDIQJToCoWkcjJwdHdNzAVTu1Ny23W1LYqtK+rVI=`.
- Generation JSON SHA256: `71823f1494115ee88da819eba57b3f519b4e87ca1898656c0e6051fdd47d912f`.

### cz.vpsfree/containers/prg/int.mon2

- Derivation: `/nix/store/mwrnp6ci89q0n1xzw1wnpgvk65qjbc71-nixos-system-mon2-26.05.20261026.718f670.drv`.
- Output NAR: `sha256-7qAjKVrOikr78nLQxtb3ypZKYvyH1vDjCIGCS9oxZSo=`.
- Generation JSON SHA256: `547a56a32ff455658e863f59d888114fd41df017f9f13eab399428478064304c`.

Native source/input-context reconciliation is recorded in the metadata receipt.
The earlier standalone absolute-path flake evaluation omits configuration-info
because its self has no Git revision. Native confctl builds from Git `.#` and
embeds it. All five actual outputs identify final head `1e3afc47`,
`revisionDirty=false`, schema 1, and the locked input roles; native source content
matches HEAD. This accounts for the different derivations without a stale source
or input mismatch. The full source lock graph remains recoverable with
`git show 1e3afc478fb72b54a25a0147910463f060fee88f:flake.lock`.
Lock blob `ec3d5aea9a7e55e69778e3ae4136cf2b3bb84e86`, SHA256
`505f6c89e18972827beecc29a0c7c85e1df2576ed4074205501167a3dd6f326a`.
No expected pure-evaluation path is relabeled as a successful native output.

## Production gates

The actual Debian13 primary's recipient/trust/filter policy remains unavailable
through administrative access. Protocol-only baseline observed Postfix,
self-signed STARTTLS and100MiB; no real MAIL/RCPT/DATA/AUTH was sent.
The candidate still needs actual container/host/address/primary acceptance and
propagated DNS checks in an approved staging rollout. Inbound certificate,
recipient/backscatter and absent-milter scanning policies need resolution before
cutover. Preserve independent old/new queues; drain accepted mail on rollback.
No CentOS state conversion or actual production recovery was tested.

Source internal DNS matches user-designated public mail records; unrelated
internal records/mail alias preserved, no internalorg zone invented. BIND parser
checks covered allfour template substitutions. Corrected source is not live DNS.
Exporter metadata now matches existing enabled9100 service; the consumer target
is mx2.vpsfree.cz:9100, not a literal metadata IP.

No test VM, build command, machine/repository claim or pending deployment remains.
Owned quickcheck scratch was removed and accounted; native generations, source,
branches and this active session remain retained. Repeatable instructions are in
project docs/operations/mx2.md. [Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-01-mx2-nixos-migration/).
