# C2 final consumer review packet

Current successor: see the C4 binding section at the end. The original C2 packet
and exact review range below are retained as historical evidence.

Status: ready for lead acceptance and independent consumer review. Implementation
owner implementer1 retains C2 and its follow-up fixes. No long candidate package
or host build, activation, deployment, dry-activation, copy or default-branch
integration has occurred. The lead assigns reviewer0; this packet does not invoke
review or claim that review passed.

## Outcome, scope and exact range

Replace only the central logger's Ruby exporter package/launcher with the
reviewed Rust binary, keeping the existing JSON, hosts/collectors, FIFO/account/
port, scrape/alert and file-logging contracts. The user authorized preparation
and implementation but explicitly stopped work before deployment without approval.

- Session: `2026-11-10-rust-syslog-exporter`.
- Plan/state/design: [plan.md](plan.md), [state.md](state.md), [design.md](design.md).
- Repository: `git@github.com:vpsfreecz/vpsfree-cz-configuration.git`.
- Own worktree: `worktrees/2026-11-10-rust-syslog-exporter/vpsfree-cz-configuration`.
- Branch: `2026-11-10-rust-syslog-exporter`.
- Fresh remote default/base: **3c088a4b71881b3649441ce3c4e92c71757708e6**.
- Final committed/published head: **75b0af0323db1412de457cb73362fd741941eef4**.
- Complete base-to-head series: one commit, `75b0af0323db1412de457cb73362fd741941eef4
  syslog-exporter: use the Rust implementation`.
- Fresh SSH `git ls-remote` confirms both exact feature and master heads. Clean
  index/worktree after commit/push. No PR is required or created.

Review the whole range and final diff, not just the recipe. This is one coherent
replacement: the Rust CLI launcher and package must change together; Ruby-file/
updater removal, regression coverage and operations guidance support that same
change. No independently useful extra feature or fleet/input update is bundled.

The series introduces the final result directly. No superseded source pins,
transition packages, obsolete approaches or follow-up commits remain in the
published series. Earlier hash preparation was outside Git. An unpublished
commit-message amendment preserved the source tree; only the final commit is in
the series. No repeated dependency/channel/pin update streams need retention.
**No migrations:** old/new exporters persist neither metrics nor an ingestion
cursor. There is no new database/on-disk format or supported intermediate state.
Neither consumer candidate nor its final pin has been merged, released, deployed
or externally consumed. The running Ruby baseline remains supported for rollback.

## Changed files and responsibility

- `packages/syslog-exporter/default.nix`: stable `rustPlatform.buildRustPackage`,
  exact source/dependency hashes, package metadata from Cargo.toml, Python3 only
  in nativeCheckInputs for the accepted driver-timeout regression.
- Delete only `packages/syslog-exporter/{Gemfile,Gemfile.lock,gemset.nix}`.
- `modules/services/monitoring/prometheus/conf-exporters/syslog.nix`: agreed
  `--config PATH --listen ADDRESS:PORT`, systemd argv escaping/IPv6 listener,
  Type=simple; remove Puma/Rackup/RACK_ENV/notify/watchdog. Keep every option,
  generated JSON/account/FIFO/stateDir/unit name and restart behavior.
- `.github/workflows/daily-update.yml`: remove only syslog-exporter from the
  Ruby dependency-refresh loop; other packages and all action refs unchanged.
- `tests/syslog-exporter.nix`, `flake.nix`: focused default/custom/disabled module
  check, including CLI/binding, JSON settings, account/FIFO mode and restart.
- `docs/operations/syslog-exporter.md`, `docs/operations/README.md`, `mkdocs.yml`:
  reusable service preparation, delivery limits and rollback, indexed in docs.

Final diff: **11 files, +257/-130**. Cluster host configuration, log-reader,
logrotate, rsyslog policy, monitoring rules/target generation, overlay name,
flake inputs/lock and unrelated Ruby tooling/packages are unchanged.

## Provider review lineage and exact pins

Exporter source: **8ef8241c60f3b99976191b92f0467c945e36b1c8**, package 0.14.0.
Original independent exporter review range:
`7c5a8e74e44a704cceb99cd05716af6800d78efd..9a5b3d1c5a970d7bdc8c4771f0c24f3d9ec2b052`.
[Retained exporter review](exporter-final-review.md) found no Blocking/runtime
finding; lead directly accepted narrow I1/A1 remediations under review step 9.
Final versus reviewed runtime `src` trees are identically
`1362270280553d1978986649adc54e4231c9666e`. Relevant quick checks and current-head
CI 42910934231 attempt 1 passed per lead. This packet does not replace that review.

Independently checked final Cargo.lock SHA256:
`031d0b542c8a95a8e0293cd7c62aa3c052b17c29342bbec4d4195feabb78ea1e`.
All 116 external package records and dependency edges are unchanged; 117 packages
including root. Root dev-deps add the already resolved flate2/tower; Cargo
profiles/version/MSRV are unchanged. Nevertheless the final vendor hash changed
and was revalidated instead of reusing the prior candidate proof:

- Final unpacked source hash:
  `sha256-/hSm9QVEichsqqIYS/wkxJ3hwyn+WvoxsfApVIH22mM=`.
- Final vendor hash:
  `sha256-dvnEEbDRJoHlHLj/EDXp21PYrnvx5+J1+BGYQkmN7yI=`.
- Stable nixpkgs source: **718f670e845328e9c2cecdd832835712b2cbd065**, narHash
  `sha256-Ee5BWo8sh3pGt70QUdRajnaginqFmWvrtdBc4gJzhks=`, source path
  `/nix/store/z40fynbhnw0d06q05mw2mznn49h1y9pk-source`.
- os-staging input: **dd188397abe37d0bc33f4c5dfb3605206ce5e326**, source path
  `/nix/store/cgk63vdx1wjl4ybd53abkd5aqyzc7sfa-source`.
- Unchanged full configuration flake.lock SHA256:
  `4aa576733c284b8ceb916fd3f2e18a3ca2afba0102fc54274a542c1d741320a3`.
- Exact final configuration source metadata path:
  `/nix/store/dycm2xwxaycjbhkyykr3wgppb5iy499y-source`, bound to head 75b0af03.

Complete flake source/input graph, host role mapping, package/host derivations and
4074-path host derivation requisite graph are retained untracked in
`c2-artifacts/final-{flake-metadata,host-inputs,package-derivation,host-derivation}.json`
and `final-host-derivation-requisites.txt`. Requisite graph SHA256:
`95742c6958283b183ec7372f5fd23bbcf478e862160481756a7fe72aba7ab7cf`.
These are evaluation receipts, not realized candidate build/deployment receipts.

## Quick verification and prepared outputs

Completed:

1. Exact source prefetch, final lock/profile/external-graph comparison and final
   vendor-only fixed-output fetch. Fresh Luna/low watcher completed final vendor
   check in 9s with the expected old-hash mismatch and new hash above; all effects
   ended. No Rust compilation occurred in that preparation.
2. `nix build --no-link --no-write-lock-file
   .#checks.x86_64-linux.syslog-exporter-config`: pass. Default/custom/disabled
   service, IPv6 CLI, settings, FIFO/account/restart compatibility checked.
3. Package evaluation: 0.14.0, rustc/cargo **1.95.0**, doCheck=true; exact package
   derivation/input metadata include Python3.13.15 only as a native check input.
4. Full log-host evaluation/instantiation: pass, without realization. Generated
   unit uses correct binary/JSON/listener/account, Type=simple and no RACK_ENV or
   watchdog. Generated JSON has 67 hosts and the **same exact output path as the
   read-only inventoried production JSON**:
   `/nix/store/k5a6bd0ilb1m6k1px7a4hpxrhp2r8s6p-syslog-exporter.json`.
5. Repository nixfmt; `bundle exec overcommit --run` (Nixfmt/RuboCop); required
   active pre-commit/commit-msg hooks; YAML parse using repository Ruby; changed
   docs' local links; `git diff --check`: pass. Commit hook TextWidth issued
   advisory default-72-column warnings; every line meets repository <=80 rule.
6. Feature push over SSH, exact remote-head proof and clean tree/index: pass.
   This repository has only scheduled/manual daily-update workflow, no push CI.

Known quick-check tooling issues were repaired without changing source or
bypassing checks: unsupported legacy Nix CLI flags, missing ambient PyYAML
(replaced by repository Ruby YAML), and new Nix derivation JSON schema extraction
(structured JSON value versus plain unit text). No long check was repeated for
these diagnostics. Earlier baseline hook setup failure was repaired through the
declared Nix dev shell and normal hook installation.

Prepared package output, **not built yet**:

- Derivation `/nix/store/63q2mdnravm3cb9920mc1hcp0mcinfas-syslog-exporter-0.14.0.drv`.
- Output `/nix/store/4gbgng817gz6gfvaxwh76gvzh8yvp478-syslog-exporter-0.14.0`.
- Final vendor derivation `/nix/store/2c2fwb5ms2diam1cddw80i8ziq2rm0xf-syslog-exporter-0.14.0-vendor.drv`.
- Final vendor output `/nix/store/dfpq620acg07r3zvy3kbzkrs9y92vbci-syslog-exporter-0.14.0-vendor`.
- Source `/nix/store/vvh7a4sf8qll2bxqgcafrlaggh656zlw-source`.
- Derivation confirms cargoBuildType=release, cargoCheckType=release, doCheck=1;
  source Cargo profile.release has strip=true.

Prepared host output, **not built yet**:

- Derivation `/nix/store/r211qmhibvd4qhwkgaqj9isyrkmgfwkb-nixos-system-log-26.05.20261026.718f670.drv`.
- Output `/nix/store/cihk0x7vvn8y14b20404ycxlpbp3ccik-nixos-system-log-26.05.20261026.718f670`.

After consumer final review, build the package then host with required fresh
watchers. V must reuse that package's `bin/syslog-exporter` release binary rather
than create a duplicate local Cargo release build. Full package Cargo tests,
Nix runtime closure inspection, host build and V transport/performance gates
remain pending. No source/package build claim or machine claim is held.

## Compatibility, deployment and recovery limits

The site module owns generation/permissions/launch; exporter owns parsing,
metric/HTTP semantics. Actual consumers were traced from overlay/package,
module imports, log-host settings, service definitions, monitor scrape generator
and syslog alert rules at base/final source. Existing senders and monitoring can
coexist with this replacement; no node update or fleet coordination is required.
No new transport, durable broker, persisted state, alert policy or metrics rename
was added. Exact legacy metric parity and deliberate robustness fixes remain
provider-owned under I's retained review.

[Read-only inventory](c2-evidence.md#read-only-production-rollback-inventory-2026-11-10-2147-utc)
proved production generation143 and running Ruby package
`/nix/store/w7g32wplgls6x79608h6nij02a4vvq9y-syslog-exporter`, exactly matching
C2's retained baseline; stateDir empty, FIFO mode/account correct, all18 legacy
TYPE families present. Deployed system:
`/nix/store/kgrfplplhrhhj4idvzx172lqh4hiyimq-nixos-system-log-26.05.20261026.718f670`.
No new production probes occurred after the one explicitly authorized pass.
Exact deployed configuration commit and matching retained confctl local build
name remain unknown. Do not use remote generation143 as --generation NAME.
No production closure was copied/rooted; retention must be reconciled before a
future approved activation. The Ruby baseline root remains for I/V fixtures.

Cutover/rollback need separate explicit deployment approval and machine ownership;
none is granted. Preserve one FIFO reader, FIFO/state/log paths, log-reader and
rotation recovery. Counters/gauges reset; software rollback cannot recover lost
FIFO events. Pinned ompipe nonblocking/full/short-write behavior and UDP can lose
records; no losslessness or capacity result is claimed. Long tests follow review;
stop before any deploy/dry-activate/copy/remote mutation. Default-branch integration
has its own separate approval gate.

## Documentation placement and reviewer lanes

| Topic → reader/class | Authoritative destination | Fidelity/evidence |
| --- | --- | --- |
| Runtime/protocol/metrics → exporter maintainers/reference | Exporter docs/reference.md at 8ef8241 | Provider review retained; consumer links to exporter contract |
| Site preparation/delivery/recovery → operators/reusable operations | Configuration docs/operations/syslog-exporter.md | Final module/recipe, pinned rsyslog source, accepted single-reader/reset/loss limits |
| Discovery → operators/index | docs/operations/README.md and mkdocs.yml | Existing root README links Operations index; new guide reachable; YAML/links checked |
| One rollout/exact paths/results → lead/operator/individual execution | c2-evidence.md and raw c2-artifacts | Exact source, read-only inventory and pending gates; no receipts in project docs |

Lead applied required main-agent user-facing writing/fidelity skills and released
the operations docs. Later source reconciliation only joined a wrapped sentence
and added the already-reviewed guide title to MkDocs navigation. No supported
recovery path was removed; existing log-reader access/rotation recovery remains
linked and unchanged. Review should explicitly assess placement/preservation and
unknown production lineage, not treat prepared operations as executed.

Recommended risk: **high**, due cross-project launch/dependency replacement,
host behavior, mixed versions and rollback. Applicable lanes: general,
architecture/repetition, scope/proportionality, risk/compatibility. Reviewer:
retained **reviewer0, gpt-6.1-sol/xhigh/read_only**, same independent reviewer as I;
no model/effort override or nested reviewer. Lead owns acceptance and invocation.
Request explicit whole-series/no-obsolete-history/no-migrations conclusions and
record remaining build/runtime/performance/rollback-provenance gaps.

Disk checkpoint: 95 GiB available/90% usage; own temporary C2 files13MiB,
raw receipt directory428KiB, declared dev gems52MiB. No broad cleanup, GC, peer
output deletion or duplicate release build. All operation-owned commands/watchers
have completed.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-10-rust-syslog-exporter/>.

## C4 final binding, reviewed ranges and delivery boundary

Current consumer is **e91c8d21055b7110182fd4c531389947f180e359..dda57166bd8bb6d85a74decdd05a8810933bdecc**
(one commit; treef56d93d060cc9e0e44917a32452d8a9c3bccbab9).
The original reviewed C2 range3c..75b and affected I2/M proofs remain unchanged.
Deployed consumer3c..ebe/provider6ec/current3hk remains a supported exact recovery
boundary, protected by refs and local source/output/host-drv roots. The clean
rebase ontoe91 preserves the exact deployed patch; only upstream public DNS,
health checks and unselected vpsfStatus changed. No selected logging input drift.

After that rebase, only packages/syslog-exporter/default.nix changes revision
6ec→891db6b82ccd37e985507c654050143e165041a7 and source hash
sha256-eWPE7ZtE8d4+D8Jr0Dm40ykjoW6PBtLGqMI2GJLhDNI=.
The native alternate-index full reconstruction equals the final tree and lead's
independent expected tree/recipe blobdf91bac5a20cb62951f94d035a3b3f378fcd520e.
Lead accepted this review binding in c4-lead-expected-tree.json and released local
builds. There is no obsolete pin stream, migration, extra module/docs/test/lock
change or new shipped operational instruction. Existing operations guide remains
applicable; no additional writing pass is required for unchanged prose.

Accepted independent R3 source range7c5a8e74..891db6b8 (affected6ec..891) is
substantive, with no findings,25 source tests/hooks and exact-head CI success.
See r3-final-review.md and design.md D7. Manifest/lock/toolchain/profile/driver/
HTTP/CLI identities are unchanged, but src/parser/input/collector changes require
new package and live-readiness verification; prior3hk/V numbers are historical.
No universal parser parity or new production peak/losslessness claim is made.

Quick consumer check and all active hooks pass; SSH publication/remote verification
passes; worktree clean. Normal package zrd9→gv3 and Git-confctl host7sxm→79kk
identities, source and complete raw input graphs are saved. Typed vendor staging
hashdvnEE and processed outputdfpq/NAR+zko stay distinct. Full Nix package25tests,
version/config, runtime closure and normal host/source/unit/policy/closure checks
are executing next, followed by lead-gated focused V3 using that exact binary.
Current production stays3hk/gsw. No new production probe/copy/switch/claim/default
merge by I1. Both immediate Rust rollback and original Ruby rollback stay rooted.

Documentation inventory: parser/encoding behavior belongs to provider
`docs/reference.md` and its tests; reusable site operations remain unchanged in
`docs/operations/syslog-exporter.md`; current revisions/results/recovery are in
this session packet, c2-evidence.md and c2-artifacts. Lead owns rollout/state and
review acceptance. Original receipts are preserved rather than rewritten.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-10-rust-syslog-exporter/

C4 local verification now complete: new gv3 Nix package passed all25 RELEASE
tests; normal79kk host built with NAME2026-11-12--00-30-03, all653 runtime paths
valid. Version/config67/runtime7path checks pass; no Ruby/Python in package
runtime. Host unit/JSON/FIFO/state/logging-policy checks preserve reviewed
contracts. Both builds and all effects quiescent. Exact binary/NAR/profile/full
input/closure/root receipts are linked in c2-artifacts/c4-prepared-summary.json.
Immediate deployedRust and originalRuby fallbacks remain rooted. V3 and cutover
remain lead-gated; no production or default-branch action by this owner.
