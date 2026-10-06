---
lifecycle: active
---
# 2026-08-03-vpsadmin-ci-failure

## Repositories

- `vpsadmin`
  - branch: `2026-08-03-vpsadmin-ci-failure`
  - worktree: `worktrees/2026-08-03-vpsadmin-ci-failure/vpsadmin`
  - base at creation: `origin/master` / `ae5dd5e01`

## Status

The precise server-side exception cannot be recovered from the historical CI
artifact. Per the user's decision, the retry and its synthetic regressions were
removed. The final branch keeps nested WebUI service diagnostics and the
independently discovered Playwright navigation synchronization fix. The two
commits were fast-forwarded into `master` and pushed. Exact-master CI passed on
attempt 2 after attempt 1 was terminated by self-hosted runner disk quota.

## Commands run

- `bin/dev-session current`
- `gh run view 30748100208 --repo vpsfreecz/vpsadmin ...`
- `gh run download 30748100208 --repo vpsfreecz/vpsadmin ...`
- `gh api repos/vpsfreecz/vpsadmin/actions/runs/30748100208/attempts/1/jobs`
- `git --git-dir=repos/vpsadmin.git fetch origin`
- `git --git-dir=repos/vpsadmin.git worktree add ...`
- `gh run list --repo vpsfreecz/vpsadmin --workflow CI --limit 50 ...`
- inspected failed logs from nine nearby workflow runs for the same signature
- `./test-runner.sh test 'webui#transactions'`
- JavaScript and Ruby syntax checks plus `git diff --check`
- installed the root and API bundles required by repository hooks
- refreshed the local signature for the changed `VpsadminApiI18n` hook
- committed through Overcommit; all declared pre-commit hooks passed for all
  three commits
- after the final history rewrite, the full-tree hook run passed Nixfmt,
  MigrationSpecs, VpsadminWebuiI18n, RuboCop, and PhpCsFixer; the API i18n hook
  was then run in `nix develop .#api` and passed (the full-run wrapper had
  incorrectly leaked the root Bundler environment into that component hook)

## Results

- Attempt 1 failed during self-hosted runner setup before checkout or tests.
- Attempt 2 ran the selected CI suite; only `webui` failed.
- The failing Playwright example was the first example in
  `webui#transactions`. OAuth authorization proceeded, but the redirect to
  `webui.vpsadmin.test` returned HTTP 500. Four following transaction examples
  logged in and passed.
- Full test logs were downloaded from artifact `8836976149` and inspected at
  `/tmp/vpsadmin-ci-30748100208`.
- The artifact contains host service journals and database diagnostics, but it
  does not contain the nginx or PHP-FPM journal from the nested `webui` NixOS
  container. The discarded journal is the only place the precise PHP failure
  from the transient callback response would have been recorded.
- Nine nearby failed workflows all completed `webui#transactions`
  successfully; none contained the same WebUI HTTP 500 signature.
- The exact `webui#transactions` script passed locally, including all five
  Playwright examples, in 954.49 seconds.
- WebUI HTTP failures remain test-fatal; no retry or recovery behavior is part
  of the final branch.
- Unexpected script failures will now collect failed services and nginx /
  PHP-FPM journals from the nested WebUI container.
- Rewritten commit series:
  - `c970e2c12 tests: collect WebUI container failure logs`
  - `e3693d516 tests: avoid implicit WebUI login navigation wait`

## Mandatory change review

- Standalone review completed after the initial two-commit series.
- No blocking findings, advisory findings, compatibility issues, production
  impact, or security impact were reported.
- Important finding: the injected-500 test covered successful recovery but did
  not lock in the two-attempt limit, the non-5xx boundary, or cookie clearing.
- Resolution: added regressions that verify a persistent 5xx stops after two
  callback attempts, a 4xx is attempted only once, and a sentinel cookie is
  absent from the recovered callback. Rewrote the unpublished first commit and
  reran all repository hooks successfully.
- Follow-up review approved the exact-origin route matching, bounded negative
  cases, cookie clearing, and explicit post-click synchronization.
- Follow-up blocking finding: the separately discovered implicit navigation
  wait fix was independently reviewable. Resolution: split it into commit
  `7e31b3e33` and reran all hooks.
- Failure-time journal collection was initially only syntax/static checked, but
  targeted integration attempt 1 subsequently exercised it end to end.
- Final post-integration review found the tree functionally sound and approved
  the isolated integration rerun, but blocked on folding the follow-up login
  synchronization commit into the original retry commit. It also advised
  restricting response classification and test interception to the main frame.
- Resolution: folded the follow-up into the retry commit, added explicit
  main-frame checks, reduced the series back to three independently valid
  commits, and reran syntax, whitespace, and every declared hook successfully.

## Targeted auth integration attempt 1

- `./test-runner.sh test 'webui#auth'` failed after 1019.11 seconds.
- Playwright result: 16 passed, 4 failed in 6.9 minutes.
- The three new injected-response tests did not intercept the OAuth callback:
  the `${webuiBaseURL}/**` route glob does not match the WebUI root path when
  the callback is expressed only in the query string. Normal login succeeded,
  so the negative expectations correctly exposed the test defect.
- The existing invalid-password test also exposed a separate implicit
  navigation-wait race on the anonymous WebUI login button: the click completed
  and navigation began, but Playwright's click wait timed out after 15 seconds.
- Follow-up: route WebUI requests by exact origin and use the helper's existing
  explicit URL/locator synchronization after the anonymous login click.
- The failed run exercised the diagnostics hook end to end. `services-shell.log`
  contains the nested WebUI container's nginx and PHP-FPM journal, including
  both verified unit startups.

## Targeted auth integration attempt 2

- `./test-runner.sh test 'webui#auth'` failed after 231.11 seconds, before
  Playwright or fixture setup.
- `services-console.log`: QEMU could not connect to its virtiofsd socket because
  the socket path did not exist.
- `node1-console.log`: QEMU's virtiofsd connection was refused.
- Both machine logs record immediate QEMU exit status 1, followed by runner
  teardown; the top-level symptom was `stream closed in another thread`.
- The failed attempt executed none of the changed browser behavior.

## Targeted auth integration attempt 3

- `./test-runner.sh test 'webui#auth'` failed after 76.35 seconds, again before
  Playwright or fixture setup.
- Both machine consoles reported missing virtiofsd sockets and immediate QEMU
  exit, matching attempt 2.
- Process inspection found another development session concurrently running
  `webui#support-pages` in the default `/tmp/os-test-runner` state directory.
  Its active services and node VMs used the same deterministic
  `74bd7b23-services-fs-vmSharedDir.sock` and related socket namespace as these
  attempts.
- Root cause: independent local runner invocations shared the default state and
  socket directory. Cleanup and socket lifecycle from overlapping `webui` tests
  collided. The other session was left untouched. Further validation will use
  the runner's documented `--state-dir` option with an initiative-specific
  directory.

## Targeted auth integration attempt 4

- `./test-runner.sh test --state-dir
  /tmp/os-test-runner-vpsadmin-ci-failure-20260803 'webui#auth'` used an
  isolated state and socket directory. Both VMs booted normally and Playwright
  ran all 20 examples.
- Result: 17 passed and the three new injected-response examples failed in 6.8
  minutes. All existing examples, including the implicit-navigation regression,
  passed.
- The injected routes never matched the OAuth return, so each example completed
  a normal login: the transient counter remained zero and both negative login
  promises resolved.
- Initial resolution, superseded by attempt 5: match the OAuth return as the
  next main-frame WebUI document after a login kickoff instead of assuming a
  particular callback query, and evaluate recorded main-frame 4xx/5xx
  responses after credential navigation.

## Targeted auth integration attempt 5

- `./test-runner.sh test --state-dir
  /tmp/os-test-runner-vpsadmin-ci-failure-final-20260803 'webui#auth'` again
  used an isolated state directory. Both VMs and their virtiofsd sockets were
  healthy; Playwright ran all 20 examples.
- Result: 17 existing examples passed and the same three injected-response
  examples failed in 6.1 minutes because no synthetic response was injected.
- A minimal Playwright redirect reproduction identified the exact test defect:
  route handlers run only for the first URL in an HTTP redirect chain. Routing
  the WebUI login kickoff therefore cannot intercept its API redirect target,
  and routing does not begin mid-chain when the API credential POST redirects
  back to the WebUI.
- Resolution in `adf71fe3e`: route the API credential POST and return a small
  script that starts a new client-side WebUI navigation, then fulfill that
  routable document with the injected response. The login helper polls the
  logout control and recorded document errors with no abandoned assertion
  promise.
- The complete flow was verified locally with the repository's exact
  Playwright and Chromium builds against fake WebUI/API servers: transient 500
  retried exactly once and cleared the sentinel cookie; persistent 500 stopped
  after two submissions; HTTP 400 stopped after one. JavaScript syntax,
  whitespace, and all commit-time hooks passed before the final autosquash.
- Final mandatory follow-up review of `adf71fe3e..7e31b3e33` reported no
  blocking, important, or advisory findings. It approved another isolated
  `webui#auth` run and confirmed all three commits are independently valid.

## Targeted auth integration attempt 6

- `./test-runner.sh test --state-dir
  /tmp/os-test-runner-vpsadmin-ci-failure-final2-20260803 'webui#auth'` used a
  fresh isolated state and socket directory. Both VMs booted normally.
- All 20 Playwright examples passed, including transient HTTP 500 recovery,
  the persistent-500 two-attempt limit, the non-retried HTTP 400 case, cookie
  clearing, and the anonymous login synchronization regression.
- The browser example passed in 347.64 seconds and `webui#auth` completed in
  681.56 seconds. Guest shutdown then waited for the configured five-minute
  `vpsadmin-webui-route-router.service` stop timeout; the complete runner
  exited successfully after 1208.3 seconds with one test successful.

## Root cause

The workflow failed because the first OAuth return navigation in
`webui#transactions` reached a WebUI document that returned transient HTTP 500.
Four later logins in the same script succeeded, the focused reproduction
succeeded, and the same script passed in all inspected nearby runs. That is the
observable failure signature, not the root cause of the server response.

The historical artifact cannot identify the lower-level PHP exception because
failure collection ran only on the outer services VM and omitted the nested
WebUI container journal. The final diagnostics change closes that evidence gap
for any repeated failure while deliberately leaving the HTTP 500 test-fatal.

## Cleanup

- Kept the local and remote feature branch refs after integration, as required
  by workspace policy.
- Removed the clean feature and temporary `master` merge worktrees, then
  removed the empty initiative worktree group.
- Deleted the five initiative-specific isolated runner state directories under
  `/tmp`; no active process or mount referenced them. Shared runner state and
  every other initiative's worktree were left untouched.
- Preserved this plan/state record and the durable local-runner collision note.

## Published validation

- Fetched `origin` after local validation; `origin/master` remained at
  `ae5dd5e01`, so the reviewed branch required no rebase.
- Pushed `2026-08-03-vpsadmin-ci-failure` over SSH at `7e31b3e33`.
- RuboCop run `30825096781` completed successfully.
- Integration CI run `30825096801` started on the same head after waiting for
  self-hosted runner capacity. Selection mode is full (`tag=ci`) because
  `tests/runner/extensions/after_test_script_run.rb` matches the intentional
  `tests/runner/**` full-suite rule. This run is superseded by the user's
  decision to remove the retry and will be cancelled after the rewritten
  branch is pushed.

## Final-scope decision

- The user chose not to hide a future server error behind a retry. The retry
  commit `adf71fe3e` and all synthetic retry tests were removed with
  `git rebase --onto origin/master adf71fe3e`.
- The user authorized fast-forward integration into `master`, pushing, and
  initiative cleanup after review and validation succeed.
- Quick verification of the rewritten two-commit series passed JavaScript and
  Ruby syntax checks, `git diff --check`, Nixfmt, MigrationSpecs,
  VpsadminWebuiI18n, RuboCop, and PhpCsFixer. The root Overcommit invocation
  again leaked its Bundler environment into `VpsadminApiI18n`; the exact API
  i18n health task passed in `nix develop .#api`.
- A fresh standalone mandatory review of `ae5dd5e01..e3693d516` reported no
  blocking, important, or advisory findings. It confirmed that no retry or
  synthetic retry tests remain, both commits are independently valid, nested
  journal collection is bounded/non-fatal, and the retained `noWaitAfter`
  click is followed by explicit URL/form synchronization. The only residual
  gap is an exact-HEAD isolated `webui#auth` run.
- Exact rewritten HEAD validation passed with
  `./test-runner.sh test --state-dir
  /tmp/os-test-runner-vpsadmin-ci-failure-no-retry-20260803 'webui#auth'`.
  All 17 Playwright auth cases passed; the browser example took 320.34 seconds,
  the script took 707.57 seconds, and the complete isolated run exited 0 with
  one test successful after 936.58 seconds.
- Refetched `origin`; `origin/master` remained `ae5dd5e01`. Replaced the remote
  feature branch using an explicit force-with-lease from `7e31b3e33` to
  `e3693d516`.
- Submitted cancellation for superseded integration run `30825096801`, whose
  head was `7e31b3e33`. New runs on the final head are RuboCop `30846949240`
  and integration CI `30846949184`.
- Superseded run `30825096801` completed as cancelled. RuboCop `30846949240`
  passed on `e3693d516`; integration CI `30846949184` started on the same head
  and is evaluating the full `tag=ci` selection required by `tests/runner/**`.
- Integration CI `30846949184` completed successfully on `e3693d516` after
  approximately three hours.
- Before integration, `origin/master` advanced to `2f9546ce8` (`webui: make
  translated spacing explicit`), including WebUI login files. Rebased cleanly
  onto that commit. `git range-diff` shows the two patches are identical; new
  commit hashes are `d7dc92835` and `6fb60827f`.
- Exact rebased-head validation passed with
  `./test-runner.sh test --state-dir
  /tmp/os-test-runner-vpsadmin-ci-failure-rebased-20260804 'webui#auth'`.
  All 17 auth browser cases passed; the browser example took 301.9 seconds,
  the script took 665.54 seconds, and the complete run exited 0 with one test
  successful after 910.23 seconds.
- Created fresh temporary target worktree
  `worktrees/2026-08-03-vpsadmin-ci-failure/vpsadmin-master-merge`, checked out
  `master` at `2f9546ce8`, and fast-forwarded it to `6fb60827f` with no merge
  commit. JavaScript/Ruby syntax and `git diff --check` passed there.
- Refetched `origin/master`, confirmed it remained `2f9546ce8`, and pushed the
  linear fast-forward `2f9546ce8..6fb60827f` to `master` over SSH.
- Master-triggered workflows: RuboCop `30860948808` and integration CI
  `30860948703`; both started on final head `6fb60827f`.
- Master RuboCop `30860948808` passed. Integration CI `30860948703` attempt 1
  was terminated outside the test workflow on
  `gh-runner2.int.vpsadminos.org`: the GitHub check annotation reports
  `System.IO.IOException: Disk quota exceeded` while writing
  `/var/lib/github-runner/runner/_diag/Worker_20260803-230350-utc.log`.
  GitHub left `Run tests` marked in progress and every artifact, evaluation,
  summary, cleanup, and post-checkout step pending. No workflow log or artifact
  exists for this attempt, so it produced no vpsAdmin test result.
- Repository runner registration status is not readable by the available token
  (`403`), but a later full CI job was accepted by
  `gh-runner3.int.vpsadminos.org` and is actively running. The failed master
  job will be rerun now that the infrastructure cause has been identified.
- Integration CI `30860948703` attempt 2 started on
  `gh-runner1.int.vpsadminos.org` as job `91894180841` and entered workflow
  execution normally.
- Integration CI `30860948703` attempt 2 completed successfully on exact master
  head `6fb60827f`. `Run tests`, result evaluation, summary, test-state cleanup,
  and checkout cleanup all passed. The job ran from 04:39:37 to 10:17:50 UTC;
  successful runs intentionally skipped failure-log upload and produced no
  artifact.
- While final CI ran, upstream `master` advanced to `d0efecb36` with a package
  dependency update. Verified `6fb60827f` is its ancestor and fast-forwarded
  the bare repository's local `master` ref to the new upstream tip; the two fix
  commits remain in the linear `master` history.

## Archival request, 2026-10-06

The workspace operator requested archival of sessions dated August 2026 or
older, retaining recorded work and branches. This checkpoint commits the
existing plan and active state before the ordinary archive transition.
