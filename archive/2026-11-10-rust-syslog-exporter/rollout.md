# Syslog exporter deployment on log.int

## Final corrected deployment and integration

The corrected exporter is running and working on log.int. Normal switch with
automatic rollback completed0, all4health checks passed, and D4's complete240s
live window passed. Current/profile is exact79kk / `system-145-link`, clean
configurationdda57166 and provider891db6b8; RustPID69580/executablegv3/SHA14b542
match the actual tested release. RsyslogPID63415 and start identity never changed.
No synthetic fatal message or production payload read was performed.

Both remote masters now equal the exact deployed final feature heads:

- syslog-exporter: `891db6b82ccd37e985507c654050143e165041a7`.
- vpsfree-cz-configuration: `dda57166bd8bb6d85a74decdd05a8810933bdecc`.

Each was FF merged with required hooks in a prepared Nix environment under one
short repository claim, pushed normally over SSH and independently proved by
fresh remote refs/ancestry. Both claims were released before records/CI. Final
master CI43124385181 passed on891. Machine6fda was released and its released state
verified at00:09:39Z after deployment effects and integrated lineage were known.
Later deployment requires fresh ownership. No session lifecycle action occurred.

D4:5/5HTTP200/no503 or retries, records+57,467, knownmessages+42,758,
kernel+35,582, rejected/reopens/decoded-body0; RSS4.80–5.49MB and CPU+3.18s.
All4exact archivefiles advanced by metadata; account/FIFO/state/policy and18legacy
metric contracts held. Monitor APIs remain unverified after earlier access
refusals; no retry or synthetic flare was used. Source60837, all SSH/sampler and
watcher effects joined. Detailed evidence: [live verification](deployment-verification.md)
and `deployment/d4-verification-summary.json`.

Full final paths/NARs/source/input graphs: C4 prepared summary and correction
preparation below. Exact normal NAME `2026-11-12--00-30-03` selected host79kk/gv3;
copy/dry/switch receipts and final lineage/release proofs live in deployment/.
The18 required roots retain current79kk/gv3, immediate Rustgsw/3hk and original
Rubykgr/w7 recovery plus sources/input graphs. Only the unused C5 env profile was
removed after all commands ended; no GC/store deletion. Original recovery
commands/contracts and complete historical receipts remain intact below.

## Initial deployment history (2026-11-11)

Deployed on2026-11-11 at about21:03UTC. The normal confctl switch with automatic
rollback completed0; all4health checks passed. Actual running system and system
profile match the prepared candidate, and its process executable/hash match the
measured Rust release. Rsyslog retained PID63415 and was not restarted.
The241.078s live verification window passed all five serial snapshots; the
monitor-API and manual-trigger limits below remain explicit.

The user explicitly authorized: "all right, so you can deploy the log.int system.
keep the work unmerged so that we can fix it up in case bugs are found."
The user later said "okay then, merge it", approving both project branches
into their remote master targets, then explicitly authorized the compatibility
fixes and required this essential service to remain running and working.
No default push has occurred. I3/C4 corrections and their final release must
pass review, checks and readiness before cutover/integration. No session lifecycle
action is authorized; the session stays open.

## Correction preparation history

The user authorized the confirmed compatibility corrections and both project
integrations. R3 accepted provider891db6b82ccd37e985507c654050143e165041a7 with
no findings;25local/release tests and exactCI43116296064 passed. Consumer
`dda57166bd8bb6d85a74decdd05a8810933bdecc` atop currente91 is independently
whole-tree reconstructed and mechanically review-bound. It pins891 with source
hash `sha256-eWPE7ZtE8d4+D8Jr0Dm40ykjoW6PBtLGqMI2GJLhDNI=`.

Prepared normal host:
`/nix/store/79kkfqwr8mc82g5si9ifzkl9ygaqys5r-nixos-system-log-26.05.20261026.718f670`,
NAME `2026-11-12--00-30-03`, NAR
`sha256-KtlZ05Wflr7PywgK7JEyXuURrqY8zslMg4cdO+t6U2c=`.
Package `/nix/store/gv3akrpsz9skwi7skkbkf0kb0wskbzn8-syslog-exporter-0.14.0`,
binary SHA256 `14b542eb040024f0245a645d4ec338c5bdb52b502eb8f520669f410737500bd4`,
NAR `sha256-ea5OgznIj3F/HV/RH2VReomvJCWiIpPSSKYC3CXv2GU=`. All653hostpaths
and7packagepaths are valid; generated settings/logging policy remain unchanged.
C4 owner reconciled a post-build evidence-wrapper error against saved native
build0; it was not a product failure or build rerun. Full typed source/input/
build/closure/root/effect receipts: c2-artifacts/c4-prepared-summary.json.

Currentgsw/3hk stays serving. Explicit oldRust fallback aliases now protect its
system/source/normaldrv in addition to originalkgr/Ruby recovery. All18ownroot
targets valid. V3 measured execution is released on the corrected binary; no
copy/dry/switch/defaultpush has occurred for this successor. C5/D4 read-only
verification waits explicit SWITCH-COMPLETE. Any failed preflight/review/build
or uncertain mutation stops cutover while the current service remains serving.

## Initial deployed and original recovery identity (historical)

| Item | Identity |
| --- | --- |
| Configuration repository / target | git@github.com:vpsfreecz/vpsfree-cz-configuration.git / master |
| Exporter repository / target | git@github.com:vpsfreecz/syslog-exporter.git / master |
| Configured target / SSH alias | cz.vpsfree/containers/prg/int.log / log.int.prg.vpsfree.cz |
| Deployed configuration head | ebe9248d7f57f1cec22089d40432aa95b3b93f60 |
| Selected exporter head | 6ecada0a9d2f6457a11031a3a4ffc341584fb29c |
| Configuration base retained | 3c088a4b71881b3649441ce3c4e92c71757708e6 |
| Fresh upstream default, intentionally unadopted | e91c8d21055b7110182fd4c531389947f180e359 |
| Exact confctl local build NAME | 2026-11-11--21-51-14 |
| Deployed system | /nix/store/gsw7sx6vmin2ndvz1m6rwynbssd1mjc5-nixos-system-log-26.05.20261026.718f670 |
| Normal system derivation | /nix/store/lr1ivf06avilizm3121pfacjk7gx1wmg-nixos-system-log-26.05.20261026.718f670.drv |
| Exporter package | /nix/store/3hk34i2k760dirn1xrarxqsrwrcryaj5-syslog-exporter-0.14.0 |
| Running Rust PID initially | 68364 |
| Running binary SHA256 | f1ad1b4f65be4e4315224b8e3426603f67eb8e99a42593e8f7cfe40ddbc4062c |
| Retained prior system | /nix/store/kgrfplplhrhhj4idvzx172lqh4hiyimq-nixos-system-log-26.05.20261026.718f670 |
| Prior exporter package | /nix/store/w7g32wplgls6x79608h6nij02a4vvq9y-syslog-exporter |
| Observed prior production source | 959e1d54cabc7ac5530dac6179acacb077a57754, clean |
| Observed prior profile | system-143-link; not a local confctl build NAME |

- Deployed system NAR: `sha256-n9ngXaq/qLjOCvcD39XUEfpuZFKPdchFP2uSUEyNWxo=`.
- Package NAR: `sha256-Y+H0duMpY5PGDsNk9DYyO7YJXG3u8u4kwV9Y9X0md28=`.
- Prior system NAR: `sha256-bWKb/DaGJe+JB1a1VYYtML3ejYssKpSyRRi1HudJxZU=`.
- Exporter source NAR: `sha256-2ChtOI8cW7zKer4jbaD5b77Eut+Mf/NzsLc/Hwhy2TE=`.
- Deployed configuration source NAR: `sha256-FU9SjDGaC9II1Igw6hgdSl+Ua1EXt+HyS5QRlKC//pw=`.
- Selected stable nixpkgs718f670e845328e9c2cecdd832835712b2cbd065 and OS staging
  dd188397abe37d0bc33f4c5dfb3605206ce5e326 are unchanged.
- The complete source/input/package/system graphs and runtime closures are in
  [C2 evidence](c2-evidence.md) and C3 receipts. Prior662path closure is locally
  retained; current653path closure is valid. No migration or persistent metric
  state conversion exists.

Fresh mastere91 contains unrelated DNS/status changes. The lead retained the
reviewed/tested3c base for this deployment instead of adding unrelated changes.
Integration approval is now recorded. C4 has prepared a conflict-free rebase
onto e91 with the identical feature patch and independent native tree proof;
final corrected provider pin and selected logger graph checks remain pending.

## Review, measurements and successor lineage

[Review record](review-packet.md) retains the independent full exporter/consumer
reviews, direct narrow fixes and affected HTTP review. Provider6ec changes only
the commit message from measuredfaf: entire tree5d3e6ed8aba81c5b43c34f92b13a5b604d24c478
is identical, independently reconstructed in logs/m-lead-reconstruction.json.
The commit message now contains the measured comparison and its limitations.

Consumerebe changes only the provider revision froma839. Native complete-tree
reconstruction matches38d58a87009f72fa93dbd5ca450f7d064244e062; schema1
c2-artifacts/c3-lead-pin-reconstruction.json binds the original reviewer/ranges,
provider proof and no-migration inventory. Literal package/vendor/source drv IDs
changed through fixed-source rev/revCustom/urls metadata. Builder/environment/
profile/source content/output hashes and actual3hk path are unchanged; the typed
c3-package-input-equivalence.json proof supports reuse of19release tests and V.
The new normal system build passed162.683s and differs from previousnw3 only in
system/etc/configuration-info paths; the entire systemd unit tree is identical.

The new metadata-only commit's CI43096574664 is queued externally. Prior exact
source CI and all19local amended-head hook tests passed; this is not a claim of
a new green CI run. Activation used the exact unchanged tested/measured binary.
M owner continues the queued CI observation; no run was repeated or cancelled.

[V evidence](verification.md) retains actual final-binary42paired/periodic200
responses during1.04Mrecords/65s at16k/s, max6.76ms, zero observed reader count gap.
Finite100k replays gave Rust ordinary50–70k/s and OOM36k/s versus freshRuby16k/s
and4.1k/s, RSS7.6–8.2MB versus38–39MB. Shared-host/producer limits apply. Isolated
causal<=10%normal-scrape capacity impact and production peak remain unestablished.
Useful transport fixtures preserved counts; forced overload lost records, and
pinned ompipe reproduced a partial write joining records. No losslessness claim.

## Executed operation and effects

1. Fresh readonly20:33UTC preflight verified actualkgr/profile143/clean959e,
   both services active, same JSON/FIFO/state and logging policy identities.
2. Normal `confctl deploy --generation 2026-11-11--21-51-14 --copy-only` completed0,
   copying six immutable paths. Lead session39804 joined. Managed observer ended
   without terminal report; parent reconciled actual command0/status/log/exact
   process evidence without retry. Normal monitor resolution is recorded, with
   original incomplete outcome preserved. Later observers used native fallback.
3. Acquired machine claim6fda89a5-8d08-4e52-acb4-a18e4204d331 and verified exact
   configebe binding. Canonical identifier is
   `machine:github.com/vpsfreecz/vpsfree-cz-configuration:cz.vpsfree/containers/prg/int.log`.
   `workspace-host coordination acquire` refused at parsing; the selected guide's
   ordinary `dev-session coordination acquire` succeeded with the same request.
4. Under the claim, fresh SSH verified actual current/profile stillkgr and copied
   candidate/package executables present. Normal confctl dry activation completed0
   (session39333 joined). It suppressed successful preview output, so a bounded
   direct dry activation of the same exact candidate captured the authoritative
   list: only prometheus-syslog-exporter.service stops/starts, no syslog restart.
5. Normal `confctl deploy --generation 2026-11-11--21-51-14 --enable-auto-rollback`
   switch completed0 (session61964 joined); native observer completed,4health
   checks pass. This guard checks connectivity, not metrics semantics.
6. Initial readonly check proves current AND profilegsw, activeRustPID68364 and
   exact3hk executable/hash, syslogPID63415 unchanged. D3 steady validation passed
   over241.078s, all five HTTP200,18legacycontracts and natural counter/file
   progress. [Final D3 report](deployment-verification.md) records exact values;
   both monitor API probes were refused and no node2 trigger was observed.

Exact argv, outcomes, selected utility policy, copy/claim/dry/switch and initial
running-state evidence are in this session's deployment/ receipts and logs.
No synthetic fatal/OOM message was injected by this session. The user owns the
manual node2 alert test below.

## Manual alert requested by the user

After deployment confirmation, on configured node2.stg (whose configured hostname
is node2.stg.vpsfree.cz), use util-linux logger:

```sh
logger --server log.int.prg.vpsfree.cz --port 11514 --tcp \
  --rfc5424 --tag kernel --priority user.err -- \
  'BUG: kernel NULL pointer dereference (manual syslog-exporter test)'
```

Expected series is `syslog_kernel_bug{alias="node2.stg",fqdn="node2.stg.vpsfree.cz",type="nullptr"}=1`.
It raises the real KernelNullPointer/fatal alert after ingestion/scraping. The
pulse lasts240s after the latest matching message, then resets on the5s sweep
strictly after expiry. Do not add a colon or --id to this explicit RFC5424 tag.
The exporter routes by configured key/FQDN, not alias; an unexpected short OS
hostname would need the explicit-host frame retained in C3 manual-alert evidence.
The existing `flare test` message instead pulses15s and may be missed by60s
Prometheus scraping. No production alert trigger or expiry is claimed until
actually observed; no detector crash is generated by this test.

## Retention, recovery and unmerged work

All10 ordinary indirect roots under retained/ hold currentgsw/package3hk,
configuration-source4lkw, exporter-source1if, production-sourcejm67, exactoldkgr,
selected stable/OS/confctl sources and normallr1 derivation. Root updates were
validated before old links changed; source/input/history/NAR receipts remain.
Temporary Cargo targets and proven owned scratch were cleaned at earlier safe
boundaries; M later removed its sole temporary target after confirming no local rerun or
active reference; its remote CI observer does not need that data.
No global GC, store-path deletion, peer cleanup or lifecycle action occurred.

On a regression, lead-owned recovery restores exact retainedkgr through its
switch-to-configuration switch, then sets the system profile to that same path,
following the recorded normal rollback argv. First reconcile any unfinished
confctl auto-rollback/SSH effects; do not run competing switches. Keep FIFO,
state/log paths and ownership, one reader, and package+launcher together.
Counters/gauges reset and missed metric events cannot be recovered by rollback.

Claim6fda89a5-8d08-4e52-acb4-a18e4204d331 remains held during the authorized
correction. Essential health rechecked22:38Z: same current/profilegsw, exporter68364
and syslog63415, two HTTP200 responses, natural intake+1199records/5s, rejected
and reconnects0. Current3hk/gsw is the immediate healthy fallback for the new
correction; retain originalkgr/Ruby recovery as well. No mutation is underway.
Release requires verified corrected deployment/effects and complete approved
remote integration of deployed lineage. No merge claim has been acquired.
Do not archive/delete/stop this session.
