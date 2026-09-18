# General review

Reviewed vpsAdmin commits
`791ab3aa89e2f613979da6090b89785c78245db5..6682da3bafc1212f30c395707319147a8c51fcc9`
(`22fa7adc3` and `6682da3ba`) for scope, correctness, commit history, tests,
documentation, and operator guidance.

## Findings

### Blocking: the engine topic contains prose that becomes RSpec path arguments

Commit `6682da3ba` adds the line
`# Includes recorder and historical-bound repair database regressions.` at
`.github/workflows/api-specs.yml:56`, indented inside the engine topic's YAML
`patterns: |` literal block. It is therefore part of `matrix.patterns`, rather
than a YAML comment.

Both the full and core jobs split every nonempty line with unquoted shell
expansion (`.github/workflows/api-specs.yml:166-173` and `:267-274`). Replaying
that exact selection logic adds these entries after the real model specs:

```text
#
Includes
recorder
and
historical-bound
repair
database
regressions.
```

The jobs then pass the generated list to RSpec with `xargs`. These nonexistent
paths make both engine jobs fail even though the tracked-spec coverage check can
still report every real spec exactly once. Move the comment outside the literal
block or remove it, and verify the exact workflow file-list generation after
the change.

## Review notes and residual gaps

No other general-review finding was established. The two commits have coherent
purposes and compliant messages: the first owns the additive schema and live
recorder behavior with its focused regressions, while the second owns the
independent repair operation, task, operator documentation, integration
scenario, and CI selection. The generated schema reordering is mechanical; the
reviewed semantic schema delta is the nullable `last_confirmed_at` column.

The recorder preserves bounds, immutable evidence, `updated_at`, and public
revisions while advancing confirmations under the node lock. The repair is
node-scoped and dry-run by default, validates `APPLY` and `BATCH_SIZE`, selects
only retained event snapshots inside the interval, revalidates the target,
predecessor, and evidence under the node lock, and changes only the lower bound
through normal timestamped persistence. Its specs cover apply, dry-run,
idempotence, eligibility, evidence choice, boot rejection, role and argument
validation, and simulated concurrent changes.

Long synthetic integration testing and GitHub Actions had not run at this
checkpoint. The exact downstream configuration and KB pins are intentionally
deferred to their separately reviewed checkpoint. Production evidence was not
inspected, so the documented possibility that the node1 dry-run finds no
retained proof remains an accepted operational limitation.
