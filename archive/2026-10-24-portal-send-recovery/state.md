---
lifecycle: complete
---

# Portal message delivery recovery

Phase: complete. Deployed and verified on aitherdev, all four exact feature
heads merged into remote master after live verification, and all final CI passed.
Machine and repository claims released; temporary merge targets removed.
Session remains open. User authorized implementation and deployment, then:
"when the fix is deployed and verified, you can merge it". This covered the
codex-web, dev-workspace, configuration and workspace feature branches into master.

- [x] Investigate original failure and approve portal-level recovery plan.
- [x] Create a separate tracked initiative without starting a new Codex task.
- [x] Implement client/HTTP delivery handling and focused regressions.
- [x] Implement portal recovery and current composer feedback.
- [x] Commit source, quick checks and independent final review.
- [x] Complete final packaged/native/browser checks and feature CI.
- [x] Compose matching runtime/configuration and deploy aitherdev.
- [x] Verify live continuity/recovery, integrate approved branches and release machine.

The original confctl message was absent from native history, rollout and queue.
Its submission record remained `submitting`; retries only reconciled history.
The banner additionally cleared only for the same attempt ID, so a successful
reworded message left the earlier composer error visible.

Baseline: installed application
`/nix/store/l9sc1ksacdkm7iij99ggyg87bqsp9n15-dev-workspace-0.2.0`;
codex-web `11ec57d2203fc735696fe75a837d47da55a5c6af`, native Codex 0.163.0.
Recheck published defaults and current deployment before composition. Retain
existing caller-cancellation isolation and the deployed retry/UI improvements.

This initiative has no retained team roster. The external lead owns development;
use the installed default review and verification utility policies for final
review and long checks. Preserve unrelated dirty shared-workspace files.

Final clean published feature branches: `2026-10-24-portal-send-recovery`.
All worktrees are beneath `worktrees/2026-10-24-portal-send-recovery/`.

| Repository | Final head | Base |
| --- | --- | --- |
| codex-web | 872c7ad3962f9fa9b17358244e27f3e3fac59fc5 | 11ec57d2203fc735696fe75a837d47da55a5c6af |
| dev-workspace | 10bb047513c82d1310e8fcaa797e8772f948dd8a | b3a6eb2fc0b41cf0cb965bf4c39991815d9df734 |
| vpsfree-cz-configuration | d12a77374b18e15fe7600f95307114e2e1882828 | 25258cd3f483f0116dbab35c7acf89b16eff4bbc |
| workspace | b1b86b2b8a075666ccdef7f9d254047be972508a | c99b4de612993f8c7af9de7dea1d74d89212d539 |

Provider history is one consolidated functional commit; runtime has one
functional commit plus one dependency update. Configuration/workspace each
have one matching final pin update. No migrations. Workspace rebase was patch
equivalent to earlier reviewed head 57f5ec659. Native Codex remains 0.163.0.

Quick checks passed: client send/cancellation/operation-timeout Go selectors;
47 conversation/upload browser contract tests; schema corpus coverage; portal
submission notice and composer handoff contracts; portal response-loss, composer
and notice Go selectors. The first notice regression needed a cross-VM array
comparison correction; the protocol validator needed to recognize the new
admission helper (wire shapes unchanged). Both now pass. No declared hook
framework in either project. The generated vendor tree hash was computed with
the repository Nix Go environment. Long checks await independent final review.

Reviewer policy: no eligible retained lead/roster because this is deliberately
threadless tracking of the external conversation; use the installed default
development team's reviewer, gpt-6.1-sol/xhigh, as a fresh standalone agent.
Verification utility policy gpt-6-luna/low was resolved from installed catalog
digest `840de47527dea8325fcac0c2eb7ca5ae9728b31523ec368bcce595c6f15983fa`;
native utility `dw_b9dd4137280d3e047a81fbdfe0ea73c900c9fd89f8861d12`,
execution access full_access. First quick-check watcher completed successfully.

Initial final review found three Important browser issues (review-report.md):
retained unsent state during composer retry, false unsent guidance after a
storage failure, and stale queue-start feedback. All three are corrected with
focused regressions and folded into the functional commit. A parent audit also
found competing clients could both claim a prepared attempt; admission now
atomically requires prepared state and reconciles if another client won. The
two-client native-wire fixture proves one mutation and accepted-receipt recovery.
The same reviewer assessed that additional boundary (review-followup-report.md)
and requested F1-F3: recheck shared state on cancellation/early refusal, retain
nonzero original options, and adopt positive history atomically rather than
through mutation admission. These direct corrections are committed in provider
`57dd01b1d860181e12aa7ccb37ecdeae8b2c08c5`, with runtime pin
`fac4e6a3d2169dd81d0ae9bb891e7f8ca62114de`. Focused checks pass, including the
cancelled/noncancelled, unknown/already-accepted winner matrix with nonzero
options and two simultaneous history callers. Parent verified the requested
narrow fixes under mandatory-review step 9; no extra boundary or policy was
introduced. Original I1-I3 were independently confirmed resolved in follow-up.
The long-check gate is satisfied with all reported Important findings fixed.

Long verification passed: packaged provider suite, two pinned native recovery
fixtures, generic runtime build, and Chromium/Firefox delivery/composer/recovery
browser tests. See `verification-watcher-result.txt` and its linked logs. Watcher
01a16fa9-dc14-7f20-97ab-7f0fbb9ba62a completed with exit 0.
Provider CI 40130866773 passed at final head. Runtime CI 40131027714 and composed
application build are owned by fresh Luna/low utility
01a16fb4-033f-72f1-977b-2d9620ea5a0c; see composed-watcher files.

Aitherdev configuration build passed at exact feature head (generation
2026-10-24--22-56-18). The first build stopped at confirmation with EOF because
`--yes` followed the selector; putting command options before the selector fixed
it. No activation occurred. Source/provider pins and runtime/config selection
passed deployment-contract checks. No machine claim acquired yet.

Next: collect composed build/CI, acquire aitherdev near activation, dry-activate
and switch system then user profile, verify installed behavior and live continuity,
then integrate approved final heads using individual short repository claims.
Retain machine ownership until verified integrated deployed lineage, then release.

Pre-merge preparation: current upstream source/configuration defaults still equal
the recorded bases. Clean detached target worktrees are prepared beneath
`integration-targets/`. Configuration worktree creation's checkout hook required
its Nix shell; signature is prepared without bypassing hooks. Final series/diff
checks are recorded in `final-series.txt`; all repeated pins consolidated and no
migrations. Saved portal comparisons captured for all four heads. Workspace's
comparison uses locally available origin/master (aadb664); its reviewed feature
range remains 04f92aec1..32f9c8866. A request to overwrite that immutable saved
comparison with another base was safely refused; no comparison state changed.

Static assets are served Cache-Control: no-store; ordinary page reload fetches
the upgraded app. Existing open tabs need reload. Live verification will use the
installed assets with all send requests intercepted, plus real read-only native
thread/portal continuity checks.

Composed application build passed:
`/nix/store/fsp42gfclql2pjm0l8gq77m8qicl4f0z-dev-workspace-0.2.0`
(derivation 18qwmx6wlgac64g57l0wi4fmwb8j3jg6). The watcher script then exited 1
because runtime CI 40131027714 had failed its fast job. Archive and creation VM
jobs passed. Downloaded full failed-job log to runtime-ci-failure.log before
considering a rerun. Only failure: existing
TestRetireThreadPersistedEmptyRootRefusesUnsafeEvidence/cancel expected
context.Canceled but received websocket disconnection. Its server calls cancel
while sending a read-only discovery reply. The unchanged request response select
can receive disconnect evidence before cancellation; this is an existing
cancellation/disconnect ordering race, outside send-admission callbacks.
Neither the retirement fixture nor the response select was changed by this fix;
normal Request uses a nil callback and the same writer/response behavior.
Focused 100 repetitions passed on both final runtime and exact old baseline
b3a6eb2f (old provider 11ec57d), 1.467s and 1.394s respectively. The race did not
reproduce locally; CI's complete log identifies it. Accepting this existing
intermittent diagnostic distinction as unrelated to delivery recovery; request
one failed-job rerun, with no source or test expectation weakening.

Additional baseline diagnosis: 1,000 single-scheduler cancellation-fixture
repetitions passed on old runtime b3a6eb2f in 10.722s; CI timing distinction
remains non-reproduced locally, with unchanged response-selection evidence.
Fresh watcher 01a16fbd-3a4d-7000-98de-0ffc5137dc94 (verified Luna/low,
full_access, approval never) owns attempt 2 CI observation.

Live-browser regression against currently installed old assets reproduced the
user's banner defect exactly: after uncertain original plus simulated reworded
successful response, #message-submission-status remained visible. All API sends
were intercepted; no original-session mutation occurred. Evidence:
live-browser-before.log. Run the same script after selecting the new profile.

Attempt 2 failed the same cancellation/disconnect race. Machine claim
17bc6fd6-64a2-4fa5-83f3-cd13d6339158 was briefly acquired before interpreting
the watcher result, then immediately released with no activation or other effects.
No original artifacts have been deployed. Preserve them only as superseded evidence.

Corrected the error-chain boundary rather than retrying again: requestWithAdmission
retains both existing error and concurrently completed ctx.Err, leaving successful
results, transport/RPC identity and durable delivery classification intact.
Deterministic cancelled/noncancelled admission-failure regression passes, as do
send/shared-ledger/history checks. Existing retirement proof suite passes 10
repetitions at the new pin. Provider 872c7ad3962f9fa9b17358244e27f3e3fac59fc5,
runtime 1b56299642e3cc7abdcc77fb63369a1abaf91412 (pins being refreshed).
Provider CI 40133589406 passed. Runtime CI 40133742300 is running.
The same independent reviewer owns cancellation-review-packet.md, assessing
only added boundary plus final provider history. No migrations; native unchanged.

Final cancellation review has no findings; all prior findings remain resolved.
See cancellation-review-report.md. Final heads/series: final-heads.json.
Mechanical source consumers consistently select provider872c7ad/runtime1b562996;
configuration was regenerated directly from base to preserve the full confctl
changelog in one final pin commit. Obsolete generated pin commits removed.
Workspace remains one final pin commit; native and extension unchanged.
Final verification watcher owns verify-final.sh. No deployment yet.

Final watcher 01a16fca-cbe6-79d3-9191-d6b7ec10dc96 verified as Luna/low,
codex-lb, full_access, approval never; owns verify-final.sh and all inner logs.
Final deployment contract passed at 1b562996. Captured updated portal comparisons.
Integration target configuration restored to upstream baseline after generating
the single consolidated pin; required checkout hooks passed in Nix shell.
Prepared integrate-reviewed.py requires live-verification-passed.json and exact
clean reviewed heads, acquires/rechecks one repository at a time, fast-forwards,
pushes over SSH, verifies remote equality, and releases. Shared master also takes
the nonblocking tracking lock. Prepared read-only verify-live.py checks exact
asset bytes, system/profile identities, original thread continuity and unchanged
Codex/tmux PIDs. Neither deployment nor integration scripts have run.

Final batch stopped at composer_handoff_browser_test line224: after reload no
new message request reached the peer; zero page errors. New delivery/recovery
browser regressions passed. Full provider package/native and runtime build passed
at provider872c7ad/runtime1b562996. Runtime CI fast+archive passed; creation still
running at supersession. Its exact old-head run was cancelled after publishing
replacement10bb0475 under the force-push policy.

Diagnosis found a real startup gap: server HTML enabled Send before app.js had
loaded conversation.js and registered submit listeners. The last fixture reload
could click native form before JavaScript admission; its upload controls appeared
only after the click. Fix initial Send disabled, with existing action state update
enabling it once handlers are installed. Added a delayed-conversation-asset check
to the message browser regression. Folded into functional2c847e6d, dependency
head10bb047513c82d1310e8fcaa797e8772f948dd8a. Focused Composer/SubmissionNotice/
Conversation Go checks pass. Same reviewer owns startup-review-packet.md.
No provider change, migrations, native update or deployment.

Shared workspace advanced only through other sessions' tracking. Rebased our
single pin onto shared master; range-diff proves identical patch before updating
the selected runtime. See workspace-tracking-rebase-range-diff.txt.

Startup review passed with no findings: startup-review-report.md. Reviewer
confirmed initial disabled state, same-stack handler ordering and delayed-asset
regression. Provider remains872c7ad with exact package/native passes; runtime
now10bb0475, configurationd12a7737, workspaceb1b86b2b. Final exact heads in
final-heads.json. Captured updated comparisons. Candidate watcher owns only
remaining affected runtime/browser/composition/system checks and CI40134903928;
no repeat of unchanged provider/native checks. No deployment yet.

Candidate verification watcher01a16fd9-aa4c-7a81-a4f8-b8cf654d7b6f validated
Luna/low/full_access/never. It owns verify-rollout-candidate.sh and inner logs.
Parent has not polled its inner checks or changed candidate sources while running.
Machine remains unclaimed; all prior briefly held ownership was released before
any activation. Activation must use claim-vpsfree-aitherdev-final.json with a
fresh request UUID. Collect candidate-watcher-result.txt before acting.

Candidate browser, generic/runtime/composed builds and exact system generation
2026-10-24--23-56-19 passed. Runtime CI40134903928 fast and archive passed.
Creation VM failed naming-collision at new-session admission with
`session is changing: resource temporarily unavailable`, before conversation
submission. Full failed logs saved candidate-ci-failure.log/json. This is the
existing nonblocking LockRuntimeExclusive in creation.go/installCreationLocked,
implemented by session/authority.go's Flock without context; neither source,
naming/creation fixture, nor creation path changed. Last source delta after
previous VM creation successes was initial existing-conversation Send disabled.
The new-session form is a separate template/control. This failure is unrelated
to delivery and is accepted as a pre-existing transient lock refusal for this
rollout; rerun failed VM once after diagnosis. Applicable delivery verification,
review, package/native/browser and host preparation gates passed. Proceed with
authorized activation while independent unchanged creation VM reruns. Retain
full evidence, do not weaken tests or change creation locking in this task.

DEPLOYED AND VERIFIED. System activation exit0 with two passing health checks;
profile activation exit0 selected8ph05i3nps8xi1jfs450b16aysc16nvg. Live asset bytes
match reviewed app.js and conversation.js, original confctl thread/latest turn
unchanged, native PID3387667 and tmux PID435397 unchanged. Portal/router/coordinator
active. Installed Chromium/Firefox check passes banner clearing, per-message
unknown retention, replacement and known-unsent reload. All submissions intercepted.
First live browser wrapper had an invalid models:{} stub; corrected test to[];
no production source change. Evidence live-verification-passed.json,live-after.json,
live-browser-after-corrected.log. User's conditional merge direction now applies.

Final pre-merge history: providerone functional872c7ad; runtimetwo commits
2c847e6d+10bb0475; configone generatedd12a7737; workspaceone pinb1b86b2b on
tracking-only c99b4de61. No repeated update streams, obsolete fixups or migrations.
All heads/series match accepted reviews and final mechanical pin inspection.
Fresh upstream source/config targets still recorded bases. Begin individual
short claimed fast-forward integrations; keep machine until full deployed lineage
integrated. Independent pre-existing creation-lock VM rerun still monitored.

Provider872c7ad and runtime10bb0475 integrated into exact remote master heads.
Their individual repository claims released after remote proof. Configuration
merge acquisition briefly waiting during coordination collection; no Git mutation
occurred. Resume the same request296cd7db-5c02-42be-b419-be91c37c5fe0 after
claim-status proves held. Machinefaea8db4 remains held while lineage integration.

All four exact final heads merged into their remote master branches after live
verification. See merge-*.log and integrated-lineage.json. Unchanged extension
767dfd58 also matches remote master. No deployed-history replacement needed:
all deployed exact SHAs are literally integrated. Shared master remains selected,
unrelated dirty files and index preserved. Each repository claim released after
remote proof. Machinefaea8db4 released after final live/profile and lineage checks.
No unfinished/uncertain deployment effects remain. Branches/source worktrees
retained. CI watcher still owns creation retry40134903928/attempt2; post-merge
runtime40137122653 at identical10bb0475 also running. Provider masterCI40137101265
passed. Initiative stays active until monitoring/temporary-target cleanup finishes.

Creation CI retry40134903928/attempt2 passed at exact final10bb0475. Earlier
failure was investigated and retained as documented lock-contention evidence,
not erased by the rerun. Post-merge40137122653 fast/archive/host passed; creation
still running. Fresh operation-scoped watcher owns only that existing run.
Temporary integration-target checkouts removed cleanly. All source worktrees
and feature refs retained. No active own resource claims remain.

FINAL: post-merge runtime CI40137122653 passed all four jobs (fast, creation,
archive, host). Feature40134903928 attempt2 also passed. Provider final/master
CI40133589406/40137101265 passed. Postmerge watcher01a17001-4a08-71f1-af73-
2acbd8e52bd4 initially retried a transient model-account connection failure,
then recovered under verified Luna/low/full_access/never and completed normally.
A brief parent read-only CI observer also exited0; no duplicate builds or CI runs
were launched. Evidence postmerge-watcher-result.txt/postmerge-ci.json.
All verification processes finished. No unresolved review, CI, deployment,
integration, approval or temporary-target cleanup remains. All exact feature
heads are integrated; machine release and absence of own held/waiting claims
verified. The initiative is complete without archival/deletion; source worktrees,
feature branches and compact evidence remain available for follow-up.
