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

The runner configuration was merged only. It was not built into an activated
deployment and was not deployed to any runner.

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
