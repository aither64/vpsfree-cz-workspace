# 2026-08-22-security-advisories-6-12-95-6

## Goal

Identify every CVE covered by the deployed Linux 6.12.95 live patch version 6,
including CVEs documented retrospectively whose first fixing patch version is
older, and prepare a deduplicated proposed advisory list for user review.
After explicit approval of that list, create complete evidence-backed dossiers
and synchronize them as vpsAdmin drafts. Publication and email notification are
out of scope without separate explicit approval.

## Affected repositories

- `security-advisories`: advisory dossiers, evaluations, submission baselines,
  and the vpsAdmin draft synchronization workflow.
- `vpsadminos`: read-only source of the canonical 6.12.95 live-patch coverage,
  live-patch implementation, tests, and fixing-version provenance.
- `vpsadmin`, `vpsfree-cz-configuration`, and Linux upstream: read-only sources
  for reachability, deployed configuration, primary CVE records, and fixes.

## Approach

1. Diff the canonical 6.12.95 coverage and cumulative live-patch source between
   patch versions 5 and 6.
2. Separate CVEs first fixed by patch 6 from retrospective documentation of
   CVEs already fixed by an earlier cumulative patch.
3. Exclude CVEs that already have dossiers or vpsAdmin advisories, and verify
   the remaining candidates against primary CVE records and upstream fixes.
4. Present the proposed advisory set, first fixing patch version, vulnerability
   primitive, and inclusion rationale for review; stop before any draft write.
5. After approval, create dossiers, validate and evaluate them against fresh
   typed production evidence, commit the reviewed evaluations, and synchronize
   drafts with revision preconditions and exact readback.
6. Remove the wall-clock expiry of an already coherent evidence snapshot.
   Evaluate stored evidence against its recorded collection time and require
   an explicit collection only when operators need to observe changed Node
   state. Reuse the reviewed snapshot for draft synchronization.

## Compatibility and deployment

This phase is read-only and does not alter running systems, APIs, schemas, or
configuration. Later draft synchronization creates unpublished vpsAdmin
records only. It does not change kernel state, publish advisories, or send mail.
The dossier must retain the first patch version that fixed each CVE even when a
newer cumulative patch is currently deployed, so mixed historical patch states
are classified correctly and durable public text does not become stale.

The evidence workflow change affects only local assessment tooling. It does not
change vpsAdmin APIs, schemas, production Nodes, or persisted remote data.
Existing schema-8 evidence documents remain compatible. Their per-Node receipt
and history timestamps must have been current when `collected_at` was recorded;
the same immutable document can then be evaluated reproducibly later. Operators
must run `collect` explicitly after a deployment or when Node state may have
changed. Rollback restores wall-clock expiry but does not invalidate evaluations
already committed with complete provenance.

## Testing plan

- Compare patch v5/v6 coverage and live-patch source at exact vpsAdminOS commits.
- Verify each candidate in the authoritative CVE record and upstream Linux fix.
- Compare candidates with tracked dossiers and read-only vpsAdmin advisory data.
- After approval: run dossier validation, the full repository RSpec and RuboCop
  suites, evaluate fresh typed Node evidence, and dry-run draft synchronization.
- Add evaluator and reconciler regression tests proving that old snapshots are
  accepted when they were coherent at collection time, that stale-at-collection
  and future timestamps still fail closed, and that reuse does not recollect.
