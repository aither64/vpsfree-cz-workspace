---
lifecycle: complete
---

# 2026-09-23-notification-subject-prefix

## Status

- All registered exact feature heads are merged into their remote default
  branches: notification templates `2cfd218`, configuration `76ce8add`, and
  workspace guidance `5b7946cc`. The user explicitly directed integration
  into the remaining default branches on 2026-09-24. No deployment was
  requested. The session remains open.
- The prior combined change was merged as `675e326`. The user has authorized
  replacing that published head with two commits: the final rule, then the
  corrected templates. The feature branch and remote `master` both point to
  final two-commit head `2cfd218`; local checks, review, and CI passed. The
  template repository work is complete and the session remains open.
- The user now requests updating the configuration channel. Their earlier
  direction to merge `vpsfree-cz-configuration` into `master` was explicitly
  withdrawn. On 2026-09-24 they explicitly directed, “ok, merge it into default
  branches.” This renewed integration approval for the configuration feature
  branch into `vpsfree-cz-configuration/master`.
- The generic confctl instruction change is committed on a separate workspace
  feature branch. The same 2026-09-24 direction authorizes its integration
  into workspace `master`. The template repository was already integrated.
- This process lacks the session environment markers, but `dev-session
  current` from this directory resolves to this slug; the user explicitly
  directed reuse of `2026-09-23-notification-subject-prefix`. A separate
  shell-only initiative `2026-09-23-notification-template-config-pin` was
  started unnecessarily before that correction and has no project worktree.
  The user will pass this portal/runtime issue to the responsible Codex
  instance; no workspace runtime change is part of this initiative.

## Next actions

- None for the requested merge. Keep the session open; deployment was outside
  the request.

## Documentation

- Repository `AGENTS.md` owns the subject-authoring rule. `README.md` still
  accurately describes the Nix-based integration and needs no edit.
- The follow-up changes the `AGENTS.md` rule only; template subjects are
  maintained in their owning `email/*.subject.erb` files.
- Stable session portal:
  https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-09-23-notification-subject-prefix/

## Repositories

- `vpsfree-notification-templates`: branch
  `2026-09-23-notification-subject-prefix`, worktree
  `worktrees/2026-09-23-notification-subject-prefix/vpsfree-notification-templates`,
  base `f275bf35abc0dc501881b5af78b1e19fb98aec68`.
- `vpsfree-cz-configuration`: branch/worktree
  `2026-09-23-notification-subject-prefix`, based on fetched `origin/master`
  `ba83425e5bfe5b8cd396bd48c7a58baa77ded5e9`.
- `workspace`: branch/worktree `2026-09-23-notification-subject-prefix`, based
  on remote workspace `master` at `7787ee79eadd14c2a7623eeb7a6b206b75ad9ee8`;
  rebased feature head `5b7946cc600c8698774cf45d96e2a16b612cf8f4`
  on current workspace `master` `1acf69b1d620702c9dc890f967651a90a9bc4026`.

## Commands run

- `dev-session current` matched `DEV_SESSION_SLUG`.
- Read workspace and repository guidance; inspected metadata and vpsAdmin's
  outage sender to classify the generic outage template.
- Fetched `origin/master`, committed initial plan/state as `ae65e51`, and
  created the feature worktree with `dev-session worktree add`.
- Audited all 136 `email/*.subject.erb` files with a focused Python check and
  compared changed files against `HEAD`.
- Launched a pinned Luna/low verification watcher for `nix run .#check` and
  `nix flake check`.
- Committed project change as `675e326` and launched the mandatory general-lane
  reviewer at Sol/xhigh. Review packet: `review-packet.md`.
- Pushed `2026-09-23-notification-subject-prefix` to origin; GitHub Actions
  `Check` run `35862757625` tests exact head `675e326`.
- Feature CI `35862757625` passed. Captured comparison for `f275bf3..675e326`.
  Merged the feature branch by fast-forward in a temporary target worktree;
  `nix flake check` and `nix run .#check` passed there, then pushed `HEAD:master`.
  Removed only the clean temporary target worktree. Master CI run
  `35863013462` targets the same `675e326` head.
- Master CI `35863013462` passed. Fetched remote refs and confirmed that
  `origin/master`, `origin/2026-09-23-notification-subject-prefix`, and the
  local feature branch all point to exact head `675e326`.
- Follow-up requested: preserve the already published commit and make two new
  focused commits, first the rule and then the template changes.
- User clarified that project work should remain on feature branches pending
  integration direction. The previous `675e326` integration was premature;
  the written workspace Git procedure specifies merge mechanics but does not
  require explicit direction for project repositories. The user then explicitly
  authorized force-pushing this repository's `master` for the two-commit split.
- Read-only check of configuration `origin/master:flake.lock` found its
  notification-template input pinned to predecessor `f275bf3`; it does not
  reference the published `675e326` head being replaced.
- Rebuilt the feature history from `f275bf3` in a temporary worktree: rule
  commit `1cadd74` changes only `AGENTS.md`; template commit `2cfd218`
  changes only six subject variants. Moved this session's feature branch to
  the new head and removed the clean temporary worktree.
- Audited all 136 subjects under the conditional prefix rule: no missing or
  doubled prefixes; 12 admin-only directories exempt. `nix run .#check`
  passed (73 templates, 363 files); `nix flake check` passed on the clean
  `2cfd218` worktree. `git diff --check` passed.
- Preserved the published `675e326` head in local backup ref
  `refs/backup/2026-09-23-notification-subject-prefix-before-master-rewrite`.
  Launched a related mandatory review follow-up (general, scope, and risk lanes,
  Sol/xhigh) using `review-packet-split.md`. Overall risk is high because
  replacing published `master` history is deliberate and irreversible for
  collaborators without reconciliation.
- Review of `1cadd74..2cfd218` found no project-code issues. A general-lane
  Advisory found stale plan/state wording about reply prefixes and the number
  of changed subjects; both records were corrected. No review rerun was needed
  for this tracking-only clarification. The risk and scope lanes found no
  issues. The reviewer checked live configuration `master` at `ba83425e` and
  confirmed its lock still pins `f275bf3`. Residual risks are collaborator
  reconciliation after the history rewrite and the lack of a delivered-mail
  preview.
- Captured the final comparison `f275bf3..2cfd218`, verified both live remote
  refs still equaled `675e326`, and force-pushed the feature branch with an
  explicit lease against that head. CI run `35864934816` targets `2cfd218`.
- Feature CI `35864934816` passed. Rechecked live `master` at `675e326`, then
  force-pushed `2cfd218` to `master` with an explicit lease against `675e326`.
  Master CI run `35865058725` targets `2cfd218`.
- Fetched remote refs after the pushes; local feature, remote feature, and
  remote `master` all point to `2cfd218`. The local backup ref still retains
  the replaced `675e326` head.
- Master CI `35865058725` passed. Final remote history from predecessor
  `f275bf3` contains exactly two commits, `1cadd74` and `2cfd218`; the
  registered exact feature head is merged into remote `master`.
- The portal-launched tool shell had no `DEV_SESSION_SLUG` or
  `DEV_SESSION_WORKSPACE`, while `dev-session current` inferred this slug from
  cwd and the managed tmux session had both variables. The shared App Server
  parent had neither. The user asked to pass the runtime issue to another
  Codex instance, so this initiative will only change the notification pin.
- Added configuration worktree from `ba83425e`. The first `dev-session
  worktree add` reported a post-checkout Overcommit missing-gems error from the
  ambient shell, but the worktree was created cleanly. Installed Overcommit
  through `nix develop -c bundle exec overcommit --install`.
- `nix develop -c confctl inputs channel update --commit
  vpsfree-notification-templates` created `76ce8addc3fae81778f44be3e9fd6dc14c1632b0`.
  Hooks passed. Only `flake.lock` changed: `vpsfreeNotificationTemplates`
  moved from `f275bf3` to exactly `2cfd218`; `git diff --check` passed.
- Mandatory review skipped for the configuration follow-up under its explicit
  generated lockfile-only/dependency-only exception. No hand-written code or
  configuration logic changed.
- Fetched configuration `origin/master` and confirmed it remained at
  `ba83425e`, an ancestor of the feature head. Pushed the feature branch at
  `76ce8add`; no configuration `master` integration occurred. Captured the
  feature comparison `ba83425e..76ce8add` for the portal.
- The first scoped `confctl build` stopped at its interactive confirmation
  prompt before building anything; the existing workspace note
  `notes/vpsfree-cz-configuration/2026-09-10-confctl-build-noninteractive.md`
  covers this behavior. A fresh Luna/low watcher is running the same build
  with `--yes`.
- The confirmed build passed at `76ce8add`: `nix develop -c confctl build
  --yes cz.vpsfree/vpsadmin/int.api1` built generation
  `2026-09-23--23-27-44`. Complete log: `config-api-build-confirmed.log`.
- This repository has only a scheduled `daily-update.yml` workflow and no
  push-triggered CI run for the feature branch.
- After confirming that the pin commit already used confctl and preserved its
  generated two-commit Git history, the user requested generic guidance for
  every confctl-managed configuration. Inspected `vpsfree-cz-configuration`
  channels (staging, production, vpsadmin, os-staging, system channels and
  service channels) and `vpsadminos-org-configuration` channels (nixos-stable
  and os-staging). Created workspace feature worktree and committed
  `67f27b7` to generalize `docs/agent-instructions/deployment.md`.
- The independent mandatory review of the workspace instruction used the
  installed standalone reviewer `gpt-6-sol`/`xhigh`, identity
  `/root/config_guidance_review`, on general, scope, and risk lanes. It found
  no issues. Packet: `review-packet-config-guidance.md`. The reviewer noted
  that the local-only shared-master tracking commit `d6ba1cae` for the
  unnecessary shell session must not be included in the feature branch.
- Rebased the single workspace documentation commit from `d6ba1cae` onto
  remote workspace `master` `7787ee79`; new head `fd615bba`. `git range-diff`
  proved exact patch equivalence, and `git diff --check` passed. The reviewer
  verified the new head. Pushed the workspace feature branch; captured
  comparison `7787ee79..fd615bba` in the portal. Shared local workspace
  `master` remains at `d6ba1cae` and was not pushed or rewritten.
- Configuration feature branch and workspace instruction feature branch are
  published. Neither `vpsfree-cz-configuration/master` nor workspace
  `origin/master` has been changed by these follow-ups. The configuration
  repository has no push-triggered CI, and the workspace has no GitHub Actions
  workflow in this checkout.
- On 2026-09-24, the user explicitly directed merging both remaining feature
  branches into their default branches, renewing approval for
  `vpsfree-cz-configuration/master` and authorizing workspace `master`.
  No deployment was requested.
- Fetched configuration remote refs; `master` remained `ba83425e`. Merged
  `76ce8add` by fast-forward in a fresh temporary target worktree. There,
  `git diff --check`, exact lock revision/head assertions, and
  `nix develop -c confctl inputs channel ls` passed; the listing showed the
  notification-template channel at `2cfd218d`. Pushed `HEAD:master` from that
  worktree and removed the clean temporary worktree. Live remote feature and
  `master` both point to exact head `76ce8add`.
- Workspace remote `master` had advanced to `1acf69b1`. Rebased the one
  documentation commit onto it, producing `5b7946cc`. `git range-diff`
  proved exact patch equivalence with the reviewed `fd615bba` commit and
  `git diff --check` passed. Captured the new comparison
  `1acf69b1..5b7946cc` before integration; no review rerun was needed for
  the clean patch-equivalent rebase.
- Updated the remote workspace feature ref to `5b7946cc` with an exact lease
  against `fd615bba`; no push-triggered workspace workflow exists. From the
  shared workspace `master`, verified the feature branch descended from
  current `master` and changed only
  `docs/agent-instructions/deployment.md`. Fast-forwarded to `5b7946cc`,
  checked the merged diff, and pushed `HEAD:master`.
- Read-only remote checks confirmed that both feature and default branch refs
  equal the exact final head in each of the three registered repositories:
  templates `2cfd218`, configuration `76ce8add`, workspace `5b7946cc`.

## Results

- The audit found unprefixed user-facing request, IP release, and generic
  outage subjects. The user confirmed existing `Re: [vpsFree.cz] …` subjects
  are valid; the newly identified omissions have been fixed.
- Current `origin/master` uses standalone subject ERB files, unlike the stale
  bare clone's local `master` inspected initially.
- The prior published `675e326` revision changed ten subject variants,
  including four that produced double prefixes. The replacement `2cfd218`
  revision changes six variants and leaves the four request subjects at their
  original single prefix. No user-facing subject among 136 variants lacks an
  identifying prefix; 12 administrator-only directories are exempted.
- `nix run .#check` passed (73 templates, 363 files); `nix flake check`
  passed. Logs: `nix-run-check.log`, `nix-flake-check.log`.
- Mandatory review: low risk, general lane, pinned Sol/xhigh reviewer
  `dw_aedcfbb1a3dc69f0aebc22073bb4abbd78ac1803dd2d0f57` reviewed
  `f275bf3..675e326` and found no issues. No rerun needed. Residual gap:
  no delivered-email preview was checked; validation covered template checks
  and sender paths.
- Four user request subject variants currently contain both `[vpsFree.cz] `
  and `[vpsAdmin Request #…]` in the previously published `675e326` tree.
  The rebuilt `2cfd218` tree keeps only `[vpsAdmin Request #…]` in those
  variants, preserving `Re: ` on replies.

## Open questions

- None blocking implementation.

## Cleanup

- Session remains open. Local and remote feature branches, owned feature
  worktrees, and the template-history backup ref are retained. Temporary merge
  worktrees were removed after their verified merges.
