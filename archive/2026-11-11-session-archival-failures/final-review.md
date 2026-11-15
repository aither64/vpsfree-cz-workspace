# Final review — package R

No Blocking, Important or Advisory findings in the reviewed committed deliverable. The branch may proceed to the planned exact-head packaged CI checks. This is not a claim that integration, deployment or either live archive recovery is complete.

## Reviewed identity and scope

Reviewer: retained `reviewer0`, thread `01a1cbe8-2ad5-7ee0-8c9e-1ab799e21fbd`, review-purpose, ready, `gpt-6.1-sol` / saved `xhigh` / `read_only`. Own `dev-session current` from the bound tracking directory printed `2026-11-11-session-archival-failures`; both environment identity variables were absent and the trusted developer binding matched. No fallback or nested reviewers. All four assigned lane references and mandatory-change-review were read and applied.

Repository `git@github.com:aither64/dev-workspace.git`, worktree `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-11-session-archival-failures/dev-workspace`. Complete reviewed range: `6587c4c1cedabee95bcc52f4667e7d33e3a82859..359636df4e38b3f8c4049eb7e894c3c5eeca2625`. I inspected both full logical commits and the final diff, relevant adjacent admission/execution/monitor/store/lifecycle/UI code, existing and new tests, repository instructions, README and owning documentation. Final local HEAD matched the packet, worktree/index were clean, merge-base was the stated base, and base-to-head `git diff --check` passed. I ran no tests, builds, deployment or live lifecycle mutations; review commands were read-only. Lead will save this report verbatim because my read-only boundary excludes tracking-file writes.

## Scope and proportionality

The original recorded request concerns two failed Archive clicks and surviving registered services; the later recorded user direction is “implement it”. The two concrete causes are preparation treating transient runtime-lock contention as terminal and a historical monitor report retaining an effects fence because `stillRunning` contains completed-work prose. The implementation stays within those causes: one bounded admission retry loop, one new-event validation rule, existing status projections/presentation, instructions and regression coverage. It does not introduce a scheduler, persistent format, cleanup framework, heuristic interpretation of English report text or automatic resolution of old evidence.

The 12-file diff is +562/-6, with 417 added regression-test lines. The remaining source/docs changes fit the requested behavior. Records show investigation/design, upstream reconciliation, separate C/D delivery and quick-check milestones; the visible 18:39–20:10 UTC wall interval includes gaps and does not establish continuous active work. I found no delivered mechanism justified solely by internal design or speculative future needs. Keeping readiness before service shutdown is consistent with the supported ownership/external-effects boundary; bypassing those fences would expand the contract and risk data loss. Live recovery remains separately prepared.

## Correctness, architecture and risk conclusions

- Archive contention (`archive_preparation.go:377–459`): retry is limited to typed `EAGAIN`/`EWOULDBLOCK` from `LockRuntimeShared`, distinguished by a private sentinel. An action's errno, generation/identity failure or failed durable save is not silently retried. Each unsuccessful admission unwinds transition/runtime locks before the interruptible 100 ms–2 s backoff. The existing preparation record retains the receipt, attempt, target/journal, repair message/options/delivery, round and no-progress counters. Waiting updates the existing Error field without consuming repair rounds.
- Admission and cancellation: each attempt checks the current running request; successful runtime admission repeats generation/provider, pending lifecycle, retained lead/receipt and exact target proof before action. Cancellation/replacement prevents further native sends or archival. An admitted send still uses the existing message-lock/reconciliation protocol. No new ordering inversion or authority bypass was found.
- Restart (`archive_preparation.go:471–491`): a paused matching active preparation restores its semantic checking/rechecking/repair phase through the guarded updater. This preserves existing restart/replay behavior and makes Cancel/status available during the resumed wait. Existing failed receipts are not enrolled by error-string matching. No new persistent state enum or schema is introduced.
- Monitor (`monitoroperation/service.go:94–170`): the retained validator remains unchanged; the stronger invariant runs only after same-slot exact replay/conflict checks. New passed/failed terminal reports reject any nonempty `stillRunning`, including whitespace and `none`; incomplete reports remain fenced. Historical persisted reports and immutable exact retries remain readable, retain their original receipt and preserve the conservative effects fence. Reporter/owner/epoch/source-result checks remain ahead of API mutation; evidence resolution still requires exact ownership and native proof.
- Status/UI: live preparation Error and blocker projection makes the wait visible even over an older snapshot. Failure presentation identifies the blocker, retains Retry/Cancel behavior and states that service cleanup has not started, with Services navigation. It does not claim unknown services stopped. Detail is rendered through existing textContent paths. Actual shutdown-before-file-removal behavior and uncertain-cleanup recovery are unchanged.
- Ownership/repetition: archive preparation remains in its existing owner; monitor event admission is shared by Service.Report and the cold observer through AddEvent. Existing response projections/UI glue do not warrant another abstraction. Launch/skill/operator instructions describe the same invariant without creating a second enforcement owner.

Overall High risk classification is appropriate for lifecycle persisted/destructive admission. No new authorization, target, secrets or data-loss regression was identified within the trusted local-operator / untrusted remote-client boundary.

## Compatibility and consumers

No persisted schema, archive journal, public request shape, Codex protocol, cluster state or configuration input changed. New preparation records use predecessor fields/states; new monitor records remain acceptable to old readers. The new reader preserves retained contradictory reports and exact replay instead of rewriting history. An older resumed implementation can retain its old fail-fast behavior; safety/recovery evidence is not weakened by rollback. Old frozen utilities may receive the explicit new admission error if they submit contradictory *new* reports; accepted historical outcomes remain supported.

The generic runtime owns these interfaces. I checked the site workspace flake override at runtime base `6587c4c1…`, the pinned site extension `0c7168f…` package composition and the runtime's Codex/browser/CLI consumers. The extension delegates packaging to `dev-workspace.lib.mkPackage`; the affected internal fields/validation do not change its extension API. No companion consumer source or pin change is needed for this implementation review. Deployment and selection of the changed runtime are still pending and require their ordinary approvals/procedures.

## Whole-branch history and migrations

The complete series contains only:

1. `3a0af7ad6b97ae4a3a7e38921beac8a2cdf9ff54` — monitor admission, supporting tests and instructions/docs.
2. `359636df4e38b3f8c4049eb7e894c3c5eeca2625` — archive contention/status/restart behavior and supporting tests/docs.

Both have one independently reviewable behavior with its supporting material and appropriate rationale/compatibility commit bodies. No obsolete unmerged approach, fixup/tidy series or transitional compatibility path remains in the reviewed history. The superseded unpushed C head is not in the final base-to-head series. No migrations: the migration inventory is empty, including persisted-file-format migrations; there is no migration merge/release/deployment/external-consumption lineage to preserve. No dependency/channel/input/generated-artifact update stream exists, repeated or otherwise. No consolidation is outstanding.

## Documentation placement and preservation

Placement and preservation pass. README's existing grouped links reach `docs/session-archive-recovery.md`, `docs/dev-sessions.md#monitor-long-verification` and the relevant skill. README remains an entry point. Archive wait/blocker/cleanup ordering and recovery belong in the existing maintained operator guide; report semantics and legacy compatibility belong in the session guide; utility reporting belongs in the monitoring skill and frozen launch instructions. These explanations remain usable without private session context. Individual failure identities, historical unknowns and prepared recovery stay in session records.

The added claims agree with the final code and distinguish current supported behavior from recovery proposals. No material was moved or deleted, no old anchor or supported upgrade/recovery path was retired, and existing prerequisites, uncertain effects/cleanup, target proof and rollback constraints remain accessible. The authoritative runtime admission remains AddEvent; documentation/instructions explain it. No documentation-placement exception or lost preservation requirement was found. No deployment or successful live-recovery claim is added.

## Verification and remaining limits

The new focused tests cover admission acceptance/rejection, the exact historical malformed report, Store.Get and both exact-replay routes, immutable conflict and caller/epoch checks, fence preservation and evidence/native proof. Archive tests use disposable real locks for durable waiting, lock release, accepted repair/restart identity, cancellation, generation/target change, action errno and persistence failure; existing tests retain the three-round bound and unrelated-session behavior. Browser assertions cover wait/blocker and pending-cleanup presentation. These are meaningful tests of the owned behavior.

Quick-check reports were inspected, not rerun by me. Available logs confirm the D package pass (5.913 s) and C's corrected Go pass (18.235 s); C's later final 18.343 s rerun and corrected Node unit pass are recorded in implementation evidence. `/tmp/session-archival-c2.log` also retains the earlier Node harness setup failure, so it should not be cited as the final browser pass. This does not require another local rerun: exact-head CI supplies the next complete packaged result.

I inspected the unchanged workflow, flake checks/package checkPhase and archive VM scenarios. Feature-branch `fast` (evaluate all plus non-VM/package checks), `archive` and `creation` CI at this exact final head are a sufficient next gate; no duplicate local package/VM execution or host-activation lane is justified by these changes. The existing archive VM covers preparation repair/restart, unrelated-session availability, supervised worker shared-lock waiting/restart, service descendants/unload and failure preserving supporting files. Its shared-lock wait scenario exercises the executor; the new preparation-exclusive-lock wait/cancel/restart cases are specifically focused Go evidence. Keep those scopes distinct.

Residual limits: packaged CI is pending; these tests do not reconcile historical local tool-session effects or unmanaged HaveAPI content. No deployment, live monitor resolution, archive retry, service stop or service retirement has been performed by this work. Native proof still does not inventory every operation-owned external code cell; the documented reporting/evidence contract retains that limit. Do not declare either original session recovered from code review alone.

Next action: record review accepted/resolved with no findings, publish the feature branch and obtain exact-head CI results. Integration, deployment and live recovery remain separate decisions. Session stays open.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-11-session-archival-failures/
