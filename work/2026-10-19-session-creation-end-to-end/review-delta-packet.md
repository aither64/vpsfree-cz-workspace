# Retirement correction and final branch delta review

Same generic runtime worktree/base as the original review. Complete final series
now has the original journal fix 98ae6b3, acceptance suite 1fb4442, and the new
retirement discovery fix (current HEAD). Read the actual exact HEAD before review.
No migrations, repeated pins, superseded approaches or transitional formats.
Each commit owns a distinct behavior. Narrow suite fixes were folded into its
commit; original review and direct reconciliation are retained separately.

New substantive product change: the handoff's documented completed user deletion
had failed because ordinary retirement discovery hid an alternate-provider root.
The mandatory suite's final stale-retry case deletes an alternate-provider
fixture, so this bug is directly relevant. The original removed request stays
removed; no lifecycle retry or mutation against it occurred.

The selected stock 0.163.0 native binary generated ThreadListParams schema states:
modelProviders, when present but empty, includes all providers. The pinned shared
codex-web ListThreads options cannot express it. The bounded workspacecodex query
now sends this filter for both existing retirement discovery paths, preserving
cwd/source/indexed/pagination/ambiguity/exact-root/idle proof behavior. No native
or dependency patch/rebuild and no persistence change. Current source docs explain
the behavior. The lead applied the English writing skill directly.

Quick verification: gofmt and diff check pass. Declared Nix environment, absent
host provider catalog and TMPDIR=/tmp: focused workspacecodex
`-run "TestRetir|TestRequireThreadArchived" -count=1` passed in 5.117 seconds.
New boundary test models native provider filtering for active indexed candidate
and archived exact-ID discovery. Existing ambiguity and retirement tests pass.

Also inspect the narrow test-driver delta against your original review: all
seven findings corrected per review-remediation.md. First packaged run failed
before any creation scenario solely because fixture setup omitted required
repos/. That setup is fixed. Existing baseline f27925c confirms Chromium can
discard accepted POST bodies during navigation, so the driver now recovers the
actual durable status by the serialized request ID, with exact route matching.
Second immutable VM run is still testing 1fb4442, before this retirement change;
its outcome cannot validate the new product code. No package with the retirement
change will run integration tests until this review is reconciled.

Review all four affected lanes (general, architecture, scope, risk), the new
product behavior plus final complete history/migration/pin conclusions. Compare
review-delta.diff, original report and packet and current design brief. Report
concrete findings directly; no source edits, long tests or nested reviewers.
Persist report in final-review-delta.md. Retain the same reviewer settings and
identity from the original independent review.
