# Final affected review: node issues filter at 79980b6a

No findings: **0 Blocking, 0 Important, 0 Advisory** in the assigned affected deliverable. No unresolved finding from this review prevents the parent from releasing the planned verification after its disposition. This is source/history review, not browser, packaging, CI, merge or deployment acceptance.

## Identity, instructions and exact scope

Reviewer0 retained its verified same-session review-purpose identity: gpt-6-astra / xhigh / read_only, ready, roster revision61, thread 01a19801-c630-7971-b7b9-cc178b6ced88. dev-session current returned 2026-11-01-typescript-client-migration; both DEV_SESSION_SLUG and DEV_SESSION_WORKSPACE matched that session and /home/aither/workspace/ai/vpsfree.cz. No override, fallback or nested reviewer was used.

I read mandatory-change-review and all four lane references directly, current repository AGENTS and applicable workspace session, Git, verification and documentation guidance. All four lanes were performed directly. Overall branch risk remains HIGH because of the retained bulk-note behavior; the new test-correctness delta is medium risk.

Repository: vpsfreecz/vpsadmin-webui, canonical session worktree.
- Affected range: 91ca5ab44d07d62a8226f5a2b774747a44ff2c0d..79980b6a6607d08cccd252439ced328a250bd5b0.
- Complete follow-up range: 670cf286daf9bddb65594035507ca112a9e6d397..79980b6a6607d08cccd252439ced328a250bd5b0.
- Final tree: 57d045735c136be50bfee0a832a51653692c00ed.
- Actual narrow diff: five paths, +46/-14; full eight-stage diff: 28 paths, +1254/-483.
- Independently observed clean index/worktree, no untracked files or operation markers.

The packet SHA256 matched 62647787aa3d7b7a634371efd96bea1d5e7339c4ea546f2e6291edbbb55c59f7. All linked artifact hashes matched. Actual Git objects, paths and binary diffs matched the supplied inventories. I retained the completed seven-stage review cac25a7f and parent step9 dispositions e1e35462 and 80d950c4 for unchanged source; I also inspected their actual two-file remedy delta. I did not repeat the unrelated original 517-path migration audit.

## General: fixture correctness, assertion reachability and evidence

Owning new commit: 79980b6a6607d08cccd252439ced328a250bd5b0.

The fixture correction in e2e/specs/admin/nodes_issues_only_filter.spec.ts:12–25 matches the actually installed and locked vpsadmin-typescript-client 0.4.0, with haveapi-client 0.32.0 peer:
- dist/generated/resources/node/actions/public_status.d.ts declares name, boolean status and string-or-null maintenance_lock/maintenance_lock_reason.
- Its runtime action declares outputNamespace "nodes"; OverviewList likewise uses "nodes".
- The existing mock helper supplies the status/response envelope but does not infer resource namespaces (e2e/fixtures/haveapi.ts:28,259–274).
- src/lib/api/public.ts:27–45 requires the name/status types and validates string lock fields; :56–60 consumes the generated public-status output.

The explicit public names match inventory domain_name/fqdn. NodesModel.ts:168–232 joins those identities; :260–269 combines the authenticated inventory with public fallback when the explicit overview is empty. Its :280–300,331–332 and existing nodeMaintenance.ts retain status=false as an issue, "lock" as locked, and "no" as unlocked. Thus the corrected data gives the intended down125 / locked124 / healthy123 distinction without bypassing production narrowing or guards.

The applied-state barrier at spec:61–67 is sound for this fixture. It awaits issues=1, then disappearance of the initially observed healthy123 row before positive checks for 125 and124. It therefore cannot satisfy those positive checks solely against the old unfiltered rows in the observed failure. All initial three-row assertions remain at :55–58, the healthy-row negative remains at :65, both issue-row positives remain at :66–67, and clear-filter button availability remains at :69–70. This last assertion proves availability, not execution of the clear action; the patch preserves its original scope. No new casts, sleeps, timeout increases, retries, skips or assertion weakening were introduced.

I inspected the retained original failed trace/context in memory without extraction or download and verified archive/member/trace hashes. The network bodies confirm bare public-status arrays, absent name, object lock and unmatched overview response at old91ca. The failed page reports the missing Nodes namespace and "Showing 0 of 3". The actual event sequence confirms that row125's positive check passed before the later row124 check failed after the filter changed. The healthy-row barrier addresses that concrete ordering flaw; it does not claim to reconstruct the successful retry's uninspected DOM.

I independently matched both retained raw/complete log hashes and their summaries: push41724380477 Chromium has239 passed/1 skipped with no flaky result; PR41724392837 has238 passed/1 flaky/1 skipped. The earlier attribution of the flaky result to the push was incorrect. Neither the green retry nor the old green job set substitutes for executing the corrected fixture.

## Architecture and repetition

The change remains in the existing leaf fixture and its strict membership. The selected generated declaration remains the wire-contract owner; the existing mock envelope and production readers remain unchanged. The explicit empty overview is a small case-local choice to exercise public-status fallback, not a new mock framework, compatibility adapter or alternate reader. I found no new duplicated policy or cross-project ownership issue.

The existing R670-B1 remedy is preserved: member transactions omit privileged fields, admin input/output use declared JSON strings, invented result is removed, and role-specific negative/navigation assertions remain. The request-review opt-out still occurs before opening its correction dialog. Neither earlier remedy introduces a further unreviewed design here.

## Scope and proportionality

The current user outcome is broad failure repair plus PR/all-branch coverage, followed by verification and authorized parent integration. Comparing the actual diff and milestones, this additional leaf correction is supported by a newly observed failed first attempt outside the earlier repair selection. It is a conventional, bounded response: canonical fixture data, reordered assertions, whole-leaf strict adoption and the repository-required small dated log/index update. No new subsystem, production behavior or unrelated campaign appears.

The owning work log at docs/work-log/2026-11-01-typescript-client-migration.md:845 and WORK_LOG.md:1 records cause, remedy, working-input quick results and pending acceptance accurately. The two historical whitespace adjustments in WORK_LOG do not change prose. No new UI copy, locale, KB or screenshot contract is introduced; previous documentation/locale/KB conclusions and captures retain their original unchanged-source scope.

## Risk, compatibility and strict adoption

The complete new leaf is included in tsconfig.e2e.json and scripts/fixtures/e2e-type-coverage.json. I independently verified:
- 152/131 becomes153/130 solely by adopting this leaf.
- sourceRevision remains abab859d94a3f364d2bb719fa09f00749fd69ef9.
- Baseline SHA256 remains 7bdc6a363a2706be14533e05712bda641aa709ce2413a4bd68ebe427ecec3317.
- All130 surviving deferral records retain exact raw bytes and order.
- Compiler options and other configuration content are unchanged; no allowance or baseline refresh was added.

All2595 final tracked blob SHA256 values, object IDs, modes and live bindings matched the evidence. All1370 installed-input hashes matched and equal the working quick snapshot. The only differences between that working snapshot and final inputs are the two subsequently checked documentation files. Quick log hashes and exits match five source commands exit0/16.568s and three documentation commands exit0/3.282s; the retained coverage log says153 checked/130 deferred. These are exact-input reuse, not literal79980 executions. I ran no tests or checks.

All production, API adapter, BFF, shared fixture/helper, guard, SDK/runtime, npm/lock, Nix/hash and backend inputs are unchanged by this eighth commit. Existing authenticated/public isolation, guarded advisory writes, partial recovery/no replay and explicit bulk-note intent remain covered by the retained accepted review; no new deployment ordering or rollback boundary is introduced.

## Complete history, update streams and migrations

I independently matched every raw commit object, parent/tree and pathset against the eight-stage inventory and checked the complete final diff. The seven published91ca objects are literally unchanged ancestors of79980.

1. 9fd6d575 — one compatible broad-workflow action dependency refresh.
2. e615538c — PR/all-branch triggers and owning workflow documentation.
3. 96b02de8 — storage/VPS/DNS/export/focus fixture contracts.
4. d077da52 — infrastructure/outage/action-state fixture contracts, including the accepted role-shaped remedy.
5. 3e2d77ed — request-review/WebAuthn fixtures, including accepted interaction ordering.
6. 5985f173 — nine complete-leaf strict adoptions.
7. 91ca5ab4 — explicit bulk-note language intent with tests/catalogs/contracts.
8. 79980b6a — this independently diagnosed node fixture, its strict adoption and minimal owning log.

The original reviewed ebfd source differs from published91ca only in the two accepted fixture remedies; production changes remain identical. Their fixes were incorporated into their respective owning pre-publication stages. No abandoned implementation, alternate subsystem, obsolete migration or removable fixup chain remains in this complete successor range.

There is repeated coverage-metadata evolution: the ninth-leaf adoption batch at5985 and this newly diagnosed leaf's adoption at79980. It is additive membership, with protected survivor records, rather than competing dependency artifacts. The new leaf/metadata/log have one test-contract purpose. Retaining the ordinary eighth descendant respects repository AGENTS' explicit published-history protection and the assigned no-rewrite boundary for91ca; publication is not being used as a general exemption to retain redundant pin updates.

The action dependency refresh occurs once. There is **no new or repeated generated-client, npm/lock, Nix hash, backend or channel-pin update stream** anywhere in670..79980. Existing selected0.4/runtime0.32 inputs are retained.

**No migrations:** neither the eighth commit nor the complete670..79980 range adds or changes a DB schema, persisted format, migration, seed or upgrade/downgrade path. There is no transitional migration or externally consumed intermediate migration to consolidate. The integrated670 baseline and earlier migration/source history retain their prior conclusions.

## Residual verification limits and disposition

- The corrected native Chromium case, retries0, remains unexecuted at this head. List membership is enumeration only.
- Exact-final79980 Nix5 and current-head required/full broad CI remain pending. Old91ca realizations and CI keep their actual revision/input scope.
- Retained31 product tests, application strict checks and synthetic captures apply only through verified unchanged inputs; they are not new79980 executions.
- Fixture success cannot certify a live API or mixed deployment. The existing guarded backend822/equivalent minimum, preview4ed/API610 limitation and A040 cursor-completeness limit remain unchanged.
- This review provides no merge, configuration integration, deployment or lifecycle acceptance. Parent owns remaining verification, final integration checks and any separately authorized cluster action. I performed no mutation, network, build, browser, API or lifecycle operation; the session remains open.

Parent persistence target: work/2026-11-01-typescript-client-migration/webui-node-issues-79980b6a-final-review-result.md. Full text is delivered here because reviewer access is read_only.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-01-typescript-client-migration/
