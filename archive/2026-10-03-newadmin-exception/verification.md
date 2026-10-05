# Verification evidence

## API local regression and checks

Tested source is the exact tree committed as
`af8a97670293f4aa9a57e3196ac263c9c9530644`, unchanged after green verification.

- Red: three persisted regressions on unchanged old source, 3 examples/3 failures
  at the intended `nil.valid_to` dereference, including actual expiry cleanup,
  OAuth refresh and access authentication. [Result](red-regression-result.json).
- Green: resume, cleanup and OAuth configuration suites, 72 examples/0 failures,
  exit 0, 77 seconds. [Result](green-regression-result.json).
- Touched-file RuboCop: 3 files, no offenses. All mandatory API commit hooks and
  commit-message hooks passed; no bypass. [Implementation report](implementation-result.md).
- Independent final API review: all four lanes, no findings, complete one-commit
  feature history and inherited dependency delta checked, no migrations.
  [Review](review.md).

## Configuration quick checks

Initial configuration commit `e96fbde0c622e3807593e3e59daae0f668045540` selects
the reviewed/published API hash through channel/role `vpsadmin`/`vpsadmin`.

- Hook-managed confctl generator exited 0, generated history retained.
- Lead and implementer comparisons agree: only services lock revision/hash/time
  change; all 64 nodes and unrelated follows/pins remain intact. Full generated
  changelog equals the full 17-commit old-to-new API range.
- Complete config series: one generated commit, clean index/worktree,
  `git diff --check` passed, no obsolete branch mechanisms or migrations.
- Declared `confctl inputs channel ls vpsadmin` resolves the intended hash.
  Declared `confctl ls 'cz.vpsfree/vpsadmin/int.api[12]'` selects exactly API1/API2.
  [Configuration report](configuration-result.md).
- Independent configuration review passed all four lanes without findings, with
  explicit clean complete-history/no-migration conclusions. API1/API2 system
  build passed under fresh Luna/low `configuration_build_watcher`, exit 0,
  120 seconds, generation `2026-10-03--21-15-32`. Exact command
  `nix develop -c confctl build --yes 'cz.vpsfree/vpsadmin/int.api[12]'`.
  [Initial build result](configuration-build-result.json).
- Upstream subsequently advanced by two merged monitoring commits. Clean rebase
  onto `7e32833a` produced `dd5e0b5d1d8a2487d608909676c828934966abdc` with
  byte-identical feature diff/message and `git range-diff` equality. Quick checks
  pass; current final-ref general/risk checkpoint passed without findings and
  preserves earlier all-four conclusions. Fresh
  `configuration_final_build_watcher` completed the refreshed scoped system
  build: exit 0 in 78 seconds, both targets generation
  `2026-10-03--21-30-00`. [Final build result](configuration-final-build-result.json),
  [actual target outputs](configuration-final-outputs.json).
- Configuration feature head `dd5e0b5d` is published over SSH; remote tracking
  head equals the tested/reviewed local head and worktree/index remain clean.
  There is no push CI in this configuration repository: its only workflow is
  scheduled/manual Daily update, and exact feature branch run listing is empty.

## Exact-head GitHub CI

All run IDs below were verified against API head `af8a9767` before observation:

| Workflow | Run | Latest evidence |
| --- | --- | --- |
| i18n health | [37146401940](https://github.com/vpsfreecz/vpsadmin/actions/runs/37146401940) | Passed |
| RuboCop | [37146401909](https://github.com/vpsfreecz/vpsadmin/actions/runs/37146401909) | Passed |
| API Specs (topic parallel) | [37146401912](https://github.com/vpsfreecz/vpsadmin/actions/runs/37146401912) | Attempt 1 cancelled at 45-minute cap; attempt 2 superseded by requested timeout edit |
| CI integration | [37146401934](https://github.com/vpsfreecz/vpsadmin/actions/runs/37146401934) | Explicitly unawaited |

Prior fresh observers retained bounded CI handoffs while configuration builds
used the single utility slot. The completed observer collected the old workflow's
45-minute full-platform cancellation; all other jobs and coverage passed. Lead
inspected logs and baseline durations before approving one targeted retry. User
then superseded that retry with an explicit 60-minute job timeout change. Retry
observer stopped, returned incomplete and retained the running old-head attempt
identity; no watcher cancelled/reran any job. See
[timeout evidence and decision](api-specs-timeout.md).

New exact-head API Specs evidence remains pending after the workflow update.
Only its success satisfies the user's merge condition; integration CI is excluded
from waiting. Old runs will be cancelled when superseded by the follow-up push.

## Limits

No production activation or browser test was performed. Persisted cleanup/
refresh/access authentication is covered locally; exact pinned WebUI source was
inspected separately in [consumer trace](pinned-webui-trace.md). This does not
establish production closure chronology. Existing concurrency boundaries remain
unchanged and no concurrent scheduling experiment was run.

## Requested 60-minute final head

API f9beb46e5206864bca9d37672e1419cf03661467 is committed, quick-checked,
independently reviewed in all four affected lanes without findings and published
over SSH. Complete authfix+timeout series; unchanged runtime blobs preserve72/0
evidence. All mandatory hooks passed without bypass. API Specs
[37151153953](https://github.com/vpsfreecz/vpsadmin/actions/runs/37151153953) is
registered at exact f9; success remains pending. After follow-up push, lead
requested cancellation of superseded oldhead retry37146401912, preserving new
run. Stale inventory incidentally showed oldhead integrationCI37146401934
success; it was not awaited. Timeout-only push triggers onlyAPI Specs.

## Final regenerated pin verification

Configuration 074b62fe passed independent validation and general/risk checkpoint
without findings, preserving earlier unaffected reviews. Complete final series
is one generated pin with all18 referenced API commits retained. Fresh
configuration_updated_build_watcher completed the exact-tree API1/API2 builds:
exit0 in 118.821 seconds, generation 2026-10-03--22-46-01. Lead inspected actual
per-target generation metadata, confirmed exact f9 and existing switch scripts.
[Build result](configuration-updated-build-result.json),
[output evidence](configuration-updated-outputs.json). No activation.

Published 074 with an exact force-with-lease against historical dd5; local/remote
feature heads match and tree/index remain clean. No configuration branch runs
exist to cancel. Initial60-minute observer handed API Specs back still running
(23 successful, three active), allowing the single utility slot to build. Fresh
api_specs_60m_completion_watcher now observes that same immutable existing run;
no restart/rerun/cancellation was used for this handoff.

## Final API Specs gate and integration

Fresh api_specs_60m_completion_watcher observed run 37151153953 to terminal
success at exact f9, attempt 1: all 27 jobs succeeded, including coverage.
Elapsed 34m17s. Full-platform job 33m38s/RSpec 32m56s; core-platform job
23m28s/RSpec 23m. Configured limit remains 60 minutes as requested. No new-head
rerun or cancellation was needed. Earlier 45-minute timeout evidence and
investigation remain preserved; exact contributor is unknown.
[Compact workflow result](api-specs-60m-completion-result.json).

After this gate, lead fetched unchanged default baselines and fast-forwarded
API 148ef0ea -> f9 and configuration 7e32833a -> 074 from prepared target worktrees,
then pushed HEAD:master over SSH. Fresh fetches confirmed exact final
feature/remote master equality and ancestry. [Integration proof](integration-result.json).
Feature refs and all worktrees remain clean and retained. Default-branch
workflow runs are not awaited under user direction. Production deployment
remains user-owned; no activation or session cleanup occurred.

The [compact persisted regression proof](regression-proof.txt) retains the exact
three intended original-source failures and the final72-example success summary.
Full local captures are retained outside the curated Git checkpoint.
