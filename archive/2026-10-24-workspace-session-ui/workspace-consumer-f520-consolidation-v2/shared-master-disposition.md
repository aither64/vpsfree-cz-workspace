# Workspace f520 shared-master drift disposition

The prepared consolidation on recorded remote base
`3e72f394a73c33be71fcdc1313d05cc74abb802f` remains valid. The observed drift is
one local tracking-only commit, not a changed remote code baseline. No rebase,
Nix repeat, source regeneration or configuration investigation is indicated.
This is a method disposition; owner0 execution still requires the lead's release.

## Actual evidence

Saved `workspace-consumer-f520-consolidation-preparation-v1/effects-v1/consolidate/`
remains failed: summary SHA256
`a2d48a109a03f4dc605360bd1042875d743d61597d92bb919e5e32c3bd30b594`,
exit1/5.159447s, `Shared master metadata drift`, postflight null. All ten saved
commands returned0, joined/reaped with empty groups and no signals. Both
protected-guard calls stopped at the shared-master comparison, before SSH,
staging or commit. All70 saved evidence entries match their manifest hashes.
Do not turn that limited failed preflight into a successful full input check.

Bounded observation receipt [workspace-f520-default-drift-observation.json](workspace-f520-default-drift-observation.json),
SHA256 `395bf18ca4eacf3a3557284704efa2251c1f48f39342aa376cfdcce163e06b6b`,
contains exact commands, exits, timestamps and metadata/path-only output:

- Local master `7d5ac6860e0640f1904014a5d1ecf51ac4af0d48` has sole parent
  `ef1b79d339c9003562e768905448f2859130a19b`, tree
  `e6dcef13f418abd73ecf8f4adfcbec9c97e68030`. Its five changed paths are all
  beneath another session's `work/` directory: two KB candidates, two release
  records and one validation record. No contents were read.
- Recorded base3e72 is an ancestor of ef1. Their only three changed paths are
  archived tracking records. Thus the entire observed3e72..7d5 difference is
  eight tracking paths, zero overlap with the accepted620 source paths.
  The saved flake's `workspaceSource` filter excludes `work` and `archive`.
- The one authorized SSH `ls-remote` at 2026-10-26T08:44:20Z returned0/1.289s:
  master remains `3e72f394a73c33be71fcdc1313d05cc74abb802f`; own feature remains
  `0c95082f561da02bc04c09e223886d3b387d2dc5`. Local own feature matches0c.
- Saved postfailure own feature and preservation ref both remain0c. Saved
  generated flake.nix SHA256 is
  `57a0812ae8c29a21bd772b0e1752f2a39cd7d1577b77a6fc90b6443d61676c3e`;
  flake.lock is `392ea143231c416968142a78b6084369ac18f60c4b053410e93e1e62df96f932`;
  raw index is `9ac6197c84526dee2c9e6dcde9dfbb796b13a3fd410376a6059502b092ec2d03`.
  These are exactly the previously accepted generated pair/index. The saved
  original620 manifest also matches its bound SHA45a9254a. No live620 or index
  revalidation is claimed in this diagnosis.

## Smallest continuation

Owner0 should prepare a successor of the existing consolidation adapter with
fresh exclusive results. Preserve all original sources, expectations, releases,
failed summaries and raw evidence. Bind this disposition and the observation;
change only the expected *local shared-master observation* from exact ef1 to
exact7d5. The imported guard reads `S['sharedMaster']` in `protected_guard`;
a successor may assert the old value is ef1 and create an in-memory copy of
that specification with this one key set to7d5 before invoking the unchanged
guards. No old packet file is rewritten, and no guard is removed or caught.
The successor's manifest/release must bind this exact admitted delta.

Retain all original session, tools, hooks, preservation refs, complete620
source/mode/blob checks, complete57420 index semantics, accepted raw9ac,
generated pair and fresh remote3e72/feature0c requirements. Any further drift
stops normally; this is not a tracking-prefix exemption. After those checks,
the existing scoped add/normal amend may create the one two-file final pin
stream with sole parent3e72. Unrun checks and hooks still must actually pass.
No new source/lock evaluation is needed for this local ref observation.

Current shared7d5 is not an ancestor of that proposed same-base feature, and
this disposition does not claim merge readiness or authorize shared integration.
The eventual approved integration still needs the ordinary fresh target and
ancestry/rebase/equivalence assessment; preserve unrelated shared tracking.
Configuration61af/270d is a separate unchanged scope. Session remains open;
lead owns release and tracking.
