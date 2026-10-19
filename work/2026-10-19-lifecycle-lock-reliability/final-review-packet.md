# Final review packet

User asks to fix dev-session archive contention generally, deploy to aitherdev
through configuration, finish the original failed archive, and release machine
reservations on successful archive. No master integration is authorized.
Initiative: 2026-10-19-lifecycle-lock-reliability. See plan.md, design.md, state.md.
Complete final ranges and commits are in branch-inventory.json; full final diffs
are *-review.diff. All intended substantive changes are committed and clean.

Overall high risk: persisted lifecycle/coordination state, destructive cleanup,
portal authorization, concurrency and deployment ordering. Review all four lanes:
general, architecture/repetition, scope/proportionality, risk/compatibility.
Review directly without nested agents. Remain read-only except your report.

Runtime owns CLI/session locks, journal recovery, saved portal receipts, the
coordination ledger and lifecycle completion. Portal invokes installed CLI and
reads the existing progress schema. Workspace composes runtime through its direct
nested input, preserving extension 767dfd587e346168e1443e65ccdb67ce748f3fe3.
Configuration dev-workspace/devWorkspace channel selects matching host contract.
Extension/codex-web are unchanged. Composition checker passes at final runtime.

Explicit lifecycle requests wait for creation and exclusive session access,
revalidate target or journal and exact saved portal receipt after waiting; no
mutation replay. Automatic scan remains nonblocking and preserves inactivity
proofs. Portal no longer holds conversation message mutex across CLI lifecycle,
preventing shared-runtime-lock/message-mutex inversion. Revive's internal start
and lock reacquisitions remain in request context. Existing deadline boundaries
are retained; local archive worker has no total deadline. Existing progress
schema shows Waiting for session access / Preparing archive.

Archive completion releases exact bound owner's reservations atomically with
lifecycle receipt completion. Fence holds during incomplete cleanup and cancels
queued jobs. Running/uncertain deployment recovery must settle first. Completed
receipt replay may release predecessor holds while exact fence/owner matches;
revival does not reacquire/requeue. No integration proof needed to close an
explicitly archived session. Deletion semantics unchanged. Retain history and
artifacts. No migration/schema/CLI flag changes. Existing journal readers remain.
No new generic lock manager, automatic retries of mutations, force release,
ledger edits or broad bootstrap. Trusted local operator, untrusted remote clients;
review ordinary concurrency, wrong identity, interruption and authorization.

History: runtime has two coherent commits: lifecycle repair then explicit latest
reservation policy. Test follow-ups were amended into the lifecycle commit.
Prior unmerged dd39/78d29 and consumer pins superseded; no supported intermediate
consumer/state boundary requires retaining them. Each consumer has exactly one
final pin update stream plus policy documentation. No migrations in any range,
none merged/released/deployed/externally consumed. No feature commits deployed.
Prior independent original-session reviews remain separate historical evidence.

Documentation: runtime docs/session-archive-recovery.md, docs/coordination.md,
docs/coordination-operations.md own contracts; workspace docs/agent-instructions/
lifecycle.md and deployment.md, config docs/operations/workspace-coordination-
aitherdev.md link policies. Rollout specifics stay under this initiative.

Quick verification: Go ./internal/web ./internal/session passed (TMPDIR=/tmp,
-mod=readonly). Full Ruby 467 tests/6906 assertions: one obsolete immediate-fail
expectation only, fixed; focused rerun passed 1/25, plus 6/82 lifecycle subset.
Full coordination suite passed 57/399 before last narrow no-history hold change;
final focused suite passed 6/28 including that change, deployed hold release,
idempotence, another-owner isolation, queued cancel/revive, uncertain refusal.
Ruby syntax, app.js syntax, diff checks, Nix evaluation and Nixfmt passed earlier;
configuration hooks pass final source. Packaged/VM checks will follow review.
The full batch's source fingerprint is recorded in final-quick-result.json;
it is mixed pre-consolidation history and not claimed as a clean final-head run.
Final full package verification will run exact final revisions.

Rollout: original owner 6a0351a8-0f36-46ce-aed4-952be3b8a569 retains aitherdev
reservation 1ce9be0f-bd17-4c85-ab64-1a94fd352c4c, deployed_review revision4.
All original jobs succeeded, no lifecycle fence/journal. Original work is merged.
Proposed supported bootstrap ordering: use existing stable finish for old owner,
with recorded integrated final heads and existing independent rebase acceptance;
then ordinary new-owner system/profile approved jobs; then retry original saved
archive. Prepared old-owner finish request and lineage artifacts are under
../2026-10-19-session-archive-refresh-fix/release-*.json and *-range.diff.
No old branches/registrations modified. Exact stable finish independently checks
patch IDs, remote ancestry and live system/profile identities. Latest user
direction to archive/release supplies completion intent. This release is an
operational step, not new feature integration. Verify this sequence is compatible.

Acceptance: genuine contention waits within same request, stale target refuses,
portal restart worker survives, no lock inversion, automatic evidence preserved,
successful archive releases only its machines, failures preserve recovery,
revival retains recovery/branches without taking released machines. Review gaps
and concrete concerns rather than requiring hypothetical local adversary checks.

Write final report to final-review.md. Read applicable AGENTS.md and mandatory
review skill + all four lane references. Report findings ordered by severity,
whole-series/history and no-migration conclusions, and residual test gaps.

Final replacement inventory now available in branch-inventory.json (all clean).
Runtime a2c895d includes only timing-test-followup.diff beyond initial runtime
5882296. Focused timestamp check 1/5 passes. Final consumer pins regenerated via
their supported paths and each stream remains a single commit. CI initial failure
was this same obsolete timestamp assertion. Verify final report against current
inventory; no further intended code edits.

Review remediation in progress: reviewer found completed-cleanup-sidecar retry
skips coordinator completion when main journal already removed. Added replay
at cleanup.discard_completed!'s post-validation/pre-unlink callback boundary.
A real CLI/store regression now simulates predecessor deployed hold, failure of
completion replay retaining sidecar, then exact retry releasing hold without
repeating tracking commit. Await focused result and final reviewed head update.

All requested review fixes now committed and quick checked; complete final
inventory updated again. Runtime 9deefdf (sidecar replay, requested reservation
non-exclusive fence, CLI revive preflight). Workspace 2a0ea35 (also coordination
policy doc advisory), configuration 77bb990a. All clean, all published. No schema
or migration. Pins each consolidated one final stream. Direct narrow-fix checks:
sidecar CLI/store 1/30, reservation queue/timestamps 4/25, CLI confirmation 4/32.
See review-remediation-status.md, review-sidecar-remediation.diff and
review-cli-remediation.diff. Final report should bind these exact ranges.
