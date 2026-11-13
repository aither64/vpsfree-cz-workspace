# C0: vpsadminos.org scheduled update diagnosis

Investigated on 2026-11-13 by implementer1. Read-only GitHub API and exact
attempt logs; no application edits, fetch, reruns, builds, pushes, PRs, merges
or deployments. Session current/environment/thread identity all matched
`2026-11-13-scheduled-workflow-fixes` in the bound workspace. Saved team settings
were preserved. Initial plan/state commit supplied by lead: `66c6aede3`.

## Finding

The scheduled updater installs Overcommit hooks but signs only its configuration,
leaving its custom Nixfmt pre-commit plugin unsigned. The next generated commit
is rejected before the guarded push step can run. This is a deterministic
repository workflow setup error, introduced by
[`ca96c95a1fee04793468785d8323a759615b2b4e`](https://github.com/vpsfreecz/vpsadminos-org-configuration/commit/ca96c95a1fee04793468785d8323a759615b2b4e).

At that exact revision:

- [`.github/workflows/daily-update.yml:34-37`](https://github.com/vpsfreecz/vpsadminos-org-configuration/blob/ca96c95a1fee04793468785d8323a759615b2b4e/.github/workflows/daily-update.yml#L34-L37)
  installs hooks and invokes `nix develop -c bundle exec overcommit --sign`
  without a hook type.
- [`.overcommit.yml:3-5`](https://github.com/vpsfreecz/vpsadminos-org-configuration/blob/ca96c95a1fee04793468785d8323a759615b2b4e/.overcommit.yml#L3-L5)
  enables the custom hook in
  [`.git-hooks/pre_commit/nixfmt.rb`](https://github.com/vpsfreecz/vpsadminos-org-configuration/blob/ca96c95a1fee04793468785d8323a759615b2b4e/.git-hooks/pre_commit/nixfmt.rb).
- [Workflow lines 57-58](https://github.com/vpsfreecz/vpsadminos-org-configuration/blob/ca96c95a1fee04793468785d8323a759615b2b4e/.github/workflows/daily-update.yml#L57-L58)
  ask confctl to commit channel updates, triggering the unsigned plugin.
- [`Gemfile.lock:8`](https://github.com/vpsfreecz/vpsadminos-org-configuration/blob/ca96c95a1fee04793468785d8323a759615b2b4e/Gemfile.lock#L8)
  selects Overcommit 0.68.0. Its official
  [`CLI#sign`, lines 190-202](https://github.com/sds/overcommit/blob/v0.68.0/lib/overcommit/cli.rb#L190-L202)
  updates plugin signatures only when an explicit hook argument is supplied;
  the no-argument path updates the configuration signature alone.

Minimal prospective fix: retain configuration signing and add
`nix develop -c bundle exec overcommit --sign pre-commit` before any updater
commit. This recommendation is evidence for architect0's brief, not released
implementation. Keep the existing signatures and hook checks enabled.

## Exact run evidence

There is one active scheduled workflow, ID `166948797`, named `Daily update`,
at `.github/workflows/daily-update.yml`, cron `40 4 * * *`. Latest three scheduled
runs and the boundary runs all used attempt 1. The four failed runs below used
head `ca96c95a1fee04793468785d8323a759615b2b4e`.

| Role | Run / UTC creation | Result / job | Exact observed failure time |
| --- | --- | --- | --- |
| Latest | [#526 / 43426233198](https://github.com/vpsfreecz/vpsadminos-org-configuration/actions/runs/43426233198), Nov 13 12:33:55 | Failure; [job 131888211412](https://github.com/vpsfreecz/vpsadminos-org-configuration/actions/runs/43426233198/job/131888211412) | 12:37:06 |
| Previous | [#525 / 43224971552](https://github.com/vpsfreecz/vpsadminos-org-configuration/actions/runs/43224971552), Nov 12 13:11:48 | Failure; [job 131205704555](https://github.com/vpsfreecz/vpsadminos-org-configuration/actions/runs/43224971552/job/131205704555) | 13:15:05 |
| Third latest | [#524 / 43017413846](https://github.com/vpsfreecz/vpsadminos-org-configuration/actions/runs/43017413846), Nov 11 12:06:01 | Failure; [job 130511819552](https://github.com/vpsfreecz/vpsadminos-org-configuration/actions/runs/43017413846/job/130511819552) | 12:09:03 |
| First failure after last success | [#507 / 40180341616](https://github.com/vpsfreecz/vpsadminos-org-configuration/actions/runs/40180341616), Oct 25 09:22:00 | Failure; [job 121129857961](https://github.com/vpsfreecz/vpsadminos-org-configuration/actions/runs/40180341616/job/121129857961) | 09:28:34 |
| Last success | [#506 / 40080535061](https://github.com/vpsfreecz/vpsadminos-org-configuration/actions/runs/40080535061), Oct 24 09:04:51 | Success; [job 120832958682](https://github.com/vpsfreecz/vpsadminos-org-configuration/actions/runs/40080535061/job/120832958682) | Both channel updates and push succeeded |

All four exact failed-attempt logs show the same sequence:

1. `Install git hooks` succeeds. The latest log at 12:35:05 prints
   `Updating signature for configuration file...`, with no plugin-signing output.
2. `Update flake inputs` (step 8) fails with a changed/unsigned pre-commit plugin
   warning naming `Nixfmt` and `.git-hooks/pre_commit/nixfmt.rb`.
3. Overcommit requests `overcommit --sign pre-commit`. Confctl then reports
   `error: git commit failed`; the step exits 1.
4. `Check and push updates` is skipped. Cache save succeeds despite update
   failure, as configured with `!cancelled()`.

The API run list shows 20 consecutive scheduled failures from Oct 25 through
Nov 13. Only the latest three and first failure were expanded to exact failed
attempt logs because they establish the current symptom and introduction
boundary. The last success's exact attempt log was also inspected: it ran the
previous workflow, which did not install hooks; both updates and push succeeded.
Its head was `6b04b48e9c076e5525ccb7c38ce174232414f0b5`. The
[comparison to the first failing head](https://github.com/vpsfreecz/vpsadminos-org-configuration/compare/6b04b48e9c076e5525ccb7c38ce174232414f0b5...ca96c95a1fee04793468785d8323a759615b2b4e)
contains one workflow-only commit, including the new incomplete hook setup.

## Cause classification and limits

- **Repository/tool setup:** confirmed missing pre-commit plugin signing. The
  initial concern about Nix environment drift was ruled out by the explicit
  CLI semantics and config-only signing output.
- **Infrastructure/cache:** checkout, Nix install, hook install, cache restore
  and cache save succeeded in the inspected jobs. No evidence of runner
  availability, disk exhaustion or missing substitution as this failure's cause.
- **Upstream inputs:** the first failure log reaches `Updating nixpkgs in
  nixos-stable -> da6dc0e7` and then fails at commit. No observed input fetch,
  ancestry rejection or upstream build failure causes this failure.
- **Authentication:** no observed authentication failure; push is never reached.
  This does not independently validate future push credentials.
- **Toolchain/actions:** Nix and Ruby dependencies run far enough to invoke
  Overcommit. No evidence that imported action versions caused this failure.
  Architect0 owns official action-version validation; no redundant upgrades
  are proposed here.

The guarded final input ancestry check and push remain unexercised after this
failure. No full system/configuration build is useful for diagnosing an unsigned
plugin. A later implementation should verify fresh-repository hook signing and
hook rejection behavior in a disposable fixture under the repository shell,
then satisfy the architect's check brief. Do not disable signatures, skip hooks,
change deployment pins or weaken the existing confctl guard to pass CI.

## Inspection method and ownership

Used `gh api` for workflow/run/job metadata, current tree, exact-revision content
and the success-to-failure comparison; `gh run view --attempt 1 --log-failed`
for each named failure; and `gh run view --attempt 1 --log` for the last success
and latest install output. Only masked logs and relevant excerpts were read.
No credentials were printed or saved in this evidence.

The canonical bare clone was inspected with `git show`; its HEAD was older than
the remote workflow, so conclusions use the exact remote run head above.
No repository `AGENTS.md`, README or docs entry point exists at that remote
revision. Relevant workflow, shell, hook and lock sources were inspected instead.
Workspace required procedures and documentation/handoff skills were read.

Application edits remain withheld pending architect0's sufficient released brief
and lead allocation. C0 evidence is ready for lead acceptance; implementer1
retains prospective implementation ownership of this repository. No final
change review is required for investigation evidence alone. State/package-table
updates and any consolidated coordination commit remain with the lead.
