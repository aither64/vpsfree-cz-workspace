# C1: vpsadminos.org pre-commit plugin signing

Current consolidated head is `8306d29d09f1939d1f92d44b5a5e241429b40c2e`,
including the bounded manual-trigger follow-up described below. The original
reviewed delivery evidence is retained here for exact-range provenance.

Owner: implementer1. C0 was accepted and C1 allocated by lead. Implemented the
sufficient architect-owned C1 brief in [design.md](design.md) without deviation.
Diagnosis and run links remain in
[evidence-vpsadminos-org-configuration.md](evidence-vpsadminos-org-configuration.md).

## Complete review range

- Repository: `git@github.com:vpsfreecz/vpsadminos-org-configuration.git`.
- Registered branch: `2026-11-13-scheduled-workflow-fixes`.
- Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-13-scheduled-workflow-fixes/vpsadminos-org-configuration`.
- Base: `ca96c95a1fee04793468785d8323a759615b2b4e`.
- Final head: `cdb886678ba30d10b5114cab279d5eb602209954`.
- Complete series: one commit, `cdb8866 ci: sign the custom pre-commit plugin before updating inputs`.
- Complete diff: one insertion in `.github/workflows/daily-update.yml` after the
  existing configuration signing command:

  ```sh
  nix develop -c bundle exec overcommit --sign pre-commit
  ```

Schedule, actions, permissions, configuration signing, confctl pin, authentication,
channels, forward-only updates, final lock check, caching and push are unchanged.
No generated updates, migrations, dependency/pin streams, obsolete approaches or
transitional commits exist in this branch. No migration was merged, released,
deployed or externally consumed. No machine deployment is required.

Signing trusts the checked-out custom Nixfmt plugin locally in the disposable
Actions checkout, enabling its normal checks during generated commits. Revert
the workflow commit to recover prior source behavior. No lasting repository
documentation was useful for this self-explanatory command; failure semantics,
upstream CLI evidence and validation limits remain in session evidence.

## Environment and quick checks

Session identity and both environment markers were reverified. No repository
`AGENTS.md` exists at the fetched base. Relevant workflow, hook, bundle and shell
sources were read. The worktree was created/registered through `dev-session`.

Uncertain environment setup used a fresh Luna/low native verification utility
under the monitoring skill. Resolved installed package:
`/nix/store/0s5dljmmfngj7ia2r9lfkxwydnfiz6b6-dev-workspace-0.2.0`,
catalog `f2d5a8909570f32bf65098940649922528d081974eefdb3bf678fb38e4ad568d`,
native utility `dw_e792014d07f1ab00a4e052aeb6fbc575674f9dbc9073f569`,
full access / approval never. It completed with exit 0 in about two minutes;
all operation-owned tool sessions ended, with no kernel build.

Exact bootstrap command in the feature worktree:

```sh
nix develop --profile /tmp/2026-11-13-scheduled-workflow-fixes-c1-shell \
  -c bash -c 'ruby --version; bundle check; command -v nixfmt; command -v ruby; command -v bundle'
```

The profile resolves to `/nix/store/hzcy03kfm6qbyir2zjzp037zwn02k9vz-nix-shell-env`.
Ruby 3.3.10, satisfied locked bundle and nixfmt 1.2.0 were available. Later local
checks reused this exact profile with `nix develop <profile> -c ...`.
`flake.lock` stayed unchanged at blob `e1cd77561f9e0b54181acf69740e93b304eae69f`;
`Gemfile.lock` blob `88de2e53cafa9e015fb614387274a6dc2095ddb5` selects
Overcommit 0.68.0.

| Check | Result |
| --- | --- |
| Repository-shell YAML parse via Ruby `YAML.load_file` | Passed |
| `bash -n` on all five parsed workflow `run` blocks | Passed |
| Assert exact install/config-sign/plugin-sign command order | Passed |
| Fresh disposable real-hook fixture described below | Passed |
| `git diff --check`, including complete committed range | Passed |
| Actual worktree Overcommit install/config/plugin signing | Passed |
| Final commit with repository hooks enabled | Pre-commit Nixfmt and all commit-msg hooks passed |
| Fresh `git fetch origin` before commit/publication | Base unchanged; no rebase needed |
| SSH feature push plus independent `git ls-remote` | Feature equals final head; master equals base |
| Feature-branch workflow query | Zero runs; no workflow dispatch |

The final commit used `git commit -F` under the realized repository shell.
Commit-msg TextWidth emitted advisory warnings for three body lines over 72
columns; all lines meet the workspace's 80-column limit and hooks exited 0.
No hooks were disabled or skipped. No test code was added to the repository.

## Faithful hook fixture

Exact command in the feature worktree:

```sh
nix develop /tmp/2026-11-13-scheduled-workflow-fixes-c1-shell \
  -c bash /tmp/2026-11-13-scheduled-workflow-fixes-c1-fixture.sh
```

The script copied actual `.overcommit.yml`, `Gemfile`, `Gemfile.lock` and
`.git-hooks` into a newly initialized Git repository, using the same installed
bundle. Source blobs: `bb5335147a1edded5d071a7eba6421c857c07c95` for configuration,
`a56ae446c5fd39cabe4e815221bfa20b503d83c5` for the actual Nixfmt plugin.

1. Installed hooks and signed configuration only. A real formatted-Nix commit
   failed with `Nixfmt` and `overcommit --sign pre-commit`; no HEAD was created,
   faithfully reproducing the scheduled failure.
2. Ran `bundle exec overcommit --sign pre-commit`. A real commit of a formatted
   Nix attribute set passed Nixfmt and commit-msg hooks, creating fixture commit
   `abe657360a8f902a5f2dc4dc22f22fbdc905c6ca`.
3. Replaced the fixture with `{ answer=42; }` and tried another real commit.
   Nixfmt reported `not formatted` and rejected it. HEAD stayed at the successful
   fixture commit.

Fixture exit status: 0. No mocks, hook bypasses or changed configuration inputs.
Disposable active-session review artifacts:

- `/tmp/2026-11-13-scheduled-workflow-fixes-c1-environment.log` and `.exit`.
- `/tmp/2026-11-13-scheduled-workflow-fixes-c1-fixture.sh` and `.log`.
- `/tmp/2026-11-13-scheduled-workflow-fixes-c1-fixture.GFyG7R`, including
  `unsigned.log`, `formatted.log`, and `unformatted.log`.

## Publication and remaining gates

SSH push created only `refs/heads/2026-11-13-scheduled-workflow-fixes`. Fresh
`git ls-remote` proved feature `cdb886678ba30d10b5114cab279d5eb602209954` and
master `ca96c95a1fee04793468785d8323a759615b2b4e`. Worktree is clean.
`dev-session worktree capture-comparison` recorded the same base/head.

Implementation and quick checks are complete and published for lead acceptance
and independent final review. Final branch readiness awaits that review,
including its whole-series/no-migration conclusion. No merge, PR, deployment or
default-branch mutation was performed. Session remains active and open.

CI gap: the local fixture establishes signing and formatter enforcement, but
does not establish that today's remote inputs pass the complete updater. The
schedule-only workflow checks out and pushes master, so it was not dispatched
for feature validation. After separately approved integration, an actual
scheduled run can validate updater completion. No full machine build is needed.

## Manual-trigger amendment after original final review

Lead confirmed the original exact-head final review complete and accepted its
ranges for planned acceptance. The sole Important finding for C1/E1 was missing
manual triggers needed for the user's approved immediate post-integration runs.
G1 remains explicitly parked on review/lead release; implementer1 owns this
bounded C1 follow-up and does not run G1 acceptance concurrently.

Read the sufficient `C1/E1 manual-trigger amendment` brief in `design.md` before
editing. Added only the empty `workflow_dispatch:` sibling to `schedule:`.
No custom inputs, schedule/action/job/checkout/auth/guard/update/push changes.
Lead's detached target checkout and its hooks were not touched.

| Range | Base | Head |
| --- | --- | --- |
| Original reviewed | `ca96c95a1fee04793468785d8323a759615b2b4e` | `cdb886678ba30d10b5114cab279d5eb602209954` |
| Consolidated final | `ca96c95a1fee04793468785d8323a759615b2b4e` | `8306d29d09f1939d1f92d44b5a5e241429b40c2e` |

The complete final series contains one logical commit,
`8306d29 ci: fix hook signing and allow manual daily updates`, changing one file
with two insertions relative to master. There are no superseded commits,
migrations or dependency/pin update streams. The original hook-signing insertion
is retained exactly. `git range-diff` maps the old one-commit series to the new
one-commit series, showing only the trigger insertion and updated commit message.

Exact old-head to new-head source diff:

```diff
 name: Daily update
 on:
+  workflow_dispatch:
   schedule:
     - cron: '40 4 * * *'
```

Focused checks passed under the same realized C1 repository environment:

- Ruby YAML parsing accepts both events; dispatch value is empty and cron is
  exactly `40 4 * * *`.
- Removing the new trigger reproduces old workflow bytes exactly and parsed
  structure exactly. This establishes equivalence of every remaining setting
  and command, including all unchanged `uses:` refs.
- All five `run` blocks pass `bash -n`; `git diff --check` passes.
- Actual amendment commit passes Nixfmt and all commit-msg hooks cleanly.

Command: `nix develop /tmp/2026-11-13-scheduled-workflow-fixes-c1-shell -c ruby
/tmp/2026-11-13-scheduled-workflow-fixes-c1-trigger-check.rb`. Raw commit log:
`/tmp/2026-11-13-scheduled-workflow-fixes-c1-trigger-commit.log`. A separate
actionlint bootstrap and unchanged real-hook fixture were unnecessary for this
trigger-only addition; parsing, explicit trigger semantics, exact remainder
comparison and shell syntax cover the changed lane. Existing action validation
and real-hook fixture evidence above remain applicable.

Fresh fetch left master at the same base. Published the consolidated feature
with exact lease `refs/heads/2026-11-13-scheduled-workflow-fixes:cdb886678ba30d10b5114cab279d5eb602209954`.
Fresh remote verification and comparison capture use the new exact range.
The feature-branch run list is empty, so there are no superseded branch runs to
cancel. No dispatch, default-branch mutation, merge or deployment was performed.

Ready for the reviewer's focused general/risk follow-up on the new full range.
Unchanged checks are reused only for their proven scope. After reviewed
integration and remote-master proof, the lead owns `--ref master` dispatch and
run identity/result recording. Member retains C1 failure-diagnosis ownership.
Removing the trigger restores prior entry-point behavior; no persisted state or
deployed format changes. G1 can resume only after this amendment is reported
for acceptance/capacity and lead releases its real acceptance.
