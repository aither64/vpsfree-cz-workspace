# Independent review

Pass1 completed on providerca0f3bc9/runtimeedcfc18/extensionc8f9ba36/workspace421edddb.
All four high-risk lanes, retained independent reviewer0, actualgpt-6.1-sol/xhigh,
read-only, no fallback. Two Important findings, no Blocking or Advisory findings.
Coordinator decision: fix both before integration; no risk acceptance or deployment.
The coordinator accepted the architect's bounded remediation supplement.
Implementer0 is preparing the runtime fixes; the published heads remain the
initial review snapshot.

## Findings to resolve

- R1: published accepting/running writes can leave an attempt without a worker
  after directory-sync failure. Preserve exact identity and ensure one worker;
  prove same-process initial-admission and retry recovery with focused faults.
- R2: stale-catalog rejection before admission permanently freezes the browser
  draft. The accepted repair retains recovery of the original immutable request
  and offers a separate request in a new tab without an opener. It requires
  deliberate text copying and file reattachment, preserves the original attempt
  and makes no claim that an HTTP error or 404 proves non-admission.

History, commit splits and migration lineage passed. No obsolete unapplied
approach or transitional migration remains; original consumed4ef/399 lineage
retained. No database or incoming namespace migrations. Actual binary isolation,
real browser/race/old-source/package checks and deployment remain pending.

## Independent report

Independent final whole-branch mandatory review complete for 2026-10-03-automatic-session-slugs.

Reviewer: retained reviewer0, purpose review, read_only, saved gpt-6.1-sol/xhigh, unchanged; independent of implementation, no fallback or nested reviewers. Verified dev-session current against the trusted thread binding; both environment identity variables absent. Read workspace/repository instructions, all routed procedures, documentation placement rules, mandatory review skill and all four references. Reviewed general, architecture/repetition, scope/proportionality and risk/compatibility directly at high overall risk. No writes, commits, refs, pins, lifecycle operations, deployments, merges, actual Codex/browser/VM launches, or full test launches.

Decision: two Important findings require fixes or explicit reconciliation before calling the candidate ready. No additional Blocking or Advisory findings identified. This is not a claim of release readiness or real-binary isolation.

1. Important — general + risk/compatibility — a published running preparation can permanently lose its worker.
Commit: dev-workspace 991fdec12e2b21e12db7894310d971a814f0931c.
Primary location: portal/internal/web/preparation_store.go:371-375.
Related: preparation.go:298-301, 318-332, 548-568, 597-650.
Evidence: savePreparation publishes the renamed record into s.preparations before the final directory sync, then returns that sync error. During admission, finishAcceptingPreparationLocked has already changed state to running. The caller launches only if save returns nil. A post-rename sync error therefore leaves a running record with no worker. Same-ID POST repairs only accepting records; the retry endpoint returns 202 immediately for running records. Periodic reconciliation does not repair a running record without a handoff. With an ordinary request without attachments, this remains running indefinitely until restart and consumes unfinished capacity. The same gap exists when retry saves running before launch. This is a source-established failure; I did not inject a filesystem error or claim data loss.
Required action: make a published-but-unlaunched attempt recoverable in the same process while retaining the exact request/receipt identity and ensuring one worker owns each attempt. Add focused post-rename directory-sync fault tests for initial admission and retry, asserting recovery without a portal restart, duplicate workers, or another receipt. Existing restart/crash-gap tests do not exercise this same-process outcome. Do not solve it by removing the admitted identity or blindly launching under uncertain ownership.

2. Important — general — terminal admission rejection permanently locks the new-session form.
Commit: dev-workspace edcfc18f2fdc3bdebfec7089e2bd79b2d9b918b1.
Primary location: portal/internal/web/static/preparation.js:96-114 and 128-145.
Related: static/app.js:1358-1369; preparation.go:193-195 and 277-295.
Evidence: the browser freezes/persists the body before the first POST and retains it on every non-2xx response. The server rejects a stale catalog before saving an admission intent. A page/draft kept across a team-catalog change can therefore get “catalog digest is stale; reload the form”, then GET 404. Recovery reposts the exact stale digest forever. Reload retains that attempted body; update throws and form inputs/attachments/submit remain locked. There is no affordance to correct the team selection or preserve the content in a new request in that tab.
I reproduced the shipped helper's behavior with a pure in-memory Node/storage/fetch harness: first POST 409, recovery GET 404 followed by the same POST 409, then update rejected with “Recover the saved request before starting another session.” No browser or server was launched.
Required action: provide a controlled recovery path for proven non-admission so the user can correct the request without losing its text/files, while preserving locked identity for ambiguous lost replies. Add regression coverage distinguishing a stale-catalog first-submit rejection from an admitted/uncertain request. HTTP failure or GET 404 alone must not become a blanket permission to discard an identity, because an admitted intent may be uncertain. Keep the fix bounded to that distinction rather than introducing a general cancellation framework.

Review scope and independent evidence:
- Inspected actual complete base-to-head commit series, final source and relevant old-source context, not only the packet summaries.
- Reviewed all 18 commits in the four complete remote-default-to-head histories, including preserved deployed/unmerged ancestry and inherited shared-master coordination commits. Also assessed each incoming feature diff separately.
- Compared every supplied final.diff and incoming.diff byte-for-byte against actual git diff: all matched.
- Confirmed final heads and clean worktree/index status at the end of review:
  codex-web ca0f3bc980ca99454d000761aeee37b4b9bbafc3;
  dev-workspace edcfc18f2fdc3bdebfec7089e2bd79b2d9b918b1;
  vpsfree-dev-workspace c8f9ba36bbb0b346d2165229690015193ca97ac0;
  workspace 421edddb5efd0bce6a36f8acedef1cf6082c75ef.
- Independently compared whole lock nodes against incoming baselines. Runtime changes only codex-web; extension changes only codex-web/dev-workspace; workspace changes only codex-web/dev-workspace/vpsfree-dev-workspace. Exact revisions match those heads; unrelated source/provider/team/site/cluster nodes remain equal.
- Full runtime-contract JSON is byte-identical to deployed runtime4ef298b3.
- Reviewed utility framing, config/model admission, private pre-admission sink, generation and turn ownership, bounded cleanup, request-ID persistence, upload ownership/retention, receipt handoff, CLI reservation checks, browser storage identity/navigation, package policy installation and verification fixture code.
- The accepted user boundary is action-tool isolation with immediate question rejection and pure clock allowed, using unchanged Codex0.160.0 and a trusted local operator. Code/docs respect that stated scope; no zero-tool claim is warranted. I found no concrete supported failure requiring a hostile-local-operator race framework or removing the static instruction-file link-count validation.
- New preparation persistence and the existing receipt workflow serve distinct ownership stages. Their necessary checks are proportionate to crash recovery and compatibility. I found no further architecture/repetition or scope issue supported by a concrete failure/maintenance scenario.

Explicit whole-branch history conclusion:
The complete reviewed histories contain no remaining obsolete unapplied approach, unused temporary compatibility path, or superseded follow-up commit requiring consolidation. The former unpublished backend version8c0d3fc and dependency/browser/fixup versions07a98d0/51dca869/f1f1c39 are absent from the final series. Their final replacements are represented coherently in the owning commits.
Preserved runtime4ef298b30f9cdbdcfe02bf6526e0f69ecc9bf7b4 and the four extension ancestors5b2e9a4,101d3126,f50c92bf,399c3302 are deployed/published externally consumed lineage, not obsolete feature experiments. Their original identities remain. The workspace's five inherited shared-master coordination commits are ordinary ancestry, including other initiatives' records, not extra functional scope for this feature.
Commit splits are coherent: one additive helper capability; five incoming runtime units covering uploads, persistence/CLI handoff, naming adapter, dependency/policy installation and browser flow; then extension and workspace exact consumer pins. The preserved maintenance/storage/test units also remain coherent. Finding fixes will change the candidate and require a new exact-head review packet/rerun under the mandatory workflow.

Explicit migration/provenance conclusion:
No database migration files or namespace conversion migrations are introduced by the incoming feature in any of the four repositories, and no transitional unapplied migrations remain. Preparation schema1 and compact mappings are introduced directly; there is no abandoned schema migration to preserve. Receipt1/2/3, upload catalog1, existing authority/journal/manifest readers remain supported.
The complete extension ancestry does include already-consumed storage-profile bootstrap and preserving seed behavior; that is not a new automatic-slug migration. Runtime's inherited cluster policy2-to3 transition and extension's maintenance/storage lineage are already deployed, preserve authority schema1 and must retain their provenance. The migration lineage is sound on the inspected source and packet provenance; I made no independent deployment execution claim.
I agree with the source-based conclusion that this incoming feature creates no new extension host-migration VM trigger: the migration path preserves generic private trees and the incoming change does not alter namespace, rewrite inventory, host paths or the authority contract. Normal migration/host-path checks remain necessary. This does not establish an arbitrary-root relocation guarantee or executed VM evidence.
Forward-only recovery through a newer package retaining the readers is consistent with the documented package-generation contract.

Residual verification/release gates:
- Reconcile R1/R2 and add the focused regressions above; refresh exact heads/diffs and rerun the independent review for changed code.
- Parent still owns complete packaged checks, race regressions, real Playwright, exact old-source upload/CLI fixture, assembled candidate validation and canaries.
- Exact unchanged candidate Codex binary/model proof remains required before enabling model naming: actual tool schema/dispatch, local instruction/hooks/MCP sentinels, clock/question behavior, active-provider cancellation after response loss, and no persisted thread/turn/goal/memory artifacts. Mocks, schema/corpus validation, tagged compilation running zero tests, and normal mock CI do not prove this boundary. I inspected the fixture/source but did not run that proof.
- Exhaustive write/fsync fault coverage is not claimed; the specific missing case in R1 is actionable.
- No deployment, default-branch integration or lifecycle action is approved by this report. Parent records review.md and owns fixes/checks/operations.

Stable session URL: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-03-automatic-session-slugs/

Current phase: independent final review complete with findings. Completed: four lanes, complete history/final diff/provenance assessment, exact-pin checks. Remaining: R1/R2 reconciliation, new exact-head review and release gates. Material risks: recovery stalls and unproven actual-binary isolation. Next action: parent implements/reconciles findings. I remain available and idle with this session open.
