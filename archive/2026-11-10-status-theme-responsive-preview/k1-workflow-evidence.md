# K1 kernel cache workflow evidence

Ready for lead acceptance and independent review, 2026-11-10 16:49 UTC.

- Repository/worktree: `vpsadminos`,
  `worktrees/2026-11-10-status-theme-responsive-preview/vpsadminos`.
- Base: `650170d699e3033c5279b911a2ef0a355439613c` (origin/staging).
- Final: `3b6b75ed06d44ff0bce41ebe03b723ce8f5dbdb5`.
- One logical commit, `ci: build kernels after flake input updates`;
  `.github/workflows/kernels.yml` only, +26/-3. Clean worktree and index.
  Fresh fetch leaves origin/staging at the recorded base. No push yet.
- No migrations, generated dependency changes, repeated input-update history,
  superseded implementation commits, deployments, releases or external consumers.

## Behavior and compatibility

Both staging push/PR filters include flake.nix and flake.lock. The existing
nightly schedule, kernel-path triggers, seven-version matrix, build command,
cache-copy and profile publication remain unchanged. Latest stable 6.12.113 is
included. Existing targets retain builtin-ZFS and plain kernel dev outputs;
nixpkgs' standard multiple-output hook propagates dev to out. No flake/output,
kernel source/configuration, input or credential changes are needed.

Successful same-repository staging completion of `Update flake inputs` also
triggers detection: its GITHUB_TOKEN pushes cannot trigger push workflows.
Detection checks out literal trusted refs/heads/staging after completion;
the updater event's head_sha can precede its new commit. Detection exports the
resolved checkout SHA and every matrix build uses that SHA. Failed/cancelled,
other-branch and foreign-repository completion events are rejected.

Official upstream release APIs and action manifests verified
actions/checkout v7.0.1 (Node24, same runtime as prior v6) and
cachix/install-nix-action v31.11.3 (composite). Checkout v7's new fork restrictions
concern pull_request_target/workflow_run checkouts of foreign code; this workflow
uses its own trusted staging ref for workflow_run. Existing push/PR checkouts use
the event SHA. No unsafe-fork opt-in was added.

Documentation placement: the workflow contains two nearby rationale comments
for token suppression and the updater's older event SHA. A separate maintainer
page would duplicate this small trigger contract. Session execution evidence
belongs here; the architect brief is in design.md and the lead's review packet
contains the complete range and final diff.

## Checks

- `git diff --check` and final base-to-head whitespace check: pass.
- Ruby YAML parse and static assertions: pass. Both path lists, staging filters,
  nightly schedule, unchanged matrix/build/publication and exact SHA flow checked.
  The literal gate expression was exercised with eight event cases: push, PR,
  schedule, successful same-repository staging completion, failed/cancelled
  completions, other branch and foreign repository. All passed.
- `bash -n` for each workflow run block with matrix expressions substituted:
  pass.
- Pinned-nixpkgs `actionlint -shellcheck= .github/workflows/kernels.yml`,
  actionlint 1.7.12: pass. ShellCheck omitted; Bash parsing checked separately.
- `nix eval --offline --no-write-lock-file --option
  allow-import-from-derivation false --json .#lib.kernelVersions`: pass;
  6.12.109, 6.12.110, 6.12.113, 6.12.48, 6.12.95, 6.18.44, 6.18.49.
- Corresponding raw evaluation of `.#lib.availableKernels.stableKernelVersion`:
  6.12.113, included in the matrix. No builds.
- Required Overcommit precommit and commit-message hooks: pass on final commit,
  no warnings or bypass. Existing executable hooks and unchanged custom Nixfmt
  plugin inspected; configuration signatures initialized after inspection.

The complete nix develop environment was attempted with local/remote builds
disabled (`--max-jobs 0 --builders ''`) and stopped on uncached documentation
dependencies. The packaged Overcommit wrapper also needed an uncached trivial
builder. Neither launched a local build. The successful minimal environment uses
Ruby and actionlint from the repository's pinned nixpkgs store source
`/nix/store/7sa2x9c9566lfxkaxs36n3z4yayl5cy4-source`, with Overcommit 0.68.0
installed in isolated `/tmp/k1-vpsadminos-gems`. Raw logs:
`/tmp/k1-vpsadminos-{nix-prep,tools,tools-minimal,hooks}.log`.
The monitoring skill's visible parent fallback was used because the shared
utility slot was unavailable. Every operation-owned command was joined.

## Execution limits and next dependency

No kernel/system build, VM test, workflow dispatch, PR, cache write or deployment
was requested or performed. Ordinary feature push does not match staging.
A PR targeting staging would execute existing builds and cache publication;
none was created. New workflow_run delivery requires this workflow on the
default branch (staging), and integration remains separately approval-bound.
The change's actual event delivery and publication remain unexecuted.

Read-only GitHub API evidence confirms existing run
[42803793083](https://github.com/vpsfreecz/vpsadminos/actions/runs/42803793083)
was schedule-triggered on staging at base 650170d and completed successfully at
11:05:49 UTC. It does not validate this new trigger or old downstream input graphs.
Reverting the workflow restores its earlier triggers; immutable published store
paths remain valid without deletion.

Next: lead acceptance and independent whole-branch review, followed by coordinated
feature publication. Implementer3 retains ownership of K1 review findings.

Lead accepted the package and assigned independent review. Before publication,
a bounded read of every workflow's trigger configuration confirms that an ordinary
push of this one-file change on the feature branch matches no workflow. The kernel
workflow requires staging; CI, RSpec, RuboCop and changed-container-image workflows
have path filters that exclude kernels.yml. Daily-update and flake-update accept
only schedule/manual events. No command was dispatched by this inspection, and
the source remains frozen at 3b6b75ed pending review and lead publication direction.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-10-status-theme-responsive-preview/

## Reviewed feature publication, 16:56 UTC

Lead reports independent final review accepted without findings, including
whole-branch history, no migrations, documentation and trust conclusions. Source
remained exactly 3b6b75ed. Fresh origin fetch confirmed base 650170d unchanged,
clean source/index and executable mandatory hooks. Comparison capture succeeded
for that exact range after one transient same-session command-lock refusal.

Ordinary SSH push published
`refs/heads/2026-11-10-status-theme-responsive-preview` at
`3b6b75ed06d44ff0bce41ebe03b723ce8f5dbdb5`.
The first push was refused locally by Overcommit's configuration-signature check;
a fresh remote read confirmed the branch absent. Reinspection of the unchanged
configuration and pre-push defaults, followed by normal `overcommit --sign` and
`overcommit --sign pre_push`, allowed the ordinary push without bypass. No source
or reviewed-history change was needed.

Fresh SSH remote proof confirms the feature head exactly matches the reviewed
head and staging remains 650170d. The worktree remains clean. One GitHub Actions
API snapshot at 16:56:58 UTC found zero runs for the exact published SHA; no wait
or workflow dispatch followed. No PR, default integration, cache write, machine
operation or session lifecycle action occurred.

K1 is ready, awaiting explicit vpsAdminOS/staging integration approval. Package
execution is reported complete and capacity is available; implementer3 retains
K1 follow-up-fix ownership. Lead owns subsequent integration and tracking updates.

## Approved-integration target preparation

Lead relayed explicit user approval for vpsAdminOS/staging integration and assigned
preparation only. Created detached `/tmp/status-theme-os-merge-3b6b` from fresh
origin/staging at `650170d699e3033c5279b911a2ef0a355439613c`; checkout hooks passed,
and the target's index/worktree are clean. The reviewed/published feature remains
`3b6b75ed06d44ff0bce41ebe03b723ce8f5dbdb5`. Final comparison was captured again
for this exact range. No merge, default push, repository claim or build occurred.

Post-checkout, post-merge and pre-push entrypoints are executable Overcommit
hooks. Inspected repository configuration and upstream defaults: none of those
three groups enables a task, while framework/signature checks remain active.
Normal configuration/plugin signing completed, and loading target configuration
verified its stored signature. The existing precommit/commit-message checks and
independent review remain unchanged and are reused.

Prepared command environment from the target directory:

```sh
nix shell --inputs-from . --offline --no-write-lock-file --max-jobs 0 \
  --builders '' nixpkgs#ruby --command bash
export GEM_HOME=/tmp/k1-vpsadminos-gems
export GEM_PATH="$GEM_HOME"
export PATH="$GEM_HOME/bin:$PATH"
```

The pinned Ruby resolves to
`/nix/store/hyrhia8cgzghr216z0r5wnbsqg7gbb9x-ruby-3.4.11/bin/ruby`, and
Overcommit 0.68.0 is available in the prepared isolated gem directory. A previously
used direct pinned-source store path had disappeared; restoring it through the
ordinary repository-input Nix command fetched it from cache.nixos.org, with
local and remote builds disabled. No checkout-hook failure or recreation occurred.
Lead owns the short claim, fresh checks, fast-forward merge, push and remote proof.

## Integrated by lead

User approved staging integration. Lead ordinaryFF/Overcommit/SSHpush650170d→3b6b75ed
exit0, freshremote staging+featureexact, claimcfab677b released/verified20:40:10UTC.
Push automatically created Build all kernel versions run42897514474 onexact3b6b;
queued atfirstsnapshot, watcher072e4a90 observes. No workflowdispatch/production
deployment. Pushtriggerobserved; actual updaterworkflow_run delivery and cache
publication remain separate pending runtime evidence.
