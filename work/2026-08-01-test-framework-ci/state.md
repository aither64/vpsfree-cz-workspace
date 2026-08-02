# Test framework and CI integration state

## Branches and worktrees

All integration branches are named `2026-08-01-test-framework-ci`.

| Repository | Base | Worktree |
| --- | --- | --- |
| vpsadminos | `origin/staging` at `fe1978673` | `worktrees/2026-08-01-test-framework-ci/vpsadminos` |
| vpsadmin | `origin/master` at `c67a09951` | `worktrees/2026-08-01-test-framework-ci/vpsadmin` |
| confctl | `origin/master` at `7bee58a` | `worktrees/2026-08-01-test-framework-ci/confctl` |
| terraform-provider-vpsadmin | `origin/master` at `1daa01a` | `worktrees/2026-08-01-test-framework-ci/terraform-provider-vpsadmin` |
| vpsfree-irc-bot | `origin/master` at `565c4b4` | `worktrees/2026-08-01-test-framework-ci/vpsfree-irc-bot` |
| vpsadminos-org-configuration | `origin/master` at `e437660` | `worktrees/2026-08-01-test-framework-ci/vpsadminos-org-configuration` |

## Progress

- Fetched all affected canonical bare repositories over SSH on 2026-08-01.
- Created separate integration worktrees from current upstream defaults.
- Reconstructed the intended functional histories with the inline and shared
  lifecycle commits squashed in all five repositories.
- Dropped the Nix store repair workaround from the vpsAdminOS series.
- Added symmetric `succeeds_with_retries` and `fails_with_retries` OSVM APIs.
- Added the runner job/GC lock, hooks, stale-marker handling, and a deterministic
  shell test in `vpsadminos-org-configuration`.
- No runner configuration activation is authorized for this initiative.

Current reviewed functional heads before generated dependency pins:

| Repository | Head |
| --- | --- |
| vpsadminos | `0b102133b917eea19ddf6f44bbac2302fb4698d4` |
| vpsadmin | `f2624db9a` |
| confctl | `231e335` |
| terraform-provider-vpsadmin | `5318fc0` |
| vpsfree-irc-bot | `d968903` |
| vpsadminos-org-configuration | `7087bb9` |

## Verification and review

Quick verification completed:

- vpsadminos: 163 test-runner specs and 92 OSVM specs passed; RuboCop inspected
  1,443 files without offenses; changed workflows passed actionlint; shared
  action scripts passed ShellCheck; all commit hooks passed.
- vpsadmin: commit hooks passed; the changed workflow passed actionlint; the
  Playwright page object passed `node --check`.
- confctl: 35 specs passed serially and RuboCop inspected 120 files without
  offenses; the changed workflow passed actionlint.
- terraform-provider-vpsadmin: provider and get-token Go tests passed; the
  changed workflow passed actionlint.
- vpsfree-irc-bot: 49 specs passed and RuboCop inspected 61 files without
  offenses; the changed workflow passed actionlint.
- vpsadminos-org-configuration: the deterministic GC coordination test,
  ShellCheck, nixfmt, and Overcommit passed. All three runner configurations
  built and produced generations at 22:25:57-58.
- GitHub reported `v7.0.1` as the latest release of both `actions/checkout` and
  `actions/upload-artifact`; the workflows use compatible `v7` major refs.

The mandatory standalone review was performed by
`/root/mandatory_test_framework_review`. It found two blockers, one important
finding, and one advisory naming issue:

- The runner unit's `ProtectSystem=strict` sandbox did not permit writes to
  the shared GC lock. `serviceOverrides.ReadWritePaths` now contains only the
  additional lock file, `/run/github-runner-nix-gc/lock`.
- The vpsAdminOS interruption commit also migrated image result evaluation.
  The migration is now the separate `github: share image test result
  evaluation` commit.
- Missing artifact inputs previously counted as a successful upload and could
  permit cleanup of unpublished failure state. The shared upload action now
  defaults `if-no-files-found` to `error` in the lifecycle commit.
- The module-autoload subject is now scoped as
  `tests: bound module-autoload log assertion`.

After these corrections, the 163 test-runner specs passed again, both changed
vpsAdminOS workflows and all four consumer workflows passed actionlint, and
the lifecycle shell scripts passed ShellCheck. The runner coordination test,
ShellCheck, and nixfmt passed; all three runner configurations rebuilt as
generation `2026-08-01--22-54-20`. Their generated runner units contain both
job hooks, the runner runtime directory, and the narrow GC lock
`ReadWritePaths` entry.

The first vpsAdminOS spec run inherited Nix's temporary `TMPDIR` and disagreed
with three expectations for the product default `/tmp`; rerunning with
`TMPDIR=/tmp` passed. Full-repository actionlint also reported two pre-existing
ShellCheck info diagnostics in `kernels.yml`; both changed workflows passed
when checked directly.

Several overlapping confctl RSpec attempts initially collided in the fixed
`example.test` fixture generation and gcroot paths. After all duplicate
processes finished and only generated fixture state was moved to `/tmp`, one
serial run passed all 35 examples.

## Default integration

All integration branches were pushed over SSH and retained locally and
remotely. Fresh temporary worktrees fast-forwarded and pushed these defaults:

| Repository | Default | Integrated head |
| --- | --- | --- |
| vpsadminos | `staging` | `0b102133b917eea19ddf6f44bbac2302fb4698d4` |
| vpsadmin | `master` | `47fc93e3d9a4492bac13bb5a19b2763c23df02c7` |
| confctl | `master` | `9648e9ff78f4179a656e20000725994fe6b93d16` |
| terraform-provider-vpsadmin | `master` | `29c768aec86d9cdf2f145f7db7080ec3b4ef6884` |
| vpsfree-irc-bot | `master` | `af553fda06819b8f7518daf9d0d96700f0acb41f` |
| vpsadminos-org-configuration | `master` | `7087bb9cfc3733026a2dc048b58b7a613aa3ecc4` |

At the time of integration, the runner configuration was merged only. This
initiative neither built an activated generation nor deployed it to a runner.
It was activated separately afterward, as demonstrated by the extensionless
hook paths reported by `gh-runner2.int.vpsadminos.org` in job `91497114963`.

Final shared-action and lock verification:

- all four remote consumer workflows pin vpsAdminOS
  `0b102133b917eea19ddf6f44bbac2302fb4698d4`;
- vpsAdmin and confctl lock that same direct vpsAdminOS revision;
- the provider and IRC bot lock vpsAdmin
  `47fc93e3d9a4492bac13bb5a19b2763c23df02c7` and inherit the same vpsAdminOS
  revision.

Exact-head GitHub results used before integration were green for vpsAdminOS
RSpec, RuboCop, and changed-image CI; vpsAdmin WebUI PHPUnit, client,
libnodectld, and i18n workflows; confctl RSpec and RuboCop; and IRC RSpec. The
long aggregate/integration workflows were not awaited. At the final status
check they were queued or in progress with no current-head failures.

## Event branch refresh

Every distinct repository with an existing
`2026-06-15-vpsadmin-events` branch now has its actual GitHub default as an
ancestor. Local and remote heads match and all corresponding worktrees are
clean:

| Repository | Event head | Result |
| --- | --- | --- |
| vpsadminos | `0b102133b` | Equal to `staging`; obsolete framework series removed |
| vpsadmin | `9e8625583` | 109 event commits rebased onto `47fc93e3d` |
| confctl | `9648e9f` | Equal to `master`; obsolete framework series removed |
| terraform-provider-vpsadmin | `29c768a` | Equal to `master`; obsolete framework series removed |
| vpsfree-irc-bot | `af553fd` | Equal to `master`; obsolete framework series removed |
| haveapi | `0e1e67e` | Already based on current `master` |
| vpsadmin-go-client | `cbb8285` | Already based on current `master` |
| vpsadmin-kb-captures | `81c5ca0` | Final capture commit amended to pin rebased vpsAdmin `19a4a63c` |
| vpsfree-notification-templates | `6dda345` | Already based on current `master` |
| vpsfree-cz-configuration | `f9b537ae` | Functional commits rebased and exact pins regenerated with `confctl` |
| vpsfree-sms-gateway | `af7b3faf` | The event branch is the repository default |

The renamed `vpsfree-mail-templates` clone points to the same GitHub repository
as `vpsfree-notification-templates`; its local alias was synchronized to
`6dda345` without a duplicate push.

The configuration branch discarded five obsolete intermediate pin commits,
retained seven patch-equivalent functional commits, and generated two final
input commits. It resolves vpsAdmin services to `19a4a63c`, notification
templates to `6dda345a`, and the SMS gateway to `af7b3faf`.
`vpsadmin-kb-captures` passed `nix develop -c bin/check` after repinning.

Superseded vpsAdmin event run `30710962728` targeted old head `2a3f4523f` and
was canceled after the force-push. Current-head short vpsAdmin checks and the
configuration event-i18n workflow are green; the replacement aggregate run was
left queued as requested.

The initiative is complete. Long aggregate workflows may continue, but none is
a merge or completion gate for this integration.

## Operational notes

- The shared workspace checkout contains unrelated user changes. Only this
  initiative's plan/state paths may be staged for its coordination commits.
- Overcommit hooks are installed and signed in every repository that declares
  them. The provider declares no hook framework.

## Post-integration vpsAdmin master CI investigation

Run `30718729692` tested vpsAdmin `master` at
`47fc93e3d9a4492bac13bb5a19b2763c23df02c7`. The aggregate runner completed
all 117 tests: 116 succeeded and only `webui#navigation-readonly` failed.
The retained artifact showed that Playwright failed while loading the spec,
before any browser assertion, because it tried to read
`../../../../VERSION` relative to the Nix-store-packaged suite. That path
normalizes to `/VERSION`, which does not exist. The event branch already fixes
this exact issue in `9e8625583` (`tests: pass the packaged WebUI version`) by
passing the deployed version alongside the revision. The same WebUI test
succeeded in event-branch run `30719120204`, corroborating the diagnosis.

No implementation change was made during this investigation. GitHub retains
the source failure artifact for 14 days.

## Post-integration vpsAdmin remediation

The master-targeted branch `2026-08-01-test-framework-ci` now adds two focused
commits on `47fc93e3d`:

- `7f659e385` `tests: pass the packaged WebUI version`;
- `a1e999590` `nixos: publish API database config atomically`.

Both repository commits ran the active Overcommit hooks from `nix develop`;
Nixfmt, migration checks, WebUI i18n, and API i18n passed. The focused WebUI
revision/version flake check passed. Both affected integration-test names
evaluate and select correctly. The complete services NixOS system built to
`/nix/store/7a7ql1la9jfmbsbir0n6m9inpkyh0p8j-nixos-system-vpsadmin-services-26.05pre-git`.
Its generated API pre-start script creates a private sibling file, renders the
substituted database configuration, sets mode 0440, and only then renames it
over the live path. JavaScript syntax passed. ShellCheck passed for the
generated script with only pre-existing `SC2086` excluded for the unchanged
`basename $v` expression.

The first ambient-shell commit attempt was correctly blocked because the hook
dependencies were absent; rerunning the commits through the root Nix shell
passed every mandatory hook. The documented WebUI dev shell also lacks Node,
so the syntax check used `nix shell nixpkgs#nodejs`. These tool-selection
details did not affect repository content.

Standalone mandatory review found no Blocking, Important, or Advisory issues.
It confirmed the commit split, packaged-version metadata contract, atomic
same-filesystem publication, restrictive temporary permissions, unchanged
configuration format, and safe rollback. The residual gap is the lack of a
deterministic concurrent-reader regression test; the master and rebased-event
aggregate runs provide the planned end-to-end validation. During the event
rebase, its setup-serialization commit must preserve the atomic sequence inside
the existing `flock`, and its duplicate WebUI fix must be dropped as upstream.

## Runner hook suffix failure

vpsAdmin replacement master run `30748100208` and the identical-head work
branch run `30748085213` failed before checkout. GitHub Actions rejected the
configured job-start and job-completion hooks because their Nix store paths did
not end in `.sh`, `.ps1`, or `.js`. The earlier
`vpsadminos-org-configuration` change used extensionless names with
`pkgs.writeShellScript`; it had since been activated outside the initiative,
despite the earlier state recording that this initiative did not deploy it.

Commit `f924aab` (`gh-runner: give job hooks recognized script suffixes`) adds
`.sh` to both generated script names without changing the GC coordination
protocol. The active Overcommit Nixfmt hook passed. A complete configuration
build for `org.vpsadminos/int.gh-runner1` passed and produced derivations named
`github-runner-job-started.sh` and `github-runner-job-completed.sh` as required.
The correction requires activation on all three GitHub runner machines before
replacement CI can start successfully.

The current request to find and fix the CI root causes and then watch both
replacement aggregate runs requires this activation; source integration alone
cannot make any self-hosted job pass. Before rollout, an organization-runner API
query was denied by the available token, while direct connection tests to all
three private runner addresses timed out. Activation is therefore pending a
network path or operator with runner access. The independent mandatory review
found no Blocking or Important issue and one Advisory issue: update the stale
activation record and drain each runner before switching it. The record is now
corrected; a live post-activation job remains required to verify both hooks.

After rebasing over an automated input update, the reviewed suffix fix is
`f924aabd0a774d88d173419527215cf4b538168a` and is present on both
`vpsadminos-org-configuration` `master` and its retained initiative branch. A
complete build of all three runner configurations produced confctl generation
`2026-08-02--14-56-01`. Deployment was not attempted because this host cannot
connect to `172.16.4.21`, `172.16.4.22`, or `172.16.4.25`, and the available
GitHub token cannot report organization-runner busy state. Draining cannot be
verified safely from the present environment.

vpsAdmin `master` is at `a1e999590e2559ffb205e6c7e1d53f81c96673c5`.
The event branch was rebased onto it and force-pushed at
`e5ee3f056eec97c7d5d9276b9aa95460aaee7bae`. Range-diff retained all 108 event
commits patch-equivalently except the setup-serialization commit, which now
keeps atomic database configuration publication inside its `flock`; the 109th,
duplicate WebUI version fix was dropped as upstream. Nixfmt, the focused WebUI
flake check, JavaScript syntax, both exact test-selection evaluations, and
`git diff --check` passed on the rebased branch.

Replacement aggregate runs `30748100208` (`master`) and `30748413419` (event
branch) both failed during runner setup with the same extensionless-hook error.
They contain no integration-test result. Once generation
`2026-08-02--14-56-01` is activated on the drained runners, rerun both exact
workflow attempts and monitor them through completion.
