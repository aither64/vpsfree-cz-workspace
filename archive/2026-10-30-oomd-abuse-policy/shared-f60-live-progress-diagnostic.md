# One live-log progress diagnostic

Lead explicitly authorized one distinct job-log/console retrieval while retaining
sole observer/native16318. No observer interruption, duplicate run-status polling,
workflow retry/cancellation, source edit or local runtime accompanied this read.

Exact existing integration run: 41185457135, head
f60d41a453b1703e42de4341285bdc6ba339aff0. Its existing job is 124491363934.

Single command:

```sh
gh api --allow-escape-sequences --include \
  repos/vpsfreecz/vpsadmin/actions/jobs/124491363934/logs
```

Result: native exit 1. Final provider response at 2026-10-31T10:09:56Z was
HTTP 404, `The specified blob does not exist`, XML `BlobNotFound`. No current
test/build, last per-test output or blocking dependency was exposed. This proves
log-blob unavailability for that attempt, not a test failure, authentication
refusal, resource wait or runner hang. No second endpoint/retry was attempted.
Raw supporting files: shared-f60-live-log-attempt.{txt,stderr,exit}.

Committed workflow contract at f60:

- The self-hosted CI job has timeout-minutes 780.
- Run tests has timeout-minutes 720.
- Push uses the existing full selection with test --jobs auto. The workflow
  STOP_ON_FAILURE default is false; only explicit dispatch true adds the native
  --stop-on-failure flag. Neither timeout is a prediction of completion time.
- Per-test output is teed to the runner test.log/job console. Full logs upload
  after failure/cancellation; evaluation/summarization follow Run tests exit.
  The workflow configures Cleanup test state with always(), without proving that
  an interrupted action has already completed cleanup.
- The pinned runner CLI defaults --timeout to 900 seconds for machine commands
  and waits. It is not a whole-suite deadline. The inspected executor waits for
  worker output/completion without imposing a suite elapsed-time limit in that
  loop. Both required scenario metadata declare one attempt.

Sources: committed .github/workflows/ci.yml at f60d41a4, and pinned vpsAdminOS
8e44a512 test-runner/lib/test-runner/{cli/app.rb,executor.rb,test_evaluator.rb}.
No new cancellation authority or time-based failure threshold is inferred.
The next exposed result remains native Run tests completion, evaluation or
artifact publication. Required alerts/incident-escalation and
webui#incident-escalation outcomes remain unknown; sole observation continues.
