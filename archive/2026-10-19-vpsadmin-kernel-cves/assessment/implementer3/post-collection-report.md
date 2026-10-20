# Frozen collection mechanical receipt

Snapshot SHA256 `61904e984266df2f6c53435b2b026b0d0980b35a23ed843eebf95b23c27c9274`
verified: 12,544,228 bytes, mode 0600, schema 8, collected
2026-10-19T21:48:39Z, 13 Nodes. Duration is unknown; the previous elapsed zero
was a placeholder. All three configuration catalogs include the 67 requested
option names. Presence does not establish any particular option value.

The offline timestamp/history check finds two rows requiring owner review:
one current row lacks receipt/observation timestamps (cannot certify freshness),
and one row starts history/reconstruction after the required 2026-01-01 scope.
No stale receipt/history-end or future-skew category was found among the rows
whose timestamps could be checked. These are mechanical gaps, not assigned
security states. Node linkage remains only in restricted .state details.
Successful collector EXIT0 is revision-coherence provenance; the offline check
does not independently replay API revision stability. The frozen bytes and
snapshot identity match; no recollection or API request was made.

2244 booted/reported release fields were inspected across current state, all
603 retained events and 506 event security snapshots. There are 97 events without
security_evidence and two missing release fields. No RC/prerelease or 7.2 release
was observed. Seven distinct numeric four-component custom release strings
are flagged for source-owner identity interpretation. The specific observed
7.2 prerelease parser gate for CVE-2026-74753 is not triggered; no assertion of
safety for custom builds or other CVEs follows.

All 435 livepatch observations in 519 containers were extracted, with 96 empty
containers retained in completeness counts. No filtering by loaded, enabled
or transition state was applied. The sanitized source index contains 48 unique
snapshot-bound tuple identities and activation-state combinations. Missing
identity fields remain missing; no sparse inheritance, source binding, coverage,
activation acceptance or interval classification was performed.

- [Sanitized receipt](snapshot-receipt.json)
- [Sanitized tuple index](livepatch-observed-tuples.json)
- [Extraction script](extract-receipt.py)

Raw patch/kernel/software components and Node/event/boot linkage are retained
only in ignored .state/livepatch-observations.json, mode0600; release-flag and
receipt-issue linkage is in .state/mechanical-receipt-details.json, mode0600.
Owners/architect must interpret source identities and history gaps through the
existing evidence contract. No evaluation edits or additional collection occurred.
