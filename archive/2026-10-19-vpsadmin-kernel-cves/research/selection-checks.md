# Selection evidence consistency checks

Mechanical research check, 2026-10-19, owned by implementer3. This is not an
eligibility decision or independent final change review. No advisory draft,
project edit, commit, branch, build, exploit or external write was performed.

The session command and both environment identity values matched
`2026-10-19-vpsadmin-kernel-cves` and `/home/aither/workspace/ai/vpsfree.cz`.

## Results

- 109 manually screened entries, 109 unique CVE IDs.
- 109 primary snapshots report PUBLISHED and the matching CVE ID.
- 109 metric arrays match the saved primary CNA record exactly.
- 109 release/SHA pairs match the complete range ledger; all fall within
  6.12.95–6.12.113 inclusive and the exact SHA occurs in that release's saved
  official changelog.
- Zero overlap with the 57-CVE public dedup list.
- 212 human-table CVE row comparisons across classification, candidates and
  platform baseline; 105 explicit score/unscored comparisons and 109 stable
  SHA links. Zero score, first-fix version or SHA discrepancies.

The [reproduction script](selection-check-evidence/check.py) writes the
[per-ID checks, human-row comparisons and input hashes](selection-check-evidence/result.json).
Release checks read the fix column, preserving introduction ranges quoted in
explanatory prose (notably CVE-2026-74753's 6.12.96 introduction).

Generic ID/range/link checks already exist in package B's
[consistency evidence](cve-evidence/research-consistency-check.json), including
zero missing internal links. This pass reuses that result rather than repeating
its broad audit. External links were not bulk-fetched; their availability is
not established by local formatting or consistency checks.

## Concrete discrepancy for owning authors

`platform-baseline.md`, historical CVE-2026-74597 row, says the ip6_tunnel
module is absent from default preload and frames it as a module prerequisite.
`classification.md` explicitly supersedes that explanation: frozen
`IPV6_TUNNEL=y` is built in, while the mip6 type-registration gate remains.
This is a factual disagreement between the supplied documents, reported to the
lead for the platform owner to reconcile. No security reclassification is made
here and neither file was edited by this package.

## Pending final-selection check and limits

The architect's provisional [selection](selection.json) was checked at SHA256
`31dd598ef6bd4e4d6e812f68b6707ebfc40a40ee219e550afea43d900b886ed7`:
32 distinct IDs, comprising 23 recommended, four conditional host-enabled and
five borderline. Declared counts match actual entries. All 32 titles, exact
fix release/SHA pairs, supplied CVSS metric objects, and primary URLs match
the primary range ledger; primary cached records are PUBLISHED; zero overlap
with published dedup. Each exact SHA also occurs in the saved release changelog.
No discrepancies were found.

The [snapshot](selection-check-evidence/selection-snapshot.json) and
[result](selection-check-evidence/selection-result.json) preserve this checkpoint.
The [selection checker](selection-check-evidence/check-selection.py) will compare
later entries with this snapshot and validate only added or changed entries,
while always checking unique IDs, counts and removals. A status-only change
therefore does not repeat the 32-entry check. The baseline is deliberately
preserved rather than automatically advanced.

This validates the artifact's exact IDs and factual fields against saved data.
It does not establish that its decisions match every narrative classification
statement, that the proposal is exhaustive, or that omitted IDs should be
selected. CVSS comparison covers supplied metric objects; CNA scenario prose
is not copied into selection metric objects. Source revision and record freshness
remain snapshot-scoped. Supplemental additions and final classification are
pending and have not been implicitly accepted by this provisional check.

These checks establish consistency of saved evidence, not fresh upstream
status, source authenticity beyond recorded provenance, tenant reachability,
exploitability, runtime mitigation, or absence of private drafts. Eligibility
remains architect/lead owned. The full 3,493-record range join has not received
a manual security audit. No selection approval or drafting authorization is
implied.

## Final selection and approval-table delta acceptance

Final research selection status is
`final_research_recommendation_awaiting_user_approval_for_drafting`, SHA256
`09c51860a0a250c2fd0ad3c08799fba3674474da4a47bf7768c99935a2ac00b2`.
There are 69 unique entries: 41 recommended, 11 conditional, nine borderline
and eight selected deferred. Declared counts match. Against the retained
32-entry provisional snapshot, 37 entries were added, none removed, and all
original 32 entry objects remained unchanged. The bounded delta check found
zero discrepancies in the 37 additions: cached primary status PUBLISHED,
exact title/release/SHA, supplied CVSS objects and primary URL all match the
range ledger; exact SHAs occur in the corresponding saved official release
changelogs; no public dedup overlap. The unchanged 32 retain their earlier
successful checks. No full 109-entry repeat was performed.

The [delta result](selection-check-evidence/selection-delta-result.json)
preserves exact added IDs and checks. The earlier provisional status above
is historical and superseded by this final checkpoint.

The lead's [approval document](../selection-for-approval.md), SHA256
`4ca653ff2eef2d766d9ff46be6a74ad77609e7dfd2f37bc82bdcbcb14ecb34d5`,
contains exactly 61 unique table IDs: 41 recommended, 11 conditional and nine
borderline, precisely the final JSON's nondeferred subset. All table groups,
fix versions, score/severity labels (including not supplied) and primary URLs
match. The eight deferred entries are intentionally absent from those tables.
[Approval checker](selection-check-evidence/check-approval.py) and
[per-row result](selection-check-evidence/approval-result.json) retain this
comparison. No impact prose or security eligibility was reclassified.

The earlier CVE-2026-74597 narrative discrepancy is resolved: package A's
historical row now explicitly says IPV6_TUNNEL=y is built in and separates
the mip6 registration/preload gate. The exact corrected source row is saved
in the approval result. The earlier discrepancy section records the original
finding, not an outstanding blocker.

These are checks of the recorded snapshot and exact supplied fields. They do
not approve drafting, establish proposal completeness or security eligibility,
refresh upstream records, validate production exposure, resolve private drafts,
or substitute for final independent change review. User approval is still
required before drafting. No further check scope remains for this package.

## Broader member-relevance proposal checkpoint

The policy-version-2 [member selection](member-selection.json) was checked at
provisional SHA256 `8443953d3404c6ec16763f7b15045474b299b6ccaab216e9270a11eeed294fbe`.
It contains 60 unique proposals: 41 retained tenant-path entries, 11 host-feature
conditional entries, five exact-build exclusions and three privileged-program
conditional entries. All original 41 recommended titles, fix versions/SHAs,
CVSS objects and primary URLs are preserved. Eight IDs are new to the original
69-entry ledger; the other 52 reuse earlier evidence. Seventeen prior entries
are outside the new proposal; this is a selection-set comparison, not a new
exclusion judgement.

All supplied factual fields agree with the primary range ledger and cached
PUBLISHED records, with zero public dedup overlap. Required exposure scope,
unknown runtime/history and unassessed mitigation fields are present. For all
five not_affected entries, the config SHA256 matches the retained archived
configuration, the named CONFIG exclusion occurs in that file, and exact-build
scope plus role/time qualifications are present. These checks validate field
presence and mechanical consistency, not whether the named symbol alone
proves security inapplicability or the completeness of a prerequisite analysis.

The [member approval document](../member-selection-for-approval.md), SHA256
`6fa6fb6f5e83ca307b777466be9408de2e7681b543de3bc534bbbfc6310f5e8d`,
has exactly the same 60 unique table IDs, correct proposal groups, fix versions,
score labels and primary URLs. No discrepancy was found.
[Checker](selection-check-evidence/check-member.py),
[snapshot](selection-check-evidence/member-snapshot.json) and
[per-entry/table result](selection-check-evidence/member-result.json) preserve
the checkpoint. No source download, repeated full 109-entry screen, repository
documentation review or security eligibility reclassification was performed.
Only final status or materially changed entries remain to check after architect
notification. Existing snapshot, runtime/private-draft and approval limitations
continue to apply; no drafting is authorized by this consistency check.

## Final broader-selection delta acceptance

Final member-selection SHA256 is
`8e9906fb11133cb7fafafbcb68cc7ec0900ee7f6e2e7ac50b1ca1af5b2b4b72a`,
status `final_research_recommendation_awaiting_user_approval_for_drafting`.
Compared with the accepted 60-entry snapshot, the same 60 proposed IDs, core
factual fields and groups remain. All 41 retained entry objects are unchanged;
19 entries have ancillary exposure/impact/relevance/source-field changes.
Their required scope, roles, calendar, unknown current/history and unassessed
mitigation fields are present, and source-gate references resolve.

Twenty-nine distinct source/provenance/evidence-record file paths resolve.
All 14 source-manifest input hashes, the manifest's own hash and the bounded
proposal hash match. Five review-only and two deferred controls are separate
from the 60 proposals, yielding 67 distinct IDs in this record. No security
classification or primary metadata recheck of those controls was undertaken.

The approval document remains byte-identical to the accepted SHA256
`6fa6fb6f5e83ca307b777466be9408de2e7681b543de3bc534bbbfc6310f5e8d`.
Together with unchanged proposed core fields/groups, this preserves the prior
exact 60-row table match. Zero discrepancies were found.
[Final delta checker](selection-check-evidence/check-member-final.py) and
[result](selection-check-evidence/member-final-result.json) preserve evidence.
No repeated primary-fact check, source download or security reclassification
was performed. Required-field presence and hash consistency do not establish
semantic security correctness or deployed exposure. No checks remain assigned
to this package; user approval before drafting remains required.
