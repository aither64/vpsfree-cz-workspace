---
lifecycle: complete
---

# 2026-11-06-portal-message-delivery

## Status

Completed November 9. Delivery/evidence, interruption and packed-ref fixes are
deployed on aitherdev, verified live and integrated into all three remote master
branches. The machine and repository claims are released. The session stays open.

- [x] Investigate incident, design and implement delivery/evidence fix.
- [x] Remove aggregate packed-ref cap that blocked queued claims.
- [x] Rebase and consolidate branches; independent review and findings resolved.
- [x] Final CI, application/workspace and host/recovery verification passed.
- [x] Deploy matching system and user-profile application without reboot.
- [x] Verify health, naming and original Codex/tmux process continuity.
- [x] Merge all final heads, verify remote refs and preserve unrelated shared index.
- [x] Release all claims and remove clean temporary merge worktrees.

Final integrated heads:

- dev-workspace/master: d2cb9975a88079d79f361c5b4c65836ba0835821.
- workspace/master: 6e7d4514879d5e5d4c81f6da95c56105edf9c75a.
- vpsfree-cz-configuration/master: 612b3459ec9b81bf24ae078a06da487648675001.

CI [42536185097](https://github.com/aither64/dev-workspace/actions/runs/42536185097)
passed on the exact runtime head. Both local host VM checks passed. Configuration,
application and workspace checks exited 0. System/profile rollout and both health
checks exited 0; HTTP health/session pages return 200 and ephemeral naming passed.
Codex PID 1309145 and tmux PID 1917 were preserved; portal PID is 4101945.
See [rollout](rollout.md), [full review](review-nov8.md) and
[fixture follow-up review](review-fixture-nov9.md).

## Next actions

None required. Keep feature refs and the session available. After evidence
conversion, software recovery must use a SQLite-capable package; preserve
markers, databases, legacy backups and native receipts. No original incident
conversation was sent test messages or interrupted by this rollout.

## Documentation

[Plan](plan.md), [design](design.md). Project behavior and forward migration are
owned by dev-workspace docs/turn-retry-recovery.md; browser behavior by
docs/workspace-portal.md. The packed-ref diagnosis is in
docs/coordination-operations.md. Actual deployment is recorded in rollout.md.

## Repositories

dev-workspace origin/master initially 240a53dafabf24b6718195b88bee012a4ead8698.
Feature branch: 2026-11-06-portal-message-delivery.
Worktree: worktrees/2026-11-06-portal-message-delivery/dev-workspace.
Current published heads:

- Runtime d2cb9975a88079d79f361c5b4c65836ba0835821 (base 32a5e31b).
- Workspace 6e7d4514879d5e5d4c81f6da95c56105edf9c75a (base 2d45c4df2).
- Configuration 612b3459ec9b81bf24ae078a06da487648675001 (base 1072f89f).

Fresh fetch at 22:56 UTC on November 8 confirms these bases are current.
Shared workspace master has two pre-existing tracking commits beyond remote;
the feature descends from both, so no additional rebase is needed.

## Commands run

`dev-session current` found no bound session or environment identity. Created
`2026-11-06-portal-message-delivery` with `--as-is --no-attach --no-codex` and
verified `current` with its exact slug/workspace environment. The CLI rejects
`--as-is --new`; a noninteractive Codex start requires a goal file, so threadless
tracking was selected to keep execution in this conversation.

Fetched workspace and dev-workspace origin. Shared master has unrelated changes
and commits; preserve all of them. No declared workspace hooks or active hooks.

## Results

Portal URL: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-06-portal-message-delivery/

## Implementation and verification

- SQLite evidence replaces the total snapshot/JSON budget, retaining a bounded
  read batch and indexed identity/turn lookup. Shared settings are deduplicated.
- Explicit delivery no longer advances transcript proof. Optional capture or
  receipt-proof failure holds automation; positive native receipt stays accepted.
- Cancellation persists before dispatch. Confirmed exact interruption settles
  immediately. Definitely unsent failures use the existing typed browser error.
- Migration retains JSON backup and uses an incompatible marker plus completion
  flag; old packages cannot write schema 3, and rollback requires the capability.
- Native fixtures read schema-3 metadata. Idle hints include evidence revision.
- `quick-delivery.log`: focused retention/replay/queue/crash/automatic-result Go
  regressions passed (86.760 s). Initial storage tests identified fixture-only
  assumptions about internal cache equality and JSON records; assertions updated.
- `focused-evidence-delivery.log`: new delivery/proof-failure/interruption tests
  passed; one remaining lifecycle fixture cache comparison failed and was fixed.
- `quick-package.log`: direct subfile launch failed because TransitionHost is
  loaded by test/workspace_host_test.rb. Corrected verification uses that aggregator
  with a name filter; no product defect inferred from the harness error.
- `check_final_focused`: fresh Luna/low watcher owns the focused final batch.
  Previous `check_delivery_storage` watcher completed and will not be reused.
- No repository hook framework declared; canonical hooks directory contains only
  sample hooks. Nix environment prepared via nix print-dev-env and sourced for checks.

## Open questions

Root cause of the original prefix-compaction stall is not yet proven.

## Cleanup

No temporary services or development clusters. Retain the session and branches.

## Final review checkpoint

Both commits are local and unmerged: c7454451 (delivery/evidence) and 79a1cc86
(interruption). Clean worktree; upstream unchanged after fresh fetch.
All focused final checks passed (storage 25 s; delivery/web 80 s; Ruby 11 tests,
243 assertions). See [review packet](review-packet.md) for exact revisions,
all four lanes, high-risk rationale and migration lineage. Standalone fallback
reviewer will use installed gpt-6.1-sol/xhigh because the initiative is threadless.

## Review findings and remediation

[Independent report](review.md): /root/final_review, gpt-6.1-sol/xhigh,
all four lanes. No Blocking findings. Two Important findings fixed:

- R1: ErrMigrationPending distinguishes interrupted conversion. Passive idle
  reads request the full path; authorized cancellation/reconciliation reaches
  the existing lock. Completed missing databases still fail closed.
- R2: held cold-delivery activation logs optional binding failure and continues
  the recovery permission update; native activation and authority errors remain
  errors. Exact accepted queue identity survives replay.

Direct focused remediations passed in review-fixes.log: storage migration,
normal cancellation, scheduler recovery (including unknown automatic identity),
and cold root/member delivery/replay. No new design or supported boundary was
introduced, so the skill's narrow-fix rule permits lead verification without
another reviewer turn. Legacy-proof hypothetical was unconfirmed by review;
normal legacy proof is for an already terminal/handled failure. Keep the existing
conservative proof requirements without adding speculative lifecycle support.

Whole-branch history/migration conclusions: no obsolete approaches, one direct
legacy 1/2 -> SQLite schema-3 migration, never deployed/released/consumed outside
fixtures, no repeated dependency streams. Remediations will fold into the first
commit before publication; original reviewed range stays in review.md.

Final consolidated heads: b7b8c797208d3755998c4269855ae3ada6c9e143 (delivery)
and 2f1585f867baaf94d809a65b46019e5ae19c08be (interruption). Rebase conflict
was only overlapping fixture fields/cases between those logical commits. Exact
final tree equals the verified pre-consolidation 422e6f3f tree (`git diff
--exit-code 422e6f3f HEAD` passed). Both fixes are folded into their owning commit.
Lead checked the complete final series and final diff against review and narrow
remediations. Feature remains unmerged and undeployed.

Publication: branch pushed over SSH at 2f1585f867baaf94d809a65b46019e5ae19c08be.
CI run: https://github.com/aither64/dev-workspace/actions/runs/42238633687.
The fresh Luna/low packaged_verification utility owns `nix flake check
--print-build-logs` for that exact head. No live package switch or deployment.

## Packaged verification follow-up

The first packaged run failed after about 10 minutes, and CI 42238633687 failed
on the same package tests before its dependent VM checks could run. Failure logs:
packaged-verification.log and ci-first-failure.log. Ruby suites passed.

Five test groups retained old expectations: synchronous proof during Send
(plan delivery, manual observer assignment, recovered settings), a delivery-unknown
response after successful native acceptance plus optional retry receipt-save
failure, and aggregate marshaled snapshot bytes below the removed storage cap.
Tests now explicitly advance the independent proof worker before checking its
exact digest/binding; accepted delivery remains successful; 74 unverified inputs
must remain indexed beyond the 64-row load batch. Existing lost-native-response,
same-ID replay, retry-eligibility and handled-turn suppression assertions remain.
No production behavior or supported contract changed after review.

Focused plan/progress/recovery tests passed (web 3.141 s, workspacecodex 1.142 s).
The volume regression also passed (52.520 s). These are narrow fixture updates to reviewed
behavior, with no new design or compatibility boundary; retain the final review
and verify the adaptations directly under its narrow-fix rule.

Final series after folding those test updates:
13888b983675aa60dd800b4d7b7d18e2c3b1508a (delivery/storage) and
59d2fe184742694e23378a57de63ae8241f6b8ef (interruption). Clean worktree;
tree equality with pre-consolidation f45339d5 and diff whitespace checks passed.
The only difference from the preceding published tree is the four test files
above (29 additions, four removals). Full branch history remains the reviewed
two logical commits, with unchanged migration lineage. Fresh fetch confirmed
origin/master unchanged at 240a53dafabf24b6718195b88bee012a4ead8698.
Exact-lease push and ls-remote confirmed the final head. The superseded CI run
had already completed, so there was nothing to cancel.

Fresh final_verification watcher: gpt-6-luna/low, installed utility policy,
full access, one operation batch. It owns final `nix flake check
--print-build-logs` and observation of CI 42241575057 at that exact head.
Log: packaged-final.log. CI:
https://github.com/aither64/dev-workspace/actions/runs/42241575057.

CI attempt 1 fast job 127972917870 failed fetching the unchanged esbuild 0.28.2
npm tarball: registry.npmjs.org returned HTTP 503. The package did not reach
its test phase in that job. Evidence: ci-final-fast-failure.log (downloaded
directly through the completed-job logs API while the other jobs continued).
This is an external dependency fetch failure; no lock/dependency change belongs
in this delivery fix. Once the current verification batch finishes, retry only
the failed job and observe it with a fresh utility.

The final batch ended after 22 minutes locally and 21 minutes in CI. CI archive
and creation both passed. The local archive failure occurred before an archive
mutation: unchanged archive_lifecycle_browser.cjs:63 waited 30 seconds for the
initial GET operation response. Navigation itself took 15.138 s, and the
operation request started only at 28.240 s; the browser timed out before its
response. No browser script error was recorded. ERR_ABORTED appeared on a
coordination poll during browser cleanup; it was not the root assertion.
Multiple VM tests were running concurrently. Resource contention is consistent
with the delayed page hydration but not proven; this does not establish a
delivery or migration regression. CI passed this same archive scenario on the
final SHA. Keep the original log and rerun unfinished/failed local checks with
Nix max-jobs=1 to remove concurrent VM contention, without changing test limits
or product code. Also retry only the CI fast job after the confirmed npm 503.

Fresh utility launching became unavailable in the continuation; using the
monitor skill's visible parent fallback for this retry batch. Local command:
`nix flake check --max-jobs 1 --print-build-logs`, log packaged-serial.log with
packaged-serial.exit. CI: rerun only job 127972917870 in run 42241575057; watch
log ci-retry-watch.log and ci-retry-watch.exit. Source remains unchanged at
59d2fe184742694e23378a57de63ae8241f6b8ef.

Serial rerun passed the previously failing archive-preflight subtest in
150.22 s and continued into later archive tests. To avoid repeating successful
CI coverage, the lead then verified exact derivation identity against completed
CI job logs and stopped only the owned serial flake-check process (verified PID,
cwd and full argv before SIGINT). This is an intentional cancellation, not a
test failure or a claimed all-green local flake check.

Exact reused CI derivations (same final source/input graph, captured in
ci-reuse-derivations.json):

- archive: /nix/store/9i9knvc4k43apd0l7wjq3qw6ks2xj3k9-vm-test-run-dev-workspace-session-archive-lifecycle.drv;
  passed 513.72 s; ci-archive-passed.log.
- creation: /nix/store/vsypfk45i2mf1j9fzp5qf5qp34wpzbld-vm-test-run-dev-workspace-session-creation.drv;
  passed 794.51 s; ci-creation-passed.log.

check-derivations.json records all 29 evaluated check outputs. Local Nix store
validity confirmed 25 outputs; remaining were archive, creation, recovery-boot
and agent-team-catalog. The first two have exact CI successes above; CI fast
covers agent-team-catalog. Only recovery-boot still needs local execution, now
running with `nix build --no-link --max-jobs 1 --print-build-logs
.#checks.x86_64-linux.session-recovery-boot`. Log: recovery-boot-final.log and
recovery-boot-final.exit. No source, timeout or product behavior changes.

Recovery-boot passed with exit 0; VM script 294.01 s. All six subtests passed,
including journal recovery across daemon-stop reboot, lingering startup and
preserving foreign processes. Local operations are finished. CI fast is the
only remaining verification operation, including its agent-team-catalog check.

## Final readiness

CI run 42241575057 attempt 2 completed successfully on exact published head
59d2fe184742694e23378a57de63ae8241f6b8ef. Fast, archive and creation passed;
host is skipped by feature-branch workflow policy. Evidence: ci-passed.json,
ci-fast-passed.log and ci-retry-watch.exit (0).

All 29 evaluated checks are covered: 26 exact local successes, plus three
exact CI derivations for archive, creation and agent-team-catalog. The latter is
/nix/store/hscyam0whmmf77bf8rzfdwvfxlh8379q-dev-workspace-agent-team-catalog.drv,
matching the captured local derivation, input graph and output. Lead verified
that each reused derivation appears in its successful CI log and its output
matches check-derivations.json. This combines local/CI evidence; the earlier
full local flake check retains its recorded browser-timeout result.
The 25 local output identities were verified before the final recovery-boot
success. By final handoff, many of those unrooted outputs had disappeared from
the store; this does not invalidate their recorded success or require rerunning
unchanged inputs. Exact identities and logs remain in the retained evidence.

Final worktree is clean. Complete branch series remains two logical commits;
review findings and later test-only adaptations are folded into delivery/storage.
No obsolete intermediate migration or repeated pin history remains. No unresolved
code/review blocker. Software recovery after migration requires SQLite evidence
support; older packages cannot read the new state. The original long-turn stall's
underlying cause remains unproven, separate from the confirmed delivery cap.

All owned verification processes and disposable test VMs have finished or been
explicitly canceled as recorded. No deployment, integration, session archival,
service shutdown or branch deletion was performed.

## Authorized deployment continuation

User: "aitherdev can be deployed using vpsfree-cz-configuration. once deployed
and verified, you can merge it". This covers the runtime and required deployment
pins, with integration conditional on verified deployment. No reboot authorized.

Registered workspace and configuration worktrees under the same slug.
Workspace pin f5e060e4a2bf0b7f3c7204b2861f4609c3d028c0 and configuration
pin 50988c8b8bd5f2fd4e13e9892b999ed65ff21da4 are committed/published.
Only the generic runtime identity changes. Matching deployment-contract check
passed. Mechanical pin review exemption and complete history are documented in
rollout.md. No push-triggered CI exists for either pin repository.

Fresh native CLI verification utilities use installed gpt-6-luna/low and explicit
danger-full-access/approval never. Environment utility
01a1b21e-98b2-7e32-94f6-aff67033030c passed. Build utility
01a1b221-6b6a-7531-b6d5-b33ac07ae6c0 owns package, workspace checks and confctl
aitherdev build; actual launch settings verified from its header. Logs and exits
are named in deploy-build-prompt.txt. Lead owns all activation and merge work.

Configuration generation 2026-11-06--19-32-52 built successfully (exit 0);
system output /nix/store/xlbjz1jbyhdk5mxd9pfl6yvq2rxs18ra-nixos-system-aitherdev-26.05.20261026.718f670.
The first CLI package watcher ended before build completion; its process had
exited and no exit receipt or candidate link existed. No package failure was
reported. Fresh native utility /root/finish_profile_build (gpt-6-luna/low,
full access) resumes the build and workspace checks, preserving the first log.
No machine claim or activation has occurred.

## Deployment checkpoint: resource wait

Fresh native utility /root/finish_profile_build completed the resumed application
build in 381 seconds and workspace flake checks in 12 seconds, both exit 0.
Exact workspace head: f5e060e4a2bf0b7f3c7204b2861f4609c3d028c0.
Application output: /nix/store/rvfzq44dbw4d14adpn9q7ggbdzgrnr93-dev-workspace-0.2.0,
rooted by profile-candidate. Evidence: profile-build-resume.log/.exit and
workspace-checks.log/.exit. All owned build processes finished. Feature worktree
remains clean; the build's dirty-tree warning did not correspond to a source diff.

HTTP baseline /healthz and this session page both returned 200 (http-before.json).
Selected profile, system paths and portal/Codex/tmux PIDs remain the recorded
predeployment baseline. Matching deployment-contract check passed again.

At 2026-11-06 18:49:19 UTC, schema-2 machine request
51c9bb18-85d5-4150-8e88-5176510372a7 returned waiting, owning no resources.
The existing held claim 5ed5527b-c5b0-42fe-8d2d-53aacf27fd81 belongs to
2026-11-03-lead-wakeup-delivery (owner 79f69d8f-00d6-40ac-b51f-fba66bd482ee),
held since 2026-11-05 08:53:38 UTC. Its reservation prevents activation.
No bypass, cross-session message, deployment, merge or other-session mutation
was attempted. Installed mutations use `dev-session coordination`; the attempted
`workspace-host coordination acquire` refused without effect because that entry
only supports status. Original request JSON is saved as machine-claim-request.json.

Workspace coordination requires ending the turn when only a resource wait
remains. Keep lifecycle active and preserve the queued request. The existing
owner must reconcile/release its own reservation through its normal workflow.

## November 8 status check

Checked at 2026-11-08T22:26:36.153440+00:00. Original request remains
waiting; previous blocking claim is released. Installed profile now
/nix/store/9yibngx0gbiq17waqffcgszk067ngmhb-dev-workspace-0.2.0; live system
and system profile both
/nix/store/kycb055vxzjn9jzz4yyfwbgf673z6q8s-nixos-system-aitherdev-26.05.20261026.718f670.
Remote master heads: runtime 32a5e31bc32362b436ccc0cfc45b5d1b74f64cb6,
workspace 0c112efeb3e88b62ca0d48feb532bab93303735c, configuration
1072f89f932ad570fb6d14007387d230549ccd14. Published feature heads unchanged.
Local ancestry confirms runtime/workspace exact feature heads are not merged;
the new configuration target object is not locally available yet. Status-only
reads performed; no fetch, deployment, integration, or claim mutation.

November 8 continuation: found repeat coordinator error "machine source packed
refs exceed their bound". Prior held claim was released; canceled our stale
waiting claim through ordinary cancel-claim (revision 2, canceled). No resources
are held. Runtime rebased on 32a5e31b; conflicts preserve upstream timing
diagnostics, descending discovery fixtures and maintenance suppression alongside
the original asynchronous-proof changes. Rebase evidence: rebase-nov8.diff.
New heads fbba0e2e/8ef50902, not published yet. Queue fix brief added to design.

Final Nov 8 refreshed runtime: 849bfdda; packed-ref tests and rebased focused
Go checks passed. All intended changes committed; pins regenerated on current
workspace/configuration. Old claim canceled, no resources held. Fresh final
review packet review-packet-nov8.md covers new packed-ref fix, upstream conflict
integration and full migration/history. Scope retains newest installed runtime
behavior; exact installed/master tree diff is only one browser-test change.

Refreshed companion heads: workspace bcee53dd6b0058b1c2f18ce402a40dd42309dfdf
(base 8aae9bd4af090260a92ec0296472fadce13c6cd7, includes two shared tracking
commits beyond remote master); configuration 2d050cfc26b23dce824e88ee61e83e2e929e7d0d
(base 1072f89f). Exact comparisons captured. Feature pushes use explicit leases;
superseded runtime CI 42531451725 canceled. Final CI 42531660276 is on 849bfdda.
Current baseline profile 9yibngx0gbiq17waqffcgszk067ngmhb; system kycb055v.
Portal PID 1475620, Codex PID 1309145, tmux PID 1917; maintenance status none.

Nov 8 final review found Important R3: maintenance fence blocked native Stop
after recording suppression. Restored upstream retryAdmissionUnfenced in
Interrupt. New regression reproduced refusal with retry enabled and disabled,
then passed; combined maintenance/interrupt tests pass (1.100 s), review-r1-nov8.log.
Folded the narrow fix into interruption commit under review step 9; no new
behavior boundary or migration. Final runtime d23a0e302246c2e3929d0856cf62f92eaf7ccea8,
series c96503ea (delivery), 986261ac (interrupt), d23a0e30 (packed refs).
Reviewer /root/final_review_nov8 gpt-6.1-sol/xhigh accepted full history, migration
and pin consolidation, with no other findings. Packed refs unchanged from review.
Regenerate each pin into one final commit; no intermediate rollout occurred.

Final pins published: workspace 437f437befffaa790ea44b6bdd496dd06f6a1483;
configuration 830df3f5bfd3816fb754ea2b9b9ebedc8fb8fcf6. Single pin commits
retained after R3 update; mechanical diff only selects final runtime d23a0e30.
Deployment contract passed; comparisons recaptured. Fresh CLI utility
01a1bd5d-3540-7272-901c-f331c88e689d owns verify-nov8.sh; launch verified
gpt-6-luna/low, danger-full-access/approval never. Runtime monitor registration
unavailable to this threadless initiative, so active-parent fallback applies.
Batch includes CI 42532231977 attempt 1 plus package/workspace/config builds and
local host/recovery VMs. No machine claim until successful verification.

Final batch completed: configuration/profile/workspace/host all exit 0;
CI 42532231977 attempt 1 failed creation. Runtime host tests both passed, including
recovery boot (343.93 s). CI fast passed (18m39s), archive passed (12m40s),
creation failed after 41m. Watcher's reported 4h40m elapsed is incorrect; wall
clock evidence is 22:52 to 23:32 UTC, about 40 minutes. All owned processes exited.
Failure logs show native -32600 no active turn to steer, then prepared-action
mismatch on same-ID retry. Design brief records fixture isolation fix. No live
activation or claims. Do not rerun without fixing setup and reviewing the change.

Follow-up independent review: [review-fixture-nov9.md](review-fixture-nov9.md),
same gpt-6.1-sol/xhigh reviewer, no findings. Runtime has four logical commits;
fixture isolation is separate baseline-test correction, with no new migrations.
Regenerated pins each remain one final commit. Semantic lock comparison shows
only intended runtime nodes changed; extension/native/sibling/follows unchanged.
Deployment checker passed and comparisons recaptured. New CI 42536185097 attempt 1
is exact d2cb9975. verify-nov9.sh builds final profile/configuration, runs workspace
checks and host/recovery checks while monitoring CI. Previous host results remain
valid for their old artifact only; the package src identity changed with fixture.
No live deployment, claims or merges yet. Fresh watcher 01a1bd89-7fdf-7723-8368-9448a2d16983
launched 23:40 UTC, session 63878; expected about 40 minutes based on prior CI.

Deployment verified: dry/system/profile commands all exited 0. Live system and
system profile xwldgxz; application 8p7fs26. Both HTTP endpoints returned 200;
ephemeral naming succeeded and cleaned up. Portal PID 4101945; native Codex
1309145 and tmux 1917 unchanged. Maintenance status none and no portal error
journal entries after activation. No test messages to original incident session.

Final pre-merge series check: runtime d2cb9975 has four independently reviewed
logical commits, including separate baseline fixture cleanup. Direct schema-3
migration unchanged. Workspace and configuration each have one final generated
pin stream, both selecting d2cb9975 with identical content hash; no intermediate
pins retained. Checker and diff whitespace pass. Full-review and fixture-review
conclusions remain applicable; no additional migrations or runtime edits.

Shared master advanced by tracking-only 2d45c4df2. Workspace rebase 69c816579 ->
6e7d4514879d5e5d4c81f6da95c56105edf9c75a is clean and exact patch-equivalent
(workspace-rebase-nov9.diff). Final package derivation is exactly the deployed
/nix/store/ks9kg3a1lrs97sk4q6afl4hwlpgn5v1h-dev-workspace-0.2.0.drv,
so prior successful build/verification applies to the identical artifact and
inputs. The added tracking content is excluded from this package. Published new
feature ref and comparison captured. Existing explicit deploy-verify-merge
authorization is preserved; no default-branch content has entered yet.

## Completion evidence

All remote masters freshly proved their exact feature heads after ordinary
fast-forward merges and SSH pushes. Shared workspace's unrelated logical index
entries/flags were byte-for-byte equal as projected by git ls-files --stage -v
before/after integration. The extra shared tracking commit was preserved.
Repository claims 80542384, 095d048f and b886258e released after each remote proof.
Machine 8a1702ee released at 00:24:57 UTC after deployed lineage integration;
normal API returned revision 2 / released. Original waiting claim remains canceled.
No source/target mutation remains running. Clean disposable merge worktrees were
removed; registered feature worktrees and refs remain. A new master CI run may
repeat the same exact head; successful exact-head CI plus local host checks already
cover its derivations and inputs, so no duplicate verification wait is required.
