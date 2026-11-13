# B1: stable development shell for scheduled updates

Owner: implementer0. B0 accepted; B1 released by lead under the architect's
[design brief](design.md). Source/index/commit ownership is exclusive to this
package in `vpsfree-cz-configuration`.

**Ready for package acceptance and independent review.** Published feature head
`355e269f034422bb042f6c39fdab1725855b47e0`. No integration, deployment or PR.

## Source and intent

- Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-13-scheduled-workflow-fixes/vpsfree-cz-configuration`.
- Branch: `2026-11-13-scheduled-workflow-fixes`.
- Initial base: `6e9ed6fb3ded5d72fbfa31c3feb4fccfcdfee494`.
- Sole source file: `.github/workflows/daily-update.yml`.
- Capture the original shell once at
  `$RUNNER_TEMP/daily-update-dev-shell` during hook installation, then reuse
  it at every later shell entry. This keeps native gems and hooks on the same
  Ruby even after the job updates stable nixpkgs.
- Preserve action refs, cron, permissions, token handling, updater targets,
  changelog behavior, pinned `CONFCTL_FLAKE`, forward-only updates, package
  dependency/security checks, baseline/final ancestry guard and ordinary push.
- No generated input/dependency changes, database migrations, deployed state,
  protocols or machine configuration changes. No pin-update stream exists to
  consolidate.

## Completed quick checks

- `git diff --check`: pass.
- Workflow YAML parsed with repository-host Ruby/Psych: pass.
- Every extracted workflow `run` block checked with `bash -n`: pass (7 blocks).
- Structural inspection: exactly one `nix develop --profile` creation before
  the first updater, followed by 5 profile consumers; no later recreation.
- Normalizing only the six shell invocations and removing the rationale comment
  reproduces the exact original workflow. This checks the updater contracts
  listed above were preserved.
- Current diffstat: one file, 8 insertions, 6 deletions.
- `nix shell github:NixOS/nixpkgs/718f670e845328e9c2cecdd832835712b2cbd065#actionlint -c actionlint .github/workflows/daily-update.yml`:
  pass (actionlint 1.7.12).
- Feature-worktree bootstrap and lint batch: exit 0, 53 seconds; fresh installed
  policy Luna/low utility `/root/b1_bootstrap_lint_watcher`, no surviving
  operations. Exact command `bash /tmp/scheduled-workflow-fixes-b1/bootstrap-and-lint.sh`,
  log `bootstrap-and-lint.log`, receipt `bootstrap-and-lint.result` beneath the
  same temporary evidence directory.
- Ordinary feature commit through the saved profile: pre-commit Nixfmt and all
  commit-message hooks passed. TextWidth emitted two non-failing 72-column
  warnings; the message satisfies the repository's 80-column rule.

## Final source and publication receipts

Complete base-to-head series (one commit):

```text
6e9ed6fb3ded5d72fbfa31c3feb4fccfcdfee494  origin/master base
355e269f034422bb042f6c39fdab1725855b47e0  ci: reuse the initial daily update shell
```

After commit, `git fetch origin` and saved-profile `git rebase origin/master`
reported the branch up to date. Final range `git diff --check` passed, and
worktree/index are clean. Published with saved-profile
`git push -u origin 2026-11-13-scheduled-workflow-fixes`; `git ls-remote` then
proved the exact feature head above and unchanged remote master base above.
No default-branch content was changed. The portal comparison was captured at
the final head.

[Complete published comparison](https://github.com/vpsfreecz/vpsfree-cz-configuration/compare/6e9ed6fb3ded5d72fbfa31c3feb4fccfcdfee494...355e269f034422bb042f6c39fdab1725855b47e0).
The final diff is solely six profile-invocation changes and the two-line
rationale comment; no superseded commits or alternate implementations remain.
Whole-branch provenance: **no migrations and no dependency/pin update streams**.

Unchanged `flake.lock` SHA-256:
`0b473e0c2c00516d65a5e79c5ec9926aee815b2ea8757b235eea835af8b2934b`.
The initial shell's exact environment derivation is
`/nix/store/gm1nq01cb9gz3ag27v3ic44iadd4x34x-nix-shell-env.drv`.
Feature worktree Ruby matches the fixture executable below; its GEM_HOME is
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-13-scheduled-workflow-fixes/vpsfree-cz-configuration/.gems/ruby/3.4.0`.
`worktree-environment.json` records all native-gem paths.

## Profile fixture: passed

Disposable source: `/tmp/scheduled-workflow-fixes-b1/fixture`, exact initial
revision `6e9ed6fb3ded5d72fbfa31c3feb4fccfcdfee494`. Fixture uses the actual
repository flake/lock, Gemfile/lock, Overcommit configuration and custom Nixfmt
plugin. The fixture is outside feature source and has no push operation.

Command: `bash /tmp/scheduled-workflow-fixes-b1/run.sh`.

The command saves the initial shell to
`/tmp/scheduled-workflow-fixes-b1/daily-update-dev-shell`, records exact Ruby,
GEM_HOME/GEM_PATH/BUNDLE_PATH and successful native date/Overcommit loading,
installs/signs the real hooks, then replaces fixture flake evaluation with a
deliberate throw. The direct flake command must fail while the saved-profile
command must retain identical native loading/environment and perform a real
formatted-Nix commit through the configured hooks. It checks the profile store
target is unchanged.

Passed with exit 0 in 51 seconds. Initial and reused probe JSON are identical:

| Identity | Exact result |
| --- | --- |
| Saved profile store target, unchanged before/after | `/nix/store/y90v3dxkpg33x4ar6vn968cdflwn5wwi-nix-shell-env` |
| Ruby executable / realpath | `/nix/store/3rcm37q1arwggzjxzcnbiz5s8a7c1ppx-ruby-3.4.9/bin/ruby` |
| GEM_HOME | `/tmp/scheduled-workflow-fixes-b1/fixture/.gems/ruby/3.4.0` |
| BUNDLE_PATH | `/tmp/scheduled-workflow-fixes-b1/fixture/.gems` |
| Native date extension | `/tmp/scheduled-workflow-fixes-b1/fixture/.gems/ruby/3.4.0/gems/date-3.6.0/lib/date_core.so` |
| Overcommit | `/tmp/scheduled-workflow-fixes-b1/fixture/.gems/ruby/3.4.0/gems/overcommit-0.73.0` |
| Fixture commit | `1218ad0838464374b3abef411779100155727a1b` |

The direct `nix develop -c true` command failed with the deliberate
`B1 fixture changed flake evaluation` exception. It updated only the disposable
fixture lock while evaluating the changed test flake. The saved profile bypassed
that evaluation and loaded the exact same native gems. Configured Nixfmt and all
commit-message hooks passed for the fixture commit. No hidden LoadError remained
in this frozen-shell fixture and no operation-owned work remains running.

Raw scripts, probe JSON, logs and receipts are disposable under
`/tmp/scheduled-workflow-fixes-b1/`; main log `fixture.log`, result
`fixture.result`, direct-control failure `changed-flake.log`.

Fresh native monitoring utility `/root/b1_profile_fixture_watcher` uses the
installed verification-watcher policy: `gpt-6-luna` / low / full_access from
`/nix/store/0s5dljmmfngj7ia2r9lfkxwydnfiz6b6-dev-workspace-0.2.0`, catalog digest
`f2d5a8909570f32bf65098940649922528d081974eefdb3bf678fb38e4ad568d` and matching
native utility `dw_e792014d07f1ab00a4e052aeb6fbc575674f9dbc9073f569`
(danger-full-access, never approvals).

## Setup and limitations

The first `dev-session worktree add` populated the checkout but its inherited
post-checkout Overcommit hook reported missing local gems. The wrapper completed
registration. Verified the owned checkout at the exact base with a clean index
and matching portal registration before editing. Required hooks will be
bootstrapped through the declared shell; none were bypassed.

The local Nix CLI is 2.34.9; the fixture verifies its actual profile behavior.
The architect verified the same interface against official Nix 2.35.6 used by
the current Actions installer. Local verification does not execute the hosted
runner itself.

No live workflow dispatch is appropriate because this workflow checks out and
pushes master. Local fixture validation cannot establish moving upstream inputs
will complete every scheduled updater. Real schedule validation follows separate
explicit default-branch integration approval, which is absent.

Revert the workflow commit to restore previous source behavior. The temporary
profile adds no persistent on-disk format or fleet rollout requirement.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-13-scheduled-workflow-fixes/)
