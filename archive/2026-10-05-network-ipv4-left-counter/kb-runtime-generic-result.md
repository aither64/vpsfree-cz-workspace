# Public capture-lease transport checkpoint

The generic runtime change is committed and published on development branch
`2026-10-05-network-ipv4-left-counter`. Its published checkpoint is
`9fe491218e35a3250f2a72c203c2cecc3cb7ae16`, directly after
`e3315a483f3d3536d492ecbe40f2655449cf630f`.

The lease commit has since rebased unchanged onto upstream a2bbf2f1 as
c582ee757cd5b55c69db7b030ffd25eae8e5635b. Upstream owns the functional Go CAS
fix; the separate minimal deadline/test supplement is committed and published
as final head 51aba080b264c28f5584867b6cf006bf423ae2f3 with new-base checks
passing.
See [preservation and reconciliation evidence](kb-runtime-d-upstream-result.md).
E selects this final head. Its canonical immutable source is
`/nix/store/y7r40b5h4hd44jfzan4kv1zar3rxmyyl-source`; selected source and lock
bytes were checked against the commit. Superseded active CI inventory has no
candidates; only current-head run 37639120229 was active and excluded. No CI
wait or cancellation occurred.

The initial published 9b5bb4d checkpoint is retained in the evidence. The stdout
EOF correction was folded into this unmerged feature commit after focused
checks passed. Normal commit hooks were used; the clean final tree equals the
inspected staged tree. Publication used the verified old feature lease and
proved the new exact remote head. Default branches are unchanged.

Only `libexec/workspace-host`, its existing command/lock test file and
`docs/workspace-portal.md` change. Provider commands beginning with
`capture-lease` use mediated input/output/error pipes under the existing
package-generation guard. The dispatcher alone reaps its spawned provider;
other provider commands retain buffered dispatch. No persisted-state or catalog
schema changes or migrations are included.

## Verification

The original checkpoint's bytes passed `kb-runtime-generic-quick4.sh`: Ruby toolchain,
two syntax checks and 17 focused real-process/retained examples, with 171
assertions and no failures, errors or skips. All aggregate/per-step exit receipts
are zero. Recorded Ruby 3.4.9, Minitest 5.26.1 and timeout 0.4.3 load from Nix
store paths. The lead inspected the actual receipts and source diff.

The earlier quick2 run failed in its fake catalog fixture and loaded ambient user
gems. Its failure receipts remain unchanged. Quick1 and quick3 are unexecuted
preparation snapshots. The first quick4 watcher refused before launching because
the lead supplied an ambiguous overwrite prefix; the replacement watcher used
the exact `kb-runtime-generic-quick4` prefix and ran once without overwriting
earlier artifacts.

Normal commit/publication operations both exited zero. The repository declares
no hook framework, and the inspected effective hook directory contains only
samples. No hook bypass was supplied. The committed diff equals the frozen
quick4 diff, and the final worktree is clean. An independent SSH read established
that the feature ref was absent; publication rechecked the remote and proved the
exact pushed head. Default branches are unchanged.

## Stdout-loss correction

Source inspection subsequently found that provider stdout EOF was ignored until
process exit. The accepted lease contract requires prompt protocol closure even
if that process remains alive; stderr EOF alone is harmless. Architect0 confirmed
the boundary and assigned matching generic/client corrections and focused cases.
The original passing receipts do not cover that missing case.

The first correction run, `kb-runtime-generic-eof-quick1`, passed toolchain and
syntax, then reported 20 tests and 180 assertions with two Timeout::Error
errors and no assertion failures or skips. The errors occur while waiting for
downstream protocol EOF and for completion after pre-readiness stdout closure.
The other 18 tests, including stderr-only closure, pass. Root inspected the
logs and assigned source/fixture diagnosis before a new run. Its aggregate and
test exits are 1; the packet and failure evidence remain unchanged.

The root's declared Ruby 3.4.9 language probes show that STDOUT.close retains its
original fd1 pipe even with autoclose enabled. The next run (quick3) preserved
the assertions and timed out in all three stdout-loss cases: 21 tests, 181
assertions, three errors, no assertion failures or skips. Toolchain and syntax
pass; aggregate and commands exit 1. Reopening the standard stream to File::NULL
does release its original pipe. The correction deliberately detaches that pipe
and uses genuine half-close fixtures. `kb-runtime-generic-eof-quick4` passed all
four receipts and 21 tests/211 assertions with zero failures, errors or skips.
It includes default standard-stream dispatch, before/same-window stdout loss,
guard-held cleanup and harmless diagnostic stderr EOF. These checked bytes
match the consolidated current head. The language probes alone were not
accepted as transport proof.

The bounded superseded-CI cleanup exited 0 and found no candidates. Its active
inventory then included only current-head run 37597668723; no CI wait was run.

A later read found that run completed with a package-check failure in the
unchanged Go portal test
`TestArchiveJournalRetryRefusesASameKindReplacementWhileWaitingForTheLock`.
The failed step log is retained as `kb-runtime-generic-final-ci-failure.log`.
The implicated portal tree equals the e3315a48 baseline. Source tracing supports
a lost-CAS reconciliation: a display worker accepts journal A's progress after
the fresh-owner caller reads replacement B, so B's proposal is discarded and
the caller returns A without an error. The executor still rechecks the journal
under its mutation lock; this log does not show a replacement command ran.

The lead accepted a separate narrow portal repair for complete package proof.
Its original draft passed focused and full web checks. Fresh upstream then
supplied the functional fix in 8f0f40a; the ancestry guard stopped the proposed
local commit before staging. The final branch will inherit that fix and add
only post-proof deadline checking and deterministic regression coverage. A
green rerun alone would not resolve the original defect.

## Remaining work

The standalone KB runtime and optional extension adapter remain under
implementation. The extension will pin the corrected final published generic revision.
Final independent review covers all completed committed tooling branches after
their quick checks. Flake/package and isolated runtime/capture proof follow that
gate. This checkpoint does not certify real KB capture, package activation or
default integration. No VM, cluster lifecycle, PR or deployment action ran.

Evidence is retained under `kb-runtime-generic-quick4` and
`kb-runtime-generic-operation-{commit,publish}` for the original checkpoint,
and `kb-runtime-generic-eof-quick4` plus `kb-runtime-generic-eof-final` for the
corrected current feature head.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-05-network-ipv4-left-counter/)
