---
lifecycle: complete
---

# Codex package and portal settings state

Phase: complete. Implementation, independent review, verification, both
deployments and authorized remote default-branch integration are complete.
All four exact final feature heads are in their remote master branches and
their source worktrees are clean. No required work or blockers remain. New CI
was not awaited, as requested. The session, feature branches, normal worktrees
and retained deployment generations remain open/present; no archive or stop.

The upstream-reference follow-up is committed and merged as
4bec20165387d567b761e43b11fdeabb096618d7. Helper comments, package documentation
and its commit message link the upstream issues/PR and concrete removal criteria.
Its parsed Nix expression is unchanged. Retained reviewer0's actual native
gpt-6.1-sol/xhigh/read_only review found no new issues. Runtime/pins and the
verified deployment remain unchanged. See [integration.md](integration.md).

Codex 0.160.0 is live in the system and full consuming workspace package.
Ordinary CLI startup works without --no-daemon, and the native daemon's CLI,
managed package and actual server all report 0.160.0. Workspace services are
active with the expected executables and no pending Codex reconciliation.
Authenticated HTTPS with the existing local CA returns 200; deployed app.js
and style.css match the reviewed source. Desktop controls pass at 1280/1440px,
with mobile wrapping, saving/errors and Apply/Cancel preserved.

See [rollout.md](rollout.md) for deployed generations, acceptance evidence and
recovery limits. No blocking findings remain. Source branches are committed and
pushed and merged; tracking follows the normal initial-commit/working-tree cadence.

## Phase checklist

- [x] Diagnose installed 0.159.2 and missing package manifest/runtime files.
- [x] Confirm complete-package startup and desktop/mobile layout preferences.
- [x] Identify exact upstream issue and pending package PRs.
- [x] Create initiative and assign retained design/implementation members.
- [x] Commit initial plan/state and create dedicated feature worktrees.
- [x] Accept architect's design and verification brief.
- [x] Implement packaging, UI, pins and documentation.
- [x] Complete quick verification and independent whole-branch review.
- [x] Complete packaged/browser/protocol/state/daemon checks and aitherdev build.
- [x] Deploy system and user-profile application; verify live behavior.
- [x] Add requested upstream references and removal criteria; verify/review.
- [x] Integrate all four exact final heads into remote master; do not await CI.
- [x] Verify remote merge proofs and finish handoff, leaving the session open.

## Authorization and boundaries

User request: "Implement the plan." The accepted plan includes aitherdev system
deployment through vpsfree-cz-configuration and separate user-profile workspace
deployment. Preserve other initiatives and unrelated shared checkout changes.
No session was bound to this conversation at the start: environment identity
was absent and dev-session current returned "no current dev session found".
Create a separate dated initiative rather than adopting another session.

Follow-up integration authorization: "merge it into the default branches when
done. no need to wait for CI." This covers this initiative's four registered
repositories: dev-workspace -> master, vpsfree-dev-workspace -> master,
vpsfree-cz-configuration -> master and workspace -> master. Complete the narrow
upstream-reference follow-up and required review/quick checks first. Do not wait
for newly triggered CI. Approval does not include archive/delete/session stop or
branch deletion. Preserve the current deployment; documentation-only changes
do not require a new deployment.

## Initial evidence (historical, before implementation)

- Hostname aitherdev; system Codex and workspace-private Codex both 0.159.2.
- Upstream llm-agents.nix 0.160.0 revision:
  6334544a4bfd921086a252caccc6c1c6eb1d18c7.
- Existing installed package lacks codex-package.json and bundled rg and uses
  an escaping bwrap symlink. The same recipe remains in upstream main.
- Main, queue and thread-history SQL migration file hashes are unchanged
  between Codex 0.159.2 and 0.160.0.
- Upstream packaging issue #9887 and PRs #9889/#10132 are open and unmerged.
- No implementation, service changes or deployments yet.

## Next action

No action remains. When a selected upstream package provides the complete
daemon-copyable layout, follow the documented consumer migration and checks
before removing the workaround. Do not infer permission to archive, delete,
stop the session, restore real state, remove branches or prune generations.

## Current committed heads and CI

All four source worktrees are clean. See final-review.md for the complete
series, cleaned unpublished history and no-migrations inventory.

- dev-workspace: 4bec20165387d567b761e43b11fdeabb096618d7, merged into remote master;
  prior published/deployed runtime head40838aa remains intact;
  base 869b8d4728394127ba949dc76724dce56eae136b.
- vpsfree-dev-workspace: c56f981a950ab763b71dc91c59e8b5256d478851, merged into
  remote master; base 074926d33f7306288f7cfad87c6a85e8a430e750.
- vpsfree-cz-configuration: 028d70b233c5b100fea7f7aa0b945fb8b6d3ec4d, merged into remote master;
  base 2758415cc11d719f22b341cee4e8e77c773c141f.
- workspace: c5d8bed5fcd3bc01ce18831ea680aac7edfd68ee, merged into remote master;
  base 98389138caef0576dfa7a101d1dbcdbae943b0af.
- Exact extension/generic/runtime lock graphs agree; consuming-workspace
  deployment-contract checker passed. Generic/extension/workspace no-build
  flake evaluation passed; application/configuration quick checks and hooks
  passed. Both system and full consuming application deployments are verified.
- Provider CI 36999356818 passed on exact408 (5m59s); extension CI 36999495059
  passed on exactc56 (13m09s). Fresh monitor_provider_ci retained full logs.
  The extension's logged graceful-stop timeout is the deliberate stuck-poweroff
  fixture in devcluster_runner_test.rb, followed by zero failures/errors.
  Non-failing Git identity diagnostics appear in the packaged fixture suites;
  exact fixture attribution is not established. CI success does not establish
  deployment or browser geometry.
- Final reviewer0 turn 01a0fc55-b7f0-7ad0-8b2e-c6c70b83b08d completed with
  retained gpt-6.1-sol/xhigh/read_only, all four lanes. Report identity:
  610c839c-3a43-4054-9ed2-cc71b9482e9d. See final-review-result.md.
- Fresh SSH fetch/ancestry checks confirm each exact final feature head equals
  its remote feature and is an ancestor of remote master (currently equal).
  All four source worktrees are clean. Shared checkout remains master at
  c5d8bed5; pre/post binary-diff hashes prove unrelated worktree/index changes
  were preserved. Only temporary detached integration checkouts were removed,
  non-force; their contents are recoverable from the retained Git objects.

The new generic commit changes only top-level Nix comments and package documentation;
pre/post parsed Nix SHA256 is identical:
a0814fa30db39602922efb3ea7438fb467bc8a78d0d71cb7be5572534dedd51e.
Commit message and both source locations contain the three upstream links and
retirement criteria. This separate commit preserves the externally consumed
assembly history; no obsolete implementation or migration was introduced.

## Documentation

- [Generic package contract](https://github.com/aither64/dev-workspace/blob/4bec20165387d567b761e43b11fdeabb096618d7/docs/codex-package.md):
  runtime layout, consumer ownership, native updater independence, store
  retention, verification, forward recovery and upstream workaround retirement;
  linked from README/dev sessions.
- [Aitherdev operations](https://github.com/vpsfreecz/vpsfree-cz-configuration/blob/028d70b233c5b100fea7f7aa0b945fb8b6d3ec4d/docs/operations/codex-deepseek-aitherdev.md):
  shared system/wrapper assembly, separate workspace profile, version checks
  and retention/recovery, linked to the authoritative generic contract.
- Design, review results and this rollout remain separate session records.
  Reusable probe, queue, GC-root, selected-helper and local-CA lessons are in
  notes/dev-workspace. Private SQLite/TUI evidence stays outside Git/portal.

The earlier implementation checkpoint below records superseded unpublished
heads; the exact heads above are authoritative for verification/deployment.

## Initiative and team

- Initial records: 98389138 on shared master (tracking only).
- Created root thread: 01a0fc1b-bcd2-7060-901a-f47950131bd3.
- Stable URL: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-02-codex-package-portal-settings/
- Verified identity with complete DEV_SESSION_SLUG/DEV_SESSION_WORKSPACE for
  dev-session current after successful creation.
- Retained delegated catalog digest:
  4676433c6831fbaca91da8ffde84891aff6ce065a17c74c2f367f1acf1d15b17.
- architect0: design, gpt-6-astra/xhigh, workspace_write, ready; assigned
  design.md before substantive packaging implementation.
- implementer0: implementation, gpt-6.1-sol/xhigh, workspace_write, ready;
  assigned the localized UI fix directly under the bounded-edit exception,
  followed by generic package/configuration implementation from design.md.
- reviewer0: review, gpt-6.1-sol/xhigh, read_only, ready; provider and final
  independent review completed.
- Fresh prepare_codex_dependency utility: gpt-6-luna/low, dependency realization
  and configuration shell preparation; logs remain in this initiative.

## Worktrees

All feature branches are named 2026-10-02-codex-package-portal-settings under
worktrees/2026-10-02-codex-package-portal-settings/:

- dev-workspace: base 869b8d4, registered.
- vpsfree-dev-workspace: base 074926d, registered.
- vpsfree-cz-configuration: base 029c616e, registered after preparing the
  declared Nix shell and retrying the post-checkout hook. Hooks remain enabled.
- workspace: base 98389138, registered; shared checkout remains on master.

## Setup findings

The starter requires a goal file in noninteractive use. Explicit --team cannot
be combined with pre-existing committed tracking. Preserved tracking was
initialized without --team, then the documented team preset command installed
the delegated roster. Startup recovered an App Server disconnect and completed;
the retained records were preserved. No unrelated session was modified.

## Preparation verification

Fresh watcher prepare_codex_dependency completed both assigned operations:

- `nix build --accept-flake-config --no-link --print-build-logs --json
  github:numtide/llm-agents.nix/6334544a4bfd921086a252caccc6c1c6eb1d18c7#codex`
  passed, exit 0; cached Codex 0.160.0 is available. See dependency-codex.log.
- `nix develop --command true .` in the configuration worktree passed, exit 0;
  the declared tools/gem environment is ready. See configuration-shell.log.

No kernel build, source edits or deployment occurred in these operations.

The initial unrooted Codex output subsequently disappeared. A fresh
retain_codex_input watcher realized it again with the initiative-owned
prepared-codex link (exit 0, binary-cache substitution). See retained-codex.log
and notes/dev-workspace/2026-10-02-root-codex-probe-inputs.md. A separate fresh
prepare_verification_tools watcher realized the pinned Go, Node, Ruby,
Playwright and nixfmt tools (exit 0; verification-tools.log).

## Historical implementation checkpoint (superseded unpublished heads)

- Generic UI: cf84da79735a280a060653e28d3ad803e5eb3587. Dirty text removed,
  saving/errors below controls, desktop-local sizing, expanded existing
  browser regression. No settings API/storage change.
- Configuration llm-agents channel: 435a4e60, exact 6334544a revision;
  generated confctl commit, Overcommit pre-commit/commit-message hooks passed.
- `node --check` for app.js and team_settings_browser_test.cjs passed in the
  declared Node shell.
- Focused Go template/sidebar/live-authority tests passed in the declared
  Go/stdenv.cc shell (0.116s). Initial Go-only shell failed before tests because
  gcc was absent; the compiler shell resolved it.
- Package source, site consumer and documentation are still in implementation.
  Generic assembly and docs are now committed at c1bb968d; the site functional
  commit is pending its declared hook environment.
- Generic dependency-only commit: 0f67f70ed5b91f99d9350eb85eb0e404e8513414.
  Shared-index coordination initially picked up staged new files, corrected
  immediately in the unpublished commit without changing any file content.
  The implementer owns the generic index from this point onward.
- Generic Nix parse checks and `nix flake check --no-build --show-trace` passed.
  Required llm-agents transitive locks changed; primary generic nixpkgs/client
  pins remained unchanged.

## Independent review

Provider publication review is assigned to verified retained reviewer0
(gpt-6.1-sol/xhigh, read_only), all four mandatory lanes, high overall risk.
See provider-review.md for full base-to-head series, final-diff scope,
documentation, consumers, non-goals and explicit no-migrations inventory.
This is a provider gate before feature publication/automatic CI, not the final
cross-project readiness review. No integration tests or deployment completed.

Provider review completed: one Important UI intermediate-width overlap finding,
no Blocking or other findings. See provider-review-result.md. Implementer0 is
remediating the scoped CSS/test issue and folding it into the unpublished UI
owning commit. No package/security defects, obsolete history or migrations were
found. A narrow remediation is verified directly; final cross-project review
still follows pin propagation.

Configuration upstream advanced to 2758415c through scheduled input updates.
Rebased the consumer-only patch onto it; range-diff proved patch equivalence:
6f3efd09 -> 80a5a5c2. Recreated the exact llm-agents pin with confctl as 81ac31c2
(hooks passed), removing obsolete unpublished pin history. Upstream scheduled
system input updates are now the deployment base; our feature diff remains
Codex source/pins and related docs only. Generic/extension default bases did
not advance; workspace branch was checked against current shared master.

## Cutover safety preparation

Architect clarified the online per-database baseline and safe forward recovery
in design.md. Accepted: no claim of global snapshot or lossless state rollback;
no manual freezes/other-session interruption or restoring old DBs over writers.
The baseline will run before the first candidate command using live state,
after disposable checks pass. sqlite_baseline.py implements that planned method;
no baseline has run yet. All 73 upstream SQL files have matching paths/blob
hashes across 0.159.2 and 0.160.0 (verified tree inventories are nonempty).
compat_probe.go and daemon_probe.py are prepared disposable rollout probes;
only the Go harness has been compiled, not executed.

## Local integration execution

Fresh verify_codex_rollout watcher completed the first verification batch with
exit 1. Full consuming workspace built as
/nix/store/9g8wd2fppjgq1bvcwkscsbp5r1wb9yk9-dev-workspace-0.2.0 and is rooted
by candidate-workspace-package. Packaged tests, consuming flake checks and
review-asset checks passed. Codex assembly's closure was queried and launcher
reports 0.160.0. See verification-local.log.

Browser test stopped before any UI exercise: Cannot find module @playwright/test.
Lead inspected pinned nixpkgs driver.nix: playwright-driver is core-only and
installs at its output root; playwright-test provides the expected
lib/node_modules/@playwright/test and matching browsers. Corrected the
session-owned verification script to use the pinned playwright-test with a
retained out-link, plus a retained browser link. Existing workspace notes
2026-09-14-playwright-gc-root.md and 2026-09-14-playwright-full-chromium.md
confirm the intended environment. This was a verification setup error, not a
tested UI defect; no application revision changed. Protocol/state/daemon
probes were not reached. A new watcher will own the corrected batch and retain
its separate log; the failed evidence is preserved.

Fresh verify_codex_rollout_corrected completed verification-local-2.log with
exit 2 (about 74 seconds). Browser passed all seven widths and controller
transitions. Generated protocol check reported compatible 0.160.0. The state
probe stopped before its synthetic create body because its actual-executable
version assertion used CombinedOutput and included Codex's expected stderr
warning about refusing helper aliases beneath /tmp. Lead inspected the exact
panic/output: stdout version was 0.159.2, not a wrong reader. The harness now
captures stdout via Output while retaining stderr in its private log, preserving
both exact-version and nonzero-exit checks. This changes diagnostic-stream
handling, not application behavior or compatibility criteria. State and daemon
execution gates remain pending; no live-state cutover occurred.

## Accepted design

Fresh verify_runtime_and_host stopped with exit 2 after 17 seconds; see
verification-runtime-3.log. The old 0.159.2 fixture auto-dispatched the queued
message because its thread was loaded and idle. The private old-create.log
shows an unauthenticated model attempt rejected with HTTP 401; no real state or
credentials were used. This is not an upgrade incompatibility. Upstream queue
service enqueue calls wake_if_loaded, whereas add/list on a persisted unloaded
thread use its store without loading it. The fixture now uses a separate queue
thread, stops the first old server before enqueue, and never resumes that thread
in any reader. Queue preservation remains required across old/new/old readers;
all synthetic rollouts must also contain no task_started event. Daemon JSON
commands now retain stderr separately, like the corrected executable-version
assertion. These are bounded verification-harness corrections; source heads and
reviewed application contracts are unchanged. Failed evidence is retained.

Fresh verify_runtime_and_host_unloaded_queue then stopped with exit 2 in four
seconds; see verification-runtime-4.log. Queue creation on the unloaded thread
passed. The new reader reported reasoningEffort null for the other thread after
resume, whereas the creating old reader had reported high. Architect0 owns the
bounded diagnosis of whether thread/start's runtime config was persisted; no
compatibility assertion is relaxed and deployment remains gated. A separate
fresh build_aitherdev_codex160 watcher owns the authorized host-only build so
this diagnosis need not block independent build preparation.

The first host build stopped at confctl's confirmation prompt with EOF before
building the machine (verification-host-build-1.log). Inspected the exact pinned
confctl CLI: build/deploy accept --yes. Use that documented noninteractive flag
for already-authorized, exact-aitherdev operations; do not widen the target.
The prepared deployment script is corrected before launch. Runtime verification
and the host build now have separate watchers/logs.
The existing reusable note notes/confctl/2026-07-21-noninteractive-build-confirmation.md
already records this requirement; no duplicate note is needed.

Fresh build_aitherdev_codex160_noninteractive passed with exit 0 after about
1m56s, creating confctl generation 2026-10-02--14-04-08 and toplevel
/nix/store/zg389q4q7hcxxl7agg0y5nxdb3xpcz4h-nixos-system-aitherdev-26.05.20261001.4feb8eb.
Parent checked the generation, realized toplevel and system launcher 0.160.0.
The watcher retained only command-session excerpts in verification-host-build-2.log;
the announced confctl full-log path is absent. Do not treat that artifact as a
complete build transcript. No local kernel compilation was reported. Further
operations use prepared wrappers that redirect before launch and write atomic
exit-status artifacts, rather than relying on reconstructed watcher logs.

Failure location clarification for verification-runtime-4.log: compat_probe.go:178
is the newly forked thread, not the initial resume of the original. The original
old high setting was read successfully by 0.160.0 and changed to medium. The
architect is assessing the fixture's unsupported assumption that a fork
inherits the parent's runtime reasoning setting. The disposable daemon checks
for both assembled consumers are separately monitored by verify_both_codex_daemons.

Architect0 confirmed matching old/new fork behavior and documented the exact
source evidence in design.md. Accepted the bounded fixture correction: explicit
fork model/medium config, plus a cold old-reader high assertion before upgrade.
Every content/settings/queue/version/integrity criterion remains mandatory.

Both-consumer daemon operation passed with status 0 in 16 seconds; see complete
verification-daemon-1.log and atomic .status. It proved ordinary plain/resume/fork
startup, complete copied packages, restart, and separate cliVersion,
managedCodexVersion and live appServerVersion 0.160.0 for both closures. The
watcher's reported shared coordination HEAD is not the application revision;
the script guarded generic408/full-consumer9g and selected bundled a29/system53p.
Normal daemon stop leaves its pid-update-loop worker running. Parent identified
two workers by exact private executable paths, UID and command. Account for and
stop only these owned private workers; add strict home/SQLite-home/PID-fd guards
to fixture cleanup. No shared Codex server or updater is targeted.

Parent stopped the two proven private updater workers with PID-fd handles after
checking their exact executable, arguments, UID and both isolated home variables.
No matching workers remain. The cleanup helper skips unreadable unrelated
processes but fails on inspection errors after matching the owned private root.

Fresh verify_old_new_old_explicit_fork passed, status 0, in about four seconds.
verification-runtime-5.log proves actual old/new/old executable identities,
cold old high settings, new medium settings and explicit-medium fork, preserved
queue across all readers, integrity of six private SQLite stores, and absence of
task_started events in every synthetic rollout. No source head changed. The
only remaining execution phase is live baseline/deployment/verification.

Live online baseline completed 12:15:10–12:15:29 UTC, status 0. Seven SQLite
stores, 2,958,974,976 bytes, all integrity ok. Private destination:
/home/aither/.local/state/dev-workspaces/backups/2026-10-02-codex-package-portal-settings/online-9_h0m65v.
Directory 0700, complete manifest 0600, owned by aither. Parent independently
checked the manifest, status, actual artifacts and all SHA-256 checksums.
The watcher's claim that artifacts were absent is contradicted by these direct
checks; rely on the authoritative filesystem/status, not that observation.
This remains a per-database baseline, not a global snapshot or state rewind.
No real candidate state access preceded it.

Prepared system deployment now selects the already-built confctl generation
2026-10-02--14-04-08 explicitly, preserving the exact configuration HEAD and
target guards. The generic/llm input revisions in its metadata match408/633.

First detached dry-activation attempt refused before confctl: the literal PATH
omitted /home/aither/bin, which contains the stable dev-session/workspace-host
commands. Unit codex-package-portal-system-dry-activate-20261002 failed, status 1;
no configuration activation ran and selected system/profile remain old. Parent
resolved exact command locations and added the verified literal directory to
both launch scripts. Preserve failed log/status under preflight-path-failed
names before a fresh unit observes the same supported dry-activation command.

Corrected dry-activation unit completed with status 0 on exact generation
2026-10-02--14-04-08. The selected system/profile remain old, as expected.
Pinned confctl deletes its successful internal logger file (cli/command.rb);
its redirected stdout is retained but omits the underlying activation plan.
Parent ran the same exact NixOS dry-activate entry over BatchMode SSH to the
already verified aitherdev IP and captured exit 0 plus the plan: reload
dbus-broker, restart home-manager-aither and nginx. No other service restart
was listed. Old/new kernel paths are identical (Linux 6.18.54). Accepted the
brief nginx interruption and expected home-manager activation for this scoped
host rollout; no fleet update or reboot is planned.

System switch completed with status 0 at 12:25:30 UTC; both confctl health checks
passed (2/2). Parent verified /run/current-system and system profile select
zg389..., system codex reports 0.160.0, codex-ds strict-config help exits 0,
and no failed system unit is listed. Workspace application remains on z20...
with its old159 runtime pending the separately authorized full profile switch.
No reboot occurred. Previous system/profile generations remain retained.

codex-ds is a Home Manager user-profile command, not /run/current-system/sw/bin.
The first absolute-path lookup missed it; parent then verified the real command
/home/aither/.nix-profile/bin/codex-ds strict-config help exits 0. This did not
require a configuration or source change.

First full workspace switch selected candidate9g/profile generation79 and then
reported registration semantics failure, status 1 (workspace-switch.log).
Parent inspected source and exact live evidence: the older initiating helper's
final check compares its old @system_codex path, while candidate activation
reconciles to bundled newa29. The marker correctly names new9g/a29; actual
App Server executable is a29 native160 and portal executable is new9g. Pending
record was cleared by successful selected-package reconciliation. Preserve the
failed evidence and selected forward generation. Retry the same supported
source switch via the stable dispatcher, now executing from selected9g, with
exact selected-profile guards and separate retry artifacts; no manual relinks,
older package revival, marker changes or busy-session override.

Selected-forward retry completed with status 0 at 12:32:46 UTC, selecting the
same profile generation79/new9g with active assembleda29 Codex 0.160.0. See
workspace-switch-retry.log. Normal lifecycle/cluster/quiescence/registration
checks passed; no forced interruption, state restoration or manual marker
change was used. Final live CLI/native-daemon, process identity and HTTPS
reachability checks follow. All four source heads and reviewed branch histories
remain unchanged.

First live startup probe reached the OpenAI Codex header but quit its own TUI
after about half a second. The subsequent native version query reported missing
app-server-control socket (verification-live-1.log/status1); the daemon had not
finished bootstrapping. This probe's header marker was earlier than its readiness
criterion. Keep the TUI alive while polling the normal read-only daemon version
until all three exact160 fields and running status are confirmed, then terminate
only the owned TUI. Preserve private failure evidence outside Git/portal. No
model prompt, service restart, forced daemon selection or assertion relaxation
is introduced by this narrow harness correction.

Corrected live CLI probe passed in verification-live-2.log: ordinary startup,
running native daemon and all three exact160 fields, followed by expected
workspace units/processes and absent pending record. That batch ended with
status60 because its last curl used the generic CA bundle. It also omitted
the portal's existing authentication. Parent confirmed the unchanged host
module uses the local Workspace Development CA and nginx Basic Auth. No
certificate or authentication change was required.

Separate known-quick verify-portal.sh passed, status0, at 12:47:26 UTC:
authenticated stable URL HTTP200, TLS verification0 using the existing public
CA, live app.js/style.css byte-identical to reviewed source, and removed dirty
notice absent. Credentials stayed on curl stdin, never argv/logs/files. Failed
batch statuses are retained honestly; this supplemental check completes the
HTTPS/asset gate without rerunning the already-passed CLI checks.

Final retention query confirms old/new system generations155/156, full workspace
profiles78/79 and Codex generation roots78/79 remain present. Both new assembled
outputs are rooted through their consumers; no generation or GC root was
removed. The earlier failed workspace deployment unit remains as historical
failed-job status, not an inactive application service. All four reviewed
source heads remain unchanged and match their remote feature refs.

See [design.md](design.md). The shared assembly reuses cached binaries, preserves
ELF dependencies and materializes helpers within the runtime root. Existing GC
roots/system generations retain closures needed by upstream daemon copies.
No source patch or state migration is introduced. Long verification includes
disposable old/new/old state loading and separately verifies daemon selection.
CSS empty-status hiding is accepted as equivalent to toggling hidden, provided
saving/error transitions remain visible and regression coverage proves it.
