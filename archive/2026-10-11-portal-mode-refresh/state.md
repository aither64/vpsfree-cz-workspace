---
lifecycle: complete
---

# Portal mode refresh

Phase: complete. Implemented, deployed on aitherdev and merged into all three
remote `master` branches. Pre-merge and post-merge verification passed.
The user directed "merge it" after the handoff
identified all three published branches, approving integration of dev-workspace,
workspace and vpsfree-cz-configuration into their `master` branches.

- [x] Investigation and approved implementation plan.
- [x] Implementation and quick checks.
- [x] Independent final branch review and narrow findings resolved.
- [x] Full browser integration.
- [x] Runtime and composed package checks; semantic deployment contract.
- [x] Host build and published-head CI.
- [x] aitherdev deployment and live verification.
- [x] Approved integration into the three remote `master` branches.
- [x] Final exact remote merge proof.
- [x] Post-merge master CI, including the additional host VM job.

Confirmed Codex modes remain visible and usable during background metadata
refreshes. Notices use the shared visibility-aware timing policy. Fresh server
metadata and settings generations still govern plan actions; retained display
state never authorizes them. Thread changes reset the retained mode.

All three owned worktrees use branch `2026-10-11-portal-mode-refresh`, published
over SSH with one consolidated commit each:

| Repository | Final head | Worktree beneath `worktrees/2026-10-11-portal-mode-refresh/` |
| --- | --- | --- |
| dev-workspace | a8934bdac91c64f66aa3cee26b68df3bcb8c2fc0 | dev-workspace |
| workspace | 0c82757629b48cef93df2c98677c07f5a9ba5059 | workspace |
| vpsfree-cz-configuration | decd92fe3926a4a4304c15957b05cc095948f8cc | vpsfree-cz-configuration |

Integration preflight fetched all targets. Runtime remained unchanged. Workspace
was rebased onto coordination commit 187f6a63 and configuration onto f457b2e4,
which only updates vpsfreeWeb. Rebased heads are workspace 0c827576 and
configuration decd92fe. Both have identical stable patch IDs and `range-diff`
reports equality; user approval remains applicable. Their complete final series
still contains one logical pin commit each, with no migrations or obsolete pins.
No substantive change needs another review. Exact integration revisions and
equivalence evidence are in integration-final-heads.json; deployed revisions
remain recorded in final-heads.json and rollout.md.

No migrations or persisted-state/API/protocol changes. Both consumer locks
select the exact runtime. Independent whole-branch history review and focused
finding reconciliation are in [review.md](review.md). The reviewed/deployed
series is in [branch-inventory.md](branch-inventory.md) and
[final-heads.json](final-heads.json); the patch-equivalent integration series is
in [integration-final-heads.json](integration-final-heads.json). Exact comparisons
are captured for all three Repositories-tab entries, including the rebased pins.
The workspace feature was rebased onto coordination master 306e805d before review
and onto 187f6a63 for integration.

[Verification evidence](verification.md) covers browser regressions, runtime and
composed package checks, host build and successful exact-head CI 38161519600.
[Executed rollout](rollout.md) records selected outputs and live checks:
served assets match the final source, the template selects app.js?v=35,
portal/router are healthy, and Codex/tmux retain their PID/start identities.
The owning runtime's `docs/workspace-portal.md` explains the lasting behavior.

No remaining work or blockers. All three approved masters were fast-forwarded
and pushed; fresh fetches prove all exact local/remote feature heads merged
(integration-final-refs.json). Temporary integration checkouts were removed
without force. Master CI 38167063056 passed for exact runtime a8934bda, including
host VM activation/recovery checks and package/focused checks (12m24s observation).
The fresh installed Luna/low utility /root/merge_ci reported success/exit 0;
the lead checked its exact-head evidence and accepted the result.
See [approved integration](integration.md) and merge-ci-result.json.
No further operator action is required for integration. Existing portal tabs
may be reloaded to receive the deployed script.
No session archive/delete/stop action was performed. Feature refs and worktrees
are retained. Only the completed, owned rollout utility unit was stopped.

Stable portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-11-portal-mode-refresh/

## Historical implementation checkpoint

At creation, `dev-session current` found no bound session. This conversation
created its own shell-only initiative with --no-codex, after committing initial
plan/state. The lead owned the bounded implementation/design. Installed catalog
policy supplied independent review and verification utilities.

Root cause: `renderThread` cleared `currentMode` when rollout metadata expired
and immediately replaced controls with an unmanaged Checking mode notice.

Owned worktrees are under `worktrees/2026-10-11-portal-mode-refresh/` for
`dev-workspace`, `workspace`, and `vpsfree-cz-configuration`, each on the matching
feature branch. Runtime base 356f6a99; workspace base 0835fb7f; configuration base
b18412bf. The session was started with --no-codex to avoid an unrelated native
lead; team-list correctly reports no lead thread. No retained roster exists, so
the installed catalog supplies standalone review and verification policy (saved
in agent-policy.json). This is not a delegated application task.

The lead's approved plan is the bounded design brief. Mode display retention is
thread-scoped; notices use createRefreshNotice; successful explicit mode saves
and same-session plan implementation advance settings generations. Plan actions
require a fresh generation and raw known server mode, independently of retained
display. No protocol, schema or persisted-state changes or migrations.

Initial JS syntax and shipped-client/API contract checks passed in the runtime
Nix environment (Go test 1.068 seconds). A final quick rerun covers the added
plan-generation guard. The browser regression covers visibility/restoration,
notice delays, retention, writes, stale reads and thread replacement.

Configuration creation's post-checkout hook lacked locked Ruby gems in the
ambient shell. Its worktree and registration were created before the hook
refused. Resolve in the configuration Nix shell and re-run the ordinary
registration command; never bypass hooks. A fresh Luna/low utility owns that
bounded environment preparation.

## Historical review checkpoint

Final committed heads: runtime 00952377, workspace 6bdc2a60, configuration
f644b39a. Complete series and final diffs are in branch-inventory.md and
final-heads.json. Both consumer locks select the exact published runtime and
the deployment contract passes. Extension, sibling inputs and native Codex
launch configuration are unchanged. Generated configuration pin history was
consolidated to one base-to-final confctl commit with normal hooks.

Independent reviewer /root/final_review uses installed reviewer role
gpt-6-astra/xhigh and all four lanes. Overall high risk classification reflects
live cross-project deployment, rather than UI implementation complexity.
No retained review member exists. New browser test syntax passes in the retained
runtime Nix development environment; integration awaits review.

Superseded GitHub run 38159740254 at b1e62c43 could not be canceled: the token
returned HTTP 403 Resource not accessible by personal access token. Final-head
run 38159925485 at 00952377 is the only current validation candidate.

Configuration environment and hook recovery completed with exit 0 (77 seconds);
configuration re-registration and checkout hooks passed without bypasses. The
existing reusable note notes/vpsfree-cz-configuration/2026-10-11-worktree-hooks-in-nix-shell.md
accurately describes the failure and recovery, so no duplicate note is added.

## Review reconciliation

Independent review completed all four lanes and the complete three-branch
history/migration gate. See review.md and reviewed-branch-inventory.md.
The Important stale plan-render race and Advisory test ordering gap were fixed
directly. Settings writes now invalidate renders and clear visible plan controls;
freshness is checked after hashing. The regression holds both digest and settings
responses and observes save completion before releasing stale reads.
The reviewer approved focused lead verification for these narrow corrections.

Final runtime 256281e0, workspace 9cb5a3a9, and configuration 64f8037a are
consolidated single-commit branches. Consumer locks match exactly; deployment
contract and quick JS/API checks pass. Full heads and diffs are current in
final-heads.json/branch-inventory.md. Previous CI runs finished successfully
before the latest push, so there were no running superseded jobs to cancel.
Current runtime CI run: 38160923954 at 256281e0.

## Focused browser verification

The first all-browser batch was deliberately canceled after identifying a new
fixture sequencing mistake: mode controls live in the composer, which an already
visible plan panel hides. The corrected fixture begins the held save first,
then lets an older read display the panel before releasing the save. The first
focused launch failed before tests because two launcher lines were concatenated;
that script error was inspected and corrected. Both failed/canceled artifacts
are retained separately. No product failure was diagnosed from those attempts.

Focused mode browser regression passed, 11 seconds, runtime a8934bda; evidence
mode-browser.log/status. Final source and pins are a8934bda / 45aba9bf / 3faee82a;
full exact heads are in final-heads.json. The deployment contract passes.
Final runtime CI is 38161519600. Superseded 38160923954 cancellation again refused
HTTP 403 due to token permissions; it is excluded from final-head evidence.

Full browser integration passed at final runtime a8934bda in 217.948 seconds.
The watcher is continuing the runtime/composed package, host build and CI checks.

Runtime and composed package checks and the deployment contract have passed.
The host build is running. The candidate's native executable resolves to the
same retained native package as the live service; all four managed units are
active. The actual pre-deployment snapshot will be refreshed before launch.

The full batch stopped before the host build at confctl's ordinary confirmation
prompt (EOF in a noninteractive watcher). Its complete log was inspected;
confctl build --help confirms --yes. The existing reusable note
notes/vpsfree-cz-configuration/2026-10-03-noninteractive-builds.md documents this
case. Only host verification is restarted with --yes; passed browser/package
phases are retained and will not be repeated. CI 38161519600 is completed and
successful for exact final runtime a8934bda (ci-result.json).

Host build with the documented --yes option passed in 2m10s. Generation
2026-10-11--20-27-19 builds the exact system path in candidate-system.txt.
host-verification.status is 0; final-head CI is independently confirmed.
All verification phases passed. The parent then launched the rollout through its
named transient user service; a fresh utility observed the existing operation
without deploying or retrying it. Deployment and post-deployment assertions
passed: rollout.status 0, rollout.phase complete, independent unit Result success
and ExecMainStatus 0. The launcher's D-Bus wait later returned an error, but the
unit and live evidence establish success; deployment was not repeated.
See rollout.md and the linked reusable launcher lesson.
