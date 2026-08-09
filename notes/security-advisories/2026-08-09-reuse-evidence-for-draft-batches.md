# Reuse one fresh evidence document for related advisory batches

Initiative: `work/2026-08-07-security-advisories-6-12-95-2`

## Symptom

Applying related drafts took roughly three to five minutes per CVE even though
all dossiers evaluated the same active Node set and kernel history.

## Cause

Every `sync --apply` invocation performed a complete production evidence
collection before its first write. Repeating that collection for 19 related
CVEs multiplied the expensive Node, event, component, and reconstruction reads
without producing independent security evidence.

## Workflow

Run `bin/security-advisory collect` once immediately before a related batch and
pass `--evidence .state/evidence.json` to each sequential `sync` or `ready`
invocation. Reuse expires when the oldest Node receipt or history-coverage
timestamp reaches the evaluator's 15-minute evidence-age limit. Collection
itself consumes part of that window. Commit each generated submission baseline
before the next apply so the source remains clean. Recollect if the Node set or
security state may have changed.

This optimization does not weaken remote concurrency controls: every advisory
still uses content-revision preconditions and an exact post-write readback.
Focused and full RSpec cover reuse, expiration, and the default recollection
path.
