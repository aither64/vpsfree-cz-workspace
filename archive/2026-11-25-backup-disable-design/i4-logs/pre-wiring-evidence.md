# I4 D3 correction checkpoint

Status: **parked on corrected I3 generated SDK; package incomplete**. Implementer3
retains adapter/page/browser/review-fix ownership. The old D2 record below is
historical evidence, not current product behavior or a readiness claim.

- Repository/worktree/branch remain `vpsadmin-webui`,
  `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-25-backup-disable-design/vpsadmin-webui`,
  `dev/disable-backups`.
- Unchanged base: `e311b1c0af0f50fa4c6f6ce83c514c1a866eb042`.
- Prior D2 head: `b144054198c467b4e4a25a9d1521973a673a77ec`.
- Initial D3 correction head: `e1bf4004668dd6bf1b430bd43297693c14926adc`.
- Current D3 head including lead copy clarification: `8a241695ead4bda8753dc537c98f5def34ac3073`.
- The sole unpublished preparation commit was amended as explicitly directed.
  Current complete series is one commit, `8a241695 storage: prepare administrator backup cleanup`.
- Current base-to-head diff: 15 files, +556/-4. The D2 version was 17 files,
  +969/-5. The final tree contains neither D2 workflow file nor phase/continuation
  adapter/test/catalog behavior. This is a substantive correction, not a
  patch-equivalent rebase; eventual independent review must inspect D3 in full.
- Worktree clean after amendment. No branch push, PR, CI, release, integration,
  deployment or lifecycle effects occurred. No command remains running.

## Corrected scope and dependency

The prepared shared control submits one ordinary mutation with only recursive
and backup-first options, then uses the existing task controller and durable
request-generation binding. Normal preflight, duplicate-submit prevention,
known-rejection retry and unknown-outcome reconciliation remain. Accepted work
continues after browser exit; there is no cancellation or continuation controller.
The actual administrator role and permission-filtered action/input discovery gate
cleanup. Planless entry, default-on option, target/recursive/loss/no-new-snapshot
facts, existing VPS plans link and both ordinary plan-removal explanations remain.
Final D3 lead-owned copy is mapped; no extra task UI was added merely to consume
unused copy rows.

Generated dispatch and mounting in DatasetPlansPage remain blocked on the actual
corrected I3 candidate. The current 0.6.0 manifest/lock/provenance are untouched.
No old two-step tarball, handwritten generated member or raw-endpoint substitute
was used. Published registry SDK before integration remains a separate dependency.

## D3 checks and history

The final lead help clarification adds the explicit fact that cleanup does not
start when normal transfer cannot preserve a snapshot. Only the English/Czech
help strings and their rendered-help assertion changed after the complete D3
quick/34-test batch. Catalog parity and both EN/CS rendered cases were refreshed
and passed: [catalog log](i4-logs/d3-copy-i18n.log),
[render log](i4-logs/d3-copy-render.log). The same unpublished commit was amended;
no source behavior changed and no SDK-dependent work resumed.

- `npm test -- src/lib/api/datasets.test.ts src/pages/app/datasets/DatasetBackupCleanup.test.tsx src/pages/app/datasets/DatasetPlansPage.test.tsx`:
  passed, 3 files / 34 tests, [log](i4-logs/d3-unit.log).
- `npm run ci:quick`: passed on corrected source, including all required audits
  and application/tooling/E2E/BFF core types, [log](i4-logs/d3-ci-quick.log).
- `npm run audit:design-docs`: passed, 298 documents / 76 requirements,
  [log](i4-logs/d3-design-docs.log). Inventory remains 270 routes / 79 modules.
- `git diff --check`: passed. Required Nix shell and configured contributor
  identity were used for the amendment; no hooks were bypassed.
- The initial mutation audit found asynchronous preflight reading route/form
  closures. Fixed it by capturing dataset ID, object reference, label and options
  as immutable mutation variables; final ci:quick reports zero mutation warnings.
  [Initial finding](i4-logs/d3-mutation-preflight-finding.log).

Owning project docs were corrected in place: requirements/evidence, workflows,
action contract, SDK dependency contract and the dated work log. They describe
ordinary task behavior and the remaining SDK gap. KB impact stays as recorded
below; there are no new KB writes, screenshots or deployment claims.

No migrations, backend edits, dependency-pin streams, externally consumed state
or supported D2 boundary exist. The single current commit contains the corrected
approach, with earlier exact range/check evidence retained below. Full SDK-backed
adapter and mounted-page checks, full suite/build, final whole-branch independent
review, then browser/captures remain outstanding. Long checks and publication stay
held for that review checkpoint.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-25-backup-disable-design/

---

# Historical D2 preparation evidence

Status: **parked on I3 candidate SDK; package incomplete**. Implementer3 retains
follow-up ownership. This is a preparation checkpoint, not a final review request,
branch-readiness claim or integration approval.

- Repository: `git@github.com:vpsfreecz/vpsadmin-webui.git`.
- Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-25-backup-disable-design/vpsadmin-webui`.
- Branch: `dev/disable-backups`.
- Fresh fetched base: `e311b1c0af0f50fa4c6f6ce83c514c1a866eb042` (`origin/main`).
- Local preparation head: `b144054198c467b4e4a25a9d1521973a673a77ec`.
- Complete current series: one commit, `b1440541 storage: prepare administrator backup cleanup`.
- Current diffstat: 17 files, 969 insertions, 5 deletions. No backend source edits.
- Worktree clean after commit. Feature branch not pushed; no PR or CI run created.

## Delivered preparation and limits

Shared plan-removal explanation appears beside the list and in its confirmation,
using lead-owned English/Czech copy. The VPS root card uses the real plans route
in the current app/admin context, with `recursive=true` for the existing subtree.
The prepared shared cleanup component gates on actual administrator identity and
permission-filtered description, works with no plans, defaults preservation on,
explains target/time/no-new-snapshot/loss/scope facts, and handles preservation and
cleanup separately. The helper limits mutation submissions to start and one
continuation; preservation requires a known successful action-state receipt plus
the exact preservation chain in `done`. Unknown or failed outcomes and literal
`retry-needed:` rejection stop the workflow. Page exit prevents continuation.
A durable local guard spans both phases. Malformed output preserves its receipt
and tracks a usable task ID, with explicit task review before unlocking. Completion
waits for fresh dataset/plans/snapshots/active-task reads.

**The component is intentionally not yet mounted in DatasetPlansPage.** Its SDK
submission function and final page wiring depend on generated members, so no new
raw endpoint or handwritten generated declaration was introduced. The current
manifest/lock/provenance remain the existing registry SDK 0.6.0 input. I3 owner
implementer2 confirmed that final export waits for committed I1, shared export
checkout cleanliness after I2, and lead source release. Their TS baseline is
`b619eb8324bfe80c7b225f698fb83efe97639c83`; HaveAPI generator is
`1ef9b204ba45bb261d3334be5c555cc1856b713b`. They will supply a validated tarball
with complete input provenance. A published SDK release remains required before
UI integration and is separately authorized.

I1's observed wire envelope is `response.dataset` plus
`response._meta.action_state_id`; the generated SDK owns unwrapping. App-facing
normalization consumes SDK `data`/`meta`. Retry-needed is the API message prefix,
not an invented error-code field.

## Checks and evidence

All commands used the repository's locked `nix develop` environment. Node/npm
selection passed `env:locked` (24.21.0/11.19.0). The locked terminology source was
vpsAdmin `a65a4dfeb92a59df4a80a737a20bcbf8558793ff`. Required hook-framework
inspection found no declared hook framework, active non-sample hook or hooksPath.
Configured author/committer identity was verified before the Nix-shell commit.
No hooks were bypassed.

| Command | Result | Log |
| --- | --- | --- |
| `npm ci` | Passed | Temporary install log; no dependency edits |
| `npm run ci:quick` | Passed: toolchain, docs, lint/format, i18n, CSP, page/structural/component/overlay/lookup/barrel/string/mutation audits; application/tooling/E2E/BFF core types | [ci-quick.log](i4-logs/ci-quick.log) |
| `npm test -- src/lib/api/datasets.test.ts src/pages/app/datasets/DatasetBackupCleanup.test.tsx src/pages/app/datasets/DatasetBackupCleanupWorkflow.test.ts src/pages/app/datasets/DatasetPlansPage.test.tsx` | Passed, 4 files / 52 tests after final source changes | [unit.log](i4-logs/unit.log) |
| `npm run typecheck` | Passed after final source changes | [typecheck.log](i4-logs/typecheck.log) |
| `npm run audit:mutations:check` | Passed after final control changes | [mutations.log](i4-logs/mutations.log) |
| `npm run audit:ui-strings:check` | Passed after final control changes | [ui-strings.log](i4-logs/ui-strings.log) |
| `npm run docs:inventory` | Passed; inventory unchanged, 270 routes / 79 API modules | Same baseline inventory |
| `npm run audit:design-docs` | Passed after final docs, 298 documents / 76 requirements | [design-docs.log](i4-logs/design-docs.log) |
| `git diff --check` | Passed | No whitespace errors |

ci:quick preceded the final role/drift/receipt-render refinements; affected focused
tests, application types and mutation/string audits were refreshed afterwards.
The last documentation update received its own docs audit. No long browser or
integration test was run; no screenshots, real API certification or deployment
proof exists. Full unit suite/build, final quick checks against the real candidate,
independent whole-branch review, then browser tests/captures remain outstanding.
Uncertain-duration full-suite/build/browser checks require a fresh watcher; lead
coordinates the review/publication checkpoint before browser CI is launched.

## Documentation placement inventory

| Topic / reader | Authoritative location | Evidence / limitation |
| --- | --- | --- |
| Plan removal and cleanup interaction / UI maintainers | `docs/design/WORKFLOWS.md`, `ACTION_CONTRACTS.md` | Prepared component and 52 focused tests |
| Product acceptance / reviewers | `REQUIREMENTS.md` REQ-011/024/048 and `EVIDENCE_MATRIX.md` | Preparation only; SDK/browser gap explicit |
| Generated SDK compatibility / maintainers | `docs/design/HAVEAPI_CLIENT.md` | Required generated member/release gate recorded; input unchanged |
| Implementation chronology, verification, KB impact / maintainers | `docs/work-log/2026-11-25-disable-backups.md` | Source/fixture evidence distinguished from deployed behavior |
| Exact heads, current dependency and individual evidence / session lead | This record and state.md | No rollout executed |

The canonical KB workflow was read. Current `backups.vps.open` and
`backups/vps-backups` bindings reference PHP sources, not React. Relevant pages:
Czech `navody:vps:zalohy`, `navody:vps:obnova_webu_zo_zalohy`,
`navody:vps:exporty`; English `manuals:vps:backups`, `manuals:vps:exports`,
`manuals:vps:vpsadminos:storage`. I2 owns changed PHP landmarks. React requires
EN/CS desktop/mobile captures after wiring and independent review. No production
KB write or staging claim was made. The only terminology adjustment to lead copy
was “poddatasety” → locked “vnořené datasety”, already reported to lead.

## History and next dependency

No migrations, dependency-pin update streams, source release, deployment or
externally consumed state exist in this branch. Original base history is intact;
its sole preparation commit has no superseded approach to consolidate currently.
The eventual complete branch still requires independent whole-history and
no-migration conclusions. No merge/deploy/lifecycle operation is authorized.

Next: implementer2 supplies the validated SDK candidate; implementer3 implements
the generated adapter and page wiring, adds serialization/whole-page/browser
coverage, updates SDK provenance and docs, completes quick checks and commits,
then reports the final complete range for lead-owned independent review. Feature
publication and repository-required draft PR are held for that checkpoint.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-25-backup-disable-design/
