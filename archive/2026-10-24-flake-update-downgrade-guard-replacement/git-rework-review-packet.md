# Cached Git rework review packet

Status: all eight intended sources are committed, quick-checked and clean. Ready for final review assignment.

The user requested replacing the GitHub comparison backend with cached Git
ancestry checks: "yup, rework it". The existing `inputs ls --json` remains for
full alias-resolved revisions consumed by status/IRC commit messages.

Owning design: [current Git contract](design.md#current-revision-git-evidence-through-shared-mirrors).
Check boundary: [bounded verification brief](git-mirror-verification.md).
Current tracking: [state](state.md), [plan](plan.md).

Acceptance: reuse existing exact-URL mirrors and ordinary Git authentication;
prove immutable commit ancestry with typed policy/evidence outcomes; preserve
full graph/transaction/publication checks; coordinate mirror readers/writers;
cold/warm/cache failure must never bypass the guard. Five workflows acquire
cache pairs; all seven retain cache on a safe rejection. Each consumer has one
final exact tool pin. API fallback and old token-only instructions are removed.

Non-goals: arbitrary source fetcher expansion, partial-clone framework, semantic
revert detection, deployment-tool upgrades, dependency-selection changes,
default integration, deployment and cleanup/lifecycle actions. HaveAPI's known
unrelated target movement is deferred to approved integration preparation.

Risk classification: high for ancestry evidence and automated infrastructure
publication across repositories. General, architecture/repetition, scope and
risk/compatibility lanes apply to changed Git/cache behavior and consumer
workflow adoption. Retained independent reviewer0 settings are Sol/xhigh/read_only;
verify current session/identity/settings before actual assignment. Prior review
conclusions are historical and may be reused only for unchanged scope per the
mandatory-review narrow-fix rules. The complete new base-to-head inventories,
final diffs, pin streams and no-migration provenance must still be assessed.

Expected intended split: confctl's final guard directly uses Git, with separate
independent Ruby startup compatibility fix retained; consumer adoption commits
contain only final pin/cache/documentation behavior; status retains independent
vendor/test-dependency and metrics-test compatibility fixes. Preserve R exact
refs/receipts separately, consolidate obsolete API/pin shipping history. There
are no declared database, lock or mirror migrations. Final owner inventories
must confirm actual complete history and absence of deployed/released state.

Provider range is `cc40679d267165aecfa569128438bb55fe910268` to
`822c0e35dbe2549111912f539116b4225dfd3035`: guard5507177 and independent Rubyfix822c0e3.
[Provider inventory](git-cache-source-inventory.json) binds all28 paths, complete
messages/diff, R-to-new16-path delta, tested tree equality and unchanged Ruby
patch ID. [Source report](git-cache-source-report.md) links all quick evidence.
The local R evidence ref is retained; the same exact ref must be preserved
remotely before provider replacement while published consumers still pin R.

Quick results: provider author reports 147 distinct examples passing: 86 real
Git/cache/provider/guard/changelog, 36 transaction/CLI/fallback and 25 manual/
graph/output. Final32 mirror examples,12-file lint/man/diff and ordinary hooks
also passed. Expected exported suite count is 203 including two actual package
cases, from dry-run only; it is not a packaged-suite success yet. C reports C40,
D20, cache98 scheduling cases and 14 negative controls passing; see
[consumer interim report](package-c7-cache-report.md) and
[quick receipts](package-c7-cache-quick.json). Full command
receipts and exact committed ranges remain pending owner inventories.
Owning docs/man and provider safe errors passed the lead's direct writing pass;
consumer cache/local-help wording also passed. Generic mirror failures omit raw
transport text and include only the safe cache digest. See actual final owner
inventories for paths and generated man evidence.

After committed review, run the exact new packaged exported suite, IRC/two old
config shell-hook checks, seven selected updater/commit/final-lock paths with
real shared cold/warm cache receipts, and actual local target movement. These
are scoped new runs, not seven complete workflow reruns. Historical R full
workflows/VM remain exact old component evidence. New package identity and
retained inputs must be recorded; no source-tree-only identity inference.

Review, feature publication and test success do not authorize default merges.

## Final complete source inventory

[Lead inventory](git-rework-final-source-inventory.json) binds all eight exact
bases/heads, full messages/series, final binary diffs and clean checks. The
[consumer owner inventory](package-c7-final-source-inventory.json) and
[consumer report](package-c7-final-source-report.md) bind the complete seven
ranges, R deltas, final pins and independent status patch equivalence. The
[final quick receipt](package-c7-final-quick.json) binds final-pin checks/hooks.
Provider inventory/report are linked above. No obsolete fixup remains.

The final provider is822c0e35. Six consumers have one adoption commit; status
has three logical commits and the independent vendor/Perl and metrics stable
patches are preserved. All consumer lock blobs equal their bases/R/final. Only
approved14 consumer delta paths changed. All worktrees are clean.
HaveAPI retains accepted7ac base and known unrelated1103 default divergence.
There has been no source publication or long runtime for this rework yet.

Read the original R/history, status-metrics and HaveAPI review reports as
historical conclusions for unchanged scope. Perform the assigned four lanes
directly on the changed Git/cache boundary and complete final histories; no
nested reviewers. Report exact reviewed ranges/settings and independent
no-obsolete-history/no-migration conclusions. Findings ordered by severity.
Save the new report as review-git-cache-report.md; preserve all prior reports.
This review does not authorize integration, deployment or lifecycle actions.
