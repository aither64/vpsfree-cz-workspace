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

Run `bin/security-advisory collect` once for the reviewed deployment state and
pass `--evidence .state/evidence.json` to each sequential `sync` or `ready`
invocation. The evaluator checks that every Node receipt and history-coverage
timestamp was current at the document's recorded collection time. The coherent
document does not expire merely because advisory editing, review, or draft sync
takes longer than 15 minutes. Do not alter `collected_at` to extend a snapshot;
the evidence digest and original timing remain audit provenance.

Commit each generated submission baseline before the next apply so the source
remains clean. Recollect explicitly after a deployment or when the Node set or
security state may have changed.

This optimization does not weaken remote concurrency controls: every advisory
still uses content-revision preconditions and an exact post-write readback.
Focused and full RSpec cover delayed reuse, stale-at-collection rejection,
future timestamps, and the default recollection path. The behavior was updated
in initiative
`work/2026-08-22-security-advisories-6-12-95-6/` after a valid reviewed
snapshot expired during editorial follow-up and caused needless fleet reads.
