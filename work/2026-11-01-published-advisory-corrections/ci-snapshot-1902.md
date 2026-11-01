# Exact-head CI snapshot, 2026-11-01 19:02 UTC

Snapshot only. No pending-run wait, rerun, workflow dispatch, cancellation or
local application/KB/browser suite was performed. Source head inspected was
`218e3180896debd3006b9a0583e557286702761d`; KB head was
`21c5213256c28f4a65fd582485e07234a02f5f55`.

| Repository / workflow | Run | Snapshot status |
| --- | --- | --- |
| vpsAdmin API Specs | `41337574258` | Pending overall; 5 completed, 6 in progress, 15 queued jobs; one completed failed job |
| vpsAdmin integration CI | `41337574315` | In progress, no failed job |
| vpsAdmin i18n health | `41337574263` | Success |
| vpsAdmin RuboCop | `41337574264` | Success |
| vpsAdmin Webui PHPUnit | `41337574308` | Success |
| KB Check | `41337657622` | Success; hosted source check uses `--allow-missing`, not strict acceptance |
| KB Managed page runtime | `41337657793` | In progress, no failed job |

No aggregate API failure or integration success is inferred from these partial
statuses. Original per-run JSON including complete job/status inventories is
retained under
`/tmp/2026-11-01-published-advisory-corrections-ci-snapshot/`.

## Actual failed job and cause

Core platform-operations job
[124940972367](https://github.com/vpsfreecz/vpsadmin/actions/runs/41337574258/job/124940972367)
completed with failure. Both its full job log and native RSpec results were read.
The job ran 236 examples with two failures, zero pending and zero errors outside
examples. Seed was 38162; duration 689.35 seconds.

Failures are the two generated examples in
`api/spec/api/resources/security_advisory_spec.rb`:

- `[1:4:6]`: published report original text/CVE/node membership correction.
- `[1:4:7]`: retracted report original text/CVE/node membership correction.

Both stop at line 762 because the POST fixture at line 760 supplies lowercase
`cve-2026-9998`. The API responds with `status: false`, message
`input parameters are not valid`, and `cve_id: must be in CVE-YYYY-NNNN format`.

The baseline `SecurityAdvisoryCve` format regex requires uppercase `CVE`, and
HaveAPI's ActiveRecord adapter imports this model validation into its input
validators (`haveapi-0.32.0/lib/haveapi/model_adapters/active_record.rb:528`). It
validates before the model's normalization callback. The new workflow fixture
assumed model callback normalization would happen first. This is an authored
test-input error; no change to runtime validation or accepted API behavior is
needed. Existing model normalization coverage remains unchanged.

Prepared correction changes only that fixture string to `CVE-2026-9998`.
It remains unstaged/uncommitted pending the lead's next verification/history
package. Ruby syntax, focused API-shell RuboCop and diff checks pass. The two
examples have not been rerun and no test success is claimed.

## Artifact provenance

- Results artifact `13096732347`, `rspec-results-core-platform-operations`:
  native RSpec results and environment JSON downloaded.
- Manifest artifact `13096865061`, `rspec-files-core-platform-operations`:
  eligible file manifest downloaded.
- Environment: Ruby 3.4.12, Bundler 2.6.9, RSpec 3.13.6; effective generated
  Gemfile.lock SHA256
  `49f5ab631794f99e17cf5966198790e2d1e47e84ece0e13deb67e292399d9936`.
- Raw log `124940972367.log`, terminal-escape-stripped readable copy
  `124940972367-clean.log`, per-run snapshots and downloaded artifacts are all in
  the same disposable snapshot directory.

No meaningful runtime/design change was made. Remaining matrix jobs and both
runtime workflows remain pending until the authorized verification package.
