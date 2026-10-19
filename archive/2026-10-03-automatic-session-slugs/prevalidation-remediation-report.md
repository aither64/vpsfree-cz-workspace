Team assignment from implementer0 to lead:

R1 upload prevalidation correction complete; three owned source paths frozen for parent formatting/checks.

Identity: dev-session current from the bound initiative prints 2026-10-03-automatic-session-slugs; both DEV_SESSION identity variables absent and trusted binding matches. Retained settings/access unchanged. Read workspace AGENTS, required projects/sessions/lifecycle/documentation/verification procedures, runtime AGENTS and documentation skill; read full final-readiness-review.md including R1. No Git, Nix, formatting, tests, native/model/process-service, hooks, pins, tracking/docs, deployment or lifecycle changes performed.

Changed paths (runtime worktree):
1. portal/internal/uploads/store.go
   ValidatePreparation evaluates the SAME preparePreparation/prepareSubmission helper on a disposable catalog value with maps.Clone of Files and Submissions. Scopes remain read-only under that helper. These are the only maps it mutates: pending insertion and file Updated assignment cannot reach the live catalog which transaction may save for compaction. ClaimPreparation and transaction/compaction/durability behavior are unchanged.
2. portal/internal/uploads/preparation_test.go
   New TestPreparationUploadValidationCompactionDoesNotClaim: actual unused draft ages eight days; no intervening transaction before validation. Direct catalog read proves the expired scope was compacted and persisted, no submissions installed, selected Updated unchanged and selected bytes intact. Actual Create/Append/Complete/Delete and ready Complete replay remain usable. Then ClaimPreparation installs exactly one pending owner with exact request/scope/text/files/wire and updated timestamp. Same-ID validation/claim replay succeeds; changed raw text, competing validation/claim and selected-file deletion conflict.
3. portal/internal/web/preparation_test.go
   New TestSessionPreparationPreIntentFailureDoesNotClaimUploads: real nonempty ready file plus expired unrelated draft; existing preparationSync seam fails the operation-store directory sync BEFORE temporary record write/rename. Proves that point was reached exactly once, response remains conflict with no redirect, no record on disk/in memory/pending dispatch/naming, unrelated compaction persisted, no upload submission exists, selected bytes unchanged, scope Create and selected Delete remain available. No new production fault hook.

Original-code failure reasoning (not executed here): unrelated compaction sets compacted=true, and the old mutating validation inserts a pending submission into the live catalog. Both new tests then fail their zero-submission assertions; upload test would also find changed Updated and refuse scope mutation. Parent's planned original-production overlay can establish executed red/green evidence. Existing replay/durability/collector tests unchanged.

Exact new-only quick selector, two top-level cases across owning packages, from runtime worktree:
nix develop /tmp/automatic-session-slugs-runtime-env -c env TMPDIR=/tmp GOWORK=off go -C portal test -mod=readonly -race ./internal/uploads ./internal/web -run '^Test(PreparationUploadValidationCompactionDoesNotClaim|SessionPreparationPreIntentFailureDoesNotClaimUploads)$' -count=1 -json

Focused owning regression selector, six upload groups plus three web groups:
nix develop /tmp/automatic-session-slugs-runtime-env -c env TMPDIR=/tmp GOWORK=off go -C portal test -mod=readonly -race ./internal/uploads ./internal/web -run '^Test(PreparationUpload.*|SessionPreparationPreIntentFailureDoesNotClaimUploads|SessionPreparationUploadAdmissionIntentRecoveryAndReplay|SessionPreparationAcceptingUploadConfirmationRetainsBeforeCollection)$' -count=1 -json

Source SHA256 before parent formatting:
store.go dbb38471db4730270c3ce7ca405df738603ac0c71c285defb03651fef83a5bf3
uploads/preparation_test.go c33c6129e5b2e1bcf5c3b886d2e7ded180b399e5c914493ca450395ebf2a2139
web/preparation_test.go e259622ed8794a25d3eb16c265e34c3d85a775b84805b31cb0c6be316c0f5f4d

No new migration/API/policy/catalog fields, dependencies or framework. Existing ownership, ready-file/path/size/limits, claim replay confirmation and continuous pending retention still use unchanged code. No test or old-source reproduction pass claimed; formatting/overlay/quick checks and history status remain parent-owned. Owning docs already state intent-before-claim; nearby comment explains the compaction hazard and why these two maps are copied. No documentation/tracking edit within this source-only assignment.

Frozen; returning idle and available for a specific follow-up. Stable URL: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-03-automatic-session-slugs/
