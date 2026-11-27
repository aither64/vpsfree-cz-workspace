---
lifecycle: archived
---

# nodectld minimal mode and watchdog recovery

## Current phase

Merged into remote `vpsadmin/master`. Final head is
`a8ef7163832f3c246bb3927f00d68dd5a001818b`. The retained independent
reviewer reports no outstanding findings after checking the full three-commit
series and the runtime-discovered stop parser correction. All quick checks and
declared hooks pass; the final packaged watchdog scenario, all three local
regression scenarios, and the broader GitHub integration workflow passed.
The user authorized implementation and explicitly
included DNS servers and all NixOS/systemd nodectld instances. Production recovery
was performed by the user. The user authorized the merge conditional on passing
specs; that condition passed and integration is complete. Deployment remains
outside the authorized scope.

Worktree: `worktrees/2026-11-27-nodectld-minimal-watchdog/vpsadmin`, branch
`2026-11-27-nodectld-minimal-watchdog`, base
`99207a8dcd92f5907c52dbc99af52b30aa7ecac1`. Creation checked out the worktree
but its post-checkout hook refused an unsigned Overcommit configuration. The
declared hooks were inspected, signed and installed in the root Nix shell;
repeating worktree registration then succeeded without bypassing hooks.

- [x] Read-only central-log/source/monitoring investigation.
- [x] Confirm the user's restart restored transaction processing.
- [x] Create tracking after explicit authorization.
- [x] Prepare the implementation and verification brief.
- [x] Implement the two fixes and focused regression coverage.
- [x] Quick checks, committed deliverables and independent final review.
- [x] Packaged watchdog, DNS and standard/runit integration tests.
- [x] Broader GitHub integration CI.
- [x] Authorized master integration and exact remote-head delivery proof.
- [ ] Automatic post-merge workflow results (separate runs on the same commit).

## Authorization and ownership

The user initially said "no tracking" and requested logs for vpsadmin1. No
tracking records were created until the later message: "okay i've killed it.
prepare an implementation plan to fix the issues: the requirement of osctld and
the missing watchdog, it's there for a purpose. you can start tracking this
session." The later "yeah implement it" authorizes implementation and requires
the watchdog across all NixOS/systemd roles, including DNS. Neither message
authorizes deployment or default-branch integration.

`dev-session current` initially found no current initiative, and neither identity
environment variable was set. Created the new tracking-only session with
`dev-session start 2026-11-27-nodectld-minimal-watchdog --as-is --no-codex
--no-attach --json`; creation returned this exact slug, a null threadId and the
portal URL below. A subsequent current check with both newly created identity
values set returned this slug. No other initiative was adopted.

There is no retained Codex roster: team listing reports no valid lead Codex
thread for this tracking-only session. No team was invented or reconfigured.
The conversation lead owns design and implementation; standalone review and
verification utilities follow the installed policy described below.

## Incident evidence

Times below are 2026-11-27 CET, as recorded by the central logger.
Source: `log.int.prg.vpsfree.cz`,
`/var/log/remote/cz.vpsfree/vpsadmin/int.vpsadmin1/log`.

| Time | Observation |
| --- | --- |
| 03:19:39 | ExportMounts worker raises because `osctl -j ct ls --state "running"` cannot connect to `/run/osctl/osctld.sock`; the process exits with failure. Similar failures recur every six hours on prior days. |
| 03:19:45 | systemd starts PID 2401122. |
| 08:38:20 | Last completed chain before the gap: chain 13080125, transaction 75024103. |
| 08:44:30 | User identifies the first stuck transaction. Monitoring later shows oldest queued chains 13080126 and 13080127. |
| 09:19:46 | The same export-mount exception occurs, but PID 2401122 stays alive and continues status updates. |
| Before restart | Prometheus reports running=1, paused=0, initialized=1, zero used mail slots and zero mail reservations. No SMTP timeout or MySQL error appears in the relevant host-log window. |
| 12:46:05 | systemd logs that it is stopping nodectld; status updates continue. |
| 12:47:35 | Old process exits with signal 9/KILL. User confirms having killed it. Do not attribute the kill to automatic systemd escalation merely because 90 seconds elapsed. |
| 12:47:36 | New daemon PID 2440771 starts. |
| 12:47:38 | Oldest stuck chains 13080126 and 13080127 close. |
| 12:48 onward | Backlog chains continue closing; 62 chain closures were observed through 12:50:04. End-to-end delivery of every message was not independently verified. |

The final Prometheus query, after the initial tracking commit, returned no
`vpsadmin_transaction_chain_queued_seconds` series. Earlier samples still showed
63 pending chains while the exported view caught up with processing.

The daemon was running libnodectld 4.2.1 from store item
`f4sns0vs32b2kl7zrz9icdrpivzvmpw8-ruby3.4-libnodectld-4.2.1`.
The host is a NixOS mailer inside a vpsAdminOS container; the absence of osctld
inside it is expected. The recurring osctl error is a minimal-mode defect,
separate from the earlier transaction stall.

The symptoms strongly indicate a blocked main transaction loop with healthy
background/control threads. No pre-kill backtrace was captured, so the exact
blocking call and initial trigger remain unconfirmed. Do not present a mysql2
deadlock as established fact.

## Sources and checks

Fetched and inspected vpsadmin `origin/master`
`99207a8dcd92f5907c52dbc99af52b30aa7ecac1` and configuration `origin/master`
`2f264616638f4baa464692c02bea9ea76d7ffdde`.
The bare vpsadmin HEAD was older; final planning uses origin/master explicitly.

Relevant sources: AppConfig minimal-mode override, Daemon initialization,
ExportMounts/VpsOsRelease enable checks, CLI wrapper/watchdog exit paths, NixOS
and vpsAdminOS service modules, current watchdog/config/export specs, and the
existing services/mailer/Mailpit fixture. The current NixOS service combines
`--no-wrapper` with `Restart=on-failure`. The wrapper's watchdog stop path can
exit successfully, so enabling the wrapper also requires service restart-policy
coverage.

Read-only access to the central logger and documented Prometheus route worked.
Direct SSH to vpsadmin1 was denied for the available key. Investigation did not
change production state. The initial planning checkpoint had no application tests
or independent review; implementation verification and review are recorded below.

Workspace has unrelated changes; preserve them and stage only this session's
three Markdown records plus its portal manifest. No hook framework or active
pre-commit/commit-msg hook was declared/found in the coordination repository.
Initial tracking commit `63e56f5827fd95f55c896a06e965259cc09f8785` was created
on shared master after fetching origin, confirming linear ancestry and an empty
shared index, and acquiring the shared tracking lock. It contains only this
session's four files. Document whitespace, relative links, active lifecycle
front matter and the staged diff passed quick checks. This post-commit receipt
is kept in the working tree under the normal tracking cadence. Project hooks
were subsequently installed and used for all application commits.

## Implementation checkpoint

The minimal-mode policy now disables export-mount and VPS OS-release services.
The common NixOS module runs the existing wrapper with `Restart=always`,
`KillMode=mixed` and a 90-second systemd stop deadline. This covers all roles;
the runit module and production watchdog thresholds are unchanged.

Focused specs cover mode load/reload and disabled service construction/updates.
The new `admin/nodectld-minimal-watchdog` scenario uses the actual packaged
mailer and DNS service, test-only timer acceleration and a deliberately blocked
polling loop. It covers real queued mail and DNS reloads, stale polling with a
responsive control thread, an unresponsive child, crash/restart/stop behavior,
and manual service-manager stop. After review correction it also checks sustained
pause/resume, and long integration execution is now in progress.

The first focused RSpec attempt failed before examples: shared
`/tmp/dev-ruby-gems` contained ActiveRecord installation metadata but lacked
`active_record/base.rb`. No source/dependency change is indicated. The next run
uses `/tmp/nodectld-minimal-watchdog-gems` outside the packaged source, preserving
the declared Nix shell and native Ruby extension path. See `quick-checks.log`
and `isolated-specs.log`. The cache is disposable session-owned data. Existing
workspace notes already document this failure and isolation workaround.

Initial quick checks passed: the first focused RSpec run had 18 examples, zero failures
(`final-specs.log`); changed Ruby files pass RuboCop; CI selector tests pass
16 cases / 55 assertions (`lint-selection.log`). Nix parsing and full scenario
evaluation pass; `test-config.json` retains the evaluated guest paths/script.
Changed Markdown links resolve and `git diff --check` passes. Nixfmt formatted
the touched modules/test. The first lint run found only spec-style offenses;
those were corrected before the final passing checks.

CI tag listing includes the new scenario; evaluated Ruby syntax passes after
preparing API dependencies for the mandatory i18n commit hook. First application
commit: `e9a527675` (minimal-mode policy and regression specs), all declared hooks
passed. An initial split-commit attempt could not prepare Overcommit's staged
view while new files had intent-to-add entries. Removing only those entries
preserved their contents and allowed the normal hook flow. See
`notes/vpsadmin/2026-11-27-overcommit-intent-to-add.md`.

Selected post-review integration batch: the new mail/DNS watchdog scenario,
`dns/server-zone-lifecycle`, `admin/nodectl-read-and-queue-control`, and
`admin/nodectl-refresh-and-runtime-state`. Expected tens of minutes including
guest builds/boots; disposable state at `/tmp/nmw-20261127`; stop scheduling after the first unexpected failure and
investigate before a targeted rerun. The new mail case already captures actual
SMTP delivery, so an unrelated daily-report smoke adds no necessary coverage.

Verification uses standalone fresh Luna/low watchers under the monitor skill;
the installed package is
`/nix/store/4d0iy6lkl1jq9nngi9mkf3mb2ydj6vxi-dev-workspace-0.2.0`, catalog
`1184a2cf511b6e77ff7afe12433027abe06e8bb0b897f39cffc26efd443d1a7c`,
execution policy `full_access` / approval `never`. Runtime monitoring is not
exposed to this tracking-only conversation; the parent remains active.

## Documentation and next action

- [Plan](plan.md): scope, packages, compatibility and delivery sequence.
- [Design and verification brief](design.md): concrete minimal-mode and systemd
  changes, acceptance criteria, focused checks, rollout and recovery.
- Product runbook: `vpsadmin/docs/operations/nodectld.md`, linked from the docs
  index and transactions page; minimal mode, watchdog timing, service-manager
  controls, diagnosis and recovery limits.

Initial reviewed head: `84cc09332fc09e3178405df34539cbd4c1d20a46`.
Both logical commits passed declared hooks; see [review packet](review-packet.md).
This head is the initial reviewed revision, not the final corrected head.
Review findings and dispositions are in [review](review.md); the design addendum
explains the extra loop-progress clock. Existing real-poll timestamps remain
unchanged, watchdog status/debug gain one additive field, and the wrapper falls
back to the old field for older responses. The original no-RPC-change design
is superseded by this compatible additive status change. No schema/API changes.
Published final candidate: `a8ef7163832f3c246bb3927f00d68dd5a001818b`.
Next action: inspect automatic post-merge workflow results; production deployment requires separate direction. The two reliability defects remain in production
after the user's recovery restart.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-27-nodectld-minimal-watchdog/

## Retention

The registered feature worktree remains active. Dispose of the isolated external
gem cache and owned test artifacts after verification; preserve compact results.
No production service or development cluster was created. Keep the session active;
no archival or deletion was requested.
Creation CLI note: `--as-is` and `--new` are mutually exclusive. The rejected
first invocation created nothing; retry with `--as-is` alone succeeded.

## Publication and integration execution

Published the reviewed head `258a62e4ac7234639aecebf6cdce726ef9c5fcd7` over SSH to
`origin/2026-11-27-nodectld-minimal-watchdog`. Fresh origin/master remained the
recorded base. No PR, default-branch integration or deployment.

The fresh `/root/integration_batch` watcher owns `run-integration.sh`, retaining
full output in `integration.log` and native test state under `/tmp/nmw-20261127`.
Installed Luna/low utility policy is unchanged. It must stop an unexpected local
kernel build and report the derivation; no kernel change is intended.

GitHub runs for this exact head: RuboCop `46001498055`, libnodectld Specs
`46001498167`, integration CI `46001497953`, initially in progress. Runtime CI
monitor tools are unavailable and the one utility watcher is occupied by local
integration, so the active parent uses bounded read-only GitHub checks.

RuboCop CI `46001498055` and the full libnodectld Specs run `46001498167`
completed successfully at the published head. The full spec suite ran 510
examples with zero failures. Integration CI remains in progress.

First integration attempt failed before examples, after guest image builds:
`TestEvaluator` raised `undefined method let`. This runner implements describe/it
but not RSpec's let DSL. Corrected the single fixture binding to the ordinary
local variable used by the surrounding role iteration. No product behavior or
reviewed design changes. Nix parsing and diff checks pass; normal commit hooks
and a fresh batch rerun follow. Full evidence: `integration-batch.log` and
`/tmp/nmw-20261127/os-test-admin__nodectld-minimal-watchdog-7cec6e1c/test-runner.log`.
The watcher and all owned command/guest processes ended. No runtime acceptance
assertion executed, so this failure provides no runtime result for the fix.

Corrected test head `f3a74127a30fffc9d14a26100636ce2cfed91110` passed all hooks
and was published with an exact old-head force lease. Superseded integration
CI `46001497953` was canceled after the push. New exact-head runs: RuboCop
`46002774224`, libnodectld Specs `46002774246`, integration CI `46002774278`.
The fresh local rerun uses `run-integration-r2.sh` and `/tmp/nmw-20261127-r2`;
the first failure log is retained separately as `integration-first-runner.log`.

The new native watcher dispatch became unavailable in the current tool turn;
reported this limitation and used the monitor skill's active-parent fallback.
Parent exec session `31610` owns the r2 batch, with full output in
`integration-r2.log`. No second watcher or duplicate run was launched.

R2 runtime milestones: guest/API startup completed; the mailer minimal-mode
periodic/refresh/delivery example passed, followed by sustained pause and explicit
resume with queued mail delivery. Stale-poll recovery is now executing. Current-
head RuboCop and full libnodectld CI passed; integration CI remains in progress.

## Runtime verification and stop-command correction

Local r2 at `f3a74127a30fffc9d14a26100636ce2cfed91110` finished with exit 1
on 2026-11-27 at 14:13 CET (973.48 seconds). Twelve of fourteen examples passed:
minimal-mode initialization/periodic/refresh and queued delivery; pause/resume;
stale polling with responsive control; SIGSTOP recovery; child crash/restart;
and explicit systemd stop/start, for both mailer and DNS. Both hang cases used
the production 60-second TERM-to-KILL escalation. Only the two `nodectl stop`
examples failed, each before sending any request, with a NameError caused by
`Stop#options(_parse, _args)` referring to `parser` in the body. The method
parameter is corrected to `parser`; no shutdown semantics change. This restores
an existing operational command required by the reviewed lifecycle contract.

The focused real CLI parser check passes default stop, `--force`, `-f`, and
`--help`, with remote execution intercepted to avoid a service mutation. Targeted
RuboCop and whitespace checks pass. Evidence: `stop-parser-check.log` and
`check-stop-parser.rb`. The fix is a separate logical commit because it repairs
a pre-existing CLI defect, independently revertible from systemd supervision.

The r2 runner and its parent exec session `31610` are finished. Subsequent node
and DNS regression scripts were not launched because the batch stops after an
unexpected failure. Compact failure evidence is retained in `integration-r2.log`;
raw guest evidence remains in `/tmp/nmw-20261127-r2` until final cleanup.

The stop parser correction is committed as
`a8ef7163832f3c246bb3927f00d68dd5a001818b` after all declared hooks passed.
Fresh fetch still reports the original origin/master base. The retained independent
reviewer was assigned the affected general/CLI compatibility lanes and complete
three-commit series; the existing architecture/scope design is unchanged.
A fresh final batch will use `/tmp/nmw-20261127-r3`, the corrected immutable
source, and the same four acceptance/regression scripts. Successful evidence
from prior heads is retained with its actual revision, without claiming final-head
runtime success before the new run.

Final candidate was published normally over SSH (no rewrite needed). Push from
the ambient environment hit an Overcommit signature-environment mismatch;
repeating the same push in the declared root Nix shell passed the hook without
changing signatures or bypassing verification. Final CI: RuboCop `46005898709`
and integration `46005898765`; no new libnodectld run is selected for the CLI-only
follow-up. Full libnodectld success at the unchanged component revision remains
`46002774246`. Superseded integration `46002774278` was canceled only after the
new head was published. Runtime monitor registration remains unavailable.

Fresh `/root/integration_final` watcher, gpt-6-luna/low, owns `run-integration-r3.sh`
under the unchanged installed catalog/utility/full-access policy. The lead remains
active and does not duplicate local log polling. All prior exec command sessions
are finished. Expected completion is tens of minutes including guest builds and
real watchdog escalation; a failure stops the batch and returns evidence for
diagnosis. The final scenario and the three existing regressions are the bounded
remaining local acceptance batch.

RuboCop CI `46005898709` passed at the final head. Fresh SSH remote proof matches
`a8ef7163832f3c246bb3927f00d68dd5a001818b`. The ambient/Nix Overcommit mismatch is
already documented in `notes/vpsadmin/2026-09-15-plugin-rake-database.md`; keep
hook-mediated pushes in the repository shell. No additional environment change
was needed.

Superseded CI `46002774278` is confirmed canceled. Final integration CI has
entered its test step. Closed initial/r2 native test directories were removed
after confirming no owned process references; retained runner evidence is
`integration-first-runner.log` and `integration-r2-runner.log`. The r3 directory
and isolated gem cache remain available until final verification completes.

During r3, native watcher messaging/control tools became unavailable to the lead.
The existing watcher/source process remains active; no replacement run was
started. Lead uses bounded reads of the same independently accessible batch log
as the monitor skill's visible fallback. As of 14:35 CET, all seven final-head
mailer examples passed, including the corrected nodectl stop; DNS baseline and
pause examples also passed. Guest rebuild/startup took longer than r2; no kernel
build or test failure has been reported. Watcher source exec session: `92826`.

At 14:37:39 CET, all fourteen final-head mailer/DNS examples passed. This includes
both formerly failing stop cases, both main-loop stall and unresponsive-child
recovery modes, crash/restart, manual systemd stop/start, pause/resume and actual
mail/DNS work. The batch continues with existing DNS lifecycle and standard/runit
control scenarios. Full script exit and remaining batch result are still pending.

The watchdog script exited successfully at 14:37:59 CET, 1140.89 seconds.
The remaining three-script regression batch started at 14:41:03. Its first
standard/runit refresh/runtime example passed at 14:50:16 (4.4 seconds after
setup). Guest builds/startup dominated the wait: API initially returned 503,
then became ready normally; no check was restarted and no environment workaround
was needed. Node queue-control and DNS lifecycle checks remain in the same batch.

Standard/runit queue-control passed at 15:03:26 CET (338.66-second example;
779.26-second script including guest setup/teardown). It created a VPS, paused
its queue, queued a stop, resumed the queue, and verified completion. The unchanged
standard configuration retains the host facilities disabled only in minimal mode.
DNS zone lifecycle started at 15:03:55 and is the final local regression.

## Final local acceptance

All final-head local integration passed. The fresh watcher reported exit 0 for
`run-integration-r3.sh`, with source session `92826` closed and no remaining
operation-owned sessions, cells or known effects. Its terminal summary's 40m11s
is the three-regression runner duration; the complete command including the
watchdog scenario took about 63 minutes. Native test timestamps are authoritative:
watchdog 14:18:58–14:37:59, regressions 14:41:03–15:21:09 CET.

| Scenario | Result | Examples / duration |
| --- | --- | --- |
| admin/nodectld-minimal-watchdog | passed | 14 examples, 1140.89 seconds |
| admin/nodectl-refresh-and-runtime-state | passed | 1 example, 592.84 seconds |
| admin/nodectl-read-and-queue-control | passed | 1 example, 779.26 seconds |
| dns/server-zone-lifecycle | passed | 2 examples, 1033.77 seconds |

Combined evidence: `integration-r3.log`; native generated scenario configs and
individual runner logs are retained separately during cleanup. No local rerun
is needed. GitHub integration `46005898765` remains in progress as of 15:22 CET;
RuboCop is green and all 510 libnodectld examples passed at the unchanged library
revision. No production changes or default-branch integration were performed.

Cleanup completed after the watcher terminal receipt and a process-reference
check: `/tmp/nmw-20261127-r3` and the isolated gem cache were removed. Compact
individual runner logs are retained as `r3-os-test-*-runner.log` beside the combined
log. No local command, VM, database or utility operation remains running.
The worktree is clean. The stable session URL was revalidated with the current
installed `dev-session` wrapper; no lifecycle mutation occurred. Only broader
GitHub integration CI remains pending.

Read-only live CI inspection established progress unavailable through GitHub's
unfinished job-log blob. Exact job `140528852139` runs on
`gh-runner2.int.vpsadminos.org`; its process `3852125` identifies state for run
`46005898765`, attempt 1. The `/ci` path is inside its mount namespace, accessible
through that verified process root. At 15:28 CET the runner reported 21/22 tests
passed, zero unexpected failures, and only WebUI `vps-admin-ops` still running.
The new watchdog scenario passed on CI in 995.96 seconds, along with both node
regressions and all selected transaction scenarios. No remote mutation occurred.
See `notes/vpsadmin/2026-11-27-live-ci-runner-logs.md` for the read-only log access
lesson. The workflow's final conclusion is still pending.

## Final delivery checkpoint

GitHub integration run `46005898765` concluded **success** at
2026-11-27 15:39:34 CET on exact head
`a8ef7163832f3c246bb3927f00d68dd5a001818b`. It ran 27 scripts across 22 tests;
all passed, with zero unexpected results. The final WebUI long-operation script
passed in 1726.57 seconds. Complete CI evidence is retained in `ci-final.log`.
RuboCop `46005898709` is green; the unchanged libnodectld component has 510 passing
examples from `46002774246`. All declared hooks, focused checks, four local
integration scenarios and independent final review passed.

The final three-commit series remains unchanged from the last independent
whole-branch review. No obsolete history, repeated update streams or migrations.
Final worktree and base-to-head whitespace checks are clean. No review finding,
CI failure or local verification work remains. All known local exec sessions and
watcher cells have ended; owned disposable test directories/cache were removed.
The only open work is separately authorized master integration and production
configuration/deployment. Keep `lifecycle: active`; no merge, deployment,
archive or deletion is authorized by this checkpoint. The exact original native
hang trigger remains unconfirmed; the delivered fixes address minimal-mode
isolation and watchdog recovery, with both failure modes tested.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-27-nodectld-minimal-watchdog/

## Integration approval and preparation

User approval in this conversation: "looks good, mergeit", followed by the
condition "if specs workflow pass". This authorizes fast-forward integration of
vpsadmin into its remote `master` only after a passing specs workflow. It does
not authorize production configuration changes, deployment or archival.
Fresh fetch still reports base `99207a8dcd92f5907c52dbc99af52b30aa7ecac1`;
no rebase or patch change is needed. The complete reviewed three-commit series
and clean final diff remain unchanged at `a8ef7163832f3c246bb3927f00d68dd5a001818b`.
The prior libnodectld workflow passed at f3a74127a, but path filtering skipped the
CLI-only final commit. Explicitly dispatched `libnodectld Specs` on the final
feature head so the user's merge condition has an exact-head workflow result.
Prepare the target checkout/hooks without holding a repository claim; acquire
only for the fresh final target check, fast-forward, push and remote proof.

Exact-final-head `libnodectld Specs` workflow `46020722989` passed. The user's
merge condition is satisfied at a8ef7163832f3c246bb3927f00d68dd5a001818b.
The clean detached target checkout and its unchanged hooks were prepared and
signed in the declared Nix shell before requesting repository ownership.
Comparison capture binds the original base and final head. Final history matches
the independent three-commit review; no migrations or superseded updates.

## Merge receipt

User's conditional merge approval was satisfied by `libnodectld Specs` run
`46020722989`: success at exact final commit, 510 examples and zero failures.
Repository claim `0ffdfc3b-3824-44ce-8af6-d0fe385d3232` was held for the final
fresh target/feature/cleanliness checks, ordinary fast-forward merge, non-force
SSH push and remote proof. The supported claim mutation command is
`dev-session coordination`; the outer `workspace-host coordination` router
rejected acquire before any mutation. The same request then succeeded through
the documented session command. Its brief wait ended with authoritative held
status before any Git integration.

The clean detached target fast-forwarded from
`99207a8dcd92f5907c52dbc99af52b30aa7ecac1` to
`a8ef7163832f3c246bb3927f00d68dd5a001818b`. Hooks remained enabled; there were no
hook errors or history changes. SSH push updated `refs/heads/master`, and fresh
`git ls-remote` confirmed that exact final head on the remote. The claim was
released at 16:03:37 CET before record updates and disposable-checkout cleanup.
The merge shell exited successfully. Comparison capture preserves the original
base-to-head series in the portal. Keep both local and remote feature refs.

The user-requested merge is complete. Normal push-triggered master workflows are
new runs on this already reviewed and verified commit; no further source change
was introduced. Keep lifecycle active while those automatic results are pending.
No production configuration or deployment, session archive or deletion occurred.

The disposable merge-target worktree was removed successfully after release;
the registered feature worktree and both feature refs remain. Post-merge workflow
IDs on the same head: CI `46021440707`, libnodectld Specs `46021440211` (initially
running), and RuboCop `46021440278` (success). The passing pre-merge specs condition
remains `46020722989`; no rebase or source change separates those runs.
