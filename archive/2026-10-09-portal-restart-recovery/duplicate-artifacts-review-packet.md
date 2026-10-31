# Final branch review: duplicate artifact availability follow-up

Initiative: 2026-10-09-portal-restart-recovery. Lead owns implementation; no native
lead/roster exists. Previous standalone reviewer /root/review_restart_recovery is
no longer present in the live agent inventory, so its native identity cannot be
validated. Replacement is the installed default lead_reviewed/reviewer,
gpt-6-astra/xhigh/read-only, fresh context, catalog digest
437585347ac8b2cdbf498a169d8871e684f3f61ccf1dd48e8589d79ef9629abd.
Native role name dw_34bb6a768d6175719d13cda28b7adc221b586314b3fc5167.

Risk: high because manifest acceptance is a cross-client persisted-state contract
used by lifecycle operations. General, architecture/repetition, scope/proportionality
and risk/compatibility lanes apply. Read the mandatory skill and each lane reference.

## User outcome and boundaries

The affected session has one artifact declared twice, at manifest lines 77/518.
User chose silent duplicate handling, then explicitly approved the reiterated plan
and requested implementation. Existing tracking must work without cleanup. Every
raw declaration remains validated; duplicate normalized paths are allowed. The
catalog shows the first label/order once. Reads preserve raw manifest arrays and
bytes for lifecycle/journal comparisons. No warning UI, new command, automatic
repair, schema change or native protocol change. Unsafe/malformed entries and
identity/lifecycle ambiguity retain strict validation. See plan.md and design.md
for the complete original recovery and follow-up scope.

## Exact repositories and complete series

All worktrees are beneath
/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-09-portal-restart-recovery/.
All use branch 2026-10-09-portal-restart-recovery.

| Repository | Base | Final head | Complete functional series |
| --- | --- | --- | --- |
| codex-web | 7dab76305dc0084735095d6dbdaef607585d9bca | c9878454f07da244c103b8a79340b92b6d5bf052 | c987845 codex: preserve queued sends across cold thread recovery |
| dev-workspace | 66262519d497073d9bb0dccc2252cdec4528f389 | a756b2c6a3ec30efaf5fd25dccf1717c21a8efa8 | 97ea4c5 sessions: restore portal access with saved work on hold; a756b2c portal: keep sessions usable with repeated artifact links |
| workspace | b73995877adf9e70ad36eef68df06e514c9f6faf | be09a8866026fe1464814a50dd693e96e3d8ca80 | be09a886 workspace: select the session recovery runtime |
| vpsfree-cz-configuration | 1f3569902a4a6b02633019cd172eade5afe90005 | 875420e068aafb6fed9f7067a1cd3e8100ef5ef7 | 875420e0 inputs: set devWorkspace to a756b2c6 |

Fetches confirm default branches unchanged except workspace origin/master now
b7399587 (already the reviewed feature base). Inventory each complete base-to-head
list and final diff directly. Original recovery assessment/remediation is in
review.md; previous complete inventory is in review-packet.md. The original code
contracts were deployed at runtime97ea4c56/provider c9878454, and remain supported.
The new a756b2c commit is a separate bounded behavior change, not a superseded
recovery implementation. Preserve the deployed code source and its existing state
support. Tests/docs are bundled with the behavior they verify/explain.

Workspace runtime override and configuration dev-workspace/devWorkspace channel
updates are each consolidated into one final pin commit. Superseded composition
4f4060ab/configuration f715299c were deployed; provenance stays in rollout.md.
No supported consumer needs a separate superseded pin commit: runtime97ea4c56 is
retained as an ancestor, profile/system packages are immutable store outputs,
and normal rollback already refuses older packages. Extension0ff827df remains
unchanged. Assess this consolidation independently and give an explicit whole-
branch history/repeated-update conclusion.

No database migrations. Original private recovery schema1 and existing submission
ledger schema3 path import were deployed at97ea4c56, not at intermediate revisions.
No new state schema, conversion, migration or compatibility path is introduced.
The updated validators accept additional equivalent declarations while preserving
formats; older readers still reject duplicates. All supported stable commands
select the installed package under existing generation locks. No mixed-parser
workaround or previous-binary invocation is introduced.

## Owning contract and consumers

Generic dev-workspace owns manifest validation and artifact catalog. Go session
loader validates each raw entry and every identity/lifecycle field. AvailableArtifacts
supplies page rendering, details/count refresh and artifact access. Ruby
load_portal_manifest/validate_portal_manifest! supplies CLI and archive/auto-archive
readiness/projections; write_portal_manifest still validates before atomic save.
workspace-host reads identity metadata and does not reject artifact duplicates.
Workspace composition and configuration pin this exact runtime; codex-web is
unchanged by this follow-up. Trusted host operator boundary is unchanged; no
filesystem checks against a compromised local operator are added.

## Documentation and evidence

Generic docs/workspace-portal.md describes supported duplicate handling, first
label/order and read-only validation. Original recovery deployment/forward-only
constraints remain there. Individual rollout evidence stays in rollout.md; the
follow-up record is duplicate-artifacts-rollout.md, prepared only. No foreign
session records or native threads were edited during investigation/implementation.

Quick checks passed: all Go session tests; new live-server duplicate insertion
regression and shared positive/negative fixtures; all Go packages compile; Ruby
canonical test/dev_session_test.rb selection (4 runs/58 assertions/0 failures/
0 errors); Ruby syntax; Go formatting and diff whitespace. Configuration hooks
are installed and passed; generated changelog lists only66262519->a756b2c6.
Deployment pin contract passes for a756b2c6.

Two first quick invocations failed in test setup/assertion: the HTML label appears
both in attribute/text, so the corrected test counts the path attribute; direct
tracking_test.rb lacks the canonical runner's shared NullTmux fixtures, so the
canonical Ruby entry point is now used. Both have passed after correction.

No long checks for the follow-up started yet. Planned: generic/composed package
suites, browser suite, exact runtime CI, configuration build. Existing private
native and VM boot evidence from original rollout stays valid for unchanged
native/boot contracts; no repeated native or VM reboot campaign is planned.
The new HTTP regression proves live same-server manifest insertion with a fake
Codex backend; separate browser suite checks the frontend. No claim of one full
native end-to-end duplicate insertion fixture. Deployed verification will prove
the real affected page loads while its manifest bytes remain unchanged.

Require findings by severity/lane and explicit complete-history, repeated-pin and
migration conclusions. Do not edit source, tracking, deploy, rerun long checks
or delegate. Use focused read-only checks as needed.
