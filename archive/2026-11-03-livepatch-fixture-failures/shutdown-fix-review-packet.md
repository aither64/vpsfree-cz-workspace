# Production shutdown correction: committed review packet

Session: 2026-11-03-livepatch-fixture-failures. Repository vpsfreecz/vpsadminos, target staging; canonical SSH origin git@github.com:vpsfreecz/vpsadminos.git. Worktree /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-03-livepatch-fixture-failures/vpsadminos. Plan/state/design/implementation-plan are in this directory. All intended application changes are committed, source/index/nonignored-untracked clean; A released Git ownership before checks/records. No publication or integration check has begun for this head.

## Outcome, scope and approval

Original current normal-module livepatch qualification is unchanged. User explicitly approved this added production correction in current-chat request_user_input_async call_7ccafe3d4e8749109837706d8a32a8c7: “Fix here as a separate commit (Recommended)”. The question expressly covered overlapping shutdown requests sharing one complete operation/result, preserving abort/error/export hooks, separate commit and full CI. Conditional staging merge permission remains gated on accepted complete final-head verification; no deployment is authorized.

The observed exact-e175 native failure was osctl/ct-passwd teardown: body passed, stage3 repeated pool manipulation holds until 900s stop timeout; cleanup TERM supplied QEMU exit. Actual holder thread/restart/export progress is unknown. D deterministically reproduced a feasible source-level stale-snapshot interleaving with real manipulation/export/DB-removal paths. This confirms a defect but does not prove that historical VM's exact cause. See native-lineage.md#exact-e175-native-run-41865572140-shutdown-failure, #exact-e175-shutdown-unit-reproduction-confirmed-source-interleaving and package-d-result.md.

Accepted design: design.md#accepted-production-shutdown-coordination and implementation-plan.md#accepted-shutdown-fix-acceptance-and-scope. These sections' implementation-active wording is a prior checkpoint; actual current delivery is committed 645927. One daemon-local active shutdown, admitted before snapshots; overlapping callers join captured operation outcome after complete export tails and owned-lock cleanup. Abort remains responsive; duplicate cannot reset accepted abort or re-arm recreated CLI marker; fresh later request can start. Preserve marker modes/restart intent, original errors/interrupts and same-thread lock ownership. No forced foreign unlock, global Manipulable change, scheduler/framework, CLI/options/wire/schema changes or runner maintenance.

## Exact committed series and review boundary

Base 2951a632c4254a44747a8da326e3dde897eaa0e2 -> HEAD 645927e22809a29c67ffd59c072e553e05e2a72b:
1. 8169b8189c29f471b2ecf27a33b6f71dbde5e70e — tests/livepatch: qualify current module probe sites.
2. e1751c917f216897292ab0b893727a6e5553a540 — osvm: record bounded host evidence for boot failures.
3. 645927e22809a29c67ffd59c072e553e05e2a72b — osctld: coalesce concurrent shutdown requests.

Complete range: 24 paths +3637/-237. New delta e175..645927 is exactly four paths +714/-53:
- osctld/lib/osctld/daemon.rb (+99/-13)
- osctld/lib/osctld/commands/self/shutdown.rb (+44/-40)
- osctld/spec/osctld/commands/heavy_system_spec.rb (+358)
- osctld/spec/osctld/daemon_spec.rb (+213)

Independently review these four committed files and necessary consumers/startup/client/export/abort context, all four lanes, plus complete series/history/migrations. Reuse packaged-dependency-refresh-review.md, osvm-boot-evidence-review.md, source-identity-refresh-review.md and earlier final-review/reconciliation/retention/defined-symbol reports for unchanged twenty-path prefix; no unrelated full source re-audit requested. A's package-a-shutdown-history.log contains full stat/dirstat/inventory/ordered patch IDs/message hashes. Original two objects/messages and twenty modes/blobs remain exact; seven local provenance refs and detached5235 retained. No obsolete source prototype/fixup remains; intentional red logs stay evidence only. Three independently meaningful purposes justify split. No repeated dependency/channel/input/generated update streams in feature series; canonical bootstrap dependency pair remains baseline, unchanged. No migrations: no schema/database/on-disk/protocol transition, deployed or externally consumed intermediate. Nothing in this new correction has been deployed or merged.

## Verification and explicit gap

Exact committed source hashes are bound in package-a-shutdown-commit-pre.json, package-d-shutdown-fix.patch and package-d-result.md:
- daemon.rb 96869f2dc3c99ef6843062f58f5bb80a32b6488da3c3c36e7846212fa1a830ca
- shutdown.rb dcea32b51a87e5e3bd1d4d117d42cab6e9b2e31901d66bddac21e363585e2fe7
- heavy_system_spec.rb ea6a362d8cbb31813e597ec422cf037f4b04ff6a1b105865ab3a4436a4596aff
- daemon_spec.rb cd4278dc046315f5cfbd0febf5200bd163b45976446ab97da6d4c0de742b41d8

Final targeted command is the normal declared osctld bundle `bundle exec rspec spec/osctld/commands/heavy_system_spec.rb spec/osctld/daemon_spec.rb spec/osctld/manipulable_spec.rb`, using exact verified patched Ruby3.4.11/osctld Gemfile+development lock/native/NETLINK/LXC inputs. Exact invocation/result in package-d-shutdown-fix-target-final.{command.json,stdout,stderr,exit}: 45 examples/0 failures, seed11860, RSpec1.4s/total2.831s. Controls cover both owner orders, join-before-snapshot, real post-removal deploy/hook completion/error, import/partial/tail abort, recreated CLI marker, cleanup/foreign locks/original errors, pending/confirmed markers/restart and captured outcomes/back-to-back operations. Recreated-marker focused1/1, package-d-shutdown-fix-cli-marker.*. Root declared RuboCop1.75.8 four files/no offenses, package-d-shutdown-fix-rubocop-final.*. Whitespace passes. All normal mandatory commit hooks pass, package-a-shutdown-commit-hooks.log; no bypass.

Broader whole-osctld suite is UNAVAILABLE BEFORE EXAMPLES, not green and not a product assertion failure. Declared ruby-lxc native load gap was resolved via already-cached matching source+production patch+Ruby provider; incomplete declared filelock gem then blocked loading, a single load-only dry-run with matching cached declared filelock advanced to absent declared bindata. RSpec missing did_you_mean diagnostic masks underlying LoadErrors. No pin/manifest/source/cache purge/install change. Stop broader cache project. Details/package commands/full logs: package-d-result.md#final-complete-code-handoff-broader-suite-unavailable and package-d-shutdown-fix-full-unit*. Assess adequacy of remaining quick coverage independently; do not infer a broad-suite pass or waive runtime acceptance.

A fresh ONE ten-field IFD-disabled tuple on actual645927 passed28.27s; package-a-shutdown-livepatch-identity.json is structurally equal to package-a-2951-livepatch-identity.json. package-a-shutdown-identity.log binds module/sites/lock hashes. Exact producer/module/sites/resolver/SDK/compiler/config identities support artifact-specific reuse only. No new guest/runtime/packaged osctld proof follows. Earlier D81/207 OSVM and A99 shared-runner checks retained only unchanged source/bundle/native input scope, not rerun or relabeled.

## Compatibility, documentation and next runtime acceptance

Production owner Daemon and Self::Shutdown; consumers include startup resume, command client shutdown, independent abort and stage3 osctl. Internal run_shutdown is not a new wire API. Persisted marker modes000/100, existing client messages and protocol unchanged; joined clients may receive no intermediate progress. No coordinated fleet update or data migration. Code rollback reads same marker/state but restores old race risk. Restarting/upgrading a live daemon or deploying is not authorized.

Lasting invariants are explained in near-owner comments and contract tests; no new public option/workflow/error prose requires a product manual change. User-facing text inspected under writing skills: no added messages, reuse existing shutdown aborted. Session design/plan keep individual rollout and rejected alternatives; reviewer should assess documentation adequacy/placement too.

Current profile is original14400 (source SHA367dd4ce864b36c4807cb974857d7b58e22b18bb51343ad2724757132da12f2f). User-requested temporary300s patch saved separately package-c-diagnostic-aging.patch SHA c46380fdc1f05abd76fd975e25321d40ee2e37a15fdbcdb59c1ff42810554dde; none ships here. Next check has NO aging.

Third message has isolated TEMPORARY [skip ci] paragraph; exact message package-a-shutdown-commit-message.txt. Intended controlled route: after review pass, separately granted ordinary SSH feature publication then ONE workflow_dispatch with test_suite=ci/test_tag=ci/test_pattern=osctl/ct-passwd/prebuild=true/stop_on_failure=true. Existing nonempty-pattern workflow skips sites capture/all9 lifecycle and selects one group/default script. Require body+real graceful stage3+QEMU exit before timeout without cleanup TERM; retain inputs/logs. No blind retry or timeout increase. If pass: preserve tested/reviewed ref, separately authorized message-only amend removes skip directive, prove same tree/patch/prefix, lease expected own ref, then full exact-FINAL-head native+all9 with14400 and complete semantic/identity/recovery. Skip marker must not ship to default. This review does not claim current or historical VM pass. Runner updates remain operator-owned.

## Review assignment

Risk HIGH: host daemon shutdown/resource ownership and abort/recovery behavior. Apply general, architecture/repetition, scope/proportionality, risk/compatibility, each full lane reference. Eligible independent retained reviewer0, thread01a1a24e-920c-7b82-9fff-7754d1f947ab, gpt-6.1-sol/xhigh/read_only, fresh verified roster ready; no overrides/fallback. Perform directly without nested reviewer, no source/session writes, suites/build/eval/VM/network/CI/Git mutation. Report findings first, precise file/line/commit, residual gaps and explicit complete-history/repeated-stream/migration conclusion. Deliver full report via report_to_lead for root to save shutdown-fix-review.md. Routine technical clarification may use same-session D implementer2/architect0/A implementer0; consequential changes return to root. No review stamp predetermined.
