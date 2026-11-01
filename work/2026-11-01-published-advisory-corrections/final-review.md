# Expanded independent final review

Review completed for the exact committed ranges below. This is a new final review of the expanded deliverable; the earlier paused review supplies no clearance. The submitted modern UI has three Important findings and one Advisory. No Blocking finding was established. Important findings require the accepted fixes and focused verification before proceeding under the mandatory-review policy.

## Findings

### Important R1 — Node editing pairs stale child values with a current revision

Repository/commit: vpsadmin-webui, b02c922a2c11ff9f3296cf01b48df07387b7fa6e.

Files: src/pages/app/admin/security/useSecurityAdvisoryNodeSnapshot.ts:44-64; src/pages/app/admin/security/SecurityAdvisoryNodesPanel.tsx:89-97; AdminSecurityAdvisoryDetailPage.tsx:132-142 and 327-333.

capture() obtains a coherent fresh snapshot and checks its guards against props.advisory. openEditor() discards the returned snapshot and initializes the row identity, state, timestamps and original values from the earlier status prop. Parent and status queries refresh independently, and the panel's loading condition uses initial-loading state. A parent refresh can therefore expose revision N while the table still has child values from N-1. The guard comparison succeeds at N; a note-only save then writes the old state/times with revision N and overwrites the newer assessment instead of detecting a conflict. Cached/revisited detail data and ordinary post-mutation refetches can produce this ordering.

Initialize the editor and its original row from the returned coherent snapshot, matching the clicked row identity; reject missing/replaced rows rather than changing the target silently. Add a rendered regression with fresh parent props and stale child props, including preserved other-language notes. The lead accepted and delegated this narrow fix. Reported owner test passes are not independent verification of a new final head by this reviewer.

### Important R2 — Original-editor snapshot can restore an obsolete publication time through announcements

Repository/commit: vpsadmin-webui, b02c922a2c11ff9f3296cf01b48df07387b7fa6e.

Files: src/pages/app/admin/security/AdminSecurityAdvisoryDetailPage.tsx:382-389; SecurityAdvisoryDetailDialogs.tsx:186-190; useSecurityAdvisoryCorrections.ts:89-95. The existing SecurityAdvisoryUpdateModal.tsx:76-94 shows the consuming payload behavior.

The captured original-editor advisory/CVEs are passed to the entire DetailDialogs component, and the snapshot persists after save or cancel. The separate update composer consequently receives that old advisory.published_at. Example: open the original at T1, correct its publication time to T2, then post an update without touching its date. The original editor closes and detail refreshes, but the update composer initializes originalPublishedAt=T1 and explicitly sends T1 in its unchanged-date announcement payload. The API accepts it, undoing the correction.

Scope captured advisory/CVE props to the original editor; other dialogs must use their live current data. Preserve the failed original editor's snapshot rather than rebasing it. Add a rendered original-T1-to-T2-then-announcement regression. The lead accepted and delegated this narrow fix; no remediation head was reviewed here.

### Important R3 — Existing main browser scenario still asserts published editing is absent

Repository/commit: vpsadmin-webui, b02c922a2c11ff9f3296cf01b48df07387b7fa6e.

File: e2e/specs/app/security_advisories_admin.spec.ts:296.

After successful publication the scenario requires admin.security_advisory.edit to have count zero. The expanded canEditSecurityAdvisory() and detail header intentionally render that control in published state. The required admin workflow will fail at this assertion before its announcement/history coverage completes.

Assert that published Edit remains available and draft-only Publish is absent. The lead accepted and delegated this narrow correction. This contradiction is established by source inspection; I did not run the browser suite.

### Advisory A1 — Bulk failure instructions contradict the new stop-and-review behavior

Repository/commit: vpsadmin-webui, b02c922a2c11ff9f3296cf01b48df07387b7fa6e.

Files: src/i18n/locales/en/admin/security_advisories.ts:163-164; cs/admin/security_advisories.ts:162-163; SecurityAdvisoryNodesPanel.tsx:164-165, 437-469.

The partial-failure text still says the operator can safely continue with remaining nodes, while writeBlocked deliberately disables further application after a failed/uncertain request. Replace that instruction with close/reload/review guidance in both languages, preserving completed/remaining counts. The safe runtime behavior should remain. The lead accepted this Advisory and reports directly authoring the bounded copy correction.

No other concrete finding was established in the API, companion client or mechanical KB range. These findings concern the submitted b02c922a source, and remain part of its review record even when subsequent fixes are folded.

## Identity, method and scope

Reviewer: reviewer0, retained review-purpose/read_only member, native thread 01a19801-1fc5-70e3-ba37-8c0952a89392; gpt-6.1-sol/xhigh, codex-lb, no override or fallback. Independent of substantive authorship. Session current printed 2026-11-01-published-advisory-corrections from the intended tracking directory; DEV_SESSION_SLUG and DEV_SESSION_WORKSPACE were both absent, consistent with the trusted thread binding.

Risk: High. Lanes covered directly: general; architecture/repetition; scope/proportionality; risk/compatibility. Read the mandatory-change-review skill and all four lane references, packet, current authoritative expanded/E brief, plan/state/receipts, affected repository guidance and owning code/tests/docs. No nested reviewer or subagent. No source/session-file writes, test suite, build, fetch, integration, production request, deployment or lifecycle action was performed. This text is returned for the lead to persist as final-review.md.

Scope was assessed before detailed hardening. The explicit user additions authorize published CVE/node membership correction, editable/nullable time, retract/delete and matching modern UI work. The complete diff is materially larger than the initial correction, but its mechanisms remain in existing owners: API mutation/locking, two actual UIs, six-action draft-sync compatibility and required exact-source KB verification. Most API growth is focused rollback/concurrency/authorization/cascade coverage; modern growth also includes required docs, typed browser adoption and synthetic captures. The milestone record explains the expanded package, actual CI-diagnosed savepoint/metadata repairs and fresh-main rebase; I did not sum overlapping team working times or infer a stall from elapsed wall time. No additional generalized framework, soft-delete schema, shared transport redesign or speculative hardening is needed for this scope.

## Exact reviewed ranges and complete histories

All worktrees are under /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-01-published-advisory-corrections/.

| Repository / target | Base | Head | Complete series |
| --- | --- | --- | --- |
| vpsadmin / master | 610a96f8ce523afbcd3e4374a70047dbe3264b0d | 218e3180896debd3006b9a0583e557286702761d | 866bccf1a8e1d7f758012cb4d6490c0f3af2cb34; 218e3180896debd3006b9a0583e557286702761d |
| security-advisories / 2026-07-13-security-advisory-automation | 7b6c71807e3c5a41f585fd1d9563e151ada71244 | 0b771120bb2a878c012512b685208124c2b4263b | One commit, the head |
| vpsfree-kb-contracts / master | ce2c8cd9358c3636e5d39343e595df813a0b197f | 21c5213256c28f4a65fd582485e07234a02f5f55 | One commit, the head |
| vpsadmin-webui / main | 63d484fc070dbee633d32624de545e834d483701 | b02c922a2c11ff9f3296cf01b48df07387b7fa6e | One commit, the head |

Actual merge bases equal the supplied bases. Submitted local heads and clean status were checked before remediation began. Review concerns these immutable ranges, not concurrent uncommitted follow-up edits. I inspected complete commit lists/messages and final file/diff inventories: vpsadmin 22 files +1930/-146; client four files +397/-13; KB five files +8/-8; modern 48 files +1681/-605 including six PNGs.

The API and legacy UI commits are separately understandable and contain their supporting tests/docs/locales. The single client commit owns the complete draft-sync compatibility correction. The single modern commit is one advisory-management change with supporting adapters/forms/tests/docs; shared transport/BFF/dependencies remain outside it.

## Whole-branch history, consolidation and migration conclusions

- vpsadmin: the final two-commit series introduces the expanded behavior directly. The original immutable-time/membership restrictions and later savepoint/metadata fixes were folded rather than retained as obsolete implementation/fixup commits. No repeated dependency or pin stream exists. NO MIGRATIONS: no migration/schema/seed paths or transitional database versions occur in this full range.
- security-advisories: the final one-commit series directly guards all six sync mutation types. Earlier two-action-only candidates are evidence refs, not obsolete intermediate commits in this range. No repeated dependency/generated update stream exists. NO MIGRATIONS or persisted-format migrations.
- vpsfree-kb-contracts: exactly one logical vpsadmin pin update is consolidated in one commit. Actual diff changes only flake.nix, the selected vpsadmin lock node, captures.json, contract/navigation.yml and contract/pages.yml. All select 218e3180896debd3006b9a0583e557286702761d; explicit vpsadminos 6bdf458fd9105379860234ff33d352e55844f08f, unrelated nodes/root follows and capture/page provenance remain. No redundant earlier pin is retained in the complete series. NO MIGRATIONS.
- vpsadmin-webui: one final implementation commit over current supplied main; no obsolete implementation/fixup commits, dependency stream or transitional migration. R3 identifies an obsolete restriction assertion still present in final content; that must be fixed even though the commit history itself is consolidated. NO MIGRATIONS, dependency/BFF/transport changes or persisted browser-format transition.

No migration version in these inventories needs merged/released/deployed/externally-consumed lineage retention. Receipts record the superseded feature candidates as unmerged/undeployed; I performed no deployment-state audit. There is no reason to retain redundant update commits in any reviewed stream.

Modern history refresh was examined separately from the final diff: old base f2765d3fd778927f4cda3563f66615bfcf72b7cf / head 73c05d60a25ad914125c0fbf6ab5a71a269c1e11, new base 63d484fc070dbee633d32624de545e834d483701 / rebased candidate 49c4e1626227c9da6a8c68876f157921e7d4ad97 / final b02c922a2c11ff9f3296cf01b48df07387b7fa6e. The saved range-diff shows adjacent documentation/type-inventory context reconciliation. The current diff retains upstream OAuth documentation. Actual 49c4e162-to-b02c922a file inventory changes only factual worklog provenance and three desktop PNGs; application/catalog/e2e/script/type-config source is equal. Final tree is 5779c38ff97ab39765c4beebd46917920d6e63de. This preserves provenance without certifying any future remediation range automatically.

## Correctness, architecture and compatibility assessment

The API remains the authoritative mutation owner. Existing resource authorization stays admin-only and new direct retract/delete actions have separate scopes. Revision/state checks execute after parent reload/lock; scoped children are reread under that lock. Corrections preserve announcement history and do not invoke mail. Publish is draft-only and retains its unchanged-revision contract. Direct retraction increments once and is silent; parent deletion uses existing dependent ownership rather than deleting referenced infrastructure.

The savepoint repair is conventional and addresses the diagnosed outer-transaction rollback failure: mutate_content!, destroy_content!, publish!, rebuild_affected!, announcement creation and child-translation/delete writers use requires_new around the parent lock. Node CRUD refreshes projections inside the edit transaction. Locking reads address stale child/owner/projection snapshots without replacing the existing projection algorithm or changing database isolation. Named tests exercise failures after real intermediate writes. Actual MariaDB execution remains a required next gate, not something source review can certify.

Because advisory children lack SQL FKs, the narrow parent-lock/reload protection on announcement create/translation/delete and outage-link Create is relevant to deletion. Existing dependent relations include plugin outage links; tests check owned cascade, late dependent failure, deleted parent/child races and preservation of users/nodes/VPSes/outages/transaction concerns/mail logs. I found no current writer left unprotected by the new API entry-point contract in the inspected paths.

The client now checks all six used mutation capabilities before applying writes, sends draft state with revision everywhere, preserves publication recovery, and skips only the redundant no-op-parent checkpoint. Real labeled HaveAPI maps are read by machine keys; malformed labels/shapes fail closed, and supported string arrays remain deliberate compatibility. No unsafe retry without guards is introduced.

The modern advisory-specific capability helper uses authenticated root metadata and existing-record lifecycle OPTIONS, leaving shared transport unchanged. Namespaced DELETE serialization has wire tests. Parent/CVE and bulk-node revisions are sequential; unsafe continuation is blocked. The two snapshot findings above are important holes in otherwise appropriate ownership boundaries, not reasons to introduce a generic mutation framework. Legacy forms preserve submitted guards and explicit membership selection; omitted partial POST rows are not implicit deletion.

Upgrade ordering remains consequential: update every active draft-sync consumer and finish API rollout before resuming sync; mixed API pools are unsupported. Earlier two-action clients remain unsafe for newly enabled membership writes. New UIs require compatible API capability for affected writes; old unguarded UI/client versions are not safe write rollback partners. Nullable time, empty relations and retraction fit existing storage; software rollback does not reverse content, and deletion recovery requires backup. No daemon/OS-wide coordinated upgrade is introduced.

Owning behavior/compatibility docs are discoverable in vpsadmin and client docs and modern REQ-055/workflow/API/action/evidence records. Public REQ-054 boundaries remain. KB inventory has no advisory binding or modern-app input; the mechanical pin and strict source check are appropriate without inventing pages/captures. All six synthetic review PNGs were visually inspected; they show implemented editor/delete controls and clear permanent-loss confirmation, not real API acceptance.

## Verification evidence and remaining gates

I performed read-only source/history/diff, consumer, test and documentation inspection; no application test was run by this reviewer. Quick/hook evidence was read from the receipts, including real-metadata client cases and modern pinned quick/focused/capture checks. The six screenshots are synthetic capture-only evidence. Client exact-head CI success is recorded by the lead; no fresh remote/CI acceptance check was executed here.

After accepted findings are resolved and focused evidence recorded, remaining planned checks are meaningful: full/core advisory model/API/concurrency plus outage-plugin cases, the legacy advisory browser scenario, full client suite, strict exact-source KB bin/check, modern full tests/build and affected desktop/mobile mutation browsers and package checks. Preserve first failures and exact tested heads; neither quick checks nor capture-only browser passes prove transaction/cascade/mail behavior.

The lead accepted all three Important fixes and the Advisory during this review. Subsequent remediations were not reviewed as a new head here. Under the skill's narrow-fix rule, direct lead diff inspection and focused regressions can reconcile these prescribed fixes without a broad reviewer rerun solely to confirm them; new design/public-contract expansion would require the affected lanes. Preserve this original range/report and bind the actual final heads/history/checks in the follow-up record.

Session remains open: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-01-published-advisory-corrections/
