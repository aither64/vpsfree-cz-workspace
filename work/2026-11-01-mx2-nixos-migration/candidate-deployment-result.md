# Private mx2 deployment and live verification result

PASS: VPS **27627**, configured target `cz.vpsfree/containers/mx2`, private
`172.19.9.22`, runs reviewed source `0844881779d62d9a6a86d2bacd61d21565b33932`.
Final full health/drain sample: **2026-11-04T18:03:41+01:00**.
Source, build and isolated-test/review evidence remain in the existing receipts.

## Installed identity and inputs

Current, system profile and booted system all resolve to:

`/nix/store/4pc5mic0rp9h5qb2lhgmdh2x8z50pqd2-nixos-system-mx2-26.05.20261026.718f670`

Deriver: `/nix/store/bpyiq4bfdmd9anf96zqyg8kqmyd3d9b0-nixos-system-mx2-26.05.20261026.718f670.drv`.
System NAR: `sha256-dGOqT6fHxNlWSfrfMGRzPem0RqpuLSzHLoWJ/CG5cjg=`.
Installed configuration-info records exact084488 and `revisionDirty=false`.
Complete source: `/nix/store/vvbb8n2imsc3gssza91lszb5gss5mxyh-source`,
NAR `sha256-R2rH+/SVez0E8tLkdahFZwbZNkyccOVSpeBVNNLMhBQ=`.
Full graph: [staging-input-graph.json](staging-input-graph.json); lock SHA256
`507e781c2fa52da5a389e6eab824efe68baa72b1727de0fc162ea0a5e6b4c098`.

| Selected role | Revision | Source path |
| --- | --- | --- |
| nixpkgs | `718f670e845328e9c2cecdd832835712b2cbd065` | `/nix/store/z40fynbhnw0d06q05mw2mznn49h1y9pk-source` |
| vpsadminos | `b45b27b4330a08d85f413999e4bf66ba4503eee1` | `/nix/store/c24mbj25ajwn8zixx4hagr85i5kmqlmy-source` |

Full source/output/role NAR bindings: [staging-built-systems.json](staging-built-systems.json).
Reviewed range remains `c4107822060e9e34b24a83950d618c9f28a7722b..08448817`.
Local `2026-11-01-mx2-nixos-migration-deployed-staging` preserves exact084488.
Original source40411, reviewed-importe4c1, verified-runtime8d4e and reviewed-mail1e3a
refs remain as recorded. No history refresh, source/package/input change or new
build was needed for runtime recovery and live verification. Source was clean
after withdrawing the unnecessary DNS draft and remained unedited thereafter.

## Runtime health

System running; no pending jobs/failed units. Postfix, Postgrey, firewall, SSH,
logind, D-Bus and resolver active. Node exporter and rsyslog are not-found/inactive.
Strict pinned-key SSH works; approved key presence verified without key dumps.
Private IPv4 remains172.19.9.22/32, no old public address/globalIPv6/defaultIPv6
route. SMTP firewall permits only172.16.106.40/32; publicTCP22 remains.
StateVersion25.05 and persistent tank/ct/27627 ZFS are retained. Actual resolver
is solely1.1.1.1; primary A37.205.15.53 and AAAA2a03:3b40:fe:1c3::1 resolve.

User rebooted into4pc5 before verification; first strict postboot call completed
in0.60s, restoring normal session startup. Source identity alone had not proved
service readiness: initial live upgrade needed native D-Bus/interrupted-unit
recovery, and Postgrey required the separately authorized unused-state reset.

## Two authorized synthetic messages

Envelope sender and recipient for both: `podpora@vpsfree.cz`. Exactly **two**
payloads received final DATA250; no additional payload or deliberate DSN test.
Reserved unrelated-domain RCPT was rejected5545.7.1 Relay access denied without DATA.

| Test | Subject | Candidate queue | Primary queue |
| --- | --- | --- | --- |
| Normal (475 bytes) | [mx2 staging TEST 1/2] normal delivery | `791FC69382` | `55F35A7ED` |
| Outage (471 bytes) | [mx2 staging TEST 2/2] queue recovery | `D242768B88` | `C5F44F212` |

Normal Message-ID: `<mx2-normal-fc30fa23abdb4f9ca99237618a95a8a7@vpsfree.cz>`.
Outage Message-ID: `<mx2-outage-92a065c245204b8cbf63cbaf4e301928@vpsfree.cz>`.
Normal respected native300s greylisting, with one same-payload retry after305s
before DATA. The primary then temporarily greylisted its first delivery; the
same accepted queue entry was retried natively and handed off250, then removed.
Both final primary handoffs show DSN2.0.0/status=sent; candidate queue is **empty**.
User mailbox receipt remains for lead to confirm jointly; SMTP handoff is proven.

## Persistence and exact fault cleanup

Accepted outage ID `D242768B88`, exact envelope and full original
471-byte payload were verified before and after Postfix restart, then after one
candidate-only reboot. Postcat LF normalization preserved every original header
and body byte; client payload SHA256
`1267863676fd039c1cdeba1db55711929fddda0561c2264db2d7b3e6b5de1b7a`.
Boot ID changed `507276a8-af4c-4ff0-8769-d12f82669058`
to `ce6c77e2-986c-42ac-af10-b77d3c8ef5ff`; all three system paths stayed4pc5.

The persistent fault used the native `/usr/local/lib/systemd/system` load path,
with Postfix Requires/After dependency and no enable link. Exact primary-only
TCP25 reject rules covered both recorded A/AAAA addresses; IPv4 packet-counter
hits proved the exercised block. IPv6 transport was unavailable, not claimed tested.
One initial log-text assertion was corrected using this exact rule-counter proof.

Owned unit `mx2-verification-outage.service` SHA256
`2cd3fd1fabc3ad6489cb476793f72b1c05f326e52f8fd36619c6097ec58e25bc`;
owned drop-in `postfix.service.d/90-mx2-verification-outage.conf` SHA256
`190ea31707f05facfb50431d563fc7c5a1764e4e7e0514c13912feeac77f4a88`.
Hashes were rechecked before removal: drop-in removed, daemon reloaded, fault
stopped, unit removed, daemon reloaded. Unit is not-found; both MX2VERIFY chains,
OUTPUT jumps and dependency are absent. Normal targeted flush delivered the same
queue ID250 and drained it. Only empty standard directories created for these
files remain. [Persistence](mx2-outage-persistence.json),
[cleanup](mx2-outage-cleanup.json), [final health](mx2-live-final.json).

## Authorized Postgrey reset and retained recovery data

User explicitly said: "mx2 was never used, so the db can be reset". Old package
used Berkeley DB5.3; new package4.8 rejected the old log version19. Clone proof
confirmed matching5.3 opened both old DBs. No live data conversion was performed.
After verified backup, only unused `/var/postgrey` was renamed to protected
`/root/mx2-postgrey-recovery-20261104-57422c4b/reset-original`; native preStart
created a fresh4.8 environment, which stayed healthy through reboot. Postfix
spool/accepted queue was never reset or deleted.

Complete protected original backup remains at
`/root/mx2-postgrey-recovery-20261104-57422c4b/backup`.
Parent is root:root0700; metadata/hash manifests, two diagnostic clones and logs
are retained there. Final hashes of backup and reset-original still match the
original manifest. Fresh greylist state is explicitly distinct from continuity
of the unused old environment. [Reset evidence](postgrey-reset.json).

Private staging verification is complete. Banner `mx2.localdomain`, absent inbound
STARTTLS, public IPv6/PTR/outbound-source readiness, recipient/backscatter and
absent-milter policy remain public-cutover gates from the design. No public IP,
CentOS, primary, DNS-fleet, source integration or lifecycle operation occurred.
Claim13ba611e-2f87-4036-b958-b0e056e13da7 remains with lead under the existing
verification/integrated-lineage policy; this receipt does not release it.
