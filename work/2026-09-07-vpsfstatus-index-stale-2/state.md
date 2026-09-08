---
lifecycle: active
---

# 2026-09-07-vpsfstatus-index-stale-2

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
