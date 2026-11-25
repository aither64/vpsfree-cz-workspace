# Bounded integration CI progress diagnosis

Exact run44121657783/attempt1/head9b385dbb, job134174363984. Read-only diagnosis;
source remained frozen. Root owns continued status observation. No runner/host,
guest, process, cancellation, retry or new execution action was taken.

## Expected scope

The current change calls for the full `tag=ci` suite under the committed selector:
- If push-before024 is available, its22file net diff includes unselected runtime
  paths (`api/notification_templates/**`, `api/models/mail_template.rb`, locale
  files). Any unmapped runtime path deliberately selects full suite.
- If the rewritten old head is absent from checkout, the workflow uses current
  default merge-base537b. That80file feature range includes migration full rules.
- Failure to determine a base also explicitly selects full suite.

This is source-derived scope, not a downloaded live selected-tests manifest. The
job's selection and preview succeeded, consistent with nonempty selected scope.
`tests/all-tests.nix` registers122scenario definitions;117explicitly mention ci,
with five inherited/composed definitions not counted as proven ci selections here.
The suite includes service/node VM setup, storage/transfer/reinstall operations,
WebUI scripts, alerts and SMTP. The runner uses `--jobs auto`; actual capacity,
cache misses and current build/test stage are not visible from the available API.
720minute Run tests/780minute job bounds are limits, not estimates or deadlines.
Prior single SMTP1380s is illustrative scope evidence only, not current progress.

Source references: `.github/workflows/ci.yml:84` (push base), :94 (merge-base), :98
(full fallback), :118 (preview), :172 (step bound), :182 (jobs auto);
`tools/select_ci_tests.rb:54` (full rules), :72 (unmapped fallback), :126 (full).

## Actual available evidence and comparison

Current job started16:05:02UTC. Selection completed16:05:11; preview succeeded
16:07:15 (124seconds); state preparation succeeded; Run tests started16:07:15 and
remained in_progress in the one bounded job snapshot. No failure conclusion.
Artifact listing returned0. Full log upload/evaluation/summary occur after the Run
step, so no per-test progress is established by that empty listing.

One current-job log read returned HTTP503. It is a provider/read failure, not a
failed test or proof of a stall. No repeated log read or observation loop was run.
The prior completed job log was not retained because gh refused terminal escape
sequences; no bypass/retry was needed for its authoritative job/step metadata.

The prior cb8run43911462168 is not a35minute execution comparator. Its exact job
133454169626 started17:23:02 and completed17:23:20 on Nov16 (18seconds). Preview,
state preparation and Run tests were SKIPPED; the skip summary succeeded. The
longer run-level interval therefore did not measure physical integration work.
The later024spec-only skipped run is likewise not a physical runtime baseline.

## Disposition

Expected broad/long integration scope is supported. Current evidence cannot
establish per-test advancement, build stage, stall or failure. Do not infer
failure/cancel/retry from elapsed wall time or compare to earlier skipped runs.
Smallest next action: keep root's existing exact-run observation and await normal
terminal result/log publication. If fresh progress becomes necessary, root can
request a separate bounded exact-job log read when available; no duplicate watcher.
Source remains9b385dbb and no new check was launched.
