# Prior P CI observation

Bounded read-only GitHub inspection on 2026-10-24 found **no failed workflow
run for exact provider P** `bdaed19e901237e05bd0a779f368e76cb311143f` among its
three listed push-triggered runs:

| Workflow | Run | Result |
| --- | --- | --- |
| Tests | [40099730892](https://github.com/vpsfreecz/confctl/actions/runs/40099730892) | completed / success |
| RSpec | [40099730887](https://github.com/vpsfreecz/confctl/actions/runs/40099730887) | completed / success |
| RuboCop | [40099730901](https://github.com/vpsfreecz/confctl/actions/runs/40099730901) | completed / success |

The requested candidate failure inspection used `gh run view 40099730892` for
exact source/status/jobs, then `--log-failed`. That command succeeded and returned
an empty log because the run succeeded. The exact-head run list confirmed the
other two successful runs. No actual P CI failure is available to attribute to
the local fixture defect; these observations do not replace or relabel the
retained failed P/Q local exported checks.

Receipts: [run metadata](package-b-p-ci-run.json),
[exact-P run list](package-b-p-ci-runs.json),
[empty failed-only log](package-b-p-ci-failed.raw). The empty log SHA256 is
`e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.
No CI rerun, dispatch, cancellation or wait occurred. Final R CI and exact
GitHub/local source/check identity still require their separate post-publication
observations.
