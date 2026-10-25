---
lifecycle: active
---

# 2026-10-25-archive-unmanaged-files-investigation

## Status

Implementation and independent review complete; packaged verification in progress.
The priority HaveAPI archive recovery succeeded on attempt 2.

- [x] Investigate and reproduce the unmanaged sibling-cache failure.
- [x] Repair and finish the original HaveAPI archive.
- [x] Record and implement preflight with bounded lead-assisted repair.
- [x] Pass focused checks, commit, and resolve independent review findings.
- [ ] Pass packaged lifecycle and component checks.
- [ ] Publish the feature branch and inspect CI.
- [ ] Integration and deployment (not yet authorized/executed).

[Recovery evidence](recovery.md), [design](design.md),
[initial review](review.md), [follow-up review](review-followup.md).

## Next actions

Finish packaged verification, resolve any failures, publish the feature branch
and inspect its CI. Preserve the installed package. Master integration has not
been authorized by the request to implement the plan. Keep this initiative active.

## Repositories and documentation

Only `dev-workspace` is changed. Branch
`2026-10-25-archive-unmanaged-files-investigation` is checked out at
`worktrees/2026-10-25-archive-unmanaged-files-investigation/dev-workspace`.
Base/merge base: `9634151b9836311c331a58880fbb4c46133fd98f`.

Current committed series:

1. `e4f6180f` — archive readiness before shutdown.
2. `5e4e99dfecfda94da47c10cd154dfa98269a6533` — durable portal lead-assisted repair.

The source worktree is clean. Feature branch is published over SSH. No master merge or deployment yet.
Owning-project docs were updated in `docs/session-archive-recovery.md` and
`docs/dev-sessions.md`: readiness CLI, repair and cancellation, restart and
older-package behavior, unchanged automatic archival and journal recovery.
Initial [findings](findings.md) explain the original cache placement failure.

## Behavior and compatibility

Fresh explicit archives check readiness while the lead is retained. Portal repair
uses its saved model, effort and instructions, rechecks after each completed turn,
and stops after three cycles without progress or a request for operator input.
Delivery retries reuse persisted native identities. Preparation releases locks
between observations, fences same-session mutations and permits other sessions.
Only the existing archive executor stops agents and performs destructive work.
Existing journals bypass preparation; automatic and strict completion policies
retain their existing checks. No generic auxiliary-file deletion was added.

Private schema-1 preparation files do not change archive journals or cleanup
formats. Orderly portal shutdown parks an older-readable failed receipt; an old
package ignores private preparation files. No database migrations or dependency
updates. No obsolete approaches/fixup commits remain in the final two-commit series.

## Verification and review

Focused pre-review Ruby archive batch: 13 tests, 375 assertions passed. Initial
readiness tests: 3 tests, 60 assertions. Focused Go preparation, lifecycle worker,
target and shipped-browser checks passed (web 5.044 seconds).

After review remediation, Ruby readiness/authority/parent-permission batch:
6 tests, 104 assertions passed. Go preparation/native identity/archive readiness:
web 3.322 seconds and teamruntime 2.130 seconds passed; command package compiled.
Ruby, JavaScript and Python syntax, Nix parsing and diff whitespace checks passed.

High risk due to persisted operation state and destructive lifecycle behavior.
No retained reviewer exists in this tracking-only initiative. Installed catalog
`840de47527dea8325fcac0c2eb7ca5ae9728b31523ec368bcce595c6f15983fa`
provided standalone reviewer `/root/final_review`, gpt-6.1-sol/xhigh. It covered
general, architecture/repetition, scope/proportionality and risk/compatibility.
Initial findings: saved authority selection (Blocking), cancellation/send race,
removal-parent permissions, and native identity proof (Important). All were fixed
and folded into owning commits. Follow-up review cleared head `f094a94b`, with no
new Blocking or Important findings. It explicitly found no obsolete history,
repeated update streams or migrations. See the linked reports for evidence.

Fresh gpt-6-luna/low watcher `/root/packaged_checks` owns the packaged lifecycle,
host-package-contract and aggregate Ruby verification batch. Full-access policy
and utility identity come from the same installed catalog. Brief and evidence:
[packaged-checks-task.md](packaged-checks-task.md), `packaged-checks.log` and
`packaged-checks.status`. Results are pending.

## Recovery and remaining limits

The original HaveAPI generated gem cache was moved into its verified checkout,
then the accepted portal operation was retried with unchanged receipt/journal
identity. Attempt 2 completed. No lifecycle evidence was manually rewritten.
Retained branches were preserved; no archive/cleanup journal remains.

The packaged VM must still prove native shell repair, retained-lead behavior,
restart reconciliation, unrelated-session creation during repair, preflight
permission failure and later journal-owned recovery. Preflight remains sampled:
external writers or later I/O failures can require normal journal recovery.
The exact agent command that originally placed the sibling cache is unknown.

No owned VM or temporary test data predates the current verification batch.
The selected live package and this initiative remain active.

## First packaged failure and narrow repair

The first batch failed after 106 seconds: the package-layout archive-recovery
fixture copied a fixed module list and omitted the new readiness module. The
actual package already installs and links it. Added the module to the fixture's
copy and symlink lists; focused regression passed (1 test, 3 assertions). Aligned
the README lifecycle-test description with native repair and committed-content
restoration. No production behavior changed after final review. Inspected both
narrow changes directly under the mandatory review narrow-fix rule and folded
them into the owning two commits. Range-diff shows only this fixture/doc delta.

Current head `ef6c71a28fc0dc34f569210ae35aa981964041b2` is published. Superseded
CI run 40212466278 was canceled after verifying its old f094a94b head. Fresh
watcher `/root/packaged_checks_2` owns the same packaged batch, logs under
`packaged-checks-2.*`; its result is pending. The failed batch and derivation
receipts remain in `packaged-checks.*` and packaged-checks-result.md.

Packaged rerun milestone: aggregate Ruby verification reached complete shard coverage; main package build is compiling the portal. VM not started at this checkpoint.

## Second packaged failure and narrow repair

The second batch completed aggregate Ruby verification (complete unique shard
coverage) and compiled the shipped portal. Full package Go checks then found
one existing command-delegation test double returning no output for
`archive-check`. It now returns matching readiness JSON, leaving its original
high-level archive/revive argument assertions intact. Focused command-delegation
and preparation tests pass (web 3.534 seconds). No production code changed.
The owning portal commit was amended; current published head is
`d7ed6e886661a32afcb00c267bc2a54b3d447854`.

CI run 40212622111 failed the same fixture in archive, creation and fast jobs;
its failed logs were downloaded and inspected in `ci-ef6c71a2-failed.log` before
rerunning. No VM began in that run because the package prerequisite failed.
Packaged batch 2 took 545 seconds; complete evidence is in
`packaged-checks-2.*`. Batch 3 will test the corrected head. Both fixture fixes
and the README alignment are narrow verification corrections inspected directly
under the review narrow-fix policy. The independent production review remains
applicable; there are still two logical commits and no migrations.

## Older-reader verification preparation

Prepared an ad hoc extension of the exact packaged lifecycle VM in
`compatibility-session-archive.nix`, generated by `prepare-compatibility-vm.py`.
It adds the installed predecessor package closure and, during held native repair,
stops the candidate portal, starts the shipped predecessor portal binary with
the captured runtime arguments, reads the ordinary failed receipt, stops the
predecessor and resumes the candidate. The selected package/native server do not
change. This isolates the older-reader/shutdown boundary rather than claiming a
full host package rollback. No source deliverable or production behavior changed.
The Nix expression parses; execution will follow the main packaged acceptance.

## Packaged native setup correction

Batch 3 passed the package/component prerequisites and reached the VM. Its new
native scenario requested `--team solo`, but the generic default package has no
managed team catalog. Removed that preset selection, retaining the ordinary
root, explicit model/effort and initial goal. Extended failure diagnostics to
native/model logs. Also fixed the external HTTP fixture's models/usage routing
to accept native query strings (the failed VM showed `/models?client_version`
returning 404). These are bounded test-fixture corrections, not production edits.
Nix parse, Python syntax and whitespace checks pass. Head is now `33f5dab5`.
Batch 4 runs the same packaged checks after this correction.

Batch 3 logs: `packaged-checks-3.log`, VM derivation
`/nix/store/vcyvkpwzamz0s03yp2gxxi74packjp5c-vm-test-run-dev-workspace-session-archive-lifecycle.drv`.
It shut down its VM normally after the failed setup. No test reached repair yet.
CI archive at d7ed6e88 also failed; attempted early log download was unavailable
until its overall workflow completes. Preserve its run 40213519286 for evidence.

## Native CLI boundary correction

At head 33f5dab5, CI fast checks passed and its archive VM reached real repair,
portal restart and unrelated session creation. It then stopped after three
unchanged cycles. The public blocker identified a production dispatch omission:
`RequireArchiveIdentitiesAll` correctly accepts a missing roster after native
root proof, but `teamCommand`'s final JSON result loader did not include this
new command among root-only cases. Added it to the existing missing-roster
condition; no policy or proof changed. Focused CLI/native tests pass (command
0.062 seconds, teamruntime 2.048 seconds), Nix parse and whitespace checks pass.
This is a direct narrow boundary fix within the reviewed root-only contract.
It is folded into the readiness commit under the review narrow-fix rule.

The cache also stayed unmoved. The plain native fixture inherits access from
its config; its full access is now explicit so shell cleanup can reach worktrees
outside the conversation cwd. Added bounded rollout diagnostics for further
native failures. Production behavior otherwise unchanged since final review.
Published head `5e4e99dfecfda94da47c10cd154dfa98269a6533`, first commit `e4f6180f`.

CI evidence: `ci-33f5dab5-archive-failed.log` downloaded through the job logs API
and inspected before rerunning. `gh run view --log` cannot read an individual
failed job while its overall run remains active; use `gh api .../actions/jobs/ID/logs`.
That output needs `--allow-escape-sequences` when raw logs include ANSI codes;
logs remain local and bounded excerpts are used for diagnosis. Canceled the
superseded active CI run after verifying its head. Local batch 4 still owns
its captured 33f5dab5 snapshot and will finish without changing live state.
Delegation tools were unavailable for the next fresh watcher; parent monitoring
fallback was reported and used for batch 4 under dev-session-monitor.

Local batch 4 completed exit 1 with the same native root-only/no-progress failure as CI. Its package, aggregate Ruby and host-package prerequisites passed. Batch 5 now tests the corrected committed head 5e4e99df, with parent monitoring fallback; logs `packaged-checks-5.*`. No previous run remains active.

## Successful CI archive and remaining verification

CI run 40215486144 at exact head 5e4e99df: **archive and fast jobs passed**.
Archive used the same VM derivation as local batch 5:
`/nix/store/r8ihzf3w880nbbllsjpxymy3zi395bp9-vm-test-run-dev-workspace-session-archive-lifecycle.drv`.
Its test script finished in 498.14 seconds. Every scenario passed, including
native cache relocation, held-turn portal restart, unrelated session creation,
archive/revive, contention, interruption, permission preflight, post-removal
journal recovery and offline tracking sync. Full log is
`ci-5e4e99df-archive-passed.log`.

Local batch 5 passed its package/Ruby/host-package prerequisites, then hit a
browser hydration deadline before any archive POST. Captured diagnostics show
HTTP 200 for the page/assets/API responses, no JavaScript errors and no GET
operation response before Playwright's 30-second wait expired. This local timing
failure does not invalidate the exact-derivation CI archive proof; preserve
`packaged-checks-5.log`. The separate older-reader run will use a 120-second
browser fixture deadline in an ad hoc copy, retaining the same shipped app,
server and native commands.

CI creation failed in the existing naming-collision scenario: the creation
receipt reports `session is changing: resource temporarily unavailable` from
its destination runtime exclusive-lock acquisition. This is before initialization
and outside any archive preparation (none exists in that suite). `creation.go`
and the runtime-lock implementation are unchanged by this branch. Logs were
downloaded and inspected as `ci-5e4e99df-failed.log`. The implicated existing
nonblocking lock can race a read of the previous fallback-named session. This
is recorded as a pre-existing contention boundary; rerun only the creation job
after this diagnosis, not the successful archive/fast jobs.
