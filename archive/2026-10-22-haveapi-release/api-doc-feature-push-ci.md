# Expanded feature push and CI handoff

Only feature branch `2026-10-22-haveapi-release` was force-pushed over canonical SSH.
Exact final head `27b4f8f895a4e5401357a402187c2a4590699aec`, tree `4405e77d0510c2b0c9dda01d69722aa872bbd426`.
Fresh fetch and ls-remote verified target master `a32b15e379f44fc6dae4b15ef4ec17a142e5f465` and exact
prior feature lease `08345b2d5ede025972a3daec8b4a373efb51d711` before mutation. Push used the
explicit lease and exact SHA refspec shown in the JSON receipt; exited0.
Post-push remote proof matches final head exactly, master unchanged. No default,
official release branch, tag or registry mutation. No repository claim needed.

Top-level Nix with HAVEAPI_RELEASE_TOOLS_ONLY=1 supplied declared tools.
Executable Overcommit pre-push entrypoint was installed/enabled; no bypass.
The repository declares pre-commit/commit-msg checks, no additional PrePush
checks; all final source hooks passed as recorded in remediation receipt.
Root Nix refreshed cached tool closures before execution, with no gem installs
or source changes. Complete push output: api-doc-feature-push.log.

Tracked source clean/index empty after push. Known generated PHPcache and
__pycache__ preserved. All Git/hook/source/install ownership yielded to lead;
no pending commands and no checks run during the lead's immutable local watcher.
Original12 baseline dist entries retained separately by lead; expanded verification
is still pending. Lead fresh Luna watcher owns long local+CI monitoring.

Read-only gh run list observed these10 exact-head push runs; snapshot statuses
below are discovery evidence, not final conclusions. No CI wait or retries.
All older same-branch08345b2 runs were completed success. No superseded active
runs existed; none cancelled, no other branch/current-head run touched.

| Workflow | Run ID | Status at discovery | Conclusion |
| --- | --- | --- | --- |
| release | [39820754028](https://github.com/vpsfreecz/haveapi/actions/runs/39820754028) | queued | pending |
| RuboCop | [39820754283](https://github.com/vpsfreecz/haveapi/actions/runs/39820754283) | queued | pending |
| clients/python | [39820753992](https://github.com/vpsfreecz/haveapi/actions/runs/39820753992) | queued | pending |
| clients/js tests | [39820754055](https://github.com/vpsfreecz/haveapi/actions/runs/39820754055) | queued | pending |
| i18n health | [39820754005](https://github.com/vpsfreecz/haveapi/actions/runs/39820754005) | completed | success |
| clients/rust | [39820754164](https://github.com/vpsfreecz/haveapi/actions/runs/39820754164) | queued | pending |
| servers/ruby RSpec | [39820754121](https://github.com/vpsfreecz/haveapi/actions/runs/39820754121) | queued | pending |
| clients/ruby RSpec | [39820754041](https://github.com/vpsfreecz/haveapi/actions/runs/39820754041) | in_progress | pending |
| clients/php PHPUnit | [39820754014](https://github.com/vpsfreecz/haveapi/actions/runs/39820754014) | in_progress | pending |
| clients/go RSpec | [39820754208](https://github.com/vpsfreecz/haveapi/actions/runs/39820754208) | in_progress | pending |

Complete machine receipt: api-doc-feature-push-ci.json. Related final source:
api-doc-remediated-receipt.md and api-doc-remediated-* inventory. Independent
review607941c0 plus lead-accepted narrow findings remediation27b4f8f8 retained.
Feature publication does not establish full verification or merge/release approval.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-haveapi-release/
