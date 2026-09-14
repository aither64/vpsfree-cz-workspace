# Automatic archival review packet

## Requested outcome

Implement and deploy the accepted plan in plan.md. Tiers in order: explicit
complete after 24 idle hours -> complete archive; active registered branches all
merged after 168 hours -> complete archive; active with no registrations or owned
worktrees after 336 hours -> abandoned archive. Persistent Keep open in CLI and
portal overrides all automatic tiers. First enable/re-enable, hold release and
revival receive fresh periods. No initial backlog archival. Other workspaces
default disabled. Already abandoned sessions remain manual.

## Reviewed repositories and commits

All paths are below /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-14-auto-archive/.

- dev-workspace: base df21f2ea8fe27efdb2cb8c0330fa31acd0f3a933;
  head ef1fa85451ee98f9d0a1d167d586ea2765b67cf7.
  6524018 worker/CLI/sidecars/timer with tests; ef1fa85 portal controls and docs.
- vpsfree-dev-workspace: base 89a03581b13056fa83114e592f2e2993e6a87887;
  head bba4b8d8208bdfbe9a08e2a90ce04c1910c6cfce; dependency-only pin.
- workspace: base 758834a (initial initiative tracking commit);
  head 89f8efe2f7171b2a0b388e0349c24121da0ceef6.
  bba4a38 standing policy authorization; 89f8efe consuming pin.

The worker, lifecycle integration, packaged helper, timer lifecycle and tests
form one runnable CLI feature. Portal transport/presentation and its documentation
are separate. Pins are separate mechanical commits. All implementation files
are committed; plan/state and review artifacts are coordination records.

## Architecture and consumers

The generic aither64/dev-workspace runtime owns archive semantics, CLI, portal,
host profile and user units. WorkspaceAutoArchive adds a sidecar Store, retention
Policy and Runner mixin; the existing DevSession::Runner remains archive authority.
It reads existing workspacecodex ListThreadActivity via a new thread activity CLI.
The Codex package, codex-web source and App Server protocol versions are unchanged.

Public CLI: dev-session auto-archive scan [--dry-run] [--json], enable/disable,
hold/release/status SLUG [--as-is]. Public portal GET/POST
/api/sessions/SLUG/auto-archive; POST accepts hold and existing lifecycle targetId.
The owning CLI persists holds, observations and operation IDs. The portal uses
existing origin, exact-target, generation and transition-lock protections.

Private per-workspace sidecars beneath the existing user state root bind records
to canonical workspace path and session conversation identity. Existing session
manifests, authority and archive journal formats are retained. The scanner reuses
archive merge/cleanup/idle/recovery checks, with automatic guards under the locks.
Completed merges are proved when the inactivity period is due. The timer manages
register/suspend/unregister/switch/rollback behavior and uses the stable profile.

Actual consumer chain is generic runtime -> vpsfree-dev-workspace lib.mkPackage
extension package -> workspace flake siteConfig -> workspace-host user-profile
deployment. No host NixOS change is required; the user authorized configuration
deployment if needed. No project DB/API/daemon/node protocols change.

## Boundaries and compatibility

Risk: high (destructive session operations, persistent state, lifecycle recovery,
public CLI/API and deployment/rollback). All four review lanes are required with
gpt-5.6-sol and xhigh effort. Read local AGENTS.md in each reviewed repository.
The local operator is trusted to administer the host. Keep ordinary identity,
concurrency, integrity, rollback and remote-client protections; do not expand the
scope to defending against a compromised operator's filesystem manipulation.

Non-goals: goal inference from prose or AI, per-project changes, independent
cleanup implementations, deleting branches, global opt-in, hostile-root defenses,
per-event filesystem monitoring, a generic scheduler, or changing archive formats.
Changes made and reverted entirely between scans cannot be observed; this polling
limit is documented. Holds affect automatic archival only. Once an automatic
operation has a journal, disabling policy does not revoke its recovery authority.
Only a matching recorded operation ID can be resumed automatically.

Deploy through aitherdev's existing user profile after review and packaged/live
validation. Preserve branches and keep the initiative open for follow-up.

## Quick verification

Nix toolchain selected with --inputs-from the runtime flake: Ruby, Go, GCC, Node.
- Ruby syntax checks and git diff --check passed.
- test/auto_archive_test.rb: 8 runs / 33 assertions passed (retention boundaries,
  resets, holds, disable, persistence, invalid storage).
- test/dev_session_test.rb --name '/test_automatic|test_archive/':
  22 runs / 460 assertions passed, including real disposable Git archives,
  failed commit recovery after policy disable, hold race, dry-run, activity and
  queue reset, retained registrations, existing exact merge/journal checks.
- test/workspace_host_test.rb: 74 runs / 461 assertions passed, including timer
  installation/removal across rollback.
- go test ./cmd/workspace-portal ./internal/workspacecodex ./internal/web passed,
  including new API tests and the Go-owned browser contract fixture.
- node --check portal/internal/web/static/app.js passed.
- Lockfile updates resolved committed, pushed feature revisions; diff checks pass.

Two tooling invocation mistakes were investigated and corrected: Go without GCC
failed cgo compilation; adding GCC passed. Direct browser_contract_test.cjs needs
its fixture server URL; the Go owning test supplies it and passes. The reusable
note is notes/dev-workspace/2026-09-14-focused-check-toolchain.md.
Long packaged/live integration checks have not started. Branch push CI may run
its normal package checks; the master/manual VM lane is not dispatched yet.

## Reviewer instructions

Review your assigned lane directly; do not spawn reviewers. Follow
/home/aither/.codex/skills/mandatory-change-review/SKILL.md and its lane reference.
Return concrete findings with severity, file/line and commit evidence. Write
your report to work/2026-09-14-auto-archive/review-LANE.md in the shared workspace;
do not edit implementation files. State residual risks/test gaps when appropriate.
