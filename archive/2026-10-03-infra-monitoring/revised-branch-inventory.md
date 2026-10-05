# Revised final branch inventory

Base: `b66c929bb7c202ad31bd8994a691ade14c40ebf0`. Final head: `657cc0a8e087f8c4bed7fe8d7176cb9f06a6e2da`.
Final tree: `c3a20ba419ff6bc8e2b3ed2a6d4600087d143af9`, identical to the four-check passing snapshot.
The complete worktree/index including untracked files is clean. Merge base
is exactly the supplied base. Whitespace and unchanged invariant comparisons
passed independently in lead inspection.

## Complete commit series

```
f53354dec1596bf665c80f85c557a9b05755805a monitoring: restrict critical filesystem alerts by type
657cc0a8e087f8c4bed7fe8d7176cb9f06a6e2da monitoring: apply staging cpu alert policy to playground
```

First owns typed metadata, authoritative host/JVB labels and their immediate
global critical-filesystem consumer, with matching checks/docs (12 paths).
Second independently changes CPU usage policy for pgnd with related checks/docs
(five paths; union 15). The CPU source, fixtures and check registration patch
are byte-identical to the prior accepted CPU commit; overlapping policy prose
was adapted. [Implementation report](implementation-result.md) and
[machine-readable inventory](revised-final-inventory.json) list every path.

The old published e7b02916/f725dd3f SMS-only approach is superseded and was
consolidated into the owning commit. No added/removed SMS route, fixup, redundant
dependency update, interim job-filter/unless policy or unused compatibility
path remains in the final series. [Range-diff](revised-range-diff.txt) records
the final policy change and unchanged CPU source/tests.

## Final diff and migration lineage

[Complete final diff](revised-final.diff), SHA256
`4955b9e0cd56b89c64d5cca6a108b9a602cea5656c1a1e00dfd2e063bfe8fc42`. Critical common rule differs only
by the positive type selector; alerter, infra/Meet rules, Meet data and locks
are equal to base. Nodes differs only by the four accepted CPU edits.

**No migrations**: no schema/seed/persisted-format or migration version changed.
Known repository/session provenance is in [revision provenance](revision-provenance.md).
The old feature was published, unmerged, with no PR or branch CI; no session
release, deployment, pin or integration occurred. Unknown external consumption
was not audited. No migration version needs provenance reconciliation.
The independent reviewer must assess the complete series and explicitly
conclude on obsolete history and migration lineage.

A separate pre-existing local master ref b6e650ad remains untouched. Integration
will use freshly fetched origin/master in a separate target checkout, preserving
that ref and feature refs; no published default history rewrite is authorized.
