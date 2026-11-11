# C2 configuration preparation evidence

Owner: implementer1. Current phase: **corrected builds and stable retention complete;
all C2 command effects quiescent**. Current configuration head
**a839ccf7e7ff07ac616ad7994af33f07975bd1b5**, provider
**faf06c1185ad2f6d39286d2e33896a6455b7bea6**, unchanged base3c088a4b.
Accepted provider/mechanical C2 reviews and corrected build receipts remain bound.
Package **3hk34i2k760dirn1xrarxqsrwrcryaj5** passed all19release tests;
host **nw3d0j9hb1mrwf7hd0daxm6gk1vcfabc** built with normal confctl NAME
**2026-11-11--00-46-58**. Lead accepted V completion and released retention.

Ten ordinary indirect roots now live in this session's stable `retained/`
directory. Candidate653 and actual oldkgr rollback662 closure paths are all
locally valid and match saved sets. Required faf/a839/959e, selected input
sources and exact normalnc86 derivation remain rooted. New roots were registered
and verified before20 redundant own temporary links were unlinked. Removed12
unused own draft/tar/extract files; compact logs and original review/build/source/
NAR/closure receipts remain. Exact stable root map, commands, cleanup byte counts,
confctl link preservation and effects are in
`c2-artifacts/stable-retention-cleanup.json`; current retained summary is
`c2-artifacts/i2-build-verification-summary.json`.

Previous75b/8ef/4gb/3vv results and reviewed old/new ranges remain historical.
Actual production959e and oldkgr recovery proofs were reused locally; no new
production access occurred. No deployment, activation, dry-activation, copy TO
production, default integration, resource claim or session lifecycle action
occurred. Lead owns final tracking/handoff.

## Checkout, ownership and contract

Session identity verified again against `dev-session current` and both environment
variables. Live roster retains implementer1 Sol/xhigh/workspace_write. Own
configuration worktree:
`worktrees/2026-11-10-rust-syslog-exporter/vpsfree-cz-configuration`; branch
`2026-11-10-rust-syslog-exporter`; initial/fresh origin/master
`3c088a4b71881b3649441ce3c4e92c71757708e6`.

Worktree creation completed Git checkout, then post-checkout Overcommit failed
because declared development gems were not installed. The lead confirmed the
portal registration with this exact initial base. Native worktree/branch was
clean and matched the base; no recreation or clobber occurred. Fresh installed-
policy Luna/low watcher ran `nix develop --no-write-lock-file -c true` successfully
in 45s; declared dev gems/environment were repaired. Then normal `bundle exec
overcommit --install` succeeded and `--sign pre-commit` reported no plugin
signature changes. No hook bypass. Logs remain in the owned temporary directory
`/tmp/2026-11-10-rust-syslog-exporter-c2`.

Accepted contract: `syslog-exporter --config PATH --listen ADDRESS:PORT`,
Type=simple, no RACK_ENV/notify/watchdog. Keep all existing module options,
generated JSON, hosts/collector map, FIFO ownership/mode, account, working
directory, unit name, port, monitoring, log-reader and rotation. No persisted
runtime state and no migrations. No rsyslog policy changes.

Operational prose files were sent to the lead for its required main-agent writing
and fidelity pass; lead completed that pass and released the docs back. Only a
subsequent line-wrap join changed presentation. Sources:
`docs/operations/syslog-exporter.md`, `docs/operations/README.md`.

## Pinned producer source evidence

Downloaded official rsyslog 8.2610.0 source tarball from
`https://www.rsyslog.com/files/download/rsyslog/rsyslog-8.2610.0.tar.gz` into the
owned temporary directory. Verified SHA256 equals the exact consumer stable
nixpkgs package hash:
`sha256-e9+V6B6mwO5dWGNC1X0qbjlbCJ+zxnMYoNxVWBbeQEs=`.
No disposable server/capture was needed to settle source framing; actual
transport burst/restart measurements remain later post-review verification.

Source locations inside that tarball:

- `tools/ompipe.c:108-113,362-364,389`: modern action and legacy pipe default
  `RSYSLOG_FileFormat`.
- `tools/smfile.c:78-111`: reported timestamp RFC3339, space, hostname, space,
  tag, optional space if message does not already begin with one, message, LF.
- `runtime/rsconf.c:376`: default maximum message size **8096** bytes.
  `runtime/parser.c:437-440` limits sanitized expansion to this maximum.
- `runtime/rsconf.c:407-414`: trailing LF removed on reception; CR retained;
  controls including TAB escaped with `#`, non-C-style escaping, high bytes
  retained. Output framing appends its LF separately.
- `tools/ompipe.c:141-188`: open O_RDWR|O_NONBLOCK|O_CLOEXEC; one write(strlen);
  EAGAIN returns SUSPENDED; other negative writes close descriptor and suspend.
  Positive short writes are not retried/checked against total length.
- `runtime/action.c:330,352,453-455`: direct action queue, retry count zero,
  resume interval 30s defaults. `runtime/rsconf.c:382-405`: fixed-array main
  queue 100000, two workers, no queue filename or disk maximum. This is not a
  durable central FIFO replay contract. No application policy change was made.

Evidence was sent directly to architect0 and implementer0. The initial C
unknowns about template/newline/size are resolved by this source pass. Loss under
actual partial-write/full-FIFO/restart conditions is still a measurement gap;
node sender queues provide no central-delivery proof.

## Exact Ruby baseline for implementer0's fixtures

Before package removal, evaluated configuration-pinned stable packages with the
site overlays. The Ruby package derivation was independently found in the full
baseline log-host derivation's requisites:

- Host derivation:
  `/nix/store/nwb1jw34jy539z5hgbx4cwr3v5pn10kp-nixos-system-log-26.05.20261026.718f670.drv`.
  It was evaluated, not built or deployed; this is not the actual production
  generation.
- Exporter derivation:
  `/nix/store/hzv5vgrxq9iz7kl4brm8w8k0bbikwrbf-syslog-exporter.drv`.
- Realized package:
  `/nix/store/w7g32wplgls6x79608h6nij02a4vvq9y-syslog-exporter`.
- Fresh watcher realized only that baseline package in 6s, exit 0, using
  `nix-store --realise <drv> --add-root /tmp/2026-11-10-rust-syslog-exporter-c2/ruby-baseline --indirect`.
  Log: `ruby-baseline-build.log`; no running effects remained.
- Ruby:
  `/nix/store/3rcm37q1arwggzjxzcnbiz5s8a7c1ppx-ruby-3.4.9`.
- Exporter gem:
  `/nix/store/bxvjhxsk7c26hrraa7ziyaqz7xr2f2cn-ruby3.4-syslog-exporter-7c5a8e74e44a`.
- Puma 8.0.2:
  `/nix/store/sis1vq2y3r75kk0nggdi2gyd7c2l4rsx-ruby3.4-puma-8.0.2`.
- Rack 3.2.7:
  `/nix/store/1gvpz7vknvdp1iflmkb7vhla8in92fbr-ruby3.4-rack-3.2.7`.
- prometheus-client 4.2.5:
  `/nix/store/y6fnm21s29nsd5dyc84h2ryd3l2rsa04-ruby3.4-prometheus-client-4.2.5`.
- Pinned central rsyslog:
  `/nix/store/g0g8nvq928bgl2dwvvddh99l0543s9cx-rsyslog-8.2610.0`, derivation
  `/nix/store/xj16ma8rcbbbnk5q3pn9q7rgh92w3bzx-rsyslog-8.2610.0.drv`.

Baseline exporter source is `7c5a8e74e44a704cceb99cd05716af6800d78efd`.
Complete baseline configuration lock graph is the committed `flake.lock` at the
configuration base above; host input roles and exact narHashes are also in
[configuration integration](configuration-integration.md). Stable source/toolchain
is nixpkgs `718f670e845328e9c2cecdd832835712b2cbd065`, default Rust/Cargo1.95.0;
os-staging source `dd188397abe37d0bc33f4c5dfb3605206ce5e326`, following stable.
No flake input changed.

The exact closure and reproduction expression were sent to implementer0; it owns
the actual Rack middleware goldens. Preserve this baseline root through fixture
and matched benchmark use. It is baseline recovery/verification material, not a
shipped fallback. Actual deployed old closure must be captured under later
read-only operational authorization before rollout.

## Quick checks and remaining work

Prepared service module and daily Ruby-loop change; added a focused configuration
check for default/custom/disabled service, CLI/IPv6 binding, options/settings,
FIFO ownership/mode, user and restart behavior. Direct check evaluation against
pinned stable nixpkgs succeeded:
`tests/syslog-exporter.nix` →
`/nix/store/bjwi523rm7zgxk89w5nk08xy22dn4wgk-syslog-exporter-config.drv`.
Formatting with repository nixfmt succeeded; scoped diff whitespace check passes.
Attempting to realize the evaluation-only .drvPath directly failed because strict
evaluation does not write the derivation. A first attempt also used nix-build's
unsupported-on-nix-store --no-out-link flag; neither command built or mutated
source. The corrected direct nix-build check instantiated and built the derivation,
exit 0, output `/nix/store/mhkgp52n2nwgbvzd102n1mipgfrwf6nq-syslog-exporter-config`.

No final package pin or candidate build receipt yet. Next: fill exact reviewed
published source/Cargo hashes, remove only syslog Ruby package manifests, run
quick checks/hooks, commit/push feature branch and deliver final base-to-head
review packet. Long package/host/transport/performance verification follows final
exporter/config review. Stop before every deployment/activation command.

Initial C2 disk check: 100 GiB available, 90% usage. Temporary tarball ~12 MiB,
small source extracts/logs, one baseline package root; no duplicate closures,
broad cleanup or GC. Record end-of-batch headroom/owned size before handoff.

Current independent-source checkpoint: 102 GiB available/90% usage, owned
temporary directory 12 MiB and declared dev gems 52 MiB. No host/package
candidate build yet; old baseline closure retained for implementer0.

## Read-only production rollback inventory, 2026-11-10 21:47 UTC

Lead explicitly authorized one bounded read-only pass of the exact logger,
overriding only the earlier no-production-SSH brief for these reads. No deployment,
dry-activation, restart/reload, copy, remote GC/root creation, mutation or machine
claim was authorized or performed. This inventory resumes C2's preparation only;
C2 remains parked on I's final reviewed/published pin afterward.

Reverified session/environment identity and live saved roster. Re-read workspace
AGENTS/deployment routing, the repository log-reader operations guidance and the
pinned confctl SSH implementation/manpage. The normal confctl transport uses
`ssh -l root` (`lib/confctl/machine_control.rb:177-183`). Used that same account
and exact FQDN with a single noninteractive, bounded connection, no fallback or
second production attempt:

```text
ssh -T -o BatchMode=yes -o ConnectTimeout=8 -o ConnectionAttempts=1
  -o StrictHostKeyChecking=yes -o UpdateHostKeys=no
  -o ServerAliveInterval=5 -o ServerAliveCountMax=2
  -o ControlMaster=no -o ControlPath=none
  -l root log.int.prg.vpsfree.cz sh -s
```

The local subprocess had a 40-second bound. It completed exit 0 in 0.607 seconds,
with empty stderr. Exact argv and complete read-only stdin script are in the
untracked `c2-artifacts/production-inventory-command.json`; result timestamps
and exit are in `production-inventory-result.json`. The script performed only:
`date -u`; `readlink`/`readlink -e` of current-system and system profile;
`systemctl show` of the two exact units with selected Id/ActiveState/SubState/
ExecStart/FragmentPath/User/Group/WorkingDirectory properties; `stat` on the
FIFO/state directory; depth-2, at-most-1001-entry type/mode/owner/group-only
`find` summary; `nix-store --query --requisites` of current-system; and one
bounded localhost HTTP scrape filtered to family names/TYPE. It never read
state contents, environment, credentials or log payloads. No candidate was run
or workload generated; no new service/server was launched.

Observed at **2026-11-10T21:47:43Z**:

- `/run/current-system` resolves to
  `/nix/store/kgrfplplhrhhj4idvzx172lqh4hiyimq-nixos-system-log-26.05.20261026.718f670`.
- `/nix/var/nix/profiles/system` points immediately to **system-143-link** and
  resolves to that same exact system path. This is remote profile generation
  143, **not** a confctl local build `NAME` for `--generation`.
- `syslog.service`: active/running, fragment
  `/etc/systemd/system/syslog.service`, executable
  `/nix/store/g0g8nvq928bgl2dwvvddh99l0543s9cx-rsyslog-8.2610.0/sbin/rsyslogd`,
  arguments `-f /nix/store/wh66z8v44rnpf6jki0qzfz7qxalxd9na-syslog.conf -n`.
- `prometheus-syslog-exporter.service`: active/running, fragment
  `/etc/systemd/system/prometheus-syslog-exporter.service`, executable
  `/nix/store/w7g32wplgls6x79608h6nij02a4vvq9y-syslog-exporter/bin/puma`,
  arguments `-C /nix/store/97wd9r5jy2rh89z360wzj0rd4mxnid55-syslog-exporter.rb`.
  User/group `syslog-exporter`, working directory `/var/syslog-exporter`.
- The **actual running exporter package exactly matches** C2's graph-proven
  baseline Ruby output. Its Ruby source/dependency identity is therefore the
  retained package identity above; this establishes the exporter baseline, not
  a guessed complete production configuration head.
- `/var/log/rsyslog.pipe`: FIFO, **0640 root:syslog-exporter**.
- `/var/syslog-exporter`: directory, **0750 syslog-exporter:syslog-exporter**.
  Metadata scan found only the directory itself; no child entries or content
  were present/read. The bounded depth/count limit did not truncate an inventory.
- The single ordinary localhost scrape exposed all **18** legacy families with
  their expected counter/gauge types. Only names and TYPE were retained in the
  bounded inventory; no labels, values or payloads were saved.

The exact current-system closure has **662 paths** in
`c2-artifacts/production-system-closure.txt`, SHA256
`2719492cfa31d84c747763063173887d331476b8d4af3f48a1a98a1ce987ad39`.
It includes the baseline Ruby package/gem, exact rsyslog, generated Rackup/Puma/
JSON/unit files and the system path. Full bounded stdout/stderr stay untracked
in the same artifact directory (100 KiB total).

The deployed closure references
`/nix/store/1mw525zm69qz01419m11bil7ixxs589j-etc-confctl-inputs-info.json`.
That exact immutable path also exists locally and was read locally after the
single SSH pass: it records nixpkgsStable
`718f670e845328e9c2cecdd832835712b2cbd065` and vpsadminosOsStaging
`dd188397abe37d0bc33f4c5dfb3605206ce5e326`, matching C2's baseline roles.
The closure also references
`/nix/store/jgc44l9xhq24c817jk640ihsr4j0x0jv-etc-confctl-configuration-info.json`,
but that file is unavailable locally and was not read during the production pass.
**The exact deployed configuration repository revision remains unknown.**
No second SSH pass was made to resolve it.

The earlier local baseline host .drvPath could not subsequently be queried for
its output (not locally available/substitutable); do not identify its evaluated
system with the deployed system merely from the version suffix. The directly
observed deployed system and package paths above are authoritative for this
inventory. A matching retained local confctl build name, full configuration
revision and recovery closure availability must be reconciled before a future
approved deployment. No local or remote rollback root was created for the
production system, and no system closure was copied. Existing current/profile
references were inspected only; this does not promise indefinite retention.

Returned to the parked reviewed-exporter-pin dependency. Owner implementer1
retains C2; no next-package capacity or lifecycle change.


## Candidate hash preparation pending exporter review

Lead reported final exporter review assigned on
`7c5a8e74e44a704cceb99cd05716af6800d78efd..9a5b3d1c5a970d7bdc8c4771f0c24f3d9ec2b052`.
This subsection is preparation evidence, not a final pin or review disposition.
Canonical exporter SSH fetch completed. Inspected this exact published revision:
Cargo version 0.14.0, edition 2024, MSRV 1.95, Cargo.lock format 4. Lock SHA256:
`e49e3f6163856a6c29d0fb6a7fca835d1d41539cbda0b58fe95b2417ff92f2a8`.

Unpacked exact GitHub source prefetch succeeded:
`sha256-D+TpfWRZ4jfnyQZ7hgDxLNgaF+wMkkl0YdynysW6bMQ=`.
A temporary recipe outside the project tree selects stable rustPlatform and
reads package name/version/description from the source Cargo.toml. A fresh
installed-policy Luna/low watcher selected **only `.cargoDeps`**, with a temporary
fake hash, to discover the fixed-output vendor hash. It finished in 12 seconds
with expected hash-mismatch exit 1:
`sha256-kXNj47JjWTAS7FirfUOhTSUpAAMeqf+D+rq0P4weqOo=`.
Log: `/tmp/2026-11-10-rust-syslog-exporter-c2/cargo-vendor-hash.log`.
All operation sessions finished; no Rust compile, candidate package/host build,
production probe or deployment occurred. The temporary draft now contains that
actual vendor hash. No source pin is committed or finalized before review.

After final exporter and C2 reviews, use the **final buildRustPackage output's
`bin/syslog-exporter`** as V's Rust release binary. Pass its exact derivation,
output, source/full input graph and Cargo release profile (`strip = true`) to
implementer0. Do not create a second local Cargo release build/target. This
remains dependent on final review disposition and the later authorized build.
Current headroom at hash preparation: 100 GiB available, 90% filesystem usage.


## Final committed consumer checkpoint

Final feature head75b0af0323db1412de457cb73362fd741941eef4 is pushed by SSH and
verified against the exact remote ref; fresh remote master remains3c088a4b.
Tree/index clean. One coherent source change; no migrations, superseded pins or
repeated update stream in the final series. Full diff11files,+257/-130.

Final accepted exporter8ef8241c uses sourceHash
`sha256-/hSm9QVEichsqqIYS/wkxJ3hwyn+WvoxsfApVIH22mM=` and final revalidated
vendorHash`sha256-dvnEEbDRJoHlHLj/EDXp21PYrnvx5+J1+BGYQkmN7yI=`. The final
lock changes root metadata even though116external records/edges and release
profile remain identical; prior vendor hash was therefore not reused. Python3
is nativeCheckInputs only. Repository formatting, full Overcommit run, active
commit hooks, focused config check, full host evaluation, generated JSON/unit,
YAML/links and whitespace pass. Commit-msg default72-column warnings were
advisory; all lines comply with local80-column rule. Source pin/service/docs
and Ruby-only removal are complete, with no unrelated pins/policy changes.

Generated67-host JSON output exactly matches the inventoried production path;
new unit points to anticipated Rust4gbgng817gz6gfvaxwh76gvzh8yvp478 output.
Actual package/host realization still awaits consumer review; V will reuse the
Nix release output, no duplicate local Cargo release build. All final source/
input/derivation/graph/anticipated-output evidence is in c2-review-packet.md and
untracked c2-artifacts. No production follow-up or deploy/dry-activation/copy.
Owner retains C2 for review fixes and later approved verification dependency.

## Source availability and retention reconstruction, 22:23 UTC

At this checkpoint, the saved exporter/configuration source paths and both
candidate .drv paths were absent. Stable/OS input sources and the retained Ruby
baseline remained available. Cause of prior absence is unknown; earlier saved
hash/Git/derivation receipts remain original evidence, not a current retention
claim.

Using exact accepted source revision/hash, fixed-source prefetch restored
`/nix/store/vvh7a4sf8qll2bxqgcafrlaggh656zlw-source` with the same expected
`sha256-/hSm9QVEichsqqIYS/wkxJ3hwyn+WvoxsfApVIH22mM=`. Metadata reconstruction
of the clean committed configuration restored the same
`/nix/store/dycm2xwxaycjbhkyykr3wgppb5iy499y-source`, exact revision75b0af03 and
original narHash`sha256-NmMvn7S+FYMPmPWRDgwFm7Im+TSU33vIIhO+jKoqDKQ=`.
Original receipts were preserved. New proof is in
`c2-artifacts/{source-retention-receipt,reconstructed-flake-metadata}.json`.

Created only four session-owned indirect source roots under
`/tmp/2026-11-10-rust-syslog-exporter-c2/retained/`:
`exporter-source`, `configuration-source`, `nixpkgs-stable-source`,
`vpsadminos-source`. Their target identity and native registration were checked.
No candidate package/host realization or whole-raw-graph rooting occurred.
After consumer review disposition, reinstantiate exact committed candidate
derivations with their own necessary roots and compare identities before any
long build; retain actual package/system outputs through V/prepared handoff.

During registration verification, `nix-store --query --roots` itself emitted
native stale-auto-link removal for
`/nix/var/nix/gcroots/auto/xwlzpqzwcmaivg4kif9mac4prvnmfm54`, whose displayed
target was an unavailable coordination notification root. This was incidental
Nix query behavior, not an invoked GC/manual cleanup. No peer files or receipts were inspected; the stale-auto-link removal above
is the only observed incidental effect. All root-query commands completed and no further
global root query is planned. No store GC, broad cleanup, production access,
deployment/dry-activation/copy or source change occurred.

## Accepted review and local build phase

Lead accepted reviewer0's final C2 review on3c088a4b..75b0af03: no Blocking,
Important or Advisory findings; complete history/no-migration/documentation
conclusions pass. Local build phase is released, deployment is not.

Reinstantiated original package63q2... and path-evaluated hostr211... exactly,
with session-owned indirect derivation roots. Inspected dry-run cache/build
plans before realization: no actual kernel compilation. Fresh installed-policy
Luna/low watcher built package first, max-jobs2/cores4, exit0 in187.714s.
All14 release tests pass (1library,7contracts,6runtime), including the
Python-driven finite timeout/reaping check. Package version0.14.0 and
--check-config on actual generated67host JSON pass. Seven-path runtime closure
contains no Ruby or Python. Binary SHA256:
`06e40f591a64bb23f678eb1533c401256e5c529452159b6620bb005c0e2d195c`.
Build log/result, closure and package-verification.json are saved in c2-artifacts.
The realized package output4gbgng... is rooted under retained/package-output.

Before the normal confctl host build, checked the actual `.#confctl.build` Git
flake evaluation. It selects a different host derivation than the earlier
absolute-path builtins.getFlake evaluation:
`/nix/store/2kf4sdrxvj9qybg6834rrv9ln34x0gqx-nixos-system-log-26.05.20261026.718f670.drv`,
expected output
`/nix/store/3vvzbm5gch4xhyr1gmznpb5a624ar85g-nixos-system-log-26.05.20261026.718f670`.
Exact graph comparison proves only added immutable confctl configuration-info
(schema1,revision75b0af03,revisionDirtyfalse) and consequent etc/activate/top
nodes differ. Package/unit/JSON/all other graph nodes and input sources match.
Original receipts are retained. Difference was recorded/reported before acting;
lead accepted this metadata-only normal-confctl identity. Current normal host
root is retained/confctl-host-drv; proof is normal-confctl-host-identity-diff.json.

Host build is a separate fresh watcher using only normal local
`nix develop --no-write-lock-file -c confctl build --yes --max-jobs 2 --cores 4 cz.vpsfree/containers/prg/int.log`.
No activation/deploy/dry-activate/copy command is run. V waits for host build and
rollback retention preparation to finish before matched measurements.

## Clean production revision and unrelated source delta

A second separately authorized bounded read-only production pass, at
2026-11-10T22:29:12Z, read only current-system/profile links and the known
immutable configuration-info file after inspecting pinned confctl's producer
schema locally. Exit0/empty stderr; profile143 and exact kgrf... system were
unchanged. No full inventory or scrape was repeated.

The <=64KiB known JSON has exactly schemaVersion1,
revision **959e1d54cabc7ac5530dac6179acacb077a57754**, revisionDirty **false**.
No unexpected keys or raw unknown fields were retained. Exact SSH argv/stdin,
links and safe parsed fields are in production-configuration-revision.json.
This supersedes the earlier unknown deployed-configuration-revision gap.

Canonical Git comparison959e1d54..75b0af03 has exactly three commits: DNS aliases
0c6b844e, vpsfStatus pin3c088a4b, and C2. Besides C2, only internal/public DNS zone
files and the vpsfStatus lock stream differ. Five changed lock nodes are
impermanence_5,nixpkgsUnstable_3,nixpkgs_10,vpsadminos_2,vpsfStatus. Traversal from
the log host's selected nixpkgsStable/vpsadminosOsStaging role roots proves zero
changed reachable nodes and the same complete selected input graph. DNS zones
are imported by DNS/monitor host configs; vpsfStatus is imported by the apu host,
not the logger. No unrelated logger input/policy activation change was identified
from these baseline commits. Exact comparison graph is recorded separately in
production-candidate-source-comparison.json; final runtime closure checks follow
host realization. Global source provenance metadata necessarily changes to75b.

The lead additionally authorized exact old-system local retention after the host
build: inspect only saved662local paths, then a bounded read-only source pull
from production if needed and safely sized. No recovery transfer is started
while the host watcher runs. This authorizes only data FROM production, never
candidate copy TO it or profile/root/service mutation. Profile143 remains a
remote numeric generation, not a confctl local build NAME.


## Completed host and rollback retention checkpoint

Normal confctl local host build passed in127.576s, no kernel build. Local build
NAME **2026-11-10--23-35-23** retains inputs/toplevel/autoRollback in the own
worktree's `.confctl/generations/cz.vpsfree:containers:prg:int.log/` record.
Candidate host:
`/nix/store/3vvzbm5gch4xhyr1gmznpb5a624ar85g-nixos-system-log-26.05.20261026.718f670`,
derivation2kf4sdrxvj9qybg6834rrv9ln34x0gqx. Full runtime closure has653 paths;
Rust package present, old Ruby exporter package/gem absent. Unrelated Ruby
bepasty and Python log-reader remain. Realized unit/settings/tmpfiles pass;
rsyslog.conf and logrotate.conf paths exactly match inventoried production.
Installed configuration provenance is schema1, clean75b0af03.

Only7 of the observed662 old-system paths were locally missing. Source metadata
preflight on those exact7 bounded the transfer to156,824 NAR bytes. The single
fresh-watcher recovery operation streamed remote `nix-store --export` to LOCAL
`nix-store --import`, both exit0, in0.4775s. No writable remote server/profile/
root/service command or trust-bypass flag was used. All source/import processes
ended. Imported7path NAR hashes/sizes/references match source metadata. All662
paths are now locally valid and exactly set-equal to the originally observed
closure. No data was copied to production.

Exact rollback system
`/nix/store/kgrfplplhrhhj4idvzx172lqh4hiyimq-nixos-system-log-26.05.20261026.718f670`
is locally retained by the indirect root
`/tmp/2026-11-10-rust-syslog-exporter-c2/retained/rollback-system`.
Full local closure NAR identity manifest SHA256:
`9c9311bb81a72a75be1f60f10b0d6b5b3de5aa476597046883e5bed595f0424a`.
Old system narHash`sha256-bWKb/DaGJe+JB1a1VYYtML3ejYssKpSyRRi1HudJxZU=`.
Its clean source959e1d54 has canonical tree
`d12a1746a0d11506559b5dc98c1b3105e1bd7fec` and complete source/lock graph
preserved in production-flake-metadata.json. Source path
`/nix/store/jm67q6awjzqcyn9pr23i5hncxq4jj94v-source`, narHash
`sha256-jJ5pu+QpHLNSikHBfvLCm5j2NJapUEI7FyTq7ioLrdM=`, is retained under
retained/production-configuration-source. Selected role graphs remain equal.
The old runtime662→new653 path-set difference consists only of exporter Ruby
bundle/dependencies/launcher removal, Rust package addition, changed exporter
unit/system-units/etc, provenance and system outputs. This corroborates no
unrelated DNS/status activation delta. Profile143 still is not a local confctl
build NAME; rollback approval preparation retains the exact old store closure
instead of inventing such a name.

New host narHash`sha256-Ala5Jtavlb6jNPXCu7s6jyjsYw+3uPih+AItr7rjT7w=`;
Rust package narHash`sha256-+T5cM6etY80HtKvvVIShfuiHcZJxAdv3iQgPG1DmqHQ=`.
Exact root targets, source/input/derivation/output/profile/build/closure/NAR
receipts are in retained-build-recovery-summary.json and linked raw receipts.
Package/host output roots, selected source/derivation roots and old Ruby/system
roots remain necessary through V and prepared handoff. Original path-evaluation
and accepted normal Git-flake metadata-difference receipts both remain intact.

C2 released the build/transfer quiescence gate to implementer0 with exact release
binary SHA/input/profile/recovery receipts. No duplicate Cargo release target
was built. No C2 command/rerun needs implementer0's403MiB debug target; only that
owner checks/removes its files under lead direction. C2 remains responsible for
its follow-up fixes if V reveals a consumer issue. Deployment/default integration
remain separately unauthorized; no further production action is planned.


## I2 mechanical provider-pin consolidation

Lead released corrected providerfaf06c1185ad2f6d39286d2e33896a6455b7bea6 after
reviewer0 affected HTTP review found no findings and19tests/current CI passed.
Fresh SSH fetch still showed remote configuration master3c088a4b and own75b;
no rebase/input movement occurred. Bound session/live retained settings verified.
Independent full-byte comparisons prove unchanged Cargo.toml/lock/toolchain/
shell/release profiles/driver/check/hook. Only provider HTTP implementation and
two HTTP docs differ. Final lock031d0b54 unchanged.

New sourceHash`sha256-2ChtOI8cW7zKer4jbaD5b77Eut+Mf/NzsLc/Hwhy2TE=` is fetched
and rooted. Vendor-only reconstruction passed through fresh Luna/low watcher in
16.434s, reproducing exactly dvnEE... hash and dfpq... output. No candidate
compilation occurred. Scoped configuration check/Nix parse/whitespace and active
commit hooks pass. Source history is consolidated in one amended coherent commit
**a839ccf7e7ff07ac616ad7994af33f07975bd1b5**, tree514c410e; old75b tree0c409ea0
and full original commit/ranges remain in receipts. Lease-protected SSH feature
push replaced only expected remote75b, then exactremote heads were verified;
master remains3c. Working tree/index clean.

Exact old→new source diff is one recipe file,2insertions/2deletions, only revision
and sourceHash. Package derivation env differs only out/src, builder/args/name/
platform/release/check/Python inputs match. Rendered unit differs only package
output prefix. JSON/syslog/logrotate derivations and consumer logic/test/docs/
flake lock are byte-identical. No migrations or superseded pin stream remains
in the new branch. All proof/graphs/evaluated outputs are in the I2 pin packet
and raw i2-* receipts. Corrected outputs3hk/nw3 are anticipated, not realized.

Await the lead's explicit mechanical pin/review release before corrected package
and normal-host builds. Previous deployment gates remain closed; no production
probe/pull or source/module/docs logic change occurred during this refresh.

## Corrected build release and vendor hash-layer clarification

Lead accepted the mechanical binding after independently reconstructing the
entire a839 tree from reviewed75b plus exactly the two recipe substitutions;
expected/actual tree514c410e agree. Provider Git archive independently matches
2Cht... source hash. The lead's schema1 reconstruction receipt preserves exact
old/new ranges, original C2 and I2 provider reviews and no-migration/history
conclusions. Corrected package/normal-host local builds are now released,
sequentially; V remains parked until both are fully quiescent.

Pinned `pkgs/build-support/rust/fetch-cargo-vendor.nix` defines two distinct
layers, independently checked locally:

- `cargoHash = sha256-dvnEEbDRJoHlHLj/EDXp21PYrnvx5+J1+BGYQkmN7yI=` applies
  to the **recursive fixed-output vendor staging**
  `/nix/store/8f9gp8nyslnqq294aas0axrmv9622xjs-syslog-exporter-0.14.0-vendor-staging`
  (NAR15,531,992bytes).
- Processed `.cargoDeps`
  `/nix/store/dfpq620acg07r3zvy3kbzkrs9y92vbci-syslog-exporter-0.14.0-vendor`
  is a **normal runCommand** output, with distinct NAR hash
  `sha256-+zkoIofB1/aV2+6AH86P1thpT3Rpt2UpLSxDGQuIDuY=`
  (NAR93,755,976bytes).

Earlier generic 'vendor hash/output' preparation language described the pipeline;
it must not be read as equating the cargoHash to the processed output's NAR.
No recipe/product defect exists. Final typed receipt is
`c2-artifacts/i2-vendor-identities.json`; original preparation receipts remain
unaltered historical evidence.

Reinstantiated corrected package21lm and normal Git hostnc86 exactly. Dry-run
plans contain no actual kernel build; cached tools/helper work only beyond the
Rust package. Fresh required Luna/low package watcher is running the exact3hk
output with release Cargo checks/Python nativeCheckInputs, max-jobs2/cores4.
Normal host will start afterward. Starting headroom92GiB/91%; no duplicate Cargo
release target, source change, production access or cleanup.


### Corrected package milestone

I2 package watcher passed in159.576s, all19release tests:6library,7contracts,
6runtime; no failures, all processes ended. Exact package3hk reports0.14.0 and
validates the unchanged actual67host JSON. Seven-path runtime closure excludes
Ruby/Python. Binary SHA256
`f1ad1b4f65be4e4315224b8e3426603f67eb8e99a42593e8f7cfe40ddbc4062c`,
package NAR`sha256-Y+H0duMpY5PGDsNk9DYyO7YJXG3u8u4kwV9Y9X0md28=`.
Current exact log/result/closure/NAR/profile proof is i2-package-verification.json
and i2-package-build*. A new separately policy-resolved Luna/low normal-host
watcher is active for exacta839/faf nc86→nw3. V still waits; no production or
cleanup action. Old75b/4gb build/V results remain historical only.


## Corrected I2 builds verified and V released

Corrected normal host build passed in120.315s after package success; exactnc86→nw3
identity matched prediction, no new metadata/fallback difference. Local confctl
NAME **2026-11-11--00-46-58** preserves generation links and selected inputs.
Package21lm→3hk passed all19release tests in159.576s. Both watchers and all
operation-owned processes ended. Version/config67 checks pass. Binary SHA256
`f1ad1b4f65be4e4315224b8e3426603f67eb8e99a42593e8f7cfe40ddbc4062c`,
package NAR`sha256-Y+H0duMpY5PGDsNk9DYyO7YJXG3u8u4kwV9Y9X0md28=`;
seven-path package runtime closure excludes Ruby/Python.

Host653path closure includes corrected3hk and excludes both old Ruby exporter
package/gem and superseded Rust4gb. Unrelated Ruby/bepasty and Python/log-reader
remain. Realized unit exactly matches the anticipated corrected unit, JSON67
pathK5a and FIFO/state modes remain exact, rsyslog/logrotate output paths match
the observed production baseline, and provenance embeds cleana839. Host NAR
`sha256-KknCgMIpbg2EJqGIijH1rFdiAWjtdt33n+Saj2HLemU=`. Host/package results,
logs, full closure/NAR manifest, source/input derivation graphs and current own
root targets are preserved in i2-* receipts. Oldkgr rollback root/validity proof
is reused locally; no production probe or pull occurred.

The current build/verification summary explicitly separates cargoHash/FOD staging
(dvnEE...) from processed vendor NAR(+zko...). All C2 build/check effects are now
quiescent and V may use the corrected3hk release binary. Stable root migration,
obsolete scratch removal and final stable output map remain held for lead's new
V-complete/safe-between-batches release. No cleanup or source changes were made.


## Stable retention and owned scratch cleanup after V

The final lead-released bounded step is complete. Stable roots hold exact current
systemnw3/package3hk, actual rollback systemkgr, exporter/configuration/production
sourcesfaf/a839/959e, pinned stable nixpkgs/os-staging/confctl sources and normalnc86
derivation. All10 targets are locally valid; the candidate653/rollback662 sets
match saved receipts. The existing normal derivation's4075-path graph is valid.
Package src binding separately matches exactfaf source1if; derivation requisites
represent fetched sources through their fetch derivations. Normalnc86 was rooted
by importing that existing immutable .drv with nix-instantiate, without rebuild.

Registration/local-validity checks preceded unlinking20 redundant own temporary
root links, including superseded candidate/path-eval and Ruby-baseline links.
Only12 explicit unused own draft/tar/extract files were removed. Existing
C2 operation receipts and lead-accepted V watcher/unit quiescence establish no
remaining owned effects. An optional same-UID process reference scan encountered
an unreadable /proc cwd and stopped; it made no mutation and was not broadened.
The receipt records this supplementary visibility limit; it does not claim a
complete process scan.

All final confctl NAME2026-11-11--00-46-58 links and metadata are unchanged.
Profile143 remains historical observed production metadata, not an old confctl
NAME. Exact root targets, removed paths/bytes, disk headroom and command effects
are in `c2-artifacts/stable-retention-cleanup.json`. Existing NAR/source/build
proofs were reused without rehashing, rebuilding, fetching or production access.
No GC/global-root query/store-path deletion or peer/lifecycle change occurred.
C2 has no pending command, transfer, build or cleanup effect.
