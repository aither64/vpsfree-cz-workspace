# Nov5 public mx2 source preparation

Source package complete; independent review and native builds remain lead-owned.
No Nov5 remote access, activation, certificate issuance, IP transfer or mail was
performed by this package. Actual deployed source remains084488.

## Exact sources and inputs

- Final feature: `b120342c4517b6faa1a519913ab92acafbc506f3`.
- TLS bootstrap: `27fcf245fdfa3b1bff78815481d9bb954d915146`, preserved and
  published as `2026-11-01-mx2-nixos-migration-tls-bootstrap`.
- Deployed ancestor: `0844881779d62d9a6a86d2bacd61d21565b33932`, preserved and
  published as `2026-11-01-mx2-nixos-migration-deployed-staging`.
- Existing base remains `c4107822060e9e34b24a83950d618c9f28a7722b`.
  Fresh origin/master is `f4069909b55fbed907cb658f350ec6a59f97e05a`.
  Its selected vpsadminosOsStaging revision differs; the lead explicitly retained
  the deployed inputs rather than rebasing this service-only package.
- Entire lock graph and lock bytes equal084488. Lock SHA256:
  `507e781c2fa52da5a389e6eab824efe68baa72b1727de0fc162ea0a5e6b4c098`.
  nixpkgsStable remains718f670e845328e9c2cecdd832835712b2cbd065;
  vpsadminosOsStaging remainsb45b27b4330a08d85f413999e4bf66ba4503eee1;
  confctl remains7bee58a52372b95c2198ce3f2a719807a3c2c66b.

Full source/input graphs: [bootstrap](public-bootstrap-input-graph.json),
[final](public-final-input-graph.json), and deployed
[084488](staging-input-graph.json). Normal Git-self metadata reports both new
sources clean. Per-machine role paths/revisions are in
[public-final-system-table.json](public-final-system-table.json).

- bootstrap source: `/nix/store/1yn6aqmg9w476gnsd1dgdcll1gk32cq9-source`, NAR `sha256-Q7+YuPOTEPNjPU4l/Aul8gTTaHD/xCyKvCWb6HhyNew=`.
- final source: `/nix/store/ncip0nmlbj47222zxyd3in71rc52y008-source`, NAR `sha256-i827HUjux+9Tji9iF7t5LY587GEEnY2d/ImH7UHapxY=`.

## Generated quick checks

PASS parse, nixfmt, whitespace and normal Overcommit pre-commit/commit-msg hooks
for both commits. Commit-msg TextWidth produced warnings only; every line meets
repository80-column policy. Final source worktree is clean. Only assigned host
config/module and existing operations paragraphs changed:42 insertions/13 deletions
relative to084488. No lock/shared mail/test/data edit.

[public-generated-assertions.json](public-generated-assertions.json), with raw
[bootstrap](public-bootstrap-generated.json) and [final](public-final-generated.json)
proof, validates both committed native installables:

- FQDN and key.pem then fullchain.pem; inbound `may`, outbound policy unchanged.
- Postfix requires/after only native local acme-mx2.vpsfree.cz.service, which
  generates provisional files. Native order/renew listens HTTP80; daily timer
  invokes it and the postrun reloads Postfix. Group postfix, base directory750,
  UMask0027, and renewal chmod/chown preserve restricted key access.
- Bootstrap general ports22/80 for both families; exact172.16.106.40/32 TCP25
  accept before final refusal. Final general22/25/80 and no temporary rule.
- Both retain exporter9100 rules only from172.16.4.10 and172.16.4.18; exporter
  and syslog units present. No general9100 or auto-upgrade unit.
- Deployed root authorized_keys are byte-identical, retaining approved aitherdev.
  Postgrey and resolver units are identical. Generated main.cf differs only at
  myhostname/smtpd_tls_chain_files/smtpd_tls_security_level; transport is identical.
  ID27627, private management172.19.9.22, stateVersion25.05 remain unchanged.

The existing operations page now describes native TLS/bootstrap/renewal and keeps
backscatter and absent-milter limitations explicit. Recipient sync is follow-up.
Private activation is not requested: public HTTP80 must route here before the
lead switches bootstrap; verify a trusted certificate before final public SMTP.

## Evaluated identities, not built outputs

All below are instantiated native flake derivations and their expected outputs.
Neither new candidate generation nor changed consumer has been realized here.

| Candidate | Derivation | Expected output |
| --- | --- | --- |
| bootstrap | `/nix/store/7gfx37scwxp2azgxhxlm1cz6sgb8dfm2-nixos-system-mx2-26.05.20261026.718f670.drv` | `/nix/store/yyq4710fi3nz3mxb60b51z8q04mqkki7-nixos-system-mx2-26.05.20261026.718f670` |
| final | `/nix/store/6vi1hxiz36nfl5iikaa3h9qvwx0l5rk3-nixos-system-mx2-26.05.20261026.718f670.drv` | `/nix/store/9ywq4mzx32rmplnn8nyc7hpql8vjf3sa-nixos-system-mx2-26.05.20261026.718f670` |

| Changed consumer | Derivation | Expected output |
| --- | --- | --- |
| prg/int.mon1 | `/nix/store/0fis1s2kahllnif5yy7iqb84lf7qf1np-nixos-system-mon1-26.05.20261026.718f670.drv` | `/nix/store/dvcqhn5pbr67nkykqbbdjy0wjgplizfr-nixos-system-mon1-26.05.20261026.718f670` |
| prg/int.mon2 | `/nix/store/rkq17aadwhrik6dgk3qbwx3073n5gzbw-nixos-system-mon2-26.05.20261026.718f670.drv` | `/nix/store/xrybmyql7b7c5hnf6mccwx6ppxrnf3mj-nixos-system-mon2-26.05.20261026.718f670` |
| prg/int.alerts1 | `/nix/store/igwqvfkva69avl3ivyxbpg9m82s75nxn-nixos-system-alerts1-26.05.20261026.718f670.drv` | `/nix/store/1i4kib9vpgvd8cp2piby5vfxmmffw9jz-nixos-system-alerts1-26.05.20261026.718f670` |
| prg/int.alerts2 | `/nix/store/dv15i6flvsnlmkpz9xqv9ik1aryqqdm0-nixos-system-alerts2-26.05.20261026.718f670.drv` | `/nix/store/vx92wis1rda75a36qzvvbf2f23g8821b-nixos-system-alerts2-26.05.20261026.718f670` |

[public-consumer-comparison.json](public-consumer-comparison.json) and
[public-consumer-policy-comparison.json](public-consumer-policy-comparison.json)
prove monitors add only mx2 infra target`mx2.vpsfree.cz:9100` and ping target;
alerters add only the mx2 container-inhibit entry. `monitoring.target=null` makes
this an FQDN endpoint; metadata37.205.11.114 is distinct. Both internal DNS systems
change only source-revision receipt, with identical otheretc/unit dependencies.
Their new roots/expected outputs are in the system table; they are not built and
require no behavior-driven rebuild for this package. Logging is sender-local;
no shared collector or DNS source changed.

The exact five-target native inventory passed:
[public-build-inventory.txt](public-build-inventory.txt).

```sh
nix develop --no-write-lock-file -c confctl build --yes 'cz.vpsfree/containers/{mx2,prg/int.mon1,prg/int.mon2,prg/int.alerts1,prg/int.alerts2}'
```

Bootstrap additionally needs only its mx2 build. Pinned confctl has no source-ref
build flag: NixFlake#build_attributes uses relative .#confctl.build.<key>.toplevel,
with ConfDir=CWD realpath. After review, serialize ordinary checkouts in the owned
worktree: exact bootstrap branch/build mx2; capture its returned native generation
and generation.json+toplevel/roles; return exact final branch/build five. Assert
heads before launching each. Generation::Build#save retains separate dated
metadata/GC roots; build does not prune earlier generations. Flake mode explicitly
skips swpins autoupdate. Capture both exact generations; cutover must select their
literal `--generation` values, never implicit latest. No new launcher is needed.

## VM reuse qualification and hashes

[public-vm-reuse.json](public-vm-reuse.json) proves bootstrap and final roots equal
the historical passed `/nix/store/8pan3ddqairw3js87iaysvjqwzalxgls-vm-test-run-mx2.drv`
root from the complete4038-node consumed graph. Its unchanged immutable input
references bind that same graph; this is derivation/input equality, not tree-only
reuse. Historical runtime pass/output NAR were verified; later output availability
was absent. No current-existence claim and no new VM run.

Hash boundaries differ: compact sorted JSON without trailing newline of the
native singleton version4 envelope `{derivations:{basename:root},version:4}`
recomputes exact historical
`d1e739bbeefe29f257dbb3a5e27558bb2183fe48314d324fa59a7ee661191255`.
Hashing only its nested derivations dictionary givesd917587b…; hashing only the
root value gives962ecf7f…. These hashes cover different objects and are not
presented as equal. Entire prior recursive graph canonical hash remainse366b148…
(full values and algorithms in JSON). No new graph batch was needed.

## Publication and history

Exact-lease feature push succeeded from084488; bootstrap and deployed refs are
published. Fresh SSH proof: [public-remote-proof.txt](public-remote-proof.txt).
Comparison captured c410..b120. GitHub current branch workflow list is empty
([public-ci.json](public-ci.json)); no superseded active run to cancel.

Complete final series above c410:548514a9 host/shared policy, e7cd91d8 internalDNS,
08448817 isolated tests/docs, b120342c public service. The first three commits are
unchanged deployed lineage. Bootstrap27fc is a sibling ofb120 above084488; their
only source difference is the SMTP ingress gate. Bootstrap is an intentional
cutover snapshot, not an obsolete fixup in final history. No migrations, no own
input-update stream, and no intermediate lock refresh. Earlier source/import/
reviewed/runtime refs remain intact. Independent reviewer covers whole history
and both source IDs; long builds follow the lead's review acceptance.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-01-mx2-nixos-migration/)

## Bootstrap actual native build verified

Utility build passed once at clean27fcf245 (exit0/about65s; launch timestamp
approximate). Exact generation `2026-11-05--13-04-34` is retained in
[public-built-systems.json](public-built-systems.json), including original native
generation JSON+SHA, toplevel/role links, registered deriver/NAR, clean source and
input info. Actual output `/nix/store/yyq4710fi3nz3mxb60b51z8q04mqkki7-nixos-system-mx2-26.05.20261026.718f670` matches the prepared identity;
NAR `sha256-2u0CGS+pPWAh7bhDKpoZVFhkwddwHibQEN130WmsljA=`. Source and selected role NARs also match.
The separately reported native logfile is absent;
[public-bootstrap-build.log](public-bootstrap-build.log) retains the available
utility transcript. No fabricated log, rerun or realization during validation.
Baseline VM reuse covers shared mail policy, not host ACME; actual certificate
issuance/renewal remains host cutover acceptance. Final system outputs remain
unbuilt until the next lead-run batch.

## Final actual native build verified

Parent fallback build passed once at cleanb120342c, exit0/162.881s. All five
returned literal generation `2026-11-05--13-11-54`.
[public-built-systems.json](public-built-systems.json) now captures all five
original generation JSONs/SHA, links, registered output derivers/NARs, clean
configuration-info and matching generation/output inputs-info. Every actual
identity matches the prepared table; complete source/role NARs match the frozen
graph. Complete process output is [public-final-build.log](public-final-build.log),
with authoritative [result](public-final-build-result.json).
Bootstrap generation2026-11-05--13-04-34, original JSON/links and exactyyq471 output
registration/NAR were rechecked intact after final build. Both mx2 literal
generations are ready for copy-only: bootstrap2026-11-05--13-04-34 and
final2026-11-05--13-11-54. No mismatch, rebuild, guest operation or activation.
The separately reported final native logfile is also absent at validation; the
complete parent stdout/stderr log is retained and authoritative with its exit
capture. No missing native logfile was reconstructed.

## Copy-only and guest verification complete

Lead copy-only succeeded for bootstrap2026-11-05--13-04-34 (exit0/27.718s) and
final2026-11-05--13-11-54 (exit0/14.088s), with no activation/profile/health driver.
See [public-copy-result.json](public-copy-result.json) and its two retained logs.
One strict read-only SSH call at2026-11-05T12:22:35Z finished exit0/0.693s
(first output0.318s); no retry or active command.
[public-copy-guest-verification.json](public-copy-guest-verification.json) captures
complete stdout/stderr and validation: both remote toplevels have exact built
derivers/NARs, clean27fc/b120 source info and frozen role-input metadata.

Current/profile/booted remain staging4pc5/clean084488. Private172.19.9.22 is
configured; neither37.205.11.114 nor2a03:3b40:100::1:95 is present. System is running;
Postfix/Postgrey/sshd active/running, firewall active/exited, all Result=success;
queue count0. Native mx2 ACME base/order-renew/timer units are not-found/inactive
with no start timestamps. Preparation has not activated the public profile.

Qualification: the additional role-source registration query finds matching
nixpkgs source NAR, but vpsadminos sourcec24mbj… is absent remotely. Both embedded
role revisions match; complete build-source/role NAR graphs remain verified
locally. No claim that all build-time sources were copied, no retry/realization.

Owner preparation package is closed, with session and held machine claim left
active. Lead owns remaining operator handover: approved public IP transfer, then
literal bootstrap generation2026-11-05--13-04-34 switch retaining SMTP source gate,
verify trusted HTTP-01 certificate, then literal final2026-11-05--13-11-54 switch.
No guest mutation, SMTP, monitor activation, merge, pruning or cleanup was done.

## Nov6 transferred-address activation preflight

User-reported public transfer was observed in the single strict read-only SSH
check2026-11-06T20:28:10Z: private172.19.9.22/32 plus37.205.11.114/32 and
2a03:3b40:100::1:95/128 on venet0, with both default routes. Current/profile/booted
remain4pc5/clean084488, profile system-4-link; rollback executables retained.
Both copied generation outputs/NARs/clean source/role metadata still match.
System/services healthy, queue0, no jobs or ACME activation. Local finalb120 and
lock are clean/frozen; both literal generations retained. SSH exit0/0.610s,
first output0.357s. [Preflight JSON](public-activation-preflight.json) retains facts.
Candidate own-hostname NSS uses its native127.0.0.2 alias; direct local1.1.1.1
DNS gives expected public A/AAAA (NOERROR, TTL3600). Primary guest resolution is
correct in both families. Old VPS queue is unknown; no old-host probe or empty
queue assumption. Lead owns the now-released bootstrap/final switches; no owner
mutation or reboot.

## Nov6 bootstrap activation verified

After lead's settled ordinary switch, strict read-only check20:32:16Z confirms
current/profileyyq471/clean27fc, profile system-5-link; BOOTED remains4pc5. Six
mail/SSH/firewall/exporter/syslog units healthy, systemrunning, no jobs, queue0.
ExactIPv4 source-only SMTP gate remains; generalTCP25 closed bothfamilies,
22/80 open and exporter ACLs unchanged. Native ACME bootstrap/order succeeded,
renewal timer active/waiting, acme-successpresent.

Actual Let's EncryptYE2 certificate SANmx2.vpsfree.cz is valid Nov6 19:31:56UTC
through Feb4 2027 19:31:55UTC. Guest chain/name verification passes; key/fullchain
metadata isacme:postfix0640 (key contents never read). Allowedsource172.16.106.40
STARTTLS to172.19.9.22 at20:32:47Z verifies default trust/hostname and serves exact
leafSHA256c706203230917a7473dca88dcb7b4878692161f6ec5d19e26a3ae168d72341b1,
matching the installed certificate. TLS1.3, FQDN andSIZE104857600 confirmed.
Only EHLO/STARTTLS/EHLO/QUIT; no MAIL/RCPT/DATA.
[Bootstrap verification](public-bootstrap-activation-verification.json) retains
full command evidence and public certificate details. No ACME retry/forced
issuance, service mutation, source change or reboot by owner. Lead's final
activation is separate; no guest probe while it is active.

## Nov6 final activation: healthy, external IPv6 observation pending

Final guest check20:36:28Z (SSHexit0/0.712s) proves current/profile9ywq4/cleanb120,
profile system-6-link, BOOTED4pc5 and uptime185771s. Six services healthy, system
running, nojobs, queue0; ports22/25/80 open bothfamilies, temporary SMTP gate
removed, exporter ACLs retained. Same trusted certificate remains installed.
PublicIPv4 STARTTLS/defaulttrust/hostname and exactsame leaf pass; unrelated RCPT
gets5545.7.1Relayaccessdenied, thenRSET/QUIT. No DATA/message was sent.
Public A/AAAA and both PTRs match mx2.vpsfree.cz. Candidate primary greeting/
EHLO/QUIT succeeds over bothfamilies, with route+ESTAB source37.205.11.114 and
2a03:3b40:100::1:95; no primary recipient/auth/delivery or externalNAT proof is
claimed. Four monitor/alert consumer systems remain built only, not activated.

Required remaining observation: workspace IPv6 connect fails before reaching
server witherrno101Networkisunreachable. Candidate IPv6 egress success is not
external IPv6 ingress proof. No blind retry or self-connect substitution.
[Final guest evidence](public-final-activation-verification.json) and
[public checks](public-final-public-checks.json) preserve exact results/limitations.
Lead is selecting any existing authorized dualstack observation source; owner
performs only bounded local discovery meanwhile. No source/build/guest mutation.

Bounded local observer discovery found no usable authorized external endpoint:
effective Nix builders empty, ordinary user SSH config absent, repository scoped
builder declarations absent; system SSH has only literal.host andmachine/.host
aliases. No remote host was probed and no credentials/key material inspected.
External incoming IPv6 TLS/relay denial remains an explicit verification gap;
lead owns any observation-source selection. All completed facts remain intact.

## User external IPv6 TLS proof and reply-aware relay check

User's external host connected to exact2a03:3b40:100::1:95. Supplied OpenSSL output
under verify_hostname/verify_return_error verifies ISRG RootX2 → RootYE →
Let's EncryptYE2 → CNmx2.vpsfree.cz, each verifyreturn1. This closes external
IPv6 connectivity/STARTTLS/name/trust coverage. Its later5545.5.0SMTPprotocol
synchronization followed our unsynchronized piped commands; it is not recorded
as a server regression or as relay denial.

A corrected reply-aware Python stdlib snippet was delivered directly to lead.
It connects the literal target, asserts peerIP, then sets smtplib._host to
mx2.vpsfree.cz before default-trust STARTTLS; every SMTP method waits for its
reply. EHLO/STARTTLS/EHLO/MAILpodpora/unrelatedRCPT/RSET/QUIT, noDATA. One bounded
execution of this exact harness against publicIPv4 passed exit0 (~0.227s),
trustedTLS1.3/samec706…leaf and exact5545.7.1Relayaccessdenied. No candidateSSH,
newmessage/source/deploy/build/install. Remaining check is only externalIPv6
relay denial using the corrected command, not IPv6 connectivity/certificate.

## Public-cutover acceptance closed: user confirms IPv6 relay denial

After running the corrected reply-aware client against the exact public IPv6
address, the user supplied:

```text
554 5.7.1 <mx2-check@example.org>: Relay access denied
```

Together with their earlier external IPv6 TLS chain/hostname verification, this
closes the outstanding IPv6 SMTP/TLS/relay observation. It is user-supplied
evidence; the source host and execution timestamp were not supplied. The corrected
client uses the exact IPv6 target and verified mx2.vpsfree.cz TLS name, then waits
for each SMTP reply. It sends no DATA. No additional message or server change.

Lead accepts the completed public cutover at final b120342c/system 9ywq4. The
historical unavailable-workspace-IPv6 result and first command's synchronization
error remain preserved above, superseded by the user observation. Both public
families, actual source/profile/services, DNS/PTR, certificate/renewal and primary
connection paths now have the required evidence. The last observed queue was
empty. Monitoring consumers remain built only; configuration/master integration,
claim release and old-VPS retirement remain separate obligations and authorities.
