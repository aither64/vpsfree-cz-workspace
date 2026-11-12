# C2 final independent consumer review

Reviewer: reviewer0, retained gpt-6.1-sol/xhigh/read_only, thread 01a1c742-93c5-7c50-b59e-f792fafd9624.
Mode: final committed consumer deliverable C2, high risk; general, architecture/repetition, scope/proportionality and risk/compatibility lanes.
Repository: vpsfree-cz-configuration, target origin/master.
Complete reviewed range: 3c088a4b71881b3649441ce3c4e92c71757708e6..75b0af0323db1412de457cb73362fd741941eef4.
Provider: syslog-exporter 8ef8241c60f3b99976191b92f0467c945e36b1c8.

## Findings and decision

No Blocking, Important or Advisory findings in the C2 committed source.

The package, service, narrow Ruby removal, module check and reusable operations guide are coherent within the requested boundary. C2 source review is complete and does not block the already authorized local package/host builds and V verification. This is not a successful-build, capacity, production-verification, deployment or integration certification. No additional subsystem or optional hardening is required.

## Identity, instructions and scope

Reverified dev-session current from this session's tracking directory: 2026-11-10-rust-syslog-exporter. DEV_SESSION_SLUG and DEV_SESSION_WORKSPACE were both absent; the trusted exact thread/workspace binding matches. Live same-session roster retains reviewer0, review purpose, ready, independent, gpt-6.1-sol/xhigh/read_only. No settings override or nested agent was used.

Read/reused the unchanged applicable workspace instructions and mandatory-change-review skill with all four references already read in this context. Re-read repository AGENTS.md and the newly applicable deployment procedure, alongside the complete C2 packet/evidence, updated main packet, current state, design/contract context and project documentation. Workspace routing guidance is unchanged from before this review.

Compared the actual user request in plan.md and later preparation/implementation/no-deployment decisions with the whole C2 diffstat and delivered milestones before detailed hardening. The requested consumer work is replacing the single logger's exporter package and launcher while preserving existing JSON, FIFO, account, port, monitoring and logging, and removing only this exporter's Ruby packaging/update entry.

The complete change is one commit, 11 files, +257/-130. Source/check preparation was delivered approximately 21:32 after 21:21 assignment, then parked on the reviewed provider dependency and resumed approximately 22:05, with the final review packet accepted approximately 22:17. These are approximate recorded milestones, not exact active-time measurements; the dependency wait must not be counted as unexplained implementation churn.

The final change remains the smallest conventional consumer integration: buildRustPackage, the existing module/options, ordinary systemd argv escaping, one focused evaluation check and operations guidance. No channel/lock update, transport policy, broker, persisted state, fleet change, new monitoring policy or unrelated Ruby removal was added.

## Package and provider boundary

Reviewed packages/syslog-exporter/default.nix:8–22 against the final provider source and saved derivation evidence.

- Exact pinned revision 8ef8241c60f3b99976191b92f0467c945e36b1c8 is the final published provider following lead-accepted narrow I1/A1 fixes. Preserve my original independent exporter review and the lead's direct narrow-fix disposition; another whole-exporter review was not needed or performed.
- Independently verified that original reviewed 9a5b3d1 and final 8ef8241 have the identical runtime src tree 1362270280553d1978986649adc54e4231c9666e. Inspected the narrow provider Cargo/driver/HTTP-test delta for its effect on consumer build/check dependencies.
- Independently compared all 34 tracked provider files with the fetched /nix/store/vvh7a4sf8qll2bxqgcafrlaggh656zlw-source while it was available: every file matched 8ef8241 exactly. Final Cargo.lock SHA256 is 031d0b542c8a95a8e0293cd7c62aa3c052b17c29342bbec4d4195feabb78ea1e. All 116 external package records and dependency edges are identical to the originally reviewed lock; only root dev-dependency membership changed.
- Name, version 0.14.0 and description are derived from the fixed source manifest rather than separately maintained package metadata. Its Rust 1.95 MSRV agrees with the existing stable rustPlatform. The configuration source hash is sha256-/hSm9QVEichsqqIYS/wkxJ3hwyn+WvoxsfApVIH22mM=.
- The saved vendor-only fetch log reports the newly calculated sha256-dvnEEbDRJoHlHLj/EDXp21PYrnvx5+J1+BGYQkmN7yI=, replacing the prior root-lock hash rather than incorrectly reusing it. This expected hash-discovery mismatch is not a passing full package build; the recipe and prepared final vendor derivation use the returned value.
- Saved final package derivation 63q2mdnravm3cb9920mc1hcp0mcinfas-syslog-exporter-0.14.0.drv binds source, final vendor, Rust/Cargo 1.95.0, cargoBuildType=release, cargoCheckType=release and doCheck=1. Python3 is declared only in nativeCheckInputs for the provider's driver regression. Nix's final environment folds enabled check inputs into its build-time inputs; that does not make Python a declared runtime dependency.
- The anticipated package output is /nix/store/4gbgng817gz6gfvaxwh76gvzh8yvp478-syslog-exporter-0.14.0. Full Cargo check execution, actual installation and runtime-reference/closure inspection remain the next build gate. Do not claim a realized Ruby-free/Python-free package closure merely from evaluation.
- The unchanged overlay retains the package name. Deleting only the three packages/syslog-exporter Ruby manifests and only syslog-exporter from the daily Ruby update loop leaves geminabox, ssh-exporter and repository development Ruby intact.

This preserves provider ownership of parsing/metrics and consumer ownership of source selection, packaging, generated settings and service launch. No duplicated runtime implementation or speculative shared abstraction was introduced.

## Service and consumer compatibility

Reviewed modules/services/monitoring/prometheus/conf-exporters/syslog.nix and the saved complete generated unit.

The new argv calls the package's bin/syslog-exporter with explicit --config and --listen using utils.escapeSystemdExecArgs. Its arguments agree with the reviewed Rust CLI. Bare IPv6 literals receive brackets; the ::1 override is covered by the module check. The default remains 0.0.0.0:9102.

Type=simple and removal of RACK_ENV, notify and WatchdogSec correctly match a binary without Puma's notification protocol. Unit name, network.target ordering, multi-user target, account/group, working directory, Restart=on-failure and RestartSec=30 are preserved. The provider exits on fatal ingestion errors; no incompatible notify unit or fake readiness guarantee remains.

The module retains every option and freeform JSON setting. FIFO defaults and tmpfiles ownership/modes remain 0640 root:syslog-exporter; stateDir remains 0750 and owned by the exporter. Custom account creation behavior is unchanged. There is no FIFO replacement, state deletion, log-reader/rotation edit or new persistence.

Independently checked the saved generated JSON: 67 hosts, all satisfying the provider's required nonempty name/alias/fqdn/os and collector-list shape. Its generated path /nix/store/k5a6bd0ilb1m6k1px7a4hpxrhp2r8s6p-syslog-exporter.json is also in the actual production closure inventory. The generated file was not locally realized during this review, so this is store-identity/evaluation evidence, not an independent new read of production JSON bytes.

Verified that the full C2 diff leaves the log-host tree, monitor target/rule source, overlay and flake.lock unchanged. Inspected actual package/module/host/scrape/alert consumers rather than relying only on the packet's catalog. Existing TCP/UDP/local senders and monitoring can coexist with the new central reader; no coordinated node update is introduced. Literal legacy metric and flare contracts remain provider-owned under the retained exporter review.

The actual production configuration commit is still unknown. Therefore an unchanged feature diff against the chosen repository base does not establish that the eventual full host activation will change only this exporter relative to production. Reconcile the complete activation difference before any separately approved deployment.

## Meaningfulness and limits of verification

tests/syslog-exporter.nix forces evaluation of the real module for default, custom and disabled cases. Its assertions cover the behavior being changed: CLI and listen binding, simple service/no watchdog/no RACK_ENV, restart/account/directory, host settings, FIFO mode and custom overrides. The empty package deliberately keeps this a module/evaluation check; it is not a binary-build or runtime integration test. The separate full log-host evaluation binds the actual selected package.

Inspected final package/host/input JSON receipts, generated unit/settings and the full host requisite inventory. The 4074-path derivation graph includes the exact final package and vendor derivations; SHA256 matches 95742c6958283b183ec7372f5fd23bbcf478e862160481756a7fe72aba7ab7cf. Final configuration metadata binds revision 75b0af03. Stable host roles remain nixpkgs 718f670e845328e9c2cecdd832835712b2cbd065 and vpsadminos dd188397abe37d0bc33f4c5dfb3605206ce5e326. The unchanged configuration lock hash is 4aa576733c284b8ceb916fd3f2e18a3ca2afba0102fc54274a542c1d741320a3.

The owner reports the focused module check, full host evaluation, nixfmt, complete Overcommit run and required commit hooks, YAML/links and quick provider checks passing. I inspected the check source and receipts; I did not rebuild or rerun those mutation-producing checks. The repository has no push CI to wait for; scheduled/manual workflow action refs are unchanged. Git diff --check passes independently.

Local input availability changed during review: after the successful provider file-byte comparison, its fetched source path was absent for a later NAR hash attempt. The final configuration source snapshot path /nix/store/dycm2xwxaycjbhkyykr3wgppb5iy499y-source was also unavailable for a later snapshot-byte comparison. I reported this promptly, did not infer who removed them, and did not refetch/build/clean. The saved graph and Git identities remain valid preparation evidence; these paths must not be represented as currently retained. The attempted NAR/snapshot checks are not passing checks.

## Recovery and operations fidelity

Read the saved production inventory and independently matched its 662-path closure hash 2719492cfa31d84c747763063173887d331476b8d4af3f48a1a98a1ce987ad39.

The observed deployed system is /nix/store/kgrfplplhrhhj4idvzx172lqh4hiyimq-nixos-system-log-26.05.20261026.718f670 with system profile generation 143. The running Ruby package /nix/store/w7g32wplgls6x79608h6nij02a4vvq9y-syslog-exporter and rsyslog path agree with the graph-proven fixture baseline. The recorded FIFO/account/stateDir inventory supports the preparation assumptions; I performed no production probes.

Generation 143 is not a confctl local build NAME. Exact deployed configuration commit and a matching retained local confctl build remain unknown; no production system closure was copied or explicitly rooted. Current/profile references at the inventory time are not indefinite rollback retention. Preserve these limits and reconcile actual recovery availability before an approved activation.

The operations guide correctly requires retaining the old system/package, preserving FIFO/state/log paths and ownership, and restoring package plus launcher together. It preserves one live FIFO reader and explicitly explains restart counter/gauge resets and irreversible loss of already missed metric events. Avoiding an unnecessary rsyslog restart is appropriate; record any actual restart and gap during a later approved switch.

Independently verified the retained rsyslog tarball hash sha256-e9+V6B6mwO5dWGNC1X0qbjlbCJ+zxnMYoNxVWBbeQEs= and inspected its ompipe source: RSYSLOG_FileFormat default, O_RDWR|O_NONBLOCK open, EAGAIN suspension and lack of positive-short-write retry. The guide's central delivery-loss warning is supported by source, not an invented durability promise.

## Whole-branch history and migrations

Independently checked HEAD, merge base, complete log and final diff. C2 contains exactly one commit, 75b0af0323db1412de457cb73362fd741941eef4, “syslog-exporter: use the Rust implementation”. Its message follows local scope/imperative/body rules and describes the final result.

The package and launch change must be introduced/reverted together; scoped Ruby removal, relevant check and operations/index updates support that behavior. There is no independently useful unrelated feature bundled in the commit.

No obsolete unmerged approaches, transition packages, fixup chain or superseded source-pin commits remain in the series. Source-hash drafts were not committed. No repeated dependency/channel/pin update streams exist; the single final provider pin and unchanged flake.lock require no further consolidation. The unpublished message amendment did not retain an obsolete source commit.

No migrations. Neither exporter adds a persisted metric/cursor format, no DB/on-disk migration file or transitional state path appears in C2, and no intermediate consumer feature is reported merged, released, deployed or externally consumed. The existing Ruby generation remains a rollback target, not a shipped compatibility shim.

## Documentation placement and preservation

1. Reachability: existing root README leads to Operations; the new Logging index and MkDocs navigation lead to the new syslog-exporter guide. The existing log-reader recovery page remains linked.
2. Audience/owner/home: site account/FIFO/service and preparation/cutover/rollback procedures belong in configuration docs/operations/syslog-exporter.md. Provider parsing/metrics reference remains in the exporter. Individual heads/results/input inventories stay in session records.
3. Useful lifetime: the project guide is reusable without knowing this initiative's branch status or private receipt paths. It does not embed this rollout's revisions, raw outputs or acceptance results.
4. Fidelity: service/CLI, modes, endpoint, timers/reset statements and producer loss warnings agree with source/evidence. Passing build/scrape is explicitly insufficient for a capacity claim; deployment requires separate approval.
5. Preservation: no existing operational guide or supported recovery instruction was removed. Log-reader/rotation ownership and recovery remain unchanged. Single-reader, service-gap, partial-success/loss and rollback limits are visible.
6. Upgrade/retirement: the Ruby-to-Rust transition explicitly requires retaining the previous closure; it invents neither a persisted migration nor an automatic retirement boundary. Completion or a current profile reference is not presented as proof of indefinite retention.
7. Authority: site operations point to provider semantics rather than duplicating the complete metric/parser contract; local index/log-reader links resolve, and no execution receipt was misplaced into project documentation.

Conclusion: documentation placement and preservation are sound. No supported recovery path was lost or falsely retired.

## Remaining gates and handoff

After lead acceptance, implementer1 may perform the authorized local final package build/checks and host build with required watchers. Inspect the realized package's executable and runtime closure, preserving exact derivation/input identities. V must use that Nix release binary rather than duplicate a Cargo release target.

V remains necessary for matched Ruby/Rust ordinary/OOM/cardinality capacity and memory/scrape measurements, repeated runs and finite pinned-producer overflow/reconnect/restart/partial-write/loss accounting. None of those results is established by C2 source review.

All builds/copies/dry-activation/activation on production and any default-branch integration remain subject to their separate exact authorization; the user currently requires stopping before deployment. No machine or merge claim was acquired. No file edits, report writes, nested agents, builds, long tests, new production access or lifecycle/cleanup actions were performed by this reviewer.

Please persist this report in this session's review records and record acceptance/residual gates in state.md. C2 owner implementer1 retains any later findings. The role remains read-only.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-10-rust-syslog-exporter/
