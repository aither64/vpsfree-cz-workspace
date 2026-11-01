# Verification evidence

Final source revisions are in final-heads.json. The browser and build runner
checks exact heads and clean tracked content before execution. Every operation
uses the relevant repository's Nix environment.

Quick checks passed: git diff --check, browser JS syntax, and
TestShippedBrowserClientMatchesSessionAPI (Go 1.102 seconds).

Focused TestQuestionBrowser/mode_refresh_browser_test.cjs passed in 11 seconds
at runtime a8934bda. It covers initial notice grace, confirmed/pending/recovered
modes, usable explicit controls, hidden-tab and page restoration, failure grace,
distinct mode saves, stale reads, hashes completing after saves, panels displayed
while saves are pending, and thread replacement. Evidence: mode-browser.log and
mode-browser.status (0).

The first all-browser run was canceled deliberately to correct the new test's
fixture order; verification-canceled.* retain its outcome. mode-browser-launch-failed.*
record a launcher error before tests, which was corrected after inspection.
Neither interrupted attempt is accepted as verification.

The final related batch ran all TestQuestionBrowser subtests, the runtime
package check, the composed workspace package, the semantic deployment contract,
confctl build cz.vpsfree/machines/aitherdev, and observes exact runtime GitHub
run 38161519600. Execution is owned by fresh Luna/low watcher /root/final_verification.
Results: verification.log, verification.status and verification.phase; ci.log
contains the exact-head workflow observation. Package output is candidate-package.

Full TestQuestionBrowser passed at the final runtime in 217.948 seconds.
Runtime and composed packages passed. The composed package is
/nix/store/sfsck9wxbhkrzl5qygcxxm096bmhdg5v-dev-workspace-0.2.0.
The Ruby lifecycle suite reports 405 runs, 5463 assertions, no failures/errors,
and 12 expected skips; other package suites also pass.

The batch stopped before the host build at confctl's ordinary confirmation
prompt because stdin was closed. Failure evidence was inspected, and the pinned
command's help documents --yes. verify-host.sh repeats only that authorized host
build with --yes and confirms the final-head CI result. A fresh watcher owns this
operation; evidence is host-verification.log/status/phase. The original
verification.status remains 1, preserving the partial batch's actual outcome.
The remaining host build passed in 2m10s with host-verification.status 0;
generation 2026-10-11--20-27-19 selected candidate-system.txt. CI 38161519600
completed successfully for the exact final runtime (ci-result.json):
https://github.com/aither64/dev-workspace/actions/runs/38161519600.
Together, the completed batch phases and host follow-up cover every planned
verification phase without repeating successful tests or concealing the EOF.

Live checks in pre-deploy.py/post-deploy.py and rollout.sh also passed, with
rollout.status 0, phase complete and independent unit exit status 0. They guarded
exact clean source heads and predeployment profile/native identity, then compared
served JS/CSS bytes and template cache version, selected application/system
outputs, and native/tmux PID plus start identity. Read-only HTTP verification
used the local UNIX socket without credentials in artifacts. Actual execution,
selected outputs and launcher transport diagnostics are in [rollout.md](rollout.md).

After the approved master integration, runtime master CI 38167063056 also passed
for the same exact a8934bda head, with watch exit 0. Both the fast package/focused
job and additional host VM activation/recovery job succeeded. Evidence is
merge-ci-result.json/status and [integration.md](integration.md).
