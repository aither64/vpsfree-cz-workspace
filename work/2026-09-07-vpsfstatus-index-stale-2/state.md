---
lifecycle: active
---

# 2026-09-07-vpsfstatus-index-stale-2

## Current follow-up: 2026-09-08

- User requires keeping the 60-second scrape interval and asks for improvement
  within that constraint. Prepare the alert fix described in the updated plan.
- The portal restored this exact retained conversation under the original slug
  in workspace commit `958688c`. Its manifest still identifies thread
  `01a07c42-a006-77e2-b4cd-5424d3acdd07`. The resumed tool environment lacked
  session variables, so `dev-session current` initially reported none.
- `dev-session list` confirmed the restored managed session; `dev-session start
  2026-09-07-vpsfstatus-index-stale-2 --as-is --no-attach` resumed it. Restoring
  the verified slug/workspace environment for helper commands makes `current`
  report the matching slug. No other initiative was reused.
- Scope: configuration-only rule adjustment, focused promtool regression tests,
  mandatory review and scoped monitoring builds. No production deployment.
- Current decision after the user's larger-margin request: separate 60-second
  rule group, 600-second render-age threshold, unchanged five-minute
  missing-metric window, and `for = "2m"` for either condition. The former
  15-second scrape recommendation in the investigation is superseded.
- Configuration branch: `2026-09-07-vpsfstatus-index-stale-2`; worktree:
  `worktrees/2026-09-07-vpsfstatus-index-stale-2/vpsfree-cz-configuration`;
  fetched base: `e26f0a3360e1a20e76c3c0ef4193448584a8c1bb`.
- `dev-session worktree add` created the checkout but its post-checkout
  Overcommit hook failed in the ambient environment because gems were missing.
  Entered `nix develop`, installed and signed hooks with `overcommit --install`
  and `overcommit --sign`. Repeating the helper registered the existing
  worktree. This is the known Nix-shell/worktree-hook setup issue.
- Added production-rule tests for scrape/evaluation phase mismatch, one failed
  scrape, sustained stalls, sustained absence, confirmation and recovery.
- Committed head: `0297b0c3bfcec0a4cc0e32fa294c996bfe978afa`.
- Quick verification: `nix build
  .#checks.x86_64-linux.vpsf-status-prometheus-rules --no-link -L` passed all six
  scenarios; `overcommit --run` passed Nixfmt/RuboCop; commit hooks passed.
  The first fixture run exposed incorrect expectations for `$labels` in
  annotations; corrected those expected strings and recorded the lesson in
  `notes/vpsfree-cz-configuration/2026-09-08-prometheus-template-labels.md`.
- Applied the user-facing writing skill to the final alert description before
  committing. Both age/absence branches and the confirmation period are
  described explicitly.
- Mandatory review packet: `review-packet.md`. Classification high because of
  critical alert timing and rollout implications. All four lanes use
  `gpt-5.6-sol` with `xhigh` effort; scoped builds wait for their findings.
- General review completed for `0297b0c3` with no findings. Residual risks are
  unavailable historical alert evidence, alert-state reset during the rule-group
  move, and noise from a monitor still running the old policy during rollout.
- Read the generated JSON: the new group contains only the render alert at
  60-second evaluation, with threshold 600 and confirmation 2m. The original
  group retains its six existing alerts and 300-second interval. The scrape
  module has no diff. `confctl ls 'cz.vpsfree/containers/prg/int.mon*'` selected
  exactly mon1 and mon2 for the planned scoped builds.
- Architecture and scope lanes also completed with no findings. The risk lane
  found an Important label-identity transition issue; see `review-results.md`.
  Corrected it with static service labels and a transition regression case.
  Missing-metric alerts now retain the same service identity as stale renders.
- Amended head: `08dae58b16abdde30cff1572478b29343ed32fc4`. All seven promtool
  scenarios and commit hooks pass; commit message now also satisfies the hook's
  advisory 72-column width. New risk and architecture reviewers inspect the
  bounded label remediation via `review-rerun-packet.md`, with the same required
  model/effort. General and scope do not require reruns for this targeted fix.
- Both affected-lane reruns completed with no findings for `08dae58b`.
  Singleton target-label coupling and temporary grouping differences during a
  mixed rollout are accepted and documented. No Blocking or Important finding
  remains. Full reconciliation is in `review-results.md`.
- Fetched configuration origin again after review: feature branch is one commit
  ahead and zero behind `origin/master`. The repository has only a scheduled
  and manually triggered daily-update workflow, with no push/PR check workflow.
- Completed `nix develop -c confctl build --yes
  'cz.vpsfree/containers/prg/int.mon*'` after review completion, scoped to both
  Prometheus containers. Exit status 0; both systems and their full Prometheus
  configurations/rules passed the build checks. Local generation:
  `2026-09-08--09-48-32`. No deploy command was run.
- Built system outputs:
  - mon1: `/nix/store/rifgphs98ksfm3yms1wvkw4537dzr7bj-nixos-system-mon1-26.05.20260903.a5cc6f2`
  - mon2: `/nix/store/igl5vi8582582d7ykf3zkih8bg3m4r5n-nixos-system-mon2-26.05.20260903.a5cc6f2`
- Implementation and local verification are complete at `08dae58b`; the branch
  is committed locally, not pushed or merged. No production change has occurred.
  The next operator action is to integrate the prepared commit and deploy both
  monitor containers when requested. The branch/worktree remain available.
- Removed only this worktree's generated untracked `.bin/`, `.bundle/` and
  `.rubocop_cache/` directories after tooling finished. Build generations and
  logs remain in the ignored `.confctl/` directory for the next step.
- Handoff uses the stable portal URL below. This is the consolidated September
  8 tracking checkpoint; preserve other initiatives' shared-master changes.
- Initiative remains active for handoff and any subsequent integration or
  deployment. No automatic finalization is scheduled.

## Historical investigation record: 2026-09-07

The sections below preserve the original read-only investigation. The current
follow-up above supersedes its proposed scrape interval and completion status.

## Repositories

- Canonical bare repositories: `repos/vpsf-status.git` and
  `repos/vpsfree-cz-configuration.git`; inspect `origin/master` and deployed pins.
- No feature worktrees or project code changes are currently needed.
- Workspace coordination checkout remains on `master`.
- Fetched status head: `587cd65bb02e6dddea7f6b6409e42a15f36ab4fb`.
- Fetched configuration head: `4d570e3053b114518ada59c2a45d5e9d8644347b`.
- Configuration `vpsfStatus` input pins that status head. Running revisions
  could not be independently checked because SSH credentials were rejected.

## Status

- Session created with an initial request.
- Verified `dev-session current` and `VPSFREE_DEV_SESSION_SLUG` both match
  `2026-09-07-vpsfstatus-index-stale-2`. Other sessions are untouched.
- Inspected the supplied screenshot: a regular sawtooth, roughly four minutes
  between resets, with peaks close to 300 seconds.
- Initial tracking committed as `90ee397`; no hook framework is declared in
  the workspace checkout, and no executable pre-commit hook was present.
- Traced body-cache keepalive, render attempts, shared localized render gauge,
  per-request shell timestamp, scrape cadence and alert evaluation/notification.
- Prepared `investigation.md` and registered it in the portal manifest.

## Commands run

- `dev-session current`, workspace `git status`, repository `git grep` and
  `git show`, screenshot inspection.
- Read workspace orchestration, handoff and mandatory-review instructions.
- Fetched all inspected repository origins. Source inspected with `git show`,
  `git grep` and commit history; no project worktrees were needed.
- Read public `https://status.vpsf.cz/metrics`; sampled every five seconds with
  curl and summarized only the index metrics and response cache headers.
- Queried both public Prometheus APIs (HTTP 401), internal port 9090 (timeout),
  and SSH on `172.16.254.254` and `mon1.int.prg.vpsfree.cz` (authentication
  rejected). Initial unknown host keys were accepted using `accept-new`, which
  retains rejection of changed keys; no credential values were read or written.
- Compared public HTTP client behavior: default Python user agent receives
  Cloudflare 403/1010; ordinary curl over HTTP/1.1 or HTTP/2 and a Prometheus
  user agent receive 200. Stopped the failed Python collector before replacing
  it with curl. Recorded the reusable client lesson under `notes/vpsf-status/`.
- Reproduced a false age crossing using a small local timing model: renders
  every 242 seconds, scrapes at 1+60n seconds, evaluation at 300.5 seconds.
  Observed age 300.5; actual age 58.5; next scrape resolves the condition.
- Read primary Prometheus documentation for query and alert evaluation meaning.
- Portal TLS verification used the published public CA after the ambient trust
  store rejected its private issuer; endpoint returns expected HTTP 401.
- `git diff --check` passed. Early `dev-session finalize --check` correctly
  refused the still-active lifecycle; finalization waits for sampling to end.

## Results

- Located the alert in `modules/clusterconf/monitor/rules/vpsfree-web.nix`
  and the metric producer in `vpsf-status/exporter.go` and `index.go`.
- Confirmed source settings: 240-second unchanged-body keepalive, 60-second
  scrape, age threshold >300 seconds, 300-second rule group, no `for`.
- Commit `c6fab247` deliberately replaced per-second expensive rendering to
  reduce CPU use, choosing the 240-second keepalive for the existing alert.
- The screenshot matches elapsed time since the last observed cached-body
  render, rather than render duration. Its query is not visible, so this is an
  inference supported by the alert expression and observed values.
- Source and local reproduction establish a normal-timing false-positive
  mechanism. No claim is made that every historical notification has that cause.
- Initial live sample at 14:27:40 UTC: operational=1, failures=0, duration
  0.943233379 seconds, skips=692929. Continued sample summary follows below.
- Proposed follow-up: 15-second scrapes and a dedicated 30-second group with
  `for = "1m"`, preserving caching, metric meanings and the 300-second cutoff.
  Confirm against historical alerts before implementing. No fix deployed.
- Mandatory change review is not applicable: this is a read-only diagnosis
  with coordination records, no implemented code, configuration or design
  change. No review agents, builds, tests or CI runs were required. The timing
  model is the focused verification of the sampling explanation.
- Applied handoff and user-facing-writing skills directly to the report.
- Final live sample: 62 successful requests from 14:30:22 to 14:35:27 UTC,
  zero request errors, operational gauge continuously 1, failures continuously
  0, 452 additional render skips, render duration 0.856012848 to 0.943233379
  seconds, maximum observed attempt age 5.3304 seconds.
- Render timestamp updates included 14:30:37 / 14:30:43 and 14:34:39 /
  14:34:45 UTC. Corresponding updates are 242 seconds apart, consistent with
  localized caches reaching the keepalive in separate attempts. The unlabelled
  metric cannot identify the locale of an individual update.
- `metrics-summary.json` retains the compact observations. The finite sampler
  completed normally; its reproducible bulk capture was removed from `tmp/`.
- Investigation complete within the documented evidence limits. No required
  implementation, review, CI, approval or deployment remains in this task.

## Open questions

- Exact causes of individual historical notifications require their timestamps,
  VALUE and historical scrape data. An optional question was sent to the user;
  this evidence was unavailable during the diagnosis.
- The report explains how to distinguish the age branch from missing metrics
  and how to correlate render attempts, failures and `up`. A follow-up fix is
  a separate task; there is no pending production operation in this initiative.

## Cleanup

- Unrelated shared workspace changes were preserved. No project mutations or
  production background services were started.
- Both local collectors have stopped. No worktrees, caches, credentials or raw
  captures remain in the initiative. Finalization refused the current thread's
  `inProgress` turn. A task-scoped cleanup process waits for the normal idle
  check, verifies the prepared files are unchanged, then finalizes, commits the
  exact archive move and three task-owned durable notes, and stops the managed
  tmux session. No feature branch refs need removal. Cleanup log:
  `tmp/vpsfstatus-index-stale-2-finalize.log`.
- Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-09-07-vpsfstatus-index-stale-2/

- Post-turn cleanup: idle check passed; normal finalization archived the
  initiative. This final record and the exact archive move are committed
  together; managed session stop follows that commit.
